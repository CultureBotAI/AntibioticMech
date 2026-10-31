# Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Repository**: `CultureBotAI/AntibioticMech` (`antibioticmech`)
- **Source revision**: `13bf5681ca4fac4a15c87b7c4c78391594e472d4`
- **Scope frozen at**: `2026-10-31T06:43:03Z`
- **Frozen snapshot SHA-256**: `7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`

## 1. Frozen Intake Scope

At the Stage 6 cutoff (`2026-10-31T06:43:03Z`), the supervisor-frozen `INFRA_TASKS.md` snapshot (`infra_snapshot.md`) contains 1 historical task entry and **0 non-resolved tasks** (`open`, `note`, or `deferred`):

| Task ID | Status at Cutoff | GitHub Issue | Resolved In | Summary |
| --- | --- | --- | --- | --- |
| `antibioticmech-infra-0001` | `resolved` | [#1256](https://github.com/CultureBotAI/AntibioticMech/issues/1256) | Cycle 1, Stage 6 (PR [#1261](https://github.com/CultureBotAI/AntibioticMech/pull/1261)) | Preserve curator-reviewed `structural_observations` across `scripts/seed_from_sources.py` `merge_with_existing` runs |

During Cycle 3 Stages 1–5:
- Stage 1 (PR [#1279](https://github.com/CultureBotAI/AntibioticMech/pull/1279)) added 20 exact antimicrobial structures, expanding the corpus from 2,992 to 3,012 records; Stage 2 (PR [#1280](https://github.com/CultureBotAI/AntibioticMech/pull/1280)) promoted 5 held `REVIEWED` records (`avibactam`, `bromodeoxytopsentin`, `zafirlukast`, `oteseconazole`, `thermorubin A`) to curated `causal_graphs` (bringing total records with `causal_graphs` to 64 across 65 graphs) and co-curated primary-literature-backed top-level mechanism representations across all 20 Cycle 3 Stage 1 `PROPOSED` records; Stage 3 (PR [#1281](https://github.com/CultureBotAI/AntibioticMech/pull/1281)) curated reviewed `UniProtKB` `ProteinExample` entries and primary-literature `MolecularTarget` entries on `PROPOSED` records.
- Stage 4 (`review_records`, PR [#1282](https://github.com/CultureBotAI/AntibioticMech/pull/1282)) reviewed all 3,012 records in the corpus and recorded 11 stable findings (3 open actionable findings across 12 records and 8 deferred findings carried forward), with `infra_tasks: []` and zero schema, generator, or tooling infrastructure bottlenecks.
- Stage 5 (`resolve_review_findings`, PR [#1287](https://github.com/CultureBotAI/AntibioticMech/pull/1287), merged at `13bf5681ca4fac4a15c87b7c4c78391594e472d4`) resolved all 3 open actionable Stage 4 findings across 12 records (`proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion` on 2 records — `bactobolin A`, `negamycin` — under [#1284](https://github.com/CultureBotAI/AntibioticMech/issues/1284); `proposed-exact-quinolones-with-moa-missing-primary-targets-and-reviewed-promotion` on 3 records — `besifloxacin`, `ozenoxacin`, `pazufloxacin` — under [#1285](https://github.com/CultureBotAI/AntibioticMech/issues/1285); and `proposed-minted-records-with-moa-missing-primary-targets` on 7 records — `cadazolid`, `radezolid`, `sutezolid`, `sanfetrinem`, `tomopenem`, `albaconazole`, `quilseconazole` — under [#1286](https://github.com/CultureBotAI/AntibioticMech/issues/1286)), as well as the PR [#1287](https://github.com/CultureBotAI/AntibioticMech/pull/1287) review remediation issue [#1288](https://github.com/CultureBotAI/AntibioticMech/issues/1288). All 4 Stage 5 issues ([#1284](https://github.com/CultureBotAI/AntibioticMech/issues/1284), [#1285](https://github.com/CultureBotAI/AntibioticMech/issues/1285), [#1286](https://github.com/CultureBotAI/AntibioticMech/issues/1286), [#1288](https://github.com/CultureBotAI/AntibioticMech/issues/1288)) are closed and verified. The 8 deferred scientific/curation findings were carried forward under Issues [#1140](https://github.com/CultureBotAI/AntibioticMech/issues/1140)–[#1144](https://github.com/CultureBotAI/AntibioticMech/issues/1144) and [#1257](https://github.com/CultureBotAI/AntibioticMech/issues/1257)–[#1259](https://github.com/CultureBotAI/AntibioticMech/issues/1259).

## 2. Open-Issue Queue Audit (`review-open-issues`)

An audit of the open GitHub issue queue (`gh issue list --state open --limit 5000`) confirmed:
- The three active workflow review issues ([#1257](https://github.com/CultureBotAI/AntibioticMech/issues/1257), [#1258](https://github.com/CultureBotAI/AntibioticMech/issues/1258), [#1259](https://github.com/CultureBotAI/AntibioticMech/issues/1259)) and the five pre-existing curation blockers ([#1140](https://github.com/CultureBotAI/AntibioticMech/issues/1140)–[#1144](https://github.com/CultureBotAI/AntibioticMech/issues/1144)) are scientific/curation tasks rather than infrastructure tasks.
- Issue [#1256](https://github.com/CultureBotAI/AntibioticMech/issues/1256) (`antibioticmech-infra-0001`), the 3 Cycle 3 Stage 5 finding-group issues ([#1284](https://github.com/CultureBotAI/AntibioticMech/issues/1284), [#1285](https://github.com/CultureBotAI/AntibioticMech/issues/1285), [#1286](https://github.com/CultureBotAI/AntibioticMech/issues/1286)), and the PR [#1287](https://github.com/CultureBotAI/AntibioticMech/pull/1287) review remediation issue ([#1288](https://github.com/CultureBotAI/AntibioticMech/issues/1288)) are closed and resolved.
- No unrecorded `note`, `open`, or `deferred` tasks exist in `INFRA_TASKS.md` at the `2026-10-31T06:43:03Z` cutoff.

## 3. Dependency-Aware Implementation Plan

Because the frozen intake at `2026-10-31T06:43:03Z` has **0 non-resolved tasks** (`pending_tasks == {}`), no code or schema changes are required or permitted under the bounded Stage 6 scope rule ("never expand the frozen task-ID scope"). The Stage 6 implementation plan consists of:

1. **Verified Evidence Index Synchronization**:
   - Update `reviews/workflow/latest.yaml` from the supervisor-verified `verified-evidence-index.json` to record the verified Cycle 3 Stage 5 closure (`pr_number: 1287`, `head_sha: f9226fb26f7233e708bf9fd5df7994e7b07d5c0c`, `merge_commit_sha: 13bf5681ca4fac4a15c87b7c4c78391594e472d4`, `receipt_sha256: af0019283dc19ed1a48102df2c0c7833ed16d01a190350e68eaafa8bb4d76fcd`).
2. **Bounded Stage 6 Evidence Persistence**:
   - Persist the exact supervisor-frozen `INFRA_TASKS.md` snapshot (`sha256: 7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`) at `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/infra_snapshot.md`.
   - Persist this `implementation_plan.md`, `validation.md`, and the parent-contract `evidence.yaml` (`outcome: no_findings`, `infra_tasks: []`, `scope_frozen_at: '2026-10-31T06:43:03Z'`).
   - Retain `antibioticmech-infra-0001` (`status: resolved`) unchanged in `INFRA_TASKS.md`.

## 4. Acceptance Criteria

- `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/infra_snapshot.md` matches the supervisor-frozen `INFRA_TASKS.md` SHA-256 (`7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`).
- `kg_microbe_workflows validate` and `kg_microbe_workflows validate-evidence` pass with zero errors.
- Lightweight sequential repository validation checks (`ruff check`, targeted `pytest`, `check_docs.py`, and full CI `qc` + `vendored-sync` gates on the PR) pass with zero errors.
