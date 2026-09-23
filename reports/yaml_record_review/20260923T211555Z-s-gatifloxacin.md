# YAML Record Review: (S)-gatifloxacin

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/unspecified/s-gatifloxacin.yaml
- Started UTC: 2026-09-23T21:15:55Z
- Finished UTC: 2026-09-23T21:15:55Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/antibiotics/unspecified/s-gatifloxacin.yaml` |
| Identifier | `CHEBI:53562` |
| Label | `(S)-gatifloxacin` |
| Filing class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Generated or maintained | Generated record, emitted from `data/raw/chebi_antimicrobials.tsv` through the ChEBI seeding path |
| Source concept | `CHEBI:53562` from ChEBI release `2026-08-30` |
| Minted source key | `antibioticmech:chebi-05171eefd5` |

This review inspected the complete YAML record and treated `data/raw/chebi_antimicrobials.tsv`, `data/antibiotics/PATHS.tsv`, `conf/sources.yaml`, and `curation/record_review_queue.tsv` as the maintained local inputs for seeded ChEBI identity, class, role, structure, and source-owned mechanism claims.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/s-gatifloxacin.yaml` | Passed with no LinkML validation issues. |
| `just validate-strict data/antibiotics/unspecified/s-gatifloxacin.yaml --out /tmp/s-gatifloxacin-validate-strict.tsv` | Passed: 1 file checked, 0 files with `ERROR`, and 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed: all 2,939 expected records were on disk, no unexpected records were present, no generated fields drifted, no identifiers were absent from `PATHS.tsv`, and no stale lockfile rows were present. The only diagnostic was the pre-existing unrelated CARD iclaprim/CHEBI:31724 cross-reference refusal. |
| `just worklist --limit 0 --tsv /tmp/s-gatifloxacin-worklist.tsv` | Passed and regenerated a full worklist. Exact rows for `CHEBI:53562` report `mechanism` and `review-readiness` gaps with 0 CARD targets, 0 resistance edges, 0 source literature leads, 0 record evidence items, and 0 targets. The only diagnostic was the pre-existing unrelated CARD iclaprim/CHEBI:31724 cross-reference refusal. |
| `just review-queue --limit 120` | Passed and listed `(S)-gatifloxacin` as `MECHANISM_REVIEW: mechanism is source-seeded and not curator-checked; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just lint` | Passed before writing this report. |
| `git diff --check` | Passed before writing this report. |
| `git diff --cached --check` | Passed after staging this report. |

No narrower single-record term, reference, or curation-history validator is exposed for this plain ChEBI-seeded record, so the review used the available single-record schema checks plus full-corpus reproducibility and queue/worklist checks.

## Identity and Grounding

The record identity is internally consistent:

| Claim | Review |
|---|---|
| ChEBI grounding | `identifier: CHEBI:53562`, `label: (S)-gatifloxacin`, `grounding_status: EXACT`, and the sole `source_concepts` entry all agree. EBI OLS4 confirms that `CHEBI:53562` is active, non-obsolete, ChEBI-defining, and in the 3-star subset. |
| Raw ChEBI seed | `data/raw/chebi_antimicrobials.tsv` carries the same identifier, label, definition, 3-star status, SMILES, Standard InChI, Standard InChIKey `XUBOMFCQGDBHNK-JTQLQIEISA-N`, formula, charge, masses, IUPAC name, Reaxys xref, and ChEBI topoisomerase-inhibitor mode-of-action role. |
| Structure | SMILES `COc1c(N2CCN[C@@H](C)C2)c(F)cc2c(=O)c(C(=O)O)cn(C3CC3)c12`, Standard InChI, InChIKey, formula `C19H22FN3O4`, charge `0`, average mass `375.4`, and monoisotopic mass `375.15943` are the exact ChEBI-imported values. |
| Parent and sibling boundary | OLS and the local raw ChEBI row agree that `CHEBI:5280` is the broader gatifloxacin parent. OLS relates `CHEBI:53562` to `CHEBI:53560` by `RO_0018039`, matching the local `(R)-gatifloxacin` sibling record with a different InChIKey. |
| Filing class | The retained activity role is the generic ChEBI role `CHEBI:33281` / antimicrobial agent. That role is in local ChEBI scope but is not mapped to a specific `role_to_class` filing class, so `ANTIMICROBIAL_UNSPECIFIED` and the `data/antibiotics/unspecified/` path are consistent with the local mapping. |
| Path lock | `data/antibiotics/PATHS.tsv` maps `CHEBI:53562` to `ANTIMICROBIAL_UNSPECIFIED` / `s-gatifloxacin`, matching the current record path. |

An ignored-inclusive search across `data/antibiotics/PATHS.tsv`, `data/raw`, `curation`, and `reports/yaml_record_review` for `CHEBI:53562`, `gatifloxacin`, `XUBOMFCQGDBHNK-JTQLQIEISA-N`, and `s-gatifloxacin` found the expected ChEBI raw row, path-lock row, ARO/raw parent rows, resistance and target edges for parent gatifloxacin, the prior `(R)-gatifloxacin` report, and no previous exact `(S)-gatifloxacin` review report.

## Evidence

The generated chemistry and ChEBI provenance are supported, but all antimicrobial mechanism claims remain seed-owned:

| Assertion | Support |
|---|---|
| `(S)-gatifloxacin` is a ChEBI-grounded exact record with the listed IUPAC synonym, Reaxys xref, and structure. | Supported by the committed ChEBI inventory row for `CHEBI:53562`, and independently consistent with the live OLS4 `CHEBI:53562` term. |
| The record carries the ChEBI generic antimicrobial-agent role. | Supported by the committed ChEBI row, which lists `CHEBI:33281` as its activity role term. |
| `mode_of_action: NUCLEIC_ACID_SYNTHESIS_INHIBITION` and `mode_of_action_target_scope: HOST_SHARED_TARGET`. | Traceable to the local ChEBI inventory's `CHEBI:50750` EC 5.99.1.3 [DNA topoisomerase (ATP-hydrolysing)] inhibitor role and the seed transform. The YAML correctly warns that this is "Not a curator's mechanistic review"; no record-level evidence has been inspected and attached for the exact `CHEBI:53562` stereoisomer. |

Bounded publication discovery did not find a source that could justify promoting the exact reviewed structure to `REVIEWED`:

| Query | Result |
|---|---|
| Exact `(S)-gatifloxacin` | PubMed returned 2 candidates; Semantic Scholar was rate-limited with HTTP 429. `PMID:35630751` uses `(S)-gatifloxacin` as a DNA-gyrase-inhibitor reference compound in a docking study of plant-derived hydroxyanthraquinones, but it is not primary evidence for exact `(S)-gatifloxacin` antimicrobial activity. `PMID:35492441` describes enantioselective antibody recognition of S-(-)-gatifloxacin and does not support an antimicrobial mode, target, activity observation, or resistance mechanism. |
| Exact `XUBOMFCQGDBHNK-JTQLQIEISA-N` InChIKey through PubMed and Semantic Scholar | PubMed returned 0 candidates; Semantic Scholar was rate-limited with HTTP 429. |
| Exact `1-cyclopropyl-6-fluoro-8-methoxy-7-[(3S)-3-methylpiperazin-1-yl]-4-oxo-1,4-dihydroquinoline-3-carboxylic acid` IUPAC name | PubMed returned 0 candidates; Semantic Scholar was rate-limited with HTTP 429. |
| Parent-style `gatifloxacin enantiomer DNA gyrase topoisomerase S gatifloxacin` query | PubMed returned 0 candidates; Semantic Scholar was rate-limited with HTTP 429. |

## Completeness

The generated identity, source-concept, structure, parent, xref, seed-derived mode, and curation-history fields are complete enough for a ChEBI seed.

The record remains scientifically incomplete because its mode of action and host-shared target scope are source-seeded and not yet supported by record-level primary evidence for the exact `(S)` enantiomer. The record also lacks a curated target, resistance mechanism, direct activity observation, causal graph, or exact source literature lead. The derived worklist keeps it in both the `mechanism` and `review-readiness` queues with no CARD targets, resistance edges, source literature leads, record evidence, or targets, which blocks `REVIEWED` status under the local gate.

The optional target, activity, resistance, producer, causal-graph, dataset, and discussion slots are correctly absent in the sense that the bounded exact searches did not produce inspected support that would justify populating them during this read-only review.

## Findings

### Blocker

None found.

### Major

| Finding | Evidence | Maintained owner |
|---|---|---|
| The record has only a source-seeded, non-curator-checked mode of action and no evidence-backed molecular target, resistance mechanism, direct activity observation, or causal graph for exact `(S)-gatifloxacin`, so it cannot qualify as `REVIEWED`. | The YAML mode fields are labeled "Not a curator's mechanistic review" and the record lacks `molecular_targets`, `resistance_mechanisms`, `activity_observations`, `causal_graphs`, and record-level `evidence`; `curation/record_review_queue.tsv` and the regenerated worklist both place `CHEBI:53562` in `MECHANISM_REVIEW` with 0 literature leads, 0 record evidence items, and 0 targets. Bounded exact searches found only a secondary docking reference mention and an antibody-specific study. | Future curator-owned additions to `data/antibiotics/unspecified/s-gatifloxacin.yaml`, written only through `write_validated_antibiotic` with a `record_curation_event`. |

### Minor

None found.

## Recommended Edits

1. Keep the seeded identity, structure, generic antimicrobial ChEBI role, source-derived mode fields, parent, Reaxys xref, and path unchanged.
2. Before promoting `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, `activity_observations`, `resistance_mechanisms`, or `causal_graphs`, inspect primary evidence for the exact `CHEBI:53562` enantiomer or an explicitly structure-equivalent S-(-)-gatifloxacin source.
3. Do not transfer gatifloxacin DNA-gyrase, topoisomerase-IV, MIC, or resistance claims from the unspecific `CHEBI:5280` parent or the `(R)` enantiomer to this `(S)` enantiomer unless the source itself demonstrates that the measurement or mechanism applies to the exact same stereochemical form.

## Follow-up Checks

Run the focused and full-corpus gates after any future curation:

1. `just validate data/antibiotics/unspecified/s-gatifloxacin.yaml`
2. `just validate-strict data/antibiotics/unspecified/s-gatifloxacin.yaml --out /tmp/s-gatifloxacin-validate-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/s-gatifloxacin-worklist.tsv`
5. `just review-queue --limit 120`
6. `just lint`

Also re-run exact publication searches for `(S)-gatifloxacin`, `CHEBI:53562`, `XUBOMFCQGDBHNK-JTQLQIEISA-N`, and the exact ChEBI IUPAC name before concluding that mechanism evidence remains unresolved.

## Additional Notes

- The record has only seed and reseed curation-history events from `2026-08-30`, accurately matching its generated `SEEDED` state.
- The ChEBI row imports only `reaxys:9090393` for this exact stereoisomer, so the generated `xrefs` section correctly contains only that xref.
- Live OLS relations confirmed the exact parent and enantiomer relations, but did not return the raw ChEBI `CHEBI:50750` DNA-topoisomerase-inhibitor role that drives the source-seeded mode fields.
- Semantic Scholar returned HTTP 429 for all bounded publication searches; PubMed and local derived queues carried the exact low-candidate or no-candidate results for those searches.
