# YAML Record Review: (2-cis,6-trans)-farnesol

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/unspecified/2-cis-6-trans-farnesol.yaml`
- Started UTC: 2026-09-21T23:55:30Z
- Finished UTC: 2026-09-21T23:59:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:16774` |
| Label | `(2-cis,6-trans)-farnesol` |
| Path | `data/antibiotics/unspecified/2-cis-6-trans-farnesol.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:16774`, version `2026-08-30`, minted key `antibioticmech:chebi-914d295e86` |
| Source role | `CHEBI:33281` antimicrobial agent, inherited from parent `CHEBI:28600` farnesol |
| Structure | `CRDAMVZIKSXKFV-PVMFERMNSA-N`; formula `C15H26O`; charge `0` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded farnesol stereoisomer. The YAML
has source-derived identity, parent, role, structure, and cross-reference
metadata, but no curator-owned mode of action, target, activity observation,
producer, resistance, discussion, or causal graph.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/2-cis-6-trans-farnesol.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/2-cis-6-trans-farnesol.yaml --out /tmp/antibioticmech-cis-trans-farnesol-16774-validation.tsv` | Pass: 1 file scanned, 0 errors. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-cis-trans-farnesol-16774.tsv` | Pass: the full worklist TSV was written. `CHEBI:16774` appears on `mechanism` and `review-readiness`; it has 0 CARD targets and 0 resistance edges to build on. |
| `just review-queue --limit 39` | Pass: `CHEBI:16774` is the next queued unreported record after `CHEBI:42680`; its row says `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this ChEBI-seeded record; the schema/strict checks and `verify-corpus` are the
narrowest documented local gates.

## Identity and Grounding

`CHEBI:16774` resolves in official OLS as a current, non-obsolete, 3-star ChEBI
term labeled `(2-cis,6-trans)-farnesol`. Its formula, charge, monoisotopic mass,
Standard InChI, Standard InChIKey, CAS xref, Beilstein xref, KEGG COMPOUND xref,
and stereospecific synonyms match the committed `data/raw/chebi_antimicrobials.tsv`
row and the generated YAML.

The record is correctly distinct from `CHEBI:28600` farnesol. OLS exposes
`CHEBI:16774 subClassOf CHEBI:28600`; the parent has a Standard InChIKey without
fixed double-bond stereochemistry, while this child fixes the `(2Z,6E)` geometry
and matches `CRDAMVZIKSXKFV-PVMFERMNSA-N`.

The `kegg.compound:C03220` xref denotes the same structure. The KEGG REST record
for `C03220` resolves to `(2Z,6E)-Farnesol`, names ChEBI `16774`, lists CAS
`3790-71-4`, and reports formula `C15H26O`, exact mass `222.1984`, and molecular
weight `222.37`.

The `CHEBI:33281` antimicrobial-agent role is inherited from the broader
`CHEBI:28600` farnesol node. Official OLS lists `antimicrobial agent`, `plant
metabolite`, and `fungal metabolite` as `has role` fillers on `CHEBI:28600`; it
lists no direct `has role` fillers on `CHEBI:16774`. This inheritance is
intentional: `scripts/extract_source_inventory.py` propagates in-scope ChEBI
roles from a bearer to all descendants, and `conf/sources.yaml` maps the generic
`CHEBI:33281` role to `ANTIMICROBIAL_UNSPECIFIED`.

Before this report was written, an ignored-inclusive search for `CHEBI:16774`,
`CRDAMVZIKSXKFV-PVMFERMNSA-N`, `antibioticmech:chebi-914d295e86`, and exact
cis,trans-farnesol names across `data/antibiotics`, `data/raw`, `curation`, and
`reports` found only the expected `PATHS.tsv` row, `record_review_queue.tsv` row,
raw ChEBI row, and generated YAML. No prior review report, curated overlay, or
second generated record claims this exact Standard InChIKey.

## Evidence

The target record has no evidence-bearing assertions. That is schema-valid for a
ChEBI-seeded record because the source concept supplies database provenance and
no mechanism, target, activity, resistance, producer, or causal claim has been
promoted into curator-owned slots.

A bounded exact-stereoisomer PubMed/Semantic Scholar search for
`"(2-cis,6-trans)-farnesol" OR "(2Z,6E)-farnesol" OR "(Z,E)-farnesol" OR
"cis,trans-farnesol" OR "CRDAMVZIKSXKFV-PVMFERMNSA-N"` found 20 PubMed
candidates and hit Semantic Scholar HTTP 429. Most PubMed candidates were
phytochemical occurrence, odorant, insecticidal, essential-oil mixture, or
organic-chemistry papers rather than isolated `(2Z,6E)-farnesol` antimicrobial
assays.

A second bounded query that added antimicrobial terms found 13 PubMed candidates
and hit the same Semantic Scholar HTTP 429. The closest lead is PMID:26411038,
which reports `(2Z,6E)-farnesol` as 35.0% of *Diospyros discolor* flower
essential oil and names it among active compounds for the oil's antimicrobial
activity. That abstract is not enough by itself to add an `ActivityObservation`,
because the isolate-specific organism, endpoint values, value qualifiers, and
units need to be recovered from the full paper.

The other antimicrobial-query candidates do not support curation from the
abstracts inspected here. PMID:26434142 reports `(2Z,6E)-farnesol` as 6.9% of
*Cupressus cashmeriana* twig oil, but names carvacrol as the major ingredient
responsible for the oil's activities. PMID:25920237 and PMID:20385420 concern
`trans,trans-farnesol`, a different stereoisomer. Several later exact-query hits
tested unspecified `farnesol` as an insecticide against *Anopheles* mosquitoes,
not as an antimicrobial agent against a microbial taxon.

## Completeness

The record is incomplete as a reviewed antimicrobial record. Its generic
antimicrobial role is inherited from stereochemically broader `CHEBI:28600`; no
claim-level activity, MIC, equivalent quantitative endpoint, target group, or
mode of action for isolated `CHEBI:16774` has been curated.

The empty `mode_of_action`, `molecular_targets`, `activity_spectrum`,
`resistance_mechanisms`, `producer_organisms`, and `causal_graphs` slots are
therefore preferable to over-scoped filler. A later curation pass should inspect
PMID:26411038 first, then add to these slots only after it finds full-text
support for the exact compound or an explicitly defensible reason to curate from
a stereoisomerically defined mixture.

No producer-candidate row is queued for this record, and the bounded exact-name
publication searches did not find a biosynthetic producer claim for this
stereoisomer.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The exact-compound antimicrobial lead from PMID:26411038 has not been resolved into evidence-backed activity observations or an explicit unresolved curation discussion. | The generated YAML has no evidence-bearing activity items; PMID:26411038 reports `(2Z,6E)-farnesol` as a major constituent of antimicrobial *Diospyros discolor* flower essential oil and names it among active antimicrobial constituents; `just worklist` still queues only `mechanism` and `review-readiness` for `CHEBI:16774`. | Future curator-owned fields on `data/antibiotics/unspecified/2-cis-6-trans-farnesol.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blocker identity, structure, schema, or xref findings were found.

No minor findings.

## Recommended Edits

1. Inspect PMID:26411038 full text and curate isolated `(2Z,6E)-farnesol`
   activity only if the paper supplies the tested microbial taxa or strains,
   assay methods, endpoint values, value qualifiers, and units for this exact
   compound. If the paper tested only the mixture, add a bounded `CURATION_TODO`
   discussion instead of generalizing the oil MIC values to `(2Z,6E)-farnesol`.
2. Keep `mode_of_action`, `molecular_targets`, `resistance_mechanisms`,
   `producer_organisms`, and `causal_graphs` empty until a curator finds primary
   evidence for isolated `(2Z,6E)-farnesol` or a source that explicitly assays a
   known stereoisomeric composition containing it.
3. If exact mechanism evidence is found, curate `mode_of_action` with `CURATOR:`
   provenance, set `mode_of_action_target_scope`, and add target or causal-graph
   assertions only at the same scope as their primary evidence.

## Follow-up Checks

After any future curation, run:

| Check | Purpose |
|---|---|
| `just validate data/antibiotics/unspecified/2-cis-6-trans-farnesol.yaml` | Confirm the edited YAML still validates as an `AntibioticRecord`. |
| `just validate-strict data/antibiotics/unspecified/2-cis-6-trans-farnesol.yaml --out /tmp/antibioticmech-cis-trans-farnesol-16774-validation.tsv` | Confirm closed-schema validation has zero errors. |
| `just verify-corpus --summary` | Confirm any curator-owned additions survive seeding and no generated ChEBI fields drift. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-cis-trans-farnesol-16774.tsv` | Confirm the mechanism/review-readiness rows change only when a curator has actually resolved them. |
| `just review-queue --limit 39` | Confirm the queue position if the record is still `SEEDED`, or confirm it leaves the queue only after `REVIEWED` or `DEPRECATED` is justified. |

## Additional Notes

`uvx --from oaklib runoak -i ols:chebi info CHEBI:16774 CHEBI:28600 CHEBI:33281`
resolved the three relevant ChEBI CURIEs through OLS. Direct `curl` calls to EBI
OLS verified the term payload and graph/role endpoints used for the detailed
edge checks; one initial sandboxed OLS lookup failed on DNS and succeeded when
retried.

Both repository publication searches used `env -u NCBI_EMAIL` so no contact email
was sent in NCBI API metadata. Semantic Scholar returned HTTP 429 on both
queries, so the literature review should be read as PubMed-bounded plus the KEGG
and OLS official registry checks above.
