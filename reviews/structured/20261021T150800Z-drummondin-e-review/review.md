# Drummondin E: coherent tautomeric identity with unresolved stereochemistry

- Review: 20261021T150800Z-drummondin-e-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:43:56Z
- Finished UTC: 2026-10-21T15:08:00Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The neutral drummondin E graph is internally coherent and matches current chemical authorities after explicitly accounting for keto–enol tautomerism. The sole adopted original abstract supports plant isolation and activity against the three named bacterial species. One stereocentre and primary assay details remain unresolved; no confirmed native correction is established. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position380; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65810 | data/antibiotics/antibacterial/drummondin-e.yaml | generated | drummondin E |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:65810 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:65810 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:65810 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:65810 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65810 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65810 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65810 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65810 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65810 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65810 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65810 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65810 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral connectivity and tautomeric authority comparison

identity: supported. Targets: CHEBI:65810.

All native fields are coherent. Explicit chemical comparison reconciles current PubChem tautomerism rather than treating differing full keys as automatically different compounds.

### One unassigned centre and positive-rotation name

identity: unknown. Targets: CHEBI:65810.

Native and inspected independent encodings omit the same stereocentre. The (+) alias is consistently source-attested, but the unavailable original characterization prevents independent confirmation of its measured rotation or an absolute assignment. Neither a wrong epimer nor a racemate is demonstrated.

### Broader structural classes and exact CAS

grounding: supported. Targets: CHEBI:65810.

Parent classes fit the graph, and exact CAS/name provenance is corroborated. No salt, hydrate, mixture or unrelated positional isomer is substituted.

### Original plant and named bacterial scope

evidence: supported. Targets: CHEBI:65810.

The sole adopted abstract directly supports stem/leaf isolation and the three named bacterial species. Current ChEBI root metadata is a separate source inconsistency, not a demonstrated native error. Quantitative potency and exact primary material characterization remain limited.

### Unpopulated mechanism and target fields

completeness: unknown. Targets: CHEBI:65810.

No native mechanistic assertion requires correction. Docking supplies a hypothesis rather than direct biochemical evidence; absence of an optional target field is not a schema defect. No native gene/regulator/transcriptomic claim requires a structured gene adapter.

### Optional strain-specific activity and resistance enrichment

completeness: unknown. Targets: CHEBI:65810.

Recover original material, assay and strain details before importing numerical observations. Bacterial growth activity is not a demonstrated resistance allele, universal clinical efficacy or host-safety result.

### Clinical status, producer objects and causal graphs

scope: not_applicable. Targets: CHEBI:65810.

No such native objects are present. Plant isolation is contextual origin, not a verified microbial producer or an obligation to invent a causal graph.

### Generated status, source ownership and citation disposition

provenance: supported. Targets: CHEBI:65810.

All captured hashes, source mint and ordered history remain consistent. The original citation was assessed at its actual accessible depth, with later computational and biological sources separately scoped.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optional future enrichment should recover original characterization and assay details before assigning stereochemistry or numerical potency.

- Do not assign R/S solely from a (+) optical-rotation alias or infer a racemate from an unspecified graph.
- Keep keto–enol tautomer handling explicit and preserve positional-isomer distinctions.
- Read original material and assay conditions before importing individual strain-specific observations; do not transfer other compounds’ values.
- Keep docking and simulation as predictions rather than direct molecular-target experiments.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/drummondin-e.yaml; Entire YAML: definition, two synonyms,6 parents, role, all structure fields, one CAS identifier, source and three history events | supports | The SEEDED/EXACT record encodes neutral C28H34O8, key LACABBHUBUCHAU-UHFFFAOYSA-N, and one unspecified carbon stereocentre. The systematic name and (+)-name are source-derived. No quantitative spectrum, mode, molecular target, resistance, clinical product, structured producer or causal graph is populated. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact adopted source row1315; readiness1075; original thirteen hashes plus readiness context | supports | The frozen source supplies the chemical identity, aliases, parents, antibacterial role and sole PMID1800634 lead. Generated fields and three seed/reseed events reproduce. Fourteen captured input hashes remain unchanged; no native curation promotion or source edit occurred. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/65810/; Complete names, default structure, source identifiers, roles, parents and compound-origin metadata | supports | Current ChEBI reproduces the native graph and all structural classes. Its definition says stems and leaves, agreeing with the original abstract; a separate current compound-origin metadata field says root. That root metadata is not a native assertion and must not overwrite the supported definition. The filicinic-acid relationship is functional derivation, not an assertion that an exact small molecule is a broader class. |
| chemistry | Independent RDKit2026.03.5 / InChI1.07.3; 038-root-chemistry.py; atom mapping and stereochemistry-preserving tautomer comparison | supports | Native SMILES/InChI and current ChEBI molfile match LACABBHUBUCHAU-UHFFFAOYSA-N. PubChem132133 uses a different keto–enol drawing and key, but exact heavy-atom topology, formula, charge and reciprocal canonical-tautomer graph matching agree. Four mapped bond-order changes account for the keto/enol shift. Every input retains one unspecified centre; no R/S assignment or racemic state is inferred. |
| cas | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/132133/synonyms/JSON; Complete current PubChem alias list and adopted original PubMed chemical indexing | supports | PubChem associates drummondin E, (+)-drummondin E, the systematic names and CAS138169-54-7; the original PMID chemical indexing assigns the same CAS. Registry provenance is corroborated without claiming access to the proprietary CAS record. The (+) alias alone cannot determine an absolute R/S configuration. |
| classes | CHEBI:33823; CHEBI:51689; CHEBI:51867; CHEBI:76224; CHEBI:33572; CHEBI:35618; Complete current parent definitions and native graph comparison | supports | The native enol, conjugated ketone, methyl ketones and aromatic ketone satisfy the named broader classes. The meta-dihydroxy aromatic ring supports resorcinols, and the prenyl group attached through aromatic oxygen supports aromatic ether. Current filicinic-acid identity is consistent with the general derivative description. |
| adopted1991 | https://doi.org/10.1021/np50077a013; PMID1800634 complete original indexed abstract and chemical indexing | supports | The original paper explicitly includes drummondin E among compounds isolated by fractionation of H. drummondii stem/leaf hexane extract. It reports spectroscopy-based structures and activity against S. aureus, B. subtilis and M. smegmatis. The abstract supports those bounded claims but supplies no individual strain, test concentration, quantitative MIC or molecular target. The full publisher article was not independently recovered. |
| docking2016 | https://doi.org/10.3390/antibiotics5030030; PMID27626453/PMC5039526; original abstract, Computational Methods, exact drummondin Results paragraph and Conclusions | supports | Drummondin E is among561 phytochemicals screened computationally. The study predicts favorable docking to M. tuberculosis UDP-galactopyranose mutase and cites the1991 paper for bacterial activity. Rigid-receptor docking scores are not measured binding, enzyme inhibition, MICs or causal validation. No microbial target is added from this result. |
| activity2014 | https://doi.org/10.1002/cbdv.201300399; PMID24827680 complete original indexed abstract | supports | The original study identifies drummondin E as compound6 among six isolated compounds tested against vegetative P. larvae. The reported MIC range covers the entire six-compound panel and cannot be assigned as the exact drummondin E value. Spore experiments concern H. perforatum extract and hyperforin, not drummondin E. Publisher full-text routes returned403, so strain/material and individual potency remain unadopted. |
| computational2022 | https://doi.org/10.5114/bta.2022.113915; PMID36605381/PMC9642944; original abstract, Methods, Table1 and Conclusions | supports | The study selects PubChem132133 and its explicit SMILES for docking and molecular dynamics against SARS-CoV-2 RdRp. Activity, toxicity and drug-likeness claims derive from computational tools. The authors explicitly call for experimental validation. This is neither demonstrated antiviral efficacy nor an antibacterial mechanism; simulation is not an independent biochemical validation. |
| access | Public authority, exact adopted citation and original full-text discovery; 038-root-fetch manifests through fifth retrieval; OpenAlex exact DOI locations; ignored-inclusive local owner search | supports | Initial sandbox DNS failures were resolved by authorized public retrieval. A guessed ChEBI structure route returned JSON and another returned404; only the successful molfile endpoint was parsed as molfile. PubChem exact native-key search returned404 because its retrieved named representation uses a different tautomer. Publisher full text remained inaccessible; no access failure is evidence of an absent compound or paper. |

## Limits And Additional Notes

- The sole adopted1991 paper was read at complete original indexed-abstract depth. The original full structure drawing, NMR tables, optical-rotation conditions and antibacterial assay table were not independently recovered through the inspected public routes.
- One stereocentre is unassigned in native/current structures. Its absolute configuration remains unresolved; exact native connectivity does not certify a fully specified natural stereoisomer.
- Current ChEBI and PubChem represent different keto–enol tautomers. Independent atom mapping and stereochemistry-preserving tautomer comparison explain the difference; no unconditional full-key equivalence is claimed.
- The2016 original computational methods, exact Results paragraph and Conclusions were read; docking poses and all561 ligands were not independently reprocessed. Docking does not establish microbial target causality.
- The original CAS registry was not directly accessed. Current PubChem synonyms and original PubMed chemical indexing corroborate the asserted CAS/name relationship.
- No native/source/status/history was edited; shared required gates retain their actual outcomes.
- The2014 antibacterial paper was read at complete original abstract depth; its six-compound MIC range and hyperforin spore results are not drummondin E-specific observations. Full publisher access failed.
- The2022 computational original was read for Methods, Table1 and Conclusions; simulation trajectories were not rerun and predicted safety or antiviral efficacy is not experimentally certified.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T150800Z-drummondin-e-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Drummondin E: coherent tautomeric identity with unresolved stereochemistry'
started_at: '2026-10-21T14:43:56Z'
finished_at: '2026-10-21T15:08:00Z'
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
summary: The neutral drummondin E graph is internally coherent and matches current
  chemical authorities after explicitly accounting for keto–enol tautomerism. The
  sole adopted original abstract supports plant isolation and activity against the
  three named bacterial species. One stereocentre and primary assay details remain
  unresolved; no confirmed native correction is established. Scientific assessment
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
  - path: data/antibiotics/antibacterial/drummondin-e.yaml
    sha256: d9646f0abab4d2349775119cb4a1d7a2f8494fc9f928a0a08996fa84f45f5663
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
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
    role: context
targets:
- target_id: CHEBI:65810
  path: data/antibiotics/antibacterial/drummondin-e.yaml
  label: drummondin E
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
  selection: Initially uncovered queue position380; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65810
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65810
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    380
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65810
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/drummondin-e.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65810
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/drummondin-e.yaml --out /private/tmp/am-review-session/380-strict.tsv
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
  - CHEBI:65810
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
  - CHEBI:65810
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
  - CHEBI:65810
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
  - CHEBI:65810
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
  - CHEBI:65810
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
  - CHEBI:65810
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
  - CHEBI:65810
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
  - CHEBI:65810
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
  - CHEBI:65810
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/drummondin-e.yaml
  locator: 'Entire YAML: definition, two synonyms,6 parents, role, all structure fields,
    one CAS identifier, source and three history events'
  accessed_at: '2026-10-21T14:49:52Z'
  support: supports
  summary: The SEEDED/EXACT record encodes neutral C28H34O8, key LACABBHUBUCHAU-UHFFFAOYSA-N,
    and one unspecified carbon stereocentre. The systematic name and (+)-name are
    source-derived. No quantitative spectrum, mode, molecular target, resistance,
    clinical product, structured producer or causal graph is populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Exact adopted source row1315; readiness1075; original thirteen hashes plus
    readiness context
  accessed_at: '2026-10-21T14:49:52Z'
  support: supports
  summary: The frozen source supplies the chemical identity, aliases, parents, antibacterial
    role and sole PMID1800634 lead. Generated fields and three seed/reseed events
    reproduce. Fourteen captured input hashes remain unchanged; no native curation
    promotion or source edit occurred.
  snapshot_sha256: 3efe7ec972bd24a2847717dbefeb9aa08db0af715eef516a37afd5f5de0d7bbc
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/65810/
  locator: Complete names, default structure, source identifiers, roles, parents and
    compound-origin metadata
  accessed_at: '2026-10-21T14:49:52Z'
  support: supports
  summary: Current ChEBI reproduces the native graph and all structural classes. Its
    definition says stems and leaves, agreeing with the original abstract; a separate
    current compound-origin metadata field says root. That root metadata is not a
    native assertion and must not overwrite the supported definition. The filicinic-acid
    relationship is functional derivation, not an assertion that an exact small molecule
    is a broader class.
  snapshot_sha256: f19e201653f2f477c5504ae4de241364b2d69fbf447d60dad23e98467468591b
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit2026.03.5 / InChI1.07.3
  locator: 038-root-chemistry.py; atom mapping and stereochemistry-preserving tautomer
    comparison
  accessed_at: '2026-10-21T14:49:52Z'
  support: supports
  summary: Native SMILES/InChI and current ChEBI molfile match LACABBHUBUCHAU-UHFFFAOYSA-N.
    PubChem132133 uses a different keto–enol drawing and key, but exact heavy-atom
    topology, formula, charge and reciprocal canonical-tautomer graph matching agree.
    Four mapped bond-order changes account for the keto/enol shift. Every input retains
    one unspecified centre; no R/S assignment or racemic state is inferred.
  snapshot_sha256: 65250899ea6c3ffc85517785e1cb4c8fc913e858e81266e19465ed6dd15efa03
- evidence_id: cas
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/132133/synonyms/JSON
  locator: Complete current PubChem alias list and adopted original PubMed chemical
    indexing
  accessed_at: '2026-10-21T14:49:52Z'
  support: supports
  summary: PubChem associates drummondin E, (+)-drummondin E, the systematic names
    and CAS138169-54-7; the original PMID chemical indexing assigns the same CAS.
    Registry provenance is corroborated without claiming access to the proprietary
    CAS record. The (+) alias alone cannot determine an absolute R/S configuration.
  snapshot_sha256: df14ccbd940e2c0aa3fae808364a59aa32071c1db4f0adfa31546411d2822fbf
- evidence_id: classes
  kind: authority
  reference: CHEBI:33823; CHEBI:51689; CHEBI:51867; CHEBI:76224; CHEBI:33572; CHEBI:35618
  locator: Complete current parent definitions and native graph comparison
  accessed_at: '2026-10-21T14:49:52Z'
  support: supports
  summary: The native enol, conjugated ketone, methyl ketones and aromatic ketone
    satisfy the named broader classes. The meta-dihydroxy aromatic ring supports resorcinols,
    and the prenyl group attached through aromatic oxygen supports aromatic ether.
    Current filicinic-acid identity is consistent with the general derivative description.
  snapshot_sha256: 3773760f57ea2d844685e1b715dbfddf1c334b246027c8a748baeef6efe72b16
- evidence_id: adopted1991
  kind: primary_source
  reference: https://doi.org/10.1021/np50077a013
  locator: PMID1800634 complete original indexed abstract and chemical indexing
  accessed_at: '2026-10-21T14:49:52Z'
  support: supports
  summary: The original paper explicitly includes drummondin E among compounds isolated
    by fractionation of H. drummondii stem/leaf hexane extract. It reports spectroscopy-based
    structures and activity against S. aureus, B. subtilis and M. smegmatis. The abstract
    supports those bounded claims but supplies no individual strain, test concentration,
    quantitative MIC or molecular target. The full publisher article was not independently
    recovered.
  snapshot_sha256: 8b2d8788e4ee3354dca04466276b2699105c59514cdc13b6f04afe9effff945e
- evidence_id: docking2016
  kind: primary_source
  reference: https://doi.org/10.3390/antibiotics5030030
  locator: PMID27626453/PMC5039526; original abstract, Computational Methods, exact
    drummondin Results paragraph and Conclusions
  accessed_at: '2026-10-21T14:49:52Z'
  support: supports
  summary: Drummondin E is among561 phytochemicals screened computationally. The study
    predicts favorable docking to M. tuberculosis UDP-galactopyranose mutase and cites
    the1991 paper for bacterial activity. Rigid-receptor docking scores are not measured
    binding, enzyme inhibition, MICs or causal validation. No microbial target is
    added from this result.
  snapshot_sha256: 80c5a65ef46bda6664afd765d3ba70a6f1d2ebae2c8b3f6c7a6f2cdb0306c84b
- evidence_id: activity2014
  kind: primary_source
  reference: https://doi.org/10.1002/cbdv.201300399
  locator: PMID24827680 complete original indexed abstract
  accessed_at: '2026-10-21T14:49:52Z'
  support: supports
  summary: The original study identifies drummondin E as compound6 among six isolated
    compounds tested against vegetative P. larvae. The reported MIC range covers the
    entire six-compound panel and cannot be assigned as the exact drummondin E value.
    Spore experiments concern H. perforatum extract and hyperforin, not drummondin
    E. Publisher full-text routes returned403, so strain/material and individual potency
    remain unadopted.
  snapshot_sha256: 106fc4388ae7f7ead1112eec34c6fb6911a3fcc64610cb65c942999ff3280a6f
- evidence_id: computational2022
  kind: primary_source
  reference: https://doi.org/10.5114/bta.2022.113915
  locator: PMID36605381/PMC9642944; original abstract, Methods, Table1 and Conclusions
  accessed_at: '2026-10-21T14:49:52Z'
  support: supports
  summary: The study selects PubChem132133 and its explicit SMILES for docking and
    molecular dynamics against SARS-CoV-2 RdRp. Activity, toxicity and drug-likeness
    claims derive from computational tools. The authors explicitly call for experimental
    validation. This is neither demonstrated antiviral efficacy nor an antibacterial
    mechanism; simulation is not an independent biochemical validation.
  snapshot_sha256: 8a92caeca0a246476310f3300ee60af495f44c422e9d16165303fccecd9e0e02
- evidence_id: access
  kind: search
  reference: Public authority, exact adopted citation and original full-text discovery
  locator: 038-root-fetch manifests through fifth retrieval; OpenAlex exact DOI locations;
    ignored-inclusive local owner search
  accessed_at: '2026-10-21T14:49:52Z'
  support: supports
  summary: Initial sandbox DNS failures were resolved by authorized public retrieval.
    A guessed ChEBI structure route returned JSON and another returned404; only the
    successful molfile endpoint was parsed as molfile. PubChem exact native-key search
    returned404 because its retrieved named representation uses a different tautomer.
    Publisher full text remained inaccessible; no access failure is evidence of an
    absent compound or paper.
  search_scope: 2026-10-21; rg --no-ignore --hidden across maintained curation, conf,
    scripts, data/raw and .claude plus original repository inspection for drummondin
    E, exact ChEBI and key. Public exact PMID/DOI, name, CAS and stereochemistry follow-up.
    No exhaustive absence claim.
  snapshot_sha256: 3de668d9f6de8497e29c5b0328a0a7b0eda41466e3813a2dfe7f58190cd5693c
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral connectivity and tautomeric authority comparison
  outcome: supported
  summary: All native fields are coherent. Explicit chemical comparison reconciles
    current PubChem tautomerism rather than treating differing full keys as automatically
    different compounds.
  target_ids:
  - CHEBI:65810
  evidence_ids:
  - native
  - chemistry
  - chebi
  - cas
- assessment_id: stereochemistry
  area: identity
  topic: One unassigned centre and positive-rotation name
  outcome: unknown
  summary: Native and inspected independent encodings omit the same stereocentre.
    The (+) alias is consistently source-attested, but the unavailable original characterization
    prevents independent confirmation of its measured rotation or an absolute assignment.
    Neither a wrong epimer nor a racemate is demonstrated.
  target_ids:
  - CHEBI:65810
  evidence_ids:
  - native
  - chemistry
  - cas
  - adopted1991
  - access
- assessment_id: classes
  area: grounding
  topic: Broader structural classes and exact CAS
  outcome: supported
  summary: Parent classes fit the graph, and exact CAS/name provenance is corroborated.
    No salt, hydrate, mixture or unrelated positional isomer is substituted.
  target_ids:
  - CHEBI:65810
  evidence_ids:
  - classes
  - chemistry
  - cas
- assessment_id: definition
  area: evidence
  topic: Original plant and named bacterial scope
  outcome: supported
  summary: The sole adopted abstract directly supports stem/leaf isolation and the
    three named bacterial species. Current ChEBI root metadata is a separate source
    inconsistency, not a demonstrated native error. Quantitative potency and exact
    primary material characterization remain limited.
  target_ids:
  - CHEBI:65810
  evidence_ids:
  - adopted1991
  - chebi
  - access
- assessment_id: mechanism
  area: completeness
  topic: Unpopulated mechanism and target fields
  outcome: unknown
  summary: No native mechanistic assertion requires correction. Docking supplies a
    hypothesis rather than direct biochemical evidence; absence of an optional target
    field is not a schema defect. No native gene/regulator/transcriptomic claim requires
    a structured gene adapter.
  target_ids:
  - CHEBI:65810
  evidence_ids:
  - native
  - docking2016
  - computational2022
- assessment_id: activity
  area: completeness
  topic: Optional strain-specific activity and resistance enrichment
  outcome: unknown
  summary: Recover original material, assay and strain details before importing numerical
    observations. Bacterial growth activity is not a demonstrated resistance allele,
    universal clinical efficacy or host-safety result.
  target_ids:
  - CHEBI:65810
  evidence_ids:
  - native
  - adopted1991
  - activity2014
- assessment_id: other
  area: scope
  topic: Clinical status, producer objects and causal graphs
  outcome: not_applicable
  summary: No such native objects are present. Plant isolation is contextual origin,
    not a verified microbial producer or an obligation to invent a causal graph.
  target_ids:
  - CHEBI:65810
  evidence_ids:
  - native
  - adopted1991
- assessment_id: provenance
  area: provenance
  topic: Generated status, source ownership and citation disposition
  outcome: supported
  summary: All captured hashes, source mint and ordered history remain consistent.
    The original citation was assessed at its actual accessible depth, with later
    computational and biological sources separately scoped.
  target_ids:
  - CHEBI:65810
  evidence_ids:
  - owners
  - adopted1991
  - access
findings: []
actions:
- action_id: A1
  description: Optional future enrichment should recover original characterization
    and assay details before assigning stereochemistry or numerical potency.
  finding_ids: []
  target_ids:
  - CHEBI:65810
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/drummondin-e.yaml
    role: Future curator-owned evidence and history
  acceptance_checks:
  - Do not assign R/S solely from a (+) optical-rotation alias or infer a racemate
    from an unspecified graph.
  - Keep keto–enol tautomer handling explicit and preserve positional-isomer distinctions.
  - Read original material and assay conditions before importing individual strain-specific
    observations; do not transfer other compounds’ values.
  - Keep docking and simulation as predictions rather than direct molecular-target
    experiments.
limitations:
- The sole adopted1991 paper was read at complete original indexed-abstract depth.
  The original full structure drawing, NMR tables, optical-rotation conditions and
  antibacterial assay table were not independently recovered through the inspected
  public routes.
- One stereocentre is unassigned in native/current structures. Its absolute configuration
  remains unresolved; exact native connectivity does not certify a fully specified
  natural stereoisomer.
- Current ChEBI and PubChem represent different keto–enol tautomers. Independent atom
  mapping and stereochemistry-preserving tautomer comparison explain the difference;
  no unconditional full-key equivalence is claimed.
- The2016 original computational methods, exact Results paragraph and Conclusions
  were read; docking poses and all561 ligands were not independently reprocessed.
  Docking does not establish microbial target causality.
- The original CAS registry was not directly accessed. Current PubChem synonyms and
  original PubMed chemical indexing corroborate the asserted CAS/name relationship.
- No native/source/status/history was edited; shared required gates retain their actual
  outcomes.
- The2014 antibacterial paper was read at complete original abstract depth; its six-compound
  MIC range and hyperforin spore results are not drummondin E-specific observations.
  Full publisher access failed.
- The2022 computational original was read for Methods, Table1 and Conclusions; simulation
  trajectories were not rerun and predicted safety or antiviral efficacy is not experimentally
  certified.
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
