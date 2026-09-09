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
paper_v7/
  IAKM_PAPER_V7_DRAFT.md        Prose source of the paper
  IAKM_PAPER_V7_IEEE.tex        Typeset source of record (hand-maintained)
  IAKM_Public.pdf               Built paper — start here
  IAKM_V7_FLOAT_PLACEMENT.md    Float/caption spec the .tex is tuned against
  IAKM_V7_REFERENCES.md         Reference list
  IAKM_CITATION_DIGGING_LIST.md Citation provenance notes
  fig1..fig5_*.pdf              Print-ready figures
scripts/                        Build tooling (see scripts/README.md)
```

**To read the paper:** open [`paper_v7/IAKM_Public.pdf`](paper_v7/IAKM_Public.pdf).

## Building the paper

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

If you apply IAKM to a system, the most useful thing you can contribute back is a
collection produced under declared bindings and evidence rules. Section 10 of the
paper describes why cumulative study of this kind requires shared conventions that
no single author can settle alone.

## Citing

A DOI will be minted on public release; this section will carry it.

```bibtex
@misc{osborn2026iakm,
  author = {Osborn, Elizabeth},
  title  = {Interface-Anchored Knowledge Mapping: A Coordinate System for
            Locating Knowledge-Relevant Metadata in Modular Sociotechnical
            Systems},
  year   = {2026},
  note   = {DOI pending}
}
```

## License

Dual-licensed. See [LICENSE](LICENSE) for the full statement.

| What | License |
|---|---|
| Paper, figures, documentation | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Everything under `scripts/` | [MIT](LICENSE-CODE) |

Neither license grants patent rights. CC BY 4.0 reserves them expressly
(§2(b)(2)); the MIT License contains no patent grant.
