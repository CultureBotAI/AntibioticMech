# YAML Record Review: (−)-α-phellandrene

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/unspecified/α-phellandrene.yaml`
- Started UTC: 2026-09-24T22:36:00Z
- Finished UTC: 2026-09-24T22:54:08Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:301` |
| Label | `(−)-α-phellandrene` |
| Path | `data/antibiotics/unspecified/α-phellandrene.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:301` / `(−)-α-phellandrene` |
| Minted source key | `antibioticmech:chebi-dcac805eb1` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, structure, class, role, synonym, xref, or source-PMID changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:158` names `CHEBI:301`, label
  `(−)-α-phellandrene`, and the review hint
  `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:731` maps `CHEBI:301` to the
  `ANTIMICROBIAL_UNSPECIFIED` directory and `α-phellandrene` slug.
- `data/raw/chebi_antimicrobials.tsv:7` is the ChEBI source row that seeds the
  target record.
- The whole 68-line target YAML was read before judging generated identity,
  structure, xrefs, source concept, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/α-phellandrene.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/α-phellandrene.yaml --out /tmp/alpha-phellandrene-301-validate-strict.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed after emitting the known unrelated `iclaprim` / `CHEBI:31724` CARD diagnostic: 2939 expected records, 2939 on disk, no missing, unexpected, drifted, `PATHS.tsv`-absent, or stale-lockfile records. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv` | Passed after emitting the known unrelated `iclaprim` / `CHEBI:31724` CARD diagnostic; `CHEBI:301` appears in `mechanism`, `xref-span-conflict`, and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Passed and confirmed `CHEBI:301` remains in the review-readiness queue as `MECHANISM_REVIEW`, with one source literature lead, zero record evidence items, and zero targets. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and `PATHS.tsv`
inputs.

## Identity and Grounding

The seeded identity is consistent with official ChEBI for exact
`CHEBI:301`:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:301`, `(−)-α-phellandrene` | Official OLS resolved `CHEBI:301` to `(-)-alpha-phellandrene`. |
| Definition | `The (R)-(−)-stereoisomer of α-phellandrene.` | Matched ChEBI after stripping OLS HTML formatting. |
| Formula and charge | `C10H16`, charge `0` | Matched ChEBI. |
| Masses | average `136.238`, monoisotopic `136.1252` | Matched ChEBI. |
| SMILES | `[H][C@@]1(C(C)C)C=CC(C)=CC1` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C10H16/c1-8(2)10-6-4-9(3)5-7-10/h4-6,8,10H,7H2,1-3H3/t10-/m1/s1` | Matched ChEBI. |
| InChIKey | `OGLDWXZKYODSOB-SNVBAGLBSA-N` | Matched ChEBI. |
| Parent compounds | `CHEBI:50035` | ChEBI asserts `CHEBI:50035` / `alpha-phellandrene` as the direct `subClassOf` parent. |
| Activity role | `CHEBI:33281` | The committed ChEBI row assigns `antimicrobial agent`, the generic role that drives `ANTIMICROBIAL_UNSPECIFIED` filing. |

Official OLS relates exact `CHEBI:301` to `CHEBI:367` /
`(+)-alpha-phellandrene` only through `is enantiomer of`, and to the
stereochemically unspecified `CHEBI:50035` / `alpha-phellandrene` through the
broader `subClassOf` edge. The generated record is therefore the exact
`(R)/(−)` enantiomer with Standard InChIKey
`OGLDWXZKYODSOB-SNVBAGLBSA-N`, not the `(S)/(+)` enantiomer at
`data/antibiotics/unspecified/α-phellandrene-367.yaml` and not the
stereochemically unspecified parent at
`data/antibiotics/unspecified/α-phellandrene-50035.yaml`.

The record omits the broad `cas:99-83-2` xref even though ChEBI and KEGG still
publish it on `CHEBI:301`: `/tmp/antibioticmech-worklist.tsv` lists
`cas:99-83-2` as an `xref-span-conflict` shared by `CHEBI:301` and parent
`CHEBI:50035`. That omission is consistent with the invariant that an xref must
denote the same exact structure.

Checked exact xrefs:

| Xref | Check |
|---|---|
| `kegg.compound:C09875` | KEGG names `(R)-(-)-alpha-Phellandrene`, formula `C10H16`, and DB links to `ChEBI: 301`, `LIPIDMAPS: LMPR0102090021`, and `KNApSAcK: C00003051`. |
| `knapsack:C00003051` | KNApSAcK resolves `C00003051` to `alpha-Phellandrene`, formula `C10H16`, and the same stereospecific Standard InChI; its page uses the broad CAS `99-83-2`. |
| `lipidmaps:LMPR0102090021` | LIPID MAPS resolves `LMPR0102090021` to `(R)-(-)-alpha-Phellandrene`, formula `C10H16`, KEGG `C09875`, ChEBI `301`, and the same Standard InChIKey. |
| `cas:4221-98-1` | Present on official ChEBI and KEGG for exact `CHEBI:301`; the CAS Common Chemistry public page returned an application-shell detail error and its API returned `401`, so it was not independently verified. |
| `beilstein:2497824`, `beilstein:5239645`, `reaxys:4290853` | Present on official ChEBI; not independently checked because Beilstein/Reaxys are not publicly resolvable identifier registries. |
| `lipidmaps:LMPR01020061` | Present on official ChEBI, but the LIPID MAPS REST `lm_id` lookup returned `[]`; this may be a stale or retired LIPID MAPS accession. |

## Evidence

The target record has no record-level `evidence`. That is allowed for a
ChEBI-seeded record because the ChEBI source concept supplies provenance, and
there are no `activity_spectrum`, `molecular_targets`,
`resistance_mechanisms`, `producer_organisms`, `clinical_status_assertions`,
`datasets`, or `causal_graphs` that would require claim-local evidence.

`data/raw/chebi_antimicrobials.tsv:7` carries one PubMed lead for exact
`CHEBI:301`:

| PMID | Public title/abstract support |
|---|---|
| `PMID:16780354` | Reports in vivo and in vitro structure-activity work on conjugated-diene prohaptens in contact allergy, with DOI `10.1021/tx060006n`. The title and abstract support skin-sensitization and metabolic-activation work, not antimicrobial activity. |

Bounded PubMed searches:

- The query
  `("alpha-phellandrene"[Title/Abstract] OR "α-phellandrene"[Title/Abstract] OR phellandrene[Title/Abstract]) AND (antimicrobial[Title/Abstract] OR antibacterial[Title/Abstract] OR antifungal[Title/Abstract] OR MIC[Title/Abstract] OR "minimum inhibitory"[Title/Abstract])`
  returned 221 PMIDs, all of which were fetched. Most title/abstract records
  report essential-oil or extract mixtures containing stereochemically
  unspecified alpha-phellandrene, not exact isolated `(−)-α-phellandrene`.
- The xref/InChIKey query dropped `OGLDWXZKYODSOB`, `C09875`, `C00003051`,
  `LMPR01020061`, and `LMPR0102090021` as phrases not found, then searched
  only exact phrase `4221-98-1` and returned 71 PMIDs. The only public
  title/abstract hits naming exact `(-)-(R)-α-phellandrene` were a fragrance
  safety assessment (`PMID:35278499`) and an insect biotransformation paper
  (`PMID:10898642`), not antimicrobial assay reports.

Near antimicrobial leads that still do not support claim-local activity for
exact `CHEBI:301`:

| PMID | Why it is a near miss |
|---|---|
| `PMID:22899613` | Biotransforms exact `(-)-(R)-α-phellandrene` and tests the substrate plus metabolite `5-p-menthene-1,2-diol`; the public abstract reports moderate-to-good antibacterial and anticandidal MICs for the metabolite in comparison with the `(-)-(R)-α-phellandrene` substrate, but does not expose a record-ready exact-substrate MIC. |
| `PMID:28510196` | Reports dose-dependent growth inhibition, MIC/MFC values, hyphal disruption, and membrane-permeability effects for `α-Phellandrene` against *Penicillium cyclopium*; the public title and abstract are stereochemically unspecified and therefore support parent `CHEBI:50035`, not exact `(−)-α-phellandrene`. |
| `PMID:35736100` | Tests pure `α-phellandrene` as one of five essential-oil constituents against *Fusarium* species; the public abstract says carvacrol was the strongest radial-growth inhibitor and does not resolve α-phellandrene stereochemistry. |
| `PMID:33095499` | Reports antibacterial oils and hydrosols from *Canarium ovatum* rich in `>95% (S)-(+)-α-phellandrene`, the opposite enantiomer represented by `CHEBI:367`. |
| `PMID:40950592` | Reports *Clausena lansium* essential-oil and main-constituent activity against *Streptococcus mutans*, but the public abstract names `β-phellandrene`, not `α-phellandrene`, as the predominant peel-oil constituent. |
| `PMID:36295037` | A systematic review that summarizes pure alpha-phellandrene and alpha-phellandrene-rich essential-oil activity; useful for citation discovery, but secondary and not exact-enantiomer primary evidence by itself. |
| `PMID:15883716` | Tests selected essential oils and pure constituents against *Candida albicans*; the public abstract reports `beta-phellandrene` as the active cyclic monoterpenic hydrocarbon, not α-phellandrene. |

## Completeness

Consequential gaps:

- `activity_spectrum` is absent, so the record has no exact microbial taxon,
  strain, assay, value, qualifier, unit, or claim-local evidence for isolated
  exact `CHEBI:301`.
- `mode_of_action`, `mode_of_action_target_scope`,
  `mode_of_action_notes`, `molecular_targets`, and `causal_graphs` are absent,
  so the record has no curator-owned mechanism.
- `producer_organisms` is absent. KNApSAcK lists many plant occurrence leads
  for `C00003051`, but its public record is broad `alpha-Phellandrene` and
  cannot by itself establish biosynthesis of the exact `(R)/(−)` enantiomer.
- `lipidmaps:LMPR01020061` did not resolve through the current LIPID MAPS REST
  `lm_id` endpoint, leaving one generated exact xref unresolved.

Correctly empty optional slots:

- No `resistance_mechanisms`: the record is ChEBI-only and CARD resistance
  routes do not apply.
- No `clinical_status` or `clinical_status_assertions`: the ChEBI-only source
  concept and inspected metadata do not assert regulatory use.
- No `datasets`: inspected ChEBI, registry, and PubMed metadata did not surface
  a public screening, omics, or structural dataset accession for exact
  `(−)-α-phellandrene`.

Ignored-inclusive absence search:

- Ran `rg --hidden --no-ignore` over `curation/`, `data/raw/`,
  `data/antibiotics/`, `reports/yaml_record_review/`, the full exported
  worklist and review queue under `/tmp/`, and `.git` for `CHEBI:301`,
  `α-phellandrene`, `alpha-phellandrene`, `phellandrene`,
  `OGLDWXZKYODSOB-SNVBAGLBSA-N`, `4221-98-1`, `C09875`,
  `C00003051`, `LMPR01020061`, and `LMPR0102090021`.
- The search included ignored files. It found the generated target, the
  generated parent and sibling phellandrene records, `PATHS.tsv`, the ChEBI raw
  rows, exported worklist and review-queue rows, the maintained
  review-queue rows, and a prior `CHEBI:367` review report that mentions but
  does not review this exact `CHEBI:301` target. It found no prior exact
  `CHEBI:301` review report, no `curation/decisions.tsv` row, no curated
  mechanism decision, and no curated activity/provenance addition for this
  exact ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | PHELLANDRENE-301-M1 | The record is still a seeded exact-enantiomer stub with a generic ChEBI antimicrobial role but no curator-owned isolated-compound activity spectrum, mode of action, mechanism scope, molecular target, producer assertion, or causal graph. | `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` reports `MECHANISM_REVIEW: mechanism is absent` with one source literature lead, zero record evidence items, and zero targets; `/tmp/antibioticmech-worklist.tsv` lists `CHEBI:301` in `mechanism` and `review-readiness`. The exact ChEBI PubMed source supports contact-allergy structure/activity work, the 221-PMID bounded PubMed search surfaced exact-metabolite, unspecified-parent, opposite-enantiomer, review, and essential-oil mixture leads, and no exact `(−)-α-phellandrene` MIC or mechanism claim has been curated onto the record. | `data/antibiotics/unspecified/α-phellandrene.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`; or `curation/decisions.tsv` if exact `(−)-α-phellandrene` antimicrobial activity cannot be verified. |
| Minor | PHELLANDRENE-301-m1 | `lipidmaps:LMPR01020061` may be stale: the current LIPID MAPS REST API did not resolve it, while `lipidmaps:LMPR0102090021` resolved to exact `CHEBI:301`. | The generated record carries both LIPID MAPS xrefs from official ChEBI; `curl https://www.lipidmaps.org/rest/compound/lm_id/LMPR01020061/all/` returned `[]`, while the same lookup for `LMPR0102090021` returned `(R)-(-)-alpha-Phellandrene`, formula `C10H16`, KEGG `C09875`, ChEBI `301`, and InChIKey `OGLDWXZKYODSOB-SNVBAGLBSA-N`. | ChEBI xref import from `data/raw/chebi_antimicrobials.tsv`, with a future extractor/seeder xref filter only if this accession is confirmed retired rather than temporarily absent from the REST API. |

No blocker findings.

## Recommended Edits

1. Inspect full text for `PMID:22899613` and its assay tables to determine
   whether exact `(-)-(R)-α-phellandrene`, not only the metabolite
   `5-p-menthene-1,2-diol`, has a representable MIC or anticandidal value.
2. Inspect primary papers from the 221-PMID alpha-phellandrene search that test
   isolated `α-phellandrene`; curate activity onto exact `CHEBI:301` only when
   the paper resolves the tested reagent to the `(R)/(−)` enantiomer rather
   than stereochemically unspecified `CHEBI:50035`.
3. Keep `CHEBI:367` / `(+)-α-phellandrene` and `CHEBI:50035` /
   `α-phellandrene` activity separate from `CHEBI:301`. Do not generalize
   *Canarium ovatum* `(S)/(+)`-phellandrene oil activity or unspecified
   alpha-phellandrene MICs onto this record.
4. Curate `mode_of_action`, `mode_of_action_target_scope`,
   `mode_of_action_notes`, molecular targets, and a causal graph only to the
   precision directly supported by inspected exact-compound mechanism sources.
5. Add `producer_organisms` assertions only from primary sources that verify a
   named organism biosynthesizes exact `(−)-α-phellandrene`; keep KNApSAcK
   broad-occurrence leads and exact stereochemical claims separate.
6. Recheck `LMPR01020061` through LIPID MAPS or ChEBI during the next ChEBI
   refresh. If the accession is confirmed retired, drop it through the
   maintained ChEBI extraction or seeding path rather than hand-editing
   `data/antibiotics/unspecified/α-phellandrene.yaml`.
7. If exact `(−)-α-phellandrene` antimicrobial activity cannot be verified,
   leave the record `SEEDED` and add either a curator discussion for the
   ChEBI-derived role or a source-concept decision in `curation/decisions.tsv`
   if the ChEBI antimicrobial role is clearly unsupported.

## Follow-up Checks

- `just validate-strict data/antibiotics/unspecified/α-phellandrene.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-alpha-phellandrene.tsv`
- `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue-alpha-phellandrene.tsv`
- `just qc`
- Manual diff review of `data/antibiotics/unspecified/α-phellandrene.yaml`,
  `curation/decisions.tsv`, and any xref filtering path to confirm every
  retained activity or xref claim is exact-structure and source-supported.

## Additional Notes

- `NCBI_EMAIL` was absent from the local environment before direct PubMed
  E-Utilities fetches; no contact email was sent as NCBI API metadata.
- The local `runoak` executable was unavailable, so this review used the
  official OLS HTTP API for ChEBI identity, parent, and enantiomer checks.
- The CAS Common Chemistry public page for `4221-98-1` returned an application
  shell with `Get detail failed: TypeError: Cannot read properties of undefined
  (reading 'message')`, and the apparent detail API returned HTTP `401`.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded finding above.
