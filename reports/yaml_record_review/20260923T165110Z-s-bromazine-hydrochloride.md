# YAML Record Review: (S)-bromazine hydrochloride

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/unspecified/s-bromazine-hydrochloride.yaml`
- Started UTC: `2026-09-23T16:48:00Z`
- Finished UTC: `2026-09-23T16:51:10Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:59305` |
| Label | `(S)-bromazine hydrochloride` |
| Path | `data/antibiotics/unspecified/s-bromazine-hydrochloride.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Status | `SEEDED` |
| Grounding | `EXACT`, through the `CHEBI` source concept `CHEBI:59305` |
| Structure | `ZQDJSWUEGOYDGT-LMOVPXPDSA-N`, formula `C17H21BrNO.Cl`, charge `0` |
| Drug xref | `drugbank:DB01237` |
| Maintained input | `data/raw/chebi_antimicrobials.tsv` |
| Generated or maintained | Generated record under `data/antibiotics`; do not hand-edit seeded identity, class, structure, parent, drug-xref, or source-concept fields |

The full target YAML was read before judgement. `CHEBI:59305` resolves through
`data/antibiotics/PATHS.tsv` to the unspecified antimicrobial record
`data/antibiotics/unspecified/s-bromazine-hydrochloride.yaml`.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/s-bromazine-hydrochloride.yaml` | Pass; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/s-bromazine-hydrochloride.yaml --out /tmp/s-bromazine-hydrochloride-validate-strict.tsv` | Pass; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Pass; 2,939 records expected and on disk, 0 missing, 0 unexpected, 0 drifted, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/s-bromazine-hydrochloride-worklist.tsv` | Pass; the relevant entries were `mechanism` and `review-readiness`; the record was not queued for minted grounding, xref, multi-component, producer-candidate, activity-candidate, structure, scope, or target-evidence defects. |
| `just review-queue --limit 115` | Pass; `CHEBI:59305` remains queued immediately after the already-reviewed `(S)-bromazine` row with `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --query '"(S)-bromazine hydrochloride" OR "(S)-bromodiphenhydramine hydrochloride" OR "(S)-bromodiphenhydramine HCl" OR "ZQDJSWUEGOYDGT-LMOVPXPDSA-N"' --limit 20 --output /tmp/s-bromazine-hydrochloride-publications.jsonl` | PubMed returned five general bromodiphenhydramine candidates; none of their abstracts named exact `(S)-bromazine hydrochloride`, exact `(S)-bromodiphenhydramine hydrochloride`, or the exact Standard InChIKey. Semantic Scholar returned HTTP 429 and was unavailable for this pass. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --query '"bromazine hydrochloride" OR "bromodiphenhydramine hydrochloride" OR ambodryl antimicrobial antibacterial synergism MIC resistance' --limit 20 --output /tmp/s-bromazine-hydrochloride-broad-pubmed.jsonl` | PubMed returned 5 hydrochloride-name candidates but no antimicrobial activity, target, or mechanism abstract. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --query 'ambodryl' --limit 20 --output /tmp/s-bromazine-hydrochloride-ambodryl-pubmed.jsonl` | PubMed returned older `ambodryl` / bromodiphenhydramine antimicrobial leads; their abstracts do not pin the tested compound to exact `(S)-bromazine hydrochloride`. |

No narrower single-record term, reference, or history validator is exposed for a
plain ChEBI-seeded record. The bounded absence searches for a prior exact
review, curator decision, duplicate exact InChIKey, shared drug-level xref, and
the minted source identifier used `rg --no-ignore --hidden` and `find`, so
ignored `reports/` files were included.

## Identity and Grounding

The ChEBI import row for `CHEBI:59305` exactly matches the generated identity:

- label `(S)-bromazine hydrochloride`
- 3-star ChEBI entry with `EXACT` grounding
- ChEBI role term `CHEBI:33281`
- broader parent `CHEBI:59178`
- Standard InChIKey `ZQDJSWUEGOYDGT-LMOVPXPDSA-N`
- salt formula `C17H21BrNO.Cl` and net charge `0`
- drug-level xref `drugbank:DB01237`

OLS4 resolves `CHEBI:59305` as an active `(S)-bromazine hydrochloride` term,
resolves its hierarchical parent as `CHEBI:59178` / `bromazine hydrochloride`,
and reports reciprocal `is enantiomer of` graph edges between `CHEBI:59305` and
`CHEBI:59304` / `(R)-bromazine hydrochloride`. `CHEBI:33281` resolves as
`antimicrobial agent`, and `data/raw/chebi_role_names.tsv` classifies that term
as a generic `scope` role rather than as a specific antibacterial, antifungal,
antiprotozoal, antiviral, or disinfectant class.

The record denotes the hydrochloride salt of `(S)-bromazine`, not neutral
`(S)-bromazine` `CHEBI:59302`, the racemic hydrochloride `CHEBI:59178`, or
`(R)-bromazine hydrochloride` `CHEBI:59304`.

The exact ChEBI row places `drugbank:DB01237` in `drug_xrefs`, not `xrefs`.
The ignored-inclusive local search found `drugbank:DB01237` on racemic
bromazine, racemic bromazine hydrochloride, `(R)-bromazine hydrochloride`, and
`(S)-bromazine hydrochloride`, which is consistent with a drug-level identifier
that spans several kept-apart structures rather than a same-structure xref.

An ignored-inclusive search over `data/raw`, `data/antibiotics`, `curation`,
and `reports` found the exact InChIKey only in the ChEBI raw row and this
generated YAML record. The same bounded search found the minted source
identifier `antibioticmech:chebi-728f985cbf` only in the generated YAML, with
no `curation/decisions.tsv` override or prior exact review report.

## Evidence

Existing claim evidence is narrow:

| Claim | Evidence review |
|---|---|
| ChEBI identity, definition, synonyms, antimicrobial role, parent, drug xref, and structure fields | Database-seeded from the `CHEBI:59305` row in `data/raw/chebi_antimicrobials.tsv`; no curator-owned literature citation is required at record level. |
| `(S)-bromazine hydrochloride` is parented to bromazine hydrochloride | The ChEBI source row and live OLS4 graph list `CHEBI:59178`, the racemic bromazine hydrochloride record, as the broader parent. That is a strict broader relationship, not an exact xref. |
| `(S)-bromazine hydrochloride` is the enantiomeric counterpart of `(R)-bromazine hydrochloride` | OLS4 reports reciprocal `is enantiomer of` graph edges between `CHEBI:59305` and `CHEBI:59304`; the opposite enantiomer is a related term, not a duplicate identity. |
| `drugbank:DB01237` is a drug-level reference | The same DrugBank accession spans bromazine, bromazine hydrochloride, and both enantiomeric hydrochloride salts in the ChEBI rows; it is therefore correctly retained as `drug_xrefs`, not as exact structural equivalence. |

The record has no `mode_of_action`, `molecular_targets`,
`activity_observations`, `resistance_mechanisms`, `producer_organisms`,
`causal_graphs`, or record-level literature `evidence` items to overstate. No
existing citation is attached to a broader claim than it supports.

The exact-label and exact-InChIKey publication search did not find a
compound-specific mechanism or antimicrobial assay for the isolated
`(S)-bromazine hydrochloride` salt. Bounded broader PubMed searches found older
antimicrobial leads for `ambodryl` / bromodiphenhydramine HCl, including
penicillin synergy, methdilazine synergy, promethazine synergy, and
cross-resistance reports. Those abstracts do not establish that the tested
compound was exact `(S)-bromazine hydrochloride` rather than the racemic salt or
another unspecified bromodiphenhydramine form.

## Completeness

The record is not complete enough for `REVIEWED` because the mechanism gate is
unsettled:

- `mode_of_action` and `mode_of_action_target_scope` are absent.
- `molecular_targets` is absent.
- `causal_graphs` is absent.
- `activity_observations` is absent.
- `producer_organisms` is absent and the full worklist did not nominate a
  producer candidate for this ChEBI seed.
- `resistance_mechanisms`, `clinical_status`, and `datasets` are empty; the
  bounded review did not find local source rows proving these omissions are
  defects.

The exact ChEBI source row has no PMID or DOI lead. Future activity curation
needs primary full text or another exact source before copying MIC, synergy, or
cross-resistance values from `ambodryl` papers, because their abstracts do not
resolve the reported material to this isolated enantiomeric salt.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| major | `mode_of_action`, `molecular_targets`, `causal_graphs`, and `activity_observations` are absent. ChEBI asserts the antimicrobial role for exact `CHEBI:59305`, but the local ChEBI row carries no source PMID/DOI and the bounded PubMed searches found only `ambodryl` or bromodiphenhydramine hydrochloride leads that are not exact `(S)`-salt evidence from their abstracts alone. | Curator-owned additions in `data/antibiotics/unspecified/s-bromazine-hydrochloride.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blockers or minor findings were found.

## Recommended Edits

1. Inspect ChEBI's upstream provenance or primary literature for the isolated
   `(S)` hydrochloride salt and decide whether exact `ActivityObservation` rows
   are supportable.
2. Inspect the `ambodryl` / bromodiphenhydramine HCl antimicrobial leads in
   full text and curate them to the exact racemic or enantiomeric record only
   after resolving the source compound form.
3. Leave `mode_of_action` unset unless a primary source supports a specific
   target or pathway for exact `(S)-bromazine hydrochloride`.
4. Add `molecular_targets` only if primary evidence supports a target beyond
   the source-seeded antimicrobial role.
5. Add a causal graph only after the activity and any mechanism interpretation
   are resolved; every edge needs its own primary-paper `EvidenceItem`.
6. Leave the seeded identity, role, parent, drug xref, and structure untouched
   unless a ChEBI refresh or `curation/decisions.tsv` row changes the maintained
   import.

## Follow-up Checks

- After any curator-owned edit, rerun
  `just validate-strict data/antibiotics/unspecified/s-bromazine-hydrochloride.yaml --out /tmp/antibioticmech-record-validation.tsv`.
- Rerun `just verify-corpus` to prove the generated record still reproduces
  from `data/raw/` plus curator inputs.
- Rerun
  `just worklist --limit 0 --tsv /tmp/s-bromazine-hydrochloride-worklist.tsv`
  and confirm the `CHEBI:59305` `mechanism` and `review-readiness` rows changed
  as intended.
- Rerun `just lint`, `just test`, and `just render-check` through `just qc` if a
  later pass mutates the YAML rather than writing a review report only.

## Additional Notes

- `reports/` is gitignored. This report must be staged with `git add -f`.
- The bounded, ignored-inclusive local search found no committed PMID or DOI
  row for exact `CHEBI:59305`.
- The local exact-InChIKey search did not find any other source row or generated
  record with `ZQDJSWUEGOYDGT-LMOVPXPDSA-N`; ignored `reports` were included.
- Semantic Scholar returned HTTP 429 and was not treated as a negative source.
