# Source ingestion sequence: CRyPTIC, PHI-base, AMRFinderPlus, NCBI AST, RCSB PDB

Date: 2026-09-01

Scope: execute the requested source sequence without contacting maintainers or
creating external issues. All network activity was read-only retrieval from
public source endpoints.

## Outcome

- PHI-base is adopted and seeded: 217 resistance associations on 23 exact
  ChEBI-grounded corpus structures.
- CRyPTIC remains `EVALUATING`: its measurements are valuable, but release
  3.4.0 supplies drug names/codes rather than structures or stable chemical
  identifiers, so zero observations pass the structure-identity gate.
- AMRFinderPlus remains a reference audit: it adds family/class coverage but
  cannot support structure-specific resistance claims without another mapping
  and evidence layer.
- NCBI AST is not seeded because its antibiotic field is not a structure
  identifier, submitted cross-field relationships are not verified, and
  cross-project deduplication remains unresolved. License resolution is
  explicitly deferred to a later pass and is not used as the technical gate.
- RCSB PDB remains `EVALUATING`: exact ligand plus established UniProt overlap
  produces 42 candidate entries on 8 records, but entry co-occurrence is not an
  atom-level ligand--protein contact assertion.

## 1. CRyPTIC 3.4.0 dry run

Source: [Zenodo record 15680920](https://zenodo.org/records/15680920), DOI
`10.5281/zenodo.15680920`, CC BY 4.0, published 2025-05-21.

Pinned files and upstream MD5 checksums:

| File | MD5 |
|---|---|
| `DRUG_CODES.csv.gz` | `923d3a193df21698bd6a00f857ab337e` |
| `DST_MEASUREMENTS.parquet` | `45b4501ea7c3925af565dbbc6188dec0` |
| `UKMYC_PHENOTYPES.parquet` | `020b6c0af6c05e19610a59f5ef97b832` |

Dry-run result:

| Table | Rows | Isolates | Drugs | Usable phenotype/measurement rows |
|---|---:|---:|---:|---:|
| DST | 660,961 | 65,816 | 30 | 617,072 S/R/I; 226,994 high-quality |
| UKMYC | 288,904 | 21,685 | 14 | 285,757 MIC; 278,875 S/R/I |

Twenty-nine drug names have at least one lexical corpus candidate. They are not
identity evidence. The dry run exposes concrete collisions: `CYC` cycloserine
has two corpus candidates, imipenem has two, and ofloxacin has three (including
levofloxacin). Attaching by name would violate the one-structure-per-record
contract. `scripts/evaluate_cryptic_activity.py` therefore reports zero eligible
observations and never writes an inventory.

Required unblocking evidence: a versioned CRyPTIC drug-code crosswalk carrying
an exact structure identifier or Standard InChIKey, including an explicit rule
for combinations, salts, stereoisomers and assay reagent forms.

## 2. PHI-base AMR adoption

Sources:

- [PHI-base data repository](https://github.com/PHI-base/data), CC BY 4.0,
  pinned commit `62e6a87a49397cba6ceb211b254d7ac8e5d09ff8`.
- `ensembl/phibase_amr_export.csv` at that commit.
- PHIPO vocabulary from pipeline commit
  `bdaf084c971366084badabee96bd65da2ee84ae9`.

The extractor requires all of:

1. `antimicrobial_interaction`;
2. a PHIPO label beginning `resistance to`;
3. numeric primary PMID;
4. pathogen NCBI Taxonomy identifier;
5. source ChEBI identifier present in the corpus;
6. source chemical label agreeing with the corpus label;
7. the committed inventory InChIKey still agreeing with the seeded record.

From 271 source rows, 217 rows on 23 records pass. Rejections are 22
out-of-scope ChEBI identifiers, 12 non-resistance phenotypes, 14 missing
pathogen taxonomy identifiers, and 6 upstream rows that identify the chemical
as fenhexamid while assigning `CHEBI:9242` (spiroxamine).

Every seeded assertion retains PHIG identifier, protein accession, pathogen,
strain, exact alteration, PHIPO phenotype, evidence code, source commit/date
and PMID. `mechanism_type` is deliberately `UNKNOWN`: the curated phenotype
supports a gene-alteration/chemical resistance association, not a specific
biochemical route.

## 3. AMRFinderPlus audit

Source: [NCBI AMRFinderPlus](https://github.com/ncbi/amr), public-domain notice;
database version `2026-08-07.1`.

Inputs:

- `ReferenceGeneCatalog.txt`, SHA-256
  `fa41ade01712841e639c91163243bace1c34755b927e69e0c8678540268a7fd4`;
- `fam.tsv`, SHA-256
  `00323cb11e1a5195c636b9d7d54d925e8274518300f3b6188ec87edc016b4487`;
- committed `aro_resistance_edges.tsv`.

Results:

- ARO slice: 4,555 edges, 2,010 determinants, 285 antibiotic identifiers.
- AMRFinderPlus: 1,457 reportable AMR families; 8,493 AMR catalog rows in
  1,147 families; 3,492 rows carry a PMID.
- Exact normalized node/symbol/family-name overlap: 494 AMRFinderPlus families.
  The 963 unmatched names are a lexical audit backlog, not proof of novel
  biology.
- The catalog has 87 slash-separated subclass tokens; only 49 exactly match an
  ARO antibiotic name.

No rows are seeded. A family attached to a category such as `BETA-LACTAM` does
not prove resistance to every structure filed under that category, and an
ungrounded drug-name token cannot identify a corpus structure.

## 4. NCBI Pathogen Detection AST technical and provenance audit

Sources:

- [AST Browser documentation](https://www.ncbi.nlm.nih.gov/pathogens/docs/ast/)
- [NCBI data usage policy](https://www.ncbi.nlm.nih.gov/home/about/policies/)
- [AST at Google Cloud](https://www.ncbi.nlm.nih.gov/pathogens/docs/ast_gcp/)

The AST Browser offers downloadable, submitter-provided phenotypic observations
with BioSample, organism, antibiotic, S/R phenotype, MIC or disk measurement,
measurement sign, platform, reagent, testing standard and BioProject. NCBI says
it does not verify relationships between submitted fields. Its general policy
places no NCBI restriction on molecular data, but also says rights are not
transferred from submitters and NCBI cannot transfer them to third parties.
The BigQuery route is an alpha release and its documentation asks users to make
contact before production use.

Disposition: no corpus import. Per project direction, license resolution is
deferred and is not treated as the blocker in this pass. The remaining
technical gates are structure-grounded antibiotic identity, validation of the
submitted field relationships needed for a claim, and deduplication of
BioSample/BioProject rows already present in CRyPTIC or other project datasets.
No contact was made.

## 5. RCSB PDB candidate audit

Sources:

- [RCSB usage policy](https://www.rcsb.org/pages/usage-policy), CC0 for archive
  files and API data.
- [RCSB Search and Data APIs](https://www.rcsb.org/docs/programmatic-access/web-apis-overview).

The evaluator starts only from the 95 BindingDB target assertions that already
carry UniProt examples, spanning 45 compounds. Each query requires both the
record's exact Standard InChIKey and one of those established UniProt
accessions. It finds 42 unique candidate entries, 243 raw target-label/entry
pairs and 8 records. The raw pair count is inflated by BindingDB variant-specific
target labels sharing the same protein accession.

No PDB evidence is seeded. The current query proves exact ligand and matching
protein coexist in an entry, but not that the specific ligand component contacts
the matching polymer entity. Adoption requires component-to-chain contact
validation, stable target deduplication, and a primary citation where available.

## Reproduction commands

```bash
just evaluate-cryptic --dst DST_MEASUREMENTS.parquet \
  --ukmyc UKMYC_PHENOTYPES.parquet --drug-codes DRUG_CODES.csv.gz
just extract-phibase-dry --amr phibase_amr_export.csv --phenotypes phipo.csv
just evaluate-amrfinder --catalog ReferenceGeneCatalog.txt --families fam.tsv \
  --aro data/raw/aro_resistance_edges.tsv
just evaluate-rcsb-pdb
```
