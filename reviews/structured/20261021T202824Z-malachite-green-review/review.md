# Malachite green chloride: coherent exact structure with bounded salt-specific biological evidence

- Review: 20261021T202824Z-malachite-green-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T20:11:24Z
- Finished UTC: 2026-10-21T20:28:24Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The whole native record, all adopted bibliography leads and asserted groundings were inspected. Independent structure comparisons confirm the cation or chloride graph and its charge, composition and masses. Primary biological follow-up supports MG activity and QacR ligand recognition with explicit counterion, assay and mechanism boundaries; oxalate measurements are not transferred to the chloride. No confirmed native defect was found in this bounded review. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position629; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:72449 | data/antibiotics/antibacterial/malachite-green.yaml | generated | malachite green |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:72449 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:72449 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:72449 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:72449 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:72449 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:72449 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:72449 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:72449 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:72449 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:72449 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:72449 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:72449 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact cation or chloride graph

identity: supported. Targets: CHEBI:72449.

Full native structure and independent authorities agree on composition, charge, connectivity and cation/salt boundary. The salt record retains one chloride and must not be collapsed into the monocation. Synonyms were assessed in their explicit record context.

### Asserted mappings and their access limits

grounding: supported. Targets: CHEBI:72449.

Parsed chemical authorities corroborate the exact record. CAS and Reaxys were not independently inspectable; source mappings are retained as limited corroboration, not falsely reported as directly validated. Document references are topical chemical context, and the chloride patent is not activity evidence.

### Antibacterial/antifungal roles and preparation boundaries

evidence: supported. Targets: CHEBI:72449.

The broad source roles are consistent with primary MG antimicrobial observations. The cation is the shared active chemical component, but bulk salt, concentration and preparation remain experimental attributes. Explicit oxalate data and studies with unspecified counterion do not establish an exact chloride MIC. The native asserts no numerical activity object, so these evidence bounds are not themselves a false native claim.

### Ligand recognition, resistance regulation and downstream responses

evidence: unknown. Targets: CHEBI:72449.

QacR binding and qacA derepression concern efflux regulation; LspA-dependent permeability, Candida ROS/iron responses and expression/deletion phenotypes do not by themselves identify a direct lethal protein target. The native contains no target claim requiring removal.

### Complete native audit and bounded enrichment opportunities

completeness: unknown. Targets: CHEBI:72449.

All native fields, four history events, asserted groundings and ten adopted literature leads were covered. Optional activity, resistance, producer and causal graph fields are not required merely because relevant evidence exists. Exact material identity and endpoint support would be needed for future enrichment.

### Source fidelity and preserved input capture

provenance: supported. Targets: CHEBI:72449.

Original thirteen inputs and exact source row remain unchanged. Bibliography abstracts, fully read articles and peer-inspected selected passages are distinguished explicitly. No experimental status, chemical record or source was modified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/malachite-green.yaml; Entire record, all synonyms, xrefs and four history entries | supports | The native exact ChEBI record encodes an organic monocation plus one chloride, C23H25N2.Cl, net zero. All fields were read. There are no native molecular-target, resistance, activity-spectrum, producer, causal-graph or quoted-evidence objects. The absence of optional fields is not itself a defect. |
| source | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact ChEBI row and source-owned definition, bibliography, mappings and provenance | supports | The raw ChEBI row reproduces the native identity, role and chemical mappings. Ten adopted bibliography entries were individually followed. Original thirteen captured input hashes remain unchanged; no native status or history was edited. |
| local | /private/tmp/am-review-session/629-local-hits.txt; Captured local identity/source search | context_only | Local references were checked alongside the exact source row and entire native record; the bounded search includes ignored and hidden files and is not a claim that no other literature exists. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/72449/; Current ChEBI identity, structures, synonyms, roles and mappings | supports | Current ChEBI agrees with the native graph and its cation/salt distinction. Conventional dye names are interpreted in this explicit chemical context; matching labels alone are not the basis of identity. |
| chemistry | /private/tmp/am-review-session/628629-authority-chemistry.json; Independent RDKit parsing and reciprocal chirality-aware graph comparison | supports | Seventeen actual encodings were parsed across the two records: twelve cation representations (native SMILES/InChI, current ChEBI SMILES/InChI, PubChem SMILES/InChI and six CCD MGR descriptors) and five chloride representations (native/current ChEBI pairs and KEGG MOL). Each agrees within its exact chemical form. Cation key VFCNQNZNPKRXIT-UHFFFAOYSA-N and chloride key FDZZZRQASAIRJF-UHFFFAOYSA-M remain distinct; fragment counts are one and two. Formula, charge and mass checks pass. MGR CIF was retrieved but its atom graph was not separately parsed. |
| term-36094 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/36094/; Current asserted parent or role definition | supports | The source term was read and assessed in the exact native chemical context. The iminium/organic-chloride parent is structurally appropriate; antibacterial/antifungal role labels do not assert current regulatory approval or a specific lethal molecular target. |
| term-33282 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/; Current asserted parent or role definition | supports | The source term was read and assessed in the exact native chemical context. The iminium/organic-chloride parent is structurally appropriate; antibacterial/antifungal role labels do not assert current regulatory approval or a specific lethal molecular target. |
| term-86327 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/86327/; Current asserted parent or role definition | supports | The source term was read and assessed in the exact native chemical context. The iminium/organic-chloride parent is structurally appropriate; antibacterial/antifungal role labels do not assert current regulatory approval or a specific lethal molecular target. |
| kegg | https://rest.kegg.jp/get/C18367; Actual KEGG entry and MOL structure | supports | C18367 labels the chloride and its parsed two-fragment MOL matches native composition, charge and full graph. The cation is not silently substituted for its salt. |
| patent | https://patents.google.com/patent/WO2008063374A2/en; Abstract, comparative colorant 4 and selected claim 1; not all claims | context_only | The native document accession resolves through A2/A3; an attempted A1 route returned 404. Comparative Basic Green 4 has C23H25N2Cl and CI42000 and is a nonfugitive staining dye. Main claims concern alkyleneoxy derivatives. This is relevant chemical/document context, not an antimicrobial experiment or evidence of patent legal status. |
| access | /private/tmp/am-review-session/628630-fetch.json; Per-request public retrieval manifest and declared authority limits | context_only | CAS pages returned401 and Reaxys403; direct DrugBank returned403 for the cation. These access limits are not broken-identifier findings. Wikipedia was checked as topic-level document context, not as primary support for activity. Current ChEBI mappings and independently parsed structures supply bounded corroboration. |
| adopted-22236952 | PMID:22236952; Complete adopted original abstract; additional full-text depth stated separately | context_only | Lysozyme binding and host-protein toxicology, not an antibacterial molecular target. |
| adopted-22526306 | PMID:22526306; Complete adopted original abstract; additional full-text depth stated separately | context_only | Original mycobacterial oxalate study; main text and methods were additionally read in full below. |
| adopted-22623907 | PMID:22623907; Complete adopted original abstract; additional full-text depth stated separately | context_only | Bacterial consortium biodegradation, not exact-salt antimicrobial efficacy. |
| adopted-23122763 | PMID:23122763; Complete adopted original abstract; additional full-text depth stated separately | context_only | Molecularly imprinted extraction of dye from samples, not an organism susceptibility experiment. |
| adopted-23199816 | PMID:23199816; Complete adopted original abstract; additional full-text depth stated separately | context_only | Ultrasound/ozone degradation, not antibiotic target inhibition. |
| adopted-23203820 | PMID:23203820; Complete adopted original abstract; additional full-text depth stated separately | context_only | Nanosilver analytical detection, not standalone parent-compound antibacterial evidence. |
| adopted-23286983 | PMID:23286983; Complete adopted original abstract; additional full-text depth stated separately | context_only | Fish residue analysis of dyes and leuco forms, not primary antifungal efficacy. |
| adopted-23296502 | PMID:23296502; Complete adopted original abstract; additional full-text depth stated separately | context_only | Antarctic soil bacterial community adaptation and biodegradation; stress-enzyme associations do not establish a direct lethal target. |
| adopted-23323052 | PMID:23323052; Complete adopted original abstract; additional full-text depth stated separately | context_only | Glyoxal oxidase/manganese peroxidase decolorization, not fungicidal activity of parent MG. |
| adopted-25128680 | PMID:25128680; Complete adopted original abstract; additional full-text depth stated separately | context_only | Crab hemocyanin binding and host toxicology, not a microbial molecular target. |
| myco2012 | PMID:22526306; DOI:10.1128/AAC.00406-12; https://pmc.ncbi.nlm.nih.gov/articles/PMC3393420/; Full main article, all main methods/results and relevant numerical passages | partial | Material is explicitly Sigma malachite green OXALATE, 2.5mg/mL aqueous stock. M. smegmatis mc2 155 at37C has an approximate30 micrograms/mL MG MIC; plating at0.25 micrograms/mL after cell-wall-active antibiotics lowers recovered CFU100–1000fold. M. tuberculosis Erdman has roughly tenfold analogous effects for some pre-exposures; its ethambutol comparison is not statistically significant. Catalase and radical scavengers did not rescue the plating defect. These are preparation- and sequential-exposure-specific observations, not chloride MICs, clinical breakpoints or evidence for a particular direct lethal protein target. |
| myco2009 | PMID:19596883; DOI:10.1128/AAC.00647-09; https://pmc.ncbi.nlm.nih.gov/articles/PMC2737861/; Full main article, methods/results and Table1 | partial | M. tuberculosis H37Rv lspA-deficient material with inactive complementation has a104fold CFU defect on7H9 with1mg/L MG, rescued by active complementation. Increased decolorization and SDS sensitivity support a permeability interpretation. The main text does not resolve the MG salt. LspA genetic dependence is not direct MG binding to LspA, and background respiratory-chain discussion is not a newly demonstrated target. |
| qacr | PMID:21264225; DOI:10.1371/journal.pone.0015974; https://pmc.ncbi.nlm.nih.gov/articles/PMC3022030/; Independent peer: MG results, Tables1/2 and footnotes, all main methods/conclusion; Figures2C/3B viewed; root read complete peer report | partial | WT QacR binds MG with Kd1.23±0.14 micromolar (n3, intrinsic Trp fluorescence quenching,1MNaCl/20mMTris/5%glycerol,pH7.5). At1.25 micromolar MG, the qacA-promoter blaZ reporter increases3.6fold in S. aureus RN4220 norA::erm SAK1759. Mutant MG crystals are E90Q3BQZ/E120Q3BR0, both with K67S crystallization background and reductive alkylation. Salt, catalog and purity of supplied MG are unspecified. This supports cation ligand recognition and efflux derepression, not a demonstrated lethal mechanism; reported MIC data are not shown. |
| candida | PMID:22006003; DOI:10.1128/AAC.00574-11; https://pmc.ncbi.nlm.nih.gov/articles/PMC3256066/; Independent peer: abstract, material/strain/growth/susceptibility/ROS/iron/genetic methods, selected results/discussion and actual Figure1; root read complete report | partial | Sigma MG has no stated counterion, CAS or catalog. C. albicans CAI4 MIC50 is100ng/mL, explicitly50%growth suppression. Figure1A uses RPMI1640, nominal10^4cells/mL,30C/200rpm; CFU were read on Sabouraud after24h. The400ng/mL curve supports killing, while100/200 mainly suppress growth. ROS/iron assays, rescue and UPC2/STP2 hypersensitivity support downstream phenotypes rather than direct protein binding. These numerical results are not assigned specifically to chloride. |
| pdt | PMID:20690840; DOI:10.1089/pho.2009.2526; Independent peer: free author PDF abstract and methods ppS67–S69 only | context_only | The selected photodynamic study uses0.1% MG powder from Synth in saline with660nm irradiation. Its material paragraph confusingly calls MG4-dimethylaminophenol and supplies no salt identity. This unresolved material detail and illumination prevent direct parent-chloride susceptibility transfer; full results/figures were not read. |
| peer | /private/tmp/am-review-session/628629-peer-report.json; Complete independent report read by root | supports | Independent primary-source review corroborates MG-QacR ligand recognition and antifungal observations while preserving unknown counterions, assay endpoints, crystallization constructs and downstream-versus-binding distinctions. |
| adapter | /private/tmp/am-review-session/628630-adapter-results.json; Dataset catalog and SA staph_precise108 qacR probe | context_only | No protein or pathway object is asserted in the native record. The available structured catalog was inspected and a qacR query returned no genes or modules in the selected dataset; this dataset-specific empty result is not evidence that QacR does not exist. Primary follow-up was used for the newly encountered ligand association. |
| discovery | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=TITLE_ABS%3A%22malachite%20green%22%20AND%20%28antibacterial%20OR%20antimicrobial%20OR%20fung%2A%20OR%20mycobacter%2A%29; First100 titles from698-hit MG query and selected exact follow-up | context_only | All returned first100 titles were screened; many concern materials, degradation or detection rather than parent activity. Ten adopted leads and selected original mycobacterial, QacR and Candida studies were read at the explicitly recorded depth. This is a bounded discovery, not an exhaustive literature census. |

## Limits And Additional Notes

- CAS/Reaxys public access was restricted; direct DrugBank access was also restricted for the cation. Source mappings and independent structural corroboration do not substitute for unread authority content.
- The2012 mycobacterial preparation is oxalate. The2009 mycobacterial,2011 QacR and2012 Candida main articles do not resolve the supplied MG counterion; their values are not chloride-specific.
- Ten adopted original abstracts were read in full, but most underlying full articles were not. Two mycobacterial main articles were read fully; QacR/Candida primary selections and figures were inspected by an independent reviewer whose complete report was read by root. Their supplements and unselected details were not reviewed.
- The photodynamic paper was inspected only through its abstract and selected methods and has unresolved material nomenclature. The chloride patent was read selectively for document and chemical context, not as a comprehensive claim or legal-status review.
- Discovery screened the first100 of698 hits plus selected exact sources; it does not establish exhaustive literature coverage. Required shared corpus gates are incorporated separately, and their environment failures remain failures.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Review only; no native/source edits. No finding was manufactured from an optional empty field, a failed access attempt or an unmeasured salt-specific endpoint.
- Unpublished earlier bundle preserved unchanged in session scratch; final publication uses this newly saved observation after sequential-save and source-reference metadata correction. Scientific findings are unchanged.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T202824Z-malachite-green-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Malachite green chloride: coherent exact structure with bounded salt-specific
  biological evidence'
started_at: '2026-10-21T20:11:24Z'
finished_at: '2026-10-21T20:28:24Z'
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
summary: The whole native record, all adopted bibliography leads and asserted groundings
  were inspected. Independent structure comparisons confirm the cation or chloride
  graph and its charge, composition and masses. Primary biological follow-up supports
  MG activity and QacR ligand recognition with explicit counterion, assay and mechanism
  boundaries; oxalate measurements are not transferred to the chloride. No confirmed
  native defect was found in this bounded review. Scientific assessment retains the
  stated evidence limits; full verification is blocked by the shared native-library
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
  - path: data/antibiotics/antibacterial/malachite-green.yaml
    sha256: 1104f8aa9ccb7ad6b12dc29de28f599cc7a12233f17360825929692bb7cf0458
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
- target_id: CHEBI:72449
  path: data/antibiotics/antibacterial/malachite-green.yaml
  label: malachite green
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
  selection: Initially uncovered queue position629; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:72449
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:72449
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    629
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:72449
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/malachite-green.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:72449
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/malachite-green.yaml --out /private/tmp/am-review-session/629-strict.tsv
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
  - CHEBI:72449
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
  - CHEBI:72449
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
  - CHEBI:72449
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
  - CHEBI:72449
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
  - CHEBI:72449
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
  - CHEBI:72449
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
  - CHEBI:72449
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
  - CHEBI:72449
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
  - CHEBI:72449
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/malachite-green.yaml
  locator: Entire record, all synonyms, xrefs and four history entries
  accessed_at: '2026-10-21T20:27:14Z'
  support: supports
  summary: The native exact ChEBI record encodes an organic monocation plus one chloride,
    C23H25N2.Cl, net zero. All fields were read. There are no native molecular-target,
    resistance, activity-spectrum, producer, causal-graph or quoted-evidence objects.
    The absence of optional fields is not itself a defect.
  snapshot_sha256: 1104f8aa9ccb7ad6b12dc29de28f599cc7a12233f17360825929692bb7cf0458
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Exact ChEBI row and source-owned definition, bibliography, mappings and
    provenance
  accessed_at: '2026-10-21T20:27:14Z'
  support: supports
  summary: The raw ChEBI row reproduces the native identity, role and chemical mappings.
    Ten adopted bibliography entries were individually followed. Original thirteen
    captured input hashes remain unchanged; no native status or history was edited.
  snapshot_sha256: 77ea45535dc33833f7318bff802835454cfa1d09c33c629187b44b30389c0032
- evidence_id: local
  kind: search
  reference: /private/tmp/am-review-session/629-local-hits.txt
  locator: Captured local identity/source search
  accessed_at: '2026-10-21T20:27:14Z'
  support: context_only
  summary: Local references were checked alongside the exact source row and entire
    native record; the bounded search includes ignored and hidden files and is not
    a claim that no other literature exists.
  search_scope: Initial rg --no-ignore --hidden exact identity/name/identifier search
    across repository source and curation context; native and source row read in full.
  snapshot_sha256: c539eb141d6383035b701c8c2afcc0c6c27b8740669d71fd5d82c87d1446a127
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/72449/
  locator: Current ChEBI identity, structures, synonyms, roles and mappings
  accessed_at: '2026-10-21T20:17:18Z'
  support: supports
  summary: Current ChEBI agrees with the native graph and its cation/salt distinction.
    Conventional dye names are interpreted in this explicit chemical context; matching
    labels alone are not the basis of identity.
  snapshot_sha256: ec1e61b12bc34172caddd01e85b0aee6ca27404dfd2864ecc1fe8bbe3ef0969b
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/am-review-session/628629-authority-chemistry.json
  locator: Independent RDKit parsing and reciprocal chirality-aware graph comparison
  accessed_at: '2026-10-21T20:27:14Z'
  support: supports
  summary: 'Seventeen actual encodings were parsed across the two records: twelve
    cation representations (native SMILES/InChI, current ChEBI SMILES/InChI, PubChem
    SMILES/InChI and six CCD MGR descriptors) and five chloride representations (native/current
    ChEBI pairs and KEGG MOL). Each agrees within its exact chemical form. Cation
    key VFCNQNZNPKRXIT-UHFFFAOYSA-N and chloride key FDZZZRQASAIRJF-UHFFFAOYSA-M remain
    distinct; fragment counts are one and two. Formula, charge and mass checks pass.
    MGR CIF was retrieved but its atom graph was not separately parsed.'
  snapshot_sha256: fe43f8f8a59ecb84a0dd82d11826afa2462c60b0b7df07c1e267e82a6a700d7a
- evidence_id: term-36094
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/36094/
  locator: Current asserted parent or role definition
  accessed_at: '2026-10-21T20:17:20Z'
  support: supports
  summary: The source term was read and assessed in the exact native chemical context.
    The iminium/organic-chloride parent is structurally appropriate; antibacterial/antifungal
    role labels do not assert current regulatory approval or a specific lethal molecular
    target.
  snapshot_sha256: 8f107a1c2c27c26f593ee57fb1760556728159a76f7deb7078f791212a24ea65
- evidence_id: term-33282
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/
  locator: Current asserted parent or role definition
  accessed_at: '2026-10-21T20:17:20Z'
  support: supports
  summary: The source term was read and assessed in the exact native chemical context.
    The iminium/organic-chloride parent is structurally appropriate; antibacterial/antifungal
    role labels do not assert current regulatory approval or a specific lethal molecular
    target.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: term-86327
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/86327/
  locator: Current asserted parent or role definition
  accessed_at: '2026-10-21T20:17:20Z'
  support: supports
  summary: The source term was read and assessed in the exact native chemical context.
    The iminium/organic-chloride parent is structurally appropriate; antibacterial/antifungal
    role labels do not assert current regulatory approval or a specific lethal molecular
    target.
  snapshot_sha256: be8a0222643379046d4af450729b5798e84197fba2492db90bc767648adf483a
- evidence_id: kegg
  kind: authority
  reference: https://rest.kegg.jp/get/C18367
  locator: Actual KEGG entry and MOL structure
  accessed_at: '2026-10-21T20:17:21Z'
  support: supports
  summary: C18367 labels the chloride and its parsed two-fragment MOL matches native
    composition, charge and full graph. The cation is not silently substituted for
    its salt.
  snapshot_sha256: ab315c84b6faa2c12321003582dcc69ea8cc6a088c0f3633378dce9ec70b08b8
- evidence_id: patent
  kind: primary_source
  reference: https://patents.google.com/patent/WO2008063374A2/en
  locator: Abstract, comparative colorant 4 and selected claim 1; not all claims
  accessed_at: '2026-10-21T20:17:43Z'
  support: context_only
  summary: The native document accession resolves through A2/A3; an attempted A1 route
    returned 404. Comparative Basic Green 4 has C23H25N2Cl and CI42000 and is a nonfugitive
    staining dye. Main claims concern alkyleneoxy derivatives. This is relevant chemical/document
    context, not an antimicrobial experiment or evidence of patent legal status.
  snapshot_sha256: bb2d441fcefce80cfefb39dd3fbb3e1b8f689e5d2c0d9bffa2c37fcd889b7407
- evidence_id: access
  kind: search
  reference: /private/tmp/am-review-session/628630-fetch.json
  locator: Per-request public retrieval manifest and declared authority limits
  accessed_at: '2026-10-21T20:27:14Z'
  support: context_only
  summary: CAS pages returned401 and Reaxys403; direct DrugBank returned403 for the
    cation. These access limits are not broken-identifier findings. Wikipedia was
    checked as topic-level document context, not as primary support for activity.
    Current ChEBI mappings and independently parsed structures supply bounded corroboration.
  search_scope: Exact asserted ChEBI, CAS, Reaxys, CCD/DrugBank or KEGG and document
    identifiers; current public endpoints with response status and content hashes.
    No paid providers.
  snapshot_sha256: 36ef89b7f8ac60a7c3f11e798ebfe723dc44939344c1b1038bfe347b4acd9cf6
- evidence_id: adopted-22236952
  kind: primary_source
  reference: PMID:22236952
  locator: Complete adopted original abstract; additional full-text depth stated separately
  accessed_at: '2026-10-21T20:17:18Z'
  support: context_only
  summary: Lysozyme binding and host-protein toxicology, not an antibacterial molecular
    target.
  snapshot_sha256: 03c853045daea44ee82c475003514fedfcaed27a834e73aab4c0e79b1577ba30
- evidence_id: adopted-22526306
  kind: primary_source
  reference: PMID:22526306
  locator: Complete adopted original abstract; additional full-text depth stated separately
  accessed_at: '2026-10-21T20:17:18Z'
  support: context_only
  summary: Original mycobacterial oxalate study; main text and methods were additionally
    read in full below.
  snapshot_sha256: 4b8db76c03e7d5a7d81c8c5a93ddd429080702cb707258c473e37978085cf5e1
- evidence_id: adopted-22623907
  kind: primary_source
  reference: PMID:22623907
  locator: Complete adopted original abstract; additional full-text depth stated separately
  accessed_at: '2026-10-21T20:17:18Z'
  support: context_only
  summary: Bacterial consortium biodegradation, not exact-salt antimicrobial efficacy.
  snapshot_sha256: 9ce952f9b60188a95746fe8f9ee92c4ad1dda2cb9d347a7eb0c5c12f59bc8ba8
- evidence_id: adopted-23122763
  kind: primary_source
  reference: PMID:23122763
  locator: Complete adopted original abstract; additional full-text depth stated separately
  accessed_at: '2026-10-21T20:17:18Z'
  support: context_only
  summary: Molecularly imprinted extraction of dye from samples, not an organism susceptibility
    experiment.
  snapshot_sha256: f5f743cf0278dabd4592861ac4f388c8e32021e18f1d3edd0343355514bce534
- evidence_id: adopted-23199816
  kind: primary_source
  reference: PMID:23199816
  locator: Complete adopted original abstract; additional full-text depth stated separately
  accessed_at: '2026-10-21T20:17:19Z'
  support: context_only
  summary: Ultrasound/ozone degradation, not antibiotic target inhibition.
  snapshot_sha256: cfa35233f11545a97cf8debd354c9e278f183b4ff00c69abc30448c3792c1211
- evidence_id: adopted-23203820
  kind: primary_source
  reference: PMID:23203820
  locator: Complete adopted original abstract; additional full-text depth stated separately
  accessed_at: '2026-10-21T20:17:19Z'
  support: context_only
  summary: Nanosilver analytical detection, not standalone parent-compound antibacterial
    evidence.
  snapshot_sha256: 69d28b67f8a9805c089eefec882e5b0794e3a14deefddbfa2f2086b9554e62ae
- evidence_id: adopted-23286983
  kind: primary_source
  reference: PMID:23286983
  locator: Complete adopted original abstract; additional full-text depth stated separately
  accessed_at: '2026-10-21T20:17:19Z'
  support: context_only
  summary: Fish residue analysis of dyes and leuco forms, not primary antifungal efficacy.
  snapshot_sha256: 844f1cb1d4a0bd950640263495158f1983c754f83d18fd15a17a87a7bf7255cf
- evidence_id: adopted-23296502
  kind: primary_source
  reference: PMID:23296502
  locator: Complete adopted original abstract; additional full-text depth stated separately
  accessed_at: '2026-10-21T20:17:19Z'
  support: context_only
  summary: Antarctic soil bacterial community adaptation and biodegradation; stress-enzyme
    associations do not establish a direct lethal target.
  snapshot_sha256: ac54db797d2d8a0bd46156ce9cb2269ffe61f2f9f6e6269d345660725b8cc83a
- evidence_id: adopted-23323052
  kind: primary_source
  reference: PMID:23323052
  locator: Complete adopted original abstract; additional full-text depth stated separately
  accessed_at: '2026-10-21T20:17:19Z'
  support: context_only
  summary: Glyoxal oxidase/manganese peroxidase decolorization, not fungicidal activity
    of parent MG.
  snapshot_sha256: 57cf8ac279d8fe117a6690d49a40c7b1f37360e289fe63b8137969461802465e
- evidence_id: adopted-25128680
  kind: primary_source
  reference: PMID:25128680
  locator: Complete adopted original abstract; additional full-text depth stated separately
  accessed_at: '2026-10-21T20:17:19Z'
  support: context_only
  summary: Crab hemocyanin binding and host toxicology, not a microbial molecular
    target.
  snapshot_sha256: e743ca4aee1531cabb8c0b5943d6a767753cbd772d2625b7ede9c4b7b80f77ba
- evidence_id: myco2012
  kind: primary_source
  reference: PMID:22526306; DOI:10.1128/AAC.00406-12; https://pmc.ncbi.nlm.nih.gov/articles/PMC3393420/
  locator: Full main article, all main methods/results and relevant numerical passages
  accessed_at: '2026-10-21T20:17:43Z'
  support: partial
  summary: Material is explicitly Sigma malachite green OXALATE, 2.5mg/mL aqueous
    stock. M. smegmatis mc2 155 at37C has an approximate30 micrograms/mL MG MIC; plating
    at0.25 micrograms/mL after cell-wall-active antibiotics lowers recovered CFU100–1000fold.
    M. tuberculosis Erdman has roughly tenfold analogous effects for some pre-exposures;
    its ethambutol comparison is not statistically significant. Catalase and radical
    scavengers did not rescue the plating defect. These are preparation- and sequential-exposure-specific
    observations, not chloride MICs, clinical breakpoints or evidence for a particular
    direct lethal protein target.
  snapshot_sha256: 61e8cc2b823dc4a86c3cf08353ad1df7414f267ac33a087eff6c804866804034
- evidence_id: myco2009
  kind: primary_source
  reference: PMID:19596883; DOI:10.1128/AAC.00647-09; https://pmc.ncbi.nlm.nih.gov/articles/PMC2737861/
  locator: Full main article, methods/results and Table1
  accessed_at: '2026-10-21T20:17:43Z'
  support: partial
  summary: M. tuberculosis H37Rv lspA-deficient material with inactive complementation
    has a104fold CFU defect on7H9 with1mg/L MG, rescued by active complementation.
    Increased decolorization and SDS sensitivity support a permeability interpretation.
    The main text does not resolve the MG salt. LspA genetic dependence is not direct
    MG binding to LspA, and background respiratory-chain discussion is not a newly
    demonstrated target.
  snapshot_sha256: aced8dcb06e3faadb28e271a36a008f51300d6f206c30b5b359676284ce4e0a4
- evidence_id: qacr
  kind: primary_source
  reference: PMID:21264225; DOI:10.1371/journal.pone.0015974; https://pmc.ncbi.nlm.nih.gov/articles/PMC3022030/
  locator: 'Independent peer: MG results, Tables1/2 and footnotes, all main methods/conclusion;
    Figures2C/3B viewed; root read complete peer report'
  accessed_at: '2026-10-21T20:21:41Z'
  support: partial
  summary: WT QacR binds MG with Kd1.23±0.14 micromolar (n3, intrinsic Trp fluorescence
    quenching,1MNaCl/20mMTris/5%glycerol,pH7.5). At1.25 micromolar MG, the qacA-promoter
    blaZ reporter increases3.6fold in S. aureus RN4220 norA::erm SAK1759. Mutant MG
    crystals are E90Q3BQZ/E120Q3BR0, both with K67S crystallization background and
    reductive alkylation. Salt, catalog and purity of supplied MG are unspecified.
    This supports cation ligand recognition and efflux derepression, not a demonstrated
    lethal mechanism; reported MIC data are not shown.
  snapshot_sha256: b497c378c2aa46faa761c19d96cd1c220fd37a982b35d6d7cd9c384fabcf22c7
- evidence_id: candida
  kind: primary_source
  reference: PMID:22006003; DOI:10.1128/AAC.00574-11; https://pmc.ncbi.nlm.nih.gov/articles/PMC3256066/
  locator: 'Independent peer: abstract, material/strain/growth/susceptibility/ROS/iron/genetic
    methods, selected results/discussion and actual Figure1; root read complete report'
  accessed_at: '2026-10-21T20:21:41Z'
  support: partial
  summary: Sigma MG has no stated counterion, CAS or catalog. C. albicans CAI4 MIC50
    is100ng/mL, explicitly50%growth suppression. Figure1A uses RPMI1640, nominal10^4cells/mL,30C/200rpm;
    CFU were read on Sabouraud after24h. The400ng/mL curve supports killing, while100/200
    mainly suppress growth. ROS/iron assays, rescue and UPC2/STP2 hypersensitivity
    support downstream phenotypes rather than direct protein binding. These numerical
    results are not assigned specifically to chloride.
  snapshot_sha256: 9b1d2dc29b6a9edce3c4200d9af65e26a60333e01c849135e41132c5b987fa12
- evidence_id: pdt
  kind: primary_source
  reference: PMID:20690840; DOI:10.1089/pho.2009.2526
  locator: 'Independent peer: free author PDF abstract and methods ppS67–S69 only'
  accessed_at: '2026-10-21T20:21:41Z'
  support: context_only
  summary: The selected photodynamic study uses0.1% MG powder from Synth in saline
    with660nm irradiation. Its material paragraph confusingly calls MG4-dimethylaminophenol
    and supplies no salt identity. This unresolved material detail and illumination
    prevent direct parent-chloride susceptibility transfer; full results/figures were
    not read.
  snapshot_sha256: 66725074089e46adba3cba31c9882f41978e8350c638478a7557a1894690f05e
- evidence_id: peer
  kind: validation
  reference: /private/tmp/am-review-session/628629-peer-report.json
  locator: Complete independent report read by root
  accessed_at: '2026-10-21T20:27:14Z'
  support: supports
  summary: Independent primary-source review corroborates MG-QacR ligand recognition
    and antifungal observations while preserving unknown counterions, assay endpoints,
    crystallization constructs and downstream-versus-binding distinctions.
  snapshot_sha256: 86bd9f2b3ff3b54efa2a8971f0e336073ccf6a33714631311794dcb3269f01ba
- evidence_id: adapter
  kind: search
  reference: /private/tmp/am-review-session/628630-adapter-results.json
  locator: Dataset catalog and SA staph_precise108 qacR probe
  accessed_at: '2026-10-21T20:27:14Z'
  support: context_only
  summary: No protein or pathway object is asserted in the native record. The available
    structured catalog was inspected and a qacR query returned no genes or modules
    in the selected dataset; this dataset-specific empty result is not evidence that
    QacR does not exist. Primary follow-up was used for the newly encountered ligand
    association.
  search_scope: Available structured dataset catalog and one qacR probe in SA staph_precise108,
    with raw output retained; not an organism-wide absence search.
  snapshot_sha256: 70c1925cc83f1c744662de888f08ff39185334fbecd4194c521266438ba66422
- evidence_id: discovery
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=TITLE_ABS%3A%22malachite%20green%22%20AND%20%28antibacterial%20OR%20antimicrobial%20OR%20fung%2A%20OR%20mycobacter%2A%29
  locator: First100 titles from698-hit MG query and selected exact follow-up
  accessed_at: '2026-10-21T20:17:18Z'
  support: context_only
  summary: All returned first100 titles were screened; many concern materials, degradation
    or detection rather than parent activity. Ten adopted leads and selected original
    mycobacterial, QacR and Candida studies were read at the explicitly recorded depth.
    This is a bounded discovery, not an exhaustive literature census.
  search_scope: TITLE_ABS:"malachite green" AND (antibacterial OR antimicrobial OR
    fung* OR mycobacter*), first100 returned titles; exact original identifiers and
    independent peer selected follow-up.
  snapshot_sha256: 8ff7008fb9340f02630ad1592823afd6e105ed8d0c005a12c89860a5b2c76aa1
assessments:
- assessment_id: identity
  area: identity
  topic: Exact cation or chloride graph
  outcome: supported
  summary: Full native structure and independent authorities agree on composition,
    charge, connectivity and cation/salt boundary. The salt record retains one chloride
    and must not be collapsed into the monocation. Synonyms were assessed in their
    explicit record context.
  target_ids:
  - CHEBI:72449
  evidence_ids:
  - native
  - source
  - chebi
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Asserted mappings and their access limits
  outcome: supported
  summary: Parsed chemical authorities corroborate the exact record. CAS and Reaxys
    were not independently inspectable; source mappings are retained as limited corroboration,
    not falsely reported as directly validated. Document references are topical chemical
    context, and the chloride patent is not activity evidence.
  target_ids:
  - CHEBI:72449
  evidence_ids:
  - chebi
  - chemistry
  - access
  - kegg
- assessment_id: activity
  area: evidence
  topic: Antibacterial/antifungal roles and preparation boundaries
  outcome: supported
  summary: The broad source roles are consistent with primary MG antimicrobial observations.
    The cation is the shared active chemical component, but bulk salt, concentration
    and preparation remain experimental attributes. Explicit oxalate data and studies
    with unspecified counterion do not establish an exact chloride MIC. The native
    asserts no numerical activity object, so these evidence bounds are not themselves
    a false native claim.
  target_ids:
  - CHEBI:72449
  evidence_ids:
  - native
  - chebi
  - myco2012
  - myco2009
  - candida
- assessment_id: mechanism
  area: evidence
  topic: Ligand recognition, resistance regulation and downstream responses
  outcome: unknown
  summary: QacR binding and qacA derepression concern efflux regulation; LspA-dependent
    permeability, Candida ROS/iron responses and expression/deletion phenotypes do
    not by themselves identify a direct lethal protein target. The native contains
    no target claim requiring removal.
  target_ids:
  - CHEBI:72449
  evidence_ids:
  - native
  - qacr
  - myco2009
  - candida
  - adapter
- assessment_id: completeness
  area: completeness
  topic: Complete native audit and bounded enrichment opportunities
  outcome: unknown
  summary: All native fields, four history events, asserted groundings and ten adopted
    literature leads were covered. Optional activity, resistance, producer and causal
    graph fields are not required merely because relevant evidence exists. Exact material
    identity and endpoint support would be needed for future enrichment.
  target_ids:
  - CHEBI:72449
  evidence_ids:
  - native
  - source
  - discovery
  - peer
- assessment_id: provenance
  area: provenance
  topic: Source fidelity and preserved input capture
  outcome: supported
  summary: Original thirteen inputs and exact source row remain unchanged. Bibliography
    abstracts, fully read articles and peer-inspected selected passages are distinguished
    explicitly. No experimental status, chemical record or source was modified.
  target_ids:
  - CHEBI:72449
  evidence_ids:
  - native
  - source
  - local
findings: []
actions: []
limitations:
- CAS/Reaxys public access was restricted; direct DrugBank access was also restricted
  for the cation. Source mappings and independent structural corroboration do not
  substitute for unread authority content.
- The2012 mycobacterial preparation is oxalate. The2009 mycobacterial,2011 QacR and2012
  Candida main articles do not resolve the supplied MG counterion; their values are
  not chloride-specific.
- Ten adopted original abstracts were read in full, but most underlying full articles
  were not. Two mycobacterial main articles were read fully; QacR/Candida primary
  selections and figures were inspected by an independent reviewer whose complete
  report was read by root. Their supplements and unselected details were not reviewed.
- The photodynamic paper was inspected only through its abstract and selected methods
  and has unresolved material nomenclature. The chloride patent was read selectively
  for document and chemical context, not as a comprehensive claim or legal-status
  review.
- Discovery screened the first100 of698 hits plus selected exact sources; it does
  not establish exhaustive literature coverage. Required shared corpus gates are incorporated
  separately, and their environment failures remain failures.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Review only; no native/source edits. No finding was manufactured from an optional
  empty field, a failed access attempt or an unmeasured salt-specific endpoint.
- Unpublished earlier bundle preserved unchanged in session scratch; final publication
  uses this newly saved observation after sequential-save and source-reference metadata
  correction. Scientific findings are unchanged.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
