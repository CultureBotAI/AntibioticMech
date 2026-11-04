# Single-record review of rustmicin (CHEBI:206910)

- Review: 20261104T152500Z-rustmicin-record-review
- Repository: culturebotai/AntibioticMech
- Started UTC: 2026-11-04T15:15:00Z
- Finished UTC: 2026-11-04T15:25:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review of PROPOSED/EXACT record CHEBI:206910 (rustmicin, data/antibiotics/antifungal/rustmicin.yaml) verified exact single-molecule chemical structure (C21H32O6, InChIKey WOFFENQLRMDHKE-VHWRYTFUSA-N, PubChem CID 10091177), antifungal filing (CHEBI:35718), CURATOR discovery and biosynthetic evidence (Mandala et al. 1998 DOI:10.1074/jbc.273.24.14942 / PMID:9614099; Karki et al. 2010 DOI:10.1111/j.1574-6968.2010.02048.x / PMID:20662933), MIBiG 4.0.1 BGC0000065 producer provenance in Streptomyces galbus (NCBITaxon:33898), biosynthesis_origin (NATURAL_PRODUCT), mode_of_action (CELL_MEMBRANE_SYNTHESIS_INHIBITION, MICROBIAL_TARGET), and the PRIMARY_LITERATURE molecular_targets entry for fungal inositol phosphorylceramide synthase (Aur1 / Ipc1; GO:0052645) carrying 2 reviewed Swiss-Prot UniProtKB protein_examples (UniProtKB:P36107 in Saccharomyces cerevisiae S288c NCBITaxon:559292 and UniProtKB:O13332 in Candida albicans SC5314 NCBITaxon:237561). One open coherence finding requires Cycle 5 Stage 5 grouped remediation: despite having grounding_status: EXACT, complete chemical_structure, curated mode_of_action, and PRIMARY_LITERATURE molecular_targets with reviewed UniProtKB protein_examples, curation_status remains PROPOSED.

## Scope And Provenance

Complete single-record review of data/antibiotics/antifungal/rustmicin.yaml (CHEBI:206910) across chemical identity, grounding, filing, source_concepts, producer_organisms, biosynthesis_origin, mode_of_action, molecular_targets, UniProtKB protein_examples accounting, and curation_status gate eligibility.

Selection: Selected CHEBI:206910 (rustmicin) as a representative PROPOSED/EXACT record in the 3,064-record Cycle 5 Stage 4 inventory that carries curated mode_of_action, PRIMARY_LITERATURE molecular_targets, and reviewed Swiss-Prot UniProtKB protein_examples and is immediately eligible for promotion to REVIEWED.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 47746980c7f56e7d9a37ebb7eb4d475d3a7ea6e5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:206910 | data/antibiotics/antifungal/rustmicin.yaml | maintained | rustmicin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and ontology-grounding validation | passed | True | CHEBI:206910 | CHEBI:206910 passes closed LinkML schema validation and OAK ontology label correspondence (CHEBI:206910, CHEBI:35718, GO:0052645, NCBITaxon:33898, NCBITaxon:4751, NCBITaxon:559292, NCBITaxon:237561) with 0 errors. |
| Corpus integrity and CURATOR provenance verification | passed | True | CHEBI:206910 | CHEBI:206910 passes verify_corpus.py with 0 errors; seeded fields match curation/curator_antibiotics.tsv and MIBiG 4.0.1 BGC0000065. |

## Scientific And Domain Assessments

### Exact ChEBI structure, mode_of_action, Aur1/Ipc1 IPC synthase target, and reviewed UniProtKB protein_examples

evidence: supported. Targets: CHEBI:206910.

Exact CHEBI:206910 identity, C21H32O6 chemical_structure, NATURAL_PRODUCT biosynthesis_origin, CELL_MEMBRANE_SYNTHESIS_INHIBITION mode_of_action (MICROBIAL_TARGET), and PRIMARY_LITERATURE fungal inositol phosphorylceramide synthase (Aur1 / Ipc1; GO:0052645) target with reviewed UniProtKB:P36107 and UniProtKB:O13332 protein_examples are accurately grounded in DOI:10.1074/jbc.273.24.14942 (PMID:9614099) and DOI:10.1111/j.1574-6968.2010.02048.x (PMID:20662933).

### Eligibility of CHEBI:206910 for promotion from PROPOSED to REVIEWED

completeness: concern. Targets: CHEBI:206910.

rustmicin.yaml satisfies every REVIEWED gate requirement (grounding_status: EXACT, complete chemical_structure, curated mode_of_action, and PRIMARY_LITERATURE molecular_targets with reviewed UniProtKB protein_examples), but still carries curation_status: PROPOSED.

## Findings

### rustmicin-awaiting-reviewed-promotion: Rustmicin (CHEBI:206910) has complete EXACT structure and primary-literature mechanism/target curation but remains curation_status: PROPOSED

major / open / confirmed; issue key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion.

In data/antibiotics/antifungal/rustmicin.yaml (CHEBI:206910), Cycle 5 Stage 1 seeded the exact ChEBI compound, Cycle 5 Stage 2 curated biosynthesis_origin: NATURAL_PRODUCT, mode_of_action: CELL_MEMBRANE_SYNTHESIS_INHIBITION (MICROBIAL_TARGET) with CURATOR mode_of_action_notes, and a PRIMARY_LITERATURE molecular_targets entry for fungal inositol phosphorylceramide synthase (Aur1 / Ipc1; GO:0052645), and Cycle 5 Stage 3 curated 2 reviewed Swiss-Prot UniProtKB protein_examples (UniProtKB:P36107, UniProtKB:O13332) backed by DOI:10.1074/jbc.273.24.14942 (PMID:9614099) and DOI:10.1111/j.1574-6968.2010.02048.x (PMID:20662933), yet curation_status remains PROPOSED.

## Recommended Actions And Acceptance Checks

### promote-rustmicin-to-reviewed

Promote CHEBI:206910 (rustmicin) from curation_status: PROPOSED to REVIEWED via record_curation_event and write_validated_antibiotic during Cycle 5 Stage 5 grouped remediation.

- CHEBI:206910 carries curation_status: REVIEWED and survives seed_from_sources.py --apply --only CHEBI:206910.
- scripts/validate_strict.py and scripts/verify_corpus.py pass with 0 errors.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| rustmicin-record | data/antibiotics/antifungal/rustmicin.yaml; lines 1-150 | supports | CHEBI:206910 carries exact C21H32O6 structure (InChIKey WOFFENQLRMDHKE-VHWRYTFUSA-N, PubChem CID 10091177), biosynthesis_origin: NATURAL_PRODUCT, mode_of_action: CELL_MEMBRANE_SYNTHESIS_INHIBITION (MICROBIAL_TARGET), and PRIMARY_LITERATURE molecular_targets[0] for fungal inositol phosphorylceramide synthase (Aur1 / Ipc1; GO:0052645) with 2 reviewed UniProtKB protein_examples (P36107, O13332), while retaining curation_status: PROPOSED. |
| mandala-1998-karki-2010-rustmicin | DOI:10.1074/jbc.273.24.14942; Mandala et al. 1998 J Biol Chem 273:14942-14949 (PMID:9614099); Karki et al. 2010 FEMS Microbiol Lett 310:69-75 (DOI:10.1111/j.1574-6968.2010.02048.x; PMID:20662933) | supports | Establishes rustmicin (galbonolide A) from Streptomyces galbus as a subnanomolar inhibitor of fungal inositol phosphorylceramide (IPC) synthase (Aur1 / Ipc1; C. neoformans IC50 = 70 pM, C. albicans IC50 = 4.3 nM, S. cerevisiae IC50 = 5.5 nM) that blocks fungal sphingolipid biosynthesis. |
| strict-validation-suite | scripts/validate_strict.py; validate_strict.py and verify_corpus.py | supports | Confirms zero schema or ontology-label errors on rustmicin.yaml and verifies that CHEBI:206910 meets all REVIEWED gate requirements. |

## Limits And Additional Notes

- Stage 4 is a read-only review stage; no scientific YAML records were modified in this commit sequence.
- Rustmicin is also included in the companion Cycle 5 Stage 4 full-inventory cohort review (3,064 records) under the open finding proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion alongside CHEBI:70619 (pentabromopseudilin), CHEBI:219845 (taromycin A), CHEBI:198520 (pneumocandin A0), and CHEBI:9200 (soraphen A).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T152500Z-rustmicin-record-review
kind: record
repository: culturebotai/AntibioticMech
title: Single-record review of rustmicin (CHEBI:206910)
started_at: '2026-11-04T15:15:00Z'
finished_at: '2026-11-04T15:25:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Cycle 5 Stage 4 workflow record-review pass executed by the
    repository curation agent prior to independent adversarial PR review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION
scientific_review: true
summary: 'Whole-record review of PROPOSED/EXACT record CHEBI:206910 (rustmicin, data/antibiotics/antifungal/rustmicin.yaml)
  verified exact single-molecule chemical structure (C21H32O6, InChIKey WOFFENQLRMDHKE-VHWRYTFUSA-N,
  PubChem CID 10091177), antifungal filing (CHEBI:35718), CURATOR discovery and biosynthetic
  evidence (Mandala et al. 1998 DOI:10.1074/jbc.273.24.14942 / PMID:9614099; Karki
  et al. 2010 DOI:10.1111/j.1574-6968.2010.02048.x / PMID:20662933), MIBiG 4.0.1 BGC0000065
  producer provenance in Streptomyces galbus (NCBITaxon:33898), biosynthesis_origin
  (NATURAL_PRODUCT), mode_of_action (CELL_MEMBRANE_SYNTHESIS_INHIBITION, MICROBIAL_TARGET),
  and the PRIMARY_LITERATURE molecular_targets entry for fungal inositol phosphorylceramide
  synthase (Aur1 / Ipc1; GO:0052645) carrying 2 reviewed Swiss-Prot UniProtKB protein_examples
  (UniProtKB:P36107 in Saccharomyces cerevisiae S288c NCBITaxon:559292 and UniProtKB:O13332
  in Candida albicans SC5314 NCBITaxon:237561). One open coherence finding requires
  Cycle 5 Stage 5 grouped remediation: despite having grounding_status: EXACT, complete
  chemical_structure, curated mode_of_action, and PRIMARY_LITERATURE molecular_targets
  with reviewed UniProtKB protein_examples, curation_status remains PROPOSED.'
source:
  git_revision: 47746980c7f56e7d9a37ebb7eb4d475d3a7ea6e5
  state: working_tree
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    role: context
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
  - path: curation/curator_antibiotics.tsv
    role: context
    sha256: 78b63b403fd2c96f428b6cd37010b24d853a777199109c93db946c469878680d
  - path: curation/uniprot_protein_examples.yaml
    role: context
    sha256: 923a34d1796bbf95b088fab14de96f4e464d5a0f824dc95b57bb3cdc09981e41
  - path: data/antibiotics/antifungal/rustmicin.yaml
    role: target
    sha256: 986994d61a86698834710ab547e4ee8c2a50335c4555fd3e37eebdedd801e8bd
  - path: docs/CURATION.md
    role: context
    sha256: c0de443e6d91e787119551e48da2666bb972e1236b2a421f170c518cbe7d6289
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
  description: Complete single-record review of data/antibiotics/antifungal/rustmicin.yaml
    (CHEBI:206910) across chemical identity, grounding, filing, source_concepts, producer_organisms,
    biosynthesis_origin, mode_of_action, molecular_targets, UniProtKB protein_examples
    accounting, and curation_status gate eligibility.
  selection: Selected CHEBI:206910 (rustmicin) as a representative PROPOSED/EXACT
    record in the 3,064-record Cycle 5 Stage 4 inventory that carries curated mode_of_action,
    PRIMARY_LITERATURE molecular_targets, and reviewed Swiss-Prot UniProtKB protein_examples
    and is immediately eligible for promotion to REVIEWED.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:206910
targets:
- target_id: CHEBI:206910
  path: data/antibiotics/antifungal/rustmicin.yaml
  label: rustmicin
  record_class: AntibioticRecord
  kind: maintained
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antifungal/rustmicin.yaml
    role: Curator-maintained slots (curation_status, mode_of_action, molecular_targets)
  - repository: culturebotai/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Seeded CURATOR source_concepts, definition, and MIBiG/PubChem structure
      provenance
checks:
- check_id: strict-schema-rustmicin
  name: Closed-schema and ontology-grounding validation
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py --quiet --workers 4 --out /tmp/instance_validation_failures.tsv
  exit_code: 0
  summary: CHEBI:206910 passes closed LinkML schema validation and OAK ontology label
    correspondence (CHEBI:206910, CHEBI:35718, GO:0052645, NCBITaxon:33898, NCBITaxon:4751,
    NCBITaxon:559292, NCBITaxon:237561) with 0 errors.
  target_ids:
  - CHEBI:206910
  evidence_ids:
  - rustmicin-record
  - strict-validation-suite
- check_id: verify-corpus-rustmicin
  name: Corpus integrity and CURATOR provenance verification
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py --summary
  exit_code: 0
  summary: CHEBI:206910 passes verify_corpus.py with 0 errors; seeded fields match
    curation/curator_antibiotics.tsv and MIBiG 4.0.1 BGC0000065.
  target_ids:
  - CHEBI:206910
  evidence_ids:
  - rustmicin-record
  - strict-validation-suite
evidence:
- evidence_id: rustmicin-record
  kind: record_content
  reference: data/antibiotics/antifungal/rustmicin.yaml
  locator: lines 1-150
  accessed_at: '2026-11-04T15:25:00Z'
  support: supports
  snapshot_sha256: 986994d61a86698834710ab547e4ee8c2a50335c4555fd3e37eebdedd801e8bd
  summary: 'CHEBI:206910 carries exact C21H32O6 structure (InChIKey WOFFENQLRMDHKE-VHWRYTFUSA-N,
    PubChem CID 10091177), biosynthesis_origin: NATURAL_PRODUCT, mode_of_action: CELL_MEMBRANE_SYNTHESIS_INHIBITION
    (MICROBIAL_TARGET), and PRIMARY_LITERATURE molecular_targets[0] for fungal inositol
    phosphorylceramide synthase (Aur1 / Ipc1; GO:0052645) with 2 reviewed UniProtKB
    protein_examples (P36107, O13332), while retaining curation_status: PROPOSED.'
- evidence_id: mandala-1998-karki-2010-rustmicin
  kind: primary_source
  reference: DOI:10.1074/jbc.273.24.14942
  locator: Mandala et al. 1998 J Biol Chem 273:14942-14949 (PMID:9614099); Karki et
    al. 2010 FEMS Microbiol Lett 310:69-75 (DOI:10.1111/j.1574-6968.2010.02048.x;
    PMID:20662933)
  accessed_at: '2026-11-04T15:25:00Z'
  support: supports
  summary: Establishes rustmicin (galbonolide A) from Streptomyces galbus as a subnanomolar
    inhibitor of fungal inositol phosphorylceramide (IPC) synthase (Aur1 / Ipc1; C.
    neoformans IC50 = 70 pM, C. albicans IC50 = 4.3 nM, S. cerevisiae IC50 = 5.5 nM)
    that blocks fungal sphingolipid biosynthesis.
- evidence_id: strict-validation-suite
  kind: validation
  reference: scripts/validate_strict.py
  locator: validate_strict.py and verify_corpus.py
  accessed_at: '2026-11-04T15:25:00Z'
  support: supports
  snapshot_sha256: d70e6739c881260927dfc99abea16e56be0f34f353f9f95353a43da76e8e7217
  summary: Confirms zero schema or ontology-label errors on rustmicin.yaml and verifies
    that CHEBI:206910 meets all REVIEWED gate requirements.
assessments:
- assessment_id: rustmicin-identity-moa-and-target-grounding
  area: evidence
  topic: Exact ChEBI structure, mode_of_action, Aur1/Ipc1 IPC synthase target, and
    reviewed UniProtKB protein_examples
  outcome: supported
  summary: Exact CHEBI:206910 identity, C21H32O6 chemical_structure, NATURAL_PRODUCT
    biosynthesis_origin, CELL_MEMBRANE_SYNTHESIS_INHIBITION mode_of_action (MICROBIAL_TARGET),
    and PRIMARY_LITERATURE fungal inositol phosphorylceramide synthase (Aur1 / Ipc1;
    GO:0052645) target with reviewed UniProtKB:P36107 and UniProtKB:O13332 protein_examples
    are accurately grounded in DOI:10.1074/jbc.273.24.14942 (PMID:9614099) and DOI:10.1111/j.1574-6968.2010.02048.x
    (PMID:20662933).
  target_ids:
  - CHEBI:206910
  evidence_ids:
  - rustmicin-record
  - mandala-1998-karki-2010-rustmicin
- assessment_id: rustmicin-curation-status-gate-alignment
  area: completeness
  topic: Eligibility of CHEBI:206910 for promotion from PROPOSED to REVIEWED
  outcome: concern
  summary: 'rustmicin.yaml satisfies every REVIEWED gate requirement (grounding_status:
    EXACT, complete chemical_structure, curated mode_of_action, and PRIMARY_LITERATURE
    molecular_targets with reviewed UniProtKB protein_examples), but still carries
    curation_status: PROPOSED.'
  target_ids:
  - CHEBI:206910
  evidence_ids:
  - rustmicin-record
  - mandala-1998-karki-2010-rustmicin
  - strict-validation-suite
findings:
- finding_id: rustmicin-awaiting-reviewed-promotion
  issue_key: proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: 'Rustmicin (CHEBI:206910) has complete EXACT structure and primary-literature
    mechanism/target curation but remains curation_status: PROPOSED'
  description: 'In data/antibiotics/antifungal/rustmicin.yaml (CHEBI:206910), Cycle
    5 Stage 1 seeded the exact ChEBI compound, Cycle 5 Stage 2 curated biosynthesis_origin:
    NATURAL_PRODUCT, mode_of_action: CELL_MEMBRANE_SYNTHESIS_INHIBITION (MICROBIAL_TARGET)
    with CURATOR mode_of_action_notes, and a PRIMARY_LITERATURE molecular_targets
    entry for fungal inositol phosphorylceramide synthase (Aur1 / Ipc1; GO:0052645),
    and Cycle 5 Stage 3 curated 2 reviewed Swiss-Prot UniProtKB protein_examples (UniProtKB:P36107,
    UniProtKB:O13332) backed by DOI:10.1074/jbc.273.24.14942 (PMID:9614099) and DOI:10.1111/j.1574-6968.2010.02048.x
    (PMID:20662933), yet curation_status remains PROPOSED.'
  target_ids:
  - CHEBI:206910
  field_paths:
  - curation_status
  - curation_history
  evidence_ids:
  - rustmicin-record
  - mandala-1998-karki-2010-rustmicin
  - strict-validation-suite
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antifungal/rustmicin.yaml
    role: Curator-owned curation_status slot on EXACT record
actions:
- action_id: promote-rustmicin-to-reviewed
  description: 'Promote CHEBI:206910 (rustmicin) from curation_status: PROPOSED to
    REVIEWED via record_curation_event and write_validated_antibiotic during Cycle
    5 Stage 5 grouped remediation.'
  finding_ids:
  - rustmicin-awaiting-reviewed-promotion
  target_ids:
  - CHEBI:206910
  owner_paths:
  - repository: culturebotai/AntibioticMech
    path: data/antibiotics/antifungal/rustmicin.yaml
    role: Curator-owned curation_status slot
  acceptance_checks:
  - 'CHEBI:206910 carries curation_status: REVIEWED and survives seed_from_sources.py
    --apply --only CHEBI:206910.'
  - scripts/validate_strict.py and scripts/verify_corpus.py pass with 0 errors.
limitations:
- Stage 4 is a read-only review stage; no scientific YAML records were modified in
  this commit sequence.
notes:
- Rustmicin is also included in the companion Cycle 5 Stage 4 full-inventory cohort
  review (3,064 records) under the open finding proposed-exact-records-with-primary-targets-awaiting-reviewed-promotion
  alongside CHEBI:70619 (pentabromopseudilin), CHEBI:219845 (taromycin A), CHEBI:198520
  (pneumocandin A0), and CHEBI:9200 (soraphen A).
tags:
- record-review
- rustmicin
- antifungal
- cycle-05
- stage-04
```
