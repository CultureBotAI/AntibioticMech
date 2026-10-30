# Cycle 3 Stage 5 post-remediation review of 12 remediated AntibioticRecord files (Issues #1284, #1285, #1286)

- Review: 20261026T071500Z-cycle3-stage5-remediated-records-review
- Repository: culturebotai/AntibioticMech
- Started UTC: 2026-10-26T07:05:00Z
- Finished UTC: 2026-10-26T07:15:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Post-remediation batch review of the 12 AntibioticRecord YAML files updated in Cycle 3 Stage 5 to resolve all 3 open Stage 4 record and category review findings: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion (Issue #1284, 2 records: bactobolin A CHEBI:138579, negamycin CHEBI:198310 including companion single-record review 20261026T003500Z-negamycin-record-review), proposed-exact-quinolones-with-moa-missing-primary-targets-and-reviewed-promotion (Issue #1285, 3 records: besifloxacin CHEBI:135622, ozenoxacin CHEBI:136050, pazufloxacin CHEBI:94700), and proposed-minted-records-with-moa-missing-primary-targets (Issue #1286, 7 records: cadazolid antibioticmech:curator-975acd7c4d, radezolid antibioticmech:curator-a739fc0555, sutezolid antibioticmech:curator-f56d459cee, sanfetrinem antibioticmech:curator-daae3d88a3, tomopenem antibioticmech:curator-e14f58e6dc, albaconazole antibioticmech:curator-6bdee75cea, quilseconazole antibioticmech:curator-217ed2935e). Verified that all 5 Group 1 and Group 2 EXACT ChEBI records (bactobolin A, negamycin, besifloxacin, ozenoxacin, pazufloxacin) carry complete primary-literature mode_of_action and molecular_targets and are promoted to curation_status: REVIEWED (raising corpus REVIEWED count from 96 to 101), and that all 7 Group 3 PROPOSED/MINTED records carry curated source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets aligned with their top-level mode_of_action while preserving curation_status: PROPOSED under structure_completeness_audit.

## Scope And Provenance

Complete post-remediation review of all 12 AntibioticRecord YAML files modified in Cycle 3 Stage 5 across resolved finding groups 1-3 (Issues #1284, #1285, #1286).

Selection: All 12 records in Cycle 3 Stage 5 resolved finding groups (Issues #1284, #1285, #1286).
Coverage: full; 12 reviewed / 12 in the declared population.
Source: working_tree at Git base e8beeb9097baa104a6c9abece25054625da639ff.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:138579 | data/antibiotics/antibacterial/bactobolin-a.yaml | maintained | bactobolin A |
| CHEBI:198310 | data/antibiotics/antibacterial/negamycin.yaml | maintained | negamycin |
| CHEBI:135622 | data/antibiotics/antibacterial/besifloxacin.yaml | maintained | besifloxacin |
| CHEBI:136050 | data/antibiotics/antibacterial/ozenoxacin.yaml | maintained | ozenoxacin |
| CHEBI:94700 | data/antibiotics/antibacterial/pazufloxacin.yaml | maintained | pazufloxacin |
| antibioticmech:curator-975acd7c4d | data/antibiotics/antibacterial/cadazolid.yaml | maintained | cadazolid |
| antibioticmech:curator-a739fc0555 | data/antibiotics/antibacterial/radezolid.yaml | maintained | radezolid |
| antibioticmech:curator-f56d459cee | data/antibiotics/antibacterial/sutezolid.yaml | maintained | sutezolid |
| antibioticmech:curator-daae3d88a3 | data/antibiotics/antibacterial/sanfetrinem.yaml | maintained | sanfetrinem |
| antibioticmech:curator-e14f58e6dc | data/antibiotics/antibacterial/tomopenem.yaml | maintained | tomopenem |
| antibioticmech:curator-6bdee75cea | data/antibiotics/antifungal/albaconazole.yaml | maintained | albaconazole |
| antibioticmech:curator-217ed2935e | data/antibiotics/antifungal/quilseconazole.yaml | maintained | quilseconazole |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and OAK ontology-label validation | passed | True | CHEBI:138579, CHEBI:198310, CHEBI:135622, CHEBI:136050, CHEBI:94700, antibioticmech:curator-975acd7c4d, antibioticmech:curator-a739fc0555, antibioticmech:curator-f56d459cee, antibioticmech:curator-daae3d88a3, antibioticmech:curator-e14f58e6dc, antibioticmech:curator-6bdee75cea, antibioticmech:curator-217ed2935e | All 3,012 corpus records, including the 12 remediated records, pass closed LinkML schema validation and OAK label correspondence with 0 errors. |
| Full corpus seed reproduction check | passed | True | CHEBI:138579, CHEBI:198310, CHEBI:135622, CHEBI:136050, CHEBI:94700, antibioticmech:curator-975acd7c4d, antibioticmech:curator-a739fc0555, antibioticmech:curator-f56d459cee, antibioticmech:curator-daae3d88a3, antibioticmech:curator-e14f58e6dc, antibioticmech:curator-6bdee75cea, antibioticmech:curator-217ed2935e | All 3,012 records reproduce byte-for-byte from data/raw/ plus curator inputs with 0 missing, 0 unexpected, and 0 drifted fields. |
| UniProt protein examples and causal graphs curation test suites | passed | True | CHEBI:138579, CHEBI:198310, CHEBI:135622, CHEBI:136050, CHEBI:94700, antibioticmech:curator-975acd7c4d, antibioticmech:curator-a739fc0555, antibioticmech:curator-f56d459cee, antibioticmech:curator-daae3d88a3, antibioticmech:curator-e14f58e6dc, antibioticmech:curator-6bdee75cea, antibioticmech:curator-217ed2935e | All 128 tests across test_uniprot_protein_examples.py and test_causal_graphs_curation.py pass with exit code 0. |

## Scientific And Domain Assessments

### Promotion of 2 PROPOSED/EXACT records with complete mechanism and target curation to REVIEWED

completeness: supported. Targets: CHEBI:138579, CHEBI:198310.

Both Group 1 records (CHEBI:138579 bactobolin A, CHEBI:198310 negamycin) carry exact single-molecule ChEBI structures, curated biosynthesis_origin, curator-settled mode_of_action (MICROBIAL_TARGET), and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets, and are now promoted to curation_status: REVIEWED with PROMOTED_TO_REVIEWED events.

### Population of PRIMARY_LITERATURE molecular_targets and REVIEWED promotion on 3 PROPOSED/EXACT quinolones

completeness: supported. Targets: CHEBI:135622, CHEBI:136050, CHEBI:94700.

All 3 Group 2 EXACT ChEBI quinolone records (CHEBI:135622 besifloxacin, CHEBI:136050 ozenoxacin, CHEBI:94700 pazufloxacin) now carry source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) DNA gyrase and DNA topoisomerase IV molecular_targets with reviewed S. pneumoniae, S. aureus, and E. coli UniProtKB protein_examples across all 3 records, and are promoted to curation_status: REVIEWED with PROMOTED_TO_REVIEWED events.

### Population of PRIMARY_LITERATURE molecular_targets on 7 PROPOSED/MINTED records with curated mode_of_action

completeness: supported. Targets: antibioticmech:curator-975acd7c4d, antibioticmech:curator-a739fc0555, antibioticmech:curator-f56d459cee, antibioticmech:curator-daae3d88a3, antibioticmech:curator-e14f58e6dc, antibioticmech:curator-6bdee75cea, antibioticmech:curator-217ed2935e.

All 7 Group 3 PROPOSED/MINTED records (cadazolid, radezolid, sutezolid, sanfetrinem, tomopenem, albaconazole, quilseconazole) now carry curated source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets aligned with their top-level mode_of_action (plus reviewed C. albicans ERG11 UniProtKB protein_examples on albaconazole and documented held_targets rationales on quilseconazole and the 5 other Group 3 records in curation/uniprot_protein_examples.yaml), while retaining curation_status: PROPOSED under structure_completeness_audit.

## Findings

### proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion: Promoted 2 PROPOSED/EXACT ChEBI records with complete primary mechanism curation to REVIEWED

major / resolved / confirmed; issue key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion.

Promoted CHEBI:138579 (bactobolin A) and CHEBI:198310 (negamycin) from PROPOSED to REVIEWED via record_curation_event (PROMOTED_TO_REVIEWED) and write_validated_antibiotic.

Disposition: Resolved in Cycle 3 Stage 5 (Issue #1284): promoted both PROPOSED/EXACT records with complete primary mechanism and target curation to REVIEWED.

### proposed-exact-quinolones-with-moa-missing-primary-targets-and-reviewed-promotion: Populated PRIMARY_LITERATURE molecular_targets and promoted 3 PROPOSED/EXACT quinolones to REVIEWED

major / resolved / confirmed; issue key: proposed-exact-quinolones-with-moa-missing-primary-targets-and-reviewed-promotion.

Populated source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) DNA gyrase and DNA topoisomerase IV molecular_targets (with reviewed UniProtKB protein_examples via apply_uniprot_examples_plan across besifloxacin, ozenoxacin, and pazufloxacin) and promoted CHEBI:135622 (besifloxacin), CHEBI:136050 (ozenoxacin), and CHEBI:94700 (pazufloxacin) from PROPOSED to REVIEWED via record_curation_event (PROMOTED_TO_REVIEWED) and write_validated_antibiotic.

Disposition: Resolved in Cycle 3 Stage 5 (Issue #1285): populated PRIMARY_LITERATURE molecular_targets and promoted all 3 EXACT ChEBI quinolone records to REVIEWED.

### proposed-minted-records-with-moa-missing-primary-targets: Populated PRIMARY_LITERATURE molecular_targets on 7 PROPOSED/MINTED records with curated mode_of_action

major / resolved / confirmed; issue key: proposed-minted-records-with-moa-missing-primary-targets.

Populated source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets via record_curation_event and write_validated_antibiotic across all 7 Group 3 PROPOSED/MINTED records (cadazolid, radezolid, sutezolid, sanfetrinem, tomopenem, albaconazole, quilseconazole), plus reviewed ERG11 UniProtKB protein_examples via apply_uniprot_examples_plan on albaconazole and documented held_targets rationales on quilseconazole and the 5 other Group 3 records.

Disposition: Resolved in Cycle 3 Stage 5 (Issue #1286): populated PRIMARY_LITERATURE molecular_targets on all 7 PROPOSED/MINTED records.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| remediated-records-content | curation/record_review_queue.tsv; 12 remediated YAML records and refreshed review-readiness worklist (2,911 items) | supports | All 12 records were updated through native validated writers (write_validated_antibiotic, apply_uniprot_examples_plan, record_curation_event): 2 Group 1 PROPOSED/EXACT records (bactobolin A, negamycin) promoted to REVIEWED; 3 Group 2 PROPOSED/EXACT quinolones (besifloxacin, ozenoxacin, pazufloxacin) populated with PRIMARY_LITERATURE molecular_targets and promoted to REVIEWED (raising corpus REVIEWED count from 96 to 101 and reducing the review-readiness queue from 2,916 to 2,911); and 7 Group 3 PROPOSED/MINTED records (cadazolid, radezolid, sutezolid, sanfetrinem, tomopenem, albaconazole, quilseconazole) populated with PRIMARY_LITERATURE molecular_targets. |
| validate-strict-pass | scripts/validate_strict.py; 3012 files scanned, 0 files with ERROR, 0 total ERROR rows | supports | Closed-mode LinkML validation and OAK ontology label verification pass across all 3,012 records. |
| verify-corpus-pass | scripts/verify_corpus.py; records expected: 3012, on disk: 3012, missing: 0, unexpected: 0, drifted fields: 0 | supports | Every curator-owned edit on the 12 remediated records survives seed_from_sources.py reproduction without drift. |
| primary-literature-sources | PMID:23249812, PMID:25562208, PMID:25368144, PMID:25306922, PMID:19451292, PMID:19506065, PMID:11959549, PMID:24080666, PMID:8460909, PMID:11959571, PMID:24128668, PMID:19752277, PMID:18663023, PMID:19075058, PMID:8878596, PMID:7840571, PMID:16048932, PMID:18070969, PMID:11408242, PMID:10582896, PMID:26787697, PMID:27161862; Primary experimental mechanism and target studies cited across the 12 remediated records | supports | Primary studies support REVIEWED promotion on the 2 Group 1 EXACT ChEBI records (bactobolin A PMID:23249812/PMID:25562208, negamycin PMID:25368144/PMID:25306922), PRIMARY_LITERATURE DNA gyrase and topoisomerase IV molecular_targets and REVIEWED promotion on the 3 Group 2 EXACT ChEBI quinolones (besifloxacin PMID:19451292/PMID:19506065, ozenoxacin PMID:11959549/PMID:24080666, pazufloxacin PMID:8460909/PMID:11959571), and PRIMARY_LITERATURE molecular_targets on the 7 Group 3 PROPOSED/MINTED records (cadazolid PMID:24128668, radezolid PMID:19752277, sutezolid PMID:18663023/PMID:19075058, sanfetrinem PMID:8878596/PMID:7840571, tomopenem PMID:16048932/PMID:18070969, albaconazole PMID:11408242/PMID:10582896, quilseconazole PMID:26787697/PMID:27161862). |

## Limits And Additional Notes

- The 7 Group 3 records retain curation_status: PROPOSED and grounding_status: MINTED until upstream single-molecule ChEBI identifiers are assigned, per structure_completeness_audit policy.
- Original Cycle 3 Stage 4 review bundles (20261026T003500Z-negamycin-record-review and 20261026T003600Z-cycle3-frozen-inventory-cohort-review) are preserved byte-for-byte.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261026T071500Z-cycle3-stage5-remediated-records-review
kind: batch
repository: culturebotai/AntibioticMech
title: 'Cycle 3 Stage 5 post-remediation review of 12 remediated AntibioticRecord
  files (Issues #1284, #1285, #1286)'
started_at: '2026-10-26T07:05:00Z'
finished_at: '2026-10-26T07:15:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Cycle 3 Stage 5 post-remediation verification review of the
    12 remediated records prior to independent adversarial PR review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass
native_verdict: PASS
scientific_review: true
summary: 'Post-remediation batch review of the 12 AntibioticRecord YAML files updated
  in Cycle 3 Stage 5 to resolve all 3 open Stage 4 record and category review findings:
  proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion (Issue #1284,
  2 records: bactobolin A CHEBI:138579, negamycin CHEBI:198310 including companion
  single-record review 20261026T003500Z-negamycin-record-review), proposed-exact-quinolones-with-moa-missing-primary-targets-and-reviewed-promotion
  (Issue #1285, 3 records: besifloxacin CHEBI:135622, ozenoxacin CHEBI:136050, pazufloxacin
  CHEBI:94700), and proposed-minted-records-with-moa-missing-primary-targets (Issue
  #1286, 7 records: cadazolid antibioticmech:curator-975acd7c4d, radezolid antibioticmech:curator-a739fc0555,
  sutezolid antibioticmech:curator-f56d459cee, sanfetrinem antibioticmech:curator-daae3d88a3,
  tomopenem antibioticmech:curator-e14f58e6dc, albaconazole antibioticmech:curator-6bdee75cea,
  quilseconazole antibioticmech:curator-217ed2935e). Verified that all 5 Group 1 and
  Group 2 EXACT ChEBI records (bactobolin A, negamycin, besifloxacin, ozenoxacin,
  pazufloxacin) carry complete primary-literature mode_of_action and molecular_targets
  and are promoted to curation_status: REVIEWED (raising corpus REVIEWED count from
  96 to 101), and that all 7 Group 3 PROPOSED/MINTED records carry curated source:
  PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets aligned
  with their top-level mode_of_action while preserving curation_status: PROPOSED under
  structure_completeness_audit.'
source:
  git_revision: e8beeb9097baa104a6c9abece25054625da639ff
  state: working_tree
  inputs:
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: 4c438f137570d6c75a208422f04c0ad21873f5ee467f230a43ec8ed9709d2178
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: curation/causal_graphs.yaml
    sha256: e11d66db669d30454c36ea8076fed494e24bf29cb1390476108f361c18b7a71d
    role: context
  - path: curation/curator_antibiotics.tsv
    sha256: 5a7a6d3c2994644de73400a599908ed5f3a9aa93a952fe678a1887f248cbe9c7
    role: context
  - path: curation/cycle3_stage5_review_remediation_transition.json
    sha256: f257cd9621feabd4b715e6fff37a47361d6e387e80a388ff8311d2b8c2fc8a35
    role: context
  - path: curation/record_review_queue.tsv
    sha256: 8fff653e693fbbddcfabc35bda3f35a9fcc34d8723a3dbaa0356a4444854d87a
    role: context
  - path: curation/uniprot_protein_examples.yaml
    sha256: fbf9ed715319e30a54f58319184753816ba854c2bd4bb8a5b12b125278647323
    role: context
  - path: curation/uniprot_protein_examples_transition.json
    sha256: 22d8abac0a2b22bb81df1f2800bc085dd00906ff53fb4962cf11d1d930ada3dd
    role: context
  - path: data/antibiotics/antibacterial/bactobolin-a.yaml
    sha256: a2987fdcfc1f53fe88d6a346b9495bdbfd2116f59e4f1ca6a1a92fca7771653e
    role: target
  - path: data/antibiotics/antibacterial/besifloxacin.yaml
    sha256: 45dcb6be1b9fb9e9971f5514da101a0f399c7ee75a6ec97af220f191f8242920
    role: target
  - path: data/antibiotics/antibacterial/cadazolid.yaml
    sha256: b849f7085d8108e28dffee4b39f7a512d66061a9151fae58aa58afa3ddb0f025
    role: target
  - path: data/antibiotics/antibacterial/negamycin.yaml
    sha256: 70d4867db1fffb1b2653f15be0ed8db4d46e0ff82d42d13613bc9b36b9338f93
    role: target
  - path: data/antibiotics/antibacterial/ozenoxacin.yaml
    sha256: 2b1c0225a639107adf5a1448a3092fe6a3f49a1df9ecac9ebe6a88caeac4359e
    role: target
  - path: data/antibiotics/antibacterial/pazufloxacin.yaml
    sha256: 787576578bb35055b90b4319d582218599c63e86f2e2b9ccd01a90b0d8fa56da
    role: target
  - path: data/antibiotics/antibacterial/radezolid.yaml
    sha256: eda0b73c9afb05addd53adb447d827dd16454d03a2b68f74168ab3b1489699af
    role: target
  - path: data/antibiotics/antibacterial/sanfetrinem.yaml
    sha256: 136ed5d11e92a5d4b470e61199e5c743d4d7d0e4a7aeb899f39f671b3f5839e0
    role: target
  - path: data/antibiotics/antibacterial/sutezolid.yaml
    sha256: e45cdff363a44ed6930c659d051834b3021384acfba963070904f499e503e55d
    role: target
  - path: data/antibiotics/antibacterial/tomopenem.yaml
    sha256: 4c7379b2fc7bca21c374d89a771bfe7aff1b1659044dfbaf7cc4d48d33f3e781
    role: target
  - path: data/antibiotics/antifungal/albaconazole.yaml
    sha256: 111b26069867bf3d8338510b47ec9997372a2a8a15473e18b3efd85931c72460
    role: target
  - path: data/antibiotics/antifungal/quilseconazole.yaml
    sha256: cf5a5faaa474f41277e3e0e93a7d089e5733e3aaa16bd2c0237295eda619cdbe
    role: target
  - path: scripts/curation_worklist.py
    sha256: 692fdcc39a0c8135c89b483a19ab0a428bfac3d851ff67a6a1ceac80225a2430
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 53cf79eb1417ff7758a94f2d18ac1ce47b0f8c91c8961023363cf37698d4a056
    role: context
  - path: scripts/validate_strict.py
    sha256: d70e6739c881260927dfc99abea16e56be0f34f353f9f95353a43da76e8e7217
    role: context
  - path: scripts/verify_corpus.py
    sha256: 7d881f9b4e17b02d7f3ec3eb48404ad0a41a0cefa915edc9a442f755b834df78
    role: context
  - path: src/antibioticmech/schema/antibioticmech.yaml
    sha256: de62be2dd2dd55f141a0c14ff666eaa00efc6f3b431d651d0196ebcfddfbb301
    role: context
scope:
  description: 'Complete post-remediation review of all 12 AntibioticRecord YAML files
    modified in Cycle 3 Stage 5 across resolved finding groups 1-3 (Issues #1284,
    #1285, #1286).'
  selection: 'All 12 records in Cycle 3 Stage 5 resolved finding groups (Issues #1284,
    #1285, #1286).'
  coverage: full
  population_size: 12
  reviewed_target_ids:
  - CHEBI:138579
  - CHEBI:198310
  - CHEBI:135622
  - CHEBI:136050
  - CHEBI:94700
  - antibioticmech:curator-975acd7c4d
  - antibioticmech:curator-a739fc0555
  - antibioticmech:curator-f56d459cee
  - antibioticmech:curator-daae3d88a3
  - antibioticmech:curator-e14f58e6dc
  - antibioticmech:curator-6bdee75cea
  - antibioticmech:curator-217ed2935e
targets:
- target_id: CHEBI:138579
  path: data/antibiotics/antibacterial/bactobolin-a.yaml
  label: bactobolin A
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/bactobolin-a.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:198310
  path: data/antibiotics/antibacterial/negamycin.yaml
  label: negamycin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/negamycin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:135622
  path: data/antibiotics/antibacterial/besifloxacin.yaml
  label: besifloxacin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/besifloxacin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:136050
  path: data/antibiotics/antibacterial/ozenoxacin.yaml
  label: ozenoxacin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/ozenoxacin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:94700
  path: data/antibiotics/antibacterial/pazufloxacin.yaml
  label: pazufloxacin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/pazufloxacin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: antibioticmech:curator-975acd7c4d
  path: data/antibiotics/antibacterial/cadazolid.yaml
  label: cadazolid
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/cadazolid.yaml
    role: Curator-maintained PROPOSED/MINTED record slots (biosynthesis_origin, mode_of_action,
      mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: antibioticmech:curator-a739fc0555
  path: data/antibiotics/antibacterial/radezolid.yaml
  label: radezolid
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/radezolid.yaml
    role: Curator-maintained PROPOSED/MINTED record slots (biosynthesis_origin, mode_of_action,
      mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: antibioticmech:curator-f56d459cee
  path: data/antibiotics/antibacterial/sutezolid.yaml
  label: sutezolid
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sutezolid.yaml
    role: Curator-maintained PROPOSED/MINTED record slots (biosynthesis_origin, mode_of_action,
      mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: antibioticmech:curator-daae3d88a3
  path: data/antibiotics/antibacterial/sanfetrinem.yaml
  label: sanfetrinem
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sanfetrinem.yaml
    role: Curator-maintained PROPOSED/MINTED record slots (biosynthesis_origin, mode_of_action,
      mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: antibioticmech:curator-e14f58e6dc
  path: data/antibiotics/antibacterial/tomopenem.yaml
  label: tomopenem
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/tomopenem.yaml
    role: Curator-maintained PROPOSED/MINTED record slots (biosynthesis_origin, mode_of_action,
      mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: antibioticmech:curator-6bdee75cea
  path: data/antibiotics/antifungal/albaconazole.yaml
  label: albaconazole
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antifungal/albaconazole.yaml
    role: Curator-maintained PROPOSED/MINTED record slots (biosynthesis_origin, mode_of_action,
      mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: antibioticmech:curator-217ed2935e
  path: data/antibiotics/antifungal/quilseconazole.yaml
  label: quilseconazole
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antifungal/quilseconazole.yaml
    role: Curator-maintained PROPOSED/MINTED record slots (biosynthesis_origin, mode_of_action,
      mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
checks:
- check_id: strict-schema-remediated-records
  name: Closed-schema and OAK ontology-label validation
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  exit_code: 0
  summary: All 3,012 corpus records, including the 12 remediated records, pass closed
    LinkML schema validation and OAK label correspondence with 0 errors.
  target_ids:
  - CHEBI:138579
  - CHEBI:198310
  - CHEBI:135622
  - CHEBI:136050
  - CHEBI:94700
  - antibioticmech:curator-975acd7c4d
  - antibioticmech:curator-a739fc0555
  - antibioticmech:curator-f56d459cee
  - antibioticmech:curator-daae3d88a3
  - antibioticmech:curator-e14f58e6dc
  - antibioticmech:curator-6bdee75cea
  - antibioticmech:curator-217ed2935e
  evidence_ids:
  - validate-strict-pass
  - remediated-records-content
- check_id: corpus-reproduction-remediated-records
  name: Full corpus seed reproduction check
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py
  exit_code: 0
  summary: All 3,012 records reproduce byte-for-byte from data/raw/ plus curator inputs
    with 0 missing, 0 unexpected, and 0 drifted fields.
  target_ids:
  - CHEBI:138579
  - CHEBI:198310
  - CHEBI:135622
  - CHEBI:136050
  - CHEBI:94700
  - antibioticmech:curator-975acd7c4d
  - antibioticmech:curator-a739fc0555
  - antibioticmech:curator-f56d459cee
  - antibioticmech:curator-daae3d88a3
  - antibioticmech:curator-e14f58e6dc
  - antibioticmech:curator-6bdee75cea
  - antibioticmech:curator-217ed2935e
  evidence_ids:
  - verify-corpus-pass
  - remediated-records-content
- check_id: uniprot-and-causal-graphs-pytest
  name: UniProt protein examples and causal graphs curation test suites
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_uniprot_protein_examples.py tests/test_causal_graphs_curation.py
    -q
  exit_code: 0
  summary: All 128 tests across test_uniprot_protein_examples.py and test_causal_graphs_curation.py
    pass with exit code 0.
  target_ids:
  - CHEBI:138579
  - CHEBI:198310
  - CHEBI:135622
  - CHEBI:136050
  - CHEBI:94700
  - antibioticmech:curator-975acd7c4d
  - antibioticmech:curator-a739fc0555
  - antibioticmech:curator-f56d459cee
  - antibioticmech:curator-daae3d88a3
  - antibioticmech:curator-e14f58e6dc
  - antibioticmech:curator-6bdee75cea
  - antibioticmech:curator-217ed2935e
  evidence_ids:
  - remediated-records-content
evidence:
- evidence_id: remediated-records-content
  kind: record_content
  reference: curation/record_review_queue.tsv
  locator: 12 remediated YAML records and refreshed review-readiness worklist (2,911
    items)
  accessed_at: '2026-10-26T07:10:00Z'
  support: supports
  snapshot_sha256: 8fff653e693fbbddcfabc35bda3f35a9fcc34d8723a3dbaa0356a4444854d87a
  summary: 'All 12 records were updated through native validated writers (write_validated_antibiotic,
    apply_uniprot_examples_plan, record_curation_event): 2 Group 1 PROPOSED/EXACT
    records (bactobolin A, negamycin) promoted to REVIEWED; 3 Group 2 PROPOSED/EXACT
    quinolones (besifloxacin, ozenoxacin, pazufloxacin) populated with PRIMARY_LITERATURE
    molecular_targets and promoted to REVIEWED (raising corpus REVIEWED count from
    96 to 101 and reducing the review-readiness queue from 2,916 to 2,911); and 7
    Group 3 PROPOSED/MINTED records (cadazolid, radezolid, sutezolid, sanfetrinem,
    tomopenem, albaconazole, quilseconazole) populated with PRIMARY_LITERATURE molecular_targets.'
- evidence_id: validate-strict-pass
  kind: validation
  reference: scripts/validate_strict.py
  locator: 3012 files scanned, 0 files with ERROR, 0 total ERROR rows
  accessed_at: '2026-10-26T07:08:00Z'
  support: supports
  snapshot_sha256: d70e6739c881260927dfc99abea16e56be0f34f353f9f95353a43da76e8e7217
  summary: Closed-mode LinkML validation and OAK ontology label verification pass
    across all 3,012 records.
- evidence_id: verify-corpus-pass
  kind: validation
  reference: scripts/verify_corpus.py
  locator: 'records expected: 3012, on disk: 3012, missing: 0, unexpected: 0, drifted
    fields: 0'
  accessed_at: '2026-10-26T07:09:00Z'
  support: supports
  snapshot_sha256: 7d881f9b4e17b02d7f3ec3eb48404ad0a41a0cefa915edc9a442f755b834df78
  summary: Every curator-owned edit on the 12 remediated records survives seed_from_sources.py
    reproduction without drift.
- evidence_id: primary-literature-sources
  kind: primary_source
  reference: PMID:23249812, PMID:25562208, PMID:25368144, PMID:25306922, PMID:19451292,
    PMID:19506065, PMID:11959549, PMID:24080666, PMID:8460909, PMID:11959571, PMID:24128668,
    PMID:19752277, PMID:18663023, PMID:19075058, PMID:8878596, PMID:7840571, PMID:16048932,
    PMID:18070969, PMID:11408242, PMID:10582896, PMID:26787697, PMID:27161862
  locator: Primary experimental mechanism and target studies cited across the 12 remediated
    records
  accessed_at: '2026-10-26T07:10:00Z'
  support: supports
  summary: Primary studies support REVIEWED promotion on the 2 Group 1 EXACT ChEBI
    records (bactobolin A PMID:23249812/PMID:25562208, negamycin PMID:25368144/PMID:25306922),
    PRIMARY_LITERATURE DNA gyrase and topoisomerase IV molecular_targets and REVIEWED
    promotion on the 3 Group 2 EXACT ChEBI quinolones (besifloxacin PMID:19451292/PMID:19506065,
    ozenoxacin PMID:11959549/PMID:24080666, pazufloxacin PMID:8460909/PMID:11959571),
    and PRIMARY_LITERATURE molecular_targets on the 7 Group 3 PROPOSED/MINTED records
    (cadazolid PMID:24128668, radezolid PMID:19752277, sutezolid PMID:18663023/PMID:19075058,
    sanfetrinem PMID:8878596/PMID:7840571, tomopenem PMID:16048932/PMID:18070969,
    albaconazole PMID:11408242/PMID:10582896, quilseconazole PMID:26787697/PMID:27161862).
assessments:
- assessment_id: group1-proposed-exact-promoted-to-reviewed
  area: completeness
  topic: Promotion of 2 PROPOSED/EXACT records with complete mechanism and target
    curation to REVIEWED
  outcome: supported
  summary: 'Both Group 1 records (CHEBI:138579 bactobolin A, CHEBI:198310 negamycin)
    carry exact single-molecule ChEBI structures, curated biosynthesis_origin, curator-settled
    mode_of_action (MICROBIAL_TARGET), and source: PRIMARY_LITERATURE (evidence_status:
    PRIMARY_EVIDENCE) molecular_targets, and are now promoted to curation_status:
    REVIEWED with PROMOTED_TO_REVIEWED events.'
  target_ids:
  - CHEBI:138579
  - CHEBI:198310
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
- assessment_id: group2-proposed-exact-quinolones-targets-and-reviewed
  area: completeness
  topic: Population of PRIMARY_LITERATURE molecular_targets and REVIEWED promotion
    on 3 PROPOSED/EXACT quinolones
  outcome: supported
  summary: 'All 3 Group 2 EXACT ChEBI quinolone records (CHEBI:135622 besifloxacin,
    CHEBI:136050 ozenoxacin, CHEBI:94700 pazufloxacin) now carry source: PRIMARY_LITERATURE
    (evidence_status: PRIMARY_EVIDENCE) DNA gyrase and DNA topoisomerase IV molecular_targets
    with reviewed S. pneumoniae, S. aureus, and E. coli UniProtKB protein_examples
    across all 3 records, and are promoted to curation_status: REVIEWED with PROMOTED_TO_REVIEWED
    events.'
  target_ids:
  - CHEBI:135622
  - CHEBI:136050
  - CHEBI:94700
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
- assessment_id: group3-proposed-minted-primary-targets
  area: completeness
  topic: Population of PRIMARY_LITERATURE molecular_targets on 7 PROPOSED/MINTED records
    with curated mode_of_action
  outcome: supported
  summary: 'All 7 Group 3 PROPOSED/MINTED records (cadazolid, radezolid, sutezolid,
    sanfetrinem, tomopenem, albaconazole, quilseconazole) now carry curated source:
    PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets aligned
    with their top-level mode_of_action (plus reviewed C. albicans ERG11 UniProtKB
    protein_examples on albaconazole and documented held_targets rationales on quilseconazole
    and the 5 other Group 3 records in curation/uniprot_protein_examples.yaml), while
    retaining curation_status: PROPOSED under structure_completeness_audit.'
  target_ids:
  - antibioticmech:curator-975acd7c4d
  - antibioticmech:curator-a739fc0555
  - antibioticmech:curator-f56d459cee
  - antibioticmech:curator-daae3d88a3
  - antibioticmech:curator-e14f58e6dc
  - antibioticmech:curator-6bdee75cea
  - antibioticmech:curator-217ed2935e
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
  title: Promoted 2 PROPOSED/EXACT ChEBI records with complete primary mechanism curation
    to REVIEWED
  description: Promoted CHEBI:138579 (bactobolin A) and CHEBI:198310 (negamycin) from
    PROPOSED to REVIEWED via record_curation_event (PROMOTED_TO_REVIEWED) and write_validated_antibiotic.
  target_ids:
  - CHEBI:138579
  - CHEBI:198310
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
    path: data/antibiotics/antibacterial/bactobolin-a.yaml
    role: Curator-owned curation_status and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/negamycin.yaml
    role: Curator-owned curation_status and curation_history
  disposition_reason: 'Resolved in Cycle 3 Stage 5 (Issue #1284): promoted both PROPOSED/EXACT
    records with complete primary mechanism and target curation to REVIEWED.'
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261026T003600Z-cycle3-frozen-inventory-cohort-review
    finding_id: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion
  - repository: culturebotai/AntibioticMech
    review_id: 20261026T003500Z-negamycin-record-review
    finding_id: negamycin-awaiting-reviewed-promotion
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1284
- finding_id: proposed-exact-quinolones-with-moa-missing-primary-targets-and-reviewed-promotion
  issue_key: proposed-exact-quinolones-with-moa-missing-primary-targets-and-reviewed-promotion
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Populated PRIMARY_LITERATURE molecular_targets and promoted 3 PROPOSED/EXACT
    quinolones to REVIEWED
  description: 'Populated source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE)
    DNA gyrase and DNA topoisomerase IV molecular_targets (with reviewed UniProtKB
    protein_examples via apply_uniprot_examples_plan across besifloxacin, ozenoxacin,
    and pazufloxacin) and promoted CHEBI:135622 (besifloxacin), CHEBI:136050 (ozenoxacin),
    and CHEBI:94700 (pazufloxacin) from PROPOSED to REVIEWED via record_curation_event
    (PROMOTED_TO_REVIEWED) and write_validated_antibiotic.'
  target_ids:
  - CHEBI:135622
  - CHEBI:136050
  - CHEBI:94700
  field_paths:
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
    path: data/antibiotics/antibacterial/besifloxacin.yaml
    role: Curator-owned molecular_targets, curation_status, and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/ozenoxacin.yaml
    role: Curator-owned molecular_targets, curation_status, and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/pazufloxacin.yaml
    role: Curator-owned molecular_targets, curation_status, and curation_history
  disposition_reason: 'Resolved in Cycle 3 Stage 5 (Issue #1285): populated PRIMARY_LITERATURE
    molecular_targets and promoted all 3 EXACT ChEBI quinolone records to REVIEWED.'
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261026T003600Z-cycle3-frozen-inventory-cohort-review
    finding_id: proposed-exact-quinolones-with-moa-missing-primary-targets-and-reviewed-promotion
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1285
- finding_id: proposed-minted-records-with-moa-missing-primary-targets
  issue_key: proposed-minted-records-with-moa-missing-primary-targets
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Populated PRIMARY_LITERATURE molecular_targets on 7 PROPOSED/MINTED records
    with curated mode_of_action
  description: 'Populated source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE)
    molecular_targets via record_curation_event and write_validated_antibiotic across
    all 7 Group 3 PROPOSED/MINTED records (cadazolid, radezolid, sutezolid, sanfetrinem,
    tomopenem, albaconazole, quilseconazole), plus reviewed ERG11 UniProtKB protein_examples
    via apply_uniprot_examples_plan on albaconazole and documented held_targets rationales
    on quilseconazole and the 5 other Group 3 records.'
  target_ids:
  - antibioticmech:curator-975acd7c4d
  - antibioticmech:curator-a739fc0555
  - antibioticmech:curator-f56d459cee
  - antibioticmech:curator-daae3d88a3
  - antibioticmech:curator-e14f58e6dc
  - antibioticmech:curator-6bdee75cea
  - antibioticmech:curator-217ed2935e
  field_paths:
  - molecular_targets
  - curation_history
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/cadazolid.yaml
    role: Curator-owned molecular_targets and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/radezolid.yaml
    role: Curator-owned molecular_targets and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sutezolid.yaml
    role: Curator-owned molecular_targets and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/sanfetrinem.yaml
    role: Curator-owned molecular_targets and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/tomopenem.yaml
    role: Curator-owned molecular_targets and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antifungal/albaconazole.yaml
    role: Curator-owned molecular_targets and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antifungal/quilseconazole.yaml
    role: Curator-owned molecular_targets and curation_history
  disposition_reason: 'Resolved in Cycle 3 Stage 5 (Issue #1286): populated PRIMARY_LITERATURE
    molecular_targets on all 7 PROPOSED/MINTED records.'
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261026T003600Z-cycle3-frozen-inventory-cohort-review
    finding_id: proposed-minted-records-with-moa-missing-primary-targets
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1286
actions: []
limitations:
- 'The 7 Group 3 records retain curation_status: PROPOSED and grounding_status: MINTED
  until upstream single-molecule ChEBI identifiers are assigned, per structure_completeness_audit
  policy.'
notes:
- Original Cycle 3 Stage 4 review bundles (20261026T003500Z-negamycin-record-review
  and 20261026T003600Z-cycle3-frozen-inventory-cohort-review) are preserved byte-for-byte.
related_reviews:
- repository: culturebotai/AntibioticMech
  review_id: 20261026T003500Z-negamycin-record-review
  relationship: Predecessor Cycle 3 Stage 4 single-record review of negamycin (CHEBI:198310)
- repository: culturebotai/AntibioticMech
  review_id: 20261026T003600Z-cycle3-frozen-inventory-cohort-review
  relationship: Predecessor Cycle 3 Stage 4 full-inventory cohort review identifying
    the 3 resolved finding groups
tags:
- batch-review
- cycle-03
- stage-05
- remediation-verification
```
