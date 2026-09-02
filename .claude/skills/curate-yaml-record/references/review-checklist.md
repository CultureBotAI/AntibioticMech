# AntibioticRecord review checklist

Use this checklist to make claim-level decisions for one record. It is not a
requirement to populate every optional slot.

## Evidence standard

- Put evidence on the narrowest object it supports. `MolecularTarget`,
  `ResistanceMechanism`, `ActivityObservation`, and every `CausalEdge` require
  their own `evidence`; record-level evidence does not satisfy that obligation.
- An `EvidenceItem.reference` should be a stable `PMID:...`, `DOI:...`, database
  CURIE, or official URL. Confirm that the identifier resolves to the inspected
  source and that the source concerns the exact compound form.
- A `snippet` is a short verbatim passage, not a paraphrase. Use `notes` for the
  curator's interpretation, limitations, model system, or the fact that an
  assertion comes from a database rather than primary literature.
- Cite a database assertion as a database assertion. CARD/ARO evidence does not
  become primary literature merely because the assertion is plausible.
- Reviews are useful for vocabulary and citation discovery. Prefer the cited
  primary experiment for the actual mechanism, target, activity, or resistance
  claim.
- Preserve disagreement. When reliable sources conflict, narrow the claim or
  capture a `CONTROVERSY`; do not silently choose the convenient source.
- Negative search results mean "not found in the bounded search," not "no
  evidence exists." State the query/provider/date when that distinction matters.

## Field-by-field audit

| Area | Verify | Complete enough when |
|---|---|---|
| Identity | `identifier`, label, synonyms, `grounding_status`, source concepts, and exact chemical form agree. | The record denotes one individual structure and any minted identity has an explicit rationale or queued decision. |
| Structure | SMILES, Standard InChI, InChIKey, formula, charge, masses, source, and retrieval date are mutually consistent. | The InChIKey is valid and the source record is the same salt/stereo/charge form. |
| Equivalence | Every `xref` denotes the same structure; every `parent_compounds` value is strictly broader. | No class, conjugate, salt, stereoisomer, patent, article, or macromolecular structure is asserted as exact chemical identity without a documented allowed exception. |
| Classification | `antimicrobial_class` is a filing choice and `activity_roles` preserves every source-supported activity role. | The class follows repository priority without erasing additional roles; no activity is inferred only from a chemical family. |
| Mode of action | The enum matches compound-specific evidence; notes identify seeder versus curator ownership. | A defensible mode exists with honest provenance, or a curator veto explicitly leaves it blank. |
| Target scope | `MICROBIAL_TARGET` versus `HOST_SHARED_TARGET` describes the target of the asserted mode, not confidence or clinical selectivity. | The scope is source-supported or deliberately left empty after a curator-owned mechanism change. |
| Molecular targets | Target identity/type/relation, taxon and strain, experimental context, evidence status, source version/date, measurements, and protein examples are appropriately scoped. | Each target has claim-level evidence; direct binding is asserted only from direct evidence; the target is a family, complex, or function and organism-specific UniProt records remain examples. |
| Activity | Organism/strain, outcome, assay, value, qualifier, and units match the experiment. | Every observation has evidence, and every MIC has both units and method. Do not generalize one strain to a species-wide spectrum. |
| Resistance | Mechanism type, ARO grounding, label, gene family, organism/context, and evidence agree. | Each route has claim-level evidence and phenotype association is not overstated as a biochemical mechanism. |
| Producer | Taxon and strain truly biosynthesize the compound rather than merely transform, resist, or respond to it. | Each claim has a citation or MIBiG BGC; MIBiG provenance and review/version fields remain intact. |
| Clinical status | Substance identity is separate from product, jurisdiction, application, and marketing state. | The official source supports the exact product/substance assertion and its retrieval/version metadata is present. |
| Causal graph | Nodes represent the right entity types; edges connect declared nodes and state only source-supported direction and causality. | Every edge has evidence and the graph distinguishes mechanistic biology from classification or measurement context. |
| Datasets | Dataset is public, specifically relevant, and identified by accession or durable URL. | Relevance and associated publication/evidence are clear; the field is not a bibliography dump. |
| Discussions | Prompt describes a concrete unresolved question, conflict, or consequential curation task. | It has a stable local ID, kind/status, rationale, and citations when the gap itself is evidence-based. |
| Audit | Status and history match what was actually checked and changed. | The latest event is accurate, transparent about LLM assistance, and REVIEWED is used only after all sign-off criteria pass. |

## Generated versus curator-owned changes

Seeder-owned fields include identity, label/definition, synonyms,
`parent_compounds`, `xrefs`, class and roles, structural class, chemical
structure, source concepts, and grounding status. Fix these through the
committed inventory, extractor, seeder, or `curation/decisions.tsv`, then
re-seed. Do not make a record-only correction that the next seed run will undo.

Curator additions can include evidence, activity, producer claims, mechanism
graphs, datasets, discussions, and literature-backed additions beside imported
targets or resistance mechanisms. Imported slices remain source-owned: add a
curator-supported item or replace an assertion only according to the merge and
provenance rules; do not disguise a database row as hand-curated literature.

For any record mutation, load YAML and finish with both repository helpers:

```python
from pathlib import Path

import yaml

from antibioticmech.curate.curation_event import record_curation_event
from antibioticmech.validation.write_validated import write_validated_antibiotic

path = Path("data/antibiotics/<class>/<slug>.yaml")
doc = yaml.safe_load(path.read_text(encoding="utf-8"))
assert doc["identifier"] == "<expected CURIE>"

# Apply only the source-checked curator-owned changes here.

record_curation_event(
    doc,
    curator="<actual agent identifier>",
    action="RECORD_CURATED",
    changes="Describe the exact evidence-backed changes and unresolved gaps.",
    llm_assisted=True,
)
write_validated_antibiotic(doc, path)
```

Put a one-off mutator under `/tmp`, not in the repository, unless reusable
curation behavior and tests are themselves part of the requested change. Review
the object-level diff before writing. If no substantive field changed, do not
write and do not append an event.

## REVIEWED gate

`REVIEWED` means all four repository sign-off criteria have passed:

1. The label, exact structure, and ChEBI grounding or minted-identity rationale
   are correct.
2. SMILES, InChI, InChIKey, formula, and source describe the same structure.
3. Filing class and all retained activity roles match source assertions.
4. At least a mode of action has been checked; known molecular targets carry
   real citations.

A complete causal graph is a goal, not a prerequisite. Conversely, a long list
of citations does not compensate for an unresolved identity conflict. Leave the
record `SEEDED` or `PROPOSED` and report blockers whenever a gate is unmet.

For a multi-record request, regenerate `curation/record_review_queue.tsv` after
each batch. The queue must contain every record that is neither `REVIEWED` nor
`DEPRECATED`; it is a checkpoint, not evidence that any listed claim was read.
