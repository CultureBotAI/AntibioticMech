# Ambiguine H: invalid aromatic SMILES with independently recoverable exact identity

- Review: 20261021T084934Z-ambiguine-h-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:35:44Z
- Finished UTC: 2026-10-21T08:49:34Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The retained InChI, full key, formula and stereochemistry identify ambiguine H, but the native SMILES is invalid because the pyrrolic nitrogen lacks its hydrogen. A scratch-only [nH] correction regenerates the exact retained structure and matches independent PubChem and ChemSpider encodings. Primary evidence supports antimicrobial roles with the stated access and assay boundaries.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position089; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65400 | data/antibiotics/antibacterial/ambiguine-h.yaml | generated | ambiguine H |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | CHEBI:65400 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:65400 | Actual focused execution exited 0. |
| Focused chemistry verification | failed | False | CHEBI:65400 | Actual focused execution exited 1. |
| Authoritative full QC | failed | True | CHEBI:65400 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65400 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65400 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65400 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65400 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65400 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65400 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65400 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65400 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Recoverable exact compound

identity: supported. Targets: CHEBI:65400.

Retained InChI/full key and external encodings agree on the named exact structure.

### Malformed aromatic nitrogen

consistency: concern. Targets: CHEBI:65400.

Native SMILES fails sanitization; a one-atom hydrogen correction reproduces the independently corroborated identity.

### Parents and both activity roles

grounding: supported. Targets: CHEBI:65400.

Broader chemical parents fit and primary biological evidence supports antibacterial/antifungal activity within inspected scope.

### External identifier coverage

identity: unknown. Targets: CHEBI:65400.

ChemSpider exact full key is verified; Reaxys detail was not independently accessible.

### Primary activity and producer context

completeness: unknown. Targets: CHEBI:65400.

Optional detailed annotations need exact preparation, organism and endpoint evidence. Isolation wording does not identify a biosynthetic pathway; no molecular target is asserted.

### Source and seed provenance

ownership: supported. Targets: CHEBI:65400.

Raw/current source share the defect; all13 captures and deterministic mint are unchanged.

## Findings

### F1: Restore the pyrrolic hydrogen in the imported SMILES

major / open / confirmed; issue key: chebi-65400-ambiguine-h-invalid-pyrrolic-smiles.

Native SMILES uses aromatic n where the retained exact structure requires [nH], causing kekulization failure. The same source defect exists in current ChEBI. Scratch correction regenerates DBOXZAYTFKDLHJ-CSOFANMDSA-N and agrees with independent valid PubChem and ChemSpider representations.

## Recommended Actions And Acceptance Checks

### A1

Correct the inherited aromatic nitrogen representation through the maintained source/import route.

- Use a valid pyrrolic [nH] encoding; both resulting structure encodings must regenerate DBOXZAYTFKDLHJ-CSOFANMDSA-N. Preserve all4 specified centres, native formula, neutral total charge and isonitrile charge representation.
- Use upstream correction or documented extractor handling; do not hand-edit immutable source snapshots or erase stereochemistry to force agreement.
- Retain provenance and run independent sanitization/full-key comparison, schema, strict, source-reproduction and history gates. Existing schema/strict success did not detect this chemical defect.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/ambiguine-h.yaml; Entire YAML and three seed/reseed events | supports | SEEDED/EXACT neutral C26H32N2, 4 assigned tetrahedral centres, systematic stereochemical name, isonitrile synonym, chemical parents and antibacterial/antifungal roles. ChemSpider17214460 and Reaxys18851757 are the only chemical xrefs. No quantitative activity, direct target, mechanism, resistance, structured producer, clinical claim or graph is asserted. |
| owner | data/raw/chebi_antimicrobials.tsv; Exact row in 089-raw.json; source extractor/seeder and manifest | supports | Raw ChEBI row repeats the malformed aromatic SMILES and the independently consistent InChI/key. All13 captured maintained inputs remain unchanged, and source-specific mint reproduces. The source supplies three adopted publication leads. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:65400; 089-chebi-clean.txt; complete current entry | supports | Current ChEBI repeats native name, systematic stereo, formula, full key, masses, chemical parents, roles and malformed SMILES. The broad Fischerella isolation statement is source-derived. Fischerella is a genus, not a resolved strain identifier; no exact producer strain should be inferred from this wording. |
| chemistry | Independent native and scratch-only RDKit comparison; 089-chemistry-final.json/log; check_ambiguine.py | supports | Native aromatic n fails kekulization. Replacing that one pyrrolic atom with [nH] in scratch yields DBOXZAYTFKDLHJ-CSOFANMDSA-N, the native formula/charge/masses and all4 assigned centres. Native InChI parsed without initial sanitization and then explicitly sanitized is valid and regenerates the same key. PubChem valid SMILES independently agrees. This is a specific SMILES hydrogen/aromaticity defect, not evidence to replace the retained identity. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/16069590; 089-pubchem.json, full-key lookup and independently parsed SMILES | supports | CID16069590 provides a valid structure and matching InChI/key DBOXZAYTFKDLHJ-CSOFANMDSA-N, formula and charge. Rounding of average mass in PubChem is compatible with the more precise native mass. |
| chemspider | https://www.chemspider.com/Chemical-Structure.17214460.html; Visible full entry and JSON-LD MolecularEntity identifiers | supports | Exact linked ChemSpider accession names ambiguine H isonitrile and supplies the native InChI and full key. Its InChI was independently parsed/sanitized to DBOXZAYTFKDLHJ-CSOFANMDSA-N; formula, masses and systematic name agree. Reaxys remains corroborated by the ChEBI mapping, not independently inspected. |
| ontology | CHEBI:141618; CHEBI:35353; CHEBI:33282; CHEBI:35718; 089-ols-parents.json and complete ChEBI outgoing relations | supports | Ambiguine and isocyanide parents are broader; heterotetracyclic structure fits the retained graph. Antibacterial filing retains the antifungal role. Pyrrolic hydrogen repair does not change these chemical classes. |
| isolation2007 | PMID:17315959; DOI:10.1021/np060495r; complete original abstract in 089-adopted.json | partial | Cultured Fischerella sp. from Israel yielded nine isonitrile compounds; ambiguines H, I and J were newly characterized by spectroscopy/MS. The abstract explicitly reports antibacterial and antimycotic activity for H and I. Publisher full text returned403, so detailed assay values, strains, purity and spectra were not inspected. The broad roles and isolation context are supported at abstract level. |
| synthesis2014 | PMID:25983347; DOI:10.1016/j.tet.2014.11.010; PMC4430130 abstract, Results2.3, conclusion, final compound4.2.16 and crystallographic-data section | supports | The full-account study explicitly synthesizes (+)-ambiguine H as compound5a, distinguishes the C6-prenylated isomer46 and hapalindole U, and reports C26H32N2-compatible HRMS, NMR, positive optical rotation and crystal deposition CCDC623052. This supports exact named-compound identity; it is synthetic characterization, not a new antimicrobial assay. Raw diffraction coordinates were not re-refined. |
| synthesis2018 | PMID:30336678; DOI:10.1021/acs.orglett.8b02804; complete adopted abstract | context_only | Stereodivergent syntheses of nine hapalindole/ambiguine alkaloids include the named H compound. This is additional synthetic identity context, not direct antimicrobial target evidence. Full paper was not inspected. |
| scope | Exact ambiguine H primary follow-up; Bounded isolation and synthesis searches | context_only | The2009 Fischerella ambigua antimicrobial panel includes ambiguine I and hapalindole H, but not ambiguine H among its listed assay compounds; its numeric results are not transferred here. Biosynthetic-cluster search hits and other ambiguine-family mechanisms remain unassessed leads. |
| search | CultureBotAI/AntibioticMech; 089-local-hits.txt and081089090-maintained-hits.txt | context_only | Ignored-inclusive searches identify source/native/queue references and historical discovery/status artifacts. All adopted references were dispositioned. Native record has no gene/protein/pathway/transcriptomic assertion requiring a pre-web biological adapter. No literature-absence conclusion is drawn. |

## Limits And Additional Notes

- Original2007 full text was unavailable through the publisher (HTTP403); its complete abstract supports only the stated qualitative isolation/activity scope. Reaxys was not independently inspected.
- The native SMILES check fails as reported; valid native InChI was verified via explicit sanitization after parsing. Scratch corrections were not applied to any native or raw record.
- EuropePMC fullTextXML requests failed HTTP500 for the follow-up primary; its public PMC HTML was successfully retrieved and the specifically cited sections read.
- The independent chemistry helper initially used an incorrect mint-input convention; it was corrected to source&#124;source_id before the reported final calculation. The final failure is specifically the native invalid SMILES.
- The2014/2015 synthesis full account was read in the listed H-specific sections, not every intermediate procedure. The2018 synthesis was assessed at abstract level. No numeric antimicrobial observation or molecular target is independently verified here.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T084934Z-ambiguine-h-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Ambiguine H: invalid aromatic SMILES with independently recoverable exact
  identity'
started_at: '2026-10-21T08:35:44Z'
finished_at: '2026-10-21T08:49:34Z'
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
summary: The retained InChI, full key, formula and stereochemistry identify ambiguine
  H, but the native SMILES is invalid because the pyrrolic nitrogen lacks its hydrogen.
  A scratch-only [nH] correction regenerates the exact retained structure and matches
  independent PubChem and ChemSpider encodings. Primary evidence supports antimicrobial
  roles with the stated access and assay boundaries.
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
  - path: data/antibiotics/antibacterial/ambiguine-h.yaml
    sha256: 10bb8d8809faa5f0258d20869d244312c68b59648dd9c57d164abe4cea13872e
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
- target_id: CHEBI:65400
  path: data/antibiotics/antibacterial/ambiguine-h.yaml
  label: ambiguine H
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
  selection: Initially uncovered queue position089; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65400
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65400
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/ambiguine-h.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65400
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/ambiguine-h.yaml --out /private/tmp/am-review-session/089-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: failed
  required: false
  summary: Actual focused execution exited 1.
  target_ids:
  - CHEBI:65400
  command: .venv/bin/python /private/tmp/am-review-session/check_ambiguine.py 89
  exit_code: 1
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
  - CHEBI:65400
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
  - CHEBI:65400
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
  - CHEBI:65400
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
  - CHEBI:65400
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
  - CHEBI:65400
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
  - CHEBI:65400
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
  - CHEBI:65400
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
  - CHEBI:65400
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
  - CHEBI:65400
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/ambiguine-h.yaml
  locator: Entire YAML and three seed/reseed events
  accessed_at: '2026-10-21T08:49:08Z'
  support: supports
  summary: SEEDED/EXACT neutral C26H32N2, 4 assigned tetrahedral centres, systematic
    stereochemical name, isonitrile synonym, chemical parents and antibacterial/antifungal
    roles. ChemSpider17214460 and Reaxys18851757 are the only chemical xrefs. No quantitative
    activity, direct target, mechanism, resistance, structured producer, clinical
    claim or graph is asserted.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Exact row in 089-raw.json; source extractor/seeder and manifest
  accessed_at: '2026-10-21T08:49:08Z'
  support: supports
  summary: Raw ChEBI row repeats the malformed aromatic SMILES and the independently
    consistent InChI/key. All13 captured maintained inputs remain unchanged, and source-specific
    mint reproduces. The source supplies three adopted publication leads.
  snapshot_sha256: 80b03554e90ae2b64e52707b178bc4a199197cdd24521c58a818cf64b62a223d
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:65400
  locator: 089-chebi-clean.txt; complete current entry
  accessed_at: '2026-10-21T08:49:08Z'
  support: supports
  summary: Current ChEBI repeats native name, systematic stereo, formula, full key,
    masses, chemical parents, roles and malformed SMILES. The broad Fischerella isolation
    statement is source-derived. Fischerella is a genus, not a resolved strain identifier;
    no exact producer strain should be inferred from this wording.
  snapshot_sha256: 4953310034893697207a4a580578c72f60e66e9e2c137af83b9a87ef3c6bca1f
- evidence_id: chemistry
  kind: validation
  reference: Independent native and scratch-only RDKit comparison
  locator: 089-chemistry-final.json/log; check_ambiguine.py
  accessed_at: '2026-10-21T08:49:08Z'
  support: supports
  summary: Native aromatic n fails kekulization. Replacing that one pyrrolic atom
    with [nH] in scratch yields DBOXZAYTFKDLHJ-CSOFANMDSA-N, the native formula/charge/masses
    and all4 assigned centres. Native InChI parsed without initial sanitization and
    then explicitly sanitized is valid and regenerates the same key. PubChem valid
    SMILES independently agrees. This is a specific SMILES hydrogen/aromaticity defect,
    not evidence to replace the retained identity.
  snapshot_sha256: 008966e2c45d4650fa13ded8b71c5e662577d88d720208bb2b129b9c0fa6590e
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/16069590
  locator: 089-pubchem.json, full-key lookup and independently parsed SMILES
  accessed_at: '2026-10-21T08:49:08Z'
  support: supports
  summary: CID16069590 provides a valid structure and matching InChI/key DBOXZAYTFKDLHJ-CSOFANMDSA-N,
    formula and charge. Rounding of average mass in PubChem is compatible with the
    more precise native mass.
  snapshot_sha256: 7230fafa268ae0b3eb6f8fe221c2c0869607d46f3f9f9db9cf5ab9a5f7909a41
- evidence_id: chemspider
  kind: database
  reference: https://www.chemspider.com/Chemical-Structure.17214460.html
  locator: Visible full entry and JSON-LD MolecularEntity identifiers
  accessed_at: '2026-10-21T08:49:08Z'
  support: supports
  summary: Exact linked ChemSpider accession names ambiguine H isonitrile and supplies
    the native InChI and full key. Its InChI was independently parsed/sanitized to
    DBOXZAYTFKDLHJ-CSOFANMDSA-N; formula, masses and systematic name agree. Reaxys
    remains corroborated by the ChEBI mapping, not independently inspected.
  snapshot_sha256: d2cafca9bbb7861b95c67dd64423b72c437add692be504d3e5a33acd56b61991
- evidence_id: ontology
  kind: authority
  reference: CHEBI:141618; CHEBI:35353; CHEBI:33282; CHEBI:35718
  locator: 089-ols-parents.json and complete ChEBI outgoing relations
  accessed_at: '2026-10-21T08:49:08Z'
  support: supports
  summary: Ambiguine and isocyanide parents are broader; heterotetracyclic structure
    fits the retained graph. Antibacterial filing retains the antifungal role. Pyrrolic
    hydrogen repair does not change these chemical classes.
  snapshot_sha256: 09b72d9df75fcef275637c4cc2e7110c3967795a148f68f58c6f3bd6daa02091
- evidence_id: isolation2007
  kind: primary_source
  reference: PMID:17315959
  locator: DOI:10.1021/np060495r; complete original abstract in 089-adopted.json
  accessed_at: '2026-10-21T08:49:08Z'
  support: partial
  summary: Cultured Fischerella sp. from Israel yielded nine isonitrile compounds;
    ambiguines H, I and J were newly characterized by spectroscopy/MS. The abstract
    explicitly reports antibacterial and antimycotic activity for H and I. Publisher
    full text returned403, so detailed assay values, strains, purity and spectra were
    not inspected. The broad roles and isolation context are supported at abstract
    level.
  snapshot_sha256: debab5656cb4ff1fb7b93486a604970402ba09a32167247a70127c4e80e4a7c6
- evidence_id: synthesis2014
  kind: primary_source
  reference: PMID:25983347
  locator: DOI:10.1016/j.tet.2014.11.010; PMC4430130 abstract, Results2.3, conclusion,
    final compound4.2.16 and crystallographic-data section
  accessed_at: '2026-10-21T08:49:08Z'
  support: supports
  summary: The full-account study explicitly synthesizes (+)-ambiguine H as compound5a,
    distinguishes the C6-prenylated isomer46 and hapalindole U, and reports C26H32N2-compatible
    HRMS, NMR, positive optical rotation and crystal deposition CCDC623052. This supports
    exact named-compound identity; it is synthetic characterization, not a new antimicrobial
    assay. Raw diffraction coordinates were not re-refined.
  snapshot_sha256: bb51f8665c008152caa9a242445aee460591cc023bfd92ec0b817e8a1eafc740
- evidence_id: synthesis2018
  kind: primary_source
  reference: PMID:30336678
  locator: DOI:10.1021/acs.orglett.8b02804; complete adopted abstract
  accessed_at: '2026-10-21T08:49:08Z'
  support: context_only
  summary: Stereodivergent syntheses of nine hapalindole/ambiguine alkaloids include
    the named H compound. This is additional synthetic identity context, not direct
    antimicrobial target evidence. Full paper was not inspected.
- evidence_id: scope
  kind: search
  reference: Exact ambiguine H primary follow-up
  locator: Bounded isolation and synthesis searches
  accessed_at: '2026-10-21T08:49:08Z'
  support: context_only
  summary: The2009 Fischerella ambigua antimicrobial panel includes ambiguine I and
    hapalindole H, but not ambiguine H among its listed assay compounds; its numeric
    results are not transferred here. Biosynthetic-cluster search hits and other ambiguine-family
    mechanisms remain unassessed leads.
  search_scope: Exact ambiguine H/isonitrile, adopted PMIDs, synthesis DOI and public
    PMC full account; no exhaustive mechanism or producer absence claim.
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 089-local-hits.txt and081089090-maintained-hits.txt
  accessed_at: '2026-10-21T08:49:08Z'
  support: context_only
  summary: Ignored-inclusive searches identify source/native/queue references and
    historical discovery/status artifacts. All adopted references were dispositioned.
    Native record has no gene/protein/pathway/transcriptomic assertion requiring a
    pre-web biological adapter. No literature-absence conclusion is drawn.
  search_scope: rg --no-ignore --hidden across isolated batch009 excluding .git/.venv;
    targeted maintained follow-up with large .obo/.jsonl/.html exclusions limited
    to that narrower pass. Public ChEBI/OLS, PubChem, ChemSpider, EuropePMC, PMC and
    original publisher access attempts.
assessments:
- assessment_id: identity
  area: identity
  topic: Recoverable exact compound
  outcome: supported
  summary: Retained InChI/full key and external encodings agree on the named exact
    structure.
  target_ids:
  - CHEBI:65400
  evidence_ids:
  - native
  - pubchem
  - chemspider
  - chemistry
- assessment_id: smiles
  area: consistency
  topic: Malformed aromatic nitrogen
  outcome: concern
  summary: Native SMILES fails sanitization; a one-atom hydrogen correction reproduces
    the independently corroborated identity.
  target_ids:
  - CHEBI:65400
  evidence_ids:
  - chemistry
  - owner
  - chebi
- assessment_id: classes
  area: grounding
  topic: Parents and both activity roles
  outcome: supported
  summary: Broader chemical parents fit and primary biological evidence supports antibacterial/antifungal
    activity within inspected scope.
  target_ids:
  - CHEBI:65400
  evidence_ids:
  - ontology
  - isolation2007
- assessment_id: xref
  area: identity
  topic: External identifier coverage
  outcome: unknown
  summary: ChemSpider exact full key is verified; Reaxys detail was not independently
    accessible.
  target_ids:
  - CHEBI:65400
  evidence_ids:
  - chemspider
  - chebi
- assessment_id: completeness
  area: completeness
  topic: Primary activity and producer context
  outcome: unknown
  summary: Optional detailed annotations need exact preparation, organism and endpoint
    evidence. Isolation wording does not identify a biosynthetic pathway; no molecular
    target is asserted.
  target_ids:
  - CHEBI:65400
  evidence_ids:
  - isolation2007
  - synthesis2014
  - scope
- assessment_id: ownership
  area: ownership
  topic: Source and seed provenance
  outcome: supported
  summary: Raw/current source share the defect; all13 captures and deterministic mint
    are unchanged.
  target_ids:
  - CHEBI:65400
  evidence_ids:
  - native
  - owner
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-65400-ambiguine-h-invalid-pyrrolic-smiles
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Restore the pyrrolic hydrogen in the imported SMILES
  description: Native SMILES uses aromatic n where the retained exact structure requires
    [nH], causing kekulization failure. The same source defect exists in current ChEBI.
    Scratch correction regenerates DBOXZAYTFKDLHJ-CSOFANMDSA-N and agrees with independent
    valid PubChem and ChemSpider representations.
  target_ids:
  - CHEBI:65400
  field_paths:
  - chemical_structure.smiles
  evidence_ids:
  - native
  - owner
  - chebi
  - chemistry
  - pubchem
  - chemspider
  rule_id: 'native-review-checklist: Chemical structure consistency'
  native_severity: major invalid structure serialization
  normalization_reason: The exact molecule is recoverable from retained InChI and
    independent authorities, but one native structure field is not a valid representation.
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
actions:
- action_id: A1
  description: Correct the inherited aromatic nitrogen representation through the
    maintained source/import route.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65400
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
  acceptance_checks:
  - Use a valid pyrrolic [nH] encoding; both resulting structure encodings must regenerate
    DBOXZAYTFKDLHJ-CSOFANMDSA-N. Preserve all4 specified centres, native formula,
    neutral total charge and isonitrile charge representation.
  - Use upstream correction or documented extractor handling; do not hand-edit immutable
    source snapshots or erase stereochemistry to force agreement.
  - Retain provenance and run independent sanitization/full-key comparison, schema,
    strict, source-reproduction and history gates. Existing schema/strict success
    did not detect this chemical defect.
limitations:
- Original2007 full text was unavailable through the publisher (HTTP403); its complete
  abstract supports only the stated qualitative isolation/activity scope. Reaxys was
  not independently inspected.
- The native SMILES check fails as reported; valid native InChI was verified via explicit
  sanitization after parsing. Scratch corrections were not applied to any native or
  raw record.
- EuropePMC fullTextXML requests failed HTTP500 for the follow-up primary; its public
  PMC HTML was successfully retrieved and the specifically cited sections read.
- The independent chemistry helper initially used an incorrect mint-input convention;
  it was corrected to source|source_id before the reported final calculation. The
  final failure is specifically the native invalid SMILES.
- The2014/2015 synthesis full account was read in the listed H-specific sections,
  not every intermediate procedure. The2018 synthesis was assessed at abstract level.
  No numeric antimicrobial observation or molecular target is independently verified
  here.
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
