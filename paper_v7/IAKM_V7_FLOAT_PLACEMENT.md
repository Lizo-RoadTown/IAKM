# V7 float placement specification

For the LaTeX build agent. Every figure and table in the paper, with the exact anchor text it attaches to, the float environment to use, the caption to set, the label to assign, and the in-text callout sentence to insert.

**Read this before touching the .tex file.** The anchor sentences below are quoted verbatim from `canon/IAKM_PAPER_V7_DRAFT.md`. Match on them literally.

---

## Standing rules for the build

1. **The paper is IEEE two-column.** A float wider than one column must use the starred environment (`figure*` or `table*`), which forces it to the top of a page and spans both columns. The Environment column below is not a suggestion.
2. **Every float needs an in-text callout.** The markdown draft currently has zero. IEEE requires each figure and table to be referenced in the body before it appears. The callout sentences to insert are given below, and they are the only prose the build agent adds to the paper. Nothing else in the manuscript changes.
3. **Callout style:** "Fig. 1" mid-sentence, "Figure 1" only if it starts a sentence. Tables are "Table I" always, Roman numerals, never abbreviated.
4. **Table numbering is Roman** (I through X). **Figure numbering is Arabic** (1 through 5). This is IEEE house style, not a preference.
5. **Placement specifier:** use `[!t]` for starred floats and `[!t]` for single-column floats as well. Do not use `[h]` or `[H]`; IEEE templates do not honor them reliably and the float will drift or error.
6. **Captions:** table captions go **above** the table. Figure captions go **below** the figure. IEEE style. Getting this backwards is the single most common build error in this template.
7. **Table captions are set in small caps and centered** by the IEEEtran class automatically. Do not add manual formatting.
8. **Do not reorder anything.** Floats may drift to the top of a later page; that is normal and correct. The callout is what preserves the reading order, not the physical position.

---

## Figures

Five figures, all supplied as print-ready PDFs. All five are wide landscape artwork and all five span both columns.

| Fig. | File | Section | Environment | Placement |
|---|---|---|---|---|
| 1 | `fig1_three_senses_of_location_print.pdf` | 5 | `figure*` | `[!t]` |
| 2 | `fig2_timing_coverage_plane_print.pdf` | 2 | `figure*` | `[!t]` |
| 3 | `fig3_gradient_stays_a_vector_print.pdf` | 8 | `figure*` | `[!t]` |
| 4 | `fig4_collection_stage_print.pdf` | 9 | `figure*` | `[!t]` |
| 5 | `fig5_future_work_print.pdf` | 10 | `figure*` | `[!t]` |

Figure order in the file is **2, 1, 3, 4, 5** by section, which is why the numbering below does not match the supplied filenames. **Renumber the figures to reading order.** The mapping is given explicitly in the next table so there is no guesswork.

### Renumbering map, authoritative

| Supplied filename | Becomes | Label to use |
|---|---|---|
| `fig2_timing_coverage_plane_print.pdf` | **Fig. 1** | `\label{fig:timing-coverage}` |
| `fig1_three_senses_of_location_print.pdf` | **Fig. 2** | `\label{fig:three-senses}` |
| `fig3_gradient_stays_a_vector_print.pdf` | **Fig. 3** | `\label{fig:gradient-vector}` |
| `fig4_collection_stage_print.pdf` | **Fig. 4** | `\label{fig:collection-stage}` |
| `fig5_future_work_print.pdf` | **Fig. 5** | `\label{fig:future-work}` |

Use the labels, never the numbers, in `\ref{}`. If a figure moves later, the labels keep the cross-references correct.

---

### Fig. 1 — Timing and coverage plane

**File:** `fig2_timing_coverage_plane_print.pdf`
**Label:** `fig:timing-coverage`
**Section:** 2, after Table I
**Environment:** `figure*`, placement `[!t]`

**Anchor.** Place the float so it appears on the same spread as Table I. It follows Table I and precedes the paragraph beginning:

> "A digital mapping system for knowledge loss depends on several claims that are already established in other literatures"

**Callout to insert.** The paragraph currently reads:

> "The table below compares what each method makes visible and what remains outside its record."

Replace with:

> "Table I compares what each method makes visible and what remains outside its record. Fig. 1 places the same methods on two axes that matter for recovery: when the observation happens, and how much of the program it reaches."

**Caption:**

> Fig. 1. Existing methods plotted by timing of observation and coverage across the program. Methods that observe while work unfolds reach one site at a time. Methods that reach the whole program observe after the work has settled. Only AI-assisted artifact analysis reaches the upper right, observing while work is still unfolding and across the whole program, and it reaches that region without supplying the constraint that makes the observations verifiable.

**Caption correction, 2026-09-09.** The earlier caption ended "No existing method occupies the upper right, which is the region a recovery record has to reach." That contradicted the figure, which places AI-assisted artifact analysis in the upper right, and contradicted Section IV, which argues that AI-assisted analysis is exactly what reaches that region. Use the caption above.

**Note.** The figure plots the same eight rows as Table I. Keep them adjacent. If LaTeX floats them onto separate pages, add `\usepackage{stfloats}` and use `[!t]` on both, or move Table I to `table*[!b]` on the page carrying the figure.

---

### Fig. 2 — Three senses of location

**File:** `fig1_three_senses_of_location_print.pdf`
**Label:** `fig:three-senses`
**Section:** 5, after Table III
**Environment:** `figure*`, placement `[!t]`

**Anchor.** Follows Table III (the three-senses table) and precedes the paragraph beginning:

> "The technician who knows by feel when a connector has seated"

**Callout to insert.** The sentence currently reads:

> "Three senses of location run together in ordinary speech, and the methodology keeps them apart because each does different work."

Replace with:

> "Three senses of location run together in ordinary speech, and the methodology keeps them apart because each does different work. Table III states the distinction and Fig. 2 shows how the three relate."

**Caption:**

> Fig. 2. The three senses of location. The structural location is the addressed interface relation between knower and component under a declared field, domain, and layer. The metadata capture point is where evidence about that relation was observed. The carrier location, recorded as a separate field, is where the knowledge itself appears to persist. The knowledge is not assumed to sit in the interface.

**Note.** Both the table and the figure stay. This was settled in the decision record: a figure can be cropped or skipped, and a table can be scanned and cited, so the distinction is carried twice on purpose. Do not drop one for length.

---

### Fig. 3 — The gradient stays a vector

**File:** `fig3_gradient_stays_a_vector_print.pdf`
**Label:** `fig:gradient-vector`
**Section:** 8, after Table VIII
**Environment:** `figure*`, placement `[!t]`

**Anchor.** Follows Table VIII (uses of verified map records). It attaches to the paragraph beginning:

> "The gradient is a layer profile rather than a single score."

**Callout to insert.** That paragraph currently reads:

> "The gradient is a layer profile rather than a single score. That distinction matters because different weak layers point to different preservation actions: a weak documentary layer may call for documentation, while a weak embodied or physical-contact layer may call for demonstration, paired work, or practice. Any scalar reduction, propagation model, or predictive use of the gradient remains unvalidated until tested in a particular study."

Replace with:

> "The gradient is a layer profile rather than a single score. That distinction matters because different weak layers point to different preservation actions: a weak documentary layer may call for documentation, while a weak embodied or physical-contact layer may call for demonstration, paired work, or practice. Fig. 3 shows two components whose scalar summaries are identical and whose layer profiles call for opposite interventions. Any scalar reduction, propagation model, or predictive use of the gradient remains unvalidated until tested in a particular study."

**Caption:**

> Fig. 3. Two components with the same scalar summary and different layer profiles. Component A has a strong documentary layer and weak physical contact; Component B is the reverse. Both reduce to 0.50. The intervention that repairs one will not reach the other, which is why coupling strength is recorded per layer rather than as a single value.

**Note.** This figure is the visual argument for the Pimmler and Eppinger row in Table II. If a reviewer questions why coupling strength is never collapsed to one number, this is the answer. Keep it in the paper even under a length cut.

---

### Fig. 4 — The collection stage

**File:** `fig4_collection_stage_print.pdf`
**Label:** `fig:collection-stage`
**Section:** 9, after Table IX
**Environment:** `figure*`, placement `[!t]`

**Anchor.** Follows Table IX (the collection-stage check table). It attaches to the paragraph beginning:

> "Success at this stage concerns the form of the records rather than the values inside them."

**Callout to insert.** In that paragraph, the sentence currently reads:

> "A record must be locatable, source-traceable, convention-bound, and auditable. Collections must be poolable across analysts, systems, and domains, because records that cannot join other records cannot form a corpus."

Replace with:

> "A record must be locatable, source-traceable, convention-bound, and auditable. Collections must be poolable across analysts, systems, and domains, because records that cannot join other records cannot form a corpus. Fig. 4 pairs each of those criteria with the collection failure it prevents, and separates the standards work that follows from the science that depends on it."

**Caption:**

> Fig. 4. The collection stage. Each record criterion prevents a specific collection failure. Shared standards work follows from the collection instrument; the science that depends on a corpus, including reviewer agreement, coupling-strength measurement, intervention tests, and knowledge-emergence studies, follows from that. The near aim is reduction of knowledge loss through preemptive capture.

**Note.** The figure carries the argument that Sections 9 and 10 make jointly. It sits in Section 9 because that is where the criteria are stated, but its right-hand column is the Section 10 material. If the two sections split across a page boundary, place the figure at the top of the page carrying the Section 9 to Section 10 transition.

---

### Fig. 5 — Cross-domain future work

**File:** `fig5_future_work_print.pdf`
**Label:** `fig:future-work`
**Section:** 10, in "Future work by the author"
**Environment:** `figure*`, placement `[!t]`

**Anchor.** Attaches to the paragraph beginning:

> "The goal would not be to compare domains as if they should produce the same records."

**Callout to insert.** That paragraph currently reads:

> "The goal would not be to compare domains as if they should produce the same records. It would be to learn which models, components, sources, and levels of granularity make different outcomes more interpretable."

Replace with:

> "The goal would not be to compare domains as if they should produce the same records. It would be to learn which models, components, sources, and levels of granularity make different outcomes more interpretable, as shown in Fig. 5."

**Caption:**

> Fig. 5. Cross-domain future work. Each domain is mapped at two times and compared against its own outcomes, not against the other domains. The learning target is which models, components, sources, and levels of granularity make which outcomes interpretable.

**Note.** The figure's bottom line, that this is not a comparison of domains as if the same results should appear in each, is the same guardrail the paragraph states. That repetition is deliberate. A reader who looks only at figures should not come away with the generalization reading.

---

## Tables

**Ten tables.** The former Table VI, "What follows when two addresses share elements," was absorbed into Section 5 prose on 2026-09-09, and every table after it moved up one Roman numeral. Earlier notes said eleven, and before that thirteen. Ten is the count verified against the current draft.

| Table | Section | Cols | Body rows | Environment | Placement |
|---|---|---|---|---|---|
| I | 2 | 3 | 8 | `table*` | `[!t]` |
| II | 2 | 3 | 7 | `table*` | `[!t]` |
| III | 5 | 3 | 3 | `table*` | `[!t]` |
| IV | 5 | 3 | 5 | `table*` | `[!t]` |
| V | 5 | 3 | 7 | `table*` | `[!t]` |
| VI | 6 | 3 | 8 | `table*` | `[!t]` |
| VII | 7.3 | 4 | 9 | `table` | `[!t]` |
| VIII | 8 | 4 | 6 | `table*` | `[!t]` |
| IX | 9 | 2 | 6 | `table*` | `[!b]` |
| X | 10 | 3 | 10 | `table*` | `[!t]` |

**Why the environment differs.** Three-column tables whose cells are full sentences will not fit a single IEEE column at any readable font size, so they span. Table VII is four columns but three of them hold only the words "yes," "no," "partial," or "open," so it fits a single column with the first column set to `p{}` and the other three centered. Table IX takes `[!b]` rather than `[!t]`, which requires `\usepackage{stfloats}`; see the float-congestion note below.

### Table-by-table anchors and captions

| Table | Anchor sentence in the draft | Caption |
|---|---|---|
| I | "Table I compares what each method makes visible and what remains outside its record." (as revised for the Fig. 1 callout above) | TABLE I. What existing methods make visible, and what remains outside their records |
| II | "The table below identifies which part of that foundation each literature supplies." → change to "Table II identifies which part of that foundation each literature supplies." | TABLE II. Established results the methodology builds on, and what it takes from each |
| III | "Table III states the distinction and Fig. 2 shows how the three relate." (as revised for the Fig. 2 callout above) | TABLE III. Three senses of location kept distinct by the methodology |
| IV | Follows the sentence "The smallest addressable unit is one interface layer, under one declared field and domain, between one component and one knower:" and the block-quoted equation under it. **Do not anchor on the equation string itself: `A = (T1, T2, T3, C, K)` appears twice in the draft**, once as the display and once in the record-validity constraints paragraph. Match the blockquote line `> A = (T1, T2, T3, C, K)` if an equation anchor is needed. Insert before the table: "Table IV defines each element." | TABLE IV. Elements of the address, and why the record requires each |
| V | Insert before the table: "Table V lists the descriptors that attach to an address without becoming part of it." | TABLE V. Descriptors attached to an address, and why each is not part of address identity |
| VI | Insert before the table: "Table VI gives the procedure step by step." | TABLE VI. Procedure for producing verified records |
| VII | The lead-in already exists: "The table separates three statuses..." → change to "Table VII separates three statuses..." | TABLE VII. What is specified, implemented, and demonstrated |
| VIII | Insert before the table: "Table VIII lists the operations verified records support, and the guardrail on each." | TABLE VIII. Uses of verified map records, with guardrails |
| IX | "The checks available at this stage ask whether the collection procedure produces records stable, interpretable, and varied enough to justify further study." → append: "Table IX states those checks." | TABLE IX. Collection-stage checks, and what would support continuing |
| X | "The relevant question is which method family can help build which part of an IAKM collection standard." → append: "Table X names the candidate families." | TABLE X. Method families that build conventions in emerging fields |

---

## Two things to fix while the build agent is in the file

1. **Table I row seven** reads "Telemetry and logs," not "Runtime traces." An earlier version of Figure 1 used the old wording. The supplied `fig2_timing_coverage_plane_print.pdf` already says "Telemetry and logs," so the figure and table now agree. Verify this after import rather than assuming it.
2. **Table I has eight rows.** Earlier build notes said seven. The eighth is "Meetings, chats, and recorded calls." The supplied figure has all eight. Verify.

---

## Citations and the reference list

**The reference list has THIRTEEN entries.** The source of record is `IAKM_V7_REFERENCES.md` in this folder. If the `.tex` bibliography stops at [11], it is stale. Pull [12] and [13] before building.

### Table X citation policy, settled 2026-09-09. Do not re-litigate.

Table X names ten method families. The anchors are treated in two classes:

| Class | Anchors | Treatment |
|---|---|---|
| Named with an author and a year | Dalkey and Helmer, Biber, Silberzahn et al. | Carry a reference number |
| Named programme, standard, or guidance family | OAEI, PRISMA, METHONTOLOGY, COSMIN, ISO 15489, AHRQ registry user guide | Bare pointer. **No reference entry.** |

A standard moves into the first class only if the manuscript discusses it in prose. None currently does, so none moves.

**No separate citation column.** The three numbers sit inside the existing "Where it is established" column. Table X stays three columns wide.

The three cells, verbatim:

```
Delphi studies              | Expert consensus and standards development; Dalkey and Helmer [12]
Reference corpus construction | Corpus linguistics and information retrieval evaluation; Biber [13]
Many-analyst designs        | Metascience; Silberzahn et al. [11]
```

Reason for the policy, recorded so it is not undone by a later pass: adding entries for all six programme anchors would take the list past nineteen and make Table X read as the paper's main contribution rather than as a pointer to standards work the field still has to do.

### The two entries to add

`thebibliography` form:

```latex
\bibitem{dalkey1963}
N. Dalkey and O. Helmer, "An experimental application of the DELPHI method to the use of experts,"
\emph{Manage. Sci.}, vol. 9, no. 3, pp. 458--467, Apr. 1963, doi: 10.1287/mnsc.9.3.458.

\bibitem{biber1993}
D. Biber, "Representativeness in corpus design," \emph{Literary Linguistic Comput.},
vol. 8, no. 4, pp. 243--257, 1993, doi: 10.1093/llc/8.4.243.
```

BibTeX form, if the build uses a `.bib`:

```bibtex
@article{dalkey1963,
  author  = {Dalkey, Norman and Helmer, Olaf},
  title   = {An experimental application of the {DELPHI} method to the use of experts},
  journal = {Management Science},
  volume  = {9}, number = {3}, pages = {458--467},
  year    = {1963}, month = apr,
  doi     = {10.1287/mnsc.9.3.458}
}
@article{biber1993,
  author  = {Biber, Douglas},
  title   = {Representativeness in corpus design},
  journal = {Literary and Linguistic Computing},
  volume  = {8}, number = {4}, pages = {243--257},
  year    = {1993},
  doi     = {10.1093/llc/8.4.243}
}
```

Both were verified against Crossref on 2026-09-09. Note the capitalization: the Dalkey and Helmer title carries **DELPHI** in full caps as published, which is why the BibTeX title wraps it in braces. Do not let BibTeX lowercase it.

### One false alarm to expect

A reference-integrity check run against the **markdown** will report [3] through [10] as defined-but-uncited. That is an artifact: Table II in the markdown still carries author-year names in its Source column, and the build converts them to numbers. Run the check against the `.tex` or the PDF, not the `.md`.

---

## Sanity check before declaring the build done

Run these seven checks and report the results rather than a summary:

1. Every `\label` has at least one `\ref` pointing at it, and every `\ref` resolves. No `??` in the compiled PDF.
2. Figure captions are below their figures, table captions above their tables. Spot-check Fig. 1 and Table I.
3. No float appears before its first callout in the reading order of the compiled PDF. If one does, move the callout earlier rather than forcing the float.
4. Table I and Fig. 1 are on the same page or facing pages. Same for Table III and Fig. 2, Table IX and Fig. 4.
5. No table overruns the column or page width. Check Table VII and Table X specifically, since they are the widest.
6. **The reference list ends at [13], not [11].** Confirm [12] Dalkey and Helmer and [13] Biber both appear in the compiled PDF, and that Table X's three bracketed numbers resolve to them and to [11].
7. No reference entry exists for OAEI, PRISMA, METHONTOLOGY, COSMIN, ISO 15489, or the AHRQ registry user guide. Those are deliberate bare pointers.


---

## Float congestion, added 2026-09-09

Three full-width floats collided on one page in the first build, producing a page that was almost entirely floats with four lines of body text. Starred floats (`table*`, `figure*`) can only occupy the top of a page in two-column IEEE, so they queue for the same slot and LaTeX flushes them together.

Two changes in the preamble, plus the `[!b]` on Table IX above:

```latex
\usepackage{stfloats}          % enables [b] for table*/figure* in two-column
\renewcommand{\topfraction}{0.85}
\renewcommand{\textfraction}{0.15}   % minimum share of a page that must be text
\renewcommand{\floatpagefraction}{0.75}
```

`\textfraction` at 0.15 is what forbids a near-empty page. If the section carrying Table VIII, Fig. 3, and Table IX still crowds after this, make Table IX single-column: it is two columns and the narrowest of the three.
