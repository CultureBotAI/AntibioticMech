# Fumagillin: coherent meroterpenoid identity with unresolved antibacterial-drug role

- Review: 20261021T170349Z-fumagillin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:45:53Z
- Finished UTC: 2026-10-21T17:03:49Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native fully configured fumagillin structure agrees across independent chemical sources. Original biosynthetic and strain-level metabolite studies support Aspergillus fumigatus production, and original bee and human microsporidiosis studies support the stated treatment context. A recent original antibacterial abstract supplies positive antibacterial evidence, but does not establish treatment or prevention of bacterial infections. One provisional major finding asks for adjudication of that narrower inherited drug-role assertion.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position478; one exact record in path order. Original thirteen hashes remain unchanged within sixteen inputs after actual MIBiG/readiness ownership was appended.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:48635 | data/antibiotics/antibacterial/fumagillin.yaml | generated | fumagillin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:48635 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:48635 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:48635 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:48635 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:48635 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:48635 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:48635 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:48635 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:48635 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:48635 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:48635 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:48635 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact configured meroterpenoid and names

identity: supported. Targets: CHEBI:48635.

Independent structures, masses, six centres and E-chain geometry agree. Brands/INNs and exact/common names are appropriately separated; KNApSAcK displayed-key inconsistency does not contradict its two matching structure strings.

### Species, strain and biosynthetic provenance

evidence: supported. Targets: CHEBI:48635.

Native is an explicitly qualified MIBiG association. The2013 original supports the species/pathway while distinguishing Af293 genomic reference from CEA17 experiments; the2016 profile independently supports Af293 production. The source method annotations must retain those limits.

### Bee-use definition and antifungal/antiprotozoal scope

evidence: supported. Targets: CHEBI:48635.

Original bee and human studies support the microsporidial use context. Tested salt formulation and named organisms are preserved; no universal efficacy, current approval or host-selective mechanism is inferred.

### Antibacterial activity versus antibacterial drug use

evidence: concern. Targets: CHEBI:48635.

The2026 original abstract supports activity in bacterial experiments. The inspected treatment evidence concerns microsporidia, while CHEBI36047 requires bacterial infection treatment/prevention. The inherited narrower role remains unverified and needs claim-specific adjudication.

### Mechanism, resistance and optional annotations

completeness: supported. Targets: CHEBI:48635.

No native named target or quantitative activity is asserted. Human MetAP2, fungal biosynthesis enzymes, reporter responses, phage inhibition and Nosema dose responses are distinct evidence types. Their absence as new target/causal objects is not a defect.

### Maintained source/history and link semantics

provenance: supported. Targets: CHEBI:48635.

All adopted/native citations, source concepts and seven histories were assessed at stated access depths. Native quality and citation-attachment limits are visible; exact chemistry agrees and broader drug/document links are kept separate.

## Findings

### F1: Adjudicate the inherited antibacterial-drug role separately from in-vitro activity

major / open / provisional; issue key: fumagillin-antibacterial-drug-use-role-unresolved.

CHEBI36047 asserts use to treat or prevent bacterial infections. The inspected primary treatment evidence concerns Nosema or E.bieneusi, while the2026 bacterial experiment supports activity and proposed drug development. The record/current ChEBI do not provide claim-specific evidence for the narrower bacterial-use role. This is an unresolved support gap, not a confirmed statement that no such use exists or that fumagillin lacks antibacterial activity.

## Recommended Actions And Acceptance Checks

### A1

Resolve the bacterial treatment/prevention evidence for CHEBI36047 before scientific sign-off.

- Inspect a primary source or authoritative exact indication establishing treatment/prevention of bacterial infection, with organism, material and use context, or remove/qualify this specific inherited role through maintained ownership.
- Retain independently supported antibacterial activity and microsporidial treatment context; do not equate bacteriophage inhibition, host angiogenesis effects or fungal biosynthesis with bacterial treatment.
- Preserve provenance and source quality; regenerate role changes reproducibly and run focused schema/strict, reference, corpus and QC checks. Do not alter the valid structure to resolve an evidence-scope issue.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/fumagillin.yaml; Entire native YAML, eight synonyms, six parents, five roles, five exact xrefs, drug/document links, producer/evidence and seven histories | supports | The SEEDED exact ChEBI record denotes neutral C26H34O7, NGGMYCMLYOUNGM-CSDLUJIJSA-N, six configured centres and four E double bonds. It describes the fumagillol/dioic-acid ester and Nosema control in bees. Names distinguish brands and INNs. The Af293 producer has MIBiG4.0.1 entry5 questionable quality and explicit source-citation placement notes. No native MIC, named molecular target, resistance gene, clinical approval, causal graph or transcriptomic dataset is asserted. |
| owners | 478-source-rows.json; data/raw/mibig_producers.tsv; scripts/extract_mibig_producers.py; scripts/seed_from_sources.py; Complete ChEBI and MIBiG rows and relevant maintained producer/seed ownership | supports | ChEBI owns native identity/names/roles/definition. The MIBiG row has one compound, exact matching standard key, stereo_complete true, taxon330879 Af293, entry5/questionable, expert_reviewed false, three link methods and DOI10.1021/ja312503y with reference_basis compound_evidence. Native correctly distinguishes that citation attachment from a primary citation assigned to the producer link. Seven history events and all source mints were inspected; original captured inputs remain unchanged. |
| identity | CHEBI:48635; PubChem6917655; KEGG C09668; LIPIDMAPS LMPR0103060003; KNApSAcK C00003133; 048-root-authority-chemistry.json and 477478-knapsack-check.json, independently parsed exact graphs | supports | Native SMILES/InChI, current ChEBI and PubChem, KEGG molfile, LIPIDMAPS SMILES/InChI and adopted MIBiG graph all reproduce the complete native key and formula. The KNApSAcK displayed key is NGGMYCMLYOUNGM-XPNXQVIANA-N, but its actual SMILES and standard InChI both independently reproduce the native CSDLUJIJSA key. That external display inconsistency is noted without claiming the linked graph is a different stereoisomer. CAS23110-15-8 is corroborated by these sources. |
| terms | CHEBI:48635; CHEBI:133131,25807,33308,36244,64419,87113; CHEBI:33281,35718,35820,36047,86327; Complete current compound and every asserted parent/role definition | supports | The spiroepoxide, organooxygen heterocyclic antibiotic, carboxylic ester, dicarboxylic-acid monoester and meroterpenoid parents fit. Antifungal-drug/agent and historical antiprotozoal-drug context can be reconciled with microsporidial treatment and the evolving classification of those organisms. In contrast, CHEBI36047 explicitly requires use to treat or prevent bacterial infections; in-vitro antibacterial activity alone is insufficient. Current ChEBI repeats that role without a claim-specific clinical citation. |
| adopted | PMID:14514693,14809278,15723631,23121865,23488861,23505365; All six adopted citation records; complete available abstracts | supports | PM14514693 studies protonation/human MetAP2 inhibition;15723631 is an angiogenesis review;23121865 concerns erythrocyte eryptosis;23488861 is the original fungal biosynthesis paper;23505365 is the original Nosema/bee study. PM14809278 is the1951 amebicidal antibiotic report with no available abstract, so title/metadata alone were inspected. Host antiangiogenesis/toxicity and microsporidial treatment do not demonstrate bacterial treatment. Additional original depths are recorded separately. |
| biosynthesis | PMID:23488861; DOI:10.1021/ja312503y; PMC3652892; Complete original main text through the conclusion, retrieved as NCBI EFetch XML after Europe PMC500/PMCchallenge | supports | The fma cluster was identified using the Af293 genome. Functional deletion experiments were performed in A.fumigatus CEA17 akuBKU80; loss and feeding restoration of fumagillin link PKS and terpene-cyclase functions. Heterologous yeast expression and enzyme assays resolve pathway intermediates. Those biosynthetic proteins are not antibacterial targets. Af293 genome assignment and CEA17 experiments must not be collapsed into an Af293 knockout experiment. The work is positive species/pathway evidence, with its exact strain scope retained. |
| af293 | PMID:27830189; DOI:10.1128/mSphere.00227-16; PMC5082629; Original secondary-metabolite Results, Figure4 caption, extraction/analysis Methods and complete abstract | supports | The original2016 comparison includes Af293, CEA10 and two ISS isolates. HPLC-DAD-MS after five days on GMM agar at30C identifies fumagillin in Af293 and other strains. This independently supports the exact named native producer at metabolite-profile level; it does not assign every2013 knockout/heterologous method specifically to Af293. No natural-product absolute stereochemical re-determination is claimed from this profiling study. |
| bee | PMID:23505365; DOI:10.1371/journal.ppat.1003185; PMC3591333; Complete original main Methods, Results and Discussion including Tables1–2 | supports | The material is explicitly bicyclohexylammonium fumagillin, abbreviated fumagillin by the authors. Controlled oral Nosema infections of honey bees are suppressed below the counting limit at25mg/L treatment; lower levels allow recovery and, for N.ceranae under some conditions, increased spore production. This supports the native historical bee-use statement without transferring formulation concentrations to a free-acid MIC. MetAP2 sequence comparisons and bee midgut proteomics are not direct binding measurements in Nosema, nor bacterial resistance evidence. The source does not support universal resistance-free efficacy. |
| human | PMID:12075057; DOI:10.1056/NEJMoa012924; Complete original randomized-trial abstract; main paper inaccessible via403 | supports | The2002 trial studies12 immunocompromised patients with E.bieneusi intestinal microsporidiosis. It reports microsporidial clearance with fumagillin versus placebo, along with serious blood-cell adverse effects in some treated patients. It supports an antimicrosporidial treatment context, not treatment of bacterial infection. No current prescribing recommendation, approval status or universal safety claim is inferred. |
| recent-bacterial | DOI:10.1016/j.microb.2026.100791; https://www.sciencedirect.com/science/article/pii/S2950194626001378; Complete original publisher abstract exposed by search; direct main-text retrieval403 | partial | The2026 original reports purification and FTIR/LC-ESI-MS/NMR identification of fumagillin from A.fumigatus MBL_F107, with antibacterial experiments including MRSA and antifungal activity. Its reporter and imaging observations concern protein-synthesis response and cellular deformation. This is positive exact-named antibacterial evidence at abstract depth; no exact MIC, full material characterization, direct binding mechanism or treatment use is reconstructed. MBL_F107 is not Af293. |
| patent | patent:US2652356; Original patent descriptive paragraphs on identification, producer and activity | context_only | The patent concerns fumagillin preparation from A.fumigatus H-3 and reports anti-S.aureus-bacteriophage and E.histolytica activity. Inhibition of a phage must not be read as killing its bacterial host. The historical approximate formula is not substituted for the modern validated molecular structure. This is a topical document association rather than exact chemical equivalence. |
| search | 478-local-hits.txt;478-owners-search.json;048-root-fetch1-manifest.json through048-root-fetch7-manifest.json; Ignored-inclusive owner search, all adopted citations, bounded primary producer and antibacterial-use follow-up | context_only | Public searches recovered original microsporidial treatment, biosynthesis, Af293 profiling and the2026 antibacterial abstract. No primary bacterial-treatment indication was established in the inspected trail, but this is not a proof of global non-use or inactivity. Direct current MIBiG JSON attempts returned404, while the exact versioned adopted row remained available. Proprietary Reaxys structure was not independently accessed. KNApSAcK and LIPIDMAPS structures were checked directly. DrugBank/DrugCentral remain broader drug-context associations. |
| adapter | 475-imodulon-datasets.json; Earlier actual same-session adapter catalog, independently read for fungal coverage | context_only | The actual catalog lists covered bacteria and an archaeon but no Aspergillus, Nosema or bee dataset. No matching iModulonDB dataset is applicable to the native fungal producer assertion. This catalog reuse is stated explicitly; no new gene or component query is claimed, and lack of coverage is not negative biological evidence. |
| gates | 478-focused-results.json;478-chemistry.json;048-root-authority-chemistry.json; Actual focused schema/strict/internal chemistry and independent external graph checks | supports | All focused executions exit0. Sixteen captured inputs remain unchanged. Internal chemistry and source reproducibility do not validate the narrower antibacterial-drug use claim. |

## Limits And Additional Notes

- The2026 primary bacterial study was accessible only as its complete publisher abstract; direct main text returned403 and the exact DOI Europe PMC query returned no indexed result. No quantitative MIC or detailed assay condition is extracted.
- The1951 adopted paper has no available abstract; its metadata/title are not full-text evidence. The2002 clinical original was read at abstract level; adopted host-toxicity and review papers were likewise assessed at abstract depth.
- The2013 biosynthesis main text and2013 bee main text were read in full. The2016 Af293 study was read at selected metabolite Results/Methods and abstract depth; raw chromatograms/genomics and supplemental spectra were not reprocessed.
- The MIBiG association is supported by its frozen exact row and independently inspected papers; current direct JSON routes were unavailable. The reference attachment does not convert CEA17 knockout methods into Af293-specific experiments.
- KNApSAcK displays an inconsistent historical key, while its SMILES and InChI parse to the native structure. Reaxys remains source-attributed; broader drug links are not treated as independent exact-structure evidence.
- A bounded search failed to establish bacterial treatment/prevention use. The provisional finding is not a universal negative and does not deny the positive2026 antibacterial report.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T170349Z-fumagillin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Fumagillin: coherent meroterpenoid identity with unresolved antibacterial-drug
  role'
started_at: '2026-10-21T16:45:53Z'
finished_at: '2026-10-21T17:03:49Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. The entire record
    and maintained source were read, independent chemistry calculated, asserted chemical
    groundings checked and exact-compound primary literature assessed with explicit
    access boundaries.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The native fully configured fumagillin structure agrees across independent
  chemical sources. Original biosynthetic and strain-level metabolite studies support
  Aspergillus fumigatus production, and original bee and human microsporidiosis studies
  support the stated treatment context. A recent original antibacterial abstract supplies
  positive antibacterial evidence, but does not establish treatment or prevention
  of bacterial infections. One provisional major finding asks for adjudication of
  that narrower inherited drug-role assertion.
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
  - path: data/antibiotics/antibacterial/fumagillin.yaml
    sha256: e364dc524ed72f4e5587fecc8f872d5f41625715308ce3e1911ca478af977c8c
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
  - path: curation/record_review_queue.tsv
    role: context
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
  - path: data/raw/mibig_producers.tsv
    role: context
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
  - path: scripts/extract_mibig_producers.py
    role: context
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
targets:
- target_id: CHEBI:48635
  path: data/antibiotics/antibacterial/fumagillin.yaml
  label: fumagillin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position478; one exact record in path order.
    Original thirteen hashes remain unchanged within sixteen inputs after actual MIBiG/readiness
    ownership was appended.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:48635
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:48635
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    478
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:48635
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/fumagillin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:48635
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/fumagillin.yaml --out /private/tmp/am-review-session/478-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:48635
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
  - CHEBI:48635
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
  - CHEBI:48635
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
  - CHEBI:48635
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
  - CHEBI:48635
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
  - CHEBI:48635
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
  - CHEBI:48635
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
  - CHEBI:48635
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
  - CHEBI:48635
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/fumagillin.yaml
  locator: Entire native YAML, eight synonyms, six parents, five roles, five exact
    xrefs, drug/document links, producer/evidence and seven histories
  accessed_at: '2026-10-21T16:58:19Z'
  support: supports
  summary: The SEEDED exact ChEBI record denotes neutral C26H34O7, NGGMYCMLYOUNGM-CSDLUJIJSA-N,
    six configured centres and four E double bonds. It describes the fumagillol/dioic-acid
    ester and Nosema control in bees. Names distinguish brands and INNs. The Af293
    producer has MIBiG4.0.1 entry5 questionable quality and explicit source-citation
    placement notes. No native MIC, named molecular target, resistance gene, clinical
    approval, causal graph or transcriptomic dataset is asserted.
- evidence_id: owners
  kind: record_content
  reference: 478-source-rows.json; data/raw/mibig_producers.tsv; scripts/extract_mibig_producers.py;
    scripts/seed_from_sources.py
  locator: Complete ChEBI and MIBiG rows and relevant maintained producer/seed ownership
  accessed_at: '2026-10-21T16:58:19Z'
  support: supports
  summary: ChEBI owns native identity/names/roles/definition. The MIBiG row has one
    compound, exact matching standard key, stereo_complete true, taxon330879 Af293,
    entry5/questionable, expert_reviewed false, three link methods and DOI10.1021/ja312503y
    with reference_basis compound_evidence. Native correctly distinguishes that citation
    attachment from a primary citation assigned to the producer link. Seven history
    events and all source mints were inspected; original captured inputs remain unchanged.
  snapshot_sha256: ebe068056510f434b58fd316b533524d31ae6a8e51f011146f7e19993e76b8ba
- evidence_id: identity
  kind: validation
  reference: CHEBI:48635; PubChem6917655; KEGG C09668; LIPIDMAPS LMPR0103060003; KNApSAcK
    C00003133
  locator: 048-root-authority-chemistry.json and 477478-knapsack-check.json, independently
    parsed exact graphs
  accessed_at: '2026-10-21T16:58:19Z'
  support: supports
  summary: Native SMILES/InChI, current ChEBI and PubChem, KEGG molfile, LIPIDMAPS
    SMILES/InChI and adopted MIBiG graph all reproduce the complete native key and
    formula. The KNApSAcK displayed key is NGGMYCMLYOUNGM-XPNXQVIANA-N, but its actual
    SMILES and standard InChI both independently reproduce the native CSDLUJIJSA key.
    That external display inconsistency is noted without claiming the linked graph
    is a different stereoisomer. CAS23110-15-8 is corroborated by these sources.
  snapshot_sha256: fe824fa5edc3ec374c65fdab2cc222b57b90f8cee88df20c83410bf37b9a2982
- evidence_id: terms
  kind: authority
  reference: CHEBI:48635; CHEBI:133131,25807,33308,36244,64419,87113; CHEBI:33281,35718,35820,36047,86327
  locator: Complete current compound and every asserted parent/role definition
  accessed_at: '2026-10-21T16:58:19Z'
  support: supports
  summary: The spiroepoxide, organooxygen heterocyclic antibiotic, carboxylic ester,
    dicarboxylic-acid monoester and meroterpenoid parents fit. Antifungal-drug/agent
    and historical antiprotozoal-drug context can be reconciled with microsporidial
    treatment and the evolving classification of those organisms. In contrast, CHEBI36047
    explicitly requires use to treat or prevent bacterial infections; in-vitro antibacterial
    activity alone is insufficient. Current ChEBI repeats that role without a claim-specific
    clinical citation.
  snapshot_sha256: 5a4f3cc60e95c624b317aee901bd958524108e7ad0bb710086f35b14a82fa50e
- evidence_id: adopted
  kind: primary_source
  reference: PMID:14514693,14809278,15723631,23121865,23488861,23505365
  locator: All six adopted citation records; complete available abstracts
  accessed_at: '2026-10-21T16:58:19Z'
  support: supports
  summary: PM14514693 studies protonation/human MetAP2 inhibition;15723631 is an angiogenesis
    review;23121865 concerns erythrocyte eryptosis;23488861 is the original fungal
    biosynthesis paper;23505365 is the original Nosema/bee study. PM14809278 is the1951
    amebicidal antibiotic report with no available abstract, so title/metadata alone
    were inspected. Host antiangiogenesis/toxicity and microsporidial treatment do
    not demonstrate bacterial treatment. Additional original depths are recorded separately.
  snapshot_sha256: 6981bf281e341134762cfe573aae3d02aa6c5e4ac2b7ed1b604d8e4389cf06d4
- evidence_id: biosynthesis
  kind: primary_source
  reference: PMID:23488861; DOI:10.1021/ja312503y; PMC3652892
  locator: Complete original main text through the conclusion, retrieved as NCBI EFetch
    XML after Europe PMC500/PMCchallenge
  accessed_at: '2026-10-21T16:58:19Z'
  support: supports
  summary: The fma cluster was identified using the Af293 genome. Functional deletion
    experiments were performed in A.fumigatus CEA17 akuBKU80; loss and feeding restoration
    of fumagillin link PKS and terpene-cyclase functions. Heterologous yeast expression
    and enzyme assays resolve pathway intermediates. Those biosynthetic proteins are
    not antibacterial targets. Af293 genome assignment and CEA17 experiments must
    not be collapsed into an Af293 knockout experiment. The work is positive species/pathway
    evidence, with its exact strain scope retained.
  snapshot_sha256: f0077d1a389310f12e3dea640390f34ffe043d2c3581d7780524e0b12f9153b5
- evidence_id: af293
  kind: primary_source
  reference: PMID:27830189; DOI:10.1128/mSphere.00227-16; PMC5082629
  locator: Original secondary-metabolite Results, Figure4 caption, extraction/analysis
    Methods and complete abstract
  accessed_at: '2026-10-21T16:58:19Z'
  support: supports
  summary: The original2016 comparison includes Af293, CEA10 and two ISS isolates.
    HPLC-DAD-MS after five days on GMM agar at30C identifies fumagillin in Af293 and
    other strains. This independently supports the exact named native producer at
    metabolite-profile level; it does not assign every2013 knockout/heterologous method
    specifically to Af293. No natural-product absolute stereochemical re-determination
    is claimed from this profiling study.
  snapshot_sha256: 147b129e575911ce674218106d80e5f7c124b1ffc9952017335c1ae4c2c874fe
- evidence_id: bee
  kind: primary_source
  reference: PMID:23505365; DOI:10.1371/journal.ppat.1003185; PMC3591333
  locator: Complete original main Methods, Results and Discussion including Tables1–2
  accessed_at: '2026-10-21T16:58:19Z'
  support: supports
  summary: The material is explicitly bicyclohexylammonium fumagillin, abbreviated
    fumagillin by the authors. Controlled oral Nosema infections of honey bees are
    suppressed below the counting limit at25mg/L treatment; lower levels allow recovery
    and, for N.ceranae under some conditions, increased spore production. This supports
    the native historical bee-use statement without transferring formulation concentrations
    to a free-acid MIC. MetAP2 sequence comparisons and bee midgut proteomics are
    not direct binding measurements in Nosema, nor bacterial resistance evidence.
    The source does not support universal resistance-free efficacy.
  snapshot_sha256: c694203f4e7f9b8b0e4d06faaec1ed92aaa94d02bcd507fc096fb4a902ccdbab
- evidence_id: human
  kind: primary_source
  reference: PMID:12075057; DOI:10.1056/NEJMoa012924
  locator: Complete original randomized-trial abstract; main paper inaccessible via403
  accessed_at: '2026-10-21T16:58:19Z'
  support: supports
  summary: The2002 trial studies12 immunocompromised patients with E.bieneusi intestinal
    microsporidiosis. It reports microsporidial clearance with fumagillin versus placebo,
    along with serious blood-cell adverse effects in some treated patients. It supports
    an antimicrosporidial treatment context, not treatment of bacterial infection.
    No current prescribing recommendation, approval status or universal safety claim
    is inferred.
  snapshot_sha256: 605a38e2cbc00e8333678cf8b2ca496db52d5424292a17786d2d24ac4db14576
- evidence_id: recent-bacterial
  kind: primary_source
  reference: DOI:10.1016/j.microb.2026.100791; https://www.sciencedirect.com/science/article/pii/S2950194626001378
  locator: Complete original publisher abstract exposed by search; direct main-text
    retrieval403
  accessed_at: '2026-10-21T16:58:19Z'
  support: partial
  summary: The2026 original reports purification and FTIR/LC-ESI-MS/NMR identification
    of fumagillin from A.fumigatus MBL_F107, with antibacterial experiments including
    MRSA and antifungal activity. Its reporter and imaging observations concern protein-synthesis
    response and cellular deformation. This is positive exact-named antibacterial
    evidence at abstract depth; no exact MIC, full material characterization, direct
    binding mechanism or treatment use is reconstructed. MBL_F107 is not Af293.
- evidence_id: patent
  kind: primary_source
  reference: patent:US2652356
  locator: Original patent descriptive paragraphs on identification, producer and
    activity
  accessed_at: '2026-10-21T16:58:19Z'
  support: context_only
  summary: The patent concerns fumagillin preparation from A.fumigatus H-3 and reports
    anti-S.aureus-bacteriophage and E.histolytica activity. Inhibition of a phage
    must not be read as killing its bacterial host. The historical approximate formula
    is not substituted for the modern validated molecular structure. This is a topical
    document association rather than exact chemical equivalence.
  snapshot_sha256: 2e43c751590056b5ff73abf61023098750806f42e80431ccbefa9d505f3c0629
- evidence_id: search
  kind: search
  reference: 478-local-hits.txt;478-owners-search.json;048-root-fetch1-manifest.json
    through048-root-fetch7-manifest.json
  locator: Ignored-inclusive owner search, all adopted citations, bounded primary
    producer and antibacterial-use follow-up
  accessed_at: '2026-10-21T16:58:19Z'
  support: context_only
  summary: Public searches recovered original microsporidial treatment, biosynthesis,
    Af293 profiling and the2026 antibacterial abstract. No primary bacterial-treatment
    indication was established in the inspected trail, but this is not a proof of
    global non-use or inactivity. Direct current MIBiG JSON attempts returned404,
    while the exact versioned adopted row remained available. Proprietary Reaxys structure
    was not independently accessed. KNApSAcK and LIPIDMAPS structures were checked
    directly. DrugBank/DrugCentral remain broader drug-context associations.
  search_scope: 2026-10-21; rg --no-ignore --hidden exact label, CHEBI48635 and NGGMYCMLYOUNGM
    through maintained sources/curation/scripts/reports; Europe PMC TITLE_ABS:fumagillin
    first100 results plus adoptedPMIDs; web exact fumagillin antibacterial drug/bacterial
    infections clinical treatment, Af293 production and sourceDOIs.
  snapshot_sha256: ebe068056510f434b58fd316b533524d31ae6a8e51f011146f7e19993e76b8ba
- evidence_id: adapter
  kind: database
  reference: 475-imodulon-datasets.json
  locator: Earlier actual same-session adapter catalog, independently read for fungal
    coverage
  accessed_at: '2026-10-21T16:58:19Z'
  support: context_only
  summary: The actual catalog lists covered bacteria and an archaeon but no Aspergillus,
    Nosema or bee dataset. No matching iModulonDB dataset is applicable to the native
    fungal producer assertion. This catalog reuse is stated explicitly; no new gene
    or component query is claimed, and lack of coverage is not negative biological
    evidence.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: gates
  kind: validation
  reference: 478-focused-results.json;478-chemistry.json;048-root-authority-chemistry.json
  locator: Actual focused schema/strict/internal chemistry and independent external
    graph checks
  accessed_at: '2026-10-21T16:58:19Z'
  support: supports
  summary: All focused executions exit0. Sixteen captured inputs remain unchanged.
    Internal chemistry and source reproducibility do not validate the narrower antibacterial-drug
    use claim.
  snapshot_sha256: a09fd297c81ac887303f38496d3fc5cc54e7cc5e2eeebff8603b0b94c3cc2b89
assessments:
- assessment_id: chemical
  area: identity
  topic: Exact configured meroterpenoid and names
  outcome: supported
  summary: Independent structures, masses, six centres and E-chain geometry agree.
    Brands/INNs and exact/common names are appropriately separated; KNApSAcK displayed-key
    inconsistency does not contradict its two matching structure strings.
  target_ids:
  - CHEBI:48635
  evidence_ids:
  - native
  - identity
  - terms
- assessment_id: producer
  area: evidence
  topic: Species, strain and biosynthetic provenance
  outcome: supported
  summary: Native is an explicitly qualified MIBiG association. The2013 original supports
    the species/pathway while distinguishing Af293 genomic reference from CEA17 experiments;
    the2016 profile independently supports Af293 production. The source method annotations
    must retain those limits.
  target_ids:
  - CHEBI:48635
  evidence_ids:
  - owners
  - biosynthesis
  - af293
- assessment_id: microsporidia
  area: evidence
  topic: Bee-use definition and antifungal/antiprotozoal scope
  outcome: supported
  summary: Original bee and human studies support the microsporidial use context.
    Tested salt formulation and named organisms are preserved; no universal efficacy,
    current approval or host-selective mechanism is inferred.
  target_ids:
  - CHEBI:48635
  evidence_ids:
  - bee
  - human
  - terms
- assessment_id: antibacterial
  area: evidence
  topic: Antibacterial activity versus antibacterial drug use
  outcome: concern
  summary: The2026 original abstract supports activity in bacterial experiments. The
    inspected treatment evidence concerns microsporidia, while CHEBI36047 requires
    bacterial infection treatment/prevention. The inherited narrower role remains
    unverified and needs claim-specific adjudication.
  target_ids:
  - CHEBI:48635
  evidence_ids:
  - terms
  - adopted
  - recent-bacterial
  - human
  - search
  - patent
- assessment_id: scope
  area: completeness
  topic: Mechanism, resistance and optional annotations
  outcome: supported
  summary: No native named target or quantitative activity is asserted. Human MetAP2,
    fungal biosynthesis enzymes, reporter responses, phage inhibition and Nosema dose
    responses are distinct evidence types. Their absence as new target/causal objects
    is not a defect.
  target_ids:
  - CHEBI:48635
  evidence_ids:
  - native
  - biosynthesis
  - bee
  - recent-bacterial
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Maintained source/history and link semantics
  outcome: supported
  summary: All adopted/native citations, source concepts and seven histories were
    assessed at stated access depths. Native quality and citation-attachment limits
    are visible; exact chemistry agrees and broader drug/document links are kept separate.
  target_ids:
  - CHEBI:48635
  evidence_ids:
  - owners
  - adopted
  - identity
  - gates
findings:
- finding_id: F1
  issue_key: fumagillin-antibacterial-drug-use-role-unresolved
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: Adjudicate the inherited antibacterial-drug role separately from in-vitro
    activity
  description: CHEBI36047 asserts use to treat or prevent bacterial infections. The
    inspected primary treatment evidence concerns Nosema or E.bieneusi, while the2026
    bacterial experiment supports activity and proposed drug development. The record/current
    ChEBI do not provide claim-specific evidence for the narrower bacterial-use role.
    This is an unresolved support gap, not a confirmed statement that no such use
    exists or that fumagillin lacks antibacterial activity.
  target_ids:
  - CHEBI:48635
  field_paths:
  - activity_roles
  evidence_ids:
  - terms
  - adopted
  - bee
  - human
  - recent-bacterial
  - search
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Inherited activity-role owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Claim-specific maintained role adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible activity-role emission
  rule_id: Claim-level evidence and role scope
  native_severity: major provisional
  normalization_reason: If unsupported, a drug-use assertion materially exceeds laboratory
    activity. Certainty remains provisional because a bounded search cannot rule out
    every historical bacterial-treatment indication.
actions:
- action_id: A1
  description: Resolve the bacterial treatment/prevention evidence for CHEBI36047
    before scientific sign-off.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:48635
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Inherited activity-role owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Claim-specific maintained role adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible activity-role emission
  acceptance_checks:
  - Inspect a primary source or authoritative exact indication establishing treatment/prevention
    of bacterial infection, with organism, material and use context, or remove/qualify
    this specific inherited role through maintained ownership.
  - Retain independently supported antibacterial activity and microsporidial treatment
    context; do not equate bacteriophage inhibition, host angiogenesis effects or
    fungal biosynthesis with bacterial treatment.
  - Preserve provenance and source quality; regenerate role changes reproducibly and
    run focused schema/strict, reference, corpus and QC checks. Do not alter the valid
    structure to resolve an evidence-scope issue.
limitations:
- The2026 primary bacterial study was accessible only as its complete publisher abstract;
  direct main text returned403 and the exact DOI Europe PMC query returned no indexed
  result. No quantitative MIC or detailed assay condition is extracted.
- The1951 adopted paper has no available abstract; its metadata/title are not full-text
  evidence. The2002 clinical original was read at abstract level; adopted host-toxicity
  and review papers were likewise assessed at abstract depth.
- The2013 biosynthesis main text and2013 bee main text were read in full. The2016
  Af293 study was read at selected metabolite Results/Methods and abstract depth;
  raw chromatograms/genomics and supplemental spectra were not reprocessed.
- The MIBiG association is supported by its frozen exact row and independently inspected
  papers; current direct JSON routes were unavailable. The reference attachment does
  not convert CEA17 knockout methods into Af293-specific experiments.
- KNApSAcK displays an inconsistent historical key, while its SMILES and InChI parse
  to the native structure. Reaxys remains source-attributed; broader drug links are
  not treated as independent exact-structure evidence.
- A bounded search failed to establish bacterial treatment/prevention use. The provisional
  finding is not a universal negative and does not deny the positive2026 antibacterial
  report.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
