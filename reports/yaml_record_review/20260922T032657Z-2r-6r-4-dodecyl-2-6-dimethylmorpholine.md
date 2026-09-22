# YAML Record Review: (2R,6R)-4-dodecyl-2,6-dimethylmorpholine

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antifungal/2r-6r-4-dodecyl-2-6-dimethylmorpholine.yaml`
- Started UTC: 2026-09-22T03:21:00Z
- Finished UTC: 2026-09-22T03:26:57Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:83301` |
| Label | `(2R,6R)-4-dodecyl-2,6-dimethylmorpholine` |
| Path | `data/antibiotics/antifungal/2r-6r-4-dodecyl-2-6-dimethylmorpholine.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:83301`, version `2026-08-30`, minted key `antibioticmech:chebi-75fe589d11` |
| Source role | `CHEBI:86328` antifungal agrochemical |
| Structure | `SBUKOHLFHYSZNG-QZTJIDSGSA-N`; formula `C18H37NO`; charge `0` |
| Same-structure xrefs | None |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded 4-dodecyl-2,6-dimethylmorpholine
enantiomer. The YAML has source-derived identity, definition, one exact
synonym, one broader ChEBI parent, one antifungal agrochemical role, structure,
and source-concept metadata, but no curator-owned mode of action, target,
resistance mechanism, activity observation, producer, discussion, dataset, or
causal graph.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/2r-6r-4-dodecyl-2-6-dimethylmorpholine.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/2r-6r-4-dodecyl-2-6-dimethylmorpholine.yaml --out /tmp/antibioticmech-chebi-83301-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-83301.tsv` | Pass: the full worklist TSV was written. `CHEBI:83301` appears only on `mechanism` and `review-readiness`; it is absent from `xref-unverified`, `xref-span-conflict`, `xref-name-conflict`, `multi-component`, `moa-scope`, `unknown-mech`, `target-evidence`, `activity-candidate`, and `producer-candidate`. |
| `just review-queue --limit 45` | Pass: `CHEBI:83301` is the next queued record without an existing `reports/yaml_record_review` report; its row says `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:83301` resolves in official OLS as a current, non-obsolete ChEBI term
labeled `(2R,6R)-4-dodecyl-2,6-dimethylmorpholine`. The live OLS annotations
list the same formula, charge, average mass, monoisotopic mass, Standard InChI,
Standard InChIKey, and SMILES as the committed `data/raw/chebi_antimicrobials.tsv`
row and the generated YAML.

The generated record's only `parent_compounds` entry is exactly the official
OLS hierarchical parent of `CHEBI:83301`: `CHEBI:83297`
4-dodecyl-2,6-dimethylmorpholine, whose definition explicitly leaves the
configuration at positions 2 and 6 unknown or unspecified. That parent is a
broader stereochemistry-unspecified structure, not a same-structure identity.

The official OLS graph distinguishes the reviewed R,R enantiomer from its
`CHEBI:83300` S,S enantiomer, whose Standard InChIKey is
`SBUKOHLFHYSZNG-ROUUACIJSA-N`. The graph also links `CHEBI:83302`
rac-trans-4-dodecyl-2,6-dimethylmorpholine to `CHEBI:83301` by a `has part`
edge. Neither edge belongs in `parent_compounds` or `xrefs`.

The generated record correctly has no same-structure xrefs. Official OLS lists
no database cross-reference annotation on exact term `CHEBI:83301`, and the
committed raw row has no xrefs. The nearby xrefs for CAS `1704-28-5`,
PPDB `1128`, and Reaxys `123296` belong to the broader unspecified parent
`CHEBI:83297`; importing them onto the R,R enantiomer would overstate their
stereochemical scope.

The `ANTIFUNGAL` filing class is consistent with the source role. The live
`CHEBI:86328` role term resolves in OLS as current and non-obsolete
`antifungal agrochemical`, and `conf/sources.yaml` maps that ChEBI role to
`ANTIFUNGAL`, which the schema defines to include agrochemical fungicides.

An ignored-inclusive search for `CHEBI:83301`,
`SBUKOHLFHYSZNG-QZTJIDSGSA-N`, `antibioticmech:chebi-75fe589d11`, and
`4-dodecyl-2,6-dimethylmorpholine` across `data/antibiotics`, `data/raw`,
`curation`, `reports`, `.claude`, `docs`, and `README.md` found the expected
PATHS row, generated YAML, raw ChEBI row, review-readiness row, and
stereochemical siblings `CHEBI:83297`, `CHEBI:83298`, and `CHEBI:83300`. It
found no prior dedicated review report, curation decision, curator-inventory
row, generated mechanism, activity observation, target, resistance, or producer
claim resolving `CHEBI:83301`.

## Evidence

The target record has no evidence-bearing assertions. That is schema-valid for
a ChEBI-seeded record because the source concept supplies database provenance
and no mechanism, target, activity, resistance, producer, dataset, or causal
claim has been promoted into curator-owned slots.

The committed raw ChEBI row for `CHEBI:83301` has no source literature
reference and no database xref. The review-readiness queue therefore reports
zero source literature leads, zero record evidence items, and zero targets.

A bounded repository publication search for exact labels and the Standard
InChIKey:

`"(2R,6R)-4-dodecyl-2,6-dimethylmorpholine" OR "(R,R)-4-dodecyl-2,6-dimethylmorpholine" OR "SBUKOHLFHYSZNG-QZTJIDSGSA-N"`

found zero PubMed candidates. A second search for the broader phrase
`"4-dodecyl-2,6-dimethylmorpholine" aldimorph morpholine fungicide` also found
zero PubMed candidates. Semantic Scholar returned HTTP 429 for both searches.

## Completeness

The record is incomplete as a reviewed antifungal record. It has exact ChEBI
identity, structure, a broader stereochemistry-unspecified parent, and an
antifungal agrochemical role, but no inspected primary paper or public
compound registry lead resolves the R,R enantiomer into a supported mode of
action, molecular target, resistance mechanism, activity observation, producer,
dataset, or causal graph.

The empty `mode_of_action`, `mode_of_action_target_scope`,
`molecular_targets`, `resistance_mechanisms`, `activity_spectrum`,
`producer_organisms`, `clinical_status_assertions`, `datasets`, `discussions`,
and `causal_graphs` slots are preferable to over-scoped filler. Morpholine
fungicide family members can inhibit sterol biosynthesis, but no inspected
source during this review supported assigning that mechanism to exact
`CHEBI:83301`.

`just worklist` correctly reports a `mechanism` row for `CHEBI:83301` because
there is no curator-owned or source-seeded mode of action and no CARD target or
resistance edge to build on.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | No mechanism or claim-level antifungal evidence has been resolved for the exact R,R stereoisomer. | The YAML has no evidence-bearing objects; the ChEBI raw row has no literature reference or xref; exact-label, InChIKey, and broader parent-name publication searches found zero PubMed candidates; `just worklist` queues `CHEBI:83301` only on `mechanism` and `review-readiness`. | Future curator-owned fields on `data/antibiotics/antifungal/2r-6r-4-dodecyl-2-6-dimethylmorpholine.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI later supplies source xrefs for this exact term, the ChEBI inventory extractor owns that refresh. |

No blocker identity, structure, schema, xref, or parentage findings were found.

No minor findings.

## Recommended Edits

1. Leave `mode_of_action`, `molecular_targets`, `resistance_mechanisms`,
   `activity_spectrum`, and `causal_graphs` empty until an exact
   `CHEBI:83301` source is found. Do not copy mechanism, activity, or registry
   xrefs from the stereochemistry-unspecified `CHEBI:83297` parent, the
   `CHEBI:83298` cis form, or the `CHEBI:83300` S,S enantiomer.
2. Recheck ChEBI and public literature for exact `CHEBI:83301` references
   during a later family-level review of the `CHEBI:83297` dodecyl
   dimethylmorpholine cluster. Any supported mechanism should be curated on
   each exact stereochemical record only after the inspected source scopes the
   claim to that structure.
3. If ChEBI later adds database cross-references, keep exact R,R enantiomer
   xrefs separate from the parent term's CAS, PPDB, and Reaxys identifiers
   unless the source explicitly identifies the same Standard InChIKey
   `SBUKOHLFHYSZNG-QZTJIDSGSA-N`.

## Follow-up Checks

After any exact-term curation or source refresh, rerun:

1. `just validate data/antibiotics/antifungal/2r-6r-4-dodecyl-2-6-dimethylmorpholine.yaml`
2. `just validate-strict data/antibiotics/antifungal/2r-6r-4-dodecyl-2-6-dimethylmorpholine.yaml --out /tmp/antibioticmech-chebi-83301-validation.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-83301.tsv`
5. `just review-queue --limit 45`
6. `just qc`

Manually compare `CHEBI:83301` against `CHEBI:83297`, `CHEBI:83298`, and
`CHEBI:83300` after any curation to confirm that parent, cis-form, or opposite
enantiomer evidence has not been promoted onto the exact R,R child.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, so they
included ignored `reports/` files.

`runoak` was not available in this shell, so official ChEBI term checks were
performed against the EBI OLS4 HTTPS API.

Semantic Scholar returned HTTP 429 for both repository publication searches;
the PubMed side of both searches completed.
