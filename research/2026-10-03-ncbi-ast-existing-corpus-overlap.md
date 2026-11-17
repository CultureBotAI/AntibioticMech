# NCBI AST overlap with existing corpus observations

Date: 2026-10-03

The CRyPTIC accession/taxonomy audit is necessary but does not cover every
existing activity observation. The corpus also contains BioSample-linked
curator evidence, including CDC/FDA AR Isolate Bank citations. Issue #1035
tracks the missing reproducible comparison before further AST coverage work.
NCBI AST remains `EVALUATING`; no drug map, review decision, production record
or source inventory is changed here.

## Audit contract

`scripts/audit_ncbi_ast_overlap.py` now also reads the existing corpus, resolving
activity collections before inspecting observations. It excludes `NCBI_AST`
rows from this cross-source comparison so a later source refresh cannot match
itself. It retains evidence whose `source` field is absent without assigning a
source enum. Top-level and nested BioSample/BioProject contexts are included;
repeated references to the same sample within one observation count once.

The new `existing_corpus` report section distinguishes shared samples, shared
projects and exact sample/compound matches. The latter requires both the
mapped record identifier and full Standard InChIKey. Even an unmapped raw drug
can produce a shared-sample review lead without becoming a chemical match.
Leads retain source drug names, existing record paths, one-based observation
numbers, source observation IDs when present, and the existing citations.

The audit pins all record YAML, collection artifacts and the path lockfile,
checks them again after reading, and rejects changed, added or removed inputs
before accepting the comparison. Empty corpora, invalid accessions and corrupt
collections fail closed. Counts refer to observations or AST export rows, not
independently verified unique experimental measurements. No lead automatically
excludes an observation, a drug or a whole project.

## Full snapshot result

The existing-corpus comparison ran alongside the complete CRyPTIC/AST
reconstruction and pinned taxonomy audit on the expanded reviewed inventory.
The report is an ignored evaluation artifact:

- Report: `reports/ncbi_ast_existing_corpus_overlap_2026-10-03.json`
- Report SHA-256: `bbc1f48c55ebbf81fcec77828d1fbc88a8ef8e911b2ac1b258c71b564f13ee3c`
- Audit script SHA-256: `0fdbca832172ec232e0c3832e420a23a88f82bd07d080db027b82b067d59daa9`
- Reviewed report logical SHA-256: `bcac2fb84c9f7df5d78fab90f330738e31dcdb7b82bc3dfc7069a351edacc41a`
- Compressed report SHA-256: `4f396c7843750066afb8225832ac6023305779a4bcd037940de8ff8d0149b4f2`

| Existing corpus quantity | Count |
|---|---:|
| Records examined | 2,939 |
| Pinned corpus files | 2,940 |
| Non-AST activity observations | 4,490 |
| Observations with BioSample accessions | 431 |
| Distinct BioSamples | 77 |
| Observations without BioSample accessions | 4,059 |
| Explicit BioProjects on these observations | 0 |
| Existing AST observations excluded | 0 |

| Comparison against existing corpus evidence | Raw AST export | Reviewed AST groups |
|---|---:|---:|
| Rows examined | 505,890 | 213,144 |
| Rows sharing a BioSample | 1,013 | 0 |
| Distinct shared BioSamples | 48 | 0 |
| Rows sharing exact sample and compound | 304 | 0 |
| Rows sharing an explicit BioProject | 0 | 0 |

The raw overlaps are review leads outside the currently accepted cohort, not
proof of duplicate assays. Zero project overlap is uninformative here because
the existing observations supply no project accessions. The separate CRyPTIC
reconstruction still finds zero reviewed sample/project overlaps and the same
conditional `DISJOINT_BY_REPORTED_TAXONOMY` result for the reviewed cohort.

The coverage preflight that prompted this change found eight raw minocycline
rows whose samples already have curated minocycline observations:
`SAMN04901687`, `SAMN11953783`, `SAMN34111336`, `SAMN34111338`, `SAMN34111339`,
`SAMN34111340`, `SAMN34111348` and `SAMN34111349`. Minocycline is not yet mapped
in the AST crosswalk; the audit therefore reports sample leads, not exact
minocycline chemical matches. The source assay and provenance must be reviewed
before any future coverage change admits these as independent observations.
Matching names, accessions or MIC values alone is insufficient.

## Reproduction

The corpus defaults to `data/antibiotics`; `--corpus-directory` permits an
explicit staged corpus. Its actual paths and checksums remain in the report.
Use a new output filename for each run; existing reports cannot be overwritten.

```bash
.venv/bin/python3 scripts/audit_ncbi_ast_overlap.py \
  --ast downloads/ncbi_ast_snapshot_2026-10-03/ast.tsv \
  --activity-report reports/ncbi_ast_drug_expanded_compressed_2026-10-03/activity.tsv.gz \
  --isolate-snapshot downloads/ncbi_ast_isolate_snapshot_2026-10-03 \
  --wgs downloads/cryptic_3.4.0/dedupe/WGS_SAMPLES.parquet \
  --assay-review curation/ncbi_ast_assay_review.json \
  --taxonomy-snapshot downloads/ncbi_ast_drug_expanded_taxonomy_2026-10-03 \
  --report reports/ncbi_ast_existing_corpus_overlap_2026-10-03.json
```

All 73 focused overlap, taxonomy, inventory and source-queue tests pass,
including collection-backed reads, missing source enums, nested contexts,
unmapped names, chemical-key mismatch, project-only overlap, empty corpora and
changed input pins. All 2,939 production records strictly validate. Lint,
source-queue validation and whitespace checks pass. Full Linux QC is still
required on the final PR head.

## Limits

This comparison cannot match different BioSample aliases or observations with
no BioSample links. CRyPTIC's separate WGS/taxonomy analysis covers its grouped
phenotypes under its stated assumptions; it must not be replaced by the
record-level missing-accession count. Other accession-free evidence remains
outside this exact-accession comparison. This does not establish global assay
independence, resolve quarantined source contexts or authorize source adoption.
