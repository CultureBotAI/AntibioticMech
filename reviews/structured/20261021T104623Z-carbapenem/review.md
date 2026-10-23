# Carbapenem nucleus: exact identity is coherent; compound-specific antibacterial support remains unresolved

- Review: 20261021T104623Z-carbapenem
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:32:39Z
- Finished UTC: 2026-10-21T10:46:23Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The record denotes the fixed (5R) bare carbapenem nucleus, C6H7NO, and matches current ChEBI and exact-key PubChem identity. It is not a variable drug-class record and is not the carboxylated natural antibiotic SQ27860. Documented validators and independent chemistry pass. The antibacterial role is inherited and source-attested, but no exact-material antibacterial assay was established in the bounded primary search. One informational source-evidence follow-up remains; this is neither proof of inactivity nor a confirmed classification error. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole CHEBI46765 record: definition, two exact synonyms, one parent, two activity roles, all chemical descriptors, sole source concept/mint and three history entries. The exact adopted source has no xrefs, citation leads or mechanism roles.

Selection: Queue 196; preserved initial capture and exact native path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:46765 | data/antibiotics/antibacterial/carbapenem.yaml | generated | carbapenem |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:46765 | Actual focused command exited 0. |
| strict | passed | True | CHEBI:46765 | Actual focused command exited 0. |
| chemistry | passed | False | CHEBI:46765 | Actual focused command exited 0. The batch020 environment lacks RDKit, so the existing batch019 interpreter was used with batch020 as cwd. Both strings independently reproduce the full key, formula, charge, masses, R stereocentre and source mint. |
| Authoritative full QC | failed | True | CHEBI:46765 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:46765 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:46765 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:46765 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:46765 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:46765 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:46765 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:46765 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:46765 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Fixed nucleus versus class or carboxylated antibiotic

identity: supported. Targets: CHEBI:46765.

CHEBI46765 denotes one fixed (5R) C6H7NO structure. It must remain distinct from the variable class parent and C7H7NO3 SQ27860/carboxylic acid; the label alone does not make it a forbidden class record.

### Definition and both exact synonyms

nomenclature: supported. Targets: CHEBI:46765.

Definition, conventional carbapenam numbering and azabicyclic synonym agree with the current official exact entity and its parsed R configuration.

### Inherited source activity roles

provenance: supported. Targets: CHEBI:46765.

The exact maintained row and current ChEBI ontology explain both retained roles and ANTIBACTERIAL filing. This supports source fidelity, not independent experimental confirmation.

### Exact-material antibacterial support

evidence: unknown. Targets: CHEBI:46765.

No inspected primary experiment establishes the bare C6H7NO nucleus as antibacterial. The bounded search found distinct carboxylated antibiotics, substituted-drug assays, docking and class context. No inactivity conclusion or confirmed wrong role follows.

### Targets, resistance and causal graph

completeness: unknown. Targets: CHEBI:46765.

The native record makes no mechanism or target claims. Family PBP descriptions, meropenem docking and resistance profiles cannot fill these optional fields for the bare nucleus.

### Producer and biosynthesis

completeness: unknown. Targets: CHEBI:46765.

Serratia/Erwinia evidence concerns the carboxylated SQ27860 molecule. No exact bare-nucleus producer or biosynthetic origin was established.

### Maintained-source adjudication

ownership: supported. Targets: CHEBI:46765.

Any future source-role or inclusion correction belongs to the maintained ChEBI source/extractor and documented decision layer; a native-only patch would be overwritten. Exact claim-level additions, if found, belong to the actual native record.

### Focused schema, strict, chemistry and history

schema: supported. Targets: CHEBI:46765.

Complete history was read and all actual focused gates pass. These do not close the exact-material experimental support gap.

## Findings

### F1: Resolve exact-nucleus activity support before extending inherited class-level biology

informational / open / provisional; issue key: bare-carbapenem-exact-activity-source-followup.

The inherited ChEBI antibacterial role is source-attested, but the bare C6H7NO nucleus has no adopted citation and no exact positive experiment was established in the bounded search. Inspected near matches concern SQ27860/carboxylic acid, named substituted carbapenems or structural context. This is a conditional source-evidence follow-up, not proof of inactivity, a demand for optional fields, or a confirmed class-record error.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate the inherited antibacterial role with exact-material evidence and preserve nucleus/drug boundaries.

- Seek an original experiment whose tested structure is the (5R) C6H7NO nucleus with full key YZBQHRLRFGPBSL-RXMQYKEDSA-N. Inspect the actual compound drawing and methods, not only a carbapenem title, broad-name database link or class annotation.
- Keep the reviewed entity distinct from SQ27860/C7H7NO3, PubChem441133, meropenem, imipenem and the variable CHEBI46633 class. Do not import their MICs, producer organisms, PBP targets, efflux-pump docking or resistance observations.
- If exact positive evidence is found, attach it at the narrow tested-material/activity claim using write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/carbapenem.yaml; preserve organism, method, endpoint and material stereochemistry. Do not promote to REVIEWED until native sign-off requirements are satisfied.
- If a documented source adjudication establishes that the role applies only to substituted class members, implement an exact maintained-source correction or justified curation/decisions.tsv exclusion for antibioticmech:chebi-c1b974cf3a and regenerate through the documented pipeline. A zero-result literature query alone is insufficient grounds for exclusion.
- After any separately authorized change, run the focused record validators, check role/source coherence and exact structure/mint, and run applicable shared gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/carbapenem.yaml; Entire native record and all three history events. | supports | SEEDED/EXACT structure of the bare (5R) nucleus. No variable R groups, xrefs, curated evidence, molecular targets, mode of action, producer, activity observations, resistance mechanism or causal graph is asserted. Missing optional fields alone are not errors. |
| source | data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact row 877; source three-star/reviewed-edge rules; extractor lines202–336 and seeder structure/concept import. | supports | The raw row reproduces every native source assertion and contains no citation or mechanism-role leads. The extractor propagates roles through reviewed is_a descendants; the current official parent CHEBI46633 carries antibacterial agent. Thus this is a source-backed inherited role, not a new curator inference. No exact corrective maintained row was found in the hidden-and-ignored-inclusive search. All 13 initial input hashes remain unchanged. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:46765; Complete official entry, definition, structures, names, role display and outgoing relation. | supports | ChEBI denotes a fixed (5R) organic heterobicycle and calls it the parent nucleus. Both exact synonyms correspond to that structure. Formula C6H7NO, charge 0, average mass 109.128, monoisotopic mass 109.05276 and key YZBQHRLRFGPBSL-RXMQYKEDSA-N match the record. Its outgoing is_a relation points to CHEBI46633 carbapenems; the displayed antibacterial/antimicrobial roles are inherited. No citation is listed on this exact entry. |
| parent | https://www.ebi.ac.uk/chebi/CHEBI:46633; Complete official parent entry and outgoing role relation. | partial | CHEBI46633 is the broader carbapenems class with variable substituents and has_role CHEBI33282 antibacterial agent; CHEBI33281 antimicrobial agent is its broader role. The class role explains source selection but does not independently demonstrate a bacterial-growth assay for the fixed unsubstituted C6H7NO nucleus. The native class parent is not an asserted exact xref. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/13293131; https://pubchem.ncbi.nlm.nih.gov/compound/441133; Official exact-key property response and complete PUG-View annotations; separate CID441133 property response. | supports | Exact-key CID13293131 agrees with the native structure and computed properties. Its current display name is Carbapenem antibacterials, and several ambiguous aliases are in removed synonyms. The name-only carbapenem result CID441133 instead has C7H7NO3 and key BSIMZHVOQZIAOY-SCSAIBSYSA-N, a carboxylated molecule. Literature/co-occurrence links attached to a broad name do not establish exact-material activity. No native xref makes this name collision a record error. |
| chemistry | 196-chemistry.json; Independent RDKit parsing and source-mint reproduction. | supports | Both native strings are valid one-fragment neutral molecules with one assigned R stereocentre and matching composition, key and masses. The source mint antibioticmech:chebi-c1b974cf3a reproduces. The fixed chemical structure meets the exact-identity operational contract despite its scaffold name. |
| sq27860 | PMID:7118721; DOI:10.7164/antibiotics.35.653; Original PDF p653 title, abstract, introductory antibacterial statement and Figure 1, visually inspected; adjacent strain-description text. | context_only | The superficially relevant simple-carbapenem paper concerns SQ27860. Its original Figure 1 explicitly includes a carboxylic acid substituent, absent from the reviewed nucleus. Its antibacterial and Serratia/Erwinia production statements therefore do not establish corresponding claims for CHEBI46765. This primary paper is used only to resolve the near-match boundary, not as exact positive or negative activity evidence. |
| plant2020 | DOI:10.7732/kjpr.2020.33.6.578; https://www.kjpr.kr/articles/xml/wO1j/; Complete main article HTML, Methods, Results and tables. | context_only | A portal hit annotates carbapenem with C6H7NO, but the original experiments test ampicillin with medicinal-plant extracts; the Hodge-test controls include named imipenem and meropenem discs. Carbapenem appears in general background. There is no exact bare-nucleus assay in this inspected study, so its activity and beta-lactamase results do not transfer. |
| efflux2023 | PMID:36978353; DOI:10.3390/antibiotics12030486; PMC10044530; Complete main text; Methods 2.4/2.7, Results 3.5 and Tables 2/5/13. | context_only | The systematic-name hit refers to the carbapenem substructure within docked meropenem. Table 2 lists meropenem and imipenem as the tested carbapenems; docking is explicitly meropenem. Neither these susceptibility results nor computational contacts with efflux-pump models establish bare C6H7NO activity, direct binding or resistance. |
| review2025 | PMID:40430299; DOI:10.3390/molecules30102126; PMC12113772; Abstract, Section 2.1 and Figure 3 caption; selected structural discussion only. | context_only | This secondary review identifies the exact systematic name as the central carbapenem heterocycle. It distinguishes that core from named substituted therapeutic compounds. It is nomenclature context only, not a primary assay of the bare nucleus; the whole review was not independently audited. |
| literature-search | 196-epmc-query1.json; 196-epmc-query2.json; 196-epmc-query3.json; 196-search-notes.json; Bounded exact-name/key public search and EuropePMC responses. | context_only | EuropePMC exact key-stem and exact 2,3-didehydro-1-carbapenam searches return zero; the systematic-name query returns four hits: the inspected 2025 review, the inspected 2023 meropenem paper, and two patent abstracts explicitly concerning substituted carboxylic acids. Additional exact-formula/name searches yielded the inspected 2020 and 1982 near matches. No exact C6H7NO antibacterial experiment was established; this is a search limitation rather than proof that none exists. |
| local-search | 196-local-hits.txt; 196-inclusive-file-hits.txt; 196-maintained-exact-search.txt; Hidden-and-ignored-inclusive local search before absence conclusions. | context_only | Matches include exact source/native records, path ledger, generated maps, readiness queue and related compound/historical-report references. No exact corrective curator or decision row was found within the maintained search. Historical reviews were leads only and their prior severity or conclusions were not adopted. |
| adapter | Structured-source applicability assessed from complete native record before open-ended web research; No native gene, locus, protein, regulator, pathway, stress-response or transcriptomics assertion. | context_only | No native claim triggered an iModulonDB query. The meropenem efflux search hit concerns a different molecule and cannot become bare-nucleus response or resistance evidence. |
| validation | 196-focused-results.json; 196-schema.log; 196-strict.log; Actual documented per-record schema/strict checks and independent chemistry. | supports | All focused checks exit 0. They establish deterministic consistency without establishing experimentally demonstrated exact-material activity. |

## Limits And Additional Notes

- All 13 initial input hashes were captured before assessment and remain unchanged. Complete native record, exact source row and relevant configuration, role-inheritance, extraction and seeding code were inspected.
- The adopted source contains zero citation leads. This review is partial because exact-material antibacterial activity, target, resistance and producer evidence remains unresolved, despite consistent official identity and source roles.
- The original SQ27860 paper was inspected for p653 identity, antibacterial statement and Figure 1, plus adjacent strain-description text, to resolve a near match. Its entire production/assay dataset was not independently reviewed for this distinct bare-nucleus record.
- The 2020 primary article main text was read in full. The 2023 primary main text and relevant antibiotic/docking tables were read. The 2025 secondary review was inspected only for abstract and relevant structural sections/caption; it is context rather than primary support.
- Exact EuropePMC searches are not a comprehensive literature inventory. Two patent abstracts concern substituted carboxylic acids and their full patents were not inspected. Broad PubChem literature/co-occurrence and patent counts were not treated as exact chemical experiments.
- The absence of a direct antibacterial experiment in this bounded review does not prove the bare nucleus inactive and does not itself overturn a reviewed ChEBI role or authorize exclusion.
- The batch020 locked environment lacks RDKit; chemistry used the batch019 interpreter against unchanged batch020 inputs. Native gene/protein/response assertions are absent, so no structured transcriptomic query was applicable.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T104623Z-carbapenem
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Carbapenem nucleus: exact identity is coherent; compound-specific antibacterial
  support remains unresolved'
started_at: '2026-10-21T10:32:39Z'
finished_at: '2026-10-21T10:46:23Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the native seed. Preserved and checked initial
    input captures, read the entire native record and maintained source, traced inherited
    roles through source transforms, checked exact official structures and inspected
    relevant primary search hits without transferring substituted-drug results.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The record denotes the fixed (5R) bare carbapenem nucleus, C6H7NO, and matches
  current ChEBI and exact-key PubChem identity. It is not a variable drug-class record
  and is not the carboxylated natural antibiotic SQ27860. Documented validators and
  independent chemistry pass. The antibacterial role is inherited and source-attested,
  but no exact-material antibacterial assay was established in the bounded primary
  search. One informational source-evidence follow-up remains; this is neither proof
  of inactivity nor a confirmed classification error. Scientific assessment retains
  the stated evidence limits; full verification is blocked by the shared native-library
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
  - path: data/antibiotics/antibacterial/carbapenem.yaml
    sha256: 10b9f7ccae19c8241ebda35e14188a29d22f231d745a8eed3bbb0ace5e65e1cb
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
- target_id: CHEBI:46765
  path: data/antibiotics/antibacterial/carbapenem.yaml
  label: carbapenem
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
  description: 'Whole CHEBI46765 record: definition, two exact synonyms, one parent,
    two activity roles, all chemical descriptors, sole source concept/mint and three
    history entries. The exact adopted source has no xrefs, citation leads or mechanism
    roles.'
  selection: Queue 196; preserved initial capture and exact native path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:46765
  exclusions:
  - target: Carbapenem drug class, carbapenem-3-carboxylic acid/SQ27860, meropenem,
      imipenem and other substituted derivatives
    reason: The reviewed molecule is the fixed C6H7NO nucleus. Evidence for these
      classes or distinct molecules cannot establish its exact activity, targets,
      producer or resistance.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:46765
  evidence_ids:
  - validation
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/carbapenem.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:46765
  evidence_ids:
  - validation
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/carbapenem.yaml --out /private/tmp/am-review-session/196-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Actual focused command exited 0. The batch020 environment lacks RDKit,
    so the existing batch019 interpreter was used with batch020 as cwd. Both strings
    independently reproduce the full key, formula, charge, masses, R stereocentre
    and source mint.
  target_ids:
  - CHEBI:46765
  evidence_ids:
  - validation
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 196
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
  - CHEBI:46765
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
  - CHEBI:46765
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
  - CHEBI:46765
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
  - CHEBI:46765
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
  - CHEBI:46765
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
  - CHEBI:46765
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
  - CHEBI:46765
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
  - CHEBI:46765
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
  - CHEBI:46765
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/carbapenem.yaml
  locator: Entire native record and all three history events.
  accessed_at: '2026-10-21T10:44:21Z'
  support: supports
  summary: SEEDED/EXACT structure of the bare (5R) nucleus. No variable R groups,
    xrefs, curated evidence, molecular targets, mode of action, producer, activity
    observations, resistance mechanism or causal graph is asserted. Missing optional
    fields alone are not errors.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Exact row 877; source three-star/reviewed-edge rules; extractor lines202–336
    and seeder structure/concept import.
  accessed_at: '2026-10-21T10:44:21Z'
  support: supports
  summary: The raw row reproduces every native source assertion and contains no citation
    or mechanism-role leads. The extractor propagates roles through reviewed is_a
    descendants; the current official parent CHEBI46633 carries antibacterial agent.
    Thus this is a source-backed inherited role, not a new curator inference. No exact
    corrective maintained row was found in the hidden-and-ignored-inclusive search.
    All 13 initial input hashes remain unchanged.
  snapshot_sha256: 7d012ccaad2cdac789738db4fde5b04322dc334d0e0579d0a86a7adb74c68d88
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:46765
  locator: Complete official entry, definition, structures, names, role display and
    outgoing relation.
  accessed_at: '2026-10-21T10:44:21Z'
  support: supports
  summary: ChEBI denotes a fixed (5R) organic heterobicycle and calls it the parent
    nucleus. Both exact synonyms correspond to that structure. Formula C6H7NO, charge
    0, average mass 109.128, monoisotopic mass 109.05276 and key YZBQHRLRFGPBSL-RXMQYKEDSA-N
    match the record. Its outgoing is_a relation points to CHEBI46633 carbapenems;
    the displayed antibacterial/antimicrobial roles are inherited. No citation is
    listed on this exact entry.
  snapshot_sha256: 7c04225390121e8e756e500ff5e2edeef715f4a24ce1a77cb20fe00a1b3a105e
- evidence_id: parent
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:46633
  locator: Complete official parent entry and outgoing role relation.
  accessed_at: '2026-10-21T10:44:21Z'
  support: partial
  summary: CHEBI46633 is the broader carbapenems class with variable substituents
    and has_role CHEBI33282 antibacterial agent; CHEBI33281 antimicrobial agent is
    its broader role. The class role explains source selection but does not independently
    demonstrate a bacterial-growth assay for the fixed unsubstituted C6H7NO nucleus.
    The native class parent is not an asserted exact xref.
  snapshot_sha256: af7b0368b05fcd1a5e2de81da150e59db9acc2169f48508d8c6b918ffc10de5f
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/13293131; https://pubchem.ncbi.nlm.nih.gov/compound/441133
  locator: Official exact-key property response and complete PUG-View annotations;
    separate CID441133 property response.
  accessed_at: '2026-10-21T10:44:21Z'
  support: supports
  summary: Exact-key CID13293131 agrees with the native structure and computed properties.
    Its current display name is Carbapenem antibacterials, and several ambiguous aliases
    are in removed synonyms. The name-only carbapenem result CID441133 instead has
    C7H7NO3 and key BSIMZHVOQZIAOY-SCSAIBSYSA-N, a carboxylated molecule. Literature/co-occurrence
    links attached to a broad name do not establish exact-material activity. No native
    xref makes this name collision a record error.
  snapshot_sha256: 050aa4ed511d4ea1c079b469f18c77f75fb1d4f6e7cea879a6ce14dcec118595
- evidence_id: chemistry
  kind: validation
  reference: 196-chemistry.json
  locator: Independent RDKit parsing and source-mint reproduction.
  accessed_at: '2026-10-21T10:44:21Z'
  support: supports
  summary: Both native strings are valid one-fragment neutral molecules with one assigned
    R stereocentre and matching composition, key and masses. The source mint antibioticmech:chebi-c1b974cf3a
    reproduces. The fixed chemical structure meets the exact-identity operational
    contract despite its scaffold name.
  snapshot_sha256: f2b634f4c5691b77684aa5660f08f575acedb4d8f836adbb7025f9de4a7a0ac5
- evidence_id: sq27860
  kind: primary_source
  reference: PMID:7118721; DOI:10.7164/antibiotics.35.653
  locator: Original PDF p653 title, abstract, introductory antibacterial statement
    and Figure 1, visually inspected; adjacent strain-description text.
  accessed_at: '2026-10-21T10:44:21Z'
  support: context_only
  summary: The superficially relevant simple-carbapenem paper concerns SQ27860. Its
    original Figure 1 explicitly includes a carboxylic acid substituent, absent from
    the reviewed nucleus. Its antibacterial and Serratia/Erwinia production statements
    therefore do not establish corresponding claims for CHEBI46765. This primary paper
    is used only to resolve the near-match boundary, not as exact positive or negative
    activity evidence.
  snapshot_sha256: 285e55535a68f0dddf45803ab63b8f63b086ea235ff9f570f031f789c922e774
- evidence_id: plant2020
  kind: primary_source
  reference: DOI:10.7732/kjpr.2020.33.6.578; https://www.kjpr.kr/articles/xml/wO1j/
  locator: Complete main article HTML, Methods, Results and tables.
  accessed_at: '2026-10-21T10:44:21Z'
  support: context_only
  summary: A portal hit annotates carbapenem with C6H7NO, but the original experiments
    test ampicillin with medicinal-plant extracts; the Hodge-test controls include
    named imipenem and meropenem discs. Carbapenem appears in general background.
    There is no exact bare-nucleus assay in this inspected study, so its activity
    and beta-lactamase results do not transfer.
  snapshot_sha256: 907a093a99095646676f26f7f9aef10db4706362953672fd225cbae6a98aac24
- evidence_id: efflux2023
  kind: primary_source
  reference: PMID:36978353; DOI:10.3390/antibiotics12030486; PMC10044530
  locator: Complete main text; Methods 2.4/2.7, Results 3.5 and Tables 2/5/13.
  accessed_at: '2026-10-21T10:44:21Z'
  support: context_only
  summary: The systematic-name hit refers to the carbapenem substructure within docked
    meropenem. Table 2 lists meropenem and imipenem as the tested carbapenems; docking
    is explicitly meropenem. Neither these susceptibility results nor computational
    contacts with efflux-pump models establish bare C6H7NO activity, direct binding
    or resistance.
  snapshot_sha256: db87ca4bfcb99e2a9c73a5723fe73aaf02db6270b6235bf31ab9125cae1fbd5d
- evidence_id: review2025
  kind: database
  reference: PMID:40430299; DOI:10.3390/molecules30102126; PMC12113772
  locator: Abstract, Section 2.1 and Figure 3 caption; selected structural discussion
    only.
  accessed_at: '2026-10-21T10:44:21Z'
  support: context_only
  summary: This secondary review identifies the exact systematic name as the central
    carbapenem heterocycle. It distinguishes that core from named substituted therapeutic
    compounds. It is nomenclature context only, not a primary assay of the bare nucleus;
    the whole review was not independently audited.
  snapshot_sha256: b856647941f43cf97af1cd1a8918e609123b93c1e2bf8b7b68733e7151261e2c
- evidence_id: literature-search
  kind: search
  reference: 196-epmc-query1.json; 196-epmc-query2.json; 196-epmc-query3.json; 196-search-notes.json
  locator: Bounded exact-name/key public search and EuropePMC responses.
  accessed_at: '2026-10-21T10:44:21Z'
  support: context_only
  summary: 'EuropePMC exact key-stem and exact 2,3-didehydro-1-carbapenam searches
    return zero; the systematic-name query returns four hits: the inspected 2025 review,
    the inspected 2023 meropenem paper, and two patent abstracts explicitly concerning
    substituted carboxylic acids. Additional exact-formula/name searches yielded the
    inspected 2020 and 1982 near matches. No exact C6H7NO antibacterial experiment
    was established; this is a search limitation rather than proof that none exists.'
  snapshot_sha256: 976766118baca39b9d016c7d8b401c53489090f7db9f736851bb7a7994ea9b91
  search_scope: Free public web queries for full InChIKey, CHEBI46765, exact synonyms,
    C6H7NO with antibacterial/activity/synthesis, bare or unsubstituted carbapenem
    nucleus, and the SQ27860 near match; exact EuropePMC queries captured in three
    JSON responses. No subscription or exhaustive patent search.
- evidence_id: local-search
  kind: search
  reference: 196-local-hits.txt; 196-inclusive-file-hits.txt; 196-maintained-exact-search.txt
  locator: Hidden-and-ignored-inclusive local search before absence conclusions.
  accessed_at: '2026-10-21T10:44:21Z'
  support: context_only
  summary: Matches include exact source/native records, path ledger, generated maps,
    readiness queue and related compound/historical-report references. No exact corrective
    curator or decision row was found within the maintained search. Historical reviews
    were leads only and their prior severity or conclusions were not adopted.
  snapshot_sha256: cb132b5169e1f0fd83a6bd19cb55280958ffdfba8be23fc1fe4ea9589191e33e
  search_scope: rg --no-ignore --hidden across data, curation, conf, scripts, src,
    docs, .claude, reviews and reports for CHEBI:46765, YZBQHRLRFGPBSL, carbapenem.yaml
    and the exact systematic synonym; .git and .venv internals excluded. Initial capture
    also searched identifier, label and slug across the worktree.
- evidence_id: adapter
  kind: database
  reference: Structured-source applicability assessed from complete native record
    before open-ended web research
  locator: No native gene, locus, protein, regulator, pathway, stress-response or
    transcriptomics assertion.
  accessed_at: '2026-10-21T10:44:21Z'
  support: context_only
  summary: No native claim triggered an iModulonDB query. The meropenem efflux search
    hit concerns a different molecule and cannot become bare-nucleus response or resistance
    evidence.
- evidence_id: validation
  kind: validation
  reference: 196-focused-results.json; 196-schema.log; 196-strict.log
  locator: Actual documented per-record schema/strict checks and independent chemistry.
  accessed_at: '2026-10-21T10:44:21Z'
  support: supports
  summary: All focused checks exit 0. They establish deterministic consistency without
    establishing experimentally demonstrated exact-material activity.
  snapshot_sha256: 23632a8f8272f9326a315a62bd42668e6db5175b06b2c6b6177466c88017df43
assessments:
- assessment_id: identity
  area: identity
  topic: Fixed nucleus versus class or carboxylated antibiotic
  outcome: supported
  summary: CHEBI46765 denotes one fixed (5R) C6H7NO structure. It must remain distinct
    from the variable class parent and C7H7NO3 SQ27860/carboxylic acid; the label
    alone does not make it a forbidden class record.
  target_ids:
  - CHEBI:46765
  evidence_ids:
  - record
  - chebi
  - pubchem
  - chemistry
  - sq27860
- assessment_id: nomenclature
  area: nomenclature
  topic: Definition and both exact synonyms
  outcome: supported
  summary: Definition, conventional carbapenam numbering and azabicyclic synonym agree
    with the current official exact entity and its parsed R configuration.
  target_ids:
  - CHEBI:46765
  evidence_ids:
  - chebi
  - chemistry
  - review2025
- assessment_id: source-roles
  area: provenance
  topic: Inherited source activity roles
  outcome: supported
  summary: The exact maintained row and current ChEBI ontology explain both retained
    roles and ANTIBACTERIAL filing. This supports source fidelity, not independent
    experimental confirmation.
  target_ids:
  - CHEBI:46765
  evidence_ids:
  - source
  - chebi
  - parent
- assessment_id: activity
  area: evidence
  topic: Exact-material antibacterial support
  outcome: unknown
  summary: No inspected primary experiment establishes the bare C6H7NO nucleus as
    antibacterial. The bounded search found distinct carboxylated antibiotics, substituted-drug
    assays, docking and class context. No inactivity conclusion or confirmed wrong
    role follows.
  target_ids:
  - CHEBI:46765
  evidence_ids:
  - literature-search
  - sq27860
  - plant2020
  - efflux2023
  - parent
- assessment_id: mechanism
  area: completeness
  topic: Targets, resistance and causal graph
  outcome: unknown
  summary: The native record makes no mechanism or target claims. Family PBP descriptions,
    meropenem docking and resistance profiles cannot fill these optional fields for
    the bare nucleus.
  target_ids:
  - CHEBI:46765
  evidence_ids:
  - record
  - efflux2023
  - adapter
- assessment_id: production
  area: completeness
  topic: Producer and biosynthesis
  outcome: unknown
  summary: Serratia/Erwinia evidence concerns the carboxylated SQ27860 molecule. No
    exact bare-nucleus producer or biosynthetic origin was established.
  target_ids:
  - CHEBI:46765
  evidence_ids:
  - sq27860
  - record
- assessment_id: ownership
  area: ownership
  topic: Maintained-source adjudication
  outcome: supported
  summary: Any future source-role or inclusion correction belongs to the maintained
    ChEBI source/extractor and documented decision layer; a native-only patch would
    be overwritten. Exact claim-level additions, if found, belong to the actual native
    record.
  target_ids:
  - CHEBI:46765
  evidence_ids:
  - source
  - local-search
- assessment_id: validation
  area: schema
  topic: Focused schema, strict, chemistry and history
  outcome: supported
  summary: Complete history was read and all actual focused gates pass. These do not
    close the exact-material experimental support gap.
  target_ids:
  - CHEBI:46765
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: bare-carbapenem-exact-activity-source-followup
  category: evidence
  severity: informational
  status: open
  certainty: provisional
  title: Resolve exact-nucleus activity support before extending inherited class-level
    biology
  description: The inherited ChEBI antibacterial role is source-attested, but the
    bare C6H7NO nucleus has no adopted citation and no exact positive experiment was
    established in the bounded search. Inspected near matches concern SQ27860/carboxylic
    acid, named substituted carbapenems or structural context. This is a conditional
    source-evidence follow-up, not proof of inactivity, a demand for optional fields,
    or a confirmed class-record error.
  target_ids:
  - CHEBI:46765
  field_paths:
  - activity_roles
  - source_concepts[0].role_terms
  - evidence
  evidence_ids:
  - source
  - parent
  - literature-search
  - sq27860
  - plant2020
  - efflux2023
  - pubchem
  rule_id: 'native-review-checklist: exact-material activity scope; no activity inferred
    solely from chemical family'
  native_severity: informational bounded exact-activity uncertainty
  normalization_reason: Source fidelity and exact chemical identity are supported.
    A bounded search failure cannot establish that the role is false or justify automatic
    exclusion.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Inherited identity and activity-role source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained role inheritance and exact-source policy
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Conditional grounding or exclusion decision after evidence adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regeneration after an authorized source decision
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/carbapenem.yaml
    role: Future exact-material primary evidence if independently established
actions:
- action_id: A1
  description: Adjudicate the inherited antibacterial role with exact-material evidence
    and preserve nucleus/drug boundaries.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:46765
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Inherited identity and activity-role source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained role inheritance and exact-source policy
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Conditional grounding or exclusion decision after evidence adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regeneration after an authorized source decision
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/carbapenem.yaml
    role: Future exact-material primary evidence if independently established
  acceptance_checks:
  - Seek an original experiment whose tested structure is the (5R) C6H7NO nucleus
    with full key YZBQHRLRFGPBSL-RXMQYKEDSA-N. Inspect the actual compound drawing
    and methods, not only a carbapenem title, broad-name database link or class annotation.
  - Keep the reviewed entity distinct from SQ27860/C7H7NO3, PubChem441133, meropenem,
    imipenem and the variable CHEBI46633 class. Do not import their MICs, producer
    organisms, PBP targets, efflux-pump docking or resistance observations.
  - If exact positive evidence is found, attach it at the narrow tested-material/activity
    claim using write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/carbapenem.yaml;
    preserve organism, method, endpoint and material stereochemistry. Do not promote
    to REVIEWED until native sign-off requirements are satisfied.
  - If a documented source adjudication establishes that the role applies only to
    substituted class members, implement an exact maintained-source correction or
    justified curation/decisions.tsv exclusion for antibioticmech:chebi-c1b974cf3a
    and regenerate through the documented pipeline. A zero-result literature query
    alone is insufficient grounds for exclusion.
  - After any separately authorized change, run the focused record validators, check
    role/source coherence and exact structure/mint, and run applicable shared gates.
limitations:
- All 13 initial input hashes were captured before assessment and remain unchanged.
  Complete native record, exact source row and relevant configuration, role-inheritance,
  extraction and seeding code were inspected.
- The adopted source contains zero citation leads. This review is partial because
  exact-material antibacterial activity, target, resistance and producer evidence
  remains unresolved, despite consistent official identity and source roles.
- The original SQ27860 paper was inspected for p653 identity, antibacterial statement
  and Figure 1, plus adjacent strain-description text, to resolve a near match. Its
  entire production/assay dataset was not independently reviewed for this distinct
  bare-nucleus record.
- The 2020 primary article main text was read in full. The 2023 primary main text
  and relevant antibiotic/docking tables were read. The 2025 secondary review was
  inspected only for abstract and relevant structural sections/caption; it is context
  rather than primary support.
- Exact EuropePMC searches are not a comprehensive literature inventory. Two patent
  abstracts concern substituted carboxylic acids and their full patents were not inspected.
  Broad PubChem literature/co-occurrence and patent counts were not treated as exact
  chemical experiments.
- The absence of a direct antibacterial experiment in this bounded review does not
  prove the bare nucleus inactive and does not itself overturn a reviewed ChEBI role
  or authorize exclusion.
- The batch020 locked environment lacks RDKit; chemistry used the batch019 interpreter
  against unchanged batch020 inputs. Native gene/protein/response assertions are absent,
  so no structured transcriptomic query was applicable.
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
