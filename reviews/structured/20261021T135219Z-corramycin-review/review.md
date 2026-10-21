# Corramycin: exact stereochemical identity with a paraphrase misplaced as a quotation

- Review: 20261021T135219Z-corramycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T13:38:59Z
- Finished UTC: 2026-10-21T13:52:19Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native linear peptide agrees with current RCSB and PubChem and the original absolute-configuration study. One minor evidence-placement correction is needed: a curator summary is stored in the verbatim snippet field. Antibacterial activity is supported; transport dependence should remain distinct from an experimentally established lethal target.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position328; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:curator-452d38df8e | data/antibiotics/antibacterial/corramycin.yaml | generated | Corramycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:curator-452d38df8e | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:curator-452d38df8e | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:curator-452d38df8e | Actual focused execution exited 0. |
| Current authoritative graph comparison | passed | False | antibioticmech:curator-452d38df8e | Current authority graphs and native SMILES generate the stored native Standard InChIKey. Exit 0; round-trip diagnostics are retained separately. |
| Authoritative full QC | failed | True | antibioticmech:curator-452d38df8e | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:curator-452d38df8e | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:curator-452d38df8e | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:curator-452d38df8e | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:curator-452d38df8e | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:curator-452d38df8e | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:curator-452d38df8e | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:curator-452d38df8e | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:curator-452d38df8e | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### One fully assigned peptide identity and exact xref

identity: supported. Targets: antibioticmech:curator-452d38df8e.

Native SMILES/InChI, both RCSB stereo descriptors and PubChem agree on constitution, charge and all 13 assigned centres. Original Figure 3 supports the unusual stereochemical units, including the N-terminal and histidine R/S assignments and the valerate S/R/S sequence. No mixture or inversion is supported.

### Linear-peptide definition and antibacterial role

evidence: supported. Targets: antibioticmech:curator-452d38df8e.

The concise native definition and CHEBI:33282 role are supported at experimental scope. Myxobacterial isolation is supported; no unasserted clinical indication or universal host safety is inferred.

### Verbatim snippet versus curator summary

provenance: concern. Targets: antibioticmech:curator-452d38df8e.

The source-owned evidence_snippet uses an accurate paraphrase in a field reserved for a verbatim quotation. Move the narrative into notes or substitute a short verified quotation; retain the source reference.

### Optional mechanism, transport and activity enrichment

evidence: unknown. Targets: antibioticmech:curator-452d38df8e.

Uptake-system experiments are available for optional evidence curation. They should not be emitted as direct lethal-target binding, and the 2022 study does not establish the target. No mechanism, measured MIC, resistance, producer or clinical-status field is currently asserted.

### Curator source, exact mint and reproducibility

provenance: supported. Targets: antibioticmech:curator-452d38df8e.

The DOI-qualified curator source, structure source/retrieval date, source version and single PROPOSED history event reconcile. PROPOSED/MINTED accurately retains a curator identity; matching an external database alone does not authorize promotion.

## Findings

### F1: A curator paraphrase occupies the verbatim evidence field

minor / open / confirmed; issue key: corramycin-paraphrase-in-verbatim-snippet.

The stored sentence summarizes Couturier et al. in the third person and is not a quotation from the cited complete article. Its factual substance is supported. Correct evidence_snippet at the maintained curator row by moving the paraphrase to notes or replacing it with a short verified quotation.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained evidence field and regenerate the record reproducibly.

- Place curator narrative in evidence_notes, or use a short passage verified verbatim against the original article in evidence_snippet. Preserve the DOI reference and exact compound scope.
- Regenerate via the validated curator-inventory workflow and check source-to-record reproduction, evidence field semantics and focused validation. Do not change the supported structure or status as a side effect.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/corramycin.yaml; entire record | supports | Read every native field, all aliases, parent/role identifiers, exact encodings, xrefs, source concepts and history. Initial target and context hashes remain unchanged. |
| owners | curation/curator_antibiotics.tsv; line 10; exact source row and generation owners | supports | Read the complete adopted row and traced its fields through the maintained extraction/seeding and decision context. Gitignored and hidden files were included in local identity/owner searches. |
| chemistry | RDKit 2026.03.5 / InChI 1.07.3; native encoding calculation; current authority graph comparison | supports | Independent formula, charge, mass, stereochemistry and Standard InChIKey calculations were compared with native and accessible current authoritative encodings. See the explicit identity assessment and diagnostic limitations. |
| rcsb | https://www.rcsb.org/ligand/PRD_002426; complete BIRD record, PRDCC descriptors and current ligand identity page | supports | Both independent current RCSB stereochemical SMILES descriptors regenerate native WVMKFROBDLCDEJ-LINZXDLISA-N: C51H81N11O21, charge zero and 13 assigned tetrahedral centres. The BIRD record describes ten linked monomers, including two nonstandard non-alpha-amino-acid units; the eight alpha-amino-acid statement is not a sequence-length contradiction. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/138485664; current PUG REST identity properties | supports | The sole native xref independently matches full native InChI and stereochemical SMILES. Calculated average/exact masses are 1184.265/1183.560848612; their optional omission natively is not an error. |
| primary | https://doi.org/10.1002/anie.202210747; PMID:36197755 / PMC10099666; complete main text; Figure 3 and Tables 1/2 visually inspected | supports | Couturier and colleagues isolated Corramycin from C. coralloides ST201330 and established the absolute configuration through chiral analyses and synthetic diastereomer comparison. The original assays support anti-Gram-negative activity. Transporter deletion and complementation implicate SbmA/YejABEF in uptake; medium matters. These experiments do not by themselves identify the lethal target. |
| supplement | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10099666/supplementaryFiles; ANIE-61-0-s001.pdf; contents and PDF pages 6,19–21,33,63–64,103–104,106 | supports | Inspected isolation, stereochemical work, selected susceptibility methods, synthetic purification and genetic/complementation procedures. Natural isolation and synthetic TFA-containing purification are different preparation histories; neither fixes a universally applicable bulk counterion. Optional numerical activities require preparation- and method-specific extraction. |
| snippet-rule | src/antibioticmech/schema/antibioticmech.yaml; snippet slot near line 1627; native evidence and source evidence_snippet | supports | The schema defines snippet as a verbatim source quotation. The stored sentence beginning Couturier et al. established is a curator narrative summary, not a passage in the complete fetched original article; normalized whole-article text comparison returned false. Its substance is supported, but its field semantics are wrong. |
| adapter | https://imodulondb.org/; structured adapter e_coli/precise1k; sbmA and yejA searches | supports | Both searches returned their corresponding gene annotations, b0377 and b2177, and zero matching iModulons. These bounded dataset results are not evidence of absent biology or direct Corramycin targets. |

## Limits And Additional Notes

- Focused record checks do not substitute for required corpus gates or authorize a REVIEWED status change.
- The complete original main text was read, with Figure 3 and Tables 1/2 inspected visually. Only the explicitly listed supplementary sections were read; the 108-page supplement and raw spectra were not exhaustively reinterpreted.
- No original crystallographic/ribosome study associated with representative PDB 8AGY was audited; its presence in BIRD is not used here to assert a target.
- The original study contains medium-specific transport effects and differing numerical presentation between selected main and supplementary measurements. No single universal MIC or frequency-of-resistance value is imported.
- TFA-containing synthetic isolation does not demonstrate a specified stoichiometric salt for the native parent. Natural and synthetic lots must retain separate assay provenance.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Review only: no native record, inventory, decision, schema, dependency or generator changes. Optional absent fields do not independently establish an error. These scientific findings do not imply permission for curation.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T135219Z-corramycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Corramycin: exact stereochemical identity with a paraphrase misplaced as a
  quotation'
started_at: '2026-10-21T13:38:59Z'
finished_at: '2026-10-21T13:52:19Z'
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
summary: 'The native linear peptide agrees with current RCSB and PubChem and the original
  absolute-configuration study. One minor evidence-placement correction is needed:
  a curator summary is stored in the verbatim snippet field. Antibacterial activity
  is supported; transport dependence should remain distinct from an experimentally
  established lethal target.'
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
  - path: data/antibiotics/antibacterial/corramycin.yaml
    sha256: 59c5b39c3791493baad3f146a923c7ef4336d1d987143b64d64c7d07d0c1864d
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
- target_id: antibioticmech:curator-452d38df8e
  path: data/antibiotics/antibacterial/corramycin.yaml
  label: Corramycin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Maintained exact curator structure and evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator inventory validated generation
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Identity and exclusion decisions
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position328; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:curator-452d38df8e
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-452d38df8e
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus033-root.py
    328
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-452d38df8e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/corramycin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-452d38df8e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/corramycin.yaml --out /private/tmp/am-review-session/328-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-forward-chemistry
  name: Current authoritative graph comparison
  status: passed
  required: false
  summary: Current authority graphs and native SMILES generate the stored native Standard
    InChIKey. Exit 0; round-trip diagnostics are retained separately.
  target_ids:
  - antibioticmech:curator-452d38df8e
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
  - antibioticmech:curator-452d38df8e
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
  - antibioticmech:curator-452d38df8e
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
  - antibioticmech:curator-452d38df8e
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
  - antibioticmech:curator-452d38df8e
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
  - antibioticmech:curator-452d38df8e
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
  - antibioticmech:curator-452d38df8e
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
  - antibioticmech:curator-452d38df8e
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
  - antibioticmech:curator-452d38df8e
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
  - antibioticmech:curator-452d38df8e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/corramycin.yaml
  locator: entire record
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: Read every native field, all aliases, parent/role identifiers, exact encodings,
    xrefs, source concepts and history. Initial target and context hashes remain unchanged.
- evidence_id: owners
  kind: record_content
  reference: curation/curator_antibiotics.tsv
  locator: line 10; exact source row and generation owners
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: Read the complete adopted row and traced its fields through the maintained
    extraction/seeding and decision context. Gitignored and hidden files were included
    in local identity/owner searches.
  snapshot_sha256: dac9e92c7abb88c0247b3b06e6587d945e601f6e05a9e7456b0b5306b2e95e58
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5 / InChI 1.07.3
  locator: native encoding calculation; current authority graph comparison
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: Independent formula, charge, mass, stereochemistry and Standard InChIKey
    calculations were compared with native and accessible current authoritative encodings.
    See the explicit identity assessment and diagnostic limitations.
  snapshot_sha256: d1155fd1a0fc390f5b97fe4f3b117f6c5051c75597f980ec4c2323066f7904c8
- evidence_id: rcsb
  kind: authority
  reference: https://www.rcsb.org/ligand/PRD_002426
  locator: complete BIRD record, PRDCC descriptors and current ligand identity page
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: 'Both independent current RCSB stereochemical SMILES descriptors regenerate
    native WVMKFROBDLCDEJ-LINZXDLISA-N: C51H81N11O21, charge zero and 13 assigned
    tetrahedral centres. The BIRD record describes ten linked monomers, including
    two nonstandard non-alpha-amino-acid units; the eight alpha-amino-acid statement
    is not a sequence-length contradiction.'
  snapshot_sha256: 6c659a21db14f6b93cdcb0786ba4deffb5d2d1409e9f9aa6e4301604245b8d05
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/138485664
  locator: current PUG REST identity properties
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: The sole native xref independently matches full native InChI and stereochemical
    SMILES. Calculated average/exact masses are 1184.265/1183.560848612; their optional
    omission natively is not an error.
  snapshot_sha256: c2938220a9eb604cb3a276fb4aa87560ae62d955bfdc986bd181bcd150763350
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1002/anie.202210747
  locator: PMID:36197755 / PMC10099666; complete main text; Figure 3 and Tables 1/2
    visually inspected
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: Couturier and colleagues isolated Corramycin from C. coralloides ST201330
    and established the absolute configuration through chiral analyses and synthetic
    diastereomer comparison. The original assays support anti-Gram-negative activity.
    Transporter deletion and complementation implicate SbmA/YejABEF in uptake; medium
    matters. These experiments do not by themselves identify the lethal target.
  snapshot_sha256: a086a381bc99248be5e68e050019c2634e95210dcfb9b323eb8244f8943a02c5
- evidence_id: supplement
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10099666/supplementaryFiles
  locator: ANIE-61-0-s001.pdf; contents and PDF pages 6,19–21,33,63–64,103–104,106
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: Inspected isolation, stereochemical work, selected susceptibility methods,
    synthetic purification and genetic/complementation procedures. Natural isolation
    and synthetic TFA-containing purification are different preparation histories;
    neither fixes a universally applicable bulk counterion. Optional numerical activities
    require preparation- and method-specific extraction.
  snapshot_sha256: c84c17e62480dcb0b644795d8afd9464c4b1a25b1d8b1aeaeede46535bc0e866
- evidence_id: snippet-rule
  kind: record_content
  reference: src/antibioticmech/schema/antibioticmech.yaml
  locator: snippet slot near line 1627; native evidence and source evidence_snippet
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: The schema defines snippet as a verbatim source quotation. The stored sentence
    beginning Couturier et al. established is a curator narrative summary, not a passage
    in the complete fetched original article; normalized whole-article text comparison
    returned false. Its substance is supported, but its field semantics are wrong.
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/
  locator: structured adapter e_coli/precise1k; sbmA and yejA searches
  accessed_at: '2026-10-21T13:50:59Z'
  support: supports
  summary: Both searches returned their corresponding gene annotations, b0377 and
    b2177, and zero matching iModulons. These bounded dataset results are not evidence
    of absent biology or direct Corramycin targets.
  snapshot_sha256: ac32015ed98e12513783a2bef8faf9d764683f9c7c132478b481780dee12ae60
assessments:
- assessment_id: identity
  area: identity
  topic: One fully assigned peptide identity and exact xref
  outcome: supported
  summary: Native SMILES/InChI, both RCSB stereo descriptors and PubChem agree on
    constitution, charge and all 13 assigned centres. Original Figure 3 supports the
    unusual stereochemical units, including the N-terminal and histidine R/S assignments
    and the valerate S/R/S sequence. No mixture or inversion is supported.
  target_ids:
  - antibioticmech:curator-452d38df8e
  evidence_ids:
  - chemistry
  - rcsb
  - pubchem
  - primary
- assessment_id: definition
  area: evidence
  topic: Linear-peptide definition and antibacterial role
  outcome: supported
  summary: The concise native definition and CHEBI:33282 role are supported at experimental
    scope. Myxobacterial isolation is supported; no unasserted clinical indication
    or universal host safety is inferred.
  target_ids:
  - antibioticmech:curator-452d38df8e
  evidence_ids:
  - native
  - primary
  - supplement
- assessment_id: evidence-placement
  area: provenance
  topic: Verbatim snippet versus curator summary
  outcome: concern
  summary: The source-owned evidence_snippet uses an accurate paraphrase in a field
    reserved for a verbatim quotation. Move the narrative into notes or substitute
    a short verified quotation; retain the source reference.
  target_ids:
  - antibioticmech:curator-452d38df8e
  evidence_ids:
  - native
  - owners
  - primary
  - snippet-rule
- assessment_id: mechanism
  area: evidence
  topic: Optional mechanism, transport and activity enrichment
  outcome: unknown
  summary: Uptake-system experiments are available for optional evidence curation.
    They should not be emitted as direct lethal-target binding, and the 2022 study
    does not establish the target. No mechanism, measured MIC, resistance, producer
    or clinical-status field is currently asserted.
  target_ids:
  - antibioticmech:curator-452d38df8e
  evidence_ids:
  - native
  - primary
  - supplement
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Curator source, exact mint and reproducibility
  outcome: supported
  summary: The DOI-qualified curator source, structure source/retrieval date, source
    version and single PROPOSED history event reconcile. PROPOSED/MINTED accurately
    retains a curator identity; matching an external database alone does not authorize
    promotion.
  target_ids:
  - antibioticmech:curator-452d38df8e
  evidence_ids:
  - owners
  - native
  - chemistry
  - rcsb
findings:
- finding_id: F1
  issue_key: corramycin-paraphrase-in-verbatim-snippet
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: A curator paraphrase occupies the verbatim evidence field
  description: The stored sentence summarizes Couturier et al. in the third person
    and is not a quotation from the cited complete article. Its factual substance
    is supported. Correct evidence_snippet at the maintained curator row by moving
    the paraphrase to notes or replacing it with a short verified quotation.
  target_ids:
  - antibioticmech:curator-452d38df8e
  field_paths:
  - source_concepts[0].evidence[0].snippet
  evidence_ids:
  - native
  - owners
  - primary
  - snippet-rule
  rule_id: 'EvidenceItem.snippet: Verbatim quote from source'
  native_severity: minor evidence representation
  normalization_reason: The claim and identity remain supported; this changes quotation
    provenance rather than the scientific conclusion.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Maintained evidence_snippet and evidence_notes for exact Corramycin row
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Validated curator-inventory evidence generation
actions:
- action_id: A1
  description: Correct the maintained evidence field and regenerate the record reproducibly.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:curator-452d38df8e
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Maintained evidence_snippet and evidence_notes for exact Corramycin row
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Validated curator-inventory evidence generation
  acceptance_checks:
  - Place curator narrative in evidence_notes, or use a short passage verified verbatim
    against the original article in evidence_snippet. Preserve the DOI reference and
    exact compound scope.
  - Regenerate via the validated curator-inventory workflow and check source-to-record
    reproduction, evidence field semantics and focused validation. Do not change the
    supported structure or status as a side effect.
limitations:
- Focused record checks do not substitute for required corpus gates or authorize a
  REVIEWED status change.
- The complete original main text was read, with Figure 3 and Tables 1/2 inspected
  visually. Only the explicitly listed supplementary sections were read; the 108-page
  supplement and raw spectra were not exhaustively reinterpreted.
- No original crystallographic/ribosome study associated with representative PDB 8AGY
  was audited; its presence in BIRD is not used here to assert a target.
- The original study contains medium-specific transport effects and differing numerical
  presentation between selected main and supplementary measurements. No single universal
  MIC or frequency-of-resistance value is imported.
- TFA-containing synthetic isolation does not demonstrate a specified stoichiometric
  salt for the native parent. Natural and synthetic lots must retain separate assay
  provenance.
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
