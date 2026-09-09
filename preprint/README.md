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

Output: `IAKM_Preprints.pdf` (14 pages).

> If the build reports `I can't write on file`, the PDF is open in a viewer.
> Close it and rerun.

## Packaging for submission

Preprints.org requires LaTeX submissions as an archive containing every file
needed to recreate the PDF.

```sh
# Windows
scripts\package_preprint.bat

# Linux / macOS
./scripts/package_preprint.sh
```

Output: `IAKM_Preprints_submission.zip` — the `.tex`, `Definitions/`, the five
figures, and the built PDF. There is no `.bib` file; the bibliography is inline
(`thebibliography`), so the `.tex` is self-contained for references.

The archive has been verified by extracting it into an empty directory and
compiling from scratch: 14 pages, no errors, no missing files.

## Submission requirements

Checked against the Preprints.org author guidance.

### Met

| Requirement | Status |
| --- | --- |
| Preprints.org template used | Yes — MDPI class, `preprints` journal option |
| Title on first page | Yes |
| Author list on first page | Yes |
| Abstract on first page | Yes |
| Keywords on first page | Yes |
| Corresponding author contact details on first page | Yes |
| Affiliation on first page | Present, but see below |
| No publisher or journal logos or names | Verified: zero occurrences of MDPI, Preprints, or any logo image in the PDF |
| Comprehensive bibliography | 13 references, all verified against publisher or Crossref records |
| LaTeX submitted as a complete archive | `scripts/package_preprint.*`, clean-room verified |

Note on the class option: `moreauthors` is used rather than `oneauthor`, even
though there is one author. `mdpi.cls` suppresses the `\corres` correspondence
line entirely under `oneauthor`, and Preprints.org requires corresponding
author contact details on the first page.

### Still needed from the author

1. **Back matter statements.** Four `TODO(author)` placeholders in the `.tex`:
   - `\funding` — funder and grant number, or an explicit statement of none
   - `\institutionalreview` — the IRB determination for the reference
     implementation, which was deployed on a university program involving
     people, or an explicit "Not applicable" with rationale
   - `\informedconsent` — consent position, or "Not applicable"
   - `\dataavailability` — where the verified records can be obtained

2. **Institutional email.** Preprints.org asks for an institutional address
   (e.g. a university one) or an address used in previously published papers,
   to help with author identification. The manuscript currently carries a
   Gmail address.

3. **Affiliation.** The address line reads "Pomona, CA, USA" — a location, not
   an institution. If there is an institutional affiliation, it belongs here.

4. **ORCID.** Recommended by the venue. A commented `\orcidauthorA` placeholder
   is in the `.tex`; fill it in and append `\orcidA{}` after the author name.

5. **Abstract length.** 258 words against MDPI's ~200 guidance. Needs trimming.

6. **Graphical abstract.** Recommended, as JPG or PNG. A screenshot of the
   textual abstract does not qualify and will be removed by the editorial
   office. Figure 1 (three senses of location) or Figure 2 (timing and coverage
   plane) is the most likely basis, exported to PNG.

7. **Bibliography recency.** The venue asks for a bibliography "showing
   relevance to recent research." The current list runs 1962–2023 with only one
   reference from the last five years. For a paper whose contribution depends
   on AI-assisted analysis of work artifacts, the absence of recent literature
   in that area is likely to be noticed.

8. **Article structure.** The venue requires IMRaD structure (introduction,
   methods, results, discussion) *if reporting original experimental research*.
   This paper is a methodology paper with a reference implementation, and it
   states plainly that it is at the collection stage with reproducibility and
   validity untested. The 11-section thematic structure is probably defensible
   on that basis, but the deployment run in Section 7 does report figures, so
   it is worth a deliberate decision rather than an assumption.

To remove the line numbers from the margins, change `submit` to `accept` in the
`\documentclass` options. Keep `submit` while the manuscript is under review.

## Third-party files

`Definitions/` contains the MDPI LaTeX class and bibliography styles, taken
from the official Preprints.org template. **Those files are MDPI's, not part of
this project, and are not covered by this repository's licenses.** They are
included so the paper builds from a clean checkout. See [`../NOTICE`](../NOTICE).
