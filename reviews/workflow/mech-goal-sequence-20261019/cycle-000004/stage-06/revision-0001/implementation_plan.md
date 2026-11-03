# Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `4`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Repository**: `CultureBotAI/AntibioticMech` (`antibioticmech`)
- **Source revision**: `a9d5d5c146ba67cd3b302e4f229a9520c096c0c4`
- **Scope frozen at**: `2026-11-03T17:32:01Z`
- **Frozen snapshot SHA-256**: `7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`

## 1. Frozen Intake Scope

At the Stage 6 cutoff (`2026-11-03T17:32:01Z`), the supervisor-frozen `INFRA_TASKS.md` snapshot (`infra_snapshot.md`) contains 1 historical task entry and **0 non-resolved tasks** (`open`, `note`, or `deferred`):

| Task ID | Status at Cutoff | GitHub Issue | Resolved In | Summary |
| --- | --- | --- | --- | --- |
| `antibioticmech-infra-0001` | `resolved` | [#1256](https://github.com/CultureBotAI/AntibioticMech/issues/1256) | Cycle 1, Stage 6 (PR [#1261](https://github.com/CultureBotAI/AntibioticMech/pull/1261)) | Preserve curator-reviewed `structural_observations` across `scripts/seed_from_sources.py` `merge_with_existing` runs |

During Cycle 4 Stages 1–5:
- Stage 1 (PR [#1292](https://github.com/CultureBotAI/AntibioticMech/pull/1292)) added 38 MIBiG v4.0 antimicrobial structures (and retired 8 duplicate curator entries), bringing the corpus to 3,042 records; Stage 2 (PR [#1297](https://github.com/CultureBotAI/AntibioticMech/pull/1297)) promoted 5 held `REVIEWED` records to curated `causal_graphs` (bringing total records with `causal_graphs` to 69 across 70 graphs) and curated primary-literature-backed top-level mechanism representations across 32 Cycle 4 Stage 1 MIBiG 4.0 records; Stage 3 (PR [#1300](https://github.com/CultureBotAI/AntibioticMech/pull/1300)) curated reviewed `UniProtKB` `ProteinExample` entries and primary-literature `MolecularTarget` entries across eligible records.
- Stage 4 (`review_records`, PR [#1304](https://github.com/CultureBotAI/AntibioticMech/pull/1304)) reviewed all 3,042 records in the corpus and recorded 11 stable findings (3 open actionable findings across 11 `EXACT` ChEBI records and 8 deferred findings carried forward), with `infra_tasks: []` and zero schema, generator, or tooling infrastructure bottlenecks.
- Stage 5 (`resolve_review_findings`, PR [#1309](https://github.com/CultureBotAI/AntibioticMech/pull/1309), merged at `a9d5d5c146ba67cd3b302e4f229a9520c096c0c4`) resolved all 3 open actionable Stage 4 findings across 11 `EXACT` ChEBI records (`proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion` on 1 record — `squalestatin-s1` `CHEBI:220211` — under [#1306](https://github.com/CultureBotAI/AntibioticMech/issues/1306); `cycle4-stage1-proposed-exact-natural-products-missing-mechanism-and-targets` on 6 records — `diazaquinomycin-h`, `diazaquinomycin-j`, `jessenipeptin`, `minimycin`, `pamamycin-621a`, `pamamycin-649b` — under [#1307](https://github.com/CultureBotAI/AntibioticMech/issues/1307); and `seeded-exact-fluoroquinolones-with-card-only-targets-awaiting-primary-literature-promotion` on 4 records — `enoxacin`, `fleroxacin`, `gatifloxacin`, `trovafloxacin` — under [#1308](https://github.com/CultureBotAI/AntibioticMech/issues/1308)), as well as the PR [#1309](https://github.com/CultureBotAI/AntibioticMech/pull/1309) review remediation issue [#1310](https://github.com/CultureBotAI/AntibioticMech/issues/1310). All 4 Stage 5 issues ([#1306](https://github.com/CultureBotAI/AntibioticMech/issues/1306), [#1307](https://github.com/CultureBotAI/AntibioticMech/issues/1307), [#1308](https://github.com/CultureBotAI/AntibioticMech/issues/1308), [#1310](https://github.com/CultureBotAI/AntibioticMech/issues/1310)) are closed and verified. The 8 deferred scientific/curation findings were carried forward under Issues [#1140](https://github.com/CultureBotAI/AntibioticMech/issues/1140)–[#1144](https://github.com/CultureBotAI/AntibioticMech/issues/1144) and [#1257](https://github.com/CultureBotAI/AntibioticMech/issues/1257)–[#1259](https://github.com/CultureBotAI/AntibioticMech/issues/1259).

## 2. Open-Issue Queue Audit (`review-open-issues`)

An audit of the open GitHub issue queue (`gh issue list --repo CultureBotAI/AntibioticMech --state open --limit 5000`) confirmed:
- The three active workflow review issues ([#1257](https://github.com/CultureBotAI/AntibioticMech/issues/1257), [#1258](https://github.com/CultureBotAI/AntibioticMech/issues/1258), [#1259](https://github.com/CultureBotAI/AntibioticMech/issues/1259)) and the five pre-existing curation blockers ([#1140](https://github.com/CultureBotAI/AntibioticMech/issues/1140)–[#1144](https://github.com/CultureBotAI/AntibioticMech/issues/1144)) are scientific/curation tasks rather than infrastructure tasks.
- Issue [#1256](https://github.com/CultureBotAI/AntibioticMech/issues/1256) (`antibioticmech-infra-0001`), the 3 Cycle 4 Stage 5 finding-group issues ([#1306](https://github.com/CultureBotAI/AntibioticMech/issues/1306), [#1307](https://github.com/CultureBotAI/AntibioticMech/issues/1307), [#1308](https://github.com/CultureBotAI/AntibioticMech/issues/1308)), and the PR [#1309](https://github.com/CultureBotAI/AntibioticMech/pull/1309) review remediation issue ([#1310](https://github.com/CultureBotAI/AntibioticMech/issues/1310)) are closed and resolved.
- No unrecorded `note`, `open`, or `deferred` tasks exist in `INFRA_TASKS.md` at the `2026-11-03T17:32:01Z` cutoff.

## 3. Dependency-Aware Implementation Plan

Because the frozen intake at `2026-11-03T17:32:01Z` has **0 non-resolved tasks** (`pending_tasks == {}`), no code or schema changes are required or permitted under the bounded Stage 6 scope rule ("never expand the frozen task-ID scope"). The Stage 6 implementation plan consists of:

1. **Verified Evidence Index Synchronization**:
   - Update `reviews/workflow/latest.yaml` from the supervisor-verified `verified-evidence-index.json` to record the verified Cycle 4 Stage 5 closure (`pr_number: 1309`, `head_sha: 3a93399101f0bbe968f60f986cac6ea8b4c6c98b`, `merge_commit_sha: a9d5d5c146ba67cd3b302e4f229a9520c096c0c4`, `receipt_sha256: 2171f7afcd6f9bff8c4e5cd80003134d1186c2505734a642d93aa2129b3e3641`).
2. **Bounded Stage 6 Evidence Persistence**:
   - Persist the exact supervisor-frozen `INFRA_TASKS.md` snapshot (`sha256: 7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`) at `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/infra_snapshot.md`.
   - Persist this `implementation_plan.md`, `validation.md`, and the parent-contract `evidence.yaml` (`outcome: no_findings`, `infra_tasks: []`, `scope_frozen_at: '2026-11-03T17:32:01Z'`).
   - Retain `antibioticmech-infra-0001` (`status: resolved`) unchanged in `INFRA_TASKS.md`.

## 4. Acceptance Criteria

- `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/infra_snapshot.md` matches the supervisor-frozen `INFRA_TASKS.md` SHA-256 (`7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`).
- `kg_microbe_workflows validate` and `kg_microbe_workflows validate-evidence` pass with zero errors.
- Lightweight sequential repository validation checks (`ruff check`, targeted `pytest`, `check_docs.py`, and full CI `qc` + `vendored-sync` gates on the PR) pass with zero errors.
