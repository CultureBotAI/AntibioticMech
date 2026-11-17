# YAML Record Review: (9S)-erythromycyclamine

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/unspecified/9s-erythromycyclamine.yaml`
- Started UTC: 2026-09-22T14:58:00Z
- Finished UTC: 2026-09-22T15:06:30Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:73708` |
| Label | `(9S)-erythromycyclamine` |
| Path | `data/antibiotics/unspecified/9s-erythromycyclamine.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:73708`, version `2026-08-30`, minted key `antibioticmech:chebi-5f2f3d3250` |
| Source role | `CHEBI:33281` antimicrobial agent |
| Parent compounds | `CHEBI:25105` macrolide antibiotic |
| Structure | `XCLJRCAJSCMIND-JCTYMORFSA-N`; formula `C37H70N2O12`; charge `0` |
| Xrefs | `cas:26116-56-3`; `reaxys:4241492` |
| Source literature leads | None in `curation/record_review_queue.tsv` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded record for exact
`(9S)-erythromycyclamine`, the neutral 9S amino derivative of erythromycin A.
The YAML has exact ChEBI grounding, the ChEBI definition, four ChEBI synonyms,
one strictly broader ChEBI parent, two ChEBI xrefs, the generic ChEBI
`antimicrobial agent` role, structure, and source-concept metadata. It has no
generated or curator-owned mode of action, molecular target, activity
observation, resistance mechanism, producer, dataset, discussion, causal graph,
or claim-level evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/9s-erythromycyclamine.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/9s-erythromycyclamine.yaml --out /tmp/antibioticmech-chebi-73708-strict.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-73708-worklist.tsv` | Pass: the full worklist TSV was written. `CHEBI:73708` appears on `mechanism` and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 70` | Pass: `CHEBI:73708` is queued with `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:73708` resolves in official OLS as a current, non-obsolete 3-star ChEBI
term with label `(9S)-erythromycyclamine`, the same definition, the exact
Standard InChIKey `XCLJRCAJSCMIND-JCTYMORFSA-N`, the exact formula
`C37H70N2O12`, matching average and monoisotopic masses, the exact SMILES, and
the exact `cas:26116-56-3` and `reaxys:4241492` xrefs stored by this generated
record.

The live OLS term exposes the same four related synonyms stored in the YAML:
`(9S)-9-amino-9-deoxoerythromycin`, `9-amino-9-deoxoerythromycin`,
`9-epierythromycylamine`, and `BRN 4241492`.

The live OLS graph gives `CHEBI:73708` one direct `subClassOf` edge,
`CHEBI:25105` `macrolide antibiotic`. That is exactly the generated
`parent_compounds` value. The committed ChEBI role inventory confirms that
`CHEBI:33281` is `antimicrobial agent`, and `conf/sources.yaml` keeps that
generic role in scope without mapping it to a narrower bacterial, fungal,
protozoal, mycobacterial, viral, or biocidal filing class; the generated
`ANTIMICROBIAL_UNSPECIFIED` class is therefore correct.

The committed ChEBI inventory row for `CHEBI:73708` has the same label,
definition, 3-star status, role, parent, SMILES, Standard InChI, Standard
InChIKey, formula, neutral charge, masses, four synonyms, and two xrefs that
appear in the generated record. `PATHS.tsv` maps `CHEBI:73708` to
`ANTIMICROBIAL_UNSPECIFIED/9s-erythromycyclamine`, matching the generated path
and filing class.

Before this report was created, ignored-inclusive exact searches for
`CHEBI:73708`, the exact file stem, the exact label, the exact Standard
InChIKey, the exact CAS number, the exact Reaxys accession, and exact
erythromycyclamine synonym strings across `reports/yaml_record_review`,
`data/antibiotics`, `data/raw`, `curation`, `conf`, `docs`, `src`, `tests`, and
`.claude` found only the expected generated YAML, `PATHS.tsv` row, raw ChEBI
row, and `record_review_queue.tsv` row for exact `CHEBI:73708`. The only
additional exact stem hit was the generated ChEBI-seeded `dirithromycin` row,
whose ChEBI definition correctly describes it as a prodrug for
`(9S)-erythromycyclamine`.

## Evidence

The record's antimicrobial classification is inherited from committed ChEBI
role `CHEBI:33281`, `antimicrobial agent`. `data/raw/chebi_role_names.tsv`
marks that role as a generic ChEBI scope role, and `conf/sources.yaml` maps it
to the generated `ANTIMICROBIAL_UNSPECIFIED` filing class. That role is enough
for reproducible generic filing but not enough to fill a specific activity
observation, mode of action, target, or causal graph.

The generated record has no source PubMed leads and no evidence-bearing
objects. PubMed and the local publication helper returned no hits for exact
phrases matching ChEBI's preferred spelling, ChEBI synonym spelling,
`BRN 4241492`, or the Standard InChIKey. Semantic Scholar returned HTTP 429 for
the exact-name and common-spelling helper searches and was not used for claim
support.

Direct PubMed eSearch for exact CAS `26116-56-3` returned 14 indexed candidates,
and exact `erythromycylamine` returned 47 candidates. The CAS-indexed title set
includes obvious future antibacterial or antimycobacterial activity leads such
as `PMID:7603759`, an in vitro evaluation of dirithromycin and
erythromycylamine, and `PMID:7868412`, an activity study against
`Mycobacterium avium` complex. It also includes pharmacokinetic,
chromatographic, dirithromycin-metabolite, derivative-chemistry, host-cell, and
immunomodulation papers that are not by themselves enough to curate a microbial
activity observation or ribosomal target for exact `CHEBI:73708`.

No inspected PubMed abstract in the bounded CAS/common-spelling checks named a
compound-specific 50S ribosomal target, `peptidyltransferase` target relation,
or exact MIC value ready for claim-level import without full-text inspection.
The macrolide parent is a mechanism cue only; mechanism, target, MIC, producer,
and causal-graph assertions still need primary exact-compound evidence before
they can be curated.

## Completeness

The record is incomplete as a reviewed antimicrobial `(9S)-erythromycyclamine`
record. It has exact ChEBI identity, structure, parentage, xrefs, generic
antimicrobial classification, and reproducible source metadata, but no curated
mode of action, molecular target, activity observation, dataset, or causal
graph.

The empty activity and mechanism slots are correct for the current seed.
`CHEBI:33281` states only that the molecule is an antimicrobial agent, and the
seed has no source PMID to inspect for a per-organism activity value or
mechanism. Exact external PubMed searches expose plausible erythromycylamine
activity papers that a curator should triage, but none have yet been reduced to
claim-level evidence in this record.

The empty `producer_organisms`, `resistance_mechanisms`,
`clinical_status_assertions`, `datasets`, and `discussions` slots are
acceptable. No measured resistance edge, producer assertion, standalone
clinical status assertion for this exact metabolite, public dataset accession,
or discussion-worthy conflict with exact `CHEBI:73708` claim-level evidence
was identified in the bounded checks.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:73708` has only generic source-level antimicrobial classification and no curator-owned exact-compound activity, mechanism, target, or causal-graph claim. | The generated record has no source PubMed leads, zero record evidence items, zero `activity_spectrum` rows, zero targets, and no `mode_of_action`. Exact-CAS PubMed search returned 14 candidates, including in vitro erythromycylamine activity leads, so the record is missing triageable evidence rather than merely lacking a search term. | Future curator-owned fields on `data/antibiotics/unspecified/9s-erythromycyclamine.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blocker identity, structure, schema, xref, parentage, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Triage exact-CAS PubMed leads for primary antibacterial and
   antimycobacterial activity papers, starting with `PMID:7603759` and
   `PMID:7868412`. If the full text reports exact-organism MIC values or other
   interpretable activity values for exact erythromycylamine, add
   claim-level `ActivityObservation` entries with units, assay, organism and
   strain scope, and evidence.
2. Curate a `mode_of_action`, molecular target, and causal graph only from
   primary evidence that explicitly applies to exact `(9S)-erythromycyclamine`.
   The broader `macrolide antibiotic` parent should not by itself create a 50S
   ribosomal target assertion.
3. If exact full-text review shows that the CAS-indexed studies test only
   dirithromycin, prodrug exposure, host-cell accumulation, synthetic
   derivatives, or the adjacent `(9R)-erythromycylamine` stereoisomer, leave
   those data out of exact `CHEBI:73708` activity and add a `Discussion` only
   for a concrete unresolved stereochemistry or evidence-scope conflict.
4. Leave the source-owned ChEBI identity, structure, role, parent, synonyms, and
   xrefs untouched unless the committed ChEBI inventory diverges from OLS or a
   curator decision needs to exclude a proven wrong source assertion.

## Follow-up Checks

After any exact-term curation, exclusion, or source refresh, rerun:

1. `just validate data/antibiotics/unspecified/9s-erythromycyclamine.yaml`
2. `just validate-strict data/antibiotics/unspecified/9s-erythromycyclamine.yaml --out /tmp/antibioticmech-chebi-73708-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-73708-worklist.tsv`
5. `just review-queue --limit 70`
6. `just qc`

Manually compare any future activity, mechanism, target, dataset, or
causal-graph assertion against exact `(9S)-erythromycyclamine` identity. Confirm
that every claim-level evidence block attaches to the specific object it
supports, not only to the whole ChEBI term, the generic antimicrobial-agent
role, the macrolide class, the dirithromycin prodrug, or a nearby derivative.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, so they
included ignored `reports/` files.
