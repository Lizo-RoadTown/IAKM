#!/usr/bin/env bash
# build_preprint.sh - Build the Preprints.org submission version
#
# POSIX counterpart to build_preprint.bat, for TeX Live on Linux/macOS.
#
# Target venue: Preprints.org (MDPI). Uses the MDPI class in
# preprint/Definitions/, which ships with the Preprints.org LaTeX template.
#
# Body prose, tables, and references are identical to the IEEE conference
# version in paper_v7/. Only the container differs, so a change to the paper
# must be made in BOTH .tex files.
set -euo pipefail

cd "$(dirname "$0")/.."

TEX="IAKM_Preprints.tex"
DIR="preprint"
BASE="IAKM_Preprints"

echo "=== IAKM: Preprints.org submission ==="

if ! command -v pdflatex >/dev/null 2>&1; then
    echo "[ERROR] pdflatex not found. Install TeX Live." >&2
    exit 1
fi

if [ ! -f "$DIR/$TEX" ]; then
    echo "[ERROR] Not found: $DIR/$TEX" >&2
    exit 1
fi

# Compile from the .tex's own directory so Definitions/ and the figure paths
# resolve.
cd "$DIR"

for pass in 1 2; do
    echo "[$pass/2] pdflatex..."
    pdflatex -interaction=nonstopmode "$TEX" >/dev/null 2>&1 || true
done

if [ ! -f "$BASE.pdf" ]; then
    echo "[ERROR] No PDF produced; rerunning to show the error:" >&2
    pdflatex -interaction=nonstopmode "$TEX" || true
    exit 1
fi

echo "[OK] $DIR/$BASE.pdf"

rm -f "$BASE".{aux,log,out,synctex.gz,spl,bbl,blg,toc,loe}
echo "[OK] Build artifacts cleaned."
