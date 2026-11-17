# Single-record review of rifampicin (CHEBI:28077)

- Review: 20261023T160013Z-rifampicin-record-review
- Repository: culturebotai/AntibioticMech
- Started UTC: 2026-10-23T15:48:43Z
- Finished UTC: 2026-10-23T16:00:13Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review of REVIEWED record CHEBI:28077 (rifampicin) verified exact single-molecule ChEBI/CARD identity, structure, antimycobacterial filing, FDA GSRS clinical approvals, CRyPTIC 3.4.0 and CDC/FDA AR Bank activity observations, primary-literature bacterial RNAP beta-subunit target (PMID:11290327) with Thermus aquaticus (UniProtKB:Q9KWU6) and M. tuberculosis H37Rv (UniProtKB:P9WGY9) protein_examples, and the 4-node/3-edge causal graph rifampicin_rnap_beta_channel_transcription_occlusion. One open finding requires Stage 5 remediation: mode_of_action_target_scope retains seeder leftover HOST_SHARED_TARGET from the replaced MULTIPLE bucket instead of MICROBIAL_TARGET.

## Scope And Provenance

Complete single-record review of data/antibiotics/antimycobacterial/rifampicin.yaml (CHEBI:28077) across identity, filing, mode_of_action, molecular_targets, causal_graphs, resistance_mechanisms, activity_spectrum, and clinical_status_assertions.

Selection: Selected CHEBI:28077 (rifampicin) as the single REVIEWED record flagged by the curation_worklist.py moa-settled-scope-review queue during the Stage 4 full-inventory audit.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 38cee22ec3e9a6c8ce2a3159c039dcfbb2a282bc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:28077 | data/antibiotics/antimycobacterial/rifampicin.yaml | maintained | rifampicin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and ontology-grounding validation | passed | True | CHEBI:28077 | CHEBI:28077 passes closed LinkML schema validation and OAK label correspondence with 0 errors. |
| Curation worklist moa-settled-scope-review diagnostic | passed | True | CHEBI:28077 | Diagnostic identifies CHEBI:28077 as the sole record where curator-settled mode_of_action (NUCLEIC_ACID_SYNTHESIS_INHIBITION) still carries HOST_SHARED_TARGET. |

## Scientific And Domain Assessments

### Exact chemical identity, primary target, and causal mechanism graph

evidence: supported. Targets: CHEBI:28077.

Exact single-molecule ChEBI:28077 and CARD ARO:3000169 identity, antimycobacterial filing, PRIMARY_LITERATURE bacterial RNAP beta-subunit target, UniProtKB protein_examples (Q9KWU6, P9WGY9), and 4-node/3-edge causal graph are accurately grounded in PMID:11290327.

### Mode-of-action target scope alignment with settled bacterial RNAP mechanism

scope: concern. Targets: CHEBI:28077.

mode_of_action_target_scope is still HOST_SHARED_TARGET (a leftover from ChEBI role CHEBI:35816 under seeded mode_of_action: MULTIPLE) despite curator-settled bacterial RNA polymerase transcription inhibition (MICROBIAL_TARGET).

## Findings

### rifampicin-moa-scope-leftover: Rifampicin retains seeder leftover mode_of_action_target_scope: HOST_SHARED_TARGET

major / open / confirmed; issue key: rifampicin-moa-target-scope-host-shared-leftover.

In data/antibiotics/antimycobacterial/rifampicin.yaml (CHEBI:28077), mode_of_action was curated from MULTIPLE to NUCLEIC_ACID_SYNTHESIS_INHIBITION with CURATOR mode_of_action_notes citing PMID:11290327 for bacterial core RNA polymerase beta-subunit channel occlusion, but mode_of_action_target_scope at line 6179 was left as HOST_SHARED_TARGET from the ChEBI CHEBI:35816 role projection instead of MICROBIAL_TARGET.

## Recommended Actions And Acceptance Checks

### remediate-rifampicin-moa-target-scope

Update mode_of_action_target_scope on data/antibiotics/antimycobacterial/rifampicin.yaml from HOST_SHARED_TARGET to MICROBIAL_TARGET via write_validated.py with a CURATED_MODE_OF_ACTION history entry during Stage 5 grouped remediation.

- mode_of_action_target_scope is MICROBIAL_TARGET on CHEBI:28077 and survives seed_from_sources.py --apply --only CHEBI:28077.
- scripts/curation_worklist.py --queue moa-settled-scope-review returns 0 records.
- scripts/validate_strict.py and scripts/verify_corpus.py pass with 0 errors.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| rifampicin-record | data/antibiotics/antimycobacterial/rifampicin.yaml; lines 1-9, 6173-6188, 6507-6558, 7081-7162 | supports | CHEBI:28077 carries exact C43H58N4O12 structure (InChIKey JQXXHWHPUNPDRT-WLSIYKJHSA-N), CURATOR mode_of_action_notes citing PMID:11290327 for bacterial RNAP beta-subunit channel occlusion, mode_of_action_target_scope: HOST_SHARED_TARGET at line 6179, PRIMARY_LITERATURE molecular_targets entry (lines 6522-6557), and causal_graphs entry rifampicin_rnap_beta_channel_transcription_occlusion (lines 7081-7162). |
| pmid-11290327 | PMID:11290327; Campbell et al. 2001 Cell 104(6):901-912; DOI:10.1016/S0092-8674(01)00286-0 (PDB 1I6V) | supports | 3.3-angstrom crystal structure of Thermus aquaticus core RNA polymerase complexed with rifampicin proves binding to a conserved bacterial RpoB pocket in the DNA/RNA exit channel that sterically blocks nascent RNA extension beyond 2-3 nt. |
| worklist-audit | scripts/curation_worklist.py; moa_settled_scope_review queue | supports | Confirms that CHEBI:35816 (DNA synthesis inhibitor) seeded MULTIPLE + HOST_SHARED_TARGET, and replacing MULTIPLE with bacterial RNAP transcription inhibition left HOST_SHARED_TARGET on CHEBI:28077. |

## Limits And Additional Notes

- Stage 4 is a read-only review stage; no scientific YAML records were modified in this commit sequence.
- CARD ARO resistance_mechanisms entries on CHEBI:28077 (including ARO:3004960 labeled for rifabutin in upstream CARD) remain source-owned database assertions with PRIMARY_EVIDENCE_NEEDED.
- Rifampicin is also included in the companion Stage 4 full-inventory cohort review (2,969 records).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261023T160013Z-rifampicin-record-review
kind: record
repository: culturebotai/AntibioticMech
title: Single-record review of rifampicin (CHEBI:28077)
started_at: '2026-10-23T15:48:43Z'
finished_at: '2026-10-23T16:00:13Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Stage 4 workflow record-review pass executed by the repository
    curation agent prior to independent adversarial PR review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION
scientific_review: true
summary: 'Whole-record review of REVIEWED record CHEBI:28077 (rifampicin) verified
  exact single-molecule ChEBI/CARD identity, structure, antimycobacterial filing,
  FDA GSRS clinical approvals, CRyPTIC 3.4.0 and CDC/FDA AR Bank activity observations,
  primary-literature bacterial RNAP beta-subunit target (PMID:11290327) with Thermus
  aquaticus (UniProtKB:Q9KWU6) and M. tuberculosis H37Rv (UniProtKB:P9WGY9) protein_examples,
  and the 4-node/3-edge causal graph rifampicin_rnap_beta_channel_transcription_occlusion.
  One open finding requires Stage 5 remediation: mode_of_action_target_scope retains
  seeder leftover HOST_SHARED_TARGET from the replaced MULTIPLE bucket instead of
  MICROBIAL_TARGET.'
source:
  git_revision: 38cee22ec3e9a6c8ce2a3159c039dcfbb2a282bc
  state: working_tree
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    role: context
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
  - path: data/antibiotics/antimycobacterial/rifampicin.yaml
    role: target
    sha256: b925cd4b323b726ef5b846418547a4ca7da97da999bd2d072cec47cb16e809b0
  - path: data/raw/aro_antibiotics.tsv
    role: context
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
  - path: data/raw/aro_resistance_edges.tsv
    role: context
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
  - path: data/raw/aro_target_edges.tsv
    role: context
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
  - path: data/raw/chebi_antimicrobials.tsv
    role: context
    sha256: 4c33e56c3c342be657309f720f5b5cb9cad1fae13bec202ef99e449503c32004
  - path: docs/CURATION.md
    role: context
    sha256: 3a060b8518ea0bdace3ca7efe6e7749c4216a7f486192994f9be82d55c301f29
  - path: docs/record-reviews.md
    role: context
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
  - path: scripts/curation_worklist.py
    role: context
    sha256: 692fdcc39a0c8135c89b483a19ab0a428bfac3d851ff67a6a1ceac80225a2430
  - path: scripts/seed_from_sources.py
    role: context
    sha256: 0cf1f4421d74516b193f8a9b95cccc9535f9aabd324b81af1bdffcb7b054811d
  - path: scripts/validate_strict.py
    role: context
    sha256: d70e6739c881260927dfc99abea16e56be0f34f353f9f95353a43da76e8e7217
  - path: src/antibioticmech/schema/antibioticmech.yaml
    role: context
    sha256: de62be2dd2dd55f141a0c14ff666eaa00efc6f3b431d651d0196ebcfddfbb301
scope:
  description: Complete single-record review of data/antibiotics/antimycobacterial/rifampicin.yaml
    (CHEBI:28077) across identity, filing, mode_of_action, molecular_targets, causal_graphs,
    resistance_mechanisms, activity_spectrum, and clinical_status_assertions.
  selection: Selected CHEBI:28077 (rifampicin) as the single REVIEWED record flagged
    by the curation_worklist.py moa-settled-scope-review queue during the Stage 4
    full-inventory audit.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:28077
targets:
- target_id: CHEBI:28077
  path: data/antibiotics/antimycobacterial/rifampicin.yaml
  label: rifampicin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antimycobacterial/rifampicin.yaml
    role: Curator-maintained REVIEWED record slots (mode_of_action, molecular_targets,
      causal_graphs)
  - repository: culturebotai/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-owned projection of ChEBI, CARD ARO, CRyPTIC, and FDA GSRS fields
checks:
- check_id: strict-schema-rifampicin
  name: Closed-schema and ontology-grounding validation
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py --quiet --workers 2
  exit_code: 0
  summary: CHEBI:28077 passes closed LinkML schema validation and OAK label correspondence
    with 0 errors.
  target_ids:
  - CHEBI:28077
  evidence_ids:
  - rifampicin-record
  - worklist-audit
- check_id: worklist-moa-scope-queue
  name: Curation worklist moa-settled-scope-review diagnostic
  status: passed
  required: true
  command: .venv/bin/python scripts/curation_worklist.py --queue moa-settled-scope-review
    --limit 20
  exit_code: 0
  summary: Diagnostic identifies CHEBI:28077 as the sole record where curator-settled
    mode_of_action (NUCLEIC_ACID_SYNTHESIS_INHIBITION) still carries HOST_SHARED_TARGET.
  target_ids:
  - CHEBI:28077
  evidence_ids:
  - worklist-audit
evidence:
- evidence_id: rifampicin-record
  kind: record_content
  reference: data/antibiotics/antimycobacterial/rifampicin.yaml
  locator: lines 1-9, 6173-6188, 6507-6558, 7081-7162
  accessed_at: '2026-10-23T16:00:13Z'
  support: supports
  snapshot_sha256: b925cd4b323b726ef5b846418547a4ca7da97da999bd2d072cec47cb16e809b0
  summary: 'CHEBI:28077 carries exact C43H58N4O12 structure (InChIKey JQXXHWHPUNPDRT-WLSIYKJHSA-N),
    CURATOR mode_of_action_notes citing PMID:11290327 for bacterial RNAP beta-subunit
    channel occlusion, mode_of_action_target_scope: HOST_SHARED_TARGET at line 6179,
    PRIMARY_LITERATURE molecular_targets entry (lines 6522-6557), and causal_graphs
    entry rifampicin_rnap_beta_channel_transcription_occlusion (lines 7081-7162).'
- evidence_id: pmid-11290327
  kind: primary_source
  reference: PMID:11290327
  locator: Campbell et al. 2001 Cell 104(6):901-912; DOI:10.1016/S0092-8674(01)00286-0
    (PDB 1I6V)
  accessed_at: '2026-10-23T16:00:13Z'
  support: supports
  summary: 3.3-angstrom crystal structure of Thermus aquaticus core RNA polymerase
    complexed with rifampicin proves binding to a conserved bacterial RpoB pocket
    in the DNA/RNA exit channel that sterically blocks nascent RNA extension beyond
    2-3 nt.
- evidence_id: worklist-audit
  kind: validation
  reference: scripts/curation_worklist.py
  locator: moa_settled_scope_review queue
  accessed_at: '2026-10-23T16:00:13Z'
  support: supports
  snapshot_sha256: 692fdcc39a0c8135c89b483a19ab0a428bfac3d851ff67a6a1ceac80225a2430
  summary: Confirms that CHEBI:35816 (DNA synthesis inhibitor) seeded MULTIPLE + HOST_SHARED_TARGET,
    and replacing MULTIPLE with bacterial RNAP transcription inhibition left HOST_SHARED_TARGET
    on CHEBI:28077.
assessments:
- assessment_id: rifampicin-identity-and-mechanism
  area: evidence
  topic: Exact chemical identity, primary target, and causal mechanism graph
  outcome: supported
  summary: Exact single-molecule ChEBI:28077 and CARD ARO:3000169 identity, antimycobacterial
    filing, PRIMARY_LITERATURE bacterial RNAP beta-subunit target, UniProtKB protein_examples
    (Q9KWU6, P9WGY9), and 4-node/3-edge causal graph are accurately grounded in PMID:11290327.
  target_ids:
  - CHEBI:28077
  evidence_ids:
  - rifampicin-record
  - pmid-11290327
- assessment_id: rifampicin-moa-target-scope
  area: scope
  topic: Mode-of-action target scope alignment with settled bacterial RNAP mechanism
  outcome: concern
  summary: 'mode_of_action_target_scope is still HOST_SHARED_TARGET (a leftover from
    ChEBI role CHEBI:35816 under seeded mode_of_action: MULTIPLE) despite curator-settled
    bacterial RNA polymerase transcription inhibition (MICROBIAL_TARGET).'
  target_ids:
  - CHEBI:28077
  evidence_ids:
  - rifampicin-record
  - pmid-11290327
  - worklist-audit
findings:
- finding_id: rifampicin-moa-scope-leftover
  issue_key: rifampicin-moa-target-scope-host-shared-leftover
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: 'Rifampicin retains seeder leftover mode_of_action_target_scope: HOST_SHARED_TARGET'
  description: In data/antibiotics/antimycobacterial/rifampicin.yaml (CHEBI:28077),
    mode_of_action was curated from MULTIPLE to NUCLEIC_ACID_SYNTHESIS_INHIBITION
    with CURATOR mode_of_action_notes citing PMID:11290327 for bacterial core RNA
    polymerase beta-subunit channel occlusion, but mode_of_action_target_scope at
    line 6179 was left as HOST_SHARED_TARGET from the ChEBI CHEBI:35816 role projection
    instead of MICROBIAL_TARGET.
  target_ids:
  - CHEBI:28077
  field_paths:
  - mode_of_action_target_scope
  evidence_ids:
  - rifampicin-record
  - pmid-11290327
  - worklist-audit
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antimycobacterial/rifampicin.yaml
    role: Curator-owned mode_of_action_target_scope slot on REVIEWED record
actions:
- action_id: remediate-rifampicin-moa-target-scope
  description: Update mode_of_action_target_scope on data/antibiotics/antimycobacterial/rifampicin.yaml
    from HOST_SHARED_TARGET to MICROBIAL_TARGET via write_validated.py with a CURATED_MODE_OF_ACTION
    history entry during Stage 5 grouped remediation.
  finding_ids:
  - rifampicin-moa-scope-leftover
  target_ids:
  - CHEBI:28077
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antimycobacterial/rifampicin.yaml
    role: Curator-owned mode_of_action_target_scope slot on REVIEWED record
  acceptance_checks:
  - mode_of_action_target_scope is MICROBIAL_TARGET on CHEBI:28077 and survives seed_from_sources.py
    --apply --only CHEBI:28077.
  - scripts/curation_worklist.py --queue moa-settled-scope-review returns 0 records.
  - scripts/validate_strict.py and scripts/verify_corpus.py pass with 0 errors.
limitations:
- Stage 4 is a read-only review stage; no scientific YAML records were modified in
  this commit sequence.
- CARD ARO resistance_mechanisms entries on CHEBI:28077 (including ARO:3004960 labeled
  for rifabutin in upstream CARD) remain source-owned database assertions with PRIMARY_EVIDENCE_NEEDED.
notes:
- Rifampicin is also included in the companion Stage 4 full-inventory cohort review
  (2,969 records).
tags:
- record-review
- rifampicin
- antimycobacterial
- stage-04
```
