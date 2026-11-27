# Brasiliquinone B: exact congener identity and primary activity scope

- Review: 20261021T102746Z-brasiliquinone-b-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:59:29Z
- Finished UTC: 2026-10-21T10:27:46Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Native exact identity and bounded antibacterial/antitumour claims are supported; no confirmed corrective finding was established. One informational enrichment item remains. The adopted original paper was read in full, with structure and assay tables visually checked. Its assay-method discrepancy and congener-specific endpoints must be retained. The qualified MIBiG producer assertion is faithfully inherited; independent original supporting data identify the donor and heterologous host. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position164; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65517 | data/antibiotics/antibacterial/brasiliquinone-b.yaml | generated | brasiliquinone B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:65517 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:65517 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:65517 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:65517 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65517 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65517 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65517 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65517 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65517 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65517 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65517 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65517 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Qualified biosynthetic producer assertion

evidence: supported. Targets: CHEBI:65517.

The native MIBiG link accurately carries locus-level rather than per-compound evidence. Original fermentation independently supports N. brasiliensis production; newer original SI enables a donor/host-specific follow-up without silently upgrading the native evidence.

### Exact congener, molecular graph and synonym

identity: supported. Targets: CHEBI:65517.

Independent encodings and public molecular sources agree on the exact native congener and stereochemistry. Source and assay congeners remain distinct.

### Parents, activity roles and biological definition

grounding: supported. Targets: CHEBI:65517.

The chemical parents and broad biological roles are supported by the exact-compound original study. Gram-positive and P388/ADR claims are restricted to the tested in-vitro systems.

### Maintained source and hash stability

provenance: supported. Targets: CHEBI:65517.

The native source-owned claims reproduce from captured inputs; initial and supplemental owner hashes remain unchanged. No native record or maintained source was edited.

### Qualified primary enrichment

completeness: unknown. Targets: CHEBI:65517.

Primary activity and cultured-production details can be added optionally, after resolving the paper’s assay-method discrepancy. No direct antibacterial molecular target was demonstrated by the inspected studies.

### Focused native gates

schema: supported. Targets: CHEBI:65517.

Focused schema, strict validation and independent chemistry checks pass. These checks do not resolve scientific evidence quality by themselves.

## Findings

### F1: Preserve congener, cell type and unresolved assay-method scope in optional enrichment

informational / open / confirmed; issue key: brasiliquinone-b-qualified-primary-assay-enrichment.

The original paper supports the native broad activity claims and offers useful exact-congener assay values. Empty optional activity/target fields are not required-field defects. The contradictory broth-versus-agar wording must be explicitly reconciled or retained as a limitation before precise assay annotation.

## Recommended Actions And Acceptance Checks

### A1

Optionally attach exact-congener primary activity and producer evidence with preserved experimental scope.

- Cite the appropriate A/B/C column in original Table3; retain strain IDs, reported micrograms/mL and &gt;100 censoring. Resolve or explicitly document microbroth Methods versus agar table caption; do not invent incubation conditions.
- Keep 72h MTT tumour IC50 and P388/ADR resistance separate from bacterial MIC/resistance. Do not import D/E BCG values, XJ31 provenance or a direct protein target from family analogy.
- For optional natural production, use cultivated IFM0089 fermentation evidence and distinguish it from a mere organism occurrence. For B BGC enrichment, distinguish AUSMDU00024985 donor, S. coelicolor M1152 heterologous host and native MIBiG locus-inherited evidence; inspect main expression controls before promoting detailed causal assertions.
- Use validated writers, curation history and required gates for future additions; native SEEDED status is not promoted by a saved review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/brasiliquinone-b.yaml; Entire native record, exact source row, chemical parents and all curation events | supports | The SEEDED record encodes one neutral, stereospecified brasiliquinone B, an exact systematic synonym, two registry crosswalks, antibacterial/antineoplastic roles and source-owned chemical/biological definition. It also contains a MIBiG producer with QUESTIONABLE source quality, CLUSTER_INHERITED heterologous-expression evidence and an explicit warning that its legacy reference is not established per-compound evidence. |
| source | data/raw/chebi_antimicrobials.tsv; data/raw/chebi_role_names.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; 164-raw.json; initial captured source, role, configuration and generation owners | supports | The adopted row reproduces native identity, names, definition, roles and crosswalks. Its sole publication lead is PMID9066761. The source mint reproduces independently. Exact source/curator inventory searches included hidden and ignored files; no matching curator override was found in those maintained files. This is bounded local absence, not a claim about all evidence. |
| chemistry | Independent native molecular parsing and focused repository gates; 164-chemistry.json; 164-focused-results.json | supports | SMILES and Standard InChI independently reproduce the full stored key, one neutral component, formula and both mass values at native precision. The single potential tetrahedral centre is assigned S. Focused schema and strict validation pass. |
| identity | ChEBI:65517; PubChem CID:9884187; ChemSpider:8059861; 164-ols.json; 164-pubchem.json; 164-chemspider.html | supports | Current ChEBI and PubChem complete molecular fields agree with YXEPHAVILJDRHK-VIFPVBQESA-N. ChemSpider resolves to the correct congener, formula, systematic name and one of one defined stereocentres. ChemSpider was checked through displayed metadata/names rather than an independently parsed downloadable molecule. Reaxys is a source-attested crosswalk; the proprietary record was not queried. |
| grounding | https://www.ebi.ac.uk/chebi/CHEBI:65517; 164-parents.json and current source term | supports | Current direct parents resolve as p-quinones CHEBI:25830, polyphenol CHEBI:26195, carbopolycyclic compound CHEBI:35294. They fit the molecular substructures. Antibacterial and antineoplastic roles agree with the original in-vitro observations; no human clinical indication follows. |
| primary-identity | PMID:9066761; DOI:10.7164/antibiotics.50.18; 163-primaryI.pdf, all four pages; p18 Figure1, p20 Table2 and p21 Table4 visually inspected | supports | The original study separately isolates A, B and C from cultivated Nocardia brasiliensis IFM0089 and characterizes the purified products. Figure1 differentiates the ristosamine O-glycoside A, 8-hydroxy aglycone B and 8-methoxy congener C. The reported fermentation and extraction support production in this cultured strain, not merely detection in an environmental sample. The mass listed as466 for A in Table2 conflicts with its printed neutral formula; native465.502 is independently correct and must not be changed to match that rounded source value. |
| primary-activity | PMID:9066761; DOI:10.7164/antibiotics.50.18; 163-primaryI.pdf, Methods and p20 Table3, exact B column visually inspected | supports | Table3 reports MICs in micrograms/mL for B: S. aureus 209P:25; MRSA IFM62971:25; M. smegmatis ATCC607:0.78; M. luteus IFM2066:3.13. E. coli NIHJ JC-2, A. niger ATCC40606 and C. albicans ATCC90028 are each &gt;100. Preserve that censoring and exact panel. Methods describes microbroth dilution in BHI, but the table caption names BHI agar/Sabouraud agar. The paper does not resolve this medium/method contradiction or state a complete incubation protocol; do not invent those qualifiers. This supports bounded Gram-positive activity, not universal efficacy or a resistance mechanism. |
| tumour-scope | DOI:10.7164/antibiotics.50.18; Cell-culture Methods and p21 Table4 visually inspected | supports | Purified B has 72h MTT-assay IC50 values in micrograms/mL of L1210:3.3, P388:3.0 and P388/ADR:3.0. These are mammalian cell-line cytotoxicity endpoints. The drug-resistant P388/ADR cell line is not an antimicrobial-resistant bacterial strain, and this study does not establish a clinical cancer indication or an antibacterial molecular target. |
| structure1996 | DOI:10.1039/P19960001773; Original publisher abstract, https://pubs.rsc.org/en/content/articlelanding/1996/p1/p19960001773 | partial | The original structural-paper abstract identifies a ristosamine O-glycoside A, its aglycone B and the 8-O-methyl derivative C. Full text was not retrieved: publisher route returned403 and an indexed academic mirror returned404. Detailed spectral or absolute-sugar assignments are not claimed from the abstract alone. |
| synthetic-stereo | PMID:36042538; DOI:10.1021/acs.joc.2c01653; 163-trio-discovery.json, complete indexed abstract | partial | Asymmetric total synthesis of B and C confirms the natural S configuration by correlation with synthetic products. This supports the aglycone stereochemistry in B/C at abstract level. The full synthetic Methods/SI were not read, and the abstract is not independent proof of A sugar absolute stereochemistry. |
| other-congeners | PMID:32830291; DOI:10.1007/s00253-020-10842-2; 163-primary2020.xml; complete Materials and Methods, relevant congener-identification and activity Results | context_only | The XJ31 fermentation/BCG study isolates brasiliquinones D and E, compounds13/14. Their ~25 micromolar BCG activity is not an A/B/C measurement. XJ31, its deposited strain, and its assay endpoints must not be transferred to this record by family-name matching. The other siderophore structures and raw spectra were not independently audited. |
| search | CultureBotAI/AntibioticMech and official public primary/chemical sources; 164-local-hits.txt; 163-trio-discovery.json | context_only | Initial source capture preceded scientific judgment. Name/identifier searches included ignored and hidden files outside .git and .venv. The sole adopted publication was read in full; bounded family discovery supplied structural synthesis, biosynthetic and distinct-congener studies. Search results and database annotations are not treated as primary assay evidence. |
| mibig | https://mibig.secondarymetabolites.org/repository/BGC0002047.2/annotations.json; 164-mibig-v2-annotations.json; data/raw/mibig_producers.tsv; scripts/extract_mibig_producers.py | supports | Version2 remains active, questionable quality and unknown completeness, with N. brasiliensis NCBITaxon37326. Heterologous-expression evidence is attached to locus MT023106.1, not individually to compound evidence arrays, which are empty. B exactly matches native full key. A lacks the anomeric assignment and is correctly excluded from an exact A join. Native CLUSTER_INHERITED and legacy-reference warning faithfully reflect that source scope. |
| biosynthesis-primary | PMID:31697466; DOI:10.1021/acschembio.9b00763; DOI:10.1021/acschembio.9b00763.s001; Original complete abstract; publisher SI PDF164-acs-SI-0.pdf, Table1, TableS4 and figure captions | partial | The abstract establishes capture and heterologous expression of the brasiliquinone biosynthetic locus. SI Table1 identifies N. brasiliensis AUSMDU00024985 as donor and S. coelicolor M1152 carrying pTPS790 as the heterologous host; pTPS790 carries a55kb cloned region. TableS4 and spectrum captions specifically identify brasiliquinone B isolated in this study. The SI supports an exact B biosynthetic follow-up but does not replace an unread full main-text expression/control experiment. Predicted TDP-L-ristosamine enzymes are biosynthetic context, not antimicrobial drug targets. |
| adapter | iModulonDB structured source runner; 017-root-imodulondb-datasets-retry.txt; datasets command before web follow-up | context_only | The structured catalog was inspected before open-ended mechanism research. No Nocardia dataset is listed; the bounded catalog search returned no matching taxon. A Streptomyces dataset is not substituted for the native producer merely because it is an actinomycete or expression host. This is a source-coverage limit, not evidence that no transcriptome exists. |

## Limits And Additional Notes

- The1997 four-page primary paper was read in full and key structure/assay tables were visually checked. Original raw spectra were not reprocessed. The1996 structure and2022 asymmetric-synthesis reports remain abstract-only; A sugar absolute stereochemistry is corroborated by current chemical sources, not independently rederived here.
- Current ChemSpider names/formula/stereocentre count were inspected, but its downloadable molecular graph and proprietary Reaxys registry were not independently parsed.
- The2020 XJ31 Methods and relevant congener/assay Results were inspected to reject transfer from D/E. Its full siderophore structural work and supplements were not audited. No exhaustive target, clinical, resistance or transcriptomic review is claimed.
- Optional quantitative enrichment is limited by the1997 method/medium discrepancy and incompletely stated incubation conditions. No clinical efficacy or universal organism spectrum follows.
- The2019/2020 biosynthesis main article was not retrieved in full. Its original abstract and DOI-verified free SI were inspected; Table1 and TableS4 were read, with spectrum captions checked but raw spectral assignments not independently reconstructed. The MIBiG entry remains explicitly questionable and locus-inherited.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 15 captured repository input hashes were rechecked unchanged. Native records and source inventories were not edited.
- Initial public network retrieval needed a permitted retry. Failed requests are retained as access limitations rather than evidence absence.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T102746Z-brasiliquinone-b-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Brasiliquinone B: exact congener identity and primary activity scope'
started_at: '2026-10-21T09:59:29Z'
finished_at: '2026-10-21T10:27:46Z'
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
summary: Native exact identity and bounded antibacterial/antitumour claims are supported;
  no confirmed corrective finding was established. One informational enrichment item
  remains. The adopted original paper was read in full, with structure and assay tables
  visually checked. Its assay-method discrepancy and congener-specific endpoints must
  be retained. The qualified MIBiG producer assertion is faithfully inherited; independent
  original supporting data identify the donor and heterologous host. Scientific assessment
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
  - path: data/antibiotics/antibacterial/brasiliquinone-b.yaml
    sha256: d64eaaec990487964f500c6c6be4459002b639612014fdbbf52a4fb9741d1069
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
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
    role: context
  - path: scripts/extract_mibig_producers.py
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
    role: context
targets:
- target_id: CHEBI:65517
  path: data/antibiotics/antibacterial/brasiliquinone-b.yaml
  label: brasiliquinone B
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
  selection: Initially uncovered queue position164; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65517
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65517
  command: .venv/bin/python /private/tmp/am-review-session/focus014-root.py 164
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65517
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/brasiliquinone-b.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65517
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/brasiliquinone-b.yaml --out /private/tmp/am-review-session/164-strict.tsv
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
  - CHEBI:65517
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
  - CHEBI:65517
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
  - CHEBI:65517
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
  - CHEBI:65517
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
  - CHEBI:65517
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
  - CHEBI:65517
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
  - CHEBI:65517
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
  - CHEBI:65517
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
  - CHEBI:65517
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/brasiliquinone-b.yaml
  locator: Entire native record, exact source row, chemical parents and all curation
    events
  accessed_at: '2026-10-21T10:08:33Z'
  support: supports
  summary: The SEEDED record encodes one neutral, stereospecified brasiliquinone B,
    an exact systematic synonym, two registry crosswalks, antibacterial/antineoplastic
    roles and source-owned chemical/biological definition. It also contains a MIBiG
    producer with QUESTIONABLE source quality, CLUSTER_INHERITED heterologous-expression
    evidence and an explicit warning that its legacy reference is not established
    per-compound evidence.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/chebi_role_names.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: 164-raw.json; initial captured source, role, configuration and generation
    owners
  accessed_at: '2026-10-21T10:08:33Z'
  support: supports
  summary: The adopted row reproduces native identity, names, definition, roles and
    crosswalks. Its sole publication lead is PMID9066761. The source mint reproduces
    independently. Exact source/curator inventory searches included hidden and ignored
    files; no matching curator override was found in those maintained files. This
    is bounded local absence, not a claim about all evidence.
  snapshot_sha256: 24ede9dfcd5fa6ae9e35febd54922bf092445cde5352d79932c4d21c11d80355
- evidence_id: chemistry
  kind: validation
  reference: Independent native molecular parsing and focused repository gates
  locator: 164-chemistry.json; 164-focused-results.json
  accessed_at: '2026-10-21T10:08:33Z'
  support: supports
  summary: SMILES and Standard InChI independently reproduce the full stored key,
    one neutral component, formula and both mass values at native precision. The single
    potential tetrahedral centre is assigned S. Focused schema and strict validation
    pass.
  snapshot_sha256: af35e3c40c02a525ce56a8347fda037e79641b2d7d66a9d1c9fcd8c0aad26c6f
- evidence_id: identity
  kind: database
  reference: ChEBI:65517; PubChem CID:9884187; ChemSpider:8059861
  locator: 164-ols.json; 164-pubchem.json; 164-chemspider.html
  accessed_at: '2026-10-21T10:08:33Z'
  support: supports
  summary: Current ChEBI and PubChem complete molecular fields agree with YXEPHAVILJDRHK-VIFPVBQESA-N.
    ChemSpider resolves to the correct congener, formula, systematic name and one
    of one defined stereocentres. ChemSpider was checked through displayed metadata/names
    rather than an independently parsed downloadable molecule. Reaxys is a source-attested
    crosswalk; the proprietary record was not queried.
  snapshot_sha256: 27b426b4fe6c280f338fbe888966c470085f72074c88488787678040c297021c
- evidence_id: grounding
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:65517
  locator: 164-parents.json and current source term
  accessed_at: '2026-10-21T10:08:33Z'
  support: supports
  summary: Current direct parents resolve as p-quinones CHEBI:25830, polyphenol CHEBI:26195,
    carbopolycyclic compound CHEBI:35294. They fit the molecular substructures. Antibacterial
    and antineoplastic roles agree with the original in-vitro observations; no human
    clinical indication follows.
  snapshot_sha256: 392f67efbf6803c3354931e7bf5f9b5a9c4fb2097617c55c840cf7a44f9510e9
- evidence_id: primary-identity
  kind: primary_source
  reference: PMID:9066761; DOI:10.7164/antibiotics.50.18
  locator: 163-primaryI.pdf, all four pages; p18 Figure1, p20 Table2 and p21 Table4
    visually inspected
  accessed_at: '2026-10-21T10:08:33Z'
  support: supports
  summary: The original study separately isolates A, B and C from cultivated Nocardia
    brasiliensis IFM0089 and characterizes the purified products. Figure1 differentiates
    the ristosamine O-glycoside A, 8-hydroxy aglycone B and 8-methoxy congener C.
    The reported fermentation and extraction support production in this cultured strain,
    not merely detection in an environmental sample. The mass listed as466 for A in
    Table2 conflicts with its printed neutral formula; native465.502 is independently
    correct and must not be changed to match that rounded source value.
  snapshot_sha256: 6c253ea2df93b7dfbec2f82538fab22f808c520f2f464a2aee645a49c5243e22
- evidence_id: primary-activity
  kind: primary_source
  reference: PMID:9066761; DOI:10.7164/antibiotics.50.18
  locator: 163-primaryI.pdf, Methods and p20 Table3, exact B column visually inspected
  accessed_at: '2026-10-21T10:08:33Z'
  support: supports
  summary: 'Table3 reports MICs in micrograms/mL for B: S. aureus 209P:25; MRSA IFM62971:25;
    M. smegmatis ATCC607:0.78; M. luteus IFM2066:3.13. E. coli NIHJ JC-2, A. niger
    ATCC40606 and C. albicans ATCC90028 are each >100. Preserve that censoring and
    exact panel. Methods describes microbroth dilution in BHI, but the table caption
    names BHI agar/Sabouraud agar. The paper does not resolve this medium/method contradiction
    or state a complete incubation protocol; do not invent those qualifiers. This
    supports bounded Gram-positive activity, not universal efficacy or a resistance
    mechanism.'
  snapshot_sha256: 6c253ea2df93b7dfbec2f82538fab22f808c520f2f464a2aee645a49c5243e22
- evidence_id: tumour-scope
  kind: primary_source
  reference: DOI:10.7164/antibiotics.50.18
  locator: Cell-culture Methods and p21 Table4 visually inspected
  accessed_at: '2026-10-21T10:08:33Z'
  support: supports
  summary: Purified B has 72h MTT-assay IC50 values in micrograms/mL of L1210:3.3,
    P388:3.0 and P388/ADR:3.0. These are mammalian cell-line cytotoxicity endpoints.
    The drug-resistant P388/ADR cell line is not an antimicrobial-resistant bacterial
    strain, and this study does not establish a clinical cancer indication or an antibacterial
    molecular target.
  snapshot_sha256: 6c253ea2df93b7dfbec2f82538fab22f808c520f2f464a2aee645a49c5243e22
- evidence_id: structure1996
  kind: primary_source
  reference: DOI:10.1039/P19960001773
  locator: Original publisher abstract, https://pubs.rsc.org/en/content/articlelanding/1996/p1/p19960001773
  accessed_at: '2026-10-21T10:08:33Z'
  support: partial
  summary: 'The original structural-paper abstract identifies a ristosamine O-glycoside
    A, its aglycone B and the 8-O-methyl derivative C. Full text was not retrieved:
    publisher route returned403 and an indexed academic mirror returned404. Detailed
    spectral or absolute-sugar assignments are not claimed from the abstract alone.'
- evidence_id: synthetic-stereo
  kind: primary_source
  reference: PMID:36042538; DOI:10.1021/acs.joc.2c01653
  locator: 163-trio-discovery.json, complete indexed abstract
  accessed_at: '2026-10-21T10:08:33Z'
  support: partial
  summary: Asymmetric total synthesis of B and C confirms the natural S configuration
    by correlation with synthetic products. This supports the aglycone stereochemistry
    in B/C at abstract level. The full synthetic Methods/SI were not read, and the
    abstract is not independent proof of A sugar absolute stereochemistry.
  snapshot_sha256: a8ff8691cf40293e66f2a13ec1ce14108e07391dcb7fa6082ece487776fd448d
- evidence_id: other-congeners
  kind: primary_source
  reference: PMID:32830291; DOI:10.1007/s00253-020-10842-2
  locator: 163-primary2020.xml; complete Materials and Methods, relevant congener-identification
    and activity Results
  accessed_at: '2026-10-21T10:08:33Z'
  support: context_only
  summary: The XJ31 fermentation/BCG study isolates brasiliquinones D and E, compounds13/14.
    Their ~25 micromolar BCG activity is not an A/B/C measurement. XJ31, its deposited
    strain, and its assay endpoints must not be transferred to this record by family-name
    matching. The other siderophore structures and raw spectra were not independently
    audited.
  snapshot_sha256: a3dbaaffc8bddc856a9d72a906b621c35bcc190325d10f100e7d60749163c331
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech and official public primary/chemical sources
  locator: 164-local-hits.txt; 163-trio-discovery.json
  accessed_at: '2026-10-21T10:08:33Z'
  support: context_only
  summary: Initial source capture preceded scientific judgment. Name/identifier searches
    included ignored and hidden files outside .git and .venv. The sole adopted publication
    was read in full; bounded family discovery supplied structural synthesis, biosynthetic
    and distinct-congener studies. Search results and database annotations are not
    treated as primary assay evidence.
  search_scope: Isolated batch017 exact identifier/name search with rg --no-ignore
    --hidden excluding .git/.venv, maintained exact rows, current chemical authorities,
    capped EuropePMC family discovery and targeted original sources.
  snapshot_sha256: 5cdabc2326e3cca2abdb3c627af962edb0897cd12fc3aa8fa089b95ba62bfc88
- evidence_id: mibig
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002047.2/annotations.json
  locator: 164-mibig-v2-annotations.json; data/raw/mibig_producers.tsv; scripts/extract_mibig_producers.py
  accessed_at: '2026-10-21T10:08:33Z'
  support: supports
  summary: Version2 remains active, questionable quality and unknown completeness,
    with N. brasiliensis NCBITaxon37326. Heterologous-expression evidence is attached
    to locus MT023106.1, not individually to compound evidence arrays, which are empty.
    B exactly matches native full key. A lacks the anomeric assignment and is correctly
    excluded from an exact A join. Native CLUSTER_INHERITED and legacy-reference warning
    faithfully reflect that source scope.
  snapshot_sha256: 7c74080c14d13a41deb3f39c14b923e69a686e8c7d89643813c41315a55774bb
- evidence_id: biosynthesis-primary
  kind: primary_source
  reference: PMID:31697466; DOI:10.1021/acschembio.9b00763; DOI:10.1021/acschembio.9b00763.s001
  locator: Original complete abstract; publisher SI PDF164-acs-SI-0.pdf, Table1, TableS4
    and figure captions
  accessed_at: '2026-10-21T10:08:33Z'
  support: partial
  summary: The abstract establishes capture and heterologous expression of the brasiliquinone
    biosynthetic locus. SI Table1 identifies N. brasiliensis AUSMDU00024985 as donor
    and S. coelicolor M1152 carrying pTPS790 as the heterologous host; pTPS790 carries
    a55kb cloned region. TableS4 and spectrum captions specifically identify brasiliquinone
    B isolated in this study. The SI supports an exact B biosynthetic follow-up but
    does not replace an unread full main-text expression/control experiment. Predicted
    TDP-L-ristosamine enzymes are biosynthetic context, not antimicrobial drug targets.
  snapshot_sha256: 150c92594f53dfba53e55bd90b2eca9307f13e0d8a0bd5ccc63648cb944ba733
- evidence_id: adapter
  kind: database
  reference: iModulonDB structured source runner
  locator: 017-root-imodulondb-datasets-retry.txt; datasets command before web follow-up
  accessed_at: '2026-10-21T10:08:33Z'
  support: context_only
  summary: The structured catalog was inspected before open-ended mechanism research.
    No Nocardia dataset is listed; the bounded catalog search returned no matching
    taxon. A Streptomyces dataset is not substituted for the native producer merely
    because it is an actinomycete or expression host. This is a source-coverage limit,
    not evidence that no transcriptome exists.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
assessments:
- assessment_id: producer
  area: evidence
  topic: Qualified biosynthetic producer assertion
  outcome: supported
  summary: The native MIBiG link accurately carries locus-level rather than per-compound
    evidence. Original fermentation independently supports N. brasiliensis production;
    newer original SI enables a donor/host-specific follow-up without silently upgrading
    the native evidence.
  target_ids:
  - CHEBI:65517
  evidence_ids:
  - native
  - mibig
  - biosynthesis-primary
  - primary-identity
  - adapter
- assessment_id: identity
  area: identity
  topic: Exact congener, molecular graph and synonym
  outcome: supported
  summary: Independent encodings and public molecular sources agree on the exact native
    congener and stereochemistry. Source and assay congeners remain distinct.
  target_ids:
  - CHEBI:65517
  evidence_ids:
  - chemistry
  - identity
  - primary-identity
  - structure1996
  - synthetic-stereo
- assessment_id: classification
  area: grounding
  topic: Parents, activity roles and biological definition
  outcome: supported
  summary: The chemical parents and broad biological roles are supported by the exact-compound
    original study. Gram-positive and P388/ADR claims are restricted to the tested
    in-vitro systems.
  target_ids:
  - CHEBI:65517
  evidence_ids:
  - grounding
  - primary-activity
  - tumour-scope
  - native
- assessment_id: provenance
  area: provenance
  topic: Maintained source and hash stability
  outcome: supported
  summary: The native source-owned claims reproduce from captured inputs; initial
    and supplemental owner hashes remain unchanged. No native record or maintained
    source was edited.
  target_ids:
  - CHEBI:65517
  evidence_ids:
  - source
  - chemistry
- assessment_id: completeness
  area: completeness
  topic: Qualified primary enrichment
  outcome: unknown
  summary: Primary activity and cultured-production details can be added optionally,
    after resolving the paper’s assay-method discrepancy. No direct antibacterial
    molecular target was demonstrated by the inspected studies.
  target_ids:
  - CHEBI:65517
  evidence_ids:
  - primary-activity
  - primary-identity
  - tumour-scope
  - other-congeners
- assessment_id: schema
  area: schema
  topic: Focused native gates
  outcome: supported
  summary: Focused schema, strict validation and independent chemistry checks pass.
    These checks do not resolve scientific evidence quality by themselves.
  target_ids:
  - CHEBI:65517
  evidence_ids:
  - chemistry
findings:
- finding_id: F1
  issue_key: brasiliquinone-b-qualified-primary-assay-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Preserve congener, cell type and unresolved assay-method scope in optional
    enrichment
  description: The original paper supports the native broad activity claims and offers
    useful exact-congener assay values. Empty optional activity/target fields are
    not required-field defects. The contradictory broth-versus-agar wording must be
    explicitly reconciled or retained as a limitation before precise assay annotation.
  target_ids:
  - CHEBI:65517
  field_paths:
  - evidence
  - activity_spectrum
  - producer_organisms
  - discussions
  evidence_ids:
  - primary-identity
  - primary-activity
  - tumour-scope
  - other-congeners
  rule_id: 'native-review-checklist: Evidence Fidelity and optional completeness'
  native_severity: informational optional enrichment
  normalization_reason: No unsupported native quantitative result is populated; this
    item improves traceability rather than correcting a demonstrated missing requirement.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/brasiliquinone-b.yaml
    role: Curator-owned optional primary evidence and assay/producer annotations through
      validated writer/history workflow
actions:
- action_id: A1
  description: Optionally attach exact-congener primary activity and producer evidence
    with preserved experimental scope.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65517
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/brasiliquinone-b.yaml
    role: Curator-owned optional primary evidence and assay/producer annotations through
      validated writer/history workflow
  acceptance_checks:
  - Cite the appropriate A/B/C column in original Table3; retain strain IDs, reported
    micrograms/mL and >100 censoring. Resolve or explicitly document microbroth Methods
    versus agar table caption; do not invent incubation conditions.
  - Keep 72h MTT tumour IC50 and P388/ADR resistance separate from bacterial MIC/resistance.
    Do not import D/E BCG values, XJ31 provenance or a direct protein target from
    family analogy.
  - For optional natural production, use cultivated IFM0089 fermentation evidence
    and distinguish it from a mere organism occurrence. For B BGC enrichment, distinguish
    AUSMDU00024985 donor, S. coelicolor M1152 heterologous host and native MIBiG locus-inherited
    evidence; inspect main expression controls before promoting detailed causal assertions.
  - Use validated writers, curation history and required gates for future additions;
    native SEEDED status is not promoted by a saved review.
limitations:
- The1997 four-page primary paper was read in full and key structure/assay tables
  were visually checked. Original raw spectra were not reprocessed. The1996 structure
  and2022 asymmetric-synthesis reports remain abstract-only; A sugar absolute stereochemistry
  is corroborated by current chemical sources, not independently rederived here.
- Current ChemSpider names/formula/stereocentre count were inspected, but its downloadable
  molecular graph and proprietary Reaxys registry were not independently parsed.
- The2020 XJ31 Methods and relevant congener/assay Results were inspected to reject
  transfer from D/E. Its full siderophore structural work and supplements were not
  audited. No exhaustive target, clinical, resistance or transcriptomic review is
  claimed.
- Optional quantitative enrichment is limited by the1997 method/medium discrepancy
  and incompletely stated incubation conditions. No clinical efficacy or universal
  organism spectrum follows.
- The2019/2020 biosynthesis main article was not retrieved in full. Its original abstract
  and DOI-verified free SI were inspected; Table1 and TableS4 were read, with spectrum
  captions checked but raw spectral assignments not independently reconstructed. The
  MIBiG entry remains explicitly questionable and locus-inherited.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 15 captured repository input hashes were rechecked unchanged. Native records
  and source inventories were not edited.
- Initial public network retrieval needed a permitted retry. Failed requests are retained
  as access limitations rather than evidence absence.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:65517
- https://doi.org/10.7164/antibiotics.50.18
- https://doi.org/10.1039/P19960001773
- https://doi.org/10.1021/acs.joc.2c01653
- https://mibig.secondarymetabolites.org/repository/BGC0002047.2/index.html
- https://doi.org/10.1021/acschembio.9b00763.s001
```
