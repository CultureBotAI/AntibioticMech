# YAML Record Review: (+)-(11R,2'S)-erythro-mefloquine

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antiprotozoal/11r-2-s-erythro-mefloquine.yaml`
- Started UTC: 2026-09-21T06:41:36Z
- Finished UTC: 2026-09-21T06:41:36Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/antibiotics/antiprotozoal/11r-2-s-erythro-mefloquine.yaml` |
| Class | `ANTIPROTOZOAL` |
| ID | `CHEBI:63684` |
| Label | `(+)-(11R,2'S)-erythro-mefloquine` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained status | Generated from `data/raw/` inventories |

The record denotes the exact ChEBI-grounded `(+)-(11R,2'S)-erythro` enantiomer
of mefloquine with InChIKey `XEEQGYMUWCZPDN-SWLSCSKDSA-N`. It has one ChEBI
source concept, one antimalarial activity role, one broader parent
`CHEBI:63681`, CAS and Reaxys xrefs, and no record evidence, mode of action,
molecular target, activity observation, resistance mechanism, clinical
assertion, causal graph, dataset, or `Discussion`.

## Validation

| Command | Result |
|---|---|
| `just validate data/antibiotics/antiprotozoal/11r-2-s-erythro-mefloquine.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antiprotozoal/11r-2-s-erythro-mefloquine.yaml --out /tmp/antibioticmech-mefloquine-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2,939 expected records, 2,939 records on disk, no missing records, no unexpected records, no drifted fields, no `PATHS.tsv` drift. |
| `just review-queue --limit 10` | Confirmed `(+)-(11R,2'S)-erythro-mefloquine` remains in `review-readiness`: `MECHANISM_REVIEW`, no mechanism, zero source literature leads, zero record evidence items, and zero targets. |
| `uv run python scripts/search_publications.py --provider pubmed --provider semantic-scholar --query "(+)-mefloquine antimalarial mechanism Plasmodium" --limit 20 --output /tmp/antibioticmech-mefloquine-pubs.jsonl` | PubMed returned 20 candidates; Semantic Scholar returned HTTP 429. The candidates were discovery leads only and were not promoted to record evidence. |
| `uv run python scripts/search_publications.py --provider pubmed --provider semantic-scholar --query "CHEBI:63684 OR (+)-mefloquine OR erythro-mefloquine" --limit 20 --output /tmp/antibioticmech-mefloquine-identity-pubs.jsonl` | PubMed returned 20 candidates; Semantic Scholar returned HTTP 429. The candidates were mostly generic mefloquine leads rather than curated exact-enantiomer mechanism evidence. |

No separate single-record term, reference, or history validator is documented in
the local `justfile`. The full `just qc` gate is left for the PR-level check
because this review made no YAML mutation.

## Identity and Grounding

`11r-2-s-erythro-mefloquine.yaml` resolves unambiguously under
`data/antibiotics/antiprotozoal/`. The generated lock row in
`data/antibiotics/PATHS.tsv` maps `CHEBI:63684` to
`ANTIPROTOZOAL/11r-2-s-erythro-mefloquine`, and `source_concepts` carries only
the expected ChEBI upstream identity.

The exact structure block matches the committed ChEBI antimicrobial inventory
row for `CHEBI:63684`: SMILES, Standard InChI, InChIKey
`XEEQGYMUWCZPDN-SWLSCSKDSA-N`, formula `C17H16F6N2O`, charge `0`, average
mass, and monoisotopic mass agree with `data/raw/chebi_antimicrobials.tsv`.
The official ChEBI page for `CHEBI:63684` also reports the same label, formula,
SMILES, Standard InChI, InChIKey, neutral charge, masses, `CHEBI:38068`
antimalarial role, `CHEBI:63681` parent, `CHEBI:63687` opposite-enantiomer
relation, CAS `51688-68-7`, and Reaxys `766169`.

The target is distinct from both the racemate `CHEBI:63609` and the opposite
`CHEBI:63687` enantiomer. The adjacent `CHEBI:63687` inventory row has the same
formula and neutral charge, but its SMILES and Standard InChI carry the opposite
stereochemistry and its InChIKey is `XEEQGYMUWCZPDN-DOMZBBRYSA-N`.

No local grounding decision was found for `CHEBI:63684` or its source-concept
mint `antibioticmech:chebi-a0baeb1623` in a gitignore-independent search over
`curation/`, `data/`, and `reports/yaml_record_review/` with
`rg --hidden --no-ignore`.

## Evidence

The generated identity, label, definition, exact synonyms, exact structure,
parent compound, xrefs, filing class, antimalarial activity role, source
concept, and grounding status reproduce from the committed ChEBI inventory with
no `verify-corpus` drift. The definition and role are database assertions from
ChEBI; there is no record-level primary literature for this exact enantiomer.

The record makes no molecular-target, activity, resistance, producer, clinical,
or causal-edge claims, so there are no unsupported claim-level citations in the
YAML.

The committed BindingDB, Drugs@FDA, MIBiG, and PHI-base inventories contain no
local row for `CHEBI:63684`, InChIKey `XEEQGYMUWCZPDN-SWLSCSKDSA-N`, CAS
`51688-68-7`, or the exact label/synonym strings in this record.

PubMed searches by the exact label and by `(+)-mefloquine` plus antimalarial
mechanism terms surfaced generic mefloquine, arylamino alcohol, PfMDR1, and
Plasmodium drug-response papers. Those are plausible future leads for the
racemate or class, but this read-only pass did not inspect a primary paper that
supports a mode of action, molecular target, or causal graph for the exact
`CHEBI:63684` structure.

## Completeness

The exact identity, stereochemistry, ChEBI grounding, source concept, filing
class, antimalarial activity role, and same-structure xrefs are defensible.

The consequential gap is mechanism sign-off. The YAML has no
`mode_of_action`, no `mode_of_action_target_scope`, no `molecular_targets`, and
no `causal_graphs`; ChEBI's own definition also treats the mechanism of the
racemic drug as unknown rather than asserting a target. `just review-queue
--limit 10` therefore keeps the record in `MECHANISM_REVIEW`.

No activity observations, producer claims, public datasets, structural
observations, resistance assertions, clinical assertions, or discussions are
present. The review found no specific local evidence that any of those optional
sections must be populated before the absent mechanism is resolved.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record has no curated antimalarial mechanism and cannot satisfy the `REVIEWED` gate. | The target YAML has no `mode_of_action`, `molecular_targets`, or `causal_graphs`; the source-literature column in `curation/record_review_queue.tsv` is empty for `CHEBI:63684`; `just review-queue --limit 10` reports `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. | Curator-owned mechanism, target, discussion, or causal-graph additions written to `data/antibiotics/antiprotozoal/11r-2-s-erythro-mefloquine.yaml` through `write_validated_antibiotic`, if primary literature supports them. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Leave `mode_of_action` blank until a curator inspects primary literature
   that establishes whether exact `CHEBI:63684`, the racemate, or the broader
   arylamino-alcohol class has a representable antimalarial mechanism.
2. Review the PubMed leads around PfMDR1, heme or hemozoin metabolism, and
   beta-hematin formation as discovery leads. Do not attach them to this
   enantiomer unless the inspected paper's compound scope supports that exact
   assertion.
3. If a mechanism remains genuinely unresolved after primary-paper review, add
   a scoped `Discussion` that records the unresolved question and the bounded
   searches rather than promoting a speculative target.
4. If a mode of action or target is supported, write it with a guarded mutator
   that asserts `identifier == "CHEBI:63684"`, updates only the
   curator-owned mechanism fields, appends a `codex` `CurationEvent` with
   `llm_assisted: true`, and emits via `write_validated_antibiotic`.
5. Move `curation_status` to `REVIEWED` only after identity, structure, filing
   class, and the newly curated mode of action satisfy the `docs/CURATION.md`
   sign-off criteria.

## Follow-up Checks

After a future mechanism curation edit:

- `just validate-strict data/antibiotics/antiprotozoal/11r-2-s-erythro-mefloquine.yaml --out /tmp/antibioticmech-mefloquine-validation.tsv`
- `just verify-corpus`
- `just qc`
- `git diff -- data/antibiotics/antiprotozoal/11r-2-s-erythro-mefloquine.yaml curation/decisions.tsv src scripts tests`
- `just review-queue --limit 0 --tsv curation/record_review_queue.tsv`

## Additional Notes

Searches used to establish absence included ignored files:

- `rg --hidden --no-ignore` over `curation/`, `data/`, and
  `reports/yaml_record_review/` for `CHEBI:63684`,
  `antibioticmech:chebi-a0baeb1623`, `11r-2-s-erythro-mefloquine`, and
  `erythro-mefloquine`.
- `rg --hidden --no-ignore` over `reports/yaml_record_review/` for an existing
  `CHEBI:63684`, `11r-2-s-erythro-mefloquine`, or `erythro-mefloquine` review
  report.
- `rg --hidden --no-ignore` over
  `data/raw/bindingdb_target_measurements.tsv`,
  `data/raw/fda_clinical_status.tsv`, `data/raw/mibig_producers.tsv`, and
  `data/raw/phibase_amr.tsv` for `CHEBI:63684`,
  `XEEQGYMUWCZPDN`, `51688-68-7`, and `mefloquine`.
- `rg --hidden --no-ignore` over `curation/decisions.tsv` for `CHEBI:63684`
  and `antibioticmech:chebi-a0baeb1623`.

`NCBI_EMAIL` was unset for the PubMed searches. Semantic Scholar returned HTTP
429 for both targeted publication searches, so that provider's literature leads
were not available in this pass.

This report is read-only review output. No generated record, upstream
inventory, decision row, page, queue, or curation-history entry was edited.
