# Benzyl isothiocyanate: exact neutral identity with material-specific antibacterial support

- Review: 20261021T102333Z-benzyl-isothiocyanate-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:53:30Z
- Finished UTC: 2026-10-21T10:23:33Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Exact neutral benzyl isothiocyanate is supported by ChEBI, independently parsed KEGG structure, PubChem and KNApSAcK. Primary synthetic-compound CFU experiments support antibacterial inclusion. Extract-wide spectra, oil killing kinetics and speculative redox mechanisms must remain distinct from pure-compound observations. No corrective native finding was established; one informational enrichment item remains. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position153; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:17484 | data/antibiotics/antibacterial/benzyl-isothiocyanate.yaml | generated | benzyl isothiocyanate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:17484 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:17484 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:17484 | Actual focused execution exited 0. |
| Structured protein-context applicability | not_applicable | False | CHEBI:17484 | The native record asserts no protein, gene, regulator, pathway or transcriptomic response. Literature-only biosynthesis and mechanism leads remain optional context; no expression-module evidence is used. |
| Authoritative full QC | failed | True | CHEBI:17484 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:17484 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:17484 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:17484 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:17484 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:17484 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:17484 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:17484 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:17484 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Maintained source and native history

provenance: supported. Targets: CHEBI:17484.

The adopted identity/roles and generated provenance agree; all 13 captured input hashes remain unchanged. Native status remains SEEDED.

### Focused validation

schema: supported. Targets: CHEBI:17484.

Focused schema, strict and independent chemistry checks passed. Scientific evidence scope is assessed separately.

### Exact chemical identity and aliases

identity: supported. Targets: CHEBI:17484.

Current independent molecular sources and native encodings agree at full-structure level. The benzyl group and isothiocyanate bond order are preserved.

### Class, role and parents

grounding: supported. Targets: CHEBI:17484.

The chemical parents and broader antibacterial class are appropriate; exact-compound primary assays support antibacterial activity. The ontology drug role is not treated as a regulatory approval assertion.

### Native populated biological claims

evidence: supported. Targets: CHEBI:17484.

The native record makes no organism-specific potency or direct-target assertion that conflicts with the inspected experiments. Pure synthetic compound evidence supports the general inclusion.

### Optional assay and mechanism enrichment

completeness: unknown. Targets: CHEBI:17484.

Primary enrichment is possible, but the oil/pure-compound boundary and CFU-dose units must be maintained. No exact direct molecular target is established by this review.

## Findings

### F1: Preserve exact material and assay scope in optional primary enrichment

informational / open / confirmed; issue key: benzyl-isothiocyanate-primary-material-and-cfu-scope.

Useful exact-compound activity evidence is available, but the study contains chemically different essential-oil and MPLC materials. Empty optional activity and mechanism fields are not defects.

## Recommended Actions And Acceptance Checks

### A1

Optionally curate the demonstrated primary observations with their material, organism and assay qualifiers.

- Use synthetic-BITC Figure 3 for the pure parent; retain E. coli MC4100 and A. actinomycetemcomitans HK1519 identities, 90 min exposure, 37 C and CFU endpoint.
- Preserve reported micromoles as amount applied; resolve assay volume before converting units and do not relabel the endpoint as MIC.
- Keep essential-oil multistrain activity and 5–10 min killing kinetics separate; do not infer universal Gram-negative specificity from that mixed material.
- Describe membrane observations as measured phenotypes and redox explanations as hypotheses, not direct protein binding.
- If adding plant provenance, distinguish detection/isolation from demonstrated biosynthesis; do not import KNApSAcK organism rows automatically. Use validated writer/history and required gates before status promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/benzyl-isothiocyanate.yaml; Entire native YAML, source concept and three seed/reseed events | supports | The exact ChEBI record is SEEDED, with a single neutral chemical structure, source-owned names, chemical parents, activity roles and chemical xrefs. No native quantitative assay, molecular target, resistance, producer, clinical, transcriptomic or causal-graph claim is populated. |
| source | data/raw/chebi_antimicrobials.tsv; data/raw/chebi_role_names.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; 153-raw.json; captured source, role, configuration and generation inputs | supports | The adopted row reproduces the native chemical data, classifications and aliases. The source mint independently reproduces. Exact identifier searches in the captured curator inventory and decisions file, including ignored files, returned no matching override; this is a bounded search of those files, not an absence claim about all external evidence. |
| chemistry | Independent RDKit native chemistry and focused repository gates; 153-chemistry.json; 153-focused-results.json | supports | SMILES and Standard InChI reproduce the same stored full key, formula, neutral one-component graph and masses at stated precision. Neither structure contains a potential tetrahedral stereocentre. The minted source identifier and focused schema/strict validators pass. |
| search | CultureBotAI/AntibioticMech and free chemical/primary-literature sources; 153-local-hits.txt; 153-discovery.json | context_only | Initial target/source hashes preceded judgment. The local identifier/name/slug search included hidden and ignored files outside .git and .venv. Current official chemical sources and a capped EuropePMC discovery search were inspected, followed by selected relevant primary papers. Generated and historical copies are discovery context only. |
| identity | CHEBI:17484; PubChem CID:2346; KEGG:C03098; KNApSAcK:C00007675; Current complete ChEBI page, PUG structure, KEGG MOL and KNApSAcK molecular fields | supports | All encode C8H7NS and MDKCFLQDBWCQCV-UHFFFAOYSA-N: benzyl-N=C=S, distinct from benzyl thiocyanate or phenyl isothiocyanate. Native aliases and CAS 622-78-6 agree with the chemical authorities. KNApSAcK has an overly generic display name but its full structure matches exactly. Its organism table is not used as producer evidence. Beilstein 386135 was verified as an official ChEBI crosswalk, not independently queried in the proprietary registry. |
| grounding | https://www.ebi.ac.uk/chebi/CHEBI:17484; Current roles, names and direct-parent export | supports | The benzenes and isothiocyanate parents and antibacterial-drug role remain current. Classification is broader than a quantitative or clinical-efficacy claim. The native definition is absent, and the adopted source has no publication citation; neither creates a confirmed scientific defect in this review. |
| primary | PMID:21829688; DOI:10.1371/journal.pone.0023045; 153-primary2011.xml; complete Methods, Results and Discussion; synthetic-compound Figure 3 visually inspected | supports | Commercial synthetic BITC (&gt;98% GC purity, Lancaster) was compared with plant material. Figure 3 and Results separately demonstrate dose-dependent CFU reductions for E. coli MC4100 and A. actinomycetemcomitans HK1519. The suspension assay uses 90 min exposure at 37 C and plating for surviving CFU; doses are reported as micromoles applied, not a standard broth MIC. The wider 13-strain panel and rapid time-kill series used essential oil, which contains 73.8% BITC and 26.2% benzyl nitrile. Those oil measurements must not be copied as pure-BITC observations. |
| mechanism-boundary | DOI:10.1371/journal.pone.0023045; Transmission-electron-microscopy Methods/Results and Discussion | partial | The authors report membrane protrusions after pure BITC or oil treatment; no protein-binding measurement is presented. Penetration and interference with bacterial redox systems are proposed mechanisms. Mitochondrial work is cited by analogy, not established as a bacterial target. The study is in vitro and does not prove clinical periodontal treatment efficacy or safety. |
| independent-activity | PMID:19291240; DOI:10.1111/j.1365-2672.2009.04180.x; Complete indexed abstract within153-discovery.json | partial | A separate disc-diffusion study reports BITC growth inhibition among tested Gram-positive and Gram-negative intestinal isolates. It supports antibacterial scope at abstract level but does not supply inspected exact strain/dose data or resolve all apparent differences with the oil study. No quantitative MIC is inferred from disc diffusion. |

## Limits And Additional Notes

- The literature review is bounded to the stated original sources and access levels. No optional empty field is automatically a defect, and this review does not certify clinical use or promote native status.
- The2011 Methods, Results and Discussion were inspected and Figure3 was visually checked; supplementary TLC data and raw spectra were not independently audited. The2009 study remains abstract-only.
- There are no adopted citation leads in the raw ChEBI row. An empty citation-query helper returned unrelated EuropePMC records in153-adopted.json; those results were discarded and are not evidence.
- The primary oil and pure-compound datasets have distinct material scope. Biological membrane charge/state and solvent effects are not deduced from the neutral parent structure.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 13 captured inputs rechecked unchanged. No native record or source table was edited.
- Initial public requests failed sandbox DNS; the permitted public-network retry succeeded. Failed requests were not treated as evidence absence.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T102333Z-benzyl-isothiocyanate-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Benzyl isothiocyanate: exact neutral identity with material-specific antibacterial
  support'
started_at: '2026-10-21T09:53:30Z'
finished_at: '2026-10-21T10:23:33Z'
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
summary: Exact neutral benzyl isothiocyanate is supported by ChEBI, independently
  parsed KEGG structure, PubChem and KNApSAcK. Primary synthetic-compound CFU experiments
  support antibacterial inclusion. Extract-wide spectra, oil killing kinetics and
  speculative redox mechanisms must remain distinct from pure-compound observations.
  No corrective native finding was established; one informational enrichment item
  remains. Scientific assessment retains the stated evidence limits; full verification
  is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/benzyl-isothiocyanate.yaml
    sha256: e1ee8f383aaa6ab7a37a35d12cd27114efd6207a1deab6fea971350f6ae216db
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
- target_id: CHEBI:17484
  path: data/antibiotics/antibacterial/benzyl-isothiocyanate.yaml
  label: benzyl isothiocyanate
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
  selection: Initially uncovered queue position153; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:17484
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:17484
  command: .venv/bin/python /private/tmp/am-review-session/focus014-root.py 153
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:17484
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/benzyl-isothiocyanate.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:17484
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/benzyl-isothiocyanate.yaml --out /private/tmp/am-review-session/153-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-applicability
  name: Structured protein-context applicability
  status: not_applicable
  required: false
  summary: The native record asserts no protein, gene, regulator, pathway or transcriptomic
    response. Literature-only biosynthesis and mechanism leads remain optional context;
    no expression-module evidence is used.
  target_ids:
  - CHEBI:17484
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
  - CHEBI:17484
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
  - CHEBI:17484
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
  - CHEBI:17484
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
  - CHEBI:17484
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
  - CHEBI:17484
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
  - CHEBI:17484
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
  - CHEBI:17484
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
  - CHEBI:17484
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
  - CHEBI:17484
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/benzyl-isothiocyanate.yaml
  locator: Entire native YAML, source concept and three seed/reseed events
  accessed_at: '2026-10-21T09:58:10Z'
  support: supports
  summary: The exact ChEBI record is SEEDED, with a single neutral chemical structure,
    source-owned names, chemical parents, activity roles and chemical xrefs. No native
    quantitative assay, molecular target, resistance, producer, clinical, transcriptomic
    or causal-graph claim is populated.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/chebi_role_names.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: 153-raw.json; captured source, role, configuration and generation inputs
  accessed_at: '2026-10-21T09:58:10Z'
  support: supports
  summary: The adopted row reproduces the native chemical data, classifications and
    aliases. The source mint independently reproduces. Exact identifier searches in
    the captured curator inventory and decisions file, including ignored files, returned
    no matching override; this is a bounded search of those files, not an absence
    claim about all external evidence.
  snapshot_sha256: e490932fab66585f53c73b7bc7bee82b652767006019878126a8734ed58af7b5
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit native chemistry and focused repository gates
  locator: 153-chemistry.json; 153-focused-results.json
  accessed_at: '2026-10-21T09:58:10Z'
  support: supports
  summary: SMILES and Standard InChI reproduce the same stored full key, formula,
    neutral one-component graph and masses at stated precision. Neither structure
    contains a potential tetrahedral stereocentre. The minted source identifier and
    focused schema/strict validators pass.
  snapshot_sha256: 3d83ce8c5078556f25a043698b6d6a1e691aa4ab0867a416fb54faac828be1b6
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech and free chemical/primary-literature sources
  locator: 153-local-hits.txt; 153-discovery.json
  accessed_at: '2026-10-21T09:58:10Z'
  support: context_only
  summary: Initial target/source hashes preceded judgment. The local identifier/name/slug
    search included hidden and ignored files outside .git and .venv. Current official
    chemical sources and a capped EuropePMC discovery search were inspected, followed
    by selected relevant primary papers. Generated and historical copies are discovery
    context only.
  search_scope: Isolated batch016; rg --no-ignore --hidden excluding .git and .venv.
    Exact target and maintained owners; EuropePMC first 100 results with citation
    ordering, not an exhaustive literature survey.
  snapshot_sha256: 4bc1ff3fa6a02460ba2cc3362755007890735132e8580295b49297d45ee2abc9
- evidence_id: identity
  kind: database
  reference: CHEBI:17484; PubChem CID:2346; KEGG:C03098; KNApSAcK:C00007675
  locator: Current complete ChEBI page, PUG structure, KEGG MOL and KNApSAcK molecular
    fields
  accessed_at: '2026-10-21T09:58:10Z'
  support: supports
  summary: 'All encode C8H7NS and MDKCFLQDBWCQCV-UHFFFAOYSA-N: benzyl-N=C=S, distinct
    from benzyl thiocyanate or phenyl isothiocyanate. Native aliases and CAS 622-78-6
    agree with the chemical authorities. KNApSAcK has an overly generic display name
    but its full structure matches exactly. Its organism table is not used as producer
    evidence. Beilstein 386135 was verified as an official ChEBI crosswalk, not independently
    queried in the proprietary registry.'
  snapshot_sha256: 3fa2ac5fb9e64bec76ab04945a9b6a49a2b9221d6e457c4c0bde683612395875
- evidence_id: grounding
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:17484
  locator: Current roles, names and direct-parent export
  accessed_at: '2026-10-21T09:58:10Z'
  support: supports
  summary: The benzenes and isothiocyanate parents and antibacterial-drug role remain
    current. Classification is broader than a quantitative or clinical-efficacy claim.
    The native definition is absent, and the adopted source has no publication citation;
    neither creates a confirmed scientific defect in this review.
  snapshot_sha256: 1cd98f849b71563e5f9ceba3bff835a5a0beb920787cbd1648e4d0cf0a052f4f
- evidence_id: primary
  kind: primary_source
  reference: PMID:21829688; DOI:10.1371/journal.pone.0023045
  locator: 153-primary2011.xml; complete Methods, Results and Discussion; synthetic-compound
    Figure 3 visually inspected
  accessed_at: '2026-10-21T09:58:10Z'
  support: supports
  summary: Commercial synthetic BITC (>98% GC purity, Lancaster) was compared with
    plant material. Figure 3 and Results separately demonstrate dose-dependent CFU
    reductions for E. coli MC4100 and A. actinomycetemcomitans HK1519. The suspension
    assay uses 90 min exposure at 37 C and plating for surviving CFU; doses are reported
    as micromoles applied, not a standard broth MIC. The wider 13-strain panel and
    rapid time-kill series used essential oil, which contains 73.8% BITC and 26.2%
    benzyl nitrile. Those oil measurements must not be copied as pure-BITC observations.
  snapshot_sha256: 0318cc99a7039f9c6c94ed08c1c49743e1f93d18005032b0876556ef95d0df70
- evidence_id: mechanism-boundary
  kind: primary_source
  reference: DOI:10.1371/journal.pone.0023045
  locator: Transmission-electron-microscopy Methods/Results and Discussion
  accessed_at: '2026-10-21T09:58:10Z'
  support: partial
  summary: The authors report membrane protrusions after pure BITC or oil treatment;
    no protein-binding measurement is presented. Penetration and interference with
    bacterial redox systems are proposed mechanisms. Mitochondrial work is cited by
    analogy, not established as a bacterial target. The study is in vitro and does
    not prove clinical periodontal treatment efficacy or safety.
  snapshot_sha256: 0318cc99a7039f9c6c94ed08c1c49743e1f93d18005032b0876556ef95d0df70
- evidence_id: independent-activity
  kind: primary_source
  reference: PMID:19291240; DOI:10.1111/j.1365-2672.2009.04180.x
  locator: Complete indexed abstract within153-discovery.json
  accessed_at: '2026-10-21T09:58:10Z'
  support: partial
  summary: A separate disc-diffusion study reports BITC growth inhibition among tested
    Gram-positive and Gram-negative intestinal isolates. It supports antibacterial
    scope at abstract level but does not supply inspected exact strain/dose data or
    resolve all apparent differences with the oil study. No quantitative MIC is inferred
    from disc diffusion.
  snapshot_sha256: 8b880afbd61b86d0158e6c046fa7225cbdb8e1f2e7c5faf2dca6b1a6270e4ea9
assessments:
- assessment_id: provenance
  area: provenance
  topic: Maintained source and native history
  outcome: supported
  summary: The adopted identity/roles and generated provenance agree; all 13 captured
    input hashes remain unchanged. Native status remains SEEDED.
  target_ids:
  - CHEBI:17484
  evidence_ids:
  - native
  - source
  - chemistry
- assessment_id: schema
  area: schema
  topic: Focused validation
  outcome: supported
  summary: Focused schema, strict and independent chemistry checks passed. Scientific
    evidence scope is assessed separately.
  target_ids:
  - CHEBI:17484
  evidence_ids:
  - chemistry
- assessment_id: identity
  area: identity
  topic: Exact chemical identity and aliases
  outcome: supported
  summary: Current independent molecular sources and native encodings agree at full-structure
    level. The benzyl group and isothiocyanate bond order are preserved.
  target_ids:
  - CHEBI:17484
  evidence_ids:
  - identity
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Class, role and parents
  outcome: supported
  summary: The chemical parents and broader antibacterial class are appropriate; exact-compound
    primary assays support antibacterial activity. The ontology drug role is not treated
    as a regulatory approval assertion.
  target_ids:
  - CHEBI:17484
  evidence_ids:
  - grounding
  - primary
  - independent-activity
- assessment_id: claims
  area: evidence
  topic: Native populated biological claims
  outcome: supported
  summary: The native record makes no organism-specific potency or direct-target assertion
    that conflicts with the inspected experiments. Pure synthetic compound evidence
    supports the general inclusion.
  target_ids:
  - CHEBI:17484
  evidence_ids:
  - native
  - primary
- assessment_id: completeness
  area: completeness
  topic: Optional assay and mechanism enrichment
  outcome: unknown
  summary: Primary enrichment is possible, but the oil/pure-compound boundary and
    CFU-dose units must be maintained. No exact direct molecular target is established
    by this review.
  target_ids:
  - CHEBI:17484
  evidence_ids:
  - primary
  - mechanism-boundary
  - independent-activity
findings:
- finding_id: F1
  issue_key: benzyl-isothiocyanate-primary-material-and-cfu-scope
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Preserve exact material and assay scope in optional primary enrichment
  description: Useful exact-compound activity evidence is available, but the study
    contains chemically different essential-oil and MPLC materials. Empty optional
    activity and mechanism fields are not defects.
  target_ids:
  - CHEBI:17484
  field_paths:
  - evidence
  - activity_spectrum
  - discussions
  evidence_ids:
  - primary
  - mechanism-boundary
  - independent-activity
  rule_id: 'native-review-checklist: Evidence Fidelity and completeness'
  native_severity: informational optional enrichment
  normalization_reason: The native record has no contradictory populated assay claim.
    This is a useful primary-evidence follow-up, not a missing-required-field defect.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/benzyl-isothiocyanate.yaml
    role: Future curator-owned primary evidence and optional assay annotations via
      validated writer/history workflow
actions:
- action_id: A1
  description: Optionally curate the demonstrated primary observations with their
    material, organism and assay qualifiers.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:17484
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/benzyl-isothiocyanate.yaml
    role: Future curator-owned primary evidence and optional assay annotations via
      validated writer/history workflow
  acceptance_checks:
  - Use synthetic-BITC Figure 3 for the pure parent; retain E. coli MC4100 and A.
    actinomycetemcomitans HK1519 identities, 90 min exposure, 37 C and CFU endpoint.
  - Preserve reported micromoles as amount applied; resolve assay volume before converting
    units and do not relabel the endpoint as MIC.
  - Keep essential-oil multistrain activity and 5–10 min killing kinetics separate;
    do not infer universal Gram-negative specificity from that mixed material.
  - Describe membrane observations as measured phenotypes and redox explanations as
    hypotheses, not direct protein binding.
  - If adding plant provenance, distinguish detection/isolation from demonstrated
    biosynthesis; do not import KNApSAcK organism rows automatically. Use validated
    writer/history and required gates before status promotion.
limitations:
- The literature review is bounded to the stated original sources and access levels.
  No optional empty field is automatically a defect, and this review does not certify
  clinical use or promote native status.
- The2011 Methods, Results and Discussion were inspected and Figure3 was visually
  checked; supplementary TLC data and raw spectra were not independently audited.
  The2009 study remains abstract-only.
- There are no adopted citation leads in the raw ChEBI row. An empty citation-query
  helper returned unrelated EuropePMC records in153-adopted.json; those results were
  discarded and are not evidence.
- The primary oil and pure-compound datasets have distinct material scope. Biological
  membrane charge/state and solvent effects are not deduced from the neutral parent
  structure.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 13 captured inputs rechecked unchanged. No native record or source table was
  edited.
- Initial public requests failed sandbox DNS; the permitted public-network retry succeeded.
  Failed requests were not treated as evidence absence.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:17484
- https://doi.org/10.1371/journal.pone.0023045
- https://doi.org/10.1111/j.1365-2672.2009.04180.x
```
