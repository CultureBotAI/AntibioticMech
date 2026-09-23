# YAML Record Review: (R)-butaconazole

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antifungal/r-butaconazole.yaml`
- Started UTC: `2026-09-23T04:59:00Z`
- Finished UTC: `2026-09-23T05:03:27Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:59287` |
| Label | `(R)-butaconazole` |
| Path | `data/antibiotics/antifungal/r-butaconazole.yaml` |
| Class | `ANTIFUNGAL` |
| Status | `SEEDED` |
| Grounding | `EXACT`, through the `CHEBI` source concept `CHEBI:59287` |
| Structure | `SWLMUYACZKCSHZ-MRXNPFEDSA-N`, formula `C19H17Cl3N2S`, charge `0` |
| ChEBI roles | `CHEBI:35718`, `CHEBI:86327`, `CHEBI:75282` |
| Maintained input | `data/raw/chebi_antimicrobials.tsv` |
| Generated or maintained | Generated record under `data/antibiotics`; do not hand-edit seeded identity, class, structure, parent, xref, mode, scope, or source-concept fields |

The full target YAML was read before judgement. `CHEBI:59287` resolves through
`data/antibiotics/PATHS.tsv` to the antifungal record
`data/antibiotics/antifungal/r-butaconazole.yaml`.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/r-butaconazole.yaml` | Pass; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/r-butaconazole.yaml --out /tmp/r-butaconazole-validate-strict.tsv` | Pass; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Pass; 2,939 records expected and on disk, 0 missing, 0 unexpected, 0 drifted, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `just review-queue --limit 125` | Pass; `CHEBI:59287` is queued immediately after the already-reviewed `(R)-bromazine hydrochloride` row with `MECHANISM_REVIEW: mechanism is source-seeded and not curator-checked; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just worklist --limit 0 --tsv /tmp/r-butaconazole-worklist.tsv` | Pass; the relevant entries were `mechanism` and `review-readiness`; the record was not queued for minted grounding, xref, multi-component, producer-candidate, activity-candidate, structure, scope, or target-evidence defects. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --query '"(R)-butoconazole" OR "(R)-butaconazole" OR "1-{(2R)-4-(4-chlorophenyl)-2-[(2,6-dichlorophenyl)sulfanyl]butyl}-1H-imidazole"' --limit 20` | PubMed returned racemic butoconazole clinical, plasma, and broad in-vitro activity leads, including `PMID:30425538`, `PMID:24939312`, and `PMID:6094418`; Semantic Scholar returned HTTP 429 and was unavailable for this pass. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --query '"SWLMUYACZKCSHZ-MRXNPFEDSA-N" OR "1-{(2R)-4-(4-chlorophenyl)-2-[(2,6-dichlorophenyl)sulfanyl]butyl}-1H-imidazole"' --limit 20` | PubMed found no exact InChIKey or exact IUPAC candidates; Semantic Scholar returned HTTP 429 and was unavailable for this pass. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --query 'butoconazole ERG11 CYP51 lanosterol demethylase ergosterol Candida resistance MIC' --limit 20` | PubMed found no candidate; Semantic Scholar returned HTTP 429 and was unavailable for this pass. |

No narrower single-record term, reference, or history validator is exposed for a
plain ChEBI-seeded record. The bounded absence searches for a prior review,
curator decision, duplicate exact InChIKey, and the minted source identifier
used `rg --no-ignore --hidden`, so ignored `reports/` files were included.

## Identity and Grounding

The ChEBI import row for `CHEBI:59287` exactly matches the generated identity:

- label `(R)-butaconazole`
- 3-star ChEBI entry with `EXACT` grounding
- ChEBI role terms `CHEBI:35718`, `CHEBI:86327`, and `CHEBI:75282`
- broader parent `CHEBI:3240`
- Standard InChIKey `SWLMUYACZKCSHZ-MRXNPFEDSA-N`
- neutral formula `C19H17Cl3N2S` and charge `0`
- same-structure xref `reaxys:6374956`

The record denotes the neutral `(R)` enantiomer of butoconazole, not racemic
butoconazole `CHEBI:3240`, racemic butoconazole nitrate `CHEBI:3241`, the
opposite `(S)` enantiomer `CHEBI:59288`, the `(R)` nitrate salt `CHEBI:59289`,
or the `(S)` nitrate salt `CHEBI:59290`. The broader racemate and salt records
carry DrugBank, KEGG, CAS, and other xrefs that ChEBI does not assert for the
isolated `(R)` free base, so the generated record correctly imports only the
one same-structure Reaxys xref from exact `CHEBI:59287`.

The antifungal class and source-seeded mechanism follow configured ChEBI role
mappings. `CHEBI:35718` and `CHEBI:86327` map to `ANTIFUNGAL`, while the
`CHEBI:75282` ergosterol-biosynthesis-inhibitor role maps to
`ERGOSTEROL_PATHWAY_INHIBITION` with `HOST_SHARED_TARGET` target scope. The
scope is mechanically consistent with `conf/sources.yaml`: ChEBI names
ergosterol biosynthesis as a fungal pathway, but the local scope mapping treats
this as host-shared until a curator promotes a microorganism-specific enzyme,
organism, or resistance determinant.

An ignored-inclusive search over `data/raw`, `data/antibiotics`, `curation`,
and `reports/yaml_record_review` found the exact InChIKey only in the ChEBI raw
row and this generated YAML record. The same bounded search found the minted
source identifier `antibioticmech:chebi-5a1fa7ad9f` only in the generated YAML,
with no `curation/decisions.tsv` override or prior exact review report.

## Evidence

Existing claim evidence is narrow:

| Claim | Evidence review |
|---|---|
| ChEBI identity, definition, role, parent, structure, and same-structure xref fields | Database-seeded from the `CHEBI:59287` row in `data/raw/chebi_antimicrobials.tsv`; no curator-owned literature citation is required at record level. |
| `(R)-butaconazole` is parented to butoconazole | The ChEBI source row lists `CHEBI:3240`, the racemic butoconazole record, as the broader parent. That is a strict broader relationship, not an exact xref. |
| `ERGOSTEROL_PATHWAY_INHIBITION` and `HOST_SHARED_TARGET` | Source-seeded from ChEBI role `CHEBI:75282`; the local ChEBI row carries no PMID or DOI source-literature lead for the exact `(R)` enantiomer. |

The record has no `molecular_targets`, `activity_observations`,
`resistance_mechanisms`, `producer_organisms`, `causal_graphs`, or
record-level literature `evidence` items. No existing citation is attached to a
broader claim than it supports.

The exact-label search did not find a compound-specific mechanism or antifungal
assay for the isolated neutral `(R)` enantiomer. It returned racemic
butoconazole or butoconazole-nitrate leads: `PMID:30425538`, a Bayesian network
meta-analysis of vulvovaginal candidiasis clinical trials; `PMID:24939312`, a
plasma LC-MS/MS pharmacokinetic method for butoconazole nitrate suppositories;
and `PMID:6094418`, a 1984 relative-inhibition-factor study that tested
butoconazole among other antifungal agents against Candida, Aspergillus, and
dermatophyte isolates. The bounded exact InChIKey, exact IUPAC, and
ERG11/CYP51/lanosterol-demethylase mechanism searches did not return a PubMed
source for exact `CHEBI:59287`.

## Completeness

The record is not complete enough for `REVIEWED` because the source-seeded
ergosterol pathway claim has not been checked against primary evidence for the
exact `(R)` enantiomer:

- `molecular_targets` is absent.
- `activity_observations` is absent.
- `causal_graphs` is absent.
- `producer_organisms` is absent and the full worklist did not nominate a
  producer candidate for this ChEBI seed.
- `resistance_mechanisms`, `clinical_status`, and `datasets` are empty; the
  bounded review did not find local source rows proving these omissions are
  defects.

The exact ChEBI source row has no PMID or DOI lead. Future activity curation
needs primary full text or another exact source before copying MIC values,
clinical-use claims, or sterol-demethylase mechanism details from racemic
butoconazole or racemic butoconazole nitrate onto isolated `(R)-butoconazole`.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| major | `mode_of_action` and `mode_of_action_target_scope` are still source-seeded rather than curator-checked, and the record has no `molecular_targets`, `activity_observations`, or `causal_graphs`. ChEBI asserts `CHEBI:75282` for exact `CHEBI:59287`, but the local ChEBI row carries no source PMID/DOI and the bounded PubMed searches found only racemic butoconazole or butoconazole-nitrate leads rather than exact `(R)-butoconazole` mechanism evidence. | Curator-owned additions in `data/antibiotics/antifungal/r-butaconazole.yaml`, written through `record_curation_event` and `write_validated_antibiotic`; if ChEBI later changes this term's role or source xrefs, the ChEBI inventory extractor owns that refresh. |

No blockers or minor findings were found.

## Recommended Edits

1. Inspect ChEBI's upstream provenance for `CHEBI:59287` and decide whether the
   exact `(R)` enantiomer has primary literature behind its
   `CHEBI:75282` role.
2. Inspect racemic butoconazole and butoconazole-nitrate antifungal leads only
   as parent and salt follow-up. Curate them to `CHEBI:3240`, `CHEBI:3241`,
   `CHEBI:59289`, or another exact record only if the source compound form is
   explicit.
3. Replace or confirm the source-seeded `mode_of_action` only if primary text
   supports an exact `(R)-butoconazole` ergosterol-biosynthesis or
   sterol-demethylase mechanism claim.
4. Add `molecular_targets`, `activity_observations`, and causal-graph edges
   only after an exact source resolves target, assay unit, organism or strain,
   and compound-form scope.
5. Leave the seeded identity, parent, same-structure xref, and structure
   untouched unless a ChEBI refresh or `curation/decisions.tsv` row changes the
   maintained import.

## Follow-up Checks

- After any curator-owned edit, rerun
  `just validate-strict data/antibiotics/antifungal/r-butaconazole.yaml --out /tmp/antibioticmech-record-validation.tsv`.
- Rerun `just verify-corpus` to prove the generated record still reproduces
  from `data/raw/` plus curator inputs.
- Rerun `just worklist --limit 0 --tsv /tmp/r-butaconazole-worklist.tsv` and
  confirm the `CHEBI:59287` `mechanism` and `review-readiness` rows changed as
  intended.
- Rerun `just lint`, `just test`, and `just render-check` through `just qc` if a
  later pass mutates the YAML rather than writing a review report only.

## Additional Notes

- `reports/` is gitignored. This report must be staged with `git add -f`.
- The bounded, ignored-inclusive local search found no committed PMID or DOI
  row for exact `CHEBI:59287`.
- The local exact-InChIKey search did not find any other source row or
  generated record with `SWLMUYACZKCSHZ-MRXNPFEDSA-N`; ignored `reports`
  were included.
- Semantic Scholar was rate-limited with HTTP 429 and was not treated as a
  negative source.
