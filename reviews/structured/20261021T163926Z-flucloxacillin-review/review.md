# flucloxacillin: exact identity and primary-evidence boundaries

- Review: 20261021T163926Z-flucloxacillin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:12:24Z
- Finished UTC: 2026-10-21T16:39:26Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact neutral flucloxacillin graph and antibacterial eligibility are supported. The inherited PBP assertion is correctly marked as database evidence; a later original whole-cell competition study is a useful bounded enrichment lead. One minor brand-type inconsistency is confirmed.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position448; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:5098 | data/antibiotics/antibacterial/flucloxacillin.yaml | generated | flucloxacillin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:5098 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:5098 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:5098 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:5098 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:5098 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:5098 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:5098 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:5098 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:5098 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:5098 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:5098 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:5098 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact molecular representation

identity: supported. Targets: CHEBI:5098.

The native graph, formula C19H17ClFN3O5S, charge and mass agree across independent encodings. All penam stereocentres and the systematic chemical name agree.

### Chemical, drug and document groundings

grounding: concern. Targets: CHEBI:5098.

Exact PubChem, KEGG compound and ARO mappings agree. Reaxys and DrugBank remain limited-access gaps; drug_xrefs allow broader associations. The ARO floxapen spelling requires BRAND_NAME typing.

### Parents and antibacterial eligibility

scope: supported. Targets: CHEBI:5098.

Penicillin scaffold and penicillin-allergen parent are coherent with the graph and clinical/allergy sources; official product and original assays support antibacterial-drug use.

### Native target assertions and prospective mechanism

evidence: supported. Targets: CHEBI:5098.

The native PBP assertion is transparently database-level. The2022 whole-cell competition study supports a later species-qualified primary annotation if reagent form and exact target scope are resolved; no native update is made.

### Optional activity, resistance and producer enrichment

completeness: unknown. Targets: CHEBI:5098.

Quantitative enrichment must preserve sodium-monohydrate or unspecified commercial-powder preparation, assay format and strain. No absence of optional collections is a schema defect.

### Maintained sources and historical events

provenance: supported. Targets: CHEBI:5098.

The entire source rows and native seed/reseed histories were read; original hashes are preserved and actual additional owners captured. Authority updates do not silently rewrite historical provenance. No native or source file is edited.

### Actual checks

schema: supported. Targets: CHEBI:5098.

Focused native schema, strict and chemistry checks passed. Independent authority graph comparisons also passed. Shared required checks are attached at finalization, with their existing failure retained.

## Findings

### F1: The ARO floxapen synonym is typed as an exact chemical synonym

minor / open / confirmed; issue key: flucloxacillin-floxapen-brand-synonym-type.

The lowercase ARO floxapen is the same medicinal brand already correctly represented as Floxapen/BRAND_NAME from ChEBI. The official product record confirms the brand and sodium formulation. Correct the synonym type through the maintained owner without replacing neutral flucloxacillin with the product salt.

## Recommended Actions And Acceptance Checks

### A1

Classify the ARO-derived floxapen spelling as a brand through its maintained generator/owner.

- Retain exact neutral graph and other chemical synonyms.
- Make Floxapen case variants consistently BRAND_NAME and preserve source provenance.
- Regenerate and run schema, strict and corpus reproduction checks.

### A2

For optional enrichment, resolve exact experimental material and claim-level evidence before adding assertions.

- Retain database-level PBP status until a species/material-qualified original experiment is curated.
- Separate growth MIC, whole-cell PBP competition IC50, serum binding and clinical exposure; preserve salt/potency basis.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/flucloxacillin.yaml; Entire native YAML, all names, groundings, classifications and history events | supports | The complete SEEDED/EXACT record CHEBI:5098 was read. One taxon-unspecified PBP target carries PRIMARY_EVIDENCE_NEEDED. No quantitative susceptibility, resistance or causal graph is asserted. The ChEBI Floxapen synonym is BRAND_NAME while the ARO lowercase spelling is EXACT_SYNONYM. |
| owners | 448-source-rows.json; Exact maintained source rows, readiness pointer and expanded capture | supports | All original thirteen input hashes are preserved within 17 captured inputs. ChEBI row165 and ARO row136 supply the identity, names, roles and eight combined adopted PMID leads; the actual target inventory and role configuration explain the PBP assertion. |
| local | 448-local-hits.txt; Ignored- and hidden-inclusive local identity and owner search | context_only | The complete search included ignored and hidden files. Exact maintained rows and generated annotations were inspected. No additional exact curator override was identified in this bounded repository search; this does not establish global evidence absence. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/5098/; Current full compound export: graph, names, roles, origins, parent relationships and accessions | supports | Current ChEBI reproduces the native graph, formula C19H17ClFN3O5S, zero net charge and key UIOFUWFRIANQPC-JKIFEVAISA-N. Source agreement is recorded separately from primary biological evidence. |
| chemistry | 448-authority-chemistry.json; Independent native/current ChEBI molfile and PubChem graph comparison | supports | Native SMILES and InChI, ChEBI SMILES and molfile, and PubChem SMILES and InChI all give UIOFUWFRIANQPC-JKIFEVAISA-N, formula C19H17ClFN3O5S and charge zero. KEGG C11748 molfile also agrees. All three penam stereocentres agree with the systematic (2S,5R,6R) name. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/UIOFUWFRIANQPC-JKIFEVAISA-N/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; Current PubChem structure properties | supports | The independently parsed structure agrees with the exact native graph and mass/formula. CID21319 is the native exact link. |
| term-17334 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/17334/; Current asserted class or role definition | supports | CHEBI:17334 resolves as penicillin. The term was assessed against the native graph or original activity/product evidence. |
| term-88187 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/88187/; Current asserted class or role definition | supports | CHEBI:88187 resolves as penicillin allergen. The term was assessed against the native graph or original activity/product evidence. |
| term-33281 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33281/; Current asserted class or role definition | supports | CHEBI:33281 resolves as antimicrobial agent. The term was assessed against the native graph or original activity/product evidence. |
| term-36047 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/36047/; Current asserted class or role definition | supports | CHEBI:36047 resolves as antibacterial drug. The term was assessed against the native graph or original activity/product evidence. |
| gates | 448-focused-results.json; Executed native schema, strict and chemical checks | supports | All focused checks passed on the untouched native record. Structural checks do not replace primary biological evidence. |
| adapter | iModulonDB; Actual pre-follow-up catalog and relevant bacterial query | context_only | The structured catalog completed. The s_aureus/staph_precise108 PBP query returned seven gene-name matches and no iModulons; these are discovery context, not drug binding. No S. pneumoniae dataset was substituted from another species. |
| aro | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FARO_3000636; Current ARO identity through OLS | supports | ARO3000636 is flucloxacillin and repeats CAS5250-39-5, CHEBI5098 and PubChem21319. Its penicillin class is coherent. An initial numeric CARD page resolved to unrelated OXA-229 and was discarded; direct ARO-style CARD routes returned404. The exact OLS term, not those failed routes, supports the mapping. |
| aro-target | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FARO_3000749; Current ARO PBP target definition | supports | The target is beta-lactam sensitive penicillin-binding protein. Its generic numbering explicitly refers to E. coli and varies among species. The native assertion remains database-level, without an invented organism, strain or primary binding experiment. |
| product | https://www.geneesmiddeleninformatiebank.nl/smpc/h05990_smpc.pdf; Current official Dutch RVG05990 SmPC, sections1,2 and4.1 | supports | Floxapen is the named injectable medicinal product containing flucloxacillin as its sodium salt. The indication and product identity support antibacterial-drug use and confirm that Floxapen/floxapen is a brand name. This formulation does not replace the neutral native formula. |
| original1970 | https://doi.org/10.1136/bmj.4.5733.455; PMID5481218 / PMC1820086; original scanned pages455–460, OCR main prose | supports | The original uses flucloxacillin sodium monohydrate and distinguishes it from oxacillin, cloxacillin and dicloxacillin. Growth inhibition, bactericidal observations, serum binding and healthy-volunteer exposure are separate endpoints. MICs were measured in stated nutrient media at37C/24h, with blood supplements for selected taxa. Penicillinase-producing and methicillin-resistant staphylococci are distinct populations. No table values are imported into the neutral graph; the scans and OCR are not used to infer uninspected numeric cells. |
| pbp2022 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9115913/; PMID35218689; original relevant Introduction, penicillin Results, exact Table1 row, growth/material and titration Methods | supports | MilliporeSigma flucloxacillin powder was tested in whole cells of unencapsulated S. pneumoniae D39 derivative IU1945, followed by Bocillin-FL competition and gel readout. Table1 reports PBP2x IC50 0.832±0.323µM and PBP3 0.911±0.252µM; growth MIC is separately1.00µM. PBP3 labeling does not itself explain lethality. This is primary target-occupancy evidence with explicit strain and whole-cell context, not purified-protein affinity or E. coli numbering. Exact isolated salt/catalogue/purity is not supplied in the inspected materials; supplementary raw gels were not inspected. |
| links | https://rest.kegg.jp/get/C11748; KEGG compound C11748, KEGG drug D04196, DrugCentral1183 card and document routing | supports | C11748 chemical molfile agrees exactly; D04196 and DrugCentral1183 resolve to flucloxacillin under the broader drug_xrefs semantics. DrugBankDB00301 public access returned403 and the attempted DrugCentral SDF route404, so their underlying exact encodings are not independently certified. Wikipedia resolves as a document. Reaxys4771988 is cross-listed but its registry graph was not independently inspected. |
| lead-12569987 | https://pubmed.ncbi.nlm.nih.gov/12569987/; Complete indexed original abstract/metadata; deeper reading only where separately recorded | context_only | Original allergen study abstract concerns benzylpenicillin/cephalothin determinants; it is not direct flucloxacillin-PBP evidence. |
| lead-15773973 | https://pubmed.ncbi.nlm.nih.gov/15773973/; Complete indexed original abstract/metadata; deeper reading only where separately recorded | context_only | Original case report abstract describes aplastic anemia/liver failure after flucloxacillin; supports adverse-reaction context, not a bacterial target. |
| lead-23032409 | https://pubmed.ncbi.nlm.nih.gov/23032409/; Complete indexed original abstract/metadata; deeper reading only where separately recorded | context_only | HIV/HLA-B5701 retrospective safety report metadata and abstract scope, not efficacy or direct binding. |
| lead-23542420 | https://pubmed.ncbi.nlm.nih.gov/23542420/; Complete indexed original abstract/metadata; deeper reading only where separately recorded | context_only | Systematic review abstract found no eligible RCT for the specified ED monotherapy/dual comparison; no combination benefit is inferred. |
| lead-25998949 | https://pubmed.ncbi.nlm.nih.gov/25998949/; Complete indexed original abstract/metadata; deeper reading only where separately recorded | context_only | Original amoxicillin/clavulanate T-cell liver-injury work concerns different agents and is not transferred to flucloxacillin. |
| lead-29017833 | https://pubmed.ncbi.nlm.nih.gov/29017833/; Complete indexed original abstract/metadata; deeper reading only where separately recorded | context_only | Beta-lactam allergy review abstract is secondary context, not an exact original target experiment. |
| lead-5481218 | https://pubmed.ncbi.nlm.nih.gov/5481218/; Complete indexed original abstract/metadata; deeper reading only where separately recorded | context_only | Original1970 comparison; full scanned main prose inspected separately with sodium-monohydrate preparation boundaries. |
| lead-3588519 | https://pubmed.ncbi.nlm.nih.gov/3588519/; Complete indexed original abstract/metadata; deeper reading only where separately recorded | context_only | Original pediatric dicloxacillin/flucloxacillin oral-liquid pharmacokinetics abstract; the adopted ARO citation is not itself structural elucidation or PBP binding. |

## Limits And Additional Notes

- Review is bounded to the inspected original material, current authority exports and explicit local search; no global evidence absence is asserted.
- Optional absent schema fields are not treated as defects. No native, maintained source or previously saved review is edited.
- The1970 scanned main prose was read through OCR; numerical tables were not independently transcribed or normalized. The original material is sodium monohydrate.
- The2022 relevant primary main methods/results and exact Table1 row were read; supplementary gels and an exact commercial salt certificate were not inspected.
- Seven ChEBI leads and one ARO lead were read at complete indexed abstract/metadata depth, with deeper1970 reading separately stated. DrugBank403, Reaxys registry access and an unsuccessful DrugCentral SDF route remain bounded.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Native curation status remains SEEDED. This review records evidence boundaries without changing the record.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T163926Z-flucloxacillin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'flucloxacillin: exact identity and primary-evidence boundaries'
started_at: '2026-10-21T16:12:24Z'
finished_at: '2026-10-21T16:39:26Z'
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
summary: The exact neutral flucloxacillin graph and antibacterial eligibility are
  supported. The inherited PBP assertion is correctly marked as database evidence;
  a later original whole-cell competition study is a useful bounded enrichment lead.
  One minor brand-type inconsistency is confirmed.
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
  - path: data/antibiotics/antibacterial/flucloxacillin.yaml
    sha256: 26dcc8ad4a40b0561e36aca5634fffba8f56816294daaca568a3661ba258b670
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
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
targets:
- target_id: CHEBI:5098
  path: data/antibiotics/antibacterial/flucloxacillin.yaml
  label: flucloxacillin
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
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO class, additional names and reference leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Actual qualified PBP target assertion
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target type and relation mapping
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position448; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:5098
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:5098
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    448
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:5098
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/flucloxacillin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:5098
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/flucloxacillin.yaml --out /private/tmp/am-review-session/448-strict.tsv
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
  - CHEBI:5098
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
  - CHEBI:5098
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
  - CHEBI:5098
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
  - CHEBI:5098
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
  - CHEBI:5098
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
  - CHEBI:5098
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
  - CHEBI:5098
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
  - CHEBI:5098
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
  - CHEBI:5098
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/flucloxacillin.yaml
  locator: Entire native YAML, all names, groundings, classifications and history
    events
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: The complete SEEDED/EXACT record CHEBI:5098 was read. One taxon-unspecified
    PBP target carries PRIMARY_EVIDENCE_NEEDED. No quantitative susceptibility, resistance
    or causal graph is asserted. The ChEBI Floxapen synonym is BRAND_NAME while the
    ARO lowercase spelling is EXACT_SYNONYM.
- evidence_id: owners
  kind: record_content
  reference: 448-source-rows.json
  locator: Exact maintained source rows, readiness pointer and expanded capture
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: All original thirteen input hashes are preserved within 17 captured inputs.
    ChEBI row165 and ARO row136 supply the identity, names, roles and eight combined
    adopted PMID leads; the actual target inventory and role configuration explain
    the PBP assertion.
  snapshot_sha256: a66488f6cf535d84e408be56e9f28f9bb52048ed43b0c8a27b0772ed6af3c48f
- evidence_id: local
  kind: search
  reference: 448-local-hits.txt
  locator: Ignored- and hidden-inclusive local identity and owner search
  accessed_at: '2026-10-21T16:24:41Z'
  support: context_only
  summary: The complete search included ignored and hidden files. Exact maintained
    rows and generated annotations were inspected. No additional exact curator override
    was identified in this bounded repository search; this does not establish global
    evidence absence.
  search_scope: rg --no-ignore --hidden exact flucloxacillin name, identifier and
    source mint in own batch045 checkout, excluding Git metadata and virtual environment
  snapshot_sha256: 1a35a351d9adb85c85c2d8470e9e8af0a05b5011f1d1c6acc3494ccdaf952333
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/5098/
  locator: 'Current full compound export: graph, names, roles, origins, parent relationships
    and accessions'
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: Current ChEBI reproduces the native graph, formula C19H17ClFN3O5S, zero
    net charge and key UIOFUWFRIANQPC-JKIFEVAISA-N. Source agreement is recorded separately
    from primary biological evidence.
  snapshot_sha256: 5401fa8e6f1faf861e28cf1908151d4e4f177782feb32a7f04a87db44b70499c
- evidence_id: chemistry
  kind: record_content
  reference: 448-authority-chemistry.json
  locator: Independent native/current ChEBI molfile and PubChem graph comparison
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: Native SMILES and InChI, ChEBI SMILES and molfile, and PubChem SMILES and
    InChI all give UIOFUWFRIANQPC-JKIFEVAISA-N, formula C19H17ClFN3O5S and charge
    zero. KEGG C11748 molfile also agrees. All three penam stereocentres agree with
    the systematic (2S,5R,6R) name.
  snapshot_sha256: 78fcecc44809b5a1850cdbe74f53690c65ad25f40bbb0ee7aac0c03ff9de7206
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/UIOFUWFRIANQPC-JKIFEVAISA-N/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: Current PubChem structure properties
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: The independently parsed structure agrees with the exact native graph and
    mass/formula. CID21319 is the native exact link.
  snapshot_sha256: 09a33f0a53e4a94d20cabdb372911157faf1783a5c06922cf4784f47b9a2f7ab
- evidence_id: term-17334
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/17334/
  locator: Current asserted class or role definition
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: CHEBI:17334 resolves as penicillin. The term was assessed against the native
    graph or original activity/product evidence.
  snapshot_sha256: da5e4c1011949f2c38dc273d8cdb520c11a08a4673eb7ed63095ba751645785d
- evidence_id: term-88187
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/88187/
  locator: Current asserted class or role definition
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: CHEBI:88187 resolves as penicillin allergen. The term was assessed against
    the native graph or original activity/product evidence.
  snapshot_sha256: 394e677c32790883ec0e7b7a721edaeaa60f6e22edc2364cb92e0ce1d2c3210c
- evidence_id: term-33281
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33281/
  locator: Current asserted class or role definition
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: CHEBI:33281 resolves as antimicrobial agent. The term was assessed against
    the native graph or original activity/product evidence.
  snapshot_sha256: 0f66df822d1a825c02531f80cc0fcc12783ac72a0c2f0482a9d9018db0dba9e1
- evidence_id: term-36047
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/36047/
  locator: Current asserted class or role definition
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: CHEBI:36047 resolves as antibacterial drug. The term was assessed against
    the native graph or original activity/product evidence.
  snapshot_sha256: cd02b5e95a759d9be8d1b3a51657d5d536a2f53d43647448b69caf4de6bd737f
- evidence_id: gates
  kind: record_content
  reference: 448-focused-results.json
  locator: Executed native schema, strict and chemical checks
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: All focused checks passed on the untouched native record. Structural checks
    do not replace primary biological evidence.
  snapshot_sha256: 3b34d1046fa8d8c4954f7acd6ce4cfbb5c4282c6b18f41e5b3d86473d43e236b
- evidence_id: adapter
  kind: database
  reference: iModulonDB
  locator: Actual pre-follow-up catalog and relevant bacterial query
  accessed_at: '2026-10-21T16:24:41Z'
  support: context_only
  summary: The structured catalog completed. The s_aureus/staph_precise108 PBP query
    returned seven gene-name matches and no iModulons; these are discovery context,
    not drug binding. No S. pneumoniae dataset was substituted from another species.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: aro
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FARO_3000636
  locator: Current ARO identity through OLS
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: ARO3000636 is flucloxacillin and repeats CAS5250-39-5, CHEBI5098 and PubChem21319.
    Its penicillin class is coherent. An initial numeric CARD page resolved to unrelated
    OXA-229 and was discarded; direct ARO-style CARD routes returned404. The exact
    OLS term, not those failed routes, supports the mapping.
  snapshot_sha256: ceae330135e93f58aea69eca5f9195bd9de268af6702d86eca8abb634ba97c06
- evidence_id: aro-target
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FARO_3000749
  locator: Current ARO PBP target definition
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: The target is beta-lactam sensitive penicillin-binding protein. Its generic
    numbering explicitly refers to E. coli and varies among species. The native assertion
    remains database-level, without an invented organism, strain or primary binding
    experiment.
  snapshot_sha256: 8383af4f759423090e605adc35109d468b3b809f7328a7fc8368188dac9eb2c1
- evidence_id: product
  kind: authority
  reference: https://www.geneesmiddeleninformatiebank.nl/smpc/h05990_smpc.pdf
  locator: Current official Dutch RVG05990 SmPC, sections1,2 and4.1
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: Floxapen is the named injectable medicinal product containing flucloxacillin
    as its sodium salt. The indication and product identity support antibacterial-drug
    use and confirm that Floxapen/floxapen is a brand name. This formulation does
    not replace the neutral native formula.
  snapshot_sha256: bfb8a2fd18df33ba8794b8b7af25d14a496353b4986e47151a6bb60ddefec26d
- evidence_id: original1970
  kind: primary_source
  reference: https://doi.org/10.1136/bmj.4.5733.455
  locator: PMID5481218 / PMC1820086; original scanned pages455–460, OCR main prose
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: The original uses flucloxacillin sodium monohydrate and distinguishes it
    from oxacillin, cloxacillin and dicloxacillin. Growth inhibition, bactericidal
    observations, serum binding and healthy-volunteer exposure are separate endpoints.
    MICs were measured in stated nutrient media at37C/24h, with blood supplements
    for selected taxa. Penicillinase-producing and methicillin-resistant staphylococci
    are distinct populations. No table values are imported into the neutral graph;
    the scans and OCR are not used to infer uninspected numeric cells.
  snapshot_sha256: 46e5667cf3b22bbf231ece78077ced22cf2115f8578c0e2ed316b40344d43618
- evidence_id: pbp2022
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC9115913/
  locator: PMID35218689; original relevant Introduction, penicillin Results, exact
    Table1 row, growth/material and titration Methods
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: MilliporeSigma flucloxacillin powder was tested in whole cells of unencapsulated
    S. pneumoniae D39 derivative IU1945, followed by Bocillin-FL competition and gel
    readout. Table1 reports PBP2x IC50 0.832±0.323µM and PBP3 0.911±0.252µM; growth
    MIC is separately1.00µM. PBP3 labeling does not itself explain lethality. This
    is primary target-occupancy evidence with explicit strain and whole-cell context,
    not purified-protein affinity or E. coli numbering. Exact isolated salt/catalogue/purity
    is not supplied in the inspected materials; supplementary raw gels were not inspected.
  snapshot_sha256: eceae4c2dd2cbe767510fb45b7109a1953f3bcd5dac82cb4e51b03e71cc8db6a
- evidence_id: links
  kind: authority
  reference: https://rest.kegg.jp/get/C11748
  locator: KEGG compound C11748, KEGG drug D04196, DrugCentral1183 card and document
    routing
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: C11748 chemical molfile agrees exactly; D04196 and DrugCentral1183 resolve
    to flucloxacillin under the broader drug_xrefs semantics. DrugBankDB00301 public
    access returned403 and the attempted DrugCentral SDF route404, so their underlying
    exact encodings are not independently certified. Wikipedia resolves as a document.
    Reaxys4771988 is cross-listed but its registry graph was not independently inspected.
  snapshot_sha256: c0630b1c6e161d64c6be340379f624d9e2eb050e2bb443062a313d300efe3d40
- evidence_id: lead-12569987
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/12569987/
  locator: Complete indexed original abstract/metadata; deeper reading only where
    separately recorded
  accessed_at: '2026-10-21T16:24:41Z'
  support: context_only
  summary: Original allergen study abstract concerns benzylpenicillin/cephalothin
    determinants; it is not direct flucloxacillin-PBP evidence.
  snapshot_sha256: d8430ea8588a8265f1686176e3cc466dc3492bb9c5e477e96d0bfa4aea2f673b
- evidence_id: lead-15773973
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/15773973/
  locator: Complete indexed original abstract/metadata; deeper reading only where
    separately recorded
  accessed_at: '2026-10-21T16:24:41Z'
  support: context_only
  summary: Original case report abstract describes aplastic anemia/liver failure after
    flucloxacillin; supports adverse-reaction context, not a bacterial target.
  snapshot_sha256: d8430ea8588a8265f1686176e3cc466dc3492bb9c5e477e96d0bfa4aea2f673b
- evidence_id: lead-23032409
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/23032409/
  locator: Complete indexed original abstract/metadata; deeper reading only where
    separately recorded
  accessed_at: '2026-10-21T16:24:41Z'
  support: context_only
  summary: HIV/HLA-B5701 retrospective safety report metadata and abstract scope,
    not efficacy or direct binding.
  snapshot_sha256: d8430ea8588a8265f1686176e3cc466dc3492bb9c5e477e96d0bfa4aea2f673b
- evidence_id: lead-23542420
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/23542420/
  locator: Complete indexed original abstract/metadata; deeper reading only where
    separately recorded
  accessed_at: '2026-10-21T16:24:41Z'
  support: context_only
  summary: Systematic review abstract found no eligible RCT for the specified ED monotherapy/dual
    comparison; no combination benefit is inferred.
  snapshot_sha256: d8430ea8588a8265f1686176e3cc466dc3492bb9c5e477e96d0bfa4aea2f673b
- evidence_id: lead-25998949
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/25998949/
  locator: Complete indexed original abstract/metadata; deeper reading only where
    separately recorded
  accessed_at: '2026-10-21T16:24:41Z'
  support: context_only
  summary: Original amoxicillin/clavulanate T-cell liver-injury work concerns different
    agents and is not transferred to flucloxacillin.
  snapshot_sha256: d8430ea8588a8265f1686176e3cc466dc3492bb9c5e477e96d0bfa4aea2f673b
- evidence_id: lead-29017833
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/29017833/
  locator: Complete indexed original abstract/metadata; deeper reading only where
    separately recorded
  accessed_at: '2026-10-21T16:24:41Z'
  support: context_only
  summary: Beta-lactam allergy review abstract is secondary context, not an exact
    original target experiment.
  snapshot_sha256: d8430ea8588a8265f1686176e3cc466dc3492bb9c5e477e96d0bfa4aea2f673b
- evidence_id: lead-5481218
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/5481218/
  locator: Complete indexed original abstract/metadata; deeper reading only where
    separately recorded
  accessed_at: '2026-10-21T16:24:41Z'
  support: context_only
  summary: Original1970 comparison; full scanned main prose inspected separately with
    sodium-monohydrate preparation boundaries.
  snapshot_sha256: d8430ea8588a8265f1686176e3cc466dc3492bb9c5e477e96d0bfa4aea2f673b
- evidence_id: lead-3588519
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/3588519/
  locator: Complete indexed original abstract/metadata; deeper reading only where
    separately recorded
  accessed_at: '2026-10-21T16:24:41Z'
  support: context_only
  summary: Original pediatric dicloxacillin/flucloxacillin oral-liquid pharmacokinetics
    abstract; the adopted ARO citation is not itself structural elucidation or PBP
    binding.
  snapshot_sha256: efc7a3ac45286d1e10d68da413b9c07dc0ffeb840088ddc1935e9d7350e80b4b
assessments:
- assessment_id: identity
  area: identity
  topic: Exact molecular representation
  outcome: supported
  summary: The native graph, formula C19H17ClFN3O5S, charge and mass agree across
    independent encodings. All penam stereocentres and the systematic chemical name
    agree.
  target_ids:
  - CHEBI:5098
  evidence_ids:
  - native
  - chebi
  - chemistry
  - pubchem
- assessment_id: grounding
  area: grounding
  topic: Chemical, drug and document groundings
  outcome: concern
  summary: Exact PubChem, KEGG compound and ARO mappings agree. Reaxys and DrugBank
    remain limited-access gaps; drug_xrefs allow broader associations. The ARO floxapen
    spelling requires BRAND_NAME typing.
  target_ids:
  - CHEBI:5098
  evidence_ids:
  - native
  - chebi
  - chemistry
  - product
  - aro
  - links
- assessment_id: classification
  area: scope
  topic: Parents and antibacterial eligibility
  outcome: supported
  summary: Penicillin scaffold and penicillin-allergen parent are coherent with the
    graph and clinical/allergy sources; official product and original assays support
    antibacterial-drug use.
  target_ids:
  - CHEBI:5098
  evidence_ids:
  - term-17334
  - term-88187
  - term-33281
  - term-36047
  - original1970
  - product
  - lead-29017833
- assessment_id: mechanism
  area: evidence
  topic: Native target assertions and prospective mechanism
  outcome: supported
  summary: The native PBP assertion is transparently database-level. The2022 whole-cell
    competition study supports a later species-qualified primary annotation if reagent
    form and exact target scope are resolved; no native update is made.
  target_ids:
  - CHEBI:5098
  evidence_ids:
  - native
  - adapter
  - aro-target
  - pbp2022
- assessment_id: completeness
  area: completeness
  topic: Optional activity, resistance and producer enrichment
  outcome: unknown
  summary: Quantitative enrichment must preserve sodium-monohydrate or unspecified
    commercial-powder preparation, assay format and strain. No absence of optional
    collections is a schema defect.
  target_ids:
  - CHEBI:5098
  evidence_ids:
  - native
  - local
  - original1970
  - pbp2022
- assessment_id: provenance
  area: provenance
  topic: Maintained sources and historical events
  outcome: supported
  summary: The entire source rows and native seed/reseed histories were read; original
    hashes are preserved and actual additional owners captured. Authority updates
    do not silently rewrite historical provenance. No native or source file is edited.
  target_ids:
  - CHEBI:5098
  evidence_ids:
  - native
  - owners
  - local
  - gates
- assessment_id: validation
  area: schema
  topic: Actual checks
  outcome: supported
  summary: Focused native schema, strict and chemistry checks passed. Independent
    authority graph comparisons also passed. Shared required checks are attached at
    finalization, with their existing failure retained.
  target_ids:
  - CHEBI:5098
  evidence_ids:
  - gates
  - chemistry
findings:
- finding_id: F1
  issue_key: flucloxacillin-floxapen-brand-synonym-type
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: The ARO floxapen synonym is typed as an exact chemical synonym
  description: The lowercase ARO floxapen is the same medicinal brand already correctly
    represented as Floxapen/BRAND_NAME from ChEBI. The official product record confirms
    the brand and sodium formulation. Correct the synonym type through the maintained
    owner without replacing neutral flucloxacillin with the product salt.
  target_ids:
  - CHEBI:5098
  field_paths:
  - synonyms[10].synonym_type
  evidence_ids:
  - native
  - owners
  - product
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO class, additional names and reference leads
  rule_id: review-checklist:Identity/Synonyms
  native_severity: minor
  normalization_reason: Localized source-dependent synonym typing; the native molecular
    identity is otherwise coherent.
actions:
- action_id: A1
  description: Classify the ARO-derived floxapen spelling as a brand through its maintained
    generator/owner.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:5098
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO class, additional names and reference leads
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Retain exact neutral graph and other chemical synonyms.
  - Make Floxapen case variants consistently BRAND_NAME and preserve source provenance.
  - Regenerate and run schema, strict and corpus reproduction checks.
- action_id: A2
  description: For optional enrichment, resolve exact experimental material and claim-level
    evidence before adding assertions.
  finding_ids: []
  target_ids:
  - CHEBI:5098
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
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO class, additional names and reference leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Actual qualified PBP target assertion
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target type and relation mapping
  acceptance_checks:
  - Retain database-level PBP status until a species/material-qualified original experiment
    is curated.
  - Separate growth MIC, whole-cell PBP competition IC50, serum binding and clinical
    exposure; preserve salt/potency basis.
limitations:
- Review is bounded to the inspected original material, current authority exports
  and explicit local search; no global evidence absence is asserted.
- Optional absent schema fields are not treated as defects. No native, maintained
  source or previously saved review is edited.
- The1970 scanned main prose was read through OCR; numerical tables were not independently
  transcribed or normalized. The original material is sodium monohydrate.
- The2022 relevant primary main methods/results and exact Table1 row were read; supplementary
  gels and an exact commercial salt certificate were not inspected.
- Seven ChEBI leads and one ARO lead were read at complete indexed abstract/metadata
  depth, with deeper1970 reading separately stated. DrugBank403, Reaxys registry access
  and an unsuccessful DrugCentral SDF route remain bounded.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Native curation status remains SEEDED. This review records evidence boundaries without
  changing the record.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
