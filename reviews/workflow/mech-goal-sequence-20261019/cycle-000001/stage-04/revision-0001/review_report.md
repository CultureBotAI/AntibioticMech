# Stage 4 Record & Cohort Review Report (`mech-goal-sequence-20261019`, Cycle 1, Stage 4)

## Provenance & Frozen Inventory Coverage

- **Run ID**: `mech-goal-sequence-20261019` (Cycle `1`, Stage `4` `record_review`, Revision `1`)
- **Source Git Revision**: `38cee22ec3e9a6c8ce2a3159c039dcfbb2a282bc`
- **Eligible Frozen Inventory**: `2,969` `AntibioticRecord` YAML files under `data/antibiotics/**/*.yaml` (`100%` full coverage)
  - **By Curation Status**: `SEEDED`: `2,829`, `PROPOSED`: `60`, `REVIEWED`: `80`
  - **By Grounding Status**: `EXACT` (`CHEBI:*`): `2,691`, `MINTED` (`antibioticmech:aro-*`): `278`
  - **By Antimicrobial Class Filing**: `antibacterial`: `2,226`, `antimycobacterial`: `52`, `antifungal`: `128`, `antiviral`: `120`, `antiprotozoal`: `52`, `biocide`: `134`, `unspecified`: `257`
  - **Mechanism Graph Coverage**: `52` records have `causal_graphs` (`41` `REVIEWED`, `11` `SEEDED`); `49` of `52` have curated `UniProtKB` `protein_examples` (`3` non-protein membrane/lipid/peptidoglycan target graphs: `amphotericin-b`, `daptomycin`, `vancomycin`).

## Native Structured Review Bundles (`reviews/structured/`)

| Review ID | Kind | Skill | Coverage | YAML Path | YAML SHA-256 |
| --- | --- | --- | --- | --- | --- |
| `20261023T160013Z-rifampicin-record-review` | `record` | `.claude/skills/review-yaml-record/SKILL.md` | `1 / 1` (`full`) | `reviews/structured/20261023T160013Z-rifampicin-record-review/review.yaml` | `4a5a4f2482953dc74e3b2329ea69ce4ceaea26d7a65afb171c9b7a9c8deafa01` |
| `20261023T160534Z-frozen-inventory-cohort-review` | `category` | `.claude/skills/review-yaml-category/SKILL.md` | `2969 / 2969` (`full`) | `reviews/structured/20261023T160534Z-frozen-inventory-cohort-review/review.yaml` | `2f9c0a7c11ce7ad5bce970fa342ac0714dd78b6c8e25c6f9422b8422b4a75e8b` |

## Stable Findings Summary (4 Open for Stage 5 Remediation, 8 Deferred)

| Finding ID | Status | Severity | Target Count | Summary & Stage 5 / Deferral Disposition |
| --- | --- | --- | --- | --- |
| `rifampicin-moa-scope-leftover` | `open` | `major` | `1` | Rifampicin retains seeder leftover mode_of_action_target_scope: HOST_SHARED_TARGET — Queued for Stage 5 grouped remediation. |
| `seeded-causal-graphs-missing-primary-targets` | `open` | `major` | `4` | Four SEEDED EXACT records with settled MoA and causal_graphs lack PRIMARY_LITERATURE molecular_targets — Queued for Stage 5 grouped remediation. |
| `seeded-causal-graphs-unsettled-moa-and-targets` | `open` | `major` | `6` | Six SEEDED EXACT records with primary-literature causal_graphs lack settled MoA and PRIMARY_LITERATURE molecular_targets — Queued for Stage 5 grouped remediation. |
| `unreviewed-seeded-pdb-structural-observations` | `open` | `minor` | `3` | Three SEEDED records carry ChEBI-seeded PDB structural_observations with relevance: UNREVIEWED — Queued for Stage 5 grouped remediation. |
| `mcr43-context` | `deferred` | `major` | `2` | Contrasting functional contexts and component-specific grounding for MCR-4.3 remain unresolved — Source-owned qualification notes are already projected via curation/card_evidence_reviews.json; component-specific experimental grounding requires external primary experimental data not available in local cached sources. |
| `eatav-compound` | `deferred` | `major` | `1` | Tested pleuromutilin derivative (tiamulin) in eatAv study does not ground parent pleuromutilin — Derivative-versus-parent qualification note is already projected via curation/card_evidence_reviews.json; exact parent pleuromutilin experimental testing is absent from the cited primary study. |
| `msrc-evidence` | `deferred` | `minor` | `2` | Early msrC association study does not establish exclusive causality or target-protection mechanism — Awaits later primary mechanistic evidence curation and native gene-field representation on source-owned ResistanceMechanismEntry items. |
| `ddl-scope` | `deferred` | `minor` | `1` | Generic D-Ala-D-Ala ligase reference on vancomycin leaves tested alteration unresolved — Full-text primary results for PMID:11266628 remain unavailable under publisher HTTP 403 access hold; experimental allele identity cannot be inferred from abstract or review text. |
| `mexjk-role-conflict` | `deferred` | `major` | `4` | Upstream CARD aro.owl reverses MexJ and MexK component roles in MexJK-OpmH relative to MexJK-OprM — Primary papers PMID:12193619 and PMID:12951344 remain under publisher HTTP 403 hold, and generated AntibioticRecord files do not store subcomponent role restrictions; preserved without guessing which upstream CARD restriction is correct. |
| `reviewed-records-awaiting-causal-graphs` | `deferred` | `minor` | `40` | 39 REVIEWED records await primary-literature causal_graphs and ofloxacin is blocked by structureless CHEBI:7731 — Curating new multi-step primary-literature causal_graphs across 39 additional compounds and resolving upstream ChEBI structure availability for racemic CHEBI:7731 are multi-cycle corpus expansion tasks outside bounded Stage 5 coherence remediation. |
| `proposed-antibacterial-records-awaiting-grounding-and-mechanism` | `deferred` | `minor` | `60` | 60 PROPOSED literature-seeded antibacterial records await primary mechanism curation and structure registration — Requires compound-by-compound primary mechanism literature retrieval and upstream ChEBI structure registration across future dedicated curation cycles. |
| `minted-aro-records-without-exact-chebi-structure` | `deferred` | `informational` | `240` | 240 SEEDED MINTED records lack an exact single-molecule ChEBI chemical_structure — REVIEWED promotion is intentionally gated by structure_completeness_audit until exact single-molecule ChEBI structures or complex-mixture policy support is available. |

## Limitations & Guardrails

- Stage 4 is strictly read-only with respect to scientific YAML records (`data/antibiotics/**/*.yaml`); all open findings are preserved for Stage 5 (`review_remediation`).
- Publisher HTTP 403 holds on `PMID:11266628`, `PMID:12193619`, and `PMID:12951344` remain in force and were not retried.
- Stage 4 is the first stage in Cycle 1 that produces a `GoalEvidence` (`ReviewReport`) manifest; `reviews/workflow/latest.yaml` is only updated after Stage 4 closure is verified by the supervisor.
