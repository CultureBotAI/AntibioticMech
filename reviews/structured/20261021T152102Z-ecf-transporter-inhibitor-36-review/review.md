# ECF transporter inhibitor36: original structure and assay claims corroborated

- Review: 20261021T152102Z-ecf-transporter-inhibitor-36-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:52:16Z
- Finished UTC: 2026-10-21T15:21:02Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Official supplementary CSV row36 reproduces the native SMILES exactly, and the original Scheme5, synthetic characterization and transport/MIC results support this proposed record. Purified transporter inhibition, whole-cell uptake and strain-specific growth results are distinct endpoints. Supplementary unit/species-label inconsistencies are retained as limits on future detailed extraction. No confirmed native correction is established. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position390; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:curator-34020091be | data/antibiotics/antibacterial/ecf-transporter-inhibitor-36.yaml | generated | ECF transporter inhibitor 36 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:curator-34020091be | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:curator-34020091be | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:curator-34020091be | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:curator-34020091be | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:curator-34020091be | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:curator-34020091be | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:curator-34020091be | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:curator-34020091be | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:curator-34020091be | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:curator-34020091be | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:curator-34020091be | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:curator-34020091be | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact published compound36 structure

identity: supported. Targets: antibioticmech:curator-34020091be.

The maintained chemical string is the exact official supplementary row, corroborated by Scheme5 and characterization. Compound36 is publication-scoped; no global uniqueness of that bare number is implied.

### Scaffold description and antibacterial eligibility

evidence: supported. Targets: antibioticmech:curator-34020091be.

The description uses the paper’s1,4-substitution shorthand for its1,2,3-triazole scaffold and is consistent with the graph. Original pure-compound growth results directly support the antibacterial role.

### Native source-concept panel and transport statements

evidence: supported. Targets: antibioticmech:curator-34020091be.

The reported0.5–4 micrograms/mL range and42.84 micromolar IC50 agree with Table5 and refer to different assay systems. The distinct ATCC51559 result does not contradict that bounded panel.

### Supplement inconsistencies before detailed curation

completeness: unknown. Targets: antibioticmech:curator-34020091be.

Unit and species-label conflicts in the SI should be resolved or explicitly preserved before adding structured strain observations. They do not establish that the current Table5-derived native statement is false.

### Functional inhibition versus direct molecular causality

evidence: supported. Targets: antibioticmech:curator-34020091be.

A reconstituted transporter assay supports functional inhibition; specific contacts are computational. No native target or graph overstates those claims.

### Clinical, resistance and microbial origin fields

scope: not_applicable. Targets: antibioticmech:curator-34020091be.

The synthetic proposed compound has no such native claims. VRE/PRSP labels describe comparator-drug resistance, not resistance to compound36. Infection-model activity is not clinical efficacy or approval.

### Maintained curator source and reproducible identifier

provenance: supported. Targets: antibioticmech:curator-34020091be.

All fourteen inputs and the exact row reproduce; MINTED/PROPOSED appropriately retain a publication-scoped experimental compound.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optional future structured assay curation should preserve the original endpoint and source-discrepancy boundaries.

- Retain the exact official row36 structure, publication scope and neutral form.
- Keep Table5 mass units and strain panel separate from SI micromolar labels and the ATCC51559 time-kill experiment; document unresolved source disagreements.
- Represent ECF transport inhibition as a functional assay; keep docking affinities, contacts and prior-series genetics distinct from direct36 binding or causal evidence.
- Do not interpret model survival or comparator-drug-resistant strain names as clinical approval or resistance to36.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/ecf-transporter-inhibitor-36.yaml; Entire native YAML including source-concept evidence and single proposal history | supports | The PROPOSED/MINTED record encodes neutral C28H29ClN4O5, KBHNQPNHOFMZND-UHFFFAOYSA-N, one source-qualified compound36 alias and no external exact accession. Its source evidence reports a0.5–4 micrograms/mL bacterial panel range and42.84 micromolar ECF-FolT2 IC50. No molecular-target object, native quantitative measurement, resistance assertion, clinical status or causal graph is populated. |
| owners | curation/curator_antibiotics.tsv; scripts/seed_from_sources.py; Curator row31; readiness row2661;390-source-rows.json; original13 inputs plus readiness context | supports | The exact DOI#36 curator row supplies the structure, definition, source evidence and scoped compound number. The deterministic CURATOR mint and one PROPOSED_FROM_CURATOR_INVENTORY event reproduce. Fourteen captured source hashes remain unchanged. |
| chemical-primary | DOI:10.1021/acs.jmedchem.5c02721; DOI:10.1021/acs.jmedchem.5c02721.s002; Original Scheme5 visually inspected; compound36 experimental paragraph; official jm5c02721_si_002.csv row36 | supports | The official row36 SMILES is byte-for-byte identical to the native value. Scheme5 shows the1,4-disubstituted1,2,3-triazole with tert-butyl, chloropyridinyl/isopropoxy and salicylic-acid groups. The synthesis describes isolated36 and HRMS of [M–H]− consistent with the neutral formula. No salt or unspecified stereocentre is introduced. |
| chemistry | Independent RDKit2026.03.5 / InChI1.07.3; 039-root-authority.py;390-authority-chemistry.json;390-exact-csv-row.json | supports | Native SMILES, native InChI and official CSV structure all reproduce full key, formula, charge, masses and chirality-aware graph equivalence. The retrieved CSV is semicolon-delimited and Latin-1 encoded; an initial UTF-8 display failed before correct decoding. Official Figshare metadata MD5 values match both downloaded supplements. |
| characterization | DOI:10.1021/acs.jmedchem.5c02721.s001; Official SI physicalp22/printedp19 NMR plots visually inspected; main experimental paragraph36 | context_only | The supplement explicitly labels36 and shows its proton/carbon spectra. The displayed chemical shifts agree in broad placement with the main characterization; raw spectra were not reprocessed and no independent reassignment of all peaks or purity percentage is claimed. |
| primary-assays | PMID:42249838; PMC13312448; DOI:10.1021/acs.jmedchem.5c02721; Main Table5, Table4 image, biological Results; SI3.1–3.4 | supports | Table5 gives compound36 MICs2–4,2,1–2,1,0.5–1 micrograms/mL for E. faecalis DSM20478, E. faecium DSM17050/20477 and S. pneumoniae DSM11865/20566, respectively, and ECF-FolT2 IC5042.84 micromolar. Table4 gives L. casei uptake IC507±0.3 micromolar. SI describes radiolabeled folate/pantothenate transport in L. delbrueckii proteoliposomes and a separate L. casei uptake assay. These corroborate the native bounded claims; uptake IC50 is not a binding constant. |
| source-discrepancy | Original Table5; SI TableS2/FigureS2; official CSVrow36; SI physicalp11/printedp8 inspected visually;390-si-p11.png;390-exact-csv-row.json | context_only | SI TableS2 labels MICs micromolar while its FigureS2 axis uses micrograms/mL, and labels DSM20478 E. faecium whereas Table5/CSV label it E. faecalis. CSV point values lie within Table5 ranges but do not reproduce every SI number under a simple unit conversion. Native evidence accurately reflects Table5; detailed future extraction must preserve or resolve these source inconsistencies rather than silently normalizing them. |
| mechanism-boundary | DOI:10.1021/acs.jmedchem.5c02721; Main docking, transport discussion and Conclusions; SI2.1–2.2 | context_only | Transport inhibition supports the ECF-inhibitor label. Docking uses the apo6ZG3 structure and predicts an interface pose; its scores and contacts are not experimental binding affinities or a compound-bound structure. Whole-cell growth and survival outcomes do not independently prove that a unique ECF binding event caused all activity. Prior-series CRISPR findings are not automatically compound36 evidence. |
| additional-endpoints | DOI:10.1021/acs.jmedchem.5c02721; Main time-kill/in-vivo Results and SI3.5/5; inspected main ADMET context | context_only | A separate E. faecium ATCC51559 experiment uses MIC8.6 micrograms/mL and higher multiples for time-kill measurements, outside the five-strain Table5 panel. Larval and zebrafish studies have distinct strains, exposure and endpoints; improved model survival is not clinical approval or proof of a molecular mechanism. No host-safety or broad efficacy conclusion is imported. |
| adapter | iModulonDB s_pneumoniae/precise718; 390-adapter-results.json;390-adapter-pneumoniae-results.json; dataset catalog before primary mechanism follow-up | context_only | The first representative E. coli searches returned no ECF/folate-transport hits. The organism-matched S. pneumoniae dataset resolves ecfT/SP2219, ecfA2/SP2220 and ecfA1/SP2221; recF is a string-match near miss. Folate biosynthesis hits are not FolT transport targets, and FolT search returned none. No L. delbrueckii dataset was in the catalog. Adapter results are gene-context only, not drug-binding evidence. |
| access | Exact DOI, original supplements and maintained owner search; 039-root-fetch manifests;390-si-meta.json;390-sipdf-meta.json;390-owners-search.json | supports | Publisher routes returned403; the full original XML and figure images were recovered through PMC, and both free official supplements through ACS Figshare with matching resource DOI and checksums. No inaccessible route is treated as missing evidence. Only the exact36 material and relevant assay/model sections were inspected; other compounds are comparison context. |

## Limits And Additional Notes

- The original main sections relevant to compound36, Scheme5, Table4, Table5 and SI assay protocols were read. The NMR plot was visually inspected, but raw spectra, docking trajectories and all comparison compounds were not independently reprocessed.
- SI TableS2 and FigureS2 use inconsistent MIC unit labels and disagree on DSM20478 species naming with the main table/CSV. No detailed native numeric observation was imported from these conflicting representations.
- The source-concept claim is Table5-derived. A separate strain’s8.6 micrograms/mL MIC and model-survival experiments retain their own scope.
- Reconstituted transport inhibition is not direct affinity measurement; the apo-protein docking pose is predictive, and phenotypic activity does not by itself identify a unique causal binding event.
- The structured adapter initially queried a nonmatching representative organism; the subsequent S. pneumoniae query provides relevant gene context but not L. delbrueckii target proof. Zero search hits are not proof that transport machinery is absent.
- No native or maintained source was edited. Shared required validation outcomes are attached separately.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T152102Z-ecf-transporter-inhibitor-36-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'ECF transporter inhibitor36: original structure and assay claims corroborated'
started_at: '2026-10-21T14:52:16Z'
finished_at: '2026-10-21T15:21:02Z'
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
summary: Official supplementary CSV row36 reproduces the native SMILES exactly, and
  the original Scheme5, synthetic characterization and transport/MIC results support
  this proposed record. Purified transporter inhibition, whole-cell uptake and strain-specific
  growth results are distinct endpoints. Supplementary unit/species-label inconsistencies
  are retained as limits on future detailed extraction. No confirmed native correction
  is established. Scientific assessment retains the stated evidence limits; full verification
  is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/ecf-transporter-inhibitor-36.yaml
    sha256: 0547a8ff15a920c52a73114cf1e4e0e4d09a227f76d025d398efbad241859d96
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
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
    role: context
targets:
- target_id: antibioticmech:curator-34020091be
  path: data/antibiotics/antibacterial/ecf-transporter-inhibitor-36.yaml
  label: ECF transporter inhibitor 36
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
  selection: Initially uncovered queue position390; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:curator-34020091be
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-34020091be
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    390
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-34020091be
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/ecf-transporter-inhibitor-36.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-34020091be
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/ecf-transporter-inhibitor-36.yaml --out /private/tmp/am-review-session/390-strict.tsv
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
  - antibioticmech:curator-34020091be
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
  - antibioticmech:curator-34020091be
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
  - antibioticmech:curator-34020091be
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
  - antibioticmech:curator-34020091be
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
  - antibioticmech:curator-34020091be
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
  - antibioticmech:curator-34020091be
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
  - antibioticmech:curator-34020091be
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
  - antibioticmech:curator-34020091be
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
  - antibioticmech:curator-34020091be
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/ecf-transporter-inhibitor-36.yaml
  locator: Entire native YAML including source-concept evidence and single proposal
    history
  accessed_at: '2026-10-21T15:01:09Z'
  support: supports
  summary: The PROPOSED/MINTED record encodes neutral C28H29ClN4O5, KBHNQPNHOFMZND-UHFFFAOYSA-N,
    one source-qualified compound36 alias and no external exact accession. Its source
    evidence reports a0.5–4 micrograms/mL bacterial panel range and42.84 micromolar
    ECF-FolT2 IC50. No molecular-target object, native quantitative measurement, resistance
    assertion, clinical status or causal graph is populated.
- evidence_id: owners
  kind: record_content
  reference: curation/curator_antibiotics.tsv; scripts/seed_from_sources.py
  locator: Curator row31; readiness row2661;390-source-rows.json; original13 inputs
    plus readiness context
  accessed_at: '2026-10-21T15:01:09Z'
  support: supports
  summary: The exact DOI#36 curator row supplies the structure, definition, source
    evidence and scoped compound number. The deterministic CURATOR mint and one PROPOSED_FROM_CURATOR_INVENTORY
    event reproduce. Fourteen captured source hashes remain unchanged.
  snapshot_sha256: 2c5811ea8219c8cc312af56a23562185be026ad86c6a8b85926e1f42b63cdffc
- evidence_id: chemical-primary
  kind: primary_source
  reference: DOI:10.1021/acs.jmedchem.5c02721; DOI:10.1021/acs.jmedchem.5c02721.s002
  locator: Original Scheme5 visually inspected; compound36 experimental paragraph;
    official jm5c02721_si_002.csv row36
  accessed_at: '2026-10-21T15:01:09Z'
  support: supports
  summary: The official row36 SMILES is byte-for-byte identical to the native value.
    Scheme5 shows the1,4-disubstituted1,2,3-triazole with tert-butyl, chloropyridinyl/isopropoxy
    and salicylic-acid groups. The synthesis describes isolated36 and HRMS of [M–H]−
    consistent with the neutral formula. No salt or unspecified stereocentre is introduced.
  snapshot_sha256: 3d4d344a8f3a0a33e0fc715dd9a12e164e18ba9263481541a67a02cfd52a65fb
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit2026.03.5 / InChI1.07.3
  locator: 039-root-authority.py;390-authority-chemistry.json;390-exact-csv-row.json
  accessed_at: '2026-10-21T15:01:09Z'
  support: supports
  summary: Native SMILES, native InChI and official CSV structure all reproduce full
    key, formula, charge, masses and chirality-aware graph equivalence. The retrieved
    CSV is semicolon-delimited and Latin-1 encoded; an initial UTF-8 display failed
    before correct decoding. Official Figshare metadata MD5 values match both downloaded
    supplements.
  snapshot_sha256: 8d082de1892defdb18eefeca4be89b4a6fd8774b4fb2012c274f64e514d4541a
- evidence_id: characterization
  kind: primary_source
  reference: DOI:10.1021/acs.jmedchem.5c02721.s001
  locator: Official SI physicalp22/printedp19 NMR plots visually inspected; main experimental
    paragraph36
  accessed_at: '2026-10-21T15:01:09Z'
  support: context_only
  summary: The supplement explicitly labels36 and shows its proton/carbon spectra.
    The displayed chemical shifts agree in broad placement with the main characterization;
    raw spectra were not reprocessed and no independent reassignment of all peaks
    or purity percentage is claimed.
  snapshot_sha256: dee5af5a9db9811b2136a3573f43b6954ea1e1f888c9123c0dd60412ceb155d5
- evidence_id: primary-assays
  kind: primary_source
  reference: PMID:42249838; PMC13312448; DOI:10.1021/acs.jmedchem.5c02721
  locator: Main Table5, Table4 image, biological Results; SI3.1–3.4
  accessed_at: '2026-10-21T15:01:09Z'
  support: supports
  summary: Table5 gives compound36 MICs2–4,2,1–2,1,0.5–1 micrograms/mL for E. faecalis
    DSM20478, E. faecium DSM17050/20477 and S. pneumoniae DSM11865/20566, respectively,
    and ECF-FolT2 IC5042.84 micromolar. Table4 gives L. casei uptake IC507±0.3 micromolar.
    SI describes radiolabeled folate/pantothenate transport in L. delbrueckii proteoliposomes
    and a separate L. casei uptake assay. These corroborate the native bounded claims;
    uptake IC50 is not a binding constant.
  snapshot_sha256: 585985b4faced7e8caecf4798583e93f2d4b7292588b875d7ba43c3960a36b96
- evidence_id: source-discrepancy
  kind: primary_source
  reference: Original Table5; SI TableS2/FigureS2; official CSVrow36
  locator: SI physicalp11/printedp8 inspected visually;390-si-p11.png;390-exact-csv-row.json
  accessed_at: '2026-10-21T15:01:09Z'
  support: context_only
  summary: SI TableS2 labels MICs micromolar while its FigureS2 axis uses micrograms/mL,
    and labels DSM20478 E. faecium whereas Table5/CSV label it E. faecalis. CSV point
    values lie within Table5 ranges but do not reproduce every SI number under a simple
    unit conversion. Native evidence accurately reflects Table5; detailed future extraction
    must preserve or resolve these source inconsistencies rather than silently normalizing
    them.
  snapshot_sha256: dee5af5a9db9811b2136a3573f43b6954ea1e1f888c9123c0dd60412ceb155d5
- evidence_id: mechanism-boundary
  kind: primary_source
  reference: DOI:10.1021/acs.jmedchem.5c02721
  locator: Main docking, transport discussion and Conclusions; SI2.1–2.2
  accessed_at: '2026-10-21T15:01:09Z'
  support: context_only
  summary: Transport inhibition supports the ECF-inhibitor label. Docking uses the
    apo6ZG3 structure and predicts an interface pose; its scores and contacts are
    not experimental binding affinities or a compound-bound structure. Whole-cell
    growth and survival outcomes do not independently prove that a unique ECF binding
    event caused all activity. Prior-series CRISPR findings are not automatically
    compound36 evidence.
  snapshot_sha256: 585985b4faced7e8caecf4798583e93f2d4b7292588b875d7ba43c3960a36b96
- evidence_id: additional-endpoints
  kind: primary_source
  reference: DOI:10.1021/acs.jmedchem.5c02721
  locator: Main time-kill/in-vivo Results and SI3.5/5; inspected main ADMET context
  accessed_at: '2026-10-21T15:01:09Z'
  support: context_only
  summary: A separate E. faecium ATCC51559 experiment uses MIC8.6 micrograms/mL and
    higher multiples for time-kill measurements, outside the five-strain Table5 panel.
    Larval and zebrafish studies have distinct strains, exposure and endpoints; improved
    model survival is not clinical approval or proof of a molecular mechanism. No
    host-safety or broad efficacy conclusion is imported.
  snapshot_sha256: 585985b4faced7e8caecf4798583e93f2d4b7292588b875d7ba43c3960a36b96
- evidence_id: adapter
  kind: database
  reference: iModulonDB s_pneumoniae/precise718
  locator: 390-adapter-results.json;390-adapter-pneumoniae-results.json; dataset catalog
    before primary mechanism follow-up
  accessed_at: '2026-10-21T15:01:09Z'
  support: context_only
  summary: The first representative E. coli searches returned no ECF/folate-transport
    hits. The organism-matched S. pneumoniae dataset resolves ecfT/SP2219, ecfA2/SP2220
    and ecfA1/SP2221; recF is a string-match near miss. Folate biosynthesis hits are
    not FolT transport targets, and FolT search returned none. No L. delbrueckii dataset
    was in the catalog. Adapter results are gene-context only, not drug-binding evidence.
  snapshot_sha256: 24184eee03c92b03c59e77568d4e28885235b9edde64df26378ef756d20bf6f3
- evidence_id: access
  kind: search
  reference: Exact DOI, original supplements and maintained owner search
  locator: 039-root-fetch manifests;390-si-meta.json;390-sipdf-meta.json;390-owners-search.json
  accessed_at: '2026-10-21T15:01:09Z'
  support: supports
  summary: Publisher routes returned403; the full original XML and figure images were
    recovered through PMC, and both free official supplements through ACS Figshare
    with matching resource DOI and checksums. No inaccessible route is treated as
    missing evidence. Only the exact36 material and relevant assay/model sections
    were inspected; other compounds are comparison context.
  search_scope: 2026-10-21; ignored-inclusive local search for exact label, DOI5c02721,
    full key and CURATOR mint. Public DOI/PMID and official supplement retrieval,
    with structured gene-adapter queries before primary mechanism interpretation.
  snapshot_sha256: 199e96457ea5665e28b15102d9a84113d02d60cbc87093a758a740993d67ae57
assessments:
- assessment_id: identity
  area: identity
  topic: Exact published compound36 structure
  outcome: supported
  summary: The maintained chemical string is the exact official supplementary row,
    corroborated by Scheme5 and characterization. Compound36 is publication-scoped;
    no global uniqueness of that bare number is implied.
  target_ids:
  - antibioticmech:curator-34020091be
  evidence_ids:
  - native
  - chemical-primary
  - chemistry
  - characterization
- assessment_id: definition
  area: evidence
  topic: Scaffold description and antibacterial eligibility
  outcome: supported
  summary: The description uses the paper’s1,4-substitution shorthand for its1,2,3-triazole
    scaffold and is consistent with the graph. Original pure-compound growth results
    directly support the antibacterial role.
  target_ids:
  - antibioticmech:curator-34020091be
  evidence_ids:
  - chemical-primary
  - primary-assays
  - native
- assessment_id: quantitative
  area: evidence
  topic: Native source-concept panel and transport statements
  outcome: supported
  summary: The reported0.5–4 micrograms/mL range and42.84 micromolar IC50 agree with
    Table5 and refer to different assay systems. The distinct ATCC51559 result does
    not contradict that bounded panel.
  target_ids:
  - antibioticmech:curator-34020091be
  evidence_ids:
  - primary-assays
  - additional-endpoints
- assessment_id: numeric-expansion
  area: completeness
  topic: Supplement inconsistencies before detailed curation
  outcome: unknown
  summary: Unit and species-label conflicts in the SI should be resolved or explicitly
    preserved before adding structured strain observations. They do not establish
    that the current Table5-derived native statement is false.
  target_ids:
  - antibioticmech:curator-34020091be
  evidence_ids:
  - source-discrepancy
  - primary-assays
- assessment_id: target
  area: evidence
  topic: Functional inhibition versus direct molecular causality
  outcome: supported
  summary: A reconstituted transporter assay supports functional inhibition; specific
    contacts are computational. No native target or graph overstates those claims.
  target_ids:
  - antibioticmech:curator-34020091be
  evidence_ids:
  - primary-assays
  - mechanism-boundary
  - adapter
- assessment_id: other
  area: scope
  topic: Clinical, resistance and microbial origin fields
  outcome: not_applicable
  summary: The synthetic proposed compound has no such native claims. VRE/PRSP labels
    describe comparator-drug resistance, not resistance to compound36. Infection-model
    activity is not clinical efficacy or approval.
  target_ids:
  - antibioticmech:curator-34020091be
  evidence_ids:
  - native
  - additional-endpoints
  - primary-assays
- assessment_id: provenance
  area: provenance
  topic: Maintained curator source and reproducible identifier
  outcome: supported
  summary: All fourteen inputs and the exact row reproduce; MINTED/PROPOSED appropriately
    retain a publication-scoped experimental compound.
  target_ids:
  - antibioticmech:curator-34020091be
  evidence_ids:
  - owners
  - chemistry
  - access
findings: []
actions:
- action_id: A1
  description: Optional future structured assay curation should preserve the original
    endpoint and source-discrepancy boundaries.
  finding_ids: []
  target_ids:
  - antibioticmech:curator-34020091be
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/ecf-transporter-inhibitor-36.yaml
    role: Future curated observations and evidence
  acceptance_checks:
  - Retain the exact official row36 structure, publication scope and neutral form.
  - Keep Table5 mass units and strain panel separate from SI micromolar labels and
    the ATCC51559 time-kill experiment; document unresolved source disagreements.
  - Represent ECF transport inhibition as a functional assay; keep docking affinities,
    contacts and prior-series genetics distinct from direct36 binding or causal evidence.
  - Do not interpret model survival or comparator-drug-resistant strain names as clinical
    approval or resistance to36.
limitations:
- The original main sections relevant to compound36, Scheme5, Table4, Table5 and SI
  assay protocols were read. The NMR plot was visually inspected, but raw spectra,
  docking trajectories and all comparison compounds were not independently reprocessed.
- SI TableS2 and FigureS2 use inconsistent MIC unit labels and disagree on DSM20478
  species naming with the main table/CSV. No detailed native numeric observation was
  imported from these conflicting representations.
- The source-concept claim is Table5-derived. A separate strain’s8.6 micrograms/mL
  MIC and model-survival experiments retain their own scope.
- Reconstituted transport inhibition is not direct affinity measurement; the apo-protein
  docking pose is predictive, and phenotypic activity does not by itself identify
  a unique causal binding event.
- The structured adapter initially queried a nonmatching representative organism;
  the subsequent S. pneumoniae query provides relevant gene context but not L. delbrueckii
  target proof. Zero search hits are not proof that transport machinery is absent.
- No native or maintained source was edited. Shared required validation outcomes are
  attached separately.
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
