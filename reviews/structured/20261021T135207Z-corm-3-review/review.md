# CORM 3: coherent coordination parent with condition-dependent solution chemistry

- Review: 20261021T135207Z-corm-3-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T13:38:58Z
- Finished UTC: 2026-10-21T13:52:07Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No corrective native-record finding was established. The neutral ruthenium carbonyl parent and its antibacterial classification are supported. Its broad carbon-monoxide-releasing definition must not be read as an exclusive antibacterial mechanism; aqueous speciation, ligands and assay medium affect the experimentally active material. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position327; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:137081 | data/antibiotics/antibacterial/corm-3.yaml | generated | CORM 3 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:137081 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:137081 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:137081 | Actual focused execution exited 0. |
| Current authoritative graph comparison | passed | False | CHEBI:137081 | Current authority graphs and native SMILES generate the stored native Standard InChIKey. Exit 0; round-trip diagnostics are retained separately. |
| Authoritative full QC | failed | True | CHEBI:137081 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:137081 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:137081 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:137081 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:137081 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:137081 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:137081 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:137081 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:137081 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact coordination parent and representation

identity: supported. Targets: CHEBI:137081.

The native graph is one net-neutral coordination entity. Standard InChI metal disconnection produces six components while retaining the same composition and key; this is not evidence of a six-component preparation. Formal atom charges in the chosen graph are not the ruthenium oxidation state. No absolute coordination geometry is independently asserted.

### Definition, synonyms and chemical classes

evidence: supported. Targets: CHEBI:137081.

The names and metal-carbonyl/ruthenium parents describe the source-defined compound. Carbon-monoxide-releasing is a conditional chemical descriptor; the native definition does not say CO alone explains bacterial killing. The inspected primary evidence does not justify deleting that descriptor.

### Antibacterial eligibility and material scope

evidence: supported. Targets: CHEBI:137081.

Exact named CORM-3 preparations have original bacterial activity evidence. Parent identity and activity of its changing aqueous preparations must remain distinct; assay values cannot be treated as universal across media.

### Optional target, pathway and resistance fields

evidence: unknown. Targets: CHEBI:137081.

No direct bacterial protein, complete causal chain or resistance determinant is asserted natively. Structured context and host studies do not fill this gap. The class-scoped omission of a mitochondrial mechanism is intentional and scientifically appropriate.

### All adopted sources and maintained ownership

provenance: supported. Targets: CHEBI:137081.

The exact source mint, version and three history events reconcile. All ten adopted citation leads were read at abstract depth; the additional 2018 original was read in full main-text scope. Reaxys remains independently unresolved.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally curate bounded primary bacterial activity and mechanism evidence.

- Preserve preparation, time after dissolution, medium, strain and endpoint; distinguish parent, ligand-exchanged material and inactivated control.
- Keep CFU killing, inhibition, CO release, ruthenium accumulation and model-peptide interactions separate. Do not assert an exclusive protein target, intact-parent uptake, or CO-only/no-CO mechanism without exact supporting experiments.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/corm-3.yaml; entire record | supports | Read every native field, all aliases, parent/role identifiers, exact encodings, xrefs, source concepts and history. Initial target and context hashes remain unchanged. |
| owners | data/raw/chebi_antimicrobials.tsv; line 2577; exact source row and generation owners | supports | Read the complete adopted row and traced its fields through the maintained extraction/seeding and decision context. Gitignored and hidden files were included in local identity/owner searches. |
| chemistry | RDKit 2026.03.5 / InChI 1.07.3; native encoding calculation; current authority graph comparison | supports | Independent formula, charge, mass, stereochemistry and Standard InChIKey calculations were compared with native and accessible current authoritative encodings. See the explicit identity assessment and diagnostic limitations. |
| authority | https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:137081; complete current entry and official molfile; names, parents and roles | supports | Current ChEBI repeats the four aliases and neutral C5H4ClNO5Ru parent. Both current molfile and SMILES independently yield KNIGBBVETQCJTQ-UHFFFAOYSA-L, average mass 294.612 and exact mass 294.882149208. The two native parents are ruthenium coordination entity and metal carbonyl. Its Reaxys accession is source-attested. |
| primary2018 | https://doi.org/10.1016/j.redox.2018.06.008; PMID:30007887 / PMC6067063; complete main text, Figure 1 visually inspected, full supplementary DOCX text/captions | supports | The original study used freshly prepared CORM-3 synthesized from CORM-2. E. coli assays distinguish medium-dependent inhibition and CFU viability. Aqueous ligand exchange, thiol interactions and cellular ruthenium accumulation support a conditional ruthenium-mediated contribution; the analysis does not identify one exclusive bacterial protein target. Dithionite-dependent CO release and potential low-level haem effects limit an absolute no-CO conclusion. Cellular ruthenium does not prove uptake of intact parent. |
| supplement | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6067063/supplementaryFiles; mmc1.docx; all extracted text and captions | supports | Supplementary methods, synthetic peptide interaction descriptions and spectral captions were read. Spectral image panels were not independently reprocessed; model peptide binding is not an identified bacterial target. |
| microbial-leads | https://pubmed.ncbi.nlm.nih.gov/23186316/; PMID:23186316 and PMID:23472713; complete indexed abstracts | supports | Two adopted original microbiology abstracts concern respiratory inhibition/photoreversal and CORM-3 versus inactivated preparation transcriptomics. Full main articles were not recovered; no detailed dose, target or exclusive CO mechanism is imported from these abstracts. |
| host-leads | https://pubmed.ncbi.nlm.nih.gov/21376373/; complete indexed abstracts of PMID:21376373, 21382478, 21926571, 22038495, 22210380, 22644323, 22766583, 23296254 | supports | All eight remaining adopted leads were individually read: thrombosis, cardiac mitochondria, haemorrhagic stroke, myocardial infarction, endothelial-cell signalling, arthritis, aortic relaxation and eNOS. These host models do not establish antibacterial molecular targets or justify transferring mammalian mitochondrial mechanisms into bacterial annotations. |
| mapping | conf/sources.yaml; lines 375–395; CHEBI:25355 class-scoped mapping | supports | The mitochondrial respiratory-chain inhibitor mapping deliberately applies to eukaryotic antimicrobial classes and excludes ANTIBACTERIAL. The adopted CHEBI:25355 mechanism-role lead therefore does not require a bacterial mechanism entry. |
| adapter | https://imodulondb.org/; live structured adapter; e_coli/precise1k respiration search and full component 91 member summary | supports | Catalog and search succeeded before detailed primary mechanism assessment. The NDH-1 component has 12 member genes at threshold 0.0833288. This is general respiration context, not a CORM-3 exposure experiment or direct-target assay; no regulator or component membership is transferred into the record. |

## Limits And Additional Notes

- Focused record checks do not substitute for required corpus gates or authorize a REVIEWED status change.
- Reaxys 24025482 was not independently inspected. Current ChEBI and its molfile confirm the adopted identity but do not independently prove a particular coordination stereoisomer or the composition of every solution species.
- Original 2013 microbial full texts could not be recovered through the attempted XML and public HTML routes; complete indexed abstracts were read. Host papers were evaluated at abstract scope only.
- The 2018 main article, Figure 1 and complete supplementary text/captions were inspected. Other figure images, raw spectra and the cited original synthetic report were not independently reanalysed. No clinical efficacy or host-selectivity claim is inferred.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Review only: no native record, inventory, decision, schema, dependency or generator changes. Optional absent fields do not independently establish an error. These scientific findings do not imply permission for curation.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T135207Z-corm-3-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'CORM 3: coherent coordination parent with condition-dependent solution chemistry'
started_at: '2026-10-21T13:38:58Z'
finished_at: '2026-10-21T13:52:07Z'
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
summary: No corrective native-record finding was established. The neutral ruthenium
  carbonyl parent and its antibacterial classification are supported. Its broad carbon-monoxide-releasing
  definition must not be read as an exclusive antibacterial mechanism; aqueous speciation,
  ligands and assay medium affect the experimentally active material. Scientific assessment
  retains the stated evidence limits; full verification is blocked by the shared native-library
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
  - path: data/antibiotics/antibacterial/corm-3.yaml
    sha256: afd223d96e67b40683dcfd172dd9edc57145523b9ba238eaded435c34b876391
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
- target_id: CHEBI:137081
  path: data/antibiotics/antibacterial/corm-3.yaml
  label: CORM 3
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
  selection: Initially uncovered queue position327; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:137081
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:137081
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus033-root.py
    327
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:137081
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/corm-3.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:137081
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/corm-3.yaml --out /private/tmp/am-review-session/327-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-forward-chemistry
  name: Current authoritative graph comparison
  status: passed
  required: false
  summary: Current authority graphs and native SMILES generate the stored native Standard
    InChIKey. Exit 0; round-trip diagnostics are retained separately.
  target_ids:
  - CHEBI:137081
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/033-authority-chemistry.py
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
  - CHEBI:137081
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
  - CHEBI:137081
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
  - CHEBI:137081
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
  - CHEBI:137081
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
  - CHEBI:137081
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
  - CHEBI:137081
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
  - CHEBI:137081
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
  - CHEBI:137081
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
  - CHEBI:137081
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/corm-3.yaml
  locator: entire record
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: Read every native field, all aliases, parent/role identifiers, exact encodings,
    xrefs, source concepts and history. Initial target and context hashes remain unchanged.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: line 2577; exact source row and generation owners
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: Read the complete adopted row and traced its fields through the maintained
    extraction/seeding and decision context. Gitignored and hidden files were included
    in local identity/owner searches.
  snapshot_sha256: 06d650e5987d07afd25729a0ae07689462b07267b7b45b92a46ac145bbeb0242
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5 / InChI 1.07.3
  locator: native encoding calculation; current authority graph comparison
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: Independent formula, charge, mass, stereochemistry and Standard InChIKey
    calculations were compared with native and accessible current authoritative encodings.
    See the explicit identity assessment and diagnostic limitations.
  snapshot_sha256: 6fbc3cc3ed15225c0035bc7f081480e7e9233937eecfb9332d639cbc46e5b8ea
- evidence_id: authority
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:137081
  locator: complete current entry and official molfile; names, parents and roles
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: Current ChEBI repeats the four aliases and neutral C5H4ClNO5Ru parent.
    Both current molfile and SMILES independently yield KNIGBBVETQCJTQ-UHFFFAOYSA-L,
    average mass 294.612 and exact mass 294.882149208. The two native parents are
    ruthenium coordination entity and metal carbonyl. Its Reaxys accession is source-attested.
  snapshot_sha256: 447d422cdd34bbd500cdb6a338a76241958f5636ef66b7cfa22acaab1593a94a
- evidence_id: primary2018
  kind: primary_source
  reference: https://doi.org/10.1016/j.redox.2018.06.008
  locator: PMID:30007887 / PMC6067063; complete main text, Figure 1 visually inspected,
    full supplementary DOCX text/captions
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: The original study used freshly prepared CORM-3 synthesized from CORM-2.
    E. coli assays distinguish medium-dependent inhibition and CFU viability. Aqueous
    ligand exchange, thiol interactions and cellular ruthenium accumulation support
    a conditional ruthenium-mediated contribution; the analysis does not identify
    one exclusive bacterial protein target. Dithionite-dependent CO release and potential
    low-level haem effects limit an absolute no-CO conclusion. Cellular ruthenium
    does not prove uptake of intact parent.
  snapshot_sha256: 29c7c153fe34891e259542084ca8d5012fcd3986f2eb6afd6697bf039b67ea0c
- evidence_id: supplement
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6067063/supplementaryFiles
  locator: mmc1.docx; all extracted text and captions
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: Supplementary methods, synthetic peptide interaction descriptions and spectral
    captions were read. Spectral image panels were not independently reprocessed;
    model peptide binding is not an identified bacterial target.
  snapshot_sha256: dda81d60b0059af5dca0c2a85af7117b44e7afea8ed743e9b97b9c00aa512a52
- evidence_id: microbial-leads
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/23186316/
  locator: PMID:23186316 and PMID:23472713; complete indexed abstracts
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: Two adopted original microbiology abstracts concern respiratory inhibition/photoreversal
    and CORM-3 versus inactivated preparation transcriptomics. Full main articles
    were not recovered; no detailed dose, target or exclusive CO mechanism is imported
    from these abstracts.
  snapshot_sha256: 62006360f6fe182eab204d4fce72f7bdb42e75d07d033d9114976979712749e6
- evidence_id: host-leads
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/21376373/
  locator: complete indexed abstracts of PMID:21376373, 21382478, 21926571, 22038495,
    22210380, 22644323, 22766583, 23296254
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: 'All eight remaining adopted leads were individually read: thrombosis,
    cardiac mitochondria, haemorrhagic stroke, myocardial infarction, endothelial-cell
    signalling, arthritis, aortic relaxation and eNOS. These host models do not establish
    antibacterial molecular targets or justify transferring mammalian mitochondrial
    mechanisms into bacterial annotations.'
  snapshot_sha256: 62006360f6fe182eab204d4fce72f7bdb42e75d07d033d9114976979712749e6
- evidence_id: mapping
  kind: record_content
  reference: conf/sources.yaml
  locator: lines 375–395; CHEBI:25355 class-scoped mapping
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: The mitochondrial respiratory-chain inhibitor mapping deliberately applies
    to eukaryotic antimicrobial classes and excludes ANTIBACTERIAL. The adopted CHEBI:25355
    mechanism-role lead therefore does not require a bacterial mechanism entry.
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/
  locator: live structured adapter; e_coli/precise1k respiration search and full component
    91 member summary
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: Catalog and search succeeded before detailed primary mechanism assessment.
    The NDH-1 component has 12 member genes at threshold 0.0833288. This is general
    respiration context, not a CORM-3 exposure experiment or direct-target assay;
    no regulator or component membership is transferred into the record.
  snapshot_sha256: ac32015ed98e12513783a2bef8faf9d764683f9c7c132478b481780dee12ae60
assessments:
- assessment_id: identity
  area: identity
  topic: Exact coordination parent and representation
  outcome: supported
  summary: The native graph is one net-neutral coordination entity. Standard InChI
    metal disconnection produces six components while retaining the same composition
    and key; this is not evidence of a six-component preparation. Formal atom charges
    in the chosen graph are not the ruthenium oxidation state. No absolute coordination
    geometry is independently asserted.
  target_ids:
  - CHEBI:137081
  evidence_ids:
  - native
  - chemistry
  - authority
- assessment_id: definition
  area: evidence
  topic: Definition, synonyms and chemical classes
  outcome: supported
  summary: The names and metal-carbonyl/ruthenium parents describe the source-defined
    compound. Carbon-monoxide-releasing is a conditional chemical descriptor; the
    native definition does not say CO alone explains bacterial killing. The inspected
    primary evidence does not justify deleting that descriptor.
  target_ids:
  - CHEBI:137081
  evidence_ids:
  - native
  - authority
  - primary2018
- assessment_id: activity
  area: evidence
  topic: Antibacterial eligibility and material scope
  outcome: supported
  summary: Exact named CORM-3 preparations have original bacterial activity evidence.
    Parent identity and activity of its changing aqueous preparations must remain
    distinct; assay values cannot be treated as universal across media.
  target_ids:
  - CHEBI:137081
  evidence_ids:
  - primary2018
  - microbial-leads
- assessment_id: mechanism
  area: evidence
  topic: Optional target, pathway and resistance fields
  outcome: unknown
  summary: No direct bacterial protein, complete causal chain or resistance determinant
    is asserted natively. Structured context and host studies do not fill this gap.
    The class-scoped omission of a mitochondrial mechanism is intentional and scientifically
    appropriate.
  target_ids:
  - CHEBI:137081
  evidence_ids:
  - mapping
  - adapter
  - host-leads
  - primary2018
- assessment_id: provenance
  area: provenance
  topic: All adopted sources and maintained ownership
  outcome: supported
  summary: The exact source mint, version and three history events reconcile. All
    ten adopted citation leads were read at abstract depth; the additional 2018 original
    was read in full main-text scope. Reaxys remains independently unresolved.
  target_ids:
  - CHEBI:137081
  evidence_ids:
  - owners
  - native
  - microbial-leads
  - host-leads
  - authority
findings: []
actions:
- action_id: A1
  description: Optionally curate bounded primary bacterial activity and mechanism
    evidence.
  finding_ids: []
  target_ids:
  - CHEBI:137081
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/corm-3.yaml
    role: Curator-owned claim evidence and activity/mechanism additions
  acceptance_checks:
  - Preserve preparation, time after dissolution, medium, strain and endpoint; distinguish
    parent, ligand-exchanged material and inactivated control.
  - Keep CFU killing, inhibition, CO release, ruthenium accumulation and model-peptide
    interactions separate. Do not assert an exclusive protein target, intact-parent
    uptake, or CO-only/no-CO mechanism without exact supporting experiments.
limitations:
- Focused record checks do not substitute for required corpus gates or authorize a
  REVIEWED status change.
- Reaxys 24025482 was not independently inspected. Current ChEBI and its molfile confirm
  the adopted identity but do not independently prove a particular coordination stereoisomer
  or the composition of every solution species.
- Original 2013 microbial full texts could not be recovered through the attempted
  XML and public HTML routes; complete indexed abstracts were read. Host papers were
  evaluated at abstract scope only.
- The 2018 main article, Figure 1 and complete supplementary text/captions were inspected.
  Other figure images, raw spectra and the cited original synthetic report were not
  independently reanalysed. No clinical efficacy or host-selectivity claim is inferred.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- 'Review only: no native record, inventory, decision, schema, dependency or generator
  changes. Optional absent fields do not independently establish an error. These scientific
  findings do not imply permission for curation.'
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
