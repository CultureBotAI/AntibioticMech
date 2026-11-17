# Single-record review of obafluorin (CHEBI:199965)

- Review: 20261105T153000Z-obafluorin-record-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-11-05T15:20:00Z
- Finished UTC: 2026-11-05T15:30:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review of PROPOSED/EXACT record CHEBI:199965 (obafluorin, data/antibiotics/antibacterial/obafluorin.yaml) verified exact single-molecule chemical structure (C17H14N2O7, InChIKey AINNQKIVZOTQBB-KGLIPLIRSA-N, PubChem CID 146354), antibacterial filing (CHEBI:33282), CURATOR discovery and biosynthetic evidence (Schaffer et al. 2017 DOI:10.1038/nchembio.2374 / PMID:28504677; Scott et al. 2017 DOI:10.1038/ncomms15935 / PMID:28649989; Scott et al. 2019 DOI:10.1021/acschembio.9b00590 / PMID:31675206; Wells et al. 1984 DOI:10.7164/antibiotics.37.802 / PMID:6432765), MIBiG 4.0.1 BGC0001437 producer provenance in Pseudomonas fluorescens (NCBITaxon:294), biosynthesis_origin (NATURAL_PRODUCT), mode_of_action (PROTEIN_SYNTHESIS_INHIBITION, MICROBIAL_TARGET), and the PRIMARY_LITERATURE molecular_targets entry for bacterial threonyl-tRNA synthetase (ThrRS / ThrS; GO:0004829) carrying 1 reviewed Swiss-Prot UniProtKB protein_example (UniProtKB:P0A8M3 in Escherichia coli strain K12 NCBITaxon:83333). One open coherence finding requires Cycle 6 Stage 5 grouped remediation: despite having grounding_status: EXACT, complete chemical_structure, curated mode_of_action, and PRIMARY_LITERATURE molecular_targets with reviewed UniProtKB protein_examples, curation_status remains PROPOSED.

## Scope And Provenance

Complete single-record review of data/antibiotics/antibacterial/obafluorin.yaml (CHEBI:199965) across chemical identity, grounding, filing, source_concepts, producer_organisms, biosynthesis_origin, mode_of_action, molecular_targets, UniProtKB protein_examples accounting, and curation_status gate eligibility.

Selection: Selected CHEBI:199965 (obafluorin) as a representative PROPOSED/EXACT record in the 3,086-record Cycle 6 Stage 4 inventory that carries curated mode_of_action, PRIMARY_LITERATURE molecular_targets, and reviewed Swiss-Prot UniProtKB protein_examples and is immediately eligible for promotion to REVIEWED.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0de923c93426655dc335c3d92c6cda77dcc55d55.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:199965 | data/antibiotics/antibacterial/obafluorin.yaml | maintained | obafluorin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and ontology-grounding validation | passed | True | CHEBI:199965 | CHEBI:199965 passes closed LinkML schema validation and OAK ontology label correspondence (CHEBI:199965, CHEBI:33282, GO:0004829, NCBITaxon:294, NCBITaxon:2, NCBITaxon:83333) with 0 errors. |
| Corpus integrity and CURATOR provenance verification | passed | True | CHEBI:199965 | CHEBI:199965 passes verify_corpus.py with 0 errors; seeded fields match curation/curator_antibiotics.tsv and MIBiG 4.0.1 BGC0001437. |

## Scientific And Domain Assessments

### Exact ChEBI structure, mode_of_action, bacterial ThrRS target, and reviewed UniProtKB protein_examples

evidence: supported. Targets: CHEBI:199965.

Exact CHEBI:199965 identity, C17H14N2O7 chemical_structure, NATURAL_PRODUCT biosynthesis_origin, PROTEIN_SYNTHESIS_INHIBITION mode_of_action (MICROBIAL_TARGET), and PRIMARY_LITERATURE bacterial threonyl-tRNA synthetase (ThrRS / ThrS; GO:0004829) target with reviewed UniProtKB:P0A8M3 protein_example are accurately grounded in DOI:10.1038/nchembio.2374 (PMID:28504677) and DOI:10.1021/acschembio.9b00590 (PMID:31675206).

### Eligibility of CHEBI:199965 for promotion from PROPOSED to REVIEWED

completeness: concern. Targets: CHEBI:199965.

obafluorin.yaml satisfies every REVIEWED gate requirement (grounding_status: EXACT, complete chemical_structure, curated mode_of_action, and PRIMARY_LITERATURE molecular_targets with reviewed UniProtKB protein_examples), but still carries curation_status: PROPOSED.

## Findings

### obafluorin-awaiting-reviewed-promotion: Obafluorin (CHEBI:199965) has complete EXACT structure and primary-literature mechanism/target curation but remains curation_status: PROPOSED

major / open / confirmed; issue key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion.

In data/antibiotics/antibacterial/obafluorin.yaml (CHEBI:199965), Cycle 6 Stage 1 seeded the exact ChEBI compound, Cycle 6 Stage 2 curated biosynthesis_origin: NATURAL_PRODUCT and mode_of_action: PROTEIN_SYNTHESIS_INHIBITION (MICROBIAL_TARGET) with CURATOR mode_of_action_notes, and Cycle 6 Stage 3 curated a PRIMARY_LITERATURE molecular_targets entry for bacterial threonyl-tRNA synthetase (ThrRS / ThrS; GO:0004829) with 1 reviewed Swiss-Prot UniProtKB protein_example (UniProtKB:P0A8M3) backed by DOI:10.1038/nchembio.2374 (PMID:28504677) and DOI:10.1021/acschembio.9b00590 (PMID:31675206), yet curation_status remains PROPOSED.

## Recommended Actions And Acceptance Checks

### promote-obafluorin-to-reviewed

Promote CHEBI:199965 (obafluorin) from curation_status: PROPOSED to REVIEWED via record_curation_event and write_validated_antibiotic during Cycle 6 Stage 5 grouped remediation.

- CHEBI:199965 carries curation_status: REVIEWED and survives seed_from_sources.py --apply --only CHEBI:199965.
- scripts/validate_strict.py and scripts/verify_corpus.py pass with 0 errors.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| obafluorin-record | data/antibiotics/antibacterial/obafluorin.yaml; lines 1-145 | supports | CHEBI:199965 carries exact C17H14N2O7 structure (InChIKey AINNQKIVZOTQBB-KGLIPLIRSA-N, PubChem CID 146354), biosynthesis_origin: NATURAL_PRODUCT, mode_of_action: PROTEIN_SYNTHESIS_INHIBITION (MICROBIAL_TARGET), and PRIMARY_LITERATURE molecular_targets[0] for bacterial threonyl-tRNA synthetase (ThrRS / ThrS; GO:0004829) with 1 reviewed UniProtKB protein_example (P0A8M3), while retaining curation_status: PROPOSED. |
| schaffer-2017-scott-2019-obafluorin | DOI:10.1038/nchembio.2374; Schaffer et al. 2017 Nat Chem Biol 13:737-744 (PMID:28504677); Scott et al. 2019 ACS Chem Biol 14:2663-2671 (DOI:10.1021/acschembio.9b00590; PMID:31675206) | supports | Establishes obafluorin from Pseudomonas fluorescens ATCC 39502 as a strained beta-lactone aminoacyl antibiotic that covalently acylates the catalytic active-site nucleophile of bacterial threonyl-tRNA synthetase (ThrRS / ThrS) and blocks bacterial protein synthesis. |
| strict-validation-suite | scripts/validate_strict.py; validate_strict.py and verify_corpus.py | supports | Confirms zero schema or ontology-label errors on obafluorin.yaml and verifies that CHEBI:199965 meets all REVIEWED gate requirements. |

## Limits And Additional Notes

- Stage 4 is a read-only review stage; no scientific YAML records were modified in this commit sequence.
- Obafluorin is also included in the companion Cycle 6 Stage 4 full-inventory cohort review (3,086 records) under the open finding proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion alongside CHEBI:199044 (berninamycin A), CHEBI:205987 (berninamycin B), CHEBI:222785 (empedopeptin), CHEBI:219296 (laterocidine), CHEBI:227666 (salinamide A), CHEBI:200517 (salinamide B), and CHEBI:80106 (rimocidin).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T153000Z-obafluorin-record-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Single-record review of obafluorin (CHEBI:199965)
started_at: '2026-11-05T15:20:00Z'
finished_at: '2026-11-05T15:30:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Cycle 6 Stage 4 workflow record-review pass executed by the
    repository curation agent prior to independent adversarial PR review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION
scientific_review: true
summary: 'Whole-record review of PROPOSED/EXACT record CHEBI:199965 (obafluorin, data/antibiotics/antibacterial/obafluorin.yaml)
  verified exact single-molecule chemical structure (C17H14N2O7, InChIKey AINNQKIVZOTQBB-KGLIPLIRSA-N,
  PubChem CID 146354), antibacterial filing (CHEBI:33282), CURATOR discovery and biosynthetic
  evidence (Schaffer et al. 2017 DOI:10.1038/nchembio.2374 / PMID:28504677; Scott
  et al. 2017 DOI:10.1038/ncomms15935 / PMID:28649989; Scott et al. 2019 DOI:10.1021/acschembio.9b00590
  / PMID:31675206; Wells et al. 1984 DOI:10.7164/antibiotics.37.802 / PMID:6432765),
  MIBiG 4.0.1 BGC0001437 producer provenance in Pseudomonas fluorescens (NCBITaxon:294),
  biosynthesis_origin (NATURAL_PRODUCT), mode_of_action (PROTEIN_SYNTHESIS_INHIBITION,
  MICROBIAL_TARGET), and the PRIMARY_LITERATURE molecular_targets entry for bacterial
  threonyl-tRNA synthetase (ThrRS / ThrS; GO:0004829) carrying 1 reviewed Swiss-Prot
  UniProtKB protein_example (UniProtKB:P0A8M3 in Escherichia coli strain K12 NCBITaxon:83333).
  One open coherence finding requires Cycle 6 Stage 5 grouped remediation: despite
  having grounding_status: EXACT, complete chemical_structure, curated mode_of_action,
  and PRIMARY_LITERATURE molecular_targets with reviewed UniProtKB protein_examples,
  curation_status remains PROPOSED.'
source:
  git_revision: 0de923c93426655dc335c3d92c6cda77dcc55d55
  state: working_tree
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    role: context
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
  - path: curation/curator_antibiotics.tsv
    role: context
    sha256: a75ab22fa81df19ae960865a75cc8246e705a5244a5d826bf61281f32b080553
  - path: curation/uniprot_protein_examples.yaml
    role: context
    sha256: 65e3d635fa2e9cf7c393b123e5f2c9788f226e4ece6656bb76259190bae6017d
  - path: data/antibiotics/antibacterial/obafluorin.yaml
    role: target
    sha256: c995b3e61db54db4b21467babc3ededc95d61e761417ac26460779ed982b4a6b
  - path: docs/CURATION.md
    role: context
    sha256: 406dd63d134ae284cfa5b0f9bc79abae7a9045ad899bf7183d521fc13012b0f7
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
  description: Complete single-record review of data/antibiotics/antibacterial/obafluorin.yaml
    (CHEBI:199965) across chemical identity, grounding, filing, source_concepts, producer_organisms,
    biosynthesis_origin, mode_of_action, molecular_targets, UniProtKB protein_examples
    accounting, and curation_status gate eligibility.
  selection: Selected CHEBI:199965 (obafluorin) as a representative PROPOSED/EXACT
    record in the 3,086-record Cycle 6 Stage 4 inventory that carries curated mode_of_action,
    PRIMARY_LITERATURE molecular_targets, and reviewed Swiss-Prot UniProtKB protein_examples
    and is immediately eligible for promotion to REVIEWED.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:199965
targets:
- target_id: CHEBI:199965
  path: data/antibiotics/antibacterial/obafluorin.yaml
  label: obafluorin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/obafluorin.yaml
    role: Curator-maintained slots (curation_status, mode_of_action, molecular_targets)
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Seeded CURATOR source_concepts, definition, and MIBiG/PubChem structure
      provenance
checks:
- check_id: strict-schema-obafluorin
  name: Closed-schema and ontology-grounding validation
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py --quiet --workers 4 --out /tmp/instance_validation_failures.tsv
  exit_code: 0
  summary: CHEBI:199965 passes closed LinkML schema validation and OAK ontology label
    correspondence (CHEBI:199965, CHEBI:33282, GO:0004829, NCBITaxon:294, NCBITaxon:2,
    NCBITaxon:83333) with 0 errors.
  target_ids:
  - CHEBI:199965
  evidence_ids:
  - obafluorin-record
  - strict-validation-suite
- check_id: verify-corpus-obafluorin
  name: Corpus integrity and CURATOR provenance verification
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py --summary
  exit_code: 0
  summary: CHEBI:199965 passes verify_corpus.py with 0 errors; seeded fields match
    curation/curator_antibiotics.tsv and MIBiG 4.0.1 BGC0001437.
  target_ids:
  - CHEBI:199965
  evidence_ids:
  - obafluorin-record
  - strict-validation-suite
evidence:
- evidence_id: obafluorin-record
  kind: record_content
  reference: data/antibiotics/antibacterial/obafluorin.yaml
  locator: lines 1-145
  accessed_at: '2026-11-05T15:30:00Z'
  support: supports
  snapshot_sha256: c995b3e61db54db4b21467babc3ededc95d61e761417ac26460779ed982b4a6b
  summary: 'CHEBI:199965 carries exact C17H14N2O7 structure (InChIKey AINNQKIVZOTQBB-KGLIPLIRSA-N,
    PubChem CID 146354), biosynthesis_origin: NATURAL_PRODUCT, mode_of_action: PROTEIN_SYNTHESIS_INHIBITION
    (MICROBIAL_TARGET), and PRIMARY_LITERATURE molecular_targets[0] for bacterial
    threonyl-tRNA synthetase (ThrRS / ThrS; GO:0004829) with 1 reviewed UniProtKB
    protein_example (P0A8M3), while retaining curation_status: PROPOSED.'
- evidence_id: schaffer-2017-scott-2019-obafluorin
  kind: primary_source
  reference: DOI:10.1038/nchembio.2374
  locator: Schaffer et al. 2017 Nat Chem Biol 13:737-744 (PMID:28504677); Scott et
    al. 2019 ACS Chem Biol 14:2663-2671 (DOI:10.1021/acschembio.9b00590; PMID:31675206)
  accessed_at: '2026-11-05T15:30:00Z'
  support: supports
  summary: Establishes obafluorin from Pseudomonas fluorescens ATCC 39502 as a strained
    beta-lactone aminoacyl antibiotic that covalently acylates the catalytic active-site
    nucleophile of bacterial threonyl-tRNA synthetase (ThrRS / ThrS) and blocks bacterial
    protein synthesis.
- evidence_id: strict-validation-suite
  kind: validation
  reference: scripts/validate_strict.py
  locator: validate_strict.py and verify_corpus.py
  accessed_at: '2026-11-05T15:30:00Z'
  support: supports
  snapshot_sha256: d70e6739c881260927dfc99abea16e56be0f34f353f9f95353a43da76e8e7217
  summary: Confirms zero schema or ontology-label errors on obafluorin.yaml and verifies
    that CHEBI:199965 meets all REVIEWED gate requirements.
assessments:
- assessment_id: obafluorin-identity-moa-and-target-grounding
  area: evidence
  topic: Exact ChEBI structure, mode_of_action, bacterial ThrRS target, and reviewed
    UniProtKB protein_examples
  outcome: supported
  summary: Exact CHEBI:199965 identity, C17H14N2O7 chemical_structure, NATURAL_PRODUCT
    biosynthesis_origin, PROTEIN_SYNTHESIS_INHIBITION mode_of_action (MICROBIAL_TARGET),
    and PRIMARY_LITERATURE bacterial threonyl-tRNA synthetase (ThrRS / ThrS; GO:0004829)
    target with reviewed UniProtKB:P0A8M3 protein_example are accurately grounded
    in DOI:10.1038/nchembio.2374 (PMID:28504677) and DOI:10.1021/acschembio.9b00590
    (PMID:31675206).
  target_ids:
  - CHEBI:199965
  evidence_ids:
  - obafluorin-record
  - schaffer-2017-scott-2019-obafluorin
- assessment_id: obafluorin-curation-status-gate-alignment
  area: completeness
  topic: Eligibility of CHEBI:199965 for promotion from PROPOSED to REVIEWED
  outcome: concern
  summary: 'obafluorin.yaml satisfies every REVIEWED gate requirement (grounding_status:
    EXACT, complete chemical_structure, curated mode_of_action, and PRIMARY_LITERATURE
    molecular_targets with reviewed UniProtKB protein_examples), but still carries
    curation_status: PROPOSED.'
  target_ids:
  - CHEBI:199965
  evidence_ids:
  - obafluorin-record
  - schaffer-2017-scott-2019-obafluorin
  - strict-validation-suite
findings:
- finding_id: obafluorin-awaiting-reviewed-promotion
  issue_key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: 'Obafluorin (CHEBI:199965) has complete EXACT structure and primary-literature
    mechanism/target curation but remains curation_status: PROPOSED'
  description: 'In data/antibiotics/antibacterial/obafluorin.yaml (CHEBI:199965),
    Cycle 6 Stage 1 seeded the exact ChEBI compound, Cycle 6 Stage 2 curated biosynthesis_origin:
    NATURAL_PRODUCT and mode_of_action: PROTEIN_SYNTHESIS_INHIBITION (MICROBIAL_TARGET)
    with CURATOR mode_of_action_notes, and Cycle 6 Stage 3 curated a PRIMARY_LITERATURE
    molecular_targets entry for bacterial threonyl-tRNA synthetase (ThrRS / ThrS;
    GO:0004829) with 1 reviewed Swiss-Prot UniProtKB protein_example (UniProtKB:P0A8M3)
    backed by DOI:10.1038/nchembio.2374 (PMID:28504677) and DOI:10.1021/acschembio.9b00590
    (PMID:31675206), yet curation_status remains PROPOSED.'
  target_ids:
  - CHEBI:199965
  field_paths:
  - curation_status
  - curation_history
  evidence_ids:
  - obafluorin-record
  - schaffer-2017-scott-2019-obafluorin
  - strict-validation-suite
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/obafluorin.yaml
    role: Curator-owned curation_status slot on EXACT record
actions:
- action_id: promote-obafluorin-to-reviewed
  description: 'Promote CHEBI:199965 (obafluorin) from curation_status: PROPOSED to
    REVIEWED via record_curation_event and write_validated_antibiotic during Cycle
    6 Stage 5 grouped remediation.'
  finding_ids:
  - obafluorin-awaiting-reviewed-promotion
  target_ids:
  - CHEBI:199965
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/obafluorin.yaml
    role: Curator-owned curation_status slot
  acceptance_checks:
  - 'CHEBI:199965 carries curation_status: REVIEWED and survives seed_from_sources.py
    --apply --only CHEBI:199965.'
  - scripts/validate_strict.py and scripts/verify_corpus.py pass with 0 errors.
limitations:
- Stage 4 is a read-only review stage; no scientific YAML records were modified in
  this commit sequence.
notes:
- Obafluorin is also included in the companion Cycle 6 Stage 4 full-inventory cohort
  review (3,086 records) under the open finding proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion
  alongside CHEBI:199044 (berninamycin A), CHEBI:205987 (berninamycin B), CHEBI:222785
  (empedopeptin), CHEBI:219296 (laterocidine), CHEBI:227666 (salinamide A), CHEBI:200517
  (salinamide B), and CHEBI:80106 (rimocidin).
tags:
- record-review
- obafluorin
- antibacterial
- cycle-06
- stage-04
```
