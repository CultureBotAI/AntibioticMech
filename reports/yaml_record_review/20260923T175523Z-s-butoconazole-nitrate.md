# YAML Record Review: (S)-butoconazole nitrate

- Repository: AntibioticMech
- Record: `data/antibiotics/antifungal/s-butoconazole-nitrate.yaml`
- Started UTC: 2026-09-23T17:52:45Z
- Finished UTC: 2026-09-23T17:55:23Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/antibiotics/antifungal/s-butoconazole-nitrate.yaml` |
| Identifier | `CHEBI:59290` |
| Label | `(S)-butoconazole nitrate` |
| Class | `ANTIFUNGAL` |
| Grounding | `EXACT` |
| Status | `SEEDED` |
| Source concept | `CHEBI:59290` from ChEBI `2026-08-30` |
| Structure | `ZHPWRQIPPNZNML-NTISSMGPSA-N`, `C19H17Cl3N2S.HNO3`, neutral |

The target resolves unambiguously through `data/antibiotics/PATHS.tsv`, which
maps `CHEBI:59290` to `ANTIFUNGAL/s-butoconazole-nitrate`. The full target YAML
was read before review. It is a generated ChEBI-only seed with one exact
Beilstein cross-reference, one drug-level DrugBank cross-reference,
ChEBI-derived activity roles `CHEBI:35718` and `CHEBI:86327`, a ChEBI-derived
`ERGOSTEROL_PATHWAY_INHIBITION` mode, no `evidence`,
no `molecular_targets`, no `activity_observations`, no `causal_graphs`, and
only seed/reseed curation history.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/s-butoconazole-nitrate.yaml` | Pass; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/s-butoconazole-nitrate.yaml --out /tmp/s-butoconazole-nitrate-validate-strict.tsv` | Pass; 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Pass; 2,939 records expected and on disk, with no missing, unexpected, drifted, absent-from-`PATHS.tsv`, or stale-lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/s-butoconazole-nitrate-worklist.tsv` | Pass; `CHEBI:59290` appears only under `mechanism` and `review-readiness`. It is absent from minted-identity, xref, multi-component, producer-candidate, activity-candidate, structure-unreviewed, and target-evidence queues. |
| `just review-queue --limit 120` | Pass; `CHEBI:59290` is queued immediately after the just-reviewed `(S)-butoconazole` row with `MECHANISM_REVIEW: mechanism is source-seeded and not curator-checked; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just lint` | Pass; Ruff reported all checks passed. |
| Term/reference/history validators | No narrower single-record term, reference, or history validator is exposed for a plain ChEBI-seeded record in the justfile. The run used single-record schema checks plus full-corpus worklist and reproducibility checks instead. |

The full worklist also repeated the known unrelated `ARO:3000337`
cross-reference refusal for iclaprim and `CHEBI:31724`; it is not connected to
`CHEBI:59290` and did not affect this record.

## Identity and Grounding

The identity is internally consistent and matches the maintained ChEBI source
row in `data/raw/chebi_antimicrobials.tsv`:

| Claim | Review |
|---|---|
| ChEBI identifier and label | `CHEBI:59290` is the live OLS ChEBI term for `(S)-butoconazole nitrate` and is not obsolete. |
| Definition | The record definition matches the source row and denotes the nitric-acid salt of isolated `(S)-butoconazole`. |
| Parent | The local parent `CHEBI:3241` is broader racemic butoconazole nitrate. The OLS `hierarchicalParents` endpoint also returns `CHEBI:3241` as the sole hierarchical parent of `CHEBI:59290`. |
| Opposite enantiomer | OLS exposes a reciprocal `is_enantiomer_of` relation from `CHEBI:59290` to `CHEBI:59289`, the distinct `(R)-butoconazole nitrate` ChEBI term. |
| Neutral sibling boundary | The target is the nitrate salt, not neutral `(S)-butoconazole` `CHEBI:59288`. The neutral sibling has formula `C19H17Cl3N2S` and InChIKey `SWLMUYACZKCSHZ-INIZCTEOSA-N`; this record has formula `C19H17Cl3N2S.HNO3` and InChIKey `ZHPWRQIPPNZNML-NTISSMGPSA-N`. |
| Broader racemate boundary | The target is not racemic butoconazole nitrate `CHEBI:3241`, whose standard InChIKey is `ZHPWRQIPPNZNML-UHFFFAOYSA-N` and whose ChEBI row carries broader Beilstein, CAS, KEGG, and DrugBank xrefs. |
| Xrefs | `beilstein:6366647` and `drugbank:DB00639` are present on the OLS `CHEBI:59290` term and in the committed ChEBI inventory row for exact `CHEBI:59290`. The seeder keeps DrugBank under `drug_xrefs`, which is appropriate because `DB00639` appears on broader butoconazole nitrate and on both enantiomeric nitrate salts. |
| Filing class | `ANTIFUNGAL` is consistent with ChEBI role `CHEBI:35718` / `antifungal agent`. The additional `CHEBI:86327` / `antifungal drug` role is retained in `activity_roles`, so filing did not erase the source's narrower activity role. |
| Seeded mode | `CHEBI:75282` is present as the source ChEBI mechanism role, explaining the seeded `ERGOSTEROL_PATHWAY_INHIBITION` mode and `HOST_SHARED_TARGET` scope. It remains an imported role assertion rather than a curator-reviewed mechanism for the exact nitrate salt. |

The structural fields agree with both the maintained ChEBI inventory and the
live OLS term: SMILES
`Clc1ccc(CC[C@@H](Cn2ccnc2)Sc2c(Cl)cccc2Cl)cc1.O=[N+]([O-])O`,
Standard InChI
`InChI=1S/C19H17Cl3N2S.HNO3/c20-15-7-4-14(5-8-15)6-9-16(12-24-11-10-23-13-24)25-19-17(21)2-1-3-18(19)22;2-1(3)4/h1-5,7-8,10-11,13,16H,6,9,12H2;(H,2,3,4)/t16-;/m0./s1`,
InChIKey `ZHPWRQIPPNZNML-NTISSMGPSA-N`, formula
`C19H17Cl3N2S.HNO3`, charge `0`, average mass `474.797`, and
monoisotopic mass `473.01345`.

## Evidence

The record has no local `evidence` objects. That is acceptable for generated
identity, structure, filing, and role imports because their provenance is the
ChEBI source concept and committed inventory row, but it is not enough to make
the mode of action curator-reviewed.

The relevant publication searches were bounded as follows:

| Query | Result |
|---|---|
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --query '"(S)-butoconazole nitrate" OR "ZHPWRQIPPNZNML-NTISSMGPSA-N" OR "1-{(2S)-4-(4-chlorophenyl)-2-[(2,6-dichlorophenyl)sulfanyl]butyl}-1H-imidazole nitrate"' --limit 20 --output /tmp/s-butoconazole-nitrate-publications.jsonl` | PubMed returned 17 broader butoconazole candidates; Semantic Scholar returned HTTP 429. None of the PubMed titles or abstracts named exact `(S)-butoconazole nitrate`, the exact `(2S)` nitrate IUPAC synonym, or the exact Standard InChIKey. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --query 'butoconazole nitrate ERG11 CYP51 lanosterol demethylase ergosterol Candida resistance MIC' --limit 20 --output /tmp/s-butoconazole-nitrate-broad-publications.jsonl` | PubMed returned 0 candidates and Semantic Scholar returned HTTP 429. |

The exact search found useful near misses, not exact support:

| Lead | Scope problem |
|---|---|
| `PMID:2184984` | Reports sterol changes after exposing `Candida albicans` to butoconazole and other azoles. The abstract does not identify the material as isolated `(S)-butoconazole nitrate`, so it should not be attached to `CHEBI:59290` without full-text confirmation of the tested stereochemical and salt form. |
| `PMID:3902762` | Reports fungistatic/fungicidal effects of butoconazole against `Candida albicans` by growth phase, but at the broader butoconazole level. |
| `PMID:6094418` | Compares relative inhibition factors for broader butoconazole against fungal isolates, not exact `(S)-butoconazole nitrate`. |
| `PMID:7983571` | Reports macro-broth dilution sensitivity against vaginal yeast isolates for broader butoconazole and other agents, not the exact isolated nitrate enantiomer. |
| `PMID:24939312` and other butoconazole nitrate clinical/formulation records | Concern racemic butoconazole nitrate products, pharmacokinetics, clinical use, or formulation retention. They do not establish exact `(S)-butoconazole nitrate` identity or the exact seeded ergosterol mechanism. |
| `PMID:33990311` | Evaluates broader butoconazole as a tetracycline resistance modifier against `Staphylococcus aureus`, not as an antifungal ergosterol-biosynthesis inhibitor, and not as exact `CHEBI:59290`. |

## Completeness

- Identity, exact ChEBI grounding, the nitrate-salt chemical structure, the
  parent racemate-salt relationship, the Beilstein xref, the DrugBank drug
  xref, and the ChEBI-derived role set are complete enough for a generated
  seed.
- The record correctly does not import broader racemic butoconazole nitrate
  CAS, KEGG compound, or KEGG drug xrefs onto isolated
  `(S)-butoconazole nitrate`.
- The `mechanism` and `review-readiness` worklist entries are expected because
  `mode_of_action` and `mode_of_action_target_scope` are still seeded from the
  ChEBI `CHEBI:75282` role and have no exact primary evidence for this
  enantiomeric salt.
- Empty `molecular_targets`, `activity_observations`, `resistance_mechanisms`,
  `producers`, `clinical_status_assertions`, `datasets`, `causal_graphs`, and
  `discussions` are appropriate for now. The bounded searches did not find
  exact evidence that would justify adding a curator-owned target, activity
  observation, causal edge, or clinical status assertion.
- An ignored-inclusive exact search over `curation`, `data/raw`,
  `data/antibiotics`, `reports/yaml_record_review`, `docs`, `src`, `scripts`,
  and `tests` found `CHEBI:59290` only in the target YAML, `PATHS.tsv`, the raw
  ChEBI row, the review queue, and earlier sibling review reports that mention
  it only as a boundary. No exact prior review report for `CHEBI:59290` was
  found.

## Findings

| Severity | Finding | Evidence | Maintained owner for a future fix |
|---|---|---|---|
| blocker | None found | The exact ChEBI identity, structure, parent relationship, role terms, xrefs, class, generated status, and schema shape are internally consistent. | Not applicable |
| major | `mode_of_action` and `mode_of_action_target_scope` are still source-seeded rather than curator-checked, and the record has no exact `molecular_targets`, `activity_observations`, or `causal_graphs`. | The YAML says the mode was assigned from ChEBI role `CHEBI:75282` and is `Not a curator's mechanistic review`; `just worklist --limit 0 --tsv /tmp/s-butoconazole-nitrate-worklist.tsv` keeps `CHEBI:59290` in `mechanism` and `review-readiness`; the ChEBI row has no source PMIDs; exact PubMed searches found only broader butoconazole or racemic butoconazole-nitrate leads. | Add future curator-owned exact claims to `data/antibiotics/antifungal/s-butoconazole-nitrate.yaml` only if the exact `(S)` nitrate evidence is found, writing through `record_curation_event` and `write_validated_antibiotic`. If ChEBI later changes this role assertion, `data/raw/chebi_antimicrobials.tsv` and the ChEBI inventory extractor own that refresh. |
| minor | None found | No spelling, style, provenance, or non-blocking xref issue was found for this seed. | Not applicable |

## Recommended Edits

1. Leave the generated identity, structure, parent, activity-role, xref, and
   filing fields unchanged.
2. Search full texts or structure-indexed sources for exact
   `(S)-butoconazole nitrate` evidence before promoting the seeded
   ergosterol-biosynthesis mode to a curator-owned mechanism. Near-miss
   racemic butoconazole, racemic butoconazole nitrate, neutral-enantiomer, and
   broader azole literature should remain only leads unless they report this
   exact nitrate salt.
3. If exact evidence is found, add the narrowest supported object-level claims:
   a primary-evidence molecular target for fungal 14-alpha-demethylase or a
   better exact target if the source names one, activity observations with MIC
   method and units where available, and causal graph edges only for
   source-supported causal steps.
4. Keep `curation_status: SEEDED` until the exact structure, ChEBI grounding,
   filing class, mode, and any known molecular target all satisfy the
   repository `REVIEWED` gate.

## Follow-up Checks

After any future curator-owned exact mechanism edit, rerun:

- `just validate data/antibiotics/antifungal/s-butoconazole-nitrate.yaml`
- `just validate-strict data/antibiotics/antifungal/s-butoconazole-nitrate.yaml --out /tmp/s-butoconazole-nitrate-validate-strict.tsv`
- `just verify-corpus --summary`
- `just worklist --limit 0 --tsv /tmp/s-butoconazole-nitrate-worklist.tsv`
- `just review-queue --limit 120`
- `just lint`
- `git diff -- data/antibiotics/antifungal/s-butoconazole-nitrate.yaml curation/decisions.tsv src scripts tests`
- Manual full-text review that any cited PMID/DOI used for a target, activity
  observation, or causal edge identifies exact `(S)-butoconazole nitrate`, not
  neutral `(S)-butoconazole`, racemic butoconazole, racemic butoconazole
  nitrate, or a generic azole.

## Additional Notes

- This was a read-only review of one generated YAML record. No generated record,
  ChEBI inventory, queue TSV, rendered page, or curation history was edited.
- The review intentionally did not create a generic discussion for the missing
  mechanism. The gap is already expressed by the source-seeded mode note and
  worklist entries.
- The exact prior-review search included ignored files via
  `rg --no-ignore --hidden`; the file-presence check used `find`, which is
  also gitignore-independent.
