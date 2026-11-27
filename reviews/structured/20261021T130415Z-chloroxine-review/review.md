# Review of chloroxine

- Review: 20261021T130415Z-chloroxine-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:48:40Z
- Finished UTC: 2026-10-21T13:04:15Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native neutral 5,7-dichloroquinolin-8-ol structure agrees with current ChEBI, PubChem, KEGG, DrugCentral and FDA GSRS. FDA confirms the exact CAPITROL application, original approval date and discontinued product status. Original bacterial and fungal experiments support activity while distinguishing cotreatment, IC50, metal effects and related compounds. No material native scientific defect was demonstrated. Some legacy cross-references and the original clinical label remain unavailable, and optional mechanism enrichment requires precise assay scope. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire SEEDED, EXACT chloroxine record: definition, eight synonyms, chemical parents and roles, neutral structure, three chemical xrefs, three drug links, Wikipedia document link, exact FDA assertion and six history events.

Selection: Queue 292; thirteen original inputs preserved and actual FDA inventory/extractor appended before detailed judgment, yielding fifteen unchanged hashes.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:59477 | data/antibiotics/antibacterial/chloroxine.yaml | generated | chloroxine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema validation | passed | True | CHEBI:59477 | Exit 0. |
| Documented strict validation | passed | True | CHEBI:59477 | Exit 0; no ERROR rows. |
| Supplemental exact structure comparison | passed | False | CHEBI:59477 | Exit 0; all inspected official structures agree with native, including exact GSRS UNII and current record version. |
| Supplemental source and FDA reconciliation | passed | False | CHEBI:59477 | Exit 0; fifteen preserved input hashes, three adopted citation dispositions, source fields, six history events and the exact current FDA product/original approval reconciled. |
| Structured protein/pathway adapter applicability | not_applicable | False | CHEBI:59477 | The native record contains no protein, gene, pathway, regulator, stress-response or transcriptomics assertion. Newly inspected host and microbial pathway studies are bounded research context; no new native target or gene claim is proposed. |
| Authoritative full QC | failed | True | CHEBI:59477 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:59477 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:59477 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:59477 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:59477 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:59477 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:59477 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:59477 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:59477 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact achiral neutral compound

identity: supported. Targets: CHEBI:59477.

Native structure and named chemical synonyms agree with multiple official authorities and exact GSRS identity.

### Legacy chemical and drug links

identity: unknown. Targets: CHEBI:59477.

LINCS and direct DrugBank access failed; Reaxys was not independently accessed. No exact-link contradiction was demonstrated.

### Chemical parents and antimicrobial roles

grounding: supported. Targets: CHEBI:59477.

Native topology supports both chemical parents; original bacterial and fungal assays support activity roles at their stated material and experimental scope.

### FDA approval and marketing status

evidence: supported. Targets: CHEBI:59477.

Exact application and ingredient match; historical approval and discontinued marketing are accurately distinguished.

### Dermatologic use and synthesis wording

evidence: unknown. Targets: CHEBI:59477.

ChEBI and DrugCentral corroborate scalp-use context; the FDA application proves the shampoo product but provides no original label. The stated chlorination preparation route was not independently checked against an original synthesis report. Neither bounded gap demonstrates an incorrect definition.

### Mechanism completeness and transfer boundaries

evidence: unknown. Targets: CHEBI:59477.

New primary studies supply context-dependent activity and pathway observations. Detailed direct targets are unasserted natively; host MR1, clioquinol resistance, metal-combination potency and artemisinin direct synthase effects must not be imported as chloroxine target proof.

### Maintained sources, citations and history

provenance: supported. Targets: CHEBI:59477.

All adopted citation leads and FDA source fields have dispositions; fifteen hashes and six history events remain unchanged.

### Optional primary enrichment

completeness: supported. Targets: CHEBI:59477.

SEEDED status is appropriate. Adding exact primary activity/mechanism evidence would be useful, but absent optional targets or MIC rows are not a demonstrated defect.

### Focused native validity

schema: supported. Targets: CHEBI:59477.

Documented native schema and strict validation pass.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/chloroxine.yaml; Entire YAML, including exact clinical assertion and six history events | supports | The native structure has two ring chlorines and one hydroxyl on quinoline, with no stereocenters or counterions. It asserts antibacterial and antifungal-drug roles, but no protein target, mode enum, resistance determinant, MIC, producer or causal graph. CAPITROL is a product name inside the clinical assertion rather than an exact chemical synonym. |
| chemistry | CHEBI:59477; PubChem:2722; KEGG:D03472; DrugCentral:611; UNII:2I8BD50I8B; 292-chemistry.py/.json, official structure snapshots and GSRS molfile | supports | Native SMILES, InChI and all inspected official structures have identical canonical graphs and WDFKMLRRRCGAKS-UHFFFAOYSA-N, C9H5Cl2NO, charge zero, no configured or unspecified stereocenters, average mass 214.051 and monoisotopic mass 212.97481914. Current GSRS version 14 identifies the exact same substance. PubChem was an independent exact-key lookup, not a native cross-reference being silently added. |
| chemical-authority | CHEBI:59477; 292-chebi.json: definition, names, parents, roles and database accessions | supports | Current ChEBI preserves the 5,7-dichloroquinolin-8-ol definition, source synonyms, organochlorine and monohydroxyquinoline parents, antibacterial-agent and antifungal-drug roles. The achiral graph supports the position-specific chemical names. The CHQ abbreviation is source supplied and is not treated as globally unique. Native links remain separated into chemical, drug and document scopes. |
| clinical | FDA NDA017594 product001; UNII:2I8BD50I8B; 292-fda.html,292-fda-open.json,292-gsrs.json and292-fda-source-row.json | supports | The official application page and openFDA identify WESTWOOD SQUIBB CAPITROL, chloroxine 2% topical shampoo, product 001, original approval on 1976-10-19 and current Discontinued marketing status. This matches the native APPROVED assertion and currently_marketed:false: historical approval is not a claim of current sale. GSRS supplies ingredient identity and version 14, not independent marketing approval. The application explicitly says its label is unavailable on that site. |
| drug-links | DrugCentral:611; KEGG:D03472; DrugBank:DB01243; LINCS:LSM-2371; 292-drugcentral.html/.mol,292-kegg.txt/.mol,292-fetch.json | context_only | DrugCentral and KEGG resolve to chloroxine with matching graphs and antiseborrheic/dermatologic context. DrugCentral also maps DB01243, while direct DrugBank access returned 403, so its current body was not independently verified. LINCS LSM-2371 returned 500; the proprietary Reaxys record was not opened. CAS773-76-2 is concordant in chemical/drug authorities, but a separate Common Chemistry API request returned 401. These limitations are not evidence of a different compound. |
| document | wikipedia.en:Chloroxine; 292-wikipedia.html: chemical infobox, article and reference list | context_only | The document resolves to chloroxine and its infobox structure agrees with the native molecule. The article includes broad clinical, spectrum and mechanism statements, some marked citation-needed, and an unverified halquinol alias. It is retained as a document link, not used to collapse halquinol mixtures, transfer clioquinol data, establish a direct target or support current regulatory advice. |
| bacterial-activity | PMID:33764972; DOI:10.1371/journal.pone.0248119; 292-burkholderia.html: original culture/material Methods, MIC and time-kill Results, SAR and Discussion | supports | The original study uses Sigma D64600 chloroxine and explicitly identifies B. thailandensis E264 and B. pseudomallei K96243. It demonstrates single-agent antibacterial activity and additional killing of ceftazidime-tolerant cells during cotreatment. The paper reports no MIC synergy, and its PrestoBlue IC50 experiments and time-kill assays are distinct endpoints. SAR suggests specificity but does not identify a bound molecular target. These results support the antibacterial role without claiming an approved melioidosis treatment. |
| fungal-activity | PMID:37493629; DOI:10.1128/mbio.01376-23; 292-candida.html: primary screening, chloroxine dose-response Results/Figure2 and culture/dose-response Methods | supports | The original study measures chloroxine growth inhibition in 13 C. auris strains using RPMI-based OD600 dose-response assays. These are IC50 observations, not clinical MICs or evidence of approved C. auris treatment. The long-term selection, reconstructed CAP1/CDR1 mutations and plating experiment establishing fungistasis specifically use clioquinol; their detailed resistance and killing conclusions were not assigned to chloroxine. The paper states that detailed family mechanisms remain unresolved. |
| mechanism | PMID:42007688; DOI:10.1128/mbio.00273-26; 292-cytochrome.html: original chloroxine Results, Figure3 description, recombinant-cell and purified-enzyme Methods, Discussion | context_only | Chloroxine reduces cytochrome-c maturation in engineered E. coli expressing bacterial maturation systems at concentrations below growth inhibition. Purified synthase assays do not show corresponding direct inhibition by chloroxine, unlike the artemisinin compounds tested in parallel. The authors discuss multiple possible processes. This is pathway-level phenotypic evidence, not verified direct binding to CcsBA or HCCS and not a universal sole antibacterial mechanism. No new target was assigned to the native record. |
| metal-context | PMID:39134284; DOI:10.1016/j.bcp.2024.116482; Complete original abstract in292-extra-core.json; publisher Introduction and selected Results text | context_only | The study reports enhanced chloroxine activity with exogenous zinc or manganese, modulation by copper/ferrous ions and oxygen, and SOD inhibition. The full target-assay provenance was not obtained. This supports a conditional metal-related mechanism lead and prevents reducing chloroxine to a context-free chelator or claiming that combination potency is intrinsic single-agent potency. |
| leads | PMID:18963921; PMID:28166217; PMID:443855; 292-lead-dispositions.json,292-core.json and292-jama-inspection.json | supports | All three adopted citations were resolved. PMID18963921 is a tin-complex spectrophotometric method, not an antimicrobial assay. PMID28166217 concerns mammalian MR1/MAIT modulation; only the complete general abstract was read, so no exact chloroxine binding claim is inferred. PMID443855 has no PubMed abstract, but the correct JAMA publisher text was inspected: it describes shampoo-related fluorescence in a patient also receiving griseofulvin and on normal scalp, not isolated antifungal efficacy. Five additional primary studies have explicit depth and scope dispositions. |
| owners | data/raw/chebi_antimicrobials.tsv;data/raw/fda_clinical_status.tsv;scripts/extract_fda_clinical_status.py;scripts/extract_source_inventory.py;scripts/seed_from_sources.py; 292-source-audit.json and exact source-row snapshots | supports | ChEBI owns identity, synonyms, roles and the three literature leads. The FDA/GSRS inventory and extractor own the application-level assertion and exact UNII match. All source dates and version fields checked against the adopted row remain coherent; all fifteen original-plus-appended hashes and six history events are preserved. |
| search | Exact chloroxine local and primary-source discovery; Ignored-inclusive search in data/raw,curation,conf,scripts for chloroxine,CHEBI:59477,UNII2I8BD50I8B and017594; public exact-name/title and source-identifier searches | context_only | Ignored files were included in local discovery. Public searches located original bacterial/fungal experiments and official identity/approval records. The broad EuropePMC query returned 195 hits and cached the first 100; only the explicitly listed selected studies were inspected beyond metadata. This is not an exhaustive full-text review of every hit. |
| validation | Focused documented native validators; 292-schema.log,292-strict.log,292-strict.tsv,292-chemistry.json and292-source-audit.json | supports | Schema, strict, exact-chemistry and preserved-source reconciliation checks pass. Shared full-corpus gates are reported separately. |

## Limits And Additional Notes

- Direct DrugBank access returned 403; LINCS returned 500; Common Chemistry returned 401 and proprietary Reaxys was not independently accessed. Current DrugCentral/KEGG and GSRS nevertheless agree on the exact native graph.
- The original CAPITROL label is unavailable on the inspected FDA application site. Historical approval/product identity are independently verified, but original indication wording and clinical efficacy were not reconstructed from a label or controlled trial.
- The definition preparation by chlorination was not independently traced to an original synthetic procedure. Current ChEBI remains the inspected authority for that wording.
- The adopted MR1/MAIT paper was inspected at complete-abstract depth; two public repository PDF routes returned 403 and the publisher route failed. It cannot justify an exact chloroxine host binding assertion in this review.
- The 1979 letter was inspected through correct publisher page 540220 using web.open. An initial mistaken 540019 URL returned 403 and was not used as article evidence; direct retrieval of the corrected page also returned 403, while browser text was available.
- The 2024 metal/SOD study was inspected at original abstract and selected publisher-text depth; detailed SOD assay provenance and every strain-specific value were not independently audited.
- The 2021 study distinguishes MIC, metabolic-readout IC50 and cotreatment time-kill effects. The 2023 fungal study distinguishes chloroxine activity from clioquinol-selected resistance and fungistasis. The 2026 study distinguishes cell-level maturation inhibition from direct synthase inhibition. No numeric MIC or new target is adopted.
- The broad literature search is discovery, not an exhaustive reading of 195 hits. Only the three adopted citations and five additional studies have explicit inspection dispositions.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record or maintained source was edited. Fifteen input hashes were rechecked.
- CAPITROL remains a product assertion; Wikipedia is a document link. No halquinol mixture, clioquinol congener or mammalian target was substituted for exact chloroxine.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T130415Z-chloroxine-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of chloroxine
started_at: '2026-10-21T12:48:40Z'
finished_at: '2026-10-21T13:04:15Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Independent entire-record audit against preserved ChEBI and
    actual FDA/GSRS owners, current official records and inspected original scientific
    sources.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: Supported exact identity and historical approval; detailed mechanism
  remains unasserted
scientific_review: true
summary: The native neutral 5,7-dichloroquinolin-8-ol structure agrees with current
  ChEBI, PubChem, KEGG, DrugCentral and FDA GSRS. FDA confirms the exact CAPITROL
  application, original approval date and discontinued product status. Original bacterial
  and fungal experiments support activity while distinguishing cotreatment, IC50,
  metal effects and related compounds. No material native scientific defect was demonstrated.
  Some legacy cross-references and the original clinical label remain unavailable,
  and optional mechanism enrichment requires precise assay scope. Scientific assessment
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
  - path: data/antibiotics/antibacterial/chloroxine.yaml
    sha256: 2256d6b8b5c527120d92986e7490ab443b39000540dacf4496a4728af56f2df7
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
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
    role: Adopted exact FDA application and GSRS identity row
  - path: scripts/extract_fda_clinical_status.py
    sha256: f30f385ea6d530dc1749e3d805dbcdbc8715fbc476abc510bf144ea13964e171
    role: Maintained FDA and GSRS assertion extraction
scope:
  description: 'Entire SEEDED, EXACT chloroxine record: definition, eight synonyms,
    chemical parents and roles, neutral structure, three chemical xrefs, three drug
    links, Wikipedia document link, exact FDA assertion and six history events.'
  selection: Queue 292; thirteen original inputs preserved and actual FDA inventory/extractor
    appended before detailed judgment, yielding fifteen unchanged hashes.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:59477
targets:
- target_id: CHEBI:59477
  path: data/antibiotics/antibacterial/chloroxine.yaml
  label: chloroxine
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
    role: Adopted exact FDA application and GSRS identity row
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Maintained FDA and GSRS assertion extraction
checks:
- check_id: schema
  name: Documented schema validation
  status: passed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/chloroxine.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0.
  target_ids:
  - CHEBI:59477
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict validation
  status: passed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/chloroxine.yaml --out /private/tmp/am-review-session/292-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no ERROR rows.
  target_ids:
  - CHEBI:59477
  evidence_ids:
  - validation
- check_id: chemistry
  name: Supplemental exact structure comparison
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/292-chemistry.py
    > /private/tmp/am-review-session/292-chemistry.log
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; all inspected official structures agree with native, including
    exact GSRS UNII and current record version.
  target_ids:
  - CHEBI:59477
  evidence_ids:
  - chemistry
- check_id: reconciliation
  name: Supplemental source and FDA reconciliation
  status: passed
  required: false
  command: .venv/bin/python /private/tmp/am-review-session/292-ledger.py
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; fifteen preserved input hashes, three adopted citation dispositions,
    source fields, six history events and the exact current FDA product/original approval
    reconciled.
  target_ids:
  - CHEBI:59477
  evidence_ids:
  - owners
  - clinical
  - leads
- check_id: structured-adapter
  name: Structured protein/pathway adapter applicability
  status: not_applicable
  required: false
  summary: The native record contains no protein, gene, pathway, regulator, stress-response
    or transcriptomics assertion. Newly inspected host and microbial pathway studies
    are bounded research context; no new native target or gene claim is proposed.
  target_ids:
  - CHEBI:59477
  evidence_ids:
  - record
  - mechanism
  - leads
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:59477
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
  - CHEBI:59477
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
  - CHEBI:59477
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
  - CHEBI:59477
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
  - CHEBI:59477
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
  - CHEBI:59477
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
  - CHEBI:59477
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
  - CHEBI:59477
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
  - CHEBI:59477
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/chloroxine.yaml
  locator: Entire YAML, including exact clinical assertion and six history events
  accessed_at: '2026-10-21T12:57:42Z'
  support: supports
  summary: The native structure has two ring chlorines and one hydroxyl on quinoline,
    with no stereocenters or counterions. It asserts antibacterial and antifungal-drug
    roles, but no protein target, mode enum, resistance determinant, MIC, producer
    or causal graph. CAPITROL is a product name inside the clinical assertion rather
    than an exact chemical synonym.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:59477; PubChem:2722; KEGG:D03472; DrugCentral:611; UNII:2I8BD50I8B
  locator: 292-chemistry.py/.json, official structure snapshots and GSRS molfile
  accessed_at: '2026-10-21T12:57:42Z'
  support: supports
  summary: Native SMILES, InChI and all inspected official structures have identical
    canonical graphs and WDFKMLRRRCGAKS-UHFFFAOYSA-N, C9H5Cl2NO, charge zero, no configured
    or unspecified stereocenters, average mass 214.051 and monoisotopic mass 212.97481914.
    Current GSRS version 14 identifies the exact same substance. PubChem was an independent
    exact-key lookup, not a native cross-reference being silently added.
  snapshot_sha256: c720022567b56d97e445d9945ae47788bd4ba4b1fe941a6b6b136b8a3fc062ca
- evidence_id: chemical-authority
  kind: authority
  reference: CHEBI:59477
  locator: '292-chebi.json: definition, names, parents, roles and database accessions'
  accessed_at: '2026-10-21T12:57:42Z'
  support: supports
  summary: Current ChEBI preserves the 5,7-dichloroquinolin-8-ol definition, source
    synonyms, organochlorine and monohydroxyquinoline parents, antibacterial-agent
    and antifungal-drug roles. The achiral graph supports the position-specific chemical
    names. The CHQ abbreviation is source supplied and is not treated as globally
    unique. Native links remain separated into chemical, drug and document scopes.
  snapshot_sha256: 44dbc352fb35847e6d1a4288d1c1d88fd65a9cab49d8dfb99e3d8fd095722d40
- evidence_id: clinical
  kind: authority
  reference: FDA NDA017594 product001; UNII:2I8BD50I8B
  locator: 292-fda.html,292-fda-open.json,292-gsrs.json and292-fda-source-row.json
  accessed_at: '2026-10-21T12:57:42Z'
  support: supports
  summary: 'The official application page and openFDA identify WESTWOOD SQUIBB CAPITROL,
    chloroxine 2% topical shampoo, product 001, original approval on 1976-10-19 and
    current Discontinued marketing status. This matches the native APPROVED assertion
    and currently_marketed:false: historical approval is not a claim of current sale.
    GSRS supplies ingredient identity and version 14, not independent marketing approval.
    The application explicitly says its label is unavailable on that site.'
  snapshot_sha256: 211d2cd60016fdbf14d8acb36a5edae11c06ae35cf8de76629680602c5a4eaa1
- evidence_id: drug-links
  kind: database
  reference: DrugCentral:611; KEGG:D03472; DrugBank:DB01243; LINCS:LSM-2371
  locator: 292-drugcentral.html/.mol,292-kegg.txt/.mol,292-fetch.json
  accessed_at: '2026-10-21T12:57:42Z'
  support: context_only
  summary: DrugCentral and KEGG resolve to chloroxine with matching graphs and antiseborrheic/dermatologic
    context. DrugCentral also maps DB01243, while direct DrugBank access returned
    403, so its current body was not independently verified. LINCS LSM-2371 returned
    500; the proprietary Reaxys record was not opened. CAS773-76-2 is concordant in
    chemical/drug authorities, but a separate Common Chemistry API request returned
    401. These limitations are not evidence of a different compound.
  snapshot_sha256: 588502fb1c7bc8fc46d264437cd7155f65d57dd423ee7735a300f14613f11025
- evidence_id: document
  kind: database
  reference: wikipedia.en:Chloroxine
  locator: '292-wikipedia.html: chemical infobox, article and reference list'
  accessed_at: '2026-10-21T12:57:42Z'
  support: context_only
  summary: The document resolves to chloroxine and its infobox structure agrees with
    the native molecule. The article includes broad clinical, spectrum and mechanism
    statements, some marked citation-needed, and an unverified halquinol alias. It
    is retained as a document link, not used to collapse halquinol mixtures, transfer
    clioquinol data, establish a direct target or support current regulatory advice.
  snapshot_sha256: d4701871c17de2e413572baba5dcdafa966777914541bb915237134915852126
- evidence_id: bacterial-activity
  kind: primary_source
  reference: PMID:33764972; DOI:10.1371/journal.pone.0248119
  locator: '292-burkholderia.html: original culture/material Methods, MIC and time-kill
    Results, SAR and Discussion'
  accessed_at: '2026-10-21T12:57:42Z'
  support: supports
  summary: The original study uses Sigma D64600 chloroxine and explicitly identifies
    B. thailandensis E264 and B. pseudomallei K96243. It demonstrates single-agent
    antibacterial activity and additional killing of ceftazidime-tolerant cells during
    cotreatment. The paper reports no MIC synergy, and its PrestoBlue IC50 experiments
    and time-kill assays are distinct endpoints. SAR suggests specificity but does
    not identify a bound molecular target. These results support the antibacterial
    role without claiming an approved melioidosis treatment.
  snapshot_sha256: b4d2301ea9957098886627e2d9b4ade1aaed3a04944ef2d2a9ade6492fb01564
- evidence_id: fungal-activity
  kind: primary_source
  reference: PMID:37493629; DOI:10.1128/mbio.01376-23
  locator: '292-candida.html: primary screening, chloroxine dose-response Results/Figure2
    and culture/dose-response Methods'
  accessed_at: '2026-10-21T12:57:42Z'
  support: supports
  summary: The original study measures chloroxine growth inhibition in 13 C. auris
    strains using RPMI-based OD600 dose-response assays. These are IC50 observations,
    not clinical MICs or evidence of approved C. auris treatment. The long-term selection,
    reconstructed CAP1/CDR1 mutations and plating experiment establishing fungistasis
    specifically use clioquinol; their detailed resistance and killing conclusions
    were not assigned to chloroxine. The paper states that detailed family mechanisms
    remain unresolved.
  snapshot_sha256: 9e88906446d75b03477d29d7f43f9c8581f45e952cbe3421e616bfba3ed0ff6d
- evidence_id: mechanism
  kind: primary_source
  reference: PMID:42007688; DOI:10.1128/mbio.00273-26
  locator: '292-cytochrome.html: original chloroxine Results, Figure3 description,
    recombinant-cell and purified-enzyme Methods, Discussion'
  accessed_at: '2026-10-21T12:57:42Z'
  support: context_only
  summary: Chloroxine reduces cytochrome-c maturation in engineered E. coli expressing
    bacterial maturation systems at concentrations below growth inhibition. Purified
    synthase assays do not show corresponding direct inhibition by chloroxine, unlike
    the artemisinin compounds tested in parallel. The authors discuss multiple possible
    processes. This is pathway-level phenotypic evidence, not verified direct binding
    to CcsBA or HCCS and not a universal sole antibacterial mechanism. No new target
    was assigned to the native record.
  snapshot_sha256: b79e273396a5c8d4f8b188d8952b208648ead0dd4c19dd4bfe2816aa61637d60
- evidence_id: metal-context
  kind: primary_source
  reference: PMID:39134284; DOI:10.1016/j.bcp.2024.116482
  locator: Complete original abstract in292-extra-core.json; publisher Introduction
    and selected Results text
  accessed_at: '2026-10-21T12:57:42Z'
  support: context_only
  summary: The study reports enhanced chloroxine activity with exogenous zinc or manganese,
    modulation by copper/ferrous ions and oxygen, and SOD inhibition. The full target-assay
    provenance was not obtained. This supports a conditional metal-related mechanism
    lead and prevents reducing chloroxine to a context-free chelator or claiming that
    combination potency is intrinsic single-agent potency.
  snapshot_sha256: 29f014c88a3bfa2b5dcb5c974decaf7cb45a2c1246c73296b7d674a4c8d10451
- evidence_id: leads
  kind: database
  reference: PMID:18963921; PMID:28166217; PMID:443855
  locator: 292-lead-dispositions.json,292-core.json and292-jama-inspection.json
  accessed_at: '2026-10-21T12:57:42Z'
  support: supports
  summary: 'All three adopted citations were resolved. PMID18963921 is a tin-complex
    spectrophotometric method, not an antimicrobial assay. PMID28166217 concerns mammalian
    MR1/MAIT modulation; only the complete general abstract was read, so no exact
    chloroxine binding claim is inferred. PMID443855 has no PubMed abstract, but the
    correct JAMA publisher text was inspected: it describes shampoo-related fluorescence
    in a patient also receiving griseofulvin and on normal scalp, not isolated antifungal
    efficacy. Five additional primary studies have explicit depth and scope dispositions.'
  snapshot_sha256: 9f392e03a9e8491ad7b893d12739c32586e73d23e2e7f10629530cd4d58b23d9
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv;data/raw/fda_clinical_status.tsv;scripts/extract_fda_clinical_status.py;scripts/extract_source_inventory.py;scripts/seed_from_sources.py
  locator: 292-source-audit.json and exact source-row snapshots
  accessed_at: '2026-10-21T12:57:42Z'
  support: supports
  summary: ChEBI owns identity, synonyms, roles and the three literature leads. The
    FDA/GSRS inventory and extractor own the application-level assertion and exact
    UNII match. All source dates and version fields checked against the adopted row
    remain coherent; all fifteen original-plus-appended hashes and six history events
    are preserved.
  snapshot_sha256: 158540bf3ff21c645d1cc6ef66adfddf9dc4498d2498ae84d879484669728b6d
- evidence_id: search
  kind: search
  reference: Exact chloroxine local and primary-source discovery
  locator: Ignored-inclusive search in data/raw,curation,conf,scripts for chloroxine,CHEBI:59477,UNII2I8BD50I8B
    and017594; public exact-name/title and source-identifier searches
  accessed_at: '2026-10-21T12:57:42Z'
  support: context_only
  summary: Ignored files were included in local discovery. Public searches located
    original bacterial/fungal experiments and official identity/approval records.
    The broad EuropePMC query returned 195 hits and cached the first 100; only the
    explicitly listed selected studies were inspected beyond metadata. This is not
    an exhaustive full-text review of every hit.
  snapshot_sha256: 154ccc9ea850bb0956ba59d271e988fa74c9aab520b823d793841aa2ec8cd7c8
  search_scope: Ignored-inclusive search in data/raw,curation,conf,scripts for chloroxine,CHEBI:59477,UNII2I8BD50I8B
    and017594; public exact-name/title and source-identifier searches
- evidence_id: validation
  kind: validation
  reference: Focused documented native validators
  locator: 292-schema.log,292-strict.log,292-strict.tsv,292-chemistry.json and292-source-audit.json
  accessed_at: '2026-10-21T12:57:42Z'
  support: supports
  summary: Schema, strict, exact-chemistry and preserved-source reconciliation checks
    pass. Shared full-corpus gates are reported separately.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact achiral neutral compound
  outcome: supported
  summary: Native structure and named chemical synonyms agree with multiple official
    authorities and exact GSRS identity.
  target_ids:
  - CHEBI:59477
  evidence_ids:
  - chemistry
  - chemical-authority
- assessment_id: external
  area: identity
  topic: Legacy chemical and drug links
  outcome: unknown
  summary: LINCS and direct DrugBank access failed; Reaxys was not independently accessed.
    No exact-link contradiction was demonstrated.
  target_ids:
  - CHEBI:59477
  evidence_ids:
  - drug-links
  - document
- assessment_id: classification
  area: grounding
  topic: Chemical parents and antimicrobial roles
  outcome: supported
  summary: Native topology supports both chemical parents; original bacterial and
    fungal assays support activity roles at their stated material and experimental
    scope.
  target_ids:
  - CHEBI:59477
  evidence_ids:
  - chemical-authority
  - bacterial-activity
  - fungal-activity
- assessment_id: clinical
  area: evidence
  topic: FDA approval and marketing status
  outcome: supported
  summary: Exact application and ingredient match; historical approval and discontinued
    marketing are accurately distinguished.
  target_ids:
  - CHEBI:59477
  evidence_ids:
  - clinical
  - chemistry
- assessment_id: definition
  area: evidence
  topic: Dermatologic use and synthesis wording
  outcome: unknown
  summary: ChEBI and DrugCentral corroborate scalp-use context; the FDA application
    proves the shampoo product but provides no original label. The stated chlorination
    preparation route was not independently checked against an original synthesis
    report. Neither bounded gap demonstrates an incorrect definition.
  target_ids:
  - CHEBI:59477
  evidence_ids:
  - chemical-authority
  - drug-links
  - clinical
- assessment_id: mechanism
  area: evidence
  topic: Mechanism completeness and transfer boundaries
  outcome: unknown
  summary: New primary studies supply context-dependent activity and pathway observations.
    Detailed direct targets are unasserted natively; host MR1, clioquinol resistance,
    metal-combination potency and artemisinin direct synthase effects must not be
    imported as chloroxine target proof.
  target_ids:
  - CHEBI:59477
  evidence_ids:
  - leads
  - mechanism
  - metal-context
  - fungal-activity
- assessment_id: provenance
  area: provenance
  topic: Maintained sources, citations and history
  outcome: supported
  summary: All adopted citation leads and FDA source fields have dispositions; fifteen
    hashes and six history events remain unchanged.
  target_ids:
  - CHEBI:59477
  evidence_ids:
  - owners
  - leads
- assessment_id: completeness
  area: completeness
  topic: Optional primary enrichment
  outcome: supported
  summary: SEEDED status is appropriate. Adding exact primary activity/mechanism evidence
    would be useful, but absent optional targets or MIC rows are not a demonstrated
    defect.
  target_ids:
  - CHEBI:59477
  evidence_ids:
  - record
  - bacterial-activity
  - fungal-activity
  - mechanism
- assessment_id: schema
  area: schema
  topic: Focused native validity
  outcome: supported
  summary: Documented native schema and strict validation pass.
  target_ids:
  - CHEBI:59477
  evidence_ids:
  - validation
findings: []
actions: []
limitations:
- Direct DrugBank access returned 403; LINCS returned 500; Common Chemistry returned
  401 and proprietary Reaxys was not independently accessed. Current DrugCentral/KEGG
  and GSRS nevertheless agree on the exact native graph.
- The original CAPITROL label is unavailable on the inspected FDA application site.
  Historical approval/product identity are independently verified, but original indication
  wording and clinical efficacy were not reconstructed from a label or controlled
  trial.
- The definition preparation by chlorination was not independently traced to an original
  synthetic procedure. Current ChEBI remains the inspected authority for that wording.
- The adopted MR1/MAIT paper was inspected at complete-abstract depth; two public
  repository PDF routes returned 403 and the publisher route failed. It cannot justify
  an exact chloroxine host binding assertion in this review.
- The 1979 letter was inspected through correct publisher page 540220 using web.open.
  An initial mistaken 540019 URL returned 403 and was not used as article evidence;
  direct retrieval of the corrected page also returned 403, while browser text was
  available.
- The 2024 metal/SOD study was inspected at original abstract and selected publisher-text
  depth; detailed SOD assay provenance and every strain-specific value were not independently
  audited.
- The 2021 study distinguishes MIC, metabolic-readout IC50 and cotreatment time-kill
  effects. The 2023 fungal study distinguishes chloroxine activity from clioquinol-selected
  resistance and fungistasis. The 2026 study distinguishes cell-level maturation inhibition
  from direct synthase inhibition. No numeric MIC or new target is adopted.
- The broad literature search is discovery, not an exhaustive reading of 195 hits.
  Only the three adopted citations and five additional studies have explicit inspection
  dispositions.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record or maintained source was edited. Fifteen input hashes were rechecked.
- CAPITROL remains a product assertion; Wikipedia is a document link. No halquinol
  mixture, clioquinol congener or mammalian target was substituted for exact chloroxine.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links: []
tags:
- record-review
- chloroxine
- clinical-status
- assay-scope
```
