# NCBI AST Inventory Containers

The exact activity report supports plain UTF-8 TSV and gzip-compressed TSV
(`.tsv.gz`). Compression changes storage only, not scientific rows, group IDs,
compound mappings, assay decisions, or paired BioSample/genome observations.
NCBI AST remains `EVALUATING`; these commands do not adopt the source.

## Checksum Contract

- `activity_report_sha256` and the assay review's `candidate_sha256` always
  hash the exact **uncompressed TSV bytes**, including quoting and line endings.
  Existing plain-report review pins are unchanged.
- File manifests' `sha256` and `bytes` describe the **stored file**. Inventory
  metadata separately records `encoding`, `content_sha256`, and `content_bytes`.
- Native AST, isolate, taxonomy XML, BioSample XML, and review JSON checksums
  continue to cover their original files. No other source's hash semantics change.
- The reader caps expanded input at 256 MiB for either format. Truncation, CRC
  failures, invalid UTF-8, malformed rows, and over-limit expansion fail closed.
  Gzip members are read to EOF and share one cumulative expanded-byte limit.

## Non-Publishing Workflow

Pack an existing validated report without reserializing its TSV:

```bash
uv run python scripts/ncbi_ast_inventory.py \
  --activity-report reports/ncbi_ast_assay_reviewed_2026-10-03/activity.tsv \
  --output-directory reports/ncbi_ast_compressed_inventory_2026-10-03
```

The command stages `activity.tsv.gz` and `inventory.json` under `reports/`,
validates the source rows, checks unchanged input and expanded output bytes,
and refuses to overwrite an existing output directory. Gzip uses no embedded
filename and a zero timestamp. Repeated packing with the same compressor is
byte-identical; logical-content hashes remain authoritative across compressors.
The manifest is evidence of packaging, not an assay or source-terms approval.

The evaluator's existing `--activity-report` output also supports `.tsv.gz`.
Use the packer when preserving already-reviewed TSV bytes: reserializing a
different quoting or newline convention would invalidate the review pin.

Exercise the compressed inventory through the full production-path audit:

```bash
uv run python scripts/audit_ncbi_ast_publication.py \
  --activity-report reports/ncbi_ast_compressed_inventory_2026-10-03/activity.tsv.gz \
  --output-directory reports/ncbi_ast_compressed_publication_2026-10-03 \
  --full-site
```

## Future Adoption

The default seeder resolves exactly one of `data/raw/ncbi_ast_activity.tsv`
and `data/raw/ncbi_ast_activity.tsv.gz`. It rejects both together instead of
choosing silently. An explicitly supplied audit report is read at that exact
path; an absent explicit path is an error.

The source-queue checker detects both representations and rejects either
before adoption. Adoption still requires the source-terms decision, configured
source, committed inventory and provenance-manifest entry, and corpus checks.
Do not commit the staged inventory or evaluated observations before that gate.
