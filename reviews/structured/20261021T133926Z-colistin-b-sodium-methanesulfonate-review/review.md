# colistin B sodium methanesulfonate: coherent exact representation with unresolved historical product scope

- Review: 20261021T133926Z-colistin-b-sodium-methanesulfonate-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T13:22:53Z
- Finished UTC: 2026-10-21T13:39:26Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native pentasodium salt of colistimethate B reproduces its exact ChEBI graph, source names, parent classes and roles. One informational finding records a substantive unresolved boundary: this fivefold mono-sulfomethyl structure is the historical model, while newer product analyses and the current USP definition describe bis-substituted mixtures. The inspected literature does not establish purified native-form antibacterial measurements or justify substituting one modern mixture component. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position319; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:59664 | data/antibiotics/antibacterial/colistin-b-sodium-methanesulfonate.yaml | generated | colistin B sodium methanesulfonate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:59664 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:59664 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:59664 | Actual focused execution exited 0. |
| Independent authority and source comparison | passed | False | CHEBI:59664 | All four exact records passed; source hashes preserved. Initial scratch assumption of direct InChI-to-SMILES graph equality was corrected for standard-InChI tautomer normalization. |
| Authoritative full QC | failed | True | CHEBI:59664 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:59664 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:59664 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:59664 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:59664 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:59664 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:59664 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:59664 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:59664 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact graph, stoichiometry and stereochemical representation

identity: supported. Targets: CHEBI:59664.

The native pentasodium salt and complete key WZLRYLCDDODFHL-WSNMVEPOSA-I agree with current official encodings and maintained source. A/B tails and acid/sodium forms remain distinct.

### Chemical parents, names, roles and stable IDs

grounding: supported. Targets: CHEBI:59664.

All native aliases and broader parents agree with their source. No unasserted chemical cross-reference or physiological microstate is silently substituted. Classification is preserved at its documented database depth.

### Historical exact derivative versus contemporary product mixture

evidence: unknown. Targets: CHEBI:59664.

Historical source representation is reproducible, but modern bis-substitution evidence and product heterogeneity prevent treating commercial results as measurements on this exact graph. The source conflict requires adjudication before primary enrichment.

### Prodrug conversion and exact-compound eligibility

evidence: unknown. Targets: CHEBI:59664.

Antibacterial source roles are not contradicted merely by prodrug behavior. The inspected primary studies establish activity after conversion in heterogeneous preparations; purified native-form activity and its contribution to product efficacy remain unresolved.

### Optional mechanisms, clinical assertions and producers

scope: not_applicable. Targets: CHEBI:59664.

There are no populated claims in these domains. Colistin active-moiety mechanism, broad clinical product labels and the fermentation origin of precursor peptides do not establish an exact-derivative direct target, approval or natural producer. No native gene/pathway is named, so structured iModulonDB follow-up is not applicable.

### Adopted citation, maintained owners and history

provenance: supported. Targets: CHEBI:59664.

The sole adopted lead was resolved and kept secondary; source/history and thirteen initial hashes reconcile. Later original sources are explicitly new review evidence.

### Focused documented checks

schema: supported. Targets: CHEBI:59664.

Native schema and strict checks pass, as do chemical identity and source reproduction comparisons. These results do not resolve physical-material scope.

## Findings

### F1: Resolve historical mono-substituted identity before transferring commercial-product evidence

informational / open / provisional; issue key: chebi-59664-historical-monosulfomethyl-product-scope.

The native pentasodium salt is the exact historical fivefold mono-sulfomethyl model retained by ChEBI. Modern analytical results and the current USP definition concern bis-substituted heterogeneous preparations. This does not establish that the exact graph is impossible or justify replacing it with one of many mixture components, but it leaves purified-form existence/activity and product correspondence unresolved. Preserve the conflicting evidence and adjudicate identity/material scope before importing clinical, MIC or direct-mechanism claims.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate the exact historical derivative against modern material characterization before optional primary enrichment.

- Separate evidence of an isolated native component from product-mixture or hydrolysis measurements; identify substitution count and positions, A/B tail, stereochemistry and counterions.
- Preserve the historical/new analytical disagreement. Do not replace the record with an arbitrary bis-substituted component, equate a mixture label with one full key, or infer universal inactivity from one preparation/strain.
- If a future scope decision is supported, implement it through maintained decisions/source handling and native validated generation, with curation history and required corpus gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/colistin-b-sodium-methanesulfonate.yaml; Entire native YAML, including every name, chemical field, source concept and all three history events | supports | The record denotes pentasodium salt, full key WZLRYLCDDODFHL-WSNMVEPOSA-I; it has 4 exact source aliases, three broader chemical parents, two role terms and three seed-history events. No quantitative activity, target, causal graph, clinical approval, resistance determinant or producer assertion is populated. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; conf/sources.yaml; curation/decisions.tsv; 319-source-row.json and original captured source files | supports | Exact ChEBI source row reproduces the identity, definition, names, parents and roles. Its sole adopted citation is PMID16931410. All thirteen initial hashes remain unchanged. Source extraction and seeding own future changes; no generated edit is proposed. |
| authority | https://www.ebi.ac.uk/chebi/backend/api/public/compound/59664/; Current complete entry, molecular encodings, names, outgoing relations, role classification and citation list | supports | Current three-star ChEBI retains the exact native pentasodium salt, full key WZLRYLCDDODFHL-WSNMVEPOSA-I, names and classification. The functional parent is colistin B. ChEBI distinguishes acid, conjugate base, sodium salt and broader mixture concepts; functional-parent or has-part links are not exact-equivalence assertions. |
| chemistry | Independent RDKit molecular and maintained-source comparison; 316319-chemistry.py;316319-authority-chemistry.json; focused native checks | supports | Native SMILES and current ChEBI SMILES/molfile match by mutual chirality-aware mapping. All five encodings reproduce the complete standard InChI and key. Formula, masses and charge pass focused checks. The graph has 6 component(s), 12 assigned stereocentres and five secondary N-H groups each bearing one sulfomethyl substituent. InChI re-import yields the standard-equivalent amide/imidic-acid tautomer representation, not a new stereoisomer. |
| terms | CHEBI:25903;CHEBI:59062;CHEBI:37793;CHEBI:38700;CHEBI:33281;CHEBI:33282; 316319-term-*.json; exact native parent/role subset | supports | Peptide antibiotic and polymyxin are broader classes. Amino sulfonic acid applies to the neutral acid and organic sodium salt to the five-counterion form. Antibacterial agent explicitly includes an active part; a prodrug is not automatically disqualified. These source roles do not establish purified-component potency or a direct target. |
| adopted-lead | PMID:16931410;DOI:10.1016/S1473-3099(06)70580-1; Complete indexed abstract and publication-type metadata; full review not inspected | context_only | The sole adopted lead is a 2006 review of colistin chemistry, pharmacokinetics and clinical use. Its abstract does not establish a purified exact derivative, counterion-specific MIC or component structure. It remains secondary context. |
| historical-synthesis | PMID:14256814;DOI:10.1111/j.1476-5381.1964.tb01610.x; Original 1964 pp 552–556 and 568–573 visually read, including electrophoresis Figure 3; complete indexed abstract | supports | The original synthesis study uses heterogeneous sodium polymyxin derivatives. Electrophoresis and activity after reversion support variable substitution; the mono-to-penta model is inferred, with elemental analyses cited but not shown. Most experiments concern polymyxin B. It does not isolate the exact native A/B component. |
| hydrolysis | PMID:16723551;DOI:10.1128/AAC.00035-06; Complete 2006 main HTML paragraphs, Methods/Results/Discussion and figure captions; images not visually audited | supports | Commercial CMS and colistin sulfate were tested against P. aeruginosa ATCC27853 in CAMHB. Delayed killing tracked hydrolytically generated colistin and was reproduced by incremental colistin addition. The apparent CMS MIC is a mixture/conversion endpoint, not a purified native-form MIC. |
| modern-analysis | PMID:39957899;DOI:10.1016/j.jpha.2024.101072; Complete 2024 main XML, all methods/results/conclusions; original Figures 3 and5 visually inspected | supports | EDQM E1/E2 standards and commercial batches were analyzed by 2D-LC-MS. Predominant four-, six- and eight-substituent species were assigned; the authors reported no mono-substituted amines in the analyzed preparations. The assignments use fragmentation/database matching, with preparation hydrolysis acknowledged. This conflicts with treating the historical graph as the measured commercial product. |
| method-2021 | PMID:33799846;DOI:10.3390/molecules26061546; Original 2021 main XML, selected introduction, methods, results and conclusion paragraphs | context_only | This original UPLC-UV study separates commercial-product peaks but does not resolve their exact structures. It explicitly discusses the historical mono/bis substitution conflict and uses an arbitrary commercial batch as reference. It is analytical context, not proof of native component identity. |
| usp | https://doi.usp.org/USPNF/USPNF_M19880_05_01.html; Public 2025 monograph definition preview, not paywalled full monograph | supports | The current USP definition describes a mixture with two to five bis-sulfomethylated primary amine sites. Its product-level definition is inconsistent with identifying the mixture solely by a fivefold mono-substituted graph. |
| label-conflict | https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6a335659-03b0-4a2d-9cd4-7dcf7da96fe6; 2025 label Description and structure caption only | supports | The label retains the historical pentasodium formula and A/B tail distinction. This supports persistence of the older model in official product descriptions, not resolution of the newer analytical conflict or proof of purified-component clinical approval. |
| stability | PMID:23070159;DOI:10.1128/AAC.01079-12; Complete 2012 main HTML prose, Methods/Results and Table 1 caption; numeric table not independently reprocessed | context_only | The commercial injection stability experiment measures released colistin A/B in reconstituted product. Its temperature/time observations do not chemically identify an individual native precursor. The review does not import mixture stability or product mass/activity units as an exact derivative measurement. |
| search | Ignored-inclusive local and bounded public-source search; Initial entire-checkout rg file hits;316319-owner-search.json; exact ChEBI IDs and adopted PMID follow-up | context_only | Initial ignored-inclusive discovery found source, generated and research context. A focused ignored-inclusive search of maintained decisions, curator inventory, conf, scripts and skills found no exact additional owner or override. No exhaustive public-literature absence claim is made. |
| modern-supplement | PMID:39957899; DOI:10.1016/j.jpha.2024.101072; original supplementary mmc3.xlsx and mmc4.docx; All 107 Table S3 assignment rows covering 99 peaks; complete supplementary DOCX prose; Tables S1/S2 headers and first entries only | context_only | Table S3 was read for formula, substitution count, source and match scores in every row. The count column reports 35 four-substituent, 46 six-substituent, 24 eight-substituent and two ten-substituent rows; neither that column nor listed formulae identify a five-sulfur species. Internal formula/count discrepancies occur for peaks 29, 59 and 74. Some assigned entries lack a tandem-MS score or fall below the stated match thresholds. The complete supplementary prose also describes inferred identities and in-source fragmentation. These assignments support a bounded commercial-material comparison, not independent structural proof of every proposed component. Supplementary mass-spectral image panels were not independently interpreted. |

## Limits And Additional Notes

- The exact native derivative was not independently isolated, measured or synthesized in this review. ChEBI agreement establishes represented identity, not physical presence in each commercial preparation.
- The sole adopted 2006 review was inspected at complete indexed-abstract depth. Original 1964 pages 552–556 and 568–573 were visually read, not the entire intervening pharmacology/results section; electrophoretic substitution assignments are indirect.
- The 2006 hydrolysis paper was read as complete main HTML prose and captions, without an independent visual audit of each figure or reanalysis of raw measurements. Its commercial sodium preparation does not establish free-acid or purified A/B component MICs.
- The 2024 main text and original Figures 3/5 were inspected. All 107 Table S3 assignment rows and complete supplementary DOCX prose were read; Tables S1/S2 were inspected only at header/first-entry depth, and supplementary spectral images were not independently interpreted. Formula/count inconsistencies and below-threshold or absent match scores prevent treating all assignments as established structures. MS/database deductions are not equivalent to independent NMR characterization of all 99 proposed components.
- The 2021 UV study was read in selected main-text passages; its statistical table values and supplementary code were not reanalyzed. The 2012 stability source provides product-level context, not a new exact-form result.
- The USP public definition and DailyMed Description were inspected; the full USP monograph and all product clinical evidence were not reviewed. No treatment guidance or source approval claim is adopted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All four native records were read separately in full; shared primary studies retain different applicability to each acid or sodium form.
- The failed initial source-row helper used source_id instead of chebi_id and was corrected before any source conclusion. This scratch failure and the graph-mapping diagnostic are not final review-validation failures.
- No native record, source table, curation status or history was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T133926Z-colistin-b-sodium-methanesulfonate-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'colistin B sodium methanesulfonate: coherent exact representation with unresolved
  historical product scope'
started_at: '2026-10-21T13:22:53Z'
finished_at: '2026-10-21T13:39:26Z'
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
summary: 'The native pentasodium salt of colistimethate B reproduces its exact ChEBI
  graph, source names, parent classes and roles. One informational finding records
  a substantive unresolved boundary: this fivefold mono-sulfomethyl structure is the
  historical model, while newer product analyses and the current USP definition describe
  bis-substituted mixtures. The inspected literature does not establish purified native-form
  antibacterial measurements or justify substituting one modern mixture component.
  Scientific assessment retains the stated evidence limits; full verification is blocked
  by the shared native-library failure.'
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
  - path: data/antibiotics/antibacterial/colistin-b-sodium-methanesulfonate.yaml
    sha256: cb19d7261df2f7ec514771da3db8a04e56d27102da605850bd1a3a2a4839e563
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
- target_id: CHEBI:59664
  path: data/antibiotics/antibacterial/colistin-b-sodium-methanesulfonate.yaml
  label: colistin B sodium methanesulfonate
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
  selection: Initially uncovered queue position319; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:59664
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:59664
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    319
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:59664
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/colistin-b-sodium-methanesulfonate.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:59664
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/colistin-b-sodium-methanesulfonate.yaml --out /private/tmp/am-review-session/319-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-chemistry
  name: Independent authority and source comparison
  required: false
  status: passed
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/316319-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  summary: All four exact records passed; source hashes preserved. Initial scratch
    assumption of direct InChI-to-SMILES graph equality was corrected for standard-InChI
    tautomer normalization.
  target_ids:
  - CHEBI:59664
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
  - CHEBI:59664
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
  - CHEBI:59664
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
  - CHEBI:59664
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
  - CHEBI:59664
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
  - CHEBI:59664
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
  - CHEBI:59664
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
  - CHEBI:59664
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
  - CHEBI:59664
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
  - CHEBI:59664
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/colistin-b-sodium-methanesulfonate.yaml
  locator: Entire native YAML, including every name, chemical field, source concept
    and all three history events
  accessed_at: '2026-10-21T13:34:43Z'
  support: supports
  summary: The record denotes pentasodium salt, full key WZLRYLCDDODFHL-WSNMVEPOSA-I;
    it has 4 exact source aliases, three broader chemical parents, two role terms
    and three seed-history events. No quantitative activity, target, causal graph,
    clinical approval, resistance determinant or producer assertion is populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py; conf/sources.yaml; curation/decisions.tsv
  locator: 319-source-row.json and original captured source files
  accessed_at: '2026-10-21T13:34:43Z'
  support: supports
  summary: Exact ChEBI source row reproduces the identity, definition, names, parents
    and roles. Its sole adopted citation is PMID16931410. All thirteen initial hashes
    remain unchanged. Source extraction and seeding own future changes; no generated
    edit is proposed.
  snapshot_sha256: efa9a8f534e23f80f698f7d77c4f07d202c230f798aed7b14c498ec3998a2a93
- evidence_id: authority
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/59664/
  locator: Current complete entry, molecular encodings, names, outgoing relations,
    role classification and citation list
  accessed_at: '2026-10-21T13:34:43Z'
  support: supports
  summary: Current three-star ChEBI retains the exact native pentasodium salt, full
    key WZLRYLCDDODFHL-WSNMVEPOSA-I, names and classification. The functional parent
    is colistin B. ChEBI distinguishes acid, conjugate base, sodium salt and broader
    mixture concepts; functional-parent or has-part links are not exact-equivalence
    assertions.
  snapshot_sha256: 3d413a3542624ad42d17b3d608a097982161ca835d36f5dd12744d054f66dbf7
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit molecular and maintained-source comparison
  locator: 316319-chemistry.py;316319-authority-chemistry.json; focused native checks
  accessed_at: '2026-10-21T13:34:43Z'
  support: supports
  summary: Native SMILES and current ChEBI SMILES/molfile match by mutual chirality-aware
    mapping. All five encodings reproduce the complete standard InChI and key. Formula,
    masses and charge pass focused checks. The graph has 6 component(s), 12 assigned
    stereocentres and five secondary N-H groups each bearing one sulfomethyl substituent.
    InChI re-import yields the standard-equivalent amide/imidic-acid tautomer representation,
    not a new stereoisomer.
  snapshot_sha256: b1914d31150fd1351f86d945722b0f86e6769a149e32f55fd0bff3af43cf67cf
- evidence_id: terms
  kind: authority
  reference: CHEBI:25903;CHEBI:59062;CHEBI:37793;CHEBI:38700;CHEBI:33281;CHEBI:33282
  locator: 316319-term-*.json; exact native parent/role subset
  accessed_at: '2026-10-21T13:34:43Z'
  support: supports
  summary: Peptide antibiotic and polymyxin are broader classes. Amino sulfonic acid
    applies to the neutral acid and organic sodium salt to the five-counterion form.
    Antibacterial agent explicitly includes an active part; a prodrug is not automatically
    disqualified. These source roles do not establish purified-component potency or
    a direct target.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: adopted-lead
  kind: database
  reference: PMID:16931410;DOI:10.1016/S1473-3099(06)70580-1
  locator: Complete indexed abstract and publication-type metadata; full review not
    inspected
  accessed_at: '2026-10-21T13:34:43Z'
  support: context_only
  summary: The sole adopted lead is a 2006 review of colistin chemistry, pharmacokinetics
    and clinical use. Its abstract does not establish a purified exact derivative,
    counterion-specific MIC or component structure. It remains secondary context.
  snapshot_sha256: 3ac6d8dc5e25be5d670f748825a55ead6ce3e7b7a6b4a58b393d052936079f87
- evidence_id: historical-synthesis
  kind: primary_source
  reference: PMID:14256814;DOI:10.1111/j.1476-5381.1964.tb01610.x
  locator: Original 1964 pp 552–556 and 568–573 visually read, including electrophoresis
    Figure 3; complete indexed abstract
  accessed_at: '2026-10-21T13:34:43Z'
  support: supports
  summary: The original synthesis study uses heterogeneous sodium polymyxin derivatives.
    Electrophoresis and activity after reversion support variable substitution; the
    mono-to-penta model is inferred, with elemental analyses cited but not shown.
    Most experiments concern polymyxin B. It does not isolate the exact native A/B
    component.
  snapshot_sha256: 57daff3d39338e954bb276a5bf867f62ee202e16131fa6c38e3346e091d3add3
- evidence_id: hydrolysis
  kind: primary_source
  reference: PMID:16723551;DOI:10.1128/AAC.00035-06
  locator: Complete 2006 main HTML paragraphs, Methods/Results/Discussion and figure
    captions; images not visually audited
  accessed_at: '2026-10-21T13:34:43Z'
  support: supports
  summary: Commercial CMS and colistin sulfate were tested against P. aeruginosa ATCC27853
    in CAMHB. Delayed killing tracked hydrolytically generated colistin and was reproduced
    by incremental colistin addition. The apparent CMS MIC is a mixture/conversion
    endpoint, not a purified native-form MIC.
  snapshot_sha256: 571f1517a1569b1289437914e7b7ea018e47010c4aa7868bab4ac67f54b07528
- evidence_id: modern-analysis
  kind: primary_source
  reference: PMID:39957899;DOI:10.1016/j.jpha.2024.101072
  locator: Complete 2024 main XML, all methods/results/conclusions; original Figures
    3 and5 visually inspected
  accessed_at: '2026-10-21T13:34:43Z'
  support: supports
  summary: EDQM E1/E2 standards and commercial batches were analyzed by 2D-LC-MS.
    Predominant four-, six- and eight-substituent species were assigned; the authors
    reported no mono-substituted amines in the analyzed preparations. The assignments
    use fragmentation/database matching, with preparation hydrolysis acknowledged.
    This conflicts with treating the historical graph as the measured commercial product.
  snapshot_sha256: 98a06a9b6acbd3b03a2f2fd399493a1ec85771ea5dce7f107767fe1694ff1baf
- evidence_id: method-2021
  kind: primary_source
  reference: PMID:33799846;DOI:10.3390/molecules26061546
  locator: Original 2021 main XML, selected introduction, methods, results and conclusion
    paragraphs
  accessed_at: '2026-10-21T13:34:43Z'
  support: context_only
  summary: This original UPLC-UV study separates commercial-product peaks but does
    not resolve their exact structures. It explicitly discusses the historical mono/bis
    substitution conflict and uses an arbitrary commercial batch as reference. It
    is analytical context, not proof of native component identity.
  snapshot_sha256: ef7335b577cfd831732fa7de4d3351fc1f023c854819b48e3ea4434227b8f045
- evidence_id: usp
  kind: authority
  reference: https://doi.usp.org/USPNF/USPNF_M19880_05_01.html
  locator: Public 2025 monograph definition preview, not paywalled full monograph
  accessed_at: '2026-10-21T13:34:43Z'
  support: supports
  summary: The current USP definition describes a mixture with two to five bis-sulfomethylated
    primary amine sites. Its product-level definition is inconsistent with identifying
    the mixture solely by a fivefold mono-substituted graph.
  snapshot_sha256: 21de61f0e17843119f006c5041f2128456abf78b8cb40c5e6d9807d05ae4bd68
- evidence_id: label-conflict
  kind: authority
  reference: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6a335659-03b0-4a2d-9cd4-7dcf7da96fe6
  locator: 2025 label Description and structure caption only
  accessed_at: '2026-10-21T13:34:43Z'
  support: supports
  summary: The label retains the historical pentasodium formula and A/B tail distinction.
    This supports persistence of the older model in official product descriptions,
    not resolution of the newer analytical conflict or proof of purified-component
    clinical approval.
  snapshot_sha256: 45f36e160319aa78b0ae533c6e2bd4aa1701d528f30c2f462223294075513704
- evidence_id: stability
  kind: primary_source
  reference: PMID:23070159;DOI:10.1128/AAC.01079-12
  locator: Complete 2012 main HTML prose, Methods/Results and Table 1 caption; numeric
    table not independently reprocessed
  accessed_at: '2026-10-21T13:34:43Z'
  support: context_only
  summary: The commercial injection stability experiment measures released colistin
    A/B in reconstituted product. Its temperature/time observations do not chemically
    identify an individual native precursor. The review does not import mixture stability
    or product mass/activity units as an exact derivative measurement.
  snapshot_sha256: 948c8fa25bb92d0bbabb369f9bdd2fcd0ee8c0b5f13c9516e9d37d9ef48e7439
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local and bounded public-source search
  locator: Initial entire-checkout rg file hits;316319-owner-search.json; exact ChEBI
    IDs and adopted PMID follow-up
  accessed_at: '2026-10-21T13:34:43Z'
  support: context_only
  summary: Initial ignored-inclusive discovery found source, generated and research
    context. A focused ignored-inclusive search of maintained decisions, curator inventory,
    conf, scripts and skills found no exact additional owner or override. No exhaustive
    public-literature absence claim is made.
  search_scope: 2026-10-21; exact four ChEBI identifiers, names and native keys; local
    rg --no-ignore --hidden; exact adopted PMID plus primary synthesis, hydrolysis
    and analytical studies.
  snapshot_sha256: 18cbb909ee2229bccb742bcf4dd7adc6e482813e42bf312ae8e171a1dc798033
- evidence_id: modern-supplement
  kind: primary_source
  reference: PMID:39957899; DOI:10.1016/j.jpha.2024.101072; original supplementary
    mmc3.xlsx and mmc4.docx
  locator: All 107 Table S3 assignment rows covering 99 peaks; complete supplementary
    DOCX prose; Tables S1/S2 headers and first entries only
  accessed_at: '2026-10-21T13:37:28Z'
  support: context_only
  summary: Table S3 was read for formula, substitution count, source and match scores
    in every row. The count column reports 35 four-substituent, 46 six-substituent,
    24 eight-substituent and two ten-substituent rows; neither that column nor listed
    formulae identify a five-sulfur species. Internal formula/count discrepancies
    occur for peaks 29, 59 and 74. Some assigned entries lack a tandem-MS score or
    fall below the stated match thresholds. The complete supplementary prose also
    describes inferred identities and in-source fragmentation. These assignments support
    a bounded commercial-material comparison, not independent structural proof of
    every proposed component. Supplementary mass-spectral image panels were not independently
    interpreted.
  snapshot_sha256: 7a3d69444151a46b410b575f8ac5b7ad812e31c086d9a22ea1280e57ab92fe54
assessments:
- assessment_id: identity
  area: identity
  topic: Exact graph, stoichiometry and stereochemical representation
  outcome: supported
  summary: The native pentasodium salt and complete key WZLRYLCDDODFHL-WSNMVEPOSA-I
    agree with current official encodings and maintained source. A/B tails and acid/sodium
    forms remain distinct.
  target_ids:
  - CHEBI:59664
  evidence_ids:
  - native
  - authority
  - chemistry
  - owners
- assessment_id: grounding
  area: grounding
  topic: Chemical parents, names, roles and stable IDs
  outcome: supported
  summary: All native aliases and broader parents agree with their source. No unasserted
    chemical cross-reference or physiological microstate is silently substituted.
    Classification is preserved at its documented database depth.
  target_ids:
  - CHEBI:59664
  evidence_ids:
  - authority
  - terms
  - chemistry
- assessment_id: material
  area: evidence
  topic: Historical exact derivative versus contemporary product mixture
  outcome: unknown
  summary: Historical source representation is reproducible, but modern bis-substitution
    evidence and product heterogeneity prevent treating commercial results as measurements
    on this exact graph. The source conflict requires adjudication before primary
    enrichment.
  target_ids:
  - CHEBI:59664
  evidence_ids:
  - historical-synthesis
  - modern-analysis
  - method-2021
  - usp
  - label-conflict
  - modern-supplement
- assessment_id: activity
  area: evidence
  topic: Prodrug conversion and exact-compound eligibility
  outcome: unknown
  summary: Antibacterial source roles are not contradicted merely by prodrug behavior.
    The inspected primary studies establish activity after conversion in heterogeneous
    preparations; purified native-form activity and its contribution to product efficacy
    remain unresolved.
  target_ids:
  - CHEBI:59664
  evidence_ids:
  - terms
  - hydrolysis
  - historical-synthesis
  - modern-analysis
  - modern-supplement
- assessment_id: scope
  area: scope
  topic: Optional mechanisms, clinical assertions and producers
  outcome: not_applicable
  summary: There are no populated claims in these domains. Colistin active-moiety
    mechanism, broad clinical product labels and the fermentation origin of precursor
    peptides do not establish an exact-derivative direct target, approval or natural
    producer. No native gene/pathway is named, so structured iModulonDB follow-up
    is not applicable.
  target_ids:
  - CHEBI:59664
  evidence_ids:
  - native
  - hydrolysis
  - label-conflict
- assessment_id: provenance
  area: provenance
  topic: Adopted citation, maintained owners and history
  outcome: supported
  summary: The sole adopted lead was resolved and kept secondary; source/history and
    thirteen initial hashes reconcile. Later original sources are explicitly new review
    evidence.
  target_ids:
  - CHEBI:59664
  evidence_ids:
  - owners
  - adopted-lead
  - search
  - chemistry
- assessment_id: validation
  area: schema
  topic: Focused documented checks
  outcome: supported
  summary: Native schema and strict checks pass, as do chemical identity and source
    reproduction comparisons. These results do not resolve physical-material scope.
  target_ids:
  - CHEBI:59664
  evidence_ids:
  - chemistry
  - owners
findings:
- finding_id: F1
  issue_key: chebi-59664-historical-monosulfomethyl-product-scope
  category: evidence
  severity: informational
  status: open
  certainty: provisional
  title: Resolve historical mono-substituted identity before transferring commercial-product
    evidence
  description: The native pentasodium salt is the exact historical fivefold mono-sulfomethyl
    model retained by ChEBI. Modern analytical results and the current USP definition
    concern bis-substituted heterogeneous preparations. This does not establish that
    the exact graph is impossible or justify replacing it with one of many mixture
    components, but it leaves purified-form existence/activity and product correspondence
    unresolved. Preserve the conflicting evidence and adjudicate identity/material
    scope before importing clinical, MIC or direct-mechanism claims.
  target_ids:
  - CHEBI:59664
  field_paths:
  - definition
  - chemical_structure
  - activity_roles
  evidence_ids:
  - authority
  - chemistry
  - historical-synthesis
  - modern-analysis
  - usp
  - label-conflict
  - hydrolysis
  - modern-supplement
  rule_id: 'native-review-checklist: exact chemical form, evidence scope and source
    conflicts'
  native_severity: informational unresolved exact-material boundary
  normalization_reason: The graph is chemically coherent and faithful to its stated
    authority. The record does not claim a purified assay or exact clinical product
    identity; no automatic corrective edit or exclusion is established by the inspected
    mixture studies.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted exact identity and source definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated identity and source provenance
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Future documented identity/scope adjudication if justified
actions:
- action_id: A1
  description: Adjudicate the exact historical derivative against modern material
    characterization before optional primary enrichment.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:59664
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted exact identity and source definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated identity and source provenance
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Future documented identity/scope adjudication if justified
  acceptance_checks:
  - Separate evidence of an isolated native component from product-mixture or hydrolysis
    measurements; identify substitution count and positions, A/B tail, stereochemistry
    and counterions.
  - Preserve the historical/new analytical disagreement. Do not replace the record
    with an arbitrary bis-substituted component, equate a mixture label with one full
    key, or infer universal inactivity from one preparation/strain.
  - If a future scope decision is supported, implement it through maintained decisions/source
    handling and native validated generation, with curation history and required corpus
    gates.
limitations:
- The exact native derivative was not independently isolated, measured or synthesized
  in this review. ChEBI agreement establishes represented identity, not physical presence
  in each commercial preparation.
- The sole adopted 2006 review was inspected at complete indexed-abstract depth. Original
  1964 pages 552–556 and 568–573 were visually read, not the entire intervening pharmacology/results
  section; electrophoretic substitution assignments are indirect.
- The 2006 hydrolysis paper was read as complete main HTML prose and captions, without
  an independent visual audit of each figure or reanalysis of raw measurements. Its
  commercial sodium preparation does not establish free-acid or purified A/B component
  MICs.
- The 2024 main text and original Figures 3/5 were inspected. All 107 Table S3 assignment
  rows and complete supplementary DOCX prose were read; Tables S1/S2 were inspected
  only at header/first-entry depth, and supplementary spectral images were not independently
  interpreted. Formula/count inconsistencies and below-threshold or absent match scores
  prevent treating all assignments as established structures. MS/database deductions
  are not equivalent to independent NMR characterization of all 99 proposed components.
- The 2021 UV study was read in selected main-text passages; its statistical table
  values and supplementary code were not reanalyzed. The 2012 stability source provides
  product-level context, not a new exact-form result.
- The USP public definition and DailyMed Description were inspected; the full USP
  monograph and all product clinical evidence were not reviewed. No treatment guidance
  or source approval claim is adopted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All four native records were read separately in full; shared primary studies retain
  different applicability to each acid or sodium form.
- The failed initial source-row helper used source_id instead of chebi_id and was
  corrected before any source conclusion. This scratch failure and the graph-mapping
  diagnostic are not final review-validation failures.
- No native record, source table, curation status or history was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
