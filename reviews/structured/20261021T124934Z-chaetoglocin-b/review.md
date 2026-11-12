# Chaetoglocin B: coherent Z isomer with original antibacterial and producer support

- Review: 20261021T124934Z-chaetoglocin-b
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:36:36Z
- Finished UTC: 2026-10-21T12:49:34Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No substantive correction identified. Chaetoglocin B identity, Z geometry, molecular fields, broader parents and source provenance are coherent. The original paper supports the stated producer and antibacterial role. Full assay detail and the proprietary Reaxys mapping remain bounded access limitations; optional mechanism absence is not treated as an error. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record review of exact chaetoglocin B.

Selection: Queue 284 in isolated batch 029; preserved initial capture and appended review-context owners before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:68767 | data/antibiotics/antibacterial/chaetoglocin-b.yaml | generated | chaetoglocin B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:68767 | Actual focused command exited 0 with no errors. |
| Focused strict | passed | True | CHEBI:68767 | Actual focused command exited 0 with no errors. |
| Independent exact molecular comparison | passed | False | CHEBI:68767 | Native and external encodings, formula, charge, masses, geometry and source mint agree. |
| Authoritative full QC | failed | True | CHEBI:68767 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:68767 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:68767 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:68767 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:68767 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:68767 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:68767 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:68767 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:68767 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact congener, connectivity and geometry

identity: supported. Targets: CHEBI:68767.

The label and systematic synonym denote the native Z isomer. Original Figure 1 and complete current ChEBI/PubChem molecular comparisons agree. A and B remain separate records with distinct complete InChIKeys.

### Parents, antibacterial filing and role

grounding: supported. Targets: CHEBI:68767.

The broader chemical parents fit the molecular graph. Original isolated-compound antibacterial observations support the antibacterial role without claiming all Gram-positive strains are susceptible.

### Sole Reaxys cross-reference

grounding: unknown. Targets: CHEBI:68767.

Current ChEBI repeats Reaxys:22515442, but the proprietary registry record was not independently inspected. No contradictory mapping was found in the inspected public sources.

### Producer and isolation context

evidence: supported. Targets: CHEBI:68767.

The original paper identifies the fungus C. globosum IFB-E036 as the fermentation producer; C. dactylon is its plant host. The native species-level isolation statement preserves that distinction.

### Antibacterial assay scope

evidence: supported. Targets: CHEBI:68767.

The original abstract supports antibacterial activity of compound 2. The 8-32 microgram/mL interval is a joint summary across the measured compounds/organisms, not a single MIC for this record or a strain-independent potency. No native quantitative activity assertion requires correction.

### Optional mode of action and targets

completeness: unknown. Targets: CHEBI:68767.

No native mode of action or target is asserted. The inspected original abstract/preview establishes activity, not an antibacterial molecular target. Chaetoglobosin actin effects and fungal biosynthetic regulation cannot fill that gap.

### Other optional domains and structured adapters

scope: not_applicable. Targets: CHEBI:68767.

No native gene, protein, pathway, stress-response or transcriptomics claim triggers the structured adapter workflow. There are no native resistance, clinical, assay-collection or causal-graph assertions. Optional fields remain unpopulated without constituting a required-field defect.

### Source ownership, history and scientific status

provenance: supported. Targets: CHEBI:68767.

The ChEBI row and extractor/seeder own generated fields. All 13 initial hashes and 21 expanded inputs were preserved and rechecked. SEEDED status, exact grounding and three seed/reseed events remain unchanged. Scientific REVIEWED status is not warranted by schema validity alone.

### Actual focused checks

schema: supported. Targets: CHEBI:68767.

Schema, strict and independent chemical checks pass. Shared corpus checks are outside the focused results recorded here.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally enrich primary producer and antibacterial evidence after recovering the original complete assay methods and table.

- Keep chaetoglocin B / compound 2 separate from the other geometric isomer and chaetoglobosin congeners.
- Preserve exact organism/strain, medium, inoculum, incubation, units, endpoint and isolated-material context before entering numerical MICs.
- Represent C. globosum IFB-E036 as the producer and C. dactylon as the host; do not infer a direct antibacterial target from biosynthetic or crude-extract observations.
- Run native schema, strict, source/reference/history and applicable QC gates after any separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/chaetoglocin-b.yaml; Entire 49-line YAML | supports | Read exact identifier, definition and systematic synonym, both parents, antibacterial role, all chemical fields, sole Reaxys xref, source concept, SEEDED/EXACT state and all three history events. No native protein, pathway, resistance, quantitative activity, clinical, collection or causal-graph claim is populated. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; curation/decisions.tsv; Exact ChEBI row 1727; seeder build_concepts and record assembly | supports | The adopted ChEBI row reproduces this exact Z isomer and contains one citation lead, PMID:20814854. The raw inventory SHA matches MANIFEST.yaml. Seeder source handling explains the ChEBI definition, structure and role fields; raw ChEBI citation leads are not automatically promoted to record evidence. The initial 13 input hashes remain unchanged; 21 expanded hashes were rechecked. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; docs/record-review-profile.md; Identity, source support, producer, activity, optional completeness and status gates | supports | Exact isomers and claim-level evidence are assessed separately. Missing optional enrichment is not a required-field defect. A completed review does not satisfy the checked-mode-of-action requirement for REVIEWED status. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:68767; Complete molecular data, definition, Names, Registry Numbers, species and outgoing relations | supports | Current ChEBI reproduces the Z definition, systematic synonym, full retained InChIKey, formula, neutral charge and both masses. It gives diol/2-pyranone parents, antibacterial role, C. globosum origin citing PMID:20814854, and Reaxys:22515442. ChEBI repetition does not independently verify the proprietary Reaxys entry. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/chaetoglocin%20B/property/InChI,InChIKey,MolecularFormula,CanonicalSMILES,IsomericSMILES,Charge,MolecularWeight/JSON; Name query resolves CID51039178; complete molecular properties | supports | PubChem returns the same complete InChI and InChIKey for chaetoglocin B, with C11H14O5, charge zero and the corresponding Z isomeric SMILES. This is an independent comparison, not an existing native PubChem assertion. |
| chemistry | RDKit 2026.03.5 independent molecular comparison; 284-chemistry.json; 283284-chemistry.py | supports | Native SMILES/InChI and current ChEBI/PubChem encodings all parse and generate the complete retained key. Each has one component, charge zero, no tetrahedral stereocentres and one specified external Z double bond. Formula, average mass 226.228, exact mass 226.084123548 and SHA256-derived source mint agree. |
| parents | https://www.ebi.ac.uk/ols4/ontologies/chebi/classes?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_23824; 283284-term23824.json, term75885.json and term33282.json; exact OLS terms | supports | CHEBI:23824 resolves to diol, CHEBI:75885 to 2-pyranones, and CHEBI:33282 to antibacterial agent. The graph contains two hydroxy groups and a 2-pyranone ring; these parents are broader classes rather than exact synonyms. |
| original | https://doi.org/10.1055/s-0030-1250292; PMID:20814854; complete original abstract, Ge et al., Planta Medica 2011;77:277-280 (online 2010-09-02) | partial | The original abstract maps chaetoglocins A-D to compounds 1-4 and identifies C. globosum IFB-E036 from inside C. dactylon roots as the solid-fermentation source. Compounds 1 and 2 have reported Gram-positive antibacterial MICs spanning 8-32 microgram/mL. This supports the qualitative role and producer statement for chaetoglocin B; the abstract does not assign exact strain-specific values or expose the full assay protocol. |
| original-figure | https://www.thieme-connect.de/media/plantamedica/201103/lookinside/10.1055-s-0030-1250292-1.jpg; Public original p277 preview; Figure 1, Table 1 and isolation/structure text | supports | Visually inspected the full-resolution public preview. Figure 1 maps compound 2 to the native pyranone connectivity and Z side-chain double bond. Table 1 separately reports NMR data for compounds 1 and 2. Page 277 identifies IFB-E036 from C. dactylon in Yancheng and describes fungal solid-substrate cultivation, ethyl-acetate extraction and fractionation. Antibacterial activity of the crude extract is distinguished from the abstract's purified-compound results. The nearby actin-binding discussion concerns chaetoglobosins, not chaetoglocins. |
| access | Public publisher, Europe PMC and OpenAlex retrieval; 283284-fetch.json; 283284-followup-fetch.json; 283284-final-fetch.json | context_only | The full-text/PDF and candidate supplementary routes returned HTML challenge pages, not research PDFs. Europe PMC lists subscription-required access and no full text; OpenAlex lists only publisher and PubMed locations. The public original page-277 preview was retrieved and inspected. No purchase, request-to-author or restricted-access workaround was used. |
| search | Ignored-inclusive repository and bounded primary-source search; 284-local-hits.txt; 283284-focused-local-hits.txt; exact curation/conf query | context_only | The local search included hidden and ignored files outside .git/.venv. Exact target hits in curation/conf were readiness-queue rows, not a target-specific curator override. The sole adopted PMID lead was resolved. Public searches used both exact compound names, the original DOI, structure and antibacterial/mechanism terms; secondary reviews remained discovery leads, not sources for strain-specific MIC transfer. |
| gates | Actual focused schema and strict validation commands; 284-focused-results.json; schema/strict logs | supports | Both focused native validators completed with exit 0 and no errors. These deterministic passes do not independently establish biological evidence. |

## Limits And Additional Notes

- Original PMID:20814854 was inspected through its complete abstract and the public page-277 preview, including Figure 1 and Table 1. Remaining full text, detailed activity table and supporting data were not retrieved; failed PDF/SI routes returned HTML rather than research documents.
- Reaxys registry content was not independently accessible. Current ChEBI corroborates the imported identifier but is not an independent registry check.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native/source/status/history or saved-bundle changes were made. Initial input captures were retained.
- Native validators used the batch 029 environment. RDKit 2026.03.5 used the existing batch 019 interpreter against batch 029 cwd.
- The review does not establish absence of an antibacterial mechanism in the literature; it reports the limits of the inspected sources.
- Optional links and tags were selected and checked specifically for this exact target.
- Root independently read the entire native record and scientific draft, checked all captured hashes, compared chemical diagnostics and visually inspected original page 277 before ordered persistence.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T124934Z-chaetoglocin-b
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Chaetoglocin B: coherent Z isomer with original antibacterial and producer
  support'
started_at: '2026-10-21T12:36:36Z'
finished_at: '2026-10-21T12:49:34Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Entire native and actual source owner read; current complete
    molecular comparisons and original public structure figure independently inspected;
    sole adopted primary citation resolved with explicit access limits.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: No substantive correction identified. Chaetoglocin B identity, Z geometry,
  molecular fields, broader parents and source provenance are coherent. The original
  paper supports the stated producer and antibacterial role. Full assay detail and
  the proprietary Reaxys mapping remain bounded access limitations; optional mechanism
  absence is not treated as an error. Scientific assessment retains the stated evidence
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
  - path: data/antibiotics/antibacterial/chaetoglocin-b.yaml
    sha256: 61f62802fecdc306a232f27a2d355372759e8ba1e3d06de45a9904ce9ac9e00c
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
  - path: CLAUDE.md
    role: context
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
  - path: docs/record-review-profile.md
    role: context
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
  - path: docs/record-reviews.md
    role: context
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
  - path: conf/record_review.yaml
    role: context
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
  - path: .claude/skills/review-yaml-record/SKILL.md
    role: context
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
  - path: schema/record_review.yaml
    role: context
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
  - path: scripts/record_review.py
    role: context
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
  - path: justfile
    role: context
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
targets:
- target_id: CHEBI:68767
  path: data/antibiotics/antibacterial/chaetoglocin-b.yaml
  label: chaetoglocin B
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
  description: Whole-record review of exact chaetoglocin B.
  selection: Queue 284 in isolated batch 029; preserved initial capture and appended
    review-context owners before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:68767
  exclusions:
  - target: Other chaetoglocin congeners, chaetoglobosins and crude fermentation extracts
      as exact assay materials
    reason: Different molecular identities or mixed preparations cannot inherit this
      exact congener identity or endpoint.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual focused command exited 0 with no errors.
  target_ids:
  - CHEBI:68767
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/chaetoglocin-b.yaml (cwd /private/tmp/antibioticmech-record-reviews-029)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual focused command exited 0 with no errors.
  target_ids:
  - CHEBI:68767
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/chaetoglocin-b.yaml --out /private/tmp/am-review-session/284-validation.tsv
    (cwd /private/tmp/antibioticmech-record-reviews-029)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Independent exact molecular comparison
  status: passed
  required: false
  summary: Native and external encodings, formula, charge, masses, geometry and source
    mint agree.
  target_ids:
  - CHEBI:68767
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/283284-chemistry.py
    (cwd /private/tmp/antibioticmech-record-reviews-029)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
  - chebi
  - pubchem
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:68767
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
  - CHEBI:68767
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
  - CHEBI:68767
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
  - CHEBI:68767
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
  - CHEBI:68767
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
  - CHEBI:68767
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
  - CHEBI:68767
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
  - CHEBI:68767
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
  - CHEBI:68767
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/chaetoglocin-b.yaml
  locator: Entire 49-line YAML
  accessed_at: '2026-10-21T12:43:16Z'
  support: supports
  summary: Read exact identifier, definition and systematic synonym, both parents,
    antibacterial role, all chemical fields, sole Reaxys xref, source concept, SEEDED/EXACT
    state and all three history events. No native protein, pathway, resistance, quantitative
    activity, clinical, collection or causal-graph claim is populated.
  snapshot_sha256: 61f62802fecdc306a232f27a2d355372759e8ba1e3d06de45a9904ce9ac9e00c
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py; curation/decisions.tsv
  locator: Exact ChEBI row 1727; seeder build_concepts and record assembly
  accessed_at: '2026-10-21T12:43:16Z'
  support: supports
  summary: The adopted ChEBI row reproduces this exact Z isomer and contains one citation
    lead, PMID:20814854. The raw inventory SHA matches MANIFEST.yaml. Seeder source
    handling explains the ChEBI definition, structure and role fields; raw ChEBI citation
    leads are not automatically promoted to record evidence. The initial 13 input
    hashes remain unchanged; 21 expanded hashes were rechecked.
  snapshot_sha256: 6e4a387121af39696485176e7c122cf913ce1d7e1f6ae375ba49ee27547daca9
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md; docs/record-review-profile.md
  locator: Identity, source support, producer, activity, optional completeness and
    status gates
  accessed_at: '2026-10-21T12:43:16Z'
  support: supports
  summary: Exact isomers and claim-level evidence are assessed separately. Missing
    optional enrichment is not a required-field defect. A completed review does not
    satisfy the checked-mode-of-action requirement for REVIEWED status.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:68767
  locator: Complete molecular data, definition, Names, Registry Numbers, species and
    outgoing relations
  accessed_at: '2026-10-21T12:38:28.496419Z'
  support: supports
  summary: Current ChEBI reproduces the Z definition, systematic synonym, full retained
    InChIKey, formula, neutral charge and both masses. It gives diol/2-pyranone parents,
    antibacterial role, C. globosum origin citing PMID:20814854, and Reaxys:22515442.
    ChEBI repetition does not independently verify the proprietary Reaxys entry.
  snapshot_sha256: 5ca89569ab3d652ddb2d575adadc3176228a6f85ed716b19f039d29a6b61c1fa
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/chaetoglocin%20B/property/InChI,InChIKey,MolecularFormula,CanonicalSMILES,IsomericSMILES,Charge,MolecularWeight/JSON
  locator: Name query resolves CID51039178; complete molecular properties
  accessed_at: '2026-10-21T12:38:29.063289Z'
  support: supports
  summary: PubChem returns the same complete InChI and InChIKey for chaetoglocin B,
    with C11H14O5, charge zero and the corresponding Z isomeric SMILES. This is an
    independent comparison, not an existing native PubChem assertion.
  snapshot_sha256: 71d7d5b2bac57d2e3b7f82f8fe36a0297879a5a6f0cdca7ff67cacd46c4bda51
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5 independent molecular comparison
  locator: 284-chemistry.json; 283284-chemistry.py
  accessed_at: '2026-10-21T12:43:16Z'
  support: supports
  summary: Native SMILES/InChI and current ChEBI/PubChem encodings all parse and generate
    the complete retained key. Each has one component, charge zero, no tetrahedral
    stereocentres and one specified external Z double bond. Formula, average mass
    226.228, exact mass 226.084123548 and SHA256-derived source mint agree.
  snapshot_sha256: 94a0e020cce9cdc1a3a0a39615f1490cbdde5e3810455d758474a39494d0ce86
- evidence_id: parents
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/ontologies/chebi/classes?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_23824
  locator: 283284-term23824.json, term75885.json and term33282.json; exact OLS terms
  accessed_at: '2026-10-21T12:38:29.167262Z'
  support: supports
  summary: CHEBI:23824 resolves to diol, CHEBI:75885 to 2-pyranones, and CHEBI:33282
    to antibacterial agent. The graph contains two hydroxy groups and a 2-pyranone
    ring; these parents are broader classes rather than exact synonyms.
  snapshot_sha256: 7b337528f37346b4e89c7bc960a617ca86bab0b71c9547caef6da62692f39acd
- evidence_id: original
  kind: primary_source
  reference: https://doi.org/10.1055/s-0030-1250292
  locator: PMID:20814854; complete original abstract, Ge et al., Planta Medica 2011;77:277-280
    (online 2010-09-02)
  accessed_at: '2026-10-21T12:38:28.496512Z'
  support: partial
  summary: The original abstract maps chaetoglocins A-D to compounds 1-4 and identifies
    C. globosum IFB-E036 from inside C. dactylon roots as the solid-fermentation source.
    Compounds 1 and 2 have reported Gram-positive antibacterial MICs spanning 8-32
    microgram/mL. This supports the qualitative role and producer statement for chaetoglocin
    B; the abstract does not assign exact strain-specific values or expose the full
    assay protocol.
  snapshot_sha256: a5a65e4a59d8ba91d56218f1b2c515e893dd4056a225d512da984779958626ad
- evidence_id: original-figure
  kind: primary_source
  reference: https://www.thieme-connect.de/media/plantamedica/201103/lookinside/10.1055-s-0030-1250292-1.jpg
  locator: Public original p277 preview; Figure 1, Table 1 and isolation/structure
    text
  accessed_at: '2026-10-21T12:41:32.794763Z'
  support: supports
  summary: Visually inspected the full-resolution public preview. Figure 1 maps compound
    2 to the native pyranone connectivity and Z side-chain double bond. Table 1 separately
    reports NMR data for compounds 1 and 2. Page 277 identifies IFB-E036 from C. dactylon
    in Yancheng and describes fungal solid-substrate cultivation, ethyl-acetate extraction
    and fractionation. Antibacterial activity of the crude extract is distinguished
    from the abstract's purified-compound results. The nearby actin-binding discussion
    concerns chaetoglobosins, not chaetoglocins.
  snapshot_sha256: 231b75ed268cc0d57353bd16452e8f0e16b0c950ce316da08fe183c1e19c4c9d
- evidence_id: access
  kind: search
  reference: Public publisher, Europe PMC and OpenAlex retrieval
  locator: 283284-fetch.json; 283284-followup-fetch.json; 283284-final-fetch.json
  accessed_at: '2026-10-21T12:43:16Z'
  support: context_only
  summary: The full-text/PDF and candidate supplementary routes returned HTML challenge
    pages, not research PDFs. Europe PMC lists subscription-required access and no
    full text; OpenAlex lists only publisher and PubMed locations. The public original
    page-277 preview was retrieved and inspected. No purchase, request-to-author or
    restricted-access workaround was used.
  snapshot_sha256: 48c7156bc0a4c381c1f3901b86294c6fb1b89d05fd6fb105bf6ea5ac681e573d
  search_scope: 2026-10-21; isolated batch 029; hidden/ignored-inclusive repository
    search and free official/primary-source retrieval, with access failures retained.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive repository and bounded primary-source search
  locator: 284-local-hits.txt; 283284-focused-local-hits.txt; exact curation/conf
    query
  accessed_at: '2026-10-21T12:43:16Z'
  support: context_only
  summary: The local search included hidden and ignored files outside .git/.venv.
    Exact target hits in curation/conf were readiness-queue rows, not a target-specific
    curator override. The sole adopted PMID lead was resolved. Public searches used
    both exact compound names, the original DOI, structure and antibacterial/mechanism
    terms; secondary reviews remained discovery leads, not sources for strain-specific
    MIC transfer.
  snapshot_sha256: 1461676edeb1b9e827d4360a13a1b1ab14387ac24fbd23891f00a69ba6ec84e3
  search_scope: 2026-10-21; isolated batch 029; hidden/ignored-inclusive repository
    search and free official/primary-source retrieval, with access failures retained.
- evidence_id: gates
  kind: validation
  reference: Actual focused schema and strict validation commands
  locator: 284-focused-results.json; schema/strict logs
  accessed_at: '2026-10-21T12:43:16Z'
  support: supports
  summary: Both focused native validators completed with exit 0 and no errors. These
    deterministic passes do not independently establish biological evidence.
  snapshot_sha256: 495b0832c513d4aad7a600957b3c9c0e6330ce365355882b12cb9d0776e16ecc
assessments:
- assessment_id: identity
  area: identity
  topic: Exact congener, connectivity and geometry
  outcome: supported
  summary: The label and systematic synonym denote the native Z isomer. Original Figure
    1 and complete current ChEBI/PubChem molecular comparisons agree. A and B remain
    separate records with distinct complete InChIKeys.
  target_ids:
  - CHEBI:68767
  evidence_ids:
  - native
  - chebi
  - pubchem
  - chemistry
  - original-figure
- assessment_id: grounding
  area: grounding
  topic: Parents, antibacterial filing and role
  outcome: supported
  summary: The broader chemical parents fit the molecular graph. Original isolated-compound
    antibacterial observations support the antibacterial role without claiming all
    Gram-positive strains are susceptible.
  target_ids:
  - CHEBI:68767
  evidence_ids:
  - parents
  - chemistry
  - original
- assessment_id: xref
  area: grounding
  topic: Sole Reaxys cross-reference
  outcome: unknown
  summary: Current ChEBI repeats Reaxys:22515442, but the proprietary registry record
    was not independently inspected. No contradictory mapping was found in the inspected
    public sources.
  target_ids:
  - CHEBI:68767
  evidence_ids:
  - chebi
  - pubchem
  - access
- assessment_id: definition
  area: evidence
  topic: Producer and isolation context
  outcome: supported
  summary: The original paper identifies the fungus C. globosum IFB-E036 as the fermentation
    producer; C. dactylon is its plant host. The native species-level isolation statement
    preserves that distinction.
  target_ids:
  - CHEBI:68767
  evidence_ids:
  - native
  - original
  - original-figure
- assessment_id: activity
  area: evidence
  topic: Antibacterial assay scope
  outcome: supported
  summary: The original abstract supports antibacterial activity of compound 2. The
    8-32 microgram/mL interval is a joint summary across the measured compounds/organisms,
    not a single MIC for this record or a strain-independent potency. No native quantitative
    activity assertion requires correction.
  target_ids:
  - CHEBI:68767
  evidence_ids:
  - original
  - original-figure
  - native
- assessment_id: mechanism
  area: completeness
  topic: Optional mode of action and targets
  outcome: unknown
  summary: No native mode of action or target is asserted. The inspected original
    abstract/preview establishes activity, not an antibacterial molecular target.
    Chaetoglobosin actin effects and fungal biosynthetic regulation cannot fill that
    gap.
  target_ids:
  - CHEBI:68767
  evidence_ids:
  - native
  - original-figure
- assessment_id: optional
  area: scope
  topic: Other optional domains and structured adapters
  outcome: not_applicable
  summary: No native gene, protein, pathway, stress-response or transcriptomics claim
    triggers the structured adapter workflow. There are no native resistance, clinical,
    assay-collection or causal-graph assertions. Optional fields remain unpopulated
    without constituting a required-field defect.
  target_ids:
  - CHEBI:68767
  evidence_ids:
  - native
  - rubric
  - search
- assessment_id: provenance
  area: provenance
  topic: Source ownership, history and scientific status
  outcome: supported
  summary: The ChEBI row and extractor/seeder own generated fields. All 13 initial
    hashes and 21 expanded inputs were preserved and rechecked. SEEDED status, exact
    grounding and three seed/reseed events remain unchanged. Scientific REVIEWED status
    is not warranted by schema validity alone.
  target_ids:
  - CHEBI:68767
  evidence_ids:
  - owners
  - native
  - rubric
- assessment_id: validation
  area: schema
  topic: Actual focused checks
  outcome: supported
  summary: Schema, strict and independent chemical checks pass. Shared corpus checks
    are outside the focused results recorded here.
  target_ids:
  - CHEBI:68767
  evidence_ids:
  - gates
  - chemistry
findings: []
actions:
- action_id: A1
  description: Optionally enrich primary producer and antibacterial evidence after
    recovering the original complete assay methods and table.
  finding_ids: []
  target_ids:
  - CHEBI:68767
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/chaetoglocin-b.yaml
    role: Curator-owned evidence, producer and activity_spectrum claims through the
      validated writer
  acceptance_checks:
  - Keep chaetoglocin B / compound 2 separate from the other geometric isomer and
    chaetoglobosin congeners.
  - Preserve exact organism/strain, medium, inoculum, incubation, units, endpoint
    and isolated-material context before entering numerical MICs.
  - Represent C. globosum IFB-E036 as the producer and C. dactylon as the host; do
    not infer a direct antibacterial target from biosynthetic or crude-extract observations.
  - Run native schema, strict, source/reference/history and applicable QC gates after
    any separately authorized curation.
limitations:
- Original PMID:20814854 was inspected through its complete abstract and the public
  page-277 preview, including Figure 1 and Table 1. Remaining full text, detailed
  activity table and supporting data were not retrieved; failed PDF/SI routes returned
  HTML rather than research documents.
- Reaxys registry content was not independently accessible. Current ChEBI corroborates
  the imported identifier but is not an independent registry check.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native/source/status/history or saved-bundle changes were made. Initial input
  captures were retained.
- Native validators used the batch 029 environment. RDKit 2026.03.5 used the existing
  batch 019 interpreter against batch 029 cwd.
- The review does not establish absence of an antibacterial mechanism in the literature;
  it reports the limits of the inspected sources.
- Optional links and tags were selected and checked specifically for this exact target.
- Root independently read the entire native record and scientific draft, checked all
  captured hashes, compared chemical diagnostics and visually inspected original page
  277 before ordered persistence.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:68767
- https://pubchem.ncbi.nlm.nih.gov/compound/51039178
- https://doi.org/10.1055/s-0030-1250292
tags:
- chaetoglocin-b
- geometric-isomer
- primary-source-scope
- fungal-metabolite
```
