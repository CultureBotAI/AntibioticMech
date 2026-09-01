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

**`ANTIMYCOBACTERIAL` is a subclass of `ANTIBACTERIAL`, and the counts say so.**
Mycobacteria are bacteria, but filing is exclusive and picks the narrower claim,
so those 78 records are not also filed `ANTIBACTERIAL`. Any count answering
"which compounds act on bacteria?" has to add them back: it is **1115**, not the
1037 filed directly. `just report`, the README table and the site all derive
this from the schema's enum `is_a` through one shared helper
(`seed_from_sources.class_parents`), so a hierarchy the schema declares cannot
be one only the site honours. 76 of the 78 carry no general antibacterial role
at all — their only bacterial evidence is `antitubercular`,
`antimycobacterial` or `leprostatic` — which is why the class stays a filing value rather than
being collapsed: it is a more specific true claim, and `activity_roles` would
be the only place it survived.

## Mode of action

`mode_of_action` is seeded from ChEBI's own mechanism roles. The maps in
`conf/sources.yaml` translate 32 of them — `protein synthesis inhibitor`,
`sterol 14α-demethylase inhibitor`, `HIV-1 reverse transcriptase inhibitor` and
so on — into `ModeOfActionEnum`, and 416 of 2,911 records carry a value.

This is a **restatement**, not an inference, and the distinction matters because
the alternative was tried here and failed. Filing a record on a ChEBI structural
class whose name states a target group asserted activity for chemotherapy drugs,
an insecticide and bare ring scaffolds, because a chemical class says what a
compound IS and its members are not all active on the named target. A role is
different: ChEBI asserting `protein synthesis inhibitor` of a compound is a
direct claim about what that compound does, and the map only puts it in this
schema's words.

Five disciplines keep it honest:

- **A role whose target only exists in a eukaryote is conditional on the target
  group.** A mitochondrion is a eukaryotic organelle, so
  `mitochondrial cytochrome-bc1 inhibitor` is exactly the mechanism of a
  strobilurin fungicide and meaningless for a bacterium. Those roles apply on
  ANTIFUNGAL and ANTIPROTOZOAL records and nowhere else — mapping them
  unconditionally put an energy-metabolism mechanism on antibacterials, and
  removing them outright stripped 23 antifungals of a correct one.
- **Host-directed roles are unmapped.** The same role space holds angiogenesis,
  acetylcholinesterase, proteasome and platelet-aggregation inhibitors. A mode of
  action here is a claim about how a compound kills or inhibits a microbe, and
  inheriting one from unrelated pharmacology is the confident wrongness the gates
  cannot see.
- **Whose target it is, is recorded rather than hedged.**
  `mode_of_action` means *the mechanism by which the compound exerts its
  antimicrobial effect*. That does **not** require a microbe-specific target: a
  host-directed antiviral inhibits the host translation the virus depends on,
  and a virus has no ribosome of its own. Suppressing those would not be rigour;
  it would make the corpus unable to express a real drug class. But
  `PROTEIN_SYNTHESIS_INHIBITION` alone cannot tell linezolid's bacterial 50S
  from omacetaxine's host 80S, so `mode_of_action_target_scope` says which:
  `MICROBIAL_TARGET` (176 records) when a contributing role names a target the
  host lacks, `HOST_SHARED_TARGET` (240) when none does. Presence is the rule
  and a role's cohort is evidence about presence, not a second rule — reading it
  the other way made trimethoprim host-shared for a host enzyme while terbinafine
  was microbial for one. It is **not a
  confidence rating** — both mark true mechanisms, and the host-shared value
  covers microbe-selective drugs acting on a conserved machine as well as
  genuinely host-directed ones. It marks where the selectivity question exists;
  `molecular_targets` is where a curator answers it. Once a curator claims
  `mode_of_action`, the seeder can no longer derive a scope for their value and
  copies the block forward untouched rather than guessing — `just worklist
  --queue moa-scope` is where an unsettled scope shows up.

  The aggregate is by ANY: a record is `MICROBIAL_TARGET` when any contributing
  role names a target the host lacks, which is what makes it a usable filter —
  ciprofloxacin carries `topoisomerase IV inhibitor` alongside the generic `DNA
  synthesis inhibitor`, and reading it the other way would put the most
  selective antibacterial class there is on the wrong side. (This was once
  described as "a specific role outranks a generic one". That was never the
  rule, only a coincidence of that example; the azoles showed the generic role
  winning over the specific one under the same sentence.)

  The split runs inside a single combination drug: sulfamethoxazole is
  `MICROBIAL_TARGET` because the host has no dihydropteroate synthase,
  trimethoprim is `HOST_SHARED_TARGET` because the host's dihydrofolate
  reductase is methotrexate's target. And it does *not* split a drug class:
  every sterol-pathway antifungal is host-shared, because an azole's target is
  CYP51 and the host has CYP51. Their selectivity is affinity, not absence.
- **Several mechanisms give `MULTIPLE`, never a silent pick.** Rifampicin carries
  both an RNA-polymerase and a protein-synthesis role; the notes name both and
  leave the primary one to a curator.
- **A mechanism from another of the compound's activities says so.**
  `mode_of_action` and `antimicrobial_class` are orthogonal axes, and some role
  names carry a target group inside them: `HIV-1 integrase inhibitor` does,
  `protein synthesis inhibitor` does not. 11 records are filed under one group
  and carry a mechanism belonging to another — equisetin is an antibacterial that
  is also an HIV integrase inhibitor. Both facts are true; a record stating the
  mechanism without stating the mismatch would read as a claim about how its
  antibacterial action works. Those notes name the discrepancy explicitly.

All of it rests on reviewed edges only: of the 572 `has_role` edges into the
mapped roles, 562 are CHECKED or OK and the 10 SUBMITTED are ignored — the same
filter that stopped an unreviewed edge from making zidovudine an antitubercular.

A curator's `mode_of_action` outranks the seeded one. Ownership is decided by a
marker in the notes rather than by the field name, the same way CARD-seeded
mechanism items work.

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

## Mixtures and combination products

A record is one chemical structure, so a fixed-dose combination is not a record.
That was documented and unenforced: a content-bearing InChIKey was taken as proof
that a source concept denotes one chemical, and
`trimethoprim-sulfamethoxazole` — whose own definition calls it "an antibiotic
cocktail" — carried two disconnected drug components and passed every gate.

Twelve are now excluded in `curation/decisions.tsv`, each with the reason: ten
fixed-dose combinations (the beta-lactam/inhibitor pairs, quinupristin-dalfopristin,
Kaletra) and two congener mixtures (capreomycin IA/IB, ganefromycin alpha/beta).
An `EXCLUDE` keeps the source concept and its provenance in `data/raw/` and on
`just worklist`; only the chemical record goes, and its slug is retired in
`RETIRED.tsv`.

**No structural rule separates a combination from a salt**, which is why this is
curated rather than computed. Salts are multi-fragment too and belong in the
corpus. Two *identical* large fragments are a stoichiometric salt — mupirocin
calcium is two mupirocins and a calcium — so those are not even candidates. But
formal charge decides nothing either: clavulanate is drawn as an anion in a
genuine combination, while tosylate is drawn neutral in a genuine salt, so the
heuristic misclassifies in both directions. `just worklist --queue
multi-component` lists what has two or more distinct large fragments and leaves
the judgement to a curator.
## Producer organisms

`producer_organisms` is the corpus's largest empty axis: 3 records of 2,911 carry
one, all from the MIBiG import. The signal is sitting in the definitions — 999
records with none use a phrase that may introduce a producer, and 801 of those
are followed by a binomial.

**That is a queue, not an extraction.** A taxon in a definition may be the
producer, the isolation source, an expression host, a susceptible organism, or
mentioned for a reason that is not biological at all — "derived from" is often
chemical derivation. `just worklist --queue producer-candidate` reports the
matched phrase, WHAT THAT PHRASE CLAIMS, and the candidate binomial, and asserts
nothing:

- *produced by*, *metabolite of* — biosynthesis stated, and a curator can often
  settle these from the definition alone. These sort first.
- *isolated from*, *obtained from* — **source only**. Frequently the producer and
  sometimes not: a marine natural product isolated from a sponge may be made by
  its symbiont.
- *derived from* — ambiguous, and often chemical rather than biological.

A curator writes the `ProducerOrganism` with its own citation, which is what the
field requires. `strain` is separate from `taxon_label` because a producer claim
is frequently strain-specific and a consumer asking "which species produce this?"
should not have to parse a collection number out of a species name.

## The corpus map

`just embed` turns each record into a 1024-d vector with a local model
(BAAI/bge-large-en-v1.5, no API and no per-record cost), and `just embed-map`
projects those to two dimensions for the site's [corpus map](../pages/map.html).

**It embeds the annotation, not the chemistry.** Proximity means "described
similarly" — same class, structural family, mechanism, asserted roles — not
"structurally similar". SMILES and InChI are deliberately excluded: a sentence
model reads them as gibberish long enough to dominate every document. So is the
seeded `mode_of_action_notes`, which is near-identical across hundreds of records
by design and would manufacture one enormous false cluster of "records carrying a
seeded mechanism"; the mechanism *value* goes in, its boilerplate does not. The
full include/exclude list is in `scripts/embed_records.py` and asserted by
`tests/test_embeddings.py`.

That makes it a map of the corpus's own descriptions, which is what makes it
useful for curation: an outlier is usually a record whose annotation is thin or
inconsistent with its neighbours, and a cluster spanning two classes is worth
looking at.

It separates the classes without being told them: in the raw 1024-d embedding
**83%** of a compound's ten nearest neighbours share its class, against a **23%**
baseline for these class sizes. That is the encoder's number, and it is the one
this section is entitled to — the 2-D map scores higher (86%) only because
PaCMAP tightens neighbourhoods by construction, so that figure belongs on the
map page describing what a reader of it sees, not here describing the
embedding.

The exception is instructive. In the raw embedding `ANTIMYCOBACTERIAL` scores
51%, with a further 28% of its neighbours in `ANTIBACTERIAL`. The encoder
recovers, from text alone, the subclass relationship the schema declares —
mycobacteria are bacteria.

Field order and length both mattered. 94 documents once exceeded the model's
512-token window, and the tail of those was silently dropped — with synonyms
emitted early, vancomycin kept a list of trade names and lost its resistance
determinants. Mechanism, roles and targets now come before the definition, and
synonyms are chosen by their DECLARED TYPE rather than by guessing from the
string — INN, then brand name, then related, then the exact-synonym residue
under a 60-character ceiling. They were 42% of all corpus tokens and the long
ones are systematic names: precisely the "gibberish of a length that would
dominate every document" that excludes SMILES, readmitted through a different
key. Ranking by type left the clustering unchanged (83.4% to 83.3%); it is done
because `synonym_type` states the answer that a shape heuristic could only
guess, and because vancomycin now carries "Vancocin" rather than a fragment of
its IUPAC name. **No
document now exceeds the window at all** (median 174 tokens, longest 503).

A chemical-similarity map is a different artifact and would need molecular
fingerprints or a chemical language model rather than a text encoder.
