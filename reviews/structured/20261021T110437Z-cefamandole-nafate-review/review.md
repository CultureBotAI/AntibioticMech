# Review cefamandole nafate identity, prodrug evidence and FDA history

- Review: 20261021T110437Z-cefamandole-nafate-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:44:47Z
- Finished UTC: 2026-10-21T11:04:37Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The sodium O-formyl cefamandole prodrug is structurally coherent. Primary experiments show conversion to cefamandole and assay-dependent antibacterial activity. One major current-status defect remains: the undated APPROVED summary overlooks official withdrawal of both cited US applications, although the original approval history and discontinued marketing flags are accurate.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position209; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3481 | data/antibiotics/antibacterial/cefamandole-nafate.yaml | generated | cefamandole nafate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:3481 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:3481 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:3481 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:3481 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3481 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3481 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3481 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3481 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3481 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3481 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3481 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3481 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact sodium form

identity: supported. Targets: CHEBI:3481.

The native graph, formula, charge, stereo descriptors and source mint agree with current ChEBI, PubChem and independently parsed KEGG. The sodium salt must remain distinct from the neutral acid, other counterions and the O-formyl prodrug.

### Parent, role and definition

grounding: supported. Targets: CHEBI:3481.

The organic sodium salt parent and antibacterial-drug role fit the graph and primary pharmacological context. Broad classification does not substitute for exact material or current clinical status.

### Maintained ownership and seed history

provenance: supported. Targets: CHEBI:3481.

Source concept and dated seed history are coherent. Review-only output preserves native status and original hashes; proposed fixes or enrichment belong to maintained owners.

### Unpopulated scientific domains

completeness: supported. Targets: CHEBI:3481.

Absent optional producer, target, causal graph or activity fields are not defects by themselves. Any additions require exact material, strain, endpoint and evidence scope.

### Focused checks

schema: supported. Targets: CHEBI:3481.

Schema and strict checks pass in batch021. Independent chemistry used the existing batch019 RDKit interpreter against unchanged batch021 inputs; shared corpus gates remain separate.

### Nafate versus active cefamandole

representation: supported. Targets: CHEBI:3481.

O-formyl sodium nafate is distinct from hydroxy cefamandole sodium and lithium. Native prodrug definition and graph are correct; quantitative activity must identify administered/tested compound and hydrolysis conditions.

### Chemical, drug and document links

grounding: supported. Targets: CHEBI:3481.

CAS42540-40-9, KEGG C08102/D00909 and GSRS structure are coherent. Beilstein remains authority-asserted, DrugBank inaccessible, and patents correctly remain broader documents.

### Historical approvals and later US withdrawal

evidence: concern. Targets: CHEBI:3481.

The original approval dates and discontinued flags are supported. The unqualified current APPROVED summary omits affirmative FDA withdrawals for both cited applications. Preserve approval history while representing application-specific later status and dates.

### Antibacterial and conversion evidence

evidence: supported. Targets: CHEBI:3481.

Original bacterial and animal experiments support prodrug antibacterial context with conversion and assay limits. No direct target engagement or universal species MIC is established by these selected studies.

### Host and combination endpoints

scope: supported. Targets: CHEBI:3481.

Platelet effects, renal interactions, pharmacokinetics and polymer/dispersin experiments remain distinct from exact single-agent antimicrobial target evidence.

## Findings

### F1: Reconcile the APPROVED summary with withdrawal of both cited FDA applications

major / open / confirmed; issue key: cefamandole-nafate-fda-withdrawn-approvals.

clinical_status remains APPROVED without temporal qualification, while FDA formally withdrew ANDA062560 effective2007-12-07 and NDA050504 effective2009-03-13. These applications account for all six native FDA product assertions. Original approval dates and discontinued marketing flags are accurate historical facts, but do not communicate the later withdrawal. The finding is confined to these US applications and does not assert worldwide withdrawal or a safety reason.

## Recommended Actions And Acceptance Checks

### A1

Preserve original approval history and reconcile the later US withdrawal through maintained regulatory owners.

- Keep the original approval dates, exact UNII/full-key join and product identifiers. Add the two official withdrawal notices with jurisdiction, application and effective dates.
- Make the undated summary consistent with supported current status; if retaining an ever-approved view, name that semantics explicitly and distinguish it from current application status. Do not label every historical approval assertion false.
- Do not infer withdrawal from Discontinued alone, do not imply a safety reason, and do not generalize these US applications to other countries or uninspected products.
- Reproduce the result through extraction/seeding, preserve historical evidence, and add a focused withdrawal-history regression alongside existing discontinuation guards. Run schema/strict, source provenance and required corpus gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cefamandole-nafate.yaml; Entire native YAML, provenance and history | supports | The complete exact sodium-salt record, all names, source concept, chemical structure, cross-reference placements and history were read. Native SEEDED status is unchanged. No primary molecular target, activity_spectrum, resistance mechanism or causal graph is populated. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact ChEBI source row, maintained extraction/seeding and initial input capture | supports | The exact ChEBI row supplies identity, synonyms, structure, ontology context and links. Initial captured input hashes remain intact. Hidden and ignored files were included in the bounded local owner/reference search, excluding .git and .venv. |
| authority | https://www.ebi.ac.uk/chebi/CHEBI:3481; 209-ols.json; current term and chemical annotations | supports | Current ChEBI agrees with the native sodium-containing formula, full stereochemical key and definition. The organic sodium salt parent and antibacterial-drug role are appropriate. This is chemical and ontology context, not a primary PBP experiment or current regulatory approval. |
| chemistry | Independent RDKit 2026.03.5 calculations; 209-chemistry.json;209-210-external-chemistry.json | supports | Native SMILES and InChI reproduce two fragments, net charge zero, three configured R centres, complete key, formula and source-precision masses. The ChEBI source mint matches. Independent parsing of the live KEGG MOL reproduces the exact native key. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/23665731; 209-pubchem-cas.json | supports | The public CAS-name query resolves to the exact sodium salt with the complete native stereochemical key and formula. It corroborates the authority mapping without implying a direct CAS registry inspection. |
| kegg | https://rest.kegg.jp/get/C08102; 209-kegg.txt/.mol;209-keggdrug.txt | supports | The compound and drug entries distinguish the appropriate sodium form; the MOL matches exactly. Drug-level PBP/peptidoglycan annotations remain database context. No exact parent-binding claim is copied from those annotations. |
| adapter | Native mechanism scope; Complete native text before public literature follow-up | context_only | Neither native record asserts a named gene/protein, pathway or stress mechanism. An adapter lookup was therefore not applicable to the native claims. Protein names in a later combination paper or KEGG drug classification are not silently adopted as native targets. |
| fda-input | data/raw/fda_clinical_status.tsv; scripts/extract_fda_clinical_status.py; scripts/seed_from_sources.py; 209-fda-rows.json; approved_originals/eligible_products; attach_fda_clinical_status | supports | Six exact-key FDA product rows match native: NDA050504 products001–004 originally approved1978-09-27; ANDA062560 products001–002 originally approved1985-09-10. All carry Discontinued/currently_marketed:false. The extractor retains earliest ORIG/AP events; the seeder hard-codes APPROVED for assertions and the undated summary. FDA source and extractor were appended to the capture without replacing initial hashes. |
| fda-current | https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&amp;ApplNo=050504; 209-fda-050504.html;209-fda-062560.html; current identity, product and approval history sections | supports | The official application pages corroborate Mandol/cefamandole nafate, the application/product identities, original approval dates and discontinued products. Historical AP records remain valid history, but these pages alone do not resolve whether approval was later withdrawn. |
| gsrs | https://gsrs.ncats.nih.gov/api/v1/substances/search?q=root_approvalID:8HDO7941DO; 209-gsrs.json; current version23 and independently parsed molfile | supports | UNII8HDO7941DO resolves to cefamandole nafate with full key ICZOIXFFVKYXOM-YCLOEFEOSA-M and C19H17N6NaO6S2. Current version23 retains the exact structure matched in native version22. GSRS substance approval is identity registration, not product marketing approval. |
| withdrawal2007 | https://www.govinfo.gov/content/pkg/FR-2007-11-07/html/E7-21886.htm; Federal Register72, pp62858–62863; ANDA62-560 table row and closing withdrawal paragraph | refutes | FDA notice E7-21886 lists Mandol under ANDA62-560 and withdraws approval of all listed applications and their amendments/supplements effective2007-12-07. Applicants stated that products were no longer marketed and requested withdrawal. The table misspells the ingredient cefamadole, but application, brand and sponsor resolve the exact application. This is affirmative withdrawal evidence, not an inference from discontinuation. |
| withdrawal2009 | https://www.govinfo.gov/content/pkg/FR-2009-02-11/html/E9-2901.htm; Federal Register74, pp6896–6901; NDA50-504 row p6900 and closing paragraph p6901 | refutes | FDA notice E9-2901 names Mandol (cefamandole nafate) Injection under NDA50-504, Eli Lilly, and withdraws the listed approvals and all amendments/supplements effective2009-03-13. The notice gives applicant-requested withdrawal after marketing ceased. It does not establish a safety-related reason or global status. |
| status-semantics | src/antibioticmech/schema/antibioticmech.yaml; clinical_status; ClinicalStatusAssertion; ClinicalStatusEnum | supports | The schema calls clinical_status regulatory/use status and provides WITHDRAWN. Assertions supply jurisdiction/product evidence; no historical-ever-approved meaning is specified for the undated summary. Preserving dated original approval evidence is compatible with separately representing later withdrawal. |
| adopted | PMID:10412;17548491;41479;533268;7000857;921240; 209-core.json; all six complete adopted abstracts plus selected follow-up metadata/abstracts | supports | 10412 concerns pH/base-catalysed prodrug conversion;17548491 antibiotic/dispersin-B polymer combinations;41479 microbiological assay hydrolysis;533268 high-concentration platelet/coagulation effects;7000857 volunteer IM/IV disposition and pain;921240 rodent coadministration with tobramycin and renal toxicity. Host effects and formulation combinations are not primary bacterial target mechanisms. |
| activity | https://doi.org/10.1128/AAC.12.1.67; PMID18988; original full pp67–72, Tables1–4 and Figures1–4;210-page67..72.png | supports | Materials are cefamandole lithium and cefamandole nafate from Lilly. Standard agar susceptibility appears similar because nafate hydrolyses; Table2 reports half-life0.9h in Mueller-Hinton agar pH7.4 and9.7h in Lilly agar pH6. Log-phase lysis/HPLC experiments distinguish intrinsic activity and conversion; calculated relative activity is approximately tenfold lower for nafate under tested conditions, not a universal target-binding ratio. Table1 contains population geometric mean MICs. Mouse protection after nafate treatment is consistent with conversion. Neither lithium data nor derived hydrolysis product measurements are unqualified sodium-cefamandole observations. |
| assay | https://doi.org/10.1128/AAC.16.3.424; PMID41479; complete original pp424–426, Tables1–3 | supports | Agar diffusion experiments compare nafate with lithium-cefamandole standards across organisms and pH. Reported potency depends on conversion and assay pH; values in Tables1–3 are microbiological potency/hydrolysis measures, not MICs. Complete hydrolysis is obtained with1.25 molar equivalents sodium carbonate for30min at room temperature or pH8 buffer for1h at37C. Authors recommend sodium or lithium cefamandole for routine assays. Do not interpret this as direct PBP binding. |
| combination | https://doi.org/10.1128/AAC.01249-06; PMID17548491/PMC1932551; complete abstract and original accessible Methods sections, not full results | context_only | The paper studies cefamandole nafate with dispersin B on polyurethane surfaces. Methods distinguish enzyme loading, antibiotic adsorption, planktonic susceptibility and adherent-cell CFU assays. The synergistic experiment exposes established polymer biofilm to0.25ug/mL antibiotic after enzyme treatment; this is combination/surface context. Dispersin B is a partner enzyme, not an antibacterial binding target of nafate. Full results and raw images were not independently reviewed. |
| patents | patent:CN101822678;patent:CN101829118;patent:CN101836960; 209-patent-*.html; titles and abstracts | supports | The three documents concern combined drug, hydrate-crystal/sodium-benzoate powder, and nafate/sodium-carbonate microsphere formulations. Their document_xrefs placement is appropriate. Neither mixtures nor hydrate formulations replace the exact native sodium-prodrug structure; broad efficacy claims were not independently validated. |

## Limits And Additional Notes

- No exhaustive producer, clinical, resistance or taxonomic survey was undertaken. Historical susceptibility assays do not establish present-day breakpoints.
- Focused schema/strict checks pass; independent chemistry used the batch019 interpreter because the locked batch021 environment lacks RDKit. Required shared corpus checks are inserted before save.
- Beilstein5403938 was not independently inspected. DrugBank DB01326 returned403. Patent titles/abstracts were checked, not every claim or example.
- All six adopted PMID complete abstracts were read. PMID41479 and follow-up18988 original pages were read in full. Other pharmacokinetic/host papers remain abstract-level; no dosing or clinical recommendation is made.
- The biofilm paper was read at complete abstract and accessible Methods scope. Direct PMC subsequently returned a browser challenge and EuropePMC XML returned500; no full-results or image inspection is claimed.
- FDA conclusion is restricted to the two cited applications. Official applicant-requested withdrawal is distinct from safety-related withdrawal and from discontinuation alone. The current GSRS structure is version23; native version22 provenance is preserved.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T110437Z-cefamandole-nafate-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review cefamandole nafate identity, prodrug evidence and FDA history
started_at: '2026-10-21T10:44:47Z'
finished_at: '2026-10-21T11:04:37Z'
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
summary: 'The sodium O-formyl cefamandole prodrug is structurally coherent. Primary
  experiments show conversion to cefamandole and assay-dependent antibacterial activity.
  One major current-status defect remains: the undated APPROVED summary overlooks
  official withdrawal of both cited US applications, although the original approval
  history and discontinued marketing flags are accurate.'
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
  - path: data/antibiotics/antibacterial/cefamandole-nafate.yaml
    sha256: d72e8d7ffb6420855022d072ddeab56c53470f05111023be00a9a4b7747a2003
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
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/extract_fda_clinical_status.py
    sha256: f30f385ea6d530dc1749e3d805dbcdbc8715fbc476abc510bf144ea13964e171
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
- target_id: CHEBI:3481
  path: data/antibiotics/antibacterial/cefamandole-nafate.yaml
  label: cefamandole nafate
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
    path: data/raw/fda_clinical_status.tsv
    role: FDA clinical source assertion ownership
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: FDA clinical source assertion ownership
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position209; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3481
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3481
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    209
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3481
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefamandole-nafate.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3481
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefamandole-nafate.yaml --out /private/tmp/am-review-session/209-strict.tsv
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
  - CHEBI:3481
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
  - CHEBI:3481
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
  - CHEBI:3481
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
  - CHEBI:3481
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
  - CHEBI:3481
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
  - CHEBI:3481
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
  - CHEBI:3481
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
  - CHEBI:3481
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
  - CHEBI:3481
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cefamandole-nafate.yaml
  locator: Entire native YAML, provenance and history
  accessed_at: '2026-10-21T11:03:00Z'
  support: supports
  summary: The complete exact sodium-salt record, all names, source concept, chemical
    structure, cross-reference placements and history were read. Native SEEDED status
    is unchanged. No primary molecular target, activity_spectrum, resistance mechanism
    or causal graph is populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Exact ChEBI source row, maintained extraction/seeding and initial input
    capture
  accessed_at: '2026-10-21T11:03:00Z'
  support: supports
  summary: The exact ChEBI row supplies identity, synonyms, structure, ontology context
    and links. Initial captured input hashes remain intact. Hidden and ignored files
    were included in the bounded local owner/reference search, excluding .git and
    .venv.
  search_scope: rg --no-ignore --hidden exact label, ChEBI identifier and full structural
    key in isolated batch021; actual owners captured before assessment.
- evidence_id: authority
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3481
  locator: 209-ols.json; current term and chemical annotations
  accessed_at: '2026-10-21T11:03:00Z'
  support: supports
  summary: Current ChEBI agrees with the native sodium-containing formula, full stereochemical
    key and definition. The organic sodium salt parent and antibacterial-drug role
    are appropriate. This is chemical and ontology context, not a primary PBP experiment
    or current regulatory approval.
  snapshot_sha256: 24b0937f2363741d90c06089f41632821d6c89b167900377d6d55f63ae590f3f
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit 2026.03.5 calculations
  locator: 209-chemistry.json;209-210-external-chemistry.json
  accessed_at: '2026-10-21T11:03:00Z'
  support: supports
  summary: Native SMILES and InChI reproduce two fragments, net charge zero, three
    configured R centres, complete key, formula and source-precision masses. The ChEBI
    source mint matches. Independent parsing of the live KEGG MOL reproduces the exact
    native key.
  snapshot_sha256: 8b20d4f36dba834ad5dcb3d9c7f6e656e32a668500234774e3c47937cd42afca
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/23665731
  locator: 209-pubchem-cas.json
  accessed_at: '2026-10-21T11:03:00Z'
  support: supports
  summary: The public CAS-name query resolves to the exact sodium salt with the complete
    native stereochemical key and formula. It corroborates the authority mapping without
    implying a direct CAS registry inspection.
  snapshot_sha256: 0d534bedb6b141a2ee1ee78ad79182e58a17a898424f1b328255620b94fea332
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/C08102
  locator: 209-kegg.txt/.mol;209-keggdrug.txt
  accessed_at: '2026-10-21T11:03:00Z'
  support: supports
  summary: The compound and drug entries distinguish the appropriate sodium form;
    the MOL matches exactly. Drug-level PBP/peptidoglycan annotations remain database
    context. No exact parent-binding claim is copied from those annotations.
  snapshot_sha256: 28ceae70736732324a71cd4044be7b9f6992ad646458048562b5bb0292b96239
- evidence_id: adapter
  kind: search
  reference: Native mechanism scope
  locator: Complete native text before public literature follow-up
  accessed_at: '2026-10-21T11:03:00Z'
  support: context_only
  summary: Neither native record asserts a named gene/protein, pathway or stress mechanism.
    An adapter lookup was therefore not applicable to the native claims. Protein names
    in a later combination paper or KEGG drug classification are not silently adopted
    as native targets.
  search_scope: Complete native mechanism/definition/target/resistance/graph review
    before web follow-up.
- evidence_id: fda-input
  kind: record_content
  reference: data/raw/fda_clinical_status.tsv; scripts/extract_fda_clinical_status.py;
    scripts/seed_from_sources.py
  locator: 209-fda-rows.json; approved_originals/eligible_products; attach_fda_clinical_status
  accessed_at: '2026-10-21T11:03:00Z'
  support: supports
  summary: 'Six exact-key FDA product rows match native: NDA050504 products001–004
    originally approved1978-09-27; ANDA062560 products001–002 originally approved1985-09-10.
    All carry Discontinued/currently_marketed:false. The extractor retains earliest
    ORIG/AP events; the seeder hard-codes APPROVED for assertions and the undated
    summary. FDA source and extractor were appended to the capture without replacing
    initial hashes.'
  snapshot_sha256: 0d60a62f9db7997d0211e41352fe6f9b0db8dfa692bc5aa1d0da5debf039c1bd
- evidence_id: fda-current
  kind: authority
  reference: https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=050504
  locator: 209-fda-050504.html;209-fda-062560.html; current identity, product and
    approval history sections
  accessed_at: '2026-10-21T11:03:00Z'
  support: supports
  summary: The official application pages corroborate Mandol/cefamandole nafate, the
    application/product identities, original approval dates and discontinued products.
    Historical AP records remain valid history, but these pages alone do not resolve
    whether approval was later withdrawn.
  snapshot_sha256: a1f69bbabb78ead3d092c2dd8e503e2ff1e636d2bb14a6de250902d1cd368245
- evidence_id: gsrs
  kind: authority
  reference: https://gsrs.ncats.nih.gov/api/v1/substances/search?q=root_approvalID:8HDO7941DO
  locator: 209-gsrs.json; current version23 and independently parsed molfile
  accessed_at: '2026-10-21T11:03:00Z'
  support: supports
  summary: UNII8HDO7941DO resolves to cefamandole nafate with full key ICZOIXFFVKYXOM-YCLOEFEOSA-M
    and C19H17N6NaO6S2. Current version23 retains the exact structure matched in native
    version22. GSRS substance approval is identity registration, not product marketing
    approval.
  snapshot_sha256: 8a354f56d85a7c93e6cc753353ecb68b01a9709c244d526bd3984f84c4355dc5
- evidence_id: withdrawal2007
  kind: primary_source
  reference: https://www.govinfo.gov/content/pkg/FR-2007-11-07/html/E7-21886.htm
  locator: Federal Register72, pp62858–62863; ANDA62-560 table row and closing withdrawal
    paragraph
  accessed_at: '2026-10-21T11:03:00Z'
  support: refutes
  summary: FDA notice E7-21886 lists Mandol under ANDA62-560 and withdraws approval
    of all listed applications and their amendments/supplements effective2007-12-07.
    Applicants stated that products were no longer marketed and requested withdrawal.
    The table misspells the ingredient cefamadole, but application, brand and sponsor
    resolve the exact application. This is affirmative withdrawal evidence, not an
    inference from discontinuation.
  snapshot_sha256: 12924653c90671b1305a20cbcc6875c031e6a4751a7cf4e52a68ee598f73b142
- evidence_id: withdrawal2009
  kind: primary_source
  reference: https://www.govinfo.gov/content/pkg/FR-2009-02-11/html/E9-2901.htm
  locator: Federal Register74, pp6896–6901; NDA50-504 row p6900 and closing paragraph
    p6901
  accessed_at: '2026-10-21T11:03:00Z'
  support: refutes
  summary: FDA notice E9-2901 names Mandol (cefamandole nafate) Injection under NDA50-504,
    Eli Lilly, and withdraws the listed approvals and all amendments/supplements effective2009-03-13.
    The notice gives applicant-requested withdrawal after marketing ceased. It does
    not establish a safety-related reason or global status.
  snapshot_sha256: 684d8b447d887e73ea8928d72fc8ceb030c896b502c14cf3a8a996c2d9598350
- evidence_id: status-semantics
  kind: record_content
  reference: src/antibioticmech/schema/antibioticmech.yaml
  locator: clinical_status; ClinicalStatusAssertion; ClinicalStatusEnum
  accessed_at: '2026-10-21T11:03:00Z'
  support: supports
  summary: The schema calls clinical_status regulatory/use status and provides WITHDRAWN.
    Assertions supply jurisdiction/product evidence; no historical-ever-approved meaning
    is specified for the undated summary. Preserving dated original approval evidence
    is compatible with separately representing later withdrawal.
- evidence_id: adopted
  kind: database
  reference: PMID:10412;17548491;41479;533268;7000857;921240
  locator: 209-core.json; all six complete adopted abstracts plus selected follow-up
    metadata/abstracts
  accessed_at: '2026-10-21T11:03:00Z'
  support: supports
  summary: 10412 concerns pH/base-catalysed prodrug conversion;17548491 antibiotic/dispersin-B
    polymer combinations;41479 microbiological assay hydrolysis;533268 high-concentration
    platelet/coagulation effects;7000857 volunteer IM/IV disposition and pain;921240
    rodent coadministration with tobramycin and renal toxicity. Host effects and formulation
    combinations are not primary bacterial target mechanisms.
  snapshot_sha256: 605075a96df6ede4ab25cfe864c00606e668e2e01d271acb97dc5ba75c67f89b
- evidence_id: activity
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.12.1.67
  locator: PMID18988; original full pp67–72, Tables1–4 and Figures1–4;210-page67..72.png
  accessed_at: '2026-10-21T11:03:00Z'
  support: supports
  summary: Materials are cefamandole lithium and cefamandole nafate from Lilly. Standard
    agar susceptibility appears similar because nafate hydrolyses; Table2 reports
    half-life0.9h in Mueller-Hinton agar pH7.4 and9.7h in Lilly agar pH6. Log-phase
    lysis/HPLC experiments distinguish intrinsic activity and conversion; calculated
    relative activity is approximately tenfold lower for nafate under tested conditions,
    not a universal target-binding ratio. Table1 contains population geometric mean
    MICs. Mouse protection after nafate treatment is consistent with conversion. Neither
    lithium data nor derived hydrolysis product measurements are unqualified sodium-cefamandole
    observations.
  snapshot_sha256: eb8554ddb4d0ed63f3e1cec5632d806b081fc49a7dc1ddb88543c51dc7db97d7
- evidence_id: assay
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.16.3.424
  locator: PMID41479; complete original pp424–426, Tables1–3
  accessed_at: '2026-10-21T11:03:00Z'
  support: supports
  summary: Agar diffusion experiments compare nafate with lithium-cefamandole standards
    across organisms and pH. Reported potency depends on conversion and assay pH;
    values in Tables1–3 are microbiological potency/hydrolysis measures, not MICs.
    Complete hydrolysis is obtained with1.25 molar equivalents sodium carbonate for30min
    at room temperature or pH8 buffer for1h at37C. Authors recommend sodium or lithium
    cefamandole for routine assays. Do not interpret this as direct PBP binding.
  snapshot_sha256: 0132a96d30cc43bba310819c00bbbe897e8814ee4b879a6ade03e69d21f43bae
- evidence_id: combination
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.01249-06
  locator: PMID17548491/PMC1932551; complete abstract and original accessible Methods
    sections, not full results
  accessed_at: '2026-10-21T11:03:00Z'
  support: context_only
  summary: The paper studies cefamandole nafate with dispersin B on polyurethane surfaces.
    Methods distinguish enzyme loading, antibiotic adsorption, planktonic susceptibility
    and adherent-cell CFU assays. The synergistic experiment exposes established polymer
    biofilm to0.25ug/mL antibiotic after enzyme treatment; this is combination/surface
    context. Dispersin B is a partner enzyme, not an antibacterial binding target
    of nafate. Full results and raw images were not independently reviewed.
- evidence_id: patents
  kind: primary_source
  reference: patent:CN101822678;patent:CN101829118;patent:CN101836960
  locator: 209-patent-*.html; titles and abstracts
  accessed_at: '2026-10-21T11:03:00Z'
  support: supports
  summary: The three documents concern combined drug, hydrate-crystal/sodium-benzoate
    powder, and nafate/sodium-carbonate microsphere formulations. Their document_xrefs
    placement is appropriate. Neither mixtures nor hydrate formulations replace the
    exact native sodium-prodrug structure; broad efficacy claims were not independently
    validated.
  snapshot_sha256: 5e421faf06abd9f7328339132fb81ae42f4c0be1b2a2ff8675f5fe51214c8f68
assessments:
- assessment_id: identity
  area: identity
  topic: Exact sodium form
  outcome: supported
  summary: The native graph, formula, charge, stereo descriptors and source mint agree
    with current ChEBI, PubChem and independently parsed KEGG. The sodium salt must
    remain distinct from the neutral acid, other counterions and the O-formyl prodrug.
  target_ids:
  - CHEBI:3481
  evidence_ids:
  - native
  - authority
  - chemistry
  - pubchem
  - kegg
- assessment_id: grounding
  area: grounding
  topic: Parent, role and definition
  outcome: supported
  summary: The organic sodium salt parent and antibacterial-drug role fit the graph
    and primary pharmacological context. Broad classification does not substitute
    for exact material or current clinical status.
  target_ids:
  - CHEBI:3481
  evidence_ids:
  - authority
  - chemistry
  - kegg
- assessment_id: provenance
  area: provenance
  topic: Maintained ownership and seed history
  outcome: supported
  summary: Source concept and dated seed history are coherent. Review-only output
    preserves native status and original hashes; proposed fixes or enrichment belong
    to maintained owners.
  target_ids:
  - CHEBI:3481
  evidence_ids:
  - native
  - owners
  - chemistry
- assessment_id: optional
  area: completeness
  topic: Unpopulated scientific domains
  outcome: supported
  summary: Absent optional producer, target, causal graph or activity fields are not
    defects by themselves. Any additions require exact material, strain, endpoint
    and evidence scope.
  target_ids:
  - CHEBI:3481
  evidence_ids:
  - native
- assessment_id: gates
  area: schema
  topic: Focused checks
  outcome: supported
  summary: Schema and strict checks pass in batch021. Independent chemistry used the
    existing batch019 RDKit interpreter against unchanged batch021 inputs; shared
    corpus gates remain separate.
  target_ids:
  - CHEBI:3481
  evidence_ids:
  - chemistry
- assessment_id: prodrug
  area: representation
  topic: Nafate versus active cefamandole
  outcome: supported
  summary: O-formyl sodium nafate is distinct from hydroxy cefamandole sodium and
    lithium. Native prodrug definition and graph are correct; quantitative activity
    must identify administered/tested compound and hydrolysis conditions.
  target_ids:
  - CHEBI:3481
  evidence_ids:
  - authority
  - chemistry
  - activity
  - assay
- assessment_id: references
  area: grounding
  topic: Chemical, drug and document links
  outcome: supported
  summary: CAS42540-40-9, KEGG C08102/D00909 and GSRS structure are coherent. Beilstein
    remains authority-asserted, DrugBank inaccessible, and patents correctly remain
    broader documents.
  target_ids:
  - CHEBI:3481
  evidence_ids:
  - authority
  - pubchem
  - kegg
  - gsrs
  - patents
- assessment_id: clinical
  area: evidence
  topic: Historical approvals and later US withdrawal
  outcome: concern
  summary: The original approval dates and discontinued flags are supported. The unqualified
    current APPROVED summary omits affirmative FDA withdrawals for both cited applications.
    Preserve approval history while representing application-specific later status
    and dates.
  target_ids:
  - CHEBI:3481
  evidence_ids:
  - fda-input
  - fda-current
  - withdrawal2007
  - withdrawal2009
  - status-semantics
- assessment_id: activity
  area: evidence
  topic: Antibacterial and conversion evidence
  outcome: supported
  summary: Original bacterial and animal experiments support prodrug antibacterial
    context with conversion and assay limits. No direct target engagement or universal
    species MIC is established by these selected studies.
  target_ids:
  - CHEBI:3481
  evidence_ids:
  - activity
  - assay
  - adopted
- assessment_id: host
  area: scope
  topic: Host and combination endpoints
  outcome: supported
  summary: Platelet effects, renal interactions, pharmacokinetics and polymer/dispersin
    experiments remain distinct from exact single-agent antimicrobial target evidence.
  target_ids:
  - CHEBI:3481
  evidence_ids:
  - adopted
  - combination
findings:
- finding_id: F1
  issue_key: cefamandole-nafate-fda-withdrawn-approvals
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile the APPROVED summary with withdrawal of both cited FDA applications
  description: clinical_status remains APPROVED without temporal qualification, while
    FDA formally withdrew ANDA062560 effective2007-12-07 and NDA050504 effective2009-03-13.
    These applications account for all six native FDA product assertions. Original
    approval dates and discontinued marketing flags are accurate historical facts,
    but do not communicate the later withdrawal. The finding is confined to these
    US applications and does not assert worldwide withdrawal or a safety reason.
  target_ids:
  - CHEBI:3481
  field_paths:
  - clinical_status
  - clinical_status_assertions
  evidence_ids:
  - fda-input
  - fda-current
  - withdrawal2007
  - withdrawal2009
  - status-semantics
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Maintained product regulatory evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Preserve original approvals and reconcile subsequent withdrawal evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generate qualified current clinical status
  - repository: CultureBotAI/AntibioticMech
    path: src/antibioticmech/schema/antibioticmech.yaml
    role: Explicit historical/current and jurisdiction semantics where needed
  rule_id: 'docs/CURATION.md: evidence-supported clinical status and provenance'
  native_severity: major unqualified regulatory-status error
  normalization_reason: Affirmative application-specific primary notices contradict
    an undated currently usable APPROVED summary; the conclusion is not based merely
    on discontinued marketing.
actions:
- action_id: A1
  description: Preserve original approval history and reconcile the later US withdrawal
    through maintained regulatory owners.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:3481
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Maintained product regulatory evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Preserve original approvals and reconcile subsequent withdrawal evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generate qualified current clinical status
  - repository: CultureBotAI/AntibioticMech
    path: src/antibioticmech/schema/antibioticmech.yaml
    role: Explicit historical/current and jurisdiction semantics where needed
  acceptance_checks:
  - Keep the original approval dates, exact UNII/full-key join and product identifiers.
    Add the two official withdrawal notices with jurisdiction, application and effective
    dates.
  - Make the undated summary consistent with supported current status; if retaining
    an ever-approved view, name that semantics explicitly and distinguish it from
    current application status. Do not label every historical approval assertion false.
  - Do not infer withdrawal from Discontinued alone, do not imply a safety reason,
    and do not generalize these US applications to other countries or uninspected
    products.
  - Reproduce the result through extraction/seeding, preserve historical evidence,
    and add a focused withdrawal-history regression alongside existing discontinuation
    guards. Run schema/strict, source provenance and required corpus gates.
limitations:
- No exhaustive producer, clinical, resistance or taxonomic survey was undertaken.
  Historical susceptibility assays do not establish present-day breakpoints.
- Focused schema/strict checks pass; independent chemistry used the batch019 interpreter
  because the locked batch021 environment lacks RDKit. Required shared corpus checks
  are inserted before save.
- Beilstein5403938 was not independently inspected. DrugBank DB01326 returned403.
  Patent titles/abstracts were checked, not every claim or example.
- All six adopted PMID complete abstracts were read. PMID41479 and follow-up18988
  original pages were read in full. Other pharmacokinetic/host papers remain abstract-level;
  no dosing or clinical recommendation is made.
- The biofilm paper was read at complete abstract and accessible Methods scope. Direct
  PMC subsequently returned a browser challenge and EuropePMC XML returned500; no
  full-results or image inspection is claimed.
- FDA conclusion is restricted to the two cited applications. Official applicant-requested
  withdrawal is distinct from safety-related withdrawal and from discontinuation alone.
  The current GSRS structure is version23; native version22 provenance is preserved.
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
