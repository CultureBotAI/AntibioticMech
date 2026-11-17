# YAML Record Review: (S)-tosufloxacin

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/unspecified/s-tosufloxacin.yaml
- Started UTC: 2026-09-24T02:50:48Z
- Finished UTC: 2026-09-24T02:50:54Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | CHEBI:77582 |
| Label | (S)-tosufloxacin |
| Path | data/antibiotics/unspecified/s-tosufloxacin.yaml |
| Class | ANTIMICROBIAL_UNSPECIFIED |
| Status | SEEDED |
| Grounding | EXACT |
| Source concept | CHEBI:77582, source version 2026-08-30 |
| Standard InChIKey | WUWFMDMBOJLQIV-JTQLQIEISA-N |
| Maintained owner | Generated from data/raw/chebi_antimicrobials.tsv plus data/antibiotics/PATHS.tsv; do not hand-edit the generated YAML |

The target resolves unambiguously to `data/antibiotics/unspecified/s-tosufloxacin.yaml`.
An ignored-file-inclusive search for `CHEBI:77582`, `(S)-tosufloxacin`,
`s-tosufloxacin`, and `tosufloxacin` across `data/antibiotics`, `data/raw`,
`curation`, and `reports/yaml_record_review` found the target, its
`(R)-tosufloxacin` sibling, tosufloxacin tosylate records, the achiral
`tosufloxacin` ARO/CHEBI merge record, the corresponding `PATHS.tsv` rows, the
ChEBI/ARO/PubChem raw rows, `curation/record_review_queue.tsv`, and the prior
`(R)-tosufloxacin` sibling report. A separate ignored-file-inclusive `find`
found no exact prior `reports/yaml_record_review/*s-tosufloxacin*` report.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/s-tosufloxacin.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/s-tosufloxacin.yaml --out /tmp/s-tosufloxacin-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2939 records expected, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/s-tosufloxacin-worklist.tsv` | Passed; `CHEBI:77582` appears only in `mechanism` and `review-readiness`. |
| `just review-queue --limit 180` | Passed; `CHEBI:77582` is the next unreviewed queue row after the already reviewed `(S)-temafloxacin` row. |
| `just lint` | Passed; `ruff` reported `All checks passed!`. |
| `git diff --cached --check` | Passed after staging this ignored report. |

`just verify-corpus` and `just worklist` both emitted the known CARD
`ARO:3000337` / iclaprim cross-reference refusal; that warning is unrelated to
this ChEBI-only record.

The repository exposes `validate`, `validate-strict`, `verify-corpus`,
`worklist`, `review-queue`, and `lint`; it does not expose narrower
single-record term, reference, or history validators for a plain ChEBI-seeded
record with no record-level citations.

## Identity and Grounding

The ChEBI identity is exact. OLS4 resolves `CHEBI:77582` to `(S)-tosufloxacin`
with the same definition, SMILES, Standard InChI, Standard InChIKey, formula,
charge, average mass, monoisotopic mass, `reaxys:4913118` xref, and IUPAC
synonym carried by the local raw ChEBI row and generated record.

The stereochemical boundary is correct:

- `CHEBI:77581` is the broader nonstereospecific parent and has the
  nonstereospecific InChIKey `WUWFMDMBOJLQIV-UHFFFAOYSA-N`.
- `CHEBI:77582` is the `(S)` enantiomer and has InChIKey
  `WUWFMDMBOJLQIV-JTQLQIEISA-N`.
- The local sibling `data/antibiotics/unspecified/r-tosufloxacin.yaml` carries
  `CHEBI:77584` with the mirror-image InChIKey
  `WUWFMDMBOJLQIV-SNVBAGLBSA-N`.
- OLS4 also surfaced `CHEBI:77594`, `(S)-tosufloxacin(1+)`; that protonation
  state is correctly not present as an exact xref.

The achiral parent merged with ARO `ARO:3004499` / `tosufloxacin` through
PubChem CID 5517, while the exact `(S)` enantiomer record remains a ChEBI-only
structure. The ARO, PubChem, ChEMBL, LINCS, and CAS xrefs on the achiral record
were not copied onto this enantiomer-specific record.

The filing class is consistent with imported source assertions. ChEBI assigns
only the generic `CHEBI:33281` antimicrobial role to `CHEBI:77582`, while the
achiral ARO/PubChem merge is filed as `ANTIBACTERIAL`.

## Evidence

This record has no record-level `evidence`, no `mode_of_action`, no
`molecular_targets`, no `activity_spectrum`, no `resistance_mechanisms`, and no
`causal_graphs`. That is structurally valid for a ChEBI-seeded entry, but it
means the exact `(S)` enantiomer has only upstream database provenance and no
primary-paper support for a compound-specific antimicrobial mechanism.

The local raw ChEBI row for `CHEBI:77582` has no PMID leads. Bounded PubMed
checks did not identify immediately supportable exact-enantiomer evidence:

- Exact PubMed query:
  `WUWFMDMBOJLQIV-JTQLQIEISA-N OR CHEBI:77582 OR "(S)-tosufloxacin" OR "S-tosufloxacin" OR "tosufloxacin enantiomer"`.
  PubMed did not match the InChIKey or quoted exact-name phrases and broadened
  the translation to `tosufloxacin`.
- Broader PubMed query:
  `tosufloxacin[Title/Abstract] AND (topoisomerase[Title/Abstract] OR "DNA gyrase"[Title/Abstract] OR mechanism[Title/Abstract] OR enantiomer[Title/Abstract])`.
  This returned 22 broad tosufloxacin mechanism or fluoroquinolone leads, but no
  inspected primary claim for the exact `(S)` enantiomer.

The adjacent achiral free-base record and the two tosylate salt records are
useful discovery context, not exact evidence for this YAML record. They should
not be projected onto `CHEBI:77582` unless a curator inspects sources that
justify transferring an achiral, racemic, or salt observation to the isolated
`(S)` free base.

Semantic Scholar was not needed after the exact PubMed query found no
identifier or exact-name match and there were no source PMIDs to resolve
through a second provider. Google Scholar was not used.

## Completeness

The generated source concept, exact ChEBI grounding, parent boundary, structure
fields, filing class, and history are sufficient for a ChEBI-seeded entry.

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, and
  `causal_graphs` are absent. This record should remain below `REVIEWED` until
  a curator either adds evidence that supports a tosufloxacin mechanism for this
  enantiomer or adds a curator-owned veto explaining why only achiral, racemic,
  or salt-form leads exist.
- `activity_spectrum` is absent. Future curation should use actual measured
  organism, strain or isolate, assay, value, qualifier, units, compound form,
  and evidence rather than generalizing from the generic fluoroquinolone class.

Empty optional slots that are acceptable in this generated seed:

- `resistance_mechanisms`: no CARD target or resistance edge was available for
  this exact ChEBI record.
- `producer_organisms`: no producer-candidate worklist row was present.
- `clinical_status_assertions`: no regulatory source was imported for this
  exact ChEBI record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record has no reviewed mechanism for the exact `(S)` enantiomer. | `just worklist --limit 0 --tsv /tmp/s-tosufloxacin-worklist.tsv` lists `CHEBI:77582` in `mechanism` with `0 CARD target(s), 0 resistance edge(s) to build on` and in `review-readiness` with `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`; exact PubMed searching found no exact `(S)-tosufloxacin`, `CHEBI:77582`, or InChIKey hit. | Add an evidence-backed curator-owned mechanism to `data/antibiotics/unspecified/s-tosufloxacin.yaml` through `write_validated_antibiotic`, or add a curator-owned veto explaining why the mechanism remains unknown for this enantiomer. |

No blockers found. No minor findings found.

## Recommended Edits

1. Inspect sources behind the achiral tosufloxacin record and broader
   tosufloxacin/topoisomerase PubMed leads for mechanism evidence. Curate this
   record only when the source supports the exact `(S)` free base or justifies
   projecting achiral, racemic, or salt evidence onto the isolated enantiomer.
2. Add a `CURATOR:`-owned mechanism, molecular target, and causal graph when
   evidence is exact enough; otherwise leave a curator-owned veto documenting
   that no exact-enantiomer mechanism was found.
3. Add only measured `activity_spectrum` rows with complete organism, strain or
   isolate, assay, value, units, compound form, and evidence.

## Follow-up Checks

- After any mechanism or activity curation, run
  `just validate-strict data/antibiotics/unspecified/s-tosufloxacin.yaml --out /tmp/antibioticmech-record-validation.tsv`,
  `just verify-corpus --summary`,
  `just worklist --limit 0 --tsv /tmp/s-tosufloxacin-worklist.tsv`, and
  `just lint`.
- Re-run OLS4 checks for `CHEBI:77582`, `CHEBI:77581`, `CHEBI:77584`, and
  `CHEBI:77594` if future edits touch identity, xrefs, or parentage.

## Additional Notes

- The ignored-file-inclusive resolution search covered `data/antibiotics`,
  `data/raw`, `curation`, and `reports/yaml_record_review`; a separate
  ignored-file-inclusive `find` found no prior exact report for
  `s-tosufloxacin`.
- OLS4 relation payloads for `CHEBI:77582` surfaced neighboring ChEBI enantiomer
  and protonation terms. OLS4 did not expose the generic `CHEBI:33281`
  antimicrobial role in the inspected `CHEBI:77582` term payload, so that role
  was verified from the local raw ChEBI inventory.
- The repository exposes only full-corpus worklist categories for mechanism,
  cross-reference, producer, target-evidence, and review-readiness checks.
  `CHEBI:77582` was absent from all inspected queues except `mechanism` and
  `review-readiness`.
