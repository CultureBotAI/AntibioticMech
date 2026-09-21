# YAML Record Review: (+)-phytocassane B

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antifungal/phytocassane-b.yaml`
- Started UTC: 2026-09-21T13:40:00Z
- Finished UTC: 2026-09-21T13:44:03Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:72666` |
| Label | `(+)-phytocassane B` |
| Path | `data/antibiotics/antifungal/phytocassane-b.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:72666` / `(+)-phytocassane B` |
| Minted source key | `antibioticmech:chebi-2739542c86` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, structure, class, role, synonym, or xref changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:19` is the next unreported queue row and
  names `CHEBI:72666`, label `(+)-phytocassane B`, and the review hint
  `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:2118` maps `CHEBI:72666` to the `ANTIFUNGAL`
  directory and `phytocassane-b` slug.
- `data/raw/chebi_antimicrobials.tsv:1858` is the ChEBI source row that seeds
  the target record.
- The whole target YAML was read before judging generated identity, structure,
  source concept, xrefs, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/phytocassane-b.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/phytocassane-b.yaml --out /tmp/antibioticmech-phytocassane-b-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2939 expected records, 2939 on disk, no missing, unexpected, or drifted records, no identifiers absent from `PATHS.tsv`, and no stale lockfile rows. |
| `just review-queue --limit 20` | Passed and confirmed `CHEBI:72666` appears in the review-readiness queue as `MECHANISM_REVIEW`. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-phytocassane-b.tsv` | Passed; `CHEBI:72666` appears in `mechanism` and `review-readiness`. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and PATHS
inputs.

## Identity and Grounding

The seeded identity is consistent with the authoritative ChEBI record:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:72666`, `(+)-phytocassane B` | Official ChEBI resolved `CHEBI:72666` to `(+)-phytocassane B`. |
| Definition | A phytocassane that is `(+)-phytocassane C` with an additional 2alpha hydroxy group | Matched ChEBI. |
| Formula and charge | `C20H30O4`, charge `0` | Matched ChEBI. |
| Masses | average `334.456`, monoisotopic `334.21441` | Matched ChEBI. |
| SMILES | `[H][C@@]12C(=O)C=C(C=C)[C@@H](C)[C@@]1([H])CC[C@]1([H])C(C)(C)[C@H](O)[C@H](O)[C@H](O)[C@@]21C` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C20H30O4/c1-6-11-9-13(21)15-12(10(11)2)7-8-14-19(3,4)17(23)16(22)18(24)20(14,15)5/h6,9-10,12,14-18,22-24H,1,7-8H2,2-5H3/t10-,12-,14-,15+,16+,17-,18+,20-/m1/s1` | Matched ChEBI. |
| InChIKey | `XFRCVLKGZMPUFQ-SUIMNPQMSA-N` | Matched ChEBI. |
| Antifungal role | `CHEBI:35718` | ChEBI asserts `has role` to `antifungal agent`. |
| Parent compounds | `CHEBI:139395`, `CHEBI:27136` | ChEBI asserts `is a` edges to phytocassane and triol. |
| Xrefs | `hmdb:HMDB0041055`, `reaxys:15793552` | Matched the official ChEBI page's HMDB manual xref and Reaxys registry number. |

The record correctly preserves the exact ChEBI source concept, the IUPAC name,
and five ChEBI synonyms:

- `1α,2α,3α-trihydroxy-14β-methyl-13-vinyl-5β,8α,9β,10α,14β-podocarp-12-en-11-one`
- `(1S,4aR,4bR,5R,6S,7S,8aR,10aR)-2-ethenyl-5,6,7-trihydroxy-1,4b,8,8-tetramethyl-4a,4b,5,6,7,8,8a,9,10,10a-decahydrophenanthren-4(1H)-one`
- `(1S,4aR,4bR,5R,6S,7S,8aR,10aR)-5,6,7-trihydroxy-1,4b,8,8-tetramethyl-2-vinyl-4a,4b,5,6,7,8,8a,9,10,10a-decahydrophenanthren-4(1H)-one`
- `(1α,2α,3α,5β,8α,9β,10α,14β)-1,2,3-trihydroxy-14-methyl-13-vinylpodocarp-12-en-11-one`
- `phytocassane B`

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

The ChEBI raw row carries no PMID leads for exact `CHEBI:72666`. Targeted
publication searches resolved only candidate literature leads rather than
record-ready mechanism claims:

| Search | Result |
|---|---|
| Exact `(+)-phytocassane B` PubMed search | Returned 15 PubMed candidates. The inspected abstracts mention phytocassane B in untargeted metabolomics, rice allelopathy, rice and wild-rice phytoalexin biosynthesis, and plant stress-response studies, but did not supply an exact microbial mode of action or molecular target for `(+)-phytocassane B`. |
| `"phytocassane B" "Magnaporthe"` PubMed search | Returned one PubMed candidate, `PMID:36212323`, which reports Hrip1-induced rice phytoalexin accumulation against *Magnaporthe oryzae* but mentions enhanced phytocassane A and G rather than an exact phytocassane B activity or target claim in the public abstract. |
| InChIKey search for `XFRCVLKGZMPUFQ-SUIMNPQMSA-N` | Returned 0 PubMed candidates. |
| Combined PubMed search for `"Phytocassanes A, B, C and D"`, `"phytocassane B"`, or `HMDB0041055` | Returned 15 PubMed candidates, overlapping the exact-name candidate set and not adding a curatable exact mechanism claim. |

The Semantic Scholar adapter returned HTTP 429 rate-limit errors during the
exact-name, antifungal, and InChIKey searches.

## Completeness

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`,
  `molecular_targets`, and `causal_graphs` are absent, so the record has no
  curator-owned antifungal mechanism.
- No `activity_spectrum` entry captures the exact fungal organism, strain,
  method, value, qualifier, units, and per-observation evidence for any
  phytocassane B activity lead.
- No `producer_organisms` entry captures a source-organism lead. The broader
  `phytocassane` class has a MIBiG row for `BGC0000672`, but it is not an
  exact `CHEBI:72666` import path: the raw MIBiG row has a different molecular
  formula, InChI, and InChIKey; is attached to the structureless
  `phytocassane` class; is flagged questionable; and correctly leaves the exact
  phytocassane B record off the `producer-candidate` worklist.

Correctly empty optional slots:

- No `resistance_mechanisms`: the record is ChEBI-only and CARD resistance
  routes do not apply to this plant phytoalexin.
- No `clinical_status` or `clinical_status_assertions`: the ChEBI-only source
  concept and inspected metadata do not assert regulatory use.
- No `datasets`: inspected ChEBI, PubMed metadata, and exact-name PubMed
  searches did not surface a public screening, omics, or structural dataset
  accession for this exact structure.

Ignored-inclusive absence search:

- Ran `rg --hidden --no-ignore` over `curation/`, `data/raw/`,
  `reports/yaml_record_review/`, the target YAML, `data/antibiotics/PATHS.tsv`,
  and the full exported worklist for `CHEBI:72666`,
  `(+)-phytocassane B`, `phytocassane-b`, `phytocassane`,
  `XFRCVLKGZMPUFQ`, `HMDB0041055`, `15793552`, and `BGC0000672`.
- The search included ignored files and found only the expected generated
  target, `PATHS.tsv`, ChEBI raw row, adjacent phytocassane records, worklist
  rows, review-queue rows, and a raw MIBiG row for the broader
  `phytocassane` producer lead. It found no prior review report,
  `curation/decisions.tsv` row, or curated mechanism decision for this exact
  ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | PHYT-B-M1 | The record is still a seeded compound stub with no curator-owned activity spectrum, mode of action, mechanism scope, molecular target, or causal graph. | `just review-queue --limit 20` reports `MECHANISM_REVIEW: mechanism is absent`; `/tmp/antibioticmech-worklist-phytocassane-b.tsv` lists `CHEBI:72666` on `mechanism` and `review-readiness`. Exact-name and targeted PubMed searches returned organism-, stress-response, and pathogen-response leads for phytocassane B, but no existing claim from those sources has been curated onto the record. | `data/antibiotics/antifungal/phytocassane-b.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the full text of the primary phytocassane isolation and activity
   paper behind the broader ChEBI phytocassane reference set, especially
   `PMID:12784637`, to determine whether exact phytocassane B antifungal assay
   observations can be curated with method, fungal organism, strain, value,
   unit, and claim-local evidence.
2. Curate `mode_of_action`, `mode_of_action_target_scope`,
   `mode_of_action_notes`, molecular targets, and causal graph only to the
   precision directly supported by inspected primary activity or mechanistic
   evidence. Leave these fields blank if the literature reports activity
   without a mechanism.
3. Inspect the `BGC0000672` rice phytocassane biosynthesis lead before deciding
   whether it supports a `producer_organisms` entry for exact `CHEBI:72666`.
   Do not promote the broader `phytocassane` MIBiG row into an exact
   phytocassane B biosynthetic producer claim without resolving the formula,
   stereochemistry, and compound-family scope.
4. Preserve the seeded ChEBI identity, structure, antifungal role, parent
   compounds, xrefs, and source concept. This review found no grounded-identity
   correction that belongs in `curation/decisions.tsv`,
   `data/raw/chebi_antimicrobials.tsv`, or `data/antibiotics/PATHS.tsv`.

## Follow-up Checks

- `just validate-strict data/antibiotics/antifungal/phytocassane-b.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-phytocassane-b.tsv`
- `just review-queue --limit 20`
- `just qc`
- Manual diff review of
  `data/antibiotics/antifungal/phytocassane-b.yaml` to confirm every new
  activity or mechanism claim is claim-local and directly supported by an
  inspected primary source.

## Additional Notes

- `NCBI_EMAIL` was unset in the local environment before using the PubMed
  search script; no contact email was sent as NCBI API metadata.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded finding above.
- Direct public HMDB and BioRegistry resolution attempts for `HMDB0041055`
  resolved to HMDB Cloudflare challenge pages, so this review treats
  `hmdb:HMDB0041055` only as a ChEBI-asserted manual xref. Reaxys is not
  publicly resolvable, so `reaxys:15793552` was likewise checked only against
  the official ChEBI page.
- The failed Semantic Scholar searches were rate-limit failures only. They did
  not affect identity validation because ChEBI supplied the needed exact
  concept, structure, role, parent, and xref metadata.
