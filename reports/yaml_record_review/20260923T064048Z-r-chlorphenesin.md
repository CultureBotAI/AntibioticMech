# YAML Record Review: (R)-chlorphenesin

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antibacterial/r-chlorphenesin.yaml
- Started UTC: 2026-09-23T06:40:48Z
- Finished UTC: 2026-09-23T06:41:03Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/antibiotics/antibacterial/r-chlorphenesin.yaml` |
| Identifier | `CHEBI:59479` |
| Label | `(R)-chlorphenesin` |
| Filing class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Generated or maintained | Generated record, emitted from `data/raw/chebi_antimicrobials.tsv` through the ChEBI seeding path |
| Source concept | `CHEBI:59479` from ChEBI release `2026-08-30` |

This review inspected the complete YAML record and treated `data/raw/chebi_antimicrobials.tsv`, `data/antibiotics/PATHS.tsv`, `conf/sources.yaml`, and `curation/record_review_queue.tsv` as the maintained local inputs for seeded ChEBI identity, class, role, structure, xref, and queue claims.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/r-chlorphenesin.yaml` | Passed with no LinkML validation issues. |
| `just validate-strict data/antibiotics/antibacterial/r-chlorphenesin.yaml --out /tmp/r-chlorphenesin-validate-strict.tsv` | Passed: 1 file checked, 0 files with `ERROR`, and 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed: all 2,939 expected records were on disk, no unexpected records were present, no generated fields drifted, no identifiers were absent from `PATHS.tsv`, and no stale lockfile rows were present. The only diagnostic was the pre-existing unrelated CARD iclaprim/CHEBI:31724 cross-reference refusal. |
| `just worklist --limit 0 --tsv /tmp/r-chlorphenesin-worklist.tsv` | Passed and regenerated a full worklist. Exact rows for `CHEBI:59479` report `mechanism` and `review-readiness` gaps with 0 CARD targets, 0 resistance edges, 0 source literature leads, 0 record evidence items, and 0 targets. The only diagnostic was the pre-existing unrelated CARD iclaprim/CHEBI:31724 cross-reference refusal. |
| `just review-queue --limit 140` | Passed and listed `(R)-chlorphenesin` as `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `git diff --check` | Passed before writing this report. |
| `just lint` | Passed. |
| `git diff --cached --check` | Passed after staging this report. |

No narrower single-record term, reference, or curation-history validator is exposed for this plain ChEBI-seeded record, so the review used the available single-record schema checks plus full-corpus reproducibility and queue/worklist checks.

## Identity and Grounding

The record identity is internally consistent:

| Claim | Review |
|---|---|
| ChEBI grounding | `identifier: CHEBI:59479`, `label: (R)-chlorphenesin`, `grounding_status: EXACT`, and the sole `source_concepts` entry all agree. |
| Raw ChEBI seed | `data/raw/chebi_antimicrobials.tsv` carries the same identifier, label, definition, 3-star status, SMILES, Standard InChI, Standard InChIKey `MXOAEAUPQDYUQM-MRVPVSSYSA-N`, formula, charge, masses, synonyms, and `reaxys:6175744` xref. |
| Structure | SMILES `OC[C@@H](O)COc1ccc(Cl)cc1`, Standard InChI, InChIKey, formula `C9H11ClO3`, charge `0`, average mass `202.637`, and monoisotopic mass `202.03967` are the exact ChEBI-imported values. |
| Parent boundary | `CHEBI:3642` is the unspecific parent `chlorphenesin`, so the parent link is broader than the reviewed enantiomer. |
| Filing class | ChEBI role `CHEBI:36047` maps to `ANTIBACTERIAL` at priority 2 and ChEBI role `CHEBI:86327` maps to `ANTIFUNGAL` at priority 3 in `conf/sources.yaml`; filing the record under `data/antibiotics/antibacterial/` follows that priority while preserving both activity roles. |
| Path lock | `data/antibiotics/PATHS.tsv` maps `CHEBI:59479` to `ANTIBACTERIAL` / `r-chlorphenesin`, matching the current record path. |

An ignored-inclusive search across `data/raw`, `curation`, `reports/yaml_record_review`, and `data/antibiotics` for `CHEBI:59479`, `antibioticmech:chebi-a5b58c0155`, `MXOAEAUPQDYUQM-MRVPVSSYSA-N`, and `reaxys:6175744` found only the expected ChEBI raw row, path-lock row, review-queue row, and exact YAML record. It found no prior exact review report for this identifier.

## Evidence

There is no claim-level evidence to audit because this seeded record has no `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, `activity_observations`, `resistance_mechanisms`, `producer_organisms`, `causal_graphs`, datasets, discussions, or record-level `evidence`.

The existing scientific assertions are seed-owned ChEBI database assertions:

| Assertion | Support |
|---|---|
| `(R)-chlorphenesin` is a ChEBI-grounded exact record with the listed synonyms and structure. | Supported by the committed ChEBI inventory row for `CHEBI:59479`. |
| The record carries both antibacterial and antifungal ChEBI role terms. | Supported by the same ChEBI row, which lists `CHEBI:36047|CHEBI:86327`; both role terms are preserved in the generated YAML. |
| The record has a Reaxys xref. | Supported by the same ChEBI row, which imports `reaxys:6175744`. |

Bounded publication discovery did not find a source that could justify adding mechanism or activity claims for the exact reviewed structure:

| Query | Result |
|---|---|
| Exact `(R)-chlorphenesin` label through PubMed and Semantic Scholar | PubMed found `PMID:28506583`, a biocatalysis paper about enantiomerically enriched drug precursors that mentions `(R)-chlorphenesin carbamate`; Semantic Scholar was rate-limited with HTTP 429. The paper is a near miss and does not support antimicrobial mechanism, target, activity, resistance, producer, or causal-graph fields. |
| Exact `(2R)-3-(4-chlorophenoxy)propane-1,2-diol` IUPAC name through PubMed and Semantic Scholar | PubMed returned 0 candidates; Semantic Scholar was rate-limited with HTTP 429. |
| Exact `MXOAEAUPQDYUQM-MRVPVSSYSA-N` InChIKey through PubMed and Semantic Scholar | PubMed returned 0 candidates; Semantic Scholar was rate-limited with HTTP 429. |
| Exact `"glycerol p-chlorophenyl ether" antimicrobial` synonym phrase through PubMed and Semantic Scholar | PubMed returned 0 candidates; Semantic Scholar was rate-limited with HTTP 429. |
| Broader `chlorphenesin antibacterial antifungal mechanism MIC` query | Returned 20 candidates from Semantic Scholar, all off-target broad antimicrobial papers or unrelated compounds on inspection of the normalized titles and abstracts. |

## Completeness

The generated identity, role, source-concept, structure, parent, xref, and curation-history fields are complete enough for a ChEBI seed.

The record remains scientifically incomplete because it does not yet have a mechanism statement or any direct antimicrobial activity measurement for the exact `(R)` enantiomer. The derived worklist keeps it in both the `mechanism` and `review-readiness` queues with no source literature leads, record evidence, or targets. That gap is consequential and blocks `REVIEWED` status under the local gate because the mode of action has not been checked.

The optional target, activity, resistance, producer, causal-graph, dataset, and discussion slots are correctly absent in the sense that the bounded exact searches did not produce inspected support that would justify populating them during this read-only review.

## Findings

### Blocker

None found.

### Major

| Finding | Evidence | Maintained owner |
|---|---|---|
| The record has no evidence-backed mode of action or direct activity observation for exact `(R)-chlorphenesin`, so it cannot qualify as `REVIEWED`. | The YAML lacks `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, `activity_observations`, and `causal_graphs`; `curation/record_review_queue.tsv` and the regenerated worklist both place `CHEBI:59479` in `MECHANISM_REVIEW` with 0 literature leads, 0 record evidence items, and 0 targets. | Future curator-owned additions to `data/antibiotics/antibacterial/r-chlorphenesin.yaml`, written only through `write_validated_antibiotic` with a `record_curation_event`. |

### Minor

None found.

## Recommended Edits

1. Keep the seeded identity, structure, ChEBI role terms, parent, Reaxys xref, and path unchanged.
2. Before adding a `mode_of_action`, `mode_of_action_target_scope`, target, activity observation, resistance mechanism, producer claim, or causal graph, inspect primary evidence for the exact `CHEBI:59479` enantiomer or an explicitly structure-equivalent source.
3. Do not transfer mechanism or MIC claims from parent `chlorphenesin` (`CHEBI:3642`) to this `(R)` enantiomer unless the source itself demonstrates that the measurement or mechanism applies to the exact same stereochemical form.

## Follow-up Checks

Run the focused and full-corpus gates after any future curation:

1. `just validate data/antibiotics/antibacterial/r-chlorphenesin.yaml`
2. `just validate-strict data/antibiotics/antibacterial/r-chlorphenesin.yaml --out /tmp/r-chlorphenesin-validate-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/r-chlorphenesin-worklist.tsv`
5. `just review-queue --limit 140`
6. `just lint`

Also re-run exact publication searches for `(R)-chlorphenesin`, `CHEBI:59479`, `MXOAEAUPQDYUQM-MRVPVSSYSA-N`, and the exact ChEBI synonyms before concluding that mechanism evidence remains unresolved.

## Additional Notes

- The record has only seed and reseed curation-history events from `2026-08-30`, accurately matching its generated `SEEDED` state.
- The ChEBI source imports antibacterial and antifungal roles, but the repository intentionally files a multi-role record under the highest-priority antimicrobial class and keeps the original ChEBI role list as evidence of additional activity labels.
- Semantic Scholar returned HTTP 429 for four of the five bounded publication searches, so PubMed and local derived queues carried the exact no-candidate result for those searches.
