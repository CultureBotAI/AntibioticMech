# Fraxetin: coherent chemical identity with species-specific antibacterial and antivirulence evidence

- Review: 20261021T170344Z-fraxetin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:45:53Z
- Finished UTC: 2026-10-21T17:03:44Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The entire fraxetin record is chemically consistent and supported as a hydroxycoumarin antibacterial. All adopted citations were assessed, although they mainly concern host/antioxidant biology. Exact-compound original studies supply bounded bacterial evidence and distinguish growth inhibition from antivirulence effects. No confirmed native corrective finding is identified. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position477; one exact record in path order. The thirteen original captured inputs remain unchanged; actual owner/readiness inputs were appended before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:5169 | data/antibiotics/antibacterial/fraxetin.yaml | generated | fraxetin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:5169 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:5169 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:5169 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:5169 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:5169 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:5169 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:5169 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:5169 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:5169 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:5169 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:5169 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:5169 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact compound and naming

identity: supported. Targets: CHEBI:5169.

Native graph, systematic name, CAS-associated material and independent chemical authorities agree; the two scaffold parents are appropriate. Source-only registry limitations remain explicit.

### Antibacterial classification with assay boundaries

evidence: supported. Targets: CHEBI:5169.

The2014 original provides direct bacterial physiological/biochemical evidence for exact fraxetin. The2024 S.agalactiae growth-negative result coexists with antivirulence effects and does not refute activity in other tested bacteria. No native numerical or target claim overstates either paper.

### Adopted citations and history

provenance: supported. Targets: CHEBI:5169.

All ten adopted abstracts and all four history events were assessed. The maintained ChEBI source and readiness owner were traced, and no optional primary mechanism object is required merely because additional papers exist.

### Optional mechanism and structured-source applicability

completeness: unknown. Targets: CHEBI:5169.

Native has no named gene/protein, pathway or expression dataset requiring a structured adapter. The newly inspected SrtA and DNA/topoisomerase experiments are potential future curation leads; causal specificity and taxon scope need separate adjudication before adding targets.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/fraxetin.yaml; Entire native YAML including all names, groundings, source concepts and chronological history | supports | The record is SEEDED, EXACT, and denotes C10H8O5 with full key HAVWRBANWNTOJX-UHFFFAOYSA-N. All 4 history events were read. No quantitative activity, molecular target, resistance object, causal graph or expression dataset is asserted. |
| owners | 477-source-rows.json; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Complete actual inventory and readiness rows, applicable extraction and emission ownership | supports | ChEBI supplies the exact native chemical graph, definition, names, parent/role assignments and its citation list. The seeder preserves source provenance and separates exact molecular links from drug and document associations. The readiness row is an unsigned evidence-worklist suggestion, not a saved scientific review. |
| search | 477-local-hits.txt; 477-owners-search.json; 048-root-fetch1-manifest.json through 048-root-fetch5-manifest.json; Ignored-inclusive local owner search and bounded current-authority/primary-publication follow-up | context_only | The initial capture and follow-up exact identifier/name searches included hidden and ignored local files. Public chemical authority entries, all adopted citation abstracts and the specifically identified original papers were read at the depths stated. Search misses and inaccessible endpoints are not proof of global absence. |
| chemistry | 048-root-authority-chemistry.json; 477478-knapsack-check.json; Independent native/current authority graph parsing with existing019 RDKit interpreter | supports | Native SMILES and InChI mutually reproduce the recorded formula, full key and neutral charge. Current ChEBI encodings agree. Current PubChem, KEGG C09265 and KNApSAcK C00002473 graphs independently reproduce HAVWRBANWNTOJX-UHFFFAOYSA-N. The native molecule is achiral and has the defined 7,8-dihydroxy-6-methoxycoumarin constitution. |
| authority | CHEBI:5169; exact parent and role API entries; Complete current compound, names, definition, parents and activity-role definitions | supports | The current ChEBI graph/definition/name types reproduce the native record. Hydroxycoumarin and aromatic ether parents match the scaffold; antimicrobial and antibacterial agent roles concern growth inhibition and do not assert clinical drug use. CAS574-84-5 is corroborated by KNApSAcK and original2024 reagent Methods. KEGG and KNApSAcK exact structures agree. Reaxys198796 and LINCSLSM3712 remain source-attributed accessions without independent registry inspection; a PubChem name lookup for LSM-3712 returned404, not a contrary identity. |
| gates | 477-focused-results.json; 477-chemistry.json; Actual focused schema, strict and chemistry outputs | supports | All focused checks exit0; the native graph is internally consistent. All expanded hashes are rechecked before finalization. Internal chemical validity cannot establish the meaning or exactness of an external cross-reference. |
| adopted | PMID:11456117,12860476,15120578,15904944,15996779,16394523,19721227,23788190,23806420,23994349; All ten complete indexed original abstracts and publication metadata | context_only | PM11456117 concerns fly stress/antioxidants;12860476,15120578,15904944 and15996779 concern neuronal/rotenone oxidative-injury models;16394523 concerns osteoblast BMP responses;19721227 reports isolated F.rhynchophylla compound and LDL/Nrf2 vascular effects;23788190 concerns breast-cell estrogen biology;23806420 diabetic-rat carbohydrate enzymes;23994349 CCl4 liver fibrosis. These support distinct chemistry/host contexts, not bacterial target binding or bacterial MICs. They are not promoted to full-text antimicrobial evidence. |
| primary2014 | PMID:25189268; DOI:10.3892/mmr.2014.2529; PMC4214354; Complete original main text, Methods, Results and Discussion | supports | The authors use99% commercial fraxetin, ethanol controls and S.aureus labelled ATCC26112. At0.05mg/mL they measure modest conductivity change, little extracellular nucleic-acid leakage, and reduced cellular protein/nucleic-acid signals. No standardized MIC is supplied. Relaxation assays use topoisomerase preparations extracted from S.aureus and show inhibition at0.05–0.08mg/mL; separate plasmid/UV/restriction assays support DNA interaction. These results support antibacterial context but do not prove selective direct binding to a particular purified bacterial protein. The paper’s abstract and body differ in percentage wording, so exact percent reductions are not normalized here. |
| primary2024 | PMID:38731341; DOI:10.3390/ani14091337; PMC11083127; Original Materials/Methods2.1–2.9, Results3.1–3.6 and Conclusions, plus complete abstract | supports | 98% commercial CAS574-84-5 fraxetin was tested against S.agalactiae PBSA0903. THB broth microdilution at37C16–18h gives MIC&gt;256µg/mL;4–32µg/mL does not alter growth. A recombinant truncated SrtAΔ82 FRET assay shows concentration-dependent catalytic inhibition, followed by reduced surface Srr1 staining, adhesion and a tilapia challenge benefit. This is a bounded antivirulence experiment, not positive growth inhibition of this strain, a solved binding structure, a universal antibacterial potency claim or clinical approval. Primary Methods specify oral gavage for fish; figure wording does not override that route. No fish mortality percentage is extracted because abstract/Results wording differs. |

## Limits And Additional Notes

- The ten adopted publications were read at complete abstract level, not all original full texts. The2014 main text was read completely; the2024 original was read in the specific full methods/results/conclusion sections stated, without raw-data reanalysis.
- No direct registry access was obtained for Reaxys or LINCS; the legacy LINCS identifier remains ChEBI-attributed. A failed public lookup is not evidence that the accession is wrong.
- The2014 strain designation is preserved as printed rather than silently corrected. Biochemical enzyme preparations, DNA interaction and bacterial physiology do not prove a single selective molecular binding mechanism.
- The2024 assay demonstrates no growth inhibition at its tested range and supports antivirulence context. It is not used as an MIC-positive observation or as evidence of treatment approval.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T170344Z-fraxetin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Fraxetin: coherent chemical identity with species-specific antibacterial and
  antivirulence evidence'
started_at: '2026-10-21T16:45:53Z'
finished_at: '2026-10-21T17:03:44Z'
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
summary: The entire fraxetin record is chemically consistent and supported as a hydroxycoumarin
  antibacterial. All adopted citations were assessed, although they mainly concern
  host/antioxidant biology. Exact-compound original studies supply bounded bacterial
  evidence and distinguish growth inhibition from antivirulence effects. No confirmed
  native corrective finding is identified. Scientific assessment retains the stated
  evidence limits; full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/fraxetin.yaml
    sha256: 318a1727a69d15f918d1de80822247f033a4acea839f8fde0a3c4e929cab006e
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
targets:
- target_id: CHEBI:5169
  path: data/antibiotics/antibacterial/fraxetin.yaml
  label: fraxetin
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
  selection: Initially uncovered queue position477; one exact record in path order.
    The thirteen original captured inputs remain unchanged; actual owner/readiness
    inputs were appended before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:5169
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:5169
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    477
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:5169
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/fraxetin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:5169
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/fraxetin.yaml --out /private/tmp/am-review-session/477-strict.tsv
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
  - CHEBI:5169
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
  - CHEBI:5169
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
  - CHEBI:5169
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
  - CHEBI:5169
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
  - CHEBI:5169
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
  - CHEBI:5169
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
  - CHEBI:5169
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
  - CHEBI:5169
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
  - CHEBI:5169
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/fraxetin.yaml
  locator: Entire native YAML including all names, groundings, source concepts and
    chronological history
  accessed_at: '2026-10-21T16:55:47Z'
  support: supports
  summary: The record is SEEDED, EXACT, and denotes C10H8O5 with full key HAVWRBANWNTOJX-UHFFFAOYSA-N.
    All 4 history events were read. No quantitative activity, molecular target, resistance
    object, causal graph or expression dataset is asserted.
- evidence_id: owners
  kind: record_content
  reference: 477-source-rows.json; scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  locator: Complete actual inventory and readiness rows, applicable extraction and
    emission ownership
  accessed_at: '2026-10-21T16:55:47Z'
  support: supports
  summary: ChEBI supplies the exact native chemical graph, definition, names, parent/role
    assignments and its citation list. The seeder preserves source provenance and
    separates exact molecular links from drug and document associations. The readiness
    row is an unsigned evidence-worklist suggestion, not a saved scientific review.
  snapshot_sha256: e75f9773c37befe4e12dc7427f3ae659c767e6030b1bead2e99da2b5938df983
- evidence_id: search
  kind: search
  reference: 477-local-hits.txt; 477-owners-search.json; 048-root-fetch1-manifest.json
    through 048-root-fetch5-manifest.json
  locator: Ignored-inclusive local owner search and bounded current-authority/primary-publication
    follow-up
  accessed_at: '2026-10-21T16:55:47Z'
  support: context_only
  summary: The initial capture and follow-up exact identifier/name searches included
    hidden and ignored local files. Public chemical authority entries, all adopted
    citation abstracts and the specifically identified original papers were read at
    the depths stated. Search misses and inaccessible endpoints are not proof of global
    absence.
  search_scope: 2026-10-21; rg --no-ignore --hidden exact record label/identifier
    across data, curation, conf, scripts and reports; Europe PMC adopted PMID lookup
    and TITLE_ABS:fraxetin first100 results, plus web exact compound and primary study
    queries.
  snapshot_sha256: e75f9773c37befe4e12dc7427f3ae659c767e6030b1bead2e99da2b5938df983
- evidence_id: chemistry
  kind: validation
  reference: 048-root-authority-chemistry.json; 477478-knapsack-check.json
  locator: Independent native/current authority graph parsing with existing019 RDKit
    interpreter
  accessed_at: '2026-10-21T16:55:47Z'
  support: supports
  summary: Native SMILES and InChI mutually reproduce the recorded formula, full key
    and neutral charge. Current ChEBI encodings agree. Current PubChem, KEGG C09265
    and KNApSAcK C00002473 graphs independently reproduce HAVWRBANWNTOJX-UHFFFAOYSA-N.
    The native molecule is achiral and has the defined 7,8-dihydroxy-6-methoxycoumarin
    constitution.
  snapshot_sha256: fe824fa5edc3ec374c65fdab2cc222b57b90f8cee88df20c83410bf37b9a2982
- evidence_id: authority
  kind: authority
  reference: CHEBI:5169; exact parent and role API entries
  locator: Complete current compound, names, definition, parents and activity-role
    definitions
  accessed_at: '2026-10-21T16:55:47Z'
  support: supports
  summary: The current ChEBI graph/definition/name types reproduce the native record.
    Hydroxycoumarin and aromatic ether parents match the scaffold; antimicrobial and
    antibacterial agent roles concern growth inhibition and do not assert clinical
    drug use. CAS574-84-5 is corroborated by KNApSAcK and original2024 reagent Methods.
    KEGG and KNApSAcK exact structures agree. Reaxys198796 and LINCSLSM3712 remain
    source-attributed accessions without independent registry inspection; a PubChem
    name lookup for LSM-3712 returned404, not a contrary identity.
  snapshot_sha256: d52c8bbd2832475cbafab0f735611826c0a236fc1c37064c18aaea915ce85b2d
- evidence_id: gates
  kind: validation
  reference: 477-focused-results.json; 477-chemistry.json
  locator: Actual focused schema, strict and chemistry outputs
  accessed_at: '2026-10-21T16:55:47Z'
  support: supports
  summary: All focused checks exit0; the native graph is internally consistent. All
    expanded hashes are rechecked before finalization. Internal chemical validity
    cannot establish the meaning or exactness of an external cross-reference.
  snapshot_sha256: e2e03047dc99ee7b665d48b3a54192dbf6470127038eacd426c05aec46285eee
- evidence_id: adopted
  kind: primary_source
  reference: PMID:11456117,12860476,15120578,15904944,15996779,16394523,19721227,23788190,23806420,23994349
  locator: All ten complete indexed original abstracts and publication metadata
  accessed_at: '2026-10-21T16:55:47Z'
  support: context_only
  summary: PM11456117 concerns fly stress/antioxidants;12860476,15120578,15904944
    and15996779 concern neuronal/rotenone oxidative-injury models;16394523 concerns
    osteoblast BMP responses;19721227 reports isolated F.rhynchophylla compound and
    LDL/Nrf2 vascular effects;23788190 concerns breast-cell estrogen biology;23806420
    diabetic-rat carbohydrate enzymes;23994349 CCl4 liver fibrosis. These support
    distinct chemistry/host contexts, not bacterial target binding or bacterial MICs.
    They are not promoted to full-text antimicrobial evidence.
  snapshot_sha256: 5e8acbb1908d60dbecac01ad6d828808cb3961ab6e332f4ac5d617567e467417
- evidence_id: primary2014
  kind: primary_source
  reference: PMID:25189268; DOI:10.3892/mmr.2014.2529; PMC4214354
  locator: Complete original main text, Methods, Results and Discussion
  accessed_at: '2026-10-21T16:55:47Z'
  support: supports
  summary: The authors use99% commercial fraxetin, ethanol controls and S.aureus labelled
    ATCC26112. At0.05mg/mL they measure modest conductivity change, little extracellular
    nucleic-acid leakage, and reduced cellular protein/nucleic-acid signals. No standardized
    MIC is supplied. Relaxation assays use topoisomerase preparations extracted from
    S.aureus and show inhibition at0.05–0.08mg/mL; separate plasmid/UV/restriction
    assays support DNA interaction. These results support antibacterial context but
    do not prove selective direct binding to a particular purified bacterial protein.
    The paper’s abstract and body differ in percentage wording, so exact percent reductions
    are not normalized here.
  snapshot_sha256: 5a888907a9d2382078243be795ed2fc0d9f46f71dee7bc005253550ce8b6f81f
- evidence_id: primary2024
  kind: primary_source
  reference: PMID:38731341; DOI:10.3390/ani14091337; PMC11083127
  locator: Original Materials/Methods2.1–2.9, Results3.1–3.6 and Conclusions, plus
    complete abstract
  accessed_at: '2026-10-21T16:55:47Z'
  support: supports
  summary: 98% commercial CAS574-84-5 fraxetin was tested against S.agalactiae PBSA0903.
    THB broth microdilution at37C16–18h gives MIC>256µg/mL;4–32µg/mL does not alter
    growth. A recombinant truncated SrtAΔ82 FRET assay shows concentration-dependent
    catalytic inhibition, followed by reduced surface Srr1 staining, adhesion and
    a tilapia challenge benefit. This is a bounded antivirulence experiment, not positive
    growth inhibition of this strain, a solved binding structure, a universal antibacterial
    potency claim or clinical approval. Primary Methods specify oral gavage for fish;
    figure wording does not override that route. No fish mortality percentage is extracted
    because abstract/Results wording differs.
  snapshot_sha256: 5264195c7886c7db5e15f391a6970812a2228be4a7b29c5a1222721904bfd367
assessments:
- assessment_id: identity
  area: identity
  topic: Exact compound and naming
  outcome: supported
  summary: Native graph, systematic name, CAS-associated material and independent
    chemical authorities agree; the two scaffold parents are appropriate. Source-only
    registry limitations remain explicit.
  target_ids:
  - CHEBI:5169
  evidence_ids:
  - native
  - chemistry
  - authority
- assessment_id: activity
  area: evidence
  topic: Antibacterial classification with assay boundaries
  outcome: supported
  summary: The2014 original provides direct bacterial physiological/biochemical evidence
    for exact fraxetin. The2024 S.agalactiae growth-negative result coexists with
    antivirulence effects and does not refute activity in other tested bacteria. No
    native numerical or target claim overstates either paper.
  target_ids:
  - CHEBI:5169
  evidence_ids:
  - primary2014
  - primary2024
  - authority
- assessment_id: provenance
  area: provenance
  topic: Adopted citations and history
  outcome: supported
  summary: All ten adopted abstracts and all four history events were assessed. The
    maintained ChEBI source and readiness owner were traced, and no optional primary
    mechanism object is required merely because additional papers exist.
  target_ids:
  - CHEBI:5169
  evidence_ids:
  - native
  - owners
  - adopted
  - gates
- assessment_id: mechanism
  area: completeness
  topic: Optional mechanism and structured-source applicability
  outcome: unknown
  summary: Native has no named gene/protein, pathway or expression dataset requiring
    a structured adapter. The newly inspected SrtA and DNA/topoisomerase experiments
    are potential future curation leads; causal specificity and taxon scope need separate
    adjudication before adding targets.
  target_ids:
  - CHEBI:5169
  evidence_ids:
  - native
  - primary2014
  - primary2024
findings: []
actions: []
limitations:
- The ten adopted publications were read at complete abstract level, not all original
  full texts. The2014 main text was read completely; the2024 original was read in
  the specific full methods/results/conclusion sections stated, without raw-data reanalysis.
- No direct registry access was obtained for Reaxys or LINCS; the legacy LINCS identifier
  remains ChEBI-attributed. A failed public lookup is not evidence that the accession
  is wrong.
- The2014 strain designation is preserved as printed rather than silently corrected.
  Biochemical enzyme preparations, DNA interaction and bacterial physiology do not
  prove a single selective molecular binding mechanism.
- The2024 assay demonstrates no growth inhibition at its tested range and supports
  antivirulence context. It is not used as an MIC-positive observation or as evidence
  of treatment approval.
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
