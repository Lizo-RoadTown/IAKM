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

# README.txt and FORM_FIELDS.txt come from one script, so the Windows
# and POSIX paths produce identical folders.
python scripts/write_submission_docs.py "$OUT"

echo "[4/4] assembled"
echo
echo "=== $OUT/ ==="
ls -la "$OUT" | tail -n +2 | awk '{printf "  %10s  %s\n", $5, $9}'
