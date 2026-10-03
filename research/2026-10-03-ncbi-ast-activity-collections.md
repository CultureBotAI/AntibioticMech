# NCBI AST lossless activity collections

Date: 2026-10-03

Scope: the storage component of issue #1022, implemented in PR #1024. This is
not NCBI AST adoption. No source inventory, corpus record, or published page
was changed by this audit. Bounded browsing and source terms remain gates.

## Full production-path result

The existing non-publishing audit was run at
`f78d2280b2f92a41301498287cb70f0e57c90d93`, with the collection-aware validated
writer, record loader, reseeder, and record renderer. It rebuilt the corpus from
the reviewed inventory and checked every affected record, not a sample.

```bash
uv run python scripts/audit_ncbi_ast_publication.py \
  --activity-report reports/ncbi_ast_assay_reviewed_2026-10-03/activity.tsv \
  --output-directory reports/ncbi_ast_collections_2026-10-03
```

Input activity report SHA-256:
`9ab2302b437ae2bb5a5aeec058fd21ba4cb11e0aeab58011b50f63e3288c0a80`.

Output `reports/ncbi_ast_collections_2026-10-03/audit.json` SHA-256:
`1bc9331cc60424651d8c243b8fd6b9cabcef66e120a932dc309b3c0f96a8e68e`.
The ignored report directory also retains every generated YAML, referenced gzip
artifact, and complete record HTML. All captured inputs were unchanged over the
run. Elapsed time was 483.781 seconds on this machine.

| Checked quantity | Result |
|---|---:|
| Exact compound records with AST observations | 32 |
| AST observations and distinct measured results | 188,759 |
| All activity rows, including existing non-AST rows | 190,833 |
| Consolidated observations with paired genome contexts | 52 |
| Unaffected records checked and unchanged | 2,907 |
| Referenced gzip artifacts | 389 |
| Largest compressed artifact, bytes | 64,957 |

Each affected record passed source-owned merge checks, closed-schema validation,
write/reload equality of the **entire expanded record**, unchanged reseeding,
and exact comparison of every rendered activity-table cell. The equality check
covers all evidence and fields that are not displayed in the current table.
The existing paired contexts, distinct assays, taxa, sample/genome IDs,
measurement/export counts, units, and comparators are preserved unchanged.

## Measured storage reduction

Compared with the full inline baseline recorded in
`research/2026-10-03-ncbi-ast-publication-audit.md`:

| Artifact | Inline baseline bytes | Collection bytes |
|---|---:|---:|
| YAML for affected records | 561,498,455 | 4,032,836 |
| Referenced gzip observations | 0 | 20,830,594 |
| Total record storage | 561,498,455 | 24,863,430 |
| Largest record: tetracycline YAML | 52,736,294 | 70,437 |
| Tetracycline gzip observations | 0 | 1,961,469 |

Total record storage is 95.57% smaller. Tetracycline's complete record storage
is 96.15% smaller; it still expands to 17,700 AST observations and 17,720 total
activity rows. Its validated write took 23.344 seconds; reload plus unchanged
reseed took 1.858 seconds. These are measurements, not cross-machine performance
guarantees.

The current renderer still emits 120,944,491 HTML bytes for the affected records,
including 11,259,459 bytes for tetracycline. This matches the baseline rerender
with the inherited accessible-table wrappers; it is not an HTML-size improvement.
No browser usability or full-site navigation claim follows from serialization.

## Validation and review

- 82 focused collection/publication tests passed; the broader storage, import,
  BioSample, CRyPTIC, seeder, graph-quality, source-queue, schema, and renderer
  regression run passed 356 tests.
- All 2,939 existing records passed closed-schema validation, and corpus
  reproduction reported no missing, unexpected, or drifted records.
- All 32 retained audit records re-emitted byte-identically, covering all
  188,759 AST observations, with no orphan artifacts. The generated current
  site also matched all 2,939 corpus records and seven classes.
- Existing-corpus byte-identical re-emission passed. An earlier broad test run
  had one outdated expectation that a missing collection path returns false;
  the API deliberately raises instead, and the corrected test passes.
- Adversarial review of the GitHub-served diff checked identity/provenance,
  ordering, cross-chunk duplicates, missing or corrupt artifacts, decompression
  limits, unsafe paths, complete evidence, source replacement, and atomic writes.
- Parent PR CI exposed a separate source-queue documentation claim failure,
  tracked as #1025. The parent fix keeps the snapshot-only count in the dated
  report and passes the unchanged numeric-claim test; it changes no data or
  collection implementation.
- A follow-up test review (#1026) replaced raw YAML reads in activity-sensitive
  documentation, table-accessibility, and publication fixtures with the same
  expanding loader as production. All 90 focused tests, including the unchanged
  numeric-claim gate, passed after that fix and the source-queue status update.

The format, loader contract, and explicit orphan cleanup are documented in
`docs/ACTIVITY_COLLECTIONS.md`. Full Linux QC is required before merge.

## Still required before adoption

1. Bounded activity browsing with access to every observation and its evidence,
   and complete downloadable data rather than a standalone manifest with missing
   companion files.
2. Full-site and desktop/mobile verification on the entire reviewed inventory.
3. A publication strategy for the 103,014,679-byte source-report inventory,
   separate from the now-compressed record artifacts.
4. The deferred source-terms decision.

Quarantined assay contexts and unmapped antibiotics remain excluded. Storage
compression does not independently verify submitted phenotypes or permit
species-wide resistance inference.
