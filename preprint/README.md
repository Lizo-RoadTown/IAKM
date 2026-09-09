# Preprints.org submission version

This directory holds the [Preprints.org](https://www.preprints.org/) submission
build of the IAKM methodology paper.

**The body prose, tables, and references are identical to the IEEE conference
version in [`../paper_v7/`](../paper_v7/).** Only the container differs: the
IEEE two-column layout becomes MDPI's single-column preprint layout, and the
front and back matter use MDPI's required commands.

Because the two `.tex` files share their content but not their markup, **a
change to the paper has to be made in both.** There is no generator that keeps
them in sync.

## Building

```sh
# Windows
scripts\build_preprint.bat

# Linux / macOS
./scripts/build_preprint.sh
```

Output: `IAKM_Preprints.pdf`.

## Before submitting

The back matter carries `TODO(author)` placeholders that Preprints.org requires
and that cannot be filled in from the manuscript:

- `\funding` — funder and grant number, or an explicit statement of none
- `\institutionalreview` — the IRB determination for the reference
  implementation, which was deployed on a university program, or an explicit
  "Not applicable" if it was not human subjects research
- `\informedconsent` — consent position, or "Not applicable"
- `\dataavailability` — where the verified records can be obtained

Also note: **the abstract runs 258 words.** MDPI asks for about 200 maximum. It
will likely need trimming.

To remove the line numbers from the margins, change `submit` to `accept` in the
`\documentclass` options. Keep `submit` while the manuscript is under review.

## Third-party files

`Definitions/` contains the MDPI LaTeX class and bibliography styles, taken
from the official Preprints.org template. **Those files are MDPI's, not part of
this project, and are not covered by this repository's licenses.** They are
included so the paper builds from a clean checkout. See [`../NOTICE`](../NOTICE).
