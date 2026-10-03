# NCBI AST taxon and genome enrichment

This implements the exact-target join audited in
`2026-10-03-ncbi-ast-live-evaluation.md`. It enriches measured AST observations
with source TaxIDs, strain labels and versioned Assembly accessions. It does
not turn gene predictions into susceptibility evidence or infer species-wide
resistance from an isolate.

## Reproducible Source Capture

The native Isolates Browser JSON is downloaded by the existing AST snapshot
command using `--collection isolates`. A one-target canary was retrieved and
joined to all 18 measurements in the earlier AST canary before the full request.
The complete capture contains 37,177 unique targets, agreeing with both source
count checks. Its provenance is committed in
`2026-10-03-ncbi-ast-isolate-snapshot.json`; raw data remain local/ignored.

```bash
just fetch-ncbi-ast --collection isolates \
  --query target_acc:PDT000277868.2 \
  --output-dir downloads/ncbi_ast_isolate_snapshot_canary_2026-10-03
just fetch-ncbi-ast --collection isolates \
  --output-dir downloads/ncbi_ast_isolate_snapshot_2026-10-03
```

The downloader requests identity fields only. It does not request genotype,
predicted resistance or the mixed `isolate_identifiers` field. SRA identifiers
already present in an AST input are retained by the evaluator, but this join
does not infer them from a strain alias.

## Join And Provenance Contract

`--isolate-snapshot` verifies the manifest, raw JSON checksum, size, counts,
retrieval date and each source identity. It also verifies the AST file SHA-256
against `--source-version` before joining. A count match is a completeness
check, not proof that a changing remote service was transactionally frozen.

Every AST row must have an exact versioned target in the isolate index, with
agreeing BioSample, BioProject and scientific name. Duplicate targets, missing
joins, conflicting pre-existing TaxIDs/assemblies/strains and contradictory
identifier aliases fail the invocation before any report is written. A broad
organism-group label is not compared as if it were a precise scientific name.
Absent assemblies and strain labels stay absent; neither is inferred from the
TaxID or sample name.

The exact report adds `isolate_source_version` and
`isolate_source_retrieved_on`. They must be both empty for a non-enriched report
or carry one consistent checksum/date pair for an enriched report. Enriched
rows require a versioned target and a TaxID. Older local reports need to be
regenerated with the new header; there is no adopted NCBI AST inventory to
migrate. Group IDs continue to hash the biological observation/context columns,
not retrieval versions, as before.

The seeder preserves the original AST version as the phenotype source and adds
a separate evidence entry containing the isolate snapshot version/date and the
checked join relationship. Existing `ActivityObservation` identity fields and
its evidence list can express this without a shared-schema change.

## Evaluate The Captured Pair

```bash
just evaluate-ncbi-ast \
  --ast downloads/ncbi_ast_snapshot_2026-10-03/ast.tsv \
  --source-version ast-browser-sha256:ec6901ddfa0da41c0250875abc39b075d345c249cc39dbb17a998efaad2af184 \
  --source-retrieved-on 2026-10-03 \
  --isolate-snapshot downloads/ncbi_ast_isolate_snapshot_2026-10-03 \
  --drug-map curation/ncbi_ast_drug_map.tsv \
  --antibiotic-report reports/ncbi_ast_enriched_names.tsv \
  --activity-report reports/ncbi_ast_enriched_activity.tsv
```

The drug crosswalk remains pinned to the original measurement snapshot, not to
the independently retrieved identity metadata. A newer AST export requires a
re-audited crosswalk, and a changed isolate snapshot remains identifiable by
its own checksum even when the measured phenotype is unchanged.

## Adoption Boundary

The full captured-pair evaluation completed successfully:

| Measure | Count |
|---|---:|
| AST rows joined without identifier conflicts | 505,890 |
| Input rows with source TaxIDs after enrichment | 505,890 |
| Input rows with source Assembly accessions | 472,931 |
| Eligible exact-report observations | 233,497 |
| Eligible observations with TaxIDs | 233,497 |
| Eligible observations with Assembly accessions | 228,650 |
| Eligible observations with strain labels | 203,968 |
| Distinct source TaxIDs in the eligible report | 440 |
| Distinct Assembly accessions in the eligible report | 24,187 |

The independent seeder loader accepted every enriched report row. Every one
of the 233,497 converted `ActivityObservation` objects also passed closed-schema
validation. A full multiset comparison with the pre-enrichment report, omitting
only the added identity/provenance fields and derived group ID, found all other
fields unchanged: MIC and disk values, qualifiers, units, assays, phenotype
calls, sample/project context, counts and original AST provenance. None of
these checks wrote corpus records.

Focused tests passed (365 downloader, join, evaluator and importer cases), as
did 86 harmonization/source-queue tests, lint, and exact reproduction of all
2,939 existing corpus records. Review issue #1012 exposed conflicting optional
identity aliases when isolate metadata was absent; failing/passing regressions
cover the fix and preservation of agreeing aliases. Full local `just qc`
cannot install the pinned RDKit wheel on macOS x86_64; Linux QC remains required.

NCBI AST remains `EVALUATING`; the enriched report is not installed as a seed
inventory. CRyPTIC/source overlap, submitted assay consistency, the remaining
drug labels and the deferred source-terms decision remain adoption work.
