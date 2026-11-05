# Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `5`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1`
- **Repository**: `CultureBotAI/AntibioticMech` (`antibioticmech`)
- **Source revision**: `33d91bc639d89de17a86c6c977577128952e53b3`
- **Scope frozen at**: `2026-11-05T03:11:23Z`
- **Frozen snapshot SHA-256**: `7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`

## 1. Frozen Intake Scope

At the Stage 6 cutoff (`2026-11-05T03:11:23Z`), the supervisor-frozen `INFRA_TASKS.md` snapshot (`infra_snapshot.md`) contains 1 historical task entry and **0 non-resolved tasks** (`open`, `note`, or `deferred`):

| Task ID | Status at Cutoff | GitHub Issue | Resolved In | Summary |
| --- | --- | --- | --- | --- |
| `antibioticmech-infra-0001` | `resolved` | [#1256](https://github.com/CultureBotAI/AntibioticMech/issues/1256) | Cycle 1, Stage 6 (PR [#1261](https://github.com/CultureBotAI/AntibioticMech/pull/1261)) | Preserve curator-reviewed `structural_observations` across `scripts/seed_from_sources.py` `merge_with_existing` runs |

During Cycle 5 Stages 1–5:
- Stage 1 (PR [#1312](https://github.com/CultureBotAI/AntibioticMech/pull/1312)) added 18 publication-backed antimicrobial structures from MIBiG 4.0 and primary literature (`alaremycin`, `amylocyclicin`, `enterocin-crl35`, `fabclavine-ib`, `formula-560`, `fusaricidin-a`, `gavibactin-a`, `glycocin-f`, `herbicolin-a`, `laterocidin`, `listeriocytocin`, `mutanobactin-a`, `pamamycin-635a`, `pentalenolactone`, `plantaricyclin-a`, `ruminococcin-c1`, `streptothricin-d`, `tridecaptin-a1`), expanding the corpus to 3,060 records (`2,803` `EXACT`, `257` `MINTED`, `2,953` `REVIEWED`).
- Stage 2 (PR [#1314](https://github.com/CultureBotAI/AntibioticMech/pull/1314)) promoted 5 held `REVIEWED` records (`acriflavinium-chloride`, `berberine`, `carvacrol`, `farnesol`, `nitroxoline`) to curated primary-literature `causal_graphs` (bringing total records with `causal_graphs` to 74 across 75 graphs) and curated primary-literature mechanisms and molecular targets across all 18 Cycle 5 Stage 1 compounds.
- Stage 3 (PR [#1316](https://github.com/CultureBotAI/AntibioticMech/pull/1316)) curated 29 reviewed `UniProtKB` `ProteinExample` entries across 15 antibiotic records (`5` causal-graph records and `10` Cycle 5 Stage 1/2 records), bringing total `ProteinExample` entries to `1,004` across `274` unique reviewed `UniProtKB` accessions on `521` records.
- Stage 4 (`review_records`, PR [#1318](https://github.com/CultureBotAI/AntibioticMech/pull/1318)) reviewed all 3,060 records in the corpus and recorded 11 stable findings (3 open actionable findings across 11 `EXACT` ChEBI records and 8 deferred findings carried forward), with `infra_tasks: []` and zero schema, generator, or tooling infrastructure bottlenecks.
- Stage 5 (`resolve_review_findings`, PR [#1323](https://github.com/CultureBotAI/AntibioticMech/pull/1323), merged at `33d91bc639d89de17a86c6c977577128952e53b3`) resolved all 3 open actionable Stage 4 findings across 11 `EXACT` ChEBI records (`seeded-exact-aminoglycoside-and-beta-lactam-records-with-card-only-targets-awaiting-primary-literature-promotion` on 4 records — `lividomycin-a`, `lividomycin-b`, `mezlocillin`, `temocillin` — under [#1320](https://github.com/CultureBotAI/AntibioticMech/issues/1320); `seeded-exact-glycopeptide-and-lipopeptide-records-with-card-only-targets-awaiting-primary-literature-promotion` on 3 records — `balhimycin`, `ristocetin`, `tsushimycin` — under [#1321](https://github.com/CultureBotAI/AntibioticMech/issues/1321); and `seeded-exact-ribosomal-and-trna-synthetase-antibacterials-with-card-only-targets-awaiting-primary-literature-promotion` on 4 records — `blasticidin-s`, `clindamycin`, `josamycin`, `pseudomonic-acid` — under [#1322](https://github.com/CultureBotAI/AntibioticMech/issues/1322)), as well as the PR [#1323](https://github.com/CultureBotAI/AntibioticMech/pull/1323) review remediation issue [#1324](https://github.com/CultureBotAI/AntibioticMech/issues/1324). All 4 Stage 5 issues ([#1320](https://github.com/CultureBotAI/AntibioticMech/issues/1320), [#1321](https://github.com/CultureBotAI/AntibioticMech/issues/1321), [#1322](https://github.com/CultureBotAI/AntibioticMech/issues/1322), [#1324](https://github.com/CultureBotAI/AntibioticMech/issues/1324)) are closed and verified. The 8 deferred scientific/curation findings were carried forward under Issues [#1140](https://github.com/CultureBotAI/AntibioticMech/issues/1140)–[#1144](https://github.com/CultureBotAI/AntibioticMech/issues/1144) and [#1257](https://github.com/CultureBotAI/AntibioticMech/issues/1257)–[#1259](https://github.com/CultureBotAI/AntibioticMech/issues/1259).

## 2. Open-Issue Queue Audit (`review-open-issues`)

An audit of the open GitHub issue queue (`gh issue list --repo CultureBotAI/AntibioticMech --state open --limit 5000`) confirmed:
- The three active workflow review issues ([#1257](https://github.com/CultureBotAI/AntibioticMech/issues/1257), [#1258](https://github.com/CultureBotAI/AntibioticMech/issues/1258), [#1259](https://github.com/CultureBotAI/AntibioticMech/issues/1259)) and the five pre-existing curation blockers ([#1140](https://github.com/CultureBotAI/AntibioticMech/issues/1140)–[#1144](https://github.com/CultureBotAI/AntibioticMech/issues/1144)) are scientific/curation tasks rather than infrastructure tasks.
- Issue [#1256](https://github.com/CultureBotAI/AntibioticMech/issues/1256) (`antibioticmech-infra-0001`), the 3 Cycle 5 Stage 5 finding-group issues ([#1320](https://github.com/CultureBotAI/AntibioticMech/issues/1320), [#1321](https://github.com/CultureBotAI/AntibioticMech/issues/1321), [#1322](https://github.com/CultureBotAI/AntibioticMech/issues/1322)), and the PR [#1323](https://github.com/CultureBotAI/AntibioticMech/pull/1323) review remediation issue ([#1324](https://github.com/CultureBotAI/AntibioticMech/issues/1324)) are closed and resolved.
- No unrecorded `note`, `open`, or `deferred` tasks exist in `INFRA_TASKS.md` at the `2026-11-05T03:11:23Z` cutoff.

## 3. Dependency-Aware Implementation Plan

Because the frozen intake at `2026-11-05T03:11:23Z` has **0 non-resolved tasks** (`pending_tasks == {}`), no code or schema changes are required or permitted under the bounded Stage 6 scope rule ("never expand the frozen task-ID scope"). The Stage 6 implementation plan consists of:

1. **Verified Evidence Index Synchronization**:
   - Update `reviews/workflow/latest.yaml` from the supervisor-verified `verified-evidence-index.json` to record the verified Cycle 5 Stage 5 closure (`pr_number: 1323`, `head_sha: 96a91b5f0f58bc7249f50c24968341f6e969643e`, `merge_commit_sha: 33d91bc639d89de17a86c6c977577128952e53b3`, `receipt_sha256: ab93bf80dcde2213b64ca59315232ce9c8171fc4f7f56380a710f4155c32b1c1`).
2. **Bounded Stage 6 Evidence Persistence**:
   - Persist the exact supervisor-frozen `INFRA_TASKS.md` snapshot (`sha256: 7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`) at `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-06/revision-0001/infra_snapshot.md`.
   - Persist this `implementation_plan.md`, `validation.md`, and the parent-contract `evidence.yaml` (`outcome: no_findings`, `infra_tasks: []`, `scope_frozen_at: '2026-11-05T03:11:23Z'`).
   - Retain `antibioticmech-infra-0001` (`status: resolved`) unchanged in `INFRA_TASKS.md`.

## 4. Acceptance Criteria

- `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-06/revision-0001/infra_snapshot.md` matches the supervisor-frozen `INFRA_TASKS.md` SHA-256 (`7d5dca5a7319de1dbd3dcde5f98c9eebb5893349990f707108681ff7afb23909`).
- `kg_microbe_workflows validate` and `kg_microbe_workflows validate-evidence` pass with zero errors.
- Lightweight sequential repository validation checks (`ruff check`, targeted `pytest`, `check_docs.py`, and full CI `qc` + `vendored-sync` gates on the PR) pass with zero errors.
