# Review of 2-heptyl-4-hydroxyquinoline: exact tautomer and bounded HHQ experiments

- Review: 20261021T070759Z-2-heptyl-4-hydroxyquinoline-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T06:59:25Z
- Finished UTC: 2026-10-21T07:07:59Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The seeded enol identity, structural parent, antibacterial role and provenance are consistent. Exact HHQ primary experiments support bounded antistaphylococcal growth effects and separately support quorum-signalling receptor agonism. No direct antibacterial molecular target is established. The record makes no erroneous mechanism assertion; optional evidence enrichment must preserve tautomer, assay, signalling and iron-binding boundaries. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire resolved record, all adopted citation abstracts, official identity and additional exact-compound primary assay/mechanistic context.

Selection: Seventeenth initially uncovered record in sorted corpus path order; seventh in batch 002.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:75306 | data/antibiotics/antibacterial/2-heptyl-4-hydroxyquinoline.yaml | generated | 2-heptyl-4-hydroxyquinoline |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema validation | passed | True | CHEBI:75306 | Actual target execution exited 0 with no validation errors. |
| Documented strict validation | passed | True | CHEBI:75306 | Actual target execution exited 0 with no validation errors. |
| Independent structure and minted identifier assertions | passed | False | CHEBI:75306 | Actual molecular and identifier assertions passed. |
| Structured source applicability | not_applicable | False | CHEBI:75306 | No gene, protein, regulator, pathway, stress response or dataset is asserted in this record. Literature gene names are contextual leads and do not constitute an existing expression claim. |
| Authoritative full QC | failed | True | CHEBI:75306 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:75306 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:75306 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:75306 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:75306 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:75306 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:75306 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:75306 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:75306 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral enol and tautomer boundary

identity: supported. Targets: CHEBI:75306.

The enol SMILES parses and agrees with identity fields. A shared Standard InChI with the lactam is not sufficient to merge source concepts or transfer tautomer-specific structural assertions.

### Broader chemical class and external mappings

grounding: supported. Targets: CHEBI:75306.

Monohydroxyquinoline is structurally appropriate and broader. CAS and Reaxys agree with the exact authority entry; registry access limits are retained.

### Ontology role and exact strain-specific experiments

evidence: supported. Targets: CHEBI:75306.

The source-backed antibacterial role is supported by an independently inspected exact-HHQ growth experiment. That fixed-dose result is not a species-wide MIC or clinical efficacy claim.

### Signalling receptor versus antibacterial target

completeness: unknown. Targets: CHEBI:75306.

MvfR/PqsR agonism, respiratory response and biosynthetic substrate relationships have distinct meanings. None of the inspected evidence establishes a direct antibacterial target. Native mechanism sign-off remains incomplete.

### Conflicting iron-binding descriptions

evidence: supported. Targets: CHEBI:75306.

The existing record does not assert iron chelation. Before adding that role or a causal mechanism, resolve the older description and later contrary statement with exact-compound binding evidence; do not transfer pseudan IX or PQS chemistry.

### Producer, resistance, quantities and graph objects

representation: not_applicable. Targets: CHEBI:75306.

Optional objects are unasserted and are not errors merely because absent. Future production, host-response or antimicrobial annotations must retain exact organism/strain, chemical identity and experimental context.

### Maintained source and native status

ownership: supported. Targets: CHEBI:75306.

Seeded provenance and history agree with inspected input ownership. No curation event or status promotion is warranted by review validation alone.

## Findings

### F1: Primary HHQ evidence can be added with explicit assay and mechanism boundaries

informational / open / confirmed; issue key: chebi-75306-hhq-assay-and-mechanism-boundaries.

The current source-backed seed is internally consistent. Optional enrichment can capture exact MRSA-M2 fixed-dose growth inhibition and separately labelled signalling evidence. It must not turn PqsR agonism into antibacterial receptor inhibition, PqsH substrate status into target inhibition, or disputed iron chemistry into an established mechanism.

## Recommended Actions And Acceptance Checks

### A1

During separately authorized curation, attach exact primary evidence and preserve fixed-dose growth, signalling and biosynthetic relationships separately. Resolve iron-binding conflicts before adding an iron-based mechanism, and retain the enol/lactam source boundary.

- The 50 micromolar MRSA-M2 result is labelled as a fixed-dose growth assay, never as an MIC; retain medium, iron condition, duration and control.
- If extracting optical-density metadata, reconcile Methods OD630 with the Figure3 caption OD600 rather than silently choosing one.
- No PqsD inhibitor, PqsH substrate relationship, PQS/HQNO activity or pseudan IX chelation is transferred to HHQ as a direct antibacterial target.
- Source tautomer concepts are not merged solely because Standard InChI normalizes mobile hydrogen.
- Use the validated writer and curation event, then focused validation, corpus reproduction and QC before any native REVIEWED promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/2-heptyl-4-hydroxyquinoline.yaml; Every field of the generated record | supports | Exact neutral enol identity, five aliases, one broader parent, antibacterial role, all structure fields, two registry xrefs, one source concept and three seed/reseed events were read. No mode, target, activity observation, producer, evidence object, resistance, clinical, graph or dataset assertion is present. |
| owner | data/raw/chebi_antimicrobials.tsv; Complete CHEBI:75306 row; conf/sources.yaml, manifest, extractor and seeder | supports | All seeded identity/role fields reproduce the adopted source. Ten PMID leads are retained in the source inventory, not copied as uninspected primary evidence objects. Additional authority roles are outside the adopted antimicrobial subset. Ignored-inclusive maintained-table searches found no exact matching decision or curator override. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:75306; Full official entry and outgoing ontology relations | supports | The exact label, five synonyms, enol SMILES, Standard InChI/key, C16H21NO, charge 0, masses and registry mappings agree. CHEBI:38775 is the broader monohydroxyquinoline parent. Explicit is-tautomer-of CHEBI:62219 preserves a source-level distinction despite a shared mobile-hydrogen Standard InChI. The authority also lists iron-chelator, metabolite and signalling roles outside the retained role subset. |
| role | https://www.ebi.ac.uk/chebi/CHEBI:33282; Antibacterial-agent definition and exact-compound outgoing relation | supports | The imported antibacterial role resolves and the exact compound is an incoming member. Source-derived classification is allowed without treating an ontology statement as a quantitative primary assay. |
| chemistry | RDKit and hashlib independent calculation; /private/tmp/am-review-session/017-chemistry.py; 017-chemistry.json | supports | Both encodings reproduce UYRHHBXYXSYGHA-UHFFFAOYSA-N, C16H21NO, charge 0, one fragment, no stereocenters and masses 243.350/243.162314292. The internal source-concept identifier is reproduced. This confirms internal consistency but does not collapse tautomer-specific ChEBI concepts. |
| pmid11846436 | PMID:11846436; Europe PMC core abstract and metadata; DOI:10.1006/bioo.2001.1225 | context_only | The principal direct iron-chelation experiments concern pseudan IX, the nonyl congener. Pseudan VII/HHQ was also isolated, but nonyl-congener experiments cannot establish an identical HHQ mechanism. |
| pmid14739337 | PMID:14739337; Europe PMC core abstract and metadata; DOI:10.1073/pnas.0307694100 | context_only | LC-MS, genetics and expression investigate HAQ production; HHQ is a precursor of PQS. Broad-family antibiotic or cytochrome statements are not exact HHQ target experiments. |
| pmid17083468 | PMID:17083468; Europe PMC core abstract and metadata; DOI:10.1111/j.1365-2958.2006.05462.x | context_only | The primary abstract describes HHQ interaction with the MvfR/PqsR ligand-binding domain and transcriptional agonism. This is quorum-signalling activation, not demonstrated antibacterial inhibition of that receptor. |
| pmid17126377 | PMID:17126377; Europe PMC core abstract and metadata; DOI:10.1016/j.bioorg.2006.10.004 | context_only | Pseudomonas inclusion particles contain HHQ and PQS as identified by NMR/MS. The abstract describes HHQ as iron-chelating and antibacterial; compound-specific binding methods require full-text adjudication, especially in light of later contradictory context. |
| pmid18539738 | PMID:18539738; Europe PMC core abstract and metadata; DOI:10.1128/JB.00400-08 | context_only | Burkholderia methylated HMAQ congeners and mutants establish related biosynthetic context. This is not automatic exact HHQ producer or target evidence. |
| pmid20102415 | PMID:20102415; Europe PMC core abstract and metadata; DOI:10.1111/j.1365-2567.2009.03160.x | context_only | HHQ/PQS suppress host NF-kappaB-dependent cytokine responses in tested immune-cell contexts. Host signalling is distinct from direct bacterial target inhibition. |
| pmid20662781 | PMID:20662781; Europe PMC core abstract and metadata; DOI:10.1111/j.1365-2958.2010.07303.x | context_only | PqsH uses HHQ, NADH and oxygen to produce PQS. HHQ is the biosynthetic substrate, not an established PqsH inhibitor. |
| pmid20738404 | PMID:20738404; Europe PMC core abstract and metadata; DOI:10.1111/j.1574-6976.2010.00247.x | context_only | This is a review of alkylquinolone signalling and is contextual, not a primary experiment. |
| pmid21189321 | PMID:21189321; Europe PMC core abstract and metadata; DOI:10.1128/IAI.00850-10 | context_only | OprF mutant phenotypes include changed virulence, reduced PQS and HHQ accumulation. This does not show direct HHQ binding to OprF. |
| pmid22992202 | PMID:22992202; Europe PMC core abstract and metadata; DOI:10.1021/ja3072397 | context_only | Other small molecules inhibit PqsD and reduce HHQ/PQS and biofilm. HHQ is a pathway product rather than the reported inhibitor. |
| antistaph | DOI:10.3389/fmicb.2016.01171; PMID:27512392; PMC4961689 full XML, Methods, Table1, Results, Figure3 caption and Discussion | supports | Individually applied HHQ at 50 micromolar suppressed MRSA-M2 growth in low-iron dialysed tryptic soy broth after 18 h at 37 C; experiments compared ethanol controls and 100 micromolar FeCl3 supplementation with three biological replicates. This is fixed-dose growth inhibition, not an MIC. TTC staining and small pflB/ldh expression changes are consistent with a respiratory/fermentative response without identifying a directly bound antibacterial enzyme. Mixtures and Pseudomonas supernatants remain separate experiments. |
| iron | DOI:10.1098/rspb.2017.0200; PMID:28404780; PMC5394672 full XML, Methods, Results and Figure1 caption | context_only | The paper states that HHQ does not bind iron. In PAO1 delta-pqsAH cultures in LB,37 C for14 h, HHQ showed no significant concentration-ordered trend in growth or pyochelin/pyoverdine output under the reported ordered-heterogeneity tests; the Discussion notes a small pyoverdine effect. This is not proof of zero effect and is not a new direct metal-binding measurement. Its iron statement differs from older descriptions and the authority role and merits exact-compound adjudication; the separate MRSA-M2 growth experiment is unaffected. |
| search | Ignored-inclusive local search and bounded free literature research; 017-local-hits.txt; 017-epmc.json; official ChEBI and full Europe PMC primary XML | context_only | Exact-compound literature was separated from PQS, HQNO, longer-chain pseudans, methylated HMAQs and synthetic Pqs inhibitors. No inspected exact antibacterial direct-binding mechanism was established. This is a bounded result, not universal absence. |

## Limits And Additional Notes

- The ten adopted PMID leads were inspected through Europe PMC core abstracts; not every full paper was available. Primary full sections of the 2016 antistaphylococcal and 2017 iron studies were separately inspected.
- Reaxys was corroborated through ChEBI rather than independently accessed. The official CAS mapping was inspected; a registry number alone cannot resolve this mobile-hydrogen tautomer boundary.
- HHQ iron binding is described inconsistently across the inspected authority and primary literature. The record retains only the antibacterial role, so no unasserted iron-chelator role is treated as an existing record error.
- Bounded searches do not prove that a direct antibacterial target is absent. Receptor agonism, a biosynthetic substrate relationship and growth effects require distinct evidence labels.
- The antibacterial paper uses the conventional HHQ identity; it does not measure an exclusively enol population in the assay. Retaining distinct ChEBI tautomer concepts is not evidence for tautomer-specific antibacterial activity.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Adversarial draft review verified all13 captured local input hashes and both primary XML hashes; checked exact-compound, fixed-dose, respiratory-response and ordered-trend scopes. Unsupported secondary_source evidence kind was changed to secondary-review discovery context using the allowed search kind.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T070759Z-2-heptyl-4-hydroxyquinoline-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Review of 2-heptyl-4-hydroxyquinoline: exact tautomer and bounded HHQ experiments'
started_at: '2026-10-21T06:59:25Z'
finished_at: '2026-10-21T07:07:59Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the target. Entire record, maintained
    inputs, independent chemistry, official identity, all adopted primary abstracts
    and relevant additional full primary sections were inspected.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The seeded enol identity, structural parent, antibacterial role and provenance
  are consistent. Exact HHQ primary experiments support bounded antistaphylococcal
  growth effects and separately support quorum-signalling receptor agonism. No direct
  antibacterial molecular target is established. The record makes no erroneous mechanism
  assertion; optional evidence enrichment must preserve tautomer, assay, signalling
  and iron-binding boundaries. Scientific assessment retains the stated evidence limits;
  full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/2-heptyl-4-hydroxyquinoline.yaml
    sha256: 3a1ee029ce91ccbd693c5359a2b949894199e9cc3103ed3f8f1edeea96ca2eda
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
- target_id: CHEBI:75306
  path: data/antibiotics/antibacterial/2-heptyl-4-hydroxyquinoline.yaml
  label: 2-heptyl-4-hydroxyquinoline
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
  description: Entire resolved record, all adopted citation abstracts, official identity
    and additional exact-compound primary assay/mechanistic context.
  selection: Seventeenth initially uncovered record in sorted corpus path order; seventh
    in batch 002.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:75306
checks:
- check_id: schema
  name: Documented schema validation
  status: passed
  required: true
  summary: Actual target execution exited 0 with no validation errors.
  target_ids:
  - CHEBI:75306
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/2-heptyl-4-hydroxyquinoline.yaml
  exit_code: 0
- check_id: strict
  name: Documented strict validation
  status: passed
  required: true
  summary: Actual target execution exited 0 with no validation errors.
  target_ids:
  - CHEBI:75306
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/2-heptyl-4-hydroxyquinoline.yaml --out /private/tmp/am-review-session/017-strict.tsv
  exit_code: 0
- check_id: chemistry
  name: Independent structure and minted identifier assertions
  status: passed
  required: false
  summary: Actual molecular and identifier assertions passed.
  target_ids:
  - CHEBI:75306
  command: .venv/bin/python /private/tmp/am-review-session/017-chemistry.py
  exit_code: 0
  evidence_ids:
  - chemistry
- check_id: imodulondb
  name: Structured source applicability
  status: not_applicable
  required: false
  summary: No gene, protein, regulator, pathway, stress response or dataset is asserted
    in this record. Literature gene names are contextual leads and do not constitute
    an existing expression claim.
  target_ids:
  - CHEBI:75306
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
  - CHEBI:75306
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
  - CHEBI:75306
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
  - CHEBI:75306
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
  - CHEBI:75306
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
  - CHEBI:75306
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
  - CHEBI:75306
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
  - CHEBI:75306
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
  - CHEBI:75306
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
  - CHEBI:75306
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/2-heptyl-4-hydroxyquinoline.yaml
  locator: Every field of the generated record
  accessed_at: '2026-10-21T07:06:12Z'
  support: supports
  summary: Exact neutral enol identity, five aliases, one broader parent, antibacterial
    role, all structure fields, two registry xrefs, one source concept and three seed/reseed
    events were read. No mode, target, activity observation, producer, evidence object,
    resistance, clinical, graph or dataset assertion is present.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Complete CHEBI:75306 row; conf/sources.yaml, manifest, extractor and seeder
  accessed_at: '2026-10-21T07:06:12Z'
  support: supports
  summary: All seeded identity/role fields reproduce the adopted source. Ten PMID
    leads are retained in the source inventory, not copied as uninspected primary
    evidence objects. Additional authority roles are outside the adopted antimicrobial
    subset. Ignored-inclusive maintained-table searches found no exact matching decision
    or curator override.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:75306
  locator: Full official entry and outgoing ontology relations
  accessed_at: '2026-10-21T07:06:12Z'
  support: supports
  summary: The exact label, five synonyms, enol SMILES, Standard InChI/key, C16H21NO,
    charge 0, masses and registry mappings agree. CHEBI:38775 is the broader monohydroxyquinoline
    parent. Explicit is-tautomer-of CHEBI:62219 preserves a source-level distinction
    despite a shared mobile-hydrogen Standard InChI. The authority also lists iron-chelator,
    metabolite and signalling roles outside the retained role subset.
- evidence_id: role
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:33282
  locator: Antibacterial-agent definition and exact-compound outgoing relation
  accessed_at: '2026-10-21T07:06:12Z'
  support: supports
  summary: The imported antibacterial role resolves and the exact compound is an incoming
    member. Source-derived classification is allowed without treating an ontology
    statement as a quantitative primary assay.
- evidence_id: chemistry
  kind: validation
  reference: RDKit and hashlib independent calculation
  locator: /private/tmp/am-review-session/017-chemistry.py; 017-chemistry.json
  accessed_at: '2026-10-21T07:06:12Z'
  support: supports
  summary: Both encodings reproduce UYRHHBXYXSYGHA-UHFFFAOYSA-N, C16H21NO, charge
    0, one fragment, no stereocenters and masses 243.350/243.162314292. The internal
    source-concept identifier is reproduced. This confirms internal consistency but
    does not collapse tautomer-specific ChEBI concepts.
  snapshot_sha256: 7661d93269f7f6dd9463b35935ab7d353af2ddbdf05758d1e00934d92335978c
- evidence_id: pmid11846436
  kind: primary_source
  reference: PMID:11846436
  locator: Europe PMC core abstract and metadata; DOI:10.1006/bioo.2001.1225
  accessed_at: '2026-10-21T07:06:12Z'
  support: context_only
  summary: The principal direct iron-chelation experiments concern pseudan IX, the
    nonyl congener. Pseudan VII/HHQ was also isolated, but nonyl-congener experiments
    cannot establish an identical HHQ mechanism.
- evidence_id: pmid14739337
  kind: primary_source
  reference: PMID:14739337
  locator: Europe PMC core abstract and metadata; DOI:10.1073/pnas.0307694100
  accessed_at: '2026-10-21T07:06:12Z'
  support: context_only
  summary: LC-MS, genetics and expression investigate HAQ production; HHQ is a precursor
    of PQS. Broad-family antibiotic or cytochrome statements are not exact HHQ target
    experiments.
- evidence_id: pmid17083468
  kind: primary_source
  reference: PMID:17083468
  locator: Europe PMC core abstract and metadata; DOI:10.1111/j.1365-2958.2006.05462.x
  accessed_at: '2026-10-21T07:06:12Z'
  support: context_only
  summary: The primary abstract describes HHQ interaction with the MvfR/PqsR ligand-binding
    domain and transcriptional agonism. This is quorum-signalling activation, not
    demonstrated antibacterial inhibition of that receptor.
- evidence_id: pmid17126377
  kind: primary_source
  reference: PMID:17126377
  locator: Europe PMC core abstract and metadata; DOI:10.1016/j.bioorg.2006.10.004
  accessed_at: '2026-10-21T07:06:12Z'
  support: context_only
  summary: Pseudomonas inclusion particles contain HHQ and PQS as identified by NMR/MS.
    The abstract describes HHQ as iron-chelating and antibacterial; compound-specific
    binding methods require full-text adjudication, especially in light of later contradictory
    context.
- evidence_id: pmid18539738
  kind: primary_source
  reference: PMID:18539738
  locator: Europe PMC core abstract and metadata; DOI:10.1128/JB.00400-08
  accessed_at: '2026-10-21T07:06:12Z'
  support: context_only
  summary: Burkholderia methylated HMAQ congeners and mutants establish related biosynthetic
    context. This is not automatic exact HHQ producer or target evidence.
- evidence_id: pmid20102415
  kind: primary_source
  reference: PMID:20102415
  locator: Europe PMC core abstract and metadata; DOI:10.1111/j.1365-2567.2009.03160.x
  accessed_at: '2026-10-21T07:06:12Z'
  support: context_only
  summary: HHQ/PQS suppress host NF-kappaB-dependent cytokine responses in tested
    immune-cell contexts. Host signalling is distinct from direct bacterial target
    inhibition.
- evidence_id: pmid20662781
  kind: primary_source
  reference: PMID:20662781
  locator: Europe PMC core abstract and metadata; DOI:10.1111/j.1365-2958.2010.07303.x
  accessed_at: '2026-10-21T07:06:12Z'
  support: context_only
  summary: PqsH uses HHQ, NADH and oxygen to produce PQS. HHQ is the biosynthetic
    substrate, not an established PqsH inhibitor.
- evidence_id: pmid20738404
  kind: search
  reference: PMID:20738404
  locator: Europe PMC core abstract and metadata; DOI:10.1111/j.1574-6976.2010.00247.x
  accessed_at: '2026-10-21T07:06:12Z'
  support: context_only
  summary: This is a review of alkylquinolone signalling and is contextual, not a
    primary experiment.
  search_scope: Europe PMC core metadata and abstract inspected for secondary-review
    citation discovery; not used as independent primary proof.
- evidence_id: pmid21189321
  kind: primary_source
  reference: PMID:21189321
  locator: Europe PMC core abstract and metadata; DOI:10.1128/IAI.00850-10
  accessed_at: '2026-10-21T07:06:12Z'
  support: context_only
  summary: OprF mutant phenotypes include changed virulence, reduced PQS and HHQ accumulation.
    This does not show direct HHQ binding to OprF.
- evidence_id: pmid22992202
  kind: primary_source
  reference: PMID:22992202
  locator: Europe PMC core abstract and metadata; DOI:10.1021/ja3072397
  accessed_at: '2026-10-21T07:06:12Z'
  support: context_only
  summary: Other small molecules inhibit PqsD and reduce HHQ/PQS and biofilm. HHQ
    is a pathway product rather than the reported inhibitor.
- evidence_id: antistaph
  kind: primary_source
  reference: DOI:10.3389/fmicb.2016.01171
  locator: PMID:27512392; PMC4961689 full XML, Methods, Table1, Results, Figure3 caption
    and Discussion
  accessed_at: '2026-10-21T07:06:12Z'
  support: supports
  summary: Individually applied HHQ at 50 micromolar suppressed MRSA-M2 growth in
    low-iron dialysed tryptic soy broth after 18 h at 37 C; experiments compared ethanol
    controls and 100 micromolar FeCl3 supplementation with three biological replicates.
    This is fixed-dose growth inhibition, not an MIC. TTC staining and small pflB/ldh
    expression changes are consistent with a respiratory/fermentative response without
    identifying a directly bound antibacterial enzyme. Mixtures and Pseudomonas supernatants
    remain separate experiments.
  snapshot_sha256: 896d46102031a0cae029c4c86c3c27bab1e5fe279d59157cb6d597782f691099
- evidence_id: iron
  kind: primary_source
  reference: DOI:10.1098/rspb.2017.0200
  locator: PMID:28404780; PMC5394672 full XML, Methods, Results and Figure1 caption
  accessed_at: '2026-10-21T07:06:12Z'
  support: context_only
  summary: The paper states that HHQ does not bind iron. In PAO1 delta-pqsAH cultures
    in LB,37 C for14 h, HHQ showed no significant concentration-ordered trend in growth
    or pyochelin/pyoverdine output under the reported ordered-heterogeneity tests;
    the Discussion notes a small pyoverdine effect. This is not proof of zero effect
    and is not a new direct metal-binding measurement. Its iron statement differs
    from older descriptions and the authority role and merits exact-compound adjudication;
    the separate MRSA-M2 growth experiment is unaffected.
  snapshot_sha256: bf2bf34e87db9dca10e9da8eb23890520745a1bd66c72452675bb16fe7f35269
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local search and bounded free literature research
  locator: 017-local-hits.txt; 017-epmc.json; official ChEBI and full Europe PMC primary
    XML
  accessed_at: '2026-10-21T07:06:12Z'
  support: context_only
  summary: Exact-compound literature was separated from PQS, HQNO, longer-chain pseudans,
    methylated HMAQs and synthetic Pqs inhibitors. No inspected exact antibacterial
    direct-binding mechanism was established. This is a bounded result, not universal
    absence.
  search_scope: rg --no-ignore --hidden searched exact CHEBI identifier, label and
    slug across the task worktree, including ignored/hidden files except .git and
    .venv. Maintained curation tables were separately searched for identity and minted
    ID. Free web queries covered exact HHQ name, mechanism, antibacterial activity
    and iron chelation; all ten adopted abstracts were read through Europe PMC core,
    then relevant 2016/2017 primary full sections were retrieved. No paid access or
    author contact occurred.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral enol and tautomer boundary
  outcome: supported
  summary: The enol SMILES parses and agrees with identity fields. A shared Standard
    InChI with the lactam is not sufficient to merge source concepts or transfer tautomer-specific
    structural assertions.
  target_ids:
  - CHEBI:75306
  evidence_ids:
  - record
  - chebi
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Broader chemical class and external mappings
  outcome: supported
  summary: Monohydroxyquinoline is structurally appropriate and broader. CAS and Reaxys
    agree with the exact authority entry; registry access limits are retained.
  target_ids:
  - CHEBI:75306
  evidence_ids:
  - record
  - chebi
- assessment_id: activity
  area: evidence
  topic: Ontology role and exact strain-specific experiments
  outcome: supported
  summary: The source-backed antibacterial role is supported by an independently inspected
    exact-HHQ growth experiment. That fixed-dose result is not a species-wide MIC
    or clinical efficacy claim.
  target_ids:
  - CHEBI:75306
  evidence_ids:
  - role
  - antistaph
- assessment_id: mechanism
  area: completeness
  topic: Signalling receptor versus antibacterial target
  outcome: unknown
  summary: MvfR/PqsR agonism, respiratory response and biosynthetic substrate relationships
    have distinct meanings. None of the inspected evidence establishes a direct antibacterial
    target. Native mechanism sign-off remains incomplete.
  target_ids:
  - CHEBI:75306
  evidence_ids:
  - pmid17083468
  - pmid20662781
  - pmid22992202
  - antistaph
- assessment_id: iron-boundary
  area: evidence
  topic: Conflicting iron-binding descriptions
  outcome: supported
  summary: The existing record does not assert iron chelation. Before adding that
    role or a causal mechanism, resolve the older description and later contrary statement
    with exact-compound binding evidence; do not transfer pseudan IX or PQS chemistry.
  target_ids:
  - CHEBI:75306
  evidence_ids:
  - chebi
  - pmid11846436
  - pmid17126377
  - iron
- assessment_id: optional
  area: representation
  topic: Producer, resistance, quantities and graph objects
  outcome: not_applicable
  summary: Optional objects are unasserted and are not errors merely because absent.
    Future production, host-response or antimicrobial annotations must retain exact
    organism/strain, chemical identity and experimental context.
  target_ids:
  - CHEBI:75306
  evidence_ids:
  - record
  - antistaph
  - pmid20102415
  - pmid18539738
- assessment_id: provenance
  area: ownership
  topic: Maintained source and native status
  outcome: supported
  summary: Seeded provenance and history agree with inspected input ownership. No
    curation event or status promotion is warranted by review validation alone.
  target_ids:
  - CHEBI:75306
  evidence_ids:
  - record
  - owner
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-75306-hhq-assay-and-mechanism-boundaries
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Primary HHQ evidence can be added with explicit assay and mechanism boundaries
  description: The current source-backed seed is internally consistent. Optional enrichment
    can capture exact MRSA-M2 fixed-dose growth inhibition and separately labelled
    signalling evidence. It must not turn PqsR agonism into antibacterial receptor
    inhibition, PqsH substrate status into target inhibition, or disputed iron chemistry
    into an established mechanism.
  target_ids:
  - CHEBI:75306
  field_paths:
  - evidence
  - activity_spectrum
  - mode_of_action
  - mode_of_action_notes
  - discussions
  evidence_ids:
  - record
  - antistaph
  - pmid17083468
  - pmid20662781
  - pmid22992202
  - iron
  - chebi
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-heptyl-4-hydroxyquinoline.yaml
    role: Curator-owned evidence, discussions, assay and mechanism annotations through
      validated writer and curation event
  rule_id: 'native-review-checklist: Evidence standard, Activity and Mode of action'
  native_severity: informational optional evidence enrichment
  normalization_reason: No false existing mechanism, quantitative assay or iron-binding
    assertion was demonstrated. Empty optional objects are not a schema defect; unresolved
    mechanism prevents native promotion without invalidating the source-backed identity.
actions:
- action_id: A1
  description: During separately authorized curation, attach exact primary evidence
    and preserve fixed-dose growth, signalling and biosynthetic relationships separately.
    Resolve iron-binding conflicts before adding an iron-based mechanism, and retain
    the enol/lactam source boundary.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:75306
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-heptyl-4-hydroxyquinoline.yaml
    role: Curator-owned evidence, discussions, assay and mechanism annotations through
      validated writer and curation event
  acceptance_checks:
  - The 50 micromolar MRSA-M2 result is labelled as a fixed-dose growth assay, never
    as an MIC; retain medium, iron condition, duration and control.
  - If extracting optical-density metadata, reconcile Methods OD630 with the Figure3
    caption OD600 rather than silently choosing one.
  - No PqsD inhibitor, PqsH substrate relationship, PQS/HQNO activity or pseudan IX
    chelation is transferred to HHQ as a direct antibacterial target.
  - Source tautomer concepts are not merged solely because Standard InChI normalizes
    mobile hydrogen.
  - Use the validated writer and curation event, then focused validation, corpus reproduction
    and QC before any native REVIEWED promotion.
limitations:
- The ten adopted PMID leads were inspected through Europe PMC core abstracts; not
  every full paper was available. Primary full sections of the 2016 antistaphylococcal
  and 2017 iron studies were separately inspected.
- Reaxys was corroborated through ChEBI rather than independently accessed. The official
  CAS mapping was inspected; a registry number alone cannot resolve this mobile-hydrogen
  tautomer boundary.
- HHQ iron binding is described inconsistently across the inspected authority and
  primary literature. The record retains only the antibacterial role, so no unasserted
  iron-chelator role is treated as an existing record error.
- Bounded searches do not prove that a direct antibacterial target is absent. Receptor
  agonism, a biosynthetic substrate relationship and growth effects require distinct
  evidence labels.
- The antibacterial paper uses the conventional HHQ identity; it does not measure
  an exclusively enol population in the assay. Retaining distinct ChEBI tautomer concepts
  is not evidence for tautomer-specific antibacterial activity.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Adversarial draft review verified all13 captured local input hashes and both primary
  XML hashes; checked exact-compound, fixed-dose, respiratory-response and ordered-trend
  scopes. Unsupported secondary_source evidence kind was changed to secondary-review
  discovery context using the allowed search kind.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
