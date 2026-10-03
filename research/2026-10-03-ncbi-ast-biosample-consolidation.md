# Consolidating BioSample results repeated across genome targets

This addresses [#1018](https://github.com/CultureBotAI/AntibioticMech/issues/1018).
NCBI AST remains `EVALUATING`; no public AST inventory or corpus observations
are seeded by this change.

## Source adjudication

[NCBI describes AST Browser results](https://www.ncbi.nlm.nih.gov/pathogens/docs/ast/)
as submitted phenotypes stored in BioSample records, associated with Pathogen
Detection isolates. Its [BioSample antibiogram documentation](https://www.ncbi.nlm.nih.gov/biosample/docs/antibiogram/)
describes the underlying table and measurement fields.

The reviewed AST report contains 52 identical assay/measurement signatures
repeated across two versioned targets each. A public BioSample EFetch snapshot
of all nine affected samples establishes that each signature matches exactly
one submitted antibiogram row. Every BioSample update predates the AST capture
date; later or same-day edits cannot establish the earlier row multiplicity
and are rejected. Exact organism identifiers and labels must agree as well.

| BioSample | Distinct confirmed results | Repeated export rows |
|---|---:|---:|
| SAMN02138579 | 8 | 16 |
| SAMN02142019 | 11 | 22 |
| SAMN35723872 | 4 | 8 |
| SAMN36733046 | 4 | 8 |
| SAMN36733052 | 5 | 10 |
| SAMN36733053 | 5 | 10 |
| SAMN36733054 | 5 | 10 |
| SAMN38351592 | 5 | 10 |
| SAMN38351594 | 5 | 10 |

Consolidation is not based on BioSample and drug alone. For example,
[SAMN36733053](https://www.ncbi.nlm.nih.gov/biosample/SAMN36733053) has distinct
vancomycin results: Vitek MIC 1 mg/L and ETEST MIC 2 mg/L. Both survive as
separate observations, each retaining its two genome contexts. Multiple
identical source-table rows would remain ambiguous and are refused rather
than silently reduced to one result.

All fields other than the original export-group identifier and paired genome
context must agree before consolidation. Measurement sign `==` corresponds
to the existing empty equality qualifier; source `missing` standard remains
empty. The native AST export omits the BioSample method field, so absence is
not filled by inference. A contradictory MIC/disk method in BioSample is
rejected. No phenotype, numeric value, unit, or qualifier is corrected.

## Schema and integration

`ActivityObservation.pathogen_detection_contexts` is a list of at least two
`PathogenDetectionContext` objects. Each keeps its versioned target, assembly,
BioProject, source creation date, sequencing accessions when present, and
original export-group ID together. This avoids inventing associations by
flattening independent accession lists. The corresponding singleton fields
are forbidden when paired contexts are present.

`measurement_count` is one for each confirmed submitted result;
`source_export_row_count` is two for these repeated export rows. The original
AST and isolate evidence remains, with additional BioSample snapshot and review
checksum evidence. The synthesized observation ID is derived from the captured
BioSample payload, accession, and antibiogram row number, not a selected genome.

The seeder requires the report-pinned review before consolidating any repeated
target groups. Missing decisions, altered reports, identity disagreement, and
ambiguous source results fail before corpus records are mutated. Source-owned
replacement behavior is unchanged. The page template displays each paired
context separately; existing rendered pages remain byte-for-byte reproducible.

## Full-data result

- 188,811 original export groups are accounted for exactly once.
- 188,759 observations remain after consolidating the 52 confirmed repeated
  results. The other 188,707 observations are unchanged in full.
- All 104 original genome contexts and their 18 distinct assembly accessions
  survive, with project/target/assembly/date associations intact.
- All resulting observations pass closed-schema validation. Original evidence,
  measurements, qualifiers, and biological sample fields are preserved.

Pinned evidence:

| Artifact | SHA-256 |
|---|---|
| Reviewed AST report | `9ab2302b437ae2bb5a5aeec058fd21ba4cb11e0aeab58011b50f63e3288c0a80` |
| BioSample XML | `498ba42ee6acb179edc9b64f8cefd58a85fdf680e62610271c71b63476e7b6e8` |
| BioSample manifest | `950d586c5a66fc573a61795edede62d36dee8ffd79f19c37227966529e5e3811` |
| Committed review | `05477913142c9133ad3a149079c6525764f91a645d9f889e1ad324a2482527b3` |

```bash
just review-ncbi-ast-biosamples \
  --activity-report reports/ncbi_ast_assay_reviewed_2026-10-03/activity.tsv \
  --output-directory downloads/ncbi_ast_biosamples_2026-10-03

just audit-ncbi-ast-biosamples \
  --activity-report reports/ncbi_ast_assay_reviewed_2026-10-03/activity.tsv \
  --biosample-snapshot downloads/ncbi_ast_biosamples_2026-10-03 \
  --report reports/ncbi_ast_biosample_verified_2026-10-03.json
```

The audit reconstructs every review decision from the raw BioSample XML, checks
its manifest, converts and validates every resulting observation, and verifies
full export-row coverage and paired-context preservation. It is non-publishing.
Later BioSample retrievals are different snapshots, not replacements for these
checksums. This establishes source export multiplicity, not independent
verification of the submitted phenotype or source redistribution permission.

## Validation

- 480 focused AST, schema, and record-rendering tests passed. These include
  preservation of distinct assays, MIC/disk separation, ambiguous source rows,
  post-snapshot edits, stale or malformed reviews, atomic attachment, paired
  context constraints, and preservation of all displayed genome links.
- The final full-data audit rebuilt all 52 decisions from the captured XML and
  validated every one of the 188,759 resulting observations against the closed
  schema. It accounts for all 188,811 original rows exactly once and checks
  unchanged non-repeated observations plus all paired associations and evidence.
- All 2,939 existing records strictly validate and reproduce exactly. All
  existing pages pass the render staleness check without regeneration churn.
- Schema generation, lint, source-queue validation, and whitespace checks
  passed. Full RDKit-dependent QC remains a Linux CI merge requirement.
