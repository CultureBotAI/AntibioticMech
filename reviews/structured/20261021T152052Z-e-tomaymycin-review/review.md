# (E)-Tomaymycin: exact stereochemistry and original antibacterial evidence supported

- Review: 20261021T152052Z-e-tomaymycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:52:15Z
- Finished UTC: 2026-10-21T15:20:52Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native (2E,11R,11aS) methoxy structure, broader geometry-unspecified parent and antibacterial role agree with current ChEBI and the original structure/synthesis papers. The adopted original contains disc-diffusion activity for the exact E product. No corrective finding was established. Optional mechanism and quantitative activity enrichment require preserving methoxy/imine, C11-epimer and assay boundaries. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 388; one exact record. Original 13 input hashes preserved within 20 expanded inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:167317 | data/antibiotics/antibacterial/e-tomaymycin.yaml | generated | (E)-tomaymycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Structured-source applicability | not_applicable | False | CHEBI:167317 | No native named gene, protein, pathway or transcriptomics assertion is present. Bounded primary DNA-complex context was not converted into a protein target. |
| Focused chemistry verification | passed | False | CHEBI:167317 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:167317 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:167317 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:167317 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:167317 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:167317 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:167317 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:167317 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:167317 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:167317 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:167317 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:167317 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact E geometry and C11/C11a configuration

identity: supported. Targets: CHEBI:167317.

The native graph and single systematic synonym agree with current authority, primary NMR assignment and the separately synthesized E methyl ether. Z-tomaymycin and the demethanolated imine remain distinct.

### Authority, broader parent and source mint

grounding: supported. Targets: CHEBI:167317.

The exact identifier and mint resolve; the parent deliberately leaves alkene geometry unspecified and is strictly broader. No external chemical xref requires adjudication.

### ANTIBACTERIAL filing and retained role

scope: supported. Targets: CHEBI:167317.

The original exact E product inhibits bacterial growth in a disc assay. The native antibacterial role and configured filing are supported; antitumor or phage activity is not used as a bacterial surrogate.

### Definition and synonym support

evidence: supported. Targets: CHEBI:167317.

The concise E-isomer definition and systematic (2E,11R,11aS) synonym are correct at the represented structural scope. The single adopted primary lead was read beyond its abstract.

### Optional activity_spectrum

completeness: unknown. Targets: CHEBI:167317.

No native quantitative row is populated. The inspected original can support disc-zone observations if concentration and method limits are retained. Its solution concentrations must not be curated as MICs, and unreported strain identifiers or incubation details must remain unknown. Optional absence is not a required correction.

### Optional mode, molecular target, resistance and causal graph

completeness: unknown. Targets: CHEBI:167317.

The record has no molecular claim. The original DNA-complex experiments offer a bounded mechanistic lead, but enrichment should reconcile exact chemical/adduct states and distinguish observations from the historical intercalation/nuclease hypotheses. No resistance allele or direct protein target was established here.

### Producer, clinical and dataset domains

scope: not_applicable. Targets: CHEBI:167317.

No structured assertions occur. The historical producer lead is experimentally grounded at the stated strain identification, but no clinical approval, modern strain equivalence or dataset membership is inferred.

### Actual maintained owners and native history

provenance: supported. Targets: CHEBI:167317.

The complete native record reproduces the exact adopted ChEBI row and three seed/reseed events. Original 13 hashes remain preserved within expanded context capture, with SEEDED status unchanged.

### Focused gates

schema: supported. Targets: CHEBI:167317.

Chemistry, schema and strict validation pass. These checks complement the source review and do not establish assay equivalence or mechanistic sign-off by themselves.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/e-tomaymycin.yaml; Entire native record, one synonym, parent, role, graph, source concept and three history events | supports | The exact ChEBI-grounded SEEDED record represents (E)-tomaymycin with C11 R and C11a S. It has no external xref, mode, molecular target, resistance, quantitative activity, structured producer, clinical product, causal graph or dataset assertion. |
| owners | data/raw/chebi_antimicrobials.tsv; Exact CHEBI:167317 row 2795; parent row 2776 and Z sibling row 2796 | supports | The source supplies the native graph, synonym, antibacterial role and single adopted PMID6833147. The parent omits ethylidene geometry while retaining the same tetrahedral configuration. No exact curator/decision/ARO owner row was found in the hidden/ignored-inclusive local search. The extractor and seeder own these generated assertions. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/167317/; Current complete CHEBI:167317 authority response | supports | Current ChEBI exactly matches the native graph, key, neutral formula, masses, synonym, parent and adopted citation. Additional broad inherited roles shown by the API are not missing native antimicrobial roles under the configured scope. |
| parent | https://www.ebi.ac.uk/chebi/backend/api/public/compound/157681/; Current CHEBI:157681 structure and outgoing/incoming relations | supports | The parent is tomaymycin with unspecified E/Z geometry and the same C11/C11a configurations, so it is strictly broader than this E record. It is not an asserted exact chemical equivalent. Its separate literature bibliography was used only for bounded discovery, not treated as adopted claim-level evidence in this child. |
| chemistry | RDKit 2026.03.5 via batch 019 interpreter against batch 039 cwd; 388-chemistry.json and 388-stereo-parent.json | supports | Native SMILES and InChI reproduce UQVNRKBFAXNOGA-LWTNMJDUSA-N, C16H20N2O4, neutral charge and masses. Zero-based SMILES atom 0 is C11a S and atom 19 is C11 R; double bond 2–3 is E. The geometry-unspecified parent matches as a chiral substructure. The source mint is reproducible. |
| adopted | https://doi.org/10.7164/antibiotics.36.276; PMID6833147; Introduction, Scheme 3, Biological Activity/Table 1, final 1E/1Z preparation and interconversion sections | supports | The original synthesizes (11R,11aS)-E product 1E and Z product 1Z separately. The final E methyl ether has molecular ion 304 and C16H20N2O4 analysis. Scheme 3 distinguishes these methoxy products from demethanolated imines 16E/16Z and shows solvent-dependent interconversion. Actual Scheme 3 and Table 1 were viewed. This directly supports the exact native structural form rather than a Z or imine substitution. |
| activity | https://doi.org/10.7164/antibiotics.36.276; Printed pages 278–279, Table 1 and complete disc-method paragraph | supports | Ten-millimetre paper discs were saturated with compound solutions and placed on seeded agar. At 1360 micrograms/mL, E product 1E gave zones of 20, 25, 11 and 22 mm for S. aureus, B. subtilis, E. coli and P. vulgaris, respectively; P. aeruginosa was marked negative. These are solution concentrations and zone diameters, not MICs or mass per disc. The inspected method does not give strain accessions, incubation time/temperature or exact loading volume. Lower rows include plus signs whose quantitative meaning must not be invented. |
| structure-original | https://doi.org/10.7164/antibiotics.36.142; Printed pages 142–144: actual E/Z drawings, carbon-NMR geometry assignment and proton-coupling/model discussion | supports | The preceding original assigns natural tomaymycin as (11R,11aS)-E using carbon-NMR steric-shift comparisons of prepared E/Z models and proton-coupling constraints at C11. It reports agreement with the earlier Arora crystal structure, which was not independently re-refined here. The actual first-page drawing matches the methoxy E form. |
| isolation | https://doi.org/10.7164/antibiotics.25.437; PMID4648485; Introduction, fermentation, isolation, chemical characterization and antimicrobial Methods/Discussion | partial | The original isolated tomaymycin from strain A-2127, then identified as Streptomyces achromogenes var. tomaymyceticus. Methanol crystallization gave the C16H20N2O4 material; the paper distinguishes it from des-methanol product. Its older molecular-complex wording should not be converted into a disconnected methanol-solvate graph when the later primary chemistry explicitly establishes the covalent methyl ether. This historical isolation supports a bounded producer lead; no modern strain-taxonomy mapping is asserted. |
| mode-lead | https://doi.org/10.7164/antibiotics.25.660; PMID4630600; original Materials/Methods, Results and Discussion text | partial | Natural-source tomaymycin was tested in B. subtilis 168/W23 and with E. coli DNA. Precursor incorporation, methyl-green displacement, gel filtration and thermal/nuclease protection support DNA complex formation and inhibition of nucleic-acid biosynthesis. The authors discuss intercalation and nuclease repair as hypotheses. This does not identify a bacterial protein target, establish a specific covalent atom linkage by itself or justify converting nuclease protection into direct nuclease inhibition. Exact in-assay methoxy/imine/C11-adduct state remains a mapping consideration for later enrichment. |
| discovery | Ignored-inclusive local search and Europe PMC original-source discovery; 388389-all-local-paths.txt;388-discovery.json | context_only | The bounded search included exact label, slug, CHEBI:167317 and its key across hidden and ignored local inputs/reports. Historical reports were discovery leads only. Primary discovery also found later C11-epimeric DNA-adduct studies; no derivative/antitumor assay was substituted for exact E antibacterial evidence. |
| gates | Focused chemistry, schema and strict execution; 388-focused-results.json | supports | All focused checks pass. Native validators ran in batch 039; standalone RDKit used the existing batch 019 interpreter against batch 039 cwd. |

## Limits And Additional Notes

- The adopted 1983 paper was read at exact final-product synthesis, identity and complete antibacterial method/Table 1 scope, with actual Scheme 3/Table 1 and the preceding structure paper drawing viewed. Unrelated intermediate synthesis procedures and raw NMR spectra were not independently reprocessed.
- The disc assay lacks strain accessions, loading volume and incubation detail in the inspected method. Its concentrations and zones cannot be normalized into MICs.
- The 1972 isolation and mechanism originals were read at producer/material and experimental-mechanism scope. The earlier Arora crystal refinement and later C11 DNA-adduct experiments were not independently reanalyzed; exact reactive-state mapping remains a prerequisite for mechanistic enrichment.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native/source/status/history was edited. Optional links, tags and notes were checked against this exact E record.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T152052Z-e-tomaymycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: '(E)-Tomaymycin: exact stereochemistry and original antibacterial evidence
  supported'
started_at: '2026-10-21T14:52:15Z'
finished_at: '2026-10-21T15:20:52Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent whole-record and actual ChEBI-row review after input
    capture; live authority comparison, independent chemistry and original structure/synthesis/biological
    source reading, including actual structural drawings and activity table.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The native (2E,11R,11aS) methoxy structure, broader geometry-unspecified
  parent and antibacterial role agree with current ChEBI and the original structure/synthesis
  papers. The adopted original contains disc-diffusion activity for the exact E product.
  No corrective finding was established. Optional mechanism and quantitative activity
  enrichment require preserving methoxy/imine, C11-epimer and assay boundaries. Scientific
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
  - path: data/antibiotics/antibacterial/e-tomaymycin.yaml
    sha256: a9a84f2ac3c47f7014fed96996d2a16bf3618d9b063cea45d458fdc320d48ee5
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
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
targets:
- target_id: CHEBI:167317
  path: data/antibiotics/antibacterial/e-tomaymycin.yaml
  label: (E)-tomaymycin
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
  selection: Queue position 388; one exact record. Original 13 input hashes preserved
    within 20 expanded inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:167317
checks:
- check_id: structured-adapter
  name: Structured-source applicability
  status: not_applicable
  required: false
  target_ids:
  - CHEBI:167317
  summary: No native named gene, protein, pathway or transcriptomics assertion is
    present. Bounded primary DNA-complex context was not converted into a protein
    target.
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:167317
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/388389-focused.py
    (cwd /private/tmp/antibioticmech-record-reviews-039)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:167317
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/e-tomaymycin.yaml (cwd /private/tmp/antibioticmech-record-reviews-039)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:167317
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/e-tomaymycin.yaml --out /private/tmp/am-review-session/388-strict.tsv
    (cwd /private/tmp/antibioticmech-record-reviews-039)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:167317
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
  - CHEBI:167317
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
  - CHEBI:167317
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
  - CHEBI:167317
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
  - CHEBI:167317
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
  - CHEBI:167317
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
  - CHEBI:167317
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
  - CHEBI:167317
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
  - CHEBI:167317
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/e-tomaymycin.yaml
  locator: Entire native record, one synonym, parent, role, graph, source concept
    and three history events
  accessed_at: '2026-10-21T15:00:10Z'
  support: supports
  summary: The exact ChEBI-grounded SEEDED record represents (E)-tomaymycin with C11
    R and C11a S. It has no external xref, mode, molecular target, resistance, quantitative
    activity, structured producer, clinical product, causal graph or dataset assertion.
  snapshot_sha256: ce80a9a4a9b05a9760f5202550b62ad07c2402b7413a7100d8989b4041ac30ab
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Exact CHEBI:167317 row 2795; parent row 2776 and Z sibling row 2796
  accessed_at: '2026-10-21T15:00:10Z'
  support: supports
  summary: The source supplies the native graph, synonym, antibacterial role and single
    adopted PMID6833147. The parent omits ethylidene geometry while retaining the
    same tetrahedral configuration. No exact curator/decision/ARO owner row was found
    in the hidden/ignored-inclusive local search. The extractor and seeder own these
    generated assertions.
  snapshot_sha256: ce80a9a4a9b05a9760f5202550b62ad07c2402b7413a7100d8989b4041ac30ab
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/167317/
  locator: Current complete CHEBI:167317 authority response
  accessed_at: '2026-10-21T14:57:52.428663Z'
  support: supports
  summary: Current ChEBI exactly matches the native graph, key, neutral formula, masses,
    synonym, parent and adopted citation. Additional broad inherited roles shown by
    the API are not missing native antimicrobial roles under the configured scope.
  snapshot_sha256: 8b42404822bdf77d8ff5331e7f661eaedb318d199c7ca9537100bed2840af28a
- evidence_id: parent
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/157681/
  locator: Current CHEBI:157681 structure and outgoing/incoming relations
  accessed_at: '2026-10-21T14:57:52.430667Z'
  support: supports
  summary: The parent is tomaymycin with unspecified E/Z geometry and the same C11/C11a
    configurations, so it is strictly broader than this E record. It is not an asserted
    exact chemical equivalent. Its separate literature bibliography was used only
    for bounded discovery, not treated as adopted claim-level evidence in this child.
  snapshot_sha256: b96f009e3f7b88a31799a37570a1c056c702d30af933865bad402fc7faf74874
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5 via batch 019 interpreter against batch 039 cwd
  locator: 388-chemistry.json and 388-stereo-parent.json
  accessed_at: '2026-10-21T15:00:10Z'
  support: supports
  summary: Native SMILES and InChI reproduce UQVNRKBFAXNOGA-LWTNMJDUSA-N, C16H20N2O4,
    neutral charge and masses. Zero-based SMILES atom 0 is C11a S and atom 19 is C11
    R; double bond 2–3 is E. The geometry-unspecified parent matches as a chiral substructure.
    The source mint is reproducible.
  snapshot_sha256: 2d7fa23782b743a66ec527bc1c04445d0cfa86a3262e4dae746856e2ad2e8b27
- evidence_id: adopted
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.36.276
  locator: PMID6833147; Introduction, Scheme 3, Biological Activity/Table 1, final
    1E/1Z preparation and interconversion sections
  accessed_at: '2026-10-21T14:58:10.975107Z'
  support: supports
  summary: The original synthesizes (11R,11aS)-E product 1E and Z product 1Z separately.
    The final E methyl ether has molecular ion 304 and C16H20N2O4 analysis. Scheme
    3 distinguishes these methoxy products from demethanolated imines 16E/16Z and
    shows solvent-dependent interconversion. Actual Scheme 3 and Table 1 were viewed.
    This directly supports the exact native structural form rather than a Z or imine
    substitution.
  snapshot_sha256: 17f58e670faabd03e4e2cdcfdec5c775b77189baa775e80aaed579c1a1739be4
- evidence_id: activity
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.36.276
  locator: Printed pages 278–279, Table 1 and complete disc-method paragraph
  accessed_at: '2026-10-21T14:58:10.975107Z'
  support: supports
  summary: Ten-millimetre paper discs were saturated with compound solutions and placed
    on seeded agar. At 1360 micrograms/mL, E product 1E gave zones of 20, 25, 11 and
    22 mm for S. aureus, B. subtilis, E. coli and P. vulgaris, respectively; P. aeruginosa
    was marked negative. These are solution concentrations and zone diameters, not
    MICs or mass per disc. The inspected method does not give strain accessions, incubation
    time/temperature or exact loading volume. Lower rows include plus signs whose
    quantitative meaning must not be invented.
  snapshot_sha256: 17f58e670faabd03e4e2cdcfdec5c775b77189baa775e80aaed579c1a1739be4
- evidence_id: structure-original
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.36.142
  locator: 'Printed pages 142–144: actual E/Z drawings, carbon-NMR geometry assignment
    and proton-coupling/model discussion'
  accessed_at: '2026-10-21T14:58:46.677223Z'
  support: supports
  summary: The preceding original assigns natural tomaymycin as (11R,11aS)-E using
    carbon-NMR steric-shift comparisons of prepared E/Z models and proton-coupling
    constraints at C11. It reports agreement with the earlier Arora crystal structure,
    which was not independently re-refined here. The actual first-page drawing matches
    the methoxy E form.
  snapshot_sha256: bbb2ce824cf2249732d7c784b468aa662d756fbcde4776f0c8a351f2cfa0284f
- evidence_id: isolation
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.25.437
  locator: PMID4648485; Introduction, fermentation, isolation, chemical characterization
    and antimicrobial Methods/Discussion
  accessed_at: '2026-10-21T14:58:46.679717Z'
  support: partial
  summary: The original isolated tomaymycin from strain A-2127, then identified as
    Streptomyces achromogenes var. tomaymyceticus. Methanol crystallization gave the
    C16H20N2O4 material; the paper distinguishes it from des-methanol product. Its
    older molecular-complex wording should not be converted into a disconnected methanol-solvate
    graph when the later primary chemistry explicitly establishes the covalent methyl
    ether. This historical isolation supports a bounded producer lead; no modern strain-taxonomy
    mapping is asserted.
  snapshot_sha256: 822ce156bf5fcd16d40f83e78f718db52d4711efc8f86138c4cf0f6056a245cb
- evidence_id: mode-lead
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.25.660
  locator: PMID4630600; original Materials/Methods, Results and Discussion text
  accessed_at: '2026-10-21T14:58:46.681491Z'
  support: partial
  summary: Natural-source tomaymycin was tested in B. subtilis 168/W23 and with E.
    coli DNA. Precursor incorporation, methyl-green displacement, gel filtration and
    thermal/nuclease protection support DNA complex formation and inhibition of nucleic-acid
    biosynthesis. The authors discuss intercalation and nuclease repair as hypotheses.
    This does not identify a bacterial protein target, establish a specific covalent
    atom linkage by itself or justify converting nuclease protection into direct nuclease
    inhibition. Exact in-assay methoxy/imine/C11-adduct state remains a mapping consideration
    for later enrichment.
  snapshot_sha256: b67bec3976391aa748caa9367aa6099cfafa262a6e80d970d0fcb27710cb8824
- evidence_id: discovery
  kind: search
  reference: Ignored-inclusive local search and Europe PMC original-source discovery
  locator: 388389-all-local-paths.txt;388-discovery.json
  accessed_at: '2026-10-21T14:57:52.432801Z'
  support: context_only
  summary: The bounded search included exact label, slug, CHEBI:167317 and its key
    across hidden and ignored local inputs/reports. Historical reports were discovery
    leads only. Primary discovery also found later C11-epimeric DNA-adduct studies;
    no derivative/antitumor assay was substituted for exact E antibacterial evidence.
  snapshot_sha256: 81538760dae1b1713c016500faa3d44fef165303ccf55f7648282916c9990d66
  search_scope: 2026-10-21; rg --no-ignore --hidden across data,curation,conf,scripts,src,reports,reviews;
    Europe PMC TITLE_ABS:tomaymycin; exact adopted PMID plus cited original structure/isolation/mechanism
    papers.
- evidence_id: gates
  kind: validation
  reference: Focused chemistry, schema and strict execution
  locator: 388-focused-results.json
  accessed_at: '2026-10-21T15:00:10Z'
  support: supports
  summary: All focused checks pass. Native validators ran in batch 039; standalone
    RDKit used the existing batch 019 interpreter against batch 039 cwd.
  snapshot_sha256: 4b9762bcc0630968cd31ce27b6ba89024d809e00d54b852c809bb9d0f424722e
assessments:
- assessment_id: identity
  area: identity
  topic: Exact E geometry and C11/C11a configuration
  outcome: supported
  summary: The native graph and single systematic synonym agree with current authority,
    primary NMR assignment and the separately synthesized E methyl ether. Z-tomaymycin
    and the demethanolated imine remain distinct.
  target_ids:
  - CHEBI:167317
  evidence_ids:
  - native
  - chebi
  - chemistry
  - adopted
  - structure-original
- assessment_id: grounding
  area: grounding
  topic: Authority, broader parent and source mint
  outcome: supported
  summary: The exact identifier and mint resolve; the parent deliberately leaves alkene
    geometry unspecified and is strictly broader. No external chemical xref requires
    adjudication.
  target_ids:
  - CHEBI:167317
  evidence_ids:
  - chebi
  - parent
  - chemistry
- assessment_id: classification
  area: scope
  topic: ANTIBACTERIAL filing and retained role
  outcome: supported
  summary: The original exact E product inhibits bacterial growth in a disc assay.
    The native antibacterial role and configured filing are supported; antitumor or
    phage activity is not used as a bacterial surrogate.
  target_ids:
  - CHEBI:167317
  evidence_ids:
  - activity
  - adopted
  - owners
- assessment_id: definition
  area: evidence
  topic: Definition and synonym support
  outcome: supported
  summary: The concise E-isomer definition and systematic (2E,11R,11aS) synonym are
    correct at the represented structural scope. The single adopted primary lead was
    read beyond its abstract.
  target_ids:
  - CHEBI:167317
  evidence_ids:
  - chebi
  - adopted
  - structure-original
- assessment_id: activity-completeness
  area: completeness
  topic: Optional activity_spectrum
  outcome: unknown
  summary: No native quantitative row is populated. The inspected original can support
    disc-zone observations if concentration and method limits are retained. Its solution
    concentrations must not be curated as MICs, and unreported strain identifiers
    or incubation details must remain unknown. Optional absence is not a required
    correction.
  target_ids:
  - CHEBI:167317
  evidence_ids:
  - native
  - activity
- assessment_id: mechanism-completeness
  area: completeness
  topic: Optional mode, molecular target, resistance and causal graph
  outcome: unknown
  summary: The record has no molecular claim. The original DNA-complex experiments
    offer a bounded mechanistic lead, but enrichment should reconcile exact chemical/adduct
    states and distinguish observations from the historical intercalation/nuclease
    hypotheses. No resistance allele or direct protein target was established here.
  target_ids:
  - CHEBI:167317
  evidence_ids:
  - native
  - mode-lead
  - adopted
- assessment_id: other
  area: scope
  topic: Producer, clinical and dataset domains
  outcome: not_applicable
  summary: No structured assertions occur. The historical producer lead is experimentally
    grounded at the stated strain identification, but no clinical approval, modern
    strain equivalence or dataset membership is inferred.
  target_ids:
  - CHEBI:167317
  evidence_ids:
  - native
  - isolation
- assessment_id: provenance
  area: provenance
  topic: Actual maintained owners and native history
  outcome: supported
  summary: The complete native record reproduces the exact adopted ChEBI row and three
    seed/reseed events. Original 13 hashes remain preserved within expanded context
    capture, with SEEDED status unchanged.
  target_ids:
  - CHEBI:167317
  evidence_ids:
  - native
  - owners
  - chemistry
- assessment_id: validation
  area: schema
  topic: Focused gates
  outcome: supported
  summary: Chemistry, schema and strict validation pass. These checks complement the
    source review and do not establish assay equivalence or mechanistic sign-off by
    themselves.
  target_ids:
  - CHEBI:167317
  evidence_ids:
  - gates
  - activity
  - mode-lead
findings: []
actions: []
limitations:
- The adopted 1983 paper was read at exact final-product synthesis, identity and complete
  antibacterial method/Table 1 scope, with actual Scheme 3/Table 1 and the preceding
  structure paper drawing viewed. Unrelated intermediate synthesis procedures and
  raw NMR spectra were not independently reprocessed.
- The disc assay lacks strain accessions, loading volume and incubation detail in
  the inspected method. Its concentrations and zones cannot be normalized into MICs.
- The 1972 isolation and mechanism originals were read at producer/material and experimental-mechanism
  scope. The earlier Arora crystal refinement and later C11 DNA-adduct experiments
  were not independently reanalyzed; exact reactive-state mapping remains a prerequisite
  for mechanistic enrichment.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native/source/status/history was edited. Optional links, tags and notes were
  checked against this exact E record.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:167317
- https://doi.org/10.7164/antibiotics.36.276
- https://doi.org/10.7164/antibiotics.36.142
tags:
- e-tomaymycin
- stereochemistry
- disc-diffusion
```
