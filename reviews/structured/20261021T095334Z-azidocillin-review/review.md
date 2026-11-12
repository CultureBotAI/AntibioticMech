# Azidocillin: exact neutral identity supported with historical assay and salt boundaries

- Review: 20261021T095334Z-azidocillin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:24:43Z
- Finished UTC: 2026-10-21T09:53:34Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Current ChEBI, PubChem and ChEMBL corroborate the native four-centre neutral azidocillin structure. Source grounding, penicillin class and broad antimicrobial role are consistent. Historical antibacterial studies and patents support useful follow-up, but salt formulations, patent-wide stereochemical scope and missing original assay methods must remain explicit. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position133; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:51758 | data/antibiotics/antibacterial/azidocillin.yaml | generated | azidocillin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:51758 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:51758 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:51758 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:51758 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:51758 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:51758 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:51758 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:51758 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:51758 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:51758 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:51758 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:51758 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Source reproduction, ownership and native status

provenance: supported. Targets: CHEBI:51758.

Captured maintained inputs remain unchanged. Source extraction and seeding explain native fields; structured review does not change SEEDED status.

### Focused validation

schema: supported. Targets: CHEBI:51758.

Schema and strict checks pass. Internal validity does not establish exact equivalence of every external cross-reference or prove all biological claims.

### Exact neutral structure and synonyms

identity: supported. Targets: CHEBI:51758.

Independent sources corroborate four-centre neutral azidocillin; salts and patent mixtures retain separate scope.

### Parents, role and two-source merge

grounding: supported. Targets: CHEBI:51758.

Hierarchy and configured nearest class explain native parents and antimicrobial classification; both source concepts reproduce.

### Definition and original antimicrobial evidence

evidence: supported. Targets: CHEBI:51758.

Original abstracts support antibacterial activity. Exact1969 cited outcomes and full strain-specific methods remain unavailable. Narrow-spectrum is a source classification, not a statement of inactivity against every Gram-negative strain.

### Patent and drug-context cross-references

evidence: supported. Targets: CHEBI:51758.

Documents resolve at the stated access scope and their broader salt/stereo scope is not a native exact-equivalence claim.

### Mechanism, producer, resistance and adapter applicability

scope: not_applicable. Targets: CHEBI:51758.

No native gene/protein/pathway/stress/transcriptomic assertion requires an adapter lookup. Optional empty objects are not defects; class analogy is insufficient to create a specific PBP target or biosynthetic producer.

## Findings

### F1: Add exact historical activity evidence with salt and method limits

informational / open / confirmed; issue key: azidocillin-primary-assay-form-enrichment.

Original antibacterial studies provide optional enrichment. Full assay conditions and preparation must be recovered before numerical annotation; patent potassium salts and sodium PK formulations must not be silently equated with the native neutral compound.

## Recommended Actions And Acceptance Checks

### A1

Retrieve original exact-compound assay and formulation details for bounded curation.

- Recover the cited1969 paper and relevant in-vitro methods before recording strain-level MICs or historical clinical outcomes.
- Distinguish paper-disk susceptibility groups from MIC values, and shared multi-drug results from drug-specific outcomes.
- Preserve neutral R side-chain identity, tested salt, purity and patent D/L/DL scope; do not infer azidocillin production from6-APA precursor fermentation.
- Keep clinical history and experimental PK distinct from current approval or treatment recommendations; use claim-level primary evidence and native curation history helpers.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/azidocillin.yaml; Entire YAML including four seed/reseed events | supports | Read exact ChEBI identity, ARO-derived definition/citation, all six synonyms, two parents, antimicrobial role, chemical encodings, four chemical xrefs, two drug xrefs, two patent documents and both source concepts. No populated mode, molecular target, resistance, quantitative activity, producer, clinical indication or graph fields. |
| source | data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv; 133-raw.json; seeder identity grouping and nearest drug-class extraction | supports | ChEBI row945 and ARO row585 merge under51758. ARO direct parent3009124 is below the configured drug class3000008, explaining the retained broad class parent. Adopted CHEBI33281 role agrees with current narrower antibacterial role33282 through hierarchy. Both source mints and history reproduce. |
| identity | CHEBI:51758;PubChem CID:15574941;ChEMBL:CHEMBL2105907; Current chemical entries, parent terms and independent ChEMBL SMILES parsing | supports | Neutral C16H17N5O4S and ODFHGIPNGIAMDK-NJBDSQKTSA-N agree across sources, with four assigned centres including the R side chain. Systematic synonyms encode the same graph; class CHEBI17334 penicillin and ARO3000008 are appropriate. CAS17243-38-8 is corroborated as an official source crosswalk, not independently through the proprietary registry. |
| adopted | PMID:4999682;PMID:3889939; 133-adopted.json; all metadata and abstract availability checked | context_only | The definition citation resolves to the1969 controlled scarlet-fever study, DOI10.3109/inf.1969.1.issue-2.01, but has no indexed abstract. The class-associated beta-lactam review also has no abstract. Neither title alone establishes exact clinical outcomes, modern use or particular bacterial target. |
| activity | PMID:183785;PMID:810753;PMID:1015013; Complete original abstracts in133-discovery.json | partial | The1976 study183785 tests azidocillin against H.influenzae, enterococci, B.pertussis, S.aureus and group-A streptococci by serial dilution, with comparative rather than exact MIC numbers in the abstract. PMID810753 tests dental-root isolates by paper disks and reports susceptibility groups, not quantitative MICs. PMID1015013 reports qualitative low-MIC activity against viridans streptococci. These support antibacterial context without universal strain susceptibility or a direct PBP-binding claim. |
| clinical | PMID:6894241;PMID:9519;PMID:1848; Complete indexed original abstracts in133-discovery.json | partial | PK6894241 explicitly studies azidocillin sodium formulations and reports formulation-dependent exposure; it is not a neutral-free-acid dose experiment. Otitis9519 has three treatment groups and mixed bacteriological outcomes; pooled narrative cannot be assigned to one drug/strain. Sinusitis1848 distinguishes in-vitro MIC from elimination in patients. These historical studies do not establish current approval or treatment recommendations. |
| patents | patent:GB940488;patent:US3293242; Complete public US description/examples/claims and GB abstract in133-patentUS-visible.txt/133-patentGB-visible.txt | partial | Documents concern alpha-azidobenzylpenicillin and salts. The US text expressly encompasses D, L and DL side-chain forms; examples isolate potassium salts of reported55% and83% purity and describe S.aureus Oxford growth inhibition. That broad patent scope and preparation cannot be silently assigned as an exact neutral R-record MIC. Semisynthetic use of6-APA does not establish azidocillin production by its precursor-producing mould. |
| drug-xrefs | DrugCentral273;DrugBankDB08795; 133-drugcentral-visible.txt;133-drugbank retrieval | partial | DrugCentral named card, CAS/formula and crosswalks agree; salt synonyms and predicted PK/toxicity fields are drug-context information, not exact chemical equivalence or experimental mechanisms. DrugBank returned403. These are correctly typed drug_xrefs, distinct from structure xrefs and patent documents. No current approval inference follows from the page. |
| discovery | Bounded azidocillin literature search; 133-discovery.json;57 returned records and available abstracts | context_only | Other records concern host allergy, analytical standards, formulation stability, PK and historical clinical use. Docking-only GLP1/NDM1 hits are not direct enzyme inhibition or antimicrobial targets. Later broad patent lists are not compound-specific efficacy experiments; no claim is imported merely from a name appearing in them. |
| chemistry | Independent RDKit and source-mint checks; 133-chemistry.json;014-root-xref-checks.json | supports | Both native encodings reproduce the full key, formula, charge, one component, exact mass and source mint. Stored average masses agree within the stated decimal precision tolerance; azamulin uses a 0.1-unit tolerance for its one-decimal source value. Focused schema and strict commands exit 0. |
| search | CultureBotAI/AntibioticMech; 133-local-hits.txt;133-maintained-search.txt | context_only | Maintained exact-name/identifier/key searches found the source rows and readiness inventory, without an exact-target curator override. Azidocillin numeric search also returned an unrelated ambiguine Reaxys identifier, rejected as a substring collision. |

## Limits And Additional Notes

- The two adopted bibliographic leads lack indexed abstracts, and their full manuscripts were not retrieved. Additional activity/PK/clinical articles remain abstract-level. No exact assay table or contemporary approval audit is claimed.
- US patent description/examples/claims and GB abstract were read; original patent formula images and all patent-family documents were not independently audited. No patent legal-status judgment is made.
- DrugBank access returned403; DrugCentral card was inspected as a drug-context crosswalk, not an independently parsed exact structural export. The absence of a target field is not evidence that a molecular mechanism does not exist.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 21 captured maintained input hashes remain unchanged. No native record was edited. Empty optional fields are not automatically defects.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T095334Z-azidocillin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Azidocillin: exact neutral identity supported with historical assay and salt
  boundaries'
started_at: '2026-10-21T09:24:43Z'
finished_at: '2026-10-21T09:53:34Z'
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
summary: Current ChEBI, PubChem and ChEMBL corroborate the native four-centre neutral
  azidocillin structure. Source grounding, penicillin class and broad antimicrobial
  role are consistent. Historical antibacterial studies and patents support useful
  follow-up, but salt formulations, patent-wide stereochemical scope and missing original
  assay methods must remain explicit. Scientific assessment retains the stated evidence
  limits; full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/azidocillin.yaml
    sha256: a0ac1f0b1c4b237c3d84857797e514987ed313aad04c3638a51b463ecec06f64
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
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
targets:
- target_id: CHEBI:51758
  path: data/antibiotics/antibacterial/azidocillin.yaml
  label: azidocillin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition, chemical and literature links
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI fields or source grounding where applicable
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Fallback PubChem chemistry where applicable
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Fallback structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated fields and exact grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained grounding/exclusion policy
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position133; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:51758
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:51758
  command: .venv/bin/python /private/tmp/am-review-session/focus014-root.py 133
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:51758
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/azidocillin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:51758
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/azidocillin.yaml --out /private/tmp/am-review-session/133-strict.tsv
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
  - CHEBI:51758
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
  - CHEBI:51758
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
  - CHEBI:51758
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
  - CHEBI:51758
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
  - CHEBI:51758
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
  - CHEBI:51758
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
  - CHEBI:51758
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
  - CHEBI:51758
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
  - CHEBI:51758
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/azidocillin.yaml
  locator: Entire YAML including four seed/reseed events
  accessed_at: '2026-10-21T09:37:08Z'
  support: supports
  summary: Read exact ChEBI identity, ARO-derived definition/citation, all six synonyms,
    two parents, antimicrobial role, chemical encodings, four chemical xrefs, two
    drug xrefs, two patent documents and both source concepts. No populated mode,
    molecular target, resistance, quantitative activity, producer, clinical indication
    or graph fields.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv
  locator: 133-raw.json; seeder identity grouping and nearest drug-class extraction
  accessed_at: '2026-10-21T09:37:08Z'
  support: supports
  summary: ChEBI row945 and ARO row585 merge under51758. ARO direct parent3009124
    is below the configured drug class3000008, explaining the retained broad class
    parent. Adopted CHEBI33281 role agrees with current narrower antibacterial role33282
    through hierarchy. Both source mints and history reproduce.
  snapshot_sha256: 21b7808e0d7e2040c4dbaac0826d84fe93289af0fe76f4027728440fc687fec5
- evidence_id: identity
  kind: database
  reference: CHEBI:51758;PubChem CID:15574941;ChEMBL:CHEMBL2105907
  locator: Current chemical entries, parent terms and independent ChEMBL SMILES parsing
  accessed_at: '2026-10-21T09:37:08Z'
  support: supports
  summary: Neutral C16H17N5O4S and ODFHGIPNGIAMDK-NJBDSQKTSA-N agree across sources,
    with four assigned centres including the R side chain. Systematic synonyms encode
    the same graph; class CHEBI17334 penicillin and ARO3000008 are appropriate. CAS17243-38-8
    is corroborated as an official source crosswalk, not independently through the
    proprietary registry.
  snapshot_sha256: 9a048b0a15cd27f58bbc1d0467507dd1dfe31a88262fa55bd0ceb6685a472536
- evidence_id: adopted
  kind: database
  reference: PMID:4999682;PMID:3889939
  locator: 133-adopted.json; all metadata and abstract availability checked
  accessed_at: '2026-10-21T09:37:08Z'
  support: context_only
  summary: The definition citation resolves to the1969 controlled scarlet-fever study,
    DOI10.3109/inf.1969.1.issue-2.01, but has no indexed abstract. The class-associated
    beta-lactam review also has no abstract. Neither title alone establishes exact
    clinical outcomes, modern use or particular bacterial target.
  snapshot_sha256: b3e157f9898de5f6defc73c19d2a23dcf7e1d335d234ceb3c8bd1d8cf6a706d1
- evidence_id: activity
  kind: primary_source
  reference: PMID:183785;PMID:810753;PMID:1015013
  locator: Complete original abstracts in133-discovery.json
  accessed_at: '2026-10-21T09:37:08Z'
  support: partial
  summary: The1976 study183785 tests azidocillin against H.influenzae, enterococci,
    B.pertussis, S.aureus and group-A streptococci by serial dilution, with comparative
    rather than exact MIC numbers in the abstract. PMID810753 tests dental-root isolates
    by paper disks and reports susceptibility groups, not quantitative MICs. PMID1015013
    reports qualitative low-MIC activity against viridans streptococci. These support
    antibacterial context without universal strain susceptibility or a direct PBP-binding
    claim.
  snapshot_sha256: 1fe5b2814749b3b125adcd4b92da952c724c1f9b482b91a7a2155566afa5a30c
- evidence_id: clinical
  kind: primary_source
  reference: PMID:6894241;PMID:9519;PMID:1848
  locator: Complete indexed original abstracts in133-discovery.json
  accessed_at: '2026-10-21T09:37:08Z'
  support: partial
  summary: PK6894241 explicitly studies azidocillin sodium formulations and reports
    formulation-dependent exposure; it is not a neutral-free-acid dose experiment.
    Otitis9519 has three treatment groups and mixed bacteriological outcomes; pooled
    narrative cannot be assigned to one drug/strain. Sinusitis1848 distinguishes in-vitro
    MIC from elimination in patients. These historical studies do not establish current
    approval or treatment recommendations.
  snapshot_sha256: 1fe5b2814749b3b125adcd4b92da952c724c1f9b482b91a7a2155566afa5a30c
- evidence_id: patents
  kind: primary_source
  reference: patent:GB940488;patent:US3293242
  locator: Complete public US description/examples/claims and GB abstract in133-patentUS-visible.txt/133-patentGB-visible.txt
  accessed_at: '2026-10-21T09:37:08Z'
  support: partial
  summary: Documents concern alpha-azidobenzylpenicillin and salts. The US text expressly
    encompasses D, L and DL side-chain forms; examples isolate potassium salts of
    reported55% and83% purity and describe S.aureus Oxford growth inhibition. That
    broad patent scope and preparation cannot be silently assigned as an exact neutral
    R-record MIC. Semisynthetic use of6-APA does not establish azidocillin production
    by its precursor-producing mould.
  snapshot_sha256: e55a57aeda15573a4a2889948d317dacc5a91569771566688219bed1783c63dc
- evidence_id: drug-xrefs
  kind: database
  reference: DrugCentral273;DrugBankDB08795
  locator: 133-drugcentral-visible.txt;133-drugbank retrieval
  accessed_at: '2026-10-21T09:37:08Z'
  support: partial
  summary: DrugCentral named card, CAS/formula and crosswalks agree; salt synonyms
    and predicted PK/toxicity fields are drug-context information, not exact chemical
    equivalence or experimental mechanisms. DrugBank returned403. These are correctly
    typed drug_xrefs, distinct from structure xrefs and patent documents. No current
    approval inference follows from the page.
  snapshot_sha256: 0a5ceec7458403b4cf3ded649781470f56df7ca98a35b6ef3342e8f669695335
- evidence_id: discovery
  kind: database
  reference: Bounded azidocillin literature search
  locator: 133-discovery.json;57 returned records and available abstracts
  accessed_at: '2026-10-21T09:37:08Z'
  support: context_only
  summary: Other records concern host allergy, analytical standards, formulation stability,
    PK and historical clinical use. Docking-only GLP1/NDM1 hits are not direct enzyme
    inhibition or antimicrobial targets. Later broad patent lists are not compound-specific
    efficacy experiments; no claim is imported merely from a name appearing in them.
  snapshot_sha256: 1fe5b2814749b3b125adcd4b92da952c724c1f9b482b91a7a2155566afa5a30c
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit and source-mint checks
  locator: 133-chemistry.json;014-root-xref-checks.json
  accessed_at: '2026-10-21T09:37:08Z'
  support: supports
  summary: Both native encodings reproduce the full key, formula, charge, one component,
    exact mass and source mint. Stored average masses agree within the stated decimal
    precision tolerance; azamulin uses a 0.1-unit tolerance for its one-decimal source
    value. Focused schema and strict commands exit 0.
  snapshot_sha256: fc0066a2dc46007ee2b476ebe39e37704cb40201745e8230189bf447d18b292c
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 133-local-hits.txt;133-maintained-search.txt
  accessed_at: '2026-10-21T09:37:08Z'
  support: context_only
  summary: Maintained exact-name/identifier/key searches found the source rows and
    readiness inventory, without an exact-target curator override. Azidocillin numeric
    search also returned an unrelated ambiguine Reaxys identifier, rejected as a substring
    collision.
  search_scope: rg --no-ignore --hidden in the isolated checkout excluding .git/.venv;
    additional same-mode search across curation, conf, scripts, data/raw, src, reports
    and reviews. Current official chemical and ARO sources, adopted citation metadata/available
    abstracts and bounded free primary literature follow-up.
  snapshot_sha256: 4aa00f9d795baa4d70e67907288676807512f1f6459f409e6ba7c90d8d7a626f
assessments:
- assessment_id: provenance
  area: provenance
  topic: Source reproduction, ownership and native status
  outcome: supported
  summary: Captured maintained inputs remain unchanged. Source extraction and seeding
    explain native fields; structured review does not change SEEDED status.
  target_ids:
  - CHEBI:51758
  evidence_ids:
  - native
  - source
  - chemistry
- assessment_id: schema
  area: schema
  topic: Focused validation
  outcome: supported
  summary: Schema and strict checks pass. Internal validity does not establish exact
    equivalence of every external cross-reference or prove all biological claims.
  target_ids:
  - CHEBI:51758
  evidence_ids:
  - chemistry
- assessment_id: identity
  area: identity
  topic: Exact neutral structure and synonyms
  outcome: supported
  summary: Independent sources corroborate four-centre neutral azidocillin; salts
    and patent mixtures retain separate scope.
  target_ids:
  - CHEBI:51758
  evidence_ids:
  - identity
  - chemistry
  - patents
  - drug-xrefs
- assessment_id: grounding
  area: grounding
  topic: Parents, role and two-source merge
  outcome: supported
  summary: Hierarchy and configured nearest class explain native parents and antimicrobial
    classification; both source concepts reproduce.
  target_ids:
  - CHEBI:51758
  evidence_ids:
  - source
  - identity
- assessment_id: activity
  area: evidence
  topic: Definition and original antimicrobial evidence
  outcome: supported
  summary: Original abstracts support antibacterial activity. Exact1969 cited outcomes
    and full strain-specific methods remain unavailable. Narrow-spectrum is a source
    classification, not a statement of inactivity against every Gram-negative strain.
  target_ids:
  - CHEBI:51758
  evidence_ids:
  - adopted
  - activity
  - clinical
- assessment_id: documents
  area: evidence
  topic: Patent and drug-context cross-references
  outcome: supported
  summary: Documents resolve at the stated access scope and their broader salt/stereo
    scope is not a native exact-equivalence claim.
  target_ids:
  - CHEBI:51758
  evidence_ids:
  - patents
  - drug-xrefs
- assessment_id: optional
  area: scope
  topic: Mechanism, producer, resistance and adapter applicability
  outcome: not_applicable
  summary: No native gene/protein/pathway/stress/transcriptomic assertion requires
    an adapter lookup. Optional empty objects are not defects; class analogy is insufficient
    to create a specific PBP target or biosynthetic producer.
  target_ids:
  - CHEBI:51758
  evidence_ids:
  - native
  - patents
  - discovery
findings:
- finding_id: F1
  issue_key: azidocillin-primary-assay-form-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Add exact historical activity evidence with salt and method limits
  description: Original antibacterial studies provide optional enrichment. Full assay
    conditions and preparation must be recovered before numerical annotation; patent
    potassium salts and sodium PK formulations must not be silently equated with the
    native neutral compound.
  target_ids:
  - CHEBI:51758
  field_paths:
  - evidence
  - activity_spectrum
  - discussions
  evidence_ids:
  - activity
  - clinical
  - patents
  - adopted
  rule_id: 'native-review-checklist: Exact identity, evidence scope and completeness'
  native_severity: informational
  normalization_reason: Original antibacterial studies provide optional enrichment.
    Full assay conditions and preparation must be recovered before numerical annotation;
    patent potassium salts and sodium PK formulations must not be silently equated
    with the native neutral compound.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/azidocillin.yaml
    role: Curator-owned primary activity, evidence and discussion annotations
actions:
- action_id: A1
  description: Retrieve original exact-compound assay and formulation details for
    bounded curation.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:51758
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/azidocillin.yaml
    role: Curator-owned primary activity, evidence and discussion annotations
  acceptance_checks:
  - Recover the cited1969 paper and relevant in-vitro methods before recording strain-level
    MICs or historical clinical outcomes.
  - Distinguish paper-disk susceptibility groups from MIC values, and shared multi-drug
    results from drug-specific outcomes.
  - Preserve neutral R side-chain identity, tested salt, purity and patent D/L/DL
    scope; do not infer azidocillin production from6-APA precursor fermentation.
  - Keep clinical history and experimental PK distinct from current approval or treatment
    recommendations; use claim-level primary evidence and native curation history
    helpers.
limitations:
- The two adopted bibliographic leads lack indexed abstracts, and their full manuscripts
  were not retrieved. Additional activity/PK/clinical articles remain abstract-level.
  No exact assay table or contemporary approval audit is claimed.
- US patent description/examples/claims and GB abstract were read; original patent
  formula images and all patent-family documents were not independently audited. No
  patent legal-status judgment is made.
- DrugBank access returned403; DrugCentral card was inspected as a drug-context crosswalk,
  not an independently parsed exact structural export. The absence of a target field
  is not evidence that a molecular mechanism does not exist.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 21 captured maintained input hashes remain unchanged. No native record was edited.
  Empty optional fields are not automatically defects.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:51758
- https://pubmed.ncbi.nlm.nih.gov/183785/
- https://patents.google.com/patent/US3293242A/en
```
