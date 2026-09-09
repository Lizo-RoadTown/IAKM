# IAKM — Interface-Anchored Knowledge Mapping

**A coordinate system for locating knowledge-relevant metadata in modular sociotechnical systems.**

Knowledge loss in sociotechnical systems becomes unrecoverable when the conditions
that made knowledge usable disappear before they are captured. Artifacts survive;
the context that made them intelligible does not. A repository preserves what was
committed without preserving why it was written that way. An organization preserves
roles without preserving the expertise that made those roles functional.

IAKM is a methodology for making that loss **observable before it becomes
unrecoverable**. It does not try to capture knowledge content. It produces a
verified record that *locates* knowledge-relevant metadata against the structure of
the system: who appears to know what, which component it concerns, what evidence
supports the claim, and where the knowledge may still be recoverable.

This repository holds **two papers**: the methodology, and its first
implementation.

| Paper | What it is |
|---|---|
| **[Interface-Anchored Knowledge Mapping](paper_v7/IAKM_Public.pdf)** | The methodology. The recovery record, the five-element coordinate system, the verification procedure, and the standards required for collections to accumulate. |
| **[Observing Knowledge at Structural Interfaces](implementation/Observing_Knowledge_at_Structural_Interfaces.pdf)** | The first implementation. A design case for automated knowledge-capture support built inside a multi-university CubeSat software program: automated extraction, staged review, observability, and a live knowledge graph. |

The methodology paper states what the record must be. The implementation paper
reports what happened when it was built.

## The five-element address

Every IAKM record is addressed by five elements. Two addresses are identical only
when all five match, which is what allows independently produced records of one
system to be differenced.

| Element | Meaning |
|---|---|
| **T1** | Governing field — the methods, vocabulary, and standards of evidence used as the analytical lens |
| **T2** | Domain — the subject area the governing field reaches into |
| **T3** | Interface layer — the structural connection layer exposed by the declared field and domain |
| **C** | Component anchor — the part of the system the metadata concerns |
| **K** | Knower anchor — the person whose knowledge, role, authorship, observation, or responsibility is implicated |

The declared pair (T1, T2) is a **binding**, and the binding determines which
interface layers are visible. Records produced under different bindings still join
through their shared component and knower anchors, without collapsing the layers
each binding exposes. There is no universal set of interface layers and no
canonical ordering across systems.

## Repository contents

```
paper_v7/                       METHODOLOGY PAPER
  IAKM_Public.pdf               Built paper — start here
  IAKM_PAPER_V7_DRAFT.md        Prose source
  IAKM_PAPER_V7_IEEE.tex        Typeset source of record (hand-maintained)
  IAKM_V7_FLOAT_PLACEMENT.md    Float/caption spec the .tex is tuned against
  IAKM_V7_REFERENCES.md         Reference list
  IAKM_CITATION_DIGGING_LIST.md Citation provenance notes
  fig1..fig5_*.pdf              Print-ready figures

preprint/                       PREPRINTS.ORG SUBMISSION
  IAKM_Preprints.tex            Same paper, MDPI single-column (generated)
  graphical_abstract.png        Graphical abstract (generated)
  Definitions/                  MDPI class files (third party; see NOTICE)
  fig1..fig5_*.pdf              Same figures as paper_v7/
  README.md                     Submission checklist

implementation/                 IMPLEMENTATION PAPER
  Observing_Knowledge_at_       Design case, May 2026 (PDF only;
    Structural_Interfaces.pdf   no LaTeX source in this repository)

scripts/                        Build tooling (see scripts/README.md)

LICENSE                         CC BY 4.0, for the papers and documentation
LICENSE-CODE                    Apache 2.0, for scripts/
NOTICE                          Attribution, including third-party files
PATENTS.md                      Patent non-assertion pledge
```

**Start here:** [`paper_v7/IAKM_Public.pdf`](paper_v7/IAKM_Public.pdf) for the
methodology, then
[`implementation/`](implementation/Observing_Knowledge_at_Structural_Interfaces.pdf)
for what building it looked like.

## Building the methodology paper

Requires a LaTeX installation providing the `IEEEtran` class — MiKTeX on Windows,
or TeX Live (`texlive-publishers` on Debian/Ubuntu, MacTeX on macOS).

```sh
# Windows
scripts\build_paper_v7.bat

# Linux / macOS
./scripts/build_paper_v7.sh
```

Both compile `paper_v7/IAKM_PAPER_V7_IEEE.tex` in two passes and write
`paper_v7/IAKM_Public.pdf`.

The implementation paper is distributed as a PDF only; there is no LaTeX source
for it in this repository, so it is not rebuildable here.

A second build of the same methodology paper, formatted for
[Preprints.org](https://www.preprints.org/) submission, lives in
[`preprint/`](preprint/README.md):

```sh
scripts\build_preprint.bat     # Windows
./scripts/build_preprint.sh    # Linux / macOS
```

The preprint `.tex` is **generated** from the IEEE `.tex`, which is the single
source of prose, tables, and references:

```sh
python scripts/generate_preprint_tex.py
```

So edit `paper_v7/IAKM_PAPER_V7_IEEE.tex` and rerun that script. Do not
hand-edit `preprint/IAKM_Preprints.tex` — regenerating overwrites it.

> **Note for contributors:** the `.tex` is the hand-maintained source of record for
> the PDF, tuned against `IAKM_V7_FLOAT_PLACEMENT.md` (float environments, caption
> sides, in-text callouts). Do **not** regenerate it from the markdown draft — the
> markdown is the prose source, and prose changes are ported into the `.tex` by
> hand.

## Using the methodology

The IAKM method is free for anyone to apply. This is worth stating plainly, because
licensing a *methodology* is widely misunderstood:

- **Copyright protects expression, not methods.** Under 17 U.S.C. §102(b),
  copyright does not extend to any "idea, procedure, process, system, method of
  operation, concept, principle, or discovery."
- So the license on this repository governs **copying and redistributing the paper
  and the code**. It does not, and cannot, govern **use of the method**.
- You do not need permission to apply IAKM, build on it, adapt it to your domain,
  or implement it in software. Attribution is asked for when you reuse the text,
  figures, or code, and is the normal scholarly courtesy when you build on the
  method.
- Patents *can* restrict a method where copyright cannot. That door is closed
  here deliberately: see [`PATENTS.md`](PATENTS.md).

If you apply IAKM to a system, the most useful thing you can contribute back is a
collection produced under declared bindings and evidence rules. Section 10 of the
paper describes why cumulative study of this kind requires shared conventions that
no single author can settle alone.

## Citing

Archived on Zenodo, CC BY 4.0.

> Osborn, E. (2026). *Interface-Anchored Knowledge Mapping: Methodology and
> Reference Implementation Materials* (Version 1.00). Zenodo.
> https://doi.org/10.5281/zenodo.22668058

Zenodo mints two DOIs for a deposit, and they are not interchangeable:

| DOI | What it points to | Use it when |
|---|---|---|
| [`10.5281/zenodo.22668058`](https://doi.org/10.5281/zenodo.22668058) | **Version 1.00** specifically | Citing this work. A reader gets exactly the files you cited |
| [`10.5281/zenodo.22668057`](https://doi.org/10.5281/zenodo.22668057) | **All versions**, resolving to the latest | Linking to the project generally, where you want the reader to land on the newest release |

Cite the version DOI in a paper. Use the concept DOI in a README or a link.

Author ORCID: [0009-0007-8678-3307](https://orcid.org/0009-0007-8678-3307)

```bibtex
@misc{osborn2026iakm,
  author    = {Osborn, Elizabeth},
  title     = {Interface-Anchored Knowledge Mapping: Methodology and
               Reference Implementation Materials},
  year      = {2026},
  publisher = {Zenodo},
  version   = {1.00},
  orcid     = {0009-0007-8678-3307},
  doi       = {10.5281/zenodo.22668058},
  url       = {https://doi.org/10.5281/zenodo.22668058}
}
```

The deposit carries the preprint PDF and the implementation paper. The
Preprints.org posting will carry its own DOI when it goes live; that one cites
the manuscript, this one cites the archived materials.

## License

Everything here is open, deliberately and permanently.

| What | License |
|---|---|
| Paper, figures, documentation | [CC BY 4.0](LICENSE) |
| Everything under `scripts/` | [Apache License 2.0](LICENSE-CODE) |
| Patent rights | [Non-assertion pledge](PATENTS.md) |

You may use, adapt, redistribute, and build on this work commercially. The
only condition is attribution, which is the ordinary scholarly courtesy.

**On patents.** This work is published as prior art, with the intent that the
IAKM methodology remain free for all to use and that no party be able to
enclose it later. The Apache License grants patent rights expressly (Section
3), and [`PATENTS.md`](PATENTS.md) records an irrevocable non-assertion pledge
covering the methodology itself. Material here goes beyond any earlier patent
filing, and that is on purpose.
