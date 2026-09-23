# YAML Record Review: (R)-3-hydroxybutanenitrile

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antifungal/r-3-hydroxybutanenitrile.yaml`
- Started UTC: `2026-09-23T01:43:08Z`
- Finished UTC: `2026-09-23T01:46:46Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:141345` |
| Label | `(R)-3-hydroxybutanenitrile` |
| Path | `data/antibiotics/antifungal/r-3-hydroxybutanenitrile.yaml` |
| Class | `ANTIFUNGAL` |
| Status | `SEEDED` |
| Grounding | `EXACT`, through the `CHEBI` source concept `CHEBI:141345` |
| Structure | `BYJAJQGCMSBKPB-SCSAIBSYSA-N`, formula `C4H7NO`, charge `0` |
| Maintained input | `data/raw/chebi_antimicrobials.tsv` |
| Generated or maintained | Generated record under `data/antibiotics`; do not hand-edit seeded identity, class, structure, parent, xref, or source-concept fields |

The full target YAML was read before judgement. `CHEBI:141345` resolves through
`data/antibiotics/PATHS.tsv` to the antifungal record
`data/antibiotics/antifungal/r-3-hydroxybutanenitrile.yaml`.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/r-3-hydroxybutanenitrile.yaml` | Pass; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/r-3-hydroxybutanenitrile.yaml --out /tmp/r-3-hydroxybutanenitrile-validate-strict.tsv` | Pass; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Pass; 2,939 records expected and on disk, 0 missing, 0 unexpected, 0 drifted, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `just review-queue --limit 92` | Pass; `CHEBI:141345` remains after the already-reviewed `(M)-viriditoxin` and `(R)-(+)-citronellal` rows with `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just worklist --limit 0 --tsv /tmp/r-3-hydroxybutanenitrile-worklist.tsv` | Pass; the relevant entries were `mechanism`, `producer-candidate`, `activity-candidate`, and `review-readiness`; the record was not queued for minted grounding, xref, multi-component, structure, scope, or target-evidence defects. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --query '"(R)-3-hydroxybutanenitrile" OR "(3R)-3-hydroxybutyronitrile" OR "125103-95-9"' --limit 20 --output /tmp/r-3-hydroxybutanenitrile-exact-publications.jsonl` | PubMed returned 20 noisy candidates; Semantic Scholar returned HTTP 429 and was unavailable for this pass. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --query '3-hydroxybutanenitrile 3-hydroxybutyronitrile Aspergillus antifungal phytopathogenic fungi' --limit 20 --output /tmp/r-3-hydroxybutanenitrile-broad-publications.jsonl` | PubMed returned 0 candidates; Semantic Scholar returned HTTP 429 and was unavailable for this pass. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --query '10.1080/14786419.2014.904308' --limit 5 --output /tmp/r-3-hydroxybutanenitrile-doi-publications.jsonl` | PubMed returned `PMID:24708541`, the apparent Aspergillus sp. KJ-9 activity source; Semantic Scholar returned HTTP 429 and was unavailable for this pass. |

No narrower single-record term, reference, or history validator is exposed for a
plain ChEBI-seeded record. The bounded absence searches for a prior review,
curator decision, duplicate exact InChIKey, and exact DOI/PMID lead used
`rg --no-ignore --hidden` or `find`, so ignored `reports/` files were included.

## Identity and Grounding

The ChEBI import row for `CHEBI:141345` exactly matches the generated identity:

- label `(R)-3-hydroxybutanenitrile`
- 3-star ChEBI entry with `EXACT` grounding
- antifungal role `CHEBI:35718`
- broader parent `CHEBI:142961`
- Standard InChIKey `BYJAJQGCMSBKPB-SCSAIBSYSA-N`
- xref `cas:125103-95-9`

The synonym list carries the variant name used in the apparent primary lead:
PubMed `PMID:24708541` names compound 7 as `(R)-3-hydroxybutanonitrile`, matching
an exact ChEBI synonym on this record.

An ignored-inclusive search over the repository found the exact InChIKey only in
the ChEBI raw row, this generated YAML record, and its generated HTML page. An
ignored-inclusive search found the minted source identifier
`antibioticmech:chebi-0fd0db1225` only in the generated YAML and generated HTML,
with no `curation/decisions.tsv` override or prior review report.

## Evidence

Existing claim evidence is narrow:

| Claim | Evidence review |
|---|---|
| ChEBI identity, definition, synonyms, role, parent, xref, and structure fields | Database-seeded from the `CHEBI:141345` row in `data/raw/chebi_antimicrobials.tsv`; no curator-owned literature citation is required at record level. |
| Definition text saying the metabolite was isolated from `Aspergillus sp. KJ-9` and active against phytopathogenic fungi | The PubMed abstract for `PMID:24708541` supports this at the discovery-abstract level, including an MIC range of 6.25-50 uM for compound 7 against almost all tested phytopathogenic fungi; full text must be inspected before converting those data into organism-scoped `ActivityObservation` entries. |

The record has no `mode_of_action`, `molecular_targets`,
`activity_observations`, `resistance_mechanisms`, `producer_organisms`,
`causal_graphs`, or record-level literature `evidence` items to overstate. No
existing citation is attached to a broader claim than it supports.

## Completeness

The record is not complete enough for `REVIEWED` because the mechanism gate is
unsettled:

- `mode_of_action` and `mode_of_action_target_scope` are absent.
- `molecular_targets` is absent.
- `causal_graphs` is absent.
- `activity_observations` is absent even though `PMID:24708541` reports MIC
  values for the exact compound against phytopathogenic fungi.
- `producer_organisms` is absent. The definition names `Aspergillus sp. KJ-9`,
  but the worklist correctly keeps that source phrase on
  `producer-candidate` rather than silently asserting a binomial species.
- `resistance_mechanisms`, `clinical_status`, and `datasets` are empty; the
  bounded review did not find local source rows proving these omissions are
  defects.

PubMed DOI lookup found a primary discovery/activity lead that a future
curation pass must inspect in full text before asserting a target, producer, or
activity observation:

| PMID | Relevance |
|---|---|
| `PMID:24708541` | Exact `(R)-3-hydroxybutanonitrile` paper from `Aspergillus sp. KJ-9`; its abstract reports MIC values for compound 7 against several phytopathogenic fungi but does not assign a mode of action. |

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| major | `mode_of_action`, `molecular_targets`, `causal_graphs`, and `activity_observations` are absent even though exact `(R)-3-hydroxybutanenitrile` antifungal literature exists, so `CHEBI:141345` cannot pass the mechanism criterion for `REVIEWED`. The PubMed abstract for `PMID:24708541` supports the organism/source and an MIC range, but it does not state a mechanism and must be full-text-checked before adding per-organism MIC rows. | Curator-owned additions in `data/antibiotics/antifungal/r-3-hydroxybutanenitrile.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blockers or minor findings were found.

## Recommended Edits

1. Inspect `PMID:24708541` in full text and decide whether
   `(R)-3-hydroxybutanenitrile` supports a specific `mode_of_action`, an
   explicitly unknown mechanism, or a curator-owned `Discussion` documenting an
   unresolved mechanism gap.
2. Add `ActivityObservation` entries from `PMID:24708541` only for claims with
   organism or strain scope, activity calls, assay methods, MIC values, and MIC
   units.
3. Resolve `Aspergillus sp. KJ-9` to a defensible NCBI taxon before adding a
   `ProducerOrganism`; if the species cannot be resolved, keep the producer
   claim as an unresolved candidate.
4. Add a causal graph only after the mode interpretation is resolved; every edge
   needs its own primary-paper `EvidenceItem`.
5. Leave the seeded identity, xref, `parent_compounds`, and class untouched
   unless a ChEBI refresh or `curation/decisions.tsv` row changes the
   maintained import.

## Follow-up Checks

- After any curator-owned edit, rerun
  `just validate-strict data/antibiotics/antifungal/r-3-hydroxybutanenitrile.yaml --out /tmp/antibioticmech-record-validation.tsv`.
- Rerun `just verify-corpus` to prove the generated record still reproduces
  from `data/raw/` plus curator inputs.
- Rerun
  `just worklist --limit 0 --tsv /tmp/r-3-hydroxybutanenitrile-worklist.tsv`
  and confirm the `CHEBI:141345` `mechanism`, `producer-candidate`,
  `activity-candidate`, and `review-readiness` rows changed as intended.
- Rerun `just lint`, `just test`, and `just render-check` through `just qc` if a
  later pass mutates the YAML rather than writing a review report only.

## Additional Notes

- `reports/` is gitignored. This report must be staged with `git add -f`.
- `PMID:24708541` is absent from the `CHEBI:141345` raw row and generated YAML,
  but it is already imported on the neighboring `CHEBI:133759` fonsecinone A
  row because the same paper also covered fonsecinone A. The ignored-inclusive
  DOI search found no committed `10.1080/14786419.2014.904308` reference.
- The local exact-InChIKey search did not find any other source row or generated
  record with `BYJAJQGCMSBKPB-SCSAIBSYSA-N`; ignored `reports` were included.
- Semantic Scholar was rate-limited with HTTP 429 and was not treated as a
  negative source.
