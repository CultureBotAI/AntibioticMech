# Cycle 7 Stage 5 post-remediation review of 14 remediated AntibioticRecord files (Issues #1345, #1346, #1347)

- Review: 20261108T235000Z-cycle7-stage5-remediated-records-review
- Repository: culturebotai/AntibioticMech
- Started UTC: 2026-11-08T23:45:00Z
- Finished UTC: 2026-11-08T23:50:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Post-remediation batch review of the 14 AntibioticRecord YAML files updated in Cycle 7 Stage 5 to resolve all 3 open Stage 4 record and category review findings: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion (Issue #1345, 3 records: neocarzinostatin CHEBI:29655 including companion single-record review 20261108T210000Z-neocarzinostatin-record-review, streptothricin E CHEBI:67576, and epoxomicin CHEBI:42265), cycle7-stage1-proposed-exact-natural-products-missing-mechanism-and-targets (Issue #1346, 5 records: benastatin A CHEBI:226154, benastatin B CHEBI:200324, tetarimycin A CHEBI:204430, 9-methylstreptimidone CHEBI:215258, and 7-deoxypactamycin CHEBI:198890), and seeded-exact-folate-inhibitors-with-card-only-targets-awaiting-primary-literature-promotion (Issue #1347, 6 records: sulfadoxine CHEBI:9329, sulfasalazine CHEBI:9334, sulfisoxazole CHEBI:102484, dapsone CHEBI:4325, brodimoprim CHEBI:131726, and tetroxoprim CHEBI:135420). Verified that all 14 EXACT ChEBI records carry complete single-molecule chemical_structure, curated biosynthesis_origin, curator-verified mode_of_action and mode_of_action_target_scope, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (with reviewed Swiss-Prot UniProtKB protein_examples on the 4 DHPS inhibitors [UniProtKB:P0AC13] and 2 DHFR inhibitors [UniProtKB:P0ABQ4], and documented held_targets rationales on neocarzinostatin, streptothricin E, epoxomicin, benastatin A, benastatin B, tetarimycin A, 9-methylstreptimidone, and 7-deoxypactamycin in curation/uniprot_protein_examples.yaml), and are promoted to curation_status: REVIEWED (raising corpus REVIEWED count from 145 to 159 and reducing the review-readiness worklist from 2,960 to 2,946).

## Scope And Provenance

Complete post-remediation review of all 14 AntibioticRecord YAML files modified in Cycle 7 Stage 5 across resolved finding groups 1-3 (Issues #1345, #1346, #1347).

Selection: All 14 records in Cycle 7 Stage 5 resolved finding groups (Issues #1345, #1346, #1347).
Coverage: full; 14 reviewed / 14 in the declared population.
Source: working_tree at Git base 8ffffaf75be8d64f0a12e6acc0e7202626c9e2b0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:29655 | data/antibiotics/antibacterial/neocarzinostatin.yaml | maintained | neocarzinostatin |
| CHEBI:67576 | data/antibiotics/antibacterial/streptothricin-e.yaml | maintained | streptothricin E |
| CHEBI:42265 | data/antibiotics/antiprotozoal/epoxomicin.yaml | maintained | epoxomicin |
| CHEBI:226154 | data/antibiotics/antibacterial/benastatin-a.yaml | maintained | benastatin A |
| CHEBI:200324 | data/antibiotics/antibacterial/benastatin-b.yaml | maintained | benastatin B |
| CHEBI:204430 | data/antibiotics/antibacterial/tetarimycin-a.yaml | maintained | tetarimycin A |
| CHEBI:215258 | data/antibiotics/antifungal/9-methylstreptimidone.yaml | maintained | 9-methylstreptimidone |
| CHEBI:198890 | data/antibiotics/antiprotozoal/7-deoxypactamycin.yaml | maintained | 7-deoxypactamycin |
| CHEBI:9329 | data/antibiotics/antibacterial/sulfadoxine.yaml | maintained | sulfadoxine |
| CHEBI:9334 | data/antibiotics/antibacterial/sulfasalazine.yaml | maintained | sulfasalazine |
| CHEBI:102484 | data/antibiotics/antibacterial/sulfisoxazole.yaml | maintained | sulfisoxazole |
| CHEBI:4325 | data/antibiotics/antimycobacterial/dapsone.yaml | maintained | dapsone |
| CHEBI:131726 | data/antibiotics/antibacterial/brodimoprim.yaml | maintained | brodimoprim |
| CHEBI:135420 | data/antibiotics/antibacterial/tetroxoprim.yaml | maintained | tetroxoprim |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and OAK ontology-label validation | passed | True | CHEBI:29655, CHEBI:67576, CHEBI:42265, CHEBI:226154, CHEBI:200324, CHEBI:204430, CHEBI:215258, CHEBI:198890, CHEBI:9329, CHEBI:9334, CHEBI:102484, CHEBI:4325, CHEBI:131726, CHEBI:135420 | All 3,105 corpus records, including the 14 remediated records, pass closed LinkML schema validation and OAK label correspondence with 0 errors. |
| Full corpus seed reproduction check | passed | True | CHEBI:29655, CHEBI:67576, CHEBI:42265, CHEBI:226154, CHEBI:200324, CHEBI:204430, CHEBI:215258, CHEBI:198890, CHEBI:9329, CHEBI:9334, CHEBI:102484, CHEBI:4325, CHEBI:131726, CHEBI:135420 | All 3,105 records reproduce byte-for-byte from data/raw/ plus curator inputs with 0 missing, 0 unexpected, and 0 drifted fields. |
| UniProt protein examples and causal graphs curation test suites | passed | True | CHEBI:29655, CHEBI:67576, CHEBI:42265, CHEBI:226154, CHEBI:200324, CHEBI:204430, CHEBI:215258, CHEBI:198890, CHEBI:9329, CHEBI:9334, CHEBI:102484, CHEBI:4325, CHEBI:131726, CHEBI:135420 | All tests across test_uniprot_protein_examples.py, test_causal_graphs_curation.py, test_embeddings.py, test_corpus_integrity.py, and test_record_review_contract.py pass with exit code 0. |

## Scientific And Domain Assessments

### Promotion of 3 PROPOSED+EXACT records (neocarzinostatin, streptothricin E, epoxomicin) with complete mechanism and target curation to REVIEWED

completeness: supported. Targets: CHEBI:29655, CHEBI:67576, CHEBI:42265.

All 3 Group 1 records (neocarzinostatin CHEBI:29655, streptothricin E CHEBI:67576, and epoxomicin CHEBI:42265) carry exact single-molecule ChEBI structures, curated biosynthesis_origin (NATURAL_PRODUCT), curator-settled mode_of_action and mode_of_action_target_scope, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (with documented held_targets rationales in curation/uniprot_protein_examples.yaml), and are promoted to curation_status: REVIEWED with PROMOTED_TO_REVIEWED curation events.

### Population of mode_of_action, PRIMARY_LITERATURE molecular_targets, and REVIEWED promotion on 5 Cycle 7 Stage 1 EXACT natural products

completeness: supported. Targets: CHEBI:226154, CHEBI:200324, CHEBI:204430, CHEBI:215258, CHEBI:198890.

All 5 Cycle 7 Stage 1 EXACT natural-product records (benastatin A CHEBI:226154, benastatin B CHEBI:200324, tetarimycin A CHEBI:204430, 9-methylstreptimidone CHEBI:215258, and 7-deoxypactamycin CHEBI:198890) now carry curated mode_of_action, mode_of_action_target_scope, CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (documented in curation/uniprot_protein_examples.yaml held_targets), and are promoted to curation_status: REVIEWED.

### Population of PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples, and REVIEWED promotion on 6 SEEDED/EXACT folate inhibitors

completeness: supported. Targets: CHEBI:9329, CHEBI:9334, CHEBI:102484, CHEBI:4325, CHEBI:131726, CHEBI:135420.

All 6 Group 3 EXACT folate-pathway inhibitor records (sulfadoxine CHEBI:9329, sulfasalazine CHEBI:9334, sulfisoxazole CHEBI:102484, dapsone CHEBI:4325, brodimoprim CHEBI:131726, and tetroxoprim CHEBI:135420) now carry biosynthesis_origin: SYNTHETIC, MICROBIAL_TARGET mode_of_action_target_scope, CURATOR mode_of_action_notes (FOLATE_PATHWAY_INHIBITION), and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) bacterial dihydropteroate synthase (FolP / DHPS; GO:0004156) or bacterial dihydrofolate reductase (FolA / DHFR; GO:0004146) molecular_targets with 1 reviewed E. coli K-12 Swiss-Prot UniProtKB protein_example per record (UniProtKB:P0AC13 folP on the 4 DHPS inhibitors and UniProtKB:P0ABQ4 folA on the 2 DHFR inhibitors; 6 total across the 6 records), and are promoted from SEEDED to REVIEWED.

## Findings

### proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion: Promoted 3 PROPOSED+EXACT records (neocarzinostatin, streptothricin E, epoxomicin) with complete primary mechanism and target curation to REVIEWED

major / resolved / confirmed; issue key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion.

Promoted CHEBI:29655 (neocarzinostatin), CHEBI:67576 (streptothricin E), and CHEBI:42265 (epoxomicin) from PROPOSED to REVIEWED via record_curation_event (PROMOTED_TO_REVIEWED) and write_validated_antibiotic, and registered their held_records entries in curation/causal_graphs.yaml.

Disposition: Resolved in Cycle 7 Stage 5 (Issue #1345): promoted neocarzinostatin (CHEBI:29655), streptothricin E (CHEBI:67576), and epoxomicin (CHEBI:42265) from PROPOSED to REVIEWED.

### cycle7-stage1-proposed-exact-natural-products-missing-mechanism-and-targets: Populated mode_of_action, PRIMARY_LITERATURE molecular_targets, and promoted 5 Cycle 7 Stage 1 EXACT natural products to REVIEWED

major / resolved / confirmed; issue key: cycle7-stage1-proposed-exact-natural-products-missing-mechanism-and-targets.

Curated mode_of_action, mode_of_action_target_scope, CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (with all 5 non-protein targets documented in curation/uniprot_protein_examples.yaml held_targets), and promoted all 5 records from PROPOSED to REVIEWED via record_curation_event and write_validated_antibiotic.

Disposition: Resolved in Cycle 7 Stage 5 (Issue #1346): curated mode_of_action and PRIMARY_LITERATURE molecular_targets and promoted all 5 Cycle 7 Stage 1 EXACT natural products to REVIEWED.

### seeded-exact-folate-inhibitors-with-card-only-targets-awaiting-primary-literature-promotion: Populated PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples, and promoted 6 EXACT folate inhibitors to REVIEWED

major / resolved / confirmed; issue key: seeded-exact-folate-inhibitors-with-card-only-targets-awaiting-primary-literature-promotion.

Curated biosynthesis_origin: SYNTHETIC, MICROBIAL_TARGET mode_of_action_target_scope, CURATOR mode_of_action_notes (FOLATE_PATHWAY_INHIBITION), and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) bacterial dihydropteroate synthase (FolP / DHPS; GO:0004156) or bacterial dihydrofolate reductase (FolA / DHFR; GO:0004146) molecular_targets with 6 reviewed E. coli K-12 Swiss-Prot UniProtKB protein_examples (UniProtKB:P0AC13 or UniProtKB:P0ABQ4) across sulfadoxine (CHEBI:9329), sulfasalazine (CHEBI:9334), sulfisoxazole (CHEBI:102484), dapsone (CHEBI:4325), brodimoprim (CHEBI:131726), and tetroxoprim (CHEBI:135420) via apply_uniprot_examples_plan, and promoted all 6 records from SEEDED to REVIEWED via record_curation_event and write_validated_antibiotic.

Disposition: Resolved in Cycle 7 Stage 5 (Issue #1347): populated PRIMARY_LITERATURE molecular_targets and reviewed UniProtKB protein_examples and promoted all 6 EXACT ChEBI folate-pathway inhibitors to REVIEWED.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| remediated-records-content | curation/record_review_queue.tsv; 14 remediated YAML records and refreshed review-readiness worklist (2,946 items) | supports | All 14 records were updated through native validated writers (write_validated_antibiotic, apply_uniprot_examples_plan, record_curation_event): 3 Group 1 PROPOSED/EXACT records (neocarzinostatin CHEBI:29655, streptothricin E CHEBI:67576, epoxomicin CHEBI:42265) promoted to REVIEWED; 5 Group 2 Cycle 7 Stage 1 PROPOSED/EXACT natural products (benastatin A CHEBI:226154, benastatin B CHEBI:200324, tetarimycin A CHEBI:204430, 9-methylstreptimidone CHEBI:215258, 7-deoxypactamycin CHEBI:198890) populated with curated mode_of_action and PRIMARY_LITERATURE molecular_targets (documented in curation/uniprot_protein_examples.yaml held_targets) and promoted to REVIEWED; and 6 Group 3 SEEDED/EXACT folate-pathway inhibitors (sulfadoxine CHEBI:9329, sulfasalazine CHEBI:9334, sulfisoxazole CHEBI:102484, dapsone CHEBI:4325, brodimoprim CHEBI:131726, tetroxoprim CHEBI:135420) populated with biosynthesis_origin: SYNTHETIC, MICROBIAL_TARGET mode_of_action, and PRIMARY_LITERATURE molecular_targets (GO:0004156 FolP or GO:0004146 FolA) with reviewed E. coli K-12 Swiss-Prot UniProtKB protein_examples (UniProtKB:P0AC13 or UniProtKB:P0ABQ4) and promoted to REVIEWED (raising corpus REVIEWED count from 145 to 159 and reducing the review-readiness queue from 2,960 to 2,946). |
| validate-strict-pass | scripts/validate_strict.py; 3105 files scanned, 0 files with ERROR, 0 total ERROR rows | supports | Closed-mode LinkML validation and OAK ontology label verification pass across all 3,105 records. |
| verify-corpus-pass | scripts/verify_corpus.py; records expected: 3105, on disk: 3105, missing: 0, unexpected: 0, drifted fields: 0 | supports | Every curator-owned edit on the 14 remediated records survives seed_from_sources.py reproduction without drift. |
| primary-literature-sources | PMID:15797213, PMID:123897, PMID:2177682, PMID:22820420, PMID:19651911, PMID:24168704, PMID:38664572, PMID:19047004, PMID:23157252, PMID:23438151, PMID:41162067, PMID:21513878, PMID:17827660, PMID:378102, PMID:22383845, PMID:16359642, PMID:391962; Primary experimental mechanism and target studies cited across the 14 remediated records | supports | Primary studies support REVIEWED promotion on the 3 Group 1 records (neocarzinostatin DOI:10.1016/j.chembiol.2004.12.013 / PMID:15797213 and DOI:10.7164/antibiotics.28.229 / PMID:123897; streptothricin E DOI:10.1248/cpb.38.2296 / PMID:2177682 and DOI:10.1038/nchembio.1040 / PMID:22820420; epoxomicin DOI:10.1128/aac.00088-09 / PMID:19651911 and DOI:10.1021/cb400699p / PMID:24168704), mode_of_action, PRIMARY_LITERATURE molecular_targets, and REVIEWED promotion on the 5 Cycle 7 Stage 1 natural products (benastatin A and benastatin B DOI:10.1038/s41429-024-00727-1 / PMID:38664572 and DOI:10.1016/j.jbiotec.2008.10.013 / PMID:19047004; tetarimycin A DOI:10.1021/ja3093828 / PMID:23157252; 9-methylstreptimidone DOI:10.1021/ol400224n / PMID:23438151 and DOI:10.1016/j.pestbp.2025.106683 / PMID:41162067; 7-deoxypactamycin DOI:10.1016/j.chembiol.2011.01.016 / PMID:21513878 and DOI:10.1038/ja.2007.63 / PMID:17827660), and PRIMARY_LITERATURE bacterial FolP (GO:0004156) and FolA (GO:0004146) molecular_targets with reviewed E. coli K-12 UniProtKB:P0AC13 and UniProtKB:P0ABQ4 protein_examples and REVIEWED promotion on the 6 EXACT folate-pathway inhibitors (sulfadoxine, sulfasalazine, sulfisoxazole, dapsone, brodimoprim, and tetroxoprim; DOI:10.1128/AAC.15.2.195 / PMID:378102, DOI:10.1126/science.1214641 / PMID:22383845, DOI:10.1016/j.bcp.2005.10.052 / PMID:16359642, and PMID:391962). |

## Limits And Additional Notes

- All 14 newly promoted REVIEWED records are registered in curation/causal_graphs.yaml held_records (bringing total held_records to 69) awaiting multi-step primary-literature causal_graphs in a subsequent Stage 2 goal.
- Original Cycle 7 Stage 4 review bundles (20261108T210000Z-neocarzinostatin-record-review and 20261108T210100Z-cycle7-frozen-inventory-cohort-review) are preserved byte-for-byte.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261108T235000Z-cycle7-stage5-remediated-records-review
kind: batch
repository: culturebotai/AntibioticMech
title: 'Cycle 7 Stage 5 post-remediation review of 14 remediated AntibioticRecord
  files (Issues #1345, #1346, #1347)'
started_at: '2026-11-08T23:45:00Z'
finished_at: '2026-11-08T23:50:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Cycle 7 Stage 5 post-remediation verification review of the
    14 remediated records prior to independent adversarial PR review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass
native_verdict: PASS
scientific_review: true
summary: 'Post-remediation batch review of the 14 AntibioticRecord YAML files updated
  in Cycle 7 Stage 5 to resolve all 3 open Stage 4 record and category review findings:
  proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion (Issue #1345,
  3 records: neocarzinostatin CHEBI:29655 including companion single-record review
  20261108T210000Z-neocarzinostatin-record-review, streptothricin E CHEBI:67576, and
  epoxomicin CHEBI:42265), cycle7-stage1-proposed-exact-natural-products-missing-mechanism-and-targets
  (Issue #1346, 5 records: benastatin A CHEBI:226154, benastatin B CHEBI:200324, tetarimycin
  A CHEBI:204430, 9-methylstreptimidone CHEBI:215258, and 7-deoxypactamycin CHEBI:198890),
  and seeded-exact-folate-inhibitors-with-card-only-targets-awaiting-primary-literature-promotion
  (Issue #1347, 6 records: sulfadoxine CHEBI:9329, sulfasalazine CHEBI:9334, sulfisoxazole
  CHEBI:102484, dapsone CHEBI:4325, brodimoprim CHEBI:131726, and tetroxoprim CHEBI:135420).
  Verified that all 14 EXACT ChEBI records carry complete single-molecule chemical_structure,
  curated biosynthesis_origin, curator-verified mode_of_action and mode_of_action_target_scope,
  and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets
  (with reviewed Swiss-Prot UniProtKB protein_examples on the 4 DHPS inhibitors [UniProtKB:P0AC13]
  and 2 DHFR inhibitors [UniProtKB:P0ABQ4], and documented held_targets rationales
  on neocarzinostatin, streptothricin E, epoxomicin, benastatin A, benastatin B, tetarimycin
  A, 9-methylstreptimidone, and 7-deoxypactamycin in curation/uniprot_protein_examples.yaml),
  and are promoted to curation_status: REVIEWED (raising corpus REVIEWED count from
  145 to 159 and reducing the review-readiness worklist from 2,960 to 2,946).'
source:
  git_revision: 8ffffaf75be8d64f0a12e6acc0e7202626c9e2b0
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
    sha256: 46a7d741f502752e763f051382d6cf13c6764166d4bb4446aa95f61b31fec0a6
  - path: curation/curator_antibiotics.tsv
    role: context
    sha256: 569005782ded1bda3f26f085bcbee60cf6cb2d2c5c494c1900274b5a054f40da
  - path: curation/cycle7_stage5_review_remediation_transition.json
    role: context
    sha256: 1a86212ece77e0acc225348e322b0b4b38d177722eeb38d26e209b1ea35d1d46
  - path: curation/record_review_queue.tsv
    role: context
    sha256: faf50ecaf2f7fa3be079f34a9e9953ce91e562b827982259eaadb5a3302dad88
  - path: curation/uniprot_protein_examples.yaml
    role: context
    sha256: 0505726e3c220b6dff07caaecab79416d43133967b8ddb443d6abb7ea605b341
  - path: curation/uniprot_protein_examples_transition.json
    role: context
    sha256: 476de2521b919db2a241950c58ec3fc2ea4aa178161f010ab7c5752c04fadb0a
  - path: data/antibiotics/antibacterial/benastatin-a.yaml
    role: target
    sha256: ae247e6f66197742a23284d21961bfeb3c42b7d2b648032ba380baa0fdb31b32
  - path: data/antibiotics/antibacterial/benastatin-b.yaml
    role: target
    sha256: f02cac4f21e786859bb3b2ab5dbc91525cccef066a140044902481aa01197f42
  - path: data/antibiotics/antibacterial/brodimoprim.yaml
    role: target
    sha256: fc0aa9a6de7432b183df91567e5c071133c8d2a3ac343c8d9b4d6ce51a594523
  - path: data/antibiotics/antibacterial/neocarzinostatin.yaml
    role: target
    sha256: 7eafd79f1733847045b9233e93af965285e4df74a52155681f0e1a28c1b6d299
  - path: data/antibiotics/antibacterial/streptothricin-e.yaml
    role: target
    sha256: a1eec3b5db3100590502457c41d0a3271557b5ff579f91021f2c646fbb301e40
  - path: data/antibiotics/antibacterial/sulfadoxine.yaml
    role: target
    sha256: 83d9c3fc7d1b6d723a1df436c347ca666dc5e43744b75f101b184840ef9881f3
  - path: data/antibiotics/antibacterial/sulfasalazine.yaml
    role: target
    sha256: 87776c3387b5344ae14bb5bbbbe01fd2708fef9226c490d31711a14a488c8520
  - path: data/antibiotics/antibacterial/sulfisoxazole.yaml
    role: target
    sha256: 68a31e812c466df50b99ad8b16f7fc349b2e1641fa9a4d32a2ffb0bd155cd391
  - path: data/antibiotics/antibacterial/tetarimycin-a.yaml
    role: target
    sha256: 319f29f8f30491f7fe99e1f6f676245e6a4eef255080278079b675747cd00351
  - path: data/antibiotics/antibacterial/tetroxoprim.yaml
    role: target
    sha256: 7bccecdaedceac399bb2aa7b67ecb9e9e107e7a15f014c86b320cac7b649b336
  - path: data/antibiotics/antifungal/9-methylstreptimidone.yaml
    role: target
    sha256: 9ff70ffa38e4e63784cbd99031b94885d66fc1414ce0c92e2ce0fad55c47c8f8
  - path: data/antibiotics/antimycobacterial/dapsone.yaml
    role: target
    sha256: 2077215e69046fca32d759342a5a2c34a4d15846091824aaf379cd3bb491251b
  - path: data/antibiotics/antiprotozoal/7-deoxypactamycin.yaml
    role: target
    sha256: 549f6f6401bbb66e521351ca58c8fc357baf8c175b43007ec4f8aa1d8f85ae29
  - path: data/antibiotics/antiprotozoal/epoxomicin.yaml
    role: target
    sha256: fa26b5fe815e30947dd7230d3010353540e110b51fb4c491e7bb5392d6358242
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
  description: 'Complete post-remediation review of all 14 AntibioticRecord YAML files
    modified in Cycle 7 Stage 5 across resolved finding groups 1-3 (Issues #1345,
    #1346, #1347).'
  selection: 'All 14 records in Cycle 7 Stage 5 resolved finding groups (Issues #1345,
    #1346, #1347).'
  coverage: full
  population_size: 14
  reviewed_target_ids:
  - CHEBI:29655
  - CHEBI:67576
  - CHEBI:42265
  - CHEBI:226154
  - CHEBI:200324
  - CHEBI:204430
  - CHEBI:215258
  - CHEBI:198890
  - CHEBI:9329
  - CHEBI:9334
  - CHEBI:102484
  - CHEBI:4325
  - CHEBI:131726
  - CHEBI:135420
targets:
- target_id: CHEBI:29655
  path: data/antibiotics/antibacterial/neocarzinostatin.yaml
  label: neocarzinostatin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/neocarzinostatin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:67576
  path: data/antibiotics/antibacterial/streptothricin-e.yaml
  label: streptothricin E
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/streptothricin-e.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:42265
  path: data/antibiotics/antiprotozoal/epoxomicin.yaml
  label: epoxomicin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antiprotozoal/epoxomicin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:226154
  path: data/antibiotics/antibacterial/benastatin-a.yaml
  label: benastatin A
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/benastatin-a.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:200324
  path: data/antibiotics/antibacterial/benastatin-b.yaml
  label: benastatin B
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/benastatin-b.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:204430
  path: data/antibiotics/antibacterial/tetarimycin-a.yaml
  label: tetarimycin A
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/tetarimycin-a.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:215258
  path: data/antibiotics/antifungal/9-methylstreptimidone.yaml
  label: 9-methylstreptimidone
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antifungal/9-methylstreptimidone.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:198890
  path: data/antibiotics/antiprotozoal/7-deoxypactamycin.yaml
  label: 7-deoxypactamycin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antiprotozoal/7-deoxypactamycin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:9329
  path: data/antibiotics/antibacterial/sulfadoxine.yaml
  label: sulfadoxine
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sulfadoxine.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:9334
  path: data/antibiotics/antibacterial/sulfasalazine.yaml
  label: sulfasalazine
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sulfasalazine.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:102484
  path: data/antibiotics/antibacterial/sulfisoxazole.yaml
  label: sulfisoxazole
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sulfisoxazole.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:4325
  path: data/antibiotics/antimycobacterial/dapsone.yaml
  label: dapsone
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antimycobacterial/dapsone.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:131726
  path: data/antibiotics/antibacterial/brodimoprim.yaml
  label: brodimoprim
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/brodimoprim.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:135420
  path: data/antibiotics/antibacterial/tetroxoprim.yaml
  label: tetroxoprim
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/tetroxoprim.yaml
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
  command: .venv/bin/python scripts/validate_strict.py
  exit_code: 0
  summary: All 3,105 corpus records, including the 14 remediated records, pass closed
    LinkML schema validation and OAK label correspondence with 0 errors.
  target_ids:
  - CHEBI:29655
  - CHEBI:67576
  - CHEBI:42265
  - CHEBI:226154
  - CHEBI:200324
  - CHEBI:204430
  - CHEBI:215258
  - CHEBI:198890
  - CHEBI:9329
  - CHEBI:9334
  - CHEBI:102484
  - CHEBI:4325
  - CHEBI:131726
  - CHEBI:135420
  evidence_ids:
  - validate-strict-pass
  - remediated-records-content
- check_id: corpus-reproduction-remediated-records
  name: Full corpus seed reproduction check
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py
  exit_code: 0
  summary: All 3,105 records reproduce byte-for-byte from data/raw/ plus curator inputs
    with 0 missing, 0 unexpected, and 0 drifted fields.
  target_ids:
  - CHEBI:29655
  - CHEBI:67576
  - CHEBI:42265
  - CHEBI:226154
  - CHEBI:200324
  - CHEBI:204430
  - CHEBI:215258
  - CHEBI:198890
  - CHEBI:9329
  - CHEBI:9334
  - CHEBI:102484
  - CHEBI:4325
  - CHEBI:131726
  - CHEBI:135420
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
  - CHEBI:29655
  - CHEBI:67576
  - CHEBI:42265
  - CHEBI:226154
  - CHEBI:200324
  - CHEBI:204430
  - CHEBI:215258
  - CHEBI:198890
  - CHEBI:9329
  - CHEBI:9334
  - CHEBI:102484
  - CHEBI:4325
  - CHEBI:131726
  - CHEBI:135420
  evidence_ids:
  - remediated-records-content
evidence:
- evidence_id: remediated-records-content
  kind: record_content
  reference: curation/record_review_queue.tsv
  locator: 14 remediated YAML records and refreshed review-readiness worklist (2,946
    items)
  accessed_at: '2026-11-08T23:46:00Z'
  support: supports
  snapshot_sha256: faf50ecaf2f7fa3be079f34a9e9953ce91e562b827982259eaadb5a3302dad88
  summary: 'All 14 records were updated through native validated writers (write_validated_antibiotic,
    apply_uniprot_examples_plan, record_curation_event): 3 Group 1 PROPOSED/EXACT
    records (neocarzinostatin CHEBI:29655, streptothricin E CHEBI:67576, epoxomicin
    CHEBI:42265) promoted to REVIEWED; 5 Group 2 Cycle 7 Stage 1 PROPOSED/EXACT natural
    products (benastatin A CHEBI:226154, benastatin B CHEBI:200324, tetarimycin A
    CHEBI:204430, 9-methylstreptimidone CHEBI:215258, 7-deoxypactamycin CHEBI:198890)
    populated with curated mode_of_action and PRIMARY_LITERATURE molecular_targets
    (documented in curation/uniprot_protein_examples.yaml held_targets) and promoted
    to REVIEWED; and 6 Group 3 SEEDED/EXACT folate-pathway inhibitors (sulfadoxine
    CHEBI:9329, sulfasalazine CHEBI:9334, sulfisoxazole CHEBI:102484, dapsone CHEBI:4325,
    brodimoprim CHEBI:131726, tetroxoprim CHEBI:135420) populated with biosynthesis_origin:
    SYNTHETIC, MICROBIAL_TARGET mode_of_action, and PRIMARY_LITERATURE molecular_targets
    (GO:0004156 FolP or GO:0004146 FolA) with reviewed E. coli K-12 Swiss-Prot UniProtKB
    protein_examples (UniProtKB:P0AC13 or UniProtKB:P0ABQ4) and promoted to REVIEWED
    (raising corpus REVIEWED count from 145 to 159 and reducing the review-readiness
    queue from 2,960 to 2,946).'
- evidence_id: validate-strict-pass
  kind: validation
  reference: scripts/validate_strict.py
  locator: 3105 files scanned, 0 files with ERROR, 0 total ERROR rows
  accessed_at: '2026-11-08T23:47:00Z'
  support: supports
  snapshot_sha256: d70e6739c881260927dfc99abea16e56be0f34f353f9f95353a43da76e8e7217
  summary: Closed-mode LinkML validation and OAK ontology label verification pass
    across all 3,105 records.
- evidence_id: verify-corpus-pass
  kind: validation
  reference: scripts/verify_corpus.py
  locator: 'records expected: 3105, on disk: 3105, missing: 0, unexpected: 0, drifted
    fields: 0'
  accessed_at: '2026-11-08T23:48:00Z'
  support: supports
  snapshot_sha256: 7d881f9b4e17b02d7f3ec3eb48404ad0a41a0cefa915edc9a442f755b834df78
  summary: Every curator-owned edit on the 14 remediated records survives seed_from_sources.py
    reproduction without drift.
- evidence_id: primary-literature-sources
  kind: primary_source
  reference: PMID:15797213, PMID:123897, PMID:2177682, PMID:22820420, PMID:19651911,
    PMID:24168704, PMID:38664572, PMID:19047004, PMID:23157252, PMID:23438151, PMID:41162067,
    PMID:21513878, PMID:17827660, PMID:378102, PMID:22383845, PMID:16359642, PMID:391962
  locator: Primary experimental mechanism and target studies cited across the 14 remediated
    records
  accessed_at: '2026-11-08T23:46:00Z'
  support: supports
  summary: Primary studies support REVIEWED promotion on the 3 Group 1 records (neocarzinostatin
    DOI:10.1016/j.chembiol.2004.12.013 / PMID:15797213 and DOI:10.7164/antibiotics.28.229
    / PMID:123897; streptothricin E DOI:10.1248/cpb.38.2296 / PMID:2177682 and DOI:10.1038/nchembio.1040
    / PMID:22820420; epoxomicin DOI:10.1128/aac.00088-09 / PMID:19651911 and DOI:10.1021/cb400699p
    / PMID:24168704), mode_of_action, PRIMARY_LITERATURE molecular_targets, and REVIEWED
    promotion on the 5 Cycle 7 Stage 1 natural products (benastatin A and benastatin
    B DOI:10.1038/s41429-024-00727-1 / PMID:38664572 and DOI:10.1016/j.jbiotec.2008.10.013
    / PMID:19047004; tetarimycin A DOI:10.1021/ja3093828 / PMID:23157252; 9-methylstreptimidone
    DOI:10.1021/ol400224n / PMID:23438151 and DOI:10.1016/j.pestbp.2025.106683 / PMID:41162067;
    7-deoxypactamycin DOI:10.1016/j.chembiol.2011.01.016 / PMID:21513878 and DOI:10.1038/ja.2007.63
    / PMID:17827660), and PRIMARY_LITERATURE bacterial FolP (GO:0004156) and FolA
    (GO:0004146) molecular_targets with reviewed E. coli K-12 UniProtKB:P0AC13 and
    UniProtKB:P0ABQ4 protein_examples and REVIEWED promotion on the 6 EXACT folate-pathway
    inhibitors (sulfadoxine, sulfasalazine, sulfisoxazole, dapsone, brodimoprim, and
    tetroxoprim; DOI:10.1128/AAC.15.2.195 / PMID:378102, DOI:10.1126/science.1214641
    / PMID:22383845, DOI:10.1016/j.bcp.2005.10.052 / PMID:16359642, and PMID:391962).
assessments:
- assessment_id: group1-three-proposed-exact-records-promoted-to-reviewed
  area: completeness
  topic: Promotion of 3 PROPOSED+EXACT records (neocarzinostatin, streptothricin E,
    epoxomicin) with complete mechanism and target curation to REVIEWED
  outcome: supported
  summary: 'All 3 Group 1 records (neocarzinostatin CHEBI:29655, streptothricin E
    CHEBI:67576, and epoxomicin CHEBI:42265) carry exact single-molecule ChEBI structures,
    curated biosynthesis_origin (NATURAL_PRODUCT), curator-settled mode_of_action
    and mode_of_action_target_scope, and source: PRIMARY_LITERATURE (evidence_status:
    PRIMARY_EVIDENCE) molecular_targets (with documented held_targets rationales in
    curation/uniprot_protein_examples.yaml), and are promoted to curation_status:
    REVIEWED with PROMOTED_TO_REVIEWED curation events.'
  target_ids:
  - CHEBI:29655
  - CHEBI:67576
  - CHEBI:42265
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
- assessment_id: group2-cycle7-stage1-natural-products-moa-targets-and-reviewed
  area: completeness
  topic: Population of mode_of_action, PRIMARY_LITERATURE molecular_targets, and REVIEWED
    promotion on 5 Cycle 7 Stage 1 EXACT natural products
  outcome: supported
  summary: 'All 5 Cycle 7 Stage 1 EXACT natural-product records (benastatin A CHEBI:226154,
    benastatin B CHEBI:200324, tetarimycin A CHEBI:204430, 9-methylstreptimidone CHEBI:215258,
    and 7-deoxypactamycin CHEBI:198890) now carry curated mode_of_action, mode_of_action_target_scope,
    CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status:
    PRIMARY_EVIDENCE) molecular_targets (documented in curation/uniprot_protein_examples.yaml
    held_targets), and are promoted to curation_status: REVIEWED.'
  target_ids:
  - CHEBI:226154
  - CHEBI:200324
  - CHEBI:204430
  - CHEBI:215258
  - CHEBI:198890
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
- assessment_id: group3-seeded-exact-folate-inhibitors-primary-targets-and-reviewed
  area: completeness
  topic: Population of PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples,
    and REVIEWED promotion on 6 SEEDED/EXACT folate inhibitors
  outcome: supported
  summary: 'All 6 Group 3 EXACT folate-pathway inhibitor records (sulfadoxine CHEBI:9329,
    sulfasalazine CHEBI:9334, sulfisoxazole CHEBI:102484, dapsone CHEBI:4325, brodimoprim
    CHEBI:131726, and tetroxoprim CHEBI:135420) now carry biosynthesis_origin: SYNTHETIC,
    MICROBIAL_TARGET mode_of_action_target_scope, CURATOR mode_of_action_notes (FOLATE_PATHWAY_INHIBITION),
    and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) bacterial dihydropteroate
    synthase (FolP / DHPS; GO:0004156) or bacterial dihydrofolate reductase (FolA
    / DHFR; GO:0004146) molecular_targets with 1 reviewed E. coli K-12 Swiss-Prot
    UniProtKB protein_example per record (UniProtKB:P0AC13 folP on the 4 DHPS inhibitors
    and UniProtKB:P0ABQ4 folA on the 2 DHFR inhibitors; 6 total across the 6 records),
    and are promoted from SEEDED to REVIEWED.'
  target_ids:
  - CHEBI:9329
  - CHEBI:9334
  - CHEBI:102484
  - CHEBI:4325
  - CHEBI:131726
  - CHEBI:135420
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
  title: Promoted 3 PROPOSED+EXACT records (neocarzinostatin, streptothricin E, epoxomicin)
    with complete primary mechanism and target curation to REVIEWED
  description: Promoted CHEBI:29655 (neocarzinostatin), CHEBI:67576 (streptothricin
    E), and CHEBI:42265 (epoxomicin) from PROPOSED to REVIEWED via record_curation_event
    (PROMOTED_TO_REVIEWED) and write_validated_antibiotic, and registered their held_records
    entries in curation/causal_graphs.yaml.
  target_ids:
  - CHEBI:29655
  - CHEBI:67576
  - CHEBI:42265
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
    path: data/antibiotics/antibacterial/neocarzinostatin.yaml
    role: Curator-owned curation_status and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/streptothricin-e.yaml
    role: Curator-owned curation_status and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antiprotozoal/epoxomicin.yaml
    role: Curator-owned curation_status and curation_history
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (Issue #1345): promoted neocarzinostatin
    (CHEBI:29655), streptothricin E (CHEBI:67576), and epoxomicin (CHEBI:42265) from
    PROPOSED to REVIEWED.'
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261108T210100Z-cycle7-frozen-inventory-cohort-review
    finding_id: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion
  - repository: culturebotai/AntibioticMech
    review_id: 20261108T210000Z-neocarzinostatin-record-review
    finding_id: neocarzinostatin-awaiting-reviewed-promotion
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1345
- finding_id: cycle7-stage1-proposed-exact-natural-products-missing-mechanism-and-targets
  issue_key: cycle7-stage1-proposed-exact-natural-products-missing-mechanism-and-targets
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Populated mode_of_action, PRIMARY_LITERATURE molecular_targets, and promoted
    5 Cycle 7 Stage 1 EXACT natural products to REVIEWED
  description: 'Curated mode_of_action, mode_of_action_target_scope, CURATOR mode_of_action_notes,
    and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets
    (with all 5 non-protein targets documented in curation/uniprot_protein_examples.yaml
    held_targets), and promoted all 5 records from PROPOSED to REVIEWED via record_curation_event
    and write_validated_antibiotic.'
  target_ids:
  - CHEBI:226154
  - CHEBI:200324
  - CHEBI:204430
  - CHEBI:215258
  - CHEBI:198890
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
    path: data/antibiotics/antibacterial/benastatin-a.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/benastatin-b.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/tetarimycin-a.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antifungal/9-methylstreptimidone.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antiprotozoal/7-deoxypactamycin.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (Issue #1346): curated mode_of_action
    and PRIMARY_LITERATURE molecular_targets and promoted all 5 Cycle 7 Stage 1 EXACT
    natural products to REVIEWED.'
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261108T210100Z-cycle7-frozen-inventory-cohort-review
    finding_id: cycle7-stage1-proposed-exact-natural-products-missing-mechanism-and-targets
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1346
- finding_id: seeded-exact-folate-inhibitors-with-card-only-targets-awaiting-primary-literature-promotion
  issue_key: seeded-exact-folate-inhibitors-with-card-only-targets-awaiting-primary-literature-promotion
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Populated PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples,
    and promoted 6 EXACT folate inhibitors to REVIEWED
  description: 'Curated biosynthesis_origin: SYNTHETIC, MICROBIAL_TARGET mode_of_action_target_scope,
    CURATOR mode_of_action_notes (FOLATE_PATHWAY_INHIBITION), and source: PRIMARY_LITERATURE
    (evidence_status: PRIMARY_EVIDENCE) bacterial dihydropteroate synthase (FolP /
    DHPS; GO:0004156) or bacterial dihydrofolate reductase (FolA / DHFR; GO:0004146)
    molecular_targets with 6 reviewed E. coli K-12 Swiss-Prot UniProtKB protein_examples
    (UniProtKB:P0AC13 or UniProtKB:P0ABQ4) across sulfadoxine (CHEBI:9329), sulfasalazine
    (CHEBI:9334), sulfisoxazole (CHEBI:102484), dapsone (CHEBI:4325), brodimoprim
    (CHEBI:131726), and tetroxoprim (CHEBI:135420) via apply_uniprot_examples_plan,
    and promoted all 6 records from SEEDED to REVIEWED via record_curation_event and
    write_validated_antibiotic.'
  target_ids:
  - CHEBI:9329
  - CHEBI:9334
  - CHEBI:102484
  - CHEBI:4325
  - CHEBI:131726
  - CHEBI:135420
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
    path: data/antibiotics/antibacterial/sulfadoxine.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sulfasalazine.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sulfisoxazole.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antimycobacterial/dapsone.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/brodimoprim.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/tetroxoprim.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (Issue #1347): populated PRIMARY_LITERATURE
    molecular_targets and reviewed UniProtKB protein_examples and promoted all 6 EXACT
    ChEBI folate-pathway inhibitors to REVIEWED.'
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261108T210100Z-cycle7-frozen-inventory-cohort-review
    finding_id: seeded-exact-folate-inhibitors-with-card-only-targets-awaiting-primary-literature-promotion
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1347
actions: []
limitations:
- All 14 newly promoted REVIEWED records are registered in curation/causal_graphs.yaml
  held_records (bringing total held_records to 69) awaiting multi-step primary-literature
  causal_graphs in a subsequent Stage 2 goal.
notes:
- Original Cycle 7 Stage 4 review bundles (20261108T210000Z-neocarzinostatin-record-review
  and 20261108T210100Z-cycle7-frozen-inventory-cohort-review) are preserved byte-for-byte.
related_reviews:
- repository: culturebotai/AntibioticMech
  review_id: 20261108T210000Z-neocarzinostatin-record-review
  relationship: Predecessor Cycle 7 Stage 4 single-record review of neocarzinostatin
    (CHEBI:29655)
- repository: culturebotai/AntibioticMech
  review_id: 20261108T210100Z-cycle7-frozen-inventory-cohort-review
  relationship: Predecessor Cycle 7 Stage 4 full-inventory cohort review identifying
    the 3 resolved finding groups
tags:
- batch-review
- cycle-07
- stage-05
- remediation-verification
```
