# AntibioticMech infrastructure tasks

This versioned ledger collects repository requirements and upgrades discovered
during every goal. The workflow profile and its parent govern intake, stage 6
implementation, closure and cycle restart.

## Intake protocol

- Give each actionable task a stable ID such as `antibioticmech-infra-0001` and retain it
  across cycles. Record the originating run, cycle and goal, observation,
  desired outcome, evidence paths, priority, dependencies and status.
- Link each task to an actual issue in https://github.com/CultureBotAI/AntibioticMech/issues.
  Search existing open and closed issues before creating one. If access fails,
  retain an explicit pending-link blocker; never invent an issue number or URL.
- Preserve resolved and deferred entries with their issue, implementation PR,
  validation and disposition. Do not overwrite previous cycle evidence.
- At stage 6, freeze a bounded snapshot, write a dependency-aware plan and
  acceptance criteria, implement selected work, validate, and complete the
  commit sequence, write the closure receipt and stop; only the supervisor
  dispatches another goal. New arrivals after the cutoff enter the next cycle;
  never expand the frozen task-ID scope. A new blocking prerequisite requires
  an explicit deferred disposition for the selected task. Carry unfinished work
  forward explicitly.

## Machine-readable task inventory

This fenced mapping is the inventory stage 6 freezes and reconciles. Each task
uses `task_id`, `summary`, `status` (`note`, `open`, `deferred`, or `resolved`),
optional `issue_url`, and optional `disposition`. Status `note` may have a
pending issue link; all other statuses require a real issue URL. Keep richer
notes below keyed by the same stable task ID.

<!-- mech-infra-tasks:start -->
```yaml
schema_version: '1.0.0'
tasks:
- task_id: antibioticmech-infra-0001
  summary: Preserve curator-reviewed structural_observations across scripts/seed_from_sources.py merge_with_existing runs
  status: resolved
  issue_url: https://github.com/CultureBotAI/AntibioticMech/issues/1256
  disposition: Implemented structural_observations preservation in scripts/seed_from_sources.py (is_curated_structural_observation, _seeded_structural_reseed_view, merge_with_existing, and reseed_delta) and expanded tests/test_structural_observations.py to cover both unreviewed and curator-classified structural_observations across reseeding.
```
<!-- mech-infra-tasks:end -->

## Tasks

### `antibioticmech-infra-0001`: Preserve curator-reviewed `structural_observations` in `scripts/seed_from_sources.py`

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019`, cycle `1`, stage `5` (`resolve_review_findings`)
- **Resolved in run / cycle / stage**: `mech-goal-sequence-20261019`, cycle `1`, stage `6` (`infrastructure`)
- **GitHub issue**: https://github.com/CultureBotAI/AntibioticMech/issues/1256
- **Status**: `resolved`
- **Priority**: `P1`
- **Dependencies**: None
- **Observation**: During Stage 5 remediation of `unreviewed-seeded-pdb-structural-observations` (`alsterpaullone` `CHEBI:138488` `PDB:1Q3W`, `ampicillin` `CHEBI:28971` `PDB:1H8S`, and `methyl-nonanoate` `CHEBI:44499` `PDB:1CLY`), `scripts/seed_from_sources.py` was found to omit `structural_observations` from `CURATOR_FIELDS` and lack a merge handler in `merge_with_existing(seeded, existing)`. Consequently, `scripts/seed_from_sources.py --verify` (`just verify-corpus`) rejects any curated `structural_observations` update on a seeded record and `just seed-apply` overwrites curated `structural_observations` back to `relevance: UNREVIEWED` and `evidence_status: PRIMARY_EVIDENCE_NEEDED`. In addition, `tests/test_structural_observations.py::test_the_migrated_accessions_are_present_and_unreviewed` asserts that those three migrated PDB accessions remain `UNREVIEWED`.
- **Desired outcome**: Add a `structural_observations` merge handler in `scripts/seed_from_sources.py::merge_with_existing` that preserves curator-upgraded `structural_observations` entries (e.g. `relevance != "UNREVIEWED"` or `evidence_status == "PRIMARY_EVIDENCE"`) by accession while retaining new seeded observations, and update `tests/test_structural_observations.py` to test both unreviewed and curator-reviewed `structural_observations` preservation.
- **Disposition**: Implemented `is_curated_structural_observation` and `_seeded_structural_reseed_view` in `scripts/seed_from_sources.py`, updated `merge_with_existing` and `reseed_delta` to preserve curator-classified/enriched seeded `structural_observations` (while updating upstream `source_version` and `retrieved_on`) as well as curator-added `structural_observations`, and updated `tests/test_structural_observations.py` to accept both unreviewed and curator-classified `structural_observations` and test preservation across `merge_with_existing` and `reseed_delta`.
- **Evidence paths**: `scripts/seed_from_sources.py`, `tests/test_structural_observations.py`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/evidence.yaml`

