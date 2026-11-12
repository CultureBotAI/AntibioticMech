# Antibiotic A40926: parent-complex label attached to an N-deacyl structure

- Review: 20261021T090157Z-antibiotic-a40926-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:49:17Z
- Finished UTC: 2026-10-21T09:01:57Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The stored structure is internally consistent N-deacyl-A40926, whereas the ARO label and producer/precursor definition describe the acylated antibiotic complex. A major identity-scope mismatch must be resolved through maintained source ownership. The D-Ala-D-Ala target remains honestly qualified database evidence, not an exact-derivative binding experiment.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position099; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-59d21b914e | data/antibiotics/antibacterial/antibiotic-a40926.yaml | generated | antibiotic A40926 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-59d21b914e | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-59d21b914e | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-59d21b914e | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-59d21b914e | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-59d21b914e | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-59d21b914e | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-59d21b914e | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-59d21b914e | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-59d21b914e | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-59d21b914e | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-59d21b914e | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-59d21b914e | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact parent versus derivative

identity: concern. Targets: antibioticmech:aro-59d21b914e.

The structure and PubChem name identify N-deacyl-A40926, while the native label and biological definition describe the acylated antibiotic complex.

### Encoded chemistry and source mint

identity: supported. Targets: antibioticmech:aro-59d21b914e.

All native chemical fields agree internally; an internally consistent derivative can still be attached to an incompatible concept.

### Producer and precursor wording

evidence: concern. Targets: antibioticmech:aro-59d21b914e.

The cited biosynthetic paper supports parent A40926; exact DA40 provenance cannot be inferred without reconciling identity.

### Acyl-D-Ala-D-Ala target

evidence: supported. Targets: antibioticmech:aro-59d21b914e.

The native cell-wall-component relation is correctly qualified as database assertion. Its exact-derivative experimental applicability remains unverified.

### Glycopeptide class

grounding: supported. Targets: antibioticmech:aro-59d21b914e.

Both the derivative scaffold and parent complex are glycopeptides; the broader class is not the defect.

### Activity, resistance and biosynthesis

completeness: unknown. Targets: antibioticmech:aro-59d21b914e.

No optional quantitative or experimental biological claims are present. Resolve the exact molecule before adding congener, derivative or biosynthetic evidence.

### Structured expression applicability

scope: not_applicable. Targets: antibioticmech:aro-59d21b914e.

The native target is a chemical cell-wall component, with no named gene/protein/regulator or transcriptomic claim. Newly read biosynthetic leads do not constitute native expression assertions.

### Reproducible source repair

ownership: supported. Targets: antibioticmech:aro-59d21b914e.

Captured ARO/PubChem owners and target qualification preserve the provenance of the mismatch.

## Findings

### F1: Resolve the A40926 parent-complex label versus N-deacyl structure

major / open / confirmed; issue key: aro-3000525-a40926-parent-complex-n-deacyl-structure-conflation.

PubChem16133962 and every native chemical field encode N-deacyl-A40926. The label, ARO concept and Nonomuraea producer/precursor definition describe the fatty-acyl antibiotic complex, whose individual factors have different chains. Exact compound identity and the scope of biological claims are therefore inconsistent.

## Recommended Actions And Acceptance Checks

### A1

Choose and reproduce an explicitly evidenced exact chemical entity before reconciling labels, mappings and biological assertions.

- Determine whether this record should represent DA40 or one explicitly identified acylated A40926 factor; the broad natural complex is not one exact structure. Do not choose a PubChem name hit or arbitrary fatty chain without primary structural evidence.
- If retaining DA40, reconcile label/definition and ARO mapping scope, and independently establish which producer/precursor/target claims apply. If representing a factor, verify its exact fatty chain, sugars and stereochemistry and update all structure-derived identifiers consistently.
- Preserve deacyl versus deacetyl versus aglycone distinctions. Microbial transformation does not automatically establish a de novo producer, and derivative antibacterial assays do not establish unmodified DA40 potency.
- Correct maintained ARO/PubChem source inputs or explicit curation decisions, regenerate through the seeder, preserve historical provenance and use validated writer/history for any later curator fields. Re-run chemistry, native schema/strict and required corpus gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/antibiotic-a40926.yaml; Entire native YAML and four seed/reseed history entries | supports | SEEDED/MINTED neutral C71H66Cl2N8O28 with eighteen assigned tetrahedral centers, ARO3000525, ChEMBL1142788 and PubChem16133962 mappings. Definition cites PMID12837387. One acyl-D-alanyl-D-alanine target is CELL_WALL_COMPONENT/ATTACKED_COMPONENT and DATABASE_ASSERTION_ONLY; no quantitative activity, producer object, resistance or primary target evidence is asserted. |
| owner | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; data/raw/aro_target_edges.tsv; 099-raw.json and maintained extractor/seeder/target qualification | supports | ARO supplies the broad label, Nonomuraea producer/precursor definition, glycopeptide class and chemical mappings. PubChem supplies the exact N-deacyl structure; the adopted target edge supplies ARO3000720. Both adopted molecule PMIDs12837387 and15664522 were resolved. Exact-row checks found no ARO resistance edge or ChEBI identity row. All eighteen captured maintained hashes remain unchanged. |
| chemistry | Independent RDKit calculation; 099-chemistry.json; focus009-root.py99 | supports | Native SMILES and InChI agree on full key VZDDQLYACFXSQP-KBQMXOHMSA-N, formula, neutral charge, one fragment and eighteen assigned centers. Average1550.243 rounds to native1550.2; exact1548.336358832 agrees. The source-specific mint reproduces. These checks establish internal consistency, not identity with the acylated antibiotic complex. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/16133962; 099-pubchem.json and099-pubchem-synonyms.json | refutes | The exact CID has the native full key and formula and explicitly names N-Deacyl-A40926, DA40 and DA40926. The structure contains a free amino sugar and lacks the N-linked fatty-acyl chain of A40926 congeners. This is positive evidence of a derivative/parent mismatch, not a mass rounding error. |
| aro | https://card.mcmaster.ca/ontology/36664; 099-card.html; official094-aro.obo exact ARO3000525 and3000720 terms | partial | Current official CARD repeats the parent-antibiotic definition, both adopted citations and the same chemical references. The official ontology explicitly links acyl-D-alanyl-D-alanine to A40926. Thus the source itself carries the chemical-scope conflation; database agreement does not resolve it. |
| biosynthesis | PMID:12837387; DOI:10.1016/S1074-5521(03)00120-0; complete EuropePMC abstract in099-adopted.json | partial | The2003 primary identifies37 open reading frames in the Nonomuraea ATCC39727 A40926 cluster and an engineered dbv8–10 deletion yielding dechloromannosyl A40926 aglycone. This is biosynthetic-cluster evidence for the parent antibiotic and a different engineered intermediate; it does not prove that the native DA40 structure is the ordinary fermentation product. |
| acyltransferase | PMID:15664522; DOI:10.1016/j.chembiol.2004.12.005; complete EuropePMC abstract | context_only | The2005 primary studies glycopeptide acyltransferases and regiospecific N-acylation of amino-sugar scaffolds. It supports the importance of the acylated scaffold and synthetic transformations, not direct binding of this exact N-deacyl derivative to its antibacterial target. Biosynthetic enzymes must not be imported as drug targets. |
| congeners | PMID:1504339; DOI:10.1002/rcm.1290060208; complete EuropePMC abstract in099-extra.json | refutes | Original mass-spectrometric characterization distinguishes fatty acids across A40926 factors: A n-undecanoic, B10-methylundecanoic, A1 9-methyldecanoic, B1 n-dodecanoic, RS1 8-methylnonanoic, RS2 n-decanoic and RS3 n-tridecanoic. A broad A40926 name therefore does not select one exact N-acyl congener, much less the N-deacyl structure. |
| deacyl | PMID:15993054; DOI:10.1016/j.bmcl.2005.05.076; complete EuropePMC abstract; public publisher preview | refutes | The2005 primary explicitly obtains deacyl A40926 by microbial transformation of A40926 with Actinoplanes teichomyceticus ATCC31121, then makes alkyl/carboxylamide derivatives for antibacterial testing. This distinguishes DA40 from the parent. Transformation is not evidence that this strain biosynthesizes A40926 de novo; derivative activity must not automatically be assigned to unmodified DA40. |
| later | PMID:30830742; PMID:18559264; DOI:10.1021/acschembio.9b00050 and10.1016/j.chembiol.2008.05.009; complete abstracts | context_only | The2019 study describes Nonomuraea-produced A40926 as fatty-acyl congeners and uses a dbv23/dbv8 mutant to obtain intermediates for later chemical acylation. The2008 deacetylase study distinguishes sugar deacetylation from long-chain N-acylation. Do not conflate deacyl, deacetyl and aglycone intermediates or use biosynthetic enzyme structures as antimicrobial-target structures. |
| search | CultureBotAI/AntibioticMech; 099-local-hits.txt and099100-maintained-hits.txt; exact current database and primary queries | context_only | Ignored-inclusive maintained search identifies ARO/PubChem source and queue context but no target-specific curation overlay within the stated scope. The exact ChEMBL1142788 API request returned404; no independent current ChEMBL structure was verified. Both adopted references were dispositioned, and free primary abstracts establish the parent/derivative distinction. |

## Limits And Additional Notes

- Both adopted and four selected follow-up primary abstracts were read completely. Publisher previews supplied limited additional context; full2003/2005 papers were unavailable through attempted public DOI/Cell/ScienceDirect routes. No full synthetic scheme, supplemental chemistry or quantitative derivative table was independently audited.
- The exact ChEMBL API request returned404; this is an access/endpoint observation, not proof that the identifier does not exist. PubChem exact structure and positive primary parent/derivative distinctions establish the finding independently.
- No exact N-deacyl target-binding experiment, clinical approval, clinical susceptibility breakpoint or genome-linked producer claim is established here.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T090157Z-antibiotic-a40926-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Antibiotic A40926: parent-complex label attached to an N-deacyl structure'
started_at: '2026-10-21T08:49:17Z'
finished_at: '2026-10-21T09:01:57Z'
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
summary: The stored structure is internally consistent N-deacyl-A40926, whereas the
  ARO label and producer/precursor definition describe the acylated antibiotic complex.
  A major identity-scope mismatch must be resolved through maintained source ownership.
  The D-Ala-D-Ala target remains honestly qualified database evidence, not an exact-derivative
  binding experiment.
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
  - path: data/antibiotics/antibacterial/antibiotic-a40926.yaml
    sha256: 79f4f6afd312ace34c53e7e828db2de1eb91a0a7fa47da3fe7f3c32c7bd53c4f
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
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
targets:
- target_id: antibioticmech:aro-59d21b914e
  path: data/antibiotics/antibacterial/antibiotic-a40926.yaml
  label: antibiotic A40926
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition and identity links
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Qualified target component edge
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted chemical structure
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Reviewed target qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source fields
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decision
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position099; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-59d21b914e
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-59d21b914e
  command: .venv/bin/python /private/tmp/am-review-session/focus009-root.py 99
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-59d21b914e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/antibiotic-a40926.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-59d21b914e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/antibiotic-a40926.yaml --out /private/tmp/am-review-session/099-strict.tsv
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
  - antibioticmech:aro-59d21b914e
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
  - antibioticmech:aro-59d21b914e
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
  - antibioticmech:aro-59d21b914e
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
  - antibioticmech:aro-59d21b914e
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
  - antibioticmech:aro-59d21b914e
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
  - antibioticmech:aro-59d21b914e
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
  - antibioticmech:aro-59d21b914e
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
  - antibioticmech:aro-59d21b914e
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
  - antibioticmech:aro-59d21b914e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/antibiotic-a40926.yaml
  locator: Entire native YAML and four seed/reseed history entries
  accessed_at: '2026-10-21T08:57:52Z'
  support: supports
  summary: SEEDED/MINTED neutral C71H66Cl2N8O28 with eighteen assigned tetrahedral
    centers, ARO3000525, ChEMBL1142788 and PubChem16133962 mappings. Definition cites
    PMID12837387. One acyl-D-alanyl-D-alanine target is CELL_WALL_COMPONENT/ATTACKED_COMPONENT
    and DATABASE_ASSERTION_ONLY; no quantitative activity, producer object, resistance
    or primary target evidence is asserted.
- evidence_id: owner
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; data/raw/aro_target_edges.tsv
  locator: 099-raw.json and maintained extractor/seeder/target qualification
  accessed_at: '2026-10-21T08:57:52Z'
  support: supports
  summary: ARO supplies the broad label, Nonomuraea producer/precursor definition,
    glycopeptide class and chemical mappings. PubChem supplies the exact N-deacyl
    structure; the adopted target edge supplies ARO3000720. Both adopted molecule
    PMIDs12837387 and15664522 were resolved. Exact-row checks found no ARO resistance
    edge or ChEBI identity row. All eighteen captured maintained hashes remain unchanged.
  snapshot_sha256: 34fc9c29aaba803667d6c55c98da19157495cb7a92af6a599bd7a78ccdfe03bf
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculation
  locator: 099-chemistry.json; focus009-root.py99
  accessed_at: '2026-10-21T08:57:52Z'
  support: supports
  summary: Native SMILES and InChI agree on full key VZDDQLYACFXSQP-KBQMXOHMSA-N,
    formula, neutral charge, one fragment and eighteen assigned centers. Average1550.243
    rounds to native1550.2; exact1548.336358832 agrees. The source-specific mint reproduces.
    These checks establish internal consistency, not identity with the acylated antibiotic
    complex.
  snapshot_sha256: ec85e9a68b6f4acedbf3ad0a1f0a49ee2feaf14cd790f6362c86adb020f91ca3
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/16133962
  locator: 099-pubchem.json and099-pubchem-synonyms.json
  accessed_at: '2026-10-21T08:57:52Z'
  support: refutes
  summary: The exact CID has the native full key and formula and explicitly names
    N-Deacyl-A40926, DA40 and DA40926. The structure contains a free amino sugar and
    lacks the N-linked fatty-acyl chain of A40926 congeners. This is positive evidence
    of a derivative/parent mismatch, not a mass rounding error.
  snapshot_sha256: 7764bc9b2e6ceb57f438904e42ed8cdc14a934dc3e5a2447c213ccd7479bbede
- evidence_id: aro
  kind: database
  reference: https://card.mcmaster.ca/ontology/36664
  locator: 099-card.html; official094-aro.obo exact ARO3000525 and3000720 terms
  accessed_at: '2026-10-21T08:57:52Z'
  support: partial
  summary: Current official CARD repeats the parent-antibiotic definition, both adopted
    citations and the same chemical references. The official ontology explicitly links
    acyl-D-alanyl-D-alanine to A40926. Thus the source itself carries the chemical-scope
    conflation; database agreement does not resolve it.
  snapshot_sha256: f61a805aff689eaaf1b8954a4d13b15ef14ce6cd169aa20863d40e55e2144a82
- evidence_id: biosynthesis
  kind: primary_source
  reference: PMID:12837387
  locator: DOI:10.1016/S1074-5521(03)00120-0; complete EuropePMC abstract in099-adopted.json
  accessed_at: '2026-10-21T08:57:52Z'
  support: partial
  summary: The2003 primary identifies37 open reading frames in the Nonomuraea ATCC39727
    A40926 cluster and an engineered dbv8–10 deletion yielding dechloromannosyl A40926
    aglycone. This is biosynthetic-cluster evidence for the parent antibiotic and
    a different engineered intermediate; it does not prove that the native DA40 structure
    is the ordinary fermentation product.
  snapshot_sha256: ffd148241c2509f5013fe7f72e59e5fa5b1a030bad9e8516be56c22c6b26c409
- evidence_id: acyltransferase
  kind: primary_source
  reference: PMID:15664522
  locator: DOI:10.1016/j.chembiol.2004.12.005; complete EuropePMC abstract
  accessed_at: '2026-10-21T08:57:52Z'
  support: context_only
  summary: The2005 primary studies glycopeptide acyltransferases and regiospecific
    N-acylation of amino-sugar scaffolds. It supports the importance of the acylated
    scaffold and synthetic transformations, not direct binding of this exact N-deacyl
    derivative to its antibacterial target. Biosynthetic enzymes must not be imported
    as drug targets.
- evidence_id: congeners
  kind: primary_source
  reference: PMID:1504339
  locator: DOI:10.1002/rcm.1290060208; complete EuropePMC abstract in099-extra.json
  accessed_at: '2026-10-21T08:57:52Z'
  support: refutes
  summary: 'Original mass-spectrometric characterization distinguishes fatty acids
    across A40926 factors: A n-undecanoic, B10-methylundecanoic, A1 9-methyldecanoic,
    B1 n-dodecanoic, RS1 8-methylnonanoic, RS2 n-decanoic and RS3 n-tridecanoic. A
    broad A40926 name therefore does not select one exact N-acyl congener, much less
    the N-deacyl structure.'
  snapshot_sha256: 158ef2e1df7a1b230fb1065179ce154680ca85d13b616be73dc110e5b9d7bdfa
- evidence_id: deacyl
  kind: primary_source
  reference: PMID:15993054
  locator: DOI:10.1016/j.bmcl.2005.05.076; complete EuropePMC abstract; public publisher
    preview
  accessed_at: '2026-10-21T08:57:52Z'
  support: refutes
  summary: The2005 primary explicitly obtains deacyl A40926 by microbial transformation
    of A40926 with Actinoplanes teichomyceticus ATCC31121, then makes alkyl/carboxylamide
    derivatives for antibacterial testing. This distinguishes DA40 from the parent.
    Transformation is not evidence that this strain biosynthesizes A40926 de novo;
    derivative activity must not automatically be assigned to unmodified DA40.
- evidence_id: later
  kind: primary_source
  reference: PMID:30830742; PMID:18559264
  locator: DOI:10.1021/acschembio.9b00050 and10.1016/j.chembiol.2008.05.009; complete
    abstracts
  accessed_at: '2026-10-21T08:57:52Z'
  support: context_only
  summary: The2019 study describes Nonomuraea-produced A40926 as fatty-acyl congeners
    and uses a dbv23/dbv8 mutant to obtain intermediates for later chemical acylation.
    The2008 deacetylase study distinguishes sugar deacetylation from long-chain N-acylation.
    Do not conflate deacyl, deacetyl and aglycone intermediates or use biosynthetic
    enzyme structures as antimicrobial-target structures.
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 099-local-hits.txt and099100-maintained-hits.txt; exact current database
    and primary queries
  accessed_at: '2026-10-21T08:57:52Z'
  support: context_only
  summary: Ignored-inclusive maintained search identifies ARO/PubChem source and queue
    context but no target-specific curation overlay within the stated scope. The exact
    ChEMBL1142788 API request returned404; no independent current ChEMBL structure
    was verified. Both adopted references were dispositioned, and free primary abstracts
    establish the parent/derivative distinction.
  search_scope: rg --no-ignore --hidden in isolated batch010 excluding.git/.venv;
    narrower maintained curation/conf/scripts/data/raw/reviews follow-up excludes
    large.obo/.jsonl/.html files. CARD, PubChem, ChEMBL, EuropePMC and original publisher
    pages; no paid sources.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact parent versus derivative
  outcome: concern
  summary: The structure and PubChem name identify N-deacyl-A40926, while the native
    label and biological definition describe the acylated antibiotic complex.
  target_ids:
  - antibioticmech:aro-59d21b914e
  evidence_ids:
  - native
  - pubchem
  - congeners
  - deacyl
- assessment_id: internal
  area: identity
  topic: Encoded chemistry and source mint
  outcome: supported
  summary: All native chemical fields agree internally; an internally consistent derivative
    can still be attached to an incompatible concept.
  target_ids:
  - antibioticmech:aro-59d21b914e
  evidence_ids:
  - chemistry
  - owner
- assessment_id: definition
  area: evidence
  topic: Producer and precursor wording
  outcome: concern
  summary: The cited biosynthetic paper supports parent A40926; exact DA40 provenance
    cannot be inferred without reconciling identity.
  target_ids:
  - antibioticmech:aro-59d21b914e
  evidence_ids:
  - biosynthesis
  - deacyl
  - later
- assessment_id: target
  area: evidence
  topic: Acyl-D-Ala-D-Ala target
  outcome: supported
  summary: The native cell-wall-component relation is correctly qualified as database
    assertion. Its exact-derivative experimental applicability remains unverified.
  target_ids:
  - antibioticmech:aro-59d21b914e
  evidence_ids:
  - native
  - aro
  - acyltransferase
- assessment_id: class
  area: grounding
  topic: Glycopeptide class
  outcome: supported
  summary: Both the derivative scaffold and parent complex are glycopeptides; the
    broader class is not the defect.
  target_ids:
  - antibioticmech:aro-59d21b914e
  evidence_ids:
  - chemistry
  - aro
- assessment_id: optional
  area: completeness
  topic: Activity, resistance and biosynthesis
  outcome: unknown
  summary: No optional quantitative or experimental biological claims are present.
    Resolve the exact molecule before adding congener, derivative or biosynthetic
    evidence.
  target_ids:
  - antibioticmech:aro-59d21b914e
  evidence_ids:
  - native
  - congeners
  - deacyl
  - later
- assessment_id: adapter
  area: scope
  topic: Structured expression applicability
  outcome: not_applicable
  summary: The native target is a chemical cell-wall component, with no named gene/protein/regulator
    or transcriptomic claim. Newly read biosynthetic leads do not constitute native
    expression assertions.
  target_ids:
  - antibioticmech:aro-59d21b914e
  evidence_ids:
  - native
- assessment_id: ownership
  area: ownership
  topic: Reproducible source repair
  outcome: supported
  summary: Captured ARO/PubChem owners and target qualification preserve the provenance
    of the mismatch.
  target_ids:
  - antibioticmech:aro-59d21b914e
  evidence_ids:
  - owner
  - search
findings:
- finding_id: F1
  issue_key: aro-3000525-a40926-parent-complex-n-deacyl-structure-conflation
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Resolve the A40926 parent-complex label versus N-deacyl structure
  description: PubChem16133962 and every native chemical field encode N-deacyl-A40926.
    The label, ARO concept and Nonomuraea producer/precursor definition describe the
    fatty-acyl antibiotic complex, whose individual factors have different chains.
    Exact compound identity and the scope of biological claims are therefore inconsistent.
  target_ids:
  - antibioticmech:aro-59d21b914e
  field_paths:
  - label
  - definition
  - definition_source
  - chemical_structure
  - xrefs
  - source_concepts
  - molecular_targets
  evidence_ids:
  - native
  - pubchem
  - congeners
  - deacyl
  - biosynthesis
  - aro
  rule_id: 'native-review-checklist: exact chemical identity and evidence scope'
  native_severity: major parent/derivative identity conflation
  normalization_reason: The glycopeptide family is recognizable and chemistry parses,
    but parent and N-deacyl derivative are distinct exact molecules. This is more
    than a synonym or rounding issue.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition and identity links
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Qualified target component edge
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted chemical structure
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Reviewed target qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source fields
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decision
actions:
- action_id: A1
  description: Choose and reproduce an explicitly evidenced exact chemical entity
    before reconciling labels, mappings and biological assertions.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-59d21b914e
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition and identity links
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Qualified target component edge
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted chemical structure
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Reviewed target qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source fields
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decision
  acceptance_checks:
  - Determine whether this record should represent DA40 or one explicitly identified
    acylated A40926 factor; the broad natural complex is not one exact structure.
    Do not choose a PubChem name hit or arbitrary fatty chain without primary structural
    evidence.
  - If retaining DA40, reconcile label/definition and ARO mapping scope, and independently
    establish which producer/precursor/target claims apply. If representing a factor,
    verify its exact fatty chain, sugars and stereochemistry and update all structure-derived
    identifiers consistently.
  - Preserve deacyl versus deacetyl versus aglycone distinctions. Microbial transformation
    does not automatically establish a de novo producer, and derivative antibacterial
    assays do not establish unmodified DA40 potency.
  - Correct maintained ARO/PubChem source inputs or explicit curation decisions, regenerate
    through the seeder, preserve historical provenance and use validated writer/history
    for any later curator fields. Re-run chemistry, native schema/strict and required
    corpus gates.
limitations:
- Both adopted and four selected follow-up primary abstracts were read completely.
  Publisher previews supplied limited additional context; full2003/2005 papers were
  unavailable through attempted public DOI/Cell/ScienceDirect routes. No full synthetic
  scheme, supplemental chemistry or quantitative derivative table was independently
  audited.
- The exact ChEMBL API request returned404; this is an access/endpoint observation,
  not proof that the identifier does not exist. PubChem exact structure and positive
  primary parent/derivative distinctions establish the finding independently.
- No exact N-deacyl target-binding experiment, clinical approval, clinical susceptibility
  breakpoint or genome-linked producer claim is established here.
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
