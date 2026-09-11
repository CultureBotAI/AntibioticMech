---
name: add-causal-graph
description: Add or improve evidence-backed causal_graphs on existing AntibioticMech YAML records by curating primary-paper mechanism chains. Use add-antibiotic for missing compounds and curate-yaml-record for full record sign-off.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Add an AntibioticMech causal graph

Produce a defensible `causal_graphs` entry for one existing
`AntibioticRecord`: a connected, edge-evidenced path from the compound through
target engagement or transport to the affected molecular function, process,
state, structure, or phenotype.

## Boundaries

- Start from one existing YAML record under `data/antibiotics/<class>/`. If the
  compound is absent, use `add-antibiotic`; if the request is a complete
  scientific review or `REVIEWED` sign-off, use `curate-yaml-record`.
- Verify the record identity before researching a mechanism. A graph for the
  wrong salt, stereoisomer, parent, or duplicate record is worse than no graph.
- Prefer primary experimental papers. Reviews, CARD/ARO, BindingDB and ChEBI
  can guide discovery or support their own source assertions, but a causal edge
  needs a cited source that actually supports that directed relationship.
- Do not upgrade docking, sequence homology, resistant mutant fitness,
  susceptibility, or class membership into direct binding or causation.
- Never invent missing intermediate steps. It is better to draw a shorter
  supported graph than to bridge two well-supported facts with an implied edge.
- Do not create a GitHub issue, PR, comment, email, form, or `@` mention unless
  the user explicitly authorizes that exact outbound action.

## Read First

- `CLAUDE.md` for generated-file boundaries and curation-event requirements.
- `docs/CURATION.md` for evidence semantics and `REVIEWED` criteria.
- `docs/HARMONIZATION.md` for identity and target-scope rules.
- `src/antibioticmech/schema/antibioticmech.yaml` for `CausalGraph`,
  `CausalNode`, `CausalEdge`, `EvidenceItem`, `CausalGraphScopeEnum` and
  `CausalNodeTypeEnum`.
- The whole target YAML and two or three graph-bearing records from the same
  broad mechanism family.

Useful local examples include:

- `data/antibiotics/antibacterial/ciprofloxacin.yaml`
- `data/antibiotics/antibacterial/streptomycin.yaml`
- `data/antibiotics/antimycobacterial/ethambutol.yaml`
- `data/antibiotics/antiviral/nevirapine.yaml`

## Find a Target

Prefer records that already have reviewed target or resistance evidence:

```bash
just worklist --queue mechanism --limit 25
just causal-graph-quality --limit 25
```

For a named target, resolve its path, read the full YAML, and note:

- `identifier`, `label`, `antimicrobial_class` and `chemical_structure`;
- `mode_of_action`, `mode_of_action_target_scope` and notes;
- all `molecular_targets`, `resistance_mechanisms` and `activity_spectrum`
  items;
- existing `causal_graphs`, `discussions` and `curation_history`.

Run a pre-edit baseline without dirtying the checked-in report:

```bash
just validate-strict <record-path> --out /tmp/antibioticmech-causal-validation.tsv
just verify-corpus --summary
```

## Curate the Mechanism

Research the exact compound and the exact target or process in the record.
Search by stable identifiers, important synonyms, target names, gene symbols,
DOIs and PMIDs; treat search output as leads, not evidence. Follow promising
citations to the primary experiment.

Build the graph around source-backed steps:

- Start with a `COMPOUND` node grounded to the record identifier when possible.
- Model a protein target as a family, function or complex. A UniProt accession
  is an organism-specific example; keep it under `MolecularTarget` or in
  `xrefs`, not as the primary `grounding`.
- Use `RNA`, `CHEMICAL`, `CELL_STRUCTURE`, `MOLECULAR_FUNCTION`,
  `BIOLOGICAL_PROCESS`, `TRANSPORT_PROCESS`, `STATE`, `QUALITY` and
  `PHENOTYPE` nodes for the downstream biology the source actually measured.
- Ground nodes with GO, ARO, ChEBI, InterPro, NCBIfam, ComplexPortal or another
  exact CURIE when there is a precise match.
- Use `grounding_status: REVIEWED_LABEL_ONLY` with `grounding_notes` when the
  label is supported but an exact ontology/database term would overclaim.
- Keep `node_id` and `graph_id` stable, local, lowercase and descriptive.
- Every `subject` and `object` must point at a node in the same graph.
- Every edge needs its own `evidence` item. The citation must support the edge,
  not merely mention the compound somewhere in the same paper.
- Set `scope_status: MECHANISTIC` only when the graph is a source-backed
  biological mechanism. Use `NONMECHANISTIC` only for an explicitly reviewed
  classification or measurement context and explain it in `scope_notes`.

Keep wording causal but honest. For example, use "stabilizes a cleavage
complex", "binds the 30S decoding site", "is required for", or "reduces"
only when the source supports that direction and strength. If the source only
shows a correlated mutant or phenotypic rescue, either draw the narrower
supported edge or leave a `Discussion` attached to `causal_graphs#<edge_id>` for
the unresolved step.

## Co-Curate Nearby Fields

Adding the first causal graph often exposes missing or stale mechanism fields.
In the same guarded mutation, update only claims that the same review actually
supports:

- `mode_of_action`, `mode_of_action_target_scope` and `mode_of_action_notes`;
- `molecular_targets` evidence or reviewed target scope;
- a `Discussion` for a concrete unresolved mechanism gap.

Do not set `curation_status: REVIEWED` solely because the graph is complete. The
record qualifies only after identity, structure, class and at least
`mode_of_action` have all been checked under `docs/CURATION.md`.

## Write Through the Guarded Path

Never hand-edit the YAML. Use a narrowly scoped Python mutator under `/tmp`
unless the request is to add reusable tooling:

1. load the target YAML;
2. assert the expected `identifier` and path;
3. append or replace exactly the intended `causal_graphs` entry;
4. update nearby curator-owned fields only when supported;
5. call `record_curation_event(..., curator="codex",
   action="CURATED_CAUSAL_GRAPH", llm_assisted=True, changes=...)`; and
6. write with `write_validated_antibiotic`.

Skip the write and do not append a history event if the source review produced
no substantive record change.

## Regenerate and Verify

After any edit, regenerate the derived surfaces that expose graph count or
rendered graph content:

```bash
just review-queue --limit 0 --tsv curation/record_review_queue.tsv
just render
just docs-stats
```

Then run the record and repository gates:

```bash
just validate-strict <record-path> --out /tmp/antibioticmech-causal-validation.tsv
just verify-corpus
just causal-graph-quality --limit 25
just qc
git diff --check
```

Read the final YAML and rendered page. Confirm that every graph edge is
connected, every edge has evidence on the closest supported claim, label-only
nodes explain their grounding limit, generated counts changed as expected, and
the curation-history event describes the actual diff.

## Report

Report the record path, graph ID, nodes and edges added, PMIDs/DOIs that support
the graph, any nearby mechanism fields changed, gaps deliberately left as
`Discussion` entries, generated files refreshed, causal-graph-quality result,
and every validation command run.
