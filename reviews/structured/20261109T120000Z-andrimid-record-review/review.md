# Single-record review of andrimid (CHEBI:216634)

- Review: 20261109T120000Z-andrimid-record-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-11-09T11:52:00Z
- Finished UTC: 2026-11-09T12:00:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review of PROPOSED/EXACT record CHEBI:216634 (andrimid, data/antibiotics/antibacterial/andrimid.yaml) verified exact single-molecule chemical structure (C27H33N3O5, InChIKey BDHVWPFPGIGCPA-MDKDCDSJSA-N, PubChem CID 54675763), antibacterial filing (CHEBI:33282), CURATOR discovery and mechanistic evidence (Freiberg et al. 2004 DOI:10.1074/jbc.m402989200 / PMID:15166242; Jin et al. 2006 DOI:10.1021/ja063074c / PMID:16866529), MIBiG 4.0.1 BGC0000956 producer provenance in Pantoea agglomerans (NCBITaxon:549), biosynthesis_origin (NATURAL_PRODUCT), mode_of_action (FATTY_ACID_SYNTHESIS_INHIBITION, MICROBIAL_TARGET), and the PRIMARY_LITERATURE molecular_targets entry for bacterial acetyl-CoA carboxylase carboxyltransferase (AccAD, GO:0003989, PROTEIN, DIRECT_BINDING_TARGET) carrying reviewed Swiss-Prot UniProtKB protein_examples P0ABD5 (accA) and P0A9Q5 (accD) in Escherichia coli K-12. One open coherence finding requires Cycle 8 Stage 5 grouped remediation: despite having grounding_status: EXACT, complete chemical_structure, curated mode_of_action, and PRIMARY_LITERATURE molecular_targets with reviewed UniProtKB protein_examples, curation_status remains PROPOSED.

## Scope And Provenance

Complete single-record review of data/antibiotics/antibacterial/andrimid.yaml (CHEBI:216634) across chemical identity, grounding, filing, source_concepts, producer_organisms, biosynthesis_origin, mode_of_action, molecular_targets, UniProtKB protein_examples accounting, and curation_status gate eligibility.

Selection: Selected CHEBI:216634 (andrimid) as a representative PROPOSED/EXACT record in the 3,125-record Cycle 8 Stage 4 inventory that was seeded in Cycle 8 Stage 1, enriched with mode_of_action and PRIMARY_LITERATURE molecular_targets in Cycle 8 Stage 2 and reviewed UniProtKB protein_examples (P0ABD5, P0A9Q5) in Cycle 8 Stage 3, and is immediately eligible for promotion to REVIEWED.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base defe41100737cee8dc1e4722a2930e9752e6bee8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:216634 | data/antibiotics/antibacterial/andrimid.yaml | maintained | andrimid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and ontology-grounding validation | passed | True | CHEBI:216634 | CHEBI:216634 passes closed LinkML schema validation and OAK ontology label correspondence (CHEBI:216634, CHEBI:33282, GO:0003989, NCBITaxon:549, NCBITaxon:83333, UniProtKB:P0ABD5, UniProtKB:P0A9Q5) with 0 errors. |
| Corpus integrity and CURATOR provenance verification | passed | True | CHEBI:216634 | CHEBI:216634 passes verify_corpus.py with 0 errors; seeded fields match curation/curator_antibiotics.tsv and MIBiG 4.0.1 BGC0000956. |

## Scientific And Domain Assessments

### Exact ChEBI structure, mode_of_action, AccAD target grounding, and UniProtKB protein_examples

evidence: supported. Targets: CHEBI:216634.

Exact CHEBI:216634 identity, C27H33N3O5 chemical_structure, NATURAL_PRODUCT biosynthesis_origin, FATTY_ACID_SYNTHESIS_INHIBITION mode_of_action (MICROBIAL_TARGET), and PRIMARY_LITERATURE bacterial acetyl-CoA carboxylase carboxyltransferase (GO:0003989, PROTEIN) target with reviewed Swiss-Prot UniProtKB protein_examples P0ABD5 (accA) and P0A9Q5 (accD) in Escherichia coli K-12 are accurately grounded in DOI:10.1074/jbc.m402989200 (PMID:15166242) and DOI:10.1021/ja063074c (PMID:16866529).

### Eligibility of CHEBI:216634 for promotion from PROPOSED to REVIEWED

completeness: concern. Targets: CHEBI:216634.

andrimid.yaml satisfies every REVIEWED gate requirement (grounding_status: EXACT, complete chemical_structure, curated mode_of_action, and PRIMARY_LITERATURE molecular_targets with reviewed Swiss-Prot UniProtKB protein_examples), but still carries curation_status: PROPOSED.

## Findings

### andrimid-awaiting-reviewed-promotion: Andrimid (CHEBI:216634) has complete EXACT structure and primary-literature mechanism/target curation but remains curation_status: PROPOSED

major / open / confirmed; issue key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion.

In data/antibiotics/antibacterial/andrimid.yaml (CHEBI:216634), Cycle 8 Stage 1 seeded the exact ChEBI compound, Cycle 8 Stage 2 curated biosynthesis_origin: NATURAL_PRODUCT, mode_of_action: FATTY_ACID_SYNTHESIS_INHIBITION (MICROBIAL_TARGET) with CURATOR mode_of_action_notes, and a PRIMARY_LITERATURE molecular_targets entry for bacterial acetyl-CoA carboxylase carboxyltransferase (GO:0003989, PROTEIN, DIRECT_BINDING_TARGET), and Cycle 8 Stage 3 curated reviewed Swiss-Prot UniProtKB protein_examples P0ABD5 (accA) and P0A9Q5 (accD) in Escherichia coli K-12 backed by DOI:10.1074/jbc.m402989200 (PMID:15166242) and DOI:10.1021/ja063074c (PMID:16866529), yet curation_status remains PROPOSED.

## Recommended Actions And Acceptance Checks

### promote-andrimid-to-reviewed

Promote CHEBI:216634 (andrimid) from curation_status: PROPOSED to REVIEWED via record_curation_event and write_validated_antibiotic during Cycle 8 Stage 5 grouped remediation.

- CHEBI:216634 carries curation_status: REVIEWED and survives seed_from_sources.py --apply --only CHEBI:216634.
- scripts/validate_strict.py and scripts/verify_corpus.py pass with 0 errors.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| andrimid-record | data/antibiotics/antibacterial/andrimid.yaml; lines 1-162 | supports | CHEBI:216634 carries exact C27H33N3O5 structure (InChIKey BDHVWPFPGIGCPA-MDKDCDSJSA-N, PubChem CID 54675763), biosynthesis_origin: NATURAL_PRODUCT, mode_of_action: FATTY_ACID_SYNTHESIS_INHIBITION (MICROBIAL_TARGET), and PRIMARY_LITERATURE molecular_targets[0] for bacterial acetyl-CoA carboxylase carboxyltransferase (AccAD, GO:0003989, PROTEIN, DIRECT_BINDING_TARGET) with reviewed Swiss-Prot UniProtKB protein_examples P0ABD5 and P0A9Q5, while retaining curation_status: PROPOSED. |
| freiberg-2004-jin-2006-andrimid | DOI:10.1074/jbc.m402989200; Freiberg et al. 2004 J Biol Chem 279:26066-26073 (PMID:15166242); Jin et al. 2006 J Am Chem Soc 128:10660-10661 (DOI:10.1021/ja063074c; PMID:16866529) | supports | Establishes andrimid as a hybrid polyketide-nonribosomal peptide pyrrolidinedione antibiotic from Pantoea agglomerans that directly binds and inhibits the bacterial acetyl-CoA carboxylase carboxyltransferase beta/alpha complex (AccD/AccA, Ki = 5 nM against E. coli AccAD), blocking malonyl-CoA formation and bacterial fatty acid biosynthesis. |
| strict-validation-suite | scripts/validate_strict.py; validate_strict.py and verify_corpus.py | supports | Confirms zero schema or ontology-label errors on andrimid.yaml and verifies that CHEBI:216634 meets all REVIEWED gate requirements. |

## Limits And Additional Notes

- Stage 4 is a read-only review stage; no scientific YAML records were modified in this commit sequence.
- Andrimid is also included in the companion Cycle 8 Stage 4 full-inventory cohort review (3,125 records) under the open finding proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion alongside CHEBI:81029 (alanylclavam), CHEBI:199652 (amicetin), CHEBI:202006 (bottromycin A2), CHEBI:226796 (planosporicin), and CHEBI:204968 (ajudazol A).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T120000Z-andrimid-record-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Single-record review of andrimid (CHEBI:216634)
started_at: '2026-11-09T11:52:00Z'
finished_at: '2026-11-09T12:00:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Cycle 8 Stage 4 workflow record-review pass executed by the
    repository curation agent prior to independent adversarial PR review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION
scientific_review: true
summary: 'Whole-record review of PROPOSED/EXACT record CHEBI:216634 (andrimid, data/antibiotics/antibacterial/andrimid.yaml)
  verified exact single-molecule chemical structure (C27H33N3O5, InChIKey BDHVWPFPGIGCPA-MDKDCDSJSA-N,
  PubChem CID 54675763), antibacterial filing (CHEBI:33282), CURATOR discovery and
  mechanistic evidence (Freiberg et al. 2004 DOI:10.1074/jbc.m402989200 / PMID:15166242;
  Jin et al. 2006 DOI:10.1021/ja063074c / PMID:16866529), MIBiG 4.0.1 BGC0000956 producer
  provenance in Pantoea agglomerans (NCBITaxon:549), biosynthesis_origin (NATURAL_PRODUCT),
  mode_of_action (FATTY_ACID_SYNTHESIS_INHIBITION, MICROBIAL_TARGET), and the PRIMARY_LITERATURE
  molecular_targets entry for bacterial acetyl-CoA carboxylase carboxyltransferase
  (AccAD, GO:0003989, PROTEIN, DIRECT_BINDING_TARGET) carrying reviewed Swiss-Prot
  UniProtKB protein_examples P0ABD5 (accA) and P0A9Q5 (accD) in Escherichia coli K-12.
  One open coherence finding requires Cycle 8 Stage 5 grouped remediation: despite
  having grounding_status: EXACT, complete chemical_structure, curated mode_of_action,
  and PRIMARY_LITERATURE molecular_targets with reviewed UniProtKB protein_examples,
  curation_status remains PROPOSED.'
source:
  git_revision: defe41100737cee8dc1e4722a2930e9752e6bee8
  state: working_tree
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    role: context
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
  - path: curation/curator_antibiotics.tsv
    role: context
    sha256: cae7471ab358d3d8a4529198dd8d99206176e53cd94ba05e5f458b69a634a45d
  - path: curation/uniprot_protein_examples.yaml
    role: context
    sha256: f438ab7a073bb4b07d752ad33024b79d24f8a6294cb031b22bf90460d763b837
  - path: data/antibiotics/antibacterial/andrimid.yaml
    role: target
    sha256: 277c3c8c325ec351cae780551511632ad3ce46b737818914dba7177189fa87c7
  - path: docs/CURATION.md
    role: context
    sha256: bcd2bd06e0efef13de7863fadd27609dd59d408cb44d74e99937c53d5bbbb954
  - path: docs/record-reviews.md
    role: context
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
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
  description: Complete single-record review of data/antibiotics/antibacterial/andrimid.yaml
    (CHEBI:216634) across chemical identity, grounding, filing, source_concepts, producer_organisms,
    biosynthesis_origin, mode_of_action, molecular_targets, UniProtKB protein_examples
    accounting, and curation_status gate eligibility.
  selection: Selected CHEBI:216634 (andrimid) as a representative PROPOSED/EXACT record
    in the 3,125-record Cycle 8 Stage 4 inventory that was seeded in Cycle 8 Stage
    1, enriched with mode_of_action and PRIMARY_LITERATURE molecular_targets in Cycle
    8 Stage 2 and reviewed UniProtKB protein_examples (P0ABD5, P0A9Q5) in Cycle 8
    Stage 3, and is immediately eligible for promotion to REVIEWED.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:216634
targets:
- target_id: CHEBI:216634
  path: data/antibiotics/antibacterial/andrimid.yaml
  label: andrimid
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/andrimid.yaml
    role: Curator-maintained slots (curation_status, mode_of_action, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Seeded CURATOR source_concepts, definition, and MIBiG/PubChem structure
      provenance
checks:
- check_id: strict-schema-andrimid
  name: Closed-schema and ontology-grounding validation
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py --quiet --workers 4 --out .temp/antibioticmech-record-validation.tsv
  exit_code: 0
  summary: CHEBI:216634 passes closed LinkML schema validation and OAK ontology label
    correspondence (CHEBI:216634, CHEBI:33282, GO:0003989, NCBITaxon:549, NCBITaxon:83333,
    UniProtKB:P0ABD5, UniProtKB:P0A9Q5) with 0 errors.
  target_ids:
  - CHEBI:216634
  evidence_ids:
  - andrimid-record
  - strict-validation-suite
- check_id: verify-corpus-andrimid
  name: Corpus integrity and CURATOR provenance verification
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py --summary
  exit_code: 0
  summary: CHEBI:216634 passes verify_corpus.py with 0 errors; seeded fields match
    curation/curator_antibiotics.tsv and MIBiG 4.0.1 BGC0000956.
  target_ids:
  - CHEBI:216634
  evidence_ids:
  - andrimid-record
  - strict-validation-suite
evidence:
- evidence_id: andrimid-record
  kind: record_content
  reference: data/antibiotics/antibacterial/andrimid.yaml
  locator: lines 1-162
  accessed_at: '2026-11-09T12:00:00Z'
  support: supports
  snapshot_sha256: 277c3c8c325ec351cae780551511632ad3ce46b737818914dba7177189fa87c7
  summary: 'CHEBI:216634 carries exact C27H33N3O5 structure (InChIKey BDHVWPFPGIGCPA-MDKDCDSJSA-N,
    PubChem CID 54675763), biosynthesis_origin: NATURAL_PRODUCT, mode_of_action: FATTY_ACID_SYNTHESIS_INHIBITION
    (MICROBIAL_TARGET), and PRIMARY_LITERATURE molecular_targets[0] for bacterial
    acetyl-CoA carboxylase carboxyltransferase (AccAD, GO:0003989, PROTEIN, DIRECT_BINDING_TARGET)
    with reviewed Swiss-Prot UniProtKB protein_examples P0ABD5 and P0A9Q5, while retaining
    curation_status: PROPOSED.'
- evidence_id: freiberg-2004-jin-2006-andrimid
  kind: primary_source
  reference: DOI:10.1074/jbc.m402989200
  locator: Freiberg et al. 2004 J Biol Chem 279:26066-26073 (PMID:15166242); Jin et
    al. 2006 J Am Chem Soc 128:10660-10661 (DOI:10.1021/ja063074c; PMID:16866529)
  accessed_at: '2026-11-09T12:00:00Z'
  support: supports
  summary: Establishes andrimid as a hybrid polyketide-nonribosomal peptide pyrrolidinedione
    antibiotic from Pantoea agglomerans that directly binds and inhibits the bacterial
    acetyl-CoA carboxylase carboxyltransferase beta/alpha complex (AccD/AccA, Ki =
    5 nM against E. coli AccAD), blocking malonyl-CoA formation and bacterial fatty
    acid biosynthesis.
- evidence_id: strict-validation-suite
  kind: validation
  reference: scripts/validate_strict.py
  locator: validate_strict.py and verify_corpus.py
  accessed_at: '2026-11-09T12:00:00Z'
  support: supports
  snapshot_sha256: d70e6739c881260927dfc99abea16e56be0f34f353f9f95353a43da76e8e7217
  summary: Confirms zero schema or ontology-label errors on andrimid.yaml and verifies
    that CHEBI:216634 meets all REVIEWED gate requirements.
assessments:
- assessment_id: andrimid-identity-moa-and-target-grounding
  area: evidence
  topic: Exact ChEBI structure, mode_of_action, AccAD target grounding, and UniProtKB
    protein_examples
  outcome: supported
  summary: Exact CHEBI:216634 identity, C27H33N3O5 chemical_structure, NATURAL_PRODUCT
    biosynthesis_origin, FATTY_ACID_SYNTHESIS_INHIBITION mode_of_action (MICROBIAL_TARGET),
    and PRIMARY_LITERATURE bacterial acetyl-CoA carboxylase carboxyltransferase (GO:0003989,
    PROTEIN) target with reviewed Swiss-Prot UniProtKB protein_examples P0ABD5 (accA)
    and P0A9Q5 (accD) in Escherichia coli K-12 are accurately grounded in DOI:10.1074/jbc.m402989200
    (PMID:15166242) and DOI:10.1021/ja063074c (PMID:16866529).
  target_ids:
  - CHEBI:216634
  evidence_ids:
  - andrimid-record
  - freiberg-2004-jin-2006-andrimid
- assessment_id: andrimid-curation-status-gate-alignment
  area: completeness
  topic: Eligibility of CHEBI:216634 for promotion from PROPOSED to REVIEWED
  outcome: concern
  summary: 'andrimid.yaml satisfies every REVIEWED gate requirement (grounding_status:
    EXACT, complete chemical_structure, curated mode_of_action, and PRIMARY_LITERATURE
    molecular_targets with reviewed Swiss-Prot UniProtKB protein_examples), but still
    carries curation_status: PROPOSED.'
  target_ids:
  - CHEBI:216634
  evidence_ids:
  - andrimid-record
  - freiberg-2004-jin-2006-andrimid
  - strict-validation-suite
findings:
- finding_id: andrimid-awaiting-reviewed-promotion
  issue_key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: 'Andrimid (CHEBI:216634) has complete EXACT structure and primary-literature
    mechanism/target curation but remains curation_status: PROPOSED'
  description: 'In data/antibiotics/antibacterial/andrimid.yaml (CHEBI:216634), Cycle
    8 Stage 1 seeded the exact ChEBI compound, Cycle 8 Stage 2 curated biosynthesis_origin:
    NATURAL_PRODUCT, mode_of_action: FATTY_ACID_SYNTHESIS_INHIBITION (MICROBIAL_TARGET)
    with CURATOR mode_of_action_notes, and a PRIMARY_LITERATURE molecular_targets
    entry for bacterial acetyl-CoA carboxylase carboxyltransferase (GO:0003989, PROTEIN,
    DIRECT_BINDING_TARGET), and Cycle 8 Stage 3 curated reviewed Swiss-Prot UniProtKB
    protein_examples P0ABD5 (accA) and P0A9Q5 (accD) in Escherichia coli K-12 backed
    by DOI:10.1074/jbc.m402989200 (PMID:15166242) and DOI:10.1021/ja063074c (PMID:16866529),
    yet curation_status remains PROPOSED.'
  target_ids:
  - CHEBI:216634
  field_paths:
  - curation_status
  - curation_history
  evidence_ids:
  - andrimid-record
  - freiberg-2004-jin-2006-andrimid
  - strict-validation-suite
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/andrimid.yaml
    role: Curator-owned curation_status slot on EXACT record
actions:
- action_id: promote-andrimid-to-reviewed
  description: 'Promote CHEBI:216634 (andrimid) from curation_status: PROPOSED to
    REVIEWED via record_curation_event and write_validated_antibiotic during Cycle
    8 Stage 5 grouped remediation.'
  finding_ids:
  - andrimid-awaiting-reviewed-promotion
  target_ids:
  - CHEBI:216634
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/andrimid.yaml
    role: Curator-owned curation_status slot
  acceptance_checks:
  - 'CHEBI:216634 carries curation_status: REVIEWED and survives seed_from_sources.py
    --apply --only CHEBI:216634.'
  - scripts/validate_strict.py and scripts/verify_corpus.py pass with 0 errors.
limitations:
- Stage 4 is a read-only review stage; no scientific YAML records were modified in
  this commit sequence.
notes:
- Andrimid is also included in the companion Cycle 8 Stage 4 full-inventory cohort
  review (3,125 records) under the open finding proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion
  alongside CHEBI:81029 (alanylclavam), CHEBI:199652 (amicetin), CHEBI:202006 (bottromycin
  A2), CHEBI:226796 (planosporicin), and CHEBI:204968 (ajudazol A).
tags:
- record-review
- andrimid
- antibacterial
- cycle-08
```
