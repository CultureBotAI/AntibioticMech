# Cefditoren pivoxil: coherent prodrug identity with unresolved optical-rotation naming

- Review: 20261021T111944Z-cefditoren-pivoxil-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:55:31Z
- Finished UTC: 2026-10-21T11:19:44Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The neutral pivoxil ester, exact public chemical mappings and retained historical FDA assertions agree. Active cefditoren measurements must remain separate from administered prodrug evidence. A source synonym uses (+), whereas the FDA whole-compound name and Japanese Pharmacopoeia rotation are negative; the possible acid-moiety scope of the ester name remains unresolved, so this is a provisional informational follow-up rather than a confirmed structural error. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 219; one exact record in path order, captured before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:560555 | data/antibiotics/antibacterial/cefditoren-pivoxil.yaml | generated | cefditoren pivoxil |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:560555 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:560555 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:560555 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:560555 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:560555 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:560555 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:560555 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:560555 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:560555 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:560555 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:560555 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:560555 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Maintained ownership and source history

provenance: supported. Targets: CHEBI:560555.

Source concepts, minted identifiers and history are coherent. Source-origin corrections require regeneration; new primary observations require the validated native writer and curation event.

### Focused native gates

schema: supported. Targets: CHEBI:560555.

Documented schema/strict checks and independent native chemistry pass. These do not validate every external cross-reference or confer scientific sign-off.

### Neutral prodrug and exact groundings

identity: supported. Targets: CHEBI:560555.

Native structure and public mappings agree, and the ester definition distinguishes the free acid. No opposite enantiomer, racemate or salt is inferred from optical-rotation wording.

### Optical-rotation qualifier in an ester synonym

representation: unknown. Targets: CHEBI:560555.

The imported pivaloyloxymethyl (+)-(6R,7R)...carboxylate wording contrasts with the FDA whole-compound (-) name and measured negative rotation. Its (+) may instead modify the acid-derived moiety of the functional-class ester name; the naming convention or original source must be resolved before calling it erroneous. Absolute stereochemistry agrees.

### Historical approval versus current marketing

evidence: supported. Targets: CHEBI:560555.

Both retained FDA application assertions match current product/date tables. The record already distinguishes discontinued marketing from historical approval. No confirmed withdrawal conflict was established.

### Prodrug, active-moiety assays and clinical evidence

evidence: supported. Targets: CHEBI:560555.

The prodrug definition is supported by the label and human exposure literature. Antibacterial testing of cefditoren powder is not an experiment with intact cefditoren pivoxil, and PK time-above-MIC estimates are not new susceptibility observations.

### Mechanism, producer and causal graph

completeness: unknown. Targets: CHEBI:560555.

No named native protein, gene, pathway or transcriptomic claim requires an adapter. Optional targets and causal graphs are absent without constituting a defect. No natural producer or direct intact-prodrug target experiment was established.

## Findings

### F1: Resolve the scope of the optical-rotation sign in the imported ester name

informational / open / provisional; issue key: cefditoren-pivoxil-optical-rotation-name-scope.

The native exact synonym uses (+), while the FDA whole-compound name uses (-) and the pharmacopoeial material has negative rotation under specified conditions. The native qualifier may refer to the acid-derived moiety within the ester name. This unresolved naming scope does not establish a structural or stereochemical error.

## Recommended Actions And Acceptance Checks

### A1

Clarify the original nomenclature before changing the exact synonym

- Inspect the original naming source and determine whether (+) modifies the complete ester or its acid-derived moiety, preserving the optical-rotation conditions.
- If a misapplied sign is confirmed, correct or suppress the synonym at the maintained source boundary and regenerate; otherwise document why the functional-class name is valid. Preserve the independently supported structure, absolute stereochemistry and full key.
- Any separately authorized correction must pass focused schema/strict validation, independent chemistry and corpus reproduction.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cefditoren-pivoxil.yaml; Complete YAML, including all source concepts and history events. | supports | Read every native field and retained assertion. This review does not change the generated record or promote SEEDED status. |
| source | data/raw/chebi_antimicrobials.tsv; data/raw/fda_clinical_status.tsv; Exact maintained rows in 219-raw-rows.json; applicable extraction, join and seeding code. | supports | The maintained rows reproduce the native source-owned content. Initial input hashes are retained; actual additional owners were appended from a supplemental capture before detailed judgment. Corrections belong at the reproducible source/decision boundary. |
| chemistry | 219-chemistry.json; 217-220-external-chemistry.json; Independent RDKit parse of native SMILES/InChI and inspected official structures. | supports | Native encodings reproduce AFZFFLVORLEPPO-UVYJNCLZSA-N, C25H28N6O7S3, charge 0, masses and two R centres. Oxime geometry is Z and the thiazolylvinyl bond is Z. The batch019 interpreter operated on unchanged batch022 inputs because batch022 has no RDKit. |
| search | 219-local-hits.txt; 219-owner-hits.txt; Exact identifier, label, key and slug; hidden and ignored files included. | supports | The complete native record, maintained inputs, generated references and related chemical forms were distinguished. No exact corrective decision was identified in the inspected maintained inputs. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:560555; https://pubchem.ncbi.nlm.nih.gov/compound/6437877; https://rest.kegg.jp/get/D01628; Current ChEBI entry, CAS 117467-28-4 PubChem resolution and independent KEGG MOL parse. | supports | The complete neutral pivoxil ester graph, formula C25H28N6O7S3, two R centres and two Z bonds agree. Current ChEBI parents identify pivaloyloxymethyl esters, cephams, oxime O-ethers and 1,3-thiazoles, all present in the structure. The free acid is a distinct molecular form. Beilstein 4902739 remains source-attested; DrugBank DB01066 and Wikipedia retrieval returned 403. |
| gsrs | https://gsrs.ncats.nih.gov/api/v1/substances/search?q=root_approvalID:78THA212DH; drugcentral:534; Current GSRS v26 and independently parsed adopted DrugCentral SMILES/InChI. | supports | Both structures and GSRS reproduce full native key AFZFFLVORLEPPO-UVYJNCLZSA-N. Current GSRS version agrees with retained v26. UNII confirms chemical identity, independently of approval status. |
| fda | https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&amp;ApplNo=021222; Current NDA 021222 product table and ORIG action date; all two native assertions and exact maintained rows. | supports | SPECTRACEF products 001/002, 200/400 mg, are listed as discontinued; the original approval date is 2001-08-29. These agree with the retained Vansen Pharma application rows and false currently_marketed flags. Discontinued marketing alone does not establish withdrawal of approval. A bounded public withdrawal-notice search found no affirmative determination for this application; that is not an exhaustive legal conclusion. |
| label | https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/021222s013s016lbl.pdf; Historical FDA label Description, Pharmacokinetics, Microbiology and Indications. | supports | The whole-compound name carries (-), with the matching formula and prodrug structure. Oral cefditoren pivoxil is hydrolyzed by esterases to active cefditoren; tablet doses are cefditoren-equivalent amounts. Susceptibility testing uses cefditoren powder. The label describes an amorphous drug form and historical approved use; it does not turn prodrug exposure into direct intact-ester antibacterial binding or establish current treatment guidance. |
| jp14 | https://jpdb.nihs.go.jp/jp14e/14data/Part-I/Cefdinir.pdf; https://jpdb.nihs.go.jp/jp14e/14data/Part-I/Cefepime_Dihydrochloride.pdf; Japanese Pharmacopoeia XIV original cefditoren pivoxil monograph pp325–326, split across these official PDFs; both pages visually inspected. | supports | CAS, formula and depicted 6R,7R and Z configurations agree. The monograph gives specific rotation -45 to -52 degrees at 20 C for 0.05 g in 10 mL methanol using a 100 mm cell. It describes crystalline material and potency as cefditoren equivalents. Rotation conditions and solid form matter; this source does not show that the native (+) ester-name modifier has the same intended referent. |
| pk-primary | PMID:17530036; https://seq.es/seq/0214-3429/20/1/51.pdf; Original abstract and relevant Methods pp52–54; complete PDF obtained, not every result table audited. | supports | Twenty healthy adult men received single oral pivoxil doses, followed after washout by twice- or thrice-daily dosing or placebo. Doses followed meals. HPLC measured active cefditoren in plasma and urine; time above MIC used literature pneumococcal values. This is human prodrug exposure and tolerability evidence, not new bacterial MIC testing or direct target binding. |
| other-primary | PMID:9515223; PMID:12501878; DOI:10.1016/S0149-2918(02)80083-2; Complete primary abstracts and metadata. | supports | The 1997 phase I study compares oral ME1207 dosing and food effects using HPLC/bioassay. Its abbreviated wording is insufficient to assign an unchanged-prodrug urinary species. The 2002 randomized double-blind pneumonia trial enrolled 851 patients and compared oral pivoxil with cefpodoxime proxetil, reporting clinical and bacteriological outcomes. These support administered-prodrug context, without establishing an exact intact-ester MIC or molecular target. |

## Limits And Additional Notes

- No paid registry or research service was used. An inaccessible document is an explicit verification limit, not evidence that the document or biological effect does not exist.
- The native record has no adopted compound PMID list. Three exact-prodrug primary studies were pursued; two remain abstract-level. The 2007 original abstract and relevant analytical Methods were inspected, not every result table.
- The two official JP XIV pages were visually inspected. The historical FDA label and current application table serve different identity, use and regulatory purposes. No comprehensive worldwide or legal withdrawal-status audit is claimed.
- The optical-rotation naming issue remains provisional; it must not prompt inversion of stereocentres or substitution of an enantiomer.
- DrugBank, Beilstein registry detail and the Wikipedia document remain independently unverified. Blank optional fields and authority-only classification were not treated as defects.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T111944Z-cefditoren-pivoxil-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefditoren pivoxil: coherent prodrug identity with unresolved optical-rotation
  naming'
started_at: '2026-10-21T10:55:31Z'
finished_at: '2026-10-21T11:19:44Z'
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
summary: The neutral pivoxil ester, exact public chemical mappings and retained historical
  FDA assertions agree. Active cefditoren measurements must remain separate from administered
  prodrug evidence. A source synonym uses (+), whereas the FDA whole-compound name
  and Japanese Pharmacopoeia rotation are negative; the possible acid-moiety scope
  of the ester name remains unresolved, so this is a provisional informational follow-up
  rather than a confirmed structural error. Scientific assessment retains the stated
  evidence limits; full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/cefditoren-pivoxil.yaml
    sha256: 762dce34ed5d77e82dafc0506a5f1dd52aff827de843ec1a479b0261d8ab50b6
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
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
    role: context
  - path: scripts/extract_fda_clinical_status.py
    sha256: f30f385ea6d530dc1749e3d805dbcdbc8715fbc476abc510bf144ea13964e171
    role: context
targets:
- target_id: CHEBI:560555
  path: data/antibiotics/antibacterial/cefditoren-pivoxil.yaml
  label: cefditoren pivoxil
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
    path: data/raw/fda_clinical_status.tsv
    role: Adopted exact-key FDA product assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Product regulatory extraction and GSRS exact join
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 219; one exact record in path order,
    captured before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:560555
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:560555
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    219
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:560555
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefditoren-pivoxil.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:560555
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefditoren-pivoxil.yaml --out /private/tmp/am-review-session/219-strict.tsv
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
  - CHEBI:560555
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
  - CHEBI:560555
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
  - CHEBI:560555
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
  - CHEBI:560555
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
  - CHEBI:560555
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
  - CHEBI:560555
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
  - CHEBI:560555
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
  - CHEBI:560555
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
  - CHEBI:560555
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cefditoren-pivoxil.yaml
  locator: Complete YAML, including all source concepts and history events.
  accessed_at: '2026-10-21T11:18:55Z'
  support: supports
  summary: Read every native field and retained assertion. This review does not change
    the generated record or promote SEEDED status.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/fda_clinical_status.tsv
  locator: Exact maintained rows in 219-raw-rows.json; applicable extraction, join
    and seeding code.
  accessed_at: '2026-10-21T11:18:55Z'
  support: supports
  summary: The maintained rows reproduce the native source-owned content. Initial
    input hashes are retained; actual additional owners were appended from a supplemental
    capture before detailed judgment. Corrections belong at the reproducible source/decision
    boundary.
  snapshot_sha256: 64e19390abd2c330abf84a97c9415e41d6d426be9d55bb9b943ae2d00aa17932
- evidence_id: chemistry
  kind: validation
  reference: 219-chemistry.json; 217-220-external-chemistry.json
  locator: Independent RDKit parse of native SMILES/InChI and inspected official structures.
  accessed_at: '2026-10-21T11:18:55Z'
  support: supports
  summary: Native encodings reproduce AFZFFLVORLEPPO-UVYJNCLZSA-N, C25H28N6O7S3, charge
    0, masses and two R centres. Oxime geometry is Z and the thiazolylvinyl bond is
    Z. The batch019 interpreter operated on unchanged batch022 inputs because batch022
    has no RDKit.
  snapshot_sha256: 172d479791c82d57b5cc3c95343be4e3e51360eca4842240e2983a0be6eea779
- evidence_id: search
  kind: search
  reference: 219-local-hits.txt; 219-owner-hits.txt
  locator: Exact identifier, label, key and slug; hidden and ignored files included.
  accessed_at: '2026-10-21T11:18:55Z'
  support: supports
  summary: The complete native record, maintained inputs, generated references and
    related chemical forms were distinguished. No exact corrective decision was identified
    in the inspected maintained inputs.
  search_scope: rg --no-ignore --hidden across the isolated worktree, excluding .git
    and .venv internals; exact identifier, label, slug and full-key searches.
  snapshot_sha256: 14beb7502c9e00cc68358f02f7af205c61e424c381c50e04c0f68e99bb4be872
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:560555; https://pubchem.ncbi.nlm.nih.gov/compound/6437877;
    https://rest.kegg.jp/get/D01628
  locator: Current ChEBI entry, CAS 117467-28-4 PubChem resolution and independent
    KEGG MOL parse.
  accessed_at: '2026-10-21T11:18:55Z'
  support: supports
  summary: The complete neutral pivoxil ester graph, formula C25H28N6O7S3, two R centres
    and two Z bonds agree. Current ChEBI parents identify pivaloyloxymethyl esters,
    cephams, oxime O-ethers and 1,3-thiazoles, all present in the structure. The free
    acid is a distinct molecular form. Beilstein 4902739 remains source-attested;
    DrugBank DB01066 and Wikipedia retrieval returned 403.
  snapshot_sha256: 7b0a9e5be8472a463352dd2c54cfa3fcac1a95776ae67e58b82d592771a9a446
- evidence_id: gsrs
  kind: authority
  reference: https://gsrs.ncats.nih.gov/api/v1/substances/search?q=root_approvalID:78THA212DH;
    drugcentral:534
  locator: Current GSRS v26 and independently parsed adopted DrugCentral SMILES/InChI.
  accessed_at: '2026-10-21T11:18:55Z'
  support: supports
  summary: Both structures and GSRS reproduce full native key AFZFFLVORLEPPO-UVYJNCLZSA-N.
    Current GSRS version agrees with retained v26. UNII confirms chemical identity,
    independently of approval status.
  snapshot_sha256: d608f801586c68fddc05b17f254ec0a931dce5ce97583cb173abefed4ecaa1b0
- evidence_id: fda
  kind: authority
  reference: https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=021222
  locator: Current NDA 021222 product table and ORIG action date; all two native assertions
    and exact maintained rows.
  accessed_at: '2026-10-21T11:18:55Z'
  support: supports
  summary: SPECTRACEF products 001/002, 200/400 mg, are listed as discontinued; the
    original approval date is 2001-08-29. These agree with the retained Vansen Pharma
    application rows and false currently_marketed flags. Discontinued marketing alone
    does not establish withdrawal of approval. A bounded public withdrawal-notice
    search found no affirmative determination for this application; that is not an
    exhaustive legal conclusion.
  snapshot_sha256: 584d6f28a1c849fc3a7d2443496011f67b8c7d5967fcdbe66fb3e2c0bc09cd3c
- evidence_id: label
  kind: authority
  reference: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/021222s013s016lbl.pdf
  locator: Historical FDA label Description, Pharmacokinetics, Microbiology and Indications.
  accessed_at: '2026-10-21T11:18:55Z'
  support: supports
  summary: The whole-compound name carries (-), with the matching formula and prodrug
    structure. Oral cefditoren pivoxil is hydrolyzed by esterases to active cefditoren;
    tablet doses are cefditoren-equivalent amounts. Susceptibility testing uses cefditoren
    powder. The label describes an amorphous drug form and historical approved use;
    it does not turn prodrug exposure into direct intact-ester antibacterial binding
    or establish current treatment guidance.
  snapshot_sha256: f26e1ef02d78c3e28d4a7dcfd836c4e5086f82a8ae26a01a3d7591d0676e93e2
- evidence_id: jp14
  kind: authority
  reference: https://jpdb.nihs.go.jp/jp14e/14data/Part-I/Cefdinir.pdf; https://jpdb.nihs.go.jp/jp14e/14data/Part-I/Cefepime_Dihydrochloride.pdf
  locator: Japanese Pharmacopoeia XIV original cefditoren pivoxil monograph pp325–326,
    split across these official PDFs; both pages visually inspected.
  accessed_at: '2026-10-21T11:18:55Z'
  support: supports
  summary: CAS, formula and depicted 6R,7R and Z configurations agree. The monograph
    gives specific rotation -45 to -52 degrees at 20 C for 0.05 g in 10 mL methanol
    using a 100 mm cell. It describes crystalline material and potency as cefditoren
    equivalents. Rotation conditions and solid form matter; this source does not show
    that the native (+) ester-name modifier has the same intended referent.
  snapshot_sha256: 8389be3336e7115a58d209d2e6c6a1929d315a7758f7c596172a1f364a1ed605
- evidence_id: pk-primary
  kind: primary_source
  reference: PMID:17530036; https://seq.es/seq/0214-3429/20/1/51.pdf
  locator: Original abstract and relevant Methods pp52–54; complete PDF obtained,
    not every result table audited.
  accessed_at: '2026-10-21T11:18:55Z'
  support: supports
  summary: Twenty healthy adult men received single oral pivoxil doses, followed after
    washout by twice- or thrice-daily dosing or placebo. Doses followed meals. HPLC
    measured active cefditoren in plasma and urine; time above MIC used literature
    pneumococcal values. This is human prodrug exposure and tolerability evidence,
    not new bacterial MIC testing or direct target binding.
  snapshot_sha256: 29db59a423e2aadd19fa53932e581db9d51574386248ab15bcad0d06f328237c
- evidence_id: other-primary
  kind: primary_source
  reference: PMID:9515223; PMID:12501878; DOI:10.1016/S0149-2918(02)80083-2
  locator: Complete primary abstracts and metadata.
  accessed_at: '2026-10-21T11:18:55Z'
  support: supports
  summary: The 1997 phase I study compares oral ME1207 dosing and food effects using
    HPLC/bioassay. Its abbreviated wording is insufficient to assign an unchanged-prodrug
    urinary species. The 2002 randomized double-blind pneumonia trial enrolled 851
    patients and compared oral pivoxil with cefpodoxime proxetil, reporting clinical
    and bacteriological outcomes. These support administered-prodrug context, without
    establishing an exact intact-ester MIC or molecular target.
  snapshot_sha256: 88a8103e486e436a80a24f9bae4b13c97ad0befb802259c1245136393af37d7f
assessments:
- assessment_id: provenance
  area: provenance
  topic: Maintained ownership and source history
  outcome: supported
  summary: Source concepts, minted identifiers and history are coherent. Source-origin
    corrections require regeneration; new primary observations require the validated
    native writer and curation event.
  target_ids:
  - CHEBI:560555
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
  - CHEBI:560555
  evidence_ids:
  - chemistry
- assessment_id: identity
  area: identity
  topic: Neutral prodrug and exact groundings
  outcome: supported
  summary: Native structure and public mappings agree, and the ester definition distinguishes
    the free acid. No opposite enantiomer, racemate or salt is inferred from optical-rotation
    wording.
  target_ids:
  - CHEBI:560555
  evidence_ids:
  - identity
  - chemistry
  - gsrs
  - label
  - jp14
- assessment_id: nomenclature
  area: representation
  topic: Optical-rotation qualifier in an ester synonym
  outcome: unknown
  summary: The imported pivaloyloxymethyl (+)-(6R,7R)...carboxylate wording contrasts
    with the FDA whole-compound (-) name and measured negative rotation. Its (+) may
    instead modify the acid-derived moiety of the functional-class ester name; the
    naming convention or original source must be resolved before calling it erroneous.
    Absolute stereochemistry agrees.
  target_ids:
  - CHEBI:560555
  evidence_ids:
  - record
  - source
  - identity
  - label
  - jp14
- assessment_id: clinical
  area: evidence
  topic: Historical approval versus current marketing
  outcome: supported
  summary: Both retained FDA application assertions match current product/date tables.
    The record already distinguishes discontinued marketing from historical approval.
    No confirmed withdrawal conflict was established.
  target_ids:
  - CHEBI:560555
  evidence_ids:
  - fda
  - gsrs
  - source
- assessment_id: activity
  area: evidence
  topic: Prodrug, active-moiety assays and clinical evidence
  outcome: supported
  summary: The prodrug definition is supported by the label and human exposure literature.
    Antibacterial testing of cefditoren powder is not an experiment with intact cefditoren
    pivoxil, and PK time-above-MIC estimates are not new susceptibility observations.
  target_ids:
  - CHEBI:560555
  evidence_ids:
  - label
  - pk-primary
  - other-primary
- assessment_id: optional
  area: completeness
  topic: Mechanism, producer and causal graph
  outcome: unknown
  summary: No named native protein, gene, pathway or transcriptomic claim requires
    an adapter. Optional targets and causal graphs are absent without constituting
    a defect. No natural producer or direct intact-prodrug target experiment was established.
  target_ids:
  - CHEBI:560555
  evidence_ids:
  - record
  - label
  - pk-primary
findings:
- finding_id: F1
  issue_key: cefditoren-pivoxil-optical-rotation-name-scope
  category: representation
  severity: informational
  status: open
  certainty: provisional
  title: Resolve the scope of the optical-rotation sign in the imported ester name
  description: The native exact synonym uses (+), while the FDA whole-compound name
    uses (-) and the pharmacopoeial material has negative rotation under specified
    conditions. The native qualifier may refer to the acid-derived moiety within the
    ester name. This unresolved naming scope does not establish a structural or stereochemical
    error.
  target_ids:
  - CHEBI:560555
  field_paths:
  - synonyms[4]
  evidence_ids:
  - record
  - source
  - label
  - jp14
  - identity
  rule_id: 'native-review-checklist: exact nomenclature and explicit evidence conflicts'
  native_severity: informational
  normalization_reason: Conflicting wording is documented, but its referent is unresolved
    and all inspected chemical graphs agree.
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
  description: Clarify the original nomenclature before changing the exact synonym
  finding_ids:
  - F1
  target_ids:
  - CHEBI:560555
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
  - Inspect the original naming source and determine whether (+) modifies the complete
    ester or its acid-derived moiety, preserving the optical-rotation conditions.
  - If a misapplied sign is confirmed, correct or suppress the synonym at the maintained
    source boundary and regenerate; otherwise document why the functional-class name
    is valid. Preserve the independently supported structure, absolute stereochemistry
    and full key.
  - Any separately authorized correction must pass focused schema/strict validation,
    independent chemistry and corpus reproduction.
limitations:
- No paid registry or research service was used. An inaccessible document is an explicit
  verification limit, not evidence that the document or biological effect does not
  exist.
- The native record has no adopted compound PMID list. Three exact-prodrug primary
  studies were pursued; two remain abstract-level. The 2007 original abstract and
  relevant analytical Methods were inspected, not every result table.
- The two official JP XIV pages were visually inspected. The historical FDA label
  and current application table serve different identity, use and regulatory purposes.
  No comprehensive worldwide or legal withdrawal-status audit is claimed.
- The optical-rotation naming issue remains provisional; it must not prompt inversion
  of stereocentres or substitution of an enantiomer.
- DrugBank, Beilstein registry detail and the Wikipedia document remain independently
  unverified. Blank optional fields and authority-only classification were not treated
  as defects.
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
