# YAML Record Review: (R)-4-hydroxy-1-methyl-L-proline

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antiviral/r-4-hydroxy-1-methyl-l-proline.yaml`
- Started UTC: `2026-09-23T02:46:05Z`
- Finished UTC: `2026-09-23T02:50:51Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:134543` |
| Label | `(R)-4-hydroxy-1-methyl-L-proline` |
| Path | `data/antibiotics/antiviral/r-4-hydroxy-1-methyl-l-proline.yaml` |
| Class | `ANTIVIRAL` |
| Status | `SEEDED` |
| Grounding | `EXACT`, through the `CHEBI` source concept `CHEBI:134543` |
| Structure | `FMIPNAUMSPFTHK-UHNVWZDZSA-N`, formula `C6H11NO3`, charge `0` |
| Maintained input | `data/raw/chebi_antimicrobials.tsv` |
| Generated or maintained | Generated record under `data/antibiotics`; do not hand-edit seeded identity, class, structure, parent, xref, or source-concept fields |

The full target YAML was read before judgement. `CHEBI:134543` resolves through
`data/antibiotics/PATHS.tsv` to the antiviral record
`data/antibiotics/antiviral/r-4-hydroxy-1-methyl-l-proline.yaml`.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiviral/r-4-hydroxy-1-methyl-l-proline.yaml` | Pass; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/antiviral/r-4-hydroxy-1-methyl-l-proline.yaml --out /tmp/r-4-hydroxy-1-methyl-l-proline-validate-strict.tsv` | Pass; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Pass; 2,939 records expected and on disk, 0 missing, 0 unexpected, 0 drifted, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `just review-queue --limit 100` | Pass; `CHEBI:134543` remains immediately after the already-reviewed `(R)-4''-methoxydalbergione` row with `MECHANISM_REVIEW: mechanism is absent; 5 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just worklist --limit 0 --tsv /tmp/r-4-hydroxy-1-methyl-l-proline-worklist.tsv` | Pass; the relevant entries were `mechanism` and `review-readiness`; the record was not queued for minted grounding, xref, multi-component, producer-candidate, activity-candidate, structure, scope, or target-evidence defects. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --query '11199132[uid] OR 12903959[uid] OR 16425210[uid] OR 22071447[uid] OR 26427611[uid]' --limit 20 --output /tmp/r-4-hydroxy-1-methyl-l-proline-pmid-publications.jsonl` | PubMed returned the 5 exact ChEBI source PMID leads. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --query '"4-hydroxy-1-methyl-L-proline" antiviral antibiotic mechanism target' --limit 20 --output /tmp/r-4-hydroxy-1-methyl-l-proline-broad-publications.jsonl` | PubMed returned 0 candidates; Semantic Scholar returned HTTP 429 and was unavailable for this pass. |

No narrower single-record term, reference, or history validator is exposed for a
plain ChEBI-seeded record. The bounded absence searches for a prior review,
curator decision, duplicate exact InChIKey, exact DOI leads, and the minted
source identifier used `rg --no-ignore --hidden` or `find`, so ignored
`reports/` files were included.

## Identity and Grounding

The ChEBI import row for `CHEBI:134543` exactly matches the generated identity:

- label `(R)-4-hydroxy-1-methyl-L-proline`
- 3-star ChEBI entry with `EXACT` grounding
- antiviral role `CHEBI:64947`
- broader parents `CHEBI:26456` and `CHEBI:84186`
- Standard InChIKey `FMIPNAUMSPFTHK-UHNVWZDZSA-N`
- xrefs `chemspider:9943383` and `reaxys:472151`

The ChEBI label and exact synonym list cover the names used by the five source
PMID leads, including `(R)-4-hydroxy-N-methyl-L-proline` and
`N-methyl-trans-4-hydroxy-L-proline`. The apparent direct antiviral paper,
PubMed `PMID:26427611`, names the active molecule as
`N-methyl-trans-4-hydroxy-l-proline (10)`.

An ignored-inclusive search over `data/raw`, `data/antibiotics`, `curation`, and
`reports` found the exact InChIKey only in the ChEBI raw row and this generated
YAML record. The same bounded search found the minted source identifier
`antibioticmech:chebi-1e83c91cd4` only in the generated YAML, with no
`curation/decisions.tsv` override or prior review report.

## Evidence

Existing claim evidence is narrow:

| Claim | Evidence review |
|---|---|
| ChEBI identity, definition, synonyms, role, parent, xrefs, and structure fields | Database-seeded from the `CHEBI:134543` row in `data/raw/chebi_antimicrobials.tsv`; no curator-owned literature citation is required at record level. |
| Antiviral role | `PMID:26427611` supports an exact anti-HIV-1 integrase literature lead for `N-methyl-trans-4-hydroxy-L-proline`: the PubMed abstract reports compound 10 inhibited HIV-1 integrase in a multiplate integration assay with IC50 `11.8 ug/mL` and was docked against HIV-1 integrase. |
| Natural product occurrence | `PMID:11199132` identified this compound from `Aglaia andamanica` leaves; `PMID:22071447`, `PMID:16425210`, and `PMID:12903959` identify the same synonym in plant phytochemistry or structural-correction contexts but do not report an antiviral mechanism for this compound in their PubMed abstracts. |

The record has no `mode_of_action`, `molecular_targets`,
`activity_observations`, `resistance_mechanisms`, `producer_organisms`,
`causal_graphs`, or record-level literature `evidence` items to overstate. No
existing citation is attached to a broader claim than it supports.

## Completeness

The record is not complete enough for `REVIEWED` because the mechanism gate is
unsettled:

- `mode_of_action` and `mode_of_action_target_scope` are absent.
- `molecular_targets` is absent even though the source PMID list contains an
  exact anti-HIV-1 integrase in vitro assay lead.
- `causal_graphs` is absent.
- `activity_observations` is absent even though `PMID:26427611` reports HIV-1
  integrase inhibition for this compound.
- `producer_organisms` is absent. The PubMed leads identify several plant
  source contexts, but this review did not check the full texts or NCBI taxa
  needed to decide whether any source plant should be asserted as a producer.
- `resistance_mechanisms`, `clinical_status`, and `datasets` are empty; the
  bounded review did not find local source rows proving these omissions are
  defects.

Only `PMID:26427611` is a direct antiviral lead in the PubMed abstracts. The
other ChEBI source PMIDs are useful identity or isolation leads but should not
be reused as evidence for HIV-1 integrase activity.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| major | `mode_of_action`, `molecular_targets`, `causal_graphs`, and `activity_observations` are absent even though an exact anti-HIV-1 integrase paper exists for `N-methyl-trans-4-hydroxy-L-proline`. The PubMed abstract for `PMID:26427611` reports in vitro HIV-1 integrase inhibition with IC50 `11.8 ug/mL` and a docking model against HIV-1 integrase, but the generated record does not yet capture the assay, target, or causal interpretation. | Curator-owned additions in `data/antibiotics/antiviral/r-4-hydroxy-1-methyl-l-proline.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blockers or minor findings were found.

## Recommended Edits

1. Inspect `PMID:26427611` in full text and decide whether compound 10 supports
   a defensible `ActivityObservation`, including the HIV-1 integrase assay,
   exact IC50 value, qualifier, and units.
2. Convert the reported `11.8 ug/mL` IC50 to a molar standard only if the schema
   and curation policy allow a derived concentration from the ChEBI molecular
   weight; otherwise preserve the primary unit in the observation.
3. Add a molecular target for HIV-1 integrase only after checking whether the
   full text names a specific HIV-1 integrase construct or accession and whether
   the enzyme assay plus docking are enough to support target causality.
4. Keep `PMID:11199132`, `PMID:22071447`, `PMID:16425210`, and `PMID:12903959`
   scoped to isolation or identity evidence unless their full texts report an
   antimicrobial phenotype for this compound.
5. Add a causal graph only after the activity and any HIV-1 integrase mechanism
   interpretation are resolved; every edge needs its own primary-paper
   `EvidenceItem`.
6. Leave the seeded identity, xrefs, `parent_compounds`, and class untouched
   unless a ChEBI refresh or `curation/decisions.tsv` row changes the maintained
   import.

## Follow-up Checks

- After any curator-owned edit, rerun
  `just validate-strict data/antibiotics/antiviral/r-4-hydroxy-1-methyl-l-proline.yaml --out /tmp/antibioticmech-record-validation.tsv`.
- Rerun `just verify-corpus` to prove the generated record still reproduces
  from `data/raw/` plus curator inputs.
- Rerun
  `just worklist --limit 0 --tsv /tmp/r-4-hydroxy-1-methyl-l-proline-worklist.tsv`
  and confirm the `CHEBI:134543` `mechanism` and `review-readiness` rows
  changed as intended.
- Rerun `just lint`, `just test`, and `just render-check` through `just qc` if a
  later pass mutates the YAML rather than writing a review report only.

## Additional Notes

- `reports/` is gitignored. This report must be staged with `git add -f`.
- The initial exact-name PubMed search returned irrelevant numeric free-text
  matches; exact ChEBI source PMIDs were then rerun with PubMed `[uid]` terms.
- The bounded, ignored-inclusive DOI search found no committed copies of
  `10.3109/13880209.2015.1071413`, `10.3390/molecules16119397`,
  `10.1002/mrc.1783`, `10.1021/jf0341722`, or `10.1055/s-2000-9901`.
- Semantic Scholar was rate-limited with HTTP 429 and was not treated as a
  negative source.
