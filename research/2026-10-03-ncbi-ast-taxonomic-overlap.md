# NCBI AST / CRyPTIC taxonomic-scope audit

This addresses [#1017](https://github.com/CultureBotAI/AntibioticMech/issues/1017).
It extends the accession audit with an independent taxonomy retrieval, without
changing measurements, assigning new isolate identities, or adopting NCBI AST.

## Evidence and conclusion

[CRyPTIC 3.4.0](https://zenodo.org/records/15680920) describes its population as
Mycobacterium tuberculosis complex, including samples with phenotype data but
no WGS. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=77643)
identifies that complex as `NCBITaxon:77643`. This is a release-specific scope
interpretation, not an assignment of a species-level TaxID to the grouped
CRyPTIC observations.

On 2026-10-03, one public NCBI Taxonomy EFetch request returned all 434 requested
records: the 433 distinct TaxIDs in the reviewed AST report plus the complex.
The XML preserves full identifier-bearing lineages, scientific names, and
source metadata. No label matching is used to infer ancestry.

The lineage comparison places all 188,811 reviewed AST measurements outside
the complex. All 433 submitted taxon labels also agree exactly with the
retrieved scientific names. No candidate directly shares a BioSample or
BioProject with the adopted CRyPTIC phenotype slice.

The conclusion is **disjoint by reported taxonomy**, conditional on the source
TaxIDs and CRyPTIC's published scope being correct. This argument covers the
11,370 adopted phenotype IDs without WGS links as well as potential alternative
sample accessions: neither creates taxonomic overlap under those source
assertions. It does not resolve those aliases, independently re-identify any
organism, or prove within-source uniqueness. The unfiltered AST snapshot still
has 1,142 BioSamples shared with CRyPTIC; this result must not be generalized to
all AST data, unmapped drugs, or quarantined measurements.

## Reproducibility and checks

`scripts/ncbi_ast_taxonomy.py` uses the documented
[EFetch taxonomy XML interface](https://www.ncbi.nlm.nih.gov/books/NBK25499/table/chapter4.T._valid_values_of__retmode_and/).
It validates the activity report, requests exact IDs, checks response coverage
and lineage consistency, and publishes a new snapshot directory only after
validation. Existing snapshots are not overwritten. Missing or merged IDs
require review rather than silent replacement.

The manifest pins the input report checksum, request IDs, endpoint, retrieval
date, raw XML checksum, and byte count. The overlap audit checks those pins,
reconstructs the AST candidate slice and adopted CRyPTIC inventory, and compares
every report row before calculating scope. It records the taxonomy and manifest
hashes with the other audit inputs.

Scope outcomes distinguish descendants, ancestors, outside taxa, unresolved
lineages, direct sample/TaxID conflicts, and TaxID/name disagreements. Only a
nonempty, entirely outside set can receive the disjointness conclusion.
Conflicting sample identities take precedence over outside ancestry. A
legitimate scientific-name change also requires review, not an inferred
identity correction. A new CRyPTIC release requires a new scope review.

Pinned inputs:

| Artifact | SHA-256 |
|---|---|
| Reviewed activity report | `9ab2302b437ae2bb5a5aeec058fd21ba4cb11e0aeab58011b50f63e3288c0a80` |
| Taxonomy XML, 1,309,946 bytes | `0b2c5aaad4b05541aaa8282f8382ea45cf590ea289e8f43574aa790496169f26` |
| Taxonomy manifest | `fc5dcaec2c32c217c48f58bf8e61e643ee35d40b7ab33ea4e1b2f8c8f7d0e419` |
| Full reconstructed scope audit | `0afa3069f0a036b5e53f85f635fd8f0b4d0ca938c0708e44140e1a6d546ea302` |

```bash
just fetch-ncbi-ast-taxonomy \
  --activity-report reports/ncbi_ast_assay_reviewed_2026-10-03/activity.tsv \
  --output-directory downloads/ncbi_ast_taxonomy_2026-10-03

just audit-ncbi-ast-overlap \
  --ast downloads/ncbi_ast_snapshot_2026-10-03/ast.tsv \
  --activity-report reports/ncbi_ast_assay_reviewed_2026-10-03/activity.tsv \
  --isolate-snapshot downloads/ncbi_ast_isolate_snapshot_2026-10-03 \
  --wgs downloads/cryptic_3.4.0/dedupe/WGS_SAMPLES.parquet \
  --assay-review curation/ncbi_ast_assay_review.json \
  --taxonomy-snapshot downloads/ncbi_ast_taxonomy_2026-10-03 \
  --report reports/ncbi_ast_taxonomic_scope_2026-10-03.json
```

NCBI taxonomy is mutable. A later retrieval has its own checksum and must be
reviewed; it must not be presented as the captured snapshot above.

No schema change is required because this is source-adoption audit evidence,
not a new activity claim. NCBI AST remains `EVALUATING`; the deferred source-terms
decision, end-to-end publication verification, and recovery of quarantined or
unmapped evidence remain separate work. No public AST inventory is written.

## Within-source follow-up

A separate audit found nine BioSamples with two versioned Pathogen Detection
targets each. Their 104 retained rows have 52 identical BioSample, exact drug,
taxon, phenotype, measurement, method/platform/vendor/reagent, and standard
signatures across targets. This is not proof of duplicate experiments.
[#1018](https://github.com/CultureBotAI/AntibioticMech/issues/1018) tracks
adjudication against original BioSample antibiograms and assembly relationships
before adoption. Neither target is selected or excluded by this scope audit.

## Validation

- The final full-data audit rebuilt both source inventories, matched every
  retained AST row, and classified all 188,811 as outside scope. All five
  unresolved, within/ancestral, or conflicting categories contain zero rows.
- 433 focused AST tests passed, including taxonomy scope, snapshot integrity,
  missing/merged IDs, malformed or inconsistent lineages, name disagreement,
  conflicting sample identity, and prevention of partial snapshot publication.
- All 2,939 existing corpus records passed strict validation and reproduce
  exactly from committed source inventories and curator inputs.
- Lint, source-queue validation, and whitespace checks passed. Full
  RDKit-dependent QC remains a Linux CI requirement.
