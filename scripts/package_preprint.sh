#!/usr/bin/env bash
# package_preprint.sh - Build the Preprints.org submission archive.
#
# Preprints.org requires LaTeX submissions as an archive containing every file
# needed to recreate the PDF. This packages the .tex, the MDPI class files in
# Definitions/, and the figures.
#
# There is no .bib file: the bibliography is inline (thebibliography), so the
# .tex is self-contained for references.
#
# Output: preprint/IAKM_Preprints_submission.zip
set -euo pipefail

cd "$(dirname "$0")/.."

OUT="IAKM_Preprints_submission.zip"

cd preprint

if [ ! -f IAKM_Preprints.tex ]; then
    echo "[ERROR] IAKM_Preprints.tex not found" >&2
    exit 1
fi

rm -f "$OUT"

# Everything needed for a clean-room rebuild. The built PDF is included so the
# editorial office can compare against their own compile.
FILES=(
    IAKM_Preprints.tex
    Definitions
    fig1_three_senses_of_location_print.pdf
    fig2_timing_coverage_plane_print.pdf
    fig3_gradient_stays_a_vector_print.pdf
    fig4_collection_stage_print.pdf
    fig5_future_work_print.pdf
)

for f in "${FILES[@]}"; do
    if [ ! -e "$f" ]; then
        echo "[ERROR] missing required file: $f" >&2
        exit 1
    fi
done

if [ -f IAKM_Preprints.pdf ]; then
    FILES+=(IAKM_Preprints.pdf)
else
    echo "[WARN] IAKM_Preprints.pdf not present; archiving source only." >&2
fi

# -x excludes build artifacts that may be sitting in the directory.
zip -q -r "$OUT" "${FILES[@]}" \
    -x "*.aux" "*.log" "*.out" "*.synctex.gz" "*.spl" "*.bbl" "*.blg" "*.toc" "*.loe"

echo "[OK] preprint/$OUT"
unzip -l "$OUT" | tail -n +2
