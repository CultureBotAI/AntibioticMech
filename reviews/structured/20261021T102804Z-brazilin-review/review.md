# brazilin: exact chemical form and primary evidence scope

- Review: 20261021T102804Z-brazilin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:59:33Z
- Finished UTC: 2026-10-21T10:28:04Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Two minor corrections concern the red-pigment definition and an internally inconsistent KNApSAcK cross-reference. The supported native stereospecific graph should be preserved. Primary activity is kept separate from host-cell signaling, mixtures and other compounds. Focused schema, strict and molecular consistency checks pass.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position167; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3170 | data/antibiotics/antibacterial/brazilin.yaml | generated | brazilin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:3170 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:3170 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:3170 | Actual focused execution exited 0. |
| Structured protein-context applicability | not_applicable | False | CHEBI:3170 | The native record contains no protein, gene, regulator, pathway or transcriptomic-response claim. Literature host-cell signaling and chemical dye assays are not used to infer bacterial targets or expression responses. |
| Authoritative full QC | failed | True | CHEBI:3170 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3170 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3170 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3170 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3170 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3170 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3170 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3170 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3170 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact graph, chemical form and external mappings

identity: concern. Targets: CHEBI:3170.

Internal chemical representation is consistent. The KNApSAcK page needs qualification because its descriptors disagree with one another and with the native enantiomer.

### Chemical parents and broad antibacterial role

grounding: supported. Targets: CHEBI:3170.

Current chemical parents fit the graph and original biological evidence supports bounded antibacterial context. Specific MICs, host-cell effects and compound-family mechanisms are not generalized.

### Source-owned definition

evidence: concern. Targets: CHEBI:3170.

The reduced brazilin description should distinguish colorless precursor from oxidized red pigment.

### Maintained source and history

provenance: supported. Targets: CHEBI:3170.

Source ownership and initial hashes are preserved; no native data, source inventories or history were edited.

### Primary evidence and optional fields

completeness: unknown. Targets: CHEBI:3170.

Optional exact-assay evidence can be improved, but blanks are not missing requirements. A direct bacterial protein target, producer biosynthesis or clinical indication is not inferred from the inspected evidence.

### Focused repository and chemical gates

schema: supported. Targets: CHEBI:3170.

Actual focused gates and chemical checks pass; scientific source fidelity remains a separate assessment.

## Findings

### F1: Distinguish colorless brazilin from oxidized red brazilein

minor / open / confirmed; issue key: brazilin-reduced-form-color-definition.

The exact reduced molecule is described as a red pigment, repeating the brazilein definition. Original photophysical work identifies brazilin as colorless reduced brazilein, corroborated by a white isolated material that oxidizes red-brown. The correction concerns chemical form and color; the established dye-context aliases and native structure should be retained.

### F2: Qualify the internally inconsistent KNApSAcK mapping

minor / open / confirmed; issue key: brazilin-knapsack-descriptor-conflict.

KNApSAcK C00010268 identifies the expected name/formula but its displayed InChI specifies the opposite enantiomer and its SMILES omits both configurations. Its displayed key does not reproduce its InChI. The native graph agrees with PubChem and KEGG and should not be changed to match the inconsistent page.

## Recommended Actions And Acceptance Checks

### A1

Correct the reduced-form description and qualify or repair the KNApSAcK crosswalk through maintained owners.

- Describe brazilin as a reduced dye precursor that oxidizes to colored brazilein; retain plant occurrence and historically used aliases with appropriate scope.
- Verify full native key UWHUTZOCTZJUKC-JKSUJKDBSA-N, (6aS,11bR), formula and charge against independent structures. Record KNApSAcK descriptor conflict; seek upstream correction or qualify/suppress the exact-structure mapping without replacing the native enantiomer.
- Use a documented maintained source correction and canary reseeding; do not make a generated YAML-only edit. Run focused and required corpus/history gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/brazilin.yaml; Entire native YAML, exact maintained source row and history | supports | The SEEDED record contains source-owned chemical identity, definition, synonyms, cross-references and antibacterial role. It has no populated direct molecular target, resistance mechanism, quantitative susceptibility, producer organism or causal graph. The graph is neutral C16H14O5 with two assigned centres, (6aS,11bR), and the (+)-brazilin synonym. The definition repeats the red-pigment description used for brazilein. |
| source | data/raw/chebi_antimicrobials.tsv; data/raw/chebi_role_names.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; 167-raw.json; initially captured maintained owners | supports | The adopted source row reproduces the native fields. Local exact identity and owner searches included ignored and hidden files outside Git internals and virtual environments. No matching curator override was found within inspected maintained inventories; this is bounded local absence, not evidence absence. |
| chemistry | Independent native molecular encodings and focused gates; 167-chemistry.json; 167-focused-results.json | supports | SMILES and Standard InChI independently reproduce the complete stored key, molecular formula, formal charge, component count and both mass values at native precision. Source mint and focused schema/strict checks pass. Both stereocentres are assigned. |
| grounding | https://www.ebi.ac.uk/chebi/CHEBI:3170; 167-chebi.html; 167-parents.json | supports | Current source definition, roles and chemical parents resolve. The direct parents are tertiary alcohol CHEBI:26878, catechols CHEBI:33566, organic heterotetracyclic compound CHEBI:38163. These chemical classes fit the encoded graph; database classification is not promoted to an experimentally demonstrated protein mechanism. |
| adopted | Adopted ChEBI publication leads; 167-adopted.json; complete original indexed abstracts | context_only | All 10 adopted records resolved and their complete original abstracts were read. PMID24963948 directly tests purified brazilin and separately a standardized extract against acne-associated bacteria. PMID25248564 concerns separation and retinal protection;25233024 solar cells;24735611 host IL-1 signaling;24716195 endothelial high-glucose injury;24095700 rat pharmacokinetics;22920671 asthma;22044921 UVB-exposed fibroblasts;18983903 macrophages and18021765 auditory cells. Host signaling and rat exposure are not antibacterial targets or clinical efficacy. |
| antibacterial2014 | PMID:24703330; DOI:10.1016/j.phymed.2014.03.004; 166-adopted.json; complete original abstract | supports | The study separately tests brazilin1, brazilein2 and sappanone B3. Its reported MIC/MBC ranges span compounds and strains and cannot be assigned wholesale to one record. Strong aminoglycoside synergy and time-kill conclusions are chiefly for brazilin1; brazilein2 and sappanone B3 combinations were less potent. This supports bounded antibacterial context without a direct protein target or clinical treatment claim. |
| photochemistry | PMID:24050687; DOI:10.1021/jp404789f; 166-adopted.json; complete original abstract | supports | The original aqueous acid-base/photophysical study explicitly distinguishes colorless reduced brazilin from oxidized brazilein. Their chemical forms, protonation and excited-state properties differ; a dye-family name does not make the exact reduced molecule itself the red chromophore. |
| synthesis | PMID:23657435; DOI:10.1039/C3CC42385A; Complete original abstract and publisher page; limited SI access | partial | The original report describes enantioselective synthesis of (+)-brazilin and (-)-brazilein. The abstract does not independently establish every native stereochemical assignment. Only the initial SI general-method/intermediate pages were accessible through the web route; final-product spectra and assignments were not independently audited. |
| external-identity | PubChem:73384; KEGG:C09920; KNApSAcK:C00010268; 167-pubchem.json; 167-kegg.mol; 167-knapsack.html; 017-root-next-xref-chemistry.json | partial | Current PubChem and independently parsed KEGG reproduce the native full key UWHUTZOCTZJUKC-JKSUJKDBSA-N. KNApSAcK names brazilin and the correct gross formula but its displayed InChI encodes the opposite enantiomer (UWHUTZOCTZJUKC-CVEARBPZSA-N), while its SMILES omits both stereocentres and its displayed key is also nonconcordant. This internally inconsistent external page cannot independently verify native absolute configuration. CAS and Reaxys were checked as adopted source crosswalks, without proprietary registry access. |
| acne | PMID:24963948; DOI:10.3109/13880209.2014.884607; 167-adopted.json; complete original abstract | supports | Assay-guided isolation yielded pure brazilin, tested by broth microdilution against P. acnes with reported MIC15.6 and MBC31.2 micrograms/mL. These are abstract-level values: exact strain, medium, incubation and stability were not independently recovered. The 39.9% brazilin-rich extract is a separate test material and its potency cannot be attributed directly to pure brazilin. |
| white-isolate | https://pmc.ncbi.nlm.nih.gov/articles/PMC3282169/; Original Methods2.1–2.2, visible through indexed primary PMC text | supports | Preparative HPLC fractions from C. sappan heartwood produced a white compound that rapidly oxidized to red-brown material; the isolate was identified by proton NMR as (6aS,11bR)-brazilin. The paper separately describes commercial Natural Red24 as sappan-wood extract. Only the relevant extraction/identification Methods were inspected; its host-cell experiments are not used as antibacterial evidence. |

## Limits And Additional Notes

- Current public records and native molecular encodings were checked, but absolute structures were not independently rederived from raw spectroscopy or crystallography. Proprietary registry databases were not accessed.
- No exhaustive clinical, resistance, transcriptomic or natural-biosynthesis survey is claimed. Optional fields and source classifications were assessed at their actual native evidence level.
- All ten adopted original abstracts were read. The2014 antibacterial full papers were not inspected; abstract assay ranges and synergy conclusions are not converted to exact strain-specific measurements. The2013 synthesis SI was only partly accessible, and no final-product stereochemical claim is based on its unread sections.
- Brazilein2020 extraction Methods and Conclusion were read; its complete spectral Results were not reanalyzed. Brazilin2011 relevant isolation Methods were visible through indexed primary PMC text, while direct PMC/XML access was blocked; no full-paper access is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 13 captured repository input hashes were rechecked unchanged. Native records, source inventories and curation status remain unchanged.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T102804Z-brazilin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'brazilin: exact chemical form and primary evidence scope'
started_at: '2026-10-21T09:59:33Z'
finished_at: '2026-10-21T10:28:04Z'
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
summary: Two minor corrections concern the red-pigment definition and an internally
  inconsistent KNApSAcK cross-reference. The supported native stereospecific graph
  should be preserved. Primary activity is kept separate from host-cell signaling,
  mixtures and other compounds. Focused schema, strict and molecular consistency checks
  pass.
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
  - path: data/antibiotics/antibacterial/brazilin.yaml
    sha256: c528a3654a5d3c8ed24f09e594cd602d3543ffa1280fd2f00adb9c23e174ae28
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
targets:
- target_id: CHEBI:3170
  path: data/antibiotics/antibacterial/brazilin.yaml
  label: brazilin
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
  selection: Initially uncovered queue position167; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3170
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3170
  command: .venv/bin/python /private/tmp/am-review-session/focus014-root.py 167
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3170
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/brazilin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3170
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/brazilin.yaml --out /private/tmp/am-review-session/167-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-applicability
  name: Structured protein-context applicability
  status: not_applicable
  required: false
  summary: The native record contains no protein, gene, regulator, pathway or transcriptomic-response
    claim. Literature host-cell signaling and chemical dye assays are not used to
    infer bacterial targets or expression responses.
  target_ids:
  - CHEBI:3170
  evidence_ids:
  - native
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:3170
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
  - CHEBI:3170
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
  - CHEBI:3170
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
  - CHEBI:3170
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
  - CHEBI:3170
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
  - CHEBI:3170
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
  - CHEBI:3170
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
  - CHEBI:3170
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
  - CHEBI:3170
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/brazilin.yaml
  locator: Entire native YAML, exact maintained source row and history
  accessed_at: '2026-10-21T10:19:49Z'
  support: supports
  summary: The SEEDED record contains source-owned chemical identity, definition,
    synonyms, cross-references and antibacterial role. It has no populated direct
    molecular target, resistance mechanism, quantitative susceptibility, producer
    organism or causal graph. The graph is neutral C16H14O5 with two assigned centres,
    (6aS,11bR), and the (+)-brazilin synonym. The definition repeats the red-pigment
    description used for brazilein.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/chebi_role_names.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: 167-raw.json; initially captured maintained owners
  accessed_at: '2026-10-21T10:19:49Z'
  support: supports
  summary: The adopted source row reproduces the native fields. Local exact identity
    and owner searches included ignored and hidden files outside Git internals and
    virtual environments. No matching curator override was found within inspected
    maintained inventories; this is bounded local absence, not evidence absence.
  snapshot_sha256: 1e279202d5dcaa5f9f187b55c87b3bfe35903de1ae283e0a93f34239905d1641
- evidence_id: chemistry
  kind: validation
  reference: Independent native molecular encodings and focused gates
  locator: 167-chemistry.json; 167-focused-results.json
  accessed_at: '2026-10-21T10:19:49Z'
  support: supports
  summary: SMILES and Standard InChI independently reproduce the complete stored key,
    molecular formula, formal charge, component count and both mass values at native
    precision. Source mint and focused schema/strict checks pass. Both stereocentres
    are assigned.
  snapshot_sha256: 7a72c4c8c8d54f932d5aaa1474eb439e711d7e641edd2525cfcabfa5951da2a4
- evidence_id: grounding
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3170
  locator: 167-chebi.html; 167-parents.json
  accessed_at: '2026-10-21T10:19:49Z'
  support: supports
  summary: Current source definition, roles and chemical parents resolve. The direct
    parents are tertiary alcohol CHEBI:26878, catechols CHEBI:33566, organic heterotetracyclic
    compound CHEBI:38163. These chemical classes fit the encoded graph; database classification
    is not promoted to an experimentally demonstrated protein mechanism.
  snapshot_sha256: fb5ea5ea3f929722ed9f4adf9927c8c8ccef2712845383da9e879819d375095c
- evidence_id: adopted
  kind: search
  reference: Adopted ChEBI publication leads
  locator: 167-adopted.json; complete original indexed abstracts
  accessed_at: '2026-10-21T10:19:49Z'
  support: context_only
  summary: All 10 adopted records resolved and their complete original abstracts were
    read. PMID24963948 directly tests purified brazilin and separately a standardized
    extract against acne-associated bacteria. PMID25248564 concerns separation and
    retinal protection;25233024 solar cells;24735611 host IL-1 signaling;24716195
    endothelial high-glucose injury;24095700 rat pharmacokinetics;22920671 asthma;22044921
    UVB-exposed fibroblasts;18983903 macrophages and18021765 auditory cells. Host
    signaling and rat exposure are not antibacterial targets or clinical efficacy.
  search_scope: 'Exact adopted PMID set: 25248564, 25233024, 24963948, 24735611, 24716195,
    24095700, 22920671, 22044921, 18983903, 18021765. Full-text inspection is separately
    described.'
  snapshot_sha256: 16d5bde49599c90ebe936baaadf7f7f59e9a7b5f67166a557c35e5352b581f61
- evidence_id: antibacterial2014
  kind: primary_source
  reference: PMID:24703330; DOI:10.1016/j.phymed.2014.03.004
  locator: 166-adopted.json; complete original abstract
  accessed_at: '2026-10-21T10:19:49Z'
  support: supports
  summary: The study separately tests brazilin1, brazilein2 and sappanone B3. Its
    reported MIC/MBC ranges span compounds and strains and cannot be assigned wholesale
    to one record. Strong aminoglycoside synergy and time-kill conclusions are chiefly
    for brazilin1; brazilein2 and sappanone B3 combinations were less potent. This
    supports bounded antibacterial context without a direct protein target or clinical
    treatment claim.
  snapshot_sha256: 3c20b1856b5636bf5d3141b54a6daee100c0b5631ea27785a6de463fa2d56d15
- evidence_id: photochemistry
  kind: primary_source
  reference: PMID:24050687; DOI:10.1021/jp404789f
  locator: 166-adopted.json; complete original abstract
  accessed_at: '2026-10-21T10:19:49Z'
  support: supports
  summary: The original aqueous acid-base/photophysical study explicitly distinguishes
    colorless reduced brazilin from oxidized brazilein. Their chemical forms, protonation
    and excited-state properties differ; a dye-family name does not make the exact
    reduced molecule itself the red chromophore.
  snapshot_sha256: 3c20b1856b5636bf5d3141b54a6daee100c0b5631ea27785a6de463fa2d56d15
- evidence_id: synthesis
  kind: primary_source
  reference: PMID:23657435; DOI:10.1039/C3CC42385A
  locator: Complete original abstract and publisher page; limited SI access
  accessed_at: '2026-10-21T10:19:49Z'
  support: partial
  summary: The original report describes enantioselective synthesis of (+)-brazilin
    and (-)-brazilein. The abstract does not independently establish every native
    stereochemical assignment. Only the initial SI general-method/intermediate pages
    were accessible through the web route; final-product spectra and assignments were
    not independently audited.
  snapshot_sha256: 3c20b1856b5636bf5d3141b54a6daee100c0b5631ea27785a6de463fa2d56d15
- evidence_id: external-identity
  kind: database
  reference: PubChem:73384; KEGG:C09920; KNApSAcK:C00010268
  locator: 167-pubchem.json; 167-kegg.mol; 167-knapsack.html; 017-root-next-xref-chemistry.json
  accessed_at: '2026-10-21T10:19:49Z'
  support: partial
  summary: Current PubChem and independently parsed KEGG reproduce the native full
    key UWHUTZOCTZJUKC-JKSUJKDBSA-N. KNApSAcK names brazilin and the correct gross
    formula but its displayed InChI encodes the opposite enantiomer (UWHUTZOCTZJUKC-CVEARBPZSA-N),
    while its SMILES omits both stereocentres and its displayed key is also nonconcordant.
    This internally inconsistent external page cannot independently verify native
    absolute configuration. CAS and Reaxys were checked as adopted source crosswalks,
    without proprietary registry access.
  snapshot_sha256: 99afdc9a6474bdb1a805a14e11e578fddc453159be907d617b40d1d8a68d02a4
- evidence_id: acne
  kind: primary_source
  reference: PMID:24963948; DOI:10.3109/13880209.2014.884607
  locator: 167-adopted.json; complete original abstract
  accessed_at: '2026-10-21T10:19:49Z'
  support: supports
  summary: 'Assay-guided isolation yielded pure brazilin, tested by broth microdilution
    against P. acnes with reported MIC15.6 and MBC31.2 micrograms/mL. These are abstract-level
    values: exact strain, medium, incubation and stability were not independently
    recovered. The 39.9% brazilin-rich extract is a separate test material and its
    potency cannot be attributed directly to pure brazilin.'
  snapshot_sha256: 16d5bde49599c90ebe936baaadf7f7f59e9a7b5f67166a557c35e5352b581f61
- evidence_id: white-isolate
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3282169/
  locator: Original Methods2.1–2.2, visible through indexed primary PMC text
  accessed_at: '2026-10-21T10:19:49Z'
  support: supports
  summary: Preparative HPLC fractions from C. sappan heartwood produced a white compound
    that rapidly oxidized to red-brown material; the isolate was identified by proton
    NMR as (6aS,11bR)-brazilin. The paper separately describes commercial Natural
    Red24 as sappan-wood extract. Only the relevant extraction/identification Methods
    were inspected; its host-cell experiments are not used as antibacterial evidence.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact graph, chemical form and external mappings
  outcome: concern
  summary: Internal chemical representation is consistent. The KNApSAcK page needs
    qualification because its descriptors disagree with one another and with the native
    enantiomer.
  target_ids:
  - CHEBI:3170
  evidence_ids:
  - chemistry
  - external-identity
- assessment_id: classification
  area: grounding
  topic: Chemical parents and broad antibacterial role
  outcome: supported
  summary: Current chemical parents fit the graph and original biological evidence
    supports bounded antibacterial context. Specific MICs, host-cell effects and compound-family
    mechanisms are not generalized.
  target_ids:
  - CHEBI:3170
  evidence_ids:
  - grounding
  - antibacterial2014
- assessment_id: definition
  area: evidence
  topic: Source-owned definition
  outcome: concern
  summary: The reduced brazilin description should distinguish colorless precursor
    from oxidized red pigment.
  target_ids:
  - CHEBI:3170
  evidence_ids:
  - native
  - photochemistry
- assessment_id: provenance
  area: provenance
  topic: Maintained source and history
  outcome: supported
  summary: Source ownership and initial hashes are preserved; no native data, source
    inventories or history were edited.
  target_ids:
  - CHEBI:3170
  evidence_ids:
  - source
  - chemistry
- assessment_id: completeness
  area: completeness
  topic: Primary evidence and optional fields
  outcome: unknown
  summary: Optional exact-assay evidence can be improved, but blanks are not missing
    requirements. A direct bacterial protein target, producer biosynthesis or clinical
    indication is not inferred from the inspected evidence.
  target_ids:
  - CHEBI:3170
  evidence_ids:
  - native
  - antibacterial2014
- assessment_id: schema
  area: schema
  topic: Focused repository and chemical gates
  outcome: supported
  summary: Actual focused gates and chemical checks pass; scientific source fidelity
    remains a separate assessment.
  target_ids:
  - CHEBI:3170
  evidence_ids:
  - chemistry
findings:
- finding_id: F1
  issue_key: brazilin-reduced-form-color-definition
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish colorless brazilin from oxidized red brazilein
  description: The exact reduced molecule is described as a red pigment, repeating
    the brazilein definition. Original photophysical work identifies brazilin as colorless
    reduced brazilein, corroborated by a white isolated material that oxidizes red-brown.
    The correction concerns chemical form and color; the established dye-context aliases
    and native structure should be retained.
  target_ids:
  - CHEBI:3170
  field_paths:
  - definition
  evidence_ids:
  - native
  - photochemistry
  - white-isolate
  rule_id: 'native-review-checklist: exact chemical identity and source fidelity'
  native_severity: bounded source-definition or external-metadata correction
  normalization_reason: The native exact molecular identity remains supported. The
    defects are confined to source-owned descriptive text or an internally inconsistent
    external cross-reference.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted definition and external cross-reference
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source field reproduction
- finding_id: F2
  issue_key: brazilin-knapsack-descriptor-conflict
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify the internally inconsistent KNApSAcK mapping
  description: KNApSAcK C00010268 identifies the expected name/formula but its displayed
    InChI specifies the opposite enantiomer and its SMILES omits both configurations.
    Its displayed key does not reproduce its InChI. The native graph agrees with PubChem
    and KEGG and should not be changed to match the inconsistent page.
  target_ids:
  - CHEBI:3170
  field_paths:
  - xrefs
  evidence_ids:
  - external-identity
  - chemistry
  rule_id: 'native-review-checklist: exact chemical identity and source fidelity'
  native_severity: bounded source-definition or external-metadata correction
  normalization_reason: The native exact molecular identity remains supported. The
    defects are confined to source-owned descriptive text or an internally inconsistent
    external cross-reference.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted definition and external cross-reference
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source field reproduction
actions:
- action_id: A1
  description: Correct the reduced-form description and qualify or repair the KNApSAcK
    crosswalk through maintained owners.
  finding_ids:
  - F1
  - F2
  target_ids:
  - CHEBI:3170
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted definition and external cross-reference
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source field reproduction
  acceptance_checks:
  - Describe brazilin as a reduced dye precursor that oxidizes to colored brazilein;
    retain plant occurrence and historically used aliases with appropriate scope.
  - Verify full native key UWHUTZOCTZJUKC-JKSUJKDBSA-N, (6aS,11bR), formula and charge
    against independent structures. Record KNApSAcK descriptor conflict; seek upstream
    correction or qualify/suppress the exact-structure mapping without replacing the
    native enantiomer.
  - Use a documented maintained source correction and canary reseeding; do not make
    a generated YAML-only edit. Run focused and required corpus/history gates.
limitations:
- Current public records and native molecular encodings were checked, but absolute
  structures were not independently rederived from raw spectroscopy or crystallography.
  Proprietary registry databases were not accessed.
- No exhaustive clinical, resistance, transcriptomic or natural-biosynthesis survey
  is claimed. Optional fields and source classifications were assessed at their actual
  native evidence level.
- All ten adopted original abstracts were read. The2014 antibacterial full papers
  were not inspected; abstract assay ranges and synergy conclusions are not converted
  to exact strain-specific measurements. The2013 synthesis SI was only partly accessible,
  and no final-product stereochemical claim is based on its unread sections.
- Brazilein2020 extraction Methods and Conclusion were read; its complete spectral
  Results were not reanalyzed. Brazilin2011 relevant isolation Methods were visible
  through indexed primary PMC text, while direct PMC/XML access was blocked; no full-paper
  access is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 13 captured repository input hashes were rechecked unchanged. Native records,
  source inventories and curation status remain unchanged.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:3170
- https://doi.org/10.1016/j.phymed.2014.03.004
- https://doi.org/10.1021/jp404789f
- https://www.knapsackfamily.com/knapsack_core/information.php?word=C00010268
```
