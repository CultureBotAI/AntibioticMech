# 1-hydroxycrisamicin A: structure, source claims and primary assay review

- Review: 20261021T065006Z-1-hydroxycrisamicin-a
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T06:44:08Z
- Finished UTC: 2026-10-21T06:50:06Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact hydroxylated dimer, producer context and antibacterial definition are supported. One minor finding identifies unstructured primary producer and activity evidence; assay details need recovery before quantitative curation. The structural-class ring terminology and antimicrobial mechanism remain unresolved within the stated limits.

## Scope And Provenance

Full one-record field review, source row and exact original isolation/activity paper.

Selection: Sixth unreviewed path selected in sorted data/antibiotics/**/*.yaml order; one resolved target in this bundle.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:66042 | data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml | generated | 1-hydroxycrisamicin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema record validation | passed | True | CHEBI:66042 | Actual target execution exited0 with no issues. |
| strict record validation | passed | True | CHEBI:66042 | Actual target execution exited0 with no issues. |
| Structured expression adapter applicability | not_applicable | False | CHEBI:66042 | No gene, protein, regulator or expression dataset is asserted; chemical identity and isolation cannot be inferred from module membership. |
| Authoritative full QC | failed | True | CHEBI:66042 | Exited 2 at test collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This is not a scientific failure of this record. |
| Generated corpus reproduction | passed | True | CHEBI:66042 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:66042 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Full closed-schema validation | passed | True | CHEBI:66042 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:66042 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:66042 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:66042 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:66042 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. No invented per-record validator. |

## Scientific And Domain Assessments

### Exact structure and congener distinction

identity: supported. Targets: CHEBI:66042.

The record denotes the1-hydroxy derivative, not the9-hydroxy isomer or parent crisamicin A; source data and independent chemistry agree.

### Filing class and primary activity scope

scope: supported. Targets: CHEBI:66042.

The antibacterial role is supported. The definition uses a tested-group qualification; tested inactivity cannot be generalized to all Gram-negative bacteria or fungi.

### Structural parent and descriptor scope

nomenclature: unknown. Targets: CHEBI:66042.

Functional-group parents fit. The official authority assigns the heterotetracyclic parent. The structure contains two linked four-ring systems; without a definition of how the ontology counts linked systems, total ring count does not establish a classification error.

### Producer and quantitative activity

completeness: concern. Targets: CHEBI:66042.

The definition has genuine primary support, but claim-local producer/activity objects are unpopulated. Missing assay metadata limits immediate numeric curation.

### Mode, target scope and molecular target

evidence: unknown. Targets: CHEBI:66042.

No mechanism/target is asserted. Neither chemical-family membership nor antibacterial MIC establishes a specific target. Native REVIEWED gate4 remains unmet.

### Resistance, clinical status, datasets and graph

scope: not_applicable. Targets: CHEBI:66042.

No such claims occur in this record; no defect follows solely from optional-field absence.

### Provenance and status

ownership: supported. Targets: CHEBI:66042.

SEEDED and three source-only events accurately describe generated ownership. Classification/source identity fixes must persist through regeneration.

## Findings

### primary-gap: Primary producer and assay context remains unstructured

minor / open / confirmed; issue key: chebi-66042-primary-context-unstructured.

The definition is source-supported, but the record has no claim-level representation of the reported biological evidence. This is a bounded enrichment opportunity, not a schema failure. Missing assay procedure must remain explicit.

## Recommended Actions And Acceptance Checks

### assess-primary-curation

Curate producer context and preserve the original strain label. Recover the MIC method from original supporting material or report its absence explicitly; retain reported qualifiers and avoid species-wide extrapolation.

- Each added object has its own inspected citation and exact compound/organism context.
- No inferred assay method or target is inserted; quantitative entries preserve units and qualifiers.
- Use validated writer/event; run target strict validation, verify-corpus and QC after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml; entire generated YAML | supports | One ChEBI identity/source, systematic synonym, five structural parents, antibacterial role, exact structure, one registry link and three seed/reseed events. Definition contains organism and activity context; no structured mechanism, target, activity, resistance, producer, clinical, dataset or graph is asserted. |
| seed | data/raw/chebi_antimicrobials.tsv; CHEBI:66042 row; conf/sources.yaml priority; seed_from_sources.py mechanism-role mapping | supports | Source row preserves exact structure and cites PMID9531992. Empty mechanism_role_ids explains absent mode without seed drift. Source/extractor/seeder own identity, definition, parents and classification; curator-owned additions must use validated writer and curation event. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:66042; Identity/properties, ontology, source species and registry sections; retrieved HTML | supports | Exact formula C32H22O13, neutral charge, key RGOCVNGEBMGCNA-WIDQCZIUSA-N, systematic stereochemical synonym, masses and Reaxys8180397 match. Parent IDs resolve to p-quinones, organic hydroxy compound, cyclic ether, gamma-lactone and organic heterotetracyclic compound. Antibacterial role and Micromonospora strainSA246 are present. |
| parent | https://www.ebi.ac.uk/chebi/CHEBI:38163; Name and outgoing is-a relation | context_only | The entry is named organic heterotetracyclic compound and lies under organic heteropolycyclic compound; the displayed page supplies no clarifying definition of total molecule versus individual ring-system counting. |
| chemistry | RDKit2026.3.5; Independent calculation for the target; /private/tmp/am-review-session/006-chemistry.json | supports | Both representations regenerate the stored key. Formula/charge and masses614.515/614.106040764 agree. Six assigned S stereocenters agree with the systematic synonym. The connected dimer has eight independent rings. |
| primary | https://www.jstage.jst.go.jp/article/antibiotics1968/51/1/51_1_82/_pdf; DOI10.7164/antibiotics.51.82; pp82–84; Figures1/3 and Table3 visually read | supports | The paper isolates compound1 from Micromonospora SA246 and distinguishes it from crisamicin A, crisamicin C and 9-hydroxycrisamicin A by spectroscopy. Table3 reports Gram-positive MICs0.78–3.12µg/mL; tested Gram-negative and fungal MICs exceed100µg/mL. The short report does not clearly state the MIC procedure or identify a molecular target. |
| pubmed | https://pubmed.ncbi.nlm.nih.gov/9531992/; Title, journal, DOI and correction metadata | supports | PubMed resolves the adopted PMID to the same1998 isolation paper and DOI. Its correction concerns an author name, not an experimental or chemical-identity correction. |
| search | local ignored-inclusive search and free web literature search; 006-local-hits.txt; exact name and primary citation queries | context_only | Search locates generated record, adopted row, projections, queues and historical report. Only the newly inspected primary paper supports experimental conclusions here; vendors and snippets were used as discovery leads, not proof. |

## Limits And Additional Notes

- The original three-page paper reports MICs without a clearly specified antimicrobial assay procedure; do not invent broth, medium, incubation or inoculum details.
- Reaxys8180397 was checked through ChEBI, not by accessing the licensed registry.
- Absolute stereochemistry is corroborated by stored SMILES/InChI agreement and ChEBI. The 1998 paper supports connectivity by NMR/comparison with crisamicin A; this review does not independently reconstruct every historical absolute-configuration assignment.
- Mechanism and direct target remain unresolved in the inspected scope. No exhaustive absence of later mechanistic evidence is claimed.
- CHEBI:38163 supplies no inspected definition resolving whole-molecule versus ring-system counting. Eight calculated rings across two linked tetracyclic systems are insufficient to establish an ontology error; no corrective finding is assigned.
- Authoritative just qc failed during collection because the pinned SciPy 1.15.3 native library has an invalid Mach-O section on this platform; identical pinned version also failed under Python 3.10. No dependency versions were changed. Full closed-schema, reproduction and corpus-integrity gates passed independently; these do not replace full QC.
- Bundle completion is partial because full repository QC is not available on this runtime; the selected record was read and assessed in full. A saved review does not promote scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T065006Z-1-hydroxycrisamicin-a
kind: record
repository: CultureBotAI/AntibioticMech
title: '1-hydroxycrisamicin A: structure, source claims and primary assay review'
started_at: '2026-10-21T06:44:08Z'
finished_at: '2026-10-21T06:50:06Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not generate or curate the target. Entire target
    and primary source were read; original structure/assay table was visually checked.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The exact hydroxylated dimer, producer context and antibacterial definition
  are supported. One minor finding identifies unstructured primary producer and activity
  evidence; assay details need recovery before quantitative curation. The structural-class
  ring terminology and antimicrobial mechanism remain unresolved within the stated
  limits.
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
  - path: data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml
    sha256: 1e50ea28aa0682b85bc38e862dbb9c92b598427652871715f310ba9fff44c65d
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
- target_id: CHEBI:66042
  path: data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml
  label: 1-hydroxycrisamicin A
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
  description: Full one-record field review, source row and exact original isolation/activity
    paper.
  selection: Sixth unreviewed path selected in sorted data/antibiotics/**/*.yaml order;
    one resolved target in this bundle.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:66042
checks:
- check_id: schema
  name: schema record validation
  status: passed
  required: true
  summary: Actual target execution exited0 with no issues.
  target_ids:
  - CHEBI:66042
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml
  exit_code: 0
- check_id: strict
  name: strict record validation
  status: passed
  required: true
  summary: Actual target execution exited0 with no issues.
  target_ids:
  - CHEBI:66042
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml --out /private/tmp/am-review-session/006-strict.tsv
  exit_code: 0
- check_id: imodulondb
  name: Structured expression adapter applicability
  status: not_applicable
  required: false
  summary: No gene, protein, regulator or expression dataset is asserted; chemical
    identity and isolation cannot be inferred from module membership.
  target_ids:
  - CHEBI:66042
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at test collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This is not a scientific
    failure of this record.'
  target_ids:
  - CHEBI:66042
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just qc
  exit_code: 2
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all 2939 records.
- check_id: shared-verify-corpus
  name: Generated corpus reproduction
  status: passed
  required: true
  summary: 2939 expected and present; zero missing, unexpected, drifted fields or
    lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic
    retained.
  target_ids:
  - CHEBI:66042
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just verify-corpus
    --summary
  exit_code: 0
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all 2939 records.
- check_id: shared-review-queue
  name: Native review-readiness inventory
  status: passed
  required: false
  summary: 2859 native unsigned readiness rows written; this status queue does not
    determine structured-review coverage.
  target_ids:
  - CHEBI:66042
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just review-queue
    --limit 0 --tsv /private/tmp/am-review-session/native-queue.tsv
  exit_code: 0
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all 2939 records.
- check_id: shared-validate-all
  name: Full closed-schema validation
  status: passed
  required: true
  summary: 2939 files, zero ERROR rows.
  target_ids:
  - CHEBI:66042
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-all
    --quiet --workers 2 --out /private/tmp/am-review-session/corpus-validation.tsv
  exit_code: 0
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all 2939 records.
- check_id: shared-chemical-map-check
  name: Chemical map consistency
  status: failed
  required: false
  summary: Exited 1 on the same pinned SciPy native library import failure.
  target_ids:
  - CHEBI:66042
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just chemical-map-check
  exit_code: 1
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all 2939 records.
- check_id: shared-render-check
  name: Generated site consistency
  status: passed
  required: false
  summary: 2939 compound pages and seven class pages current.
  target_ids:
  - CHEBI:66042
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just render-check
  exit_code: 0
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all 2939 records.
- check_id: shared-report
  name: Corpus statistics
  status: passed
  required: false
  summary: Corpus report completed successfully.
  target_ids:
  - CHEBI:66042
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just report
  exit_code: 0
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all 2939 records.
- check_id: shared-corpus-integrity
  name: Full-corpus history/evidence/reference invariants
  status: passed
  required: true
  summary: 23 full-corpus integrity tests passed, including seed history, evidence
    placement and internal references. No invented per-record validator.
  target_ids:
  - CHEBI:66042
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml
  locator: entire generated YAML
  accessed_at: '2026-10-21T06:46:37Z'
  support: supports
  summary: One ChEBI identity/source, systematic synonym, five structural parents,
    antibacterial role, exact structure, one registry link and three seed/reseed events.
    Definition contains organism and activity context; no structured mechanism, target,
    activity, resistance, producer, clinical, dataset or graph is asserted.
- evidence_id: seed
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: CHEBI:66042 row; conf/sources.yaml priority; seed_from_sources.py mechanism-role
    mapping
  accessed_at: '2026-10-21T06:46:37Z'
  support: supports
  summary: Source row preserves exact structure and cites PMID9531992. Empty mechanism_role_ids
    explains absent mode without seed drift. Source/extractor/seeder own identity,
    definition, parents and classification; curator-owned additions must use validated
    writer and curation event.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:66042
  locator: Identity/properties, ontology, source species and registry sections; retrieved
    HTML
  accessed_at: '2026-10-21T06:46:37Z'
  support: supports
  summary: Exact formula C32H22O13, neutral charge, key RGOCVNGEBMGCNA-WIDQCZIUSA-N,
    systematic stereochemical synonym, masses and Reaxys8180397 match. Parent IDs
    resolve to p-quinones, organic hydroxy compound, cyclic ether, gamma-lactone and
    organic heterotetracyclic compound. Antibacterial role and Micromonospora strainSA246
    are present.
  snapshot_sha256: 9882f41aadfaa6cafe5840ba9096a9739c8a7ed7c698b67e33554a2327fffb93
- evidence_id: parent
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:38163
  locator: Name and outgoing is-a relation
  accessed_at: '2026-10-21T06:46:37Z'
  support: context_only
  summary: The entry is named organic heterotetracyclic compound and lies under organic
    heteropolycyclic compound; the displayed page supplies no clarifying definition
    of total molecule versus individual ring-system counting.
  snapshot_sha256: 8939f4446bc92dbcdf76910b570c3ca96bba343bc2ceb231bf4b2121d8cc467e
- evidence_id: chemistry
  kind: validation
  reference: RDKit2026.3.5
  locator: Independent calculation for the target; /private/tmp/am-review-session/006-chemistry.json
  accessed_at: '2026-10-21T06:46:37Z'
  support: supports
  summary: Both representations regenerate the stored key. Formula/charge and masses614.515/614.106040764
    agree. Six assigned S stereocenters agree with the systematic synonym. The connected
    dimer has eight independent rings.
  snapshot_sha256: 6a5afd0e3d335fd639bb4ba84f733cbd51cd3437c32c6a86b7cb140b83482e7b
- evidence_id: primary
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/antibiotics1968/51/1/51_1_82/_pdf
  locator: DOI10.7164/antibiotics.51.82; pp82–84; Figures1/3 and Table3 visually read
  accessed_at: '2026-10-21T06:46:37Z'
  support: supports
  summary: The paper isolates compound1 from Micromonospora SA246 and distinguishes
    it from crisamicin A, crisamicin C and 9-hydroxycrisamicin A by spectroscopy.
    Table3 reports Gram-positive MICs0.78–3.12µg/mL; tested Gram-negative and fungal
    MICs exceed100µg/mL. The short report does not clearly state the MIC procedure
    or identify a molecular target.
  snapshot_sha256: 77323ebea5b7889672b3369b5683098ced0d9c0458febcdd75cc2101f6553dec
- evidence_id: pubmed
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/9531992/
  locator: Title, journal, DOI and correction metadata
  accessed_at: '2026-10-21T06:46:37Z'
  support: supports
  summary: PubMed resolves the adopted PMID to the same1998 isolation paper and DOI.
    Its correction concerns an author name, not an experimental or chemical-identity
    correction.
- evidence_id: search
  kind: search
  reference: local ignored-inclusive search and free web literature search
  locator: 006-local-hits.txt; exact name and primary citation queries
  accessed_at: '2026-10-21T06:46:37Z'
  support: context_only
  summary: Search locates generated record, adopted row, projections, queues and historical
    report. Only the newly inspected primary paper supports experimental conclusions
    here; vendors and snippets were used as discovery leads, not proof.
  search_scope: rg --no-ignore --hidden exact CHEBI:66042, 1-hydroxycrisamicin A and
    slug across isolated clone except .git and .venv. Free web exact-name search;
    official ChEBI HTML fetched with curl after web-tool access failed; J-STAGE primary
    PDF downloaded and read in full.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact structure and congener distinction
  outcome: supported
  summary: The record denotes the1-hydroxy derivative, not the9-hydroxy isomer or
    parent crisamicin A; source data and independent chemistry agree.
  target_ids:
  - CHEBI:66042
  evidence_ids:
  - record
  - chebi
  - chemistry
  - primary
- assessment_id: roles
  area: scope
  topic: Filing class and primary activity scope
  outcome: supported
  summary: The antibacterial role is supported. The definition uses a tested-group
    qualification; tested inactivity cannot be generalized to all Gram-negative bacteria
    or fungi.
  target_ids:
  - CHEBI:66042
  evidence_ids:
  - record
  - seed
  - chebi
  - primary
- assessment_id: parents
  area: nomenclature
  topic: Structural parent and descriptor scope
  outcome: unknown
  summary: Functional-group parents fit. The official authority assigns the heterotetracyclic
    parent. The structure contains two linked four-ring systems; without a definition
    of how the ontology counts linked systems, total ring count does not establish
    a classification error.
  target_ids:
  - CHEBI:66042
  evidence_ids:
  - record
  - parent
  - chemistry
  - primary
- assessment_id: evidence
  area: completeness
  topic: Producer and quantitative activity
  outcome: concern
  summary: The definition has genuine primary support, but claim-local producer/activity
    objects are unpopulated. Missing assay metadata limits immediate numeric curation.
  target_ids:
  - CHEBI:66042
  evidence_ids:
  - record
  - primary
- assessment_id: mechanism
  area: evidence
  topic: Mode, target scope and molecular target
  outcome: unknown
  summary: No mechanism/target is asserted. Neither chemical-family membership nor
    antibacterial MIC establishes a specific target. Native REVIEWED gate4 remains
    unmet.
  target_ids:
  - CHEBI:66042
  evidence_ids:
  - record
  - primary
  - seed
- assessment_id: optional
  area: scope
  topic: Resistance, clinical status, datasets and graph
  outcome: not_applicable
  summary: No such claims occur in this record; no defect follows solely from optional-field
    absence.
  target_ids:
  - CHEBI:66042
  evidence_ids:
  - record
- assessment_id: audit
  area: ownership
  topic: Provenance and status
  outcome: supported
  summary: SEEDED and three source-only events accurately describe generated ownership.
    Classification/source identity fixes must persist through regeneration.
  target_ids:
  - CHEBI:66042
  evidence_ids:
  - record
  - seed
findings:
- finding_id: primary-gap
  issue_key: chebi-66042-primary-context-unstructured
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Primary producer and assay context remains unstructured
  description: The definition is source-supported, but the record has no claim-level
    representation of the reported biological evidence. This is a bounded enrichment
    opportunity, not a schema failure. Missing assay procedure must remain explicit.
  target_ids:
  - CHEBI:66042
  field_paths:
  - producer_organisms
  - activity_spectrum
  - evidence
  - discussions
  evidence_ids:
  - record
  - primary
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml
    role: Future curator-owned producer, activity, evidence and discussion through
      native validated writer/event
actions:
- action_id: assess-primary-curation
  description: Curate producer context and preserve the original strain label. Recover
    the MIC method from original supporting material or report its absence explicitly;
    retain reported qualifiers and avoid species-wide extrapolation.
  finding_ids:
  - primary-gap
  target_ids:
  - CHEBI:66042
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/1-hydroxycrisamicin-a.yaml
    role: Future curator-owned producer, activity, evidence and discussion through
      native validated writer/event
  acceptance_checks:
  - Each added object has its own inspected citation and exact compound/organism context.
  - No inferred assay method or target is inserted; quantitative entries preserve
    units and qualifiers.
  - Use validated writer/event; run target strict validation, verify-corpus and QC
    after separately authorized curation.
limitations:
- The original three-page paper reports MICs without a clearly specified antimicrobial
  assay procedure; do not invent broth, medium, incubation or inoculum details.
- Reaxys8180397 was checked through ChEBI, not by accessing the licensed registry.
- Absolute stereochemistry is corroborated by stored SMILES/InChI agreement and ChEBI.
  The 1998 paper supports connectivity by NMR/comparison with crisamicin A; this review
  does not independently reconstruct every historical absolute-configuration assignment.
- Mechanism and direct target remain unresolved in the inspected scope. No exhaustive
  absence of later mechanistic evidence is claimed.
- CHEBI:38163 supplies no inspected definition resolving whole-molecule versus ring-system
  counting. Eight calculated rings across two linked tetracyclic systems are insufficient
  to establish an ontology error; no corrective finding is assigned.
- Authoritative just qc failed during collection because the pinned SciPy 1.15.3 native
  library has an invalid Mach-O section on this platform; identical pinned version
  also failed under Python 3.10. No dependency versions were changed. Full closed-schema,
  reproduction and corpus-integrity gates passed independently; these do not replace
  full QC.
notes:
- Bundle completion is partial because full repository QC is not available on this
  runtime; the selected record was read and assessed in full. A saved review does
  not promote scientific status.
```
