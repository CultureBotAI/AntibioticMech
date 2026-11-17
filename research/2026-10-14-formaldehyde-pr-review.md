# Formaldehyde Publication Review

PR: [#1114](https://github.com/CultureBotAI/AntibioticMech/pull/1114).
Reviewed checkpoint: `9c8813b44`.
This was a separate same-agent adversarial code and evidence-boundary review,
not independent scientific signoff or a whole-record primary review.

## Findings and Fixes

- [#1115](https://github.com/CultureBotAI/AntibioticMech/issues/1115), P2:
  the context-to-claims boundary accepted contradictory subject/background and
  reference taxon metadata. The builder now checks the native species,
  laboratory background, heterologous host, reference review status, gene names,
  organism/taxon names, TaxID/rank and strictly boolean lineage verification.
  Missing or changed values fail before claim generation.
- [#1116](https://github.com/CultureBotAI/AntibioticMech/issues/1116), P2:
  falsey non-array `results` values became scoped zero-hit search assertions.
  The handler now requires an object containing an explicit empty results
  array. Malformed responses are rejected; fuzzy suggestions remain unused.

All 34 new regression cases failed before the fixes. Afterward, the focused
suite passed **204 tests**, including all **64 formaldehyde tests**. The latter
also passed separately after formatting. Ruff lint, Ruff formatting and
`git diff --check` passed. Offline native-cache replay reproduced the saved
context exactly, and historical curation replay retained the saved record hash.

The focused suite covered `test_formaldehyde_efga.py`,
`test_curator_resistance_fields.py`, `test_antiviral_taxa.py` and
`test_resistance_checkpoint_records.py`. No additional defects were found in
the final scoped review of the fixes.

## Verification Boundary

The [original verification receipt](2026-10-14-formaldehyde-verification.json)
is immutable evidence for the pre-review checkpoint in `9c8813b44`, including
the 12-gate local QC run with 5,008 passing tests and four skips. All 30 file
pins matched before publication. After the fixes, only the audit script and
its test file differ among those pins; the biological record, evidence
artifacts, corpus indexes, generated pages and embedding artifacts are unchanged.
The receipt is not a claim that its old script/test hashes match this revision.

Pinned-environment PR and merge-queue CI results are recorded on the PR before
merge, separately from the prior local run with RDKit 2025.3.6. Private native
source caches are not published, so their replay test is skipped in clean CI;
public fixture, context-boundary and historical-writer tests run without them.

No scientific request, NCBI contact, source adoption or reuse-terms review was
performed during this publication review. #1040 remains deferred. Exact
experimental identities, broader literature and the corpus-wide goal remain
open.
