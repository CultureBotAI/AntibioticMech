# YAML Record Review: (−)-vincadifformine

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antiprotozoal/vincadifformine.yaml`
- Started UTC: 2026-09-24T21:19:57Z
- Finished UTC: 2026-09-24T21:23:20Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:70507` |
| Label | `(−)-vincadifformine` |
| Path | `data/antibiotics/antiprotozoal/vincadifformine.yaml` |
| Class | `ANTIPROTOZOAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:70507` / `(−)-vincadifformine` |
| Minted source key | `antibioticmech:chebi-b8a9c2c831` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, structure, class, role, synonym, xref, or source-PMID changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:156` names `CHEBI:70507`, label
  `(−)-vincadifformine`, and the review hint
  `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:2060` maps `CHEBI:70507` to the
  `ANTIPROTOZOAL` directory and `vincadifformine` slug.
- `data/raw/chebi_antimicrobials.tsv:1794` is the ChEBI source row that seeds
  the target record.
- The whole 63-line target YAML was read before judging generated identity,
  structure, xrefs, source concept, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiprotozoal/vincadifformine.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antiprotozoal/vincadifformine.yaml --out /tmp/vincadifformine-70507-validate-strict.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2939 expected records, 2939 on disk, no missing, unexpected, drifted, `PATHS.tsv`-absent, or stale-lockfile records. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv` | Passed after emitting the known unrelated `iclaprim` / `CHEBI:31724` CARD diagnostic; `CHEBI:70507` appears in `mechanism` and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Passed and confirmed `CHEBI:70507` remains in the review-readiness queue as `MECHANISM_REVIEW`, with nine source literature leads, zero record evidence items, and zero targets. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and `PATHS.tsv`
inputs.

## Identity and Grounding

The seeded identity is consistent with the authoritative ChEBI record:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:70507`, `(−)-vincadifformine` | Official ChEBI resolved `CHEBI:70507` to `(-)-vincadifformine`. |
| Definition | `An aspidosperma alkaloid...` | Matched ChEBI. |
| Formula and charge | `C21H26N2O2`, charge `0` | Matched ChEBI. |
| Masses | average `338.451`, monoisotopic `338.19943` | Matched ChEBI. |
| SMILES | `[H][C@]12N3CCC[C@@]1(CC)CC(C(=O)OC)=C1Nc4ccccc4[C@@]12CC3` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C21H26N2O2/c1-3-20-9-6-11-23-12-10-21(19(20)23)15-7-4-5-8-16(15)22-17(21)14(13-20)18(24)25-2/h4-5,7-8,19,22H,3,6,9-13H2,1-2H3/t19-,20-,21-/m0/s1` | Matched ChEBI. |
| InChIKey | `GIGFIWJRTMBSRP-ACRUOGEOSA-N` | Matched ChEBI. |
| Parent compounds | `CHEBI:142772`, `CHEBI:25248`, `CHEBI:38101`, `CHEBI:38164`, `CHEBI:50995`, `CHEBI:50996` | ChEBI asserts exactly these six direct `subClassOf` parents. |
| Xrefs | `cas:3247-10-7`, `knapsack:C00024463` | Matched the official ChEBI term. |

Official ChEBI also relates `CHEBI:70507` to the protonated
`CHEBI:142771` / `(-)-vincadifformine(1+)` and the enantiomeric
`CHEBI:142834` / `(+)-vincadifformine`. The generated record is the exact
negative enantiomer with Standard InChIKey `GIGFIWJRTMBSRP-ACRUOGEOSA-N`, not
the sibling positive enantiomer whose Standard InChIKey is
`GIGFIWJRTMBSRP-NJDAHSKKSA-N`.

Official ChEBI asserts two direct roles for exact `CHEBI:70507`:
`CHEBI:64915` / `antiplasmodial drug` and `CHEBI:76924` /
`plant metabolite`. The generated record correctly omits the out-of-scope plant
role and preserves the ChEBI antimicrobial role that drives the
`ANTIPROTOZOAL` filing class.

## Evidence

The target record has no record-level `evidence`. That is allowed for a
ChEBI-seeded record because the ChEBI source concept supplies provenance, and
there are no `activity_spectrum`, `molecular_targets`,
`resistance_mechanisms`, `producer_organisms`, `clinical_status_assertions`,
`datasets`, or `causal_graphs` that would require claim-local evidence.

`data/raw/chebi_antimicrobials.tsv:1794` carries nine PubMed leads for exact
`CHEBI:70507`. Public PubMed metadata supports the identity, isolation, and
total-synthesis trail but does not expose a record-ready antiplasmodial
observation:

| PMID | Public title/abstract support |
|---|---|
| `PMID:13900664` | No public abstract; the indexed title reports isolation of alkuammidine and vincadifformine from leaves of *Vinca difformis*. |
| `PMID:13935801` | No public abstract; the indexed title reports vincadifformine and minovine from *Vinca minor*. |
| `PMID:13943964` | No public abstract; the indexed title reports `(-) vincadifformine` among new *Vinca minor* alkaloids. |
| `PMID:21043460` | Reports alkaloids from *Alstonia spatulata* leaf and stem-bark extracts; this supports the plant-source clause in the ChEBI definition. |
| `PMID:21753848` | Reports asymmetric total synthesis including vincadifformine by organocascade catalysis. |
| `PMID:23971538` | Reports total synthesis of `(-)-vincadifformine`. |
| `PMID:25522533` | Reports vincadifformine as one of eight known alkaloids isolated from *Kopsia arborea* twigs; the public abstract does not attach the tested bioactivity to vincadifformine. |
| `PMID:27936683` | Reports total syntheses of Aspidosperma alkaloids including `(-)-vincadifformine`. |
| `PMID:29131648` | Reports vincadifformine as a main alkaloid in *Vinca minor* leaves and compares alkaloid abundance after methyl jasmonate treatment. |

Bounded PubMed searches:

- The exact query for `vincadifformine` title/abstract records returned 41
  PMIDs. A local scan of those fetched records found zero public title or
  abstract mentions of `antiplasmodial`, `plasmodium`, `malaria`,
  `antiprotozoal`, or `trypanosoma`.
- The targeted PubMed query
  `vincadifformine AND (Plasmodium OR antiplasmodial OR malaria OR trypanosoma
  OR antiprotozoal)` in Title/Abstract returned zero PMIDs.
- PubMed dropped `6,7-dihydrotabersonine` from phrase searches, so these
  searches should not be treated as exhaustive synonym searches for the ChEBI
  synonym set.
- The PubMed xref query dropped the InChIKey stem and KNApSAcK identifier and
  searched only `3247-10-7`; it returned 17 broad vincadifformine PMIDs and
  did not materially narrow the exact-compound activity search.

## Completeness

Consequential gaps:

- `activity_spectrum` is absent, so the record has no exact Plasmodium or other
  protozoan taxon, strain, assay, value, qualifier, unit, or claim-local
  evidence for exact `CHEBI:70507`.
- `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`,
  `molecular_targets`, and `causal_graphs` are absent, so the record has no
  curator-owned antiprotozoal mechanism.
- `producer_organisms` is absent despite source PMIDs naming *Vinca difformis*,
  *Vinca minor*, *Alstonia spatulata*, and *Kopsia arborea* as vincadifformine
  plant-source leads and the ChEBI definition specifically mentioning
  *Alstonia spatulata*. Full-text review is still needed before any lead can be
  promoted to an exact `(−)-vincadifformine` producer assertion.

Correctly empty optional slots:

- No `resistance_mechanisms`: the record is ChEBI-only and CARD resistance
  routes do not apply.
- No `clinical_status` or `clinical_status_assertions`: the ChEBI-only source
  concept and inspected metadata do not assert regulatory use.
- No `datasets`: inspected ChEBI and PubMed metadata did not surface a public
  screening, omics, or structural dataset accession for exact
  `(−)-vincadifformine`.

Ignored-inclusive absence search:

- Ran `rg --hidden --no-ignore` over `curation/`, `data/raw/`,
  `data/antibiotics/`, `reports/yaml_record_review/`, the full exported
  worklist and review queue under `/tmp/`, and `.git` for `CHEBI:70507`,
  `vincadifformine`, `Vincadifformine`, `vincadifformine.yaml`,
  `GIGFIWJRTMBSRP`, `3247-10-7`, and `C00024463`.
- The search included ignored files and found only the expected generated
  target, `PATHS.tsv`, ChEBI raw row, exported worklist and review-queue rows,
  the maintained review-queue row, the checked-out branch name in `.git`, and
  one adjacent `(16R,19E)-isositsirikine` prior report mentioning
  `CHEBI:70507`. It found no prior exact `CHEBI:70507` review report,
  `curation/decisions.tsv` row, curated mechanism decision, or curated
  activity/provenance addition for this exact ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | VINCADIFFORMINE-70507-M1 | The record is still a seeded exact-compound stub with a ChEBI-derived antiplasmodial role but no curator-owned antiplasmodial activity spectrum, producer assertion, mode of action, mechanism scope, molecular target, or causal graph. | `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` reports `MECHANISM_REVIEW: mechanism is absent` with nine source literature leads, zero record evidence items, and zero targets; `/tmp/antibioticmech-worklist.tsv` lists `CHEBI:70507` only on `mechanism` and `review-readiness`. The exact-vincadifformine ChEBI PubMed leads and broader 41-PMID title/abstract search surfaced no public abstract antiplasmodial observation ready to curate. | `data/antibiotics/antiprotozoal/vincadifformine.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`; or `curation/decisions.tsv` if full-text inspection cannot verify exact `(−)-vincadifformine` antiplasmodial activity. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the full text of the nine ChEBI-linked source papers for exact
   `CHEBI:70507` and determine which publication, if any, substantiates the
   ChEBI `antiplasmodial drug` role.
2. Add claim-local `activity_spectrum` observations only if an inspected source
   reports isolated exact `(−)-vincadifformine` against a parasite taxon with a
   usable assay, value, qualifier, and unit; do not generalize plant extract,
   related-alkaloid, racemic-mixture, or synthetic-analogue activity onto exact
   `CHEBI:70507`.
3. Curate `mode_of_action`, `mode_of_action_target_scope`,
   `mode_of_action_notes`, molecular targets, and a causal graph only to the
   precision directly supported by inspected exact-compound mechanism sources.
4. If a source verifies biosynthesis or isolation of exact
   `(−)-vincadifformine` in a named plant species or strain, add a
   `producer_organisms` assertion with claim-local evidence.
5. If exact `(−)-vincadifformine` antiplasmodial activity cannot be verified,
   leave the record `SEEDED` and add either a curator discussion for the
   ChEBI-derived role or a source-concept decision in `curation/decisions.tsv`
   if the ChEBI role is clearly unsupported.
6. Preserve the seeded ChEBI identity, stereospecific structure, parent, xrefs,
   source PMIDs, and source concept. This review found no grounded-identity
   correction that belongs in `data/raw/chebi_antimicrobials.tsv` or
   `data/antibiotics/PATHS.tsv`.

## Follow-up Checks

- `just validate-strict data/antibiotics/antiprotozoal/vincadifformine.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-vincadifformine.tsv`
- `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue-vincadifformine.tsv`
- `just qc`
- Manual diff review of `data/antibiotics/antiprotozoal/vincadifformine.yaml`
  and `curation/decisions.tsv` to confirm every new exact-structure claim is
  claim-local and directly supported by an inspected primary source.

## Additional Notes

- `NCBI_EMAIL` was unset in the local environment before direct PubMed
  E-Utilities fetches; no contact email was sent as NCBI API metadata.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded finding above.
