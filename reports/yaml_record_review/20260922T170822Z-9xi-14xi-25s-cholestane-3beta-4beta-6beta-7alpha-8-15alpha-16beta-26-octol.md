# YAML Record Review: (9ξ,14ξ,25S)-cholestane-3β,4β,6β,7α,8,15α,16β,26-octol

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antifungal/9ξ-14ξ-25s-cholestane-3β-4β-6β-7α-8-15α-16β-26-octol.yaml`
- Started UTC: 2026-09-22T17:05:00Z
- Finished UTC: 2026-09-22T17:08:22Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:228372` |
| Label | `(9ξ,14ξ,25S)-cholestane-3β,4β,6β,7α,8,15α,16β,26-octol` |
| Path | `data/antibiotics/antifungal/9ξ-14ξ-25s-cholestane-3β-4β-6β-7α-8-15α-16β-26-octol.yaml` |
| Class | `ANTIFUNGAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:228372`, version `2026-08-30`, minted key `antibioticmech:chebi-6d4a0cce99` |
| Source role | `CHEBI:35718` antifungal agent |
| Parent compounds | `CHEBI:139333` 8-hydroxy steroid; `CHEBI:17354` 16beta-hydroxy steroid; `CHEBI:36836` 3beta-hydroxy steroid; `CHEBI:36843` 7alpha-hydroxy steroid; `CHEBI:36851` 6beta-hydroxy steroid; `CHEBI:36852` 26-hydroxy steroid; `CHEBI:62846` 4-hydroxy steroid; `CHEBI:83147` 15alpha-hydroxy steroid |
| Structure | `VYOXQPQXOVKJIA-NMTBNCKFSA-N`; formula `C27H48O8`; charge `0` |
| Xrefs | None |
| Document xrefs | None |
| Source literature leads | None |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded record for exact
`(9ξ,14ξ,25S)-cholestane-3β,4β,6β,7α,8,15α,16β,26-octol`. The YAML has exact
ChEBI grounding, eight ChEBI parents, the antifungal ChEBI role, structure, and
source-concept metadata. It has no ChEBI definition, distinct synonyms, xrefs,
document xrefs, generated or curator-owned mode of action, molecular target,
activity observation, producer organism, resistance mechanism, dataset,
discussion, causal graph, or claim-level evidence.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/9ξ-14ξ-25s-cholestane-3β-4β-6β-7α-8-15α-16β-26-octol.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/9ξ-14ξ-25s-cholestane-3β-4β-6β-7α-8-15α-16β-26-octol.yaml --out /tmp/antibioticmech-chebi-228372-strict.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-228372-worklist.tsv` | Pass: the full worklist TSV was written. `CHEBI:228372` appears on `mechanism` and `review-readiness`; it was not found on any other queue in that TSV. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just review-queue --limit 84` | Pass: `CHEBI:228372` is queued with `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for
this plain ChEBI-seeded record; the schema/strict checks, `verify-corpus`, and
worklist are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:228372` resolves in official OLS as a current, non-obsolete 3-star ChEBI
term with label `(9xi,14xi,25S)-cholestane-3beta,4beta,6beta,7alpha,8,15alpha,16beta,26-octol`,
the exact Standard InChIKey `VYOXQPQXOVKJIA-NMTBNCKFSA-N`, formula `C27H48O8`,
neutral charge, matching average and monoisotopic masses, the same SMILES, no
database xrefs, and no definition or source PubMed xrefs. The live OLS label
spells the Greek stereochemical affixes out as `xi`, `alpha`, and `beta`,
whereas the committed `2026-08-30` ChEBI inventory row uses the equivalent
Greek symbols in the generated label and filename stem.

The generated YAML stores no synonyms. OLS exposes only duplicate IUPAC
synonyms that repeat the preferred ASCII label; the local seeder correctly
de-duplicates them out of `synonyms`.

The live OLS hierarchy gives `CHEBI:228372` eight direct parents:
`CHEBI:139333` 8-hydroxy steroid, `CHEBI:17354` 16beta-hydroxy steroid,
`CHEBI:36836` 3beta-hydroxy steroid, `CHEBI:36843` 7alpha-hydroxy steroid,
`CHEBI:36851` 6beta-hydroxy steroid, `CHEBI:36852` 26-hydroxy steroid,
`CHEBI:62846` 4-hydroxy steroid, and `CHEBI:83147` 15alpha-hydroxy steroid.
Those are exactly the generated `parent_compounds` values. The live OLS
`has_role` relation gives the term three roles: `CHEBI:35718` antifungal
agent, `CHEBI:75767` animal metabolite, and `CHEBI:76507` marine metabolite.
Only `CHEBI:35718` is an antimicrobial role in `conf/sources.yaml`, and the
committed source configuration maps that role to generated filing class
`ANTIFUNGAL`.

The committed ChEBI inventory row for `CHEBI:228372` has the same Greek-symbol
label, 3-star status, antifungal role, parents, SMILES, Standard InChI,
Standard InChIKey, formula, neutral charge, and masses that were used to seed
this record. `PATHS.tsv` maps `CHEBI:228372` to
`ANTIFUNGAL/9ξ-14ξ-25s-cholestane-3β-4β-6β-7α-8-15α-16β-26-octol`, matching the
generated path and filing class.

Before this report was created, ignored-inclusive exact searches for
`CHEBI:228372`, the exact file stem, the exact Greek-symbol label, and the exact
Standard InChIKey across `reports/yaml_record_review`, `data/antibiotics`,
`data/raw`, `curation`, `conf`, `.claude`, `CLAUDE.md`, and `justfile` found
only the expected generated YAML, `PATHS.tsv` row, raw ChEBI row, and
`record_review_queue.tsv` row for exact `CHEBI:228372`. An ignored-inclusive
filename search for `*cholestane*` under `reports/yaml_record_review` found no
prior report for this exact record.

## Evidence

The record's antifungal classification is inherited from committed ChEBI role
`CHEBI:35718`, `antifungal agent`. `data/raw/chebi_role_names.tsv` marks that
role as a ChEBI scope role, and `conf/sources.yaml` maps it to generated class
`ANTIFUNGAL`. That role is enough for reproducible source-level filing but not
enough to fill a specific activity observation, producer assertion, mode of
action, target, or causal graph.

No source PMID, DOI, xref, or document xref is available in the committed ChEBI
row or the live OLS term for `CHEBI:228372`. An exact-label, Standard
InChIKey, and formula publication-helper query returned zero PubMed candidates;
Semantic Scholar returned HTTP 429. The bounded search therefore found no
immediate primary-paper lead that could support exact-compound antifungal
activity, mechanism, target, producer, resistance, dataset, clinical, or
causal-graph assertions.

## Completeness

The record is incomplete as a reviewed antifungal record. It has exact ChEBI
identity, structure, parentage, source-level antifungal classification, and
reproducible source metadata, but it has no literature-backed activity,
mechanism, target, or causal graph, and the source ChEBI row contributes no
PMID or xref leads for a curator to follow.

The empty `mode_of_action`, `molecular_targets`, activity-observation,
producer, resistance, clinical, dataset, discussion, and causal-graph slots are
acceptable for the current seed. None of the bounded checks identified a
source-supported exact-compound assertion to add.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Exact `CHEBI:228372` has source-level antifungal classification but no local source literature leads or curator-owned exact-compound activity, mechanism, target, or causal-graph claim. | The generated record has zero source PubMed leads, zero record evidence items, zero `activity_spectrum` rows, zero targets, no `mode_of_action`, and no xrefs. `just worklist` places the record only on `mechanism` and `review-readiness`. Exact-label/InChIKey/formula publication discovery returned zero PubMed candidates. | Future curator-owned fields on `data/antibiotics/antifungal/9ξ-14ξ-25s-cholestane-3β-4β-6β-7α-8-15α-16β-26-octol.yaml`, written through `record_curation_event` and `write_validated_antibiotic`, or a source-owned exclusion/role correction in `curation/decisions.tsv` or the ChEBI extractor path if the upstream antifungal role proves unsupported. |

No blocker identity, structure, schema, xref, parentage, or audit-history
findings were found.

No minor findings.

## Recommended Edits

1. Trace the ChEBI `CHEBI:35718` antifungal role for exact `CHEBI:228372` to a
   primary source. If the role is supported, curate exact antifungal
   `ActivityObservation` entries with organism, strain, assay, value, unit, and
   evidence details; leave `mode_of_action`, `molecular_targets`, and the
   causal graph empty unless that same or another exact-compound primary source
   supports them.
2. If the ChEBI antifungal role cannot be supported for exact
   `CHEBI:228372`, add an exclusion or role-correction decision through
   `curation/decisions.tsv`, or adjust the ChEBI extractor path if the absence
   of source evidence reflects a systemic source-filtering issue.
3. Leave the source-owned ChEBI identity, structure, parents, and antifungal
   role untouched unless the committed ChEBI inventory diverges from a refreshed
   upstream ChEBI release or a curator decision needs to exclude a proven wrong
   source assertion.

## Follow-up Checks

After any exact-term curation, exclusion, or source refresh, rerun:

1. `just validate data/antibiotics/antifungal/9ξ-14ξ-25s-cholestane-3β-4β-6β-7α-8-15α-16β-26-octol.yaml`
2. `just validate-strict data/antibiotics/antifungal/9ξ-14ξ-25s-cholestane-3β-4β-6β-7α-8-15α-16β-26-octol.yaml --out /tmp/antibioticmech-chebi-228372-strict.tsv`
3. `just verify-corpus --summary`
4. `just worklist --limit 0 --tsv /tmp/antibioticmech-chebi-228372-worklist.tsv`
5. `just review-queue --limit 84`
6. `just qc`

Manually compare any future activity, mode-of-action, target, dataset,
discussion, or causal-graph assertion against exact `CHEBI:228372` identity.
Confirm that every claim-level evidence block attaches to the specific object
it supports, not only to the whole ChEBI term, the source antifungal-agent role,
or an adjacent hydroxy steroid.

## Additional Notes

All absence checks in this report used `rg --no-ignore --hidden` or `find`, so
they included ignored `reports/` files.
