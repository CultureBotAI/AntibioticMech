# YAML Record Review: (+)-microdiplodiasone

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antibacterial/microdiplodiasone.yaml`
- Started UTC: 2026-09-21T12:06:30Z
- Finished UTC: 2026-09-21T12:11:19Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:68284` |
| Label | `(+)-microdiplodiasone` |
| Path | `data/antibiotics/antibacterial/microdiplodiasone.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:68284` / `(+)-microdiplodiasone` |
| Minted source key | `antibioticmech:chebi-5c8a6fb66d` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, structure, class, role, or synonym changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:16` is the next unreported queue row and
  names `CHEBI:68284`, label `(+)-microdiplodiasone`, and the review hint
  `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:1959` maps `CHEBI:68284` to the
  `ANTIBACTERIAL` directory and `microdiplodiasone` slug.
- `data/raw/chebi_antimicrobials.tsv:1699` is the ChEBI source row that seeds
  the target record.
- The whole target YAML was read before judging generated identity, structure,
  source concept, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/microdiplodiasone.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/microdiplodiasone.yaml --out /tmp/antibioticmech-microdiplodiasone-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2939 expected records, 2939 on disk, no missing, unexpected, or drifted records, no identifiers absent from `PATHS.tsv`, and no stale lockfile rows. |
| `just review-queue --limit 17` | Passed and confirmed `CHEBI:68284` appears in the review-readiness queue as `MECHANISM_REVIEW`. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-microdiplodiasone.tsv` | Passed; `CHEBI:68284` appears in `mechanism`, `producer-candidate`, and `review-readiness`. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and PATHS
inputs.

## Identity and Grounding

The seeded identity is consistent with the authoritative ChEBI record:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:68284`, `(+)-microdiplodiasone` | Official ChEBI resolved `CHEBI:68284` to `(+)-microdiplodiasone`. |
| Definition | 5,7-dihydroxy-2-methyl-2-(5-oxotetrahydrofuran-2-yl)-substituted 2,3-dihydro-4H-chromen-4-one, isolated from an endophytic `Microdiplodia` species, with antibacterial activity | Matched ChEBI's definition. |
| Formula and charge | `C14H14O6`, charge `0` | Matched ChEBI. |
| Masses | average `278.260`, monoisotopic `278.07904` | Matched ChEBI. |
| SMILES | `[H][C@]1([C@@]2(C)CC(=O)c3c(O)cc(O)cc3O2)CCC(=O)O1` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C14H14O6/c1-14(11-2-3-12(18)19-11)6-9(17)13-8(16)4-7(15)5-10(13)20-14/h4-5,11,15-16H,2-3,6H2,1H3/t11-,14-/m1/s1` | Matched ChEBI. |
| InChIKey | `KYUNATJAFQPBJE-BXUZGUMPSA-N` | Matched ChEBI. |
| Antibacterial role | `CHEBI:33282` | ChEBI asserts `has role` to `antibacterial agent`. |
| Parent compounds | `CHEBI:22950`, `CHEBI:27171`, `CHEBI:33572`, `CHEBI:38763` | ChEBI asserts `is a` edges to butan-4-olide, organic heterobicyclic compound, resorcinols, and chromanone. |

The record correctly preserves the exact ChEBI source concept and ChEBI's IUPAC
name as an exact synonym:

- `(2R)-5,7-dihydroxy-2-methyl-2-[(2R)-5-oxotetrahydrofuran-2-yl]-2,3-dihydro-4H-chromen-4-one`

The record has no `xrefs`, matching the public ChEBI page. ChEBI's Species of
Metabolite table links `Microdiplodia` to `NCBITaxon:371130`, cites
`PMID:21244021`, gives strain text `9907`, and describes an ethyl-acetate
extract of an endophytic fungus isolated from `Lycium intricatum`. An NCBI
Taxonomy exact-scientific-name search confirmed that `NCBITaxon:371130` is the
genus `Microdiplodia`.

## Evidence

The target record has no record-level `evidence`. That is allowed for a
ChEBI-seeded record because the ChEBI source concept supplies provenance, and
there are no `activity_spectrum`, `molecular_targets`,
`resistance_mechanisms`, `producer_organisms`, `clinical_status_assertions`,
`datasets`, or `causal_graphs` that would require claim-level evidence.

ChEBI's source row carries one PMID lead:

| PMID | DOI | What the resolved source covers for this review |
|---|---|---|
| `PMID:21244021` | `10.1021/np100730b` | Siddiqui et al. 2011 reports chemical investigation of `Microdiplodia` sp. isolated from `Lycium intricatum` and isolation of four new compounds, including 2,3-dihydrochroman-4-one derivatives. PubMed and Europe PMC metadata report antibacterial activity against `Legionella pneumophila` and/or antifungal activity against `Microbotryum violaceum` for most isolated metabolites, but the public abstract does not map exact MICs, assay conditions, or organism outcomes to `(+)-microdiplodiasone`. |

Targeted literature searches:

| Query | Result |
|---|---|
| Exact `(+)-microdiplodiasone` publication search | Returned one PubMed candidate, the later total-synthesis paper `PMID:25560746`. Its abstract reports total synthesis of racemic microdiplodiasone and related chromanone lactones but does not describe antimicrobial testing. |
| `microdiplodiasone antibacterial Legionella` | Returned a noisy PubMed/Semantic Scholar candidate set dominated by unrelated `Legionella` antibacterial and host-response papers. |
| `KYUNATJAFQPBJE-BXUZGUMPSA-N OR CHEBI:68284 OR CID 52937071` | Returned a noisy PubMed candidate set unrelated to this ChEBI concept; the local Semantic Scholar adapter returned an invalid-response error. |

The exact-name Semantic Scholar search returned an HTTP 429 rate-limit error.

## Completeness

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`,
  `molecular_targets`, and `causal_graphs` are absent, so the record has no
  curator-owned antibacterial mechanism.
- No `activity_spectrum` entry captures the exact `Legionella pneumophila` or
  `Microbotryum violaceum` assay results, organism strains, MICs or other
  measurements, values, units, and per-observation evidence from Siddiqui et
  al. 2011.
- No `producer_organisms` entry captures the `Microdiplodia` source-organism
  lead. ChEBI and the worklist only support a source/isolation lead, so a
  curator must inspect the primary paper before converting that item into a
  biosynthetic producer claim.

Correctly empty optional slots:

- No `resistance_mechanisms`: the record is ChEBI-only and CARD resistance
  routes do not apply to this fungal natural product.
- No `clinical_status` or `clinical_status_assertions`: the ChEBI-only source
  concept and inspected metadata do not assert regulatory use.
- No `datasets`: inspected ChEBI, PubMed, Europe PMC, and exact-name PubMed
  metadata did not surface a public screening, omics, or structural dataset
  accession for this exact structure.

Ignored-inclusive absence search:

- Ran `rg --hidden --no-ignore` over `curation/`, `data/raw/`,
  `reports/yaml_record_review/`, `data/antibiotics/PATHS.tsv`, and the full
  exported worklist for `CHEBI:68284`, `microdiplodiasone`,
  `KYUNATJAFQPBJE-BXUZGUMPSA-N`, `PMID:21244021`, and `Microdiplodia`.
- The search found only the expected `PATHS.tsv`, ChEBI raw row, worklist, and
  review-queue rows. It found no prior review report, `curation/decisions.tsv`
  row, or curated mechanism decision for this exact ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | MICRODIPLODIASONE-M1 | The record is still a seeded compound stub with no curator-owned activity spectrum, mode of action, mechanism scope, molecular target, or causal graph despite an exact primary activity lead. | `just review-queue --limit 17` reports `MECHANISM_REVIEW: mechanism is absent`; `/tmp/antibioticmech-worklist-microdiplodiasone.tsv` lists `CHEBI:68284` on `mechanism`, `producer-candidate`, and `review-readiness`. PubMed and Europe PMC resolve `PMID:21244021` as the exact ChEBI-cited primary paper for `Microdiplodia` antibacterial and antifungal metabolites, but no claim from that source has been curated onto the record. | `data/antibiotics/antibacterial/microdiplodiasone.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the full text of Siddiqui et al. 2011, DOI `10.1021/np100730b`, and
   curate organism-specific `activity_spectrum` entries for exact assay results
   involving `(+)-microdiplodiasone`, with method, value, unit, strain, and
   evidence on each observation.
2. Curate `mode_of_action`, `mode_of_action_target_scope`,
   `mode_of_action_notes`, molecular targets, and causal graph only to the
   precision directly supported by the Siddiqui et al. full text.
3. Inspect Siddiqui et al. 2011 before deciding whether `Microdiplodia` sp.
   strain `9907` should become a `producer_organisms` entry; do not promote
   ChEBI's source-only species row into a biosynthetic producer claim unless
   the primary paper supports that wording.
4. Preserve the seeded ChEBI identity, structure, role, parent compounds, and
   source concept. This review found no grounded-identity correction that
   belongs in `curation/decisions.tsv`, `data/raw/chebi_antimicrobials.tsv`, or
   `data/antibiotics/PATHS.tsv`.

## Follow-up Checks

- `just validate-strict data/antibiotics/antibacterial/microdiplodiasone.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-microdiplodiasone.tsv`
- `just review-queue --limit 20`
- `just qc`
- Manual diff review of
  `data/antibiotics/antibacterial/microdiplodiasone.yaml` to confirm every new
  activity or mechanism claim is claim-local and directly supported by
  `PMID:21244021`.

## Additional Notes

- `NCBI_EMAIL` was unset in the local environment before using NCBI E-utilities
  and the PubMed search script; no contact email was sent as NCBI API metadata.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded finding above.
- The failed Semantic Scholar searches were rate-limit or invalid-response
  failures only. They did not affect identity validation because ChEBI, PubMed,
  Europe PMC, and NCBI Taxonomy supplied the needed exact checks.
