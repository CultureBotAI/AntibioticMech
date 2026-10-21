# Review of fasamycin I

- Review: 20261021T160837Z-fasamycin-i-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:38:22Z
- Finished UTC: 2026-10-21T16:08:37Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Fasamycin I has consistent native/current ARO, ChEBI and PubChem identity. Seven molecular encodings agree on the reported neutral connectivity and formula, and original compound 3 spectral illustrations agree with its substitution pattern. The adopted definition accurately reports family naming history; the underlying FabF experiments concern A/B and do not establish a separate I target edge. Exact strain-level MICs and full axial stereochemical encoding remain unverified. No demonstrated native correction was established. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole SEEDED, MINTED fasamycin I record: family-history definition and PMID, ARO class/parent, full structure, all three xrefs, source concept and three histories. Exact congener discovery, spectral identity, family mechanism evidence and current structural revision scope reviewed.

Selection: Queue 430 in isolated batch 043. Initial 13 hashes preserved and three actual ARO/PubChem owners appended before detailed assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-4406f1da89 | data/antibiotics/antibacterial/fasamycin-i.yaml | generated | fasamycin I |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native schema | passed | True | antibioticmech:aro-4406f1da89 | Exit 0. |
| Native strict terms | passed | True | antibioticmech:aro-4406f1da89 | Exit 0; no ERROR rows. |
| Native molecular consistency | passed | False | antibioticmech:aro-4406f1da89 | Native structure, formula, charge, masses and minted identifier agree. |
| Independent authority graph comparison | passed | False | antibioticmech:aro-4406f1da89 | Seven encodings agree by full reciprocal graph matching; axial chirality is outside this standard-encoding comparison. |
| Whole source and reference ledger | passed | False | antibioticmech:aro-4406f1da89 | All 16 hashes unchanged; sole adopted lead disposed, actual source fields reconciled and three histories checked. |
| Structured source coverage | passed | False | antibioticmech:aro-4406f1da89 | Exit 0; covered E. coli and S. aureus datasets identified before mechanism search. |
| Structured FabF gene lookup | passed | False | antibioticmech:aro-4406f1da89 | Exit 0; b1095 gene hit, zero iModulon hits. |
| Structured FabF gene lookup | passed | False | antibioticmech:aro-4406f1da89 | Exit 0; USA300HOU_RS04880 gene hit, zero iModulon hits. |
| Authoritative full QC | failed | True | antibioticmech:aro-4406f1da89 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-4406f1da89 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-4406f1da89 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-4406f1da89 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-4406f1da89 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-4406f1da89 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-4406f1da89 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-4406f1da89 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-4406f1da89 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact congener connectivity and formula

identity: supported. Targets: antibioticmech:aro-4406f1da89.

All authorities and the original compound 3 drawings agree on the reported I substitution pattern and formula.

### Axial configuration and encoding

representation: unknown. Targets: antibioticmech:aro-4406f1da89.

Standard graph concordance does not encode or prove the natural axial state. Original configurational text and a validated axial representation remain follow-up; no mixture or opposite-isomer claim follows.

### ARO class and exact xrefs

grounding: supported. Targets: antibioticmech:aro-4406f1da89.

All three native links resolve to the named congener; class-parent transformation matches the maintained seeder. MINTED status is preserved.

### Family naming and FabF context

evidence: supported. Targets: antibioticmech:aro-4406f1da89.

The adopted source supports the historical family statement. A/B mechanism experiments remain bounded to A/B; no dedicated exact-congener target edge is asserted.

### Exact-congener FabF inhibition

evidence: unknown. Targets: antibioticmech:aro-4406f1da89.

Independent FabF inhibition for I was not established; family similarity and gene presence are insufficient for a new direct-binding claim.

### Antibacterial classification

evidence: supported. Targets: antibioticmech:aro-4406f1da89.

The original discovery includes the exact congener in its antibacterial compound panel; no numerical strain-specific value or clinical efficacy is inferred.

### Individual MIC and strain context

quantity: unknown. Targets: antibioticmech:aro-4406f1da89.

The original main assay table was not independently retrieved; panel ranges and 2023 glycoside assays cannot supply an exact native MIC.

### Later congener structural revisions

scope: supported. Targets: antibioticmech:aro-4406f1da89.

The newer original was checked and its specific corrections were not generalized to unmeasured G/H/I structures.

### Optional evidence enrichment

completeness: supported. Targets: antibioticmech:aro-4406f1da89.

A compound-specific definition could cite the discovery and explain axial scope, but no demonstrated required native defect is established. Any quantitative/target enrichment needs exact material and experiment support.

### Inputs, source claims and history

ownership: supported. Targets: antibioticmech:aro-4406f1da89.

Actual owners, all16 unchanged hashes and three chronological histories reconcile.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/fasamycin-i.yaml; Entire native YAML | supports | The exact named congener is MINTED from ARO:3007579. Its definition is explicitly about fasamycin family naming, not a dedicated experimentally supported I molecular-target edge. No quantitative MIC, resistance, producer or clinical-status objects are present. |
| chemistry | CHEBI:226614; PubChem CID156012442; 430-chebi.json/.mol;430-pubchem.json/.sdf;430-authority-chemistry.json | supports | Native SMILES/InChI, ChEBI SMILES/molfile and PubChem SMILES/InChI/SDF give ASZOUSIHEISETE-UHFFFAOYSA-N and neutral C29H25ClO7. Complete reciprocal graph mappings agree, with one chlorine, two methoxy groups and four phenolic hydroxyls. The exact ChEBI entry is a two-star submission and PubChem shares adopted provenance; database concordance is not independent experimental proof. No tetrahedral centers are present, while axial configuration is not resolved by these standard encodings. |
| aro | ARO:3007579; ARO:3007573; ARO:3005171; 430-aro-blocks.txt extracted from374-current-aro.obo;374-fetch-results.json | supports | Current ARO retains the same congener label, definition PMID, exact ChEBI/PubChem xrefs and fasamycin parent. The broader polyketide-with-antibiotic-activity term resolves correctly. The seeder intentionally selects the drug class as the native parent, rather than the immediate raw ARO parent. |
| adopted | PMID:37327570; DOI:10.1021/acs.jnatprod.3c00052; 428-PMC10391614.xml introduction, selected material-identification/results and Antibacterial Assays section | supports | The original introduction gives the same family naming/history sentence and cites the 2012 A/B study. Its experimental glycosides derive from C/D/J aglycones and are distinct from G/H/I. Its described antibacterial assay uses spotted material and clearance zones; those results are not silently transformed into G/H/I MICs or direct FabF inhibition. |
| fabf | PMID:22224500; DOI:10.1021/ja207662w; 428-PMC3335777.html/.txt selected isolation, FASII assays, FabT/FabF experiments and docking methods/results;426-2012-nihms354784f6.jpg Figure6b visually inspected;426-fetch3-results.json | context_only | The original studies A and B. Both inhibit S. aureus FASII extract elongation. The resolved ACP gel and Figure 6a growth plate are A-specific. Figure 6b reports FabF-overexpression/WT MIC ratios of 2.5 for A and 2.0 for B, with FabH/WT ratios of 1 for both. FabT mutants and docking support distinct mechanistic steps, with docking remaining predictive. These experiments explain the family history but were not conducted on the present G/H/I congeners. |
| discovery | PMID:32519857; DOI:10.1021/acs.jnatprod.0c00161; 428-core-32519857.json complete original abstract; compound 3 mapping | supports | The discovery paper identifies fasamycins G–K as compounds 1–5 from Streptomyces sp. KIB-1414, including I as compound 3. Its abstract reports antibacterial testing across the isolated panel. The whole-panel MIC range does not establish an individual I/strain value; the main assay table and exact configurational argument were not retrieved. |
| spectra | DOI:10.1021/acs.jnatprod.0c00161.s001; 428-2020-si.pdf pp.S16/S19: compound 3 drawings, proton/carbon NMR and HRESIMS;430-si-p16.png;430-si-p19.png | supports | The original compound 3 spectral pages were visually inspected. The depicted substitution pattern agrees with the native, including one chlorine, two methoxy groups and four phenolic hydroxyls. HRESIMS reports [M−H]− m/z 519.1213, consistent with the neutral formula; the detected ion does not change record charge. The drawings use a bold hanging-ring depiction. Its exact axial meaning was not independently translated into a machine-readable stereodescriptor; full de novo NMR elucidation is not claimed. |
| revision | PMID:41988676; DOI:10.1021/acs.jnatprod.6c00145; 428-PMC13532170.xml selected structural-revision/axial-chirality Results;428-2026-original.pdf available for reinspection | context_only | The 2026 original revises specified S. formicae congeners, including C/E/L/N/Q and a proposed D reassignment. It does not report a G/H/I-specific regiochemical correction or crystal determination. Measured congeners support Sa axial chirality, and the authors extend a family hypothesis. Neither a methoxy-position change nor a racemic-mixture interpretation is imposed on this native from those adjacent results. |
| adapter | iModulonDB e_coli/precise1k/b1095; s_aureus/staph_precise108/USA300HOU_RS04880; 428-adapter-datasets.json;428-adapter-fabF-ecoli.txt;428-adapter-fabF-saureus.txt | context_only | Structured lookup preceded open protein literature. Both datasets contain a FabF gene entry and neither search returns an iModulon hit. This verifies gene-label context only, not fasamycin binding, susceptibility or the exact target relation for this congener. |
| owners | Actual ARO/PubChem maintained inputs and transforms; 430-owner-append.json;430-raw-rows.json;430-source-audit.json;seed_from_sources.py lines785–840 | supports | All 13 initial hashes were retained and three actual owner inputs added, giving 16 unchanged hashes. ARO owns definition/class/citation/xrefs; PubChem enrichment owns the structure. Generated native fields and all three histories reconcile. The original generic ChEBI capture is preserved in provenance while target ownership names the actual source. Sole adopted PMID coverage is explicit. |
| validation | Focused native and scientific consistency checks; 430-focused-results.json;430-strict.tsv;430-authority-chemistry.log;430-ledger.log | supports | Schema, strict terms, native molecular consistency, authority graph comparison and exact source ledger all passed. The graph checks do not test absent axial encoding or provide exact-congener mechanism evidence. |
| access | Bounded public exact-congener research; 430-local-hits.txt includes ignored files;428-fetch.json through428-fetch8.json;428-2020-openalex.json;428-2020-semantic.json | context_only | The 2020 main paper remained closed or returned 403; its public official supplement was retrieved through Figshare. The original 2012 EPMC XML request failed500, followed by a successful PMC HTML retrieval. The 2023 and 2026 originals were read from public XML. Search leads and inaccessible main-table details are not substituted with commercial summaries. |

## Limits And Additional Notes

- The 2020 original discovery abstract and compound 3 spectral drawings/HRESIMS pages were inspected. Its main MIC table, strain-level method details and exact configurational argument were unavailable.
- The original 2012 experiments were inspected as A/B mechanism context. They do not establish direct FabF binding or inhibition for this exact congener.
- Standard native/authority encodings lack an explicit axial designation. The bold original drawing and later family stereochemistry discussion are recorded; no racemate, opposite axial isomer or experimentally determined G/H/I crystal is inferred.
- The 2026 regiochemical corrections concern specified other congeners. The full original spectral dataset was not reprocessed, and an adjacent correction is not automatically a correction to this record.
- The broad activity panel in the discovery abstract is not a per-organism numerical result. No susceptibility-breakpoint, clinical efficacy or producer-strain biosynthetic claim is added.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- The structured adapter was run before protein-specific open literature follow-up. No matching iModulon component was returned, so no component summary was applicable.
- Standalone chemistry used the batch 019 interpreter against batch 043; native checks and source ledger used batch 043.
- An optional future definition may distinguish the exact congener discovery from historical A/B FabF evidence and record the validated axial stereochemistry in a suitable supported representation.
- No native content, scientific status or immutable bundle was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T160837Z-fasamycin-i-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of fasamycin I
started_at: '2026-10-21T15:38:22Z'
finished_at: '2026-10-21T16:08:37Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Entire native and actual source rows read; independent chemical
    parsing with atom mappings, original discovery spectra and selected mechanism
    experiments inspected. Structured gene searches preceded protein literature follow-up.
    Family evidence and exact-congener experiments were kept separate.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: Published connectivity and family-history definition supported; exact
  mechanism and axial encoding remain bounded
scientific_review: true
summary: Fasamycin I has consistent native/current ARO, ChEBI and PubChem identity.
  Seven molecular encodings agree on the reported neutral connectivity and formula,
  and original compound 3 spectral illustrations agree with its substitution pattern.
  The adopted definition accurately reports family naming history; the underlying
  FabF experiments concern A/B and do not establish a separate I target edge. Exact
  strain-level MICs and full axial stereochemical encoding remain unverified. No demonstrated
  native correction was established. Scientific assessment retains the stated evidence
  limits; full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/fasamycin-i.yaml
    sha256: db2035f733cd1cdce4d55f8212de5142c9be2f50a444acba3daa2d9b5f826168
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
  - path: data/raw/aro_antibiotics.tsv
    role: context
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
  - path: data/raw/pubchem_structures.tsv
    role: context
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
  - path: scripts/enrich_pubchem_structures.py
    role: context
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
scope:
  description: 'Whole SEEDED, MINTED fasamycin I record: family-history definition
    and PMID, ARO class/parent, full structure, all three xrefs, source concept and
    three histories. Exact congener discovery, spectral identity, family mechanism
    evidence and current structural revision scope reviewed.'
  selection: Queue 430 in isolated batch 043. Initial 13 hashes preserved and three
    actual ARO/PubChem owners appended before detailed assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-4406f1da89
targets:
- target_id: antibioticmech:aro-4406f1da89
  path: data/antibiotics/antibacterial/fasamycin-i.yaml
  label: fasamycin I
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained CARD/ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact PubChem structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained PubChem enrichment owner
checks:
- check_id: schema
  name: Native schema
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/fasamycin-i.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - validation
- check_id: strict
  name: Native strict terms
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/fasamycin-i.yaml --out /private/tmp/am-review-session/430-strict.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no ERROR rows.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - validation
- check_id: native-chemistry
  name: Native molecular consistency
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    430 > /private/tmp/am-review-session/430-focused-run.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Native structure, formula, charge, masses and minted identifier agree.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - chemistry
  - validation
- check_id: authority-chemistry
  name: Independent authority graph comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/428-authority-chemistry.py
    430 > /private/tmp/am-review-session/430-authority-chemistry.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Seven encodings agree by full reciprocal graph matching; axial chirality
    is outside this standard-encoding comparison.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - chemistry
- check_id: source-ledger
  name: Whole source and reference ledger
  command: .venv/bin/python /private/tmp/am-review-session/428-ledger.py 430 > /private/tmp/am-review-session/430-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All 16 hashes unchanged; sole adopted lead disposed, actual source fields
    reconciled and three histories checked.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - owners
  - adopted
- check_id: adapter-datasets
  name: Structured source coverage
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets > /private/tmp/am-review-session/428-adapter-datasets.json
    2> /private/tmp/am-review-session/428-adapter-datasets.err
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; covered E. coli and S. aureus datasets identified before mechanism
    search.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - adapter
- check_id: adapter-ecoli
  name: Structured FabF gene lookup
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism e_coli --dataset precise1k --query fabF > /private/tmp/am-review-session/428-adapter-fabF-ecoli.txt
    2> /private/tmp/am-review-session/428-adapter-fabF-ecoli.err
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; b1095 gene hit, zero iModulon hits.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - adapter
- check_id: adapter-saureus
  name: Structured FabF gene lookup
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb search --organism s_aureus --dataset staph_precise108 --query fabF
    > /private/tmp/am-review-session/428-adapter-fabF-saureus.txt 2> /private/tmp/am-review-session/428-adapter-fabF-saureus.err
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; USA300HOU_RS04880 gene hit, zero iModulon hits.
  target_ids:
  - antibioticmech:aro-4406f1da89
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
  - antibioticmech:aro-4406f1da89
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
  - antibioticmech:aro-4406f1da89
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
  - antibioticmech:aro-4406f1da89
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
  - antibioticmech:aro-4406f1da89
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
  - antibioticmech:aro-4406f1da89
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
  - antibioticmech:aro-4406f1da89
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
  - antibioticmech:aro-4406f1da89
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
  - antibioticmech:aro-4406f1da89
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
  - antibioticmech:aro-4406f1da89
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/fasamycin-i.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T15:55:36Z'
  support: supports
  summary: The exact named congener is MINTED from ARO:3007579. Its definition is
    explicitly about fasamycin family naming, not a dedicated experimentally supported
    I molecular-target edge. No quantitative MIC, resistance, producer or clinical-status
    objects are present.
- evidence_id: chemistry
  kind: authority
  reference: CHEBI:226614; PubChem CID156012442
  locator: 430-chebi.json/.mol;430-pubchem.json/.sdf;430-authority-chemistry.json
  accessed_at: '2026-10-21T15:55:36Z'
  support: supports
  summary: Native SMILES/InChI, ChEBI SMILES/molfile and PubChem SMILES/InChI/SDF
    give ASZOUSIHEISETE-UHFFFAOYSA-N and neutral C29H25ClO7. Complete reciprocal graph
    mappings agree, with one chlorine, two methoxy groups and four phenolic hydroxyls.
    The exact ChEBI entry is a two-star submission and PubChem shares adopted provenance;
    database concordance is not independent experimental proof. No tetrahedral centers
    are present, while axial configuration is not resolved by these standard encodings.
  snapshot_sha256: ae8cddc9bb1a8376071d1ddd83651701a5af54422f03e74f683080277ca9af81
- evidence_id: aro
  kind: authority
  reference: ARO:3007579; ARO:3007573; ARO:3005171
  locator: 430-aro-blocks.txt extracted from374-current-aro.obo;374-fetch-results.json
  accessed_at: '2026-10-21T14:50:57Z'
  support: supports
  summary: Current ARO retains the same congener label, definition PMID, exact ChEBI/PubChem
    xrefs and fasamycin parent. The broader polyketide-with-antibiotic-activity term
    resolves correctly. The seeder intentionally selects the drug class as the native
    parent, rather than the immediate raw ARO parent.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: adopted
  kind: primary_source
  reference: PMID:37327570; DOI:10.1021/acs.jnatprod.3c00052
  locator: 428-PMC10391614.xml introduction, selected material-identification/results
    and Antibacterial Assays section
  accessed_at: '2026-10-21T15:49:43.170958Z'
  support: supports
  summary: The original introduction gives the same family naming/history sentence
    and cites the 2012 A/B study. Its experimental glycosides derive from C/D/J aglycones
    and are distinct from G/H/I. Its described antibacterial assay uses spotted material
    and clearance zones; those results are not silently transformed into G/H/I MICs
    or direct FabF inhibition.
  snapshot_sha256: f6b5f4419134d9a03d48c4d1ac156ce39bd8bf09434d9f18a6da504ec28e23a2
- evidence_id: fabf
  kind: primary_source
  reference: PMID:22224500; DOI:10.1021/ja207662w
  locator: 428-PMC3335777.html/.txt selected isolation, FASII assays, FabT/FabF experiments
    and docking methods/results;426-2012-nihms354784f6.jpg Figure6b visually inspected;426-fetch3-results.json
  accessed_at: '2026-10-21T15:50:36.813741Z'
  support: context_only
  summary: The original studies A and B. Both inhibit S. aureus FASII extract elongation.
    The resolved ACP gel and Figure 6a growth plate are A-specific. Figure 6b reports
    FabF-overexpression/WT MIC ratios of 2.5 for A and 2.0 for B, with FabH/WT ratios
    of 1 for both. FabT mutants and docking support distinct mechanistic steps, with
    docking remaining predictive. These experiments explain the family history but
    were not conducted on the present G/H/I congeners.
  snapshot_sha256: 2f8c8c12dbb28d3f9a66043a4cb1d48cc62d84bb0cf2ca1b8f4f4eb52acbb9ad
- evidence_id: discovery
  kind: primary_source
  reference: PMID:32519857; DOI:10.1021/acs.jnatprod.0c00161
  locator: 428-core-32519857.json complete original abstract; compound 3 mapping
  accessed_at: '2026-10-21T15:50:11.856687Z'
  support: supports
  summary: The discovery paper identifies fasamycins G–K as compounds 1–5 from Streptomyces
    sp. KIB-1414, including I as compound 3. Its abstract reports antibacterial testing
    across the isolated panel. The whole-panel MIC range does not establish an individual
    I/strain value; the main assay table and exact configurational argument were not
    retrieved.
  snapshot_sha256: 35bb96428628985d411d72b8615f4d96d0a77c25d50beaa4abe635e79802fb79
- evidence_id: spectra
  kind: primary_source
  reference: DOI:10.1021/acs.jnatprod.0c00161.s001
  locator: '428-2020-si.pdf pp.S16/S19: compound 3 drawings, proton/carbon NMR and
    HRESIMS;430-si-p16.png;430-si-p19.png'
  accessed_at: '2026-10-21T15:50:36.814181Z'
  support: supports
  summary: The original compound 3 spectral pages were visually inspected. The depicted
    substitution pattern agrees with the native, including one chlorine, two methoxy
    groups and four phenolic hydroxyls. HRESIMS reports [M−H]− m/z 519.1213, consistent
    with the neutral formula; the detected ion does not change record charge. The
    drawings use a bold hanging-ring depiction. Its exact axial meaning was not independently
    translated into a machine-readable stereodescriptor; full de novo NMR elucidation
    is not claimed.
  snapshot_sha256: 541af1eb06e40a6048ad327ca0c61a7eae45200a93c2541e98ee7a6a444c6d9b
- evidence_id: revision
  kind: primary_source
  reference: PMID:41988676; DOI:10.1021/acs.jnatprod.6c00145
  locator: 428-PMC13532170.xml selected structural-revision/axial-chirality Results;428-2026-original.pdf
    available for reinspection
  accessed_at: '2026-10-21T15:52:36.412551Z'
  support: context_only
  summary: The 2026 original revises specified S. formicae congeners, including C/E/L/N/Q
    and a proposed D reassignment. It does not report a G/H/I-specific regiochemical
    correction or crystal determination. Measured congeners support Sa axial chirality,
    and the authors extend a family hypothesis. Neither a methoxy-position change
    nor a racemic-mixture interpretation is imposed on this native from those adjacent
    results.
  snapshot_sha256: 55796020973e571658d3a02c0080a44cff02e2bd6113dbfe0c942357eb04354d
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/precise1k/b1095; s_aureus/staph_precise108/USA300HOU_RS04880
  locator: 428-adapter-datasets.json;428-adapter-fabF-ecoli.txt;428-adapter-fabF-saureus.txt
  accessed_at: '2026-10-21T15:55:36Z'
  support: context_only
  summary: Structured lookup preceded open protein literature. Both datasets contain
    a FabF gene entry and neither search returns an iModulon hit. This verifies gene-label
    context only, not fasamycin binding, susceptibility or the exact target relation
    for this congener.
  snapshot_sha256: 9208915c33e73f36e3e38af2ad6d5c8c27b46d44a93a7304e4c37b6ee1bcc34a
- evidence_id: owners
  kind: database
  reference: Actual ARO/PubChem maintained inputs and transforms
  locator: 430-owner-append.json;430-raw-rows.json;430-source-audit.json;seed_from_sources.py
    lines785–840
  accessed_at: '2026-10-21T15:55:36Z'
  support: supports
  summary: All 13 initial hashes were retained and three actual owner inputs added,
    giving 16 unchanged hashes. ARO owns definition/class/citation/xrefs; PubChem
    enrichment owns the structure. Generated native fields and all three histories
    reconcile. The original generic ChEBI capture is preserved in provenance while
    target ownership names the actual source. Sole adopted PMID coverage is explicit.
  snapshot_sha256: dbc829a5b74f0e5990adbb0a164a4393848cc49f3104543ce1447d050f1cef90
- evidence_id: validation
  kind: validation
  reference: Focused native and scientific consistency checks
  locator: 430-focused-results.json;430-strict.tsv;430-authority-chemistry.log;430-ledger.log
  accessed_at: '2026-10-21T15:55:36Z'
  support: supports
  summary: Schema, strict terms, native molecular consistency, authority graph comparison
    and exact source ledger all passed. The graph checks do not test absent axial
    encoding or provide exact-congener mechanism evidence.
  snapshot_sha256: b664613b4912108cf8998fd0611ec4c74a9e0df93c39920b3def92931d30ec3d
- evidence_id: access
  kind: search
  reference: Bounded public exact-congener research
  locator: 430-local-hits.txt includes ignored files;428-fetch.json through428-fetch8.json;428-2020-openalex.json;428-2020-semantic.json
  accessed_at: '2026-10-21T15:55:36Z'
  support: context_only
  summary: The 2020 main paper remained closed or returned 403; its public official
    supplement was retrieved through Figshare. The original 2012 EPMC XML request
    failed500, followed by a successful PMC HTML retrieval. The 2023 and 2026 originals
    were read from public XML. Search leads and inaccessible main-table details are
    not substituted with commercial summaries.
  snapshot_sha256: c45a8f3fd8d885fa0f00a21caa8c879229b90813cfc69ae30a4bc637cf054604
  search_scope: 430-local-hits.txt includes ignored files;428-fetch.json through428-fetch8.json;428-2020-openalex.json;428-2020-semantic.json
assessments:
- assessment_id: identity
  area: identity
  topic: Exact congener connectivity and formula
  outcome: supported
  summary: All authorities and the original compound 3 drawings agree on the reported
    I substitution pattern and formula.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - chemistry
  - spectra
  - discovery
- assessment_id: axial
  area: representation
  topic: Axial configuration and encoding
  outcome: unknown
  summary: Standard graph concordance does not encode or prove the natural axial state.
    Original configurational text and a validated axial representation remain follow-up;
    no mixture or opposite-isomer claim follows.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - chemistry
  - spectra
  - revision
- assessment_id: grounding
  area: grounding
  topic: ARO class and exact xrefs
  outcome: supported
  summary: All three native links resolve to the named congener; class-parent transformation
    matches the maintained seeder. MINTED status is preserved.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - aro
  - chemistry
  - owners
- assessment_id: definition
  area: evidence
  topic: Family naming and FabF context
  outcome: supported
  summary: The adopted source supports the historical family statement. A/B mechanism
    experiments remain bounded to A/B; no dedicated exact-congener target edge is
    asserted.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - record
  - adopted
  - fabf
- assessment_id: specific-mechanism
  area: evidence
  topic: Exact-congener FabF inhibition
  outcome: unknown
  summary: Independent FabF inhibition for I was not established; family similarity
    and gene presence are insufficient for a new direct-binding claim.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - fabf
  - adapter
  - adopted
- assessment_id: activity
  area: evidence
  topic: Antibacterial classification
  outcome: supported
  summary: The original discovery includes the exact congener in its antibacterial
    compound panel; no numerical strain-specific value or clinical efficacy is inferred.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - discovery
- assessment_id: quantitative
  area: quantity
  topic: Individual MIC and strain context
  outcome: unknown
  summary: The original main assay table was not independently retrieved; panel ranges
    and 2023 glycoside assays cannot supply an exact native MIC.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - discovery
  - adopted
  - access
- assessment_id: revision
  area: scope
  topic: Later congener structural revisions
  outcome: supported
  summary: The newer original was checked and its specific corrections were not generalized
    to unmeasured G/H/I structures.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - revision
- assessment_id: completeness
  area: completeness
  topic: Optional evidence enrichment
  outcome: supported
  summary: A compound-specific definition could cite the discovery and explain axial
    scope, but no demonstrated required native defect is established. Any quantitative/target
    enrichment needs exact material and experiment support.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - record
  - discovery
  - spectra
- assessment_id: ownership
  area: ownership
  topic: Inputs, source claims and history
  outcome: supported
  summary: Actual owners, all16 unchanged hashes and three chronological histories
    reconcile.
  target_ids:
  - antibioticmech:aro-4406f1da89
  evidence_ids:
  - owners
  - validation
findings: []
actions: []
limitations:
- The 2020 original discovery abstract and compound 3 spectral drawings/HRESIMS pages
  were inspected. Its main MIC table, strain-level method details and exact configurational
  argument were unavailable.
- The original 2012 experiments were inspected as A/B mechanism context. They do not
  establish direct FabF binding or inhibition for this exact congener.
- Standard native/authority encodings lack an explicit axial designation. The bold
  original drawing and later family stereochemistry discussion are recorded; no racemate,
  opposite axial isomer or experimentally determined G/H/I crystal is inferred.
- The 2026 regiochemical corrections concern specified other congeners. The full original
  spectral dataset was not reprocessed, and an adjacent correction is not automatically
  a correction to this record.
- The broad activity panel in the discovery abstract is not a per-organism numerical
  result. No susceptibility-breakpoint, clinical efficacy or producer-strain biosynthetic
  claim is added.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- The structured adapter was run before protein-specific open literature follow-up.
  No matching iModulon component was returned, so no component summary was applicable.
- Standalone chemistry used the batch 019 interpreter against batch 043; native checks
  and source ledger used batch 043.
- An optional future definition may distinguish the exact congener discovery from
  historical A/B FabF evidence and record the validated axial stereochemistry in a
  suitable supported representation.
- No native content, scientific status or immutable bundle was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:226614
- https://pubchem.ncbi.nlm.nih.gov/compound/156012442
- https://doi.org/10.1021/acs.jnatprod.0c00161
- https://doi.org/10.1021/acs.jnatprod.0c00161.s001
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10391614/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3335777/
- https://doi.org/10.1021/acs.jnatprod.6c00145
tags:
- record-review
- fasamycin-i
- polyketide
- exact-congener
```
