# Erianin: coherent identity and distinct growth, sortase and host-cell evidence

- Review: 20261021T154515Z-erianin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:30:46Z
- Finished UTC: 2026-10-21T15:45:15Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The exact neutral erianin structure and broader chemical classes are supported. Original bacterial growth and purified-sortase experiments support the antibacterial role, while adopted cancer and neurological studies address host biology. No confirmed native defect was established; precise source and assay boundaries remain explicit. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 411; one entire native record. Thirteen initial input hashes were retained when the actual readiness-queue context was appended; fourteen unchanged inputs are captured.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:233659 | data/antibiotics/antibacterial/erianin.yaml | generated | erianin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:233659 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:233659 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:233659 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:233659 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:233659 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:233659 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:233659 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:233659 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:233659 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:233659 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:233659 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:233659 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact substitution pattern and external component links

identity: supported. Targets: CHEBI:233659.

Independent graphs agree; equivalent ring numbering does not create an isomer. Broader classes and accessible exact xrefs are coherent. HMDB and original NSC naming remain bounded.

### Growth inhibition, sortase and host-cell endpoints

evidence: supported. Targets: CHEBI:233659.

Original bacterial assays support eligibility. Purified-SrtA evidence offers a specific curation lead, with docking, affinity experiments, cellular phenotypes and growth MIC kept distinct. Host anticancer/tubulin results are not antimicrobial mechanisms.

### Dendrobium statement

evidence: supported. Targets: CHEBI:233659.

Original phytochemical abstract and selected2024 main-text experiments support the broad source statement. Candidate biosynthetic enzymes and source organism are not antibacterial targets.

### Optional biological fields and record status

completeness: supported. Targets: CHEBI:233659.

Absent optional quantitative activity, mechanism, resistance, producer, clinical, graph and dataset fields are not automatic defects in this SEEDED record. Useful exact primary leads are documented without treating this review as native curation or biological sign-off.

### Adopted leads, generated ownership and immutable source capture

provenance: supported. Targets: CHEBI:233659.

Every native field and all ten adopted lead dispositions were covered at the stated reading depth. Focused schema, strict and chemistry checks pass, and all fourteen captured source inputs remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/erianin.yaml; Entire native YAML, all fields and history | supports | The SEEDED/EXACT record has 5 exact synonyms, 3 broader parents, one antibacterial role, one ChEBI source concept and 3 source history events. All were inspected. No quantitative activity, molecular target, mode, resistance, producer, clinical, graph or dataset object is asserted. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; curation/record_review_queue.tsv; 411-source-rows.json; applicable extraction, normalization and seeding code | supports | The exact adopted ChEBI row supplies identity, definition, structure, roles, links and ten publication leads. Readiness is context, not independent scientific evidence. Original hashes were retained before judgment. No additional exact source owner was established by the ignored-inclusive local search. |
| chemistry | 042-authority-compare.json; 411-chemistry.json; Independent full-key, formula, charge and atom-adjacency comparisons | supports | Native SMILES and InChI, current ChEBI SMILES/InChI/molfile and PubChem encodings agree on UXDFUVFNIAJEGM-UHFFFAOYSA-N, C18H22O5, neutral charge and no stereocentres. All four inspected CCD W4F SMILES and both KNApSAcK encodings also agree; thirteen encodings in total. Focused chemistry additionally verifies stored masses and the deterministic source alias. |
| authority | CHEBI:233659; https://www.ebi.ac.uk/chebi/CHEBI:233659; Current complete chemical entry and definitions of all asserted broader parents and role | supports | CHEBI33853 phenols,51571 diphenylethanes and51683 methoxybenzenes fit the graph. The four systematic synonyms describe the same substitution pattern; NSC613744 is authority-attested, without an original NCI naming-history audit. The current entry has29 literature links; all ten adopted abstracts were read, nineteen additional titles screened, and one relevant additional original examined in selected full-text sections. |
| search | 411-local-hits.txt; 411-owners-search.json; 042-root-fetch-manifest.json through 042-root-fetch5-manifest.json; Ignored-inclusive local discovery, current linked authorities and bounded original-paper retrieval | supports | Hidden and gitignored files were included in the local evidence/owner search. Exact source rows and all adopted publication leads were assessed. Access failures, login pages and HTML challenges were not treated as read full texts or chemical structures. |
| xrefs | KNApSAcK:C00015428; PDB-CCD:W4F; CAS:95041-90-0; Complete KNApSAcK entry and CCD JSON; independent parsed encodings | supports | KNApSAcK CAS and complete structure match. Its ring-renumbered name is equivalent, and an Eria carinata occurrence does not exclude Dendrobium. W4F is the exact chemical component and links the2024 tubulin study, not a whole protein structure or bacterial target. HMDB0251918 returned403 and remains independently unverified. |
| adopted | PMID:11749794;16378617;35060996;37608888;38374284;38401517;38905886;39039049;39063214;39146784; All ten complete indexed abstracts read; original versus review status retained | supports | 11749794 reports HL60 apoptosis;16378617 HPLC analysis of eleven phenols in31 Dendrobium samples, without listing every individual compound in its abstract;35060996 retinal Rho/ROCK biology;37608888 and38401517 are reviews;38374284 rat traumatic brain injury;38905886 original tubulin binding/crystallography;39039049 glioma stem-cell ferroptosis;39063214 gastric cancer signaling;39146784 rat cerebral ischemia/reperfusion. These are host or phytochemical contexts, not direct bacterial growth or bacterial-target experiments. No potency is transferred from these abstracts. |
| bacterial | PMID:30249042; DOI:10.3390/toxins10100385; PMC6215257; https://pmc.ncbi.nlm.nih.gov/articles/PMC6215257/; Original main text and methods read; actual original PDF Figures1–3 inspected | supports | Commercial erianin from Chengdu Herbpurify in DMSO was tested against S. aureus Newman D2C/ATCC25904 and its srtA deletion strain. Reported MIC is512 micrograms/mL; growth at8–64 micrograms/mL was not inhibited. Purified recombinant SrtA residues60–206 were examined by FRET after30-minute preincubation and60-minute reaction at37°C, giving IC50 20.91±2.31 micrograms/mL. This is enzyme inhibition, not a growth MIC. Fluorescence quenching and V193A/R197A mutant experiments accompany docking; modeled atomic contacts are not a co-crystal determination. Fibrinogen binding assays and mouse experiments address virulence effects, not clinical efficacy. |
| producer | PMID:39391777; DOI:10.3389/fpls.2024.1436560; PMC11464314; https://pmc.ncbi.nlm.nih.gov/articles/PMC11464314/; Original Methods, Results and Discussion sections; indexed abstract | supports | Two-year-old D. chrysotoxum and D. thyrsiflorum stems from Yunnan were profiled by UPLC-MS/MS and database-assisted metabolite identification. Feeding deuterated gigantol and detecting labeled erianin supports a precursor relationship. Expression and docking analyses nominate CYP/OMT candidates but do not establish every proposed purified-enzyme reaction. This supports bounded Dendrobium occurrence; no named producer strain or fully validated biosynthetic chain is inferred. |
| adapter | iModulonDB catalog and S. aureus staph_precise108 gene query; Actual catalog inspected before mechanism research; sortase query completed | supports | The catalog was inspected first. The covered USA300 dataset query identifies srtA USA300HOU_RS13705 and srtB USA300HOU_RS05670 with no iModulons returned by that search. Individual gene memberships were not separately queried. This is a different strain from the primary Newman experiment; no allele-level equivalence or transcriptional component was invented. |

## Limits And Additional Notes

- The ten adopted leads were read as complete indexed abstracts, not ten full papers. The2005 HPLC publisher route returned challenge HTML. The2018 antibacterial main text and original selected figures were read; raw data and every supplement were not reanalyzed.
- The current ChEBI entry has nineteen additional leads beyond the adopted ten; those titles were screened, not all their abstracts or full texts. One title is explicitly a retraction (PMID39957357) and was not used as evidence.
- The2024 producer paper was read in selected Methods/Results/Discussion sections; original spectra and all supplementary figures were not independently inspected. HMDB access failed.
- The2018 paper uses fibrinogen in the methods despite fibronectin wording in the abstract, and one figure caption dose differs from its legend/methods. These reporting limits are not silently reconciled. Exact microdilution details beyond the paper and cited standard are not invented.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native or source file was modified. Independent chemistry used the existing batch019 interpreter against the batch042 records; focused schema and strict gates used the batch042 environment.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T154515Z-erianin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Erianin: coherent identity and distinct growth, sortase and host-cell evidence'
started_at: '2026-10-21T15:30:46Z'
finished_at: '2026-10-21T15:45:15Z'
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
summary: The exact neutral erianin structure and broader chemical classes are supported.
  Original bacterial growth and purified-sortase experiments support the antibacterial
  role, while adopted cancer and neurological studies address host biology. No confirmed
  native defect was established; precise source and assay boundaries remain explicit.
  Scientific assessment retains the stated evidence limits; full verification is blocked
  by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/erianin.yaml
    sha256: c16a0e85a727c411120b017f6d05337199208d6330e34efbf2f132b1e3d25560
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
- target_id: CHEBI:233659
  path: data/antibiotics/antibacterial/erianin.yaml
  label: erianin
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
  selection: Queue position 411; one entire native record. Thirteen initial input
    hashes were retained when the actual readiness-queue context was appended; fourteen
    unchanged inputs are captured.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:233659
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:233659
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    411
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:233659
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/erianin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:233659
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/erianin.yaml --out /private/tmp/am-review-session/411-strict.tsv
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
  - CHEBI:233659
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
  - CHEBI:233659
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
  - CHEBI:233659
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
  - CHEBI:233659
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
  - CHEBI:233659
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
  - CHEBI:233659
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
  - CHEBI:233659
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
  - CHEBI:233659
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
  - CHEBI:233659
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/erianin.yaml
  locator: Entire native YAML, all fields and history
  accessed_at: '2026-10-21T15:45:14Z'
  support: supports
  summary: The SEEDED/EXACT record has 5 exact synonyms, 3 broader parents, one antibacterial
    role, one ChEBI source concept and 3 source history events. All were inspected.
    No quantitative activity, molecular target, mode, resistance, producer, clinical,
    graph or dataset object is asserted.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py; curation/record_review_queue.tsv
  locator: 411-source-rows.json; applicable extraction, normalization and seeding
    code
  accessed_at: '2026-10-21T15:45:14Z'
  support: supports
  summary: The exact adopted ChEBI row supplies identity, definition, structure, roles,
    links and ten publication leads. Readiness is context, not independent scientific
    evidence. Original hashes were retained before judgment. No additional exact source
    owner was established by the ignored-inclusive local search.
  snapshot_sha256: d9d20f2b3e7f58b0f22d82893426034d5ed7a058bbf46d9cc5d14e34065e417b
- evidence_id: chemistry
  kind: validation
  reference: 042-authority-compare.json; 411-chemistry.json
  locator: Independent full-key, formula, charge and atom-adjacency comparisons
  accessed_at: '2026-10-21T15:45:14Z'
  support: supports
  summary: Native SMILES and InChI, current ChEBI SMILES/InChI/molfile and PubChem
    encodings agree on UXDFUVFNIAJEGM-UHFFFAOYSA-N, C18H22O5, neutral charge and no
    stereocentres. All four inspected CCD W4F SMILES and both KNApSAcK encodings also
    agree; thirteen encodings in total. Focused chemistry additionally verifies stored
    masses and the deterministic source alias.
  snapshot_sha256: b272eea3b5cb152c442ab57efd0f202a9aa4f9afbc007c25784f9128b79dd74b
- evidence_id: authority
  kind: authority
  reference: CHEBI:233659; https://www.ebi.ac.uk/chebi/CHEBI:233659
  locator: Current complete chemical entry and definitions of all asserted broader
    parents and role
  accessed_at: '2026-10-21T15:45:14Z'
  support: supports
  summary: CHEBI33853 phenols,51571 diphenylethanes and51683 methoxybenzenes fit the
    graph. The four systematic synonyms describe the same substitution pattern; NSC613744
    is authority-attested, without an original NCI naming-history audit. The current
    entry has29 literature links; all ten adopted abstracts were read, nineteen additional
    titles screened, and one relevant additional original examined in selected full-text
    sections.
  snapshot_sha256: dc0c7721a7e5e86853513682fa7c3361a664413a695b619c2359f499226674f7
- evidence_id: search
  kind: search
  reference: 411-local-hits.txt; 411-owners-search.json; 042-root-fetch-manifest.json
    through 042-root-fetch5-manifest.json
  locator: Ignored-inclusive local discovery, current linked authorities and bounded
    original-paper retrieval
  accessed_at: '2026-10-21T15:45:14Z'
  support: supports
  summary: Hidden and gitignored files were included in the local evidence/owner search.
    Exact source rows and all adopted publication leads were assessed. Access failures,
    login pages and HTML challenges were not treated as read full texts or chemical
    structures.
  search_scope: '2026-10-21: rg --no-ignore --hidden using exact compound names, native
    identifier and molecular key over repository data, curation, conf, scripts, src,
    docs, reviews and reports; direct official linked authorities, EuropePMC metadata/full
    text and free publisher routes. Broader searches were discovery only, not an exhaustive
    absence claim.'
  snapshot_sha256: d0d169c0ff173bf2f595d001902087a6a1b25dd2ddca28c8c8c3b89807684dc8
- evidence_id: xrefs
  kind: authority
  reference: KNApSAcK:C00015428; PDB-CCD:W4F; CAS:95041-90-0
  locator: Complete KNApSAcK entry and CCD JSON; independent parsed encodings
  accessed_at: '2026-10-21T15:45:14Z'
  support: supports
  summary: KNApSAcK CAS and complete structure match. Its ring-renumbered name is
    equivalent, and an Eria carinata occurrence does not exclude Dendrobium. W4F is
    the exact chemical component and links the2024 tubulin study, not a whole protein
    structure or bacterial target. HMDB0251918 returned403 and remains independently
    unverified.
  snapshot_sha256: 7fa43d2c26216b59d645472ac88bc9f0473f667f6e3ca2606943e39d4e8a2cb8
- evidence_id: adopted
  kind: primary_source
  reference: PMID:11749794;16378617;35060996;37608888;38374284;38401517;38905886;39039049;39063214;39146784
  locator: All ten complete indexed abstracts read; original versus review status
    retained
  accessed_at: '2026-10-21T15:45:14Z'
  support: supports
  summary: 11749794 reports HL60 apoptosis;16378617 HPLC analysis of eleven phenols
    in31 Dendrobium samples, without listing every individual compound in its abstract;35060996
    retinal Rho/ROCK biology;37608888 and38401517 are reviews;38374284 rat traumatic
    brain injury;38905886 original tubulin binding/crystallography;39039049 glioma
    stem-cell ferroptosis;39063214 gastric cancer signaling;39146784 rat cerebral
    ischemia/reperfusion. These are host or phytochemical contexts, not direct bacterial
    growth or bacterial-target experiments. No potency is transferred from these abstracts.
  snapshot_sha256: e2b3906b0336fbcbcedf89a44e7b2d2c102b008c345dbf9e2da54079f0cb3a2e
- evidence_id: bacterial
  kind: primary_source
  reference: PMID:30249042; DOI:10.3390/toxins10100385; PMC6215257; https://pmc.ncbi.nlm.nih.gov/articles/PMC6215257/
  locator: Original main text and methods read; actual original PDF Figures1–3 inspected
  accessed_at: '2026-10-21T15:45:14Z'
  support: supports
  summary: Commercial erianin from Chengdu Herbpurify in DMSO was tested against S.
    aureus Newman D2C/ATCC25904 and its srtA deletion strain. Reported MIC is512 micrograms/mL;
    growth at8–64 micrograms/mL was not inhibited. Purified recombinant SrtA residues60–206
    were examined by FRET after30-minute preincubation and60-minute reaction at37°C,
    giving IC50 20.91±2.31 micrograms/mL. This is enzyme inhibition, not a growth
    MIC. Fluorescence quenching and V193A/R197A mutant experiments accompany docking;
    modeled atomic contacts are not a co-crystal determination. Fibrinogen binding
    assays and mouse experiments address virulence effects, not clinical efficacy.
  snapshot_sha256: 4c4fd2ccca7d4de0b0db4b350ea06703aa454718adcc833d2afabb120b23f17d
- evidence_id: producer
  kind: primary_source
  reference: PMID:39391777; DOI:10.3389/fpls.2024.1436560; PMC11464314; https://pmc.ncbi.nlm.nih.gov/articles/PMC11464314/
  locator: Original Methods, Results and Discussion sections; indexed abstract
  accessed_at: '2026-10-21T15:45:14Z'
  support: supports
  summary: Two-year-old D. chrysotoxum and D. thyrsiflorum stems from Yunnan were
    profiled by UPLC-MS/MS and database-assisted metabolite identification. Feeding
    deuterated gigantol and detecting labeled erianin supports a precursor relationship.
    Expression and docking analyses nominate CYP/OMT candidates but do not establish
    every proposed purified-enzyme reaction. This supports bounded Dendrobium occurrence;
    no named producer strain or fully validated biosynthetic chain is inferred.
  snapshot_sha256: a06046060a3769de1f021de9be22fc230bc38bd9d9ebbf2ab5af4fca2b6b5dc1
- evidence_id: adapter
  kind: database
  reference: iModulonDB catalog and S. aureus staph_precise108 gene query
  locator: Actual catalog inspected before mechanism research; sortase query completed
  accessed_at: '2026-10-21T15:45:14Z'
  support: supports
  summary: The catalog was inspected first. The covered USA300 dataset query identifies
    srtA USA300HOU_RS13705 and srtB USA300HOU_RS05670 with no iModulons returned by
    that search. Individual gene memberships were not separately queried. This is
    a different strain from the primary Newman experiment; no allele-level equivalence
    or transcriptional component was invented.
  snapshot_sha256: 22a23e3df3cd69d64e57697f0c0b289ac26edfb911ebc0d4e7a51bee454d10fc
assessments:
- assessment_id: identity
  area: identity
  topic: Exact substitution pattern and external component links
  outcome: supported
  summary: Independent graphs agree; equivalent ring numbering does not create an
    isomer. Broader classes and accessible exact xrefs are coherent. HMDB and original
    NSC naming remain bounded.
  target_ids:
  - CHEBI:233659
  evidence_ids:
  - native
  - chemistry
  - authority
  - xrefs
- assessment_id: activity
  area: evidence
  topic: Growth inhibition, sortase and host-cell endpoints
  outcome: supported
  summary: Original bacterial assays support eligibility. Purified-SrtA evidence offers
    a specific curation lead, with docking, affinity experiments, cellular phenotypes
    and growth MIC kept distinct. Host anticancer/tubulin results are not antimicrobial
    mechanisms.
  target_ids:
  - CHEBI:233659
  evidence_ids:
  - bacterial
  - adopted
  - adapter
- assessment_id: origin
  area: evidence
  topic: Dendrobium statement
  outcome: supported
  summary: Original phytochemical abstract and selected2024 main-text experiments
    support the broad source statement. Candidate biosynthetic enzymes and source
    organism are not antibacterial targets.
  target_ids:
  - CHEBI:233659
  evidence_ids:
  - adopted
  - producer
  - xrefs
- assessment_id: coverage
  area: completeness
  topic: Optional biological fields and record status
  outcome: supported
  summary: Absent optional quantitative activity, mechanism, resistance, producer,
    clinical, graph and dataset fields are not automatic defects in this SEEDED record.
    Useful exact primary leads are documented without treating this review as native
    curation or biological sign-off.
  target_ids:
  - CHEBI:233659
  evidence_ids:
  - native
  - adopted
  - search
- assessment_id: provenance
  area: provenance
  topic: Adopted leads, generated ownership and immutable source capture
  outcome: supported
  summary: Every native field and all ten adopted lead dispositions were covered at
    the stated reading depth. Focused schema, strict and chemistry checks pass, and
    all fourteen captured source inputs remain unchanged.
  target_ids:
  - CHEBI:233659
  evidence_ids:
  - owners
  - native
  - chemistry
  - search
findings: []
actions: []
limitations:
- The ten adopted leads were read as complete indexed abstracts, not ten full papers.
  The2005 HPLC publisher route returned challenge HTML. The2018 antibacterial main
  text and original selected figures were read; raw data and every supplement were
  not reanalyzed.
- The current ChEBI entry has nineteen additional leads beyond the adopted ten; those
  titles were screened, not all their abstracts or full texts. One title is explicitly
  a retraction (PMID39957357) and was not used as evidence.
- The2024 producer paper was read in selected Methods/Results/Discussion sections;
  original spectra and all supplementary figures were not independently inspected.
  HMDB access failed.
- The2018 paper uses fibrinogen in the methods despite fibronectin wording in the
  abstract, and one figure caption dose differs from its legend/methods. These reporting
  limits are not silently reconciled. Exact microdilution details beyond the paper
  and cited standard are not invented.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native or source file was modified. Independent chemistry used the existing batch019
  interpreter against the batch042 records; focused schema and strict gates used the
  batch042 environment.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
