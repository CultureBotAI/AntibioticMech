# YAML Record Review: (2-trans,6-cis)-farnesol

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/unspecified/2-trans-6-cis-farnesol.yaml`
- Started UTC: 2026-09-22T00:26:30Z
- Finished UTC: 2026-09-22T00:32:54Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:35966` |
| Label | `(2-trans,6-cis)-farnesol` |
| Path | `data/antibiotics/unspecified/2-trans-6-cis-farnesol.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:35966`, version `2026-08-30`, minted key `antibioticmech:chebi-d62ebeb279` |
| Source role | `CHEBI:33281` antimicrobial agent, inherited from parent `CHEBI:28600` farnesol |
| Structure | `CRDAMVZIKSXKFV-GNESMGCMSA-N`; formula `C15H26O`; charge `0` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded farnesol stereoisomer. The YAML
has source-derived identity, definition, parent, role, structure, and
cross-reference metadata, but no curator-owned mode of action, target, activity
observation, producer, resistance, discussion, or causal graph.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/2-trans-6-cis-farnesol.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/2-trans-6-cis-farnesol.yaml --out /tmp/antibioticmech-trans-cis-farnesol-35966-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-trans-cis-farnesol-35966.tsv` | Pass: the full worklist TSV was written. `CHEBI:35966` appears on `mechanism` and `review-readiness`; it has 0 CARD targets and 0 resistance edges to build on. |
| `just review-queue --limit 40` | Pass: `CHEBI:35966` is the next queued record after `CHEBI:16774`; its row says `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this ChEBI-seeded record; the schema/strict checks and `verify-corpus` are the
narrowest documented local gates.

## Identity and Grounding

`CHEBI:35966` resolves in official OLS as a current, non-obsolete ChEBI term
labeled `(2-trans,6-cis)-farnesol` and defined as the `(2E,6Z)` stereoisomer of
farnesol. Its formula, charge, monoisotopic mass, Standard InChI, Standard
InChIKey, CAS xref, Beilstein xref, definition, and stereospecific synonyms
match the committed `data/raw/chebi_antimicrobials.tsv` row and the generated
YAML.

The record is correctly distinct from `CHEBI:28600` farnesol. OLS lists
`CHEBI:28600` as the only parent of `CHEBI:35966`; the parent has a Standard
InChIKey without fixed double-bond stereochemistry, while this child fixes the
`(2E,6Z)` geometry and matches `CRDAMVZIKSXKFV-GNESMGCMSA-N`.

The `CHEBI:33281` antimicrobial-agent role is inherited from the broader
`CHEBI:28600` farnesol node. Official OLS lists `antimicrobial agent`, `plant
metabolite`, and `fungal metabolite` as `has role` fillers on `CHEBI:28600`; it
lists no direct `has role` fillers on `CHEBI:35966`. This inheritance is
intentional: `scripts/extract_source_inventory.py` propagates in-scope ChEBI
roles from a bearer to all descendants, and `conf/sources.yaml` maps the generic
`CHEBI:33281` role to `ANTIMICROBIAL_UNSPECIFIED`.

An ignored-inclusive search for `CHEBI:35966`,
`CRDAMVZIKSXKFV-GNESMGCMSA-N`, `antibioticmech:chebi-d62ebeb279`, and exact
trans,cis-farnesol names across `data/antibiotics`, `data/raw`, `curation`, and
`reports` found only the expected `PATHS.tsv` row, `record_review_queue.tsv` row,
raw ChEBI row, and generated YAML. No prior review report, curated overlay, or
second generated record claims this exact Standard InChIKey.

## Evidence

The target record has no evidence-bearing assertions. That is schema-valid for a
ChEBI-seeded record because the source concept supplies database provenance and
no mechanism, target, activity, resistance, producer, or causal claim has been
promoted into curator-owned slots.

A bounded exact-stereoisomer PubMed/Semantic Scholar search for
`"(2E,6Z)-3,7,11-trimethyldodeca-2,6,10-trien-1-ol"`, `"(2E,6Z)-farnesol"`,
`"(2-trans,6-cis)-farnesol"`, `"2-trans,6-cis-farnesol"`, `"3879-60-5"`, and
`"CRDAMVZIKSXKFV-GNESMGCMSA-N"` in PubMed Title/Abstract metadata found 0 PubMed
candidates; Semantic Scholar returned HTTP 429 or an invalid unauthenticated
response. Direct NCBI ESearch for the same Title/Abstract query also returned 0
PubMed IDs, with and without antimicrobial terms.

A broader PubMed fallback query for `farnesol` with `2E`, `6Z`, `(E,Z)`, the
Beilstein accession, or the CAS number found 9 candidates; adding antimicrobial
terms reduced that set to 3. Only one was a true chemical near miss:
PMID:28109063 reports antifungal testing of *Calendula arvensis* essential oil
and hydrosol extracts and identifies `(E,Z)-farnesol` among many essential-oil
constituents. It does not support an `ActivityObservation` for isolated
`(2E,6Z)-farnesol`.

The other fallback antimicrobial hits were false positives for this record:
PMID:25268327 tested host plant volatile lures against insect pests, and
PMID:1723037 appeared only because its PMID is identical to the Beilstein
accession on `CHEBI:35966`.

## Completeness

The record is incomplete as a reviewed antimicrobial record. Its generic
antimicrobial role is inherited from stereochemically broader `CHEBI:28600`; no
inspected source in this review identified a target group, assay organism,
quantitative MIC or equivalent endpoint, or mode of action for isolated
`CHEBI:35966`.

The empty `mode_of_action`, `molecular_targets`, `activity_spectrum`,
`resistance_mechanisms`, `producer_organisms`, and `causal_graphs` slots are
therefore preferable to over-scoped filler. A later curation pass should add to
them only after it has a primary source for the exact compound or an explicitly
defensible reason to curate from a stereoisomeric mixture.

No producer-candidate row is queued for this record, and the bounded
publication searches did not find a biosynthetic producer claim for this
stereoisomer.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | No stereoisomer-specific antimicrobial assay or mechanism has been curated for `CHEBI:35966`. | The record contains only an inherited generic `CHEBI:33281` role and no evidence-bearing objects; `just worklist` queues only `mechanism` and `review-readiness`; bounded exact PubMed searches found no isolated `(2E,6Z)-farnesol` antimicrobial assay. | Future curator-owned additions on `data/antibiotics/unspecified/2-trans-6-cis-farnesol.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blocker identity, structure, schema, or xref findings were found.

No minor findings.

## Recommended Edits

1. Keep `mode_of_action`, `molecular_targets`, `activity_spectrum`,
   `resistance_mechanisms`, `producer_organisms`, and `causal_graphs` empty until
   a curator finds primary evidence for isolated `(2E,6Z)-farnesol` or a source
   that explicitly assays a known stereoisomeric composition containing it.
2. If an exact assay is found, add one or more claim-level `ActivityObservation`
   entries with the organism or strain, assay, endpoint, value qualifier, units,
   and primary citation. Preserve `ANTIMICROBIAL_UNSPECIFIED` unless the source
   establishes a narrower antibacterial, antifungal, antiprotozoal, antiviral, or
   biocidal target group for the exact structure.
3. If exact mechanism evidence is found, curate `mode_of_action` with `CURATOR:`
   provenance, set `mode_of_action_target_scope`, and add target or causal-graph
   assertions only at the same scope as their primary evidence.

## Follow-up Checks

After any future curation, run:

| Check | Purpose |
|---|---|
| `just validate data/antibiotics/unspecified/2-trans-6-cis-farnesol.yaml` | Confirm the edited YAML still validates as an `AntibioticRecord`. |
| `just validate-strict data/antibiotics/unspecified/2-trans-6-cis-farnesol.yaml --out /tmp/antibioticmech-trans-cis-farnesol-35966-validation.tsv` | Confirm closed-schema validation has zero errors. |
| `just verify-corpus --summary` | Confirm any curator-owned additions survive seeding and no generated ChEBI fields drift. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-trans-cis-farnesol-35966.tsv` | Confirm the mechanism/review-readiness rows change only when a curator has actually resolved them. |
| `just review-queue --limit 40` | Confirm the queue position if the record is still `SEEDED`, or confirm it leaves the queue only after `REVIEWED` or `DEPRECATED` is justified. |

## Additional Notes

`uvx --from oaklib runoak -i ols:chebi info CHEBI:35966 CHEBI:28600 CHEBI:33281`
resolved the three relevant ChEBI CURIEs through OLS. Direct `curl` calls to EBI
OLS verified the term payload and parent/role endpoints used for the detailed
edge checks.

All repository publication searches used `env -u NCBI_EMAIL` so no contact email
was sent in NCBI API metadata. The first punctuation-heavy exact query
overmatched newer PubMed records that mentioned unrelated `trans`, `cis`, and
`2E` tokens, so the review above relies on the narrower Title/Abstract query,
direct NCBI ESearch confirmation, and the deliberately broader farnesol fallback
summarized under **Evidence**.
