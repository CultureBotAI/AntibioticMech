# Curation

## The decision file

`curation/decisions.tsv` is the curator's half of seeding. One row per source
concept, keyed by that concept's **minted identifier** — the stable
`antibioticmech:<source>-<hash>` CURIE that appears in every record's
`source_concepts` block, including for concepts that ground to ChEBI.

| Column | Meaning |
|---|---|
| `minted_identifier` | The key. Copy it from the record or from `just worklist`. |
| `source` / `source_id` / `source_label` | Context for a human reading the file. |
| `decision` | `GROUND` (use `identifier`), `EXCLUDE` (drop the concept), or `KEEP_MINTED`. |
| `identifier` | The CURIE to ground to. Required for `GROUND`. |
| `curator` / `date` / `rationale` | Who decided, when, and why. |

Decisions are applied at seed time, so a decision changes the corpus only after
`just seed-apply` — and `just verify-corpus` then proves the corpus matches.

A `GROUND` decision is honoured **before** the structure gate, and the grounding
target lends its structure to the concept. That is what makes the decision file
useful on the no-structure queue, the largest backlog: grounding
`ARO:3000636` to `CHEBI:18208` gives the concept ChEBI's identity *and* ChEBI's
structure. If the target has no structure either, the seeder says so on stderr
rather than dropping the decision silently.

## What a REVIEWED record means

A record moves from `SEEDED` to `REVIEWED` when a curator has checked all of:

1. **Identity** — the structure is the compound the label names, and the ChEBI
   grounding (or the reason for a minted identity) is right.
2. **Structure** — SMILES/InChI/InChIKey agree with each other and with the
   formula. For a PubChem-sourced structure, that the CID denotes this compound
   and not a salt, a stereoisomer, or a different member of the family.
3. **Class** — `antimicrobial_class` and `activity_roles` reflect what the
   sources actually assert.
4. **Mechanism** — at least a `mode_of_action`, with `molecular_targets` carrying
   real citations where the target is known.

A record with a curated `causal_graph` is the goal state, not the entry
requirement.

## Correcting or vetoing a seeded mode of action

`mode_of_action` is seeded from ChEBI's mechanism roles, and its note names the
role it came from. To take the field over, write a note beginning `CURATOR:`.

```yaml
mode_of_action: PROTEIN_SYNTHESIS_INHIBITION
mode_of_action_notes: >-
  Assigned from ChEBI role CHEBI:67268 (...). CURATOR: corrected — the integrase
  role belongs to this compound's antiviral activity, PMID:123.
```

The same marker with **no** `mode_of_action` is a veto: it says no mechanism
should be seeded here, and the seeder will leave the field empty rather than
writing its own value back.

```yaml
mode_of_action_notes: >-
  CURATOR: cefdinir is a cephalosporin. CARD cross-references it to an unrelated
  ChEBI entry, so any derived mechanism is wrong. Leave blank.
```

Both survive `just seed-apply`.

**`mode_of_action_target_scope` travels with the value.** It records whether the
target belongs to the microbe (`MICROBIAL_TARGET`) or is one the host has too
(`HOST_SHARED_TARGET`), derived from the same roles as the mechanism.

Claiming the mechanism claims the scope, and `verify-corpus` stops comparing
both from then on — so a `CURATOR:` note is the only thing standing between a
hand edit and a selectivity claim the sources never made. Write one only when
you mean it.

**If you change the mechanism, state the scope.** The seeder derived the scope
for the value it wrote; once you replace that value, the scope describes
something no longer on the record — and the seeder cannot tell your scope from
its own leftover, so it does not guess. It copies your whole block forward
verbatim, an omitted scope included. `just worklist --queue moa-scope` lists the
records where that is still owed. A veto is the exception: with no mechanism
asserted there is nothing for a scope to describe, so it is dropped. It is **not a confidence rating** — `HOST_SHARED_TARGET`
covers linezolid, which is genuinely microbe-selective on a conserved ribosome,
as well as omacetaxine, which is not. It marks where the selectivity question
exists so that `molecular_targets` can answer it.

**The notes decide ownership, not the value.** Setting `mode_of_action` without
writing a note leaves the field the seeder's, and the next run will replace it —
because a bare value is indistinguishable from a hand-falsified one, and
`verify-corpus` has to be able to tell.

**Write the `CURATOR:` token whenever the seeder's sentence is still in the
note.** Appending prose without it does *not* claim the field: the seeder's
marker is still there, so the note reads as the seeder's, your correction is
reverted on the next run and `verify-corpus` reports drift until it is. Replacing
the note wholesale with your own prose does claim the field — but appending is
the natural thing to do, and appending is the case that needs the token.

## Evidence rules

- `AntibioticRecord.evidence` is **optional**: a seeded record inherits
  provenance from ChEBI and CARD, and requiring per-record citations would fill
  2,600 files with boilerplate.
- `MolecularTarget.evidence`, `ResistanceMechanism.evidence`,
  `ActivityObservation.evidence` and `CausalEdge.evidence` are **required**.
  These are asserted mechanism claims, not inherited classifications.
- A CARD-seeded item cites the ARO term and says so in `notes`. Replacing that
  with a primary citation is an upgrade a curator makes deliberately; leaving it
  is honest.
- An MIC without units is not a measurement. The schema keeps `mic_units`
  separate and a test fails on a value without them.

## Semantic invariants

- **`parent_compounds` means strictly broader.** A ChEBI `is_a` parent or an ARO
  drug class belongs there. A related-but-not-broader compound is an xref.
- **An xref is the same structure.** A conjugate acid, a salt, or a stereoisomer
  is a different structure and a different record.
- **A protein target should be taxon-agnostic.** Prefer a family, complex or
  function term (GO, InterPro, ComplexPortal); a UniProt accession is an example
  of the target in one organism, and belongs in `protein_examples`.
- **A producer organism claim needs a citation or a MIBiG BGC accession.** "This
  compound is made by *Streptomyces*" is a biological claim like any other.
- **Do not read a mode of action off a drug class.** Most macrolides inhibit
  protein synthesis; that is a reason to look, not a citation.

## Working safely

- **Canary before a bulk write.** `just seed` (dry run), then
  `just seed-canary <IDENTIFIER>`, then read the file that was written — not just
  the exit code — before `just seed-apply`.
**An xref means the same structure, and the seeder now enforces it.** Three
kinds of source cross-reference are dropped rather than copied: a namespace that
does not identify a structure at all (a `pdb:` accession is a macromolecular
entry — ampicillin carried `pdb:1H8S`, an anti-ampicillin *antibody* complex);
one whose structure is known and different (polymyxin B2 carried `CHEBI:8309`,
which is polymyxin B1); and one already listed in `parent_compounds`, which
means strictly broader and cannot also mean the same. `pdb-ccd` stays — it
identifies a ligand chemical component. `patent:` and `wikipedia.en` fail the same test — a patent covers a class of
compounds and an article covers a topic — but are **kept**, because dropping
them cost more than it fixed: 96% and 97% of those accessions map to exactly one
structure in this corpus, so removing ~1,800 links would have fixed 57 false
equivalences and left 7 records with no cross-references at all. Issue #92 asked
for such identifiers to be *moved* rather than deleted, and the destination is a
schema decision not yet taken (#136).

**One caveat the field cannot escape.** Some namespaces identify a *drug* rather
than a molecule — `drugbank:DB00639` legitimately covers butoconazole, its
nitrate and both enantiomers, which this corpus keeps as separate records. Those
are kept for their utility and named in `DRUG_GRANULARITY_XREF_PREFIXES`, so the
exception is declared rather than discovered. See issue #134.

Where the structure cannot be compared, the xref is **kept** and listed by
`just worklist --queue xref-unverified`. Dropping a source assertion because we
cannot check it would be a worse error than carrying one unchecked; carrying it
silently was the error.

- **Never rename a record file.** Slugs are published URLs. Change the row in
  `data/antibiotics/PATHS.tsv` and re-seed; the integrity tests reject
  disagreement between filename and lockfile.

- **A slug that leaves the corpus stays reserved.** When a record drops out its
  row moves to `data/antibiotics/RETIRED.tsv`, and `assign_slugs` keeps that
  string out of circulation, so a later compound can never inherit a published
  URL that pointed at something else. A returning identifier is removed from the
  ledger and reclaims its own slug. 134 slugs were retired when unreviewed ChEBI
  relations stopped being trusted, 19 of which returned when antivirals entered
  scope, leaving 115; the pages they served are gone, and a
  redirect map for them is still owed (see NEXT_TASKS.md).
- **Never hand-edit a seeded field.** `just verify-corpus` rebuilds the corpus
  from `data/raw/` and fails on drift — for the fields the seeder owns. It
  deliberately does not police curated fields, so it cannot see a *fabricated*
  mechanism claim; that is what review is for. Put source changes in the extractor and
  curator decisions in `decisions.tsv`.
- **A moved record keeps its curation.** A record whose class changes moves
  directory, and the seeder reads its previous location from `PATHS.tsv` before
  writing, so curated fields survive the move and the old file is removed in the
  same step. 57 records moved class on a single run of this pipeline.

- **`--prune` only on a full run.** The seeder refuses `--prune` together with
  `--only` or `--limit`, because pruning against a partial build deletes records
  the run never attempted.
