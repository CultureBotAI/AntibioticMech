# YAML Record Review: (1R,4S)-1-hydroperoxy-p-menth-2-en-8-ol acetate

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antiprotozoal/1r-4s-1-hydroperoxy-p-menth-2-en-8-ol-acetate.yaml`
- Started UTC: 2026-09-21T21:38:00Z
- Finished UTC: 2026-09-21T21:41:16Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:66035` |
| Label | `(1R,4S)-1-hydroperoxy-p-menth-2-en-8-ol acetate` |
| Path | `data/antibiotics/antiprotozoal/1r-4s-1-hydroperoxy-p-menth-2-en-8-ol-acetate.yaml` |
| Class | `ANTIPROTOZOAL` |
| Grounding | `EXACT` |
| Status | `SEEDED` |
| Source concept | `CHEBI:66035`, source version `2026-08-30`, minted source identifier `antibioticmech:chebi-119523e84a` |
| Structure key | `VIUQTXYGNHOJBD-PWSUYJOCSA-N` |

An ignored-inclusive search over `data/antibiotics`, `data/raw`, `curation`,
and `reports` for `CHEBI:66035`, `1-hydroperoxy-p-menth-2-en-8-ol acetate`,
and `66035` found only the target `PATHS.tsv`, ChEBI raw, review-queue, and
generated YAML rows. It found no prior `reports/yaml_record_review/*66035*` or
`*hydroperoxy-p-menth*` report.

## Validation

| Command | Result |
|---|---|
| `just validate data/antibiotics/antiprotozoal/1r-4s-1-hydroperoxy-p-menth-2-en-8-ol-acetate.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antiprotozoal/1r-4s-1-hydroperoxy-p-menth-2-en-8-ol-acetate.yaml --out /tmp/antibioticmech-hydroperoxy-menth-acetate-66035-validation.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Passed; 2,939 records expected and on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, and 0 stale lockfile rows. |
| `just review-queue --limit 36` | Listed `CHEBI:66035` at row 34 with `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-hydroperoxy-menth-acetate-66035.tsv` | Passed and wrote the full TSV; `CHEBI:66035` appears in `mechanism`, `producer-candidate`, and `review-readiness`. |

No narrower single-record term, reference, or history validator is exposed for
this ChEBI-seeded record category. The full-corpus worklist also repeated the
known unrelated CARD conflict for `ARO:3000337` / iclaprim versus isoaminile
citrate; that conflict does not name `CHEBI:66035`.

## Identity and Grounding

The ChEBI grounding is coherent. The YAML identifier, label, synonym,
definition, activity role, three parent terms, `reaxys:9260434` xref, SMILES,
Standard InChI, formula, neutral charge, average mass, monoisotopic mass, and
InChIKey all reproduce from the committed `data/raw/chebi_antimicrobials.tsv`
row for `CHEBI:66035`.

The current official ChEBI page still denotes the same exact structure:

| Claim | Status |
|---|---|
| Structure | Coherent; ChEBI reports formula `C12H20O4`, charge `0`, average mass `228.288`, monoisotopic mass `228.13616`, the YAML SMILES, the YAML Standard InChI, and InChIKey `VIUQTXYGNHOJBD-PWSUYJOCSA-N`. |
| Activity role | Coherent; ChEBI asserts a `has role` relation to `CHEBI:36335` / trypanocidal drug, which is the sole antimicrobial role imported into `activity_roles` and correctly files the record as `ANTIPROTOZOAL`. |
| Parent terms | Coherent; current ChEBI asserts `is a` relations to `CHEBI:25186`, `CHEBI:35924`, and `CHEBI:47622`, matching the generated `parent_compounds` list. |
| Reaxys xref | Coherent as imported provenance; current ChEBI lists `Reaxys:9260434`, matching the record's only exact xref. |
| Source organism lead | Present upstream but not imported. Current ChEBI lists `Laurus nobilis` / `NCBITaxon:85223` and component `leaf` / `BTO:0000713` as the species of metabolite and source part for `PMID:12419922`; NCBI Taxonomy confirms `85223` is `Laurus nobilis`. |

The full worklist has no `CHEBI:66035` rows in the xref, minted,
multi-component, structure-unreviewed, target-evidence, moa-scope, or
unknown-mechanism queues.

## Evidence

The only committed ChEBI literature lead is `PMID:12419922` / DOI
`10.1248/cpb.50.1514`, "Trypanocidal terpenoids from Laurus nobilis L."
PubMed confirms that Uchiyama and coauthors reported the target compound as
compound 3, a new p-menthane hydroperoxide isolated during activity-guided
fractionation of a methanol extract from dried `Laurus nobilis` leaves.

The paper is a direct activity lead for this exact compound. The abstract maps
compound 3 to this record and reports minimum lethal concentrations for
dehydrocostus lactone, zaluzanin D, and this target against epimastigotes of
`Trypanosoma cruzi`; by the compound order, `CHEBI:66035` has the 1.4 uM value.
The YAML has no `activity_spectrum`, so the source organism, assay type,
qualifier, lifecycle stage, and minimum-lethal-concentration measurement are
still not structured.

The paper also supports a bounded producer follow-up. ChEBI resolves the dried
leaf source to `NCBITaxon:85223` `Laurus nobilis` plus `BTO:0000713` leaf, and
the worklist already flags the source phrase as `producer-candidate`. This is a
plant source rather than a strain-scoped microbial culture, so a future
producer assertion should preserve that it is a leaf metabolite from a plant
extract.

The successful repository publication search used PubMed with `NCBI_EMAIL`
unset and wrote
`/tmp/antibioticmech-hydroperoxy-menth-acetate-66035-publications.jsonl`. It
found `PMID:12419922` as the exact target paper. Semantic Scholar returned HTTP
429 for the same query, so that provider was not available during this pass.

## Completeness

- `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, and
  `causal_graphs` are absent; no inspected source identified a trypanocidal
  molecular target or pathway for this exact p-menthane hydroperoxide.
- `activity_spectrum` is absent despite the exact ChEBI/PubMed activity lead.
  The abstract supplies `Trypanosoma cruzi` epimastigotes and a minimum lethal
  concentration, but not the full assay context a structured observation should
  carry.
- `producer_organisms` is absent. Current ChEBI identifies
  `Laurus nobilis` leaves as the source, but that plant-metabolite claim has not
  been curated into this record.
- `resistance_mechanisms`, `clinical_status_assertions`, `datasets`, and
  `discussions` are absent. No inspected local or PubMed lead required these
  optional sections before the mechanism, activity, and producer gaps are
  resolved.

A gitignore-independent search over the target record, `data/antibiotics`,
`data/raw`, `curation`, and `reports` for `CHEBI:66035`,
`antibioticmech:chebi-119523e84a`, `VIUQTXYGNHOJBD`, and `PMID:12419922` found
the generated record, the ChEBI antimicrobial inventory row, the `PATHS.tsv`
row, the review-readiness row, the same-source sibling records for
`dehydrocostus lactone` and `zaluzanin D`, and the worklist `mechanism`,
`producer-candidate`, and `review-readiness` rows. It found no existing curator
decision, generated mechanism, activity observation, producer assertion, or
prior review that resolves this target.

## Findings

| Severity | ID | Finding |
|---|---|---|
| Major | HYDROPEROXY-MENTH-66035-M1 | The record is still a ChEBI-only exact antiprotozoal stub with no curated mode of action, target, activity observation, producer assertion, or causal graph despite a primary-paper lead that supports exact structure, plant-leaf origin, and `Trypanosoma cruzi` minimum-lethal-concentration follow-up. |

### HYDROPEROXY-MENTH-66035-M1

The source-owned identity, ChEBI structure, Reaxys xref, antiprotozoal filing
class, and trypanocidal role are internally coherent, but all antimicrobial
evidence remains implicit in ChEBI provenance. `just review-queue --limit 36`
reports `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0
record evidence item(s), 0 target(s)`, and the full worklist places
`CHEBI:66035` in both `mechanism` and `producer-candidate`. `PMID:12419922` is
exact for the compound and is enough to drive manual curation of antiprotozoal
activity and plant-source producer claims, but this review found no claim-level
evidence in the YAML and no primary-paper mechanism or target assertion.

Owner: curator-owned additions on
`data/antibiotics/antiprotozoal/1r-4s-1-hydroperoxy-p-menth-2-en-8-ol-acetate.yaml`
via a guarded mutator, `record_curation_event`, and
`write_validated_antibiotic`.

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the full `PMID:12419922` article and, if its assay methods support
   the abstract-level mapping, add an `activity_spectrum` observation for the
   1.4 uM minimum lethal concentration against `Trypanosoma cruzi`
   epimastigotes.
2. Curate a producer/source assertion for `NCBITaxon:85223` `Laurus nobilis`
   leaves if the full paper supports that dried leaves were the biosynthetic
   source of compound 3; preserve the source component `leaf` / `BTO:0000713`
   in evidence notes if the schema has no narrower component slot.
3. Run a targeted mechanism search for the exact label, InChIKey, DOI, PMID,
   `Laurus nobilis`, and `Trypanosoma cruzi`. Add `mode_of_action`,
   `mode_of_action_target_scope`, `molecular_targets`, or a causal graph only
   if the inspected literature supports a compound-specific mechanistic claim.
4. Keep `curation_status: SEEDED` until at least the mode of action and any
   known molecular target have claim-level citations.

## Follow-up Checks

- Re-run `just validate data/antibiotics/antiprotozoal/1r-4s-1-hydroperoxy-p-menth-2-en-8-ol-acetate.yaml`.
- Re-run `just validate-strict data/antibiotics/antiprotozoal/1r-4s-1-hydroperoxy-p-menth-2-en-8-ol-acetate.yaml --out /tmp/antibioticmech-hydroperoxy-menth-acetate-66035-validation.tsv`.
- Re-run `just verify-corpus --summary` to prove any record change was made through a maintained, generated path.
- Re-run `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-hydroperoxy-menth-acetate-66035.tsv` and confirm `CHEBI:66035` leaves `producer-candidate` only after the plant source has been accepted or explicitly rejected.
- Re-run `just review-queue --limit 36` or a full review-readiness checkpoint to confirm the row changes only after the record has a real mechanism disposition.
- Re-run `just qc` before merging any future curation change.

## Additional Notes

- Searches used to establish absence included ignored files through
  `rg --no-ignore --hidden`. `reports/` is gitignored, so this new review
  report must be staged with `git add -f`.
- `PMID:12419922` also supports dehydrocostus lactone and zaluzanin D rows.
  Curation for this record should use the compound numbering in the source
  paper rather than copying every trypanocidal claim across all three ChEBI
  records.
- This report is read-only review output. No generated record, upstream
  inventory, decision row, page, queue, or curation-history entry was edited.
