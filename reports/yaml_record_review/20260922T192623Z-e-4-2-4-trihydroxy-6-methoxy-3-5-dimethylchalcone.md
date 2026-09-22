# YAML Record Review: (E)-4,2',4'-trihydroxy-6'-methoxy-3',5'-dimethylchalcone

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antiviral/e-4-2-4-trihydroxy-6-methoxy-3-5-dimethylchalcone.yaml`
- Started UTC: 2026-09-22T19:20:00Z
- Finished UTC: 2026-09-22T19:26:42Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:70655` |
| Label | `(E)-4,2',4'-trihydroxy-6'-methoxy-3',5'-dimethylchalcone` |
| Path | `data/antibiotics/antiviral/e-4-2-4-trihydroxy-6-methoxy-3-5-dimethylchalcone.yaml` |
| Class | `ANTIVIRAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:70655`, version `2026-08-30`, minted key `antibioticmech:chebi-57a8caee72` |
| Source role | `CHEBI:52425` EC 3.2.1.18 inhibitor |
| Parent compounds | `CHEBI:23086`, `CHEBI:25235`, `CHEBI:26195` |
| Structure | `HTDSMOBGCNRBHQ-RMKNXTFCSA-N`; formula `C18H18O5`; charge `0` |
| Xrefs | `reaxys:21040404` |
| Source literature lead | `PMID:20886838` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded antiviral chalcone record. The
YAML has source-derived exact ChEBI grounding, a ChEBI definition, one exact
IUPAC synonym, three strictly broader ChEBI parents, one Reaxys xref, one
exo-alpha-sialidase-inhibitor role, source-seeded viral-release mode-of-action
fields, structure, and source-concept metadata. It has no generated or
curator-owned molecular target, activity observation, resistance mechanism,
producer, discussion, dataset, causal graph, or claim-level evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiviral/e-4-2-4-trihydroxy-6-methoxy-3-5-dimethylchalcone.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antiviral/e-4-2-4-trihydroxy-6-methoxy-3-5-dimethylchalcone.yaml --out /tmp/antibioticmech-chebi-70655-strict.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-70655-worklist.tsv` | Pass: the full worklist TSV was written. `CHEBI:70655` appears on `mechanism`, `producer-candidate`, and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 120` | Pass: `CHEBI:70655` is the first queued record after the records that already have `reports/yaml_record_review` reports; its row says `MECHANISM_REVIEW: mechanism is source-seeded and not curator-checked; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:70655` resolves in official OLS as a current, non-obsolete 3-star ChEBI
term labeled `(E)-4,2',4'-trihydroxy-6'-methoxy-3',5'-dimethylchalcone`. The
live OLS annotations list the same formula, charge, average mass, monoisotopic
mass, Standard InChI, Standard InChIKey, SMILES, Reaxys cross-reference, and
PubMed cross-reference as the committed `data/raw/chebi_antimicrobials.tsv`
row.

The live OLS graph gives `CHEBI:70655` three direct hierarchical parents:
`CHEBI:23086` `chalcones`, `CHEBI:25235` `monomethoxybenzene`, and
`CHEBI:26195` `polyphenol`. Those are exactly the generated
`parent_compounds` values. OLS also links `CHEBI:70655` to `CHEBI:48965`
`trans-chalcone` as a related structural parent and to `CHEBI:76924` `plant
metabolite` by role; those broader edges do not belong in `parent_compounds` or
antimicrobial `activity_roles`.

The generated `ANTIVIRAL` filing class, source-seeded
`VIRAL_RELEASE_INHIBITION` mode, and `HOST_SHARED_TARGET` scope are consistent
with the ChEBI antimicrobial role. Live OLS resolves `CHEBI:52425` as a
current, non-obsolete ChEBI term labeled `EC 3.2.1.18 (exo-alpha-sialidase)
inhibitor`; the live ChEBI relation endpoint includes that role on
`CHEBI:70655`; `data/raw/chebi_role_names.tsv` marks it as a
`class,mode_of_action` role; and `conf/sources.yaml` maps it to `ANTIVIRAL`,
`VIRAL_RELEASE_INHIBITION`, and `HOST_SHARED_TARGET`.

The generated same-structure xref is correctly scoped. ChEBI attaches
`reaxys:21040404` and `pubmed:20886838` to this exact term; the YAML imports
the Reaxys registry xref, while the raw ChEBI inventory exposes the PubMed
article as source-literature provenance rather than as a same-structure
database xref.

Before this review branch was created, ignored-inclusive searches found no
prior dedicated `CHEBI:70655` review report or same-named local or remote
branch, and no curation decision, curator-inventory row, generated activity
observation, molecular target, resistance, producer, dataset, or causal-graph
claim resolving this record. The exact identifier search across
`data/antibiotics`, `data/raw`, `curation`, `conf`, and
`reports/yaml_record_review` found only the expected `PATHS.tsv` row,
generated YAML, raw ChEBI row, and review-readiness row.

## Evidence

The record's antiviral classification and source-seeded viral-release mechanism
are inherited from ChEBI role `CHEBI:52425`, `EC 3.2.1.18
(exo-alpha-sialidase) inhibitor`. That role is sufficient for the generator to
file the record under `ANTIVIRAL` and infer `VIRAL_RELEASE_INHIBITION` with
`HOST_SHARED_TARGET`; it is not compound-specific primary evidence for a
particular viral neuraminidase, a particular influenza isolate, a measured
activity observation, or a causal graph edge.

OLS and the raw ChEBI inventory expose one PubMed cross-reference for exact
`CHEBI:70655`: `PMID:20886838`. The repository publication helper and Europe
PMC both resolve that PMID to Dao, Tung, Nguyen, Thuong, Yoo, Kim, Kim, and
Oh's 2010 Journal of Natural Products paper, DOI `10.1021/np1002753`. Europe
PMC reports the article as absent from PMC/Europe PMC open full text, with a
subscription-only DOI full-text URL and no indexed supplement.

The inspected abstract reports isolation of 14 C-methylated flavonoids from
the methanol extract of `Cleistocalyx operculatus` buds by using an influenza
H1N1 neuraminidase-inhibition assay. It further reports that compounds 4, 7, 8,
and 14, all chalcones, inhibited viral neuraminidases from H1N1 and H9N2, that
compound 4 had the strongest wild-type H1N1 and oseltamivir-resistant H1N1
H274Y activity, and that compounds 4, 7, 8, and 14 behaved as noncompetitive
inhibitors in kinetic studies. The abstract therefore supports the ChEBI source
paper as an exact antiviral-screening lead for this chalcone record, but it
does not map exact `CHEBI:70655` to a source-paper compound number, IC50,
enzyme target, or influenza strain.

NCBI Taxonomy no longer resolves `Cleistocalyx operculatus` as a current
scientific name, but its all-names search maps that synonym to species
`NCBITaxon:219895`, whose current scientific name is `Syzygium nervosum` and
whose synonym list retains `Cleistocalyx operculatus`. That mapping confirms
the plant name as a taxon lead; it does not, by itself, promote the isolation
context into a `ProducerOrganism` claim.

Bounded repository publication searches for `PMID:20886838` and for the
`Cleistocalyx operculatus` chalcone-neuraminidase context each found the same
PubMed candidate, `PMID:20886838`. A search for the exact Standard InChIKey
`HTDSMOBGCNRBHQ-RMKNXTFCSA-N` found zero PubMed candidates. Semantic Scholar
returned HTTP 429 or an invalid response for those focused searches.

## Completeness

The record is incomplete as a reviewed influenza neuraminidase-inhibitor
record. It has exact ChEBI identity, structure, one same-structure xref, three
strictly broader ChEBI parents, ChEBI EC 3.2.1.18 inhibitor classification, a
source-seeded release-inhibition mode, and a primary-paper lead, but no
primary-paper evidence, no `activity_spectrum`, no molecular target, no
producer, no dataset, and no causal graph.

The empty molecular target, activity, and causal graph slots are correct for
the current seed. ChEBI states a broad EC 3.2.1.18 inhibitor role, and the
generated note correctly warns that this role is also a host-shared target
family, but exact viral-neuraminidase target curation still needs full-paper
mapping from exact `CHEBI:70655` to one of Dao et al.'s numbered chalcones and
their measured H1N1, H274Y, and H9N2 assays.

The empty producer slot is preferable to over-scoped filler.
`Cleistocalyx operculatus`, now `Syzygium nervosum`, is a credible isolation
source, and the full worklist correctly reports a `producer-candidate` row for
curator review, but the source-only phrase does not by itself prove a
biosynthetic producer claim.

The empty `resistance_mechanisms`, `clinical_status_assertions`, `datasets`,
and `discussions` slots are also acceptable. No measured resistance edge,
clinical assertion, public dataset accession, or discussion-worthy conflict
with exact `CHEBI:70655` claim-level evidence was identified in the bounded
checks.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:70655` has source-level ChEBI neuraminidase-inhibitor classification and a generated viral-release mechanism, but no curator-owned primary evidence for exact activity, a molecular target, or a causal graph. | The generated record has one source literature lead, zero record evidence items, zero `activity_spectrum` rows, zero targets, and no causal graph. OLS supports the ChEBI `has role` assertion, and the abstract for `PMID:20886838` reports that compounds 4, 7, 8, and 14 in the Cleistocalyx paper were active chalcones, but the inspected abstract does not name exact `CHEBI:70655` or map it to a compound number or assay row. | Future curator-owned fields on `data/antibiotics/antiviral/e-4-2-4-trihydroxy-6-methoxy-3-5-dimethylchalcone.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI later changes this term's roles, xrefs, parents, or citations, the ChEBI inventory extractor owns that refresh. |

No blocker identity, structure, schema, xref, class, parentage, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Inspect DOI `10.1021/np1002753` in full and map compounds 4, 7, 8, and 14 to
   exact ChEBI structures before keeping, revising, or replacing the
   source-seeded `VIRAL_RELEASE_INHIBITION` mode with curator provenance for
   `CHEBI:70655`.
2. Add a `MolecularTarget` for influenza viral neuraminidase only if the full
   paper supports an exact target assertion for this compound. Preserve any
   distinction between wild-type H1N1, oseltamivir-resistant H1N1 H274Y, and
   H9N2 assays.
3. Add `activity_spectrum` rows only for source-reported observations with
   exact compound identity, assay, value, units, and organism or strain scope.
   Use IC50 fields only if the table maps quantitative values to `CHEBI:70655`.
4. Treat `Cleistocalyx operculatus` / `Syzygium nervosum` as an isolation-source
   lead, not automatically as a biosynthetic producer. Add a `ProducerOrganism`
   row only if inspected primary evidence supports exact `CHEBI:70655`
   production and satisfies the field's assertion-level evidence requirements.
5. Leave the ChEBI PubMed cross-reference out of the same-structure `xrefs`;
   cite PMID `20886838` from assertion-level `evidence` blocks if its tables or
   text are later curated into target, activity, or provenance fields.

## Follow-up Checks

After any exact-term curation or source refresh, rerun:

1. `just validate data/antibiotics/antiviral/e-4-2-4-trihydroxy-6-methoxy-3-5-dimethylchalcone.yaml`
2. `just validate-strict data/antibiotics/antiviral/e-4-2-4-trihydroxy-6-methoxy-3-5-dimethylchalcone.yaml --out /tmp/antibioticmech-chebi-70655-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-70655-worklist.tsv`
5. `just review-queue --limit 120`
6. `just qc`

Manually compare future activity, target, and causal-graph curation against the
full Dao, Tung, Nguyen, Thuong, Yoo, Kim, Kim, and Oh paper to confirm that any
curated neuraminidase-inhibition claim is attached to exact `CHEBI:70655`
rather than to a chalcone sibling from the same Cleistocalyx paper.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, `find`, or
Git/GitHub ref listing, so they included ignored `reports/` files or otherwise
did not depend on Git's ignore filters.
