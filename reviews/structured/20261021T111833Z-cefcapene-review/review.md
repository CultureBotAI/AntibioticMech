# Review of cefcapene

- Review: 20261021T111833Z-cefcapene-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:55:30Z
- Finished UTC: 2026-10-21T11:18:33Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The cefcapene free-acid graph, 6R/7R centers and Z side chain agree with current ChEBI, PubChem, ChEMBL and KEGG. The native definition distinguishes the active compound from its pivoxil ester prodrug. All six adopted or parent PMID records resolve at stated depth. Original abstracts support S-1006 antibacterial activity and PBP affinity, while a full case report concerns pivoxil hydrochloride and pivalate-associated carnitine loss. The class C beta-lactamase study describes transient enzyme inactivation. No native mechanism or assay is asserted, and no required correction was demonstrated. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact SEEDED cefcapene record, four history events, all synonyms, chemical identifiers, parent and role groundings, actual ChEBI/ARO owner rows, all six adopted or parent PMID leads, and two additional original activity/PBP studies.

Selection: Queue 216. Original 13 captured inputs preserved; three actual ARO inventory inputs appended before detailed judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:131729 | data/antibiotics/antibacterial/cefcapene.yaml | generated | cefcapene |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema check | passed | True | CHEBI:131729 | Exit 0. |
| Documented strict check | passed | True | CHEBI:131729 | Exit 0; zero ERROR rows. |
| Supplemental exact graph comparison | passed | False | CHEBI:131729 | Exit 0 using the 019 chemistry interpreter against 022 files. |
| Structured source applicability | not_applicable | False | CHEBI:131729 | The native record has no named protein, gene, pathway, stress-response or transcriptomic claim requiring a structured adapter cross-check. |
| Authoritative full QC | failed | True | CHEBI:131729 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:131729 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:131729 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:131729 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:131729 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:131729 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:131729 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:131729 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:131729 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact active free acid and stereochemistry

identity: supported. Targets: CHEBI:131729.

Checked authorities agree with the native graph, stereocenters and Z alkene. The native definition distinguishes the pivoxil ester.

### Parents, roles and antibacterial classification

grounding: supported. Targets: CHEBI:131729.

Chemical parent and role terms match the graph and source owners; primary S-1006 activity supports antibacterial context.

### Optional primary mechanism enrichment

completeness: unknown. Targets: CHEBI:131729.

Primary PBP affinity evidence was located and its original abstract inspected, but full methods were not retrieved. There is no native target overclaim requiring correction.

### Enzyme and prodrug boundaries

evidence: supported. Targets: CHEBI:131729.

Transient class C enzyme inactivation, active S-1006 PBP affinity and pivoxil/pivalate adverse effects remain separate claims.

### Source ownership, reference depth and history

provenance: supported. Targets: CHEBI:131729.

All six adopted or parent MED references resolve at declared depth, owners match, and four source-history events remain intact.

### Focused validation

schema: supported. Targets: CHEBI:131729.

Focused schema, strict and supplemental chemistry checks passed.

### Retained encyclopedia document link

evidence: supported. Targets: CHEBI:131729.

The document resolves to the named compound and its identity infobox agrees; clinical product and evidence-level boundaries remain explicit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cefcapene.yaml; Entire native YAML and four history events | supports | EXACT/SEEDED cefcapene is the neutral active free acid. Its definition explicitly identifies the corresponding pivaloyloxymethyl ester as a prodrug. There is no populated mode, molecular target, resistance entry, MIC, producer or causal graph. All four history events concern source seeding. |
| chemistry | CHEBI:131729; PubChem:6436055; CHEMBL582912; KEGG:D07638; 216-chemistry.py/.json and public source structure snapshots | supports | Native SMILES, InChI, full key HJJRIJDTIPFROI-NVKITGPLSA-N, formula C17H19N5O6S2, net charge 0 and masses agree. The two configured centers are 6R/7R and the side-chain alkene is Z. Current ChEBI, PubChem, ChEMBL and KEGG graphs agree with the active free acid rather than pivoxil, hydrochloride or hydrate. |
| grounding | CHEBI:131729; ARO:3007475; ARO:0000032; 216-ols.json; individual ChEBI term snapshots; 216-aro-stanzas.txt; 216-kegg.txt; 216-drugcentral.html | supports | The exact compound and cephalosporin class resolve. ChEBI parents are secondary carboxamide, carbamate ester, cephalosporin, carboxylic acid, 1,3-thiazoles and enamide; roles are antimicrobial agent and antibacterial drug. These match the native graph and source rows. DrugCentral 4159 and KEGG D07638 resolve at drug-context scope. CAS 135889-00-8 is corroborated through authorities, not direct registry access. Reaxys 6945919 was not independently resolved. |
| adopted-leads | PMID:12373482; PMID:36872372; PMID:29017833; PMID:11585791; PMID:15673804; PMID:6810737; 216-core.json; 216-lead-dispositions.json | context_only | All six MED records resolve. Complete abstracts were read for the class C enzyme study 12373482, pivoxil adverse-event case 36872372, allergy review 29017833 and ESBL review 11585791. Parent reviews 15673804 and 6810737 are metadata-only because no indexed abstract was returned. Full original case text was also read. |
| class-c | PMID:12373482; DOI:10.1007/s10156-002-0177-7; 216-core.json; 216-classc.pdf is publisher HTML containing the complete abstract and a subscription-preview notice | partial | The original study compares cefcapene and cefpodoxime with selected beta-lactamases. Its abstract describes cefcapene as a poor substrate or inactivator of tested class C enzymes and explicitly reports transient inactivation with enzyme reactivation. This is not universal irreversible inhibition, not a clinical susceptibility guarantee and not direct evidence of primary PBP-mediated killing. The abstract names cefotaxime in one class A kinetic sentence despite its stated cefcapene/cefpodoxime comparison; no quantitative value from that ambiguous sentence is adopted. |
| prodrug-case | PMID:36872372; DOI:10.1186/s12902-023-01314-5; 216-case.xml, full case presentation and discussion | context_only | The original report concerns cefcapene pivoxil hydrochloride in an elderly malnourished patient with subclinical ACTH deficiency. Its interpretation involves pivalate-associated carnitine loss after prodrug hydrolysis, with acknowledged unmeasured urinary carnitine and blood ketones. This supports the prodrug distinction and an individual adverse-event context, not a native free-acid antibacterial assay or direct toxicity mechanism of cefcapene itself. |
| pbp | DOI:10.11250/chemotherapy1953.41.Supplement1_102; 216-pbp.html, complete original journal abstract | partial | Nomura, Doi and Yoshida explicitly distinguish oral prodrug S-1108 from active S-1006. The abstract reports affinity of S-1006 for E. coli K12 PBP3 and additional PBPs, and affinity for S. aureus ATCC 25923 PBPs. It also describes enzyme-specific hydrolysis differences. This is compound-specific primary PBP evidence at abstract depth; the PDF could not be retrieved, so detailed competition methods, preparations and quantitative thresholds were not verified. |
| activity | PMID:1416835; DOI:10.1128/aac.36.6.1336; 216-additional-core.json, complete original abstract | partial | The original S-1006 study explicitly identifies the active component of S-1108 and reports antibacterial activity in tested bacterial panels. Selected TEM/PSE and other enzyme hydrolysis results show why stability must remain enzyme-specific. This supports active cefcapene antibacterial activity without converting historical panel results into universal susceptibility or adopting an unverified exact-form MIC. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; 216 source-row snapshots and 216-local-hits.txt | supports | ChEBI owns the graph, definition, parents, roles, synonyms and two citation leads. The ARO row supplies its cephalosporin concept and the pivoxil case citation. The adopted ARO resistance and target inventories have no row for ARO:3007475. An ignored-inclusive search found no separate cefcapene curator claim overlay. |
| validation | Focused native validators and supplemental chemistry; 216-strict.tsv; 216-chemistry.json | supports | Schema and strict checks passed with exit 0; strict reported zero ERROR rows. Supplemental graph comparison passed using the existing 019 RDKit environment against 022 files. Required shared corpus gates remain separate. |
| wiki-document | https://en.wikipedia.org/wiki/Cefcapene; Direct article/infobox inspection by the review agent; named document link only. | supports | The native document link resolves to Cefcapene; the infobox displays the matching free-acid InChIKey HJJRIJDTIPFROI-NVKITGPLSA-N. This checks document relevance, not primary antibacterial or mechanism evidence. Clinical adverse-effect prose concerns pivoxil products and is not transferred to the active acid. |

## Limits And Additional Notes

- Two adopted parent references, 15673804 and 6810737, are metadata-only. Four adopted/parent abstracts, one additional MED primary abstract and the original J-STAGE PBP abstract were read; full text was read for the pivoxil case only.
- The J-STAGE primary PBP PDF request failed with a connection reset; its public PDF route was also inaccessible through the web tool. The complete original journal abstract was inspected. The class C PDF request returned publisher HTML showing only the complete abstract and subscription preview, not a PDF or full methods.
- A future curator can pursue the exact S-1006 PBP experiment through the native validated writer and curation-event path after confirming reagent form, assay protocol and protein identities. Any enriched mode/target or resistance evidence needs the appropriate primary claim-level placement and native validators. Missing optional enrichment is not a demonstrated required defect.
- The pivoxil hydrochloride case is not exact free-acid adverse-effect evidence. Historical susceptibility and selected beta-lactamase hydrolysis/inactivation results are not generalized to every organism or present-day clinical resistance.
- CAS was checked through authorities rather than the CAS registry; Reaxys was not independently resolved and DrugCentral was inspected at drug-card scope. The 022 native environment lacks RDKit, so supplemental chemistry used the existing 019 interpreter. Focused checks do not substitute for shared corpus checks or native REVIEWED gates.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 16 captured repository inputs and the separately recorded external ARO cache retain their hashes. No native record, saved bundle or Git state was modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T111833Z-cefcapene-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of cefcapene
started_at: '2026-10-21T10:55:30Z'
finished_at: '2026-10-21T11:18:33Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: Exact active free-acid identity supported; optional primary mechanism
  enrichment requires full-method verification
scientific_review: true
summary: The cefcapene free-acid graph, 6R/7R centers and Z side chain agree with
  current ChEBI, PubChem, ChEMBL and KEGG. The native definition distinguishes the
  active compound from its pivoxil ester prodrug. All six adopted or parent PMID records
  resolve at stated depth. Original abstracts support S-1006 antibacterial activity
  and PBP affinity, while a full case report concerns pivoxil hydrochloride and pivalate-associated
  carnitine loss. The class C beta-lactamase study describes transient enzyme inactivation.
  No native mechanism or assay is asserted, and no required correction was demonstrated.
  Scientific assessment retains the stated evidence limits; full verification is blocked
  by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/cefcapene.yaml
    sha256: d0217c4bd46cdbb04ec6a5b1d3a6932456836b198a779cbadbd36c34e51762c4
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
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
scope:
  description: Entire exact SEEDED cefcapene record, four history events, all synonyms,
    chemical identifiers, parent and role groundings, actual ChEBI/ARO owner rows,
    all six adopted or parent PMID leads, and two additional original activity/PBP
    studies.
  selection: Queue 216. Original 13 captured inputs preserved; three actual ARO inventory
    inputs appended before detailed judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:131729
targets:
- target_id: CHEBI:131729
  path: data/antibiotics/antibacterial/cefcapene.yaml
  label: cefcapene
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
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO inventory or imported claim owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Actual ARO inventory or imported claim owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Actual ARO inventory or imported claim owner
checks:
- check_id: schema
  name: Documented schema check
  status: passed
  required: true
  summary: Exit 0.
  target_ids:
  - CHEBI:131729
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefcapene.yaml
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
  - CHEBI:131729
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefcapene.yaml --out /private/tmp/am-review-session/216-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Supplemental exact graph comparison
  status: passed
  required: false
  summary: Exit 0 using the 019 chemistry interpreter against 022 files.
  target_ids:
  - CHEBI:131729
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/216-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: structured-adapter
  name: Structured source applicability
  status: not_applicable
  required: false
  summary: The native record has no named protein, gene, pathway, stress-response
    or transcriptomic claim requiring a structured adapter cross-check.
  target_ids:
  - CHEBI:131729
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
  - CHEBI:131729
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
  - CHEBI:131729
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
  - CHEBI:131729
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
  - CHEBI:131729
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
  - CHEBI:131729
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
  - CHEBI:131729
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
  - CHEBI:131729
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
  - CHEBI:131729
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
  - CHEBI:131729
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cefcapene.yaml
  locator: Entire native YAML and four history events
  accessed_at: '2026-10-21T11:10:29Z'
  support: supports
  summary: EXACT/SEEDED cefcapene is the neutral active free acid. Its definition
    explicitly identifies the corresponding pivaloyloxymethyl ester as a prodrug.
    There is no populated mode, molecular target, resistance entry, MIC, producer
    or causal graph. All four history events concern source seeding.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:131729; PubChem:6436055; CHEMBL582912; KEGG:D07638
  locator: 216-chemistry.py/.json and public source structure snapshots
  accessed_at: '2026-10-21T11:10:29Z'
  support: supports
  summary: Native SMILES, InChI, full key HJJRIJDTIPFROI-NVKITGPLSA-N, formula C17H19N5O6S2,
    net charge 0 and masses agree. The two configured centers are 6R/7R and the side-chain
    alkene is Z. Current ChEBI, PubChem, ChEMBL and KEGG graphs agree with the active
    free acid rather than pivoxil, hydrochloride or hydrate.
  snapshot_sha256: 1a4c2a13f47673ca44ac5f7160311e42163430def724e277b85bc79e36881dd9
- evidence_id: grounding
  kind: authority
  reference: CHEBI:131729; ARO:3007475; ARO:0000032
  locator: 216-ols.json; individual ChEBI term snapshots; 216-aro-stanzas.txt; 216-kegg.txt;
    216-drugcentral.html
  accessed_at: '2026-10-21T11:10:29Z'
  support: supports
  summary: The exact compound and cephalosporin class resolve. ChEBI parents are secondary
    carboxamide, carbamate ester, cephalosporin, carboxylic acid, 1,3-thiazoles and
    enamide; roles are antimicrobial agent and antibacterial drug. These match the
    native graph and source rows. DrugCentral 4159 and KEGG D07638 resolve at drug-context
    scope. CAS 135889-00-8 is corroborated through authorities, not direct registry
    access. Reaxys 6945919 was not independently resolved.
  snapshot_sha256: afc162a11b5ca05e934fbcdfe301324b58c79b406bbe5b5204bd7f3ce5a47669
- evidence_id: adopted-leads
  kind: database
  reference: PMID:12373482; PMID:36872372; PMID:29017833; PMID:11585791; PMID:15673804;
    PMID:6810737
  locator: 216-core.json; 216-lead-dispositions.json
  accessed_at: '2026-10-21T11:10:29Z'
  support: context_only
  summary: All six MED records resolve. Complete abstracts were read for the class
    C enzyme study 12373482, pivoxil adverse-event case 36872372, allergy review 29017833
    and ESBL review 11585791. Parent reviews 15673804 and 6810737 are metadata-only
    because no indexed abstract was returned. Full original case text was also read.
  snapshot_sha256: 9a566a98eb2633816532f285fa8e4dfc73f967290fa98dfce26db1958a7b5f2a
- evidence_id: class-c
  kind: primary_source
  reference: PMID:12373482; DOI:10.1007/s10156-002-0177-7
  locator: 216-core.json; 216-classc.pdf is publisher HTML containing the complete
    abstract and a subscription-preview notice
  accessed_at: '2026-10-21T11:10:29Z'
  support: partial
  summary: The original study compares cefcapene and cefpodoxime with selected beta-lactamases.
    Its abstract describes cefcapene as a poor substrate or inactivator of tested
    class C enzymes and explicitly reports transient inactivation with enzyme reactivation.
    This is not universal irreversible inhibition, not a clinical susceptibility guarantee
    and not direct evidence of primary PBP-mediated killing. The abstract names cefotaxime
    in one class A kinetic sentence despite its stated cefcapene/cefpodoxime comparison;
    no quantitative value from that ambiguous sentence is adopted.
  snapshot_sha256: fdfed719b1008ae0036a60414f9eefc1e66dea71275e3ca41b931623e163d48c
- evidence_id: prodrug-case
  kind: primary_source
  reference: PMID:36872372; DOI:10.1186/s12902-023-01314-5
  locator: 216-case.xml, full case presentation and discussion
  accessed_at: '2026-10-21T11:10:29Z'
  support: context_only
  summary: The original report concerns cefcapene pivoxil hydrochloride in an elderly
    malnourished patient with subclinical ACTH deficiency. Its interpretation involves
    pivalate-associated carnitine loss after prodrug hydrolysis, with acknowledged
    unmeasured urinary carnitine and blood ketones. This supports the prodrug distinction
    and an individual adverse-event context, not a native free-acid antibacterial
    assay or direct toxicity mechanism of cefcapene itself.
  snapshot_sha256: 0b0c052e61fb1fee1471ba2016790e3f3d4d4ed0e73d59d647fb211fce439d8d
- evidence_id: pbp
  kind: primary_source
  reference: DOI:10.11250/chemotherapy1953.41.Supplement1_102
  locator: 216-pbp.html, complete original journal abstract
  accessed_at: '2026-10-21T11:10:29Z'
  support: partial
  summary: Nomura, Doi and Yoshida explicitly distinguish oral prodrug S-1108 from
    active S-1006. The abstract reports affinity of S-1006 for E. coli K12 PBP3 and
    additional PBPs, and affinity for S. aureus ATCC 25923 PBPs. It also describes
    enzyme-specific hydrolysis differences. This is compound-specific primary PBP
    evidence at abstract depth; the PDF could not be retrieved, so detailed competition
    methods, preparations and quantitative thresholds were not verified.
  snapshot_sha256: 12c54dcd75e982f5e9183e249ed97201d589f7b1f240edda848be905f023e531
- evidence_id: activity
  kind: primary_source
  reference: PMID:1416835; DOI:10.1128/aac.36.6.1336
  locator: 216-additional-core.json, complete original abstract
  accessed_at: '2026-10-21T11:10:29Z'
  support: partial
  summary: The original S-1006 study explicitly identifies the active component of
    S-1108 and reports antibacterial activity in tested bacterial panels. Selected
    TEM/PSE and other enzyme hydrolysis results show why stability must remain enzyme-specific.
    This supports active cefcapene antibacterial activity without converting historical
    panel results into universal susceptibility or adopting an unverified exact-form
    MIC.
  snapshot_sha256: 84e7fbd78e2ce0654ec8e0f3d264e90771f045d942eabc631c9fdc71fbd78150
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv
  locator: 216 source-row snapshots and 216-local-hits.txt
  accessed_at: '2026-10-21T11:10:29Z'
  support: supports
  summary: ChEBI owns the graph, definition, parents, roles, synonyms and two citation
    leads. The ARO row supplies its cephalosporin concept and the pivoxil case citation.
    The adopted ARO resistance and target inventories have no row for ARO:3007475.
    An ignored-inclusive search found no separate cefcapene curator claim overlay.
  snapshot_sha256: 935f03e03b15e74dfc56272b657486557097335ba51abea3217bdd35ec641608
  search_scope: rg --no-ignore --hidden across curation, conf and data/antibiotics
    for cefcapene, CHEBI:131729, ARO:3007475, S-1006 and S-1108; full matching inventory
    rows inspected.
- evidence_id: validation
  kind: validation
  reference: Focused native validators and supplemental chemistry
  locator: 216-strict.tsv; 216-chemistry.json
  accessed_at: '2026-10-21T11:10:29Z'
  support: supports
  summary: Schema and strict checks passed with exit 0; strict reported zero ERROR
    rows. Supplemental graph comparison passed using the existing 019 RDKit environment
    against 022 files. Required shared corpus gates remain separate.
- evidence_id: wiki-document
  kind: database
  reference: https://en.wikipedia.org/wiki/Cefcapene
  locator: Direct article/infobox inspection by the review agent; named document link
    only.
  accessed_at: '2026-10-21T11:14:49.739953Z'
  support: supports
  summary: The native document link resolves to Cefcapene; the infobox displays the
    matching free-acid InChIKey HJJRIJDTIPFROI-NVKITGPLSA-N. This checks document
    relevance, not primary antibacterial or mechanism evidence. Clinical adverse-effect
    prose concerns pivoxil products and is not transferred to the active acid.
  snapshot_sha256: 93ca0e0f77a0c9cee6e44566a2c7eb393d942ff71112b5a17b7c5ac868e85612
assessments:
- assessment_id: identity
  area: identity
  topic: Exact active free acid and stereochemistry
  outcome: supported
  summary: Checked authorities agree with the native graph, stereocenters and Z alkene.
    The native definition distinguishes the pivoxil ester.
  target_ids:
  - CHEBI:131729
  evidence_ids:
  - chemistry
  - record
- assessment_id: grounding
  area: grounding
  topic: Parents, roles and antibacterial classification
  outcome: supported
  summary: Chemical parent and role terms match the graph and source owners; primary
    S-1006 activity supports antibacterial context.
  target_ids:
  - CHEBI:131729
  evidence_ids:
  - grounding
  - activity
- assessment_id: mechanism
  area: completeness
  topic: Optional primary mechanism enrichment
  outcome: unknown
  summary: Primary PBP affinity evidence was located and its original abstract inspected,
    but full methods were not retrieved. There is no native target overclaim requiring
    correction.
  target_ids:
  - CHEBI:131729
  evidence_ids:
  - pbp
  - record
- assessment_id: scope
  area: evidence
  topic: Enzyme and prodrug boundaries
  outcome: supported
  summary: Transient class C enzyme inactivation, active S-1006 PBP affinity and pivoxil/pivalate
    adverse effects remain separate claims.
  target_ids:
  - CHEBI:131729
  evidence_ids:
  - class-c
  - pbp
  - prodrug-case
- assessment_id: provenance
  area: provenance
  topic: Source ownership, reference depth and history
  outcome: supported
  summary: All six adopted or parent MED references resolve at declared depth, owners
    match, and four source-history events remain intact.
  target_ids:
  - CHEBI:131729
  evidence_ids:
  - adopted-leads
  - owners
  - record
- assessment_id: schema
  area: schema
  topic: Focused validation
  outcome: supported
  summary: Focused schema, strict and supplemental chemistry checks passed.
  target_ids:
  - CHEBI:131729
  evidence_ids:
  - validation
- assessment_id: wiki-document
  area: evidence
  topic: Retained encyclopedia document link
  outcome: supported
  summary: The document resolves to the named compound and its identity infobox agrees;
    clinical product and evidence-level boundaries remain explicit.
  target_ids:
  - CHEBI:131729
  evidence_ids:
  - wiki-document
findings: []
actions: []
limitations:
- Two adopted parent references, 15673804 and 6810737, are metadata-only. Four adopted/parent
  abstracts, one additional MED primary abstract and the original J-STAGE PBP abstract
  were read; full text was read for the pivoxil case only.
- The J-STAGE primary PBP PDF request failed with a connection reset; its public PDF
  route was also inaccessible through the web tool. The complete original journal
  abstract was inspected. The class C PDF request returned publisher HTML showing
  only the complete abstract and subscription preview, not a PDF or full methods.
- A future curator can pursue the exact S-1006 PBP experiment through the native validated
  writer and curation-event path after confirming reagent form, assay protocol and
  protein identities. Any enriched mode/target or resistance evidence needs the appropriate
  primary claim-level placement and native validators. Missing optional enrichment
  is not a demonstrated required defect.
- The pivoxil hydrochloride case is not exact free-acid adverse-effect evidence. Historical
  susceptibility and selected beta-lactamase hydrolysis/inactivation results are not
  generalized to every organism or present-day clinical resistance.
- CAS was checked through authorities rather than the CAS registry; Reaxys was not
  independently resolved and DrugCentral was inspected at drug-card scope. The 022
  native environment lacks RDKit, so supplemental chemistry used the existing 019
  interpreter. Focused checks do not substitute for shared corpus checks or native
  REVIEWED gates.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 16 captured repository inputs and the separately recorded external ARO cache
  retain their hashes. No native record, saved bundle or Git state was modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.11250/chemotherapy1953.41.Supplement1_102
- https://doi.org/10.1007/s10156-002-0177-7
- https://doi.org/10.1186/s12902-023-01314-5
tags:
- record-review
- cefcapene
- prodrug-scope
```
