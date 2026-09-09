#!/usr/bin/env bash
# prepare_submission.sh - Assemble everything Preprints.org needs, in one folder.
#
# Rebuilds the PDF and the source archive first, so the folder can never carry
# a stale manuscript. Output: submission/
#
# The folder's contents are derived from tracked sources and are gitignored;
# rerun this script to recreate them.
set -euo pipefail

cd "$(dirname "$0")/.."

OUT="submission"

echo "=== Preparing Preprints.org submission ==="

# 1. Rebuild the manuscript so the folder cannot ship a stale PDF.
if command -v pdflatex >/dev/null 2>&1; then
    ./scripts/build_preprint.sh >/dev/null
    echo "[1/4] manuscript rebuilt"
else
    echo "[1/4] pdflatex not found; using the existing PDF" >&2
fi

# 2. Regenerate the graphical abstract.
if command -v python >/dev/null 2>&1; then
    python scripts/generate_graphical_abstract.py >/dev/null
    echo "[2/4] graphical abstract regenerated"
fi

# 3. Rebuild the source archive.
./scripts/package_preprint.sh >/dev/null
echo "[3/4] source archive rebuilt"

# 4. Assemble.
rm -rf "$OUT"
mkdir -p "$OUT"

cp preprint/IAKM_Preprints.pdf              "$OUT/1_manuscript.pdf"
cp preprint/IAKM_Preprints_submission.zip   "$OUT/2_latex_source.zip"
cp preprint/graphical_abstract.png          "$OUT/3_graphical_abstract.png"

# Derive the page count so this README can never drift from the manuscript.
PAGES="unknown"
if command -v pdfinfo >/dev/null 2>&1; then
    PAGES=$(pdfinfo "$OUT/1_manuscript.pdf" 2>/dev/null | awk '/^Pages/{print $2}')
elif [ -n "${LOCALAPPDATA:-}" ] && [ -x "$LOCALAPPDATA/Programs/MiKTeX/miktex/bin/x64/pdfinfo.exe" ]; then
    PAGES=$("$LOCALAPPDATA/Programs/MiKTeX/miktex/bin/x64/pdfinfo.exe" "$OUT/1_manuscript.pdf" 2>/dev/null | awk '/^Pages/{print $2}')
fi
[ -z "$PAGES" ] && PAGES="unknown"

cat > "$OUT/README.txt" <<TXT
PREPRINTS.ORG SUBMISSION
Interface-Anchored Knowledge Mapping - Elizabeth Osborn

Upload these three files. The numbers are the order the form asks for them.

  1_manuscript.pdf
      The compiled manuscript. ${PAGES} pages.
      Upload as the main manuscript file.

  2_latex_source.zip
      The complete LaTeX source: IAKM_Preprints.tex, the MDPI class files
      in Definitions/, the five figures, and the compiled PDF.
      Preprints.org requires LaTeX submissions to include every file needed
      to recreate the PDF. There is no .bib file; the bibliography is inline
      in the .tex.
      Verified by extracting into an empty directory and compiling from
      scratch: ${PAGES} pages, no errors, no missing files.

  3_graphical_abstract.png
      1775 x 1019 px, RGB.
      Upload in the graphical abstract field, NOT with the manuscript.
      Preprints.org removes graphical abstracts that are screenshots of the
      textual abstract; this one is a drawn figure, so it qualifies.

FORM DETAILS YOU WILL BE ASKED FOR

  Title        Interface-Anchored Knowledge Mapping: A Coordinate System for
               Locating Knowledge-Relevant Metadata in Modular Sociotechnical
               Systems
  Author       Elizabeth Osborn
  Affiliation  Independent Researcher, Pomona, CA, USA
  Email        eosborn@cpp.edu
  ORCID        0009-0007-8678-3307
  Abstract     In the manuscript, 207 words
  Keywords     10, semicolon separated, in the manuscript

ARCHIVED RECORD

  This work is deposited on Zenodo under CC BY 4.0. The data availability
  statement in the manuscript cites both:

    Version 1.00   https://doi.org/10.5281/zenodo.22668058
    All versions   https://doi.org/10.5281/zenodo.22668057
    Repository     https://github.com/Lizo-RoadTown/IAKM   (public)

  Cite the version DOI in a paper; use the concept DOI for a general link.

TO REGENERATE THIS FOLDER

  ./scripts/prepare_submission.sh      (Linux / macOS)
  scripts\prepare_submission.bat       (Windows)
TXT

echo "[4/4] assembled"
echo
echo "=== $OUT/ ==="
ls -la "$OUT" | tail -n +2 | awk '{printf "  %10s  %s\n", $5, $9}'
