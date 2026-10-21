# Gepotidacin: coherent exact structure with outdated clinical status and mismatched citation scope

- Review: 20261021T173830Z-gepotidacin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:15:15Z
- Finished UTC: 2026-10-21T17:38:30Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact R-gepotidacin free-compound structure is corroborated by independent public graphs. The native experimental/phase-III description is outdated in light of official2025 US approvals and current product labeling, and the cited2016 in-vitro study does not support the2019 trial chronology. Original antibacterial and gyrase studies support eligibility and mechanism with explicit assay and formulation boundaries.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position500; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-b2e68d25c8 | data/antibiotics/antibacterial/gepotidacin.yaml | generated | gepotidacin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-b2e68d25c8 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-b2e68d25c8 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-b2e68d25c8 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-b2e68d25c8 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-b2e68d25c8 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-b2e68d25c8 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-b2e68d25c8 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-b2e68d25c8 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-b2e68d25c8 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-b2e68d25c8 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-b2e68d25c8 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-b2e68d25c8 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact R-gepotidacin parent and pharmaceutical forms

identity: supported. Targets: antibioticmech:aro-b2e68d25c8.

Both native encodings and six external encodings agree. Official product naming confirms R configuration while distinguishing mesylate dihydrate from the native free compound.

### Experimental status and clinical chronology

consistency: concern. Targets: antibioticmech:aro-b2e68d25c8.

The definition is outdated after the2025 US approvals, and its2016 citation cannot establish a2019 chronology. Update with date/jurisdiction-specific sources or remove time-sensitive development prose.

### Exact-compound antibacterial eligibility

evidence: supported. Targets: antibioticmech:aro-b2e68d25c8.

The adopted original broad-isolate study directly demonstrates in-vitro antibacterial activity. Its historical breakpoint and investigational language are retained as study context, not current status.

### TypeII topoisomerase description and optional target enrichment

evidence: supported. Targets: antibioticmech:aro-b2e68d25c8.

Primary biochemical and structural work establishes S.aureus gyrase inhibition/cleavage-complex interactions. Distinct constructs, reaction endpoints, DNA states and proposed cellular steps must remain separate when adding optional target or graph claims.

### Mint, fallback structure, adopted reference and history

provenance: supported. Targets: antibioticmech:aro-b2e68d25c8.

The one source concept and all three history entries are coherent with the maintained ARO/PubChem rows. No ChEBI replacement is justified by an unverified candidate; source-level correction is needed for the stale definition.

### Optional biological fields and access limits

completeness: unknown. Targets: antibioticmech:aro-b2e68d25c8.

Native target, resistance and numerical activity objects are absent rather than falsely populated. The inspected studies support bounded future enrichment; this review is not an exhaustive current clinical or resistance survey.

## Findings

### F1: Replace the outdated experimental/phaseIII status and its unsupported chronology citation

major / open / confirmed; issue key: gepotidacin-outdated-experimental-status-and-citation.

The native definition frames gepotidacin as experimentally used and in phaseIII since2019, citing PMID26729499. The cited2016 in-vitro study discusses phaseII development and cannot support the2019 chronology. FDA approved the branded medicine for uncomplicated UTI in March2025 and for restricted uncomplicated urogenital gonorrhea use in December2025. Current official labeling confirms these uses with age, weight and indication restrictions. Preserve the neutral compound structure and update or remove the stale clinical framing with appropriate dated evidence.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained gepotidacin definition and attach evidence to the claims it supports.

- Use durable compound/mechanism wording or explicitly dated US approval language with the actual indication restrictions. Do not imply global or unrestricted approval.
- Keep PMID26729499 for its in-vitro antibacterial evidence; use the official dated approval/label for clinical status and an appropriate trial source if retaining historical phaseIII chronology.
- Preserve the native R free-compound structure and distinguish product mesylate dihydrate. Regenerate through maintained sources and run schema, strict, reproduction and required QC.

### A2

If adding targets or mechanism chains, curate the original S.aureus biochemical and structural experiments at their actual scope.

- Separate full-length gyrase activity, core-fusion crystal contacts, nicked versus intact DNA, IC50/cleavage endpoints and proposed downstream cell-death steps.
- Do not infer topoisomeraseIV ortholog binding, clinical efficacy or exact commercial assay salt composition from this one gyrase study.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/gepotidacin.yaml; Entire native YAML and every chronological history event | supports | The SEEDED record denotes neutral C24H28N6O3 with full key PZFAZQUREQIODZ-LJQANCHMSA-N. Every asserted name, classification, chemical value, grounding, provenance and evidence field was read. No numerical activity observation, producer object or causal graph is asserted. |
| owners | 500-source-rows.json; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Complete matching maintained inventory rows and actual extraction/emission ownership | supports | The original thirteen captured inputs are preserved, with actual additional owners appended before assessment. The ARO compound row supplies the definition, class and adopted PMID. The exact PubChem fallback row supplies the structure and retrieval date. The ARO-derived mint reproduces and does not assert ChEBI identity. |
| chemistry | 050-root-authority-chemistry.json; Independent forward parsing of both native encodings and current public authority encodings | supports | Eight encodings from native SMILES/InChI, PubChem name resolution and exact CID25101874, and CHEMBL3317856 agree at the full key. The one tetrahedral centre is R. The native graph is the neutral free compound; it does not encode the marketed mesylate dihydrate. |
| gates | 500-focused-results.json; 500-chemistry.json; Actual focused internal chemistry, schema and strict outputs | supports | All focused checks exit 0; formula, charge, masses and full key are internally coherent. Deterministic success does not validate source prose or current regulatory status. |
| search | 500-local-hits.txt; 050-root-fetch1.json through 050-root-fetch5.json; Hidden- and ignored-inclusive local search and bounded public source retrievals | context_only | Local searches included ignored files. Current chemical authorities, each adopted compound citation and selected original activity/mechanism papers were inspected at the stated depths. Search-result totals are not claimed as fully read literature. Failed XML and blocked registry requests are access limits, not evidence of absence. |
| authority | ARO:3007092; ARO:3007164; PubChem:25101874; ChEMBL:CHEMBL3317856; Current complete ARO compound/class stanzas and public exact structure entries | supports | The triazaacenaphthylene class fits the graph. Current ARO repeats the stale experimental/phase-III description. PubChem and ChEMBL agree at full molecular identity; neither the ARO mint nor absent native ChEBI xref is itself a scientific error. No external ChEBI equivalence has been established. |
| adopted | PMID:26729499; DOI:10.1128/AAC.02820-15; https://pmc.ncbi.nlm.nih.gov/articles/PMC4776004/; Complete indexed abstract; original main Methods, Results narrative, opening S.aureus/MRSA Table1 rows and final Discussion; remaining table cells not comprehensively audited | supports | The2016 study tested4027 clinical isolates using CLSI broth microdilution and agar dilution for C.perfringens. The S.aureus collection had MIC50/90 of0.25/0.5 micrograms/mL, including MRSA; E.coli MIC90 was2, with higher values in some resistant subsets. Manufacturers supplied compounds, but the inspected text does not establish exact gepotidacin salt/hydrate batch composition. No gepotidacin susceptibility breakpoint was proposed at that time. The article discusses phaseII development, not phaseIII since2019, approval or direct structural binding experiments. |
| approval | https://www.fda.gov/news-events/press-announcements/fda-approves-two-oral-therapies-treat-gonorrhea; FDA announcement dated December12,2025, opening approval paragraphs and gepotidacin-specific trial paragraph | supports | FDA states that Blujepa/gepotidacin was approved on December11,2025 for uncomplicated urogenital gonorrhea in patients12years and older weighing at least45kg with limited or no alternatives, and was first approved in March2025 for urinary tract infections. These dated official approvals contradict an exclusively experimental/phaseIII framing. The adjacent zoliflodacin study is a different medicine and is not used as gepotidacin evidence. |
| label | https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=80b57cfe-7819-4d95-a57d-014af42f118d&amp;type=display; Current labeling revised February2026, highlights, full Indications1.1–1.3 and Description11 | supports | The label identifies US indications for uncomplicated UTI in female patients12years and older weighing at least40kg and uncomplicated urogenital gonorrhea in patients12years and older weighing at least45kg with limited or no alternatives. The latter approval has limited clinical safety data. Tablets contain R-gepotidacin mesylate dihydrate, formula C24H28N6O3.CH4O3S.2H2O; the750mg strength is active-compound equivalent. This supports current status and formulation distinction without changing the native neutral parent or implying unrestricted use. |
| mechanism | PMID:30757898; DOI:10.1021/acsinfecdis.8b00315; https://pmc.ncbi.nlm.nih.gov/articles/PMC6461504/; Original complete Methods, Results/Discussion and Conclusions; visual Figures1,3 and12; other captions, not all images or supplement | supports | The2019 study used full-length S.aureus GyrA/GyrB for biochemical assays and GyrB27-A56 core fusions for crystallography. Gepotidacin supplied by GSK in DMSO inhibited negative supercoiling at IC50 about0.047micromolar and positive-supercoil relaxation at about0.6micromolar under different reaction times. It stabilized single-stranded DNA breaks with long-lived ternary complexes; the mechanism proposed for blocking second-strand cleavage remains a model. Crystal complexes used a GyrA Y123F fusion with doubly nicked DNA at2.31angstrom and wild-type fusion with intact DNA at2.37angstrom. One compound spans DNA and the interface between GyrA subunits; crystallographic twofold disorder is not two simultaneously bound molecules. The drawn basic nitrogen is protonated, a binding-state depiction rather than evidence that the neutral native graph is incorrect. This study does not directly establish gepotidacin binding to every bacterial topoisomeraseIV ortholog. |
| figures | PMID:30757898 Figures1,3,12; Direct visual inspection of downloaded original figure images | supports | Figure1 depicts GSK2140944 with the stereochemical wedge and protonated basic nitrogen. Figure3 directly labels distinct supercoiling and relaxation IC50 values. Figure12 shows nicked-DNA Y123F, intact-DNA wild-type and superposed complexes; these constructs and DNA states must not be collapsed into an unqualified isolated-protein binding claim. |
| adapter | 475-imodulon-datasets.json; 050-root-adapter-results.json; 050-root-adapter-s_aureus-gyrA.txt; Actual covered-dataset catalog and successful staph_precise108 gyrA query | supports | The structured query resolves gyrA/USA300HOU_RS00030 and gyrB/USA300HOU_RS00025 through its broad matching, with zero module hits. The dataset strain is not asserted to be the original experimental enzyme source. These results are descriptive catalog context, not evidence for or against binding or susceptibility. |

## Limits And Additional Notes

- The2016 original main Methods and Results/Discussion narrative plus selected Table1 rows were read; not every comparator/subgroup table cell was audited. It does not establish the precise assay-batch salt/hydrate composition.
- The2019 original Methods/Results/Discussion/Conclusions and visual Figures1,3,12 were inspected. Other figure captions were read, but the separate supporting DOCX, all remaining raw images and deposited coordinates were not independently analyzed.
- Official FDA and DailyMed sources support dated US status and formulation. No worldwide approval, treatment recommendation or independent clinical-trial reanalysis is claimed.
- Current public molecular graphs corroborate the ARO/PubChem mint. No verified exact ChEBI equivalent was established; optional missing biological fields are not automatically defects.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T173830Z-gepotidacin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Gepotidacin: coherent exact structure with outdated clinical status and mismatched
  citation scope'
started_at: '2026-10-21T17:15:15Z'
finished_at: '2026-10-21T17:38:30Z'
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
summary: The exact R-gepotidacin free-compound structure is corroborated by independent
  public graphs. The native experimental/phase-III description is outdated in light
  of official2025 US approvals and current product labeling, and the cited2016 in-vitro
  study does not support the2019 trial chronology. Original antibacterial and gyrase
  studies support eligibility and mechanism with explicit assay and formulation boundaries.
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
  - path: data/antibiotics/antibacterial/gepotidacin.yaml
    sha256: 669d3ca1ed4257c69f2442636ef93b6afe1874204de044d99fdf357114acc40c
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
targets:
- target_id: antibioticmech:aro-b2e68d25c8
  path: data/antibiotics/antibacterial/gepotidacin.yaml
  label: gepotidacin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO compound, class, definition and cross-references
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Native field emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained grounding decisions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Exact PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained PubChem enrichment writer
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position500; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-b2e68d25c8
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-b2e68d25c8
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    500
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-b2e68d25c8
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/gepotidacin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-b2e68d25c8
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/gepotidacin.yaml --out /private/tmp/am-review-session/500-strict.tsv
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
  - antibioticmech:aro-b2e68d25c8
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
  - antibioticmech:aro-b2e68d25c8
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
  - antibioticmech:aro-b2e68d25c8
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
  - antibioticmech:aro-b2e68d25c8
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
  - antibioticmech:aro-b2e68d25c8
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
  - antibioticmech:aro-b2e68d25c8
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
  - antibioticmech:aro-b2e68d25c8
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
  - antibioticmech:aro-b2e68d25c8
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
  - antibioticmech:aro-b2e68d25c8
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/gepotidacin.yaml
  locator: Entire native YAML and every chronological history event
  accessed_at: '2026-10-21T17:26:15Z'
  support: supports
  summary: The SEEDED record denotes neutral C24H28N6O3 with full key PZFAZQUREQIODZ-LJQANCHMSA-N.
    Every asserted name, classification, chemical value, grounding, provenance and
    evidence field was read. No numerical activity observation, producer object or
    causal graph is asserted.
- evidence_id: owners
  kind: record_content
  reference: 500-source-rows.json; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Complete matching maintained inventory rows and actual extraction/emission
    ownership
  accessed_at: '2026-10-21T17:26:15Z'
  support: supports
  summary: The original thirteen captured inputs are preserved, with actual additional
    owners appended before assessment. The ARO compound row supplies the definition,
    class and adopted PMID. The exact PubChem fallback row supplies the structure
    and retrieval date. The ARO-derived mint reproduces and does not assert ChEBI
    identity.
  snapshot_sha256: 7daec346e84124247d98117e2484f9db64c66cbaeefbc412104d55bc2e2eb634
- evidence_id: chemistry
  kind: validation
  reference: 050-root-authority-chemistry.json
  locator: Independent forward parsing of both native encodings and current public
    authority encodings
  accessed_at: '2026-10-21T17:26:15Z'
  support: supports
  summary: Eight encodings from native SMILES/InChI, PubChem name resolution and exact
    CID25101874, and CHEMBL3317856 agree at the full key. The one tetrahedral centre
    is R. The native graph is the neutral free compound; it does not encode the marketed
    mesylate dihydrate.
  snapshot_sha256: 2627fe582a7974f745e9762382f402a6adc04160d704bcdb568883e6aa3ed7e1
- evidence_id: gates
  kind: validation
  reference: 500-focused-results.json; 500-chemistry.json
  locator: Actual focused internal chemistry, schema and strict outputs
  accessed_at: '2026-10-21T17:26:15Z'
  support: supports
  summary: All focused checks exit 0; formula, charge, masses and full key are internally
    coherent. Deterministic success does not validate source prose or current regulatory
    status.
  snapshot_sha256: 935bc787c00051a75b2d182d5654f5d75d0213bc4931ca5f2c901e3f95be3228
- evidence_id: search
  kind: search
  reference: 500-local-hits.txt; 050-root-fetch1.json through 050-root-fetch5.json
  locator: Hidden- and ignored-inclusive local search and bounded public source retrievals
  accessed_at: '2026-10-21T17:26:15Z'
  support: context_only
  summary: Local searches included ignored files. Current chemical authorities, each
    adopted compound citation and selected original activity/mechanism papers were
    inspected at the stated depths. Search-result totals are not claimed as fully
    read literature. Failed XML and blocked registry requests are access limits, not
    evidence of absence.
  search_scope: 2026-10-21; own050 checkout rg --no-ignore --hidden; adopted exact
    PMID and bounded Europe PMC TITLE_ABS:gepotidacin mechanism/gyrase/synthesis searches;
    current official authorities and selected PMC originals.
  snapshot_sha256: 47c5ce0a6cc87607cb630d689eb3beba48edb1761893f6beca447601ad627b59
- evidence_id: authority
  kind: authority
  reference: ARO:3007092; ARO:3007164; PubChem:25101874; ChEMBL:CHEMBL3317856
  locator: Current complete ARO compound/class stanzas and public exact structure
    entries
  accessed_at: '2026-10-21T17:26:15Z'
  support: supports
  summary: The triazaacenaphthylene class fits the graph. Current ARO repeats the
    stale experimental/phase-III description. PubChem and ChEMBL agree at full molecular
    identity; neither the ARO mint nor absent native ChEBI xref is itself a scientific
    error. No external ChEBI equivalence has been established.
  snapshot_sha256: c6b041136577328cafe1ac9578e1f99d6e889dffc53b9a78d07f9a2ff5e7f93c
- evidence_id: adopted
  kind: primary_source
  reference: PMID:26729499; DOI:10.1128/AAC.02820-15; https://pmc.ncbi.nlm.nih.gov/articles/PMC4776004/
  locator: Complete indexed abstract; original main Methods, Results narrative, opening
    S.aureus/MRSA Table1 rows and final Discussion; remaining table cells not comprehensively
    audited
  accessed_at: '2026-10-21T17:26:15Z'
  support: supports
  summary: The2016 study tested4027 clinical isolates using CLSI broth microdilution
    and agar dilution for C.perfringens. The S.aureus collection had MIC50/90 of0.25/0.5
    micrograms/mL, including MRSA; E.coli MIC90 was2, with higher values in some resistant
    subsets. Manufacturers supplied compounds, but the inspected text does not establish
    exact gepotidacin salt/hydrate batch composition. No gepotidacin susceptibility
    breakpoint was proposed at that time. The article discusses phaseII development,
    not phaseIII since2019, approval or direct structural binding experiments.
  snapshot_sha256: 86c41c1d41a147b3cac2dbd9e7cdc2518a11e91b5abab5dd8d46c2a99a9bafce
- evidence_id: approval
  kind: primary_source
  reference: https://www.fda.gov/news-events/press-announcements/fda-approves-two-oral-therapies-treat-gonorrhea
  locator: FDA announcement dated December12,2025, opening approval paragraphs and
    gepotidacin-specific trial paragraph
  accessed_at: '2026-10-21T17:26:15Z'
  support: supports
  summary: FDA states that Blujepa/gepotidacin was approved on December11,2025 for
    uncomplicated urogenital gonorrhea in patients12years and older weighing at least45kg
    with limited or no alternatives, and was first approved in March2025 for urinary
    tract infections. These dated official approvals contradict an exclusively experimental/phaseIII
    framing. The adjacent zoliflodacin study is a different medicine and is not used
    as gepotidacin evidence.
  snapshot_sha256: bd50b63917120687a8e62a5d6fc121f0909b5cf5017be8141a55c7221383d3f4
- evidence_id: label
  kind: primary_source
  reference: https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=80b57cfe-7819-4d95-a57d-014af42f118d&type=display
  locator: Current labeling revised February2026, highlights, full Indications1.1–1.3
    and Description11
  accessed_at: '2026-10-21T17:26:15Z'
  support: supports
  summary: The label identifies US indications for uncomplicated UTI in female patients12years
    and older weighing at least40kg and uncomplicated urogenital gonorrhea in patients12years
    and older weighing at least45kg with limited or no alternatives. The latter approval
    has limited clinical safety data. Tablets contain R-gepotidacin mesylate dihydrate,
    formula C24H28N6O3.CH4O3S.2H2O; the750mg strength is active-compound equivalent.
    This supports current status and formulation distinction without changing the
    native neutral parent or implying unrestricted use.
  snapshot_sha256: c32ba2bc51ecfc9331022661bfc97c1ec901373152ea5a892fbc2d220a379143
- evidence_id: mechanism
  kind: primary_source
  reference: PMID:30757898; DOI:10.1021/acsinfecdis.8b00315; https://pmc.ncbi.nlm.nih.gov/articles/PMC6461504/
  locator: Original complete Methods, Results/Discussion and Conclusions; visual Figures1,3
    and12; other captions, not all images or supplement
  accessed_at: '2026-10-21T17:26:15Z'
  support: supports
  summary: The2019 study used full-length S.aureus GyrA/GyrB for biochemical assays
    and GyrB27-A56 core fusions for crystallography. Gepotidacin supplied by GSK in
    DMSO inhibited negative supercoiling at IC50 about0.047micromolar and positive-supercoil
    relaxation at about0.6micromolar under different reaction times. It stabilized
    single-stranded DNA breaks with long-lived ternary complexes; the mechanism proposed
    for blocking second-strand cleavage remains a model. Crystal complexes used a
    GyrA Y123F fusion with doubly nicked DNA at2.31angstrom and wild-type fusion with
    intact DNA at2.37angstrom. One compound spans DNA and the interface between GyrA
    subunits; crystallographic twofold disorder is not two simultaneously bound molecules.
    The drawn basic nitrogen is protonated, a binding-state depiction rather than
    evidence that the neutral native graph is incorrect. This study does not directly
    establish gepotidacin binding to every bacterial topoisomeraseIV ortholog.
  snapshot_sha256: d5d86ba61a185af51357ffb8619c62e11a0b73cc71971c2191edc2f43de92dcd
- evidence_id: figures
  kind: primary_source
  reference: PMID:30757898 Figures1,3,12
  locator: Direct visual inspection of downloaded original figure images
  accessed_at: '2026-10-21T17:26:15Z'
  support: supports
  summary: Figure1 depicts GSK2140944 with the stereochemical wedge and protonated
    basic nitrogen. Figure3 directly labels distinct supercoiling and relaxation IC50
    values. Figure12 shows nicked-DNA Y123F, intact-DNA wild-type and superposed complexes;
    these constructs and DNA states must not be collapsed into an unqualified isolated-protein
    binding claim.
  snapshot_sha256: d0b6eba66b4b54420303b9fdd7f4c3cc7a6d983d000d65262be4b00acd05d54e
- evidence_id: adapter
  kind: database
  reference: 475-imodulon-datasets.json; 050-root-adapter-results.json; 050-root-adapter-s_aureus-gyrA.txt
  locator: Actual covered-dataset catalog and successful staph_precise108 gyrA query
  accessed_at: '2026-10-21T17:26:15Z'
  support: supports
  summary: The structured query resolves gyrA/USA300HOU_RS00030 and gyrB/USA300HOU_RS00025
    through its broad matching, with zero module hits. The dataset strain is not asserted
    to be the original experimental enzyme source. These results are descriptive catalog
    context, not evidence for or against binding or susceptibility.
  snapshot_sha256: 00ad02c9a6ad840fb00a725e3e6e2a1fb4560773516c0d3311fb722eaffb736f
assessments:
- assessment_id: identity
  area: identity
  topic: Exact R-gepotidacin parent and pharmaceutical forms
  outcome: supported
  summary: Both native encodings and six external encodings agree. Official product
    naming confirms R configuration while distinguishing mesylate dihydrate from the
    native free compound.
  target_ids:
  - antibioticmech:aro-b2e68d25c8
  evidence_ids:
  - native
  - chemistry
  - label
  - authority
- assessment_id: status
  area: consistency
  topic: Experimental status and clinical chronology
  outcome: concern
  summary: The definition is outdated after the2025 US approvals, and its2016 citation
    cannot establish a2019 chronology. Update with date/jurisdiction-specific sources
    or remove time-sensitive development prose.
  target_ids:
  - antibioticmech:aro-b2e68d25c8
  evidence_ids:
  - native
  - owners
  - approval
  - label
  - adopted
- assessment_id: activity
  area: evidence
  topic: Exact-compound antibacterial eligibility
  outcome: supported
  summary: The adopted original broad-isolate study directly demonstrates in-vitro
    antibacterial activity. Its historical breakpoint and investigational language
    are retained as study context, not current status.
  target_ids:
  - antibioticmech:aro-b2e68d25c8
  evidence_ids:
  - adopted
  - label
- assessment_id: mechanism
  area: evidence
  topic: TypeII topoisomerase description and optional target enrichment
  outcome: supported
  summary: Primary biochemical and structural work establishes S.aureus gyrase inhibition/cleavage-complex
    interactions. Distinct constructs, reaction endpoints, DNA states and proposed
    cellular steps must remain separate when adding optional target or graph claims.
  target_ids:
  - antibioticmech:aro-b2e68d25c8
  evidence_ids:
  - mechanism
  - figures
  - adapter
  - authority
- assessment_id: provenance
  area: provenance
  topic: Mint, fallback structure, adopted reference and history
  outcome: supported
  summary: The one source concept and all three history entries are coherent with
    the maintained ARO/PubChem rows. No ChEBI replacement is justified by an unverified
    candidate; source-level correction is needed for the stale definition.
  target_ids:
  - antibioticmech:aro-b2e68d25c8
  evidence_ids:
  - native
  - owners
  - gates
  - authority
- assessment_id: completeness
  area: completeness
  topic: Optional biological fields and access limits
  outcome: unknown
  summary: Native target, resistance and numerical activity objects are absent rather
    than falsely populated. The inspected studies support bounded future enrichment;
    this review is not an exhaustive current clinical or resistance survey.
  target_ids:
  - antibioticmech:aro-b2e68d25c8
  evidence_ids:
  - native
  - adopted
  - mechanism
  - search
findings:
- finding_id: F1
  issue_key: gepotidacin-outdated-experimental-status-and-citation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Replace the outdated experimental/phaseIII status and its unsupported chronology
    citation
  description: The native definition frames gepotidacin as experimentally used and
    in phaseIII since2019, citing PMID26729499. The cited2016 in-vitro study discusses
    phaseII development and cannot support the2019 chronology. FDA approved the branded
    medicine for uncomplicated UTI in March2025 and for restricted uncomplicated urogenital
    gonorrhea use in December2025. Current official labeling confirms these uses with
    age, weight and indication restrictions. Preserve the neutral compound structure
    and update or remove the stale clinical framing with appropriate dated evidence.
  target_ids:
  - antibioticmech:aro-b2e68d25c8
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - native
  - owners
  - adopted
  - approval
  - label
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted gepotidacin definition and PMID
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO definition/reference extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Definition selection and source regeneration
  rule_id: Scientific claim-level evidence and current clinical-status accuracy
  native_severity: major
  normalization_reason: The error changes the stated clinical-development/authorization
    status and cites a paper that cannot support the chronology, while exact molecular
    identity remains intact.
actions:
- action_id: A1
  description: Correct the maintained gepotidacin definition and attach evidence to
    the claims it supports.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-b2e68d25c8
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted gepotidacin definition and PMID
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO definition/reference extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Definition selection and source regeneration
  acceptance_checks:
  - Use durable compound/mechanism wording or explicitly dated US approval language
    with the actual indication restrictions. Do not imply global or unrestricted approval.
  - Keep PMID26729499 for its in-vitro antibacterial evidence; use the official dated
    approval/label for clinical status and an appropriate trial source if retaining
    historical phaseIII chronology.
  - Preserve the native R free-compound structure and distinguish product mesylate
    dihydrate. Regenerate through maintained sources and run schema, strict, reproduction
    and required QC.
- action_id: A2
  description: If adding targets or mechanism chains, curate the original S.aureus
    biochemical and structural experiments at their actual scope.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-b2e68d25c8
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/gepotidacin.yaml
    role: Optional evidence-backed native target and causal-graph enrichment
  acceptance_checks:
  - Separate full-length gyrase activity, core-fusion crystal contacts, nicked versus
    intact DNA, IC50/cleavage endpoints and proposed downstream cell-death steps.
  - Do not infer topoisomeraseIV ortholog binding, clinical efficacy or exact commercial
    assay salt composition from this one gyrase study.
limitations:
- The2016 original main Methods and Results/Discussion narrative plus selected Table1
  rows were read; not every comparator/subgroup table cell was audited. It does not
  establish the precise assay-batch salt/hydrate composition.
- The2019 original Methods/Results/Discussion/Conclusions and visual Figures1,3,12
  were inspected. Other figure captions were read, but the separate supporting DOCX,
  all remaining raw images and deposited coordinates were not independently analyzed.
- Official FDA and DailyMed sources support dated US status and formulation. No worldwide
  approval, treatment recommendation or independent clinical-trial reanalysis is claimed.
- Current public molecular graphs corroborate the ARO/PubChem mint. No verified exact
  ChEBI equivalent was established; optional missing biological fields are not automatically
  defects.
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
