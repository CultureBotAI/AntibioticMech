---
name: curate-yaml-record
description: Review and curate one AntibioticMech compound YAML record for scientific accuracy, claim-level evidence, completeness, and resolvable gaps. Use when asked to audit, improve, complete, add evidence to, or mark an individual antibiotic record REVIEWED; do not use for bulk source ingestion or as permission to contact anyone or mutate GitHub.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 2.0.0
---

# Curate one AntibioticMech YAML record

Produce a scientifically defensible record and an explicit account of what is
supported, corrected, still missing, and genuinely unknown. Search results are
leads; only inspected sources can support a claim.

## The contract

<!-- canonical:begin the-contract -->
Produce a defensible record and an explicit account of four things: what is
**supported**, what was **corrected**, what is **still unresolved**, and what is
**genuinely unknown**. The last two are different — a gap you searched for and
could not close is a finding; a gap you did not look at is not.

**One target.** Resolve exactly one record before touching anything. If a label
matches several, or a request names a family rather than a member, stop and
disambiguate. Silently substituting a similar record is the error that no later
check catches, because everything downstream is then correct about the wrong
thing.

**Audit preserves scientific inputs. Curation authorises edits to the named
record only.** A review or audit request changes no scientific record, status,
or curation history. It does save a new timestamped structured review through
`docs/record-reviews.md` and the native rubric in `docs/record-review-profile.md`.
A curate, improve, complete, correct or add-evidence request authorises local edits to that record and the smallest
maintained path its provenance requires — not to neighbours, not to whatever
else looked wrong on the way.

**Search results are leads. Only an inspected source supports a claim.** A
search hit, a deep-research report, a rendered page, and a generated artifact are
each somewhere to look, and none is evidence. Evidence is text you read in the
source, attached to the narrowest assertion it actually supports.
<!-- canonical:end the-contract -->

## Structured audit output

For a review, audit, or assessment request, apply the scientific checklist below
without taking the curation write steps. Follow [docs/record-reviews.md](../../../docs/record-reviews.md)
and [the local profile](../../../docs/record-review-profile.md): capture target
and maintained-input hashes before judging, then save the assessed result with
`uv run python scripts/record_review.py validate <completed-review.yaml>` and
`uv run python scripts/record_review.py save --content <completed-review.yaml>`.
The output is `reviews/structured/<YYYYMMDDTHHMMSSZ>-<slug>/review.yaml` plus its
derived `review.md`; link both in the final response. Preserve actual check
results, evidence, scope, unresolved findings, and unavailable checks. Use a
partial/blocked review when required checks are unavailable after assessment.
Do not append curation/history events or promote native status from an audit.

Worklists, sampling output, source searches, and raw provider drafts are inputs
to review, not completed scientific reviews. Keep their selection rules and
population denominators when assessing a sample; deterministic-only inspection
uses `scientific_review: false`. A queue checkpoint never substitutes for the
validated saved bundle. Existing curation write and scientific sign-off gates
below still apply when curation is explicitly requested.

## Boundaries

- Resolve one target under `data/antibiotics/<class>/<slug>.yaml`. If a name
  matches multiple structures, stop and disambiguate before changing anything.
- A request to review or assess is read-only. A request to curate, improve,
  complete, correct, or add evidence authorizes local edits to the named record
  and the smallest necessary repository-owned provenance path.
- Never create or edit a GitHub issue, PR, comment, discussion, email, form, or
  message, and never add an `@` mention, without explicit authorization for
  that exact outbound action. Read-only literature and database requests are
  allowed when they are needed for the requested curation.
- Do not transmit a contact email as API metadata. In particular, unset
  `NCBI_EMAIL` for publication discovery unless the user explicitly authorizes
  sending it. Google Scholar via SerpAPI may be billable; use it only with
  explicit approval.
- Preserve unrelated work. Follow `CLAUDE.md`: work on a branch before editing,
  and use a separate worktree when the current checkout is dirty or occupied.
- Never infer that a missing optional field is false. Never fill a field merely
  to improve coverage.

## Read before judging the record

Read the target record and these repository contracts:

- `CLAUDE.md`
- `docs/CURATION.md`
- `docs/HARMONIZATION.md`
- the relevant classes and enums in
  `src/antibioticmech/schema/antibioticmech.yaml`
- [references/review-checklist.md](references/review-checklist.md)

Check the record's `source_concepts` against the committed inventories and
`curation/decisions.tsv`; do not treat the rendered page or generated prose as
an independent source.

## Workflow

### 1. Establish a baseline

Read the entire YAML, not selected fields. Record its identifier, InChIKey,
grounding state, source concepts, curation status, existing citations, and
existing discussions. Run closed-schema validation without dirtying the normal
report:

```bash
just validate-strict <record-path> --out /tmp/antibioticmech-record-validation.tsv
just verify-corpus --summary
```

Inspect relevant worklist entries, especially `mechanism`, `moa-scope`,
`target-evidence`, `xref-unverified`, `xref-span-conflict`, `multi-component`,
and `producer-candidate`. A green gate establishes structural consistency, not
scientific truth.

For a bulk request, still review records one at a time. Generate the exhaustive
checkpoint with:

```bash
just review-queue --limit 0 --tsv curation/record_review_queue.tsv
```

Remove a row only by actually moving its record to `REVIEWED` or `DEPRECATED`;
the queue is derived state. Its source references are discovery leads, not
claim evidence, and readiness labels are triage rather than scientific
sign-off.

### 2. Verify identity and structure first

Do not research a mechanism until the record is known to denote the intended
individual chemical structure. Check label and synonyms, identifier grounding,
salt/parent/stereoisomer boundaries, source-concept agreement, and consistency
among SMILES, Standard InChI, InChIKey, formula, charge, and masses.

Prefer structure registries and the record's authoritative upstream sources for
identity. A name match alone is insufficient. An xref must denote the same
structure; a drug class belongs in `parent_compounds`; an organism-specific
protein accession is not a compound identifier.

If a seeded identity, structure, classification, source concept, or xref is
wrong, correct its inventory, extractor, seeder, or the applicable row in
`curation/decisions.tsv`. Do not patch a generated field in the record.

### 3. Review every existing scientific claim

For each claim, ask whether the cited source supports this exact compound,
relationship, organism/context, and strength of wording. Check citations rather
than assuming a plausible mechanism is correct. Distinguish:

- an upstream database assertion;
- a primary experimental publication;
- a review or other secondary summary; and
- a search-result snippet, which is discovery metadata and not evidence.

Prefer primary experimental papers for molecular targets, activity,
resistance, producers, and causal edges. Use official regulatory or database
records where those are the claim's actual authority. Verify PMID/DOI identity
and inspect the abstract or full text far enough to establish support. Keep any
verbatim `snippet` short, exact, and attached to the closest supported claim.
Do not upgrade correlation, susceptibility, docking, or class membership into
direct binding or causation.

Use the repository adapters for candidate discovery when useful:

```bash
env -u NCBI_EMAIL uv run python scripts/search_publications.py \
  --provider pubmed --provider semantic-scholar \
  --query '<compound names plus the claim being checked>' \
  --limit 20 --output /tmp/antibioticmech-publications.jsonl
```

Search by exact label, important synonyms, identifiers, and targeted claim
terms rather than one broad query. Follow promising citations backward to the
primary report. Do not cite the normalized search output itself.

### 4. Assess completeness and address supported gaps

Apply the field-by-field checklist. Attempt to resolve material gaps with
bounded, targeted searches. Add information only when the exact assertion is
supported and representable without stretching the schema.

Prioritize gaps that determine whether the record can be trusted:

1. identity and structure conflicts;
2. unsupported or overstated existing claims;
3. missing mechanism and target evidence;
4. missing scope/context on mechanistic and activity claims;
5. resistance, producer, activity, clinical, and causal detail that a source
   specifically reports.

Do not add a generic `Discussion` for every empty optional field. Add one only
for a concrete unresolved conflict, evidence gap, or curation task whose
resolution would materially change the record. State what is unknown, why it
matters, what was checked, and what evidence would resolve it. Do not propose
experiments when a literature or identifier check is the actual next step.

### 5. Write through the guarded path

Never hand-edit a record and never serialize it directly. For curator-owned
fields, use a narrowly scoped temporary or checked-in Python mutator that:

1. loads the existing YAML;
2. asserts the expected record identifier and path;
3. makes only the reviewed changes;
4. calls `record_curation_event` from
   `antibioticmech.curate.curation_event` with a specific action and change
   summary, and `llm_assisted=True` for agent-produced changes; and
5. writes with `write_validated_antibiotic` from
   `antibioticmech.validation.write_validated`.

Do not append a history event when the document is otherwise unchanged. Use the
actual agent identifier (`claude` in Claude Code, `codex` in Codex) when no
human curator identity was supplied; never attribute an agent's judgement to
the user.

`mode_of_action`, its target scope, and its notes are one claim. When taking
ownership from the seeder, follow `docs/CURATION.md`: retain or replace the
provenance honestly and include an actual `CURATOR:` statement. A veto leaves
`mode_of_action` empty and explains why. Do not infer target scope from class.

Set `curation_status: REVIEWED` only when identity, structure, class, and at
least the mode of action have all been checked to the standard in
`docs/CURATION.md`. Otherwise preserve the existing status and report the
blocking gaps. A record may be materially improved without being REVIEWED.

### 6. Verify and report

After any edit, run:

```bash
just validate-strict <record-path> --out /tmp/antibioticmech-record-validation.tsv
just verify-corpus
just qc
git diff --check
git diff -- <record-path> curation/decisions.tsv src scripts tests
```

Read the resulting YAML again. Confirm citations sit on the claims they support,
the audit event accurately describes the diff, and no seeded field drifted.

Report:

- corrections and additions, with the supporting PMID, DOI, database record,
  or official URL;
- claims checked and retained;
- remaining gaps, including searches that did not resolve them;
- whether the record qualifies as REVIEWED and why; and
- validation and test results.

Do not create an issue for a remaining gap unless the user separately asks for
that GitHub mutation.
