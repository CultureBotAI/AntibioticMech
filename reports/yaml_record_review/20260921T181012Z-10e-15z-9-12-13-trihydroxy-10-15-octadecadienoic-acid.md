# YAML Record Review: (10E,15Z)-9,12,13-trihydroxy-10,15-octadecadienoic acid

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antifungal/10e-15z-9-12-13-trihydroxy-10-15-octadecadienoic-acid.yaml`
- Started UTC: 2026-09-21T18:06:00Z
- Finished UTC: 2026-09-21T18:10:12Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:91218` |
| Label | `(10E,15Z)-9,12,13-trihydroxy-10,15-octadecadienoic acid` |
| Path | `data/antibiotics/antifungal/10e-15z-9-12-13-trihydroxy-10-15-octadecadienoic-acid.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:91218` / `(10E,15Z)-9,12,13-trihydroxy-10,15-octadecadienoic acid` |
| Minted source key | `antibioticmech:chebi-f84264e3cc` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, structure, class, role, synonym, or xref changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:28` names `CHEBI:91218`, label
  `(10E,15Z)-9,12,13-trihydroxy-10,15-octadecadienoic acid`, the four source
  literature leads `PMID:15668923|PMID:19731587|PMID:25457500|PMID:9658577`,
  and the review hint `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:2606` maps `CHEBI:91218` to the `ANTIFUNGAL`
  directory and `10e-15z-9-12-13-trihydroxy-10-15-octadecadienoic-acid` slug.
- `data/raw/chebi_antimicrobials.tsv:2426` is the ChEBI source row that seeds
  the target record.
- The whole 56-line target YAML was read before judging generated identity,
  structure, xrefs, source concept, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/10e-15z-9-12-13-trihydroxy-10-15-octadecadienoic-acid.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/10e-15z-9-12-13-trihydroxy-10-15-octadecadienoic-acid.yaml --out /tmp/antibioticmech-octadecadienoic-acid-91218-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2939 expected records, 2939 on disk, no missing, unexpected, or drifted records, no identifiers absent from `PATHS.tsv`, and no stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-octadecadienoic-acid-91218.tsv` | Passed; `CHEBI:91218` appears in `mechanism` and `review-readiness`. |
| `just review-queue --limit 28` | Passed and confirmed `CHEBI:91218` remains in the review-readiness queue as `MECHANISM_REVIEW`, with four source literature leads, zero record evidence items, and zero targets. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and PATHS
inputs.

## Identity and Grounding

The seeded identity is consistent with the authoritative ChEBI record:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:91218`, `(10E,15Z)-9,12,13-trihydroxy-10,15-octadecadienoic acid` | Official ChEBI resolved `CHEBI:91218` to the same compound, with the same ASCII name. |
| Definition | An octadecanoid that is `(10E,15Z)-octadecadienoic acid` with three hydroxy substituents at positions 9, 12, and 13 | Matched ChEBI. |
| Formula and charge | `C18H32O5`, charge `0` | Matched ChEBI. |
| Masses | average `328.449`, monoisotopic `328.22497` | Matched ChEBI. |
| SMILES | `CC/C=C\CC(O)C(O)/C=C/C(O)CCCCCCCC(=O)O` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C18H32O5/c1-2-3-7-11-16(20)17(21)14-13-15(19)10-8-5-4-6-9-12-18(22)23/h3,7,13-17,19-21H,2,4-6,8-12H2,1H3,(H,22,23)/b7-3-,14-13+` | Matched ChEBI. |
| InChIKey | `MKYUCBXUUSZMQB-MKZMYESJSA-N` | Matched ChEBI. |
| Antifungal role | `CHEBI:35718` | ChEBI asserts `has role` to `antifungal agent`. |
| Parent compounds | `CHEBI:140345`, `CHEBI:15904`, `CHEBI:36326`, `CHEBI:61121` | ChEBI asserts the same `is a` relationships to hydroxy polyunsaturated fatty acid, long-chain fatty acid, octadecanoid, and oxylipin. |
| IUPAC name and synonyms | `(10E,15Z)-9,12,13-trihydroxyoctadeca-10,15-dienoic acid`, `9,12,13-trihydroxy-10(E),15(Z)-octadecadienoic acid`, `Corchorifatty acid F` | Matched ChEBI; ChEBI sources `Corchorifatty acid F` from LIPID MAPS. |
| Xrefs | `cas:95341-44-9`, `hmdb:HMDB0035919`, `reaxys:2287207` | Matched ChEBI's manual xref and registry rows. |

ChEBI also asserts the non-antimicrobial roles `antioxidant` `CHEBI:22586`,
`plant metabolite` `CHEBI:76924`, and `Bronsted acid` `CHEBI:39141`.
The seeded AntibioticMech record retains the ChEBI `antifungal agent` role
that drives inclusion in this repository and this review found no identity
evidence that the record should move out of the `ANTIFUNGAL` filing class.

ChEBI names three plant occurrences that can seed future producer review:

| Organism | Component | Source |
|---|---|---|
| `Arabidopsis thaliana` | root | `PMID:25457500`; MetaboLights `MTBLS160` |
| `Corchorus olitorius` | leaf | `PMID:9658577` |
| `Malva sylvestris` | not specified | `PMID:19731587` |

## Evidence

The target record has no record-level `evidence`. That is allowed for a
ChEBI-seeded record because the ChEBI source concept supplies provenance, and
there are no `activity_spectrum`, `molecular_targets`,
`resistance_mechanisms`, `producer_organisms`, `clinical_status_assertions`,
`datasets`, or `causal_graphs` that would require claim-level evidence.

`data/raw/chebi_antimicrobials.tsv:2426` carries four PubMed leads imported
from ChEBI for the exact source concept:

| PMID | Public abstract support |
|---|---|
| `PMID:15668923` | Reports that 9,12,13-trihydroxy-10(E),15(Z)-octadecadienoic acid reduced powdery mildew infection in second barley leaves when the oxylipin was applied to first leaves. This is the direct antifungal lead for the record, but its full assay context and whether the effect is a direct fungal inhibition or plant-mediated induced defense still need full-text review before a precise `activity_spectrum` or mechanism claim can be added. |
| `PMID:19731587` | Reports isolating `(10E,15Z)-9,12,13-trihydroxyoctadeca-10,15-dienoic acid` from *Malva sylvestris* in an antioxidant and radical-scavenging study. The abstract supports the ChEBI occurrence lead, not antimicrobial activity. |
| `PMID:25457500` | Reports nontargeted profiling of the semipolar fraction of *Arabidopsis thaliana* root exudates and identification of oxylipins. The abstract supports a candidate *Arabidopsis* metabolite-source lead, not antimicrobial activity. |
| `PMID:9658577` | Reports isolating corchorifatty acid F from the less-polar fraction of `moroheiya`, the leaves of *Corchorus olitorius*, and determining the corchorifatty-acid structures and optical purity. The abstract reports NO-production inhibition for corchorifatty acids A, B, and C, not F. |

A broader exact-name PubMed search for `Corchorifatty acid F` returned newer
plant, food, host-cell inflammation, and agricultural metabolomics papers. The
most antifungal-adjacent lead was `PMID:38460554`, where zinc- or
manganese-primed *Capsicum annuum* accumulated corchorifatty acid F during
*Botrytis cinerea* infection but the abstract names acetophenone, not
corchorifatty acid F, as the compound tested for direct toxicity against
*B. cinerea*. The inspected broader PubMed abstracts did not resolve a molecular
target, resistance mechanism, MIC-style activity observation, or dataset that
could be curated without full-text follow-up.

## Completeness

Consequential gaps:

- `activity_spectrum` is absent despite the ChEBI source row already carrying
  `PMID:15668923` as a direct oxylipin and powdery-mildew lead.
- `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`,
  `molecular_targets`, and `causal_graphs` are absent, so the record has no
  curator-owned antifungal mechanism.
- `producer_organisms` is absent despite ChEBI occurrence leads for
  *Arabidopsis thaliana*, *Corchorus olitorius*, and *Malva sylvestris*.
- `datasets` is absent despite the ChEBI MetaboLights `MTBLS160` lead for the
  *A. thaliana* root-exudate occurrence.

Correctly empty optional slots:

- No `resistance_mechanisms`: the record is ChEBI-only and CARD resistance
  routes do not apply.
- No `clinical_status` or `clinical_status_assertions`: the ChEBI-only source
  concept and inspected metadata do not assert regulatory use.

Ignored-inclusive absence search:

- Ran `rg --hidden --no-ignore` over `curation/`, `data/raw/`,
  `data/antibiotics/`, `reports/yaml_record_review/`, and the full exported
  worklist for these exact terms: `CHEBI:91218`;
  `(10E,15Z)-9,12,13-trihydroxy-10,15-octadecadienoic acid`;
  `10e-15z-9-12-13-trihydroxy-10-15-octadecadienoic-acid`;
  `MKYUCBXUUSZMQB-MKZMYESJSA-N`; `95341-44-9`; `HMDB0035919`; `2287207`;
  and `Corchorifatty acid F`.
- The search included ignored files and found only the expected generated
  target, `PATHS.tsv`, ChEBI raw row, worklist rows, and review-queue row. It
  found no prior review report, `curation/decisions.tsv` row, curated
  mechanism decision, or curated activity/provenance addition for this exact
  ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | OCTADECADIENOIC-91218-M1 | The record is still a seeded ChEBI stub even though the source row already carries one direct antifungal activity lead and several plant-occurrence leads. It has no curated activity observation, producer assertion, dataset assertion, mode of action, mechanism scope, molecular target, or causal graph. | `just review-queue --limit 28` reports `MECHANISM_REVIEW: mechanism is absent; 4 source literature lead(s), 0 record evidence item(s), 0 target(s)`; `/tmp/antibioticmech-worklist-octadecadienoic-acid-91218.tsv` lists `CHEBI:91218` in `mechanism` and `review-readiness`; public abstracts for `PMID:15668923`, `PMID:19731587`, `PMID:25457500`, and `PMID:9658577` show curated activity and producer follow-up work rather than a completed claim-local record. | `data/antibiotics/antifungal/10e-15z-9-12-13-trihydroxy-10-15-octadecadienoic-acid.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the full text for `PMID:15668923` and capture the barley cultivar,
   fungal organism or strain, oxylipin dose, treatment location, endpoint, and
   statistical result behind the powdery-mildew infection reduction. Add an
   `activity_spectrum` observation only if the result is representable without
   overstating a plant-induced defense phenotype as direct fungal killing.
2. Curate `mode_of_action`, `mode_of_action_target_scope`,
   `mode_of_action_notes`, molecular targets, and a causal graph only to the
   precision directly supported by inspected exact-compound mechanism sources.
   Leave mechanism fields empty if the available evidence only shows host plant
   defense priming.
3. Inspect `PMID:25457500`, `PMID:9658577`, `PMID:19731587`, and MetaboLights
   `MTBLS160` to determine which plant occurrence rows are specific enough for
   `producer_organisms` or `datasets` entries with claim-local evidence.
4. Check the `PMID:38460554` full text for the *Capsicum annuum* and
   *Botrytis cinerea* infection response only as a producer or defense-signaling
   lead; do not curate acetophenone toxicity as an effect of corchorifatty acid
   F.
5. Preserve the seeded ChEBI identity, neutral exact structure, parent terms,
   synonyms, xrefs, source concept, and `ANTIFUNGAL` filing class. This review
   found no seeded-identity correction that belongs in
   `data/raw/chebi_antimicrobials.tsv` or `data/antibiotics/PATHS.tsv`.

## Follow-up Checks

- `just validate-strict data/antibiotics/antifungal/10e-15z-9-12-13-trihydroxy-10-15-octadecadienoic-acid.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-octadecadienoic-acid-91218.tsv`
- `just review-queue --limit 28`
- `just qc`
- Manual diff review of
  `data/antibiotics/antifungal/10e-15z-9-12-13-trihydroxy-10-15-octadecadienoic-acid.yaml`
  to confirm every antimicrobial activity, producer, dataset, or mechanism
  claim is claim-local and directly supported by an inspected primary source or
  durable dataset.

## Additional Notes

- `NCBI_EMAIL` was unset in the local environment before using the PubMed
  search script; no contact email was sent as NCBI API metadata.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded finding above.
- Search result metadata was used only to triage source leads. No candidate
  abstract was treated as claim-local evidence for a record field that would
  require exact activity, taxon, strain, or mechanism context from the inspected
  primary source.
