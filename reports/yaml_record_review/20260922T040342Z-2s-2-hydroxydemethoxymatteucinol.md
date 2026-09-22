# YAML Record Review: (2S)-2'-hydroxydemethoxymatteucinol

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antimycobacterial/2s-2-hydroxydemethoxymatteucinol.yaml`
- Started UTC: 2026-09-22T03:43:00Z
- Finished UTC: 2026-09-22T04:03:42Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:67371` |
| Label | `(2S)-2'-hydroxydemethoxymatteucinol` |
| Path | `data/antibiotics/antimycobacterial/2s-2-hydroxydemethoxymatteucinol.yaml` |
| Class | `ANTIMYCOBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:67371`, version `2026-08-30`, minted key `antibioticmech:chebi-99dafc003b` |
| Source role | `CHEBI:33231` antitubercular agent |
| Structure | `WOGYXYDORXIAGE-ZDUSSCGKSA-N`; formula `C17H16O5`; charge `0` |
| Same-structure xrefs | `cas:77744-53-7`, `reaxys:4519598` |
| Source literature lead | `PMID:21542597` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded flavanone record. The YAML has
source-derived identity, definition, three exact synonyms, one ChEBI parent, one
antitubercular role, same-structure CAS and Reaxys xrefs, structure, and
source-concept metadata, but no curator-owned mode of action, target, resistance
mechanism, activity observation, producer, discussion, dataset, or causal graph.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antimycobacterial/2s-2-hydroxydemethoxymatteucinol.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antimycobacterial/2s-2-hydroxydemethoxymatteucinol.yaml --out /tmp/antibioticmech-chebi-67371-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-67371.tsv` | Pass: the full worklist TSV was written. `CHEBI:67371` appears on `mechanism`, `producer-candidate`, and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 46` | Pass: `CHEBI:67371` is the next queued record without an existing `reports/yaml_record_review` report; its row says `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:67371` resolves in official OLS as a current, non-obsolete ChEBI term
labeled `(2S)-2'-hydroxydemethoxymatteucinol`. The live OLS annotations list
the same formula, charge, average mass, monoisotopic mass, Standard InChI,
Standard InChIKey, SMILES, CAS cross-reference, Reaxys cross-reference, and
PubMed cross-reference as the committed `data/raw/chebi_antimicrobials.tsv`
row.

The generated record's only `parent_compounds` entry is exactly the official
OLS hierarchical parent of `CHEBI:67371`: `CHEBI:38739`
trihydroxyflavanone. The official OLS graph also links the reviewed term to
`CHEBI:76323` matteucinol by `has functional parent` and to `CHEBI:76924` plant
metabolite by `has role`; those broader chemical and biological role edges do
not belong in this record's `parent_compounds` or antimicrobial
`activity_roles` slots.

The `ANTIMYCOBACTERIAL` filing class is consistent with the source role. The
live `CHEBI:33231` role term resolves in OLS as current and non-obsolete
`antitubercular agent`, and `conf/sources.yaml` maps that ChEBI role to
`ANTIMYCOBACTERIAL`.

The generated same-structure xrefs are correctly scoped. ChEBI attaches
`cas:77744-53-7`, `reaxys:4519598`, and `pubmed:21542597` to this exact term;
the YAML imports the CAS and Reaxys registry xrefs, while the raw ChEBI
inventory exposes the PubMed article as source-literature provenance rather than
as a same-structure database xref.

An ignored-inclusive search for `CHEBI:67371`,
`WOGYXYDORXIAGE-ZDUSSCGKSA-N`, `antibioticmech:chebi-99dafc003b`, and
`hydroxydemethoxymatteucinol` across `data/antibiotics`, `data/raw`,
`curation`, `reports`, `.claude`, `docs`, and `README.md` found the expected
PATHS row, generated YAML, raw ChEBI row, and review-readiness row. It found no
prior dedicated review report, curation decision, curator-inventory row,
generated mechanism, activity observation, target, resistance, or producer claim
resolving `CHEBI:67371`.

## Evidence

The target record has no evidence-bearing assertions. That is schema-valid for
a ChEBI-seeded record because the source concept supplies database provenance
and no mechanism, target, activity, resistance, producer, dataset, or causal
claim has been promoted into curator-owned slots.

The committed raw ChEBI row for `CHEBI:67371` has one source-literature lead:
`PMID:21542597`. PubMed resolves that PMID to Wu, Peng, Chen, and Tsai's 2011
Journal of Natural Products paper, DOI `10.1021/np1008575`, and Crossref
resolves the same DOI to the same title and journal.

PubMed's abstract reports isolation of new and known chromones, flavonoids, and
an isoflavonoid from a methanol extract of combined `Pisonia aculeata` stem and
root and states that compounds 2, 7, 14, 16, and 19 had in vitro activity with
MICs of at most 50.0 micrograms/mL against `Mycobacterium tuberculosis` H37Rv.
The abstract is enough to corroborate that the ChEBI source paper concerns
antitubercular compounds from the plant source, but it does not map exact
`CHEBI:67371` to one of those active compound numbers or expose the per-compound
MIC value.

The plant name from the definition resolves in NCBI Taxonomy as species
`NCBITaxon:363212` `Pisonia aculeata`. The H37Rv strain from the source-paper
abstract resolves in NCBI Taxonomy as `NCBITaxon:83332`
`Mycobacterium tuberculosis H37Rv`.

A bounded repository publication search for the exact Standard InChIKey
`WOGYXYDORXIAGE-ZDUSSCGKSA-N` found zero PubMed candidates. A second search for
the exact ChEBI-linked paper title found one PubMed candidate: `PMID:21542597`.
Semantic Scholar returned HTTP 429 for both searches.

## Completeness

The record is incomplete as a reviewed antimycobacterial natural-product record.
It has exact ChEBI identity, structure, a chemically broader flavanone parent, an
antitubercular role, two same-structure registry xrefs, and a primary-paper lead,
but no curator-owned mode of action, molecular target, resistance mechanism,
activity observation, producer, dataset, or causal graph.

The empty `mode_of_action`, `mode_of_action_target_scope`,
`molecular_targets`, `resistance_mechanisms`, `activity_spectrum`,
`producer_organisms`, `clinical_status_assertions`, `datasets`, `discussions`,
and `causal_graphs` slots are preferable to over-scoped filler. The inspected
abstract supports an antimycobacterial screening context and a plant isolation
source, but it does not support a specific molecular target, resistance
mechanism, or biosynthetic producer assertion.

`just worklist` correctly reports a `mechanism` row for `CHEBI:67371` because
there is no curator-owned or source-seeded mode of action and no CARD target or
resistance edge to build on. It also correctly reports a `producer-candidate`
row: the definition phrase `isolated from Pisonia aculeata` is a source-organism
lead that needs review before anyone can decide whether a `ProducerOrganism`
assertion is warranted.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The ChEBI-linked source paper has not been resolved into claim-level mechanism, target, resistance, activity, or producer evidence. | The YAML has no evidence-bearing objects; `PMID:21542597` is the only source-literature lead in the ChEBI raw row; the PubMed abstract confirms in vitro `M. tuberculosis` H37Rv screening of several `Pisonia aculeata` isolates but does not expose a mechanism, target, resistance claim, exact `CHEBI:67371` compound number, or `CHEBI:67371` MIC; `just worklist` queues `CHEBI:67371` on `mechanism`, `producer-candidate`, and `review-readiness`. | Future curator-owned fields on `data/antibiotics/antimycobacterial/2s-2-hydroxydemethoxymatteucinol.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI later changes this term's source xrefs, the ChEBI inventory extractor owns that refresh. |

No blocker identity, structure, schema, xref, class, or parentage findings were
found.

No minor findings.

## Recommended Edits

1. Leave `mode_of_action`, `molecular_targets`, `resistance_mechanisms`, and
   `causal_graphs` empty until a full source establishes what the compound does
   mechanistically against `Mycobacterium tuberculosis` H37Rv.
2. Inspect the full DOI `10.1021/np1008575` before adding an
   `activity_spectrum` row. Add a MIC observation only if the table maps exact
   `(2S)-2'-hydroxydemethoxymatteucinol` to one of the active compound numbers
   and reports units and assay context; record the target strain as
   `NCBITaxon:83332` if the paper's only tested organism was
   `Mycobacterium tuberculosis H37Rv`.
3. Treat `Pisonia aculeata` as an isolation-source lead, not automatically as a
   biosynthetic producer. A `producer_organisms` assertion should be added only
   if an inspected primary source explicitly supports a compound-to-organism
   production claim, ideally for `NCBITaxon:363212`.
4. Keep the ChEBI PubMed cross-reference out of the YAML's same-structure
   `xrefs`; cite PMID `21542597` from an assertion-level `evidence` block if
   its table or text is later curated into activity or provenance fields.

## Follow-up Checks

After any exact-term curation or source refresh, rerun:

1. `just validate data/antibiotics/antimycobacterial/2s-2-hydroxydemethoxymatteucinol.yaml`
2. `just validate-strict data/antibiotics/antimycobacterial/2s-2-hydroxydemethoxymatteucinol.yaml --out /tmp/antibioticmech-chebi-67371-validation.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-67371.tsv`
5. `just review-queue --limit 46`
6. `just qc`

Manually compare future activity curation against the full Wu, Peng, Chen, and
Tsai table to confirm that an activity observation has been attached to the
exact `CHEBI:67371` structure and not to a sibling Pisonia isolate from the same
paper.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, so they
included ignored `reports/` files.

`runoak` was not available in this shell, so official ChEBI term checks were
performed against the EBI OLS4 HTTPS API.

Direct HTTPS access to the ACS DOI page returned a Cloudflare challenge, so the
report uses PubMed and Crossref metadata for the ChEBI-linked source article.

Semantic Scholar returned HTTP 429 for both repository publication searches;
the PubMed side of both searches completed.
