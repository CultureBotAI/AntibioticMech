# Furagin: unspecified native geometry conflicts with two exact chemical links

- Review: 20261021T170358Z-furagin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:45:55Z
- Finished UTC: 2026-10-21T17:03:58Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native ChEBI identity consistently and explicitly leaves the two linking double-bond configurations unspecified. Current exact PubChem and ChEMBL links denote the E,E-configured compound instead. One confirmed major grounding finding identifies that equivalence error without calling the native graph invalid. Original clinical and microbiological sources support the drug/class context with material and assay limits.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position480; one exact record in path order. The thirteen original captured inputs remain unchanged; actual owner/readiness inputs were appended before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:131714 | data/antibiotics/antibacterial/furagin.yaml | generated | furagin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:131714 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:131714 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:131714 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:131714 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:131714 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:131714 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:131714 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:131714 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:131714 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:131714 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:131714 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:131714 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Intentional unspecified geometry

identity: supported. Targets: CHEBI:131714.

Native structure, definition and current ChEBI agree. The absence of E/Z assignment is explicit and is not itself a mixture claim or a parser error.

### Exact versus narrower configured identities

grounding: concern. Targets: CHEBI:131714.

PubChem6870646 and CHEMBL3707254 narrow the unspecified native concept to E,E. They cannot be retained as exact identity assertions without a deliberate identity/mapping decision.

### Antibacterial drug role and native definition

evidence: supported. Targets: CHEBI:131714.

The cited clinical treatment comparison and original commercial-material E.coli assays support furagin/furazidin antibacterial use. Clinical, pharmacokinetic and susceptibility statements remain at their original scope; no exact native MIC or resistance genotype is asserted.

### Maintained ownership and complete history

provenance: supported. Targets: CHEBI:131714.

Both source concepts and all four seed/reseed events were read. ChEBI supplies structure; ARO contributes class and xrefs. Future corrections belong in source reconciliation, with original snapshots preserved.

### Optional mechanisms and adapter applicability

completeness: supported. Targets: CHEBI:131714.

There is no native named gene, molecular target, pathway or expression dataset requiring adapter lookup. Nitrofuran class and MIC correlation alone are not specific reductase or resistance-mechanism proof. Missing optional target and spectrum annotations are not separate defects.

## Findings

### F1: Do not equate unspecified furagin with E,E-specific PubChem and ChEMBL identities

major / open / confirmed; issue key: furagin-unspecified-geometry-exact-configured-xrefs.

The native definition and both encodings explicitly omit the C=C/C=N geometry. PubChem6870646 and CHEMBL3707254 independently encode E,E and yield a different stereochemical InChIKey. Their shared connectivity does not satisfy exact-xref equivalence. This is a positive graph-level scope mismatch, not a failed lookup or evidence that the native unspecified concept must be replaced.

## Recommended Actions And Acceptance Checks

### A1

Reconcile configured and unspecified furagin identities through maintained mapping ownership.

- Decide whether to preserve the explicitly unspecified ChEBI concept or adopt a separately supported E,E identity; do not insert geometry solely to match an imported link.
- If preserving the native concept, remove the non-equivalent links from exact xrefs or represent them only in a schema-supported broader association field with clear scope. If changing identity, coherently update graph, definition, identifiers and source decisions after primary chemical adjudication.
- Regenerate reproducibly, verify complete keys and both double-bond configurations against every retained exact authority, and run focused schema/strict, identity and corpus checks. Preserve drug/document association semantics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/furagin.yaml; Entire native YAML including all names, groundings, source concepts and chronological history | supports | The record is SEEDED, EXACT, and denotes C10H8N4O5 with full key DECBQELQORZLLP-UHFFFAOYSA-N. All 4 history events were read. No quantitative activity, molecular target, resistance object, causal graph or expression dataset is asserted. |
| owners | 480-source-rows.json; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Complete actual inventory and readiness rows, applicable extraction and emission ownership | supports | ChEBI supplies the exact native chemical graph, definition, names, parent/role assignments and its citation list. The seeder preserves source provenance and separates exact molecular links from drug and document associations. ARO additionally supplies the nitrofuran class, alternate label and exact chemical links; its PMID37629208 is assessed separately. The captured PubChem inventory has no exact owner row, because ChEBI supplies the emitted structure. |
| search | 480-local-hits.txt; 480-owners-search.json; 048-root-fetch1-manifest.json through 048-root-fetch5-manifest.json; Ignored-inclusive local owner search and bounded current-authority/primary-publication follow-up | context_only | The initial capture and follow-up exact identifier/name searches included hidden and ignored local files. Public chemical authority entries, all adopted citation abstracts and the specifically identified original papers were read at the depths stated. Search misses and inaccessible endpoints are not proof of global absence. |
| chemistry | 048-root-authority-chemistry.json; 477478-knapsack-check.json; Independent native/current authority graph parsing with existing019 RDKit interpreter | supports | Native SMILES and InChI mutually reproduce the recorded formula, full key and neutral charge. Current ChEBI encodings agree. Current PubChem and ChEMBL both encode E geometry at the linking alkene and imine, producing DECBQELQORZLLP-UAIOPKHMSA-N rather than the deliberately unspecified native DECBQELQORZLLP-UHFFFAOYSA-N. Connectivity and formula agreement do not make these exact stereochemical equivalents. |
| authority | CHEBI:131714; exact parent and role API entries; Complete current compound, names, definition, parents and activity-role definitions | supports | The current ChEBI graph/definition/name types reproduce the native record. Imidazolidine-2,4-dione, the two heterocyclic antibiotic classes and nitrofuran antibiotic parents match the scaffold. ChEBI explicitly leaves the linking C=C and C=N configuration unspecified. Akritoin and Furagin are correctly typed BRAND_NAME. The drug-level KEGG D07998 and DrugCentral4869 associations have broader schema semantics and are not the exact-xref defect. CAS1672-88-4/Reaxys307076 retain source-attributed scope; the WO9841520 patent is a document link. |
| gates | 480-focused-results.json; 480-chemistry.json; Actual focused schema, strict and chemistry outputs | supports | All focused checks exit0; the native graph is internally consistent. All expanded hashes are rechecked before finalization. Internal chemical validity cannot establish the meaning or exactness of an external cross-reference. |
| adopted-chebi | PMID:18060746,10809412,9411425,9172693,468451; All five complete ChEBI-adopted abstracts | supports | PM18060746 is a27-woman acute-cystitis clinical comparison of ciprofloxacin and furagin, supporting actual antibacterial treatment context, not molecular mechanism;10809412 is observational pregnancy exposure;9411425 is a pulmonary adverse-reaction case with provocation;9172693 concerns photochemical reactions with tryptophan;468451 is human pharmacokinetics/food/atropine and comparative antibacterial background. The host safety/PK papers do not become bacterial mechanism evidence or present-day recommendations. |
| adopted-aro | PMID:37629208; DOI:10.3390/jcm12165166; PMC10455607; Complete original main text including Materials/Methods, Results, Discussion and Conclusions | supports | The2023 study assays100 unique clinical urinary E.coli isolates collected February–August2021. Pure commercial furazidin powder is dissolved in DMSO and diluted into Mueller–Hinton broth,0.5–256mg/L,18±2h at35±1C, triplicate, no visible growth endpoint. Furazidin MIC50/90 is8/64mg/L versus16/128 for nitrofurantoin. It compares raw susceptibility and correlations; its13% broth resistance statistic uses nitrofurantoin breakpoints, not a separately validated furazidin breakpoint. The paper itself identifies absent furazidin standards. Neither author extrapolation nor shared class proves a universal cross-resistance genotype or justifies assigning clinical resistance to all high furazidin MICs. Article preparation is named furazidin but does not experimentally resolve all stereochemical states represented by the underspecified native concept. |
| xref | pubchem.compound:6870646; chembl:CHEMBL3707254; Complete exact-CID PubChem properties and ChEMBL molecule structures; independently parsed SMILES/InChI | supports | Both exact authorities explicitly encode E,E geometry and produce DECBQELQORZLLP-UAIOPKHMSA-N. Native and current ChEBI intentionally omit both configurations and produce DECBQELQORZLLP-UHFFFAOYSA-N. These are compatible broader/narrower structure concepts, not exact equivalent representations. The discrepancy comes from ARO’s imported xrefs merged into the ChEBI-led record. The existing drug_xrefs field permits related molecular forms, while xrefs asserts equivalence. |

## Limits And Additional Notes

- Five ChEBI-adopted sources were read at full abstract level; the ARO-adopted2023 microbiology study was read in full main text. The supplementary individual-isolate table was not independently reprocessed.
- The2023 preparation is commercial furazidin; no new absolute E/Z structural proof is claimed from its microbiology Methods. Summary MICs remain preparation- and method-specific.
- The nitrofurantoin clinical breakpoint and its13% resistant proportion cannot be transferred automatically to furazidin. Author conclusions on susceptibility extrapolation are distinguished from demonstrated universal cross-resistance or validated drug-specific interpretation.
- CAS/Reaxys provenance remains source-attributed; the confirmed mismatch is based on directly parsed PubChem and ChEMBL graphs, not registry-name assumptions.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T170358Z-furagin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Furagin: unspecified native geometry conflicts with two exact chemical links'
started_at: '2026-10-21T16:45:55Z'
finished_at: '2026-10-21T17:03:58Z'
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
summary: The native ChEBI identity consistently and explicitly leaves the two linking
  double-bond configurations unspecified. Current exact PubChem and ChEMBL links denote
  the E,E-configured compound instead. One confirmed major grounding finding identifies
  that equivalence error without calling the native graph invalid. Original clinical
  and microbiological sources support the drug/class context with material and assay
  limits.
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
  - path: data/antibiotics/antibacterial/furagin.yaml
    sha256: b06bab9e8c14167df8e5249a12222da97d3820079c3761c483425a77378b58e7
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
    role: context
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
  - path: data/raw/aro_antibiotics.tsv
    role: context
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
  - path: data/raw/pubchem_structures.tsv
    role: context
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
  - path: scripts/enrich_pubchem_structures.py
    role: context
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
targets:
- target_id: CHEBI:131714
  path: data/antibiotics/antibacterial/furagin.yaml
  label: furagin
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
  selection: Initially uncovered queue position480; one exact record in path order.
    The thirteen original captured inputs remain unchanged; actual owner/readiness
    inputs were appended before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:131714
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:131714
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    480
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:131714
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/furagin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:131714
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/furagin.yaml --out /private/tmp/am-review-session/480-strict.tsv
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
  - CHEBI:131714
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
  - CHEBI:131714
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
  - CHEBI:131714
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
  - CHEBI:131714
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
  - CHEBI:131714
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
  - CHEBI:131714
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
  - CHEBI:131714
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
  - CHEBI:131714
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
  - CHEBI:131714
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/furagin.yaml
  locator: Entire native YAML including all names, groundings, source concepts and
    chronological history
  accessed_at: '2026-10-21T16:55:47Z'
  support: supports
  summary: The record is SEEDED, EXACT, and denotes C10H8N4O5 with full key DECBQELQORZLLP-UHFFFAOYSA-N.
    All 4 history events were read. No quantitative activity, molecular target, resistance
    object, causal graph or expression dataset is asserted.
- evidence_id: owners
  kind: record_content
  reference: 480-source-rows.json; scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  locator: Complete actual inventory and readiness rows, applicable extraction and
    emission ownership
  accessed_at: '2026-10-21T16:55:47Z'
  support: supports
  summary: ChEBI supplies the exact native chemical graph, definition, names, parent/role
    assignments and its citation list. The seeder preserves source provenance and
    separates exact molecular links from drug and document associations. ARO additionally
    supplies the nitrofuran class, alternate label and exact chemical links; its PMID37629208
    is assessed separately. The captured PubChem inventory has no exact owner row,
    because ChEBI supplies the emitted structure.
  snapshot_sha256: 1816202c8512e7287bcf222b4084753a52db11e92da1cf74796831f5d201ea02
- evidence_id: search
  kind: search
  reference: 480-local-hits.txt; 480-owners-search.json; 048-root-fetch1-manifest.json
    through 048-root-fetch5-manifest.json
  locator: Ignored-inclusive local owner search and bounded current-authority/primary-publication
    follow-up
  accessed_at: '2026-10-21T16:55:47Z'
  support: context_only
  summary: The initial capture and follow-up exact identifier/name searches included
    hidden and ignored local files. Public chemical authority entries, all adopted
    citation abstracts and the specifically identified original papers were read at
    the depths stated. Search misses and inaccessible endpoints are not proof of global
    absence.
  search_scope: 2026-10-21; rg --no-ignore --hidden exact record label/identifier
    across data, curation, conf, scripts and reports; Europe PMC adopted PMID lookup
    and TITLE_ABS:furagin first100 results, plus web exact compound and primary study
    queries.
  snapshot_sha256: 1816202c8512e7287bcf222b4084753a52db11e92da1cf74796831f5d201ea02
- evidence_id: chemistry
  kind: validation
  reference: 048-root-authority-chemistry.json; 477478-knapsack-check.json
  locator: Independent native/current authority graph parsing with existing019 RDKit
    interpreter
  accessed_at: '2026-10-21T16:55:47Z'
  support: supports
  summary: Native SMILES and InChI mutually reproduce the recorded formula, full key
    and neutral charge. Current ChEBI encodings agree. Current PubChem and ChEMBL
    both encode E geometry at the linking alkene and imine, producing DECBQELQORZLLP-UAIOPKHMSA-N
    rather than the deliberately unspecified native DECBQELQORZLLP-UHFFFAOYSA-N. Connectivity
    and formula agreement do not make these exact stereochemical equivalents.
  snapshot_sha256: fe824fa5edc3ec374c65fdab2cc222b57b90f8cee88df20c83410bf37b9a2982
- evidence_id: authority
  kind: authority
  reference: CHEBI:131714; exact parent and role API entries
  locator: Complete current compound, names, definition, parents and activity-role
    definitions
  accessed_at: '2026-10-21T16:55:47Z'
  support: supports
  summary: The current ChEBI graph/definition/name types reproduce the native record.
    Imidazolidine-2,4-dione, the two heterocyclic antibiotic classes and nitrofuran
    antibiotic parents match the scaffold. ChEBI explicitly leaves the linking C=C
    and C=N configuration unspecified. Akritoin and Furagin are correctly typed BRAND_NAME.
    The drug-level KEGG D07998 and DrugCentral4869 associations have broader schema
    semantics and are not the exact-xref defect. CAS1672-88-4/Reaxys307076 retain
    source-attributed scope; the WO9841520 patent is a document link.
  snapshot_sha256: a9421b76055d7e58c2826fcab2597d0e5043d8c7d4980842e8606258072c97c6
- evidence_id: gates
  kind: validation
  reference: 480-focused-results.json; 480-chemistry.json
  locator: Actual focused schema, strict and chemistry outputs
  accessed_at: '2026-10-21T16:55:47Z'
  support: supports
  summary: All focused checks exit0; the native graph is internally consistent. All
    expanded hashes are rechecked before finalization. Internal chemical validity
    cannot establish the meaning or exactness of an external cross-reference.
  snapshot_sha256: c53560b0596911c574593cbc1e7fcd9801eba4ff98ed10d709ff60b3b4dea0f2
- evidence_id: adopted-chebi
  kind: primary_source
  reference: PMID:18060746,10809412,9411425,9172693,468451
  locator: All five complete ChEBI-adopted abstracts
  accessed_at: '2026-10-21T16:55:47Z'
  support: supports
  summary: PM18060746 is a27-woman acute-cystitis clinical comparison of ciprofloxacin
    and furagin, supporting actual antibacterial treatment context, not molecular
    mechanism;10809412 is observational pregnancy exposure;9411425 is a pulmonary
    adverse-reaction case with provocation;9172693 concerns photochemical reactions
    with tryptophan;468451 is human pharmacokinetics/food/atropine and comparative
    antibacterial background. The host safety/PK papers do not become bacterial mechanism
    evidence or present-day recommendations.
  snapshot_sha256: ecab646b24b06b59fad3f7c70dd11c690fd55f6d3c9352a369142cae81ed06eb
- evidence_id: adopted-aro
  kind: primary_source
  reference: PMID:37629208; DOI:10.3390/jcm12165166; PMC10455607
  locator: Complete original main text including Materials/Methods, Results, Discussion
    and Conclusions
  accessed_at: '2026-10-21T16:55:47Z'
  support: supports
  summary: The2023 study assays100 unique clinical urinary E.coli isolates collected
    February–August2021. Pure commercial furazidin powder is dissolved in DMSO and
    diluted into Mueller–Hinton broth,0.5–256mg/L,18±2h at35±1C, triplicate, no visible
    growth endpoint. Furazidin MIC50/90 is8/64mg/L versus16/128 for nitrofurantoin.
    It compares raw susceptibility and correlations; its13% broth resistance statistic
    uses nitrofurantoin breakpoints, not a separately validated furazidin breakpoint.
    The paper itself identifies absent furazidin standards. Neither author extrapolation
    nor shared class proves a universal cross-resistance genotype or justifies assigning
    clinical resistance to all high furazidin MICs. Article preparation is named furazidin
    but does not experimentally resolve all stereochemical states represented by the
    underspecified native concept.
  snapshot_sha256: 16432f208a72e19903b295177ecad5623de5a1d30c4c1a2b24b1fd29a096f1f6
- evidence_id: xref
  kind: authority
  reference: pubchem.compound:6870646; chembl:CHEMBL3707254
  locator: Complete exact-CID PubChem properties and ChEMBL molecule structures; independently
    parsed SMILES/InChI
  accessed_at: '2026-10-21T16:55:47Z'
  support: supports
  summary: Both exact authorities explicitly encode E,E geometry and produce DECBQELQORZLLP-UAIOPKHMSA-N.
    Native and current ChEBI intentionally omit both configurations and produce DECBQELQORZLLP-UHFFFAOYSA-N.
    These are compatible broader/narrower structure concepts, not exact equivalent
    representations. The discrepancy comes from ARO’s imported xrefs merged into the
    ChEBI-led record. The existing drug_xrefs field permits related molecular forms,
    while xrefs asserts equivalence.
  snapshot_sha256: e81a19524ad3b2b08e6d41c1e0f75091c97a3db7c6d2b6be50ae924642285b25
assessments:
- assessment_id: native-identity
  area: identity
  topic: Intentional unspecified geometry
  outcome: supported
  summary: Native structure, definition and current ChEBI agree. The absence of E/Z
    assignment is explicit and is not itself a mixture claim or a parser error.
  target_ids:
  - CHEBI:131714
  evidence_ids:
  - native
  - authority
  - chemistry
- assessment_id: xref
  area: grounding
  topic: Exact versus narrower configured identities
  outcome: concern
  summary: PubChem6870646 and CHEMBL3707254 narrow the unspecified native concept
    to E,E. They cannot be retained as exact identity assertions without a deliberate
    identity/mapping decision.
  target_ids:
  - CHEBI:131714
  evidence_ids:
  - owners
  - xref
  - chemistry
- assessment_id: activity
  area: evidence
  topic: Antibacterial drug role and native definition
  outcome: supported
  summary: The cited clinical treatment comparison and original commercial-material
    E.coli assays support furagin/furazidin antibacterial use. Clinical, pharmacokinetic
    and susceptibility statements remain at their original scope; no exact native
    MIC or resistance genotype is asserted.
  target_ids:
  - CHEBI:131714
  evidence_ids:
  - adopted-chebi
  - adopted-aro
  - authority
- assessment_id: provenance
  area: provenance
  topic: Maintained ownership and complete history
  outcome: supported
  summary: Both source concepts and all four seed/reseed events were read. ChEBI supplies
    structure; ARO contributes class and xrefs. Future corrections belong in source
    reconciliation, with original snapshots preserved.
  target_ids:
  - CHEBI:131714
  evidence_ids:
  - native
  - owners
  - gates
- assessment_id: completeness
  area: completeness
  topic: Optional mechanisms and adapter applicability
  outcome: supported
  summary: There is no native named gene, molecular target, pathway or expression
    dataset requiring adapter lookup. Nitrofuran class and MIC correlation alone are
    not specific reductase or resistance-mechanism proof. Missing optional target
    and spectrum annotations are not separate defects.
  target_ids:
  - CHEBI:131714
  evidence_ids:
  - native
  - adopted-aro
findings:
- finding_id: F1
  issue_key: furagin-unspecified-geometry-exact-configured-xrefs
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Do not equate unspecified furagin with E,E-specific PubChem and ChEMBL identities
  description: The native definition and both encodings explicitly omit the C=C/C=N
    geometry. PubChem6870646 and CHEMBL3707254 independently encode E,E and yield
    a different stereochemical InChIKey. Their shared connectivity does not satisfy
    exact-xref equivalence. This is a positive graph-level scope mismatch, not a failed
    lookup or evidence that the native unspecified concept must be replaced.
  target_ids:
  - CHEBI:131714
  field_paths:
  - xrefs
  - chemical_structure
  - definition
  evidence_ids:
  - native
  - owners
  - chemistry
  - xref
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported exact chemical xrefs
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Intentionally unspecified native identity
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Cross-source reconciliation and xref emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained identity or mapping override
  rule_id: xrefs exact equivalence and chemical-form scope
  native_severity: major
  normalization_reason: The native concept remains internally coherent and explicitly
    unspecified. The defect is over-specific exact grounding rather than a demonstrated
    wrong native constitution.
actions:
- action_id: A1
  description: Reconcile configured and unspecified furagin identities through maintained
    mapping ownership.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:131714
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported exact chemical xrefs
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Intentionally unspecified native identity
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Cross-source reconciliation and xref emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained identity or mapping override
  acceptance_checks:
  - Decide whether to preserve the explicitly unspecified ChEBI concept or adopt a
    separately supported E,E identity; do not insert geometry solely to match an imported
    link.
  - If preserving the native concept, remove the non-equivalent links from exact xrefs
    or represent them only in a schema-supported broader association field with clear
    scope. If changing identity, coherently update graph, definition, identifiers
    and source decisions after primary chemical adjudication.
  - Regenerate reproducibly, verify complete keys and both double-bond configurations
    against every retained exact authority, and run focused schema/strict, identity
    and corpus checks. Preserve drug/document association semantics.
limitations:
- Five ChEBI-adopted sources were read at full abstract level; the ARO-adopted2023
  microbiology study was read in full main text. The supplementary individual-isolate
  table was not independently reprocessed.
- The2023 preparation is commercial furazidin; no new absolute E/Z structural proof
  is claimed from its microbiology Methods. Summary MICs remain preparation- and method-specific.
- The nitrofurantoin clinical breakpoint and its13% resistant proportion cannot be
  transferred automatically to furazidin. Author conclusions on susceptibility extrapolation
  are distinguished from demonstrated universal cross-resistance or validated drug-specific
  interpretation.
- CAS/Reaxys provenance remains source-attributed; the confirmed mismatch is based
  on directly parsed PubChem and ChEMBL graphs, not registry-name assumptions.
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
