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
