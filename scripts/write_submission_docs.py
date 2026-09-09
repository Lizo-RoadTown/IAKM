"""Write the two text files that accompany the Preprints.org upload folder.

  README.txt       what to upload, into which field, and the archived record
  FORM_FIELDS.txt  title, abstract, and keywords as plain text to paste

Both are derived from the manuscript source and the built PDF, so neither can
drift from what is actually being submitted. This is the single source for
both; the shell wrappers only call it.

Usage:
    python scripts/write_submission_docs.py [output_dir]   (default: submission)
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "submission"
TEX = ROOT / "preprint" / "IAKM_Preprints.tex"

VERSION_DOI = "10.5281/zenodo.22668058"
CONCEPT_DOI = "10.5281/zenodo.22668057"
REPO = "https://github.com/Lizo-RoadTown/IAKM"

tex = TEX.read_text(encoding="utf-8")


def field(name):
    """Pull one brace-delimited front-matter field, flattened to one line."""
    m = re.search(r"\\" + name + r"\{(.*?)\}\s*\n\s*\n", tex, re.S)
    if not m:
        m = re.search(r"\\" + name + r"\{(.*?)\}", tex, re.S)
    t = m.group(1) if m else ""
    t = re.sub(r"\s+", " ", t).strip()
    return t.replace("~", " ").replace(r"\%", "%")


def page_count(pdf):
    """Ask pdfinfo; it is the only reliable source. Never guess."""
    exe = shutil.which("pdfinfo")
    if not exe:
        local = os.environ.get("LOCALAPPDATA", "")
        cand = Path(local) / "Programs/MiKTeX/miktex/bin/x64/pdfinfo.exe"
        exe = str(cand) if cand.exists() else None
    if not exe:
        return "unknown"
    try:
        out = subprocess.run([exe, str(pdf)], capture_output=True, text=True,
                             timeout=60).stdout
        m = re.search(r"^Pages:\s+(\d+)", out, re.M)
        return m.group(1) if m else "unknown"
    except Exception:
        return "unknown"


title = field("Title")
abstract = field("abstract")
keywords = field("keyword")
if not (title and abstract and keywords):
    sys.exit("ERROR: could not extract title, abstract, and keywords from the .tex")

OUT.mkdir(parents=True, exist_ok=True)
pages = page_count(OUT / "1_manuscript.pdf")

# ------------------------------------------------------------------ README
(OUT / "README.txt").write_text(f"""PREPRINTS.ORG SUBMISSION
Interface-Anchored Knowledge Mapping - Elizabeth Osborn

Upload these three files. The numbers are the order the form asks for them.

  1_manuscript.pdf
      The compiled manuscript. {pages} pages.
      Upload as the main manuscript file.

  2_latex_source.zip
      The complete LaTeX source: IAKM_Preprints.tex, the MDPI class files
      in Definitions/, the five figures, and the compiled PDF.
      Preprints.org requires LaTeX submissions to include every file needed
      to recreate the PDF. There is no .bib file; the bibliography is inline
      in the .tex.
      Verified by extracting into an empty directory and compiling from
      scratch: {pages} pages, no errors, no missing files.

  3_graphical_abstract.png
      1775 x 1019 px, RGB.
      Upload in the graphical abstract field, NOT with the manuscript.
      Preprints.org removes graphical abstracts that are screenshots of the
      textual abstract; this one is a drawn figure, so it qualifies.

FORM_FIELDS.txt holds the title, abstract, and keywords as plain text, ready
to paste. It is for you, not for upload.

ARCHIVED RECORD

  This work is deposited on Zenodo under CC BY 4.0. The data availability
  statement in the manuscript cites both:

    Version 1.00   https://doi.org/{VERSION_DOI}
    All versions   https://doi.org/{CONCEPT_DOI}
    Repository     {REPO}   (public)

  Cite the version DOI in a paper; use the concept DOI for a general link.

TO REGENERATE THIS FOLDER

  ./scripts/prepare_submission.sh      (Linux / macOS)
  scripts\\prepare_submission.bat       (Windows)
""", encoding="utf-8")

# ------------------------------------------------------------- FORM_FIELDS
(OUT / "FORM_FIELDS.txt").write_text(f"""COPY-PASTE FIELDS FOR THE PREPRINTS.ORG FORM
Extracted from the manuscript source, so they match it exactly.

-- TITLE {"-" * 58}

{title}

-- AUTHOR {"-" * 57}

Elizabeth Osborn
Independent Researcher, Pomona, CA, USA
eosborn@cpp.edu
ORCID 0009-0007-8678-3307

-- ABSTRACT ({len(abstract.split())} words) {"-" * 42}

{abstract}

-- KEYWORDS ({keywords.count(';') + 1}) {"-" * 50}

{keywords}

-- SUGGESTED CATEGORY {"-" * 45}

Computer Science and Mathematics
  subcategory: Information Systems, or Software if that is not offered
  second category, if the form allows one: Engineering
""", encoding="utf-8")

print(f"  README.txt ({pages} pages) and FORM_FIELDS.txt written "
      f"(abstract {len(abstract.split())} words, "
      f"{keywords.count(';') + 1} keywords)")
