# YAML Record Review: (+)-phytocassane D

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antifungal/phytocassane-d.yaml`
- Started UTC: 2026-09-21T14:36:00Z
- Finished UTC: 2026-09-21T14:37:58Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:72669` |
| Label | `(+)-phytocassane D` |
| Path | `data/antibiotics/antifungal/phytocassane-d.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:72669` / `(+)-phytocassane D` |
| Minted source key | `antibioticmech:chebi-9739abf91a` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, structure, class, role, synonym, or xref changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:21` is the next unreported queue row and
  names `CHEBI:72669`, label `(+)-phytocassane D`, and the review hint
  `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:2120` maps `CHEBI:72669` to the `ANTIFUNGAL`
  directory and `phytocassane-d` slug.
- `data/raw/chebi_antimicrobials.tsv:1860` is the ChEBI source row that seeds
  the target record.
- The whole target YAML was read before judging generated identity, structure,
  source concept, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/phytocassane-d.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/phytocassane-d.yaml --out /tmp/antibioticmech-phytocassane-d-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2939 expected records, 2939 on disk, no missing, unexpected, or drifted records, no identifiers absent from `PATHS.tsv`, and no stale lockfile rows. |
| `just review-queue --limit 22` | Passed and confirmed `CHEBI:72669` appears in the review-readiness queue as `MECHANISM_REVIEW`. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-phytocassane-d.tsv` | Passed; `CHEBI:72669` appears in `mechanism` and `review-readiness`. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and PATHS
inputs.

## Identity and Grounding

The seeded identity is consistent with the authoritative ChEBI record:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:72669`, `(+)-phytocassane D` | Official ChEBI resolved `CHEBI:72669` to `(+)-phytocassane D`. |
| Definition | A phytocassane that is `(+)-phytocassane A` with the position-2 hydroxy oxidised to a ketone and the position-3 keto reduced to a 3-alpha hydroxy group | Matched ChEBI. |
| Formula and charge | `C20H28O3`, charge `0` | Matched ChEBI. |
| Masses | average `316.441`, monoisotopic `316.20384` | Matched ChEBI. |
| SMILES | `[H][C@@]12C(=O)C=C(C=C)[C@@H](C)[C@@]1([H])CC[C@]1([H])C(C)(C)[C@H](O)C(=O)C[C@@]21C` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C20H28O3/c1-6-12-9-14(21)17-13(11(12)2)7-8-16-19(3,4)18(23)15(22)10-20(16,17)5/h6,9,11,13,16-18,23H,1,7-8,10H2,2-5H3/t11-,13-,16-,17+,18-,20-/m1/s1` | Matched ChEBI. |
| InChIKey | `DGUIKAVSMBLZCL-MKSLXUROSA-N` | Matched ChEBI. |
| Antifungal role | `CHEBI:35718` | ChEBI asserts `has role` to `antifungal agent`. |
| Parent compounds | `CHEBI:139395`, `CHEBI:2468`, `CHEBI:46640` | ChEBI asserts `is a` edges to phytocassane, secondary alpha-hydroxy ketone, and diketone. |
| Xrefs | none | Matched the official ChEBI page, which has no manual xrefs or registry numbers for this concept. |

The record correctly preserves the exact ChEBI source concept, the IUPAC name,
and five ChEBI synonyms:

- `3α-hydroxy-14β-methyl-13-vinyl-5β,8α,9β,10α-podocarp-12-ene-2,11-dione`
- `(2S,4aR,4bR,8S,8aR,10aS)-2-hydroxy-1,1,4a,8-tetramethyl-7-vinyl-1,4a,4b,8,8a,9,10,10a-octahydrophenanthrene-3,5(2H,4H)-dione`
- `(2S,4aR,4bR,8S,8aR,10aS)-7-ethenyl-2-hydroxy-1,1,4a,8-tetramethyl-1,4a,4b,8,8a,9,10,10a-octahydrophenanthrene-3,5(2H,4H)-dione`
- `(3α,5β,8α,9β,10α,14β)-3-hydroxy-14-methyl-13-vinylpodocarp-12-ene-2,11-dione`
- `phytocassane D`

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

The ChEBI raw row carries no PMID leads for exact `CHEBI:72669`. Targeted
publication searches resolved only candidate literature leads rather than
record-ready mechanism claims:

| Search | Result |
|---|---|
| Exact `(+)-phytocassane D` PubMed search | Returned 4 PubMed candidates. The inspected abstracts mention rice phytoalexin variation, elicitor-induced phytocassane D accumulation, phytocassane-family biosynthesis, or off-target phytocassane A modeling leads, but did not supply an exact microbial mode of action or molecular target for `(+)-phytocassane D`. |
| `"phytocassane D" "Magnaporthe"` PubMed search | Returned 0 PubMed candidates. |
| InChIKey search for `DGUIKAVSMBLZCL-MKSLXUROSA-N` | Returned 0 PubMed candidates. |
| Combined PubMed search for `"Phytocassanes A, B, C and D"` or `"phytocassane D"` | Returned 4 PubMed candidates, overlapping the exact-name candidate set and not adding a curatable exact mechanism claim. |

## Completeness

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`,
  `molecular_targets`, and `causal_graphs` are absent, so the record has no
  curator-owned antifungal mechanism.
- No `activity_spectrum` entry captures the exact fungal organism, strain,
  method, value, qualifier, units, and per-observation evidence for any
  phytocassane D activity lead.
- No `producer_organisms` entry captures a source-organism lead. The broader
  `phytocassane` class has a MIBiG row for `BGC0000672`, but it is not an
  exact `CHEBI:72669` import path: the raw MIBiG row has a different
  stereochemistry layer in the InChIKey, is attached to the structureless
  `phytocassane` class, is flagged questionable, and correctly leaves the exact
  phytocassane D record off the `producer-candidate` worklist.

Correctly empty optional slots:

- No `xrefs`: the ChEBI source row and official ChEBI page do not assert any
  manual xref or registry number for exact `CHEBI:72669`.
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
  and the full exported worklist for `CHEBI:72669`,
  `(+)-phytocassane D`, `phytocassane-d`, `phytocassane`,
  `DGUIKAVSMBLZCL`, and `BGC0000672`.
- The search included ignored files and found only the expected generated
  target, `PATHS.tsv`, ChEBI raw row, adjacent phytocassane records, worklist
  rows, review-queue rows, the existing adjacent phytocassane A/B/C reports,
  and a raw MIBiG row for the broader `phytocassane` producer lead. It found
  no prior review report, `curation/decisions.tsv` row, or curated mechanism
  decision for this exact ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | PHYT-D-M1 | The record is still a seeded compound stub with no curator-owned activity spectrum, mode of action, mechanism scope, molecular target, or causal graph. | `just review-queue --limit 22` reports `MECHANISM_REVIEW: mechanism is absent`; `/tmp/antibioticmech-worklist-phytocassane-d.tsv` lists `CHEBI:72669` on `mechanism` and `review-readiness`. Exact-name and targeted PubMed searches returned phytocassane-family biosynthesis and pathogen-response leads for phytocassane D, but no existing claim from those sources has been curated onto the record. | `data/antibiotics/antifungal/phytocassane-d.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the full text of the primary phytocassane isolation and activity
   paper behind the broader ChEBI phytocassane reference set, especially
   `PMID:12784637`, to determine whether exact phytocassane D antifungal assay
   observations can be curated with method, fungal organism, strain, value,
   unit, and claim-local evidence.
2. Curate `mode_of_action`, `mode_of_action_target_scope`,
   `mode_of_action_notes`, molecular targets, and causal graph only to the
   precision directly supported by inspected primary activity or mechanistic
   evidence. Leave these fields blank if the literature reports activity
   without a mechanism.
3. Inspect the `BGC0000672` rice phytocassane biosynthesis lead before deciding
   whether it supports a `producer_organisms` entry for exact `CHEBI:72669`.
   Do not promote the broader `phytocassane` MIBiG row into an exact
   phytocassane D biosynthetic producer claim without resolving the
   stereochemistry and compound-family scope.
4. Preserve the seeded ChEBI identity, structure, antifungal role, parent
   compounds, empty xrefs, and source concept. This review found no
   grounded-identity correction that belongs in `curation/decisions.tsv`,
   `data/raw/chebi_antimicrobials.tsv`, or `data/antibiotics/PATHS.tsv`.

## Follow-up Checks

- `just validate-strict data/antibiotics/antifungal/phytocassane-d.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-phytocassane-d.tsv`
- `just review-queue --limit 22`
- `just qc`
- Manual diff review of
  `data/antibiotics/antifungal/phytocassane-d.yaml` to confirm every new
  activity or mechanism claim is claim-local and directly supported by an
  inspected primary source.

## Additional Notes

- `NCBI_EMAIL` was unset in the local environment before using the PubMed
  search script; no contact email was sent as NCBI API metadata.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded finding above.
- The official ChEBI page was sufficient to verify that exact `CHEBI:72669` has
  no ChEBI-asserted HMDB, Reaxys, or other xref requiring independent public
  resolution.
