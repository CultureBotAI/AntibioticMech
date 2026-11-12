# Formicamycin B: normalize the existing wrong-isomer finding to blocker

- Review: 20261021T164809Z-formicamycin-b-severity-correction
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:46:54Z
- Finished UTC: 2026-10-21T16:48:09Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

The saved formicamycin B review correctly establishes that the recorded para-methoxy graph is a superseded constitutional regioisomer but labels that finding major. The repository rubric assigns blocker to a record that denotes the wrong thing. This linked observation retains the exact issue key, affected target, evidence conclusion and open status, and normalizes severity to blocker. Original YAML/Markdown bytes and native data remain unchanged.

## Scope And Provenance

Only severity normalization of the linked saved finding F1, using its established chemical conclusion and the repository rubric. Native content is used only to identify the same target; primary literature and scientific evidence are not newly reassessed.

Selection: Correction of saved queue457 review metadata in a separate append-only branch, one exact target per observation. This adds no new scientific record coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-39c9b140ad | data/antibiotics/antibacterial/formicamycin-b.yaml | generated | formicamycin B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original immutable pair contract check | passed | True | antibioticmech:aro-39c9b140ad | Actual original-pair check exited zero after copying both saved B/D pairs byte-for-byte into the fresh branch. This validates review storage, not the underlying native chemistry. |
| Original bytes, captured inputs and lineage ledger | passed | True | antibioticmech:aro-39c9b140ad | All seven captured input hashes per target remain unchanged; original YAML/Markdown are byte-identical to batch046; exact finding/target identity and declared blocker rubric are verified. |

## Scientific And Domain Assessments

### Normalize the established identity defect

consistency: concern. Targets: antibioticmech:aro-39c9b140ad.

The earlier major label conflicts with the explicit blocker definition for a graph denoting a different constitutional isomer. The finding is retained as open and confirmed under its existing issue key, with severity blocker.

### Append-only lineage and bounded scope

provenance: supported. Targets: antibioticmech:aro-39c9b140ad.

Exact repository/review/finding lineage and affected target are retained. Original pair bytes remain unchanged. This metadata correction neither adds scientific coverage nor retires the identity defect or prior QC limitations.

## Findings

### F1: Formicamycin B retains the superseded para-methoxy structure

blocker / open / confirmed; issue key: formicamycin-b-obsolete-para-methoxy-regioisomer.

Original authors corrected formicamycin B in PMID41988676 using congener-specific 1,n-ADEQUATE NMR. The pendant E-ring methoxy is ortho to the biaryl linkage; native SMILES/InChI and all checked chemical authorities retain para methoxy and ortho hydroxy. Independent graph analysis gives ring distance3 for the current methoxy and distance1 for the current hydroxy. Correcting the methyl attachment preserves formula and bridgehead stereochemistry but changes constitution and InChIKey. The stored exact structure and equivalent xrefs therefore need an evidence-backed maintained correction; database agreement alone is insufficient.

Disposition: Open status retained. The earlier major severity was incorrectly normalized; no native correction or scientific resolution is claimed.

## Recommended Actions And Acceptance Checks

### A1

Curate the 2026 ortho-methoxy formicamycin B structure through maintained inputs and reconcile all exact links.

- Use the congener-specific original Figure3 and SI NMR evidence; preserve chlorine positions and 10R,19R centers.
- Recompute mutually consistent SMILES/InChI/InChIKey and confirm unchanged formula; adjudicate Sa axial representation explicitly.
- Retain an exact chemical xref only when its authority graph supports the corrected structure; document unresolved upstream records without treating them as exact matches.
- Regenerate reproducibly and run chemistry, schema, strict, provenance and corpus checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| prior-finding | reviews/structured/20261021T164021Z-formicamycin-b-review/review.yaml; F1: issue_key, description, severity, normalization_reason, affected fields and retained A1 | supports | The earlier review of antibioticmech:aro-39c9b140ad formicamycin B already establishes a congener-specific para-to-ortho methoxy constitutional correction based on original2026 evidence and graph comparison. F1 explicitly says a different constitutional regioisomer is encoded, yet its severity and native_severity say major. This observation uses that established conclusion for normalization without rereading or expanding its scientific scope. |
| rubric | docs/record-reviews.md; .claude/skills/review-yaml-record/SKILL.md; Verdict And Severity, blocker definition; workflow step6 | supports | Both governing texts classify wrong identity or a claim/representation making a record denote the wrong thing as blocker. The already-established constitutional-isomer defect meets that criterion. The prior major classification is therefore a metadata normalization error, independently of whether a valid SMILES parser accepts the old graph. |
| target | data/antibiotics/antibacterial/formicamycin-b.yaml; identifier, label and chemical_structure identity | context_only | The captured native file identifies the same antibioticmech:aro-39c9b140ad formicamycin B target. This is an identity anchor for the linked correction, not fresh chemical validation or a curation event. |
| bytes | severity001-setup.json; severity001-ledger.json; severity001-original-check.log; Actual original-pair comparisons, captured hashes and review-contract output | supports | The original saved YAML and rendered Markdown were copied byte-for-byte into the isolated correction worktree. Their original review IDs, timestamps, source hashes, text, scientific completion and findings remain unchanged. The new observation is separate and names the original F1 through previous_occurrences. |

## Limits And Additional Notes

- This is a metadata-only self-review. Completion means the severity audit is complete; it does not complete the earlier partial scientific assessment.
- The prior primary-source findings, chemical evidence, source access limits and actions remain authoritative at their original reviewed scope. They were not scientifically reassessed here.
- The earlier required full-QC failure from the pinned SciPy platform problem remains applicable to the scientific review. Native scientific gates were not rerun for this bounded severity normalization.
- The open identity finding is not resolved, rejected or accepted as risk. No native structure, cross-reference or source input was changed.
- The same issue_key and exact previous_occurrences reference are retained; no duplicate scientific issue or new coverage claim is created.
- The original saved review still records the historical major label; this separate linked observation supplies the corrected blocker normalization.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T164809Z-formicamycin-b-severity-correction
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Formicamycin B: normalize the existing wrong-isomer finding to blocker'
started_at: '2026-10-21T16:46:54Z'
finished_at: '2026-10-21T16:48:09Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: The agent team audits severity metadata in its own saved scientific
    review. This is explicitly a self-review; it is not an independent repeat scientific
    assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: Completed metadata-only severity normalization; prior scientific assessment
  remains partial and the identity finding remains open
scientific_review: false
summary: The saved formicamycin B review correctly establishes that the recorded para-methoxy
  graph is a superseded constitutional regioisomer but labels that finding major.
  The repository rubric assigns blocker to a record that denotes the wrong thing.
  This linked observation retains the exact issue key, affected target, evidence conclusion
  and open status, and normalizes severity to blocker. Original YAML/Markdown bytes
  and native data remain unchanged.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: data/antibiotics/antibacterial/formicamycin-b.yaml
    sha256: 0f9282954d03292cffe0b63e4ddfafd09ee2db19fe6f382fcef66619de12db72
    role: target
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: reviews/structured/20261021T164021Z-formicamycin-b-review/review.md
    sha256: 34b4f03fff6f025e01d72f82119f16d629ce142d047da1c3aa2773bd0fd65186
    role: context
  - path: reviews/structured/20261021T164021Z-formicamycin-b-review/review.yaml
    sha256: 5829a78e73cebddceca080196403e6d1b79052b4f596e843e8ce6c1a65318652
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
targets:
- target_id: antibioticmech:aro-39c9b140ad
  path: data/antibiotics/antibacterial/formicamycin-b.yaml
  label: formicamycin B
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Captured ChEBI inventory context; exact current terms checked separately;
      native structure comes from PubChem
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO identity, class and citation extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO identity, class, definition and citation owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Exact structure enrichment owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained PubChem structure enrichment owner
scope:
  description: Only severity normalization of the linked saved finding F1, using its
    established chemical conclusion and the repository rubric. Native content is used
    only to identify the same target; primary literature and scientific evidence are
    not newly reassessed.
  selection: Correction of saved queue457 review metadata in a separate append-only
    branch, one exact target per observation. This adds no new scientific record coverage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-39c9b140ad
  exclusions:
  - target: antibioticmech:aro-39c9b140ad
    reason: 'Excluded from this bounded metadata assessment: new scientific reassessment
      or sign-off, native/source curation or status changes, and resolution/rejection/accepted-risk
      disposition of the existing finding.'
checks:
- check_id: original-bundle-contract
  name: Original immutable pair contract check
  command: .venv/bin/python scripts/record_review.py check --base origin/main
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Actual original-pair check exited zero after copying both saved B/D pairs
    byte-for-byte into the fresh branch. This validates review storage, not the underlying
    native chemistry.
  target_ids:
  - antibioticmech:aro-39c9b140ad
  evidence_ids:
  - bytes
- check_id: provenance-ledger
  name: Original bytes, captured inputs and lineage ledger
  command: .venv/bin/python /private/tmp/am-review-session/severity001-ledger.py >
    /private/tmp/am-review-session/severity001-ledger.log 2>&1
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: All seven captured input hashes per target remain unchanged; original YAML/Markdown
    are byte-identical to batch046; exact finding/target identity and declared blocker
    rubric are verified.
  target_ids:
  - antibioticmech:aro-39c9b140ad
  evidence_ids:
  - bytes
  - rubric
evidence:
- evidence_id: prior-finding
  kind: prior_review
  reference: reviews/structured/20261021T164021Z-formicamycin-b-review/review.yaml
  locator: 'F1: issue_key, description, severity, normalization_reason, affected fields
    and retained A1'
  accessed_at: '2026-10-21T16:48:09Z'
  support: supports
  summary: The earlier review of antibioticmech:aro-39c9b140ad formicamycin B already
    establishes a congener-specific para-to-ortho methoxy constitutional correction
    based on original2026 evidence and graph comparison. F1 explicitly says a different
    constitutional regioisomer is encoded, yet its severity and native_severity say
    major. This observation uses that established conclusion for normalization without
    rereading or expanding its scientific scope.
  snapshot_sha256: 5829a78e73cebddceca080196403e6d1b79052b4f596e843e8ce6c1a65318652
- evidence_id: rubric
  kind: record_content
  reference: docs/record-reviews.md; .claude/skills/review-yaml-record/SKILL.md
  locator: Verdict And Severity, blocker definition; workflow step6
  accessed_at: '2026-10-21T16:48:09Z'
  support: supports
  summary: Both governing texts classify wrong identity or a claim/representation
    making a record denote the wrong thing as blocker. The already-established constitutional-isomer
    defect meets that criterion. The prior major classification is therefore a metadata
    normalization error, independently of whether a valid SMILES parser accepts the
    old graph.
- evidence_id: target
  kind: record_content
  reference: data/antibiotics/antibacterial/formicamycin-b.yaml
  locator: identifier, label and chemical_structure identity
  accessed_at: '2026-10-21T16:48:09Z'
  support: context_only
  summary: The captured native file identifies the same antibioticmech:aro-39c9b140ad
    formicamycin B target. This is an identity anchor for the linked correction, not
    fresh chemical validation or a curation event.
- evidence_id: bytes
  kind: validation
  reference: severity001-setup.json; severity001-ledger.json; severity001-original-check.log
  locator: Actual original-pair comparisons, captured hashes and review-contract output
  accessed_at: '2026-10-21T16:48:09Z'
  support: supports
  summary: The original saved YAML and rendered Markdown were copied byte-for-byte
    into the isolated correction worktree. Their original review IDs, timestamps,
    source hashes, text, scientific completion and findings remain unchanged. The
    new observation is separate and names the original F1 through previous_occurrences.
  snapshot_sha256: 45873d71e684b34d3772378a8b24036fda6bff88f5dd548a07e79dcbd334f617
assessments:
- assessment_id: severity
  area: consistency
  topic: Normalize the established identity defect
  outcome: concern
  summary: The earlier major label conflicts with the explicit blocker definition
    for a graph denoting a different constitutional isomer. The finding is retained
    as open and confirmed under its existing issue key, with severity blocker.
  target_ids:
  - antibioticmech:aro-39c9b140ad
  evidence_ids:
  - prior-finding
  - rubric
- assessment_id: lineage
  area: provenance
  topic: Append-only lineage and bounded scope
  outcome: supported
  summary: Exact repository/review/finding lineage and affected target are retained.
    Original pair bytes remain unchanged. This metadata correction neither adds scientific
    coverage nor retires the identity defect or prior QC limitations.
  target_ids:
  - antibioticmech:aro-39c9b140ad
  evidence_ids:
  - target
  - bytes
findings:
- finding_id: F1
  issue_key: formicamycin-b-obsolete-para-methoxy-regioisomer
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Formicamycin B retains the superseded para-methoxy structure
  description: Original authors corrected formicamycin B in PMID41988676 using congener-specific
    1,n-ADEQUATE NMR. The pendant E-ring methoxy is ortho to the biaryl linkage; native
    SMILES/InChI and all checked chemical authorities retain para methoxy and ortho
    hydroxy. Independent graph analysis gives ring distance3 for the current methoxy
    and distance1 for the current hydroxy. Correcting the methyl attachment preserves
    formula and bridgehead stereochemistry but changes constitution and InChIKey.
    The stored exact structure and equivalent xrefs therefore need an evidence-backed
    maintained correction; database agreement alone is insufficient.
  target_ids:
  - antibioticmech:aro-39c9b140ad
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  - xrefs
  evidence_ids:
  - prior-finding
  - rubric
  rule_id: 'review-checklist: exact chemical identity and primary-source support'
  native_severity: 'Blocker: recorded exact graph denotes a different constitutional
    regioisomer'
  normalization_reason: The earlier finding already establishes a different constitutional
    regioisomer. Under docs/record-reviews.md, Verdict And Severity, and review-yaml-record
    step6, wrong identity or a representation that denotes the wrong thing is blocker.
    This corrects only severity normalization; the chemical finding remains confirmed
    and open.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact molecular graph input
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained PubChem structure enrichment policy
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Exact identity and cross-reference input
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproduce corrected maintained inputs
  previous_occurrences:
  - repository: CultureBotAI/AntibioticMech
    review_id: 20261021T164021Z-formicamycin-b-review
    finding_id: F1
  disposition_reason: Open status retained. The earlier major severity was incorrectly
    normalized; no native correction or scientific resolution is claimed.
actions:
- action_id: A1
  description: Curate the 2026 ortho-methoxy formicamycin B structure through maintained
    inputs and reconcile all exact links.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-39c9b140ad
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact molecular graph input
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained PubChem structure enrichment policy
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Exact identity and cross-reference input
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproduce corrected maintained inputs
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Use the congener-specific original Figure3 and SI NMR evidence; preserve chlorine
    positions and 10R,19R centers.
  - Recompute mutually consistent SMILES/InChI/InChIKey and confirm unchanged formula;
    adjudicate Sa axial representation explicitly.
  - Retain an exact chemical xref only when its authority graph supports the corrected
    structure; document unresolved upstream records without treating them as exact
    matches.
  - Regenerate reproducibly and run chemistry, schema, strict, provenance and corpus
    checks.
limitations:
- This is a metadata-only self-review. Completion means the severity audit is complete;
  it does not complete the earlier partial scientific assessment.
- The prior primary-source findings, chemical evidence, source access limits and actions
  remain authoritative at their original reviewed scope. They were not scientifically
  reassessed here.
- The earlier required full-QC failure from the pinned SciPy platform problem remains
  applicable to the scientific review. Native scientific gates were not rerun for
  this bounded severity normalization.
- The open identity finding is not resolved, rejected or accepted as risk. No native
  structure, cross-reference or source input was changed.
notes:
- The same issue_key and exact previous_occurrences reference are retained; no duplicate
  scientific issue or new coverage claim is created.
- The original saved review still records the historical major label; this separate
  linked observation supplies the corrected blocker normalization.
related_reviews:
- repository: CultureBotAI/AntibioticMech
  review_id: 20261021T164021Z-formicamycin-b-review
  relationship: Corrects only F1 severity normalization from major to blocker; preserves
    the established scientific conclusion, open status, actions and scientific limitations.
links:
- https://github.com/CultureBotAI/AntibioticMech/blob/2ce81253f/reviews/structured/20261021T164021Z-formicamycin-b-review/review.yaml
tags:
- record-review
- severity-correction
- formicamycin-b
- self-review
```
