# YAML Record Review: (+)-lariciresinol

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antifungal/lariciresinol.yaml`
- Started UTC: 2026-09-21T10:33:00Z
- Finished UTC: 2026-09-21T10:36:30Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:67246` |
| Label | `(+)-lariciresinol` |
| Path | `data/antibiotics/antifungal/lariciresinol.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:67246` / `(+)-lariciresinol` |
| Minted source key | `antibioticmech:chebi-434a99ff21` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity or xref changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:13` is the next unreported queue row and names `CHEBI:67246`, label `(+)-lariciresinol`, and the review hint `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:1913` maps `CHEBI:67246` to the `ANTIFUNGAL` directory and `lariciresinol` slug.
- `data/raw/chebi_antimicrobials.tsv:1658` is the ChEBI source row that seeds the target record.
- The whole target YAML was read before judging generated identity, structure, xrefs, source concept, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/lariciresinol.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/lariciresinol.yaml --out /tmp/antibioticmech-lariciresinol-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2939 expected records, 2939 on disk, no missing, unexpected, or drifted records, no identifiers absent from `PATHS.tsv`, and no stale lockfile rows. |
| `just review-queue --limit 14` | Passed and confirmed `CHEBI:67246` appears in the review-readiness queue as `MECHANISM_REVIEW`. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-lariciresinol.tsv` | Passed; `CHEBI:67246` appears only in the `mechanism` and `review-readiness` queues. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and PATHS
inputs.

## Identity and Grounding

The seeded identity is consistent with the authoritative ChEBI record:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:67246`, `(+)-lariciresinol` | Official ChEBI resolved `CHEBI:67246` to `(+)-lariciresinol`. |
| Definition | Lignan with a tetrahydrofuran substituted at the 2, 3, and 4 positions, explicitly the `(2S,3R,4R)` diastereomer | Matched ChEBI's definition. |
| Formula and charge | `C20H24O6`, charge `0` | Matched ChEBI. |
| Masses | average `360.406`, monoisotopic `360.15729` | Matched ChEBI. |
| SMILES | `COc1cc(C[C@H]2CO[C@H](c3ccc(O)c(OC)c3)[C@H]2CO)ccc1O` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C20H24O6/.../t14-,15-,20+/m0/s1` | Matched ChEBI. |
| InChIKey | `MHXCIKYXNYCMHY-AUSJPIAWSA-N` | Matched ChEBI. |
| Antifungal role | `CHEBI:35718` | ChEBI asserts `has role` to `antifungal agent`. |
| Parent compounds | `CHEBI:15734`, `CHEBI:25036`, `CHEBI:26912`, `CHEBI:33853`, `CHEBI:35618` | ChEBI asserts `is a` edges to primary alcohol, lignan, oxolanes, phenols, and aromatic ether. |

The record correctly preserves one exact ChEBI source concept and keeps ChEBI's
alternate names as synonyms:

- `4-[(2S,3R,4R)-4-(4-hydroxy-3-methoxybenzyl)-3-(hydroxymethyl)tetrahydrofuran-2-yl]-2-methoxyphenol`
- `Lariciresinol`

The xrefs are mostly corroborated:

| Xref | Check |
|---|---|
| `cas:27003-73-2` | ChEBI lists this registry number from KEGG; KEGG `C10646` also lists this CAS. |
| `cas:83327-19-9` | ChEBI lists this registry number from ChemIDplus. |
| `kegg.compound:C10646` | KEGG `C10646` is `(+)-Lariciresinol`, has formula `C20H24O6`, and links back to ChEBI `67246` and KNApSAcK `C00000602`. |
| `knapsack:C00000602` | KNApSAcK `C00000602` is `(+)-Lariciresinol` / `Lariciresinol`, formula `C20H24O6`, CAS `27003-73-2`, and prints the same Standard InChI as the record. |
| `metacyc.compound:CPD-8907` | MetaCyc `CPD-8907` resolved as `(+)-lariciresinol`. |
| `wikipedia.en:Lariciresinol` | The document xref resolves to the English Wikipedia article titled `Lariciresinol`; it is correctly outside `xrefs` because it is an article, not a structure registry. |

KNApSAcK displays `MHXCIKYXNYCMHY-KICIYKGHNA-N` while also displaying the same
Standard InChI as ChEBI and this record. Because the Standard InChI, name,
formula, CAS, and reciprocal ChEBI/KEGG/KNApSAcK links are otherwise aligned,
this looks like an upstream KNApSAcK display inconsistency rather than a record
identity defect.

## Evidence

The target record has no record-level `evidence`. That is allowed for a
ChEBI-seeded record because the ChEBI source concept supplies provenance, and
there are no `molecular_targets`, `resistance_mechanisms`,
`activity_spectrum`, `causal_graphs`, `producer_organisms`, or
`clinical_status_assertions` that would require claim-level evidence.

ChEBI's source row carries five PMID leads:

| PMID | DOI | What the resolved source covers for this review |
|---|---|---|
| `PMID:21679690` | `10.1016/j.bbrc.2011.06.004` | Exact antifungal mechanism lead: Hwang et al. 2011 reports lariciresinol isolated from `Sambucus williamsii`, antifungal testing, and membrane-active work in `Candida albicans`. |
| `PMID:21138310` | `10.1021/np100665j` | Tezuka et al. 2011 reports constituents of `Taxus yunnanensis` wood; ChEBI uses this as a species-of-metabolite citation, not a mechanism citation. |
| `PMID:21973054` | `10.1021/np2002918` | Fan et al. 2011 reports compounds from `Rubia yunnanensis` roots and broad cytotoxic/antibacterial/antifungal testing; ChEBI uses it as a species-of-metabolite citation. |
| `PMID:22218086` | `10.1016/j.jplph.2011.12.006` | Linum album fungal elicitor and lignan-biosynthesis study; not an antimicrobial mechanism source. |
| `PMID:8262939` | None in PubMed | Plant pinoresinol/(+)-lariciresinol reductase stereospecificity study; not an antimicrobial mechanism source. |

Targeted literature searches:

| Query | Result |
|---|---|
| `(+)-lariciresinol antifungal` | PubMed returned 7 candidates; the Hwang et al. exact antifungal mechanism paper appeared. Semantic Scholar returned HTTP 429. |
| `MHXCIKYXNYCMHY OR C10646 OR C00000602 OR CPD-8907 OR 27003-73-2 OR 83327-19-9` | PubMed returned 20 candidates, dominated by lignan biosynthesis and non-antimicrobial lariciresinol papers. Semantic Scholar returned HTTP 429. |
| `Lariciresinol MIC antifungal Candida` | PubMed returned 0 candidates. Semantic Scholar returned HTTP 429. |

## Completeness

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`,
  `molecular_targets`, and `causal_graphs` are absent, so the record has no
  curator-owned antifungal mechanism despite a precise membrane-active primary
  lead in `PMID:21679690`.
- No MIC or other strain-level antifungal activity assertions are curated.
  PubMed did not return a direct `Lariciresinol MIC antifungal Candida` hit, so
  a curator would need the Hwang et al. full text before adding MIC values,
  units, organism names, and assay conditions.

Correctly empty optional slots:

- No `resistance_mechanisms`: the record is ChEBI-only and no CARD resistance
  route is imported.
- No `producer_organisms`: ChEBI records plant origin metadata, but this record
  has no curated microbial biosynthesis claim.
- No `clinical_status` or `clinical_status_assertions`: no official regulatory
  source was found or expected for this natural-product lignan.
- No `datasets`: the bounded review found no public dataset accession that
  should be linked.

Ignored-inclusive absence search:

- Ran `rg --hidden --no-ignore` over `curation/`, `data/raw/`,
  `reports/yaml_record_review/`, the target YAML, and `data/antibiotics/PATHS.tsv`
  for `CHEBI:67246`, `antibioticmech:chebi-434a99ff21`,
  `MHXCIKYXNYCMHY`, `27003-73-2`, `83327-19-9`, `C10646`, `C00000602`,
  `CPD-8907`, `21679690`, and `lariciresinol`.
- The search found only the expected ChEBI raw row, generated target YAML,
  `PATHS.tsv` row, and review-queue row. It found no prior review report,
  `curation/decisions.tsv` entry, or curated mechanism decision for this exact
  ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | LARICIRESINOL-M1 | The record is still a seeded compound stub with no curator-owned mode of action, mechanism scope, molecular target, activity observation, or causal graph. It therefore cannot satisfy the repository `REVIEWED` gate. | `just review-queue --limit 14` reports `MECHANISM_REVIEW: mechanism is absent`; `/tmp/antibioticmech-worklist-lariciresinol.tsv` lists `CHEBI:67246` only on `mechanism` and `review-readiness`. PubMed/Europe PMC resolve `PMID:21679690` as an exact lariciresinol antifungal mechanism lead in `Candida albicans`, but no claim from that source has been curated onto the record. | `data/antibiotics/antifungal/lariciresinol.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the full text of Hwang et al. 2011, DOI
   `10.1016/j.bbrc.2011.06.004`, and curate any exact organism panel,
   MIC/fungicidal measurements, membrane-permeabilization assays, and coarse
   `MEMBRANE_DISRUPTION` mechanism that the paper directly supports.
2. If the membrane claim is curated, decide and justify
   `mode_of_action_target_scope` with a `CURATOR:` note at the same time;
   this record has no ChEBI-seeded mechanism block for the seeder to own.
3. Attach `PMID:21679690` evidence to the narrowest supported objects:
   `activity_spectrum` entries for measured assay results, a coarse
   `mode_of_action` note for the mechanism bucket, and causal graph edges only
   for specific membrane-probe or permeabilization relationships actually shown
   by the source.
4. Preserve the seeded ChEBI identity, structure, role, parents, and source
   concept. This review found no grounded-identity correction that belongs in
   `curation/decisions.tsv`, `data/raw/chebi_antimicrobials.tsv`, or
   `data/antibiotics/PATHS.tsv`.

## Follow-up Checks

- `just validate-strict data/antibiotics/antifungal/lariciresinol.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-lariciresinol.tsv`
- `just review-queue --limit 20`
- `just qc`
- Manual diff review of `data/antibiotics/antifungal/lariciresinol.yaml` to
  confirm evidence is claim-local and every `mode_of_action` claim is paired
  with honest `CURATOR:` provenance.

## Additional Notes

- `NCBI_EMAIL` was unset in the local environment before using the PubMed
  search script; no contact email was sent as NCBI API metadata.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded findings above.
- The failed Semantic Scholar searches were rate-limit failures only. They did
  not affect identity validation because ChEBI, KEGG, KNApSAcK, MetaCyc,
  PubMed, and Europe PMC supplied the needed exact checks.
