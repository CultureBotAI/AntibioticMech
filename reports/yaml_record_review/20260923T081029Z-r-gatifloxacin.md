# YAML Record Review: (R)-gatifloxacin

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/unspecified/r-gatifloxacin.yaml
- Started UTC: 2026-09-23T08:10:29Z
- Finished UTC: 2026-09-23T08:10:29Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/antibiotics/unspecified/r-gatifloxacin.yaml` |
| Identifier | `CHEBI:53560` |
| Label | `(R)-gatifloxacin` |
| Filing class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Generated or maintained | Generated record, emitted from `data/raw/chebi_antimicrobials.tsv` through the ChEBI seeding path |
| Source concept | `CHEBI:53560` from ChEBI release `2026-08-30` |
| Minted source key | `antibioticmech:chebi-f75f42b545` |

This review inspected the complete YAML record and treated `data/raw/chebi_antimicrobials.tsv`, `data/antibiotics/PATHS.tsv`, `conf/sources.yaml`, and `curation/record_review_queue.tsv` as the maintained local inputs for seeded ChEBI identity, class, role, structure, and source-owned mechanism claims.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/r-gatifloxacin.yaml` | Passed with no LinkML validation issues. |
| `just validate-strict data/antibiotics/unspecified/r-gatifloxacin.yaml --out /tmp/r-gatifloxacin-validate-strict.tsv` | Passed: 1 file checked, 0 files with `ERROR`, and 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed: all 2,939 expected records were on disk, no unexpected records were present, no generated fields drifted, no identifiers were absent from `PATHS.tsv`, and no stale lockfile rows were present. The only diagnostic was the pre-existing unrelated CARD iclaprim/CHEBI:31724 cross-reference refusal. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-next-review-worklist.tsv` | Passed and regenerated a full worklist. Exact rows for `CHEBI:53560` report `mechanism` and `review-readiness` gaps with 0 CARD targets, 0 resistance edges, 0 source literature leads, 0 record evidence items, and 0 targets. The only diagnostic was the pre-existing unrelated CARD iclaprim/CHEBI:31724 cross-reference refusal. |
| `just review-queue --limit 120` | Passed and listed `(R)-gatifloxacin` as `MECHANISM_REVIEW: mechanism is source-seeded and not curator-checked; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just lint` | Passed before writing this report. |
| `git diff --check` | Passed before writing this report. |
| `git diff --cached --check` | Passed after staging this report. |

No narrower single-record term, reference, or curation-history validator is exposed for this plain ChEBI-seeded record, so the review used the available single-record schema checks plus full-corpus reproducibility and queue/worklist checks.

## Identity and Grounding

The record identity is internally consistent:

| Claim | Review |
|---|---|
| ChEBI grounding | `identifier: CHEBI:53560`, `label: (R)-gatifloxacin`, `grounding_status: EXACT`, and the sole `source_concepts` entry all agree. |
| Raw ChEBI seed | `data/raw/chebi_antimicrobials.tsv` carries the same identifier, label, definition, 3-star status, SMILES, Standard InChI, Standard InChIKey `XUBOMFCQGDBHNK-SNVBAGLBSA-N`, formula, charge, masses, IUPAC name, and ChEBI topoisomerase-inhibitor mode-of-action role. |
| Structure | SMILES `COc1c(N2CCN[C@H](C)C2)c(F)cc2c(=O)c(C(=O)O)cn(C3CC3)c12`, Standard InChI, InChIKey, formula `C19H22FN3O4`, charge `0`, average mass `375.4`, and monoisotopic mass `375.15943` are the exact ChEBI-imported values. |
| Parent boundary | `CHEBI:5280` is the broader gatifloxacin parent, and `CHEBI:53562` is the sibling `(S)-gatifloxacin` enantiomer with a different InChIKey, so this record denotes the intended individual stereoisomer. |
| Filing class | The retained activity role is the generic ChEBI role `CHEBI:33281` / antimicrobial agent. That role is in local ChEBI scope but is not mapped to a specific `role_to_class` filing class, so `ANTIMICROBIAL_UNSPECIFIED` and the `data/antibiotics/unspecified/` path are consistent with the local mapping. |
| Source-owned mode | ChEBI also imports the mode-of-action role `CHEBI:50750`, locally mapped to `NUCLEIC_ACID_SYNTHESIS_INHIBITION` and `HOST_SHARED_TARGET`; the YAML notes correctly say the assignment is source-seeded and not a curator's mechanistic review. |
| Path lock | `data/antibiotics/PATHS.tsv` maps `CHEBI:53560` to `ANTIMICROBIAL_UNSPECIFIED` / `r-gatifloxacin`, matching the current record path. |

An ignored-inclusive search across `data/raw`, `curation`, `reports/yaml_record_review`, and `data/antibiotics` for `CHEBI:53560`, `antibioticmech:chebi-f75f42b545`, `XUBOMFCQGDBHNK-SNVBAGLBSA-N`, and `r-gatifloxacin` found only the expected ChEBI raw row, path-lock row, review-queue row, and exact YAML record. It found no prior exact review report for this identifier.

## Evidence

There is no claim-level literature evidence to audit because this seeded record has no `molecular_targets`, `activity_observations`, `resistance_mechanisms`, `producer_organisms`, `causal_graphs`, datasets, discussions, or record-level `evidence`.

The existing scientific assertions are seed-owned ChEBI database assertions:

| Assertion | Support |
|---|---|
| `(R)-gatifloxacin` is a ChEBI-grounded exact record with the listed IUPAC synonym and structure. | Supported by the committed ChEBI inventory row for `CHEBI:53560`. |
| The record carries the ChEBI generic antimicrobial-agent role. | Supported by the same ChEBI row, which lists `CHEBI:33281` as its activity role term. |
| The record carries `NUCLEIC_ACID_SYNTHESIS_INHIBITION` and `HOST_SHARED_TARGET`. | Supported only as a source-seeded ChEBI role transform from `CHEBI:50750`; no primary paper has been inspected for this exact enantiomer. |

Bounded publication discovery did not find a source that could justify promoting the source-seeded mechanism or adding exact-enantiomer target/activity claims:

| Query | Result |
|---|---|
| Exact `(R)-gatifloxacin` label through PubMed and Semantic Scholar | Mostly returned generic gatifloxacin candidates. `PMID:35492441` specifically mentions the `R` enantiomer only as an antibody cross-reactivity comparator against an `S`-gatifloxacin antibody; it is not antimicrobial mechanism, target, resistance, or activity evidence. |
| Exact `XUBOMFCQGDBHNK-SNVBAGLBSA-N` InChIKey through PubMed and Semantic Scholar | PubMed returned 0 candidates; Semantic Scholar was rate-limited with HTTP 429. |
| Exact ChEBI IUPAC name through PubMed and Semantic Scholar | PubMed returned 0 candidates; Semantic Scholar was rate-limited with HTTP 429. |
| Parent/enantiomer `gatifloxacin enantiomer DNA gyrase topoisomerase R gatifloxacin` query | PubMed returned 0 candidates; Semantic Scholar was rate-limited with HTTP 429. |

## Completeness

The generated identity, structure, source-concept, parent, source-seeded mechanism, and curation-history fields are complete enough for a ChEBI seed.

The record remains scientifically incomplete because no curator has checked the source-seeded mode of action against evidence for exact `(R)-gatifloxacin`, and the record has no target, resistance mechanism, causal graph, or direct activity observation. The derived worklist keeps it in both the `mechanism` and `review-readiness` queues with no CARD targets, resistance edges, source literature leads, record evidence, or targets. That gap blocks `REVIEWED` status under the local gate because the mode of action has not been checked.

The optional target, activity, resistance, producer, causal-graph, dataset, xref, and discussion slots are correctly absent in the sense that the bounded exact searches did not produce inspected support that would justify populating them during this read-only review.

## Findings

### Blocker

None found.

### Major

| Finding | Evidence | Maintained owner |
|---|---|---|
| The record has a source-seeded mode of action and target scope but no primary evidence for exact `(R)-gatifloxacin`, so the mechanism cannot yet qualify as curator-checked and the record cannot qualify as `REVIEWED`. | `mode_of_action_notes` explicitly mark the mechanism as not curator-reviewed; the YAML lacks `molecular_targets`, `resistance_mechanisms`, `activity_observations`, and `causal_graphs`; `curation/record_review_queue.tsv` and the regenerated worklist both place `CHEBI:53560` in `MECHANISM_REVIEW` with 0 source literature leads, 0 record evidence items, and 0 targets. | Future curator-owned additions to `data/antibiotics/unspecified/r-gatifloxacin.yaml`, written only through `write_validated_antibiotic` with a `record_curation_event`. |

### Minor

None found.

## Recommended Edits

1. Keep the seeded identity, structure, generic antimicrobial role, parent, source concept, ChEBI-derived mode, and path unchanged.
2. Before promoting the `NUCLEIC_ACID_SYNTHESIS_INHIBITION` claim to curator-checked evidence, inspect primary evidence for the exact `CHEBI:53560` enantiomer or an explicitly structure-equivalent source.
3. Do not transfer gatifloxacin DNA-gyrase, topoisomerase-IV, MIC, clinical-efficacy, or resistance claims from the unspecific `CHEBI:5280` parent or the `(S)` enantiomer to this `(R)` enantiomer unless the source itself demonstrates that the measurement or mechanism applies to the exact same stereochemical form.

## Follow-up Checks

Run the focused and full-corpus gates after any future curation:

1. `just validate data/antibiotics/unspecified/r-gatifloxacin.yaml`
2. `just validate-strict data/antibiotics/unspecified/r-gatifloxacin.yaml --out /tmp/r-gatifloxacin-validate-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/r-gatifloxacin-worklist.tsv`
5. `just review-queue --limit 120`
6. `just lint`

Also re-run exact publication searches for `(R)-gatifloxacin`, `CHEBI:53560`, `XUBOMFCQGDBHNK-SNVBAGLBSA-N`, and the exact ChEBI IUPAC name before concluding that mechanism evidence remains unresolved.

## Additional Notes

- The record has only seed and reseed curation-history events from `2026-08-30`, accurately matching its generated `SEEDED` state.
- The ChEBI row does not import xrefs for this record, so the generated record correctly has no `xrefs` section.
- Parent-level gatifloxacin evidence exists and the parent ChEBI row has literature leads, but this read-only review did not inspect full text far enough to justify a stereoisomer-specific curator claim.
- Semantic Scholar returned HTTP 429 for three of four bounded publication searches; PubMed carried the exact no-candidate result for those searches.
