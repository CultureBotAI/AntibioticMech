# YAML Record Review: (2S)-6-formyl-8-methyl-7-O-methylpinocembrin

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antiviral/2s-6-formyl-8-methyl-7-o-methylpinocembrin.yaml`
- Started UTC: 2026-09-22T07:10:00Z
- Finished UTC: 2026-09-22T07:15:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:70660` |
| Label | `(2S)-6-formyl-8-methyl-7-O-methylpinocembrin` |
| Path | `data/antibiotics/antiviral/2s-6-formyl-8-methyl-7-o-methylpinocembrin.yaml` |
| Class | `ANTIVIRAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:70660`, version `2026-08-30`, minted key `antibioticmech:chebi-4ed58a85ad` |
| Source role | `CHEBI:52425` EC 3.2.1.18 inhibitor |
| Structure | `HGTSZOYDQGUVER-AWEZNQCLSA-N`; formula `C18H16O5`; charge `0` |
| Same-structure xrefs | `reaxys:5449075` |
| Source literature lead | `PMID:20886838` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded flavanone record. The YAML has
source-derived identity, definition, one exact ChEBI synonym, three ChEBI
parents, one exo-alpha-sialidase-inhibitor role, one source-seeded
`VIRAL_RELEASE_INHIBITION` mode, one same-structure xref, structure, and
source-concept metadata, but no curator-owned target, activity observation,
resistance mechanism, producer, discussion, dataset, causal graph, or
claim-level evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiviral/2s-6-formyl-8-methyl-7-o-methylpinocembrin.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antiviral/2s-6-formyl-8-methyl-7-o-methylpinocembrin.yaml --out /tmp/antibioticmech-chebi-70660-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-70660.tsv` | Pass: the full worklist TSV was written. `CHEBI:70660` appears on `mechanism`, `producer-candidate`, and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 49` | Pass: `CHEBI:70660` is the first queued record after the records that already have `reports/yaml_record_review` reports; its row says `MECHANISM_REVIEW: mechanism is source-seeded and not curator-checked; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:70660` resolves in official OLS as a current, non-obsolete ChEBI term
labeled `(2S)-6-formyl-8-methyl-7-O-methylpinocembrin`. The live OLS
annotations list the same formula, charge, average mass, monoisotopic mass,
Standard InChI, Standard InChIKey, SMILES, Reaxys cross-reference, and PubMed
cross-reference as the committed `data/raw/chebi_antimicrobials.tsv` row.

The generated record's three `parent_compounds` entries are exactly the
official OLS hierarchical parents of `CHEBI:70660`: `CHEBI:17478` aldehyde,
`CHEBI:38738` monomethoxyflavanone, and `CHEBI:38748`
monohydroxyflavanone.

The `ANTIVIRAL` filing class, `VIRAL_RELEASE_INHIBITION` mode, and
`HOST_SHARED_TARGET` target scope are consistent with the ChEBI role. The live
`CHEBI:52425` role resolves in OLS as current and non-obsolete
`EC 3.2.1.18 (exo-alpha-sialidase) inhibitor`, and `conf/sources.yaml` maps that
role to `ANTIVIRAL`, source-seeded `VIRAL_RELEASE_INHIBITION`, and
`HOST_SHARED_TARGET`.

The generated same-structure xref is correctly scoped. ChEBI attaches
`reaxys:5449075` and `pubmed:20886838` to this exact term; the YAML imports the
Reaxys registry xref, while the raw ChEBI inventory exposes the PubMed article
as source-literature provenance rather than as a same-structure database xref.

An ignored-inclusive search for `CHEBI:70660`, the exact label, and the
filename stem across `data/antibiotics`, `data/raw`, `curation`, and `reports`
found only the expected PATHS row, generated YAML, raw ChEBI row, and
review-readiness row. It found no prior dedicated review report, curation
decision, curator-inventory row, generated activity observation, molecular
target, resistance, producer, or causal-graph claim resolving `CHEBI:70660`.

## Evidence

The only mechanistic assertion is source-seeded from ChEBI role `CHEBI:52425`.
The record has no evidence-bearing `MolecularTarget`, `ActivityObservation`,
`ResistanceMechanism`, `ProducerOrganism`, `Dataset`, or `CausalGraph` objects,
so no primary source has been promoted onto a curator-owned claim.

The committed raw ChEBI row for `CHEBI:70660` has one source-literature lead:
`PMID:20886838`. PubMed resolves that PMID to Dao, Tung, Nguyen, Thuong, Yoo,
Kim, Kim, and Oh's 2010 Journal of Natural Products paper, DOI
`10.1021/np1002753`, and Crossref resolves the same DOI to the same title and
journal.

PubMed's abstract reports that four new and 10 known C-methylated flavonoids
were isolated from methanol extract of `Cleistocalyx operculatus` buds using an
influenza H1N1 neuraminidase-inhibition assay. It states that compounds 4, 7, 8,
and 14, all chalcones, had significant inhibitory effects on H1N1 and H9N2 viral
neuraminidases; compound 4 was strongest against wild-type and H274Y-mutant
novel H1N1 neuraminidases expressed in 293T cells. The abstract is enough to
confirm the ChEBI source paper's antiviral screening context, but it does not
map exact flavanone `CHEBI:70660` to a source-paper compound number or expose an
IC50 for this structure.

NCBI Taxonomy maps the isolation-source name `Cleistocalyx operculatus` to
species `NCBITaxon:219895`, whose current scientific name is
`Syzygium nervosum` and whose synonym list retains `Cleistocalyx operculatus`.

A bounded repository publication search for the exact Standard InChIKey
`HGTSZOYDQGUVER-AWEZNQCLSA-N` found zero PubMed candidates. A second search for
the exact ChEBI-linked paper title found one PubMed candidate: `PMID:20886838`.
Semantic Scholar returned HTTP 429 for both of those focused searches.

## Completeness

The record is incomplete as a reviewed antiviral natural-product record. It has
exact ChEBI identity, structure, chemically broader aldehyde, flavanone, and
methoxyflavanone parents, an exo-alpha-sialidase-inhibitor role, a
source-seeded release-inhibition mode, one same-structure registry xref, and a
primary-paper lead, but no curator-owned molecular target, activity
observation, producer, dataset, or causal graph.

The source-seeded mode is not enough to make this record `REVIEWED`. The record
needs a full inspection of DOI `10.1021/np1002753` to determine whether exact
`CHEBI:70660` was one of the source paper's neuraminidase-inhibiting compounds,
whether the reported target was a specific influenza neuraminidase, whether a
quantitative IC50 or only a qualitative observation is in scope, and whether any
viral strain or H274Y-mutant context can be curated.

The empty `molecular_targets`, `resistance_mechanisms`, `activity_spectrum`,
`producer_organisms`, `clinical_status_assertions`, `datasets`, `discussions`,
and `causal_graphs` slots are preferable to over-scoped filler. The inspected
abstract supports a plant isolation source but does not support a biosynthetic
producer assertion; `just worklist` correctly reports a `producer-candidate` row
for curator review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The source-seeded neuraminidase-inhibition mechanism has not been curator-checked against claim-level primary evidence for exact `CHEBI:70660`. | `mode_of_action` and `mode_of_action_target_scope` were seeded from `CHEBI:52425`; the record has zero record evidence items and zero targets; the only ChEBI source-literature lead is `PMID:20886838`; PubMed's abstract names the active chalcones but does not map exact flavanone `CHEBI:70660` to a compound number, IC50, enzyme target, or influenza strain. | Future curator-owned fields on `data/antibiotics/antiviral/2s-6-formyl-8-methyl-7-o-methylpinocembrin.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI later changes this term's role or source xrefs, the ChEBI inventory extractor owns that refresh. |

No blocker identity, structure, schema, xref, class, parentage, or source-seeded
mode-mapping findings were found.

No minor findings.

## Recommended Edits

1. Inspect the full DOI `10.1021/np1002753` before keeping, revising, or
   replacing the source-seeded `VIRAL_RELEASE_INHIBITION` mode with curator
   provenance. Confirm the exact compound number and whether this flavanone, not
   only the paper's active chalcones, inhibited influenza neuraminidase.
2. Add a `MolecularTarget` for the viral neuraminidase only if the full paper
   supports an exact target assertion for this compound. Preserve any distinction
   between wild-type H1N1, oseltamivir-resistant H1N1 H274Y, and H9N2 assays.
3. Add `activity_spectrum` rows only for source-reported observations with exact
   compound identity, assay, units, and organism or strain scope. Use IC50 fields
   only if the table maps quantitative values to `CHEBI:70660`.
4. Treat `Cleistocalyx operculatus` / `Syzygium nervosum` as an isolation-source
   lead, not automatically as a biosynthetic producer. A `producer_organisms`
   assertion should be added only if an inspected primary source explicitly
   supports a compound-to-organism production claim.
5. Leave the ChEBI PubMed cross-reference out of the same-structure `xrefs`;
   cite PMID `20886838` from assertion-level `evidence` blocks if its table or
   text is later curated into target, activity, or provenance fields.

## Follow-up Checks

After any exact-term curation or source refresh, rerun:

1. `just validate data/antibiotics/antiviral/2s-6-formyl-8-methyl-7-o-methylpinocembrin.yaml`
2. `just validate-strict data/antibiotics/antiviral/2s-6-formyl-8-methyl-7-o-methylpinocembrin.yaml --out /tmp/antibioticmech-chebi-70660-validation.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-70660.tsv`
5. `just review-queue --limit 49`
6. `just qc`

Manually compare future activity and target curation against the full Dao,
Tung, Nguyen, Thuong, Yoo, Kim, Kim, and Oh paper to confirm that any curated
neuraminidase inhibition claim is attached to exact `CHEBI:70660` rather than a
chalcone sibling from the same Cleistocalyx paper.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, so they
included ignored `reports/` files.

`runoak` was not available in this shell, so official ChEBI term checks were
performed against the EBI OLS4 HTTPS API.

Direct HTTPS access to the ACS DOI page returned Cloudflare's HTTP 403
challenge, so the report uses PubMed and Crossref metadata for the ChEBI-linked
source article.

Semantic Scholar returned HTTP 429 for both focused repository publication
searches; the PubMed side of both searches completed.
