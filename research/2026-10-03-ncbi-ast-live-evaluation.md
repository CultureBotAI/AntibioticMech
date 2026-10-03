# NCBI AST live export evaluation

The public AST Browser was downloaded on 2026-10-03 using its native TSV export
endpoint. The snapshot has 505,890 observations, 144 submitted antibiotic
labels, and 126,533,404 bytes. Both the pre-download and post-download source
counts are 505,890; all exported AST row IDs are nonblank and unique.

The exact request, retrieval timestamps, counts, and SHA-256 are recorded in
`2026-10-03-ncbi-ast-snapshot.json`. The raw export lives locally in the ignored
`downloads/ncbi_ast_snapshot_2026-10-03/ast.tsv`. The source version is
`ast-browser-sha256:ec6901ddfa0da41c0250875abc39b075d345c249cc39dbb17a998efaad2af184`.
NCBI updates the source daily. The checksum identifies the bytes received;
matching counts cannot prove that individual source rows were unchanged during
the download, and repeating the request later need not reproduce those bytes.

## Chemical identity decisions

`curation/ncbi_ast_drug_map.tsv` contains 69 decisions for this snapshot:
36 exact active-moiety mappings and 33 explicit exclusions. The other 75 labels
remain unmapped. The map is deliberately partial and the evaluator checks every
exact identifier against the current corpus's full Standard InChIKey.

These are curator interpretations of NCBI's recognized antibiotic vocabulary,
not structure identifiers provided by NCBI. Nineteen mappings use the chemical
identity already curated in the CRyPTIC crosswalk, including its racemate versus
enantiomer decisions. Seventeen additional mappings select the named ChEBI
active moiety. The interpretation does not identify the assay reagent's salt,
hydrate, manufacturer, or formulation. For example, ofloxacin maps to the
racemate while levofloxacin maps to its specified stereoisomer; gentamicin,
kanamycin, colistin, and component-unspecified complexes remain mixtures.
Combination measurements cannot attach to either individual component.

Evidence consulted:

- [NCBI AST documentation](https://www.ncbi.nlm.nih.gov/pathogens/docs/ast/)
  describes submitter-provided phenotypes, units, and the downloadable table.
- [NCBI BioSample antibiogram vocabulary](https://www.ncbi.nlm.nih.gov/biosample/docs/antibiogram/)
  supplies the recognized drug names, combination flags, and measurement fields.
- The corpus ChEBI structures and `curation/cryptic_drug_map.tsv` supply the
  selected chemical identities; mapping notes preserve the curation basis.

## Reproduction

Download a canary before requesting all rows. These commands refuse to replace
an existing snapshot directory and publish a new directory only after header,
row-shape, unique-ID, and row-count checks succeed:

```bash
just fetch-ncbi-ast --query biosample_acc:SAMN04622941 --output-dir downloads/ncbi_ast_canary_2026-10-03
just fetch-ncbi-ast --output-dir downloads/ncbi_ast_snapshot_2026-10-03
```

For the captured bytes, the exact-map evaluation is:

```bash
just evaluate-ncbi-ast \
  --ast downloads/ncbi_ast_snapshot_2026-10-03/ast.tsv \
  --source-version ast-browser-sha256:ec6901ddfa0da41c0250875abc39b075d345c249cc39dbb17a998efaad2af184 \
  --source-retrieved-on 2026-10-03 \
  --drug-map curation/ncbi_ast_drug_map.tsv \
  --antibiotic-report reports/ncbi_ast_exact_names.tsv \
  --activity-report reports/ncbi_ast_exact_activity.tsv \
  --project-dedupe-report reports/ncbi_ast_project_dedupe.tsv
```

A fresh download needs its own checksum/version and a re-audited drug map.
The native TSV keeps measurement signs, MIC in mg/L, and disk diffusion in mm.
The evaluator keeps those measurement types separate and preserves the source
phenotype, assay platform/reagent, and sample/project context.

## Adoption Work

NCBI AST remains `EVALUATING`. These local reports do not activate the seeder or
publish source observations in the CC BY 4.0 corpus. Before adoption:

1. Resolve BioSample/BioProject overlap with CRyPTIC and other adopted sources.
2. Join the Isolates Browser on exact `target_acc` to retain TaxIDs, assemblies,
   strain names, and sequencing accessions, checking source identity agreement.
   The native AST export carries organism labels and PDT accessions; those must
   not be mislabeled as taxonomy or genome identifiers.
3. Review assay and submitted-field consistency. NCBI explicitly does not
   verify the biological relationships among submitted fields.
4. Finish the deferred source-terms decision before committing an adopted
   `data/raw/ncbi_ast_activity.tsv` inventory.

The first live evaluation also motivated a performance change: cached matching
headers retain alias priority and read current cell values while avoiding
repeated regular-expression work. On the same first 100 native export rows,
evaluation fell from 2.219 seconds to 0.036 seconds locally. Safe C YAML loading
is used when available for the corpus identity lookup.
