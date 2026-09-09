# Citation items that need more digging

What the ToolUniverse verification pass could not close. Each item states the question, what is known, and what would answer it. Nothing here blocks the draft; all of it should close before submission.

---

## The one real inconsistency

**The Section 10 method-family table names ten anchors that are not in the reference list.**

The table's middle column carries Dalkey and Helmer 1963, OAEI, Biber 1993, the AHRQ registry user guide, PRISMA, METHONTOLOGY, Silberzahn et al. 2018, COSMIN, and ISO 15489. Only Silberzahn is in the reference list. The rest are named in the paper as attributions but carry no entry.

Three ways to close it, and the choice is yours:

| Option | What it costs | What it buys |
|---|---|---|
| Add all nine to the reference list | Takes the list from eleven to twenty | Every named source is checkable |
| Cite only the ones named as a specific work with a year, and leave field names bare | Adds Dalkey and Helmer, Biber, METHONTOLOGY, and the AHRQ guide; leaves PRISMA, COSMIN, OAEI, and ISO 15489 as field-level pointers | Smaller list, but the line between a citation and a pointer has to hold under review |
| Strip years and author names from the table so every cell reads as a field pointer | No new entries | A reviewer who wants the anchor has to go find it |

A reviewer from systems engineering or metascience will check this column, because it is the part of Section 10 that claims the standards work has precedent.

---

## Two anchor names are wrong as written

| In the table | Correct form | Note |
|---|---|---|
| METHONTOLOGY | First author is **Mariano Fernández**, not Fernández-López. Fernández-López is the later form of the name; the 1997 paper carries Fernández | Fix before either citing or leaving as a pointer |
| ISO 15489 | **ISO 15489-1**. The standard is a multi-part series, and the records-management principles the table points at are in Part 1 | Naming the series without the part is imprecise but not wrong; naming Part 1 is better |

---

## COSMIN resolves to three papers

COSMIN is a research initiative, not a single publication. The name resolves to at least three distinct anchor papers depending on what is being cited: the checklist development study, the taxonomy and definitions paper, and the risk-of-bias tool. The table's claim is about reliability, validity, calibration, and construct definition, which points at the taxonomy paper rather than the bias tool, but that should be a deliberate pick rather than a default.

**What would answer it:** read the three abstracts and choose the one whose scope matches the sentence.

---

## Argote 1999 versus the 2013 second edition

Crossref holds a record for the 2013 second edition with a DOI. It holds no clean record for the 1999 first edition, and the 1999 title page was not read, so the subtitle punctuation in entry [4] is unverified.

Two questions, in order:

1. Does the claim in the Section 2 table, that organizations accumulate knowledge through experience and lose it over time, sit in the 1999 edition specifically, or is it in both? If both, the 2013 edition is the better citation because it has a DOI and is the edition a reader will find.
2. If the 1999 edition stays, the title page needs to be read to confirm the subtitle.

**What would answer it:** a library copy or a publisher preview of either edition.

---

## Three sources verified bibliographically but not read

| Source | What it carries in the paper | Risk if it does not support the sentence |
|---|---|---|
| Argote 1999 | Organizations accumulate and lose knowledge over time | Low. Standard attribution, and the claim is the thesis of the book |
| Lave and Wenger 1991 | Knowledge can be associated with activity and position, but observing it requires presence | Low to moderate. The first half is squarely theirs; the "requires presence" half is a reading of the method, not a quoted claim |
| Hjørland and Albrechtsen 1995 | The field under which a system is examined governs what becomes visible within it | Low. This is the domain-analysis thesis |

Hjørland 2002 was closed during the pass: the eleven approaches are confirmed against the publisher record, and the Section 10 sentence was already reworded to say IAKM adopts none of them as a fixed procedure, which is what the source supports.

**What would answer the remaining three:** each is obtainable. Lave and Wenger and Hutchins are in most university libraries. Hjørland and Albrechtsen is behind a Wiley paywall but reachable through institutional access.

---

## Sources that blocked automated verification

Recorded so the next pass does not repeat the attempt: JSTOR, Emerald, the ACM Digital Library, and PubMed all refuse automated fetch. OpenAlex and Semantic Scholar returned HTTP 429 during the pass. Fatcat timed out. EuropePMC does not index *Advances in Methods and Practices in Psychological Science*, which is why Silberzahn had to be verified through the publisher record.

Crossref REST worked for everything it holds. The ToolUniverse `Crossref_search_works` wrapper requires `query`, `limit`, and `filter` together, and its return schema drops volume, issue, and pages, so page ranges have to come from a direct Crossref REST query.

---

## Not a citation problem, but adjacent

The modularity canon is still uncited. The title says "modular sociotechnical systems" and the paper cites none of Baldwin and Clark 2000, Ulrich 1995, Parnas 1972, Schilling 2000, or Sanchez and Mahoney 1996. Frandsen 2017 and Sinha 2019 are already PDFs in the project. This is on the open-items list in the decision record and is a separate decision from the anchor-table question above.
