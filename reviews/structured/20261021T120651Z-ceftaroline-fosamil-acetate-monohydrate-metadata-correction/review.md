# ceftaroline fosamil acetate monohydrate: correction of unrelated review links and tags

- Review: 20261021T120651Z-ceftaroline-fosamil-acetate-monohydrate-metadata-correction
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:05:37Z
- Finished UTC: 2026-10-21T12:06:51Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The related earlier review contains unrelated cefozopran links and tags copied from a template. This linked observation identifies the correct ceftaroline fosamil acetate monohydrate reference and tags. It does not change the earlier scientific assessment, findings, evidence, completion limitations or native record.

## Scope And Provenance

Only optional links and tags on the exact related review; native content is read only to resolve its target. Scientific claims and findings are carried by the earlier scientific review, not reassessed here.

Selection: Correction after a bounded audit of handed-off review metadata; one exact record per bundle.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:70714 | data/antibiotics/antibacterial/ceftaroline-fosamil-acetate-monohydrate.yaml | generated | ceftaroline fosamil acetate monohydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Validate original immutable pairs | passed | True | CHEBI:70714 | All five copied originals passed the contract and are byte-identical to their saved source pairs. |

## Scientific And Domain Assessments

### Correct reference and classification metadata for this review target

provenance: supported. Targets: CHEBI:70714.

For the linked earlier review, disregard the three cefozopran links and copied tags. Use the exact ChEBI link and target-specific tags supplied by this observation. This correction does not override any prior scientific finding.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| original | reviews/structured/20261021T115721Z-ceftaroline-fosamil-acetate-monohydrate/review.yaml; Top-level links and tags, contrasted with targets, title and evidence | context_only | The earlier scientific review correctly targets CHEBI:70714 ceftaroline fosamil acetate monohydrate but its optional links point to CHEBI:3502 and cefozopran synthesis DOI10.7164/antibiotics.45.709 (including its J-STAGE PDF). The cefozopran tag and those three links are unrelated to this target. Other inherited generic tags can be applicable and are not individually declared false. |
| target | data/antibiotics/antibacterial/ceftaroline-fosamil-acetate-monohydrate.yaml; identifier, label and source concepts; earlier evidence and chemical authority references | supports | The exact native target and earlier scientific evidence establish CHEBI:70714 ceftaroline fosamil acetate monohydrate. The corrected authority link is https://www.ebi.ac.uk/chebi/CHEBI:70714. The replacement tags below describe this metadata observation; all earlier source evidence remains in the linked scientific review. |
| bytes | metadata001-original-check.log; Actual command output and byte comparison against original saved YAML/Markdown | supports | The original pair was copied byte-for-byte into this standalone branch, then included in a successful append-only contract check. Its original ID, timestamps, input hashes and scientific content remain unchanged. |

## Limits And Additional Notes

- This is a metadata-only self-review. No scientific finding is resolved, rejected or replaced, and no new scientific sign-off is claimed.
- Earlier required QC failures and all scientific limitations remain applicable. Native scientific gates were not rerun for this bounded metadata correction.
- The earlier immutable YAML/Markdown necessarily retains its historical erroneous metadata; this linked observation supplies the correction.
- Correct links: https://www.ebi.ac.uk/chebi/CHEBI:70714
- Correct tags for this metadata observation: record-review, ceftaroline-fosamil-acetate-monohydrate, metadata-correction
- Original scientific review: 20261021T115721Z-ceftaroline-fosamil-acetate-monohydrate

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T120651Z-ceftaroline-fosamil-acetate-monohydrate-metadata-correction
kind: record
repository: CultureBotAI/AntibioticMech
title: 'ceftaroline fosamil acetate monohydrate: correction of unrelated review links
  and tags'
started_at: '2026-10-21T12:05:37Z'
finished_at: '2026-10-21T12:06:51Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: The coordinator audits metadata in its own previously saved
    review; this is explicitly a self-review, not an independent scientific reassessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: The related earlier review contains unrelated cefozopran links and tags copied
  from a template. This linked observation identifies the correct ceftaroline fosamil
  acetate monohydrate reference and tags. It does not change the earlier scientific
  assessment, findings, evidence, completion limitations or native record.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: data/antibiotics/antibacterial/ceftaroline-fosamil-acetate-monohydrate.yaml
    sha256: 2cca302e8f83403d3f6f72e6f43577384647e9501ea7ca3e2ad634ff789ac064
    role: target
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: reviews/structured/20261021T115721Z-ceftaroline-fosamil-acetate-monohydrate/review.md
    sha256: 5cfe2129dfc1ebaa8f32c8c665fcc8c673566d622bbccc7cdb035756400c6f0c
    role: context
  - path: reviews/structured/20261021T115721Z-ceftaroline-fosamil-acetate-monohydrate/review.yaml
    sha256: 61ae05a3b3a5b49e9d4e4b60d541ca5d920ec24e22b2537c53629e15d28744aa
    role: context
targets:
- target_id: CHEBI:70714
  path: data/antibiotics/antibacterial/ceftaroline-fosamil-acetate-monohydrate.yaml
  label: ceftaroline fosamil acetate monohydrate
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI identity, structure, definition, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusion overrides
scope:
  description: Only optional links and tags on the exact related review; native content
    is read only to resolve its target. Scientific claims and findings are carried
    by the earlier scientific review, not reassessed here.
  selection: Correction after a bounded audit of handed-off review metadata; one exact
    record per bundle.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:70714
  exclusions:
  - target: Native scientific claims and prior finding dispositions
    reason: Only review metadata is corrected; previous scientific assessments and
      limitations remain authoritative at their original scope.
checks:
- check_id: original-bundle-contract
  name: Validate original immutable pairs
  status: passed
  required: true
  summary: All five copied originals passed the contract and are byte-identical to
    their saved source pairs.
  command: .venv/bin/python scripts/record_review.py check --base origin/main
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:70714
  evidence_ids:
  - original
  - bytes
evidence:
- evidence_id: original
  kind: prior_review
  reference: reviews/structured/20261021T115721Z-ceftaroline-fosamil-acetate-monohydrate/review.yaml
  locator: Top-level links and tags, contrasted with targets, title and evidence
  accessed_at: '2026-10-21T12:05:37Z'
  support: context_only
  summary: The earlier scientific review correctly targets CHEBI:70714 ceftaroline
    fosamil acetate monohydrate but its optional links point to CHEBI:3502 and cefozopran
    synthesis DOI10.7164/antibiotics.45.709 (including its J-STAGE PDF). The cefozopran
    tag and those three links are unrelated to this target. Other inherited generic
    tags can be applicable and are not individually declared false.
  snapshot_sha256: 61ae05a3b3a5b49e9d4e4b60d541ca5d920ec24e22b2537c53629e15d28744aa
- evidence_id: target
  kind: record_content
  reference: data/antibiotics/antibacterial/ceftaroline-fosamil-acetate-monohydrate.yaml
  locator: identifier, label and source concepts; earlier evidence and chemical authority
    references
  accessed_at: '2026-10-21T12:05:37Z'
  support: supports
  summary: The exact native target and earlier scientific evidence establish CHEBI:70714
    ceftaroline fosamil acetate monohydrate. The corrected authority link is https://www.ebi.ac.uk/chebi/CHEBI:70714.
    The replacement tags below describe this metadata observation; all earlier source
    evidence remains in the linked scientific review.
- evidence_id: bytes
  kind: validation
  reference: metadata001-original-check.log
  locator: Actual command output and byte comparison against original saved YAML/Markdown
  accessed_at: '2026-10-21T12:05:37Z'
  support: supports
  summary: The original pair was copied byte-for-byte into this standalone branch,
    then included in a successful append-only contract check. Its original ID, timestamps,
    input hashes and scientific content remain unchanged.
assessments:
- assessment_id: metadata
  area: provenance
  topic: Correct reference and classification metadata for this review target
  outcome: supported
  summary: For the linked earlier review, disregard the three cefozopran links and
    copied tags. Use the exact ChEBI link and target-specific tags supplied by this
    observation. This correction does not override any prior scientific finding.
  target_ids:
  - CHEBI:70714
  evidence_ids:
  - original
  - target
  - bytes
findings: []
actions: []
limitations:
- This is a metadata-only self-review. No scientific finding is resolved, rejected
  or replaced, and no new scientific sign-off is claimed.
- Earlier required QC failures and all scientific limitations remain applicable. Native
  scientific gates were not rerun for this bounded metadata correction.
- The earlier immutable YAML/Markdown necessarily retains its historical erroneous
  metadata; this linked observation supplies the correction.
notes:
- 'Correct links: https://www.ebi.ac.uk/chebi/CHEBI:70714'
- 'Correct tags for this metadata observation: record-review, ceftaroline-fosamil-acetate-monohydrate,
  metadata-correction'
- 'Original scientific review: 20261021T115721Z-ceftaroline-fosamil-acetate-monohydrate'
links:
- https://www.ebi.ac.uk/chebi/CHEBI:70714
tags:
- record-review
- ceftaroline-fosamil-acetate-monohydrate
- metadata-correction
related_reviews:
- repository: CultureBotAI/AntibioticMech
  review_id: 20261021T115721Z-ceftaroline-fosamil-acetate-monohydrate
  relationship: Corrects only unrelated optional links and tags; preserves all scientific
    findings and assessments.
```
