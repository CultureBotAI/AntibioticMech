# Review of CHEBI:65995 (Z-Halidrysone A)

- Review: 20261021T071351Z-chebi-65995-z-halidrysone-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:07:56Z
- Finished UTC: 2026-10-21T07:13:51Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The defined ChEBI entity and source-derived filing are sound; per-record validators and chemistry pass. Author-uploaded primary text resolves the experimental compound and supplies activity context without assigning a molecular mechanism. One minor evidence-completeness finding is actionable. Unassigned stereocentres are consistent with the source, and an external OLS SMILES discrepancy is not a record defect.

## Scope And Provenance

Entire record, maintained source row and ownership, all ontology IDs, native ChEBI structure, primary full-text transcription, experimental identity and assay scope.

Selection: Path-ordered unreviewed queue index 021; exactly one record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65995 | data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml | generated | (2E,6Z)-13-hydroxy-1-(2-hydroxy-5-methoxy-3-methylphenyl)-3,7,11,15-tetramethylhexadeca-2,6,14-triene-5,12-dione |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record LinkML validation | passed | True | CHEBI:65995 | Exit 0; No issues found. |
| Documented per-record closed-schema validation | passed | True | CHEBI:65995 | Exit 0; one file, zero ERROR rows. |
| Independent chemical and minted-identifier consistency | passed | False | CHEBI:65995 | Both encodings, metadata and minted source identity agree. |
| Current official term, parent, role and native structure comparison | passed | False | CHEBI:65995 | Assertions pass; the separate OLS SMILES serialization discrepancy is recorded explicitly. |
| Structured expression-module adapter applicability | not_applicable | False | CHEBI:65995 | The record names no gene, protein, regulator, pathway, stress-response or transcriptomic dataset. An algal isolation source and small-molecule identity do not supply a gene/module query. No absence of biology is inferred. |
| Authoritative full QC | failed | True | CHEBI:65995 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65995 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65995 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65995 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65995 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65995 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65995 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65995 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65995 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Defined constitution and alkene geometry, unresolved stereocentres

identity: supported. Targets: CHEBI:65995.

The record denotes the ChEBI 2E/6Z entity with two unassigned stereocentres. It is not the E congener or an isohalidrysone positional variant. The source experiments do not justify adding R/S assignments.

### Six broader ontology parents and source identity

grounding: supported. Targets: CHEBI:65995.

All parents are current direct broader classes and fit the represented functional groups. EXACT identifies the adopted ChEBI concept; it does not imply complete absolute stereochemistry. No unverified exact xref is asserted.

### Antibacterial filing and distinct antifouling endpoint

evidence: supported. Targets: CHEBI:65995.

ChEBI classification is independently corroborated by the compound-resolved growth assay. Barnacle settlement activity must remain a different endpoint and cannot establish a microbial target.

### Claim-level primary activity representation

completeness: concern. Targets: CHEBI:65995.

Concrete strain-specific activity and isolation evidence can now be curated from the identified experiment. The current seed preserves the broad source claim but lacks this bounded evidence context.

### Antimicrobial mode, target and target scope

scope: unknown. Targets: CHEBI:65995.

No exact-compound molecular mechanism or direct target was established. Meroterpenoid membership, growth inhibition and antifouling activity are insufficient to assign one. Native REVIEWED mechanism criteria remain unresolved.

### Algal isolation versus demonstrated biosynthesis

representation: supported. Targets: CHEBI:65995.

The definition accurately describes isolation. No producer_organisms object is asserted. A future biosynthetic producer claim needs evidence for that claim, rather than automatically treating collection material as proof.

### OLS SMILES versus native ChEBI representation

consistency: supported. Targets: CHEBI:65995.

The record retains the geometry supported by the native ChEBI page and primary structure discussion. OLS loses one directional marker while retaining the stereospecific InChI; preserve that observed source discrepancy without weakening the record.

### Other optional scientific objects

representation: not_applicable. Targets: CHEBI:65995.

No resistance, clinical, graph or dataset claim is asserted. Their absence alone is not a schema or scientific error.

### Generated ownership and audit trail

ownership: supported. Targets: CHEBI:65995.

Imported fields and three seed/reseed events agree with the maintained inputs. Captured hashes are retained. Evidence curation would belong to the actual record through the validated writer and history helpers.

### Native record validation

schema: supported. Targets: CHEBI:65995.

Both native per-record validators and independent molecular/source comparisons pass. These checks do not supply a missing mechanism.

## Findings

### F1: Identified primary activity evidence can be represented at claim level

minor / open / confirmed; issue key: chebi-65995-primary-activity-evidence-completeness.

The full primary text resolves the previously unassigned experimental compound and supplies bounded activity evidence. Curating that evidence would make the broad database claim reviewable at the assay level. The current seed makes no false numerical or mechanistic assertion, so this is a non-blocking evidence-completeness gap.

## Recommended Actions And Acceptance Checks

### A1

In a separately authorized curation pass, add narrow primary evidence and strain-specific observations for the structurally matched experimental material. Preserve unresolved stereochemistry and an explicit mechanism gap; retain the distinction between bacterial growth, barnacle settlement and toxicity.

- Visually confirm Table 3 and the structure chart before saving quantitative observations from the author-uploaded transcription; resolve the printed ATTC/ATCC culture-collection spelling against the catalog.
- Preserve the reported MIC values, units, organism/strain, medium, temperature, duration and assay; do not convert them into species-wide susceptibility or clinical categories.
- Do not assign R/S, a racemic composition, direct target, or microbial-target scope from structural class or endpoint alone.
- Retain isolation context in evidence/discussion; only add producer_organisms with separate support for biosynthesis.
- Keep imported identity and geometry unchanged unless independently justified source curation is later authorized. Use the validated writer and curation event, then just validate, just validate-strict, just verify-corpus --summary and just qc. Do not promote REVIEWED before its native requirements are met.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml; Entire generated record | supports | Read definition, one alias, six broader parents, antibacterial role, structure, source concept and all three seed/reseed events. No exact xrefs, scientific evidence objects, molecular target, activity, resistance, producer, clinical, graph or dataset object is asserted. |
| inventory | data/raw/chebi_antimicrobials.tsv; Complete CHEBI:65995 row and header; source manifest | supports | The adopted three-star row supplies the same identity, structure, parent set, single antimicrobial role and PMID:18529079 discovery lead. Its mechanism-role field is empty. Ignored-inclusive searches of maintained curation tables and conf found no exact-ID, minted-ID or Z-Halidrysone override. |
| ownership | scripts/extract_source_inventory.py; Default-structure copying, citation separation; scripts/seed_from_sources.py structure_from_chebi, mint, classification and curator merge | supports | The extractor selects the default ChEBI structure; the seeder reproduces imported identity, broader parents and in-scope activity. Source citation leads deliberately do not become blanket claim evidence. Additional annotations are curator-owned; a source-field repair would require maintained input/transform changes and reseeding. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:65995; Official HTML fetched directly after browser-tool access failed; /private/tmp/am-review-session/021-chebi.html | supports | The native entry matches the name, Z-Halidrysone A alias, definition, formula, charge, masses, both encodings and key. Its SMILES preserves both named double-bond geometries. No exact-identity cross-reference is asserted by the record. |
| ontology | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_65995; Official term, parents and has_role responses; 021-ols.json, 021-parents.json, 021-has_role.json | supports | The current non-obsolete term has six direct parents: secondary alpha-hydroxy ketone, phenols, aromatic ether, secondary alcohol, enone and meroterpenoid. All resolve. Its antibacterial role resolves; metabolite and antifouling-biocide roles lie outside the adopted antimicrobial role subset. OLS InChI agrees, but its SMILES literal omits the 2E marker. The native ChEBI page and record retain it. |
| primary | PMID:18529079; DOI:10.1021/np070110k; author-uploaded full-text transcription at https://www.academia.edu/18973886/Antifouling_Activity_of_Meroditerpenoids_from_the_Marine_Brown_Alga_Halidrys_siliquosa; pp.1123-1125, Table 3, structure discussion and methods | supports | Compound 2 matches the 2E/6Z constitution and hydroxyl/ketone positions; absolute-configuration attempts were inconclusive. Table 3 reports MICs 0.5, 1, 0.5 and 1 micrograms/mL for Cobetia marina 25374, Marinobacterium stanieri 27130, Vibrio fischeri 7744 and Pseudoalteromonas haloplanktis 14393, respectively. Methods specify microtiter broth dilution, Mueller-Hinton broth plus 15 g/L NaCl, 25 C, 24 hours and six replicates. Material came from voucher-identified H. siliquosa collected in Brittany. Barnacle settlement and toxicity are distinct endpoints; no antibacterial binding target is established. |
| primary-metadata | https://pubmed.ncbi.nlm.nih.gov/18529079/; Opened PubMed metadata and abstract | context_only | PMID and DOI identify the same 2008 Culioli study. Its abstract alone does not map Z-Halidrysone A to a numbered compound; the mapping above uses the inspected full-text structural discussion rather than the abstract activity superlative. |
| chemistry | RDKit and hashlib local calculations; /private/tmp/am-review-session/021-chemistry.py and 021-chemistry.json | supports | Both encodings yield HBKSTRSDLUAESY-PKVUCGNLSA-N, C28H40O5, charge zero, one fragment, average mass 456.623 and exact mass 456.28757438. Double-bond geometry agrees with 2E/6Z. Two stereocentres remain unspecified; this does not encode a racemate or assign an absolute configuration. The source-concept minted identifier is reproduced. |
| source-check | Focused source consistency assertions; /private/tmp/am-review-session/021-source-check.py and 021-source-check.json | supports | All parent identifiers and current role IDs resolve. Native-page SMILES and OLS InChI match the record. OLS SMILES gives a different key because one alkene geometry is unspecified; it was not substituted into the record or treated as a record defect. |
| validation | just validate; just validate-strict; Actual executions in isolated batch-003 checkout; /private/tmp/am-review-session/021-strict.tsv | supports | Both documented per-record validators exited 0; strict validation scanned one record with zero ERROR rows. |
| legacy | reports/yaml_record_review/20260922T022007Z-2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.md; Historical ad hoc review, read as a discovery and process lead | context_only | The legacy review could not inspect the full paper and left compound-number mapping unresolved. The present review independently inspected source text and resolves that bounded question. Its older major classification for missing optional annotations is not inherited; no saved structured finding is being closed. |
| search | Ignored-inclusive local and bounded free web discovery; 021-local-hits.txt; official ChEBI/OLS, publication and exact-compound searches on review date | context_only | The full paper was located through an author profile after publisher retrieval failed. No exact-compound molecular mechanism was established in the inspected material. Search results and predicted targets were not promoted into evidence. |

## Limits And Additional Notes

- The primary source was read as full-text transcription from an author-uploaded copy on Academia, not merely its abstract or generated takeaways. Publisher PDF and supporting-file requests returned 403, and direct author-site retrieval also returned 403. Table and structure images were not independently inspected; visual confirmation is an acceptance check before numeric curation.
- OLS metadata, parents and role endpoints were fetched successfully after sandbox DNS failure. Native ChEBI HTML was also fetched and checked. Its exact SMILES agrees with the record; the OLS SMILES literal loses one alkene directional marker although the same OLS response retains the correct InChI.
- Absolute stereochemical assignments were inconclusive in the inspected study. The compound-number match rests on its constitution and explicit alkene-geometry discussion; it does not establish a fully specified stereoisomer or racemate.
- Bounded searches did not establish a molecular antibacterial mechanism. This is not a universal absence claim, and no predicted target or neighbouring-compound result was adopted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Only scratch review artifacts were written. No record, maintained inventory, generated artifact or curation history was modified.
- Historical ad hoc review is retained as historical context; this observation does not overwrite it or close a structured finding.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T071351Z-chebi-65995-z-halidrysone-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of CHEBI:65995 (Z-Halidrysone A)
started_at: '2026-10-21T07:07:56Z'
finished_at: '2026-10-21T07:13:51Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and input hashes were captured before assessment. Historical
    review prose was used only as a lead.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Source identity, geometry and antibacterial role supported; primary
  evidence enrichment and mechanism review remain
scientific_review: true
summary: The defined ChEBI entity and source-derived filing are sound; per-record
  validators and chemistry pass. Author-uploaded primary text resolves the experimental
  compound and supplies activity context without assigning a molecular mechanism.
  One minor evidence-completeness finding is actionable. Unassigned stereocentres
  are consistent with the source, and an external OLS SMILES discrepancy is not a
  record defect.
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
  - path: data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml
    sha256: 8aab0c124322f0d57bfcc15e28c0c1cbc576724aea6d57492c59de753e6e3314
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
scope:
  description: Entire record, maintained source row and ownership, all ontology IDs,
    native ChEBI structure, primary full-text transcription, experimental identity
    and assay scope.
  selection: Path-ordered unreviewed queue index 021; exactly one record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65995
targets:
- target_id: CHEBI:65995
  path: data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml
  label: (2E,6Z)-13-hydroxy-1-(2-hydroxy-5-methoxy-3-methylphenyl)-3,7,11,15-tetramethylhexadeca-2,6,14-triene-5,12-dione
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
checks:
- check_id: schema
  name: Documented per-record LinkML validation
  status: passed
  required: true
  summary: Exit 0; No issues found.
  target_ids:
  - CHEBI:65995
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented per-record closed-schema validation
  status: passed
  required: true
  summary: Exit 0; one file, zero ERROR rows.
  target_ids:
  - CHEBI:65995
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml
    --out /private/tmp/am-review-session/021-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Independent chemical and minted-identifier consistency
  status: passed
  required: false
  summary: Both encodings, metadata and minted source identity agree.
  target_ids:
  - CHEBI:65995
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/021-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: source-check
  name: Current official term, parent, role and native structure comparison
  status: passed
  required: false
  summary: Assertions pass; the separate OLS SMILES serialization discrepancy is recorded
    explicitly.
  target_ids:
  - CHEBI:65995
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/021-source-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ontology
  - source-check
- check_id: imodulondb
  name: Structured expression-module adapter applicability
  status: not_applicable
  required: false
  summary: The record names no gene, protein, regulator, pathway, stress-response
    or transcriptomic dataset. An algal isolation source and small-molecule identity
    do not supply a gene/module query. No absence of biology is inferred.
  target_ids:
  - CHEBI:65995
  evidence_ids:
  - record
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:65995
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
  - CHEBI:65995
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
  - CHEBI:65995
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
  - CHEBI:65995
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
  - CHEBI:65995
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
  - CHEBI:65995
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
  - CHEBI:65995
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
  - CHEBI:65995
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
  - CHEBI:65995
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml
  locator: Entire generated record
  accessed_at: '2026-10-21T07:12:56Z'
  support: supports
  summary: Read definition, one alias, six broader parents, antibacterial role, structure,
    source concept and all three seed/reseed events. No exact xrefs, scientific evidence
    objects, molecular target, activity, resistance, producer, clinical, graph or
    dataset object is asserted.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Complete CHEBI:65995 row and header; source manifest
  accessed_at: '2026-10-21T07:12:56Z'
  support: supports
  summary: The adopted three-star row supplies the same identity, structure, parent
    set, single antimicrobial role and PMID:18529079 discovery lead. Its mechanism-role
    field is empty. Ignored-inclusive searches of maintained curation tables and conf
    found no exact-ID, minted-ID or Z-Halidrysone override.
- evidence_id: ownership
  kind: record_content
  reference: scripts/extract_source_inventory.py
  locator: Default-structure copying, citation separation; scripts/seed_from_sources.py
    structure_from_chebi, mint, classification and curator merge
  accessed_at: '2026-10-21T07:12:56Z'
  support: supports
  summary: The extractor selects the default ChEBI structure; the seeder reproduces
    imported identity, broader parents and in-scope activity. Source citation leads
    deliberately do not become blanket claim evidence. Additional annotations are
    curator-owned; a source-field repair would require maintained input/transform
    changes and reseeding.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:65995
  locator: Official HTML fetched directly after browser-tool access failed; /private/tmp/am-review-session/021-chebi.html
  accessed_at: '2026-10-21T07:12:56Z'
  support: supports
  summary: The native entry matches the name, Z-Halidrysone A alias, definition, formula,
    charge, masses, both encodings and key. Its SMILES preserves both named double-bond
    geometries. No exact-identity cross-reference is asserted by the record.
  snapshot_sha256: 64b9af9e50ab1b2a3cb11bf3f19a1865eeeef0e75da8402508596743a69df5b1
- evidence_id: ontology
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_65995
  locator: Official term, parents and has_role responses; 021-ols.json, 021-parents.json,
    021-has_role.json
  accessed_at: '2026-10-21T07:12:56Z'
  support: supports
  summary: 'The current non-obsolete term has six direct parents: secondary alpha-hydroxy
    ketone, phenols, aromatic ether, secondary alcohol, enone and meroterpenoid. All
    resolve. Its antibacterial role resolves; metabolite and antifouling-biocide roles
    lie outside the adopted antimicrobial role subset. OLS InChI agrees, but its SMILES
    literal omits the 2E marker. The native ChEBI page and record retain it.'
  snapshot_sha256: 59cbff7f9ca55c41703551332bc1270fdb7ee51061b8606b34464388c85e628a
- evidence_id: primary
  kind: primary_source
  reference: PMID:18529079
  locator: DOI:10.1021/np070110k; author-uploaded full-text transcription at https://www.academia.edu/18973886/Antifouling_Activity_of_Meroditerpenoids_from_the_Marine_Brown_Alga_Halidrys_siliquosa;
    pp.1123-1125, Table 3, structure discussion and methods
  accessed_at: '2026-10-21T07:12:56Z'
  support: supports
  summary: Compound 2 matches the 2E/6Z constitution and hydroxyl/ketone positions;
    absolute-configuration attempts were inconclusive. Table 3 reports MICs 0.5, 1,
    0.5 and 1 micrograms/mL for Cobetia marina 25374, Marinobacterium stanieri 27130,
    Vibrio fischeri 7744 and Pseudoalteromonas haloplanktis 14393, respectively. Methods
    specify microtiter broth dilution, Mueller-Hinton broth plus 15 g/L NaCl, 25 C,
    24 hours and six replicates. Material came from voucher-identified H. siliquosa
    collected in Brittany. Barnacle settlement and toxicity are distinct endpoints;
    no antibacterial binding target is established.
- evidence_id: primary-metadata
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/18529079/
  locator: Opened PubMed metadata and abstract
  accessed_at: '2026-10-21T07:12:56Z'
  support: context_only
  summary: PMID and DOI identify the same 2008 Culioli study. Its abstract alone does
    not map Z-Halidrysone A to a numbered compound; the mapping above uses the inspected
    full-text structural discussion rather than the abstract activity superlative.
- evidence_id: chemistry
  kind: validation
  reference: RDKit and hashlib local calculations
  locator: /private/tmp/am-review-session/021-chemistry.py and 021-chemistry.json
  accessed_at: '2026-10-21T07:12:56Z'
  support: supports
  summary: Both encodings yield HBKSTRSDLUAESY-PKVUCGNLSA-N, C28H40O5, charge zero,
    one fragment, average mass 456.623 and exact mass 456.28757438. Double-bond geometry
    agrees with 2E/6Z. Two stereocentres remain unspecified; this does not encode
    a racemate or assign an absolute configuration. The source-concept minted identifier
    is reproduced.
  snapshot_sha256: cfbb16728e39385250fa9569bc0b94ddd6114022aacb17955b0378dfd8af37b1
- evidence_id: source-check
  kind: validation
  reference: Focused source consistency assertions
  locator: /private/tmp/am-review-session/021-source-check.py and 021-source-check.json
  accessed_at: '2026-10-21T07:12:56Z'
  support: supports
  summary: All parent identifiers and current role IDs resolve. Native-page SMILES
    and OLS InChI match the record. OLS SMILES gives a different key because one alkene
    geometry is unspecified; it was not substituted into the record or treated as
    a record defect.
  snapshot_sha256: d2cfb14157bb04af2518e2384d9af81b3c12d609faaa028ff88aa07e51c120d8
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual executions in isolated batch-003 checkout; /private/tmp/am-review-session/021-strict.tsv
  accessed_at: '2026-10-21T07:12:56Z'
  support: supports
  summary: Both documented per-record validators exited 0; strict validation scanned
    one record with zero ERROR rows.
- evidence_id: legacy
  kind: prior_review
  reference: reports/yaml_record_review/20260922T022007Z-2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.md
  locator: Historical ad hoc review, read as a discovery and process lead
  accessed_at: '2026-10-21T07:12:56Z'
  support: context_only
  summary: The legacy review could not inspect the full paper and left compound-number
    mapping unresolved. The present review independently inspected source text and
    resolves that bounded question. Its older major classification for missing optional
    annotations is not inherited; no saved structured finding is being closed.
  snapshot_sha256: ae19b71d3afb16957bef74d6f1972e588bc4efbcca082304ce5405e3a1018d07
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local and bounded free web discovery
  locator: 021-local-hits.txt; official ChEBI/OLS, publication and exact-compound
    searches on review date
  accessed_at: '2026-10-21T07:12:56Z'
  support: context_only
  summary: The full paper was located through an author profile after publisher retrieval
    failed. No exact-compound molecular mechanism was established in the inspected
    material. Search results and predicted targets were not promoted into evidence.
  search_scope: prepare.py 21 searched identifier, label and slug with rg --no-ignore
    --hidden, excluding only .git and .venv. Maintained curation/conf searches included
    CHEBI:65995, minted identifier and Z-Halidrysone. Free web queries included Z-Halidrysone
    A antibacterial, Halidrysone mechanism, the exact primary title and DOI, and structure
    identifiers. Official ontology metadata, the native entry, PubMed and the author-uploaded
    primary text were read.
assessments:
- assessment_id: identity
  area: identity
  topic: Defined constitution and alkene geometry, unresolved stereocentres
  outcome: supported
  summary: The record denotes the ChEBI 2E/6Z entity with two unassigned stereocentres.
    It is not the E congener or an isohalidrysone positional variant. The source experiments
    do not justify adding R/S assignments.
  target_ids:
  - CHEBI:65995
  evidence_ids:
  - record
  - chebi
  - primary
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Six broader ontology parents and source identity
  outcome: supported
  summary: All parents are current direct broader classes and fit the represented
    functional groups. EXACT identifies the adopted ChEBI concept; it does not imply
    complete absolute stereochemistry. No unverified exact xref is asserted.
  target_ids:
  - CHEBI:65995
  evidence_ids:
  - ontology
  - record
  - chemistry
- assessment_id: classification
  area: evidence
  topic: Antibacterial filing and distinct antifouling endpoint
  outcome: supported
  summary: ChEBI classification is independently corroborated by the compound-resolved
    growth assay. Barnacle settlement activity must remain a different endpoint and
    cannot establish a microbial target.
  target_ids:
  - CHEBI:65995
  evidence_ids:
  - chebi
  - ontology
  - primary
- assessment_id: activity
  area: completeness
  topic: Claim-level primary activity representation
  outcome: concern
  summary: Concrete strain-specific activity and isolation evidence can now be curated
    from the identified experiment. The current seed preserves the broad source claim
    but lacks this bounded evidence context.
  target_ids:
  - CHEBI:65995
  evidence_ids:
  - record
  - primary
- assessment_id: mechanism
  area: scope
  topic: Antimicrobial mode, target and target scope
  outcome: unknown
  summary: No exact-compound molecular mechanism or direct target was established.
    Meroterpenoid membership, growth inhibition and antifouling activity are insufficient
    to assign one. Native REVIEWED mechanism criteria remain unresolved.
  target_ids:
  - CHEBI:65995
  evidence_ids:
  - record
  - primary
  - search
- assessment_id: producer
  area: representation
  topic: Algal isolation versus demonstrated biosynthesis
  outcome: supported
  summary: The definition accurately describes isolation. No producer_organisms object
    is asserted. A future biosynthetic producer claim needs evidence for that claim,
    rather than automatically treating collection material as proof.
  target_ids:
  - CHEBI:65995
  evidence_ids:
  - record
  - primary
- assessment_id: external-source
  area: consistency
  topic: OLS SMILES versus native ChEBI representation
  outcome: supported
  summary: The record retains the geometry supported by the native ChEBI page and
    primary structure discussion. OLS loses one directional marker while retaining
    the stereospecific InChI; preserve that observed source discrepancy without weakening
    the record.
  target_ids:
  - CHEBI:65995
  evidence_ids:
  - chebi
  - ontology
  - source-check
  - primary
- assessment_id: optional
  area: representation
  topic: Other optional scientific objects
  outcome: not_applicable
  summary: No resistance, clinical, graph or dataset claim is asserted. Their absence
    alone is not a schema or scientific error.
  target_ids:
  - CHEBI:65995
  evidence_ids:
  - record
- assessment_id: provenance
  area: ownership
  topic: Generated ownership and audit trail
  outcome: supported
  summary: Imported fields and three seed/reseed events agree with the maintained
    inputs. Captured hashes are retained. Evidence curation would belong to the actual
    record through the validated writer and history helpers.
  target_ids:
  - CHEBI:65995
  evidence_ids:
  - record
  - inventory
  - ownership
- assessment_id: schema-assessment
  area: schema
  topic: Native record validation
  outcome: supported
  summary: Both native per-record validators and independent molecular/source comparisons
    pass. These checks do not supply a missing mechanism.
  target_ids:
  - CHEBI:65995
  evidence_ids:
  - validation
  - chemistry
  - source-check
findings:
- finding_id: F1
  issue_key: chebi-65995-primary-activity-evidence-completeness
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Identified primary activity evidence can be represented at claim level
  description: The full primary text resolves the previously unassigned experimental
    compound and supplies bounded activity evidence. Curating that evidence would
    make the broad database claim reviewable at the assay level. The current seed
    makes no false numerical or mechanistic assertion, so this is a non-blocking evidence-completeness
    gap.
  target_ids:
  - CHEBI:65995
  field_paths:
  - evidence
  - activity_spectrum
  - discussions
  - mode_of_action_notes
  evidence_ids:
  - record
  - primary
  - legacy
  rule_id: 'review-checklist: Evidence standard, Activity, Mode of action and Audit'
  native_severity: minor primary-evidence completeness gap
  normalization_reason: A concrete source-backed enrichment is available. Optional
    fields are not mandatory merely because empty, and no incorrect identity, structure,
    role or mechanism is demonstrated. The legacy ad hoc major rating is not reused.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml
    role: Curator-owned evidence, activity observations and discussions through the
      validated writer with curation history; imported identity and roles remain source-owned
actions:
- action_id: A1
  description: In a separately authorized curation pass, add narrow primary evidence
    and strain-specific observations for the structurally matched experimental material.
    Preserve unresolved stereochemistry and an explicit mechanism gap; retain the
    distinction between bacterial growth, barnacle settlement and toxicity.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65995
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2e-6z-13-hydroxy-1-2-hydroxy-5-methoxy-3-methylphenyl-3-7-11-15-tetram.yaml
    role: Curator-owned evidence, activity observations and discussions through the
      validated writer with curation history; imported identity and roles remain source-owned
  acceptance_checks:
  - Visually confirm Table 3 and the structure chart before saving quantitative observations
    from the author-uploaded transcription; resolve the printed ATTC/ATCC culture-collection
    spelling against the catalog.
  - Preserve the reported MIC values, units, organism/strain, medium, temperature,
    duration and assay; do not convert them into species-wide susceptibility or clinical
    categories.
  - Do not assign R/S, a racemic composition, direct target, or microbial-target scope
    from structural class or endpoint alone.
  - Retain isolation context in evidence/discussion; only add producer_organisms with
    separate support for biosynthesis.
  - Keep imported identity and geometry unchanged unless independently justified source
    curation is later authorized. Use the validated writer and curation event, then
    just validate, just validate-strict, just verify-corpus --summary and just qc.
    Do not promote REVIEWED before its native requirements are met.
limitations:
- The primary source was read as full-text transcription from an author-uploaded copy
  on Academia, not merely its abstract or generated takeaways. Publisher PDF and supporting-file
  requests returned 403, and direct author-site retrieval also returned 403. Table
  and structure images were not independently inspected; visual confirmation is an
  acceptance check before numeric curation.
- OLS metadata, parents and role endpoints were fetched successfully after sandbox
  DNS failure. Native ChEBI HTML was also fetched and checked. Its exact SMILES agrees
  with the record; the OLS SMILES literal loses one alkene directional marker although
  the same OLS response retains the correct InChI.
- Absolute stereochemical assignments were inconclusive in the inspected study. The
  compound-number match rests on its constitution and explicit alkene-geometry discussion;
  it does not establish a fully specified stereoisomer or racemate.
- Bounded searches did not establish a molecular antibacterial mechanism. This is
  not a universal absence claim, and no predicted target or neighbouring-compound
  result was adopted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Only scratch review artifacts were written. No record, maintained inventory, generated
  artifact or curation history was modified.
- Historical ad hoc review is retained as historical context; this observation does
  not overwrite it or close a structured finding.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:65995
- https://pubmed.ncbi.nlm.nih.gov/18529079/
- https://doi.org/10.1021/np070110k
- https://www.academia.edu/18973886/Antifouling_Activity_of_Meroditerpenoids_from_the_Marine_Brown_Alga_Halidrys_siliquosa
tags:
- record-review
- meroterpenoid
- stereochemical-scope
- primary-activity-evidence
```
