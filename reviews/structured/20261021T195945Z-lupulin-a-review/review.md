# Lupulin A: inherited C-15 epimer conflicts with primary structural reassignment

- Review: 20261021T195945Z-lupulin-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:52:45Z
- Finished UTC: 2026-10-21T19:59:45Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The complete native record and actual ChEBI source were assessed. Native chemistry is internally coherent and reproduced by current ChEBI and an additional PubChem comparator, but encodes C-15 R rather than the revised natural lupulin A assignment supported by original NMR work and the published crystallographic correction. One wrong-epimer blocker is recorded. Broad antibacterial and plant-origin claims have primary support, with exact assay and material boundaries retained.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Assigned queue position 611; one exact native record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:66597 | data/antibiotics/antibacterial/lupulin-a.yaml | generated | lupulin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:66597 | Actual focused execution exited 0. Actual execution against batch062; chemistry used the existing 019 RDKit interpreter and schema/strict used the 062 environment. |
| Focused schema verification | passed | True | CHEBI:66597 | Actual focused execution exited 0. Actual execution against batch062; chemistry used the existing 019 RDKit interpreter and schema/strict used the 062 environment. |
| Focused strict verification | passed | True | CHEBI:66597 | Actual focused execution exited 0. Actual execution against batch062; chemistry used the existing 019 RDKit interpreter and schema/strict used the 062 environment. |
| Authoritative full QC | failed | True | CHEBI:66597 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:66597 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:66597 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:66597 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:66597 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:66597 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:66597 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:66597 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:66597 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### C15 assignment and unresolved remaining centres

identity: concern. Targets: CHEBI:66597.

Internal graph agreement is not sufficient: native C15 R conflicts with the original 2008 identification of natural lupulin A as S and the later explicit structural correction. The three unspecified native centres remain distinct from this affirmative wrong assignment; they are not called a racemate or automatically filled. A one-centre scratch diagnostic does not establish the complete corrected natural graph.

### Current chemical authorities and ontology

grounding: concern. Targets: CHEBI:66597.

Current ChEBI and PubChem retain the historical C15 encoding, explaining propagation without resolving the primary contradiction. Four parent skeleton/function classifications fit the graph. Reaxys exact structural content remains uninspected. No unrelated PubChem xref finding is created because PubChem is only a comparator.

### Activity, producer and host-effect claim boundaries

evidence: supported. Targets: CHEBI:66597.

The 1996 primary abstract supports broad antibacterial activity and A. lupulina isolation of named lupulin A. Exact species-level activity is not converted to strain-level MICs without methods, and exact graph transfer remains contingent on identity correction. The 2010 host COX evidence supports limited anti-inflammatory context, with extract mouse results separated from purified compound tests.

### Optional mechanism and quantitative enrichment

completeness: unknown. Targets: CHEBI:66597.

No required missing optional field is established. Exact antibacterial assay methods, material stereopurity and complete corrected stereochemistry require follow-up before quantitative enrichment. The adopted withanolide cholinesterase results and host COX effects do not establish a lupulin A antibacterial protein target.

### Maintained source ownership and all adopted citations

provenance: supported. Targets: CHEBI:66597.

All four adopted PMIDs were resolved with complete original abstracts; relevant full 2008 material and the additional original 2009 correction were inspected. Entire native history and original 13/expanded 21 owner hashes remain unchanged. Scientific corrections belong in maintained source handling, with generated YAML reproduced by seeding.

## Findings

### F1: The native structure encodes the unrevised C15 epimer

blocker / open / confirmed; issue key: lupulin-a-c15-unrevised-epimer.

The methoxy-bearing C15 carbon is R in both native encodings and in the exact systematic synonym. Original NMR work identifies previously known lupulin A as C15 S, and the published structural correction expressly revises lupulin A to the corresponding 15α-methoxy neoclerodane. Current ChEBI/PubChem agreement reproduces the historical discrepancy. The affirmative wrong C15 assignment is distinct from the three remaining unassigned centres; the observed R:S mixture in a separate 2008 isolation does not make the original named natural compound a pure R epimer.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate the full revised lupulin A structure through maintained ChEBI source handling and regenerate the exact record.

- Map the primary numbered C15 to the methoxy-bearing native atom 35 and apply the explicit original reassignment, preserving its primary provenance.
- Independently resolve C13/C16 and ester side-chain stereochemistry before declaring a fully corrected natural graph. Do not treat the one-centre diagnostic key as a complete replacement or copy an unverified secondary graph.
- Update systematic synonym and all structure encodings coherently; compare current authority associations without silently substituting propagated erroneous chemistry.
- Preserve the 2008 R:S mixture as separate material context and recover original assay methods before transferring quantitative antibacterial results.
- Regenerate, rerun required validators and verify formula, charge, masses, full key, source ownership and exact xrefs.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/lupulin-a.yaml; Entire native record and all source/history fields | supports | The record claims exact neutral lupulin A, C30H46O11, and a diterpenoid isolated from Ajuga lupulina with anti-inflammatory and antibacterial activity. Its sole systematic synonym fixes the methoxy-bearing furofuran centre as 5R. No separate structured target, resistance, activity spectrum, producer, product or causal graph objects occur; definition claims are assessed below. |
| owners | data/raw/chebi_antimicrobials.tsv; Full exact source row 1594 and readiness row 1568 | context_only | ChEBI is the actual identity/structure/ontology/citation owner, with four adopted PMIDs. All 13 original capture hashes were preserved; context and actual-owner verification expanded the input set to 21 before detailed judgment. Extraction and seeding are the generated owners. |
| search | /private/tmp/am-review-session/611-context-search.txt; Ignored-inclusive source/context follow-up | context_only | Exact CHEBI:66597 and lupulin A searches included hidden and ignored files in curation, conf, scripts and data/raw. No exact curator or decisions override was found in that scope. The preserved initial local search also remains available. |
| adapter | Native structured-source applicability assessment; Full native definition and fields checked before open research | context_only | No native gene, protein, pathway, regulator or transcriptomic claim is named. iModulonDB is not applicable to the chemical identity and broad activity claims. Host COX assays located in literature are not adopted as antibacterial target evidence. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/66597/; Complete current CHEBI:66597 response | partial | Current ChEBI reproduces native SMILES, InChI, full key, formula, charge, masses, systematic name, four parents and antibacterial role. Its four citation leads and A. lupulina origin association were read. This establishes inherited source state, not independent adjudication of the historical stereochemical correction. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/lupulin%20A/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass/JSON; Additional name lookup CID10841022 | context_only | Both current PubChem encodings reproduce native UEZOFWAZJUOMCN-HKDNVZQMSA-N. This is an additional comparator, not an asserted native PubChem xref. Its agreement does not resolve the primary C-15 conflict. |
| chemistry | /private/tmp/am-review-session/611-authority-map.json; Six actual authority/native encodings, explicit atom neighbourhood and single-centre diagnostic | refutes | Native, ChEBI and PubChem encodings have formula C30H46O11, zero charge, ten assigned and three unassigned tetrahedral centres. Native zero-based SMILES atom 35 is the C-15 methoxy-bearing acetal carbon: bonded to C14 atom 34, methoxy O36 and ring O38 leading to C16 atom 39. Its CIP assignment is R. Inverting only atom 35 gives S and diagnostic key UEZOFWAZJUOMCN-WBWVRVPDSA-N while retaining the other unresolved centres. This diagnostic is not a fully adjudicated replacement graph. Supplied masses and source mint independently pass. |
| parent-23849 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/23849/; Complete current parent definition | supports | The neoclerodane C20 skeleton, with appended ester and methoxy carbons, fits diterpenoid derivation; total C30 count alone was not used. |
| parent-32955 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/32955/; Complete current parent definition | supports | The graph contains the three-membered oxygen epoxide ring. |
| parent-47622 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/47622/; Complete current parent definition | supports | Two acetate ester groups are present. |
| parent-47790 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/47790/; Complete current parent definition | supports | The graph contains the fused furofuran skeleton; the primary paper explicitly identifies its saturated hexahydrofurofuran form. |
| reaxys | Reaxys:8528547; Asserted registry access and source association | unknown | Direct Reaxys access returned 403. The current ChEBI association matches the native accession, but its independent exact structure was not inspected; no chemical equivalence is inferred solely from the propagated registry link. |
| adopted1996 | PMID:8759163; DOI:10.1021/np960385s; Complete original indexed abstract | partial | Whole A. lupulina plants yielded lupulins A–C as compounds1–3. Lupulin A 1, lupulin B 2 and the acid hydrolysate 5 of lupulin D 4 showed antibacterial activity against S. aureus, P. aeruginosa and E. coli. This supports the broad natural-material activity and producer claim, but gives no exact strains, MIC values, medium or exposure time. The publisher main returned 403. |
| adopted2004 | PMID:17191906; DOI:10.1002/cbdv.200490091; Complete original indexed abstract; actual publication 2004 | context_only | The A. bracteosa study isolates known lupulin A alongside new bracteosin withanolides. Reported cholinesterase inhibition belongs to the newly characterized withanolides; it is not transferred to lupulin A. Publisher main returned 403, so detailed lupulin stereochemical characterization was not independently inspected. |
| adopted2008 | PMID:19946570; DOI:10.1016/j.phytol.2008.03.004; https://pmc.ncbi.nlm.nih.gov/articles/PMC2782872/?pdf=1; Original full main: exact compound 6 discussion, Figure 1, plant material and extraction sections | refutes | The exact lupulin A material6 was a 1:2 mixture of C-15 R:S epimers. The authors explicitly identify the previously known lupulin A as the S epimer and distinguish both through proton/carbon NMR signals. They isolated 2.8 mg of6 from 500 g dried A. turkestanica shoots/leaves, collected July 2004 in Uzbekistan (voucher UPL_00057), after methanol extraction and ethyl-acetate partition/fractionation. This is a structural/isolation paper, not a new antibacterial assay, and its mixture is not relabeled as pure native R material. |
| 2008-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/f965/2782872/47dbeafd75e7/nihms77156f1.jpg; Actual Figure 1 viewed locally; compound 6 legend and numbered skeleton | partial | Compound6 has R = OCH3 and R1 = H. The C15 substituent is wavy, matching the reported epimer mixture; C13 and C16 ring-junction hydrogens are drawn stereochemically. The numbered methoxy-bearing C15 corresponds unambiguously to native atom 35. The figure does not itself assert a single C15 configuration for the mixture. |
| correction2009 | https://journals.iucr.org/c/issues/2009/03/00/fg9000/index.html; DOI:10.1107/S0108270108000309; Complete original two-page correction, Comment, Figure 2 caption and note added in proof; web text representation retained | refutes | Molins and Coll explicitly revise lupulin A to the 15α-methoxy neoclerodane structure. They reconcile erroneous older drawings with crystallographic and NOESY evidence, distinguish lupulin D inversion, and identify revised lupulin A with hativene D. This supports the C15 correction independently of current registry agreement. Full text was read through the web tool; local HTML/PDF downloads were 403. The actual 2009 figure pixels and original crystal coordinates were not recovered. |
| adopted2010 | PMID:21073945; DOI:10.1016/j.jep.2010.11.003; Complete original indexed abstract | partial | The 70% ethanolic A. bracteosa extract was tested in TPA mouse ear edema and COX assays. Purified isolates including lupulin A were tested separately at 30 µM and showed weak-to-moderate COX1/2 inhibition; the highest COX2 effect belonged to 6-deoxyharpagide. This supplies bounded host anti-inflammatory context, not a direct bacterial target or proof that purified lupulin A reproduced the extract mouse effect. Exact lupulin percentages and material stereopurity were not recovered. |
| older-crystal | PMID:9208462; DOI:10.1107/S0108270196013637; Complete original indexed abstract and explicitly bounded access attempts | context_only | The 1997 crystal report gives C30H46O11 from fresh A. lupulina with P. aeruginosa/E. coli activity, but uses a nonstandard compound name. Exact lupulin A mapping and conflicting drawings are adjudicated by the later original correction, not assumed from formula alone. IUCr direct access was 403; the indexed CiteSeer PDF route was 404 locally and 403 through the web tool. Original figures/data were not read. |
| structural-review | https://pharmacy.hebmu.edu.cn/trywhx/resources/43/20201911454.pdf; Coll/Tandron Phytochemistry Reviews2008, exact lupulin structural discussion pp33–35 and references | context_only | The secondary review was used only as a discovery lead to original reassignment work and historical drawing conflicts. It is not experimental antibacterial or absolute-configuration evidence. The original 2008 NMR work and2009 correction were subsequently inspected. Unrelated genera and biological tables were not adopted. |
| access | /private/tmp/am-review-session/611-fetch2.json; /private/tmp/am-review-session/611-fetch3.json; /private/tmp/am-review-session/611-fetch6.json; /private/tmp/am-review-session/611-fetch8.json; Actual response manifests and full-text reading boundary | context_only | EPMC fullTextXML failed 500 and BioC 429, while the public PMC HTML query recovered the 2008 main. Its PDF response was challenge HTML. The 1996 and2004 adopted mains returned 403; the 2010 DOI response was a redirect page and the final publisher route 403. The 1999/2004 stereochemistry sources likewise remained inaccessible in full. The 2009 correction was readable through web-rendered original text despite local 403 responses. |

## Limits And Additional Notes

- Focused chemistry, schema and strict checks passed. Required shared full-QC limitations remain recorded separately and prevent completed review status.
- Reaxys returned 403; independent exact registry structure was not inspected. Current ChEBI/PubChem agreement was recorded as source state, not proof against a primary structural correction.
- Adopted 1996,2004 and2010 papers were read through complete original abstracts only; publisher full-text attempts were inaccessible. No exact bacterial strains, MICs, medium, exposure time or purified lupulin A mouse effects were inferred.
- The 2008 paper was read for exact lupulin A discussion, original Figure 1, relevant material/extraction sections and citation context. Raw NMR spectra and all unrelated compound assignments were not reprocessed. Its material is a 1:2 C15 R:S mixture.
- The complete2009 original correction was readable via web text, retained as a tool-derived snapshot; local original HTML/PDF and figure bytes were 403. Original 1997 crystal figures/coordinates and the 1999/2004 reassignment full texts were not recovered. These access limits do not erase the inspected explicit correction, but the remaining full stereochemical replacement requires adjudication.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Original 13 and expanded 21 input hashes were verified unchanged. Native records, maintained source inputs and scientific history were preserved during assessment.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T195945Z-lupulin-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Lupulin A: inherited C-15 epimer conflicts with primary structural reassignment'
started_at: '2026-10-21T19:52:45Z'
finished_at: '2026-10-21T19:59:45Z'
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
summary: The complete native record and actual ChEBI source were assessed. Native
  chemistry is internally coherent and reproduced by current ChEBI and an additional
  PubChem comparator, but encodes C-15 R rather than the revised natural lupulin A
  assignment supported by original NMR work and the published crystallographic correction.
  One wrong-epimer blocker is recorded. Broad antibacterial and plant-origin claims
  have primary support, with exact assay and material boundaries retained.
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
  - path: data/antibiotics/antibacterial/lupulin-a.yaml
    sha256: fdee9412b4d7a4a582266bdb600564d35bbe1cbb00c426a62a2674dbe0e5ad36
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
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
    role: context
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
targets:
- target_id: CHEBI:66597
  path: data/antibiotics/antibacterial/lupulin-a.yaml
  label: lupulin A
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
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Assigned queue position 611; one exact native record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:66597
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0. Actual execution against batch062; chemistry
    used the existing 019 RDKit interpreter and schema/strict used the 062 environment.
  target_ids:
  - CHEBI:66597
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    611
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Actual execution against batch062; chemistry
    used the existing 019 RDKit interpreter and schema/strict used the 062 environment.
  target_ids:
  - CHEBI:66597
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/lupulin-a.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Actual execution against batch062; chemistry
    used the existing 019 RDKit interpreter and schema/strict used the 062 environment.
  target_ids:
  - CHEBI:66597
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/lupulin-a.yaml --out /private/tmp/am-review-session/611-strict.tsv
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
  - CHEBI:66597
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
  - CHEBI:66597
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
  - CHEBI:66597
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
  - CHEBI:66597
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
  - CHEBI:66597
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
  - CHEBI:66597
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
  - CHEBI:66597
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
  - CHEBI:66597
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
  - CHEBI:66597
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/lupulin-a.yaml
  locator: Entire native record and all source/history fields
  accessed_at: '2026-10-21T19:58:27Z'
  support: supports
  summary: The record claims exact neutral lupulin A, C30H46O11, and a diterpenoid
    isolated from Ajuga lupulina with anti-inflammatory and antibacterial activity.
    Its sole systematic synonym fixes the methoxy-bearing furofuran centre as 5R.
    No separate structured target, resistance, activity spectrum, producer, product
    or causal graph objects occur; definition claims are assessed below.
  snapshot_sha256: fdee9412b4d7a4a582266bdb600564d35bbe1cbb00c426a62a2674dbe0e5ad36
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Full exact source row 1594 and readiness row 1568
  accessed_at: '2026-10-21T19:58:27Z'
  support: context_only
  summary: ChEBI is the actual identity/structure/ontology/citation owner, with four
    adopted PMIDs. All 13 original capture hashes were preserved; context and actual-owner
    verification expanded the input set to 21 before detailed judgment. Extraction
    and seeding are the generated owners.
  snapshot_sha256: 3b2c74cc18e7c97b2ed9856854021e2bdc2db77cdb24b40da93598b8b940cb35
- evidence_id: search
  kind: search
  reference: /private/tmp/am-review-session/611-context-search.txt
  locator: Ignored-inclusive source/context follow-up
  accessed_at: '2026-10-21T19:58:27Z'
  support: context_only
  summary: Exact CHEBI:66597 and lupulin A searches included hidden and ignored files
    in curation, conf, scripts and data/raw. No exact curator or decisions override
    was found in that scope. The preserved initial local search also remains available.
  snapshot_sha256: e4659bf875fcc2eb8f57ace4c1518f90c1d1a3bc5a4f02dec8bf5cd66e8c70c6
  search_scope: rg --no-ignore --hidden -n -i for CHEBI:66597 and lupulin A in curation,
    conf, scripts and data/raw, plus initial local hits.
- evidence_id: adapter
  kind: search
  reference: Native structured-source applicability assessment
  locator: Full native definition and fields checked before open research
  accessed_at: '2026-10-21T19:58:27Z'
  support: context_only
  summary: No native gene, protein, pathway, regulator or transcriptomic claim is
    named. iModulonDB is not applicable to the chemical identity and broad activity
    claims. Host COX assays located in literature are not adopted as antibacterial
    target evidence.
  snapshot_sha256: fdee9412b4d7a4a582266bdb600564d35bbe1cbb00c426a62a2674dbe0e5ad36
  search_scope: Complete native field set and definition; no named protein/pathway
    claim.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/66597/
  locator: Complete current CHEBI:66597 response
  accessed_at: '2026-10-21T19:53:17.583253Z'
  support: partial
  summary: Current ChEBI reproduces native SMILES, InChI, full key, formula, charge,
    masses, systematic name, four parents and antibacterial role. Its four citation
    leads and A. lupulina origin association were read. This establishes inherited
    source state, not independent adjudication of the historical stereochemical correction.
  snapshot_sha256: 60aa00a000fc7518d4f7b783029f69d88e9bd65b9b473b8f490305a42ab131d3
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/lupulin%20A/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass/JSON
  locator: Additional name lookup CID10841022
  accessed_at: '2026-10-21T19:53:17.584614Z'
  support: context_only
  summary: Both current PubChem encodings reproduce native UEZOFWAZJUOMCN-HKDNVZQMSA-N.
    This is an additional comparator, not an asserted native PubChem xref. Its agreement
    does not resolve the primary C-15 conflict.
  snapshot_sha256: 6d120894279b9f2a7abf6e09d80746033126d292fa5e4d3761807095cb8e53d5
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/am-review-session/611-authority-map.json
  locator: Six actual authority/native encodings, explicit atom neighbourhood and
    single-centre diagnostic
  accessed_at: '2026-10-21T19:58:27Z'
  support: refutes
  summary: 'Native, ChEBI and PubChem encodings have formula C30H46O11, zero charge,
    ten assigned and three unassigned tetrahedral centres. Native zero-based SMILES
    atom 35 is the C-15 methoxy-bearing acetal carbon: bonded to C14 atom 34, methoxy
    O36 and ring O38 leading to C16 atom 39. Its CIP assignment is R. Inverting only
    atom 35 gives S and diagnostic key UEZOFWAZJUOMCN-WBWVRVPDSA-N while retaining
    the other unresolved centres. This diagnostic is not a fully adjudicated replacement
    graph. Supplied masses and source mint independently pass.'
  snapshot_sha256: cc9575feb1e9388b374a9a1f21281ecf174921d3cc79c33a0117af87e6fff5a0
- evidence_id: parent-23849
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/23849/
  locator: Complete current parent definition
  accessed_at: '2026-10-21T19:53:17.671615Z'
  support: supports
  summary: The neoclerodane C20 skeleton, with appended ester and methoxy carbons,
    fits diterpenoid derivation; total C30 count alone was not used.
  snapshot_sha256: 3b6a2e13ca544afbd9daf2a267be671e1aadba586a4082e7ef10792eb2bcd22e
- evidence_id: parent-32955
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/32955/
  locator: Complete current parent definition
  accessed_at: '2026-10-21T19:53:18.072258Z'
  support: supports
  summary: The graph contains the three-membered oxygen epoxide ring.
  snapshot_sha256: 6ee823580e8a06a022a9f591342ebc5e26b244c64a4a515f6ffd9844b1270d20
- evidence_id: parent-47622
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/47622/
  locator: Complete current parent definition
  accessed_at: '2026-10-21T19:53:18.255503Z'
  support: supports
  summary: Two acetate ester groups are present.
  snapshot_sha256: 920adf6e3ca4fd81d4289410e249bcd5893dadac27014a9f753d82df2883a005
- evidence_id: parent-47790
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/47790/
  locator: Complete current parent definition
  accessed_at: '2026-10-21T19:53:18.336732Z'
  support: supports
  summary: The graph contains the fused furofuran skeleton; the primary paper explicitly
    identifies its saturated hexahydrofurofuran form.
  snapshot_sha256: f5c4a7a873afa2b625400eaee840e32a9eb162305ede09633841077da9c6f1cc
- evidence_id: reaxys
  kind: authority
  reference: Reaxys:8528547
  locator: Asserted registry access and source association
  accessed_at: '2026-10-21T19:58:27Z'
  support: unknown
  summary: Direct Reaxys access returned 403. The current ChEBI association matches
    the native accession, but its independent exact structure was not inspected; no
    chemical equivalence is inferred solely from the propagated registry link.
  snapshot_sha256: 470b33a2153893fda24771b87699be213b8668bc3804dbcc347ee85491f4abab
- evidence_id: adopted1996
  kind: primary_source
  reference: PMID:8759163; DOI:10.1021/np960385s
  locator: Complete original indexed abstract
  accessed_at: '2026-10-21T19:53:17.587360Z'
  support: partial
  summary: Whole A. lupulina plants yielded lupulins A–C as compounds1–3. Lupulin
    A 1, lupulin B 2 and the acid hydrolysate 5 of lupulin D 4 showed antibacterial
    activity against S. aureus, P. aeruginosa and E. coli. This supports the broad
    natural-material activity and producer claim, but gives no exact strains, MIC
    values, medium or exposure time. The publisher main returned 403.
  snapshot_sha256: b20bf259066b91764a029a59122f78b9b4fe03058a6270646612e42808fc89f3
- evidence_id: adopted2004
  kind: primary_source
  reference: PMID:17191906; DOI:10.1002/cbdv.200490091
  locator: Complete original indexed abstract; actual publication 2004
  accessed_at: '2026-10-21T19:53:17.587360Z'
  support: context_only
  summary: The A. bracteosa study isolates known lupulin A alongside new bracteosin
    withanolides. Reported cholinesterase inhibition belongs to the newly characterized
    withanolides; it is not transferred to lupulin A. Publisher main returned 403,
    so detailed lupulin stereochemical characterization was not independently inspected.
  snapshot_sha256: b20bf259066b91764a029a59122f78b9b4fe03058a6270646612e42808fc89f3
- evidence_id: adopted2008
  kind: primary_source
  reference: PMID:19946570; DOI:10.1016/j.phytol.2008.03.004; https://pmc.ncbi.nlm.nih.gov/articles/PMC2782872/?pdf=1
  locator: 'Original full main: exact compound 6 discussion, Figure 1, plant material
    and extraction sections'
  accessed_at: '2026-10-21T19:55:22.875018Z'
  support: refutes
  summary: The exact lupulin A material6 was a 1:2 mixture of C-15 R:S epimers. The
    authors explicitly identify the previously known lupulin A as the S epimer and
    distinguish both through proton/carbon NMR signals. They isolated 2.8 mg of6 from
    500 g dried A. turkestanica shoots/leaves, collected July 2004 in Uzbekistan (voucher
    UPL_00057), after methanol extraction and ethyl-acetate partition/fractionation.
    This is a structural/isolation paper, not a new antibacterial assay, and its mixture
    is not relabeled as pure native R material.
  snapshot_sha256: 12b7f6e7cbd69835bafd455c284f32cd01bd8ab9cb7b365b4056a2552b7c80b9
- evidence_id: 2008-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/f965/2782872/47dbeafd75e7/nihms77156f1.jpg
  locator: Actual Figure 1 viewed locally; compound 6 legend and numbered skeleton
  accessed_at: '2026-10-21T19:55:44.750020Z'
  support: partial
  summary: Compound6 has R = OCH3 and R1 = H. The C15 substituent is wavy, matching
    the reported epimer mixture; C13 and C16 ring-junction hydrogens are drawn stereochemically.
    The numbered methoxy-bearing C15 corresponds unambiguously to native atom 35.
    The figure does not itself assert a single C15 configuration for the mixture.
  snapshot_sha256: 608fbe217ec146510eeee753893c9f881832e187bfc6ab885772579ed1319712
- evidence_id: correction2009
  kind: primary_source
  reference: https://journals.iucr.org/c/issues/2009/03/00/fg9000/index.html; DOI:10.1107/S0108270108000309
  locator: Complete original two-page correction, Comment, Figure 2 caption and note
    added in proof; web text representation retained
  accessed_at: '2026-10-21T19:58:27Z'
  support: refutes
  summary: Molins and Coll explicitly revise lupulin A to the 15α-methoxy neoclerodane
    structure. They reconcile erroneous older drawings with crystallographic and NOESY
    evidence, distinguish lupulin D inversion, and identify revised lupulin A with
    hativene D. This supports the C15 correction independently of current registry
    agreement. Full text was read through the web tool; local HTML/PDF downloads were
    403. The actual 2009 figure pixels and original crystal coordinates were not recovered.
  snapshot_sha256: 2c0eb2b1c8450118ce77465500863867655f5fb8da29c50b9c39e387c24134d2
- evidence_id: adopted2010
  kind: primary_source
  reference: PMID:21073945; DOI:10.1016/j.jep.2010.11.003
  locator: Complete original indexed abstract
  accessed_at: '2026-10-21T19:53:17.587360Z'
  support: partial
  summary: The 70% ethanolic A. bracteosa extract was tested in TPA mouse ear edema
    and COX assays. Purified isolates including lupulin A were tested separately at
    30 µM and showed weak-to-moderate COX1/2 inhibition; the highest COX2 effect belonged
    to 6-deoxyharpagide. This supplies bounded host anti-inflammatory context, not
    a direct bacterial target or proof that purified lupulin A reproduced the extract
    mouse effect. Exact lupulin percentages and material stereopurity were not recovered.
  snapshot_sha256: b20bf259066b91764a029a59122f78b9b4fe03058a6270646612e42808fc89f3
- evidence_id: older-crystal
  kind: primary_source
  reference: PMID:9208462; DOI:10.1107/S0108270196013637
  locator: Complete original indexed abstract and explicitly bounded access attempts
  accessed_at: '2026-10-21T19:53:36.457166Z'
  support: context_only
  summary: The 1997 crystal report gives C30H46O11 from fresh A. lupulina with P.
    aeruginosa/E. coli activity, but uses a nonstandard compound name. Exact lupulin
    A mapping and conflicting drawings are adjudicated by the later original correction,
    not assumed from formula alone. IUCr direct access was 403; the indexed CiteSeer
    PDF route was 404 locally and 403 through the web tool. Original figures/data
    were not read.
  snapshot_sha256: d070ae35f04f49361897765cc16a01622e78aef0812a2940c313e1ba3edbff2b
- evidence_id: structural-review
  kind: database
  reference: https://pharmacy.hebmu.edu.cn/trywhx/resources/43/20201911454.pdf
  locator: Coll/Tandron Phytochemistry Reviews2008, exact lupulin structural discussion
    pp33–35 and references
  accessed_at: '2026-10-21T19:55:35.583836Z'
  support: context_only
  summary: The secondary review was used only as a discovery lead to original reassignment
    work and historical drawing conflicts. It is not experimental antibacterial or
    absolute-configuration evidence. The original 2008 NMR work and2009 correction
    were subsequently inspected. Unrelated genera and biological tables were not adopted.
  snapshot_sha256: 6307a93ede566342f9b7aea16fc67f80055a3b11e0534fc1bf0305b180a0e5dd
- evidence_id: access
  kind: validation
  reference: /private/tmp/am-review-session/611-fetch2.json; /private/tmp/am-review-session/611-fetch3.json;
    /private/tmp/am-review-session/611-fetch6.json; /private/tmp/am-review-session/611-fetch8.json
  locator: Actual response manifests and full-text reading boundary
  accessed_at: '2026-10-21T19:58:27Z'
  support: context_only
  summary: EPMC fullTextXML failed 500 and BioC 429, while the public PMC HTML query
    recovered the 2008 main. Its PDF response was challenge HTML. The 1996 and2004
    adopted mains returned 403; the 2010 DOI response was a redirect page and the
    final publisher route 403. The 1999/2004 stereochemistry sources likewise remained
    inaccessible in full. The 2009 correction was readable through web-rendered original
    text despite local 403 responses.
  snapshot_sha256: 2d5f3c4c56f51b3e521c21ffbad3680ac10b387bfeb9cb0302d789153ceb16cf
assessments:
- assessment_id: identity
  area: identity
  topic: C15 assignment and unresolved remaining centres
  outcome: concern
  summary: 'Internal graph agreement is not sufficient: native C15 R conflicts with
    the original 2008 identification of natural lupulin A as S and the later explicit
    structural correction. The three unspecified native centres remain distinct from
    this affirmative wrong assignment; they are not called a racemate or automatically
    filled. A one-centre scratch diagnostic does not establish the complete corrected
    natural graph.'
  target_ids:
  - CHEBI:66597
  evidence_ids:
  - native
  - chemistry
  - adopted2008
  - 2008-figure
  - correction2009
- assessment_id: grounding
  area: grounding
  topic: Current chemical authorities and ontology
  outcome: concern
  summary: Current ChEBI and PubChem retain the historical C15 encoding, explaining
    propagation without resolving the primary contradiction. Four parent skeleton/function
    classifications fit the graph. Reaxys exact structural content remains uninspected.
    No unrelated PubChem xref finding is created because PubChem is only a comparator.
  target_ids:
  - CHEBI:66597
  evidence_ids:
  - chebi
  - pubchem
  - chemistry
  - parent-23849
  - parent-32955
  - parent-47622
  - parent-47790
  - reaxys
- assessment_id: evidence
  area: evidence
  topic: Activity, producer and host-effect claim boundaries
  outcome: supported
  summary: The 1996 primary abstract supports broad antibacterial activity and A.
    lupulina isolation of named lupulin A. Exact species-level activity is not converted
    to strain-level MICs without methods, and exact graph transfer remains contingent
    on identity correction. The 2010 host COX evidence supports limited anti-inflammatory
    context, with extract mouse results separated from purified compound tests.
  target_ids:
  - CHEBI:66597
  evidence_ids:
  - adopted1996
  - adopted2008
  - adopted2010
  - older-crystal
- assessment_id: completeness
  area: completeness
  topic: Optional mechanism and quantitative enrichment
  outcome: unknown
  summary: No required missing optional field is established. Exact antibacterial
    assay methods, material stereopurity and complete corrected stereochemistry require
    follow-up before quantitative enrichment. The adopted withanolide cholinesterase
    results and host COX effects do not establish a lupulin A antibacterial protein
    target.
  target_ids:
  - CHEBI:66597
  evidence_ids:
  - adopted1996
  - adopted2004
  - adopted2008
  - adopted2010
  - access
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Maintained source ownership and all adopted citations
  outcome: supported
  summary: All four adopted PMIDs were resolved with complete original abstracts;
    relevant full 2008 material and the additional original 2009 correction were inspected.
    Entire native history and original 13/expanded 21 owner hashes remain unchanged.
    Scientific corrections belong in maintained source handling, with generated YAML
    reproduced by seeding.
  target_ids:
  - CHEBI:66597
  evidence_ids:
  - native
  - owners
  - search
  - chebi
  - adopted1996
  - adopted2004
  - adopted2008
  - adopted2010
findings:
- finding_id: F1
  issue_key: lupulin-a-c15-unrevised-epimer
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The native structure encodes the unrevised C15 epimer
  description: The methoxy-bearing C15 carbon is R in both native encodings and in
    the exact systematic synonym. Original NMR work identifies previously known lupulin
    A as C15 S, and the published structural correction expressly revises lupulin
    A to the corresponding 15α-methoxy neoclerodane. Current ChEBI/PubChem agreement
    reproduces the historical discrepancy. The affirmative wrong C15 assignment is
    distinct from the three remaining unassigned centres; the observed R:S mixture
    in a separate 2008 isolation does not make the original named natural compound
    a pure R epimer.
  target_ids:
  - CHEBI:66597
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  - synonyms[0].synonym_text
  - grounding_status
  evidence_ids:
  - native
  - owners
  - chemistry
  - adopted2008
  - 2008-figure
  - correction2009
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
  rule_id: 'review-yaml-record: wrong exact chemical identity'
  normalization_reason: 'Blocker under the explicit wrong-identity rubric: a specified
    stereocentre denotes a different epimer. This is not a finding based only on unspecified
    stereochemistry, rotation sign or database disagreement.'
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - CHEBI:66597
  description: Adjudicate the full revised lupulin A structure through maintained
    ChEBI source handling and regenerate the exact record.
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
  generator: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  acceptance_checks:
  - Map the primary numbered C15 to the methoxy-bearing native atom 35 and apply the
    explicit original reassignment, preserving its primary provenance.
  - Independently resolve C13/C16 and ester side-chain stereochemistry before declaring
    a fully corrected natural graph. Do not treat the one-centre diagnostic key as
    a complete replacement or copy an unverified secondary graph.
  - Update systematic synonym and all structure encodings coherently; compare current
    authority associations without silently substituting propagated erroneous chemistry.
  - Preserve the 2008 R:S mixture as separate material context and recover original
    assay methods before transferring quantitative antibacterial results.
  - Regenerate, rerun required validators and verify formula, charge, masses, full
    key, source ownership and exact xrefs.
limitations:
- Focused chemistry, schema and strict checks passed. Required shared full-QC limitations
  remain recorded separately and prevent completed review status.
- Reaxys returned 403; independent exact registry structure was not inspected. Current
  ChEBI/PubChem agreement was recorded as source state, not proof against a primary
  structural correction.
- Adopted 1996,2004 and2010 papers were read through complete original abstracts only;
  publisher full-text attempts were inaccessible. No exact bacterial strains, MICs,
  medium, exposure time or purified lupulin A mouse effects were inferred.
- The 2008 paper was read for exact lupulin A discussion, original Figure 1, relevant
  material/extraction sections and citation context. Raw NMR spectra and all unrelated
  compound assignments were not reprocessed. Its material is a 1:2 C15 R:S mixture.
- The complete2009 original correction was readable via web text, retained as a tool-derived
  snapshot; local original HTML/PDF and figure bytes were 403. Original 1997 crystal
  figures/coordinates and the 1999/2004 reassignment full texts were not recovered.
  These access limits do not erase the inspected explicit correction, but the remaining
  full stereochemical replacement requires adjudication.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Original 13 and expanded 21 input hashes were verified unchanged. Native records,
  maintained source inputs and scientific history were preserved during assessment.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
