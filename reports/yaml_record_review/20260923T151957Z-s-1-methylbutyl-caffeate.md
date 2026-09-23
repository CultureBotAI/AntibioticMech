# YAML Record Review: (S)-1'-methylbutyl caffeate

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antiprotozoal/s-1-methylbutyl-caffeate.yaml`
- Started UTC: `2026-09-23T15:19:57Z`
- Finished UTC: `2026-09-23T15:20:52Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:70482` |
| Label | `(S)-1'-methylbutyl caffeate` |
| Path | `data/antibiotics/antiprotozoal/s-1-methylbutyl-caffeate.yaml` |
| Class | `ANTIPROTOZOAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Generated status | Generated from `data/raw/chebi_antimicrobials.tsv` and `data/antibiotics/PATHS.tsv`; no `curation/decisions.tsv` override owns this ChEBI seed. |
| Source concept | `CHEBI:70482` / `(S)-1'-methylbutyl caffeate`, version `2026-08-30`, role `CHEBI:70868` |
| Standard InChIKey | `AGXDVPULWUXVDT-PCGIRMHASA-N` |

This review read the entire generated record at
`data/antibiotics/antiprotozoal/s-1-methylbutyl-caffeate.yaml`.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiprotozoal/s-1-methylbutyl-caffeate.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/antiprotozoal/s-1-methylbutyl-caffeate.yaml --out /tmp/s-1-methylbutyl-caffeate-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2,939 records expected and on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, and 0 stale lockfile rows. The only warning was the known unrelated `ARO:3000337` / iclaprim CARD cross-reference refusal. |
| `just worklist --limit 0 --tsv /tmp/s-1-methylbutyl-caffeate-worklist.tsv` | Passed; `CHEBI:70482` appears in `mechanism`, `producer-candidate`, and `review-readiness`. It is not queued for minted grounding, xref, multi-component, structure, scope, or target-evidence defects. |
| `just review-queue --limit 107` | Passed; `CHEBI:70482` is still queued immediately after the reviewed `(S)-(−)-citronellal` row with `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| OLS4 ChEBI `CHEBI:70482` term lookup | Passed; the live ChEBI term is active and matched the generated definition, SMILES, Standard InChI, Standard InChIKey, formula, charge, masses, and xref/source lead split. |
| OLS4 ChEBI graph and role lookups | Passed; `CHEBI:65331` is the direct `subClassOf` parent, `CHEBI:77518` is the `has functional parent` 2-pentanol, `CHEBI:70868` resolves to `antileishmanial agent`, and `CHEBI:76924` is a plant-metabolite role that this antimicrobial corpus correctly does not file as an `activity_roles` value. |
| PubMed `PMID:20954722` XML fetch | Passed; resolved to the expected 2010 Journal of Natural Products paper with DOI `10.1021/np1005357`. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --query '"AGXDVPULWUXVDT-PCGIRMHASA-N"[All Fields] OR "CHEBI:70482"[All Fields] OR "(S)-1'\''-methylbutyl caffeate"' --limit 20 --output /tmp/s-1-methylbutyl-caffeate-pubmed-exact.jsonl` | PubMed returned one candidate, the exact source lead `PMID:20954722`. |
| Single-record term, reference, or history validators | Not available for this plain ChEBI-seeded generated record. The narrowest repository validators exposed by `justfile` for these concerns are the full-corpus `verify-corpus`, `worklist`, and `review-queue` checks above. |
| `just lint` | Passed after writing this ignored report. |
| `git diff --cached --check` | Passed after staging this ignored report. |

## Identity and Grounding

Identity is internally consistent and agrees with ChEBI:

- `data/raw/chebi_antimicrobials.tsv` row 1792 is the maintained ChEBI input
  for `CHEBI:70482`; its label, definition, role, parent, SMILES, Standard
  InChI, Standard InChIKey, formula, charge, masses, IUPAC synonym, Reaxys
  xref, and `PMID:20954722` source reference reproduce the generated YAML.
- The OLS4 ChEBI `CHEBI:70482` term is not obsolete and has the same Standard
  InChIKey, `AGXDVPULWUXVDT-PCGIRMHASA-N`.
- ChEBI describes the same `(2S)` pentan-2-yl caffeate ester that the local
  stereospecific SMILES `CCC[C@H](C)OC(=O)/C=C/c1ccc(O)c(O)c1` encodes.
- The parent `CHEBI:65331` is the structural class `alkyl caffeate ester` and
  correctly belongs in `parent_compounds`.
- OLS4 additionally asserts 2-pentanol, `CHEBI:77518`, by `has functional
  parent`; this is not an exact xref or an `is_a` parent and is correctly absent
  from `parent_compounds`.
- The OLS4 ChEBI term carries two database cross-references:
  `reaxys:21092025`, which is the generated exact xref, and
  `pubmed:20954722`, which is correctly retained as the ChEBI source reference
  rather than a chemical-identity xref.
- The adjacent `(S)-1'-methyloctyl caffeate` seed at `CHEBI:70484` shares
  `CHEBI:65331`, `CHEBI:70868`, and `PMID:20954722`, but it has a different
  formula, Reaxys xref, and Standard InChIKey
  `DEXGFPWDAXJBTA-WONIAPNHSA-N`, so it is a sibling record rather than an
  asserted equivalent.
- `CHEBI:70868` resolves to `antileishmanial agent`, an antiprotozoal drug
  class, so the `ANTIPROTOZOAL` filing class and the retained
  `activity_roles` entry agree with the sole ChEBI-seeded antimicrobial role.

## Evidence

Existing claim evidence is narrow:

| Claim | Evidence review |
|---|---|
| ChEBI identity, definition, synonym, antileishmanial role, parent, Reaxys xref, structure fields, and `PMID:20954722` source reference | Database-seeded from the `CHEBI:70482` row in `data/raw/chebi_antimicrobials.tsv`; no curator-owned literature citation is required at record level. |

The record has no `mode_of_action`, `molecular_targets`,
`activity_observations`, `resistance_mechanisms`, `producer_organisms`,
`causal_graphs`, or record-level literature `evidence` items. No existing
citation is therefore attached to a broader claim than it supports.

## Completeness

The record is structurally grounded but not complete enough for `REVIEWED`:

- `mode_of_action` and `mode_of_action_target_scope` are absent.
- `molecular_targets` is absent.
- `causal_graphs` is absent.
- `activity_observations` is absent even though `PMID:20954722` is an exact
  antileishmanial source lead.
- `producer_organisms` is absent; the full text of `PMID:20954722` should be
  checked before treating the ChEBI definition's `Piper sanguineispicum` leaf
  isolation statement as a biosynthetic producer assertion.
- `resistance_mechanisms`, `clinical_status`, and `datasets` are empty; this
  bounded review found no local source rows proving these omissions are defects.

`PMID:20954722` is promising but not enough by abstract alone to fill the
curator-owned fields. Its abstract says new caffeic acid esters, numbered
`1-3`, were isolated from `Piper sanguineispicum` leaves and assessed against
axenic amastigote forms of `Leishmania amazonensis`, and that compounds `1`
and `3` had the best antileishmanial activity with `IC50` values of `2.0` and
`1.8 μM`. The abstract does not map those compound numbers to `CHEBI:70482`
unambiguously, does not report a mode of action, and does not provide enough
assay context for a claim-level `ActivityObservation`.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| major | `mode_of_action`, `molecular_targets`, `activity_observations`, and `causal_graphs` are absent even though `PMID:20954722` is an exact ChEBI source lead for antileishmanial activity. The full text must be inspected to map the paper's compound numbers to `CHEBI:70482`, capture any `Leishmania amazonensis` activity measurement, and decide whether the paper supports a specific mode of action or only activity. | Curator-owned additions in `data/antibiotics/antiprotozoal/s-1-methylbutyl-caffeate.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |
| minor | `Piper sanguineispicum` is present only as a ChEBI isolation statement and a `producer-candidate` worklist row. No `producer_organisms` assertion exists yet, and the source paper should be checked for wording that distinguishes plant biosynthesis from source-material isolation before any producer claim is added. | Curator-owned additions in `data/antibiotics/antiprotozoal/s-1-methylbutyl-caffeate.yaml`, written through `record_curation_event` and `write_validated_antibiotic`. |

No blockers were found.

## Recommended Edits

1. Inspect `PMID:20954722` in full text and map the paper's compound numbers to
   `CHEBI:70482` and `CHEBI:70484` before adding any activity values. Make any
   update through a guarded mutator that loads
   `data/antibiotics/antiprotozoal/s-1-methylbutyl-caffeate.yaml`, asserts
   `CHEBI:70482`, appends a `codex` `record_curation_event`, and writes with
   `write_validated_antibiotic`.
2. If the full text reports a source-supported organism context, add one or
   more `ActivityObservation` entries for the `Leishmania amazonensis` assay
   with its exact value type, units, assay, and `PMID:20954722` evidence.
   Preserve an `IC50` as an `activity_notes` detail if it cannot be represented
   in the MIC-specific slots.
3. Add `mode_of_action`, `molecular_targets`, or `causal_graphs` only if the
   paper or a follow-up primary source proves a mechanistic claim for the exact
   `CHEBI:70482` structure.
4. Curate `Piper sanguineispicum` as a `producer_organisms` entry only if the
   inspected source text supports the plant as a true source organism for this
   exact compound.

## Follow-up Checks

- Rerun
  `just validate data/antibiotics/antiprotozoal/s-1-methylbutyl-caffeate.yaml`
  and `just validate-strict
  data/antibiotics/antiprotozoal/s-1-methylbutyl-caffeate.yaml --out
  /tmp/s-1-methylbutyl-caffeate-strict.tsv`.
- Rerun `just verify-corpus --summary` to prove the generated record still
  reproduces exactly from maintained sources plus curator-owned additions.
- Rerun `just worklist --limit 0 --tsv
  /tmp/s-1-methylbutyl-caffeate-worklist.tsv` and verify that `CHEBI:70482`
  leaves `mechanism`, `producer-candidate`, and `review-readiness` only when
  the corresponding curated assertions satisfy the local gates.
- Run `just qc` before opening any curation PR.

## Additional Notes

- An ignored/hidden-inclusive search of `reports/yaml_record_review` found no
  prior `s-1-methylbutyl-caffeate` report.
- An ignored/hidden-inclusive search of the target record, `PATHS.tsv`,
  `data/raw`, `curation`, `reports/yaml_record_review`, and
  `/tmp/s-1-methylbutyl-caffeate-worklist.tsv` found `CHEBI:70482` only in the
  generated target, the path lockfile, the ChEBI raw row, the derived
  `record_review_queue.tsv` row, and the expected `mechanism`,
  `producer-candidate`, and `review-readiness` worklist rows.
- The same search found no `curation/decisions.tsv` override for
  `antibioticmech:chebi-52bdfe56a8`.
- An ignored/hidden-inclusive `AGENTS.md` search, excluding `.git`, found no
  local AGENTS guidance files; only the chat-provided exhaustive-search rule
  applied.
