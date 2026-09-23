# YAML Record Review: (R)-fluoxapiprolin

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antifungal/r-fluoxapiprolin.yaml
- Started UTC: 2026-09-23T07:34:43Z
- Finished UTC: 2026-09-23T07:34:43Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/antibiotics/antifungal/r-fluoxapiprolin.yaml` |
| Identifier | `CHEBI:145868` |
| Label | `(R)-fluoxapiprolin` |
| Filing class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Generated or maintained | Generated record, emitted from `data/raw/chebi_antimicrobials.tsv` through the ChEBI seeding path |
| Source concept | `CHEBI:145868` from ChEBI release `2026-08-30` |
| Minted source key | `antibioticmech:chebi-a0fe1e4c18` |

This review inspected the complete YAML record and treated `data/raw/chebi_antimicrobials.tsv`, `data/antibiotics/PATHS.tsv`, `conf/sources.yaml`, and `curation/record_review_queue.tsv` as the maintained local inputs for seeded ChEBI identity, class, role, and structure claims.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/r-fluoxapiprolin.yaml` | Passed with no LinkML validation issues. |
| `just validate-strict data/antibiotics/antifungal/r-fluoxapiprolin.yaml --out /tmp/r-fluoxapiprolin-validate-strict.tsv` | Passed: 1 file checked, 0 files with `ERROR`, and 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed: all 2,939 expected records were on disk, no unexpected records were present, no generated fields drifted, no identifiers were absent from `PATHS.tsv`, and no stale lockfile rows were present. The only diagnostic was the pre-existing unrelated CARD iclaprim/CHEBI:31724 cross-reference refusal. |
| `just worklist --limit 0 --tsv /tmp/r-fluoxapiprolin-worklist.tsv` | Passed and regenerated a full worklist. Exact rows for `CHEBI:145868` report `mechanism` and `review-readiness` gaps with 0 CARD targets, 0 resistance edges, 0 source literature leads, 0 record evidence items, and 0 targets. The only diagnostic was the pre-existing unrelated CARD iclaprim/CHEBI:31724 cross-reference refusal. |
| `just review-queue --limit 150` | Passed and listed `(R)-fluoxapiprolin` as `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just lint` | Passed before writing this report. |
| `git diff --check` | Passed before writing this report. |
| `git diff --cached --check` | Passed after staging this report. |

No narrower single-record term, reference, or curation-history validator is exposed for this plain ChEBI-seeded record, so the review used the available single-record schema checks plus full-corpus reproducibility and queue/worklist checks.

## Identity and Grounding

The record identity is internally consistent:

| Claim | Review |
|---|---|
| ChEBI grounding | `identifier: CHEBI:145868`, `label: (R)-fluoxapiprolin`, `grounding_status: EXACT`, and the sole `source_concepts` entry all agree. |
| Raw ChEBI seed | `data/raw/chebi_antimicrobials.tsv` carries the same identifier, label, definition, 3-star status, SMILES, Standard InChI, Standard InChIKey `ZEXXEODAXHSRDJ-HXUWFJFHSA-N`, formula, charge, masses, and IUPAC name. |
| Structure | SMILES `[H][C@]1(c2c(Cl)cccc2OS(C)(=O)=O)CC(c2csc(C3CCN(C(=O)Cn4nc(C(F)F)cc4C(F)F)CC3)n2)=NO1`, Standard InChI, InChIKey, formula `C25H24ClF4N5O5S2`, charge `0`, average mass `650.076`, and monoisotopic mass `649.08435` are the exact ChEBI-imported values. |
| Parent boundary | `CHEBI:145867` is the broader fluoxapiprolin parent, and `CHEBI:145869` is the sibling `(S)-fluoxapiprolin` enantiomer with a different InChIKey, so this record denotes the intended individual stereoisomer. |
| Filing class | The sole ChEBI role is `CHEBI:24127` / fungicide, which `conf/sources.yaml` maps to `ANTIFUNGAL` at priority 3; filing the record under `data/antibiotics/antifungal/` is consistent with that mapping. |
| Path lock | `data/antibiotics/PATHS.tsv` maps `CHEBI:145868` to `ANTIFUNGAL` / `r-fluoxapiprolin`, matching the current record path. |

An ignored-inclusive search across `data/raw`, `curation`, `reports/yaml_record_review`, and `data/antibiotics` for `CHEBI:145868`, `antibioticmech:chebi-a0fe1e4c18`, and `ZEXXEODAXHSRDJ-HXUWFJFHSA-N` found only the expected ChEBI raw row, path-lock row, review-queue row, and exact YAML record. It found no prior exact review report for this identifier.

## Evidence

There is no claim-level evidence to audit because this seeded record has no `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, `activity_observations`, `resistance_mechanisms`, `producer_organisms`, `causal_graphs`, datasets, discussions, or record-level `evidence`.

The existing scientific assertions are seed-owned ChEBI database assertions:

| Assertion | Support |
|---|---|
| `(R)-fluoxapiprolin` is a ChEBI-grounded exact record with the listed IUPAC synonym and structure. | Supported by the committed ChEBI inventory row for `CHEBI:145868`. |
| The record carries the ChEBI fungicide role term. | Supported by the same ChEBI row, which lists `CHEBI:24127` as the sole role term. |

Bounded publication discovery did not find a source that could justify adding mechanism or activity claims for the exact reviewed structure:

| Query | Result |
|---|---|
| Exact `(R)-fluoxapiprolin` label through PubMed and Semantic Scholar | PubMed returned 0 candidates; Semantic Scholar was rate-limited with HTTP 429. |
| Exact `ZEXXEODAXHSRDJ-HXUWFJFHSA-N` InChIKey through PubMed and Semantic Scholar | PubMed returned 0 candidates; Semantic Scholar returned 2 false positives with unrelated reagent titles. |
| Exact ChEBI IUPAC name through PubMed and Semantic Scholar | PubMed returned 0 candidates; Semantic Scholar was rate-limited with HTTP 429. |
| Parent `fluoxapiprolin oxysterol binding protein fungicide` query | PubMed found `PMID:35416662`, a parent fluoxapiprolin resistance-risk paper that studies *Phytophthora infestans* and PiORP1 mutations but does not name `CHEBI:145868`, `(R)-fluoxapiprolin`, or the exact InChIKey. Semantic Scholar was rate-limited with HTTP 429. |

## Completeness

The generated identity, source-concept, structure, parent, and curation-history fields are complete enough for a ChEBI seed.

The record remains scientifically incomplete because it does not yet have a mechanism statement, target, resistance mechanism, or direct activity observation for the exact `(R)` enantiomer. The derived worklist keeps it in both the `mechanism` and `review-readiness` queues with no source literature leads, record evidence, or targets. That gap is consequential and blocks `REVIEWED` status under the local gate because the mode of action has not been checked.

The optional target, activity, resistance, producer, causal-graph, dataset, and discussion slots are correctly absent in the sense that the bounded exact searches did not produce inspected support that would justify populating them during this read-only review.

## Findings

### Blocker

None found.

### Major

| Finding | Evidence | Maintained owner |
|---|---|---|
| The record has no evidence-backed mode of action, target, resistance mechanism, or direct activity observation for exact `(R)-fluoxapiprolin`, so it cannot qualify as `REVIEWED`. | The YAML lacks `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, `resistance_mechanisms`, `activity_observations`, and `causal_graphs`; `curation/record_review_queue.tsv` and the regenerated worklist both place `CHEBI:145868` in `MECHANISM_REVIEW` with 0 literature leads, 0 record evidence items, and 0 targets. | Future curator-owned additions to `data/antibiotics/antifungal/r-fluoxapiprolin.yaml`, written only through `write_validated_antibiotic` with a `record_curation_event`. |

### Minor

None found.

## Recommended Edits

1. Keep the seeded identity, structure, fungicide ChEBI role, parent, and path unchanged.
2. Before adding a `mode_of_action`, `mode_of_action_target_scope`, target, activity observation, resistance mechanism, or causal graph, inspect primary evidence for the exact `CHEBI:145868` enantiomer or an explicitly structure-equivalent source.
3. Do not transfer fluoxapiprolin PiORP1, oxysterol-binding-protein, EC50, or resistance claims from the unspecific `CHEBI:145867` parent or the `(S)` enantiomer to this `(R)` enantiomer unless the source itself demonstrates that the measurement or mechanism applies to the exact same stereochemical form.

## Follow-up Checks

Run the focused and full-corpus gates after any future curation:

1. `just validate data/antibiotics/antifungal/r-fluoxapiprolin.yaml`
2. `just validate-strict data/antibiotics/antifungal/r-fluoxapiprolin.yaml --out /tmp/r-fluoxapiprolin-validate-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/r-fluoxapiprolin-worklist.tsv`
5. `just review-queue --limit 150`
6. `just lint`

Also re-run exact publication searches for `(R)-fluoxapiprolin`, `CHEBI:145868`, `ZEXXEODAXHSRDJ-HXUWFJFHSA-N`, and the exact ChEBI IUPAC name before concluding that mechanism evidence remains unresolved.

## Additional Notes

- The record has only seed and reseed curation-history events from `2026-08-30`, accurately matching its generated `SEEDED` state.
- The ChEBI row does not import xrefs for this record, so the generated record correctly has no `xrefs` section.
- Parent-level fluoxapiprolin evidence exists, but this read-only review did not inspect full text far enough to justify a stereoisomer-specific curator claim.
- Semantic Scholar returned HTTP 429 for three of four bounded publication searches; PubMed and local derived queues carried the exact no-candidate result for those searches.
