# Cycle 8 Stage 5 post-remediation review of 15 remediated AntibioticRecord files (Issues #1359, #1360, #1361)

- Review: 20261109T155000Z-cycle8-stage5-remediated-records-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-11-09T15:45:00Z
- Finished UTC: 2026-11-09T15:50:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Post-remediation batch review of the 15 AntibioticRecord YAML files updated in Cycle 8 Stage 5 to resolve all 3 open Stage 4 record and category review findings: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion (Issue #1359, 6 records: alanylclavam CHEBI:81029, amicetin CHEBI:199652, andrimid CHEBI:216634 including companion single-record review 20261109T120000Z-andrimid-record-review, bottromycin A2 CHEBI:202006, planosporicin CHEBI:226796, and ajudazol A CHEBI:204968), cycle8-stage1-proposed-exact-natural-products-missing-mechanism-and-targets (Issue #1360, 4 records: TP-1161 CHEBI:217619, 2-formyloxymethylclavam CHEBI:81025, 2-hydroxymethylclavam CHEBI:81026, and clavam-2-carboxylate CHEBI:81027), and seeded-exact-rifamycins-and-elfamycins-with-card-only-targets-awaiting-primary-literature-promotion (Issue #1361, 5 records: rifabutin CHEBI:45367, rifaximin CHEBI:75246, rifapentine CHEBI:45304, GE2270A CHEBI:29584, and pulvomycin CHEBI:29668). Verified that all 15 EXACT ChEBI records carry complete single-molecule chemical_structure, curated biosynthesis_origin, curator-verified mode_of_action and mode_of_action_target_scope, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (with reviewed Swiss-Prot UniProtKB protein_examples on andrimid [UniProtKB:P0ABD5, UniProtKB:P0A9Q5], the 3 rifamycins [UniProtKB:P0A8V2, UniProtKB:P9WGY9], and the 2 elfamycins [UniProtKB:P0CE47], and documented held_targets rationales on the 9 non-protein molecular_targets in curation/uniprot_protein_examples.yaml), and are promoted to curation_status: REVIEWED (raising corpus REVIEWED count from 159 to 174 and reducing the review-readiness worklist from 2,966 to 2,951).

## Scope And Provenance

Complete post-remediation review of all 15 AntibioticRecord YAML files modified in Cycle 8 Stage 5 across resolved finding groups 1-3 (Issues #1359, #1360, #1361).

Selection: All 15 records in Cycle 8 Stage 5 resolved finding groups (Issues #1359, #1360, #1361).
Coverage: full; 15 reviewed / 15 in the declared population.
Source: working_tree at Git base 0b7380c610b9c07b8858c5e748ca724218b76f55.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:81029 | data/antibiotics/antibacterial/alanylclavam.yaml | maintained | alanylclavam |
| CHEBI:199652 | data/antibiotics/antibacterial/amicetin.yaml | maintained | amicetin |
| CHEBI:216634 | data/antibiotics/antibacterial/andrimid.yaml | maintained | andrimid |
| CHEBI:202006 | data/antibiotics/antibacterial/bottromycin-a2.yaml | maintained | bottromycin A2 |
| CHEBI:226796 | data/antibiotics/antibacterial/planosporicin.yaml | maintained | planosporicin |
| CHEBI:204968 | data/antibiotics/antifungal/ajudazol-a.yaml | maintained | ajudazol A |
| CHEBI:217619 | data/antibiotics/antibacterial/tp-1161.yaml | maintained | TP-1161 |
| CHEBI:81025 | data/antibiotics/antifungal/2-formyloxymethylclavam.yaml | maintained | 2-formyloxymethylclavam |
| CHEBI:81026 | data/antibiotics/antifungal/2-hydroxymethylclavam.yaml | maintained | 2-hydroxymethylclavam |
| CHEBI:81027 | data/antibiotics/antifungal/clavam-2-carboxylate.yaml | maintained | clavam-2-carboxylate |
| CHEBI:45367 | data/antibiotics/antibacterial/rifabutin.yaml | maintained | rifabutin |
| CHEBI:75246 | data/antibiotics/antibacterial/rifaximin.yaml | maintained | rifaximin |
| CHEBI:45304 | data/antibiotics/antimycobacterial/rifapentine.yaml | maintained | rifapentine |
| CHEBI:29584 | data/antibiotics/antibacterial/ge2270a.yaml | maintained | GE2270A |
| CHEBI:29668 | data/antibiotics/antibacterial/pulvomycin.yaml | maintained | pulvomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and OAK ontology-label validation | passed | True | CHEBI:81029, CHEBI:199652, CHEBI:216634, CHEBI:202006, CHEBI:226796, CHEBI:204968, CHEBI:217619, CHEBI:81025, CHEBI:81026, CHEBI:81027, CHEBI:45367, CHEBI:75246, CHEBI:45304, CHEBI:29584, CHEBI:29668 | All 3,125 corpus records, including the 15 remediated records, pass closed LinkML schema validation and OAK label correspondence with 0 errors. |
| Full corpus seed reproduction check | passed | True | CHEBI:81029, CHEBI:199652, CHEBI:216634, CHEBI:202006, CHEBI:226796, CHEBI:204968, CHEBI:217619, CHEBI:81025, CHEBI:81026, CHEBI:81027, CHEBI:45367, CHEBI:75246, CHEBI:45304, CHEBI:29584, CHEBI:29668 | All 3,125 records reproduce byte-for-byte from data/raw/ plus curator inputs with 0 missing, 0 unexpected, and 0 drifted fields. |
| UniProt protein examples and causal graphs curation test suites | passed | True | CHEBI:81029, CHEBI:199652, CHEBI:216634, CHEBI:202006, CHEBI:226796, CHEBI:204968, CHEBI:217619, CHEBI:81025, CHEBI:81026, CHEBI:81027, CHEBI:45367, CHEBI:75246, CHEBI:45304, CHEBI:29584, CHEBI:29668 | All tests across test_uniprot_protein_examples.py, test_causal_graphs_curation.py, test_embeddings.py, test_corpus_integrity.py, and test_record_review_contract.py pass with exit code 0. |

## Scientific And Domain Assessments

### Promotion of 6 PROPOSED+EXACT records (alanylclavam, amicetin, andrimid, bottromycin A2, planosporicin, ajudazol A) with complete mechanism and target curation to REVIEWED

completeness: supported. Targets: CHEBI:81029, CHEBI:199652, CHEBI:216634, CHEBI:202006, CHEBI:226796, CHEBI:204968.

All 6 Group 1 records (alanylclavam CHEBI:81029, amicetin CHEBI:199652, andrimid CHEBI:216634, bottromycin A2 CHEBI:202006, planosporicin CHEBI:226796, and ajudazol A CHEBI:204968) carry exact single-molecule ChEBI structures, curated biosynthesis_origin (NATURAL_PRODUCT), curator-settled mode_of_action and mode_of_action_target_scope, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (with reviewed Swiss-Prot UniProtKB protein_examples P0ABD5/P0A9Q5 on andrimid and documented held_targets rationales on the other 5 records in curation/uniprot_protein_examples.yaml), and are promoted to curation_status: REVIEWED with PROMOTED_TO_REVIEWED curation events.

### Population of mode_of_action, PRIMARY_LITERATURE molecular_targets, and REVIEWED promotion on 4 Cycle 8 Stage 1 EXACT natural products

completeness: supported. Targets: CHEBI:217619, CHEBI:81025, CHEBI:81026, CHEBI:81027.

All 4 Cycle 8 Stage 1 EXACT natural-product records (TP-1161 CHEBI:217619, 2-formyloxymethylclavam CHEBI:81025, 2-hydroxymethylclavam CHEBI:81026, and clavam-2-carboxylate CHEBI:81027) now carry curated mode_of_action, mode_of_action_target_scope, CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (documented in curation/uniprot_protein_examples.yaml held_targets), and are promoted to curation_status: REVIEWED.

### Population of PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples, and REVIEWED promotion on 5 SEEDED/EXACT rifamycins and elfamycins

completeness: supported. Targets: CHEBI:45367, CHEBI:75246, CHEBI:45304, CHEBI:29584, CHEBI:29668.

All 5 Group 3 EXACT rifamycin and elfamycin records (rifabutin CHEBI:45367, rifaximin CHEBI:75246, rifapentine CHEBI:45304, GE2270A CHEBI:29584, and pulvomycin CHEBI:29668) now carry curated biosynthesis_origin (SEMISYNTHETIC on the 3 rifamycins; NATURAL_PRODUCT on the 2 elfamycins), MICROBIAL_TARGET mode_of_action_target_scope, CURATOR mode_of_action_notes (NUCLEIC_ACID_SYNTHESIS_INHIBITION or PROTEIN_SYNTHESIS_INHIBITION), and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) bacterial DNA-directed RNA polymerase beta-subunit (RpoB; GO:0003899) or bacterial translation elongation factor Tu (EF-Tu / TufA; GO:0003746) molecular_targets with 8 reviewed Swiss-Prot UniProtKB protein_examples (UniProtKB:P0A8V2 rpoB in E. coli K-12 and UniProtKB:P9WGY9 rpoB in M. tuberculosis H37Rv on each of the 3 rifamycins; UniProtKB:P0CE47 tufA in E. coli K-12 on each of the 2 elfamycins) while preserving their CARD_ARO molecular_targets, and are promoted from SEEDED to REVIEWED.

## Findings

### proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion: Promoted 6 PROPOSED+EXACT records (alanylclavam, amicetin, andrimid, bottromycin A2, planosporicin, ajudazol A) with complete primary mechanism and target curation to REVIEWED

major / resolved / confirmed; issue key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion.

Promoted CHEBI:81029 (alanylclavam), CHEBI:199652 (amicetin), CHEBI:216634 (andrimid), CHEBI:202006 (bottromycin A2), CHEBI:226796 (planosporicin), and CHEBI:204968 (ajudazol A) from PROPOSED to REVIEWED via record_curation_event (PROMOTED_TO_REVIEWED) and write_validated_antibiotic, and registered their held_records entries in curation/causal_graphs.yaml.

Disposition: Resolved in Cycle 8 Stage 5 (Issue #1359): promoted alanylclavam (CHEBI:81029), amicetin (CHEBI:199652), andrimid (CHEBI:216634), bottromycin A2 (CHEBI:202006), planosporicin (CHEBI:226796), and ajudazol A (CHEBI:204968) from PROPOSED to REVIEWED.

### cycle8-stage1-proposed-exact-natural-products-missing-mechanism-and-targets: Populated mode_of_action, PRIMARY_LITERATURE molecular_targets, and promoted 4 Cycle 8 Stage 1 EXACT natural products to REVIEWED

major / resolved / confirmed; issue key: cycle8-stage1-proposed-exact-natural-products-missing-mechanism-and-targets.

Curated mode_of_action, mode_of_action_target_scope, CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (with all 4 non-protein targets documented in curation/uniprot_protein_examples.yaml held_targets), and promoted all 4 records from PROPOSED to REVIEWED via record_curation_event and write_validated_antibiotic.

Disposition: Resolved in Cycle 8 Stage 5 (Issue #1360): curated mode_of_action and PRIMARY_LITERATURE molecular_targets and promoted all 4 Cycle 8 Stage 1 EXACT natural products to REVIEWED.

### seeded-exact-rifamycins-and-elfamycins-with-card-only-targets-awaiting-primary-literature-promotion: Populated PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples, and promoted 5 EXACT rifamycins and elfamycins to REVIEWED

major / resolved / confirmed; issue key: seeded-exact-rifamycins-and-elfamycins-with-card-only-targets-awaiting-primary-literature-promotion.

Curated biosynthesis_origin (SEMISYNTHETIC on rifabutin, rifaximin, rifapentine; NATURAL_PRODUCT on GE2270A, pulvomycin), MICROBIAL_TARGET mode_of_action_target_scope, CURATOR mode_of_action_notes (NUCLEIC_ACID_SYNTHESIS_INHIBITION or PROTEIN_SYNTHESIS_INHIBITION), and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) bacterial DNA-directed RNA polymerase beta-subunit (RpoB; GO:0003899) or bacterial translation elongation factor Tu (EF-Tu / TufA; GO:0003746) molecular_targets with 8 reviewed Swiss-Prot UniProtKB protein_examples (UniProtKB:P0A8V2 and UniProtKB:P9WGY9 on the 3 rifamycins; UniProtKB:P0CE47 on the 2 elfamycins) across rifabutin (CHEBI:45367), rifaximin (CHEBI:75246), rifapentine (CHEBI:45304), GE2270A (CHEBI:29584), and pulvomycin (CHEBI:29668) via apply_uniprot_examples_plan while preserving CARD_ARO molecular_targets, and promoted all 5 records from SEEDED to REVIEWED via record_curation_event and write_validated_antibiotic.

Disposition: Resolved in Cycle 8 Stage 5 (Issue #1361): populated PRIMARY_LITERATURE molecular_targets and reviewed UniProtKB protein_examples and promoted all 5 EXACT ChEBI rifamycins and elfamycins to REVIEWED.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| remediated-records-content | curation/record_review_queue.tsv; 15 remediated YAML records and refreshed review-readiness worklist (2,951 items) | supports | All 15 records were updated through native validated writers (write_validated_antibiotic, apply_uniprot_examples_plan, record_curation_event): 6 Group 1 PROPOSED/EXACT records (alanylclavam CHEBI:81029, amicetin CHEBI:199652, andrimid CHEBI:216634, bottromycin A2 CHEBI:202006, planosporicin CHEBI:226796, ajudazol A CHEBI:204968) promoted to REVIEWED; 4 Group 2 Cycle 8 Stage 1 PROPOSED/EXACT natural products (TP-1161 CHEBI:217619, 2-formyloxymethylclavam CHEBI:81025, 2-hydroxymethylclavam CHEBI:81026, clavam-2-carboxylate CHEBI:81027) populated with curated mode_of_action and PRIMARY_LITERATURE molecular_targets (documented in curation/uniprot_protein_examples.yaml held_targets) and promoted to REVIEWED; and 5 Group 3 SEEDED/EXACT rifamycins and elfamycins (rifabutin CHEBI:45367, rifaximin CHEBI:75246, rifapentine CHEBI:45304, GE2270A CHEBI:29584, pulvomycin CHEBI:29668) populated with curated biosynthesis_origin, MICROBIAL_TARGET mode_of_action, and PRIMARY_LITERATURE molecular_targets (GO:0003899 RpoB or GO:0003746 EF-Tu) with 8 reviewed Swiss-Prot UniProtKB protein_examples (UniProtKB:P0A8V2 and UniProtKB:P9WGY9 on the 3 rifamycins; UniProtKB:P0CE47 on the 2 elfamycins) while preserving CARD_ARO molecular_targets and promoted to REVIEWED (raising corpus REVIEWED count from 159 to 174 and reducing the review-readiness queue from 2,966 to 2,951). |
| validate-strict-pass | scripts/validate_strict.py; 3125 files scanned, 0 files with ERROR, 0 total ERROR rows | supports | Closed-mode LinkML validation and OAK ontology label verification pass across all 3,125 records. |
| verify-corpus-pass | scripts/verify_corpus.py; records expected: 3125, on disk: 3125, missing: 0, unexpected: 0, drifted fields: 0 | supports | Every curator-owned edit on the 15 remediated records survives seed_from_sources.py reproduction without drift. |
| primary-literature-sources | PMID:10681345, PMID:6833138, PMID:22267658, PMID:15066985, PMID:16866529, PMID:19115340, PMID:22293474, PMID:23021914, PMID:23475977, PMID:17469849, PMID:19301921, PMID:15112964, PMID:20432424, PMID:20562278, PMID:20929206, PMID:10223939, PMID:15950068, PMID:1936373, PMID:28121985, PMID:7541225, PMID:9774383, PMID:16616535, PMID:9515709, PMID:16303766; Primary experimental mechanism and target studies cited across the 15 remediated records | supports | Primary studies support REVIEWED promotion on the 6 Group 1 records (alanylclavam PMID:10681345, PMID:6833138; amicetin PMID:22267658, DOI:10.1021/ja01098a518; andrimid PMID:15066985, PMID:16866529; bottromycin A2 PMID:19115340, PMID:22293474, PMID:23021914; planosporicin PMID:23475977, PMID:17469849, PMID:19301921; ajudazol A PMID:15112964, PMID:20432424), mode_of_action, PRIMARY_LITERATURE molecular_targets, and REVIEWED promotion on the 4 Cycle 8 Stage 1 natural products (TP-1161 PMID:20562278, PMID:20929206; 2-formyloxymethylclavam, 2-hydroxymethylclavam, and clavam-2-carboxylate PMID:10681345, PMID:10223939, DOI:10.1039/c39790000282), and PRIMARY_LITERATURE bacterial RpoB (GO:0003899) and EF-Tu (GO:0003746) molecular_targets with reviewed Swiss-Prot UniProtKB protein_examples (UniProtKB:P0A8V2, UniProtKB:P9WGY9, UniProtKB:P0CE47) and REVIEWED promotion on the 5 SEEDED/EXACT rifamycins and elfamycins (rifabutin PMID:15950068, PMID:1936373; rifaximin PMID:28121985, PMID:7541225; rifapentine PMID:15950068, PMID:9774383; GE2270A PMID:16616535, PMID:9515709; pulvomycin PMID:16616535, PMID:16303766). |

## Limits And Additional Notes

- All 15 newly promoted REVIEWED records are registered in curation/causal_graphs.yaml held_records (bringing total held_records to 78) awaiting multi-step primary-literature causal_graphs in a subsequent Stage 2 goal.
- Original Cycle 8 Stage 4 review bundles (20261109T120000Z-andrimid-record-review and 20261109T120100Z-cycle8-frozen-inventory-cohort-review) are preserved byte-for-byte.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T155000Z-cycle8-stage5-remediated-records-review
kind: batch
repository: CultureBotAI/AntibioticMech
title: 'Cycle 8 Stage 5 post-remediation review of 15 remediated AntibioticRecord
  files (Issues #1359, #1360, #1361)'
started_at: '2026-11-09T15:45:00Z'
finished_at: '2026-11-09T15:50:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Cycle 8 Stage 5 post-remediation verification review of the
    15 remediated records prior to independent adversarial PR review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass
native_verdict: PASS
scientific_review: true
summary: 'Post-remediation batch review of the 15 AntibioticRecord YAML files updated
  in Cycle 8 Stage 5 to resolve all 3 open Stage 4 record and category review findings:
  proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion (Issue #1359,
  6 records: alanylclavam CHEBI:81029, amicetin CHEBI:199652, andrimid CHEBI:216634
  including companion single-record review 20261109T120000Z-andrimid-record-review,
  bottromycin A2 CHEBI:202006, planosporicin CHEBI:226796, and ajudazol A CHEBI:204968),
  cycle8-stage1-proposed-exact-natural-products-missing-mechanism-and-targets (Issue
  #1360, 4 records: TP-1161 CHEBI:217619, 2-formyloxymethylclavam CHEBI:81025, 2-hydroxymethylclavam
  CHEBI:81026, and clavam-2-carboxylate CHEBI:81027), and seeded-exact-rifamycins-and-elfamycins-with-card-only-targets-awaiting-primary-literature-promotion
  (Issue #1361, 5 records: rifabutin CHEBI:45367, rifaximin CHEBI:75246, rifapentine
  CHEBI:45304, GE2270A CHEBI:29584, and pulvomycin CHEBI:29668). Verified that all
  15 EXACT ChEBI records carry complete single-molecule chemical_structure, curated
  biosynthesis_origin, curator-verified mode_of_action and mode_of_action_target_scope,
  and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets
  (with reviewed Swiss-Prot UniProtKB protein_examples on andrimid [UniProtKB:P0ABD5,
  UniProtKB:P0A9Q5], the 3 rifamycins [UniProtKB:P0A8V2, UniProtKB:P9WGY9], and the
  2 elfamycins [UniProtKB:P0CE47], and documented held_targets rationales on the 9
  non-protein molecular_targets in curation/uniprot_protein_examples.yaml), and are
  promoted to curation_status: REVIEWED (raising corpus REVIEWED count from 159 to
  174 and reducing the review-readiness worklist from 2,966 to 2,951).'
source:
  git_revision: 0b7380c610b9c07b8858c5e748ca724218b76f55
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
    sha256: 07aec03fe019218b87a7fa0cc310820b46f1c6af2aa4562aa9b5dbe52885d498
  - path: curation/curator_antibiotics.tsv
    role: context
    sha256: cae7471ab358d3d8a4529198dd8d99206176e53cd94ba05e5f458b69a634a45d
  - path: curation/cycle8_stage5_review_remediation_transition.json
    role: context
    sha256: c9c6235beab6941d1af90bc318da98f2240f4c8bff83a4ee7c0026127b90b9e7
  - path: curation/record_review_queue.tsv
    role: context
    sha256: 91aa57f1cd2dec3cb751555e31a077f8e783291bc293073976ff33db87093f19
  - path: curation/uniprot_protein_examples.yaml
    role: context
    sha256: c39f5eee35d652d2a0a409632a21fe87ca4e68e7dcebc7348df0a2206bd0c016
  - path: curation/uniprot_protein_examples_transition.json
    role: context
    sha256: 48b5f467ca7c684032866839bef7455e84310640b52abee9b25da865df312fcc
  - path: data/antibiotics/antibacterial/alanylclavam.yaml
    role: target
    sha256: 837286a6fefb3031b7c90cabcd1acc4c0de507ea618a5a241376257dc8f8cd3d
  - path: data/antibiotics/antibacterial/amicetin.yaml
    role: target
    sha256: cb2ace2f9ecb51c242d27741656c1ea07fcfaa008d528c7b050f4b259e1b2795
  - path: data/antibiotics/antibacterial/andrimid.yaml
    role: target
    sha256: 7b53657676806be127b35ff3f789a95c965f26ce61a51fffc934824b41dd85ba
  - path: data/antibiotics/antibacterial/bottromycin-a2.yaml
    role: target
    sha256: 6b7d848697f11747c550a21a9ee6097693c1253b3f4debe048c30ba29eb6b381
  - path: data/antibiotics/antibacterial/ge2270a.yaml
    role: target
    sha256: 9fe69a1b2a3ab324fdbd2dc86a6b26d06cb57f4cba82d1be20ec57da44602d5c
  - path: data/antibiotics/antibacterial/planosporicin.yaml
    role: target
    sha256: dc8ca260e5a33a7e47f4466fbc27ab555af81c1156f5ea86963ea240e356455f
  - path: data/antibiotics/antibacterial/pulvomycin.yaml
    role: target
    sha256: dd19e0248b22c9ad4a52d3493014616f6bb4d1d8570ff9987f1a7c031ae342e1
  - path: data/antibiotics/antibacterial/rifabutin.yaml
    role: target
    sha256: 4d5e40d7b47344fb9178238d7a7f2328fc0834f910b27801625907e235fdde88
  - path: data/antibiotics/antibacterial/rifaximin.yaml
    role: target
    sha256: c1fb640c8314ac8fe7e57317b4d7dbd249aae25aef65fd9fbca66636444c1b4f
  - path: data/antibiotics/antibacterial/tp-1161.yaml
    role: target
    sha256: 5e8787757547242e735e82c85af4652b4183840eccbf08b05547599256cfb0bb
  - path: data/antibiotics/antifungal/2-formyloxymethylclavam.yaml
    role: target
    sha256: be575e1b8bcc47a76f32ecd8294fdab5f9ffee78729478b530362c831a419da0
  - path: data/antibiotics/antifungal/2-hydroxymethylclavam.yaml
    role: target
    sha256: 7cd16d2b018cbebccd9e6be0433b9ba6c5cd8a39ac1011714b918fc80c48a0d6
  - path: data/antibiotics/antifungal/ajudazol-a.yaml
    role: target
    sha256: 883671b70e306bd11421159df71831e8a9da2809bd50b71f387b57d5a8ac8fc3
  - path: data/antibiotics/antifungal/clavam-2-carboxylate.yaml
    role: target
    sha256: 6f17e10dc9b9c9d20d80d0d1a5f7eccc1a7c44d784582cd3a117fe65f1da00cf
  - path: data/antibiotics/antimycobacterial/rifapentine.yaml
    role: target
    sha256: a3b3f0aec413293d176bfdb44db07b4310cbec8971451e44b89c741a5ebdcb0f
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
  description: 'Complete post-remediation review of all 15 AntibioticRecord YAML files
    modified in Cycle 8 Stage 5 across resolved finding groups 1-3 (Issues #1359,
    #1360, #1361).'
  selection: 'All 15 records in Cycle 8 Stage 5 resolved finding groups (Issues #1359,
    #1360, #1361).'
  coverage: full
  population_size: 15
  reviewed_target_ids:
  - CHEBI:81029
  - CHEBI:199652
  - CHEBI:216634
  - CHEBI:202006
  - CHEBI:226796
  - CHEBI:204968
  - CHEBI:217619
  - CHEBI:81025
  - CHEBI:81026
  - CHEBI:81027
  - CHEBI:45367
  - CHEBI:75246
  - CHEBI:45304
  - CHEBI:29584
  - CHEBI:29668
targets:
- target_id: CHEBI:81029
  path: data/antibiotics/antibacterial/alanylclavam.yaml
  label: alanylclavam
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/alanylclavam.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:199652
  path: data/antibiotics/antibacterial/amicetin.yaml
  label: amicetin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/amicetin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:216634
  path: data/antibiotics/antibacterial/andrimid.yaml
  label: andrimid
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/andrimid.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:202006
  path: data/antibiotics/antibacterial/bottromycin-a2.yaml
  label: bottromycin A2
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/bottromycin-a2.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:226796
  path: data/antibiotics/antibacterial/planosporicin.yaml
  label: planosporicin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/planosporicin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:204968
  path: data/antibiotics/antifungal/ajudazol-a.yaml
  label: ajudazol A
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antifungal/ajudazol-a.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:217619
  path: data/antibiotics/antibacterial/tp-1161.yaml
  label: TP-1161
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/tp-1161.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:81025
  path: data/antibiotics/antifungal/2-formyloxymethylclavam.yaml
  label: 2-formyloxymethylclavam
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antifungal/2-formyloxymethylclavam.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:81026
  path: data/antibiotics/antifungal/2-hydroxymethylclavam.yaml
  label: 2-hydroxymethylclavam
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antifungal/2-hydroxymethylclavam.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:81027
  path: data/antibiotics/antifungal/clavam-2-carboxylate.yaml
  label: clavam-2-carboxylate
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antifungal/clavam-2-carboxylate.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:45367
  path: data/antibiotics/antibacterial/rifabutin.yaml
  label: rifabutin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/rifabutin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:75246
  path: data/antibiotics/antibacterial/rifaximin.yaml
  label: rifaximin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/rifaximin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:45304
  path: data/antibiotics/antimycobacterial/rifapentine.yaml
  label: rifapentine
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antimycobacterial/rifapentine.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:29584
  path: data/antibiotics/antibacterial/ge2270a.yaml
  label: GE2270A
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/ge2270a.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:29668
  path: data/antibiotics/antibacterial/pulvomycin.yaml
  label: pulvomycin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/pulvomycin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
checks:
- check_id: strict-schema-remediated-records
  name: Closed-schema and OAK ontology-label validation
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py
  exit_code: 0
  summary: All 3,125 corpus records, including the 15 remediated records, pass closed
    LinkML schema validation and OAK label correspondence with 0 errors.
  target_ids:
  - CHEBI:81029
  - CHEBI:199652
  - CHEBI:216634
  - CHEBI:202006
  - CHEBI:226796
  - CHEBI:204968
  - CHEBI:217619
  - CHEBI:81025
  - CHEBI:81026
  - CHEBI:81027
  - CHEBI:45367
  - CHEBI:75246
  - CHEBI:45304
  - CHEBI:29584
  - CHEBI:29668
  evidence_ids:
  - validate-strict-pass
  - remediated-records-content
- check_id: corpus-reproduction-remediated-records
  name: Full corpus seed reproduction check
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py
  exit_code: 0
  summary: All 3,125 records reproduce byte-for-byte from data/raw/ plus curator inputs
    with 0 missing, 0 unexpected, and 0 drifted fields.
  target_ids:
  - CHEBI:81029
  - CHEBI:199652
  - CHEBI:216634
  - CHEBI:202006
  - CHEBI:226796
  - CHEBI:204968
  - CHEBI:217619
  - CHEBI:81025
  - CHEBI:81026
  - CHEBI:81027
  - CHEBI:45367
  - CHEBI:75246
  - CHEBI:45304
  - CHEBI:29584
  - CHEBI:29668
  evidence_ids:
  - verify-corpus-pass
  - remediated-records-content
- check_id: uniprot-and-causal-graphs-pytest
  name: UniProt protein examples and causal graphs curation test suites
  status: passed
  required: true
  command: .venv/bin/python -m pytest -q tests/test_uniprot_protein_examples.py tests/test_causal_graphs_curation.py
    tests/test_embeddings.py tests/test_corpus_integrity.py tests/test_record_review_contract.py
  exit_code: 0
  summary: All tests across test_uniprot_protein_examples.py, test_causal_graphs_curation.py,
    test_embeddings.py, test_corpus_integrity.py, and test_record_review_contract.py
    pass with exit code 0.
  target_ids:
  - CHEBI:81029
  - CHEBI:199652
  - CHEBI:216634
  - CHEBI:202006
  - CHEBI:226796
  - CHEBI:204968
  - CHEBI:217619
  - CHEBI:81025
  - CHEBI:81026
  - CHEBI:81027
  - CHEBI:45367
  - CHEBI:75246
  - CHEBI:45304
  - CHEBI:29584
  - CHEBI:29668
  evidence_ids:
  - remediated-records-content
evidence:
- evidence_id: remediated-records-content
  kind: record_content
  reference: curation/record_review_queue.tsv
  locator: 15 remediated YAML records and refreshed review-readiness worklist (2,951
    items)
  accessed_at: '2026-11-09T15:48:00Z'
  support: supports
  snapshot_sha256: 91aa57f1cd2dec3cb751555e31a077f8e783291bc293073976ff33db87093f19
  summary: 'All 15 records were updated through native validated writers (write_validated_antibiotic,
    apply_uniprot_examples_plan, record_curation_event): 6 Group 1 PROPOSED/EXACT
    records (alanylclavam CHEBI:81029, amicetin CHEBI:199652, andrimid CHEBI:216634,
    bottromycin A2 CHEBI:202006, planosporicin CHEBI:226796, ajudazol A CHEBI:204968)
    promoted to REVIEWED; 4 Group 2 Cycle 8 Stage 1 PROPOSED/EXACT natural products
    (TP-1161 CHEBI:217619, 2-formyloxymethylclavam CHEBI:81025, 2-hydroxymethylclavam
    CHEBI:81026, clavam-2-carboxylate CHEBI:81027) populated with curated mode_of_action
    and PRIMARY_LITERATURE molecular_targets (documented in curation/uniprot_protein_examples.yaml
    held_targets) and promoted to REVIEWED; and 5 Group 3 SEEDED/EXACT rifamycins
    and elfamycins (rifabutin CHEBI:45367, rifaximin CHEBI:75246, rifapentine CHEBI:45304,
    GE2270A CHEBI:29584, pulvomycin CHEBI:29668) populated with curated biosynthesis_origin,
    MICROBIAL_TARGET mode_of_action, and PRIMARY_LITERATURE molecular_targets (GO:0003899
    RpoB or GO:0003746 EF-Tu) with 8 reviewed Swiss-Prot UniProtKB protein_examples
    (UniProtKB:P0A8V2 and UniProtKB:P9WGY9 on the 3 rifamycins; UniProtKB:P0CE47 on
    the 2 elfamycins) while preserving CARD_ARO molecular_targets and promoted to
    REVIEWED (raising corpus REVIEWED count from 159 to 174 and reducing the review-readiness
    queue from 2,966 to 2,951).'
- evidence_id: validate-strict-pass
  kind: validation
  reference: scripts/validate_strict.py
  locator: 3125 files scanned, 0 files with ERROR, 0 total ERROR rows
  accessed_at: '2026-11-09T15:49:00Z'
  support: supports
  snapshot_sha256: d70e6739c881260927dfc99abea16e56be0f34f353f9f95353a43da76e8e7217
  summary: Closed-mode LinkML validation and OAK ontology label verification pass
    across all 3,125 records.
- evidence_id: verify-corpus-pass
  kind: validation
  reference: scripts/verify_corpus.py
  locator: 'records expected: 3125, on disk: 3125, missing: 0, unexpected: 0, drifted
    fields: 0'
  accessed_at: '2026-11-09T15:49:00Z'
  support: supports
  snapshot_sha256: 7d881f9b4e17b02d7f3ec3eb48404ad0a41a0cefa915edc9a442f755b834df78
  summary: Every curator-owned edit on the 15 remediated records survives seed_from_sources.py
    reproduction without drift.
- evidence_id: primary-literature-sources
  kind: primary_source
  reference: PMID:10681345, PMID:6833138, PMID:22267658, PMID:15066985, PMID:16866529,
    PMID:19115340, PMID:22293474, PMID:23021914, PMID:23475977, PMID:17469849, PMID:19301921,
    PMID:15112964, PMID:20432424, PMID:20562278, PMID:20929206, PMID:10223939, PMID:15950068,
    PMID:1936373, PMID:28121985, PMID:7541225, PMID:9774383, PMID:16616535, PMID:9515709,
    PMID:16303766
  locator: Primary experimental mechanism and target studies cited across the 15 remediated
    records
  accessed_at: '2026-11-09T15:48:00Z'
  support: supports
  summary: Primary studies support REVIEWED promotion on the 6 Group 1 records (alanylclavam
    PMID:10681345, PMID:6833138; amicetin PMID:22267658, DOI:10.1021/ja01098a518;
    andrimid PMID:15066985, PMID:16866529; bottromycin A2 PMID:19115340, PMID:22293474,
    PMID:23021914; planosporicin PMID:23475977, PMID:17469849, PMID:19301921; ajudazol
    A PMID:15112964, PMID:20432424), mode_of_action, PRIMARY_LITERATURE molecular_targets,
    and REVIEWED promotion on the 4 Cycle 8 Stage 1 natural products (TP-1161 PMID:20562278,
    PMID:20929206; 2-formyloxymethylclavam, 2-hydroxymethylclavam, and clavam-2-carboxylate
    PMID:10681345, PMID:10223939, DOI:10.1039/c39790000282), and PRIMARY_LITERATURE
    bacterial RpoB (GO:0003899) and EF-Tu (GO:0003746) molecular_targets with reviewed
    Swiss-Prot UniProtKB protein_examples (UniProtKB:P0A8V2, UniProtKB:P9WGY9, UniProtKB:P0CE47)
    and REVIEWED promotion on the 5 SEEDED/EXACT rifamycins and elfamycins (rifabutin
    PMID:15950068, PMID:1936373; rifaximin PMID:28121985, PMID:7541225; rifapentine
    PMID:15950068, PMID:9774383; GE2270A PMID:16616535, PMID:9515709; pulvomycin PMID:16616535,
    PMID:16303766).
assessments:
- assessment_id: group1-six-proposed-exact-records-promoted-to-reviewed
  area: completeness
  topic: Promotion of 6 PROPOSED+EXACT records (alanylclavam, amicetin, andrimid,
    bottromycin A2, planosporicin, ajudazol A) with complete mechanism and target
    curation to REVIEWED
  outcome: supported
  summary: 'All 6 Group 1 records (alanylclavam CHEBI:81029, amicetin CHEBI:199652,
    andrimid CHEBI:216634, bottromycin A2 CHEBI:202006, planosporicin CHEBI:226796,
    and ajudazol A CHEBI:204968) carry exact single-molecule ChEBI structures, curated
    biosynthesis_origin (NATURAL_PRODUCT), curator-settled mode_of_action and mode_of_action_target_scope,
    and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets
    (with reviewed Swiss-Prot UniProtKB protein_examples P0ABD5/P0A9Q5 on andrimid
    and documented held_targets rationales on the other 5 records in curation/uniprot_protein_examples.yaml),
    and are promoted to curation_status: REVIEWED with PROMOTED_TO_REVIEWED curation
    events.'
  target_ids:
  - CHEBI:81029
  - CHEBI:199652
  - CHEBI:216634
  - CHEBI:202006
  - CHEBI:226796
  - CHEBI:204968
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
- assessment_id: group2-cycle8-stage1-natural-products-moa-targets-and-reviewed
  area: completeness
  topic: Population of mode_of_action, PRIMARY_LITERATURE molecular_targets, and REVIEWED
    promotion on 4 Cycle 8 Stage 1 EXACT natural products
  outcome: supported
  summary: 'All 4 Cycle 8 Stage 1 EXACT natural-product records (TP-1161 CHEBI:217619,
    2-formyloxymethylclavam CHEBI:81025, 2-hydroxymethylclavam CHEBI:81026, and clavam-2-carboxylate
    CHEBI:81027) now carry curated mode_of_action, mode_of_action_target_scope, CURATOR
    mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE)
    molecular_targets (documented in curation/uniprot_protein_examples.yaml held_targets),
    and are promoted to curation_status: REVIEWED.'
  target_ids:
  - CHEBI:217619
  - CHEBI:81025
  - CHEBI:81026
  - CHEBI:81027
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
- assessment_id: group3-seeded-exact-rifamycins-and-elfamycins-primary-targets-and-reviewed
  area: completeness
  topic: Population of PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples,
    and REVIEWED promotion on 5 SEEDED/EXACT rifamycins and elfamycins
  outcome: supported
  summary: 'All 5 Group 3 EXACT rifamycin and elfamycin records (rifabutin CHEBI:45367,
    rifaximin CHEBI:75246, rifapentine CHEBI:45304, GE2270A CHEBI:29584, and pulvomycin
    CHEBI:29668) now carry curated biosynthesis_origin (SEMISYNTHETIC on the 3 rifamycins;
    NATURAL_PRODUCT on the 2 elfamycins), MICROBIAL_TARGET mode_of_action_target_scope,
    CURATOR mode_of_action_notes (NUCLEIC_ACID_SYNTHESIS_INHIBITION or PROTEIN_SYNTHESIS_INHIBITION),
    and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) bacterial DNA-directed
    RNA polymerase beta-subunit (RpoB; GO:0003899) or bacterial translation elongation
    factor Tu (EF-Tu / TufA; GO:0003746) molecular_targets with 8 reviewed Swiss-Prot
    UniProtKB protein_examples (UniProtKB:P0A8V2 rpoB in E. coli K-12 and UniProtKB:P9WGY9
    rpoB in M. tuberculosis H37Rv on each of the 3 rifamycins; UniProtKB:P0CE47 tufA
    in E. coli K-12 on each of the 2 elfamycins) while preserving their CARD_ARO molecular_targets,
    and are promoted from SEEDED to REVIEWED.'
  target_ids:
  - CHEBI:45367
  - CHEBI:75246
  - CHEBI:45304
  - CHEBI:29584
  - CHEBI:29668
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
  title: Promoted 6 PROPOSED+EXACT records (alanylclavam, amicetin, andrimid, bottromycin
    A2, planosporicin, ajudazol A) with complete primary mechanism and target curation
    to REVIEWED
  description: Promoted CHEBI:81029 (alanylclavam), CHEBI:199652 (amicetin), CHEBI:216634
    (andrimid), CHEBI:202006 (bottromycin A2), CHEBI:226796 (planosporicin), and CHEBI:204968
    (ajudazol A) from PROPOSED to REVIEWED via record_curation_event (PROMOTED_TO_REVIEWED)
    and write_validated_antibiotic, and registered their held_records entries in curation/causal_graphs.yaml.
  target_ids:
  - CHEBI:81029
  - CHEBI:199652
  - CHEBI:216634
  - CHEBI:202006
  - CHEBI:226796
  - CHEBI:204968
  field_paths:
  - curation_status
  - curation_history
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/alanylclavam.yaml
    role: Curator-owned curation_status and curation_history
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/amicetin.yaml
    role: Curator-owned curation_status and curation_history
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/andrimid.yaml
    role: Curator-owned curation_status and curation_history
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/bottromycin-a2.yaml
    role: Curator-owned curation_status and curation_history
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/planosporicin.yaml
    role: Curator-owned curation_status and curation_history
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antifungal/ajudazol-a.yaml
    role: Curator-owned curation_status and curation_history
  disposition_reason: 'Resolved in Cycle 8 Stage 5 (Issue #1359): promoted alanylclavam
    (CHEBI:81029), amicetin (CHEBI:199652), andrimid (CHEBI:216634), bottromycin A2
    (CHEBI:202006), planosporicin (CHEBI:226796), and ajudazol A (CHEBI:204968) from
    PROPOSED to REVIEWED.'
  previous_occurrences:
  - repository: CultureBotAI/AntibioticMech
    review_id: 20261109T120100Z-cycle8-frozen-inventory-cohort-review
    finding_id: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion
  - repository: CultureBotAI/AntibioticMech
    review_id: 20261109T120000Z-andrimid-record-review
    finding_id: andrimid-awaiting-reviewed-promotion
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1359
- finding_id: cycle8-stage1-proposed-exact-natural-products-missing-mechanism-and-targets
  issue_key: cycle8-stage1-proposed-exact-natural-products-missing-mechanism-and-targets
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Populated mode_of_action, PRIMARY_LITERATURE molecular_targets, and promoted
    4 Cycle 8 Stage 1 EXACT natural products to REVIEWED
  description: 'Curated mode_of_action, mode_of_action_target_scope, CURATOR mode_of_action_notes,
    and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets
    (with all 4 non-protein targets documented in curation/uniprot_protein_examples.yaml
    held_targets), and promoted all 4 records from PROPOSED to REVIEWED via record_curation_event
    and write_validated_antibiotic.'
  target_ids:
  - CHEBI:217619
  - CHEBI:81025
  - CHEBI:81026
  - CHEBI:81027
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
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/tp-1161.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antifungal/2-formyloxymethylclavam.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antifungal/2-hydroxymethylclavam.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antifungal/clavam-2-carboxylate.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  disposition_reason: 'Resolved in Cycle 8 Stage 5 (Issue #1360): curated mode_of_action
    and PRIMARY_LITERATURE molecular_targets and promoted all 4 Cycle 8 Stage 1 EXACT
    natural products to REVIEWED.'
  previous_occurrences:
  - repository: CultureBotAI/AntibioticMech
    review_id: 20261109T120100Z-cycle8-frozen-inventory-cohort-review
    finding_id: cycle8-stage1-proposed-exact-natural-products-missing-mechanism-and-targets
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1360
- finding_id: seeded-exact-rifamycins-and-elfamycins-with-card-only-targets-awaiting-primary-literature-promotion
  issue_key: seeded-exact-rifamycins-and-elfamycins-with-card-only-targets-awaiting-primary-literature-promotion
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Populated PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples,
    and promoted 5 EXACT rifamycins and elfamycins to REVIEWED
  description: 'Curated biosynthesis_origin (SEMISYNTHETIC on rifabutin, rifaximin,
    rifapentine; NATURAL_PRODUCT on GE2270A, pulvomycin), MICROBIAL_TARGET mode_of_action_target_scope,
    CURATOR mode_of_action_notes (NUCLEIC_ACID_SYNTHESIS_INHIBITION or PROTEIN_SYNTHESIS_INHIBITION),
    and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) bacterial DNA-directed
    RNA polymerase beta-subunit (RpoB; GO:0003899) or bacterial translation elongation
    factor Tu (EF-Tu / TufA; GO:0003746) molecular_targets with 8 reviewed Swiss-Prot
    UniProtKB protein_examples (UniProtKB:P0A8V2 and UniProtKB:P9WGY9 on the 3 rifamycins;
    UniProtKB:P0CE47 on the 2 elfamycins) across rifabutin (CHEBI:45367), rifaximin
    (CHEBI:75246), rifapentine (CHEBI:45304), GE2270A (CHEBI:29584), and pulvomycin
    (CHEBI:29668) via apply_uniprot_examples_plan while preserving CARD_ARO molecular_targets,
    and promoted all 5 records from SEEDED to REVIEWED via record_curation_event and
    write_validated_antibiotic.'
  target_ids:
  - CHEBI:45367
  - CHEBI:75246
  - CHEBI:45304
  - CHEBI:29584
  - CHEBI:29668
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
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/rifabutin.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/rifaximin.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antimycobacterial/rifapentine.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/ge2270a.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/pulvomycin.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  disposition_reason: 'Resolved in Cycle 8 Stage 5 (Issue #1361): populated PRIMARY_LITERATURE
    molecular_targets and reviewed UniProtKB protein_examples and promoted all 5 EXACT
    ChEBI rifamycins and elfamycins to REVIEWED.'
  previous_occurrences:
  - repository: CultureBotAI/AntibioticMech
    review_id: 20261109T120100Z-cycle8-frozen-inventory-cohort-review
    finding_id: seeded-exact-rifamycins-and-elfamycins-with-card-only-targets-awaiting-primary-literature-promotion
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1361
actions: []
limitations:
- All 15 newly promoted REVIEWED records are registered in curation/causal_graphs.yaml
  held_records (bringing total held_records to 78) awaiting multi-step primary-literature
  causal_graphs in a subsequent Stage 2 goal.
notes:
- Original Cycle 8 Stage 4 review bundles (20261109T120000Z-andrimid-record-review
  and 20261109T120100Z-cycle8-frozen-inventory-cohort-review) are preserved byte-for-byte.
related_reviews:
- repository: CultureBotAI/AntibioticMech
  review_id: 20261109T120000Z-andrimid-record-review
  relationship: Predecessor Cycle 8 Stage 4 single-record review of andrimid (CHEBI:216634)
- repository: CultureBotAI/AntibioticMech
  review_id: 20261109T120100Z-cycle8-frozen-inventory-cohort-review
  relationship: Predecessor Cycle 8 Stage 4 full-inventory cohort review identifying
    the 3 resolved finding groups
tags:
- batch-review
- cycle-08
- stage-05
- remediation-verification
```
