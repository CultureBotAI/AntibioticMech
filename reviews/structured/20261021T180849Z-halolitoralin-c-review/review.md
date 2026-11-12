# Review of halolitoralin C

- Review: 20261021T180849Z-halolitoralin-c-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:48:32Z
- Finished UTC: 2026-10-21T18:08:49Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Halolitoralin C has a supported cyclic tetrapeptide graph, but its definition incorrectly calls it an alanine-rich hexapeptide and copies A-specific activity wording. Correct the inherited ARO definition and citation using exact C evidence. The public C synthesis paper confirms the target composition but reports failed cyclization; it is not evidence for tested completed C material.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 524; original 13 hashes preserved and three actual ARO/PubChem owners appended before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-e690d68430 | data/antibiotics/antibacterial/halolitoralin-c.yaml | generated | halolitoralin C |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-e690d68430 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-e690d68430 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-e690d68430 | Actual focused execution exited 0. |
| Exact chemical authority comparison | passed | False | antibioticmech:aro-e690d68430 | Eight encodings agree at full key, formula and stereo-preserving normalized graph; four residue alpha atoms and six S centres verified. |
| Input, adopted-source and history audit | passed | False | antibioticmech:aro-e690d68430 | All 16 input hashes unchanged, original 13 preserved; one adopted review scoped and three chronological history events verified. |
| Authoritative full QC | failed | True | antibioticmech:aro-e690d68430 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-e690d68430 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-e690d68430 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-e690d68430 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-e690d68430 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-e690d68430 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-e690d68430 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-e690d68430 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-e690d68430 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact cyclic tetrapeptide

identity: supported. Targets: antibioticmech:aro-e690d68430.

Current exact authorities support the configured native graph. The inspected original synthesis target independently corroborates four-residue constitution, while its unsuccessful ring closure and unwedged side chains limit experimental natural-product confirmation.

### Copied A composition and activity paragraph

consistency: concern. Targets: antibioticmech:aro-e690d68430.

A four-residue Ile-Leu-Ile-Val peptide without Ala is materially misdescribed as an alanine-rich hexapeptide. The copied activity paragraph also lacks exact C support in the adopted review and needs the same source repair.

### Exact C antibacterial, fungal and earthworm evidence

scope: unknown. Targets: antibioticmech:aro-e690d68430.

The accessed discovery evidence supports only a family-level antifungal summary. The completed C assays needed for the detailed native potency sentence were not verified. Neither a failed synthesis nor unavailable primary data proves inactivity or requires removal of the antibacterial category.

### Minted xrefs and NRPS class

grounding: unknown. Targets: antibioticmech:aro-e690d68430.

Exact chemical xrefs and source mint are supported. The NRPS class remains a qualified database inference with unknown BGC; no exact biosynthetic route was established.

### Optional exact C target

completeness: supported. Targets: antibioticmech:aro-e690d68430.

No target is natively asserted and no inspected exact C target experiment was identified. A-only ClpC1 findings are not transferred; lack of optional enrichment is not itself a defect.

## Findings

### F1: Halolitoralin C incorrectly inherits halolitoralin A residue composition

major / open / confirmed; issue key: halolitoralin-c-copied-a-hexapeptide-definition.

The native/current ARO definition calls C an alanine-rich cyclic hexapeptide. Its supported graph and the original C synthesis target instead have four residues, Ile-Leu-Ile-Val, and no alanine. The remaining activity wording is copied from A and is not established for C by the cited review. Repair the composition and exact source scope together. No wrong-graph replacement or conclusion that C lacks activity follows.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained ARO C definition through a reproducible source-specific input or transform correction to describe the cyclic tetrapeptide. Replace copied potency and earthworm statements with an exact C original-supported summary, or qualify/remove those specific statements until the 2002/2006 C data are inspected. Cite the 2007 report only for its proposed target and failed synthetic sequence, not completed C assays. Reseed while retaining the supported graph.

- The C definition describes a tetrapeptide with no Ala and does not inherit A-specific composition or potency.
- Each retained C activity claim maps to exact C material and experiment; the failed 2007 synthesis is not treated as a C bioassay.
- Preserve ACTUUECIBHHYLY-DYKIIFRCSA-N and C23H42N4O4 unless separate primary natural-product evidence proves a change.
- Re-run focused schema/strict, reference/history/corpus and full QC gates for eventual native edits.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/halolitoralin-c.yaml; Entire native record, including definition, chemical structure, three xrefs, source concept and three history events | supports | The SEEDED/MINTED ARO record describes an alanine-rich hexapeptide, although its graph has four residues and no alanine. No native MIC, target, resistance, structured producer, drug-product or causal-graph assertion is present. |
| chemistry | CHEBI:221356;pubchem.compound:11812205;NPA011838; 524-authority-chemistry.json; current 524-chebi.json/.mol,524-pubchem.json,524-npatlas.json; retrieval hashes524-fetch.json | supports | Eight native and authority encodings agree at ACTUUECIBHHYLY-DYKIIFRCSA-N, C23H42N4O4 and zero charge. Four alpha centres and two Ile side-chain centres are S. The native ring contains Ile-Leu-Ile-Val, allowing cyclic rotation, with no Ala. Chirality-aware atom mapping follows stereo-preserving tautomer normalization for InChI reconstruction. |
| current-aro | ARO:3007782;ARO:3007779;ARO:3009657; 524-aro-blocks.json; reused official426-current-aro.obo SHA d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4 | supports | Current ARO repeats the native C definition and exact xrefs. Its family parent correctly calls B/C tetrapeptides and A a hexapeptide, and qualifies NRPS origin as likely with unknown biosynthetic cluster. The error lies in the C definition, not in the supported chemical graph. |
| synthesis | https://nopr.niscpr.res.in/bitstream/123456789/656/1/IJCB%2046B%287%29%20%282007%29%201137-1142.pdf; Reddy et al., Indian Journal of Chemistry46B:1137–1142 (2007);524-synthesis2007.pdf; entire six pages read, actual Chart I/II p1138 and Scheme III/IV p1140 viewed | supports | The proposed target1 is the cyclic Ile-Leu-Ile-Val tetrapeptide; the synthesis uses L-amino acids. The authors obtained linear intermediates but explicitly failed to close the ring, as shown by crossed arrows in Scheme IV and Results p1139. This is independent structural-target corroboration, not successful C synthesis or a new C bioassay. Chart I leaves Ile side-chain stereochemistry unwedged. |
| adopted-review | PMID:34677431;DOI:10.3390/md19100530; Reused522-adopted-core.json and522-PMC8539464.xml; complete abstract, exact halolitoralin paragraph and reference142 inspected;524-source-audit.json | refutes | The adopted review mentions A/B/C isolation but gives quantified fungal activity for A, not C. It supplies neither the C bacterial/earthworm claims nor the copied hexapeptide composition. Reference142 leads to an unrelated 2001 marine-sponge peptide review. Exact C activity is unresolved at this citation; inactivity is not inferred. |
| discovery | DOI:10.1016/S0040-4039(02)01458-2; Original 2002 publisher abstract/graphical-abstract prose; shared522-fetch.json and522-2002-openalex.json access record | supports | The discovery abstract calls A a hexapeptide and B/C tetrapeptides from Halobacillus litoralis YS3106, composed of hydrophobic L-amino-acid residues. It reports family-level antifungal and weak antitumor activity. The full original structure workup and congener assay table were unavailable; no exact C quantitative bacterial or worm endpoint is adopted. |
| other-original | https://uwischolar.sta.uwi.edu/activity/view/b55f5bbc-19ea-31db-848d-bdcbb17ff388; Official UWI author publication metadata; Dahiya and Pathak, J.Pharm.Res.5(3):69–73 (2006) | unknown | This separate C synthesis publication was identified through official author metadata and later references, but its original text was not obtained. Its title does not establish a completed synthesis, exact assay panel or result; these remain unverified. |
| owners | data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv;scripts/extract_source_inventory.py;scripts/enrich_pubchem_structures.py;scripts/seed_from_sources.py; 524-raw-rows.json;524-source-audit.json;524-owners-search.json | supports | The ARO row owns the erroneous definition and citation, while PubChem enrichment supplies the supported graph. Sixteen inputs retain their captured hashes, including the original 13. The ignored-inclusive exact label/ARO/ChEBI/key search and deterministic mint inspection support this source path; no native correction was applied. |
| search | Exact halolitoralin C literature and source discovery; 524-fetch.json/524-fetch2.json;524-owners-search.json; reused522-discovery.json | supports | The public six-page C synthesis original was fully inspected. The 2006 C source remains metadata-only and the 2002 discovery remains abstract-level. No exact C molecular-target experiment was established in this bounded search. The A-specific ClpC1 report is not transferred, and no native protein/pathway claim triggers the adapter. |

## Limits And Additional Notes

- The 2002 discovery full text was unavailable; only publisher abstract/graphical-abstract prose was inspected. The original natural C stereochemical workup and individual assay table remain unverified.
- The separate Dahiya/Pathak2006 C publication was located through official author metadata and later references but not read as a full original. No result is inferred from its title.
- The complete 2007 C synthesis report was read, including actual schemes. It failed cyclization and has no new completed C bioassay. Its side-chain centres are not explicitly wedged in the target drawing; current exact authority consensus is retained rather than independently reassigning natural stereo.
- The broad adopted 2021 review was inspected at its complete abstract and exact halolitoralin paragraph/reference; unrelated sections were not read in full. Its A-focused activity statements do not establish the C potency paragraph.
- NRPS origin and exact C antibacterial/earthworm scope remain unresolved at the inspected primary level. This is not proof of absence of activity, biosynthesis or molecular targets.
- The initial image-conversion attempt failed because system Python lacked fitz; pdftotext/pdftoppm successfully produced the text and images actually read. This auxiliary retrieval issue is separate from passed focused validation.
- Required shared corpus gates and the known platform SciPy failure are integrated by the coordinating finalizer; focused checks do not substitute for full QC.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record, maintained source or immutable bundle was changed. The scratch draft and evidence are handed off for independent final audit and saving.
- Original 13 hashes are preserved with three actual ARO/PubChem owner inputs. Standalone chemistry019 runs against053; native schema/strict and ledger use053.
- One linked major finding covers the copied definition and its citation scope, avoiding duplicate findings for the same inherited paragraph.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T180849Z-halolitoralin-c-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of halolitoralin C
started_at: '2026-10-21T17:48:32Z'
finished_at: '2026-10-21T18:08:49Z'
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
summary: Halolitoralin C has a supported cyclic tetrapeptide graph, but its definition
  incorrectly calls it an alanine-rich hexapeptide and copies A-specific activity
  wording. Correct the inherited ARO definition and citation using exact C evidence.
  The public C synthesis paper confirms the target composition but reports failed
  cyclization; it is not evidence for tested completed C material.
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
  - path: data/antibiotics/antibacterial/halolitoralin-c.yaml
    sha256: e2ffd11f5ac0db9c2f05ba76539ef262eefb0c7dd0eb9abc12380f51753fd65f
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
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: antibioticmech:aro-e690d68430
  path: data/antibiotics/antibacterial/halolitoralin-c.yaml
  label: halolitoralin C
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition, class and equivalence
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact chemical representation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Native generation and identity resolution
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Source and class policy
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion decisions
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 524; original 13 hashes preserved
    and three actual ARO/PubChem owners appended before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-e690d68430
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-e690d68430
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    524
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-e690d68430
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/halolitoralin-c.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-e690d68430
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/halolitoralin-c.yaml --out /private/tmp/am-review-session/524-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority
  name: Exact chemical authority comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/524-authority-check.py
    > /private/tmp/am-review-session/524-authority-check.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Eight encodings agree at full key, formula and stereo-preserving normalized
    graph; four residue alpha atoms and six S centres verified.
  target_ids:
  - antibioticmech:aro-e690d68430
- check_id: ledger
  name: Input, adopted-source and history audit
  command: .venv/bin/python /private/tmp/am-review-session/524-ledger.py > /private/tmp/am-review-session/524-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All 16 input hashes unchanged, original 13 preserved; one adopted review
    scoped and three chronological history events verified.
  target_ids:
  - antibioticmech:aro-e690d68430
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-e690d68430
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
  - antibioticmech:aro-e690d68430
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
  - antibioticmech:aro-e690d68430
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
  - antibioticmech:aro-e690d68430
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
  - antibioticmech:aro-e690d68430
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
  - antibioticmech:aro-e690d68430
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
  - antibioticmech:aro-e690d68430
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
  - antibioticmech:aro-e690d68430
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
  - antibioticmech:aro-e690d68430
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/halolitoralin-c.yaml
  locator: Entire native record, including definition, chemical structure, three xrefs,
    source concept and three history events
  accessed_at: '2026-10-21T18:08:30Z'
  support: supports
  summary: The SEEDED/MINTED ARO record describes an alanine-rich hexapeptide, although
    its graph has four residues and no alanine. No native MIC, target, resistance,
    structured producer, drug-product or causal-graph assertion is present.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:221356;pubchem.compound:11812205;NPA011838
  locator: 524-authority-chemistry.json; current 524-chebi.json/.mol,524-pubchem.json,524-npatlas.json;
    retrieval hashes524-fetch.json
  accessed_at: '2026-10-21T18:08:30Z'
  support: supports
  summary: Eight native and authority encodings agree at ACTUUECIBHHYLY-DYKIIFRCSA-N,
    C23H42N4O4 and zero charge. Four alpha centres and two Ile side-chain centres
    are S. The native ring contains Ile-Leu-Ile-Val, allowing cyclic rotation, with
    no Ala. Chirality-aware atom mapping follows stereo-preserving tautomer normalization
    for InChI reconstruction.
  snapshot_sha256: 80628b45e58da650a6d4db8b09fb07009905b476553c2ceab60a5d322c049c18
- evidence_id: current-aro
  kind: database
  reference: ARO:3007782;ARO:3007779;ARO:3009657
  locator: 524-aro-blocks.json; reused official426-current-aro.obo SHA d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
  accessed_at: '2026-10-21T18:08:30Z'
  support: supports
  summary: Current ARO repeats the native C definition and exact xrefs. Its family
    parent correctly calls B/C tetrapeptides and A a hexapeptide, and qualifies NRPS
    origin as likely with unknown biosynthetic cluster. The error lies in the C definition,
    not in the supported chemical graph.
  snapshot_sha256: b6d96aa3cc1d24dcda3866547edae85c7142124c694b546911867db06fe0309b
- evidence_id: synthesis
  kind: primary_source
  reference: https://nopr.niscpr.res.in/bitstream/123456789/656/1/IJCB%2046B%287%29%20%282007%29%201137-1142.pdf
  locator: Reddy et al., Indian Journal of Chemistry46B:1137–1142 (2007);524-synthesis2007.pdf;
    entire six pages read, actual Chart I/II p1138 and Scheme III/IV p1140 viewed
  accessed_at: '2026-10-21T18:08:30Z'
  support: supports
  summary: The proposed target1 is the cyclic Ile-Leu-Ile-Val tetrapeptide; the synthesis
    uses L-amino acids. The authors obtained linear intermediates but explicitly failed
    to close the ring, as shown by crossed arrows in Scheme IV and Results p1139.
    This is independent structural-target corroboration, not successful C synthesis
    or a new C bioassay. Chart I leaves Ile side-chain stereochemistry unwedged.
  snapshot_sha256: 962bc2dcda6ba87035186e79aa6f828d27a789f63b2e8bfb9f069b0e330e52bc
- evidence_id: adopted-review
  kind: authority
  reference: PMID:34677431;DOI:10.3390/md19100530
  locator: Reused522-adopted-core.json and522-PMC8539464.xml; complete abstract, exact
    halolitoralin paragraph and reference142 inspected;524-source-audit.json
  accessed_at: '2026-10-21T18:08:30Z'
  support: refutes
  summary: The adopted review mentions A/B/C isolation but gives quantified fungal
    activity for A, not C. It supplies neither the C bacterial/earthworm claims nor
    the copied hexapeptide composition. Reference142 leads to an unrelated 2001 marine-sponge
    peptide review. Exact C activity is unresolved at this citation; inactivity is
    not inferred.
  snapshot_sha256: 40280f418211135d9c16b44d8cd4d950e58167af65b8486917c8cce8d0143457
- evidence_id: discovery
  kind: primary_source
  reference: DOI:10.1016/S0040-4039(02)01458-2
  locator: Original 2002 publisher abstract/graphical-abstract prose; shared522-fetch.json
    and522-2002-openalex.json access record
  accessed_at: '2026-10-21T18:08:30Z'
  support: supports
  summary: The discovery abstract calls A a hexapeptide and B/C tetrapeptides from
    Halobacillus litoralis YS3106, composed of hydrophobic L-amino-acid residues.
    It reports family-level antifungal and weak antitumor activity. The full original
    structure workup and congener assay table were unavailable; no exact C quantitative
    bacterial or worm endpoint is adopted.
- evidence_id: other-original
  kind: authority
  reference: https://uwischolar.sta.uwi.edu/activity/view/b55f5bbc-19ea-31db-848d-bdcbb17ff388
  locator: Official UWI author publication metadata; Dahiya and Pathak, J.Pharm.Res.5(3):69–73
    (2006)
  accessed_at: '2026-10-21T18:08:30Z'
  support: unknown
  summary: This separate C synthesis publication was identified through official author
    metadata and later references, but its original text was not obtained. Its title
    does not establish a completed synthesis, exact assay panel or result; these remain
    unverified.
- evidence_id: owners
  kind: validation
  reference: data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv;scripts/extract_source_inventory.py;scripts/enrich_pubchem_structures.py;scripts/seed_from_sources.py
  locator: 524-raw-rows.json;524-source-audit.json;524-owners-search.json
  accessed_at: '2026-10-21T18:08:30Z'
  support: supports
  summary: The ARO row owns the erroneous definition and citation, while PubChem enrichment
    supplies the supported graph. Sixteen inputs retain their captured hashes, including
    the original 13. The ignored-inclusive exact label/ARO/ChEBI/key search and deterministic
    mint inspection support this source path; no native correction was applied.
  snapshot_sha256: 7bd73b61bf681d88caeaaa36f029c374141c7c4ed87c55e34d1270c65c05f30c
- evidence_id: search
  kind: search
  reference: Exact halolitoralin C literature and source discovery
  locator: 524-fetch.json/524-fetch2.json;524-owners-search.json; reused522-discovery.json
  accessed_at: '2026-10-21T18:08:30Z'
  support: supports
  summary: The public six-page C synthesis original was fully inspected. The 2006
    C source remains metadata-only and the 2002 discovery remains abstract-level.
    No exact C molecular-target experiment was established in this bounded search.
    The A-specific ClpC1 report is not transferred, and no native protein/pathway
    claim triggers the adapter.
  search_scope: Ignored-inclusive raw/curation/conf/scripts/src exact label, ARO3007782,
    CHEBI221356 and full key search; shared nine-hit EuropePMC discovery; exact C
    original-publication/author-metadata searches and current native chemical groundings.
  snapshot_sha256: 7bd73b61bf681d88caeaaa36f029c374141c7c4ed87c55e34d1270c65c05f30c
assessments:
- assessment_id: graph
  area: identity
  topic: Exact cyclic tetrapeptide
  outcome: supported
  summary: Current exact authorities support the configured native graph. The inspected
    original synthesis target independently corroborates four-residue constitution,
    while its unsuccessful ring closure and unwedged side chains limit experimental
    natural-product confirmation.
  target_ids:
  - antibioticmech:aro-e690d68430
  evidence_ids:
  - chemistry
  - synthesis
  - discovery
- assessment_id: definition
  area: consistency
  topic: Copied A composition and activity paragraph
  outcome: concern
  summary: A four-residue Ile-Leu-Ile-Val peptide without Ala is materially misdescribed
    as an alanine-rich hexapeptide. The copied activity paragraph also lacks exact
    C support in the adopted review and needs the same source repair.
  target_ids:
  - antibioticmech:aro-e690d68430
  evidence_ids:
  - record
  - chemistry
  - current-aro
  - synthesis
  - adopted-review
- assessment_id: activity
  area: scope
  topic: Exact C antibacterial, fungal and earthworm evidence
  outcome: unknown
  summary: The accessed discovery evidence supports only a family-level antifungal
    summary. The completed C assays needed for the detailed native potency sentence
    were not verified. Neither a failed synthesis nor unavailable primary data proves
    inactivity or requires removal of the antibacterial category.
  target_ids:
  - antibioticmech:aro-e690d68430
  evidence_ids:
  - adopted-review
  - discovery
  - synthesis
  - other-original
- assessment_id: classification
  area: grounding
  topic: Minted xrefs and NRPS class
  outcome: unknown
  summary: Exact chemical xrefs and source mint are supported. The NRPS class remains
    a qualified database inference with unknown BGC; no exact biosynthetic route was
    established.
  target_ids:
  - antibioticmech:aro-e690d68430
  evidence_ids:
  - chemistry
  - current-aro
  - owners
- assessment_id: mechanism
  area: completeness
  topic: Optional exact C target
  outcome: supported
  summary: No target is natively asserted and no inspected exact C target experiment
    was identified. A-only ClpC1 findings are not transferred; lack of optional enrichment
    is not itself a defect.
  target_ids:
  - antibioticmech:aro-e690d68430
  evidence_ids:
  - record
  - search
findings:
- finding_id: F1
  issue_key: halolitoralin-c-copied-a-hexapeptide-definition
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Halolitoralin C incorrectly inherits halolitoralin A residue composition
  description: The native/current ARO definition calls C an alanine-rich cyclic hexapeptide.
    Its supported graph and the original C synthesis target instead have four residues,
    Ile-Leu-Ile-Val, and no alanine. The remaining activity wording is copied from
    A and is not established for C by the cited review. Repair the composition and
    exact source scope together. No wrong-graph replacement or conclusion that C lacks
    activity follows.
  target_ids:
  - antibioticmech:aro-e690d68430
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - record
  - chemistry
  - current-aro
  - synthesis
  - adopted-review
  - owners
  rule_id: 'review-checklist: exact compound composition, definition consistency and
    claim-level source scope'
  normalization_reason: Major material misdescription of peptide composition and congener
    scope; the exact C graph remains supported, so this is not a wrong-molecule graph
    blocker.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Exact C definition and definition_refs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible source-specific definition correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition and reference projection
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-e690d68430
  description: Correct the maintained ARO C definition through a reproducible source-specific
    input or transform correction to describe the cyclic tetrapeptide. Replace copied
    potency and earthworm statements with an exact C original-supported summary, or
    qualify/remove those specific statements until the 2002/2006 C data are inspected.
    Cite the 2007 report only for its proposed target and failed synthetic sequence,
    not completed C assays. Reseed while retaining the supported graph.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Exact C definition and definition_refs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible source-specific definition correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition and reference projection
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py
  acceptance_checks:
  - The C definition describes a tetrapeptide with no Ala and does not inherit A-specific
    composition or potency.
  - Each retained C activity claim maps to exact C material and experiment; the failed
    2007 synthesis is not treated as a C bioassay.
  - Preserve ACTUUECIBHHYLY-DYKIIFRCSA-N and C23H42N4O4 unless separate primary natural-product
    evidence proves a change.
  - Re-run focused schema/strict, reference/history/corpus and full QC gates for eventual
    native edits.
limitations:
- The 2002 discovery full text was unavailable; only publisher abstract/graphical-abstract
  prose was inspected. The original natural C stereochemical workup and individual
  assay table remain unverified.
- The separate Dahiya/Pathak2006 C publication was located through official author
  metadata and later references but not read as a full original. No result is inferred
  from its title.
- The complete 2007 C synthesis report was read, including actual schemes. It failed
  cyclization and has no new completed C bioassay. Its side-chain centres are not
  explicitly wedged in the target drawing; current exact authority consensus is retained
  rather than independently reassigning natural stereo.
- The broad adopted 2021 review was inspected at its complete abstract and exact halolitoralin
  paragraph/reference; unrelated sections were not read in full. Its A-focused activity
  statements do not establish the C potency paragraph.
- NRPS origin and exact C antibacterial/earthworm scope remain unresolved at the inspected
  primary level. This is not proof of absence of activity, biosynthesis or molecular
  targets.
- The initial image-conversion attempt failed because system Python lacked fitz; pdftotext/pdftoppm
  successfully produced the text and images actually read. This auxiliary retrieval
  issue is separate from passed focused validation.
- Required shared corpus gates and the known platform SciPy failure are integrated
  by the coordinating finalizer; focused checks do not substitute for full QC.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record, maintained source or immutable bundle was changed. The scratch
  draft and evidence are handed off for independent final audit and saving.
- Original 13 hashes are preserved with three actual ARO/PubChem owner inputs. Standalone
  chemistry019 runs against053; native schema/strict and ledger use053.
- One linked major finding covers the copied definition and its citation scope, avoiding
  duplicate findings for the same inherited paragraph.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
