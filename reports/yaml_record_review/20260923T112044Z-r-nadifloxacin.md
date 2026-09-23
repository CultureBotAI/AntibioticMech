# YAML Record Review: (R)-nadifloxacin

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antibacterial/r-nadifloxacin.yaml
- Started UTC: 2026-09-23T11:20:45Z
- Finished UTC: 2026-09-23T11:21:39Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | CHEBI:37907 |
| Label | (R)-nadifloxacin |
| Path | data/antibiotics/antibacterial/r-nadifloxacin.yaml |
| Class | ANTIBACTERIAL |
| Curation status | SEEDED |
| Grounding status | EXACT |
| Maintained owner | Generated from `data/raw/chebi_antimicrobials.tsv`; do not hand-edit the generated YAML |
| Source concept | CHEBI / CHEBI:37907 / `antibioticmech:chebi-cf7fff59b7` |

The entire target YAML was read before judging the record. The generated record contains seeded ChEBI identity, role, structure, `beilstein:7084298`, and source-concept fields only: it has no `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, `activity_observations`, `resistance_mechanisms`, `producer_organisms`, `causal_graphs`, `datasets`, `discussions`, or record-level `evidence`.

## Validation

| Check | Result |
|---|---|
| `rg --no-ignore --hidden --files -g 'AGENTS.md'` | Passed; no repo-local `AGENTS.md` was found, with hidden and ignored files included. |
| `rg --no-ignore --hidden '(^identifier: CHEBI:37907$|source_id: CHEBI:37907$|^CHEBI:37907\t|^review-readiness\tCHEBI:37907\t|r-nadifloxacin)' data/antibiotics data/raw curation reports/yaml_record_review` | Passed; resolved one YAML file, the raw ChEBI inventory row, the `PATHS.tsv` row, and the `review-readiness` row. No prior `r-nadifloxacin` review report was found in `reports/yaml_record_review` with ignored files included. |
| `just validate data/antibiotics/antibacterial/r-nadifloxacin.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/antibiotics/antibacterial/r-nadifloxacin.yaml --out /tmp/antibioticmech-r-nadifloxacin-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2,939 records expected and present, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `just review-queue --limit 5` | Passed; regenerated the review-readiness queue and reported 2,859 unsigned records. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-r-nadifloxacin-worklist.tsv` | Passed; wrote 8,252 rows. `CHEBI:37907` appears on the `mechanism` queue and the `review-readiness` queue only. |
| `just lint` | Passed; Ruff reported all checks passed. |
| `git diff --cached --check` | Passed after staging this ignored report. |
| Narrow single-record term/reference/history validators | Not available for plain ChEBI-seeded records; the repository exposes schema validation for a single record plus full-corpus generated-state and worklist checks. |

## Identity and Grounding

The record denotes the same individual ChEBI structure named by the target:

- The official EBI OLS search for `CHEBI:37907` returned one non-obsolete defining ChEBI term with label `(R)-nadifloxacin` and exact synonym `(5R)-9-fluoro-8-(4-hydroxypiperidin-1-yl)-5-methyl-1-oxo-6,7-dihydro-1H,5H-pyrido[3,2,1-ij]quinoline-2-carboxylic acid`.
- The OLS term detail for `CHEBI:37907` matched the generated `smiles`, Standard InChI, Standard InChIKey `JYJTVFIEFKZWCJ-SNVBAGLBSA-N`, formula `C19H21FN2O4`, charge `0`, average mass `360.385`, monoisotopic mass `360.14854`, and `beilstein:7084298`.
- The OLS parent lookup for `CHEBI:37907` returned `CHEBI:31889` / `nadifloxacin`; that broader parent has a Standard InChIKey without stereochemical assignment (`JYJTVFIEFKZWCJ-UHFFFAOYSA-N`), so the record's `parent_compounds: CHEBI:31889` is a broader stereochemical parent rather than an equivalent exact xref.
- The ignored-inclusive YAML search for `standard_inchi_key: JYJTVFIEFKZWCJ-SNVBAGLBSA-N` under `data/antibiotics -g '*.yaml'` found only this record, so no other curated YAML currently duplicates this exact ChEBI structure.

No grounding conflict was found. Future fixes to seeded identity, structure, class, role, parent, xref, or source-concept fields would be owned by `data/raw/chebi_antimicrobials.tsv`, `curation/decisions.tsv`, the extractor, or the seeder rather than by direct record edits.

## Evidence

Existing evidence-backed claim objects are absent, so there were no claim-level citations, snippets, molecular-target assertions, resistance mechanisms, activity observations, producer claims, datasets, or causal edges to verify.

Bounded literature checks found mechanistic leads for the broader nadifloxacin concept but not enough exact-scope support to populate `(R)-nadifloxacin`:

- `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --provider semantic-scholar --query '(R)-nadifloxacin DNA gyrase topoisomerase MIC antibacterial' --limit 20 --output /tmp/antibioticmech-r-nadifloxacin-pub.jsonl` found PMID:11709337 / DOI:10.1128/aac.45.12.3544-3547.2001 via PubMed; Semantic Scholar returned HTTP 429. The PubMed abstract reports nadifloxacin target-preference assays against *Staphylococcus aureus* mutant strains and IC50 assays against topoisomerase IV and DNA gyrase, but it refers to nadifloxacin rather than the `(R)` enantiomer.
- `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --query '"(R)-nadifloxacin" OR "CHEBI:37907" OR "JYJTVFIEFKZWCJ"' --limit 20 --output /tmp/antibioticmech-r-nadifloxacin-exact-pubmed.jsonl` returned 11 PubMed candidates. The top exact stereochemistry lead was PMID:42670252 / DOI:10.1002/chir.70143, whose abstract reports multimilligram enantioresolution of nadifloxacin and states that marketed nadifloxacin is racemic; its abstract frames `(R)-nadifloxacin` as less active than `(S)-nadifloxacin` against *Staphylococcus aureus* and *Propionibacterium acnes*. That supports a stereochemistry caution but does not provide claim-level mechanism support.

## Completeness

The record is structurally complete enough for a seed-only exact ChEBI term:

- Identity and structure are grounded to ChEBI and reproduce from `data/raw/chebi_antimicrobials.tsv`.
- ChEBI's broader `nadifloxacin` term is retained as `parent_compounds`, not mis-modeled as an equivalent `xrefs` value.
- The one Beilstein xref is present as an exact ChEBI-provided structure xref.
- The ChEBI `antimicrobial agent` and `antibacterial drug` roles are retained as `activity_roles`.

Consequential gaps remain:

- No mode of action has been curated.
- No target scope has been curated.
- No DNA gyrase or topoisomerase IV target has been curated.
- No organism-scoped MIC or other `ActivityObservation` has been curated.
- No resistance phenotype, causal graph, or exact-enantiomer dataset has been curated.

The full worklist row for `CHEBI:37907` reports `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. A targeted ignored-inclusive search found no prior `r-nadifloxacin` review report in `reports/yaml_record_review`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `CHEBI:37907` is not mechanism-reviewed: it lacks `mode_of_action`, target scope, molecular targets, and a causal graph for the exact `(R)` enantiomer. | The target YAML has no mechanism or target fields; `just worklist --limit 0 --tsv /tmp/antibioticmech-r-nadifloxacin-worklist.tsv` lists `mechanism	CHEBI:37907	(R)-nadifloxacin	CHEBI		0 CARD target(s), 0 resistance edge(s) to build on`; the review-readiness row reports `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. | `data/antibiotics/antibacterial/r-nadifloxacin.yaml`, written through a validated one-off curation mutator that calls `record_curation_event` and `write_validated_antibiotic`. |
| Blocker | None found. Identity, exact ChEBI grounding, seeded structure, xref placement, source concept, and corpus reproduction all check out. | See `Identity and Grounding` and `Validation`. | Not applicable. |
| Minor | None found. | Not applicable. | Not applicable. |

## Recommended Edits

1. Curate `(R)-nadifloxacin` mechanism evidence from exact-stereochemistry primary literature, or record a bounded `UNKNOWN`/`CURATION_TODO` discussion if the available nadifloxacin mechanism literature proves racemate-scoped rather than `(R)`-scoped.
   - Maintained path: `data/antibiotics/antibacterial/r-nadifloxacin.yaml` through a guarded `/tmp` mutator using `record_curation_event(..., curator="codex", llm_assisted=True)` and `write_validated_antibiotic`.
   - Expected fields: `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets` for bacterial DNA gyrase and/or topoisomerase IV only if the inspected source supports that exact target relationship, and `causal_graphs` only after every directed edge has primary evidence.

2. Curate organism-scoped activity observations only from sources that identify which enantiomer was assayed.
   - Maintained path: `data/antibiotics/antibacterial/r-nadifloxacin.yaml` through the same guarded write path.
   - Expected fields: `ActivityObservation` entries with organism or strain, assay, numeric value and qualifier, units for each MIC, and claim-level `EvidenceItem` values.

## Follow-up Checks

- `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --provider semantic-scholar --query '"R-nadifloxacin" OR "(R)-nadifloxacin" OR "CHEBI:37907" OR "JYJTVFIEFKZWCJ"' --limit 50 --output /tmp/antibioticmech-r-nadifloxacin-followup.jsonl`; retry Semantic Scholar after its 429 clears.
- Inspect the full texts for PMID:11709337 and PMID:42670252 to decide whether their nadifloxacin and enantiomer data can support any exact `(R)` mechanism or activity claim.
- After any curation edit, run `just validate-strict data/antibiotics/antibacterial/r-nadifloxacin.yaml --out /tmp/antibioticmech-r-nadifloxacin-strict-after.tsv`.
- Run `just verify-corpus` and confirm curator-owned mechanism additions persist without drift.
- Run `just worklist --queue mechanism --limit 0 --tsv /tmp/antibioticmech-mechanism-after.tsv` and verify `CHEBI:37907` leaves the mechanism queue if a concrete mechanism is added.
- Run `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-after.tsv` and verify the row moves from `MECHANISM_REVIEW` to the next unresolved evidence gate.
- Run `just qc` before opening a curation PR.

## Additional Notes

- Search results, PubMed abstracts, and OLS responses were treated as leads or identifier checks only; no generated report asserts a new biological mechanism from them.
- Publication discovery was run with `NCBI_EMAIL` unset, as required by `.claude/skills/curate-yaml-record/SKILL.md`.
- Google Scholar was not queried because it uses SerpAPI and requires explicit approval.
- No generated YAML was edited.
