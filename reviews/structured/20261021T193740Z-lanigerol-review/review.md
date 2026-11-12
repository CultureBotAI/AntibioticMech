# Lanigerol: supported identity with published pisiferanol correction

- Review: 20261021T193740Z-lanigerol-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:16:33Z
- Finished UTC: 2026-10-21T19:37:40Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native lanigerol graph and coarse antibacterial/origin claims are supported. The1996 original correction identifies lanigerol as previously known pisiferanol; it does not invalidate the native structure or correct its reported MIC. No confirmed native defect is established. Original full Methods and independent Reaxys equivalence remain unverified. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position591; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:66549 | data/antibiotics/antibacterial/lanigerol.yaml | generated | lanigerol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:66549 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:66549 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:66549 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:66549 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:66549 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:66549 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:66549 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:66549 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:66549 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:66549 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:66549 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:66549 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact graph and corrected historical name

identity: supported. Targets: CHEBI:66549.

Native serializations, systematic naming and current authorities agree. The primary correction and independent pisiferanol lookup support the alternate name without changing native chemical identity.

### Parents, role and registry scope

grounding: unknown. Targets: CHEBI:66549.

Broader structural parents and the antibacterial role are consistent. Independent exact Reaxys equivalence remains unresolved; this access limit alone is not a finding.

### Root isolation and coarse antibacterial claim

evidence: supported. Targets: CHEBI:66549.

The original abstract directly supports the stated origin and coarse Gram-positive activity. The unavailable detailed Methods prevent strain-level quantitative enrichment or an asserted mechanism.

### Native/source coverage and generation history

provenance: supported. Targets: CHEBI:66549.

All populated fields and the sole adopted citation are dispositioned; deterministic mint and original owner hashes are intact.

### Optional corrected alias and primary follow-up

completeness: supported. Targets: CHEBI:66549.

Adding the corrected pisiferanol alias and earlier isolation source is useful optional work. Missing optional targets, MIC objects or synonym completeness is not itself a native error.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optional corrected-name and primary-evidence enrichment.

- If adding pisiferanol, cite the1996 original correction and verify exact structure scope. Do not assert that the1995 paper was the first natural isolation.
- Obtain original1995/1985/2001 full text before importing exact strains, assay methods or experimental absolute-configuration claims. Keep the reported1 mg/mL abstract value unchanged unless primary correction evidence establishes otherwise.
- Verify the licensed Reaxys graph if accessible; do not invent a target from other icetexanes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/lanigerol.yaml; Entire native YAML, including both exact names, four parents, role, chemistry, sole xref, source concept and three history events. | supports | SEEDED/EXACT CHEBI66549 is neutral C20H30O2, key UZNOTFOFROXACM-ICSRJNTNSA-N, with two assigned S centres. The definition describes an icetexane isolated from Salvia lanigera roots with antibacterial activity; it does not claim first discovery. No molecular target, quantitative activity, resistance, clinical claim, producer object or causal graph is asserted. |
| owners | data/raw/chebi_antimicrobials.tsv:1580;conf/sources.yaml;scripts/extract_source_inventory.py;scripts/seed_from_sources.py; Exact maintained source row, relevant extraction/emission branches and ignored-inclusive owner searches. | supports | The adopted row owns the native fields and lists PMID8824952 as a literature lead. Source citations are not automatically emitted as claim evidence. The mint independently reproduces antibioticmech:chebi-05afda824a. The three generation events are chronological. No exact curator/decision overlay was found in the inspected hidden/ignored-inclusive searches. Original thirteen hashes already capture the actual owners and remain unchanged. |
| authorities | CHEBI:66549;PubChem:188496; Complete official ChEBI JSON and PubChem properties; independent native/current-authority structure calculations. | supports | All six native/current structural encodings reproduce the same full key, C20H30O2, charge0, mass302.22458020 and two accurate S centres. The systematic4aS,11aS synonym and conventional abeo-abietane name describe the same icetexane scaffold. The diterpenoid, tertiary-alcohol, phenol and carbotricyclic parents fit. Reaxys6062537 is repeated by current ChEBI but its licensed graph was not independently inspected. |
| original1995 | PMID:8824952;DOI:10.1055/s-2006-959372; Complete original abstract and bibliographic metadata, including the indexed erratum link. | supports | The1995 paper reports isolation of the named icetexane from S. lanigera roots and activity against Gram-positive bacteria with an abstract MIC of1 mg/mL. The unit is retained exactly as reported; it is not silently changed to micrograms. Original full assay Methods, strains, material purity and stereochemical assignment were not accessible through attempted free publisher routes. |
| erratum1996 | DOI:10.1055/s-2006-957885;Planta Medica62(3):288; Complete lanigerol correction paragraph in the publisher PDF as indexed by the web retrieval tool; direct local PDF requests returned HTML challenges. | supports | The primary correction states that lanigerol had already been isolated from Chamaecyparis pisifera as pisiferanol in Phytochemistry1985,24(7),1545–1551. The Salvia report was its second natural isolation and first from Labiatae. This corrects novelty/naming history; it does not state a changed structure or an MIC-unit correction. Because the native definition does not assert novelty, this is optional synonym/source enrichment rather than a confirmed defect. |
| alias | PubChem name/pisiferanol/property endpoint; Complete official property response for the corrected original name. | supports | The pisiferanol query returns the same CID188496 and exact native full key. It corroborates the correction at database level without substituting for the original1985 experimental text, which was not obtained. |
| secondary-leads | DOI:10.1039/B908984E;DOI:10.1002/cbdv.202200793; Selected2009 review identity discussion/references and2022 accepted-manuscript introduction read; neither whole review claimed read. | context_only | The2009 review directs to the original1985 isolation,1995 activity report and1996 correction, and a2001 Chamaecyparis paper at Chem Pharm Bull49:1479–1481. Its biological summaries are leads only. The2022 introduction uses lanigerol as an antimicrobial example; novel congeners and their activities elsewhere are not transferred. The2001 J-Stage PDF attempt returned500 and was not inspected. |
| search | 591-discovery.json;591-pisiferanol-discovery.json;591-local-hits.txt;591-owner-hits.txt; All three lanigerol and six pisiferanol result titles screened; complete relevant indexed abstracts and bounded public primary follow-up. | context_only | The1998 Salvia root orthoquinone paper concerns lanigerone, salvigerone, arucadiol and pisiferal, not exact lanigerol, and supplies no transferable mechanism. Broader reviews and plant-metabolomics results are not primary exact antibacterial evidence. The native contains no gene/pathway/stress assertion requiring a structured-adapter query; that applicability decision preceded open research. No exhaustive-literature or universal-inactivity claim is made. |

## Limits And Additional Notes

- The original1995 paper was read at complete-abstract depth only. The entire short lanigerol correction was read in indexed publisher PDF text, while direct PDF downloads yielded HTML challenges.
- The original1985 study and2001 full text were not obtained. Selected2009/2022 review passages were used as leads only. Current database stereo agreement is not an independent reconstruction of the historical absolute-configuration experiment.
- Reaxys equivalence remains unverified and the literature search was bounded. No MIC object, clinical efficacy or direct antibacterial target is inferred.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All13 original inputs remain unchanged. No native fields or curation status were modified. Shared full-QC disposition is attached during finalization.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T193740Z-lanigerol-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Lanigerol: supported identity with published pisiferanol correction'
started_at: '2026-10-21T19:16:33Z'
finished_at: '2026-10-21T19:37:40Z'
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
summary: The native lanigerol graph and coarse antibacterial/origin claims are supported.
  The1996 original correction identifies lanigerol as previously known pisiferanol;
  it does not invalidate the native structure or correct its reported MIC. No confirmed
  native defect is established. Original full Methods and independent Reaxys equivalence
  remain unverified. Scientific assessment retains the stated evidence limits; full
  verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/lanigerol.yaml
    sha256: 496c4e42c2940000d941e41f9db3eb430176755d6e35ee3fd9b7d946021ca63b
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
- target_id: CHEBI:66549
  path: data/antibiotics/antibacterial/lanigerol.yaml
  label: lanigerol
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
  selection: Initially uncovered queue position591; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:66549
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:66549
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    591
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:66549
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/lanigerol.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:66549
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/lanigerol.yaml --out /private/tmp/am-review-session/591-strict.tsv
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
  - CHEBI:66549
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
  - CHEBI:66549
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
  - CHEBI:66549
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
  - CHEBI:66549
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
  - CHEBI:66549
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
  - CHEBI:66549
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
  - CHEBI:66549
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
  - CHEBI:66549
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
  - CHEBI:66549
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/lanigerol.yaml
  locator: Entire native YAML, including both exact names, four parents, role, chemistry,
    sole xref, source concept and three history events.
  accessed_at: '2026-10-21T19:34:49Z'
  support: supports
  summary: SEEDED/EXACT CHEBI66549 is neutral C20H30O2, key UZNOTFOFROXACM-ICSRJNTNSA-N,
    with two assigned S centres. The definition describes an icetexane isolated from
    Salvia lanigera roots with antibacterial activity; it does not claim first discovery.
    No molecular target, quantitative activity, resistance, clinical claim, producer
    object or causal graph is asserted.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv:1580;conf/sources.yaml;scripts/extract_source_inventory.py;scripts/seed_from_sources.py
  locator: Exact maintained source row, relevant extraction/emission branches and
    ignored-inclusive owner searches.
  accessed_at: '2026-10-21T19:34:49Z'
  support: supports
  summary: The adopted row owns the native fields and lists PMID8824952 as a literature
    lead. Source citations are not automatically emitted as claim evidence. The mint
    independently reproduces antibioticmech:chebi-05afda824a. The three generation
    events are chronological. No exact curator/decision overlay was found in the inspected
    hidden/ignored-inclusive searches. Original thirteen hashes already capture the
    actual owners and remain unchanged.
  snapshot_sha256: 80bac01157c05eb624bcafb6ea40a2d0c9ed15866742ea02fb8be58efa890bad
- evidence_id: authorities
  kind: authority
  reference: CHEBI:66549;PubChem:188496
  locator: Complete official ChEBI JSON and PubChem properties; independent native/current-authority
    structure calculations.
  accessed_at: '2026-10-21T19:34:49Z'
  support: supports
  summary: All six native/current structural encodings reproduce the same full key,
    C20H30O2, charge0, mass302.22458020 and two accurate S centres. The systematic4aS,11aS
    synonym and conventional abeo-abietane name describe the same icetexane scaffold.
    The diterpenoid, tertiary-alcohol, phenol and carbotricyclic parents fit. Reaxys6062537
    is repeated by current ChEBI but its licensed graph was not independently inspected.
  snapshot_sha256: 6f9b4e94c432a0bd143e5b917f2a813453d7d1b99f3fe8566184323158a72479
- evidence_id: original1995
  kind: primary_source
  reference: PMID:8824952;DOI:10.1055/s-2006-959372
  locator: Complete original abstract and bibliographic metadata, including the indexed
    erratum link.
  accessed_at: '2026-10-21T19:34:49Z'
  support: supports
  summary: The1995 paper reports isolation of the named icetexane from S. lanigera
    roots and activity against Gram-positive bacteria with an abstract MIC of1 mg/mL.
    The unit is retained exactly as reported; it is not silently changed to micrograms.
    Original full assay Methods, strains, material purity and stereochemical assignment
    were not accessible through attempted free publisher routes.
  snapshot_sha256: 7aad7509abbb1f6823fd88c6d1bca9787ea5125fdbf5cc5c070066a581a9d216
- evidence_id: erratum1996
  kind: primary_source
  reference: DOI:10.1055/s-2006-957885;Planta Medica62(3):288
  locator: Complete lanigerol correction paragraph in the publisher PDF as indexed
    by the web retrieval tool; direct local PDF requests returned HTML challenges.
  accessed_at: '2026-10-21T19:34:49Z'
  support: supports
  summary: The primary correction states that lanigerol had already been isolated
    from Chamaecyparis pisifera as pisiferanol in Phytochemistry1985,24(7),1545–1551.
    The Salvia report was its second natural isolation and first from Labiatae. This
    corrects novelty/naming history; it does not state a changed structure or an MIC-unit
    correction. Because the native definition does not assert novelty, this is optional
    synonym/source enrichment rather than a confirmed defect.
  snapshot_sha256: 810f0e352944ddcd0d5e15ed2f0cb14f33e112838a3446b11abc7ad9ffdf2270
- evidence_id: alias
  kind: authority
  reference: PubChem name/pisiferanol/property endpoint
  locator: Complete official property response for the corrected original name.
  accessed_at: '2026-10-21T19:34:49Z'
  support: supports
  summary: The pisiferanol query returns the same CID188496 and exact native full
    key. It corroborates the correction at database level without substituting for
    the original1985 experimental text, which was not obtained.
  snapshot_sha256: 1211594483df30991f1af4f36eb7207bc3a3484e22533a7bf429bb8d52627c60
- evidence_id: secondary-leads
  kind: search
  reference: DOI:10.1039/B908984E;DOI:10.1002/cbdv.202200793
  locator: Selected2009 review identity discussion/references and2022 accepted-manuscript
    introduction read; neither whole review claimed read.
  accessed_at: '2026-10-21T19:34:49Z'
  support: context_only
  summary: The2009 review directs to the original1985 isolation,1995 activity report
    and1996 correction, and a2001 Chamaecyparis paper at Chem Pharm Bull49:1479–1481.
    Its biological summaries are leads only. The2022 introduction uses lanigerol as
    an antimicrobial example; novel congeners and their activities elsewhere are not
    transferred. The2001 J-Stage PDF attempt returned500 and was not inspected.
  search_scope: 2026-10-21; selected exact lanigerol/pisiferanol passages and referenced
    primary sources in two reviews; not whole-review coverage.
  snapshot_sha256: dd0c1a3302159f6ebc8d6da62e815eed2f0b9b7681ba44fa34b29016ce67f3ea
- evidence_id: search
  kind: search
  reference: 591-discovery.json;591-pisiferanol-discovery.json;591-local-hits.txt;591-owner-hits.txt
  locator: All three lanigerol and six pisiferanol result titles screened; complete
    relevant indexed abstracts and bounded public primary follow-up.
  accessed_at: '2026-10-21T19:34:49Z'
  support: context_only
  summary: The1998 Salvia root orthoquinone paper concerns lanigerone, salvigerone,
    arucadiol and pisiferal, not exact lanigerol, and supplies no transferable mechanism.
    Broader reviews and plant-metabolomics results are not primary exact antibacterial
    evidence. The native contains no gene/pathway/stress assertion requiring a structured-adapter
    query; that applicability decision preceded open research. No exhaustive-literature
    or universal-inactivity claim is made.
  search_scope: 2026-10-21; lanigerol, pisiferanol, CHEBI66549, full key, adopted
    PMID/DOI and correction; local search included ignored/hidden files.
  snapshot_sha256: 8bde46ec2280541b18ed7c06a73c91c9babe0822e6b0acee13bcc031639c4633
assessments:
- assessment_id: identity
  area: identity
  topic: Exact graph and corrected historical name
  outcome: supported
  summary: Native serializations, systematic naming and current authorities agree.
    The primary correction and independent pisiferanol lookup support the alternate
    name without changing native chemical identity.
  target_ids:
  - CHEBI:66549
  evidence_ids:
  - native
  - authorities
  - erratum1996
  - alias
- assessment_id: grounding
  area: grounding
  topic: Parents, role and registry scope
  outcome: unknown
  summary: Broader structural parents and the antibacterial role are consistent. Independent
    exact Reaxys equivalence remains unresolved; this access limit alone is not a
    finding.
  target_ids:
  - CHEBI:66549
  evidence_ids:
  - authorities
  - original1995
- assessment_id: activity
  area: evidence
  topic: Root isolation and coarse antibacterial claim
  outcome: supported
  summary: The original abstract directly supports the stated origin and coarse Gram-positive
    activity. The unavailable detailed Methods prevent strain-level quantitative enrichment
    or an asserted mechanism.
  target_ids:
  - CHEBI:66549
  evidence_ids:
  - original1995
  - erratum1996
  - search
- assessment_id: provenance
  area: provenance
  topic: Native/source coverage and generation history
  outcome: supported
  summary: All populated fields and the sole adopted citation are dispositioned; deterministic
    mint and original owner hashes are intact.
  target_ids:
  - CHEBI:66549
  evidence_ids:
  - native
  - owners
- assessment_id: completeness
  area: completeness
  topic: Optional corrected alias and primary follow-up
  outcome: supported
  summary: Adding the corrected pisiferanol alias and earlier isolation source is
    useful optional work. Missing optional targets, MIC objects or synonym completeness
    is not itself a native error.
  target_ids:
  - CHEBI:66549
  evidence_ids:
  - erratum1996
  - alias
  - secondary-leads
  - search
findings: []
actions:
- action_id: A1
  description: Optional corrected-name and primary-evidence enrichment.
  finding_ids: []
  target_ids:
  - CHEBI:66549
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained identity and source evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated field owner
  acceptance_checks:
  - If adding pisiferanol, cite the1996 original correction and verify exact structure
    scope. Do not assert that the1995 paper was the first natural isolation.
  - Obtain original1995/1985/2001 full text before importing exact strains, assay
    methods or experimental absolute-configuration claims. Keep the reported1 mg/mL
    abstract value unchanged unless primary correction evidence establishes otherwise.
  - Verify the licensed Reaxys graph if accessible; do not invent a target from other
    icetexanes.
limitations:
- The original1995 paper was read at complete-abstract depth only. The entire short
  lanigerol correction was read in indexed publisher PDF text, while direct PDF downloads
  yielded HTML challenges.
- The original1985 study and2001 full text were not obtained. Selected2009/2022 review
  passages were used as leads only. Current database stereo agreement is not an independent
  reconstruction of the historical absolute-configuration experiment.
- Reaxys equivalence remains unverified and the literature search was bounded. No
  MIC object, clinical efficacy or direct antibacterial target is inferred.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All13 original inputs remain unchanged. No native fields or curation status were
  modified. Shared full-QC disposition is attached during finalization.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
