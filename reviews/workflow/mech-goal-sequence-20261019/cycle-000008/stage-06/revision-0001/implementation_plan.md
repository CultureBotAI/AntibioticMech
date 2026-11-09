# Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `8`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Repository**: `CultureBotAI/AntibioticMech` (`antibioticmech`)
- **Source revision**: `5c426b76ef06c0321ddca356d095c972052df80e`
- **Scope frozen at**: `2026-11-09T17:58:55Z`
- **Frozen snapshot SHA-256**: `7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`

## 1. Frozen Intake Scope

At the Stage 6 cutoff (`2026-11-09T17:58:55Z`), the supervisor-frozen `INFRA_TASKS.md` snapshot (`infra_snapshot.md`) contains 1 historical task entry and **0 non-resolved tasks** (`open`, `note`, or `deferred`):

| Task ID | Status at Cutoff | GitHub Issue | Resolved In | Summary |
| --- | --- | --- | --- | --- |
| `antibioticmech-infra-0001` | `resolved` | [#1256](https://github.com/CultureBotAI/AntibioticMech/issues/1256) | Cycle 1, Stage 6 (PR [#1261](https://github.com/CultureBotAI/AntibioticMech/pull/1261)) | Preserve curator-reviewed `structural_observations` across `scripts/seed_from_sources.py` `merge_with_existing` runs |

During Cycle 8 Stages 1–5:
- Stage 1 (`add_records`, PR [#1353](https://github.com/CultureBotAI/AntibioticMech/pull/1353)) added 20 exact antimicrobial chemical structures (`15` `EXACT` ChEBI natural products and `5` `MINTED` literature-backed structures), expanding the corpus from 3,105 to 3,125 records (`2,782` `EXACT`, `343` `MINTED`; `2,799` `SEEDED`, `167` `PROPOSED`, `159` `REVIEWED`).
- Stage 2 (`causal_graphs`, PR [#1354](https://github.com/CultureBotAI/AntibioticMech/pull/1354)) curated primary-literature `causal_graphs` on 6 held `REVIEWED` folate-pathway inhibitor records (`dapsone`, `sulfadoxine`, `sulfasalazine`, `sulfisoxazole`, `brodimoprim`, and `tetroxoprim`, bringing total records with `causal_graphs` from 91 to 97 — `96` `REVIEWED` records plus `1` `SEEDED` `ofloxacin` record — across 98 graphs) and curated `biosynthesis_origin` across all 20 Cycle 8 Stage 1 records plus primary-literature `mode_of_action` claims on 6 of them (`alanylclavam`, `amicetin`, `andrimid`, `bottromycin-a2`, `planosporicin`, and `ajudazol-a`).
- Stage 3 (`protein_examples`, PR [#1355](https://github.com/CultureBotAI/AntibioticMech/pull/1355)) curated primary-literature `molecular_targets` across 6 Cycle 8 Stage 1 `PROPOSED` records (`alanylclavam`, `amicetin`, `andrimid`, `bottromycin-a2`, `planosporicin`, `ajudazol-a`), added 8 reviewed Swiss-Prot `UniProtKB` `protein_examples` across 7 records (`andrimid`, `dapsone`, `sulfadoxine`, `sulfasalazine`, `sulfisoxazole`, `brodimoprim`, `tetroxoprim`, raising total `protein_examples` to 179) and 6 `held_targets` entries in `curation/uniprot_protein_examples.yaml` (`records=97`, `held_targets=131`).
- Stage 4 (`record_review`, PR [#1357](https://github.com/CultureBotAI/AntibioticMech/pull/1357), resolving review remediation issue [#1358](https://github.com/CultureBotAI/AntibioticMech/issues/1358)) reviewed all 3,125 records in the corpus (`20261109T120000Z-andrimid-record-review` and `20261109T120100Z-cycle8-frozen-inventory-cohort-review`) and recorded 11 stable findings (3 open actionable findings across 15 `EXACT` ChEBI records and 8 deferred findings carried forward), with `infra_tasks: []` and zero schema, generator, or tooling infrastructure bottlenecks.
- Stage 5 (`resolve_review_findings`, PR [#1362](https://github.com/CultureBotAI/AntibioticMech/pull/1362), merged at `5c426b76ef06c0321ddca356d095c972052df80e`) resolved all 3 open actionable Stage 4 findings across 15 `EXACT` ChEBI records (promoting all 15 to `REVIEWED`, raising `REVIEWED` from 159 to 174, `SEEDED` 2,794, `PROPOSED` 157, `With mode of action` 566, `With molecular target` 378, and `With target or resistance evidence` 518, expanding `curation/uniprot_protein_examples.yaml` to `records=102`, `held_targets=135` and `190` reviewed `protein_examples`, and updating `curation/causal_graphs.yaml` to `records=81`, `held_records=78`: `proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion` on 6 records — `alanylclavam`, `amicetin`, `andrimid`, `bottromycin-a2`, `planosporicin`, `ajudazol-a` — under [#1359](https://github.com/CultureBotAI/AntibioticMech/issues/1359); `cycle8-stage1-proposed-exact-natural-products-missing-mechanism-and-targets` on 4 records — `tp-1161`, `2-formyloxymethylclavam`, `2-hydroxymethylclavam`, `clavam-2-carboxylate` — under [#1360](https://github.com/CultureBotAI/AntibioticMech/issues/1360); and `seeded-exact-rifamycins-and-elfamycins-with-card-only-targets-awaiting-primary-literature-promotion` on 5 records — `rifabutin`, `rifaximin`, `rifapentine`, `ge2270a`, `pulvomycin` — under [#1361](https://github.com/CultureBotAI/AntibioticMech/issues/1361)). All 3 Stage 5 finding-group issues ([#1359](https://github.com/CultureBotAI/AntibioticMech/issues/1359), [#1360](https://github.com/CultureBotAI/AntibioticMech/issues/1360), [#1361](https://github.com/CultureBotAI/AntibioticMech/issues/1361)) are closed and verified. The 8 deferred scientific/curation findings were carried forward under Issues [#1140](https://github.com/CultureBotAI/AntibioticMech/issues/1140)–[#1144](https://github.com/CultureBotAI/AntibioticMech/issues/1144) and [#1257](https://github.com/CultureBotAI/AntibioticMech/issues/1257)–[#1259](https://github.com/CultureBotAI/AntibioticMech/issues/1259).

## 2. Open-Issue Queue Audit (`review-open-issues`)

An audit of the open GitHub issue queue (`gh issue list --repo CultureBotAI/AntibioticMech --state open --limit 5000`, `80` open issues) confirmed:
- The three active workflow review issues ([#1257](https://github.com/CultureBotAI/AntibioticMech/issues/1257), [#1258](https://github.com/CultureBotAI/AntibioticMech/issues/1258), [#1259](https://github.com/CultureBotAI/AntibioticMech/issues/1259)) and the five pre-existing curation blockers ([#1140](https://github.com/CultureBotAI/AntibioticMech/issues/1140)–[#1144](https://github.com/CultureBotAI/AntibioticMech/issues/1144)) are scientific/curation tasks rather than infrastructure tasks.
- Issue [#1256](https://github.com/CultureBotAI/AntibioticMech/issues/1256) (`antibioticmech-infra-0001`) and the 3 Cycle 8 Stage 5 finding-group issues ([#1359](https://github.com/CultureBotAI/AntibioticMech/issues/1359), [#1360](https://github.com/CultureBotAI/AntibioticMech/issues/1360), [#1361](https://github.com/CultureBotAI/AntibioticMech/issues/1361)) are closed and resolved.
- No unrecorded `note`, `open`, or `deferred` tasks exist in `INFRA_TASKS.md` at the `2026-11-09T17:58:55Z` cutoff.

## 3. Dependency-Aware Implementation Plan

Because the frozen intake at `2026-11-09T17:58:55Z` has **0 non-resolved tasks** (`pending_tasks == {}`), no code or schema changes are required or permitted under the bounded Stage 6 scope rule ("never expand the frozen task-ID scope"). The Stage 6 implementation plan consists of:

1. **Verified Evidence Index Synchronization**:
   - Update `reviews/workflow/latest.yaml` from the supervisor-verified `verified-evidence-index.json` to record the verified Cycle 8 Stage 5 closure (`pr_number: 1362`, `head_sha: 144e68e7143c70e7e0d65f8f02f4979c2a3eb48a`, `merge_commit_sha: 5c426b76ef06c0321ddca356d095c972052df80e`, `receipt_sha256: 3e3f50b2979a4052d673a7dc7bfabf3ec149ab774aac9e8f1053ecb25044c47b`).
2. **Bounded Stage 6 Evidence Persistence**:
   - Persist the exact supervisor-frozen `INFRA_TASKS.md` snapshot (`sha256: 7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`) at `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-06/revision-0001/infra_snapshot.md`.
   - Persist this `implementation_plan.md`, `validation.md`, and the parent-contract `evidence.yaml` (`outcome: no_findings`, `infra_tasks: []`, `scope_frozen_at: '2026-11-09T17:58:55Z'`).
   - Retain `antibioticmech-infra-0001` (`status: resolved`) unchanged in `INFRA_TASKS.md`.

## 4. Acceptance Criteria

- `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-06/revision-0001/infra_snapshot.md` matches the supervisor-frozen `INFRA_TASKS.md` SHA-256 (`7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`).
- `kg_microbe_workflows validate` and `kg_microbe_workflows validate-evidence` pass with zero errors.
- Lightweight sequential repository validation checks (`ruff check`, targeted `pytest`, `check_docs.py`, and full CI `qc` + `vendored-sync` gates on the PR) pass with zero errors.
