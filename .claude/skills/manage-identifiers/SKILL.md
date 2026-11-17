---
name: manage-identifiers
description: "Assign, mint, and audit record identifiers in AntibioticMech. Covers which identifier a new record gets, how to mint one when the corpus mints its own, and the hygiene checks — duplicates, format, collisions, and identifiers that changed. Use when adding or importing records, promoting a placeholder, or reconciling a collision."
category: workflow
requires_database: false
requires_internet: false
version: 1.0.0
tags: [identifiers, curation, provenance]
---

# Identifier management

- Repository: `CultureBotAI/AntibioticMech`
- Records this governs: `data/antibiotics/**/*.yaml`
- Schema: `src/antibioticmech/schema/antibioticmech.yaml`

## The invariants

<!-- canonical:begin the-invariants -->
Three rules hold in every Mech, whatever scheme it uses:

- **An identifier never changes once assigned.** Anything that cited the old
  value now points at nothing, and the fleet is built on cross-repository
  citation. If a record turns out to denote something else, that is a new
  record and a retirement, not an edit.
- **An identifier is never reused.** A retired id stays retired. Reuse is worse
  than a dangling reference, because a dangling reference is detectable and a
  silently repointed one is not.
- **Exactly one slot is the identity.** The schema marks it `identifier: true`.
  A record may carry many other CURIEs — grounding targets, cross-references,
  registry accessions — and none of them is the identity, however similar it
  looks.

The third is where corpora actually go wrong. A record whose `identifier`
happens to equal its ontology grounding is not thereby an ontology record: the
two fields answer different questions, and they are allowed to diverge.
<!-- canonical:end the-invariants -->

## Choosing a scheme

<!-- canonical:begin choosing-a-scheme -->
The fleet uses **three** legitimate schemes. Which one a corpus uses is a
property of the corpus, not a fleet convention, and none is more correct:

- **Minted sequential.** `<RepoName>:NNNNNN`, zero-padded, assigned in order and
  never reused. Right when the corpus defines entities nobody else has defined,
  so there is no upstream id to adopt.
- **Upstream-first.** The record carries the ontology's own CURIE as its
  identity, with a minted prefix reserved only for entities the ontology does
  not yet cover. Right when an upstream ontology already enumerates the domain
  and the corpus is curating against it.
- **External CURIE with placeholder.** The identity is whichever external CURIE
  best denotes the thing — several prefixes in play — with a local placeholder
  for records not yet resolved, promoted to the real CURIE when they are. Right
  when the corpus is a mapping product: the identity *is* the mapping.

Adopting the wrong one is expensive to undo, because of invariant one. Decide
from the corpus: does something upstream already name these things?
<!-- canonical:end choosing-a-scheme -->

## Do not describe another repository's scheme

<!-- canonical:begin describing-siblings -->
**State this repository's scheme. Do not state a sibling's.** A sentence about
how another Mech mints ids has no check on it, and the sibling will change
without telling you.

This is not hypothetical. Measured on 2026-09-04, **three of the four** existing
copies carried false claims about their neighbours:

- one asserted that MediaIngredientMech "mints its own `<RepoName>:NNNNNN`
  sequential IDs" — MIM has **zero** such identifiers, and its own skill records
  that the legacy sequential id was deliberately removed;
- another described MediaIngredientMech as a "single-file collection" — it is
  2,952 separate YAML files;
- the third, and the origin of the pattern, is a document titled "Identifier
  Management for X-Mech Repositories" that lives inside a single Mech, declares
  its scope to be "all X-Mech repositories", and works its examples in
  `MediaIngredientMech:000001`.

All three were accurate about some earlier state and rotted in place. Each copy
is right about itself and wrong about its neighbours — the predictable result of
writing down something nothing verifies. The generic one rotted worst, because
breadth is exactly what nothing checks.

If a cross-repository fact matters, cite the check that establishes it rather
than the fact: `kg-microbe-skills check` for references, the sibling's own
schema for its identity slot. A pointer stays true; a copy does not.
<!-- canonical:end describing-siblings -->

## Hygiene

<!-- canonical:begin hygiene -->
Whatever the scheme, the same four things go wrong and are worth checking
before a batch lands:

- **Duplicates.** Two records claiming one identity. The corpus can no longer
  answer which one a citation meant.
- **Format.** A padding, prefix or case that differs from the rest. `CHEBI:1234`
  and `chebi:1234` are the same term to a reader and two strings to everything
  else.
- **Collisions on import.** A batch that mints from a stale high-water mark, or
  adopts upstream ids that already exist in the corpus.
- **Changed identifiers.** The invariant that is hardest to see, because the
  diff looks like an ordinary edit. Compare against the previous release, not
  against the working tree.

A gap in a sequence is **not** a defect. Retirement leaves holes, and a run that
closes them has renumbered records, which violates the first invariant.

**Record the retirement rather than merely permitting it.** A retired id that is
simply absent makes every citation to it fail silently; a recorded one resolves
to a retirement a reader can act on. The shape that works, which one Mech in the
fleet already operates:

- retirement is written down, not implied by absence;
- a successor claim requires an *established* successor — one for a merge, two
  or more for a split;
- when no successor is established, say so and **do not guess a redirect**. A
  wrong redirect is worse than an honest dead end, because it resolves.

Where that record lives and what columns it has is this repository's business;
that it exists is not.
<!-- canonical:end hygiene -->

## This repository's scheme

- **Scheme**: Upstream-first (`CHEBI:<digits>`) with content-hashed minted fallback (`antibioticmech:<source>-<10-hex>`)
- **Identity slot**: `identifier` (`identifier: true` on `AntibioticRecord`)

AntibioticMech uses the **upstream-first** scheme:

- **Identity slot**: `identifier` on `AntibioticRecord` (`range: curie`), enforced by `scripts/verify_corpus.py` and tracked in `data/antibiotics/PATHS.tsv` (active records) and `data/antibiotics/RETIRED.tsv` (retired records).
- **When ChEBI has an exact compound entry with a verified chemical structure**: `identifier` is `CHEBI:<digits>` and `grounding_status` is `EXACT`.
- **When ChEBI lacks an exact structure-bearing compound**: `identifier` is minted deterministically by `mint(source, source_id)` in `scripts/seed_from_sources.py` as `antibioticmech:<source>-<10-hex>` (lowercase source tag `curator`, `aro`, or `chebi` followed by the first 10 hex digits of `sha256("{source}|{source_id}")`), and `grounding_status` is `CLOSE` (if `parent_compounds` maps to a broader `CHEBI:` parent) or `MINTED` (if no ChEBI parent applies). Slug stability, retirements, and merge/keep/split decisions are governed by `data/antibiotics/PATHS.tsv`, `data/antibiotics/RETIRED.tsv`, and `curation/decisions.tsv`.
- **Validation commands**:
  ```bash
  just validate-strict
  just verify-corpus
  ```
- **Worked example**: `identifier: CHEBI:17833` (daptomycin, `grounding_status: EXACT`) or `identifier: antibioticmech:curator-452d38df8e` (corramycin, `grounding_status: MINTED`, tracked in `data/antibiotics/PATHS.tsv`).
## Related

- `kg-microbe-skills check` validates that every path and sibling-skill
  reference in `.claude/` resolves, which is the check that would have caught
  the rotted cross-repository claims above had they been references rather than
  prose.
- The `id-label-correspondence` skill governs a different question: whether an
  identifier carries its own correct label. Identity and labelling are separate
  failures — a record can have the right id and the wrong label, and the reverse.
