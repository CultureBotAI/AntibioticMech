# Harmonization: how sources become records

This document explains the identity model. Read it before changing
`scripts/seed_from_sources.py` or `scripts/extract_source_inventory.py`.

## The unit of the corpus is a structure

One `AntibioticRecord` is one chemical structure. Not one name, not one drug
product, not one class. The operational test is an InChIKey: a concept without
one is not written.

That excludes things upstream sources legitimately model but this corpus cannot
key on:

| Upstream concept | Why it is not a record |
|---|---|
| `ARO:3000707` antibiotic mixture | A category, not a compound |
| `ARO:3000705` ampicillin-sulbactam | Two compounds sold together |
| `CHEBI:48923` erythromycin | A ChEBI *class* over erythromycins A–E |
| `ARO:0000000` macrolide antibiotic | A drug class — `structural_class`, not a record |

The 364 concepts in that position are not lost: `just worklist` lists them, and
each needs either a structure or an `EXCLUDE` decision.

## Identity resolution

For each source concept, in order:

1. **A ChEBI concept grounds to its own CURIE.** ChEBI is the identity authority
   for chemical structures here.
2. **An ARO concept grounds to its ChEBI cross-reference** when that ChEBI entry
   has a default structure.
3. **Otherwise the concept keeps a minted identifier**:
   `antibioticmech:<source>-<10-hex>`, hashed from `(source, source_id)`.

The hash covers the source identifier, never the label. A minted CURIE is the
key that `curation/decisions.tsv` rows are written against, so an upstream label
correction must not move it.

## The merge, and its limit

Concepts that resolve to the same **InChIKey** merge into one record carrying
every source concept. That is how CARD's `ARO:0000006` "erythromycin" — whose
ChEBI cross-reference points at a structureless class — still lands on
`CHEBI:42355` "erythromycin A": PubChem supplies the structure CARD's CID
actually denotes, and the InChIKey matches ChEBI's.

Two limits on that rule, both deliberate:

**ChEBI-internal collisions are not merged.** ChEBI keeps `tetracycline` and
`tetracycline zwitterion` as separate entries with the same standard InChIKey,
because they are different protonation states related by `is_conjugate_acid_of`.
Merging them would overrule a curation decision made by the people who own the
identifiers. Both records stay.

**Two minted concepts sharing a structure are flagged, not merged.** CARD gives
gramicidin S and gramicidin C PubChem CIDs that resolve to one structure, so at
least one cross-reference is wrong upstream. Merging would assert the two
peptides are the same compound; dropping both would discard the one that is
right. The seeder can tell neither, so it writes both and attaches a
`CURATION_TODO` discussion to each naming its twin. `tests/test_corpus_integrity.py`
enforces that the flag is present.

What must *never* happen is a minted record duplicating a ChEBI-grounded
structure — that is a failure of resolution, and a test fails on it.

## Class assignment

`antimicrobial_class` decides one thing: which directory the record lives in and
which row of the report it lands on. `activity_roles` keeps every asserted role,
unreduced, so nothing is lost to the filing decision.

Compounds bear several roles at once (tetracycline is antibacterial, antifungal
*and* antiprotozoal in ChEBI). The priority table in `conf/sources.yaml` resolves
that by **target group, bacteria first**: `ANTIMYCOBACTERIAL` (narrower than
antibacterial) beats `ANTIBACTERIAL`, which beats `ANTIFUNGAL`, `ANTIPROTOZOAL`
and `BIOCIDE`. Filing tetracycline under `ANTIFUNGAL` because the mapping
happened to reach it first would be a reporting artefact, not a fact about
tetracycline.

An ARO concept with no ChEBI role is `ANTIBACTERIAL`: every molecule in CARD's
antibiotic subtree is there because a bacterial resistance determinant acts on it.

## Scope

`conf/sources.yaml` holds the in-scope and out-of-scope ChEBI role roots. The
antiviral branch — antiviral agent, anti-HIV, anti-HBV, anticoronaviral, the
viral-enzyme inhibitors — is out. A virus is not a cellular microbe, and nothing
in this mechanism model (envelope uptake, target engagement, resistance
determinant) carries over to a compound acting on host machinery. Antibiotic
pesticides (insecticides, acaricides, nematicides) are out for the same reason:
their targets are metazoa.

Both lists are curation decisions written where they can be changed and
re-extracted, not assumptions buried in code.

## Why 3-star ChEBI only

ChEBI's 2-star entries are automatically imported and not manually reviewed. An
automatic import is exactly where a wrong role assertion enters unexamined, and a
wrong role here means a compound that is not an antimicrobial getting an
antimicrobial record. The exception is a ChEBI entry cross-referenced by an ARO
molecule: CARD's assertion that the compound is an antibiotic is itself evidence,
so the entry is admitted for its structure regardless of star rating.

## What CARD contributes, and how it is cited

CARD supplies two things no chemistry resource does: `confers_resistance_to_antibiotic`
edges (4,555 of them) and `targeted_by_antibiotic` edges (252). Both are seeded
onto records, each item citing the ARO term itself with a note saying plainly
that it is a database assertion rather than a primary citation. A curator
upgrading one to literature replaces the reference.

CARD's determinant→mechanism association lives in `card.json`, not in `aro.obo`,
so `mechanism_type` is read off the determinant's `is_a` lineage using the map in
`conf/sources.yaml`. A determinant whose lineage matches nothing is seeded
`UNKNOWN` and lands on the worklist — it is not guessed.
