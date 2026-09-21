# YAML Record Review: (+)-bisdechlorogeodin

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/unspecified/bisdechlorogeodin.yaml`
- Started UTC: 2026-09-21T08:49:04Z
- Finished UTC: 2026-09-21T08:49:04Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/antibiotics/unspecified/bisdechlorogeodin.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| ID | `CHEBI:15390` |
| Label | `(+)-bisdechlorogeodin` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained status | Generated from `data/raw/` inventories |

The record denotes the exact ChEBI-grounded `(+)` enantiomer of
bisdechlorogeodin with InChIKey `JCMPRFCVZKOFIT-KRWDZBQOSA-N`. It has one ChEBI
source concept, one broad antimicrobial activity role, one broader ChEBI parent
compound, two same-structure xrefs, and no record evidence, mode of action,
molecular target, activity observation, resistance mechanism, producer organism,
clinical assertion, causal graph, dataset, or `Discussion`.

## Validation

| Command | Result |
|---|---|
| `just validate data/antibiotics/unspecified/bisdechlorogeodin.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/bisdechlorogeodin.yaml --out /tmp/antibioticmech-bisdechlorogeodin-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2,939 expected records, 2,939 records on disk, no missing records, no unexpected records, no drifted fields, no `PATHS.tsv` issues. |
| `just review-queue --limit 10` | Confirmed `(+)-bisdechlorogeodin` remains in `review-readiness`: `MECHANISM_REVIEW`, no mechanism, zero source literature leads, zero record evidence items, and zero targets. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --provider semantic-scholar --query '"(+)-bisdechlorogeodin" OR "bisdechlorogeodin"' --limit 20 --output /tmp/antibioticmech-bisdechlorogeodin-publications.jsonl` | Wrote 12 broad bisdechlorogeodin candidates. |
| `env -u NCBI_EMAIL uv run python scripts/search_publications.py --provider pubmed --provider semantic-scholar --query 'JCMPRFCVZKOFIT OR 59092-96-5 OR C03036' --limit 20 --output /tmp/antibioticmech-bisdechlorogeodin-ids-publications.jsonl` | PubMed found no identifier-matching candidates; Semantic Scholar returned an invalid response. |

No separate single-record term, reference, or history validator is documented in
the local `justfile`. The full `just qc` gate is left for the PR-level check
because this review made no YAML mutation.

## Identity and Grounding

`bisdechlorogeodin.yaml` resolves unambiguously under
`data/antibiotics/unspecified/`. The generated lock row in
`data/antibiotics/PATHS.tsv` maps `CHEBI:15390` to
`ANTIMICROBIAL_UNSPECIFIED/bisdechlorogeodin`, and `source_concepts` carries
only the expected ChEBI upstream identity with minted ID
`antibioticmech:chebi-711321b801`.

The exact structure block matches the committed ChEBI antimicrobial inventory
row for `CHEBI:15390`: SMILES, Standard InChI, InChIKey
`JCMPRFCVZKOFIT-KRWDZBQOSA-N`, formula `C17H14O7`, charge `0`, average mass,
and monoisotopic mass agree with `data/raw/chebi_antimicrobials.tsv`. The
official ChEBI page for `CHEBI:15390` reports the same label, formula, SMILES,
Standard InChI, InChIKey, antimicrobial role, CAS `59092-96-5`, and KEGG
`C03036` xref.

The target is distinct from its adjacent ChEBI relatives that are also present
in the corpus. `CHEBI:15391` is `(−)-bisdechlorogeodin`, has the opposite
stereochemical layer in its Standard InChI, and has a different InChIKey
`JCMPRFCVZKOFIT-QGZVFWFLSA-N`; `CHEBI:22899` is the broader racemic or
unspecified `bisdechlorogeodin` parent with InChIKey
`JCMPRFCVZKOFIT-UHFFFAOYSA-N`.

No local grounding decision was found for `CHEBI:15390`,
`JCMPRFCVZKOFIT-KRWDZBQOSA-N`, `59092-96-5`, or KEGG `C03036` in a
gitignore-independent search over `curation/`, `data/raw/`, and
`reports/yaml_record_review/`.

## Evidence

The generated identity, label, exact and related synonyms, exact structure,
parent compound, same-structure xrefs, filing class, antimicrobial activity
role, source concept, and grounding status reproduce from the committed ChEBI
inventory with no `verify-corpus` drift.

The retained ChEBI role is `CHEBI:33281`, the broad `antimicrobial agent` role.
That role explains why the record is filed as `ANTIMICROBIAL_UNSPECIFIED` rather
than as an antibacterial, antifungal, antiprotozoal, or antiviral subclass.

The exact-label and general-name publication search found discovery leads for
the `(+)-bisdechlorogeodin` producer `Penicillium frequentans`, the
stereospecific sulochrin oxidase reaction that forms the `(+)` enantiomer, and
activity of stereochemically unspecified bisdechlorogeodin against
`Xanthomonas citri` subsp. `citri`. The inspected metadata did not establish a
primary-literature mode of action, target, or MIC claim that could be promoted
directly to this exact `CHEBI:15390` record.

The identifier query found no papers by `JCMPRFCVZKOFIT`, `59092-96-5`, or
`C03036`, so registry identifiers did not resolve a more exact activity or
mechanism source.

The record makes no molecular-target, activity, resistance, producer, clinical,
or causal-edge claims, so there are no unsupported claim-level citations in the
YAML.

## Completeness

The exact ChEBI identity, stereochemistry, structure, ChEBI grounding, source
concept, parent compound, same-structure xrefs, and broad antimicrobial role are
defensible.

The consequential gap is mechanism sign-off. The YAML has no `mode_of_action`,
no `mode_of_action_target_scope`, no `molecular_targets`, and no
`causal_graphs`; it also has no record-level evidence or discussion documenting
the exact searches needed to decide whether an unknown mechanism should stay
blank. `just review-queue --limit 10` therefore keeps the record in
`MECHANISM_REVIEW`.

No activity observations, producer claims, resistance assertions, clinical
assertions, or public datasets are present. The publication search found
producer and bioactivity leads that could support future optional additions,
but this read-only pass found no local evidence that any of those optional
sections must be populated before the absent mechanism is resolved.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record has no curated antimicrobial mechanism and cannot satisfy the `REVIEWED` gate. | The target YAML has no `record_evidence`, `mode_of_action`, `molecular_targets`, or `causal_graphs`; the committed ChEBI inventory has no source-literature leads for `CHEBI:15390`; `just review-queue --limit 10` reports `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`. | Curator-owned evidence, mechanism, target, discussion, or causal-graph additions written to `data/antibiotics/unspecified/bisdechlorogeodin.yaml` through `write_validated_antibiotic`, if primary literature supports them. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Review the exact `(+)-bisdechlorogeodin` isolation and sulochrin oxidase
   papers, the `Pseudogymnoascus` bisdechlorogeodin anti-`Xanthomonas citri`
   report, and citations around the 2024 membrane-permeabilization result to
   decide whether any primary source supports a mode of action, activity
   observation, producer claim, or unresolved-mechanism discussion for
   `CHEBI:15390`.
2. Do not promote activity or membrane-effect evidence from unspecified
   `bisdechlorogeodin`, `(+)-geodin`, `2'-hydroxy bisdechlorogeodin`, or other
   related fungal metabolites unless the inspected paper explicitly supports
   the same assertion for the `(+)` enantiomer represented by `CHEBI:15390`.
3. If the mechanism remains genuinely unresolved after the primary-paper
   review, add a scoped `Discussion` that records the search boundary instead
   of asserting a speculative molecular target.
4. If a mode of action, target, activity observation, or producer claim is
   supported, write it with a guarded mutator that asserts
   `identifier == "CHEBI:15390"`, updates only curator-owned fields, appends a
   `codex` `CurationEvent` with `llm_assisted: true`, and emits via
   `write_validated_antibiotic`.
5. Move `curation_status` to `REVIEWED` only after identity, structure, filing
   class, and the newly curated mechanism or unresolved-mechanism discussion
   satisfy the `docs/CURATION.md` sign-off criteria.

## Follow-up Checks

After a future mechanism curation edit:

- `just validate-strict data/antibiotics/unspecified/bisdechlorogeodin.yaml --out /tmp/antibioticmech-bisdechlorogeodin-validation.tsv`
- `just verify-corpus`
- `just qc`
- `git diff -- data/antibiotics/unspecified/bisdechlorogeodin.yaml curation/decisions.tsv src scripts tests`
- `just review-queue --limit 0 --tsv curation/record_review_queue.tsv`

## Additional Notes

Searches used to establish absence included ignored files:

- `rg --hidden --no-ignore` over `curation/`, `data/raw/`, and
  `reports/yaml_record_review/` for `CHEBI:15390`,
  `JCMPRFCVZKOFIT-KRWDZBQOSA-N`, `59092-96-5`, `C03036`, and
  `bisdechlorogeodin`.
- `rg --hidden --no-ignore` over `data/antibiotics`, `data/raw`, `curation`,
  and `reports` for `CHEBI:15390`, `JCMPRFCVZKOFIT-KRWDZBQOSA-N`,
  `59092-96-5`, and `kegg.compound:C03036`.

`NCBI_EMAIL` was unset for the PubMed searches. The exact label/name search
returned broad PubMed and Semantic Scholar leads; the identifier search found
no PubMed candidates and Semantic Scholar returned an invalid response, so that
provider was not available for the registry-identifier pass.

This report is read-only review output. No generated record, upstream
inventory, decision row, page, queue, or curation-history entry was edited.
