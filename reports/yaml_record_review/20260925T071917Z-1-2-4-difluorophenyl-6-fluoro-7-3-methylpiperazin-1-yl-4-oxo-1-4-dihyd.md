# YAML Record Review: 1-(2,4-difluorophenyl)-6-fluoro-7-(3-methylpiperazin-1-yl)-4-oxo-1,4-dihydroquinoline-3-carboxylic acid

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/unspecified/1-2-4-difluorophenyl-6-fluoro-7-3-methylpiperazin-1-yl-4-oxo-1-4-dihyd.yaml`
- Started UTC: 2026-09-25T07:19:17Z
- Finished UTC: 2026-09-25T07:19:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/antibiotics/unspecified/1-2-4-difluorophenyl-6-fluoro-7-3-methylpiperazin-1-yl-4-oxo-1-4-dihyd.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| ID | `CHEBI:77796` |
| Label | `1-(2,4-difluorophenyl)-6-fluoro-7-(3-methylpiperazin-1-yl)-4-oxo-1,4-dihydroquinoline-3-carboxylic acid` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained status | Generated from `data/raw/` inventories |

The record denotes exact ChEBI-grounded nonstereospecific
`1-(2,4-difluorophenyl)-6-fluoro-7-(3-methylpiperazin-1-yl)-4-oxo-1,4-dihydroquinoline-3-carboxylic acid`
with InChIKey `QKDHBVNJCZBTMR-UHFFFAOYSA-N`. It has one ChEBI source concept, a
generic ChEBI `antimicrobial agent` activity role, eight broader ChEBI parent
compounds, no same-structure xrefs, and no record evidence, seeded
`mode_of_action`, molecular target, activity observation, resistance mechanism,
producer organism, clinical assertion, causal graph, dataset, or `Discussion`.

## Validation

| Command | Result |
|---|---|
| `just validate data/antibiotics/unspecified/1-2-4-difluorophenyl-6-fluoro-7-3-methylpiperazin-1-yl-4-oxo-1-4-dihyd.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/1-2-4-difluorophenyl-6-fluoro-7-3-methylpiperazin-1-yl-4-oxo-1-4-dihyd.yaml --out /tmp/chebi-77796-validate-strict.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2,939 expected records, 2,939 records on disk, no missing records, no unexpected records, no drifted fields, no `PATHS.tsv` issues. |
| `just worklist --limit 0 --tsv /tmp/chebi-77796-worklist.tsv` | Confirmed `CHEBI:77796` appears in `mechanism` and `review-readiness` only; the review row reports `MECHANISM_REVIEW`, zero source literature leads, zero record evidence items, and zero targets. |
| `uvx --from oaklib runoak -i ols:chebi info CHEBI:77796 CHEBI:33281 CHEBI:23765 CHEBI:25384 CHEBI:33709 CHEBI:37143 CHEBI:46848 CHEBI:50995 CHEBI:50996 CHEBI:86324` | Resolved the compound, the `antimicrobial agent` activity role, and all eight parent terms through OLS/ChEBI. |
| `curl -L 'https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:77796'` | Resolved the official ChEBI term with the same label, definition, formula, SMILES, Standard InChI, InChIKey, charge, average mass, monoisotopic mass, no xrefs, and no PubMed xrefs. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --query '"1-(2,4-difluorophenyl)-6-fluoro-7-(3-methylpiperazin-1-yl)-4-oxo-1,4-dihydroquinoline-3-carboxylic acid"' --limit 20 --output /tmp/chebi-77796-exact-label-publications.jsonl` | Wrote zero PubMed candidates for the exact ChEBI label. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --provider semantic-scholar --query 'QKDHBVNJCZBTMR-UHFFFAOYSA-N OR CHEBI:77796 OR "antibioticmech:chebi-b5334a40b3"' --limit 20 --output /tmp/chebi-77796-ids-publications.jsonl` | PubMed wrote zero candidates; Semantic Scholar returned HTTP 429. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --provider semantic-scholar --query '"3-methylpiperazin-1-yl" temafloxacin quinolone' --limit 20 --output /tmp/chebi-77796-temafloxacin-publications.jsonl` | PubMed wrote zero candidates; Semantic Scholar returned HTTP 429. |

No separate single-record term, reference, or history validator is documented in
the local `justfile`. The full `just qc` gate is left for the PR-level check
because this review made no YAML mutation.

## Identity and Grounding

The generated lock row in `data/antibiotics/PATHS.tsv` maps `CHEBI:77796` to
`ANTIMICROBIAL_UNSPECIFIED/1-2-4-difluorophenyl-6-fluoro-7-3-methylpiperazin-1-yl-4-oxo-1-4-dihyd`,
and `source_concepts` carries only the expected ChEBI upstream identity with
minted ID `antibioticmech:chebi-b5334a40b3`.

The exact structure block matches the committed ChEBI antimicrobial inventory
row for `CHEBI:77796`: SMILES, Standard InChI, nonstereospecific InChIKey
`QKDHBVNJCZBTMR-UHFFFAOYSA-N`, formula `C21H18F3N3O3`, charge `0`, average
mass, monoisotopic mass, role term `CHEBI:33281`, and all eight
`parent_compounds` values agree with `data/raw/chebi_antimicrobials.tsv`. The
official ChEBI OLS term for `CHEBI:77796` reports the same label, definition,
formula, SMILES, Standard InChI, InChIKey, and mass fields.

The stereochemical boundary is correct. The already-reviewed sibling records
`CHEBI:77794` `(R)-temafloxacin` and `CHEBI:77795` `(S)-temafloxacin` both list
`CHEBI:77796` as a strictly broader parent compound and use stereospecific
Standard InChIKeys, respectively `QKDHBVNJCZBTMR-LLVKDONJSA-N` and
`QKDHBVNJCZBTMR-NSHDSACASA-N`.

No local grounding decision or prior review report was found for `CHEBI:77796`,
`antibioticmech:chebi-b5334a40b3`,
`QKDHBVNJCZBTMR-UHFFFAOYSA-N`, the exact label, or the slug in
gitignore-independent searches over `data/antibiotics`, `data/raw`, `curation`,
`reports/yaml_record_review`, `.claude`, `docs`, `README.md`, `conf`, `src`,
`scripts`, `tests`, `justfile`, and `pyproject.toml`. The exact ID search found
only sibling-report notes that name `CHEBI:77796` as the nonstereospecific
parent of `(R)-` and `(S)-temafloxacin`, not a review of this parent record.

## Evidence

The generated identity, label, definition, exact structure, parent compounds,
filing class, generic ChEBI activity role, source concept, and grounding status
reproduce from the committed ChEBI inventory with no `verify-corpus` drift.

The official ChEBI term and local raw row expose no xrefs and no PubMed xrefs
for the exact nonstereospecific parent. ChEBI does attach `PMID:1846917` to each
stereospecific enantiomer and several PMIDs to the `CHEBI:77788` racemate, but
those are distinct ChEBI structures. A later curator should inspect those full
texts before deciding whether any temafloxacin assay or target claim is stated
at a scope that applies to this parent record.

The exact-label, identifier, and structural-fragment publication searches did
not return direct PubMed candidates for `CHEBI:77796`. The record makes no
mode-of-action, molecular-target, activity, resistance, producer, clinical, or
causal-edge claims, so there are no unsupported claim-level citations in the
YAML.

## Completeness

The exact ChEBI identity, structure, ChEBI grounding, source concept, generic
activity role, parent compounds, and absence of same-structure xrefs are
defensible.

The consequential gap is mechanism sign-off. The YAML has no `mode_of_action`,
no `mode_of_action_target_scope`, no `molecular_targets` item, no causal graph,
and no target-specific `EvidenceItem`. `just worklist --limit 0 --tsv
/tmp/chebi-77796-worklist.tsv` therefore keeps the record in the `mechanism`
and `review-readiness` queues.

No activity observations, producer claims, resistance assertions, clinical
assertions, or public datasets are present. The ChEBI definition does not embed
organismal or assay prose, and the full worklist TSV has no
`producer-candidate` or `activity-candidate` row for `CHEBI:77796`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record has no antimicrobial mechanism and cannot satisfy the `REVIEWED` gate until a curator either supports a mechanism for this exact nonstereospecific structure or explicitly records why no mechanism should be asserted. | The target YAML has no `mode_of_action`, no `mode_of_action_target_scope`, no `record_evidence`, no `molecular_targets`, and no `causal_graphs`; `just worklist --limit 0 --tsv /tmp/chebi-77796-worklist.tsv` reports `0 CARD target(s), 0 resistance edge(s) to build on` for the `mechanism` queue and `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)` for the `review-readiness` queue. | Curator-owned evidence, molecular target, activity observation, discussion, or causal-graph additions written to `data/antibiotics/unspecified/1-2-4-difluorophenyl-6-fluoro-7-3-methylpiperazin-1-yl-4-oxo-1-4-dihyd.yaml` through `write_validated_antibiotic`, if primary literature supports them. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the racemate and enantiomer literature before asserting a mechanism
   on the nonstereospecific parent. Prioritize `PMID:1846917`, which ChEBI
   attaches to `(R)-` and `(S)-temafloxacin`, plus the seven source PMIDs on
   `CHEBI:77788` temafloxacin.
2. If an inspected source states that the compound inhibits bacterial DNA
   gyrase or topoisomerase IV at a scope that applies to this ChEBI parent, add
   a curator-owned `MolecularTarget`, curator-owned
   `mode_of_action: DNA_TOPOISOMERASE_INHIBITION`, and
   `mode_of_action_target_scope: MICROBIAL_TARGET` with claim-level primary
   evidence.
3. If the only available evidence is racemic or enantiomer-specific, leave
   mechanism fields empty and add a `Discussion` describing the stereochemical
   scope gap, why `CHEBI:77796` cannot inherit the racemate or enantiomer claim
   directly, and which publications were checked.
4. Do not copy `CHEBI:77788` drug xrefs, `CHEBI:77794` Reaxys `4301728`, or
   `CHEBI:77795` Reaxys `4301727` onto this exact parent record; those refer to
   the racemate or a stereospecific structure.
5. If a mode of action, target, activity observation, discussion, or causal
   graph is supported, write it with a guarded mutator that asserts
   `identifier == "CHEBI:77796"`, updates only curator-owned fields, appends a
   `codex` `CurationEvent` with `llm_assisted: true`, and emits via
   `write_validated_antibiotic`.
6. Move `curation_status` to `REVIEWED` only after identity, structure, filing
   class, and any newly curator-checked mechanism satisfy the
   `docs/CURATION.md` sign-off criteria.

## Follow-up Checks

After a future mechanism curation edit:

- `just validate-strict data/antibiotics/unspecified/1-2-4-difluorophenyl-6-fluoro-7-3-methylpiperazin-1-yl-4-oxo-1-4-dihyd.yaml --out /tmp/chebi-77796-validate-strict.tsv`
- `just verify-corpus`
- `just qc`
- `git diff -- data/antibiotics/unspecified/1-2-4-difluorophenyl-6-fluoro-7-3-methylpiperazin-1-yl-4-oxo-1-4-dihyd.yaml curation/decisions.tsv src scripts tests`
- `just review-queue --limit 0 --tsv curation/record_review_queue.tsv`

## Additional Notes

Searches used to establish absence included ignored files:

- `rg --no-ignore --hidden` over `data/antibiotics`, `data/raw`, `curation`,
  `reports/yaml_record_review`, `.claude`, `docs`, `README.md`, `conf`, `src`,
  `scripts`, `tests`, `justfile`, and `pyproject.toml` for `CHEBI:77796`,
  `QKDHBVNJCZBTMR-UHFFFAOYSA-N`, the exact label, and the exact slug.

`NCBI_EMAIL` was unset for the PubMed searches. Semantic Scholar returned HTTP
429 for both non-PubMed searches, so that provider's literature leads were not
available in this pass.

This report is read-only review output. No generated record, upstream
inventory, decision row, page, queue, or curation-history entry was edited.
