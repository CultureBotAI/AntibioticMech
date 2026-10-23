# Genipin: supported exact seed with a nonverbatim evidence snippet

- Review: 20261021T172701Z-genipin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:15:12Z
- Finished UTC: 2026-10-21T17:27:01Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact genipin structure and narrow canine ocular staphylococcal activity claim are supported by the current chemical authority and the complete cited original study. The one confirmed correction is evidence placement: the source-concept snippet is a curator summary rather than a verbatim passage. The study supports concentration- and time-dependent in vitro activity, not a resolved antibacterial target, MIC values or clinical efficacy. Focused schema, strict and chemistry checks pass.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 494; entire exact native record. All thirteen initial input hashes were verified unchanged before judgment; the generic ChEBI owner list was corrected to the actual curator inventory and seeder without replacing any original input hash.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:curator-a1214aecf9 | data/antibiotics/antibacterial/genipin.yaml | generated | Genipin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | antibioticmech:curator-a1214aecf9 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:curator-a1214aecf9 | Actual focused execution exited 0. |
| Focused chemistry verification | passed | False | antibioticmech:curator-a1214aecf9 | Actual focused execution exited 0. |
| Independent exact chemical authority comparison | passed | False | antibioticmech:curator-a1214aecf9 | All six native, PubChem and corroborating current ChEBI SMILES/InChI encodings reproduce the full native key and three assigned stereocentres. |
| Authoritative full QC | failed | True | antibioticmech:curator-a1214aecf9 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:curator-a1214aecf9 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:curator-a1214aecf9 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:curator-a1214aecf9 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:curator-a1214aecf9 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:curator-a1214aecf9 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:curator-a1214aecf9 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:curator-a1214aecf9 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:curator-a1214aecf9 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Individual structure, name, quantities and exact xref

identity: supported. Targets: antibioticmech:curator-a1214aecf9.

Native, current PubChem and corroborating ChEBI graphs agree. The exact synonym and quantities are supported; a two-star external ChEBI entry does not make the curator seed a duplicate of an adopted ChEBI record.

### Narrow antibacterial definition and activity role

evidence: supported. Targets: antibioticmech:curator-a1214aecf9.

The cited exact commercial genipin experiment directly supports activity against canine ocular staphylococcal isolates. No broad clinical, target or rapid Pseudomonas claim is native. Batch stereochemical recharacterization and solvent/carryover limits remain explicit.

### Source-concept snippet versus interpretation

evidence: concern. Targets: antibioticmech:curator-a1214aecf9.

The adopted reference is correct and the summary is broadly faithful, but the evidence text is a paraphrase in a field explicitly reserved for verbatim quotation.

### Mechanism and optional numerical enrichment

completeness: supported. Targets: antibioticmech:curator-a1214aecf9.

Optional mode, target, numerical activity, producer and graph fields are not required to be filled. The article leaves mechanism unresolved and MIC unmeasurable; those facts justify conservative representation rather than automatic enrichment.

### Curator row, proposal history and input ownership

provenance: supported. Targets: antibioticmech:curator-a1214aecf9.

All fields are traceable to the exact curator row and source-aware seeder, with a reproducible mint and proposal event. The original 13 input hashes were preserved and generic owners corrected before judgment.

## Findings

### F1: Move the genipin study summary out of the verbatim snippet field

minor / open / confirmed; issue key: genipin-curator-summary-in-verbatim-snippet.

source_concepts[0].evidence[0].snippet contains a third-person curator summary beginning Slenter et al. tested genipin. The complete cited original article supports its broad content, but this wording is not a quotation. The schema explicitly defines snippet as verbatim source text. Move the existing summary to evidence_notes in the maintained curator inventory and either omit evidence_snippet or use a short checked quotation.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained genipin evidence column placement and regenerate the exact record.

- Retain DOI10.1167/iovs.67.3.18 and the useful summary in evidence_notes. Remove the paraphrase from evidence_snippet or replace it with a short exact passage checked against the original.
- Regeneration preserves the exact compound selector, mint, chemical structure, PubChem xref and proposal history. Run focused schema/strict and corpus reproduction checks.

### A2

If quantitative activity enrichment is undertaken, preserve the original assay boundaries and resolve source inconsistencies first.

- Do not add MIC values: the study could not determine them. Distinguish MBC from the growth-control-relative time-kill endpoints and preserve isolate, concentration, incubation, medium and DMSO context.
- Resolve the abstract versus Table 1 S.canis range before recording a numerical value. Keep P.aeruginosa long-exposure MBC separate from the negative 120 min time-kill result.
- Do not infer a bacterial molecular target from crosslinking, host effects, background literature or the activity phenotype; retain exact material characterization limits.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/genipin.yaml; Entire YAML: identifier, label, class/status, definition and source, exact synonym, role, all chemical fields, sole exact xref, source-concept evidence and history. | supports | The record is a PROPOSED, MINTED curator seed for one neutral genipin structure. It asserts antibacterial activity against canine ocular staphylococcal isolates and one exact PubChem reference. It has no mode, target, protein/gene/pathway, numerical activity, resistance, producer, clinical status, dataset or causal graph. The single history event accurately identifies the curator inventory proposal, not scientific sign-off. |
| owners | curation/curator_antibiotics.tsv:25; scripts/seed_from_sources.py:617; scripts/seed_from_sources.py:1496; conf/sources.yaml; curation/decisions.tsv; Complete exact curator row, its source/structure/evidence columns, curator loader, class/definition selection and proposal logic; hidden-inclusive exact identity search. | supports | The maintained curator row supplies every native claim. The loader copies evidence_snippet directly into EvidenceItem.snippet and evidence_notes into notes, while preserving explicit class and source version. The DOI fragment source_id is a local compound selector and its reproducible mint is antibioticmech:curator-a1214aecf9. No matching adopted ChEBI or PubChem fallback inventory row was found in the complete inspected tables. Actual ownership is the curator inventory and seeder, not the default ChEBI extraction owner listed by the initial generic capture. |
| identity | pubchem.compound:442424; CHEBI:5298; Complete current PubChem properties and synonyms; complete corroborating ChEBI entry; independent forward graph parsing. | supports | CID442424 agrees exactly with native C11H14O5, charge0, key AZKVWQKMDGGDSV-BCMRRPTOSA-N, average mass226.23 and exact mass226.08412354. It assigns 1R,4aS,7aS stereochemistry and names (+)-Genipin. Current ChEBI5298 independently matches the graph but is a two-star entry outside the maintained adopted antimicrobial slice. That current external identity is not a reason to invalidate the reproducible curator mint or force a source refresh. The fused cyclopentapyran constitution supports the broad iridoid description. |
| role | CHEBI:33282; Complete official role definition. | supports | CHEBI33282 denotes antibacterial agent, covering a substance or active part that kills or slows bacterial growth. The narrow native staphylococcal in vitro claim satisfies that role without implying approval, clinical efficacy, universal strain susceptibility or a particular molecular mechanism. |
| primary | PMID:41800841; DOI:10.1167/iovs.67.3.18; https://pmc.ncbi.nlm.nih.gov/articles/PMC12988688/; Complete original main article from Introduction through Conclusions, Methods, both main tables and all three figure captions; Figures 1–3 additionally inspected visually. Sole adopted publication. | supports | Slenter et al. tested 19 canine corneal-ulcer isolates: ten S. pseudintermedius including five MRSP, five P. aeruginosa and four S. canis. Material was commercial genipin from Challenge Bioproducts with stated 98% HPLC purity, prepared freshly in DMSO/PBS. The paper does not independently recharacterize the batch absolute configuration or give a batch optical rotation; the exact public structure is separately grounded to PubChem. The study directly supports the native broad in vitro antibacterial claim. Tissue crosslinking and other background effects are not demonstrated antibacterial targets in this experiment. |
| assay | PMID:41800841; DOI:10.1167/iovs.67.3.18; Complete inhibitor, MIC/MBC, broth-type, time-kill and statistical Methods; Table 1 and Table 2, Results and corresponding Discussion. | partial | Blue discoloration prevented both visual and spectrophotometric MIC determination. MBC testing used a final approximately 5 × 10^5 CFU/mL inoculum, 22 h exposure at 37 degrees C and subsequent 20 h blood-agar recovery; the stated endpoint was fewer than five colonies from a 10 microlitre aliquot, described as a 3-log reduction. MBC modes are 0.075–0.125% for the tested staphylococci/P. aeruginosa and 0.5% for every S. canis row in Table 1. The abstract instead gives 0.25–0.5% for S. canis; this internal inconsistency needs resolution before quantitative enrichment. It does not conflict with a native numerical claim because none exists. The neutral record must not receive invented MICs or an unqualified species-wide susceptibility range. |
| timekill | PMID:41800841; DOI:10.1167/iovs.67.3.18; Complete time-kill Methods, all Table 2 values, Results/Discussion and direct visual review of Figures 1–3. | supports | Time-kill assays use one selected isolate each of S. pseudintermedius, MRSP and P. aeruginosa, with three independent experiments. The study defines bacteriostatic and bactericidal effects relative to the concurrent growth control, not simply the starting inoculum. Higher genipin concentrations produce the reported mean staphylococcal killing over 60–120 min, with substantial interexperiment variability. P. aeruginosa shows no killing within 120 min despite activity in the longer MBC experiment; S. canis was excluded from time-kill because appropriate logarithmic growth was not achieved. These distinctions support the native limited staphylococcal definition and preclude universal rapid-killing claims. |
| source-limits | PMID:41800841; DOI:10.1167/iovs.67.3.18; Original Discussion and Limitations, all main table notes and supplementary-link retrieval status. | partial | The authors acknowledge possible indirect DMSO effects, unaccounted antimicrobial carryover during plating, unresolved mechanism and lack of direct clinical translation. Their primary main text reports DMSO controls but the separate supplement was not read: the apparent DOCX response was an HTML download challenge. No mechanistic target, safety conclusion, clinical recommendation or in vivo efficacy is inferred from this in vitro experiment. |
| snippet | source_concepts[0].evidence[0].snippet; curation/curator_antibiotics.tsv:25; src/antibioticmech/schema/antibioticmech.yaml:1627; Entire native snippet compared with the complete cited main article and the explicit EvidenceItem.snippet definition. | refutes | The sentence beginning Slenter et al. tested genipin is a third-person synthesis of the study, not a verbatim passage. Its broad factual meaning is supported, but the schema requires a source quotation in snippet and provides notes for interpretation. Preserve the summary and citation by moving it into evidence_notes, leaving snippet empty or replacing it with a short inspected exact quotation. |
| policy | docs/HARMONIZATION.md; docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md; src/antibioticmech/schema/antibioticmech.yaml; Exact identity, minted-source, proposed-status, evidence-placement and optional-coverage rules. | supports | A curator publication-backed source can retain a minted identifier; exact PubChem grounding is independently checkable. Missing optional target/graph/numerical slots are not defects. A verbatim snippet must be distinguished from curator interpretation; PROPOSED is not equivalent to REVIEWED. |
| search | 494-inclusive-hits.txt; 494-owner-hits.txt; 494-raw-rows.json; Hidden- and ignored-inclusive local search across data, curation, conf, scripts, src, docs, .claude, reviews and reports; complete exact source rows; public DOI/PMID and chemical authority retrieval. | context_only | The exact native, maintained owner and source evidence were located and inspected. No claim that primary evidence is absent is made. Structured transcriptomic adapters are not applicable because the native record names no gene, protein, regulator, pathway, stress response or dataset; no target was inferred from newly encountered host background literature. |
| checks | 494-focused-results.json; 494-chemistry.json; 494-authority-chemistry.json; Actual schema/strict/internal chemistry and independent native-authority graph checks; all original input hashes rechecked. | supports | All commands exited 0. Both native encodings reproduce formula, charge, masses, full key and three stereocentres; the mint reproduces from the exact source_id. Original 13 hashes are unchanged. The deterministic checks do not validate whether a paraphrase is a verbatim quotation. |

## Limits And Additional Notes

- The complete main article, both main tables and Figures 1–3 were inspected. The separate supplement was not read because its download response was an HTML challenge rather than a DOCX; supplemental control images and tables are therefore known only through main-text statements.
- The tested commercial material is specified as genipin with 98% HPLC purity and supplier, but no independent batch absolute-configuration measurement or optical rotation is reported in the inspected main text. Public PubChem/ChEBI identity agrees with the native graph.
- The primary study itself reports unresolved MICs, possible DMSO contribution, no carryover correction and no direct clinical translation. Its abstract S.canis MBC range differs from the all 0.5% Table 1 values. These source limitations do not create a native numerical defect because no observations are stored.
- A preliminary ChEBI search endpoint call returned irrelevant search results and was not used as absence or identity evidence; the direct official CHEBI5298 entry was subsequently inspected. No other mechanism or clinical-literature survey is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- The only adopted publication was read in full main-text scope. There are no additional adopted PMIDs in the exact curator source row.
- Source fetch times and SHA256 values are recorded in 494-fetch-results.json through 494-fetch3-results.json; visual figure snapshots are 494-fig1.jpg,494-fig2.jpg and494-fig3.jpg.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T172701Z-genipin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Genipin: supported exact seed with a nonverbatim evidence snippet'
started_at: '2026-10-21T17:15:12Z'
finished_at: '2026-10-21T17:27:01Z'
reviewer:
  identity: Codex review002 subagent
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
summary: 'The exact genipin structure and narrow canine ocular staphylococcal activity
  claim are supported by the current chemical authority and the complete cited original
  study. The one confirmed correction is evidence placement: the source-concept snippet
  is a curator summary rather than a verbatim passage. The study supports concentration-
  and time-dependent in vitro activity, not a resolved antibacterial target, MIC values
  or clinical efficacy. Focused schema, strict and chemistry checks pass.'
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
  - path: data/antibiotics/antibacterial/genipin.yaml
    sha256: d40f85a5ec46f71df086e0b99f321d61395eaedb877a338451bd81eafbbeb6d3
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
- target_id: antibioticmech:curator-a1214aecf9
  path: data/antibiotics/antibacterial/genipin.yaml
  label: Genipin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Exact curator seed row and primary evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator inventory import and structure/source evidence handling
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained grounding decision when needed
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 494; entire exact native record. All thirteen initial
    input hashes were verified unchanged before judgment; the generic ChEBI owner
    list was corrected to the actual curator inventory and seeder without replacing
    any original input hash.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:curator-a1214aecf9
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-a1214aecf9
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/genipin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-a1214aecf9
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/genipin.yaml --out /private/tmp/am-review-session/494-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-a1214aecf9
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 494
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-chemistry
  name: Independent exact chemical authority comparison
  status: passed
  required: false
  summary: All six native, PubChem and corroborating current ChEBI SMILES/InChI encodings
    reproduce the full native key and three assigned stereocentres.
  target_ids:
  - antibioticmech:curator-a1214aecf9
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/494-authority-check.py
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
  - antibioticmech:curator-a1214aecf9
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
  - antibioticmech:curator-a1214aecf9
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
  - antibioticmech:curator-a1214aecf9
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
  - antibioticmech:curator-a1214aecf9
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
  - antibioticmech:curator-a1214aecf9
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
  - antibioticmech:curator-a1214aecf9
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
  - antibioticmech:curator-a1214aecf9
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
  - antibioticmech:curator-a1214aecf9
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
  - antibioticmech:curator-a1214aecf9
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/genipin.yaml
  locator: 'Entire YAML: identifier, label, class/status, definition and source, exact
    synonym, role, all chemical fields, sole exact xref, source-concept evidence and
    history.'
  accessed_at: '2026-10-21T17:22:21Z'
  support: supports
  summary: The record is a PROPOSED, MINTED curator seed for one neutral genipin structure.
    It asserts antibacterial activity against canine ocular staphylococcal isolates
    and one exact PubChem reference. It has no mode, target, protein/gene/pathway,
    numerical activity, resistance, producer, clinical status, dataset or causal graph.
    The single history event accurately identifies the curator inventory proposal,
    not scientific sign-off.
- evidence_id: owners
  kind: record_content
  reference: curation/curator_antibiotics.tsv:25; scripts/seed_from_sources.py:617;
    scripts/seed_from_sources.py:1496; conf/sources.yaml; curation/decisions.tsv
  locator: Complete exact curator row, its source/structure/evidence columns, curator
    loader, class/definition selection and proposal logic; hidden-inclusive exact
    identity search.
  accessed_at: '2026-10-21T17:22:21Z'
  support: supports
  summary: The maintained curator row supplies every native claim. The loader copies
    evidence_snippet directly into EvidenceItem.snippet and evidence_notes into notes,
    while preserving explicit class and source version. The DOI fragment source_id
    is a local compound selector and its reproducible mint is antibioticmech:curator-a1214aecf9.
    No matching adopted ChEBI or PubChem fallback inventory row was found in the complete
    inspected tables. Actual ownership is the curator inventory and seeder, not the
    default ChEBI extraction owner listed by the initial generic capture.
  snapshot_sha256: d3e0bf2b7abaaf6cc302ecf4d61399cf4d385c7d2b87a6917e11c34533b4e4bc
- evidence_id: identity
  kind: authority
  reference: pubchem.compound:442424; CHEBI:5298
  locator: Complete current PubChem properties and synonyms; complete corroborating
    ChEBI entry; independent forward graph parsing.
  accessed_at: '2026-10-21T17:22:21Z'
  support: supports
  summary: CID442424 agrees exactly with native C11H14O5, charge0, key AZKVWQKMDGGDSV-BCMRRPTOSA-N,
    average mass226.23 and exact mass226.08412354. It assigns 1R,4aS,7aS stereochemistry
    and names (+)-Genipin. Current ChEBI5298 independently matches the graph but is
    a two-star entry outside the maintained adopted antimicrobial slice. That current
    external identity is not a reason to invalidate the reproducible curator mint
    or force a source refresh. The fused cyclopentapyran constitution supports the
    broad iridoid description.
  snapshot_sha256: 5daf05f8101e2d6596ed0db6057a067c723d9b92b6c55e2f99abe9141983028a
- evidence_id: role
  kind: authority
  reference: CHEBI:33282
  locator: Complete official role definition.
  accessed_at: '2026-10-21T17:19:47Z'
  support: supports
  summary: CHEBI33282 denotes antibacterial agent, covering a substance or active
    part that kills or slows bacterial growth. The narrow native staphylococcal in
    vitro claim satisfies that role without implying approval, clinical efficacy,
    universal strain susceptibility or a particular molecular mechanism.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: primary
  kind: primary_source
  reference: PMID:41800841; DOI:10.1167/iovs.67.3.18; https://pmc.ncbi.nlm.nih.gov/articles/PMC12988688/
  locator: Complete original main article from Introduction through Conclusions, Methods,
    both main tables and all three figure captions; Figures 1–3 additionally inspected
    visually. Sole adopted publication.
  accessed_at: '2026-10-21T17:20:01Z'
  support: supports
  summary: 'Slenter et al. tested 19 canine corneal-ulcer isolates: ten S. pseudintermedius
    including five MRSP, five P. aeruginosa and four S. canis. Material was commercial
    genipin from Challenge Bioproducts with stated 98% HPLC purity, prepared freshly
    in DMSO/PBS. The paper does not independently recharacterize the batch absolute
    configuration or give a batch optical rotation; the exact public structure is
    separately grounded to PubChem. The study directly supports the native broad in
    vitro antibacterial claim. Tissue crosslinking and other background effects are
    not demonstrated antibacterial targets in this experiment.'
  snapshot_sha256: b0ca6f5a3a3faee539efa80463aa56ef2b5f0e883984fc78d6d1a23b02ff7a30
- evidence_id: assay
  kind: primary_source
  reference: PMID:41800841; DOI:10.1167/iovs.67.3.18
  locator: Complete inhibitor, MIC/MBC, broth-type, time-kill and statistical Methods;
    Table 1 and Table 2, Results and corresponding Discussion.
  accessed_at: '2026-10-21T17:20:01Z'
  support: partial
  summary: Blue discoloration prevented both visual and spectrophotometric MIC determination.
    MBC testing used a final approximately 5 × 10^5 CFU/mL inoculum, 22 h exposure
    at 37 degrees C and subsequent 20 h blood-agar recovery; the stated endpoint was
    fewer than five colonies from a 10 microlitre aliquot, described as a 3-log reduction.
    MBC modes are 0.075–0.125% for the tested staphylococci/P. aeruginosa and 0.5%
    for every S. canis row in Table 1. The abstract instead gives 0.25–0.5% for S.
    canis; this internal inconsistency needs resolution before quantitative enrichment.
    It does not conflict with a native numerical claim because none exists. The neutral
    record must not receive invented MICs or an unqualified species-wide susceptibility
    range.
  snapshot_sha256: b0ca6f5a3a3faee539efa80463aa56ef2b5f0e883984fc78d6d1a23b02ff7a30
- evidence_id: timekill
  kind: primary_source
  reference: PMID:41800841; DOI:10.1167/iovs.67.3.18
  locator: Complete time-kill Methods, all Table 2 values, Results/Discussion and
    direct visual review of Figures 1–3.
  accessed_at: '2026-10-21T17:20:01Z'
  support: supports
  summary: Time-kill assays use one selected isolate each of S. pseudintermedius,
    MRSP and P. aeruginosa, with three independent experiments. The study defines
    bacteriostatic and bactericidal effects relative to the concurrent growth control,
    not simply the starting inoculum. Higher genipin concentrations produce the reported
    mean staphylococcal killing over 60–120 min, with substantial interexperiment
    variability. P. aeruginosa shows no killing within 120 min despite activity in
    the longer MBC experiment; S. canis was excluded from time-kill because appropriate
    logarithmic growth was not achieved. These distinctions support the native limited
    staphylococcal definition and preclude universal rapid-killing claims.
  snapshot_sha256: b0ca6f5a3a3faee539efa80463aa56ef2b5f0e883984fc78d6d1a23b02ff7a30
- evidence_id: source-limits
  kind: primary_source
  reference: PMID:41800841; DOI:10.1167/iovs.67.3.18
  locator: Original Discussion and Limitations, all main table notes and supplementary-link
    retrieval status.
  accessed_at: '2026-10-21T17:20:01Z'
  support: partial
  summary: 'The authors acknowledge possible indirect DMSO effects, unaccounted antimicrobial
    carryover during plating, unresolved mechanism and lack of direct clinical translation.
    Their primary main text reports DMSO controls but the separate supplement was
    not read: the apparent DOCX response was an HTML download challenge. No mechanistic
    target, safety conclusion, clinical recommendation or in vivo efficacy is inferred
    from this in vitro experiment.'
  snapshot_sha256: b0ca6f5a3a3faee539efa80463aa56ef2b5f0e883984fc78d6d1a23b02ff7a30
- evidence_id: snippet
  kind: record_content
  reference: source_concepts[0].evidence[0].snippet; curation/curator_antibiotics.tsv:25;
    src/antibioticmech/schema/antibioticmech.yaml:1627
  locator: Entire native snippet compared with the complete cited main article and
    the explicit EvidenceItem.snippet definition.
  accessed_at: '2026-10-21T17:22:21Z'
  support: refutes
  summary: The sentence beginning Slenter et al. tested genipin is a third-person
    synthesis of the study, not a verbatim passage. Its broad factual meaning is supported,
    but the schema requires a source quotation in snippet and provides notes for interpretation.
    Preserve the summary and citation by moving it into evidence_notes, leaving snippet
    empty or replacing it with a short inspected exact quotation.
- evidence_id: policy
  kind: record_content
  reference: docs/HARMONIZATION.md; docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md;
    src/antibioticmech/schema/antibioticmech.yaml
  locator: Exact identity, minted-source, proposed-status, evidence-placement and
    optional-coverage rules.
  accessed_at: '2026-10-21T17:22:21Z'
  support: supports
  summary: A curator publication-backed source can retain a minted identifier; exact
    PubChem grounding is independently checkable. Missing optional target/graph/numerical
    slots are not defects. A verbatim snippet must be distinguished from curator interpretation;
    PROPOSED is not equivalent to REVIEWED.
- evidence_id: search
  kind: search
  reference: 494-inclusive-hits.txt; 494-owner-hits.txt; 494-raw-rows.json
  locator: Hidden- and ignored-inclusive local search across data, curation, conf,
    scripts, src, docs, .claude, reviews and reports; complete exact source rows;
    public DOI/PMID and chemical authority retrieval.
  accessed_at: '2026-10-21T17:22:21Z'
  support: context_only
  summary: The exact native, maintained owner and source evidence were located and
    inspected. No claim that primary evidence is absent is made. Structured transcriptomic
    adapters are not applicable because the native record names no gene, protein,
    regulator, pathway, stress response or dataset; no target was inferred from newly
    encountered host background literature.
  search_scope: 2026-10-21; rg --no-ignore --hidden for genipin/Genipin, curator-a1214aecf9
    and iovs.67.3.18 across maintained and ignored-inclusive local evidence paths;
    exact PubChem442424, CHEBI5298, CHEBI33282 and DOI/PMID retrieval.
  snapshot_sha256: 95c7e5f3d64095a5682d8ccab3ab029375a7f74891733227bb9c9085a499408f
- evidence_id: checks
  kind: validation
  reference: 494-focused-results.json; 494-chemistry.json; 494-authority-chemistry.json
  locator: Actual schema/strict/internal chemistry and independent native-authority
    graph checks; all original input hashes rechecked.
  accessed_at: '2026-10-21T17:22:21Z'
  support: supports
  summary: All commands exited 0. Both native encodings reproduce formula, charge,
    masses, full key and three stereocentres; the mint reproduces from the exact source_id.
    Original 13 hashes are unchanged. The deterministic checks do not validate whether
    a paraphrase is a verbatim quotation.
  snapshot_sha256: 4fdb39c18fc72de69df746e949dd714d0449333fbb640d4dd75d5127993819bd
assessments:
- assessment_id: identity
  area: identity
  topic: Individual structure, name, quantities and exact xref
  outcome: supported
  summary: Native, current PubChem and corroborating ChEBI graphs agree. The exact
    synonym and quantities are supported; a two-star external ChEBI entry does not
    make the curator seed a duplicate of an adopted ChEBI record.
  target_ids:
  - antibioticmech:curator-a1214aecf9
  evidence_ids:
  - identity
  - owners
  - checks
  - policy
- assessment_id: activity
  area: evidence
  topic: Narrow antibacterial definition and activity role
  outcome: supported
  summary: The cited exact commercial genipin experiment directly supports activity
    against canine ocular staphylococcal isolates. No broad clinical, target or rapid
    Pseudomonas claim is native. Batch stereochemical recharacterization and solvent/carryover
    limits remain explicit.
  target_ids:
  - antibioticmech:curator-a1214aecf9
  evidence_ids:
  - primary
  - role
  - assay
  - timekill
  - source-limits
- assessment_id: evidence-placement
  area: evidence
  topic: Source-concept snippet versus interpretation
  outcome: concern
  summary: The adopted reference is correct and the summary is broadly faithful, but
    the evidence text is a paraphrase in a field explicitly reserved for verbatim
    quotation.
  target_ids:
  - antibioticmech:curator-a1214aecf9
  evidence_ids:
  - snippet
  - owners
  - primary
  - policy
- assessment_id: coverage
  area: completeness
  topic: Mechanism and optional numerical enrichment
  outcome: supported
  summary: Optional mode, target, numerical activity, producer and graph fields are
    not required to be filled. The article leaves mechanism unresolved and MIC unmeasurable;
    those facts justify conservative representation rather than automatic enrichment.
  target_ids:
  - antibioticmech:curator-a1214aecf9
  evidence_ids:
  - native
  - assay
  - source-limits
  - search
  - policy
- assessment_id: provenance
  area: provenance
  topic: Curator row, proposal history and input ownership
  outcome: supported
  summary: All fields are traceable to the exact curator row and source-aware seeder,
    with a reproducible mint and proposal event. The original 13 input hashes were
    preserved and generic owners corrected before judgment.
  target_ids:
  - antibioticmech:curator-a1214aecf9
  evidence_ids:
  - native
  - owners
  - checks
findings:
- finding_id: F1
  issue_key: genipin-curator-summary-in-verbatim-snippet
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Move the genipin study summary out of the verbatim snippet field
  description: source_concepts[0].evidence[0].snippet contains a third-person curator
    summary beginning Slenter et al. tested genipin. The complete cited original article
    supports its broad content, but this wording is not a quotation. The schema explicitly
    defines snippet as verbatim source text. Move the existing summary to evidence_notes
    in the maintained curator inventory and either omit evidence_snippet or use a
    short checked quotation.
  target_ids:
  - antibioticmech:curator-a1214aecf9
  field_paths:
  - source_concepts[0].evidence[0].snippet
  evidence_ids:
  - snippet
  - primary
  - owners
  - policy
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Exact genipin row evidence_snippet and evidence_notes
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Preserves curator evidence field semantics during regeneration
  rule_id: EvidenceItem.snippet must contain verbatim source text
  native_severity: minor
  normalization_reason: The reference and narrow activity claim are supported; the
    defect is bounded evidence-format attribution rather than unsupported antibacterial
    activity or wrong chemical identity.
actions:
- action_id: A1
  description: Correct the maintained genipin evidence column placement and regenerate
    the exact record.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:curator-a1214aecf9
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Exact genipin row evidence_snippet and evidence_notes
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Preserves curator evidence field semantics during regeneration
  acceptance_checks:
  - Retain DOI10.1167/iovs.67.3.18 and the useful summary in evidence_notes. Remove
    the paraphrase from evidence_snippet or replace it with a short exact passage
    checked against the original.
  - Regeneration preserves the exact compound selector, mint, chemical structure,
    PubChem xref and proposal history. Run focused schema/strict and corpus reproduction
    checks.
- action_id: A2
  description: If quantitative activity enrichment is undertaken, preserve the original
    assay boundaries and resolve source inconsistencies first.
  finding_ids: []
  target_ids:
  - antibioticmech:curator-a1214aecf9
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/genipin.yaml
    role: Optional curator-owned claim additions through the validated writer
  acceptance_checks:
  - 'Do not add MIC values: the study could not determine them. Distinguish MBC from
    the growth-control-relative time-kill endpoints and preserve isolate, concentration,
    incubation, medium and DMSO context.'
  - Resolve the abstract versus Table 1 S.canis range before recording a numerical
    value. Keep P.aeruginosa long-exposure MBC separate from the negative 120 min
    time-kill result.
  - Do not infer a bacterial molecular target from crosslinking, host effects, background
    literature or the activity phenotype; retain exact material characterization limits.
limitations:
- The complete main article, both main tables and Figures 1–3 were inspected. The
  separate supplement was not read because its download response was an HTML challenge
  rather than a DOCX; supplemental control images and tables are therefore known only
  through main-text statements.
- The tested commercial material is specified as genipin with 98% HPLC purity and
  supplier, but no independent batch absolute-configuration measurement or optical
  rotation is reported in the inspected main text. Public PubChem/ChEBI identity agrees
  with the native graph.
- The primary study itself reports unresolved MICs, possible DMSO contribution, no
  carryover correction and no direct clinical translation. Its abstract S.canis MBC
  range differs from the all 0.5% Table 1 values. These source limitations do not
  create a native numerical defect because no observations are stored.
- A preliminary ChEBI search endpoint call returned irrelevant search results and
  was not used as absence or identity evidence; the direct official CHEBI5298 entry
  was subsequently inspected. No other mechanism or clinical-literature survey is
  claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- The only adopted publication was read in full main-text scope. There are no additional
  adopted PMIDs in the exact curator source row.
- Source fetch times and SHA256 values are recorded in 494-fetch-results.json through
  494-fetch3-results.json; visual figure snapshots are 494-fig1.jpg,494-fig2.jpg and494-fig3.jpg.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
