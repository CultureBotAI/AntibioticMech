# YAML Record Review: (+)-pisiferic acid

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antibacterial/pisiferic-acid.yaml`
- Started UTC: 2026-09-21T15:39:39Z
- Finished UTC: 2026-09-21T15:39:39Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:70576` |
| Label | `(+)-pisiferic acid` |
| Path | `data/antibiotics/antibacterial/pisiferic-acid.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:70576` / `(+)-pisiferic acid` |
| Minted source key | `antibioticmech:chebi-8fda9e257e` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, structure, class, role, synonym, or xref changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:23` is the next unreported queue row and
  names `CHEBI:70576`, label `(+)-pisiferic acid`, source literature leads
  `PMID:20961093|PMID:26697686`, and the review hint
  `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:2062` maps `CHEBI:70576` to the `ANTIBACTERIAL`
  directory and `pisiferic-acid` slug.
- `data/raw/chebi_antimicrobials.tsv:1796` is the ChEBI source row that seeds
  the target record.
- The whole target YAML was read before judging generated identity, structure,
  xrefs, source concept, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/pisiferic-acid.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/pisiferic-acid.yaml --out /tmp/antibioticmech-pisiferic-acid-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2939 expected records, 2939 on disk, no missing, unexpected, or drifted records, no identifiers absent from `PATHS.tsv`, and no stale lockfile rows. |
| `just review-queue --limit 24` | Passed and confirmed `CHEBI:70576` appears in the review-readiness queue as `MECHANISM_REVIEW`, with two source literature leads. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-pisiferic-acid.tsv` | Passed; `CHEBI:70576` appears in `mechanism`, `producer-candidate`, and `review-readiness`. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and PATHS
inputs.

## Identity and Grounding

The seeded identity is consistent with the authoritative ChEBI record:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:70576`, `(+)-pisiferic acid` | Official ChEBI resolved `CHEBI:70576` to `(+)-pisiferic acid`. |
| Definition | An abietane diterpenoid that is abieta-8,11,13-trien-20-oic acid with a 12-hydroxy group, isolated from the stem bark of *Fraxinus sieboldiana* | Matched ChEBI. |
| Formula and charge | `C20H28O3`, charge `0` | Matched ChEBI. |
| Masses | average `316.441`, monoisotopic `316.20384` | Matched ChEBI and KEGG. |
| SMILES | `[H][C@@]12CCc3cc(C(C)C)c(O)cc3[C@@]1(C(=O)O)CCCC2(C)C` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C20H28O3/c1-12(2)14-10-13-6-7-17-19(3,4)8-5-9-20(17,18(22)23)15(13)11-16(14)21/h10-12,17,21H,5-9H2,1-4H3,(H,22,23)/t17-,20-/m0/s1` | Matched ChEBI. |
| InChIKey | `ATHWSPHADLLZSS-PXNSSMCTSA-N` | Matched ChEBI. |
| Antibacterial role | `CHEBI:33282` | ChEBI asserts `has role` to `antibacterial agent`. |
| Parent compounds | `CHEBI:25384`, `CHEBI:33853`, `CHEBI:36762`, `CHEBI:79084` | ChEBI asserts `is a` edges to monocarboxylic acid, phenols, abietane diterpenoid, and tricyclic diterpenoid. |
| Conjugate base relation | absent from `parent_compounds` | ChEBI asserts `(+)-pisiferic acid is conjugate acid of CHEBI:167487`; the record correctly omits that non-`is a` relation from the strictly broader parent list. |
| Xrefs | `cas:67494-15-9`, `kegg.compound:C09163`, `knapsack:C00003470`, `reaxys:6893431` | Matched the official ChEBI page. KEGG `C09163` also resolves to `Pisiferic acid` and cross-links ChEBI `70576`, CAS `67494-15-9`, and KNApSAcK `C00003470`. |

The record correctly preserves the exact ChEBI source concept, the IUPAC name,
and the ChEBI/ChemIDplus synonym:

- `12-hydroxyabieta-8,11,13-trien-20-oic acid`
- `pisiferic acid`

ChEBI also asserts the non-antimicrobial biological role `plant metabolite` /
`CHEBI:76924` and the chemical role `Bronsted acid` / `CHEBI:39141`. The
seeded record retains the ChEBI `antibacterial agent` antimicrobial role that
drives inclusion in this repository, and this review found no evidence that the
filing class should move out of `ANTIBACTERIAL`.

## Evidence

The target record has no record-level `evidence`. That is allowed for a
ChEBI-seeded record because the ChEBI source concept supplies provenance, and
there are no `activity_spectrum`, `molecular_targets`,
`resistance_mechanisms`, `producer_organisms`, `clinical_status_assertions`,
`datasets`, or `causal_graphs` that would require claim-level evidence.

The ChEBI raw row carries two PMID leads. Direct PMID searches resolved both
lead papers:

| PMID | Public abstract support |
|---|---|
| `PMID:20961093` | Reports isolation of abietane and C20-norabietane diterpenes from *Fraxinus sieboldiana* stem bark and several non-bacterial bioactivities, including anti-inflammatory, anti-H5N1, and cytotoxicity readouts for numbered compounds. It does not identify an antibacterial assay, MIC, molecular target, or exact mode of action for `(+)-pisiferic acid` in the public abstract. |
| `PMID:26697686` | Reports isolation and structure elucidation of 50 known compounds from an ethanol extract of *Fraxinus sieboldiana* branch, including `(+)-pisiferic acid`, but does not report an antibacterial assay or mechanism in the public abstract. |

Targeted publication searches resolved candidate literature leads rather than
record-ready mechanism claims:

| Search | Result |
|---|---|
| Exact PubMed search for `(+)-pisiferic acid`, `pisiferic acid`, or `ATHWSPHADLLZSS` | Returned 14 PubMed candidates. The inspected abstracts mention plant isolation, pisiferic-acid synthesis chemistry, human Kv1.1/Kv1.2 rescue, human-cell cytotoxicity, adipogenesis, and non-exact derivatives such as `O-methyl pisiferic acid`, but did not surface an exact antibacterial mode of action or molecular target claim ready to curate. |
| PubMed search for `20961093`, `26697686`, or `pisiferic acid antibacterial` | Returned three broad candidates that did not include the two ChEBI PMID leads; the hits concerned in-silico *Pseudomonas aeruginosa* anti-biofilm screening, carnosic acid/carnosol synthesized from pisiferic acid, and `O-methyl pisiferic acid` chitin synthase inhibition. Direct PMID queries resolved the two ChEBI leads separately. |

## Completeness

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`,
  `molecular_targets`, and `causal_graphs` are absent, so the record has no
  curator-owned antibacterial mechanism.
- No `activity_spectrum` entry captures the exact bacterial organism, strain,
  method, value, qualifier, units, and per-observation evidence for any exact
  pisiferic-acid activity lead.
- No `producer_organisms` entry captures a source-organism lead. ChEBI and
  `PMID:20961093` support *Fraxinus sieboldiana* stem bark as an isolation
  source, and the full worklist lists this as `producer-candidate`; that row
  is explicitly guarded as `SOURCE only — may not be the producer`, so it
  still needs curator inspection before becoming a biosynthetic producer
  assertion.

Correctly empty optional slots:

- No `resistance_mechanisms`: the record is ChEBI-only and CARD resistance
  routes do not apply to this plant diterpenoid.
- No `clinical_status` or `clinical_status_assertions`: the ChEBI-only source
  concept and inspected metadata do not assert regulatory use.
- No `datasets`: inspected ChEBI, PubMed metadata, KEGG, and exact-name PubMed
  searches did not surface a public screening, omics, or structural dataset
  accession for this exact structure.

Ignored-inclusive absence search:

- Ran `rg --hidden --no-ignore` over `curation/`, `data/raw/`,
  `data/antibiotics/`, `reports/yaml_record_review/`, and the full exported
  worklist for `CHEBI:70576`, `(+)-pisiferic acid`, `pisiferic-acid`,
  `pisiferic_acid`, `pisiferic acid`, `ATHWSPHADLLZSS`, `67494-15-9`,
  `C09163`, `C00003470`, `6893431`, `PMID:20961093`, and `PMID:26697686`.
- The search included ignored files and found only the expected generated
  target, `PATHS.tsv`, ChEBI raw row, worklist rows, and review-queue row. It
  found no prior review report, `curation/decisions.tsv` row, curated
  mechanism decision, or curated activity/provenance addition for this exact
  ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | PIS-M1 | The record is still a seeded compound stub with source literature leads but no curator-owned activity spectrum, producer assertion, mode of action, mechanism scope, molecular target, or causal graph. | `just review-queue --limit 24` reports `MECHANISM_REVIEW: mechanism is absent` with `PMID:20961093` and `PMID:26697686` as uncurated source literature leads; `/tmp/antibioticmech-worklist-pisiferic-acid.tsv` lists `CHEBI:70576` on `mechanism`, `producer-candidate`, and `review-readiness`. Exact-name and direct-PMID PubMed searches returned plant-isolation and bioactivity leads, but no existing claim from those sources has been curated onto the record. | `data/antibiotics/antibacterial/pisiferic-acid.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the full text of `PMID:20961093` and the primary antibacterial
   paper behind ChEBI's `antibacterial agent` role to determine whether exact
   pisiferic-acid antibacterial assay observations can be curated with method,
   bacterial organism, strain, value, unit, and claim-local evidence.
2. Inspect `PMID:20961093`, `PMID:26697686`, and the *Fraxinus sieboldiana*
   extraction context before deciding whether the stem or stem-bark isolation
   lead supports a `producer_organisms` entry for exact `CHEBI:70576`.
3. Curate `mode_of_action`, `mode_of_action_target_scope`,
   `mode_of_action_notes`, molecular targets, and causal graph only to the
   precision directly supported by inspected primary antibacterial or
   mechanistic evidence. Leave these fields blank if the literature reports
   activity without a mechanism.
4. Preserve the seeded ChEBI identity, structure, antibacterial role, xrefs,
   parent compounds, and source concept. This review found no grounded-identity
   correction that belongs in `curation/decisions.tsv`,
   `data/raw/chebi_antimicrobials.tsv`, or `data/antibiotics/PATHS.tsv`.

## Follow-up Checks

- `just validate-strict data/antibiotics/antibacterial/pisiferic-acid.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-pisiferic-acid.tsv`
- `just review-queue --limit 24`
- `just qc`
- Manual diff review of
  `data/antibiotics/antibacterial/pisiferic-acid.yaml` to confirm every new
  activity, producer, or mechanism claim is claim-local and directly supported
  by an inspected primary source.

## Additional Notes

- `NCBI_EMAIL` was unset in the local environment before using the PubMed
  search script; no contact email was sent as NCBI API metadata.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded finding above.
- The direct KEGG check confirmed the `kegg.compound:C09163` xref and
  cross-links to ChEBI, CAS, and KNApSAcK. The KNApSAcK and Reaxys xrefs were
  verified as ChEBI manual xrefs but were not independently resolved.
