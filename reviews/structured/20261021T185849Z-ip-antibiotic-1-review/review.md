# IP-antibiotic 1: exact structure and preliminary antibacterial evidence

- Review: 20261021T185849Z-ip-antibiotic-1-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:21:50Z
- Finished UTC: 2026-10-21T18:58:49Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native structure matches compound 1 in the original synthesis, actual Table1 drawing and exact supplementary characterization pages. The reported WHO Z MIC of 0.156mg/L is supported at its preliminary assay scope. One minor evidence-placement defect remains: a faithful curator paraphrase is stored as a verbatim snippet. Mechanism, broader spectrum, resistance-selection and host-cell findings for compounds2/3 are not transferred to this compound.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 554; one exact record in path order. Original thirteen input hashes preserved; actual curator-table ownership replaces the generic initial ChEBI ownership annotation.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:curator-fb7e3bd3f5 | data/antibiotics/antibacterial/ip-antibiotic-1.yaml | generated | IP-antibiotic 1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:curator-fb7e3bd3f5 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:curator-fb7e3bd3f5 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:curator-fb7e3bd3f5 | Actual focused execution exited 0. |
| Independent reconstruction from the original drawing | passed | False | antibioticmech:curator-fb7e3bd3f5 | An independently typed alternate graph from the original Table1 structure matches the native complete key and reciprocal graph comparison. |
| Structured-source applicability | not_applicable | False | antibioticmech:curator-fb7e3bd3f5 | The native record has no gene, regulator, protein target, pathway or expression assertion. Proteomic experiments in the shared source concern other numbered compounds. |
| Authoritative full QC | failed | True | antibioticmech:curator-fb7e3bd3f5 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:curator-fb7e3bd3f5 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:curator-fb7e3bd3f5 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:curator-fb7e3bd3f5 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:curator-fb7e3bd3f5 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:curator-fb7e3bd3f5 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:curator-fb7e3bd3f5 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:curator-fb7e3bd3f5 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:curator-fb7e3bd3f5 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact publication-numbered compound

identity: supported. Targets: antibioticmech:curator-fb7e3bd3f5.

Actual primary drawings, systematic synthesis name, independent chemistry and the exact supplementary pages support compound1, distinct from the other analogues and protected intermediate.

### Preliminary WHO Z inhibition and definition

evidence: supported. Targets: antibioticmech:curator-fb7e3bd3f5.

The definition, retained role and source quantitative summary match the 0.156mg/L Table1 result with explicit WHO Z, medium and endpoint. Broader claims are not inferred.

### Verbatim snippet semantics

evidence: concern. Targets: antibioticmech:curator-fb7e3bd3f5.

The supported study summary is misfiled as a verbatim snippet and should be moved into the maintained notes column while preserving the existing notes.

### Boundaries of optional mechanism and downstream experiments

completeness: supported. Targets: antibioticmech:curator-fb7e3bd3f5.

No native target or mode is asserted. The shared paper selects compounds2/3 for further experiments; protein-abundance responses, host-cell results and absence of detected resistance during passage must not be generalized to this numbered analogue.

### Curator lane, mint and history

provenance: supported. Targets: antibioticmech:curator-fb7e3bd3f5.

The explicit DOI fragment resolves one exact structure. The generated status and history are consistent; all thirteen initial input hashes remain unchanged. A provider miss or missing optional field does not invalidate the minted identity.

## Findings

### F1: Move the curator paraphrase out of the verbatim snippet field

minor / open / confirmed; issue key: ip-antibiotic-1-paraphrase-in-source-snippet.

The exact curator row places a summary of study design and compound1 Table1 activity in evidence_snippet, which is copied into native source_concepts[0].evidence[0].snippet. The primary supports the factual content, but this is not a verbatim passage. Move it to notes or use a short exact passage while retaining the assay-specific interpretation separately.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained curator evidence placement and regenerate reproducibly.

- For exact source ID DOI:10.1021/acsinfecdis.5c00812#1, move the paraphrase from evidence_snippet into evidence_notes while preserving the current structure-normalization notes and DOI.
- Preserve native exact keyRSTGMHXUQRABLF-UHFFFAOYSA-N, compound number, formula, role and source version; do not transfer compound2/3 follow-up claims.
- Retain the 0.156mg/L preliminary WHO Z result with its assay context. Any replacement snippet must be a short exact primary passage.
- Pass focused schema/strict and corpus reproduction checks without manually patching generated YAML or rewriting history.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/ip-antibiotic-1.yaml; Entire native record, definition, two aliases, role, complete chemistry, source evidence and all history events. | supports | The MINTED/PROPOSED record denotes neutral 2-amino-5,7-dichloroquinolin-8-ol, with complete key RSTGMHXUQRABLF-UHFFFAOYSA-N and no specified stereocentre. Its compound-number alias is source-local to the identified DOI. There are no exact external xrefs, parents, quantitative activity objects, targets, resistance routes, producers or clinical claims. 2 history event(s) remain consistent with proposed curator-inventory status. |
| owners | curation/curator_antibiotics.tsv:2; scripts/seed_from_sources.py:618; scripts/seed_from_sources.py:686; Exact maintained row and curator loader/build logic; source ID matched by equality rather than prefix. | supports | The exact source ID DOI:10.1021/acsinfecdis.5c00812#1 supplies structure, names, definition, role and evidence. The loader copies evidence_snippet directly to source_concepts evidence.snippet and evidence_notes to notes. The native deterministic mint, source/retrieval dates and 2 chronological event(s) were checked. The original thirteen captured inputs include the actual curator table and seeder. |
| chemistry | 554-chemistry.json; 554-authority-chemistry.json; IP-structure-check.py; Native SMILES/InChI/formula/charge/mass/mint checks and independent alternate drawing reconstruction. | supports | Native encodings and the independently reconstructed Table1 graph agree at RSTGMHXUQRABLF-UHFFFAOYSA-N. Formula, neutral charge, one molecular fragment and both masses agree at stated precision. No salt, metal complex, protected precursor or positional isomer is substituted. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/130156098; Current official exact-key response; both structure encodings independently parsed. | supports | PubChem CID130156098 agrees with the native exact graph and systematic name. It is an additional corroborating authority, not a native claimed xref or a reason to replace the explicit publication-based minted identity. |
| primary | PMID:41405126; DOI:10.1021/acsinfecdis.5c00812; https://pmc.ncbi.nlm.nih.gov/articles/PMC12797230/; Entire original main text, abstract, all tables and captions read; actual Scheme1 and Table1 images inspected. | supports | The study separately synthesizes twelve numbered compounds and screens them against multidrug-resistant N.gonorrhoeae WHO Z. The synthesis numbering and drawings resolve the source-local compound names. Subsequent time-kill, resistance-selection, cervical-cell, cytotoxicity, additional-species and proteomic experiments select compounds2/3 and PBT2; they do not establish those outcomes for every analogue. |
| material | DOI:10.1021/acsinfecdis.5c00812; DOI:10.1021/acsinfecdis.5c00812.s001; https://ndownloader.figshare.com/files/60451332; Exact main synthesis/characterization subsection for compound1; actual supplementary pagesS2–S3; publisher Figshare resource DOI and file identity verified. | supports | The named compound1 is isolated as the deprotected amine; the main reports HRMS[M+H]+ found228.9929 versus calculated228.9930. The source purity statement is greater than95% by NMR. The actual S2 proton/carbon spectra and S3 mass spectrum depict the same amine and support the reported characterization. Neither protonated/deprotonated MS ions nor reaction reagents are separate native salt components. Raw spectra were visually inspected as published, not independently reprocessed or fully reassigned. |
| activity | PMID:41405126; Table1; Bacterial Strains/Media and MIC Determination Methods; Actual Table1 compound1 cell and complete corresponding methods. | supports | Table1 gives 0.156mg/L against N.gonorrhoeae WHO Z. Gonococcal GC broth/agar includes1% IsoVitaleX; the MIC method uses approximately5×10^5CFU/mL adjusted suspension,100µL inoculum, serially diluted compound and overnight37°C growth with no turbidity as endpoint. Each assay is stated as three times in triplicate. No exogenous zinc supplementation is specified for this monotherapy screen. PBT2 is0.313mg/L in the same table, supporting the approximately twofold comparison. This is not species-wide efficacy, a clinical breakpoint or a resistance mechanism. |
| role | CHEBI:33282; Current official antibacterial-agent definition. | supports | The role denotes bacterial growth inhibition or killing. The exact WHO Z experiment supports antibacterial filing without requiring a clinical indication, a molecular target or activity against all strains. |
| snippet | .claude/skills/curate-yaml-record/references/review-checklist.md:14; source_concepts[0].evidence[0].snippet; Native/source-row wording compared with the fully read original main and exact Table1 result. | supports | The native sentence begins with a third-person description of Jen and colleagues and combines study design with a table result. It is a faithful curator summary, not a verbatim primary passage. The checklist reserves snippet for exact source text and directs interpretation to notes. The factual antibacterial statement itself is supported; the defect is evidence placement, not unsupported activity. |
| search | 554-local-hits.txt; 554-owner-hits.txt;056-root-fetch1.json through056-root-fetch5.json; Hidden/ignored-inclusive initial whole-worktree search and exact full-key search in data/curation/conf; direct DOI/source and supplement retrieval. | context_only | The exact-key maintained-input search returned the target record and its curator row. No additional exact key was returned in those searched YAML/TSV/JSON surfaces, including ignored and hidden paths. Primary DOI/PMC identity resolved. Ordinary PMC supplement returned challenge HTML and ACS/Europe PMC PDF routes failed403; the publisher-linked Figshare API supplied the verified original1.4MB PDF. No broad claim of exhaustive later literature or registry coverage is made. |

## Limits And Additional Notes

- The entire main was read, but actual image inspection for this review covered Scheme1/Table1 and the exact supplementary pagesS2–S3; other compounds spectra and biological figure pixels were not independently assessed for this target.
- Published spectra support the stated characterization; raw instrumental data, peak integration and the authors greater-than95% purity judgment were not independently reprocessed.
- The MIC method gives overnight incubation and an approximate inoculum based on optical density; the review does not invent an exact incubation duration, final viable count or solvent concentration absent from that assay description.
- No comprehensive later-literature or registry search was undertaken. Follow-up experiments on other numbered analogues remain outside the target-specific evidence, and no clinical use or safety conclusion is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Only scratch review artifacts were written. Original input hashes, native record, maintained source, curation history and proposed status remain unchanged.
- The actual curator table and seeder own a future correction; generic initial ChEBI owner annotations were corrected in the review target without altering captured input hashes.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T185849Z-ip-antibiotic-1-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'IP-antibiotic 1: exact structure and preliminary antibacterial evidence'
started_at: '2026-10-21T18:21:50Z'
finished_at: '2026-10-21T18:58:49Z'
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
summary: 'The native structure matches compound 1 in the original synthesis, actual
  Table1 drawing and exact supplementary characterization pages. The reported WHO
  Z MIC of 0.156mg/L is supported at its preliminary assay scope. One minor evidence-placement
  defect remains: a faithful curator paraphrase is stored as a verbatim snippet. Mechanism,
  broader spectrum, resistance-selection and host-cell findings for compounds2/3 are
  not transferred to this compound.'
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
  - path: data/antibiotics/antibacterial/ip-antibiotic-1.yaml
    sha256: 7ac03ca0e304faf444c4504f7940626e8f247d2c6a421725cdfeba7082173701
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
- target_id: antibioticmech:curator-fb7e3bd3f5
  path: data/antibiotics/antibacterial/ip-antibiotic-1.yaml
  label: IP-antibiotic 1
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Exact publication-derived structure, definition and source evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator-inventory loading and native emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Optional maintained grounding adjudication
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 554; one exact record in path order.
    Original thirteen input hashes preserved; actual curator-table ownership replaces
    the generic initial ChEBI ownership annotation.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:curator-fb7e3bd3f5
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-fb7e3bd3f5
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    554
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-fb7e3bd3f5
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/ip-antibiotic-1.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-fb7e3bd3f5
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/ip-antibiotic-1.yaml --out /private/tmp/am-review-session/554-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: primary-graph
  name: Independent reconstruction from the original drawing
  status: passed
  required: false
  summary: An independently typed alternate graph from the original Table1 structure
    matches the native complete key and reciprocal graph comparison.
  target_ids:
  - antibioticmech:curator-fb7e3bd3f5
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/IP-structure-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter
  name: Structured-source applicability
  status: not_applicable
  required: false
  summary: The native record has no gene, regulator, protein target, pathway or expression
    assertion. Proteomic experiments in the shared source concern other numbered compounds.
  target_ids:
  - antibioticmech:curator-fb7e3bd3f5
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:curator-fb7e3bd3f5
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
  - antibioticmech:curator-fb7e3bd3f5
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
  - antibioticmech:curator-fb7e3bd3f5
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
  - antibioticmech:curator-fb7e3bd3f5
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
  - antibioticmech:curator-fb7e3bd3f5
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
  - antibioticmech:curator-fb7e3bd3f5
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
  - antibioticmech:curator-fb7e3bd3f5
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
  - antibioticmech:curator-fb7e3bd3f5
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
  - antibioticmech:curator-fb7e3bd3f5
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/ip-antibiotic-1.yaml
  locator: Entire native record, definition, two aliases, role, complete chemistry,
    source evidence and all history events.
  accessed_at: '2026-10-21T18:34:04Z'
  support: supports
  summary: The MINTED/PROPOSED record denotes neutral 2-amino-5,7-dichloroquinolin-8-ol,
    with complete key RSTGMHXUQRABLF-UHFFFAOYSA-N and no specified stereocentre. Its
    compound-number alias is source-local to the identified DOI. There are no exact
    external xrefs, parents, quantitative activity objects, targets, resistance routes,
    producers or clinical claims. 2 history event(s) remain consistent with proposed
    curator-inventory status.
- evidence_id: owners
  kind: record_content
  reference: curation/curator_antibiotics.tsv:2; scripts/seed_from_sources.py:618;
    scripts/seed_from_sources.py:686
  locator: Exact maintained row and curator loader/build logic; source ID matched
    by equality rather than prefix.
  accessed_at: '2026-10-21T18:34:04Z'
  support: supports
  summary: The exact source ID DOI:10.1021/acsinfecdis.5c00812#1 supplies structure,
    names, definition, role and evidence. The loader copies evidence_snippet directly
    to source_concepts evidence.snippet and evidence_notes to notes. The native deterministic
    mint, source/retrieval dates and 2 chronological event(s) were checked. The original
    thirteen captured inputs include the actual curator table and seeder.
  snapshot_sha256: e16497823dd301468e6b11071be76b7440660f89d1d91dcd887a1aaadde7e220
- evidence_id: chemistry
  kind: validation
  reference: 554-chemistry.json; 554-authority-chemistry.json; IP-structure-check.py
  locator: Native SMILES/InChI/formula/charge/mass/mint checks and independent alternate
    drawing reconstruction.
  accessed_at: '2026-10-21T18:34:04Z'
  support: supports
  summary: Native encodings and the independently reconstructed Table1 graph agree
    at RSTGMHXUQRABLF-UHFFFAOYSA-N. Formula, neutral charge, one molecular fragment
    and both masses agree at stated precision. No salt, metal complex, protected precursor
    or positional isomer is substituted.
  snapshot_sha256: 93d22fcff1f9c174873e5a01aca583df5c632e779a20193747f385a3cb6ecf4b
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/130156098
  locator: Current official exact-key response; both structure encodings independently
    parsed.
  accessed_at: '2026-10-21T18:34:04Z'
  support: supports
  summary: PubChem CID130156098 agrees with the native exact graph and systematic
    name. It is an additional corroborating authority, not a native claimed xref or
    a reason to replace the explicit publication-based minted identity.
  snapshot_sha256: eecd08ccbfe7c52733a22137e9f1b4d3bfda57c0262aa363cd82a8a43fc1af69
- evidence_id: primary
  kind: primary_source
  reference: PMID:41405126; DOI:10.1021/acsinfecdis.5c00812; https://pmc.ncbi.nlm.nih.gov/articles/PMC12797230/
  locator: Entire original main text, abstract, all tables and captions read; actual
    Scheme1 and Table1 images inspected.
  accessed_at: '2026-10-21T18:34:04Z'
  support: supports
  summary: The study separately synthesizes twelve numbered compounds and screens
    them against multidrug-resistant N.gonorrhoeae WHO Z. The synthesis numbering
    and drawings resolve the source-local compound names. Subsequent time-kill, resistance-selection,
    cervical-cell, cytotoxicity, additional-species and proteomic experiments select
    compounds2/3 and PBT2; they do not establish those outcomes for every analogue.
  snapshot_sha256: 2a99c3f72244f2e8a63dd207e623081cb3e00101c49502b9043ce4ff4b584fab
- evidence_id: material
  kind: primary_source
  reference: DOI:10.1021/acsinfecdis.5c00812; DOI:10.1021/acsinfecdis.5c00812.s001;
    https://ndownloader.figshare.com/files/60451332
  locator: Exact main synthesis/characterization subsection for compound1; actual
    supplementary pagesS2–S3; publisher Figshare resource DOI and file identity verified.
  accessed_at: '2026-10-21T18:34:04Z'
  support: supports
  summary: The named compound1 is isolated as the deprotected amine; the main reports
    HRMS[M+H]+ found228.9929 versus calculated228.9930. The source purity statement
    is greater than95% by NMR. The actual S2 proton/carbon spectra and S3 mass spectrum
    depict the same amine and support the reported characterization. Neither protonated/deprotonated
    MS ions nor reaction reagents are separate native salt components. Raw spectra
    were visually inspected as published, not independently reprocessed or fully reassigned.
  snapshot_sha256: 1b130403095d4518fbc3a59edf57c3ed7753d47b6beb2f16c21d46c6efe583b8
- evidence_id: activity
  kind: primary_source
  reference: PMID:41405126; Table1; Bacterial Strains/Media and MIC Determination
    Methods
  locator: Actual Table1 compound1 cell and complete corresponding methods.
  accessed_at: '2026-10-21T18:34:04Z'
  support: supports
  summary: Table1 gives 0.156mg/L against N.gonorrhoeae WHO Z. Gonococcal GC broth/agar
    includes1% IsoVitaleX; the MIC method uses approximately5×10^5CFU/mL adjusted
    suspension,100µL inoculum, serially diluted compound and overnight37°C growth
    with no turbidity as endpoint. Each assay is stated as three times in triplicate.
    No exogenous zinc supplementation is specified for this monotherapy screen. PBT2
    is0.313mg/L in the same table, supporting the approximately twofold comparison.
    This is not species-wide efficacy, a clinical breakpoint or a resistance mechanism.
  snapshot_sha256: 67e867b42477bf51aa785476377153818c3e9d95041fa4d8e8acdf9e84fd7ff0
- evidence_id: role
  kind: authority
  reference: CHEBI:33282
  locator: Current official antibacterial-agent definition.
  accessed_at: '2026-10-21T18:34:04Z'
  support: supports
  summary: The role denotes bacterial growth inhibition or killing. The exact WHO
    Z experiment supports antibacterial filing without requiring a clinical indication,
    a molecular target or activity against all strains.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: snippet
  kind: validation
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md:14;
    source_concepts[0].evidence[0].snippet
  locator: Native/source-row wording compared with the fully read original main and
    exact Table1 result.
  accessed_at: '2026-10-21T18:34:04Z'
  support: supports
  summary: The native sentence begins with a third-person description of Jen and colleagues
    and combines study design with a table result. It is a faithful curator summary,
    not a verbatim primary passage. The checklist reserves snippet for exact source
    text and directs interpretation to notes. The factual antibacterial statement
    itself is supported; the defect is evidence placement, not unsupported activity.
- evidence_id: search
  kind: search
  reference: 554-local-hits.txt; 554-owner-hits.txt;056-root-fetch1.json through056-root-fetch5.json
  locator: Hidden/ignored-inclusive initial whole-worktree search and exact full-key
    search in data/curation/conf; direct DOI/source and supplement retrieval.
  accessed_at: '2026-10-21T18:34:04Z'
  support: context_only
  summary: The exact-key maintained-input search returned the target record and its
    curator row. No additional exact key was returned in those searched YAML/TSV/JSON
    surfaces, including ignored and hidden paths. Primary DOI/PMC identity resolved.
    Ordinary PMC supplement returned challenge HTML and ACS/Europe PMC PDF routes
    failed403; the publisher-linked Figshare API supplied the verified original1.4MB
    PDF. No broad claim of exhaustive later literature or registry coverage is made.
  search_scope: 2026-10-21; rg --no-ignore --hidden exact label/identifier/key/slug
    searches; additional full-key query across data,curation,conf YAML/TSV/JSON; exact
    primary DOI and publisher supplement API follow-up.
  snapshot_sha256: 1871b9d3e93ada5f4f9d16dffd151251d412d0347f10bdd8eaaa6f73ad3217b9
assessments:
- assessment_id: identity
  area: identity
  topic: Exact publication-numbered compound
  outcome: supported
  summary: Actual primary drawings, systematic synthesis name, independent chemistry
    and the exact supplementary pages support compound1, distinct from the other analogues
    and protected intermediate.
  target_ids:
  - antibioticmech:curator-fb7e3bd3f5
  evidence_ids:
  - native
  - owners
  - chemistry
  - primary
  - material
- assessment_id: activity
  area: evidence
  topic: Preliminary WHO Z inhibition and definition
  outcome: supported
  summary: The definition, retained role and source quantitative summary match the
    0.156mg/L Table1 result with explicit WHO Z, medium and endpoint. Broader claims
    are not inferred.
  target_ids:
  - antibioticmech:curator-fb7e3bd3f5
  evidence_ids:
  - primary
  - activity
  - role
- assessment_id: quotation
  area: evidence
  topic: Verbatim snippet semantics
  outcome: concern
  summary: The supported study summary is misfiled as a verbatim snippet and should
    be moved into the maintained notes column while preserving the existing notes.
  target_ids:
  - antibioticmech:curator-fb7e3bd3f5
  evidence_ids:
  - native
  - owners
  - snippet
  - activity
- assessment_id: mechanism
  area: completeness
  topic: Boundaries of optional mechanism and downstream experiments
  outcome: supported
  summary: No native target or mode is asserted. The shared paper selects compounds2/3
    for further experiments; protein-abundance responses, host-cell results and absence
    of detected resistance during passage must not be generalized to this numbered
    analogue.
  target_ids:
  - antibioticmech:curator-fb7e3bd3f5
  evidence_ids:
  - native
  - primary
- assessment_id: provenance
  area: provenance
  topic: Curator lane, mint and history
  outcome: supported
  summary: The explicit DOI fragment resolves one exact structure. The generated status
    and history are consistent; all thirteen initial input hashes remain unchanged.
    A provider miss or missing optional field does not invalidate the minted identity.
  target_ids:
  - antibioticmech:curator-fb7e3bd3f5
  evidence_ids:
  - owners
  - native
  - chemistry
  - pubchem
  - search
findings:
- finding_id: F1
  issue_key: ip-antibiotic-1-paraphrase-in-source-snippet
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Move the curator paraphrase out of the verbatim snippet field
  description: The exact curator row places a summary of study design and compound1
    Table1 activity in evidence_snippet, which is copied into native source_concepts[0].evidence[0].snippet.
    The primary supports the factual content, but this is not a verbatim passage.
    Move it to notes or use a short exact passage while retaining the assay-specific
    interpretation separately.
  target_ids:
  - antibioticmech:curator-fb7e3bd3f5
  field_paths:
  - source_concepts[0].evidence[0].snippet
  evidence_ids:
  - native
  - owners
  - snippet
  - activity
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Exact publication-derived structure, definition and source evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator-inventory loading and native emission
  rule_id: 'review-checklist: Evidence standard, verbatim snippet versus curator notes'
  native_severity: minor
  normalization_reason: This is a bounded evidence-placement defect; the identity
    and quantitative source statement remain supported.
actions:
- action_id: A1
  description: Correct the maintained curator evidence placement and regenerate reproducibly.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:curator-fb7e3bd3f5
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Exact publication-derived structure, definition and source evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator-inventory loading and native emission
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - For exact source ID DOI:10.1021/acsinfecdis.5c00812#1, move the paraphrase from
    evidence_snippet into evidence_notes while preserving the current structure-normalization
    notes and DOI.
  - Preserve native exact keyRSTGMHXUQRABLF-UHFFFAOYSA-N, compound number, formula,
    role and source version; do not transfer compound2/3 follow-up claims.
  - Retain the 0.156mg/L preliminary WHO Z result with its assay context. Any replacement
    snippet must be a short exact primary passage.
  - Pass focused schema/strict and corpus reproduction checks without manually patching
    generated YAML or rewriting history.
limitations:
- The entire main was read, but actual image inspection for this review covered Scheme1/Table1
  and the exact supplementary pagesS2–S3; other compounds spectra and biological figure
  pixels were not independently assessed for this target.
- Published spectra support the stated characterization; raw instrumental data, peak
  integration and the authors greater-than95% purity judgment were not independently
  reprocessed.
- The MIC method gives overnight incubation and an approximate inoculum based on optical
  density; the review does not invent an exact incubation duration, final viable count
  or solvent concentration absent from that assay description.
- No comprehensive later-literature or registry search was undertaken. Follow-up experiments
  on other numbered analogues remain outside the target-specific evidence, and no
  clinical use or safety conclusion is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Only scratch review artifacts were written. Original input hashes, native record,
  maintained source, curation history and proposed status remain unchanged.
- The actual curator table and seeder own a future correction; generic initial ChEBI
  owner annotations were corrected in the review target without altering captured
  input hashes.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
