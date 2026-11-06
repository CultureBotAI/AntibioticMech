# Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `6`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Repository**: `CultureBotAI/AntibioticMech` (`antibioticmech`)
- **Source revision**: `f9f029631945a7307f62db26b74f317cdf4d716a`
- **Scope frozen at**: `2026-11-06T00:31:02Z`
- **Frozen snapshot SHA-256**: `7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`

## 1. Frozen Intake Scope

At the Stage 6 cutoff (`2026-11-06T00:31:02Z`), the supervisor-frozen `INFRA_TASKS.md` snapshot (`infra_snapshot.md`) contains 1 historical task entry and **0 non-resolved tasks** (`open`, `note`, or `deferred`):

| Task ID | Status at Cutoff | GitHub Issue | Resolved In | Summary |
| --- | --- | --- | --- | --- |
| `antibioticmech-infra-0001` | `resolved` | [#1256](https://github.com/CultureBotAI/AntibioticMech/issues/1256) | Cycle 1, Stage 6 (PR [#1261](https://github.com/CultureBotAI/AntibioticMech/pull/1261)) | Preserve curator-reviewed `structural_observations` across `scripts/seed_from_sources.py` `merge_with_existing` runs |

During Cycle 6 Stages 1–5:
- Stage 1 (PR [#1327](https://github.com/CultureBotAI/AntibioticMech/pull/1327), resolving review remediation issue [#1328](https://github.com/CultureBotAI/AntibioticMech/issues/1328)) added 22 exact antimicrobial chemical structures (`15` `EXACT` ChEBI natural products and `7` `MINTED` literature-backed structures), expanding the corpus from 3,064 to 3,086 records (`2,755` `EXACT`, `331` `MINTED`; `2,859` `SEEDED`, `100` `PROPOSED`, `127` `REVIEWED`).
- Stage 2 (PR [#1329](https://github.com/CultureBotAI/AntibioticMech/pull/1329)) curated primary-literature `causal_graphs` on 6 held `REVIEWED` records (`cinoxacin`, `Grepafloxacin`, `lomefloxacin`, `moxifloxacin`, `sparfloxacin`, and `pneumocandin-a0`, bringing total records with `causal_graphs` from 75 to 81 across 82 graphs) and curated `biosynthesis_origin` across all 22 Cycle 6 Stage 1 records plus primary-literature `mode_of_action` claims on 8 of them (`berninamycin-a`, `berninamycin-b`, `empedopeptin`, `laterocidine`, `obafluorin`, `salinamide-a`, `salinamide-b`, `rimocidin`, raising `mode_of_action` coverage from 514 to 522).
- Stage 3 (PR [#1330](https://github.com/CultureBotAI/AntibioticMech/pull/1330), resolving review remediation issue [#1331](https://github.com/CultureBotAI/AntibioticMech/issues/1331)) curated primary-literature `molecular_targets` across 8 Cycle 6 Stage 1 `PROPOSED` records (`berninamycin-a`, `berninamycin-b`, `empedopeptin`, `laterocidine`, `obafluorin`, `salinamide-a`, `salinamide-b`, `rimocidin`), added 20 reviewed Swiss-Prot `UniProtKB` `protein_examples` across 9 records (`cinoxacin`, `Grepafloxacin`, `lomefloxacin`, `moxifloxacin`, `sparfloxacin`, `pneumocandin-a0`, `obafluorin`, `salinamide-a`, `salinamide-b`) and 11 `held_targets` entries in `curation/uniprot_protein_examples.yaml` (`records=81`, `held_targets=111`).
- Stage 4 (`review_records`, PR [#1332](https://github.com/CultureBotAI/AntibioticMech/pull/1332)) reviewed all 3,086 records in the corpus and recorded 11 stable findings (3 open actionable findings across 18 `EXACT` ChEBI records and 8 deferred findings carried forward), with `infra_tasks: []` and zero schema, generator, or tooling infrastructure bottlenecks.
- Stage 5 (`resolve_review_findings`, PR [#1336](https://github.com/CultureBotAI/AntibioticMech/pull/1336), merged at `f9f029631945a7307f62db26b74f317cdf4d716a`) resolved all 3 open actionable Stage 4 findings across 18 `EXACT` ChEBI records (promoting all 18 to `REVIEWED`, raising `REVIEWED` from 127 to 145, `SEEDED` 2,854, `PROPOSED` 87, and `With target or resistance evidence` 494: `proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion` on 8 records — `berninamycin-a`, `berninamycin-b`, `empedopeptin`, `laterocidine`, `obafluorin`, `salinamide-a`, `salinamide-b`, `rimocidin` — under [#1333](https://github.com/CultureBotAI/AntibioticMech/issues/1333); `cycle6-stage1-proposed-exact-natural-products-missing-mechanism-and-targets` on 5 records — `kendomycin-b`, `marinopyrrole-c`, `marinopyrrole-d`, `marinopyrrole-e`, `amipurimycin` — under [#1334](https://github.com/CultureBotAI/AntibioticMech/issues/1334); and `seeded-exact-sulfonamides-with-card-only-targets-awaiting-primary-literature-promotion` on 5 records — `sulfacetamide`, `sulfamethazine`, `sulfamethizole`, `sulfamethoxazole`, `sulfadiazine` — under [#1335](https://github.com/CultureBotAI/AntibioticMech/issues/1335)). All 3 Stage 5 issues ([#1333](https://github.com/CultureBotAI/AntibioticMech/issues/1333), [#1334](https://github.com/CultureBotAI/AntibioticMech/issues/1334), [#1335](https://github.com/CultureBotAI/AntibioticMech/issues/1335)) are closed and verified. The 8 deferred scientific/curation findings were carried forward under Issues [#1140](https://github.com/CultureBotAI/AntibioticMech/issues/1140)–[#1144](https://github.com/CultureBotAI/AntibioticMech/issues/1144) and [#1257](https://github.com/CultureBotAI/AntibioticMech/issues/1257)–[#1259](https://github.com/CultureBotAI/AntibioticMech/issues/1259).

## 2. Open-Issue Queue Audit (`review-open-issues`)

An audit of the open GitHub issue queue (`gh issue list --repo CultureBotAI/AntibioticMech --state open --limit 5000`) confirmed:
- The three active workflow review issues ([#1257](https://github.com/CultureBotAI/AntibioticMech/issues/1257), [#1258](https://github.com/CultureBotAI/AntibioticMech/issues/1258), [#1259](https://github.com/CultureBotAI/AntibioticMech/issues/1259)) and the five pre-existing curation blockers ([#1140](https://github.com/CultureBotAI/AntibioticMech/issues/1140)–[#1144](https://github.com/CultureBotAI/AntibioticMech/issues/1144)) are scientific/curation tasks rather than infrastructure tasks.
- Issue [#1256](https://github.com/CultureBotAI/AntibioticMech/issues/1256) (`antibioticmech-infra-0001`) and the 3 Cycle 6 Stage 5 finding-group issues ([#1333](https://github.com/CultureBotAI/AntibioticMech/issues/1333), [#1334](https://github.com/CultureBotAI/AntibioticMech/issues/1334), [#1335](https://github.com/CultureBotAI/AntibioticMech/issues/1335)) are closed and resolved.
- No unrecorded `note`, `open`, or `deferred` tasks exist in `INFRA_TASKS.md` at the `2026-11-06T00:31:02Z` cutoff.

## 3. Dependency-Aware Implementation Plan

Because the frozen intake at `2026-11-06T00:31:02Z` has **0 non-resolved tasks** (`pending_tasks == {}`), no code or schema changes are required or permitted under the bounded Stage 6 scope rule ("never expand the frozen task-ID scope"). The Stage 6 implementation plan consists of:

1. **Verified Evidence Index Synchronization**:
   - Update `reviews/workflow/latest.yaml` from the supervisor-verified `verified-evidence-index.json` to record the verified Cycle 6 Stage 5 closure (`pr_number: 1336`, `head_sha: 919b91aea0a5ddaec6cbba1f61235dccafacab33`, `merge_commit_sha: f9f029631945a7307f62db26b74f317cdf4d716a`, `receipt_sha256: 781896cc651ffd0479d81bfeeeb354bae7d248bae6253caf7756343a24bb0a7a`).
2. **Bounded Stage 6 Evidence Persistence**:
   - Persist the exact supervisor-frozen `INFRA_TASKS.md` snapshot (`sha256: 7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`) at `reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-06/revision-0001/infra_snapshot.md`.
   - Persist this `implementation_plan.md`, `validation.md`, and the parent-contract `evidence.yaml` (`outcome: no_findings`, `infra_tasks: []`, `scope_frozen_at: '2026-11-06T00:31:02Z'`).
   - Retain `antibioticmech-infra-0001` (`status: resolved`) unchanged in `INFRA_TASKS.md`.

## 4. Acceptance Criteria

- `reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-06/revision-0001/infra_snapshot.md` matches the supervisor-frozen `INFRA_TASKS.md` SHA-256 (`7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`).
- `kg_microbe_workflows validate` and `kg_microbe_workflows validate-evidence` pass with zero errors.
- Lightweight sequential repository validation checks (`ruff check`, targeted `pytest`, `check_docs.py`, and full CI `qc` + `vendored-sync` gates on the PR) pass with zero errors.
