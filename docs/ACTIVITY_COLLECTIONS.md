# Activity collections

An `AntibioticRecord` may store large NCBI AST observation slices in sibling
`activity-<sha256>.jsonl.gz` artifacts. This is a lossless storage format, not an
aggregation or a new resistance inference. Source adoption remains a separate
gate: this format does not authorize publishing an evaluating source.

## Read and write

```python
from pathlib import Path
from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

path = Path("data/antibiotics/antibacterial/example.yaml")
record = load_record(path)
observations = record.get("activity_spectrum", [])
# After evidence-backed curation and its curation event:
write_validated_antibiotic(record, path)
```

Always use `load_record` when reading or modifying activity-bearing records.
Plain YAML loading returns the physical manifest, not the complete observation
list. Copying the YAML alone is insufficient: retain all referenced sibling
artifacts. To move a record, load it from its original location and write the
expanded object through the validated writer at its new location.

The seeder, corpus verifier, strict schema validator, research prompt builder,
corpus reports, curation worklist, graph-quality scorer, site renderer, and
shared corpus-test fixture resolve collections. Identity-only extractors can
read the YAML manifest without expanding observations. The fleet-vendored
generic ID/label validator is unchanged; it is not an AntibioticMech QC gate
and does not resolve this repository-specific format.

## Format contract

- Consecutive NCBI AST slices with at least 500 observations and identical
  source/version/retrieval-date metadata are split into chunks of at most 500.
  Smaller slices and other sources remain inline.
- Each gzip stream contains UTF-8 JSON Lines: one exact compound-identity and
  source-provenance header, followed by complete `ActivityObservation` objects.
  Format: `antibioticmech-activity-jsonl-v1`.
- Every observation retains all evidence, taxa, isolate and genome context,
  MIC or disk units and comparators, and measurement/export counts.
- YAML references bind the artifact's SHA-256, compressed byte size, observation
  and measurement counts, source metadata, and zero-based insertion offset in
  the fully expanded observation list. Inline rows fill the remaining positions.
- Both compressed and uncompressed payloads are limited to 16 MiB per chunk.
  Paths must be regular sibling files with their content-addressed basenames.
  Missing files, symlinks, mismatched identity/provenance/counts, malformed JSON,
  non-finite numbers, duplicate JSON keys, overlapping offsets, and duplicate
  NCBI AST observation IDs fail closed.
- Closed-schema validation checks both the manifest and all expanded rows.
  Header/checksum validation alone is not scientific or schema validation.

## Refresh and cleanup

Artifacts are deterministic and immutable. The writer validates the complete
record, installs complete artifacts, then atomically replaces the YAML. A
failed record replacement leaves the previous record readable; new artifacts
may remain unreferenced until explicit cleanup.

Source refresh and record moves also leave old, unreferenced artifacts until
`just seed-apply --prune`. Pruning is full-corpus only, not allowed with partial
selection. It resolves every remaining reference before selecting deletions,
checks the content address and format of each orphan, and leaves unrelated
files alone. As with YAML pruning, do not run concurrent corpus writers.

## Publication gate

Storage is only one part of issue #1022. Before NCBI AST adoption, verify the
entire reviewed inventory through write/reload/reseed and complete rendered
activity comparisons; implement bounded browsing and complete downloads; run
desktop/mobile and full-site checks. A smaller YAML file does not by itself
make an unbounded HTML activity table usable.
