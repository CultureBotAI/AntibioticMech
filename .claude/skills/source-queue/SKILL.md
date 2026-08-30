---
name: source-queue
description: Triage and maintain AntibioticMech's prioritized data-source queue in curation/source_queue.tsv — rank candidate sources by the corpus gap they close, verify licence and structure completeness before adoption, and fold in deep-research findings. Use when asked what data source to add next, when evaluating a specific source, or after a research report lands; do not use as permission to extract, seed, or adopt a source.
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Triage the data-source queue

`curation/source_queue.tsv` is the ranked list of data sources this corpus might
adopt. This skill keeps it honest and answers "what should we add next?" with
evidence rather than enthusiasm.

## Read these first

- `curation/source_queue.tsv` — the queue itself.
- `just report` — which fields are actually empty, corpus-wide. A source that
  closes a full column beats one that improves a column already at 90%.
- `docs/HARMONIZATION.md` — the scope decision and the identity model. A source
  outside scope is a rejection, not a low priority.
- `conf/sources.yaml` — what the pipeline reads today.
- `NEXT_TASKS.md` — the work already committed to.

## The ranking rule

Rank by **what the corpus cannot currently assert**, not by how well known the
source is. In order:

1. **Does it close a stated gap?** Check against `just report`, not intuition.
   `producer_organisms`, `activity_spectrum`, `mode_of_action` and `causal_graphs`
   are empty on every record; `molecular_targets` and `resistance_mechanisms`
   exist but cover a minority, and antiviral records have no resistance source
   at all. A source that fills an empty column is worth more than one that
   thickens a full one.
2. **Can we redistribute it?** A source we cannot redistribute is
   `use: CURATE_ONLY` or `REFERENCE` at best — it can inform a curator, and it
   must never be seeded. This is a hard gate, not a weighting.

   The repository's own licence position is **unresolved** (issue #27): `LICENSE`
   says CC0, but every upstream source is CC BY, CC BY-SA or proprietary, and a
   blanket CC0 dedication over CC BY content is not permitted. Until that is
   decided, judge a candidate against the stricter reading: CC BY is acceptable
   with attribution; CC BY-SA propagates share-alike to the whole corpus;
   NonCommercial restricts every downstream user and is refused under either
   outcome; proprietary is refused. Record what the licence says, not what it
   would take to make it work.
3. **Does it carry complete structures where it needs to?** A record is one
   chemical structure. A source that names compounds without structures can
   still supply mechanism or activity data keyed to compounds we already have,
   but it cannot introduce records.
4. **Bulk access over API.** `data/raw/` is committed and the pipeline runs
   offline; a source that can only be scraped or queried per-compound imposes a
   networked step, and there is exactly one of those today for a reason.
5. **Effort, last.** A tractable source that closes nothing still closes nothing.

Two sources that close the same gap: adopt one, measure what it actually added,
then decide about the second. NPAtlas and LOTUS both claim producer organisms;
the second one's value is only knowable after the first.

## Verifying a source before it moves to ADOPTED

`redistribution` starts `UNVERIFIED` and must be checked against the source's own
licence page — not a summary, not a memory, not another database's claim about
it. Record the date in `verified_on`. `scripts/check_source_queue.py` refuses an
ADOPTED row whose terms are unverified, and refuses a `SEED` adoption under
`RESTRICTED` terms, because the CC0 promise is only as strong as the weakest
thing seeded into the corpus.

Also establish, and write into `rationale`:

- **Coverage against this corpus**, not in the abstract: how many of our 2,900+
  records would actually gain a field. "40,000 compounds" is not an answer.
- **Identifier joinability** — does it carry InChIKeys, ChEBI ids, or only
  names? Name-only joining is a curation project, not an extraction.
- **Update cadence and versioning** — a source with no release identity cannot
  be recorded in `data/raw/MANIFEST.yaml`, which every committed inventory needs.
- **Known data-quality traps.** The ones this corpus has already been bitten by:
  class terms modelled as if they were compounds, unreviewed auto-generated
  assertions presented identically to curated ones, salts conflated with parent
  compounds, and activity values with no assay attached.

- **Whether an already-adopted source closes it.** Before adding a dependency,
  check what the sources already in `conf/sources.yaml` assert and are being
  discarded. `mode_of_action` had no candidate in this queue for a week while
  ChEBI was asserting mechanism roles on 765 records we already read.

A licence that cannot be reached is a result too. Record the attempt, the URLs
tried and what blocked them, so the next pass does not repeat a failed fetch —
Stanford HIVdb renders its terms client-side and returns nothing to a fetcher.

## Folding in a research report

When a deep-research report on sources lands, do not paste it into the queue.
For each source it covers: add or update the row, move `redistribution` off
`UNVERIFIED` only where the report cites the licence page itself, and put the
report's specific finding in `rationale`. A claim the report could not verify
stays `UNVERIFIED` in the queue — the report's own confidence labels carry over.

## What this skill does not do

It does not extract, seed, or adopt. Moving a source to ADOPTED means the
extractor reads it, `data/raw/` carries its inventory with a manifest entry, and
`just qc` passes — that is a pull request, with the canary discipline in
`CLAUDE.md`, not a row edit. Editing the row to say ADOPTED without that work
makes `check_source_queue.py` fail, which is the intended behaviour.

## Output

Report: the top three candidates with the gap each closes and what is unverified
about it; anything whose status should change and why; and any source in the
queue that the corpus has outgrown. If the queue is already accurate, say so —
a short honest answer beats a reshuffle.
