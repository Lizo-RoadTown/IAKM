# Interface-Anchored Knowledge Mapping

## A Coordinate System for Locating Knowledge-Relevant Metadata in Modular Sociotechnical Systems

---

## 1. The Methodological Problem

Knowledge loss in sociotechnical systems becomes unrecoverable when the conditions that made knowledge usable disappear before they are captured. In rapidly developing technical fields, critical knowledge is often formed during the work itself: debugging, integration, tool adaptation, failure interpretation, and design decisions made under pressure. Some of that knowledge becomes documentation, code, diagrams, test records, or procedures. Much of it remains with people: the professor who remembers why a laboratory method changed, the senior student who knows why a subsystem behaves strangely, the engineer who knows why an interface was built a certain way, or the technician who can recognize a failure pattern before it appears in a formal report.

When those people leave, the artifacts may remain while the conditions that made them intelligible disappear. A repository can preserve what was committed without preserving why it was written that way. A document can preserve a procedure after the tools, dependencies, assumptions, or design context that made it valid have changed. An organization can preserve roles without preserving the expertise that once made those roles functional. The contextual meaning that surrounds each artifact degrades, making it more difficult for new cohorts to integrate.

As development accelerates, emerging-technology methods are used and revised simultaneously, tools are often obsolete immediately after they are used, and experimental workflows are patched or abandoned before anyone has time to convert what was learned into durable institutional memory. The result is not merely incomplete documentation. It is a system that remains physically intact, digitally archived, and organizationally staffed while becoming difficult or impossible to understand.

The methodological problem is therefore to make knowledge loss observable before it becomes unrecoverable. Doing that requires a record that locates knowledge-relevant metadata in relation to the system: who appears to know what, what component it concerns, what evidence supports the claim, and where the knowledge may still be recoverable.

---

## 2. What Existing Methods Make Visible, and Why Loss Persists

Existing methods already preserve parts of this problem. The question is whether any of them also preserves the relation needed for recovery. That relation has four parts: a person appears connected to knowledge about a particular component; the connection rests on some evidence; the knowledge was produced, used, or transferred through some interface; and the knowledge may or may not remain recoverable after people, tools, documents, or roles change. Existing methods capture parts of that relation. None records it whole.

The table below compares what each method makes visible and what remains outside its record.

| Method or record type | What it makes visible | What remains outside the record |
|---|---|---|
| Documentation | Procedures, explanations, requirements, and design descriptions | Tacit judgment, changing assumptions, tool drift, and context that was not written down |
| Repositories and version history | Code, authorship traces, sequencing, and change over time | Why a change mattered, who still understands it, and whether its rationale remains recoverable |
| Organizational records | People, roles, assignments, authority, and responsibility | Component-specific knowledge and the conditions under which a person came to know |
| Meetings, chats, and recorded calls | Discussion, coordination, rationale, questions, informal decisions, and explanations as work unfolds | Stable structural address, later recoverability, and whether the knowledge persists outside the conversation |
| Direct observation of work in progress | Knowledge as it is used, seen at the site of the work | Coverage across teams that are distributed and working at once |
| Systems engineering, DSM, MBSE, and dependency models | Components, interfaces, couplings, and technical structure | Which people understand which parts, and on what grounds |
| Telemetry and logs | Runtime behavior, failures, and operational traces | The human interpretive knowledge needed to explain why behavior occurred |
| AI-assisted artifact analysis | Large-scale candidate extraction from available artifacts while work is ongoing | Verification, address, provenance, epistemic metadata, and recoverability |

Recent work has sharpened this gap rather than closed it. Repository-history methods estimate how concentrated developer knowledge is and visualize where that concentration sits, while leaving open what knowledge exists outside the commit record and why a particular component matters [10], [14], [15]. Large language models have been applied to mining software repositories and to answering repository questions over knowledge graphs, extending how much of an artifact set can be searched and organized [16], [17]. Each of these widens what can be observed without settling how an observation becomes a checkable record.

A digital mapping system for knowledge loss depends on several claims that are already established in other literatures: that systems can be decomposed into components and interfaces, that knowledge can be lost when people and practices change, and that the field of analysis shapes what becomes visible. The table below identifies which part of that foundation each literature supplies.

| What the literature establishes | Source | What the methodology takes from it |
|---|---|---|
| Systems decompose into subsystems whose internal interactions exceed those between them | Simon 1962 | Components are identifiable enough to anchor an address |
| Interfaces carry types and differential magnitude, so a pair is described by a vector | Pimmler and Eppinger 1994 | Coupling strength is recorded per layer, never as one number |
| The design structure matrix tradition has extended that representation across lineages | Browning 2016 | The representation can be adopted rather than argued for |
| Organizations accumulate knowledge through experience and lose it over time | Argote 1999 | The loss is real and has been measured |
| Departures can reduce the expertise available to an organization, though severity by structural position is unsettled | Galan 2023 | A recovery record must capture position and knower before the question can be posed |
| Knowledge can be associated with activity and position, but observing it requires presence | Lave and Wenger 1991; Hutchins 1995 | Location was reached once, by a method that does not scale |
| The field under which a system is examined governs what becomes visible within it | Hjørland and Albrechtsen 1995; Hjørland 2002 | The field and domain of analysis have to be declared inside the record |

Across the methods surveyed here, the missing element is a shared way to record the connection between a person and the part of the system they understand. These methods preserve useful evidence, but they do not produce a digital map that names that connection, links it to sources, and keeps it comparable across collections.

---

## 3. Preemptive Decomposition

A mapping system for knowledge loss requires the system to be decomposed before the loss occurs. Components, couplings, boundaries, and interfaces must be identifiable while the people, artifacts, practices, and traces that carry recoverable knowledge are still present.

The decomposition comes from a structural model of the sociotechnical system rather than from the knowledge record itself. That role can be filled by nearly decomposable architecture, which treats the system as a molecular structure: bond strengths between elements differ by orders of magnitude, so modules are defined by relatively tighter internal bonds and looser relations across boundaries [1]. Couplings are the relations between parts, typically stronger inside a module than across its boundary. Interfaces occur where parts connect, within modules as well as across module boundaries. Sustaining mechanisms are the formal or informal structures that keep an interface working, such as a role, tool, protocol, or shared repository. The first three of these units, module, coupling, and interface, are inherited from systems and modularity literature. A sustaining mechanism field is added because a sociotechnical interface is not fully described by the fact that a connection exists; the record also needs to state what, if anything, keeps that connection usable.

Preemptive decomposition matters because it gives the later map places to look. Once components and interfaces are identifiable, knowledge-relevant metadata can be sought at the relations where people, artifacts, tools, practices, and system parts meet. At the present collection stage, interface characterization guides search by suggesting what kinds of evidence may be recoverable. It remains a heuristic rather than a proof rule until repeated collections show whether those interface characteristics correspond reliably to recoverable metadata.

Preemptive decomposition identifies candidate structural locations; the record-producing procedure in Section 6 depends on those locations before an address can be anchored.

---

## 4. Digital Interfaces as the AI Seam

The new observational opening is digital. Modern technical work produces repositories, issues, reviews, documents, logs, chats, meeting records, workflow traces, and other artifacts as part of ordinary activity. These records do not preserve knowledge completely, but they often preserve metadata about where knowledge was used, who was involved, what component was affected, what decision or failure prompted action, and where recovery may still be possible.

Artificial intelligence changes the scale and timing of that observation. Earlier methods either observe knowledge-rich activity while it is happening but only locally, or preserve records at scale after the work has settled. AI-assisted analysis can examine large bodies of ordinary work artifacts while the work is still unfolding. That allows candidate interface relations to be identified before the people and traces that make verification possible have disappeared.

AI identifies candidate observations from digital traces. A methodology is still required to structure those candidates, attach evidence, distinguish metadata from knowledge content, and verify which records enter the map.

Interface-Anchored Knowledge Mapping (IAKM) is a digital mapping system that uses artificial intelligence to locate knowledge-relevant metadata about a physical system. It does not claim to capture the knowledge itself. It produces structured records about what appears to be known, who is implicated in that knowing, what component of the system the knowledge concerns, where the relevant interface relation is exposed, what evidence supports the observation, how the knowledge is grounded, and where the knowledge remains recoverable.

The methodology of IAKM specifies how those observations are decomposed, addressed, checked, and preserved. Its coordinate system gives each verified record a structural address, so that records can be found again, compared across collections, audited against evidence, and accumulated into a corpus.

The methodology is specified for modular sociotechnical systems in which components can be identified, ordinary work produces artifacts, and a governing field can be declared. It is not specified for systems without identifiable components, for knowledge unrelated to any component, or for settings where no artifact record exists.

The reference implementation appears only as evidence that portions of the methodology were exercised in software, and to state what was and was not demonstrated.

---

## 5. The Recovery Record and Coordinate System

IAKM does not need to store the knowledge itself. No copy of it, no summary of it, and no permanent access to it is required once a verified record has adequate provenance. That is the part that runs against ordinary intuition.

Preservation is usually taken to mean capture, so knowledge that cannot be written down has often been treated as already lost. A component that depends on one person is nonetheless a fact about the system, and that fact can be established without anyone writing down what the person knows. The connection is observable whether or not the content is.

The record is one of metadata rather than content. It preserves enough to locate, verify, and revisit a knowledge-relevant relation after people, tools, documents, or organizational roles have changed.

Three senses of location run together in ordinary speech, and the methodology keeps them apart because each does different work.

| Sense of location | What is located | Function in the methodology |
|---|---|---|
| Structural location | The interface relation between a knower and a component, under a declared field, domain, and layer | Gives the record an address: the relation can be found again, compared, queried, and joined with other records |
| Metadata capture point | The place in the available evidence where descriptors of the relation are observed | Shows where the methodology recovered evidence about the relation, without implying that the knowledge itself resides there |
| Carrier location | The person, artifact, instrument, model, practice, or community in which the knowledge itself appears to persist | Shows where recovery, transfer, preservation, or loss would take place |

The technician who knows by feel when a connector has seated is the case that makes the separation necessary. The content of what that person knows is not in the digital record and may never be. The relation is addressed because the component, knower, field, domain, and interface layer can be named. The capture point may be thin: perhaps a maintenance note, a repeated repair pattern, or a test anomaly. The carrier is recorded as the person, and the record therefore states that a specific component depends on knowledge held in one body and nowhere else. That is a structural condition the record can state, produced without capturing the knowledge itself.

A digital map requires stable addresses. The coordinate system supplies them for verified records. IAKM anchors the record to the relation between a knower and a component, rather than to the record itself or to only one end of the relation.

The smallest addressable unit is one interface layer, under one declared field and domain, between one component and one knower:

> A = (T1, T2, T3, C, K)

| Element | Meaning | Why the record requires it |
|---|---|---|
| T1 | Governing field: the body of methods, vocabulary, and standards of evidence used as the analytical lens | Fixes the standards of evidence under which the relation is claimed |
| T2 | Domain: the subject area into which the governing field reaches | One field reaches several subject areas, and which one is in play has to be fixed |
| T3 | Interface layer: the structural connection layer exposed by the declared field and domain | Locates where the relation between knower and component is exposed |
| C | Component anchor: the part of the system the metadata concerns | Identifies what part of the system the knowledge concerns |
| K | Knower anchor: the person whose knowledge, role, authorship, observation, or responsibility is implicated | Identifies whose knowledge is implicated |

A binding is the declared pair (T1, T2): the governing field and the domain to which it is applied. The binding determines which interface layers are visible. A software-architecture binding and a hardware-integration binding may expose different layers for the same person-component pair. They can still be joined through shared component and knower anchors. There is therefore no universal set of interface layers, no fixed count, and no canonical ordering across systems.

Nothing else belongs in the address. The descriptors below attach to an address without forming part of one, because none of them tells two addresses apart and several can change while the relation stays where it is. Holding that line prevents the address from being read as a container for knowledge content.

| Attached descriptor | What it records | Why it is not part of the address |
|---|---|---|
| Interaction type | What kind of relation crosses the interface | Relations of different kinds can be exposed at one address, so type does not tell two addresses apart |
| Sustaining mechanism | Who or what keeps that relation working | A mechanism can be added or removed while the relation stays at the same address |
| Coupling strength | The strength of that structural connection | A value that moves over time cannot be part of what makes two records the same |
| Evidence and lineage | The source material the observation rests on | Two analysts can reach one address from different evidence |
| Epistemic metadata | How the knowledge was grounded | It describes the knowing rather than the position the knowing occupies |
| Carrier or persistence location | Where the knowledge itself appears to persist | The carrier can change while the structural relation is unchanged |
| Confirmation status | Whether the record has been admitted to the verified map | Status changes through the procedure, so it is attached to the address rather than part of address identity |

Type and strength are what the design structure matrix tradition already records about an interface [2]. Sustaining mechanism adds a separate descriptor: what, if anything, keeps the relation usable.

Address identity is strict, and partial agreement is still informative. Two records refer to the same address only when all five elements match, which is what allows independent records of one system to be differenced. Records produced under different bindings still join through their shared component and knower anchors, without collapsing the layers each binding exposes. Holding a component fixed while varying the knower makes visible how many knowers are named at that component.

A component at which exactly one verified address names a knower is a structural condition of the record, and not by itself a prediction that knowledge will be lost.

Several constraints follow from the coordinate system. The address must remain exactly A = (T1, T2, T3, C, K), because adding metadata fields to the tuple would make address identity unstable. Interface layers must remain binding-relative, because a layer visible under one field and domain may not exist under another. Evidence and lineage must remain attached, because later readers must be able to check why a record was admitted. Structural location and carrier location must remain distinct, because the relation being mapped is not the place where the knowledge itself necessarily persists.

An implementation instantiates IAKM only if it preserves these constraints. The coordinate system defines what a record must preserve; the next step is the procedure that determines how candidate records are produced, checked, and admitted to the verified map.

---

## 6. Procedure for Producing Verified Records

The procedure begins from the decomposition set out in Section 3, which IAKM presumes rather than derives, and which must be in place before an address can be anchored. With that decomposition available, the IAKM methodology produces verified map records through candidate extraction, validation, and human verification. Computation over the verified record comes afterward.

| Step | What is done | What it yields |
|---|---|---|
| Represent | Identify components and structural couplings | Anchors for C |
| Select | Declare the governing field and domain | The binding, (T1, T2) |
| Configure | Translate system structure into the layers that binding exposes | The layer set for T3 |
| Ingest | Read artifacts as ordinary work already produces them | Source material, unaltered |
| Identify | Locate five-element addresses with metadata attached | Candidate records |
| Validate | Check lineage, duplicates, schema, identities, layer validity | Validated candidates |
| Verify | A person with standing dispositions each candidate | Approved, corrected, rejected, or duplicate |
| Admit | Promote verified records only | The map |

Candidate records remain separate from verified records throughout, because extraction is not confirmation.

During collection, metadata is recovered from available evidence about addressed interface relations, and what IAKM preserves is the verified recovery record rather than the source it was recovered from. Teams are not asked to author documentation for the map; the ingest step reads repositories, issues, reviews, documents, logs, wikis, contracts, and meeting records as they already exist. Each candidate carries the five-element address with the Section 5 descriptors attached and the evidence held as a source snapshot. Of the four dispositions, the two that alter or exclude a candidate require a recorded reason, so that a later reader can distinguish a rejected claim from one never made. Queries, exports, gradients, composition, and change analysis operate on the verified store by default.

Verification has stated criteria, and they are what a reviewer with standing is checking. First, that the address is correctly located, meaning the component, knower, field, domain, and layer named are the ones the cited evidence supports. Second, that each attached descriptor is supported by that evidence rather than inferred beyond it. Third, that the seven epistemic questions are answered from the same evidence, with an unknown recorded as an unknown rather than left blank. A failed check produces a disposition other than approval, and the recorded reason names which check failed.

Epistemic metadata is recorded against seven named questions rather than as free commentary, each carrying its own recorded fields. The questions ask who knew the relevant knowledge and how close they were to the system; where the knowledge lives now; what must stay connected for it to work; under what conditions it was true; when it stops being reliable; who wrote or taught it and why; and whether it works only while someone keeps doing it. Naming the questions allows two analysts to produce comparable records. They elicit answers rather than scoring them. No threshold, weighting, or score is defined over the answers, and every question concerns what can be recovered from the available evidence about an addressed interface relation and where the knowledge itself appears to persist.

---

## 7. Reference Implementation and Deployment Status

### 7.1 Reference implementation

The reference implementation was built to capture knowledge-relevant metadata during rapid, distributed technical development. It used automated extraction, staged review, provenance preservation, and a verified knowledge graph while the work was still unfolding. Here it is treated as one software embodiment of the methodology, showing which parts were exercised, which remained partial, and which implementation requirements became visible during use.

The implementation ingested sources, preserved raw snapshots, extracted candidate records with classification applied at capture, ran automated validation, presented candidates for human review, and promoted approved records into a verified store. Its design boundary separates replaceable extraction infrastructure from the methodology-bearing layers: address structure, metadata, provenance, validation, and verification. Extraction technology is expected to change, and the record structure is what the methodology contributes.

### 7.2 Deployment and run-level finding

The implementation was built and deployed across five universities in a distributed aerospace program whose teams were developing CubeSat missions on a shared open-source hardware platform and a shared open-source modular flight software framework. For tractability, the deployment used one binding, meaning one declared field-and-domain lens, rather than mapping the program under multiple bindings. That binding exposed five interface layers. The available sources reached two of them: documentation and software.

In the most recent extraction run, the agents produced 121 verified nodes and 24 verified edges in the knowledge graph, with 199 candidates pending in the review queue. These figures record what that run extracted, validated, and stored. They are not cumulative totals, evidence of a complete five-element address set, or evidence that the methodology was exercised in full. More material was extracted and validated than was confirmed, which is the expected behavior of a review step that filters candidates rather than passing them through. Coverage was partial, and the record is a sample rather than a census.

The run showed that the implementation could produce structured candidate records from ordinary work artifacts, keep candidate and verified records separate, and promote reviewed records into a verified knowledge graph. The run suggested that some forms of knowledge were more visible in available sources than others. Knowledge already expressed in documents, code, or other artifacts was directly observable. Knowledge held in practice, judgment, or bodily skill was less directly visible, though the structural positions associated with it could sometimes be named. It did not show predictive validity, long-term performance, intervention effects, coupling-strength calibration, reviewer agreement at scale, complete census, or which mapping choices suit other domains.

### 7.3 Demonstration status and limits

The status of each element differs, and collapsing the differences into a single disclaimer would misstate the work in both directions. The table separates three statuses. Specified means the methodology defines the element. Implemented means the reference implementation included it in software. Demonstrated means the deployment exercised it and left an outcome in the record. No row was measured against an external criterion; Section 9 describes what such checks would require.

| Element | Specified | Implemented | Demonstrated |
|---|:-:|:-:|:-:|
| Five-element address | yes | partial | no |
| Candidate and verified separation | yes | yes | yes |
| Evidence and lineage | yes | yes | partial |
| Explicit unknown as a value | yes | partial | no |
| Epistemic metadata | yes | partial | partial |
| Gradient | yes | no | no |
| Multi-domain composition | yes | no | no |
| Propagation | yes | no | no |
| Census closure | open | no | no |

The distinction matters because a feature can be specified by the methodology, implemented in software, or demonstrated in deployment without occupying all three states.

Verification coverage was partial, and the reason belongs in the result. The team dispersed before review at scale was possible, so the lead researcher verified a representative sample rather than the program's engineers verifying every candidate. The methodology admits both arrangements and requires that a study declare which was used. The deployment shows that the review gate operates, not that it was operated at full coverage.

The deployment did not evaluate sustained use. It did not measure operator workload, reviewer agreement, cohort transfer, or predictive validity. Those questions require multiple operators, repeated review cycles, and later beneficiaries using the verified library.

### 7.4 Requirements observed during use

Four implementation failures during use produced requirements for future implementations of this kind:

1. Completeness must be checked against stored counts, not assumed from a clean exit.
2. Classification must occur when a relationship is first captured, because type cannot be reliably reconstructed afterward.
3. Invocation limits must not silently drop validated records.
4. Cross-source identity conflicts must be detected and resolved during verification.

These are implementation requirements, not additional methodology rules.

The partial deployment is enough to show that verified records can be produced, but not enough to establish every use available to a mature map. The next section separates those uses from the evidence needed to validate them.

---

## 8. Uses of Verified Map Records

The implementation produced only a partial verified map, but the record structure specifies operations that become available once verified records exist. Verified records can be used immediately for queries and structured review. Other uses require repeated collections or a corpus.

| Use | Record basis | What it yields | Guardrail |
|---|---|---|---|
| Query and retrieval | Verified records under a declared binding | Which records exist at a given component, knower, or layer | Available once verified records exist; results are only as complete as the verified map |
| Knowledge gradient | Verified addresses differing only by layer, at one (T1, T2, C, K) | A vector of layer-specific coupling strengths | Requires enough verified layer records under one binding; not defined across bindings |
| Multi-domain composition | Maps made under different bindings | A join at their shared C and K anchors | Differences across bindings are observations, not errors |
| Change and departure analysis | Verified addresses naming one knower | The components and layers connected to that person | Identifies affected records; does not by itself predict loss |
| Absence and unknown states | Addresses at which something was expected | An explicit unknown, distinct from a blank | Meaningful only where an address and expectation exist |
| Repeated collection | The same sources collected again under the same convention | Change in the records between collections | Requires comparable conventions over time; enables trajectories, not causal claims by itself |

The gradient is a layer profile rather than a single score. That distinction matters because different weak layers point to different preservation actions: a weak documentary layer may call for documentation, while a weak embodied or physical-contact layer may call for demonstration, paired work, or practice. Any scalar reduction, propagation model, or predictive use of the gradient remains unvalidated until tested in a particular study.

---

## 9. Current-Stage Evaluation

Uses of the map and validation of those uses are separate questions. Verified records make query, comparison, layer profiles, and later repeated collection possible, but they do not by themselves establish that the resulting measures are valid or predictive. At the present collection stage, the first evaluation question is whether records can be produced in a form stable enough to accumulate.

Success at this stage concerns the form of the records rather than the values inside them. Fields that work with variable observations, including clinical trials, epidemiology, and satellite measurement, do not begin by assuming every observation will agree. They begin by making the collection procedure explicit enough that variation can be interpreted. IAKM requires the same kind of discipline. A record must be locatable, source-traceable, convention-bound, and auditable. Collections must be poolable across analysts, systems, and domains, because records that cannot join other records cannot form a corpus.

A corpus is a collection of records produced under declared conventions so that they can be pooled, compared, audited, and analyzed together. The necessary conventions include how fields and domains are named, how layers are derived, how evidence is admitted, how missingness is recorded, how reviewer standing is defined, how disagreements are reconciled, how addresses are versioned, and how coupling strength or later scalar reductions are calibrated. If those choices remain implicit, independently produced maps become separate descriptions rather than cumulative evidence. If they are fixed too early and without versioning, the wrong categories are encoded at scale.

The basic observation can still be simple. For a declared address, a record either verifies that a knowledge-relevant relation was observed or it does not. Many yes-or-no observations can later support probabilistic claims about where knowledge-relevant metadata tends to appear and which interface conditions change those probabilities. The methodology therefore requires stable records, not deterministic claims that a type of interface always contains a type of knowledge.

The checks available at this stage ask whether the collection procedure produces records stable, interpretable, and varied enough to justify further study.

| Collection-stage question | What would support continuing |
|---|---|
| Can addresses be located reproducibly? | Analysts using the same sources and declared field-domain lens locate substantially similar addresses |
| Can records be verified consistently? | Reviewers with standing make comparable disposition decisions on the same candidate records |
| Can the record structure preserve uncertainty? | Unknowns are recorded explicitly rather than hidden as blanks |
| Do layer profiles vary? | Components differ by layer profile, showing that the vector carries information a single value would discard |
| Do single-knower dependencies surface recognizably? | Components named by the map as having one associated knower are recognized by participants as difficult to recover |
| Does declaring a binding do any work? | Some addresses are locatable only under the declared field-domain lens, showing that the binding changes what the map can see |

These checks do not validate prediction, intervention, or generalizability. They ask whether the collection procedure produces records stable and varied enough to support the next stage of study; a negative answer is a reason to revise the procedure before collecting further.

A precedent exists for the last check. Truck factor estimates computed from repository history were taken back to the developers of the systems they described. In eighty-four percent of valid answers, developers agreed or partially agreed that the identified developers were the main authors of their systems, while fifty-three percent gave a positive or partially positive response about the estimated truck factor itself [Avelino et al. 2016]. The same distinction matters here. Who is connected to a component is a claim people can often confirm from where they sit; the value attached to that connection requires more evidence.

Until these checks are run, IAKM should be claimed as a digital mapping system with a coordinate system and methodology for producing verified records, not as a validated predictor of loss. Section 10 turns from collection-stage checks to the standards and longitudinal work needed next.

---

## 10. Standards and Future Work

### Standards work for the field

Mature sciences make variation studyable by standardizing how observations are named, measured, and reported. Chemistry has shared naming conventions and reporting standards. Physics has agreed units and calibration practices. Those conventions do not remove variation from the world; they make observations comparable despite variation. IAKM is at an earlier stage.

The next stage for the field is standards-building through shared collection. IAKM can specify a record form, coordinate system, and verification procedure, but cumulative study requires conventions that no single author can settle alone. Fields and domains have to be bounded, layers have to be derived, evidence rules have to be declared, reviewer standing has to be defined, and record formats have to be stable enough for separate collections to join.

That work requires other collectors because the central claims concern reproducibility, comparability, and accumulation. A record reproduced only by the person who produced it has not yet been reproduced. Nor can agreement be assumed: in one many-analyst study, twenty-nine teams working from the same dataset and question reached materially different conclusions, with sixty-nine percent finding a significant effect and thirty-one percent not, and neither analyst expertise nor peer-rated quality readily explained the variation [Silberzahn et al. 2018]. The deployment reported above also makes the need for shared collection concrete: it used one binding, reached two of five exposed layers, drew on one program's sources, and was checked by one person against a sample.

Other fields already have methods for building conventions when categories are still emerging. The relevant question is which method family can help build which part of an IAKM collection standard.

| Method family | Where it is established | What it can help build for IAKM |
|---|---|---|
| Delphi studies | Expert consensus and standards development; Dalkey and Helmer [12] | Convergence on definitions, categories, reviewer rules, and convention choices |
| Evaluation campaigns and shared tasks | Ontology matching, OAEI; shared tasks in natural language processing and information retrieval | Shared source sets, common output formats, benchmark comparison, visible disagreement |
| Reference corpus construction | Corpus linguistics and information retrieval evaluation; Biber [13] | Common records built under documented sampling and annotation rules |
| Registry design | Medical and public health registries; AHRQ registry user guide | Stable schemas, longitudinal accumulation, versioned data definitions |
| Systematic review protocols | Evidence synthesis; PRISMA | Inclusion criteria, extraction fields, source traceability, disagreement handling |
| Content analysis and codebook development | Communication research and qualitative methods | Coding rules, coder training, agreement checks, category refinement |
| Ontology engineering | Knowledge representation; METHONTOLOGY | Formal vocabulary, classes, relations, identity rules |
| Many-analyst designs | Metascience; Silberzahn et al. [11] | Shows where competent analysts diverge under shared data and task definitions |
| Measurement-instrument development | Psychometrics; COSMIN | Reliability, validity, calibration, construct definition |
| Records and provenance standards | Archival records management; ISO 15489 | Provenance, audit trails, record metadata, custody, traceability |

Shared collection studies would test whether different analysts and reviewers can produce compatible records from common source sets. Those studies would show where the current methodology is reproducible and where conventions need to be written, narrowed, or versioned.

These methods are not adopted here as a fixed procedure. They identify the kinds of standards work needed before IAKM collections can accumulate into a corpus.

### Future work by the author

With future funding and access, the next study would continue the CubeSat work as a baseline while developing comparable mapping systems in other domains alongside it. Continued CubeSat collection would allow verified records to be compared with changes in the organization, changes in components, data collected through ground stations, and operational outcomes after launch. New domains would test how the methodology changes when the mapped system, evidence sources, components, and outcomes differ.

The goal would not be to compare domains as if they should produce the same records. It would be to learn which models, components, sources, and levels of granularity make different outcomes more interpretable. Different domains may require different surfaces, component models, and outcome measures. Keeping the CubeSat work as a baseline while building new domain maps would show what remains stable in the methodology and what must be adapted.

Repeated collection may also support later study of knowledge emergence. If comparable interface relations recur where new knowledge forms, then interface identification may help researchers know where to look while knowledge is still forming. That possibility requires a longitudinal corpus and shared conventions; it is future work, not a claim established here.

---

## 11. Conclusion

IAKM is a collection-stage mapping system. It addresses knowledge loss by making knowledge-relevant metadata structurally addressable before recovery becomes impossible, and its present contribution is a coordinate system, a collection convention, and a verification procedure.

AI-assisted analysis creates the observational opportunity, because large artifact sets can be examined while work is still ongoing and candidate interface relations can be identified before the people, practices, and traces that carry recoverable knowledge disappear. IAKM supplies the constraint that makes those observations scientific rather than merely extensive.

What the methodology does not yet establish is a validated predictor of loss, a calibrated measure of coupling strength, or an intervention model. Each requires a corpus, and a corpus requires shared standards, repeated collection, and validation by parties other than the author.

The longer horizon, set out in Section 10, is whether the same records can support the study of knowledge emergence.

Knowledge loss in modular sociotechnical systems cannot become a cumulative science until knowledge-relevant metadata is collected under shared, auditable, versioned conventions. IAKM is a proposed digital mapping system and methodology for making that work possible.
