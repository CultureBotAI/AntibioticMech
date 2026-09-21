# YAML Record Review: (+)-zwittermicin A

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antifungal/zwittermicin-a.yaml`
- Started UTC: 2026-09-21T17:17:36Z
- Finished UTC: 2026-09-21T17:20:01Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:80056` |
| Label | `(+)-zwittermicin A` |
| Path | `data/antibiotics/antifungal/zwittermicin-a.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:80056` / `(+)-zwittermicin A` |
| Minted source key | `antibioticmech:chebi-c37eba3bd7` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, structure, class, role, synonym, or xref changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:26` names `CHEBI:80056`, label
  `(+)-zwittermicin A`, and the review hint
  `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:2324` maps `CHEBI:80056` to the `ANTIFUNGAL`
  directory and `zwittermicin-a` slug.
- `data/raw/chebi_antimicrobials.tsv:2045` is the ChEBI source row that seeds
  the target record.
- The whole 61-line target YAML was read before judging generated identity,
  structure, xrefs, source concept, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/zwittermicin-a.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/zwittermicin-a.yaml --out /tmp/antibioticmech-zwittermicin-a-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2939 expected records, 2939 on disk, no missing, unexpected, or drifted records, no identifiers absent from `PATHS.tsv`, and no stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-zwittermicin-a.tsv` | Passed; `CHEBI:80056` appears in `mechanism`, `activity-candidate`, and `review-readiness`. |
| `just review-queue --limit 26` | Passed and confirmed `CHEBI:80056` remains in the review-readiness queue as `MECHANISM_REVIEW`, with 10 source literature leads, zero record evidence items, and zero targets. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and PATHS
inputs.

## Identity and Grounding

The seeded identity is consistent with the authoritative ChEBI record:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:80056`, `(+)-zwittermicin A` | Official ChEBI resolved `CHEBI:80056` to `(+)-zwittermicin A`. |
| Formula and charge | `C13H28N6O8`, charge `0` | Matched ChEBI and KEGG. |
| Masses | average `396.401`, monoisotopic `396.19686` | Matched ChEBI and KEGG rounded exact mass `396.1969`. |
| SMILES | `NC(=O)NC[C@H](NC(=O)[C@H](O)[C@@H](O)[C@@H](N)[C@@H](O)C[C@H](O)[C@H](N)CO)C(N)=O` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C13H28N6O8/c14-4(3-20)6(21)1-7(22)8(15)9(23)10(24)12(26)19-5(11(16)25)2-18-13(17)27/h4-10,20-24H,1-3,14-15H2,(H2,16,25)(H,19,26)(H3,17,18,27)/t4-,5+,6+,7+,8+,9+,10-/m1/s1` | Matched ChEBI. |
| InChIKey | `FYIPKJHNWFVEIR-FXQWNPMTSA-N` | Matched ChEBI. |
| Antifungal role | `CHEBI:35718` | ChEBI asserts `has role` to `antifungal agent`. |
| Antimicrobial role | `CHEBI:33281` | ChEBI asserts `has role` to `antimicrobial agent`. |
| Parent compounds | `CHEBI:167622`, `CHEBI:25903` | ChEBI asserts `(+)-zwittermicin A is a 4,8-diamino-N-[1-amino-3-(carbamoylamino)-1-oxopropan-2-yl]-2,3,5,7,9-pentahydroxynonanamide` and `(+)-zwittermicin A is a peptide antibiotic`. |
| Xrefs | `cas:155547-95-8`, `kegg.compound:C15726`, `metacyc.compound:CPD-18237`, `patent:EP1163347`, `wikipedia.en:Zwittermicin_A` | Matched the official ChEBI page; KEGG `C15726` cross-links back to `CHEBI:80056` and CAS `155547-95-8`. |

The target is specifically the `(+)-` enantiomer of zwittermicin A. Official
ChEBI relates it by `is enantiomer of` to `CHEBI:167210` /
`(-)-zwittermicin A`, which is not present as a separate generated record in
this corpus.

ChEBI also asserts the non-antimicrobial `bacterial metabolite` biological role
`CHEBI:76969` and a duplicated `Bronsted base` chemical role. The seeded record
correctly retains only the antimicrobial ChEBI roles that drive inclusion in
this repository, and this review found no identity evidence that the record
should move out of the `ANTIFUNGAL` filing class.

## Evidence

The target record has no record-level `evidence`. That is allowed for a
ChEBI-seeded record because the ChEBI source concept supplies provenance, and
there are no `activity_spectrum`, `molecular_targets`,
`resistance_mechanisms`, `producer_organisms`, `clinical_status_assertions`,
`datasets`, or `causal_graphs` that would require claim-level evidence.

`data/raw/chebi_antimicrobials.tsv:2045` carries 10 PubMed leads for the exact
`CHEBI:80056` source concept. The source abstracts are useful follow-up leads,
but no PubMed lead has been curated onto the generated record:

| PMID | Public abstract support |
|---|---|
| `PMID:10464220` | Reports that ZmaR confers zwittermicin A resistance to gram-positive and gram-negative bacteria, that purified ZmaR inactivates zwittermicin A, and that ZmaR catalyzes acetylation of zwittermicin A. |
| `PMID:10521664` | Reports that the `zmaR` self-resistance gene sits in a *Bacillus cereus* UW85 biosynthetic cluster, is necessary for high-level resistance to zwittermicin A, and is not required for zwittermicin A production. |
| `PMID:14711631` | Reports *Bacillus cereus* UW101C transposon mutants that no longer accumulated zwittermicin A and sequence evidence supporting mixed NRPS/PKS zwittermicin A biosynthesis. |
| `PMID:15281929` | Reports partial cloning and characterization of a *Bacillus thuringiensis* subsp. *kurstaki* HD1 `zmaR` resistance-gene cluster and inhibition zones from a `zmaR`-positive HD1 strain against fungal and bacterial indicators. |
| `PMID:17225146` | Reports additional zwittermicin A biosynthesis-related genes in a *Bacillus thuringiensis* subsp. *kurstaki* YBT-1520 cluster. |
| `PMID:17249781` | Reports asymmetric synthesis of a C9-C15 segment model and degradation/synthetic evidence toward assigning the absolute configuration of natural `(+)-zwittermicin A`. |
| `PMID:18438870` | Reports an AHL-lactonase engineering study in a zwittermicin A-producing *Bacillus cereus* host and compares prevention efficacy against *Erwinia carotovora*. |
| `PMID:18446411` | Reports that deleting *Bacillus thuringiensis* G03 `tzw1` abolished zwittermicin A production and complementation restored productivity. |
| `PMID:18692050` | Reports that L-2,3-diaminopropionate is one zwittermicin A biosynthetic building block in *Bacillus thuringiensis* subsp. *kurstaki* YBT-1520. |
| `PMID:18798190` | Reports total-synthesis-based assignment of the complete `(+)-zwittermicin A` configuration and implications for D-serine in biosynthesis; no abstract was available through the PubMed search result. |

The broader PubMed search for `"zwittermicin A" OR FYIPKJHNWFVEIR OR
"155547-95-8" OR C15726` returned 20 candidates, but the inspected public
abstract metadata skewed toward genome reports, secondary-metabolite gene
presence, docking, and review mentions. Those newer leads may eventually help
with producer strain curation, but none displaced the ChEBI-listed primary
ZmaR and biosynthetic-cluster papers as the best immediate sources for this
exact record.

## Completeness

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`,
  `molecular_targets`, and `causal_graphs` are absent, so the record has no
  curator-owned antifungal or antibacterial mechanism.
- No `resistance_mechanisms` entry captures the ZmaR self-resistance route,
  acetylation reaction, organism context, or primary biochemical support from
  `PMID:10464220` and `PMID:10521664`.
- No `activity_spectrum` entry captures an exact organism or strain, assay,
  value, qualifier, unit, and per-observation evidence for exact
  `(+)-zwittermicin A`.
- No `producer_organisms` entry captures the *Bacillus cereus* or
  *Bacillus thuringiensis* strain-level producers supported by the ChEBI
  species-of-metabolite row and biosynthetic-cluster papers.

Correctly empty optional slots:

- No `clinical_status` or `clinical_status_assertions`: the ChEBI-only source
  concept and inspected metadata do not assert regulatory use.
- No `datasets`: inspected ChEBI, KEGG, and PubMed metadata did not surface a
  public screening, omics, or structural dataset accession for this exact
  structure.

Ignored-inclusive absence search:

- Ran `rg --hidden --no-ignore` over `curation/`, `data/raw/`,
  `data/antibiotics/`, `reports/yaml_record_review/`, and the full exported
  worklist for `CHEBI:80056`, `(+)-zwittermicin A`, `zwittermicin-a`,
  `FYIPKJHNWFVEIR-FXQWNPMTSA-N`, `155547-95-8`, `C15726`, and `CPD-18237`.
- The search included ignored files and found only the expected generated
  target, `PATHS.tsv`, ChEBI raw row, worklist rows, and the review-queue row.
  It found no prior review report, `curation/decisions.tsv` row, curated
  mechanism decision, or curated activity/provenance addition for this exact
  ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | ZWITTERMICIN-80056-M1 | The record is still a seeded exact-enantiomer stub with antifungal and antimicrobial ChEBI roles but no curator-owned mode of action, mechanism scope, molecular target, resistance route, activity spectrum, producer assertion, or causal graph. | `just review-queue --limit 26` reports `MECHANISM_REVIEW: mechanism is absent` with 10 source literature leads, zero record evidence items, and zero targets; `/tmp/antibioticmech-worklist-zwittermicin-a.tsv` lists `CHEBI:80056` in `mechanism`, `activity-candidate`, and `review-readiness`. ChEBI lists ZmaR, biosynthetic-cluster, and stereochemistry PMIDs, but none of those exact-compound activity, production, or resistance claims has been curated onto the record. | `data/antibiotics/antifungal/zwittermicin-a.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the full text of `PMID:10464220` and `PMID:10521664`, then add a
   claim-local `resistance_mechanisms` entry only to the exact biochemical and
   organism scope they support: ZmaR-mediated acetylation of zwittermicin A and
   high-level self-resistance in a producing *Bacillus* context.
2. Inspect the primary biosynthetic-cluster papers, especially `PMID:14711631`,
   `PMID:17225146`, `PMID:18446411`, and `PMID:18692050`, to add
   strain-scoped `producer_organisms` assertions for exact zwittermicin A
   producers that are experimentally shown to biosynthesize the compound.
3. Use `PMID:17249781` and `PMID:18798190` as stereochemistry leads if future
   work needs to distinguish `(+)-zwittermicin A` from an unspecified or
   opposite-enantiomer claim.
4. Curate exact `activity_spectrum` observations only from primary studies that
   report an activity measurement, organism and strain, assay, value,
   qualifier, unit, and exact zwittermicin A test article.
5. Curate `mode_of_action`, `mode_of_action_target_scope`,
   `mode_of_action_notes`, molecular targets, and a causal graph only to the
   precision directly supported by inspected exact-compound mechanism sources.
6. Preserve the seeded ChEBI identity, `(+)-` stereochemistry, parent
   compounds, xrefs, and source concept. This review found no grounded-identity
   correction that belongs in `data/raw/chebi_antimicrobials.tsv` or
   `data/antibiotics/PATHS.tsv`.

## Follow-up Checks

- `just validate-strict data/antibiotics/antifungal/zwittermicin-a.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-zwittermicin-a.tsv`
- `just review-queue --limit 26`
- `just qc`
- Manual diff review of `data/antibiotics/antifungal/zwittermicin-a.yaml` to
  confirm every new exact-structure claim is claim-local and directly supported
  by an inspected primary source.

## Additional Notes

- `NCBI_EMAIL` was unset in the local environment before using the PubMed
  search script; no contact email was sent as NCBI API metadata.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded finding above.
- KEGG `C15726` names *Bacillus cereus* as an organism for zwittermicin A and
  links UniProt `Q7BQ70`, the ZmaR resistance protein; if this becomes curation
  evidence, cite it as a KEGG database assertion rather than as primary
  literature.
