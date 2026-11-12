# Garenoxacin: consistent R-configured free base and bounded antibacterial-drug evidence

- Review: 20261021T172027Z-garenoxacin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:59:22Z
- Finished UTC: 2026-10-21T17:20:27Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The stored R-configured garenoxacin free base, names and structural classifications agree with current chemical authorities and original discovery literature. Clinical and microbiological studies support antibacterial-drug context with formulation and study-design limits. No confirmed native corrective finding is identified. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position489; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:131716 | data/antibiotics/antibacterial/garenoxacin.yaml | generated | garenoxacin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:131716 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:131716 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:131716 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:131716 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:131716 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:131716 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:131716 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:131716 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:131716 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:131716 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:131716 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:131716 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### R configuration and compound/form names

identity: supported. Targets: CHEBI:131716.

The native definition and independent graphs match R garenoxacin. Original discovery distinguishes that identity from the mesylate, preserving the exact-versus-drug association boundary.

### Antibacterial agent and drug roles

evidence: supported. Targets: CHEBI:131716.

Original microbiological, development and clinical studies establish actual antibacterial-drug context; no quantitative native efficacy or safety assertion overstates the evidence.

### Chemical and document association scope

grounding: supported. Targets: CHEBI:131716.

CAS is directly corroborated by discovery nomenclature. DrugCentral is a broader drug association; Reaxys exact registry inspection remains limited. The Wikipedia identifier denotes the matching subject and is not primary mechanistic evidence.

### All adopted leads and history

provenance: supported. Targets: CHEBI:131716.

All ten leads and all four history events were assessed. One lead has metadata only and one is explicitly a review; neither is represented as inspected original experimental full text.

### Optional molecular target and adapter applicability

completeness: unknown. Targets: CHEBI:131716.

There is no native named molecular target, gene, pathway or expression dataset requiring an adapter lookup. Clinical PK/PD and quinolone-class membership do not independently prove an exact bacterial binding mechanism. Optional mechanism curation needs direct enzyme/structural evidence.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/garenoxacin.yaml; Entire native YAML, every asserted field and chronological history | supports | The SEEDED, EXACT record denotes C23H20F2N2O4 and full key NJDRXTDGYFKORP-LLVKDONJSA-N. All 4 history events, names, parents, activity roles and exact/drug/document links were read. No quantitative activity observation, molecular-target object, resistance object, producer object or causal graph is asserted. |
| owners | 489-source-rows.json; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Complete exact maintained source row and actual source/configuration/extraction/emission ownership | supports | ChEBI supplies the native structure, definition, names, ontology and adopted citation leads. There is one ChEBI source concept. Exact chemical links, broader drug associations and document links have different schema semantics. Original thirteen hashes were preserved; actual additional owners were captured where applicable. |
| search | 489-local-hits.txt; 049-root-fetch1-manifest.json through 049-root-fetch7-manifest.json; Ignored-inclusive initial local search and bounded public chemical/primary-literature retrievals | context_only | The local target search included hidden and ignored files. Current chemical entries and adopted citation abstracts were inspected, with original full-text follow-up at the specifically stated depths. Unsuccessful endpoints are access limits, not proof of absence. |
| chemistry | 049-root-authority-chemistry.json; Independent native and current-authority forward graph parsing with existing019 RDKit interpreter | supports | Six independently parsed native, ChEBI and name-resolved PubChem encodings reproduce neutral C23H20F2N2O4, NJDRXTDGYFKORP-LLVKDONJSA-N and the one assigned R centre. The definition matches the substituent positions and does not equate the free base with its mesylate. |
| gates | 489-focused-results.json; 489-chemistry.json; Actual chemistry, schema and strict outputs | supports | Focused checks all exit0. Independent formula, charge, masses, full key and source mint are internally consistent. These checks do not establish the truth of every external-source assertion. |
| authority | CHEBI:131716; CHEBI:24897,26512,35618,37143,51454,86324; drugcentral:4053; Complete current chemical, parent/role and public DrugCentral entries | supports | Isoindole, quinolinemonocarboxylic acid, aromatic ether, organofluorine, cyclopropane and quinolone-antibiotic classifications fit. DrugCentral4053 resolves to garenoxacin with CAS194804-75-6 and C23H20F2N2O4, while aggregating mesylate/hydrate names; the native drug_xrefs field allows this broader association. It is not used as an exact salt-equivalence assertion or source of current prescribing guidance. Reaxys8878492 remains source-attributed; Wikipedia is a document association. |
| adopted | PMID:11711258,11892932,12572531,21762685,21796376,22088660,25327090,25989991,26097813,26349115; All ten indexed citation records: nine complete available abstracts and one metadata-only drug profile | supports | 11711258 tests137 N.gonorrhoeae isolates and reports method-dependent MICs;11892932 is a2002 review/drug-development profile, not current trial status;12572531 is original synthesis/activity;21762685 tests host A549/THP-1 inflammatory signaling;21796376 is clinical PK/PD;22088660 studies pneumococcal mutants in an in-vitro PK model;25327090 has no abstract;25989991 is retrospective AML prophylaxis;26097813 is observational Indian postmarketing surveillance;26349115 is renal-impairment PK. Host signaling, safety and PK observations are not direct antibacterial target evidence. Observational comparisons and absence of selected resistance in one model are not universal efficacy or resistance claims. |
| discovery | PMID:12572531; DOI:10.1055/s-0031-1299988; Complete original2003 indexed abstract | supports | The paper identifies the R enantiomer5b as T-3811/garenoxacin, CAS194804-75-6, and distinguishes T-3811ME mesylate CAS223652-90-2. The R compound is two- to fourfold more active than S against most tested organisms, with similar activity against S.pneumoniae and H.influenzae. The native R graph and free-base identity therefore agree with direct discovery nomenclature. The publisher full-text endpoint returned a challenge page and was not treated as full text. |
| clinical | PMID:21796376; DOI:10.1007/s00228-011-1095-3; PMC3249185; Original Introduction, selected Methods and complete Results/Discussion, including Tables4–7 | supports | The analysis pools five Japanese phaseI–III studies from1999–2005. The chronic-respiratory-infection phaseIII study was open and single-arm;136 participants received400mg for10days,133 entered PK analysis and66 with identified organisms/MICs entered PK/PD efficacy analysis. Efficacy was56/61 above free AUC/MIC30 and2/5 at or below30. These are study-specific exposure-response observations, not a randomized treatment comparison, a purified target assay or a present-day dose recommendation. Clinical microbiology used stated Japanese/CLSI methods with different medium/dilution contexts. No clinical formulation is silently made identical to the isolated free base. |

## Limits And Additional Notes

- All ten adopted records were assessed; nine abstracts were available and PMID25327090 was metadata only. PMID11892932 is a historical review. The original discovery publisher page was a challenge, so its detailed synthetic experiments were not read.
- The2011 clinical original was read in the specifically named sections; not every Methods subsection was fully inspected. Raw patient-level data and supplementary datasets were not reanalyzed.
- Reaxys was not directly inspected. DrugCentral aggregates related pharmaceutical forms under a drug-level association; this review makes no current approval, dosing or product-safety recommendation.
- The des-fluoro description concerns absence of the usual position6 fluorine and does not mean the difluoromethoxy-containing molecule lacks fluorine altogether.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T172027Z-garenoxacin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Garenoxacin: consistent R-configured free base and bounded antibacterial-drug
  evidence'
started_at: '2026-10-21T16:59:22Z'
finished_at: '2026-10-21T17:20:27Z'
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
summary: The stored R-configured garenoxacin free base, names and structural classifications
  agree with current chemical authorities and original discovery literature. Clinical
  and microbiological studies support antibacterial-drug context with formulation
  and study-design limits. No confirmed native corrective finding is identified. Scientific
  assessment retains the stated evidence limits; full verification is blocked by the
  shared native-library failure.
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
  - path: data/antibiotics/antibacterial/garenoxacin.yaml
    sha256: 6865390d76b965ae2a568741a643f4b2e4f940396f07a6085b680a69c8f979ab
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
- target_id: CHEBI:131716
  path: data/antibiotics/antibacterial/garenoxacin.yaml
  label: garenoxacin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI identity, structure, ontology, xrefs and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI and ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated native field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusion decisions
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position489; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:131716
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:131716
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    489
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:131716
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/garenoxacin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:131716
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/garenoxacin.yaml --out /private/tmp/am-review-session/489-strict.tsv
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
  - CHEBI:131716
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
  - CHEBI:131716
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
  - CHEBI:131716
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
  - CHEBI:131716
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
  - CHEBI:131716
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
  - CHEBI:131716
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
  - CHEBI:131716
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
  - CHEBI:131716
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
  - CHEBI:131716
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/garenoxacin.yaml
  locator: Entire native YAML, every asserted field and chronological history
  accessed_at: '2026-10-21T17:14:10Z'
  support: supports
  summary: The SEEDED, EXACT record denotes C23H20F2N2O4 and full key NJDRXTDGYFKORP-LLVKDONJSA-N.
    All 4 history events, names, parents, activity roles and exact/drug/document links
    were read. No quantitative activity observation, molecular-target object, resistance
    object, producer object or causal graph is asserted.
- evidence_id: owners
  kind: record_content
  reference: 489-source-rows.json; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Complete exact maintained source row and actual source/configuration/extraction/emission
    ownership
  accessed_at: '2026-10-21T17:14:10Z'
  support: supports
  summary: ChEBI supplies the native structure, definition, names, ontology and adopted
    citation leads. There is one ChEBI source concept. Exact chemical links, broader
    drug associations and document links have different schema semantics. Original
    thirteen hashes were preserved; actual additional owners were captured where applicable.
  snapshot_sha256: 508145cff0fe337f3c8055108c8c97d1bc926063da43d0ac7431af482d73a52e
- evidence_id: search
  kind: search
  reference: 489-local-hits.txt; 049-root-fetch1-manifest.json through 049-root-fetch7-manifest.json
  locator: Ignored-inclusive initial local search and bounded public chemical/primary-literature
    retrievals
  accessed_at: '2026-10-21T17:14:10Z'
  support: context_only
  summary: The local target search included hidden and ignored files. Current chemical
    entries and adopted citation abstracts were inspected, with original full-text
    follow-up at the specifically stated depths. Unsuccessful endpoints are access
    limits, not proof of absence.
  search_scope: 2026-10-21; rg --no-ignore --hidden in own049 checkout; current ChEBI,
    PubChem and asserted public authority lookups; Europe PMC exact adopted PMID and
    TITLE_ABS:garenoxacin searches; bounded exact-compound original-paper follow-up.
  snapshot_sha256: cb81a494c7559c87bccf5cfdfed5361bde0c19dd35cc8828da97afe4c862c2eb
- evidence_id: chemistry
  kind: validation
  reference: 049-root-authority-chemistry.json
  locator: Independent native and current-authority forward graph parsing with existing019
    RDKit interpreter
  accessed_at: '2026-10-21T17:14:10Z'
  support: supports
  summary: Six independently parsed native, ChEBI and name-resolved PubChem encodings
    reproduce neutral C23H20F2N2O4, NJDRXTDGYFKORP-LLVKDONJSA-N and the one assigned
    R centre. The definition matches the substituent positions and does not equate
    the free base with its mesylate.
  snapshot_sha256: 708b390e6a3a9b13adf021f4f7291c2bf9623e2db88a5b188c1c6d9533361d36
- evidence_id: gates
  kind: validation
  reference: 489-focused-results.json; 489-chemistry.json
  locator: Actual chemistry, schema and strict outputs
  accessed_at: '2026-10-21T17:14:10Z'
  support: supports
  summary: Focused checks all exit0. Independent formula, charge, masses, full key
    and source mint are internally consistent. These checks do not establish the truth
    of every external-source assertion.
  snapshot_sha256: 14dec4e7b7ad3fd049124af04d71802922eb67859691493ee074205c82cb5f5a
- evidence_id: authority
  kind: authority
  reference: CHEBI:131716; CHEBI:24897,26512,35618,37143,51454,86324; drugcentral:4053
  locator: Complete current chemical, parent/role and public DrugCentral entries
  accessed_at: '2026-10-21T17:14:10Z'
  support: supports
  summary: Isoindole, quinolinemonocarboxylic acid, aromatic ether, organofluorine,
    cyclopropane and quinolone-antibiotic classifications fit. DrugCentral4053 resolves
    to garenoxacin with CAS194804-75-6 and C23H20F2N2O4, while aggregating mesylate/hydrate
    names; the native drug_xrefs field allows this broader association. It is not
    used as an exact salt-equivalence assertion or source of current prescribing guidance.
    Reaxys8878492 remains source-attributed; Wikipedia is a document association.
  snapshot_sha256: c1b8bf42a3845f80cbf857699fbfd82d0bd0505f0e03b773646acaf0cb8d5554
- evidence_id: adopted
  kind: primary_source
  reference: PMID:11711258,11892932,12572531,21762685,21796376,22088660,25327090,25989991,26097813,26349115
  locator: 'All ten indexed citation records: nine complete available abstracts and
    one metadata-only drug profile'
  accessed_at: '2026-10-21T17:14:10Z'
  support: supports
  summary: 11711258 tests137 N.gonorrhoeae isolates and reports method-dependent MICs;11892932
    is a2002 review/drug-development profile, not current trial status;12572531 is
    original synthesis/activity;21762685 tests host A549/THP-1 inflammatory signaling;21796376
    is clinical PK/PD;22088660 studies pneumococcal mutants in an in-vitro PK model;25327090
    has no abstract;25989991 is retrospective AML prophylaxis;26097813 is observational
    Indian postmarketing surveillance;26349115 is renal-impairment PK. Host signaling,
    safety and PK observations are not direct antibacterial target evidence. Observational
    comparisons and absence of selected resistance in one model are not universal
    efficacy or resistance claims.
  snapshot_sha256: 6c8811f8fe0b5b5bf401cee044049b6508659b890da102fb21baf570abebbceb
- evidence_id: discovery
  kind: primary_source
  reference: PMID:12572531; DOI:10.1055/s-0031-1299988
  locator: Complete original2003 indexed abstract
  accessed_at: '2026-10-21T17:14:10Z'
  support: supports
  summary: The paper identifies the R enantiomer5b as T-3811/garenoxacin, CAS194804-75-6,
    and distinguishes T-3811ME mesylate CAS223652-90-2. The R compound is two- to
    fourfold more active than S against most tested organisms, with similar activity
    against S.pneumoniae and H.influenzae. The native R graph and free-base identity
    therefore agree with direct discovery nomenclature. The publisher full-text endpoint
    returned a challenge page and was not treated as full text.
  snapshot_sha256: 6c8811f8fe0b5b5bf401cee044049b6508659b890da102fb21baf570abebbceb
- evidence_id: clinical
  kind: primary_source
  reference: PMID:21796376; DOI:10.1007/s00228-011-1095-3; PMC3249185
  locator: Original Introduction, selected Methods and complete Results/Discussion,
    including Tables4–7
  accessed_at: '2026-10-21T17:14:10Z'
  support: supports
  summary: The analysis pools five Japanese phaseI–III studies from1999–2005. The
    chronic-respiratory-infection phaseIII study was open and single-arm;136 participants
    received400mg for10days,133 entered PK analysis and66 with identified organisms/MICs
    entered PK/PD efficacy analysis. Efficacy was56/61 above free AUC/MIC30 and2/5
    at or below30. These are study-specific exposure-response observations, not a
    randomized treatment comparison, a purified target assay or a present-day dose
    recommendation. Clinical microbiology used stated Japanese/CLSI methods with different
    medium/dilution contexts. No clinical formulation is silently made identical to
    the isolated free base.
  snapshot_sha256: 8093140875b62bb8ea2ec603cb050cbbd48e7f404769d2bf23ca786298a649f7
assessments:
- assessment_id: identity
  area: identity
  topic: R configuration and compound/form names
  outcome: supported
  summary: The native definition and independent graphs match R garenoxacin. Original
    discovery distinguishes that identity from the mesylate, preserving the exact-versus-drug
    association boundary.
  target_ids:
  - CHEBI:131716
  evidence_ids:
  - native
  - chemistry
  - discovery
  - authority
- assessment_id: activity
  area: evidence
  topic: Antibacterial agent and drug roles
  outcome: supported
  summary: Original microbiological, development and clinical studies establish actual
    antibacterial-drug context; no quantitative native efficacy or safety assertion
    overstates the evidence.
  target_ids:
  - CHEBI:131716
  evidence_ids:
  - adopted
  - clinical
  - discovery
- assessment_id: grounding
  area: grounding
  topic: Chemical and document association scope
  outcome: supported
  summary: CAS is directly corroborated by discovery nomenclature. DrugCentral is
    a broader drug association; Reaxys exact registry inspection remains limited.
    The Wikipedia identifier denotes the matching subject and is not primary mechanistic
    evidence.
  target_ids:
  - CHEBI:131716
  evidence_ids:
  - authority
  - discovery
  - search
- assessment_id: provenance
  area: provenance
  topic: All adopted leads and history
  outcome: supported
  summary: All ten leads and all four history events were assessed. One lead has metadata
    only and one is explicitly a review; neither is represented as inspected original
    experimental full text.
  target_ids:
  - CHEBI:131716
  evidence_ids:
  - native
  - owners
  - adopted
  - gates
- assessment_id: completeness
  area: completeness
  topic: Optional molecular target and adapter applicability
  outcome: unknown
  summary: There is no native named molecular target, gene, pathway or expression
    dataset requiring an adapter lookup. Clinical PK/PD and quinolone-class membership
    do not independently prove an exact bacterial binding mechanism. Optional mechanism
    curation needs direct enzyme/structural evidence.
  target_ids:
  - CHEBI:131716
  evidence_ids:
  - native
  - clinical
  - adopted
findings: []
actions: []
limitations:
- All ten adopted records were assessed; nine abstracts were available and PMID25327090
  was metadata only. PMID11892932 is a historical review. The original discovery publisher
  page was a challenge, so its detailed synthetic experiments were not read.
- The2011 clinical original was read in the specifically named sections; not every
  Methods subsection was fully inspected. Raw patient-level data and supplementary
  datasets were not reanalyzed.
- Reaxys was not directly inspected. DrugCentral aggregates related pharmaceutical
  forms under a drug-level association; this review makes no current approval, dosing
  or product-safety recommendation.
- The des-fluoro description concerns absence of the usual position6 fluorine and
  does not mean the difluoromethoxy-containing molecule lacks fluorine altogether.
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
