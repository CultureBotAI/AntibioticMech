# Cervimycin D: exact congener identity and primary-source scope

- Review: 20261021T124029Z-cervimycin-d-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:20:07Z
- Finished UTC: 2026-10-21T12:40:29Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native cervimycin D record and current complete chemical entries agree. The exact graph retains carbamoyl and monomethylmalonyl groups and is distinguished from the other congeners. The adopted 2022 original directly reports D susceptibility and selected D-resistant strains; it does not establish a direct D protein target. An unassigned methylmalonyl centre and an unattached MIBiG candidate remain qualified. No confirmed native correction is identified within these limits. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 277; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-5c527c4696 | data/antibiotics/antibacterial/cervimycin-d.yaml | generated | cervimycin D |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-5c527c4696 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-5c527c4696 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-5c527c4696 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-5c527c4696 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-5c527c4696 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-5c527c4696 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-5c527c4696 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-5c527c4696 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-5c527c4696 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-5c527c4696 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-5c527c4696 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-5c527c4696 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact congener and chemical representations

identity: supported. Targets: antibioticmech:aro-5c527c4696.

All inspected exact chemical authorities and independent parses agree on D, with carbamoyl and monomethylmalonyl. The source mint, formula, charge, masses and history are coherent. Preserve the stated stereochemical specification.

### Primary structural evidence and scope

identity: unknown. Targets: antibioticmech:aro-5c527c4696.

Original figures support the congener substituents, but every configured atom was not independently reassigned from original NMR/degradation data. Published figures also use a different A-ring keto/enol depiction; no exact-key normalization policy is silently changed.

### Adopted family description and source placement

evidence: supported. Targets: antibioticmech:aro-5c527c4696.

The cited article supports the broad polyketide description. The exact label and structure distinguish the congener; a broad definition alone does not merge it into a mixture or another family member.

### Exact-congener antibacterial evidence

grounding: supported. Targets: antibioticmech:aro-5c527c4696.

The adopted original directly supports D antibacterial observations with strain, protocol and censoring preserved.

### Direct target and resistance evidence

evidence: unknown. Targets: antibioticmech:aro-5c527c4696.

No native molecular target needs correction. CerJ is a biosynthetic enzyme, not an established antibacterial target. C-specific gyrase, Clp/WalK or stress-response results are not imported. D-selected mutant genotypes support a scoped resistance association, not direct protein binding.

### Producer and preparation provenance

completeness: unknown. Targets: antibioticmech:aro-5c527c4696.

Original-family context names S. tendae HKI0179; the optional MIBiG candidate requires identity, incomplete-stereo and CS113 strain reconciliation.

### Maintained owners and status

provenance: supported. Targets: antibioticmech:aro-5c527c4696.

Actual ARO/PubChem owners, all three history events and captured hashes are coherent. ChEBI intake context is distinguished from an actual seed owner. A saved review does not promote SEEDED/MINTED status.

### Sparse optional domains

completeness: not_applicable. Targets: antibioticmech:aro-5c527c4696.

No native clinical-product, causal graph or omics dataset claim is populated. Optional enrichment remains a separate evidence-backed curation task, not a mandatory schema defect.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally enrich cervimycin D using only exact-congener primary evidence at its verified depth.

- Preserve YQSUNUWAYVGFKR-DIMVSIEISA-N, the native formula and stereochemical specification unless independently justified curation changes them.
- Retain organism/strain, engineered genotype, assay material, medium, inoculum, incubation, endpoint, units and censoring for any quantitative observation.
- Separate biosynthetic conversion, antibacterial phenotype, resistance association and direct molecular-target evidence. Do not transfer sibling-congener results.
- Resolve original structure/material and producer scope before adding exact identity or producer assertions. Keep numerical uncertainty and inaccessible original detail explicit.
- Run native evidence/history, focused validators and applicable corpus gates after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cervimycin-d.yaml; Entire YAML, including all three history events | supports | Read the minted identifier, exact D label, antibacterial filing, SEEDED status, generic definition and its sole PMID, parent and structural class, every molecular descriptor, all xrefs, one ARO source concept and three history events. No synonym, molecular target, mode, resistance, producer, quantitative activity, clinical, causal graph or dataset assertion is populated. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/extract_source_inventory.py; scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py; 277-raw-rows.json; ARO row 490, PubChem row 200; exact source selection and enrichment | supports | ARO owns the label, general definition and PMID:36173303; PubChem enrichment supplies the exact structure. No matched ChEBI seed row supplies this record. The seeder emits the broader drug class as structural parent and retains the reproducible ARO mint. Initial hashes are preserved, with actual maintained owners appended. No matching target, resistance or FDA row was found in the inspected inventories. |
| chemistry | RDKit 2026.03.5 / InChI 1.07.3; 277-chemistry.json; focus021-root.py 277 | supports | Native SMILES and InChI independently produce YQSUNUWAYVGFKR-DIMVSIEISA-N, C60H79NO25, net charge zero and one connected component. Masses agree at native precision and the ARO mint recomputes. There are 21 assigned tetrahedral centres and one unspecified methylmalonyl centre; unspecified does not mean racemic or mixed. |
| official-chemistry | Current official PubChem and ChEBI structure comparison; batch028-root-xref-check.py/.json | supports | Independent parses of current complete PubChem SMILES and InChI plus ChEBI SMILES and InChI all reproduce the native full key and C60H79NO25. This is structural cross-reference verification, not new activity evidence. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/54677926; 277-pc.json complete official PUG response | supports | The current CID names cervimycin D and matches the complete native molecular identity, including stereochemical specification. The carbamoyl and monomethylmalonyl substitution pattern is retained. |
| aro | https://card.mcmaster.ca/aro/3007604; Complete current entry; ARO:3005171 parent | supports | Current CARD resolves the exact D concept, its chemical xrefs, polyketide antibiotic class and sole adopted 2022 citation. Its family-level definition is not a congener-specific mechanistic experiment. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:198705; Complete OLS structure and current entry | supports | The current two-star ChEBI entry identifies D and agrees with the full native molecular key, formula, neutral charge and unspecified methylmalonyl stereocentre. An external exact xref does not itself require replacement of the native minted identity. |
| adopted2022 | PMID:36173303; DOI:10.1128/spectrum.02567-22; Primary XML: Introduction, Results/Table 1, Table 3, antimicrobial susceptibility and selection Methods | partial | The original reports D MICs in Mueller Hinton broth after 24 h; Methods give 5e5 CFU/mL and 37 C. D values include B. subtilis 168 0.5, S. aureus SG511 32, N315 64 and E. faecium BM4147 4 microgram/mL. E. coli MB5746 is &gt;64; the D+PMBN cell is ND. These are strain/protocol observations, not universal susceptibility or clinical breakpoints. |
| D-resistance | PMID:36173303; DOI:10.1128/spectrum.02567-22; Results/Table 3 and selected-mutant Methods | partial | CmR07–09 were D-selected from S. aureus SG511. Table 3 reports CmR09 D MIC 107.5 and revertant 16 microgram/mL, with ClpC P204H and WalK Y549D plus revertant R555H. Preserve 107.5 rather than rounding it into a twofold series. Association and mutant physiology do not prove direct D binding. The single-allele Table 5 and main omics comparison concern C-selected contexts. |
| 2012 | PMID:22179067; DOI:10.1038/nchembio.746; Author-posted full-text snapshots; pp154–155 and Figure 1, transacylase Methods p160 | partial | Figure 1 identifies D as carbamoyl/monomethylmalonyl. CerJ with K1 and methylmalonyl-CoA produces D. This is biosynthetic evidence, not a bacterial target assay. |
| 2012-figures | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnchembio.746/MediaObjects/41589_2012_BFnchembio746_MOESM159_ESM.pdf; Supplementary Methods and Figures 2a–c; original main Figure 1 pixels | partial | Supplementary Figure 2b displays D formula C60H79NO25 and exact mass 1213.4941 with the monomethylmalonyl group. N and C have different acyl substitutions. The sodium-containing spectral peak is labelled [M+Na]+. |
| graph-relation | Scratch-only molecular graph comparison; batch028-root-xref-check.json graph_relations | supports | Removing the malonyl ester linkage from the D or N graph and retaining the largest sanitized fragment reproduces the exact native K1 key. This confirms computational congener consistency only; no biological conversion, activity or salt identity is inferred from the calculation. |
| mibig | MIBiG:BGC0001439; data/raw/mibig_producers.tsv; Adopted row 684; scripts/seed_from_sources.py attach_mibig_producers | unknown | The unattached D candidate is questionable, not expert reviewed, stereo_complete=false and names Streptomyces sp. CS113. Its MJANQOPHKCQYSL-DIMVSIEISA-N key differs in keto/enol encoding, and its legacy reference PMID15326518 concerns C biosynthesis. The seeder skips incomplete stereochemistry before requiring an exact unique full key. Neither these data nor family labels establish the CS113/HKI0179 relationship; no missing-producer defect is inferred. |
| leads | PMID:15940739; PMID:15326518; PMID:21077936; PMID:38722162; PMID:33999625; Complete indexed abstracts in 028-cervimycin-core.json | context_only | The 2005 original abstract addresses A–D isolation/structure and antibacterial context but its original tables remain inaccessible. The 2004 biosynthesis, 2010 resistance and 2024 mechanism studies concern C. The 2021 synthesis concerns a K carbohydrate fragment. These leads do not provide interchangeable quantitative evidence for this exact congener. |
| search | Ignored-inclusive local search and bounded public primary-source retrieval; 277-local-hits.txt; 277-owner-hits.txt; batch028-cervimycin-owner-all.txt; retrieval manifests | context_only | Initial repository searches included hidden and ignored files outside .git/.venv. Exact owners, source concepts and available native assertions were checked. Primary source reading depth and failed routes are explicit; failure to retrieve an original is not evidence that its experiment never occurred. |

## Limits And Additional Notes

- The original 2005 full discovery paper and Herold thesis were not obtained; the indexed original abstract is not a replacement for all structural and assay tables.
- The author-posted 2012 main article was read through public web-text snapshots; direct PDF download failed. The actual publisher supplement and selected structure figures were retrieved and inspected. Snapshot hashes distinguish web text from PDF bytes.
- Original figures were used to verify congener substitutions and analytical-ion labels; every stereocentre was not independently derived from original NMR data. Different keto/enol depictions are not automatically wrong congeners.
- The 2024 C mechanism and other ancillary C/fragment papers were inspected at complete indexed-abstract depth for scope here; they are not exact-congener target evidence.
- No native gene, protein, pathway, regulator or dataset assertion triggers a structured adapter. Sibling mechanisms were considered only to prevent unsupported transfer.
- The 2022 D activity/selected-mutant sections and main tables were inspected; C-focused protein and omics experiments cannot be generalized to D. The 2022 supplemental MBC table was not independently inspected for D.
- The adopted MIBiG candidate uses an incomplete-stereo flag, a different tautomer key and unresolved CS113 taxon attribution. No producer join is recommended without resolving those independent constraints.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Original and expanded source hashes were checked before finalization; 18 captured inputs remain unchanged.
- No native record, source inventory, grounding decision or status was edited. Optional review metadata was selected for this exact congener.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T124029Z-cervimycin-d-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cervimycin D: exact congener identity and primary-source scope'
started_at: '2026-10-21T12:20:07Z'
finished_at: '2026-10-21T12:40:29Z'
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
summary: The native cervimycin D record and current complete chemical entries agree.
  The exact graph retains carbamoyl and monomethylmalonyl groups and is distinguished
  from the other congeners. The adopted 2022 original directly reports D susceptibility
  and selected D-resistant strains; it does not establish a direct D protein target.
  An unassigned methylmalonyl centre and an unattached MIBiG candidate remain qualified.
  No confirmed native correction is identified within these limits. Scientific assessment
  retains the stated evidence limits; full verification is blocked by the shared native-library
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
  - path: data/antibiotics/antibacterial/cervimycin-d.yaml
    sha256: 88ea51f4f11e8b2343d2e3f841d4503c4f5591f16b4b02db44a71dbc74dc8b79
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
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
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
  - path: scripts/extract_mibig_producers.py
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
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
- target_id: antibioticmech:aro-5c527c4696
  path: data/antibiotics/antibacterial/cervimycin-d.yaml
  label: cervimycin D
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
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/mibig_producers.tsv
    role: Optional candidate producer context; not an attached native assertion
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_mibig_producers.py
    role: Optional candidate producer context; not an attached native assertion
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 277; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-5c527c4696
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
  - antibioticmech:aro-5c527c4696
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    277
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-5c527c4696
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cervimycin-d.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-5c527c4696
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cervimycin-d.yaml --out /private/tmp/am-review-session/277-strict.tsv
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
  - antibioticmech:aro-5c527c4696
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
  - antibioticmech:aro-5c527c4696
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
  - antibioticmech:aro-5c527c4696
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
  - antibioticmech:aro-5c527c4696
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
  - antibioticmech:aro-5c527c4696
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
  - antibioticmech:aro-5c527c4696
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
  - antibioticmech:aro-5c527c4696
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
  - antibioticmech:aro-5c527c4696
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
  - antibioticmech:aro-5c527c4696
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cervimycin-d.yaml
  locator: Entire YAML, including all three history events
  accessed_at: '2026-10-21T12:37:33Z'
  support: supports
  summary: Read the minted identifier, exact D label, antibacterial filing, SEEDED
    status, generic definition and its sole PMID, parent and structural class, every
    molecular descriptor, all xrefs, one ARO source concept and three history events.
    No synonym, molecular target, mode, resistance, producer, quantitative activity,
    clinical, causal graph or dataset assertion is populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/extract_source_inventory.py;
    scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py
  locator: 277-raw-rows.json; ARO row 490, PubChem row 200; exact source selection
    and enrichment
  accessed_at: '2026-10-21T12:37:33Z'
  support: supports
  summary: ARO owns the label, general definition and PMID:36173303; PubChem enrichment
    supplies the exact structure. No matched ChEBI seed row supplies this record.
    The seeder emits the broader drug class as structural parent and retains the reproducible
    ARO mint. Initial hashes are preserved, with actual maintained owners appended.
    No matching target, resistance or FDA row was found in the inspected inventories.
  snapshot_sha256: a26bea5189dcda40648bf77ea86da5cbe16ec34bf6f9f4a85dec7a05b4e93587
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5 / InChI 1.07.3
  locator: 277-chemistry.json; focus021-root.py 277
  accessed_at: '2026-10-21T12:37:33Z'
  support: supports
  summary: Native SMILES and InChI independently produce YQSUNUWAYVGFKR-DIMVSIEISA-N,
    C60H79NO25, net charge zero and one connected component. Masses agree at native
    precision and the ARO mint recomputes. There are 21 assigned tetrahedral centres
    and one unspecified methylmalonyl centre; unspecified does not mean racemic or
    mixed.
  snapshot_sha256: f4edf4c7b0a7ee94bb0e6143dbf25fc5d1ec5c05a499498152d4007faffcce46
- evidence_id: official-chemistry
  kind: validation
  reference: Current official PubChem and ChEBI structure comparison
  locator: batch028-root-xref-check.py/.json
  accessed_at: '2026-10-21T12:37:33Z'
  support: supports
  summary: Independent parses of current complete PubChem SMILES and InChI plus ChEBI
    SMILES and InChI all reproduce the native full key and C60H79NO25. This is structural
    cross-reference verification, not new activity evidence.
  snapshot_sha256: f5a6cfa15c1029ad4bd86eeae3357b294bce9566acccd4dfc347191a23e46da2
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/54677926
  locator: 277-pc.json complete official PUG response
  accessed_at: '2026-10-21T12:37:33Z'
  support: supports
  summary: The current CID names cervimycin D and matches the complete native molecular
    identity, including stereochemical specification. The carbamoyl and monomethylmalonyl
    substitution pattern is retained.
  snapshot_sha256: 4306c5f92195bfe998d44a08b2edce8f964fd8eac17b40717d447ba908897ea6
- evidence_id: aro
  kind: database
  reference: https://card.mcmaster.ca/aro/3007604
  locator: Complete current entry; ARO:3005171 parent
  accessed_at: '2026-10-21T12:37:33Z'
  support: supports
  summary: Current CARD resolves the exact D concept, its chemical xrefs, polyketide
    antibiotic class and sole adopted 2022 citation. Its family-level definition is
    not a congener-specific mechanistic experiment.
  snapshot_sha256: 9a509291f3702f155c4dff5b5d9ff280a4455c46cfa97c5f321dcd44853691ad
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:198705
  locator: Complete OLS structure and current entry
  accessed_at: '2026-10-21T12:37:33Z'
  support: supports
  summary: The current two-star ChEBI entry identifies D and agrees with the full
    native molecular key, formula, neutral charge and unspecified methylmalonyl stereocentre.
    An external exact xref does not itself require replacement of the native minted
    identity.
  snapshot_sha256: bc700c92c51e895f0953b93a4b33741796a2aba68de172517530f0ebc1302d8a
- evidence_id: adopted2022
  kind: primary_source
  reference: PMID:36173303; DOI:10.1128/spectrum.02567-22
  locator: 'Primary XML: Introduction, Results/Table 1, Table 3, antimicrobial susceptibility
    and selection Methods'
  accessed_at: '2026-10-21T12:37:33Z'
  support: partial
  summary: The original reports D MICs in Mueller Hinton broth after 24 h; Methods
    give 5e5 CFU/mL and 37 C. D values include B. subtilis 168 0.5, S. aureus SG511
    32, N315 64 and E. faecium BM4147 4 microgram/mL. E. coli MB5746 is >64; the D+PMBN
    cell is ND. These are strain/protocol observations, not universal susceptibility
    or clinical breakpoints.
  snapshot_sha256: 571563deb53e4ecdf391db262053dd2c022534737f7d43a45cd131a90b397d35
- evidence_id: D-resistance
  kind: primary_source
  reference: PMID:36173303; DOI:10.1128/spectrum.02567-22
  locator: Results/Table 3 and selected-mutant Methods
  accessed_at: '2026-10-21T12:37:33Z'
  support: partial
  summary: CmR07–09 were D-selected from S. aureus SG511. Table 3 reports CmR09 D
    MIC 107.5 and revertant 16 microgram/mL, with ClpC P204H and WalK Y549D plus revertant
    R555H. Preserve 107.5 rather than rounding it into a twofold series. Association
    and mutant physiology do not prove direct D binding. The single-allele Table 5
    and main omics comparison concern C-selected contexts.
  snapshot_sha256: 571563deb53e4ecdf391db262053dd2c022534737f7d43a45cd131a90b397d35
- evidence_id: '2012'
  kind: primary_source
  reference: PMID:22179067; DOI:10.1038/nchembio.746
  locator: Author-posted full-text snapshots; pp154–155 and Figure 1, transacylase
    Methods p160
  accessed_at: '2026-10-21T12:37:33Z'
  support: partial
  summary: Figure 1 identifies D as carbamoyl/monomethylmalonyl. CerJ with K1 and
    methylmalonyl-CoA produces D. This is biosynthetic evidence, not a bacterial target
    assay.
  snapshot_sha256: b883f6a322b2e345740285831f49e3c7258959b74b924795bb28465a3241a6d1
- evidence_id: 2012-figures
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnchembio.746/MediaObjects/41589_2012_BFnchembio746_MOESM159_ESM.pdf
  locator: Supplementary Methods and Figures 2a–c; original main Figure 1 pixels
  accessed_at: '2026-10-21T12:37:33Z'
  support: partial
  summary: Supplementary Figure 2b displays D formula C60H79NO25 and exact mass 1213.4941
    with the monomethylmalonyl group. N and C have different acyl substitutions. The
    sodium-containing spectral peak is labelled [M+Na]+.
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
- evidence_id: mibig
  kind: database
  reference: MIBiG:BGC0001439; data/raw/mibig_producers.tsv
  locator: Adopted row 684; scripts/seed_from_sources.py attach_mibig_producers
  accessed_at: '2026-10-21T12:37:33Z'
  support: unknown
  summary: The unattached D candidate is questionable, not expert reviewed, stereo_complete=false
    and names Streptomyces sp. CS113. Its MJANQOPHKCQYSL-DIMVSIEISA-N key differs
    in keto/enol encoding, and its legacy reference PMID15326518 concerns C biosynthesis.
    The seeder skips incomplete stereochemistry before requiring an exact unique full
    key. Neither these data nor family labels establish the CS113/HKI0179 relationship;
    no missing-producer defect is inferred.
  snapshot_sha256: 4d9267bf7aed30504892c39daccc39a4f52ead4730d7b0056f392695e160bdda
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
  locator: 277-local-hits.txt; 277-owner-hits.txt; batch028-cervimycin-owner-all.txt;
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
  snapshot_sha256: 9a55e7bfb9c9045a0ce98eb2ab21556221399f1c6303694e57d83e13d61b73e9
assessments:
- assessment_id: identity
  area: identity
  topic: Exact congener and chemical representations
  outcome: supported
  summary: All inspected exact chemical authorities and independent parses agree on
    D, with carbamoyl and monomethylmalonyl. The source mint, formula, charge, masses
    and history are coherent. Preserve the stated stereochemical specification.
  target_ids:
  - antibioticmech:aro-5c527c4696
  evidence_ids:
  - native
  - owners
  - chemistry
  - official-chemistry
  - pubchem
  - aro
  - chebi
- assessment_id: primary-structure
  area: identity
  topic: Primary structural evidence and scope
  outcome: unknown
  summary: Original figures support the congener substituents, but every configured
    atom was not independently reassigned from original NMR/degradation data. Published
    figures also use a different A-ring keto/enol depiction; no exact-key normalization
    policy is silently changed.
  target_ids:
  - antibioticmech:aro-5c527c4696
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
  - antibioticmech:aro-5c527c4696
  evidence_ids:
  - adopted2022
  - aro
  - native
- assessment_id: activity
  area: grounding
  topic: Exact-congener antibacterial evidence
  outcome: supported
  summary: The adopted original directly supports D antibacterial observations with
    strain, protocol and censoring preserved.
  target_ids:
  - antibioticmech:aro-5c527c4696
  evidence_ids:
  - '2012'
  - 2012-figures
  - adopted2022
- assessment_id: mechanism
  area: evidence
  topic: Direct target and resistance evidence
  outcome: unknown
  summary: No native molecular target needs correction. CerJ is a biosynthetic enzyme,
    not an established antibacterial target. C-specific gyrase, Clp/WalK or stress-response
    results are not imported. D-selected mutant genotypes support a scoped resistance
    association, not direct protein binding.
  target_ids:
  - antibioticmech:aro-5c527c4696
  evidence_ids:
  - native
  - '2012'
  - leads
  - D-resistance
- assessment_id: producer
  area: completeness
  topic: Producer and preparation provenance
  outcome: unknown
  summary: Original-family context names S. tendae HKI0179; the optional MIBiG candidate
    requires identity, incomplete-stereo and CS113 strain reconciliation.
  target_ids:
  - antibioticmech:aro-5c527c4696
  evidence_ids:
  - '2012'
  - mibig
- assessment_id: provenance
  area: provenance
  topic: Maintained owners and status
  outcome: supported
  summary: Actual ARO/PubChem owners, all three history events and captured hashes
    are coherent. ChEBI intake context is distinguished from an actual seed owner.
    A saved review does not promote SEEDED/MINTED status.
  target_ids:
  - antibioticmech:aro-5c527c4696
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
  - antibioticmech:aro-5c527c4696
  evidence_ids:
  - native
  - leads
findings: []
actions:
- action_id: A1
  description: Optionally enrich cervimycin D using only exact-congener primary evidence
    at its verified depth.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-5c527c4696
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cervimycin-d.yaml
    role: Curator-owned exact-congener evidence through the documented validated writer
  acceptance_checks:
  - Preserve YQSUNUWAYVGFKR-DIMVSIEISA-N, the native formula and stereochemical specification
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
- The 2022 D activity/selected-mutant sections and main tables were inspected; C-focused
  protein and omics experiments cannot be generalized to D. The 2022 supplemental
  MBC table was not independently inspected for D.
- The adopted MIBiG candidate uses an incomplete-stereo flag, a different tautomer
  key and unresolved CS113 taxon attribution. No producer join is recommended without
  resolving those independent constraints.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Original and expanded source hashes were checked before finalization; 18 captured
  inputs remain unchanged.
- No native record, source inventory, grounding decision or status was edited. Optional
  review metadata was selected for this exact congener.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://card.mcmaster.ca/aro/3007604
- https://doi.org/10.1038/nchembio.746
tags:
- cervimycin-d
- exact-congener
- primary-source-scope
```
