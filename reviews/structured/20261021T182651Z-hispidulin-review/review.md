# Hispidulin: exact flavone and primary antibacterial evidence supported

- Review: 20261021T182651Z-hispidulin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:00:58Z
- Finished UTC: 2026-10-21T18:26:51Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native neutral hispidulin structure agrees with current PubChem and ChEBI and the named reagent in the adopted primary study. The study directly supports growth inhibition of resistant bacterial strains. Its efflux and antibiotic-combination experiments concern orientin and isoorientin, and are not transferred to hispidulin. The scientific claims are supported, but the source evidence snippet is a curator paraphrase and should be moved to notes.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position535; entire native PROPOSED curator record and actual maintained owner. All original13 inputs retained.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:curator-b453af7884 | data/antibiotics/antibacterial/hispidulin.yaml | generated | Hispidulin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:curator-b453af7884 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:curator-b453af7884 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:curator-b453af7884 | Actual focused execution exited 0. |
| Independent native and authority graph comparison | passed | False | antibioticmech:curator-b453af7884 | All six native, PubChem and ChEBI encodings reproduce the full key, formula, charge and reciprocal graph match. |
| Authoritative full QC | failed | True | antibioticmech:curator-b453af7884 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:curator-b453af7884 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:curator-b453af7884 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:curator-b453af7884 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:curator-b453af7884 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:curator-b453af7884 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:curator-b453af7884 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:curator-b453af7884 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:curator-b453af7884 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact chemical identity and external equivalence

identity: supported. Targets: antibioticmech:curator-b453af7884.

Neutral hispidulin, its formula/masses and the sole native PubChem xref agree across six encodings. Original reagent naming/formula/purity identifies the same aglycone; no glycoside, acetate, salt or plant extract is substituted.

### Resistant-pathogen antibacterial claim

evidence: supported. Targets: antibioticmech:curator-b453af7884.

The adopted original includes explicit hispidulin inhibition of MRSA and ESBL bacterial strains, independently of the other five active flavonoids. The source-concept summary is faithful at its broad qualitative scope.

### Efflux, synergy and safety boundaries

evidence: supported. Targets: antibioticmech:curator-b453af7884.

No hispidulin molecular target or efflux claim appears in the native. Orientin/isoorientin experiments and Artemia toxicity are kept within their exact compounds, assays and organisms. Optional unpopulated objects are not defects.

### Curator ownership, source citation and history

provenance: supported. Targets: antibioticmech:curator-b453af7884.

The exact curator row, stable mint, explicit class, attached source evidence and one chronological proposal event reproduce through the inspected seeder. All thirteen initial hashes are retained and native status remains PROPOSED.

### Optional enrichment and actual access limits

completeness: unknown. Targets: antibioticmech:curator-b453af7884.

The main original supports the current record, but final microdilution timing/readout, replicate reporting, supplier certificate and Fig.S1c remain incompletely resolved. They would need attention before adding quantitative assay rows or stronger identity/clinical claims.

### Paraphrase stored as source quotation

provenance: concern. Targets: antibioticmech:curator-b453af7884.

The attached citation and scientific summary are valid, but the paraphrase is in the verbatim-only snippet slot. Move the summary to notes or use an inspected short exact quotation.

## Findings

### F1: A curator paraphrase occupies the verbatim snippet field

minor / open / confirmed; issue key: hispidulin-source-evidence-paraphrase-in-snippet.

The source-concept evidence snippet beginning Zai et al. reported hispidulin is a faithful curator summary, not a verbatim passage from the cited original. The explicit checklist requires verbatim snippets and places interpretation in notes. This is an evidence-format defect; the antibacterial and identity claims remain supported.

## Recommended Actions And Acceptance Checks

### A0

Move the faithful paper summary from evidence_snippet to evidence_notes in the maintained curator row, preserving the existing chemistry provenance note and citation, or replace it with a short verified verbatim passage.

- The emitted source evidence has only an actual inspected verbatim quotation in snippet, or no snippet; the faithful summary is retained in notes.
- Preserve the DOI, exact chemical graph, antibacterial scope and PROPOSED status, then regenerate through maintained owners and run focused and corpus checks.

### A1

If later adding quantitative activity, preserve exact-compound and assay boundaries.

- Retain the exact Table1 hispidulin row, named strains and unnamed clinical isolate; inspect cited microdilution methods and reconcile replicate descriptions before constructing full assay observations.
- Do not transfer orientin/isoorientin efflux or combination findings to hispidulin. Artemia LC50 and derived ratios do not establish human safety or clinical use.
- Inspect actual Fig.S1c and a relevant reagent certificate if a future identity decision requires that depth; preserve all already corroborated molecular fields.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/hispidulin.yaml; Entire YAML, including definition citation, exact chemistry/xref, source-concept evidence snippet/notes and one proposal history event. | supports | The record denotes neutral C16H12O6 hispidulin, IHFBPDAQLQOCBX-UHFFFAOYSA-N. It is MINTED/PROPOSED from the curator inventory and asserts broad antibacterial activity against resistant pathogens. It contains no aliases, parent classes, target, MIC row, resistance mechanism, producer, causal graph or clinical assertion. The source-concept citation is explicitly attached to the publication-backed provenance claim. |
| owner | curation/curator_antibiotics.tsv:17; scripts/seed_from_sources.py:617; scripts/seed_from_sources.py:1496; scripts/seed_from_sources.py:1661; Complete exact curator row and load_curator_concepts, definition/class selection, source evidence emission and PROPOSED_FROM_CURATOR_INVENTORY code. | supports | The maintained row supplies all native claims and PubChem source details. Curator-only concepts deliberately receive stable minted identity and PROPOSED status; the definition source is the row publication. Source version and structure retrieval are2026-09-07 and the proposal event is2026-09-08. Current ChEBI availability does not by itself make the source mint wrong or authorize merging with another concept. |
| chemistry | PubChem:5281628; CHEBI:75902; Current official PubChem property response, exact ChEBI search result and full record; six independent SMILES/InChI parses. | supports | All encodings agree at full key, formula, neutral charge and graph. The compound is5,7,4-prime-trihydroxy-6-methoxyflavone, consistent with the ChEBI description of6-O-methylscutellarein. There are no stereocentres or salt components. Average and exact masses agree within displayed precision. The exact PubChem xref is independently verified; ChEBI is a comparison authority, not an asserted native xref. |
| role | CHEBI:33282; Current official role definition. | supports | The antibacterial role denotes killing or slowing bacterial growth, compatible with the exact-compound growth-inhibition observations. The native broad classification does not assert bactericidal action, clinical efficacy or a particular molecular target. |
| primary | DOI:10.1128/spectrum.02374-25; PMC12955415; https://pmc.ncbi.nlm.nih.gov/articles/PMC12955415/; Complete original Abstract, Introduction, Results, Discussion and Materials/Methods read from public XML/HTML; all four HTML tables and figure captions read. Raw main figure panels and supplement were not independently inspected. | supports | Zai et al. explicitly test hispidulin among15 purified commercial flavonoids. Table4 identifies Adooq A13945, &gt;98% purity, C16H12O6 and300.26g/mol, procured through Sapphire Biosciences. This is a named exact reagent, not a Terminalia extract assay. Table1 gives hispidulin MICs125,250,250,125,125,125 micrograms/mL in the order E.coli ATCC25922, unnamed hospital ESBL E.coli, K.pneumoniae ATCC31488, ESBL K.pneumoniae ATCC700603, S.aureus ATCC25923 and MRSA ATCC43300. The native broad definition and evidence snippet are directly supported. |
| assay | DOI:10.1128/spectrum.02374-25; Original Materials, Bacterial strains/culture growth, Liquid microdilution, Statistical analysis and Table1 footnotes. | supports | Mueller-Hinton broth/agar and serial twofold dilutions from250 micrograms/mL were used, with0.6% DMSO in the first tested well. Growth preparation was37 degrees C except MRSA at35 degrees C. The main refers to an earlier method for complete microdilution details and does not spell out the full final MIC incubation/readout protocol here. Table1 and the microdilution paragraph describe n=3, whereas statistical text also describes two days with internal n=4; this source reporting difference must be resolved before quantitative enrichment. The reviewer does not silently turn preparation temperature into a fully specified final MIC protocol. |
| scope | DOI:10.1128/spectrum.02374-25; Original combination/efflux Results and Methods, Tables2–3, and complete Discussion. | supports | Only orientin and isoorientin proceed to antibiotic combinations and ethidium-bromide accumulation/efflux testing. Those experiments do not establish hispidulin efflux-pump inhibition, antibiotic synergy or direct protein binding. Hispidulin has Artemia LC50&gt;2000 micrograms/mL in Table3; the authors call this non-toxic in that assay, but it is not human safety, clinical therapeutic index or regulatory approval. The broad Discussion contains general flavonoid mechanisms and even conflates gyrase with topoisomeraseIV; those statements are not imported into the native record. |
| access | 054-root-fetch1.json;054-root-fetch2.json;054-root-fetch3.json;535-local-hits.txt; Ignored/hidden-inclusive native capture and exact owner/key follow-up; current authority retrieval and attempted official supplementary/supplier routes. | partial | The one adopted DOI resolves to the inspected original. The supplier page returned403; its exact lot and certificate were not independently verified beyond original Table4. The publisher supplement returned403 and the alternate PMC binary path404; an earlier instance-path download was only a redirect shell. Fig.S1c therefore remains uninspected. This is a bounded native-claim review, not an exhaustive hispidulin mechanism or natural-occurrence literature survey. |
| snippet-placement | .claude/skills/curate-yaml-record/references/review-checklist.md:14; curation/curator_antibiotics.tsv:17; Verbatim-snippet rule compared with the entire original scientific text and native source evidence. | supports | The checklist reserves snippet for a short verbatim source passage and notes for curator interpretation. The native phrase beginning Zai et al. reported hispidulin summarizes the paper; it is not a quoted passage. Its biological content remains supported by the exact hispidulin table row. The maintained curator evidence_snippet is projected unchanged by the seeder. |

## Limits And Additional Notes

- The complete main scientific text, four HTML tables and all captions were read. Main raw figure panels concern other compounds and were not independently reprocessed; the linked supplement including Fig.S1c could not be obtained through the attempted free routes.
- The exact commercial reagent is identified by original Table4, but its batch-specific certificate and supplier page were not inspected because the page returned403.
- The original main defers final microdilution details to earlier methods and has differing replicate descriptions. No complete assay observation is newly asserted by this review.
- The review follows the one adopted primary citation and exact authorities. It does not claim exhaustive hispidulin literature, biosynthetic origin, resistance or mechanistic coverage.
- No populated native protein/pathway or expression-dataset assertion requires a structured target-dataset query. The paper efflux experiments are explicitly for other flavonoids.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- The original paper XML/HTML was already retrieved during this review campaign for another compound; it was reread independently for exact hispidulin claims. The current DOI metadata and chemical authorities were fetched again.
- All native and maintained source files are unchanged. This draft does not promote PROPOSED to REVIEWED or add quantitative activity.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T182651Z-hispidulin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Hispidulin: exact flavone and primary antibacterial evidence supported'
started_at: '2026-10-21T18:00:58Z'
finished_at: '2026-10-21T18:26:51Z'
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
summary: The native neutral hispidulin structure agrees with current PubChem and ChEBI
  and the named reagent in the adopted primary study. The study directly supports
  growth inhibition of resistant bacterial strains. Its efflux and antibiotic-combination
  experiments concern orientin and isoorientin, and are not transferred to hispidulin.
  The scientific claims are supported, but the source evidence snippet is a curator
  paraphrase and should be moved to notes.
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
  - path: data/antibiotics/antibacterial/hispidulin.yaml
    sha256: fee5ef69c7a6535effc03ddae7059a5a62fc0b155f6f181effed9e6290d5070a
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
- target_id: antibioticmech:curator-b453af7884
  path: data/antibiotics/antibacterial/hispidulin.yaml
  label: Hispidulin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Publication-backed exact compound, definition and evidence owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator concept loading, identity mint and native emission
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Class and identifier normalization context
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position535; entire native PROPOSED curator
    record and actual maintained owner. All original13 inputs retained.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:curator-b453af7884
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-b453af7884
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    535
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-b453af7884
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/hispidulin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-b453af7884
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/hispidulin.yaml --out /private/tmp/am-review-session/535-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority
  name: Independent native and authority graph comparison
  status: passed
  required: false
  summary: All six native, PubChem and ChEBI encodings reproduce the full key, formula,
    charge and reciprocal graph match.
  target_ids:
  - antibioticmech:curator-b453af7884
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/535-authorities.py
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
  - antibioticmech:curator-b453af7884
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
  - antibioticmech:curator-b453af7884
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
  - antibioticmech:curator-b453af7884
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
  - antibioticmech:curator-b453af7884
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
  - antibioticmech:curator-b453af7884
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
  - antibioticmech:curator-b453af7884
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
  - antibioticmech:curator-b453af7884
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
  - antibioticmech:curator-b453af7884
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
  - antibioticmech:curator-b453af7884
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/hispidulin.yaml
  locator: Entire YAML, including definition citation, exact chemistry/xref, source-concept
    evidence snippet/notes and one proposal history event.
  accessed_at: '2026-10-21T18:09:36Z'
  support: supports
  summary: The record denotes neutral C16H12O6 hispidulin, IHFBPDAQLQOCBX-UHFFFAOYSA-N.
    It is MINTED/PROPOSED from the curator inventory and asserts broad antibacterial
    activity against resistant pathogens. It contains no aliases, parent classes,
    target, MIC row, resistance mechanism, producer, causal graph or clinical assertion.
    The source-concept citation is explicitly attached to the publication-backed provenance
    claim.
- evidence_id: owner
  kind: record_content
  reference: curation/curator_antibiotics.tsv:17; scripts/seed_from_sources.py:617;
    scripts/seed_from_sources.py:1496; scripts/seed_from_sources.py:1661
  locator: Complete exact curator row and load_curator_concepts, definition/class
    selection, source evidence emission and PROPOSED_FROM_CURATOR_INVENTORY code.
  accessed_at: '2026-10-21T18:09:36Z'
  support: supports
  summary: The maintained row supplies all native claims and PubChem source details.
    Curator-only concepts deliberately receive stable minted identity and PROPOSED
    status; the definition source is the row publication. Source version and structure
    retrieval are2026-09-07 and the proposal event is2026-09-08. Current ChEBI availability
    does not by itself make the source mint wrong or authorize merging with another
    concept.
  snapshot_sha256: ab3085943ad8776137d45f7c08e14a2ca1254417c6b6394d74c8acf6817be849
- evidence_id: chemistry
  kind: authority
  reference: PubChem:5281628; CHEBI:75902
  locator: Current official PubChem property response, exact ChEBI search result and
    full record; six independent SMILES/InChI parses.
  accessed_at: '2026-10-21T18:09:36Z'
  support: supports
  summary: All encodings agree at full key, formula, neutral charge and graph. The
    compound is5,7,4-prime-trihydroxy-6-methoxyflavone, consistent with the ChEBI
    description of6-O-methylscutellarein. There are no stereocentres or salt components.
    Average and exact masses agree within displayed precision. The exact PubChem xref
    is independently verified; ChEBI is a comparison authority, not an asserted native
    xref.
  snapshot_sha256: 1abff160269048bf9c0f8b03a17cdf85de5aeb6d109ef4fecc94006b90f3e63f
- evidence_id: role
  kind: authority
  reference: CHEBI:33282
  locator: Current official role definition.
  accessed_at: '2026-10-21T18:09:36Z'
  support: supports
  summary: The antibacterial role denotes killing or slowing bacterial growth, compatible
    with the exact-compound growth-inhibition observations. The native broad classification
    does not assert bactericidal action, clinical efficacy or a particular molecular
    target.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: primary
  kind: primary_source
  reference: DOI:10.1128/spectrum.02374-25; PMC12955415; https://pmc.ncbi.nlm.nih.gov/articles/PMC12955415/
  locator: Complete original Abstract, Introduction, Results, Discussion and Materials/Methods
    read from public XML/HTML; all four HTML tables and figure captions read. Raw
    main figure panels and supplement were not independently inspected.
  accessed_at: '2026-10-21T18:09:36Z'
  support: supports
  summary: Zai et al. explicitly test hispidulin among15 purified commercial flavonoids.
    Table4 identifies Adooq A13945, >98% purity, C16H12O6 and300.26g/mol, procured
    through Sapphire Biosciences. This is a named exact reagent, not a Terminalia
    extract assay. Table1 gives hispidulin MICs125,250,250,125,125,125 micrograms/mL
    in the order E.coli ATCC25922, unnamed hospital ESBL E.coli, K.pneumoniae ATCC31488,
    ESBL K.pneumoniae ATCC700603, S.aureus ATCC25923 and MRSA ATCC43300. The native
    broad definition and evidence snippet are directly supported.
  snapshot_sha256: e3f3cc81fbcbb83c68396688f660b3a652176996c9ebeaf5463d2691a3163d6c
- evidence_id: assay
  kind: primary_source
  reference: DOI:10.1128/spectrum.02374-25
  locator: Original Materials, Bacterial strains/culture growth, Liquid microdilution,
    Statistical analysis and Table1 footnotes.
  accessed_at: '2026-10-21T18:09:36Z'
  support: supports
  summary: Mueller-Hinton broth/agar and serial twofold dilutions from250 micrograms/mL
    were used, with0.6% DMSO in the first tested well. Growth preparation was37 degrees
    C except MRSA at35 degrees C. The main refers to an earlier method for complete
    microdilution details and does not spell out the full final MIC incubation/readout
    protocol here. Table1 and the microdilution paragraph describe n=3, whereas statistical
    text also describes two days with internal n=4; this source reporting difference
    must be resolved before quantitative enrichment. The reviewer does not silently
    turn preparation temperature into a fully specified final MIC protocol.
  snapshot_sha256: e3f3cc81fbcbb83c68396688f660b3a652176996c9ebeaf5463d2691a3163d6c
- evidence_id: scope
  kind: primary_source
  reference: DOI:10.1128/spectrum.02374-25
  locator: Original combination/efflux Results and Methods, Tables2–3, and complete
    Discussion.
  accessed_at: '2026-10-21T18:09:36Z'
  support: supports
  summary: Only orientin and isoorientin proceed to antibiotic combinations and ethidium-bromide
    accumulation/efflux testing. Those experiments do not establish hispidulin efflux-pump
    inhibition, antibiotic synergy or direct protein binding. Hispidulin has Artemia
    LC50>2000 micrograms/mL in Table3; the authors call this non-toxic in that assay,
    but it is not human safety, clinical therapeutic index or regulatory approval.
    The broad Discussion contains general flavonoid mechanisms and even conflates
    gyrase with topoisomeraseIV; those statements are not imported into the native
    record.
  snapshot_sha256: e3f3cc81fbcbb83c68396688f660b3a652176996c9ebeaf5463d2691a3163d6c
- evidence_id: access
  kind: search
  reference: 054-root-fetch1.json;054-root-fetch2.json;054-root-fetch3.json;535-local-hits.txt
  locator: Ignored/hidden-inclusive native capture and exact owner/key follow-up;
    current authority retrieval and attempted official supplementary/supplier routes.
  accessed_at: '2026-10-21T18:09:36Z'
  support: partial
  summary: The one adopted DOI resolves to the inspected original. The supplier page
    returned403; its exact lot and certificate were not independently verified beyond
    original Table4. The publisher supplement returned403 and the alternate PMC binary
    path404; an earlier instance-path download was only a redirect shell. Fig.S1c
    therefore remains uninspected. This is a bounded native-claim review, not an exhaustive
    hispidulin mechanism or natural-occurrence literature survey.
  search_scope: 2026-10-21; isolated054 native/source searches include ignored and
    hidden files. Exact PubChem CID, ChEBI name and adopted DOI endpoints; ordinary
    publisher and PMC supplement URLs.
  snapshot_sha256: 876c4efbaa44611307ada145cf1cc89cc5a5e7e6767f7b004b5990fc28398b71
- evidence_id: snippet-placement
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md:14;
    curation/curator_antibiotics.tsv:17
  locator: Verbatim-snippet rule compared with the entire original scientific text
    and native source evidence.
  accessed_at: '2026-10-21T18:09:36Z'
  support: supports
  summary: The checklist reserves snippet for a short verbatim source passage and
    notes for curator interpretation. The native phrase beginning Zai et al. reported
    hispidulin summarizes the paper; it is not a quoted passage. Its biological content
    remains supported by the exact hispidulin table row. The maintained curator evidence_snippet
    is projected unchanged by the seeder.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact chemical identity and external equivalence
  outcome: supported
  summary: Neutral hispidulin, its formula/masses and the sole native PubChem xref
    agree across six encodings. Original reagent naming/formula/purity identifies
    the same aglycone; no glycoside, acetate, salt or plant extract is substituted.
  target_ids:
  - antibioticmech:curator-b453af7884
  evidence_ids:
  - native
  - chemistry
  - primary
- assessment_id: activity
  area: evidence
  topic: Resistant-pathogen antibacterial claim
  outcome: supported
  summary: The adopted original includes explicit hispidulin inhibition of MRSA and
    ESBL bacterial strains, independently of the other five active flavonoids. The
    source-concept summary is faithful at its broad qualitative scope.
  target_ids:
  - antibioticmech:curator-b453af7884
  evidence_ids:
  - primary
  - assay
  - native
- assessment_id: mechanism
  area: evidence
  topic: Efflux, synergy and safety boundaries
  outcome: supported
  summary: No hispidulin molecular target or efflux claim appears in the native. Orientin/isoorientin
    experiments and Artemia toxicity are kept within their exact compounds, assays
    and organisms. Optional unpopulated objects are not defects.
  target_ids:
  - antibioticmech:curator-b453af7884
  evidence_ids:
  - scope
  - native
- assessment_id: provenance
  area: provenance
  topic: Curator ownership, source citation and history
  outcome: supported
  summary: The exact curator row, stable mint, explicit class, attached source evidence
    and one chronological proposal event reproduce through the inspected seeder. All
    thirteen initial hashes are retained and native status remains PROPOSED.
  target_ids:
  - antibioticmech:curator-b453af7884
  evidence_ids:
  - owner
  - native
- assessment_id: completeness
  area: completeness
  topic: Optional enrichment and actual access limits
  outcome: unknown
  summary: The main original supports the current record, but final microdilution
    timing/readout, replicate reporting, supplier certificate and Fig.S1c remain incompletely
    resolved. They would need attention before adding quantitative assay rows or stronger
    identity/clinical claims.
  target_ids:
  - antibioticmech:curator-b453af7884
  evidence_ids:
  - primary
  - assay
  - access
- assessment_id: snippet-format
  area: provenance
  topic: Paraphrase stored as source quotation
  outcome: concern
  summary: The attached citation and scientific summary are valid, but the paraphrase
    is in the verbatim-only snippet slot. Move the summary to notes or use an inspected
    short exact quotation.
  target_ids:
  - antibioticmech:curator-b453af7884
  evidence_ids:
  - native
  - owner
  - primary
  - snippet-placement
findings:
- finding_id: F1
  issue_key: hispidulin-source-evidence-paraphrase-in-snippet
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: A curator paraphrase occupies the verbatim snippet field
  description: The source-concept evidence snippet beginning Zai et al. reported hispidulin
    is a faithful curator summary, not a verbatim passage from the cited original.
    The explicit checklist requires verbatim snippets and places interpretation in
    notes. This is an evidence-format defect; the antibacterial and identity claims
    remain supported.
  target_ids:
  - antibioticmech:curator-b453af7884
  field_paths:
  - source_concepts[0].evidence[0].snippet
  evidence_ids:
  - native
  - owner
  - primary
  - snippet-placement
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Publication-backed exact compound, definition and evidence owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator concept loading, identity mint and native emission
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Class and identifier normalization context
  rule_id: 'review-checklist: Evidence standard: verbatim snippet versus notes'
  normalization_reason: Minor quotation/annotation placement error without changing
    the supported scientific conclusion.
actions:
- action_id: A0
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:curator-b453af7884
  description: Move the faithful paper summary from evidence_snippet to evidence_notes
    in the maintained curator row, preserving the existing chemistry provenance note
    and citation, or replace it with a short verified verbatim passage.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Publication-backed exact compound, definition and evidence owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator concept loading, identity mint and native emission
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Class and identifier normalization context
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - The emitted source evidence has only an actual inspected verbatim quotation in
    snippet, or no snippet; the faithful summary is retained in notes.
  - Preserve the DOI, exact chemical graph, antibacterial scope and PROPOSED status,
    then regenerate through maintained owners and run focused and corpus checks.
- action_id: A1
  description: If later adding quantitative activity, preserve exact-compound and
    assay boundaries.
  finding_ids: []
  target_ids:
  - antibioticmech:curator-b453af7884
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Publication-backed exact compound, definition and evidence owner
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/hispidulin.yaml
    role: Optional evidence-backed native annotation through the validated writer
  acceptance_checks:
  - Retain the exact Table1 hispidulin row, named strains and unnamed clinical isolate;
    inspect cited microdilution methods and reconcile replicate descriptions before
    constructing full assay observations.
  - Do not transfer orientin/isoorientin efflux or combination findings to hispidulin.
    Artemia LC50 and derived ratios do not establish human safety or clinical use.
  - Inspect actual Fig.S1c and a relevant reagent certificate if a future identity
    decision requires that depth; preserve all already corroborated molecular fields.
limitations:
- The complete main scientific text, four HTML tables and all captions were read.
  Main raw figure panels concern other compounds and were not independently reprocessed;
  the linked supplement including Fig.S1c could not be obtained through the attempted
  free routes.
- The exact commercial reagent is identified by original Table4, but its batch-specific
  certificate and supplier page were not inspected because the page returned403.
- The original main defers final microdilution details to earlier methods and has
  differing replicate descriptions. No complete assay observation is newly asserted
  by this review.
- The review follows the one adopted primary citation and exact authorities. It does
  not claim exhaustive hispidulin literature, biosynthetic origin, resistance or mechanistic
  coverage.
- No populated native protein/pathway or expression-dataset assertion requires a structured
  target-dataset query. The paper efflux experiments are explicitly for other flavonoids.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- The original paper XML/HTML was already retrieved during this review campaign for
  another compound; it was reread independently for exact hispidulin claims. The current
  DOI metadata and chemical authorities were fetched again.
- All native and maintained source files are unchanged. This draft does not promote
  PROPOSED to REVIEWED or add quantitative activity.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
