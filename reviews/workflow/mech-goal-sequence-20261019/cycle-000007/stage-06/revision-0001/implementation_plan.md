# Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `7`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Repository**: `CultureBotAI/AntibioticMech` (`antibioticmech`)
- **Source revision**: `817d3f186fdf61b437a8a56b4499328e57e97e46`
- **Scope frozen at**: `2026-11-09T01:36:41Z`
- **Frozen snapshot SHA-256**: `7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`

## 1. Frozen Intake Scope

At the Stage 6 cutoff (`2026-11-09T01:36:41Z`), the supervisor-frozen `INFRA_TASKS.md` snapshot (`infra_snapshot.md`) contains 1 historical task entry and **0 non-resolved tasks** (`open`, `note`, or `deferred`):

| Task ID | Status at Cutoff | GitHub Issue | Resolved In | Summary |
| --- | --- | --- | --- | --- |
| `antibioticmech-infra-0001` | `resolved` | [#1256](https://github.com/CultureBotAI/AntibioticMech/issues/1256) | Cycle 1, Stage 6 (PR [#1261](https://github.com/CultureBotAI/AntibioticMech/pull/1261)) | Preserve curator-reviewed `structural_observations` across `scripts/seed_from_sources.py` `merge_with_existing` runs |

During Cycle 7 Stages 1–5:
- Stage 1 (`add_records`, PR [#1338](https://github.com/CultureBotAI/AntibioticMech/pull/1338)) added 19 exact antimicrobial chemical structures (`8` `EXACT` ChEBI natural products and `11` `MINTED` literature-backed structures), expanding the corpus from 3,086 to 3,105 records (`2,763` `EXACT`, `342` `MINTED`; `2,854` `SEEDED`, `106` `PROPOSED`, `145` `REVIEWED`).
- Stage 2 (`causal_graphs`, PR [#1339](https://github.com/CultureBotAI/AntibioticMech/pull/1339)) curated primary-literature `causal_graphs` on 8 held `REVIEWED` records (`obafluorin`, `salinamide-a`, `salinamide-b`, `sulfacetamide`, `sulfamethazine`, `sulfamethizole`, `sulfamethoxazole`, and `sulfadiazine`, bringing total records with `causal_graphs` from 81 to 89 across 90 graphs) and curated `biosynthesis_origin` across all 19 Cycle 7 Stage 1 records plus primary-literature `mode_of_action` claims on 3 of them (`neocarzinostatin`, `streptothricin-e`, and `epoxomicin`).
- Stage 3 (`protein_examples`, PR [#1340](https://github.com/CultureBotAI/AntibioticMech/pull/1340)) curated primary-literature `molecular_targets` across 3 Cycle 7 Stage 1 `PROPOSED` records (`neocarzinostatin`, `streptothricin-e`, `epoxomicin`), added 17 reviewed Swiss-Prot `UniProtKB` `protein_examples` across 8 records (`obafluorin`, `salinamide-a`, `salinamide-b`, `sulfacetamide`, `sulfamethazine`, `sulfamethizole`, `sulfamethoxazole`, `sulfadiazine`) and 3 `held_targets` entries in `curation/uniprot_protein_examples.yaml` (`records=89`, `held_targets=114`).
- Stage 4 (`record_review`, PR [#1343](https://github.com/CultureBotAI/AntibioticMech/pull/1343), resolving review remediation issue [#1344](https://github.com/CultureBotAI/AntibioticMech/issues/1344)) reviewed all 3,105 records in the corpus (`20261108T210000Z-neocarzinostatin-record-review` and `20261108T210100Z-cycle7-frozen-inventory-cohort-review`) and recorded 11 stable findings (3 open actionable findings across 14 `EXACT` ChEBI records and 8 deferred findings carried forward), with `infra_tasks: []` and zero schema, generator, or tooling infrastructure bottlenecks.
- Stage 5 (`resolve_review_findings`, PR [#1348](https://github.com/CultureBotAI/AntibioticMech/pull/1348), resolving review remediation issue [#1349](https://github.com/CultureBotAI/AntibioticMech/issues/1349), merged at `817d3f186fdf61b437a8a56b4499328e57e97e46`) resolved all 3 open actionable Stage 4 findings across 14 `EXACT` ChEBI records (promoting all 14 to `REVIEWED`, raising `REVIEWED` from 145 to 159, `SEEDED` 2,848, `PROPOSED` 98, `With mode of action` 538, and `With target or resistance evidence` 502: `proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion` on 3 records — `neocarzinostatin`, `streptothricin-e`, `epoxomicin` — under [#1345](https://github.com/CultureBotAI/AntibioticMech/issues/1345); `cycle7-stage1-proposed-exact-natural-products-missing-mechanism-and-targets` on 5 records — `benastatin-a`, `benastatin-b`, `tetarimycin-a`, `9-methylstreptimidone`, `7-deoxypactamycin` — under [#1346](https://github.com/CultureBotAI/AntibioticMech/issues/1346); and `seeded-exact-folate-inhibitors-with-card-only-targets-awaiting-primary-literature-promotion` on 6 records — `sulfadoxine`, `sulfasalazine`, `sulfisoxazole`, `dapsone`, `brodimoprim`, `tetroxoprim` — under [#1347](https://github.com/CultureBotAI/AntibioticMech/issues/1347)). All 3 Stage 5 finding-group issues ([#1345](https://github.com/CultureBotAI/AntibioticMech/issues/1345), [#1346](https://github.com/CultureBotAI/AntibioticMech/issues/1346), [#1347](https://github.com/CultureBotAI/AntibioticMech/issues/1347)) are closed and verified. The 8 deferred scientific/curation findings were carried forward under Issues [#1140](https://github.com/CultureBotAI/AntibioticMech/issues/1140)–[#1144](https://github.com/CultureBotAI/AntibioticMech/issues/1144) and [#1257](https://github.com/CultureBotAI/AntibioticMech/issues/1257)–[#1259](https://github.com/CultureBotAI/AntibioticMech/issues/1259).

## 2. Open-Issue Queue Audit (`review-open-issues`)

An audit of the open GitHub issue queue (`gh issue list --repo CultureBotAI/AntibioticMech --state open --limit 5000`) confirmed:
- The three active workflow review issues ([#1257](https://github.com/CultureBotAI/AntibioticMech/issues/1257), [#1258](https://github.com/CultureBotAI/AntibioticMech/issues/1258), [#1259](https://github.com/CultureBotAI/AntibioticMech/issues/1259)) and the five pre-existing curation blockers ([#1140](https://github.com/CultureBotAI/AntibioticMech/issues/1140)–[#1144](https://github.com/CultureBotAI/AntibioticMech/issues/1144)) are scientific/curation tasks rather than infrastructure tasks.
- Issue [#1256](https://github.com/CultureBotAI/AntibioticMech/issues/1256) (`antibioticmech-infra-0001`) and the 3 Cycle 7 Stage 5 finding-group issues ([#1345](https://github.com/CultureBotAI/AntibioticMech/issues/1345), [#1346](https://github.com/CultureBotAI/AntibioticMech/issues/1346), [#1347](https://github.com/CultureBotAI/AntibioticMech/issues/1347)) are closed and resolved.
- No unrecorded `note`, `open`, or `deferred` tasks exist in `INFRA_TASKS.md` at the `2026-11-09T01:36:41Z` cutoff.

## 3. Dependency-Aware Implementation Plan

Because the frozen intake at `2026-11-09T01:36:41Z` has **0 non-resolved tasks** (`pending_tasks == {}`), no code or schema changes are required or permitted under the bounded Stage 6 scope rule ("never expand the frozen task-ID scope"). The Stage 6 implementation plan consists of:

1. **Verified Evidence Index Synchronization**:
   - Update `reviews/workflow/latest.yaml` from the supervisor-verified `verified-evidence-index.json` to record the verified Cycle 7 Stage 5 closure (`pr_number: 1348`, `head_sha: aa6f6378460a108866abb74255079f04bb2f177a`, `merge_commit_sha: 817d3f186fdf61b437a8a56b4499328e57e97e46`, `receipt_sha256: 6719bb7b6bcf3701849f2880e17d429328e42cabd531eacee1417c7541d4f967`).
2. **Bounded Stage 6 Evidence Persistence**:
   - Persist the exact supervisor-frozen `INFRA_TASKS.md` snapshot (`sha256: 7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`) at `reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-06/revision-0001/infra_snapshot.md`.
   - Persist this `implementation_plan.md`, `validation.md`, and the parent-contract `evidence.yaml` (`outcome: no_findings`, `infra_tasks: []`, `scope_frozen_at: '2026-11-09T01:36:41Z'`).
   - Retain `antibioticmech-infra-0001` (`status: resolved`) unchanged in `INFRA_TASKS.md`.

## 4. Acceptance Criteria

- `reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-06/revision-0001/infra_snapshot.md` matches the supervisor-frozen `INFRA_TASKS.md` SHA-256 (`7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`).
- `kg_microbe_workflows validate` and `kg_microbe_workflows validate-evidence` pass with zero errors.
- Lightweight sequential repository validation checks (`ruff check`, targeted `pytest`, `check_docs.py`, and full CI `qc` + `vendored-sync` gates on the PR) pass with zero errors.
