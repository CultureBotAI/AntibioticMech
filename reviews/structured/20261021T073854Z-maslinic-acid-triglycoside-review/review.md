# Maslinic acid triglycoside: exact structure and primary activity scope

- Review: 20261021T073854Z-maslinic-acid-triglycoside-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:25:47Z
- Finished UTC: 2026-10-21T07:38:54Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact maslinic acid triglycoside is structurally consistent with its source. One major finding concerns the unqualified antibacterial definition and source role: the adopted primary paper does not establish activity for this isolated saponin. Its negative result under the tested conditions must remain distinct from active fractions and free-aglycone assays. This is not proof of universal inactivity.

## Scope And Provenance

Whole exact record, source provenance and identity, all asserted ontology/registry groundings, cited primary compound mapping and antibacterial experimental scope.

Selection: Initially uncovered queue position037; batch004 target7 in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:68377 | data/antibiotics/antibacterial/3-o-β-d-glucopyranosyl-28-o-α-l-rhamnopyranosyl-12-β-d-glucopyranosyl-.yaml | generated | 3-O-[β-D-glucopyranosyl]-28-O-[α-L-rhamnopyranosyl-(1→2)-β-D-glucopyranosyl]maslinic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema validation | passed | True | CHEBI:68377 | Corrected task-local-cache invocation exited0 with no validation errors. |
| Documented strict validation | passed | True | CHEBI:68377 | Corrected task-local-cache invocation exited0 with no validation errors. |
| Independent chemical and minted identity consistency | passed | False | CHEBI:68377 | Both encodings and all identity assertions agree. |
| Structured adapter applicability | not_applicable | False | CHEBI:68377 | The native record names no gene, protein, regulator, pathway, stress response or transcriptomic dataset. |
| Authoritative full QC | failed | True | CHEBI:68377 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:68377 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:68377 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:68377 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:68377 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:68377 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:68377 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:68377 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:68377 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact glycoside and chemical representation

identity: supported. Targets: CHEBI:68377.

Native encodings, source authority and compound-specific paper assignment are coherent. The free aglycone, neighbouring oxygenation variant and other sugar sequences are separate entities.

### Broader parents and registry assertion

grounding: supported. Targets: CHEBI:68377.

The two chemical parents are broader classes. Registry equivalence is authority-corroborated with an explicit independent-access limit.

### Unqualified antibacterial wording and role

evidence: concern. Targets: CHEBI:68377.

The imported classification is faithfully reproduced, but the detailed source experiment does not support the attributed positive activity. The claim needs adjudication at its maintained source owner.

### Plant source and producer scope

provenance: supported. Targets: CHEBI:68377.

Leaf isolation is supported. No native biosynthesizing-producer claim is asserted or inferred merely from extraction.

### Mode of action and target

completeness: unknown. Targets: CHEBI:68377.

No mechanism or direct target is asserted or established for this exact glycoside. Its chemical family does not supply a causal mechanism.

### Other optional objects

representation: not_applicable. Targets: CHEBI:68377.

No false resistance, clinical, graph, dataset or quantitative assay claim is present. Empty optional fields do not independently warrant defects.

### Maintained provenance and native status

ownership: supported. Targets: CHEBI:68377.

Source concept and curation events reproduce the inventory. Scientific sign-off remains separate from a saved review; native SEEDED is retained.

## Findings

### F1: The adopted experiment does not support the isolated-saponin activity claim

major / open / confirmed; issue key: chebi-68377-saponin-activity-source-scope.

The unqualified antibacterial sentence and role need source adjudication. Positive mixture, fraction or parent-aglycone observations cannot establish activity of this exact conjugate; preserve the inspected negative endpoint and its limits. This does not declare the compound universally inactive or authorize deleting it without the maintained inclusion process.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate the positive activity attribution against the full primary experiment and any independently supported exact-compound study. Correct or qualify the maintained source definition/role and resulting inclusion decision, preserving exact chemical identity and evidence provenance.

- The maintained disposition explicitly distinguishes this glycoside from fractions, mixtures, free aglycones and other sugar conjugates.
- Retain the negative assay as condition-limited evidence; do not turn it into a claim of universal inactivity, a resistance phenotype or a numerical MIC.
- Any retained positive antibacterial statement identifies an inspected exact-compound experiment. If none supports retention, use the documented maintained decision/extraction/seeding process rather than a generated-YAML-only deletion or role patch.
- Any source or inclusion correction reproduces deterministically and passes focused schema/strict, corpus reproduction and fullQC. Preserve supported chemical identity and source-concept provenance.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/3-o-β-d-glucopyranosyl-28-o-α-l-rhamnopyranosyl-12-β-d-glucopyranosyl-.yaml; Every field of native YAML | supports | Read exact definition and synonym, two parent classes, antibacterial role, all chemical fields, registry xref, source concept and three seed/reseed events. No mechanism, target, quantitative activity, resistance, producer, clinical, graph or dataset object is asserted; SEEDED and EXACT are unchanged. |
| owner | data/raw/chebi_antimicrobials.tsv; Complete CHEBI:68377 row, source manifest/configuration, extractor and seeder | supports | The native identity and unqualified activity wording faithfully reproduce the adopted ChEBI row. Its only publication lead is PMID21288041; mechanism_role_ids is empty. Exact ID/minted-ID searches including ignored files in maintained curation tables and conf found no override. Source-owned role/definition corrections must reproduce upstream rather than as a YAML-only edit. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:68377; Entire official visible entry;037-chebi.html | supports | Official identity agrees on the maslinic acid conjugate, its sugar substitutions, structural encodings and registry assertion. The broader parents are pentacyclic triterpenoid CHEBI25872 and triterpenoid saponin CHEBI61778; antibacterial agent CHEBI33282 is an asserted role. The functional-parent aglycone is chemically distinct from this glycoside. Authority agreement confirms source reproduction, not experimental activity. |
| chemistry | RDKit and hashlib independent recomputation; 037-chemistry.py;037-chemistry.json | supports | Both encodings agree on IKQKYNWOONQHQK-DVSNLDMXSA-N, C48H78O18, net charge0, one fragment and 24 assigned stereocentres. Average and exact masses match the native values within their recorded precision; the minted source ID is reproduced. The neighbouring arjunolic glycoside has a different oxygen count and key, so similar filename stems do not make these duplicates. |
| primary | DOI:10.1021/np100502y; PMID21288041; author-deposited full primary text https://www.researchgate.net/publication/49804721_Triterpenoid_Saponins_from_Symplocos_lancifolia ; pp164–165 compound1, p166 activity, pp167–168 Table3/methods | refutes | Compound1 is the exact maslinic acid glycoside. Purified saponins1–3 produced no inhibition zones against E.faecalis ATCC29212 in TLC bioautography at10/50/100µg per spot. Active fractions and free-aglycone MICs are separate results. The text supports leaf isolation and structure assignment, not the unqualified activity attribution. |
| metadata | Europe PMC core API; 036-epmc.json; complete adopted publication abstract and metadata | context_only | The abstract names three glycosides and reports that several isolated triterpenoids were active. It does not assign that activity to every isolate. Detailed full-paper results therefore govern compound-specific interpretation. |
| search | Ignored-inclusive local search and bounded exact-structure public discovery; 037-local-hits.txt; exact-key and glycoside-name searches | context_only | The inspected primary source conflicts with a straightforward assignment of its positive activity to this isolated glycoside. Database repetitions do not provide an independent experiment; related saponins with different sugars and free aglycones remain distinct. Independent second-agent exact-name/key searches corroborated the bounded result. |

## Limits And Additional Notes

- The original paper was inspected through its freely author-deposited full text on ResearchGate, including structural assignment, Results, Table3 and Experimental sections. Direct HTML/PDF retrieval failed; no visual inspection of structure drawings or fresh numerical NMR reanalysis is claimed.
- Reaxys was corroborated as an official ChEBI source assertion rather than through independent paid-registry access.
- The observed lack of inhibition applies to the reported assay conditions. Bounded discovery did not locate an independent exact-saponin positive experiment; it does not establish global inactivity or absence of all later evidence.
- Initial focused validation invocation omitted the task-local uv cache and failed before validation because the default cache path was sandbox-inaccessible. The corrected documented invocation with UV_NO_SYNC=1 and the permitted task cache passed both focused gates.
- No native record was edited, no paid provider was used and no external issue or author contact occurred.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T073854Z-maslinic-acid-triglycoside-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Maslinic acid triglycoside: exact structure and primary activity scope'
started_at: '2026-10-21T07:25:47Z'
finished_at: '2026-10-21T07:38:54Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the target. Entire record, maintained
    ownership and official authority were inspected; source-paper identity and assay
    scope were read and native chemistry independently recomputed. An independent
    second agent checked the exact primary compound mapping and negative assay scope
    before finalization.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'The exact maslinic acid triglycoside is structurally consistent with its
  source. One major finding concerns the unqualified antibacterial definition and
  source role: the adopted primary paper does not establish activity for this isolated
  saponin. Its negative result under the tested conditions must remain distinct from
  active fractions and free-aglycone assays. This is not proof of universal inactivity.'
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
  - path: data/antibiotics/antibacterial/3-o-β-d-glucopyranosyl-28-o-α-l-rhamnopyranosyl-12-β-d-glucopyranosyl-.yaml
    sha256: 57a4410a0cd90e9ac483fd5764118dea6b98647fedd54ff8a790121e95bbf9d0
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
- target_id: CHEBI:68377
  path: data/antibiotics/antibacterial/3-o-β-d-glucopyranosyl-28-o-α-l-rhamnopyranosyl-12-β-d-glucopyranosyl-.yaml
  label: 3-O-[β-D-glucopyranosyl]-28-O-[α-L-rhamnopyranosyl-(1→2)-β-D-glucopyranosyl]maslinic
    acid
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
  description: Whole exact record, source provenance and identity, all asserted ontology/registry
    groundings, cited primary compound mapping and antibacterial experimental scope.
  selection: Initially uncovered queue position037; batch004 target7 in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:68377
checks:
- check_id: schema
  name: Documented schema validation
  status: passed
  required: true
  summary: Corrected task-local-cache invocation exited0 with no validation errors.
  target_ids:
  - CHEBI:68377
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/3-o-β-d-glucopyranosyl-28-o-α-l-rhamnopyranosyl-12-β-d-glucopyranosyl-.yaml
  exit_code: 0
- check_id: strict
  name: Documented strict validation
  status: passed
  required: true
  summary: Corrected task-local-cache invocation exited0 with no validation errors.
  target_ids:
  - CHEBI:68377
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/3-o-β-d-glucopyranosyl-28-o-α-l-rhamnopyranosyl-12-β-d-glucopyranosyl-.yaml
    --out /private/tmp/am-review-session/037-strict.tsv
  exit_code: 0
- check_id: chemistry
  name: Independent chemical and minted identity consistency
  status: passed
  required: false
  summary: Both encodings and all identity assertions agree.
  target_ids:
  - CHEBI:68377
  command: .venv/bin/python /private/tmp/am-review-session/037-chemistry.py
  exit_code: 0
  evidence_ids:
  - chemistry
- check_id: imodulondb
  name: Structured adapter applicability
  status: not_applicable
  required: false
  summary: The native record names no gene, protein, regulator, pathway, stress response
    or transcriptomic dataset.
  target_ids:
  - CHEBI:68377
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
  - CHEBI:68377
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
  - CHEBI:68377
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
  - CHEBI:68377
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
  - CHEBI:68377
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
  - CHEBI:68377
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
  - CHEBI:68377
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
  - CHEBI:68377
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
  - CHEBI:68377
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
  - CHEBI:68377
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/3-o-β-d-glucopyranosyl-28-o-α-l-rhamnopyranosyl-12-β-d-glucopyranosyl-.yaml
  locator: Every field of native YAML
  accessed_at: '2026-10-21T07:31:37Z'
  support: supports
  summary: Read exact definition and synonym, two parent classes, antibacterial role,
    all chemical fields, registry xref, source concept and three seed/reseed events.
    No mechanism, target, quantitative activity, resistance, producer, clinical, graph
    or dataset object is asserted; SEEDED and EXACT are unchanged.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Complete CHEBI:68377 row, source manifest/configuration, extractor and
    seeder
  accessed_at: '2026-10-21T07:31:37Z'
  support: supports
  summary: The native identity and unqualified activity wording faithfully reproduce
    the adopted ChEBI row. Its only publication lead is PMID21288041; mechanism_role_ids
    is empty. Exact ID/minted-ID searches including ignored files in maintained curation
    tables and conf found no override. Source-owned role/definition corrections must
    reproduce upstream rather than as a YAML-only edit.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:68377
  locator: Entire official visible entry;037-chebi.html
  accessed_at: '2026-10-21T07:31:37Z'
  support: supports
  summary: Official identity agrees on the maslinic acid conjugate, its sugar substitutions,
    structural encodings and registry assertion. The broader parents are pentacyclic
    triterpenoid CHEBI25872 and triterpenoid saponin CHEBI61778; antibacterial agent
    CHEBI33282 is an asserted role. The functional-parent aglycone is chemically distinct
    from this glycoside. Authority agreement confirms source reproduction, not experimental
    activity.
  snapshot_sha256: 2143265882766c48a7125108fa8fb37b9a5fae66e90b8581f98c6728b631b9df
- evidence_id: chemistry
  kind: validation
  reference: RDKit and hashlib independent recomputation
  locator: 037-chemistry.py;037-chemistry.json
  accessed_at: '2026-10-21T07:31:37Z'
  support: supports
  summary: Both encodings agree on IKQKYNWOONQHQK-DVSNLDMXSA-N, C48H78O18, net charge0,
    one fragment and 24 assigned stereocentres. Average and exact masses match the
    native values within their recorded precision; the minted source ID is reproduced.
    The neighbouring arjunolic glycoside has a different oxygen count and key, so
    similar filename stems do not make these duplicates.
  snapshot_sha256: bb3b38869d9bba87342e751851ee2bde02db8a113710cffc77a3cd09ab92cbb3
- evidence_id: primary
  kind: primary_source
  reference: DOI:10.1021/np100502y
  locator: PMID21288041; author-deposited full primary text https://www.researchgate.net/publication/49804721_Triterpenoid_Saponins_from_Symplocos_lancifolia
    ; pp164–165 compound1, p166 activity, pp167–168 Table3/methods
  accessed_at: '2026-10-21T07:31:37Z'
  support: refutes
  summary: Compound1 is the exact maslinic acid glycoside. Purified saponins1–3 produced
    no inhibition zones against E.faecalis ATCC29212 in TLC bioautography at10/50/100µg
    per spot. Active fractions and free-aglycone MICs are separate results. The text
    supports leaf isolation and structure assignment, not the unqualified activity
    attribution.
- evidence_id: metadata
  kind: database
  reference: Europe PMC core API
  locator: 036-epmc.json; complete adopted publication abstract and metadata
  accessed_at: '2026-10-21T07:31:37Z'
  support: context_only
  summary: The abstract names three glycosides and reports that several isolated triterpenoids
    were active. It does not assign that activity to every isolate. Detailed full-paper
    results therefore govern compound-specific interpretation.
  snapshot_sha256: 811e970f0efbcdc5a8a3d71c9e0bf63f5f5e3cb0e207c1017f975a74d49104ce
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local search and bounded exact-structure public discovery
  locator: 037-local-hits.txt; exact-key and glycoside-name searches
  accessed_at: '2026-10-21T07:31:37Z'
  support: context_only
  summary: The inspected primary source conflicts with a straightforward assignment
    of its positive activity to this isolated glycoside. Database repetitions do not
    provide an independent experiment; related saponins with different sugars and
    free aglycones remain distinct. Independent second-agent exact-name/key searches
    corroborated the bounded result.
  search_scope: prepare.py37 used rg --no-ignore --hidden over batch004 excluding
    .git/.venv. Focused CHEBI68377/68378 and minted IDs covered curation/decisions.tsv,
    curation/curator_antibiotics.tsv and conf with no override. Free searches used
    both full InChIKeys, glucopyranosyl/rhamnopyranosyl plus maslinic, antibacterial
    and Symplocos lancifolia. Adopted primary full text and official ChEBI were inspected;
    database summaries, review/thesis hits and different glycosides were not substituted
    as exact primary evidence.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact glycoside and chemical representation
  outcome: supported
  summary: Native encodings, source authority and compound-specific paper assignment
    are coherent. The free aglycone, neighbouring oxygenation variant and other sugar
    sequences are separate entities.
  target_ids:
  - CHEBI:68377
  evidence_ids:
  - record
  - chebi
  - chemistry
  - primary
- assessment_id: parents
  area: grounding
  topic: Broader parents and registry assertion
  outcome: supported
  summary: The two chemical parents are broader classes. Registry equivalence is authority-corroborated
    with an explicit independent-access limit.
  target_ids:
  - CHEBI:68377
  evidence_ids:
  - record
  - chebi
- assessment_id: activity
  area: evidence
  topic: Unqualified antibacterial wording and role
  outcome: concern
  summary: The imported classification is faithfully reproduced, but the detailed
    source experiment does not support the attributed positive activity. The claim
    needs adjudication at its maintained source owner.
  target_ids:
  - CHEBI:68377
  evidence_ids:
  - record
  - owner
  - chebi
  - primary
- assessment_id: isolation
  area: provenance
  topic: Plant source and producer scope
  outcome: supported
  summary: Leaf isolation is supported. No native biosynthesizing-producer claim is
    asserted or inferred merely from extraction.
  target_ids:
  - CHEBI:68377
  evidence_ids:
  - record
  - primary
- assessment_id: mechanism
  area: completeness
  topic: Mode of action and target
  outcome: unknown
  summary: No mechanism or direct target is asserted or established for this exact
    glycoside. Its chemical family does not supply a causal mechanism.
  target_ids:
  - CHEBI:68377
  evidence_ids:
  - record
  - primary
  - search
- assessment_id: optional
  area: representation
  topic: Other optional objects
  outcome: not_applicable
  summary: No false resistance, clinical, graph, dataset or quantitative assay claim
    is present. Empty optional fields do not independently warrant defects.
  target_ids:
  - CHEBI:68377
  evidence_ids:
  - record
- assessment_id: ownership
  area: ownership
  topic: Maintained provenance and native status
  outcome: supported
  summary: Source concept and curation events reproduce the inventory. Scientific
    sign-off remains separate from a saved review; native SEEDED is retained.
  target_ids:
  - CHEBI:68377
  evidence_ids:
  - record
  - owner
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-68377-saponin-activity-source-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The adopted experiment does not support the isolated-saponin activity claim
  description: The unqualified antibacterial sentence and role need source adjudication.
    Positive mixture, fraction or parent-aglycone observations cannot establish activity
    of this exact conjugate; preserve the inspected negative endpoint and its limits.
    This does not declare the compound universally inactive or authorize deleting
    it without the maintained inclusion process.
  target_ids:
  - CHEBI:68377
  field_paths:
  - definition
  - activity_roles
  - antimicrobial_class
  - source_concepts
  evidence_ids:
  - record
  - owner
  - chebi
  - primary
  - search
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted definition, role and publication lead; correct through maintained
      source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI import and any justified source normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated-field owner and reproducible seeding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Supported inclusion/grounding/exclusion decision if warranted after source
      adjudication
  rule_id: 'native-review-checklist: Evidence standard, exact compound activity and
    source ownership'
  native_severity: major unsupported compound-specific positive activity attribution
  normalization_reason: This concerns a substantive asserted antibacterial property,
    not an optional empty field or a requirement for every ontology classification
    to carry record-level literature. The detailed linked experiment provides contrary
    compound-specific scope.
actions:
- action_id: A1
  description: Adjudicate the positive activity attribution against the full primary
    experiment and any independently supported exact-compound study. Correct or qualify
    the maintained source definition/role and resulting inclusion decision, preserving
    exact chemical identity and evidence provenance.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:68377
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted definition, role and publication lead; correct through maintained
      source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI import and any justified source normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated-field owner and reproducible seeding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Supported inclusion/grounding/exclusion decision if warranted after source
      adjudication
  acceptance_checks:
  - The maintained disposition explicitly distinguishes this glycoside from fractions,
    mixtures, free aglycones and other sugar conjugates.
  - Retain the negative assay as condition-limited evidence; do not turn it into a
    claim of universal inactivity, a resistance phenotype or a numerical MIC.
  - Any retained positive antibacterial statement identifies an inspected exact-compound
    experiment. If none supports retention, use the documented maintained decision/extraction/seeding
    process rather than a generated-YAML-only deletion or role patch.
  - Any source or inclusion correction reproduces deterministically and passes focused
    schema/strict, corpus reproduction and fullQC. Preserve supported chemical identity
    and source-concept provenance.
limitations:
- The original paper was inspected through its freely author-deposited full text on
  ResearchGate, including structural assignment, Results, Table3 and Experimental
  sections. Direct HTML/PDF retrieval failed; no visual inspection of structure drawings
  or fresh numerical NMR reanalysis is claimed.
- Reaxys was corroborated as an official ChEBI source assertion rather than through
  independent paid-registry access.
- The observed lack of inhibition applies to the reported assay conditions. Bounded
  discovery did not locate an independent exact-saponin positive experiment; it does
  not establish global inactivity or absence of all later evidence.
- Initial focused validation invocation omitted the task-local uv cache and failed
  before validation because the default cache path was sandbox-inaccessible. The corrected
  documented invocation with UV_NO_SYNC=1 and the permitted task cache passed both
  focused gates.
- No native record was edited, no paid provider was used and no external issue or
  author contact occurred.
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
