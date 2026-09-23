# YAML Record Review: (R)-4''-methoxydalbergione

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antiprotozoal/r-4-methoxydalbergione.yaml`
- Started UTC: `2026-09-23T02:15:32Z`
- Finished UTC: `2026-09-23T02:17:20Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:66703` |
| Label | `(R)-4''-methoxydalbergione` |
| Path | `data/antibiotics/antiprotozoal/r-4-methoxydalbergione.yaml` |
| Class | `ANTIPROTOZOAL` |
| Status | `SEEDED` |
| Grounding | `EXACT`, through the `CHEBI` source concept `CHEBI:66703` |
| Structure | `RGSUZUQISVAJJF-GFCCVEGCSA-N`, formula `C16H14O3`, charge `0` |
| Maintained input | `data/raw/chebi_antimicrobials.tsv` |
| Generated or maintained | Generated record under `data/antibiotics`; do not hand-edit seeded identity, class, structure, parent, xref, or source-concept fields |

The full target YAML was read before judgement. `CHEBI:66703` resolves through
`data/antibiotics/PATHS.tsv` to the antiprotozoal record
`data/antibiotics/antiprotozoal/r-4-methoxydalbergione.yaml`.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiprotozoal/r-4-methoxydalbergione.yaml` | Pass; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/antiprotozoal/r-4-methoxydalbergione.yaml --out /tmp/r-4-methoxydalbergione-validate-strict.tsv` | Pass; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Pass; 2,939 records expected and on disk, 0 missing, 0 unexpected, 0 drifted, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `just review-queue --limit 96` | Pass; `CHEBI:66703` remains after the already-reviewed `(M)-viriditoxin`, `(R)-(+)-citronellal`, and `(R)-3-hydroxybutanenitrile` rows with `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just worklist --limit 0 --tsv /tmp/r-4-methoxydalbergione-worklist.tsv` | Pass; the relevant entries were `mechanism`, `producer-candidate`, and `review-readiness`; the record was not queued for minted grounding, xref, multi-component, structure, scope, or target-evidence defects. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --query '"(R)-4-methoxydalbergione" OR "(R)-4''''-methoxydalbergione" OR "14640516"' --limit 20 --output /tmp/r-4-methoxydalbergione-exact-publications.jsonl` | PubMed returned 7 candidates, including `PMID:14640516`; Semantic Scholar returned HTTP 429 and was unavailable for this pass. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --query 'methoxydalbergione Plasmodium antiplasmodial mechanism target Dalbergia louvelii' --limit 20 --output /tmp/r-4-methoxydalbergione-broad-publications.jsonl` | PubMed returned 0 candidates; Semantic Scholar returned HTTP 429 and was unavailable for this pass. |

No narrower single-record term, reference, or history validator is exposed for a
plain ChEBI-seeded record. The bounded absence searches for a prior review,
curator decision, duplicate exact InChIKey, and exact DOI lead used
`rg --no-ignore --hidden` or `find`, so ignored `reports/` files were included.

## Identity and Grounding

The ChEBI import row for `CHEBI:66703` exactly matches the generated identity:

- label `(R)-4''-methoxydalbergione`
- 3-star ChEBI entry with `EXACT` grounding
- antiplasmodial role `CHEBI:64915`
- broader parents `CHEBI:132124` and `CHEBI:47985`
- Standard InChIKey `RGSUZUQISVAJJF-GFCCVEGCSA-N`
- xrefs `cas:28396-75-0`, `cas:4646-86-0`, `kegg.compound:C10505`,
  `knapsack:C00002549`, and `reaxys:2054297`

The ChEBI label and exact synonym list cover the name used by the apparent
primary activity paper: PubMed `PMID:14640516` names `(R)-4''-methoxydalbergione`
as compound 5, with spacing differences around the prime marks but no evidence
of a different stereochemical form.

An ignored-inclusive search over `data/raw`, `data/antibiotics`, `curation`, and
`reports` found the exact InChIKey only in the ChEBI raw row and this generated
YAML record. The same bounded search found the minted source identifier
`antibioticmech:chebi-541bc9955a` only in the generated YAML, with no
`curation/decisions.tsv` override or prior review report.

## Evidence

Existing claim evidence is narrow:

| Claim | Evidence review |
|---|---|
| ChEBI identity, definition, synonyms, role, parent, xrefs, and structure fields | Database-seeded from the `CHEBI:66703` row in `data/raw/chebi_antimicrobials.tsv`; no curator-owned literature citation is required at record level. |
| Definition text saying the compound was isolated from `Dalbergia louveli` heartwood and exhibits antiplasmodial activity | The PubMed abstract for `PMID:14640516` supports the exact compound, `Dalbergia louvelii` heartwood isolation context, and an antiplasmodial IC50 range of 5.8-8.7 uM across four known compounds including `(R)-4''-methoxydalbergione`; full text must be inspected before converting those data into an organism-scoped `ActivityObservation` with this compound's exact IC50. |

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
- `activity_observations` is absent even though `PMID:14640516` reports in
  vitro inhibition of `Plasmodium falciparum`.
- `producer_organisms` is absent. The ChEBI definition names a plant source, and
  the worklist correctly keeps that phrase on `producer-candidate` rather than
  asserting a taxon without a curator checking the spelling, taxon, and whether
  the heartwood isolation supports biosynthesis.
- `resistance_mechanisms`, `clinical_status`, and `datasets` are empty; the
  bounded review did not find local source rows proving these omissions are
  defects.

The exact PMID appears on three ChEBI raw rows, because Beldjoudi et al. also
reported `7,4'-dihydroxy-3'-methoxyisoflavone` and `obtusafuran`; a future
activity curation pass must not copy a co-isolated compound's IC50 onto this
record without checking the full table.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| major | `mode_of_action`, `molecular_targets`, `causal_graphs`, and `activity_observations` are absent even though exact `(R)-4''-methoxydalbergione` antiplasmodial literature exists, so `CHEBI:66703` cannot pass the mechanism criterion for `REVIEWED`. The PubMed abstract for `PMID:14640516` supports the exact compound and an antiplasmodial IC50 range across several compounds, but it does not state a mechanism or enough per-compound assay detail to add an exact activity row from the abstract alone. | Curator-owned additions in `data/antibiotics/antiprotozoal/r-4-methoxydalbergione.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blockers or minor findings were found.

## Recommended Edits

1. Inspect `PMID:14640516` in full text and decide whether
   `(R)-4''-methoxydalbergione` supports a defensible `ActivityObservation`
   against `Plasmodium falciparum`, including the parasite strain, assay, exact
   IC50 value, qualifier, and units.
2. Resolve the `Dalbergia louvelii` plant-source statement to a defensible
   NCBI taxon before adding a `ProducerOrganism`; preserve the source's
   heartwood tissue context in notes because the schema has no tissue slot.
3. Leave `mode_of_action` unset unless full-text primary evidence supports a
   Plasmodium mechanism; add a curator-owned `Discussion` for an unresolved
   mechanism gap if the activity paper has no target or mechanistic assay.
4. Add `molecular_targets` only if a primary source supports a target beyond
   the compound's antiplasmodial phenotype.
5. Add a causal graph only after the activity and any mechanism interpretation
   are resolved; every edge needs its own primary-paper `EvidenceItem`.
6. Leave the seeded identity, xrefs, `parent_compounds`, and class untouched
   unless a ChEBI refresh or `curation/decisions.tsv` row changes the maintained
   import.

## Follow-up Checks

- After any curator-owned edit, rerun
  `just validate-strict data/antibiotics/antiprotozoal/r-4-methoxydalbergione.yaml --out /tmp/antibioticmech-record-validation.tsv`.
- Rerun `just verify-corpus` to prove the generated record still reproduces
  from `data/raw/` plus curator inputs.
- Rerun
  `just worklist --limit 0 --tsv /tmp/r-4-methoxydalbergione-worklist.tsv`
  and confirm the `CHEBI:66703` `mechanism`, `producer-candidate`, and
  `review-readiness` rows changed as intended.
- Rerun `just lint`, `just test`, and `just render-check` through `just qc` if a
  later pass mutates the YAML rather than writing a review report only.

## Additional Notes

- `reports/` is gitignored. This report must be staged with `git add -f`.
- `PMID:14640516` is shared by the `CHEBI:66703`, `CHEBI:65780`, and
  `CHEBI:66804` raw ChEBI rows. The bounded, ignored-inclusive DOI search found
  no committed `10.1021/np030008x` reference.
- The local exact-InChIKey search did not find any other source row or generated
  record with `RGSUZUQISVAJJF-GFCCVEGCSA-N`; ignored `reports` were included.
- Semantic Scholar was rate-limited with HTTP 429 and was not treated as a
  negative source.
