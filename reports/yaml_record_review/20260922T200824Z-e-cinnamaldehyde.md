# YAML Record Review: (E)-cinnamaldehyde

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antifungal/e-cinnamaldehyde.yaml`
- Started UTC: 2026-09-22T20:03:50Z
- Finished UTC: 2026-09-22T20:08:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:16731` |
| Label | `(E)-cinnamaldehyde` |
| Path | `data/antibiotics/antifungal/e-cinnamaldehyde.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:16731`, version `2026-08-30`, minted key `antibioticmech:chebi-37832f9f09` |
| Source role | `CHEBI:35718` antifungal agent |
| Parent compounds | `CHEBI:142921`, `CHEBI:23245` |
| Structure | `KJPRLNWUNMBNBZ-QPJJXVBHSA-N`; formula `C9H8O`; charge `0` |
| Xrefs | `bpdb:1069`, `cas:14371-10-9`, `hmdb:HMDB0003441`, `kegg.compound:C00903`, `knapsack:C00002725`, `knapsack:C00035187`, `reaxys:1071571` |
| Source literature leads | `PMID:11975643`, `PMID:17140783`, `PMID:17662960`, `PMID:18218683`, `PMID:19845671`, `PMID:20431333`, `PMID:20955755`, `PMID:21266172`, `PMID:21388814`, `PMID:21394803` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded antifungal phenylpropanoid
record. The YAML has source-derived exact ChEBI grounding, a ChEBI definition,
ten exact ChEBI synonyms, two broader ChEBI parents, seven same-structure xrefs,
one antifungal role, structure, and source-concept metadata. It has no generated
or curator-owned activity observation, molecular target, resistance mechanism,
mode of action, producer, discussion, dataset, causal graph, or claim-level
evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/e-cinnamaldehyde.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/e-cinnamaldehyde.yaml --out /tmp/antibioticmech-chebi-16731-strict.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-16731-worklist.tsv` | Pass: the full worklist TSV was written. Exact `CHEBI:16731` appears on `mechanism` and `review-readiness`; it was not found on any other queue in that TSV. |
| `just review-queue --limit 140` | Pass: `CHEBI:16731` is the first queued record after the records that already have `reports/yaml_record_review` reports; its row says `MECHANISM_REVIEW: mechanism is absent; 10 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`data/raw/chebi_antimicrobials.tsv` seeds `CHEBI:16731` as a 3-star ChEBI entry
in antimicrobial role scope and gives the same label, exact definition, SMILES,
Standard InChI, Standard InChIKey, formula, charge, masses, ChEBI parent terms,
synonyms, and xrefs that appear in the generated YAML. OAK through OLS resolves
the identifier as `(E)-cinnamaldehyde`, resolves generated parent
`CHEBI:142921` as `3-phenylprop-2-enal`, resolves generated parent
`CHEBI:23245` as `cinnamaldehydes`, and resolves generated role `CHEBI:35718`
as `antifungal agent`.

The `ANTIFUNGAL` filing class is consistent with the only generated ChEBI role:
`CHEBI:35718` maps to `ANTIFUNGAL` in `conf/sources.yaml`. Because the source
row has no more-specific mechanism role, the generated YAML correctly has no
`mode_of_action`, `mode_of_action_target_scope`, molecular target, activity
observation, or causal graph.

The same-structure xrefs are correctly scoped to database accessions rather
than literature accessions. ChEBI attaches BPDB, CAS, HMDB, KEGG, KNApSAcK, and
Reaxys accessions to this term, and the YAML imports those accessions while
leaving the raw ChEBI PubMed citations as source-literature provenance.

Before this review branch was created, ignored-inclusive searches found no
prior dedicated `CHEBI:16731` or `e-cinnamaldehyde` review report and no
curation decision, curator-inventory row, generated activity observation,
molecular target, resistance, producer, dataset, or causal-graph claim resolving
this record. Exact branch lookups found no local branch, remote-tracking branch,
or remote `review-chebi-16731-cinnamaldehyde` branch.

## Evidence

The record's antifungal class comes from the broad ChEBI `CHEBI:35718`
`antifungal agent` role. That role is sufficient for the generator to file the
record under `ANTIFUNGAL`, but it is not assertion-level primary evidence for a
particular fungal organism, MIC value, fungal molecular target, mode of action,
or causal graph edge.

The ten ChEBI-seeded PubMed leads resolve through the repository publication
helper to studies of cinnamaldehyde as a reagent or as a bioactive in non-fungal
systems. They cover an organic-chemistry carbonylation reagent paper
(`PMID:11975643`), antidiabetic rat work (`PMID:17140783`), an antibacterial
FtsZ paper (`PMID:17662960`), TRPA1 and cough or sensory-neuron studies
(`PMID:18218683`, `PMID:19845671`, `PMID:21266172`), an allergen/prohapten
transcriptional study (`PMID:20431333`), a GLUT1 glucose-transport study
(`PMID:20955755`), a snake-venom analog study (`PMID:21388814`), and an in vivo
cytokine paper (`PMID:21394803`). None of the ChEBI-seeded abstracts provide
exact antifungal MICs, fungal target claims, or Candida mechanism evidence for
exact `CHEBI:16731`.

Focused repository publication searches for `cinnamaldehyde Candida albicans
minimum inhibitory concentration` and `cinnamaldehyde antifungal mechanism
Candida albicans` found direct primary antifungal leads that are absent from
the current YAML. Shreaz, Bhatia, Khan, Muralidhar, Basir, Manzoor, and Khan
reported MIC90 values for cinnamaldehyde against fluconazole-resistant
`Candida` isolates and investigated sterol biosynthesis and plasma-membrane
ATPase activity in `PMID:21708228`. Shahina, El-Ganiny, Minion, Whiteway,
Sultana, and Dahms reported `Candida albicans` cell-wall remodeling and spindle
defects after cinnamon bark oil or cinnamaldehyde treatment in `PMID:29456868`.
Ying and coauthors reported trans-cinnamaldehyde inhibition of `C. albicans`
adhesion, morphological transition, and biofilm formation with low serial-passage
resistance in `PMID:31176484`.

The same focused searches also returned more recent papers on formulations,
essential oils, derivatives, mixtures, docking studies, and reviews. Those are
useful discovery leads but should not be curated into exact
`CHEBI:16731` activity or target slots unless the full text reports an isolated
trans-cinnamaldehyde measurement and a source-specific assay row.

Semantic Scholar returned HTTP 429 or an invalid response for the bounded
publication-helper searches, but PubMed resolved both the ChEBI-seeded PMIDs and
the targeted cinnamaldehyde/Candida search leads.

## Completeness

The record is incomplete as a reviewed antifungal record. It has exact ChEBI
identity, structure, database xrefs, two broader ChEBI parents, a ChEBI
antifungal role, and source-paper leads, but no claim-level evidence, no
`activity_spectrum`, no molecular target, no mode of action, no producer, no
dataset, and no causal graph.

The empty molecular target, mode-of-action, and causal graph slots are correct
for the current seed. The ChEBI role proves only that the term is in antifungal
scope; it does not identify whether this record should model membrane
ergosterol disruption, fungal H+-ATPase inhibition, cell-wall remodeling,
tubulin/spindle disruption, a C. albicans virulence pathway, a biofilm-only
phenotype, or a broader unknown mechanism.

The empty `activity_spectrum` slot should be treated as missing curation, not
as negative activity. PubMed has primary leads for pure cinnamaldehyde against
fluconazole-resistant `Candida` isolates and for trans-cinnamaldehyde effects
against `Candida albicans`; exact organism, strain, assay, endpoint, value, and
unit details still need full-paper extraction.

The empty `producers`, `resistance_mechanisms`, `clinical_status_assertions`,
`datasets`, and `discussions` slots are acceptable for the generated record. No
producer row, measured resistance edge, clinical assertion, public dataset
accession, or discussion-worthy conflict with exact `CHEBI:16731` claim-level
evidence was identified in the bounded checks.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:16731` has source-level ChEBI antifungal classification, but no curator-owned primary evidence for exact antifungal activity, no activity observation, no molecular target, no mode of action, and no causal graph. | The generated record has 10 source literature leads, zero record evidence items, zero `activity_spectrum` rows, zero targets, no mode-of-action fields, and no causal graph. The worklist flags exact `CHEBI:16731` for `mechanism` and `review-readiness` only. The ChEBI-seeded PubMed abstracts do not support exact antifungal MICs or target claims, while bounded PubMed searches identify separate primary Candida leads such as `PMID:21708228`, `PMID:29456868`, and `PMID:31176484` that are not yet represented in the YAML. | Future curator-owned fields on `data/antibiotics/antifungal/e-cinnamaldehyde.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI later changes this term's roles, xrefs, parents, or citations, the ChEBI inventory extractor owns that refresh. |

No blocker identity, structure, schema, xref, class, parentage, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Add exact `activity_spectrum` rows only after inspecting full primary papers
   that report pure trans-cinnamaldehyde measurements. Preserve organism,
   strain or isolate, endpoint, value, unit, assay, and resistance phenotype
   distinctions from each source.
2. Inspect `PMID:21708228`, `PMID:29456868`, and `PMID:31176484` in full before
   choosing a mode of action. The abstracts point to different biological
   surfaces: sterol biosynthesis and plasma-membrane ATPase, cell-wall and
   spindle disruption, and Candida virulence or biofilm suppression.
3. Add a `MolecularTarget` only for a target that is directly assayed for exact
   `CHEBI:16731`. Do not promote docking-only targets, essential-oil mixture
   targets, or derivative activity into a target assertion for this record.
4. Do not add the ChEBI-seeded non-antifungal PubMed leads as evidence for the
   antifungal class. Keep `PMID:17662960` as an antibacterial FtsZ discovery
   lead only if this compound is later reviewed for an antibacterial claim.
5. Add a `ProducerOrganism` row only if inspected primary evidence supports
   exact cinnamaldehyde production by a taxon that satisfies the field's
   assertion-level evidence requirements.

## Follow-up Checks

After any exact-term curation or source refresh, rerun:

1. `just validate data/antibiotics/antifungal/e-cinnamaldehyde.yaml`
2. `just validate-strict data/antibiotics/antifungal/e-cinnamaldehyde.yaml --out /tmp/antibioticmech-chebi-16731-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-16731-worklist.tsv`
5. `just review-queue --limit 140`
6. `just qc`

Manually compare future MIC rows, mechanism claims, target assertions, and
causal-graph curation against full primary papers to confirm they are attached
to isolated `(E)-cinnamaldehyde` rather than cinnamon essential oil, delivery
formulations, cinnamaldehyde derivatives, or mixed phytochemical combinations.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden`, `find`, or
Git/GitHub ref listing, so they included ignored `reports/` files or otherwise
did not depend on Git's ignore filters.
