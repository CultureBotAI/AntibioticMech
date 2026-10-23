# Albicidin: exact identity and qualified gyrase evidence

- Review: 20261021T084555Z-albicidin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:35:43Z
- Finished UTC: 2026-10-21T08:45:55Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact neutral S/E albicidin structure is internally consistent and corroborated by current chemical authorities. The gyrase-poisoning mechanism is supported, but the imported definition makes an unbounded comparative potency claim. Original studies provide useful mechanism and resistance evidence with important material, construct and assay distinctions.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position081; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-34c0642a61 | data/antibiotics/antibacterial/albicidin.yaml | generated | albicidin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-34c0642a61 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-34c0642a61 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-34c0642a61 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-34c0642a61 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-34c0642a61 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-34c0642a61 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-34c0642a61 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-34c0642a61 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-34c0642a61 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-34c0642a61 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-34c0642a61 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-34c0642a61 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact S/E neutral molecule

identity: supported. Targets: antibioticmech:aro-34c0642a61.

Native representations and external full keys agree. Historical minted identifier is reproducible.

### Comparative potency

evidence: concern. Targets: antibioticmech:aro-34c0642a61.

The definition lacks comparator set and assay context; broad superiority is not established for this exact molecule.

### Gyrase poisoning and complex binding

evidence: supported. Targets: antibioticmech:aro-34c0642a61.

Later primary structural evidence supports the broad mechanism while resolving protein/DNA participation. Earlier exact-material and mutant-label limitations must be retained.

### Nonribosomal peptide antibacterial

grounding: supported. Targets: antibioticmech:aro-34c0642a61.

Chemical and biological class is defensible; no need to fabricate missing activity-role objects.

### Primary evidence and resistance context

completeness: unknown. Targets: antibioticmech:aro-34c0642a61.

Optional enrichment is available; AlbA sequestration must be distinguished from target inhibition and isolate-level causality.

### Source ownership and unchanged record

ownership: supported. Targets: antibioticmech:aro-34c0642a61.

Captured ARO/PubChem owners and provenance reproduce the native assertions; no record edits were made.

## Findings

### F1: Scope the imported comparative potency claim

minor / open / confirmed; issue key: albicidin-unbounded-comparative-potency.

The definition states superiority over most DNA gyrase inhibitors without naming comparators, endpoint or assay. The adopted review repeats the generalization; the original controlled experiments use specific comparators and an incompletely characterized α-peak material.

### F2: Add direct complex-binding and resistance evidence with experiment boundaries

informational / open / confirmed; issue key: albicidin-scoped-primary-complex-and-resistance-evidence.

Concrete2023 gyrase–DNA structural and2018 AlbA sequestration studies can enrich optional evidence and target/resistance objects without transferring analogue, construct or clinical-isolate claims.

## Recommended Actions And Acceptance Checks

### A1

Replace the unbounded comparison with a source-scoped mechanism definition and optionally curate direct primary evidence.

- Name comparator and endpoint for any retained potency comparison; keep2007 α-peak identity uncertainty and bioassay calibration explicit. Resolve MG1665/MG1655 and S83L/S83W discrepancies before strain/variant import.
- Ground the gyrase–DNA complex mechanism with2023 evidence; distinguish directly observed binding from the proposed temporal model, and parent albicidin from Albi-1–3/photo-Albi.
- Represent AlbA as a resistance sequestration factor; distinguish AlbAS from AlbAL and do not infer isolate-level causal resistance from homolog presence alone.
- Use the maintained source/curation route, validated writer and history, preserve exact neutral E/S chemistry, and run required gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/albicidin.yaml; Entire YAML and all three seed/reseed history entries | supports | SEEDED/MINTED exact neutral C44H38N6O12 with one assigned tetrahedral centre and E alkene, four xrefs, one ARO source concept and nonribosomal peptide class. Definition cites PMID31451755. No structured target, quantitative activity, producer, resistance or expression claim is present. |
| owner | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; Exact adopted row and 081-raw.json; inspected source extractor/seeder | supports | ARO row reproduces the definition, parent/class and chemical references; it also cites PMID17074789. The source-specific mint reproduces. Exact-row checks found no ChEBI source inventory row or ARO target/resistance edge for this compound. All17 captured maintained hashes are unchanged. |
| identity | https://pubchem.ncbi.nlm.nih.gov/compound/78322514; 081-pubchem.json, current CHEBI218232 page and ChEMBL5281137 API | supports | All three authorities agree on NZSWNNDHPOTJNH-VEJILBAHSA-N and C44H38N6O12. Current ChEBI is a two-star third-party entry; its present existence alone does not invalidate the historical source-specific minted status. ChEMBL SMILES was independently parsed to the native full key. |
| chemistry | Independent RDKit calculation; 081-chemistry.json; focus009-root.py81 | supports | Native SMILES and InChI regenerate the same full key, one neutral fragment, S centre and assigned E double bond. Calculated average842.818 rounds correctly to native842.8; exact842.254770656 agrees. No mass or stereo defect is present. |
| ontology | https://card.mcmaster.ca/ontology/46436; Official ARO3007658 page; ARO3009657 and current OLS parent check | supports | CARD names albicidin, repeats the definition and both adopted citations, and links the same chemical structures. Nonribosomal peptide classification is consistent with the molecule and published biosynthetic context. Current CARD displays peptide-antibiotic class wording; the adopted narrower ARO class remains scientifically appropriate. |
| review | PMID:31451755; DOI:10.1038/s41429-019-0228-2; complete EuropePMC abstract | partial | The adopted2019 article is a review summarizing mechanism, production and therapeutic prospects. It uses broad comparative potency language; it is not a new controlled comparison establishing superiority over most gyrase inhibitors. |
| early | PMID:17074789; DOI:10.1128/AAC.00918-06; PMC1797663 complete main Methods, Results and Discussion | supports | Purified E.coli gyrase inhibition and cleavage-complex experiments support the general mechanism. Methods explicitly used the HPLC α peak, distinct from the β peak described from rich media, and state full structures were then unresolved. Drug amounts were bioassay-calibrated. Thus the ~40nM gyrase IC50 and mutant effects need an exact-material qualifier before attachment to this modern structure. Comparisons with ciprofloxacin and novobiocin concern specific assay conditions, not all inhibitors. |
| early-boundaries | https://pmc.ncbi.nlm.nih.gov/articles/PMC1797663/; Methods bacterial strains, Fig1/5 captions, Table2 and Discussion | context_only | Cellular GyrA S83L and purified GyrA S83W experiments are distinct; Table2 inconsistently labels the mutant enzyme S83L. The paper prints MG1665 in multiple places and MG1655 elsewhere, so identifiers require adjudication before strain mapping. AlbG protection and quinolone cross-resistance are mechanistic observations, not clinical breakpoint calls. Original speculation about a binding pose is superseded by direct later structural evidence. |
| structure | https://doi.org/10.1038/s41929-022-00904-1; PMC9886550 Main, cleavage/binding Results, mutagenesis and TopoIV Results, Discussion and relevant Methods; Fig1 visually inspected | supports | The2023 cryo-EM study examines full-length E.coli gyrase with217bp DNA and ADPNP. Native albicidin is explicitly distinguished from Albi-1–3 and photo-Albi. Its N-terminal segment intercalates into cleaved DNA while the C-terminal arm occupies the GyrA/GyrA interface; the central S residue connects them and contacts involve GyrB as well. This supports a gyrase–DNA complex mechanism, not an exclusive isolated-subunit target. Figure1b depicts the native E/S structure. |
| structure-boundaries | https://pmc.ncbi.nlm.nih.gov/articles/PMC9886550/; Mutagenesis, TopoIV, MIC Methods and Discussion | context_only | Designed enzyme mutants establish assay-level susceptibility effects; impaired catalytic activity complicates some variants. Parent albicidin and improved analogues have different potency and resistance profiles. TopoIV inhibition is weaker than gyrase inhibition. Native MIC methods name six strains, MHBII and20h incubation, but the supplementary numeric table was not assessed. The proposed temporal entry sequence and AlbG displacement model remain interpretations; analog animal efficacy is not native albicidin clinical efficacy. |
| resistance | https://doi.org/10.1038/s41467-018-05551-4; PMC6078987 abstract, Results1–3, MIC/chemical-synthesis/fluorescence Methods and data availability | supports | The2018 study distinguishes Klebsiella oxytoca AlbAS drug-binding domain from full-length AlbAL. Fluorescence fits report5.6±0.2nM and7.4±0.9nM respectively; a1.7Å AlbAS–albicidin structure is deposited as6ET8. Neutralization and competition assays support sequestration. AlbA is a resistance factor, not the antibacterial target. Reported high MICs across clinical isolates and homolog presence do not prove AlbA causes resistance in every isolate; the main Methods lack strain-level identifiers and detailed AST conditions. |
| adapter | iModulonDB e_coli/precise1k; 081-imodulondb-gyra.txt, structured query before web research | context_only | Native definition names gyrase, triggering a structured gene-context check. Query succeeded with gyrA b2231, gyrB b3699, sbmC b2009 and yacG b0101, and zero modules. These are dataset-context hits, not albicidin perturbation evidence or organism/strain equivalence. |
| search | CultureBotAI/AntibioticMech; 081-local-hits.txt and081089090-maintained-hits.txt | context_only | Ignored-inclusive local searches identify source/native/queue references and historical discovery/status artifacts. They do not establish primary adjudication. Both adopted citations were dispositioned, and free follow-up found direct structural and resistance evidence. No exhaustive absence claim is made. |

## Limits And Additional Notes

- The2007 full main article was read, but its historical α-peak material cannot be retrospectively equated to the present exact structure from that paper alone.
- The2023 primary was read in the listed main sections and Figure1; supplementary numeric MIC tables, raw cryo-EM data and derivative synthesis were not independently audited. The2018 study was read in the listed sections; supplementary isolate and raw structure details were not reanalysed.
- The adopted2019 review was assessed at abstract level. Its review status and comparative wording are explicit. No clinical efficacy or approval is inferred.
- Structured gene-context results contain no demonstrated drug-response module and are not evidence of mechanism absence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T084555Z-albicidin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Albicidin: exact identity and qualified gyrase evidence'
started_at: '2026-10-21T08:35:43Z'
finished_at: '2026-10-21T08:45:55Z'
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
summary: The exact neutral S/E albicidin structure is internally consistent and corroborated
  by current chemical authorities. The gyrase-poisoning mechanism is supported, but
  the imported definition makes an unbounded comparative potency claim. Original studies
  provide useful mechanism and resistance evidence with important material, construct
  and assay distinctions.
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
  - path: data/antibiotics/antibacterial/albicidin.yaml
    sha256: 7943a642afbcd79e8fbaa61b0fb07b09ef04b5e3171722773e6bf344162132e5
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
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
targets:
- target_id: antibioticmech:aro-34c0642a61
  path: data/antibiotics/antibacterial/albicidin.yaml
  label: albicidin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition, class and chemical references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record and chemical grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Formal exact-grounding override
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position081; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-34c0642a61
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-34c0642a61
  command: .venv/bin/python /private/tmp/am-review-session/focus009-root.py 81
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-34c0642a61
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/albicidin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-34c0642a61
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/albicidin.yaml --out /private/tmp/am-review-session/081-strict.tsv
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
  - antibioticmech:aro-34c0642a61
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
  - antibioticmech:aro-34c0642a61
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
  - antibioticmech:aro-34c0642a61
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
  - antibioticmech:aro-34c0642a61
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
  - antibioticmech:aro-34c0642a61
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
  - antibioticmech:aro-34c0642a61
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
  - antibioticmech:aro-34c0642a61
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
  - antibioticmech:aro-34c0642a61
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
  - antibioticmech:aro-34c0642a61
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/albicidin.yaml
  locator: Entire YAML and all three seed/reseed history entries
  accessed_at: '2026-10-21T08:45:48Z'
  support: supports
  summary: SEEDED/MINTED exact neutral C44H38N6O12 with one assigned tetrahedral centre
    and E alkene, four xrefs, one ARO source concept and nonribosomal peptide class.
    Definition cites PMID31451755. No structured target, quantitative activity, producer,
    resistance or expression claim is present.
- evidence_id: owner
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv
  locator: Exact adopted row and 081-raw.json; inspected source extractor/seeder
  accessed_at: '2026-10-21T08:45:48Z'
  support: supports
  summary: ARO row reproduces the definition, parent/class and chemical references;
    it also cites PMID17074789. The source-specific mint reproduces. Exact-row checks
    found no ChEBI source inventory row or ARO target/resistance edge for this compound.
    All17 captured maintained hashes are unchanged.
  snapshot_sha256: 6d421333d2712c4908919273bad2d3186a2cebaca17961c36fbaabac427f84db
- evidence_id: identity
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/78322514
  locator: 081-pubchem.json, current CHEBI218232 page and ChEMBL5281137 API
  accessed_at: '2026-10-21T08:45:48Z'
  support: supports
  summary: All three authorities agree on NZSWNNDHPOTJNH-VEJILBAHSA-N and C44H38N6O12.
    Current ChEBI is a two-star third-party entry; its present existence alone does
    not invalidate the historical source-specific minted status. ChEMBL SMILES was
    independently parsed to the native full key.
  snapshot_sha256: 7fd91a7860db3abcd81f5c8fefd31dca8a987e49cf1a9c3397e3c5bc48940c86
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculation
  locator: 081-chemistry.json; focus009-root.py81
  accessed_at: '2026-10-21T08:45:48Z'
  support: supports
  summary: Native SMILES and InChI regenerate the same full key, one neutral fragment,
    S centre and assigned E double bond. Calculated average842.818 rounds correctly
    to native842.8; exact842.254770656 agrees. No mass or stereo defect is present.
  snapshot_sha256: 1136011157d6182dc2e18c640412668d4e91e7671a309d78927d73139fe14ecb
- evidence_id: ontology
  kind: authority
  reference: https://card.mcmaster.ca/ontology/46436
  locator: Official ARO3007658 page; ARO3009657 and current OLS parent check
  accessed_at: '2026-10-21T08:45:48Z'
  support: supports
  summary: CARD names albicidin, repeats the definition and both adopted citations,
    and links the same chemical structures. Nonribosomal peptide classification is
    consistent with the molecule and published biosynthetic context. Current CARD
    displays peptide-antibiotic class wording; the adopted narrower ARO class remains
    scientifically appropriate.
- evidence_id: review
  kind: authority
  reference: PMID:31451755
  locator: DOI:10.1038/s41429-019-0228-2; complete EuropePMC abstract
  accessed_at: '2026-10-21T08:45:48Z'
  support: partial
  summary: The adopted2019 article is a review summarizing mechanism, production and
    therapeutic prospects. It uses broad comparative potency language; it is not a
    new controlled comparison establishing superiority over most gyrase inhibitors.
  snapshot_sha256: 547c09048aa9f1dcc8d9a89c0efc41246f8c4bf7ac386afb450abc340d6f668d
- evidence_id: early
  kind: primary_source
  reference: PMID:17074789
  locator: DOI:10.1128/AAC.00918-06; PMC1797663 complete main Methods, Results and
    Discussion
  accessed_at: '2026-10-21T08:45:48Z'
  support: supports
  summary: Purified E.coli gyrase inhibition and cleavage-complex experiments support
    the general mechanism. Methods explicitly used the HPLC α peak, distinct from
    the β peak described from rich media, and state full structures were then unresolved.
    Drug amounts were bioassay-calibrated. Thus the ~40nM gyrase IC50 and mutant effects
    need an exact-material qualifier before attachment to this modern structure. Comparisons
    with ciprofloxacin and novobiocin concern specific assay conditions, not all inhibitors.
  snapshot_sha256: fa24b6ca31daa323807a2281c1e3d406ec4109be60eaea1ad9b60587aa89b4d0
- evidence_id: early-boundaries
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1797663/
  locator: Methods bacterial strains, Fig1/5 captions, Table2 and Discussion
  accessed_at: '2026-10-21T08:45:48Z'
  support: context_only
  summary: Cellular GyrA S83L and purified GyrA S83W experiments are distinct; Table2
    inconsistently labels the mutant enzyme S83L. The paper prints MG1665 in multiple
    places and MG1655 elsewhere, so identifiers require adjudication before strain
    mapping. AlbG protection and quinolone cross-resistance are mechanistic observations,
    not clinical breakpoint calls. Original speculation about a binding pose is superseded
    by direct later structural evidence.
- evidence_id: structure
  kind: primary_source
  reference: https://doi.org/10.1038/s41929-022-00904-1
  locator: PMC9886550 Main, cleavage/binding Results, mutagenesis and TopoIV Results,
    Discussion and relevant Methods; Fig1 visually inspected
  accessed_at: '2026-10-21T08:45:48Z'
  support: supports
  summary: The2023 cryo-EM study examines full-length E.coli gyrase with217bp DNA
    and ADPNP. Native albicidin is explicitly distinguished from Albi-1–3 and photo-Albi.
    Its N-terminal segment intercalates into cleaved DNA while the C-terminal arm
    occupies the GyrA/GyrA interface; the central S residue connects them and contacts
    involve GyrB as well. This supports a gyrase–DNA complex mechanism, not an exclusive
    isolated-subunit target. Figure1b depicts the native E/S structure.
  snapshot_sha256: efb75b515f463b7a95b6558f003ee0ef0163ba0a2d2a8fee88f7163add045c81
- evidence_id: structure-boundaries
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC9886550/
  locator: Mutagenesis, TopoIV, MIC Methods and Discussion
  accessed_at: '2026-10-21T08:45:48Z'
  support: context_only
  summary: Designed enzyme mutants establish assay-level susceptibility effects; impaired
    catalytic activity complicates some variants. Parent albicidin and improved analogues
    have different potency and resistance profiles. TopoIV inhibition is weaker than
    gyrase inhibition. Native MIC methods name six strains, MHBII and20h incubation,
    but the supplementary numeric table was not assessed. The proposed temporal entry
    sequence and AlbG displacement model remain interpretations; analog animal efficacy
    is not native albicidin clinical efficacy.
- evidence_id: resistance
  kind: primary_source
  reference: https://doi.org/10.1038/s41467-018-05551-4
  locator: PMC6078987 abstract, Results1–3, MIC/chemical-synthesis/fluorescence Methods
    and data availability
  accessed_at: '2026-10-21T08:45:48Z'
  support: supports
  summary: The2018 study distinguishes Klebsiella oxytoca AlbAS drug-binding domain
    from full-length AlbAL. Fluorescence fits report5.6±0.2nM and7.4±0.9nM respectively;
    a1.7Å AlbAS–albicidin structure is deposited as6ET8. Neutralization and competition
    assays support sequestration. AlbA is a resistance factor, not the antibacterial
    target. Reported high MICs across clinical isolates and homolog presence do not
    prove AlbA causes resistance in every isolate; the main Methods lack strain-level
    identifiers and detailed AST conditions.
  snapshot_sha256: ec8fe78e8a2df431910ac9049974558356221a5de1a616ce8306c980eef6b9ab
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/precise1k
  locator: 081-imodulondb-gyra.txt, structured query before web research
  accessed_at: '2026-10-21T08:45:48Z'
  support: context_only
  summary: Native definition names gyrase, triggering a structured gene-context check.
    Query succeeded with gyrA b2231, gyrB b3699, sbmC b2009 and yacG b0101, and zero
    modules. These are dataset-context hits, not albicidin perturbation evidence or
    organism/strain equivalence.
  snapshot_sha256: 424b867c86f081f31f7cce9346e736715e30d1de662965620bbdb8b547d23f99
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 081-local-hits.txt and081089090-maintained-hits.txt
  accessed_at: '2026-10-21T08:45:48Z'
  support: context_only
  summary: Ignored-inclusive local searches identify source/native/queue references
    and historical discovery/status artifacts. They do not establish primary adjudication.
    Both adopted citations were dispositioned, and free follow-up found direct structural
    and resistance evidence. No exhaustive absence claim is made.
  search_scope: rg --no-ignore --hidden in isolated batch009 excluding .git/.venv;
    targeted maintained curation/conf/scripts/data/raw/research/reviews follow-up,
    with large .obo/.jsonl/.html exclusions limited to that narrower follow-up. Current
    public CARD, ChEBI, PubChem, ChEMBL, OLS, EuropePMC and PMC originals.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact S/E neutral molecule
  outcome: supported
  summary: Native representations and external full keys agree. Historical minted
    identifier is reproducible.
  target_ids:
  - antibioticmech:aro-34c0642a61
  evidence_ids:
  - identity
  - chemistry
  - owner
- assessment_id: definition
  area: evidence
  topic: Comparative potency
  outcome: concern
  summary: The definition lacks comparator set and assay context; broad superiority
    is not established for this exact molecule.
  target_ids:
  - antibioticmech:aro-34c0642a61
  evidence_ids:
  - native
  - review
  - early
- assessment_id: mechanism
  area: evidence
  topic: Gyrase poisoning and complex binding
  outcome: supported
  summary: Later primary structural evidence supports the broad mechanism while resolving
    protein/DNA participation. Earlier exact-material and mutant-label limitations
    must be retained.
  target_ids:
  - antibioticmech:aro-34c0642a61
  evidence_ids:
  - early
  - early-boundaries
  - structure
  - structure-boundaries
- assessment_id: class
  area: grounding
  topic: Nonribosomal peptide antibacterial
  outcome: supported
  summary: Chemical and biological class is defensible; no need to fabricate missing
    activity-role objects.
  target_ids:
  - antibioticmech:aro-34c0642a61
  evidence_ids:
  - ontology
  - structure
- assessment_id: completeness
  area: completeness
  topic: Primary evidence and resistance context
  outcome: unknown
  summary: Optional enrichment is available; AlbA sequestration must be distinguished
    from target inhibition and isolate-level causality.
  target_ids:
  - antibioticmech:aro-34c0642a61
  evidence_ids:
  - structure
  - resistance
  - adapter
- assessment_id: ownership
  area: ownership
  topic: Source ownership and unchanged record
  outcome: supported
  summary: Captured ARO/PubChem owners and provenance reproduce the native assertions;
    no record edits were made.
  target_ids:
  - antibioticmech:aro-34c0642a61
  evidence_ids:
  - native
  - owner
findings:
- finding_id: F1
  issue_key: albicidin-unbounded-comparative-potency
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Scope the imported comparative potency claim
  description: The definition states superiority over most DNA gyrase inhibitors without
    naming comparators, endpoint or assay. The adopted review repeats the generalization;
    the original controlled experiments use specific comparators and an incompletely
    characterized α-peak material.
  target_ids:
  - antibioticmech:aro-34c0642a61
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - native
  - review
  - early
  rule_id: 'native-review-checklist: Definition and Evidence'
  native_severity: minor unsupported claim scope
  normalization_reason: The core mechanism and identity are supported; the defect
    is an overbroad comparison.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition, class and chemical references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record and chemical grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Formal exact-grounding override
- finding_id: F2
  issue_key: albicidin-scoped-primary-complex-and-resistance-evidence
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Add direct complex-binding and resistance evidence with experiment boundaries
  description: Concrete2023 gyrase–DNA structural and2018 AlbA sequestration studies
    can enrich optional evidence and target/resistance objects without transferring
    analogue, construct or clinical-isolate claims.
  target_ids:
  - antibioticmech:aro-34c0642a61
  field_paths:
  - evidence
  - molecular_targets
  - resistance
  - discussions
  evidence_ids:
  - structure
  - structure-boundaries
  - resistance
  - early-boundaries
  rule_id: 'native-review-checklist: Targets and Resistance'
  native_severity: informational optional enrichment
  normalization_reason: Missing optional collections alone are not defects.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition, class and chemical references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record and chemical grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Formal exact-grounding override
actions:
- action_id: A1
  description: Replace the unbounded comparison with a source-scoped mechanism definition
    and optionally curate direct primary evidence.
  finding_ids:
  - F1
  - F2
  target_ids:
  - antibioticmech:aro-34c0642a61
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition, class and chemical references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record and chemical grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Formal exact-grounding override
  acceptance_checks:
  - Name comparator and endpoint for any retained potency comparison; keep2007 α-peak
    identity uncertainty and bioassay calibration explicit. Resolve MG1665/MG1655
    and S83L/S83W discrepancies before strain/variant import.
  - Ground the gyrase–DNA complex mechanism with2023 evidence; distinguish directly
    observed binding from the proposed temporal model, and parent albicidin from Albi-1–3/photo-Albi.
  - Represent AlbA as a resistance sequestration factor; distinguish AlbAS from AlbAL
    and do not infer isolate-level causal resistance from homolog presence alone.
  - Use the maintained source/curation route, validated writer and history, preserve
    exact neutral E/S chemistry, and run required gates.
limitations:
- The2007 full main article was read, but its historical α-peak material cannot be
  retrospectively equated to the present exact structure from that paper alone.
- The2023 primary was read in the listed main sections and Figure1; supplementary
  numeric MIC tables, raw cryo-EM data and derivative synthesis were not independently
  audited. The2018 study was read in the listed sections; supplementary isolate and
  raw structure details were not reanalysed.
- The adopted2019 review was assessed at abstract level. Its review status and comparative
  wording are explicit. No clinical efficacy or approval is inferred.
- Structured gene-context results contain no demonstrated drug-response module and
  are not evidence of mechanism absence.
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
