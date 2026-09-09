#!/usr/bin/env bash
# build_paper_v7.sh - Build the IAKM v7 paper (IEEE conference format)
#
# POSIX counterpart to build_paper_v7.bat, for TeX Live on Linux/macOS.
# Requires: pdflatex with the IEEEtran class (texlive-publishers on Debian
# and Ubuntu; the full TeX Live or MacTeX install on macOS).
#
# IMPORTANT: paper_v7/IAKM_PAPER_V7_IEEE.tex is the hand-maintained source
# of record for the PDF. It is tuned by hand against
# paper_v7/IAKM_V7_FLOAT_PLACEMENT.md (float environments, caption sides,
# in-text callouts). Do NOT regenerate it from the markdown draft; the
# converter would discard that placement work.
set -euo pipefail

cd "$(dirname "$0")/.."

TEX="IAKM_PAPER_V7_IEEE.tex"
DIR="paper_v7"
BASE="IAKM_PAPER_V7_IEEE"
PUBLIC="IAKM_Public.pdf"

echo "=== IAKM v7: IEEE conference ==="

if ! command -v pdflatex >/dev/null 2>&1; then
    echo "[ERROR] pdflatex not found. Install TeX Live (with IEEEtran)." >&2
    exit 1
fi

if [ ! -f "$DIR/$TEX" ]; then
    echo "[ERROR] Not found: $DIR/$TEX" >&2
    exit 1
fi

# Compile from the .tex's own directory so the relative figure paths resolve.
cd "$DIR"

# Two passes to resolve cross-references.
for pass in 1 2; do
    echo "[$pass/2] pdflatex..."
    if ! pdflatex -interaction=nonstopmode "$TEX" >/dev/null 2>&1; then
        echo "[ERROR] Pass $pass failed; rerunning to show the error:" >&2
        pdflatex -interaction=nonstopmode "$TEX" || true
        exit 1
    fi
done

# Publish under the distribution name used for release/DOI.
cp "$BASE.pdf" "$PUBLIC"

# Clean build artifacts.
rm -f "$BASE".{aux,log,out,synctex.gz,spl,bbl,blg,toc}

echo "[OK] $DIR/$PUBLIC"
