# YAML Record Review: clarithromycin

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antibacterial/clarithromycin.yaml`
- Started UTC: 2026-09-21T04:15:35Z
- Finished UTC: 2026-09-21T04:16:40Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/antibiotics/antibacterial/clarithromycin.yaml` |
| Class | `ANTIBACTERIAL` |
| ID | `CHEBI:3732` |
| Label | `clarithromycin` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained status | Generated from `data/raw/` inventories plus curator-owned generated fields |

The record denotes the ChEBI-grounded clarithromycin structure with InChIKey
`AGOYDEPGAOXOCK-KCBOHYOISA-N`, an ARO source concept
`ARO:0000065`, a ChEBI source concept `CHEBI:3732`, 44 CARD/ARO
resistance assertions, one CARD/ARO molecular-target assertion, one
curator-added causal graph, 45 US-FDA clinical status assertions, and no
`Discussion` entries.

## Validation

| Command | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/clarithromycin.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/clarithromycin.yaml --out /tmp/antibioticmech-clarithromycin-validation.tsv` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `just verify-corpus --summary` | Passed: 2,939 expected records, 2,939 records on disk, no missing records, no unexpected records, no drifted fields, no `PATHS.tsv` drift. |
| `just review-queue --limit 5` | Confirmed `clarithromycin` remains first in `review-readiness`: `TARGET_EVIDENCE_REVIEW`, one target assertion needing primary evidence. |

No separate single-record term, reference, or history validator is documented in
the local `justfile`. The full `just qc` gate was left for the PR-level check
after this report because this review made no YAML mutation.

## Identity and Grounding

`clarithromycin.yaml` resolves unambiguously under
`data/antibiotics/antibacterial/`. The generated lock row in
`data/antibiotics/PATHS.tsv` maps `CHEBI:3732` to
`ANTIBACTERIAL/clarithromycin`, and `source_concepts` carry the expected
`ARO:0000065` and `CHEBI:3732` upstream identities.

The exact structure block matches the committed ChEBI antimicrobial inventory
row for `CHEBI:3732`: SMILES, Standard InChI, InChIKey
`AGOYDEPGAOXOCK-KCBOHYOISA-N`, formula `C38H69NO13`, charge `0`, average mass,
and monoisotopic mass agree with `data/raw/chebi_antimicrobials.tsv`.

No conflicting local grounding decision was found for
`antibioticmech:aro-5c92a4ddc8` or `antibioticmech:chebi-e63133b2eb` in a
gitignore-independent search over `curation/` and `data/` with
`rg --hidden --no-ignore`; the only matches were the two `source_concepts`
inside this record.

## Evidence

The generated identity, label, synonyms, exact structure, parent compounds,
xrefs, filing class, activity roles, structural class, source concepts,
resistance assertions, and clinical status assertions reproduce from the
committed inventories with no `verify-corpus` drift.

The 44 `resistance_mechanisms` entries are imported CARD/ARO database
assertions from `data/raw/aro_resistance_edges.tsv`. Each item cites its own
`ARO:*` identifier and states that the edge is a CARD/ARO assertion rather than
a primary paper; this is honest database provenance, not a primary-literature
upgrade.

The one `molecular_targets` entry is also source-owned:
`ARO:3000757`, `50S ribosomal subunit P-site`, imported from
`data/raw/aro_target_edges.tsv`. Its `evidence_status:
PRIMARY_EVIDENCE_NEEDED`, `source: CARD_ARO`, and `ARO:3000757` evidence
accurately describe an unresolved database assertion. That row still lacks
compound-level primary support attached directly to the target claim.

The curator-owned `clarithromycin_50s_exit_tunnel_inhibition` causal graph
carries edge-level `PMID:34935599` and `PMID:9425251` references. A
gitignore-independent search over the record, `data/raw/`, and `curation/`
found those two PMIDs only in the generated clarithromycin YAML, so the graph
is the local owner for those paper-backed mechanism assertions. This pass did
not re-inspect the paper text for either PMID and therefore did not revalidate
the exact wording of the graph edge notes against the primary articles.

## Completeness

The record has a defensible exact identity, structure, filing class, curated
mode of action, target scope, causal graph, imported CARD/ARO resistance rows,
and FDA-derived clinical approvals.

The consequential remaining gap is sign-off of the imported target row. The
causal graph reviews the more precise 50S exit-tunnel mechanism, but it does
not rewrite `molecular_targets[0]`, whose target label remains the coarser
CARD/ARO `50S ribosomal subunit P-site` with no organism, strain, assay, or
primary article.

No activity observations, producer claims, public datasets, structural
observations, or discussions are present. The review found no specific local
evidence that any of those optional sections must be populated before the target
claim is curated.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The source-owned molecular target assertion still needs primary evidence before the record can be `REVIEWED`. | `molecular_targets[0]` is the imported `ARO:3000757` `50S ribosomal subunit P-site` row with `evidence_status: PRIMARY_EVIDENCE_NEEDED`, and `just review-queue --limit 5` keeps `clarithromycin` in `TARGET_EVIDENCE_REVIEW`. | Either the ARO target import/merge path that emits the `ARO:3000757` row or a curator-owned target replacement written to `data/antibiotics/antibacterial/clarithromycin.yaml` through `write_validated_antibiotic`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Decide whether the coarse CARD/ARO `ARO:3000757` target row should be
   replaced by a curator-owned, primary-paper-backed 50S macrolide-site target
   or retained as a queued database assertion.
2. If it is retained, leave `curation_status: SEEDED` and keep the record in
   `TARGET_EVIDENCE_REVIEW`.
3. If it is replaced or upgraded, write only through a guarded mutator that
   asserts `identifier == "CHEBI:3732"`, updates the `molecular_targets` slice,
   appends a `codex` `CurationEvent` with `llm_assisted: true`, and emits via
   `write_validated_antibiotic`.
4. Move `curation_status` to `REVIEWED` only after the upgraded target plus the
   already curated identity, structure, class, mode of action, and causal graph
   satisfy the `docs/CURATION.md` sign-off criteria.

## Follow-up Checks

After a future target curation edit:

- `just validate-strict data/antibiotics/antibacterial/clarithromycin.yaml --out /tmp/antibioticmech-clarithromycin-validation.tsv`
- `just verify-corpus`
- `just qc`
- `git diff -- data/antibiotics/antibacterial/clarithromycin.yaml curation/decisions.tsv src scripts tests`
- `just review-queue --limit 0 --tsv curation/record_review_queue.tsv`

## Additional Notes

Searches used to establish absence included ignored files:

- `rg --hidden --no-ignore` over `curation/`, `data/`, and the target record for
  `CHEBI:3732`, `ARO:0000065`, `clarithromycin`,
  `antibioticmech:aro-5c92a4ddc8`, and
  `antibioticmech:chebi-e63133b2eb`.
- `rg --hidden --no-ignore` over the target record, `data/raw/`, and
  `curation/` for `PMID:34935599` and `PMID:9425251`.

Not checked: external paper text for `PMID:34935599` or `PMID:9425251`.

This report is read-only review output. No generated record, upstream
inventory, decision row, page, queue, or curation-history entry was edited.
