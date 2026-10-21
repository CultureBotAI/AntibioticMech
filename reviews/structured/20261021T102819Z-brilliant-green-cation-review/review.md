# brilliant green cation: exact chemical form and primary evidence scope

- Review: 20261021T102819Z-brilliant-green-cation-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:59:36Z
- Finished UTC: 2026-10-21T10:28:19Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The exact native molecular representation and broad antibacterial context are supported; no confirmed corrective finding was established. The free cation and hydrogensulfate salt remain separate records; assay mass cannot be transferred between forms without material verification. Focused schema, strict and molecular consistency checks pass. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position169; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:88176 | data/antibiotics/antibacterial/brilliant-green-cation.yaml | generated | brilliant green cation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:88176 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:88176 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:88176 | Actual focused execution exited 0. |
| Structured protein-context applicability | not_applicable | False | CHEBI:88176 | The native record contains no protein, gene, regulator, pathway or transcriptomic-response claim. Literature host-cell signaling and chemical dye assays are not used to infer bacterial targets or expression responses. |
| Authoritative full QC | failed | True | CHEBI:88176 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:88176 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:88176 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:88176 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:88176 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:88176 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:88176 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:88176 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:88176 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact graph, chemical form and external mappings

identity: supported. Targets: CHEBI:88176.

Internal chemical representation is consistent. External comparison limits and material distinctions are explicit; no unsupported exact replacement is proposed.

### Chemical parents and broad antibacterial role

grounding: supported. Targets: CHEBI:88176.

Current chemical parents fit the graph and original biological evidence supports bounded antibacterial context. Specific MICs, host-cell effects and compound-family mechanisms are not generalized.

### Source-owned definition

evidence: supported. Targets: CHEBI:88176.

The source definition is compatible with the inspected identity and occurrence evidence, with stated material and source-access limits.

### Maintained source and history

provenance: supported. Targets: CHEBI:88176.

Source ownership and initial hashes are preserved; no native data, source inventories or history were edited.

### Primary evidence and optional fields

completeness: unknown. Targets: CHEBI:88176.

Optional exact-assay evidence can be improved, but blanks are not missing requirements. A direct bacterial protein target, producer biosynthesis or clinical indication is not inferred from the inspected evidence.

### Focused repository and chemical gates

schema: supported. Targets: CHEBI:88176.

Actual focused gates and chemical checks pass; scientific source fidelity remains a separate assessment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/brilliant-green-cation.yaml; Entire native YAML, exact maintained source row and history | supports | The SEEDED record contains source-owned chemical identity, definition, synonyms, cross-references and antibacterial role. It has no populated direct molecular target, resistance mechanism, quantitative susceptibility, producer organism or causal graph. The graph is a single C27H33N2 cation with charge+1; DrugCentral4665 is its only external cross-reference. |
| source | data/raw/chebi_antimicrobials.tsv; data/raw/chebi_role_names.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; 169-raw.json; initially captured maintained owners | supports | The adopted source row reproduces the native fields. Local exact identity and owner searches included ignored and hidden files outside Git internals and virtual environments. No matching curator override was found within inspected maintained inventories; this is bounded local absence, not evidence absence. |
| chemistry | Independent native molecular encodings and focused gates; 169-chemistry.json; 169-focused-results.json | supports | SMILES and Standard InChI independently reproduce the complete stored key, molecular formula, formal charge, component count and both mass values at native precision. Source mint and focused schema/strict checks pass. No unassigned tetrahedral stereocentre is present. |
| grounding | https://www.ebi.ac.uk/chebi/CHEBI:88176; 169-chebi.html; 169-parents.json | supports | Current source definition, roles and chemical parents resolve. The direct parents are iminium ion CHEBI:35286. These chemical classes fit the encoded graph; database classification is not promoted to an experimentally demonstrated protein mechanism. |
| external-identity | PubChem:12450; DrugCentral:4665; 169-pubchem.json; 169-drugcentral.inchi; 169-drugcentral.smiles; 017-root-next-xref-chemistry.json | supports | Current PubChem12450 and both independently parsed DrugCentral molecular encodings match the full cation key HXCILVUBKWANLN-UHFFFAOYSA-N. DrugCentral displays generic drug/salt nomenclature and a salt CAS but its actual graph is the cation, so the native graph cross-reference is concordant. Its modeled properties are not bacterial targets or evidence of approval. |
| primary-activity | PMID:33339219; DOI:10.3390/ph13120469; 170-bg2020.xml; biological Results2.2, lipophilicity2.3, general reagents and biological Methods3.2–3.3; Table1 XML | supports | Brilliant Green was a reference antibacterial in a study of distinct trisindolylmethylium compounds8a–e. The BG column in Table1 reports activity against several Gram-positive and Gram-negative strains, with P. aeruginosa ATCC27853 above the tested range. Broth microdilution used cation-adjusted Mueller-Hinton medium and complete growth inhibition. The inspected paper does not specify the BG counterion/catalog or establish an isolated free-cation mass basis. Do not transfer compound8 membrane mechanisms to BG. Fibroblast MTT endpoints are separate from bacterial MICs. |
| material-boundary | Comparison of separately encoded cation and salt; 169-chemistry.json; 170-chemistry.json; original primary material description | partial | The cation and hydrogensulfate salt differ in composition, charge and molecular mass. Broad antibacterial role for the active dye component is compatible with the salt literature, but no direct quantitative free-cation assay or counterion-normalized dose was established. The native record asserts no numeric assay, so this limitation is not an incorrect native measurement. |

## Limits And Additional Notes

- Current public records and native molecular encodings were checked, but absolute structures were not independently rederived from raw spectroscopy or crystallography. Proprietary registry databases were not accessed.
- No exhaustive clinical, resistance, transcriptomic or natural-biosynthesis survey is claimed. Optional fields and source classifications were assessed at their actual native evidence level.
- The2020 primary biological Results, reagent description, biological Methods and Table1 XML were inspected. Its synthesis/NMR supporting data were not fully audited. BG counterion/catalog and assay incubation details remain unresolved for quantitative enrichment; the table was not independently reread as a rendered figure.
- The2023 New Microbiologica comparison was located but local full-PDF retrieval failed. Conflicting abstract/indexed numeric summaries were not adopted. The2020 primary comparator is the activity basis used here.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 13 captured repository input hashes were rechecked unchanged. Native records, source inventories and curation status remain unchanged.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T102819Z-brilliant-green-cation-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'brilliant green cation: exact chemical form and primary evidence scope'
started_at: '2026-10-21T09:59:36Z'
finished_at: '2026-10-21T10:28:19Z'
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
verdict: blocked
scientific_review: true
summary: The exact native molecular representation and broad antibacterial context
  are supported; no confirmed corrective finding was established. The free cation
  and hydrogensulfate salt remain separate records; assay mass cannot be transferred
  between forms without material verification. Focused schema, strict and molecular
  consistency checks pass. Scientific assessment retains the stated evidence limits;
  full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/brilliant-green-cation.yaml
    sha256: 3d6ea28ca1a52877d62b6441031a7ce24a73dad09171982550cae186f30da579
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
targets:
- target_id: CHEBI:88176
  path: data/antibiotics/antibacterial/brilliant-green-cation.yaml
  label: brilliant green cation
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
  selection: Initially uncovered queue position169; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:88176
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:88176
  command: .venv/bin/python /private/tmp/am-review-session/focus014-root.py 169
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:88176
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/brilliant-green-cation.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:88176
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/brilliant-green-cation.yaml --out /private/tmp/am-review-session/169-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-applicability
  name: Structured protein-context applicability
  status: not_applicable
  required: false
  summary: The native record contains no protein, gene, regulator, pathway or transcriptomic-response
    claim. Literature host-cell signaling and chemical dye assays are not used to
    infer bacterial targets or expression responses.
  target_ids:
  - CHEBI:88176
  evidence_ids:
  - native
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:88176
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
  - CHEBI:88176
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
  - CHEBI:88176
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
  - CHEBI:88176
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
  - CHEBI:88176
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
  - CHEBI:88176
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
  - CHEBI:88176
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
  - CHEBI:88176
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
  - CHEBI:88176
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/brilliant-green-cation.yaml
  locator: Entire native YAML, exact maintained source row and history
  accessed_at: '2026-10-21T10:19:49Z'
  support: supports
  summary: The SEEDED record contains source-owned chemical identity, definition,
    synonyms, cross-references and antibacterial role. It has no populated direct
    molecular target, resistance mechanism, quantitative susceptibility, producer
    organism or causal graph. The graph is a single C27H33N2 cation with charge+1;
    DrugCentral4665 is its only external cross-reference.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/chebi_role_names.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: 169-raw.json; initially captured maintained owners
  accessed_at: '2026-10-21T10:19:49Z'
  support: supports
  summary: The adopted source row reproduces the native fields. Local exact identity
    and owner searches included ignored and hidden files outside Git internals and
    virtual environments. No matching curator override was found within inspected
    maintained inventories; this is bounded local absence, not evidence absence.
  snapshot_sha256: 1dfc67931d50ee0c284120a495ee3b15316d22ebc81c8b98c3ccef397509aac8
- evidence_id: chemistry
  kind: validation
  reference: Independent native molecular encodings and focused gates
  locator: 169-chemistry.json; 169-focused-results.json
  accessed_at: '2026-10-21T10:19:49Z'
  support: supports
  summary: SMILES and Standard InChI independently reproduce the complete stored key,
    molecular formula, formal charge, component count and both mass values at native
    precision. Source mint and focused schema/strict checks pass. No unassigned tetrahedral
    stereocentre is present.
  snapshot_sha256: 9629cb95642b0cf2dc0de9b200e10c6d8bc9e8f1e16e248cf9cfd6bd5c25944c
- evidence_id: grounding
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:88176
  locator: 169-chebi.html; 169-parents.json
  accessed_at: '2026-10-21T10:19:49Z'
  support: supports
  summary: Current source definition, roles and chemical parents resolve. The direct
    parents are iminium ion CHEBI:35286. These chemical classes fit the encoded graph;
    database classification is not promoted to an experimentally demonstrated protein
    mechanism.
  snapshot_sha256: 5d16b97f23e084c01ec84cf27c492ad1649dafbcebe45e085350c4bd31fcb2c3
- evidence_id: external-identity
  kind: database
  reference: PubChem:12450; DrugCentral:4665
  locator: 169-pubchem.json; 169-drugcentral.inchi; 169-drugcentral.smiles; 017-root-next-xref-chemistry.json
  accessed_at: '2026-10-21T10:19:49Z'
  support: supports
  summary: Current PubChem12450 and both independently parsed DrugCentral molecular
    encodings match the full cation key HXCILVUBKWANLN-UHFFFAOYSA-N. DrugCentral displays
    generic drug/salt nomenclature and a salt CAS but its actual graph is the cation,
    so the native graph cross-reference is concordant. Its modeled properties are
    not bacterial targets or evidence of approval.
  snapshot_sha256: b77a5e2d178320f5e21ec7454a532e6448081293583fa960de33beea10f08081
- evidence_id: primary-activity
  kind: primary_source
  reference: PMID:33339219; DOI:10.3390/ph13120469
  locator: 170-bg2020.xml; biological Results2.2, lipophilicity2.3, general reagents
    and biological Methods3.2–3.3; Table1 XML
  accessed_at: '2026-10-21T10:19:49Z'
  support: supports
  summary: Brilliant Green was a reference antibacterial in a study of distinct trisindolylmethylium
    compounds8a–e. The BG column in Table1 reports activity against several Gram-positive
    and Gram-negative strains, with P. aeruginosa ATCC27853 above the tested range.
    Broth microdilution used cation-adjusted Mueller-Hinton medium and complete growth
    inhibition. The inspected paper does not specify the BG counterion/catalog or
    establish an isolated free-cation mass basis. Do not transfer compound8 membrane
    mechanisms to BG. Fibroblast MTT endpoints are separate from bacterial MICs.
  snapshot_sha256: 39c0353c96f5b1de805fc99d2b5b02d91b4deb27a9989c01f9b4fe577717bb14
- evidence_id: material-boundary
  kind: validation
  reference: Comparison of separately encoded cation and salt
  locator: 169-chemistry.json; 170-chemistry.json; original primary material description
  accessed_at: '2026-10-21T10:19:49Z'
  support: partial
  summary: The cation and hydrogensulfate salt differ in composition, charge and molecular
    mass. Broad antibacterial role for the active dye component is compatible with
    the salt literature, but no direct quantitative free-cation assay or counterion-normalized
    dose was established. The native record asserts no numeric assay, so this limitation
    is not an incorrect native measurement.
  snapshot_sha256: 99afdc9a6474bdb1a805a14e11e578fddc453159be907d617b40d1d8a68d02a4
assessments:
- assessment_id: identity
  area: identity
  topic: Exact graph, chemical form and external mappings
  outcome: supported
  summary: Internal chemical representation is consistent. External comparison limits
    and material distinctions are explicit; no unsupported exact replacement is proposed.
  target_ids:
  - CHEBI:88176
  evidence_ids:
  - chemistry
  - external-identity
- assessment_id: classification
  area: grounding
  topic: Chemical parents and broad antibacterial role
  outcome: supported
  summary: Current chemical parents fit the graph and original biological evidence
    supports bounded antibacterial context. Specific MICs, host-cell effects and compound-family
    mechanisms are not generalized.
  target_ids:
  - CHEBI:88176
  evidence_ids:
  - grounding
  - primary-activity
- assessment_id: definition
  area: evidence
  topic: Source-owned definition
  outcome: supported
  summary: The source definition is compatible with the inspected identity and occurrence
    evidence, with stated material and source-access limits.
  target_ids:
  - CHEBI:88176
  evidence_ids:
  - native
  - external-identity
- assessment_id: provenance
  area: provenance
  topic: Maintained source and history
  outcome: supported
  summary: Source ownership and initial hashes are preserved; no native data, source
    inventories or history were edited.
  target_ids:
  - CHEBI:88176
  evidence_ids:
  - source
  - chemistry
- assessment_id: completeness
  area: completeness
  topic: Primary evidence and optional fields
  outcome: unknown
  summary: Optional exact-assay evidence can be improved, but blanks are not missing
    requirements. A direct bacterial protein target, producer biosynthesis or clinical
    indication is not inferred from the inspected evidence.
  target_ids:
  - CHEBI:88176
  evidence_ids:
  - native
  - primary-activity
- assessment_id: schema
  area: schema
  topic: Focused repository and chemical gates
  outcome: supported
  summary: Actual focused gates and chemical checks pass; scientific source fidelity
    remains a separate assessment.
  target_ids:
  - CHEBI:88176
  evidence_ids:
  - chemistry
findings: []
actions: []
limitations:
- Current public records and native molecular encodings were checked, but absolute
  structures were not independently rederived from raw spectroscopy or crystallography.
  Proprietary registry databases were not accessed.
- No exhaustive clinical, resistance, transcriptomic or natural-biosynthesis survey
  is claimed. Optional fields and source classifications were assessed at their actual
  native evidence level.
- The2020 primary biological Results, reagent description, biological Methods and
  Table1 XML were inspected. Its synthesis/NMR supporting data were not fully audited.
  BG counterion/catalog and assay incubation details remain unresolved for quantitative
  enrichment; the table was not independently reread as a rendered figure.
- The2023 New Microbiologica comparison was located but local full-PDF retrieval failed.
  Conflicting abstract/indexed numeric summaries were not adopted. The2020 primary
  comparator is the activity basis used here.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 13 captured repository input hashes were rechecked unchanged. Native records,
  source inventories and curation status remain unchanged.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:88176
- https://doi.org/10.3390/ph13120469
```
