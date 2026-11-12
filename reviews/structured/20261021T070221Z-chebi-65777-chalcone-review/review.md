# Review of CHEBI:65777 (benzylated methoxychalcone)

- Review: 20261021T070221Z-chebi-65777-chalcone-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T06:53:17Z
- Finished UTC: 2026-10-21T07:02:21Z
- Reviewer: Codex agent review002 (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Official identity, substituent pattern and E geometry agree with the source record and independent calculation. The cited primary abstract supports plant isolation, antimycobacterial activity, antiplasmodial activity and cancer-cell cytotoxicity. Per-record validators pass. Mechanism and full assay context remain unresolved; optional evidence enrichment requires caution with the abstract MIC unit. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire one-record content, maintained inventory/configuration and code, official identities/roles, primary publication abstract and bounded free full-text discovery.

Selection: Path-ordered unreviewed queue index 013.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65777 | data/antibiotics/antibacterial/2-4-dihydroxy-3-2-hydroxy-benzyl-6-methoxy-chalcone.yaml | generated | 2',4'-dihydroxy-3'-(2-hydroxy benzyl)-6'-methoxy chalcone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record LinkML validation | passed | True | CHEBI:65777 | Exit 0; No issues found. |
| Documented per-record closed-schema validation | passed | True | CHEBI:65777 | Exit 0; one file scanned; zero ERROR rows. |
| Independent RDKit structure and internal identifier consistency | passed | False | CHEBI:65777 | Both encodings reproduce key, formula, charge and masses; one E double bond, no tetrahedral stereocenters and one fragment; minted ID reproduced. |
| Structured expression-module adapter applicability | not_applicable | False | CHEBI:65777 | No named gene, protein, regulator, pathway, stress response or expression dataset is asserted. iModulonDB is not applicable and this does not supply negative evidence. |
| Authoritative full QC | failed | True | CHEBI:65777 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65777 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65777 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65777 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65777 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65777 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65777 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65777 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65777 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact compound and geometry

identity: supported. Targets: CHEBI:65777.

The specific benzylated E-chalcone agrees across official identity and source paper. No hydrogenated dihydrochalcone, positional isomer or extract is substituted.

### Broad parent classes and registry

grounding: supported. Targets: CHEBI:65777.

Both parents are broader and structurally appropriate. Reaxys matches the official entry but the registry itself was not independently accessed.

### Activities and filing

evidence: supported. Targets: CHEBI:65777.

Primary text supports the source activities, including antimycobacterial testing. Filing correctly follows the retained ontology roles; it does not need automatic refiling from one assay organism. Antineoplastic wording is limited to cancer-cell cytotoxicity.

### Aerial-part isolation

provenance: supported. Targets: CHEBI:65777.

The paper explicitly names the compound and plant part. No biosynthetic pathway or independently proven producer taxon object is inferred.

### Molecular mode and target

completeness: unknown. Targets: CHEBI:65777.

No exact antimicrobial mechanism is established by inspected text. Family mechanisms, mixed-extract ROS results and computational predictions cannot fill this gap. Native REVIEWED criteria remain unmet.

### Assays, resistance, clinical status and graphs

representation: not_applicable. Targets: CHEBI:65777.

Optional objects are absent without a schema error. The source MIC unit and unavailable assay context must be resolved before adding a quantitative observation. No resistance or clinical claim is implied.

### Source and history

ownership: supported. Targets: CHEBI:65777.

SEEDED status and three events accurately preserve generation provenance; source fields and curator additions have distinct maintained ownership.

### Validation and structure

schema: supported. Targets: CHEBI:65777.

Both per-record validators and independent structure calculations pass.

## Findings

### F1: Primary evidence and assay context remain an optional curation follow-up

informational / open / confirmed; issue key: chebi-65777-primary-assay-enrichment.

Existing identity and activity assertions are supported. No structured evidence or activity observation is present; full methods and literal MIC-unit verification are needed before safe enrichment. The missing optional slots are not an error.

## Recommended Actions And Acceptance Checks

### A1

During separately authorized curation, attach exact-compound primary evidence and inspect the full paper before encoding assays. Verify the tuberculosis MIC unit directly against methods/table text; preserve any unresolved discrepancy. Leave mechanism unresolved absent an exact-compound experiment.

- Each observation retains exact compound, organism/strain, method, value and units from inspected primary text.
- Do not silently replace the abstract mg/mL unit with micrograms or transfer results from dihydrochalcones, plant extracts or computational models.
- Use the native validated writer and curation event; pass just validate, just validate-strict, just verify-corpus --summary and just qc before native promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/2-4-dihydroxy-3-2-hydroxy-benzyl-6-methoxy-chalcone.yaml; Every field of generated AntibioticRecord | supports | Read definition, systematic synonym, two parents, two roles, structure, Reaxys reference, source concept and all three seed/reseed events. No mechanism, target, MIC, resistance, structured producer, clinical, causal-graph or dataset assertion is present. |
| inventory | data/raw/chebi_antimicrobials.tsv; Complete CHEBI:65777 row and header | supports | The in-scope 3-star source row carries matching seeded data and PMID:16833018 as its single citation lead; mechanism-role column is empty. Inclusive maintained-table searches found no override. |
| ownership | scripts/seed_from_sources.py; mint, structure_from_chebi, classification priority and build_record; scripts/extract_source_inventory.py ChEBI rows; conf/sources.yaml; MANIFEST | supports | Source fields and reviewed antimicrobial roles are emitted reproducibly; ANTIBACTERIAL has priority over ANTIPROTOZOAL. The extractor deliberately retains citation leads without assuming claim-level support. Source version agrees with retrieval metadata. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:65777; Official full entry, including structure, IUPAC name, ontology and registry; reached from antimalarial role | supports | Official exact structure, synonym, formula, masses and charge agree. Both retained roles, both broader parents, Reaxys 4564762 and trans-chalcone relationship are corroborated. Isolation and activity wording match; the antineoplastic role lies outside the antimicrobial role subset. |
| parent-chalcones | https://www.ebi.ac.uk/chebi/CHEBI:23086; Definition and ontology | supports | The parent denotes chalcones, the broader substituted diaryl enone class. |
| parent-resorcinols | https://www.ebi.ac.uk/chebi/CHEBI:33572; Definition | supports | The parent denotes benzenediols with meta-related hydroxyl groups, matching the 2-prime/4-prime substitution pattern. |
| role-antibacterial | https://www.ebi.ac.uk/chebi/CHEBI:33282; Definition | supports | The role identifier denotes antibacterial agent. |
| role-antimalarial | https://www.ebi.ac.uk/chebi/CHEBI:38068; Definition and incoming CHEBI:65777 edge | supports | The role identifier denotes antimalarial and explicitly lists the compound; retained source role does not imply clinical approval. |
| primary | PMID:16833018; PubMed abstract and metadata; DOI:10.1007/BF02969423; publisher abstract at https://link.springer.com/article/10.1007/BF02969423 | supports | The primary abstract names exact compound 2, aerial-part isolation from Ellipeiopsis cherrevensis, M. tuberculosis growth inhibition, P. falciparum inhibition and cytotoxicity in three human cancer-cell lines. It reports the tuberculosis MIC as 25 mg/mL; that literal unit is not silently corrected or imported. Full methods and tables were unavailable. |
| chemistry | RDKit and hashlib calculation; /private/tmp/am-review-session/013-chemistry.py; 013-structure.json | supports | SMILES and InChI yield IVKGLRZLTNXWKF-VAWYXSNFSA-N; C23H20O5; charge 0; average mass 376.408; exact mass 376.13107374; E geometry; one fragment. Minted ID antibioticmech:chebi-2cc7bf5201 agrees. |
| validation | just validate; just validate-strict; /private/tmp/am-review-session/013-validate.log; 013-strict.log; 013-strict.tsv | supports | Both documented per-record gates exited 0; strict found zero ERROR rows. |
| search | Inclusive repository and bounded free literature retrieval; /private/tmp/am-review-session/013-local-hits.txt; 013-owner-search.txt; free web search on review date | context_only | No matching maintained decision/curator override was found. Exact name/key and paper-title searches were used; related dihydrochalcones, plant extracts and computational predictions were not treated as exact experimental mechanism evidence. |

## Limits And Additional Notes

- Only the primary abstract was inspected, corroborated on PubMed and the publisher. Full methods/tables were inaccessible through the bounded free search.
- The abstract literally reports 25 mg/mL for the tuberculosis MIC. No numerical observation is in the record, and this review does not silently correct the source unit.
- Reaxys itself was not accessed; the cross-reference is corroborated by official ChEBI.
- No exact experimental antimicrobial mechanism was established in the bounded search; this is not an exhaustive absence claim.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No source record, maintained input, generated product or history event was modified. Review performed in /private/tmp/antibioticmech-record-reviews-002.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T070221Z-chebi-65777-chalcone-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of CHEBI:65777 (benzylated methoxychalcone)
started_at: '2026-10-21T06:53:17Z'
finished_at: '2026-10-21T07:02:21Z'
reviewer:
  identity: Codex agent review002
  kind: agent
  independence: independent
  independence_basis: Read-only review in a task-owned worktree, by an agent uninvolved
    in authoring the record; exact input hashes were captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: SEEDED exact structure and activity supported; mechanism unresolved
scientific_review: true
summary: Official identity, substituent pattern and E geometry agree with the source
  record and independent calculation. The cited primary abstract supports plant isolation,
  antimycobacterial activity, antiplasmodial activity and cancer-cell cytotoxicity.
  Per-record validators pass. Mechanism and full assay context remain unresolved;
  optional evidence enrichment requires caution with the abstract MIC unit. Scientific
  assessment retains the stated evidence limits; full verification is blocked by the
  shared native-library failure.
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
  - path: data/antibiotics/antibacterial/2-4-dihydroxy-3-2-hydroxy-benzyl-6-methoxy-chalcone.yaml
    sha256: 96a1698cdb948d3ab9254e6f8bb290af2ad45109154e3d6bb555d42c6f023021
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
scope:
  description: Entire one-record content, maintained inventory/configuration and code,
    official identities/roles, primary publication abstract and bounded free full-text
    discovery.
  selection: Path-ordered unreviewed queue index 013.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65777
targets:
- target_id: CHEBI:65777
  path: data/antibiotics/antibacterial/2-4-dihydroxy-3-2-hydroxy-benzyl-6-methoxy-chalcone.yaml
  label: 2',4'-dihydroxy-3'-(2-hydroxy benzyl)-6'-methoxy chalcone
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
  name: Documented per-record LinkML validation
  status: passed
  required: true
  summary: Exit 0; No issues found.
  target_ids:
  - CHEBI:65777
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/2-4-dihydroxy-3-2-hydroxy-benzyl-6-methoxy-chalcone.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented per-record closed-schema validation
  status: passed
  required: true
  summary: Exit 0; one file scanned; zero ERROR rows.
  target_ids:
  - CHEBI:65777
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/2-4-dihydroxy-3-2-hydroxy-benzyl-6-methoxy-chalcone.yaml
    --out /private/tmp/am-review-session/013-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Independent RDKit structure and internal identifier consistency
  status: passed
  required: false
  summary: Both encodings reproduce key, formula, charge and masses; one E double
    bond, no tetrahedral stereocenters and one fragment; minted ID reproduced.
  target_ids:
  - CHEBI:65777
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/013-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: imodulondb
  name: Structured expression-module adapter applicability
  status: not_applicable
  required: false
  summary: No named gene, protein, regulator, pathway, stress response or expression
    dataset is asserted. iModulonDB is not applicable and this does not supply negative
    evidence.
  target_ids:
  - CHEBI:65777
  evidence_ids:
  - record
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:65777
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
  - CHEBI:65777
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
  - CHEBI:65777
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
  - CHEBI:65777
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
  - CHEBI:65777
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
  - CHEBI:65777
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
  - CHEBI:65777
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
  - CHEBI:65777
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
  - CHEBI:65777
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/2-4-dihydroxy-3-2-hydroxy-benzyl-6-methoxy-chalcone.yaml
  locator: Every field of generated AntibioticRecord
  accessed_at: '2026-10-21T06:54:58Z'
  support: supports
  summary: Read definition, systematic synonym, two parents, two roles, structure,
    Reaxys reference, source concept and all three seed/reseed events. No mechanism,
    target, MIC, resistance, structured producer, clinical, causal-graph or dataset
    assertion is present.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Complete CHEBI:65777 row and header
  accessed_at: '2026-10-21T06:54:58Z'
  support: supports
  summary: The in-scope 3-star source row carries matching seeded data and PMID:16833018
    as its single citation lead; mechanism-role column is empty. Inclusive maintained-table
    searches found no override.
- evidence_id: ownership
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: mint, structure_from_chebi, classification priority and build_record; scripts/extract_source_inventory.py
    ChEBI rows; conf/sources.yaml; MANIFEST
  accessed_at: '2026-10-21T06:54:58Z'
  support: supports
  summary: Source fields and reviewed antimicrobial roles are emitted reproducibly;
    ANTIBACTERIAL has priority over ANTIPROTOZOAL. The extractor deliberately retains
    citation leads without assuming claim-level support. Source version agrees with
    retrieval metadata.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:65777
  locator: Official full entry, including structure, IUPAC name, ontology and registry;
    reached from antimalarial role
  accessed_at: '2026-10-21T06:54:58Z'
  support: supports
  summary: Official exact structure, synonym, formula, masses and charge agree. Both
    retained roles, both broader parents, Reaxys 4564762 and trans-chalcone relationship
    are corroborated. Isolation and activity wording match; the antineoplastic role
    lies outside the antimicrobial role subset.
- evidence_id: parent-chalcones
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:23086
  locator: Definition and ontology
  accessed_at: '2026-10-21T06:54:58Z'
  support: supports
  summary: The parent denotes chalcones, the broader substituted diaryl enone class.
- evidence_id: parent-resorcinols
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:33572
  locator: Definition
  accessed_at: '2026-10-21T06:54:58Z'
  support: supports
  summary: The parent denotes benzenediols with meta-related hydroxyl groups, matching
    the 2-prime/4-prime substitution pattern.
- evidence_id: role-antibacterial
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:33282
  locator: Definition
  accessed_at: '2026-10-21T06:54:58Z'
  support: supports
  summary: The role identifier denotes antibacterial agent.
- evidence_id: role-antimalarial
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:38068
  locator: Definition and incoming CHEBI:65777 edge
  accessed_at: '2026-10-21T06:54:58Z'
  support: supports
  summary: The role identifier denotes antimalarial and explicitly lists the compound;
    retained source role does not imply clinical approval.
- evidence_id: primary
  kind: primary_source
  reference: PMID:16833018
  locator: PubMed abstract and metadata; DOI:10.1007/BF02969423; publisher abstract
    at https://link.springer.com/article/10.1007/BF02969423
  accessed_at: '2026-10-21T06:54:58Z'
  support: supports
  summary: The primary abstract names exact compound 2, aerial-part isolation from
    Ellipeiopsis cherrevensis, M. tuberculosis growth inhibition, P. falciparum inhibition
    and cytotoxicity in three human cancer-cell lines. It reports the tuberculosis
    MIC as 25 mg/mL; that literal unit is not silently corrected or imported. Full
    methods and tables were unavailable.
- evidence_id: chemistry
  kind: validation
  reference: RDKit and hashlib calculation
  locator: /private/tmp/am-review-session/013-chemistry.py; 013-structure.json
  accessed_at: '2026-10-21T06:54:58Z'
  support: supports
  summary: SMILES and InChI yield IVKGLRZLTNXWKF-VAWYXSNFSA-N; C23H20O5; charge 0;
    average mass 376.408; exact mass 376.13107374; E geometry; one fragment. Minted
    ID antibioticmech:chebi-2cc7bf5201 agrees.
  snapshot_sha256: a1c001f742c00b8c74637f44a9ef8590e3d6b4eff40597b687ba1194bc666cc0
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: /private/tmp/am-review-session/013-validate.log; 013-strict.log; 013-strict.tsv
  accessed_at: '2026-10-21T06:54:58Z'
  support: supports
  summary: Both documented per-record gates exited 0; strict found zero ERROR rows.
- evidence_id: search
  kind: search
  reference: Inclusive repository and bounded free literature retrieval
  locator: /private/tmp/am-review-session/013-local-hits.txt; 013-owner-search.txt;
    free web search on review date
  accessed_at: '2026-10-21T06:54:58Z'
  support: context_only
  summary: No matching maintained decision/curator override was found. Exact name/key
    and paper-title searches were used; related dihydrochalcones, plant extracts and
    computational predictions were not treated as exact experimental mechanism evidence.
  search_scope: prepare.py 13 ran rg --no-ignore --hidden -l -F for CHEBI:65777, exact
    label and slug across the worktree including ignored/hidden files, excluding only
    .git and .venv; maintained tables also searched by minted ID. Free web queries
    included exact label plus antibacterial, IVKGLRZLTNXWKF plus mechanism, exact
    primary title plus PDF, and author/chalcone/MIC queries. Official ChEBI, PubMed
    and Springer abstracts inspected. Springer full text was subscription-only; ResearchGate
    explicitly had no full text available. No contact or purchase occurred.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact compound and geometry
  outcome: supported
  summary: The specific benzylated E-chalcone agrees across official identity and
    source paper. No hydrogenated dihydrochalcone, positional isomer or extract is
    substituted.
  target_ids:
  - CHEBI:65777
  evidence_ids:
  - record
  - inventory
  - chebi
  - chemistry
  - primary
- assessment_id: grounding
  area: grounding
  topic: Broad parent classes and registry
  outcome: supported
  summary: Both parents are broader and structurally appropriate. Reaxys matches the
    official entry but the registry itself was not independently accessed.
  target_ids:
  - CHEBI:65777
  evidence_ids:
  - chebi
  - parent-chalcones
  - parent-resorcinols
- assessment_id: classification
  area: evidence
  topic: Activities and filing
  outcome: supported
  summary: Primary text supports the source activities, including antimycobacterial
    testing. Filing correctly follows the retained ontology roles; it does not need
    automatic refiling from one assay organism. Antineoplastic wording is limited
    to cancer-cell cytotoxicity.
  target_ids:
  - CHEBI:65777
  evidence_ids:
  - primary
  - ownership
  - role-antibacterial
  - role-antimalarial
- assessment_id: isolation
  area: provenance
  topic: Aerial-part isolation
  outcome: supported
  summary: The paper explicitly names the compound and plant part. No biosynthetic
    pathway or independently proven producer taxon object is inferred.
  target_ids:
  - CHEBI:65777
  evidence_ids:
  - primary
  - record
- assessment_id: mechanism
  area: completeness
  topic: Molecular mode and target
  outcome: unknown
  summary: No exact antimicrobial mechanism is established by inspected text. Family
    mechanisms, mixed-extract ROS results and computational predictions cannot fill
    this gap. Native REVIEWED criteria remain unmet.
  target_ids:
  - CHEBI:65777
  evidence_ids:
  - record
  - inventory
  - primary
  - search
- assessment_id: optional
  area: representation
  topic: Assays, resistance, clinical status and graphs
  outcome: not_applicable
  summary: Optional objects are absent without a schema error. The source MIC unit
    and unavailable assay context must be resolved before adding a quantitative observation.
    No resistance or clinical claim is implied.
  target_ids:
  - CHEBI:65777
  evidence_ids:
  - record
  - primary
- assessment_id: provenance
  area: ownership
  topic: Source and history
  outcome: supported
  summary: SEEDED status and three events accurately preserve generation provenance;
    source fields and curator additions have distinct maintained ownership.
  target_ids:
  - CHEBI:65777
  evidence_ids:
  - record
  - inventory
  - ownership
- assessment_id: schema-assessment
  area: schema
  topic: Validation and structure
  outcome: supported
  summary: Both per-record validators and independent structure calculations pass.
  target_ids:
  - CHEBI:65777
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-65777-primary-assay-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Primary evidence and assay context remain an optional curation follow-up
  description: Existing identity and activity assertions are supported. No structured
    evidence or activity observation is present; full methods and literal MIC-unit
    verification are needed before safe enrichment. The missing optional slots are
    not an error.
  target_ids:
  - CHEBI:65777
  field_paths:
  - evidence
  - activity_spectrum
  - mode_of_action
  evidence_ids:
  - record
  - primary
  - search
  rule_id: 'review-checklist: Evidence standard, Activity, Mode of action'
  native_severity: informational optional enrichment
  normalization_reason: No false assertion or missing required representation was
    demonstrated; quantitative and mechanistic additions require narrower source support.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-4-dihydroxy-3-2-hydroxy-benzyl-6-methoxy-chalcone.yaml
    role: Curator-owned evidence, activity observations and mechanism notes through
      write_validated_antibiotic and a curation event
actions:
- action_id: A1
  description: During separately authorized curation, attach exact-compound primary
    evidence and inspect the full paper before encoding assays. Verify the tuberculosis
    MIC unit directly against methods/table text; preserve any unresolved discrepancy.
    Leave mechanism unresolved absent an exact-compound experiment.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65777
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-4-dihydroxy-3-2-hydroxy-benzyl-6-methoxy-chalcone.yaml
    role: Curator-owned evidence, activity observations and mechanism notes through
      write_validated_antibiotic and a curation event
  acceptance_checks:
  - Each observation retains exact compound, organism/strain, method, value and units
    from inspected primary text.
  - Do not silently replace the abstract mg/mL unit with micrograms or transfer results
    from dihydrochalcones, plant extracts or computational models.
  - Use the native validated writer and curation event; pass just validate, just validate-strict,
    just verify-corpus --summary and just qc before native promotion.
limitations:
- Only the primary abstract was inspected, corroborated on PubMed and the publisher.
  Full methods/tables were inaccessible through the bounded free search.
- The abstract literally reports 25 mg/mL for the tuberculosis MIC. No numerical observation
  is in the record, and this review does not silently correct the source unit.
- Reaxys itself was not accessed; the cross-reference is corroborated by official
  ChEBI.
- No exact experimental antimicrobial mechanism was established in the bounded search;
  this is not an exhaustive absence claim.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No source record, maintained input, generated product or history event was modified.
  Review performed in /private/tmp/antibioticmech-record-reviews-002.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:65777
- https://pubmed.ncbi.nlm.nih.gov/16833018/
- https://link.springer.com/article/10.1007/BF02969423
tags:
- record-review
- chalcone
- primary-scope
```
