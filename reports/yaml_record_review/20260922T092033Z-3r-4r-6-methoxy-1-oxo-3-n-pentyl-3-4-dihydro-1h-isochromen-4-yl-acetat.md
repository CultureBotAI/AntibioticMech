# YAML Record Review: (3R,4R)-(−)-6-methoxy-1-oxo-3-n-pentyl-3,4-dihydro-1H-isochromen-4-yl-acetate

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antifungal/3r-4r-6-methoxy-1-oxo-3-n-pentyl-3-4-dihydro-1h-isochromen-4-yl-acetat.yaml`
- Started UTC: 2026-09-22T09:15:45Z
- Finished UTC: 2026-09-22T09:20:33Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:66698` |
| Label | `(3R,4R)-(−)-6-methoxy-1-oxo-3-n-pentyl-3,4-dihydro-1H-isochromen-4-yl-acetate` |
| Path | `data/antibiotics/antifungal/3r-4r-6-methoxy-1-oxo-3-n-pentyl-3-4-dihydro-1h-isochromen-4-yl-acetat.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:66698`, version `2026-08-30`, minted key `antibioticmech:chebi-3959766aad` |
| Source role | `CHEBI:35718` antifungal agent |
| Parent compounds | `CHEBI:35618`; `CHEBI:38762`; `CHEBI:47622` |
| Structure | `XFZDFYYRUDDKBS-HZPDHXFCSA-N`; formula `C17H22O5`; charge `0` |
| Same-structure xrefs | `reaxys:15809380` |
| Source literature lead | `PMID:17870137` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded antifungal record. The YAML has
source-derived exact ChEBI grounding, a ChEBI definition, two exact ChEBI
synonyms, three ChEBI parents, one Reaxys xref, one antifungal role, structure,
and source-concept metadata. It has no generated or curator-owned mode of
action, molecular target, activity observation, resistance mechanism, producer,
discussion, dataset, causal graph, or claim-level evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/3r-4r-6-methoxy-1-oxo-3-n-pentyl-3-4-dihydro-1h-isochromen-4-yl-acetat.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/3r-4r-6-methoxy-1-oxo-3-n-pentyl-3-4-dihydro-1h-isochromen-4-yl-acetat.yaml --out /tmp/antibioticmech-chebi-66698-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-66698.tsv` | Pass: the full worklist TSV was written. `CHEBI:66698` appears on `mechanism`, `producer-candidate`, `activity-candidate`, and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 53` | Pass: `CHEBI:66698` is queued with `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:66698` resolves in official OLS as a current, non-obsolete ChEBI term
labeled with the same structure name as the generated record. Live OLS uses
ASCII `(-)` while the committed raw ChEBI inventory and generated record use
the typographic minus sign `−`; this is a label-glyph difference, not an
identity or structure conflict.

The live OLS annotations list the same formula, charge, average mass,
monoisotopic mass, Standard InChI, Standard InChIKey, SMILES, PubMed
cross-reference, and Reaxys cross-reference as the committed
`data/raw/chebi_antimicrobials.tsv` row. The raw inventory exposes `pubmed`
provenance in its `citations` column and `reaxys:15809380` as the single
same-structure `xrefs` row; the generated record correctly preserves only the
Reaxys chemical identity xref.

The generated `parent_compounds` values are exactly the live OLS hierarchical
parents of `CHEBI:66698`: `CHEBI:35618` aromatic ether, `CHEBI:38762`
isochromanes, and `CHEBI:47622` acetate ester.

The `ANTIFUNGAL` filing class and empty `mode_of_action` are consistent with
the ChEBI source role. The live `CHEBI:35718` role resolves in OLS as current
and non-obsolete `antifungal agent`, and `conf/sources.yaml` maps that role to
`ANTIFUNGAL` without a mechanism mapping.

An ignored-inclusive search for `CHEBI:66698`, the exact label, the filename
stem, and the exact Standard InChIKey across `data/antibiotics`, `data/raw`,
`curation`, `reports`, and the full `/tmp` worklist found only the expected
PATHS row, generated YAML, raw ChEBI row, worklist/review-readiness rows, and
publication-search output. It found no prior dedicated review report, curation
decision, curator-inventory row, generated activity observation, molecular
target, resistance, producer, or causal-graph claim resolving `CHEBI:66698`.

## Evidence

The record's only antimicrobial assertion is inherited from ChEBI role
`CHEBI:35718`, `antifungal agent`. That role is sufficient to file the record
under `ANTIFUNGAL`; it is not a compound-specific mechanism or target claim.

The committed raw ChEBI row for `CHEBI:66698` has one source-literature lead:
`PMID:17870137`. PubMed resolves that PMID to Guimarães, de Souza Filho, dos
Mares-Guia, and Braga's Phytochemistry paper
`Dihydroisocoumarin from Xyris pterygoblephara active against dermatophyte
fungi`; Crossref resolves DOI `10.1016/j.phytochem.2007.08.002` to the same
title and authors.

The PubMed abstract supports this record's isolation-source and broad
antifungal leads. It reports fractionating ethanol extract from
`Xyris pterygoblephara` aerial parts; assigning compound 1 by spectrometric data
as the same 3R,4R dihydroisocoumarin, under a synonym with apparent
typographical variants; defining compound 1's absolute configuration by
circular dichroism; and testing compound 1 at `100 microg/disc` by agar
diffusion against clinical isolates of `Epidermophyton floccosum`,
`Trichophyton mentagrophytes`, and `Trichophyton rubrum`.

The abstract is not enough to make this record `REVIEWED`. It does not state a
biochemical target or mode of action, and the future activity assertions need a
full-paper table check before recording exact isolate identifiers, assay
parameters, zone-of-inhibition values, and whether the record should encode
only qualitative inhibition rather than MIC fields.

NCBI Taxonomy resolves `Xyris pterygoblephara` to current species
`NCBITaxon:3834353`, matching the isolation-source organism named in the
ChEBI-linked source paper.

A bounded repository publication search found zero PubMed candidates for the
exact Standard InChIKey `XFZDFYYRUDDKBS-HZPDHXFCSA-N` and zero candidates for
the exact ChEBI label. A search for the exact ChEBI-linked source-paper title
found one candidate, `PMID:17870137`. Semantic Scholar returned HTTP 429 for
the exact InChIKey and title searches.

## Completeness

The record is incomplete as a reviewed antifungal natural-product record. It
has exact ChEBI identity, structure, same-structure Reaxys xref, chemically
broader ChEBI parents, an antifungal role, a source-paper lead, and a primary
paper abstract linking the exact compound to dermatophyte activity, but no
curator-owned activity observation, producer assertion, molecular target,
mode of action, dataset, or causal graph.

The empty mechanism fields are correct for a ChEBI `antifungal agent` seed. No
inspected source names an ergosterol, cell-wall, membrane, energy-metabolism,
or other fungal mechanism for compound 1.

The empty `producer_organisms` and `activity_spectrum` slots need follow-up but
should not be auto-filled from the definition alone. `just worklist` correctly
reports a `producer-candidate` row for the phrase `isolated from
Xyris pterygoblephara` and an `activity-candidate` row for the phrase `active
against dermatophyte`; the inspected abstract narrows those to a plant aerial
part isolation source and three tested dermatophyte clinical isolates.

The empty `molecular_targets`, `resistance_mechanisms`,
`clinical_status_assertions`, `datasets`, `discussions`, and `causal_graphs`
slots are preferable to over-scoped filler. No molecular target, resistance
mechanism, clinical status, public dataset accession, or evidence-backed causal
edge was identified in the bounded checks.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:66698` has primary antifungal activity support but no curator-owned activity observations, mechanism, target, or producer claims. | The only source-literature lead is `PMID:17870137`; the PubMed abstract maps exact compound 1 to agar-diffusion activity against three dermatophyte clinical isolates and to isolation from `Xyris pterygoblephara`, but the generated record has zero record evidence items, zero `activity_spectrum` rows, zero `producer_organisms`, zero targets, and no `mode_of_action`. | Future curator-owned fields on `data/antibiotics/antifungal/3r-4r-6-methoxy-1-oxo-3-n-pentyl-3-4-dihydro-1h-isochromen-4-yl-acetat.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI later changes this term's role, xrefs, parents, or citations, the ChEBI inventory extractor owns that refresh. |

No blocker identity, structure, schema, xref, class, parentage, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Inspect the full DOI `10.1016/j.phytochem.2007.08.002` and curate
   `activity_spectrum` rows for `Epidermophyton floccosum`,
   `Trichophyton mentagrophytes`, and `Trichophyton rubrum` only if the full
   paper provides exact isolate, assay, outcome, value, qualifier, and unit
   scope. The PubMed abstract reports agar-diffusion inhibition-zone values,
   not MIC values.
2. Add `Xyris pterygoblephara` / `NCBITaxon:3834353` as a
   `producer_organisms` assertion only if the full paper supports the
   plant-to-compound production claim directly enough for this corpus. Preserve
   the `aerial parts` scope in the evidence notes if the claim is curated.
3. Add `mode_of_action`, `mode_of_action_target_scope`, and a fungal
   `MolecularTarget` only if an inspected primary source maps the exact
   dihydroisocoumarin to a biochemical effect or target. Do not infer a
   mechanism from antifungal activity alone.
4. Keep `PMID:17870137` out of same-structure `xrefs`; it should be cited from
   assertion-level `evidence` blocks if its full text supports future activity
   or producer rows.
5. Add a `Discussion` only for a concrete unresolved full-paper conflict or
   curation task. The missing mechanism is represented by the worklist and does
   not need a record-local discussion without a checked citation trail.

## Follow-up Checks

After any exact-term curation or source refresh, rerun:

1. `just validate data/antibiotics/antifungal/3r-4r-6-methoxy-1-oxo-3-n-pentyl-3-4-dihydro-1h-isochromen-4-yl-acetat.yaml`
2. `just validate-strict data/antibiotics/antifungal/3r-4r-6-methoxy-1-oxo-3-n-pentyl-3-4-dihydro-1h-isochromen-4-yl-acetat.yaml --out /tmp/antibioticmech-chebi-66698-validation.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-66698.tsv`
5. `just review-queue --limit 53`
6. `just qc`

Manually compare future activity and producer assertions against the full
Guimarães, de Souza Filho, dos Mares-Guia, and Braga paper to confirm that
claim-level evidence is attached to exact `CHEBI:66698`, not merely to the
plant extract or a dermatophyte group phrase.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, so they
included ignored `reports/` files.

`runoak` was not available in this shell, so official ChEBI term checks were
performed against the EBI OLS4 HTTPS API.

The OLS exact InChIKey search transiently failed DNS resolution, but the direct
term, hierarchical-parent, antifungal-role, and has-role relation endpoints
resolved.

Semantic Scholar returned HTTP 429 for the exact InChIKey and exact title
searches; the PubMed exact-title search resolved `PMID:17870137`.
