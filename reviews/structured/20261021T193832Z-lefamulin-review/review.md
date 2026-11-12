# Lefamulin: supported exact references with bounded assay and naming scope

- Review: 20261021T193832Z-lefamulin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:16:38Z
- Finished UTC: 2026-10-21T19:38:32Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No confirmed native defect was found. All asserted exact chemical references reproduce the neutral eleven-centre lefamulin graph, and the deposited ligand in the cited primary ribosome structure agrees. Original structural, translation and multidrug-resistant pneumococcal studies support the definition and antibacterial class. A broader current PubChem name result and unspecified experimental bulk form limit automatic identity and quantitative transfers; optional target and activity gaps are not defects. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 597; one whole native record. All thirteen initial input hashes were verified unchanged before assessment. Actual ARO/PubChem inventory and enrichment owners were appended, giving sixteen captured inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-f8f4257b4b | data/antibiotics/antibacterial/lefamulin.yaml | generated | lefamulin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | antibioticmech:aro-f8f4257b4b | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-f8f4257b4b | Actual focused execution exited 0. |
| Focused chemistry verification | passed | False | antibioticmech:aro-f8f4257b4b | Actual focused execution exited 0. |
| Independent chemical reference comparison | passed | False | antibioticmech:aro-f8f4257b4b | Native, adopted/current exact PubChem, ChEMBL SMILES/InChI/molfile, current ChEBI and CCD62B serializations reproduce the same full key. A separate PubChem name result leaves one centre unspecified; clearing only native canonical C16 reproduces that broader key. |
| Authoritative full QC | failed | True | antibioticmech:aro-f8f4257b4b | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-f8f4257b4b | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-f8f4257b4b | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-f8f4257b4b | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-f8f4257b4b | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-f8f4257b4b | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-f8f4257b4b | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-f8f4257b4b | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-f8f4257b4b | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral structure and stereochemical scope

identity: supported. Targets: antibioticmech:aro-f8f4257b4b.

All native exact references and the deposited primary ligand match the fully assigned neutral graph. The separate current name result has one unspecified centre and does not establish an opposite structure. The official acetate formulation remains chemically distinct.

### Exact xrefs, broader class and mint

grounding: supported. Targets: antibioticmech:aro-f8f4257b4b.

ARO, ChEMBL and PubChem exact assertions agree. The pleuromutilin class is broader than the semisynthetic derivative. A current nonadopted two-star ChEBI entry is corroboration, not automatic invalidation of the historical mint.

### Semisynthesis and resistant-pathogen activity

evidence: supported. Targets: antibioticmech:aro-f8f4257b4b.

The definition closely matches the adopted 2016 primary introduction and is supported by the original MDR pneumococcal collection. It does not explicitly assert all pathogens are susceptible. A more specific description could help future curation, but optional wording precision is not a confirmed defect. The nearest emitted citation is correctly recognized here as a review.

### Ribosome binding and translation inhibition

evidence: supported. Targets: antibioticmech:aro-f8f4257b4b.

Exact lefamulin binding to the S. aureus PTC and coupled reporter-expression inhibition are directly supported. The A/P-site distinction and structural selectivity rationale are preserved. The native record makes no incorrect direct-protein or single-step kinetic claim.

### Source ownership and history

provenance: supported. Targets: antibioticmech:aro-f8f4257b4b.

The complete native record and maintained rows were read. Both adopted citations were dispositioned and source dates/mint/history reproduce. All original hashes remain unchanged and actual owners are included.

### Optional biological enrichment and access boundaries

completeness: supported. Targets: antibioticmech:aro-f8f4257b4b.

Every asserted field and exact chemical reference was examined. Primary activity and molecular mode were checked even though those optional structured objects are not present. No missing optional field was counted as a defect; clinical product data were kept separate.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Keep any optional mechanism and activity enrichment tied to the exact experiment.

- Use the S. aureus 23S-rRNA/PTC binding context, distinguish the A-site core from the P-site extension and keep structural selectivity rationale separate from direct host assays.
- Treat the 0.02 µg/mL endpoint as coupled reporter-expression IC50. Preserve or resolve the inconsistent concentration conversions before copying detailed dose ranges.
- Keep pneumococcal MDR collection statistics and their definition distinct from individual-strain MICs or a universal resistance claim. Do not assume the unspecified bulk material was the neutral solid or a particular salt.

### A2

Preserve exact-accession identity when consulting name-based authorities.

- Do not replace the eleven-centre native graph with the ten-assigned-centre PubChem name result without an explicit evidence-backed scope decision.
- Retain the free-compound versus acetate distinction and historical minted provenance. A current two-star ChEBI record alone is not a mandate to alter the adopted inventory.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/lefamulin.yaml; Complete native YAML: identifier, definition/source, class/parent, all chemical properties, three exact references, source concept and three history events. | supports | The SEEDED MINTED record denotes neutral C28H45NO5S with key KPVIXBKIJXZQJX-FCEONZPQSA-N and eleven assigned tetrahedral centres. Its only biological description is a semisynthetic pleuromutilin with activity against multiresistant pathogens. No direct target, MIC, resistance, clinical, producer, dataset or causal-graph object is asserted. |
| owners | data/raw/aro_antibiotics.tsv:324; data/raw/pubchem_structures.tsv:110; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py; Complete exact source rows and applicable source extraction, structure fallback and reference/class/definition seeding branches. | supports | ARO3004088 supplies the definition, class and citation leads PMID32493034 and 27958389. The first is emitted as definition_source. PubChem25185057 supplies native chemistry. No adopted ChEBI row supplies this record; the mint is reproducible. Actual owners were appended while preserving all thirteen original hashes. |
| local-search | /private/tmp/am-review-session/597-local-hits.txt; Complete returned path inventory from ignored-inclusive and hidden-inclusive identifier/label/slug search. | context_only | Matches include native/raw/generated files and historical research ledgers. Those ledgers were not scientific evidence. Exact maintained rows and the complete native record determine the scope of present claims and optional objects. |
| aro | https://purl.obolibrary.org/obo/aro.obo; Current ARO3004088 and parent/class ARO3000670, fully read. | supports | The current exact compound term reproduces the native definition and both citations, with the same ChEMBL and PubChem links. ARO3000670 is the broader pleuromutilin class. Its generic natural-product and P-site prose is not an assertion that this semisynthetic exact compound was produced by a fungus or binds only one ribosomal site. |
| exact-chemistry | PubChem:25185057; ChEMBL:CHEMBL3291398; Complete current structure responses and independent parsing of SMILES, InChI and ChEMBL molfile. | supports | Both native exact chemical accessions reproduce FCEONZPQSA-N, formula C28H45NO5S and all eleven assigned centres. Native masses and neutral charge are consistent at source precision. ChEMBL clinical annotations were not treated as native clinical assertions or exact product identity. |
| current-chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/755252/; Complete current two-star entry and both structural strings. | supports | Current ChEBI matches the exact native graph and antibacterial role. It is not an adopted source row and does not invalidate the historical minted rationale. Its newer citation list is not silently substituted for the record adopted leads. |
| name-scope | PubChem:58076382; PubChem:25185057; Current preferred-name query compared with the actual native exact accession. | context_only | The name lefamulin currently resolves to CID58076382, with key KPVIXBKIJXZQJX-CSOZIWFHSA-N and canonical InChI C16 unspecified. All other centres agree with the native exact graph. CID25185057 remains the valid fully assigned accession used by this record. An annotation move or broader name hit does not by itself prove the exact native graph wrong or establish a mixture. |
| diagnostic | /private/tmp/am-review-session/597-authority-chemistry.json; Independent graph and stereo-scope calculations. | supports | Twelve native/exact-authority serializations, including CCD and current ChEBI, match the fully assigned native key. Clearing only canonical InChI C16 from the native graph reproduces the separate preferred-name result. That is a scope diagnostic rather than evidence for an opposite stereoisomer or an authorized structure change. |
| primary-structure | PMID:27958389; DOI:10.1038/srep39004; PMC5154188; Full original main text, all figure captions and crystallographic Table 1 read; Figures 1 and 3 viewed. | supports | The 2016 original describes semisynthetic lefamulin and determines its S. aureus RN4220 large-subunit complex at 3.55Å. Figure 1 shows the mutilin-derived skeleton; the cyclohexyl sidechain drawing is not itself a complete absolute-stereo proof. The paper supports binding at the peptidyl-transferase centre, with the core occupying the A-site region and the extension directed toward the P-site. Structural modelling supports the ligand pose; no new independent absolute-hand determination is claimed. |
| deposition | PDB:5HL7; pdb-ccd:62B; Official RCSB entry/nonpolymer entity 31 and complete PDBe CCD response. | supports | The deposited entry cites PMID27958389 and identifies entity 31 as lefamulin 62B. Both CCD isomeric SMILES and its InChI reproduce all eleven native assignments. The ligand is modelled without an acetate counterion. This corroborates the deposited chemical identity but is not proof of the exact bulk reagent salt or independent re-refinement of the diffraction data. |
| primary-function | PMID:27958389; DOI:10.1038/srep39004; Original Figure 3 and coupled transcription/translation Methods. | supports | The cell-free assay uses S. aureus ribosomes with ribosome-free E. coli extract and a luciferase reporter. Figure 3 and Results report lefamulin IC50 0.02 µg/mL, versus 0.08 for BC3205 and 0.10 for tiamulin. This is reporter-expression inhibition, not Kd or an isolated chemical-step rate. The Methods concentration endpoints have inconsistent molar/mass conversions, so numerical enrichment should preserve the source ambiguity rather than silently repair it. |
| primary-selectivity | PMID:27958389; DOI:10.1038/srep39004; Original selectivity Results, Figure 4 caption and Discussion. | context_only | The authors compare bacterial, archaeal and eukaryotic ribosome structures and propose how local nucleotide conformations stabilize the bacterial binding pocket. The exact lefamulin experiment is the S. aureus complex and cell-free assay; the cross-kingdom structural rationale is not an experimental demonstration of absence of every host interaction. Optional target curation should retain that distinction. |
| primary-mdr | PMID:27161634; DOI:10.1128/AAC.00627-16; PMC4914675; Full original main article and all three tables read; supplemental comparator-breakpoint table not inspected. | supports | Broth microdilution tested 822 S. pneumoniae isolates from 58 US hospitals in 2010, using dry-form Thermo Fisher panels. MDR was defined by elevated MICs to at least three specified drug classes; 180 isolates met that definition. Lefamulin MIC50/MIC90 were 0.12/0.25 µg/mL in both the whole collection and MDR subset. These are collection statistics, not a universal claim about all multiresistant pathogens. Bulk salt/purity is not specified in the inspected article. |
| adopted-review | PMID:32493034; DOI:10.1177/1060028020932521; Complete original review abstract read; review full text not obtained. | context_only | This is a 2020 pharmacology/microbiology/clinical review, not a new primary experiment. It supports the broad drug-class and activity context but its trial summaries are not used as direct primary efficacy or molecular-binding proof. The second adopted citation and independently read original MDR study supply direct experimental support for the native description. |
| official-salt | https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/211672s000%2C211673s000lbl.pdf; Original 2019 label section 11, printed page 12, text and structure viewed. | supports | The official description identifies semisynthetic lefamulin with a 1R,2R,4R amino-hydroxycyclohexyl sidechain, supplied as acetate C30H49NO7S. It explicitly distinguishes acetate mass from equivalent lefamulin mass. The neutral native graph has no acetate component. No product identity, present marketing status or clinical approval assertion is added to this record. |
| additional-primary-leads | PMID:28893785; PMID:29530863; PMID:27855075; Complete original abstracts read; full papers not inspected in this bounded review. | context_only | These exact lefamulin studies report activity against resistant gonococci, selected sexually transmitted pathogens and macrolide-resistant M. pneumoniae. They corroborate that resistant-pathogen activity is not based solely on a chemical family inference. Their detailed efflux mechanisms, bactericidal endpoints and assay numbers were not transferred without full experimental scope. |
| bounded-search | Europe PMC exact lefamulin and resistance/structure/ribosome search,2010-2018, executed2026-10-21; All seventeen result titles inspected; adopted abstracts and selected relevant primary abstracts read; two decisive originals obtained in full. | context_only | The search also returned secondary reviews, conference abstracts and derivative studies, which were not promoted to exact-parent experimental evidence. Official structure/label follow-up and a separate current PubChem name query resolved identity scope. No global absence claim is made. |
| adapter-scope | Structured-source applicability to the native record; Native inventory before open-ended protein mechanism research. | context_only | The native record has no gene, locus, exact protein target, pathway, stress response or transcriptomic dataset. Its chemical class alone does not require a matched iModulon query. The original rRNA complex and cell-free experiments were assessed directly; no expression-module result was needed or inferred. |

## Limits And Additional Notes

- The 2016 ribosome original was read in full with all captions and Table 1; Figures 1 and 3 were viewed. Coordinates/diffraction data were not re-refined. The crystal model corroborates ligand identity but does not independently establish every absolute centre or bulk formulation.
- The 2016 MDR pneumococcal main text and all three tables were read; the supplemental comparator-breakpoint table was not. Exact bulk salt, purity and mass normalization were not specified in the inspected text.
- The coupled-assay Methods has inconsistent molar/mass endpoint conversions; the reported 0.02 µg/mL IC50 agrees between Figure 3 and Results. This source limitation does not contradict any native numerical claim, because none is present.
- The adopted 2020 review was read at complete-abstract depth only. Three additional exact-parent activity abstracts were inspected, but no detailed assay or efflux data were transferred from them.
- The current PubChem preferred-name result leaves canonical C16 unspecified, whereas the actual native exact accession, ChEMBL, ChEBI and CCD agree on all eleven assigned centres. This is retained as a naming-scope boundary, not proof of a mixture or a wrong exact native graph.
- The 2019 FDA label was read only for section 11 identity and salt composition; current regulatory or marketing status was not assessed. An attempted openFDA substance query returned 404 and NCATS required browser verification, so no GSRS graph corroboration is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All original thirteen hashes are preserved, with actual source owners appended to sixteen. Public retrieval manifests retain real URLs, timestamps, status and hashes. Optional enrichment and source adoption were not performed.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T193832Z-lefamulin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Lefamulin: supported exact references with bounded assay and naming scope'
started_at: '2026-10-21T19:16:38Z'
finished_at: '2026-10-21T19:38:32Z'
reviewer:
  identity: Codex review002 subagent
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
summary: No confirmed native defect was found. All asserted exact chemical references
  reproduce the neutral eleven-centre lefamulin graph, and the deposited ligand in
  the cited primary ribosome structure agrees. Original structural, translation and
  multidrug-resistant pneumococcal studies support the definition and antibacterial
  class. A broader current PubChem name result and unspecified experimental bulk form
  limit automatic identity and quantitative transfers; optional target and activity
  gaps are not defects. Scientific assessment retains the stated evidence limits;
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
  - path: data/antibiotics/antibacterial/lefamulin.yaml
    sha256: 84854070cee781c6750bcd7499ab0628d37d1b31406b12b069e7577bcf1ff704
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/chebi_antimicrobials.tsv
    sha256: 4c33e56c3c342be657309f720f5b5cb9cad1fae13bec202ef99e449503c32004
    role: context
  - path: data/raw/chebi_role_names.tsv
    sha256: 5c476c0aacd7c98d7241d2343a6fc41ee9eb9338077404c5b011a04bf40c6ac5
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
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
- target_id: antibioticmech:aro-f8f4257b4b
  path: data/antibiotics/antibacterial/lefamulin.yaml
  label: lefamulin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI/ARO source extraction and class mapping
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Actual maintained source input for the record
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 597; one whole native record. All thirteen initial input
    hashes were verified unchanged before assessment. Actual ARO/PubChem inventory
    and enrichment owners were appended, giving sixteen captured inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-f8f4257b4b
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-f8f4257b4b
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/lefamulin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-f8f4257b4b
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/lefamulin.yaml --out /private/tmp/am-review-session/597-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-f8f4257b4b
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 597
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-comparison
  name: Independent chemical reference comparison
  status: passed
  required: false
  summary: Native, adopted/current exact PubChem, ChEMBL SMILES/InChI/molfile, current
    ChEBI and CCD62B serializations reproduce the same full key. A separate PubChem
    name result leaves one centre unspecified; clearing only native canonical C16
    reproduces that broader key.
  target_ids:
  - antibioticmech:aro-f8f4257b4b
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/597-compare.py
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
  - antibioticmech:aro-f8f4257b4b
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
  - antibioticmech:aro-f8f4257b4b
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
  - antibioticmech:aro-f8f4257b4b
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
  - antibioticmech:aro-f8f4257b4b
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
  - antibioticmech:aro-f8f4257b4b
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
  - antibioticmech:aro-f8f4257b4b
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
  - antibioticmech:aro-f8f4257b4b
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
  - antibioticmech:aro-f8f4257b4b
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
  - antibioticmech:aro-f8f4257b4b
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/lefamulin.yaml
  locator: 'Complete native YAML: identifier, definition/source, class/parent, all
    chemical properties, three exact references, source concept and three history
    events.'
  accessed_at: '2026-10-21T19:34:54Z'
  support: supports
  summary: The SEEDED MINTED record denotes neutral C28H45NO5S with key KPVIXBKIJXZQJX-FCEONZPQSA-N
    and eleven assigned tetrahedral centres. Its only biological description is a
    semisynthetic pleuromutilin with activity against multiresistant pathogens. No
    direct target, MIC, resistance, clinical, producer, dataset or causal-graph object
    is asserted.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv:324; data/raw/pubchem_structures.tsv:110;
    conf/sources.yaml; scripts/extract_source_inventory.py; scripts/enrich_pubchem_structures.py;
    scripts/seed_from_sources.py
  locator: Complete exact source rows and applicable source extraction, structure
    fallback and reference/class/definition seeding branches.
  accessed_at: '2026-10-21T19:34:54Z'
  support: supports
  summary: ARO3004088 supplies the definition, class and citation leads PMID32493034
    and 27958389. The first is emitted as definition_source. PubChem25185057 supplies
    native chemistry. No adopted ChEBI row supplies this record; the mint is reproducible.
    Actual owners were appended while preserving all thirteen original hashes.
  snapshot_sha256: 8e3e38ce5774ea9f39f05295906e96e18d78b8c047f76da72b4cc74b91c71b5a
- evidence_id: local-search
  kind: search
  reference: /private/tmp/am-review-session/597-local-hits.txt
  locator: Complete returned path inventory from ignored-inclusive and hidden-inclusive
    identifier/label/slug search.
  accessed_at: '2026-10-21T19:34:54Z'
  support: context_only
  summary: Matches include native/raw/generated files and historical research ledgers.
    Those ledgers were not scientific evidence. Exact maintained rows and the complete
    native record determine the scope of present claims and optional objects.
  snapshot_sha256: ec429c2506c5b177cf597a46ca59d3f1d2ba991b79053cac6d5b59bb7cc41d56
  search_scope: 2026-10-21; exact lefamulin, ARO3004088, CID25185057, CHEMBL3291398,
    slug and key. Local searches included ignored and hidden files. Europe PMC lefamulin
    with structure/ribosome/resistant limited to2010-2018 returned seventeen records;
    all titles and selected complete abstracts inspected. Bounded official identity
    follow-up.
- evidence_id: aro
  kind: database
  reference: https://purl.obolibrary.org/obo/aro.obo
  locator: Current ARO3004088 and parent/class ARO3000670, fully read.
  accessed_at: '2026-10-21T15:57:42Z'
  support: supports
  summary: The current exact compound term reproduces the native definition and both
    citations, with the same ChEMBL and PubChem links. ARO3000670 is the broader pleuromutilin
    class. Its generic natural-product and P-site prose is not an assertion that this
    semisynthetic exact compound was produced by a fungus or binds only one ribosomal
    site.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: exact-chemistry
  kind: database
  reference: PubChem:25185057; ChEMBL:CHEMBL3291398
  locator: Complete current structure responses and independent parsing of SMILES,
    InChI and ChEMBL molfile.
  accessed_at: '2026-10-21T19:31:38Z'
  support: supports
  summary: Both native exact chemical accessions reproduce FCEONZPQSA-N, formula C28H45NO5S
    and all eleven assigned centres. Native masses and neutral charge are consistent
    at source precision. ChEMBL clinical annotations were not treated as native clinical
    assertions or exact product identity.
  snapshot_sha256: 9fc2d703550e66cb83836d826a415965bd1da3a40011ed5f82060cefeee70e77
- evidence_id: current-chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/755252/
  locator: Complete current two-star entry and both structural strings.
  accessed_at: '2026-10-21T19:33:25Z'
  support: supports
  summary: Current ChEBI matches the exact native graph and antibacterial role. It
    is not an adopted source row and does not invalidate the historical minted rationale.
    Its newer citation list is not silently substituted for the record adopted leads.
  snapshot_sha256: 1edaab5b2825136938e241fbf2acd7d1f447c98d6e90ae54d8a53da76afdcb78
- evidence_id: name-scope
  kind: database
  reference: PubChem:58076382; PubChem:25185057
  locator: Current preferred-name query compared with the actual native exact accession.
  accessed_at: '2026-10-21T19:33:25Z'
  support: context_only
  summary: The name lefamulin currently resolves to CID58076382, with key KPVIXBKIJXZQJX-CSOZIWFHSA-N
    and canonical InChI C16 unspecified. All other centres agree with the native exact
    graph. CID25185057 remains the valid fully assigned accession used by this record.
    An annotation move or broader name hit does not by itself prove the exact native
    graph wrong or establish a mixture.
  snapshot_sha256: 4ec0af67039df993631f8b94ff9ca97802a222960ef44234e12368f4827d7f36
- evidence_id: diagnostic
  kind: validation
  reference: /private/tmp/am-review-session/597-authority-chemistry.json
  locator: Independent graph and stereo-scope calculations.
  accessed_at: '2026-10-21T19:34:54Z'
  support: supports
  summary: Twelve native/exact-authority serializations, including CCD and current
    ChEBI, match the fully assigned native key. Clearing only canonical InChI C16
    from the native graph reproduces the separate preferred-name result. That is a
    scope diagnostic rather than evidence for an opposite stereoisomer or an authorized
    structure change.
  snapshot_sha256: e090295482a8a82cd576e054b5bc28e04387c9714fba2bf974a124cb8e760c5e
- evidence_id: primary-structure
  kind: primary_source
  reference: PMID:27958389; DOI:10.1038/srep39004; PMC5154188
  locator: Full original main text, all figure captions and crystallographic Table
    1 read; Figures 1 and 3 viewed.
  accessed_at: '2026-10-21T19:31:54Z'
  support: supports
  summary: The 2016 original describes semisynthetic lefamulin and determines its
    S. aureus RN4220 large-subunit complex at 3.55Å. Figure 1 shows the mutilin-derived
    skeleton; the cyclohexyl sidechain drawing is not itself a complete absolute-stereo
    proof. The paper supports binding at the peptidyl-transferase centre, with the
    core occupying the A-site region and the extension directed toward the P-site.
    Structural modelling supports the ligand pose; no new independent absolute-hand
    determination is claimed.
  snapshot_sha256: c570a0aca1aeba097f37420aec72137fada970f67f8d286d8e69d0a06b4e3431
- evidence_id: deposition
  kind: database
  reference: PDB:5HL7; pdb-ccd:62B
  locator: Official RCSB entry/nonpolymer entity 31 and complete PDBe CCD response.
  accessed_at: '2026-10-21T19:32:49Z'
  support: supports
  summary: The deposited entry cites PMID27958389 and identifies entity 31 as lefamulin
    62B. Both CCD isomeric SMILES and its InChI reproduce all eleven native assignments.
    The ligand is modelled without an acetate counterion. This corroborates the deposited
    chemical identity but is not proof of the exact bulk reagent salt or independent
    re-refinement of the diffraction data.
  snapshot_sha256: 6a2ff8607157fd05be94b36e303a2340f2fb02da6dc4363a3a4119ad681ed280
- evidence_id: primary-function
  kind: primary_source
  reference: PMID:27958389; DOI:10.1038/srep39004
  locator: Original Figure 3 and coupled transcription/translation Methods.
  accessed_at: '2026-10-21T19:32:20Z'
  support: supports
  summary: The cell-free assay uses S. aureus ribosomes with ribosome-free E. coli
    extract and a luciferase reporter. Figure 3 and Results report lefamulin IC50
    0.02 µg/mL, versus 0.08 for BC3205 and 0.10 for tiamulin. This is reporter-expression
    inhibition, not Kd or an isolated chemical-step rate. The Methods concentration
    endpoints have inconsistent molar/mass conversions, so numerical enrichment should
    preserve the source ambiguity rather than silently repair it.
  snapshot_sha256: 128d84ae62b3413f40ae95a06f111422549945b5e1e084446a645a9d7d8220b7
- evidence_id: primary-selectivity
  kind: primary_source
  reference: PMID:27958389; DOI:10.1038/srep39004
  locator: Original selectivity Results, Figure 4 caption and Discussion.
  accessed_at: '2026-10-21T19:31:54Z'
  support: context_only
  summary: The authors compare bacterial, archaeal and eukaryotic ribosome structures
    and propose how local nucleotide conformations stabilize the bacterial binding
    pocket. The exact lefamulin experiment is the S. aureus complex and cell-free
    assay; the cross-kingdom structural rationale is not an experimental demonstration
    of absence of every host interaction. Optional target curation should retain that
    distinction.
  snapshot_sha256: c570a0aca1aeba097f37420aec72137fada970f67f8d286d8e69d0a06b4e3431
- evidence_id: primary-mdr
  kind: primary_source
  reference: PMID:27161634; DOI:10.1128/AAC.00627-16; PMC4914675
  locator: Full original main article and all three tables read; supplemental comparator-breakpoint
    table not inspected.
  accessed_at: '2026-10-21T19:31:54Z'
  support: supports
  summary: Broth microdilution tested 822 S. pneumoniae isolates from 58 US hospitals
    in 2010, using dry-form Thermo Fisher panels. MDR was defined by elevated MICs
    to at least three specified drug classes; 180 isolates met that definition. Lefamulin
    MIC50/MIC90 were 0.12/0.25 µg/mL in both the whole collection and MDR subset.
    These are collection statistics, not a universal claim about all multiresistant
    pathogens. Bulk salt/purity is not specified in the inspected article.
  snapshot_sha256: 8aaaa3ad2a73bd5367ebbb044ac343f4fab4e6c8ff398305f8529b1433ffdfb5
- evidence_id: adopted-review
  kind: database
  reference: PMID:32493034; DOI:10.1177/1060028020932521
  locator: Complete original review abstract read; review full text not obtained.
  accessed_at: '2026-10-21T19:31:38Z'
  support: context_only
  summary: This is a 2020 pharmacology/microbiology/clinical review, not a new primary
    experiment. It supports the broad drug-class and activity context but its trial
    summaries are not used as direct primary efficacy or molecular-binding proof.
    The second adopted citation and independently read original MDR study supply direct
    experimental support for the native description.
  snapshot_sha256: 1010707937b90868d8b071491d1096e6e121d350ff8bb4ccf39889384a07c84a
- evidence_id: official-salt
  kind: authority
  reference: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/211672s000%2C211673s000lbl.pdf
  locator: Original 2019 label section 11, printed page 12, text and structure viewed.
  accessed_at: '2026-10-21T19:34:54Z'
  support: supports
  summary: The official description identifies semisynthetic lefamulin with a 1R,2R,4R
    amino-hydroxycyclohexyl sidechain, supplied as acetate C30H49NO7S. It explicitly
    distinguishes acetate mass from equivalent lefamulin mass. The neutral native
    graph has no acetate component. No product identity, present marketing status
    or clinical approval assertion is added to this record.
  snapshot_sha256: a79ae297a09cd88b92902c91f929c1570f4caaa5a35331abc131ff2fdc7a576d
- evidence_id: additional-primary-leads
  kind: primary_source
  reference: PMID:28893785; PMID:29530863; PMID:27855075
  locator: Complete original abstracts read; full papers not inspected in this bounded
    review.
  accessed_at: '2026-10-21T19:31:38Z'
  support: context_only
  summary: These exact lefamulin studies report activity against resistant gonococci,
    selected sexually transmitted pathogens and macrolide-resistant M. pneumoniae.
    They corroborate that resistant-pathogen activity is not based solely on a chemical
    family inference. Their detailed efflux mechanisms, bactericidal endpoints and
    assay numbers were not transferred without full experimental scope.
  snapshot_sha256: 6b29964ad959fd9803e9682dd04ae100873262398ab79cf9dba0da811d93cde7
- evidence_id: bounded-search
  kind: search
  reference: Europe PMC exact lefamulin and resistance/structure/ribosome search,2010-2018,
    executed2026-10-21
  locator: All seventeen result titles inspected; adopted abstracts and selected relevant
    primary abstracts read; two decisive originals obtained in full.
  accessed_at: '2026-10-21T19:31:38Z'
  support: context_only
  summary: The search also returned secondary reviews, conference abstracts and derivative
    studies, which were not promoted to exact-parent experimental evidence. Official
    structure/label follow-up and a separate current PubChem name query resolved identity
    scope. No global absence claim is made.
  snapshot_sha256: 6b29964ad959fd9803e9682dd04ae100873262398ab79cf9dba0da811d93cde7
  search_scope: 2026-10-21; exact lefamulin, ARO3004088, CID25185057, CHEMBL3291398,
    slug and key. Local searches included ignored and hidden files. Europe PMC lefamulin
    with structure/ribosome/resistant limited to2010-2018 returned seventeen records;
    all titles and selected complete abstracts inspected. Bounded official identity
    follow-up.
- evidence_id: adapter-scope
  kind: database
  reference: Structured-source applicability to the native record
  locator: Native inventory before open-ended protein mechanism research.
  accessed_at: '2026-10-21T19:34:54Z'
  support: context_only
  summary: The native record has no gene, locus, exact protein target, pathway, stress
    response or transcriptomic dataset. Its chemical class alone does not require
    a matched iModulon query. The original rRNA complex and cell-free experiments
    were assessed directly; no expression-module result was needed or inferred.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral structure and stereochemical scope
  outcome: supported
  summary: All native exact references and the deposited primary ligand match the
    fully assigned neutral graph. The separate current name result has one unspecified
    centre and does not establish an opposite structure. The official acetate formulation
    remains chemically distinct.
  target_ids:
  - antibioticmech:aro-f8f4257b4b
  evidence_ids:
  - native
  - exact-chemistry
  - current-chebi
  - diagnostic
  - deposition
  - official-salt
- assessment_id: grounding
  area: grounding
  topic: Exact xrefs, broader class and mint
  outcome: supported
  summary: ARO, ChEMBL and PubChem exact assertions agree. The pleuromutilin class
    is broader than the semisynthetic derivative. A current nonadopted two-star ChEBI
    entry is corroboration, not automatic invalidation of the historical mint.
  target_ids:
  - antibioticmech:aro-f8f4257b4b
  evidence_ids:
  - aro
  - owners
  - exact-chemistry
  - current-chebi
- assessment_id: definition
  area: evidence
  topic: Semisynthesis and resistant-pathogen activity
  outcome: supported
  summary: The definition closely matches the adopted 2016 primary introduction and
    is supported by the original MDR pneumococcal collection. It does not explicitly
    assert all pathogens are susceptible. A more specific description could help future
    curation, but optional wording precision is not a confirmed defect. The nearest
    emitted citation is correctly recognized here as a review.
  target_ids:
  - antibioticmech:aro-f8f4257b4b
  evidence_ids:
  - primary-structure
  - primary-mdr
  - adopted-review
  - additional-primary-leads
- assessment_id: mechanism
  area: evidence
  topic: Ribosome binding and translation inhibition
  outcome: supported
  summary: Exact lefamulin binding to the S. aureus PTC and coupled reporter-expression
    inhibition are directly supported. The A/P-site distinction and structural selectivity
    rationale are preserved. The native record makes no incorrect direct-protein or
    single-step kinetic claim.
  target_ids:
  - antibioticmech:aro-f8f4257b4b
  evidence_ids:
  - primary-structure
  - deposition
  - primary-function
  - primary-selectivity
- assessment_id: provenance
  area: provenance
  topic: Source ownership and history
  outcome: supported
  summary: The complete native record and maintained rows were read. Both adopted
    citations were dispositioned and source dates/mint/history reproduce. All original
    hashes remain unchanged and actual owners are included.
  target_ids:
  - antibioticmech:aro-f8f4257b4b
  evidence_ids:
  - owners
  - native
  - local-search
- assessment_id: coverage
  area: completeness
  topic: Optional biological enrichment and access boundaries
  outcome: supported
  summary: Every asserted field and exact chemical reference was examined. Primary
    activity and molecular mode were checked even though those optional structured
    objects are not present. No missing optional field was counted as a defect; clinical
    product data were kept separate.
  target_ids:
  - antibioticmech:aro-f8f4257b4b
  evidence_ids:
  - native
  - primary-mdr
  - primary-function
  - official-salt
  - bounded-search
  - adapter-scope
findings: []
actions:
- action_id: A1
  description: Keep any optional mechanism and activity enrichment tied to the exact
    experiment.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-f8f4257b4b
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/lefamulin.yaml
    role: Curator-owned mechanism and activity evidence through the validated writer
  acceptance_checks:
  - Use the S. aureus 23S-rRNA/PTC binding context, distinguish the A-site core from
    the P-site extension and keep structural selectivity rationale separate from direct
    host assays.
  - Treat the 0.02 µg/mL endpoint as coupled reporter-expression IC50. Preserve or
    resolve the inconsistent concentration conversions before copying detailed dose
    ranges.
  - Keep pneumococcal MDR collection statistics and their definition distinct from
    individual-strain MICs or a universal resistance claim. Do not assume the unspecified
    bulk material was the neutral solid or a particular salt.
- action_id: A2
  description: Preserve exact-accession identity when consulting name-based authorities.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-f8f4257b4b
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained exact-accession structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding adjudication if future source adoption is authorized
  acceptance_checks:
  - Do not replace the eleven-centre native graph with the ten-assigned-centre PubChem
    name result without an explicit evidence-backed scope decision.
  - Retain the free-compound versus acetate distinction and historical minted provenance.
    A current two-star ChEBI record alone is not a mandate to alter the adopted inventory.
limitations:
- The 2016 ribosome original was read in full with all captions and Table 1; Figures
  1 and 3 were viewed. Coordinates/diffraction data were not re-refined. The crystal
  model corroborates ligand identity but does not independently establish every absolute
  centre or bulk formulation.
- The 2016 MDR pneumococcal main text and all three tables were read; the supplemental
  comparator-breakpoint table was not. Exact bulk salt, purity and mass normalization
  were not specified in the inspected text.
- The coupled-assay Methods has inconsistent molar/mass endpoint conversions; the
  reported 0.02 µg/mL IC50 agrees between Figure 3 and Results. This source limitation
  does not contradict any native numerical claim, because none is present.
- The adopted 2020 review was read at complete-abstract depth only. Three additional
  exact-parent activity abstracts were inspected, but no detailed assay or efflux
  data were transferred from them.
- The current PubChem preferred-name result leaves canonical C16 unspecified, whereas
  the actual native exact accession, ChEMBL, ChEBI and CCD agree on all eleven assigned
  centres. This is retained as a naming-scope boundary, not proof of a mixture or
  a wrong exact native graph.
- The 2019 FDA label was read only for section 11 identity and salt composition; current
  regulatory or marketing status was not assessed. An attempted openFDA substance
  query returned 404 and NCATS required browser verification, so no GSRS graph corroboration
  is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All original thirteen hashes are preserved, with actual source owners appended to
  sixteen. Public retrieval manifests retain real URLs, timestamps, status and hashes.
  Optional enrichment and source adoption were not performed.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
