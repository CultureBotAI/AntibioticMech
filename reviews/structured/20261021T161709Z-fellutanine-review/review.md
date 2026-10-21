# Review of fellutanine

- Review: 20261021T161709Z-fellutanine-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:56:40Z
- Finished UTC: 2026-10-21T16:17:09Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native and current ChEBI SMILES omit both indole pyrrolic hydrogens and fail kekulization. A scratch repair using two [nH] atoms agrees with the valid ChEBI molfile, PubChem and stored meso InChI identity. The adopted antibacterial source attributes activity to fellutanine rather than eutypoids, but its main paper was not retrieved. Later S/S and prenylated biosynthetic materials are kept separate from this R/S record. One major maintained-source correction is required.

## Scope And Provenance

Whole SEEDED, EXACT fellutanine record: definition, all four aliases, two structural parents, antibacterial role, every structure field, Reaxys mapping, source concept and three histories; all three adopted primary leads and later stereochemical/material boundaries.

Selection: Queue 436 in isolated batch 044. Root captured the original 13 inputs before assessment and appended the actual source-lead queue as input 14; all 14 remain unchanged. A second agent independently checked chemistry and completed the source audit.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:70168 | data/antibiotics/antibacterial/fellutanine.yaml | generated | fellutanine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native schema | passed | True | CHEBI:70168 | Root actual exit 0. |
| Native strict terms | passed | True | CHEBI:70168 | Root actual exit 0; no ERROR rows. |
| Native molecular consistency | failed | False | CHEBI:70168 | Root actual native chemistry failed at sanitized SMILES parsing with indole kekulization errors. Schema/strict were then executed separately and passed. |
| Initial raw graph comparison | failed | False | CHEBI:70168 | First independent raw graph comparison additionally failed because Standard InChI reconstructs a lactim tautomer while molfile/SMILES encode the diketopiperazine lactam. This representational difference was diagnosed and resolved in a separate stereochemistry-preserving tautomer check. |
| Independent defect and repaired-identity verification | passed | False | CHEBI:70168 | Reproduces invalid native/current ChEBI SMILES; six valid or repaired encodings agree after controlled tautomer normalization preserving sp3 and bond stereochemistry. Mirror identity confirms the meso graph. This passes a candidate check, not the unchanged native SMILES. |
| Whole source and reference ledger | passed | False | CHEBI:70168 | All 14 hashes unchanged and original 13 preserved; all four source aliases, three adopted PMIDs, ontology terms and three chronological histories reconciled. |
| Authoritative full QC | failed | True | CHEBI:70168 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:70168 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:70168 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:70168 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:70168 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:70168 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:70168 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:70168 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:70168 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### SMILES validity

consistency: concern. Targets: CHEBI:70168.

Both indole aromatic nitrogens lack explicit pyrrolic hydrogens and prevent parsing. The validated two-[nH] repair preserves the intended identity.

### Stored intended meso identity

identity: supported. Targets: CHEBI:70168.

The valid InChI/key, named L/D and R/S aliases, official molfile and PubChem agree on the meso compound. Controlled tautomer normalization preserves the two configured centers.

### Exact natural-product stereochemical assignment

scope: unknown. Targets: CHEBI:70168.

Later literature uses the fellutanine A name for a presumed S/S material. Complete original stereochemical evidence is needed before transferring those assays or changing this explicitly meso record. Generic cyclo(Trp-Trp) naming is insufficient.

### Structural parents and antibacterial role

grounding: supported. Targets: CHEBI:70168.

Parents match the valid graph; current ChEBI and the adopted KF620 abstract support the named-compound antibacterial attribution. Exact-meso potency remains bounded.

### Penicillium occurrence

evidence: supported. Targets: CHEBI:70168.

All three adopted abstracts provide relevant Penicillium occurrence context. This supports the unquantified definition; no unverified strain-specific biosynthesis object is asserted.

### Quantitative exact-meso activity

quantity: unknown. Targets: CHEBI:70168.

Original fellutanine assay details were not accessible; no numerical native MIC or transfer from the later S/S panel is justified.

### Antibacterial molecular target

evidence: unknown. Targets: CHEBI:70168.

Native has no molecular-target edge. Eutypoid GSK-3β activity and FelB biosynthesis do not identify a fellutanine antibacterial target.

### Reaxys mapping

grounding: unknown. Targets: CHEBI:70168.

Current ChEBI supports the registry attribution; direct registry access failed, leaving independent form/stereo scope unverified.

### Maintained repair and provenance

ownership: supported. Targets: CHEBI:70168.

Invalid text is traceable to the adopted ChEBI row and unchanged current upstream JSON. A maintained correction is needed; refreshing unchanged upstream input or editing only generated YAML would not resolve recurrence.

## Findings

### F1: Both indole nitrogens omit [nH], making the SMILES invalid

major / open / confirmed; issue key: chebi-70168-invalid-smiles-two-missing-indole-hydrogens.

The source-derived SMILES contains two bare aromatic indole n atoms and fails kekulization. Valid native InChI, current ChEBI molfile and PubChem agree on the neutral meso structure. A scratch-only two-[nH] repair reproduces the same key, formula and configured centers. Current ChEBI JSON still contains the defect, so unchanged source refresh is insufficient.

## Recommended Actions And Acceptance Checks

### A1

Implement a documented maintained ChEBI structure correction and regenerate the affected record. Verified candidate SMILES: O=C1N[C@H](Cc2c[nH]c3ccccc23)C(=O)N[C@H]1Cc1c[nH]c2ccccc12. Preserve the already supported meso identity; do not patch only the generated YAML.

- Require a sanitized parse with two indole [nH] atoms, C22H20N4O2, charge 0 and DNHODRZUCGXYKU-BGYRXZFFSA-N. Preserve the configured R/S meso pair.
- Require reciprocal chiral graph agreement with the official molfile and PubChem; compare Standard InChI after explicit tautomer handling that preserves sp3/bond stereo. Do not change valid InChI/key merely to match an invalid input.
- Make the repair reproducible through the maintained extraction/input policy and reseeding, with provenance and meaningful regression coverage for this two-indole case.
- After authorized curation, rerun native chemistry, just validate, just validate-strict, just verify-corpus --summary and just qc. Preserve history and leave REVIEWED unset until all required native gates pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/fellutanine.yaml; Entire native YAML | supports | The explicit systematic and L/D aliases, stored InChI/key and neutral formula identify the meso diketopiperazine. The generic cyclo(Trp-Trp) alias is less specific and cannot identify stereochemistry in external papers by itself. No dedicated protein target, MIC, clinical status or producer object is present. |
| chemistry | CHEBI:70168; PubChem CID6571639; 436-chebi.json/.mol;436-pubchem.json/.sdf;436-authority-chemistry.json;436-tautomer-check.json | refutes | Native and current ChEBI SMILES use two bare aromatic n atoms in indole rings and fail sanitization. Native InChI, ChEBI molfile and PubChem preserve C22H20N4O2, neutral charge and DNHODRZUCGXYKU-BGYRXZFFSA-N. Adding [nH] at both indoles in scratch yields that same meso identity. Molfile, PubChem and corrected SMILES agree by reciprocal chiral graph mapping; native InChI agrees after tautomer normalization. |
| tautomer | Independent raw and tautomer-aware chemical comparisons; 436-chemistry-independent-attempt1.log;436-chemistry-probe.log;436-chemistry-tautomer-check.py;436-tautomer-check.json | supports | The first raw graph assertion failed because RDKit reconstructs the Standard InChI as the di-lactim. The repair and official molfile are the di-lactam. Canonical tautomer comparison with removal of sp3 and bond stereo disabled gives identical graphs and keys. This is distinct from the actual missing-[nH] defect and does not justify changing the valid InChI or configured centers. |
| authority | CHEBI:70168; CHEBI:38958; CHEBI:65061; CHEBI:33282; 436-chebi.json;436-chebi-38958/65061/33282.json | supports | Current ChEBI retains the meso aliases, definition, indole-alkaloid/diketopiperazine parents, antibacterial role and Reaxys 8651145 mapping. Its own molfile is valid although its JSON SMILES repeats the defect. Source consistency therefore does not establish usable SMILES. |
| adopted | PMID:10867952; PMID:14520967; PMID:21126094; 436-adopted-core.json, all three source:MED complete abstracts | supports | PMID 10867952 reports named fellutanine A production by P. piscarium. PMID 14520967 reports P. fellutanum F-3020 production in growth-medium context. PMID 21126094 assigns the KF620 extract antibacterial activity to fellutanine; it assigns GSK-3β inhibition to eutypoids instead. These abstracts support occurrence and the named-compound activity report, but do not independently distinguish the antibacterial material as meso R/S or supply its quantitative assay. |
| supplement | DOI:10.1021/np100633k.s001; 436-np100633k_si_001.pdf title/contents and full text extraction | context_only | The official supplement contains spectra and spectral tables for eutypoids B–E, compounds 1–4. It does not supply the missing fellutanine stereochemical assignment or antimicrobial assay details; eutypoid kinase findings are not substituted for a fellutanine mechanism. |
| discovery | PMID:10843594; DOI:10.1021/np9903853; 436-discovery2000-core.json complete discovery abstract;436-discovery2000-figshare.json | context_only | The original discovery abstract reports four diketopiperazines from P. fellutanum and MS/NMR structure determination. It does not spell out the exact stereochemical assignment. The official supplementary query returned an empty list, so no uninspected original stereochemical argument is claimed. |
| later-stereo | PMID:27447650; DOI:10.3390/md14070136; 436-PMC4962026.xml selected Results, isolation, assay and stereochemical methods | context_only | The 2016 original calls compound 7 fellutanine A, but presumes S/S stereochemistry from L-Trp biosynthetic reasoning; its chiral-hydrolysate experiments concern compounds 5/6, not 7. Its bacterial MICs &gt;256 µg/mL concern that material and E. coli ATCC 25922/S. aureus ATCC 25923; the paper reverses their Gram labels. These bounded negatives do not refute meso-native activity or establish a native identity correction. |
| biosynthesis | PMID:40289498; DOI:10.1021/acs.jnatprod.4c01116; 436-later2025-core.json complete original abstract | context_only | The 2025 study describes a Nannizzia fulva cluster expressed in Aspergillus nidulans and FelB dual prenylation of cyclo(L-Trp-L-Trp). The substrate stereochemistry and prenylated/oxidized pathway products differ from the unprenylated meso target. A biosynthetic enzyme is not an antibacterial target; no native mechanism or producer object is added from this abstract. |
| owners | Maintained ChEBI input and extraction; 436-source-rows.json;436-source-audit.json;scripts/extract_source_inventory.py lines318–325;scripts/seed_from_sources.py | supports | The frozen CHEBI:70168 row carries the same invalid SMILES. The extractor copies the source string, and the seeder propagates it into the generated record. All 14 input hashes remain unchanged, including original 13; every adopted lead, all aliases and histories are accounted for. Future repair must be reproducible in the maintained ChEBI extraction/input lane. |
| validation | Actual native gate results; 436-focused-results.json;436-chemistry.log;436-schema.log;436-strict.log;436-ledger.log | refutes | Actual native chemistry exit 1 is preserved; schema and strict terms exit 0. The repaired scratch and source-ledger checks pass, but neither changes native bytes nor clears the native REVIEWED structure-consistency gate. |
| access | Bounded public fellutanine research; 436-local-hits.txt includes ignored files;044-root-fetch1/2.json;436-fetch3/4/5.json;436-openalex.json | context_only | Official ACS main retrieval failed; two public author-repository URLs returned HTTP 200 HTML bot challenges despite PDF filenames, not readable PDFs. The official supplement was retrieved. The 2000 Springer page also returned challenge content. Direct Reaxys returned 403. A 2009 review paragraph was read as speculative biosynthesis context only; no primary mechanism was adopted from it. |

## Limits And Additional Notes

- All three adopted complete abstracts were read. The 2011 main paper was not obtained: the author-repository PDF paths served HTML bot challenges. The official supplement covers eutypoids rather than fellutanine.
- The meso graph is internally supported by valid native and authority structures. Exact stereochemical mapping of the antibacterial 2011 material remains unverified; later presumed S/S materials and prenylated derivatives cannot be silently equated.
- The first raw InChI-versus-molfile comparison failed due to lactim/lactam representation. A separate controlled tautomer check passed while preserving configured centers; this does not excuse the independently invalid native SMILES.
- Reaxys 8651145 is repeated by current ChEBI but could not be independently inspected.
- The 2016 source swaps Gram labels for its stated E. coli/S. aureus panel and infers fellutanine A stereochemistry from biosynthesis. Its negative measurements remain restricted to that reported material and panel.
- No primary molecular-target mechanism or clinical efficacy was established for the exact native compound.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Root native schema/strict results and initial captures were reused at the unchanged base; validation_plan independently completed chemical comparison and primary-source scope review.
- Standalone chemistry used the batch 019 interpreter against batch 044; the source ledger and contract use batch 044.
- No native gene/protein/pathway is asserted. Adjacent biosynthetic enzymes and eutypoid kinase assays were excluded before any mechanism adoption, so a bacterial structured adapter was not applicable.
- The review preserves native bytes and scientific status; the suggested SMILES exists only in scratch evidence and this proposed action.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T161709Z-fellutanine-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of fellutanine
started_at: '2026-10-21T15:56:40Z'
finished_at: '2026-10-21T16:17:09Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Root performed the initial native/source capture and focused
    validators; validation_plan read the entire native and actual source row, verified
    original hashes, independently reproduced the two-indole defect with parity-aware
    comparisons, and completed adopted-lead and exact-material research. Shared preliminary
    conclusions were tested against source artifacts.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Major invalid SMILES; exact meso identity retained, native REVIEWED
  structure gate blocked
scientific_review: true
summary: The native and current ChEBI SMILES omit both indole pyrrolic hydrogens and
  fail kekulization. A scratch repair using two [nH] atoms agrees with the valid ChEBI
  molfile, PubChem and stored meso InChI identity. The adopted antibacterial source
  attributes activity to fellutanine rather than eutypoids, but its main paper was
  not retrieved. Later S/S and prenylated biosynthetic materials are kept separate
  from this R/S record. One major maintained-source correction is required.
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
  - path: data/antibiotics/antibacterial/fellutanine.yaml
    sha256: 8f8648c24a82d901dee27367f9086aa8e2a68466abaee278652536695387e2a9
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
scope:
  description: 'Whole SEEDED, EXACT fellutanine record: definition, all four aliases,
    two structural parents, antibacterial role, every structure field, Reaxys mapping,
    source concept and three histories; all three adopted primary leads and later
    stereochemical/material boundaries.'
  selection: Queue 436 in isolated batch 044. Root captured the original 13 inputs
    before assessment and appended the actual source-lead queue as input 14; all 14
    remain unchanged. A second agent independently checked chemistry and completed
    the source audit.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:70168
targets:
- target_id: CHEBI:70168
  path: data/antibiotics/antibacterial/fellutanine.yaml
  label: fellutanine
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
checks:
- check_id: schema
  name: Native schema
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/fellutanine.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root actual exit 0.
  target_ids:
  - CHEBI:70168
  evidence_ids:
  - validation
- check_id: strict
  name: Native strict terms
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/fellutanine.yaml --out /private/tmp/am-review-session/436-strict.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Root actual exit 0; no ERROR rows.
  target_ids:
  - CHEBI:70168
  evidence_ids:
  - validation
- check_id: native-chemistry
  name: Native molecular consistency
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    436
  status: failed
  required: false
  exit_code: 1
  expected_exit_code: 0
  summary: Root actual native chemistry failed at sanitized SMILES parsing with indole
    kekulization errors. Schema/strict were then executed separately and passed.
  target_ids:
  - CHEBI:70168
  evidence_ids:
  - chemistry
  - validation
- check_id: raw-comparison
  name: Initial raw graph comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/436-chemistry-verify.py
    > /private/tmp/am-review-session/436-chemistry-independent.log 2>&1
  status: failed
  required: false
  exit_code: 1
  expected_exit_code: 0
  summary: First independent raw graph comparison additionally failed because Standard
    InChI reconstructs a lactim tautomer while molfile/SMILES encode the diketopiperazine
    lactam. This representational difference was diagnosed and resolved in a separate
    stereochemistry-preserving tautomer check.
  target_ids:
  - CHEBI:70168
  evidence_ids:
  - chemistry
  - tautomer
- check_id: candidate-comparison
  name: Independent defect and repaired-identity verification
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/436-chemistry-tautomer-check.py
    > /private/tmp/am-review-session/436-tautomer-check.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Reproduces invalid native/current ChEBI SMILES; six valid or repaired encodings
    agree after controlled tautomer normalization preserving sp3 and bond stereochemistry.
    Mirror identity confirms the meso graph. This passes a candidate check, not the
    unchanged native SMILES.
  target_ids:
  - CHEBI:70168
  evidence_ids:
  - chemistry
  - tautomer
- check_id: source-ledger
  name: Whole source and reference ledger
  command: .venv/bin/python /private/tmp/am-review-session/436-ledger.py > /private/tmp/am-review-session/436-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All 14 hashes unchanged and original 13 preserved; all four source aliases,
    three adopted PMIDs, ontology terms and three chronological histories reconciled.
  target_ids:
  - CHEBI:70168
  evidence_ids:
  - owners
  - adopted
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:70168
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
  - CHEBI:70168
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
  - CHEBI:70168
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
  - CHEBI:70168
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
  - CHEBI:70168
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
  - CHEBI:70168
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
  - CHEBI:70168
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
  - CHEBI:70168
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
  - CHEBI:70168
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/fellutanine.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T16:14:26Z'
  support: supports
  summary: The explicit systematic and L/D aliases, stored InChI/key and neutral formula
    identify the meso diketopiperazine. The generic cyclo(Trp-Trp) alias is less specific
    and cannot identify stereochemistry in external papers by itself. No dedicated
    protein target, MIC, clinical status or producer object is present.
- evidence_id: chemistry
  kind: authority
  reference: CHEBI:70168; PubChem CID6571639
  locator: 436-chebi.json/.mol;436-pubchem.json/.sdf;436-authority-chemistry.json;436-tautomer-check.json
  accessed_at: '2026-10-21T16:14:26Z'
  support: refutes
  summary: Native and current ChEBI SMILES use two bare aromatic n atoms in indole
    rings and fail sanitization. Native InChI, ChEBI molfile and PubChem preserve
    C22H20N4O2, neutral charge and DNHODRZUCGXYKU-BGYRXZFFSA-N. Adding [nH] at both
    indoles in scratch yields that same meso identity. Molfile, PubChem and corrected
    SMILES agree by reciprocal chiral graph mapping; native InChI agrees after tautomer
    normalization.
  snapshot_sha256: dd6503bde6c4b3f0ecbfaebcc7baa21edbe5e94744f07214bf34dd9f96bb4649
- evidence_id: tautomer
  kind: validation
  reference: Independent raw and tautomer-aware chemical comparisons
  locator: 436-chemistry-independent-attempt1.log;436-chemistry-probe.log;436-chemistry-tautomer-check.py;436-tautomer-check.json
  accessed_at: '2026-10-21T16:14:26Z'
  support: supports
  summary: The first raw graph assertion failed because RDKit reconstructs the Standard
    InChI as the di-lactim. The repair and official molfile are the di-lactam. Canonical
    tautomer comparison with removal of sp3 and bond stereo disabled gives identical
    graphs and keys. This is distinct from the actual missing-[nH] defect and does
    not justify changing the valid InChI or configured centers.
  snapshot_sha256: dd6503bde6c4b3f0ecbfaebcc7baa21edbe5e94744f07214bf34dd9f96bb4649
- evidence_id: authority
  kind: authority
  reference: CHEBI:70168; CHEBI:38958; CHEBI:65061; CHEBI:33282
  locator: 436-chebi.json;436-chebi-38958/65061/33282.json
  accessed_at: '2026-10-21T16:03:33Z'
  support: supports
  summary: Current ChEBI retains the meso aliases, definition, indole-alkaloid/diketopiperazine
    parents, antibacterial role and Reaxys 8651145 mapping. Its own molfile is valid
    although its JSON SMILES repeats the defect. Source consistency therefore does
    not establish usable SMILES.
  snapshot_sha256: 90e31fb25b746e8bc1657a29830b7cf561d3dcab5c7dfbc6ff73ba9c65592e2a
- evidence_id: adopted
  kind: primary_source
  reference: PMID:10867952; PMID:14520967; PMID:21126094
  locator: 436-adopted-core.json, all three source:MED complete abstracts
  accessed_at: '2026-10-21T16:03:34Z'
  support: supports
  summary: PMID 10867952 reports named fellutanine A production by P. piscarium. PMID
    14520967 reports P. fellutanum F-3020 production in growth-medium context. PMID
    21126094 assigns the KF620 extract antibacterial activity to fellutanine; it assigns
    GSK-3β inhibition to eutypoids instead. These abstracts support occurrence and
    the named-compound activity report, but do not independently distinguish the antibacterial
    material as meso R/S or supply its quantitative assay.
  snapshot_sha256: 643535374191e7f62af61b4868aebea6d3fc149db850409d8cf326ef7ce0621f
- evidence_id: supplement
  kind: primary_source
  reference: DOI:10.1021/np100633k.s001
  locator: 436-np100633k_si_001.pdf title/contents and full text extraction
  accessed_at: '2026-10-21T16:08:51.493721Z'
  support: context_only
  summary: The official supplement contains spectra and spectral tables for eutypoids
    B–E, compounds 1–4. It does not supply the missing fellutanine stereochemical
    assignment or antimicrobial assay details; eutypoid kinase findings are not substituted
    for a fellutanine mechanism.
  snapshot_sha256: 5c991035a5a5625578ad96530a1e81a8ce352343f1b078eb61d0ff7f1ab7fdc6
- evidence_id: discovery
  kind: primary_source
  reference: PMID:10843594; DOI:10.1021/np9903853
  locator: 436-discovery2000-core.json complete discovery abstract;436-discovery2000-figshare.json
  accessed_at: '2026-10-21T16:11:06.224662Z'
  support: context_only
  summary: The original discovery abstract reports four diketopiperazines from P.
    fellutanum and MS/NMR structure determination. It does not spell out the exact
    stereochemical assignment. The official supplementary query returned an empty
    list, so no uninspected original stereochemical argument is claimed.
  snapshot_sha256: 05c8f963fd2b57a5bc3feadd3f27b988ec2bc7381e991bd545a8d17dc0ec5638
- evidence_id: later-stereo
  kind: primary_source
  reference: PMID:27447650; DOI:10.3390/md14070136
  locator: 436-PMC4962026.xml selected Results, isolation, assay and stereochemical
    methods
  accessed_at: '2026-10-21T16:07:03Z'
  support: context_only
  summary: The 2016 original calls compound 7 fellutanine A, but presumes S/S stereochemistry
    from L-Trp biosynthetic reasoning; its chiral-hydrolysate experiments concern
    compounds 5/6, not 7. Its bacterial MICs >256 µg/mL concern that material and
    E. coli ATCC 25922/S. aureus ATCC 25923; the paper reverses their Gram labels.
    These bounded negatives do not refute meso-native activity or establish a native
    identity correction.
  snapshot_sha256: 71c7499197bfcdb6eaf214bd403ead989ef4a00f8d0f3478dea7a1bac5ea2035
- evidence_id: biosynthesis
  kind: primary_source
  reference: PMID:40289498; DOI:10.1021/acs.jnatprod.4c01116
  locator: 436-later2025-core.json complete original abstract
  accessed_at: '2026-10-21T16:07:03Z'
  support: context_only
  summary: The 2025 study describes a Nannizzia fulva cluster expressed in Aspergillus
    nidulans and FelB dual prenylation of cyclo(L-Trp-L-Trp). The substrate stereochemistry
    and prenylated/oxidized pathway products differ from the unprenylated meso target.
    A biosynthetic enzyme is not an antibacterial target; no native mechanism or producer
    object is added from this abstract.
  snapshot_sha256: 84a954b20fd08d184db8497312c3449c0ca1fdfff2d0eb7970b32027ed98ab70
- evidence_id: owners
  kind: database
  reference: Maintained ChEBI input and extraction
  locator: 436-source-rows.json;436-source-audit.json;scripts/extract_source_inventory.py
    lines318–325;scripts/seed_from_sources.py
  accessed_at: '2026-10-21T16:14:26Z'
  support: supports
  summary: The frozen CHEBI:70168 row carries the same invalid SMILES. The extractor
    copies the source string, and the seeder propagates it into the generated record.
    All 14 input hashes remain unchanged, including original 13; every adopted lead,
    all aliases and histories are accounted for. Future repair must be reproducible
    in the maintained ChEBI extraction/input lane.
  snapshot_sha256: 21e5c08501db77df2d2c8e3e15db79189672a6dd51fead0b7b583b5da685dad2
- evidence_id: validation
  kind: validation
  reference: Actual native gate results
  locator: 436-focused-results.json;436-chemistry.log;436-schema.log;436-strict.log;436-ledger.log
  accessed_at: '2026-10-21T16:14:26Z'
  support: refutes
  summary: Actual native chemistry exit 1 is preserved; schema and strict terms exit
    0. The repaired scratch and source-ledger checks pass, but neither changes native
    bytes nor clears the native REVIEWED structure-consistency gate.
  snapshot_sha256: 44209523ef77b283b595ba167126929b9abb4b754589c8869133c0c276897ff4
- evidence_id: access
  kind: search
  reference: Bounded public fellutanine research
  locator: 436-local-hits.txt includes ignored files;044-root-fetch1/2.json;436-fetch3/4/5.json;436-openalex.json
  accessed_at: '2026-10-21T16:14:26Z'
  support: context_only
  summary: Official ACS main retrieval failed; two public author-repository URLs returned
    HTTP 200 HTML bot challenges despite PDF filenames, not readable PDFs. The official
    supplement was retrieved. The 2000 Springer page also returned challenge content.
    Direct Reaxys returned 403. A 2009 review paragraph was read as speculative biosynthesis
    context only; no primary mechanism was adopted from it.
  snapshot_sha256: caa4d55e0e74ab5cfeee82f5f1238c3c47c624923e3d0a91ecb1ef7a98c72dd7
  search_scope: 436-local-hits.txt includes ignored files;044-root-fetch1/2.json;436-fetch3/4/5.json;436-openalex.json
assessments:
- assessment_id: structure
  area: consistency
  topic: SMILES validity
  outcome: concern
  summary: Both indole aromatic nitrogens lack explicit pyrrolic hydrogens and prevent
    parsing. The validated two-[nH] repair preserves the intended identity.
  target_ids:
  - CHEBI:70168
  evidence_ids:
  - chemistry
  - validation
  - owners
- assessment_id: identity
  area: identity
  topic: Stored intended meso identity
  outcome: supported
  summary: The valid InChI/key, named L/D and R/S aliases, official molfile and PubChem
    agree on the meso compound. Controlled tautomer normalization preserves the two
    configured centers.
  target_ids:
  - CHEBI:70168
  evidence_ids:
  - record
  - authority
  - chemistry
  - tautomer
- assessment_id: literature-stereo
  area: scope
  topic: Exact natural-product stereochemical assignment
  outcome: unknown
  summary: Later literature uses the fellutanine A name for a presumed S/S material.
    Complete original stereochemical evidence is needed before transferring those
    assays or changing this explicitly meso record. Generic cyclo(Trp-Trp) naming
    is insufficient.
  target_ids:
  - CHEBI:70168
  evidence_ids:
  - adopted
  - later-stereo
  - discovery
- assessment_id: classification
  area: grounding
  topic: Structural parents and antibacterial role
  outcome: supported
  summary: Parents match the valid graph; current ChEBI and the adopted KF620 abstract
    support the named-compound antibacterial attribution. Exact-meso potency remains
    bounded.
  target_ids:
  - CHEBI:70168
  evidence_ids:
  - authority
  - adopted
  - chemistry
- assessment_id: producer
  area: evidence
  topic: Penicillium occurrence
  outcome: supported
  summary: All three adopted abstracts provide relevant Penicillium occurrence context.
    This supports the unquantified definition; no unverified strain-specific biosynthesis
    object is asserted.
  target_ids:
  - CHEBI:70168
  evidence_ids:
  - adopted
- assessment_id: activity
  area: quantity
  topic: Quantitative exact-meso activity
  outcome: unknown
  summary: Original fellutanine assay details were not accessible; no numerical native
    MIC or transfer from the later S/S panel is justified.
  target_ids:
  - CHEBI:70168
  evidence_ids:
  - adopted
  - supplement
  - later-stereo
  - access
- assessment_id: mechanism
  area: evidence
  topic: Antibacterial molecular target
  outcome: unknown
  summary: Native has no molecular-target edge. Eutypoid GSK-3β activity and FelB
    biosynthesis do not identify a fellutanine antibacterial target.
  target_ids:
  - CHEBI:70168
  evidence_ids:
  - adopted
  - biosynthesis
  - record
- assessment_id: registry
  area: grounding
  topic: Reaxys mapping
  outcome: unknown
  summary: Current ChEBI supports the registry attribution; direct registry access
    failed, leaving independent form/stereo scope unverified.
  target_ids:
  - CHEBI:70168
  evidence_ids:
  - authority
  - access
- assessment_id: ownership
  area: ownership
  topic: Maintained repair and provenance
  outcome: supported
  summary: Invalid text is traceable to the adopted ChEBI row and unchanged current
    upstream JSON. A maintained correction is needed; refreshing unchanged upstream
    input or editing only generated YAML would not resolve recurrence.
  target_ids:
  - CHEBI:70168
  evidence_ids:
  - owners
  - authority
findings:
- finding_id: F1
  issue_key: chebi-70168-invalid-smiles-two-missing-indole-hydrogens
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Both indole nitrogens omit [nH], making the SMILES invalid
  description: The source-derived SMILES contains two bare aromatic indole n atoms
    and fails kekulization. Valid native InChI, current ChEBI molfile and PubChem
    agree on the neutral meso structure. A scratch-only two-[nH] repair reproduces
    the same key, formula and configured centers. Current ChEBI JSON still contains
    the defect, so unchanged source refresh is insufficient.
  target_ids:
  - CHEBI:70168
  field_paths:
  - chemical_structure.smiles
  evidence_ids:
  - chemistry
  - authority
  - tautomer
  - owners
  - validation
  rule_id: 'review-checklist: Structure and REVIEWED gate criteria1-2'
  native_severity: Major molecular-encoding inconsistency; native REVIEWED structure
    gate blocked
  normalization_reason: A core chemical representation is unusable, but other exact
    encodings agree on identity. Major severity captures the required representation
    correction without asserting that the whole record denotes a different compound.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted CHEBI:70168 structure input
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI extraction and structure normalization policy
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproduce corrected maintained structure in generated record
actions:
- action_id: A1
  description: 'Implement a documented maintained ChEBI structure correction and regenerate
    the affected record. Verified candidate SMILES: O=C1N[C@H](Cc2c[nH]c3ccccc23)C(=O)N[C@H]1Cc1c[nH]c2ccccc12.
    Preserve the already supported meso identity; do not patch only the generated
    YAML.'
  finding_ids:
  - F1
  target_ids:
  - CHEBI:70168
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted CHEBI:70168 structure input
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI extraction and structure normalization policy
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproduce corrected maintained structure in generated record
  acceptance_checks:
  - Require a sanitized parse with two indole [nH] atoms, C22H20N4O2, charge 0 and
    DNHODRZUCGXYKU-BGYRXZFFSA-N. Preserve the configured R/S meso pair.
  - Require reciprocal chiral graph agreement with the official molfile and PubChem;
    compare Standard InChI after explicit tautomer handling that preserves sp3/bond
    stereo. Do not change valid InChI/key merely to match an invalid input.
  - Make the repair reproducible through the maintained extraction/input policy and
    reseeding, with provenance and meaningful regression coverage for this two-indole
    case.
  - After authorized curation, rerun native chemistry, just validate, just validate-strict,
    just verify-corpus --summary and just qc. Preserve history and leave REVIEWED
    unset until all required native gates pass.
limitations:
- 'All three adopted complete abstracts were read. The 2011 main paper was not obtained:
  the author-repository PDF paths served HTML bot challenges. The official supplement
  covers eutypoids rather than fellutanine.'
- The meso graph is internally supported by valid native and authority structures.
  Exact stereochemical mapping of the antibacterial 2011 material remains unverified;
  later presumed S/S materials and prenylated derivatives cannot be silently equated.
- The first raw InChI-versus-molfile comparison failed due to lactim/lactam representation.
  A separate controlled tautomer check passed while preserving configured centers;
  this does not excuse the independently invalid native SMILES.
- Reaxys 8651145 is repeated by current ChEBI but could not be independently inspected.
- The 2016 source swaps Gram labels for its stated E. coli/S. aureus panel and infers
  fellutanine A stereochemistry from biosynthesis. Its negative measurements remain
  restricted to that reported material and panel.
- No primary molecular-target mechanism or clinical efficacy was established for the
  exact native compound.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Root native schema/strict results and initial captures were reused at the unchanged
  base; validation_plan independently completed chemical comparison and primary-source
  scope review.
- Standalone chemistry used the batch 019 interpreter against batch 044; the source
  ledger and contract use batch 044.
- No native gene/protein/pathway is asserted. Adjacent biosynthetic enzymes and eutypoid
  kinase assays were excluded before any mechanism adoption, so a bacterial structured
  adapter was not applicable.
- The review preserves native bytes and scientific status; the suggested SMILES exists
  only in scratch evidence and this proposed action.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:70168
- https://pubchem.ncbi.nlm.nih.gov/compound/6571639
- https://pubmed.ncbi.nlm.nih.gov/10867952/
- https://pubmed.ncbi.nlm.nih.gov/14520967/
- https://doi.org/10.1021/np100633k
- https://doi.org/10.1021/np100633k.s001
- https://doi.org/10.1021/np9903853
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4962026/
- https://doi.org/10.1021/acs.jnatprod.4c01116
tags:
- record-review
- fellutanine
- diketopiperazine
- invalid-smiles
```
