# YAML Record Review: (13R)-13-dihydrocarminomycin

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/unspecified/13r-13-dihydrocarminomycin.yaml`
- Started UTC: 2026-09-21T18:36:00Z
- Finished UTC: 2026-09-21T18:40:08Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:31058` |
| Label | `(13R)-13-dihydrocarminomycin` |
| Path | `data/antibiotics/unspecified/13r-13-dihydrocarminomycin.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Source concept | `CHEBI:31058` / `(13R)-13-dihydrocarminomycin` |
| Minted source key | `antibioticmech:chebi-77c8e114bc` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv`; future seeded identity, structure, class, role, synonym, or xref changes belong upstream rather than as hand edits. |

Resolution:

- `curation/record_review_queue.tsv:29` names `CHEBI:31058`, label
  `(13R)-13-dihydrocarminomycin`, the five source literature leads
  `PMID:1037188|PMID:623453|PMID:6889513|PMID:7083181|PMID:7181464`, and
  the review hint `MECHANISM_REVIEW: mechanism is absent`.
- `data/antibiotics/PATHS.tsv:756` maps `CHEBI:31058` to the
  `ANTIMICROBIAL_UNSPECIFIED` directory and `13r-13-dihydrocarminomycin` slug.
- `data/raw/chebi_antimicrobials.tsv:621` is the ChEBI source row that seeds
  the target record.
- The whole 67-line target YAML was read before judging generated identity,
  structure, xrefs, source concept, and curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/13r-13-dihydrocarminomycin.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/13r-13-dihydrocarminomycin.yaml --out /tmp/antibioticmech-dihydrocarminomycin-31058-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2939 expected records, 2939 on disk, no missing, unexpected, or drifted records, no identifiers absent from `PATHS.tsv`, and no stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-dihydrocarminomycin-31058.tsv` | Passed; `CHEBI:31058` appears in `mechanism`, `producer-candidate`, and `review-readiness`. |
| `just review-queue --limit 29` | Passed and confirmed `CHEBI:31058` remains in the review-readiness queue as `MECHANISM_REVIEW`, with seven source literature leads, zero record evidence items, and zero targets. |

No narrower term, reference, or curation-history validator is exposed for this
single ChEBI-seeded record. The focused strict validator covered closed schema
shape, and `verify-corpus` covered drift from the maintained raw and PATHS
inputs.

## Identity and Grounding

The seeded identity is consistent with the authoritative ChEBI and KEGG
records:

| Assertion | Record value | Check |
|---|---|---|
| ChEBI identity | `CHEBI:31058`, `(13R)-13-dihydrocarminomycin` | Official ChEBI resolved `CHEBI:31058` to the same compound, with the same ASCII name. |
| Definition | An anthracycline antibiotic that is a cardiotoxic metabolite of carminomycin obtained by formal reduction of the carbonyl group | Matched ChEBI. |
| Formula and charge | `C26H29NO10`, charge `0` | Matched ChEBI; KEGG `C12431` also reports formula `C26H29NO10`. |
| Masses | average `515.515`, monoisotopic `515.17915` | Matched ChEBI; KEGG `C12431` reports exact mass `515.1791` and molecular weight `515.51`. |
| SMILES | `C[C@@H]1O[C@@H](O[C@H]2C[C@](O)([C@@H](C)O)Cc3c(O)c4c(c(O)c32)C(=O)c2c(O)cccc2C4=O)C[C@H](N)[C@@H]1O` | Matched ChEBI. |
| Standard InChI | `InChI=1S/C26H29NO10/c1-9-21(30)13(27)6-16(36-9)37-15-8-26(35,10(2)28)7-12-18(15)25(34)20-19(23(12)32)22(31)11-4-3-5-14(29)17(11)24(20)33/h3-5,9-10,13,15-16,21,28-30,32,34-35H,6-8,27H2,1-2H3/t9-,10+,13-,15-,16-,21+,26-/m0/s1` | Matched ChEBI. |
| InChIKey | `YXBSCYMMPXQFDS-LBIZDXDESA-N` | Matched ChEBI. |
| Antimicrobial role | `CHEBI:33281` | ChEBI asserts `has role` to `antimicrobial agent`. |
| Parent compounds | `CHEBI:22507`, `CHEBI:25830`, `CHEBI:49322`, `CHEBI:51286` | ChEBI asserts the same `is a` relationships to aminoglycoside antibiotic, *p*-quinones, anthracycline antibiotic, and tetracenequinones. |
| IUPAC name and synonyms | The long `(1S,3S)-...` IUPAC name plus `Antibiotic 32999RP`, `Carminomycinol`, `Dihydrocarminomycin`, `Dihydrokarminomycin`, and `RP-32999` | Matched ChEBI. |
| Xrefs | `cas:62182-86-9`, `kegg.compound:C12431`, `metacyc.compound:CPD-15736` | Matched ChEBI's xref rows; KEGG `C12431` names `13-Dihydrocarminomycin`, links back to `ChEBI: 31058`, and carries CAS `62182-86-9`. |

ChEBI also asserts non-antimicrobial `antineoplastic agent`, `cardiotoxic
agent`, `drug metabolite`, and `metabolite` roles. The seeded AntibioticMech
record correctly retains only the `antimicrobial agent` role that drives
inclusion in this repository, and this review found no identity evidence that
the record should move out of the `ANTIMICROBIAL_UNSPECIFIED` filing class.

The target is the neutral exact `CHEBI:31058` structure, not the conjugate-acid
record `CHEBI:140330`, its functional parent `CHEBI:31359` / carminomycin, or
the adjacent ChEBI records for `10-carboxy-13-deoxycarminomycin` and
`13-deoxycarminomycin`.

## Evidence

The target record has no record-level `evidence`. That is allowed for a
ChEBI-seeded record because the ChEBI source concept supplies provenance, and
there are no `activity_spectrum`, `molecular_targets`,
`resistance_mechanisms`, `producer_organisms`, `clinical_status_assertions`,
`datasets`, or `causal_graphs` that would require claim-level evidence.

`data/raw/chebi_antimicrobials.tsv:621` carries seven PubMed leads imported
from ChEBI for the exact source concept. Five of those also appear in the
review-readiness queue. Their public abstracts support leads rather than any
completed claim-local record field:

| PMID | Public abstract support |
|---|---|
| `PMID:1037188` | Reports preparing a dihydro derivative of karminomycin by chemical reduction with potassium borohydride and comparing intravenous antitumor activity in mice. The public abstract supports exact-compound synthesis and antitumor/toxicity follow-up, not a microbial activity measurement. |
| `PMID:623453` | Compares cardiotoxicity of rubomycin, carminomycin, and dihydrocarminomycin in albino mice. The public abstract supports the cardiotoxic role, not antimicrobial activity. |
| `PMID:6889513` | Measures plasma carminomycin and carminomycinol in humans by high-pressure liquid chromatography after intravenous carminomycin. The public abstract supports a carminomycin metabolite lead, not antimicrobial activity. |
| `PMID:7083181` | Reports a phase I carminomycin clinical pharmacology study and says carminomycin is rapidly metabolized to carminomycinol. The public abstract supports a carminomycin metabolite lead, not antimicrobial activity. |
| `PMID:7181464` | Measures carminomycin and 13-dihydrocarminomycin in patient blood plasma by high-efficiency liquid chromatography. The public abstract supports a metabolite assay lead, not antimicrobial activity. |
| `PMID:7251757` | Describes a fluorometric HPLC method for carminomycin and the major metabolite carminomycinol in serum from cancer patients after intravenous carminomycin. The public abstract supports a metabolite assay lead, not antimicrobial activity. |
| `PMID:7307236` | Reports carminomycin pharmacokinetics in dogs and humans and says carminomycinol concentrations rapidly surpassed carminomycin levels. The public abstract supports a pharmacokinetic metabolite lead, not antimicrobial activity. |

Focused PubMed searches for exact synonyms surfaced producer and biosynthesis
leads for future full-text review. `PMID:11910122` reports *Streptomyces
peucetius* mutants that accumulated 13-dihydrocarminomycin in culture
filtrates. `PMID:9098063` and `PMID:9864343` report that the *Streptomyces*
DoxA cytochrome P450 can hydroxylate 13-deoxycarminomycin to
13-dihydrocarminomycin or oxidize 13-dihydrocarminomycin. `PMID:8360627`
reports a carminomycin 4-*O*-methyltransferase from *Streptomyces* sp. strain
C5 that acts on 13-dihydrocarminomycin. Those abstracts support bounded
biosynthesis follow-up work, but they do not by themselves establish which
species and strain biosynthesize this exact ChEBI structure naturally enough to
write a `producer_organisms` entry.

None of the inspected public abstracts supplied a molecular target, resistance
mechanism, MIC-style activity observation, clinical status assertion, dataset,
or causal edge that could be curated directly into the record without full-text
review.

## Completeness

Consequential gaps:

- `activity_spectrum` is absent; the ChEBI source row carries source leads but
  none has been curated to an exact organism, strain, assay, endpoint, or
  per-observation evidence item for `CHEBI:31058`.
- `mode_of_action`, `mode_of_action_target_scope`, `mode_of_action_notes`,
  `molecular_targets`, and `causal_graphs` are absent, so the record has no
  curator-owned antimicrobial mechanism.
- `producer_organisms` is absent even though exact-synonym PubMed searches found
  *Streptomyces* biosynthesis and mutant-accumulation leads.
- `/tmp/antibioticmech-worklist-dihydrocarminomycin-31058.tsv` lists
  `CHEBI:31058` in `producer-candidate` because the ChEBI definition contains
  the phrase `metabolite of carminomycin`. That text is not an organismal
  biosynthesis claim and should not be promoted directly to a producer row.

Correctly empty optional slots:

- No `resistance_mechanisms`: the record is ChEBI-only and CARD resistance
  routes do not apply.
- No `clinical_status` or `clinical_status_assertions`: inspected ChEBI, KEGG,
  and PubMed metadata did not assert an official regulatory product.
- No `datasets`: inspected ChEBI, KEGG, and PubMed metadata did not surface a
  public screening, omics, or structural dataset accession for this exact
  structure.

Ignored-inclusive absence search:

- Ran `rg --hidden --no-ignore` over `curation/`, `data/raw/`,
  `data/antibiotics/`, `reports/yaml_record_review/`, and the full exported
  worklist for these exact terms: `CHEBI:31058`;
  `13r-13-dihydrocarminomycin`; `(13R)-13-dihydrocarminomycin`;
  `YXBSCYMMPXQFDS-LBIZDXDESA-N`; `62182-86-9`; `C12431`; `CPD-15736`;
  `Antibiotic 32999RP`; `Carminomycinol`; `Dihydrokarminomycin`; and
  `RP-32999`.
- The search included ignored files and found only the expected generated
  target, `PATHS.tsv`, ChEBI raw row, worklist rows, and review-queue row. It
  found no prior review report, `curation/decisions.tsv` row, curated
  mechanism decision, or curated activity/provenance addition for this exact
  ChEBI concept.

## Findings

| Severity | ID | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| Major | DIHYDROCARMINOMYCIN-31058-M1 | The record is still a seeded ChEBI stub with an antimicrobial ChEBI role but no curated antimicrobial activity, exact producer assertion, mode of action, mechanism scope, molecular target, or causal graph. | `just review-queue --limit 29` reports `MECHANISM_REVIEW: mechanism is absent` with seven source literature leads, zero record evidence items, and zero targets; `/tmp/antibioticmech-worklist-dihydrocarminomycin-31058.tsv` lists `CHEBI:31058` in `mechanism`, `producer-candidate`, and `review-readiness`; inspected PubMed abstracts show uncurated antitumor, cardiotoxicity, pharmacokinetic, and *Streptomyces* biosynthesis leads rather than a completed claim-local antimicrobial record. | `data/antibiotics/unspecified/13r-13-dihydrocarminomycin.yaml`, via guarded curator-owned record mutation plus a new `CurationEvent`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect full text behind the older direct ChEBI leads, starting with
   `PMID:1037188` and `PMID:623453`, to determine whether any paper measured
   antimicrobial activity of isolated exact `13-dihydrocarminomycin`, rather
   than only antitumor activity or host cardiotoxicity.
2. Inspect `PMID:11910122`, `PMID:9098063`, `PMID:9864343`, and `PMID:8360627`
   to determine whether a strain-scoped *Streptomyces* `producer_organisms`
   claim is exact enough for `CHEBI:31058`, and to keep mutant accumulation or
   in vitro enzyme conversion separate from natural biosynthesis.
3. Curate `mode_of_action`, `mode_of_action_target_scope`,
   `mode_of_action_notes`, molecular targets, and a causal graph only to the
   precision directly supported by inspected exact-compound antimicrobial
   mechanism sources; do not infer the mechanism from host antitumor use or
   anthracycline class membership alone.
4. Ignore the current `producer-candidate` signal caused only by `metabolite of
   carminomycin` unless a primary source names an actual producing organism or
   strain.
5. Preserve the seeded ChEBI identity, neutral exact structure, parent terms,
   synonyms, xrefs, source concept, and `ANTIMICROBIAL_UNSPECIFIED` filing
   class. This review found no seeded-identity correction that belongs in
   `data/raw/chebi_antimicrobials.tsv` or `data/antibiotics/PATHS.tsv`.

## Follow-up Checks

- `just validate-strict data/antibiotics/unspecified/13r-13-dihydrocarminomycin.yaml --out /tmp/antibioticmech-record-validation.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-dihydrocarminomycin-31058.tsv`
- `just review-queue --limit 29`
- `just qc`
- Manual diff review of
  `data/antibiotics/unspecified/13r-13-dihydrocarminomycin.yaml` to confirm
  every antimicrobial activity, producer, dataset, or mechanism claim is
  claim-local and directly supported by an inspected primary source or durable
  dataset.

## Additional Notes

- `NCBI_EMAIL` was unset in the local environment before using the PubMed
  search script; no contact email was sent as NCBI API metadata.
- The review avoided SerpAPI/Google Scholar because that path can be billable
  and was not necessary to establish the bounded finding above.
- Search result metadata was used only to triage source leads. No candidate
  abstract was treated as claim-local evidence for a record field that would
  require exact activity, taxon, strain, or mechanism context from the inspected
  primary source.
