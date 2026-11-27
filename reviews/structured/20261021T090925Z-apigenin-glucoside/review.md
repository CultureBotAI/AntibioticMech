# Apigenin 7-O-beta-D-glucoside: supported neutral identity and activity; qualify external descriptors and mechanism scope

- Review: 20261021T090925Z-apigenin-glucoside
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:55:40Z
- Finished UTC: 2026-10-21T09:09:25Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Neutral stereospecific glucoside chemistry and the accepted ChEBI antibacterial role are supported. Original 2023 experiments provide antibacterial and biofilm-formation evidence for the named glucoside; a 2025 Origanum study adds independent phenotypic evidence. KNApSAcK has internally inconsistent descriptors, although its InChI matches native identity. Optional primary enrichment must preserve tested forms, assay endpoints, reporter organisms, and uncertainty in a separate 2025 Terminalia identity assignment. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole exact record; adopted ChEBI row and adjacent conjugate-base row as boundary context; all four adopted abstracts; official identity and cross-references; original 2023 and 2025 activity evidence.

Selection: Queue 101, CHEBI:16778, neutral apigenin 7-O-beta-D-glucoside.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:16778 | data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside.yaml | generated | apigenin 7-O-β-D-glucoside |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:16778 | Focused LinkML validation exited 0. |
| strict | passed | True | CHEBI:16778 | Focused strict scan exited 0 with no ERROR rows. |
| chemistry | passed | False | CHEBI:16778 | SMILES, InChI, formula, charge, masses, and mint identifier agree. |
| Authoritative full QC | failed | True | CHEBI:16778 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:16778 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:16778 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:16778 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:16778 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:16778 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:16778 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:16778 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:16778 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral exact structure and conjugate-base boundary

identity: supported. Targets: CHEBI:16778.

Native structure, definition, and accepted role match the official source and independent KEGG chemistry. The adjacent anion is distinct, not a duplicate.

### KNApSAcK internal descriptors

evidence: concern. Targets: CHEBI:16778.

The complete InChI agrees, while the displayed key and underspecified SMILES disagree. Qualify endpoint reliability without asserting an incorrect native entity.

### Antibacterial role and named-compound assays

evidence: supported. Targets: CHEBI:16778.

Purchased-glucoside activity in 2023 corroborates the source role; the 2025 Origanum study adds independent biofilm data. The adopted abstract alone does not provide an exact MIC, and the Terminalia identity requires qualification.

### Optional phenotype and mechanism enrichment

completeness: unknown. Targets: CHEBI:16778.

Measured EPS, hydrophobicity, biofilm, and reporter results are available. A direct target and causality across species remain unestablished. Missing an optional target is not an error.

### Producer, clinical, resistance, omics, and graphs

completeness: unknown. Targets: CHEBI:16778.

No unsupported native claims. Plant isolation and host pharmacokinetics do not establish a biosynthetic pathway, clinical approval, or antibacterial target. No omics dataset is inferred.

### Maintained source versus curator additions

ownership: supported. Targets: CHEBI:16778.

ChEBI source, extractor, seeder, and decision owners are captured. The actual native record path owns optional primary annotations.

### Focused gates and history

schema: supported. Targets: CHEBI:16778.

Focused checks pass; SEEDED status and history are consistent. No REVIEWED promotion is made.

## Findings

### F1: Qualify KNApSAcK descriptor inconsistency

minor / open / confirmed; issue key: apigenin-glucoside-knapsack-internal-descriptor-conflict.

KNApSAcK C00001017 has a complete InChI matching the native compound, but its displayed InChIKey and partially specified stereochemical SMILES disagree. The linked entry has an internal conflict. This does not establish that it denotes an opposite isomer or justify replacing native chemistry.

### F2: Add bounded primary activity and phenotypic evidence

informational / open / confirmed; issue key: apigenin-glucoside-qualified-primary-activity-enrichment.

The 2023 purchased-glucoside and 2025 Origanum studies support optional activity and biofilm annotation. Preserve MIC versus MBIC or biomass endpoints and the tested strains. The CV026 reporter does not establish E. coli or S. aureus quorum-sensing protein targets. The exact identity of the 2025 Terminalia isolate remains uncertain. Do not transfer assays without qualification to the separately recorded monoanion.

## Recommended Actions And Acceptance Checks

### A1

Document the exact KNApSAcK descriptor disagreement through maintained source ownership.

- Recheck the current KNApSAcK InChI, key, and SMILES independently; preserve the correct native full key and evidence from the complete InChI.
- Apply a documented source-specific qualification or curatorial decision if needed. Do not silently replace native chemistry or infer opposite stereochemistry from unspecified centres. Preserve provenance and verify that any future change survives reseeding.

### A2

Optionally curate qualified exact-compound activity and phenotypic mechanism evidence on the native record.

- Use PMID:37070126 with the exact supplier, material, strains, LB broth, 24-hour incubation, and Table 1 MIC/MBIC distinctions. Keep biofilm formation during co-incubation separate from eradication of preformed biofilm.
- Use PMID:40457736 compound 2 NMR identity and qualified phenotypes from Tables 2–3. Retain MIC &gt;100 µM and the negative efflux result. Do not transfer arbutin, extract, or fraction effects.
- Keep the CV026 violacein reporter separate from E. coli and S. aureus mechanisms. Do not add a LuxS or Agr direct target without binding or inhibition evidence. No gene-expression dataset is reported.
- Resolve the characterization and purity inconsistencies in PMID:40942120 before using its exact-compound MIC. Preserve the plant-source ambiguity in adopted PMID:19112896. Do not infer a biosynthetic pathway or clinical efficacy from isolation or pharmacokinetics.
- Preserve the neutral-compound versus CHEBI:77722 ion boundary and glucoside versus apigenin-aglycone distinction. Use write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside.yaml for an authorized future mutation. Run focused and shared gates without automatic REVIEWED promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside.yaml; Entire native YAML and four seed/reseed history events. | supports | SEEDED/EXACT neutral compound; nine synonyms, four structural parents, one antibacterial role, seven chemical cross-references, one Wikipedia document, and one ChEBI source concept. No primary evidence, mode, target, resistance, quantified activity, producer, clinical, graph, or dataset assertion is currently present. Optional blanks are not schema defects. |
| source | data/raw/chebi_antimicrobials.tsv; 101-raw.json, line 409; adjacent CHEBI:77722 row at line 1973; source configuration and extractor lines 176–335; seeder loading and building logic. | supports | The three-star, in-scope row reproduces native identity, synonyms, parents, and antibacterial role CHEBI:33282. No source mechanism roles are present. Four PMID leads are intentionally not automatically seeded as claim evidence. Configuration accepts only checked or OK role edges. All 13 captured input hashes are unchanged. The neighboring anion has a distinct charge, formula, and full key and remains a separate record. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:16778; 101-chebi.html/txt and KEGG C04608 text and MOL file. | supports | Official neutral formula C21H20O10, charge 0, full key KMOUJOKENFFTPU-QNDFHXLGSA-N, and five sugar stereocentres match. The definition correctly places the beta-D-glucosyl linkage at position 7. Parents CHEBI:22798 (beta-D-glucoside), CHEBI:38686 (dihydroxyflavone), CHEBI:50018 (glycosyloxyflavone), and CHEBI:63367 (monosaccharide derivative) agree. ChEBI explicitly separates conjugate base CHEBI:77722 and beta-L enantiomer CHEBI:132818. Its additional host anti-inflammatory role is not a bacterial target assertion. |
| chemistry | Independent RDKit calculations; 101-chemistry.json and 101-xref-chemistry.json. | supports | Both native structures match the formula, zero charge, one fragment, average mass 432.381, exact mass 432.1056468, and source mint. Independently parsed KEGG MOL yields the native full key. KNApSAcK InChI also yields that key; its other descriptors disagree internally. |
| knapsack | https://www.knapsackfamily.com/knapsack_core/information.php?word=C00001017; 101-knapsack.html/txt and 101-xref-chemistry.json. | partial | Entry names, formula, CAS number, and complete InChI identify the native glucoside. The displayed key is instead KMOUJOKENFFTPU-OHPGNTIMNA-N. Its SMILES leaves two sugar stereocentres unspecified and independently generates KMOUJOKENFFTPU-NFRVFMFJSA-N. Thus the linked entry contains mutually inconsistent descriptors. This does not prove an opposite stereoisomer or an incorrect native compound. |
| other-links | Official chemical/document endpoints; 101-fetch-results.json, 101-fetch2-results.json, and schema cross-reference expansion. | partial | CAS 578-74-5 is corroborated by ChEBI, KEGG, and KNApSAcK, rather than by direct registry inspection. HMDB0037340 returns 403; MetaCyc redirects to an account-required page; LINCS LSM-2286 returns 500; Reaxys 65669 was not directly inspected. ChEBI explicitly links these accessions and Wikipedia Apigetrin. The direct Wikipedia fetch returned 403, so its document identity is verified only through the source crosswalk. |
| adopted-citations | PMID:17186490&#124;PMID:19112896&#124;PMID:21656359&#124;PMID:21756194; 101-epmc.json; complete abstracts and DOI metadata inspected. | partial | PMID:17186490, DOI:10.1002/ptr.2061, isolates multiple compounds including the named glucoside from Marrubium globosum and tests pure compounds. Its abstract identifies three other compounds as most active but gives no exact glucoside MIC. PMID:19112896 identifies compound 4 by isolation, ESI-MS, and NMR as the glucoside; its abstract inconsistently names Pteris multifida and S. barbata, so source-organism assignment requires the full paper. PMID:21656359, DOI:10.1007/s12272-011-0507-3, validates rat-plasma pharmacokinetics after intravenous glucoside administration. PMID:21756194, DOI:10.1080/14786419.2010.532127, measures this glucoside and luteolin glucoside after intravenous Humulus extract. The latter two concern host analytical or pharmacokinetic work, not antibacterial mechanism. |
| primary2023 | DOI:10.2147/IDR.S387157; PMID:37070126, PMC10105580; full main Introduction, Methods, Results/Discussion, and Tables 1–2 in 101-2023.xml. | supports | Purchased apigenin 7-O-glucoside, stated purity 98%, from Shanghai Yuanye is tested. Table 1 gives MICs of 0.14 mg/mL for E. coli ATCC 25922 and 0.28 mg/mL for S. aureus ATCC 6538. MBICs of 0.10 and 0.20 mg/mL are a different crystal-violet endpoint. Methods use LB broth and 24-hour growth assessment. Sub-MIC treatment reduces biofilm formation, EPS production, and cell-surface hydrophobicity, with AFM context. Co-incubation experiments do not establish eradication of preformed biofilm. The material is named glucoside; no isolated monoanion, salt, or speciation characterization is reported. |
| mechanism2023 | DOI:10.2147/IDR.S387157; 101-2023.xml, Methods violacein assay and Results sections on QS, EPS, and CSH. | partial | The quorum-sensing reporter is Chromobacterium violaceum CV026 supplemented with C6-HSL; violacein decreases under the tested conditions. The authors extrapolate possible quorum-sensing effects to E. coli and S. aureus, but neither a direct protein target nor the proposed shared-pathway causality is established. EPS and cell-surface hydrophobicity changes are measured phenotypes. Binding to LuxS, Agr, or another protein is not measured. No transcriptomic experiment or accession is reported. |
| primary2025 | DOI:10.1080/13880209.2025.2511805; PMID:40457736, PMC12135086; full main article, compound 2 NMR assignments, and Tables 1–3 in 100-PMC12135086.xml. | supports | Origanum majorana isolate compound 2 is identified by 1D/2D NMR and literature comparison as apigenin 7-O-glucoside. Its MIC exceeds 100 µM in MRSA ATCC 43300 and E. coli ATCC 25922. At 50 and 100 µM, E. coli biofilm formation decreases by 33.75±1.62% and 42.98±2.18%, measured with crystal violet. MRSA effects are 13.38±0.87% and −1.10±0.67%. No MRSA efflux inhibition is observed: RFI is −0.002 and −0.08. Arbutin effects must not transfer. Isolation from plant material does not itself establish a biosynthetic pathway or clinical effect. |
| terminalia | DOI:10.3390/molecules30173595; PMID:40942120, PMC12430666; abstract, Results, and Methods in 100-PMC12430666.xml. | partial | The paper identifies a T. catappa active-band isolate as apigenin 7-O-beta-D-glucoside and reports MIC 9.5 µg/mL for clinical S. aureus and MRSA 1503. Confidence in that identity is limited: the assigned formula C21H20O10 has no nitrogen or carboxyl group, yet the FTIR discussion assigns nitrile and carboxylic groups; the claimed m/z 433.11 is outside the stated 500–1000 scan range; and the NMR description is weak and internally problematic. Quantitative activity should not be assigned to this exact identity without resolving characterization and purity. These concerns do not refute other independently supported glucoside assays. |
| search | CultureBotAI/AntibioticMech; 101-local-hits.txt and 101-maintained-search.txt; bounded exact-compound, synonym, and primary-DOI searches. | context_only | Searches that include ignored files identify source and queue records plus the adjacent anion. No target-specific curator override or primary annotation was found among the searched maintained paths. This is not proof that relevant literature is absent. The native record has no protein, expression, or omics claim requiring an organism-specific gene adapter. The retrieved primary experiments are phenotype assays rather than transcriptomics; no protein target is inferred from quorum-sensing language. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity, equivalence, evidence, targets, activity, producer, and audit rules; CLAUDE, HARMONIZATION, and CURATION guidance. | supports | Optional enrichment is not mandatory-field repair. Preserve neutral/ion and glycoside/aglycone boundaries, measured phenotypes versus direct targets, source isolation versus biosynthesis, and distinct assay endpoints. |
| validation | Documented focused checks; 101-focused-results.json, schema/strict logs, and 101-chemistry.json. | supports | Focused schema, strict validation, and independent chemistry all exit 0. An initial helper guessed the raw column chebi_accession and failed before source-row processing and validators. It was corrected to the actual column chebi_id; subsequent capture and checks succeeded. All 13 input hashes remain unchanged. |

## Limits And Additional Notes

- No native edits, paid sources, or contact occurred during research. All 13 captured input hashes remain unchanged.
- All four adopted abstracts and their metadata were read. The full Wiley page for PMID:17186490 returned 403; no exact glucoside MIC was inferred from its abstract. The other three adopted papers were reviewed at abstract level.
- The full main article and Tables 1–2 of PMID:37070126 were read; raw data and images were not reanalyzed. The full main article, NMR assignments, and Tables 1–3 of PMID:40457736 were read; Figure 1 was not independently visually inspected. The abstract, Results, and Methods of PMID:40942120 were inspected; this was not a complete article or spectra audit.
- KNApSAcK complete InChI supports identity, but its key and SMILES conflict. HMDB returned 403, MetaCyc required an account, and LINCS returned 500. Reaxys and the CAS registry were not directly inspected. The Wikipedia fetch returned 403. Source crosswalks do not independently verify every endpoint.
- The inspected primary experiments do not report supplied salt or ion speciation measurements. The 2023 purity of 98% is the authors supplier statement, not independent analytical verification. Origanum isolation does not establish a biosynthetic pathway.
- The bounded literature search is not exhaustive, and no absence of direct-target literature is claimed. Quorum-sensing reporter and EPS/hydrophobicity phenotypes do not establish a direct molecular target. The inspected mechanism paper reports no transcriptomic experiment or accession.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T090925Z-apigenin-glucoside
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Apigenin 7-O-beta-D-glucoside: supported neutral identity and activity; qualify
  external descriptors and mechanism scope'
started_at: '2026-10-21T08:55:40Z'
finished_at: '2026-10-21T09:09:25Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the record. Input capture preceded judgment.
    The entire native record and source row, maintained transformations, independent
    chemistry, official identifiers, all adopted citations, and bounded primary literature
    were reviewed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: Neutral stereospecific glucoside chemistry and the accepted ChEBI antibacterial
  role are supported. Original 2023 experiments provide antibacterial and biofilm-formation
  evidence for the named glucoside; a 2025 Origanum study adds independent phenotypic
  evidence. KNApSAcK has internally inconsistent descriptors, although its InChI matches
  native identity. Optional primary enrichment must preserve tested forms, assay endpoints,
  reporter organisms, and uncertainty in a separate 2025 Terminalia identity assignment.
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
  - path: data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside.yaml
    sha256: 3edb94e83eeeb73933d204f09d60cca034042a866d7af2250b4d8d61a52ffe00
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
- target_id: CHEBI:16778
  path: data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside.yaml
  label: apigenin 7-O-β-D-glucoside
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
  description: Whole exact record; adopted ChEBI row and adjacent conjugate-base row
    as boundary context; all four adopted abstracts; official identity and cross-references;
    original 2023 and 2025 activity evidence.
  selection: Queue 101, CHEBI:16778, neutral apigenin 7-O-beta-D-glucoside.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:16778
  exclusions:
  - target: CHEBI:77722 monoanion, apigenin aglycone, beta-L glucoside, acylated glycosides,
      and crude extracts
    reason: Distinct entities or mixtures. The neighboring anion is reviewed independently;
      shared scaffold or name does not permit unqualified identity or assay transfer.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Focused LinkML validation exited 0.
  target_ids:
  - CHEBI:16778
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Focused strict scan exited 0 with no ERROR rows.
  target_ids:
  - CHEBI:16778
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside.yaml --out /private/tmp/am-review-session/101-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: SMILES, InChI, formula, charge, masses, and mint identifier agree.
  target_ids:
  - CHEBI:16778
  evidence_ids:
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache .venv/bin/python
    /private/tmp/am-review-session/101-chemistry-check.py 101
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
  - CHEBI:16778
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
  - CHEBI:16778
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
  - CHEBI:16778
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
  - CHEBI:16778
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
  - CHEBI:16778
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
  - CHEBI:16778
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
  - CHEBI:16778
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
  - CHEBI:16778
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
  - CHEBI:16778
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside.yaml
  locator: Entire native YAML and four seed/reseed history events.
  accessed_at: '2026-10-21T08:59:32Z'
  support: supports
  summary: SEEDED/EXACT neutral compound; nine synonyms, four structural parents,
    one antibacterial role, seven chemical cross-references, one Wikipedia document,
    and one ChEBI source concept. No primary evidence, mode, target, resistance, quantified
    activity, producer, clinical, graph, or dataset assertion is currently present.
    Optional blanks are not schema defects.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: 101-raw.json, line 409; adjacent CHEBI:77722 row at line 1973; source configuration
    and extractor lines 176–335; seeder loading and building logic.
  accessed_at: '2026-10-21T08:59:32Z'
  support: supports
  summary: The three-star, in-scope row reproduces native identity, synonyms, parents,
    and antibacterial role CHEBI:33282. No source mechanism roles are present. Four
    PMID leads are intentionally not automatically seeded as claim evidence. Configuration
    accepts only checked or OK role edges. All 13 captured input hashes are unchanged.
    The neighboring anion has a distinct charge, formula, and full key and remains
    a separate record.
  snapshot_sha256: 29489fcad130bdc8c56924550728321cc3d493656a45e0827fe25e9a7e292a0d
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:16778
  locator: 101-chebi.html/txt and KEGG C04608 text and MOL file.
  accessed_at: '2026-10-21T08:59:32Z'
  support: supports
  summary: Official neutral formula C21H20O10, charge 0, full key KMOUJOKENFFTPU-QNDFHXLGSA-N,
    and five sugar stereocentres match. The definition correctly places the beta-D-glucosyl
    linkage at position 7. Parents CHEBI:22798 (beta-D-glucoside), CHEBI:38686 (dihydroxyflavone),
    CHEBI:50018 (glycosyloxyflavone), and CHEBI:63367 (monosaccharide derivative)
    agree. ChEBI explicitly separates conjugate base CHEBI:77722 and beta-L enantiomer
    CHEBI:132818. Its additional host anti-inflammatory role is not a bacterial target
    assertion.
  snapshot_sha256: e834cc45ded42d27b0636066fae6ba72cdeb45b47e64f636e73d68958b94b24e
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculations
  locator: 101-chemistry.json and 101-xref-chemistry.json.
  accessed_at: '2026-10-21T08:59:32Z'
  support: supports
  summary: Both native structures match the formula, zero charge, one fragment, average
    mass 432.381, exact mass 432.1056468, and source mint. Independently parsed KEGG
    MOL yields the native full key. KNApSAcK InChI also yields that key; its other
    descriptors disagree internally.
  snapshot_sha256: c6fbb78a7dc2904d92a6104a4ca18463be0fb7fd0cd96177cab4d23a2fd21b4f
- evidence_id: knapsack
  kind: database
  reference: https://www.knapsackfamily.com/knapsack_core/information.php?word=C00001017
  locator: 101-knapsack.html/txt and 101-xref-chemistry.json.
  accessed_at: '2026-10-21T08:59:32Z'
  support: partial
  summary: Entry names, formula, CAS number, and complete InChI identify the native
    glucoside. The displayed key is instead KMOUJOKENFFTPU-OHPGNTIMNA-N. Its SMILES
    leaves two sugar stereocentres unspecified and independently generates KMOUJOKENFFTPU-NFRVFMFJSA-N.
    Thus the linked entry contains mutually inconsistent descriptors. This does not
    prove an opposite stereoisomer or an incorrect native compound.
  snapshot_sha256: f18993821674a996c2df009bac4f6d994801a02daf4c1212576b88838058eeab
- evidence_id: other-links
  kind: database
  reference: Official chemical/document endpoints
  locator: 101-fetch-results.json, 101-fetch2-results.json, and schema cross-reference
    expansion.
  accessed_at: '2026-10-21T08:59:32Z'
  support: partial
  summary: CAS 578-74-5 is corroborated by ChEBI, KEGG, and KNApSAcK, rather than
    by direct registry inspection. HMDB0037340 returns 403; MetaCyc redirects to an
    account-required page; LINCS LSM-2286 returns 500; Reaxys 65669 was not directly
    inspected. ChEBI explicitly links these accessions and Wikipedia Apigetrin. The
    direct Wikipedia fetch returned 403, so its document identity is verified only
    through the source crosswalk.
  snapshot_sha256: 636bd2071b5bd5da81d3040298a8b6408776a3d45271d459396254106c73feed
- evidence_id: adopted-citations
  kind: primary_source
  reference: PMID:17186490|PMID:19112896|PMID:21656359|PMID:21756194
  locator: 101-epmc.json; complete abstracts and DOI metadata inspected.
  accessed_at: '2026-10-21T08:59:32Z'
  support: partial
  summary: PMID:17186490, DOI:10.1002/ptr.2061, isolates multiple compounds including
    the named glucoside from Marrubium globosum and tests pure compounds. Its abstract
    identifies three other compounds as most active but gives no exact glucoside MIC.
    PMID:19112896 identifies compound 4 by isolation, ESI-MS, and NMR as the glucoside;
    its abstract inconsistently names Pteris multifida and S. barbata, so source-organism
    assignment requires the full paper. PMID:21656359, DOI:10.1007/s12272-011-0507-3,
    validates rat-plasma pharmacokinetics after intravenous glucoside administration.
    PMID:21756194, DOI:10.1080/14786419.2010.532127, measures this glucoside and luteolin
    glucoside after intravenous Humulus extract. The latter two concern host analytical
    or pharmacokinetic work, not antibacterial mechanism.
  snapshot_sha256: 1189c71d9c4fd1521676e1a8484b533e5b620d159e845d34a011021c9739a773
- evidence_id: primary2023
  kind: primary_source
  reference: DOI:10.2147/IDR.S387157
  locator: PMID:37070126, PMC10105580; full main Introduction, Methods, Results/Discussion,
    and Tables 1–2 in 101-2023.xml.
  accessed_at: '2026-10-21T08:59:32Z'
  support: supports
  summary: Purchased apigenin 7-O-glucoside, stated purity 98%, from Shanghai Yuanye
    is tested. Table 1 gives MICs of 0.14 mg/mL for E. coli ATCC 25922 and 0.28 mg/mL
    for S. aureus ATCC 6538. MBICs of 0.10 and 0.20 mg/mL are a different crystal-violet
    endpoint. Methods use LB broth and 24-hour growth assessment. Sub-MIC treatment
    reduces biofilm formation, EPS production, and cell-surface hydrophobicity, with
    AFM context. Co-incubation experiments do not establish eradication of preformed
    biofilm. The material is named glucoside; no isolated monoanion, salt, or speciation
    characterization is reported.
  snapshot_sha256: b4539aed4bd9ec82f10b00ebe1bd441e096636d57f96d725e684b7c1be911aa1
- evidence_id: mechanism2023
  kind: primary_source
  reference: DOI:10.2147/IDR.S387157
  locator: 101-2023.xml, Methods violacein assay and Results sections on QS, EPS,
    and CSH.
  accessed_at: '2026-10-21T08:59:32Z'
  support: partial
  summary: The quorum-sensing reporter is Chromobacterium violaceum CV026 supplemented
    with C6-HSL; violacein decreases under the tested conditions. The authors extrapolate
    possible quorum-sensing effects to E. coli and S. aureus, but neither a direct
    protein target nor the proposed shared-pathway causality is established. EPS and
    cell-surface hydrophobicity changes are measured phenotypes. Binding to LuxS,
    Agr, or another protein is not measured. No transcriptomic experiment or accession
    is reported.
  snapshot_sha256: b4539aed4bd9ec82f10b00ebe1bd441e096636d57f96d725e684b7c1be911aa1
- evidence_id: primary2025
  kind: primary_source
  reference: DOI:10.1080/13880209.2025.2511805
  locator: PMID:40457736, PMC12135086; full main article, compound 2 NMR assignments,
    and Tables 1–3 in 100-PMC12135086.xml.
  accessed_at: '2026-10-21T08:59:32Z'
  support: supports
  summary: 'Origanum majorana isolate compound 2 is identified by 1D/2D NMR and literature
    comparison as apigenin 7-O-glucoside. Its MIC exceeds 100 µM in MRSA ATCC 43300
    and E. coli ATCC 25922. At 50 and 100 µM, E. coli biofilm formation decreases
    by 33.75±1.62% and 42.98±2.18%, measured with crystal violet. MRSA effects are
    13.38±0.87% and −1.10±0.67%. No MRSA efflux inhibition is observed: RFI is −0.002
    and −0.08. Arbutin effects must not transfer. Isolation from plant material does
    not itself establish a biosynthetic pathway or clinical effect.'
  snapshot_sha256: 4a014cd86b7dfa5b736e5eb8402a9a92734822378c0290a90d15cc11432adeac
- evidence_id: terminalia
  kind: primary_source
  reference: DOI:10.3390/molecules30173595
  locator: PMID:40942120, PMC12430666; abstract, Results, and Methods in 100-PMC12430666.xml.
  accessed_at: '2026-10-21T08:59:32Z'
  support: partial
  summary: 'The paper identifies a T. catappa active-band isolate as apigenin 7-O-beta-D-glucoside
    and reports MIC 9.5 µg/mL for clinical S. aureus and MRSA 1503. Confidence in
    that identity is limited: the assigned formula C21H20O10 has no nitrogen or carboxyl
    group, yet the FTIR discussion assigns nitrile and carboxylic groups; the claimed
    m/z 433.11 is outside the stated 500–1000 scan range; and the NMR description
    is weak and internally problematic. Quantitative activity should not be assigned
    to this exact identity without resolving characterization and purity. These concerns
    do not refute other independently supported glucoside assays.'
  snapshot_sha256: d65c10c95abdc8efba1cfa2fc04457997ad6c7cbfcd62657d0b50943b95fdb74
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 101-local-hits.txt and 101-maintained-search.txt; bounded exact-compound,
    synonym, and primary-DOI searches.
  accessed_at: '2026-10-21T08:59:32Z'
  support: context_only
  summary: Searches that include ignored files identify source and queue records plus
    the adjacent anion. No target-specific curator override or primary annotation
    was found among the searched maintained paths. This is not proof that relevant
    literature is absent. The native record has no protein, expression, or omics claim
    requiring an organism-specific gene adapter. The retrieved primary experiments
    are phenotype assays rather than transcriptomics; no protein target is inferred
    from quorum-sensing language.
  search_scope: rg --no-ignore --hidden for apigenin.7, Apigetrin, cosmosiin, Cosmosiin,
    CHEBI:16778, and KMOUJOKENFFTPU across batch 011 and maintained curation/conf/scripts/data/raw/src/reports/reviews,
    excluding .git and .venv. Exact PubMed, Europe PMC, and Wiley DOI searches; apigetrin,
    cosmosiin, and Pei 2023 activity searches; official ChEBI, KEGG, KNApSAcK, HMDB,
    MetaCyc, and LINCS routes. Free sources only.
  snapshot_sha256: 7479172417272573862b66cfe7bb4c314aa21ff8751fb67ea7b301e5d20ce65c
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity, equivalence, evidence, targets, activity, producer, and audit
    rules; CLAUDE, HARMONIZATION, and CURATION guidance.
  accessed_at: '2026-10-21T08:59:32Z'
  support: supports
  summary: Optional enrichment is not mandatory-field repair. Preserve neutral/ion
    and glycoside/aglycone boundaries, measured phenotypes versus direct targets,
    source isolation versus biosynthesis, and distinct assay endpoints.
- evidence_id: validation
  kind: validation
  reference: Documented focused checks
  locator: 101-focused-results.json, schema/strict logs, and 101-chemistry.json.
  accessed_at: '2026-10-21T08:59:32Z'
  support: supports
  summary: Focused schema, strict validation, and independent chemistry all exit 0.
    An initial helper guessed the raw column chebi_accession and failed before source-row
    processing and validators. It was corrected to the actual column chebi_id; subsequent
    capture and checks succeeded. All 13 input hashes remain unchanged.
  snapshot_sha256: 83848c7b896d21465d6bbfec470960651e887b765684ed495fbbc360ccf1287b
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral exact structure and conjugate-base boundary
  outcome: supported
  summary: Native structure, definition, and accepted role match the official source
    and independent KEGG chemistry. The adjacent anion is distinct, not a duplicate.
  target_ids:
  - CHEBI:16778
  evidence_ids:
  - identity
  - chemistry
  - source
- assessment_id: xref
  area: evidence
  topic: KNApSAcK internal descriptors
  outcome: concern
  summary: The complete InChI agrees, while the displayed key and underspecified SMILES
    disagree. Qualify endpoint reliability without asserting an incorrect native entity.
  target_ids:
  - CHEBI:16778
  evidence_ids:
  - knapsack
  - chemistry
- assessment_id: activity
  area: evidence
  topic: Antibacterial role and named-compound assays
  outcome: supported
  summary: Purchased-glucoside activity in 2023 corroborates the source role; the
    2025 Origanum study adds independent biofilm data. The adopted abstract alone
    does not provide an exact MIC, and the Terminalia identity requires qualification.
  target_ids:
  - CHEBI:16778
  evidence_ids:
  - primary2023
  - primary2025
  - adopted-citations
  - terminalia
- assessment_id: mechanism
  area: completeness
  topic: Optional phenotype and mechanism enrichment
  outcome: unknown
  summary: Measured EPS, hydrophobicity, biofilm, and reporter results are available.
    A direct target and causality across species remain unestablished. Missing an
    optional target is not an error.
  target_ids:
  - CHEBI:16778
  evidence_ids:
  - mechanism2023
  - primary2025
  - rubric
- assessment_id: other
  area: completeness
  topic: Producer, clinical, resistance, omics, and graphs
  outcome: unknown
  summary: No unsupported native claims. Plant isolation and host pharmacokinetics
    do not establish a biosynthetic pathway, clinical approval, or antibacterial target.
    No omics dataset is inferred.
  target_ids:
  - CHEBI:16778
  evidence_ids:
  - record
  - adopted-citations
  - primary2025
  - search
- assessment_id: ownership
  area: ownership
  topic: Maintained source versus curator additions
  outcome: supported
  summary: ChEBI source, extractor, seeder, and decision owners are captured. The
    actual native record path owns optional primary annotations.
  target_ids:
  - CHEBI:16778
  evidence_ids:
  - source
  - search
- assessment_id: gates
  area: schema
  topic: Focused gates and history
  outcome: supported
  summary: Focused checks pass; SEEDED status and history are consistent. No REVIEWED
    promotion is made.
  target_ids:
  - CHEBI:16778
  evidence_ids:
  - validation
  - record
findings:
- finding_id: F1
  issue_key: apigenin-glucoside-knapsack-internal-descriptor-conflict
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify KNApSAcK descriptor inconsistency
  description: KNApSAcK C00001017 has a complete InChI matching the native compound,
    but its displayed InChIKey and partially specified stereochemical SMILES disagree.
    The linked entry has an internal conflict. This does not establish that it denotes
    an opposite isomer or justify replacing native chemistry.
  target_ids:
  - CHEBI:16778
  field_paths:
  - xrefs
  evidence_ids:
  - knapsack
  - chemistry
  - identity
  - rubric
  rule_id: 'native-review-checklist: Identity/Equivalence'
  native_severity: Minor qualification of external descriptor reliability.
  normalization_reason: The exact entity has a matching complete InChI and independent
    KEGG support. The issue is inconsistent external descriptors, not a demonstrated
    native identity error.
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
- finding_id: F2
  issue_key: apigenin-glucoside-qualified-primary-activity-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Add bounded primary activity and phenotypic evidence
  description: The 2023 purchased-glucoside and 2025 Origanum studies support optional
    activity and biofilm annotation. Preserve MIC versus MBIC or biomass endpoints
    and the tested strains. The CV026 reporter does not establish E. coli or S. aureus
    quorum-sensing protein targets. The exact identity of the 2025 Terminalia isolate
    remains uncertain. Do not transfer assays without qualification to the separately
    recorded monoanion.
  target_ids:
  - CHEBI:16778
  field_paths:
  - activity_spectrum
  - mode_of_action
  - evidence
  - discussions
  evidence_ids:
  - primary2023
  - mechanism2023
  - primary2025
  - terminalia
  - adopted-citations
  - rubric
  rule_id: 'native-review-checklist: Activity/Targets/Evidence/Completeness'
  native_severity: Informational opportunity for optional primary enrichment.
  normalization_reason: The native record contains no exaggerated mechanism or quantitative
    claims. Missing optional annotations are not mandatory-field defects.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside.yaml
    role: Curator-owned activity,mechanism,evidence and discussions through validated
      writer/history
actions:
- action_id: A1
  description: Document the exact KNApSAcK descriptor disagreement through maintained
    source ownership.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:16778
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
  acceptance_checks:
  - Recheck the current KNApSAcK InChI, key, and SMILES independently; preserve the
    correct native full key and evidence from the complete InChI.
  - Apply a documented source-specific qualification or curatorial decision if needed.
    Do not silently replace native chemistry or infer opposite stereochemistry from
    unspecified centres. Preserve provenance and verify that any future change survives
    reseeding.
- action_id: A2
  description: Optionally curate qualified exact-compound activity and phenotypic
    mechanism evidence on the native record.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:16778
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside.yaml
    role: Curator-owned activity,mechanism,evidence and discussions through validated
      writer/history
  acceptance_checks:
  - Use PMID:37070126 with the exact supplier, material, strains, LB broth, 24-hour
    incubation, and Table 1 MIC/MBIC distinctions. Keep biofilm formation during co-incubation
    separate from eradication of preformed biofilm.
  - Use PMID:40457736 compound 2 NMR identity and qualified phenotypes from Tables
    2–3. Retain MIC >100 µM and the negative efflux result. Do not transfer arbutin,
    extract, or fraction effects.
  - Keep the CV026 violacein reporter separate from E. coli and S. aureus mechanisms.
    Do not add a LuxS or Agr direct target without binding or inhibition evidence.
    No gene-expression dataset is reported.
  - Resolve the characterization and purity inconsistencies in PMID:40942120 before
    using its exact-compound MIC. Preserve the plant-source ambiguity in adopted PMID:19112896.
    Do not infer a biosynthetic pathway or clinical efficacy from isolation or pharmacokinetics.
  - Preserve the neutral-compound versus CHEBI:77722 ion boundary and glucoside versus
    apigenin-aglycone distinction. Use write_validated_antibiotic and record_curation_event
    on data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside.yaml for an authorized
    future mutation. Run focused and shared gates without automatic REVIEWED promotion.
limitations:
- No native edits, paid sources, or contact occurred during research. All 13 captured
  input hashes remain unchanged.
- All four adopted abstracts and their metadata were read. The full Wiley page for
  PMID:17186490 returned 403; no exact glucoside MIC was inferred from its abstract.
  The other three adopted papers were reviewed at abstract level.
- The full main article and Tables 1–2 of PMID:37070126 were read; raw data and images
  were not reanalyzed. The full main article, NMR assignments, and Tables 1–3 of PMID:40457736
  were read; Figure 1 was not independently visually inspected. The abstract, Results,
  and Methods of PMID:40942120 were inspected; this was not a complete article or
  spectra audit.
- KNApSAcK complete InChI supports identity, but its key and SMILES conflict. HMDB
  returned 403, MetaCyc required an account, and LINCS returned 500. Reaxys and the
  CAS registry were not directly inspected. The Wikipedia fetch returned 403. Source
  crosswalks do not independently verify every endpoint.
- The inspected primary experiments do not report supplied salt or ion speciation
  measurements. The 2023 purity of 98% is the authors supplier statement, not independent
  analytical verification. Origanum isolation does not establish a biosynthetic pathway.
- The bounded literature search is not exhaustive, and no absence of direct-target
  literature is claimed. Quorum-sensing reporter and EPS/hydrophobicity phenotypes
  do not establish a direct molecular target. The inspected mechanism paper reports
  no transcriptomic experiment or accession.
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
