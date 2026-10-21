# Chlorhexidine acetate: coherent diacetate identity with bounded original activity evidence

- Review: 20261021T125722Z-chlorhexidine-acetate-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:36:39Z
- Finished UTC: 2026-10-21T12:57:22Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No substantive correction identified. The exact 1:2 acetate composition, synonyms, broader classes and source provenance are coherent. Original primary evidence supports antibacterial activity and the adopted lead set supports a bounded antifungal role. Formulations and co-treatments are kept separate from pure-compound potency; unavailable proprietary mappings and detailed assay gaps remain explicit. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position288; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:81711 | data/antibiotics/antibacterial/chlorhexidine-acetate.yaml | generated | chlorhexidine acetate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:81711 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:81711 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:81711 | Actual focused execution exited 0. |
| Structured adapter applicability | not_applicable | False | CHEBI:81711 | The native record asserts no gene, protein, pathway, regulator or transcriptomic dataset. Primary transcriptomic lead disposition did not add a target or pathway claim. |
| Authoritative full QC | failed | True | CHEBI:81711 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:81711 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:81711 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:81711 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:81711 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:81711 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:81711 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:81711 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:81711 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Source ownership and history

provenance: supported. Targets: CHEBI:81711.

Maintained source rows and owning extraction/seeding paths were inspected. Initial provenance hashes remain unchanged; source-only and experimental assertions are distinguished.

### Focused documented gates

schema: supported. Targets: CHEBI:81711.

Schema and strict validation passed; independent native chemistry also passed. These checks do not establish biological truth or scientific REVIEWED status.

### Exact diacetate composition and names

identity: supported. Targets: CHEBI:81711.

Native and inspected official encodings agree; six exact chemical names and one brand name have coherent scope. Acetate, gluconate and free base remain separate molecular records.

### Antibacterial and antifungal classification

evidence: supported. Targets: CHEBI:81711.

The original diacetate paper directly supports antibacterial activity. The adopted Candida adhesive study supports a bounded antifungal role at abstract depth. Effects are material-, organism- and assay-specific.

### Registry and document link scope

grounding: unknown. Targets: CHEBI:81711.

CAS and exact KEGG/ChemSpider identities are corroborated by inspected official chemical records. DrugBank salt detail remains inaccessible and is only attested by current ChEBI. Both patent links are relevant documents.

### Optional target and primary detail

completeness: unknown. Targets: CHEBI:81711.

No target, mechanism enum, resistance, MIC, clinical-product assertion or causal graph is populated. Transcriptional response is not direct binding, and optional absence alone is not a defect.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally add exact-material primary evidence after recovering full assay methods for the chosen endpoint.

- Retain diacetate identity; distinguish formulated products, combinations, controls and negative results.
- Record exact organism/strain, material concentration basis, medium, inoculum, incubation and endpoint before entering MICs.
- Do not infer a direct antibacterial target from transcriptional changes or transfer gluconate/free-base experiments as exact diacetate assays.
- Run documented native validators and applicable source/reference/history/corpus gates after any curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/chlorhexidine-acetate.yaml; Entire native YAML, all populated domains and all history events | supports | Read the whole native record without changing it. All initial captured hashes were retained; actual source-owner inputs were appended before detailed assessment. |
| owners | 288-raw-rows.json; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact source rows and applicable source assembly/attachment functions | supports | Inspected adopted rows against the native fields, including identifier, source mint, chemical fields, parents, roles, synonyms and source/history scope. Provenance agreement is distinguished from scientific validation. |
| chemistry | 288-chemistry.json; 029-xref-check.json; Independent RDKit native encoding and official external structure comparisons | supports | Native SMILES and InChI agree on the full key, formula, charge, masses and fragment/stereochemical scope. Official external molecular comparisons described below preserve salts and configured stereochemistry. |
| search | 029-local-hits.txt; official source retrieval and original-paper follow-up; Ignored-inclusive local source/curation search; bounded official and primary-source discovery | supports | Local searches included hidden and ignored files in the stated repository source/curation scope. Adopted citation leads were resolved separately from additional discovery. No claim of an exhaustive literature search is made. |
| identity | CHEBI:81711; KEGG:C18372; KEGG:D07669; 288-chebi.json and both official KEGG molfiles/text; complete molecular comparison | supports | All inspected molecular encodings give WDRFFJWBUDTUCA-UHFFFAOYSA-N, C26H38Cl2N10O4, charge zero and three components: one chlorhexidine plus two acetic-acid components in the standardized neutral representation. This encodes salt composition and does not assert neutral speciation in aqueous solution. The systematic 1:2 names agree. Nolvasan is correctly typed BRAND_NAME. CHEBI:59230 is the broader acetate-salt class; CHEBI:33282/35718 are antibacterial/antifungal roles. ChemSpider7838272 was also retrieved directly; its standard InChI recomputes the same full key. The initial browser403 did not prevent a subsequent public-page retrieval. |
| discovery | PMID:13172429; DOI:10.1111/j.1476-5381.1954.tb00840.x; Original 1954 five-page scanned article, pages 192–196; all five page images visually read | supports | The original study distinguishes free-base structure 10,040 from diacetate and dihydrochloride. Diacetate was used almost entirely; selected in-vitro hydrochloride comparisons gave similar potency. The paper reports bacteriostatic dilution and bactericidal experiments with inoculum, pH, medium and egg-yolk neutralization effects. BHI/egg-yolk antagonism and condition-specific spore results preclude a universal kill claim. Old dilution endpoints are not converted into modern strain-specific mass MICs. These data directly support diacetate antibacterial activity, without asserting a measured bacterial protein target. |
| adopted-leads | PMID:19924977; 22058347; 22563792; 24815823; 28012407; 28468901; 28575994; 28691453; 28727160; 29178741; 288-primary-abstracts.txt and 288-all-core.json; all ten complete original abstracts | partial | Every adopted ChEBI lead was inspected. PMID19924977 reports P. aeruginosa transcriptional responses at 0.008 mM, not direct target binding. PMID22058347 is a canine preputial disinfection study. PMID22563792 studies 7.5% cement formulations; 24815823 is dentin bonding; 28012407 uses PLGA/chitosan plus bFGF; 28575994 combines silver nanoparticles with chlorhexidine acetate. PMID28691453 directly supports Candida albicans growth suppression in chlorhexidine-diacetate denture adhesive, with material/assay limits. PMID28727160 uses zinc-acetate/chlorhexidine mouthrinse. PMID28468901 has ambiguous title/abstract salt wording and cannot cleanly identify exact acetate efficacy. PMID29178741 found no reduction in biofilm microorganism counts from tested acetate-containing glass ionomer cements; this negative result is preserved. No formulation endpoint is silently treated as pure-compound MIC. |
| patents | patent:EP2376129; patent:WO2012033625; Selected original patent definitions, formulation passages and examples | context_only | Both document links concern chlorhexidine acetate formulations. EP2376129 includes diacetate plus isopropanol cleaner experiments; WO2012033625 describes diacetate composition and medical-device cleaning formulations. These are document links, not exact molecule xrefs or blanket clinical efficacy claims. Selected passages were read, not a full legal/patent audit. The EP table has organism/count inconsistencies and is not adopted as a numeric assay source. |
| chemspider | https://www.chemspider.com/Chemical-Structure.7838272.html; Complete JSON-LD standard InChI; 029-extra-chemistry.json | supports | The exact current ChemSpider standard InChI reproduces the native diacetate key, three-component composition and formula. |

## Limits And Additional Notes

- All ten adopted leads were read at complete original-abstract depth; full methods/tables were not inspected for those ten studies. The original 1954 discovery was independently read as all five page images.
- DrugBank salt detail was unavailable; the ChemSpider standard InChI was independently checked after a successful subsequent retrieval. CAS was not queried through a paid registry.
- Patent reading was limited to the stated composition/formulation/assay passages; no legal status assessment or unqualified formulation potency claim is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record, maintained input, scientific status or history was changed. This review is evidence for separately authorized curation, not status promotion.
- Root completed the entire native-record audit, preserved every captured input hash and inspected each adopted literature lead at the explicitly documented depth. Final saved conclusions retain all access, material, organism and assay boundaries.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T125722Z-chlorhexidine-acetate-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Chlorhexidine acetate: coherent diacetate identity with bounded original activity
  evidence'
started_at: '2026-10-21T12:36:39Z'
finished_at: '2026-10-21T12:57:22Z'
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
summary: No substantive correction identified. The exact 1:2 acetate composition,
  synonyms, broader classes and source provenance are coherent. Original primary evidence
  supports antibacterial activity and the adopted lead set supports a bounded antifungal
  role. Formulations and co-treatments are kept separate from pure-compound potency;
  unavailable proprietary mappings and detailed assay gaps remain explicit. Scientific
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
  - path: data/antibiotics/antibacterial/chlorhexidine-acetate.yaml
    sha256: 4470af0ecb2fc043eb8389c838f9f07428dbaffaa88f3c47b67e284d832daee5
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
- target_id: CHEBI:81711
  path: data/antibiotics/antibacterial/chlorhexidine-acetate.yaml
  label: chlorhexidine acetate
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
    role: ChEBI activity role label resolution
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position288; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:81711
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:81711
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    288
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:81711
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/chlorhexidine-acetate.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:81711
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/chlorhexidine-acetate.yaml --out /private/tmp/am-review-session/288-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: structured-adapter
  name: Structured adapter applicability
  status: not_applicable
  required: false
  summary: The native record asserts no gene, protein, pathway, regulator or transcriptomic
    dataset. Primary transcriptomic lead disposition did not add a target or pathway
    claim.
  target_ids:
  - CHEBI:81711
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:81711
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
  - CHEBI:81711
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
  - CHEBI:81711
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
  - CHEBI:81711
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
  - CHEBI:81711
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
  - CHEBI:81711
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
  - CHEBI:81711
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
  - CHEBI:81711
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
  - CHEBI:81711
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/chlorhexidine-acetate.yaml
  locator: Entire native YAML, all populated domains and all history events
  accessed_at: '2026-10-21T12:52:32Z'
  support: supports
  summary: Read the whole native record without changing it. All initial captured
    hashes were retained; actual source-owner inputs were appended before detailed
    assessment.
- evidence_id: owners
  kind: record_content
  reference: 288-raw-rows.json; scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  locator: Exact source rows and applicable source assembly/attachment functions
  accessed_at: '2026-10-21T12:52:32Z'
  support: supports
  summary: Inspected adopted rows against the native fields, including identifier,
    source mint, chemical fields, parents, roles, synonyms and source/history scope.
    Provenance agreement is distinguished from scientific validation.
  snapshot_sha256: 81b29b265a0cd3ff71a4b235465d78177499027cdb3f848b14dd6c003732fa5e
- evidence_id: chemistry
  kind: validation
  reference: 288-chemistry.json; 029-xref-check.json
  locator: Independent RDKit native encoding and official external structure comparisons
  accessed_at: '2026-10-21T12:52:32Z'
  support: supports
  summary: Native SMILES and InChI agree on the full key, formula, charge, masses
    and fragment/stereochemical scope. Official external molecular comparisons described
    below preserve salts and configured stereochemistry.
  snapshot_sha256: 25bb891a2a3a7995b83fb6ad9c45f15dcb0261a0b321d2812cc3919ed23bad76
- evidence_id: search
  kind: search
  reference: 029-local-hits.txt; official source retrieval and original-paper follow-up
  locator: Ignored-inclusive local source/curation search; bounded official and primary-source
    discovery
  accessed_at: '2026-10-21T12:52:32Z'
  support: supports
  summary: Local searches included hidden and ignored files in the stated repository
    source/curation scope. Adopted citation leads were resolved separately from additional
    discovery. No claim of an exhaustive literature search is made.
  search_scope: Exact compound names/identifiers in conf, curation, data/raw, scripts
    and docs using rg --no-ignore --hidden; official registries and original-paper
    sources retrieved 2026-10-21.
  snapshot_sha256: d9a197c22e7a2a8497755404097bbdde15925d25a022cebdd7e38c3162d58d94
- evidence_id: identity
  kind: authority
  reference: CHEBI:81711; KEGG:C18372; KEGG:D07669
  locator: 288-chebi.json and both official KEGG molfiles/text; complete molecular
    comparison
  accessed_at: '2026-10-21T12:52:32Z'
  support: supports
  summary: 'All inspected molecular encodings give WDRFFJWBUDTUCA-UHFFFAOYSA-N, C26H38Cl2N10O4,
    charge zero and three components: one chlorhexidine plus two acetic-acid components
    in the standardized neutral representation. This encodes salt composition and
    does not assert neutral speciation in aqueous solution. The systematic 1:2 names
    agree. Nolvasan is correctly typed BRAND_NAME. CHEBI:59230 is the broader acetate-salt
    class; CHEBI:33282/35718 are antibacterial/antifungal roles. ChemSpider7838272
    was also retrieved directly; its standard InChI recomputes the same full key.
    The initial browser403 did not prevent a subsequent public-page retrieval.'
  snapshot_sha256: 62b3b75bf01f911e5a2c1d7d88bb8a52c9c8db926166325d03a0af4cbab74882
- evidence_id: discovery
  kind: primary_source
  reference: PMID:13172429; DOI:10.1111/j.1476-5381.1954.tb00840.x
  locator: Original 1954 five-page scanned article, pages 192–196; all five page images
    visually read
  accessed_at: '2026-10-21T12:52:32Z'
  support: supports
  summary: The original study distinguishes free-base structure 10,040 from diacetate
    and dihydrochloride. Diacetate was used almost entirely; selected in-vitro hydrochloride
    comparisons gave similar potency. The paper reports bacteriostatic dilution and
    bactericidal experiments with inoculum, pH, medium and egg-yolk neutralization
    effects. BHI/egg-yolk antagonism and condition-specific spore results preclude
    a universal kill claim. Old dilution endpoints are not converted into modern strain-specific
    mass MICs. These data directly support diacetate antibacterial activity, without
    asserting a measured bacterial protein target.
  snapshot_sha256: 5f113327cd4097bf08c583da7d5fc086702690768b68b4d102e5ba9c699f44ae
- evidence_id: adopted-leads
  kind: primary_source
  reference: PMID:19924977; 22058347; 22563792; 24815823; 28012407; 28468901; 28575994;
    28691453; 28727160; 29178741
  locator: 288-primary-abstracts.txt and 288-all-core.json; all ten complete original
    abstracts
  accessed_at: '2026-10-21T12:52:32Z'
  support: partial
  summary: Every adopted ChEBI lead was inspected. PMID19924977 reports P. aeruginosa
    transcriptional responses at 0.008 mM, not direct target binding. PMID22058347
    is a canine preputial disinfection study. PMID22563792 studies 7.5% cement formulations;
    24815823 is dentin bonding; 28012407 uses PLGA/chitosan plus bFGF; 28575994 combines
    silver nanoparticles with chlorhexidine acetate. PMID28691453 directly supports
    Candida albicans growth suppression in chlorhexidine-diacetate denture adhesive,
    with material/assay limits. PMID28727160 uses zinc-acetate/chlorhexidine mouthrinse.
    PMID28468901 has ambiguous title/abstract salt wording and cannot cleanly identify
    exact acetate efficacy. PMID29178741 found no reduction in biofilm microorganism
    counts from tested acetate-containing glass ionomer cements; this negative result
    is preserved. No formulation endpoint is silently treated as pure-compound MIC.
  snapshot_sha256: e256d989d736c2d9ce04df9a8f3155c80c6ec9b50057eaade49dc68da41fe3ed
- evidence_id: patents
  kind: primary_source
  reference: patent:EP2376129; patent:WO2012033625
  locator: Selected original patent definitions, formulation passages and examples
  accessed_at: '2026-10-21T12:52:32Z'
  support: context_only
  summary: Both document links concern chlorhexidine acetate formulations. EP2376129
    includes diacetate plus isopropanol cleaner experiments; WO2012033625 describes
    diacetate composition and medical-device cleaning formulations. These are document
    links, not exact molecule xrefs or blanket clinical efficacy claims. Selected
    passages were read, not a full legal/patent audit. The EP table has organism/count
    inconsistencies and is not adopted as a numeric assay source.
  snapshot_sha256: b9b1b078598a2c7a0b2443793c0f5780033a377b443c67927ea9669b066c99d5
- evidence_id: chemspider
  kind: authority
  reference: https://www.chemspider.com/Chemical-Structure.7838272.html
  locator: Complete JSON-LD standard InChI; 029-extra-chemistry.json
  accessed_at: '2026-10-21T12:57:15Z'
  support: supports
  summary: The exact current ChemSpider standard InChI reproduces the native diacetate
    key, three-component composition and formula.
  snapshot_sha256: b339050f8ee65725de1149e7b8eca6362f58b211edfc7ca358cb4ca2b0aed6a8
assessments:
- assessment_id: provenance
  area: provenance
  topic: Source ownership and history
  outcome: supported
  summary: Maintained source rows and owning extraction/seeding paths were inspected.
    Initial provenance hashes remain unchanged; source-only and experimental assertions
    are distinguished.
  target_ids:
  - CHEBI:81711
  evidence_ids:
  - native
  - owners
- assessment_id: validation
  area: schema
  topic: Focused documented gates
  outcome: supported
  summary: Schema and strict validation passed; independent native chemistry also
    passed. These checks do not establish biological truth or scientific REVIEWED
    status.
  target_ids:
  - CHEBI:81711
  evidence_ids:
  - chemistry
- assessment_id: identity
  area: identity
  topic: Exact diacetate composition and names
  outcome: supported
  summary: Native and inspected official encodings agree; six exact chemical names
    and one brand name have coherent scope. Acetate, gluconate and free base remain
    separate molecular records.
  target_ids:
  - CHEBI:81711
  evidence_ids:
  - native
  - identity
  - chemistry
- assessment_id: activity
  area: evidence
  topic: Antibacterial and antifungal classification
  outcome: supported
  summary: The original diacetate paper directly supports antibacterial activity.
    The adopted Candida adhesive study supports a bounded antifungal role at abstract
    depth. Effects are material-, organism- and assay-specific.
  target_ids:
  - CHEBI:81711
  evidence_ids:
  - discovery
  - adopted-leads
- assessment_id: xrefs
  area: grounding
  topic: Registry and document link scope
  outcome: unknown
  summary: CAS and exact KEGG/ChemSpider identities are corroborated by inspected
    official chemical records. DrugBank salt detail remains inaccessible and is only
    attested by current ChEBI. Both patent links are relevant documents.
  target_ids:
  - CHEBI:81711
  evidence_ids:
  - identity
  - patents
  - search
- assessment_id: mechanism
  area: completeness
  topic: Optional target and primary detail
  outcome: unknown
  summary: No target, mechanism enum, resistance, MIC, clinical-product assertion
    or causal graph is populated. Transcriptional response is not direct binding,
    and optional absence alone is not a defect.
  target_ids:
  - CHEBI:81711
  evidence_ids:
  - native
  - adopted-leads
  - discovery
findings: []
actions:
- action_id: A1
  description: Optionally add exact-material primary evidence after recovering full
    assay methods for the chosen endpoint.
  finding_ids: []
  target_ids:
  - CHEBI:81711
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/chlorhexidine-acetate.yaml
    role: Curator-owned evidence and activity assertions
  acceptance_checks:
  - Retain diacetate identity; distinguish formulated products, combinations, controls
    and negative results.
  - Record exact organism/strain, material concentration basis, medium, inoculum,
    incubation and endpoint before entering MICs.
  - Do not infer a direct antibacterial target from transcriptional changes or transfer
    gluconate/free-base experiments as exact diacetate assays.
  - Run documented native validators and applicable source/reference/history/corpus
    gates after any curation.
limitations:
- All ten adopted leads were read at complete original-abstract depth; full methods/tables
  were not inspected for those ten studies. The original 1954 discovery was independently
  read as all five page images.
- DrugBank salt detail was unavailable; the ChemSpider standard InChI was independently
  checked after a successful subsequent retrieval. CAS was not queried through a paid
  registry.
- Patent reading was limited to the stated composition/formulation/assay passages;
  no legal status assessment or unqualified formulation potency claim is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record, maintained input, scientific status or history was changed. This
  review is evidence for separately authorized curation, not status promotion.
- Root completed the entire native-record audit, preserved every captured input hash
  and inspected each adopted literature lead at the explicitly documented depth. Final
  saved conclusions retain all access, material, organism and assay boundaries.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
