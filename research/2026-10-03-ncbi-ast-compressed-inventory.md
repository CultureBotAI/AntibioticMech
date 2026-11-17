# NCBI AST Lossless Source Inventory

Date: 2026-10-03. Source status remains `EVALUATING`; no evaluated AST inventory
or observations were added to production. This addresses the source-inventory
size component of #1022, following the lossless collections and bounded
publication audits. It does not settle the deferred source-terms decision.

## Packaging Evidence

At code commit `28024f77f86db0ef0bc1e0281750e163d398c211`:

```bash
uv run python scripts/ncbi_ast_inventory.py \
  --activity-report reports/ncbi_ast_assay_reviewed_2026-10-03/activity.tsv \
  --output-directory reports/ncbi_ast_compressed_inventory_2026-10-03
```

| Property | Verified value |
|---|---|
| Plain TSV bytes | 103014679 |
| Gzip bytes | 7858841 |
| Source groups | 188811 |
| Plain / expanded SHA-256 | `9ab2302b437ae2bb5a5aeec058fd21ba4cb11e0aeab58011b50f63e3288c0a80` |
| Stored gzip SHA-256 | `bc795c93db8ebb0dcef967a9f1802908effd57f8acefcde2daf69a3b018fd8fd` |

The packer validates the complete source report, copies its exact bytes into a
deterministic gzip container, verifies both expanded bytes and unchanged input,
and writes `inventory.json` beside it. It never reserializes TSV values or
changes a review checksum. The storage reduction is approximately 92.37%.
Packaging manifest SHA-256:
`a148f7ccd098a6bbbdb9b80e1ffe3e251e21ba87f7969977d338aa1682197a14`.

## Complete Evidence Equivalence

A full read-only comparison loaded both representations through
`load_ncbi_ast_activity_inventory` and compared every row in order. It then
converted both through the real assay review and BioSample-consolidation path,
comparing every complete `(identifier, observation)` pair with `zip_longest`.
The comparison checked values and nested evidence, not only counts or IDs.

- All 188811 source groups were equal.
- All 188759 resulting observations across 32 exact structures were equal.
- Summed `measurement_count` stayed 188759; this is not an assertion that all
  source entries represent independent experiments.
- All 52 observations with paired genome contexts were equal.
- The pinned BioSample review was rebuilt from its captured XML and compared
  against the unchanged curated decisions using the gzip input.
- The pinned taxonomy snapshot loaded successfully against the gzip input,
  including the 433 reviewed TaxIDs and the CRyPTIC scope taxon.

The ordered complete observation-pair SHA-256 was
`33f7faef3aaf9b5d6dfccbffff2e8f2e659ea9493eba639e0c5f412d525cb169`.
Its serialization is one `json.dumps(pair, sort_keys=True, ensure_ascii=True,
separators=(',', ':'))` followed by a newline per pair, in inventory order.
This checksum excludes no observation or evidence fields.

## Review And Gates

PR #1030's adversarial review found that the raw-data provenance checker only
discovered plain TSV files. Issue #1031 records two reproduced regressions:
an unmanifested gzip inventory incorrectly passed, and a correctly manifested
one failed UTF-8 decoding. The source-queue adoption gate remained intact.

Fixed in `81839064d8594bb3de831c0838808721033ad7d3`: provenance discovery now
includes gzip TSVs, verifies stored hashes and sizes separately from required
expanded-content metadata, and counts expanded rows. Tests reject missing or
stale manifest fields, corruption, and oversized expansion. The actual full
compressed inventory passed with a valid temporary manifest and failed when
its expanded-content checksum was replaced. No production manifest was edited.

The container reader rejects malformed headers/rows, invalid UTF-8, CRC errors,
truncated streams and expanded input above 256 MiB. Multiple gzip members share
that cumulative limit. Assay and BioSample reviews reject a container hash
substituted for the required logical-content hash. The default seeder rejects
simultaneous plain and gzip inventories; source-queue checks detect both forms.

Verification after the provenance fix: 505 focused tests passed in 52.13 s,
covering inventory containers, source queue, imports, assays, BioSamples,
taxonomy, evaluator, publication, isolates, and provenance. Ruff, source-queue,
provenance and diff checks passed. All 14 documentation tests passed before
the final report/source-queue prose update; focused documentation checks were
rerun for that update.

The existing corpus's 2939 records passed closed-schema validation with no
errors and reproduced exactly with zero missing, unexpected or drifted records.
No generated production records, schemas, or pages were changed.

## Compressed Production-Path Audit

```bash
uv run python scripts/audit_ncbi_ast_publication.py \
  --activity-report reports/ncbi_ast_compressed_inventory_2026-10-03/activity.tsv.gz \
  --output-directory reports/ncbi_ast_compressed_publication_2026-10-03 \
  --full-site
```

Completed at `28024f77f86db0ef0bc1e0281750e163d398c211` in 757.775 s. All frozen
code, evidence, inventory and production-record inputs remained unchanged during
the run. The later provenance fix changes only `scripts/check_provenance.py`,
tests and documentation; the audited conversion, writer and renderer are
unchanged. Full-audit SHA-256:
`2277a60a036f7460068278fcd90b93aaf5fe278fc695bfdcee7487712bcfe649`.

- All 188759 AST observations in 32 affected records passed production merge,
  closed-schema writes, complete expanded reload equality, unchanged reseeding,
  activity-cell checks, search-index bindings and complete evidence downloads.
- All 2907 unaffected records remained unchanged.
- Affected records contain 190833 total activity rows, including other sources.
- Their storage remains 4032836 YAML bytes plus 20830594 collection bytes in
  389 files, identical to the plain-input storage audit's totals.
- The full site rendered 2939 compound records and 1970 activity pages;
  all 261075 checked local link targets resolved.

This audit does not independently re-identify isolates, verify submitted
phenotypes, or authorize redistribution. Browser interaction behavior was
tested in the preceding bounded-publication audit; this change adds no browser
code and does not claim a new browser-interaction run.

## Reproduction And Remaining Work

See [the container contract](../docs/NCBI_AST_INVENTORY.md) for commands and the
distinction between stored-file and expanded-content checksums. Linux QC and
the dependent PR merge sequence remain required before these changes land on
main.

Adoption still requires the deferred source-terms decision, source configuration,
the committed inventory and provenance-manifest entry, and the normal corpus
publication gates. Quarantined assay contexts and unmapped antibiotics are
separate curation work; compression does not admit them.
