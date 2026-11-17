# Resistance Reference Publication Review

PR: [#1146](https://github.com/CultureBotAI/AntibioticMech/pull/1146).
Reviewed checkpoint: `30dd06aed`, based on `a03841240`.
This was a separate same-agent adversarial code and evidence-boundary review,
not independent scientific signoff or a whole-record primary review.

## Finding and Fix

- [#1147](https://github.com/CultureBotAI/AntibioticMech/issues/1147), P3:
  the PBP audit's `--output` option failed with `FileNotFoundError` for a new
  nested directory after building the dossier. It now creates missing parents
  only in the new-output write branch, retaining exclusive creation.

The new nested-output regression failed before the fix. Four portable CLI cases
now cover nested creation, unchanged existing output, read-only checks against
missing output, and divergent existing artifacts in both modes. All 57 PBP
tests passed after the fix, including native-cache replay. Ruff lint, Ruff
formatting and `git diff --check` passed.

The combined pre-fix suite passed 441 tests with one historical-fixture skip.
It covers all nine new audit modules and the shared protein-name projector.
Post-fix combined results and authoritative Linux CI are recorded on the PR.

## Review Scope

The review inspected all nine audit implementations, the shared projector
change, regression coverage, frozen plans, and public evidence boundaries.
Checks included exact ontology relation ownership, query completeness and
provenance, native TaxID/name disagreement handling, reference-versus-experiment
identity, source/host separation, chemical-form qualifiers, publication types,
negative findings, and access holds. No additional actionable defect was found
in this scoped pass. Primary papers were not independently re-read or figures
visually re-reviewed during publication; the dossiers retain those limitations.

An offline pin walk checked 965 pin occurrences across 387 distinct local paths
in the initial PR's JSON artifacts, including ignored native caches. No pinned
path was missing. Mismatches were limited to historical report versions and the
two PBP code/test files changed to address #1147. The 7,890-file PBP baseline was
also rechecked: all prior files except the already-appended report retained
their hashes, including all 2,939 biological records. No source-owned inputs,
generated records, schema, or site files differ from the PR base.

## Verification Boundary

The original cohort verification receipts are immutable checkpoint evidence.
The PBP receipt's script/test hashes identify the pre-review version in
`30dd06aed`, not the repaired version. Earlier report pins identify their
respective append-only research checkpoints. The fix does not change any
dossier, assessment, plan, biological record, or source request.

Native response caches remain local under ignored `reports/`. Cache-dependent
replay tests explicitly skip in clean CI; portable artifact and mutation tests
still run. Authoritative QC must pass on Linux before merge because the pinned
RDKit build is unavailable for local Intel macOS. CI results are recorded on the
PR separately from these local checkpoints.

No new scientific request, NCBI contact, source adoption, access-hold retry, or
reuse-terms review occurred during publication. #1040 remains deferred. The
corpus-wide investigation and whole-record primary signoffs remain open.
