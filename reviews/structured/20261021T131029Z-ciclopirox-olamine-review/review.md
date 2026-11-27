# Ciclopirox olamine: exact salt identity and bounded antimicrobial evidence

- Review: 20261021T131029Z-ciclopirox-olamine-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:48:50Z
- Finished UTC: 2026-10-21T13:10:29Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native 1:1 ethanolamine salt is internally coherent. Official KEGG uses neutral component notation for the same drug stoichiometry, while ChEBI uses the charged ion pair; this is recorded without treating the drug reference as a different compound. Original antibacterial, fungal and anti-inflammatory studies support the broad roles at their stated evidence depth. No substantive scientific correction is demonstrated; proprietary-link and full-method limits remain explicit. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position299; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:31398 | data/antibiotics/antibacterial/ciclopirox-olamine.yaml | generated | ciclopirox olamine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:31398 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:31398 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:31398 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:31398 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:31398 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:31398 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:31398 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:31398 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:31398 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:31398 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:31398 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:31398 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact 1:1 salt and drug-reference scope

identity: supported. Targets: CHEBI:31398.

The native charged ion pair is correct. KEGG drug notation differs only in component proton placement; the drug link is not represented as exact equality of charged graphs.

### Parents, aliases and activity roles

grounding: supported. Targets: CHEBI:31398.

Chemical parents, source-scoped names and original antibacterial/fungal evidence agree. Brand names remain separate from exact chemical synonyms.

### Activity, anti-inflammatory and topical-use wording

evidence: supported. Targets: CHEBI:31398.

Original studies support the qualitative wording within their stated formulation and assay scope; no quantitative clinical result or current product status is asserted.

### Restricted proprietary references

identity: unknown. Targets: CHEBI:31398.

Direct DrugBank salt-entry and Beilstein content could not be independently verified. No positive wrong-compound evidence was found.

### Source and literature disposition

provenance: supported. Targets: CHEBI:31398.

All ten adopted leads and the complete generated content were checked. No host pathway was imported as an antibacterial mechanism.

### Optional mechanistic and quantitative enrichment

completeness: supported. Targets: CHEBI:31398.

Absent optional fields do not create a defect. The native record has no protein/pathway/transcriptomic assertion requiring the structured adapter; new host-paper context does not establish an antimicrobial target.

### Focused deterministic validity

schema: supported. Targets: CHEBI:31398.

Documented focused validators pass; scientific limitations and shared failed corpus gates remain separate.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/ciclopirox-olamine.yaml; Entire 85-line native record and all four history events | supports | The SEEDED/EXACT record has five correctly typed brand names, a charge-specific systematic name and three other chemical aliases, two broader parents, two roles, two registry references and two drug links. It has no target, quantitative activity, resistance, producer, regulatory assertion or causal graph. The two source-copied spelling errors in the definition do not change its scientific meaning. |
| owners | data/raw/chebi_antimicrobials.tsv;data/raw/chebi_role_names.tsv;scripts/extract_source_inventory.py;scripts/seed_from_sources.py; 299-raw-rows.json and generated field owners | supports | The exact ChEBI row supplies the definition, names, parents, roles, structure, links and ten adopted PMID leads. All thirteen preserved input hashes remain unchanged, and four seed/reseed events agree with provenance. |
| chemistry | CHEBI:31398;KEGG:D01364; 299-chemistry.json;030-root-xref-chemistry.json;299-protonation-check.json | supports | Native and current ChEBI encode a ciclopirox anion plus ethanolammonium, net charge zero, two components, total C14H24N2O3 and HKUKJIQHPXYJTP-UHFFFAOYSA-O. KEGG encodes neutral ciclopirox plus ethanolamine, MBRHNTMUYWQHMR-UHFFFAOYSA-N. Neutralizing both representations gives identical canonical component graphs and mutual chirality-aware matches. The 1:1 salt is distinct from the one-component free base; no stereo is unspecified. |
| authority | CHEBI:31398;CHEBI:46850;CHEBI:87130;CHEBI:33282;CHEBI:86327;KEGG:D01364; Official chemical JSON, all four retained term responses and complete KEGG entry/molfile | supports | Organoammonium-salt and hydroxypyridone-antifungal parents fit the graph and drug scope. KEGG explicitly identifies ciclopirox olamine, CAS41621-49-2 and Loprox as a trade name. Current ChEBI repeats the remaining brand/registry aliases. DrugBank salt-page retrieval returned403; Beilstein was not independently accessed. Registry repetition is not an independent proprietary graph check. |
| activity | PMID:12895182;DOI:10.1046/j.1365-4362.42.s1.4.x; Complete original indexed abstract | supports | The study explicitly tests ciclopirox olamine by adapted NCCLS microdilution against39 fungal and45 bacterial isolates, reporting activity across the tested Gram-positive and Gram-negative panel. Its full strain/material/medium tables were not obtained. This supports qualitative antibacterial and antifungal roles, not an unqualified clinical breakpoint or imported species-level MIC. |
| inflammation | PMID:9372359;PMID:1840158; Complete original indexed abstracts | supports | The1997 controlled human UVB experiment tests proprietary topical preparations and reports anti-inflammatory effects of ciclopirox olamine. The1991 work separately examines cell-based inflammatory readouts, a mouse-ear model and clinical preparations. These support conditional anti-inflammatory activity, not a bacterial protein target or a universal direct enzyme mechanism. |
| clinical-use | PMID:2870809;PMID:1838936;PMID:33796559;DOI:10.1159/000512037; Complete original skin/nail study abstracts; original PMC7991492 Case Report and Discussion | supports | The1985 cutaneous-candidosis trials test1% cream. The1991 report explicitly names an8% olamine nail preparation, although full composition/method details were not recovered. The2021 case uses1% olamine solution with nail debridement for culture-confirmed T.rubrum infection. These support topical-use context; combination benefit is not isolated drug efficacy, and no current approval or universal cure claim follows. |
| combination | PMID:31907180;DOI:10.1128/AAC.01909-19; Complete original indexed abstract; full XML retrieval returned500 | context_only | Ciclopirox olamine potentiates thiostrepton under iron-limited conditions. Individual agents are described as bacteriostatic and selected combinations as bactericidal; these outcomes must remain distinct. Detailed doses, media and isolate-level results were not independently audited. |
| leads | Ten adopted PMID leads; 299-lead-dispositions.json and299-adopted-core.json | context_only | All ten original abstracts were read and individually dispositioned. Two synthetic-series abstracts do not specify the exact ciclopirox comparator; formulation/PK, host signaling, cancer, aging, angiogenesis and viral results remain separate from the native antimicrobial roles. Full XML downloaded for two host papers was not relied on as independently read full text. |
| validation | Focused schema, strict and independent chemistry checks; 299-focused-results.json;299-chemistry.json | supports | The actual focused checks pass. Every preserved source-input hash was recomputed unchanged. These results do not replace the separate shared corpus gates. |
| search | Exact local and public source discovery; 299-local-hits.txt and public retrieval manifests | context_only | Local discovery included hidden and ignored files. Public research followed exact source identifiers and compound-specific primary studies; it is a bounded review, not an exhaustive reading of every publication. |

## Limits And Additional Notes

- All ten adopted citations were read at complete-original-abstract depth. Two host-paper XML files were downloaded but not relied on as fully inspected evidence. Exact comparator use in the two synthetic-series papers remains unresolved.
- The2003 activity study,1991/1997 anti-inflammatory studies and1985/1991 clinical studies were abstract-depth. Full strain/material/medium tables and quantitative clinical outcomes were not independently audited.
- The2021 original case report was read through its main text. Nail debridement and topical olamine were combined; the report cannot establish isolated single-agent efficacy. Historical8% olamine naming was not used to equate every modern8% ciclopirox lacquer with this salt.
- DrugBank direct access returned403; Beilstein was not independently accessed. CAS is cross-attested by ChEBI/KEGG without separate registry graph retrieval.
- The iron-limited thiostrepton combination source remained complete-abstract depth after XML/PMC retrieval failures. Its combination killing is not assigned to single-agent olamine.
- Current ChEBI has additional role/citation annotations outside the adopted seed slice. They are not silently imported or treated as missing required fields.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Native records, source inventories, status and history were not modified. Initial captures were preserved and actual owners appended before judgment.
- All optional notes, links and tags were checked for this exact target.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T131029Z-ciclopirox-olamine-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Ciclopirox olamine: exact salt identity and bounded antimicrobial evidence'
started_at: '2026-10-21T12:48:50Z'
finished_at: '2026-10-21T13:10:29Z'
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
summary: The native 1:1 ethanolamine salt is internally coherent. Official KEGG uses
  neutral component notation for the same drug stoichiometry, while ChEBI uses the
  charged ion pair; this is recorded without treating the drug reference as a different
  compound. Original antibacterial, fungal and anti-inflammatory studies support the
  broad roles at their stated evidence depth. No substantive scientific correction
  is demonstrated; proprietary-link and full-method limits remain explicit. Scientific
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
  - path: data/antibiotics/antibacterial/ciclopirox-olamine.yaml
    sha256: f3bf3b2007a77857cf56585534c70a0f1e08b139f7f4cc32f15979b40835fe94
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
- target_id: CHEBI:31398
  path: data/antibiotics/antibacterial/ciclopirox-olamine.yaml
  label: ciclopirox olamine
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
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_role_names.tsv
    role: ChEBI activity role names
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position299; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:31398
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:31398
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    299
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:31398
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/ciclopirox-olamine.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:31398
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/ciclopirox-olamine.yaml --out /private/tmp/am-review-session/299-strict.tsv
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
  - CHEBI:31398
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
  - CHEBI:31398
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
  - CHEBI:31398
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
  - CHEBI:31398
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
  - CHEBI:31398
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
  - CHEBI:31398
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
  - CHEBI:31398
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
  - CHEBI:31398
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
  - CHEBI:31398
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/ciclopirox-olamine.yaml
  locator: Entire 85-line native record and all four history events
  accessed_at: '2026-10-21T13:08:46Z'
  support: supports
  summary: The SEEDED/EXACT record has five correctly typed brand names, a charge-specific
    systematic name and three other chemical aliases, two broader parents, two roles,
    two registry references and two drug links. It has no target, quantitative activity,
    resistance, producer, regulatory assertion or causal graph. The two source-copied
    spelling errors in the definition do not change its scientific meaning.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv;data/raw/chebi_role_names.tsv;scripts/extract_source_inventory.py;scripts/seed_from_sources.py
  locator: 299-raw-rows.json and generated field owners
  accessed_at: '2026-10-21T13:08:46Z'
  support: supports
  summary: The exact ChEBI row supplies the definition, names, parents, roles, structure,
    links and ten adopted PMID leads. All thirteen preserved input hashes remain unchanged,
    and four seed/reseed events agree with provenance.
  snapshot_sha256: 20e435fd0b2263c27d1ec6276a8a9a09602a408d2a6becf37561fc5bed092696
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:31398;KEGG:D01364
  locator: 299-chemistry.json;030-root-xref-chemistry.json;299-protonation-check.json
  accessed_at: '2026-10-21T13:08:46Z'
  support: supports
  summary: Native and current ChEBI encode a ciclopirox anion plus ethanolammonium,
    net charge zero, two components, total C14H24N2O3 and HKUKJIQHPXYJTP-UHFFFAOYSA-O.
    KEGG encodes neutral ciclopirox plus ethanolamine, MBRHNTMUYWQHMR-UHFFFAOYSA-N.
    Neutralizing both representations gives identical canonical component graphs and
    mutual chirality-aware matches. The 1:1 salt is distinct from the one-component
    free base; no stereo is unspecified.
  snapshot_sha256: 504fb9855d817ef8fa67f3942bae55cf2d08a91c31e3c0b4a8d6862bee6d571c
- evidence_id: authority
  kind: authority
  reference: CHEBI:31398;CHEBI:46850;CHEBI:87130;CHEBI:33282;CHEBI:86327;KEGG:D01364
  locator: Official chemical JSON, all four retained term responses and complete KEGG
    entry/molfile
  accessed_at: '2026-10-21T13:08:46Z'
  support: supports
  summary: Organoammonium-salt and hydroxypyridone-antifungal parents fit the graph
    and drug scope. KEGG explicitly identifies ciclopirox olamine, CAS41621-49-2 and
    Loprox as a trade name. Current ChEBI repeats the remaining brand/registry aliases.
    DrugBank salt-page retrieval returned403; Beilstein was not independently accessed.
    Registry repetition is not an independent proprietary graph check.
  snapshot_sha256: 7132f53048e8f8f582da683752e57359c3a876b3080d47b53b625777bb8e4c45
- evidence_id: activity
  kind: primary_source
  reference: PMID:12895182;DOI:10.1046/j.1365-4362.42.s1.4.x
  locator: Complete original indexed abstract
  accessed_at: '2026-10-21T13:08:46Z'
  support: supports
  summary: The study explicitly tests ciclopirox olamine by adapted NCCLS microdilution
    against39 fungal and45 bacterial isolates, reporting activity across the tested
    Gram-positive and Gram-negative panel. Its full strain/material/medium tables
    were not obtained. This supports qualitative antibacterial and antifungal roles,
    not an unqualified clinical breakpoint or imported species-level MIC.
  snapshot_sha256: 552b878d6859f65ca1ac1f5b4ec62b6e27c574fa9e27bf0cc1a30e83a07def72
- evidence_id: inflammation
  kind: primary_source
  reference: PMID:9372359;PMID:1840158
  locator: Complete original indexed abstracts
  accessed_at: '2026-10-21T13:08:46Z'
  support: supports
  summary: The1997 controlled human UVB experiment tests proprietary topical preparations
    and reports anti-inflammatory effects of ciclopirox olamine. The1991 work separately
    examines cell-based inflammatory readouts, a mouse-ear model and clinical preparations.
    These support conditional anti-inflammatory activity, not a bacterial protein
    target or a universal direct enzyme mechanism.
  snapshot_sha256: 552b878d6859f65ca1ac1f5b4ec62b6e27c574fa9e27bf0cc1a30e83a07def72
- evidence_id: clinical-use
  kind: primary_source
  reference: PMID:2870809;PMID:1838936;PMID:33796559;DOI:10.1159/000512037
  locator: Complete original skin/nail study abstracts; original PMC7991492 Case Report
    and Discussion
  accessed_at: '2026-10-21T13:08:46Z'
  support: supports
  summary: The1985 cutaneous-candidosis trials test1% cream. The1991 report explicitly
    names an8% olamine nail preparation, although full composition/method details
    were not recovered. The2021 case uses1% olamine solution with nail debridement
    for culture-confirmed T.rubrum infection. These support topical-use context; combination
    benefit is not isolated drug efficacy, and no current approval or universal cure
    claim follows.
- evidence_id: combination
  kind: primary_source
  reference: PMID:31907180;DOI:10.1128/AAC.01909-19
  locator: Complete original indexed abstract; full XML retrieval returned500
  accessed_at: '2026-10-21T13:08:46Z'
  support: context_only
  summary: Ciclopirox olamine potentiates thiostrepton under iron-limited conditions.
    Individual agents are described as bacteriostatic and selected combinations as
    bactericidal; these outcomes must remain distinct. Detailed doses, media and isolate-level
    results were not independently audited.
  snapshot_sha256: 32b5adcb87f742864ec45a704e1b87611dc39980f8ec96f92bb6b7ab36f3efca
- evidence_id: leads
  kind: database
  reference: Ten adopted PMID leads
  locator: 299-lead-dispositions.json and299-adopted-core.json
  accessed_at: '2026-10-21T13:08:46Z'
  support: context_only
  summary: All ten original abstracts were read and individually dispositioned. Two
    synthetic-series abstracts do not specify the exact ciclopirox comparator; formulation/PK,
    host signaling, cancer, aging, angiogenesis and viral results remain separate
    from the native antimicrobial roles. Full XML downloaded for two host papers was
    not relied on as independently read full text.
  snapshot_sha256: 11eeb9614bc929ad3ddf81a1a12faa962570b2b6fcd7349ac6ebf73f6e71f2e7
- evidence_id: validation
  kind: validation
  reference: Focused schema, strict and independent chemistry checks
  locator: 299-focused-results.json;299-chemistry.json
  accessed_at: '2026-10-21T13:08:46Z'
  support: supports
  summary: The actual focused checks pass. Every preserved source-input hash was recomputed
    unchanged. These results do not replace the separate shared corpus gates.
  snapshot_sha256: 07574a9c1a8b0e51717db67e7431ce248d78f24c372e05ef64e6e31eee056672
- evidence_id: search
  kind: search
  reference: Exact local and public source discovery
  locator: 299-local-hits.txt and public retrieval manifests
  accessed_at: '2026-10-21T13:08:46Z'
  support: context_only
  summary: Local discovery included hidden and ignored files. Public research followed
    exact source identifiers and compound-specific primary studies; it is a bounded
    review, not an exhaustive reading of every publication.
  search_scope: Ignored-inclusive local search and public exact-name, identifier,
    activity and source-publication searches on 2026-10-21.
  snapshot_sha256: af401c01d8d0561077f37b017e72aa8298b674a9c95734a2596675a29c6c0771
assessments:
- assessment_id: identity
  area: identity
  topic: Exact 1:1 salt and drug-reference scope
  outcome: supported
  summary: The native charged ion pair is correct. KEGG drug notation differs only
    in component proton placement; the drug link is not represented as exact equality
    of charged graphs.
  target_ids:
  - CHEBI:31398
  evidence_ids:
  - chemistry
  - authority
- assessment_id: class
  area: grounding
  topic: Parents, aliases and activity roles
  outcome: supported
  summary: Chemical parents, source-scoped names and original antibacterial/fungal
    evidence agree. Brand names remain separate from exact chemical synonyms.
  target_ids:
  - CHEBI:31398
  evidence_ids:
  - authority
  - activity
  - clinical-use
- assessment_id: definition
  area: evidence
  topic: Activity, anti-inflammatory and topical-use wording
  outcome: supported
  summary: Original studies support the qualitative wording within their stated formulation
    and assay scope; no quantitative clinical result or current product status is
    asserted.
  target_ids:
  - CHEBI:31398
  evidence_ids:
  - activity
  - inflammation
  - clinical-use
- assessment_id: links
  area: identity
  topic: Restricted proprietary references
  outcome: unknown
  summary: Direct DrugBank salt-entry and Beilstein content could not be independently
    verified. No positive wrong-compound evidence was found.
  target_ids:
  - CHEBI:31398
  evidence_ids:
  - authority
- assessment_id: provenance
  area: provenance
  topic: Source and literature disposition
  outcome: supported
  summary: All ten adopted leads and the complete generated content were checked.
    No host pathway was imported as an antibacterial mechanism.
  target_ids:
  - CHEBI:31398
  evidence_ids:
  - owners
  - leads
- assessment_id: completeness
  area: completeness
  topic: Optional mechanistic and quantitative enrichment
  outcome: supported
  summary: Absent optional fields do not create a defect. The native record has no
    protein/pathway/transcriptomic assertion requiring the structured adapter; new
    host-paper context does not establish an antimicrobial target.
  target_ids:
  - CHEBI:31398
  evidence_ids:
  - native
  - leads
  - combination
- assessment_id: validation
  area: schema
  topic: Focused deterministic validity
  outcome: supported
  summary: Documented focused validators pass; scientific limitations and shared failed
    corpus gates remain separate.
  target_ids:
  - CHEBI:31398
  evidence_ids:
  - validation
findings: []
actions: []
limitations:
- All ten adopted citations were read at complete-original-abstract depth. Two host-paper
  XML files were downloaded but not relied on as fully inspected evidence. Exact comparator
  use in the two synthetic-series papers remains unresolved.
- The2003 activity study,1991/1997 anti-inflammatory studies and1985/1991 clinical
  studies were abstract-depth. Full strain/material/medium tables and quantitative
  clinical outcomes were not independently audited.
- The2021 original case report was read through its main text. Nail debridement and
  topical olamine were combined; the report cannot establish isolated single-agent
  efficacy. Historical8% olamine naming was not used to equate every modern8% ciclopirox
  lacquer with this salt.
- DrugBank direct access returned403; Beilstein was not independently accessed. CAS
  is cross-attested by ChEBI/KEGG without separate registry graph retrieval.
- The iron-limited thiostrepton combination source remained complete-abstract depth
  after XML/PMC retrieval failures. Its combination killing is not assigned to single-agent
  olamine.
- Current ChEBI has additional role/citation annotations outside the adopted seed
  slice. They are not silently imported or treated as missing required fields.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Native records, source inventories, status and history were not modified. Initial
  captures were preserved and actual owners appended before judgment.
- All optional notes, links and tags were checked for this exact target.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:31398
- https://rest.kegg.jp/get/D01364
- https://pubmed.ncbi.nlm.nih.gov/12895182/
tags:
- ciclopirox-olamine
- salt-identity
- assay-scope
```
