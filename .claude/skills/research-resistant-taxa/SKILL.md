---
name: research-resistant-taxa
description: Research and curate taxon- or strain-level MIC observations that show resistance to specific existing AntibioticMech compounds. Use when asked which taxa, strains, isolates, or genomes resist an antibiotic; use add-antibiotic for absent compounds and source-queue for bulk AST source adoption.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Research resistant taxa for an AntibioticMech record

Find and, when asked to curate, add defensible phenotypic resistance
observations for one existing `AntibioticRecord`. Prefer taxon- and
strain-specific MICs backed by primary papers or redistributable AST rows; keep
genome/sample accessions when sources provide them, even though the current
`ActivityObservation` schema has no dedicated BioSample, Assembly or SRA slot.

## Boundaries

- Start from one exact compound under `data/antibiotics/<class>/`. If the
  compound is absent, use `add-antibiotic`; if the request is whole-record
  sign-off, use `curate-yaml-record`.
- A request to find, list or report resistant taxa is read-only. A request to
  add, curate or write observations authorizes local edits to existing records.
- Curate phenotypic MIC or breakpoint calls in `activity_spectrum`.
  Mechanism-free resistance is still useful activity evidence.
- Curate `resistance_mechanisms` only when a source identifies a determinant,
  allele, expression change or mechanism. Use `mechanism_type: UNKNOWN` when
  the phenotype is specific but the biochemical route is not known.
- Do not infer resistance from a MIC unless the source states an R/S/I
  interpretation or cites a versioned breakpoint standard for the organism,
  drug and assay.
- Do not copy bulk rows from a candidate, restricted or unverified source. Treat
  NCBI Pathogen AST, CRyPTIC, BV-BRC, BacDive, ChEMBL and CO-ADD as discovery
  leads unless `curation/source_queue.tsv` and `conf/sources.yaml` show an
  adopted lane that can redistribute that exact slice.
- Do not create a GitHub issue, PR, comment, email, form or `@` mention unless
  the user explicitly authorizes that exact outbound action.

## Read First

- `CLAUDE.md` for generated-file boundaries and curation-event requirements.
- `docs/CURATION.md`, especially "The organismal evidence model".
- `docs/HARMONIZATION.md` for exact compound identity rules.
- `curation/source_queue.tsv` for AST and AMR source status and licence traps.
- `src/antibioticmech/schema/antibioticmech.yaml` for
  `ActivityObservation`, `ActivityCallEnum`, `ResistanceMechanism`,
  `ResistanceMechanismEnum` and `EvidenceItem`.
- The full target YAML plus activity or PHI-base resistance examples.

Useful local examples include:

- `data/antibiotics/antibacterial/althiomycin.yaml`
- `data/antibiotics/antibacterial/linoleic-acid.yaml`
- `data/antibiotics/antifungal/micafungin.yaml`

## Find a Target

Resolve the exact record first. Check the label, `identifier`, Standard
InChIKey, salts, stereochemistry and `source_concepts` before researching
organismal resistance to a similarly named drug.

Use the activity worklist for phrase-level leads:

```bash
just worklist --queue activity-candidate --limit 25
```

For a named record, run a pre-edit baseline without dirtying the checked-in
report:

```bash
just validate-strict <record-path> --out /tmp/antibioticmech-resistant-taxa-validation.tsv
just verify-corpus --summary
```

## Evaluate Observations

Standardize curated quantitative AST on MIC in `mg/L`:

- Convert `ug/mL` or `micrograms/mL` to `mg/L` without changing the numeric
  value.
- Convert molar MICs only when the tested compound is exactly this record and
  the molecular mass makes the conversion unambiguous; preserve the original
  value in `EvidenceItem.notes`.
- Keep relational qualifiers such as `<`, `<=`, `>`, `>=`, `MIC50` and `MIC90`
  in `mic_qualifier`, never by changing the number.
- Do not convert disk-diffusion zones, Etest ellipse text, gradient-strip
  values reported as ranges or S/I/R-only calls into MICs. Record them as
  assay context or leave a `Discussion` if the schema cannot faithfully carry
  the result.

Map the organism at the same precision the source supports:

- Fill `taxon_label` exactly enough to name the tested organism or group.
- Add `taxon_id` only after verifying it is the NCBITaxon CURIE for that label.
- Put strain or isolate designations in `strain`, not in `taxon_label`.
- Do not put BioSample, BioProject, SRA or Assembly accessions in `taxon_id`.
  Preserve them in evidence notes with the source row ID until a structured
  genome/sample slot exists.
- Do not generalize one resistant strain to a resistant species or genus.

Preserve breakpoint context honestly. CLSI and EUCAST breakpoints are
versioned, organism-specific and method-specific; a MIC can be resistant under
one standard and susceptible under another. If the source calls an isolate
resistant, include the standard and version in `assay` or evidence notes when
available. If the source only gives a MIC, write the MIC and leave the
qualitative `activity` empty rather than deriving a resistant call.

Set `activity` conservatively:

- `INACTIVE` when the source directly frames the compound as inactive against
  the tested organism or isolate.
- `INTRINSICALLY_RESISTANT` only when the source asserts intrinsic resistance
  for that organism.
- `VARIABLE` for a taxon-level summary that explicitly spans resistant and
  susceptible isolates.
- Do not coerce a clinical breakpoint `R` or `I` call into `INACTIVE`; preserve
  the call, standard and version in `EvidenceItem.notes`.
- Omit `activity` when the MIC is reported without a supported qualitative
  interpretation.

## Write Through the Guarded Path

Never hand-edit the YAML. Use a narrowly scoped Python mutator under `/tmp`
unless the request is to add reusable tooling:

1. load the target YAML;
2. assert the expected `identifier` and path;
3. append or replace exactly the intended `activity_spectrum` and, when
   separately supported, `resistance_mechanisms` entries;
4. add a `Discussion` only for a concrete unresolved representation gap, source
   conflict or taxon/strain ambiguity;
5. call `record_curation_event(..., curator="codex",
   action="CURATED_RESISTANT_TAXA", llm_assisted=True, changes=...)`; and
6. write with `write_validated_antibiotic`.

Skip the write and do not append a history event if the source review produced
no substantive record change.

## Regenerate and Verify

After any edit, regenerate the derived surfaces that expose curation status,
activity counts or rendered AST rows:

```bash
just review-queue --limit 0 --tsv curation/record_review_queue.tsv
just render
just docs-stats
```

Then run the record and repository gates:

```bash
just validate-strict <record-path> --out /tmp/antibioticmech-resistant-taxa-validation.tsv
just verify-corpus
just qc
git diff --check
```

Read the final YAML and rendered page. Confirm that MIC values have units and
assays, every observation has evidence on the closest supported AST claim,
taxon IDs denote the written labels, isolate/genome IDs are not silently lost,
and the curation-history event describes the actual diff.

## Report

Report the record path, resistant taxa or strains found, NCBITaxon CURIEs,
strain/isolate names, genome/sample accessions that were present but not
structurable, normalized MICs with original units, breakpoint standard or
qualitative call, PMIDs/DOIs/database rows supporting each observation, any
`resistance_mechanisms` separately added, representation gaps left as
`Discussion` entries, generated files refreshed and every validation command
run.
