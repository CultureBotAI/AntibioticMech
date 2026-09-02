# AntibioticMech

Knowledge base of **individual chemical structures with antimicrobial activity**,
harmonized from ChEBI and CARD's Antibiotic Resistance Ontology, grounded in
chemistry, and built to carry the *mechanism* — what the compound hits, how
microbes resist it, and the evidence for both.

AntibioticMech is the antimicrobial-compound counterpart of
[TraitMech](https://github.com/CultureBotAI/TraitMech) (traits),
[CultureMech](https://github.com/CultureBotAI/CultureMech) (growth media),
[MediaIngredientMech](https://github.com/CultureBotAI/MediaIngredientMech)
(ingredients), [HabitatMech](https://github.com/CultureBotAI/HabitatMech)
(habitats) and [CommunityMech](https://github.com/CultureBotAI/CommunityMech)
(communities), and follows the curation pattern established by
[dismech](https://github.com/monarch-initiative/dismech): one YAML per entity,
ontology-grounded, evidence-backed, schema-validated, curated incrementally.

**[Browse the corpus online →](https://culturebotai.github.io/AntibioticMech/)**
— every record, browsable by antimicrobial class, with structures, sources,
CARD targets and resistance determinants.

## One record is one chemical structure

That constraint is the design. "Macrolide antibiotic" is not a record — it is a
`structural_class` on the records it covers. Erythromycin A is a record, keyed
by `CHEBI:42355`, carrying its SMILES, InChI and InChIKey.

A record with no InChIKey is never written. Without a structure there is nothing
to assert identity on, and a name is not a structure: `antibiotic mixture`,
`ampicillin-sulbactam` and `aminonucleoside antibiotic` are all real upstream
concepts and none of them is one compound. They go to the curation worklist
instead of quietly becoming records.

## The problem it solves

Each source names and scopes antimicrobials differently:

| Source | How it describes erythromycin |
|---|---|
| ChEBI | `CHEBI:48923` "erythromycin" — a *class*, with no structure of its own |
| ChEBI | `CHEBI:42355` "erythromycin A" — the structure, with SMILES/InChI |
| CARD/ARO | `ARO:0000006` "erythromycin" — a macrolide, with 110 resistance determinants and a ribosomal target |
| PubChem | CID 12560 — the structure CARD's cross-reference actually points at |

Those become *source concepts*. Each resolves to an identifier — a ChEBI CURIE
where the entry has a structure, otherwise a minted, content-hashed
`antibioticmech:` CURIE — and concepts resolving to the same structure merge
into one `AntibioticRecord` carrying all their attestations.

That merge is the product.
`data/antibiotics/antibacterial/erythromycin-a.yaml` is one record grounded in
`CHEBI:42355` that keeps ChEBI's structure and definition, CARD's macrolide
classification, CARD's 110 resistance determinants, and the trail showing how a
class-level ChEBI term and an ARO molecule ended up in the same place.

## Current corpus

<!-- BEGIN GENERATED CORPUS STATS -->

| Class | Records | SEEDED | REVIEWED | With resistance evidence |
|---|---:|---:|---:|---:|
| ANTIBACTERIAL *(incl. subclasses)* | 1093 | 1093 | 0 | 279 |
| &nbsp;&nbsp;↳ ANTIMYCOBACTERIAL *(subclass of ANTIBACTERIAL)* | 78 | 78 | 0 | 15 |
| ANTIFUNGAL | 594 | 594 | 0 | 55 |
| ANTIPROTOZOAL | 248 | 248 | 0 | 5 |
| ANTIVIRAL | 473 | 473 | 0 | 21 |
| BIOCIDE | 31 | 31 | 0 | 3 |
| ANTIMICROBIAL_UNSPECIFIED | 472 | 472 | 0 | 3 |
| **TOTAL** | **2911** | **2911** | **0** | **366** |

A row marked *(subclass of X)* is already counted in X's own row — mycobacteria are bacteria, and filing is exclusive, so a compound filed ANTIMYCOBACTERIAL is not filed ANTIBACTERIAL as well. TOTAL counts each record once, so the Records column does not sum to it.

Identity: **2671** records (92%) are grounded in a ChEBI term; **240** keep a minted `antibioticmech:` CURIE because no ChEBI entry with a structure covers them.

Corroboration: **281** records carry source concepts from both ChEBI and CARD/ARO; **2341** come from ChEBI alone and **289** from CARD alone.

Mechanism layer: **246** records carry a molecular target and **282** carry resistance determinants or associations seeded from CARD and PHI-base; **416** carry a mode of action seeded from ChEBI's mechanism roles; **0** carry a curated causal graph. That last number is the work.

<!-- END GENERATED CORPUS STATS -->

## Quick start

```bash
just install                       # uv sync --extra dev
just seed                          # dry run: what would be written, per class
just seed-canary CHEBI:42355       # write exactly one record and validate it
just seed-apply                    # write the corpus
just qc                            # every local and CI quality gate
just report                        # corpus, grounding and curation statistics
just worklist                      # what curation owes, ranked
just chemical-map                 # regenerate the structure-only map + site
just chemical-map-check           # verify the committed map without writing
```

Nothing above touches the network. The inventories in `data/raw/` are committed,
so seeding, validation, rendering and the whole test suite run offline.

## Chemical structure map

The generated site includes a
**[Chemical structure map](https://culturebotai.github.io/AntibioticMech/pages/chemical-map.html)**
covering all 2,911 records. Its coordinates and nearest neighbors use only the
exact stored chemical structure:

```text
distance = 0.90 × (1 - Tanimoto(chiral Morgan count radius 2))
         + 0.10 × (1 - Tanimoto(chiral Morgan count radius 4))
```

UMAP projects the complete precomputed distance matrix with
`n_neighbors=15`, `min_dist=0.05`, and `random_state=42`. Labels,
antimicrobial classes, mechanisms, targets, and curation metadata can filter or
color the view but never affect fingerprints, distance, neighbors, or position.
Local neighborhoods are the meaningful part of the projection; axes and
map-wide spacing are not quantitative chemical distances.

The build parses stored SMILES first and falls back to the record's standard
InChI when required. It preserves charge, stereochemistry, counterions, and
fragments rather than silently neutralizing or desalting a structure. The
committed artifact records parser provenance, dependency/configuration
versions, quality metrics, duplicate InChIKey groups, and multi-fragment counts.

`just chemical-map-check` performs the fast CI staleness and quality check.
`just chemical-map-recompute-check` additionally reruns the full exact
fingerprint, pairwise-distance, and UMAP build and requires byte-identical
output in the pinned local environment.

## Schema

`src/antibioticmech/schema/antibioticmech.yaml` defines:

- **AntibioticRecord** — root class, one per YAML file: `identifier`, `label`,
  `definition`, `synonyms`, `parent_compounds`, `xrefs`, `antimicrobial_class`,
  `activity_roles`, `structural_class`, `chemical_structure`, `source_concepts`,
  `grounding_status`, `curation_status`, `curation_history`.
- **ChemicalStructure** — SMILES, standard InChI, InChIKey, formula, charge,
  masses, and where they came from. The InChIKey is the identity check.
- **MolecularTarget / ResistanceMechanism / ActivityObservation** — the
  mechanism layer. Every one of them **requires evidence**: classification is
  inherited from ChEBI and CARD, but a mechanism claim is asserted and must say
  who asserted it.
- **CausalGraph / CausalNode / CausalEdge** — evidence-backed mechanism graphs
  (uptake → target engagement → growth inhibition or death), the same shape
  TraitMech uses for trait mechanisms.
- **Discussion / Dataset** — from `mech_shared.yaml`, vendored byte-identical
  across the Mech repositories and sha-pinned by `tests/test_schema.py`.

## Sources

| Source | What it contributes | Scope |
|---|---|---|
| [ChEBI](https://www.ebi.ac.uk/chebi/) | Identity, structures, definitions, synonyms, cross-references, antimicrobial roles | 3-star (manually curated) entries only |
| [CARD/ARO](https://card.mcmaster.ca/) | Individual antibiotic molecules, drug classes, resistance determinants, drug targets | `ARO:1000003` antibiotic molecule subtree |
| [PubChem](https://pubchem.ncbi.nlm.nih.gov/) | Structures for ARO molecules ChEBI does not cover | Only the CIDs CARD cross-references |

Scope follows ChEBI's own reading of "antimicrobial": compounds acting on
bacteria, mycobacteria, fungi, protozoa **and viruses**, plus the biocides used
against them. Antibiotic pesticides are excluded by an explicit, revisitable
decision in `conf/sources.yaml` — insecticides, acaricides and nematicides act
on metazoa.

Antivirals sit differently in the mechanism layer: their target is a viral
protein or a replication step, and CARD's resistance determinants do not apply,
so an antiviral record carries no CARD mechanism evidence. The schema's
mode-of-action and target vocabularies cover both kinds.

## What is generated, and what is curated

**Generated** (never hand-edit): `data/antibiotics/**`, `data/raw/**`,
`data/antibiotics/PATHS.tsv`,
`data/embeddings/chemical-structure-map.json`, `pages/**`, and the
statistics block in this README. `just verify-corpus` rebuilds the corpus from
`data/raw/` and rejects
drift **in the fields the seeder owns** — identity, label, definition, synonyms,
parents, xrefs, class, roles, structural class, structure, source concepts,
grounding status, and the CARD-derived mechanism items.

It does **not** compare curated fields, by design, or curation would make the
check permanently red. So it will not catch a *fabricated* claim: a hand-added
`molecular_target` citing an invented PMID, or a hand flip of `curation_status`
to `REVIEWED`, passes every gate. Those are what review is for, not the
reproduction check.

**Curated**: `curation/decisions.tsv` (grounding and exclusion decisions, keyed
by a source concept's minted identifier), and the mechanism fields on a record —
`mode_of_action`, `molecular_targets` beyond CARD's, `activity_spectrum`,
`producer_organisms` beyond the MIBiG-marked slice, `causal_graphs`,
`discussions`. `verify-corpus` does not compare those, so curation and
reproducibility coexist — with three exceptions: MIBiG-marked producer
assertions and Drugs@FDA-marked clinical assertions are compared to their
committed inventories, and a `mode_of_action` still carrying the seeder's note marker is the
seeder's, and is compared along with its notes and target scope, because a bare
hand edit of a seeded mechanism is drift rather than curation. Writing a
`CURATOR:` note claims the field and ends the comparison.

## Licence

Two licences, because the repository holds two different things.

**Code, schema, tests, configuration, documentation and curation decisions:
[CC0 1.0](LICENSE).** This repository's own work, dedicated to the public domain.

**Record content — `data/antibiotics/**` and `data/raw/**`:
[CC BY 4.0](LICENSE-DATA), attribution in [ATTRIBUTION.md](ATTRIBUTION.md).**
It is derived from ChEBI (CC BY 4.0) and CARD's ARO (CC BY 4.0), and CC BY
content cannot be re-dedicated to the public domain: §3(b) permits an adapter's
licence only if it does not prevent recipients complying with the original, and
stripping attribution does exactly that. So the corpus is redistributable —
freely, commercially, modified — provided the attribution rides along.

Attribution is per-record and machine-readable: every record's `source_concepts`
block names the upstream concepts it came from, so a consumer taking a subset can
derive precisely which sources that subset depends on.
`data/raw/MANIFEST.yaml` records what was retrieved and when.
