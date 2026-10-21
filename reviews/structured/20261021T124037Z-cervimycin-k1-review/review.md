# Cervimycin K1: exact congener identity and primary-source scope

- Review: 20261021T124037Z-cervimycin-k1-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:20:08Z
- Finished UTC: 2026-10-21T12:40:37Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native cervimycin K1 record and current complete chemical entries agree. The exact graph retains carbamoyl and an unacylated terminal sugar hydroxyl groups and is distinguished from the other congeners. The 2012 original identifies K1 and its production; the earlier cited patent provides scoped HKI10311129 antibacterial measurements. The sodium-containing mass-spectrometric ion is an analytical adduct, not a different isolated salt. No confirmed native correction is identified within these limits. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 278; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-eeb30db614 | data/antibiotics/antibacterial/cervimycin-k1.yaml | generated | cervimycin K1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-eeb30db614 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-eeb30db614 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-eeb30db614 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-eeb30db614 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-eeb30db614 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-eeb30db614 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-eeb30db614 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-eeb30db614 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-eeb30db614 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-eeb30db614 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-eeb30db614 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-eeb30db614 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact congener and chemical representations

identity: supported. Targets: antibioticmech:aro-eeb30db614.

All inspected exact chemical authorities and independent parses agree on K1, with carbamoyl and an unacylated terminal sugar hydroxyl. The source mint, formula, charge, masses and history are coherent. Preserve the stated stereochemical specification.

### Primary structural evidence and scope

identity: unknown. Targets: antibioticmech:aro-eeb30db614.

Original figures support the congener substituents, but every configured atom was not independently reassigned from original NMR/degradation data. Published figures also use a different A-ring keto/enol depiction; no exact-key normalization policy is silently changed.

### Adopted family description and source placement

evidence: supported. Targets: antibioticmech:aro-eeb30db614.

The cited article supports the broad polyketide description. The exact label and structure distinguish the congener; a broad definition alone does not merge it into a mixture or another family member.

### Exact-congener antibacterial evidence

grounding: supported. Targets: antibioticmech:aro-eeb30db614.

K1 antibacterial context has an original chemical-name bridge and patent assay table; quantitative adoption must retain the historical protocol and incomplete solid-form details.

### Direct target and resistance evidence

evidence: unknown. Targets: antibioticmech:aro-eeb30db614.

No native molecular target needs correction. CerJ is a biosynthetic enzyme, not an established antibacterial target. C-specific gyrase, Clp/WalK or stress-response results are not imported. No exact-congener direct target was established by the inspected source material.

### Producer and preparation provenance

completeness: unknown. Targets: antibioticmech:aro-eeb30db614.

The patent supports culture isolation from HKI0179/DSM13059, and the 2012 study distinguishes trace wild-type K1 from ΔcerJ production.

### Maintained owners and status

provenance: supported. Targets: antibioticmech:aro-eeb30db614.

Actual ARO/PubChem owners, all three history events and captured hashes are coherent. ChEBI intake context is distinguished from an actual seed owner. A saved review does not promote SEEDED/MINTED status.

### Sparse optional domains

completeness: not_applicable. Targets: antibioticmech:aro-eeb30db614.

No native clinical-product, causal graph or omics dataset claim is populated. Optional enrichment remains a separate evidence-backed curation task, not a mandatory schema defect.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally enrich cervimycin K1 using only exact-congener primary evidence at its verified depth.

- Preserve JHZMFWWPPNBNOE-BTYMIDDJSA-N, the native formula and stereochemical specification unless independently justified curation changes them.
- Retain organism/strain, engineered genotype, assay material, medium, inoculum, incubation, endpoint, units and censoring for any quantitative observation.
- Separate biosynthetic conversion, antibacterial phenotype, resistance association and direct molecular-target evidence. Do not transfer sibling-congener results.
- Resolve original structure/material and producer scope before adding exact identity or producer assertions. Keep numerical uncertainty and inaccessible original detail explicit.
- Run native evidence/history, focused validators and applicable corpus gates after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cervimycin-k1.yaml; Entire YAML, including all three history events | supports | Read the minted identifier, exact K1 label, antibacterial filing, SEEDED status, generic definition and its sole PMID, parent and structural class, every molecular descriptor, all xrefs, one ARO source concept and three history events. No synonym, molecular target, mode, resistance, producer, quantitative activity, clinical, causal graph or dataset assertion is populated. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/extract_source_inventory.py; scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py; 278-raw-rows.json; ARO row 491, PubChem row 201; exact source selection and enrichment | supports | ARO owns the label, general definition and PMID:36173303; PubChem enrichment supplies the exact structure. No matched ChEBI seed row supplies this record. The seeder emits the broader drug class as structural parent and retains the reproducible ARO mint. Initial hashes are preserved, with actual maintained owners appended. No matching target, resistance or FDA row was found in the inspected inventories. |
| chemistry | RDKit 2026.03.5 / InChI 1.07.3; 278-chemistry.json; focus021-root.py 278 | supports | Native SMILES and InChI independently produce JHZMFWWPPNBNOE-BTYMIDDJSA-N, C56H75NO22, net charge zero and one connected component. Masses agree at native precision and the ARO mint recomputes. There are 21 assigned tetrahedral centres; comparison does not independently reproduce every original stereochemical assignment. |
| official-chemistry | Current official PubChem structure comparison; batch028-root-xref-check.py/.json | supports | Independent parses of current complete PubChem SMILES and InChI all reproduce the native full key and C56H75NO22. This is structural cross-reference verification, not new activity evidence. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/54726226; 278-pc.json complete official PUG response | supports | The current CID names cervimycin K1 and matches the complete native molecular identity, including stereochemical specification. The carbamoyl and an unacylated terminal sugar hydroxyl substitution pattern is retained. |
| aro | https://card.mcmaster.ca/aro/3007605; Complete current entry; ARO:3005171 parent | supports | Current CARD resolves the exact K1 concept, its chemical xrefs, polyketide antibiotic class and sole adopted 2022 citation. Its family-level definition is not a congener-specific mechanistic experiment. |
| adopted2022 | PMID:36173303; DOI:10.1128/spectrum.02567-22; Primary XML: Introduction, Results/Table 1, Table 3, antimicrobial susceptibility and selection Methods | partial | The sole adopted citation supports the generic polyketide-family description. Its new activity and resistance experiments use C and D, with further tests using C unless explicitly stated. It supplies no exact K1 MIC, selected resistant strain or direct protein target. |
| 2012 | PMID:22179067; DOI:10.1038/nchembio.746; Author-posted full-text snapshots; pp154–155 and Figure 1, transacylase Methods p160 | partial | Figure 1 maps compound 5 to K1. HR-MS/NMR identify the major product of S. tendae HKI179 ΔcerJ; wild-type K1 is trace. It is described qualitatively as the most potent family member. The article supplies no antibacterial MIC table. |
| 2012-figures | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnchembio.746/MediaObjects/41589_2012_BFnchembio746_MOESM159_ESM.pdf; Supplementary Methods and Figures 2a–c; original main Figure 1 pixels | partial | The original main figure distinguishes the unacylated sugar terminus and carbamoyl K1 from acetyl K2. Supplemental crystallographic Methods explicitly decline to model a complete valid K ligand; that experiment cannot certify all ligand stereochemistry. |
| graph-relation | Scratch-only molecular graph comparison; batch028-root-xref-check.json graph_relations | supports | Removing the malonyl ester linkage from the D or N graph and retaining the largest sanitized fragment reproduces the exact native K1 key. This confirms computational congener consistency only; no biological conversion, activity or salt identity is inferred from the calculation. |
| K-patent | https://patents.google.com/patent/DE102004010219B4/en; Original PDF pp3,5–8; structure, Table 1 and Table 3; fermentation/isolation examples | partial | The patent identifies HKI10311129 as C56H75NO22 and isolates it from HKI0179/DSM13059 culture. Table 1 explicitly identifies 1136.4707 as [M+Na]+. Table 3 MICs are S. aureus SG511 and 134/93 0.8, E. faecalis1528 0.4 and B. subtilis ATCC6633 &lt;0.05 microgram/mL. It cites NCCLS M7-A1991 liquid testing but does not restate all assay conditions. Therapeutic patent claims are not clinical efficacy evidence. |
| K-name-link | https://patents.google.com/patent/US20090142809A1/en; Background and Example 2 | partial | The source equates cervimycin K with HKI10311129 and describes the unesterified carbamoyl structure. The earlier DE patent resolves the sodium-containing formula in this later prose as an analytical adduct. Its ester-cleavage examples measure product formation, not antibacterial potency; broad reaction language does not make K1 and K2 identical. |
| leads | PMID:15940739; PMID:15326518; PMID:21077936; PMID:38722162; PMID:33999625; Complete indexed abstracts in 028-cervimycin-core.json | context_only | The 2005 original abstract addresses A–D isolation/structure and antibacterial context but its original tables remain inaccessible. The 2004 biosynthesis, 2010 resistance and 2024 mechanism studies concern C. The 2021 synthesis concerns a K carbohydrate fragment. These leads do not provide interchangeable quantitative evidence for this exact congener. |
| search | Ignored-inclusive local search and bounded public primary-source retrieval; 278-local-hits.txt; 278-owner-hits.txt; batch028-cervimycin-owner-all.txt; retrieval manifests | context_only | Initial repository searches included hidden and ignored files outside .git/.venv. Exact owners, source concepts and available native assertions were checked. Primary source reading depth and failed routes are explicit; failure to retrieve an original is not evidence that its experiment never occurred. |

## Limits And Additional Notes

- The original 2005 full discovery paper and Herold thesis were not obtained; the indexed original abstract is not a replacement for all structural and assay tables.
- The author-posted 2012 main article was read through public web-text snapshots; direct PDF download failed. The actual publisher supplement and selected structure figures were retrieved and inspected. Snapshot hashes distinguish web text from PDF bytes.
- Original figures were used to verify congener substitutions and analytical-ion labels; every stereocentre was not independently derived from original NMR data. Different keto/enol depictions are not automatically wrong congeners.
- The 2024 C mechanism and other ancillary C/fragment papers were inspected at complete indexed-abstract depth for scope here; they are not exact-congener target evidence.
- No native gene, protein, pathway, regulator or dataset assertion triggers a structured adapter. Sibling mechanisms were considered only to prevent unsupported transfer.
- The K patent provides historical liquid-MIC results but does not restate complete medium, inoculum and incubation details. Its structural drawing lacks a complete atomwise absolute-configuration derivation. Patent treatment claims do not establish clinical success.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Original and expanded source hashes were checked before finalization; 16 captured inputs remain unchanged.
- No native record, source inventory, grounding decision or status was edited. Optional review metadata was selected for this exact congener.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T124037Z-cervimycin-k1-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cervimycin K1: exact congener identity and primary-source scope'
started_at: '2026-10-21T12:20:08Z'
finished_at: '2026-10-21T12:40:37Z'
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
summary: The native cervimycin K1 record and current complete chemical entries agree.
  The exact graph retains carbamoyl and an unacylated terminal sugar hydroxyl groups
  and is distinguished from the other congeners. The 2012 original identifies K1 and
  its production; the earlier cited patent provides scoped HKI10311129 antibacterial
  measurements. The sodium-containing mass-spectrometric ion is an analytical adduct,
  not a different isolated salt. No confirmed native correction is identified within
  these limits. Scientific assessment retains the stated evidence limits; full verification
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
  - path: data/antibiotics/antibacterial/cervimycin-k1.yaml
    sha256: c5c7fc30f48d335fcf16f0c1e8d1b046a0fe3e44694e5d5d15663a80be5510c6
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/chebi_antimicrobials.tsv
    sha256: 4c33e56c3c342be657309f720f5b5cb9cad1fae13bec202ef99e449503c32004
    role: context
  - path: data/raw/chebi_role_names.tsv
    sha256: 5c476c0aacd7c98d7241d2343a6fc41ee9eb9338077404c5b011a04bf40c6ac5
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
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
- target_id: antibioticmech:aro-eeb30db614
  path: data/antibiotics/antibacterial/cervimycin-k1.yaml
  label: cervimycin K1
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Standard intake context; no ChEBI inventory row supplies this ARO-only record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained CARD/ARO inventory extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual maintained source or transform for this record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual maintained source or transform for this record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Actual PubChem enrichment owner
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 278; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-eeb30db614
  exclusions:
  - target: Other cervimycin congeners, bulk antibiotic complexes and analytical ion
      adducts as exact identities
    reason: Their structures, material preparations and measured phenotypes retain
      their own scope.
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-eeb30db614
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    278
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-eeb30db614
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cervimycin-k1.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-eeb30db614
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cervimycin-k1.yaml --out /private/tmp/am-review-session/278-strict.tsv
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
  - antibioticmech:aro-eeb30db614
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
  - antibioticmech:aro-eeb30db614
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
  - antibioticmech:aro-eeb30db614
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
  - antibioticmech:aro-eeb30db614
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
  - antibioticmech:aro-eeb30db614
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
  - antibioticmech:aro-eeb30db614
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
  - antibioticmech:aro-eeb30db614
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
  - antibioticmech:aro-eeb30db614
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
  - antibioticmech:aro-eeb30db614
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cervimycin-k1.yaml
  locator: Entire YAML, including all three history events
  accessed_at: '2026-10-21T12:37:33Z'
  support: supports
  summary: Read the minted identifier, exact K1 label, antibacterial filing, SEEDED
    status, generic definition and its sole PMID, parent and structural class, every
    molecular descriptor, all xrefs, one ARO source concept and three history events.
    No synonym, molecular target, mode, resistance, producer, quantitative activity,
    clinical, causal graph or dataset assertion is populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/extract_source_inventory.py;
    scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py
  locator: 278-raw-rows.json; ARO row 491, PubChem row 201; exact source selection
    and enrichment
  accessed_at: '2026-10-21T12:37:33Z'
  support: supports
  summary: ARO owns the label, general definition and PMID:36173303; PubChem enrichment
    supplies the exact structure. No matched ChEBI seed row supplies this record.
    The seeder emits the broader drug class as structural parent and retains the reproducible
    ARO mint. Initial hashes are preserved, with actual maintained owners appended.
    No matching target, resistance or FDA row was found in the inspected inventories.
  snapshot_sha256: cf451cc799f73edf065102fbabef2d005d4cfbc6ad43e6407be1b97b5c4eb008
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5 / InChI 1.07.3
  locator: 278-chemistry.json; focus021-root.py 278
  accessed_at: '2026-10-21T12:37:33Z'
  support: supports
  summary: Native SMILES and InChI independently produce JHZMFWWPPNBNOE-BTYMIDDJSA-N,
    C56H75NO22, net charge zero and one connected component. Masses agree at native
    precision and the ARO mint recomputes. There are 21 assigned tetrahedral centres;
    comparison does not independently reproduce every original stereochemical assignment.
  snapshot_sha256: 36de9ef3a25eb517d1dd7c3190621662d55127b97a71ff3d9a969f498bea90ea
- evidence_id: official-chemistry
  kind: validation
  reference: Current official PubChem structure comparison
  locator: batch028-root-xref-check.py/.json
  accessed_at: '2026-10-21T12:37:33Z'
  support: supports
  summary: Independent parses of current complete PubChem SMILES and InChI all reproduce
    the native full key and C56H75NO22. This is structural cross-reference verification,
    not new activity evidence.
  snapshot_sha256: f5a6cfa15c1029ad4bd86eeae3357b294bce9566acccd4dfc347191a23e46da2
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/54726226
  locator: 278-pc.json complete official PUG response
  accessed_at: '2026-10-21T12:37:33Z'
  support: supports
  summary: The current CID names cervimycin K1 and matches the complete native molecular
    identity, including stereochemical specification. The carbamoyl and an unacylated
    terminal sugar hydroxyl substitution pattern is retained.
  snapshot_sha256: 94f2268a92599a9033fcec520783effefb284d61ae51954f70d1d67d668718eb
- evidence_id: aro
  kind: database
  reference: https://card.mcmaster.ca/aro/3007605
  locator: Complete current entry; ARO:3005171 parent
  accessed_at: '2026-10-21T12:37:33Z'
  support: supports
  summary: Current CARD resolves the exact K1 concept, its chemical xrefs, polyketide
    antibiotic class and sole adopted 2022 citation. Its family-level definition is
    not a congener-specific mechanistic experiment.
  snapshot_sha256: e29786e42bfb5ac09a94882fbc0de7fafd0456e2c9007edd36f419e30b40a69c
- evidence_id: adopted2022
  kind: primary_source
  reference: PMID:36173303; DOI:10.1128/spectrum.02567-22
  locator: 'Primary XML: Introduction, Results/Table 1, Table 3, antimicrobial susceptibility
    and selection Methods'
  accessed_at: '2026-10-21T12:37:33Z'
  support: partial
  summary: The sole adopted citation supports the generic polyketide-family description.
    Its new activity and resistance experiments use C and D, with further tests using
    C unless explicitly stated. It supplies no exact K1 MIC, selected resistant strain
    or direct protein target.
  snapshot_sha256: 571563deb53e4ecdf391db262053dd2c022534737f7d43a45cd131a90b397d35
- evidence_id: '2012'
  kind: primary_source
  reference: PMID:22179067; DOI:10.1038/nchembio.746
  locator: Author-posted full-text snapshots; pp154–155 and Figure 1, transacylase
    Methods p160
  accessed_at: '2026-10-21T12:37:33Z'
  support: partial
  summary: Figure 1 maps compound 5 to K1. HR-MS/NMR identify the major product of
    S. tendae HKI179 ΔcerJ; wild-type K1 is trace. It is described qualitatively as
    the most potent family member. The article supplies no antibacterial MIC table.
  snapshot_sha256: b883f6a322b2e345740285831f49e3c7258959b74b924795bb28465a3241a6d1
- evidence_id: 2012-figures
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnchembio.746/MediaObjects/41589_2012_BFnchembio746_MOESM159_ESM.pdf
  locator: Supplementary Methods and Figures 2a–c; original main Figure 1 pixels
  accessed_at: '2026-10-21T12:37:33Z'
  support: partial
  summary: The original main figure distinguishes the unacylated sugar terminus and
    carbamoyl K1 from acetyl K2. Supplemental crystallographic Methods explicitly
    decline to model a complete valid K ligand; that experiment cannot certify all
    ligand stereochemistry.
  snapshot_sha256: 3fb5d3af467a35ac45ef2914b9f67daae53489362c4f020788f108768fa62a30
- evidence_id: graph-relation
  kind: validation
  reference: Scratch-only molecular graph comparison
  locator: batch028-root-xref-check.json graph_relations
  accessed_at: '2026-10-21T12:37:33Z'
  support: supports
  summary: Removing the malonyl ester linkage from the D or N graph and retaining
    the largest sanitized fragment reproduces the exact native K1 key. This confirms
    computational congener consistency only; no biological conversion, activity or
    salt identity is inferred from the calculation.
  snapshot_sha256: f5a6cfa15c1029ad4bd86eeae3357b294bce9566acccd4dfc347191a23e46da2
- evidence_id: K-patent
  kind: primary_source
  reference: https://patents.google.com/patent/DE102004010219B4/en
  locator: Original PDF pp3,5–8; structure, Table 1 and Table 3; fermentation/isolation
    examples
  accessed_at: '2026-10-21T12:37:33Z'
  support: partial
  summary: The patent identifies HKI10311129 as C56H75NO22 and isolates it from HKI0179/DSM13059
    culture. Table 1 explicitly identifies 1136.4707 as [M+Na]+. Table 3 MICs are
    S. aureus SG511 and 134/93 0.8, E. faecalis1528 0.4 and B. subtilis ATCC6633 <0.05
    microgram/mL. It cites NCCLS M7-A1991 liquid testing but does not restate all
    assay conditions. Therapeutic patent claims are not clinical efficacy evidence.
  snapshot_sha256: 08243cc06856a1ce4c6adc96da85745b35980b1037553a5e7ee10926fd4d3ede
- evidence_id: K-name-link
  kind: primary_source
  reference: https://patents.google.com/patent/US20090142809A1/en
  locator: Background and Example 2
  accessed_at: '2026-10-21T12:37:33Z'
  support: partial
  summary: The source equates cervimycin K with HKI10311129 and describes the unesterified
    carbamoyl structure. The earlier DE patent resolves the sodium-containing formula
    in this later prose as an analytical adduct. Its ester-cleavage examples measure
    product formation, not antibacterial potency; broad reaction language does not
    make K1 and K2 identical.
  snapshot_sha256: 422fe9651eda616fbf9fd41ccf6b8e226f7097185fd36d1095237879f2d8270d
- evidence_id: leads
  kind: database
  reference: PMID:15940739; PMID:15326518; PMID:21077936; PMID:38722162; PMID:33999625
  locator: Complete indexed abstracts in 028-cervimycin-core.json
  accessed_at: '2026-10-21T12:37:33Z'
  support: context_only
  summary: The 2005 original abstract addresses A–D isolation/structure and antibacterial
    context but its original tables remain inaccessible. The 2004 biosynthesis, 2010
    resistance and 2024 mechanism studies concern C. The 2021 synthesis concerns a
    K carbohydrate fragment. These leads do not provide interchangeable quantitative
    evidence for this exact congener.
  snapshot_sha256: 9679f6e13b949f4c316df16943301a7aa6f9e148f41009391612043ce1b08893
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local search and bounded public primary-source retrieval
  locator: 278-local-hits.txt; 278-owner-hits.txt; batch028-cervimycin-owner-all.txt;
    retrieval manifests
  accessed_at: '2026-10-21T12:37:33Z'
  support: context_only
  summary: Initial repository searches included hidden and ignored files outside .git/.venv.
    Exact owners, source concepts and available native assertions were checked. Primary
    source reading depth and failed routes are explicit; failure to retrieve an original
    is not evidence that its experiment never occurred.
  search_scope: Exact label, identifier, slug and full key across the isolated repository;
    maintained inventories and curation; official chemical entries and the adopted
    PMID plus original-family follow-up.
  snapshot_sha256: 745dbb8d42efa4e0f612a9435db8cf6a4d50ac22a02d30dc970bfc6157163c08
assessments:
- assessment_id: identity
  area: identity
  topic: Exact congener and chemical representations
  outcome: supported
  summary: All inspected exact chemical authorities and independent parses agree on
    K1, with carbamoyl and an unacylated terminal sugar hydroxyl. The source mint,
    formula, charge, masses and history are coherent. Preserve the stated stereochemical
    specification.
  target_ids:
  - antibioticmech:aro-eeb30db614
  evidence_ids:
  - native
  - owners
  - chemistry
  - official-chemistry
  - pubchem
  - aro
- assessment_id: primary-structure
  area: identity
  topic: Primary structural evidence and scope
  outcome: unknown
  summary: Original figures support the congener substituents, but every configured
    atom was not independently reassigned from original NMR/degradation data. Published
    figures also use a different A-ring keto/enol depiction; no exact-key normalization
    policy is silently changed.
  target_ids:
  - antibioticmech:aro-eeb30db614
  evidence_ids:
  - '2012'
  - 2012-figures
  - official-chemistry
- assessment_id: definition
  area: evidence
  topic: Adopted family description and source placement
  outcome: supported
  summary: The cited article supports the broad polyketide description. The exact
    label and structure distinguish the congener; a broad definition alone does not
    merge it into a mixture or another family member.
  target_ids:
  - antibioticmech:aro-eeb30db614
  evidence_ids:
  - adopted2022
  - aro
  - native
- assessment_id: activity
  area: grounding
  topic: Exact-congener antibacterial evidence
  outcome: supported
  summary: K1 antibacterial context has an original chemical-name bridge and patent
    assay table; quantitative adoption must retain the historical protocol and incomplete
    solid-form details.
  target_ids:
  - antibioticmech:aro-eeb30db614
  evidence_ids:
  - '2012'
  - 2012-figures
  - adopted2022
  - K-patent
  - K-name-link
- assessment_id: mechanism
  area: evidence
  topic: Direct target and resistance evidence
  outcome: unknown
  summary: No native molecular target needs correction. CerJ is a biosynthetic enzyme,
    not an established antibacterial target. C-specific gyrase, Clp/WalK or stress-response
    results are not imported. No exact-congener direct target was established by the
    inspected source material.
  target_ids:
  - antibioticmech:aro-eeb30db614
  evidence_ids:
  - native
  - '2012'
  - leads
- assessment_id: producer
  area: completeness
  topic: Producer and preparation provenance
  outcome: unknown
  summary: The patent supports culture isolation from HKI0179/DSM13059, and the 2012
    study distinguishes trace wild-type K1 from ΔcerJ production.
  target_ids:
  - antibioticmech:aro-eeb30db614
  evidence_ids:
  - '2012'
  - K-patent
- assessment_id: provenance
  area: provenance
  topic: Maintained owners and status
  outcome: supported
  summary: Actual ARO/PubChem owners, all three history events and captured hashes
    are coherent. ChEBI intake context is distinguished from an actual seed owner.
    A saved review does not promote SEEDED/MINTED status.
  target_ids:
  - antibioticmech:aro-eeb30db614
  evidence_ids:
  - native
  - owners
  - search
- assessment_id: optional
  area: completeness
  topic: Sparse optional domains
  outcome: not_applicable
  summary: No native clinical-product, causal graph or omics dataset claim is populated.
    Optional enrichment remains a separate evidence-backed curation task, not a mandatory
    schema defect.
  target_ids:
  - antibioticmech:aro-eeb30db614
  evidence_ids:
  - native
  - leads
findings: []
actions:
- action_id: A1
  description: Optionally enrich cervimycin K1 using only exact-congener primary evidence
    at its verified depth.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-eeb30db614
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cervimycin-k1.yaml
    role: Curator-owned exact-congener evidence through the documented validated writer
  acceptance_checks:
  - Preserve JHZMFWWPPNBNOE-BTYMIDDJSA-N, the native formula and stereochemical specification
    unless independently justified curation changes them.
  - Retain organism/strain, engineered genotype, assay material, medium, inoculum,
    incubation, endpoint, units and censoring for any quantitative observation.
  - Separate biosynthetic conversion, antibacterial phenotype, resistance association
    and direct molecular-target evidence. Do not transfer sibling-congener results.
  - Resolve original structure/material and producer scope before adding exact identity
    or producer assertions. Keep numerical uncertainty and inaccessible original detail
    explicit.
  - Run native evidence/history, focused validators and applicable corpus gates after
    separately authorized curation.
limitations:
- The original 2005 full discovery paper and Herold thesis were not obtained; the
  indexed original abstract is not a replacement for all structural and assay tables.
- The author-posted 2012 main article was read through public web-text snapshots;
  direct PDF download failed. The actual publisher supplement and selected structure
  figures were retrieved and inspected. Snapshot hashes distinguish web text from
  PDF bytes.
- Original figures were used to verify congener substitutions and analytical-ion labels;
  every stereocentre was not independently derived from original NMR data. Different
  keto/enol depictions are not automatically wrong congeners.
- The 2024 C mechanism and other ancillary C/fragment papers were inspected at complete
  indexed-abstract depth for scope here; they are not exact-congener target evidence.
- No native gene, protein, pathway, regulator or dataset assertion triggers a structured
  adapter. Sibling mechanisms were considered only to prevent unsupported transfer.
- The K patent provides historical liquid-MIC results but does not restate complete
  medium, inoculum and incubation details. Its structural drawing lacks a complete
  atomwise absolute-configuration derivation. Patent treatment claims do not establish
  clinical success.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Original and expanded source hashes were checked before finalization; 16 captured
  inputs remain unchanged.
- No native record, source inventory, grounding decision or status was edited. Optional
  review metadata was selected for this exact congener.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://card.mcmaster.ca/aro/3007605
- https://doi.org/10.1038/nchembio.746
tags:
- cervimycin-k1
- exact-congener
- primary-source-scope
```
