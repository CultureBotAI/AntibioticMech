# YAML Record Review: nalidixic acid

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antibacterial/nalidixic-acid.yaml`
- Started UTC: 2026-09-21T04:54:46Z
- Finished UTC: 2026-09-21T04:55:32Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/antibiotics/antibacterial/nalidixic-acid.yaml` |
| Class | `ANTIBACTERIAL` |
| ID | `CHEBI:100147` |
| Label | `nalidixic acid` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained status | Generated from `data/raw/` inventories plus curator-owned generated fields |

The record denotes the ChEBI-grounded nalidixic acid structure with InChIKey
`MHWLWQUZZRMNGJ-UHFFFAOYSA-N`, an ARO source concept `ARO:3000661`, a
ChEBI source concept `CHEBI:100147`, 35 CARD/ARO resistance assertions, two
molecular-target assertions, one curator-added causal graph, 10 US-FDA clinical
status assertions, and no `Discussion` entries.

## Validation

| Command | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/nalidixic-acid.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/nalidixic-acid.yaml --out /tmp/antibioticmech-nalidixic-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2,939 expected records, 2,939 records on disk, no missing records, no unexpected records, no drifted fields, no `PATHS.tsv` drift. |
| `just review-queue --limit 5` | Confirmed `nalidixic acid` remains in `review-readiness`: `TARGET_EVIDENCE_REVIEW`, one target assertion needing primary evidence. |

No separate single-record term, reference, or history validator is documented in
the local `justfile`. A later local `just qc` attempt stopped during dependency
resolution because pinned `rdkit==2026.3.5` has no macOS x86_64 wheel; the full
Linux gate is therefore left to required PR CI.

## Identity and Grounding

`nalidixic-acid.yaml` resolves unambiguously under
`data/antibiotics/antibacterial/`. The generated lock row in
`data/antibiotics/PATHS.tsv` maps `CHEBI:100147` to
`ANTIBACTERIAL/nalidixic-acid`, and `source_concepts` carry the expected
`ARO:3000661` and `CHEBI:100147` upstream identities.

The exact structure block matches the committed ChEBI antimicrobial inventory
row for `CHEBI:100147`: SMILES, Standard InChI, InChIKey
`MHWLWQUZZRMNGJ-UHFFFAOYSA-N`, formula `C12H12N2O3`, charge `0`, average mass,
and monoisotopic mass agree with `data/raw/chebi_antimicrobials.tsv`.

No conflicting local grounding decision was found for
`antibioticmech:aro-4cf71250ed` or `antibioticmech:chebi-561a3b207f` in a
gitignore-independent search over `curation/`, `data/`, and
`reports/yaml_record_review/` with `rg --hidden --no-ignore`; the only matches
were the two `source_concepts` inside this record.

## Evidence

The generated identity, label, synonyms, exact structure, parent compounds,
xrefs, filing class, activity roles, structural class, source concepts,
resistance assertions, BindingDB target measurement, and clinical status
assertions reproduce from the committed inventories with no `verify-corpus`
drift.

The 35 `resistance_mechanisms` entries are imported CARD/ARO database
assertions from `data/raw/aro_resistance_edges.tsv`. Each item cites its own
`ARO:*` identifier and states that the edge is a CARD/ARO assertion rather than
a primary paper; this is honest database provenance, not a primary-literature
upgrade.

One `molecular_targets` entry is source-owned CARD/ARO content:
`ARO:3000733`, `fluoroquinolone sensitive gyrA`, imported from
`data/raw/aro_target_edges.tsv`. Its `evidence_status:
PRIMARY_EVIDENCE_NEEDED`, `source: CARD_ARO`, and `ARO:3000733` evidence
accurately describe an unresolved database assertion. That row still lacks
compound-level primary support attached directly to the target claim.

The other `molecular_targets` entry is imported BindingDB content for
`Bacillus subtilis` DNA topoisomerase IV subunit A [V210L]/B. Its retained
measurement matches `data/raw/bindingdb_target_measurements.tsv`: IC50
`1090000` nM, assay `2532_2`, BindingDB reaction set `39230`, monomer `21691`,
and `PMID:17074800`.

The curator-owned `nalidixic_acid_gyrase_cleavage_complex` causal graph carries
edge-level `PMID:200930` references. A gitignore-independent search over the
record, `data/raw/`, and `curation/` found `PMID:200930` only in the generated
nalidixic acid YAML, so the graph is the local owner for those paper-backed
mechanism assertions. This pass did not re-inspect the paper text for that PMID
and therefore did not revalidate the exact wording of the graph edge notes
against the primary article.

## Completeness

The record has a defensible exact identity, structure, filing class, curated
mode of action, target scope, causal graph, imported CARD/ARO resistance rows,
one BindingDB quantitative target row, and FDA-derived clinical approvals.

The consequential remaining gap is sign-off of the imported CARD/ARO GyrA
target row. The causal graph reviews the DNA gyrase mechanism, but it does not
rewrite `molecular_targets[0]`, whose target label remains the CARD/ARO
`fluoroquinolone sensitive gyrA` assertion with no organism, strain, assay, or
primary article.

No activity observations, producer claims, public datasets, structural
observations, or discussions are present. The review found no specific local
evidence that any of those optional sections must be populated before the
CARD/ARO target claim is curated.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The source-owned CARD/ARO molecular target assertion still needs primary evidence before the record can be `REVIEWED`. | `molecular_targets[0]` is the imported `ARO:3000733` `fluoroquinolone sensitive gyrA` row with `evidence_status: PRIMARY_EVIDENCE_NEEDED`, and `just review-queue --limit 5` keeps `nalidixic acid` in `TARGET_EVIDENCE_REVIEW`. | Either the ARO target import/merge path that emits the `ARO:3000733` row or a curator-owned target replacement written to `data/antibiotics/antibacterial/nalidixic-acid.yaml` through `write_validated_antibiotic`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Decide whether the coarse CARD/ARO `ARO:3000733` target row should be
   replaced by a curator-owned, primary-paper-backed bacterial DNA gyrase
   target or retained as a queued database assertion.
2. If it is retained, leave `curation_status: SEEDED` and keep the record in
   `TARGET_EVIDENCE_REVIEW`.
3. If it is replaced or upgraded, write only through a guarded mutator that
   asserts `identifier == "CHEBI:100147"`, updates the `molecular_targets`
   slice, appends a `codex` `CurationEvent` with `llm_assisted: true`, and
   emits via `write_validated_antibiotic`.
4. Move `curation_status` to `REVIEWED` only after the upgraded target plus the
   already curated identity, structure, class, mode of action, causal graph,
   and BindingDB target row satisfy the `docs/CURATION.md` sign-off criteria.

## Follow-up Checks

After a future target curation edit:

- `just validate-strict data/antibiotics/antibacterial/nalidixic-acid.yaml --out /tmp/antibioticmech-nalidixic-validation.tsv`
- `just verify-corpus`
- `just qc`
- `git diff -- data/antibiotics/antibacterial/nalidixic-acid.yaml curation/decisions.tsv src scripts tests`
- `just review-queue --limit 0 --tsv curation/record_review_queue.tsv`

## Additional Notes

Searches used to establish absence included ignored files:

- `rg --hidden --no-ignore` over `curation/`, `data/`, and
  `reports/yaml_record_review/` for `CHEBI:100147`, `ARO:3000661`,
  `nalidixic acid`, `antibioticmech:aro-4cf71250ed`, and
  `antibioticmech:chebi-561a3b207f`.
- `rg --hidden --no-ignore` over the target record, `data/raw/`, and
  `curation/` for `PMID:200930` and `PMID:17074800`.

Not checked: external paper text for `PMID:200930` or `PMID:17074800`.

This report is read-only review output. No generated record, upstream
inventory, decision row, page, queue, or curation-history entry was edited.
