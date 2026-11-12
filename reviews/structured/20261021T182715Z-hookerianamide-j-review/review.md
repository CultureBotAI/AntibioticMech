# Review of hookerianamide J

- Review: 20261021T182715Z-hookerianamide-j-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:01:00Z
- Finished UTC: 2026-10-21T18:27:15Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The exact steroidal alkaloid identity, structural parents and source provenance agree with independent current authorities. Original abstract and structure diagram support the J assignment; compound-specific database extracts support the recorded antibacterial and antileishmanial roles, with the original assay tables unavailable. No confirmed native defect was found. Later host-protein docking is not evidence of an antimicrobial molecular target. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 537; all original 13 captured inputs preserved, with actual ChEBI owners identified before scientific assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:66022 | data/antibiotics/antibacterial/hookerianamide-j.yaml | generated | hookerianamide J |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:66022 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:66022 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:66022 | Actual focused execution exited 0. |
| Independent exact chemical authority comparison | passed | False | CHEBI:66022 | Nine native/current authority encodings agree at complete key, formula and charge with reciprocal chirality-aware atom mapping. |
| Source, history and input audit | passed | False | CHEBI:66022 | All original 13 hashes unchanged; three chronological history events, deterministic source mint, sole adopted PMID and ten exact database assay rows checked. |
| Authoritative full QC | failed | True | CHEBI:66022 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:66022 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:66022 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:66022 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:66022 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:66022 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:66022 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:66022 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:66022 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact J constitution and configured stereochemistry

identity: supported. Targets: CHEBI:66022.

The source diagram and nine current/native encodings agree. The full original spectroscopic assignment was unavailable, so authority agreement is not represented as a reanalysis of natural-product NMR.

### Names, parents and exact source grounding

grounding: supported. Targets: CHEBI:66022.

Both systematic names and all four structural parents match the configured graph; source mint and current CHEBI66022 are consistent. Direct Reaxys verification remains limited to the source assertion.

### Exact J antibacterial and antileishmanial scope

scope: supported. Targets: CHEBI:66022.

The retained qualitative roles have compound-specific source-linked database support in the stated assays. Original methods, strains and assay tables remain unverified; neither zones nor host enzyme inhibition are relabelled as antimicrobial target or clinical evidence.

### Optional exact J antimicrobial target

completeness: unknown. Targets: CHEBI:66022.

No target is natively asserted. The later exact J POP study is a computational host-pharmacology lead, not a missing validated antimicrobial mechanism. No bacterial protein/pathway follow-up was triggered, so the structured bacterial adapter is not applicable.

### Plant isolation versus biosynthetic producer

scope: supported. Targets: CHEBI:66022.

The exact original abstract supports isolation from S.hookeriana. No BGC or demonstrated biosynthetic-producer object is inferred from plant isolation.

### Maintained inputs and adopted citation coverage

provenance: supported. Targets: CHEBI:66022.

The sole adopted PMID was inspected at available original depth; current database extraction supplements rather than substitutes silently for its unread main. All13 original hashes and native history remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/hookerianamide-j.yaml; Entire record: definition, two exact synonyms, four parents, two roles, chemical structure, Reaxys link, source concept and three history events | supports | The native SEEDED/EXACT record represents neutral hookerianamide J with configured steroid stereochemistry. It asserts antibacterial and antileishmanial activity and plant isolation, with no native target, pathway, MIC, resistance, clinical claim, causal graph or structured producer object. |
| identity | CHEBI:66022;pubchem.compound:25016666;CHEMBL496487; 537-authority-chemistry.json; current537-chebi-66022.json/.mol,537-pubchem.json,537-chembl-search.json; retrieval manifests537-fetch.json/537-fetch2.json | supports | Native SMILES and InChI plus current ChEBI, PubChem and ChEMBL structures agree at UBWMSSICUOCSHT-BJHCZKLTSA-N, C28H46N2O2 and zero charge. Reciprocal chirality-aware atom mapping verifies nine tetrahedral centres; masses agree at declared precision. The two exact names describe the senecoylamino, 4-hydroxy, 20-dimethylamino delta16 steroid shown in the source diagram. |
| terms | CHEBI:140325;CHEBI:26767;CHEBI:35681;CHEBI:51751;CHEBI:33282;CHEBI:70868; 537-chebi-*.json; exact current term definitions read and structural predicates compared | supports | The secondary carboxamide, steroid alkaloid, secondary alcohol and enamide parents match the graph. CHEBI51751 explicitly defines an alpha,beta-unsaturated carboxamide, which includes the senecoyl group. Native activity terms resolve. Current ChEBI reproduces Reaxys18885924; direct licensed Reaxys structure was not accessed. |
| original | PMID:18681480;DOI:10.1021/np800305b; 537-adopted-core.json; 537-repository.pdf, entire one-page abstract and structure diagram visually read; repository URL and SHA in537-fetch3.json | supports | The discovery identifies J as compound1 and K as2 from Sarcococca hookeriana. The original diagram gives J the N-senecoyl group, 4-OH and delta16,17 bond with explicit steroid stereochemistry. The abstract reports cholinesterase inhibition and testing against L.major and four bacteria. It does not give the exact J bacterial results; the downloaded repository item contains only this one page, not the full main. |
| activity | CHEMBL496487;CHEMBL1156637;PMID:18681480; 537-chembl-activity.json, all ten rows read; exact compound graph independently mapped | supports | The source-linked J extraction reports L.major IC50 11.3 micromolar and agar-well zones of15mm for B.subtilis and12mm for the source-named P.pallida at1mg/mL. M.luteus and source-named S.faecalis are marked not active in that zone assay. Separate extracted MIC rows are141.4 and70.7 micromolar for B.subtilis and P.pallida; they are not inferred from zones. Cholinesterase entries concern host pharmacology. These are database-extracted values, not original tables inspected by this reviewer. |
| host-computation | PMID:33897801;DOI:10.1155/2021/6687572; 537-PMC8052153.html/.txt; full abstract, Methods, J-specific docking/MD Results and Discussion/Conclusion inspected | supports | The study retrieves J from ChEBI and computationally screens prolyl oligopeptidase in a Parkinson disease context. Docking and dynamics propose interactions and explicitly motivate future in-vitro testing. They do not show measured J binding, bacterial killing or an antimicrobial POP mechanism. The supplement was not inspected. |
| owners | data/raw/chebi_antimicrobials.tsv;data/raw/chebi_role_names.tsv;scripts/extract_source_inventory.py;scripts/seed_from_sources.py;curation/decisions.tsv;conf/sources.yaml; 537-raw-rows.json;537-owners-search.json;537-source-audit.json | supports | Exact source row reproduces the native definition and structure. All actual owners were already among the original13 inputs, whose hashes remain unchanged. The source-concept mint and three chronological events reproduce. The owner search explicitly includes ignored and hidden files. |
| search | Public exact J source and mechanism discovery; 537-discovery.json;537-fetch*.json;537-source-audit.json | supports | All91 discovery titles were screened; the adopted2008 source and exact J2021 host-computational source were followed at declared depth. ACS main/PDF requests failed403; Bielefeld returned an anti-bot page and the SEKU repository provided only a one-page abstract/diagram. No exact antimicrobial molecular target was established in this bounded inspection. |

## Limits And Additional Notes

- The2008 full main and original spectroscopic/assay tables were not obtained. ACS requests failed403; Bielefeld was an anti-bot page; the accessible institutional PDF is only a one-page abstract and diagram. The exact DOI Figshare resource query returned an empty list, which is not proof that no supplement exists.
- Exact J assay values are current ChEMBL literature extracts. Original bacterial strain identifiers, detailed agar-well and MIC protocols, parasite stage, replicate/error data and source enzyme species were not independently verified; no quantitative native enrichment is proposed from these extracts alone.
- Reaxys18885924 is reproduced by the native and live ChEBI record; direct licensed Reaxys data were not accessed.
- The2021 J POP primary was read at abstract, methods and exact J results/discussion depth, not all unrelated compound passages or supplement. Its computation cannot establish experimental target binding or antimicrobial action.
- The91-result discovery query includes irrelevant full-text matches; titles were screened, not all abstracts/full papers read. This bounded review does not prove absence of later activity or mechanism studies.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All original13 hashes remain unchanged; actual owners were already captured. Standalone chemistry019 runs against054; schema, strict and source ledger use054.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T182715Z-hookerianamide-j-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of hookerianamide J
started_at: '2026-10-21T18:01:00Z'
finished_at: '2026-10-21T18:27:15Z'
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
summary: The exact steroidal alkaloid identity, structural parents and source provenance
  agree with independent current authorities. Original abstract and structure diagram
  support the J assignment; compound-specific database extracts support the recorded
  antibacterial and antileishmanial roles, with the original assay tables unavailable.
  No confirmed native defect was found. Later host-protein docking is not evidence
  of an antimicrobial molecular target. Scientific assessment retains the stated evidence
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
  - path: data/antibiotics/antibacterial/hookerianamide-j.yaml
    sha256: 6b57a21b0ace74616611202e2a93ad44346b87ce478c367673a3bf5e22fde007
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
- target_id: CHEBI:66022
  path: data/antibiotics/antibacterial/hookerianamide-j.yaml
  label: hookerianamide J
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Exact identity, definition, synonyms, parents, roles and adopted lead
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_role_names.tsv
    role: Role labels
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record and role policy
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusions
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Class and role configuration
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 537; all original 13 captured inputs
    preserved, with actual ChEBI owners identified before scientific assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:66022
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:66022
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    537
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:66022
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/hookerianamide-j.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:66022
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/hookerianamide-j.yaml --out /private/tmp/am-review-session/537-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority
  name: Independent exact chemical authority comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/537-authority-check.py
    > /private/tmp/am-review-session/537-authority-check.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Nine native/current authority encodings agree at complete key, formula
    and charge with reciprocal chirality-aware atom mapping.
  target_ids:
  - CHEBI:66022
- check_id: ledger
  name: Source, history and input audit
  command: .venv/bin/python /private/tmp/am-review-session/537-ledger.py > /private/tmp/am-review-session/537-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All original 13 hashes unchanged; three chronological history events, deterministic
    source mint, sole adopted PMID and ten exact database assay rows checked.
  target_ids:
  - CHEBI:66022
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:66022
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
  - CHEBI:66022
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
  - CHEBI:66022
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
  - CHEBI:66022
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
  - CHEBI:66022
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
  - CHEBI:66022
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
  - CHEBI:66022
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
  - CHEBI:66022
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
  - CHEBI:66022
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/hookerianamide-j.yaml
  locator: 'Entire record: definition, two exact synonyms, four parents, two roles,
    chemical structure, Reaxys link, source concept and three history events'
  accessed_at: '2026-10-21T18:17:49Z'
  support: supports
  summary: The native SEEDED/EXACT record represents neutral hookerianamide J with
    configured steroid stereochemistry. It asserts antibacterial and antileishmanial
    activity and plant isolation, with no native target, pathway, MIC, resistance,
    clinical claim, causal graph or structured producer object.
- evidence_id: identity
  kind: validation
  reference: CHEBI:66022;pubchem.compound:25016666;CHEMBL496487
  locator: 537-authority-chemistry.json; current537-chebi-66022.json/.mol,537-pubchem.json,537-chembl-search.json;
    retrieval manifests537-fetch.json/537-fetch2.json
  accessed_at: '2026-10-21T18:17:49Z'
  support: supports
  summary: Native SMILES and InChI plus current ChEBI, PubChem and ChEMBL structures
    agree at UBWMSSICUOCSHT-BJHCZKLTSA-N, C28H46N2O2 and zero charge. Reciprocal chirality-aware
    atom mapping verifies nine tetrahedral centres; masses agree at declared precision.
    The two exact names describe the senecoylamino, 4-hydroxy, 20-dimethylamino delta16
    steroid shown in the source diagram.
  snapshot_sha256: e6d6ee71cdce6beae1702576fcc5b7fc982c19357f21565df7f8b1b34438e600
- evidence_id: terms
  kind: database
  reference: CHEBI:140325;CHEBI:26767;CHEBI:35681;CHEBI:51751;CHEBI:33282;CHEBI:70868
  locator: 537-chebi-*.json; exact current term definitions read and structural predicates
    compared
  accessed_at: '2026-10-21T18:17:49Z'
  support: supports
  summary: The secondary carboxamide, steroid alkaloid, secondary alcohol and enamide
    parents match the graph. CHEBI51751 explicitly defines an alpha,beta-unsaturated
    carboxamide, which includes the senecoyl group. Native activity terms resolve.
    Current ChEBI reproduces Reaxys18885924; direct licensed Reaxys structure was
    not accessed.
  snapshot_sha256: 5cdd393cc530233a5e4d9f7a6e69a10280bf0a0c0b1ef703322914a9172110f4
- evidence_id: original
  kind: primary_source
  reference: PMID:18681480;DOI:10.1021/np800305b
  locator: 537-adopted-core.json; 537-repository.pdf, entire one-page abstract and
    structure diagram visually read; repository URL and SHA in537-fetch3.json
  accessed_at: '2026-10-21T18:17:49Z'
  support: supports
  summary: The discovery identifies J as compound1 and K as2 from Sarcococca hookeriana.
    The original diagram gives J the N-senecoyl group, 4-OH and delta16,17 bond with
    explicit steroid stereochemistry. The abstract reports cholinesterase inhibition
    and testing against L.major and four bacteria. It does not give the exact J bacterial
    results; the downloaded repository item contains only this one page, not the full
    main.
  snapshot_sha256: f584cbc50c1a1c6cc011810e4692ea5c86776084089605482b1f44e3c3bd608b
- evidence_id: activity
  kind: database
  reference: CHEMBL496487;CHEMBL1156637;PMID:18681480
  locator: 537-chembl-activity.json, all ten rows read; exact compound graph independently
    mapped
  accessed_at: '2026-10-21T18:17:49Z'
  support: supports
  summary: The source-linked J extraction reports L.major IC50 11.3 micromolar and
    agar-well zones of15mm for B.subtilis and12mm for the source-named P.pallida at1mg/mL.
    M.luteus and source-named S.faecalis are marked not active in that zone assay.
    Separate extracted MIC rows are141.4 and70.7 micromolar for B.subtilis and P.pallida;
    they are not inferred from zones. Cholinesterase entries concern host pharmacology.
    These are database-extracted values, not original tables inspected by this reviewer.
  snapshot_sha256: 7c33775cd23328f8dff81ae1ff828433e011f64e7d67b5422e7a681983c4f572
- evidence_id: host-computation
  kind: primary_source
  reference: PMID:33897801;DOI:10.1155/2021/6687572
  locator: 537-PMC8052153.html/.txt; full abstract, Methods, J-specific docking/MD
    Results and Discussion/Conclusion inspected
  accessed_at: '2026-10-21T18:17:49Z'
  support: supports
  summary: The study retrieves J from ChEBI and computationally screens prolyl oligopeptidase
    in a Parkinson disease context. Docking and dynamics propose interactions and
    explicitly motivate future in-vitro testing. They do not show measured J binding,
    bacterial killing or an antimicrobial POP mechanism. The supplement was not inspected.
  snapshot_sha256: 9972a4492a77e516ef88b5eac2fb43ed769b33e31d322e0c57f2a1e2ba00a073
- evidence_id: owners
  kind: validation
  reference: data/raw/chebi_antimicrobials.tsv;data/raw/chebi_role_names.tsv;scripts/extract_source_inventory.py;scripts/seed_from_sources.py;curation/decisions.tsv;conf/sources.yaml
  locator: 537-raw-rows.json;537-owners-search.json;537-source-audit.json
  accessed_at: '2026-10-21T18:17:49Z'
  support: supports
  summary: Exact source row reproduces the native definition and structure. All actual
    owners were already among the original13 inputs, whose hashes remain unchanged.
    The source-concept mint and three chronological events reproduce. The owner search
    explicitly includes ignored and hidden files.
  snapshot_sha256: 310633eb5b1a0d3493d9d72065b97cd8de48aa451ce4a3b84ef61e3509d86345
- evidence_id: search
  kind: search
  reference: Public exact J source and mechanism discovery
  locator: 537-discovery.json;537-fetch*.json;537-source-audit.json
  accessed_at: '2026-10-21T18:17:49Z'
  support: supports
  summary: All91 discovery titles were screened; the adopted2008 source and exact
    J2021 host-computational source were followed at declared depth. ACS main/PDF
    requests failed403; Bielefeld returned an anti-bot page and the SEKU repository
    provided only a one-page abstract/diagram. No exact antimicrobial molecular target
    was established in this bounded inspection.
  search_scope: Ignored-inclusive native-owner label, identifier and key search; EuropePMC
    hookerianamide query; exact PMID/DOI/title searches; public publisher, institutional
    repository, OpenAlex and official exact chemical authority routes.
  snapshot_sha256: 310633eb5b1a0d3493d9d72065b97cd8de48aa451ce4a3b84ef61e3509d86345
assessments:
- assessment_id: chemical
  area: identity
  topic: Exact J constitution and configured stereochemistry
  outcome: supported
  summary: The source diagram and nine current/native encodings agree. The full original
    spectroscopic assignment was unavailable, so authority agreement is not represented
    as a reanalysis of natural-product NMR.
  target_ids:
  - CHEBI:66022
  evidence_ids:
  - identity
  - original
- assessment_id: grounding
  area: grounding
  topic: Names, parents and exact source grounding
  outcome: supported
  summary: Both systematic names and all four structural parents match the configured
    graph; source mint and current CHEBI66022 are consistent. Direct Reaxys verification
    remains limited to the source assertion.
  target_ids:
  - CHEBI:66022
  evidence_ids:
  - record
  - identity
  - terms
  - owners
- assessment_id: activity
  area: scope
  topic: Exact J antibacterial and antileishmanial scope
  outcome: supported
  summary: The retained qualitative roles have compound-specific source-linked database
    support in the stated assays. Original methods, strains and assay tables remain
    unverified; neither zones nor host enzyme inhibition are relabelled as antimicrobial
    target or clinical evidence.
  target_ids:
  - CHEBI:66022
  evidence_ids:
  - original
  - activity
- assessment_id: mechanism
  area: completeness
  topic: Optional exact J antimicrobial target
  outcome: unknown
  summary: No target is natively asserted. The later exact J POP study is a computational
    host-pharmacology lead, not a missing validated antimicrobial mechanism. No bacterial
    protein/pathway follow-up was triggered, so the structured bacterial adapter is
    not applicable.
  target_ids:
  - CHEBI:66022
  evidence_ids:
  - record
  - host-computation
  - search
- assessment_id: producer
  area: scope
  topic: Plant isolation versus biosynthetic producer
  outcome: supported
  summary: The exact original abstract supports isolation from S.hookeriana. No BGC
    or demonstrated biosynthetic-producer object is inferred from plant isolation.
  target_ids:
  - CHEBI:66022
  evidence_ids:
  - original
  - record
- assessment_id: provenance
  area: provenance
  topic: Maintained inputs and adopted citation coverage
  outcome: supported
  summary: The sole adopted PMID was inspected at available original depth; current
    database extraction supplements rather than substitutes silently for its unread
    main. All13 original hashes and native history remain unchanged.
  target_ids:
  - CHEBI:66022
  evidence_ids:
  - owners
  - original
  - activity
findings: []
actions: []
limitations:
- The2008 full main and original spectroscopic/assay tables were not obtained. ACS
  requests failed403; Bielefeld was an anti-bot page; the accessible institutional
  PDF is only a one-page abstract and diagram. The exact DOI Figshare resource query
  returned an empty list, which is not proof that no supplement exists.
- Exact J assay values are current ChEMBL literature extracts. Original bacterial
  strain identifiers, detailed agar-well and MIC protocols, parasite stage, replicate/error
  data and source enzyme species were not independently verified; no quantitative
  native enrichment is proposed from these extracts alone.
- Reaxys18885924 is reproduced by the native and live ChEBI record; direct licensed
  Reaxys data were not accessed.
- The2021 J POP primary was read at abstract, methods and exact J results/discussion
  depth, not all unrelated compound passages or supplement. Its computation cannot
  establish experimental target binding or antimicrobial action.
- The91-result discovery query includes irrelevant full-text matches; titles were
  screened, not all abstracts/full papers read. This bounded review does not prove
  absence of later activity or mechanism studies.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All original13 hashes remain unchanged; actual owners were already captured. Standalone
  chemistry019 runs against054; schema, strict and source ledger use054.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
