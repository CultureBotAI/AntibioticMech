# YAML Record Review: (Z)-dimethomorph

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antifungal/z-dimethomorph.yaml
- Started UTC: 2026-09-24T03:51:07Z
- Finished UTC: 2026-09-24T03:51:07Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | CHEBI:83427 |
| Label | (Z)-dimethomorph |
| Path | data/antibiotics/antifungal/z-dimethomorph.yaml |
| Class | ANTIFUNGAL |
| Status | SEEDED |
| Grounding | EXACT |
| Source concept | CHEBI:83427, source version 2026-08-30 |
| Standard InChIKey | QNBTYORWCCMPQP-JXAWBTAJSA-N |
| Maintained owner | Generated from data/raw/chebi_antimicrobials.tsv plus data/antibiotics/PATHS.tsv; do not hand-edit the generated YAML |

The target resolves unambiguously to
`data/antibiotics/antifungal/z-dimethomorph.yaml`. An
ignored-file-inclusive search for `CHEBI:83427`, `(Z)-dimethomorph`,
`z-dimethomorph`, and `dimethomorph` across `data/antibiotics`, `data/raw`,
`curation`, and `reports/yaml_record_review` found the target, its exact
`PATHS.tsv` row, the exact raw ChEBI row, the exact `review-readiness` queue
row, and the broader `CHEBI:81848` dimethomorph-mixture sibling. A separate
ignored-file-inclusive `find` found no prior exact
`reports/yaml_record_review/*z-dimethomorph*` report.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/z-dimethomorph.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/z-dimethomorph.yaml --out /tmp/z-dimethomorph-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2939 records expected, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/z-dimethomorph-worklist.tsv` | Passed; `CHEBI:83427` appears only in `mechanism` and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Passed; `CHEBI:83427` is the first queue row without an exact one-record review report after normalizing backticked and unbackticked report headers. |
| `just lint` | Passed; `ruff` reported `All checks passed!`. |
| `git diff --cached --check` | Passed after staging this ignored report. |

`just verify-corpus` and `just worklist` both emitted the known CARD
`ARO:3000337` / iclaprim cross-reference refusal; that warning is unrelated to
this ChEBI-only record.

The repository exposes `validate`, `validate-strict`, `verify-corpus`,
`worklist`, `review-queue`, and `lint`; it does not expose narrower
single-record term, reference, or history validators for a plain ChEBI-seeded
record with no record-level citations.

## Identity and Grounding

The ChEBI identity is exact. OLS4 resolves `CHEBI:83427` to `(Z)-dimethomorph`
with the same formula, Standard InChI, Standard InChIKey
`QNBTYORWCCMPQP-JXAWBTAJSA-N`, charge, average mass, monoisotopic mass,
`cas:113210-98-3`, and `reaxys:11343579` carried by the local raw ChEBI row and
generated record.

The isomer boundary is correct:

- `CHEBI:83427` is the `Z` isomer and has the stereospecific InChIKey
  `QNBTYORWCCMPQP-JXAWBTAJSA-N`.
- `CHEBI:81848` is the broader unspecified mixture of `E`- and
  `Z`-dimethomorph and has the nonstereospecific InChIKey
  `QNBTYORWCCMPQP-UHFFFAOYSA-N`.

The `parent_compounds` values are strictly broader ChEBI terms:

- `CHEBI:140326`: tertiary carboxamide.
- `CHEBI:35618`: aromatic ether.
- `CHEBI:51751`: enamide.
- `CHEBI:83403`: monochlorobenzenes.
- `CHEBI:87134`: morpholine fungicide.

The broader dimethomorph-mixture record has `kegg.compound:C18583`,
`pesticides:dimethomorph`, `ppdb:245`, patent, and Reaxys xrefs that were
correctly not projected onto exact `CHEBI:83427`. The exact `(Z)` isomer record
remains a ChEBI-only structure with no CARD/ARO merge.

The filing class is consistent with imported source assertions. ChEBI assigns
`CHEBI:24127` fungicide and `CHEBI:35718` antifungal-agent roles to
`CHEBI:83427`, and the record is filed as `ANTIFUNGAL`.

## Evidence

This record has no record-level `evidence`, no `mode_of_action`, no
`molecular_targets`, no `activity_spectrum`, no `resistance_mechanisms`, and no
`causal_graphs`. That is structurally valid for a ChEBI seed, but it means the
exact `(Z)` dimethomorph isomer has only upstream database provenance and no
primary-paper support for a compound-specific antifungal mechanism.

The local raw ChEBI row for `CHEBI:83427` carries four PMID leads. Fetching
those exact PMIDs from PubMed found environmental fate, LC/ESI-MS isomer
response, mixed-formulation field residue, and heterogeneous ozonolysis papers;
the metadata did not show a primary target or antimicrobial mode-of-action
claim for the exact `(Z)` isomer.

Bounded PubMed checks did not resolve the missing mechanism:

- An exact-identifier and exact-name query over `QNBTYORWCCMPQP-JXAWBTAJSA-N`,
  `CHEBI:83427`, `(Z)-dimethomorph`, `Z-Dimethomorph`, `Dimethomorph Z`, and
  `113210-98-3` broadened to dimethomorph residue, degradation, toxicity, and
  oomycete-activity hits.
- A broader `dimethomorph` mechanism query returned recent combination,
  activity, environmental, sensitivity, and RNA-seq leads.
- A focused `dimethomorph` query for cell-wall, cellulose-synthase, and `CesA`
  terms returned carboxylic-acid-amide fungicide mechanism and resistance
  leads, but those leads were not inspected far enough to support a
  `CHEBI:83427` molecular-target assertion and would need exact compound-form
  checking before curation.

Semantic Scholar was not needed after the exact ChEBI PMID fetch and bounded
PubMed searches found enough primary dimethomorph leads to define the remaining
manual curation task. Google Scholar was not used.

## Completeness

The generated source concept, exact ChEBI grounding, isomer boundary,
structural-class parentage, structure fields, antifungal filing class, and seed
history are sufficient for a ChEBI-only seed.

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, and
  `causal_graphs` are absent. This record should remain below `REVIEWED` until
  a curator either adds evidence that supports an exact `(Z)-dimethomorph`
  antifungal mechanism or adds a curator-owned veto explaining why only
  mixture-level or carboxylic-acid-amide class leads exist.
- `activity_spectrum` is absent. Future activity curation should use measured
  organism, strain or isolate, assay, value, qualifier, units, compound form,
  and evidence rather than generalizing from the morpholine-fungicide parent or
  from mixture-level dimethomorph papers.

Empty optional slots that are acceptable in this generated seed:

- `resistance_mechanisms`: no CARD target or resistance edge was available for
  this exact ChEBI record.
- `producer_organisms`: no producer-candidate worklist row was present.
- `clinical_status_assertions`: no regulatory source was imported for this
  exact ChEBI record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The exact `(Z)-dimethomorph` record has no reviewed antifungal mechanism. | `just worklist --limit 0 --tsv /tmp/z-dimethomorph-worklist.tsv` lists `CHEBI:83427` in `mechanism` with `0 CARD target(s), 0 resistance edge(s) to build on` and in `review-readiness` with `MECHANISM_REVIEW: mechanism is absent; 4 source literature lead(s), 0 record evidence item(s), 0 target(s)`; the ChEBI-listed PMIDs are not mechanism sources in PubMed metadata; bounded dimethomorph PubMed checks yielded follow-up leads but no inspected exact-isomer target claim. | Add an evidence-backed curator-owned mechanism to `data/antibiotics/antifungal/z-dimethomorph.yaml` through `write_validated_antibiotic`, or add a curator-owned veto explaining why the mechanism remains unknown for exact `(Z)-dimethomorph`. |

No blockers found. No minor findings found.

## Recommended Edits

1. Inspect the carboxylic-acid-amide mechanism and `CesA` resistance leads for
   exact dimethomorph compound form, organism, target, and assay scope.
2. Add a `CURATOR:`-owned mechanism, target scope, molecular target, and causal
   graph only when a source supports exact `(Z)-dimethomorph`; otherwise leave a
   curator-owned veto documenting why only mixture-level or class-level evidence
   was found.
3. Add measured `activity_spectrum` rows only when the source provides complete
   organism, strain or isolate, assay, value, units, compound form, and evidence
   for `(Z)-dimethomorph`.

## Follow-up Checks

- After any mechanism or activity curation, run
  `just validate-strict data/antibiotics/antifungal/z-dimethomorph.yaml --out /tmp/antibioticmech-record-validation.tsv`,
  `just verify-corpus --summary`,
  `just worklist --limit 0 --tsv /tmp/z-dimethomorph-worklist.tsv`, and
  `just lint`.
- Re-run OLS4 checks for `CHEBI:83427`, `CHEBI:81848`, `CHEBI:140326`,
  `CHEBI:35618`, `CHEBI:51751`, `CHEBI:83403`, and `CHEBI:87134` if future
  edits touch identity, xrefs, or parentage.

## Additional Notes

- The ignored-file-inclusive resolution search covered `data/antibiotics`,
  `data/raw`, `curation`, and `reports/yaml_record_review`; a separate
  ignored-file-inclusive `find` found no prior exact report for
  `z-dimethomorph`.
- The repository exposes only full-corpus worklist categories for mechanism,
  cross-reference, producer, target-evidence, and review-readiness checks.
  `CHEBI:83427` was absent from all inspected queues except `mechanism` and
  `review-readiness`.
