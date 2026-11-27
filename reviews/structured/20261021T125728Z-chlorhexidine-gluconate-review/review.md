# Chlorhexidine gluconate: verified FDA product assertions with two misclassified brand synonyms

- Review: 20261021T125728Z-chlorhexidine-gluconate-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:36:40Z
- Finished UTC: 2026-10-21T12:57:28Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact digluconate identity and all 32 retained FDA product assertions are corroborated. One minor correction is needed: Hibiclens and Peridex are brand names, but the native synonym entries mark them exact chemical synonyms. Primary comparator experiments support bounded gluconate antibacterial and membrane effects; no product approval or assay result is generalized to the free base or other salts.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position289; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:28312 | data/antibiotics/antibacterial/chlorhexidine-gluconate.yaml | generated | chlorhexidine gluconate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:28312 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:28312 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:28312 | Actual focused execution exited 0. |
| Structured adapter applicability | not_applicable | False | CHEBI:28312 | The native record contains no protein, gene, pathway or transcriptomic claims. Membrane comparator assays do not identify a native molecular protein target. |
| Authoritative full QC | failed | True | CHEBI:28312 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:28312 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:28312 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:28312 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:28312 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:28312 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:28312 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:28312 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:28312 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Source ownership and history

provenance: supported. Targets: CHEBI:28312.

Maintained source rows and owning extraction/seeding paths were inspected. Initial provenance hashes remain unchanged; source-only and experimental assertions are distinguished.

### Focused documented gates

schema: supported. Targets: CHEBI:28312.

Schema and strict validation passed; independent native chemistry also passed. These checks do not establish biological truth or scientific REVIEWED status.

### Exact digluconate structure and synonym scope

identity: concern. Targets: CHEBI:28312.

The molecular identity and five chemical synonym entries are coherent. Two product names require BRAND_NAME typing. This does not change the selected chemical graph.

### Every retained clinical assertion

evidence: supported. Targets: CHEBI:28312.

All 32 product assertions were checked independently against current FDA responses, including historical approval and present marketing status. Exact GSRS structure binding is preserved.

### Activity role and optional membrane mechanism

evidence: supported. Targets: CHEBI:28312.

Exact gluconate comparator methods/results support antibacterial activity and defined membrane effects, with concentration-, organism- and assay-specific limitations. No native target/causal mechanism is currently asserted.

### Registry scope

grounding: unknown. Targets: CHEBI:28312.

The CAS and Beilstein mappings are repeated by current official chemical authorities; the proprietary registry records were not independently accessed. No conflicting mapping was identified in the inspected sources.

### Optional definition, mechanism and MIC detail

completeness: unknown. Targets: CHEBI:28312.

Missing optional definition and mechanism fields are not corrective defects. No adopted ChEBI PMID leads occur in this source row. Any future quantitative enrichment needs the exact commercial material and nonstandard contact/neutralization protocol.

## Findings

### F1: Type Hibiclens and Peridex as brand names

minor / open / confirmed; issue key: chlorhexidine-gluconate-brand-synonyms.

Native synonyms[2] Hibiclens and synonyms[3] Peridex are EXACT_SYNONYM entries. Current FDA product records establish these as product brands whose active ingredient is chlorhexidine gluconate. Preserve discoverability while using the native BRAND_NAME distinction.

## Recommended Actions And Acceptance Checks

### A1

Correct the two brand synonym types through a maintained source/seeding correction.

- Hibiclens and Peridex remain searchable as BRAND_NAME, while true exact chemical names remain EXACT_SYNONYM.
- Preserve all 32 product-specific clinical assertions and their historical source metadata.
- Re-seeding reproduces the correction; focused schema/strict and applicable corpus gates pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/chlorhexidine-gluconate.yaml; Entire native YAML, all populated domains and all history events | supports | Read the whole native record without changing it. All initial captured hashes were retained; actual source-owner inputs were appended before detailed assessment. |
| owners | 289-raw-rows.json; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact source rows and applicable source assembly/attachment functions | supports | Inspected adopted rows against the native fields, including identifier, source mint, chemical fields, parents, roles, synonyms and source/history scope. Provenance agreement is distinguished from scientific validation. |
| chemistry | 289-chemistry.json; 029-xref-check.json; Independent RDKit native encoding and official external structure comparisons | supports | Native SMILES and InChI agree on the full key, formula, charge, masses and fragment/stereochemical scope. Official external molecular comparisons described below preserve salts and configured stereochemistry. |
| search | 029-local-hits.txt; official source retrieval and original-paper follow-up; Ignored-inclusive local source/curation search; bounded official and primary-source discovery | supports | Local searches included hidden and ignored files in the stated repository source/curation scope. Adopted citation leads were resolved separately from additional discovery. No claim of an exhaustive literature search is made. |
| identity | CHEBI:28312; KEGG:D00858; FDA GSRS UNII:MOR84MUD8E; 289-chebi.json, KEGG molfile and 289-gsrs.json; full molecular comparison | supports | Native, ChEBI, KEGG and GSRS molfile agree on YZIYKJHYYHPJIB-UUPCJSQJSA-N, C34H54Cl2N10O14, charge zero, three components and eight configured D-gluconate stereocenters. The standardized representation contains chlorhexidine plus two D-gluconic-acid components. Broader D-gluconate-adduct/organochlorine parents are coherent. Current GSRS version 44 is later than retained historical version 38; this does not invalidate the dated source provenance. |
| fda | FDA Drugs@FDA, all 31 retained applications / 32 products; 289-fda-audit.json; all original submission/product responses; data/raw/fda_clinical_status.tsv and attach_fda_clinical_status | supports | All 32 application/product identifiers, sponsors, names, active-ingredient names, approval dates/AP statuses and marketing statuses match current original FDA responses. NDA019258 has two products. Native currently_marketed flags agree with retained marketing statuses; discontinued products retain historical APPROVED status rather than current-market availability. The seeder joins exact full InChIKey via GSRS, not just ingredient-name similarity. These are product-level US assertions, not approval of every formulation or indication. |
| brands | FDA NDA017768 product001; NDA019028 product001; Current FDA products brand_name and ingredient fields, plus native synonyms[2:4] | refutes | FDA distinguishes HIBICLENS and PERIDEX product brand names from CHLORHEXIDINE GLUCONATE active ingredient. Native synonyms[2] and [3] use EXACT_SYNONYM for these brands. The adopted ChEBI row supplies them as generic SYNONYM and the seeder retains that type; this is a reproducible source-normalization issue. |
| primary | PMID:25987609; DOI:10.1128/AAC.05048-14; PMC4505255; Original main HTML: Materials/Methods, relevant chlorhexidine comparator Results/Discussion, Tables1–3 and figure captions | partial | The study explicitly uses commercial Hibitane chlorhexidine gluconate solution as a comparator to olanexidine. Chlorhexidine data are kept separate. Modified short-contact MBCs use aqueous bacterial challenge at 23±3 C for 30/60/180 seconds, SCDLP neutralization and subsequent growth, not a standard overnight MIC assay. Clinical-isolate ranges vary markedly, including CHG 180-second MRSA MBCs 2500 to &gt;5000 microgram/mL. E. coli ML35p assays show outer/inner-membrane permeability at &gt;=2.5 microgram/mL; S. aureus ATCC29213 depolarization occurs at 5–50 microgram/mL. Probe displacement from LPS/lipid A/LTA is a comparator assay, not a binding Kd. These data support bounded membrane effects and antibacterial activity; they do not establish a universal single target or transfer olanexidine-specific effects. |

## Limits And Additional Notes

- Primary comparator paper was read in the stated methods, relevant results/discussion, tables and captions; not every main-text paragraph, figure image or supplementary experiment was independently audited.
- Current GSRS version44 corroborates the same complete molecular graph; historical version38 was not retrieved as a separate archival API object. The committed dated source row was inspected.
- CAS/Beilstein proprietary records were not directly queried. No clinical advice or universal claim about all chlorhexidine products is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record, maintained input, scientific status or history was changed. This review is evidence for separately authorized curation, not status promotion.
- Root completed the entire native-record audit, preserved every captured input hash and inspected each adopted literature lead at the explicitly documented depth. Final saved conclusions retain all access, material, organism and assay boundaries.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T125728Z-chlorhexidine-gluconate-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Chlorhexidine gluconate: verified FDA product assertions with two misclassified
  brand synonyms'
started_at: '2026-10-21T12:36:40Z'
finished_at: '2026-10-21T12:57:28Z'
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
summary: 'Exact digluconate identity and all 32 retained FDA product assertions are
  corroborated. One minor correction is needed: Hibiclens and Peridex are brand names,
  but the native synonym entries mark them exact chemical synonyms. Primary comparator
  experiments support bounded gluconate antibacterial and membrane effects; no product
  approval or assay result is generalized to the free base or other salts.'
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
  - path: data/antibiotics/antibacterial/chlorhexidine-gluconate.yaml
    sha256: 21c27a12f3e2239e0667062873051bf62e4611cd12a86f157adfd43adc31c311
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
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/extract_fda_clinical_status.py
    sha256: f30f385ea6d530dc1749e3d805dbcdbc8715fbc476abc510bf144ea13964e171
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
targets:
- target_id: CHEBI:28312
  path: data/antibiotics/antibacterial/chlorhexidine-gluconate.yaml
  label: chlorhexidine gluconate
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
    path: data/raw/chebi_role_names.tsv
    role: ChEBI activity role label resolution
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: FDA product and GSRS exact-structure assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: FDA product ingestion and identity gate
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position289; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:28312
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:28312
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    289
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:28312
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/chlorhexidine-gluconate.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:28312
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/chlorhexidine-gluconate.yaml --out /private/tmp/am-review-session/289-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: structured-adapter
  name: Structured adapter applicability
  status: not_applicable
  required: false
  summary: The native record contains no protein, gene, pathway or transcriptomic
    claims. Membrane comparator assays do not identify a native molecular protein
    target.
  target_ids:
  - CHEBI:28312
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:28312
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
  - CHEBI:28312
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
  - CHEBI:28312
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
  - CHEBI:28312
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
  - CHEBI:28312
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
  - CHEBI:28312
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
  - CHEBI:28312
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
  - CHEBI:28312
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
  - CHEBI:28312
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/chlorhexidine-gluconate.yaml
  locator: Entire native YAML, all populated domains and all history events
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: Read the whole native record without changing it. All initial captured
    hashes were retained; actual source-owner inputs were appended before detailed
    assessment.
- evidence_id: owners
  kind: record_content
  reference: 289-raw-rows.json; scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  locator: Exact source rows and applicable source assembly/attachment functions
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: Inspected adopted rows against the native fields, including identifier,
    source mint, chemical fields, parents, roles, synonyms and source/history scope.
    Provenance agreement is distinguished from scientific validation.
  snapshot_sha256: 235d64c6bc419d2a7b373bc39d97884bae3b73f19c8b2b63cd6d868c634c09bd
- evidence_id: chemistry
  kind: validation
  reference: 289-chemistry.json; 029-xref-check.json
  locator: Independent RDKit native encoding and official external structure comparisons
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: Native SMILES and InChI agree on the full key, formula, charge, masses
    and fragment/stereochemical scope. Official external molecular comparisons described
    below preserve salts and configured stereochemistry.
  snapshot_sha256: 74aabf79e545bbfa82045c57cf00be2a89c3ac57014c2ef1442fdf8688452982
- evidence_id: search
  kind: search
  reference: 029-local-hits.txt; official source retrieval and original-paper follow-up
  locator: Ignored-inclusive local source/curation search; bounded official and primary-source
    discovery
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: Local searches included hidden and ignored files in the stated repository
    source/curation scope. Adopted citation leads were resolved separately from additional
    discovery. No claim of an exhaustive literature search is made.
  search_scope: Exact compound names/identifiers in conf, curation, data/raw, scripts
    and docs using rg --no-ignore --hidden; official registries and original-paper
    sources retrieved 2026-10-21.
  snapshot_sha256: d9a197c22e7a2a8497755404097bbdde15925d25a022cebdd7e38c3162d58d94
- evidence_id: identity
  kind: authority
  reference: CHEBI:28312; KEGG:D00858; FDA GSRS UNII:MOR84MUD8E
  locator: 289-chebi.json, KEGG molfile and 289-gsrs.json; full molecular comparison
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: Native, ChEBI, KEGG and GSRS molfile agree on YZIYKJHYYHPJIB-UUPCJSQJSA-N,
    C34H54Cl2N10O14, charge zero, three components and eight configured D-gluconate
    stereocenters. The standardized representation contains chlorhexidine plus two
    D-gluconic-acid components. Broader D-gluconate-adduct/organochlorine parents
    are coherent. Current GSRS version 44 is later than retained historical version
    38; this does not invalidate the dated source provenance.
  snapshot_sha256: 14731599db9e249b303f4cd228d2db042cb42e2c72a20671bd61b4af6c735a2f
- evidence_id: fda
  kind: authority
  reference: FDA Drugs@FDA, all 31 retained applications / 32 products
  locator: 289-fda-audit.json; all original submission/product responses; data/raw/fda_clinical_status.tsv
    and attach_fda_clinical_status
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: All 32 application/product identifiers, sponsors, names, active-ingredient
    names, approval dates/AP statuses and marketing statuses match current original
    FDA responses. NDA019258 has two products. Native currently_marketed flags agree
    with retained marketing statuses; discontinued products retain historical APPROVED
    status rather than current-market availability. The seeder joins exact full InChIKey
    via GSRS, not just ingredient-name similarity. These are product-level US assertions,
    not approval of every formulation or indication.
  snapshot_sha256: 6d1d50dfc4bbcc0d49eee5452cb3926d3d41035cf24dccd7cf27af4a9fa083c2
- evidence_id: brands
  kind: authority
  reference: FDA NDA017768 product001; NDA019028 product001
  locator: Current FDA products brand_name and ingredient fields, plus native synonyms[2:4]
  accessed_at: '2026-10-21T12:52:33Z'
  support: refutes
  summary: FDA distinguishes HIBICLENS and PERIDEX product brand names from CHLORHEXIDINE
    GLUCONATE active ingredient. Native synonyms[2] and [3] use EXACT_SYNONYM for
    these brands. The adopted ChEBI row supplies them as generic SYNONYM and the seeder
    retains that type; this is a reproducible source-normalization issue.
  snapshot_sha256: e08bc4fdc22774bd442aff49ce973fca746e636ba2577ec1023e95eddd7b7723
- evidence_id: primary
  kind: primary_source
  reference: PMID:25987609; DOI:10.1128/AAC.05048-14; PMC4505255
  locator: 'Original main HTML: Materials/Methods, relevant chlorhexidine comparator
    Results/Discussion, Tables1–3 and figure captions'
  accessed_at: '2026-10-21T12:52:33Z'
  support: partial
  summary: The study explicitly uses commercial Hibitane chlorhexidine gluconate solution
    as a comparator to olanexidine. Chlorhexidine data are kept separate. Modified
    short-contact MBCs use aqueous bacterial challenge at 23±3 C for 30/60/180 seconds,
    SCDLP neutralization and subsequent growth, not a standard overnight MIC assay.
    Clinical-isolate ranges vary markedly, including CHG 180-second MRSA MBCs 2500
    to >5000 microgram/mL. E. coli ML35p assays show outer/inner-membrane permeability
    at >=2.5 microgram/mL; S. aureus ATCC29213 depolarization occurs at 5–50 microgram/mL.
    Probe displacement from LPS/lipid A/LTA is a comparator assay, not a binding Kd.
    These data support bounded membrane effects and antibacterial activity; they do
    not establish a universal single target or transfer olanexidine-specific effects.
  snapshot_sha256: b0d9e05a12bdf4b1e887806af5ff27310c133f977686d3d8b8eb1bc8ea1d6171
assessments:
- assessment_id: provenance
  area: provenance
  topic: Source ownership and history
  outcome: supported
  summary: Maintained source rows and owning extraction/seeding paths were inspected.
    Initial provenance hashes remain unchanged; source-only and experimental assertions
    are distinguished.
  target_ids:
  - CHEBI:28312
  evidence_ids:
  - native
  - owners
- assessment_id: validation
  area: schema
  topic: Focused documented gates
  outcome: supported
  summary: Schema and strict validation passed; independent native chemistry also
    passed. These checks do not establish biological truth or scientific REVIEWED
    status.
  target_ids:
  - CHEBI:28312
  evidence_ids:
  - chemistry
- assessment_id: identity
  area: identity
  topic: Exact digluconate structure and synonym scope
  outcome: concern
  summary: The molecular identity and five chemical synonym entries are coherent.
    Two product names require BRAND_NAME typing. This does not change the selected
    chemical graph.
  target_ids:
  - CHEBI:28312
  evidence_ids:
  - identity
  - chemistry
  - brands
- assessment_id: clinical
  area: evidence
  topic: Every retained clinical assertion
  outcome: supported
  summary: All 32 product assertions were checked independently against current FDA
    responses, including historical approval and present marketing status. Exact GSRS
    structure binding is preserved.
  target_ids:
  - CHEBI:28312
  evidence_ids:
  - fda
  - identity
- assessment_id: antibacterial
  area: evidence
  topic: Activity role and optional membrane mechanism
  outcome: supported
  summary: Exact gluconate comparator methods/results support antibacterial activity
    and defined membrane effects, with concentration-, organism- and assay-specific
    limitations. No native target/causal mechanism is currently asserted.
  target_ids:
  - CHEBI:28312
  evidence_ids:
  - primary
  - native
- assessment_id: proprietary
  area: grounding
  topic: Registry scope
  outcome: unknown
  summary: The CAS and Beilstein mappings are repeated by current official chemical
    authorities; the proprietary registry records were not independently accessed.
    No conflicting mapping was identified in the inspected sources.
  target_ids:
  - CHEBI:28312
  evidence_ids:
  - identity
  - search
- assessment_id: completeness
  area: completeness
  topic: Optional definition, mechanism and MIC detail
  outcome: unknown
  summary: Missing optional definition and mechanism fields are not corrective defects.
    No adopted ChEBI PMID leads occur in this source row. Any future quantitative
    enrichment needs the exact commercial material and nonstandard contact/neutralization
    protocol.
  target_ids:
  - CHEBI:28312
  evidence_ids:
  - native
  - owners
  - primary
findings:
- finding_id: F1
  issue_key: chlorhexidine-gluconate-brand-synonyms
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Type Hibiclens and Peridex as brand names
  description: Native synonyms[2] Hibiclens and synonyms[3] Peridex are EXACT_SYNONYM
    entries. Current FDA product records establish these as product brands whose active
    ingredient is chlorhexidine gluconate. Preserve discoverability while using the
    native BRAND_NAME distinction.
  target_ids:
  - CHEBI:28312
  field_paths:
  - synonyms[2].synonym_type
  - synonyms[3].synonym_type
  evidence_ids:
  - native
  - owners
  - brands
  - fda
  rule_id: Native synonym-type semantics and exact molecule/product distinction
  native_severity: minor
  normalization_reason: The chemical graph and FDA products are correct; the defect
    is a bounded product-name classification error.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Imported generic synonym labels
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated synonym typing
actions:
- action_id: A1
  description: Correct the two brand synonym types through a maintained source/seeding
    correction.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:28312
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Imported generic synonym labels
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated synonym typing
  acceptance_checks:
  - Hibiclens and Peridex remain searchable as BRAND_NAME, while true exact chemical
    names remain EXACT_SYNONYM.
  - Preserve all 32 product-specific clinical assertions and their historical source
    metadata.
  - Re-seeding reproduces the correction; focused schema/strict and applicable corpus
    gates pass.
limitations:
- Primary comparator paper was read in the stated methods, relevant results/discussion,
  tables and captions; not every main-text paragraph, figure image or supplementary
  experiment was independently audited.
- Current GSRS version44 corroborates the same complete molecular graph; historical
  version38 was not retrieved as a separate archival API object. The committed dated
  source row was inspected.
- CAS/Beilstein proprietary records were not directly queried. No clinical advice
  or universal claim about all chlorhexidine products is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record, maintained input, scientific status or history was changed. This
  review is evidence for separately authorized curation, not status promotion.
- Root completed the entire native-record audit, preserved every captured input hash
  and inspected each adopted literature lead at the explicitly documented depth. Final
  saved conclusions retain all access, material, organism and assay boundaries.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
