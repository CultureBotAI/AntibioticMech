# Review of CHEBI:78884 (4-terpineol)

- Review: 20261021T074930Z-chebi-78884-4-terpineol-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:39:24Z
- Finished UTC: 2026-10-21T07:49:30Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The neutral, stereochemically unspecified 4-terpineol structure agrees across its encodings and official sources. One minor finding identifies available compound-specific activity and membrane-action evidence. Tea tree oil is a mixture; proposed PBP2a binding is computational. Current source synonym spelling differs only by Greek alpha versus ASCII alpha. Native REVIEWED sign-off remains incomplete.

## Scope And Provenance

Entire record, source ownership, native structure consistency, current ontology and external identifiers, and primary exact-component antibacterial activity, membrane effects and scope of docking and resistance observations.

Selection: Path-ordered unreviewed queue index 045; exactly one record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:78884 | data/antibiotics/antibacterial/4-terpineol.yaml | generated | 4-terpineol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record LinkML validation | passed | True | CHEBI:78884 | Exit 0; No issues found. |
| Documented per-record closed-schema validation | passed | True | CHEBI:78884 | Exit 0; one file, zero ERROR rows. |
| Independent structure and minted-identifier comparison | passed | False | CHEBI:78884 | Both structure encodings and all stored molecular metadata agree. |
| Initial literal synonym comparison | failed | False | CHEBI:78884 | Exit 1 because the record/native page use α-terpinen-4-ol and OLS exposes alpha-terpinen-4-ol. This representation difference was investigated and explicitly normalized in the succeeding check; it is not an identity failure. |
| Current source term, parent, role and structure comparison | passed | False | CHEBI:78884 | Exit 0 after explicitly accounting for native Greek alpha versus OLS ASCII alpha synonym spelling; term, parents, role, structure and source xrefs agree. |
| Structured expression-module adapter applicability | not_applicable | False | CHEBI:78884 | The current record names no gene, protein, regulator, pathway, stress response or transcriptomic dataset. Literature-only PBP2a is an uncurated docking hypothesis, not an existing annotation needing an expression-module query. |
| Authoritative full QC | failed | True | CHEBI:78884 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:78884 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:78884 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:78884 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:78884 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:78884 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:78884 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:78884 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:78884 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral unspecified 4-terpineol

identity: supported. Targets: CHEBI:78884.

Structure and molecular metadata agree. Retain unspecified stereochemistry and distinguish positional isomers, isolated component, enantiomers and whole tea tree oil.

### Parents, source synonyms and role

grounding: supported. Targets: CHEBI:78884.

Both direct parents and the antibacterial role resolve and fit. Greek alpha spelling is a source representation difference; it does not turn this molecule into alpha-terpineol.

### External exact-identity references

grounding: unknown. Targets: CHEBI:78884.

KEGG structure and BPDB identity section agree. HMDB/Reaxys target verification and independent CAS structure resolution remain incomplete; mixed BPDB use text must not be transferred.

### Exact-component antibacterial classification

evidence: supported. Targets: CHEBI:78884.

Primary compound experiments independently support antibacterial filing. Numerical observations require method, strain and volumetric units.

### Available primary mechanism and assay context

completeness: concern. Targets: CHEBI:78884.

Concrete primary evidence can enrich the broad seed. Optional empty fields alone are not the finding; usable activity and membrane-action evidence has been verified.

### Membrane observations versus predicted protein interaction

scope: supported. Targets: CHEBI:78884.

Membrane compromise is supported at a cellular-process level. PBP2a docking is a hypothesis and supplies no direct target binding or inhibition measurement. No single exclusive lethal target is established.

### Natural-oil component versus producer claim

representation: not_applicable. Targets: CHEBI:78884.

No producer object is asserted. A source plant or tea-tree-oil composition alone is insufficient to add a structured biosynthetic producer claim.

### Assay-bounded adaptation and resistance

scope: unknown. Targets: CHEBI:78884.

There is no resistance annotation to correct. Short experimental exposure results do not establish universal resistance avoidance or a defined genetic mechanism.

### Clinical, graph and dataset scope

representation: not_applicable. Targets: CHEBI:78884.

No such objects are asserted; docking, biomass assays and predicted drug properties cannot establish clinical efficacy.

### Reproducible imported identity and audit history

ownership: supported. Targets: CHEBI:78884.

Source row and mint agree; three seed/reseed events are consistent. Use the validated curator writer for new primary annotations.

### Native validation and independent checks

schema: supported. Targets: CHEBI:78884.

Native validators and chemistry pass. The resolved literal synonym failure is preserved as an executed failed check; independent external target limitations remain explicit.

## Findings

### F1: Available component-specific antibacterial and membrane evidence can be curated

minor / open / confirmed; issue key: chebi-78884-primary-membrane-activity-evidence-completeness.

The seed contains no primary activity or mechanism annotation, although individually tested terpinen-4-ol has experimentally supported antibacterial and membrane effects. Capturing these bounded observations would improve usefulness without inventing a specific protein target.

## Recommended Actions And Acceptance Checks

### A1

In a separately authorized curation pass, attach component-specific activity and membrane-action evidence with assay and hypothesis boundaries.

- Use the exact component and preserve stated purity, strain, medium, timing, controls and % vol/vol units. Distinguish measured new MIC/MBC results from earlier MIC values reused to set treatment concentrations.
- Represent membrane compromise at its supported process level; delayed autolysis is not immediate gross lysis. Do not infer a unique molecular target from membrane phenotypes.
- Label PBP2a docking as computational hypothesis, not binding or enzyme inhibition. Crystal-violet biomass reduction is not a viable-cell kill count, and predicted pharmacokinetics are not clinical evidence.
- Keep whole tea tree oil, other components and stereodefined enantiomers separate. The generic record does not encode a measured racemic mixture. BPDB mixture descriptions and TTO-only resistance experiments cannot become compound-specific evidence.
- Retain explicit unresolved HMDB/Reaxys and independent CAS target checks. Apply validated writer/history and run just validate, just validate-strict, just verify-corpus --summary and just qc before native REVIEWED sign-off.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/4-terpineol.yaml; Entire generated record | supports | Read definition, 19 synonyms, two parents, antibacterial role, five external xrefs, chemical fields, source concept and three seed/reseed events. No primary evidence, mode, target, producer, resistance, clinical, causal graph or dataset annotation is asserted. |
| inventory | data/raw/chebi_antimicrobials.tsv; Full CHEBI:78884 row and manifest; ignored-inclusive maintained-input search | supports | Source identity and structure match the seed. Eight imported PMID leads are not automatically claim evidence; the source contains no mechanism-role annotation. No exact curator override was found in the ignored-inclusive search of maintained inputs. |
| ownership | scripts/extract_source_inventory.py; ChEBI extraction and scripts/seed_from_sources.py source/mint and curator merge | supports | Imported identity belongs to maintained source inventory and generation; evidence and mechanism enrichment belong to curator-owned annotations with validated history. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:78884; 045-chebi.html and current OLS term | supports | Native entry matches identity and structural encodings. One stereocentre is unspecified. The racemate-formatted alias does not encode a measured enantiomer ratio or justify assigning one enantiomer. Native Greek alpha and OLS ASCII alpha are explicitly paired in the source. |
| ontology | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_78884; 045-ols.json, 045-parents.json and 045-has_role.json | supports | The non-obsolete term has direct terpineol and tertiary-alcohol parents and an antibacterial-agent role. Additional source roles do not imply missing antibacterial record fields. |
| kegg | https://rest.kegg.jp/get/C17073; 045-kegg.html and 045-keggmol.html; plain-text files despite suffix | supports | C17073 names terpinen-4-ol, formula C10H18O, CAS 562-74-3 and ChEBI 78884. Its downloaded Molfile independently yields WRYLYDPHFGVWKC-UHFFFAOYSA-N. |
| bpdb | https://sitem.herts.ac.uk/aeru/bpdb/Reports/2012.htm; 045-bpdb.html identity section versus use/composition text | supports | The identifier leads to terpinen-4-ol with the recorded InChI/key, formula and CAS. The same page also discusses tea tree oil, includes mixture aliases and lists a 300 g/kg minimum active purity; those mixture/use statements are not exact-compound evidence. |
| xref-limits | HMDB:HMDB0035833; cas:562-74-3; reaxys:1906603; 045-fetch-results.json; CAS public page and HMDB XML request | context_only | HMDB direct request returned 403; CAS returned an application shell without a readable structure. CAS is corroborated by KEGG/BPDB, not independently verified from registry structure. Reaxys exact target was not independently resolved from accessible authority. No incorrect mapping is established. |
| primary2002 | PMID:12019108; DOI:10.1128/AAC.46.6.1914-1920.2002; full publisher Methods, Results and Discussion at https://journals.asm.org/doi/10.1128/aac.46.6.1914-1920.2002 | supports | The study separately tests 97%-pure terpinen-4-ol against S. aureus ATCC 9144. At 0.25% vol/vol it causes killing, later 260-nm leakage and reduced salt tolerance; no immediate gross lysis is demonstrated. Electron microscopy follows 0.3% treatment for 10 minutes. These observations support membrane compromise, without proving a single protein target. The quoted 0.25% MIC originates from earlier component studies, rather than a new component MIC determination here. |
| primary2020 | PMID:32630600; DOI:10.3390/ijms21124531; full 045-primary2020.xml, Table 1 and Methods 3.1-3.7 | supports | Individually purchased terpinen-4-ol gives MIC 0.25% and reported MBC 0.5% vol/vol for ten S. aureus strains. Broth MIC uses cation-adjusted Mueller-Hinton broth, 35±2 C and 24 hours. Crystal-violet biofilm biomass, checkerboard interactions, and PBP2a docking are separate endpoints. Docking and predicted pharmacokinetics establish neither binding nor clinical efficacy. |
| resistance2012 | PMID:22083482; DOI:10.1128/AAC.05741-11; full web text at https://pmc.ncbi.nlm.nih.gov/articles/PMC3264233/ | context_only | The component-specific serial-exposure experiments show modest terpinen-4-ol MIC increases under some protocols. The single-step mutation-frequency experiment uses tea tree oil. These results do not justify a universal no-resistance claim or a terpinen-4-ol-specific genetic resistance mechanism. |
| chemistry | RDKit and hashlib calculations; 045-chemistry.py and 045-chemistry.json | supports | SMILES and InChI both yield the recorded key, C10H18O, neutral charge, one fragment and one unspecified stereocentre. Average and exact masses agree and the source-concept mint reproduces. |
| source-check | Focused official-source comparisons; 045-source-check-literal.py preserves initial code; 045-source-check.py and 045-source-check.json contain corrected explicit spelling comparison | supports | Initial exact-string synonym assertion exited 1. The native page explicitly pairs α-terpinen-4-ol with alpha-terpinen-4-ol; accounting for that spelling yields exit 0 for all assertions. Current source xrefs match the imported strings; this alone does not validate every external target. |
| validation | just validate; just validate-strict; Actual isolated batch-005 executions; 045-strict.tsv | supports | Both documented per-record validators exited 0; strict validation scanned one record with zero ERROR rows. |
| search | Ignored-inclusive local and bounded public primary-source discovery; 045-local-hits.txt and official-source/article searches | context_only | Exact component studies were prioritized over whole-oil effects. Authoritative target access is incomplete for some xrefs; no universal absence claim is made. |

## Limits And Additional Notes

- The 2002 full publisher text was read; Europe PMC fullTextXML returned HTTP 500 and the attempted CiteSeer PDF returned 404 (curl exit 56). No successful local full-text snapshot is claimed for that article; no electron-micrograph image was independently interpreted.
- The 2012 full web text was inspected, but its XML retrieval returned HTTP 500 and later web refreshes encountered a browser challenge. Its findings are bounded context, not a claim that resistance never arises.
- The 2020 full XML provides explicit assay methods and docking limits. Purity/catalog identifier and absolute configuration of its purchased terpinen-4-ol were not reported in the inspected Methods; no enantiomer-specific activity is inferred.
- HMDB returned 403, the CAS page was a JavaScript application shell, and Reaxys target identity was not independently resolved. Source xref reproduction is not equivalent to independent authority verification.
- Initial literal synonym comparison failed; the native page explicitly pairs Greek α and ASCII alpha forms and the corrected comparison passes. Both outcomes are recorded.
- This bounded review does not exhaust all activities or all literature; it does not authorize clinical claims or invent unobserved targets. Native REVIEWED criteria remain incomplete until evidence curation, unresolved checks and required gates are addressed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Only scratch review artifacts were written. No native record, maintained input, generated artifact or curation history was modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T074930Z-chebi-78884-4-terpineol-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of CHEBI:78884 (4-terpineol)
started_at: '2026-10-21T07:39:24Z'
finished_at: '2026-10-21T07:49:30Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Identity and antibacterial role supported; primary membrane-action
  and activity evidence awaits curation, with some external identifiers unresolved
scientific_review: true
summary: The neutral, stereochemically unspecified 4-terpineol structure agrees across
  its encodings and official sources. One minor finding identifies available compound-specific
  activity and membrane-action evidence. Tea tree oil is a mixture; proposed PBP2a
  binding is computational. Current source synonym spelling differs only by Greek
  alpha versus ASCII alpha. Native REVIEWED sign-off remains incomplete.
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
  - path: data/antibiotics/antibacterial/4-terpineol.yaml
    sha256: b03b335ddf15c7a39edf238d87d4f1fe143903878c926a710a9d8a4da96937eb
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
  description: Entire record, source ownership, native structure consistency, current
    ontology and external identifiers, and primary exact-component antibacterial activity,
    membrane effects and scope of docking and resistance observations.
  selection: Path-ordered unreviewed queue index 045; exactly one record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:78884
targets:
- target_id: CHEBI:78884
  path: data/antibiotics/antibacterial/4-terpineol.yaml
  label: 4-terpineol
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
  - CHEBI:78884
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/4-terpineol.yaml
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
  - CHEBI:78884
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/4-terpineol.yaml --out /private/tmp/am-review-session/045-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Independent structure and minted-identifier comparison
  status: passed
  required: false
  summary: Both structure encodings and all stored molecular metadata agree.
  target_ids:
  - CHEBI:78884
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/045-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: source-literal-first
  name: Initial literal synonym comparison
  status: failed
  required: false
  summary: Exit 1 because the record/native page use α-terpinen-4-ol and OLS exposes
    alpha-terpinen-4-ol. This representation difference was investigated and explicitly
    normalized in the succeeding check; it is not an identity failure.
  target_ids:
  - CHEBI:78884
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/045-source-check.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - source-check
- check_id: source-check
  name: Current source term, parent, role and structure comparison
  status: passed
  required: false
  summary: Exit 0 after explicitly accounting for native Greek alpha versus OLS ASCII
    alpha synonym spelling; term, parents, role, structure and source xrefs agree.
  target_ids:
  - CHEBI:78884
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/045-source-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ontology
  - source-check
- check_id: imodulondb
  name: Structured expression-module adapter applicability
  status: not_applicable
  required: false
  summary: The current record names no gene, protein, regulator, pathway, stress response
    or transcriptomic dataset. Literature-only PBP2a is an uncurated docking hypothesis,
    not an existing annotation needing an expression-module query.
  target_ids:
  - CHEBI:78884
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
  - CHEBI:78884
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
  - CHEBI:78884
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
  - CHEBI:78884
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
  - CHEBI:78884
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
  - CHEBI:78884
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
  - CHEBI:78884
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
  - CHEBI:78884
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
  - CHEBI:78884
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
  - CHEBI:78884
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/4-terpineol.yaml
  locator: Entire generated record
  accessed_at: '2026-10-21T07:44:02Z'
  support: supports
  summary: Read definition, 19 synonyms, two parents, antibacterial role, five external
    xrefs, chemical fields, source concept and three seed/reseed events. No primary
    evidence, mode, target, producer, resistance, clinical, causal graph or dataset
    annotation is asserted.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Full CHEBI:78884 row and manifest; ignored-inclusive maintained-input search
  accessed_at: '2026-10-21T07:44:02Z'
  support: supports
  summary: Source identity and structure match the seed. Eight imported PMID leads
    are not automatically claim evidence; the source contains no mechanism-role annotation.
    No exact curator override was found in the ignored-inclusive search of maintained
    inputs.
- evidence_id: ownership
  kind: record_content
  reference: scripts/extract_source_inventory.py
  locator: ChEBI extraction and scripts/seed_from_sources.py source/mint and curator
    merge
  accessed_at: '2026-10-21T07:44:02Z'
  support: supports
  summary: Imported identity belongs to maintained source inventory and generation;
    evidence and mechanism enrichment belong to curator-owned annotations with validated
    history.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:78884
  locator: 045-chebi.html and current OLS term
  accessed_at: '2026-10-21T07:44:02Z'
  support: supports
  summary: Native entry matches identity and structural encodings. One stereocentre
    is unspecified. The racemate-formatted alias does not encode a measured enantiomer
    ratio or justify assigning one enantiomer. Native Greek alpha and OLS ASCII alpha
    are explicitly paired in the source.
  snapshot_sha256: 76cdfdecf62be995c25c3e52f846b3c677e0c2f634e4aa824b7a085f07edba1c
- evidence_id: ontology
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_78884
  locator: 045-ols.json, 045-parents.json and 045-has_role.json
  accessed_at: '2026-10-21T07:44:02Z'
  support: supports
  summary: The non-obsolete term has direct terpineol and tertiary-alcohol parents
    and an antibacterial-agent role. Additional source roles do not imply missing
    antibacterial record fields.
  snapshot_sha256: 0edf048af6f748c468c4b4bce18d2f10e09e2e1a2b44e03c1b0b54bcf44dafe2
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/C17073
  locator: 045-kegg.html and 045-keggmol.html; plain-text files despite suffix
  accessed_at: '2026-10-21T07:44:02Z'
  support: supports
  summary: C17073 names terpinen-4-ol, formula C10H18O, CAS 562-74-3 and ChEBI 78884.
    Its downloaded Molfile independently yields WRYLYDPHFGVWKC-UHFFFAOYSA-N.
  snapshot_sha256: 87d7ee15cabcd7eac39cc96f74f9d117d829c05753a5c94b409aea26313cc2e3
- evidence_id: bpdb
  kind: database
  reference: https://sitem.herts.ac.uk/aeru/bpdb/Reports/2012.htm
  locator: 045-bpdb.html identity section versus use/composition text
  accessed_at: '2026-10-21T07:44:02Z'
  support: supports
  summary: The identifier leads to terpinen-4-ol with the recorded InChI/key, formula
    and CAS. The same page also discusses tea tree oil, includes mixture aliases and
    lists a 300 g/kg minimum active purity; those mixture/use statements are not exact-compound
    evidence.
  snapshot_sha256: 0fcde1d5e3ee397913f70c18bb40e7c673bbce4b880461d216dcd791a24785c5
- evidence_id: xref-limits
  kind: database
  reference: HMDB:HMDB0035833; cas:562-74-3; reaxys:1906603
  locator: 045-fetch-results.json; CAS public page and HMDB XML request
  accessed_at: '2026-10-21T07:44:02Z'
  support: context_only
  summary: HMDB direct request returned 403; CAS returned an application shell without
    a readable structure. CAS is corroborated by KEGG/BPDB, not independently verified
    from registry structure. Reaxys exact target was not independently resolved from
    accessible authority. No incorrect mapping is established.
  snapshot_sha256: 3f86d83ce3b9929b8f36d4d5d093e3d6eb97f15f82d26e491a18acd53f9567a3
- evidence_id: primary2002
  kind: primary_source
  reference: PMID:12019108
  locator: DOI:10.1128/AAC.46.6.1914-1920.2002; full publisher Methods, Results and
    Discussion at https://journals.asm.org/doi/10.1128/aac.46.6.1914-1920.2002
  accessed_at: '2026-10-21T07:44:02Z'
  support: supports
  summary: The study separately tests 97%-pure terpinen-4-ol against S. aureus ATCC
    9144. At 0.25% vol/vol it causes killing, later 260-nm leakage and reduced salt
    tolerance; no immediate gross lysis is demonstrated. Electron microscopy follows
    0.3% treatment for 10 minutes. These observations support membrane compromise,
    without proving a single protein target. The quoted 0.25% MIC originates from
    earlier component studies, rather than a new component MIC determination here.
- evidence_id: primary2020
  kind: primary_source
  reference: PMID:32630600
  locator: DOI:10.3390/ijms21124531; full 045-primary2020.xml, Table 1 and Methods
    3.1-3.7
  accessed_at: '2026-10-21T07:44:02Z'
  support: supports
  summary: Individually purchased terpinen-4-ol gives MIC 0.25% and reported MBC 0.5%
    vol/vol for ten S. aureus strains. Broth MIC uses cation-adjusted Mueller-Hinton
    broth, 35±2 C and 24 hours. Crystal-violet biofilm biomass, checkerboard interactions,
    and PBP2a docking are separate endpoints. Docking and predicted pharmacokinetics
    establish neither binding nor clinical efficacy.
  snapshot_sha256: eb042a449f354359738b8f168a480b39fa41fdfc303d99bd968383971b2c43e6
- evidence_id: resistance2012
  kind: primary_source
  reference: PMID:22083482
  locator: DOI:10.1128/AAC.05741-11; full web text at https://pmc.ncbi.nlm.nih.gov/articles/PMC3264233/
  accessed_at: '2026-10-21T07:44:02Z'
  support: context_only
  summary: The component-specific serial-exposure experiments show modest terpinen-4-ol
    MIC increases under some protocols. The single-step mutation-frequency experiment
    uses tea tree oil. These results do not justify a universal no-resistance claim
    or a terpinen-4-ol-specific genetic resistance mechanism.
- evidence_id: chemistry
  kind: validation
  reference: RDKit and hashlib calculations
  locator: 045-chemistry.py and 045-chemistry.json
  accessed_at: '2026-10-21T07:44:02Z'
  support: supports
  summary: SMILES and InChI both yield the recorded key, C10H18O, neutral charge,
    one fragment and one unspecified stereocentre. Average and exact masses agree
    and the source-concept mint reproduces.
  snapshot_sha256: fa1194e155cbf5c34a1716c3e6a23573d9cda9ba4b48b1016949472a9d76011a
- evidence_id: source-check
  kind: validation
  reference: Focused official-source comparisons
  locator: 045-source-check-literal.py preserves initial code; 045-source-check.py
    and 045-source-check.json contain corrected explicit spelling comparison
  accessed_at: '2026-10-21T07:44:02Z'
  support: supports
  summary: Initial exact-string synonym assertion exited 1. The native page explicitly
    pairs α-terpinen-4-ol with alpha-terpinen-4-ol; accounting for that spelling yields
    exit 0 for all assertions. Current source xrefs match the imported strings; this
    alone does not validate every external target.
  snapshot_sha256: 1fbb6e8b01163d5b79f97212ac134afaddca20d7b57c3b33b5b59a1a664d670f
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual isolated batch-005 executions; 045-strict.tsv
  accessed_at: '2026-10-21T07:44:02Z'
  support: supports
  summary: Both documented per-record validators exited 0; strict validation scanned
    one record with zero ERROR rows.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local and bounded public primary-source discovery
  locator: 045-local-hits.txt and official-source/article searches
  accessed_at: '2026-10-21T07:44:02Z'
  support: context_only
  summary: Exact component studies were prioritized over whole-oil effects. Authoritative
    target access is incomplete for some xrefs; no universal absence claim is made.
  search_scope: prepare.py 45 used rg --no-ignore --hidden, excluding only .git and
    .venv. Follow-up examined maintained tables/conf/legacy review data for CHEBI:78884,
    minted ID, 4-terpineol and terpinen-4-ol. Public searches covered exact names,
    antibacterial mechanism, tea-tree components, membrane assays, docking and resistance;
    current ChEBI/OLS, KEGG, BPDB, primary 2002 publisher text, 2020 XML and 2012
    web text were inspected.
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral unspecified 4-terpineol
  outcome: supported
  summary: Structure and molecular metadata agree. Retain unspecified stereochemistry
    and distinguish positional isomers, isolated component, enantiomers and whole
    tea tree oil.
  target_ids:
  - CHEBI:78884
  evidence_ids:
  - record
  - chebi
  - chemistry
  - kegg
- assessment_id: grounding
  area: grounding
  topic: Parents, source synonyms and role
  outcome: supported
  summary: Both direct parents and the antibacterial role resolve and fit. Greek alpha
    spelling is a source representation difference; it does not turn this molecule
    into alpha-terpineol.
  target_ids:
  - CHEBI:78884
  evidence_ids:
  - ontology
  - source-check
- assessment_id: xrefs
  area: grounding
  topic: External exact-identity references
  outcome: unknown
  summary: KEGG structure and BPDB identity section agree. HMDB/Reaxys target verification
    and independent CAS structure resolution remain incomplete; mixed BPDB use text
    must not be transferred.
  target_ids:
  - CHEBI:78884
  evidence_ids:
  - kegg
  - bpdb
  - xref-limits
- assessment_id: activity
  area: evidence
  topic: Exact-component antibacterial classification
  outcome: supported
  summary: Primary compound experiments independently support antibacterial filing.
    Numerical observations require method, strain and volumetric units.
  target_ids:
  - CHEBI:78884
  evidence_ids:
  - primary2002
  - primary2020
- assessment_id: completeness
  area: completeness
  topic: Available primary mechanism and assay context
  outcome: concern
  summary: Concrete primary evidence can enrich the broad seed. Optional empty fields
    alone are not the finding; usable activity and membrane-action evidence has been
    verified.
  target_ids:
  - CHEBI:78884
  evidence_ids:
  - record
  - primary2002
  - primary2020
- assessment_id: mechanism
  area: scope
  topic: Membrane observations versus predicted protein interaction
  outcome: supported
  summary: Membrane compromise is supported at a cellular-process level. PBP2a docking
    is a hypothesis and supplies no direct target binding or inhibition measurement.
    No single exclusive lethal target is established.
  target_ids:
  - CHEBI:78884
  evidence_ids:
  - primary2002
  - primary2020
- assessment_id: producer
  area: representation
  topic: Natural-oil component versus producer claim
  outcome: not_applicable
  summary: No producer object is asserted. A source plant or tea-tree-oil composition
    alone is insufficient to add a structured biosynthetic producer claim.
  target_ids:
  - CHEBI:78884
  evidence_ids:
  - record
  - bpdb
- assessment_id: resistance
  area: scope
  topic: Assay-bounded adaptation and resistance
  outcome: unknown
  summary: There is no resistance annotation to correct. Short experimental exposure
    results do not establish universal resistance avoidance or a defined genetic mechanism.
  target_ids:
  - CHEBI:78884
  evidence_ids:
  - record
  - resistance2012
- assessment_id: optional
  area: representation
  topic: Clinical, graph and dataset scope
  outcome: not_applicable
  summary: No such objects are asserted; docking, biomass assays and predicted drug
    properties cannot establish clinical efficacy.
  target_ids:
  - CHEBI:78884
  evidence_ids:
  - record
  - primary2020
- assessment_id: provenance
  area: ownership
  topic: Reproducible imported identity and audit history
  outcome: supported
  summary: Source row and mint agree; three seed/reseed events are consistent. Use
    the validated curator writer for new primary annotations.
  target_ids:
  - CHEBI:78884
  evidence_ids:
  - record
  - inventory
  - ownership
  - chemistry
- assessment_id: schema-assessment
  area: schema
  topic: Native validation and independent checks
  outcome: supported
  summary: Native validators and chemistry pass. The resolved literal synonym failure
    is preserved as an executed failed check; independent external target limitations
    remain explicit.
  target_ids:
  - CHEBI:78884
  evidence_ids:
  - validation
  - source-check
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-78884-primary-membrane-activity-evidence-completeness
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Available component-specific antibacterial and membrane evidence can be curated
  description: The seed contains no primary activity or mechanism annotation, although
    individually tested terpinen-4-ol has experimentally supported antibacterial and
    membrane effects. Capturing these bounded observations would improve usefulness
    without inventing a specific protein target.
  target_ids:
  - CHEBI:78884
  field_paths:
  - evidence
  - activity_spectrum
  - mode_of_action
  - mode_of_action_notes
  - discussions
  evidence_ids:
  - record
  - primary2002
  - primary2020
  rule_id: 'review-checklist: Evidence standard, Activity, Mode of action and Audit'
  native_severity: minor actionable primary-evidence completeness gap
  normalization_reason: A specific verified enrichment is available; no false existing
    structure, activity value or protein-target assertion is demonstrated. Missing
    optional fields alone do not warrant major severity.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/4-terpineol.yaml
    role: Curator-owned evidence, activity, mode_of_action and discussions through
      validated writer and curation history
actions:
- action_id: A1
  description: In a separately authorized curation pass, attach component-specific
    activity and membrane-action evidence with assay and hypothesis boundaries.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:78884
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/4-terpineol.yaml
    role: Curator-owned evidence, activity, mode_of_action and discussions through
      validated writer and curation history
  acceptance_checks:
  - Use the exact component and preserve stated purity, strain, medium, timing, controls
    and % vol/vol units. Distinguish measured new MIC/MBC results from earlier MIC
    values reused to set treatment concentrations.
  - Represent membrane compromise at its supported process level; delayed autolysis
    is not immediate gross lysis. Do not infer a unique molecular target from membrane
    phenotypes.
  - Label PBP2a docking as computational hypothesis, not binding or enzyme inhibition.
    Crystal-violet biomass reduction is not a viable-cell kill count, and predicted
    pharmacokinetics are not clinical evidence.
  - Keep whole tea tree oil, other components and stereodefined enantiomers separate.
    The generic record does not encode a measured racemic mixture. BPDB mixture descriptions
    and TTO-only resistance experiments cannot become compound-specific evidence.
  - Retain explicit unresolved HMDB/Reaxys and independent CAS target checks. Apply
    validated writer/history and run just validate, just validate-strict, just verify-corpus
    --summary and just qc before native REVIEWED sign-off.
limitations:
- The 2002 full publisher text was read; Europe PMC fullTextXML returned HTTP 500
  and the attempted CiteSeer PDF returned 404 (curl exit 56). No successful local
  full-text snapshot is claimed for that article; no electron-micrograph image was
  independently interpreted.
- The 2012 full web text was inspected, but its XML retrieval returned HTTP 500 and
  later web refreshes encountered a browser challenge. Its findings are bounded context,
  not a claim that resistance never arises.
- The 2020 full XML provides explicit assay methods and docking limits. Purity/catalog
  identifier and absolute configuration of its purchased terpinen-4-ol were not reported
  in the inspected Methods; no enantiomer-specific activity is inferred.
- HMDB returned 403, the CAS page was a JavaScript application shell, and Reaxys target
  identity was not independently resolved. Source xref reproduction is not equivalent
  to independent authority verification.
- Initial literal synonym comparison failed; the native page explicitly pairs Greek
  α and ASCII alpha forms and the corrected comparison passes. Both outcomes are recorded.
- This bounded review does not exhaust all activities or all literature; it does not
  authorize clinical claims or invent unobserved targets. Native REVIEWED criteria
  remain incomplete until evidence curation, unresolved checks and required gates
  are addressed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Only scratch review artifacts were written. No native record, maintained input,
  generated artifact or curation history was modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:78884
- https://rest.kegg.jp/get/C17073
- https://sitem.herts.ac.uk/aeru/bpdb/Reports/2012.htm
- https://doi.org/10.1128/AAC.46.6.1914-1920.2002
- https://doi.org/10.3390/ijms21124531
- https://doi.org/10.1128/AAC.05741-11
tags:
- record-review
- terpineol
- component-mixture-scope
- membrane-effects
- docking-hypothesis
```
