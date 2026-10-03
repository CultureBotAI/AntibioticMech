# NCBI AST record-publication audit

This addresses the verification gap in
[#1021](https://github.com/CultureBotAI/AntibioticMech/issues/1021).
The source remains `EVALUATING`; no inventory or observations are published.

## Scope

`scripts/audit_ncbi_ast_publication.py` rebuilds the complete corpus using the
production seeder with an explicitly supplied reviewed AST inventory. It never
copies the inventory into `data/raw/`. The default seeding path remains unchanged;
an explicitly supplied missing inventory fails instead of silently skipping it.

For every affected compound, the audit:

1. Uses the production record merge, preserving existing non-AST activities,
   unrelated record fields, and the existing curation-history prefix.
2. Writes the complete record through the closed-schema validated YAML writer.
3. Reloads that YAML and requires exact full-record equality.
4. Repeats the production merge and requires an unchanged record, including
   its activity observations and curation history.
5. Renders the production record template from the reloaded record and parses
   its activity table. All rows and all seven cells must agree in order, including
   MIC/disk qualifiers and units, assay, strain, and paired genome contexts.
6. Records output sizes, checksums, and stage timings.

Unaffected records must remain exactly unchanged after the merge. Captured input
files and existing record files are hashed before and after the run. Artifacts
are staged in a temporary directory and retained only when every check passes.
The output must be a new direct child of the ignored `reports/` directory;
existing output directories cannot be overwritten. Failures do not publish
partial results or write to the corpus or public pages.

This checks complete record serialization and record-template activity content.
It does not prove browser responsiveness, full-site navigation or deployment,
source redistribution permission, or independent biological validity. It builds
on the separate assay, taxonomic-overlap, and primary BioSample adjudication
audits; it does not replace their source-evidence checks.

## Reproduction

```bash
just audit-ncbi-ast-publication \
  --activity-report reports/ncbi_ast_assay_reviewed_2026-10-03/activity.tsv \
  --output-directory reports/ncbi_ast_publication_2026-10-03
```

The reviewed activity report has SHA-256
`9ab2302b437ae2bb5a5aeec058fd21ba4cb11e0aeab58011b50f63e3288c0a80`.
The output contains `audit.json`, validated YAML under `records/`, and rendered
record pages under `pages/`. These are evaluation artifacts, not a deployed site.
Audit-generated reseed history uses the normal writer's current event timestamp;
timings and resulting artifact hashes are evidence of a specific run.

## Full-scale canary

The largest retained AST record, tetracycline (`CHEBI:27902`), completed every
check with 17,700 AST observations and 17,720 total activity rows:

| Artifact | Existing bytes | Audited bytes |
|---|---:|---:|
| YAML | 53,908 | 52,736,294 |
| HTML | 87,590 | 11,258,342 |

On this machine the validated write took 82.544 seconds, reload/reseed took
97.424 seconds, and rendering plus cell verification took 4.737 seconds.
These are not browser timings. Other validation jobs were running concurrently,
so these measurements are not isolated performance benchmarks.

The YAML is above GitHub's documented 50 MiB warning threshold, though below
its 100 MiB hard file limit
([GitHub documentation](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)).
An 11.3 MB page with 17,720 activity rows also requires a bounded browsing
design before claiming publication readiness. The lossless storage and browsing
follow-up is [#1022](https://github.com/CultureBotAI/AntibioticMech/issues/1022).
Passing the serialization audit does not resolve that issue or the deferred
source-terms decision.

## Complete retained-data result

The full audit completed successfully in 1,673.148 seconds at code commit
`b33cf28d25c0470a15a9b0c185e48cb6a594a1ca`:

| Check | Result |
|---|---:|
| Affected exact-structure records | 32 |
| Unaffected records unchanged | 2,907 |
| AST observations and measurements | 188,759 |
| Consolidated observations retaining paired genome contexts | 52 |
| All rendered activity rows, including existing non-AST rows | 190,833 |
| Affected YAML bytes | 561,498,455 |
| Affected HTML bytes | 120,919,520 |

Every affected full record passed closed-schema writing, complete YAML reload
equality, and unchanged reseeding. Every activity cell matched the serialized
observation. Non-AST activities, unrelated fields, existing history, and all
captured input files were preserved. The retained evidence is
`reports/ncbi_ast_publication_2026-10-03/audit.json`, SHA-256
`c61d9299c7e0ff356544daeecd7f95d786a313bc03bb3904fce106c3f40ca30c`.
The report includes per-record output checksums, sizes, timings, and input hashes.

These byte counts belong to that pinned run before main's table-accessibility
wrapper changes were merged into this branch. The subsequent source-queue
status update describes these results; it is not an input to the earlier run.
Neither the full audit nor this status update adopts NCBI AST.

After merging the tested parent into commit
`2c4f3162e`, the audit/seeder/validation scripts, schema, inventories, configuration,
and corpus still match the full-run commit. Only inherited table-accessibility
templates changed. A second read-only check verified each retained YAML checksum,
loaded the same records with `yaml.CSafeLoader`, rebuilt the full record views,
and rerendered all 32 pages with the updated template. All 190,833 activity rows
and all seven cells matched again. Updated HTML totals 120,944,491 bytes;
`record.html` SHA-256 is
`caa347620f5797c773b2c0bd650a31d78e6d9d8435baf03b69fab9cf93765dbd`.
The original full audit used the production `yaml.safe_load` path, not this
faster supplemental reader. The original retained artifacts are unchanged.
Repeating the main audit command with a new output-directory name exercises
the full production path against the current templates.

## Regression checks

- 148 focused AST/publication/schema/rendering tests passed before the parent
  merge; 160 seed-harmonization/CRyPTIC/publication tests also passed. These
  suites overlap, so their counts are not additive.
- After the parent merge, all 150 focused AST/publication/schema/rendering and
  table-scrolling tests passed.
- All 2,939 existing records strictly validated and reproduced exactly; all
  existing record pages and seven class views passed render-check.
- Lint, source-queue validation, and whitespace checks passed.
- Fixtures deliberately alter rendered MICs, phenotype calls, genome links,
  dates, counts, row order, non-AST content, and input files to check refusal.
  They also cover real validated writes, source-slice replacement, curator
  preservation, unchanged reseeding, and staged-output cleanup on failure.
