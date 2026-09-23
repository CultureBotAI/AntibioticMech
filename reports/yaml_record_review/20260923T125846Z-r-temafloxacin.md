# YAML Record Review: (R)-temafloxacin

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antibacterial/r-temafloxacin.yaml
- Started UTC: 2026-09-23T12:58:46Z
- Finished UTC: 2026-09-23T13:01:45Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | CHEBI:77794 |
| Label | (R)-temafloxacin |
| Path | data/antibiotics/antibacterial/r-temafloxacin.yaml |
| Class | ANTIBACTERIAL |
| Status | SEEDED |
| Grounding | EXACT |
| Source concept | CHEBI:77794, source version 2026-08-30 |
| Standard InChIKey | QKDHBVNJCZBTMR-LLVKDONJSA-N |
| Maintained owner | Generated from data/raw/chebi_antimicrobials.tsv plus data/antibiotics/PATHS.tsv; do not hand-edit the generated YAML |

The target resolves unambiguously to `data/antibiotics/antibacterial/r-temafloxacin.yaml`.
An ignored-file-inclusive search for `CHEBI:77794`, `(R)-temafloxacin`,
`r-temafloxacin`, and `temafloxacin` across `data`, `curation`, and
`reports` found the target record, its sibling `s-temafloxacin.yaml`, the
corresponding `PATHS.tsv`, `data/raw/chebi_antimicrobials.tsv`, and
`curation/record_review_queue.tsv` rows. The same search found no prior
`reports/yaml_record_review/` report for this stem.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antibacterial/r-temafloxacin.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antibacterial/r-temafloxacin.yaml --out /tmp/r-temafloxacin-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2939 records expected, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `just review-queue --limit 130` | Passed; `CHEBI:77794` is the first queue entry after the already reviewed `(R)-quinacrine` row. |
| `just worklist --limit 0 --tsv /tmp/r-temafloxacin-worklist.tsv` | Passed; `CHEBI:77794` appears only in `mechanism` and `review-readiness`. |
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

The ChEBI identity is exact. OLS4 resolves `CHEBI:77794` to `(R)-temafloxacin`
with the same definition, SMILES, Standard InChI, Standard InChIKey, formula,
charge, average mass, monoisotopic mass, `pubmed:1846917` xref, and
`reaxys:4301728` xref carried by the local raw ChEBI row and generated record.

The stereochemical boundary is correct:

- `CHEBI:77796` is the broader nonstereospecific parent and has the
  nonstereospecific InChIKey `QKDHBVNJCZBTMR-UHFFFAOYSA-N`.
- `CHEBI:77794` is the `(R)` enantiomer and has InChIKey
  `QKDHBVNJCZBTMR-LLVKDONJSA-N`.
- The local sibling `data/antibiotics/antibacterial/s-temafloxacin.yaml` carries
  `CHEBI:77795` with the mirror-image InChIKey
  `QKDHBVNJCZBTMR-NSHDSACASA-N`.

The local `parent_compounds` value `CHEBI:77796` is strictly broader than this
record, and neither the racemate record's drug xrefs nor the sibling
`(S)-temafloxacin` Reaxys xref were inappropriately copied onto the
`(R)`-specific record.

Two ChEBI related synonyms were flattened to exact synonyms. OLS4 reports
`(+)-temafloxacin` and `(R)-(+)-temafloxacin` on `CHEBI:77794` with
`scope: hasRelatedSynonym`, while the local generated record emits both as
`EXACT_SYNONYM`.

## Evidence

This record has no record-level `evidence`, no `activity_spectrum`, no
`molecular_targets`, no `resistance_mechanisms`, no `producer_organisms`, and
no `causal_graphs`. That is structurally valid for a ChEBI-seeded entry, but it
means the record has only upstream database provenance and no primary-paper
support for a compound-specific antibacterial mechanism.

The ChEBI mechanism import itself is traceable: the local raw ChEBI row for
`CHEBI:77794` carries `CHEBI:50750`, and OLS4 resolves that role to
`EC 5.99.1.3 [DNA topoisomerase (ATP-hydrolysing)] inhibitor`, with DNA gyrase
listed as a related synonym. The generated record's `NUCLEIC_ACID_SYNTHESIS_INHIBITION`
value is therefore an honest restatement of a ChEBI role, but it remains
source-seeded, target-family-level, and not curator-checked.

The only ChEBI PMID lead for the exact enantiomer is `PMID:1846917`. PubMed
resolves it to Chu et al. 1991, "Synthesis, antibacterial activities, and
pharmacological properties of enantiomers of temafloxacin hydrochloride," DOI
`10.1021/jm00105a025`. The PubMed abstract supports synthesis and antibacterial
testing of temafloxacin hydrochloride enantiomers, but it does not identify a
molecular target, causal edge, or complete activity measurements that could be
promoted into this exact free-base record without inspecting the full paper.

Bounded publication checks did not identify an immediately supportable exact
`(R)-temafloxacin` mechanism:

- Exact PubMed query:
  `QKDHBVNJCZBTMR-LLVKDONJSA-N OR CHEBI:77794 OR "(R)-(+)-temafloxacin" OR "(+)-temafloxacin"`.
  PubMed did not match the InChIKey, ChEBI CURIE, or `(R)-(+)-temafloxacin`
  phrase and broadened the translation to `temafloxacin`.
- Broader PubMed query:
  `temafloxacin[Title/Abstract] AND ("DNA gyrase"[Title/Abstract] OR topoisomerase[Title/Abstract] OR mechanism[Title/Abstract])`.
  This returned 15 temafloxacin or fluoroquinolone mechanism/resistance leads,
  including non-stereospecific papers on resistance to temafloxacin or
  fluoroquinolones; none was an inspected primary claim for the exact
  `(R)` enantiomer.

Semantic Scholar returned HTTP 429 for `PMID:1846917`, so PubMed was the only
successful literature provider. Google Scholar was not used.

## Completeness

The generated source concept, exact ChEBI grounding, parent boundary, structure
fields, xref, class, activity roles, and history are sufficient for a
ChEBI-seeded entry after the related-synonym scope defect is corrected upstream.

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, and
  `causal_graphs` need curator review. The current mechanism block is a
  source-seeded ChEBI restatement, and the record should remain below `REVIEWED`
  until a curator either adds an evidence-backed gyrase or topoisomerase target
  claim for temafloxacin or leaves an explicit curator-owned veto.
- `activity_spectrum` is absent. `PMID:1846917` appears likely to contain
  antibacterial measurements for the enantiomers, but future curation must use
  the actual measured organism, strain or isolate, assay, value, qualifier,
  units, and compound form rather than inferring MIC rows from the PubMed
  abstract.

Empty optional slots that are acceptable in this generated seed:

- `resistance_mechanisms`: no CARD target or resistance edge was available for
  this exact ChEBI record.
- `producer_organisms`: no producer-candidate worklist row was present.
- `clinical_status_assertions`: the racemic temafloxacin entry, not this
  isolated free-base enantiomer, carries the marketed-drug xrefs.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Related ChEBI synonyms were emitted as exact synonyms. | OLS4 lists `(+)-temafloxacin` and `(R)-(+)-temafloxacin` on `CHEBI:77794` with `scope: hasRelatedSynonym`, but `r-temafloxacin.yaml` marks both as `EXACT_SYNONYM`. | Preserve synonym scope in the ChEBI extraction/seeding path, then refresh `data/raw/chebi_antimicrobials.tsv` and re-run `just seed-apply`. The local flattening currently enters through `scripts/seed_from_sources.py`. |
| Major | The source-seeded topoisomerase mechanism has not been reviewed against claim-level primary evidence. | `r-temafloxacin.yaml` has `mode_of_action: NUCLEIC_ACID_SYNTHESIS_INHIBITION` with seeder-owned notes, zero `molecular_targets`, and zero `causal_graphs`; `just worklist --limit 0 --tsv /tmp/r-temafloxacin-worklist.tsv` lists `CHEBI:77794` under `mechanism` with `0 CARD target(s), 0 resistance edge(s) to build on` and under `review-readiness` as source-seeded and not curator-checked. | Add an evidence-backed curator-owned mechanism, molecular target, and causal graph through `write_validated_antibiotic`, or add a curator-owned veto explaining why the mechanism remains unresolved. |

No blockers found. No minor findings found.

## Recommended Edits

1. Preserve ChEBI synonym scope in the import path so `hasRelatedSynonym`
   values remain related or are omitted from `CompoundSynonym` until the schema
   can represent them. Re-extract ChEBI and re-seed; the regenerated
   `(R)-temafloxacin` record should no longer label related ChEBI synonyms as
   exact synonyms.
2. Inspect `PMID:1846917` in full, and the 15 non-stereospecific PubMed
   mechanism leads if necessary, before replacing the source-seeded
   topoisomerase mechanism with a `CURATOR:`-owned mechanism and target.
   Preserve the distinction between exact `(R)-temafloxacin`, racemic
   temafloxacin, and hydrochloride salt evidence.
3. Add only measured `activity_spectrum` rows with complete method, organism,
   strain or isolate, value, units, compound form, and evidence.

## Follow-up Checks

- Re-run `just seed-apply`, then
  `just validate data/antibiotics/antibacterial/r-temafloxacin.yaml` and
  `just verify-corpus --summary`; confirm the record no longer emits ChEBI
  `hasRelatedSynonym` values as `EXACT_SYNONYM`.
- Run the OLS4 exact-term check for `CHEBI:77794` and confirm generated
  synonyms reflect OBO synonym scopes.
- After any mechanism or activity curation, run
  `just validate-strict data/antibiotics/antibacterial/r-temafloxacin.yaml --out /tmp/antibioticmech-record-validation.tsv`,
  `just verify-corpus --summary`,
  `just worklist --limit 0 --tsv /tmp/r-temafloxacin-worklist.tsv`, and
  `just lint`.

## Additional Notes

- The first ignored-file-inclusive resolution search covered `data`, `curation`,
  `reports`, `.claude`, `CLAUDE.md`, and `justfile`, but it also matched the
  generated embedding JSON files and produced truncated output. A second
  ignored-file-inclusive search was restricted to YAML, TSV, and Markdown under
  `data`, `curation`, and `reports`, confirmed the target and neighbor rows, and
  found no prior review report for `r-temafloxacin`.
- OLS4's `has_role` relation endpoint for `CHEBI:77794` returned
  `CHEBI:36047` and `CHEBI:50750`, plus `CHEBI:35441` as a role ancestor. The
  local ChEBI inventory also carries `CHEBI:33281`, the generic antimicrobial
  activity role retained in the generated record.
- The repository exposes only full-corpus worklist categories for mechanism,
  cross-reference, producer, target-evidence, and review-readiness checks.
  `CHEBI:77794` was absent from all inspected queues except `mechanism` and
  `review-readiness`.
