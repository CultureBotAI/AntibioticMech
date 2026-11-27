# Cadaside A: exact structure and calcium-dependent antibacterial evidence

- Review: 20261021T103531Z-cadaside-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:11:10Z
- Finished UTC: 2026-10-21T10:35:31Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native PubChem structure, ARO classification and broad antibacterial definition are supported. Original isolation and assay evidence can be added with ammonium-salt, calcium, compound and heterologous-production qualifications. Current ChEBI InChI agrees, but its SMILES omits alkene geometry. No confirmed native correction was established. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position176; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-07e4fbc49d | data/antibiotics/antibacterial/cadaside-a.yaml | generated | cadaside A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-07e4fbc49d | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-07e4fbc49d | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-07e4fbc49d | Actual focused execution exited 0. |
| Structured protein-context applicability | not_applicable | False | antibioticmech:aro-07e4fbc49d | The native contains no named protein, gene, regulator, pathway or transcriptomic-response claim. Nonribosomal peptide is a structural/biosynthetic class; literature-only synthetases and A-specific cell-wall effects are not native molecular targets. |
| Authoritative full QC | failed | True | antibioticmech:aro-07e4fbc49d | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-07e4fbc49d | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-07e4fbc49d | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-07e4fbc49d | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-07e4fbc49d | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-07e4fbc49d | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-07e4fbc49d | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-07e4fbc49d | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-07e4fbc49d | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact graph and stereochemical limits

identity: supported. Targets: antibioticmech:aro-07e4fbc49d.

Native representation agrees with original structural scope and current full InChI mappings; external ChEBI SMILES omissions are qualified.

### ARO classification and exact cross-references

grounding: supported. Targets: antibioticmech:aro-07e4fbc49d.

Source mint, exact compound cross-references and nonribosomal-peptide antibiotic class are supported.

### Definition and primary activity

evidence: supported. Targets: antibioticmech:aro-07e4fbc49d.

Natural-compound activity supports the broad native definition. Synthetic epimer results are kept separate.

### Maintained sources and initial hashes

provenance: supported. Targets: antibioticmech:aro-07e4fbc49d.

Initial input captures, actual source owners and source history are retained without native edits.

### Optional assay, producer and mechanism curation

completeness: unknown. Targets: antibioticmech:aro-07e4fbc49d.

Primary data support optional enrichment with exact compound, material, calcium and heterologous-host qualifiers. Optional blanks are not defects.

### Focused gates and chemical consistency

schema: supported. Targets: antibioticmech:aro-07e4fbc49d.

Focused schema, strict and molecular checks pass.

## Findings

### F1: Add primary activity with calcium and isolated-material qualifications

informational / open / confirmed; issue key: cadaside-a-qualified-primary-enrichment.

The2019 discovery and supporting Methods provide exact-compound activity beyond the family-level synthesis citation. Optional enrichment must preserve ammonium-salt preparation and100mM calcium; A-specific mechanistic evidence and an unidentified natural soil producer need separate scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally curate the original discovery with exact compound and assay boundaries.

- Use compound-specific TableS5 values, preserving strain, medium,100mM calcium,18h/37C, visible-growth endpoint, units, replicate count and censoring; verify neutral-parent mass basis before conversion.
- Record S.albus J1074 as a demonstrated heterologous producer, with construct/cluster provenance; do not infer the native soil producer, or call E.coli cloning and yeast assembly hosts producers.
- Keep cell-wall and membrane experiments A-specific and phenotype-level. Do not create a direct protein target or transfer mechanism to B. Distinguish natural compounds from inactive2022 synthetic material.
- Preserve native2Z/4E geometry and A’s unassigned lipidC8; qualify external ChEBI SMILES omissions. Use validated writers and history only during separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cadaside-a.yaml; Entire44-line native record and initial16 hashed inputs | supports | The SEEDED ARO mint contains a neutral molecular graph, antibacterial class, nonribosomal-peptide structural class, one family-level definition citation and ARO/ChEBI/PubChem cross-references. No target, producer, resistance observation, quantitative susceptibility or causal graph is populated. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/seed_from_sources.py; scripts/enrich_pubchem_structures.py; 176-raw-all.json; original and supplemental input captures | supports | The exact adopted ARO row and PubChem enrichment reproduce the native fields. Initial capture was preserved; actual ARO/PubChem owners were added before detailed judgment. Source mint independently reproduces the identifier. Inclusive local searches covered hidden and ignored files outside Git internals/virtual environments; no curator override was found in inspected maintained inputs. |
| chemistry | Independent native SMILES and InChI parsing; 176-chemistry.json; focused schema and strict outputs | supports | Both molecular encodings reproduce HKTPJHSXELPTFT-UBMKZYSCSA-N, the full formula, neutral charge, single component and both masses at stored precision. Both2Z/4E lipid double bonds are specified. Fourteen of fifteen potential tetrahedral centres are assigned; lipid C8 is deliberately unassigned, matching the original drawing rather than establishing a racemate. |
| external | PubChem:146682091; ChEBI:226051; 176-pubchem.json; 176-chebi.json; 018-cadaside-chebi-chemistry.json | partial | Current PubChem and ChEBI InChI reproduce the native full key. The current ChEBI SMILES retains4E but omits2Z and produces a different stereo key. This external descriptor inconsistency does not invalidate the ChEBI concept mapping or justify replacing the correct native structure. The native remains an ARO mint because its adopted ChEBI antibacterial inventory has no exact row; discovery of a current cross-reference alone is not a required grounding migration. |
| aro | ARO:3007630; ARO:3007631; ARO:3007629; ARO:3009657; 018-root-aro-stanzas.txt; external cached ontology hashed before inspection | supports | The individual ARO concepts sit under the cadaside family and nonribosomal-peptide antibiotic class. Family and member definition references lead to the2022 synthesis paper. The biosynthetic machinery in the2019 original study supports nonribosomal-peptide classification, without making the synthetases bacterial drug targets. |
| discovery | PMID:30735616; DOI:10.1021/jacs.8b12087; 176-primary.pdf, scientific main text pp1–8; Figure2 rendered p3 | supports | Original environmental-DNA discovery isolated two related13-residue lipopeptides with a nine-residue macrocycle. A and B share the peptide and differ in their2Z,4E lipid chains. Soil DNA from three overlapping cosmids was assembled into a108.4-kb contig containing a65.8-kb biosynthetic cluster. Heterologous Streptomyces albus J1074 produced both compounds compared with empty-vector controls; the native soil producer was not identified. Final preparative HPLC yielded the compounds as ammonium salts. |
| stereochemistry | DOI:10.1021/jacs.8b12087.s001; 176-si-0.pdf; Methods and structure discussion pp4–8; rendered TablesS3/S4 p12 | supports | Marfey analysis and GITC methods support the authors’ amino-acid assignments, including D-Glu3/11, D-Ile6 and D-AMPA, with L assignments for the other reported chiral residues. Hydroxyaspartate is assigned2S,3R and hydroxyglutamate2S,4R. A has8-methyldeca-2Z,4E-dienoyl and B8-methylnona-2Z,4E-dienoyl chains. The source leaves A lipidC8 unassigned. Raw spectra were not independently reconstructed; some Ile/allo-Ile derivative retention times coincide in TableS3, so the review retains author assignment and its analytical limits. |
| activity | PMID:30735616; DOI:10.1021/jacs.8b12087.s001; Main biological Results; SI antibacterial Methods pp4–5 and rendered TableS5 p13 | supports | Triplicate visible-growth MIC assays used LB,100mM CaCl2,0.03–64micrograms/mL compound, overnight cultures diluted5000-fold,50microlitre wells and37C/18h incubation. Both compounds inhibit the tested Gram-positive bacteria. For S.aureus RN4220 both MICs are4micrograms/mL; for USA300 A is8 and B16. Most Gram-negative bacteria and all three yeasts are above the tested range. E.coli BAS849 differs: A32–64 and B&gt;64. These are ammonium-salt preparations with no established neutral-parent mass correction. Above-range values do not prove universal inactivity or resistance categories. |
| mechanism | PMID:30735616; DOI:10.1021/jacs.8b12087; Main Results and SI mechanism Methods, A-specific experiments | supports | Cadaside A was used for calcium/pH titrations and mechanistic experiments. At the tested conditions SYTOX/DiBAC assays did not show membrane permeabilization or depolarization. Pretreated S.aureus exposed to A accumulated UDP-MurNAc-pentapeptide, supporting cell-wall-biosynthesis interference without resolving a direct molecular target. These A-specific experiments cannot be copied to B. Calcium/soil gene-frequency associations and iron-chelation assays do not establish target binding. Tumour-line MTT results do not establish general safety. |
| adopted | PMID:36168660; DOI:10.1002/chem.202202554; Complete original indexed abstract in 176-literature.json | partial | The source cited by the native definition reports synthesis of proposed cadaside B. The synthetic material differed in NMR from natural material and was inactive; an epimeric relationship was suspected. This is not successful validation of the natural stereostructure, nor evidence that natural B or A is inactive. The narrow family-level statement remains compatible with the original2019 discovery. |

## Limits And Additional Notes

- The original2019 scientific main text pp1–8, Figure2, relevant SI Methods/structure discussion and TablesS3–S5 were inspected. Reference-list pages and every raw NMR/chromatography panel were not independently audited.
- The2022 synthesis paper was assessed through its complete original abstract; detailed experimental assignments were not retrieved. Later analogue work is not used as exact-natural-compound proof.
- Ammonium stoichiometry and free-parent assay mass normalization were not established. Native soil producer and a direct molecular target remain unresolved. No exhaustive clinical, resistance or transcriptomic survey is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All16 repository input hashes remain unchanged. Native records, inventories, histories and curation status were not edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T103531Z-cadaside-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cadaside A: exact structure and calcium-dependent antibacterial evidence'
started_at: '2026-10-21T10:11:10Z'
finished_at: '2026-10-21T10:35:31Z'
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
summary: The native PubChem structure, ARO classification and broad antibacterial
  definition are supported. Original isolation and assay evidence can be added with
  ammonium-salt, calcium, compound and heterologous-production qualifications. Current
  ChEBI InChI agrees, but its SMILES omits alkene geometry. No confirmed native correction
  was established. Scientific assessment retains the stated evidence limits; full
  verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/cadaside-a.yaml
    sha256: 729d1a60d24f91c2da5f10204c1812bc80c7bb69dd2dc7f28e68154c550f84fd
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
- target_id: antibioticmech:aro-07e4fbc49d
  path: data/antibiotics/antibacterial/cadaside-a.yaml
  label: cadaside A
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
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual adopted ARO source or exact PubChem enrichment owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual adopted ARO source or exact PubChem enrichment owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Actual adopted ARO source or exact PubChem enrichment owner
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position176; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-07e4fbc49d
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-07e4fbc49d
  command: .venv/bin/python /private/tmp/am-review-session/focus014-root.py 176
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-07e4fbc49d
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cadaside-a.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-07e4fbc49d
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cadaside-a.yaml --out /private/tmp/am-review-session/176-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-applicability
  name: Structured protein-context applicability
  status: not_applicable
  required: false
  summary: The native contains no named protein, gene, regulator, pathway or transcriptomic-response
    claim. Nonribosomal peptide is a structural/biosynthetic class; literature-only
    synthetases and A-specific cell-wall effects are not native molecular targets.
  target_ids:
  - antibioticmech:aro-07e4fbc49d
  evidence_ids:
  - native
  - aro
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-07e4fbc49d
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
  - antibioticmech:aro-07e4fbc49d
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
  - antibioticmech:aro-07e4fbc49d
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
  - antibioticmech:aro-07e4fbc49d
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
  - antibioticmech:aro-07e4fbc49d
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
  - antibioticmech:aro-07e4fbc49d
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
  - antibioticmech:aro-07e4fbc49d
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
  - antibioticmech:aro-07e4fbc49d
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
  - antibioticmech:aro-07e4fbc49d
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cadaside-a.yaml
  locator: Entire44-line native record and initial16 hashed inputs
  accessed_at: '2026-10-21T10:29:27Z'
  support: supports
  summary: The SEEDED ARO mint contains a neutral molecular graph, antibacterial class,
    nonribosomal-peptide structural class, one family-level definition citation and
    ARO/ChEBI/PubChem cross-references. No target, producer, resistance observation,
    quantitative susceptibility or causal graph is populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/seed_from_sources.py;
    scripts/enrich_pubchem_structures.py
  locator: 176-raw-all.json; original and supplemental input captures
  accessed_at: '2026-10-21T10:29:27Z'
  support: supports
  summary: The exact adopted ARO row and PubChem enrichment reproduce the native fields.
    Initial capture was preserved; actual ARO/PubChem owners were added before detailed
    judgment. Source mint independently reproduces the identifier. Inclusive local
    searches covered hidden and ignored files outside Git internals/virtual environments;
    no curator override was found in inspected maintained inputs.
  snapshot_sha256: 79390f19949072546bb989d95ae91160c819e7492bc6ed35695602476ce4d44c
- evidence_id: chemistry
  kind: validation
  reference: Independent native SMILES and InChI parsing
  locator: 176-chemistry.json; focused schema and strict outputs
  accessed_at: '2026-10-21T10:29:27Z'
  support: supports
  summary: Both molecular encodings reproduce HKTPJHSXELPTFT-UBMKZYSCSA-N, the full
    formula, neutral charge, single component and both masses at stored precision.
    Both2Z/4E lipid double bonds are specified. Fourteen of fifteen potential tetrahedral
    centres are assigned; lipid C8 is deliberately unassigned, matching the original
    drawing rather than establishing a racemate.
  snapshot_sha256: 725f5b9231282a5457122025e05fdcde55186b28719bfd4fdf305d9c383a0081
- evidence_id: external
  kind: database
  reference: PubChem:146682091; ChEBI:226051
  locator: 176-pubchem.json; 176-chebi.json; 018-cadaside-chebi-chemistry.json
  accessed_at: '2026-10-21T10:29:27Z'
  support: partial
  summary: Current PubChem and ChEBI InChI reproduce the native full key. The current
    ChEBI SMILES retains4E but omits2Z and produces a different stereo key. This external
    descriptor inconsistency does not invalidate the ChEBI concept mapping or justify
    replacing the correct native structure. The native remains an ARO mint because
    its adopted ChEBI antibacterial inventory has no exact row; discovery of a current
    cross-reference alone is not a required grounding migration.
  snapshot_sha256: b64380a208af65ab4f5246654012699d26870507dfeecd6621858f70fbc9e4ba
- evidence_id: aro
  kind: authority
  reference: ARO:3007630; ARO:3007631; ARO:3007629; ARO:3009657
  locator: 018-root-aro-stanzas.txt; external cached ontology hashed before inspection
  accessed_at: '2026-10-21T10:29:27Z'
  support: supports
  summary: The individual ARO concepts sit under the cadaside family and nonribosomal-peptide
    antibiotic class. Family and member definition references lead to the2022 synthesis
    paper. The biosynthetic machinery in the2019 original study supports nonribosomal-peptide
    classification, without making the synthetases bacterial drug targets.
- evidence_id: discovery
  kind: primary_source
  reference: PMID:30735616; DOI:10.1021/jacs.8b12087
  locator: 176-primary.pdf, scientific main text pp1–8; Figure2 rendered p3
  accessed_at: '2026-10-21T10:29:27Z'
  support: supports
  summary: Original environmental-DNA discovery isolated two related13-residue lipopeptides
    with a nine-residue macrocycle. A and B share the peptide and differ in their2Z,4E
    lipid chains. Soil DNA from three overlapping cosmids was assembled into a108.4-kb
    contig containing a65.8-kb biosynthetic cluster. Heterologous Streptomyces albus
    J1074 produced both compounds compared with empty-vector controls; the native
    soil producer was not identified. Final preparative HPLC yielded the compounds
    as ammonium salts.
  snapshot_sha256: 48689c1a02fc8cb9bd7e0c8cf8d11880525211fec9f90e8f8f6cb66610d2416f
- evidence_id: stereochemistry
  kind: primary_source
  reference: DOI:10.1021/jacs.8b12087.s001
  locator: 176-si-0.pdf; Methods and structure discussion pp4–8; rendered TablesS3/S4
    p12
  accessed_at: '2026-10-21T10:29:27Z'
  support: supports
  summary: Marfey analysis and GITC methods support the authors’ amino-acid assignments,
    including D-Glu3/11, D-Ile6 and D-AMPA, with L assignments for the other reported
    chiral residues. Hydroxyaspartate is assigned2S,3R and hydroxyglutamate2S,4R.
    A has8-methyldeca-2Z,4E-dienoyl and B8-methylnona-2Z,4E-dienoyl chains. The source
    leaves A lipidC8 unassigned. Raw spectra were not independently reconstructed;
    some Ile/allo-Ile derivative retention times coincide in TableS3, so the review
    retains author assignment and its analytical limits.
  snapshot_sha256: dac79644ef8ae187dcda44149028a4a960a2c5a7f58f38ac2e0a7101c913ac94
- evidence_id: activity
  kind: primary_source
  reference: PMID:30735616; DOI:10.1021/jacs.8b12087.s001
  locator: Main biological Results; SI antibacterial Methods pp4–5 and rendered TableS5
    p13
  accessed_at: '2026-10-21T10:29:27Z'
  support: supports
  summary: 'Triplicate visible-growth MIC assays used LB,100mM CaCl2,0.03–64micrograms/mL
    compound, overnight cultures diluted5000-fold,50microlitre wells and37C/18h incubation.
    Both compounds inhibit the tested Gram-positive bacteria. For S.aureus RN4220
    both MICs are4micrograms/mL; for USA300 A is8 and B16. Most Gram-negative bacteria
    and all three yeasts are above the tested range. E.coli BAS849 differs: A32–64
    and B>64. These are ammonium-salt preparations with no established neutral-parent
    mass correction. Above-range values do not prove universal inactivity or resistance
    categories.'
  snapshot_sha256: dac79644ef8ae187dcda44149028a4a960a2c5a7f58f38ac2e0a7101c913ac94
- evidence_id: mechanism
  kind: primary_source
  reference: PMID:30735616; DOI:10.1021/jacs.8b12087
  locator: Main Results and SI mechanism Methods, A-specific experiments
  accessed_at: '2026-10-21T10:29:27Z'
  support: supports
  summary: Cadaside A was used for calcium/pH titrations and mechanistic experiments.
    At the tested conditions SYTOX/DiBAC assays did not show membrane permeabilization
    or depolarization. Pretreated S.aureus exposed to A accumulated UDP-MurNAc-pentapeptide,
    supporting cell-wall-biosynthesis interference without resolving a direct molecular
    target. These A-specific experiments cannot be copied to B. Calcium/soil gene-frequency
    associations and iron-chelation assays do not establish target binding. Tumour-line
    MTT results do not establish general safety.
  snapshot_sha256: 48689c1a02fc8cb9bd7e0c8cf8d11880525211fec9f90e8f8f6cb66610d2416f
- evidence_id: adopted
  kind: primary_source
  reference: PMID:36168660; DOI:10.1002/chem.202202554
  locator: Complete original indexed abstract in 176-literature.json
  accessed_at: '2026-10-21T10:29:27Z'
  support: partial
  summary: The source cited by the native definition reports synthesis of proposed
    cadaside B. The synthetic material differed in NMR from natural material and was
    inactive; an epimeric relationship was suspected. This is not successful validation
    of the natural stereostructure, nor evidence that natural B or A is inactive.
    The narrow family-level statement remains compatible with the original2019 discovery.
  snapshot_sha256: f0c24d5a097a9509fd08b4b3a4636a5624b4f5b9bb3c857ef5cbc1f89055d4cb
assessments:
- assessment_id: identity
  area: identity
  topic: Exact graph and stereochemical limits
  outcome: supported
  summary: Native representation agrees with original structural scope and current
    full InChI mappings; external ChEBI SMILES omissions are qualified.
  target_ids:
  - antibioticmech:aro-07e4fbc49d
  evidence_ids:
  - chemistry
  - external
  - stereochemistry
- assessment_id: grounding
  area: grounding
  topic: ARO classification and exact cross-references
  outcome: supported
  summary: Source mint, exact compound cross-references and nonribosomal-peptide antibiotic
    class are supported.
  target_ids:
  - antibioticmech:aro-07e4fbc49d
  evidence_ids:
  - owners
  - aro
  - external
  - discovery
- assessment_id: evidence
  area: evidence
  topic: Definition and primary activity
  outcome: supported
  summary: Natural-compound activity supports the broad native definition. Synthetic
    epimer results are kept separate.
  target_ids:
  - antibioticmech:aro-07e4fbc49d
  evidence_ids:
  - native
  - activity
  - adopted
- assessment_id: provenance
  area: provenance
  topic: Maintained sources and initial hashes
  outcome: supported
  summary: Initial input captures, actual source owners and source history are retained
    without native edits.
  target_ids:
  - antibioticmech:aro-07e4fbc49d
  evidence_ids:
  - owners
- assessment_id: completeness
  area: completeness
  topic: Optional assay, producer and mechanism curation
  outcome: unknown
  summary: Primary data support optional enrichment with exact compound, material,
    calcium and heterologous-host qualifiers. Optional blanks are not defects.
  target_ids:
  - antibioticmech:aro-07e4fbc49d
  evidence_ids:
  - activity
  - discovery
  - mechanism
- assessment_id: schema
  area: schema
  topic: Focused gates and chemical consistency
  outcome: supported
  summary: Focused schema, strict and molecular checks pass.
  target_ids:
  - antibioticmech:aro-07e4fbc49d
  evidence_ids:
  - chemistry
findings:
- finding_id: F1
  issue_key: cadaside-a-qualified-primary-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Add primary activity with calcium and isolated-material qualifications
  description: The2019 discovery and supporting Methods provide exact-compound activity
    beyond the family-level synthesis citation. Optional enrichment must preserve
    ammonium-salt preparation and100mM calcium; A-specific mechanistic evidence and
    an unidentified natural soil producer need separate scope.
  target_ids:
  - antibioticmech:aro-07e4fbc49d
  field_paths:
  - evidence
  - activity_spectrum
  - producer_organisms
  evidence_ids:
  - activity
  - discovery
  - mechanism
  - adopted
  rule_id: 'native-review-checklist: exact material and claim-level evidence'
  native_severity: informational optional enrichment
  normalization_reason: No incorrect quantitative assay, producer or molecular target
    is populated in the native record.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cadaside-a.yaml
    role: Optional curator-owned claim evidence through validated writers/history
actions:
- action_id: A1
  description: Optionally curate the original discovery with exact compound and assay
    boundaries.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-07e4fbc49d
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cadaside-a.yaml
    role: Optional curator-owned claim evidence through validated writers/history
  acceptance_checks:
  - Use compound-specific TableS5 values, preserving strain, medium,100mM calcium,18h/37C,
    visible-growth endpoint, units, replicate count and censoring; verify neutral-parent
    mass basis before conversion.
  - Record S.albus J1074 as a demonstrated heterologous producer, with construct/cluster
    provenance; do not infer the native soil producer, or call E.coli cloning and
    yeast assembly hosts producers.
  - Keep cell-wall and membrane experiments A-specific and phenotype-level. Do not
    create a direct protein target or transfer mechanism to B. Distinguish natural
    compounds from inactive2022 synthetic material.
  - Preserve native2Z/4E geometry and A’s unassigned lipidC8; qualify external ChEBI
    SMILES omissions. Use validated writers and history only during separately authorized
    curation.
limitations:
- The original2019 scientific main text pp1–8, Figure2, relevant SI Methods/structure
  discussion and TablesS3–S5 were inspected. Reference-list pages and every raw NMR/chromatography
  panel were not independently audited.
- The2022 synthesis paper was assessed through its complete original abstract; detailed
  experimental assignments were not retrieved. Later analogue work is not used as
  exact-natural-compound proof.
- Ammonium stoichiometry and free-parent assay mass normalization were not established.
  Native soil producer and a direct molecular target remain unresolved. No exhaustive
  clinical, resistance or transcriptomic survey is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All16 repository input hashes remain unchanged. Native records, inventories, histories
  and curation status were not edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.1021/jacs.8b12087
- https://doi.org/10.1021/jacs.8b12087.s001
- https://doi.org/10.1002/chem.202202554
```
