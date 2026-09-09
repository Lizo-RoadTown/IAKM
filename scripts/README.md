# Build Scripts

## First-Time Setup

1. **Install MiKTeX** (if not already): https://miktex.org/download
2. **Run setup once** in a terminal:
   ```
   scripts\setup_latex_env.bat
   ```
   This adds MiKTeX to your PATH and enables auto-install of missing LaTeX packages.

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
