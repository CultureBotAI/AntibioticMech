# Glycyrrhizol B: corroborated purified-compound identity and antibacterial evidence

- Review: 20261021T174515Z-glycyrrhizol-b-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:27:42Z
- Finished UTC: 2026-10-21T17:45:15Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native glycyrrhizol B graph agrees with independent authorities and the original structure elucidation. The original assay distinguishes its purified-compound activity from other licorice constituents. No confirmed scientific defect was found; optional target and producer fields remain appropriately absent. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position506; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65977 | data/antibiotics/antibacterial/glycyrrhizol-b.yaml | generated | glycyrrhizol B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:65977 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:65977 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:65977 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:65977 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65977 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65977 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65977 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65977 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65977 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65977 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65977 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65977 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact individual structure, names and botanical isolation

identity: supported. Targets: CHEBI:65977.

Independent graph parsing and original compound-specific structural interpretation support the native chemical identity and isolation sentence. No missing stereochemistry is inferred for the achiral graph.

### Compatible structural parents and activity role

grounding: supported. Targets: CHEBI:65977.

All asserted parent definitions fit the actual graph. Purified-compound growth inhibition supports the antibacterial role without implying broad clinical use.

### Adopted citation scope and chronological history

provenance: supported. Targets: CHEBI:65977.

The exact maintained row and every history event were read; all adopted PMIDs were resolved with primary-versus-review/material scope preserved. Source imports and native status remain unchanged.

### Mechanism, quantitative activity, producer and external registry limits

completeness: unknown. Targets: CHEBI:65977.

The record does not invent targets, resistance, activity quantities or causal graphs. Original MIC data are available for optional curation with exact strain, material and assay context; plant isolation alone does not demonstrate de novo production. Direct Reaxys remains unverified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

If enriching B activity, use the original B-specific experiment and preserve compound boundaries.

- Use B compound2 MIC32 micrograms/mL with S. mutans ATCC25175 and the original BHI/anaerobic/16–20 h visible-growth assay.
- Do not assign A-only potency, extract lollipop outcomes or an untested molecular target to B; absence of optional objects is not a mandatory defect.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/glycyrrhizol-b.yaml; Entire native record, all names, groundings, chemical properties and chronological history | supports | The exact SEEDED ChEBI record denotes neutral C21H18O5 with full key BKLGAGSBCOUJGV-UHFFFAOYSA-N. All 3 history entries were read. No molecular target, resistance claim, quantitative activity observation, producer object or causal graph is asserted. The botanical isolation sentence is narrower than a de novo biosynthetic-producer claim. |
| owners | 506-source-rows.json; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Complete exact adopted row and applicable extraction, precedence and emission logic | supports | The native imported content reproduces the maintained ChEBI row. Its antibacterial role determines the ANTIBACTERIAL category. Original thirteen captured inputs cover the actual owners and remain unchanged; no additional owner was required. Seed/reseed history is not scientific sign-off. |
| chemistry | 051-root-authority-chemistry.json; Independent forward parsing of native and external SMILES/InChI encodings | supports | 6 encodings from native, current ChEBI and PubChem reproduce the same full key, formula and neutral charge. No tetrahedral stereocentre is present; UHFFFAOY is not evidence of missing configuration in these graphs. Focused internal formula, masses, charge and key checks also pass. |
| authorities | CHEBI:65977; CHEBI:25698; CHEBI:33853; CHEBI:38164; CHEBI:33282; Complete current compound entry and relevant official parent/role definitions | supports | Current ChEBI agrees with the native chemical graph and imported content. The individual structural-parent semantics were checked against the actual graph, not accepted solely because the current source repeats a relation. Antibacterial-agent status is assessed using exact purified-compound experiments. |
| gates | 506-focused-results.json; Actual focused schema, strict and chemistry executions | supports | All three focused commands exit 0. These checks establish internal consistency and schema conformance, not scientific correctness of every imported class or name. |
| search | 506-local-hits.txt; 051-root-fetch1.json through 051-root-fetch5.json; Ignored- and hidden-inclusive local search; bounded current-authority, adopted-PMID and primary-literature retrieval | context_only | Local searches included ignored files. Every adopted PMID was resolved and its indexed abstract read. Exact accessible originals were inspected at the depths stated below. PubMed search result lists are discovery inventories, not claims that every returned paper was read. No native gene/protein/pathway/dataset claim requires a transcriptomic-adapter query; newly encountered mechanism leads remain bounded. |
| original2006 | PMID:16441081; DOI:10.1021/np058069d; https://scispace.com/pdf/antibacterial-compounds-from-glycyrrhiza-uralensis-5auosmk8yq.pdf; All original main text via readable four-page PDF extraction, including both NMR structure assignments, isolation/Experimental and antibacterial Methods; figure pixels not inspected | supports | Authenticated G. uralensis roots (voucher GS-Jiangying-002) yielded glycyrrhizol A compound1 and B compound2 by fractionation; NMR/HRMS establish distinct pterocarpene and pyrano-fused pterocarpene structures. The purified compounds were tested against S. mutans ATCC25175 in BHI at37 degrees C under anaerobic gas. Equal50-microlitre volumes of compound dilution and10^6 CFU/mL inoculum were combined, then incubated16–20 h; MIC was the lowest concentration without visible growth. A had MIC1 and B32 micrograms/mL. This establishes antibacterial activity and plant isolation, not molecular target, clinical anticaries efficacy or de novo biosynthetic producer status. |
| exact-class | CHEBI:25698; CHEBI:33853; CHEBI:38164; Official parent definitions/wildcard structure assessed against the exact native graph | supports | Native B has five fused heterocyclic/carbocyclic rings, a phenolic hydroxy group and methoxy ether. Phenols, aromatic ether and organic heteropentacyclic compound are compatible broader classes. Its ring-closed B constitution is distinct from the more highly prenylated A. |
| links | reaxys:18589783; Current exact ChEBI/PubChem structure corroboration; direct Reaxys not inspected | supports | The Reaxys identifier remains an attributed source cross-reference without direct registry verification. No document cross-reference, unsupported synonym or additional exact authority equivalence is asserted. |
| adopted | PMID:16441081; Complete sole adopted indexed abstract; original main text additionally read | supports | The sole adopted citation explicitly distinguishes the two new compounds and qualitatively describes B as less active than A. The original main text provides B-specific MIC32 micrograms/mL. No A-only extract or clinical evidence is assigned to B. |

## Limits And Additional Notes

- Original2006 main text and all chemical/antibacterial Methods were read via a readable public PDF rendering. ACS direct access and direct download of the alternate PDF failed; figure pixels and raw spectra were not inspected. Available text includes full compound-specific NMR/HRMS interpretation, which is not a claim of independent spectrum reanalysis.
- Direct Reaxys was not accessed; current ChEBI and independent PubChem graphs corroborate molecular identity but do not certify the proprietary registry record. No paid research was used.
- No antibacterial molecular target or de novo plant biosynthetic pathway was established in this bounded review. Missing optional target/graph/producer fields are not automatically errors.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T174515Z-glycyrrhizol-b-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Glycyrrhizol B: corroborated purified-compound identity and antibacterial
  evidence'
started_at: '2026-10-21T17:27:42Z'
finished_at: '2026-10-21T17:45:15Z'
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
summary: The native glycyrrhizol B graph agrees with independent authorities and the
  original structure elucidation. The original assay distinguishes its purified-compound
  activity from other licorice constituents. No confirmed scientific defect was found;
  optional target and producer fields remain appropriately absent. Scientific assessment
  retains the stated evidence limits; full verification is blocked by the shared native-library
  failure.
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
  - path: data/antibiotics/antibacterial/glycyrrhizol-b.yaml
    sha256: 22eeff098339cece62a785c0284d7d35b4912ca9bda0122bd90a804bfd96ea1e
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
- target_id: CHEBI:65977
  path: data/antibiotics/antibacterial/glycyrrhizol-b.yaml
  label: glycyrrhizol B
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
  selection: Initially uncovered queue position506; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65977
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65977
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    506
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65977
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/glycyrrhizol-b.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65977
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/glycyrrhizol-b.yaml --out /private/tmp/am-review-session/506-strict.tsv
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
  - CHEBI:65977
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
  - CHEBI:65977
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
  - CHEBI:65977
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
  - CHEBI:65977
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
  - CHEBI:65977
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
  - CHEBI:65977
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
  - CHEBI:65977
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
  - CHEBI:65977
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
  - CHEBI:65977
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/glycyrrhizol-b.yaml
  locator: Entire native record, all names, groundings, chemical properties and chronological
    history
  accessed_at: '2026-10-21T17:38:49Z'
  support: supports
  summary: The exact SEEDED ChEBI record denotes neutral C21H18O5 with full key BKLGAGSBCOUJGV-UHFFFAOYSA-N.
    All 3 history entries were read. No molecular target, resistance claim, quantitative
    activity observation, producer object or causal graph is asserted. The botanical
    isolation sentence is narrower than a de novo biosynthetic-producer claim.
- evidence_id: owners
  kind: record_content
  reference: 506-source-rows.json; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Complete exact adopted row and applicable extraction, precedence and emission
    logic
  accessed_at: '2026-10-21T17:38:49Z'
  support: supports
  summary: The native imported content reproduces the maintained ChEBI row. Its antibacterial
    role determines the ANTIBACTERIAL category. Original thirteen captured inputs
    cover the actual owners and remain unchanged; no additional owner was required.
    Seed/reseed history is not scientific sign-off.
  snapshot_sha256: a95d441b6d13e6acd9ae2fa2be9ddb72007880c061fab10e9f86ef7db2965cd4
- evidence_id: chemistry
  kind: validation
  reference: 051-root-authority-chemistry.json
  locator: Independent forward parsing of native and external SMILES/InChI encodings
  accessed_at: '2026-10-21T17:38:49Z'
  support: supports
  summary: 6 encodings from native, current ChEBI and PubChem reproduce the same full
    key, formula and neutral charge. No tetrahedral stereocentre is present; UHFFFAOY
    is not evidence of missing configuration in these graphs. Focused internal formula,
    masses, charge and key checks also pass.
  snapshot_sha256: b5dad6916ddb9942a19121928dfc22f54a2f0408f81ab485447441ae1882a8bb
- evidence_id: authorities
  kind: authority
  reference: CHEBI:65977; CHEBI:25698; CHEBI:33853; CHEBI:38164; CHEBI:33282
  locator: Complete current compound entry and relevant official parent/role definitions
  accessed_at: '2026-10-21T17:38:49Z'
  support: supports
  summary: Current ChEBI agrees with the native chemical graph and imported content.
    The individual structural-parent semantics were checked against the actual graph,
    not accepted solely because the current source repeats a relation. Antibacterial-agent
    status is assessed using exact purified-compound experiments.
  snapshot_sha256: 6e9da1867d9058d0fa4eb870333e26bbede770ba3826fd3509e04ae2d59aff0e
- evidence_id: gates
  kind: validation
  reference: 506-focused-results.json
  locator: Actual focused schema, strict and chemistry executions
  accessed_at: '2026-10-21T17:38:49Z'
  support: supports
  summary: All three focused commands exit 0. These checks establish internal consistency
    and schema conformance, not scientific correctness of every imported class or
    name.
  snapshot_sha256: eaba902da096556e7ca29e9e20cb665b08938e9d9e274b36e323850d5014db2a
- evidence_id: search
  kind: search
  reference: 506-local-hits.txt; 051-root-fetch1.json through 051-root-fetch5.json
  locator: Ignored- and hidden-inclusive local search; bounded current-authority,
    adopted-PMID and primary-literature retrieval
  accessed_at: '2026-10-21T17:38:49Z'
  support: context_only
  summary: Local searches included ignored files. Every adopted PMID was resolved
    and its indexed abstract read. Exact accessible originals were inspected at the
    depths stated below. PubMed search result lists are discovery inventories, not
    claims that every returned paper was read. No native gene/protein/pathway/dataset
    claim requires a transcriptomic-adapter query; newly encountered mechanism leads
    remain bounded.
  search_scope: 2026-10-21; own051 worktree rg --no-ignore --hidden; exact glycyrrhizol
    B and ChEBI identifiers, all adopted PMIDs, EuropePMC name search, official ChEBI/PubChem
    and linked source pages.
  snapshot_sha256: c4d5096c2ed160b775d12dceb9aa81506e4ab19f31e5e7788b95a65a9d299f0e
- evidence_id: original2006
  kind: primary_source
  reference: PMID:16441081; DOI:10.1021/np058069d; https://scispace.com/pdf/antibacterial-compounds-from-glycyrrhiza-uralensis-5auosmk8yq.pdf
  locator: All original main text via readable four-page PDF extraction, including
    both NMR structure assignments, isolation/Experimental and antibacterial Methods;
    figure pixels not inspected
  accessed_at: '2026-10-21T17:38:49Z'
  support: supports
  summary: Authenticated G. uralensis roots (voucher GS-Jiangying-002) yielded glycyrrhizol
    A compound1 and B compound2 by fractionation; NMR/HRMS establish distinct pterocarpene
    and pyrano-fused pterocarpene structures. The purified compounds were tested against
    S. mutans ATCC25175 in BHI at37 degrees C under anaerobic gas. Equal50-microlitre
    volumes of compound dilution and10^6 CFU/mL inoculum were combined, then incubated16–20
    h; MIC was the lowest concentration without visible growth. A had MIC1 and B32
    micrograms/mL. This establishes antibacterial activity and plant isolation, not
    molecular target, clinical anticaries efficacy or de novo biosynthetic producer
    status.
  snapshot_sha256: 06d5d0a346ec59d8b6e2fe69b6221a940673eb048fc2bb4975a309d59d06d6c4
- evidence_id: exact-class
  kind: authority
  reference: CHEBI:25698; CHEBI:33853; CHEBI:38164
  locator: Official parent definitions/wildcard structure assessed against the exact
    native graph
  accessed_at: '2026-10-21T17:38:49Z'
  support: supports
  summary: Native B has five fused heterocyclic/carbocyclic rings, a phenolic hydroxy
    group and methoxy ether. Phenols, aromatic ether and organic heteropentacyclic
    compound are compatible broader classes. Its ring-closed B constitution is distinct
    from the more highly prenylated A.
  snapshot_sha256: 3a6c0608c2e82831f273ba19a8e16944d1162c8e398ad697af51ab51c4a0ec87
- evidence_id: links
  kind: authority
  reference: reaxys:18589783
  locator: Current exact ChEBI/PubChem structure corroboration; direct Reaxys not
    inspected
  accessed_at: '2026-10-21T17:38:49Z'
  support: supports
  summary: The Reaxys identifier remains an attributed source cross-reference without
    direct registry verification. No document cross-reference, unsupported synonym
    or additional exact authority equivalence is asserted.
  snapshot_sha256: 49c62e4678783f0bcf25941a379305f55e0b0f4a6ca989582ebcdad7cf54fcba
- evidence_id: adopted
  kind: database
  reference: PMID:16441081
  locator: Complete sole adopted indexed abstract; original main text additionally
    read
  accessed_at: '2026-10-21T17:38:49Z'
  support: supports
  summary: The sole adopted citation explicitly distinguishes the two new compounds
    and qualitatively describes B as less active than A. The original main text provides
    B-specific MIC32 micrograms/mL. No A-only extract or clinical evidence is assigned
    to B.
  snapshot_sha256: abbeac80d6a7ac0ea81c9f7865c8387cf2e0be9060a4f905c5331707d9b95650
assessments:
- assessment_id: identity
  area: identity
  topic: Exact individual structure, names and botanical isolation
  outcome: supported
  summary: Independent graph parsing and original compound-specific structural interpretation
    support the native chemical identity and isolation sentence. No missing stereochemistry
    is inferred for the achiral graph.
  target_ids:
  - CHEBI:65977
  evidence_ids:
  - native
  - chemistry
  - original2006
  - authorities
- assessment_id: classes
  area: grounding
  topic: Compatible structural parents and activity role
  outcome: supported
  summary: All asserted parent definitions fit the actual graph. Purified-compound
    growth inhibition supports the antibacterial role without implying broad clinical
    use.
  target_ids:
  - CHEBI:65977
  evidence_ids:
  - exact-class
  - original2006
  - gates
- assessment_id: provenance
  area: provenance
  topic: Adopted citation scope and chronological history
  outcome: supported
  summary: The exact maintained row and every history event were read; all adopted
    PMIDs were resolved with primary-versus-review/material scope preserved. Source
    imports and native status remain unchanged.
  target_ids:
  - CHEBI:65977
  evidence_ids:
  - native
  - owners
  - adopted
- assessment_id: optional
  area: completeness
  topic: Mechanism, quantitative activity, producer and external registry limits
  outcome: unknown
  summary: The record does not invent targets, resistance, activity quantities or
    causal graphs. Original MIC data are available for optional curation with exact
    strain, material and assay context; plant isolation alone does not demonstrate
    de novo production. Direct Reaxys remains unverified.
  target_ids:
  - CHEBI:65977
  evidence_ids:
  - original2006
  - links
  - search
findings: []
actions:
- action_id: A1
  description: If enriching B activity, use the original B-specific experiment and
    preserve compound boundaries.
  finding_ids: []
  target_ids:
  - CHEBI:65977
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/glycyrrhizol-b.yaml
    role: Optional curator-owned activity evidence
  acceptance_checks:
  - Use B compound2 MIC32 micrograms/mL with S. mutans ATCC25175 and the original
    BHI/anaerobic/16–20 h visible-growth assay.
  - Do not assign A-only potency, extract lollipop outcomes or an untested molecular
    target to B; absence of optional objects is not a mandatory defect.
limitations:
- Original2006 main text and all chemical/antibacterial Methods were read via a readable
  public PDF rendering. ACS direct access and direct download of the alternate PDF
  failed; figure pixels and raw spectra were not inspected. Available text includes
  full compound-specific NMR/HRMS interpretation, which is not a claim of independent
  spectrum reanalysis.
- Direct Reaxys was not accessed; current ChEBI and independent PubChem graphs corroborate
  molecular identity but do not certify the proprietary registry record. No paid research
  was used.
- No antibacterial molecular target or de novo plant biosynthetic pathway was established
  in this bounded review. Missing optional target/graph/producer fields are not automatically
  errors.
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
