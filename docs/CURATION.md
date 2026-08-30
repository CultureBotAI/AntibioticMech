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
- **Never rename a record file.** Slugs are published URLs. Change the row in
  `data/antibiotics/PATHS.tsv` and re-seed; the integrity tests reject
  disagreement between filename and lockfile.
- **Never hand-edit a seeded field.** `just verify-corpus` rebuilds the corpus
  from `data/raw/` and fails on drift. Put source changes in the extractor and
  curator decisions in `decisions.tsv`.
- **`--prune` only on a full run.** The seeder refuses `--prune` together with
  `--only` or `--limit`, because pruning against a partial build deletes records
  the run never attempted.
