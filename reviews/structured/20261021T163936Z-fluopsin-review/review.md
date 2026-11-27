# fluopsin: exact identity and primary-evidence boundaries

- Review: 20261021T163936Z-fluopsin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:12:28Z
- Finished UTC: 2026-10-21T16:39:36Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The neutral free ligand is structurally supported by original synthesis/degradation and modern biosynthetic work. Original authors describe thioformin as an antibiotic, but the inspected numerical MIC tables primarily concern metal complexes or derivatives. Exact free-ligand quantitative activity remains unresolved; no transfer from the copper complex is made. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position450; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:231919 | data/antibiotics/antibacterial/fluopsin.yaml | generated | fluopsin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:231919 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:231919 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:231919 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:231919 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:231919 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:231919 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:231919 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:231919 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:231919 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:231919 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:231919 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:231919 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact molecular representation

identity: supported. Targets: CHEBI:231919.

The native graph, formula C2H5NOS, charge and mass agree across independent encodings. Original synthesis/degradation and modern Figure4 identify the same neutral free ligand; metal complexes and derivatives remain distinct.

### Chemical, drug and document groundings

grounding: supported. Targets: CHEBI:231919.

The exact CAS public lookup agrees; an independent proprietary registry record is not available. All five native chemical synonyms describe the free ligand, not a metal complex.

### Parents and antibacterial eligibility

scope: unknown. Targets: CHEBI:231919.

Hydroxylamine and thiocarbonyl parents match the graph. Original authors describe thioformin as an antibiotic, and the role permits an active part of a substance, so complex-associated evidence does not prove the role false. However, exact free-ligand quantitative activity and metal speciation in assay media remain unresolved.

### Native target assertions and prospective mechanism

evidence: unknown. Targets: CHEBI:231919.

No native direct target is asserted. Biosynthetic Flc proteins, ferric-complex QSAR and copper-complex membrane phenotypes do not establish a free-ligand molecular target.

### Optional activity, resistance and producer enrichment

completeness: unknown. Targets: CHEBI:231919.

Free-ligand bioactivity would need exact material, medium, metal content and endpoint reconciliation. The inspected ferric/copper and O-acyl MICs cannot populate this neutral record as exact-compound observations.

### Maintained sources and historical events

provenance: supported. Targets: CHEBI:231919.

The entire source rows and native seed/reseed histories were read; original hashes are preserved and actual additional owners captured. Authority updates do not silently rewrite historical provenance. No native or source file is edited.

### Actual checks

schema: supported. Targets: CHEBI:231919.

Focused native schema, strict and chemistry checks passed. Independent authority graph comparisons also passed. Shared required checks are attached at finalization, with their existing failure retained.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A2

For optional enrichment, resolve exact experimental material and claim-level evidence before adding assertions.

- Locate and read an exact free-ligand bacterial assay, including material and medium metal content, before numeric enrichment.
- Do not transfer ferric/copper-complex or O-acyl derivative MICs into the neutral record.
- Keep biosynthetic enzyme activity separate from antibacterial target claims.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/fluopsin.yaml; Entire native YAML, all names, groundings, classifications and history events | supports | The complete SEEDED/EXACT record CHEBI:231919 was read. It describes the neutral C2H5NOS free ligand with five synonyms, hydroxylamine and thiocarbonyl parents, one antibacterial role and one CAS accession. No copper, iron, protein target, producer collection or numerical assay is asserted. |
| owners | 450-source-rows.json; Exact maintained source rows, readiness pointer and expanded capture | supports | All original thirteen input hashes are preserved within 14 captured inputs. The CHEBI231919 source row was read separately from the CHEBI222417 copper-complex row. It supplies the free-ligand graph, names, role, CAS and five adopted PMID leads. The readiness pointer is not evidence of activity. |
| local | 450-local-hits.txt; Ignored- and hidden-inclusive local identity and owner search | context_only | The complete search included ignored and hidden files. Exact maintained rows and generated annotations were inspected. No additional exact curator override was identified in this bounded repository search; this does not establish global evidence absence. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/231919/; Current full compound export: graph, names, roles, origins, parent relationships and accessions | supports | Current ChEBI reproduces the native graph, formula C2H5NOS, zero net charge and key LSLVHNSGLHQBDX-UHFFFAOYSA-N. Source agreement is recorded separately from primary biological evidence. |
| chemistry | 450-authority-chemistry.json; Independent native/current ChEBI molfile and PubChem graph comparison | supports | Native SMILES and InChI, ChEBI SMILES and molfile, and PubChem SMILES and InChI all give LSLVHNSGLHQBDX-UHFFFAOYSA-N, formula C2H5NOS and charge zero. The neutral molecule has no tetrahedral stereocentres. Its graph is distinct from both the copper complex and ferric complexes; neither metal formulation is an exact synonym. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/LSLVHNSGLHQBDX-UHFFFAOYSA-N/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; Current PubChem structure properties | supports | The independently parsed structure agrees with the exact native graph and mass/formula. This is independent structure corroboration; no new native identifier is added. |
| term-24709 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/24709/; Current asserted class or role definition | supports | CHEBI:24709 resolves as hydroxylamines. The term was assessed against the native graph or original activity/product evidence. |
| term-50492 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/50492/; Current asserted class or role definition | supports | CHEBI:50492 resolves as thiocarbonyl compound. The term was assessed against the native graph or original activity/product evidence. |
| term-33282 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/; Current asserted class or role definition | supports | CHEBI:33282 resolves as antibacterial agent. The role explicitly includes a substance or active part thereof that kills or slows bacterial growth. |
| gates | 450-focused-results.json; Executed native schema, strict and chemical checks | supports | All focused checks passed on the untouched native record. Structural checks do not replace primary biological evidence. |
| adapter | iModulonDB; Actual pre-follow-up catalog and relevant bacterial query | context_only | The structured catalog completed. The same catalog and copper-pathway discovery query were consulted; hflC is an unrelated substring match. Biosynthetic enzymes are not direct antibacterial targets of the ligand. |
| original1971 | https://doi.org/10.7164/antibiotics.24.124; PMID5549384; full seven-page original OCR, actual page126 structure and table viewed | supports | The original removes copper from YC73, isolates neutral C2H5NOS thioformin and verifies N-methyl-N-thioformylhydroxylamine by degradation, synthesis and matching IR/UV/NMR. Recomplexation gives the original Cu(II) antibiotic with two ligands per metal. Table1 assays are O-acyl/aryl derivatives; Table2 assays are metal complexes. The free ligand is explicitly described as an acidic antibiotic, with bioautographic detection, but no exact free-ligand numeric MIC is imported. |
| original1971-analogues | https://doi.org/10.7164/antibiotics.24.131; PMID4927254; full four-page original OCR | supports | The introduction explicitly describes thioformin itself as having antimicrobial activity. The actual comparative Table1 is labeled ferric complexes, including the methyl parent, so these numbers are not free-ligand measurements. Synthetic intermediates and substituted analogues remain distinct. |
| original1974 | https://doi.org/10.1248/cpb.22.2283; PMID4468081; original first two pages, introduction/material and antibacterial-method scope | supports | The paper distinguishes thioformin from its copper and ferric complexes and identifies historical P. fluorescens MCRL-10107 production of YC73. It explicitly tests stable metal complexes because free acids are often unstable; the MIC table is ferric derivatives. Those observations do not establish copper-free quantitative activity. The historical source does not contradict modern P. aeruginosa production. |
| qsar1974 | https://doi.org/10.1248/cpb.22.2288; PMID4219752; full six-page original OCR | supports | Despite generic thioformylhydroxylamine terminology, Methods and TablesI/III explicitly use ferric complexes. Hansch-Fujita regressions are correlations of hydrophobicity with bacterial growth inhibition, not direct molecular-binding experiments and not free-ligand MICs. |
| science2021 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8939262/; PMID34793213 / DOI10.1126/science.abj6749; complete main prose and captions, actual Figure4 viewed | supports | Original PAO1 insertion mutants and heterologous P. fluorescens SBW25 expression establish PA3515–PA3519/flcA–E biosynthesis of fluopsin C under copper stress. Purified-enzyme reconstitution yields the Cu-free ligand6 before added copper produces complex1. Figure4 explicitly draws the same neutral ligand and copper complex as the native records. The enzymes synthesize the antibiotic; they are not its antibacterial protein targets. Isotope labeling supports cysteine/methionine-derived atoms. |
| geometry2021 | https://doi.org/10.1126/science.abj6749; Original EPR/ENDOR and reductant paragraphs with Figure1 caption | partial | Cu(II) is experimentally supported. The toluene sample contains cis/trans coordination isomers, approximately1:1 at room temperature and1:6 at15K. Native encodings do not claim one fixed geometry. Reductant-induced spectra suggest intracellular Cu(I), but this does not replace the isolated Cu(II) formula or prove the in-cell active species. The original SI request returned challenge HTML and was not treated as a readable PDF. |
| cas | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/31335-60-1/property/IsomericSMILES,InChI,InChIKey,MolecularFormula/JSON; Exact native CAS lookup in public PubChem | supports | The CAS lookup returns the same full InChIKey and formula. This is corroborating cross-reference evidence, not independent access to the proprietary CAS registry. |
| adopted | 450-adopted-core.json; All five adopted PMID leads individually followed | partial | PMID5549384 establishes free-ligand identity;4927254 describes free-ligand activity qualitatively but assays ferric analogues;4468081 assays stable metal complexes;4219752 is ferric-complex QSAR;34793213 establishes Cu-free ligand6 as a biosynthetic intermediate and distinguishes complex1. Each original was read at the depth separately documented; the copper-complex antibacterial panel is not transferred. |

## Limits And Additional Notes

- Review is bounded to the inspected original material, current authority exports and explicit local search; no global evidence absence is asserted.
- Optional absent schema fields are not treated as defects. No native, maintained source or previously saved review is edited.
- The1971 structure and analogue papers and1974 QSAR paper were read through full OCR; the1971 page126 structure/table was visually inspected. The1974 synthesis paper was read for its first two pages and assay-material scope.
- Original quantitative tables mainly concern metal complexes or derivatives. Free-ligand activity is described qualitatively, but exact independent MIC/speciation remains unresolved.
- The2021 main biosynthetic paper and actual Figure4 were inspected; its SI was inaccessible. Public CAS lookup does not certify an independently obtained proprietary registry graph.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Native curation status remains SEEDED. This review records evidence boundaries without changing the record.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T163936Z-fluopsin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'fluopsin: exact identity and primary-evidence boundaries'
started_at: '2026-10-21T16:12:28Z'
finished_at: '2026-10-21T16:39:36Z'
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
summary: The neutral free ligand is structurally supported by original synthesis/degradation
  and modern biosynthetic work. Original authors describe thioformin as an antibiotic,
  but the inspected numerical MIC tables primarily concern metal complexes or derivatives.
  Exact free-ligand quantitative activity remains unresolved; no transfer from the
  copper complex is made. Scientific assessment retains the stated evidence limits;
  full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/fluopsin.yaml
    sha256: 81f2f4c7802d3ff3031b513690cbdb0f285380b716a21631469b504c9bd02b9c
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
- target_id: CHEBI:231919
  path: data/antibiotics/antibacterial/fluopsin.yaml
  label: fluopsin
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
  selection: Initially uncovered queue position450; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:231919
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:231919
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    450
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:231919
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/fluopsin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:231919
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/fluopsin.yaml --out /private/tmp/am-review-session/450-strict.tsv
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
  - CHEBI:231919
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
  - CHEBI:231919
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
  - CHEBI:231919
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
  - CHEBI:231919
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
  - CHEBI:231919
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
  - CHEBI:231919
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
  - CHEBI:231919
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
  - CHEBI:231919
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
  - CHEBI:231919
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/fluopsin.yaml
  locator: Entire native YAML, all names, groundings, classifications and history
    events
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: The complete SEEDED/EXACT record CHEBI:231919 was read. It describes the
    neutral C2H5NOS free ligand with five synonyms, hydroxylamine and thiocarbonyl
    parents, one antibacterial role and one CAS accession. No copper, iron, protein
    target, producer collection or numerical assay is asserted.
- evidence_id: owners
  kind: record_content
  reference: 450-source-rows.json
  locator: Exact maintained source rows, readiness pointer and expanded capture
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: All original thirteen input hashes are preserved within 14 captured inputs.
    The CHEBI231919 source row was read separately from the CHEBI222417 copper-complex
    row. It supplies the free-ligand graph, names, role, CAS and five adopted PMID
    leads. The readiness pointer is not evidence of activity.
  snapshot_sha256: 6c5eb4a3ca9792bb192fa4321904fc1fc316006dc59a5a084122ef5986c6fbea
- evidence_id: local
  kind: search
  reference: 450-local-hits.txt
  locator: Ignored- and hidden-inclusive local identity and owner search
  accessed_at: '2026-10-21T16:24:41Z'
  support: context_only
  summary: The complete search included ignored and hidden files. Exact maintained
    rows and generated annotations were inspected. No additional exact curator override
    was identified in this bounded repository search; this does not establish global
    evidence absence.
  search_scope: rg --no-ignore --hidden exact fluopsin name, identifier and source
    mint in own batch045 checkout, excluding Git metadata and virtual environment
  snapshot_sha256: a1efd45c5754480eb361dabf48c7a23721bf1301f3474c309f6a011a905d95e8
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/231919/
  locator: 'Current full compound export: graph, names, roles, origins, parent relationships
    and accessions'
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: Current ChEBI reproduces the native graph, formula C2H5NOS, zero net charge
    and key LSLVHNSGLHQBDX-UHFFFAOYSA-N. Source agreement is recorded separately from
    primary biological evidence.
  snapshot_sha256: 47e2b6f905c1d8c2b10fa00067c23cb5cd18e5e551f744889b100daa58043a6e
- evidence_id: chemistry
  kind: record_content
  reference: 450-authority-chemistry.json
  locator: Independent native/current ChEBI molfile and PubChem graph comparison
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: Native SMILES and InChI, ChEBI SMILES and molfile, and PubChem SMILES and
    InChI all give LSLVHNSGLHQBDX-UHFFFAOYSA-N, formula C2H5NOS and charge zero. The
    neutral molecule has no tetrahedral stereocentres. Its graph is distinct from
    both the copper complex and ferric complexes; neither metal formulation is an
    exact synonym.
  snapshot_sha256: 4fc571396b74d51384d00eac8e99b38aa53b19f291e49b607e5455cd5022cb40
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/LSLVHNSGLHQBDX-UHFFFAOYSA-N/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: Current PubChem structure properties
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: The independently parsed structure agrees with the exact native graph and
    mass/formula. This is independent structure corroboration; no new native identifier
    is added.
  snapshot_sha256: 8c076c452523524ac494a1c15cfe28f1b15d9518bf61621e94b0ae26435cc4eb
- evidence_id: term-24709
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/24709/
  locator: Current asserted class or role definition
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: CHEBI:24709 resolves as hydroxylamines. The term was assessed against the
    native graph or original activity/product evidence.
  snapshot_sha256: d8e990375b71b201825a3d28a9f4e628e1b6d1d1b99337a59d49bab937bf297c
- evidence_id: term-50492
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/50492/
  locator: Current asserted class or role definition
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: CHEBI:50492 resolves as thiocarbonyl compound. The term was assessed against
    the native graph or original activity/product evidence.
  snapshot_sha256: e4c95bfbe3602ba9b9522307c945a4994dc654662c5cc33eab0e476af07db076
- evidence_id: term-33282
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/
  locator: Current asserted class or role definition
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: CHEBI:33282 resolves as antibacterial agent. The role explicitly includes
    a substance or active part thereof that kills or slows bacterial growth.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: gates
  kind: record_content
  reference: 450-focused-results.json
  locator: Executed native schema, strict and chemical checks
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: All focused checks passed on the untouched native record. Structural checks
    do not replace primary biological evidence.
  snapshot_sha256: 633bd911a36f4a5366ee62b32aa10b695230cc29c4b948ce570e8e653de8d7b9
- evidence_id: adapter
  kind: database
  reference: iModulonDB
  locator: Actual pre-follow-up catalog and relevant bacterial query
  accessed_at: '2026-10-21T16:24:41Z'
  support: context_only
  summary: The structured catalog completed. The same catalog and copper-pathway discovery
    query were consulted; hflC is an unrelated substring match. Biosynthetic enzymes
    are not direct antibacterial targets of the ligand.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: original1971
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.24.124
  locator: PMID5549384; full seven-page original OCR, actual page126 structure and
    table viewed
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: The original removes copper from YC73, isolates neutral C2H5NOS thioformin
    and verifies N-methyl-N-thioformylhydroxylamine by degradation, synthesis and
    matching IR/UV/NMR. Recomplexation gives the original Cu(II) antibiotic with two
    ligands per metal. Table1 assays are O-acyl/aryl derivatives; Table2 assays are
    metal complexes. The free ligand is explicitly described as an acidic antibiotic,
    with bioautographic detection, but no exact free-ligand numeric MIC is imported.
  snapshot_sha256: 537687a7b2c56a380c852b97247c1198a2c6b5d27ca90789a4325918eba5fd84
- evidence_id: original1971-analogues
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.24.131
  locator: PMID4927254; full four-page original OCR
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: The introduction explicitly describes thioformin itself as having antimicrobial
    activity. The actual comparative Table1 is labeled ferric complexes, including
    the methyl parent, so these numbers are not free-ligand measurements. Synthetic
    intermediates and substituted analogues remain distinct.
  snapshot_sha256: b82cab2b411253c73896c30741a307992ba10100f9a327f7535c15a94488fbb9
- evidence_id: original1974
  kind: primary_source
  reference: https://doi.org/10.1248/cpb.22.2283
  locator: PMID4468081; original first two pages, introduction/material and antibacterial-method
    scope
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: The paper distinguishes thioformin from its copper and ferric complexes
    and identifies historical P. fluorescens MCRL-10107 production of YC73. It explicitly
    tests stable metal complexes because free acids are often unstable; the MIC table
    is ferric derivatives. Those observations do not establish copper-free quantitative
    activity. The historical source does not contradict modern P. aeruginosa production.
  snapshot_sha256: 9b47df31d511e2f5b75fda0efdd61da25f64377daf05f409bd7880732030313e
- evidence_id: qsar1974
  kind: primary_source
  reference: https://doi.org/10.1248/cpb.22.2288
  locator: PMID4219752; full six-page original OCR
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: Despite generic thioformylhydroxylamine terminology, Methods and TablesI/III
    explicitly use ferric complexes. Hansch-Fujita regressions are correlations of
    hydrophobicity with bacterial growth inhibition, not direct molecular-binding
    experiments and not free-ligand MICs.
  snapshot_sha256: d79b383e91d407c539926fc9689c670d189ca19868d76e9fbc87e2e9b665f20f
- evidence_id: science2021
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8939262/
  locator: PMID34793213 / DOI10.1126/science.abj6749; complete main prose and captions,
    actual Figure4 viewed
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: Original PAO1 insertion mutants and heterologous P. fluorescens SBW25 expression
    establish PA3515–PA3519/flcA–E biosynthesis of fluopsin C under copper stress.
    Purified-enzyme reconstitution yields the Cu-free ligand6 before added copper
    produces complex1. Figure4 explicitly draws the same neutral ligand and copper
    complex as the native records. The enzymes synthesize the antibiotic; they are
    not its antibacterial protein targets. Isotope labeling supports cysteine/methionine-derived
    atoms.
  snapshot_sha256: 2259a8523d0f3fad4a9059e6de8ac4639244ca400aac879c96a00120208e1ca5
- evidence_id: geometry2021
  kind: primary_source
  reference: https://doi.org/10.1126/science.abj6749
  locator: Original EPR/ENDOR and reductant paragraphs with Figure1 caption
  accessed_at: '2026-10-21T16:24:41Z'
  support: partial
  summary: Cu(II) is experimentally supported. The toluene sample contains cis/trans
    coordination isomers, approximately1:1 at room temperature and1:6 at15K. Native
    encodings do not claim one fixed geometry. Reductant-induced spectra suggest intracellular
    Cu(I), but this does not replace the isolated Cu(II) formula or prove the in-cell
    active species. The original SI request returned challenge HTML and was not treated
    as a readable PDF.
  snapshot_sha256: 2259a8523d0f3fad4a9059e6de8ac4639244ca400aac879c96a00120208e1ca5
- evidence_id: cas
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/31335-60-1/property/IsomericSMILES,InChI,InChIKey,MolecularFormula/JSON
  locator: Exact native CAS lookup in public PubChem
  accessed_at: '2026-10-21T16:24:41Z'
  support: supports
  summary: The CAS lookup returns the same full InChIKey and formula. This is corroborating
    cross-reference evidence, not independent access to the proprietary CAS registry.
  snapshot_sha256: 16f470822615620b940c4febb95346ad811161df74ac7c0852919f44a40c5d2f
- evidence_id: adopted
  kind: record_content
  reference: 450-adopted-core.json
  locator: All five adopted PMID leads individually followed
  accessed_at: '2026-10-21T16:24:41Z'
  support: partial
  summary: PMID5549384 establishes free-ligand identity;4927254 describes free-ligand
    activity qualitatively but assays ferric analogues;4468081 assays stable metal
    complexes;4219752 is ferric-complex QSAR;34793213 establishes Cu-free ligand6
    as a biosynthetic intermediate and distinguishes complex1. Each original was read
    at the depth separately documented; the copper-complex antibacterial panel is
    not transferred.
  snapshot_sha256: 5676ab8589f02e4b4607759b9db13d04cedc780af0ce1df01a5d9572f8b10d3f
assessments:
- assessment_id: identity
  area: identity
  topic: Exact molecular representation
  outcome: supported
  summary: The native graph, formula C2H5NOS, charge and mass agree across independent
    encodings. Original synthesis/degradation and modern Figure4 identify the same
    neutral free ligand; metal complexes and derivatives remain distinct.
  target_ids:
  - CHEBI:231919
  evidence_ids:
  - native
  - chebi
  - chemistry
  - pubchem
  - original1971
  - science2021
- assessment_id: grounding
  area: grounding
  topic: Chemical, drug and document groundings
  outcome: supported
  summary: The exact CAS public lookup agrees; an independent proprietary registry
    record is not available. All five native chemical synonyms describe the free ligand,
    not a metal complex.
  target_ids:
  - CHEBI:231919
  evidence_ids:
  - native
  - chebi
  - chemistry
  - cas
  - original1971
- assessment_id: classification
  area: scope
  topic: Parents and antibacterial eligibility
  outcome: unknown
  summary: Hydroxylamine and thiocarbonyl parents match the graph. Original authors
    describe thioformin as an antibiotic, and the role permits an active part of a
    substance, so complex-associated evidence does not prove the role false. However,
    exact free-ligand quantitative activity and metal speciation in assay media remain
    unresolved.
  target_ids:
  - CHEBI:231919
  evidence_ids:
  - term-24709
  - term-50492
  - term-33282
  - original1971
  - original1971-analogues
  - qsar1974
- assessment_id: mechanism
  area: evidence
  topic: Native target assertions and prospective mechanism
  outcome: unknown
  summary: No native direct target is asserted. Biosynthetic Flc proteins, ferric-complex
    QSAR and copper-complex membrane phenotypes do not establish a free-ligand molecular
    target.
  target_ids:
  - CHEBI:231919
  evidence_ids:
  - native
  - adapter
  - science2021
  - qsar1974
- assessment_id: completeness
  area: completeness
  topic: Optional activity, resistance and producer enrichment
  outcome: unknown
  summary: Free-ligand bioactivity would need exact material, medium, metal content
    and endpoint reconciliation. The inspected ferric/copper and O-acyl MICs cannot
    populate this neutral record as exact-compound observations.
  target_ids:
  - CHEBI:231919
  evidence_ids:
  - native
  - local
  - original1971
  - original1974
  - science2021
  - qsar1974
- assessment_id: provenance
  area: provenance
  topic: Maintained sources and historical events
  outcome: supported
  summary: The entire source rows and native seed/reseed histories were read; original
    hashes are preserved and actual additional owners captured. Authority updates
    do not silently rewrite historical provenance. No native or source file is edited.
  target_ids:
  - CHEBI:231919
  evidence_ids:
  - native
  - owners
  - local
  - gates
- assessment_id: validation
  area: schema
  topic: Actual checks
  outcome: supported
  summary: Focused native schema, strict and chemistry checks passed. Independent
    authority graph comparisons also passed. Shared required checks are attached at
    finalization, with their existing failure retained.
  target_ids:
  - CHEBI:231919
  evidence_ids:
  - gates
  - chemistry
findings: []
actions:
- action_id: A2
  description: For optional enrichment, resolve exact experimental material and claim-level
    evidence before adding assertions.
  finding_ids: []
  target_ids:
  - CHEBI:231919
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
  acceptance_checks:
  - Locate and read an exact free-ligand bacterial assay, including material and medium
    metal content, before numeric enrichment.
  - Do not transfer ferric/copper-complex or O-acyl derivative MICs into the neutral
    record.
  - Keep biosynthetic enzyme activity separate from antibacterial target claims.
limitations:
- Review is bounded to the inspected original material, current authority exports
  and explicit local search; no global evidence absence is asserted.
- Optional absent schema fields are not treated as defects. No native, maintained
  source or previously saved review is edited.
- The1971 structure and analogue papers and1974 QSAR paper were read through full
  OCR; the1971 page126 structure/table was visually inspected. The1974 synthesis paper
  was read for its first two pages and assay-material scope.
- Original quantitative tables mainly concern metal complexes or derivatives. Free-ligand
  activity is described qualitatively, but exact independent MIC/speciation remains
  unresolved.
- The2021 main biosynthetic paper and actual Figure4 were inspected; its SI was inaccessible.
  Public CAS lookup does not certify an independently obtained proprietary registry
  graph.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Native curation status remains SEEDED. This review records evidence boundaries without
  changing the record.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
