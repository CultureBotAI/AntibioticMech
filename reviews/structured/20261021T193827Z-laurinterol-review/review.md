# Laurinterol: supported antibacterial identity with a minor definition repair

- Review: 20261021T193827Z-laurinterol-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:16:37Z
- Finished UTC: 2026-10-21T19:38:27Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native brominated sesquiterpene is chemically valid and agrees with current ChEBI, PubChem, KEGG and an original structure drawing. Original mycobacterial and staphylococcal experiments support the antibacterial classification. One minor terminal-punctuation defect requires source-level repair. Host, protozoan and extract effects remain distinct from a demonstrated bacterial molecular target.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position596; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:66555 | data/antibiotics/antibacterial/laurinterol.yaml | generated | laurinterol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:66555 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:66555 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:66555 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:66555 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:66555 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:66555 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:66555 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:66555 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:66555 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:66555 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:66555 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:66555 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact parent, halogen and stereochemistry

identity: supported. Targets: CHEBI:66555.

All native/current-authority graphs agree with original2005 compound2 drawing and analytical characterization. Acetates, debrominated congeners, dimers and allolaurinterol remain distinct.

### Chemical references, parents and patent documents

grounding: unknown. Targets: CHEBI:66555.

KEGG exact chemistry and broader parents agree; CAS is publicly corroborated but the licensed registry and Reaxys graph were not inspected. Patent associations are correctly document-level.

### Antibacterial role and origin

evidence: supported. Targets: CHEBI:66555.

Original2005 staphylococcal inhibition and2020 mycobacterial tables support the coarse antibacterial role. Isolation from the sea hare is direct evidence of occurrence, not biosynthesis; historical algal attribution retains source-depth limits.

### Target causality and organism/material boundaries

evidence: supported. Targets: CHEBI:66555.

Native omission of optional target/graph fields is appropriate to the inspected evidence. ATPase hypotheses, host extracts, protozoan endpoints and related compounds cannot be merged into an established direct bacterial mechanism.

### Definition text and complete-field coverage

completeness: concern. Targets: CHEBI:66555.

The scientific description is broadly supported but the sentence has a terminal comma. All other populated fields and six citation leads are dispositioned; optional enrichment omissions are not findings.

## Findings

### F1: Finish the definition sentence with a period

minor / open / confirmed; issue key: laurinterol-definition-terminal-comma.

The source-derived definition ends with antibacterial activity followed by a comma. Repair the terminal punctuation in maintained source handling and regenerate, preserving the qualified occurrence and antibacterial meaning.

## Recommended Actions And Acceptance Checks

### A1

Repair the source-derived definition punctuation.

- Replace the terminal comma with a period through the maintained source path and verify regeneration preserves it.
- Rerun focused schema, strict and source-reproduction checks; do not alter the supported native graph or infer a producer biosynthesis claim.

### A2

Optional experimental enrichment with exact source and material boundaries.

- Retain the2005 disk-zone endpoint and the2020 exact strain/MIC/method information if adding activity objects; preserve the6.2/6.25 source rounding distinction.
- Inspect original enzyme Methods before adding a molecular target. Do not convert the2020 amoeba hypothesis, LOEL extract response or laurequinone mechanism into a proven bacterial laurinterol target.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/laurinterol.yaml; Entire native YAML, including definition, three parents, role, chemistry, all chemical/document references, source concept and four history events. | supports | CHEBI66555 is SEEDED/EXACT neutral C15H19BrO with key UGGAHNIITODSKB-ONERCXAPSA-N and three assigned centres. The definition describes isolation from Laurencia intermedia and Aplysia kurodai with antibacterial activity, but ends with a comma. No optional synonym, MIC, direct target, resistance, producer object, clinical indication or causal graph is asserted. |
| owners | data/raw/chebi_antimicrobials.tsv;conf/sources.yaml;scripts/extract_source_inventory.py;scripts/seed_from_sources.py; Complete exact source row, relevant field/reference routing and ignored-inclusive owner search. | supports | The maintained ChEBI row owns all source-derived native fields and six PMID leads. Patents are routed to document_xrefs, not exact chemical equivalence. The mint reproduces antibioticmech:chebi-d4401b2e20; four seed/reseed events are chronological. No exact curator/decision override was found in the inspected ignored/hidden-inclusive overlays. Original thirteen input hashes already capture the actual owners and remain unchanged. |
| authorities | CHEBI:66555;PubChem laurinterol;KEGG:C17136;CAS:10539-87-4;Reaxys:1880118; Current official ChEBI, PubChem properties, KEGG entry/molfile and independent chemistry. | supports | Seven native/current-authority encodings reproduce the native full key, formula, neutral charge and accurate R,R,S configuration. Exact mass294.06192733 and average295.22 agree with native precision. Phenol, organobromine-compound and sesquiterpenoid parents fit. KEGG repeats the CAS association; the licensed CAS registry API required authorization. Reaxys is consistently attributed by ChEBI but its exact registry graph was not independently inspected. |
| seahare2005 | DOI:10.3390/md302022;PMC3756325; Complete original scientific main, all three tables and actual introductory structure drawing viewed; compound2 distinguished from1/3/4. | supports | Purified laurinterol2 was isolated from Aplysia kurodai collected in Toyama Bay; the paper discusses dietary origin of sea-hare metabolites, not demonstrated animal biosynthesis. Original structure2 has Br and free phenolic OH, distinct from acetate1 and debrominated3/4. At50/25/12.5 micrograms per6-mm disk, compound2 gave S. aureus zones16/12/7 mm at37 degreesC. This is disk inhibition, not an MIC. Strain, inoculum, specific agar and incubation duration are not stated locally. HeLa IC50 32 micrograms/mL after three days is a host-cell endpoint. |
| mycobacteria2020 | PMID:32486286;DOI:10.3390/md18060287;PMC7345040; Complete scientific main, extraction/assay Methods and both original table texts read; figure caption read but original Figure1 image unavailable. | supports | Purified laurinterol from L. johnstonii was tested against nine M. tuberculosis and six NTM strains. Table1 ranges from25 to100 micrograms/mL, with C131 censored greater than100; H37Rv is100. Table2 gives6.2 micrograms/mL for three M. abscessus isolates,12.5 for M. fortuitum and one M. intracellulare isolate, and25 for the other M. intracellulare isolate. The conclusion rounds M. abscessus to6.25. Rapid growers used cation-adjusted Mueller-Hinton broth72h/37C; M. intracellulare used7H9/OADC7–10days. Mtb AlamarBlue method is referenced. Duplicate experiments and the prior macrophage toxicity source are retained. P-type ATPase discussion is a rationale, not a measured bacterial target. |
| antibacterial2004 | PMID:15549668;DOI:10.1055/s-2004-832653; Complete original indexed abstract; attempted full PDF routes returned HTML challenges. | supports | The paper tests halogenated Laurencia compounds against22 human-pathogen strains, seven antibiotic resistant. It specifically names laurinterol and allolaurinterol as bactericidal against three MRSA strains at3.13 micrograms/mL. Exact strain identities, detailed methods and full source-table assignment remain uninspected, so no new quantitative native observation is inferred from the abstract alone. |
| atpase2001 | PMID:11302194;DOI:10.1271/bbb.65.474; Complete original abstract; J-Stage full-text routes returned500. | supports | The principal new molecule is aplysiallene, but the abstract explicitly says isolated laurinterol and debromolaurinterol were also evaluated for Na,K-ATPase inhibition. This is an enzyme-context lead, not proof that a bacterial ATPase mediates antibacterial killing. Full enzyme source, constants and assay conditions were not independently inspected. |
| amoeba2020 | PMID:33082417;DOI:10.1038/s41598-020-74729-y;PMC7576160; Full original scientific main, Methods, Table1 and figure captions read; images and supplement not visually audited. | supports | N. fowleri ATCC30808 trophozoite growth/viability was measured by48h AlamarBlue at37C: laurinterol IC50 13.42±2.57 micromolar. Subsequent IC90 experiments measure ATP depletion, mitochondrial potential, ROS and membrane/nuclear responses. Although the title suggests ATPase inhibition, the main text presents ENA/ATP-competitive inhibition as a proposed mechanism needing further study: it compares whole-cell ouabain/furosemide responses and prior enzyme literature rather than measuring purified ENA binding or competition. Neither those responses nor a related allolaurinterol eIF4A experiment establishes a direct bacterial target. |
| other-adopted | PMID:18598167 DOI:10.1089/jmf.2007.575;PMID:37367658 DOI:10.3390/md21060333; Both complete original abstracts;2023 original figure captions additionally inspected. | supports | The2008 melanoma study tests Laurencia okamurai extract containing laurinterol, abbreviated LOEL; its p53/p21 and apoptotic effects must retain the extract material boundary. The2023 study measures laurinterol promastigote IC50 34.45 micromolar, but selects laurequinone for the detailed death-mechanism experiments. These host/protozoan outcomes are not antibacterial MICs or a laurinterol-specific causal chain. |
| patents | JPH08245359A;WO2009048195A1; Actual patent titles, abstracts and selected material/claim passages; Japanese text and supplied English translation inspected for scope. | context_only | The native JP8245359 lead resolves to a photoaging/skin-cosmetic patent covering laurinterol and debromolaurinterol, with selected purification text from L. okamurai. WO2009048195 describes laurinterol-related melanoma prevention/inhibition compositions. Both are relevant document associations. They are not exact chemical identifiers, approved clinical indications or independent antibacterial measurements; full patent claims/figures and legal status were not audited. |
| origin-search | 596-discovery-refined.json;596-local-hits.txt;596-owner-hits.txt;DOI:10.1016/S0040-4020(01)92906-0; Twenty refined discovery titles screened, all six adopted complete abstracts dispositioned, exact original/public authority follow-up and ignored-inclusive local search. | context_only | The1970 original Laurencia structure paper was identified through current source metadata and original references but its full text returned403. Current ChEBI associates Palisada intermedia with the historical Laurencia intermedia name. Sea-hare isolation is independently supported by the fully read2005 original. Additional related-congener, host and amoeba studies do not establish a new exact antibacterial target. The native lacks a gene/pathway assertion requiring structured-adapter lookup; later protozoan/host discussions do not match the bacterial adapter dataset. |

## Limits And Additional Notes

- The2005 and2020 mycobacterial full scientific texts and tables were read; only the2005 actual compound drawing was visually checked. The2020 mycobacterial image/PDF routes were inaccessible.
- The2020 amoeba full main and captions were read without image/SI audit. The1970 original,2001 enzyme and2004 antibacterial full papers were unavailable; the latter two were complete-abstract-only. The2008/2023 studies were abstract-level with stated2023 caption follow-up.
- Patents were inspected only for document/material relevance, not complete claims, legal interpretation or clinical efficacy. CAS/Reaxys registry limits and bounded discovery coverage remain explicit.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- The scratch filename596-seahare2004.xml contains the2005 published paper; actual publication year2005 is used throughout this review. All13 original source hashes remain unchanged. Native status and records were not modified; shared full-QC disposition follows at finalization.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T193827Z-laurinterol-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Laurinterol: supported antibacterial identity with a minor definition repair'
started_at: '2026-10-21T19:16:37Z'
finished_at: '2026-10-21T19:38:27Z'
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
summary: The native brominated sesquiterpene is chemically valid and agrees with current
  ChEBI, PubChem, KEGG and an original structure drawing. Original mycobacterial and
  staphylococcal experiments support the antibacterial classification. One minor terminal-punctuation
  defect requires source-level repair. Host, protozoan and extract effects remain
  distinct from a demonstrated bacterial molecular target.
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
  - path: data/antibiotics/antibacterial/laurinterol.yaml
    sha256: 70ad77ac34b691169513541824708815db76efbe4037edac23846d99b1f77c05
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
- target_id: CHEBI:66555
  path: data/antibiotics/antibacterial/laurinterol.yaml
  label: laurinterol
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
  selection: Initially uncovered queue position596; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:66555
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:66555
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    596
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:66555
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/laurinterol.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:66555
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/laurinterol.yaml --out /private/tmp/am-review-session/596-strict.tsv
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
  - CHEBI:66555
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
  - CHEBI:66555
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
  - CHEBI:66555
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
  - CHEBI:66555
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
  - CHEBI:66555
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
  - CHEBI:66555
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
  - CHEBI:66555
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
  - CHEBI:66555
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
  - CHEBI:66555
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/laurinterol.yaml
  locator: Entire native YAML, including definition, three parents, role, chemistry,
    all chemical/document references, source concept and four history events.
  accessed_at: '2026-10-21T19:36:51Z'
  support: supports
  summary: CHEBI66555 is SEEDED/EXACT neutral C15H19BrO with key UGGAHNIITODSKB-ONERCXAPSA-N
    and three assigned centres. The definition describes isolation from Laurencia
    intermedia and Aplysia kurodai with antibacterial activity, but ends with a comma.
    No optional synonym, MIC, direct target, resistance, producer object, clinical
    indication or causal graph is asserted.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv;conf/sources.yaml;scripts/extract_source_inventory.py;scripts/seed_from_sources.py
  locator: Complete exact source row, relevant field/reference routing and ignored-inclusive
    owner search.
  accessed_at: '2026-10-21T19:36:51Z'
  support: supports
  summary: The maintained ChEBI row owns all source-derived native fields and six
    PMID leads. Patents are routed to document_xrefs, not exact chemical equivalence.
    The mint reproduces antibioticmech:chebi-d4401b2e20; four seed/reseed events are
    chronological. No exact curator/decision override was found in the inspected ignored/hidden-inclusive
    overlays. Original thirteen input hashes already capture the actual owners and
    remain unchanged.
  snapshot_sha256: 2e9ffdf23f5b8b6255ae44a9c9c79d6fa51550ed9724e010f42dc679e751a0ed
- evidence_id: authorities
  kind: authority
  reference: CHEBI:66555;PubChem laurinterol;KEGG:C17136;CAS:10539-87-4;Reaxys:1880118
  locator: Current official ChEBI, PubChem properties, KEGG entry/molfile and independent
    chemistry.
  accessed_at: '2026-10-21T19:36:51Z'
  support: supports
  summary: Seven native/current-authority encodings reproduce the native full key,
    formula, neutral charge and accurate R,R,S configuration. Exact mass294.06192733
    and average295.22 agree with native precision. Phenol, organobromine-compound
    and sesquiterpenoid parents fit. KEGG repeats the CAS association; the licensed
    CAS registry API required authorization. Reaxys is consistently attributed by
    ChEBI but its exact registry graph was not independently inspected.
  snapshot_sha256: 6f9b4e94c432a0bd143e5b917f2a813453d7d1b99f3fe8566184323158a72479
- evidence_id: seahare2005
  kind: primary_source
  reference: DOI:10.3390/md302022;PMC3756325
  locator: Complete original scientific main, all three tables and actual introductory
    structure drawing viewed; compound2 distinguished from1/3/4.
  accessed_at: '2026-10-21T19:36:51Z'
  support: supports
  summary: Purified laurinterol2 was isolated from Aplysia kurodai collected in Toyama
    Bay; the paper discusses dietary origin of sea-hare metabolites, not demonstrated
    animal biosynthesis. Original structure2 has Br and free phenolic OH, distinct
    from acetate1 and debrominated3/4. At50/25/12.5 micrograms per6-mm disk, compound2
    gave S. aureus zones16/12/7 mm at37 degreesC. This is disk inhibition, not an
    MIC. Strain, inoculum, specific agar and incubation duration are not stated locally.
    HeLa IC50 32 micrograms/mL after three days is a host-cell endpoint.
  snapshot_sha256: a7f6c2f2c114c106dbd83e50521b6706f29d9d44e06383dcedb5d6ffe37dad3d
- evidence_id: mycobacteria2020
  kind: primary_source
  reference: PMID:32486286;DOI:10.3390/md18060287;PMC7345040
  locator: Complete scientific main, extraction/assay Methods and both original table
    texts read; figure caption read but original Figure1 image unavailable.
  accessed_at: '2026-10-21T19:36:51Z'
  support: supports
  summary: Purified laurinterol from L. johnstonii was tested against nine M. tuberculosis
    and six NTM strains. Table1 ranges from25 to100 micrograms/mL, with C131 censored
    greater than100; H37Rv is100. Table2 gives6.2 micrograms/mL for three M. abscessus
    isolates,12.5 for M. fortuitum and one M. intracellulare isolate, and25 for the
    other M. intracellulare isolate. The conclusion rounds M. abscessus to6.25. Rapid
    growers used cation-adjusted Mueller-Hinton broth72h/37C; M. intracellulare used7H9/OADC7–10days.
    Mtb AlamarBlue method is referenced. Duplicate experiments and the prior macrophage
    toxicity source are retained. P-type ATPase discussion is a rationale, not a measured
    bacterial target.
  snapshot_sha256: ae110f90a563f11473392c11b195d939718eaa3642538cec977b64a4ada1d98e
- evidence_id: antibacterial2004
  kind: primary_source
  reference: PMID:15549668;DOI:10.1055/s-2004-832653
  locator: Complete original indexed abstract; attempted full PDF routes returned
    HTML challenges.
  accessed_at: '2026-10-21T19:36:51Z'
  support: supports
  summary: The paper tests halogenated Laurencia compounds against22 human-pathogen
    strains, seven antibiotic resistant. It specifically names laurinterol and allolaurinterol
    as bactericidal against three MRSA strains at3.13 micrograms/mL. Exact strain
    identities, detailed methods and full source-table assignment remain uninspected,
    so no new quantitative native observation is inferred from the abstract alone.
  snapshot_sha256: 0a3e3e0bceb5bb980c7f7ba9a4ff7ffd727077fde656d5cf0c6fcfe55d98841b
- evidence_id: atpase2001
  kind: primary_source
  reference: PMID:11302194;DOI:10.1271/bbb.65.474
  locator: Complete original abstract; J-Stage full-text routes returned500.
  accessed_at: '2026-10-21T19:36:51Z'
  support: supports
  summary: The principal new molecule is aplysiallene, but the abstract explicitly
    says isolated laurinterol and debromolaurinterol were also evaluated for Na,K-ATPase
    inhibition. This is an enzyme-context lead, not proof that a bacterial ATPase
    mediates antibacterial killing. Full enzyme source, constants and assay conditions
    were not independently inspected.
  snapshot_sha256: 0a3e3e0bceb5bb980c7f7ba9a4ff7ffd727077fde656d5cf0c6fcfe55d98841b
- evidence_id: amoeba2020
  kind: primary_source
  reference: PMID:33082417;DOI:10.1038/s41598-020-74729-y;PMC7576160
  locator: Full original scientific main, Methods, Table1 and figure captions read;
    images and supplement not visually audited.
  accessed_at: '2026-10-21T19:36:51Z'
  support: supports
  summary: 'N. fowleri ATCC30808 trophozoite growth/viability was measured by48h AlamarBlue
    at37C: laurinterol IC50 13.42±2.57 micromolar. Subsequent IC90 experiments measure
    ATP depletion, mitochondrial potential, ROS and membrane/nuclear responses. Although
    the title suggests ATPase inhibition, the main text presents ENA/ATP-competitive
    inhibition as a proposed mechanism needing further study: it compares whole-cell
    ouabain/furosemide responses and prior enzyme literature rather than measuring
    purified ENA binding or competition. Neither those responses nor a related allolaurinterol
    eIF4A experiment establishes a direct bacterial target.'
  snapshot_sha256: b82eacd8224ff585aab0bf937917666b68a804d196ffc993bd8634a9021acf82
- evidence_id: other-adopted
  kind: primary_source
  reference: PMID:18598167 DOI:10.1089/jmf.2007.575;PMID:37367658 DOI:10.3390/md21060333
  locator: Both complete original abstracts;2023 original figure captions additionally
    inspected.
  accessed_at: '2026-10-21T19:36:51Z'
  support: supports
  summary: The2008 melanoma study tests Laurencia okamurai extract containing laurinterol,
    abbreviated LOEL; its p53/p21 and apoptotic effects must retain the extract material
    boundary. The2023 study measures laurinterol promastigote IC50 34.45 micromolar,
    but selects laurequinone for the detailed death-mechanism experiments. These host/protozoan
    outcomes are not antibacterial MICs or a laurinterol-specific causal chain.
  snapshot_sha256: 0a3e3e0bceb5bb980c7f7ba9a4ff7ffd727077fde656d5cf0c6fcfe55d98841b
- evidence_id: patents
  kind: primary_source
  reference: JPH08245359A;WO2009048195A1
  locator: Actual patent titles, abstracts and selected material/claim passages; Japanese
    text and supplied English translation inspected for scope.
  accessed_at: '2026-10-21T19:36:51Z'
  support: context_only
  summary: The native JP8245359 lead resolves to a photoaging/skin-cosmetic patent
    covering laurinterol and debromolaurinterol, with selected purification text from
    L. okamurai. WO2009048195 describes laurinterol-related melanoma prevention/inhibition
    compositions. Both are relevant document associations. They are not exact chemical
    identifiers, approved clinical indications or independent antibacterial measurements;
    full patent claims/figures and legal status were not audited.
  snapshot_sha256: 0e46a05e0ec1de3612afba59ed0494c6e8eb6faa1ef4a12b4fdf51c3d68d0871
- evidence_id: origin-search
  kind: search
  reference: 596-discovery-refined.json;596-local-hits.txt;596-owner-hits.txt;DOI:10.1016/S0040-4020(01)92906-0
  locator: Twenty refined discovery titles screened, all six adopted complete abstracts
    dispositioned, exact original/public authority follow-up and ignored-inclusive
    local search.
  accessed_at: '2026-10-21T19:36:51Z'
  support: context_only
  summary: The1970 original Laurencia structure paper was identified through current
    source metadata and original references but its full text returned403. Current
    ChEBI associates Palisada intermedia with the historical Laurencia intermedia
    name. Sea-hare isolation is independently supported by the fully read2005 original.
    Additional related-congener, host and amoeba studies do not establish a new exact
    antibacterial target. The native lacks a gene/pathway assertion requiring structured-adapter
    lookup; later protozoan/host discussions do not match the bacterial adapter dataset.
  search_scope: 2026-10-21; laurinterol, CHEBI66555, full key, all six adopted PMIDs,1970
    original DOI and source patents; ignored/hidden-inclusive maintained searches.
  snapshot_sha256: 0cdc76daae3754deafae45233d5b72d3a5bf6449735ffe9eb4c623ccd96388ea
assessments:
- assessment_id: identity
  area: identity
  topic: Exact parent, halogen and stereochemistry
  outcome: supported
  summary: All native/current-authority graphs agree with original2005 compound2 drawing
    and analytical characterization. Acetates, debrominated congeners, dimers and
    allolaurinterol remain distinct.
  target_ids:
  - CHEBI:66555
  evidence_ids:
  - native
  - authorities
  - seahare2005
- assessment_id: grounding
  area: grounding
  topic: Chemical references, parents and patent documents
  outcome: unknown
  summary: KEGG exact chemistry and broader parents agree; CAS is publicly corroborated
    but the licensed registry and Reaxys graph were not inspected. Patent associations
    are correctly document-level.
  target_ids:
  - CHEBI:66555
  evidence_ids:
  - authorities
  - patents
- assessment_id: activity
  area: evidence
  topic: Antibacterial role and origin
  outcome: supported
  summary: Original2005 staphylococcal inhibition and2020 mycobacterial tables support
    the coarse antibacterial role. Isolation from the sea hare is direct evidence
    of occurrence, not biosynthesis; historical algal attribution retains source-depth
    limits.
  target_ids:
  - CHEBI:66555
  evidence_ids:
  - seahare2005
  - mycobacteria2020
  - antibacterial2004
  - origin-search
- assessment_id: mechanism
  area: evidence
  topic: Target causality and organism/material boundaries
  outcome: supported
  summary: Native omission of optional target/graph fields is appropriate to the inspected
    evidence. ATPase hypotheses, host extracts, protozoan endpoints and related compounds
    cannot be merged into an established direct bacterial mechanism.
  target_ids:
  - CHEBI:66555
  evidence_ids:
  - atpase2001
  - amoeba2020
  - other-adopted
- assessment_id: definition
  area: completeness
  topic: Definition text and complete-field coverage
  outcome: concern
  summary: The scientific description is broadly supported but the sentence has a
    terminal comma. All other populated fields and six citation leads are dispositioned;
    optional enrichment omissions are not findings.
  target_ids:
  - CHEBI:66555
  evidence_ids:
  - native
  - owners
  - origin-search
findings:
- finding_id: F1
  issue_key: laurinterol-definition-terminal-comma
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Finish the definition sentence with a period
  description: The source-derived definition ends with antibacterial activity followed
    by a comma. Repair the terminal punctuation in maintained source handling and
    regenerate, preserving the qualified occurrence and antibacterial meaning.
  target_ids:
  - CHEBI:66555
  field_paths:
  - definition
  evidence_ids:
  - native
  - owners
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted definition and source identity
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI definition extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition emission
  rule_id: Definitions should be complete readable sentences
  native_severity: minor
  normalization_reason: This is a bounded text defect without a wrong identity or
    scientific activity assertion.
actions:
- action_id: A1
  description: Repair the source-derived definition punctuation.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:66555
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted definition and source identity
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI definition extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition emission
  acceptance_checks:
  - Replace the terminal comma with a period through the maintained source path and
    verify regeneration preserves it.
  - Rerun focused schema, strict and source-reproduction checks; do not alter the
    supported native graph or infer a producer biosynthesis claim.
- action_id: A2
  description: Optional experimental enrichment with exact source and material boundaries.
  finding_ids: []
  target_ids:
  - CHEBI:66555
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted definition and source identity
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI definition extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition emission
  acceptance_checks:
  - Retain the2005 disk-zone endpoint and the2020 exact strain/MIC/method information
    if adding activity objects; preserve the6.2/6.25 source rounding distinction.
  - Inspect original enzyme Methods before adding a molecular target. Do not convert
    the2020 amoeba hypothesis, LOEL extract response or laurequinone mechanism into
    a proven bacterial laurinterol target.
limitations:
- The2005 and2020 mycobacterial full scientific texts and tables were read; only the2005
  actual compound drawing was visually checked. The2020 mycobacterial image/PDF routes
  were inaccessible.
- The2020 amoeba full main and captions were read without image/SI audit. The1970
  original,2001 enzyme and2004 antibacterial full papers were unavailable; the latter
  two were complete-abstract-only. The2008/2023 studies were abstract-level with stated2023
  caption follow-up.
- Patents were inspected only for document/material relevance, not complete claims,
  legal interpretation or clinical efficacy. CAS/Reaxys registry limits and bounded
  discovery coverage remain explicit.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- The scratch filename596-seahare2004.xml contains the2005 published paper; actual
  publication year2005 is used throughout this review. All13 original source hashes
  remain unchanged. Native status and records were not modified; shared full-QC disposition
  follows at finalization.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
