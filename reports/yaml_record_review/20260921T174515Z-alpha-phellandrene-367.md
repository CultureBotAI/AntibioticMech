# YAML Record Review: (+)-α-phellandrene

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/unspecified/α-phellandrene-367.yaml`
- Started UTC: 2026-09-21T17:42:00Z
- Finished UTC: 2026-09-21T17:45:15Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:367` |
| Label | `(+)-α-phellandrene` |
| Path | `data/antibiotics/unspecified/α-phellandrene-367.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:367` / `(+)-α-phellandrene` |
| Minted source key | `antibioticmech:chebi-56560414a5` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, structure, class, role, synonym, or xref changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:27` names `CHEBI:367`, label
  `(+)-α-phellandrene`, and the review hint
  `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:938` maps `CHEBI:367` to the
  `ANTIMICROBIAL_UNSPECIFIED` directory and `α-phellandrene-367` slug.
- `data/raw/chebi_antimicrobials.tsv:8` is the ChEBI source row that seeds the
  target record.
- The whole 59-line target YAML was read before judging generated identity,
  structure, xrefs, source concept, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/α-phellandrene-367.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/α-phellandrene-367.yaml --out /tmp/antibioticmech-phellandrene-367-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2939 expected records, 2939 on disk, no missing, unexpected, or drifted records, no identifiers absent from `PATHS.tsv`, and no stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-phellandrene-367.tsv` | Passed; `CHEBI:367` appears in `mechanism` and `review-readiness`. |
| `just review-queue --limit 27` | Passed and confirmed `CHEBI:367` remains in the review-readiness queue as `MECHANISM_REVIEW`, with zero source literature leads, zero record evidence items, and zero targets. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and PATHS
inputs.

## Identity and Grounding

The seeded identity is consistent with the authoritative ChEBI and KEGG
records:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:367`, `(+)-α-phellandrene` | Official ChEBI resolved `CHEBI:367` to `(+)-α-phellandrene`, with ASCII name `(+)-alpha-phellandrene`. |
| Definition | The `(5S)` stereoisomer of `α-phellandrene` | Matched ChEBI. |
| Formula and charge | `C10H16`, charge `0` | Matched ChEBI and KEGG. |
| Masses | average `136.238`, monoisotopic `136.1252` | Matched ChEBI and KEGG exact mass `136.1252`. |
| SMILES | `[H][C@]1(C(C)C)C=CC(C)=CC1` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C10H16/c1-8(2)10-6-4-9(3)5-7-10/h4-6,8,10H,7H2,1-3H3/t10-/m0/s1` | Matched ChEBI. |
| InChIKey | `OGLDWXZKYODSOB-JTQLQIEISA-N` | Matched ChEBI. |
| Antimicrobial role | `CHEBI:33281` | ChEBI asserts `has role` to `antimicrobial agent`. |
| Parent compound | `CHEBI:50035` | ChEBI asserts `(+)-α-phellandrene is a α-phellandrene`. |
| Xrefs | `beilstein:3194394`, `cas:2243-33-6`, `kegg.compound:C11391`, `reaxys:5239644` | Matched the official ChEBI page; KEGG `C11391` names `(S)-(+)-alpha-Phellandrene` and cross-links back to `CHEBI:367` and CAS `2243-33-6`. |

The target is specifically the `(5S)/(+)` enantiomer, not the sibling
`CHEBI:301` / `(−)-α-phellandrene` record at
`data/antibiotics/unspecified/α-phellandrene.yaml` and not the
stereochemically-unspecified parent `CHEBI:50035` / `α-phellandrene` record at
`data/antibiotics/unspecified/α-phellandrene-50035.yaml`. Those three records
have different ChEBI identifiers, Standard InChIKeys, and xref sets.

ChEBI also asserts the non-antimicrobial `plant metabolite` role `CHEBI:76924`
and `volatile oil component` role `CHEBI:27311`. The seeded record correctly
retains only the ChEBI `antimicrobial agent` role that drives inclusion in this
repository, and this review found no identity evidence that the record should
move out of the `ANTIMICROBIAL_UNSPECIFIED` filing class.

## Evidence

The target record has no record-level `evidence`. That is allowed for a
ChEBI-seeded record because the ChEBI source concept supplies provenance, and
there are no `activity_spectrum`, `molecular_targets`,
`resistance_mechanisms`, `producer_organisms`, `clinical_status_assertions`,
`datasets`, or `causal_graphs` that would require claim-level evidence.

`data/raw/chebi_antimicrobials.tsv:8` carries no PubMed or DOI leads for the
exact `CHEBI:367` source concept. A PubMed query for exact
`(+)-α-phellandrene`, ASCII `(+)-alpha-phellandrene`,
`(S)-(+)-alpha-Phellandrene`, `OGLDWXZKYODSOB`, `2243-33-6`, or `C11391`
returned 20 candidates, but the inspected public abstract metadata did not
surface record-ready antimicrobial evidence for isolated exact
`(+)-α-phellandrene`:

| PMID | Public abstract support |
|---|---|
| `PMID:42684560` | Reports testing α-phellandrene individually as one volatile organic compound in *Colletotrichum gloeosporioides* growth and pathogenicity work, but the abstract highlights 6-pentyl-α-pyrone and 2-oxindole, not stereochemically exact `(+)-α-phellandrene`, as the functional inhibitory compounds. |
| `PMID:42624574` | Reports *Schinus terebinthifolia* residue essential oil whose major constituents include α-phellandrene and that inhibited *Colletotrichum musae*; the abstract does not map an isolated exact-enantiomer measurement to `CHEBI:367`. |
| `PMID:42627028` | Reports seasonal *Ageratina adenophora* oil and extract bioactivity correlations, but screens oil-borne α-terpinolene and α-cadinol rather than exact `(+)-α-phellandrene` as active dual-bioactivity compounds. |
| `PMID:42518439` | Reports *Beilschmiedia* essential-oil antifungal tests where an α-phellandrene-rich oil is one of several mixtures; the abstract explicitly reserves active-constituent isolation for additional work. |
| `PMID:42357405` | Reports antibacterial activity of *Senecio polyanthemoides* essential oils containing α-phellandrene; the abstract supports an oil-mixture lead, not isolated exact `CHEBI:367`. |
| `PMID:42280169` | Reports wild Croatian fennel oils in which α-phellandrene predominated in stem essential oil, while antimicrobial activity was limited to *Escherichia coli* and likely attributed to other constituents. |

Other returned candidates described plant, food, or insect olfaction volatile
profiles, docking in host olfactory systems, or non-antimicrobial essential-oil
effects.

## Completeness

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`,
  `molecular_targets`, and `causal_graphs` are absent, so the record has no
  curator-owned antimicrobial mechanism.
- No `activity_spectrum` entry captures an exact organism or strain, assay,
  value, qualifier, unit, and per-observation evidence for isolated exact
  `(+)-α-phellandrene`.
- No `producer_organisms` entry captures a strain- or species-scoped producer
  of exact `CHEBI:367`.

Correctly empty optional slots:

- No `resistance_mechanisms`: the record is ChEBI-only and CARD resistance
  routes do not apply.
- No `clinical_status` or `clinical_status_assertions`: the ChEBI-only source
  concept and inspected metadata do not assert regulatory use.
- No `datasets`: inspected ChEBI, KEGG, and PubMed metadata did not surface a
  public screening, omics, or structural dataset accession for this exact
  structure.

Ignored-inclusive absence search:

- Ran `rg --hidden --no-ignore` over `curation/`, `data/raw/`,
  `data/antibiotics/`, `reports/yaml_record_review/`, and the full exported
  worklist for `CHEBI:367`, `(+)-α-phellandrene`, `α-phellandrene-367`,
  `OGLDWXZKYODSOB-JTQLQIEISA-N`, `2243-33-6`, `C11391`, `5239644`, and
  `3194394`.
- The search included ignored files and found only the expected generated
  target, `PATHS.tsv`, ChEBI raw row, worklist rows, and the review-queue row.
  It found no prior review report, `curation/decisions.tsv` row, curated
  mechanism decision, or curated activity/provenance addition for this exact
  ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | PHELLANDRENE-367-M1 | The record is still a seeded exact-enantiomer stub with an antimicrobial ChEBI role but no curator-owned activity spectrum, mode of action, mechanism scope, molecular target, producer assertion, or causal graph. | `just review-queue --limit 27` reports `MECHANISM_REVIEW: mechanism is absent` with zero source literature leads, zero record evidence items, and zero targets; `/tmp/antibioticmech-worklist-phellandrene-367.tsv` lists `CHEBI:367` only in `mechanism` and `review-readiness`. The targeted PubMed search returned α-phellandrene mixture leads but no existing exact `(+)-α-phellandrene` activity or mechanism claim has been curated onto the record. | `data/antibiotics/unspecified/α-phellandrene-367.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`; or `curation/decisions.tsv` if exact `(+)-α-phellandrene` antimicrobial activity cannot be verified. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect full text behind the volatile-oil PubMed leads, starting with
   `PMID:42684560`, to determine whether any paper tested isolated
   `(+)-α-phellandrene`, racemic or unspecified α-phellandrene, an essential
   oil mixture, or another VOC as the actual active ingredient.
2. If exact `(+)-α-phellandrene` antimicrobial primary evidence is found, add
   claim-local `activity_spectrum` observations with organism, strain, assay,
   value, unit, and evidence; do not generalize essential-oil mixture activity
   onto the exact enantiomer.
3. Curate `mode_of_action`, `mode_of_action_target_scope`,
   `mode_of_action_notes`, molecular targets, and a causal graph only to the
   precision directly supported by inspected exact-compound mechanism sources.
4. If a biosynthesis or natural-product source names the exact
   `(+)-α-phellandrene` enantiomer and a plant species or strain, add a
   `producer_organisms` assertion with claim-local evidence.
5. If exact `(+)-α-phellandrene` antimicrobial activity cannot be verified,
   leave the record `SEEDED` and add either a curator discussion for the
   unsupported ChEBI role or a source-concept decision in
   `curation/decisions.tsv` if the ChEBI antimicrobial role is clearly
   over-scoped from stereochemically unspecified α-phellandrene or mixture
   assays.
6. Preserve the seeded ChEBI identity, `(5S)/(+)` structure, parent, xrefs, and
   source concept. This review found no grounded-identity correction that
   belongs in `data/raw/chebi_antimicrobials.tsv` or
   `data/antibiotics/PATHS.tsv`.

## Follow-up Checks

- `just validate-strict data/antibiotics/unspecified/α-phellandrene-367.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-phellandrene-367.tsv`
- `just review-queue --limit 27`
- `just qc`
- Manual diff review of
  `data/antibiotics/unspecified/α-phellandrene-367.yaml` and
  `curation/decisions.tsv` to confirm every exact-structure claim is
  claim-local and directly supported by an inspected primary source.

## Additional Notes

- `NCBI_EMAIL` was unset in the local environment before using the PubMed
  search script; no contact email was sent as NCBI API metadata.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded finding above.
- ChEBI and KEGG spell the same concept as `α-phellandrene` and
  `alpha-Phellandrene`; the seeded KEGG xref is still exact because KEGG
  `C11391` resolves to `(S)-(+)-alpha-Phellandrene` and cross-links back to
  `CHEBI:367`.
