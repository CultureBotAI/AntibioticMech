# NCBI AST adoption audit: assay context and CRyPTIC overlap

NCBI AST remains `EVALUATING`. This audit does not seed records or authorize
redistribution. It uses the AST and isolate snapshots documented in
`2026-10-03-ncbi-ast-isolate-enrichment.md`.

## Minimum assay context

Full inspection of the 233,497 enriched candidate groups found three
uninformative-only assay signatures:

| Platform | Reagent | MIC groups |
|---|---|---:|
| empty | 96-Well Plate | 3,047 |
| In-house | 96-Well Plate | 144 |
| Other | empty | 12 |

These strings identify neither a method nor a specific assay platform. Issue
[#1013](https://github.com/CultureBotAI/AntibioticMech/issues/1013) records the
bug: previously any nonempty method/platform/reagent passed. Evaluation,
report validation, and independent inventory loading now share a minimum
context gate. Known placeholders and generic vessels cannot satisfy it alone.
A meaningful alternative field still counts; for example, Sensititre plus
96-Well Plate is not excluded by this change. Raw source labels are preserved,
not rewritten into inferred methods.

The full captured-pair evaluation now yields **230,294** candidate groups,
excluding exactly those 3,203 groups. This is a minimum-context check, not
certification that the remaining submitted fields are mutually consistent.
The independent seeder loader accepted all remaining rows. Full row equality
against the previous report after applying only this filter proves every
retained measurement, qualifier, identifier, and provenance field is unchanged.
All 230,294 retain TaxIDs; 226,549 have assembly links and 202,264 have strain
labels.

## Reproduce the candidate report

```bash
just evaluate-ncbi-ast \
  --ast downloads/ncbi_ast_snapshot_2026-10-03/ast.tsv \
  --source-version ast-browser-sha256:ec6901ddfa0da41c0250875abc39b075d345c249cc39dbb17a998efaad2af184 \
  --source-retrieved-on 2026-10-03 \
  --isolate-snapshot downloads/ncbi_ast_isolate_snapshot_2026-10-03 \
  --drug-map curation/ncbi_ast_drug_map.tsv \
  --antibiotic-report reports/ncbi_ast_assay_filtered_names.tsv \
  --activity-report reports/ncbi_ast_assay_filtered_activity.tsv
```

## Reproducible overlap audit

`scripts/audit_ncbi_ast_overlap.py` verifies the published CRyPTIC 3.4.0
checksums, regenerates the exact-mapped activity inventory, and requires full
equality with the adopted inventory before using its sample membership. It
joins exact-mapped DST/UKMYC phenotype `UNIQUEID` values to
`WGS_SAMPLES.parquet`, whose published MD5 is
`ea798f4cfc28525cf394ff9196c93021`. The release file is available from the
[pinned Zenodo record](https://zenodo.org/records/15680920).

The audit also reconstructs the entire supplied AST candidate report from the
checksummed raw AST snapshot, current drug map, and verified isolate snapshot.
Stale or selectively truncated reports fail comparison. Every input receives
a SHA-256 in the audit output. The command refuses to overwrite an existing
report; use a new output path for each revision.

```bash
just audit-ncbi-ast-overlap \
  --ast downloads/ncbi_ast_snapshot_2026-10-03/ast.tsv \
  --activity-report reports/ncbi_ast_assay_filtered_activity.tsv \
  --isolate-snapshot downloads/ncbi_ast_isolate_snapshot_2026-10-03 \
  --wgs downloads/cryptic_3.4.0/dedupe/WGS_SAMPLES.parquet \
  --report reports/ncbi_ast_cryptic_overlap_2026-10-03.json
```

The output separates shared WGS sample accessions, samples represented by
adopted phenotype evidence, shared sample-and-compound pairs, and shared
projects. None automatically creates a deduplication exclusion. Different
assays on one sample may be distinct observations; project membership alone
is not sufficient to discard observations. It also counts adopted phenotype
isolates without a WGS sample link, which this accession audit cannot match.
Cross-accession aliases remain outside its scope.

### Full snapshot result

Local output SHA-256 values:

- `ncbi_ast_assay_filtered_activity.tsv`:
  `84def0c3b6b4ecb41d34bcd7945b3def05e218d68bc0e777f928c5bc2df4c7ec`
- `ncbi_ast_cryptic_overlap_2026-10-03.json`:
  `5b9b777739895d93ee6e69e6c8ed9527ce974670e86722d8c21f0a98c1907ee0`

Both reconstruction comparisons passed. The adopted CRyPTIC phenotype slice
contains 65,444 distinct `UNIQUEID` values. Of these, 54,074 have WGS mappings
to 54,052 distinct BioSample accessions and 129 projects; **11,370 have no WGS
link**. The full WGS mapping has 54,565 rows and 54,543 distinct BioSamples.

| Overlap measure | All 505,890 raw AST rows | 230,294 eligible AST groups |
|---|---:|---:|
| BioSamples shared with adopted CRyPTIC phenotype membership | 1,142 | 0 |
| Measurements on those shared BioSamples | 4,591 | 0 |
| Measurements sharing both BioSample and exact compound | 4,583 | 0 |
| Measurements sharing a represented BioProject | 4,687 | 0 |

No sample or project exclusions were generated: no current candidate has a
direct accession overlap, and the raw overlaps do not justify discarding
unrelated observations from a whole project. This result is restricted to the
captured inputs, current chemical maps, current eligibility rules, and exact
accessions. It does not resolve alternative sample accessions or the 11,370
phenotype isolates without WGS links.

## Remaining field-consistency review

[NCBI documents](https://www.ncbi.nlm.nih.gov/pathogens/docs/ast/) that it does
not validate relationships between submitted AST fields. The full assay
signature audit exposes unresolved combinations, including ciprofloxacin MICs
on BioSamples SAMN32227270 and SAMN32227269 with only `Antibiotic disk` as
informative assay context, and disk measurements associated with Vitek or
Microscan platform labels. These are review leads, not corrected data.

Issue [#1014](https://github.com/CultureBotAI/AntibioticMech/issues/1014) tracks
the necessary source-evidence adjudication or reproducible quarantine. The
audit preserves every candidate assay signature and its measurement count to
support that review. Passing a generic-placeholder filter does not close it.
Source terms and the limitations of cross-source sample matching also remain
explicit adoption gates.

## Validation

- Eight new negative regressions failed before the assay-context fix.
- 377 downloader, isolate join, evaluator, and importer tests passed afterward.
- 81 overlap, CRyPTIC, and source-queue tests passed, including the real
  parquet-reader fixture under `--extra source-ingest`.
- All 2,939 corpus records passed strict schema validation and reproduced
  exactly from their inventories, without missing, extra, or drifted records.
- Repository lint, source-queue validation, and `git diff --check` passed.
- RDKit-dependent full QC remains a Linux CI gate; the pinned wheel is
  unavailable for the local macOS x86_64 environment.
