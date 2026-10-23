# Cefdaloxime: coherent neutral acid with an anion-form exact synonym

- Review: 20261021T111921Z-cefdaloxime-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:55:31Z
- Finished UTC: 2026-10-21T11:19:21Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact neutral cefdaloxime graph and antibacterial role are supported. One source-imported exact synonym ends in carboxylate despite the neutral carboxylic-acid structure. A minor naming correction is required; original susceptibility abstracts support only their historical assay and population scope.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 217; one exact record in path order, captured before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:140109 | data/antibiotics/antibacterial/cefdaloxime.yaml | generated | cefdaloxime |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:140109 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:140109 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:140109 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:140109 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:140109 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:140109 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:140109 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:140109 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:140109 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:140109 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:140109 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:140109 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Maintained ownership and source history

provenance: supported. Targets: CHEBI:140109.

Source concepts, minted identifiers and history are coherent. Source-origin corrections require regeneration; new primary observations require the validated native writer and curation event.

### Focused native gates

schema: supported. Targets: CHEBI:140109.

Documented schema/strict checks and independent native chemistry pass. These do not validate every external cross-reference or confer scientific sign-off.

### Exact acid, synonyms and groundings

identity: concern. Targets: CHEBI:140109.

The chemical graph, CAS resolution and INN identity agree, but the imported standalone carboxylate name denotes the anionic form without an ester substituent or balancing cation.

### Antibacterial role and historical assays

evidence: supported. Targets: CHEBI:140109.

Exact-compound primary abstracts support antibacterial activity while exposing medium, organism and formulation limits. Tentative historical disk criteria are not current clinical standards.

### Mechanism, producer, clinical status and causal graph

completeness: unknown. Targets: CHEBI:140109.

These optional fields are unpopulated; no named native protein/gene/pathway claim requires a structured adapter. No direct exact-compound PBP experiment or natural producer was established in this bounded review.

## Findings

### F1: Correct the anion-form synonym attached to neutral cefdaloxime

minor / open / confirmed; issue key: cefdaloxime-carboxylate-exact-synonym.

synonyms[2] ends in cepham-4-carboxylate and contains no esterifying group, whereas the native graph has COOH, charge 0 and formula C14H15N5O6S2. The source and current ChEBI repeat the mismatch; the other systematic synonym and WHO INN specify the acid. This is a nomenclature defect, not evidence that the stored structure is the wrong antibiotic.

## Recommended Actions And Acceptance Checks

### A1

Correct the anion-form synonym attached to neutral cefdaloxime

- Reconcile the source synonym with the exact neutral acid; use a verified carboxylic-acid name or suppress the anion name from exact synonyms.
- Preserve the supported structure, full key and stereo. Do not change the record to an anion or infer salt identity from this naming error.
- Implement through a maintained source/extraction/decision correction and regenerate; preserve original provenance and inspect the exact diff. Do not patch generated YAML alone.
- Run focused schema/strict and independent chemistry, verify-corpus, and applicable shared gates after any separately authorized correction.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cefdaloxime.yaml; Complete YAML, including all source concepts and history events. | supports | Read every native field and retained assertion. This review does not change the generated record or promote SEEDED status. |
| source | data/raw/chebi_antimicrobials.tsv; Exact maintained rows in 217-raw-rows.json; applicable extraction, join and seeding code. | supports | The maintained rows reproduce the native source-owned content. Initial input hashes are retained; actual additional owners were appended from a supplemental capture before detailed judgment. Corrections belong at the reproducible source/decision boundary. |
| chemistry | 217-chemistry.json; 217-220-external-chemistry.json; Independent RDKit parse of native SMILES/InChI and inspected official structures. | supports | Native encodings reproduce HOGISBSFFHDTRM-GHXIOONMSA-N, C14H15N5O6S2, charge 0, masses and two R centres. Oxime geometry is Z. The batch019 interpreter operated on unchanged batch022 inputs because batch022 has no RDKit. |
| search | 217-local-hits.txt; 217-owner-hits.txt; Exact identifier, label, key and slug; hidden and ignored files included. | supports | The complete native record, maintained inputs, generated references and related chemical forms were distinguished. No exact corrective decision was identified in the inspected maintained inputs. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:140109; https://pubchem.ncbi.nlm.nih.gov/compound/9571072; Current ChEBI/OLS entry and CAS 80195-36-4 PubChem resolution. | supports | The full key, neutral formula, (6R,7R) centres and Z hydroxyimino group agree. CHEBI:23066 is the broader cephalosporin class; antimicrobial/antibacterial-drug roles are coherent. Reaxys 7608234 is source-attested, not independently inspected. The current ChEBI entry retains the problematic carboxylate name. |
| who | https://cdn.who.int/media/docs/default-source/international-nonproprietary-names-(inn)/rl31.pdf?download=true; WHO recommended INN list 31, original page 3, cefdaloximum/cefdaloxime entry, visually inspected. | supports | The INN entry identifies a (6R,7R) carboxylic acid with Z oxime and formula C14H15N5O6S2. It supports the neutral acid identity and the Latin/English names. It is a nomenclature source, not a marketing approval. |
| diffusion | PMID:1583135; DOI:10.1128/JCM.30.5.1297-1300.1992; PMC265269; Complete adopted abstract and metadata. | supports | The paper identifies RU29246 as the active component of HR-916 ester and compares dilution and 10/30 µg disk tests in 391 clinical isolates. Proposed zone/MIC criteria were explicitly tentative for clinical trials. They are neither current breakpoints nor measurements of the intact ester; complete original tables and supplied material form were not recovered. |
| medium | PMID:8150978; DOI:10.1128/JCM.32.2.565-567.1994; PMC263080; Complete adopted abstract; PMC identifier is the same paper. | supports | Among 57 enterococcal strains, including 30 E. faecalis, disk tests on Mueller–Hinton agar with or without 5% sheep blood show medium-dependent enhancement for cefdaloxime and cefdinir. This is susceptibility-method context, not universal enterococcal efficacy or a direct molecular target. |
| htm | PMID:1478050; DOI:10.1016/0732-8893(92)90073-3; Available adopted abstract, explicitly truncated by its index at 250 words. | supports | The study compares Haemophilus test-medium disk zones and MICs and proposes tentative criteria. BLNAR isolates have high MICs in the panel. The index truncation and lack of full methods prevent individual MIC adoption or a mechanistic conclusion. |
| multicentre | PMID:1810737; DOI:10.1007/BF01972510; Complete primary abstract retrieved as exact-compound follow-up. | supports | A multicentre study of more than 5000 clinical isolates tests RU29246, the active HR916 metabolite. It reports organism-dependent activity, poor activity against selected nonfermenters and proposed QC ranges. These are bounded population observations; they do not establish a native PBP assay or all-strain susceptibility. |
| context | PMID:29017833; PMID:15673804; PMID:11585791; PMID:6810737; All remaining adopted/parent records: available complete abstracts or metadata. | supports | 29017833 is an allergy review; 11585791 is a broad ESBL review. Parent leads 15673804 and 6810737 had no indexed abstracts. None supplies independently verified cefdaloxime target binding. Wikipedia document retrieval returned 403; its contents were not independently verified. |

## Limits And Additional Notes

- No paid registry or research service was used. An inaccessible document is an explicit verification limit, not evidence that the document or biological effect does not exist.
- All four unique adopted PMIDs were dispositioned; PMC263080 duplicates PMID8150978. Three parent review leads and the exact-compound multicentre follow-up were also inspected at available abstract/metadata level.
- The primary papers remain abstract-level evidence; public PMC routes returned browser challenges. PMID1478050 is itself truncated in the index. No complete primary assay or numerical extraction is claimed.
- Reaxys registry detail and the Wikipedia document remain independently unverified. Source classification alone was not treated as a required defect.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T111921Z-cefdaloxime-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefdaloxime: coherent neutral acid with an anion-form exact synonym'
started_at: '2026-10-21T10:55:31Z'
finished_at: '2026-10-21T11:19:21Z'
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
summary: The exact neutral cefdaloxime graph and antibacterial role are supported.
  One source-imported exact synonym ends in carboxylate despite the neutral carboxylic-acid
  structure. A minor naming correction is required; original susceptibility abstracts
  support only their historical assay and population scope.
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
  - path: data/antibiotics/antibacterial/cefdaloxime.yaml
    sha256: c1d2ba14ca3ec98383a2f70ef2e5922e8aa91d92c71fe0334b6348865016f007
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
- target_id: CHEBI:140109
  path: data/antibiotics/antibacterial/cefdaloxime.yaml
  label: cefdaloxime
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
  selection: Initially uncovered queue position 217; one exact record in path order,
    captured before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:140109
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:140109
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    217
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:140109
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefdaloxime.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:140109
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefdaloxime.yaml --out /private/tmp/am-review-session/217-strict.tsv
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
  - CHEBI:140109
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
  - CHEBI:140109
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
  - CHEBI:140109
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
  - CHEBI:140109
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
  - CHEBI:140109
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
  - CHEBI:140109
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
  - CHEBI:140109
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
  - CHEBI:140109
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
  - CHEBI:140109
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cefdaloxime.yaml
  locator: Complete YAML, including all source concepts and history events.
  accessed_at: '2026-10-21T11:12:14Z'
  support: supports
  summary: Read every native field and retained assertion. This review does not change
    the generated record or promote SEEDED status.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Exact maintained rows in 217-raw-rows.json; applicable extraction, join
    and seeding code.
  accessed_at: '2026-10-21T11:12:14Z'
  support: supports
  summary: The maintained rows reproduce the native source-owned content. Initial
    input hashes are retained; actual additional owners were appended from a supplemental
    capture before detailed judgment. Corrections belong at the reproducible source/decision
    boundary.
  snapshot_sha256: 02819f2c5850817a215754af8e469463444ae49b8e050d4c4dc49ad5f285830a
- evidence_id: chemistry
  kind: validation
  reference: 217-chemistry.json; 217-220-external-chemistry.json
  locator: Independent RDKit parse of native SMILES/InChI and inspected official structures.
  accessed_at: '2026-10-21T11:12:14Z'
  support: supports
  summary: Native encodings reproduce HOGISBSFFHDTRM-GHXIOONMSA-N, C14H15N5O6S2, charge
    0, masses and two R centres. Oxime geometry is Z. The batch019 interpreter operated
    on unchanged batch022 inputs because batch022 has no RDKit.
  snapshot_sha256: 172d479791c82d57b5cc3c95343be4e3e51360eca4842240e2983a0be6eea779
- evidence_id: search
  kind: search
  reference: 217-local-hits.txt; 217-owner-hits.txt
  locator: Exact identifier, label, key and slug; hidden and ignored files included.
  accessed_at: '2026-10-21T11:12:14Z'
  support: supports
  summary: The complete native record, maintained inputs, generated references and
    related chemical forms were distinguished. No exact corrective decision was identified
    in the inspected maintained inputs.
  search_scope: rg --no-ignore --hidden across the isolated worktree, excluding .git
    and .venv internals; exact identifier, label, slug and full-key searches.
  snapshot_sha256: 27807f7b1ff60e4ce36c7b5da5990611335d08f700da10a2861eafb13aa04dc6
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:140109; https://pubchem.ncbi.nlm.nih.gov/compound/9571072
  locator: Current ChEBI/OLS entry and CAS 80195-36-4 PubChem resolution.
  accessed_at: '2026-10-21T11:12:14Z'
  support: supports
  summary: The full key, neutral formula, (6R,7R) centres and Z hydroxyimino group
    agree. CHEBI:23066 is the broader cephalosporin class; antimicrobial/antibacterial-drug
    roles are coherent. Reaxys 7608234 is source-attested, not independently inspected.
    The current ChEBI entry retains the problematic carboxylate name.
  snapshot_sha256: 8a6d02652b503a084a8e3ef7aa5a74914da087780e904a51de5de2eef1053993
- evidence_id: who
  kind: authority
  reference: https://cdn.who.int/media/docs/default-source/international-nonproprietary-names-(inn)/rl31.pdf?download=true
  locator: WHO recommended INN list 31, original page 3, cefdaloximum/cefdaloxime
    entry, visually inspected.
  accessed_at: '2026-10-21T11:12:14Z'
  support: supports
  summary: The INN entry identifies a (6R,7R) carboxylic acid with Z oxime and formula
    C14H15N5O6S2. It supports the neutral acid identity and the Latin/English names.
    It is a nomenclature source, not a marketing approval.
  snapshot_sha256: 610df70d9e5de9734699b02a0809b7acb53f74485604dbba49268ed9c884ba36
- evidence_id: diffusion
  kind: primary_source
  reference: PMID:1583135; DOI:10.1128/JCM.30.5.1297-1300.1992; PMC265269
  locator: Complete adopted abstract and metadata.
  accessed_at: '2026-10-21T11:12:14Z'
  support: supports
  summary: The paper identifies RU29246 as the active component of HR-916 ester and
    compares dilution and 10/30 µg disk tests in 391 clinical isolates. Proposed zone/MIC
    criteria were explicitly tentative for clinical trials. They are neither current
    breakpoints nor measurements of the intact ester; complete original tables and
    supplied material form were not recovered.
  snapshot_sha256: 65bb9e0433c3920402fc270692d1d1763fafd89d1c1e887d0eed485c98b14cf3
- evidence_id: medium
  kind: primary_source
  reference: PMID:8150978; DOI:10.1128/JCM.32.2.565-567.1994; PMC263080
  locator: Complete adopted abstract; PMC identifier is the same paper.
  accessed_at: '2026-10-21T11:12:14Z'
  support: supports
  summary: Among 57 enterococcal strains, including 30 E. faecalis, disk tests on
    Mueller–Hinton agar with or without 5% sheep blood show medium-dependent enhancement
    for cefdaloxime and cefdinir. This is susceptibility-method context, not universal
    enterococcal efficacy or a direct molecular target.
  snapshot_sha256: 65bb9e0433c3920402fc270692d1d1763fafd89d1c1e887d0eed485c98b14cf3
- evidence_id: htm
  kind: primary_source
  reference: PMID:1478050; DOI:10.1016/0732-8893(92)90073-3
  locator: Available adopted abstract, explicitly truncated by its index at 250 words.
  accessed_at: '2026-10-21T11:12:14Z'
  support: supports
  summary: The study compares Haemophilus test-medium disk zones and MICs and proposes
    tentative criteria. BLNAR isolates have high MICs in the panel. The index truncation
    and lack of full methods prevent individual MIC adoption or a mechanistic conclusion.
  snapshot_sha256: 65bb9e0433c3920402fc270692d1d1763fafd89d1c1e887d0eed485c98b14cf3
- evidence_id: multicentre
  kind: primary_source
  reference: PMID:1810737; DOI:10.1007/BF01972510
  locator: Complete primary abstract retrieved as exact-compound follow-up.
  accessed_at: '2026-10-21T11:12:14Z'
  support: supports
  summary: A multicentre study of more than 5000 clinical isolates tests RU29246,
    the active HR916 metabolite. It reports organism-dependent activity, poor activity
    against selected nonfermenters and proposed QC ranges. These are bounded population
    observations; they do not establish a native PBP assay or all-strain susceptibility.
  snapshot_sha256: 5c93db4e543b6754099395f490ffc20d5efea0babfb57a0f6e409490e31af6f1
- evidence_id: context
  kind: database
  reference: PMID:29017833; PMID:15673804; PMID:11585791; PMID:6810737
  locator: 'All remaining adopted/parent records: available complete abstracts or
    metadata.'
  accessed_at: '2026-10-21T11:12:14Z'
  support: supports
  summary: 29017833 is an allergy review; 11585791 is a broad ESBL review. Parent
    leads 15673804 and 6810737 had no indexed abstracts. None supplies independently
    verified cefdaloxime target binding. Wikipedia document retrieval returned 403;
    its contents were not independently verified.
  snapshot_sha256: 65bb9e0433c3920402fc270692d1d1763fafd89d1c1e887d0eed485c98b14cf3
assessments:
- assessment_id: provenance
  area: provenance
  topic: Maintained ownership and source history
  outcome: supported
  summary: Source concepts, minted identifiers and history are coherent. Source-origin
    corrections require regeneration; new primary observations require the validated
    native writer and curation event.
  target_ids:
  - CHEBI:140109
  evidence_ids:
  - record
  - source
  - search
- assessment_id: checks
  area: schema
  topic: Focused native gates
  outcome: supported
  summary: Documented schema/strict checks and independent native chemistry pass.
    These do not validate every external cross-reference or confer scientific sign-off.
  target_ids:
  - CHEBI:140109
  evidence_ids:
  - chemistry
- assessment_id: identity
  area: identity
  topic: Exact acid, synonyms and groundings
  outcome: concern
  summary: The chemical graph, CAS resolution and INN identity agree, but the imported
    standalone carboxylate name denotes the anionic form without an ester substituent
    or balancing cation.
  target_ids:
  - CHEBI:140109
  evidence_ids:
  - identity
  - who
  - chemistry
  - source
- assessment_id: activity
  area: evidence
  topic: Antibacterial role and historical assays
  outcome: supported
  summary: Exact-compound primary abstracts support antibacterial activity while exposing
    medium, organism and formulation limits. Tentative historical disk criteria are
    not current clinical standards.
  target_ids:
  - CHEBI:140109
  evidence_ids:
  - diffusion
  - medium
  - htm
  - multicentre
- assessment_id: optional
  area: completeness
  topic: Mechanism, producer, clinical status and causal graph
  outcome: unknown
  summary: These optional fields are unpopulated; no named native protein/gene/pathway
    claim requires a structured adapter. No direct exact-compound PBP experiment or
    natural producer was established in this bounded review.
  target_ids:
  - CHEBI:140109
  evidence_ids:
  - record
  - context
  - multicentre
findings:
- finding_id: F1
  issue_key: cefdaloxime-carboxylate-exact-synonym
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the anion-form synonym attached to neutral cefdaloxime
  description: synonyms[2] ends in cepham-4-carboxylate and contains no esterifying
    group, whereas the native graph has COOH, charge 0 and formula C14H15N5O6S2. The
    source and current ChEBI repeat the mismatch; the other systematic synonym and
    WHO INN specify the acid. This is a nomenclature defect, not evidence that the
    stored structure is the wrong antibiotic.
  target_ids:
  - CHEBI:140109
  field_paths:
  - synonyms[2]
  evidence_ids:
  - record
  - source
  - identity
  - who
  - chemistry
  rule_id: 'native-review-checklist: exact chemical identity, accurate names and source-supported
    references'
  native_severity: minor
  normalization_reason: Severity reflects the specific confirmed field error; coherent
    native identity is retained where independently supported.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI identity, names and document references
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintain reproducible source extraction or correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerate source-owned fields
actions:
- action_id: A1
  description: Correct the anion-form synonym attached to neutral cefdaloxime
  finding_ids:
  - F1
  target_ids:
  - CHEBI:140109
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI identity, names and document references
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintain reproducible source extraction or correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerate source-owned fields
  acceptance_checks:
  - Reconcile the source synonym with the exact neutral acid; use a verified carboxylic-acid
    name or suppress the anion name from exact synonyms.
  - Preserve the supported structure, full key and stereo. Do not change the record
    to an anion or infer salt identity from this naming error.
  - Implement through a maintained source/extraction/decision correction and regenerate;
    preserve original provenance and inspect the exact diff. Do not patch generated
    YAML alone.
  - Run focused schema/strict and independent chemistry, verify-corpus, and applicable
    shared gates after any separately authorized correction.
limitations:
- No paid registry or research service was used. An inaccessible document is an explicit
  verification limit, not evidence that the document or biological effect does not
  exist.
- All four unique adopted PMIDs were dispositioned; PMC263080 duplicates PMID8150978.
  Three parent review leads and the exact-compound multicentre follow-up were also
  inspected at available abstract/metadata level.
- The primary papers remain abstract-level evidence; public PMC routes returned browser
  challenges. PMID1478050 is itself truncated in the index. No complete primary assay
  or numerical extraction is claimed.
- Reaxys registry detail and the Wikipedia document remain independently unverified.
  Source classification alone was not treated as a required defect.
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
