# Review of battacin

- Review: 20261021T101536Z-battacin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:46:07Z
- Finished UTC: 2026-10-21T10:15:36Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native battacin graph agrees with current PubChem and is internally consistent, but three amino-acid centers remain unspecified despite the original paper’s assignments. Two additional unassigned fatty-acid centers need separate resolution. Antibacterial classification and the tentative membrane-mechanism definition have compound-specific primary support; optional additions require assay and material qualifiers.

## Scope And Provenance

Whole SEEDED record and three history events; sole adopted publication, original main paper and structure figure; current PubChem/CARD and source-owned mapping; bounded follow-up synthesis abstract and selected supporting information.

Selection: Path-ordered queue index 148 prepared and hashed before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-e9c8697a8e | data/antibiotics/antibacterial/battacin.yaml | generated | battacin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema check | passed | True | antibioticmech:aro-e9c8697a8e | Exit 0. |
| Documented strict check | passed | True | antibioticmech:aro-e9c8697a8e | Exit 0; zero ERROR rows. |
| Native chemistry and residue mapping | passed | False | antibioticmech:aro-e9c8697a8e | Exit 0; graph, formula, masses, charge, mint and live PubChem agree. The check reports five unassigned centers and maps the three unassigned amino-acid centers to the primary sequence. |
| Native iModulonDB applicability | not_applicable | False | antibioticmech:aro-e9c8697a8e | The record names no gene, protein target, regulator, expression module or specific transcriptomic response. Its chemical membrane-effect claim is not adjudicated by expression-module membership. |
| Authoritative full QC | failed | True | antibioticmech:aro-e9c8697a8e | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-e9c8697a8e | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-e9c8697a8e | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-e9c8697a8e | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-e9c8697a8e | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-e9c8697a8e | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-e9c8697a8e | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-e9c8697a8e | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-e9c8697a8e | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Natural-product stereochemical completeness

identity: concern. Targets: antibioticmech:aro-e9c8697a8e.

The adopted database representation omits known amino-acid configurations; the remaining fatty-acid uncertainty must be tracked separately.

### Mint and broader chemical class

grounding: supported. Targets: antibioticmech:aro-e9c8697a8e.

ARO identity mint reproduces; lipopeptide/nonribosomal-peptide classification is broader than this entity. Antibacterial filing is primary-supported, and no ChEBI role is fabricated.

### Tentative membrane-effect definition

evidence: supported. Targets: antibioticmech:aro-e9c8697a8e.

The definition retains the measured-effect/inference distinction. No direct protein or lipid-binding claim is asserted.

### Adopted source, lead and history

provenance: supported. Targets: antibioticmech:aro-e9c8697a8e.

The sole adopted paper and generated owners were checked; PubChem agreement is documented without equating it with complete stereo.

### Required identity versus optional assay fields

completeness: concern. Targets: antibioticmech:aro-e9c8697a8e.

The confirmed identity omission needs correction; producer, MIC and mechanism additions remain optional and must retain source-specific scope.

### Focused gates

schema: supported. Targets: antibioticmech:aro-e9c8697a8e.

Schema/strict/native chemistry checks pass while the scientific identity concern remains.

## Findings

### F1: Encode the experimentally assigned amino-acid stereochemistry

major / open / confirmed; issue key: aro-3003822-battacin-known-amino-acid-stereo-omitted.

Three amino-acid centers are unspecified in both the adopted/current PubChem graph and native record despite the assignments documented in primary-structure evidence. This is a source-level omission, not an invalid SMILES or a mismatch between native InChI and SMILES. The graph is less specific than the named natural product. Two additional unassigned fatty-acid centers require separate evidence, so completing the amino-acid assignments alone must not be described as complete absolute stereochemical resolution.

## Recommended Actions And Acceptance Checks

### A1

Correct the source-owned stereochemical representation and explicitly retain unresolved fatty-acid scope.

- Use the exact residue mapping and primary assignments in the evidence to complete the three omitted amino-acid centers; independently verify the cyclic sequence, amide closure and all resulting CIP assignments. Keep already supported centers and connectivity unless new primary evidence requires change.
- Seek primary evidence for the fatty-acid stereocenters separately. Do not copy configurations from another octapeptin, a secondary table or a modified synthetic analogue. If unresolved, record a concrete discussion/limitation and withhold full exact-identity sign-off.
- Correct upstream PubChem/ARO mapping or implement a documented maintained literature-backed structure correction path. A plain enrichment refresh of CID177394116 currently reintroduces the omission. Recompute all structure identifiers consistently and preserve truthful structure_source provenance.
- Review the old same-structure PubChem xref after correction: the current partially specified source is not automatically an exact match to a more specific corrected graph. Check merges/minted identity and canary output before corpus reseeding.
- If optionally adding biological claims, preserve exact strain, method, concentrations and inference scope. Resolve the paper’s ATCC strain-number inconsistency; do not transfer linear-analogue biofilm potency or infer direct binding from membrane dyes.
- Use the validated writer/history path for any future native mutation and pass required gates before scientific status promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/battacin.yaml; Whole native YAML and three history events | supports | ARO-minted, PubChem-seeded record has a primary-cited tentative membrane definition and octapeptin B5 synonym. No structured mode, target, MIC, producer, resistance or causal graph is asserted. History remains SEEDED with two subsequent reseeds. |
| chemistry | PubChem CID:177394116; native literal SMILES; 148-chemistry.py;148-chemistry.json;148-pubchem.json | supports | Native SMILES/InChI and current PubChem yield GFRZMEVTBQRIMT-NUWCLZTQSA-N, C50H87N13O10, neutral single graph and consistent masses. Five of ten potential centers are unspecified. Residue mapping identifies unassigned alpha atoms18/44/24 as positions2/3/8, respectively; assigned residues agree with the primary sequence. Two unassigned centers belong to the fatty acid. Atom indices are zero-based in the native literal SMILES. |
| primary-structure | PMID:22183171; DOI:10.1128/AAC.05580-11;148-primary.html/txt; stereochemical Methods, structure Results/Table1, visually inspected Figure1B in148-figure1.jpg | refutes | Advanced Marfey and DNP analyses assign D-Dab1, L-Dab2/3/6/7, L-Leu4/8 and D-Phe5. The proposed fatty-acid connectivity is 3-hydroxy-6-methyloctanoate; this paper does not assign its absolute configuration. |
| primary-biology | PMID:22183171; 148-primary.html/txt; production/antimicrobial/membrane Methods, Tables2/3 and Figures2–4; entire main text read | partial | Fermentation of P. tianmuensis F6-B70 and purification support production. Agar-dilution and viable-count assays support antibacterial activity. P. aeruginosa ATCC27853 NPN and EDTA-assisted diSC3-5/CFU assays support membrane effects with the definition’s cautious inference. Lipid-A interaction remains a proposed explanation, not direct binding. The paper inconsistently prints E. coli ATCC35218/35318; any imported observation needs strain reconciliation. |
| synthesis | PMID:25495219; DOI:10.1021/jm501084q;148-synthesis-core.json;148-synthesis-si.pdf contents,TableS1,peptide labels and compound10 mass entry | context_only | The synthesis abstract distinguishes cyclic battacin from altered fatty-acid and linear analogues. The inspected supplement labels battacin as10 and reports exact neutral mass1029.6699; its table uses the protonated formula for [M+H]+. Most biofilm/NMR discussion concerns linear analogue17. This partial inspection does not establish absolute natural fatty-acid stereochemistry or justify transferring analogue activity. |
| aro | ARO:3003822;ARO:3000035;ARO:3009657; 148-card-current.html;148-aro-stanzas.txt;data/raw/aro_antibiotics.tsv | context_only | The adopted row and separately hashed cache reproduce the definition, sole PMID and octapeptin B5 synonym. Cache ancestry places lipopeptide antibiotics under nonribosomal peptide antibiotics. The live CARD page displays the broader peptide-antibiotic class; that presentation difference is not evidence that the retained broader class is biologically wrong. |
| aro-cache | Cached ARO ontology; Original cache /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/downloads/aro.obo;148-aro-cache-hash.json | context_only | The cache bytes were hashed before the three relevant stanzas were judged and rechecked at draft construction. |
| owners | PubChem enrichment and seeder owners; scripts/enrich_pubchem_structures.py property mapping;scripts/seed_from_sources.py structure_from_pubchem/build_concepts;data/raw/pubchem_structures.tsv | context_only | Current public structure is reproduced verbatim in the adopted row and copied by the seeder. A fresh fetch of this CID alone will retain the omitted configurations. Any maintained correction must preserve source attribution and avoid pretending a curator-modified graph is the untouched PubChem response. |
| validation | Focused native schema and strict checks; 148-strict.tsv | supports | Both focused validators passed. They establish shape/constraint consistency, not completeness of natural-product stereochemistry. |
| search | Ignored-inclusive local ownership search; 148-local-hits.txt;148-inspect.json | context_only | All 16 captured repository input hashes and separately hashed ARO cache remain unchanged. The only adopted publication lead was resolved and read as an original main article. |

## Limits And Additional Notes

- The original main article and Figure1B were read; its linked DOC supplements returned HTML browser challenges, so raw supplementary chromatograms and the detailed clinical susceptibility table were not independently verified. The main Methods/Results and Table1 remain the assignment evidence.
- The primary paper does not settle fatty-acid absolute stereochemistry. Secondary sources differ in presentation of octapeptin configurations; they were discovery leads only. No configuration was imported from them.
- The first-synthesis paper was inspected through its complete abstract and selected public supporting-information sections, not the full paywalled main text or every spectrum. This does not independently prove the natural lipid stereochemistry.
- Initial source fetches failed sandbox DNS and succeeded after permitted network retry. Original XML returned500; a guessed PDF endpoint returned a download interstitial, while the alternate PMC HTML query yielded the complete main text. The first guessed CARD URL returned500; the resolved current record URL succeeded.
- The neutral drawn graph is not a statement that the peptide remains uncharged under assay conditions. Cationic behavior and neutral parent representation are compatible.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 16 repository input hashes unchanged and external ARO cache rechecked separately; no native edits.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T101536Z-battacin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of battacin
started_at: '2026-10-21T09:46:07Z'
finished_at: '2026-10-21T10:15:36Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: PubChem graph reproduces but omits experimentally assigned amino-acid
  stereochemistry
scientific_review: true
summary: The native battacin graph agrees with current PubChem and is internally consistent,
  but three amino-acid centers remain unspecified despite the original paper’s assignments.
  Two additional unassigned fatty-acid centers need separate resolution. Antibacterial
  classification and the tentative membrane-mechanism definition have compound-specific
  primary support; optional additions require assay and material qualifiers.
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
  - path: data/antibiotics/antibacterial/battacin.yaml
    sha256: fc46eb550e926bda4d7c78dbb11165628de292bc8362e2727fd43c7f61ea20e7
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
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
scope:
  description: Whole SEEDED record and three history events; sole adopted publication,
    original main paper and structure figure; current PubChem/CARD and source-owned
    mapping; bounded follow-up synthesis abstract and selected supporting information.
  selection: Path-ordered queue index 148 prepared and hashed before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-e9c8697a8e
targets:
- target_id: antibioticmech:aro-e9c8697a8e
  path: data/antibiotics/antibacterial/battacin.yaml
  label: battacin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition and classification
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted ARO-linked PubChem identity
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extractor
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem enrichment owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion decisions
checks:
- check_id: schema
  name: Documented schema check
  status: passed
  required: true
  summary: Exit 0.
  target_ids:
  - antibioticmech:aro-e9c8697a8e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/battacin.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict check
  status: passed
  required: true
  summary: Exit 0; zero ERROR rows.
  target_ids:
  - antibioticmech:aro-e9c8697a8e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/battacin.yaml --out /private/tmp/am-review-session/148-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Native chemistry and residue mapping
  status: passed
  required: false
  summary: Exit 0; graph, formula, masses, charge, mint and live PubChem agree. The
    check reports five unassigned centers and maps the three unassigned amino-acid
    centers to the primary sequence.
  target_ids:
  - antibioticmech:aro-e9c8697a8e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/148-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
  - primary-structure
- check_id: adapter
  name: Native iModulonDB applicability
  status: not_applicable
  required: false
  summary: The record names no gene, protein target, regulator, expression module
    or specific transcriptomic response. Its chemical membrane-effect claim is not
    adjudicated by expression-module membership.
  target_ids:
  - antibioticmech:aro-e9c8697a8e
  evidence_ids:
  - record
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-e9c8697a8e
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
  - antibioticmech:aro-e9c8697a8e
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
  - antibioticmech:aro-e9c8697a8e
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
  - antibioticmech:aro-e9c8697a8e
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
  - antibioticmech:aro-e9c8697a8e
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
  - antibioticmech:aro-e9c8697a8e
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
  - antibioticmech:aro-e9c8697a8e
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
  - antibioticmech:aro-e9c8697a8e
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
  - antibioticmech:aro-e9c8697a8e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/battacin.yaml
  locator: Whole native YAML and three history events
  accessed_at: '2026-10-21T09:50:12Z'
  support: supports
  summary: ARO-minted, PubChem-seeded record has a primary-cited tentative membrane
    definition and octapeptin B5 synonym. No structured mode, target, MIC, producer,
    resistance or causal graph is asserted. History remains SEEDED with two subsequent
    reseeds.
- evidence_id: chemistry
  kind: validation
  reference: PubChem CID:177394116; native literal SMILES
  locator: 148-chemistry.py;148-chemistry.json;148-pubchem.json
  accessed_at: '2026-10-21T09:50:12Z'
  support: supports
  summary: Native SMILES/InChI and current PubChem yield GFRZMEVTBQRIMT-NUWCLZTQSA-N,
    C50H87N13O10, neutral single graph and consistent masses. Five of ten potential
    centers are unspecified. Residue mapping identifies unassigned alpha atoms18/44/24
    as positions2/3/8, respectively; assigned residues agree with the primary sequence.
    Two unassigned centers belong to the fatty acid. Atom indices are zero-based in
    the native literal SMILES.
  snapshot_sha256: 8984a9a60fdf1bcd353cebe0a495a4ebc204674f65427f4a22372f24bfbff3e0
- evidence_id: primary-structure
  kind: primary_source
  reference: PMID:22183171
  locator: DOI:10.1128/AAC.05580-11;148-primary.html/txt; stereochemical Methods,
    structure Results/Table1, visually inspected Figure1B in148-figure1.jpg
  accessed_at: '2026-10-21T09:50:12Z'
  support: refutes
  summary: Advanced Marfey and DNP analyses assign D-Dab1, L-Dab2/3/6/7, L-Leu4/8
    and D-Phe5. The proposed fatty-acid connectivity is 3-hydroxy-6-methyloctanoate;
    this paper does not assign its absolute configuration.
  snapshot_sha256: 373b72af05e0e1e1f77d5b3bb80c19d09519a91d63142c61b53d5a1977326bd0
- evidence_id: primary-biology
  kind: primary_source
  reference: PMID:22183171
  locator: 148-primary.html/txt; production/antimicrobial/membrane Methods, Tables2/3
    and Figures2–4; entire main text read
  accessed_at: '2026-10-21T09:50:12Z'
  support: partial
  summary: Fermentation of P. tianmuensis F6-B70 and purification support production.
    Agar-dilution and viable-count assays support antibacterial activity. P. aeruginosa
    ATCC27853 NPN and EDTA-assisted diSC3-5/CFU assays support membrane effects with
    the definition’s cautious inference. Lipid-A interaction remains a proposed explanation,
    not direct binding. The paper inconsistently prints E. coli ATCC35218/35318; any
    imported observation needs strain reconciliation.
  snapshot_sha256: 373b72af05e0e1e1f77d5b3bb80c19d09519a91d63142c61b53d5a1977326bd0
- evidence_id: synthesis
  kind: primary_source
  reference: PMID:25495219
  locator: DOI:10.1021/jm501084q;148-synthesis-core.json;148-synthesis-si.pdf contents,TableS1,peptide
    labels and compound10 mass entry
  accessed_at: '2026-10-21T09:50:12Z'
  support: context_only
  summary: The synthesis abstract distinguishes cyclic battacin from altered fatty-acid
    and linear analogues. The inspected supplement labels battacin as10 and reports
    exact neutral mass1029.6699; its table uses the protonated formula for [M+H]+.
    Most biofilm/NMR discussion concerns linear analogue17. This partial inspection
    does not establish absolute natural fatty-acid stereochemistry or justify transferring
    analogue activity.
  snapshot_sha256: ca0146934abb82ea2fba6ef89a3e346278781d2e4a03a52d9918ebe31b6b4017
- evidence_id: aro
  kind: database
  reference: ARO:3003822;ARO:3000035;ARO:3009657
  locator: 148-card-current.html;148-aro-stanzas.txt;data/raw/aro_antibiotics.tsv
  accessed_at: '2026-10-21T09:50:12Z'
  support: context_only
  summary: The adopted row and separately hashed cache reproduce the definition, sole
    PMID and octapeptin B5 synonym. Cache ancestry places lipopeptide antibiotics
    under nonribosomal peptide antibiotics. The live CARD page displays the broader
    peptide-antibiotic class; that presentation difference is not evidence that the
    retained broader class is biologically wrong.
  snapshot_sha256: c6690405dc387153a1c985163edb47d2d8e67dff99a89e6fafb1823116f50d37
- evidence_id: aro-cache
  kind: database
  reference: Cached ARO ontology
  locator: Original cache /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/downloads/aro.obo;148-aro-cache-hash.json
  accessed_at: '2026-10-21T09:50:12Z'
  support: context_only
  summary: The cache bytes were hashed before the three relevant stanzas were judged
    and rechecked at draft construction.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: owners
  kind: record_content
  reference: PubChem enrichment and seeder owners
  locator: scripts/enrich_pubchem_structures.py property mapping;scripts/seed_from_sources.py
    structure_from_pubchem/build_concepts;data/raw/pubchem_structures.tsv
  accessed_at: '2026-10-21T09:50:12Z'
  support: context_only
  summary: Current public structure is reproduced verbatim in the adopted row and
    copied by the seeder. A fresh fetch of this CID alone will retain the omitted
    configurations. Any maintained correction must preserve source attribution and
    avoid pretending a curator-modified graph is the untouched PubChem response.
- evidence_id: validation
  kind: validation
  reference: Focused native schema and strict checks
  locator: 148-strict.tsv
  accessed_at: '2026-10-21T09:50:12Z'
  support: supports
  summary: Both focused validators passed. They establish shape/constraint consistency,
    not completeness of natural-product stereochemistry.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local ownership search
  locator: 148-local-hits.txt;148-inspect.json
  accessed_at: '2026-10-21T09:50:12Z'
  support: context_only
  summary: All 16 captured repository input hashes and separately hashed ARO cache
    remain unchanged. The only adopted publication lead was resolved and read as an
    original main article.
  search_scope: prepare.py 148 searched identifier/label/slug with rg --no-ignore
    --hidden excluding .git/.venv. Bounded follow-up covered current PubChem/CARD,
    the original battacin paper and the cited first-synthesis work; this was not an
    exhaustive octapeptin or analogue review.
assessments:
- assessment_id: identity
  area: identity
  topic: Natural-product stereochemical completeness
  outcome: concern
  summary: The adopted database representation omits known amino-acid configurations;
    the remaining fatty-acid uncertainty must be tracked separately.
  target_ids:
  - antibioticmech:aro-e9c8697a8e
  evidence_ids:
  - chemistry
  - primary-structure
- assessment_id: grounding
  area: grounding
  topic: Mint and broader chemical class
  outcome: supported
  summary: ARO identity mint reproduces; lipopeptide/nonribosomal-peptide classification
    is broader than this entity. Antibacterial filing is primary-supported, and no
    ChEBI role is fabricated.
  target_ids:
  - antibioticmech:aro-e9c8697a8e
  evidence_ids:
  - chemistry
  - aro
  - primary-biology
- assessment_id: mechanism
  area: evidence
  topic: Tentative membrane-effect definition
  outcome: supported
  summary: The definition retains the measured-effect/inference distinction. No direct
    protein or lipid-binding claim is asserted.
  target_ids:
  - antibioticmech:aro-e9c8697a8e
  evidence_ids:
  - record
  - primary-biology
- assessment_id: provenance
  area: provenance
  topic: Adopted source, lead and history
  outcome: supported
  summary: The sole adopted paper and generated owners were checked; PubChem agreement
    is documented without equating it with complete stereo.
  target_ids:
  - antibioticmech:aro-e9c8697a8e
  evidence_ids:
  - record
  - aro
  - owners
- assessment_id: completeness
  area: completeness
  topic: Required identity versus optional assay fields
  outcome: concern
  summary: The confirmed identity omission needs correction; producer, MIC and mechanism
    additions remain optional and must retain source-specific scope.
  target_ids:
  - antibioticmech:aro-e9c8697a8e
  evidence_ids:
  - chemistry
  - primary-structure
  - primary-biology
  - synthesis
- assessment_id: validation
  area: schema
  topic: Focused gates
  outcome: supported
  summary: Schema/strict/native chemistry checks pass while the scientific identity
    concern remains.
  target_ids:
  - antibioticmech:aro-e9c8697a8e
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: aro-3003822-battacin-known-amino-acid-stereo-omitted
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Encode the experimentally assigned amino-acid stereochemistry
  description: Three amino-acid centers are unspecified in both the adopted/current
    PubChem graph and native record despite the assignments documented in primary-structure
    evidence. This is a source-level omission, not an invalid SMILES or a mismatch
    between native InChI and SMILES. The graph is less specific than the named natural
    product. Two additional unassigned fatty-acid centers require separate evidence,
    so completing the amino-acid assignments alone must not be described as complete
    absolute stereochemical resolution.
  target_ids:
  - antibioticmech:aro-e9c8697a8e
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  - chemical_structure.structure_source
  - xrefs
  - source_concepts
  evidence_ids:
  - chemistry
  - primary-structure
  - owners
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition and classification
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted ARO-linked PubChem identity
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extractor
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem enrichment owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion decisions
  rule_id: 'CLAUDE.md: record is an individual structure; review-checklist identity/structure
    gate'
  native_severity: major stereochemical identity incompleteness
  normalization_reason: Known configurations materially distinguish natural-product
    stereoisomers. Existing connectivity and encoded centers are consistent, so this
    is a major omitted-identity-information defect rather than a claim that the graph
    encodes a demonstrated wrong enantiomer.
actions:
- action_id: A1
  description: Correct the source-owned stereochemical representation and explicitly
    retain unresolved fatty-acid scope.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-e9c8697a8e
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition and classification
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted ARO-linked PubChem identity
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extractor
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem enrichment owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion decisions
  acceptance_checks:
  - Use the exact residue mapping and primary assignments in the evidence to complete
    the three omitted amino-acid centers; independently verify the cyclic sequence,
    amide closure and all resulting CIP assignments. Keep already supported centers
    and connectivity unless new primary evidence requires change.
  - Seek primary evidence for the fatty-acid stereocenters separately. Do not copy
    configurations from another octapeptin, a secondary table or a modified synthetic
    analogue. If unresolved, record a concrete discussion/limitation and withhold
    full exact-identity sign-off.
  - Correct upstream PubChem/ARO mapping or implement a documented maintained literature-backed
    structure correction path. A plain enrichment refresh of CID177394116 currently
    reintroduces the omission. Recompute all structure identifiers consistently and
    preserve truthful structure_source provenance.
  - 'Review the old same-structure PubChem xref after correction: the current partially
    specified source is not automatically an exact match to a more specific corrected
    graph. Check merges/minted identity and canary output before corpus reseeding.'
  - If optionally adding biological claims, preserve exact strain, method, concentrations
    and inference scope. Resolve the paper’s ATCC strain-number inconsistency; do
    not transfer linear-analogue biofilm potency or infer direct binding from membrane
    dyes.
  - Use the validated writer/history path for any future native mutation and pass
    required gates before scientific status promotion.
limitations:
- The original main article and Figure1B were read; its linked DOC supplements returned
  HTML browser challenges, so raw supplementary chromatograms and the detailed clinical
  susceptibility table were not independently verified. The main Methods/Results and
  Table1 remain the assignment evidence.
- The primary paper does not settle fatty-acid absolute stereochemistry. Secondary
  sources differ in presentation of octapeptin configurations; they were discovery
  leads only. No configuration was imported from them.
- The first-synthesis paper was inspected through its complete abstract and selected
  public supporting-information sections, not the full paywalled main text or every
  spectrum. This does not independently prove the natural lipid stereochemistry.
- Initial source fetches failed sandbox DNS and succeeded after permitted network
  retry. Original XML returned500; a guessed PDF endpoint returned a download interstitial,
  while the alternate PMC HTML query yielded the complete main text. The first guessed
  CARD URL returned500; the resolved current record URL succeeded.
- The neutral drawn graph is not a statement that the peptide remains uncharged under
  assay conditions. Cationic behavior and neutral parent representation are compatible.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 16 repository input hashes unchanged and external ARO cache rechecked separately;
  no native edits.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://pubchem.ncbi.nlm.nih.gov/compound/177394116
- https://card.mcmaster.ca/ontology/40513
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3294921/
- https://doi.org/10.1021/jm501084q
tags:
- record-review
- battacin
- octapeptin-b5
- stereochemical-completeness
```
