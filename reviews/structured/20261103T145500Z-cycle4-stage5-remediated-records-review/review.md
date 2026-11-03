# Cycle 4 Stage 5 post-remediation review of 11 remediated AntibioticRecord files (Issues #1306, #1307, #1308)

- Review: 20261103T145500Z-cycle4-stage5-remediated-records-review
- Repository: culturebotai/AntibioticMech
- Started UTC: 2026-11-03T14:45:00Z
- Finished UTC: 2026-11-03T14:55:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Post-remediation batch review of the 11 AntibioticRecord YAML files updated in Cycle 4 Stage 5 to resolve all 3 open Stage 4 record and category review findings: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion (Issue #1306, 1 record: squalestatin S1 CHEBI:220211 including companion single-record review 20261103T053500Z-squalestatin-s1-record-review), cycle4-stage1-proposed-exact-natural-products-missing-mechanism-and-targets (Issue #1307, 6 records: diazaquinomycin H CHEBI:199753, diazaquinomycin J CHEBI:225769, jessenipeptin CHEBI:221686, minimycin CHEBI:224130, pamamycin-621A CHEBI:219230, pamamycin-649B CHEBI:198952), and seeded-exact-fluoroquinolones-with-card-only-targets-awaiting-primary-literature-promotion (Issue #1308, 4 records: enoxacin CHEBI:157175, fleroxacin CHEBI:31810, gatifloxacin CHEBI:5280, trovafloxacin CHEBI:9763). Verified that all 11 EXACT ChEBI records carry complete single-molecule chemical_structure, curated biosynthesis_origin, curator-verified mode_of_action and mode_of_action_target_scope, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (with reviewed Swiss-Prot UniProtKB protein_examples on squalestatin S1, minimycin, enoxacin, fleroxacin, gatifloxacin, and trovafloxacin, and documented held_targets rationales on diazaquinomycin H, diazaquinomycin J, jessenipeptin, pamamycin-621A, and pamamycin-649B in curation/uniprot_protein_examples.yaml), and are promoted to curation_status: REVIEWED (raising corpus REVIEWED count from 101 to 112 and reducing the review-readiness worklist from 2,941 to 2,930).

## Scope And Provenance

Complete post-remediation review of all 11 AntibioticRecord YAML files modified in Cycle 4 Stage 5 across resolved finding groups 1-3 (Issues #1306, #1307, #1308).

Selection: All 11 records in Cycle 4 Stage 5 resolved finding groups (Issues #1306, #1307, #1308).
Coverage: full; 11 reviewed / 11 in the declared population.
Source: working_tree at Git base 6d8b6202f8b3bcc40934b6730b1c0d080a244232.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:220211 | data/antibiotics/antifungal/squalestatin-s1.yaml | maintained | squalestatin S1 |
| CHEBI:199753 | data/antibiotics/antibacterial/diazaquinomycin-h.yaml | maintained | diazaquinomycin H |
| CHEBI:225769 | data/antibiotics/antibacterial/diazaquinomycin-j.yaml | maintained | diazaquinomycin J |
| CHEBI:221686 | data/antibiotics/antibacterial/jessenipeptin.yaml | maintained | jessenipeptin |
| CHEBI:224130 | data/antibiotics/antibacterial/minimycin.yaml | maintained | minimycin |
| CHEBI:219230 | data/antibiotics/antibacterial/pamamycin-621a.yaml | maintained | pamamycin-621A |
| CHEBI:198952 | data/antibiotics/antibacterial/pamamycin-649b.yaml | maintained | pamamycin-649B |
| CHEBI:157175 | data/antibiotics/antibacterial/enoxacin.yaml | maintained | enoxacin |
| CHEBI:31810 | data/antibiotics/antibacterial/fleroxacin.yaml | maintained | fleroxacin |
| CHEBI:5280 | data/antibiotics/antibacterial/gatifloxacin.yaml | maintained | gatifloxacin |
| CHEBI:9763 | data/antibiotics/antibacterial/trovafloxacin.yaml | maintained | trovafloxacin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and OAK ontology-label validation | passed | True | CHEBI:220211, CHEBI:199753, CHEBI:225769, CHEBI:221686, CHEBI:224130, CHEBI:219230, CHEBI:198952, CHEBI:157175, CHEBI:31810, CHEBI:5280, CHEBI:9763 | All 3,042 corpus records, including the 11 remediated records, pass closed LinkML schema validation and OAK label correspondence with 0 errors. |
| Full corpus seed reproduction check | passed | True | CHEBI:220211, CHEBI:199753, CHEBI:225769, CHEBI:221686, CHEBI:224130, CHEBI:219230, CHEBI:198952, CHEBI:157175, CHEBI:31810, CHEBI:5280, CHEBI:9763 | All 3,042 records reproduce byte-for-byte from data/raw/ plus curator inputs with 0 missing, 0 unexpected, and 0 drifted fields. |
| UniProt protein examples and causal graphs curation test suites | passed | True | CHEBI:220211, CHEBI:199753, CHEBI:225769, CHEBI:221686, CHEBI:224130, CHEBI:219230, CHEBI:198952, CHEBI:157175, CHEBI:31810, CHEBI:5280, CHEBI:9763 | All 160 tests across test_uniprot_protein_examples.py, test_causal_graphs_curation.py, test_review_readiness_queue.py, and test_embeddings.py pass with exit code 0. |

## Scientific And Domain Assessments

### Promotion of squalestatin S1 (CHEBI:220211) with complete mechanism and target curation to REVIEWED

completeness: supported. Targets: CHEBI:220211.

Squalestatin S1 (CHEBI:220211) carries an exact single-molecule ChEBI structure, curated biosynthesis_origin (NATURAL_PRODUCT), curator-settled mode_of_action (ERGOSTEROL_PATHWAY_INHIBITION, HOST_SHARED_TARGET), and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (fungal squalene synthase (Erg9); GO:0051996) with 3 reviewed UniProtKB protein_examples (UniProtKB:P78589, UniProtKB:A0A1D8PI71, UniProtKB:P29704), and is now promoted to curation_status: REVIEWED with a PROMOTED_TO_REVIEWED curation event.

### Population of mode_of_action, PRIMARY_LITERATURE molecular_targets, and REVIEWED promotion on 6 Cycle 4 Stage 1 EXACT natural products

completeness: supported. Targets: CHEBI:199753, CHEBI:225769, CHEBI:221686, CHEBI:224130, CHEBI:219230, CHEBI:198952.

All 6 Cycle 4 Stage 1 EXACT natural-product records (diazaquinomycin H CHEBI:199753, diazaquinomycin J CHEBI:225769, jessenipeptin CHEBI:221686, minimycin CHEBI:224130, pamamycin-621A CHEBI:219230, pamamycin-649B CHEBI:198952) now carry curated mode_of_action, mode_of_action_target_scope, CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (with 2 reviewed E. coli rpoB/rpoC UniProtKB protein_examples UniProtKB:P0A8V2 and UniProtKB:P0A8T7 on minimycin's GO:0000428 DNA-directed RNA polymerase complex target and documented held_targets rationales on the other 5 records in curation/uniprot_protein_examples.yaml), and are promoted to curation_status: REVIEWED.

### Population of PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples, and REVIEWED promotion on 4 SEEDED/EXACT fluoroquinolones

completeness: supported. Targets: CHEBI:157175, CHEBI:31810, CHEBI:5280, CHEBI:9763.

All 4 Group 3 EXACT fluoroquinolone records (enoxacin CHEBI:157175, fleroxacin CHEBI:31810, gatifloxacin CHEBI:5280, trovafloxacin CHEBI:9763) now carry biosynthesis_origin: SYNTHETIC, MICROBIAL_TARGET mode_of_action_target_scope, CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) bacterial DNA gyrase (GyrA/GyrB) and topoisomerase IV (ParC/ParE) molecular_targets (PROTEIN_COMPLEX, DIRECT_BINDING_TARGET, NCBITaxon:2 Bacteria) with 4 reviewed E. coli K-12 Swiss-Prot UniProtKB protein_examples per record (UniProtKB:P0AES4 gyrA, UniProtKB:P0AES6 gyrB, UniProtKB:P0AFI2 parC, UniProtKB:P20083 parE; 16 total across the 4 records, citing DOI:10.1128/AAC.45.12.3544-3547.2001 / PMID:11709337), and are promoted from SEEDED to REVIEWED.

## Findings

### proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion: Promoted squalestatin S1 (CHEBI:220211) with complete primary mechanism and target curation to REVIEWED

major / resolved / confirmed; issue key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion.

Promoted CHEBI:220211 (squalestatin S1) from PROPOSED to REVIEWED via record_curation_event (PROMOTED_TO_REVIEWED) and write_validated_antibiotic, and registered its held_records entry in curation/causal_graphs.yaml.

Disposition: Resolved in Cycle 4 Stage 5 (Issue #1306): promoted squalestatin S1 (CHEBI:220211) from PROPOSED to REVIEWED.

### cycle4-stage1-proposed-exact-natural-products-missing-mechanism-and-targets: Populated mode_of_action, PRIMARY_LITERATURE molecular_targets, and promoted 6 Cycle 4 Stage 1 EXACT natural products to REVIEWED

major / resolved / confirmed; issue key: cycle4-stage1-proposed-exact-natural-products-missing-mechanism-and-targets.

Curated mode_of_action, mode_of_action_target_scope, CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (with reviewed E. coli rpoB/rpoC UniProtKB protein_examples UniProtKB:P0A8V2 and UniProtKB:P0A8T7 on minimycin's GO:0000428 DNA-directed RNA polymerase complex target and documented held_targets rationales on diazaquinomycin H, diazaquinomycin J, jessenipeptin, pamamycin-621A, and pamamycin-649B via apply_uniprot_examples_plan), and promoted all 6 records from PROPOSED to REVIEWED via record_curation_event and write_validated_antibiotic.

Disposition: Resolved in Cycle 4 Stage 5 (Issue #1307): curated mode_of_action and PRIMARY_LITERATURE molecular_targets and promoted all 6 Cycle 4 Stage 1 EXACT natural products to REVIEWED.

### seeded-exact-fluoroquinolones-with-card-only-targets-awaiting-primary-literature-promotion: Populated PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples, and promoted 4 EXACT fluoroquinolones to REVIEWED

major / resolved / confirmed; issue key: seeded-exact-fluoroquinolones-with-card-only-targets-awaiting-primary-literature-promotion.

Curated biosynthesis_origin: SYNTHETIC, MICROBIAL_TARGET mode_of_action_target_scope, CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) bacterial DNA gyrase (GyrA/GyrB) and topoisomerase IV (ParC/ParE) molecular_targets (PROTEIN_COMPLEX, DIRECT_BINDING_TARGET, NCBITaxon:2 Bacteria; DOI:10.1128/AAC.45.12.3544-3547.2001 / PMID:11709337) with 16 reviewed E. coli K-12 Swiss-Prot UniProtKB protein_examples (UniProtKB:P0AES4, UniProtKB:P0AES6, UniProtKB:P0AFI2, UniProtKB:P20083 on each record) across enoxacin (CHEBI:157175), fleroxacin (CHEBI:31810), gatifloxacin (CHEBI:5280), and trovafloxacin (CHEBI:9763) via apply_uniprot_examples_plan, and promoted all 4 records from SEEDED to REVIEWED via record_curation_event and write_validated_antibiotic.

Disposition: Resolved in Cycle 4 Stage 5 (Issue #1308): populated PRIMARY_LITERATURE molecular_targets and reviewed UniProtKB protein_examples and promoted all 4 EXACT ChEBI fluoroquinolones to REVIEWED.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| remediated-records-content | curation/record_review_queue.tsv; 11 remediated YAML records and refreshed review-readiness worklist (2,930 items) | supports | All 11 records were updated through native validated writers (write_validated_antibiotic, apply_uniprot_examples_plan, record_curation_event): 1 Group 1 PROPOSED/EXACT record (squalestatin S1 CHEBI:220211) promoted to REVIEWED; 6 Group 2 Cycle 4 Stage 1 PROPOSED/EXACT natural products (diazaquinomycin H CHEBI:199753, diazaquinomycin J CHEBI:225769, jessenipeptin CHEBI:221686, minimycin CHEBI:224130, pamamycin-621A CHEBI:219230, pamamycin-649B CHEBI:198952) populated with curated mode_of_action and PRIMARY_LITERATURE molecular_targets and promoted to REVIEWED; and 4 Group 3 SEEDED/EXACT fluoroquinolones (enoxacin CHEBI:157175, fleroxacin CHEBI:31810, gatifloxacin CHEBI:5280, trovafloxacin CHEBI:9763) populated with biosynthesis_origin: SYNTHETIC, MICROBIAL_TARGET mode_of_action, and PRIMARY_LITERATURE molecular_targets with reviewed UniProtKB protein_examples and promoted to REVIEWED (raising corpus REVIEWED count from 101 to 112 and reducing the review-readiness queue from 2,941 to 2,930). |
| validate-strict-pass | scripts/validate_strict.py; 3042 files scanned, 0 files with ERROR, 0 total ERROR rows | supports | Closed-mode LinkML validation and OAK ontology label verification pass across all 3,042 records. |
| verify-corpus-pass | scripts/verify_corpus.py; records expected: 3042, on disk: 3042, missing: 0, unexpected: 0, drifted fields: 0 | supports | Every curator-owned edit on the 11 remediated records survives seed_from_sources.py reproduction without drift. |
| primary-literature-sources | PMID:1624366, PMID:8419946, PMID:27032439, PMID:25893226, PMID:30110167, PMID:29592954, PMID:31535140, PMID:31816530, PMID:7490225, PMID:19924823, DOI:10.1002/chem.201102093, PMID:11709337; Primary experimental mechanism and target studies cited across the 11 remediated records | supports | Primary studies support REVIEWED promotion on squalestatin S1 (PMID:1624366, PMID:8419946, PMID:27032439), mode_of_action, PRIMARY_LITERATURE molecular_targets, and REVIEWED promotion on the 6 Cycle 4 Stage 1 natural products (diazaquinomycin H and J DOI:10.1021/acsinfecdis.5b00005 / PMID:25893226 and DOI:10.1021/acs.jnatprod.8b00394 / PMID:30110167, jessenipeptin DOI:10.1073/pnas.1721790115 / PMID:29592954, minimycin DOI:10.1093/nar/gkz782 / PMID:31535140 and DOI:10.1016/j.isci.2019.11.037 / PMID:31816530, pamamycin-621A DOI:10.7164/antibiotics.48.1159 / PMID:7490225 and DOI:10.1021/ol902290v / PMID:19924823, pamamycin-649B DOI:10.7164/antibiotics.48.1159 / PMID:7490225 and DOI:10.1002/chem.201102093), and PRIMARY_LITERATURE bacterial DNA gyrase (GyrA/GyrB) and topoisomerase IV (ParC/ParE) molecular_targets with reviewed E. coli UniProtKB protein_examples (UniProtKB:P0AES4, UniProtKB:P0AES6, UniProtKB:P0AFI2, UniProtKB:P20083) and REVIEWED promotion on the 4 EXACT fluoroquinolones (enoxacin, fleroxacin, gatifloxacin, and trovafloxacin; DOI:10.1128/AAC.45.12.3544-3547.2001 / PMID:11709337). |

## Limits And Additional Notes

- All 11 newly promoted REVIEWED records are registered in curation/causal_graphs.yaml held_records awaiting multi-step primary-literature causal_graphs in a subsequent Stage 2 goal.
- Original Cycle 4 Stage 4 review bundles (20261103T053500Z-squalestatin-s1-record-review and 20261103T053600Z-cycle4-frozen-inventory-cohort-review) are preserved byte-for-byte.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T145500Z-cycle4-stage5-remediated-records-review
kind: batch
repository: culturebotai/AntibioticMech
title: 'Cycle 4 Stage 5 post-remediation review of 11 remediated AntibioticRecord
  files (Issues #1306, #1307, #1308)'
started_at: '2026-11-03T14:45:00Z'
finished_at: '2026-11-03T14:55:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Cycle 4 Stage 5 post-remediation verification review of the
    11 remediated records prior to independent adversarial PR review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass
native_verdict: PASS
scientific_review: true
summary: 'Post-remediation batch review of the 11 AntibioticRecord YAML files updated
  in Cycle 4 Stage 5 to resolve all 3 open Stage 4 record and category review findings:
  proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion (Issue #1306,
  1 record: squalestatin S1 CHEBI:220211 including companion single-record review
  20261103T053500Z-squalestatin-s1-record-review), cycle4-stage1-proposed-exact-natural-products-missing-mechanism-and-targets
  (Issue #1307, 6 records: diazaquinomycin H CHEBI:199753, diazaquinomycin J CHEBI:225769,
  jessenipeptin CHEBI:221686, minimycin CHEBI:224130, pamamycin-621A CHEBI:219230,
  pamamycin-649B CHEBI:198952), and seeded-exact-fluoroquinolones-with-card-only-targets-awaiting-primary-literature-promotion
  (Issue #1308, 4 records: enoxacin CHEBI:157175, fleroxacin CHEBI:31810, gatifloxacin
  CHEBI:5280, trovafloxacin CHEBI:9763). Verified that all 11 EXACT ChEBI records
  carry complete single-molecule chemical_structure, curated biosynthesis_origin,
  curator-verified mode_of_action and mode_of_action_target_scope, and source: PRIMARY_LITERATURE
  (evidence_status: PRIMARY_EVIDENCE) molecular_targets (with reviewed Swiss-Prot
  UniProtKB protein_examples on squalestatin S1, minimycin, enoxacin, fleroxacin,
  gatifloxacin, and trovafloxacin, and documented held_targets rationales on diazaquinomycin
  H, diazaquinomycin J, jessenipeptin, pamamycin-621A, and pamamycin-649B in curation/uniprot_protein_examples.yaml),
  and are promoted to curation_status: REVIEWED (raising corpus REVIEWED count from
  101 to 112 and reducing the review-readiness worklist from 2,941 to 2,930).'
source:
  git_revision: 6d8b6202f8b3bcc40934b6730b1c0d080a244232
  state: working_tree
  inputs:
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: 4c438f137570d6c75a208422f04c0ad21873f5ee467f230a43ec8ed9709d2178
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: curation/causal_graphs.yaml
    sha256: 26d3e3dbd068107c9d2c539e273465251a8730c981b66d920195ef54bb8bbd09
    role: context
  - path: curation/curator_antibiotics.tsv
    sha256: 9ddfcab29e24f39ab5c3850104fee40a0c4b98f0ba26f5e92f08aa6cdbade470
    role: context
  - path: curation/cycle4_stage5_review_remediation_transition.json
    sha256: 94b65a2d6925394cb1e2af480ede6bf0bf4e529bcd5ba295804997342c2e2cc4
    role: context
  - path: curation/record_review_queue.tsv
    sha256: 04f5b80d2e1bc041cc98d4efee194b6f57c61b0e6f770c9631bb3971ceffec40
    role: context
  - path: curation/uniprot_protein_examples.yaml
    sha256: 1ebd4e6d8cff7e10bb883e04cc8d48f9a6d626e2628528ac56f442206e568363
    role: context
  - path: curation/uniprot_protein_examples_transition.json
    sha256: 55243bb2c76d62d502dbb316770ecad3a23b38e8220c7eec7d2ffe10b10c2921
    role: context
  - path: data/antibiotics/antibacterial/diazaquinomycin-h.yaml
    sha256: 2e996a7e10322000f8119e6c878d81bdd5d675893318f2f85b292dfb9bdde7ab
    role: target
  - path: data/antibiotics/antibacterial/diazaquinomycin-j.yaml
    sha256: 071eb52e5ec5344a5e8b9be8b72ef24aad5ae0161240b45a51fbb39ab1ec9323
    role: target
  - path: data/antibiotics/antibacterial/enoxacin.yaml
    sha256: 19868f9e3c38efc0b2e484ae22cf6b24603de25b63a8d7a9f238398daba79fb0
    role: target
  - path: data/antibiotics/antibacterial/fleroxacin.yaml
    sha256: 4c6b74bec30ae3c023dfa9c1f21d52bbf0a67a50d70b863964717d66d9295178
    role: target
  - path: data/antibiotics/antibacterial/gatifloxacin.yaml
    sha256: c60c434f45eed1be8caf48595ee471f4add5a1f362adace6173415ff1545f6c3
    role: target
  - path: data/antibiotics/antibacterial/jessenipeptin.yaml
    sha256: eec406751796902db4016cd7578277a02d6019783d74ce256d303a31ba2fa4d2
    role: target
  - path: data/antibiotics/antibacterial/minimycin.yaml
    sha256: 788a155366c454936918cb00390f192cc2e643d6fe6aa52314edbdddf4e396b7
    role: target
  - path: data/antibiotics/antibacterial/pamamycin-621a.yaml
    sha256: 30d947def6c1f5f3e30a4cd3486b5480df22eae24e772840858d5f857976c44a
    role: target
  - path: data/antibiotics/antibacterial/pamamycin-649b.yaml
    sha256: a611cc9291d0abb58bd67b3ca6f61b27eec004389a213efbf08fac670ea156c8
    role: target
  - path: data/antibiotics/antibacterial/trovafloxacin.yaml
    sha256: 581e21595ea69540bb9f3f0f9935a21075add8b14bc780669c138271241cfbf4
    role: target
  - path: data/antibiotics/antifungal/squalestatin-s1.yaml
    sha256: 35d3cba06abb2d76d6c876d97e1a5787d12d64143d220ca6f8a17252a650a460
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
  description: 'Complete post-remediation review of all 11 AntibioticRecord YAML files
    modified in Cycle 4 Stage 5 across resolved finding groups 1-3 (Issues #1306,
    #1307, #1308).'
  selection: 'All 11 records in Cycle 4 Stage 5 resolved finding groups (Issues #1306,
    #1307, #1308).'
  coverage: full
  population_size: 11
  reviewed_target_ids:
  - CHEBI:220211
  - CHEBI:199753
  - CHEBI:225769
  - CHEBI:221686
  - CHEBI:224130
  - CHEBI:219230
  - CHEBI:198952
  - CHEBI:157175
  - CHEBI:31810
  - CHEBI:5280
  - CHEBI:9763
targets:
- target_id: CHEBI:220211
  path: data/antibiotics/antifungal/squalestatin-s1.yaml
  label: squalestatin S1
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antifungal/squalestatin-s1.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:199753
  path: data/antibiotics/antibacterial/diazaquinomycin-h.yaml
  label: diazaquinomycin H
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/diazaquinomycin-h.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:225769
  path: data/antibiotics/antibacterial/diazaquinomycin-j.yaml
  label: diazaquinomycin J
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/diazaquinomycin-j.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:221686
  path: data/antibiotics/antibacterial/jessenipeptin.yaml
  label: jessenipeptin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/jessenipeptin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:224130
  path: data/antibiotics/antibacterial/minimycin.yaml
  label: minimycin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/minimycin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:219230
  path: data/antibiotics/antibacterial/pamamycin-621a.yaml
  label: pamamycin-621A
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/pamamycin-621a.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:198952
  path: data/antibiotics/antibacterial/pamamycin-649b.yaml
  label: pamamycin-649B
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/pamamycin-649b.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:157175
  path: data/antibiotics/antibacterial/enoxacin.yaml
  label: enoxacin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/enoxacin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:31810
  path: data/antibiotics/antibacterial/fleroxacin.yaml
  label: fleroxacin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/fleroxacin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:5280
  path: data/antibiotics/antibacterial/gatifloxacin.yaml
  label: gatifloxacin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/gatifloxacin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, biosynthesis_origin,
      mode_of_action, mode_of_action_target_scope, mode_of_action_notes, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:9763
  path: data/antibiotics/antibacterial/trovafloxacin.yaml
  label: trovafloxacin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/trovafloxacin.yaml
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
  command: .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  exit_code: 0
  summary: All 3,042 corpus records, including the 11 remediated records, pass closed
    LinkML schema validation and OAK label correspondence with 0 errors.
  target_ids:
  - CHEBI:220211
  - CHEBI:199753
  - CHEBI:225769
  - CHEBI:221686
  - CHEBI:224130
  - CHEBI:219230
  - CHEBI:198952
  - CHEBI:157175
  - CHEBI:31810
  - CHEBI:5280
  - CHEBI:9763
  evidence_ids:
  - validate-strict-pass
  - remediated-records-content
- check_id: corpus-reproduction-remediated-records
  name: Full corpus seed reproduction check
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py
  exit_code: 0
  summary: All 3,042 records reproduce byte-for-byte from data/raw/ plus curator inputs
    with 0 missing, 0 unexpected, and 0 drifted fields.
  target_ids:
  - CHEBI:220211
  - CHEBI:199753
  - CHEBI:225769
  - CHEBI:221686
  - CHEBI:224130
  - CHEBI:219230
  - CHEBI:198952
  - CHEBI:157175
  - CHEBI:31810
  - CHEBI:5280
  - CHEBI:9763
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
  summary: All 160 tests across test_uniprot_protein_examples.py, test_causal_graphs_curation.py,
    test_review_readiness_queue.py, and test_embeddings.py pass with exit code 0.
  target_ids:
  - CHEBI:220211
  - CHEBI:199753
  - CHEBI:225769
  - CHEBI:221686
  - CHEBI:224130
  - CHEBI:219230
  - CHEBI:198952
  - CHEBI:157175
  - CHEBI:31810
  - CHEBI:5280
  - CHEBI:9763
  evidence_ids:
  - remediated-records-content
evidence:
- evidence_id: remediated-records-content
  kind: record_content
  reference: curation/record_review_queue.tsv
  locator: 11 remediated YAML records and refreshed review-readiness worklist (2,930
    items)
  accessed_at: '2026-11-03T14:50:00Z'
  support: supports
  snapshot_sha256: 04f5b80d2e1bc041cc98d4efee194b6f57c61b0e6f770c9631bb3971ceffec40
  summary: 'All 11 records were updated through native validated writers (write_validated_antibiotic,
    apply_uniprot_examples_plan, record_curation_event): 1 Group 1 PROPOSED/EXACT
    record (squalestatin S1 CHEBI:220211) promoted to REVIEWED; 6 Group 2 Cycle 4
    Stage 1 PROPOSED/EXACT natural products (diazaquinomycin H CHEBI:199753, diazaquinomycin
    J CHEBI:225769, jessenipeptin CHEBI:221686, minimycin CHEBI:224130, pamamycin-621A
    CHEBI:219230, pamamycin-649B CHEBI:198952) populated with curated mode_of_action
    and PRIMARY_LITERATURE molecular_targets and promoted to REVIEWED; and 4 Group
    3 SEEDED/EXACT fluoroquinolones (enoxacin CHEBI:157175, fleroxacin CHEBI:31810,
    gatifloxacin CHEBI:5280, trovafloxacin CHEBI:9763) populated with biosynthesis_origin:
    SYNTHETIC, MICROBIAL_TARGET mode_of_action, and PRIMARY_LITERATURE molecular_targets
    with reviewed UniProtKB protein_examples and promoted to REVIEWED (raising corpus
    REVIEWED count from 101 to 112 and reducing the review-readiness queue from 2,941
    to 2,930).'
- evidence_id: validate-strict-pass
  kind: validation
  reference: scripts/validate_strict.py
  locator: 3042 files scanned, 0 files with ERROR, 0 total ERROR rows
  accessed_at: '2026-11-03T14:51:00Z'
  support: supports
  snapshot_sha256: d70e6739c881260927dfc99abea16e56be0f34f353f9f95353a43da76e8e7217
  summary: Closed-mode LinkML validation and OAK ontology label verification pass
    across all 3,042 records.
- evidence_id: verify-corpus-pass
  kind: validation
  reference: scripts/verify_corpus.py
  locator: 'records expected: 3042, on disk: 3042, missing: 0, unexpected: 0, drifted
    fields: 0'
  accessed_at: '2026-11-03T14:52:00Z'
  support: supports
  snapshot_sha256: 7d881f9b4e17b02d7f3ec3eb48404ad0a41a0cefa915edc9a442f755b834df78
  summary: Every curator-owned edit on the 11 remediated records survives seed_from_sources.py
    reproduction without drift.
- evidence_id: primary-literature-sources
  kind: primary_source
  reference: PMID:1624366, PMID:8419946, PMID:27032439, PMID:25893226, PMID:30110167,
    PMID:29592954, PMID:31535140, PMID:31816530, PMID:7490225, PMID:19924823, DOI:10.1002/chem.201102093,
    PMID:11709337
  locator: Primary experimental mechanism and target studies cited across the 11 remediated
    records
  accessed_at: '2026-11-03T14:50:00Z'
  support: supports
  summary: Primary studies support REVIEWED promotion on squalestatin S1 (PMID:1624366,
    PMID:8419946, PMID:27032439), mode_of_action, PRIMARY_LITERATURE molecular_targets,
    and REVIEWED promotion on the 6 Cycle 4 Stage 1 natural products (diazaquinomycin
    H and J DOI:10.1021/acsinfecdis.5b00005 / PMID:25893226 and DOI:10.1021/acs.jnatprod.8b00394
    / PMID:30110167, jessenipeptin DOI:10.1073/pnas.1721790115 / PMID:29592954, minimycin
    DOI:10.1093/nar/gkz782 / PMID:31535140 and DOI:10.1016/j.isci.2019.11.037 / PMID:31816530,
    pamamycin-621A DOI:10.7164/antibiotics.48.1159 / PMID:7490225 and DOI:10.1021/ol902290v
    / PMID:19924823, pamamycin-649B DOI:10.7164/antibiotics.48.1159 / PMID:7490225
    and DOI:10.1002/chem.201102093), and PRIMARY_LITERATURE bacterial DNA gyrase (GyrA/GyrB)
    and topoisomerase IV (ParC/ParE) molecular_targets with reviewed E. coli UniProtKB
    protein_examples (UniProtKB:P0AES4, UniProtKB:P0AES6, UniProtKB:P0AFI2, UniProtKB:P20083)
    and REVIEWED promotion on the 4 EXACT fluoroquinolones (enoxacin, fleroxacin,
    gatifloxacin, and trovafloxacin; DOI:10.1128/AAC.45.12.3544-3547.2001 / PMID:11709337).
assessments:
- assessment_id: group1-squalestatin-s1-promoted-to-reviewed
  area: completeness
  topic: Promotion of squalestatin S1 (CHEBI:220211) with complete mechanism and target
    curation to REVIEWED
  outcome: supported
  summary: 'Squalestatin S1 (CHEBI:220211) carries an exact single-molecule ChEBI
    structure, curated biosynthesis_origin (NATURAL_PRODUCT), curator-settled mode_of_action
    (ERGOSTEROL_PATHWAY_INHIBITION, HOST_SHARED_TARGET), and source: PRIMARY_LITERATURE
    (evidence_status: PRIMARY_EVIDENCE) molecular_targets (fungal squalene synthase
    (Erg9); GO:0051996) with 3 reviewed UniProtKB protein_examples (UniProtKB:P78589,
    UniProtKB:A0A1D8PI71, UniProtKB:P29704), and is now promoted to curation_status:
    REVIEWED with a PROMOTED_TO_REVIEWED curation event.'
  target_ids:
  - CHEBI:220211
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
- assessment_id: group2-cycle4-stage1-natural-products-moa-targets-and-reviewed
  area: completeness
  topic: Population of mode_of_action, PRIMARY_LITERATURE molecular_targets, and REVIEWED
    promotion on 6 Cycle 4 Stage 1 EXACT natural products
  outcome: supported
  summary: 'All 6 Cycle 4 Stage 1 EXACT natural-product records (diazaquinomycin H
    CHEBI:199753, diazaquinomycin J CHEBI:225769, jessenipeptin CHEBI:221686, minimycin
    CHEBI:224130, pamamycin-621A CHEBI:219230, pamamycin-649B CHEBI:198952) now carry
    curated mode_of_action, mode_of_action_target_scope, CURATOR mode_of_action_notes,
    and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets
    (with 2 reviewed E. coli rpoB/rpoC UniProtKB protein_examples UniProtKB:P0A8V2
    and UniProtKB:P0A8T7 on minimycin''s GO:0000428 DNA-directed RNA polymerase complex
    target and documented held_targets rationales on the other 5 records in curation/uniprot_protein_examples.yaml),
    and are promoted to curation_status: REVIEWED.'
  target_ids:
  - CHEBI:199753
  - CHEBI:225769
  - CHEBI:221686
  - CHEBI:224130
  - CHEBI:219230
  - CHEBI:198952
  evidence_ids:
  - remediated-records-content
  - primary-literature-sources
  - validate-strict-pass
  - verify-corpus-pass
- assessment_id: group3-seeded-exact-fluoroquinolones-primary-targets-and-reviewed
  area: completeness
  topic: Population of PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples,
    and REVIEWED promotion on 4 SEEDED/EXACT fluoroquinolones
  outcome: supported
  summary: 'All 4 Group 3 EXACT fluoroquinolone records (enoxacin CHEBI:157175, fleroxacin
    CHEBI:31810, gatifloxacin CHEBI:5280, trovafloxacin CHEBI:9763) now carry biosynthesis_origin:
    SYNTHETIC, MICROBIAL_TARGET mode_of_action_target_scope, CURATOR mode_of_action_notes,
    and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) bacterial DNA
    gyrase (GyrA/GyrB) and topoisomerase IV (ParC/ParE) molecular_targets (PROTEIN_COMPLEX,
    DIRECT_BINDING_TARGET, NCBITaxon:2 Bacteria) with 4 reviewed E. coli K-12 Swiss-Prot
    UniProtKB protein_examples per record (UniProtKB:P0AES4 gyrA, UniProtKB:P0AES6
    gyrB, UniProtKB:P0AFI2 parC, UniProtKB:P20083 parE; 16 total across the 4 records,
    citing DOI:10.1128/AAC.45.12.3544-3547.2001 / PMID:11709337), and are promoted
    from SEEDED to REVIEWED.'
  target_ids:
  - CHEBI:157175
  - CHEBI:31810
  - CHEBI:5280
  - CHEBI:9763
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
  title: Promoted squalestatin S1 (CHEBI:220211) with complete primary mechanism and
    target curation to REVIEWED
  description: Promoted CHEBI:220211 (squalestatin S1) from PROPOSED to REVIEWED via
    record_curation_event (PROMOTED_TO_REVIEWED) and write_validated_antibiotic, and
    registered its held_records entry in curation/causal_graphs.yaml.
  target_ids:
  - CHEBI:220211
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
    path: data/antibiotics/antifungal/squalestatin-s1.yaml
    role: Curator-owned curation_status and curation_history
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (Issue #1306): promoted squalestatin
    S1 (CHEBI:220211) from PROPOSED to REVIEWED.'
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261103T053600Z-cycle4-frozen-inventory-cohort-review
    finding_id: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion
  - repository: culturebotai/AntibioticMech
    review_id: 20261103T053500Z-squalestatin-s1-record-review
    finding_id: squalestatin-s1-awaiting-reviewed-promotion
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1306
- finding_id: cycle4-stage1-proposed-exact-natural-products-missing-mechanism-and-targets
  issue_key: cycle4-stage1-proposed-exact-natural-products-missing-mechanism-and-targets
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Populated mode_of_action, PRIMARY_LITERATURE molecular_targets, and promoted
    6 Cycle 4 Stage 1 EXACT natural products to REVIEWED
  description: 'Curated mode_of_action, mode_of_action_target_scope, CURATOR mode_of_action_notes,
    and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets
    (with reviewed E. coli rpoB/rpoC UniProtKB protein_examples UniProtKB:P0A8V2 and
    UniProtKB:P0A8T7 on minimycin''s GO:0000428 DNA-directed RNA polymerase complex
    target and documented held_targets rationales on diazaquinomycin H, diazaquinomycin
    J, jessenipeptin, pamamycin-621A, and pamamycin-649B via apply_uniprot_examples_plan),
    and promoted all 6 records from PROPOSED to REVIEWED via record_curation_event
    and write_validated_antibiotic.'
  target_ids:
  - CHEBI:199753
  - CHEBI:225769
  - CHEBI:221686
  - CHEBI:224130
  - CHEBI:219230
  - CHEBI:198952
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
    path: data/antibiotics/antibacterial/diazaquinomycin-h.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/diazaquinomycin-j.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/jessenipeptin.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/minimycin.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/pamamycin-621a.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/pamamycin-649b.yaml
    role: Curator-owned mode_of_action, molecular_targets, curation_status, and curation_history
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (Issue #1307): curated mode_of_action
    and PRIMARY_LITERATURE molecular_targets and promoted all 6 Cycle 4 Stage 1 EXACT
    natural products to REVIEWED.'
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261103T053600Z-cycle4-frozen-inventory-cohort-review
    finding_id: cycle4-stage1-proposed-exact-natural-products-missing-mechanism-and-targets
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1307
- finding_id: seeded-exact-fluoroquinolones-with-card-only-targets-awaiting-primary-literature-promotion
  issue_key: seeded-exact-fluoroquinolones-with-card-only-targets-awaiting-primary-literature-promotion
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Populated PRIMARY_LITERATURE molecular_targets, reviewed UniProtKB protein_examples,
    and promoted 4 EXACT fluoroquinolones to REVIEWED
  description: 'Curated biosynthesis_origin: SYNTHETIC, MICROBIAL_TARGET mode_of_action_target_scope,
    CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status:
    PRIMARY_EVIDENCE) bacterial DNA gyrase (GyrA/GyrB) and topoisomerase IV (ParC/ParE)
    molecular_targets (PROTEIN_COMPLEX, DIRECT_BINDING_TARGET, NCBITaxon:2 Bacteria;
    DOI:10.1128/AAC.45.12.3544-3547.2001 / PMID:11709337) with 16 reviewed E. coli
    K-12 Swiss-Prot UniProtKB protein_examples (UniProtKB:P0AES4, UniProtKB:P0AES6,
    UniProtKB:P0AFI2, UniProtKB:P20083 on each record) across enoxacin (CHEBI:157175),
    fleroxacin (CHEBI:31810), gatifloxacin (CHEBI:5280), and trovafloxacin (CHEBI:9763)
    via apply_uniprot_examples_plan, and promoted all 4 records from SEEDED to REVIEWED
    via record_curation_event and write_validated_antibiotic.'
  target_ids:
  - CHEBI:157175
  - CHEBI:31810
  - CHEBI:5280
  - CHEBI:9763
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
    path: data/antibiotics/antibacterial/enoxacin.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/fleroxacin.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/gatifloxacin.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/trovafloxacin.yaml
    role: Curator-owned biosynthesis_origin, mode_of_action, molecular_targets, curation_status,
      and curation_history
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (Issue #1308): populated PRIMARY_LITERATURE
    molecular_targets and reviewed UniProtKB protein_examples and promoted all 4 EXACT
    ChEBI fluoroquinolones to REVIEWED.'
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261103T053600Z-cycle4-frozen-inventory-cohort-review
    finding_id: seeded-exact-fluoroquinolones-with-card-only-targets-awaiting-primary-literature-promotion
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1308
actions: []
limitations:
- All 11 newly promoted REVIEWED records are registered in curation/causal_graphs.yaml
  held_records awaiting multi-step primary-literature causal_graphs in a subsequent
  Stage 2 goal.
notes:
- Original Cycle 4 Stage 4 review bundles (20261103T053500Z-squalestatin-s1-record-review
  and 20261103T053600Z-cycle4-frozen-inventory-cohort-review) are preserved byte-for-byte.
related_reviews:
- repository: culturebotai/AntibioticMech
  review_id: 20261103T053500Z-squalestatin-s1-record-review
  relationship: Predecessor Cycle 4 Stage 4 single-record review of squalestatin S1
    (CHEBI:220211)
- repository: culturebotai/AntibioticMech
  review_id: 20261103T053600Z-cycle4-frozen-inventory-cohort-review
  relationship: Predecessor Cycle 4 Stage 4 full-inventory cohort review identifying
    the 3 resolved finding groups
tags:
- batch-review
- cycle-04
- stage-05
- remediation-verification
```
