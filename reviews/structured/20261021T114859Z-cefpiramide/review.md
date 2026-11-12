# Cefpiramide: coherent exact identity with bounded primary and patent evidence

- Review: 20261021T114859Z-cefpiramide
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:39:19Z
- Finished UTC: 2026-10-21T11:48:59Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No confirmed native defect. The neutral cefpiramide structure, three assigned stereocentres, source mints and current PubChem/ChEMBL identities agree. Additional primary abstracts support broad antibacterial activity, while one explicitly assays the sodium preparation. The ARO-adopted cefodizime paper is an unrelated discovery lead and is not used as cefpiramide evidence. A new MtrA paper remains an abstract-level follow-up with unresolved material and binding-unit details. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record review of exact neutral cefpiramide.

Selection: Queue 242 in isolated batch 025; original captures preserved and actual ARO owner appended before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:59213 | data/antibiotics/antibacterial/cefpiramide.yaml | generated | cefpiramide |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:59213 | Actual focused command passed with zero errors. |
| Focused strict | passed | True | CHEBI:59213 | Actual focused command passed with zero errors. |
| Supplemental molecular encodings and source mints | passed | False | CHEBI:59213 | Both encodings reproduce the complete key, formula, charge, masses and three R stereocentres; both source mints agree. |
| Authoritative full QC | failed | True | CHEBI:59213 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:59213 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:59213 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:59213 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:59213 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:59213 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:59213 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:59213 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:59213 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral cefpiramide

identity: supported. Targets: CHEBI:59213.

Names, definition, graph, formula, masses, charge, three R centres, complete keys and source mints agree. PubChem keto/enol naming does not establish a distinct chemical identity.

### Parents, class and roles

grounding: supported. Targets: CHEBI:59213.

Cephalosporin/carboxylic-acid parents and ARO third-generation class match. Original cefpiramide/SM-1652 abstracts support antibacterial identity with sodium-material and strain boundaries.

### Typed drug and document mappings

grounding: unknown. Targets: CHEBI:59213.

Exact accessible structure xrefs agree; KEGG/DrugCentral are appropriate drug-level mappings. Patents are relevant series documents but exact individual examples are incompletely mapped. DrugBank and independent proprietary Beilstein details remain inaccessible/uninspected.

### Both adopted PMID dispositions

evidence: supported. Targets: CHEBI:59213.

Cefodizime activity is excluded; allergy review is contextual. Neither becomes blanket record-level support. The source lead mismatch warrants optional upstream bibliography adjudication, not a fabricated native assay finding.

### Broad antibacterial definition and optional assay enrichment

evidence: supported. Targets: CHEBI:59213.

Original abstracts support broad activity while documenting species-dependent resistance and sodium formulation. No exact neutral-form numeric activity observation is curated from abstract-only evidence.

### Optional MtrA/RegX3 lead

evidence: unknown. Targets: CHEBI:59213.

No native molecular claim exists. The new primary abstract is promising but material, constructs and printed Kb units require full source adjudication; docking against five proteins cannot establish binding to all five.

### Structured expression-source applicability

scope: not_applicable. Targets: CHEBI:59213.

Native record names no gene, protein, regulator, pathway, stress response or transcriptomics dataset. The newly located abstract is retained as a lead, not promoted into a native assertion.

### Clinical, resistance, producer, dataset and graph fields

scope: not_applicable. Targets: CHEBI:59213.

No populated native assertions in these optional domains. MIC and drug database context do not imply approved clinical use, producer or causal graph.

### Actual ownership and history

provenance: supported. Targets: CHEBI:59213.

Both raw owners and source mints are traceable; four history events and original captures preserved. Scientific status remains SEEDED.

### Optional enrichment

completeness: supported. Targets: CHEBI:59213.

No mandatory representation defect established. Additional activity, material and mechanism work is optional and must use claim-specific primary evidence.

### Focused native gates

schema: supported. Targets: CHEBI:59213.

Schema, strict and supplemental chemistry/mint checks pass.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally curate exact-material primary activity and mechanism evidence after resolving full-text limits.

- Inspect original methods and identify neutral acid versus sodium reagent and concentration basis before adding strain-level observations.
- For the 2026 MtrA study, inspect constructs, controls, binding-model units and material; preserve the distinction between docking, MtrA/RegX3 measured binding and H37Rv growth. Do not convert printed Kb to Kd without justification.
- Attach evidence narrowly, then run applicable schema, strict, term, reference, history and corpus gates.

### A2

Optionally adjudicate the unrelated ARO discovery lead and complete patent example mapping.

- Do not use cefodizime PMID 6275785 as cefpiramide evidence. If bibliographic ownership is repaired upstream or through a supported maintained source route, retain provenance and verify regeneration.
- Map exact methylpyridine, R side chain, cephem stereochemistry and preparation form before using any patent example or quantitative result.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cefpiramide.yaml; Entire YAML | supports | Read identifier, seeded/exact status, structural definition, four synonyms, three parents, two roles, full structure, five exact xrefs, three drug and four document xrefs, both source concepts and four history events. No native assay, target, mode, resistance, clinical, producer, dataset or graph claims. |
| owners | data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv; Entire matched ChEBI row 1028 and ARO row 579 | supports | ChEBI owns identity, structure, roles, document mappings and allergy review lead. ARO owns class and an adopted cefodizime paper. Both inventory leads were inspected; raw discovery leads are not claim-level native evidence. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity, Equivalence, Evidence standard and generated ownership | supports | Exact compounds and material scope must be preserved. Optional missing evidence objects alone are not native defects. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:59213; Current structure, definition, synonyms, parents and roles | supports | Current entry reproduces native cefpiramide graph, 6R,7R core and R side chain, neutral acid formula and masses. Cephalosporin and carboxylic-acid parents fit; additional live annotations do not force optional native expansion. |
| chemistry | RDKit 2026.03.5 molecular checks; 242-chemistry.json | supports | Both encodings reproduce PWAUCHMQEXVFJR-PMAPCBKXSA-N, C25H24N8O7S2, one fragment, net charge zero, masses and three R stereocentres. Both ARO/ChEBI mints agree. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/636405/JSON; Complete current molecular identity | supports | CID 636405 has the same complete Standard InChIKey and formula. Its preferred 4-oxo-1H-pyridine name is a tautomeric representation of the native 4-hydroxypyridine structure; no distinct-isomer finding is established. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL1201204.json; Complete current molecule | supports | CHEMBL1201204 reproduces native full key and stereochemical enol SMILES. |
| cas | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/70797-11-4/JSON; CAS lookup | supports | CAS 70797-11-4 resolves the same neutral cefpiramide CID 636405. |
| aro | https://card.mcmaster.ca/aro/3009120; Current molecular identity, class and publication | partial | ARO resolves cefpiramide with matching canonical stereochemical structure and third-generation class. Its displayed PMID 6275785 title explicitly concerns cefodizime, so it is not evidence for this exact compound. |
| kegg | https://rest.kegg.jp/get/D03428; Drug identity and class | supports | D03428 resolves cefpiramide USP/INN with matching formula and third-generation class. Generic PBP/cell-wall drug context does not establish a primary direct-binding experiment. |
| drugcentral | https://drugcentral.org/drugcard/552; Identity and aliases | supports | DrugCentral 552 names cefpiramide with matching CAS, formula and mass; its sodium alias demonstrates drug-level aggregation. This drug_xref is not treated as exact salt equivalence. |
| adopted-6275785 | PMID:6275785; DOI 10.1128/AAC.20.6.760; complete inspected abstract | context_only | The original paper evaluates cefodizime (HR 221), with cefotaxime/ceftizoxime comparators. It provides no inspected exact-cefpiramide result. This mismatched ARO discovery lead is explicitly excluded from support for cefpiramide; no native claim-level evidence object cites it. |
| adopted-29017833 | PMID:29017833; DOI 10.1016/j.jaip.2017.08.027; inspected abstract | context_only | A review of beta-lactam allergy and side-chain cross-reactivity. Context only, not original cefpiramide antibacterial or target evidence. |
| primary-6983860 | PMID:6983860; DOI 10.1128/AAC.22.5.721; complete abstract | partial | Original SM-1652 study reports broad in vitro activity, Pseudomonas/nonfermenter comparisons and mouse protection. Beta-lactamase stability varies by enzyme. The abstract does not resolve the exact isolated formulation or all assay methods; it supports antibacterial identity without neutral-form quantitative transfer. |
| primary-6601470 | PMID:6601470; DOI 10.1128/AAC.23.2.195; complete abstract | partial | Original SM-1652 study explicitly names the sodium salt of the cefpiramide structure, establishing the code-to-moiety mapping. It reports broad activity including a panel of 200 clinical P. aeruginosa isolates. Salt and protocol boundaries preclude assigning numerical results directly to the neutral acid. |
| primary-3943292 | PMID:3943292; DOI 10.1016/0732-8893(86)90060-X; complete abstract | partial | Original study evaluates cefpiramide against 317 Gram-negative isolates by standard microdilution and disk diffusion, including 75 µg disks. The abstract supports panel-specific activity; reagent form and full methods remain uninspected and historical breakpoints are not treated as current. |
| primary-11810540 | PMID:11810540; DOI 10.1007/PL00012156; complete abstract | partial | Agar-dilution survey of 440 Chinese clinical isolates collected in 1998 reports species-dependent cefpiramide activity and resistance. Broad spectrum is not universal susceptibility; precise material and full assay context require full-text inspection. |
| mtra-lead | PMID:42445024; DOI 10.1021/acsmedchemlett.6c00139; complete inspected abstract | partial | 2026 original abstract separates docking against five response regulators from experimental binding reported for MtrA and RegX3. It reports MtrA DNA-binding-domain mutant analysis and H37Rv growth MIC50 4 ± 2.38 µg/mL. Association constants are printed as Kb values in nM^-1, not dissociation constants in nM. Exact reagent form, protein constructs, full binding methodology and these units remain unresolved; this is an optional lead, not a curated native interaction. |
| patent-be | https://patents.google.com/patent/BE833063A/en; Original description and selected claims, especially 4–5 | partial | Relevant N-acylamino-alpha-arylacetamido-cephalosporin chemical series includes hydroxyaryl and methyltetrazolyl substitution. The exact methylpyridine cefpiramide example and salt/stereochemical mapping were not completely resolved; no analogue activity is transferred. English translation is secondary to the original French document. |
| patent-4156724 | https://patents.google.com/patent/US4156724A/en; Description and claims 1–2 | partial | Relevant broad cephalosporin series includes hydroxy-substituted pyridine with optional alkyl, hydroxyaryl and 1-methyltetrazol-5-yl side-chain scope. Free acids, salts and analogues are distinct; an exact individual cefpiramide preparation or assay is not fully mapped. Later legal-event text naming cefpiramide sodium is not original experimental proof. |
| patent-4160087 | https://patents.google.com/patent/US4160087A/en; Description, example 126 and broad claim 1 | partial | Relevant series patent. Inspected example 126 has an unmethylated hydroxypyridine substituent and is an analogue, not exact cefpiramide. Broad ring/alkyl/salt claims do not justify quantitative assay transfer to the native neutral compound. |
| wiki | https://en.wikipedia.org/wiki/Cefpiramide; Document identity | context_only | The named native document resolves to cefpiramide; it is contextual, not primary assay evidence. |
| local-search | Ignored-inclusive native, owner and public literature searches; 242-owner-hits.txt;242-local-hits.txt;242-primary-search.json;242-activity-search.json | context_only | Label, exact ID, source IDs and complete key were searched across isolated batch 025 with ignored/hidden coverage outside .git/.venv. All two adopted PMID abstracts were disposed; additional primary activity and MtrA leads were inspected at abstract level. No exhaustive worldwide literature claim. |
| gates | Focused native checks; 242-focused-results.json | supports | Schema, strict and supplemental molecular/mint checks each exit 0. Scientific material and citation boundaries require the source review above. |

## Limits And Additional Notes

- Primary activity and new MtrA sources were inspected at abstract level. PMC pages returned CAPTCHA, Europe PMC XML/PDF retrieval failed, and the ACS publisher returned 403; no full original methods or tables are claimed.
- The 1983 source explicitly uses sodium SM-1652; exact neutral-acid quantitative assay transfer is unresolved. Broad activity does not establish universal susceptibility or current clinical breakpoints.
- The 2026 abstract prints association constants in nM^-1; full-text verification of units and binding interpretation remains open.
- Patent descriptions and selected claims establish relevant series scope, but not complete exact-compound/example mapping; one inspected example is an unmethylated pyridine analogue.
- DrugBank returned 403; independent Beilstein content was not inspected. Current ChEBI retention alone is not independent validation of every proprietary database detail.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 21 expanded input hashes remain unchanged; original captures preserved. No native/source/status/history edits.
- Focused native checks used batch 025 environment; standalone chemistry used existing batch 019 RDKit 2026.03.5 against batch 025 cwd.
- Only free public sources were retrieved. No optional absence was converted into a finding.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T114859Z-cefpiramide
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefpiramide: coherent exact identity with bounded primary and patent evidence'
started_at: '2026-10-21T11:39:19Z'
finished_at: '2026-10-21T11:48:59Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent entire native and actual ChEBI/ARO owner review;
    current complete molecular comparisons; both adopted PMID abstracts and additional
    original activity abstracts; original patent descriptions and selected claims.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: No confirmed native defect. The neutral cefpiramide structure, three assigned
  stereocentres, source mints and current PubChem/ChEMBL identities agree. Additional
  primary abstracts support broad antibacterial activity, while one explicitly assays
  the sodium preparation. The ARO-adopted cefodizime paper is an unrelated discovery
  lead and is not used as cefpiramide evidence. A new MtrA paper remains an abstract-level
  follow-up with unresolved material and binding-unit details. Scientific assessment
  retains the stated evidence limits; full verification is blocked by the shared native-library
  failure.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
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
  - path: data/antibiotics/antibacterial/cefpiramide.yaml
    sha256: 805f738eb84ae4ca52ea189c4629545e1b08aa5962b955262dad83fb009371db
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
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
- target_id: CHEBI:59213
  path: data/antibiotics/antibacterial/cefpiramide.yaml
  label: cefpiramide
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI identity, structure, definition, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, class, xrefs and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusion overrides
scope:
  description: Whole-record review of exact neutral cefpiramide.
  selection: Queue 242 in isolated batch 025; original captures preserved and actual
    ARO owner appended before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:59213
  exclusions:
  - target: Cefpiramide sodium, cefodizime, patent analogues and unverified quantitative
      target assignments
    reason: Distinct materials or compounds and incompletely inspected experiments
      retain separate scope.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual focused command passed with zero errors.
  target_ids:
  - CHEBI:59213
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefpiramide.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual focused command passed with zero errors.
  target_ids:
  - CHEBI:59213
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefpiramide.yaml --out /private/tmp/am-review-session/242-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Supplemental molecular encodings and source mints
  status: passed
  required: false
  summary: Both encodings reproduce the complete key, formula, charge, masses and
    three R stereocentres; both source mints agree.
  target_ids:
  - CHEBI:59213
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/check199200.py
    242 (cwd /private/tmp/antibioticmech-record-reviews-025)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:59213
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
  - CHEBI:59213
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
  - CHEBI:59213
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
  - CHEBI:59213
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
  - CHEBI:59213
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
  - CHEBI:59213
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
  - CHEBI:59213
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
  - CHEBI:59213
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
  - CHEBI:59213
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cefpiramide.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T11:48:03Z'
  support: supports
  summary: Read identifier, seeded/exact status, structural definition, four synonyms,
    three parents, two roles, full structure, five exact xrefs, three drug and four
    document xrefs, both source concepts and four history events. No native assay,
    target, mode, resistance, clinical, producer, dataset or graph claims.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv
  locator: Entire matched ChEBI row 1028 and ARO row 579
  accessed_at: '2026-10-21T11:48:03Z'
  support: supports
  summary: ChEBI owns identity, structure, roles, document mappings and allergy review
    lead. ARO owns class and an adopted cefodizime paper. Both inventory leads were
    inspected; raw discovery leads are not claim-level native evidence.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity, Equivalence, Evidence standard and generated ownership
  accessed_at: '2026-10-21T11:48:03Z'
  support: supports
  summary: Exact compounds and material scope must be preserved. Optional missing
    evidence objects alone are not native defects.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:59213
  locator: Current structure, definition, synonyms, parents and roles
  accessed_at: '2026-10-21T11:40:07Z'
  support: supports
  summary: Current entry reproduces native cefpiramide graph, 6R,7R core and R side
    chain, neutral acid formula and masses. Cephalosporin and carboxylic-acid parents
    fit; additional live annotations do not force optional native expansion.
  snapshot_sha256: 01da9a16179d413d54e52a0fbb448d9d2f22f1fc49fce690ca1b9cdfb3872af7
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5 molecular checks
  locator: 242-chemistry.json
  accessed_at: '2026-10-21T11:39:53Z'
  support: supports
  summary: Both encodings reproduce PWAUCHMQEXVFJR-PMAPCBKXSA-N, C25H24N8O7S2, one
    fragment, net charge zero, masses and three R stereocentres. Both ARO/ChEBI mints
    agree.
  snapshot_sha256: 4689c6ad243346a96e1fd0b49d5e389c3ea8d19985598e7ef6eecbc9e48780c7
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/636405/JSON
  locator: Complete current molecular identity
  accessed_at: '2026-10-21T11:40:08Z'
  support: supports
  summary: CID 636405 has the same complete Standard InChIKey and formula. Its preferred
    4-oxo-1H-pyridine name is a tautomeric representation of the native 4-hydroxypyridine
    structure; no distinct-isomer finding is established.
  snapshot_sha256: 5117ece7f65efd1a2ef31458a9136fc7efe5610b2083fbe37eab1faa932d1588
- evidence_id: chembl
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL1201204.json
  locator: Complete current molecule
  accessed_at: '2026-10-21T11:40:08Z'
  support: supports
  summary: CHEMBL1201204 reproduces native full key and stereochemical enol SMILES.
  snapshot_sha256: fd442b57da4aacb25eb2fcb854d7a205246af617a7c52a9e15de55664e334ac5
- evidence_id: cas
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/70797-11-4/JSON
  locator: CAS lookup
  accessed_at: '2026-10-21T11:40:08Z'
  support: supports
  summary: CAS 70797-11-4 resolves the same neutral cefpiramide CID 636405.
  snapshot_sha256: 5117ece7f65efd1a2ef31458a9136fc7efe5610b2083fbe37eab1faa932d1588
- evidence_id: aro
  kind: authority
  reference: https://card.mcmaster.ca/aro/3009120
  locator: Current molecular identity, class and publication
  accessed_at: '2026-10-21T11:40:08Z'
  support: partial
  summary: ARO resolves cefpiramide with matching canonical stereochemical structure
    and third-generation class. Its displayed PMID 6275785 title explicitly concerns
    cefodizime, so it is not evidence for this exact compound.
  snapshot_sha256: 2bb1f063e15bff3e1a28d0317d8278d513adaad1463c1f670702a8f12edd2a9d
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/D03428
  locator: Drug identity and class
  accessed_at: '2026-10-21T11:40:09Z'
  support: supports
  summary: D03428 resolves cefpiramide USP/INN with matching formula and third-generation
    class. Generic PBP/cell-wall drug context does not establish a primary direct-binding
    experiment.
  snapshot_sha256: b37f3f64e587d14bad3944d8871e0962941170c6ecf9a054f2afec13fab45c72
- evidence_id: drugcentral
  kind: database
  reference: https://drugcentral.org/drugcard/552
  locator: Identity and aliases
  accessed_at: '2026-10-21T11:40:10Z'
  support: supports
  summary: DrugCentral 552 names cefpiramide with matching CAS, formula and mass;
    its sodium alias demonstrates drug-level aggregation. This drug_xref is not treated
    as exact salt equivalence.
  snapshot_sha256: dc89077f0687c2d019b4ecf0c415f3b7caa316239fcaaa89bc7f52004c96f2e0
- evidence_id: adopted-6275785
  kind: primary_source
  reference: PMID:6275785
  locator: DOI 10.1128/AAC.20.6.760; complete inspected abstract
  accessed_at: '2026-10-21T11:40:09Z'
  support: context_only
  summary: The original paper evaluates cefodizime (HR 221), with cefotaxime/ceftizoxime
    comparators. It provides no inspected exact-cefpiramide result. This mismatched
    ARO discovery lead is explicitly excluded from support for cefpiramide; no native
    claim-level evidence object cites it.
  snapshot_sha256: 0e72ee13d385bf1ac8a28b9ce8c5e2781f66f2ed677e22e28b4f5ff6e742023e
- evidence_id: adopted-29017833
  kind: primary_source
  reference: PMID:29017833
  locator: DOI 10.1016/j.jaip.2017.08.027; inspected abstract
  accessed_at: '2026-10-21T11:40:09Z'
  support: context_only
  summary: A review of beta-lactam allergy and side-chain cross-reactivity. Context
    only, not original cefpiramide antibacterial or target evidence.
  snapshot_sha256: 0e72ee13d385bf1ac8a28b9ce8c5e2781f66f2ed677e22e28b4f5ff6e742023e
- evidence_id: primary-6983860
  kind: primary_source
  reference: PMID:6983860
  locator: DOI 10.1128/AAC.22.5.721; complete abstract
  accessed_at: '2026-10-21T11:41:17Z'
  support: partial
  summary: Original SM-1652 study reports broad in vitro activity, Pseudomonas/nonfermenter
    comparisons and mouse protection. Beta-lactamase stability varies by enzyme. The
    abstract does not resolve the exact isolated formulation or all assay methods;
    it supports antibacterial identity without neutral-form quantitative transfer.
  snapshot_sha256: 2759b572dea824729ae7f30042f1795d3826e305afaa1c22c3724e27e832f03c
- evidence_id: primary-6601470
  kind: primary_source
  reference: PMID:6601470
  locator: DOI 10.1128/AAC.23.2.195; complete abstract
  accessed_at: '2026-10-21T11:41:17Z'
  support: partial
  summary: Original SM-1652 study explicitly names the sodium salt of the cefpiramide
    structure, establishing the code-to-moiety mapping. It reports broad activity
    including a panel of 200 clinical P. aeruginosa isolates. Salt and protocol boundaries
    preclude assigning numerical results directly to the neutral acid.
  snapshot_sha256: 2759b572dea824729ae7f30042f1795d3826e305afaa1c22c3724e27e832f03c
- evidence_id: primary-3943292
  kind: primary_source
  reference: PMID:3943292
  locator: DOI 10.1016/0732-8893(86)90060-X; complete abstract
  accessed_at: '2026-10-21T11:41:17Z'
  support: partial
  summary: Original study evaluates cefpiramide against 317 Gram-negative isolates
    by standard microdilution and disk diffusion, including 75 µg disks. The abstract
    supports panel-specific activity; reagent form and full methods remain uninspected
    and historical breakpoints are not treated as current.
  snapshot_sha256: 2759b572dea824729ae7f30042f1795d3826e305afaa1c22c3724e27e832f03c
- evidence_id: primary-11810540
  kind: primary_source
  reference: PMID:11810540
  locator: DOI 10.1007/PL00012156; complete abstract
  accessed_at: '2026-10-21T11:41:17Z'
  support: partial
  summary: Agar-dilution survey of 440 Chinese clinical isolates collected in 1998
    reports species-dependent cefpiramide activity and resistance. Broad spectrum
    is not universal susceptibility; precise material and full assay context require
    full-text inspection.
  snapshot_sha256: 2759b572dea824729ae7f30042f1795d3826e305afaa1c22c3724e27e832f03c
- evidence_id: mtra-lead
  kind: primary_source
  reference: PMID:42445024
  locator: DOI 10.1021/acsmedchemlett.6c00139; complete inspected abstract
  accessed_at: '2026-10-21T11:40:38Z'
  support: partial
  summary: 2026 original abstract separates docking against five response regulators
    from experimental binding reported for MtrA and RegX3. It reports MtrA DNA-binding-domain
    mutant analysis and H37Rv growth MIC50 4 ± 2.38 µg/mL. Association constants are
    printed as Kb values in nM^-1, not dissociation constants in nM. Exact reagent
    form, protein constructs, full binding methodology and these units remain unresolved;
    this is an optional lead, not a curated native interaction.
  snapshot_sha256: b2beb8e8686b64dd5d06478a65188e806a99714df5ed514af39ea4c9189ff95e
- evidence_id: patent-be
  kind: primary_source
  reference: https://patents.google.com/patent/BE833063A/en
  locator: Original description and selected claims, especially 4–5
  accessed_at: '2026-10-21T11:40:09Z'
  support: partial
  summary: Relevant N-acylamino-alpha-arylacetamido-cephalosporin chemical series
    includes hydroxyaryl and methyltetrazolyl substitution. The exact methylpyridine
    cefpiramide example and salt/stereochemical mapping were not completely resolved;
    no analogue activity is transferred. English translation is secondary to the original
    French document.
  snapshot_sha256: 7550e5a64f1e957071f6b69bb6d6bf6f664753b5cc80de84b256513702e42c66
- evidence_id: patent-4156724
  kind: primary_source
  reference: https://patents.google.com/patent/US4156724A/en
  locator: Description and claims 1–2
  accessed_at: '2026-10-21T11:40:10Z'
  support: partial
  summary: Relevant broad cephalosporin series includes hydroxy-substituted pyridine
    with optional alkyl, hydroxyaryl and 1-methyltetrazol-5-yl side-chain scope. Free
    acids, salts and analogues are distinct; an exact individual cefpiramide preparation
    or assay is not fully mapped. Later legal-event text naming cefpiramide sodium
    is not original experimental proof.
  snapshot_sha256: 4987149f51f7ff3df818e26da1ceab1f7e056427c31fa3100da6f981d8e4ada0
- evidence_id: patent-4160087
  kind: primary_source
  reference: https://patents.google.com/patent/US4160087A/en
  locator: Description, example 126 and broad claim 1
  accessed_at: '2026-10-21T11:40:10Z'
  support: partial
  summary: Relevant series patent. Inspected example 126 has an unmethylated hydroxypyridine
    substituent and is an analogue, not exact cefpiramide. Broad ring/alkyl/salt claims
    do not justify quantitative assay transfer to the native neutral compound.
  snapshot_sha256: bf448c26f232bd848f67025d3a686357f6b7d410008de4d61e5703c91cb42f04
- evidence_id: wiki
  kind: database
  reference: https://en.wikipedia.org/wiki/Cefpiramide
  locator: Document identity
  accessed_at: '2026-10-21T11:40:10Z'
  support: context_only
  summary: The named native document resolves to cefpiramide; it is contextual, not
    primary assay evidence.
  snapshot_sha256: 7601bea8c98d490c258187acc08245e9620092430f0193624f513bc05002066f
- evidence_id: local-search
  kind: search
  reference: Ignored-inclusive native, owner and public literature searches
  locator: 242-owner-hits.txt;242-local-hits.txt;242-primary-search.json;242-activity-search.json
  accessed_at: '2026-10-21T11:39:46Z'
  support: context_only
  summary: Label, exact ID, source IDs and complete key were searched across isolated
    batch 025 with ignored/hidden coverage outside .git/.venv. All two adopted PMID
    abstracts were disposed; additional primary activity and MtrA leads were inspected
    at abstract level. No exhaustive worldwide literature claim.
  snapshot_sha256: 99662bf9fe5d77b7eaf04f1bf73f0a5e540cd2c056bee5472360c35ea78a271a
  search_scope: 2026-10-21; rg --no-ignore --hidden in isolated batch 025 outside
    .git/.venv; current official identities and native patents; both adopted PMID
    abstracts and free Europe PMC primary searches.
- evidence_id: gates
  kind: validation
  reference: Focused native checks
  locator: 242-focused-results.json
  accessed_at: '2026-10-21T11:39:53Z'
  support: supports
  summary: Schema, strict and supplemental molecular/mint checks each exit 0. Scientific
    material and citation boundaries require the source review above.
  snapshot_sha256: 823c2d528f6c819cabaa8746491407050bd81d76c686449ff036becbd0347912
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral cefpiramide
  outcome: supported
  summary: Names, definition, graph, formula, masses, charge, three R centres, complete
    keys and source mints agree. PubChem keto/enol naming does not establish a distinct
    chemical identity.
  target_ids:
  - CHEBI:59213
  evidence_ids:
  - native
  - chebi
  - chemistry
  - pubchem
  - chembl
  - cas
- assessment_id: grounding
  area: grounding
  topic: Parents, class and roles
  outcome: supported
  summary: Cephalosporin/carboxylic-acid parents and ARO third-generation class match.
    Original cefpiramide/SM-1652 abstracts support antibacterial identity with sodium-material
    and strain boundaries.
  target_ids:
  - CHEBI:59213
  evidence_ids:
  - chebi
  - aro
  - primary-6983860
  - primary-6601470
- assessment_id: xrefs
  area: grounding
  topic: Typed drug and document mappings
  outcome: unknown
  summary: Exact accessible structure xrefs agree; KEGG/DrugCentral are appropriate
    drug-level mappings. Patents are relevant series documents but exact individual
    examples are incompletely mapped. DrugBank and independent proprietary Beilstein
    details remain inaccessible/uninspected.
  target_ids:
  - CHEBI:59213
  evidence_ids:
  - pubchem
  - chembl
  - kegg
  - drugcentral
  - patent-be
  - patent-4156724
  - patent-4160087
  - wiki
- assessment_id: adopted
  area: evidence
  topic: Both adopted PMID dispositions
  outcome: supported
  summary: Cefodizime activity is excluded; allergy review is contextual. Neither
    becomes blanket record-level support. The source lead mismatch warrants optional
    upstream bibliography adjudication, not a fabricated native assay finding.
  target_ids:
  - CHEBI:59213
  evidence_ids:
  - owners
  - adopted-6275785
  - adopted-29017833
- assessment_id: activity
  area: evidence
  topic: Broad antibacterial definition and optional assay enrichment
  outcome: supported
  summary: Original abstracts support broad activity while documenting species-dependent
    resistance and sodium formulation. No exact neutral-form numeric activity observation
    is curated from abstract-only evidence.
  target_ids:
  - CHEBI:59213
  evidence_ids:
  - primary-6983860
  - primary-6601470
  - primary-3943292
  - primary-11810540
- assessment_id: mechanism
  area: evidence
  topic: Optional MtrA/RegX3 lead
  outcome: unknown
  summary: No native molecular claim exists. The new primary abstract is promising
    but material, constructs and printed Kb units require full source adjudication;
    docking against five proteins cannot establish binding to all five.
  target_ids:
  - CHEBI:59213
  evidence_ids:
  - native
  - mtra-lead
- assessment_id: adapter
  area: scope
  topic: Structured expression-source applicability
  outcome: not_applicable
  summary: Native record names no gene, protein, regulator, pathway, stress response
    or transcriptomics dataset. The newly located abstract is retained as a lead,
    not promoted into a native assertion.
  target_ids:
  - CHEBI:59213
  evidence_ids:
  - native
  - mtra-lead
- assessment_id: other-fields
  area: scope
  topic: Clinical, resistance, producer, dataset and graph fields
  outcome: not_applicable
  summary: No populated native assertions in these optional domains. MIC and drug
    database context do not imply approved clinical use, producer or causal graph.
  target_ids:
  - CHEBI:59213
  evidence_ids:
  - native
  - kegg
- assessment_id: provenance
  area: provenance
  topic: Actual ownership and history
  outcome: supported
  summary: Both raw owners and source mints are traceable; four history events and
    original captures preserved. Scientific status remains SEEDED.
  target_ids:
  - CHEBI:59213
  evidence_ids:
  - native
  - owners
  - chemistry
- assessment_id: completeness
  area: completeness
  topic: Optional enrichment
  outcome: supported
  summary: No mandatory representation defect established. Additional activity, material
    and mechanism work is optional and must use claim-specific primary evidence.
  target_ids:
  - CHEBI:59213
  evidence_ids:
  - rubric
  - primary-6601470
  - mtra-lead
- assessment_id: schema
  area: schema
  topic: Focused native gates
  outcome: supported
  summary: Schema, strict and supplemental chemistry/mint checks pass.
  target_ids:
  - CHEBI:59213
  evidence_ids:
  - gates
  - chemistry
findings: []
actions:
- action_id: A1
  description: Optionally curate exact-material primary activity and mechanism evidence
    after resolving full-text limits.
  finding_ids: []
  target_ids:
  - CHEBI:59213
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefpiramide.yaml
    role: Curator-owned activity_spectrum and PRIMARY_LITERATURE targets via validated
      writer
  acceptance_checks:
  - Inspect original methods and identify neutral acid versus sodium reagent and concentration
    basis before adding strain-level observations.
  - For the 2026 MtrA study, inspect constructs, controls, binding-model units and
    material; preserve the distinction between docking, MtrA/RegX3 measured binding
    and H37Rv growth. Do not convert printed Kb to Kd without justification.
  - Attach evidence narrowly, then run applicable schema, strict, term, reference,
    history and corpus gates.
- action_id: A2
  description: Optionally adjudicate the unrelated ARO discovery lead and complete
    patent example mapping.
  finding_ids: []
  target_ids:
  - CHEBI:59213
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI identity, structure, definition, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, class, xrefs and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusion overrides
  acceptance_checks:
  - Do not use cefodizime PMID 6275785 as cefpiramide evidence. If bibliographic ownership
    is repaired upstream or through a supported maintained source route, retain provenance
    and verify regeneration.
  - Map exact methylpyridine, R side chain, cephem stereochemistry and preparation
    form before using any patent example or quantitative result.
limitations:
- Primary activity and new MtrA sources were inspected at abstract level. PMC pages
  returned CAPTCHA, Europe PMC XML/PDF retrieval failed, and the ACS publisher returned
  403; no full original methods or tables are claimed.
- The 1983 source explicitly uses sodium SM-1652; exact neutral-acid quantitative
  assay transfer is unresolved. Broad activity does not establish universal susceptibility
  or current clinical breakpoints.
- The 2026 abstract prints association constants in nM^-1; full-text verification
  of units and binding interpretation remains open.
- Patent descriptions and selected claims establish relevant series scope, but not
  complete exact-compound/example mapping; one inspected example is an unmethylated
  pyridine analogue.
- DrugBank returned 403; independent Beilstein content was not inspected. Current
  ChEBI retention alone is not independent validation of every proprietary database
  detail.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 21 expanded input hashes remain unchanged; original captures preserved. No native/source/status/history
  edits.
- Focused native checks used batch 025 environment; standalone chemistry used existing
  batch 019 RDKit 2026.03.5 against batch 025 cwd.
- Only free public sources were retrieved. No optional absence was converted into
  a finding.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:3502
- https://doi.org/10.7164/antibiotics.45.709
- https://www.jstage.jst.go.jp/article/antibiotics1968/45/5/45_5_709/_pdf
tags:
- cefozopran
- chemical-description
- thiadiazole
- primary-activity
```
