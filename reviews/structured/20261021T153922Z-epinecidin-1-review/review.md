# Review of epinecidin-1

- Review: 20261021T153922Z-epinecidin-1-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:13:48Z
- Finished UTC: 2026-10-21T15:39:22Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native graph matches an independently constructed all-L 21-residue epinecidin-1 fragment with a free amino terminus and C-terminal amide. Original experimental methods explicitly identify this material, while the fish precursor and longer synthetic fragments remain distinct. The antibacterial definition and peptide class are supported at the inspected scope. The only confirmed correction is the inherited phrase “a range or” in the definition.

## Scope And Provenance

Whole SEEDED, MINTED record: definition and sole adopted PMID, peptide parent and structural class, complete PubChem structure, two cross-references, source concept and three histories. Exact sequence/terminal chemistry, precursor relationship, original antibacterial evidence and experimental material boundaries reviewed.

Selection: Queue 404 in isolated batch 041. All 13 initial hashes preserved; three actual ARO/PubChem owner inputs appended before assessment for 16 unchanged inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-d623ec0929 | data/antibiotics/antibacterial/epinecidin-1.yaml | generated | epinecidin-1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native schema | passed | True | antibioticmech:aro-d623ec0929 | Exit 0. |
| Native strict terms | passed | True | antibioticmech:aro-d623ec0929 | Exit 0; no ERROR rows. |
| Native molecular consistency | passed | False | antibioticmech:aro-d623ec0929 | Native graph, key, formula, charge, masses and minted identifier agree. |
| Independent peptide construction and precursor mapping | passed | False | antibioticmech:aro-d623ec0929 | An independently built amidated 21-mer matches native chirality and key. The free-acid control differs. The sequence maps exactly to residues 22–42 of the 67-residue precursor. |
| Whole source and reference ledger | passed | False | antibioticmech:aro-d623ec0929 | All 16 hashes unchanged; sole adopted PMID disposed, source fields reconciled and three ordered histories checked. |
| Authoritative full QC | failed | True | antibioticmech:aro-d623ec0929 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-d623ec0929 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-d623ec0929 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-d623ec0929 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-d623ec0929 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-d623ec0929 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-d623ec0929 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-d623ec0929 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-d623ec0929 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact synthetic fragment and termini

identity: supported. Targets: antibioticmech:aro-d623ec0929.

The native represents the experimentally used amidated 21-mer; independent sequence construction and official PubChem agree.

### Fish precursor versus experimental peptide

scope: supported. Targets: antibioticmech:aro-d623ec0929.

The native derives from positions 22–42 of a 67-residue precursor; this does not make the graph the full precursor or every longer fragment.

### Antibacterial role and material scope

evidence: supported. Targets: antibioticmech:aro-d623ec0929.

Original evidence supports activity, with organism, fragment, formulation and endpoint boundaries retained.

### Membrane/host effects versus direct bacterial target

scope: supported. Targets: antibioticmech:aro-d623ec0929.

Lytic morphology and experimental host-response observations are not promoted to direct bacterial protein binding. No native target object requires repair.

### Inherited grammatical typo

nomenclature: concern. Targets: antibioticmech:aro-d623ec0929.

Replace “a range or” with “a range of” through the maintained ARO lane. This is a minor wording issue, not an identity or antibacterial-evidence defect.

### Exact original 2007 material details

evidence: unknown. Targets: antibioticmech:aro-d623ec0929.

The complete abstract was read, but exact terminal chemistry and per-fragment tables in the original body were not independently accessible. Later exact-material evidence is explicit.

### Additional susceptibility and mechanism objects

completeness: supported. Targets: antibioticmech:aro-d623ec0929.

No demonstrated missing required representation. Optional future enrichment must use exact fragment/terminal form and distinguish combinations, animal outcomes and lytic observations.

### Source and history reconciliation

ownership: supported. Targets: antibioticmech:aro-d623ec0929.

All 16 inputs, source rows, identifiers and three histories reconcile; actual ARO/PubChem owners are recorded.

## Findings

### F1: The inherited definition contains “a range or”

minor / open / confirmed; issue key: aro-3007086-definition-range-or-typo.

The native definition and current ARO source both use “a range or Gram positive and Gram negative bacteria.” The intended grammatical relation is “a range of.” This non-blocking wording error does not change the supported peptide identity or measured antibacterial activity.

## Recommended Actions And Acceptance Checks

### A1

Correct “a range or” to “a range of” upstream in ARO and refresh the maintained extraction, or implement a documented narrow source-text correction before reseeding. Preserve the exact PubChem peptide and citation. Optional wording may identify the experimental 21-residue C-terminal amide explicitly, but no forced relabeling to the full fish precursor is justified.

- Regenerated definition reads “a range of” while preserving ARO:3007086, the adopted primary citation and exact amidated graph.
- The correction survives extraction/reseeding without manual changes only to generated YAML.
- Run documented schema/strict checks and required corpus gates after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/epinecidin-1.yaml; Entire native YAML | supports | The native represents one exact neutral peptide graph, with an ARO-derived antibacterial definition and no dedicated target, resistance, MIC, producer or clinical-status objects. It does not claim that the entire fish precursor is the encoded molecule. |
| chemistry | PubChem CID49769423; independently constructed GFIFHIIKGLFHAGKMIHGLV-NH2; 404-pubchem.json;404-sequence-chemistry.json | supports | Current PubChem and both native encodings give neutral C114H176N30O21S and key IJMVGIBIGDBVLY-FIFJRYGNSA-N. Independent synthesis of the all-L sequence in RDKit, followed by explicit C-terminal amidation, matches the native graph reciprocally with chirality enabled. All 21 tetrahedral centers are specified. The otherwise identical free-acid control has a different composition/key. This verifies the exact terminal form without assuming the natural precursor itself is a 21-mer. |
| precursor | UniProtKB:Q6JWQ9; 404-uniprot-search.json exact Q6JWQ9 entry, extracted as404-uniprot-Q6JWQ9.json;404-sequence-chemistry.json | supports | The unreviewed E. coioides entry explicitly describes a 67-residue epinecidin-1 prepropeptide and cites the original cloning paper. Residues 22–42 exactly equal the native 21-mer sequence. Automated signal/chain boundaries and the amidation keyword are not treated as experimental proof of natural mature processing or of the synthetic terminal modification. |
| adopted | PMID:17570764; DOI:10.1089/dna.2006.0564; 404-core-17570764.json complete original abstract | supports | The cited original examines grouper expression/localization and tests two synthetic fragments, g-ple 22–51 and g-ple 22–42, alongside winter-flounder pleurocidin. It reports activity against Gram-positive and Gram-negative bacteria and fish infection outcomes. This supports derived-peptide antibacterial context. The 30-mer, 21-mer, gene-expression result and fish survival endpoint must remain separate; exact 2007 terminal chemistry and individual assay rows were not independently recovered because full publisher access returned 403. |
| exact-material | PMID:28177877; DOI:10.18632/oncotarget.15042; 404-PMC5400566.xml selected material, MRSA wound methods and results | supports | The original 2017 methods explicitly name amidated C-terminal Epinecidin-1 residues 22–42, GFIFHIIKGLFHAGKMIHGLV-NH2, synthesized by GL Biochemistry. Selected results measure MRSA counts and wound repair after topical treatment in heat-burned swine, alongside keratinocyte assays. These support the exact synthetic form and experimental antibacterial activity; they do not establish human approval, universal safety or direct binding to a bacterial protein. |
| sepsis | PMID:31835381; DOI:10.3390/md17120693; 404-PMC6950563.xml selected exact-material, MRSA susceptibility and pig infection methods/results | supports | The 2019 original independently specifies the same amidated 21-mer and distinguishes peptide-alone treatment from vancomycin combinations. It studies a clinical MRSA isolate in vitro and experimental pig infection. Animal efficacy, host injury markers and albumin interactions are not evidence for a particular bacterial molecular target or a clinical indication. |
| broader-panel | PMID:35052952; DOI:10.3390/antibiotics11010076; 404-PMC8773371.xml Table1, Tables2–6 and peptide/MIC/checkerboard methods | context_only | The study reports the same 21-residue sequence and measured activity against MRSA and carbapenem-resistant Gram-negative isolates, using explicit broth and checkerboard conditions. Terminal amidation is not stated in the inspected material section, so its numerical rows are not silently adopted for the exact native amide. Combination FICI and AlphaFold modeling are distinct from monotherapy MIC and experimentally determined binding. Its broad statements that resistance mechanisms do not act on AMPs are not adopted. |
| lytic | PMID:19463737; DOI:10.1016/j.peptides.2009.02.006; patent:US20100184647A1; 404-primary-search.json complete original PMID19463737 abstract;404-patent.html exact synthetic-material example and disclosure | supports | The original 2009 abstract describes the residues 22–42 fragment and measured bacterial, fungal and protozoal assays with lytic morphological evidence. The related primary patent disclosure explicitly specifies the exact 21-mer with an amidated C-terminus and cites that paper. Its broad generic claims also encompass variants and cyclic peptides; those are not exact identities for the native graph. No protein-binding mechanism or clinical efficacy is inferred. |
| aro | ARO:3007086; ARO:3000053; 404-aro-blocks.txt;374-current-aro.obo and374-fetch-results.json | supports | Current ARO resolves the exact epinecidin-1 concept, peptide-antibiotic parent, PubChem mapping and sole PMID. It repeats the native grammatical error “a range or Gram positive and Gram negative bacteria.” The broad peptide class is chemically supported; its general discussion of peptide mechanisms is not an exact target assertion. |
| owners | Maintained ARO/PubChem extraction and enrichment; 404-owner-append.json;404-raw-rows.json;404-source-audit.json | supports | The native definition and typo reproduce the maintained ARO row, while the graph reproduces adopted PubChem fields. All 16 input hashes remain unchanged, including the original 13. Three history events remain ordered and the native stays SEEDED. |
| validation | Native chemistry/schema/strict and source checks; 404-focused-results.json;404-strict.tsv;404-sequence-chemistry.log;404-ledger.log | supports | All actual focused checks and the independent sequence/terminal-form comparison pass. These establish deterministic consistency and exact material mapping separately from the literature scope. |
| access | Bounded public epinecidin-1 research; 404-local-hits.txt includes ignored files;404-fetch.json through404-fetch3.json | context_only | The adopted original complete abstract and later original open main texts were inspected at the stated levels. The adopted publisher body/PDF returned 403. The original cloning DOI resolves in structured metadata; a publisher route failed, so its full paper is not claimed as read. A bounded exact-name GSRS query returned no match, without establishing absence from every spelling or collection. |

## Limits And Additional Notes

- The adopted 2007 original was inspected at complete-abstract level; publisher body and PDF access returned 403. Its two tested fragment lengths remain distinct, and exact original per-fragment tables or terminal chemistry are not claimed as independently read.
- Selected full 2017 and 2019 material/method/result passages establish the exact amidated 21-mer and experimental MRSA contexts. Complete supplementary image inspection, human clinical efficacy and regulatory status were not assessed.
- The 2022 study reports the same sequence but does not explicitly state terminal amidation in the inspected material section. Its numerical MIC rows and combination results were not transferred automatically into the native exact-form record.
- The precursor UniProt entry is unreviewed and has automated processing annotations. Sequence mapping supports provenance, while natural mature processing and amidation require experimental evidence; the exact synthetic amide is established separately.
- The discovery cloning publication was resolved as original metadata only, not read as full text. Additional search leads are not treated as adopted native claims.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- The native contains no gene, locus, UniProt, pathway or molecular-target assertion requiring an iModulonDB adapter query. The fish precursor sequence was consulted to establish peptide material provenance, not a bacterial target or expression phenotype.
- Standalone chemistry used the batch 019 interpreter against batch 041; native validation and source ledger used batch 041.
- No native scientific status or record content was changed. The recommended correction is confined to the actual inherited wording defect.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T153922Z-epinecidin-1-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of epinecidin-1
started_at: '2026-10-21T15:13:48Z'
finished_at: '2026-10-21T15:39:22Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Whole native and maintained source rows read; independent sequence-to-graph
    construction with terminal-form control; exact official precursor mapping; adopted
    complete abstract and selected original full material/antibacterial studies inspected
    with species, treatment and assay scope preserved.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Exact synthetic 21-residue amide supported; minor inherited definition
  typo
scientific_review: true
summary: The native graph matches an independently constructed all-L 21-residue epinecidin-1
  fragment with a free amino terminus and C-terminal amide. Original experimental
  methods explicitly identify this material, while the fish precursor and longer synthetic
  fragments remain distinct. The antibacterial definition and peptide class are supported
  at the inspected scope. The only confirmed correction is the inherited phrase “a
  range or” in the definition.
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
  - path: data/antibiotics/antibacterial/epinecidin-1.yaml
    sha256: fca215e00078fa6336a8646e496d908f76a1c18fd994cf1b7d6803dee4a2e990
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
    role: context
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
  - path: data/raw/pubchem_structures.tsv
    role: context
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
  - path: scripts/enrich_pubchem_structures.py
    role: context
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
scope:
  description: 'Whole SEEDED, MINTED record: definition and sole adopted PMID, peptide
    parent and structural class, complete PubChem structure, two cross-references,
    source concept and three histories. Exact sequence/terminal chemistry, precursor
    relationship, original antibacterial evidence and experimental material boundaries
    reviewed.'
  selection: Queue 404 in isolated batch 041. All 13 initial hashes preserved; three
    actual ARO/PubChem owner inputs appended before assessment for 16 unchanged inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-d623ec0929
targets:
- target_id: antibioticmech:aro-d623ec0929
  path: data/antibiotics/antibacterial/epinecidin-1.yaml
  label: epinecidin-1
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted PubChem peptide structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained PubChem enrichment owner
checks:
- check_id: schema
  name: Native schema
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/epinecidin-1.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0.
  target_ids:
  - antibioticmech:aro-d623ec0929
  evidence_ids:
  - validation
- check_id: strict
  name: Native strict terms
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/epinecidin-1.yaml --out /private/tmp/am-review-session/404-strict.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no ERROR rows.
  target_ids:
  - antibioticmech:aro-d623ec0929
  evidence_ids:
  - validation
- check_id: native-chemistry
  name: Native molecular consistency
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    404 > /private/tmp/am-review-session/404-focused-run.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Native graph, key, formula, charge, masses and minted identifier agree.
  target_ids:
  - antibioticmech:aro-d623ec0929
  evidence_ids:
  - chemistry
  - validation
- check_id: sequence-chemistry
  name: Independent peptide construction and precursor mapping
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/404-sequence-chemistry.py
    > /private/tmp/am-review-session/404-sequence-chemistry.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: An independently built amidated 21-mer matches native chirality and key.
    The free-acid control differs. The sequence maps exactly to residues 22–42 of
    the 67-residue precursor.
  target_ids:
  - antibioticmech:aro-d623ec0929
  evidence_ids:
  - chemistry
  - precursor
- check_id: source-ledger
  name: Whole source and reference ledger
  command: .venv/bin/python /private/tmp/am-review-session/404-ledger.py > /private/tmp/am-review-session/404-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All 16 hashes unchanged; sole adopted PMID disposed, source fields reconciled
    and three ordered histories checked.
  target_ids:
  - antibioticmech:aro-d623ec0929
  evidence_ids:
  - owners
  - adopted
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-d623ec0929
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
  - antibioticmech:aro-d623ec0929
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
  - antibioticmech:aro-d623ec0929
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
  - antibioticmech:aro-d623ec0929
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
  - antibioticmech:aro-d623ec0929
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
  - antibioticmech:aro-d623ec0929
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
  - antibioticmech:aro-d623ec0929
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
  - antibioticmech:aro-d623ec0929
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
  - antibioticmech:aro-d623ec0929
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/epinecidin-1.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T15:38:26Z'
  support: supports
  summary: The native represents one exact neutral peptide graph, with an ARO-derived
    antibacterial definition and no dedicated target, resistance, MIC, producer or
    clinical-status objects. It does not claim that the entire fish precursor is the
    encoded molecule.
- evidence_id: chemistry
  kind: authority
  reference: PubChem CID49769423; independently constructed GFIFHIIKGLFHAGKMIHGLV-NH2
  locator: 404-pubchem.json;404-sequence-chemistry.json
  accessed_at: '2026-10-21T15:38:26Z'
  support: supports
  summary: Current PubChem and both native encodings give neutral C114H176N30O21S
    and key IJMVGIBIGDBVLY-FIFJRYGNSA-N. Independent synthesis of the all-L sequence
    in RDKit, followed by explicit C-terminal amidation, matches the native graph
    reciprocally with chirality enabled. All 21 tetrahedral centers are specified.
    The otherwise identical free-acid control has a different composition/key. This
    verifies the exact terminal form without assuming the natural precursor itself
    is a 21-mer.
  snapshot_sha256: ed78205bc45377df8385bad4a85993f1b4d798a68dac3078f3ed1b81cd16bffc
- evidence_id: precursor
  kind: authority
  reference: UniProtKB:Q6JWQ9
  locator: 404-uniprot-search.json exact Q6JWQ9 entry, extracted as404-uniprot-Q6JWQ9.json;404-sequence-chemistry.json
  accessed_at: '2026-10-21T15:36:01.898778Z'
  support: supports
  summary: The unreviewed E. coioides entry explicitly describes a 67-residue epinecidin-1
    prepropeptide and cites the original cloning paper. Residues 22–42 exactly equal
    the native 21-mer sequence. Automated signal/chain boundaries and the amidation
    keyword are not treated as experimental proof of natural mature processing or
    of the synthetic terminal modification.
  snapshot_sha256: 2e6ba7deefc2de4ebd9dce05c5bbc358e2f966d82aa90d1987a5d95557d017cb
- evidence_id: adopted
  kind: primary_source
  reference: PMID:17570764; DOI:10.1089/dna.2006.0564
  locator: 404-core-17570764.json complete original abstract
  accessed_at: '2026-10-21T15:35:28.983474Z'
  support: supports
  summary: The cited original examines grouper expression/localization and tests two
    synthetic fragments, g-ple 22–51 and g-ple 22–42, alongside winter-flounder pleurocidin.
    It reports activity against Gram-positive and Gram-negative bacteria and fish
    infection outcomes. This supports derived-peptide antibacterial context. The 30-mer,
    21-mer, gene-expression result and fish survival endpoint must remain separate;
    exact 2007 terminal chemistry and individual assay rows were not independently
    recovered because full publisher access returned 403.
  snapshot_sha256: 59501d411c7bc728f403d02ffe54fdd8fa9d03695175d50925cb23a0802459d8
- evidence_id: exact-material
  kind: primary_source
  reference: PMID:28177877; DOI:10.18632/oncotarget.15042
  locator: 404-PMC5400566.xml selected material, MRSA wound methods and results
  accessed_at: '2026-10-21T15:36:30.013520Z'
  support: supports
  summary: The original 2017 methods explicitly name amidated C-terminal Epinecidin-1
    residues 22–42, GFIFHIIKGLFHAGKMIHGLV-NH2, synthesized by GL Biochemistry. Selected
    results measure MRSA counts and wound repair after topical treatment in heat-burned
    swine, alongside keratinocyte assays. These support the exact synthetic form and
    experimental antibacterial activity; they do not establish human approval, universal
    safety or direct binding to a bacterial protein.
  snapshot_sha256: 0e38e43cae7127772d6953a3ef3ded7d7399c483dc05ab357261f1837032a4f1
- evidence_id: sepsis
  kind: primary_source
  reference: PMID:31835381; DOI:10.3390/md17120693
  locator: 404-PMC6950563.xml selected exact-material, MRSA susceptibility and pig
    infection methods/results
  accessed_at: '2026-10-21T15:36:30.013421Z'
  support: supports
  summary: The 2019 original independently specifies the same amidated 21-mer and
    distinguishes peptide-alone treatment from vancomycin combinations. It studies
    a clinical MRSA isolate in vitro and experimental pig infection. Animal efficacy,
    host injury markers and albumin interactions are not evidence for a particular
    bacterial molecular target or a clinical indication.
  snapshot_sha256: 3a22b8586dbd842f28737de16d6350b845d6b54ea66bab122f2e0732e63baf15
- evidence_id: broader-panel
  kind: primary_source
  reference: PMID:35052952; DOI:10.3390/antibiotics11010076
  locator: 404-PMC8773371.xml Table1, Tables2–6 and peptide/MIC/checkerboard methods
  accessed_at: '2026-10-21T15:36:30.013105Z'
  support: context_only
  summary: The study reports the same 21-residue sequence and measured activity against
    MRSA and carbapenem-resistant Gram-negative isolates, using explicit broth and
    checkerboard conditions. Terminal amidation is not stated in the inspected material
    section, so its numerical rows are not silently adopted for the exact native amide.
    Combination FICI and AlphaFold modeling are distinct from monotherapy MIC and
    experimentally determined binding. Its broad statements that resistance mechanisms
    do not act on AMPs are not adopted.
  snapshot_sha256: a92a5695d87e78410eaff58e7573642ec893fafca57d51810a6c9715483495fd
- evidence_id: lytic
  kind: primary_source
  reference: PMID:19463737; DOI:10.1016/j.peptides.2009.02.006; patent:US20100184647A1
  locator: 404-primary-search.json complete original PMID19463737 abstract;404-patent.html
    exact synthetic-material example and disclosure
  accessed_at: '2026-10-21T15:36:30.013645Z'
  support: supports
  summary: The original 2009 abstract describes the residues 22–42 fragment and measured
    bacterial, fungal and protozoal assays with lytic morphological evidence. The
    related primary patent disclosure explicitly specifies the exact 21-mer with an
    amidated C-terminus and cites that paper. Its broad generic claims also encompass
    variants and cyclic peptides; those are not exact identities for the native graph.
    No protein-binding mechanism or clinical efficacy is inferred.
  snapshot_sha256: 8f9f92368757ddf16b77c980edb3b63fc98d79441e21d0295fc0ec144e8af61a
- evidence_id: aro
  kind: authority
  reference: ARO:3007086; ARO:3000053
  locator: 404-aro-blocks.txt;374-current-aro.obo and374-fetch-results.json
  accessed_at: '2026-10-21T15:38:26Z'
  support: supports
  summary: Current ARO resolves the exact epinecidin-1 concept, peptide-antibiotic
    parent, PubChem mapping and sole PMID. It repeats the native grammatical error
    “a range or Gram positive and Gram negative bacteria.” The broad peptide class
    is chemically supported; its general discussion of peptide mechanisms is not an
    exact target assertion.
  snapshot_sha256: ae547b4a5e88771158a02d33e942ffe0b3c3d0ee2a827ce9a9c29c01ef29f0d8
- evidence_id: owners
  kind: database
  reference: Maintained ARO/PubChem extraction and enrichment
  locator: 404-owner-append.json;404-raw-rows.json;404-source-audit.json
  accessed_at: '2026-10-21T15:38:26Z'
  support: supports
  summary: The native definition and typo reproduce the maintained ARO row, while
    the graph reproduces adopted PubChem fields. All 16 input hashes remain unchanged,
    including the original 13. Three history events remain ordered and the native
    stays SEEDED.
  snapshot_sha256: 11810f84eae49460579809f1ab896ba16d3fae857e159a8f975311d3999a03ad
- evidence_id: validation
  kind: validation
  reference: Native chemistry/schema/strict and source checks
  locator: 404-focused-results.json;404-strict.tsv;404-sequence-chemistry.log;404-ledger.log
  accessed_at: '2026-10-21T15:38:26Z'
  support: supports
  summary: All actual focused checks and the independent sequence/terminal-form comparison
    pass. These establish deterministic consistency and exact material mapping separately
    from the literature scope.
  snapshot_sha256: a2736038eb5f4a2292c3025c1c0d061cc5ce2f6f1c3701572148489e9f60b49e
- evidence_id: access
  kind: search
  reference: Bounded public epinecidin-1 research
  locator: 404-local-hits.txt includes ignored files;404-fetch.json through404-fetch3.json
  accessed_at: '2026-10-21T15:38:26Z'
  support: context_only
  summary: The adopted original complete abstract and later original open main texts
    were inspected at the stated levels. The adopted publisher body/PDF returned 403.
    The original cloning DOI resolves in structured metadata; a publisher route failed,
    so its full paper is not claimed as read. A bounded exact-name GSRS query returned
    no match, without establishing absence from every spelling or collection.
  snapshot_sha256: 61a49b11fa8d99e04b82cbb2918b19c65d0b4e0c63a4a4fcb01b583523f314e3
  search_scope: 404-local-hits.txt includes ignored files;404-fetch.json through404-fetch3.json
assessments:
- assessment_id: identity
  area: identity
  topic: Exact synthetic fragment and termini
  outcome: supported
  summary: The native represents the experimentally used amidated 21-mer; independent
    sequence construction and official PubChem agree.
  target_ids:
  - antibioticmech:aro-d623ec0929
  evidence_ids:
  - chemistry
  - exact-material
  - sepsis
- assessment_id: precursor
  area: scope
  topic: Fish precursor versus experimental peptide
  outcome: supported
  summary: The native derives from positions 22–42 of a 67-residue precursor; this
    does not make the graph the full precursor or every longer fragment.
  target_ids:
  - antibioticmech:aro-d623ec0929
  evidence_ids:
  - precursor
  - adopted
  - exact-material
- assessment_id: activity
  area: evidence
  topic: Antibacterial role and material scope
  outcome: supported
  summary: Original evidence supports activity, with organism, fragment, formulation
    and endpoint boundaries retained.
  target_ids:
  - antibioticmech:aro-d623ec0929
  evidence_ids:
  - adopted
  - exact-material
  - sepsis
  - broader-panel
- assessment_id: mechanism
  area: scope
  topic: Membrane/host effects versus direct bacterial target
  outcome: supported
  summary: Lytic morphology and experimental host-response observations are not promoted
    to direct bacterial protein binding. No native target object requires repair.
  target_ids:
  - antibioticmech:aro-d623ec0929
  evidence_ids:
  - record
  - lytic
  - sepsis
- assessment_id: definition
  area: nomenclature
  topic: Inherited grammatical typo
  outcome: concern
  summary: Replace “a range or” with “a range of” through the maintained ARO lane.
    This is a minor wording issue, not an identity or antibacterial-evidence defect.
  target_ids:
  - antibioticmech:aro-d623ec0929
  evidence_ids:
  - record
  - aro
  - owners
- assessment_id: adopted-limit
  area: evidence
  topic: Exact original 2007 material details
  outcome: unknown
  summary: The complete abstract was read, but exact terminal chemistry and per-fragment
    tables in the original body were not independently accessible. Later exact-material
    evidence is explicit.
  target_ids:
  - antibioticmech:aro-d623ec0929
  evidence_ids:
  - adopted
  - exact-material
  - access
- assessment_id: completeness
  area: completeness
  topic: Additional susceptibility and mechanism objects
  outcome: supported
  summary: No demonstrated missing required representation. Optional future enrichment
    must use exact fragment/terminal form and distinguish combinations, animal outcomes
    and lytic observations.
  target_ids:
  - antibioticmech:aro-d623ec0929
  evidence_ids:
  - record
  - broader-panel
  - lytic
- assessment_id: ownership
  area: ownership
  topic: Source and history reconciliation
  outcome: supported
  summary: All 16 inputs, source rows, identifiers and three histories reconcile;
    actual ARO/PubChem owners are recorded.
  target_ids:
  - antibioticmech:aro-d623ec0929
  evidence_ids:
  - owners
  - validation
findings:
- finding_id: F1
  issue_key: aro-3007086-definition-range-or-typo
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: The inherited definition contains “a range or”
  description: The native definition and current ARO source both use “a range or Gram
    positive and Gram negative bacteria.” The intended grammatical relation is “a
    range of.” This non-blocking wording error does not change the supported peptide
    identity or measured antibacterial activity.
  target_ids:
  - antibioticmech:aro-d623ec0929
  field_paths:
  - definition
  evidence_ids:
  - record
  - aro
  - owners
  rule_id: 'review-checklist: Scientific definition accuracy and maintained source
    ownership'
  native_severity: Minor wording defect
  normalization_reason: A demonstrable typographical error affects readability; chemical
    identity and source-supported antibacterial scope remain intact.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained CARD/ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition selection
actions:
- action_id: A1
  description: Correct “a range or” to “a range of” upstream in ARO and refresh the
    maintained extraction, or implement a documented narrow source-text correction
    before reseeding. Preserve the exact PubChem peptide and citation. Optional wording
    may identify the experimental 21-residue C-terminal amide explicitly, but no forced
    relabeling to the full fish precursor is justified.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-d623ec0929
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained CARD/ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition selection
  acceptance_checks:
  - Regenerated definition reads “a range of” while preserving ARO:3007086, the adopted
    primary citation and exact amidated graph.
  - The correction survives extraction/reseeding without manual changes only to generated
    YAML.
  - Run documented schema/strict checks and required corpus gates after separately
    authorized curation.
limitations:
- The adopted 2007 original was inspected at complete-abstract level; publisher body
  and PDF access returned 403. Its two tested fragment lengths remain distinct, and
  exact original per-fragment tables or terminal chemistry are not claimed as independently
  read.
- Selected full 2017 and 2019 material/method/result passages establish the exact
  amidated 21-mer and experimental MRSA contexts. Complete supplementary image inspection,
  human clinical efficacy and regulatory status were not assessed.
- The 2022 study reports the same sequence but does not explicitly state terminal
  amidation in the inspected material section. Its numerical MIC rows and combination
  results were not transferred automatically into the native exact-form record.
- The precursor UniProt entry is unreviewed and has automated processing annotations.
  Sequence mapping supports provenance, while natural mature processing and amidation
  require experimental evidence; the exact synthetic amide is established separately.
- The discovery cloning publication was resolved as original metadata only, not read
  as full text. Additional search leads are not treated as adopted native claims.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- The native contains no gene, locus, UniProt, pathway or molecular-target assertion
  requiring an iModulonDB adapter query. The fish precursor sequence was consulted
  to establish peptide material provenance, not a bacterial target or expression phenotype.
- Standalone chemistry used the batch 019 interpreter against batch 041; native validation
  and source ledger used batch 041.
- No native scientific status or record content was changed. The recommended correction
  is confined to the actual inherited wording defect.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://pubchem.ncbi.nlm.nih.gov/compound/49769423
- https://doi.org/10.1089/dna.2006.0564
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5400566/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6950563/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8773371/
- https://patents.google.com/patent/US20100184647A1/en
tags:
- record-review
- epinecidin-1
- peptide
- synthetic-fragment
```
