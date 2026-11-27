# Review of luteolin

- Review: 20261021T200525Z-luteolin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:52:48Z
- Finished UTC: 2026-10-21T20:05:25Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The exact neutral luteolin structure, aliases and PubChem grounding agree with current authorities. The sole adopted original supports the attributed BA1 antibacterial, biofilm and envelope-injury results. Its ATP-synthesis language remains an author interpretation of an ATPase assay, and neither direct protein binding nor human efficacy is established. No confirmed native defect was identified. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire CURATOR-seeded record, both exact aliases, one PubChem xref, antibacterial role, single adopted DOI, source concept, chemistry and proposal history; exact primary methods/results and current authority comparison.

Selection: Initially uncovered queue position 613; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:curator-d604421a09 | data/antibiotics/antibacterial/luteolin.yaml | generated | Luteolin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:curator-d604421a09 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:curator-d604421a09 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:curator-d604421a09 | Actual focused execution exited 0. |
| authority-comparison | passed | False | antibioticmech:curator-d604421a09 | Actual scratch helper exited 0 against the 062 worktree. |
| source-ledger | passed | False | antibioticmech:curator-d604421a09 | Actual scratch helper exited 0 against the 062 worktree. |
| Authoritative full QC | failed | True | antibioticmech:curator-d604421a09 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:curator-d604421a09 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:curator-d604421a09 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:curator-d604421a09 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:curator-d604421a09 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:curator-d604421a09 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:curator-d604421a09 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:curator-d604421a09 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:curator-d604421a09 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral luteolin and aliases

identity: supported. Targets: antibioticmech:curator-d604421a09.

Seven independent encodings and both native aliases agree; no salt, glycoside or substituted flavone was substituted.

### Role, xref and proposed status

grounding: supported. Targets: antibioticmech:curator-d604421a09.

The asserted PubChem identity and antibacterial role resolve. The explicit MINTED/PROPOSED state is honest; optional CHEBI15864 grounding requires later authorized curation.

### Exact source assay support

evidence: supported. Targets: antibioticmech:curator-d604421a09.

The single original supports the attributed BA1 MIC/MBC, inhibition of biofilm formation and envelope-injury observations. Numerical values stay within the tested material, strain and methods.

### ATP interpretation and molecular target limits

evidence: unknown. Targets: antibioticmech:curator-d604421a09.

The paper uses ATP-synthesis wording for an ATPase endpoint. Native attribution is faithful, but direct synthesis inhibition, ATP-synthase binding and causal protein targets remain unestablished by this source.

### Adopted reference, history and maintained owner

provenance: supported. Targets: antibioticmech:curator-d604421a09.

The sole DOI resolves to the complete original; author attribution, source version, mint and proposal event are coherent. All original inputs are preserved and the actual curator owner is recorded.

### Whole-record coverage and bounded follow-up

completeness: supported. Targets: antibioticmech:curator-d604421a09.

Every native assertion and the sole adopted source were assessed. Future curation may add exact-strain structured activity and qualified assay interpretation, but optional enrichment is not a demonstrated mandatory missing representation. Broad host/docking claims are not transferred into antibacterial targets.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/luteolin.yaml; Entire native; 613-source-rows.json; preserved initial inspection and actual owner capture | supports | The PROPOSED/MINTED record has one attributed curator summary rather than separate structured MIC, mechanism, target, resistance, producer, clinical, dataset or causal-graph objects. Its maintained source is the exact curator inventory row, not the generic ChEBI extract. All thirteen original hashes remain unchanged. |
| identity | PubChem:5280445; CHEBI:15864; 613-authority-check.py and 613-authority-chemistry.json; current authority fetch manifests 613-fetch.json/613-fetch2.json | supports | Seven native, PubChem and ChEBI SMILES/InChI/molfile encodings agree by reciprocal chirality-aware graph matching on IQPNAANSBPBGFQ-UHFFFAOYSA-N, C15H10O6, charge 0 and exact mass. Both Digitoflavone and Luteolol occur in the exact PubChem synonym list. The four hydroxy-substituted flavone graph supports the definition. |
| activity | DOI:10.3390/microorganisms14020427; PMID:41753714; PMC12943306; Methods 2.1/2.3.1–2.3.3; Results 3.2.1–3.2.2, actual Figures 1 and 2, and Figure 2 caption | supports | The original uses Macklin luteolin of &gt;98% HPLC purity, CAS491-70-3, against MDR E. coli BA1. MHB with final 10^6 CFU/mL at 37 C for 24 h yields MIC 1 mg/mL and MBC 2 mg/mL; the MBC uses 100 microliter replating for 24 h. Biofilm formation decreases at 0.25 mg/mL. SEM changes and extracellular AKP support envelope injury. These are exact tested-strain observations, not an established-biofilm eradication or universal species MIC. |
| ATP | DOI:10.3390/microorganisms14020427; Methods 2.3.4; Results 3.2.3; Actual Figure 2F and caption; abstract and discussion | partial | The authors interpret treatment as suppression of ATP synthesis, as the native attributed summary reports. Their described measurement uses a Na+/K+-ATPase activity kit after 3 h and reports ATPase activity in U/mg (the plotted axis says ATP activity); it does not independently establish synthesis flux or direct ATP-synthase binding. The difference between the measured endpoint and author interpretation is retained. |
| broader | DOI:10.3390/microorganisms14020427; Full main text Methods 2.3.5–2.11, Results 3.2.4–3.7, discussion and conclusions | partial | RT-PCR changes in selected resistance/virulence genes, host cytokine assays, infection-model outcomes and docking/network predictions have distinct scopes. They do not prove direct bacterial protein binding or human therapeutic efficacy. Those stronger claims are not made by the native record, and no new target or clinical edge is required from this paper. |
| adapter | kg-microbe-sources iModulonDB; 613-source-audit.json adapter; 613-adapter-atp.txt; reused successful 606 dataset inventory | supports | Before ATP-mechanism follow-up, E. coli/precise1k query ATP synthesis exited 0 with zero genes and components; no summarize call applied. This reference dataset is not the BA1 experiment, and the miss is not evidence against an ATP-related phenotype. |
| role | CHEBI:33282; Current official ChEBI role response; 613-role.json | supports | The identifier resolves to antibacterial agent. Exact original growth-inhibition data support this role and the antibacterial folder assignment; a high MIC does not by itself negate activity classification. |
| owners | curation/curator_antibiotics.tsv; scripts/seed_from_sources.py; Exact Luteolin row and load_curator_concepts; 613-owners.py and 613-source-audit.json | supports | The seeder copies the curated identity, aliases, definition, evidence summary and version into a proposal with a stable CURATOR source mint. The source row and native summary match. Current ChEBI15864 offers an exact future grounding candidate; MINTED explicitly remains provisional and does not falsely assert an already curated exact mapping. |
| search | Local native corpus and source/decision owners; Ignored-inclusive exact-key/identifier and label/DOI searches detailed in 613-source-audit.json | supports | The searches resolved this sole exact native and its curator inventory row; current ChEBI identity is a future grounding lead. No claim of an exhaustive mechanism-literature search or absence of other luteolin activities is made. |

## Limits And Additional Notes

- The original ATP-synthesis interpretation is supported only at its reported ATPase-assay scope; ATP synthesis flux and direct ATP-synthase binding were not established.
- The primary experiments concern BA1 and the described &gt;98% luteolin material. Human clinical efficacy, general bacterial target specificity and eradication of established biofilms are not inferred.
- The downloaded supplement contains two network/drug-screening spreadsheets; only its archive listing was inspected. Raw assay data were not independently recomputed and the strain resistance panel was not reclassified. Network predictions, docking and gene-expression changes are not direct-binding evidence.
- The adapter query returned no relevant component in a different E. coli reference dataset; this does not refute the original phenotype.
- The required shared full-QC gate retains the established SciPy platform import failure. Focused schema/strict/chemistry and scratch-contract success do not replace the separately recorded shared corpus, term, reference and history gates.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All thirteen preserved initial inputs are verified unchanged; they already include the actual curator inventory and seeder, so no duplicate capture was added. Native/source/status/history files were not edited.
- Standalone chemistry used the 019 interpreter against 062; native validators, ledger and contract use 062. Direct MDPI HTML and PMC browser access were blocked, but public Europe PMC full original XML was retrieved and read.
- The source-concept snippet is an attributed curator summary. Any future mechanism annotation should distinguish the measured ATPase endpoint from the authors' broader interpretation and preserve the exact BA1 assay context.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T200525Z-luteolin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of luteolin
started_at: '2026-10-21T19:52:48Z'
finished_at: '2026-10-21T20:05:25Z'
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
verdict: blocked
scientific_review: true
summary: The exact neutral luteolin structure, aliases and PubChem grounding agree
  with current authorities. The sole adopted original supports the attributed BA1
  antibacterial, biofilm and envelope-injury results. Its ATP-synthesis language remains
  an author interpretation of an ATPase assay, and neither direct protein binding
  nor human efficacy is established. No confirmed native defect was identified. Scientific
  assessment retains the stated evidence limits; full verification is blocked by the
  shared native-library failure.
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
  - path: data/antibiotics/antibacterial/luteolin.yaml
    sha256: 6fe7525ed8e5f9b076e201f7d2b43100f93f487bf017c761ad0439b6a6da7e90
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
- target_id: antibioticmech:curator-d604421a09
  path: data/antibiotics/antibacterial/luteolin.yaml
  label: Luteolin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Exact curator identity, definition, aliases and source evidence owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: load_curator_concepts and generated CURATOR proposal
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Optional exact grounding decision
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Role and source policy context
scope:
  description: Entire CURATOR-seeded record, both exact aliases, one PubChem xref,
    antibacterial role, single adopted DOI, source concept, chemistry and proposal
    history; exact primary methods/results and current authority comparison.
  selection: Initially uncovered queue position 613; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:curator-d604421a09
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-d604421a09
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    613
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-d604421a09
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/luteolin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-d604421a09
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/luteolin.yaml --out /private/tmp/am-review-session/613-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-comparison
  name: authority-comparison
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/613-authority-check.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual scratch helper exited 0 against the 062 worktree.
  target_ids:
  - antibioticmech:curator-d604421a09
- check_id: source-ledger
  name: source-ledger
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-062/.venv/bin/python /private/tmp/am-review-session/613-ledger.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual scratch helper exited 0 against the 062 worktree.
  target_ids:
  - antibioticmech:curator-d604421a09
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:curator-d604421a09
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
  - antibioticmech:curator-d604421a09
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
  - antibioticmech:curator-d604421a09
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
  - antibioticmech:curator-d604421a09
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
  - antibioticmech:curator-d604421a09
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
  - antibioticmech:curator-d604421a09
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
  - antibioticmech:curator-d604421a09
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
  - antibioticmech:curator-d604421a09
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
  - antibioticmech:curator-d604421a09
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/luteolin.yaml
  locator: Entire native; 613-source-rows.json; preserved initial inspection and actual
    owner capture
  accessed_at: '2026-10-21T20:01:44Z'
  support: supports
  summary: The PROPOSED/MINTED record has one attributed curator summary rather than
    separate structured MIC, mechanism, target, resistance, producer, clinical, dataset
    or causal-graph objects. Its maintained source is the exact curator inventory
    row, not the generic ChEBI extract. All thirteen original hashes remain unchanged.
  snapshot_sha256: 1247a2190a0d306019cb77f95eb5c7de2545862c7b5e751ed93e905e9471bbb5
- evidence_id: identity
  kind: validation
  reference: PubChem:5280445; CHEBI:15864
  locator: 613-authority-check.py and 613-authority-chemistry.json; current authority
    fetch manifests 613-fetch.json/613-fetch2.json
  accessed_at: '2026-10-21T20:01:44Z'
  support: supports
  summary: Seven native, PubChem and ChEBI SMILES/InChI/molfile encodings agree by
    reciprocal chirality-aware graph matching on IQPNAANSBPBGFQ-UHFFFAOYSA-N, C15H10O6,
    charge 0 and exact mass. Both Digitoflavone and Luteolol occur in the exact PubChem
    synonym list. The four hydroxy-substituted flavone graph supports the definition.
  snapshot_sha256: a34e518116a68758546e6da07e50f3711440c1b49eeae74f916ff3e30062272a
- evidence_id: activity
  kind: primary_source
  reference: DOI:10.3390/microorganisms14020427
  locator: PMID:41753714; PMC12943306; Methods 2.1/2.3.1–2.3.3; Results 3.2.1–3.2.2,
    actual Figures 1 and 2, and Figure 2 caption
  accessed_at: '2026-10-21T20:01:44Z'
  support: supports
  summary: The original uses Macklin luteolin of >98% HPLC purity, CAS491-70-3, against
    MDR E. coli BA1. MHB with final 10^6 CFU/mL at 37 C for 24 h yields MIC 1 mg/mL
    and MBC 2 mg/mL; the MBC uses 100 microliter replating for 24 h. Biofilm formation
    decreases at 0.25 mg/mL. SEM changes and extracellular AKP support envelope injury.
    These are exact tested-strain observations, not an established-biofilm eradication
    or universal species MIC.
  snapshot_sha256: e83a46f994bff113e50d70e601257163c6722f7c8c4ac5cd123272b9355b53f5
- evidence_id: ATP
  kind: primary_source
  reference: DOI:10.3390/microorganisms14020427
  locator: Methods 2.3.4; Results 3.2.3; Actual Figure 2F and caption; abstract and
    discussion
  accessed_at: '2026-10-21T20:01:44Z'
  support: partial
  summary: The authors interpret treatment as suppression of ATP synthesis, as the
    native attributed summary reports. Their described measurement uses a Na+/K+-ATPase
    activity kit after 3 h and reports ATPase activity in U/mg (the plotted axis says
    ATP activity); it does not independently establish synthesis flux or direct ATP-synthase
    binding. The difference between the measured endpoint and author interpretation
    is retained.
  snapshot_sha256: e83a46f994bff113e50d70e601257163c6722f7c8c4ac5cd123272b9355b53f5
- evidence_id: broader
  kind: primary_source
  reference: DOI:10.3390/microorganisms14020427
  locator: Full main text Methods 2.3.5–2.11, Results 3.2.4–3.7, discussion and conclusions
  accessed_at: '2026-10-21T20:01:44Z'
  support: partial
  summary: RT-PCR changes in selected resistance/virulence genes, host cytokine assays,
    infection-model outcomes and docking/network predictions have distinct scopes.
    They do not prove direct bacterial protein binding or human therapeutic efficacy.
    Those stronger claims are not made by the native record, and no new target or
    clinical edge is required from this paper.
  snapshot_sha256: e83a46f994bff113e50d70e601257163c6722f7c8c4ac5cd123272b9355b53f5
- evidence_id: adapter
  kind: database
  reference: kg-microbe-sources iModulonDB
  locator: 613-source-audit.json adapter; 613-adapter-atp.txt; reused successful 606
    dataset inventory
  accessed_at: '2026-10-21T20:01:44Z'
  support: supports
  summary: Before ATP-mechanism follow-up, E. coli/precise1k query ATP synthesis exited
    0 with zero genes and components; no summarize call applied. This reference dataset
    is not the BA1 experiment, and the miss is not evidence against an ATP-related
    phenotype.
  snapshot_sha256: 41b361c288f917ff5af00f979e96d977c9cc46fab46335434a50298118effcee
- evidence_id: role
  kind: authority
  reference: CHEBI:33282
  locator: Current official ChEBI role response; 613-role.json
  accessed_at: '2026-10-21T20:01:44Z'
  support: supports
  summary: The identifier resolves to antibacterial agent. Exact original growth-inhibition
    data support this role and the antibacterial folder assignment; a high MIC does
    not by itself negate activity classification.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: owners
  kind: record_content
  reference: curation/curator_antibiotics.tsv; scripts/seed_from_sources.py
  locator: Exact Luteolin row and load_curator_concepts; 613-owners.py and 613-source-audit.json
  accessed_at: '2026-10-21T20:01:44Z'
  support: supports
  summary: The seeder copies the curated identity, aliases, definition, evidence summary
    and version into a proposal with a stable CURATOR source mint. The source row
    and native summary match. Current ChEBI15864 offers an exact future grounding
    candidate; MINTED explicitly remains provisional and does not falsely assert an
    already curated exact mapping.
  snapshot_sha256: 1247a2190a0d306019cb77f95eb5c7de2545862c7b5e751ed93e905e9471bbb5
- evidence_id: search
  kind: search
  reference: Local native corpus and source/decision owners
  locator: Ignored-inclusive exact-key/identifier and label/DOI searches detailed
    in 613-source-audit.json
  accessed_at: '2026-10-21T20:01:44Z'
  support: supports
  summary: The searches resolved this sole exact native and its curator inventory
    row; current ChEBI identity is a future grounding lead. No claim of an exhaustive
    mechanism-literature search or absence of other luteolin activities is made.
  search_scope: rg --no-ignore --hidden across data/antibiotics and curation/decisions.tsv
    for exact key/identifier/CHEBI15864, and curation/conf/scripts/data/raw for label/DOI;
    exact adopted DOI resolved and full original was read.
  snapshot_sha256: 1247a2190a0d306019cb77f95eb5c7de2545862c7b5e751ed93e905e9471bbb5
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral luteolin and aliases
  outcome: supported
  summary: Seven independent encodings and both native aliases agree; no salt, glycoside
    or substituted flavone was substituted.
  target_ids:
  - antibioticmech:curator-d604421a09
  evidence_ids:
  - identity
  - native
- assessment_id: grounding
  area: grounding
  topic: Role, xref and proposed status
  outcome: supported
  summary: The asserted PubChem identity and antibacterial role resolve. The explicit
    MINTED/PROPOSED state is honest; optional CHEBI15864 grounding requires later
    authorized curation.
  target_ids:
  - antibioticmech:curator-d604421a09
  evidence_ids:
  - identity
  - role
  - owners
- assessment_id: activity
  area: evidence
  topic: Exact source assay support
  outcome: supported
  summary: The single original supports the attributed BA1 MIC/MBC, inhibition of
    biofilm formation and envelope-injury observations. Numerical values stay within
    the tested material, strain and methods.
  target_ids:
  - antibioticmech:curator-d604421a09
  evidence_ids:
  - activity
  - native
- assessment_id: mechanism
  area: evidence
  topic: ATP interpretation and molecular target limits
  outcome: unknown
  summary: The paper uses ATP-synthesis wording for an ATPase endpoint. Native attribution
    is faithful, but direct synthesis inhibition, ATP-synthase binding and causal
    protein targets remain unestablished by this source.
  target_ids:
  - antibioticmech:curator-d604421a09
  evidence_ids:
  - ATP
  - broader
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Adopted reference, history and maintained owner
  outcome: supported
  summary: The sole DOI resolves to the complete original; author attribution, source
    version, mint and proposal event are coherent. All original inputs are preserved
    and the actual curator owner is recorded.
  target_ids:
  - antibioticmech:curator-d604421a09
  evidence_ids:
  - native
  - owners
  - activity
- assessment_id: completeness
  area: completeness
  topic: Whole-record coverage and bounded follow-up
  outcome: supported
  summary: Every native assertion and the sole adopted source were assessed. Future
    curation may add exact-strain structured activity and qualified assay interpretation,
    but optional enrichment is not a demonstrated mandatory missing representation.
    Broad host/docking claims are not transferred into antibacterial targets.
  target_ids:
  - antibioticmech:curator-d604421a09
  evidence_ids:
  - activity
  - broader
  - owners
  - search
findings: []
actions: []
limitations:
- The original ATP-synthesis interpretation is supported only at its reported ATPase-assay
  scope; ATP synthesis flux and direct ATP-synthase binding were not established.
- The primary experiments concern BA1 and the described >98% luteolin material. Human
  clinical efficacy, general bacterial target specificity and eradication of established
  biofilms are not inferred.
- The downloaded supplement contains two network/drug-screening spreadsheets; only
  its archive listing was inspected. Raw assay data were not independently recomputed
  and the strain resistance panel was not reclassified. Network predictions, docking
  and gene-expression changes are not direct-binding evidence.
- The adapter query returned no relevant component in a different E. coli reference
  dataset; this does not refute the original phenotype.
- The required shared full-QC gate retains the established SciPy platform import failure.
  Focused schema/strict/chemistry and scratch-contract success do not replace the
  separately recorded shared corpus, term, reference and history gates.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All thirteen preserved initial inputs are verified unchanged; they already include
  the actual curator inventory and seeder, so no duplicate capture was added. Native/source/status/history
  files were not edited.
- Standalone chemistry used the 019 interpreter against 062; native validators, ledger
  and contract use 062. Direct MDPI HTML and PMC browser access were blocked, but
  public Europe PMC full original XML was retrieved and read.
- The source-concept snippet is an attributed curator summary. Any future mechanism
  annotation should distinguish the measured ATPase endpoint from the authors' broader
  interpretation and preserve the exact BA1 assay context.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
