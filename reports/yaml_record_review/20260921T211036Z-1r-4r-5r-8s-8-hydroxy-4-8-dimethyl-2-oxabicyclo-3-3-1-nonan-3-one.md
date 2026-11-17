# YAML Record Review: (1R,4R,5R,8S)-8-hydroxy-4,8-dimethyl-2-oxabicyclo[3.3.1]nonan-3-one

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antifungal/1r-4r-5r-8s-8-hydroxy-4-8-dimethyl-2-oxabicyclo-3-3-1-nonan-3-one.yaml`
- Started UTC: 2026-09-21T21:05:00Z
- Finished UTC: 2026-09-21T21:10:36Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:141296` |
| Label | `(1R,4R,5R,8S)-8-hydroxy-4,8-dimethyl-2-oxabicyclo[3.3.1]nonan-3-one` |
| Path | `data/antibiotics/antifungal/1r-4r-5r-8s-8-hydroxy-4-8-dimethyl-2-oxabicyclo-3-3-1-nonan-3-one.yaml` |
| Class | `ANTIFUNGAL` |
| Grounding | `EXACT` |
| Status | `SEEDED` |
| Source concept | `CHEBI:141296`, source version `2026-08-30`, minted source identifier `antibioticmech:chebi-38b695a22e` |
| Structure key | `NIVFCUNTHUULDF-DQUBFYRCSA-N` |

An ignored-inclusive search over `data/antibiotics`, `data/raw`, `curation`,
and `reports` for `CHEBI:141296`, the label fragments `8-hydroxy-4,8-dimethyl-2-oxabicyclo`
and `nonan-3-one`, and the numeric fragment `141296` found the target
`PATHS.tsv`, `chebi_antimicrobials.tsv`, and `record_review_queue.tsv` rows.
It found no prior `reports/yaml_record_review/*oxabicyclo*` report; the only
spurious numeric hit was an unrelated `PMID:141296`-like substring in the
fusidic-acid ChEBI literature list.

## Validation

| Command | Result |
|---|---|
| `just validate data/antibiotics/antifungal/1r-4r-5r-8s-8-hydroxy-4-8-dimethyl-2-oxabicyclo-3-3-1-nonan-3-one.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/1r-4r-5r-8s-8-hydroxy-4-8-dimethyl-2-oxabicyclo-3-3-1-nonan-3-one.yaml --out /tmp/antibioticmech-oxabicyclo-141296-validation.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total error rows. |
| `just verify-corpus --summary` | Passed; 2,939 records expected and on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, and 0 stale lockfile rows. |
| `just review-queue --limit 35` | Listed `CHEBI:141296` at row 33 with `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-oxabicyclo-141296.tsv` | Passed and wrote the full TSV; `CHEBI:141296` appears in `mechanism`, `producer-candidate`, and `review-readiness`. |

No narrower single-record term, reference, or history validator is exposed for
this ChEBI-seeded record category. The full-corpus worklist also repeated the
known unrelated CARD conflict for `ARO:3000337` / iclaprim versus isoaminile
citrate; that conflict does not name `CHEBI:141296`.

## Identity and Grounding

The ChEBI grounding is coherent. The YAML identifier, label, definition,
activity role, four parent terms, SMILES, Standard InChI, formula, neutral
charge, average mass, monoisotopic mass, and InChIKey all reproduce from the
committed `data/raw/chebi_antimicrobials.tsv` row for `CHEBI:141296`.

The current official ChEBI page still denotes the same exact structure:

| Claim | Status |
|---|---|
| Structure | Coherent; ChEBI reports formula `C10H16O3`, charge `0`, average mass `184.235`, monoisotopic mass `184.10994`, the YAML SMILES, the YAML Standard InChI, and InChIKey `NIVFCUNTHUULDF-DQUBFYRCSA-N`. |
| Activity role | Coherent; ChEBI asserts a `has role` relation to `CHEBI:35718` / antifungal agent, which is the sole antimicrobial role imported into `activity_roles`. |
| Parent terms | Coherent; current ChEBI asserts `is a` relations to `CHEBI:18946`, `CHEBI:25409`, `CHEBI:26878`, and `CHEBI:27171`, matching the generated `parent_compounds` list. |
| Source organism lead | Present upstream but not imported. Current ChEBI lists `Neopestalotiopsis foedans` / `NCBITaxon:290095` as a species of metabolite with `PMID:27448166`; NCBI Taxonomy records `Pestalotiopsis foedans` as an older name for the same taxon. |

The record carries no `xrefs`, `drug_xrefs`, or `document_xrefs`, and the full
worklist has no `CHEBI:141296` rows in the xref, minted, multi-component,
structure-unreviewed, target-evidence, moa-scope, or unknown-mechanism queues.

## Evidence

The only committed ChEBI literature lead is `PMID:27448166` / DOI
`10.1002/cbdv.201600114`, "Antifungal Monoterpene Derivatives from the Plant
Endophytic Fungus Pestalotiopsis foedan." PubMed confirms that Xu, Zhang, and
Yang reported compound 1 as the target monoterpene lactone from liquid culture
of the plant endophytic fungus named in the paper as `Pestalotiopsis foedan`.
The abstract also reports that the authors determined the structure and
absolute configuration of compound 1 by NMR plus optical-rotation and
13C-NMR calculations.

That PMID is a direct activity lead for this exact compound, but not a
complete activity observation by itself. The abstract says both compound 1 and
the related compound 2 had strong antifungal activities against
`Botrytis cinerea` and `Phytophthora nicotianae` with MIC values of 3.1 and
6.3 ug/ml, respectively. The target record has no `activity_spectrum`; a
curator should inspect the full text or assay table before assigning each MIC
to an organism and recording the MIC method.

The same paper supports a structured producer follow-up. The abstract states
that the compound was isolated from a liquid culture of the endophytic fungus,
and current ChEBI resolves the source organism to `NCBITaxon:290095`
`Neopestalotiopsis foedans`. The record has no `producer_organisms` entry, so
the source taxon, the historical source name `Pestalotiopsis foedan`, and the
host branch context from `Bruguiera sexangula` are still outside the structured
record.

The successful repository publication search used PubMed with `NCBI_EMAIL`
unset and wrote `/tmp/antibioticmech-oxabicyclo-141296-publications.jsonl`.
It found `PMID:27448166` as the exact target paper and two older
`Pestalotiopsis foedan` papers for different secondary metabolites. Semantic
Scholar returned HTTP 429 for the same query, so that provider was not
available during this pass.

## Completeness

- `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, and
  `causal_graphs` are absent; no inspected source identified an antifungal
  molecular target or pathway for this exact monoterpene lactone.
- `activity_spectrum` is absent despite the exact ChEBI/PubMed activity lead.
  The abstract supplies target organisms and MIC values, but not enough assay
  detail to safely populate the schema without full-text inspection.
- `producer_organisms` is absent. ChEBI and PubMed together identify a fungal
  source organism, now `Neopestalotiopsis foedans` / `NCBITaxon:290095`, but no
  strain-scoped producer claim has been curated.
- `resistance_mechanisms`, `clinical_status_assertions`, `datasets`, and
  `discussions` are absent. No inspected local or PubMed lead required these
  optional sections before the mechanism, activity, and producer gaps are
  resolved.

A gitignore-independent search over the target record, `data/antibiotics`,
`data/raw`, `curation`, and `reports` for `CHEBI:141296`,
`antibioticmech:chebi-38b695a22e`, `NIVFCUNTHUULDF`, and `PMID:27448166` found
the generated record, the ChEBI antimicrobial inventory row, the `PATHS.tsv`
row, the review-readiness row, the same-source sibling `CHEBI:141292`, and the
worklist `mechanism`, `producer-candidate`, and `review-readiness` rows. It
found no existing curator decision, generated mechanism, activity observation,
producer assertion, or prior review that resolves this target.

## Findings

| Severity | ID | Finding |
|---|---|---|
| Major | OXABICYCLO-141296-M1 | The record is still a ChEBI-only exact antifungal stub with no curated mode of action, target, activity observation, producer assertion, or causal graph despite a primary-paper lead that supports exact structure, fungal-culture origin, and antifungal MIC follow-up. |

### OXABICYCLO-141296-M1

The source-owned identity, ChEBI structure, antifungal filing class, and
activity role are internally coherent, but all antimicrobial evidence remains
implicit in ChEBI provenance. `just review-queue --limit 35` reports
`MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record
evidence item(s), 0 target(s)`, and the full worklist places `CHEBI:141296` in
both `mechanism` and `producer-candidate`. `PMID:27448166` is exact for the
compound and is enough to drive manual curation of activity and producer
claims, but this review found no claim-level evidence in the YAML and no
primary-paper mechanism or target assertion.

Owner: curator-owned additions on
`data/antibiotics/antifungal/1r-4r-5r-8s-8-hydroxy-4-8-dimethyl-2-oxabicyclo-3-3-1-nonan-3-one.yaml`
via a guarded mutator, `record_curation_event`, and
`write_validated_antibiotic`.

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect the full `PMID:27448166` article or supplement and, if the organism,
   MIC, qualifier, assay method, and units unambiguously belong to compound 1,
   add `activity_spectrum` observations for the reported `Botrytis cinerea` and
   `Phytophthora nicotianae` antifungal assays.
2. Curate a `producer_organisms` entry for the liquid-culture source fungus if
   the paper supports biosynthesis by that fungus; use the current
   `NCBITaxon:290095` name `Neopestalotiopsis foedans` and preserve the
   historical `Pestalotiopsis foedan` name and `Bruguiera sexangula` branch
   context in notes if no strain identifier is available.
3. Run a targeted mechanism search for the exact label, InChIKey, DOI, PMID,
   and organism names. Add `mode_of_action`, `mode_of_action_target_scope`,
   `molecular_targets`, or a causal graph only if the inspected literature
   supports a compound-specific mechanistic claim.
4. Keep `curation_status: SEEDED` until at least the mode of action and any
   known molecular target have claim-level citations.

## Follow-up Checks

- Re-run `just validate data/antibiotics/antifungal/1r-4r-5r-8s-8-hydroxy-4-8-dimethyl-2-oxabicyclo-3-3-1-nonan-3-one.yaml`.
- Re-run `just validate-strict data/antibiotics/antifungal/1r-4r-5r-8s-8-hydroxy-4-8-dimethyl-2-oxabicyclo-3-3-1-nonan-3-one.yaml --out /tmp/antibioticmech-oxabicyclo-141296-validation.tsv`.
- Re-run `just verify-corpus --summary` to prove any record change was made through a maintained, generated path.
- Re-run `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-oxabicyclo-141296.tsv` and confirm `CHEBI:141296` leaves `producer-candidate` only after the source organism has been accepted or explicitly rejected.
- Re-run `just review-queue --limit 35` or a full review-readiness checkpoint to confirm the row changes only after the record has a real mechanism disposition.
- Re-run `just qc` before merging any future curation change.

## Additional Notes

- Searches used to establish absence included ignored files through
  `rg --no-ignore --hidden`. `reports/` is gitignored, so this new review
  report must be staged with `git add -f`.
- The same `PMID:27448166` also supports the sibling ChEBI record
  `CHEBI:141292`; activity or producer curation for this record should not
  silently assert that every source-paper claim applies to the sibling
  compound.
- This report is read-only review output. No generated record, upstream
  inventory, decision row, page, queue, or curation-history entry was edited.
