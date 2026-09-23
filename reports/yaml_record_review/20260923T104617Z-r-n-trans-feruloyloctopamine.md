# YAML Record Review: (R)-N-trans-feruloyloctopamine

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antimycobacterial/r-n-trans-feruloyloctopamine.yaml`
- Started UTC: 2026-09-23T10:33:00Z
- Finished UTC: 2026-09-23T10:46:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:67373` |
| Label | `(R)-N-trans-feruloyloctopamine` |
| Path | `data/antibiotics/antimycobacterial/r-n-trans-feruloyloctopamine.yaml` |
| Class | `ANTIMYCOBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:67373`, version `2026-08-30`, minted key `antibioticmech:chebi-323b67c54c` |
| Source role | `CHEBI:33231` antitubercular agent |
| Structure | `VJSCHQMOTSXAKB-CFZDNBDDSA-N`; formula `C18H19NO5`; charge `0` |
| Same-structure xrefs | `reaxys:9579371` |
| Source literature lead | `PMID:21542597` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded cinnamamide record. The YAML has
source-derived identity, definition, four synonyms, four ChEBI parents, one
antitubercular role, one same-structure Reaxys xref, structure, and
source-concept metadata, but no curator-owned mode of action, target, resistance
mechanism, activity observation, producer, discussion, dataset, or causal graph.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antimycobacterial/r-n-trans-feruloyloctopamine.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antimycobacterial/r-n-trans-feruloyloctopamine.yaml --out /tmp/r-n-trans-feruloyloctopamine-validate-strict.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/r-n-trans-feruloyloctopamine-worklist.tsv` | Pass: the full worklist TSV was written. `CHEBI:67373` appears on `mechanism`, `producer-candidate`, and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 110` | Pass: `CHEBI:67373` is the next queued record after the already-reviewed `(R)-mandelic acid`; its row says `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just lint` | Pass: `ruff check .` reported `All checks passed!`. |
| `git diff --check` | Pass: no whitespace errors before writing this report. |
| `git diff --cached --check` | Pass: no whitespace errors in the staged single-report diff. |

No narrower single-record term, reference, or history validator is exposed for
this ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:67373` resolves in official OLS4 as a current, non-obsolete ChEBI term
labeled `(R)-N-trans-feruloyloctopamine`. The live OLS4 annotations list the
same definition, formula, charge, average mass, monoisotopic mass, Standard
InChI, Standard InChIKey, SMILES, Reaxys cross-reference, and PubMed
cross-reference as the committed `data/raw/chebi_antimicrobials.tsv` row.

The generated `parent_compounds` match the four official OLS4 hierarchical
parents for `CHEBI:67373`: `CHEBI:140325` secondary carboxamide, `CHEBI:23247`
cinnamamides, `CHEBI:25235` monomethoxybenzene, and `CHEBI:33853` phenols.
These are chemically broader than the reviewed structure and belong in
`parent_compounds`.

The source `CHEBI:33231` role term resolves in OLS4 as a current,
non-obsolete `antitubercular agent`; `data/raw/chebi_role_names.tsv` also names
`CHEBI:33231` as `antitubercular agent`, and `conf/sources.yaml` maps that role
to `ANTIMYCOBACTERIAL`. The generated filing class is therefore consistent with
the source activity role.

The sole generated same-structure xref is correctly scoped. OLS4 attaches
`reaxys:9579371` and `pubmed:21542597` to this exact ChEBI term; the YAML
imports the Reaxys registry xref while the raw ChEBI inventory exposes
`PMID:21542597` as source-literature provenance rather than as a
same-structure database xref.

An ignored-inclusive search for `CHEBI:67373`,
`VJSCHQMOTSXAKB-CFZDNBDDSA-N`,
`antibioticmech:chebi-323b67c54c`, and `r-n-trans-feruloyloctopamine` across
`data/antibiotics`, `data/raw`, `curation`, and `reports/yaml_record_review`
found the expected `PATHS.tsv` row, raw ChEBI row, review-readiness row, and
generated YAML. It found no prior dedicated review report, no duplicated
generated record, no generated mechanism, and no generated target, activity,
resistance, or producer claim resolving `CHEBI:67373`.

## Evidence

The target record has no evidence-bearing assertions. That is schema-valid for
a ChEBI-seeded record because the source concept supplies database provenance
and no mechanism, target, activity, resistance, producer, dataset, or causal
claim has been promoted into curator-owned slots.

The committed raw ChEBI row for `CHEBI:67373` has one source-literature lead:
`PMID:21542597`. PubMed resolves that PMID to Wu, Peng, Chen, and Tsai's 2011
Journal of Natural Products paper, DOI `10.1021/np1008575`.

PubMed's abstract reports isolation of new and known chromones, flavonoids, an
isoflavonoid, pisoniamide, and pisonolic acid from a methanol extract of
combined `Pisonia aculeata` stem and root. It states that compounds 2, 7, 14,
16, and 19 had in vitro activity with MICs at or below 50.0 micrograms/mL
against `Mycobacterium tuberculosis` H37Rv. The abstract is enough to
corroborate that the ChEBI source paper concerns antitubercular compounds from
the plant source, but it does not map exact `CHEBI:67373` to one of those
active compound numbers or expose the per-compound MIC value.

The plant name from the definition resolves in NCBI Taxonomy as species
`NCBITaxon:363212` `Pisonia aculeata`. The H37Rv strain from the source-paper
abstract resolves in NCBI Taxonomy as `NCBITaxon:83332`
`Mycobacterium tuberculosis H37Rv`.

Targeted repository publication searches found no exact antimicrobial follow-up
to curate. The exact Standard InChIKey
`VJSCHQMOTSXAKB-CFZDNBDDSA-N` and the exact synonym
`(R)-N-[(E)-feruloyl]octopamine` each returned zero PubMed candidates; a search
for `(R)-N-trans-feruloyloctopamine` returned two off-target PubMed candidates
about amyloid/beta-secretase/MAO-B inhibition and acute myocardial ischemia
network pharmacology rather than antitubercular activity. The direct
`21542597` query returned the expected PubMed source-paper candidate. Semantic
Scholar returned HTTP 429 for all four repository publication searches.

## Completeness

The record is incomplete as a reviewed antimycobacterial natural-product record.
It has exact ChEBI identity, structure, four chemically broader parents, an
antitubercular role, a same-structure registry xref, and a primary-paper lead,
but no curator-owned mode of action, molecular target, resistance mechanism,
activity observation, producer, dataset, or causal graph.

The empty `mode_of_action`, `mode_of_action_target_scope`,
`molecular_targets`, `resistance_mechanisms`, `activity_spectrum`,
`producer_organisms`, `clinical_status_assertions`, `datasets`, `discussions`,
and `causal_graphs` slots are preferable to over-scoped filler. The inspected
abstract supports an antimycobacterial screening context and a plant isolation
source, but it does not support a specific molecular target, resistance
mechanism, or biosynthetic producer assertion.

`just worklist` correctly reports a `mechanism` row for `CHEBI:67373` because
there is no curator-owned or source-seeded mode of action and no CARD target or
resistance edge to build on. It also correctly reports a `producer-candidate`
row: the definition phrase `isolated from Pisonia aculeata` is a
source-organism lead that needs review before anyone can decide whether a
`ProducerOrganism` assertion is warranted.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The ChEBI-linked source paper has not been resolved into claim-level mechanism, target, resistance, activity, or producer evidence. | The YAML has no evidence-bearing objects; `PMID:21542597` is the only source-literature lead in the ChEBI raw row; the PubMed abstract confirms in vitro `M. tuberculosis` H37Rv screening of several `Pisonia aculeata` isolates but does not expose a mechanism, target, resistance claim, exact `CHEBI:67373` compound number, or `CHEBI:67373` MIC; `just worklist` queues `CHEBI:67373` on `mechanism`, `producer-candidate`, and `review-readiness`. | Future curator-owned fields on `data/antibiotics/antimycobacterial/r-n-trans-feruloyloctopamine.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI later changes this term's source xrefs, the ChEBI inventory extractor owns that refresh. |

No blocker identity, structure, schema, xref, class, or parentage findings were
found.

No minor findings.

## Recommended Edits

1. Leave `mode_of_action`, `molecular_targets`, `resistance_mechanisms`, and
   `causal_graphs` empty until a full primary source establishes what the
   compound does mechanistically against `Mycobacterium tuberculosis` H37Rv.
2. Inspect the full DOI `10.1021/np1008575` before adding an
   `activity_spectrum` row. Add a MIC observation only if the table maps exact
   `(R)-N-trans-feruloyloctopamine` to one of the active compound numbers and
   reports units and assay context; record the target strain as
   `NCBITaxon:83332` if the paper's only tested organism was
   `Mycobacterium tuberculosis H37Rv`.
3. Treat `Pisonia aculeata` as an isolation-source lead, not automatically as a
   biosynthetic producer. A `producer_organisms` assertion should be added only
   if an inspected primary source explicitly supports a compound-to-organism
   production claim, ideally for `NCBITaxon:363212`.
4. Keep the ChEBI PubMed cross-reference out of the YAML's same-structure
   `xrefs`; cite `PMID:21542597` from an assertion-level `evidence` block if
   its table or text is later curated into activity or provenance fields.

## Follow-up Checks

After any exact-term curation or source refresh, rerun:

1. `just validate data/antibiotics/antimycobacterial/r-n-trans-feruloyloctopamine.yaml`
2. `just validate-strict data/antibiotics/antimycobacterial/r-n-trans-feruloyloctopamine.yaml --out /tmp/r-n-trans-feruloyloctopamine-validate-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/r-n-trans-feruloyloctopamine-worklist.tsv`
5. `just review-queue --limit 110`
6. `just lint`
7. `git diff --check`
8. `git diff --cached --check`

Manually compare future activity curation against the full Wu, Peng, Chen, and
Tsai table to confirm that an activity observation has been attached to the
exact `CHEBI:67373` structure and not to a sibling `Pisonia aculeata` isolate
from the same paper.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, so they
included ignored `reports/` files.

`runoak` was not available in this shell, so official ChEBI term checks were
performed against the EBI OLS4 HTTPS API.

Semantic Scholar returned HTTP 429 for all four repository publication
searches; the PubMed side of all four searches completed.
