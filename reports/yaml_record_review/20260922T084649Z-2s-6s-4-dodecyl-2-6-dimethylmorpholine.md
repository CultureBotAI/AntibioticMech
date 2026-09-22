# YAML Record Review: (2S,6S)-4-dodecyl-2,6-dimethylmorpholine

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antifungal/2s-6s-4-dodecyl-2-6-dimethylmorpholine.yaml`
- Started UTC: 2026-09-22T08:40:45Z
- Finished UTC: 2026-09-22T08:46:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:83300` |
| Label | `(2S,6S)-4-dodecyl-2,6-dimethylmorpholine` |
| Path | `data/antibiotics/antifungal/2s-6s-4-dodecyl-2-6-dimethylmorpholine.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:83300`, version `2026-08-30`, minted key `antibioticmech:chebi-2f8170a27d` |
| Source role | `CHEBI:86328` antifungal agrochemical |
| Parent compound | `CHEBI:83297` 4-dodecyl-2,6-dimethylmorpholine |
| Structure | `SBUKOHLFHYSZNG-ROUUACIJSA-N`; formula `C18H37NO`; charge `0` |
| Same-structure xrefs | None |
| Source literature leads | None |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded antifungal record. The YAML has
source-derived exact ChEBI grounding, definition, two exact ChEBI synonyms, one
stereochemically broader parent, one antifungal-agrochemical role, structure,
and source-concept metadata. It has no generated or curator-owned mode of
action, molecular target, activity observation, resistance mechanism, producer,
discussion, dataset, causal graph, same-structure xref, source literature lead,
or claim-level evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/2s-6s-4-dodecyl-2-6-dimethylmorpholine.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/2s-6s-4-dodecyl-2-6-dimethylmorpholine.yaml --out /tmp/antibioticmech-chebi-83300-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-83300.tsv` | Pass: the full worklist TSV was written. `CHEBI:83300` appears on `mechanism` and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 52` | Pass: `CHEBI:83300` is queued with `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

The `CHEBI:83300` term resolves in official OLS as a current, non-obsolete
ChEBI child of `CHEBI:83297`. The live OLS child object is labeled
`(2S,6S)-4-dodecyl-2,6-dimethylmorpholine` and lists the same formula, charge,
average mass, monoisotopic mass, Standard InChI, Standard InChIKey, and SMILES
as the committed `data/raw/chebi_antimicrobials.tsv` row and the generated
YAML.

The generated `parent_compounds` value is exactly the live OLS hierarchical
parent of `CHEBI:83300`: `CHEBI:83297`, the stereochemically unspecified
4-dodecyl-2,6-dimethylmorpholine. Live OLS lists three hierarchical children
under `CHEBI:83297`: `CHEBI:83298` cis-4-dodecyl-2,6-dimethylmorpholine,
`CHEBI:83300` S,S 4-dodecyl-2,6-dimethylmorpholine, and `CHEBI:83301` R,R
4-dodecyl-2,6-dimethylmorpholine. Their Standard InChIKeys are different, so
evidence or xrefs for the broader parent, the cis form, or the R,R enantiomer
must not be copied to this exact S,S term.

The `ANTIFUNGAL` filing class and empty `mode_of_action` are consistent with
the ChEBI source role. The live `CHEBI:86328` role resolves in OLS as current
and non-obsolete `antifungal agrochemical`, and `conf/sources.yaml` maps that
role to `ANTIFUNGAL` without a mechanism mapping.

No generated same-structure xref is expected for this term. Live OLS reports no
`obo_xref` values for `CHEBI:83300`, and the raw ChEBI inventory row has empty
`xrefs` and `citations` columns. The CAS, PPDB, and Reaxys xrefs on
`CHEBI:83297` identify the stereochemically unspecified parent and are not
exact same-structure xrefs for `CHEBI:83300`.

An ignored-inclusive search for `CHEBI:83300`, the exact label, the filename
stem, and the exact Standard InChIKey across `data/antibiotics`, `data/raw`,
`curation`, `reports`, and the full `/tmp` worklist found only the expected
PATHS row, generated YAML, raw ChEBI row, worklist/review-readiness rows, and
an older sibling report that mentions `CHEBI:83300` while warning not to merge
it with `CHEBI:83301`. It found no prior dedicated review report, curation
decision, curator-inventory row, generated activity observation, molecular
target, resistance, producer, or causal-graph claim resolving `CHEBI:83300`.

## Evidence

The record's only antimicrobial assertion is inherited from ChEBI role
`CHEBI:86328`, `antifungal agrochemical`. That is sufficient to file the record
under `ANTIFUNGAL`; it is not a compound-specific mechanism or activity
measurement and it is not evidence for a target.

The committed raw ChEBI row for `CHEBI:83300` has no same-structure xrefs and
no source-literature leads. The record has no evidence-bearing
`MolecularTarget`, `ActivityObservation`, `ResistanceMechanism`,
`ProducerOrganism`, `Dataset`, or `CausalGraph` objects, so no primary source
has been promoted onto a curator-owned claim.

A bounded repository publication search found zero PubMed candidates for the
exact Standard InChIKey `SBUKOHLFHYSZNG-ROUUACIJSA-N`, the exact label
`(2S,6S)-4-dodecyl-2,6-dimethylmorpholine`, the exact synonym
`(S,S)-4-dodecyl-2,6-dimethylmorpholine`, or the exact parent label
`4-dodecyl-2,6-dimethylmorpholine`. Semantic Scholar returned HTTP 429 for the
combined exact InChIKey and label query.

## Completeness

The record is incomplete as a reviewed antifungal-agrochemical record. It has
exact ChEBI identity, exact S,S stereochemistry, a validated structure, a
correctly broader ChEBI parent, an antifungal role, and seed provenance, but no
mode of action, target, activity observation, dataset, discussion, or causal
graph.

The empty mechanism fields are better than a guessed mechanism. The
`antifungal agrochemical` role does not state whether this morpholine acts on
ergosterol biosynthesis, membrane integrity, or another fungal process, and it
does not state whether any assay measured the S,S enantiomer rather than the
stereochemically mixed parent.

The empty `xrefs`, `molecular_targets`, `resistance_mechanisms`,
`activity_spectrum`, `producer_organisms`, `clinical_status_assertions`,
`datasets`, `discussions`, and `causal_graphs` slots are preferable to
over-scoped filler. The inspected ChEBI and local sources do not provide a
same-structure database accession, a quantitative activity measurement, a
fungal strain context, or a primary source that would support a narrow curator
claim for exact `CHEBI:83300`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The exact S,S enantiomer has an antifungal filing role but no mechanism, target, or activity evidence. | `CHEBI:83300` has no `mode_of_action`, no `mode_of_action_target_scope`, zero record evidence items, zero targets, zero activity observations, and zero ChEBI source-literature leads; exact PubMed searches for the InChIKey, label, S,S synonym, and parent label returned zero candidates. | Future curator-owned fields on `data/antibiotics/antifungal/2s-6s-4-dodecyl-2-6-dimethylmorpholine.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI later adds exact `CHEBI:83300` xrefs or citations, the ChEBI inventory extractor owns that refresh. |

No blocker identity, structure, schema, class, parentage, xref, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Search for primary activity or mechanism sources that explicitly distinguish
   exact `(2S,6S)-4-dodecyl-2,6-dimethylmorpholine` from the R,R enantiomer,
   cis form, and stereochemically unspecified `CHEBI:83297` parent before
   adding any mechanism or activity claims.
2. Add a `mode_of_action`, `mode_of_action_target_scope`, and any fungal
   `MolecularTarget` only if a primary source maps a biochemical effect to this
   exact S,S structure. Do not infer a target from the antifungal agrochemical
   class alone.
3. Add `activity_spectrum` rows only for exact S,S observations with source
   assay context, organism or strain scope, measurement value, qualifier, and
   units. Leave broad parent-compound assays off this record unless the source
   explicitly says the assayed material was `CHEBI:83300`.
4. Keep the CAS, PPDB, and Reaxys xrefs from `CHEBI:83297` off this record
   unless an exact registry page is found for the S,S enantiomer. Parent-level
   xrefs do not denote the same structure.
5. Add a `Discussion` only for a concrete unresolved literature conflict or a
   curation task with a checked citation trail. No such conflict was identified
   in this bounded review.

## Follow-up Checks

After any exact-term curation or source refresh, rerun:

1. `just validate data/antibiotics/antifungal/2s-6s-4-dodecyl-2-6-dimethylmorpholine.yaml`
2. `just validate-strict data/antibiotics/antifungal/2s-6s-4-dodecyl-2-6-dimethylmorpholine.yaml --out /tmp/antibioticmech-chebi-83300-validation.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-83300.tsv`
5. `just review-queue --limit 52`
6. `just qc`

Manually compare future xref, mechanism, target, and activity curation against
`CHEBI:83297`, `CHEBI:83298`, and `CHEBI:83301` to confirm that broad-parent,
cis-form, or R,R-enantiomer evidence has not been attached to exact
`CHEBI:83300`.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, so they
included ignored `reports/` files.

`runoak` was not available in this shell, so official ChEBI term checks were
performed against the EBI OLS4 HTTPS API.

The direct OLS term endpoint for `CHEBI:83300` returned an empty body once, and
two OLS search requests failed DNS resolution transiently. The OLS hierarchical
parent, hierarchical children, enantiomer relation, `CHEBI:83297`, and
`CHEBI:86328` endpoints resolved.

Semantic Scholar returned HTTP 429 for the combined exact InChIKey and label
search; exact PubMed-only searches completed and returned no candidates.
