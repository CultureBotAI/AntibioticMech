# YAML Record Review: (1R,2S)-epoxypropylphosphonate(1−)

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/unspecified/1r-2s-epoxypropylphosphonate-1.yaml`
- Started UTC: 2026-09-21T20:34:00Z
- Finished UTC: 2026-09-21T20:38:11Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:62247` |
| Label | `(1R,2S)-epoxypropylphosphonate(1-)` |
| Path | `data/antibiotics/unspecified/1r-2s-epoxypropylphosphonate-1.yaml` |
| Class | `ANTIMICROBIAL_UNSPECIFIED` |
| Grounding | `EXACT` |
| Status | `SEEDED` |
| Source concept | `CHEBI:62247`, source version `2026-08-30`, minted source identifier `antibioticmech:chebi-ca956e579e` |
| Structure key | `YMDXZJFXQJVXBF-STHAYSLISA-M` |

This review resolved the ChEBI-grounded monoanion record, not the reviewed neutral fosfomycin record at `data/antibiotics/antibacterial/fosfomycin.yaml`.

An ignored-inclusive search over `data/antibiotics`, `data/raw`, `curation`, and `reports` for `CHEBI:62247`, `epoxypropylphosphonate`, and `62247` found the target `data/antibiotics/PATHS.tsv` row, the ChEBI raw row, the review-queue row, and FDA `ApplNo=062247` chloramphenicol rows caused by the numeric fragment. It found no prior `reports/yaml_record_review/*epoxypropylphosphonate*` report.

## Validation

| Command | Result |
|---|---|
| `just validate data/antibiotics/unspecified/1r-2s-epoxypropylphosphonate-1.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/unspecified/1r-2s-epoxypropylphosphonate-1.yaml --out /tmp/antibioticmech-epoxypropylphosphonate-62247-validation.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Passed; 2,939 records expected and on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, and 0 stale lockfile rows. |
| `just review-queue --limit 33` | Listed `CHEBI:62247` at row 32 with `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-epoxypropylphosphonate-62247.tsv` | Passed and wrote the full TSV; `CHEBI:62247` appears in `mechanism`, `xref-span-conflict`, and `review-readiness`. |

No narrower single-record term, reference, or history validator is exposed for this ChEBI-seeded record category. The full-corpus worklist also repeated the known unrelated CARD conflict for `ARO:3000337` / iclaprim versus isoaminile citrate; that conflict does not name `CHEBI:62247`.

## Identity and Grounding

The target identity is exact and source-owned:

| Claim | Status |
|---|---|
| ChEBI identity | Coherent. The YAML identifier, label, definition, source concept, charge `-1`, formula `C3H6O4P`, Standard InChI, and InChIKey `YMDXZJFXQJVXBF-STHAYSLISA-M` match the current `CHEBI:62247` page. |
| Neutral sibling | Separate and already curated. `CHEBI:28915` / `fosfomycin` has formula `C3H7O4P`, InChIKey `YMDXZJFXQJVXBF-STHAYSLISA-N`, charge `0`, CARD source concept `ARO:0000025`, antibacterial filing, MurA target evidence, and mode `CELL_WALL_SYNTHESIS_INHIBITION`. |
| ChEBI relation | Coherent. Current ChEBI records `CHEBI:28915` as conjugate acid of `CHEBI:62247`; the two records are intentionally different charge states. |
| Activity role and filing class | Coherent with the raw ChEBI row. `CHEBI:62247` imports only broad `CHEBI:33281` antimicrobial-agent activity, so `ANTIMICROBIAL_UNSPECIFIED` is the expected filing class. |
| MetaCyc xref | Conflicted. The same `metacyc.compound:CPD0-1113` accession is present on both `CHEBI:62247` and neutral `CHEBI:28915`; `just worklist` flags both records as `xref-span-conflict`. |

Current MetaCyc `CPD0-1113` renders with the label `fosfomycin` and formula `C3H6O4P`, but it also reports monoisotopic mass `138.0081952231`, matching neutral `CHEBI:28915` rather than `CHEBI:62247`'s `137.00092`. The accession is therefore ambiguous across charge forms and should not be asserted as exact identity without a curator decision.

## Evidence

The YAML target has no `evidence`, `activity_spectrum`, `molecular_targets`, `resistance_mechanisms`, `producer_organisms`, `clinical_status_assertions`, or `causal_graphs`.

The one committed ChEBI literature lead for `CHEBI:62247`, `PMID:18656958` / `DOI:10.1021/bi800877v`, supports fosfomycin biosynthesis in a `Pseudomonas syringae` enzyme system: the PubMed abstract reports that purified Ps-HppE catalyzed epoxidation of `(S)-2-hydroxypropylphosphonic acid` to fosfomycin. It is producer/biosynthetic context, not a primary antimicrobial assay or MurA mechanism paper for the monoanion record.

The adjacent reviewed neutral fosfomycin record has the bacterial MurA cocrystal evidence and CARD resistance edges expected for `ARO:0000025`, but those claims are absent from the monoanion record. That absence is not automatically false; a curator needs to decide whether the monoanion should inherit an evidence-backed fosfomycin mechanism, stay empty as a charge-state sibling, or be deprecated/excluded.

An exact PubMed search without `NCBI_EMAIL` for `epoxypropylphosphonate`, `fosfomycin(1-)`, and `CPD0-1113` wrote `/tmp/antibioticmech-epoxypropylphosphonate-62247-exact.jsonl`. Its top hits were broad 2025-2026 fosfomycin clinical and resistance papers, not exact evidence that distinguishes `CHEBI:62247` from neutral `CHEBI:28915`.

## Completeness

- `metacyc.compound:CPD0-1113` remains in `xrefs` even though the worklist flags it as a span conflict against neutral fosfomycin.
- `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, and `causal_graphs` are absent.
- `activity_spectrum` is absent; no inspected source in this pass provided an exact monoanion MIC, qualifier, unit, assay, or strain.
- `resistance_mechanisms` is absent. CARD resistance mechanisms are already attached to neutral fosfomycin through `ARO:0000025`; the monoanion is a ChEBI-only seed with no CARD source concept.
- `producer_organisms` is absent. Two fosfomycin MIBiG rows in `data/raw/mibig_producers.tsv` join by exact Standard InChIKey to neutral `CHEBI:28915`, not to the charged monoanion.

A gitignore-independent search over `data/raw`, `curation`, `data/antibiotics`, and `reports` for `CHEBI:62247`, `YMDXZJFXQJVXBF`, `CPD0-1113`, `PMID:18656958`, `fosfomycin`, and `epoxypropylphosphonate` found the target rows, the neutral reviewed fosfomycin record and its ARO/CARD/MIBiG evidence, and no curator decision or previous review that resolves the `CHEBI:62247` xref or mechanism gaps.

## Findings

| Severity | ID | Finding |
|---|---|---|
| Blocker | EPOXYPROPYLPHOSPHONATE-62247-B1 | `metacyc.compound:CPD0-1113` is asserted as an exact xref for both the charged monoanion `CHEBI:62247` and neutral fosfomycin `CHEBI:28915`; the same external accession therefore spans two different Standard InChIKeys. |
| Major | EPOXYPROPYLPHOSPHONATE-62247-M1 | The monoanion record is a ChEBI-only seeded sibling of reviewed fosfomycin, but it lacks a mechanism disposition, target, activity observation, and evidence-backed decision about whether fosfomycin mechanism evidence should apply to this exact charge state. |

### EPOXYPROPYLPHOSPHONATE-62247-B1

`metacyc.compound:CPD0-1113` is in `xrefs` on this record and in the source ChEBI row, while the same MetaCyc accession is also attached to `CHEBI:28915` / neutral fosfomycin in `data/raw/chebi_antimicrobials.tsv`. The two ChEBI structures differ by one proton and have distinct Standard InChIKeys ending `-M` and `-N`; `just worklist` accordingly emits reciprocal `xref-span-conflict` rows for `CHEBI:62247` and `CHEBI:28915`. The exact-identity xref should be removed, moved, or explicitly allowed through a maintained curation decision rather than published on both charge states.

Owner: ChEBI inventory extraction, the seeder xref filter, or `curation/decisions.tsv`; do not hand-edit only `data/antibiotics/unspecified/1r-2s-epoxypropylphosphonate-1.yaml`, because `just verify-corpus` proves it is generated from raw ChEBI.

### EPOXYPROPYLPHOSPHONATE-62247-M1

The neutral fosfomycin record already carries the curated evidence-backed claim that fosfomycin inhibits bacterial UDP-N-acetylglucosamine enolpyruvyl transferase MurA and has CARD resistance edges. The monoanion `CHEBI:62247` is a distinct, broad-antimicrobial ChEBI seed with no CARD source concept and no mechanism fields. The one ChEBI PubMed lead supports biosynthesis to fosfomycin in `Pseudomonas syringae` HppE assays, but not exact activity or MurA binding for the monoanion. A curator needs to decide whether this charge state should be reviewed as a separate bioactive form, bridged to the neutral fosfomycin mechanism, or suppressed as a duplicate charge form.

Owner: curator-owned additions on the exact YAML record via `write_validated_antibiotic`, plus `curation/decisions.tsv` if the final decision is exclusion, duplicate suppression, or an xref exception.

No minor findings.

## Recommended Edits

1. Resolve `metacyc.compound:CPD0-1113` as an exact xref: suppress it from `CHEBI:62247`, suppress it from both charge forms, or document a narrow exception that the same MetaCyc accession intentionally covers fosfomycin protonation states.
2. Decide how `CHEBI:62247` should relate to the reviewed neutral fosfomycin record: duplicate charge form to suppress, exact major species to curate separately, or child record that should carry an explicit charge-state note before inheriting any MurA mechanism.
3. If the monoanion stays in scope, add claim-level target and mechanism evidence for this exact form or an explicit discussion explaining why neutral fosfomycin evidence is being reused across the conjugate-acid/base pair.
4. Keep `curation_status: SEEDED` until the exact xref conflict and monoanion mechanism disposition are resolved.

## Follow-up Checks

- Re-run `just validate data/antibiotics/unspecified/1r-2s-epoxypropylphosphonate-1.yaml`.
- Re-run `just validate-strict data/antibiotics/unspecified/1r-2s-epoxypropylphosphonate-1.yaml --out /tmp/antibioticmech-epoxypropylphosphonate-62247-validation.tsv`.
- Re-run `just verify-corpus --summary` to prove any xref or curation decision was made through maintained inputs.
- Re-run `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-epoxypropylphosphonate-62247.tsv` and confirm `CHEBI:62247` leaves `xref-span-conflict` only when `CPD0-1113` is no longer ambiguous.
- Re-run `just review-queue --limit 33` or a full review-readiness checkpoint to confirm the row changes only after the record has a real mechanism disposition.

## Additional Notes

- The exact searched local scope included ignored files. `reports/` is gitignored, so this new review report must be staged with `git add -f`.
- The existing neutral fosfomycin record is useful context but is not a curation event on this target.
- The file stem already encodes the ion charge as `-1`; the timestamped report preserved that stem.
