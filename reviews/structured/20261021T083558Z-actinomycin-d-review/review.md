# Actinomycin D: exact identity, qualified DNA target and dated FDA assertions

- Review: 20261021T083558Z-actinomycin-d-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:21:55Z
- Finished UTC: 2026-10-21T08:35:58Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Exact actinomycin D identity and the broad DNA-mediated inhibition claim are supported. All seven dated FDA product assertions match current official records. The native target is correctly limited to a database assertion. Primary DNA-binding and antibacterial studies offer scoped enrichment; neither omics responses nor FDA approval establish clinical anti-infective efficacy. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position078; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:27666 | data/antibiotics/antibacterial/actinomycin-d.yaml | generated | actinomycin D |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:27666 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:27666 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:27666 | Actual focused execution exited 0. |
| Structured transcription query | failed | False | CHEBI:27666 | Actual public query exited2 because a returned regulator field was NoneType; no module data adopted. |
| Narrow structured locus query | passed | False | CHEBI:27666 | One gene, zero modules; context only. |
| Authoritative full QC | failed | True | CHEBI:27666 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:27666 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:27666 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:27666 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:27666 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:27666 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:27666 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:27666 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:27666 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral actinomycin D

identity: supported. Targets: CHEBI:27666.

Native chemistry, synonyms and full-key authorities agree; KEGG MOL stereo incompleteness is a source verification limitation.

### DNA target and transcription

evidence: supported. Targets: CHEBI:27666.

Database-only target qualification is truthful. Adopted model and independent primary DNA-binding experiments support the broad mechanism without asserting direct polymerase binding.

### Family and antimicrobial role

grounding: supported. Targets: CHEBI:27666.

Structure fits parent classes; primary purified-compound bacterial activity supports antimicrobial classification.

### Dated FDA approval assertions

scope: supported. Targets: CHEBI:27666.

All seven dated product assertions match official records; GSRS exact identity is corroborated. No antimicrobial clinical indication is inferred.

### Primary activity, mechanism and producer context

completeness: unknown. Targets: CHEBI:27666.

Concrete evidence can enrich optional objects. MBC range discrepancy, producer strain identification and omics inference limitations require explicit qualification.

### Imported fields and history

ownership: supported. Targets: CHEBI:27666.

Captured CHEBI/ARO/FDA owners and deterministic mints reproduce; all source hashes and native status remain unchanged.

## Findings

### F1: Add scoped primary DNA-binding and antibacterial evidence

informational / open / confirmed; issue key: actinomycin-d-scoped-primary-dna-activity-evidence.

The qualified database target is not an error. Original biochemical and purified-compound studies supply concrete optional primary evidence; keep the1985 model,1962 binding experiments and2021 downstream omics distinct.

## Recommended Actions And Acceptance Checks

### A1

Optionally curate precise original evidence without changing exact identity or generalizing regulatory approval.

- Keep DNA as the attacked component; do not substitute rpoB or RNA polymerase as a demonstrated directly bound protein. Preserve the1985 model status and1962 drug calibration limitation.
- For2021 MIC preserve ATCC25923, MHB,24h,37°C and exact purified material. Resolve MBC64 versus maximum listed32 before importing MBC.
- Retain SCAU-062 producer identity/taxonomy evidence; do not swap in its closest sequence comparator. Treat omics changes as response associations, not direct enzyme targets or bacterial mitochondrial processes.
- Use write_validated_antibiotic and record_curation_event, maintain CARD qualification consistently, and run required gates. Retain dated FDA assertions without implying clinical anti-infective use.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/actinomycin-d.yaml; Entire YAML, including all seven clinical assertions and seven history entries | supports | SEEDED/EXACT neutral C62H86N12O16, seven synonyms including actinomycin C1 and IV, two parent classes, antimicrobial role, ARO/CHEBI source concepts, ten chemical/drug xrefs and one document xref. One NUCLEIC_ACID ATTACKED_COMPONENT target explicitly states DATABASE_ASSERTION_ONLY with no organism or strain. No quantitative activity, producer, resistance, causal graph or expression dataset is asserted. |
| owner | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv; data/raw/fda_clinical_status.tsv; Exact rows in 078-raw.json; seeder and FDA extractor inspected | supports | Raw ChEBI row 499 and ARO row 192 merge consistently; target row 211 reproduces the qualified edge; seven FDA rows 2536–2542 join via exact GSRS InChIKey. Both source-specific SHA256 mints reproduce. No matching target upgrade exists in card_evidence_reviews.json (ignored-inclusive exact-ID search). All 20 captured maintained hashes remain unchanged. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:27666; 078-chebi-visible.txt, current CARD ARO:3000696 page and official PubChem/ChEMBL/DrugCentral snapshots | supports | Current ChEBI, PubChem CID457193, ChEMBL1554 and DrugCentral774 InChI all match RJURFGZVJUQBHK-IIXSONLDSA-N and the neutral formula. Current CARD label/definition and chemical grounding agree. Common names and CAS50-76-0 are corroborated. Independent registry access is not claimed. |
| chemistry | Independent RDKit calculation; 078-chemistry.json; explicit ChEMBL, DrugCentral and KEGG parsing | supports | Both native encodings yield the same full key, one neutral fragment, all ten tetrahedral centres assigned, average mass1255.438 and exact mass1254.628474672. Both source mints reproduce. KEGG C06770 and D00214 MOL files reproduce connectivity but leave all ten centres unspecified (key suffix UHFFFAOYSA); their named entries support documentary identity, not independent stereochemical verification. |
| xrefs | https://rest.kegg.jp/get/C06770; Both KEGG text/MOL entries; 078-drugcentral-inchi.txt; source registry links; Wikipedia document | partial | KEGG compound and drug entries name actinomycin D/dactinomycin, share the native formula/CAS and cross-link ChEBI27666. DrugCentral explicit InChI matches exact stereo. The KEGG generic RNA-polymerase target is not imported as direct protein binding; its biosynthesis and human drug contexts are not interchangeable. DrugBank returned403 and LINCS retrieval failed SSL; Beilstein4173766 remains source-asserted. Wikipedia resolves as a document, not biological evidence. |
| ontology | CHEBI:15369; CHEBI:33281; ARO:3009657; ARO:3000741; Current OLS terms and inspected official ARO OBO cache | supports | Actinomycin family, antimicrobial role and nonribosomal peptide class fit the exact molecule. ARO transcription-complex DNA is a nucleic-acid component, not an enzyme. Official OBO targeted_by_antibiotic edge supports the native database qualification; the OBO cache matches the adopted manifest hash d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4. |
| adopted | PMID:2410919; DOI:10.1073/pnas.82.16.5328; all four original PMC390561 page scans visually read, OCR cross-checked | supports | The sole adopted paper proposes a model in which actinomycin binds premelted DNA and restrains transcription-complex motion. It synthesizes earlier structural/biochemical observations and states testable predictions; it is not a new direct drug-binding experiment or a contemporary drug-bound transcription-complex structure. The broad native DNA/RNA-synthesis definition is supported, while its detailed model must retain that evidential status. |
| binding | PMID:13948669; DOI:10.1073/pnas.48.12.2094; all eight original scans read by OCR, original p2096 figures visually inspected | supports | The 1962 experiments explicitly label actinomycin C1, a verified synonym of D. Spectral shifts measure DNA association; E.coli B RNA polymerase assays measure radiolabeled RNA synthesis with DNA primers of differing base composition. Guanine-containing DNA supports binding/inhibition, whereas synthetic dAT does not under the reported conditions. This supports DNA-mediated inhibition, not direct polymerase binding. The standard drug concentration calibration used an older preparation with inert material, so its nominal mass concentrations need that qualification. |
| activity | https://doi.org/10.3390/ijms222212231; PMC8621895 full main body, original Results2.1–2.2 and Methods4.1–4.3 | supports | Purified actinomycin D from cultured Streptomyces sp. SCAU-062, reported as S.parvulus by99.8% similarity to OUCMDZ-2554, is supported by NMR/MS and preparative separation. S.aureus ATCC25923 MIC2µg/mL was measured by24h MHB microdilution at37°C. Reported MBC64µg/mL exceeds the method-listed maximum32µg/mL; adjudicate that inconsistency before numeric MBC curation. Producer strain identification and cultivation details need preservation; do not substitute the comparator OUCMDZ strain. |
| omics | https://pmc.ncbi.nlm.nih.gov/articles/PMC8621895/; Full main Results, Discussion and Methods | context_only | Proteomics/metabolomics, DCFH fluorescence, peroxide and morphology report treatment responses. These do not establish direct binding to catalase, aconitase or other changed proteins, nor causal necessity of ROS. The paper contains mitochondrial language inappropriate to bacterial physiology and inconsistent metabolite significance thresholds; those interpretations should not be propagated. No raw omics reanalysis or verified accession is claimed. |
| fda | https://api.fda.gov/drug/drugsfda.json; Official application queries saved as078-fda-APPLICATION.json; compared every native product001 | supports | All seven original AP dates, application types/numbers, sponsor names, product names, ingredient and marketing statuses agree: NDA0506821964-12-10; ANDA0903042010-03-16;2025622013-08-23;2033852017-11-09;2039992019-05-20;2072322019-07-16;2134632020-11-13. First three are Discontinued; last four Prescription. These are dated regulatory/product assertions, not evidence of anti-infective approval or efficacy. Discontinuation is not inferred to be a safety withdrawal. |
| gsrs | https://gsrs.ncats.nih.gov/api/v1/substances/search?q=root_approvalID:1CC1JFE158; 078-gsrs.json, substance structure and record metadata | supports | Current GSRS UNII1CC1JFE158 version30 structure has the identical native full key, formula and ten assigned centres. Native version29 is explicitly dated2026-08-31 and is not false merely because the current record advanced. Small average-mass convention differences do not change identity. Exact-key source joining supports the native FDA substance assignment. |
| adapter | iModulonDB e_coli/precise1k; 078-imodulondb-transcription.txt and078-imodulondb-rpob.txt; inspected same-session dataset inventory | context_only | Structured adapter was attempted before web research because native definition names transcription. Broad transcription search exited2 on a malformed regulator value (NoneType rather than JSON list); no module result was usable. Narrow rpoB search succeeded with gene b3987 and zero modules. This contextual polymerase locus does not establish direct actinomycin binding, drug response or E.coli strain equivalence. |
| search | CultureBotAI/AntibioticMech; 078-local-hits.txt and078079-maintained-search.txt; bounded official and primary discovery | context_only | Ignored-inclusive searches found native/raw/queue references and a separate valinomycin research script mentioning actinomycin D as a comparator. No target-specific evidence upgrade was found in the examined maintained overlay. All adopted literature was dispositioned; free follow-up supplied original DNA-binding and antibacterial evidence. No exhaustive literature-absence claim. |

## Limits And Additional Notes

- Independent DrugBank/LINCS/Beilstein detail was unavailable; identifiers remain qualified source assertions. KEGG MOL files contain no assigned tetrahedral stereo despite the named exact-compound entry.
- Both original mechanism papers were read in scanned form, with OCR and key visual checks; no raw experimental data were reanalysed. The2021 full main text was read, but supplementary spectra/raw omics were not independently reinterpreted.
- The2021 MBC range and metabolite-threshold inconsistencies preclude unqualified quantitative/causal transfer. Other discovered FtsZ or actinomycin-congener studies remain leads, not assessed native claims.
- The structured broad query failed on malformed data; narrow locus context succeeded without module hits. Neither outcome establishes gene or mechanism absence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T083558Z-actinomycin-d-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Actinomycin D: exact identity, qualified DNA target and dated FDA assertions'
started_at: '2026-10-21T08:21:55Z'
finished_at: '2026-10-21T08:35:58Z'
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
summary: Exact actinomycin D identity and the broad DNA-mediated inhibition claim
  are supported. All seven dated FDA product assertions match current official records.
  The native target is correctly limited to a database assertion. Primary DNA-binding
  and antibacterial studies offer scoped enrichment; neither omics responses nor FDA
  approval establish clinical anti-infective efficacy. Scientific assessment retains
  the stated evidence limits; full verification is blocked by the shared native-library
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
  - path: data/antibiotics/antibacterial/actinomycin-d.yaml
    sha256: 977305fb760acc98fb3ab6a74e7b57d12e50ee936bd974800f642f688034951d
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
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
    role: context
  - path: scripts/extract_fda_clinical_status.py
    sha256: f30f385ea6d530dc1749e3d805dbcdbc8715fbc476abc510bf144ea13964e171
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
targets:
- target_id: CHEBI:27666
  path: data/antibiotics/antibacterial/actinomycin-d.yaml
  label: actinomycin D
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
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition, class and ARO chemical cross-references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Database-qualified DNA target edge
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Reviewed CARD target qualification
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Dated regulatory assertions and exact GSRS key join
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: FDA/GSRS identity extraction
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position078; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:27666
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:27666
  command: .venv/bin/python /private/tmp/am-review-session/focus008-root.py 78
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:27666
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/actinomycin-d.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:27666
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/actinomycin-d.yaml --out /private/tmp/am-review-session/078-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-transcription
  name: Structured transcription query
  status: failed
  required: false
  summary: Actual public query exited2 because a returned regulator field was NoneType;
    no module data adopted.
  exit_code: 2
  expected_exit_code: 0
  evidence_ids:
  - adapter
  target_ids:
  - CHEBI:27666
- check_id: adapter-rpob
  name: Narrow structured locus query
  status: passed
  required: false
  summary: One gene, zero modules; context only.
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
  target_ids:
  - CHEBI:27666
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:27666
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
  - CHEBI:27666
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
  - CHEBI:27666
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
  - CHEBI:27666
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
  - CHEBI:27666
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
  - CHEBI:27666
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
  - CHEBI:27666
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
  - CHEBI:27666
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
  - CHEBI:27666
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/actinomycin-d.yaml
  locator: Entire YAML, including all seven clinical assertions and seven history
    entries
  accessed_at: '2026-10-21T08:34:00Z'
  support: supports
  summary: SEEDED/EXACT neutral C62H86N12O16, seven synonyms including actinomycin
    C1 and IV, two parent classes, antimicrobial role, ARO/CHEBI source concepts,
    ten chemical/drug xrefs and one document xref. One NUCLEIC_ACID ATTACKED_COMPONENT
    target explicitly states DATABASE_ASSERTION_ONLY with no organism or strain. No
    quantitative activity, producer, resistance, causal graph or expression dataset
    is asserted.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv;
    data/raw/fda_clinical_status.tsv
  locator: Exact rows in 078-raw.json; seeder and FDA extractor inspected
  accessed_at: '2026-10-21T08:34:00Z'
  support: supports
  summary: Raw ChEBI row 499 and ARO row 192 merge consistently; target row 211 reproduces
    the qualified edge; seven FDA rows 2536–2542 join via exact GSRS InChIKey. Both
    source-specific SHA256 mints reproduce. No matching target upgrade exists in card_evidence_reviews.json
    (ignored-inclusive exact-ID search). All 20 captured maintained hashes remain
    unchanged.
  snapshot_sha256: 57eaa75ecbe8ca4596993cc8ffd272d795a6941d01759c8ab88b007531c6e6cd
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:27666
  locator: 078-chebi-visible.txt, current CARD ARO:3000696 page and official PubChem/ChEMBL/DrugCentral
    snapshots
  accessed_at: '2026-10-21T08:34:00Z'
  support: supports
  summary: Current ChEBI, PubChem CID457193, ChEMBL1554 and DrugCentral774 InChI all
    match RJURFGZVJUQBHK-IIXSONLDSA-N and the neutral formula. Current CARD label/definition
    and chemical grounding agree. Common names and CAS50-76-0 are corroborated. Independent
    registry access is not claimed.
  snapshot_sha256: 0e8e024639a53c9bbcb26fed5e19fa4ea8025ea9b6e6c52338d0e5a81ef3a7d9
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculation
  locator: 078-chemistry.json; explicit ChEMBL, DrugCentral and KEGG parsing
  accessed_at: '2026-10-21T08:34:00Z'
  support: supports
  summary: Both native encodings yield the same full key, one neutral fragment, all
    ten tetrahedral centres assigned, average mass1255.438 and exact mass1254.628474672.
    Both source mints reproduce. KEGG C06770 and D00214 MOL files reproduce connectivity
    but leave all ten centres unspecified (key suffix UHFFFAOYSA); their named entries
    support documentary identity, not independent stereochemical verification.
  snapshot_sha256: 43f2e2f447bbc12d8a8daeb56dd030367e0a2d8e0918bd197f00664ff87f8e0e
- evidence_id: xrefs
  kind: database
  reference: https://rest.kegg.jp/get/C06770
  locator: Both KEGG text/MOL entries; 078-drugcentral-inchi.txt; source registry
    links; Wikipedia document
  accessed_at: '2026-10-21T08:34:00Z'
  support: partial
  summary: KEGG compound and drug entries name actinomycin D/dactinomycin, share the
    native formula/CAS and cross-link ChEBI27666. DrugCentral explicit InChI matches
    exact stereo. The KEGG generic RNA-polymerase target is not imported as direct
    protein binding; its biosynthesis and human drug contexts are not interchangeable.
    DrugBank returned403 and LINCS retrieval failed SSL; Beilstein4173766 remains
    source-asserted. Wikipedia resolves as a document, not biological evidence.
  snapshot_sha256: 660beb1bccaeac225a223ded22d4f5082e99a1f1c46e845bb68d8c065e78b1c2
- evidence_id: ontology
  kind: authority
  reference: CHEBI:15369; CHEBI:33281; ARO:3009657; ARO:3000741
  locator: Current OLS terms and inspected official ARO OBO cache
  accessed_at: '2026-10-21T08:34:00Z'
  support: supports
  summary: Actinomycin family, antimicrobial role and nonribosomal peptide class fit
    the exact molecule. ARO transcription-complex DNA is a nucleic-acid component,
    not an enzyme. Official OBO targeted_by_antibiotic edge supports the native database
    qualification; the OBO cache matches the adopted manifest hash d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4.
- evidence_id: adopted
  kind: primary_source
  reference: PMID:2410919
  locator: DOI:10.1073/pnas.82.16.5328; all four original PMC390561 page scans visually
    read, OCR cross-checked
  accessed_at: '2026-10-21T08:34:00Z'
  support: supports
  summary: The sole adopted paper proposes a model in which actinomycin binds premelted
    DNA and restrains transcription-complex motion. It synthesizes earlier structural/biochemical
    observations and states testable predictions; it is not a new direct drug-binding
    experiment or a contemporary drug-bound transcription-complex structure. The broad
    native DNA/RNA-synthesis definition is supported, while its detailed model must
    retain that evidential status.
  snapshot_sha256: f9add79e41033c8425f96cd24655f4d1599347578727db98ac4eb0bf66d3878f
- evidence_id: binding
  kind: primary_source
  reference: PMID:13948669
  locator: DOI:10.1073/pnas.48.12.2094; all eight original scans read by OCR, original
    p2096 figures visually inspected
  accessed_at: '2026-10-21T08:34:00Z'
  support: supports
  summary: The 1962 experiments explicitly label actinomycin C1, a verified synonym
    of D. Spectral shifts measure DNA association; E.coli B RNA polymerase assays
    measure radiolabeled RNA synthesis with DNA primers of differing base composition.
    Guanine-containing DNA supports binding/inhibition, whereas synthetic dAT does
    not under the reported conditions. This supports DNA-mediated inhibition, not
    direct polymerase binding. The standard drug concentration calibration used an
    older preparation with inert material, so its nominal mass concentrations need
    that qualification.
  snapshot_sha256: c36f3ab51620404fbe670b1d10db067e47f0ec0d4f7ca092fb82e3cac80193c4
- evidence_id: activity
  kind: primary_source
  reference: https://doi.org/10.3390/ijms222212231
  locator: PMC8621895 full main body, original Results2.1–2.2 and Methods4.1–4.3
  accessed_at: '2026-10-21T08:34:00Z'
  support: supports
  summary: Purified actinomycin D from cultured Streptomyces sp. SCAU-062, reported
    as S.parvulus by99.8% similarity to OUCMDZ-2554, is supported by NMR/MS and preparative
    separation. S.aureus ATCC25923 MIC2µg/mL was measured by24h MHB microdilution
    at37°C. Reported MBC64µg/mL exceeds the method-listed maximum32µg/mL; adjudicate
    that inconsistency before numeric MBC curation. Producer strain identification
    and cultivation details need preservation; do not substitute the comparator OUCMDZ
    strain.
  snapshot_sha256: 2490875a513ea992e8550b90973a001366a37fe5a4b252a2a18df8670662d880
- evidence_id: omics
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8621895/
  locator: Full main Results, Discussion and Methods
  accessed_at: '2026-10-21T08:34:00Z'
  support: context_only
  summary: Proteomics/metabolomics, DCFH fluorescence, peroxide and morphology report
    treatment responses. These do not establish direct binding to catalase, aconitase
    or other changed proteins, nor causal necessity of ROS. The paper contains mitochondrial
    language inappropriate to bacterial physiology and inconsistent metabolite significance
    thresholds; those interpretations should not be propagated. No raw omics reanalysis
    or verified accession is claimed.
- evidence_id: fda
  kind: authority
  reference: https://api.fda.gov/drug/drugsfda.json
  locator: Official application queries saved as078-fda-APPLICATION.json; compared
    every native product001
  accessed_at: '2026-10-21T08:34:00Z'
  support: supports
  summary: 'All seven original AP dates, application types/numbers, sponsor names,
    product names, ingredient and marketing statuses agree: NDA0506821964-12-10; ANDA0903042010-03-16;2025622013-08-23;2033852017-11-09;2039992019-05-20;2072322019-07-16;2134632020-11-13.
    First three are Discontinued; last four Prescription. These are dated regulatory/product
    assertions, not evidence of anti-infective approval or efficacy. Discontinuation
    is not inferred to be a safety withdrawal.'
  snapshot_sha256: 8201beaacdbad5582ac0b5bb161cd91b18936133f705ed296d3fd2acaf0a8f1e
- evidence_id: gsrs
  kind: authority
  reference: https://gsrs.ncats.nih.gov/api/v1/substances/search?q=root_approvalID:1CC1JFE158
  locator: 078-gsrs.json, substance structure and record metadata
  accessed_at: '2026-10-21T08:34:00Z'
  support: supports
  summary: Current GSRS UNII1CC1JFE158 version30 structure has the identical native
    full key, formula and ten assigned centres. Native version29 is explicitly dated2026-08-31
    and is not false merely because the current record advanced. Small average-mass
    convention differences do not change identity. Exact-key source joining supports
    the native FDA substance assignment.
  snapshot_sha256: 665d417bdb0660dac96cd64a04dcb6758a36481043ae5c36662ad327836cfb71
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/precise1k
  locator: 078-imodulondb-transcription.txt and078-imodulondb-rpob.txt; inspected
    same-session dataset inventory
  accessed_at: '2026-10-21T08:34:00Z'
  support: context_only
  summary: Structured adapter was attempted before web research because native definition
    names transcription. Broad transcription search exited2 on a malformed regulator
    value (NoneType rather than JSON list); no module result was usable. Narrow rpoB
    search succeeded with gene b3987 and zero modules. This contextual polymerase
    locus does not establish direct actinomycin binding, drug response or E.coli strain
    equivalence.
  snapshot_sha256: e2a26428bb56d7c6ed13af138dc38346bde591c4cc94d4d98fc5d97896d0745e
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 078-local-hits.txt and078079-maintained-search.txt; bounded official and
    primary discovery
  accessed_at: '2026-10-21T08:34:00Z'
  support: context_only
  summary: Ignored-inclusive searches found native/raw/queue references and a separate
    valinomycin research script mentioning actinomycin D as a comparator. No target-specific
    evidence upgrade was found in the examined maintained overlay. All adopted literature
    was dispositioned; free follow-up supplied original DNA-binding and antibacterial
    evidence. No exhaustive literature-absence claim.
  search_scope: rg --no-ignore --hidden across isolated batch008 excluding .git/.venv;
    maintained follow-up curation/conf/scripts/data/raw/reports/yaml_record_review/reviews
    with .obo/.jsonl/.html excluded from that narrower follow-up. Current ChEBI/CARD/PubChem/ChEMBL/DrugCentral/KEGG/FDA/GSRS,
    EuropePMC and PMC originals.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral actinomycin D
  outcome: supported
  summary: Native chemistry, synonyms and full-key authorities agree; KEGG MOL stereo
    incompleteness is a source verification limitation.
  target_ids:
  - CHEBI:27666
  evidence_ids:
  - identity
  - chemistry
  - xrefs
- assessment_id: target
  area: evidence
  topic: DNA target and transcription
  outcome: supported
  summary: Database-only target qualification is truthful. Adopted model and independent
    primary DNA-binding experiments support the broad mechanism without asserting
    direct polymerase binding.
  target_ids:
  - CHEBI:27666
  evidence_ids:
  - native
  - ontology
  - adopted
  - binding
- assessment_id: roles
  area: grounding
  topic: Family and antimicrobial role
  outcome: supported
  summary: Structure fits parent classes; primary purified-compound bacterial activity
    supports antimicrobial classification.
  target_ids:
  - CHEBI:27666
  evidence_ids:
  - ontology
  - activity
- assessment_id: regulatory
  area: scope
  topic: Dated FDA approval assertions
  outcome: supported
  summary: All seven dated product assertions match official records; GSRS exact identity
    is corroborated. No antimicrobial clinical indication is inferred.
  target_ids:
  - CHEBI:27666
  evidence_ids:
  - fda
  - gsrs
- assessment_id: completeness
  area: completeness
  topic: Primary activity, mechanism and producer context
  outcome: unknown
  summary: Concrete evidence can enrich optional objects. MBC range discrepancy, producer
    strain identification and omics inference limitations require explicit qualification.
  target_ids:
  - CHEBI:27666
  evidence_ids:
  - binding
  - activity
  - omics
- assessment_id: ownership
  area: ownership
  topic: Imported fields and history
  outcome: supported
  summary: Captured CHEBI/ARO/FDA owners and deterministic mints reproduce; all source
    hashes and native status remain unchanged.
  target_ids:
  - CHEBI:27666
  evidence_ids:
  - owner
  - native
findings:
- finding_id: F1
  issue_key: actinomycin-d-scoped-primary-dna-activity-evidence
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Add scoped primary DNA-binding and antibacterial evidence
  description: The qualified database target is not an error. Original biochemical
    and purified-compound studies supply concrete optional primary evidence; keep
    the1985 model,1962 binding experiments and2021 downstream omics distinct.
  target_ids:
  - CHEBI:27666
  field_paths:
  - evidence
  - molecular_targets
  - activity_spectrum
  - producer_organisms
  - discussions
  evidence_ids:
  - adopted
  - binding
  - activity
  - omics
  rule_id: 'native-review-checklist: Evidence, Targets and Activity'
  native_severity: informational optional evidence enrichment
  normalization_reason: Optional blank collections alone are not defects; existing
    claims are supported with explicit evidence status.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/actinomycin-d.yaml
    role: Curated claim evidence via native validated writer/history
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained qualification of reviewed CARD target evidence
actions:
- action_id: A1
  description: Optionally curate precise original evidence without changing exact
    identity or generalizing regulatory approval.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:27666
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/actinomycin-d.yaml
    role: Curated claim evidence via native validated writer/history
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained qualification of reviewed CARD target evidence
  acceptance_checks:
  - Keep DNA as the attacked component; do not substitute rpoB or RNA polymerase as
    a demonstrated directly bound protein. Preserve the1985 model status and1962 drug
    calibration limitation.
  - For2021 MIC preserve ATCC25923, MHB,24h,37°C and exact purified material. Resolve
    MBC64 versus maximum listed32 before importing MBC.
  - Retain SCAU-062 producer identity/taxonomy evidence; do not swap in its closest
    sequence comparator. Treat omics changes as response associations, not direct
    enzyme targets or bacterial mitochondrial processes.
  - Use write_validated_antibiotic and record_curation_event, maintain CARD qualification
    consistently, and run required gates. Retain dated FDA assertions without implying
    clinical anti-infective use.
limitations:
- Independent DrugBank/LINCS/Beilstein detail was unavailable; identifiers remain
  qualified source assertions. KEGG MOL files contain no assigned tetrahedral stereo
  despite the named exact-compound entry.
- Both original mechanism papers were read in scanned form, with OCR and key visual
  checks; no raw experimental data were reanalysed. The2021 full main text was read,
  but supplementary spectra/raw omics were not independently reinterpreted.
- The2021 MBC range and metabolite-threshold inconsistencies preclude unqualified
  quantitative/causal transfer. Other discovered FtsZ or actinomycin-congener studies
  remain leads, not assessed native claims.
- The structured broad query failed on malformed data; narrow locus context succeeded
  without module hits. Neither outcome establishes gene or mechanism absence.
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
