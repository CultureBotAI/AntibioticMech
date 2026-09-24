# YAML Record Review: (−)-α-gurjunene

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antibacterial/α-gurjunene.yaml`
- Started UTC: 2026-09-24T22:00:00Z
- Finished UTC: 2026-09-24T22:06:48Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:61699` |
| Label | `(−)-α-gurjunene` |
| Path | `data/antibiotics/antibacterial/α-gurjunene.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:61699` / `(−)-α-gurjunene` |
| Minted source key | `antibioticmech:chebi-670bdceaad` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, structure, class, role, synonym, xref, or source-PMID changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:157` names `CHEBI:61699`, label
  `(−)-α-gurjunene`, and the review hint
  `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:1324` maps `CHEBI:61699` to the
  `ANTIBACTERIAL` directory and `α-gurjunene` slug.
- `data/raw/chebi_antimicrobials.tsv:1075` is the ChEBI source row that seeds
  the target record.
- The whole 54-line target YAML was read before judging generated identity,
  structure, xrefs, source concept, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/α-gurjunene.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/α-gurjunene.yaml --out /tmp/alpha-gurjunene-61699-validate-strict.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed after emitting the known unrelated `iclaprim` / `CHEBI:31724` CARD diagnostic: 2939 expected records, 2939 on disk, no missing, unexpected, drifted, `PATHS.tsv`-absent, or stale-lockfile records. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv` | Passed after emitting the known unrelated `iclaprim` / `CHEBI:31724` CARD diagnostic; `CHEBI:61699` appears in `mechanism`, `producer-candidate`, and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Passed and confirmed `CHEBI:61699` remains in the review-readiness queue as `MECHANISM_REVIEW`, with four source literature leads, zero record evidence items, and zero targets. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and `PATHS.tsv`
inputs.

## Identity and Grounding

The seeded identity is consistent with the authoritative ChEBI record:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:61699`, `(−)-α-gurjunene` | Official ChEBI resolved `CHEBI:61699` to `(-)-alpha-gurjunene`. |
| Definition | `A carbotricyclic compound and sesquiterpene...` | Matched ChEBI after stripping OLS HTML formatting. |
| Formula and charge | `C15H24`, charge `0` | Matched ChEBI. |
| Masses | average `204.357`, monoisotopic `204.1878` | Matched ChEBI. |
| SMILES | `[H][C@]12CCC(C)=C1[C@]1([H])C(C)(C)[C@]1([H])CC[C@H]2C` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C15H24/c1-9-6-8-12-14(15(12,3)4)13-10(2)5-7-11(9)13/h9,11-12,14H,5-8H2,1-4H3/t9-,11-,12-,14-/m1/s1` | Matched ChEBI. |
| InChIKey | `SPCXZDDGSGTVAW-XIDUGBJDSA-N` | Matched ChEBI. |
| Parent compounds | `CHEBI:35189`, `CHEBI:38032` | ChEBI asserts exactly these two direct `subClassOf` parents: `sesquiterpene` and `carbotricyclic compound`. |
| Xrefs | `cas:489-40-7`, `kegg.compound:C19734`, `metacyc.compound:CPD-12891`, `reaxys:1939514` | Matched the official ChEBI term. |

Official ChEBI relates `CHEBI:61699` to the enantiomeric `CHEBI:132832` /
`(+)-alpha-gurjunene`, and the OLS graph uses exact `CHEBI:61699` as the
functional parent of `5-hydroxy-alpha-gurjunene`. The generated record is the
exact negative enantiomer with Standard InChIKey
`SPCXZDDGSGTVAW-XIDUGBJDSA-N`.

Official ChEBI asserts three direct roles for exact `CHEBI:61699`:
`CHEBI:33282` / `antibacterial agent`, `CHEBI:27311` /
`volatile oil component`, and `CHEBI:76924` / `plant metabolite`. The generated
record correctly omits the volatile-oil and plant roles and preserves the ChEBI
antimicrobial role that drives the `ANTIBACTERIAL` filing class.

## Evidence

The target record has no record-level `evidence`. That is allowed for a
ChEBI-seeded record because the ChEBI source concept supplies provenance, and
there are no `activity_spectrum`, `molecular_targets`,
`resistance_mechanisms`, `producer_organisms`, `clinical_status_assertions`,
`datasets`, or `causal_graphs` that would require claim-local evidence.

`data/raw/chebi_antimicrobials.tsv:1075` carries four PubMed leads for exact
`CHEBI:61699`. Public PubMed metadata supports identity, synthase, and plant
mixture leads but does not expose a record-ready isolated-compound
antibacterial observation:

| PMID | Public title/abstract support |
|---|---|
| `PMID:10190971` | Reports isolation, characterization, and mechanistic studies of `(-)-alpha-gurjunene synthase` from *Solidago canadensis*. The abstract supports exact biosynthetic-enzyme discovery, not antibacterial activity. |
| `PMID:19731610` | Reports *Anaphalis nubigena* essential-oil composition and MIC values for the oil against *Escherichia coli* and *Klebsiella pneumoniae*; `alpha-gurjunene` was 6.0% of a 60-component mixture. |
| `PMID:23365607` | Reports *Porella arboris-vitae* extract composition and antimicrobial MIC ranges for extracts; `alpha-gurjunene` was 6.0% to 10.9% of the assayed mixtures. |
| `PMID:24371539` | Reports volatile and essential-oil composition from *Jatropha ribifolia* roots, including `alpha-gurjunene`; the public abstract does not report an antimicrobial assay. |

Bounded PubMed searches:

- The query
  `(alpha-gurjunene OR α-gurjunene OR gurjunene) AND (antibacterial OR
  antimicrobial OR minimum inhibitory OR MIC)` in Title/Abstract returned 27
  PMIDs. A local scan of all fetched public title/abstract records surfaced
  essential oils, extracts, volatile fractions, or review leads that mention a
  gurjunene constituent, but no public title or abstract that exposed an
  isolated exact `(−)-α-gurjunene` MIC or mechanism ready to curate.
- The PubMed xref query dropped the InChIKey stem, CAS number, and MetaCyc ID
  as quoted phrases not found and searched only `C19734`; it returned four
  PMIDs and did not materially narrow the exact-compound search.

## Completeness

Consequential gaps:

- `activity_spectrum` is absent, so the record has no exact bacterial taxon,
  strain, assay, value, qualifier, unit, or claim-local evidence for isolated
  exact `CHEBI:61699`.
- `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`,
  `molecular_targets`, and `causal_graphs` are absent, so the record has no
  curator-owned antibacterial mechanism.
- `producer_organisms` is absent despite the ChEBI-linked source PMIDs naming
  *Solidago canadensis*, *Anaphalis nubigena*, *Porella arboris-vitae*, and
  *Jatropha ribifolia* as `(−)-α-gurjunene` biosynthetic or plant-mixture
  leads. Full-text review is still needed before any lead can be promoted to a
  producer assertion.

Correctly empty optional slots:

- No `resistance_mechanisms`: the record is ChEBI-only and CARD resistance
  routes do not apply.
- No `clinical_status` or `clinical_status_assertions`: the ChEBI-only source
  concept and inspected metadata do not assert regulatory use.
- No `datasets`: inspected ChEBI and PubMed metadata did not surface a public
  screening, omics, or structural dataset accession for exact
  `(−)-α-gurjunene`.

Ignored-inclusive absence search:

- Ran `rg --hidden --no-ignore` over `curation/`, `data/raw/`,
  `data/antibiotics/`, `reports/yaml_record_review/`, the full exported
  worklist and review queue under `/tmp/`, and `.git` for `CHEBI:61699`,
  `α-gurjunene`, `alpha-gurjunene`, `SPCXZDDGSGTVAW`, `489-40-7`, `C19734`,
  `CPD-12891`, and `1939514`.
- The search included ignored files and found only the expected generated
  target, `PATHS.tsv`, ChEBI raw row, exported worklist and review-queue rows,
  the maintained review-queue row, and the current branch name in `.git`. It
  found no prior exact `CHEBI:61699` review report,
  `curation/decisions.tsv` row, curated mechanism decision, or curated
  activity/provenance addition for this exact ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | GURJUNENE-61699-M1 | The record is still a seeded exact-enantiomer stub with a ChEBI-derived antibacterial role but no curator-owned isolated-compound activity spectrum, producer assertion, mode of action, mechanism scope, molecular target, or causal graph. | `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` reports `MECHANISM_REVIEW: mechanism is absent` with four source literature leads, zero record evidence items, and zero targets; `/tmp/antibioticmech-worklist.tsv` lists `CHEBI:61699` on `mechanism`, `producer-candidate`, and `review-readiness`. ChEBI and the 27-PMID bounded PubMed search surfaced essential-oil, extract, volatile-fraction, and synthase leads, but no exact isolated-compound MIC or mechanism claim has been curated onto the record. | `data/antibiotics/antibacterial/α-gurjunene.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`; or `curation/decisions.tsv` if full-text inspection cannot verify exact `(−)-α-gurjunene` antibacterial activity. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the full text behind the ChEBI-linked sources and the bounded
   exact-gurjunene antibacterial search to determine whether any paper assays
   isolated exact `(−)-α-gurjunene`, rather than a plant essential oil, extract,
   or volatile fraction that only contains gurjunene.
2. Add claim-local `activity_spectrum` observations only if an inspected source
   reports isolated exact `(−)-α-gurjunene` against a bacterial taxon with a
   usable assay, value, qualifier, and unit; do not generalize
   essential-oil-level, extract-level, or related-enantiomer activity onto exact
   `CHEBI:61699`.
3. Curate `mode_of_action`, `mode_of_action_target_scope`,
   `mode_of_action_notes`, molecular targets, and a causal graph only to the
   precision directly supported by inspected exact-compound mechanism sources.
4. Add a `producer_organisms` assertion with claim-local evidence if a source
   verifies biosynthesis or isolation of exact `(−)-α-gurjunene` in a named
   plant species, keeping synthase evidence from *Solidago canadensis* separate
   from essential-oil mixture evidence from other plants.
5. If exact `(−)-α-gurjunene` antibacterial activity cannot be verified, leave
   the record `SEEDED` and add either a curator discussion for the ChEBI-derived
   role or a source-concept decision in `curation/decisions.tsv` if the ChEBI
   antibacterial role is clearly unsupported.
6. Preserve the seeded ChEBI identity, stereospecific structure, parent, xrefs,
   source PMIDs, and source concept. This review found no grounded-identity
   correction that belongs in `data/raw/chebi_antimicrobials.tsv` or
   `data/antibiotics/PATHS.tsv`.

## Follow-up Checks

- `just validate-strict data/antibiotics/antibacterial/α-gurjunene.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-alpha-gurjunene.tsv`
- `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue-alpha-gurjunene.tsv`
- `just qc`
- Manual diff review of `data/antibiotics/antibacterial/α-gurjunene.yaml` and
  `curation/decisions.tsv` to confirm every new exact-structure claim is
  claim-local and directly supported by an inspected primary source.

## Additional Notes

- `NCBI_EMAIL` was unset in the local environment before direct PubMed
  E-Utilities fetches; no contact email was sent as NCBI API metadata.
- The first ChEBI OLS and PubMed requests failed because the sandbox could not
  resolve `www.ebi.ac.uk` or `eutils.ncbi.nlm.nih.gov`; rerunning the same
  bounded requests outside the sandboxed network path succeeded.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded finding above.
