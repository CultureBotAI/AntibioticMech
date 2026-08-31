# YAML corpus correctness and completeness audit

- **Audit date:** 2026-08-30
- **Repository commit:** `c93b3e40`
- **Scope:** every YAML file in the repository, with detailed profiling of all
  2,923 `AntibioticRecord` files under `data/antibiotics/`.

## Executive finding

The corpus is mechanically consistent and reproducible, but it is not yet
scientifically complete and should not be described as reviewed. All 2,923
records are `SEEDED`; none is `REVIEWED` under the standard in
[`CURATION.md`](CURATION.md#what-a-reviewed-record-means).

The chemical identity layer is substantially populated, but several confirmed
identity and classification defects remain. The non-chemical biology is much
less complete: producer organisms and activity observations are absent,
molecular target coverage is sparse and semantically heterogeneous, and the
schema has no usable representation of target--compound structural biology.

This audit is a full-corpus structural and semantic-pattern review. It is not a
claim that each of the 2,923 compounds received an individual primary-literature
review. Representative high-risk findings were source-checked to establish that
the automated patterns correspond to real defects.

## Audit method

The review comprised:

1. inventorying all repository YAML files and all record paths;
2. parsing with a duplicate-key-rejecting loader;
3. running the repository's complete quality gate (`just qc`);
4. profiling every record and every populated schema field;
5. comparing coverage across antimicrobial classes;
6. testing record identity, xref, list-duplication, CURIE-prefix, and
   shared-InChIKey invariants beyond the existing test suite;
7. searching every definition for producer, isolation, organismal activity,
   mechanism, mixture, and combination-product signals;
8. examining the raw ChEBI and ARO inventories and the seeding implementation;
9. source-checking representative classification, target, and PDB findings.

The formal gate passed at the audited commit:

- 2,928 YAML files parsed, with no duplicate mapping keys;
- 2,923 records passed strict closed-schema validation;
- 107 tests passed;
- corpus lock, source provenance, rendered-site synchronization, lint, and
  documentation checks passed;
- the Git worktree was clean before this report was written.

These checks establish syntax and reproducibility. They do not prove the truth
of a seeded biological assertion. The repository itself documents that
`verify-corpus` deliberately does not compare curator-owned fields and cannot
detect a fabricated claim.

## Corpus profile

### Records and identity

| Measure | Count | Coverage |
|---|---:|---:|
| Records | 2,923 | 100% |
| `SEEDED` | 2,923 | 100% |
| `REVIEWED` | 0 | 0% |
| Exact ontology grounding | 2,673 | 91.4% |
| Minted identity | 250 | 8.6% |
| ChEBI source coverage | 2,623 | 89.7% |
| ARO source coverage | 581 | 19.9% |
| ChEBI and ARO corroboration | 281 | 9.6% |

### Structure completeness

| Field | Count | Coverage |
|---|---:|---:|
| Standard InChIKey | 2,923 | 100% |
| SMILES | 2,923 | 100% |
| Standard InChI | 2,923 | 100% |
| Molecular formula | 2,916 | 99.8% |
| Monoisotopic mass | 2,916 | 99.8% |
| Structural class | 569 | 19.5% |

Seven records have an InChI but no formula or monoisotopic mass:
clindamycin, sartorypyrone D, (12Z)-10-hydroxyoctadec-12-enoic acid,
antimycin A, dehydroemetine, niclosamide, and calicheamicin gamma1I.

`structural_class` is a chemical-class field. It must not be interpreted as
structural-biology coverage.

### Biological and mechanistic coverage

| Field | Records | Coverage |
|---|---:|---:|
| Definitions | 2,789 | 95.4% |
| Molecular targets | 206 | 7.0% |
| Resistance mechanisms | 279 | 9.5% |
| Mode of action | 416 | 14.2% |
| Producer organisms | 0 | 0% |
| Biosynthesis origin | 0 | 0% |
| Activity spectrum | 0 | 0% |
| Cidality | 0 | 0% |
| Clinical status | 0 | 0% |
| Causal graphs | 0 | 0% |
| Datasets | 0 | 0% |

Coverage is uneven across activity classes. Antibacterial records account for
192 of the 206 records with targets. Antifungal, antiviral, antiprotozoal, and
biocide records are almost entirely without normalized targets.

## Confirmed correctness defects

### 1. Combination products and mixtures are represented as single chemicals

The declared corpus unit is one individual chemical structure. The repository
explicitly says that mixtures and products such as ampicillin--sulbactam are not
records. This invariant is not enforced when an upstream product concept has a
PubChem InChIKey.

The clearest example is
[`trimethoprim-sulfamethoxazole.yaml`](../data/antibiotics/antibacterial/trimethoprim-sulfamethoxazole.yaml),
whose definition calls it an antibiotic cocktail and whose SMILES contains two
disconnected components.

At least 16 records are clear product, family, or mixture concepts, including
Kaletra, tyrothricin, ticarcillin--clavulanic acid, cefepime--tazobactam,
gentamicin C/gentamicin, bleomycin, quinupristin--dalfopristin, gramicidin D,
meropenem--vaborbactam, tunicamycin, ceftazidime--avibactam, bacitracin,
piperacillin--tazobactam, and amoxicillin--clavulanic acid.

Fifty-four definitions contain mixture, cocktail, or admixture language. That
larger set is a review queue, not a claim that all 54 are invalid: some describe
an individual component's historical use in a mixture or a salt formulation.

### 2. The ARO fallback misclassifies fungal agents as antibacterial

[`triflumizole-aro-d53850fc72.yaml`](../data/antibiotics/antibacterial/triflumizole-aro-d53850fc72.yaml)
is filed as `ANTIBACTERIAL`, although its definition calls it a fungicide and
its resistance annotation concerns fungal CYP51. A separate ChEBI-grounded,
stereochemically defined triflumizole record is correctly filed as antifungal.

Phenamacril, hexaconazole, and bifonazole show the same unambiguous pattern.
Fengycin has mixed activity and needs curator adjudication rather than an
automatic reclassification.

The cause is the documented rule that an ARO-derived concept with no mapped
ChEBI activity role defaults to `ANTIBACTERIAL`. CARD includes fungal resistance
content, so ARO membership is no longer sufficient evidence for that default.

### 3. Some xrefs are not structurally equivalent identifiers

The schema and curation guide define an xref as the same chemical structure.
The corpus violates that invariant:

- [`polymyxin-b2.yaml`](../data/antibiotics/antibacterial/polymyxin-b2.yaml)
  carries `CHEBI:8309`, which identifies polymyxin B1 and has a different
  InChIKey;
- erythromycin A, lividomycin A, and mycinamicin IV contain identifiers that
  also occur as broader `parent_compounds`;
- 129 records contain a non-self ChEBI xref, but only one could be compared
  structurally from the imported inventory because the referenced terms mostly
  lack structures there;
- the seeder contains a comment recognizing the known bad cefdinir--iclaprim
  source xref, but copies source xrefs into records without a same-structure
  gate.

Three PDB accessions are also stored as chemical xrefs: `PDB:1CLY`, `PDB:1H8S`,
and `PDB:1Q3W`. PDB entries describe macromolecular structures, not equivalent
chemical identities. RCSB identifies 1H8S as an anti-ampicillin antibody
complex and 1Q3W as a human GSK3beta--alsterpaullone complex.

### 4. CURIE syntax passes while the prefix registry is incomplete

The custom `curie` type validates only the lexical shape `prefix:local`. The
corpus contains 8,806 values using 29 prefixes absent from the schema prefix
map. Frequent examples include `reaxys`, `patent`, `kegg.compound`,
`kegg.drug`, `chembl`, `knapsack`, `hmdb`, and `pdb-ccd`.

Some are naming mismatches rather than unknown databases: data use `chembl`
while the schema declares `CHEMBL.COMPOUND`, and use `kegg.compound` and
`kegg.drug` while the schema declares `KEGG`. LinkML validation therefore gives
a false impression that these identifiers are resolvable.

### 5. Exact and semantic duplicates remain inside records

- 100 records contain an exactly repeated synonym object.
- 151 contain repeated synonym text when case, type, and source are ignored.
- Lividomycin A repeats the same ARO molecular-target assertion.

The seeder deduplicates synonym strings case-sensitively before truncating the
list to 40. Case variants can therefore crowd out unique synonyms.

## Organismal-biology assessment

No record has a populated producer-organism, biosynthesis-origin, or
activity-spectrum field. This is not because the corpus lacks organismal
signals:

- 935 definitions contain phrases such as "produced by" or "isolated from";
- 284 contain activity-against language.

These are candidate queues rather than structured claims: extraction must retain
the cited source and distinguish a true producer from an isolation host,
expression host, susceptible organism, or taxonomic group named in passing.

The current model also has limitations:

- `ProducerOrganism` has a taxon and optional BGC but no explicit strain field;
- its `reference` is a scalar string rather than the shared evidence model;
- resistance mechanisms have no organism, strain, allele, or protein-accession
  context;
- causal graphs have no organism or experimental-model scope;
- activity observations represent taxon, strain, assay, and MIC, but not common
  conditions such as medium, temperature, exposure time, host infection model,
  or endpoint definition.

## Molecular-biology assessment

There are 249 target items across 206 records. Every one is inherited from ARO,
every one omits `target_type`, none has a `protein_examples` entry, and none has
a primary citation. ARO provenance is present, but it is not equivalent to
direct experimental support for the exact target relation asserted.

The most important modeling defect is that `MolecularTarget` has no relation
type. Direct binding targets, required susceptibility factors, resistance
mediators, and downstream consequences can all occupy the same list.

[`daptomycin.yaml`](../data/antibiotics/antibacterial/daptomycin.yaml) illustrates
the problem. It lists cardiolipin synthase, `rpoB`, `mprF`, and `pgsA` as
molecular targets. The imported ARO definitions describe several of these as
genes in which mutations change susceptibility, not as direct binding targets.
Primary experimental work instead supports a calcium-dependent interaction
with phosphatidylglycerol-rich membranes and downstream envelope effects.

The model should separate at least:

- direct binding target;
- attacked chemical structure or membrane component;
- required uptake or activation factor;
- susceptibility determinant;
- resistance determinant;
- downstream affected process.

Each assertion should also carry organism/strain context, experimental method,
and primary evidence where available. The existing `mode_of_action_target_scope`
is a useful warning about host-shared biology, but it is too coarse to substitute
for an identified target and contextual relation.

## Structural-biology assessment

Structural biology is effectively absent. The shared `Dataset` description
mentions structural data, but its type and repository enums have no explicit
crystallography, cryo-EM, NMR, PDB, EMDB, or AlphaFold values. No record uses the
field.

The 337 `pdb-ccd` xrefs are ligand chemical-component identifiers. They help
resolve chemical identity but do not assert that a target--compound complex was
experimentally determined.

A structural-biology observation needs, at minimum:

- PDB/EMDB accession and experimental method;
- target identifier, chain, organism, and construct;
- ligand chemical-component identifier and its mapping to the record;
- bound-site residues or region when reported;
- resolution and relevant confidence/validation values;
- biological assembly and conformational-state notes;
- primary citation and retrieval provenance.

PDB accessions currently in `xrefs` should migrate into that model.

## Other completeness findings

- 134 records lack a definition.
- All 250 minted records lack `grounding_notes`.
- Sixteen InChIKey groups contain two records. Four records in two all-minted
  collision groups have explicit curation discussions; the remaining groups are
  predominantly ChEBI distinctions such as protonation or tautomer states and
  need identity review rather than automatic merging.
- `clinical_status`, `cidality`, record-level evidence, datasets, and causal
  graphs are completely unpopulated.
- Only four records have discussions, and no record has a normalized dataset.

## Why the existing green gate did not catch these findings

The current checks are strong at closed-schema validation, deterministic
seeding, source provenance, path stability, and a small set of documented
invariants. They do not currently test:

- whether a disconnected or named combination product is one chemical;
- whether an ARO concept is antibacterial rather than fungal;
- whether an xref has the same structure as the record;
- whether a syntactically valid CURIE prefix is registered;
- whether list items are duplicated;
- whether an ARO target edge denotes direct targeting;
- whether biological fields have meaningful coverage;
- whether a PDB accession is being used as a chemical xref.

## Recommended remediation order

1. Enforce the one-structure unit and adjudicate mixture/product records.
2. Replace the ARO antibacterial fallback with source-aware classification and
   correct the confirmed fungal records.
3. Validate same-structure xrefs and move PDB accessions into structural
   evidence.
4. Introduce explicit molecular-target relation semantics and biological
   context.
5. Add a structural-biology observation model.
6. Normalize producer, biosynthetic-origin, and activity claims with evidence.
7. Enforce registered CURIE prefixes and list-level uniqueness.
8. Work through the remaining definition, formula, minted-identity, and
   collision queues before promoting records to `REVIEWED`.

## Tracking issues

The open backlog was searched by title and body before filing. The audit is
tracked through these non-duplicate issues:

| Priority | Finding | Issue |
|---|---|---|
| P0 | Mixtures and combination products violate the one-structure unit | [#90](https://github.com/CultureBotAI/AntibioticMech/issues/90) |
| P0 | ARO fallback misclassifies fungal agents as antibacterial | [#91](https://github.com/CultureBotAI/AntibioticMech/issues/91) |
| P0 | Chemical xrefs include different structures, broader terms, and PDB entries | [#92](https://github.com/CultureBotAI/AntibioticMech/issues/92) |
| P1 | Molecular targets conflate direct targets and resistance/susceptibility determinants | [#93](https://github.com/CultureBotAI/AntibioticMech/issues/93) |
| P1 | Producer, origin, activity, and resistance organismal context is absent | [#94](https://github.com/CultureBotAI/AntibioticMech/issues/94) |
| P1 | Target--compound structural biology has no data model | [#95](https://github.com/CultureBotAI/AntibioticMech/issues/95) |
| P2 | Undeclared and inconsistent CURIE prefixes pass validation | [#96](https://github.com/CultureBotAI/AntibioticMech/issues/96) |

Related pre-existing issues were retained rather than duplicated:

- [#34](https://github.com/CultureBotAI/AntibioticMech/issues/34) covers the
  converse CARD/ChEBI filing problem, where ARO evidence can be lost when a
  concept files away from antibacterial.
- [#60](https://github.com/CultureBotAI/AntibioticMech/issues/60) covers coarse
  ChEBI role-to-mechanism scope; issue #93 addresses the distinct semantics of
  individual molecular-target assertions.
- [#28](https://github.com/CultureBotAI/AntibioticMech/issues/28) already tracks
  known InChIKey identity-model limitations.

The lower-risk formula, definition, minted-grounding-note, collision, and list
duplication queues remain documented in this audit. They can be split into
implementation issues when the P0 identity fixes establish how reseeding and
curation decisions should handle them.

## External references checked

- CARD's relation model and ontology scope: [CARD 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9825576/)
- Daptomycin membrane interaction and phosphatidylglycerol dependence:
  [Muller et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC5111643/)
- PDB entry 1H8S: [RCSB PDB](https://www.rcsb.org/structure/1h8s)
- PDB entry 1Q3W: [RCSB PDB](https://www.rcsb.org/annotations/1Q3W)
- Chemical Component Dictionary scope: [wwPDB CCD](https://www.wwpdb.org/data/ccd.php)
