# CRyPTIC grouped phenotype membership

## Scope

Recover source-isolate membership for the already adopted CRyPTIC 3.4.0
phenotypes, using the same [Zenodo release](https://zenodo.org/records/15680920).
The release's `DATA_SCHEMA.pdf` identifies `UNIQUEID` on the two phenotype
tables and `WGS_SAMPLES`; the latter supplies sample, study, and run accessions.
The existing source manifest records this release under CC BY 4.0.

This is **evaluation only**, not a new inventory adoption or a corpus/schema
change. It does not access NCBI, revisit reuse terms, or resume deferred #1040.
No genotype prediction is promoted to a measured phenotype. `WGS_SAMPLES`
links identify sequencing runs, not assembled genomes or per-isolate taxa.

## Reproduction

With the frozen release files already downloaded:

```bash
just evaluate-cryptic-membership \
  --output-dir reports/cryptic_membership_2026-10-04_final
```

The command does not download anything. It verifies the published MD5 of all
four release inputs, validates the exact drug map against current chemical
identities, and requires complete field-for-field reproduction of the committed
`data/raw/cryptic_activity.tsv` before joining membership. It refuses existing
output paths and production data directories.

The output is a `report.json` and deterministic `group-membership.jsonl.gz`.
Its first line declares `EVALUATION_ONLY`, release provenance, input and
implementation SHA256 pins, and the actual DuckDB version. Each later line
contains one unchanged inventory group and its sorted members. Each member has
the source `UNIQUEID`, its measurement count within that group, and either the
paired BioSample/BioProject/run context or explicit JSON `null` for no WGS join.
The report pins the complete gzip artifact. Evaluation artifacts remain ignored
under `reports/`; no production consumer currently loads them.

## Full-Cohort Result

The checked join reproduces the current inventory, without adding or dropping
any activity group or changing its method, quality, phenotype, MIC, comparator,
units, or count:

| Quantity | Count |
|---|---:|
| Exact chemical structures | 26 |
| Adopted activity groups | 4,012 |
| Measurements | 858,402 |
| Group/source-isolate memberships | 857,940 |
| Distinct phenotype source IDs | 65,444 |
| Source IDs with a WGS join | 54,074 |
| Source IDs without a WGS join | 11,370 |
| Distinct linked BioSamples | 54,052 |
| Distinct linked BioProjects | 129 |
| Distinct linked sequencing runs | 54,074 |
| Memberships without WGS | 196,695 |
| Measurements without WGS | 196,906 |
| WGS source IDs outside the adopted phenotype slice | 491 |
| Largest group's distinct source IDs | 8,642 |

Membership totals count a source ID again when it belongs to a different assay
group. Measurement totals additionally retain repeat rows within a group.
Neither is a count of unique patients or independent experiments. Distinct
source IDs sharing a BioSample remain distinct; no automatic deduplication is
performed. Missing WGS means no join in this snapshot, not that an isolate was
never sequenced. A sequencing link does not assert genome quality or assembly
availability.

Input pins independent of the evaluator implementation:

| Input | SHA256 |
|---|---|
| `cryptic_activity.tsv` | `fa2fe5e5258328f10f9fe5724e4b74f354a98f5355bac68108ab28ffb17c7987` |
| `cryptic_drug_map.tsv` | `69643f9b5e6dfc91761a4541317de63c5dca565131f6a07a3193878d7f863a54` |
| `WGS_SAMPLES.parquet` | `b4ca79ecef0937fa0a3c304b82dcc0b45f49bd5ce404a4e6009181f4cdf62bb2` |

## Integration Boundary

The existing grouped observations must remain grouped. A subsequent integration
needs a validated, lossless membership representation that retains per-member
counts and missing links without adding hundreds of thousands of inline YAML
claims. `PathogenDetectionContext` is not that representation: it means multiple
genome targets for one measured result, not different tested source isolates.

Before adoption, require full-cohort round-trip and count checks, bounded
artifact decoding, structure/group identity checks, source-owned replacement
that preserves curator evidence, and publication/export support for membership
links. Do not infer per-isolate TaxIDs or assemblies from run accessions.
