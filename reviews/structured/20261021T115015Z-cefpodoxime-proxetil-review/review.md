# Review of cefpodoxime proxetil

- Review: 20261021T115015Z-cefpodoxime-proxetil-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:39:21Z
- Finished UTC: 2026-10-21T11:50:15Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Cefpodoxime proxetil identity, configured 6R/7R core and Z oxime, prodrug relationship and all 24 FDA product assertions are supported. The native carboxylic-acid parent is chemically incorrect for the intact ester and requires an owner-level correction. GSRS explicitly identifies epimeric material, and original synthesis reports ester-center diastereomers; an unspecified center alone is not used to infer a mixture or ratio. A current OLS SMILES discrepancy is separate from the correct native geometry. No native record was changed.

## Scope And Provenance

Entire exact SEEDED cefpodoxime proxetil record, all four synonyms, three parents, two roles, chemical/drug/document identifiers, 24 FDA assertions across 12 applications and six history events, with original synthesis and conversion research.

Selection: Queue 244. Initial 13 inputs retained; actual FDA inventory and extractor appended before detailed judgment, giving 15 captured inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3505 | data/antibiotics/antibacterial/cefpodoxime-proxetil.yaml | generated | cefpodoxime proxetil |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema check | passed | True | CHEBI:3505 | Exit 0. |
| Documented strict check | passed | True | CHEBI:3505 | Exit 0; zero ERROR rows. |
| Initial cross-authority identity comparison | failed | False | CHEBI:3505 | Exit 1 at current_chebi: the current OLS SMILES lacks oxime geometry while its stored InChI/key retain it. Native chemistry is not the cause. |
| Bounded chemistry diagnosis | passed | False | CHEBI:3505 | Exit 0: native, GSRS, PubChem and both KEGG graphs agree; the separate current OLS discrepancy and lack of a free carboxylic acid are explicitly tested. |
| All FDA application/product comparisons | passed | False | CHEBI:3505 | Exit 0; all 24 rows across 12 applications agree in the compared fields. |
| Structured source applicability | not_applicable | False | CHEBI:3505 | No native gene, protein, named pathway or expression assertion triggers an adapter. Prodrug conversion research does not establish a new native enzyme target. |
| Authoritative full QC | failed | True | CHEBI:3505 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3505 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3505 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3505 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3505 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3505 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3505 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3505 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3505 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact ester and stereochemistry

identity: supported. Targets: CHEBI:3505.

Native identity agrees with independent authorities and original synthesis. EPIMERIC material is explicitly sourced, without an inferred ratio.

### Structural parent membership

grounding: concern. Targets: CHEBI:3505.

CHEBI:33575 is not a valid class for the intact ester because no free carboxylic acid is present.

### Conversion and antibacterial scope

evidence: supported. Targets: CHEBI:3505.

Original experiments and the label support the prodrug relationship; active-acid assays remain distinct from intact-ester activity.

### All clinical assertions

provenance: supported. Targets: CHEBI:3505.

All 24 FDA rows and the exact GSRS join were checked and agree.

### Chemical versus contextual references

grounding: unknown. Targets: CHEBI:3505.

Accessible chemical mappings agree; independent DrugBank/Beilstein inspection is limited. Both patent documents resolve at their actual kind codes and series scope.

### Current source SMILES geometry

consistency: unknown. Targets: CHEBI:3505.

Current OLS SMILES loses oxime geometry despite its retained Z InChI/key; native and independent sources preserve Z. The source discrepancy must not be copied into the native graph.

### Owners and source history

provenance: supported. Targets: CHEBI:3505.

Actual source owners and six history events are preserved; no adopted PMID lead is omitted.

### Optional targets and activity observations

completeness: supported. Targets: CHEBI:3505.

Empty direct-target and MIC slots are not demonstrated defects for a prodrug; primary enrichment must retain conversion and tested-material scope.

### Focused validity

schema: supported. Targets: CHEBI:3505.

Schema and strict pass; supplemental source disagreement is separately documented.

## Findings

### F1: The intact proxetil ester is incorrectly classified as a carboxylic acid

major / open / confirmed; issue key: CHEBI-3505-carboxylic-acid-parent.

parent_compounds includes CHEBI:33575, which requires a free C(=O)OH group. Cefpodoxime proxetil esterifies that carboxyl and contains no other free carboxylic acid, as shown by the native graph, independent authority graphs and original 2a synthesis. The current ChEBI parent edge reproduces the error; source provenance does not make the chemical subsumption correct. This finding does not challenge the prodrug identity, epimeric material or the separately represented free acid.

## Recommended Actions And Acceptance Checks

### A1

Remove only the CHEBI:3505 -&gt; CHEBI:33575 structural parent through an upstream source correction and re-adoption, or an audited compound-specific exclusion implemented in scripts/extract_source_inventory.py. Regenerate data/raw/chebi_antimicrobials.tsv and reseed. Retain CHEBI:33308 and CHEBI:23066, the exact ester graph, RS material naming and all supported FDA assertions. Do not globally remove carboxylic-acid parents or hand-edit the generated YAML.

- Inspect the exact CHEBI:3505 inventory parent_ids and generated parent_compounds: CHEBI:33575 is absent, while the two valid parents remain.
- Confirm the native full key, Z oxime, two configured core centers, unspecified ester center and 24 FDA assertion rows remain unchanged.
- Run just validate and just validate-strict for data/antibiotics/antibacterial/cefpodoxime-proxetil.yaml, then documented just verify-corpus --summary, just review-queue --limit 0 and just qc after the authorized curation change.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cefpodoxime-proxetil.yaml; Entire native YAML, four synonyms, all 24 clinical assertions and six history events | supports | The record describes the proxetil ester, retains an RS ester-center alias and fixed 6R/7R/Z chemistry, and carries three structural parents. No direct target, MIC, resistant taxon, producer or causal graph is asserted. The six history events are source seeding events. |
| chemistry | CHEBI:3505; PubChem:6526396; KEGG:C08115; KEGG:D00920; UNII:2TB00A1Z7N; 244-chemistry.py, 244-chemistry-diagnostic.py and 244-chemistry.json; authority snapshots | supports | Native SMILES/InChI, GSRS, PubChem and both KEGG molfiles yield LTINZAODLRIQIX-FBXRGJNPSA-N, C21H27N5O9S2, charge 0, average mass 557.607 and exact mass 557.125019444, with two R core centers, one unspecified ester center and Z oxime. Current OLS SMILES omits oxime geometry and yields OBEQYXGQ although its stored InChI/key retain FBXRGJNP. The initial all-authority assertion failed for that source-only discrepancy; the diagnostic preserves it explicitly. Every graph has zero free-carboxylic-acid matches. |
| parent-error | CHEBI:33575; CHEBI:3505; CHEBI:33308; CHEBI:23066; 244-parent-33575.json; 244-parents.json; 244-parent-33308.json; original compound 2a structure | refutes | CHEBI:33575 defines carboxylic acids by a free C(=O)OH group. The intact proxetil graph esterifies that carboxyl and has no other free carboxylic acid. The adopted ChEBI row and current direct parents nevertheless include this class. The carboxylic ester and cephalosporin parents remain appropriate. Hydrolysis to cefpodoxime does not make the starting ester an instance of carboxylic acid. |
| stereo | UNII:2TB00A1Z7N; FDA GSRS version 38; 244-gsrs.json, structure and moiety stereochemistry; 244-label.json description | supports | GSRS explicitly marks the substance EPIMERIC, with three stereocenters and two defined; its graph agrees with the native key. The official product label uses the RS ester-center name while fixing the 6R/7R core and Z oxime. This material definition supports the native naming boundary independently of the mere lack of an ester-center stereotag. No exact mixture ratio is inferred. |
| synthesis | PMID:3570989; DOI:10.7164/antibiotics.40.370; 244-primary1987.pdf/.txt; printed pp.370-378 and p.380, Figure 2, Tables 1-4 and exact 2a preparation; pp.371/378 images inspected | supports | Fujimoto and colleagues identify compound 2a/CS-807 as the proxetil ester of acid 1. The exact 2a preparation reports a pair of diastereomers from the ester center and analytical formula C21H27N5O9S2. The paper reports hydrolysis in rat intestinal homogenate/serum and appearance of acid 1 in portal blood after ester dosing. Its Table 1 antibacterial measurements belong to the parental acids, whereas ester oral dosing is assessed by recovery of active material. Those assays do not establish direct intact-ester PBP binding. |
| conversion | PMID:9756762; DOI:10.1128/AAC.42.10.2602; 244-primary1998.html/.txt, full Methods, cefpodoxime Results and Discussion | supports | The study used Roche cefpodoxime proxetil Ro43-1826/000 and separately identified sodium cefpodoxime reference material. Human duodenal fluid collected from four volunteers was studied in vitro at pH7.4 and 37C with HPLC/NMR product analysis. The two ester diastereomers had different hydrolysis rates, and active delta3 cefpodoxime predominated over delta2 product in intestinal juice. This supports conversion and distinguishes luminal from epithelial processes; it does not measure intact-prodrug target binding or prove a new clinical dosing claim. |
| conversion-abstract | PMID:10477812; DOI:10.1016/S0378-5173(97)00227-5; 244-primary-core.json, complete abstract | context_only | Human duodenal washings showed cefpodoxime-proxetil hydrolysis in vitro. Inhibitor experiments suggested a cholinesterase contribution, which remains a hypothesis at this access depth. No specific enzyme or gene is added to the native record. Rabbit food-component experiments and comparisons with human exposure are not conflated with direct epithelial enzyme identification. |
| clinical | FDA applications 050674, 050675, 050687, 050688, 065082, 065083, 065370, 065388, 065409, 065462, 090031, 210568; UNII:2TB00A1Z7N; 244-fda-check.py/.json; all twelve 244-fda-*.json API records and matching official overview documents; 244-gsrs.json | supports | All 24 native assertion rows agree with current official API application/product numbers, sponsors, drug/ingredient names, earliest approved original date and marketing status. GSRS version 38 supplies the exact epimeric substance join. Historical approval is kept distinct from discontinued or prescription marketing. Ten rows are prescription products and fourteen discontinued; no discontinuation reason is inferred. |
| label | FDA label set 1b405104-650b-c8e3-e063-6294a90a9e8a; ANDA210568; 244-label.json, effective date 20240619, Description, Clinical Pharmacology and Indications | supports | The official label confirms oral proxetil administration and de-esterification to active cefpodoxime. The three conditions named in the native definition occur in its indication list, limited to susceptible organisms and the specified disease/patient contexts. Label doses and antibacterial microbiology are expressed as active cefpodoxime, so those values are not direct intact-ester assays. |
| identifiers | CHEBI:3505; cas:87239-81-4; kegg.compound:C08115; kegg.drug:D00920; drugcentral:555; drugbank:DB01416; beilstein:8174918; 244-ols.json; 244-kegg-compound.txt; 244-kegg-drug.txt; 244-drugcentral.html; fetch manifest | partial | The chemical authorities and DrugCentral corroborate the proxetil name and CAS. KEGG compound identity is independently graph-matched. DrugCentral spans parent and prodrug context, appropriately placed under drug_xrefs. DrugBank returned HTTP403; Beilstein was corroborated only as the current ChEBI mapping, without independent registry access. No drug-context identifier is promoted to exact acid equivalence. |
| patents | patent:EP49118; patent:US4486425; 244-patent-ep-a2.html and 244-patent-us.html, descriptions and claims | supports | EP0049118A2 and US4486425 describe the corresponding orally administered cephalosporin ester series, including carbonate variants and conversion to parent acids. These resolve as related contextual documents, not exact chemical identifiers. The guessed EP A1 endpoint returned 404, whereas the actual A2 publication resolved; no broken native accession is inferred from the wrong kind-code attempt. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; data/raw/fda_clinical_status.tsv; scripts/extract_fda_clinical_status.py; 244 owner captures and local search; extraction is_a loop and parent_ids construction; seeder parent union | supports | The ChEBI row owns the erroneous parent. The extractor copies allowed is_a edges into parent_ids, and the seeder unions them into parent_compounds. No existing targeted parent-exclusion configuration or exact curator override was found in the bounded ignored-inclusive search; one must not invent a currently supported override key. The FDA inventory/extractor own the 24 clinical joins. The adopted ChEBI row has no PMID leads. |
| validation | Focused schema and strict validators; 244-strict.tsv | supports | Schema and strict validators exited 0 with no ERROR rows. A valid term identifier does not prove that its structural parent relationship is correct. Required shared gates are separate. |

## Limits And Additional Notes

- The native ester stereocenter is unspecified, which alone does not establish a mixture or its ratio. Here the native RS name, GSRS EPIMERIC designation and original synthesized 2a pair of diastereomers independently establish the material boundary. No exact ratio or single-isomer efficacy is claimed.
- Current OLS SMILES omits the oxime directional marker although its InChI/key retain Z. The initial supplemental comparison exited 1 for that discrepancy. A separate diagnostic exited 0 and confirmed native, GSRS, PubChem and KEGG agreement; the source disagreement is preserved rather than treated as a native structure defect.
- The 1987 paper was read in the compound-specific chemistry, biological results, exact 2a preparation and relevant tables, with Figure 2 and p.378 visually checked. Other analogue syntheses were not exhaustively reviewed. The 1998 paper was read in full methods, cefpodoxime results and discussion; its donor-fluid experiments are in vitro, not direct measurements of human epithelial metabolism. PMID10477812 was inspected at complete abstract depth.
- Original parent-acid MIC measurements, sodium-cefpodoxime reference material and label microbiology must not be reassigned to the intact proxetil ester. The label supports the listed indications only at its susceptible-organism and patient-context scope; no clinical advice or new dose claim is made.
- DrugBank returned 403 and Beilstein had no independently inspected public registry record. CAS is corroborated through chemical authorities. The guessed EP A1 publication returned 404; the actual A2 publication was retrieved and inspected. Europe PMC fullTextXML returned 500, but the complete PMC HTML article was available and read.
- All 24 FDA assertion rows were compared with current official API data and the corresponding public overview pages were retrieved. This checks recorded regulatory facts and exact GSRS identity, not present pharmacy availability, prescribing suitability or reasons for discontinuation.
- Focused schema/strict checks pass despite the erroneous parent relationship. Supplemental chemistry used the existing 019 environment against 025; required shared corpus gates are separate. No native scientific status was promoted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 15 captured repository input hashes remain unchanged: 13 initial plus the two actual FDA owners. No native record, saved bundle or Git state was modified.
- Source timestamps and hashes are retained in 244-fetch-results.json and 244-fetch2-results.json. The sole adopted ChEBI row contains zero PMID leads; all publications cited here are additional research.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T115015Z-cefpodoxime-proxetil-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of cefpodoxime proxetil
started_at: '2026-10-21T11:39:21Z'
finished_at: '2026-10-21T11:50:15Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: 'Needs curation: one major erroneous structural parent'
scientific_review: true
summary: Cefpodoxime proxetil identity, configured 6R/7R core and Z oxime, prodrug
  relationship and all 24 FDA product assertions are supported. The native carboxylic-acid
  parent is chemically incorrect for the intact ester and requires an owner-level
  correction. GSRS explicitly identifies epimeric material, and original synthesis
  reports ester-center diastereomers; an unspecified center alone is not used to infer
  a mixture or ratio. A current OLS SMILES discrepancy is separate from the correct
  native geometry. No native record was changed.
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
  - path: data/antibiotics/antibacterial/cefpodoxime-proxetil.yaml
    sha256: 2f72300339c7a0cd8f8873823821017306c0413f23aee41ebab72972fa063670
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
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
    role: context
  - path: scripts/extract_fda_clinical_status.py
    sha256: f30f385ea6d530dc1749e3d805dbcdbc8715fbc476abc510bf144ea13964e171
    role: context
scope:
  description: Entire exact SEEDED cefpodoxime proxetil record, all four synonyms,
    three parents, two roles, chemical/drug/document identifiers, 24 FDA assertions
    across 12 applications and six history events, with original synthesis and conversion
    research.
  selection: Queue 244. Initial 13 inputs retained; actual FDA inventory and extractor
    appended before detailed judgment, giving 15 captured inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3505
targets:
- target_id: CHEBI:3505
  path: data/antibiotics/antibacterial/cefpodoxime-proxetil.yaml
  label: cefpodoxime proxetil
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
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Adopted regulatory assertions with exact GSRS structure join
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Clinical source extraction and identity join
checks:
- check_id: schema
  name: Documented schema check
  status: passed
  required: true
  summary: Exit 0.
  target_ids:
  - CHEBI:3505
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefpodoxime-proxetil.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict check
  status: passed
  required: true
  summary: Exit 0; zero ERROR rows.
  target_ids:
  - CHEBI:3505
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefpodoxime-proxetil.yaml --out /private/tmp/am-review-session/244-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry-initial
  name: Initial cross-authority identity comparison
  status: failed
  required: false
  summary: 'Exit 1 at current_chebi: the current OLS SMILES lacks oxime geometry while
    its stored InChI/key retain it. Native chemistry is not the cause.'
  target_ids:
  - CHEBI:3505
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/244-chemistry.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: chemistry-diagnostic
  name: Bounded chemistry diagnosis
  status: passed
  required: false
  summary: 'Exit 0: native, GSRS, PubChem and both KEGG graphs agree; the separate
    current OLS discrepancy and lack of a free carboxylic acid are explicitly tested.'
  target_ids:
  - CHEBI:3505
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/244-chemistry-diagnostic.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: fda
  name: All FDA application/product comparisons
  status: passed
  required: false
  summary: Exit 0; all 24 rows across 12 applications agree in the compared fields.
  target_ids:
  - CHEBI:3505
  command: .venv/bin/python /private/tmp/am-review-session/244-fda-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - clinical
- check_id: structured-adapter
  name: Structured source applicability
  status: not_applicable
  required: false
  summary: No native gene, protein, named pathway or expression assertion triggers
    an adapter. Prodrug conversion research does not establish a new native enzyme
    target.
  target_ids:
  - CHEBI:3505
  evidence_ids:
  - record
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:3505
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
  - CHEBI:3505
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
  - CHEBI:3505
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
  - CHEBI:3505
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
  - CHEBI:3505
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
  - CHEBI:3505
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
  - CHEBI:3505
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
  - CHEBI:3505
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
  - CHEBI:3505
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cefpodoxime-proxetil.yaml
  locator: Entire native YAML, four synonyms, all 24 clinical assertions and six history
    events
  accessed_at: '2026-10-21T11:44:12Z'
  support: supports
  summary: The record describes the proxetil ester, retains an RS ester-center alias
    and fixed 6R/7R/Z chemistry, and carries three structural parents. No direct target,
    MIC, resistant taxon, producer or causal graph is asserted. The six history events
    are source seeding events.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:3505; PubChem:6526396; KEGG:C08115; KEGG:D00920; UNII:2TB00A1Z7N
  locator: 244-chemistry.py, 244-chemistry-diagnostic.py and 244-chemistry.json; authority
    snapshots
  accessed_at: '2026-10-21T11:44:12Z'
  support: supports
  summary: Native SMILES/InChI, GSRS, PubChem and both KEGG molfiles yield LTINZAODLRIQIX-FBXRGJNPSA-N,
    C21H27N5O9S2, charge 0, average mass 557.607 and exact mass 557.125019444, with
    two R core centers, one unspecified ester center and Z oxime. Current OLS SMILES
    omits oxime geometry and yields OBEQYXGQ although its stored InChI/key retain
    FBXRGJNP. The initial all-authority assertion failed for that source-only discrepancy;
    the diagnostic preserves it explicitly. Every graph has zero free-carboxylic-acid
    matches.
  snapshot_sha256: fe6b5c73ae7ecd54293862833aa3cfc3421eebe227828752358720a8f1f2fe70
- evidence_id: parent-error
  kind: authority
  reference: CHEBI:33575; CHEBI:3505; CHEBI:33308; CHEBI:23066
  locator: 244-parent-33575.json; 244-parents.json; 244-parent-33308.json; original
    compound 2a structure
  accessed_at: '2026-10-21T11:44:12Z'
  support: refutes
  summary: CHEBI:33575 defines carboxylic acids by a free C(=O)OH group. The intact
    proxetil graph esterifies that carboxyl and has no other free carboxylic acid.
    The adopted ChEBI row and current direct parents nevertheless include this class.
    The carboxylic ester and cephalosporin parents remain appropriate. Hydrolysis
    to cefpodoxime does not make the starting ester an instance of carboxylic acid.
  snapshot_sha256: f63afc769c641224bdf70e4be96796c403d035cc44d7685193c146585ce5bd06
- evidence_id: stereo
  kind: authority
  reference: UNII:2TB00A1Z7N; FDA GSRS version 38
  locator: 244-gsrs.json, structure and moiety stereochemistry; 244-label.json description
  accessed_at: '2026-10-21T11:44:12Z'
  support: supports
  summary: GSRS explicitly marks the substance EPIMERIC, with three stereocenters
    and two defined; its graph agrees with the native key. The official product label
    uses the RS ester-center name while fixing the 6R/7R core and Z oxime. This material
    definition supports the native naming boundary independently of the mere lack
    of an ester-center stereotag. No exact mixture ratio is inferred.
  snapshot_sha256: 34825b58dd2af1591e682a405b5d41069b07c80df9ec6b262532cb50b48daa60
- evidence_id: synthesis
  kind: primary_source
  reference: PMID:3570989; DOI:10.7164/antibiotics.40.370
  locator: 244-primary1987.pdf/.txt; printed pp.370-378 and p.380, Figure 2, Tables
    1-4 and exact 2a preparation; pp.371/378 images inspected
  accessed_at: '2026-10-21T11:44:12Z'
  support: supports
  summary: Fujimoto and colleagues identify compound 2a/CS-807 as the proxetil ester
    of acid 1. The exact 2a preparation reports a pair of diastereomers from the ester
    center and analytical formula C21H27N5O9S2. The paper reports hydrolysis in rat
    intestinal homogenate/serum and appearance of acid 1 in portal blood after ester
    dosing. Its Table 1 antibacterial measurements belong to the parental acids, whereas
    ester oral dosing is assessed by recovery of active material. Those assays do
    not establish direct intact-ester PBP binding.
  snapshot_sha256: 6a9d14e5e0b2f98342c3ae433e5ba6f1f8240d35f41fcf2ee06691ce912a74a0
- evidence_id: conversion
  kind: primary_source
  reference: PMID:9756762; DOI:10.1128/AAC.42.10.2602
  locator: 244-primary1998.html/.txt, full Methods, cefpodoxime Results and Discussion
  accessed_at: '2026-10-21T11:44:12Z'
  support: supports
  summary: The study used Roche cefpodoxime proxetil Ro43-1826/000 and separately
    identified sodium cefpodoxime reference material. Human duodenal fluid collected
    from four volunteers was studied in vitro at pH7.4 and 37C with HPLC/NMR product
    analysis. The two ester diastereomers had different hydrolysis rates, and active
    delta3 cefpodoxime predominated over delta2 product in intestinal juice. This
    supports conversion and distinguishes luminal from epithelial processes; it does
    not measure intact-prodrug target binding or prove a new clinical dosing claim.
  snapshot_sha256: b8e0dfa67c026ee4d41d23741e5c7dcd8065c054996440e6d685156e369a8dca
- evidence_id: conversion-abstract
  kind: primary_source
  reference: PMID:10477812; DOI:10.1016/S0378-5173(97)00227-5
  locator: 244-primary-core.json, complete abstract
  accessed_at: '2026-10-21T11:44:12Z'
  support: context_only
  summary: Human duodenal washings showed cefpodoxime-proxetil hydrolysis in vitro.
    Inhibitor experiments suggested a cholinesterase contribution, which remains a
    hypothesis at this access depth. No specific enzyme or gene is added to the native
    record. Rabbit food-component experiments and comparisons with human exposure
    are not conflated with direct epithelial enzyme identification.
  snapshot_sha256: 9996fbc6e23dc605a1675f94780f9ba8e52299443116eab25ad35aa4736b9f52
- evidence_id: clinical
  kind: authority
  reference: FDA applications 050674, 050675, 050687, 050688, 065082, 065083, 065370,
    065388, 065409, 065462, 090031, 210568; UNII:2TB00A1Z7N
  locator: 244-fda-check.py/.json; all twelve 244-fda-*.json API records and matching
    official overview documents; 244-gsrs.json
  accessed_at: '2026-10-21T11:44:12Z'
  support: supports
  summary: All 24 native assertion rows agree with current official API application/product
    numbers, sponsors, drug/ingredient names, earliest approved original date and
    marketing status. GSRS version 38 supplies the exact epimeric substance join.
    Historical approval is kept distinct from discontinued or prescription marketing.
    Ten rows are prescription products and fourteen discontinued; no discontinuation
    reason is inferred.
  snapshot_sha256: e2df63441054bd4c4606a9d2c39d89a5f9edfbe4d01fd982b9dbdc309ff501cf
- evidence_id: label
  kind: authority
  reference: FDA label set 1b405104-650b-c8e3-e063-6294a90a9e8a; ANDA210568
  locator: 244-label.json, effective date 20240619, Description, Clinical Pharmacology
    and Indications
  accessed_at: '2026-10-21T11:44:12Z'
  support: supports
  summary: The official label confirms oral proxetil administration and de-esterification
    to active cefpodoxime. The three conditions named in the native definition occur
    in its indication list, limited to susceptible organisms and the specified disease/patient
    contexts. Label doses and antibacterial microbiology are expressed as active cefpodoxime,
    so those values are not direct intact-ester assays.
  snapshot_sha256: c79e2ddf1917dabf0708fdc70fd302a2f3786154bf62702ed6f64da5bed9a4f3
- evidence_id: identifiers
  kind: authority
  reference: CHEBI:3505; cas:87239-81-4; kegg.compound:C08115; kegg.drug:D00920; drugcentral:555;
    drugbank:DB01416; beilstein:8174918
  locator: 244-ols.json; 244-kegg-compound.txt; 244-kegg-drug.txt; 244-drugcentral.html;
    fetch manifest
  accessed_at: '2026-10-21T11:44:12Z'
  support: partial
  summary: The chemical authorities and DrugCentral corroborate the proxetil name
    and CAS. KEGG compound identity is independently graph-matched. DrugCentral spans
    parent and prodrug context, appropriately placed under drug_xrefs. DrugBank returned
    HTTP403; Beilstein was corroborated only as the current ChEBI mapping, without
    independent registry access. No drug-context identifier is promoted to exact acid
    equivalence.
  snapshot_sha256: d7b624a45702816f7ee7f9c499c9fe61bf1242ec4693a626ea254729cde38a8f
- evidence_id: patents
  kind: primary_source
  reference: patent:EP49118; patent:US4486425
  locator: 244-patent-ep-a2.html and 244-patent-us.html, descriptions and claims
  accessed_at: '2026-10-21T11:44:12Z'
  support: supports
  summary: EP0049118A2 and US4486425 describe the corresponding orally administered
    cephalosporin ester series, including carbonate variants and conversion to parent
    acids. These resolve as related contextual documents, not exact chemical identifiers.
    The guessed EP A1 endpoint returned 404, whereas the actual A2 publication resolved;
    no broken native accession is inferred from the wrong kind-code attempt.
  snapshot_sha256: 97efc88c18f470039e4c658f43c7308046f858f2738c494ede9b0a378d820867
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py; data/raw/fda_clinical_status.tsv; scripts/extract_fda_clinical_status.py
  locator: 244 owner captures and local search; extraction is_a loop and parent_ids
    construction; seeder parent union
  accessed_at: '2026-10-21T11:44:12Z'
  support: supports
  summary: The ChEBI row owns the erroneous parent. The extractor copies allowed is_a
    edges into parent_ids, and the seeder unions them into parent_compounds. No existing
    targeted parent-exclusion configuration or exact curator override was found in
    the bounded ignored-inclusive search; one must not invent a currently supported
    override key. The FDA inventory/extractor own the 24 clinical joins. The adopted
    ChEBI row has no PMID leads.
  snapshot_sha256: d89020fff645e3a6ad5f8b2339ee64e3246ede092dc25270dd96ed316643ee29
  search_scope: rg --no-ignore --hidden across curation, conf, data/raw, scripts and
    docs for CHEBI:3505, cefpodoxime.proxetil and LTINZAODLRIQIX; additional ignored-inclusive
    search of conf, curation, scripts and docs for parent-exclusion/override keys.
- evidence_id: validation
  kind: validation
  reference: Focused schema and strict validators
  locator: 244-strict.tsv
  accessed_at: '2026-10-21T11:44:12Z'
  support: supports
  summary: Schema and strict validators exited 0 with no ERROR rows. A valid term
    identifier does not prove that its structural parent relationship is correct.
    Required shared gates are separate.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact ester and stereochemistry
  outcome: supported
  summary: Native identity agrees with independent authorities and original synthesis.
    EPIMERIC material is explicitly sourced, without an inferred ratio.
  target_ids:
  - CHEBI:3505
  evidence_ids:
  - chemistry
  - stereo
  - synthesis
- assessment_id: parent
  area: grounding
  topic: Structural parent membership
  outcome: concern
  summary: CHEBI:33575 is not a valid class for the intact ester because no free carboxylic
    acid is present.
  target_ids:
  - CHEBI:3505
  evidence_ids:
  - parent-error
  - chemistry
- assessment_id: prodrug
  area: evidence
  topic: Conversion and antibacterial scope
  outcome: supported
  summary: Original experiments and the label support the prodrug relationship; active-acid
    assays remain distinct from intact-ester activity.
  target_ids:
  - CHEBI:3505
  evidence_ids:
  - synthesis
  - conversion
  - label
- assessment_id: clinical
  area: provenance
  topic: All clinical assertions
  outcome: supported
  summary: All 24 FDA rows and the exact GSRS join were checked and agree.
  target_ids:
  - CHEBI:3505
  evidence_ids:
  - clinical
  - stereo
- assessment_id: xref
  area: grounding
  topic: Chemical versus contextual references
  outcome: unknown
  summary: Accessible chemical mappings agree; independent DrugBank/Beilstein inspection
    is limited. Both patent documents resolve at their actual kind codes and series
    scope.
  target_ids:
  - CHEBI:3505
  evidence_ids:
  - identifiers
  - patents
- assessment_id: source-discrepancy
  area: consistency
  topic: Current source SMILES geometry
  outcome: unknown
  summary: Current OLS SMILES loses oxime geometry despite its retained Z InChI/key;
    native and independent sources preserve Z. The source discrepancy must not be
    copied into the native graph.
  target_ids:
  - CHEBI:3505
  evidence_ids:
  - chemistry
- assessment_id: provenance
  area: provenance
  topic: Owners and source history
  outcome: supported
  summary: Actual source owners and six history events are preserved; no adopted PMID
    lead is omitted.
  target_ids:
  - CHEBI:3505
  evidence_ids:
  - record
  - owners
- assessment_id: completeness
  area: completeness
  topic: Optional targets and activity observations
  outcome: supported
  summary: Empty direct-target and MIC slots are not demonstrated defects for a prodrug;
    primary enrichment must retain conversion and tested-material scope.
  target_ids:
  - CHEBI:3505
  evidence_ids:
  - record
  - synthesis
  - conversion
- assessment_id: schema
  area: schema
  topic: Focused validity
  outcome: supported
  summary: Schema and strict pass; supplemental source disagreement is separately
    documented.
  target_ids:
  - CHEBI:3505
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: CHEBI-3505-carboxylic-acid-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The intact proxetil ester is incorrectly classified as a carboxylic acid
  description: parent_compounds includes CHEBI:33575, which requires a free C(=O)OH
    group. Cefpodoxime proxetil esterifies that carboxyl and contains no other free
    carboxylic acid, as shown by the native graph, independent authority graphs and
    original 2a synthesis. The current ChEBI parent edge reproduces the error; source
    provenance does not make the chemical subsumption correct. This finding does not
    challenge the prodrug identity, epimeric material or the separately represented
    free acid.
  target_ids:
  - CHEBI:3505
  field_paths:
  - parent_compounds
  evidence_ids:
  - parent-error
  - chemistry
  - synthesis
  - owners
  rule_id: '.claude/skills/curate-yaml-record/references/review-checklist.md: Equivalence'
  native_severity: 'Major: wrong ontology grounding'
  normalization_reason: A valid class identifier is applied to a structure outside
    that class; this is a substantive grounding error, without a wrong-compound identity
    finding.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained adopted parent_ids for CHEBI:3505
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI is_a-to-parent_ids transform
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated parent_compounds union
  ownership_note: Correct the ChEBI source relationship or add an explicitly keyed,
    evidence-backed exclusion in the existing extraction path, then regenerate the
    maintained inventory and native record. There is no verified existing parent-override
    key.
actions:
- action_id: A1
  description: Remove only the CHEBI:3505 -> CHEBI:33575 structural parent through
    an upstream source correction and re-adoption, or an audited compound-specific
    exclusion implemented in scripts/extract_source_inventory.py. Regenerate data/raw/chebi_antimicrobials.tsv
    and reseed. Retain CHEBI:33308 and CHEBI:23066, the exact ester graph, RS material
    naming and all supported FDA assertions. Do not globally remove carboxylic-acid
    parents or hand-edit the generated YAML.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:3505
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained adopted parent_ids for CHEBI:3505
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI is_a-to-parent_ids transform
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated parent_compounds union
  ownership_note: The existing extractor directly copies ChEBI is_a edges and the
    seeder unions parents. A local exclusion would be a new, narrowly scoped implementation,
    not an already available configuration key.
  generator: just extract-inventory --offline; just seed; just seed-canary CHEBI:3505
  acceptance_checks:
  - 'Inspect the exact CHEBI:3505 inventory parent_ids and generated parent_compounds:
    CHEBI:33575 is absent, while the two valid parents remain.'
  - Confirm the native full key, Z oxime, two configured core centers, unspecified
    ester center and 24 FDA assertion rows remain unchanged.
  - Run just validate and just validate-strict for data/antibiotics/antibacterial/cefpodoxime-proxetil.yaml,
    then documented just verify-corpus --summary, just review-queue --limit 0 and
    just qc after the authorized curation change.
limitations:
- The native ester stereocenter is unspecified, which alone does not establish a mixture
  or its ratio. Here the native RS name, GSRS EPIMERIC designation and original synthesized
  2a pair of diastereomers independently establish the material boundary. No exact
  ratio or single-isomer efficacy is claimed.
- Current OLS SMILES omits the oxime directional marker although its InChI/key retain
  Z. The initial supplemental comparison exited 1 for that discrepancy. A separate
  diagnostic exited 0 and confirmed native, GSRS, PubChem and KEGG agreement; the
  source disagreement is preserved rather than treated as a native structure defect.
- The 1987 paper was read in the compound-specific chemistry, biological results,
  exact 2a preparation and relevant tables, with Figure 2 and p.378 visually checked.
  Other analogue syntheses were not exhaustively reviewed. The 1998 paper was read
  in full methods, cefpodoxime results and discussion; its donor-fluid experiments
  are in vitro, not direct measurements of human epithelial metabolism. PMID10477812
  was inspected at complete abstract depth.
- Original parent-acid MIC measurements, sodium-cefpodoxime reference material and
  label microbiology must not be reassigned to the intact proxetil ester. The label
  supports the listed indications only at its susceptible-organism and patient-context
  scope; no clinical advice or new dose claim is made.
- DrugBank returned 403 and Beilstein had no independently inspected public registry
  record. CAS is corroborated through chemical authorities. The guessed EP A1 publication
  returned 404; the actual A2 publication was retrieved and inspected. Europe PMC
  fullTextXML returned 500, but the complete PMC HTML article was available and read.
- All 24 FDA assertion rows were compared with current official API data and the corresponding
  public overview pages were retrieved. This checks recorded regulatory facts and
  exact GSRS identity, not present pharmacy availability, prescribing suitability
  or reasons for discontinuation.
- Focused schema/strict checks pass despite the erroneous parent relationship. Supplemental
  chemistry used the existing 019 environment against 025; required shared corpus
  gates are separate. No native scientific status was promoted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- 'All 15 captured repository input hashes remain unchanged: 13 initial plus the two
  actual FDA owners. No native record, saved bundle or Git state was modified.'
- Source timestamps and hashes are retained in 244-fetch-results.json and 244-fetch2-results.json.
  The sole adopted ChEBI row contains zero PMID leads; all publications cited here
  are additional research.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.7164/antibiotics.40.370
- https://doi.org/10.1128/AAC.42.10.2602
- https://doi.org/10.1016/S0378-5173(97)00227-5
- https://www.ebi.ac.uk/chebi/CHEBI:33575
- https://api.fda.gov/other/substance.json?search=unii:2TB00A1Z7N&limit=10
tags:
- record-review
- cefpodoxime-proxetil
- prodrug
- ontology-parent
- clinical-status
```
