# Source-owned qualifications for three CARD assertions

- Review: 20261015T134842Z-card-evidence-qualifications
- Repository: culturebotai/AntibioticMech
- Started UTC: 2026-10-15T13:34:44Z
- Finished UTC: 2026-10-15T13:48:42Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Three source-owned notes now preserve known scope limitations. Two major findings remain open; no whole-record signoff or experimental identity promotion.

## Scope And Provenance

Three CARD assertions in three complete records; note-only changes and prior finding follow-up, not whole-record review.

Selection: All records affected by the prior mcr43-context and eatav-compound findings.
Coverage: partial; 3 reviewed / 2939 in the declared population.
Source: working_tree at Git base 8f0dc555d7b4b683610fae7945f22bd6e9fb5105.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:59064 | data/antibiotics/antibacterial/colistin-a.yaml | generated | colistin A |
| CHEBI:59673 | data/antibiotics/antibacterial/colistin-b.yaml | generated | colistin B |
| CHEBI:8269 | data/antibiotics/antibacterial/pleuromutilin.yaml | generated | pleuromutilin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused regression suite | passed | True | CHEBI:8269, CHEBI:59064, CHEBI:59673 | 509 passed, 3 skipped. Skips are historical live replays after corpus changes; immutable public-artifact checks still pass. The initial run found two historical/live coupling failures, fixed before this complete rerun. |
| Closed-schema corpus validation | passed | True | CHEBI:8269, CHEBI:59064, CHEBI:59673 | 2939 records scanned, zero errors. |
| Whole-corpus source reproduction | passed | True | CHEBI:8269, CHEBI:59064, CHEBI:59673 | 2939 expected and present; zero missing, unexpected or drifted records; no lockfile discrepancies. |
| Repeat seeding is byte-stable | passed | True | CHEBI:8269, CHEBI:59064, CHEBI:59673 | After the dry run, inspected single-record canary and two-record apply, repeat seeding wrote zero records; all three were already current. |
| Generated site consistency | passed | True | CHEBI:8269, CHEBI:59064, CHEBI:59673 | After regeneration, all 2939 compound pages and seven classes match a clean render. Only three compound pages changed. |
| Protected files, note-only deltas and rendered text | passed | True | CHEBI:8269, CHEBI:59064, CHEBI:59673 | Read-only changes() audit in /private/tmp/card_qualification_review_20261015.py checked 7798 baseline files and all 2939 record paths. Exactly three record notes and one history event per record changed; 2936 records, source inventories, embedding files and all earlier report bytes were preserved. Embedding documents are unchanged; each rendered page contains the full qualification. |
| Raw source integrity | passed | True | CHEBI:8269, CHEBI:59064, CHEBI:59673 | 14 inventories and 23 upstream files retain valid provenance. |
| Source adoption gates | passed | True | CHEBI:8269, CHEBI:59064, CHEBI:59673 | 37 sources checked; adoption and deferral states unchanged. |
| Generated statistics | passed | True | CHEBI:8269, CHEBI:59064, CHEBI:59673 | README statistics are current. |
| Repository lint | passed | True | CHEBI:8269, CHEBI:59064, CHEBI:59673 | Repository lint passed; the four new or modified focused Python files also passed format checks, and git diff --check passed. |
| Authoritative QC | failed | True | CHEBI:8269, CHEBI:59064, CHEBI:59673 | uv cannot start the runner: locked rdkit==2026.3.5 has no source distribution or wheel for this Intel macOS platform. Available separate checks do not constitute full QC. |
| Complete primary and exact experimental grounding | unavailable | True | CHEBI:8269, CHEBI:59064, CHEBI:59673 | Figure/supplement review, reconciliation of functional contexts, and exact-compound experimental identities remain incomplete. No whole-record signoff. |

## Scientific And Domain Assessments

### Source-owned note-only curation

provenance: supported. Targets: CHEBI:8269, CHEBI:59064, CHEBI:59673.

All three complete records retain chemical identity, CARD ownership, original assertions and unrelated fields; one note and history event change per record.

### Exact experimental and compound scope

grounding: concern. Targets: CHEBI:8269, CHEBI:59064, CHEBI:59673.

Qualifications mitigate presentation gaps but do not assign an experimental protein, allele, taxon, genome or AST observation.

## Findings

### mcr43-context: Contrasting functional contexts and component-specific grounding remain unresolved

major / open / confirmed; issue key: card-protein-name-mcr43-context.

The missing qualification is now present, including later contrasting evidence. Reconciliation of tested contexts and evidence for purified colistin A and B remain open; the source assertion has not been promoted to an experiment.

### eatav-compound: Tested derivative does not ground the parent compound

major / open / confirmed; issue key: card-protein-name-eatav-compound.

The derivative-versus-parent limitation is now explicit. The inherited database assertion still lacks exact-parent experimental support; no allele or organism assignment is inferred.

## Recommended Actions And Acceptance Checks

### continue-mcr43-context

Resolve the remaining primary-evidence and exact-compound scope before experimental grounding or finding closure.

- Preserve both conflicting contexts and the exact structure boundary.
- Do not infer experimental accession, host or phenotype from reference identity.
- Complete authoritative QC on a supported platform before publication.

### continue-eatav-compound

Resolve the remaining primary-evidence and exact-compound scope before experimental grounding or finding closure.

- Preserve both conflicting contexts and the exact structure boundary.
- Do not infer experimental accession, host or phenotype from reference identity.
- Complete authoritative QC on a supported platform before publication.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| qualification-input | curation/card_evidence_reviews.json | supports | Two scoped decisions qualify three source assertions without changing their evidence, mechanism or experimental identity fields. |
| prior-context | reviews/structured/20261015T131237Z-card-protein-name-primary-context/review.yaml | context_only | Historical scoped primary assessments and their limitations remain intact; only two major findings are revisited. |
| later-mcr-context | https://doi.org/10.1093/jac/dkz413; Results and discussion: functional and lipid A results; Conclusions | context_only | Publisher primary HTML supplies contrasting functional evidence; it does not resolve every tested context or purified-component scope. Figures and supplements were not reviewed. |

## Limits And Additional Notes

- Full authoritative QC cannot start on Intel macOS with the locked RDKit distribution; available separate checks are not a full pass.
- Primary figures and supplements were not reviewed; no full source reconciliation or exact-component experimental assertion.
- No NCBI requests, source adoption, outreach, GitHub mutations or reuse-terms review. Issue #1040 remains deferred.
- No operational sequences, variants, constructs, primers, protocols or coordinates are exported.
- The full-corpus goal remains open and the prior reference index remains a historical snapshot.
- Evidence access time marks final inspection of the available text, not an underlying HTTP fetch timestamp.
- Regression tests: 509 passed; 3 explicitly skipped historical live replays.
- Protected pre-write baseline: 7798 files; three record deltas checked.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T134842Z-card-evidence-qualifications
kind: batch
repository: culturebotai/AntibioticMech
title: Source-owned qualifications for three CARD assertions
started_at: '2026-10-15T13:34:44Z'
finished_at: '2026-10-15T13:48:42Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same agent implemented and adversarially checked the bounded
    change; no independent reviewer or subagent.
skill: antibioticmech-research-resistance-genes
completion: partial
verdict: needs_curation
scientific_review: true
summary: Three source-owned notes now preserve known scope limitations. Two major
  findings remain open; no whole-record signoff or experimental identity promotion.
source:
  git_revision: 8f0dc555d7b4b683610fae7945f22bd6e9fb5105
  state: working_tree
  inputs:
  - path: curation/card_evidence_reviews.json
    sha256: 289d45797f11d85fc535a61991f0f559b83cd307625c4df31aab52f865a8b71e
    role: context
  - path: curation/source_queue.tsv
    sha256: 32ff6b625b7787e8935d6f1ec7195d2ba61fda714a664ee1b54049ebc2bd9fdb
    role: context
  - path: data/antibiotics/antibacterial/colistin-a.yaml
    sha256: 2b8020dd24bb1b98b69d0b5286ee979baa65c123be1bf2cf3344a034049f74cd
    role: target
  - path: data/antibiotics/antibacterial/colistin-b.yaml
    sha256: 6a7050a96a3bd4403760cefc7a1c502bd67b4a235790a6c9bff98fcd9053e10c
    role: target
  - path: data/antibiotics/antibacterial/pleuromutilin.yaml
    sha256: 3c9726dea285943c9a78252cee6a0be456df57723036ed5aa86e08c2b9219578
    role: target
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: docs/CURATION.md
    sha256: 1b16f856f63b074850d01a3e8111bda96aca891d8cd3b624ad411bcb1007cdf7
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: research/2026-10-15-card-protein-name-evidence-assessments.json
    sha256: ed5215a715ed801e290f7468e996f00d6ac7eea71a04762c29ccdaa7cff6f61c
    role: context
  - path: reviews/structured/20261015T131237Z-card-protein-name-primary-context/review.yaml
    sha256: a1b31734590804cbb2e399cf36f7f5f0935eb44511088ebdd6af1f2f7b0d0463
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: 92f0d5c495567fe1121c6c4044334e9558d6c3058daf215e7d5f8b9ee18a594d
    role: context
  - path: scripts/seed_from_sources.py
    sha256: be66eca74d22a3daa9ac6ff73d437c6c56e8d85b97f6877fdf3de77e2ab64680
    role: context
  - path: src/antibioticmech/schema/antibioticmech.yaml
    sha256: 27b01b64fc0c92f279964260b3c298a2769d185628fd28ce532074c9cef649eb
    role: context
  - path: tests/test_aph_ant_aad_mph_gaps.py
    sha256: d8769f52732601dcf8fecbfb6cfde260b28f19ef76d30d0e4c5534d941560fe6
    role: context
  - path: tests/test_card_evidence_reviews.py
    sha256: 89ba70eb307ed50c62f14209266e4565bb73b4bdb78380f89c5425a71f408a4d
    role: context
  - path: tests/test_card_protein_name_screen.py
    sha256: c9ee773f0b82de5396e118168466dafb6681362d3d52cfa8ffc87142575acda3
    role: context
targets:
- kind: generated
  label: colistin A
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Unchanged upstream assertions; do not hand-edit
  - repository: culturebotai/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Pinned evidence-scope qualifications
  - repository: culturebotai/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Closed qualification validation and note-only projection
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Validated, history-preserving source-owned emission
  path: data/antibiotics/antibacterial/colistin-a.yaml
  record_class: AntibioticRecord
  target_id: CHEBI:59064
- kind: generated
  label: colistin B
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Unchanged upstream assertions; do not hand-edit
  - repository: culturebotai/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Pinned evidence-scope qualifications
  - repository: culturebotai/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Closed qualification validation and note-only projection
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Validated, history-preserving source-owned emission
  path: data/antibiotics/antibacterial/colistin-b.yaml
  record_class: AntibioticRecord
  target_id: CHEBI:59673
- kind: generated
  label: pleuromutilin
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Unchanged upstream assertions; do not hand-edit
  - repository: culturebotai/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Pinned evidence-scope qualifications
  - repository: culturebotai/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Closed qualification validation and note-only projection
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Validated, history-preserving source-owned emission
  path: data/antibiotics/antibacterial/pleuromutilin.yaml
  record_class: AntibioticRecord
  target_id: CHEBI:8269
scope:
  description: Three CARD assertions in three complete records; note-only changes
    and prior finding follow-up, not whole-record review.
  selection: All records affected by the prior mcr43-context and eatav-compound findings.
  coverage: partial
  population_size: 2939
  reviewed_target_ids:
  - CHEBI:8269
  - CHEBI:59064
  - CHEBI:59673
  exclusions:
  - target: Other claims and remaining 2936 records
    reason: Not scientifically reassessed; raw inventory and unrelated record bytes
      preserved.
  - target: Prior msrC and ddl findings
    reason: Remain open and are not superseded by this review.
checks:
- check_id: regression
  name: Focused regression suite
  required: true
  status: passed
  command: .venv/bin/python -m pytest -q tests/test_card_evidence_reviews.py tests/test_seed_harmonization.py
    tests/test_phibase_grounding_reviews.py tests/test_write_validated.py tests/test_card_protein_name_screen.py
    tests/test_card_protein_name_evidence.py tests/test_card_aac6_memberships.py tests/test_card_aph_memberships.py
    tests/test_aph_ant_aad_mph_gaps.py tests/test_aac34_followup.py --junitxml=reports/card-evidence-qualifications-2026-10-15/regression-final.xml
  exit_code: 0
  summary: 509 passed, 3 skipped. Skips are historical live replays after corpus changes;
    immutable public-artifact checks still pass. The initial run found two historical/live
    coupling failures, fixed before this complete rerun.
  target_ids:
  - CHEBI:8269
  - CHEBI:59064
  - CHEBI:59673
- check_id: schema
  name: Closed-schema corpus validation
  required: true
  status: passed
  command: .venv/bin/python scripts/validate_strict.py --quiet --workers 2 --out reports/card-evidence-qualifications-2026-10-15/validation.tsv
  exit_code: 0
  summary: 2939 records scanned, zero errors.
  target_ids:
  - CHEBI:8269
  - CHEBI:59064
  - CHEBI:59673
- check_id: reproduction
  name: Whole-corpus source reproduction
  required: true
  status: passed
  command: .venv/bin/python scripts/verify_corpus.py
  exit_code: 0
  summary: 2939 expected and present; zero missing, unexpected or drifted records;
    no lockfile discrepancies.
  target_ids:
  - CHEBI:8269
  - CHEBI:59064
  - CHEBI:59673
- check_id: no-op-reseed
  name: Repeat seeding is byte-stable
  required: true
  status: passed
  command: .venv/bin/python scripts/seed_from_sources.py --apply --only CHEBI:8269
    CHEBI:59064 CHEBI:59673
  exit_code: 0
  summary: After the dry run, inspected single-record canary and two-record apply,
    repeat seeding wrote zero records; all three were already current.
  target_ids:
  - CHEBI:8269
  - CHEBI:59064
  - CHEBI:59673
- check_id: site
  name: Generated site consistency
  required: true
  status: passed
  command: .venv/bin/python scripts/render_pages.py --check
  exit_code: 0
  summary: After regeneration, all 2939 compound pages and seven classes match a clean
    render. Only three compound pages changed.
  target_ids:
  - CHEBI:8269
  - CHEBI:59064
  - CHEBI:59673
- check_id: preservation
  name: Protected files, note-only deltas and rendered text
  required: true
  status: passed
  summary: Read-only changes() audit in /private/tmp/card_qualification_review_20261015.py
    checked 7798 baseline files and all 2939 record paths. Exactly three record notes
    and one history event per record changed; 2936 records, source inventories, embedding
    files and all earlier report bytes were preserved. Embedding documents are unchanged;
    each rendered page contains the full qualification.
  target_ids:
  - CHEBI:8269
  - CHEBI:59064
  - CHEBI:59673
- check_id: provenance
  name: Raw source integrity
  required: true
  status: passed
  command: .venv/bin/python scripts/check_provenance.py
  exit_code: 0
  summary: 14 inventories and 23 upstream files retain valid provenance.
  target_ids:
  - CHEBI:8269
  - CHEBI:59064
  - CHEBI:59673
- check_id: source-queue
  name: Source adoption gates
  required: true
  status: passed
  command: .venv/bin/python scripts/check_source_queue.py
  exit_code: 0
  summary: 37 sources checked; adoption and deferral states unchanged.
  target_ids:
  - CHEBI:8269
  - CHEBI:59064
  - CHEBI:59673
- check_id: documentation
  name: Generated statistics
  required: true
  status: passed
  command: .venv/bin/python scripts/check_docs.py --check
  exit_code: 0
  summary: README statistics are current.
  target_ids:
  - CHEBI:8269
  - CHEBI:59064
  - CHEBI:59673
- check_id: lint
  name: Repository lint
  required: true
  status: passed
  command: .venv/bin/ruff check .
  exit_code: 0
  summary: Repository lint passed; the four new or modified focused Python files also
    passed format checks, and git diff --check passed.
  target_ids:
  - CHEBI:8269
  - CHEBI:59064
  - CHEBI:59673
- check_id: full-qc
  name: Authoritative QC
  required: true
  status: failed
  command: just qc
  exit_code: 2
  summary: 'uv cannot start the runner: locked rdkit==2026.3.5 has no source distribution
    or wheel for this Intel macOS platform. Available separate checks do not constitute
    full QC.'
  target_ids:
  - CHEBI:8269
  - CHEBI:59064
  - CHEBI:59673
- check_id: primary-grounding
  name: Complete primary and exact experimental grounding
  required: true
  status: unavailable
  summary: Figure/supplement review, reconciliation of functional contexts, and exact-compound
    experimental identities remain incomplete. No whole-record signoff.
  target_ids:
  - CHEBI:8269
  - CHEBI:59064
  - CHEBI:59673
evidence:
- evidence_id: qualification-input
  kind: record_content
  reference: curation/card_evidence_reviews.json
  accessed_at: '2026-10-15T13:48:42Z'
  support: supports
  snapshot_sha256: 289d45797f11d85fc535a61991f0f559b83cd307625c4df31aab52f865a8b71e
  summary: Two scoped decisions qualify three source assertions without changing their
    evidence, mechanism or experimental identity fields.
- evidence_id: prior-context
  kind: record_content
  reference: reviews/structured/20261015T131237Z-card-protein-name-primary-context/review.yaml
  accessed_at: '2026-10-15T13:48:42Z'
  support: context_only
  snapshot_sha256: a1b31734590804cbb2e399cf36f7f5f0935eb44511088ebdd6af1f2f7b0d0463
  summary: Historical scoped primary assessments and their limitations remain intact;
    only two major findings are revisited.
- evidence_id: later-mcr-context
  kind: primary_source
  reference: https://doi.org/10.1093/jac/dkz413
  locator: 'Results and discussion: functional and lipid A results; Conclusions'
  accessed_at: '2026-10-15T13:48:42Z'
  support: context_only
  summary: Publisher primary HTML supplies contrasting functional evidence; it does
    not resolve every tested context or purified-component scope. Figures and supplements
    were not reviewed.
assessments:
- assessment_id: qualification-scope
  area: provenance
  topic: Source-owned note-only curation
  outcome: supported
  summary: All three complete records retain chemical identity, CARD ownership, original
    assertions and unrelated fields; one note and history event change per record.
  target_ids:
  - CHEBI:8269
  - CHEBI:59064
  - CHEBI:59673
  evidence_ids:
  - qualification-input
- assessment_id: remaining-grounding
  area: grounding
  topic: Exact experimental and compound scope
  outcome: concern
  summary: Qualifications mitigate presentation gaps but do not assign an experimental
    protein, allele, taxon, genome or AST observation.
  target_ids:
  - CHEBI:8269
  - CHEBI:59064
  - CHEBI:59673
  evidence_ids:
  - qualification-input
  - prior-context
  - later-mcr-context
findings:
- category: evidence
  certainty: confirmed
  description: The missing qualification is now present, including later contrasting
    evidence. Reconciliation of tested contexts and evidence for purified colistin
    A and B remain open; the source assertion has not been promoted to an experiment.
  evidence_ids:
  - qualification-input
  - prior-context
  - later-mcr-context
  field_paths:
  - resistance_mechanisms[aro_id=ARO:3004695]
  finding_id: mcr43-context
  issue_key: card-protein-name-mcr43-context
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Unchanged upstream assertions; do not hand-edit
  - repository: culturebotai/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Pinned evidence-scope qualifications
  - repository: culturebotai/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Closed qualification validation and note-only projection
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Validated, history-preserving source-owned emission
  severity: major
  status: open
  target_ids:
  - CHEBI:59064
  - CHEBI:59673
  title: Contrasting functional contexts and component-specific grounding remain unresolved
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261015T131237Z-card-protein-name-primary-context
    finding_id: mcr43-context
- category: scope
  certainty: confirmed
  description: The derivative-versus-parent limitation is now explicit. The inherited
    database assertion still lacks exact-parent experimental support; no allele or
    organism assignment is inferred.
  evidence_ids:
  - qualification-input
  - prior-context
  field_paths:
  - resistance_mechanisms[aro_id=ARO:3003761]
  finding_id: eatav-compound
  issue_key: card-protein-name-eatav-compound
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Unchanged upstream assertions; do not hand-edit
  - repository: culturebotai/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Pinned evidence-scope qualifications
  - repository: culturebotai/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Closed qualification validation and note-only projection
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Validated, history-preserving source-owned emission
  severity: major
  status: open
  target_ids:
  - CHEBI:8269
  title: Tested derivative does not ground the parent compound
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261015T131237Z-card-protein-name-primary-context
    finding_id: eatav-compound
actions:
- action_id: continue-mcr43-context
  finding_ids:
  - mcr43-context
  description: Resolve the remaining primary-evidence and exact-compound scope before
    experimental grounding or finding closure.
  target_ids:
  - CHEBI:59064
  - CHEBI:59673
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Unchanged upstream assertions; do not hand-edit
  - repository: culturebotai/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Pinned evidence-scope qualifications
  - repository: culturebotai/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Closed qualification validation and note-only projection
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Validated, history-preserving source-owned emission
  acceptance_checks:
  - Preserve both conflicting contexts and the exact structure boundary.
  - Do not infer experimental accession, host or phenotype from reference identity.
  - Complete authoritative QC on a supported platform before publication.
  generator: scripts/seed_from_sources.py
- action_id: continue-eatav-compound
  finding_ids:
  - eatav-compound
  description: Resolve the remaining primary-evidence and exact-compound scope before
    experimental grounding or finding closure.
  target_ids:
  - CHEBI:8269
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Unchanged upstream assertions; do not hand-edit
  - repository: culturebotai/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Pinned evidence-scope qualifications
  - repository: culturebotai/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Closed qualification validation and note-only projection
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Validated, history-preserving source-owned emission
  acceptance_checks:
  - Preserve both conflicting contexts and the exact structure boundary.
  - Do not infer experimental accession, host or phenotype from reference identity.
  - Complete authoritative QC on a supported platform before publication.
  generator: scripts/seed_from_sources.py
related_reviews:
- repository: culturebotai/AntibioticMech
  review_id: 20261015T131237Z-card-protein-name-primary-context
  relationship: Partial follow-up of two major findings; no closure
limitations:
- Full authoritative QC cannot start on Intel macOS with the locked RDKit distribution;
  available separate checks are not a full pass.
- Primary figures and supplements were not reviewed; no full source reconciliation
  or exact-component experimental assertion.
- 'No NCBI requests, source adoption, outreach, GitHub mutations or reuse-terms review.
  Issue #1040 remains deferred.'
- No operational sequences, variants, constructs, primers, protocols or coordinates
  are exported.
- The full-corpus goal remains open and the prior reference index remains a historical
  snapshot.
- Evidence access time marks final inspection of the available text, not an underlying
  HTTP fetch timestamp.
notes:
- 'Regression tests: 509 passed; 3 explicitly skipped historical live replays.'
- 'Protected pre-write baseline: 7798 files; three record deltas checked.'
tags:
- card
- evidence-scope
- partial
- source-owned
```
