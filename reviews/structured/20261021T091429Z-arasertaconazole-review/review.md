# Review of arasertaconazole

- Review: 20261021T091429Z-arasertaconazole-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:58:59Z
- Finished UTC: 2026-10-21T09:14:29Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The neutral R-enantiomer is chemically consistent and distinct from racemic sertaconazole and its nitrate salt. Exact-enantiomer patent assays and a completed phase 2 registry support antifungal development. Existing source-derived antibacterial classification and demethylase mechanism are not independently established by the inspected exact-compound experiments; native notes already flag this scope boundary. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire SEEDED record, complete adopted ChEBI row and both cited patents; exact stereochemistry, salt distinction, class and mechanism provenance, additional primary patent assays and trial results.

Selection: Path-ordered queue index 104; one exact record prepared before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:83685 | data/antibiotics/antibacterial/arasertaconazole.yaml | generated | arasertaconazole |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record LinkML validation | passed | True | CHEBI:83685 | Exit 0; no issues found. |
| Documented closed-schema validation | passed | True | CHEBI:83685 | Exit 0; one file and zero ERROR rows. |
| Native chemistry and supplemental exact source | passed | False | CHEBI:83685 | Exit 0; native SMILES/InChI, formula, mass, charge, mint and PubChem agree; one R center. |
| Current ChEBI assertions | passed | False | CHEBI:83685 | Exit 0; current parents, retained role strings, synonyms, structure and cross-reference strings agree. |
| Native structured source catalog before web research | passed | False | CHEBI:83685 | Exit 0; catalog has no fungal organism/dataset for the native ergosterol pathway claim. No component query is applicable. |
| Authoritative full QC | failed | True | CHEBI:83685 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:83685 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:83685 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:83685 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:83685 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:83685 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:83685 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:83685 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:83685 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### R free base versus nitrate and racemate

identity: supported. Targets: CHEBI:83685.

Native stereochemistry and chemistry are coherent; the patents explicitly distinguish the forms.

### Class provenance and exact bacterial scope

grounding: unknown. Targets: CHEBI:83685.

Current ChEBI supports the source mapping. Independent exact-R bacterial experiments were not established, and the native note already identifies that limit.

### Source-derived ergosterol pathway

evidence: unknown. Targets: CHEBI:83685.

Source roles support provenance; inspected exact-form primary assays establish fungal growth inhibition rather than direct enzyme binding. Host-shared qualifier is retained.

### Antifungal and clinical formulation scope

evidence: supported. Targets: CHEBI:83685.

Exact R-nitrate fungal assays and registered clinical investigation support antifungal use in the studied contexts, without converting grouped MICs into strain records or exposure into efficacy.

### Optional bounded enrichment

completeness: supported. Targets: CHEBI:83685.

Primary data can enrich evidence/discussions; empty optional fields alone are not defects.

### Structured-source applicability

scope: not_applicable. Targets: CHEBI:83685.

No fungal organism/dataset is available for this native pathway claim.

### Generated provenance and history

ownership: supported. Targets: CHEBI:83685.

Source ownership and six native history events remain intact.

### Focused validators

schema: supported. Targets: CHEBI:83685.

Both documented focused validators pass.

## Findings

### F1: Preserve exact-form and endpoint boundaries during optional enrichment

informational / open / confirmed; issue key: chebi-83685-arasertaconazole-exact-form-evidence-scope.

Useful exact-enantiomer primary evidence is available for fungal panels and nitrate-formulation clinical investigation. Native source-derived antibacterial filing and demethylase annotations remain explicitly qualified; no demonstrated false native chemical identity or required missing representation is established.

## Recommended Actions And Acceptance Checks

### A1

Optionally curate exact-form primary evidence and resolve the already-disclosed class/target uncertainty.

- Keep native R free-base identity; attach nitrate assays and clinical formulation findings with their salt scope, without replacing structure or borrowing racemate MICs.
- If defining clinical status more precisely, say investigated as nitrate for vulvovaginal candidiasis; do not infer approval, superiority or clinical cure from patent plasma exposure.
- Preserve grouped fungal geometric means and their 50% inhibition endpoint; they are not species/strain-resolved MICs. Do not treat the patent target-affinity assertion as a measured binding constant.
- Resolve exact-R antibacterial and direct target evidence before changing the generated class or upgrading source roles to PRIMARY_LITERATURE. Use maintained decisions/source ownership and reproducible regeneration for generated changes.
- Any separate curation must run native schema,strict,term,reference,history and required corpus gates; retain current SEEDED status until those requirements are met.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/arasertaconazole.yaml; Whole YAML including all six seed/reseed history entries | supports | Exact neutral R-enantiomer, four activity roles, source-derived ergosterol inhibition and explicit HOST_SHARED_TARGET warning. Native notes flag antifungal mechanism versus antibacterial filing; no curator-reviewed target, MIC, resistance or producer object is asserted. |
| inventory | data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/seed_from_sources.py; 104-chebi-row.json; class selection and mechanism notes generation | supports | Adopted row has no PMID citations. Both document links resolve to the formulation patent family. ChEBI antibacterial-drug role explains priority-based ANTIBACTERIAL filing; disagreement with fungal activity is already disclosed. Future generated changes belong to maintained source decisions and regeneration. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:83685; 104-ols.json;104-parents.json;104-role-*.json;104-source-check.json | supports | Current nonobsolete term, three chemical/drug parents and all four retained roles resolve. Antibacterial-drug role is a database assertion; it is not an exact-enantiomer bacterial experiment. Demethylase and ergosterol roles reproduce source provenance. CAS and Reaxys strings are corroborated but not independently registry-resolved. |
| chemistry | RDKit and PubChem CID 6604451; 104-chemistry.py;104-chemistry.json;104-pubchem.json | supports | Both native encodings give JLGKQTAYUIMGRK-IBGZPJMESA-N and one R center. Neutral C20H15Cl3N2OS matches formula, charge and mass. Supplemental PubChem exact structure agrees; nitrate formulation is a distinct chemical form. |
| formulation | patent:EP2436374; patent:WO2012041966; EP2436374A1 Description and Examples 1–3; WO2012041966A1 corresponding text;104-patent-ep.pdf p2 figure inspected | partial | Both cited patents concern the R-enantiomer mononitrate vaginal formulation. Their clinical example measures plasma concentrations by chiral HPLC, not microbial susceptibility or cure. The established marketed comparator described in the background is racemic sertaconazole nitrate. Higher exposure alone does not demonstrate superior clinical efficacy. |
| primary-assay | patent:US7323433B2; 104-patent-us.html Description, synthetic examples and Example 8/Table 1 | supports | The English patent identifies the R free base and nitrate separately. Its modified M27-A assays use nitrate enantiomers, RPMI with 2% glucose at pH 7 and a 50% growth endpoint. Geometric means favor R over the racemate across grouped fungal panels; Candida spp. (42 strains) is 0.125 versus 0.256 micrograms/ml. These are group means, not species/strain MICs or direct enzyme-affinity measurements. |
| trial | https://clinicaltrials.gov/study/NCT01144286; 104-trial.json protocol and posted outcome measures; EudraCT 2009-016655-21 | partial | Completed phase 2 study tested single vaginal nitrate doses in 229 participants. Day-26 composite clinical/mycological cure percentages were 31.7, 48.7, 47.6 and 53.8 for placebo,150,300 and600 mg. Prespecified dose-trend P=0.0630 did not reach alpha0.05. This is clinical investigation, not proof of routine approval or superiority. The record does not explicitly claim approval. |
| racemate | PMID:1627186; Complete PubMed abstract; In vitro activity of sertaconazole,1992 | context_only | The primary abstract reports fungal and Gram-positive activity of sertaconazole FI7045/CAS99592-32-2. That racemate result cannot supply exact R-enantiomer bacterial MICs or antibacterial mechanism. |
| literature | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=arasertaconazole&amp;format=json&amp;resultType=core&amp;pageSize=100; 104-literature.json; all nine returned indexed records/abstracts inspected | context_only | Two hits are the adopted patents. Other hits are topical-treatment or cholesterol reviews, computational target prediction, or unrelated compounds. PMID31404334 is computational target prediction, not direct arasertaconazole enzyme inhibition. No native PMID lead is awaiting disposition. |
| adapter | iModulonDB native structured source adapter; 104-imodulondb-datasets.txt | context_only | Catalog was inspected before open web research. It contains no applicable fungal dataset; this is not negative biological evidence. |
| validation | Native schema and strict commands; 104-strict.tsv | supports | Both documented per-record checks exited 0. No semantic identity or reference failure was found. |
| search | Ignored-inclusive local identity/source search; 104-local-hits.txt;104-inspect.json | context_only | One exact target resolved and all 13 captured source/context hashes rechecked unchanged. |

## Limits And Additional Notes

- No exact-enantiomer bacterial assay or direct enzyme-binding experiment was established in the inspected sources; this is a bounded search result, not a claim that such evidence cannot exist.
- Both adopted patent descriptions and examples were read. The EP structure page was visually inspected; no quantitative pharmacokinetic curve extraction was performed. Patent claims of clinical superiority are not accepted solely from plasma exposure.
- CAS and proprietary Reaxys identifiers were corroborated through ChEBI, not independently resolved in their registries. No current jurisdiction-wide approval determination was attempted.
- Native source-derived class and mechanism remain qualified. Required shared corpus gates are integrated by the coordinating reviewer; focused checks alone do not establish full native sign-off.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 13 initially captured hashes rechecked unchanged. No native record, history or saved review was edited.
- The adopted row contains no PMID leads. All nine broader literature-search records were inspected and classified; racemate studies were excluded as exact-enantiomer proof.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T091429Z-arasertaconazole-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of arasertaconazole
started_at: '2026-10-21T08:58:59Z'
finished_at: '2026-10-21T09:14:29Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: Exact R-enantiomer supported; antifungal evidence established, antibacterial
  classification and direct target scope remain qualified
scientific_review: true
summary: The neutral R-enantiomer is chemically consistent and distinct from racemic
  sertaconazole and its nitrate salt. Exact-enantiomer patent assays and a completed
  phase 2 registry support antifungal development. Existing source-derived antibacterial
  classification and demethylase mechanism are not independently established by the
  inspected exact-compound experiments; native notes already flag this scope boundary.
  Scientific assessment retains the stated evidence limits; full verification is blocked
  by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/arasertaconazole.yaml
    sha256: 4852617fc7d28f4803c097a1bccb50a02e52412e25ae65b9a3482958ad00fe94
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
scope:
  description: Entire SEEDED record, complete adopted ChEBI row and both cited patents;
    exact stereochemistry, salt distinction, class and mechanism provenance, additional
    primary patent assays and trial results.
  selection: Path-ordered queue index 104; one exact record prepared before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:83685
targets:
- target_id: CHEBI:83685
  path: data/antibiotics/antibacterial/arasertaconazole.yaml
  label: arasertaconazole
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
checks:
- check_id: schema
  name: Documented per-record LinkML validation
  status: passed
  required: true
  summary: Exit 0; no issues found.
  target_ids:
  - CHEBI:83685
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/arasertaconazole.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented closed-schema validation
  status: passed
  required: true
  summary: Exit 0; one file and zero ERROR rows.
  target_ids:
  - CHEBI:83685
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/arasertaconazole.yaml --out /private/tmp/am-review-session/104-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Native chemistry and supplemental exact source
  status: passed
  required: false
  summary: Exit 0; native SMILES/InChI, formula, mass, charge, mint and PubChem agree;
    one R center.
  target_ids:
  - CHEBI:83685
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/104-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: source-check
  name: Current ChEBI assertions
  status: passed
  required: false
  summary: Exit 0; current parents, retained role strings, synonyms, structure and
    cross-reference strings agree.
  target_ids:
  - CHEBI:83685
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/104-source-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chebi
- check_id: adapter
  name: Native structured source catalog before web research
  status: passed
  required: false
  summary: Exit 0; catalog has no fungal organism/dataset for the native ergosterol
    pathway claim. No component query is applicable.
  target_ids:
  - CHEBI:83685
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:83685
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
  - CHEBI:83685
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
  - CHEBI:83685
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
  - CHEBI:83685
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
  - CHEBI:83685
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
  - CHEBI:83685
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
  - CHEBI:83685
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
  - CHEBI:83685
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
  - CHEBI:83685
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/arasertaconazole.yaml
  locator: Whole YAML including all six seed/reseed history entries
  accessed_at: '2026-10-21T09:03:11Z'
  support: supports
  summary: Exact neutral R-enantiomer, four activity roles, source-derived ergosterol
    inhibition and explicit HOST_SHARED_TARGET warning. Native notes flag antifungal
    mechanism versus antibacterial filing; no curator-reviewed target, MIC, resistance
    or producer object is asserted.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/seed_from_sources.py
  locator: 104-chebi-row.json; class selection and mechanism notes generation
  accessed_at: '2026-10-21T09:03:11Z'
  support: supports
  summary: Adopted row has no PMID citations. Both document links resolve to the formulation
    patent family. ChEBI antibacterial-drug role explains priority-based ANTIBACTERIAL
    filing; disagreement with fungal activity is already disclosed. Future generated
    changes belong to maintained source decisions and regeneration.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:83685
  locator: 104-ols.json;104-parents.json;104-role-*.json;104-source-check.json
  accessed_at: '2026-10-21T09:03:11Z'
  support: supports
  summary: Current nonobsolete term, three chemical/drug parents and all four retained
    roles resolve. Antibacterial-drug role is a database assertion; it is not an exact-enantiomer
    bacterial experiment. Demethylase and ergosterol roles reproduce source provenance.
    CAS and Reaxys strings are corroborated but not independently registry-resolved.
  snapshot_sha256: b0e9b9a1a9a8936ba2faff0f1d3282c747e1b4c0f598735f8129a197bcdb4563
- evidence_id: chemistry
  kind: validation
  reference: RDKit and PubChem CID 6604451
  locator: 104-chemistry.py;104-chemistry.json;104-pubchem.json
  accessed_at: '2026-10-21T09:03:11Z'
  support: supports
  summary: Both native encodings give JLGKQTAYUIMGRK-IBGZPJMESA-N and one R center.
    Neutral C20H15Cl3N2OS matches formula, charge and mass. Supplemental PubChem exact
    structure agrees; nitrate formulation is a distinct chemical form.
  snapshot_sha256: 8a098cdab946b66b06116db19dae74dfaa03f19332ae1728b57b803e2f1d7158
- evidence_id: formulation
  kind: primary_source
  reference: patent:EP2436374; patent:WO2012041966
  locator: EP2436374A1 Description and Examples 1–3; WO2012041966A1 corresponding
    text;104-patent-ep.pdf p2 figure inspected
  accessed_at: '2026-10-21T09:03:11Z'
  support: partial
  summary: Both cited patents concern the R-enantiomer mononitrate vaginal formulation.
    Their clinical example measures plasma concentrations by chiral HPLC, not microbial
    susceptibility or cure. The established marketed comparator described in the background
    is racemic sertaconazole nitrate. Higher exposure alone does not demonstrate superior
    clinical efficacy.
  snapshot_sha256: b5e4264f705685745cdccc6cf85e0a87b1ff653e2658967abfcc5019f84489e7
- evidence_id: primary-assay
  kind: primary_source
  reference: patent:US7323433B2
  locator: 104-patent-us.html Description, synthetic examples and Example 8/Table
    1
  accessed_at: '2026-10-21T09:03:11Z'
  support: supports
  summary: The English patent identifies the R free base and nitrate separately. Its
    modified M27-A assays use nitrate enantiomers, RPMI with 2% glucose at pH 7 and
    a 50% growth endpoint. Geometric means favor R over the racemate across grouped
    fungal panels; Candida spp. (42 strains) is 0.125 versus 0.256 micrograms/ml.
    These are group means, not species/strain MICs or direct enzyme-affinity measurements.
  snapshot_sha256: ccb43618878c4aabcde59c3c8a1858f7e6abcf941078784789617a5b101877f2
- evidence_id: trial
  kind: primary_source
  reference: https://clinicaltrials.gov/study/NCT01144286
  locator: 104-trial.json protocol and posted outcome measures; EudraCT 2009-016655-21
  accessed_at: '2026-10-21T09:03:11Z'
  support: partial
  summary: Completed phase 2 study tested single vaginal nitrate doses in 229 participants.
    Day-26 composite clinical/mycological cure percentages were 31.7, 48.7, 47.6 and
    53.8 for placebo,150,300 and600 mg. Prespecified dose-trend P=0.0630 did not reach
    alpha0.05. This is clinical investigation, not proof of routine approval or superiority.
    The record does not explicitly claim approval.
  snapshot_sha256: 0a417c8fd90c5b90855e0a4595f684a77d2ef116b8256128c729a25baaff0cbb
- evidence_id: racemate
  kind: primary_source
  reference: PMID:1627186
  locator: Complete PubMed abstract; In vitro activity of sertaconazole,1992
  accessed_at: '2026-10-21T09:03:11Z'
  support: context_only
  summary: The primary abstract reports fungal and Gram-positive activity of sertaconazole
    FI7045/CAS99592-32-2. That racemate result cannot supply exact R-enantiomer bacterial
    MICs or antibacterial mechanism.
- evidence_id: literature
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=arasertaconazole&format=json&resultType=core&pageSize=100
  locator: 104-literature.json; all nine returned indexed records/abstracts inspected
  accessed_at: '2026-10-21T09:03:11Z'
  support: context_only
  summary: Two hits are the adopted patents. Other hits are topical-treatment or cholesterol
    reviews, computational target prediction, or unrelated compounds. PMID31404334
    is computational target prediction, not direct arasertaconazole enzyme inhibition.
    No native PMID lead is awaiting disposition.
  snapshot_sha256: 7ab3b5bbf8fc7b8fce0dcb673aa716a5f991473f66ef2d89a763b65f746c6542
- evidence_id: adapter
  kind: database
  reference: iModulonDB native structured source adapter
  locator: 104-imodulondb-datasets.txt
  accessed_at: '2026-10-21T09:03:11Z'
  support: context_only
  summary: Catalog was inspected before open web research. It contains no applicable
    fungal dataset; this is not negative biological evidence.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: validation
  kind: validation
  reference: Native schema and strict commands
  locator: 104-strict.tsv
  accessed_at: '2026-10-21T09:03:11Z'
  support: supports
  summary: Both documented per-record checks exited 0. No semantic identity or reference
    failure was found.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local identity/source search
  locator: 104-local-hits.txt;104-inspect.json
  accessed_at: '2026-10-21T09:03:11Z'
  support: context_only
  summary: One exact target resolved and all 13 captured source/context hashes rechecked
    unchanged.
  search_scope: prepare.py 104 used rg --no-ignore --hidden excluding .git/.venv;
    full native record and maintained row were read. Negative local findings are limited
    to paths searched with ignored files included.
assessments:
- assessment_id: identity
  area: identity
  topic: R free base versus nitrate and racemate
  outcome: supported
  summary: Native stereochemistry and chemistry are coherent; the patents explicitly
    distinguish the forms.
  target_ids:
  - CHEBI:83685
  evidence_ids:
  - chemistry
  - formulation
  - primary-assay
- assessment_id: grounding
  area: grounding
  topic: Class provenance and exact bacterial scope
  outcome: unknown
  summary: Current ChEBI supports the source mapping. Independent exact-R bacterial
    experiments were not established, and the native note already identifies that
    limit.
  target_ids:
  - CHEBI:83685
  evidence_ids:
  - chebi
  - inventory
  - racemate
- assessment_id: mechanism
  area: evidence
  topic: Source-derived ergosterol pathway
  outcome: unknown
  summary: Source roles support provenance; inspected exact-form primary assays establish
    fungal growth inhibition rather than direct enzyme binding. Host-shared qualifier
    is retained.
  target_ids:
  - CHEBI:83685
  evidence_ids:
  - record
  - chebi
  - primary-assay
  - literature
- assessment_id: activity
  area: evidence
  topic: Antifungal and clinical formulation scope
  outcome: supported
  summary: Exact R-nitrate fungal assays and registered clinical investigation support
    antifungal use in the studied contexts, without converting grouped MICs into strain
    records or exposure into efficacy.
  target_ids:
  - CHEBI:83685
  evidence_ids:
  - primary-assay
  - formulation
  - trial
- assessment_id: completeness
  area: completeness
  topic: Optional bounded enrichment
  outcome: supported
  summary: Primary data can enrich evidence/discussions; empty optional fields alone
    are not defects.
  target_ids:
  - CHEBI:83685
  evidence_ids:
  - primary-assay
  - trial
- assessment_id: adapter
  area: scope
  topic: Structured-source applicability
  outcome: not_applicable
  summary: No fungal organism/dataset is available for this native pathway claim.
  target_ids:
  - CHEBI:83685
  evidence_ids:
  - adapter
- assessment_id: ownership
  area: ownership
  topic: Generated provenance and history
  outcome: supported
  summary: Source ownership and six native history events remain intact.
  target_ids:
  - CHEBI:83685
  evidence_ids:
  - record
  - inventory
- assessment_id: schema
  area: schema
  topic: Focused validators
  outcome: supported
  summary: Both documented focused validators pass.
  target_ids:
  - CHEBI:83685
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: chebi-83685-arasertaconazole-exact-form-evidence-scope
  category: evidence
  severity: informational
  status: open
  certainty: confirmed
  title: Preserve exact-form and endpoint boundaries during optional enrichment
  description: Useful exact-enantiomer primary evidence is available for fungal panels
    and nitrate-formulation clinical investigation. Native source-derived antibacterial
    filing and demethylase annotations remain explicitly qualified; no demonstrated
    false native chemical identity or required missing representation is established.
  target_ids:
  - CHEBI:83685
  field_paths:
  - definition
  - antimicrobial_class
  - activity_roles
  - mode_of_action_notes
  - activity_spectrum
  - evidence
  - discussions
  evidence_ids:
  - record
  - chebi
  - formulation
  - primary-assay
  - trial
  - racemate
  rule_id: 'review-checklist: exact structure and claim-level evidence scope'
  native_severity: informational unresolved source scope and optional enrichment
  normalization_reason: The native record discloses source-derived mechanism and class
    uncertainty. Primary antifungal evidence does not disprove possible antibacterial
    activity, and optional evidence enrichment is not a mandatory-field defect.
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
    path: data/antibiotics/antibacterial/arasertaconazole.yaml
    role: Curator-owned evidence, discussions and biological annotations
actions:
- action_id: A1
  description: Optionally curate exact-form primary evidence and resolve the already-disclosed
    class/target uncertainty.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:83685
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
    path: data/antibiotics/antibacterial/arasertaconazole.yaml
    role: Curator-owned evidence, discussions and biological annotations
  acceptance_checks:
  - Keep native R free-base identity; attach nitrate assays and clinical formulation
    findings with their salt scope, without replacing structure or borrowing racemate
    MICs.
  - If defining clinical status more precisely, say investigated as nitrate for vulvovaginal
    candidiasis; do not infer approval, superiority or clinical cure from patent plasma
    exposure.
  - Preserve grouped fungal geometric means and their 50% inhibition endpoint; they
    are not species/strain-resolved MICs. Do not treat the patent target-affinity
    assertion as a measured binding constant.
  - Resolve exact-R antibacterial and direct target evidence before changing the generated
    class or upgrading source roles to PRIMARY_LITERATURE. Use maintained decisions/source
    ownership and reproducible regeneration for generated changes.
  - Any separate curation must run native schema,strict,term,reference,history and
    required corpus gates; retain current SEEDED status until those requirements are
    met.
limitations:
- No exact-enantiomer bacterial assay or direct enzyme-binding experiment was established
  in the inspected sources; this is a bounded search result, not a claim that such
  evidence cannot exist.
- Both adopted patent descriptions and examples were read. The EP structure page was
  visually inspected; no quantitative pharmacokinetic curve extraction was performed.
  Patent claims of clinical superiority are not accepted solely from plasma exposure.
- CAS and proprietary Reaxys identifiers were corroborated through ChEBI, not independently
  resolved in their registries. No current jurisdiction-wide approval determination
  was attempted.
- Native source-derived class and mechanism remain qualified. Required shared corpus
  gates are integrated by the coordinating reviewer; focused checks alone do not establish
  full native sign-off.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 13 initially captured hashes rechecked unchanged. No native record, history
  or saved review was edited.
- The adopted row contains no PMID leads. All nine broader literature-search records
  were inspected and classified; racemate studies were excluded as exact-enantiomer
  proof.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:83685
- https://patents.google.com/patent/EP2436374A1/en
- https://patents.google.com/patent/WO2012041966A1/en
- https://patents.google.com/patent/US7323433B2/en
- https://clinicaltrials.gov/study/NCT01144286
tags:
- record-review
- arasertaconazole
- enantiomer
- antifungal
- primary-evidence
```
