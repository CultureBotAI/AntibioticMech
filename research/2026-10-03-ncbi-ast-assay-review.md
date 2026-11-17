# NCBI AST assay-context adjudication

This addresses [#1014](https://github.com/CultureBotAI/AntibioticMech/issues/1014)
by separating accepted source context from unresolved context before seeding.
NCBI AST remains `EVALUATING`; no public inventory or corpus record is added.

## Decisions and scope

`curation/ncbi_ast_assay_review.json` pins the AST snapshot, candidate-report
SHA-256, review date, and all 60 observed combinations of method, platform,
vendor, reagent, and measurement kind. Matching is exact, including case and
vendor spelling. A new context or source version fails closed instead of
inheriting approval from a vaguely similar platform name.

The table accepts 48 contexts and quarantines 12. Acceptance means only that
the submitted assay context is compatible with the measurement type. It does
not independently verify the numeric result, instrument calibration, clinical
breakpoint, or a particular panel's drug menu. Original labels, qualifiers,
units, calls, isolate identifiers, and observation IDs remain unchanged.

Primary sources used for adjudication:

- [VITEK 2 manufacturer documentation](https://www.biomerieux.com/us/en/our-offer/clinical-products/vitek-2.html)
  identifies MIC results and a 64-microwell card format.
- [Phoenix manufacturer documentation](https://www.bd.com/en-ca/products-and-solutions/products/product-families/bd-phoenix-panels)
  identifies MIC results; [FDA's device summary](https://www.accessdata.fda.gov/cdrh_docs/pdf12/K123266.pdf)
  describes its 136-well panel. The submitted 96-Well Plate combinations are
  quarantined, not silently rewritten or declared experimentally false.
- [MicroScan manufacturer specifications](https://media.beckmancoulter.com/en/products/microbiology/microscan-walkaway-plus-system)
  describe MIC panels with 96 wells; the manufacturer's
  [acquisition announcement](https://www.beckmancoulter.com/en/about-beckman-coulter/newsroom/press-releases/2014/siemens-healthcare-diagnostics-microbiology-acquisition)
  supports Siemens as a historical vendor rather than a vendor conflict.
- [Sensititre resources](https://www.thermofisher.com/us/en/home/clinical/clinical-microbiology/antimicrobial-susceptibility-testing/resources.html)
  and the [TREK catalog](https://www.trekds.com/pdf/TRK_catalog.pdf) support the
  named platform family. The curator explicitly interprets `Sensititer` as a
  spelling variant in this snapshot; it is retained verbatim in observations.
- [ETEST documentation](https://www.biomerieux.com/corp/en/our-offer/clinical-products/etest.html)
  distinguishes gradient MIC strips from disk diameters and describes ETEST
  as complementary to automated testing. Mixed platform/reagent entries are
  therefore unresolved, not proof of impossible experiments.
- [Scan 500 documentation](https://www.interscience.com/en/products/inhibition-zone-readers/scan-500?lang=en)
  supports the source's explicit disk-diffusion context.
- [NCBI AST documentation](https://www.ncbi.nlm.nih.gov/pathogens/docs/ast/)
  supplies the source-field semantics and warns that cross-field relationships
  are not verified by NCBI.

Generic `GM-NEG` reagent labels are retained as submitted, not promoted to a
specific verified card or panel identity. Missing vendors are not invented.
`KB panel` remains quarantined until its abbreviation is established from
submitter evidence. Quarantine is reversible curation, not deletion from the
captured source or an assertion that the reported phenotype is false.

## Full snapshot result

| Disposition | Groups |
|---|---:|
| Input after minimum-context filtering | 230,294 |
| Accepted | 188,811 |
| Quarantined | 41,483 |
| Panel-format conflicts | 40,110 |
| Mixed automated-platform/ETEST context | 609 |
| MIC/disk measurement-context conflicts | 520 |
| Unexpanded KB abbreviation | 184 |
| Vitek/Trek vendor conflict | 60 |

The quarantine categories sum to 41,483; the retained data contain 188,483 MIC
groups and 328 disk-diffusion groups. No MIC is converted into a diameter or
vice versa. Both susceptible and resistant observations remain eligible under
the same context rules; this is not selection on the biological outcome.

Review version:
`assay-review-sha256:3d241224219dee555ac403e94547f9cb7ae2307fc73d6a8bfd83272cc5047b0b`.
Reviewed activity TSV SHA-256:
`9ab2302b437ae2bb5a5aeec058fd21ba4cb11e0aeab58011b50f63e3288c0a80`.

## Integration contract

`just review-ncbi-ast` validates the full candidate report and its pinned hash,
applies every explicit decision, and produces a reviewed activity TSV plus a
decision/count/hash manifest. Existing output directories are refused.

The seeder's attachment path requires the canonical review map, rejects any
quarantined or unreviewed row, and records the review checksum, date, rationale,
and source references as additional observation evidence. Review never changes
the AST phenotype source version or replaces the separate isolate-identity
provenance. No schema extension is needed: the existing evidence list carries
this curation decision. Candidate report loading remains available for audits;
loading alone does not authorize publication.

```bash
just review-ncbi-ast \
  --activity-report reports/ncbi_ast_assay_filtered_activity.tsv \
  --output-directory reports/ncbi_ast_assay_reviewed_2026-10-03

just audit-ncbi-ast-overlap \
  --ast downloads/ncbi_ast_snapshot_2026-10-03/ast.tsv \
  --activity-report reports/ncbi_ast_assay_reviewed_2026-10-03/activity.tsv \
  --isolate-snapshot downloads/ncbi_ast_isolate_snapshot_2026-10-03 \
  --wgs downloads/cryptic_3.4.0/dedupe/WGS_SAMPLES.parquet \
  --assay-review curation/ncbi_ast_assay_review.json \
  --report reports/ncbi_ast_reviewed_overlap_2026-10-03.json
```

The overlap audit regenerates the exact candidate report from both source
snapshots, applies the same review decisions, then compares every reviewed row.
It does not mistake the deliberate quarantine for missing source observations.
The source-terms decision, remaining cross-accession deduplication limits, and
unmapped antibiotic identities remain separate work; this review does not
declare source adoption complete.

## Validation

- Full equality against the pre-review candidate confirms that all 188,811
  retained rows are unchanged, including observation IDs and all measurements.
- The independent seeder loader accepted every reviewed row. All 188,811
  converted observations passed closed-schema validation with the additional
  review evidence. All have TaxIDs; 185,295 have assembly links and 172,310
  have strain labels.
- Full AST/CRyPTIC reconstruction and overlap audit passed after applying the
  review. No accepted observation has a direct shared BioSample or BioProject;
  the previously documented accession-alias and phenotype-only limits remain.
- 407 focused AST tests passed after merging current main, including all 21
  assay-review tests. Unrecognized contexts, stale versions, duplicate JSON
  keys, malformed decisions, quarantine, partial attachment, changed candidate
  files, and output overwrite refusal are tested.
- All 2,939 existing corpus records reproduce exactly, without missing, extra,
  or drifted records.
- Lint, source-queue validation, and diff whitespace checks passed. Full
  RDKit-dependent QC remains a Linux CI gate.
