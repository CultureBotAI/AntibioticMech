# YAML Record Review: (+)-phytocassane A

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antifungal/phytocassane-a.yaml`
- Started UTC: 2026-09-21T13:10:00Z
- Finished UTC: 2026-09-21T13:15:58Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:72664` |
| Label | `(+)-phytocassane A` |
| Path | `data/antibiotics/antifungal/phytocassane-a.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:72664` / `(+)-phytocassane A` |
| Minted source key | `antibioticmech:chebi-5e9cdedec9` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, structure, class, role, synonym, or xref changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:18` is the next unreported queue row and
  names `CHEBI:72664`, label `(+)-phytocassane A`, and the review hint
  `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:2117` maps `CHEBI:72664` to the `ANTIFUNGAL`
  directory and `phytocassane-a` slug.
- `data/raw/chebi_antimicrobials.tsv:1857` is the ChEBI source row that seeds
  the target record.
- The whole target YAML was read before judging generated identity, structure,
  source concept, xrefs, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/phytocassane-a.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/phytocassane-a.yaml --out /tmp/antibioticmech-phytocassane-a-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2939 expected records, 2939 on disk, no missing, unexpected, or drifted records, no identifiers absent from `PATHS.tsv`, and no stale lockfile rows. |
| `just review-queue --limit 19` | Passed and confirmed `CHEBI:72664` appears in the review-readiness queue as `MECHANISM_REVIEW`. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-phytocassane-a.tsv` | Passed; `CHEBI:72664` appears in `mechanism` and `review-readiness`. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and PATHS
inputs.

## Identity and Grounding

The seeded identity is consistent with the authoritative ChEBI record:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:72664`, `(+)-phytocassane A` | Official ChEBI resolved `CHEBI:72664` to `(+)-phytocassane A`. |
| Definition | A phytocassane that is `ent`-podocarp-12-ene-3,11-dione carrying hydroxy, vinyl, and methyl substituents at 2alpha, 13, and 14 | Matched ChEBI. |
| Formula and charge | `C20H28O3`, charge `0` | Matched ChEBI. |
| Masses | average `316.441`, monoisotopic `316.20384` | Matched ChEBI. |
| SMILES | `[H][C@@]12C(=O)C=C(C=C)[C@@H](C)[C@@]1([H])CC[C@]1([H])C(C)(C)C(=O)[C@H](O)C[C@@]21C` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C20H28O3/c1-6-12-9-14(21)17-13(11(12)2)7-8-16-19(3,4)18(23)15(22)10-20(16,17)5/h6,9,11,13,15-17,22H,1,7-8,10H2,2-5H3/t11-,13-,15-,16-,17+,20-/m1/s1` | Matched ChEBI. |
| InChIKey | `XVEOIKIXOSKAFL-BJASISCMSA-N` | Matched ChEBI. |
| Antifungal role | `CHEBI:35718` | ChEBI asserts `has role` to `antifungal agent`. |
| Parent compounds | `CHEBI:139395`, `CHEBI:2468`, `CHEBI:46640` | ChEBI asserts `is a` edges to phytocassane, secondary alpha-hydroxy ketone, and diketone. |
| Xrefs | `metacyc.compound:CPD-7094`, `reaxys:8509348` | Matched the official ChEBI page's MetaCyc manual xref and Reaxys registry number. |

The record correctly preserves the exact ChEBI source concept, the IUPAC name,
and four ChEBI synonyms:

- `2α-hydroxy-14β-methyl-13-vinyl-5β,8α,9β,10α-podocarp-12-ene-3,11-dione`
- `(2α,5β,8α,9β,10α,14β)-2-hydroxy-14-methyl-13-vinylpodocarp-12-ene-3,11-dione`
- `(3R,4aR,4bR,8S,8aR,10aS)-3-hydroxy-1,1,4a,8-tetramethyl-7-vinyl-1,3,4,4a,4b,8,8a,9,10,10a-decahydrophenanthrene-2,5-dione`
- `ent-2β-hydroxy-12,15-cassadiene-3,11-dione`
- `phytocassane A`

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

The ChEBI raw row carries no PMID leads for exact `CHEBI:72664`. Targeted
publication searches resolved only candidate literature leads rather than
record-ready mechanism claims:

| Search | Result |
|---|---|
| Exact `(+)-phytocassane A` PubMed search | Returned 8 PubMed candidates. The inspected abstracts mention phytocassane A in rice phytoalexin accumulation, host defense, and host-target in silico studies, but did not supply an exact microbial mode of action or molecular target for `(+)-phytocassane A`. |
| `"phytocassane A" "Magnaporthe"` PubMed search | Returned 2 PubMed candidates: `PMID:36212323`, which reports Hrip1-induced phytocassane A accumulation in rice leaves, and `PMID:25865436`, which compares the antifungal activity of a newly characterized phytocassane F to known phytocassane A. Neither public abstract reports phytocassane A MICs, units, an exact assay method, or a molecular target. |
| InChIKey search for `XVEOIKIXOSKAFL-BJASISCMSA-N` | Returned 0 PubMed candidates. |
| PubMed exact-title search for `"Phytocassanes A, B, C and D"` | Returned 0 candidates. |

The Semantic Scholar adapter returned HTTP 429 rate-limit errors during the
exact-name, antifungal, and InChIKey searches.

## Completeness

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`,
  `molecular_targets`, and `causal_graphs` are absent, so the record has no
  curator-owned antifungal mechanism.
- No `activity_spectrum` entry captures the exact fungal organism, strain,
  method, value, qualifier, units, and per-observation evidence for any
  phytocassane A activity lead.
- No `producer_organisms` entry captures a source-organism lead. The broader
  `phytocassane` class has a MIBiG row for `BGC0000672`, but it is not an
  exact `CHEBI:72664` import path: the raw MIBiG row has a different
  stereochemistry layer in the InChIKey, is attached to the structureless
  `phytocassane` class, is flagged questionable, and correctly leaves the exact
  phytocassane A record off the `producer-candidate` worklist.

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
  and the full exported worklist for `CHEBI:72664`,
  `(+)-phytocassane A`, `phytocassane-a`, `phytocassane`,
  `XVEOIKIXOSKAFL`, `CPD-7094`, and `10.1105/tpc.108.063677`.
- The search found only the expected generated target, `PATHS.tsv`, ChEBI raw
  row, adjacent phytocassane records, worklist rows, review-queue rows, and a
  raw MIBiG row for the broader `phytocassane` producer lead. It found no prior
  review report, `curation/decisions.tsv` row, or curated mechanism decision
  for this exact ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | PHYT-A-M1 | The record is still a seeded compound stub with no curator-owned activity spectrum, mode of action, mechanism scope, molecular target, or causal graph. | `just review-queue --limit 19` reports `MECHANISM_REVIEW: mechanism is absent`; `/tmp/antibioticmech-worklist-phytocassane-a.tsv` lists `CHEBI:72664` on `mechanism` and `review-readiness`. Exact-name and targeted PubMed searches returned organism- and pathogen-response leads for phytocassane A, but no existing claim from those sources has been curated onto the record. | `data/antibiotics/antifungal/phytocassane-a.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the full text of Horie et al. 2015, `PMID:25865436` / DOI
   `10.1021/acs.jafc.5b00785`, and any cited primary phytocassane A activity
   paper to determine whether exact antifungal assay observations can be
   curated with method, fungal organism, strain, value, unit, and
   claim-local evidence.
2. Curate `mode_of_action`, `mode_of_action_target_scope`,
   `mode_of_action_notes`, molecular targets, and causal graph only to the
   precision directly supported by inspected primary activity or mechanistic
   evidence. Leave these fields blank if the literature reports activity
   without a mechanism.
3. Inspect the `BGC0000672` rice phytocassane biosynthesis lead before deciding
   whether it supports a `producer_organisms` entry for exact `CHEBI:72664`.
   Do not promote the broader `phytocassane` MIBiG row into an exact
   phytocassane A biosynthetic producer claim without resolving the
   stereochemistry and compound-family scope.
4. Preserve the seeded ChEBI identity, structure, antifungal role, parent
   compounds, xrefs, and source concept. This review found no grounded-identity
   correction that belongs in `curation/decisions.tsv`,
   `data/raw/chebi_antimicrobials.tsv`, or `data/antibiotics/PATHS.tsv`.

## Follow-up Checks

- `just validate-strict data/antibiotics/antifungal/phytocassane-a.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-phytocassane-a.tsv`
- `just review-queue --limit 20`
- `just qc`
- Manual diff review of
  `data/antibiotics/antifungal/phytocassane-a.yaml` to confirm every new
  activity or mechanism claim is claim-local and directly supported by an
  inspected primary source.

## Additional Notes

- `NCBI_EMAIL` was unset in the local environment before using the PubMed
  search script; no contact email was sent as NCBI API metadata.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded finding above.
- A public BioRegistry resolution attempt for `metacyc.compound:CPD-7094`
  redirected but then hung before yielding an independently inspectable
  MetaCyc page; this review therefore treats `CPD-7094` only as a
  ChEBI-asserted manual xref. Reaxys is not publicly resolvable, so
  `reaxys:8509348` was likewise checked only against the official ChEBI page.
- The failed Semantic Scholar searches were rate-limit failures only. They did
  not affect identity validation because ChEBI supplied the needed exact
  checks.
