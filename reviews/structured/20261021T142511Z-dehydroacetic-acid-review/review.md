# Dehydroacetic acid: coherent tautomeric identity with one brand-typing correction

- Review: 20261021T142511Z-dehydroacetic-acid-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:02:33Z
- Finished UTC: 2026-10-21T14:25:11Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native neutral keto representation is internally coherent and maps by tautomer normalization to the enol used in independent sources. Antibacterial and antifungal eligibility are supported with assay limits. One minor correction concerns Biocide470F, which the official substance registry types as a brand name rather than an exact chemical synonym.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position350; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:137426 | data/antibiotics/antibacterial/dehydroacetic-acid.yaml | generated | dehydroacetic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:137426 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:137426 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:137426 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:137426 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:137426 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:137426 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:137426 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:137426 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:137426 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:137426 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:137426 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:137426 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral keto serialization and enol relationship

identity: supported. Targets: CHEBI:137426.

Chemical encoding, formula, charge and masses are coherent. An independent enol representation is related by explicit tautomer normalization; the review does not conflate sodium salt or derivatives with the native neutral molecule.

### Chemical aliases versus brand

representation: concern. Targets: CHEBI:137426.

The systematic keto name fits the encoded graph and methylacetopyronone is used in the original patent. GSRS explicitly labels Biocide470F as a brand; the native EXACT_SYNONYM type loses that distinction.

### Chemical parents, CAS and document partition

grounding: supported. Targets: CHEBI:137426.

Both parents are broader chemical categories and the public sources corroborate CAS520-45-6 at the tautomeric-substance level. Both patents and the Wikipedia topic resolve as document links, without implying single-agent clinical efficacy.

### Antibacterial/fungal activity with assay boundaries

evidence: supported. Targets: CHEBI:137426.

Original growth-inhibition evidence supports antimicrobial eligibility. The1954 pH dependence and2025 preparation/method limitations prevent universal organism or quantitative killing claims. ANTIBACTERIAL filing keeps the fungicide role rather than discarding it.

### Structural definition and historical processed-food use

scope: supported. Targets: CHEBI:137426.

The structural definition fits. Original analytical papers and the cucumber-brining patent support historical food-processing use; they do not establish present-day market predominance or current legal permission. That unquantified use emphasis remains a limitation, not a fabricated regulatory conclusion.

### Mechanism, protein targets, resistance, clinical and producer domains

completeness: unknown. Targets: CHEBI:137426.

No corresponding specific native claims exist. Neither derivative docking nor host MR1 activity establishes a bacterial protein target for the exact parent compound. No optional target/causal/clinical field is filled by inference.

### Frozen source and adopted-lead disposition

provenance: supported. Targets: CHEBI:137426.

The source mint and four history events reconcile. All six adopted abstracts were inspected and retained at their actual evidentiary scope. Native SEEDED status is unchanged.

## Findings

### F1: Biocide470F is a brand name, not an exact chemical synonym

minor / open / confirmed; issue key: dehydroacetic-acid-biocide470f-brand-type.

GSRS2KAG279R6R explicitly marks BIOCIDE470F as name type bn. The native alias uses EXACT_SYNONYM. Preserve the searchable alias with BRAND_NAME typing through reproducible source handling, without inferring current product marketing or changing the neutral molecular graph.

## Recommended Actions And Acceptance Checks

### A1

Retain Biocide470F as a brand alias through maintained extraction/seeding.

- Adjudicate the source synonym type as BRAND_NAME using the official registry evidence; make the correction survive source refresh and reseeding.
- Preserve native keto identity, role list and document links; do not replace the graph solely to match an enol registry serialization.
- Run schema/strict, molecular consistency, source reproduction and required QC after an authorized curation change.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/dehydroacetic-acid.yaml; entire YAML, three synonyms, two chemical parents, two activity roles, CAS, three document links and four history events | supports | The native record denotes C8H8O4 neutral dehydroacetic acid in its keto serialization, PGRHXDWITVMQBC-UHFFFAOYSA-N. ANTIBACTERIAL filing preserves the fungicide role. No specific molecular target, strain observation, resistance, producer or clinical claim is populated. |
| owner | data/raw/chebi_antimicrobials.tsv; CHEBI137426 row2579 and six adopted citation leads; extraction/seeding synonym mapping | supports | The frozen source provides the native graph, processed-food-use definition, three aliases, parents, roles, CAS and patent links. SYNONYM maps to EXACT_SYNONYM while BRAND NAME maps to BRAND_NAME. Hidden and ignored files were included in the owner/overlay search. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/137426/; complete current entry, structure and asserted term responses | supports | Current ChEBI matches native keto SMILES/InChI, formula, charge and masses. Pyran2,4-dione and ketone parents resolve and fit the graph. Both antimicrobial roles resolve. Current added bibliography is distinguished from the six frozen adopted leads. |
| chemistry | RDKit 2026.03.5 / InChI 1.07.3; 035-authority-chemistry.py;350-authority-chemistry.json | supports | Native, current ChEBI molfile and PubChem122903 agree on PGRHXDWITVMQBC-UHFFFAOYSA-N. The independent GSRS enol is PKLPQOJFHFGVBS-UHFFFAOYSA-N; RDKit tautomer canonicalization gives that same enol key from both. The keto graph has one unspecified tetrahedral carbon that becomes planar in the enol; no isolated stable-enantiomer identity is claimed or automatically assigned. |
| gsrs | https://api.fda.gov/other/substance.json?search=unii%3A2KAG279R6R&amp;limit=1; GSRS2KAG279R6R version19 full names, enol structure and salt relationship | supports | Official GSRS explicitly types BIOCIDE470F as bn (brand name), while systematic names and dehydroacetic-acid names have different types. It encodes the neutral enol and distinguishes sodium dehydroacetate. It corroborates CAS520-45-6 at substance scope; this is not proprietary CAS registry verification or a native GSRS exact xref. |
| activity1954 | https://doi.org/10.1271/nogeikagaku1924.28.727; complete publisher English abstract; original PDF p728 structure/Methods and p729 culture-condition table | supports | The original distinguishes DHA from dehydroacetocarboxylic acid. DHA inhibits yeast and Acetobacter under tested conditions while Lactobacillus behavior differs; activity varies with medium pH. The actual p728 figure depicts keto/enol representations, and the method uses photoelectric turbidity rather than a direct target-binding assay. The full Japanese text was not independently translated. |
| activity2025 | https://doi.org/10.29356/jmcs.v69i2.2213; Pyrone Biomonitored Synthesis, journal2025 issue / repository Epub2026-02-06; compound1 synthesis/characterization, complete antimicrobial Methods and Table1 | supports | Compound1 is characterized dehydroacetic acid drawn/named in its enol representation. Table1 reports625 micrograms/mL for S.aureus UFPEDA02, P.aeruginosa UFPEDA416 and C.albicans, with higher endpoints for the other tested organisms. Methods specify96-well microdilution, resazurin,37C18–24h bacteria and30C48–72h fungi. The manuscript calls the media agar despite describing microdilution, and supplies a stock McFarland inoculum without a clear final well concentration. These uncertainties must accompany any numerical reuse; the assay does not measure bactericidal/fungicidal killing or protein binding. |
| adopted | PMID:18960990;23790920;25813167;28166217;4030634;6885696; all six adopted bibliographic records and complete indexed abstracts | supports | 18960990 is metal-ion gravimetry;25813167 is vibrational spectroscopy;23790920,4030634 and6885696 describe analytical determination in processed food/wine/squash.28166217 concerns mammalian MR1/MAIT ligand biology and its abstract does not establish a bacterial target for DHA. These are not six independent antimicrobial mechanisms. |
| patentUS | https://patents.google.com/patent/US3849579A/en; original patent description, examples1–8, TableI and claims1–3 | supports | The document specifically names dehydroacetic acid/methylacetopyronone and its possible water-soluble salts in cucumber brining. It claims reduced gas/bloating while retaining yeast growth. Food-processing applicability is supported historically, but suppression of gas production is not fungicidal killing, and the patent does not quantify current predominance of food use. |
| patentAU | https://patents.google.com/patent/AU2004287448A1/en; bibliographic identity, technical field and composition/method claims | supports | The exact A1 application concerns skin-care compositions containing DHA, isomers/salts/derivatives plus skin-care actives and a carrier. It is a related document as natively typed, not an exact single-molecule efficacy or regulatory-approval record. The kindless URL returned404; the explicit A1 publication resolves. |
| document-link | https://en.wikipedia.org/wiki/Dehydroacetic_acid; resolved native topic link and identifier/tautomer context | context_only | The native Wikipedia link is a correctly partitioned topic document, not an exact molecular authority. Scientific conclusions in this review use inspected original papers and official chemical sources rather than this page. |

## Limits And Additional Notes

- The1954 English abstract, actual p728 structural figure/Methods and p729 culture-condition table were inspected; the complete Japanese article was not independently translated or all figures digitized.
- The2025 paper was inspected for compound1 synthesis/characterization, complete antimicrobial Methods and Table1/results. Its agar/microdilution wording, incomplete final-inoculum detail and several chemical-text typographical errors remain source limitations; no exact numerical activity record is imported.
- All six adopted sources were read at complete indexed-abstract depth. The host MR1 paper was not read in full and was not used to assign a microbial target.
- The native food-use emphasis is historically supported but current geographic regulatory status and relative market usage were not surveyed. The review supplies no food-preservation recommendation.
- GSRS uses an enol representation and native uses keto; explicit tautomer normalization relates them without making their raw Standard InChIKeys identical. CAS common-chemistry access returned401, so the proprietary registry was not independently inspected.
- No native gene/locus/pathway claim required a structured-adapter query. Derivative and host-cell findings were not transferred to the parent antibiotic.
- All original captured input hashes were preserved. No native record, source inventory, configuration or generated product was edited.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T142511Z-dehydroacetic-acid-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Dehydroacetic acid: coherent tautomeric identity with one brand-typing correction'
started_at: '2026-10-21T14:02:33Z'
finished_at: '2026-10-21T14:25:11Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. The entire record
    and maintained source were read, independent chemistry calculated, asserted chemical
    groundings checked and exact-compound primary literature assessed with explicit
    access boundaries.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The native neutral keto representation is internally coherent and maps by
  tautomer normalization to the enol used in independent sources. Antibacterial and
  antifungal eligibility are supported with assay limits. One minor correction concerns
  Biocide470F, which the official substance registry types as a brand name rather
  than an exact chemical synonym.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: conf/sources.yaml
    sha256: 4a2dcd7a3a88953b6cb35b51a48ed77b626c3af2cbb542b0d38ba10540ed7df9
    role: context
  - path: curation/curator_antibiotics.tsv
    sha256: 224cbb7261add427184b2762a29c2ff3e85c85e0a06cf22b144545346487247b
    role: context
  - path: curation/decisions.tsv
    sha256: a5834b44307b0449b0df9362c551b7fcd707f3ae51f73d429d37d51f5a169d61
    role: context
  - path: data/antibiotics/antibacterial/dehydroacetic-acid.yaml
    sha256: 4839975b6ddb60b84843f36f8b22711871226460ed27eb1bc650994ba62e7581
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/chebi_antimicrobials.tsv
    sha256: 4c33e56c3c342be657309f720f5b5cb9cad1fae13bec202ef99e449503c32004
    role: context
  - path: data/raw/chebi_role_names.tsv
    sha256: 5c476c0aacd7c98d7241d2343a6fc41ee9eb9338077404c5b011a04bf40c6ac5
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/extract_source_inventory.py
    sha256: bb1606fd07cd8187640b5200a21ec090bb06683397d691e87ddd6884ea768860
    role: context
  - path: scripts/seed_from_sources.py
    sha256: be66eca74d22a3daa9ac6ff73d437c6c56e8d85b97f6877fdf3de77e2ab64680
    role: context
  - path: src/antibioticmech/schema/antibioticmech.yaml
    sha256: de62be2dd2dd55f141a0c14ff666eaa00efc6f3b431d651d0196ebcfddfbb301
    role: context
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
    role: context
targets:
- target_id: CHEBI:137426
  path: data/antibiotics/antibacterial/dehydroacetic-acid.yaml
  label: dehydroacetic acid
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position350; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:137426
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:137426
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    350
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:137426
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/dehydroacetic-acid.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:137426
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/dehydroacetic-acid.yaml --out /private/tmp/am-review-session/350-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:137426
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just qc
  exit_code: 2
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-verify-corpus
  name: Generated corpus reproduction
  status: passed
  required: true
  summary: 2939 expected and present; zero missing, unexpected, drifted fields or
    lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic
    retained.
  target_ids:
  - CHEBI:137426
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just verify-corpus
    --summary
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-review-queue
  name: Native review-readiness inventory
  status: passed
  required: false
  summary: 2859 native unsigned readiness rows written; this status queue does not
    determine structured-review coverage.
  target_ids:
  - CHEBI:137426
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just review-queue
    --limit 0 --tsv /private/tmp/am-review-session/native-queue.tsv
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-tests-platform-partial
  name: Supplementary test suite with two unavailable modules excluded
  status: passed
  required: false
  summary: 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy
    native library were explicitly excluded; this does not replace full QC.
  target_ids:
  - CHEBI:137426
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q -ra --ignore=tests/test_chemical_embedding.py --ignore=tests/test_chemical_map_site.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-validate-all
  name: Full closed-schema validation
  status: passed
  required: true
  summary: 2939 files, zero ERROR rows.
  target_ids:
  - CHEBI:137426
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-all
    --quiet --workers 2 --out /private/tmp/am-review-session/corpus-validation.tsv
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-chemical-map-check
  name: Chemical map consistency
  status: failed
  required: false
  summary: Exited 1 on the same pinned SciPy native library import failure.
  target_ids:
  - CHEBI:137426
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just chemical-map-check
  exit_code: 1
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-render-check
  name: Generated site consistency
  status: passed
  required: false
  summary: 2939 compound pages and seven class pages current.
  target_ids:
  - CHEBI:137426
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just render-check
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-report
  name: Corpus statistics
  status: passed
  required: false
  summary: Corpus report completed successfully.
  target_ids:
  - CHEBI:137426
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just report
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-corpus-integrity
  name: Full-corpus history/evidence/reference invariants
  status: passed
  required: true
  summary: 23 full-corpus integrity tests passed, including seed history, evidence
    placement and internal references.
  target_ids:
  - CHEBI:137426
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/dehydroacetic-acid.yaml
  locator: entire YAML, three synonyms, two chemical parents, two activity roles,
    CAS, three document links and four history events
  accessed_at: '2026-10-21T14:14:56Z'
  support: supports
  summary: The native record denotes C8H8O4 neutral dehydroacetic acid in its keto
    serialization, PGRHXDWITVMQBC-UHFFFAOYSA-N. ANTIBACTERIAL filing preserves the
    fungicide role. No specific molecular target, strain observation, resistance,
    producer or clinical claim is populated.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: CHEBI137426 row2579 and six adopted citation leads; extraction/seeding
    synonym mapping
  accessed_at: '2026-10-21T14:14:56Z'
  support: supports
  summary: The frozen source provides the native graph, processed-food-use definition,
    three aliases, parents, roles, CAS and patent links. SYNONYM maps to EXACT_SYNONYM
    while BRAND NAME maps to BRAND_NAME. Hidden and ignored files were included in
    the owner/overlay search.
  snapshot_sha256: e0c65b59d7f4f8df9fa359d47fa89ff1ae0c2bc42945e2463105211429bb769c
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/137426/
  locator: complete current entry, structure and asserted term responses
  accessed_at: '2026-10-21T14:14:56Z'
  support: supports
  summary: Current ChEBI matches native keto SMILES/InChI, formula, charge and masses.
    Pyran2,4-dione and ketone parents resolve and fit the graph. Both antimicrobial
    roles resolve. Current added bibliography is distinguished from the six frozen
    adopted leads.
  snapshot_sha256: 6803c6a5886b441059050cf18f9d70689f9e448c71cac8f43fae0ee8aa8f1d8c
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5 / InChI 1.07.3
  locator: 035-authority-chemistry.py;350-authority-chemistry.json
  accessed_at: '2026-10-21T14:14:56Z'
  support: supports
  summary: Native, current ChEBI molfile and PubChem122903 agree on PGRHXDWITVMQBC-UHFFFAOYSA-N.
    The independent GSRS enol is PKLPQOJFHFGVBS-UHFFFAOYSA-N; RDKit tautomer canonicalization
    gives that same enol key from both. The keto graph has one unspecified tetrahedral
    carbon that becomes planar in the enol; no isolated stable-enantiomer identity
    is claimed or automatically assigned.
  snapshot_sha256: 5b200975e96ef2f5e8bbc24f513b09d0655d6203bcaef98adbd4e20ffcc7b4e8
- evidence_id: gsrs
  kind: authority
  reference: https://api.fda.gov/other/substance.json?search=unii%3A2KAG279R6R&limit=1
  locator: GSRS2KAG279R6R version19 full names, enol structure and salt relationship
  accessed_at: '2026-10-21T14:14:56Z'
  support: supports
  summary: Official GSRS explicitly types BIOCIDE470F as bn (brand name), while systematic
    names and dehydroacetic-acid names have different types. It encodes the neutral
    enol and distinguishes sodium dehydroacetate. It corroborates CAS520-45-6 at substance
    scope; this is not proprietary CAS registry verification or a native GSRS exact
    xref.
  snapshot_sha256: 58238fe4f16dfcdc12bc3c9db397d431bc3e131fdb48f338bfc50a778fb91411
- evidence_id: activity1954
  kind: primary_source
  reference: https://doi.org/10.1271/nogeikagaku1924.28.727
  locator: complete publisher English abstract; original PDF p728 structure/Methods
    and p729 culture-condition table
  accessed_at: '2026-10-21T14:14:56Z'
  support: supports
  summary: The original distinguishes DHA from dehydroacetocarboxylic acid. DHA inhibits
    yeast and Acetobacter under tested conditions while Lactobacillus behavior differs;
    activity varies with medium pH. The actual p728 figure depicts keto/enol representations,
    and the method uses photoelectric turbidity rather than a direct target-binding
    assay. The full Japanese text was not independently translated.
  snapshot_sha256: 54e71aa2efd0b824b28a163b1a90a8f4ee21a9f2310f22e8bf16163aa640c30a
- evidence_id: activity2025
  kind: primary_source
  reference: https://doi.org/10.29356/jmcs.v69i2.2213
  locator: Pyrone Biomonitored Synthesis, journal2025 issue / repository Epub2026-02-06;
    compound1 synthesis/characterization, complete antimicrobial Methods and Table1
  accessed_at: '2026-10-21T14:14:56Z'
  support: supports
  summary: Compound1 is characterized dehydroacetic acid drawn/named in its enol representation.
    Table1 reports625 micrograms/mL for S.aureus UFPEDA02, P.aeruginosa UFPEDA416
    and C.albicans, with higher endpoints for the other tested organisms. Methods
    specify96-well microdilution, resazurin,37C18–24h bacteria and30C48–72h fungi.
    The manuscript calls the media agar despite describing microdilution, and supplies
    a stock McFarland inoculum without a clear final well concentration. These uncertainties
    must accompany any numerical reuse; the assay does not measure bactericidal/fungicidal
    killing or protein binding.
  snapshot_sha256: bc8e996f95e6e3abcaa1f9ffb63150a5b9af183d67450ac9ed3504eeadcac7d0
- evidence_id: adopted
  kind: primary_source
  reference: PMID:18960990;23790920;25813167;28166217;4030634;6885696
  locator: all six adopted bibliographic records and complete indexed abstracts
  accessed_at: '2026-10-21T14:14:56Z'
  support: supports
  summary: 18960990 is metal-ion gravimetry;25813167 is vibrational spectroscopy;23790920,4030634
    and6885696 describe analytical determination in processed food/wine/squash.28166217
    concerns mammalian MR1/MAIT ligand biology and its abstract does not establish
    a bacterial target for DHA. These are not six independent antimicrobial mechanisms.
  snapshot_sha256: cd63ca6535056ee523bad323411bfefb87dc2c9dd18836be4aaf480cb6ca8149
- evidence_id: patentUS
  kind: primary_source
  reference: https://patents.google.com/patent/US3849579A/en
  locator: original patent description, examples1–8, TableI and claims1–3
  accessed_at: '2026-10-21T14:14:56Z'
  support: supports
  summary: The document specifically names dehydroacetic acid/methylacetopyronone
    and its possible water-soluble salts in cucumber brining. It claims reduced gas/bloating
    while retaining yeast growth. Food-processing applicability is supported historically,
    but suppression of gas production is not fungicidal killing, and the patent does
    not quantify current predominance of food use.
  snapshot_sha256: 6908de4d08c4a87a25951e214a71da2afb1ab7fe46a705298a8c512d9079f6eb
- evidence_id: patentAU
  kind: primary_source
  reference: https://patents.google.com/patent/AU2004287448A1/en
  locator: bibliographic identity, technical field and composition/method claims
  accessed_at: '2026-10-21T14:14:56Z'
  support: supports
  summary: The exact A1 application concerns skin-care compositions containing DHA,
    isomers/salts/derivatives plus skin-care actives and a carrier. It is a related
    document as natively typed, not an exact single-molecule efficacy or regulatory-approval
    record. The kindless URL returned404; the explicit A1 publication resolves.
  snapshot_sha256: 00fe4057dc1d1eb60f485bc8f4367e627418a88af33b34445458f68df199cc57
- evidence_id: document-link
  kind: authority
  reference: https://en.wikipedia.org/wiki/Dehydroacetic_acid
  locator: resolved native topic link and identifier/tautomer context
  accessed_at: '2026-10-21T14:14:56Z'
  support: context_only
  summary: The native Wikipedia link is a correctly partitioned topic document, not
    an exact molecular authority. Scientific conclusions in this review use inspected
    original papers and official chemical sources rather than this page.
  snapshot_sha256: 32c0db6a24e4942a7ff13c0f158d331648c40a889ea916c82b707aab8ca15083
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral keto serialization and enol relationship
  outcome: supported
  summary: Chemical encoding, formula, charge and masses are coherent. An independent
    enol representation is related by explicit tautomer normalization; the review
    does not conflate sodium salt or derivatives with the native neutral molecule.
  target_ids:
  - CHEBI:137426
  evidence_ids:
  - native
  - chebi
  - chemistry
  - gsrs
  - activity1954
- assessment_id: names
  area: representation
  topic: Chemical aliases versus brand
  outcome: concern
  summary: The systematic keto name fits the encoded graph and methylacetopyronone
    is used in the original patent. GSRS explicitly labels Biocide470F as a brand;
    the native EXACT_SYNONYM type loses that distinction.
  target_ids:
  - CHEBI:137426
  evidence_ids:
  - native
  - gsrs
  - patentUS
  - owner
- assessment_id: grounding
  area: grounding
  topic: Chemical parents, CAS and document partition
  outcome: supported
  summary: Both parents are broader chemical categories and the public sources corroborate
    CAS520-45-6 at the tautomeric-substance level. Both patents and the Wikipedia
    topic resolve as document links, without implying single-agent clinical efficacy.
  target_ids:
  - CHEBI:137426
  evidence_ids:
  - chebi
  - gsrs
  - patentUS
  - patentAU
  - document-link
- assessment_id: activity
  area: evidence
  topic: Antibacterial/fungal activity with assay boundaries
  outcome: supported
  summary: Original growth-inhibition evidence supports antimicrobial eligibility.
    The1954 pH dependence and2025 preparation/method limitations prevent universal
    organism or quantitative killing claims. ANTIBACTERIAL filing keeps the fungicide
    role rather than discarding it.
  target_ids:
  - CHEBI:137426
  evidence_ids:
  - activity1954
  - activity2025
  - native
- assessment_id: definition
  area: scope
  topic: Structural definition and historical processed-food use
  outcome: supported
  summary: The structural definition fits. Original analytical papers and the cucumber-brining
    patent support historical food-processing use; they do not establish present-day
    market predominance or current legal permission. That unquantified use emphasis
    remains a limitation, not a fabricated regulatory conclusion.
  target_ids:
  - CHEBI:137426
  evidence_ids:
  - chebi
  - adopted
  - patentUS
- assessment_id: optional
  area: completeness
  topic: Mechanism, protein targets, resistance, clinical and producer domains
  outcome: unknown
  summary: No corresponding specific native claims exist. Neither derivative docking
    nor host MR1 activity establishes a bacterial protein target for the exact parent
    compound. No optional target/causal/clinical field is filled by inference.
  target_ids:
  - CHEBI:137426
  evidence_ids:
  - native
  - adopted
  - activity2025
- assessment_id: provenance
  area: provenance
  topic: Frozen source and adopted-lead disposition
  outcome: supported
  summary: The source mint and four history events reconcile. All six adopted abstracts
    were inspected and retained at their actual evidentiary scope. Native SEEDED status
    is unchanged.
  target_ids:
  - CHEBI:137426
  evidence_ids:
  - native
  - owner
  - adopted
findings:
- finding_id: F1
  issue_key: dehydroacetic-acid-biocide470f-brand-type
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Biocide470F is a brand name, not an exact chemical synonym
  description: GSRS2KAG279R6R explicitly marks BIOCIDE470F as name type bn. The native
    alias uses EXACT_SYNONYM. Preserve the searchable alias with BRAND_NAME typing
    through reproducible source handling, without inferring current product marketing
    or changing the neutral molecular graph.
  target_ids:
  - CHEBI:137426
  field_paths:
  - synonyms[1].synonym_type
  evidence_ids:
  - native
  - gsrs
  - owner
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  rule_id: native-review-checklist:Equivalence
  native_severity: minor
  normalization_reason: The compound identity remains coherent; this is a non-blocking
    alias-type/provenance distinction.
actions:
- action_id: A1
  description: Retain Biocide470F as a brand alias through maintained extraction/seeding.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:137426
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  acceptance_checks:
  - Adjudicate the source synonym type as BRAND_NAME using the official registry evidence;
    make the correction survive source refresh and reseeding.
  - Preserve native keto identity, role list and document links; do not replace the
    graph solely to match an enol registry serialization.
  - Run schema/strict, molecular consistency, source reproduction and required QC
    after an authorized curation change.
limitations:
- The1954 English abstract, actual p728 structural figure/Methods and p729 culture-condition
  table were inspected; the complete Japanese article was not independently translated
  or all figures digitized.
- The2025 paper was inspected for compound1 synthesis/characterization, complete antimicrobial
  Methods and Table1/results. Its agar/microdilution wording, incomplete final-inoculum
  detail and several chemical-text typographical errors remain source limitations;
  no exact numerical activity record is imported.
- All six adopted sources were read at complete indexed-abstract depth. The host MR1
  paper was not read in full and was not used to assign a microbial target.
- The native food-use emphasis is historically supported but current geographic regulatory
  status and relative market usage were not surveyed. The review supplies no food-preservation
  recommendation.
- GSRS uses an enol representation and native uses keto; explicit tautomer normalization
  relates them without making their raw Standard InChIKeys identical. CAS common-chemistry
  access returned401, so the proprietary registry was not independently inspected.
- No native gene/locus/pathway claim required a structured-adapter query. Derivative
  and host-cell findings were not transferred to the parent antibiotic.
- All original captured input hashes were preserved. No native record, source inventory,
  configuration or generated product was edited.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
