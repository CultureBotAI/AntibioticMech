# Stage 5 post-remediation review of 11 remediated AntibioticRecord files (Issues #1253, #1254, #1255)

- Review: 20261023T184800Z-stage5-remediated-records-review
- Repository: culturebotai/AntibioticMech
- Started UTC: 2026-10-23T18:35:00Z
- Finished UTC: 2026-10-23T18:48:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Post-remediation batch review of the 11 AntibioticRecord YAML files updated in Stage 5 to resolve Stage 4 findings rifampicin-moa-scope-leftover (Issue #1253), seeded-causal-graphs-missing-primary-targets (Issue #1254), and seeded-causal-graphs-unsettled-moa-and-targets (Issue #1255). Verified that CHEBI:28077 (rifampicin) now carries mode_of_action_target_scope: MICROBIAL_TARGET; that all 10 formerly SEEDED records with primary-literature causal_graphs (clarithromycin, nalidixic acid, norfloxacin, pefloxacin, ciprofloxacin, daptomycin, levofloxacin, trimethoprim, delavirdine, nevirapine) now carry curator-settled mode_of_action, source: PRIMARY_LITERATURE molecular_targets (with reviewed UniProtKB protein_examples on all 8 protein-target records), and curation_status: REVIEWED; and that validate_strict.py, verify_corpus.py, and all 91 causal-graph/UniProt curation tests pass with 0 errors.

## Scope And Provenance

Complete post-remediation review of the 11 AntibioticRecord YAML files modified in Stage 5 (Groups 1-3: CHEBI:28077, CHEBI:3732, CHEBI:100147, CHEBI:100246, CHEBI:50199, CHEBI:100241, CHEBI:600103, CHEBI:63598, CHEBI:45924, CHEBI:119573, CHEBI:63613).

Selection: All 11 records in Stage 5 resolved finding groups (Issues #1253, #1254, #1255).
Coverage: full; 11 reviewed / 11 in the declared population.
Source: working_tree at Git base 4e3cb51384be1b7fed69a980eb4f73de417d1a62.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:28077 | data/antibiotics/antimycobacterial/rifampicin.yaml | maintained | rifampicin |
| CHEBI:3732 | data/antibiotics/antibacterial/clarithromycin.yaml | maintained | clarithromycin |
| CHEBI:100147 | data/antibiotics/antibacterial/nalidixic-acid.yaml | maintained | nalidixic acid |
| CHEBI:100246 | data/antibiotics/antibacterial/norfloxacin.yaml | maintained | norfloxacin |
| CHEBI:50199 | data/antibiotics/antibacterial/pefloxacin.yaml | maintained | pefloxacin |
| CHEBI:100241 | data/antibiotics/antibacterial/ciprofloxacin.yaml | maintained | ciprofloxacin |
| CHEBI:600103 | data/antibiotics/antibacterial/daptomycin.yaml | maintained | daptomycin |
| CHEBI:63598 | data/antibiotics/antibacterial/levofloxacin.yaml | maintained | levofloxacin |
| CHEBI:45924 | data/antibiotics/antibacterial/trimethoprim.yaml | maintained | trimethoprim |
| CHEBI:119573 | data/antibiotics/antiviral/delavirdine.yaml | maintained | delavirdine |
| CHEBI:63613 | data/antibiotics/antiviral/nevirapine.yaml | maintained | nevirapine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and OAK ontology-label validation | passed | True | CHEBI:28077, CHEBI:3732, CHEBI:100147, CHEBI:100246, CHEBI:50199, CHEBI:100241, CHEBI:600103, CHEBI:63598, CHEBI:45924, CHEBI:119573, CHEBI:63613 | All 2,969 corpus records, including the 11 remediated records, pass closed LinkML schema validation and OAK label correspondence with 0 errors. |
| Full corpus seed reproduction check | passed | True | CHEBI:28077, CHEBI:3732, CHEBI:100147, CHEBI:100246, CHEBI:50199, CHEBI:100241, CHEBI:600103, CHEBI:63598, CHEBI:45924, CHEBI:119573, CHEBI:63613 | All 2,969 records reproduce byte-for-byte from data/raw/ plus curator inputs with 0 missing, 0 unexpected, and 0 drifted fields. |
| Causal-graph and UniProt protein-example curation test suite | passed | True | CHEBI:28077, CHEBI:3732, CHEBI:100147, CHEBI:100246, CHEBI:50199, CHEBI:100241, CHEBI:600103, CHEBI:63598, CHEBI:45924, CHEBI:119573, CHEBI:63613 | All 91 tests in test_causal_graphs_curation.py and test_uniprot_protein_examples.py pass. |

## Scientific And Domain Assessments

### Rifampicin mode_of_action_target_scope alignment with bacterial RNAP target

scope: supported. Targets: CHEBI:28077.

CHEBI:28077 (rifampicin) now carries mode_of_action_target_scope: MICROBIAL_TARGET with a CURATED_MODE_OF_ACTION curation_history event citing PMID:11290327, clearing the moa-settled-scope-review queue.

### Primary-literature molecular_targets and REVIEWED promotion on clarithromycin, nalidixic acid, norfloxacin, and pefloxacin

completeness: supported. Targets: CHEBI:3732, CHEBI:100147, CHEBI:100246, CHEBI:50199.

All 4 records in Group 2 (CHEBI:3732, CHEBI:100147, CHEBI:100246, CHEBI:50199) now carry source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets aligned with their causal_graphs (including UniProtKB:P0AES4 E. coli K-12 GyrA on the 3 quinolones) and are promoted to curation_status: REVIEWED.

### Curator-settled mode_of_action, PRIMARY_LITERATURE molecular_targets, and REVIEWED promotion on ciprofloxacin, daptomycin, levofloxacin, trimethoprim, delavirdine, and nevirapine

completeness: supported. Targets: CHEBI:100241, CHEBI:600103, CHEBI:63598, CHEBI:45924, CHEBI:119573, CHEBI:63613.

All 6 records in Group 3 (CHEBI:100241, CHEBI:600103, CHEBI:63598, CHEBI:45924, CHEBI:119573, CHEBI:63613) now carry curator-settled mode_of_action with CURATOR mode_of_action_notes, source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (with reviewed UniProtKB protein_examples on all 5 protein-target records), and curation_status: REVIEWED.

## Findings

### rifampicin-moa-scope-leftover: Rifampicin mode_of_action_target_scope updated from HOST_SHARED_TARGET to MICROBIAL_TARGET

major / resolved / confirmed; issue key: rifampicin-moa-target-scope-host-shared-leftover.

Updated mode_of_action_target_scope on CHEBI:28077 (data/antibiotics/antimycobacterial/rifampicin.yaml) from seeder leftover HOST_SHARED_TARGET to MICROBIAL_TARGET via record_curation_event (CURATED_MODE_OF_ACTION) and write_validated_antibiotic, matching bacterial core RNA polymerase beta-subunit channel occlusion (PMID:11290327).

Disposition: Resolved in Stage 5 (Issue #1253): mode_of_action_target_scope updated to MICROBIAL_TARGET and verified against validate_strict.py and verify_corpus.py.

### seeded-causal-graphs-missing-primary-targets: Added PRIMARY_LITERATURE molecular_targets and promoted 4 causal-graph records with settled MoA to REVIEWED

major / resolved / confirmed; issue key: seeded-causal-graphs-missing-primary-literature-targets.

Added source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets entries to clarithromycin (CHEBI:3732, PMID:9425251), nalidixic acid (CHEBI:100147, PMID:200930), norfloxacin (CHEBI:100246, PMID:2982149), and pefloxacin (CHEBI:50199, PMID:3010848), including reviewed UniProtKB:P0AES4 (E. coli K-12 GyrA) protein_examples on the three quinolones, and promoted all 4 records from SEEDED to REVIEWED.

Disposition: Resolved in Stage 5 (Issue #1254): added PRIMARY_LITERATURE molecular_targets and promoted CHEBI:3732, CHEBI:100147, CHEBI:100246, and CHEBI:50199 to REVIEWED.

### seeded-causal-graphs-unsettled-moa-and-targets: Settled mode_of_action, added PRIMARY_LITERATURE molecular_targets, and promoted 6 causal-graph records to REVIEWED

major / resolved / confirmed; issue key: seeded-causal-graphs-unsettled-moa-and-primary-targets.

Curated mode_of_action, mode_of_action_target_scope, CURATOR mode_of_action_notes, and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets (with reviewed UniProtKB protein_examples on all 5 protein-target records) across ciprofloxacin (CHEBI:100241, PMID:2836339), daptomycin (CHEBI:600103, PMID:14506031), levofloxacin (CHEBI:63598, PMID:1966187), trimethoprim (CHEBI:45924, PMID:351100), delavirdine (CHEBI:119573, PMID:9048503), and nevirapine (CHEBI:63613, PMID:1703307), and promoted all 6 records from SEEDED to REVIEWED.

Disposition: Resolved in Stage 5 (Issue #1255): curated mode_of_action and PRIMARY_LITERATURE molecular_targets and promoted CHEBI:100241, CHEBI:600103, CHEBI:63598, CHEBI:45924, CHEBI:119573, and CHEBI:63613 to REVIEWED.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| remediated-records-content | curation/stage5_review_remediation_transition.json; records[0..10] and SHA-256 digests of the 11 updated YAML records | supports | All 11 records were updated through record_curation_event and write_validated_antibiotic: CHEBI:28077 mode_of_action_target_scope set to MICROBIAL_TARGET; 10 records (CHEBI:3732, CHEBI:100147, CHEBI:100246, CHEBI:50199, CHEBI:100241, CHEBI:600103, CHEBI:63598, CHEBI:45924, CHEBI:119573, CHEBI:63613) promoted to REVIEWED with curator-settled mode_of_action and PRIMARY_LITERATURE molecular_targets. |
| validate-strict-pass | scripts/validate_strict.py; 2969 files scanned, 0 files with ERROR, 0 total ERROR rows | supports | Closed-mode LinkML validation and OAK ontology label verification pass across all 2,969 records. |
| verify-corpus-pass | scripts/verify_corpus.py; records expected: 2969, on disk: 2969, missing: 0, unexpected: 0, drifted fields: 0 | supports | Every curator-owned edit on the 11 remediated records survives seed_from_sources.py reproduction without drift. |
| primary-literature-targets | PMID:11290327, PMID:9425251, PMID:200930, PMID:2982149, PMID:3010848, PMID:2836339, PMID:14506031, PMID:1966187, PMID:351100, PMID:9048503, PMID:1703307; Primary experimental mechanism studies cited across the 11 remediated records | supports | Primary experimental studies ground bacterial RNAP beta-subunit occlusion for rifampicin (PMID:11290327), 23S rRNA peptidyl-transferase binding for clarithromycin (PMID:9425251), DNA gyrase subunit A / cleavage-complex stabilization for nalidixic acid (PMID:200930), norfloxacin (PMID:2982149), pefloxacin (PMID:3010848), ciprofloxacin (PMID:2836339), and levofloxacin (PMID:1966187), Ca2+-dependent cytoplasmic-membrane depolarization for daptomycin (PMID:14506031), bacterial dihydrofolate reductase inhibition for trimethoprim (PMID:351100), and HIV-1 reverse transcriptase non-nucleoside pocket inhibition for delavirdine (PMID:9048503) and nevirapine (PMID:1703307). |

## Limits And Additional Notes

- Finding unreviewed-seeded-pdb-structural-observations (Issue #1256, CHEBI:138488, CHEBI:28971, CHEBI:44499) is outside this 11-record remediated batch because scripts/seed_from_sources.py overwrites structural_observations on SEEDED records; it is tracked as infrastructure task antibioticmech-infra-0001 for Stage 6.
- Original Stage 4 review bundles (20261023T160013Z-rifampicin-record-review and 20261023T160534Z-frozen-inventory-cohort-review) are preserved byte-for-byte.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261023T184800Z-stage5-remediated-records-review
kind: batch
repository: culturebotai/AntibioticMech
title: 'Stage 5 post-remediation review of 11 remediated AntibioticRecord files (Issues
  #1253, #1254, #1255)'
started_at: '2026-10-23T18:35:00Z'
finished_at: '2026-10-23T18:48:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Stage 5 post-remediation verification review of the 11 remediated
    records prior to independent adversarial PR review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass
native_verdict: PASS
scientific_review: true
summary: 'Post-remediation batch review of the 11 AntibioticRecord YAML files updated
  in Stage 5 to resolve Stage 4 findings rifampicin-moa-scope-leftover (Issue #1253),
  seeded-causal-graphs-missing-primary-targets (Issue #1254), and seeded-causal-graphs-unsettled-moa-and-targets
  (Issue #1255). Verified that CHEBI:28077 (rifampicin) now carries mode_of_action_target_scope:
  MICROBIAL_TARGET; that all 10 formerly SEEDED records with primary-literature causal_graphs
  (clarithromycin, nalidixic acid, norfloxacin, pefloxacin, ciprofloxacin, daptomycin,
  levofloxacin, trimethoprim, delavirdine, nevirapine) now carry curator-settled mode_of_action,
  source: PRIMARY_LITERATURE molecular_targets (with reviewed UniProtKB protein_examples
  on all 8 protein-target records), and curation_status: REVIEWED; and that validate_strict.py,
  verify_corpus.py, and all 91 causal-graph/UniProt curation tests pass with 0 errors.'
source:
  git_revision: 4e3cb51384be1b7fed69a980eb4f73de417d1a62
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
    sha256: fc2d9fa01c59f42dcae48c90b5d9769be616e718e9a998d091c0e4154d508133
  - path: curation/stage5_review_remediation_transition.json
    role: context
    sha256: fbc1a55b4b433a27af8b266359aa2b5a52bdb234de0eab35f59b1a3840f1c9e5
  - path: curation/uniprot_protein_examples.yaml
    role: context
    sha256: a018458adf57dab1892dc57e04aa264d57a2e3057d7ee5e4919020796c1bfff1
  - path: data/antibiotics/antibacterial/ciprofloxacin.yaml
    role: target
    sha256: 726fe2ad31b2f95eb261d7b407ff2e98e436e64f704d5627adce99055b68710a
  - path: data/antibiotics/antibacterial/clarithromycin.yaml
    role: target
    sha256: 8bd29592ae34d48593a1dd425a12f70971f35d059af8d01a840d83f4624f6444
  - path: data/antibiotics/antibacterial/daptomycin.yaml
    role: target
    sha256: e0299a5cf5e137a456820fa5283c096ae049d55ae0d26345ceb0a3bebe47bae0
  - path: data/antibiotics/antibacterial/levofloxacin.yaml
    role: target
    sha256: 43f17250c4bdacc58b2fbed43c952d71cad27f6932441f7f80a31a8de074f051
  - path: data/antibiotics/antibacterial/nalidixic-acid.yaml
    role: target
    sha256: 0444959ad42e1b0cd5a784dc4fdd57b3db80d221bcd28907b07e1ac90874921f
  - path: data/antibiotics/antibacterial/norfloxacin.yaml
    role: target
    sha256: 2b9b08b0bab766b8ce63260a42286cafbb13ed0f73c02f9beb9766b90f656fbc
  - path: data/antibiotics/antibacterial/pefloxacin.yaml
    role: target
    sha256: 64ea0c9f2de08e1132646d55bce6a60f422694f233fb5490a4b6ee644c5ea37e
  - path: data/antibiotics/antibacterial/trimethoprim.yaml
    role: target
    sha256: 84d8b852fd2df1864ebdb3d36377a84c87883500797200fa94475f4620cb4338
  - path: data/antibiotics/antimycobacterial/rifampicin.yaml
    role: target
    sha256: 791ba4d40a12ecc7bb6238349c5ba793f5bc64a7aac043c77307e8c6ba574ae4
  - path: data/antibiotics/antiviral/delavirdine.yaml
    role: target
    sha256: 8d64f667cfdf2fbdf4867cf9190ef9062d6d247fd30d1fc08419febd39b433e6
  - path: data/antibiotics/antiviral/nevirapine.yaml
    role: target
    sha256: d5aab42aff5f78698e3a2813ce6bd21398f5cafb4145867e9188bf81b8b3a75c
  - path: scripts/curation_worklist.py
    role: context
    sha256: 692fdcc39a0c8135c89b483a19ab0a428bfac3d851ff67a6a1ceac80225a2430
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
  description: 'Complete post-remediation review of the 11 AntibioticRecord YAML files
    modified in Stage 5 (Groups 1-3: CHEBI:28077, CHEBI:3732, CHEBI:100147, CHEBI:100246,
    CHEBI:50199, CHEBI:100241, CHEBI:600103, CHEBI:63598, CHEBI:45924, CHEBI:119573,
    CHEBI:63613).'
  selection: 'All 11 records in Stage 5 resolved finding groups (Issues #1253, #1254,
    #1255).'
  coverage: full
  population_size: 11
  reviewed_target_ids:
  - CHEBI:28077
  - CHEBI:3732
  - CHEBI:100147
  - CHEBI:100246
  - CHEBI:50199
  - CHEBI:100241
  - CHEBI:600103
  - CHEBI:63598
  - CHEBI:45924
  - CHEBI:119573
  - CHEBI:63613
targets:
- target_id: CHEBI:28077
  path: data/antibiotics/antimycobacterial/rifampicin.yaml
  label: rifampicin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antimycobacterial/rifampicin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, mode_of_action,
      mode_of_action_target_scope, molecular_targets, causal_graphs)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:3732
  path: data/antibiotics/antibacterial/clarithromycin.yaml
  label: clarithromycin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/clarithromycin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, mode_of_action,
      mode_of_action_target_scope, molecular_targets, causal_graphs)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:100147
  path: data/antibiotics/antibacterial/nalidixic-acid.yaml
  label: nalidixic acid
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/nalidixic-acid.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, mode_of_action,
      mode_of_action_target_scope, molecular_targets, causal_graphs)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:100246
  path: data/antibiotics/antibacterial/norfloxacin.yaml
  label: norfloxacin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/norfloxacin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, mode_of_action,
      mode_of_action_target_scope, molecular_targets, causal_graphs)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:50199
  path: data/antibiotics/antibacterial/pefloxacin.yaml
  label: pefloxacin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/pefloxacin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, mode_of_action,
      mode_of_action_target_scope, molecular_targets, causal_graphs)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:100241
  path: data/antibiotics/antibacterial/ciprofloxacin.yaml
  label: ciprofloxacin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/ciprofloxacin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, mode_of_action,
      mode_of_action_target_scope, molecular_targets, causal_graphs)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:600103
  path: data/antibiotics/antibacterial/daptomycin.yaml
  label: daptomycin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/daptomycin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, mode_of_action,
      mode_of_action_target_scope, molecular_targets, causal_graphs)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:63598
  path: data/antibiotics/antibacterial/levofloxacin.yaml
  label: levofloxacin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/levofloxacin.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, mode_of_action,
      mode_of_action_target_scope, molecular_targets, causal_graphs)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:45924
  path: data/antibiotics/antibacterial/trimethoprim.yaml
  label: trimethoprim
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/trimethoprim.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, mode_of_action,
      mode_of_action_target_scope, molecular_targets, causal_graphs)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:119573
  path: data/antibiotics/antiviral/delavirdine.yaml
  label: delavirdine
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antiviral/delavirdine.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, mode_of_action,
      mode_of_action_target_scope, molecular_targets, causal_graphs)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
- target_id: CHEBI:63613
  path: data/antibiotics/antiviral/nevirapine.yaml
  label: nevirapine
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antiviral/nevirapine.yaml
    role: Curator-maintained REVIEWED record slots (curation_status, mode_of_action,
      mode_of_action_target_scope, molecular_targets, causal_graphs)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection and curator-owned slot preservation on re-seed
checks:
- check_id: strict-schema-remediated-records
  name: Closed-schema and OAK ontology-label validation
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py --quiet --workers 2
  exit_code: 0
  summary: All 2,969 corpus records, including the 11 remediated records, pass closed
    LinkML schema validation and OAK label correspondence with 0 errors.
  target_ids:
  - CHEBI:28077
  - CHEBI:3732
  - CHEBI:100147
  - CHEBI:100246
  - CHEBI:50199
  - CHEBI:100241
  - CHEBI:600103
  - CHEBI:63598
  - CHEBI:45924
  - CHEBI:119573
  - CHEBI:63613
  evidence_ids:
  - validate-strict-pass
  - remediated-records-content
- check_id: corpus-reproduction-remediated-records
  name: Full corpus seed reproduction check
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py
  exit_code: 0
  summary: All 2,969 records reproduce byte-for-byte from data/raw/ plus curator inputs
    with 0 missing, 0 unexpected, and 0 drifted fields.
  target_ids:
  - CHEBI:28077
  - CHEBI:3732
  - CHEBI:100147
  - CHEBI:100246
  - CHEBI:50199
  - CHEBI:100241
  - CHEBI:600103
  - CHEBI:63598
  - CHEBI:45924
  - CHEBI:119573
  - CHEBI:63613
  evidence_ids:
  - verify-corpus-pass
  - remediated-records-content
- check_id: curation-pytest-suite
  name: Causal-graph and UniProt protein-example curation test suite
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_causal_graphs_curation.py tests/test_uniprot_protein_examples.py
    -q
  exit_code: 0
  summary: All 91 tests in test_causal_graphs_curation.py and test_uniprot_protein_examples.py
    pass.
  target_ids:
  - CHEBI:28077
  - CHEBI:3732
  - CHEBI:100147
  - CHEBI:100246
  - CHEBI:50199
  - CHEBI:100241
  - CHEBI:600103
  - CHEBI:63598
  - CHEBI:45924
  - CHEBI:119573
  - CHEBI:63613
  evidence_ids:
  - remediated-records-content
evidence:
- evidence_id: remediated-records-content
  kind: record_content
  reference: curation/stage5_review_remediation_transition.json
  locator: records[0..10] and SHA-256 digests of the 11 updated YAML records
  accessed_at: '2026-10-23T18:45:00Z'
  support: supports
  snapshot_sha256: fbc1a55b4b433a27af8b266359aa2b5a52bdb234de0eab35f59b1a3840f1c9e5
  summary: 'All 11 records were updated through record_curation_event and write_validated_antibiotic:
    CHEBI:28077 mode_of_action_target_scope set to MICROBIAL_TARGET; 10 records (CHEBI:3732,
    CHEBI:100147, CHEBI:100246, CHEBI:50199, CHEBI:100241, CHEBI:600103, CHEBI:63598,
    CHEBI:45924, CHEBI:119573, CHEBI:63613) promoted to REVIEWED with curator-settled
    mode_of_action and PRIMARY_LITERATURE molecular_targets.'
- evidence_id: validate-strict-pass
  kind: validation
  reference: scripts/validate_strict.py
  locator: 2969 files scanned, 0 files with ERROR, 0 total ERROR rows
  accessed_at: '2026-10-23T18:41:22Z'
  support: supports
  snapshot_sha256: d70e6739c881260927dfc99abea16e56be0f34f353f9f95353a43da76e8e7217
  summary: Closed-mode LinkML validation and OAK ontology label verification pass
    across all 2,969 records.
- evidence_id: verify-corpus-pass
  kind: validation
  reference: scripts/verify_corpus.py
  locator: 'records expected: 2969, on disk: 2969, missing: 0, unexpected: 0, drifted
    fields: 0'
  accessed_at: '2026-10-23T18:41:22Z'
  support: supports
  snapshot_sha256: 7d881f9b4e17b02d7f3ec3eb48404ad0a41a0cefa915edc9a442f755b834df78
  summary: Every curator-owned edit on the 11 remediated records survives seed_from_sources.py
    reproduction without drift.
- evidence_id: primary-literature-targets
  kind: primary_source
  reference: PMID:11290327, PMID:9425251, PMID:200930, PMID:2982149, PMID:3010848,
    PMID:2836339, PMID:14506031, PMID:1966187, PMID:351100, PMID:9048503, PMID:1703307
  locator: Primary experimental mechanism studies cited across the 11 remediated records
  accessed_at: '2026-10-23T18:45:00Z'
  support: supports
  summary: Primary experimental studies ground bacterial RNAP beta-subunit occlusion
    for rifampicin (PMID:11290327), 23S rRNA peptidyl-transferase binding for clarithromycin
    (PMID:9425251), DNA gyrase subunit A / cleavage-complex stabilization for nalidixic
    acid (PMID:200930), norfloxacin (PMID:2982149), pefloxacin (PMID:3010848), ciprofloxacin
    (PMID:2836339), and levofloxacin (PMID:1966187), Ca2+-dependent cytoplasmic-membrane
    depolarization for daptomycin (PMID:14506031), bacterial dihydrofolate reductase
    inhibition for trimethoprim (PMID:351100), and HIV-1 reverse transcriptase non-nucleoside
    pocket inhibition for delavirdine (PMID:9048503) and nevirapine (PMID:1703307).
assessments:
- assessment_id: group1-rifampicin-moa-scope-resolved
  area: scope
  topic: Rifampicin mode_of_action_target_scope alignment with bacterial RNAP target
  outcome: supported
  summary: 'CHEBI:28077 (rifampicin) now carries mode_of_action_target_scope: MICROBIAL_TARGET
    with a CURATED_MODE_OF_ACTION curation_history event citing PMID:11290327, clearing
    the moa-settled-scope-review queue.'
  target_ids:
  - CHEBI:28077
  evidence_ids:
  - remediated-records-content
  - primary-literature-targets
  - validate-strict-pass
  - verify-corpus-pass
- assessment_id: group2-primary-targets-and-reviewed-promotion
  area: completeness
  topic: Primary-literature molecular_targets and REVIEWED promotion on clarithromycin,
    nalidixic acid, norfloxacin, and pefloxacin
  outcome: supported
  summary: 'All 4 records in Group 2 (CHEBI:3732, CHEBI:100147, CHEBI:100246, CHEBI:50199)
    now carry source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets
    aligned with their causal_graphs (including UniProtKB:P0AES4 E. coli K-12 GyrA
    on the 3 quinolones) and are promoted to curation_status: REVIEWED.'
  target_ids:
  - CHEBI:3732
  - CHEBI:100147
  - CHEBI:100246
  - CHEBI:50199
  evidence_ids:
  - remediated-records-content
  - primary-literature-targets
  - validate-strict-pass
  - verify-corpus-pass
- assessment_id: group3-settled-moa-primary-targets-and-reviewed-promotion
  area: completeness
  topic: Curator-settled mode_of_action, PRIMARY_LITERATURE molecular_targets, and
    REVIEWED promotion on ciprofloxacin, daptomycin, levofloxacin, trimethoprim, delavirdine,
    and nevirapine
  outcome: supported
  summary: 'All 6 records in Group 3 (CHEBI:100241, CHEBI:600103, CHEBI:63598, CHEBI:45924,
    CHEBI:119573, CHEBI:63613) now carry curator-settled mode_of_action with CURATOR
    mode_of_action_notes, source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE)
    molecular_targets (with reviewed UniProtKB protein_examples on all 5 protein-target
    records), and curation_status: REVIEWED.'
  target_ids:
  - CHEBI:100241
  - CHEBI:600103
  - CHEBI:63598
  - CHEBI:45924
  - CHEBI:119573
  - CHEBI:63613
  evidence_ids:
  - remediated-records-content
  - primary-literature-targets
  - validate-strict-pass
  - verify-corpus-pass
findings:
- finding_id: rifampicin-moa-scope-leftover
  issue_key: rifampicin-moa-target-scope-host-shared-leftover
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Rifampicin mode_of_action_target_scope updated from HOST_SHARED_TARGET to
    MICROBIAL_TARGET
  description: Updated mode_of_action_target_scope on CHEBI:28077 (data/antibiotics/antimycobacterial/rifampicin.yaml)
    from seeder leftover HOST_SHARED_TARGET to MICROBIAL_TARGET via record_curation_event
    (CURATED_MODE_OF_ACTION) and write_validated_antibiotic, matching bacterial core
    RNA polymerase beta-subunit channel occlusion (PMID:11290327).
  target_ids:
  - CHEBI:28077
  field_paths:
  - mode_of_action_target_scope
  - curation_history
  evidence_ids:
  - remediated-records-content
  - primary-literature-targets
  - validate-strict-pass
  - verify-corpus-pass
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antimycobacterial/rifampicin.yaml
    role: Curator-owned mode_of_action_target_scope slot on REVIEWED record
  disposition_reason: 'Resolved in Stage 5 (Issue #1253): mode_of_action_target_scope
    updated to MICROBIAL_TARGET and verified against validate_strict.py and verify_corpus.py.'
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261023T160013Z-rifampicin-record-review
    finding_id: rifampicin-moa-scope-leftover
  - repository: culturebotai/AntibioticMech
    review_id: 20261023T160534Z-frozen-inventory-cohort-review
    finding_id: rifampicin-moa-scope-leftover
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1253
- finding_id: seeded-causal-graphs-missing-primary-targets
  issue_key: seeded-causal-graphs-missing-primary-literature-targets
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Added PRIMARY_LITERATURE molecular_targets and promoted 4 causal-graph records
    with settled MoA to REVIEWED
  description: 'Added source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE)
    molecular_targets entries to clarithromycin (CHEBI:3732, PMID:9425251), nalidixic
    acid (CHEBI:100147, PMID:200930), norfloxacin (CHEBI:100246, PMID:2982149), and
    pefloxacin (CHEBI:50199, PMID:3010848), including reviewed UniProtKB:P0AES4 (E.
    coli K-12 GyrA) protein_examples on the three quinolones, and promoted all 4 records
    from SEEDED to REVIEWED.'
  target_ids:
  - CHEBI:3732
  - CHEBI:100147
  - CHEBI:100246
  - CHEBI:50199
  field_paths:
  - curation_status
  - molecular_targets
  - curation_history
  evidence_ids:
  - remediated-records-content
  - primary-literature-targets
  - validate-strict-pass
  - verify-corpus-pass
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/clarithromycin.yaml
    role: Curator-owned molecular_targets and curation_status
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/nalidixic-acid.yaml
    role: Curator-owned molecular_targets and curation_status
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/norfloxacin.yaml
    role: Curator-owned molecular_targets and curation_status
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/pefloxacin.yaml
    role: Curator-owned molecular_targets and curation_status
  disposition_reason: 'Resolved in Stage 5 (Issue #1254): added PRIMARY_LITERATURE
    molecular_targets and promoted CHEBI:3732, CHEBI:100147, CHEBI:100246, and CHEBI:50199
    to REVIEWED.'
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261023T160534Z-frozen-inventory-cohort-review
    finding_id: seeded-causal-graphs-missing-primary-targets
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1254
- finding_id: seeded-causal-graphs-unsettled-moa-and-targets
  issue_key: seeded-causal-graphs-unsettled-moa-and-primary-targets
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Settled mode_of_action, added PRIMARY_LITERATURE molecular_targets, and promoted
    6 causal-graph records to REVIEWED
  description: 'Curated mode_of_action, mode_of_action_target_scope, CURATOR mode_of_action_notes,
    and source: PRIMARY_LITERATURE (evidence_status: PRIMARY_EVIDENCE) molecular_targets
    (with reviewed UniProtKB protein_examples on all 5 protein-target records) across
    ciprofloxacin (CHEBI:100241, PMID:2836339), daptomycin (CHEBI:600103, PMID:14506031),
    levofloxacin (CHEBI:63598, PMID:1966187), trimethoprim (CHEBI:45924, PMID:351100),
    delavirdine (CHEBI:119573, PMID:9048503), and nevirapine (CHEBI:63613, PMID:1703307),
    and promoted all 6 records from SEEDED to REVIEWED.'
  target_ids:
  - CHEBI:100241
  - CHEBI:600103
  - CHEBI:63598
  - CHEBI:45924
  - CHEBI:119573
  - CHEBI:63613
  field_paths:
  - curation_status
  - mode_of_action
  - mode_of_action_target_scope
  - mode_of_action_notes
  - molecular_targets
  - curation_history
  evidence_ids:
  - remediated-records-content
  - primary-literature-targets
  - validate-strict-pass
  - verify-corpus-pass
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/ciprofloxacin.yaml
    role: Curator-owned mode_of_action, molecular_targets, and curation_status
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/daptomycin.yaml
    role: Curator-owned mode_of_action, molecular_targets, and curation_status
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/levofloxacin.yaml
    role: Curator-owned mode_of_action, molecular_targets, and curation_status
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antibacterial/trimethoprim.yaml
    role: Curator-owned mode_of_action, molecular_targets, and curation_status
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antiviral/delavirdine.yaml
    role: Curator-owned mode_of_action, molecular_targets, and curation_status
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antiviral/nevirapine.yaml
    role: Curator-owned mode_of_action, molecular_targets, and curation_status
  disposition_reason: 'Resolved in Stage 5 (Issue #1255): curated mode_of_action and
    PRIMARY_LITERATURE molecular_targets and promoted CHEBI:100241, CHEBI:600103,
    CHEBI:63598, CHEBI:45924, CHEBI:119573, and CHEBI:63613 to REVIEWED.'
  previous_occurrences:
  - repository: culturebotai/AntibioticMech
    review_id: 20261023T160534Z-frozen-inventory-cohort-review
    finding_id: seeded-causal-graphs-unsettled-moa-and-targets
  external_issues:
  - https://github.com/CultureBotAI/AntibioticMech/issues/1255
actions: []
limitations:
- 'Finding unreviewed-seeded-pdb-structural-observations (Issue #1256, CHEBI:138488,
  CHEBI:28971, CHEBI:44499) is outside this 11-record remediated batch because scripts/seed_from_sources.py
  overwrites structural_observations on SEEDED records; it is tracked as infrastructure
  task antibioticmech-infra-0001 for Stage 6.'
notes:
- Original Stage 4 review bundles (20261023T160013Z-rifampicin-record-review and 20261023T160534Z-frozen-inventory-cohort-review)
  are preserved byte-for-byte.
related_reviews:
- repository: culturebotai/AntibioticMech
  review_id: 20261023T160013Z-rifampicin-record-review
  relationship: Predecessor Stage 4 single-record review of CHEBI:28077 (rifampicin)
- repository: culturebotai/AntibioticMech
  review_id: 20261023T160534Z-frozen-inventory-cohort-review
  relationship: Predecessor Stage 4 full-inventory cohort review identifying the 3
    resolved finding groups
tags:
- batch-review
- stage-05
- remediation-verification
```
