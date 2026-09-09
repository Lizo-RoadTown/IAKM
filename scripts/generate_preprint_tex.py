"""Regenerate the Preprints.org .tex from the IEEE conference .tex.

Run this after any change to paper_v7/IAKM_PAPER_V7_IEEE.tex. The IEEE
.tex is the single source of prose, tables, and references; this script
rebuilds the MDPI-formatted preprint from it.

WARNING: this OVERWRITES preprint/IAKM_Preprints.tex. Never hand-edit
that file - edit the IEEE .tex and rerun this.


Body prose, tables, and references are carried over verbatim. Only the
container changes: IEEEtran two-column floats become single-column MDPI
floats, and the front/back matter is rebuilt to MDPI's required commands.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SRC = Path(r"C:\Users\Liz\IAKM\paper_v7\IAKM_PAPER_V7_IEEE.tex")
OUT = Path(r"C:\Users\Liz\IAKM\preprint\IAKM_Preprints.tex")

src = SRC.read_text(encoding="utf-8")

# ---------------------------------------------------------------- extraction
def between(start, end, text):
    i = text.index(start) + len(start)
    j = text.index(end, i)
    return text[i:j].strip()

abstract = between(r"\begin{abstract}", r"\end{abstract}", src)
keywords = between(r"\begin{IEEEkeywords}", r"\end{IEEEkeywords}", src)
body = between(r"\end{IEEEkeywords}", r"\begin{thebibliography}{99}", src)
bib = between(r"\begin{thebibliography}{99}", r"\end{thebibliography}", src)

# The abstract is one block in MDPI: no blank lines allowed inside \abstract{}.
abstract = re.sub(r"\n\s*\n", " ", abstract)
abstract = re.sub(r"\s+", " ", abstract).strip()
keywords = re.sub(r"\s+", " ", keywords).strip().rstrip(".")
# MDPI separates keywords with semicolons, not commas.
keywords = "; ".join(k.strip() for k in keywords.split(","))

# ------------------------------------------------------------ body transform
# Preprints.org is single column, so starred (page-wide) floats become plain.
body = body.replace(r"\begin{table*}", r"\begin{table}")
body = body.replace(r"\end{table*}", r"\end{table}")
body = body.replace(r"\begin{figure*}", r"\begin{figure}")
body = body.replace(r"\end{figure*}", r"\end{figure}")

# IEEE float placement specifiers do not apply here; MDPI uses [H] throughout.
body = re.sub(r"(\\begin\{(?:table|figure)\})\[[^\]]*\]", r"\1[H]", body)

# Figures sit at full text width in one column.
body = body.replace(r"\includegraphics[width=0.70\textwidth]",
                    r"\includegraphics[width=\textwidth]")
body = body.replace(r"\includegraphics[width=0.86\textwidth]",
                    r"\includegraphics[width=\textwidth]")
body = body.replace(r"\includegraphics[width=0.78\textwidth]",
                    r"\includegraphics[width=\textwidth]")

body = body.strip()

# ------------------------------------------------------------ bib transform
# IEEEtran keys stay; only the \bibitem form changes to MDPI's labelled form.
bib = bib.strip()

# ------------------------------------------------------------------- assemble
doc = r"""%  Interface-Anchored Knowledge Mapping
%  Preprints.org submission source, built on the MDPI preprints template.
%  Body prose, tables, and references are identical to the IEEE conference
%  version in ../paper_v7/. Only the container differs.
%
%  Build:  pdflatex IAKM_Preprints   (run twice to resolve \ref)

% NOTE: "moreauthors" rather than "oneauthor" is deliberate. mdpi.cls
% suppresses the \corres correspondence line entirely under "oneauthor"
% (see the \@authornum test in \maketitlen), and Preprints.org requires
% corresponding author contact details on the first page.
\documentclass[preprints,article,submit,moreauthors]{Definitions/mdpi}

%=================================================================
\firstpage{1}
\makeatletter
\setcounter{page}{\@firstpage}
\makeatother
\pubvolume{1}
\issuenum{1}
\articlenumber{0}
\pubyear{2026}
\copyrightyear{2026}
\datereceived{ }
\dateaccepted{ }
\datepublished{ }

%=================================================================
% Prose-heavy tables read better top-aligned than vertically centred.
\renewcommand{\tabularxcolumn}[1]{>{\raggedright\arraybackslash}p{#1}}

% W{w} is an X column with a relative width. Per-table weights must sum to the
% number of columns, so a narrow key column buys width for a prose column.
\newcolumntype{W}[1]{>{\hsize=#1\hsize\raggedright\arraybackslash}X}

%=================================================================
\Title{Interface-Anchored Knowledge Mapping: A Coordinate System for
Locating Knowledge-Relevant Metadata in Modular Sociotechnical Systems}

\newcommand{\orcidauthorA}{0009-0007-8678-3307}

\Author{Elizabeth Osborn *\orcidA{}}

\AuthorNames{Elizabeth Osborn}

% Submitted as an independent researcher, not under an institutional
% affiliation. The personal address is therefore the correct contact.
\address{%
$^{1}$ \quad Independent Researcher, Pomona, CA, USA; eosborn@cpp.edu}

\corres{Correspondence: eosborn@cpp.edu}

\abstract{ABSTRACT_HERE}

\keyword{KEYWORDS_HERE}

%=================================================================
\begin{document}

BODY_HERE

%=================================================================
\funding{This research received no external funding.}

% The ingest step reads repositories, issues, reviews, documents, logs, wikis,
% and meeting records as they already exist; teams are not asked to author
% anything for the map, and no intervention is applied to any person. The work
% is therefore not human subjects research.
\institutionalreview{Not applicable. This study did not involve an
intervention on human participants. Knowledge-relevant metadata was recovered
from digital work artifacts that already existed, and no data was collected
from participants for the purpose of this study.}

\informedconsent{Not applicable.}

\dataavailability{The manuscript source, figures, and methodology
documentation are archived at \url{https://doi.org/10.5281/zenodo.22668058}
and maintained at \url{https://github.com/Lizo-RoadTown/IAKM}. The verified map records
produced by the reference implementation describe the knowledge of
identifiable individuals within a specific program and are therefore not
publicly available. The record format, coordinate system, and verification
procedure are fully specified in this paper, so the collection is
reproducible independently of that store.}

\conflictsofinterest{The author declares no conflicts of interest.}

%=================================================================
\isAPAandChicago{}{%
\begin{thebibliography}{999}

BIB_HERE

\end{thebibliography}
}

\end{document}
"""

doc = doc.replace("ABSTRACT_HERE", abstract)
doc = doc.replace("KEYWORDS_HERE", keywords)
doc = doc.replace("BODY_HERE", body)
doc = doc.replace("BIB_HERE", bib)

OUT.write_text(doc, encoding="utf-8")

# ------------------------------------------------------------------- report
print(f"wrote {OUT}  ({len(doc.splitlines())} lines)")
print(f"  abstract words : {len(abstract.split())}")
print(f"  keywords       : {keywords.count(';') + 1}")
print(f"  sections       : {doc.count(chr(92) + 'section{')}")
print(f"  tables         : {doc.count(chr(92) + 'begin{table}')}")
print(f"  figures        : {doc.count(chr(92) + 'begin{figure}')}")
print(f"  bibitems       : {doc.count(chr(92) + 'bibitem{')}")
print(f"  starred floats left (must be 0): "
      f"{doc.count(chr(92) + 'begin{table*}') + doc.count(chr(92) + 'begin{figure*}')}")
