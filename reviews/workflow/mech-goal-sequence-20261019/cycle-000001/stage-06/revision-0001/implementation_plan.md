# Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Repository**: `CultureBotAI/AntibioticMech` (`antibioticmech`)
- **Source revision**: `13877e8d28288acfff5c4880866a6c09758d2fdc`
- **Scope frozen at**: `2026-10-23T21:52:57Z`
- **Frozen snapshot SHA-256**: `ac059552ec14b8604a42afca131875bfcd5c0a59bf2566b605451fb2c51270f9`

## 1. Frozen Intake Scope

At the Stage 6 cutoff (`2026-10-23T21:52:57Z`), the supervisor-frozen `INFRA_TASKS.md` snapshot (`infra_snapshot.md`) contains 1 non-resolved task:

| Task ID | Status at Cutoff | GitHub Issue | Priority | Dependencies | Summary |
| --- | --- | --- | --- | --- | --- |
| `antibioticmech-infra-0001` | `open` | [#1256](https://github.com/CultureBotAI/AntibioticMech/issues/1256) | `P1` | None | Preserve curator-reviewed `structural_observations` across `scripts/seed_from_sources.py` `merge_with_existing` runs |

No additional tasks were present in the frozen intake, and no tasks are deferred or blocked.

## 2. Dependency-Aware Implementation Plan

### Task `antibioticmech-infra-0001` (Issue [#1256](https://github.com/CultureBotAI/AntibioticMech/issues/1256))

1. **Problem Statement**:
   - `scripts/seed_from_sources.py` extracts macromolecular PDB accessions from ChEBI `xrefs` into `structural_observations` with `relevance: UNREVIEWED` and `evidence_status: PRIMARY_EVIDENCE_NEEDED`.
   - While `seeded_structural_view(record)` compares only `(structure_id, source)` pairs for `source in SEEDER_STRUCTURE_SOURCES`, `merge_with_existing(record, existing)` had no handler for `structural_observations` and `reseed_delta(existing, record, merged, curator_owns_clinical)` did not track `structural_observations`.
   - Consequently, running `scripts/seed_from_sources.py --apply` overwrote any curator-classified `structural_observations` on a seeded record back to `UNREVIEWED` / `PRIMARY_EVIDENCE_NEEDED` and dropped any curator-added `structural_observations` (`source: "curator"`).
   - In addition, `tests/test_structural_observations.py::test_the_migrated_accessions_are_present_and_unreviewed` required every `structural_observations` item in the corpus to remain `UNREVIEWED` with no `evidence`.

2. **Implementation Steps**:
   - In `scripts/seed_from_sources.py`:
     - Define `_SEEDED_STRUCTURE_KEYS` (`structure_id`, `relevance`, `evidence_status`, `source`, `source_version`, `retrieved_on`) and `is_curated_structural_observation(item: dict) -> bool` to detect when a seeded observation has been curator-classified (`relevance != "UNREVIEWED"`, `evidence_status != "PRIMARY_EVIDENCE_NEEDED"`, or extra curated fields/evidence present).
     - Define `_seeded_structural_reseed_view(record: dict) -> list[dict]` and include it in `reseed_delta(existing, record, merged, curator_owns_clinical)` so upstream provenance changes (`source_version`, `retrieved_on`) or new/removed seeded `structure_id` entries are detected without flagging curator classifications as drift.
     - In `merge_with_existing(record, existing)`, preserve curator-classified seeded `structural_observations` by `(structure_id, source)` while refreshing `source_version` and `retrieved_on` from the freshly seeded entry, and preserve curator-authored `structural_observations` (`source not in SEEDER_STRUCTURE_SOURCES`).
   - In `tests/test_structural_observations.py`:
     - Update `test_the_migrated_accessions_are_present_and_unreviewed` so `UNREVIEWED` observations must carry `PRIMARY_EVIDENCE_NEEDED` and no `evidence`, while curator-classified observations (`relevance != "UNREVIEWED"`) must carry `PRIMARY_EVIDENCE` and non-empty `evidence`.
     - Expand `test_a_curator_addition_does_not_break_reproduction` to test `merge_with_existing` and `reseed_delta` across both curator-classified seeded observations and curator-added observations, as well as unreviewed seeded observations.
   - Update `INFRA_TASKS.md` to mark `antibioticmech-infra-0001` as `resolved` with its disposition and evidence paths.
   - Update `reviews/workflow/latest.yaml` from the supervisor-verified `verified-evidence-index.json` (recording verified Stage 4 and Stage 5 closures).

3. **Acceptance Criteria**:
   - `merge_with_existing` preserves curator-classified fields (`relevance`, `evidence_status`, `evidence`, macromolecule metadata) on seeded `structural_observations` while updating `source_version` and `retrieved_on`, and retains curator-added `structural_observations`.
   - `reseed_delta` reports `["structural_observations"]` when upstream `source_version`/`retrieved_on` changes on a curated seeded observation and `[]` once merged.
   - `scripts/verify_corpus.py`, `pytest`, and `ruff check` pass with zero errors.
