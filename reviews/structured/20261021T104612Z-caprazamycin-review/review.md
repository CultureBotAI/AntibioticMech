# Review of caprazamycin

- Review: 20261021T104612Z-caprazamycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:32:38Z
- Finished UTC: 2026-10-21T10:46:12Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native graph reproduces its adopted and current public structure, and the cited paper explicitly depicts caprazamycin B. Original B isolation and activity support the antibacterial filing. Clarifying B in the name or definition would help distinguish congeners. A separate PubChem B entry has conflicting stereochemistry, so it is not an automatic replacement. The biosynthesis paper does not itself establish direct MraY binding; a separate primary B study supplies bounded target evidence. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire MINTED/SEEDED record and three history events; ARO term and parent, adopted PubChem graph, current public mappings, native cited2023 main text and Fig 1, original2003 full paper, original 2005 abstract and2013 mechanism Methods/Results.

Selection: Queue index194; root initial13 input hashes preserved, adopted ARO and PubChem maintained tables appended before inspection;15 repository inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-cd72e61879 | data/antibiotics/antibacterial/caprazamycin.yaml | generated | caprazamycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema check | passed | True | antibioticmech:aro-cd72e61879 | Exit0 in batch020 environment. |
| Documented strict check | passed | True | antibioticmech:aro-cd72e61879 | Exit0; zeroERRORrows in batch020 environment. |
| Supplemental structure consistency | passed | False | antibioticmech:aro-cd72e61879 | Exit0 in existing019RDKit environment against020 files. The name-query discrepancy is reported, not treated as a matching identifier. |
| Structured source catalog | passed | False | antibioticmech:aro-cd72e61879 | Catalog inspected before protein follow-up. |
| Structured MraY context | passed | False | antibioticmech:aro-cd72e61879 | One gene hit, no iModulon hit; contextual only. |
| Structured experimental-organism context | passed | False | antibioticmech:aro-cd72e61879 | One B. subtilis gene hit, no iModulon hit; contextual only. |
| Authoritative full QC | failed | True | antibioticmech:aro-cd72e61879 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-cd72e61879 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-cd72e61879 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-cd72e61879 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-cd72e61879 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-cd72e61879 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-cd72e61879 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-cd72e61879 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-cd72e61879 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Stored exact graph

identity: supported. Targets: antibioticmech:aro-cd72e61879.

Adopted and current public mappings agree internally with the native graph.

### Caprazamycin B scope and independent stereo confirmation

identity: unknown. Targets: antibioticmech:aro-cd72e61879.

Native cited Fig 1 and original isolation identify B topology, while generic wording and discordant named-B database stereochemistry warrant explicit clarification and primary stereo adjudication. No wrong native stereocenter is proven.

### Antibacterial filing and nucleoside class

grounding: supported. Targets: antibioticmech:aro-cd72e61879.

Exact B primary activity and uridine-based chemistry support the filing and parent.

### Optional mechanism enrichment

completeness: supported. Targets: antibioticmech:aro-cd72e61879.

Separate primary B evidence supports MraY inhibition in B. subtilis; this is optional enrichment in the present SEEDED record. Biosynthesis and CPZEN45 mechanisms remain distinct.

### Source and lead scope

provenance: supported. Targets: antibioticmech:aro-cd72e61879.

Native PMID and two parent leads resolved at stated depths; three history events and maintained owners checked.

### Focused checks

schema: supported. Targets: antibioticmech:aro-cd72e61879.

Schema/strict/supplemental chemistry pass.

## Findings

### F1: Make the supported B-congener scope explicit

informational / open / confirmed; issue key: aro-3007479-caprazamycin-b-scope-clarification.

The native source uses a generic name in prose but explicitly labels compound2 caprazamycin B in Fig 1. The stored branched lipid matches original B topology. Naming B explicitly in a maintained definition or label would prevent future congener-wide transfer; this is a clarification opportunity, not proof that the current PubChem-backed structure is wrong or that the source must be excluded.

## Recommended Actions And Acceptance Checks

### A1

For future curation, make the exact B context explicit and adjudicate the independent stereochemical discrepancy before changing any graph.

- Compare all configured centers against the original 2005 absolute-structure report or reliable machine-readable primary data; do not substitute CID139586173 merely because its name contains B.
- If clarifying the name or definition, reconcile upstream ARO or the maintained source transform and regenerate; preserve provenance of the original source label.
- Any MraY enrichment must cite exact B experiments and the B. subtilis organism/assay scope. Do not transfer CPZEN45 WecA dominance, biosynthetic Cpz enzymes or congener-wide MIC values.
- Run focused schema/strict and required reference, history, source and full-corpus gates after any separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/caprazamycin.yaml; Entire YAML and three history events | supports | MINTED/SEEDED ARO record has one neutral fully specified structure, generic caprazamycin label and antibacterial filing. There is no native molecular target, MIC, resistance observation, causal graph or curated producer object. |
| chemistry | PubChem:11332272;CHEMBL4542478; 194-chemistry.py/.json;194-pubchem.json;194-chembl.json | supports | Native SMILES/InChI/fullkey IDKBSYZJTHLMLI-IUKJTPATSA-N, neutral C53H87N5O22, masses and 19 configured centers agree internally and with both current public structure mappings. This verifies representation consistency, not independent experimental reassignment of every stereocenter. |
| stereo-boundary | PubChem:139586173; 194-pubchem-b.json;194-chemistry.json | partial | Exact-name query caprazamycin B returns CID139586173/key IDKBSYZJTHLMLI-DANJERETSA-N. Connectivity matches11332272, but shared InChI numbering has t37 unspecified and t44 opposite the native graph. Database name equality is insufficient for an exact replacement; original absolute-structure evidence must adjudicate this discrepancy. |
| native-paper | PMID:36697788; DOI:10.1038/s42004-022-00703-6;194-primary2023.xml;main Introduction,Results,Methods;194-2023-fig1.png visually inspected | supports | Although prose shortens the name, Fig 1 explicitly labels compound2 caprazamycin B with its branched lipid. The producing strain is Streptomyces sp.MK730-62F2. Experiments establish biosynthetic enzyme functions and intermediate chemistry, including Cpz10 hydroxylation; they do not measure direct binding of mature B to MraY. Biosynthetic Cpz proteins must not become antimicrobial targets. |
| isolation-activity | PMID:12931868; DOI:10.7164/antibiotics.56.580;194-primary2003.pdf,all4pages;Fig1 visually inspected | supports | Purified caprazamycin B is isolated from Streptomyces sp.MK730-62F2. Fig 1 identifies the branched lipid topology; stereochemistry is deferred to later work. B MICs include3.13micrograms/mL for M. tuberculosis H37Rv and Kurono, with susceptible and multidrug-resistant clinical panels. These support antibacterial/antimycobacterial activity, not clinical efficacy or all-congener quantitative transfer. |
| absolute-lead | PMID:16060385; DOI:10.1038/ja.2005.41;194-extra-core.json complete abstract;publisher abstract | partial | Original 2005 structural study distinguishes caprazamycins and reports absolute structure determination of B using NMR, crystallography of degradation products and synthesis of the aminoribose moiety. Full experimental article was not obtained; its abstract supports the existence of an absolute assignment, not a full atom-by-atom validation here. |
| mechanism | PMID:23986448; DOI:10.1074/jbc.M113.492173;https://pmc.ncbi.nlm.nih.gov/articles/PMC3798496/;web full-text Methods,Results,Table3,Fig5 captions andDiscussion | supports | B. subtilis168 experiments support caprazamycin B inhibition of MraY: overexpression shifts MIC4 to&gt;128micrograms/mL; cell-lysate enzyme assay gives approximately50ng/mL IC50. TagO is also inhibited at approximately150ng/mL, so exclusive selectivity is not established. CPZEN45 WecA/TagO findings are derivative-specific and must not be assigned to B. These are inhibition/genetic data, not a mature-B co-crystal or direct binding-affinity measurement. |
| class-leads | ARO:3000034;PMID:3061990;PMID:18679046; 194-aro-stanzas.txt;194-core.json | context_only | ARO parent denotes nucleoside antibiotic, consistent with the graph and primary papers. Its1988 nucleoside-antibiotic review resolves at metadata only(no abstract) and predates caprazamycin. Its2008 PMID18679046 complete abstract concerns Ehrlich/pharmacology history; it does not independently establish caprazamycin identity or mechanism. These are upstream parent references, not native evidence assertions. |
| adapter | iModulonDB; 194-imodulondb-datasets.txt;194-imodulondb-mray.txt;194-imodulondb-bsub-mray.txt | context_only | Catalog and gene searches succeeded. e_coli/modulome/b0087 and b_subtilis/modulome/BSU_15190 identify mraY. Neither search returned an iModulon hit, so no component summary was applicable. Gene/module context does not prove drug inhibition and does not transfer E. coli evidence to B. subtilis or mycobacteria. |
| owners | data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv;scripts/extract_source_inventory.py;scripts/seed_from_sources.py; ARO3007479 and PubChem11332272 source rows;194-aro-cache-hash.json | supports | Native definition, classification, parent and graph reproduce adopted source rows and ARO cache.15 repository inputs and separately hashed externalARO cache remained unchanged. Ignored-inclusive exact identifier/name search over curation, conf and native corpus found this record and queue references, but no maintained exact-congener reconciliation. |
| validation | Focused native validation; 194-strict.tsv;194-chemistry.json | supports | Schema and strict checks exit 0. Supplemental chemistry uses019 interpreter against020 files because020 lacks RDKit; no tracked dependency or native file changed. |

## Limits And Additional Notes

- Full2005 absolute-structure article was not obtained: two J-STAGE paths failed500; the Nature .pdf route returned HTML and pdftotext failed. The complete abstract was inspected. No raw NMR or degradation-crystal coordinates were independently reinterpreted.
- Separate PubChem caprazamycin B CID139586173 differs at one specified stereocenter and leaves another undefined. This review does not adjudicate that database discrepancy or claim every native stereocenter is experimentally revalidated.
- The 2003 paper reports C53H86N5O22 in its negative-ion mass context, while the neutral native graph calculates C53H87N5O22. This source notation is preserved, not used to remove a hydrogen from the neutral molecule.
- The 2023 main article and Fig 1 were inspected; its supplementary raw spectra and all biosynthetic structures were not reanalyzed. Biosynthetic-intermediate chemistry is separate from antimicrobial mechanism.
- The 2013 full Methods/Results were read through the web tool. A local EuropePMCXML fetch failed500 and localPMC HTML returned a challenge; those failed local artifacts are not claimed as full-text snapshots. Exact quantitative values remain paper/assay scoped.
- The native PMID36697788 and parent PMIDs3061990/18679046 were resolved; the1988 parent review has no indexed abstract and was checked only at metadata level. The unrelated historical parent reference does not negate the independently supported nucleoside classification.
- 020 lacks RDKit; supplemental chemistry used019 interpreter with020 working directory. Focused validation and structured-source success do not establish full-corpus success or promote SEEDED status.
- No exhaustive clinical, congener or resistance survey was undertaken. Current evidence supports clarification and future exact-target enrichment, not clinical efficacy or an automatic family exclusion.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 15 repository input hashes and the separately captured external ARO cache hash remain unchanged; no native or saved-bundle edits.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T104612Z-caprazamycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of caprazamycin
started_at: '2026-10-21T10:32:38Z'
finished_at: '2026-10-21T10:46:12Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: Coherent stored structure and antibacterial role; caprazamycin B scope
  supported, independent stereochemical conflict unresolved
scientific_review: true
summary: The native graph reproduces its adopted and current public structure, and
  the cited paper explicitly depicts caprazamycin B. Original B isolation and activity
  support the antibacterial filing. Clarifying B in the name or definition would help
  distinguish congeners. A separate PubChem B entry has conflicting stereochemistry,
  so it is not an automatic replacement. The biosynthesis paper does not itself establish
  direct MraY binding; a separate primary B study supplies bounded target evidence.
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
  - path: data/antibiotics/antibacterial/caprazamycin.yaml
    sha256: f5a85233ab057fdcb0a71c31522bc8c8dbc8c3cc20226216f52836ada50a94e4
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
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
scope:
  description: Entire MINTED/SEEDED record and three history events; ARO term and
    parent, adopted PubChem graph, current public mappings, native cited2023 main
    text and Fig 1, original2003 full paper, original 2005 abstract and2013 mechanism
    Methods/Results.
  selection: Queue index194; root initial13 input hashes preserved, adopted ARO and
    PubChem maintained tables appended before inspection;15 repository inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-cd72e61879
targets:
- target_id: antibioticmech:aro-cd72e61879
  path: data/antibiotics/antibacterial/caprazamycin.yaml
  label: caprazamycin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity and PubChem graph owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted ARO identity and PubChem graph owner
checks:
- check_id: schema
  name: Documented schema check
  status: passed
  required: true
  summary: Exit0 in batch020 environment.
  target_ids:
  - antibioticmech:aro-cd72e61879
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/caprazamycin.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict check
  status: passed
  required: true
  summary: Exit0; zeroERRORrows in batch020 environment.
  target_ids:
  - antibioticmech:aro-cd72e61879
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/caprazamycin.yaml --out /private/tmp/am-review-session/194-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Supplemental structure consistency
  status: passed
  required: false
  summary: Exit0 in existing019RDKit environment against020 files. The name-query
    discrepancy is reported, not treated as a matching identifier.
  target_ids:
  - antibioticmech:aro-cd72e61879
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/194-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: adapter-catalog
  name: Structured source catalog
  status: passed
  required: false
  summary: Catalog inspected before protein follow-up.
  target_ids:
  - antibioticmech:aro-cd72e61879
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets > /private/tmp/am-review-session/194-imodulondb-datasets.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-ecoli
  name: Structured MraY context
  status: passed
  required: false
  summary: One gene hit, no iModulon hit; contextual only.
  target_ids:
  - antibioticmech:aro-cd72e61879
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset modulome --query mraY
    > /private/tmp/am-review-session/194-imodulondb-mray.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-bsub
  name: Structured experimental-organism context
  status: passed
  required: false
  summary: One B. subtilis gene hit, no iModulon hit; contextual only.
  target_ids:
  - antibioticmech:aro-cd72e61879
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism b_subtilis --dataset modulome --query
    mraY > /private/tmp/am-review-session/194-imodulondb-bsub-mray.txt
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
  - antibioticmech:aro-cd72e61879
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
  - antibioticmech:aro-cd72e61879
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
  - antibioticmech:aro-cd72e61879
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
  - antibioticmech:aro-cd72e61879
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
  - antibioticmech:aro-cd72e61879
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
  - antibioticmech:aro-cd72e61879
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
  - antibioticmech:aro-cd72e61879
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
  - antibioticmech:aro-cd72e61879
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
  - antibioticmech:aro-cd72e61879
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/caprazamycin.yaml
  locator: Entire YAML and three history events
  accessed_at: '2026-10-21T10:41:57Z'
  support: supports
  summary: MINTED/SEEDED ARO record has one neutral fully specified structure, generic
    caprazamycin label and antibacterial filing. There is no native molecular target,
    MIC, resistance observation, causal graph or curated producer object.
- evidence_id: chemistry
  kind: validation
  reference: PubChem:11332272;CHEMBL4542478
  locator: 194-chemistry.py/.json;194-pubchem.json;194-chembl.json
  accessed_at: '2026-10-21T10:41:57Z'
  support: supports
  summary: Native SMILES/InChI/fullkey IDKBSYZJTHLMLI-IUKJTPATSA-N, neutral C53H87N5O22,
    masses and 19 configured centers agree internally and with both current public
    structure mappings. This verifies representation consistency, not independent
    experimental reassignment of every stereocenter.
  snapshot_sha256: aa9a1dd6147c4d84f5c4fa4e17fa737848b6bf5693311c407b9d09771af4edb3
- evidence_id: stereo-boundary
  kind: database
  reference: PubChem:139586173
  locator: 194-pubchem-b.json;194-chemistry.json
  accessed_at: '2026-10-21T10:41:57Z'
  support: partial
  summary: Exact-name query caprazamycin B returns CID139586173/key IDKBSYZJTHLMLI-DANJERETSA-N.
    Connectivity matches11332272, but shared InChI numbering has t37 unspecified and
    t44 opposite the native graph. Database name equality is insufficient for an exact
    replacement; original absolute-structure evidence must adjudicate this discrepancy.
  snapshot_sha256: a8a3f34825e515813ffc14d21813762b00782bbe30f53c584d47338459622fa7
- evidence_id: native-paper
  kind: primary_source
  reference: PMID:36697788
  locator: DOI:10.1038/s42004-022-00703-6;194-primary2023.xml;main Introduction,Results,Methods;194-2023-fig1.png
    visually inspected
  accessed_at: '2026-10-21T10:41:57Z'
  support: supports
  summary: Although prose shortens the name, Fig 1 explicitly labels compound2 caprazamycin
    B with its branched lipid. The producing strain is Streptomyces sp.MK730-62F2.
    Experiments establish biosynthetic enzyme functions and intermediate chemistry,
    including Cpz10 hydroxylation; they do not measure direct binding of mature B
    to MraY. Biosynthetic Cpz proteins must not become antimicrobial targets.
  snapshot_sha256: c98a64cc95bae36499598a1c9421ac236c6ef0e41f39fd8881cf9aedd8fa632c
- evidence_id: isolation-activity
  kind: primary_source
  reference: PMID:12931868
  locator: DOI:10.7164/antibiotics.56.580;194-primary2003.pdf,all4pages;Fig1 visually
    inspected
  accessed_at: '2026-10-21T10:41:57Z'
  support: supports
  summary: Purified caprazamycin B is isolated from Streptomyces sp.MK730-62F2. Fig
    1 identifies the branched lipid topology; stereochemistry is deferred to later
    work. B MICs include3.13micrograms/mL for M. tuberculosis H37Rv and Kurono, with
    susceptible and multidrug-resistant clinical panels. These support antibacterial/antimycobacterial
    activity, not clinical efficacy or all-congener quantitative transfer.
  snapshot_sha256: 102f9831e1b25fa48c7a091ffa884d443f63aca3f16df911de6a4d243de776d0
- evidence_id: absolute-lead
  kind: primary_source
  reference: PMID:16060385
  locator: DOI:10.1038/ja.2005.41;194-extra-core.json complete abstract;publisher
    abstract
  accessed_at: '2026-10-21T10:41:57Z'
  support: partial
  summary: Original 2005 structural study distinguishes caprazamycins and reports
    absolute structure determination of B using NMR, crystallography of degradation
    products and synthesis of the aminoribose moiety. Full experimental article was
    not obtained; its abstract supports the existence of an absolute assignment, not
    a full atom-by-atom validation here.
  snapshot_sha256: 4df3d995320b3dc8b58cd0d6852c503d65571c01e7320c3ed8d88a9774f4fad4
- evidence_id: mechanism
  kind: primary_source
  reference: PMID:23986448
  locator: DOI:10.1074/jbc.M113.492173;https://pmc.ncbi.nlm.nih.gov/articles/PMC3798496/;web
    full-text Methods,Results,Table3,Fig5 captions andDiscussion
  accessed_at: '2026-10-21T10:41:57Z'
  support: supports
  summary: 'B. subtilis168 experiments support caprazamycin B inhibition of MraY:
    overexpression shifts MIC4 to>128micrograms/mL; cell-lysate enzyme assay gives
    approximately50ng/mL IC50. TagO is also inhibited at approximately150ng/mL, so
    exclusive selectivity is not established. CPZEN45 WecA/TagO findings are derivative-specific
    and must not be assigned to B. These are inhibition/genetic data, not a mature-B
    co-crystal or direct binding-affinity measurement.'
- evidence_id: class-leads
  kind: database
  reference: ARO:3000034;PMID:3061990;PMID:18679046
  locator: 194-aro-stanzas.txt;194-core.json
  accessed_at: '2026-10-21T10:41:57Z'
  support: context_only
  summary: ARO parent denotes nucleoside antibiotic, consistent with the graph and
    primary papers. Its1988 nucleoside-antibiotic review resolves at metadata only(no
    abstract) and predates caprazamycin. Its2008 PMID18679046 complete abstract concerns
    Ehrlich/pharmacology history; it does not independently establish caprazamycin
    identity or mechanism. These are upstream parent references, not native evidence
    assertions.
  snapshot_sha256: 2e6093f8e4de4cb2cb54ab85fe416a474bbea914a6818492ece4cc5b53dbe756
- evidence_id: adapter
  kind: database
  reference: iModulonDB
  locator: 194-imodulondb-datasets.txt;194-imodulondb-mray.txt;194-imodulondb-bsub-mray.txt
  accessed_at: '2026-10-21T10:41:57Z'
  support: context_only
  summary: Catalog and gene searches succeeded. e_coli/modulome/b0087 and b_subtilis/modulome/BSU_15190
    identify mraY. Neither search returned an iModulon hit, so no component summary
    was applicable. Gene/module context does not prove drug inhibition and does not
    transfer E. coli evidence to B. subtilis or mycobacteria.
  snapshot_sha256: e4aa84b518960b8f57976eda3951b23dfcfd9f6566017f85bbc12b8d3a2423aa
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv;scripts/extract_source_inventory.py;scripts/seed_from_sources.py
  locator: ARO3007479 and PubChem11332272 source rows;194-aro-cache-hash.json
  accessed_at: '2026-10-21T10:41:57Z'
  support: supports
  summary: Native definition, classification, parent and graph reproduce adopted source
    rows and ARO cache.15 repository inputs and separately hashed externalARO cache
    remained unchanged. Ignored-inclusive exact identifier/name search over curation,
    conf and native corpus found this record and queue references, but no maintained
    exact-congener reconciliation.
  search_scope: rg --no-ignore --hidden -n -i caprazamycin|11332272|3007479 curation
    conf data/antibiotics
- evidence_id: validation
  kind: validation
  reference: Focused native validation
  locator: 194-strict.tsv;194-chemistry.json
  accessed_at: '2026-10-21T10:41:57Z'
  support: supports
  summary: Schema and strict checks exit 0. Supplemental chemistry uses019 interpreter
    against020 files because020 lacks RDKit; no tracked dependency or native file
    changed.
assessments:
- assessment_id: representation
  area: identity
  topic: Stored exact graph
  outcome: supported
  summary: Adopted and current public mappings agree internally with the native graph.
  target_ids:
  - antibioticmech:aro-cd72e61879
  evidence_ids:
  - chemistry
  - owners
- assessment_id: congener
  area: identity
  topic: Caprazamycin B scope and independent stereo confirmation
  outcome: unknown
  summary: Native cited Fig 1 and original isolation identify B topology, while generic
    wording and discordant named-B database stereochemistry warrant explicit clarification
    and primary stereo adjudication. No wrong native stereocenter is proven.
  target_ids:
  - antibioticmech:aro-cd72e61879
  evidence_ids:
  - native-paper
  - isolation-activity
  - absolute-lead
  - stereo-boundary
- assessment_id: activity
  area: grounding
  topic: Antibacterial filing and nucleoside class
  outcome: supported
  summary: Exact B primary activity and uridine-based chemistry support the filing
    and parent.
  target_ids:
  - antibioticmech:aro-cd72e61879
  evidence_ids:
  - isolation-activity
  - mechanism
  - class-leads
- assessment_id: target
  area: completeness
  topic: Optional mechanism enrichment
  outcome: supported
  summary: Separate primary B evidence supports MraY inhibition in B. subtilis; this
    is optional enrichment in the present SEEDED record. Biosynthesis and CPZEN45
    mechanisms remain distinct.
  target_ids:
  - antibioticmech:aro-cd72e61879
  evidence_ids:
  - mechanism
  - native-paper
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Source and lead scope
  outcome: supported
  summary: Native PMID and two parent leads resolved at stated depths; three history
    events and maintained owners checked.
  target_ids:
  - antibioticmech:aro-cd72e61879
  evidence_ids:
  - record
  - class-leads
  - owners
- assessment_id: schema
  area: schema
  topic: Focused checks
  outcome: supported
  summary: Schema/strict/supplemental chemistry pass.
  target_ids:
  - antibioticmech:aro-cd72e61879
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: aro-3007479-caprazamycin-b-scope-clarification
  category: nomenclature
  severity: informational
  status: open
  certainty: confirmed
  title: Make the supported B-congener scope explicit
  description: The native source uses a generic name in prose but explicitly labels
    compound2 caprazamycin B in Fig 1. The stored branched lipid matches original
    B topology. Naming B explicitly in a maintained definition or label would prevent
    future congener-wide transfer; this is a clarification opportunity, not proof
    that the current PubChem-backed structure is wrong or that the source must be
    excluded.
  target_ids:
  - antibioticmech:aro-cd72e61879
  field_paths:
  - label
  - definition
  - chemical_structure
  evidence_ids:
  - native-paper
  - isolation-activity
  - chemistry
  - stereo-boundary
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reconcile ARO label and definition reproducibly
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted source identity
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerate source-owned fields
  rule_id: 'review-checklist: exact identity and source scope'
  native_severity: informational congener clarification with unresolved independent
    stereo comparison
  normalization_reason: The inspected native source itself depicts B and the adopted
    exact graph is coherent; a generic common label and a conflicting separate database
    entry do not alone establish a native identity defect.
actions:
- action_id: A1
  description: For future curation, make the exact B context explicit and adjudicate
    the independent stereochemical discrepancy before changing any graph.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-cd72e61879
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reconcile ARO label and definition reproducibly
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted source identity
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerate source-owned fields
  acceptance_checks:
  - Compare all configured centers against the original 2005 absolute-structure report
    or reliable machine-readable primary data; do not substitute CID139586173 merely
    because its name contains B.
  - If clarifying the name or definition, reconcile upstream ARO or the maintained
    source transform and regenerate; preserve provenance of the original source label.
  - Any MraY enrichment must cite exact B experiments and the B. subtilis organism/assay
    scope. Do not transfer CPZEN45 WecA dominance, biosynthetic Cpz enzymes or congener-wide
    MIC values.
  - Run focused schema/strict and required reference, history, source and full-corpus
    gates after any separately authorized curation.
limitations:
- 'Full2005 absolute-structure article was not obtained: two J-STAGE paths failed500;
  the Nature .pdf route returned HTML and pdftotext failed. The complete abstract
  was inspected. No raw NMR or degradation-crystal coordinates were independently
  reinterpreted.'
- Separate PubChem caprazamycin B CID139586173 differs at one specified stereocenter
  and leaves another undefined. This review does not adjudicate that database discrepancy
  or claim every native stereocenter is experimentally revalidated.
- The 2003 paper reports C53H86N5O22 in its negative-ion mass context, while the neutral
  native graph calculates C53H87N5O22. This source notation is preserved, not used
  to remove a hydrogen from the neutral molecule.
- The 2023 main article and Fig 1 were inspected; its supplementary raw spectra and
  all biosynthetic structures were not reanalyzed. Biosynthetic-intermediate chemistry
  is separate from antimicrobial mechanism.
- The 2013 full Methods/Results were read through the web tool. A local EuropePMCXML
  fetch failed500 and localPMC HTML returned a challenge; those failed local artifacts
  are not claimed as full-text snapshots. Exact quantitative values remain paper/assay
  scoped.
- The native PMID36697788 and parent PMIDs3061990/18679046 were resolved; the1988
  parent review has no indexed abstract and was checked only at metadata level. The
  unrelated historical parent reference does not negate the independently supported
  nucleoside classification.
- 020 lacks RDKit; supplemental chemistry used019 interpreter with020 working directory.
  Focused validation and structured-source success do not establish full-corpus success
  or promote SEEDED status.
- No exhaustive clinical, congener or resistance survey was undertaken. Current evidence
  supports clarification and future exact-target enrichment, not clinical efficacy
  or an automatic family exclusion.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 15 repository input hashes and the separately captured external ARO cache hash
  remain unchanged; no native or saved-bundle edits.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.7164/antibiotics.56.580
- https://doi.org/10.1038/s42004-022-00703-6
- https://doi.org/10.1074/jbc.M113.492173
tags:
- record-review
- caprazamycin
- congener-scope
```
