# Ceftiolene: invalid imported aromatic SMILES with independently resolved identity

- Review: 20261021T121420Z-ceftiolene-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:49:14Z
- Finished UTC: 2026-10-21T12:14:20Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One blocker and one minor finding: the imported SMILES omits the triazinone N-H notation and cannot be sanitized, while an exact synonym has a carboxylic-acid spelling error. The native InChI/key, independent databases and original chemical figure resolve the intended ceftiolene structure. Primary antibacterial and cell-wall evidence is retained at its accessible scope.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 260; one exact record in path order, captured before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:140116 | data/antibiotics/antibacterial/ceftiolene.yaml | generated | ceftiolene |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | CHEBI:140116 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:140116 | Actual focused execution exited 0. |
| Focused chemistry verification | failed | False | CHEBI:140116 | Actual focused execution exited 1. |
| Authoritative full QC | failed | True | CHEBI:140116 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:140116 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:140116 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:140116 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:140116 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:140116 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:140116 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:140116 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:140116 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Resolved intended molecule versus invalid representation

identity: concern. Targets: CHEBI:140116.

The exact identity is resolved by native InChI, independent PubChem/ChemSpider and original Fig1. The invalid native SMILES is a representation defect, not uncertainty about which record was reviewed.

### Six synonyms and definition

identity: concern. Targets: CHEBI:140116.

Configuration, scaffold and code42980RP agree with independent sources; the carboxyic typo in synonym index3 requires a bounded correction.

### Antibacterial activity and optional mechanism enrichment

evidence: supported. Targets: CHEBI:140116.

The original activity/PBP and DAP studies support antibacterial function at their accessible abstract scopes; the original analytical study independently clarifies structure. Numerical enrichment requires full methods and form confirmation.

### All four adopted leads

provenance: supported. Targets: CHEBI:140116.

All four adopted PMIDs resolve and were read at the explicitly recorded depths. Review, analytical, bacteriolytic/PBP and DAP evidence are separated.

### Structure class and role scope

grounding: supported. Targets: CHEBI:140116.

Cephalosporin and antibacterial filing/roles fit the resolved structure and original activity evidence.

### Optional fields and status

completeness: supported. Targets: CHEBI:140116.

Missing optional target, resistance, quantitative activity, clinical, producer and graph fields are not findings by themselves. Seed history is not scientific sign-off.

### Immutable capture and reproducible fix

ownership: supported. Targets: CHEBI:140116.

All13 captured input hashes remain unchanged. Both confirmed strings originate in the actual ChEBI inventory row. A future fix needs maintained upstream/extraction/seeding ownership.

### Schema success and chemistry failure

schema: concern. Targets: CHEBI:140116.

Focused schema and strict checks exit0; supplemental chemical parsing exits1 and reveals the blocker. Exact diagnostic success does not erase that failure. Shared required QC outcomes are integrated before save.

## Findings

### F1: Imported aromatic SMILES omits required triazinone N-H

blocker / open / confirmed; issue key: chebi-140116-ceftiolene-invalid-aromatic-nh-smiles.

The aromatic )nnc(=O) segment lacks the explicit [nH] needed to encode the intended neutral triazinone. Native SMILES fails sanitization, despite schema/strict passes. A diagnostic N-H correction exactly reproduces the corroborated native InChI/key; the original chemical figure explicitly shows N-NH.

### F2: Exact systematic synonym contains carboxyic typo

minor / open / confirmed; issue key: chebi-140116-ceftiolene-carboxyic-synonym.

The exact systematic synonym ends carboxyic acid rather than carboxylic acid. The misspelling is inherited from the maintained ChEBI row; correctly spelled independent systematic names support a bounded textual correction.

## Recommended Actions And Acceptance Checks

### A1

Repair the maintained ceftiolene representation and synonym, then reproduce the generated record.

- Use an evidence-backed upstream/extractor/source correction to encode the triazinone N-H and fix carboxyic. Do not hand-edit generated YAML or invent an existing override mechanism.
- Require successful molecular parsing, exact InChI/key agreement, formula/charge agreement and retention of 6R,7R,E-vinyl,Z-oxime geometry. Do not copy the live OLS SMILES uncritically because it omits the Z annotation.
- After separately authorized curation, regenerate through the validated writer/event path; run focused schema/strict, corpus reproduction and relevant chemistry/QC gates. Preserve other source and history fields.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/ceftiolene.yaml; Entire YAML, six synonyms, molecular fields, two chemical and one document links, source concept and four history entries | supports | Read the complete record. The native InChI/key defines 6R,7R ceftiolene with E ethenyl and Z methoxyimino geometry. Its aromatic SMILES has )nnc(=O) in the triazinone segment; synonym index3 ends carboxyic acid. No target, resistance determinant, MIC, clinical object, producer or causal graph is populated. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact CHEBI:140116 row2595, 260-raw-rows.json; captured extraction/seeding inputs | supports | The three-star in-role ChEBI row directly supplies both malformed strings, all molecular fields and four adopted PMID leads. No ARO/PubChem inventory row matches in the complete row scans. Correction must be reproducible through upstream/extraction/maintained source and seeding ownership, not a generated-YAML patch. |
| chemical-failure | RDKit 2026.03.5; 260-focused-stdout.log; 026-root-xref-check.json, entry260 | supports | The actual supplemental native-chemistry command exits1 because MolFromSmiles returns no sanitized molecule: cannot kekulize atoms4,33,34. In the separate reproducible comparison the native InChI parses and reproduces WJXAHFZIHLTPFR-JLRJEBFFSA-N, C20H18N8O8S3 and both R centres. A diagnostic-only replacement of )nnc(=O) with )n[nH]c(=O) parses and reproduces the exact stored InChI and key. No native bytes were edited. An earlier interactive InChI parse failed; that isolated result is not a confirmed InChI defect. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/6537430; 260-pubchem.json and 260-cas-pubchem.json; independently parsed SMILES | supports | CID6537430 and CAS77360-52-2 lookup return the same full native InChI/key and formula. The valid Kekule encoding includes SC4=NNC(=O)C(=O)N4CC=O; explicit N-H occupancy agrees with the proposed diagnostic correction. It preserves E/Z and 6R,7R geometry. This is independent corroboration, not an automatically adopted new xref. |
| chemspider | https://www.chemspider.com/Chemical-Structure.5020599.html; Inspected JSON-LD InChI/InChIKey/formula and exact systematic synonyms | supports | The native exact xref resolves to ceftiolene and reproduces the native full InChI/key and formula. Its systematic synonym correctly spells carboxylic acid. No predicted properties or supplier claims were treated as experiments. |
| chebi | CHEBI:140116; 260-chebi-ols.json and native frozen source row | supports | Current ChEBI retains the intended name, definition and exact mappings. Its currently served SMILES still has the missing aromatic N-H and additionally omits the oxime stereo annotation found in the frozen native record. That additional live-source serialization discrepancy is not a second native finding; a future refresh must preserve the corroborated Z geometry. |
| original-figure | PMID:3733516; DOI:10.7164/antibiotics.39.669; Original pp669–672, especially Fig1 p670 and supplier paragraph p671; 260-figure1-2.png and 260-figure1-3.png visually inspected | supports | The original figure depicts ceftiolene as the free carboxylic acid and explicitly draws the triazinone N-NH, supporting the hydrogen occupancy missing from native SMILES. The study received dry ceftiolene powder from Rhone-Poulenc and tested acidic nitrite color formation. This is structural/analytical evidence, not an MIC assay or producer-organism evidence. |
| analytical-boundary | PMID:3733516; Original Methods and Results pp671–672 | supports | The color assay used aqueous solutions12.5–200 micrograms/mL, citric acid and sodium nitrite, with absorbance measured after1hour. Ceftiolene is listed among positive color-reacting compounds. The plotted quantitative curves described in the text do not include ceftiolene, so a ceftiolene-specific calibration is not inferred. The analytical range is not antibacterial potency. |
| mode-primary | PMID:6394571; DOI:10.1093/jac/14.6.581; 260-core.json, complete original abstract; publisher fulltext access403 and alternative retrieval404 | partial | The original study reports comparative PBP affinity and bacteriolysis for ceftiolene42980RP in E. coli, E. cloacae, P. mirabilis, P. aeruginosa and S. aureus. It distinguishes lysis from routine MIC, examines plasmid beta-lactamases/inoculum effects, and reports organism-specific PBP comparisons. Full strains, reagent form, competition protocol and numerical tables were unavailable; no Kd, exact-form MIC or causal graph is invented. |
| dap-primary | PMID:6739141; 260-core.json, complete original abstract | partial | Original work compared radiolabeled diaminopimelic-acid incorporation in six strains across E. coli, E. cloacae and S. aureus. Concentrations inhibiting90percent incorporation ranged0.1–3timesMIC. This is a cell-wall incorporation endpoint distinct from MIC or direct purified-PBP binding. Full experimental methods and exact reagent form remain uninspected. |
| review-lead | PMID:29017833; DOI:10.1016/j.jaip.2017.08.027; 260-core.json, complete review abstract | context_only | The adopted paper is a general beta-lactam allergy/cross-reactivity review. It is contextual and does not establish a ceftiolene-specific allergy experiment or clinical indication. |
| classification | CHEBI:23066; CHEBI:33281; CHEBI:36047; Native and current ChEBI definition/roles; original antibacterial abstract | supports | Cephalosporin structure and antimicrobial/antibacterial drug roles are consistent with the resolved exact molecule and original antibacterial experiments. Third-generation class wording is not itself a primary-mechanism claim. The roles do not assert current regulatory approval. |
| search | Ignored-inclusive local owner/coverage search; 260-local-hits.txt, 260-owner-hits.txt; bounded public exact-name mechanism search | context_only | Identifier, name, slug and full-key searches included hidden and ignored files outside .git/.venv. The curation/conf/scripts owner search found the readiness lead row but no exact-target correction overlay. The native contains no gene/protein/pathway/stress/expression claims, so the structured expression adapter is not applicable to populated native assertions. Wikipedia is only a contextual compound page; the IUPHAR download was not accepted as usable fulltext. |

## Limits And Additional Notes

- The 1984 PBP/bacteriolysis and DAP studies were inspected at complete abstract depth; full methods, exact bulk forms and numerical results remain unverified. Publisher fulltext retrieval was403 and alternative download404.
- The 1986 original was inspected through Methods/Results pp669–672 and both pages of Fig1; later discussion and references were not comprehensively assessed. Its analytical concentrations are not MICs.
- Current IUPHAR responses were not usable fulltext. CAS is corroborated via PubChem/ChemSpider, not a separately inspected proprietary registry. Wikipedia is contextual only.
- The earlier interactive InChI parse failure was superseded by a reproducible successful InChI parse, while the native SMILES failure persists. No chemical depiction or native field was modified.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T121420Z-ceftiolene-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Ceftiolene: invalid imported aromatic SMILES with independently resolved identity'
started_at: '2026-10-21T11:49:14Z'
finished_at: '2026-10-21T12:14:20Z'
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
summary: 'One blocker and one minor finding: the imported SMILES omits the triazinone
  N-H notation and cannot be sanitized, while an exact synonym has a carboxylic-acid
  spelling error. The native InChI/key, independent databases and original chemical
  figure resolve the intended ceftiolene structure. Primary antibacterial and cell-wall
  evidence is retained at its accessible scope.'
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
  - path: data/antibiotics/antibacterial/ceftiolene.yaml
    sha256: cfb1c9a873e5fe297fbcdfb7b4b8f2fecef7c422433bf625a0acce21bc285091
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
- target_id: CHEBI:140116
  path: data/antibiotics/antibacterial/ceftiolene.yaml
  label: ceftiolene
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
  selection: Initially uncovered queue position 260; one exact record in path order,
    captured before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:140116
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:140116
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/ceftiolene.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:140116
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/ceftiolene.yaml --out /private/tmp/am-review-session/260-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: failed
  required: false
  summary: Actual focused execution exited 1.
  target_ids:
  - CHEBI:140116
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    260
  exit_code: 1
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
  - CHEBI:140116
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
  - CHEBI:140116
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
  - CHEBI:140116
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
  - CHEBI:140116
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
  - CHEBI:140116
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
  - CHEBI:140116
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
  - CHEBI:140116
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
  - CHEBI:140116
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
  - CHEBI:140116
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/ceftiolene.yaml
  locator: Entire YAML, six synonyms, molecular fields, two chemical and one document
    links, source concept and four history entries
  accessed_at: '2026-10-21T12:00:54Z'
  support: supports
  summary: Read the complete record. The native InChI/key defines 6R,7R ceftiolene
    with E ethenyl and Z methoxyimino geometry. Its aromatic SMILES has )nnc(=O) in
    the triazinone segment; synonym index3 ends carboxyic acid. No target, resistance
    determinant, MIC, clinical object, producer or causal graph is populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Exact CHEBI:140116 row2595, 260-raw-rows.json; captured extraction/seeding
    inputs
  accessed_at: '2026-10-21T12:00:54Z'
  support: supports
  summary: The three-star in-role ChEBI row directly supplies both malformed strings,
    all molecular fields and four adopted PMID leads. No ARO/PubChem inventory row
    matches in the complete row scans. Correction must be reproducible through upstream/extraction/maintained
    source and seeding ownership, not a generated-YAML patch.
  snapshot_sha256: 0971ec9ce8f24bbce0ce20d17b920de4fe3ff1387de2c5b889629aa22c496096
- evidence_id: chemical-failure
  kind: validation
  reference: RDKit 2026.03.5
  locator: 260-focused-stdout.log; 026-root-xref-check.json, entry260
  accessed_at: '2026-10-21T12:00:54Z'
  support: supports
  summary: 'The actual supplemental native-chemistry command exits1 because MolFromSmiles
    returns no sanitized molecule: cannot kekulize atoms4,33,34. In the separate reproducible
    comparison the native InChI parses and reproduces WJXAHFZIHLTPFR-JLRJEBFFSA-N,
    C20H18N8O8S3 and both R centres. A diagnostic-only replacement of )nnc(=O) with
    )n[nH]c(=O) parses and reproduces the exact stored InChI and key. No native bytes
    were edited. An earlier interactive InChI parse failed; that isolated result is
    not a confirmed InChI defect.'
  snapshot_sha256: 1643d3834cf071dee6f775eb3cc483fd2876a03dbe21b09c81a07d0fc87fe2a0
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/6537430
  locator: 260-pubchem.json and 260-cas-pubchem.json; independently parsed SMILES
  accessed_at: '2026-10-21T12:00:54Z'
  support: supports
  summary: CID6537430 and CAS77360-52-2 lookup return the same full native InChI/key
    and formula. The valid Kekule encoding includes SC4=NNC(=O)C(=O)N4CC=O; explicit
    N-H occupancy agrees with the proposed diagnostic correction. It preserves E/Z
    and 6R,7R geometry. This is independent corroboration, not an automatically adopted
    new xref.
  snapshot_sha256: 29d62245c9dc65b482bc8ec5744d8c9c0d8548ad54011478089b30f75275a4d5
- evidence_id: chemspider
  kind: database
  reference: https://www.chemspider.com/Chemical-Structure.5020599.html
  locator: Inspected JSON-LD InChI/InChIKey/formula and exact systematic synonyms
  accessed_at: '2026-10-21T12:00:54Z'
  support: supports
  summary: The native exact xref resolves to ceftiolene and reproduces the native
    full InChI/key and formula. Its systematic synonym correctly spells carboxylic
    acid. No predicted properties or supplier claims were treated as experiments.
  snapshot_sha256: b6e2136a22cbbbfe325ba2adbb0c548700ee0b61c61528bf2c82a6ceedf2f289
- evidence_id: chebi
  kind: database
  reference: CHEBI:140116
  locator: 260-chebi-ols.json and native frozen source row
  accessed_at: '2026-10-21T12:00:54Z'
  support: supports
  summary: Current ChEBI retains the intended name, definition and exact mappings.
    Its currently served SMILES still has the missing aromatic N-H and additionally
    omits the oxime stereo annotation found in the frozen native record. That additional
    live-source serialization discrepancy is not a second native finding; a future
    refresh must preserve the corroborated Z geometry.
  snapshot_sha256: 87c665ba43bb3a627c82c1edbf4b9274cd0850543b611b942e8b2da9d14d7267
- evidence_id: original-figure
  kind: primary_source
  reference: PMID:3733516; DOI:10.7164/antibiotics.39.669
  locator: Original pp669–672, especially Fig1 p670 and supplier paragraph p671; 260-figure1-2.png
    and 260-figure1-3.png visually inspected
  accessed_at: '2026-10-21T12:00:54Z'
  support: supports
  summary: The original figure depicts ceftiolene as the free carboxylic acid and
    explicitly draws the triazinone N-NH, supporting the hydrogen occupancy missing
    from native SMILES. The study received dry ceftiolene powder from Rhone-Poulenc
    and tested acidic nitrite color formation. This is structural/analytical evidence,
    not an MIC assay or producer-organism evidence.
  snapshot_sha256: ff60a1dcf9f1a6ddf009f0d3e0a12dd70416f4babc554ccba03a5509f4d41519
- evidence_id: analytical-boundary
  kind: primary_source
  reference: PMID:3733516
  locator: Original Methods and Results pp671–672
  accessed_at: '2026-10-21T12:00:54Z'
  support: supports
  summary: The color assay used aqueous solutions12.5–200 micrograms/mL, citric acid
    and sodium nitrite, with absorbance measured after1hour. Ceftiolene is listed
    among positive color-reacting compounds. The plotted quantitative curves described
    in the text do not include ceftiolene, so a ceftiolene-specific calibration is
    not inferred. The analytical range is not antibacterial potency.
  snapshot_sha256: ff60a1dcf9f1a6ddf009f0d3e0a12dd70416f4babc554ccba03a5509f4d41519
- evidence_id: mode-primary
  kind: primary_source
  reference: PMID:6394571; DOI:10.1093/jac/14.6.581
  locator: 260-core.json, complete original abstract; publisher fulltext access403
    and alternative retrieval404
  accessed_at: '2026-10-21T12:00:54Z'
  support: partial
  summary: The original study reports comparative PBP affinity and bacteriolysis for
    ceftiolene42980RP in E. coli, E. cloacae, P. mirabilis, P. aeruginosa and S. aureus.
    It distinguishes lysis from routine MIC, examines plasmid beta-lactamases/inoculum
    effects, and reports organism-specific PBP comparisons. Full strains, reagent
    form, competition protocol and numerical tables were unavailable; no Kd, exact-form
    MIC or causal graph is invented.
  snapshot_sha256: 7b2bde81ded20529189d8cbf326a0130463eeaf0aa3fcacc675bc5eaff44649b
- evidence_id: dap-primary
  kind: primary_source
  reference: PMID:6739141
  locator: 260-core.json, complete original abstract
  accessed_at: '2026-10-21T12:00:54Z'
  support: partial
  summary: Original work compared radiolabeled diaminopimelic-acid incorporation in
    six strains across E. coli, E. cloacae and S. aureus. Concentrations inhibiting90percent
    incorporation ranged0.1–3timesMIC. This is a cell-wall incorporation endpoint
    distinct from MIC or direct purified-PBP binding. Full experimental methods and
    exact reagent form remain uninspected.
  snapshot_sha256: 7b2bde81ded20529189d8cbf326a0130463eeaf0aa3fcacc675bc5eaff44649b
- evidence_id: review-lead
  kind: primary_source
  reference: PMID:29017833; DOI:10.1016/j.jaip.2017.08.027
  locator: 260-core.json, complete review abstract
  accessed_at: '2026-10-21T12:00:54Z'
  support: context_only
  summary: The adopted paper is a general beta-lactam allergy/cross-reactivity review.
    It is contextual and does not establish a ceftiolene-specific allergy experiment
    or clinical indication.
  snapshot_sha256: 7b2bde81ded20529189d8cbf326a0130463eeaf0aa3fcacc675bc5eaff44649b
- evidence_id: classification
  kind: authority
  reference: CHEBI:23066; CHEBI:33281; CHEBI:36047
  locator: Native and current ChEBI definition/roles; original antibacterial abstract
  accessed_at: '2026-10-21T12:00:54Z'
  support: supports
  summary: Cephalosporin structure and antimicrobial/antibacterial drug roles are
    consistent with the resolved exact molecule and original antibacterial experiments.
    Third-generation class wording is not itself a primary-mechanism claim. The roles
    do not assert current regulatory approval.
  snapshot_sha256: 87c665ba43bb3a627c82c1edbf4b9274cd0850543b611b942e8b2da9d14d7267
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local owner/coverage search
  locator: 260-local-hits.txt, 260-owner-hits.txt; bounded public exact-name mechanism
    search
  accessed_at: '2026-10-21T12:00:54Z'
  support: context_only
  summary: Identifier, name, slug and full-key searches included hidden and ignored
    files outside .git/.venv. The curation/conf/scripts owner search found the readiness
    lead row but no exact-target correction overlay. The native contains no gene/protein/pathway/stress/expression
    claims, so the structured expression adapter is not applicable to populated native
    assertions. Wikipedia is only a contextual compound page; the IUPHAR download
    was not accepted as usable fulltext.
  search_scope: rg --no-ignore --hidden over isolated026 checkout outside .git/.venv;
    exact owner search curation/conf/scripts; public primary exact-name query in260-primary-search.json.
  snapshot_sha256: 52c7f91bf94464958de6dfafe255a3f89bca2369fb594f08cf262d2b5fa4864f
assessments:
- assessment_id: identity
  area: identity
  topic: Resolved intended molecule versus invalid representation
  outcome: concern
  summary: The exact identity is resolved by native InChI, independent PubChem/ChemSpider
    and original Fig1. The invalid native SMILES is a representation defect, not uncertainty
    about which record was reviewed.
  target_ids:
  - CHEBI:140116
  evidence_ids:
  - native
  - chemical-failure
  - pubchem
  - chemspider
  - original-figure
- assessment_id: names
  area: identity
  topic: Six synonyms and definition
  outcome: concern
  summary: Configuration, scaffold and code42980RP agree with independent sources;
    the carboxyic typo in synonym index3 requires a bounded correction.
  target_ids:
  - CHEBI:140116
  evidence_ids:
  - native
  - owners
  - chemspider
- assessment_id: activity
  area: evidence
  topic: Antibacterial activity and optional mechanism enrichment
  outcome: supported
  summary: The original activity/PBP and DAP studies support antibacterial function
    at their accessible abstract scopes; the original analytical study independently
    clarifies structure. Numerical enrichment requires full methods and form confirmation.
  target_ids:
  - CHEBI:140116
  evidence_ids:
  - mode-primary
  - dap-primary
  - original-figure
  - analytical-boundary
- assessment_id: citations
  area: provenance
  topic: All four adopted leads
  outcome: supported
  summary: All four adopted PMIDs resolve and were read at the explicitly recorded
    depths. Review, analytical, bacteriolytic/PBP and DAP evidence are separated.
  target_ids:
  - CHEBI:140116
  evidence_ids:
  - owners
  - mode-primary
  - dap-primary
  - review-lead
  - analytical-boundary
- assessment_id: classification
  area: grounding
  topic: Structure class and role scope
  outcome: supported
  summary: Cephalosporin and antibacterial filing/roles fit the resolved structure
    and original activity evidence.
  target_ids:
  - CHEBI:140116
  evidence_ids:
  - classification
  - mode-primary
- assessment_id: completeness
  area: completeness
  topic: Optional fields and status
  outcome: supported
  summary: Missing optional target, resistance, quantitative activity, clinical, producer
    and graph fields are not findings by themselves. Seed history is not scientific
    sign-off.
  target_ids:
  - CHEBI:140116
  evidence_ids:
  - native
  - mode-primary
  - dap-primary
- assessment_id: provenance
  area: ownership
  topic: Immutable capture and reproducible fix
  outcome: supported
  summary: All13 captured input hashes remain unchanged. Both confirmed strings originate
    in the actual ChEBI inventory row. A future fix needs maintained upstream/extraction/seeding
    ownership.
  target_ids:
  - CHEBI:140116
  evidence_ids:
  - owners
  - search
- assessment_id: checks
  area: schema
  topic: Schema success and chemistry failure
  outcome: concern
  summary: Focused schema and strict checks exit0; supplemental chemical parsing exits1
    and reveals the blocker. Exact diagnostic success does not erase that failure.
    Shared required QC outcomes are integrated before save.
  target_ids:
  - CHEBI:140116
  evidence_ids:
  - chemical-failure
  - native
findings:
- finding_id: F1
  issue_key: chebi-140116-ceftiolene-invalid-aromatic-nh-smiles
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Imported aromatic SMILES omits required triazinone N-H
  description: The aromatic )nnc(=O) segment lacks the explicit [nH] needed to encode
    the intended neutral triazinone. Native SMILES fails sanitization, despite schema/strict
    passes. A diagnostic N-H correction exactly reproduces the corroborated native
    InChI/key; the original chemical figure explicitly shows N-NH.
  target_ids:
  - CHEBI:140116
  field_paths:
  - chemical_structure.smiles
  evidence_ids:
  - native
  - owners
  - chemical-failure
  - pubchem
  - original-figure
  rule_id: docs/record-reviews.md:Verdict And Severity
  native_severity: blocker
  normalization_reason: Invalid molecular representation is explicitly blocker severity
    even though the intended molecule is independently resolved.
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
- finding_id: F2
  issue_key: chebi-140116-ceftiolene-carboxyic-synonym
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Exact systematic synonym contains carboxyic typo
  description: The exact systematic synonym ends carboxyic acid rather than carboxylic
    acid. The misspelling is inherited from the maintained ChEBI row; correctly spelled
    independent systematic names support a bounded textual correction.
  target_ids:
  - CHEBI:140116
  field_paths:
  - synonyms[3].synonym_text
  evidence_ids:
  - native
  - owners
  - chemspider
  rule_id: docs/record-reviews.md:Verdict And Severity
  native_severity: minor
  normalization_reason: Bounded nonblocking spelling error; it does not change the
    independently resolved molecule.
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
actions:
- action_id: A1
  description: Repair the maintained ceftiolene representation and synonym, then reproduce
    the generated record.
  finding_ids:
  - F1
  - F2
  target_ids:
  - CHEBI:140116
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
  acceptance_checks:
  - Use an evidence-backed upstream/extractor/source correction to encode the triazinone
    N-H and fix carboxyic. Do not hand-edit generated YAML or invent an existing override
    mechanism.
  - Require successful molecular parsing, exact InChI/key agreement, formula/charge
    agreement and retention of 6R,7R,E-vinyl,Z-oxime geometry. Do not copy the live
    OLS SMILES uncritically because it omits the Z annotation.
  - After separately authorized curation, regenerate through the validated writer/event
    path; run focused schema/strict, corpus reproduction and relevant chemistry/QC
    gates. Preserve other source and history fields.
limitations:
- The 1984 PBP/bacteriolysis and DAP studies were inspected at complete abstract depth;
  full methods, exact bulk forms and numerical results remain unverified. Publisher
  fulltext retrieval was403 and alternative download404.
- The 1986 original was inspected through Methods/Results pp669–672 and both pages
  of Fig1; later discussion and references were not comprehensively assessed. Its
  analytical concentrations are not MICs.
- Current IUPHAR responses were not usable fulltext. CAS is corroborated via PubChem/ChemSpider,
  not a separately inspected proprietary registry. Wikipedia is contextual only.
- The earlier interactive InChI parse failure was superseded by a reproducible successful
  InChI parse, while the native SMILES failure persists. No chemical depiction or
  native field was modified.
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
