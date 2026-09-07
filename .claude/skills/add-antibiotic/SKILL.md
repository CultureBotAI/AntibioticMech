---
name: add-antibiotic
description: Add a missing AntibioticMech compound by proving it is one exact antimicrobial structure and making the seeded corpus reproduce it. Use for a named compound or publication lead; use curate-yaml-record for an existing YAML record and source-queue for source ranking.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Add a new AntibioticMech compound

Produce the first reproducible `AntibioticRecord` for one missing antimicrobial
compound. Search hits and papers are leads; only an exact source concept with an
individual structure can become committed YAML.

## Boundaries

- Accept only one chemical structure with a Standard InChIKey and evidence of
  antimicrobial activity.
- Reject mixtures, combination drugs, drug classes, scaffolds, extracts,
  structureless names, and evidence for a salt, fragment, conjugate or
  stereoisomer that is not the exact structure being added.
- If the compound already has a YAML file under `data/antibiotics/`, switch to
  `curate-yaml-record`.
- If the source is missing from the reproducible pipeline, add the extractor or
  stop with a source-adoption issue. Do not hand-write a one-off YAML file.

## Read first

- `CLAUDE.md` for generated-file boundaries and canary discipline.
- `docs/HARMONIZATION.md` for the chemical-identity and merge model.
- `docs/CURATION.md` for `PROPOSED`, evidence and review semantics.
- `src/antibioticmech/schema/antibioticmech.yaml` for required fields.
- `scripts/seed_from_sources.py` and `scripts/verify_corpus.py` for the fields
  the seeder owns and the committed-corpus reproduction check.
- Two or three close records from the same antimicrobial class.

## Prove the compound is missing

Use exact, narrow searches and include ignored files whenever a search result is
used to prove absence:

```bash
rg --hidden --no-ignore -n -F "<Standard InChIKey>" . -g "!/.git" -g "!/.venv"
rg --hidden --no-ignore -n -F "<CHEBI or ARO id>" data curation .claude -g "!/.git" -g "!/.venv"
rg --hidden --no-ignore -n -F "<DOI or PMID>" . -g "!/.git" -g "!/.venv"
```

Search the proposed label, exact synonyms, CAS numbers, PubChem CIDs, CHEBI and
ARO CURIEs, DOI, PMID, and Standard InChIKey. Also inspect
`data/antibiotics/PATHS.tsv` and `data/antibiotics/RETIRED.tsv`; a live record,
a retired slug, or a skipped source concept changes the work from addition to
grounding, source repair, or curation.

Never use a broad pattern such as `CHEBI:` or `10.` to prove absence. If an
exact label has punctuation or spaces, pass it through `rg -F` rather than a
regular expression.

## Choose the source path

New committed records must be emitted by `scripts/seed_from_sources.py` from a
versioned input. Pick the narrowest reproducible path that covers the compound:

- **Already in ARO inventories but structureless.** Add the missing exact
  structure by the PubChem fallback only when CARD supplies a CID for the same
  ARO molecule: `just extract-pubchem-dry`, then
  `just extract-pubchem-canary <ARO_ID>`, inspect `data/raw/pubchem_structures.tsv`,
  and seed that identifier.
- **Present in a newer ChEBI or ARO release.** Refresh upstream inventories with
  `just extract-inventory-dry`, `just extract-inventory`, the PubChem canary if
  new ARO-only concepts need structures, and a seed canary before the batch.
- **Present only in another redistributable structured source.** Add or extend
  an extractor so `conf/sources.yaml`, `SourceEnum`, `data/raw/`,
  `data/raw/MANIFEST.yaml`, source concepts, structures and provenance reproduce
  offline.
- **Present only in a paper or in a restricted/name-only source.** Do not add a
  record. File the exact source gap or use `source-queue`; the current corpus has
  no direct curator-entry inventory for `CURATOR` records.

## Identity and structure

Every source concept needs a stable native `source_id`, `source_label`,
`source_version`, and `minted_identifier`. Use the same deterministic minting
style as the seeder: source plus native identifier, never the output slug or a
mutable display label.

Grounding follows the existing merge rules:

- use the ChEBI CURIE and `grounding_status: EXACT` when ChEBI itself supplies
  the exact default structure;
- merge a CARD/ARO concept into that ChEBI record only when the ChEBI
  cross-reference survives the exact cross-reference checks;
- keep an `antibioticmech:` CURIE and `grounding_status: MINTED` when no
  defensible ontology identity exists;
- leave `grounding_status: REVIEW_NEEDED` only for an exact structure whose
  ontology identity needs human adjudication.

Preserve the structure source's own SMILES or InChI and derive the Standard
InChIKey from the same structure. Parent compounds are strictly broader;
salts, stereoisomers, conjugates and prodrugs are different records unless the
source and structure prove exact identity.

## Evidence bundle

The first emitted record should keep the `curation_status` set by its emitter:
`SEEDED` for adopted-source inventories and `PROPOSED` only for a future direct
curator-entry lane. Add only fields supported by the source path:

- `label`, `identifier`, `antimicrobial_class`, `source_concepts`,
  `chemical_structure.standard_inchi_key`, `grounding_status`, and
  `curation_status` are required for a usable first record.
- `activity_roles` and `structural_class` come from a source assertion, not a
  family-name guess.
- `mode_of_action`, `molecular_targets`, `resistance_mechanisms`,
  `activity_spectrum`, `producer_organisms`, `clinical_status_assertions` and
  `causal_graphs` need claim-level evidence on each object.
- unresolved ambiguity belongs in a `Discussion`, not in over-specific fields.

## Write through the generator

Update the reproducible input or extractor first, then run:

```bash
just seed
just seed-canary <IDENTIFIER>
```

Inspect the canary YAML and object diff. The seeder should append a
`record_curation_event`, assign the slug with `assign_slugs()` and
`write_lockfile()`, and write the YAML through `write_validated_antibiotic()`.
Fix that path if any of those steps are missing.

After the canary is correct:

```bash
just seed-apply
just chemical-map
just embed
just embed-map
just render
just docs-stats
just qc
```

If the change is source adoption rather than record addition, also verify the
source queue and provenance:

```bash
just source-queue
just provenance-check
```

`pages/**`, `data/embeddings/chemical-structure-map.json`, and
`data/embeddings/corpus_map.json` are generated. Rebuild them; do not edit them
by hand.

## Report

Report the accepted structure and its InChIKey, the source concept that emitted
it, all exact duplicate searches performed, the file path assigned in
`data/antibiotics/PATHS.tsv`, the claim-level evidence added or deliberately
left empty, and every validation command run.
