# YAML Record Review: (+)-phytocassane E

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antifungal/phytocassane-e.yaml`
- Started UTC: 2026-09-21T15:06:43Z
- Finished UTC: 2026-09-21T15:07:30Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:72675` |
| Label | `(+)-phytocassane E` |
| Path | `data/antibiotics/antifungal/phytocassane-e.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:72675` / `(+)-phytocassane E` |
| Minted source key | `antibioticmech:chebi-0d5ac1a090` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, structure, class, role, synonym, or xref changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:22` is the next unreported queue row and
  names `CHEBI:72675`, label `(+)-phytocassane E`, and the review hint
  `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:2121` maps `CHEBI:72675` to the `ANTIFUNGAL`
  directory and `phytocassane-e` slug.
- `data/raw/chebi_antimicrobials.tsv:1861` is the ChEBI source row that seeds
  the target record.
- The whole target YAML was read before judging generated identity, structure,
  source concept, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/phytocassane-e.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/phytocassane-e.yaml --out /tmp/antibioticmech-phytocassane-e-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2939 expected records, 2939 on disk, no missing, unexpected, or drifted records, no identifiers absent from `PATHS.tsv`, and no stale lockfile rows. |
| `just review-queue --limit 23` | Passed and confirmed `CHEBI:72675` appears in the review-readiness queue as `MECHANISM_REVIEW`. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-phytocassane-e.tsv` | Passed; `CHEBI:72675` appears in `mechanism` and `review-readiness`. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and PATHS
inputs.

## Identity and Grounding

The seeded identity is consistent with the authoritative ChEBI record:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:72675`, `(+)-phytocassane E` | Official ChEBI resolved `CHEBI:72675` to `(+)-phytocassane E`. |
| Definition | A phytocassane that is `(+)-phytocassane C` with the position-3 hydroxy oxidised to the corresponding ketone | Matched ChEBI. |
| Formula and charge | `C20H28O3`, charge `0` | Matched ChEBI. |
| Masses | average `316.441`, monoisotopic `316.20384` | Matched ChEBI. |
| SMILES | `[H][C@@]12C(=O)C=C(C=C)[C@@H](C)[C@@]1([H])CC[C@]1([H])C(C)(C)C(=O)C[C@H](O)[C@@]21C` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C20H28O3/c1-6-12-9-14(21)18-13(11(12)2)7-8-15-19(3,4)16(22)10-17(23)20(15,18)5/h6,9,11,13,15,17-18,23H,1,7-8,10H2,2-5H3/t11-,13-,15-,17+,18+,20+/m1/s1` | Matched ChEBI. |
| InChIKey | `MMRGGLJWHXYKLZ-NEYRYYQWSA-N` | Matched ChEBI. |
| Antifungal role | `CHEBI:35718` | ChEBI asserts `has role` to `antifungal agent`. |
| Parent compounds | `CHEBI:139395`, `CHEBI:46640` | ChEBI asserts `is a` edges to phytocassane and diketone. |
| Xrefs | none | Matched the official ChEBI page, which has no manual xrefs or registry numbers for this concept. |

The record correctly preserves the exact ChEBI source concept, the IUPAC name,
and six ChEBI synonyms:

- `1α-hydroxy-14β-methyl-13-vinyl-5β,8α,9β,10α-podocarp-12-ene-3,11-dione`
- `(1α,5β,8α,9β,10α,14β)-1-hydroxy-14-methyl-13-vinylpodocarp-12-ene-3,11-dione`
- `(4S,4aR,4bR,8S,8aR,10aS)-4-hydroxy-1,1,4a,8-tetramethyl-7-vinyl-1,3,4,4a,4b,8,8a,9,10,10a-decahydrophenanthrene-2,5-dione`
- `(4S,4aR,4bR,8S,8aR,10aS)-7-ethenyl-4-hydroxy-1,1,4a,8-tetramethyl-1,3,4,4a,4b,8,8a,9,10,10a-decahydrophenanthrene-2,5-dione`
- `ent-1β-hydroxy-12,15-cassadiene-3,11-dione`
- `phytocassane E`

ChEBI also asserts the non-antimicrobial biological roles `phytoalexin` /
`CHEBI:26115` and `plant metabolite` / `CHEBI:76924`. The seeded record retains
the ChEBI `antifungal agent` antimicrobial role that drives inclusion in this
repository, and this review found no evidence that the filing class should move
out of `ANTIFUNGAL`.

## Evidence

The target record has no record-level `evidence`. That is allowed for a
ChEBI-seeded record because the ChEBI source concept supplies provenance, and
there are no `activity_spectrum`, `molecular_targets`,
`resistance_mechanisms`, `producer_organisms`, `clinical_status_assertions`,
`datasets`, or `causal_graphs` that would require claim-level evidence.

The ChEBI raw row carries no PMID leads for exact `CHEBI:72675`. Targeted
publication searches resolved only candidate literature leads rather than
record-ready mechanism claims:

| Search | Result |
|---|---|
| Exact `(+)-phytocassane E` PubMed search | Returned 11 PubMed candidates. The inspected abstracts mention MOS-triggered phytocassane E accumulation, phytocassane A-E biosynthesis, root exudation, and blast-induced phytocassane-family accumulation, but did not supply an exact microbial mode of action or molecular target for `(+)-phytocassane E`. |
| `"phytocassane E" "Magnaporthe"` PubMed search | Returned one PubMed candidate, `PMID:12784637`, which reports phytocassanes A through E in rice blast lesions but does not report an exact phytocassane E MIC, assay method, or molecular target in the public abstract. |
| InChIKey search for `MMRGGLJWHXYKLZ-NEYRYYQWSA-N` | Returned 0 PubMed candidates. |
| Combined PubMed search for `"phytocassane E"`, `"Phytocassanes A, B, C and D"`, or `phytocassanes` | Returned 20 PubMed candidates, overlapping exact-name phytocassane E leads plus broader rice phytoalexin biosynthesis, plant-defense, metabolomics, and off-target in-silico phytocassane A leads. It did not add a curatable exact mechanism claim. |

## Completeness

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`,
  `molecular_targets`, and `causal_graphs` are absent, so the record has no
  curator-owned antifungal mechanism.
- No `activity_spectrum` entry captures the exact fungal organism, strain,
  method, value, qualifier, units, and per-observation evidence for any
  phytocassane E activity lead.
- No `producer_organisms` entry captures a source-organism lead. The broader
  `phytocassane` class has a MIBiG row for `BGC0000672`, but it is not an
  exact `CHEBI:72675` import path: the raw MIBiG row has a different first
  InChIKey block, is attached to the structureless `phytocassane` class, is
  flagged questionable, and correctly leaves the exact phytocassane E record
  off the `producer-candidate` worklist.

Correctly empty optional slots:

- No `xrefs`: the ChEBI source row and official ChEBI page do not assert any
  manual xref or registry number for exact `CHEBI:72675`.
- No `resistance_mechanisms`: the record is ChEBI-only and CARD resistance
  routes do not apply to this plant phytoalexin.
- No `clinical_status` or `clinical_status_assertions`: the ChEBI-only source
  concept and inspected metadata do not assert regulatory use.
- No `datasets`: inspected ChEBI, PubMed metadata, and exact-name PubMed
  searches did not surface a public screening, omics, or structural dataset
  accession for this exact structure.

Ignored-inclusive absence search:

- Ran `rg --hidden --no-ignore` over `curation/`, `data/raw/`,
  `data/antibiotics/antifungal/`, `data/antibiotics/PATHS.tsv`,
  `reports/yaml_record_review/`, and the full exported worklist for
  `CHEBI:72675`, `(+)-phytocassane E`, `phytocassane-e`,
  `phytocassane E`, `MMRGGLJWHXYKLZ`, and `BGC0000672`.
- The search included ignored files and found only the expected generated
  target, `PATHS.tsv`, ChEBI raw row, worklist rows, review-queue row, the
  existing adjacent phytocassane A/B/C/D reports, and raw MIBiG rows for the
  broader `phytocassane` producer lead. It found no prior review report,
  `curation/decisions.tsv` row, or curated mechanism decision for this exact
  ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | PHYT-E-M1 | The record is still a seeded compound stub with no curator-owned activity spectrum, mode of action, mechanism scope, molecular target, or causal graph. | `just review-queue --limit 23` reports `MECHANISM_REVIEW: mechanism is absent`; `/tmp/antibioticmech-worklist-phytocassane-e.tsv` lists `CHEBI:72675` on `mechanism` and `review-readiness`. Exact-name and targeted PubMed searches returned phytocassane-family biosynthesis and pathogen-response leads for phytocassane E, but no existing claim from those sources has been curated onto the record. | `data/antibiotics/antifungal/phytocassane-e.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the full text of the primary phytocassane isolation and activity
   paper behind the broader ChEBI phytocassane reference set, especially
   `PMID:12784637`, to determine whether exact phytocassane E antifungal assay
   observations can be curated with method, fungal organism, strain, value,
   unit, and claim-local evidence.
2. Curate `mode_of_action`, `mode_of_action_target_scope`,
   `mode_of_action_notes`, molecular targets, and causal graph only to the
   precision directly supported by inspected primary activity or mechanistic
   evidence. Leave these fields blank if the literature reports activity
   without a mechanism.
3. Inspect the `BGC0000672` rice phytocassane biosynthesis lead before deciding
   whether it supports a `producer_organisms` entry for exact `CHEBI:72675`.
   Do not promote the broader `phytocassane` MIBiG row into an exact
   phytocassane E biosynthetic producer claim without resolving the
   stereochemistry and compound-family scope.
4. Preserve the seeded ChEBI identity, structure, antifungal role, parent
   compounds, empty xrefs, and source concept. This review found no
   grounded-identity correction that belongs in `curation/decisions.tsv`,
   `data/raw/chebi_antimicrobials.tsv`, or `data/antibiotics/PATHS.tsv`.

## Follow-up Checks

- `just validate-strict data/antibiotics/antifungal/phytocassane-e.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-phytocassane-e.tsv`
- `just review-queue --limit 23`
- `just qc`
- Manual diff review of
  `data/antibiotics/antifungal/phytocassane-e.yaml` to confirm every new
  activity or mechanism claim is claim-local and directly supported by an
  inspected primary source.

## Additional Notes

- `NCBI_EMAIL` was unset in the local environment before using the PubMed
  search script; no contact email was sent as NCBI API metadata.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded finding above.
- The official ChEBI page was sufficient to verify that exact `CHEBI:72675` has
  no ChEBI-asserted HMDB, Reaxys, or other xref requiring independent public
  resolution.
