# Cladribine: coherent parent identity with evidence-scope and brand-typing corrections

- Review: 20261021T132715Z-cladribine-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T13:04:59Z
- Finished UTC: 2026-10-21T13:27:15Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact cladribine parent structure and antibacterial eligibility are supported. One minor native evidence-scope correction is needed: the source summary describes growth inhibition and bactericidal activity against clinical isolates, while the original growth/time-kill figures use a reference strain and two migratory-bird isolates. The mixed-origin MIC panel and mouse lung-burden result should be described separately. Cellular stress responses do not establish direct bacterial targets. A second minor correction concerns Leustatin, a formulation brand currently typed as an exact chemical synonym. The corrected source interpretation belongs in notes; snippet is reserved for a short verbatim passage.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 306; one exact record. All 13 initial input hashes were preserved, and all 21 expanded input hashes were rechecked.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:curator-d33759f162 | data/antibiotics/antibacterial/cladribine.yaml | generated | Cladribine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:curator-d33759f162 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:curator-d33759f162 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:curator-d33759f162 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:curator-d33759f162 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:curator-d33759f162 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:curator-d33759f162 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:curator-d33759f162 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:curator-d33759f162 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:curator-d33759f162 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:curator-d33759f162 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:curator-d33759f162 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:curator-d33759f162 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact synthetic parent, names and chemical properties

identity: concern. Targets: antibioticmech:curator-d33759f162.

Native molecular encodings, PubChem and current ChEBI agree on the complete parent structure. FDA substance and historical label information corroborate the names and distinguish inactive sodium chloride from a drug salt. Leustatin denotes the labeled injection product, so its native EXACT_SYNONYM type needs the separate bounded correction below.

### PubChem xref, MINTED grounding and source mint

grounding: supported. Targets: antibioticmech:curator-d33759f162.

The asserted CID is exact and the curator identifier is reproducible. CHEBI:567361 is a verified optional external match, not evidence that the stable native identifier or its historical MINTED state is intrinsically wrong.

### Antibacterial definition, class and role

evidence: supported. Targets: antibioticmech:curator-d33759f162.

Original cladribine growth inhibition and a mouse bacterial-burden endpoint support antibacterial eligibility. The study is preliminary and does not establish an approved antibacterial indication or general clinical efficacy.

### Native evidence summary: clinical isolates

evidence: concern. Targets: antibioticmech:curator-d33759f162.

The native snippet groups growth inhibition and author-reported bactericidal activity under clinical isolates. The original figures instead test a reference strain and two avian isolates; the broader MIC panel has mixed origins and only one patient isolate. The snippet needs a bounded correction through the maintained curator inventory. The Liu et al. sentence is curator synthesis, not a verbatim source passage; place the corrected interpretation in evidence_notes and reserve evidence_snippet for exact quotation.

### Author-reported bactericidal terminology and quantitative interpretation

evidence: unknown. Targets: antibioticmech:curator-d33759f162.

The snippet reports the authors' characterization, but Figure 1 shows a larger difference from growing controls than decline from starting inocula. Any future quantitative killing claim must identify baseline, concentration and time rather than equating suppression relative to controls with equivalent killing. No separate categorical native defect is inferred from the attributed wording alone.

### Optional targets and causal graph

completeness: unknown. Targets: antibioticmech:curator-d33759f162.

The source supports cellular stress observations, not a validated direct target or causal ordering. SDH/PK lysate assays, porin/SOS expression, host drug pharmacology and iModulonDB coverage cannot justify direct-target annotations. Missing optional mechanisms are not a schema flaw.

### Optional quantitative activity_spectrum

completeness: unknown. Targets: antibioticmech:curator-d33759f162.

A useful original source exists, but isolate origins, MIC versus carbapenem comparator columns, growth/kill baselines, concentration units and mouse dose/endpoint must remain distinct. Assay values are not breakpoints or evidence that an entire taxon is resistant.

### Host pharmacology and clinical-product context

scope: supported. Targets: antibioticmech:curator-d33759f162.

Leustatin provides exact active-ingredient/name context. Oncology or immunomodulatory use does not supply an antibacterial clinical claim, and cytokine changes in infected mice do not independently isolate a host target. Native clinical fields are unpopulated.

### Unpopulated resistance, producer and dataset assertions

scope: not_applicable. Targets: antibioticmech:curator-d33759f162.

No such native claims require adjudication. KPC-2 and carbapenem comparator MICs concern resistance to other drugs, and purchased synthetic material is not evidence of a natural producer.

### Actual curator owner, PROPOSED status and one history event

provenance: supported. Targets: antibioticmech:curator-d33759f162.

The curated inventory and source seeding explain the record and its single proposal event. The scientific scope correction belongs to that maintained row and regenerated evidence, not a hand edit that seeding would overwrite. All captured hashes remain preserved.

### Focused deterministic gates

schema: supported. Targets: antibioticmech:curator-d33759f162.

Native schema, strict validation and molecular consistency pass. These successes do not resolve the evidence-summary scope finding.

## Findings

### F1: The source summary mislabels the growth and time-kill panel as clinical isolates

minor / open / confirmed; issue key: cladribine-clinical-isolate-evidence-scope.

source_concepts[0].evidence[0].snippet reports growth inhibition and bactericidal activity against clinical isolates. Original Figure 1 uses ATCC 700603 and isolates 21QH35K/21QH43K; Methods and Supplementary Table S1 identify the latter as migratory-bird fecal isolates. The broader MIC panel includes one patient throat-swab isolate plus avian and vegetable isolates. Revise the maintained source summary to distinguish this mixed-origin MIC panel, the reference/avian growth and time-kill experiments, and the 21QH35K mouse model. Preserve the supported antibacterial role and lung-burden result. Keep bactericidal terminology attributed to the authors and qualify control-versus-baseline interpretation if numerical killing claims are added. The same sentence is a curator paraphrase, not a verbatim passage. Move the corrected interpretation to evidence_notes, retaining the existing chemical-provenance notes, and omit evidence_snippet or replace it with a short exact passage.

### F2: Type Leustatin as a brand name

minor / open / confirmed; issue key: cladribine-leustatin-brand-exact-synonym.

The historical FDA label identifies Leustatin as a cladribine injection with inactive formulation ingredients. The native synonym is explicitly EXACT_SYNONYM. Preserve this useful product association with BRAND_NAME typing through a maintained, reproducible source path. The curator importer currently assigns EXACT_SYNONYM to every input alias, so changing generated YAML or inserting an unparsed type prefix in the TSV would not implement the fix.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained cladribine evidence summary to preserve exact isolate origins and experimental endpoints.

- Identify 21QH35K and 21QH43K as avian isolates and reserve patient-origin wording for GD18-KP-602.
- Separate the mixed-origin MIC panel from the Figure 1 reference/avian growth and time-kill panel and the avian-isolate mouse model.
- Place the corrected synthesis in evidence_notes while preserving existing chemical provenance; reserve evidence_snippet for a short, verified verbatim source passage or leave it empty.
- Preserve the supported antibacterial role and mouse lung-burden observation; do not relabel carbapenem MIC columns as cladribine data.
- Regenerate through the maintained source workflow and run native schema, strict, provenance/history and applicable QC gates after separately authorized curation.

### A2

Optionally enrich exact chemical grounding and primary activity without promoting correlated cellular responses to direct targets.

- Consider the verified CHEBI:567361 match while preserving the stable identifier and documented grounding history.
- Retain MedChemExpress cladribine material, purity, media, solvent, incubation, concentration units and endpoint scope.
- Represent killing relative to the stated starting inoculum and controls; do not infer a baseline kill magnitude from control separation.
- Keep treated-cell lysate assays, expression changes, host clinical pharmacology and mouse inflammatory endpoints distinct from direct bacterial target proof.

### A3

Add a reproducible curator synonym classification path for Leustatin as BRAND_NAME, preserving the chemical aliases and source provenance.

- Leustatin is emitted as BRAND_NAME; 2-CdA and the chemical name retain their supported types.
- The typed alias survives regeneration and documented schema/strict and corpus-reproduction gates; no formulation ingredient is added to the parent molecular structure.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cladribine.yaml; Entire 53-line native YAML, including all three synonyms, source evidence, chemical fields and single history event | supports | The record has a stable curator-minted identifier, PROPOSED curation status, MINTED grounding and antibacterial role. Its definition and sole evidence snippet cite the 2026 original paper. PubChem CID 20279 is its only external chemical xref. No native molecular target, causal graph, activity_spectrum, resistance determinant, producer, clinical status or dataset assertion is populated. |
| owners | curation/curator_antibiotics.tsv; scripts/seed_from_sources.py; curation/decisions.tsv; Exact maintained curator row 22; source concept and seeding transform | supports | The maintained curator row, not the generic ChEBI inventory, owns this record's identity, definition and evidence summary. The expanded target ownership was corrected accordingly while preserving the initial capture and all 13 initial hashes. All 21 expanded hashes were rechecked. No target-specific decision override was found with hidden and ignored files included. |
| rubric | .claude/skills/review-yaml-record/SKILL.md; docs/record-review-profile.md; .claude/skills/curate-yaml-record/references/review-checklist.md; Exact identity, source ownership, primary evidence scope and optional completeness | supports | The review distinguishes antimicrobial eligibility from clinical approval and does not require optional targets, quantitative activity or a causal graph without suitable evidence. MINTED grounding and PROPOSED curation are different concepts and are not automatically invalidated by a newly checked external match. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/20279/property/InChI,InChIKey,MolecularFormula,MolecularWeight,ExactMass,CanonicalSMILES,IsomericSMILES/JSON; Current PubChem CID 20279 molecular properties | supports | The sole asserted chemical xref resolves to cladribine with full key PTOAARAWEBMLNO-KVQBGUIXSA-N, C10H12ClN5O3 and the same three assigned stereocentres. The native structure_source and historical retrieval date describe this exact compound; the current comparison does not rewrite historical provenance. |
| chebi-comparator | https://www.ebi.ac.uk/chebi/backend/api/public/compound/567361/; Current CHEBI:567361 names, definition and structural encodings; independent comparison only | supports | Current ChEBI cladribine has the same complete standard InChI and key as the native graph. Its host antineoplastic and immunosuppressive annotations are not evidence of bacterial targets. This newly inspected exact grounding is a possible future enrichment; it is not an asserted native xref or permission to replace the stable curator identifier. |
| chemistry | Independent molecular and source-mint calculation; 306-chemistry.json; 305306-xref-chemistry.json; 305306-final-audit.json, target 306 | supports | Both native encodings yield one neutral component, formula C10H12ClN5O3, the full stored key, three assigned stereocentres, average mass 285.691 and exact mass 285.062866924. PubChem and current ChEBI encodings agree. The curator mint antibioticmech:curator-d33759f162 recomputes correctly from its source identity. |
| gsrs-name | https://precision.fda.gov/uniisearch/srs/unii/47m74x9yt5; Official FDA substance entry UNII 47M74X9YT5 | supports | The ingredient entry gives the same formula and full key and lists 2-CdA, 2-chlorodeoxyadenosine and LEUSTATIN among its names. It corroborates the name association; a substance listing does not by itself imply approval for an antibacterial indication. |
| brand-material | https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020229s034lbl.pdf; Historical FDA Leustatin label, Description pp1-2 | supports | Leustatin is a cladribine injection containing 1 mg/mL active cladribine; sodium chloride is explicitly inactive. The chemical name identifies the same parent nucleoside, not a distinct cladribine sodium salt. The brand association is coherent, while the formulation and antineoplastic clinical use remain separate from the purchased material used in the bacterial study. Only identity/formulation and host-pharmacology context were inspected, not every clinical-label claim. |
| role | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms; 305-term-33282.json, shared identical role-term lookup | supports | CHEBI:33282 denotes antibacterial agent, including substances that kill or slow bacterial growth. Measured growth inhibition is sufficient for this role; a clinical antibiotic approval or proof of a unique direct target is not required. |
| original-index | https://doi.org/10.1186/s12866-026-05197-z; PMID:42168872 / PMC13371293; complete original metadata and abstract | supports | The sole adopted DOI resolves to Liu and colleagues' 2026 original study of cladribine against carbapenem-resistant Klebsiella pneumoniae. Its abstract claims clinical isolates, cellular stress responses and mouse efficacy. The full Methods, figures and supplement were inspected rather than accepting all abstract terminology as exact experimental scope. |
| original-material | https://doi.org/10.1186/s12866-026-05197-z; Methods: Bacterial isolates, compound and antibiotics; MIC, growth and time-kill methods | supports | The experimental material is named cladribine from MedChemExpress at greater than 98% purity, dissolved in DMSO. No catalog or independent lot structure analysis is given. Broth MIC uses twofold dilution in Mueller-Hinton medium at 37 C for 16-18 h; growth curves use LB and OD600; time-kill assays start at 1×10^7 CFU/mL in Mueller-Hinton medium with colony counts over 24 h. These are separate endpoints, not a formulated Leustatin clinical trial. |
| strain-supplement | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13371293/supplementaryFiles; Original DOCX Table S1, all cells inspected; 306-tableS1-rows.json; source file 306-supp/12866_2026_5197_MOESM1_ESM.docx | supports | Table S1 identifies ATCC 700603 as a laboratory strain; 21QH35K and 21QH43K as migratory-bird fecal isolates from 2021; GD18-KP-602 as a patient throat-swab isolate; and VH1-2 as a vegetable isolate. Its three MIC columns are meropenem, imipenem and ertapenem, not cladribine. The carbapenem-resistant isolates carry KPC-2; that does not establish resistance to cladribine. The supplement resolves the main-text GD18-KP-60/602 naming discrepancy in favor of GD18-KP-602. |
| original-growth | https://doi.org/10.1186/s12866-026-05197-z; Results first subsection and original Figure 1, all six panels visually inspected | supports | Results state a cladribine MIC of 64 micrograms/mL across the named panel and report a 2% DMSO control. Figure 1 growth/time-kill panels are specifically ATCC 700603, 21QH35K and 21QH43K. The latter two are avian, not patient isolates. At 8×MIC, viable counts remain below growing untreated controls; the curves show modest decline from initial counts rather than the control-to-treatment gap representing equivalent killing from baseline. The authors use bactericidal terminology, which should remain attributed and qualified rather than becoming an unbounded killing claim. |
| original-mouse | https://doi.org/10.1186/s12866-026-05197-z; Mouse Results and animal Methods; original Figure 5 visually inspected | supports | The lung model uses 21QH35K, whose avian origin is specified in Methods and Table S1 despite being called clinical in Results. Female ICR mice receive cladribine 10 or 20 mg/kg intraperitoneally at 8 and 16 h, with lung counts measured at 24 h, n=6 per group. Reported burdens decline from 6.99 to 4.90 and 4.40 log10 CFU/g. Figure 5 supports reduced lung burden. These are approximately 2.09- and 2.59-log differences from untreated infected mice, not clinical cure or a bacterial time-kill endpoint. |
| original-mechanism | https://doi.org/10.1186/s12866-026-05197-z; Full bacterial stress Results, corresponding Methods and Discussion limitations | supports | PI/NPN permeability, leakage, TEM, ROS/MDA, ATP and transcriptional changes are measured after cellular treatment. SDH and pyruvate-kinase activities are measured in treated-cell lysates after 12 h, not as purified-protein binding or direct inhibition. Porin and SOS-gene induction are stress responses. The authors explicitly describe these results as correlative and acknowledge that primary causality was not established. Host antineoplastic DNA pharmacology is not demonstrated as the bacterial initiating mechanism. |
| original-limits | https://doi.org/10.1186/s12866-026-05197-z; Discussion final limitations paragraph; Supplementary Table S2 and figure captions; mouse Methods | supports | The panel is limited, no positive-antibiotic comparator was included in the infection efficacy experiment, and pharmacokinetics and long-term safety were not studied. Lung cytokine transcripts and histology cannot isolate a host-directed effect from lower bacterial burden. Primer identity or expression change does not establish direct molecular targeting. Supplementary material was inspected as evidence of assay design and origin, not treated as a new independent replication. |
| adapter | iModulonDB structured catalog; 297-adapter-catalog.json, already executed catalog inspected before open protein follow-up | context_only | No Klebsiella pneumoniae dataset is listed in the available catalog. The native record does not name a bacterial protein or pathway. No E. coli surrogate or expression-component membership was invented for the K. pneumoniae experiments, and database coverage absence is not negative mechanistic evidence. |
| search | Ignored-inclusive local ownership and bounded public-source search; 306-local-hits.txt; 306-focused-local-search.json; source retrieval manifests | context_only | The initial repository-wide and focused curation/conf searches included hidden and ignored files. The exact maintained curator row and no target-specific decision override were found. The sole adopted original and its supplement were recovered; current exact PubChem, ChEBI and FDA identity sources were checked. No claim of exhaustive bacterial pharmacology coverage is made. |
| access | Public publisher, PMC, Europe PMC and FDA retrievals; 305306-primary-fetch.json; 305306-supp-fetch.json; 305306-final-fetch.json; 305306-image-fetch.json | context_only | Publisher image/article routes returned HTML challenge content and one supplement route failed DNS. PMC direct supplement download also returned HTML instead of DOCX. The actual original DOCX was recovered from Europe PMC supplementaryFiles, and actual JPEG figures were recovered from PMC CDN links. Failed payloads were not treated as inspected figures or supplements. No paid or contact route was used. |
| gates | Actual focused chemistry, native schema and strict commands; 306-focused-results.json and companion logs | supports | Actual focused chemistry, schema and strict validation all exited zero against the unchanged exact record. These checks do not detect the primary-source strain-scope problem. |
| root-alias-snippet | scripts/seed_from_sources.py; .claude/skills/curate-yaml-record/references/review-checklist.md; src/antibioticmech/schema/antibioticmech.yaml; Curator importer lines 673–687; checklist Evidence standard; SynonymType enum | supports | Root inspected the maintained importer: every curator alias is assigned EXACT_SYNONYM; evidence_snippet and evidence_notes pass through to distinct native fields. The checklist reserves snippet for verbatim text, and the schema supports BRAND_NAME. A source summary and product brand therefore require different bounded corrections without changing the parent identity. |

## Limits And Additional Notes

- The full original main text and all Figure 1/5 panels were inspected. The complete supplementary DOCX text, Table S1 cells and Table S2 were read; supplementary figure captions were read but every image panel was not independently quantified.
- The original source itself inconsistently calls avian/environmental isolates clinical and uses GD18-KP-60 once where Table S1 gives GD18-KP-602. The draft preserves the explicit source conflict and uses the detailed Methods/table for origin.
- The Results state a uniform cladribine MIC but the supplementary MIC table contains carbapenem comparators. No unprovided per-isolate cladribine raw measurements or exact time-kill digitization is inferred.
- The study provides no catalog or independent lot analysis, direct bacterial target proof, positive-antibiotic efficacy comparator, pharmacokinetics or long-term safety data. No clinical antibiotic claim or causal chain is inferred.
- The FDA label was read for chemical identity, formulation and host-pharmacology context only; its full clinical safety or efficacy literature was outside this antibacterial record review.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record, source table, curation status or history was altered.
- Native schema and strict checks used the batch 031 environment. Independent molecular checks used the existing batch 019 RDKit interpreter against batch 031 cwd.
- All optional links, tags and notes were checked against this exact target. Discovery leads were not treated as evidence without the stated original-source reading.
- Root audit added the Leustatin type finding and explicit paraphrase placement correction after reading the full native record, draft evidence and maintained importer. Original draft preserved in session scratch; no saved bundle was rewritten.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T132715Z-cladribine-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cladribine: coherent parent identity with evidence-scope and brand-typing
  corrections'
started_at: '2026-10-21T13:04:59Z'
finished_at: '2026-10-21T13:27:15Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. The entire native
    record, exact maintained source row, source ownership and history were read. Independent
    molecular checks, live official groundings and original source text were assessed,
    with original figures and supplements inspected where specified.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'The exact cladribine parent structure and antibacterial eligibility are
  supported. One minor native evidence-scope correction is needed: the source summary
  describes growth inhibition and bactericidal activity against clinical isolates,
  while the original growth/time-kill figures use a reference strain and two migratory-bird
  isolates. The mixed-origin MIC panel and mouse lung-burden result should be described
  separately. Cellular stress responses do not establish direct bacterial targets.
  A second minor correction concerns Leustatin, a formulation brand currently typed
  as an exact chemical synonym. The corrected source interpretation belongs in notes;
  snippet is reserved for a short verbatim passage.'
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: conf/sources.yaml
    sha256: 4a2dcd7a3a88953b6cb35b51a48ed77b626c3af2cbb542b0d38ba10540ed7df9
    role: context
  - path: curation/curator_antibiotics.tsv
    sha256: 224cbb7261add427184b2762a29c2ff3e85c85e0a06cf22b144545346487247b
    role: context
  - path: curation/decisions.tsv
    sha256: a5834b44307b0449b0df9362c551b7fcd707f3ae51f73d429d37d51f5a169d61
    role: context
  - path: data/antibiotics/antibacterial/cladribine.yaml
    sha256: a024d4e03191b0ac456e759527642619e9ee88a55a5f11516cd013c29d111e24
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/chebi_antimicrobials.tsv
    sha256: 4c33e56c3c342be657309f720f5b5cb9cad1fae13bec202ef99e449503c32004
    role: context
  - path: data/raw/chebi_role_names.tsv
    sha256: 5c476c0aacd7c98d7241d2343a6fc41ee9eb9338077404c5b011a04bf40c6ac5
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/extract_source_inventory.py
    sha256: bb1606fd07cd8187640b5200a21ec090bb06683397d691e87ddd6884ea768860
    role: context
  - path: scripts/seed_from_sources.py
    sha256: be66eca74d22a3daa9ac6ff73d437c6c56e8d85b97f6877fdf3de77e2ab64680
    role: context
  - path: src/antibioticmech/schema/antibioticmech.yaml
    sha256: de62be2dd2dd55f141a0c14ff666eaa00efc6f3b431d651d0196ebcfddfbb301
    role: context
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
targets:
- target_id: antibioticmech:curator-d33759f162
  path: data/antibiotics/antibacterial/cladribine.yaml
  label: Cladribine
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: 'Maintained exact curator inventory: identity, definition and source evidence'
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator-inventory seeding transform
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Any grounding or exclusion override
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 306; one exact record. All 13 initial input hashes were
    preserved, and all 21 expanded input hashes were rechecked.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:curator-d33759f162
  exclusions:
  - target: Antineoplastic and immunomodulatory clinical mechanisms as proven bacterial
      targets; formulated products as the experimental reagent
    reason: The native antibacterial evidence concerns purchased cladribine in bacterial
      cultures and a mouse infection model. Host pharmacology and product regulatory
      status have distinct experimental scope.
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-d33759f162
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    306 (cwd /private/tmp/antibioticmech-record-reviews-031)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-d33759f162
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cladribine.yaml (cwd /private/tmp/antibioticmech-record-reviews-031)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-d33759f162
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cladribine.yaml --out /private/tmp/am-review-session/306-strict.tsv
    (cwd /private/tmp/antibioticmech-record-reviews-031)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:curator-d33759f162
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just qc
  exit_code: 2
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-verify-corpus
  name: Generated corpus reproduction
  status: passed
  required: true
  summary: 2939 expected and present; zero missing, unexpected, drifted fields or
    lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic
    retained.
  target_ids:
  - antibioticmech:curator-d33759f162
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just verify-corpus
    --summary
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-review-queue
  name: Native review-readiness inventory
  status: passed
  required: false
  summary: 2859 native unsigned readiness rows written; this status queue does not
    determine structured-review coverage.
  target_ids:
  - antibioticmech:curator-d33759f162
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just review-queue
    --limit 0 --tsv /private/tmp/am-review-session/native-queue.tsv
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-tests-platform-partial
  name: Supplementary test suite with two unavailable modules excluded
  status: passed
  required: false
  summary: 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy
    native library were explicitly excluded; this does not replace full QC.
  target_ids:
  - antibioticmech:curator-d33759f162
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q -ra --ignore=tests/test_chemical_embedding.py --ignore=tests/test_chemical_map_site.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-validate-all
  name: Full closed-schema validation
  status: passed
  required: true
  summary: 2939 files, zero ERROR rows.
  target_ids:
  - antibioticmech:curator-d33759f162
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-all
    --quiet --workers 2 --out /private/tmp/am-review-session/corpus-validation.tsv
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-chemical-map-check
  name: Chemical map consistency
  status: failed
  required: false
  summary: Exited 1 on the same pinned SciPy native library import failure.
  target_ids:
  - antibioticmech:curator-d33759f162
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just chemical-map-check
  exit_code: 1
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-render-check
  name: Generated site consistency
  status: passed
  required: false
  summary: 2939 compound pages and seven class pages current.
  target_ids:
  - antibioticmech:curator-d33759f162
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just render-check
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-report
  name: Corpus statistics
  status: passed
  required: false
  summary: Corpus report completed successfully.
  target_ids:
  - antibioticmech:curator-d33759f162
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just report
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-corpus-integrity
  name: Full-corpus history/evidence/reference invariants
  status: passed
  required: true
  summary: 23 full-corpus integrity tests passed, including seed history, evidence
    placement and internal references.
  target_ids:
  - antibioticmech:curator-d33759f162
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cladribine.yaml
  locator: Entire 53-line native YAML, including all three synonyms, source evidence,
    chemical fields and single history event
  accessed_at: '2026-10-21T13:23:10Z'
  support: supports
  summary: The record has a stable curator-minted identifier, PROPOSED curation status,
    MINTED grounding and antibacterial role. Its definition and sole evidence snippet
    cite the 2026 original paper. PubChem CID 20279 is its only external chemical
    xref. No native molecular target, causal graph, activity_spectrum, resistance
    determinant, producer, clinical status or dataset assertion is populated.
  snapshot_sha256: 81ac6b1025c8126ff30b33960b8e9ae503f6dfabcb6fd6b934896f5027e0c934
- evidence_id: owners
  kind: record_content
  reference: curation/curator_antibiotics.tsv; scripts/seed_from_sources.py; curation/decisions.tsv
  locator: Exact maintained curator row 22; source concept and seeding transform
  accessed_at: '2026-10-21T13:23:10Z'
  support: supports
  summary: The maintained curator row, not the generic ChEBI inventory, owns this
    record's identity, definition and evidence summary. The expanded target ownership
    was corrected accordingly while preserving the initial capture and all 13 initial
    hashes. All 21 expanded hashes were rechecked. No target-specific decision override
    was found with hidden and ignored files included.
  snapshot_sha256: cdf4c7b46964728a01141c8e5993152f263c9a45e40d1dd8ab71f93b49b21cc4
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/review-yaml-record/SKILL.md; docs/record-review-profile.md;
    .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Exact identity, source ownership, primary evidence scope and optional completeness
  accessed_at: '2026-10-21T13:23:10Z'
  support: supports
  summary: The review distinguishes antimicrobial eligibility from clinical approval
    and does not require optional targets, quantitative activity or a causal graph
    without suitable evidence. MINTED grounding and PROPOSED curation are different
    concepts and are not automatically invalidated by a newly checked external match.
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/20279/property/InChI,InChIKey,MolecularFormula,MolecularWeight,ExactMass,CanonicalSMILES,IsomericSMILES/JSON
  locator: Current PubChem CID 20279 molecular properties
  accessed_at: '2026-10-21T13:13:04.184026Z'
  support: supports
  summary: The sole asserted chemical xref resolves to cladribine with full key PTOAARAWEBMLNO-KVQBGUIXSA-N,
    C10H12ClN5O3 and the same three assigned stereocentres. The native structure_source
    and historical retrieval date describe this exact compound; the current comparison
    does not rewrite historical provenance.
  snapshot_sha256: 5269d38a0e9d992f2fc3a3fa4ad77d256883e6475cf2400c559b28c8d3c69fe9
- evidence_id: chebi-comparator
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/567361/
  locator: Current CHEBI:567361 names, definition and structural encodings; independent
    comparison only
  accessed_at: '2026-10-21T13:13:51.087687Z'
  support: supports
  summary: Current ChEBI cladribine has the same complete standard InChI and key as
    the native graph. Its host antineoplastic and immunosuppressive annotations are
    not evidence of bacterial targets. This newly inspected exact grounding is a possible
    future enrichment; it is not an asserted native xref or permission to replace
    the stable curator identifier.
  snapshot_sha256: 965e22ac37921cac133069fc327d2291471fe9318c4705ea305c53dd5a784a84
- evidence_id: chemistry
  kind: validation
  reference: Independent molecular and source-mint calculation
  locator: 306-chemistry.json; 305306-xref-chemistry.json; 305306-final-audit.json,
    target 306
  accessed_at: '2026-10-21T13:23:10Z'
  support: supports
  summary: Both native encodings yield one neutral component, formula C10H12ClN5O3,
    the full stored key, three assigned stereocentres, average mass 285.691 and exact
    mass 285.062866924. PubChem and current ChEBI encodings agree. The curator mint
    antibioticmech:curator-d33759f162 recomputes correctly from its source identity.
  snapshot_sha256: 82f2acf8b1f965f4d7894ea9e54f7063aee348ce5dac7aec9961f0501a06cc3e
- evidence_id: gsrs-name
  kind: authority
  reference: https://precision.fda.gov/uniisearch/srs/unii/47m74x9yt5
  locator: Official FDA substance entry UNII 47M74X9YT5
  accessed_at: '2026-10-21T13:18:34.605146Z'
  support: supports
  summary: The ingredient entry gives the same formula and full key and lists 2-CdA,
    2-chlorodeoxyadenosine and LEUSTATIN among its names. It corroborates the name
    association; a substance listing does not by itself imply approval for an antibacterial
    indication.
  snapshot_sha256: 651b2003cebf93d15f5eb160dc13d8f8da4e7f1260caa12b578f21c20246d960
- evidence_id: brand-material
  kind: authority
  reference: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020229s034lbl.pdf
  locator: Historical FDA Leustatin label, Description pp1-2
  accessed_at: '2026-10-21T13:18:34.601886Z'
  support: supports
  summary: Leustatin is a cladribine injection containing 1 mg/mL active cladribine;
    sodium chloride is explicitly inactive. The chemical name identifies the same
    parent nucleoside, not a distinct cladribine sodium salt. The brand association
    is coherent, while the formulation and antineoplastic clinical use remain separate
    from the purchased material used in the bacterial study. Only identity/formulation
    and host-pharmacology context were inspected, not every clinical-label claim.
  snapshot_sha256: 1184cef0250e0879e88ef9f5debba7442a3e24a60782c56bef35f7420a3fce24
- evidence_id: role
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms
  locator: 305-term-33282.json, shared identical role-term lookup
  accessed_at: '2026-10-21T13:13:04.958806Z'
  support: supports
  summary: CHEBI:33282 denotes antibacterial agent, including substances that kill
    or slow bacterial growth. Measured growth inhibition is sufficient for this role;
    a clinical antibiotic approval or proof of a unique direct target is not required.
  snapshot_sha256: cfcdde8efaa8c0b72b938ed8429882c4f52a7e151423c736a26bb5533cfd5cf9
- evidence_id: original-index
  kind: primary_source
  reference: https://doi.org/10.1186/s12866-026-05197-z
  locator: PMID:42168872 / PMC13371293; complete original metadata and abstract
  accessed_at: '2026-10-21T13:13:04.284287Z'
  support: supports
  summary: The sole adopted DOI resolves to Liu and colleagues' 2026 original study
    of cladribine against carbapenem-resistant Klebsiella pneumoniae. Its abstract
    claims clinical isolates, cellular stress responses and mouse efficacy. The full
    Methods, figures and supplement were inspected rather than accepting all abstract
    terminology as exact experimental scope.
  snapshot_sha256: 020cf0b6323eca3454f9148e20ff05d58280359ab3c3b3cf0274bf86e0f7ded0
- evidence_id: original-material
  kind: primary_source
  reference: https://doi.org/10.1186/s12866-026-05197-z
  locator: 'Methods: Bacterial isolates, compound and antibiotics; MIC, growth and
    time-kill methods'
  accessed_at: '2026-10-21T13:13:51.087577Z'
  support: supports
  summary: The experimental material is named cladribine from MedChemExpress at greater
    than 98% purity, dissolved in DMSO. No catalog or independent lot structure analysis
    is given. Broth MIC uses twofold dilution in Mueller-Hinton medium at 37 C for
    16-18 h; growth curves use LB and OD600; time-kill assays start at 1×10^7 CFU/mL
    in Mueller-Hinton medium with colony counts over 24 h. These are separate endpoints,
    not a formulated Leustatin clinical trial.
  snapshot_sha256: be5a88f9d3c7c9e4ce3129b95c17f88f64538b7525794942c14ce6d31a40416e
- evidence_id: strain-supplement
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13371293/supplementaryFiles
  locator: Original DOCX Table S1, all cells inspected; 306-tableS1-rows.json; source
    file 306-supp/12866_2026_5197_MOESM1_ESM.docx
  accessed_at: '2026-10-21T13:17:20.880386Z'
  support: supports
  summary: Table S1 identifies ATCC 700603 as a laboratory strain; 21QH35K and 21QH43K
    as migratory-bird fecal isolates from 2021; GD18-KP-602 as a patient throat-swab
    isolate; and VH1-2 as a vegetable isolate. Its three MIC columns are meropenem,
    imipenem and ertapenem, not cladribine. The carbapenem-resistant isolates carry
    KPC-2; that does not establish resistance to cladribine. The supplement resolves
    the main-text GD18-KP-60/602 naming discrepancy in favor of GD18-KP-602.
  snapshot_sha256: 60c3e64fc94777449531067e2e720b83201cc4ac7d236115eb1708162a3c3875
- evidence_id: original-growth
  kind: primary_source
  reference: https://doi.org/10.1186/s12866-026-05197-z
  locator: Results first subsection and original Figure 1, all six panels visually
    inspected
  accessed_at: '2026-10-21T13:18:34.582507Z'
  support: supports
  summary: Results state a cladribine MIC of 64 micrograms/mL across the named panel
    and report a 2% DMSO control. Figure 1 growth/time-kill panels are specifically
    ATCC 700603, 21QH35K and 21QH43K. The latter two are avian, not patient isolates.
    At 8×MIC, viable counts remain below growing untreated controls; the curves show
    modest decline from initial counts rather than the control-to-treatment gap representing
    equivalent killing from baseline. The authors use bactericidal terminology, which
    should remain attributed and qualified rather than becoming an unbounded killing
    claim.
  snapshot_sha256: c2f9d852d5907b47de757b085351250b9e3dab012403dfac725e4b820f6fb120
- evidence_id: original-mouse
  kind: primary_source
  reference: https://doi.org/10.1186/s12866-026-05197-z
  locator: Mouse Results and animal Methods; original Figure 5 visually inspected
  accessed_at: '2026-10-21T13:18:34.585186Z'
  support: supports
  summary: The lung model uses 21QH35K, whose avian origin is specified in Methods
    and Table S1 despite being called clinical in Results. Female ICR mice receive
    cladribine 10 or 20 mg/kg intraperitoneally at 8 and 16 h, with lung counts measured
    at 24 h, n=6 per group. Reported burdens decline from 6.99 to 4.90 and 4.40 log10
    CFU/g. Figure 5 supports reduced lung burden. These are approximately 2.09- and
    2.59-log differences from untreated infected mice, not clinical cure or a bacterial
    time-kill endpoint.
  snapshot_sha256: 361303b117d84e7f74d3abfdb5f7e63e0438f1d2b40771af7194d4b935491b54
- evidence_id: original-mechanism
  kind: primary_source
  reference: https://doi.org/10.1186/s12866-026-05197-z
  locator: Full bacterial stress Results, corresponding Methods and Discussion limitations
  accessed_at: '2026-10-21T13:13:51.087577Z'
  support: supports
  summary: PI/NPN permeability, leakage, TEM, ROS/MDA, ATP and transcriptional changes
    are measured after cellular treatment. SDH and pyruvate-kinase activities are
    measured in treated-cell lysates after 12 h, not as purified-protein binding or
    direct inhibition. Porin and SOS-gene induction are stress responses. The authors
    explicitly describe these results as correlative and acknowledge that primary
    causality was not established. Host antineoplastic DNA pharmacology is not demonstrated
    as the bacterial initiating mechanism.
  snapshot_sha256: be5a88f9d3c7c9e4ce3129b95c17f88f64538b7525794942c14ce6d31a40416e
- evidence_id: original-limits
  kind: primary_source
  reference: https://doi.org/10.1186/s12866-026-05197-z
  locator: Discussion final limitations paragraph; Supplementary Table S2 and figure
    captions; mouse Methods
  accessed_at: '2026-10-21T13:13:51.087577Z'
  support: supports
  summary: The panel is limited, no positive-antibiotic comparator was included in
    the infection efficacy experiment, and pharmacokinetics and long-term safety were
    not studied. Lung cytokine transcripts and histology cannot isolate a host-directed
    effect from lower bacterial burden. Primer identity or expression change does
    not establish direct molecular targeting. Supplementary material was inspected
    as evidence of assay design and origin, not treated as a new independent replication.
  snapshot_sha256: be5a88f9d3c7c9e4ce3129b95c17f88f64538b7525794942c14ce6d31a40416e
- evidence_id: adapter
  kind: database
  reference: iModulonDB structured catalog
  locator: 297-adapter-catalog.json, already executed catalog inspected before open
    protein follow-up
  accessed_at: '2026-10-21T13:23:10Z'
  support: context_only
  summary: No Klebsiella pneumoniae dataset is listed in the available catalog. The
    native record does not name a bacterial protein or pathway. No E. coli surrogate
    or expression-component membership was invented for the K. pneumoniae experiments,
    and database coverage absence is not negative mechanistic evidence.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local ownership and bounded public-source search
  locator: 306-local-hits.txt; 306-focused-local-search.json; source retrieval manifests
  accessed_at: '2026-10-21T13:23:10Z'
  support: context_only
  summary: The initial repository-wide and focused curation/conf searches included
    hidden and ignored files. The exact maintained curator row and no target-specific
    decision override were found. The sole adopted original and its supplement were
    recovered; current exact PubChem, ChEBI and FDA identity sources were checked.
    No claim of exhaustive bacterial pharmacology coverage is made.
  snapshot_sha256: 0a8aa353e52a88c99068892103c1ececc61c8e202e4ac90a306558f2153aa311
  search_scope: 2026-10-21; exact queue 306 record identifier, names, full chemical
    key and adopted citation identifiers. Initial repository-wide and focused curation/conf
    searches included hidden and ignored files. Bounded free official, primary publisher
    and public archive retrievals are recorded in the cited manifests; no exhaustive
    literature-absence claim is made.
- evidence_id: access
  kind: search
  reference: Public publisher, PMC, Europe PMC and FDA retrievals
  locator: 305306-primary-fetch.json; 305306-supp-fetch.json; 305306-final-fetch.json;
    305306-image-fetch.json
  accessed_at: '2026-10-21T13:23:10Z'
  support: context_only
  summary: Publisher image/article routes returned HTML challenge content and one
    supplement route failed DNS. PMC direct supplement download also returned HTML
    instead of DOCX. The actual original DOCX was recovered from Europe PMC supplementaryFiles,
    and actual JPEG figures were recovered from PMC CDN links. Failed payloads were
    not treated as inspected figures or supplements. No paid or contact route was
    used.
  snapshot_sha256: e90a77aa72dbb0195d9798dfd256568bf114f08a9e2a06e12cad655b557996d9
  search_scope: 2026-10-21; exact queue 306 record identifier, names, full chemical
    key and adopted citation identifiers. Initial repository-wide and focused curation/conf
    searches included hidden and ignored files. Bounded free official, primary publisher
    and public archive retrievals are recorded in the cited manifests; no exhaustive
    literature-absence claim is made.
- evidence_id: gates
  kind: validation
  reference: Actual focused chemistry, native schema and strict commands
  locator: 306-focused-results.json and companion logs
  accessed_at: '2026-10-21T13:23:10Z'
  support: supports
  summary: Actual focused chemistry, schema and strict validation all exited zero
    against the unchanged exact record. These checks do not detect the primary-source
    strain-scope problem.
  snapshot_sha256: 408c4dffdc8d35f106ea97dd0cbd8f3cc8be7ea9eeafd49e2d25ce94815c5d88
- evidence_id: root-alias-snippet
  kind: record_content
  reference: scripts/seed_from_sources.py; .claude/skills/curate-yaml-record/references/review-checklist.md;
    src/antibioticmech/schema/antibioticmech.yaml
  locator: Curator importer lines 673–687; checklist Evidence standard; SynonymType
    enum
  accessed_at: '2026-10-21T13:27:02.677587Z'
  support: supports
  summary: 'Root inspected the maintained importer: every curator alias is assigned
    EXACT_SYNONYM; evidence_snippet and evidence_notes pass through to distinct native
    fields. The checklist reserves snippet for verbatim text, and the schema supports
    BRAND_NAME. A source summary and product brand therefore require different bounded
    corrections without changing the parent identity.'
assessments:
- assessment_id: identity
  area: identity
  topic: Exact synthetic parent, names and chemical properties
  outcome: concern
  summary: Native molecular encodings, PubChem and current ChEBI agree on the complete
    parent structure. FDA substance and historical label information corroborate the
    names and distinguish inactive sodium chloride from a drug salt. Leustatin denotes
    the labeled injection product, so its native EXACT_SYNONYM type needs the separate
    bounded correction below.
  target_ids:
  - antibioticmech:curator-d33759f162
  evidence_ids:
  - native
  - pubchem
  - chebi-comparator
  - chemistry
  - gsrs-name
  - brand-material
- assessment_id: grounding
  area: grounding
  topic: PubChem xref, MINTED grounding and source mint
  outcome: supported
  summary: The asserted CID is exact and the curator identifier is reproducible. CHEBI:567361
    is a verified optional external match, not evidence that the stable native identifier
    or its historical MINTED state is intrinsically wrong.
  target_ids:
  - antibioticmech:curator-d33759f162
  evidence_ids:
  - pubchem
  - chebi-comparator
  - chemistry
  - owners
  - rubric
- assessment_id: eligibility
  area: evidence
  topic: Antibacterial definition, class and role
  outcome: supported
  summary: Original cladribine growth inhibition and a mouse bacterial-burden endpoint
    support antibacterial eligibility. The study is preliminary and does not establish
    an approved antibacterial indication or general clinical efficacy.
  target_ids:
  - antibioticmech:curator-d33759f162
  evidence_ids:
  - role
  - original-material
  - original-growth
  - original-mouse
  - original-limits
- assessment_id: source-scope
  area: evidence
  topic: 'Native evidence summary: clinical isolates'
  outcome: concern
  summary: The native snippet groups growth inhibition and author-reported bactericidal
    activity under clinical isolates. The original figures instead test a reference
    strain and two avian isolates; the broader MIC panel has mixed origins and only
    one patient isolate. The snippet needs a bounded correction through the maintained
    curator inventory. The Liu et al. sentence is curator synthesis, not a verbatim
    source passage; place the corrected interpretation in evidence_notes and reserve
    evidence_snippet for exact quotation.
  target_ids:
  - antibioticmech:curator-d33759f162
  evidence_ids:
  - native
  - owners
  - strain-supplement
  - original-growth
  - original-mouse
- assessment_id: killing
  area: evidence
  topic: Author-reported bactericidal terminology and quantitative interpretation
  outcome: unknown
  summary: The snippet reports the authors' characterization, but Figure 1 shows a
    larger difference from growing controls than decline from starting inocula. Any
    future quantitative killing claim must identify baseline, concentration and time
    rather than equating suppression relative to controls with equivalent killing.
    No separate categorical native defect is inferred from the attributed wording
    alone.
  target_ids:
  - antibioticmech:curator-d33759f162
  evidence_ids:
  - original-growth
  - original-material
- assessment_id: mechanism
  area: completeness
  topic: Optional targets and causal graph
  outcome: unknown
  summary: The source supports cellular stress observations, not a validated direct
    target or causal ordering. SDH/PK lysate assays, porin/SOS expression, host drug
    pharmacology and iModulonDB coverage cannot justify direct-target annotations.
    Missing optional mechanisms are not a schema flaw.
  target_ids:
  - antibioticmech:curator-d33759f162
  evidence_ids:
  - original-mechanism
  - original-limits
  - adapter
  - rubric
- assessment_id: activity
  area: completeness
  topic: Optional quantitative activity_spectrum
  outcome: unknown
  summary: A useful original source exists, but isolate origins, MIC versus carbapenem
    comparator columns, growth/kill baselines, concentration units and mouse dose/endpoint
    must remain distinct. Assay values are not breakpoints or evidence that an entire
    taxon is resistant.
  target_ids:
  - antibioticmech:curator-d33759f162
  evidence_ids:
  - original-material
  - strain-supplement
  - original-growth
  - original-mouse
  - rubric
- assessment_id: host-clinical
  area: scope
  topic: Host pharmacology and clinical-product context
  outcome: supported
  summary: Leustatin provides exact active-ingredient/name context. Oncology or immunomodulatory
    use does not supply an antibacterial clinical claim, and cytokine changes in infected
    mice do not independently isolate a host target. Native clinical fields are unpopulated.
  target_ids:
  - antibioticmech:curator-d33759f162
  evidence_ids:
  - brand-material
  - gsrs-name
  - original-mouse
  - original-limits
  - native
- assessment_id: other-domains
  area: scope
  topic: Unpopulated resistance, producer and dataset assertions
  outcome: not_applicable
  summary: No such native claims require adjudication. KPC-2 and carbapenem comparator
    MICs concern resistance to other drugs, and purchased synthetic material is not
    evidence of a natural producer.
  target_ids:
  - antibioticmech:curator-d33759f162
  evidence_ids:
  - native
  - strain-supplement
  - original-material
- assessment_id: provenance
  area: provenance
  topic: Actual curator owner, PROPOSED status and one history event
  outcome: supported
  summary: The curated inventory and source seeding explain the record and its single
    proposal event. The scientific scope correction belongs to that maintained row
    and regenerated evidence, not a hand edit that seeding would overwrite. All captured
    hashes remain preserved.
  target_ids:
  - antibioticmech:curator-d33759f162
  evidence_ids:
  - owners
  - native
  - rubric
- assessment_id: schema
  area: schema
  topic: Focused deterministic gates
  outcome: supported
  summary: Native schema, strict validation and molecular consistency pass. These
    successes do not resolve the evidence-summary scope finding.
  target_ids:
  - antibioticmech:curator-d33759f162
  evidence_ids:
  - gates
  - chemistry
findings:
- finding_id: F1
  issue_key: cladribine-clinical-isolate-evidence-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The source summary mislabels the growth and time-kill panel as clinical isolates
  description: source_concepts[0].evidence[0].snippet reports growth inhibition and
    bactericidal activity against clinical isolates. Original Figure 1 uses ATCC 700603
    and isolates 21QH35K/21QH43K; Methods and Supplementary Table S1 identify the
    latter as migratory-bird fecal isolates. The broader MIC panel includes one patient
    throat-swab isolate plus avian and vegetable isolates. Revise the maintained source
    summary to distinguish this mixed-origin MIC panel, the reference/avian growth
    and time-kill experiments, and the 21QH35K mouse model. Preserve the supported
    antibacterial role and lung-burden result. Keep bactericidal terminology attributed
    to the authors and qualify control-versus-baseline interpretation if numerical
    killing claims are added. The same sentence is a curator paraphrase, not a verbatim
    passage. Move the corrected interpretation to evidence_notes, retaining the existing
    chemical-provenance notes, and omit evidence_snippet or replace it with a short
    exact passage.
  target_ids:
  - antibioticmech:curator-d33759f162
  field_paths:
  - source_concepts[0].evidence[0].snippet
  evidence_ids:
  - native
  - owners
  - strain-supplement
  - original-growth
  - original-mouse
  - root-alias-snippet
  rule_id: native-review-checklist:Evidence and Provenance
  native_severity: minor bounded organism-origin and endpoint scope error
  normalization_reason: The source remains the correct original study and supports
    antibacterial eligibility. The required correction narrows a redundant evidence
    summary rather than replacing the molecular identity, class or supported in vivo
    endpoint.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Maintained cladribine evidence summary
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source-concept evidence from the curator inventory
- finding_id: F2
  issue_key: cladribine-leustatin-brand-exact-synonym
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Type Leustatin as a brand name
  description: The historical FDA label identifies Leustatin as a cladribine injection
    with inactive formulation ingredients. The native synonym is explicitly EXACT_SYNONYM.
    Preserve this useful product association with BRAND_NAME typing through a maintained,
    reproducible source path. The curator importer currently assigns EXACT_SYNONYM
    to every input alias, so changing generated YAML or inserting an unparsed type
    prefix in the TSV would not implement the fix.
  target_ids:
  - antibioticmech:curator-d33759f162
  field_paths:
  - synonyms[1].synonym_type
  evidence_ids:
  - native
  - brand-material
  - gsrs-name
  - owners
  - rubric
  - root-alias-snippet
  rule_id: 'native-review-checklist: Identity'
  native_severity: minor alias typing
  normalization_reason: The active compound and brand association are correct; only
    the product-name type is overstrong.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Maintained curator names and evidence fields
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator synonym typing and evidence emission
actions:
- action_id: A1
  description: Correct the maintained cladribine evidence summary to preserve exact
    isolate origins and experimental endpoints.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:curator-d33759f162
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Maintained cladribine evidence summary
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source-concept evidence from the curator inventory
  acceptance_checks:
  - Identify 21QH35K and 21QH43K as avian isolates and reserve patient-origin wording
    for GD18-KP-602.
  - Separate the mixed-origin MIC panel from the Figure 1 reference/avian growth and
    time-kill panel and the avian-isolate mouse model.
  - Place the corrected synthesis in evidence_notes while preserving existing chemical
    provenance; reserve evidence_snippet for a short, verified verbatim source passage
    or leave it empty.
  - Preserve the supported antibacterial role and mouse lung-burden observation; do
    not relabel carbapenem MIC columns as cladribine data.
  - Regenerate through the maintained source workflow and run native schema, strict,
    provenance/history and applicable QC gates after separately authorized curation.
- action_id: A2
  description: Optionally enrich exact chemical grounding and primary activity without
    promoting correlated cellular responses to direct targets.
  finding_ids: []
  target_ids:
  - antibioticmech:curator-d33759f162
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Maintained exact identity and source evidence
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cladribine.yaml
    role: Curator-owned activity_spectrum or mechanistic observations through the
      validated writer
  acceptance_checks:
  - Consider the verified CHEBI:567361 match while preserving the stable identifier
    and documented grounding history.
  - Retain MedChemExpress cladribine material, purity, media, solvent, incubation,
    concentration units and endpoint scope.
  - Represent killing relative to the stated starting inoculum and controls; do not
    infer a baseline kill magnitude from control separation.
  - Keep treated-cell lysate assays, expression changes, host clinical pharmacology
    and mouse inflammatory endpoints distinct from direct bacterial target proof.
- action_id: A3
  description: Add a reproducible curator synonym classification path for Leustatin
    as BRAND_NAME, preserving the chemical aliases and source provenance.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:curator-d33759f162
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Maintained curator names and evidence fields
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator synonym typing and evidence emission
  acceptance_checks:
  - Leustatin is emitted as BRAND_NAME; 2-CdA and the chemical name retain their supported
    types.
  - The typed alias survives regeneration and documented schema/strict and corpus-reproduction
    gates; no formulation ingredient is added to the parent molecular structure.
limitations:
- The full original main text and all Figure 1/5 panels were inspected. The complete
  supplementary DOCX text, Table S1 cells and Table S2 were read; supplementary figure
  captions were read but every image panel was not independently quantified.
- The original source itself inconsistently calls avian/environmental isolates clinical
  and uses GD18-KP-60 once where Table S1 gives GD18-KP-602. The draft preserves the
  explicit source conflict and uses the detailed Methods/table for origin.
- The Results state a uniform cladribine MIC but the supplementary MIC table contains
  carbapenem comparators. No unprovided per-isolate cladribine raw measurements or
  exact time-kill digitization is inferred.
- The study provides no catalog or independent lot analysis, direct bacterial target
  proof, positive-antibiotic efficacy comparator, pharmacokinetics or long-term safety
  data. No clinical antibiotic claim or causal chain is inferred.
- The FDA label was read for chemical identity, formulation and host-pharmacology
  context only; its full clinical safety or efficacy literature was outside this antibacterial
  record review.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record, source table, curation status or history was altered.
- Native schema and strict checks used the batch 031 environment. Independent molecular
  checks used the existing batch 019 RDKit interpreter against batch 031 cwd.
- All optional links, tags and notes were checked against this exact target. Discovery
  leads were not treated as evidence without the stated original-source reading.
- Root audit added the Leustatin type finding and explicit paraphrase placement correction
  after reading the full native record, draft evidence and maintained importer. Original
  draft preserved in session scratch; no saved bundle was rewritten.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://pubchem.ncbi.nlm.nih.gov/compound/20279
- https://www.ebi.ac.uk/chebi/CHEBI:567361
- https://doi.org/10.1186/s12866-026-05197-z
tags:
- cladribine
- primary-assay-scope
- isolate-origin
```
