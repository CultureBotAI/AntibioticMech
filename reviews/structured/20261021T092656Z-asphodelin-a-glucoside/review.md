# Asphodelin A glucoside: consistent exact identity and bounded primary antimicrobial support

- Review: 20261021T092656Z-asphodelin-a-glucoside
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:22:00Z
- Finished UTC: 2026-10-21T09:26:56Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native 4-prime-O-beta-D-glucoside structure is internally consistent and matches independent official PubChem chemistry. The sole original paper identifies the glycoside separately from its more active aglycone and reports antimicrobial activity in its abstract. The full original assay table and methods remain inaccessible, so named-organism details and numerical potency are not independently verified. No confirmed native error; one informational primary-evidence follow-up. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole exact glycoside record, structural and source identifiers, chemical definition, all adopted literature and bounded mechanism/assay checks. The aglycone is context only and is separately queued for review.

Selection: Queue 113, CHEBI:65454 at its locked native path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65454 | data/antibiotics/antibacterial/asphodelin-a-4-o-β-glucoside.yaml | generated | asphodelin A-4'-O-β-glucoside |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:65454 | Focused LinkML validation exited 0. |
| strict | passed | True | CHEBI:65454 | Focused strict scan exited 0 without ERROR rows. |
| chemistry | passed | False | CHEBI:65454 | Native SMILES/InChI, formula, charge, masses and source mint agree. |
| Authoritative full QC | failed | True | CHEBI:65454 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65454 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65454 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65454 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65454 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65454 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65454 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65454 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65454 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact glucoside structure and chemical identifiers

identity: supported. Targets: CHEBI:65454.

Official sources and independent calculations agree, including sugar stereochemistry and glycosidic position; Reaxys remains source-crosswalk-only.

### General antimicrobial activity versus exact organism detail

evidence: unknown. Targets: CHEBI:65454.

The primary abstract supports exact-glycoside antimicrobial activity. The detailed species list and root-specific source wording remain ontology-supported but unverified against the inaccessible full main text. No conflicting primary result was established.

### Optional target, mode and causal graph

completeness: unknown. Targets: CHEBI:65454.

No exact direct-target mechanism is established by the inspected original abstract. General coumarin or secondary-table gyrase claims are insufficient; optional absence is not a defect.

### Resistance, producer, clinical and datasets

completeness: unknown. Targets: CHEBI:65454.

No unsupported native claim in these optional fields. The isolated plant source is not evidence for an identified biosynthetic pathway or microbial producer. No clinical efficacy or transcriptomics inferred.

### Maintained sources and primary annotation owner

ownership: supported. Targets: CHEBI:65454.

ChEBI extraction/seed owners reproduce the row; the actual native path owns any later primary-evidence annotation.

### Focused validation and history

schema: supported. Targets: CHEBI:65454.

Focused schema, strict and chemistry gates pass; scientific status remains SEEDED.

## Findings

### F1: Inspect the original compound-1 assay before quantitative or target enrichment

informational / open / confirmed; issue key: asphodelin-a-glucoside-qualified-primary-assay-followup.

The adopted original abstract supports the exact glucoside and general antimicrobial activity but does not expose the detailed assay. Retrieve the original Table and Methods before adding organism-specific observations, potency or a protein target. Preserve compound 1 separately from aglycone compound 2.

## Recommended Actions And Acceptance Checks

### A1

Obtain and inspect the original glycoside assay, then curate only its exact evidence.

- Match compound 1 to the beta-D 4-prime-O-glucoside and native full key; do not transfer compound-2 potency or aglycone docking results.
- Read original Table and Methods for each named bacterial/fungal organism, strain, medium, endpoint, concentration and unit, including whether root and bulb extraction are distinguished.
- Treat antimicrobial growth inhibition as distinct from killing, and keep bacterial and fungal observations separate. Do not infer universal susceptibility from the tested isolates.
- Require a compound-specific primary enzyme/binding/genetic experiment before adding a DNA-gyrase or other protein target. Coumarin class reviews and docking hypotheses do not satisfy direct-binding evidence.
- Do not infer a biosynthetic gene cluster or organism production mechanism from plant-root isolation alone.
- Use write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/asphodelin-a-4-o-β-glucoside.yaml for separately authorized primary curation, then run focused/shared gates without automatic REVIEWED promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/asphodelin-a-4-o-β-glucoside.yaml; Entire YAML, including three seed/reseed events. | supports | SEEDED and EXACT glycoside with two chemical synonyms, three parent concepts, antibacterial and antifungal roles, one Reaxys xref and one ChEBI source concept. Biological definition names three bacteria and two fungi. No mode of action, protein target, quantitative activity, resistance, clinical indication, causal graph or transcriptomics dataset is asserted. Optional absence is not an error. |
| source | data/raw/chebi_antimicrobials.tsv; 113-raw.json, complete line 1177; adjacent aglycone row as identity context, ChEBI source config and relevant extraction/seed handling. | supports | Native chemistry, definitions, synonyms, parents, roles and Reaxys crosswalk reproduce the adopted glycoside row. Sole citation lead is PMID 17253862. The neighboring CHEBI:65453 row denotes the distinct aglycone; the source does not merge the two structures. All 13 maintained input hashes remain unchanged. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:65454; 113-chebi.html/txt, complete chemical, ontology, name, crosswalk and metabolite-source sections. | supports | Official ChEBI matches neutral C21H20O11 and full key OEZWCAHAQBRTTP-FKRBRYKNSA-N, including the beta-D sugar and 4-prime attachment. Parents CHEBI:22798, CHEBI:26195 and CHEBI:37912 denote beta-D-glucoside, polyphenol and hydroxycoumarin. Roles CHEBI:33282 and CHEBI:35718 are antibacterial and antifungal. A functional-parent relation to CHEBI:65453 is distinct from an is-a parent and its omission from the seeded parent_compounds list is not automatically an extraction error. Reaxys 11288781 is explicitly listed, but its paid database record was not inspected. |
| chemistry | Independent RDKit and official PubChem structure; 113-chemistry.json and 113-pubchem.json; PubChem CID 54679753 SMILES independently parsed. | supports | Native SMILES and InChI give one neutral fragment, five assigned sugar stereocentres, the same full key, formula C21H20O11, average mass consistent with 448.380 and exact mass consistent with 448.10056. Deterministic ChEBI mint matches. Independent PubChem SMILES yields the same full key. These checks preserve the glycoside rather than the lower-mass aglycone. |
| primary | DOI:10.1021/np060444u; PMID 17253862; complete original abstract and metadata in 113-epmc.json. | partial | El-Seedi identifies asphodelin A 4-prime-O-beta-D-glucoside as compound 1 and asphodelin A as compound 2 after bioactivity-directed fractionation of Asphodelus microcarpus. The exact chemical names and glycosidic position agree with the native structures. The abstract reports moderate antimicrobial activity for compound 1 and greater activity for compound 2. It does not provide the organism list, strain identifiers, MIC table, incubation conditions or a direct protein-target experiment. |
| access | Bounded primary full-text and exact-mechanism search; 113-fetch-results.json; official ACS abstract/PDF routes and exact-title, DOI, author-repository and mechanism searches. | context_only | ACS main and PDF routes returned 403. The author ResearchGate record offers a full-text request, which was not sent, and no free author-repository copy was located in the bounded searches. Review tables supply organism/potency and DNA-gyrase leads, but those are not substituted for inspected primary measurements. No quantitative MIC, direct gyrase inhibition or species-wide susceptibility is adopted from them. |
| local-search | CultureBotAI/AntibioticMech; 113-local-hits.txt and 113-maintained-search.txt. | context_only | Hidden- and ignored-inclusive searches locate glycoside and aglycone source rows, records and readiness context. No exact glycoside curated primary addition was found among the searched maintained owners. Generated pages and historical ad hoc ledgers were not treated as scientific evidence. |
| adapter | data/antibiotics/antibacterial/asphodelin-a-4-o-β-glucoside.yaml; Entire native assertion inventory and the primary abstract. | context_only | No native gene, protein, regulatory pathway, stress response or transcriptomics assertion triggers a structured adapter query. A secondary-review-only DNA-gyrase suggestion was not adopted as an experimentally supported target; a gene expression hit would not resolve its missing biochemical evidence. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity, evidence placement, activity, target and producer rules; CLAUDE and native review profile. | supports | A glycoside and its aglycone require separate assay attribution. Isolation supports source occurrence; biosynthesis and producer-gene claims need further evidence. Optional evidence gaps do not justify fabricated mechanisms or status promotion. |
| validation | Documented focused gates and input audit; 113-focused-results.json, schema/strict logs and independent chemistry output. | supports | All focused checks pass, and all 13 captured maintained inputs remain unchanged. Three seed/reseed events are consistent with SEEDED. No native record edits, paid access or contact occurred during the scientific review. |

## Limits And Additional Notes

- The sole adopted original abstract was read in full; ACS main/PDF routes returned 403 and no free full manuscript was found through bounded author/repository routes. Original spectra, sugar analysis, organism-specific assay table and methods were not inspected.
- The named bacterial/fungal list and root-specific extraction wording remain supported by ChEBI but are not independently verified from the primary abstract. This is an access limitation, not evidence that those assertions are false.
- Review-derived MIC numbers and proposed DNA-gyrase mechanisms were not adopted. Exact aglycone and glucoside evidence remains separate.
- Reaxys 11288781 is confirmed only through the source crosswalk; the underlying registry record was not inspected. No exhaustive literature, producer or resistance census is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T092656Z-asphodelin-a-glucoside
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Asphodelin A glucoside: consistent exact identity and bounded primary antimicrobial
  support'
started_at: '2026-10-21T09:22:00Z'
finished_at: '2026-10-21T09:26:56Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the record. Initial input capture preceded assessment.
    Entire record, exact source row and relevant transforms were inspected, together
    with official structures and the sole adopted primary abstract.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The native 4-prime-O-beta-D-glucoside structure is internally consistent
  and matches independent official PubChem chemistry. The sole original paper identifies
  the glycoside separately from its more active aglycone and reports antimicrobial
  activity in its abstract. The full original assay table and methods remain inaccessible,
  so named-organism details and numerical potency are not independently verified.
  No confirmed native error; one informational primary-evidence follow-up. Scientific
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
  - path: data/antibiotics/antibacterial/asphodelin-a-4-o-β-glucoside.yaml
    sha256: 6935e85c72cd820e802334caa1c81bd510e2982223a013c329c317571f51e65a
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
- target_id: CHEBI:65454
  path: data/antibiotics/antibacterial/asphodelin-a-4-o-β-glucoside.yaml
  label: asphodelin A-4'-O-β-glucoside
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
  description: Whole exact glycoside record, structural and source identifiers, chemical
    definition, all adopted literature and bounded mechanism/assay checks. The aglycone
    is context only and is separately queued for review.
  selection: Queue 113, CHEBI:65454 at its locked native path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65454
  exclusions:
  - target: Asphodelin A aglycone, other coumarins and plant extracts as exact assay
      substitutes
    reason: The source distinguishes glycoside compound 1 from aglycone compound 2.
      Scaffold, potency and enzyme claims cannot be transferred automatically.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Focused LinkML validation exited 0.
  target_ids:
  - CHEBI:65454
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/asphodelin-a-4-o-β-glucoside.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Focused strict scan exited 0 without ERROR rows.
  target_ids:
  - CHEBI:65454
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/asphodelin-a-4-o-β-glucoside.yaml --out /private/tmp/am-review-session/113-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Native SMILES/InChI, formula, charge, masses and source mint agree.
  target_ids:
  - CHEBI:65454
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache .venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 113
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
  - CHEBI:65454
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
  - CHEBI:65454
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
  - CHEBI:65454
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
  - CHEBI:65454
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
  - CHEBI:65454
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
  - CHEBI:65454
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
  - CHEBI:65454
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
  - CHEBI:65454
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
  - CHEBI:65454
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/asphodelin-a-4-o-β-glucoside.yaml
  locator: Entire YAML, including three seed/reseed events.
  accessed_at: '2026-10-21T09:23:44Z'
  support: supports
  summary: SEEDED and EXACT glycoside with two chemical synonyms, three parent concepts,
    antibacterial and antifungal roles, one Reaxys xref and one ChEBI source concept.
    Biological definition names three bacteria and two fungi. No mode of action, protein
    target, quantitative activity, resistance, clinical indication, causal graph or
    transcriptomics dataset is asserted. Optional absence is not an error.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: 113-raw.json, complete line 1177; adjacent aglycone row as identity context,
    ChEBI source config and relevant extraction/seed handling.
  accessed_at: '2026-10-21T09:23:44Z'
  support: supports
  summary: Native chemistry, definitions, synonyms, parents, roles and Reaxys crosswalk
    reproduce the adopted glycoside row. Sole citation lead is PMID 17253862. The
    neighboring CHEBI:65453 row denotes the distinct aglycone; the source does not
    merge the two structures. All 13 maintained input hashes remain unchanged.
  snapshot_sha256: 8ba1d2aae7857010c7277b88c7802eb3611754356f6a9c7a93c3a186ebd02fed
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:65454
  locator: 113-chebi.html/txt, complete chemical, ontology, name, crosswalk and metabolite-source
    sections.
  accessed_at: '2026-10-21T09:23:44Z'
  support: supports
  summary: Official ChEBI matches neutral C21H20O11 and full key OEZWCAHAQBRTTP-FKRBRYKNSA-N,
    including the beta-D sugar and 4-prime attachment. Parents CHEBI:22798, CHEBI:26195
    and CHEBI:37912 denote beta-D-glucoside, polyphenol and hydroxycoumarin. Roles
    CHEBI:33282 and CHEBI:35718 are antibacterial and antifungal. A functional-parent
    relation to CHEBI:65453 is distinct from an is-a parent and its omission from
    the seeded parent_compounds list is not automatically an extraction error. Reaxys
    11288781 is explicitly listed, but its paid database record was not inspected.
  snapshot_sha256: 0c71125f5c7336244ab7e66f6718d248aacfb97f96b89a465fb58ec469487c6e
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit and official PubChem structure
  locator: 113-chemistry.json and 113-pubchem.json; PubChem CID 54679753 SMILES independently
    parsed.
  accessed_at: '2026-10-21T09:23:44Z'
  support: supports
  summary: Native SMILES and InChI give one neutral fragment, five assigned sugar
    stereocentres, the same full key, formula C21H20O11, average mass consistent with
    448.380 and exact mass consistent with 448.10056. Deterministic ChEBI mint matches.
    Independent PubChem SMILES yields the same full key. These checks preserve the
    glycoside rather than the lower-mass aglycone.
  snapshot_sha256: 3cff4cc6c40f23ac07a21ff3c044b13f71179d123cdd7ac784cb079f26021f03
- evidence_id: primary
  kind: primary_source
  reference: DOI:10.1021/np060444u
  locator: PMID 17253862; complete original abstract and metadata in 113-epmc.json.
  accessed_at: '2026-10-21T09:23:44Z'
  support: partial
  summary: El-Seedi identifies asphodelin A 4-prime-O-beta-D-glucoside as compound
    1 and asphodelin A as compound 2 after bioactivity-directed fractionation of Asphodelus
    microcarpus. The exact chemical names and glycosidic position agree with the native
    structures. The abstract reports moderate antimicrobial activity for compound
    1 and greater activity for compound 2. It does not provide the organism list,
    strain identifiers, MIC table, incubation conditions or a direct protein-target
    experiment.
  snapshot_sha256: 8c754394679c2f41dbb199997edcdb07fe234fe4c3717d8e265cdb730cfcd74c
- evidence_id: access
  kind: search
  reference: Bounded primary full-text and exact-mechanism search
  locator: 113-fetch-results.json; official ACS abstract/PDF routes and exact-title,
    DOI, author-repository and mechanism searches.
  accessed_at: '2026-10-21T09:23:44Z'
  support: context_only
  summary: ACS main and PDF routes returned 403. The author ResearchGate record offers
    a full-text request, which was not sent, and no free author-repository copy was
    located in the bounded searches. Review tables supply organism/potency and DNA-gyrase
    leads, but those are not substituted for inspected primary measurements. No quantitative
    MIC, direct gyrase inhibition or species-wide susceptibility is adopted from them.
  search_scope: Exact DOI 10.1021/np060444u, PMID 17253862, title, asphodelin A glucoside,
    full-text/PDF and Uppsala DiVA routes; bounded gyrase/mechanism search; free sources
    only.
  snapshot_sha256: dbee895dc1b177d67bbfc8c3e9fc998ff82bbc9cab14fb8a46bbca4e7e70d2f6
- evidence_id: local-search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 113-local-hits.txt and 113-maintained-search.txt.
  accessed_at: '2026-10-21T09:23:44Z'
  support: context_only
  summary: Hidden- and ignored-inclusive searches locate glycoside and aglycone source
    rows, records and readiness context. No exact glycoside curated primary addition
    was found among the searched maintained owners. Generated pages and historical
    ad hoc ledgers were not treated as scientific evidence.
  search_scope: rg --no-ignore --hidden for the exact identifier, label/slug, asphodelin/Asphodelin
    and OEZWCAHAQBRTTP across batch012, then curation/conf/scripts/data/raw/src/reports/reviews;
    initial whole-worktree scan excludes .git and .venv.
  snapshot_sha256: e6ce9154d404bae43df375e9905e0ea35385b48b32062bf593d229f04eac71c8
- evidence_id: adapter
  kind: record_content
  reference: data/antibiotics/antibacterial/asphodelin-a-4-o-β-glucoside.yaml
  locator: Entire native assertion inventory and the primary abstract.
  accessed_at: '2026-10-21T09:23:44Z'
  support: context_only
  summary: No native gene, protein, regulatory pathway, stress response or transcriptomics
    assertion triggers a structured adapter query. A secondary-review-only DNA-gyrase
    suggestion was not adopted as an experimentally supported target; a gene expression
    hit would not resolve its missing biochemical evidence.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity, evidence placement, activity, target and producer rules; CLAUDE
    and native review profile.
  accessed_at: '2026-10-21T09:23:44Z'
  support: supports
  summary: A glycoside and its aglycone require separate assay attribution. Isolation
    supports source occurrence; biosynthesis and producer-gene claims need further
    evidence. Optional evidence gaps do not justify fabricated mechanisms or status
    promotion.
- evidence_id: validation
  kind: validation
  reference: Documented focused gates and input audit
  locator: 113-focused-results.json, schema/strict logs and independent chemistry
    output.
  accessed_at: '2026-10-21T09:23:44Z'
  support: supports
  summary: All focused checks pass, and all 13 captured maintained inputs remain unchanged.
    Three seed/reseed events are consistent with SEEDED. No native record edits, paid
    access or contact occurred during the scientific review.
  snapshot_sha256: 97e18b7a09f6a60751e8a3048e9c3661620f8417b244dea58115e8d6ade0caa9
assessments:
- assessment_id: identity
  area: identity
  topic: Exact glucoside structure and chemical identifiers
  outcome: supported
  summary: Official sources and independent calculations agree, including sugar stereochemistry
    and glycosidic position; Reaxys remains source-crosswalk-only.
  target_ids:
  - CHEBI:65454
  evidence_ids:
  - identity
  - chemistry
  - primary
- assessment_id: activity
  area: evidence
  topic: General antimicrobial activity versus exact organism detail
  outcome: unknown
  summary: The primary abstract supports exact-glycoside antimicrobial activity. The
    detailed species list and root-specific source wording remain ontology-supported
    but unverified against the inaccessible full main text. No conflicting primary
    result was established.
  target_ids:
  - CHEBI:65454
  evidence_ids:
  - primary
  - identity
  - access
- assessment_id: mechanism
  area: completeness
  topic: Optional target, mode and causal graph
  outcome: unknown
  summary: No exact direct-target mechanism is established by the inspected original
    abstract. General coumarin or secondary-table gyrase claims are insufficient;
    optional absence is not a defect.
  target_ids:
  - CHEBI:65454
  evidence_ids:
  - primary
  - access
  - adapter
  - rubric
- assessment_id: other
  area: completeness
  topic: Resistance, producer, clinical and datasets
  outcome: unknown
  summary: No unsupported native claim in these optional fields. The isolated plant
    source is not evidence for an identified biosynthetic pathway or microbial producer.
    No clinical efficacy or transcriptomics inferred.
  target_ids:
  - CHEBI:65454
  evidence_ids:
  - record
  - primary
  - rubric
- assessment_id: ownership
  area: ownership
  topic: Maintained sources and primary annotation owner
  outcome: supported
  summary: ChEBI extraction/seed owners reproduce the row; the actual native path
    owns any later primary-evidence annotation.
  target_ids:
  - CHEBI:65454
  evidence_ids:
  - source
  - rubric
- assessment_id: gates
  area: schema
  topic: Focused validation and history
  outcome: supported
  summary: Focused schema, strict and chemistry gates pass; scientific status remains
    SEEDED.
  target_ids:
  - CHEBI:65454
  evidence_ids:
  - validation
  - record
findings:
- finding_id: F1
  issue_key: asphodelin-a-glucoside-qualified-primary-assay-followup
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Inspect the original compound-1 assay before quantitative or target enrichment
  description: The adopted original abstract supports the exact glucoside and general
    antimicrobial activity but does not expose the detailed assay. Retrieve the original
    Table and Methods before adding organism-specific observations, potency or a protein
    target. Preserve compound 1 separately from aglycone compound 2.
  target_ids:
  - CHEBI:65454
  field_paths:
  - definition
  - activity_spectrum
  - molecular_targets
  - mode_of_action
  - evidence
  - discussions
  evidence_ids:
  - primary
  - access
  - identity
  - rubric
  rule_id: 'native-review-checklist: Exact-subject primary evidence and completeness'
  native_severity: informational optional evidence enrichment with an access limitation
  normalization_reason: No confirmed wrong assertion or required-field failure; source
    detail is limited by primary access. Secondary tables cannot replace original
    inspection.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/asphodelin-a-4-o-β-glucoside.yaml
    role: Curator-owned primary evidence and qualified activity annotations through
      the validated writer and history helper
actions:
- action_id: A1
  description: Obtain and inspect the original glycoside assay, then curate only its
    exact evidence.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65454
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/asphodelin-a-4-o-β-glucoside.yaml
    role: Curator-owned primary evidence and qualified activity annotations through
      the validated writer and history helper
  acceptance_checks:
  - Match compound 1 to the beta-D 4-prime-O-glucoside and native full key; do not
    transfer compound-2 potency or aglycone docking results.
  - Read original Table and Methods for each named bacterial/fungal organism, strain,
    medium, endpoint, concentration and unit, including whether root and bulb extraction
    are distinguished.
  - Treat antimicrobial growth inhibition as distinct from killing, and keep bacterial
    and fungal observations separate. Do not infer universal susceptibility from the
    tested isolates.
  - Require a compound-specific primary enzyme/binding/genetic experiment before adding
    a DNA-gyrase or other protein target. Coumarin class reviews and docking hypotheses
    do not satisfy direct-binding evidence.
  - Do not infer a biosynthetic gene cluster or organism production mechanism from
    plant-root isolation alone.
  - Use write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/asphodelin-a-4-o-β-glucoside.yaml
    for separately authorized primary curation, then run focused/shared gates without
    automatic REVIEWED promotion.
limitations:
- The sole adopted original abstract was read in full; ACS main/PDF routes returned
  403 and no free full manuscript was found through bounded author/repository routes.
  Original spectra, sugar analysis, organism-specific assay table and methods were
  not inspected.
- The named bacterial/fungal list and root-specific extraction wording remain supported
  by ChEBI but are not independently verified from the primary abstract. This is an
  access limitation, not evidence that those assertions are false.
- Review-derived MIC numbers and proposed DNA-gyrase mechanisms were not adopted.
  Exact aglycone and glucoside evidence remains separate.
- Reaxys 11288781 is confirmed only through the source crosswalk; the underlying registry
  record was not inspected. No exhaustive literature, producer or resistance census
  is claimed.
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
