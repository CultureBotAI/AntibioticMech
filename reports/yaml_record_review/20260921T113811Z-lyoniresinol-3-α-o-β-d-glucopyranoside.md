# YAML Record Review: (+)-lyoniresinol-3-α-O-β-D-glucopyranoside

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antibacterial/lyoniresinol-3-α-o-β-d-glucopyranoside.yaml`
- Started UTC: 2026-09-21T11:33:40Z
- Finished UTC: 2026-09-21T11:38:11Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:66606` |
| Label | `(+)-lyoniresinol-3-α-O-β-D-glucopyranoside` |
| Path | `data/antibiotics/antibacterial/lyoniresinol-3-α-o-β-d-glucopyranoside.yaml` |
| Class | `ANTIBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:66606` / `(+)-lyoniresinol-3-α-O-β-D-glucopyranoside` |
| Minted source key | `antibioticmech:chebi-2e7bb9fa53` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, class, role, or xref changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:15` is the next unreported queue row and
  names `CHEBI:66606`, label
  `(+)-lyoniresinol-3-α-O-β-D-glucopyranoside`, and the review hint
  `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:1850` maps `CHEBI:66606` to the `ANTIBACTERIAL`
  directory and `lyoniresinol-3-α-o-β-d-glucopyranoside` slug.
- `data/raw/chebi_antimicrobials.tsv:1596` is the ChEBI source row that seeds
  the target record.
- The whole target YAML was read before judging generated identity, structure,
  xrefs, source concept, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/lyoniresinol-3-α-o-β-d-glucopyranoside.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/lyoniresinol-3-α-o-β-d-glucopyranoside.yaml --out /tmp/antibioticmech-lyoniresinol-3-glucopyranoside-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2939 expected records, 2939 on disk, no missing, unexpected, or drifted records, no identifiers absent from `PATHS.tsv`, and no stale lockfile rows. |
| `just review-queue --limit 16` | Passed and confirmed `CHEBI:66606` appears in the review-readiness queue as `MECHANISM_REVIEW`. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-lyoniresinol-3-glucopyranoside.tsv` | Passed; `CHEBI:66606` appears in `mechanism`, `producer-candidate`, and `review-readiness`. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and PATHS
inputs.

## Identity and Grounding

The seeded identity is consistent with the authoritative ChEBI record:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:66606`, `(+)-lyoniresinol-3-α-O-β-D-glucopyranoside` | Official ChEBI resolved `CHEBI:66606` to `(+)-lyoniresinol-3-α-O-β-D-glucopyranoside`. |
| Definition | Lignan with a β-D-glucopyranosyl moiety at position 3, isolated from `Stemmadenia minima` and `Lycium chinense` root bark, with antimicrobial activities | Matched ChEBI's definition. |
| Formula and charge | `C28H38O13`, charge `0` | Matched ChEBI. |
| Masses | average `582.599`, monoisotopic `582.23124` | Matched ChEBI. |
| SMILES | `COc1cc([C@H]2c3c(cc(OC)c(O)c3OC)C[C@@H](CO)[C@@H]2CO[C@@H]2O[C@H](CO)[C@@H](O)[C@H](O)[C@H]2O)cc(OC)c1O` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C28H38O13/.../t14-,15-,19+,20+,23+,25-,26+,28+/m0/s1` | Matched ChEBI. |
| InChIKey | `PQQRNPDHSJDAGV-HQSXISOASA-N` | Matched ChEBI. |
| Antibacterial role | `CHEBI:33282` | ChEBI asserts `has role` to `antibacterial agent`. |
| Antifungal role | `CHEBI:35718` | ChEBI asserts `has role` to `antifungal agent`. |
| Functional parent | Not seeded into `parent_compounds` | ChEBI asserts `has functional parent` to `(+)-lyoniresinol` / `CHEBI:68168`; the seeder correctly retains only broader `is_a` parents in `parent_compounds`. |
| Parent compounds | `CHEBI:15734`, `CHEBI:22798`, `CHEBI:25036`, `CHEBI:26195`, `CHEBI:36786`, `CHEBI:51681`, `CHEBI:63367` | ChEBI asserts `is a` edges to primary alcohol, β-D-glucoside, lignan, polyphenol, tetralins, dimethoxybenzene, and monosaccharide derivative. |

The record correctly preserves the exact ChEBI source concept and keeps ChEBI's
alternate names as synonyms:

- `[(1S,2R,3R)-7-hydroxy-1-(4-hydroxy-3,5-dimethoxyphenyl)-3-(hydroxymethyl)-6,8-dimethoxy-1,2,3,4-tetrahydronaphthalen-2-yl]methyl β-D-glucopyranoside`
- `(+)-lyoniresinol 9'-O-β-D-glucopyranoside`
- `pteleifoside G`

The xref set is exactly the public ChEBI xref set:

| Xref | Check |
|---|---|
| `hmdb:HMDB0038922` | ChEBI lists `HMDB0038922` as a manual xref. |
| `reaxys:6168345` | ChEBI lists this Reaxys registry number. Reaxys itself has no public resolver for this review to inspect. |

ChEBI's Species of Metabolite table links `Lycium chinense` to
`NCBITaxon:112883` with `PMID:16212233` as the source. The
`Stemmadenia minima` row links to `IPNI:81813-1` with `PMID:17226467` as the
source; an NCBI Taxonomy exact-scientific-name search did not resolve
`Stemmadenia minima`.

## Evidence

The target record has no record-level `evidence`. That is allowed for a
ChEBI-seeded record because the ChEBI source concept supplies provenance, and
there are no `activity_spectrum`, `molecular_targets`,
`resistance_mechanisms`, `producer_organisms`, `clinical_status_assertions`,
`datasets`, or `causal_graphs` that would require claim-level evidence.

ChEBI's source row carries two PMID leads:

| PMID | DOI | What the resolved source covers for this review |
|---|---|---|
| `PMID:16212233` | `10.1007/BF02977397` | Lee et al. 2005 is the exact antimicrobial-activity lead for `(+)-lyoniresinol-3alpha-O-beta-D-glucopyranoside` isolated from `Lycium chinense` root bark; PubMed and Europe PMC metadata report antibacterial testing against antibiotic-resistant bacterial strains and methicillin-resistant `Staphylococcus aureus`, antifungal testing against human-pathogenic fungi, and `Candida albicans` stress-response and dimorphic-transition assays. |
| `PMID:17226467` | `10.1055/s-2006-961451` | Achenbach et al. 1992 reports lignan glucosides from `Stemmadenia minima` stem bark. The public abstract supports a structure/isolation lead, not an antimicrobial assay or mechanism. |

Targeted literature searches:

| Query | Result |
|---|---|
| Exact PubMed `(+)-Lyoniresinol-3alpha-O-beta-D-glucopyranoside` title/abstract search | Returned 18 tokenized candidates, including Lee et al. 2005. Later hits were dominated by related lyoniresinol glycosides, non-antimicrobial isolation papers, and non-microbial bioactivity papers. |
| `pteleifoside G` in PubMed title/abstract | Returned 0 candidates. |
| `PQQRNPDHSJDAGV-HQSXISOASA-N` in PubMed all fields | Returned 0 candidates. |
| `lyoniresinol glucopyranoside antimicrobial antibacterial antifungal` | Returned a noisy PubMed/Semantic Scholar candidate set dominated by related glucopyranoside and lyoniresinol records rather than this exact `CHEBI:66606` structure. |

The exact-name and identifier searches through the local Semantic Scholar
adapter returned HTTP 429 rate-limit errors.

## Completeness

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`,
  `molecular_targets`, and `causal_graphs` are absent, so the record has no
  curator-owned antibacterial or antifungal mechanism. The public abstract for
  `PMID:16212233` reports `Candida albicans` stress-response and
  dimorphic-transition observations, but not a molecular target.
- No `activity_spectrum` entry captures exact MICs, assay type, organisms,
  strains, outcomes, or units from the Lee et al. 2005 antibacterial and
  antifungal assays.
- No `producer_organisms` entry captures either plant origin from ChEBI's
  species table. ChEBI reports isolation/source observations, so a curator must
  inspect the primary papers and avoid converting source-only text into a
  biosynthesis claim without support.

Correctly empty optional slots:

- No `resistance_mechanisms`: the record is ChEBI-only and CARD resistance
  routes do not apply to a plant lignan glucoside.
- No `clinical_status` or `clinical_status_assertions`: the ChEBI-only source
  concept and inspected metadata do not assert regulatory use.
- No `datasets`: inspected ChEBI, PubMed, Europe PMC, and exact-name PubMed
  metadata did not surface a public screening, omics, or structural dataset
  accession for this exact structure.

Ignored-inclusive absence search:

- Ran `rg --hidden --no-ignore` over `curation/`, `data/raw/`,
  `reports/yaml_record_review/`, the target YAML, `data/antibiotics/PATHS.tsv`,
  and the full exported worklist for `CHEBI:66606`, `PQQRNPDHSJDAGV`,
  `HMDB0038922`, `6168345`, `16212233`, `17226467`, and `lyoniresinol`.
- The search found only the expected generated target, `PATHS.tsv`, ChEBI raw
  row, worklist, and review-queue rows. It found no prior review report,
  `curation/decisions.tsv` row, or curated mechanism decision for this exact
  ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | LYONIRESINOL-M1 | The record is still a seeded compound stub with no curator-owned activity spectrum, mode of action, mechanism scope, molecular target, or causal graph despite an exact primary activity lead. | `just review-queue --limit 16` reports `MECHANISM_REVIEW: mechanism is absent`; `/tmp/antibioticmech-worklist-lyoniresinol-3-glucopyranoside.tsv` lists `CHEBI:66606` on `mechanism` and `review-readiness`. PubMed/Europe PMC resolve `PMID:16212233` as an exact primary paper for antibacterial and antifungal assays of `(+)-lyoniresinol-3alpha-O-beta-D-glucopyranoside`, but no claim from that source has been curated onto the record. | `data/antibiotics/antibacterial/lyoniresinol-3-α-o-β-d-glucopyranoside.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the full text of Lee et al. 2005, DOI `10.1007/BF02977397`, and
   curate organism-specific `activity_spectrum` entries for exact antibacterial
   and antifungal assay results with method, value, unit, strain, and evidence
   on each observation.
2. Curate a `mode_of_action`, `mode_of_action_target_scope`,
   `mode_of_action_notes`, molecular targets, and causal graph only to the
   precision directly supported by the Lee et al. full text. The public
   metadata support a `Candida albicans` stress/dimorphism lead but do not name
   a molecular target.
3. Inspect Achenbach et al. 1992 and Lee et al. 2005 before deciding whether
   `Stemmadenia minima` or `Lycium chinense` should become
   `producer_organisms`; do not promote ChEBI's source-only species rows into
   biosynthetic producer claims unless the primary papers support that wording.
4. Preserve the seeded ChEBI identity, structure, role, parents, and source
   concept. This review found no grounded-identity correction that belongs in
   `curation/decisions.tsv`, `data/raw/chebi_antimicrobials.tsv`, or
   `data/antibiotics/PATHS.tsv`.

## Follow-up Checks

- `just validate-strict data/antibiotics/antibacterial/lyoniresinol-3-α-o-β-d-glucopyranoside.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-lyoniresinol-3-glucopyranoside.tsv`
- `just review-queue --limit 20`
- `just qc`
- Manual diff review of
  `data/antibiotics/antibacterial/lyoniresinol-3-α-o-β-d-glucopyranoside.yaml`
  to confirm evidence is claim-local and every `mode_of_action` or
  plant-origin claim is paired with honest `CURATOR:` provenance.

## Additional Notes

- `NCBI_EMAIL` was unset in the local environment before using NCBI E-utilities
  and the PubMed search script; no contact email was sent as NCBI API metadata.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded findings above.
- The failed Semantic Scholar searches were rate-limit failures only. They did
  not affect identity validation because ChEBI, PubMed, Europe PMC, and NCBI
  Taxonomy supplied the needed exact checks.
