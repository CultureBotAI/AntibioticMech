# Curation history

Append-only provenance for curation sessions. **One record per change** — per
target for hand curation, per *migration* for a bulk edit. Written once and
**never edited afterwards**; corrections go in a new record that references the
old one in its `details`.

```
history/<kind-dir>/<slug>/<TIMESTAMP>-<actor>-<shortid>.yaml
```

The schema (`src/antibioticmech/schema/history.yaml`) and the scaffolder's
contract are vendored from culturebotai-claw; the scaffolder and validator were
ported from CellStructureMech. The conventions below are this repository's.

## Why this exists

Per-record `curation_history` — the `CurationEvent` list that
`record_curation_event` appends inside an `AntibioticRecord` — says what changed
inside one record. It cannot say that a source's licence was re-read at the
source, that a gate was adopted and what it found, or that a review found an
issue requiring later curation. Git says a commit happened; it does not say
which model, using which tool, changed what, why, and under which issue. That
gap matters more as agents do the changing. The two layers complement each
other: a record mutation still appends its `CurationEvent`, and the session that
made it also writes one record here.

## Why the layout looks like that

Directory-per-slug plus a `shortid` hashed from the record's target, summary and
details (claw's own scaffolder draws a random one): two agents working the same
compound concurrently write different files unless they write an identical record
in the same second, so this layer has **no merge-conflict surface**. A shared
changelog would conflict on every parallel PR.

## Writing a record

Do not hand-write the filename or timestamp — scaffold it:

```bash
just new-history --kind record --slug erythromycin-a \
  --target-root data/antibiotics/antibacterial \
  --event EDIT --outcome changed \
  --sections causal_graphs \
  --summary "Add a primary-paper causal graph for ribosomal binding" \
  --actor-name claude-code --model claude-opus-5-5 --agent-tool claude-code \
  --issue https://github.com/CultureBotAI/AntibioticMech/issues/<n> \
  --details "What was done, what evidence was used, how it was validated."
```

Omit `--details` and you get a TODO placeholder — `just validate-history`
**fails** while it is still there, so an unfilled record cannot slip through.
The command prints the record path as its final stdout line.

**Name the actor that actually ran.** `--actor-name` defaults to `claude-code`,
and that name is also the filename's actor token. Pass it explicitly — `codex`
for a Codex session, a GitHub login with `--actor-type human` — together with
`--model` and `--agent-tool`, so the three agree. The scaffolder refuses to keep
the default when `--actor-type`, `--agent-tool` or a non-Claude `--model` says
otherwise; an explicit `--actor-name` is written as given, so check
`session.actors` before committing.

A record's slug is its filename stem: the `slug` column of
`data/antibiotics/PATHS.tsv`, verbatim, Greek letters included (`β-punicalagin`
and `punicalagin` are different records with different history directories).
`--target-root` is the record's class directory, `data/antibiotics/<class-dir>`.
`--kind record` and `--kind schema` derive the target path from `--slug` plus
`--target-root`. Every other kind should pass an explicit `--path`: only those
two are reliably `.yaml` (a decision is a `.tsv` row, a research note an `.md`,
infrastructure a justfile or workflow).

Then validate and stage:

```bash
just validate-history history/records/erythromycin-a/<file>.yaml
git add history/
```

## The vocabulary

`event`: `CREATE` · `EDIT` · `REVIEW` · `AUDIT` · `GENERAL`

`outcome`: `changed` · `no_change` · `needs_followup` · `blocked`

Outcome is **orthogonal** to event on purpose. A `REVIEW` that found nothing is
`no_change`, a real result that records something was checked. An `EDIT` that
hit a wall is `blocked`, and `details` must say what the wall was so the next
session does not rediscover it.

`kind`: `record` · `schema` · `mapping` · `report` · `infrastructure` · `other`
(`other` requires an explicit `--path`).

A review or audit request changes no record, status or curation history; it
saves a structured review under `reviews/structured/` instead (see
[the review profile](../docs/record-review-profile.md)), and needs no record
here. Curation that a review leads to, once separately authorized, writes the
`CREATE`/`EDIT` record for its actual change.

## One record per CHANGE, not per file

For hand curation the session and the target coincide: one compound is reasoned
about and one record is written. For a mechanical change across many records —
a re-seed, an upstream refresh, a re-render, a schema migration — write **one
record for the migration**, with `--kind infrastructure` or `--kind schema` and
the script as the target. A record per touched file would bury the reasoning in
copies of itself.

`data/antibiotics/` is generated, so a change to it usually starts in a curated
input. Record the session against what it was about:

| what happened | `--kind` | target |
|---|---|---|
| one record's curated fields — targets, mechanism, causal graph, resistant taxa | `record` | that record's YAML |
| a new curated structure in `curation/curator_antibiotics.tsv` | `record` (`--event CREATE`) | the record the seeder emits for it |
| a grounding or exclusion decision | `mapping` | `curation/decisions.tsv`, with `--slug` naming the record it concerns |
| a bulk edit, re-seed or upstream refresh | `infrastructure` | the script that made it |
| a schema change | `schema` | the schema file |
| a source adopted or re-ranked | `other` | `curation/source_queue.tsv` |
| a research note | `other` | the note under `research/` |

## What is checked

`just validate-history` — also a step of `just qc`, so CI runs it — validates
every `.yaml` or `.yml` file under `history/` against the vendored schema, and
checks that issue and PR links are absolute URLs. **Validity is blocking**: a
record that exists must pass. **Presence is advisory**: nothing fails when a
change arrives without a record; the expectation is stated in `CLAUDE.md`.
Records are append-only by convention, not by a gate; a corrected record is a
new record that names the old one.
