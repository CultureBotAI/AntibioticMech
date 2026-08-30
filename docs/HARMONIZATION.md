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

The 371 concepts in that position are not lost: `just worklist` lists them, and
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

### A caution on the InChIKey as identity

The whole corpus keys on the Standard InChIKey, and it has documented limits the
ChEMBL team states about their own registration system: it does not recognise
some 1,5 keto-enol tautomer pairs as the same compound, cannot express cis/trans
isomerism in organometallics (cisplatin and transplatin hash differently only by
luck of representation), and does not support relative stereochemistry — only
absolute or none. For this corpus that means two things. A collision is not
proof of sameness, which is why ChEBI-internal collisions are surfaced rather
than merged; and an absence of collision is not proof of difference, so a
tautomer pair can enter as two records with no signal at all. Macrocyclic
peptides and glycopeptides are where this is most likely to bite.

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

## Structural class

The ARO drug class is the nearest class ancestor of the molecule. When two class
ancestors sit at the same depth the field is left **empty** rather than resolved
by file order: lassomycin has both `rifamycin antibiotic` and `lasso peptide
antibiotics` as parents, and picking whichever line came first in `aro.obo`
asserted it is a rifamycin, which it is not. The stakes rose once
`structural_class_id` began feeding class assignment, where a wrong pick moves a
record's directory.

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

`conf/sources.yaml` holds the in-scope and out-of-scope ChEBI role roots. Scope
follows ChEBI's own reading of "antimicrobial": bacteria, mycobacteria, fungi,
protozoa **and viruses**, plus the biocides used against them. The antiviral
branch — antiviral agent, anti-HIV, anti-HBV, anticoronaviral, and the
viral-enzyme inhibitors ChEBI files beneath it — is in.

Antivirals do sit differently in the mechanism model. The target is a viral
protein or a step in a replication cycle rather than a structure of a
free-living cell, and CARD's resistance determinants and drug targets do not
apply to them at all, so an antiviral record carries no `resistance_mechanisms`
from CARD. That is a reason for the mechanism vocabulary to cover both kinds of
target — `ModeOfActionEnum` has the viral polymerase/protease/integrase/entry/
release/assembly values and `TargetTypeEnum` has `VIRAL_PROTEIN` — not a reason
to exclude the compounds.

Antibiotic pesticides (insecticides, acaricides, nematicides) remain out: their
targets are metazoa, which is a different kind of claim again.

Both lists are curation decisions written where they can be changed and
re-extracted, not assumptions buried in code.

## Two independent trust filters on ChEBI

**`min_stars: 3` governs the compound entry.** ChEBI's 2-star entries are
automatically imported and not manually reviewed.

**`relation_status_allowed: [1, 3]` governs the edges.** ChEBI stamps each
relation row with its own status (1 CHECKED, 3 OK, 9 SUBMITTED), and the star
rating of a compound says nothing about the review state of the `has_role` edge
hanging off it. Admitting SUBMITTED edges is how zidovudine and efavirenz were once classified
as **antitubercular**, on the strength of an unreviewed edge. Both are in the
corpus today — antivirals are in scope — but as antivirals, on ChEBI's reviewed
`antiviral drug` and `HIV-1 reverse transcriptase inhibitor` assertions. The
point stands independently of scope: an unreviewed edge should not decide what a
compound is. Both filters are needed; neither substitutes for the other.

A wrong role here means a compound that is not an antimicrobial getting an
antimicrobial record. The exception is a ChEBI entry cross-referenced by an ARO
molecule: CARD's assertion that the compound is an antibiotic is itself evidence,
so the entry is admitted for its structure regardless of star rating.

## What CARD contributes, and how it is cited

CARD supplies two things no chemistry resource does: `confers_resistance_to_antibiotic`
edges (4,555 of them) and `targeted_by_antibiotic` edges (252). Both are seeded
onto records, each item citing the ARO term itself with a note saying plainly
that it is a database assertion rather than a primary citation. A curator
upgrading one to literature replaces the reference.

`mechanism_type` is read off the determinant's ancestry using the map in
`conf/sources.yaml`. The walk follows **`is_a` and `participates_in`**, because
ARO does not link a determinant to its mechanism category by subclassing:
`antibiotic efflux` (ARO:0010000) is not an `is_a` ancestor of anything. The link
is carried by `participates_in` on ten determinant-family roots — efflux pump
complex or subunit, antibiotic target protection protein, and so on. Following
`is_a` alone made eight of the ten categories unassignable and left 2,252 of
4,555 rows `UNKNOWN`; following both leaves 25.

The walk is breadth-first with every level sorted, so the nearest classification
wins and a determinant with two equally-near mechanism ancestors resolves the
same way on every machine — set iteration here would make the committed
inventory depend on `PYTHONHASHSEED`. Seven determinants (the mycobacterial
iniA/iniB/iniC family) are genuinely ambiguous between target alteration and
efflux; `mechanism_source_id` records which ancestor was used.

A determinant whose ancestry matches nothing is seeded `UNKNOWN` and lands on
`just worklist --queue unknown-mech`, ranked by how many records it affects — it
is not guessed. CARD's own authoritative association lives in `card.json`, which
this repository does not yet ingest.
