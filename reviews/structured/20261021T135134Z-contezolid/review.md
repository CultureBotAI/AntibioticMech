# Contezolid: coherent exact identity; qualify approved indication separately from antibacterial spectrum

- Review: 20261021T135134Z-contezolid
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T13:38:55Z
- Finished UTC: 2026-10-21T13:51:34Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The neutral single-S-stereocentre contezolid graph agrees across native, CARD, PubChem and ChEMBL. Its oxazolidinone classification and antibacterial activity are supported. One minor definition finding separates the dated Chinese approval for complicated skin and soft tissue infections from broader in vitro activity, including VRE. The cited paper itself makes that distinction; it is a pharmacokinetic/modeling study, not evidence of approval for all resistant Gram-positive infections.

## Scope And Provenance

Entire native definition and citation, broader parent and structural class, chemical structure/properties and retrieval date, three xrefs, source concept, minted grounding and all three history events. Sole adopted publication fully inspected; bounded primary antibacterial and regulatory follow-up.

Selection: Queue324. Original thirteen input hashes retained; actual ARO row, PubChem enrichment table and enrichment script appended before assessment, for sixteen inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-ca0e85f42a | data/antibiotics/antibacterial/contezolid.yaml | generated | contezolid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | antibioticmech:aro-ca0e85f42a | Zero schema errors. |
| strict | passed | True | antibioticmech:aro-ca0e85f42a | One file; zero strict errors. |
| chemistry | passed | False | antibioticmech:aro-ca0e85f42a | Native SMILES/InChI, full key, neutral charge, formula, rounded masses and single S centre agree; ARO source mint reproduces. |
| external-chemistry | passed | False | antibioticmech:aro-ca0e85f42a | Five independently parsed CARD, PubChem and ChEMBL encodings reproduce the native full key. |
| Authoritative full QC | failed | True | antibioticmech:aro-ca0e85f42a | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-ca0e85f42a | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-ca0e85f42a | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-ca0e85f42a | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-ca0e85f42a | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-ca0e85f42a | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-ca0e85f42a | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-ca0e85f42a | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-ca0e85f42a | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral S-configured active compound and source mint

identity: supported. Targets: antibioticmech:aro-ca0e85f42a.

Native and official encodings, masses, charge, formula and mint agree. Contezolid is distinguished from its prodrug and metabolites.

### Approved indication versus resistant-organism activity

evidence: concern. Targets: antibioticmech:aro-ca0e85f42a.

The definition compresses separate approval and spectrum statements. Dated Chinese sources support a specific cSSTI indication; the primary PK paper explicitly preserves that boundary. Qualify the sentence without denying experimentally supported VRE activity.

### Antibacterial filing and oxazolidinone classification

evidence: supported. Targets: antibioticmech:aro-ca0e85f42a.

The exact chemical class and compound-specific susceptibility evidence support ANTIBACTERIAL filing. No quantitative native activity claim requires correction. Laboratory activity and an authorized clinical indication remain separate.

### Optional mechanism and evidence depth

evidence: unknown. Targets: antibioticmech:aro-ca0e85f42a.

No native target or mechanistic edge is present. A compound-specific primary mechanism follow-up would be required before direct binding curation; the PK study, regulatory summary and general parent class do not independently establish such a measurement.

### Actual maintained ownership and historical capture

provenance: supported. Targets: antibioticmech:aro-ca0e85f42a.

ARO and PubChem enrichment owners were appended before assessment while preserving the thirteen original hashes. Source definition, xrefs, structure/date, minted grounding and three seed-history events reconcile.

## Findings

### F1: Separate the approved Chinese indication from the broader laboratory spectrum

minor / open / confirmed; issue key: contezolid-approval-spectrum-definition-scope.

The definition says contezolid is newly approved for MDR Gram-positive infections, including VRE, without jurisdiction, date or indication. Its cited paper distinguishes 2021 Chinese cSSTI approval from in vitro activity. Official and manufacturer sources confirm the bounded indication. Rewrite the approval clause with China, 2021 and cSSTI, and present resistant-organism activity separately with appropriate evidence. Do not interpret this as lack of VRE activity or as an exhaustive determination of all countries and later indications.

## Recommended Actions And Acceptance Checks

### A1

Qualify the maintained definition and preserve the distinction between product authorization and antibacterial spectrum.

- Use dated, jurisdiction-specific language for the Chinese cSSTI approval and retain the approved pathogen scope when describing the label. Replace the relative term newly with an actual date.
- State VRE and other resistant-organism activity separately at the scope supported by the original experiments. Do not present laboratory susceptibility as an authorized indication.
- Keep PMID 36992830 accurately characterized as a small human PK/modeling study, with separate official approval provenance. Rerun source generation and focused validation after an authorized maintained-source correction.

### A2

Optionally add exact-material primary activity or mechanism evidence without transferring adjacent compound claims.

- Read complete original susceptibility methods and tables before importing measurements, assay conditions or breakpoints. Preserve population endpoints and distinguish contezolid from MRX-4 and its metabolites.
- Require compound-specific direct evidence for any direct ribosomal binding claim. Keep human metabolism and modeled PK/PD target attainment separate from microbial molecular targets and measured susceptibility.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/contezolid.yaml; Entire native YAML. | supports | SEEDED/MINTED/ANTIBACTERIAL. The definition joins newly approved treatment with a broad resistant Gram-positive spectrum including VRE. No separate clinical_status, molecular target, quantitative activity, resistance mechanism, producer or causal graph is populated. Native graph is neutral C18H15F3N4O4, full key SULYVXZZUMRQAX-NSHDSACASA-N. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/enrich_pubchem_structures.py; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; conf/sources.yaml; data/raw/MANIFEST.yaml; Complete ARO row 419, PubChem row 151 and relevant extraction, structure enrichment and mint/class logic. | supports | ARO supplies the exact definition, PMID 36992830, class and xrefs; PubChem supplies the graph and dated properties. The current native reproduces both rows. No matching adopted ChEBI identity, target/resistance edge, FDA or MIBiG row occurs in the inspected maintained tables. The source mint is SHA256-derived from ARO&#124;ARO:3007474. MINTED is an explicit source-identity route, not a claim of missing chemical structure. |
| identity | ARO:3007474; pubchem.compound:25184541; chembl:CHEMBL3287379; https://card.mcmaster.ca/aro/3007474; Complete current CARD entry, PubChem molecular properties and ChEMBL molecular entry. | supports | All three asserted exact xrefs resolve to contezolid. Independent SMILES/InChI parsing yields the native full key for five encodings, with one assigned S stereocentre and no counterion. PubChem mass 408.3 is rounded; calculated average 408.336 and exact 408.10453962 agree at the reported precision. The distinct water-soluble acefosamil prodrug is not represented by this graph. |
| class | https://card.mcmaster.ca/aro/3000079; Official ARO oxazolidinone class and parent/child relations. | supports | ARO 3000079 is strictly broader than contezolid and supports structural_class and parent_compounds. Its generic ribosomal mechanism and stale statement that linezolid is the only clinically used member are not imported as native contezolid-specific target or regulatory evidence. |
| adopted-primary | PMID:36992830; DOI:10.3389/fphar.2023.1135007; PMC10040594; Entire original main XML including Introduction, Methods, Results, Tables 1–3, Discussion and figure captions; supplements and raw data not independently inspected. | supports | The Introduction separately states approval in China in 2021 for cSSTI and activity against resistant Gram-positive organisms including VRE. The actual study gives a single oral 800 mg dose to six moderately hepatically impaired and six healthy participants, measures drug/metabolite PK, and models repeated-dose MRSA target attainment. It does not test cure of VRE infection or create a new approval. Simulated MIC coverage is not a new measured isolate MIC, and human metabolism is not a microbial target. The authors acknowledge small sample size, single-dose design and unmeasured unbound concentration. |
| regulator | https://mpa.xinjiang.gov.cn/xjyjj/gjjdt/202106/70d2a6e9db6c4d8ab11e737b2d0ad9bc.shtml; Complete June 2, 2021 NMPA announcement reproduced by the Xinjiang drug regulator, explicitly credited to NMPA. | refutes | The approved tablet indication is complicated skin and soft tissue infection caused by susceptible S. aureus, including methicillin-sensitive/resistant strains, S. pyogenes or S. agalactiae. The announcement does not list VRE. It supports a dated Chinese product indication, not unrestricted approval for the full laboratory spectrum. |
| nhsa | https://www.nhsa.gov.cn/attach/Ypsn2025/YPSN202500200/YPSN202500200.pdf; Manufacturer public reimbursement submission dated July 19, 2025, pp2–3: all labeled indications and initial approval date. | supports | The government-hosted manufacturer filing gives the same three-pathogen cSSTI indication, identifies 400 mg tablets and states initial approval June 1, 2021. It expressly notes that approved indications remain limited to cSSTI. This is an applicant disclosure hosted by NHSA, not an independent new NMPA approval decision. The full linked legal label was not obtained. |
| manufacturer | https://www.micurxchina.com/678.html; Complete June 2, 2021 manufacturer approval announcement. | supports | MicuRx reports the Chinese cSSTI approval and distinguishes it from the broad development program against resistant Gram-positive organisms. The same dated announcement calls FDA QIDP/Fast Track designations and US phase II development distinct from future approvals. These historical statements are not an exhaustive current worldwide regulatory census. |
| susceptibility | PMID:32778552; DOI:10.1128/AAC.01195-20; Complete original indexed abstract; full article attempts returned XML 500, PMC challenge and inaccessible publisher/EuropePMC routes. | supports | In a collection of 1,211 clinical Gram-positive isolates, contezolid inhibited all tested MRSA and vancomycin-resistant E. faecium isolates at ≤1 mg/L. This directly supports bounded laboratory activity. It does not establish an approved VRE indication, species-wide susceptibility or the exact bulk salt of every tested lot. Full methods, isolate-level tables and chemical-material certification were not inspected. |
| mechanism-context | PMID:24694071; DOI:10.1021/jm401931e; ARO:3000079; Complete original indexed abstract of the 2014 medicinal-chemistry annotation/review and the official class definition. | context_only | The annotation identifies the S-configured MRX-I compound and summarizes protein-synthesis-inhibitor class development. It is labeled a review and was not inspected as a direct ribosomal binding experiment. The bounded search did not supply an independently read contezolid-specific structural binding assay. No direct-binding edge is inferred from the parent class or human PK study. |
| adapter | Structured source applicability assessment; Native fields and actual maintained rows inspected before web research. | context_only | The native record has no gene, protein, pathway, stress-response or transcriptomic claim. MRSA/VRE are phenotype descriptions here. Structured iModulonDB follow-up is not applicable to verifying this chemical identity or the approved indication; class-level ribosome language is not silently promoted into a native target. |
| search | 324-inclusive-hits.txt;324-literature.json;324-lab-original.json; Ignored-inclusive local exact-name/identifier/key search and bounded public official/citation research. | context_only | The exact record, source rows and generated context were found. No exact maintained override or curator evidence overlay occurred in the searched local scope. Public official sources resolve the approval boundary; broad MRX-I searches also return unrelated MRX compounds, which are excluded. An unsuccessful manufacturer-label download and full-article access attempts remain explicit limits. |
| validation | 324-schema.log;324-strict.log;324-chemistry.json;324-xref-chemistry.json; Actual focused deterministic checks and final captured-input comparison. | supports | All focused checks exit 0 and all sixteen input hashes remain unchanged, including the original thirteen. The raw ARO definition reproduces native, so the wording correction belongs to maintained source/override handling. |

## Limits And Additional Notes

- The sole adopted PMID 36992830 was read completely in main XML scope, including tables and figure captions; supplements, raw data and figure images were not independently reprocessed. The study measured single-dose PK in twelve participants and simulated efficacy-related targets; it did not directly test VRE clinical outcomes.
- PMID 32778552 was read at complete original-abstract depth. EuropePMC XML returned 500, PMC requests returned challenge HTML, and public publisher/EuropePMC full-text routes failed. Its methods, numerical tables and exact test-material certificate were not inspected.
- The 2025 NHSA-hosted manufacturer disclosure was read for the relevant labeled-indication and approval-date sections, not as a full reassessment of clinical, economic or safety claims. The direct manufacturer label link timed out; no inaccessible label content is claimed read.
- The bounded regulatory audit establishes the Chinese source wording conflict; it does not exhaustively determine current approval or marketing status worldwide. A 2021 announcement is explicitly historical.
- Primary mechanism evidence remains a follow-up opportunity. Optional absent activity, mechanism, resistance, producer and clinical-status fields are not additional defects; no clinical recommendation is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T135134Z-contezolid
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Contezolid: coherent exact identity; qualify approved indication separately
  from antibacterial spectrum'
started_at: '2026-10-21T13:38:55Z'
finished_at: '2026-10-21T13:51:34Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the native record. Verified initial hashes before
    judgment, appended actual ARO and PubChem enrichment owners while preserving all
    original inputs, read the complete native/source rows and sole cited primary paper,
    independently checked official structures, and inspected regulatory and manufacturer
    material.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The neutral single-S-stereocentre contezolid graph agrees across native,
  CARD, PubChem and ChEMBL. Its oxazolidinone classification and antibacterial activity
  are supported. One minor definition finding separates the dated Chinese approval
  for complicated skin and soft tissue infections from broader in vitro activity,
  including VRE. The cited paper itself makes that distinction; it is a pharmacokinetic/modeling
  study, not evidence of approval for all resistant Gram-positive infections.
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
  - path: data/antibiotics/antibacterial/contezolid.yaml
    sha256: aed7655b59d80b1d0592b0757ac2c1ae1b299f02e09e947cdde62b9ab8fcbdfe
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/chebi_antimicrobials.tsv
    sha256: 4c33e56c3c342be657309f720f5b5cb9cad1fae13bec202ef99e449503c32004
    role: context
  - path: data/raw/chebi_role_names.tsv
    sha256: 5c476c0aacd7c98d7241d2343a6fc41ee9eb9338077404c5b011a04bf40c6ac5
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
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
- target_id: antibioticmech:aro-ca0e85f42a
  path: data/antibiotics/antibacterial/contezolid.yaml
  label: contezolid
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO inventory extraction and class mapping
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual maintained source input or enrichment transform
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual maintained source input or enrichment transform
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Actual maintained source input or enrichment transform
scope:
  description: Entire native definition and citation, broader parent and structural
    class, chemical structure/properties and retrieval date, three xrefs, source concept,
    minted grounding and all three history events. Sole adopted publication fully
    inspected; bounded primary antibacterial and regulatory follow-up.
  selection: Queue324. Original thirteen input hashes retained; actual ARO row, PubChem
    enrichment table and enrichment script appended before assessment, for sixteen
    inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-ca0e85f42a
  exclusions:
  - target: Contezolid acefosamil/MRX-4, metabolites M2/MRX445-1 and MRX459, and other
      oxazolidinones
    reason: Distinct chemical entities are not substituted for neutral contezolid/MRX-I;
      prodrug, metabolite and class-level claims are not exact native evidence.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Zero schema errors.
  target_ids:
  - antibioticmech:aro-ca0e85f42a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/contezolid.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: One file; zero strict errors.
  target_ids:
  - antibioticmech:aro-ca0e85f42a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/contezolid.yaml --out /private/tmp/am-review-session/324-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Native SMILES/InChI, full key, neutral charge, formula, rounded masses
    and single S centre agree; ARO source mint reproduces.
  target_ids:
  - antibioticmech:aro-ca0e85f42a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 324
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: external-chemistry
  name: external-chemistry
  status: passed
  required: false
  summary: Five independently parsed CARD, PubChem and ChEMBL encodings reproduce
    the native full key.
  target_ids:
  - antibioticmech:aro-ca0e85f42a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/324-xref-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-ca0e85f42a
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
  - antibioticmech:aro-ca0e85f42a
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
  - antibioticmech:aro-ca0e85f42a
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
  - antibioticmech:aro-ca0e85f42a
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
  - antibioticmech:aro-ca0e85f42a
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
  - antibioticmech:aro-ca0e85f42a
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
  - antibioticmech:aro-ca0e85f42a
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
  - antibioticmech:aro-ca0e85f42a
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
  - antibioticmech:aro-ca0e85f42a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/contezolid.yaml
  locator: Entire native YAML.
  accessed_at: '2026-10-21T13:46:20Z'
  support: supports
  summary: SEEDED/MINTED/ANTIBACTERIAL. The definition joins newly approved treatment
    with a broad resistant Gram-positive spectrum including VRE. No separate clinical_status,
    molecular target, quantitative activity, resistance mechanism, producer or causal
    graph is populated. Native graph is neutral C18H15F3N4O4, full key SULYVXZZUMRQAX-NSHDSACASA-N.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/enrich_pubchem_structures.py;
    scripts/extract_source_inventory.py; scripts/seed_from_sources.py; conf/sources.yaml;
    data/raw/MANIFEST.yaml
  locator: Complete ARO row 419, PubChem row 151 and relevant extraction, structure
    enrichment and mint/class logic.
  accessed_at: '2026-10-21T13:46:20Z'
  support: supports
  summary: ARO supplies the exact definition, PMID 36992830, class and xrefs; PubChem
    supplies the graph and dated properties. The current native reproduces both rows.
    No matching adopted ChEBI identity, target/resistance edge, FDA or MIBiG row occurs
    in the inspected maintained tables. The source mint is SHA256-derived from ARO|ARO:3007474.
    MINTED is an explicit source-identity route, not a claim of missing chemical structure.
  snapshot_sha256: c172dc56bd519fffbc88f280ce6961b45c91abcdc875c85084cb10c6ebc474de
- evidence_id: identity
  kind: authority
  reference: ARO:3007474; pubchem.compound:25184541; chembl:CHEMBL3287379; https://card.mcmaster.ca/aro/3007474
  locator: Complete current CARD entry, PubChem molecular properties and ChEMBL molecular
    entry.
  accessed_at: '2026-10-21T13:46:20Z'
  support: supports
  summary: All three asserted exact xrefs resolve to contezolid. Independent SMILES/InChI
    parsing yields the native full key for five encodings, with one assigned S stereocentre
    and no counterion. PubChem mass 408.3 is rounded; calculated average 408.336 and
    exact 408.10453962 agree at the reported precision. The distinct water-soluble
    acefosamil prodrug is not represented by this graph.
  snapshot_sha256: 26aab59fbf9ba911a7b653554c9432269d7ee17888226c2dc7446f5bf7da2787
- evidence_id: class
  kind: authority
  reference: https://card.mcmaster.ca/aro/3000079
  locator: Official ARO oxazolidinone class and parent/child relations.
  accessed_at: '2026-10-21T13:42:57Z'
  support: supports
  summary: ARO 3000079 is strictly broader than contezolid and supports structural_class
    and parent_compounds. Its generic ribosomal mechanism and stale statement that
    linezolid is the only clinically used member are not imported as native contezolid-specific
    target or regulatory evidence.
  snapshot_sha256: 500f2a2eb8d230f73520d1dc96761402a88230aaaaf81a249d54dd4c40ed7519
- evidence_id: adopted-primary
  kind: primary_source
  reference: PMID:36992830; DOI:10.3389/fphar.2023.1135007; PMC10040594
  locator: Entire original main XML including Introduction, Methods, Results, Tables
    1–3, Discussion and figure captions; supplements and raw data not independently
    inspected.
  accessed_at: '2026-10-21T13:43:25Z'
  support: supports
  summary: The Introduction separately states approval in China in 2021 for cSSTI
    and activity against resistant Gram-positive organisms including VRE. The actual
    study gives a single oral 800 mg dose to six moderately hepatically impaired and
    six healthy participants, measures drug/metabolite PK, and models repeated-dose
    MRSA target attainment. It does not test cure of VRE infection or create a new
    approval. Simulated MIC coverage is not a new measured isolate MIC, and human
    metabolism is not a microbial target. The authors acknowledge small sample size,
    single-dose design and unmeasured unbound concentration.
  snapshot_sha256: 5c25eef86a1ad8cc317af4307f76073e95cab4a8d7d11c083b762bc805943951
- evidence_id: regulator
  kind: authority
  reference: https://mpa.xinjiang.gov.cn/xjyjj/gjjdt/202106/70d2a6e9db6c4d8ab11e737b2d0ad9bc.shtml
  locator: Complete June 2, 2021 NMPA announcement reproduced by the Xinjiang drug
    regulator, explicitly credited to NMPA.
  accessed_at: '2026-10-21T13:43:49Z'
  support: refutes
  summary: The approved tablet indication is complicated skin and soft tissue infection
    caused by susceptible S. aureus, including methicillin-sensitive/resistant strains,
    S. pyogenes or S. agalactiae. The announcement does not list VRE. It supports
    a dated Chinese product indication, not unrestricted approval for the full laboratory
    spectrum.
  snapshot_sha256: 66c70e4a950ef76bb39004bed96beca3ee8699fce8bcd3f40a76841cda744efe
- evidence_id: nhsa
  kind: authority
  reference: https://www.nhsa.gov.cn/attach/Ypsn2025/YPSN202500200/YPSN202500200.pdf
  locator: 'Manufacturer public reimbursement submission dated July 19, 2025, pp2–3:
    all labeled indications and initial approval date.'
  accessed_at: '2026-10-21T13:43:49Z'
  support: supports
  summary: The government-hosted manufacturer filing gives the same three-pathogen
    cSSTI indication, identifies 400 mg tablets and states initial approval June 1,
    2021. It expressly notes that approved indications remain limited to cSSTI. This
    is an applicant disclosure hosted by NHSA, not an independent new NMPA approval
    decision. The full linked legal label was not obtained.
  snapshot_sha256: 3e2ccd4cd90eabba25c77fed4b275d791b78626236dc2b59544551f2d15a030f
- evidence_id: manufacturer
  kind: authority
  reference: https://www.micurxchina.com/678.html
  locator: Complete June 2, 2021 manufacturer approval announcement.
  accessed_at: '2026-10-21T13:43:25Z'
  support: supports
  summary: MicuRx reports the Chinese cSSTI approval and distinguishes it from the
    broad development program against resistant Gram-positive organisms. The same
    dated announcement calls FDA QIDP/Fast Track designations and US phase II development
    distinct from future approvals. These historical statements are not an exhaustive
    current worldwide regulatory census.
  snapshot_sha256: 11e99251af341ec3a2eec97f404a24b4b9d0fd5c68f44cf41aa65e752986f129
- evidence_id: susceptibility
  kind: primary_source
  reference: PMID:32778552; DOI:10.1128/AAC.01195-20
  locator: Complete original indexed abstract; full article attempts returned XML
    500, PMC challenge and inaccessible publisher/EuropePMC routes.
  accessed_at: '2026-10-21T13:43:25Z'
  support: supports
  summary: In a collection of 1,211 clinical Gram-positive isolates, contezolid inhibited
    all tested MRSA and vancomycin-resistant E. faecium isolates at ≤1 mg/L. This
    directly supports bounded laboratory activity. It does not establish an approved
    VRE indication, species-wide susceptibility or the exact bulk salt of every tested
    lot. Full methods, isolate-level tables and chemical-material certification were
    not inspected.
  snapshot_sha256: 64fe0fa697bb9f608bfae88f2af40fdbce474dabc8bd1a0d77dbef60bb0db311
- evidence_id: mechanism-context
  kind: database
  reference: PMID:24694071; DOI:10.1021/jm401931e; ARO:3000079
  locator: Complete original indexed abstract of the 2014 medicinal-chemistry annotation/review
    and the official class definition.
  accessed_at: '2026-10-21T13:46:20Z'
  support: context_only
  summary: The annotation identifies the S-configured MRX-I compound and summarizes
    protein-synthesis-inhibitor class development. It is labeled a review and was
    not inspected as a direct ribosomal binding experiment. The bounded search did
    not supply an independently read contezolid-specific structural binding assay.
    No direct-binding edge is inferred from the parent class or human PK study.
- evidence_id: adapter
  kind: database
  reference: Structured source applicability assessment
  locator: Native fields and actual maintained rows inspected before web research.
  accessed_at: '2026-10-21T13:46:20Z'
  support: context_only
  summary: The native record has no gene, protein, pathway, stress-response or transcriptomic
    claim. MRSA/VRE are phenotype descriptions here. Structured iModulonDB follow-up
    is not applicable to verifying this chemical identity or the approved indication;
    class-level ribosome language is not silently promoted into a native target.
- evidence_id: search
  kind: search
  reference: 324-inclusive-hits.txt;324-literature.json;324-lab-original.json
  locator: Ignored-inclusive local exact-name/identifier/key search and bounded public
    official/citation research.
  accessed_at: '2026-10-21T13:46:20Z'
  support: context_only
  summary: The exact record, source rows and generated context were found. No exact
    maintained override or curator evidence overlay occurred in the searched local
    scope. Public official sources resolve the approval boundary; broad MRX-I searches
    also return unrelated MRX compounds, which are excluded. An unsuccessful manufacturer-label
    download and full-article access attempts remain explicit limits.
  snapshot_sha256: 8168e914be141672d7fe0e274ea3cf037240021ce4e2347dc7adf36958abf665
  search_scope: 2026-10-21; rg --no-ignore --hidden for ARO:3007474, contezolid and
    full key across data, curation, conf, scripts, src, docs, .claude, reviews and
    reports. EuropePMC exact PMID 36992830, TITLE_ABS:contezolid and TITLE_ABS:MRX-I;
    bounded Chinese NMPA/manufacturer indication and label searches, original susceptibility
    DOI/PMID and public full-text routes.
- evidence_id: validation
  kind: validation
  reference: 324-schema.log;324-strict.log;324-chemistry.json;324-xref-chemistry.json
  locator: Actual focused deterministic checks and final captured-input comparison.
  accessed_at: '2026-10-21T13:46:20Z'
  support: supports
  summary: All focused checks exit 0 and all sixteen input hashes remain unchanged,
    including the original thirteen. The raw ARO definition reproduces native, so
    the wording correction belongs to maintained source/override handling.
  snapshot_sha256: d7c67e6cc9ae2a502a3ef0f19c757a8a17c0cad412cc1fd231a05a8f8cc5081f
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral S-configured active compound and source mint
  outcome: supported
  summary: Native and official encodings, masses, charge, formula and mint agree.
    Contezolid is distinguished from its prodrug and metabolites.
  target_ids:
  - antibioticmech:aro-ca0e85f42a
  evidence_ids:
  - native
  - identity
  - owners
  - validation
- assessment_id: clinical
  area: evidence
  topic: Approved indication versus resistant-organism activity
  outcome: concern
  summary: The definition compresses separate approval and spectrum statements. Dated
    Chinese sources support a specific cSSTI indication; the primary PK paper explicitly
    preserves that boundary. Qualify the sentence without denying experimentally supported
    VRE activity.
  target_ids:
  - antibioticmech:aro-ca0e85f42a
  evidence_ids:
  - adopted-primary
  - regulator
  - nhsa
  - manufacturer
  - susceptibility
- assessment_id: activity
  area: evidence
  topic: Antibacterial filing and oxazolidinone classification
  outcome: supported
  summary: The exact chemical class and compound-specific susceptibility evidence
    support ANTIBACTERIAL filing. No quantitative native activity claim requires correction.
    Laboratory activity and an authorized clinical indication remain separate.
  target_ids:
  - antibioticmech:aro-ca0e85f42a
  evidence_ids:
  - class
  - susceptibility
  - identity
- assessment_id: mechanism
  area: evidence
  topic: Optional mechanism and evidence depth
  outcome: unknown
  summary: No native target or mechanistic edge is present. A compound-specific primary
    mechanism follow-up would be required before direct binding curation; the PK study,
    regulatory summary and general parent class do not independently establish such
    a measurement.
  target_ids:
  - antibioticmech:aro-ca0e85f42a
  evidence_ids:
  - adopted-primary
  - mechanism-context
  - class
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Actual maintained ownership and historical capture
  outcome: supported
  summary: ARO and PubChem enrichment owners were appended before assessment while
    preserving the thirteen original hashes. Source definition, xrefs, structure/date,
    minted grounding and three seed-history events reconcile.
  target_ids:
  - antibioticmech:aro-ca0e85f42a
  evidence_ids:
  - owners
  - identity
  - validation
  - search
findings:
- finding_id: F1
  issue_key: contezolid-approval-spectrum-definition-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Separate the approved Chinese indication from the broader laboratory spectrum
  description: The definition says contezolid is newly approved for MDR Gram-positive
    infections, including VRE, without jurisdiction, date or indication. Its cited
    paper distinguishes 2021 Chinese cSSTI approval from in vitro activity. Official
    and manufacturer sources confirm the bounded indication. Rewrite the approval
    clause with China, 2021 and cSSTI, and present resistant-organism activity separately
    with appropriate evidence. Do not interpret this as lack of VRE activity or as
    an exhaustive determination of all countries and later indications.
  target_ids:
  - antibioticmech:aro-ca0e85f42a
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - native
  - owners
  - adopted-primary
  - regulator
  - nhsa
  - susceptibility
  rule_id: 'native-review-checklist: Clinical status and narrowest claim-level evidence;
    docs/CURATION.md'
  native_severity: minor
  normalization_reason: Bounded wording/provenance correction to a genuine approval
    and supported antibacterial spectrum. Identity is sound and no structured clinical-status
    assertion is present; the finding does not allege general therapeutic inefficacy.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition and definition reference
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO definition extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated definition
actions:
- action_id: A1
  description: Qualify the maintained definition and preserve the distinction between
    product authorization and antibacterial spectrum.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-ca0e85f42a
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition and definition reference
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO definition extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated definition
  acceptance_checks:
  - Use dated, jurisdiction-specific language for the Chinese cSSTI approval and retain
    the approved pathogen scope when describing the label. Replace the relative term
    newly with an actual date.
  - State VRE and other resistant-organism activity separately at the scope supported
    by the original experiments. Do not present laboratory susceptibility as an authorized
    indication.
  - Keep PMID 36992830 accurately characterized as a small human PK/modeling study,
    with separate official approval provenance. Rerun source generation and focused
    validation after an authorized maintained-source correction.
- action_id: A2
  description: Optionally add exact-material primary activity or mechanism evidence
    without transferring adjacent compound claims.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-ca0e85f42a
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/contezolid.yaml
    role: Curator-owned primary evidence additions
  acceptance_checks:
  - Read complete original susceptibility methods and tables before importing measurements,
    assay conditions or breakpoints. Preserve population endpoints and distinguish
    contezolid from MRX-4 and its metabolites.
  - Require compound-specific direct evidence for any direct ribosomal binding claim.
    Keep human metabolism and modeled PK/PD target attainment separate from microbial
    molecular targets and measured susceptibility.
limitations:
- The sole adopted PMID 36992830 was read completely in main XML scope, including
  tables and figure captions; supplements, raw data and figure images were not independently
  reprocessed. The study measured single-dose PK in twelve participants and simulated
  efficacy-related targets; it did not directly test VRE clinical outcomes.
- PMID 32778552 was read at complete original-abstract depth. EuropePMC XML returned
  500, PMC requests returned challenge HTML, and public publisher/EuropePMC full-text
  routes failed. Its methods, numerical tables and exact test-material certificate
  were not inspected.
- The 2025 NHSA-hosted manufacturer disclosure was read for the relevant labeled-indication
  and approval-date sections, not as a full reassessment of clinical, economic or
  safety claims. The direct manufacturer label link timed out; no inaccessible label
  content is claimed read.
- The bounded regulatory audit establishes the Chinese source wording conflict; it
  does not exhaustively determine current approval or marketing status worldwide.
  A 2021 announcement is explicitly historical.
- Primary mechanism evidence remains a follow-up opportunity. Optional absent activity,
  mechanism, resistance, producer and clinical-status fields are not additional defects;
  no clinical recommendation is made.
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
