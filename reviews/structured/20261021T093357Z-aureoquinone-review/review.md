# Aureoquinone: exact identity and original antibacterial/protease evidence supported

- Review: 20261021T093357Z-aureoquinone-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:15:28Z
- Finished UTC: 2026-10-21T09:33:57Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Native neutral aureoquinone structure, fungal culture origin and qualitative antibacterial/protease wording are supported by the original full paper. No confirmed native error was found. Optional enrichment should distinguish bacterial MIC, general protease inhibition, Candida secretion/adhesion effects and patent claims; none proves an unmeasured direct fungal or HIV target. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position122; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65458 | data/antibiotics/antibacterial/aureoquinone.yaml | generated | aureoquinone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:65458 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:65458 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:65458 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:65458 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65458 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65458 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65458 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65458 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65458 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65458 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65458 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65458 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Focused validation, provenance and native status

schema: supported. Targets: CHEBI:65458.

Actual checks pass and all 13 initial input hashes remain unchanged. A structured review does not promote native SEEDED status.

### Native graph and source groundings

identity: supported. Targets: CHEBI:65458.

Original structure, synthesis abstract and current ChEBI corroborate the native graph. A differently represented name-resolved PubChem tautomer is not evidence of a native identity failure.

### Antibacterial and protease definition

evidence: supported. Targets: CHEBI:65458.

Original purified-compound MIC and enzyme assays support the qualitative wording, with exact endpoint and method limits.

### Aureobasidium surface-culture origin

evidence: supported. Targets: CHEBI:65458.

Original isolated culture and fermentation support the generic source wording. Crepidotus host and later talcarpone decomposition must not be recast as proven biosynthesis by those taxa.

### Document resolution and experimental scope

evidence: supported. Targets: CHEBI:65458.

The patent xref resolves. Its broad therapeutic claims are distinguishable from measured secretion/adhesion phenotypes and are not native approval assertions.

### Optional target and antivirulence evidence

completeness: unknown. Targets: CHEBI:65458.

There is no native false target claim. Protease assays, bacterial growth and Candida secretion/adhesion do not establish a single direct antimicrobial target or a shared causal chain.

## Findings

### F1: Add exact primary evidence while preserving distinct biological endpoints

informational / open / confirmed; issue key: aureoquinone-primary-endpoint-scope-enrichment.

The original paper directly supports chemical identity, cultured-fungus origin, one bacterial MIC and general protease inhibition. Candida secretion/adhesion and patent uses need separate evidence scope; optional enrichment does not imply a missing required field.

## Recommended Actions And Acceptance Checks

### A1

Optionally curate primary identity and activity with explicit assay limits.

- Retain the original neutral graph and exact B. subtilis ATCC6633 MIC120 µg/mL. Inspect the cited method before supplying missing medium, incubation or protocol details.
- Preserve BODIPY-casein protease endpoints and measured units; resolve enzyme preparation/taxon before choosing specific protein accessions. Do not turn IC50 into binding Kd or bacterial MIC.
- Retrieve full Candida methods before quantitative phenotype curation; the inspected abstract refutes direct secreted-Sap interaction as the explanation and reports no growth killing at tested concentrations.
- Treat broad patent HIV/SAP claims and formulations as document context, not experimental target or approval evidence. Do not transfer talcarpone1/2 MICs to aureoquinone3.
- Ground the actual Aureobasidium culture and retain taxonomic resolution limits if adding a producer object; use the maintained writer and claim-level primary evidence workflow.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/aureoquinone.yaml; Entire YAML including four seed/reseed events | supports | Read the definition, exact systematic synonym, two parents, antibacterial role, complete chemistry, Reaxys xref, patent document xref and source concept. There are no populated targets, quantified activity, producer objects, clinical, resistance, mechanism, graph or dataset annotations. |
| source | data/raw/chebi_antimicrobials.tsv; Row 1178; extractor/seeder ownership | supports | The adopted source reproduces native fields and separates patent DE10349512 as a document xref. The single PMID lead is 11213290. The exact record has no primary claim evidence; this absence alone is not a native defect. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:65458; Current ChEBI page and OLS parent responses | supports | ChEBI agrees on neutral C12H10O6, key REESKGYZXCEZKQ-UHFFFAOYSA-N, one fragment, no stereocentres, average mass 250.206 and exact mass 250.04774. CHEBI:132157 hydroxynaphthoquinone and CHEBI:33853 phenols are appropriate parents; CHEBI:33282 is the retained antibacterial role. Reaxys 2588151 is source-corroborated but not directly inspected. |
| tautomer | Independent comparison with a name-resolved PubChem entry; 122-pubchem-name.json and 122-tautomer-comparison.json | context_only | The exact-key PubChem request returned 404. Name resolution gives CID10083434, key DWESCCREDKEKQP-UHFFFAOYSA-N, with a different quinone tautomer representation. RDKit tautomer enumeration produces a common candidate, supporting the relationship; its max-transforms warning prevents an exhaustive canonicalization claim. PubChem is not a native xref, and these observations do not justify replacing the paper-supported native graph or reporting it absent. |
| original-identity | PMID:11213290; DOI:10.7164/antibiotics.53.1293; 122-primary2000.pdf all three pages read as text and visually | supports | Original culture extraction yielded 60 mg of purified aureoquinone from 60 L of Aureobasidium sp. surface cultures. Genus identification was morphological; the strain originated from a Crepidotus fruiting body, which is not thereby the producer. Figure 1, NMR, high-resolution MS and X-ray analysis support the native naphthoquinone graph. The alternate positional numbering in the paper is compatible under ring reflection. Raw spectra and crystallographic coordinates were not reanalysed. |
| antibacterial | DOI:10.7164/antibiotics.53.1293; Original p1295, visually checked MIC sentence and reference7 | supports | Purified aureoquinone has reported Bacillus subtilis ATCC6633 MIC120 µg/mL. The paper cites the 1986 ninth German Pharmacopoeia for method, without giving complete medium/incubation details on the page. This is exact-compound antibacterial support, not a clinical breakpoint or broad-spectrum susceptibility claim. |
| proteases | DOI:10.7164/antibiotics.53.1293; Original p1294, visually checked enzyme paragraph and assay description | supports | Reported protease IC50 values are trypsin11.4, papain14.5, thermolysin17.8, collagenase7.1 and zinc-protease8.7 µg/mL using BODIPY-labelled casein fluorescence. This supports the generic protease-inhibitor definition. Exact enzyme preparations/taxon accessions and a microbial growth-causal target are not established; neither binding constants nor direct inhibition of every protease family follows. |
| patent | https://patents.google.com/patent/DE10349512A1/en; Complete visible German/translated description, examples and four claims in 122-patent-visible.txt | partial | The retained document resolves to a 1,4-naphthoquinone use patent. Examples measure Candida CBS5982 Sap release and HeLa S3 adhesion with solvent controls; the description names Aureobasidium sp. HKI0318 as a production strain. Broad claimed SAP/HIV-protease uses and pharmaceutical formulations are not evidence of measured HIV enzyme inhibition, direct Sap binding, clinical efficacy or approval. The patent itself states that activity against the earlier general protease panel cannot simply establish SAP/HIV activity. No legal-status conclusion is made. |
| candida | PMID:18422912; DOI:10.1111/j.1439-0507.2008.01515.x; complete indexed abstract | partial | The original study reports aureoquinone and laccaridiones reducing C. albicans adhesion and Sap release. It explicitly states these effects are not due to direct interaction with secreted Saps and that the compounds are neither fungistatic nor fungicidal at applied concentrations. These are antivirulence phenotypes, not direct Sap enzyme inhibition or fungal MICs. Full methods were unavailable, so no exact-concentration quantitative annotations are proposed. |
| synthesis | PMID:16438511; DOI:10.1021/jo0519561; complete indexed abstract | partial | The 2006 synthesis explicitly identifies aureoquinone as 2,5,7,8-tetrahydroxy-3,6-dimethyl-1,4-naphthoquinone, corroborating native substitution. Hybocarpone and boryquinone are separate structures; their cytotoxicity is not aureoquinone antibacterial mechanism evidence. |
| later-isolation | PMID:38110564; DOI:10.1038/s41429-023-00688-x; complete indexed abstract | context_only | The Talaromyces johnpittii MST-FP2594 study identifies aureoquinone as compound3 alongside talcarpones1 and2. The abstract antibacterial/fungal MIC ranges are explicitly for talcarpones1/2, not aureoquinone. It also reports conversion of talcarpone1 to3, so isolation alone does not independently prove a biosynthetic gene-level producer claim for3. |
| adapter | Native iModulonDB adapter; 122-imodulondb-datasets.txt; executed before open-ended research | context_only | The successful catalog retry returned bacterial/archaeal datasets without Aureobasidium or Candida coverage. The native definition gives no exact protease isoform or assay organism suitable for a target-specific query. No unrelated bacterial component is used as fungal or host mechanism evidence. |
| chemistry | Independent RDKit calculations; 122-chemistry.json and actual focused validation logs | supports | Both native encodings reproduce the full key, formula, neutral charge, one fragment, average and exact masses, and deterministic ChEBI mint. Schema and strict checks exit 0. Internal consistency does not by itself prove biological activity. |
| search | CultureBotAI/AntibioticMech; 122-local-hits.txt and 122-maintained-search.txt | context_only | Exact identity resolves to the native source row and readiness queue. No exact-target maintained override was found in the specified search. The aureoquinone numeric-ID search also returned an unrelated CRyPTIC measurement, which was rejected as a substring collision. |

## Limits And Additional Notes

- The single adopted PMID has no indexed abstract; this gap was resolved by reading the complete three-page original paper and all page images. The cited full antimicrobial protocol and raw spectra/crystallographic data were not independently inspected.
- The patent text and examples were read in German and displayed English translation; structure/assay figures were not digitized and no graph-derived values are adopted. Patent legal status was not evaluated.
- The 2008 Candida, 2006 synthesis and 2024 isolation studies remain abstract-only. Europe PMC full-text XML returned 500; PMC HTML required browser verification, and Europe PMC/Wiley pages were inaccessible. These access failures do not establish absence of full text.
- The PubChem tautomer comparison hit the enumerator transformation limit; only the observed common candidate is reported. No exact-key absence claim beyond the specific 404 response is made. Reaxys was not directly inspected.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 13 captured input hashes were rechecked unchanged. No native record was edited; absent optional fields are not treated as schema defects.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T093357Z-aureoquinone-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Aureoquinone: exact identity and original antibacterial/protease evidence
  supported'
started_at: '2026-10-21T09:15:28Z'
finished_at: '2026-10-21T09:33:57Z'
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
summary: Native neutral aureoquinone structure, fungal culture origin and qualitative
  antibacterial/protease wording are supported by the original full paper. No confirmed
  native error was found. Optional enrichment should distinguish bacterial MIC, general
  protease inhibition, Candida secretion/adhesion effects and patent claims; none
  proves an unmeasured direct fungal or HIV target. Scientific assessment retains
  the stated evidence limits; full verification is blocked by the shared native-library
  failure.
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
  - path: data/antibiotics/antibacterial/aureoquinone.yaml
    sha256: 7756229eb3d393c0e6ed7da9d0d27fe8301752e59295a48a30905dd3a36d65ea
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
- target_id: CHEBI:65458
  path: data/antibiotics/antibacterial/aureoquinone.yaml
  label: aureoquinone
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
  selection: Initially uncovered queue position122; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65458
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65458
  command: .venv/bin/python /private/tmp/am-review-session/focus011-root.py 122
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65458
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/aureoquinone.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65458
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/aureoquinone.yaml --out /private/tmp/am-review-session/122-strict.tsv
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
  - CHEBI:65458
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
  - CHEBI:65458
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
  - CHEBI:65458
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
  - CHEBI:65458
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
  - CHEBI:65458
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
  - CHEBI:65458
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
  - CHEBI:65458
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
  - CHEBI:65458
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
  - CHEBI:65458
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/aureoquinone.yaml
  locator: Entire YAML including four seed/reseed events
  accessed_at: '2026-10-21T09:23:22Z'
  support: supports
  summary: Read the definition, exact systematic synonym, two parents, antibacterial
    role, complete chemistry, Reaxys xref, patent document xref and source concept.
    There are no populated targets, quantified activity, producer objects, clinical,
    resistance, mechanism, graph or dataset annotations.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Row 1178; extractor/seeder ownership
  accessed_at: '2026-10-21T09:23:22Z'
  support: supports
  summary: The adopted source reproduces native fields and separates patent DE10349512
    as a document xref. The single PMID lead is 11213290. The exact record has no
    primary claim evidence; this absence alone is not a native defect.
  snapshot_sha256: a6e2a506a05f2da6bd51eee37c27a6e774ee35fb492e4dcbbff7828690951836
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:65458
  locator: Current ChEBI page and OLS parent responses
  accessed_at: '2026-10-21T09:23:22Z'
  support: supports
  summary: ChEBI agrees on neutral C12H10O6, key REESKGYZXCEZKQ-UHFFFAOYSA-N, one
    fragment, no stereocentres, average mass 250.206 and exact mass 250.04774. CHEBI:132157
    hydroxynaphthoquinone and CHEBI:33853 phenols are appropriate parents; CHEBI:33282
    is the retained antibacterial role. Reaxys 2588151 is source-corroborated but
    not directly inspected.
  snapshot_sha256: 2db5babbaddac4b2916ee5ca654c86c052e5911b5a9022c6a7e819a147eaa8d0
- evidence_id: tautomer
  kind: validation
  reference: Independent comparison with a name-resolved PubChem entry
  locator: 122-pubchem-name.json and 122-tautomer-comparison.json
  accessed_at: '2026-10-21T09:23:22Z'
  support: context_only
  summary: The exact-key PubChem request returned 404. Name resolution gives CID10083434,
    key DWESCCREDKEKQP-UHFFFAOYSA-N, with a different quinone tautomer representation.
    RDKit tautomer enumeration produces a common candidate, supporting the relationship;
    its max-transforms warning prevents an exhaustive canonicalization claim. PubChem
    is not a native xref, and these observations do not justify replacing the paper-supported
    native graph or reporting it absent.
  snapshot_sha256: 397fd8bd9873944116a243f9d537e27847d3affc64b530f2cb78e846843b23e7
- evidence_id: original-identity
  kind: primary_source
  reference: PMID:11213290
  locator: DOI:10.7164/antibiotics.53.1293; 122-primary2000.pdf all three pages read
    as text and visually
  accessed_at: '2026-10-21T09:23:22Z'
  support: supports
  summary: Original culture extraction yielded 60 mg of purified aureoquinone from
    60 L of Aureobasidium sp. surface cultures. Genus identification was morphological;
    the strain originated from a Crepidotus fruiting body, which is not thereby the
    producer. Figure 1, NMR, high-resolution MS and X-ray analysis support the native
    naphthoquinone graph. The alternate positional numbering in the paper is compatible
    under ring reflection. Raw spectra and crystallographic coordinates were not reanalysed.
  snapshot_sha256: 0af93d5a3e583e3f10225b23ce52e71c8930d2264c837c58fd1bf7287a8553dc
- evidence_id: antibacterial
  kind: primary_source
  reference: DOI:10.7164/antibiotics.53.1293
  locator: Original p1295, visually checked MIC sentence and reference7
  accessed_at: '2026-10-21T09:23:22Z'
  support: supports
  summary: Purified aureoquinone has reported Bacillus subtilis ATCC6633 MIC120 µg/mL.
    The paper cites the 1986 ninth German Pharmacopoeia for method, without giving
    complete medium/incubation details on the page. This is exact-compound antibacterial
    support, not a clinical breakpoint or broad-spectrum susceptibility claim.
  snapshot_sha256: 0af93d5a3e583e3f10225b23ce52e71c8930d2264c837c58fd1bf7287a8553dc
- evidence_id: proteases
  kind: primary_source
  reference: DOI:10.7164/antibiotics.53.1293
  locator: Original p1294, visually checked enzyme paragraph and assay description
  accessed_at: '2026-10-21T09:23:22Z'
  support: supports
  summary: Reported protease IC50 values are trypsin11.4, papain14.5, thermolysin17.8,
    collagenase7.1 and zinc-protease8.7 µg/mL using BODIPY-labelled casein fluorescence.
    This supports the generic protease-inhibitor definition. Exact enzyme preparations/taxon
    accessions and a microbial growth-causal target are not established; neither binding
    constants nor direct inhibition of every protease family follows.
  snapshot_sha256: 0af93d5a3e583e3f10225b23ce52e71c8930d2264c837c58fd1bf7287a8553dc
- evidence_id: patent
  kind: primary_source
  reference: https://patents.google.com/patent/DE10349512A1/en
  locator: Complete visible German/translated description, examples and four claims
    in 122-patent-visible.txt
  accessed_at: '2026-10-21T09:23:22Z'
  support: partial
  summary: The retained document resolves to a 1,4-naphthoquinone use patent. Examples
    measure Candida CBS5982 Sap release and HeLa S3 adhesion with solvent controls;
    the description names Aureobasidium sp. HKI0318 as a production strain. Broad
    claimed SAP/HIV-protease uses and pharmaceutical formulations are not evidence
    of measured HIV enzyme inhibition, direct Sap binding, clinical efficacy or approval.
    The patent itself states that activity against the earlier general protease panel
    cannot simply establish SAP/HIV activity. No legal-status conclusion is made.
  snapshot_sha256: 5fb4c9b813ea2838f99057195ac1a11626f7c2609e91b91ee62a16b173ccec31
- evidence_id: candida
  kind: primary_source
  reference: PMID:18422912
  locator: DOI:10.1111/j.1439-0507.2008.01515.x; complete indexed abstract
  accessed_at: '2026-10-21T09:23:22Z'
  support: partial
  summary: The original study reports aureoquinone and laccaridiones reducing C. albicans
    adhesion and Sap release. It explicitly states these effects are not due to direct
    interaction with secreted Saps and that the compounds are neither fungistatic
    nor fungicidal at applied concentrations. These are antivirulence phenotypes,
    not direct Sap enzyme inhibition or fungal MICs. Full methods were unavailable,
    so no exact-concentration quantitative annotations are proposed.
  snapshot_sha256: 740c3fe1fca8f3bb36e4935e92783a4b0fccb25875e70fe2605d6e27f90d5ccd
- evidence_id: synthesis
  kind: primary_source
  reference: PMID:16438511
  locator: DOI:10.1021/jo0519561; complete indexed abstract
  accessed_at: '2026-10-21T09:23:22Z'
  support: partial
  summary: The 2006 synthesis explicitly identifies aureoquinone as 2,5,7,8-tetrahydroxy-3,6-dimethyl-1,4-naphthoquinone,
    corroborating native substitution. Hybocarpone and boryquinone are separate structures;
    their cytotoxicity is not aureoquinone antibacterial mechanism evidence.
  snapshot_sha256: 740c3fe1fca8f3bb36e4935e92783a4b0fccb25875e70fe2605d6e27f90d5ccd
- evidence_id: later-isolation
  kind: primary_source
  reference: PMID:38110564
  locator: DOI:10.1038/s41429-023-00688-x; complete indexed abstract
  accessed_at: '2026-10-21T09:23:22Z'
  support: context_only
  summary: The Talaromyces johnpittii MST-FP2594 study identifies aureoquinone as
    compound3 alongside talcarpones1 and2. The abstract antibacterial/fungal MIC ranges
    are explicitly for talcarpones1/2, not aureoquinone. It also reports conversion
    of talcarpone1 to3, so isolation alone does not independently prove a biosynthetic
    gene-level producer claim for3.
  snapshot_sha256: 740c3fe1fca8f3bb36e4935e92783a4b0fccb25875e70fe2605d6e27f90d5ccd
- evidence_id: adapter
  kind: database
  reference: Native iModulonDB adapter
  locator: 122-imodulondb-datasets.txt; executed before open-ended research
  accessed_at: '2026-10-21T09:23:22Z'
  support: context_only
  summary: The successful catalog retry returned bacterial/archaeal datasets without
    Aureobasidium or Candida coverage. The native definition gives no exact protease
    isoform or assay organism suitable for a target-specific query. No unrelated bacterial
    component is used as fungal or host mechanism evidence.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculations
  locator: 122-chemistry.json and actual focused validation logs
  accessed_at: '2026-10-21T09:23:22Z'
  support: supports
  summary: Both native encodings reproduce the full key, formula, neutral charge,
    one fragment, average and exact masses, and deterministic ChEBI mint. Schema and
    strict checks exit 0. Internal consistency does not by itself prove biological
    activity.
  snapshot_sha256: ef7ff57f88cfc962342af3fb477c20e96309cb0b4fa1876c120a81a036721e12
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 122-local-hits.txt and 122-maintained-search.txt
  accessed_at: '2026-10-21T09:23:22Z'
  support: context_only
  summary: Exact identity resolves to the native source row and readiness queue. No
    exact-target maintained override was found in the specified search. The aureoquinone
    numeric-ID search also returned an unrelated CRyPTIC measurement, which was rejected
    as a substring collision.
  search_scope: Initial rg --no-ignore --hidden search excluding .git/.venv; subsequent
    ignored-inclusive exact name, slug, ChEBI number and full-key-stem search across
    curation, conf, scripts, data/raw, src, reports and reviews. Free official database,
    Europe PMC and primary publisher follow-up; no exhaustive literature-absence assertion.
  snapshot_sha256: ef0f37550bcc6f368e2403e82a1e9d5c49da6d0323ebf34ec6c9afe23f959401
assessments:
- assessment_id: schema
  area: schema
  topic: Focused validation, provenance and native status
  outcome: supported
  summary: Actual checks pass and all 13 initial input hashes remain unchanged. A
    structured review does not promote native SEEDED status.
  target_ids:
  - CHEBI:65458
  evidence_ids:
  - native
  - source
  - chemistry
- assessment_id: identity
  area: identity
  topic: Native graph and source groundings
  outcome: supported
  summary: Original structure, synthesis abstract and current ChEBI corroborate the
    native graph. A differently represented name-resolved PubChem tautomer is not
    evidence of a native identity failure.
  target_ids:
  - CHEBI:65458
  evidence_ids:
  - identity
  - original-identity
  - synthesis
  - tautomer
  - chemistry
- assessment_id: activity
  area: evidence
  topic: Antibacterial and protease definition
  outcome: supported
  summary: Original purified-compound MIC and enzyme assays support the qualitative
    wording, with exact endpoint and method limits.
  target_ids:
  - CHEBI:65458
  evidence_ids:
  - antibacterial
  - proteases
- assessment_id: producer
  area: evidence
  topic: Aureobasidium surface-culture origin
  outcome: supported
  summary: Original isolated culture and fermentation support the generic source wording.
    Crepidotus host and later talcarpone decomposition must not be recast as proven
    biosynthesis by those taxa.
  target_ids:
  - CHEBI:65458
  evidence_ids:
  - original-identity
  - later-isolation
- assessment_id: patent
  area: evidence
  topic: Document resolution and experimental scope
  outcome: supported
  summary: The patent xref resolves. Its broad therapeutic claims are distinguishable
    from measured secretion/adhesion phenotypes and are not native approval assertions.
  target_ids:
  - CHEBI:65458
  evidence_ids:
  - patent
  - candida
- assessment_id: mechanism
  area: completeness
  topic: Optional target and antivirulence evidence
  outcome: unknown
  summary: There is no native false target claim. Protease assays, bacterial growth
    and Candida secretion/adhesion do not establish a single direct antimicrobial
    target or a shared causal chain.
  target_ids:
  - CHEBI:65458
  evidence_ids:
  - proteases
  - antibacterial
  - candida
  - adapter
findings:
- finding_id: F1
  issue_key: aureoquinone-primary-endpoint-scope-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Add exact primary evidence while preserving distinct biological endpoints
  description: The original paper directly supports chemical identity, cultured-fungus
    origin, one bacterial MIC and general protease inhibition. Candida secretion/adhesion
    and patent uses need separate evidence scope; optional enrichment does not imply
    a missing required field.
  target_ids:
  - CHEBI:65458
  field_paths:
  - evidence
  - activity_spectrum
  - molecular_targets
  - producing_organisms
  - discussions
  evidence_ids:
  - original-identity
  - antibacterial
  - proteases
  - patent
  - candida
  - later-isolation
  rule_id: 'native-review-checklist: Identity, Equivalence, Evidence and Completeness'
  native_severity: informational
  normalization_reason: The original paper directly supports chemical identity, cultured-fungus
    origin, one bacterial MIC and general protease inhibition. Candida secretion/adhesion
    and patent uses need separate evidence scope; optional enrichment does not imply
    a missing required field.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/aureoquinone.yaml
    role: Curator-owned exact primary activity, evidence and discussions
actions:
- action_id: A1
  description: Optionally curate primary identity and activity with explicit assay
    limits.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65458
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/aureoquinone.yaml
    role: Curator-owned exact primary activity, evidence and discussions
  acceptance_checks:
  - Retain the original neutral graph and exact B. subtilis ATCC6633 MIC120 µg/mL.
    Inspect the cited method before supplying missing medium, incubation or protocol
    details.
  - Preserve BODIPY-casein protease endpoints and measured units; resolve enzyme preparation/taxon
    before choosing specific protein accessions. Do not turn IC50 into binding Kd
    or bacterial MIC.
  - Retrieve full Candida methods before quantitative phenotype curation; the inspected
    abstract refutes direct secreted-Sap interaction as the explanation and reports
    no growth killing at tested concentrations.
  - Treat broad patent HIV/SAP claims and formulations as document context, not experimental
    target or approval evidence. Do not transfer talcarpone1/2 MICs to aureoquinone3.
  - Ground the actual Aureobasidium culture and retain taxonomic resolution limits
    if adding a producer object; use the maintained writer and claim-level primary
    evidence workflow.
limitations:
- The single adopted PMID has no indexed abstract; this gap was resolved by reading
  the complete three-page original paper and all page images. The cited full antimicrobial
  protocol and raw spectra/crystallographic data were not independently inspected.
- The patent text and examples were read in German and displayed English translation;
  structure/assay figures were not digitized and no graph-derived values are adopted.
  Patent legal status was not evaluated.
- The 2008 Candida, 2006 synthesis and 2024 isolation studies remain abstract-only.
  Europe PMC full-text XML returned 500; PMC HTML required browser verification, and
  Europe PMC/Wiley pages were inaccessible. These access failures do not establish
  absence of full text.
- The PubChem tautomer comparison hit the enumerator transformation limit; only the
  observed common candidate is reported. No exact-key absence claim beyond the specific
  404 response is made. Reaxys was not directly inspected.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 13 captured input hashes were rechecked unchanged. No native record was edited;
  absent optional fields are not treated as schema defects.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
