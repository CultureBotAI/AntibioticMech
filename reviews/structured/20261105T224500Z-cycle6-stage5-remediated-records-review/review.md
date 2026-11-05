# Cycle 6 Stage 5 post-remediation review of 18 remediated AntibioticRecord files (Issues #1333, #1334, #1335)

- Review: 20261105T224500Z-cycle6-stage5-remediated-records-review
- Repository: culturebotai/AntibioticMech
- Started UTC: 2026-11-05T22:35:00Z
- Finished UTC: 2026-11-05T22:45:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Post-remediation batch review of the 18 AntibioticRecord YAML files updated in Cycle 6 Stage 5 to resolve all 3 open Stage 4 record and category review findings: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion (Issue #1333, 8 records: berninamycin A CHEBI:199044, berninamycin B CHEBI:205987, empedopeptin CHEBI:222785, laterocidine CHEBI:219296, obafluorin CHEBI:199965 including companion single-record review 20261105T153000Z-obafluorin-record-review, salinamide A CHEBI:227666, salinamide B CHEBI:200517, and rimocidin CHEBI:80106), cycle6-stage1-proposed-exact-natural-products-missing-mechanism-and-targets (Issue #1334, 5 records: kendomycin B CHEBI:225841, marinopyrrole C CHEBI:201881, marinopyrrole D CHEBI:206310, marinopyrrole E CHEBI:199931, and amipurimycin CHEBI:223870), and seeded-exact-sulfonamides-with-card-only-targets-awaiting-primary-literature-promotion (Issue #1335, 5 records: sulfacetamide CHEBI:63845, sulfamethazine CHEBI:102265, sulfamethizole CHEBI:9331, sulfamethoxazole CHEBI:9332, and sulfadiazine CHEBI:9328). Verified that all 18 EXACT ChEBI records carry complete single-molecule chemical_structure, curated biosynthesis_origin, curator-verified mode_of_action and mode_of_action_target_scope, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (with reviewed Swiss-Prot UniProtKB protein_examples on obafluorin [UniProtKB:P0A8M3], salinamide A and salinamide B [UniProtKB:P0A8V2, UniProtKB:P0A8T7], and all 5 sulfonamides [UniProtKB:P0AC13], and documented held_targets rationales on berninamycin A, berninamycin B, empedopeptin, laterocidine, rimocidin, kendomycin B, marinopyrrole C, marinopyrrole D, marinopyrrole E, and amipurimycin in curation/uniprot_protein_examples.yaml), and are promoted to curation_status: REVIEWED (raising corpus REVIEWED count from 127 to 145 and reducing the review-readiness worklist from 2,959 to 2,941).

## Scope And Provenance

Complete post-remediation review of all 18 AntibioticRecord YAML files modified in Cycle 6 Stage 5 across resolved finding groups 1-3 (Issues #1333, #1334, #1335).

Selection: All 18 records in Cycle 6 Stage 5 resolved finding groups (Issues #1333, #1334, #1335).
Coverage: full; 18 reviewed / 18 in the declared population.
Source: working_tree at Git base af42b28d22241e4b3fb4d1c7f246339075426f0f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:199044 | data/antibiotics/antibacterial/berninamycin-a.yaml | maintained | berninamycin A |
| CHEBI:205987 | data/antibiotics/antibacterial/berninamycin-b.yaml | maintained | berninamycin B |
| CHEBI:222785 | data/antibiotics/antibacterial/empedopeptin.yaml | maintained | empedopeptin |
| CHEBI:219296 | data/antibiotics/antibacterial/laterocidine.yaml | maintained | laterocidine |
| CHEBI:199965 | data/antibiotics/antibacterial/obafluorin.yaml | maintained | obafluorin |
| CHEBI:227666 | data/antibiotics/antibacterial/salinamide-a.yaml | maintained | salinamide A |
| CHEBI:200517 | data/antibiotics/antibacterial/salinamide-b.yaml | maintained | salinamide B |
| CHEBI:80106 | data/antibiotics/antifungal/rimocidin.yaml | maintained | rimocidin |
| CHEBI:225841 | data/antibiotics/antibacterial/kendomycin-b.yaml | maintained | kendomycin B |
| CHEBI:201881 | data/antibiotics/antibacterial/marinopyrrole-c.yaml | maintained | marinopyrrole C |
| CHEBI:206310 | data/antibiotics/antibacterial/marinopyrrole-d.yaml | maintained | marinopyrrole D |
| CHEBI:199931 | data/antibiotics/antibacterial/marinopyrrole-e.yaml | maintained | marinopyrrole E |
| CHEBI:223870 | data/antibiotics/antifungal/amipurimycin.yaml | maintained | amipurimycin |
| CHEBI:63845 | data/antibiotics/antibacterial/sulfacetamide.yaml | maintained | sulfacetamide |
| CHEBI:102265 | data/antibiotics/antibacterial/sulfamethazine.yaml | maintained | sulfamethazine |
| CHEBI:9331 | data/antibiotics/antibacterial/sulfamethizole.yaml | maintained | sulfamethizole |
| CHEBI:9332 | data/antibiotics/antibacterial/sulfamethoxazole.yaml | maintained | sulfamethoxazole |
| CHEBI:9328 | data/antibiotics/antiprotozoal/sulfadiazine.yaml | maintained | sulfadiazine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and OAK ontology-label validation | passed | True | CHEBI:199044, CHEBI:205987, CHEBI:222785, CHEBI:219296, CHEBI:199965, CHEBI:227666, CHEBI:200517, CHEBI:80106, CHEBI:225841, CHEBI:201881, CHEBI:206310, CHEBI:199931, CHEBI:223870, CHEBI:63845, CHEBI:102265, CHEBI:9331, CHEBI:9332, CHEBI:9328 | All 3,086 corpus records, including the 18 remediated records, pass closed LinkML schema validation and OAK label correspondence with 0 errors. |
| Full corpus seed reproduction check | passed | True | CHEBI:199044, CHEBI:205987, CHEBI:222785, CHEBI:219296, CHEBI:199965, CHEBI:227666, CHEBI:200517, CHEBI:80106, CHEBI:225841, CHEBI:201881, CHEBI:206310, CHEBI:199931, CHEBI:223870, CHEBI:63845, CHEBI:102265, CHEBI:9331, CHEBI:9332, CHEBI:9328 | All 3,086 records reproduce byte-for-byte from data/raw/ plus curator inputs with 0 missing, 0 unexpected, and 0 drifted fields. |
| UniProt protein examples and causal graphs curation test suites | passed | True | CHEBI:199044, CHEBI:205987, CHEBI:222785, CHEBI:219296, CHEBI:199965, CHEBI:227666, CHEBI:200517, CHEBI:80106, CHEBI:225841, CHEBI:201881, CHEBI:206310, CHEBI:199931, CHEBI:223870, CHEBI:63845, CHEBI:102265, CHEBI:9331, CHEBI:9332, CHEBI:9328 | All tests across test_uniprot_protein_examples.py, test_causal_graphs_curation.py, test_review_readiness_queue.py, and test_embeddings.py pass with exit code 0. |

## Scientific And Domain Assessments

### Promotion of 8 PROPOSED+EXACT records (berninamycin A, berninamycin B, empedopeptin, laterocidine, obafluorin, salinamide A, salinamide B, rimocidin) with complete mechanism and target curation to REVIEWED

completeness: supported. Targets: CHEBI:199044, CHEBI:205987, CHEBI:222785, CHEBI:219296, CHEBI:199965, CHEBI:227666, CHEBI:200517, CHEBI:80106.

All 8 Group 1 records (berninamycin A CHEBI:199044, berninamycin B CHEBI:205987, empedopeptin CHEBI:222785, laterocidine CHEBI:219296, obafluorin CHEBI:199965, salinamide A CHEBI:227666, salinamide B CHEBI:200517, and rimocidin CHEBI:80106) carry exact single-molecule ChEBI structures, curated biosynthesis_origin (NATURAL_PRODUCT), curator-settled mode_of_action and mode_of_action_target_scope (MICROBIAL_TARGET), and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (with reviewed Swiss-Prot UniProtKB protein_examples on obafluorin [UniProtKB:P0A8M3] and salinamide A / salinamide B [UniProtKB:P0A8V2, UniProtKB:P0A8T7], and documented held_targets rationales on berninamycin A, berninamycin B, empedopeptin, laterocidine, and rimocidin in curation/uniprot_protein_examples.yaml), and are promoted to curation_status: REVIEWED with PROMOTED_TO_REVIEWED curation events.

### Population of mode_of_action, PRIMARY_LITERATURE molecular_targets, and REVIEWED promotion on 5 Cycle 6 Stage 1 EXACT natural products

completeness: supported. Targets: CHEBI:225841, CHEBI:201881, CHEBI:206310, CHEBI:199931, CHEBI:223870.

All 5 Cycle 6 Stage 1 EXACT natural-product records (kendomycin B CHEBI:225841, marinopyrrole C CHEBI:201881, marinopyrrole D CHEBI:206310, marinopyrrole E CHEBI:199931, and amipurimycin CHEBI:223870) now carry curated mode_of_action, mode_of_action_target_scope: MICROBIAL_TARGET, CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (BIOLOGICAL_PROCESS, DOWNSTREAM_AFFECTED_PROCESS, NCBITaxon:2 Bacteria on kendomycin B and marinopyrroles C-E; NCBITaxon:4751 Fungi on amipurimycin, with all 5 downstream biological-process targets documented in curation/uniprot_protein_examples.yaml held_targets), and are promoted to curation_status: REVIEWED.

### Population of PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples, and REVIEWED promotion on 5 SEEDED/EXACT sulfonamides

completeness: supported. Targets: CHEBI:63845, CHEBI:102265, CHEBI:9331, CHEBI:9332, CHEBI:9328.

All 5 Group 3 EXACT sulfonamide records (sulfacetamide CHEBI:63845, sulfamethazine CHEBI:102265, sulfamethizole CHEBI:9331, sulfamethoxazole CHEBI:9332, and sulfadiazine CHEBI:9328) now carry biosynthesis_origin: SYNTHETIC, MICROBIAL_TARGET mode_of_action_target_scope, CURATOR mode_of_action_notes (FOLATE_PATHWAY_INHIBITION), and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) bacterial dihydropteroate synthase (FolP / DHPS; GO:0004156) molecular_targets (PROTEIN, DIRECT_BINDING_TARGET, NCBITaxon:2 Bacteria) with 1 reviewed E. coli K-12 Swiss-Prot UniProtKB protein_example per record (UniProtKB:P0AC13 folP; 5 total across the 5 records, citing DOI:10.1128/AAC.15.2.195 / PMID:378102 and DOI:10.1126/science.1214641 / PMID:22383845), and are promoted from SEEDED to REVIEWED.

## Findings

### proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion: Promoted 8 PROPOSED+EXACT records (berninamycin A, berninamycin B, empedopeptin, laterocidine, obafluorin, salinamide A, salinamide B, rimocidin) with complete primary mechanism and target curation to REVIEWED

major / resolved / confirmed; issue key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion.

Promoted CHEBI:199044 (berninamycin A), CHEBI:205987 (berninamycin B), CHEBI:222785 (empedopeptin), CHEBI:219296 (laterocidine), CHEBI:199965 (obafluorin), CHEBI:227666 (salinamide A), CHEBI:200517 (salinamide B), and CHEBI:80106 (rimocidin) from PROPOSED to REVIEWED via record_curation_event (PROMOTED_TO_REVIEWED) and write_validated_antibiotic, and registered their held_records entries in curation/causal_graphs.yaml.

Disposition: Resolved in Cycle 6 Stage 5 (Issue #1333): promoted berninamycin A (CHEBI:199044), berninamycin B (CHEBI:205987), empedopeptin (CHEBI:222785), laterocidine (CHEBI:219296), obafluorin (CHEBI:199965), salinamide A (CHEBI:227666), salinamide B (CHEBI:200517), and rimocidin (CHEBI:80106) from PROPOSED to REVIEWED.

### cycle6-stage1-proposed-exact-natural-products-missing-mechanism-and-targets: Populated mode_of_action, PRIMARY_LITERATURE molecular_targets, and promoted 5 Cycle 6 Stage 1 EXACT natural products to REVIEWED

major / resolved / confirmed; issue key: cycle6-stage1-proposed-exact-natural-products-missing-mechanism-and-targets.

Curated mode_of_action, mode_of_action_target_scope: MICROBIAL_TARGET, CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (BIOLOGICAL_PROCESS, DOWNSTREAM_AFFECTED_PROCESS, with all 5 downstream biological-process targets documented in curation/uniprot_protein_examples.yaml held_targets), and promoted all 5 records from PROPOSED to REVIEWED via record_curation_event and write_validated_antibiotic.

Disposition: Resolved in Cycle 6 Stage 5 (Issue #1334): curated mode_of_action and PRIMARY_LITERATURE molecular_targets and promoted all 5 Cycle 6 Stage 1 EXACT natural products to REVIEWED.

### seeded-exact-sulfonamides-with-card-only-targets-awaiting-primary-literature-promotion: Populated PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples, and promoted 5 EXACT sulfonamides to REVIEWED

major / resolved / confirmed; issue key: seeded-exact-sulfonamides-with-card-only-targets-awaiting-primary-literature-promotion.

Curated biosynthesis_origin: SYNTHETIC, MICROBIAL_TARGET mode_of_action_target_scope, CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) bacterial dihydropteroate synthase (FolP / DHPS; GO:0004156) molecular_targets (PROTEIN, DIRECT_BINDING_TARGET, NCBITaxon:2 Bacteria; DOI:10.1128/AAC.15.2.195 / PMID:378102 and DOI:10.1126/science.1214641 / PMID:22383845) with 5 reviewed E. coli K-12 Swiss-Prot UniProtKB protein_examples (UniProtKB:P0AC13 on each record) across sulfacetamide (CHEBI:63845), sulfamethazine (CHEBI:102265), sulfamethizole (CHEBI:9331), sulfamethoxazole (CHEBI:9332), and sulfadiazine (CHEBI:9328) via apply_uniprot_examples_plan, and promoted all 5 records from SEEDED to REVIEWED via record_curation_event and write_validated_antibiotic.

Disposition: Resolved in Cycle 6 Stage 5 (Issue #1335): populated PRIMARY_LITERATURE molecular_targets and reviewed UniProtKB protein_examples and promoted all 5 EXACT ChEBI sulfonamides to REVIEWED.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| remediated-records-content | curation/record_review_queue.tsv; 18 remediated YAML records and refreshed review-readiness worklist (2,941 items) | supports | All 18 records were updated through native validated writers (write_validated_antibiotic, apply_uniprot_examples_plan, record_curation_event): 8 Group 1 PROPOSED/EXACT records (berninamycin A CHEBI:199044, berninamycin B CHEBI:205987, empedopeptin CHEBI:222785, laterocidine CHEBI:219296, obafluorin CHEBI:199965, salinamide A CHEBI:227666, salinamide B CHEBI:200517, rimocidin CHEBI:80106) promoted to REVIEWED; 5 Group 2 Cycle 6 Stage 1 PROPOSED/EXACT natural products (kendomycin B CHEBI:225841, marinopyrrole C CHEBI:201881, marinopyrrole D CHEBI:206310, marinopyrrole E CHEBI:199931, amipurimycin CHEBI:223870) populated with curated mode_of_action and PRIMARY_LITERATURE molecular_targets (BIOLOGICAL_PROCESS, DOWNSTREAM_AFFECTED_PROCESS, documented in curation/uniprot_protein_examples.yaml held_targets) and promoted to REVIEWED; and 5 Group 3 SEEDED/EXACT sulfonamides (sulfacetamide CHEBI:63845, sulfamethazine CHEBI:102265, sulfamethizole CHEBI:9331, sulfamethoxazole CHEBI:9332, sulfadiazine CHEBI:9328) populated with biosynthesis_origin: SYNTHETIC, MICROBIAL_TARGET mode_of_action, and PRIMARY_LITERATURE molecular_targets (GO:0004156 bacterial dihydropteroate synthase (FolP / DHPS)) with reviewed E. coli K-12 Swiss-Prot UniProtKB protein_examples (UniProtKB:P0AC13 on each record) and promoted to REVIEWED (raising corpus REVIEWED count from 127 to 145 and reducing the review-readiness queue from 2,959 to 2,941). |
| validate-strict-pass | scripts/validate_strict.py; 3086 files scanned, 0 files with ERROR, 0 total ERROR rows | supports | Closed-mode LinkML validation and OAK ontology label verification pass across all 3,086 records. |
| verify-corpus-pass | scripts/verify_corpus.py; records expected: 3086, on disk: 3086, missing: 0, unexpected: 0, drifted fields: 0 | supports | Every curator-owned edit on the 18 remediated records survives seed_from_sources.py reproduction without drift. |
| primary-literature-sources | PMID:4897214, PMID:34617948, PMID:1244374, PMID:22518842, PMID:33918939, PMID:30115920, PMID:28504677, PMID:31675206, PMID:24843001, PMID:26553755, PMID:15031268, PMID:33057790, PMID:34966190, PMID:26795276, PMID:20175538, PMID:37887221, PMID:557042, PMID:30698415, PMID:378102, PMID:22383845; Primary experimental mechanism and target studies cited across the 18 remediated records | supports | Primary studies support REVIEWED promotion on the 8 Group 1 records (berninamycin A DOI:10.1021/bi00836a026 / PMID:4897214 and DOI:10.1039/d1ob01759d / PMID:34617948; berninamycin B DOI:10.1039/d1ob01759d / PMID:34617948 and DOI:10.1021/ja00417a047 / PMID:1244374; empedopeptin DOI:10.1074/jbc.M112.369504 / PMID:22518842 and DOI:10.3390/md19040209 / PMID:33918939; laterocidine DOI:10.1038/s41467-018-05781-6 / PMID:30115920; obafluorin DOI:10.1038/nchembio.2374 / PMID:28504677 and DOI:10.1021/acschembio.9b00590 / PMID:31675206; salinamide A and salinamide B DOI:10.7554/eLife.02451 / PMID:24843001 and DOI:10.1002/anie.201508576 / PMID:26553755; rimocidin DOI:10.1016/j.chembiol.2004.02.017 / PMID:15031268 and DOI:10.1007/s00253-020-10955-8 / PMID:33057790), mode_of_action, PRIMARY_LITERATURE molecular_targets, and REVIEWED promotion on the 5 Cycle 6 Stage 1 natural products (kendomycin B DOI:10.1038/s41429-021-00493-4 / PMID:34966190 and DOI:10.1371/journal.pone.0146165 / PMID:26795276; marinopyrrole C, D, and E DOI:10.1021/NP900834G / PMID:20175538 and DOI:10.3390/antibiotics12101520 / PMID:37887221; amipurimycin DOI:10.7164/antibiotics.30.11 / PMID:557042 and DOI:10.1021/acschembio.8b01076 / PMID:30698415), and PRIMARY_LITERATURE bacterial dihydropteroate synthase (FolP / DHPS; GO:0004156) molecular_targets with reviewed E. coli K-12 UniProtKB:P0AC13 protein_examples and REVIEWED promotion on the 5 EXACT sulfonamides (sulfacetamide, sulfamethazine, sulfamethizole, sulfamethoxazole, and sulfadiazine; DOI:10.1128/AAC.15.2.195 / PMID:378102 and DOI:10.1126/science.1214641 / PMID:22383845). |

## Limits And Additional Notes

- All 18 newly promoted REVIEWED records are registered in curation/causal_graphs.yaml held_records (bringing total held_records to 63) awaiting multi-step primary-literature causal_graphs in a subsequent Stage 2 goal.
- Original Cycle 6 Stage 4 review bundles (20261105T153000Z-obafluorin-record-review and 20261105T153100Z-cycle6-frozen-inventory-cohort-review) are preserved byte-for-byte.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T224500Z-cycle6-stage5-remediated-records-review
kind: batch
repository: culturebotai/AntibioticMech
title: 'Cycle 6 Stage 5 post-remediation review of 18 remediated AntibioticRecord
  files (Issues #1333, #1334, #1335)'
started_at: '2026-11-05T22:35:00Z'
finished_at: '2026-11-05T22:45:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Cycle 6 Stage 5 post-remediation verification review of the
    18 remediated records prior to independent adversarial PR review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass
native_verdict: PASS
scientific_review: true
summary: 'Post-remediation batch review of the 18 AntibioticRecord YAML files updated
  in Cycle 6 Stage 5 to resolve all 3 open Stage 4 record and category review findings:
  proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion (Issue #1333,
  8 records: berninamycin A CHEBI:199044, berninamycin B CHEBI:205987, empedopeptin
  CHEBI:222785, laterocidine CHEBI:219296, obafluorin CHEBI:199965 including companion
  single-record review 20261105T153000Z-obafluorin-record-review, salinamide A CHEBI:227666,
  salinamide B CHEBI:200517, and rimocidin CHEBI:80106), cycle6-stage1-proposed-exact-natural-products-missing-mechanism-and-targets
  (Issue #1334, 5 records: kendomycin B CHEBI:225841, marinopyrrole C CHEBI:201881,
  marinopyrrole D CHEBI:206310, marinopyrrole E CHEBI:199931, and amipurimycin CHEBI:223870),
  and seeded-exact-sulfonamides-with-card-only-targets-awaiting-primary-literature-promotion
  (Issue #1335, 5 records: sulfacetamide CHEBI:63845, sulfamethazine CHEBI:102265,
  sulfamethizole CHEBI:9331, sulfamethoxazole CHEBI:9332, and sulfadiazine CHEBI:9328).
  Verified that all 18 EXACT ChEBI records carry complete single-molecule chemical_structure,
  curated biosynthesis_origin, curator-verified mode_of_action and mode_of_action_target_scope,
  and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets
  (with reviewed Swiss-Prot UniProtKB protein_examples on obafluorin [UniProtKB:P0A8M3],
  salinamide A and salinamide B [UniProtKB:P0A8V2, UniProtKB:P0A8T7], and all 5 sulfonamides
  [UniProtKB:P0AC13], and documented held_targets rationales on berninamycin A, berninamycin
  B, empedopeptin, laterocidine, rimocidin, kendomycin B, marinopyrrole C, marinopyrrole
  D, marinopyrrole E, and amipurimycin in curation/uniprot_protein_examples.yaml),
  and are promoted to curation_status: REVIEWED (raising corpus REVIEWED count from
  127 to 145 and reducing the review-readiness worklist from 2,959 to 2,941).'
source:
  git_revision: af42b28d22241e4b3fb4d1c7f246339075426f0f
  state: working_tree
  inputs:
  - path: .claude/skills/review-yaml-category/SKILL.md
    role: context
    sha256: 4c438f137570d6c75a208422f04c0ad21873f5ee467f230a43ec8ed9709d2178
  - path: .claude/skills/review-yaml-record/SKILL.md
    role: context
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
  - path: curation/causal_graphs.yaml
    role: context
    sha256: a71cfb23c56a97ff2bae5bf86d9e38181ee06f54e1d4cd7f2ac462ee4faa4c48
  - path: curation/curator_antibiotics.tsv
    role: context
    sha256: a75ab22fa81df19ae960865a75cc8246e705a5244a5d826bf61281f32b080553
  - path: curation/cycle6_stage5_review_remediation_transition.json
    role: context
    sha256: 8875be6909fc1757b42d43a776f3187ff1cba96009694cbc80293364f957899e
  - path: curation/record_review_queue.tsv
    role: context
    sha256: b5838d0e92c8afc86451b52b58eb18344bf745811f7058c72aa6cf90685c468e
  - path: curation/uniprot_protein_examples.yaml
    role: context
    sha256: 48924828162b01ed91f4c04bcbe9c91f7a56a31c6fbfb0a1cfd7cc133b0cf9c0
  - path: curation/uniprot_protein_examples_transition.json
    role: context
    sha256: 56f292cb722516c346b6c61a7bc3444f97e524df4abf26cb00a6876931286724
  - path: data/antibiotics/antibacterial/berninamycin-a.yaml
    role: target
    sha256: 7baaf46088351967e0ee09d2c890c3ee7cb61b88b1a682974e3da8bb7c03a855
  - path: data/antibiotics/antibacterial/berninamycin-b.yaml
    role: target
    sha256: 6bb97c2db26dcb4fa9dcefaa78dc3938f6c8fa45f8950c8fbc7dbb8898cc8f04
  - path: data/antibiotics/antibacterial/empedopeptin.yaml
    role: target
    sha256: 92a42b462ef9a409f2a49db6ebd73cb71bece3b2ba7652d5924cb56742e66a86
  - path: data/antibiotics/antibacterial/kendomycin-b.yaml
    role: target
    sha256: 949a33aad6e71a7f45fcc74f82b4cfdb05bb93f225fc9f2ae92e47c66b6a1f98
  - path: data/antibiotics/antibacterial/laterocidine.yaml
    role: target
    sha256: f11cf57ac604dd0dcfdd32b3075c9004320f5bc05410fdc6d624e07031620b32
  - path: data/antibiotics/antibacterial/marinopyrrole-c.yaml
    role: target
    sha256: d2ecd5e69c6ce931cdd68988117813d0560dd2d83e0d20aeaf401dcef8dea0f4
  - path: data/antibiotics/antibacterial/marinopyrrole-d.yaml
    role: target
    sha256: 1ba6dedb2eab17f8d94c0e58ae3a8d97eeb471127061749108364bcafb48818b
  - path: data/antibiotics/antibacterial/marinopyrrole-e.yaml
    role: target
    sha256: 32202e478fa1a62f3693c0d8d7d6889a487c51656793927f4cdcc9b486a533b1
  - path: data/antibiotics/antibacterial/obafluorin.yaml
    role: target
    sha256: cac1385f684a63e63477ab5112f1cd90df21f431b39ca0aee7067a912b850d3e
  - path: data/antibiotics/antibacterial/salinamide-a.yaml
    role: target
    sha256: 93389abc0c2df30718c6fceab9e94ef01dde0c7c0193a16323c67300be388fbc
  - path: data/antibiotics/antibacterial/salinamide-b.yaml
    role: target
    sha256: 5c8f4e389c28974b597053e97428e35ce9c640d16583f147f9fb16a20ec4258d
  - path: data/antibiotics/antibacterial/sulfacetamide.yaml
    role: target
    sha256: 83c5e34cb849868861944beeb068e1d9b88da67b6236dab80af23ee05c57ad02
  - path: data/antibiotics/antibacterial/sulfamethazine.yaml
    role: target
    sha256: e61475e6987567a41015bfb2123cbd1b473454233fdb283870db179a15c4c782
  - path: data/antibiotics/antibacterial/sulfamethizole.yaml
    role: target
    sha256: 656ffa02ba647cb9130a8beb110cfb64de530b20f12afa32f918abeac4476abb
  - path: data/antibiotics/antibacterial/sulfamethoxazole.yaml
    role: target
    sha256: 03d20558eed3fcdee4f9d225dca7d29f4c0707ccc64e8da7234ed9693228c091
  - path: data/antibiotics/antifungal/amipurimycin.yaml
    role: target
    sha256: ab7e691717e82ed339dc4dc2bb6093f60f024368160868bc2e9f3bc89952ad7b
  - path: data/antibiotics/antifungal/rimocidin.yaml
    role: target
    sha256: 6dbd3a758c057b292554758ee33f6d9d6f3606402970d87636decc7316b100c8
  - path: data/antibiotics/antiprotozoal/sulfadiazine.yaml
    role: target
    sha256: 09189b3b5e33f9dfaa81eb8a38b90daaaadd5d23e37c60ab7bd9bff491e5c53e
  - path: scripts/curation_worklist.py
    role: context
    sha256: 692fdcc39a0c8135c89b483a19ab0a428bfac3d851ff67a6a1ceac80225a2430
  - path: scripts/seed_from_sources.py
    role: context
    sha256: 53cf79eb1417ff7758a94f2d18ac1ce47b0f8c91c8961023363cf37698d4a056
  - path: scripts/validate_strict.py
    role: context
    sha256: d70e6739c881260927dfc99abea16e56be0f34f353f9f95353a43da76e8e7217
  - path: scripts/verify_corpus.py
    role: context
    sha256: 7d881f9b4e17b02d7f3ec3eb48404ad0a41a0cefa915edc9a442f755b834df78
  - path: src/antibioticmech/schema/antibioticmech.yaml
    role: context
    sha256: de62be2dd2dd55f141a0c14ff666eaa00efc6f3b431d651d0196ebcfddfbb301
scope:
  description: 'Complete post-remediation review of all 18 AntibioticRecord YAML files
    modified in Cycle 6 Stage 5 across resolved finding groups 1-3 (Issues #1333,
    #1334, #1335).'
  selection: 'All 18 records in Cycle 6 Stage 5 resolved finding groups (Issues #1333,
    #1334, #1335).'
  coverage: full
  population_size: 18
  reviewed_target_ids:
  - CHEBI:199044
  - CHEBI:205987
  - CHEBI:222785
  - CHEBI:219296
  - CHEBI:199965
  - CHEBI:227666
  - CHEBI:200517
  - CHEBI:80106
  - CHEBI:225841
  - CHEBI:201881
  - CHEBI:206310
  - CHEBI:199931
  - CHEBI:223870
  - CHEBI:63845
  - CHEBI:102265
  - CHEBI:9331
  - CHEBI:9332
  - CHEBI:9328
targets:
- target_id: CHEBI:199044
  path: data/antibiotics/antibacterial/berninamycin-a.yaml
  label: berninamycin A
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/berninamycin-a.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:205987
  path: data/antibiotics/antibacterial/berninamycin-b.yaml
  label: berninamycin B
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/berninamycin-b.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:222785
  path: data/antibiotics/antibacterial/empedopeptin.yaml
  label: empedopeptin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/empedopeptin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:219296
  path: data/antibiotics/antibacterial/laterocidine.yaml
  label: laterocidine
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/laterocidine.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:199965
  path: data/antibiotics/antibacterial/obafluorin.yaml
  label: obafluorin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/obafluorin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:227666
  path: data/antibiotics/antibacterial/salinamide-a.yaml
  label: salinamide A
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/salinamide-a.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:200517
  path: data/antibiotics/antibacterial/salinamide-b.yaml
  label: salinamide B
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/salinamide-b.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:80106
  path: data/antibiotics/antifungal/rimocidin.yaml
  label: rimocidin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antifungal/rimocidin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:225841
  path: data/antibiotics/antibacterial/kendomycin-b.yaml
  label: kendomycin B
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/kendomycin-b.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:201881
  path: data/antibiotics/antibacterial/marinopyrrole-c.yaml
  label: marinopyrrole C
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/marinopyrrole-c.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:206310
  path: data/antibiotics/antibacterial/marinopyrrole-d.yaml
  label: marinopyrrole D
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/marinopyrrole-d.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:199931
  path: data/antibiotics/antibacterial/marinopyrrole-e.yaml
  label: marinopyrrole E
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/marinopyrrole-e.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:223870
  path: data/antibiotics/antifungal/amipurimycin.yaml
  label: amipurimycin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antifungal/amipurimycin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:63845
  path: data/antibiotics/antibacterial/sulfacetamide.yaml
  label: sulfacetamide
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sulfacetamide.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:102265
  path: data/antibiotics/antibacterial/sulfamethazine.yaml
  label: sulfamethazine
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sulfamethazine.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:9331
  path: data/antibiotics/antibacterial/sulfamethizole.yaml
  label: sulfamethizole
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sulfamethizole.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:9332
  path: data/antibiotics/antibacterial/sulfamethoxazole.yaml
  label: sulfamethoxazole
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sulfamethoxazole.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:9328
  path: data/antibiotics/antiprotozoal/sulfadiazine.yaml
  label: sulfadiazine
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antiprotozoal/sulfadiazine.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
checks:
- check_id: strict-schema-remediated-records
  name: Closed-schema and OAK ontology-label validation
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py --quiet
  exit_code: 0
  summary: All 3,086 corpus records, including the 18 remediated records, pass closed
    LinkML schema validation and OAK label correspondence with 0 errors.
  target_ids:
  - CHEBI:199044
  - CHEBI:205987
  - CHEBI:222785
  - CHEBI:219296
  - CHEBI:199965
  - CHEBI:227666
  - CHEBI:200517
  - CHEBI:80106
  - CHEBI:225841
  - CHEBI:201881
  - CHEBI:206310
  - CHEBI:199931
  - CHEBI:223870
  - CHEBI:63845
  - CHEBI:102265
  - CHEBI:9331
  - CHEBI:9332
  - CHEBI:9328
  evidence_ids:
  - validate-strict-pass
  - remediated-records-content
- check_id: corpus-reproduction-remediated-records
  name: Full corpus seed reproduction check
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py
  exit_code: 0
  summary: All 3,086 records reproduce byte-for-byte from data/raw/ plus curator inputs
    with 0 missing, 0 unexpected, and 0 drifted fields.
  target_ids:
  - CHEBI:199044
  - CHEBI:205987
  - CHEBI:222785
  - CHEBI:219296
  - CHEBI:199965
  - CHEBI:227666
  - CHEBI:200517
  - CHEBI:80106
  - CHEBI:225841
  - CHEBI:201881
  - CHEBI:206310
  - CHEBI:199931
  - CHEBI:223870
  - CHEBI:63845
  - CHEBI:102265
  - CHEBI:9331
  - CHEBI:9332
  - CHEBI:9328
  evidence_ids:
  - verify-corpus-pass
  - remediated-records-content
- check_id: uniprot-and-causal-graphs-pytest
  name: UniProt protein examples and causal graphs curation test suites
  status: passed
  required: true
  command: .venv/bin/python -m pytest -q tests/test_uniprot_protein_examples.py tests/test_causal_graphs_curation.py
    tests/test_review_readiness_queue.py tests/test_embeddings.py
  exit_code: 0
  summary: All tests across test_uniprot_protein_examples.py, test_causal_graphs_curation.py,
    test_review_readiness_queue.py, and test_embeddings.py pass with exit code 0.
  target_ids:
  - CHEBI:199044
  - CHEBI:205987
  - CHEBI:222785
  - CHEBI:219296
  - CHEBI:199965
  - CHEBI:227666
  - CHEBI:200517
  - CHEBI:80106
  - CHEBI:225841
  - CHEBI:201881
  - CHEBI:206310
  - CHEBI:199931
  - CHEBI:223870
  - CHEBI:63845
  - CHEBI:102265
  - CHEBI:9331
  - CHEBI:9332
  - CHEBI:9328
  evidence_ids:
  - remediated-records-content
evidence:
- evidence_id: remediated-records-content
  kind: record_content
  reference: curation/record_review_queue.tsv
  locator: 18 remediated YAML records and refreshed review-readiness worklist (2,941
    items)
  accessed_at: '2026-11-05T22:40:00Z'
  support: supports
  snapshot_sha256: b5838d0e92c8afc86451b52b58eb18344bf745811f7058c72aa6cf90685c468e
  summary: 'All 18 records were updated through native validated writers (write_validated_antibiotic,
    apply_uniprot_examples_plan, record_curation_event): 8 Group 1 PROPOSED/EXACT
    records (berninamycin A CHEBI:199044, berninamycin B CHEBI:205987, empedopeptin
    CHEBI:222785, laterocidine CHEBI:219296, obafluorin CHEBI:199965, salinamide A
    CHEBI:227666, salinamide B CHEBI:200517, rimocidin CHEBI:80106) promoted to REVIEWED;
    5 Group 2 Cycle 6 Stage 1 PROPOSED/EXACT natural products (kendomycin B CHEBI:225841,
    marinopyrrole C CHEBI:201881, marinopyrrole D CHEBI:206310, marinopyrrole E CHEBI:199931,
    amipurimycin CHEBI:223870) populated with curated mode_of_action and PRIMARY_LITERATURE
    molecular_targets (BIOLOGICAL_PROCESS, DOWNSTREAM_AFFECTED_PROCESS, documented
    in curation/uniprot_protein_examples.yaml held_targets) and promoted to REVIEWED;
    and 5 Group 3 SEEDED/EXACT sulfonamides (sulfacetamide CHEBI:63845, sulfamethazine
    CHEBI:102265, sulfamethizole CHEBI:9331, sulfamethoxazole CHEBI:9332, sulfadiazine
    CHEBI:9328) populated with biosynthesis_origin: SYNTHETIC, MICROBIAL_TARGET mode_of_action,
    and PRIMARY_LITERATURE molecular_targets (GO:0004156 bacterial dihydropteroate
    synthase (FolP / DHPS)) with reviewed E. coli K-12 Swiss-Prot UniProtKB protein_examples
    (UniProtKB:P0AC13 on each record) and promoted to REVIEWED (raising corpus REVIEWED
    count from 127 to 145 and reducing the review-readiness queue from 2,959 to 2,941).'
- evidence_id: validate-strict-pass
  kind: validation
  reference: scripts/validate_strict.py
  locator: 3086 files scanned, 0 files with ERROR, 0 total ERROR rows
  accessed_at: '2026-11-05T22:41:00Z'
  support: supports
  snapshot_sha256: d70e6739c881260927dfc99abea16e56be0f34f353f9f95353a43da76e8e7217
  summary: Closed-mode LinkML validation and OAK ontology label verification pass
    across all 3,086 records.
- evidence_id: verify-corpus-pass
  kind: validation
  reference: scripts/verify_corpus.py
  locator: 'records expected: 3086, on disk: 3086, missing: 0, unexpected: 0, drifted
    fields: 0'
  accessed_at: '2026-11-05T22:42:00Z'
  support: supports
  snapshot_sha256: 7d881f9b4e17b02d7f3ec3eb48404ad0a41a0cefa915edc9a442f755b834df78
  summary: Every curator-owned edit on the 18 remediated records survives seed_from_sources.py
    reproduction without drift.
- evidence_id: primary-literature-sources
  kind: primary_source
  reference: PMID:4897214, PMID:34617948, PMID:1244374, PMID:22518842, PMID:33918939,
    PMID:30115920, PMID:28504677, PMID:31675206, PMID:24843001, PMID:26553755, PMID:15031268,
    PMID:33057790, PMID:34966190, PMID:26795276, PMID:20175538, PMID:37887221, PMID:557042,
    PMID:30698415, PMID:378102, PMID:22383845
  locator: Primary experimental mechanism and target studies cited across the 18 remediated
    records
  accessed_at: '2026-11-05T22:40:00Z'
  support: supports
  summary: Primary studies support REVIEWED promotion on the 8 Group 1 records (berninamycin
    A DOI:10.1021/bi00836a026 / PMID:4897214 and DOI:10.1039/d1ob01759d / PMID:34617948;
    berninamycin B DOI:10.1039/d1ob01759d / PMID:34617948 and DOI:10.1021/ja00417a047
    / PMID:1244374; empedopeptin DOI:10.1074/jbc.M112.369504 / PMID:22518842 and DOI:10.3390/md19040209
    / PMID:33918939; laterocidine DOI:10.1038/s41467-018-05781-6 / PMID:30115920;
    obafluorin DOI:10.1038/nchembio.2374 / PMID:28504677 and DOI:10.1021/acschembio.9b00590
    / PMID:31675206; salinamide A and salinamide B DOI:10.7554/eLife.02451 / PMID:24843001
    and DOI:10.1002/anie.201508576 / PMID:26553755; rimocidin DOI:10.1016/j.chembiol.2004.02.017
    / PMID:15031268 and DOI:10.1007/s00253-020-10955-8 / PMID:33057790), mode_of_action,
    PRIMARY_LITERATURE molecular_targets, and REVIEWED promotion on the 5 Cycle 6
    Stage 1 natural products (kendomycin B DOI:10.1038/s41429-021-00493-4 / PMID:34966190
    and DOI:10.1371/journal.pone.0146165 / PMID:26795276; marinopyrrole C, D, and
    E DOI:10.1021/NP900834G / PMID:20175538 and DOI:10.3390/antibiotics12101520 /
    PMID:37887221; amipurimycin DOI:10.7164/antibiotics.30.11 / PMID:557042 and DOI:10.1021/acschembio.8b01076
    / PMID:30698415), and PRIMARY_LITERATURE bacterial dihydropteroate synthase (FolP
    / DHPS; GO:0004156) molecular_targets with reviewed E. coli K-12 UniProtKB:P0AC13
    protein_examples and REVIEWED promotion on the 5 EXACT sulfonamides (sulfacetamide,
    sulfamethazine, sulfamethizole, sulfamethoxazole, and sulfadiazine; DOI:10.1128/AAC.15.2.195
    / PMID:378102 and DOI:10.1126/science.1214641 / PMID:22383845).
assessments:
- assessment_id: group1-eight-proposed-exact-records-promoted-to-reviewed
  area: completeness
  topic: Promotion of 8 PROPOSED+EXACT records (berninamycin A, berninamycin B, empedopeptin,
    laterocidine, obafluorin, salinamide A, salinamide B, rimocidin) with complete
    mechanism and target curation to REVIEWED
  outcome: supported
  summary: 'All 8 Group 1 records (berninamycin A CHEBI:199044, berninamycin B CHEBI:205987,
    empedopeptin CHEBI:222785, laterocidine CHEBI:219296, obafluorin CHEBI:199965,
    salinamide A CHEBI:227666, salinamide B CHEBI:200517, and rimocidin CHEBI:80106)
    carry exact single-molecule ChEBI structures, curated biosynthesis_origin (NATURAL_PRODUCT),
    curator-settled mode_of_action and mode_of_action_target_scope (MICROBIAL_TARGET),
    and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets
    (with reviewed Swiss-Prot UniProtKB protein_examples on obafluorin [UniProtKB:P0A8M3]
    and salinamide A / salinamide B [UniProtKB:P0A8V2, UniProtKB:P0A8T7], and documented
    held_targets rationales on berninamycin A, berninamycin B, empedopeptin, laterocidine,
    and rimocidin in curation/uniprot_protein_examples.yaml), and are promoted to
    curation_status: REVIEWED with PROMOTED_TO_REVIEWED curation events.'
  target_ids:
  - CHEBI:199044
  - CHEBI:205987
  - CHEBI:222785
  - CHEBI:219296
  - CHEBI:199965
  - CHEBI:227666
  - CHEBI:200517
  - CHEBI:80106
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
- assessment_id: group2-cycle6-stage1-natural-products-moa-targets-and-reviewed
  area: completeness
  topic: Population of mode_of_action, PRIMARY_LITERATURE molecular_targets, and REVIEWED
    promotion on 5 Cycle 6 Stage 1 EXACT natural products
  outcome: supported
  summary: 'All 5 Cycle 6 Stage 1 EXACT natural-product records (kendomycin B CHEBI:225841,
    marinopyrrole C CHEBI:201881, marinopyrrole D CHEBI:206310, marinopyrrole E CHEBI:199931,
    and amipurimycin CHEBI:223870) now carry curated mode_of_action, mode_of_action_target_scope:
    MICROBIAL_TARGET, CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE
    (evidence_status: PRIMARY_EVIDENCE) molecular_targets (BIOLOGICAL_PROCESS, DOWNSTREAM_AFFECTED_PROCESS,
    NCBITaxon:2 Bacteria on kendomycin B and marinopyrroles C-E; NCBITaxon:4751 Fungi
    on amipurimycin, with all 5 downstream biological-process targets documented in
    curation/uniprot_protein_examples.yaml held_targets), and are promoted to curation_status:
    REVIEWED.'
  target_ids:
  - CHEBI:225841
  - CHEBI:201881
  - CHEBI:206310
  - CHEBI:199931
  - CHEBI:223870
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
- assessment_id: group3-seeded-exact-sulfonamides-primary-targets-and-reviewed
  area: completeness
  topic: Population of PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples,
    and REVIEWED promotion on 5 SEEDED/EXACT sulfonamides
  outcome: supported
  summary: 'All 5 Group 3 EXACT sulfonamide records (sulfacetamide CHEBI:63845, sulfamethazine
    CHEBI:102265, sulfamethizole CHEBI:9331, sulfamethoxazole CHEBI:9332, and sulfadiazine
    CHEBI:9328) now carry biosynthesis_origin: SYNTHETIC, MICROBIAL_TARGET mode_of_action_target_scope,
    CURATOR mode_of_action_notes (FOLATE_PATHWAY_INHIBITION), and source: PRIMARY_LITERATURE
    (evidence_status: PRIMARY_EVIDENCE) bacterial dihydropteroate synthase (FolP /
    DHPS; GO:0004156) molecular_targets (PROTEIN, DIRECT_BINDING_TARGET, NCBITaxon:2
    Bacteria) with 1 reviewed E. coli K-12 Swiss-Prot UniProtKB protein_example per
    record (UniProtKB:P0AC13 folP; 5 total across the 5 records, citing DOI:10.1128/AAC.15.2.195
    / PMID:378102 and DOI:10.1126/science.1214641 / PMID:22383845), and are promoted
    from SEEDED to REVIEWED.'
  target_ids:
  - CHEBI:63845
  - CHEBI:102265
  - CHEBI:9331
  - CHEBI:9332
  - CHEBI:9328
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
findings:
- finding_id: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion
  issue_key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Promoted 8 PROPOSED+EXACT records (berninamycin A, berninamycin B, empedopeptin,
    laterocidine, obafluorin, salinamide A, salinamide B, rimocidin) with complete
    primary mechanism and target curation to REVIEWED
  description: Promoted CHEBI:199044 (berninamycin A), CHEBI:205987 (berninamycin
    B), CHEBI:222785 (empedopeptin), CHEBI:219296 (laterocidine), CHEBI:199965 (obafluorin),
    CHEBI:227666 (salinamide A), CHEBI:200517 (salinamide B), and CHEBI:80106 (rimocidin)
    from PROPOSED to REVIEWED via record_curation_event (PROMOTED_TO_REVIEWED) and
    write_validated_antibiotic, and registered their held_records entries in curation/causal_graphs.yaml.
  target_ids:
  - CHEBI:199044
  - CHEBI:205987
  - CHEBI:222785
  - CHEBI:219296
  - CHEBI:199965
  - CHEBI:227666
  - CHEBI:200517
  - CHEBI:80106
  field_paths:
  - curation_status
  - curation_history
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/berninamycin-a.yaml
    role: Curator-owned curation_status and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/berninamycin-b.yaml
    role: Curator-owned curation_status and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/empedopeptin.yaml
    role: Curator-owned curation_status and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/laterocidine.yaml
    role: Curator-owned curation_status and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/obafluorin.yaml
    role: Curator-owned curation_status and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/salinamide-a.yaml
    role: Curator-owned curation_status and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/salinamide-b.yaml
    role: Curator-owned curation_status and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antifungal/rimocidin.yaml
    role: Curator-owned curation_status and curation_history
  disposition_reason: 'Resolved in Cycle 6 Stage 5 (Issue #1333): promoted berninamycin
    A (CHEBI:199044), berninamycin B (CHEBI:205987), empedopeptin (CHEBI:222785),
    laterocidine (CHEBI:219296), obafluorin (CHEBI:199965), salinamide A (CHEBI:227666),
    salinamide B (CHEBI:200517), and rimocidin (CHEBI:80106) from PROPOSED to REVIEWED.'
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261105T153100Z-cycle6-frozen-inventory-cohort-review
    finding_id: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion
  - repository: culturebotai/AntibioticMech
    review_id: 20261105T153000Z-obafluorin-record-review
    finding_id: obafluorin-awaiting-reviewed-promotion
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1333
- finding_id: cycle6-stage1-proposed-exact-natural-products-missing-mechanism-and-targets
  issue_key: cycle6-stage1-proposed-exact-natural-products-missing-mechanism-and-targets
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Populated mode_of_action, PRIMARY_LITERATURE molecular_targets, and promoted
    5 Cycle 6 Stage 1 EXACT natural products to REVIEWED
  description: 'Curated mode_of_action, mode_of_action_target_scope: MICROBIAL_TARGET,
    CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status:
    PRIMARY_EVIDENCE) molecular_targets (BIOLOGICAL_PROCESS, DOWNSTREAM_AFFECTED_PROCESS,
    with all 5 downstream biological-process targets documented in curation/uniprot_protein_examples.yaml
    held_targets), and promoted all 5 records from PROPOSED to REVIEWED via record_curation_event
    and write_validated_antibiotic.'
  target_ids:
  - CHEBI:225841
  - CHEBI:201881
  - CHEBI:206310
  - CHEBI:199931
  - CHEBI:223870
  field_paths:
  - mode_of_action
  - mode_of_action_target_scope
  - mode_of_action_notes
  - molecular_targets
  - curation_status
  - curation_history
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/kendomycin-b.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/marinopyrrole-c.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/marinopyrrole-d.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/marinopyrrole-e.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antifungal/amipurimycin.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  disposition_reason: 'Resolved in Cycle 6 Stage 5 (Issue #1334): curated mode_of_action
    and PRIMARY_LITERATURE molecular_targets and promoted all 5 Cycle 6 Stage 1 EXACT
    natural products to REVIEWED.'
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261105T153100Z-cycle6-frozen-inventory-cohort-review
    finding_id: cycle6-stage1-proposed-exact-natural-products-missing-mechanism-and-targets
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1334
- finding_id: seeded-exact-sulfonamides-with-card-only-targets-awaiting-primary-literature-promotion
  issue_key: seeded-exact-sulfonamides-with-card-only-targets-awaiting-primary-literature-promotion
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Populated PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples,
    and promoted 5 EXACT sulfonamides to REVIEWED
  description: 'Curated biosynthesis_origin: SYNTHETIC, MICROBIAL_TARGET mode_of_action_target_scope,
    CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status:
    PRIMARY_EVIDENCE) bacterial dihydropteroate synthase (FolP / DHPS; GO:0004156)
    molecular_targets (PROTEIN, DIRECT_BINDING_TARGET, NCBITaxon:2 Bacteria; DOI:10.1128/AAC.15.2.195
    / PMID:378102 and DOI:10.1126/science.1214641 / PMID:22383845) with 5 reviewed
    E. coli K-12 Swiss-Prot UniProtKB protein_examples (UniProtKB:P0AC13 on each record)
    across sulfacetamide (CHEBI:63845), sulfamethazine (CHEBI:102265), sulfamethizole
    (CHEBI:9331), sulfamethoxazole (CHEBI:9332), and sulfadiazine (CHEBI:9328) via
    apply_uniprot_examples_plan, and promoted all 5 records from SEEDED to REVIEWED
    via record_curation_event and write_validated_antibiotic.'
  target_ids:
  - CHEBI:63845
  - CHEBI:102265
  - CHEBI:9331
  - CHEBI:9332
  - CHEBI:9328
  field_paths:
  - biosynthesis_origin
  - mode_of_action
  - mode_of_action_target_scope
  - mode_of_action_notes
  - molecular_targets
  - curation_status
  - curation_history
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sulfacetamide.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sulfamethazine.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sulfamethizole.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sulfamethoxazole.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antiprotozoal/sulfadiazine.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  disposition_reason: 'Resolved in Cycle 6 Stage 5 (Issue #1335): populated PRIMARY_LITERATURE
    molecular_targets and reviewed UniProtKB protein_examples and promoted all 5 EXACT
    ChEBI sulfonamides to REVIEWED.'
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261105T153100Z-cycle6-frozen-inventory-cohort-review
    finding_id: seeded-exact-sulfonamides-with-card-only-targets-awaiting-primary-literature-promotion
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1335
actions: []
limitations:
- All 18 newly promoted REVIEWED records are registered in curation/causal_graphs.yaml
  held_records (bringing total held_records to 63) awaiting multi-step primary-literature
  causal_graphs in a subsequent Stage 2 goal.
notes:
- Original Cycle 6 Stage 4 review bundles (20261105T153000Z-obafluorin-record-review
  and 20261105T153100Z-cycle6-frozen-inventory-cohort-review) are preserved byte-for-byte.
related_reviews:
- repository: culturebotai/AntibioticMech
  review_id: 20261105T153000Z-obafluorin-record-review
  relationship: Predecessor Cycle 6 Stage 4 single-record review of obafluorin (CHEBI:199965)
- repository: culturebotai/AntibioticMech
  review_id: 20261105T153100Z-cycle6-frozen-inventory-cohort-review
  relationship: Predecessor Cycle 6 Stage 4 full-inventory cohort review identifying
    the 3 resolved finding groups
tags:
- batch-review
- cycle-06
- stage-05
- remediation-verification
```
