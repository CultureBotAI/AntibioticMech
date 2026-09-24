# YAML Record Review: (Z)-2-(2-furyl)-3-(5-nitro-2-furyl)acrylamide

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/unspecified/z-2-2-furyl-3-5-nitro-2-furyl-acrylamide.yaml
- Started UTC: 2026-09-24T03:20:46Z
- Finished UTC: 2026-09-24T03:21:00Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | CHEBI:15660 |
| Label | (Z)-2-(2-furyl)-3-(5-nitro-2-furyl)acrylamide |
| Path | data/antibiotics/unspecified/z-2-2-furyl-3-5-nitro-2-furyl-acrylamide.yaml |
| Class | ANTIMICROBIAL_UNSPECIFIED |
| Status | SEEDED |
| Grounding | EXACT |
| Source concept | CHEBI:15660, source version 2026-08-30 |
| Standard InChIKey | LYAHJFZLDZDIOH-VURMDHGXSA-N |
| Maintained owner | Generated from data/raw/chebi_antimicrobials.tsv plus data/antibiotics/PATHS.tsv; do not hand-edit the generated YAML |

The target resolves unambiguously to
`data/antibiotics/unspecified/z-2-2-furyl-3-5-nitro-2-furyl-acrylamide.yaml`.
An ignored-file-inclusive search for `CHEBI:15660`,
`(Z)-2-(2-furyl)-3-(5-nitro-2-furyl)acrylamide`, the full file slug, and
`5-nitro-2-furyl` across `data/antibiotics`, `data/raw`, `curation`, and
`reports/yaml_record_review` found the target, the exact `PATHS.tsv` row, the
exact raw ChEBI row, the exact `review-readiness` queue row, and related
nitrofuran records. A separate ignored-file-inclusive `find` found no prior
exact `reports/yaml_record_review/*z-2-2-furyl-3-5-nitro-2-furyl-acrylamide*`
report.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/unspecified/z-2-2-furyl-3-5-nitro-2-furyl-acrylamide.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/z-2-2-furyl-3-5-nitro-2-furyl-acrylamide.yaml --out /tmp/z-furyl-nitrofuryl-acrylamide-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2939 records expected, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `just worklist --limit 0 --tsv /tmp/z-furyl-nitrofuryl-acrylamide-worklist.tsv` | Passed; `CHEBI:15660` appears only in `mechanism` and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Passed; `CHEBI:15660` is the first queue row without an exact one-record review report after normalizing backticked and unbackticked report headers. |
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

The ChEBI identity is exact. OLS4 resolves `CHEBI:15660` to
`(Z)-2-(2-furyl)-3-(5-nitro-2-furyl)acrylamide` with the same formula, Standard
InChI, Standard InChIKey `LYAHJFZLDZDIOH-VURMDHGXSA-N`, charge, average mass,
monoisotopic mass, `cas:3688-53-7`, `kegg.compound:C04622`,
`kegg.compound:C19558`, `kegg.drug:D02528`, `wikipedia.en:Furylfuramide`, and
the same exact-name synonyms carried by the local raw ChEBI row and generated
record.

The `parent_compounds` values are strictly broader ChEBI terms:

- `CHEBI:140324`: primary carboxamide.
- `CHEBI:22216`: acrylamides.
- `CHEBI:35716`: C-nitro compound.
- `CHEBI:87230`: nitrofuran antibiotic.

The exact record is a ChEBI-only structure with no CARD/ARO merge. Nearby
nitrofurans such as furazolidone, nitrofurazone, nitrofurantoin, furaltadone,
nifurtoinol, furagin, and sodium nifurstyrenate are structurally related but
have distinct identifiers, InChIKeys, and record paths; none of their xrefs or
literature leads were projected onto `CHEBI:15660`.

The filing class is consistent with imported source assertions. ChEBI assigns
only the generic `CHEBI:33281` antimicrobial role to `CHEBI:15660`, so the
record is filed as `ANTIMICROBIAL_UNSPECIFIED` rather than as antibacterial
solely because a broader nitrofuran-antibiotic parent is present.

## Evidence

This record has no record-level `evidence`, no `mode_of_action`, no
`molecular_targets`, no `activity_spectrum`, no `resistance_mechanisms`, and no
`causal_graphs`. That is structurally valid for a ChEBI seed, but it means the
exact `(Z)` furylfuramide structure has only upstream database provenance and
no primary-paper support for a compound-specific antimicrobial mechanism.

The local raw ChEBI row for `CHEBI:15660` has no PMID leads. Bounded publication
checks did not identify an immediately supportable antimicrobial-mechanism
claim for this exact record:

- The first exact PubMed query
  `LYAHJFZLDZDIOH-VURMDHGXSA-N OR "CHEBI:15660" OR "(Z)-2-(2-furyl)-3-(5-nitro-2-furyl)acrylamide" OR "Furylfuramide" OR "AF-2"`
  demonstrated that unqualified `AF-2` is too ambiguous: PubMed broadened that
  token to atrial-fibrillation and activation-function-2 literature.
- A constrained exact PubMed query over `Furylfuramide`, the exact ChEBI label,
  `CHEBI:15660`, and `LYAHJFZLDZDIOH-VURMDHGXSA-N` returned AF-2 /
  furylfuramide hits, but the visible titles and abstracts were genotoxicity,
  mutagenicity, carcinogenicity, detoxification, or assay-control uses.
- A broader PubMed query over
  `furylfuramide[Title/Abstract] AND (antimicrobial[Title/Abstract] OR antibacterial[Title/Abstract] OR mechanism[Title/Abstract] OR nitrofuran[Title/Abstract] OR reductase[Title/Abstract])`
  returned 17 historical furylfuramide or nitrofuran leads. The inspected
  titles and abstracts covered SOS repair, mutagenesis, cis-trans
  isomerization, hepatic necrosis, carcinogen detection, and toxicity, not a
  reusable antimicrobial target or mode of action for `CHEBI:15660`.
- Semantic Scholar was also attempted with exact furylfuramide labels, but the
  public API returned HTTP 429 and no result file was emitted.

Google Scholar was not used.

## Completeness

The generated source concept, exact ChEBI grounding, structural-class
parentage, structure fields, generic filing class, xrefs, and seed history are
sufficient for a ChEBI-only seed.

Consequential gaps:

- `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, and
  `causal_graphs` are absent. This record should remain below `REVIEWED` until
  a curator either finds evidence for a furylfuramide antimicrobial mechanism or
  adds a curator-owned veto explaining that the mechanism remains unknown.
- `activity_spectrum` is absent. Future activity curation should use measured
  organism, strain or isolate, assay, value, qualifier, units, compound form,
  and evidence rather than generalizing from the nitrofuran class.

Empty optional slots that are acceptable in this generated seed:

- `resistance_mechanisms`: no CARD target or resistance edge was available for
  this exact ChEBI record.
- `producer_organisms`: no producer-candidate worklist row was present.
- `clinical_status_assertions`: no regulatory source was imported for this
  exact ChEBI record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The exact `CHEBI:15660` furylfuramide record has no reviewed antimicrobial mechanism. | `just worklist --limit 0 --tsv /tmp/z-furyl-nitrofuryl-acrylamide-worklist.tsv` lists `CHEBI:15660` in `mechanism` with `0 CARD target(s), 0 resistance edge(s) to build on` and in `review-readiness` with `MECHANISM_REVIEW: mechanism is absent; 0 source literature lead(s), 0 record evidence item(s), 0 target(s)`; the local ChEBI row has no PMIDs; bounded PubMed checks surfaced toxicity or mutagenicity leads but no exact antimicrobial-mechanism support. | Add an evidence-backed curator-owned mechanism to `data/antibiotics/unspecified/z-2-2-furyl-3-5-nitro-2-furyl-acrylamide.yaml` through `write_validated_antibiotic`, or add a curator-owned veto explaining why the mechanism remains unknown for furylfuramide. |

No blockers found. No minor findings found.

## Recommended Edits

1. Inspect primary furylfuramide and nitrofuran sources for antimicrobial
   mechanism evidence that applies to exact `CHEBI:15660`, not merely to a
   related nitrofuran.
2. Add a `CURATOR:`-owned mechanism, target scope, molecular target, and causal
   graph only if exact primary support is found; otherwise leave a
   curator-owned veto documenting the bounded negative search.
3. Add measured `activity_spectrum` rows only when the source provides complete
   organism, strain or isolate, assay, value, units, compound form, and
   evidence for furylfuramide.

## Follow-up Checks

- After any mechanism or activity curation, run
  `just validate-strict data/antibiotics/unspecified/z-2-2-furyl-3-5-nitro-2-furyl-acrylamide.yaml --out /tmp/antibioticmech-record-validation.tsv`,
  `just verify-corpus --summary`,
  `just worklist --limit 0 --tsv /tmp/z-furyl-nitrofuryl-acrylamide-worklist.tsv`,
  and `just lint`.
- Re-run OLS4 checks for `CHEBI:15660`, `CHEBI:140324`, `CHEBI:22216`,
  `CHEBI:35716`, and `CHEBI:87230` if future edits touch identity, xrefs, or
  parentage.
- Re-run PubMed and Semantic Scholar if future mechanism curation depends on a
  negative literature claim; the Semantic Scholar API was rate-limited during
  this review.

## Additional Notes

- The ignored-file-inclusive resolution search covered `data/antibiotics`,
  `data/raw`, `curation`, and `reports/yaml_record_review`; a separate
  ignored-file-inclusive `find` found no prior exact report for
  `z-2-2-furyl-3-5-nitro-2-furyl-acrylamide`.
- The repository exposes only full-corpus worklist categories for mechanism,
  cross-reference, producer, target-evidence, and review-readiness checks.
  `CHEBI:15660` was absent from all inspected queues except `mechanism` and
  `review-readiness`.
