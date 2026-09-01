# Antibiotic data sources: acquisition, licensing, and quality research

Research date: 2026-08-30
Scope: sources that can add identity, structures, mechanism, targets, measured
activity, resistance, producer organisms, biosynthetic gene clusters, and
clinical status to AntibioticMech. The repository contains antibacterial,
antifungal, antiviral, antimycobacterial, antiprotozoal, biocide, and
unspecified-antimicrobial records; the recommendations distinguish true
antibiotic evidence from adjacent antimicrobial evidence.

This report extends the 2026-08-29 source audit. It uses the current source
pages, current download/API documentation, database papers, and licence pages
as the authority. It does not treat “free to read” as permission to redistribute.

## Executive conclusion

The next three useful, legally compatible acquisitions are:

1. **MIBiG reviewed entries** for producer organisms, biosynthetic gene
   clusters, and primary references. MIBiG 4.0 is available as bulk JSON under
   CC BY 4.0. The import must require reviewed/high-confidence entries and exact
   compound identity.
2. **FDA Drugs@FDA plus GSRS/UNII** for United States approval and withdrawal
   status. FDA/openFDA data is public-domain/CC0-compatible. GSRS resolves an
   ingredient name or UNII to a substance; a UNII alone must never be interpreted
   as evidence of approval.
3. **BindingDB-curated records only** for experimentally measured compound-target
   affinities, UniProt targets, and primary citations. BindingDB's own curated
   records are CC BY 4.0, while records imported from ChEMBL remain CC BY-SA 3.0
   and must be excluded.

The largest unresolved gap is measured organism-level activity. ChEMBL/CO-ADD
has the best assay context but is share-alike; EUCAST supplies clinical
interpretation thresholds rather than experiments and prohibits resale;
BV-BRC and BacDive are technically valuable but their redistribution terms have
not been verified. No one of these should be silently folded into the CC BY 4.0
record corpus.

## Current repository gaps

`uv run python scripts/antibiotic_report.py` reports 2,923 records. All have a
SMILES, Standard InChI, and Standard InChIKey, but most biological and clinical
fields remain empty.

| Record field | Records populated | Coverage | Best next source |
|---|---:|---:|---|
| `mode_of_action` | 416 | 14.2% | ChEBI roles, already adopted; literature for refinement |
| `resistance_mechanisms` | 279 | 9.5% | ARO, already adopted; Stanford HIVDB after licence approval |
| `molecular_targets` | 206 | 7.0% | BindingDB-curated subset, then primary literature |
| `producer_organisms` | 0 | 0% | MIBiG reviewed entries |
| `activity_spectrum` | 0 | 0% | BV-BRC laboratory rows if reuse is approved; otherwise curated literature |
| `clinical_status` | 0 | 0% | Drugs@FDA plus GSRS/UNII |
| `causal_graphs` | 0 | 0% | Primary literature; no database can safely author these graphs |

These numbers also define the acquisition boundary. A PDB ligand, a predicted
resistance phenotype, or a natural-product occurrence is not a substitute for
a source-backed target, measured activity, or producer claim.

## Ranked source decisions

### Priority 1 — implement after a source-specific design review

#### 1. MIBiG: producers and biosynthetic gene clusters

MIBiG is the strongest immediate source for `producer_organisms`. Its 4.0 paper
documents bulk JSON and a CC BY 4.0 licence, and recommends reviewed entries for
high-confidence applications. At manuscript preparation, 464 of 1,147 entries
contributed or modified in that release cycle had been reviewed. The bulk data
is distributed from the [MIBiG download page](https://mibig.secondarymetabolites.org/download)
and [Zenodo](https://zenodo.org/records/14169073); the database description and
quality warning are in the [MIBiG 4.0 paper](https://academic.oup.com/nar/article/53/D1/D678/7919508).

Import rule:

- accept reviewed entries only for the first release;
- require an exact structure match to a corpus record, preferably full
  InChIKey with a documented fallback for records lacking stereochemistry;
- emit one `ProducerOrganism` per source-backed taxon/BGC pair;
- preserve the BGC accession, MIBiG version, reference, and quality/review flag;
- do not turn a reported bioactivity label into an `ActivityObservation`—MIBiG
  is not a normalized MIC dataset;
- do not interpret “compound found in organism” as biosynthetic production.

#### 2. FDA Drugs@FDA and GSRS/UNII: clinical status

[Drugs@FDA data files](https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-data-files)
provide downloadable application, product, ingredient, and approval-action
tables. [openFDA's Drugs@FDA download](https://open.fda.gov/apis/drug/drugsfda/download/)
provides the same domain as complete JSON files. [GSRS/UNII](https://precision.fda.gov/uniisearch)
supplies substance identifiers and names needed to ground an approved product
ingredient to a chemical entity. openFDA states that its content is generally
public domain and offers data under CC0 unless specifically marked otherwise
in its [terms](https://open.fda.gov/terms/); the
[Orange Book files](https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files)
are a useful corroborating product/ingredient source.

Import rule:

- join application/product/ingredient tables before making a status claim;
- use GSRS/UNII as identity evidence, never as approval evidence;
- distinguish active ingredient from product, salt, ester, hydrate, and
  combination product;
- map only defensible states to the current enum: current approval to
  `APPROVED`, an explicit withdrawal to `WITHDRAWN`; retain dates and
  application identifiers in evidence/provenance;
- label the result as United States status, not worldwide status;
- exclude multi-ingredient products until the one-structure-per-record policy
  has an explicit combination-product representation.

#### 3. BindingDB-curated subset: targets and affinity evidence

BindingDB provides experimentally measured ligand-protein affinities, target
identifiers, citations, and bulk TSV/SDF releases. Crucially, the current
[BindingDB paper](https://academic.oup.com/nar/article/53/D1/D1633/7906836)
states that BindingDB-curated records are CC BY 4.0 while ChEMBL-imported
records retain ChEMBL's CC BY-SA 3.0 terms. The
[download page](https://www.bindingdb.org/rwd/bind/chemsearch/marvin/Download.jsp)
offers a BindingDB-curated-only dataset, which is the only acceptable seed
lane for this corpus.

Import rule:

- download only the explicitly BindingDB-curated article subset;
- verify the per-row source and reject ChEMBL-derived rows even if they appear
  in a broader file;
- match compounds by exact structure and retain the BindingDB ligand ID;
- require a microbial or viral target/taxon and a primary citation before
  creating a `MolecularTarget`;
- normalize UniProt accessions and represent organism-specific proteins as
  `ProteinExample`, not automatically as the taxon-agnostic target identity;
- treat affinity as evidence of binding, not automatically as inhibition,
  antimicrobial activity, or mechanism of action.

### Priority 2 — valuable after licensing or schema work

#### BV-BRC: laboratory antimicrobial-susceptibility phenotypes

BV-BRC's [AMR overview](https://www.bv-brc.org/docs/data_protocols/antimicrobial_resistance.html),
[phenotype fields](https://www.bv-brc.org/docs/quick_references/organisms_taxon/amr_phenotypes.html),
and [API schema](https://www.bv-brc.org/api/doc/genome_amr) expose organism,
strain/genome, antibiotic, R/S/I result, MIC sign/value/unit, method, testing
standard/year, and references. The same data type also contains computational
predictions. Only laboratory-derived rows are admissible; rows identified as
`Computational Method`, `Computational Prediction`, or carrying a classifier
must be excluded.

The technical fit is strong for `activity_spectrum`, but the official pages
reviewed did not provide a clear redistribution licence for the data. Request
written terms before implementation. If approved, retain strain-level identity,
measurement comparator, units, method, standard, year, and PMID. A resistant
clinical isolate is susceptibility evidence, not a statement that the compound
has no activity against the species.

#### Stanford HIVDB: antiviral resistance

The [genotype-phenotype downloads](https://hivdb.stanford.edu/download/GenoRxDatasets/)
and [release notes](https://hivdb.stanford.edu/page/release-notes/) make Stanford
HIVDB the best candidate for the 474 antiviral records that ARO cannot cover.
The data describes genotype-drug susceptibility and algorithmic interpretation,
not the same object as the current compound-centric `ResistanceMechanism`.

Two gates remain:

1. obtain explicit redistribution terms from Stanford HIVDB; and
2. design a mutation/gene-variant evidence model rather than flattening a
   genotype score into a generic resistance-mechanism label.

Its scope is primarily HIV. It does not close resistance gaps for influenza,
herpesviruses, HBV, HCV, or other antiviral classes.

#### RCSB PDB: structural evidence, not mechanism inference

The PDB archive and RCSB APIs are made available under CC0 according to the
[RCSB usage policy](https://www.rcsb.org/pages/usage-policy). PDB complexes can
support a target claim already established elsewhere and can supply a structure
accession for a compound-target complex. A bound ligand does not by itself prove
inhibition, antimicrobial action, physiological relevance, or mode of action.
PDB enrichment should follow, not precede, the schema work tracked by issue #95
and the identity checks in issue #92.

#### AMRFinderPlus: open resistance cross-check

[NCBI AMRFinderPlus](https://github.com/ncbi/amr) and its database are United
States Government Works placed in the public domain. It includes acquired AMR
genes, point mutations, and curated hierarchy. It is a useful open comparison
against ARO and can identify coverage gaps without inheriting CARD `card.json`
terms. Its primary object is a genomic determinant, however; it should not seed
a compound `ResistanceMechanism` until determinant-to-drug relationships and
evidence are represented without overclaiming. Use it first as a reference and
coverage audit.

#### LOTUS: natural-product occurrences

[LOTUS](https://lotus.nprod.net/) distributes its data through Wikidata under
CC0 and links structures, organisms, and references. It can expand natural-
product provenance after MIBiG. The semantic limitation is decisive: an
occurrence in a taxon may reflect biosynthesis, diet, symbiosis, host uptake, or
an extraction report. LOTUS rows should not populate `producer_organisms`
without a source explicitly supporting production; otherwise the schema needs
a separate occurrence field.

### Reference or sidecar only under current terms

#### ChEMBL and CO-ADD

[ChEMBL licensing](https://chembl.github.io/chembl-licensing/) is CC BY-SA 3.0.
Current [bulk downloads](https://chembl.gitbook.io/chembl-interface-documentation/downloads)
include relational and structure formats. ChEMBL is the strongest normalized
bioactivity resource reviewed and includes CO-ADD screening as source ID 40,
but share-alike is incompatible with redistributing derived record content only
under this corpus's CC BY 4.0 licence. It may be consulted by curators or stored
in a separately licensed sidecar. CO-ADD's own
[download site](https://db.co-add.org/downloads/) provides r03.02-2020 bulk CSV
files for single-concentration and dose-response screening, but the archive has
no licence file and the program site's copyright terms prohibit systematic
download/storage and reproduction without written permission. The official
bulk is therefore blocked pending a direct grant; the ChEMBL copy remains
share-alike regardless of any separate grant for CO-ADD's files.

#### DrugCentral

DrugCentral supplies structures, targets, approvals, indications, and bulk
database downloads. Its [database paper](https://academic.oup.com/nar/article/45/D1/D932/2333938)
states that the database is CC BY-SA 4.0. It is therefore useful as a validation
or curator-reference source but cannot be merged into the CC BY 4.0 record
corpus without passing on ShareAlike. FDA is the preferred first source for
machine-loaded clinical status.

#### WHO AWaRe and ATC

The [WHO AWaRe classification](https://www.who.int/publications-detail-redirect/2021-aware-classification)
covers 258 antibiotics in Access, Watch, and Reserve groups. The
[AWaRe antibiotic book](https://iris.who.int/bitstream/handle/10665/365135/WHO-MHP-HPS-EML-2022.02-eng.pdf)
is CC BY-NC-SA 3.0 IGO, which is not seed-compatible. AWaRe should be curator
reference or a separately licensed sidecar.

ATC is a different dataset and must not share AWaRe's licence conclusion merely
because both are maintained in the WHO ecosystem. Verify the current ATC/DDD
index terms separately before any extraction or redistribution.

#### ClinicalTrials.gov and the WHO antibacterial pipeline

[ClinicalTrials.gov API v2](https://clinicaltrials.gov/data-api/api) provides
daily-refreshed study records, interventions, recruitment status, phases, dates,
sponsors, and NCT identifiers. It is useful evidence that a named intervention
was studied, but it is not a regulatory database and study status is not compound
approval status. Its [terms](https://clinicaltrials.gov/about-site/terms-conditions)
require attribution, current data, display of the processing date, and disclosure
of modifications; they also warn of international and third-party copyrights.
Use trial records as cited curator evidence unless a legal review defines a safe
redistribution lane. If later automated, require a structure-grounded intervention,
an interventional drug study, an explicit phase/status, and an NCT ID; never map a
name mention or completed study directly to `INVESTIGATIONAL`.

The current [WHO antibacterial clinical-pipeline dashboard](https://www.who.int/observatories/global-observatory-on-health-research-and-development/monitoring/antibacterial-products-in-clinical-development-for-priority-pathogens/)
is a particularly useful expert-curated snapshot of antibacterial candidates,
phases, expected priority-pathogen activity, route, target, mechanism, and
innovation. The associated [2025 report](https://www.who.int/publications/i/item/9789240113091)
and data are under WHO's CC BY-NC-SA 3.0 IGO terms, so they belong in a
non-commercial/share-alike sidecar or curator workflow, not the main corpus.
They are valuable for cross-checking the narrower FDA and trial-registry views.

#### EUCAST

EUCAST publishes current clinical breakpoints in PDF and XLS; as of this review,
the [current table page](https://www.eucast.org/bacteria/clinical-breakpoints-and-interpretation/clinical-breakpoint-tables/)
lists version 16.1. EUCAST's site notice says its documents and data may be
reused with attribution but not resold. That restriction is incompatible with
the corpus's unrestricted commercial redistribution. More importantly,
breakpoints are interpretive thresholds for an organism-drug pair, not measured
MIC observations. EUCAST belongs in a standards sidecar or curator tooling,
versioned by effective date.

#### IUPHAR/BPS Guide to Pharmacology

The [download page](https://www.guidetopharmacology.org/download.jsp) provides
ligands, targets, interactions, structures, and PostgreSQL bulk data, but the
database is ODbL and contents are CC BY-SA 4.0. It is mostly human pharmacology
and is not a primary microbial-target source. Use it only as a separately
licensed reference, particularly for host-directed antivirals or the malaria
subset.

#### NPAtlas

The current [NPAtlas developer page](https://www.npatlas.org/developers)
identifies database version 2024_09 as CC BY-NC 4.0. Older papers describing a
more permissive licence do not override the current distribution terms. NPAtlas
is high-quality natural-product reference material but cannot seed this corpus.

### Do not trust as a whole-dataset licence

#### PubChem annotations

PubChem is indispensable for identity and structure resolution, but it is an
aggregator. Its [data-source documentation](https://pubchem.ncbi.nlm.nih.gov/docs/data-sources)
states that reuse conditions are defined by each contributing source, and the
[source registry](https://pubchem.ncbi.nlm.nih.gov/rest/source/) exposes those
conditions. The current narrowly scoped use—fetching structures for CIDs already
cross-referenced by CARD—is defensible. Importing PubChem annotations wholesale
and labelling them CC0 is not.

#### COCONUT

COCONUT's [about page](https://coconut.naturalproducts.net/about) describes the
curated collection as CC0, while its
[terms](https://coconut.naturalproducts.net/terms-of-service) state that original
data owners retain their rights and COCONUT imposes no additional restrictions.
Those statements do not establish that every upstream row can be redistributed
under CC0. Preserve source-level provenance and exclude any row whose upstream
licence is absent or incompatible; do not seed a full unfiltered dump.

#### Open Targets

The [Open Targets licence page](https://platform-docs.opentargets.org/licence)
marks platform outputs CC0, but the platform integrates sources with differing
terms, including ChEMBL. It primarily models human target-disease evidence and
has low direct value for microbial antibiotic mechanisms. Use only for
host-directed candidates with source-level provenance, not as a shortcut around
an upstream licence.

## Source matrix

| Source | Best data | Access | Terms found | Corpus decision |
|---|---|---|---|---|
| ChEBI | identity, structure, classes, roles | monthly bulk + API | CC BY 4.0 | adopted |
| CARD ARO ontology | resistance vocabulary and relations | monthly bulk | CC BY 4.0 | adopted |
| CARD `card.json` | sequences, mutations, detection models | bulk | restrictive McMaster terms | blocked |
| PubChem | identity/structure fallback | API + FTP | source-dependent annotations | adopted only for narrow structure fallback |
| MIBiG | producers, BGCs, references | bulk JSON | CC BY 4.0 | implement first |
| FDA Drugs@FDA | US regulatory status | bulk tables/JSON | public domain / CC0 | implement first |
| FDA GSRS/UNII | substance identity crosswalk | bulk/search | public domain | implement with Drugs@FDA |
| BindingDB-curated | targets and affinities | monthly bulk | CC BY 4.0 | implement after target rules |
| BindingDB ChEMBL rows | targets and affinities | mixed bulk | CC BY-SA 3.0 | exclude |
| BV-BRC | strain AST/MIC | API | unverified | request terms |
| Stanford HIVDB | HIV genotype-drug resistance | bulk | unverified | request terms and extend schema |
| RCSB PDB | compound-target structures | API + bulk | CC0 | structural evidence only |
| AMRFinderPlus | AMR genes/mutations | bulk | public domain | coverage audit/reference |
| LOTUS | structure-organism-reference occurrences | Wikidata/bulk | CC0 | follow MIBiG; do not infer production |
| ChEMBL/CO-ADD | assay-attached activity | ChEMBL bulk/API; CO-ADD bulk CSV | ChEMBL CC BY-SA 3.0; CO-ADD site restrictions and no archive licence | sidecar/reference only; direct CO-ADD bulk blocked pending written grant |
| DrugCentral | approval/targets/indications | bulk | CC BY-SA 4.0 | sidecar/reference only |
| WHO AWaRe | stewardship classification | document/table | CC BY-NC-SA 3.0 IGO | sidecar/reference only |
| WHO ATC/DDD | therapeutic classification | index/files | terms not verified | verify separately |
| ClinicalTrials.gov | trial interventions, phase, study status | API + bulk | attribution/currentness + international/third-party rights | curator evidence pending legal review |
| WHO antibacterial pipeline | expert-curated investigational status, activity, innovation | XLS/dashboard | CC BY-NC-SA 3.0 IGO | sidecar/reference only |
| EUCAST | clinical breakpoints | XLS/PDF | attribution + no resale | standards sidecar only |
| IUPHAR/GtoPdb | ligand-target pharmacology | bulk + API | ODbL / CC BY-SA | sidecar/reference only |
| NPAtlas | microbial natural products | API + bulk | CC BY-NC 4.0 | blocked |
| COCONUT | natural-product structures/occurrences | bulk | conflicting aggregate/upstream terms | source-filtered only |
| BacDive | strain phenotypes | registered API | terms not verified | request terms |
| EMA PMS API | selected EU product data | beta API | review required | evaluate after beta maturation |

## Cross-source quality rules

Every importer should satisfy these invariants before its data reaches a record:

1. **Identity before biology.** Match full standardized structure, not name
   alone. Record parent/salt/prodrug transformations explicitly. Reject mixtures
   and combination products until the schema represents them.
2. **One claim, one evidence trail.** Store the upstream identifier, version,
   retrieval date, primary citation, and the exact transformation that produced
   the claim.
3. **No semantic promotion.** Binding is not inhibition; inhibition is not
   organism-level activity; occurrence is not production; a breakpoint is not
   a measured MIC; a resistance prediction is not a laboratory result; ligand
   presence in PDB is not a mechanism.
4. **Preserve assay context.** MIC and activity observations need organism or
   strain, comparator, value, units, method, medium where available, testing
   standard/version, and reference.
5. **Separate measured, curated, and predicted evidence.** Predicted records
   should never pass a measured-evidence filter because they share a field name.
6. **Filter mixed-licence sources row by row.** BindingDB and PubChem demonstrate
   why a database-level name is insufficient provenance.
7. **Version mutable standards.** FDA status, EUCAST breakpoints, AWaRe, ARO,
   and MIBiG change. Store effective/version dates and make removals auditable.

## Recommended implementation sequence

1. Add source-neutral provenance slots needed by all new imports: source record
   ID, source version, retrieved date, evidence type, and jurisdiction/effective
   date for clinical status.
2. Implement a MIBiG reviewed-only dry run and publish match/rejection counts
   before writing records.
3. Implement the Drugs@FDA–GSRS identity crosswalk as a report first. Review
   salts, prodrugs, and combination products before enabling writes.
4. Implement a BindingDB-curated-only target report with strict microbial/viral
   target and primary-citation filters.
5. Send reuse-permission questions to BV-BRC, Stanford HIVDB, BacDive, and
   CO-ADD. Record the replies, scope, date, and permitted redistribution in the
   source queue.
6. If BV-BRC terms permit redistribution, build a laboratory-only AST importer.
   Otherwise curate a small, high-value spectrum set from primary literature.
7. Keep share-alike, NonCommercial, and no-resale content in separate sidecars
   with their own licences, or use them only in curator tools.

## Definition of done for a new source

A source is not adopted merely because a parser works. Adoption requires:

- authoritative licence evidence and a verification date;
- a pinned release or immutable retrieval manifest;
- a dry-run report with matched, ambiguous, rejected, and out-of-scope counts;
- regression fixtures for salts, stereochemistry, mixtures, and name collisions;
- evidence-type tests preventing prediction/threshold/occurrence promotion;
- per-record source attribution;
- corpus validation and a reproducible no-drift rebuild.

## Tracked follow-up

- [#104 — Import reviewed MIBiG producer and BGC evidence](https://github.com/CultureBotAI/AntibioticMech/issues/104)
- [#105 — Add US clinical status from Drugs@FDA and GSRS/UNII](https://github.com/CultureBotAI/AntibioticMech/issues/105)
- [#103 — Evaluate BindingDB-curated target evidence](https://github.com/CultureBotAI/AntibioticMech/issues/103)
- [#106 — Resolve reuse terms for measured antimicrobial activity sources](https://github.com/CultureBotAI/AntibioticMech/issues/106)
