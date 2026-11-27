# Cephalexin monohydrate: coherent hydrate and FDA assertions with a circular definition

- Review: 20261021T122817Z-cephalexin-monohydrate-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:02:34Z
- Finished UTC: 2026-10-21T12:28:17Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor inherited definition error names hydrate instead of water as the equimolar partner of cephalexin. The native two-component monohydrate graph, full cross-reference structures and GSRS identity agree. All 86 FDA assertions across 47 applications match current application/product metadata; historical source versions remain explicit.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position269; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3535 | data/antibiotics/antibacterial/cephalexin-monohydrate.yaml | generated | cephalexin monohydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:3535 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:3535 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:3535 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:3535 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3535 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3535 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3535 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3535 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3535 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3535 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3535 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3535 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact monohydrate structure

identity: supported. Targets: CHEBI:3535.

Native structure, formula, charge, three stereocentres, masses and checked full cross-references agree.

### Circular hydrate definition

identity: concern. Targets: CHEBI:3535.

Water is the equimolar partner of cephalexin. Repeating hydrate as its own component contradicts the explicit formula.

### Broader parent, role and reference granularity

grounding: supported. Targets: CHEBI:3535.

The hydrate parent and antibacterial-drug role fit the exact form; KEGG compound and drug mappings are separately typed. Beilstein and direct DrugBank content remain access-limited.

### Every FDA product assertion

evidence: supported. Targets: CHEBI:3535.

All 86 product assertions match current official metadata, and GSRS confirms exact form. Source versions are preserved as historical provenance.

### Formulation and active-moiety amounts

evidence: supported. Targets: CHEBI:3535.

Official labels establish monohydrate use while distinguishing active-cephalexin dose equivalents. No original target-binding or exact hydrate-solid MIC is asserted.

### Unpopulated target, resistance, producer and graph domains

completeness: not_applicable. Targets: CHEBI:3535.

No optional omission is a defect. Regulatory microbiology prose is not silently converted to primary mechanistic or strain-level evidence.

### Source owners and history

provenance: supported. Targets: CHEBI:3535.

All 15 captured inputs and six native history events remain intact; full record and source assertions were checked.

## Findings

### F1: Definition names hydrate instead of water as the equimolar component

minor / open / confirmed; issue key: chebi-3535-circular-hydrate-definition.

The native definition says equimolar amounts of hydrate and cephalexin. The stored formula and two-component graph specify one water per cephalexin. Replace the circular component name with water through source-owned correction; preserve the correct structure.

## Recommended Actions And Acceptance Checks

### A1

Correct the source-owned monohydrate definition to specify water and cephalexin in a 1:1 ratio.

- Preserve CHEBI:3535, full monohydrate key, stereochemistry and all independently supported FDA assertions.
- Use a maintained upstream or extraction/adjudication correction that survives reseeding.
- Run schema, strict, provenance and corpus checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cephalexin-monohydrate.yaml; Entire YAML, including all 86 clinical_status_assertions | supports | Read all identity/status fields, ten synonyms, hydrate parent, antibacterial-drug role, complete structure/masses, chemical and drug references, source concept, all FDA assertion fields and six history events. Repeated FDA fields were checked for equality before lossless common-field/variant inspection. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/fda_clinical_status.tsv; scripts/extract_fda_clinical_status.py; scripts/seed_from_sources.py; Exact ChEBI row and 86 matched FDA product rows | supports | ChEBI supplies the circular definition and monohydrate graph. FDA inventory assertions carry application/product identity, original approval, marketing status and exact GSRS UNII. All 15 initial/expanded input hashes remain unchanged. |
| chemistry | Independent RDKit 2026.03.5 native calculation; 269-chemistry.json | supports | SMILES and InChI both generate AVGYWQBCYZHHPN-CYJZLJNKSA-N, C16H19N3O5S (equivalent to C16H17N3O4S.H2O), neutral charge, two components and three R stereocentres. Masses and source mint agree. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:3535; Current full identity and definition | partial | Current ChEBI repeats the native wording equating cephalexin with hydrate rather than water in a monohydrate. Its explicit formula and disconnected water molecule establish the intended composition. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/23325-78-2/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON; CAS 23325-78-2, CID 62921 | supports | Complete molecular graph and InChI agree with the native monohydrate; CAS lookup is PubChem resolution, not proprietary Registry access. |
| kegg | https://rest.kegg.jp/get/C08099; C08099 and D00906 full entries and molfiles | supports | Both KEGG structures independently generate the full monohydrate key. Drug-level D00906 is correctly typed separately from exact compound C08099. |
| external-chemistry | Independent full chemical cross-reference parsing; 027-root-xref-check.json, target 269 | supports | Current ChEBI, PubChem, both KEGG molfiles and GSRS molfile/SMILES all generate the same complete native hydrate key, two-component formula and stereochemistry. |
| gsrs | https://gsrs.ncats.nih.gov/api/v1/substances/OBN7UDS42Y?view=full; Current version 59 structure and identifier | supports | UNII OBN7UDS42Y resolves to the exact native cephalexin monohydrate structure. Native identity_record_version 50 is a dated historical assertion, not a claim to have retrieved current version 59. |
| fda | https://api.fda.gov/drug/drugsfda.json; 47 exact application responses; all 86 native product assertions | supports | For every asserted product, the application, product existence, sponsor, drug name, active ingredient, original AP date, marketing status and currently_marketed flag agree with current FDA data. Three NDAs and the remaining ANDAs are assessed by exact product number; approval is not equated with current marketing. Retrieval details and response hashes are retained in the audit ledger. |
| fda-validation | Actual full assertion comparison; 269-fda-audit.py and 269-fda-audit.json | supports | 86 products across 47 applications checked; zero field mismatches. Current marketing was compared explicitly and all native AP dates against original approved submissions. This verifies the asserted set, not completeness of all possible products. |
| label | https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=02b5cd6f-3df8-43c1-879d-217fcf55231a; FDA label response effective 2025-02-11, ANDA065253; Description and Indications | supports | The exact UNII-associated label describes cephalexin monohydrate with formula C16H17N3O4S.H2O and 365.41 mass. Capsules contain monohydrate expressed as 250 or 500 mg cephalexin equivalents; labelled susceptible-organism indications support antibacterial-drug role, without turning active-moiety dose into hydrate mass. |
| keflex | https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/050405s111lbl.pdf; FDA reference 5845515; sections 11 and 12.4 | supports | The 2026 KEFLEX label explicitly identifies the monohydrate and active-cephalexin dose equivalents. Cell-wall inhibition and organism-specific activity/resistance statements are regulatory summaries, not original binding or strain-MIC experiments. They do not override the current product-specific discontinuation metadata. |
| parents | CHEBI:35505; CHEBI:36047; Current OLS definitions | supports | Hydrate means a water-containing addition compound; antibacterial drug is supported by official product identity and indications. |
| search | Ignored-inclusive maintained-owner and authority search; 269-local-hits.txt; 269-owner-hits.txt; exact FDA and GSRS lookups | context_only | No adopted PMID lead is present in the exact ChEBI owner row. The review followed the populated chemical and regulatory claims through official authority records, with hidden/ignored repository content included outside .git/.venv. |

## Limits And Additional Notes

- The full FDA comparison verifies the 86 asserted products, not completeness of the FDA product universe or future marketing status.
- Beilstein and direct DrugBank content were not independently inspected; other exact public chemical authorities and GSRS agree.
- No primary target experiment or strain-level MIC is inferred from product labels; no such native claim requires correction.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 15 captured input hashes remain unchanged. No native data, source inventory or scientific status changed.
- The current GSRS record version differs from the historically captured version; exact structure agrees, and this temporal difference is not itself a defect.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T122817Z-cephalexin-monohydrate-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cephalexin monohydrate: coherent hydrate and FDA assertions with a circular
  definition'
started_at: '2026-10-21T12:02:34Z'
finished_at: '2026-10-21T12:28:17Z'
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
summary: One minor inherited definition error names hydrate instead of water as the
  equimolar partner of cephalexin. The native two-component monohydrate graph, full
  cross-reference structures and GSRS identity agree. All 86 FDA assertions across
  47 applications match current application/product metadata; historical source versions
  remain explicit.
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
  - path: data/antibiotics/antibacterial/cephalexin-monohydrate.yaml
    sha256: e7eab9a846f19ec268dfc50bffb8cfe478ac09f0419c162755b10094608742a4
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
- target_id: CHEBI:3535
  path: data/antibiotics/antibacterial/cephalexin-monohydrate.yaml
  label: cephalexin monohydrate
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
    role: Actual maintained source or transform for this record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Actual maintained source or transform for this record
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position269; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3535
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3535
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    269
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3535
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cephalexin-monohydrate.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3535
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cephalexin-monohydrate.yaml --out /private/tmp/am-review-session/269-strict.tsv
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
  - CHEBI:3535
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
  - CHEBI:3535
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
  - CHEBI:3535
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
  - CHEBI:3535
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
  - CHEBI:3535
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
  - CHEBI:3535
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
  - CHEBI:3535
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
  - CHEBI:3535
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
  - CHEBI:3535
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cephalexin-monohydrate.yaml
  locator: Entire YAML, including all 86 clinical_status_assertions
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: Read all identity/status fields, ten synonyms, hydrate parent, antibacterial-drug
    role, complete structure/masses, chemical and drug references, source concept,
    all FDA assertion fields and six history events. Repeated FDA fields were checked
    for equality before lossless common-field/variant inspection.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/fda_clinical_status.tsv;
    scripts/extract_fda_clinical_status.py; scripts/seed_from_sources.py
  locator: Exact ChEBI row and 86 matched FDA product rows
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: ChEBI supplies the circular definition and monohydrate graph. FDA inventory
    assertions carry application/product identity, original approval, marketing status
    and exact GSRS UNII. All 15 initial/expanded input hashes remain unchanged.
  snapshot_sha256: 9f07a9d2d2ad870fffcf08729ec8282004f3591822af2b50555f54cd070b4368
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit 2026.03.5 native calculation
  locator: 269-chemistry.json
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: SMILES and InChI both generate AVGYWQBCYZHHPN-CYJZLJNKSA-N, C16H19N3O5S
    (equivalent to C16H17N3O4S.H2O), neutral charge, two components and three R stereocentres.
    Masses and source mint agree.
  snapshot_sha256: d7587f64912938a5e1a8e4dad9f0d8b9f381be1b79ace6f42d2325d2aeb5c066
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3535
  locator: Current full identity and definition
  accessed_at: '2026-10-21T12:21:17Z'
  support: partial
  summary: Current ChEBI repeats the native wording equating cephalexin with hydrate
    rather than water in a monohydrate. Its explicit formula and disconnected water
    molecule establish the intended composition.
  snapshot_sha256: be3ceb6b721b430b0ada06928c8746c2a9fa6e35ec635a616b56ed64363dd865
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/23325-78-2/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON
  locator: CAS 23325-78-2, CID 62921
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: Complete molecular graph and InChI agree with the native monohydrate; CAS
    lookup is PubChem resolution, not proprietary Registry access.
  snapshot_sha256: c80cf201ad4fb4a11171dd3464f6ab76bb33e36311fa667648e6eb7353569fb5
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/C08099
  locator: C08099 and D00906 full entries and molfiles
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: Both KEGG structures independently generate the full monohydrate key. Drug-level
    D00906 is correctly typed separately from exact compound C08099.
  snapshot_sha256: 913102dc6701e4bc528023a9b88d6cd748644ffc11f23bd857a73e666a060388
- evidence_id: external-chemistry
  kind: validation
  reference: Independent full chemical cross-reference parsing
  locator: 027-root-xref-check.json, target 269
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: Current ChEBI, PubChem, both KEGG molfiles and GSRS molfile/SMILES all
    generate the same complete native hydrate key, two-component formula and stereochemistry.
  snapshot_sha256: fae7157a323812f8e3eeb541fc3b030c11787e689fc5e413d94f2737984bbe2e
- evidence_id: gsrs
  kind: authority
  reference: https://gsrs.ncats.nih.gov/api/v1/substances/OBN7UDS42Y?view=full
  locator: Current version 59 structure and identifier
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: UNII OBN7UDS42Y resolves to the exact native cephalexin monohydrate structure.
    Native identity_record_version 50 is a dated historical assertion, not a claim
    to have retrieved current version 59.
  snapshot_sha256: adee36d8c75fb053ed6e660ba5294622371097e7480eba263b4fbaad51030ff7
- evidence_id: fda
  kind: authority
  reference: https://api.fda.gov/drug/drugsfda.json
  locator: 47 exact application responses; all 86 native product assertions
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: For every asserted product, the application, product existence, sponsor,
    drug name, active ingredient, original AP date, marketing status and currently_marketed
    flag agree with current FDA data. Three NDAs and the remaining ANDAs are assessed
    by exact product number; approval is not equated with current marketing. Retrieval
    details and response hashes are retained in the audit ledger.
  snapshot_sha256: 3e084320ba6a5aaa6efda77f182dbb82d2e1275451836b64ea99e89990108e93
- evidence_id: fda-validation
  kind: validation
  reference: Actual full assertion comparison
  locator: 269-fda-audit.py and 269-fda-audit.json
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: 86 products across 47 applications checked; zero field mismatches. Current
    marketing was compared explicitly and all native AP dates against original approved
    submissions. This verifies the asserted set, not completeness of all possible
    products.
  snapshot_sha256: 3e084320ba6a5aaa6efda77f182dbb82d2e1275451836b64ea99e89990108e93
- evidence_id: label
  kind: authority
  reference: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=02b5cd6f-3df8-43c1-879d-217fcf55231a
  locator: FDA label response effective 2025-02-11, ANDA065253; Description and Indications
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: The exact UNII-associated label describes cephalexin monohydrate with formula
    C16H17N3O4S.H2O and 365.41 mass. Capsules contain monohydrate expressed as 250
    or 500 mg cephalexin equivalents; labelled susceptible-organism indications support
    antibacterial-drug role, without turning active-moiety dose into hydrate mass.
  snapshot_sha256: 4e4c8e6713feee2713b4b8a487be358168d3de44d13dc4d1c954c7f63325b1f4
- evidence_id: keflex
  kind: authority
  reference: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/050405s111lbl.pdf
  locator: FDA reference 5845515; sections 11 and 12.4
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: The 2026 KEFLEX label explicitly identifies the monohydrate and active-cephalexin
    dose equivalents. Cell-wall inhibition and organism-specific activity/resistance
    statements are regulatory summaries, not original binding or strain-MIC experiments.
    They do not override the current product-specific discontinuation metadata.
  snapshot_sha256: 53f2ae0182cc8120b6d688e40df3ddb40c14df4e55a8f65952c76d200adb5be2
- evidence_id: parents
  kind: authority
  reference: CHEBI:35505; CHEBI:36047
  locator: Current OLS definitions
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: Hydrate means a water-containing addition compound; antibacterial drug
    is supported by official product identity and indications.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive maintained-owner and authority search
  locator: 269-local-hits.txt; 269-owner-hits.txt; exact FDA and GSRS lookups
  accessed_at: '2026-10-21T12:21:17Z'
  support: context_only
  summary: No adopted PMID lead is present in the exact ChEBI owner row. The review
    followed the populated chemical and regulatory claims through official authority
    records, with hidden/ignored repository content included outside .git/.venv.
  search_scope: Entire exact record and matched owner rows; all 86 assertions; exact
    chemical identity, official product labels and bounded local provenance search.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact monohydrate structure
  outcome: supported
  summary: Native structure, formula, charge, three stereocentres, masses and checked
    full cross-references agree.
  target_ids:
  - CHEBI:3535
  evidence_ids:
  - native
  - chemistry
  - external-chemistry
  - gsrs
- assessment_id: definition
  area: identity
  topic: Circular hydrate definition
  outcome: concern
  summary: Water is the equimolar partner of cephalexin. Repeating hydrate as its
    own component contradicts the explicit formula.
  target_ids:
  - CHEBI:3535
  evidence_ids:
  - native
  - chebi
  - chemistry
  - parents
- assessment_id: grounding
  area: grounding
  topic: Broader parent, role and reference granularity
  outcome: supported
  summary: The hydrate parent and antibacterial-drug role fit the exact form; KEGG
    compound and drug mappings are separately typed. Beilstein and direct DrugBank
    content remain access-limited.
  target_ids:
  - CHEBI:3535
  evidence_ids:
  - parents
  - pubchem
  - kegg
  - label
- assessment_id: clinical
  area: evidence
  topic: Every FDA product assertion
  outcome: supported
  summary: All 86 product assertions match current official metadata, and GSRS confirms
    exact form. Source versions are preserved as historical provenance.
  target_ids:
  - CHEBI:3535
  evidence_ids:
  - owners
  - fda
  - fda-validation
  - gsrs
- assessment_id: material
  area: evidence
  topic: Formulation and active-moiety amounts
  outcome: supported
  summary: Official labels establish monohydrate use while distinguishing active-cephalexin
    dose equivalents. No original target-binding or exact hydrate-solid MIC is asserted.
  target_ids:
  - CHEBI:3535
  evidence_ids:
  - label
  - keflex
- assessment_id: optional
  area: completeness
  topic: Unpopulated target, resistance, producer and graph domains
  outcome: not_applicable
  summary: No optional omission is a defect. Regulatory microbiology prose is not
    silently converted to primary mechanistic or strain-level evidence.
  target_ids:
  - CHEBI:3535
  evidence_ids:
  - native
  - keflex
  - search
- assessment_id: provenance
  area: provenance
  topic: Source owners and history
  outcome: supported
  summary: All 15 captured inputs and six native history events remain intact; full
    record and source assertions were checked.
  target_ids:
  - CHEBI:3535
  evidence_ids:
  - owners
  - native
  - search
findings:
- finding_id: F1
  issue_key: chebi-3535-circular-hydrate-definition
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Definition names hydrate instead of water as the equimolar component
  description: The native definition says equimolar amounts of hydrate and cephalexin.
    The stored formula and two-component graph specify one water per cephalexin. Replace
    the circular component name with water through source-owned correction; preserve
    the correct structure.
  target_ids:
  - CHEBI:3535
  field_paths:
  - definition
  evidence_ids:
  - native
  - chebi
  - chemistry
  - parents
  rule_id: native-review-checklist:Identity and Equivalence
  native_severity: minor source-owned prose error
  normalization_reason: The exact identifier, graph, formula and clinical identity
    are coherent; the defect is a bounded incorrect component word in the definition.
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
actions:
- action_id: A1
  description: Correct the source-owned monohydrate definition to specify water and
    cephalexin in a 1:1 ratio.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:3535
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
  acceptance_checks:
  - Preserve CHEBI:3535, full monohydrate key, stereochemistry and all independently
    supported FDA assertions.
  - Use a maintained upstream or extraction/adjudication correction that survives
    reseeding.
  - Run schema, strict, provenance and corpus checks after separately authorized curation.
limitations:
- The full FDA comparison verifies the 86 asserted products, not completeness of the
  FDA product universe or future marketing status.
- Beilstein and direct DrugBank content were not independently inspected; other exact
  public chemical authorities and GSRS agree.
- No primary target experiment or strain-level MIC is inferred from product labels;
  no such native claim requires correction.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 15 captured input hashes remain unchanged. No native data, source inventory
  or scientific status changed.
- The current GSRS record version differs from the historically captured version;
  exact structure agrees, and this temporal difference is not itself a defect.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:3535
- https://gsrs.ncats.nih.gov/api/v1/substances/OBN7UDS42Y?view=full
tags:
- cephalexin-monohydrate
- FDA-product-assertions
- hydrate-definition
```
