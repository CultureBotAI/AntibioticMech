# YAML Record Review: (2E,6Z)-13-hydroxy-1-(2-hydroxy-5-methoxy-3-methylphenyl)-3,7,11,15-tetramethylhexadeca-2,6,14-triene-5,12-dione

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml`
- Started UTC: 2026-09-22T02:02:00Z
- Finished UTC: 2026-09-22T02:20:08Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:65995` |
| Label | `(2E,6Z)-13-hydroxy-1-(2-hydroxy-5-methoxy-3-methylphenyl)-3,7,11,15-tetramethylhexadeca-2,6,14-triene-5,12-dione` |
| Path | `data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:65995`, version `2026-08-30`, minted key `antibioticmech:chebi-d4565c9404` |
| Source role | `CHEBI:33282` antibacterial agent |
| Structure | `HBKSTRSDLUAESY-PKVUCGNLSA-N`; formula `C28H40O5`; charge `0` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded meroterpenoid record. The YAML
has source-derived identity, definition, synonym, ChEBI parents, antibacterial
role, structure, and source-concept metadata, but no curator-owned mode of
action, target, activity observation, producer, resistance mechanism,
discussion, dataset, or causal graph.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml --out /tmp/antibioticmech-chebi-65995-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-65995.tsv` | Pass: the full worklist TSV was written. `CHEBI:65995` appears on `mechanism`, `producer-candidate`, and `review-readiness`; it has 0 CARD targets and 0 resistance edges to build on. |
| `just review-queue --limit 43` | Pass: `CHEBI:65995` is the next queued record after `CHEBI:28913`; its row says `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this ChEBI-seeded record; the schema/strict checks and `verify-corpus` are the
narrowest documented local gates.

## Identity and Grounding

`CHEBI:65995` resolves in official OLS as a current, non-obsolete, 3-star ChEBI
term labeled `(2E,6Z)-13-hydroxy-1-(2-hydroxy-5-methoxy-3-methylphenyl)-3,7,11,15-tetramethylhexadeca-2,6,14-triene-5,12-dione`.
OLS lists `Z-Halidrysone A` as a synonym, PMID:18529079 as the ChEBI database
cross-reference, and the same Standard InChIKey, formula, charge, average mass,
and monoisotopic mass as the committed `data/raw/chebi_antimicrobials.tsv` row.

The generated record's six `parent_compounds` are exactly the official OLS
direct parents of `CHEBI:65995`: `CHEBI:2468` secondary alpha-hydroxy ketone,
`CHEBI:33853` phenols, `CHEBI:35618` aromatic ether, `CHEBI:35681` secondary
alcohol, `CHEBI:51689` enone, and `CHEBI:64419` meroterpenoid.

The `ANTIBACTERIAL` filing class is source-backed. Official OLS lists
`CHEBI:33282` antibacterial agent as a direct `has_role` filler on
`CHEBI:65995`, and the generated record preserves that in-scope ChEBI role in
`activity_roles`. OLS also lists `CHEBI:51076` antifouling biocide and
`CHEBI:25212` metabolite as ChEBI roles, but the committed antimicrobial source
row intentionally retains only the antibacterial role.

The record has no generated `xrefs`, `drug_xrefs`, or `document_xrefs`. The raw
ChEBI inventory row likewise has an empty xref column for `CHEBI:65995`, so no
same-structure cross-reference is being asserted without an InChIKey check.

An ignored-inclusive search for `CHEBI:65995`,
`HBKSTRSDLUAESY-PKVUCGNLSA-N`, `antibioticmech:chebi-d4565c9404`, and
`Z-Halidrysone` across `data/antibiotics`, `data/raw`, `curation`, and
`reports` found only the expected `PATHS.tsv` row, `record_review_queue.tsv`
row, raw ChEBI row, and generated YAML. No prior review report, curated
overlay, or second generated record claims this exact Standard InChIKey.

## Evidence

The target record has no evidence-bearing assertions. That is schema-valid for a
ChEBI-seeded record because the source concept supplies database provenance and
no mechanism, target, activity, resistance, producer, dataset, or causal claim
has been promoted into curator-owned slots.

A direct PubMed lookup for `PMID:18529079` resolves to Culioli et al. 2008,
`DOI:10.1021/np070110k`, a Journal of Natural Products paper on antifouling
meroditerpenoids from the brown alga *Halidrys siliquosa*. The PubMed abstract
supports the broad source context: the study isolated nine tetraprenyltoluquinol
metabolites from *H. siliquosa*, elucidated their planar structures, and tested
antibacterial growth inhibition and *Balanus amphitrite* cyprid settlement. The
abstract reports sub-2.5 microg/mL MICs for the most active compounds 2, 6, and
9 but does not name which of those numbered structures, if any, is
`Z-Halidrysone A`; the ACS full text at the DOI was behind a Cloudflare
JavaScript challenge during this review.

A bounded repository publication search for `18529079[pmid]` found the PubMed
record above and hit Semantic Scholar HTTP 429. A second bounded search for
`"Z-Halidrysone A" OR "Halidrysone A" OR "Halidrys siliquosa" antibacterial
antifouling meroditerpenoid` again found only PMID:18529079 on PubMed and again
hit Semantic Scholar HTTP 429.

## Completeness

The record is incomplete as a reviewed antimicrobial record. It has exact ChEBI
identity, structure, parents, and antibacterial role, but the only associated
literature lead has not been resolved into claim-level activity observations,
an antimicrobial mode of action, a molecular target, or a causal graph.

The empty `mode_of_action`, `molecular_targets`, `activity_spectrum`,
`resistance_mechanisms`, `producer_organisms`, `causal_graphs`, and `datasets`
slots are preferable to over-scoped filler. The PubMed abstract for
PMID:18529079 does not supply the exact compound-to-MIC mapping, tested
bacterial strain labels, or activity values needed for `ActivityObservation`
objects on this record.

`just worklist` correctly reports a `producer-candidate` row for
*Halidrys siliquosa* because the ChEBI definition says the compound was
isolated from that alga. The candidate is a source-only lead, not a
biosynthesis claim; it should stay out of `producer_organisms` unless the
primary paper or a later source supports actual production by the named taxon.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The lone ChEBI PMID lead for `CHEBI:65995` has not been resolved into exact activity, producer, or mechanism curation. | The generated YAML has no evidence-bearing objects; `just worklist` queues `CHEBI:65995` on `mechanism`, `producer-candidate`, and `review-readiness`; PubMed metadata for PMID:18529079 supports the source paper but does not map `Z-Halidrysone A` to a numbered tested compound or to exact MIC rows. | Future curator-owned fields on `data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blocker identity, structure, schema, or same-structure xref findings were
found.

No minor findings.

## Recommended Edits

1. Inspect the full text and supporting information for PMID:18529079 /
   `DOI:10.1021/np070110k`, map `Z-Halidrysone A` to its compound number, and
   add one `ActivityObservation` per exact organism or strain only where the
   source supplies the assay, value, qualifier, endpoint, and units for this
   exact structure.
2. Curate `mode_of_action`, `mode_of_action_target_scope`, molecular targets,
   or causal-graph edges only if the paper or a follow-on exact-compound source
   explains how `Z-Halidrysone A` inhibits bacterial growth; do not infer a
   target from meroterpenoid class membership or antifouling activity.
3. Do not add *Halidrys siliquosa* to `producer_organisms` from the ChEBI
   definition alone. Add a producer claim only if inspected evidence shows that
   the alga biosynthesizes this compound rather than merely being the isolation
   source.

## Follow-up Checks

After any curation, rerun:

1. `just validate data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml`
2. `just validate-strict data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml --out /tmp/antibioticmech-chebi-65995-validation.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-65995.tsv`
5. `just review-queue --limit 43`

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, so they
included ignored `reports/` files.

`runoak` was not available in this shell, so official ChEBI term checks were
performed against the EBI OLS4 HTTPS API.

Semantic Scholar returned HTTP 429 for both repository publication searches; the
PubMed side of both searches completed and returned candidates.
