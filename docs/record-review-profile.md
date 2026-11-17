# AntibioticMech review profile

New record reviews follow [the shared contract](record-reviews.md), with
authoritative YAML and derived Markdown under
`reviews/structured/<YYYYMMDDTHHMMSSZ>-<slug>/`. Historical ad hoc reports remain
historical evidence and need no migration. `conf/record_review.yaml` lists the
active routes and local rubrics.

## Routes and output

- `.claude/skills/review-yaml-record/SKILL.md`: one resolved record.
- `.claude/skills/review-yaml-category/SKILL.md`: a coherent category with
  explicit lump/split/retain/defer decisions; sampled coverage keeps its method,
  denominator, inspected members and limitations. Explicit batches use `kind: batch`.
- `.claude/skills/curate-yaml-record/SKILL.md`: the audit-only route uses the
  same output contract and retains the native scientific checklist.
- `.claude/skills/research-resistant-taxa/SKILL.md`: scoped resistant-taxa
  evidence assessment of one compound, retaining strain/assay/breakpoint context.

Run from the repository root using its own Python environment (LinkML,
linkml-runtime, jsonschema and PyYAML; pytest in the dev extra):

```bash
uv run python scripts/record_review.py inspect --targets /tmp/review-targets.yaml
just review-validate /tmp/completed-review.yaml
just review-save /tmp/completed-review.yaml
just review-check
```

Use session-unique temporary inputs and add `--input <path>` to inspect for each
additional rubric/schema/source/overlay used. Retain the captured Git revision
and hashes. Checks record actual commands and exit codes, never invented
success. New observations are immutable; link both saved files in the final
response. Missing dependencies or required checks are an explicit blocked output
step or partial assessment, not permission to save unvalidated prose.

## Native questions and ownership

Review exact structures under `data/antibiotics/`, including salt/stereo/charge
identity, filing class versus activity roles, mode of action and target scope,
claim-level mechanism/AST evidence, MIC units and assay, resistance determinants,
and producer context. The resistant-taxa route adds strain, isolate, genome and
versioned breakpoint dimensions without claiming whole-record coverage.

Seeded identity, structure, classification and imported claims are owned by
`data/raw/`, `curation/decisions.tsv`, `curation/curator_antibiotics.tsv`, and the
applicable extractor/seeder. Curator-owned claims require the native validated
writer and curation event; identify the actual owner for each finding. Include
referenced activity collection inputs when they inform the assessment.
`docs/CURATION.md`, `docs/HARMONIZATION.md`, and the local checklist define
the scientific rubric. REVIEWED still requires exact identity/grounding,
consistent structure, correct class/roles and checked mode of action; a valid
review bundle does not satisfy or change those gates.

## Native checks and queue

```bash
just validate-strict <record-path> --out /tmp/antibioticmech-record-validation.tsv
just verify-corpus --summary
just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv
just qc
```

`scripts/curation_worklist.py` produces deterministic readiness/lead rows, not
scientific sign-off. `scripts/search_publications.py` produces discovery leads.
Neither output is a completed review: inspect sources and save the final
assessment through the shared validator/saver. Assay-review maps and BioSample
adjudication snapshots are native ingestion inputs, not structured record-review
bundles. Provider research remains separately authorized.

## Validation and ownership of the contract

`schema/record_review.yaml`, `scripts/record_review.py`,
`docs/record-reviews.md`, and `tests/test_record_review_contract.py` are copied
byte-identically from CLAW. Canonical marked skill regions are rendered with
the native sections preserved. Edit the shared contract upstream and re-adopt;
the local profile, rubrics and scientific status gates remain repository-owned.
`just review-check` validates retained bundles and runs the profile/roundtrip
contract tests. The existing PR and merge-group quality workflow also runs the
contract test alongside its unchanged native checks. Zero structured reviews
means missing coverage, not a scientific pass. The new path is Git-visible
without opening ignored legacy report directories.

CI fetches full history and sets `RECORD_REVIEW_BASE` from the trusted PR base,
merge-group base, or push-before SHA. It requires that commit to exist before
running the canonical test, which rejects changes or deletions to previously
saved bundles. Local `just review-check` defaults to HEAD; set
`RECORD_REVIEW_BASE=<base-commit>` when checking a branch's committed changes.
There is no automatic CI fallback to an already modified HEAD.
