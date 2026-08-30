# CLAUDE.md

Operational guidance for Claude Code and other editing agents in this repository.

## Repository purpose

AntibioticMech is a LinkML knowledge base of **individual chemical structures
with antimicrobial activity**, harmonized from ChEBI (3-star entries bearing an
antimicrobial role) and CARD/ARO (the antibiotic molecule subtree), with
structures for CARD-only molecules fetched from PubChem. One generated YAML
record lives at `data/antibiotics/<class>/<slug>.yaml`. The committed
inventories in `data/raw/` are the reproducible inputs.

Read these before changing domain behavior:

- [README.md](README.md) — public model and generated current statistics.
- [docs/HARMONIZATION.md](docs/HARMONIZATION.md) — identity, merging, scope.
- [docs/CURATION.md](docs/CURATION.md) — decision semantics and evidence rules.

Sibling repositories use similar conventions: TraitMech, CultureMech,
MediaIngredientMech, HabitatMech and CommunityMech. The upstream pattern is
monarch-initiative/dismech.

## Authoritative commands

```bash
just qc                # every local and CI quality gate
just report            # corpus, grounding and mechanism-coverage statistics
just test              # unit and corpus-integrity tests
just validate-all      # closed-schema validation of every record
just verify-corpus     # prove data/antibiotics reproduces from its inputs
just worklist          # the curation backlog, ranked
just source-queue      # the ranked data-source queue and what is unverified in it
just render            # regenerate the committed site under pages/
just docs-stats        # refresh the generated README statistics block
```

`just qc` is authoritative and CI runs the same runner.

For an upstream refresh:

```bash
just extract-inventory-dry
just extract-inventory
just extract-pubchem-dry
just extract-pubchem-canary ARO:0000018
just extract-pubchem
just seed
just seed-canary CHEBI:42355
just seed-apply
just seed-apply --prune   # only when stale records should be removed
```

## Generated-file boundaries

**Never hand-edit a record.** `data/antibiotics/` is generated from the committed
inventories plus curation decisions. Put source harmonization changes in the
extractor or seeder, and curator decisions in `curation/decisions.tsv`.
`just verify-corpus` rejects drift.

**Never write a record except through `write_validated_antibiotic`.** It runs
closed-schema validation before writing, so a doc that drifted into an invalid
shape never reaches disk. Every mutation must also append a `CurationEvent` via
`antibioticmech.curate.curation_event.record_curation_event`.

**Re-emitting an unchanged record must be byte-identical.** Preserve the YAML
emission contract enforced by `tests/test_write_validated.py`; do not loosen the
test to accommodate a new serializer shape.

**Edit site templates, not `pages/`.** Change
`src/antibioticmech/templates/`, run `just render`, commit the regenerated pages.

**Do not edit `src/antibioticmech/schema/mech_shared.yaml` here.** It is vendored
byte-identically across the Mech repositories and sha-pinned by the schema tests.

## Safe corpus workflow

**Canary before a bulk write, and before any paid or networked batch.** The
PubChem enrichment is the only networked step: `just extract-pubchem-dry`, then
`just extract-pubchem-canary <ARO_ID>`, then read the written row before the
batch. Same for seeding: `just seed`, `just seed-canary <IDENTIFIER>`, read the
file, then `just seed-apply`.

**Never rename a record file directly.** Change the identifier-to-slug row in
`data/antibiotics/PATHS.tsv` and re-seed. Slugs are published URLs and the
integrity tests reject filename/lockfile disagreement.

**Do not prune on a partial run.** `--prune` with `--only` or `--limit` is
refused, because it would delete records the run never built.

**Treat extractor drift as evidence to inspect.** `data/raw/MANIFEST.yaml`
records the sha256 of every upstream file and every emitted inventory.
`just provenance-check` after any change to `data/raw/`.

## Skills

`.claude/skills/` carries two workflows, both read-only by default:

- **`review-open-issues`** — sweep and rank the whole open-issue queue against
  the committed corpus. Its P0 tier is specific to this repository: something
  wrong that every gate passes, which is how 25 defects were once found across two review
  passes, every one of them with `just qc` green.
- **`source-queue`** — triage `curation/source_queue.tsv`, the ranked list of
  data sources this corpus might adopt.

Neither closes issues, adopts sources, or edits the corpus. Those are asks.

## Adopting a data source

Candidates live in `curation/source_queue.tsv`, ranked by the corpus gap they
close. Two rules the checker enforces, both of which exist because the corpus is
CC0: a source cannot be ADOPTED while its redistribution terms are UNVERIFIED,
and a source with RESTRICTED terms cannot be seeded — it can inform a curator
and nothing more. Adoption is a pull request that adds the extractor path, the
committed inventory and its manifest entry; editing the row alone makes
`just source-queue` fail, which is intended. The `source-queue` skill triages.

## Semantic invariants

- **A record is a structure.** No InChIKey, no record — a name is not a
  structure. Concepts without one go to `just worklist`, not into the corpus.
- **A drug class is never a record.** It is `structural_class` /
  `parent_compounds` on the records it covers.
- **Merge on InChIKey, with two exceptions.** ChEBI-internal collisions (a
  compound and its zwitterion) stay separate; two *minted* concepts sharing a
  structure are flagged with a `CURATION_TODO` discussion rather than merged,
  because at least one upstream cross-reference is wrong and the seeder cannot
  tell which. A minted record must never duplicate a ChEBI-grounded structure.
- **`antimicrobial_class` is a filing decision; `activity_roles` is the
  evidence.** Never drop a role because the class was assigned.
- **Mechanism claims require evidence; classification does not.** Record-level
  `evidence` is optional because ChEBI and CARD supply provenance. Every
  `MolecularTarget`, `ResistanceMechanism`, `ActivityObservation` and
  `CausalEdge` requires its own citation.
- **A CARD-seeded item cites CARD and says so.** Do not silently present a
  database assertion as a literature citation.
- **An MIC without units is not a measurement.**
- **`parent_compounds` means strictly broader**; an xref means the same
  structure. A salt, conjugate or stereoisomer is a different record.
- **A protein target should be a family, complex or function term.** UniProt
  accessions are organism-specific examples, not target identities.

## Git workflow

Branch before the first edit. Open a PR for every change, including docs-only
changes. Review the diff as a separate adversarial pass and file findings as
issues. Do not merge without explicit approval. Delete branches after merge.
