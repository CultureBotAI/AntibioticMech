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

| Class | Records | SEEDED | REVIEWED | With CARD mechanism evidence |
|---|---:|---:|---:|---:|
| ANTIBACTERIAL | 1040 | 1040 | 0 | 264 |
| ANTIMYCOBACTERIAL | 78 | 78 | 0 | 15 |
| ANTIFUNGAL | 588 | 588 | 0 | 43 |
| ANTIPROTOZOAL | 248 | 248 | 0 | 2 |
| BIOCIDE | 29 | 29 | 0 | 0 |
| ANTIMICROBIAL_UNSPECIFIED | 486 | 486 | 0 | 0 |
| **TOTAL** | **2469** | **2469** | **0** | **324** |

Identity: **2219** records (90%) are grounded in a ChEBI term; **250** keep a minted `antibioticmech:` CURIE because no ChEBI entry with a structure covers them.

Corroboration: **279** records carry source concepts from both ChEBI and CARD/ARO; **1888** come from ChEBI alone and **302** from CARD alone.

Mechanism layer: **206** records carry a molecular target and **279** carry resistance determinants, both seeded from CARD; **0** carry a curated causal graph. That last number is the work.

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
```

Nothing above touches the network. The inventories in `data/raw/` are committed,
so seeding, validation, rendering and the whole test suite run offline.

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

"Antimicrobial" in ChEBI spans viruses too. This corpus covers compounds acting
on **cellular** microbes — bacteria, mycobacteria, fungi, protozoa — plus the
biocides used against them. The antiviral branch is excluded by an explicit,
revisitable decision in `conf/sources.yaml`, not by oversight: an antiviral acts
on a non-cellular agent through host machinery, and none of the mechanism model
here transfers to it.

## What is generated, and what is curated

**Generated** (never hand-edit): `data/antibiotics/**`, `data/raw/**`,
`data/antibiotics/PATHS.tsv`, `pages/**`, and the statistics block in this
README. `just verify-corpus` rebuilds the corpus from `data/raw/` and rejects
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
`producer_organisms`, `causal_graphs`, `discussions`. `verify-corpus`
deliberately does not compare those, so curation and reproducibility coexist.

## Licence

Code and curated content: [CC0 1.0](LICENSE). Upstream data carries its own
terms — ChEBI is CC BY 4.0, CARD requires attribution for academic use, and
`data/raw/MANIFEST.yaml` records what was retrieved and when.
