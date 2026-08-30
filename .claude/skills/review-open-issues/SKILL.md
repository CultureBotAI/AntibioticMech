---
name: review-open-issues
description: Sweep and triage the full open-issue queue for AntibioticMech. Fetches every open issue, checks each against the committed corpus, the inventories, the schema and the code, flags duplicates and stale figures, and assigns a priority tier (P0 something wrong that every gate passes, P1 real-but-schedulable, P2 low-severity/process/doc, P3 backlog). Produces a short ranked report; only writes to GitHub when asked. Use when the user asks to review issues, prioritize the backlog, or triage, or after a review pass files a batch of new issues.
tools: Bash, Read
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Review and prioritize open issues

Adapted from the `review-open-issues` skill in PFASCommunityAgents, which took
its method from the KG-Microbe Mech repos. The full-queue sweep, the
evidence-over-vibes rule and the read-only default are theirs. What a check
consists of is different here, because this repository's issues are about a
generated corpus and the pipeline that produces it.

## Overview

**Purpose**: an honest, current ranking of the whole open-issue queue.

**When NOT to use**: for choosing the next data source — that is the
`source-queue` skill — or for `NEXT_TASKS.md` upkeep. This skill ranks; it does
not implement fixes.

## What makes this repo different

**1. Almost every claim is checkable on a bare clone, so check it.**
Unlike its sibling repos, this one commits its evidence: the inventories in
`data/raw/`, all record YAMLs under `data/antibiotics/`, the generated site in
`pages/`, and the lockfile and retired-slug ledger. An issue asserting something
about a record, a role, a slug or a count can be answered by reading the file —
there is no excuse for ranking one on impression. The single exception is
`downloads/`, the raw ChEBI and CARD releases, which is gitignored: an issue
about *extraction* semantics may need `just extract-inventory` without
`--offline` to reproduce, and that is a network fetch worth saying out loud.

**2. A green gate is not evidence the code is right.**
This is the repository's defining failure mode and the one that sets P0. Nineteen
defects were found in a single review pass while `just qc` was green, 54 tests
passed and `verify-corpus` reported zero drift — because the corpus faithfully
reproduced computations that were wrong. Roles were being dropped, `ANTIBIOTIC_EFFLUX`
was structurally unassignable, and unreviewed upstream assertions were being
honoured, all with every check passing. So: run the gates, and then check the
*claim* independently of them. "QC is green" answers a different question from
"the corpus asserts the right thing".

**3. Figures drift fast, and issues quote figures.**
The corpus went 2,603 → 2,469 → 2,923 records inside one working session, as a
trust filter tightened and a scope decision widened. An issue quoting a record
count, a class breakdown or a coverage percentage may be describing a corpus
that no longer exists. Re-derive every number before repeating it, and say so
when a title has drifted.

**4. Some issues are blocked on someone who is not us.**
Three distinct kinds, none of them stalled engineering work, and none rankable
as if a contributor could pick them up and finish:
- **Owner decision** — e.g. the licence question (#27), or which label a record
  should carry (#6). No amount of code resolves these.
- **Upstream terms** — e.g. `card.json`, which needs a McMaster waiver, not a
  patch (`curation/source_queue.tsv`).
- **Upstream data** — e.g. CARD giving two different peptides PubChem CIDs that
  resolve to one structure. The corpus flags these with a `CURATION_TODO`
  discussion; the fix belongs to the provider.

## Workflow

### Step 1 — Fetch the full open-issue queue

```bash
queue_file="${TMPDIR:-/tmp}/antibioticmech-open-issues.json"
gh issue list --state open --limit 5000 \
  --json number,title,body,labels,comments,createdAt,updatedAt > "$queue_file"
jq -r '.[] | [.number, .createdAt[:10], (.labels|map(.name)|join(",")), .title] | @tsv' "$queue_file"
jq length "$queue_file"
```

`--limit` silently caps with no warning. Print `jq length` and state whether
coverage was complete. Read from the saved JSON rather than the TSV overview:
bodies and comments carry the evidence, and a "this is already fixed" note is
usually in a comment.

### Step 2 — Establish what is true right now

Once, before checking any corpus-shaped issue:

```bash
just qc                 # every gate: lint, docs, provenance, tests, validation,
                        # reproduction, source queue, generated site
just report             # live per-class counts and field coverage
just worklist           # the curation backlog by queue
git log --oneline -8    # what has landed since the issues were filed
```

**If `just qc` fails, say so before ranking anything.** A red gate does not
invalidate the sweep, but every corpus-derived verdict in it is then provisional
and must be reported as such — and the failure is usually a finding in its own
right.

**If `just qc` passes, do not treat that as agreement with any issue's claim.**
See point 2 above. The gates prove the corpus reproduces from its inputs; they
prove nothing about whether the inputs were read correctly.

Then classify each issue's evidence:

- **Checkable from the committed tree** — a record, a role, a slug, a count, a
  schema rule, a test. Measure it; most issues here are this.
- **Needs an upstream fetch** — extraction semantics against a ChEBI or CARD
  release that is not in `downloads/`. Say so, and say whether you fetched.
- **Code-only** — read the code and ignore the corpus.
- **Blocked on a person or a provider** — see point 4; do not rank as actionable.

### Step 3 — Group and dedupe

Issues filed from one review pass overlap constantly. Group by shared root
cause, same script, or near-identical failure scenario, and report a group as
one item with a shared fix.

The recurring **families** in this repository, all seen in real issues:

- **Something wrong that every gate passes.** The dominant family. Roles
  silently dropped while `activity_roles` was documented as complete (#7);
  unreviewed upstream edges honoured as if curated (#8); an enum value made
  structurally unassignable by an incomplete graph walk (#10).
- **Silent loss of curator work.** A re-seed that discards curated fields
  because a record moved directory (#9); a stale-CARD-row heuristic that deleted
  a curator's own citation (#16).
- **A claim the code does not deliver.** A documented invariant with no
  enforcement, a referenced script that does not exist (#4), a scope statement
  the config contradicts, a figure that has drifted.
- **A safety rail that is not one.** A canary that exits 0 having made no call
  (#14); a batch that loses completed work on a crash (#12); a destructive
  `--out` with no guard (#21).
- **Identity and provenance limits.** InChIKey collisions and non-collisions
  (#28); minted-vs-grounded resolution; retired slugs (#24).

### Step 4 — Check each issue against current reality

- **Already fixed?** `git fetch origin`, then
  `git log --oneline origin/main --perl-regexp --grep "#<N>\b"`. The `\b` is
  required — plain `--grep "#2"` also matches `#28`. Also check the working
  branch: this repository's scaffold work lives on a branch and `main` may be
  behind, so a fix can be real and absent from `main`.
- **Closed by a merged PR?**
  `gh issue view <N> --json closedByPullRequestsReferences`, then check
  `mergedAt` per candidate. `Closes #A and #B` only auto-closes `#A`.
- **Still reproducible?** Prefer a command over a reading. Examples that answer
  real issues in this queue:
  ```bash
  # does a record still carry the role the issue says it lost?
  python3 -c "import yaml;d=yaml.safe_load(open('data/antibiotics/antifungal/carvacrol.yaml'));print(d['activity_roles'])"
  # is a mechanism category still unassignable?
  cut -f6 data/raw/aro_resistance_edges.tsv | sort | uniq -c | sort -rn
  # has a figure in a title drifted?
  just report | head -12
  # is a retired slug still reserved?
  cut -f2 data/antibiotics/RETIRED.tsv | grep -x "<slug>"
  ```
- **Title still true?** Titles carry figures and figures move here faster than
  anywhere. Re-derive before repeating.

### Step 5 — Assign priority

- **P0 — something wrong that the gates do not catch.** A record asserting
  something the sources do not support; a claim about redistribution rights; a
  path that silently destroys curated work. The signature is *invisible*
  wrongness: `just qc` green, tests passing, and the corpus still saying
  something untrue. Every one of the four high-severity findings in this repo's
  history had exactly that shape.
- **P1 — real, schedulable.** A defect visible when it bites: a crash, a
  destructive flag, a gap in a gate over risky code.
- **P2 — low-severity, process, or doc.** Drift, cleanups, stale references.
- **P3 — backlog.** Real, not scheduled, kept as a record.

Orthogonal to severity, and worth stating in the report even though no label
exists for it yet: **blocked-on-owner**, **blocked-upstream**. A P2 blocked on a
provider is still P2, but nobody should pick it up expecting to finish.

Use P0 sparingly. If more than ~10% land P0, recalibrate. Note that this
repository has no `P0`–`P3` labels — only GitHub's defaults. Creating them is a
write action; propose it, do not assume it:

```bash
gh label create P0 --description "Wrong in a way the gates do not catch" --color b60205
```

### Step 6 — Present the report

- Ranked list, P0 first, one line per issue or group, with number and a
  one-sentence why.
- **Separate "fixed in code" from "blocked on a decision"** — different states,
  and both differ from "still open and actionable".
- List issues recommended for closing, each with evidence: a commit, a PR, a
  command and its output. Never "this looks done".
- **Recommend a top 2–3** to act on next, with reasoning.
- State how many issues were reviewed and whether coverage was complete.
- Say which verdicts were re-derived from the current corpus and which were not.

### Step 7 — Act only when asked

Read-only by default. A general "yes, go ahead" is not blanket approval for an
unattended close loop.

- **Closing**: confirm the evidence first, then
  `gh issue close <N> --comment "<evidence>"`, one at a time.
- **Relabelling** is lower risk than closing but still a write; batch it into one
  message and say what changed.
- **Retitling** when a figure has drifted is worth doing; the comment should say
  what the number was and why it moved.

## Conventions this skill enforces

- **Full-queue coverage, not first-page sampling.** State the count.
- **Re-derive every figure.** Counts in this repository move under you.
- **Evidence over vibes.** Every CLOSE, STALE or duplicate recommendation cites
  a commit, a PR, or a command and its output.
- **A green gate is not a verdict on a claim.** Check the claim.
- **Unknown stays unknown.** Never rank on a measurement that could not be taken.
- **P0 means silently wrong**, not loudly broken.
- **Read-only by default.**

## Notes and limitations

- Keep `comments` in Step 1's `--json` list.
- Merging and closing stay the user's call; prior approval of one is not
  approval of the next.
- No @-mentions in comments without explicit per-mention authorization
  (standing rule).
- This skill ranks; it does not merge, push, or edit files under review.
- The queue is small enough to read in full. Prefer reading every body over
  pattern-matching titles — titles are the part that drifts.

## Related

- `just qc` — the authoritative gate; Step 2 depends on it.
- `just report`, `just worklist` — live figures and the curation backlog.
- `curation/source_queue.tsv` and the `source-queue` skill — for issues that are
  really "should we adopt source X?".
- `docs/HARMONIZATION.md`, `docs/CURATION.md` — the invariants an issue may be
  alleging a violation of.
- `NEXT_TASKS.md` — owed work; an issue duplicating a NEXT_TASKS item should say so.
