# YAML Record Review: (+)-N-(methoxycarbonyl)-N-norboldine

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/unspecified/n-methoxycarbonyl-n-norboldine.yaml`
- Started UTC: 2026-09-21T12:37:05Z
- Finished UTC: 2026-09-21T12:43:00Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:66701` |
| Label | `(+)-N-(methoxycarbonyl)-N-norboldine` |
| Path | `data/antibiotics/unspecified/n-methoxycarbonyl-n-norboldine.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:66701` / `(+)-N-(methoxycarbonyl)-N-norboldine` |
| Minted source key | `antibioticmech:chebi-779c4a2dc8` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, structure, class, role, or synonym changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:17` is the next unreported queue row and
  names `CHEBI:66701`, label `(+)-N-(methoxycarbonyl)-N-norboldine`, and the
  review hint `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:1886` maps `CHEBI:66701` to the
  `ANTIMICROBIAL_UNSPECIFIED` directory and
  `n-methoxycarbonyl-n-norboldine` slug.
- `data/raw/chebi_antimicrobials.tsv:1632` is the ChEBI source row that seeds
  the target record.
- The whole target YAML was read before judging generated identity, structure,
  source concept, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/n-methoxycarbonyl-n-norboldine.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/n-methoxycarbonyl-n-norboldine.yaml --out /tmp/antibioticmech-n-methoxycarbonyl-n-norboldine-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2939 expected records, 2939 on disk, no missing, unexpected, or drifted records, no identifiers absent from `PATHS.tsv`, and no stale lockfile rows. |
| `just review-queue --limit 18` | Passed and confirmed `CHEBI:66701` appears in the review-readiness queue as `MECHANISM_REVIEW`. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-n-methoxycarbonyl-n-norboldine.tsv` | Passed; `CHEBI:66701` appears in `mechanism`, `producer-candidate`, and `review-readiness`. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and PATHS
inputs.

## Identity and Grounding

The seeded identity is consistent with the authoritative ChEBI record:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:66701`, `(+)-N-(methoxycarbonyl)-N-norboldine` | Official ChEBI resolved `CHEBI:66701` to `(+)-N-(methoxycarbonyl)-N-norboldine`. |
| Definition | A laurolistine aporphine alkaloid with an N-methoxycarbonyl group, isolated from the aerial parts of `Litsea cubeba`, with antimicrobial activities | Matched ChEBI's definition. |
| Formula and charge | `C20H21NO6`, charge `0` | Matched ChEBI. |
| Masses | average `371.389`, monoisotopic `371.13689` | Matched ChEBI. |
| SMILES | `[H][C@]12Cc3cc(O)c(OC)cc3-c3c(OC)c(O)cc(c31)CCN2C(=O)OC` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C20H21NO6/c1-25-16-9-12-11(8-14(16)22)6-13-17-10(4-5-21(13)20(24)27-3)7-15(23)19(26-2)18(12)17/h7-9,13,22-23H,4-6H2,1-3H3/t13-/m0/s1` | Matched ChEBI. |
| InChIKey | `RYEXLSDOKVGMTN-ZDUSSCGKSA-N` | Matched ChEBI. |
| Antimicrobial role | `CHEBI:33281` | ChEBI asserts `has role` to `antimicrobial agent`. |
| Parent compounds | `CHEBI:134209`, `CHEBI:33308`, `CHEBI:33853`, `CHEBI:35618` | ChEBI asserts `is a` edges to aporphine alkaloid, carboxylic ester, phenols, and aromatic ether. |

The record correctly preserves the exact ChEBI source concept and ChEBI's IUPAC
name as an exact synonym:

- `methyl (6aS)-2,9-dihydroxy-1,10-dimethoxy-4,5,6a,7-tetrahydro-6H-dibenzo[de,g]quinoline-6-carboxylate`

The record has no `xrefs`, matching the public ChEBI page. ChEBI's Species of
Metabolite table links `Litsea cubeba` to `NCBITaxon:155299`, component
`aerial part` to `BTO:0001658`, and source `PMID:18991207`. An NCBI Taxonomy
exact-scientific-name search confirmed `NCBITaxon:155299` is `Litsea cubeba`.
ChEBI also asserts `has functional parent` to laurolistine / `CHEBI:66557`;
the seeder correctly retains only broader `is_a` parents in
`parent_compounds`.

## Evidence

The target record has no record-level `evidence`. That is allowed for a
ChEBI-seeded record because the ChEBI source concept supplies provenance, and
there are no `activity_spectrum`, `molecular_targets`,
`resistance_mechanisms`, `producer_organisms`, `clinical_status_assertions`,
`datasets`, or `causal_graphs` that would require claim-level evidence.

ChEBI's source row carries one PMID lead:

| PMID | DOI | What the resolved source covers for this review |
|---|---|---|
| `PMID:18991207` | `10.1055/s-0028-1088344` | Feng et al. 2009 reports bioassay-guided fractionation of the alkaloidal extract from the aerial part of `Litsea cubeba`, isolation and structural assignment of `(+)-N-(methoxycarbonyl)-N-norboldine` as compound 1, and antimicrobial activity for compounds 1 and 4. PubMed indexing names microbial-sensitivity testing, fungi, `Mycobacterium tuberculosis`, and `Staphylococcus aureus`, but the public abstract does not map exact organisms, assays, MICs, or other values to compound 1. |

Targeted literature searches:

| Query | Result |
|---|---|
| Exact `(+)-N-(methoxycarbonyl)-N-norboldine` publication search | Returned one PubMed candidate, Feng et al. 2009 / `PMID:18991207`. |
| `RYEXLSDOKVGMTN-ZDUSSCGKSA-N OR CHEBI:66701` | Returned 0 PubMed candidates. |
| `"N-norboldine" antimicrobial Litsea cubeba Staphylococcus Mycobacterium` | Returned 0 PubMed candidates. |

The Semantic Scholar adapter returned HTTP 429 rate-limit errors during the
exact-name and targeted antimicrobial searches.

## Completeness

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`,
  `molecular_targets`, and `causal_graphs` are absent, so the record has no
  curator-owned antimicrobial mechanism.
- No `activity_spectrum` entry captures the exact assay organisms, strains,
  MICs or other measurements, values, units, and per-observation evidence from
  Feng et al. 2009.
- No `producer_organisms` entry captures the `Litsea cubeba` source-organism
  lead. ChEBI reports a plant occurrence/isolation observation, so a curator
  must inspect the primary paper and avoid converting source-only text into a
  biosynthesis claim without support.

Correctly empty optional slots:

- No `resistance_mechanisms`: the record is ChEBI-only and CARD resistance
  routes do not apply to this plant alkaloid.
- No `clinical_status` or `clinical_status_assertions`: the ChEBI-only source
  concept and inspected metadata do not assert regulatory use.
- No `datasets`: inspected ChEBI, PubMed metadata, and exact-name PubMed
  searches did not surface a public screening, omics, or structural dataset
  accession for this exact structure.

Ignored-inclusive absence search:

- Ran `rg --hidden --no-ignore` over `curation/`, `data/raw/`,
  `reports/yaml_record_review/`, the target YAML, `data/antibiotics/PATHS.tsv`,
  and the full exported worklist for `CHEBI:66701`,
  `(+)-N-(methoxycarbonyl)-N-norboldine`,
  `n-methoxycarbonyl-n-norboldine`, `RYEXLSDOKVGMTN`, `18991207`,
  `10.1055/s-0028-1088344`, and `Litsea cubeba`.
- The search found only the expected generated target, `PATHS.tsv`, ChEBI raw
  row, worklist, and review-queue rows. It found no prior review report,
  `curation/decisions.tsv` row, or curated mechanism decision for this exact
  ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | NORBOLDINE-M1 | The record is still a seeded compound stub with no curator-owned activity spectrum, mode of action, mechanism scope, molecular target, or causal graph despite an exact primary activity lead. | `just review-queue --limit 18` reports `MECHANISM_REVIEW: mechanism is absent`; `/tmp/antibioticmech-worklist-n-methoxycarbonyl-n-norboldine.tsv` lists `CHEBI:66701` on `mechanism`, `producer-candidate`, and `review-readiness`. PubMed resolves `PMID:18991207` as the exact ChEBI-cited primary paper for `(+)-N-(methoxycarbonyl)-N-norboldine` isolation and antimicrobial activity, but no claim from that source has been curated onto the record. | `data/antibiotics/unspecified/n-methoxycarbonyl-n-norboldine.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the full text of Feng et al. 2009, DOI `10.1055/s-0028-1088344`,
   and curate organism-specific `activity_spectrum` entries for exact assay
   results involving `(+)-N-(methoxycarbonyl)-N-norboldine`, with method,
   value, unit, strain, and evidence on each observation.
2. Curate `mode_of_action`, `mode_of_action_target_scope`,
   `mode_of_action_notes`, molecular targets, and causal graph only to the
   precision directly supported by the Feng et al. full text. Leave these
   fields blank if the paper reports activity without a mechanism.
3. Inspect Feng et al. 2009 before deciding whether `Litsea cubeba` should
   become a `producer_organisms` entry; do not promote ChEBI's source-only
   species row into a biosynthetic producer claim unless the primary paper
   supports that wording.
4. Preserve the seeded ChEBI identity, structure, role, parent compounds, and
   source concept. This review found no grounded-identity correction that
   belongs in `curation/decisions.tsv`, `data/raw/chebi_antimicrobials.tsv`, or
   `data/antibiotics/PATHS.tsv`.

## Follow-up Checks

- `just validate-strict data/antibiotics/unspecified/n-methoxycarbonyl-n-norboldine.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-n-methoxycarbonyl-n-norboldine.tsv`
- `just review-queue --limit 20`
- `just qc`
- Manual diff review of
  `data/antibiotics/unspecified/n-methoxycarbonyl-n-norboldine.yaml` to confirm
  every new activity or mechanism claim is claim-local and directly supported
  by `PMID:18991207`.

## Additional Notes

- `NCBI_EMAIL` was unset in the local environment before using NCBI E-utilities
  and the PubMed search script; no contact email was sent as NCBI API metadata.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded finding above.
- The failed Semantic Scholar searches were rate-limit failures only. They did
  not affect identity validation because ChEBI, PubMed, and NCBI Taxonomy
  supplied the needed exact checks.
