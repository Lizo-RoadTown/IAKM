# Build Scripts

## First-Time Setup

1. **Install MiKTeX** (if not already): https://miktex.org/download
2. **Run setup once** in a terminal:
   ```
   scripts\setup_latex_env.bat
   ```
   This adds MiKTeX to your PATH and enables auto-install of missing LaTeX packages.

## Papers

| Script | Builds |
|---|---|
| `build_paper_v7.bat` / `.sh` | Methodology paper, IEEE conference format -> `paper_v7/IAKM_Public.pdf` |
| `build_preprint.bat` / `.sh` | Preprints.org submission, MDPI format -> `preprint/IAKM_Preprints.pdf` |

Both papers share their prose, tables, and references but have separate `.tex`
sources. A change to the paper must be made in both.

## Submitting

```
scripts\prepare_submission.bat     # Windows
./scripts/prepare_submission.sh    # Linux / macOS
```

Rebuilds the manuscript, the graphical abstract, and the LaTeX source archive,
then assembles `submission/` with the three files Preprints.org asks for and a
README naming which field each one goes in. The folder is gitignored because
everything in it is derived; rerun the script to recreate it.

## Tools

- `compile_tex.bat` - Compiles any `.tex` to PDF (two passes, cleans artifacts)
  ```
  scripts\compile_tex.bat paper_v7\IAKM_PAPER_V7_IEEE.tex
  ```
- `clean_grammar.py` - Fixes em dashes and contractions in any `.md` file
  ```
  python scripts\clean_grammar.py paper_v7\IAKM_PAPER_V7_DRAFT-1.md
  ```
- `convert_paper_md_to_tex.py` - Converts a paper `.md` to `.tex`
- `generate_figure2_collapsing.py` - Regenerates figure 2
- `setup_latex_env.bat` - Adds MiKTeX to PATH, enables auto-install

## Workflow

1. Edit the `.md` file in `paper_v7\`
2. Regenerate the `.tex` from the updated `.md`
3. Compile: `scripts\compile_tex.bat paper_v7\IAKM_PAPER_V7_IEEE.tex`
4. Check the PDF output

The grammar cleaner is not run automatically; invoke it on the `.md` when needed.
If you change the `.md` content, the `.tex` needs to be regenerated.
