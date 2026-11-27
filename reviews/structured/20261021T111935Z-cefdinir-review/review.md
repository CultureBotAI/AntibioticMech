# Cefdinir: replace an iclaprim ChEMBL cross-reference and retain assay-specific PBP evidence

- Review: 20261021T111935Z-cefdinir-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:55:31Z
- Finished UTC: 2026-10-21T11:19:35Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native cefdinir structure is coherent, but its imported CHEMBL134561 exact cross-reference resolves to iclaprim. CHEMBL927 is an independently verified matching candidate. The FDA assertions are reproducible, and current application tables corroborate the retained dates and marketing statuses. Primary PBP competition and resistance-association studies provide bounded enrichment without making the existing database claims primary evidence.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 218; one exact record in path order, captured before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3485 | data/antibiotics/antibacterial/cefdinir.yaml | generated | cefdinir |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:3485 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:3485 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:3485 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:3485 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3485 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3485 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3485 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3485 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3485 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3485 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3485 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3485 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Maintained ownership and source history

provenance: supported. Targets: CHEBI:3485.

Source concepts, minted identifiers and history are coherent. Source-origin corrections require regeneration; new primary observations require the validated native writer and curation event.

### Focused native gates

schema: supported. Targets: CHEBI:3485.

Documented schema/strict checks and independent native chemistry pass. These do not validate every external cross-reference or confer scientific sign-off.

### Exact cross-reference set

grounding: concern. Targets: CHEBI:3485.

Native chemical identity, synonyms and broader classification are coherent; one ARO-derived exact ChEMBL reference instead denotes iclaprim.

### Historical FDA assertions and current source corroboration

evidence: supported. Targets: CHEBI:3485.

All 21 maintained assertions reproduce, with exact UNII identity and current application-table checks. Discontinued status does not alone mean approval withdrawal; prescription listings do not establish every real-world supply condition.

### PBP family and PBP3 resistance scope

evidence: supported. Targets: CHEBI:3485.

Native target PRIMARY_EVIDENCE_NEEDED and resistance database caveats are honest. Original competition measurements support narrow future target enrichment; clinical-isolate correlation is a separate type of evidence.

### Exact activity, material and endpoint

quantity: supported. Targets: CHEBI:3485.

Original assays and abstracts support the antibacterial role; their strain, medium, endpoint and censored values must remain explicit. No universal species MIC or all-enzyme stability is asserted.

### Primary observations, producer and causal graph

completeness: unknown. Targets: CHEBI:3485.

Optional primary targets/activity may be added after evidence curation. No natural producer or complete downstream causal chain is established merely by class membership.

## Findings

### F1: Replace the iclaprim ChEMBL accession in cefdinir’s exact xrefs

major / open / confirmed; issue key: cefdinir-iclaprim-chembl-cross-reference.

Native chembl:CHEMBL134561 resolves to an unrelated diaminopyrimidine compound, iclaprim, while all native structure fields describe cefdinir. The adopted ARO row supplies the wrong link. CHEMBL927 has the exact cefdinir structure. Other wrong ARO-row identifiers were not imported into this native record and are not separate native findings.

## Recommended Actions And Acceptance Checks

### A1

Replace the iclaprim ChEMBL accession in cefdinir’s exact xrefs

- Suppress or replace only the erroneous exact ChEMBL mapping through a maintained source or grounding decision; independently reconfirm CHEMBL927 before adoption.
- Preserve native cefdinir structure, exact source concepts and unrelated correct xrefs. Verify that reseeding cannot restore CHEMBL134561 to cefdinir.
- Implement through a maintained source/extraction/decision correction and regenerate; preserve original provenance and inspect the exact diff. Do not patch generated YAML alone.
- Run focused schema/strict and independent chemistry, verify-corpus, and applicable shared gates after any separately authorized correction.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cefdinir.yaml; Complete YAML, including all source concepts and history events. | supports | Read every native field and retained assertion. This review does not change the generated record or promote SEEDED status. |
| source | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv; data/raw/aro_resistance_edges.tsv; conf/aro_target_roles.tsv; data/raw/fda_clinical_status.tsv; Exact maintained rows in 218-raw-rows.json; applicable extraction, join and seeding code. | supports | The maintained rows reproduce the native source-owned content. Initial input hashes are retained; actual additional owners were appended from a supplemental capture before detailed judgment. Corrections belong at the reproducible source/decision boundary. |
| chemistry | 218-chemistry.json; 217-220-external-chemistry.json; Independent RDKit parse of native SMILES/InChI and inspected official structures. | supports | Native encodings reproduce RTXOFQZKPXMALH-GHXIOONMSA-N, C14H13N5O5S2, charge 0, masses and two R centres. Oxime geometry is Z. The batch019 interpreter operated on unchanged batch022 inputs because batch022 has no RDKit. |
| search | 218-local-hits.txt; 218-owner-hits.txt; Exact identifier, label, key and slug; hidden and ignored files included. | supports | The complete native record, maintained inputs, generated references and related chemical forms were distinguished. No exact corrective decision was identified in the inspected maintained inputs. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:3485; https://pubchem.ncbi.nlm.nih.gov/compound/6915944; https://rest.kegg.jp/get/C08110; https://rest.kegg.jp/get/D00917; ChEBI and PubChem identities; independently parsed KEGG compound/drug MOLs. | supports | The native acid, two R centres and Z oxime agree across these sources, CAS 91832-40-5 resolution and DrugCentral 533 raw InChI/SMILES. The cephalosporin and ketoxime parents fit the graph. Beilstein 6829362 remains source-attested; DrugBank DB00535 returned 403. |
| wrong-chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL134561.json; Current molecule identity and independently parsed structure. | refutes | CHEMBL134561 is iclaprim, C19H22N4O3, full key HWJPWWYTGBZDEG-UHFFFAOYSA-N. This is unrelated connectivity and composition, not a cefdinir salt or tautomer. The erroneous link is present in the exact adopted ARO:3000650 row and propagated to native xrefs. |
| replacement | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL927.json; Current cefdinir structure independently parsed. | supports | CHEMBL927 reproduces the native complete key RTXOFQZKPXMALH-GHXIOONMSA-N, formula, charge, stereocentres and Z oxime. It is a verified candidate for a maintained grounding correction, not a correction applied by this review. |
| regulatory | https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&amp;ApplNo=050739; data/raw/fda_clinical_status.tsv; All 21 native assertions and source rows; current product and ORIG action tables for all 14 named applications, stored in 218-current-fda-comparison.json. | supports | Three retained Omnicef products are discontinued and 18 generic products have Prescription status. Current product counts, statuses and original approval dates agree with the retained records. The Omnicef pages explicitly note a Federal Register determination that discontinuation was not for safety/effectiveness. Historical approval and marketing availability remain separate; this review does not establish worldwide status or the timing of every formulation supplement. |
| gsrs | https://gsrs.ncats.nih.gov/api/v1/substances/search?q=root_approvalID:CI0FAO63WC; Current GSRS v44 compared with captured native v41 and independent raw DrugCentral structures. | supports | The UNII maps to the exact native graph and formula. Current version changes do not invalidate the preserved dated v41 provenance. A UNII is identity support, not standalone regulatory approval. |
| activity | PMID:8026155; DOI:10.1016/0732-8893(94)90131-7; Complete adopted abstract and metadata. | supports | The study explicitly equates FK482 and cefdinir, using microbroth dilution across clinical panels and selected beta-lactamase-producing S. aureus strains. MIC90s are population summaries; inoculum and enzyme-type results do not support a universal beta-lactamase-stability claim. The native structural definition does not import the ARO phagocytosis wording. |
| pbp-primary | PMID:3264828; DOI:10.7164/antibiotics.41.1873; https://www.jstage.jst.go.jp/article/antibiotics1968/41/12/41_12_1873/_pdf; Original pp1873–1875 Methods, pp1884–1886 relevant Results/Discussion; Table 8 p1884 visually inspected. | supports | FK482 is the matching acid structure and laboratory-supplied material. Table 8 reports concentrations reducing 14C-benzylpenicillin binding by 50%, not equilibrium Kd: S. aureus 209P JC-1 PBP1/2/3 values 0.58/0.17/0.12 µg/mL; E. coli NIHJ JC-2 PBP1a/1bs/3 values 0.09/2.3/0.07. E. faecalis FP183 PBP2/3 values are censored &lt;0.2. The modified Spratt protocol refers to an earlier method; preserve that access limit before full numerical adoption. Agar MIC, broth MBC, time-kill, permeability and hydrolysis are distinct endpoints. Bulk hydrate/solid form was not independently specified. |
| resistance-primary | PMID:29352811; DOI:10.1186/s13104-018-3169-0; PMC5775570; Complete original XML body: Methods, Results, Figure 2 caption and limitations; supplements not audited. | supports | Japanese clinical isolates were screened by broth dilution with the cited 2015 CLSI method; 27 genomes completed the PBP comparison. Figure 2c concerns cefdinir. Linked ftsI substitutions correlate with MIC differences, but the authors cannot isolate each substitution’s causal contribution. This supports a qualified PBP3 association, not direct cefdinir binding, a single mutation effect or a modern breakpoint. Original cefaclor transformant results from other papers were not transferred. |
| context | PMID:3055170; PMID:11585791; PMID:15673804; PMID:6810737; All four remaining target/parent leads, available complete abstracts or metadata. | supports | 3055170 is a PBP review and 11585791 an ESBL review. The other two parent leads have no indexed abstracts. They provide broad context, not a new cefdinir-specific experiment. |
| documents | https://patents.google.com/patent/BE897864A/en; https://patents.google.com/patent/US4559334A/en; Both native patent titles, metadata and abstracts. | supports | Both documents concern 7-substituted 3-vinyl cephem compounds and broad protected/unprotected or salt variants. Their document relevance is supported, but every synthetic example was not audited and no assay is imported from them. The Wikipedia route returned 403. |
| adapter | 218-220-adapter-catalog.txt; 218-220-adapter-ftsi.txt; 218-220-adapter-pbp.txt; Structured imodulondb catalog and E. coli modulome searches before web research. | supports | The catalog has no H. influenzae dataset. E. coli ftsI returns b0084 and the penicillin search returns yfeW/b2430; neither returns an iModulon to summarize. These annotations do not establish drug binding or transfer a resistance phenotype between taxa. Commands used kg-microbe-sources imodulondb --timeout 15 datasets, then search --organism e_coli --dataset modulome --query ftsI and --query penicillin; all exited 0. |

## Limits And Additional Notes

- No paid registry or research service was used. An inaccessible document is an explicit verification limit, not evidence that the document or biological effect does not exist.
- All six adopted/target/parent MED lead dispositions were inspected; two have metadata only. The 1994 activity study remains abstract-level.
- Original 1988 Methods and relevant PBP/other assay Results were inspected; not every susceptibility-table cell or figure point was audited. Table 8 was checked visually. The prior referenced Spratt modification and supplied solid form remain limits.
- The 2018 resistance article’s original body was inspected; supplements and Figure 2 plot points were not independently extracted. Association is not mutation-isolated causality.
- Beilstein and DrugBank contents remain independently unverified, and Wikipedia was unavailable. Patent inspection was metadata/abstract-level.
- All FDA native/source assertions were checked; live web comparison covers application product counts, marketing statuses and original dates, not a comprehensive regulatory-event or worldwide product audit.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T111935Z-cefdinir-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefdinir: replace an iclaprim ChEMBL cross-reference and retain assay-specific
  PBP evidence'
started_at: '2026-10-21T10:55:31Z'
finished_at: '2026-10-21T11:19:35Z'
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
summary: The native cefdinir structure is coherent, but its imported CHEMBL134561
  exact cross-reference resolves to iclaprim. CHEMBL927 is an independently verified
  matching candidate. The FDA assertions are reproducible, and current application
  tables corroborate the retained dates and marketing statuses. Primary PBP competition
  and resistance-association studies provide bounded enrichment without making the
  existing database claims primary evidence.
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
  - path: data/antibiotics/antibacterial/cefdinir.yaml
    sha256: 66e4f6adc52ab29270876031784aee8aa6f1d1cebf36e8a493373029d03f5113
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
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
    role: context
  - path: scripts/extract_fda_clinical_status.py
    sha256: f30f385ea6d530dc1749e3d805dbcdbc8715fbc476abc510bf144ea13964e171
    role: context
targets:
- target_id: CHEBI:3485
  path: data/antibiotics/antibacterial/cefdinir.yaml
  label: cefdinir
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
    role: Adopted ARO compound identity and reference leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted PBP target edge
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted PBP3 resistance edge
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target role mapping
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Imported-claim adjudication searched
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Claim-review merge implementation
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Adopted exact-key FDA product assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Product regulatory extraction and GSRS exact join
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 218; one exact record in path order,
    captured before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3485
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3485
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    218
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3485
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefdinir.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3485
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefdinir.yaml --out /private/tmp/am-review-session/218-strict.tsv
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
  - CHEBI:3485
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
  - CHEBI:3485
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
  - CHEBI:3485
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
  - CHEBI:3485
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
  - CHEBI:3485
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
  - CHEBI:3485
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
  - CHEBI:3485
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
  - CHEBI:3485
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
  - CHEBI:3485
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cefdinir.yaml
  locator: Complete YAML, including all source concepts and history events.
  accessed_at: '2026-10-21T11:13:13Z'
  support: supports
  summary: Read every native field and retained assertion. This review does not change
    the generated record or promote SEEDED status.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv;
    data/raw/aro_resistance_edges.tsv; conf/aro_target_roles.tsv; data/raw/fda_clinical_status.tsv
  locator: Exact maintained rows in 218-raw-rows.json; applicable extraction, join
    and seeding code.
  accessed_at: '2026-10-21T11:13:13Z'
  support: supports
  summary: The maintained rows reproduce the native source-owned content. Initial
    input hashes are retained; actual additional owners were appended from a supplemental
    capture before detailed judgment. Corrections belong at the reproducible source/decision
    boundary.
  snapshot_sha256: 5282fae1850ec2eec508603c918f8f4b80a80b53e79502a1321a20773520f2a1
- evidence_id: chemistry
  kind: validation
  reference: 218-chemistry.json; 217-220-external-chemistry.json
  locator: Independent RDKit parse of native SMILES/InChI and inspected official structures.
  accessed_at: '2026-10-21T11:13:13Z'
  support: supports
  summary: Native encodings reproduce RTXOFQZKPXMALH-GHXIOONMSA-N, C14H13N5O5S2, charge
    0, masses and two R centres. Oxime geometry is Z. The batch019 interpreter operated
    on unchanged batch022 inputs because batch022 has no RDKit.
  snapshot_sha256: 172d479791c82d57b5cc3c95343be4e3e51360eca4842240e2983a0be6eea779
- evidence_id: search
  kind: search
  reference: 218-local-hits.txt; 218-owner-hits.txt
  locator: Exact identifier, label, key and slug; hidden and ignored files included.
  accessed_at: '2026-10-21T11:13:13Z'
  support: supports
  summary: The complete native record, maintained inputs, generated references and
    related chemical forms were distinguished. No exact corrective decision was identified
    in the inspected maintained inputs.
  search_scope: rg --no-ignore --hidden across the isolated worktree, excluding .git
    and .venv internals; exact identifier, label, slug and full-key searches.
  snapshot_sha256: f8b8ed79e2d0ce248f6318d1118ebcfc9f4d664067a5e2cc3475ef325e3d8f42
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3485; https://pubchem.ncbi.nlm.nih.gov/compound/6915944;
    https://rest.kegg.jp/get/C08110; https://rest.kegg.jp/get/D00917
  locator: ChEBI and PubChem identities; independently parsed KEGG compound/drug MOLs.
  accessed_at: '2026-10-21T11:13:13Z'
  support: supports
  summary: The native acid, two R centres and Z oxime agree across these sources,
    CAS 91832-40-5 resolution and DrugCentral 533 raw InChI/SMILES. The cephalosporin
    and ketoxime parents fit the graph. Beilstein 6829362 remains source-attested;
    DrugBank DB00535 returned 403.
  snapshot_sha256: 3c6f5e9ab811943fb581daa858c7c833b6c2a5d2abd1e1fd0b4c550f31066d62
- evidence_id: wrong-chembl
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL134561.json
  locator: Current molecule identity and independently parsed structure.
  accessed_at: '2026-10-21T11:13:13Z'
  support: refutes
  summary: CHEMBL134561 is iclaprim, C19H22N4O3, full key HWJPWWYTGBZDEG-UHFFFAOYSA-N.
    This is unrelated connectivity and composition, not a cefdinir salt or tautomer.
    The erroneous link is present in the exact adopted ARO:3000650 row and propagated
    to native xrefs.
  snapshot_sha256: 1f1db1beb4cc71d30a857b2df961326b78250bdd86434d6ff5b16dac1881ae21
- evidence_id: replacement
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL927.json
  locator: Current cefdinir structure independently parsed.
  accessed_at: '2026-10-21T11:13:13Z'
  support: supports
  summary: CHEMBL927 reproduces the native complete key RTXOFQZKPXMALH-GHXIOONMSA-N,
    formula, charge, stereocentres and Z oxime. It is a verified candidate for a maintained
    grounding correction, not a correction applied by this review.
  snapshot_sha256: 75c63cba54ffb78765525a6fe68ab82c02c75be7ce66555db545ec2476dfdf0f
- evidence_id: regulatory
  kind: authority
  reference: https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=050739;
    data/raw/fda_clinical_status.tsv
  locator: All 21 native assertions and source rows; current product and ORIG action
    tables for all 14 named applications, stored in 218-current-fda-comparison.json.
  accessed_at: '2026-10-21T11:13:13Z'
  support: supports
  summary: Three retained Omnicef products are discontinued and 18 generic products
    have Prescription status. Current product counts, statuses and original approval
    dates agree with the retained records. The Omnicef pages explicitly note a Federal
    Register determination that discontinuation was not for safety/effectiveness.
    Historical approval and marketing availability remain separate; this review does
    not establish worldwide status or the timing of every formulation supplement.
  snapshot_sha256: fc985766c5b44cbeae1dd761d15ff596daf81f698171c3c951158df0110a616c
- evidence_id: gsrs
  kind: authority
  reference: https://gsrs.ncats.nih.gov/api/v1/substances/search?q=root_approvalID:CI0FAO63WC
  locator: Current GSRS v44 compared with captured native v41 and independent raw
    DrugCentral structures.
  accessed_at: '2026-10-21T11:13:13Z'
  support: supports
  summary: The UNII maps to the exact native graph and formula. Current version changes
    do not invalidate the preserved dated v41 provenance. A UNII is identity support,
    not standalone regulatory approval.
  snapshot_sha256: d608f801586c68fddc05b17f254ec0a931dce5ce97583cb173abefed4ecaa1b0
- evidence_id: activity
  kind: primary_source
  reference: PMID:8026155; DOI:10.1016/0732-8893(94)90131-7
  locator: Complete adopted abstract and metadata.
  accessed_at: '2026-10-21T11:13:13Z'
  support: supports
  summary: The study explicitly equates FK482 and cefdinir, using microbroth dilution
    across clinical panels and selected beta-lactamase-producing S. aureus strains.
    MIC90s are population summaries; inoculum and enzyme-type results do not support
    a universal beta-lactamase-stability claim. The native structural definition does
    not import the ARO phagocytosis wording.
  snapshot_sha256: a81eece5b7ba621615edd41abacb7b81b26785ca7e2d96e1ac3f29c8fd319b2a
- evidence_id: pbp-primary
  kind: primary_source
  reference: PMID:3264828; DOI:10.7164/antibiotics.41.1873; https://www.jstage.jst.go.jp/article/antibiotics1968/41/12/41_12_1873/_pdf
  locator: Original pp1873–1875 Methods, pp1884–1886 relevant Results/Discussion;
    Table 8 p1884 visually inspected.
  accessed_at: '2026-10-21T11:13:13Z'
  support: supports
  summary: 'FK482 is the matching acid structure and laboratory-supplied material.
    Table 8 reports concentrations reducing 14C-benzylpenicillin binding by 50%, not
    equilibrium Kd: S. aureus 209P JC-1 PBP1/2/3 values 0.58/0.17/0.12 µg/mL; E. coli
    NIHJ JC-2 PBP1a/1bs/3 values 0.09/2.3/0.07. E. faecalis FP183 PBP2/3 values are
    censored <0.2. The modified Spratt protocol refers to an earlier method; preserve
    that access limit before full numerical adoption. Agar MIC, broth MBC, time-kill,
    permeability and hydrolysis are distinct endpoints. Bulk hydrate/solid form was
    not independently specified.'
  snapshot_sha256: 3a138214c9a980d69a771ec29ee425b2f906e5b6333e5afda35ce4c20fc6e599
- evidence_id: resistance-primary
  kind: primary_source
  reference: PMID:29352811; DOI:10.1186/s13104-018-3169-0; PMC5775570
  locator: 'Complete original XML body: Methods, Results, Figure 2 caption and limitations;
    supplements not audited.'
  accessed_at: '2026-10-21T11:13:13Z'
  support: supports
  summary: Japanese clinical isolates were screened by broth dilution with the cited
    2015 CLSI method; 27 genomes completed the PBP comparison. Figure 2c concerns
    cefdinir. Linked ftsI substitutions correlate with MIC differences, but the authors
    cannot isolate each substitution’s causal contribution. This supports a qualified
    PBP3 association, not direct cefdinir binding, a single mutation effect or a modern
    breakpoint. Original cefaclor transformant results from other papers were not
    transferred.
  snapshot_sha256: d74da6e4fb573e9c9b85f77c6ff2cf8392fc68008b8510e2325c4b3c514fad03
- evidence_id: context
  kind: database
  reference: PMID:3055170; PMID:11585791; PMID:15673804; PMID:6810737
  locator: All four remaining target/parent leads, available complete abstracts or
    metadata.
  accessed_at: '2026-10-21T11:13:13Z'
  support: supports
  summary: 3055170 is a PBP review and 11585791 an ESBL review. The other two parent
    leads have no indexed abstracts. They provide broad context, not a new cefdinir-specific
    experiment.
  snapshot_sha256: a81eece5b7ba621615edd41abacb7b81b26785ca7e2d96e1ac3f29c8fd319b2a
- evidence_id: documents
  kind: primary_source
  reference: https://patents.google.com/patent/BE897864A/en; https://patents.google.com/patent/US4559334A/en
  locator: Both native patent titles, metadata and abstracts.
  accessed_at: '2026-10-21T11:13:13Z'
  support: supports
  summary: Both documents concern 7-substituted 3-vinyl cephem compounds and broad
    protected/unprotected or salt variants. Their document relevance is supported,
    but every synthetic example was not audited and no assay is imported from them.
    The Wikipedia route returned 403.
  snapshot_sha256: 671fc22a3a411aecdd620d81c40665c9790daf4569a0982f0571e8cdd0f9bf0d
- evidence_id: adapter
  kind: database
  reference: 218-220-adapter-catalog.txt; 218-220-adapter-ftsi.txt; 218-220-adapter-pbp.txt
  locator: Structured imodulondb catalog and E. coli modulome searches before web
    research.
  accessed_at: '2026-10-21T11:13:13Z'
  support: supports
  summary: The catalog has no H. influenzae dataset. E. coli ftsI returns b0084 and
    the penicillin search returns yfeW/b2430; neither returns an iModulon to summarize.
    These annotations do not establish drug binding or transfer a resistance phenotype
    between taxa. Commands used kg-microbe-sources imodulondb --timeout 15 datasets,
    then search --organism e_coli --dataset modulome --query ftsI and --query penicillin;
    all exited 0.
  snapshot_sha256: 7f0b269b42a3322605c5af4032a57edb95808ac6c7c09f1b48cf364404fe84ad
assessments:
- assessment_id: provenance
  area: provenance
  topic: Maintained ownership and source history
  outcome: supported
  summary: Source concepts, minted identifiers and history are coherent. Source-origin
    corrections require regeneration; new primary observations require the validated
    native writer and curation event.
  target_ids:
  - CHEBI:3485
  evidence_ids:
  - record
  - source
  - search
- assessment_id: checks
  area: schema
  topic: Focused native gates
  outcome: supported
  summary: Documented schema/strict checks and independent native chemistry pass.
    These do not validate every external cross-reference or confer scientific sign-off.
  target_ids:
  - CHEBI:3485
  evidence_ids:
  - chemistry
- assessment_id: identity
  area: grounding
  topic: Exact cross-reference set
  outcome: concern
  summary: Native chemical identity, synonyms and broader classification are coherent;
    one ARO-derived exact ChEMBL reference instead denotes iclaprim.
  target_ids:
  - CHEBI:3485
  evidence_ids:
  - identity
  - chemistry
  - wrong-chembl
  - replacement
  - source
- assessment_id: clinical
  area: evidence
  topic: Historical FDA assertions and current source corroboration
  outcome: supported
  summary: All 21 maintained assertions reproduce, with exact UNII identity and current
    application-table checks. Discontinued status does not alone mean approval withdrawal;
    prescription listings do not establish every real-world supply condition.
  target_ids:
  - CHEBI:3485
  evidence_ids:
  - regulatory
  - gsrs
  - source
- assessment_id: target
  area: evidence
  topic: PBP family and PBP3 resistance scope
  outcome: supported
  summary: Native target PRIMARY_EVIDENCE_NEEDED and resistance database caveats are
    honest. Original competition measurements support narrow future target enrichment;
    clinical-isolate correlation is a separate type of evidence.
  target_ids:
  - CHEBI:3485
  evidence_ids:
  - record
  - pbp-primary
  - resistance-primary
  - context
  - adapter
- assessment_id: activity
  area: quantity
  topic: Exact activity, material and endpoint
  outcome: supported
  summary: Original assays and abstracts support the antibacterial role; their strain,
    medium, endpoint and censored values must remain explicit. No universal species
    MIC or all-enzyme stability is asserted.
  target_ids:
  - CHEBI:3485
  evidence_ids:
  - activity
  - pbp-primary
- assessment_id: optional
  area: completeness
  topic: Primary observations, producer and causal graph
  outcome: unknown
  summary: Optional primary targets/activity may be added after evidence curation.
    No natural producer or complete downstream causal chain is established merely
    by class membership.
  target_ids:
  - CHEBI:3485
  evidence_ids:
  - record
  - pbp-primary
  - documents
findings:
- finding_id: F1
  issue_key: cefdinir-iclaprim-chembl-cross-reference
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Replace the iclaprim ChEMBL accession in cefdinir’s exact xrefs
  description: Native chembl:CHEMBL134561 resolves to an unrelated diaminopyrimidine
    compound, iclaprim, while all native structure fields describe cefdinir. The adopted
    ARO row supplies the wrong link. CHEMBL927 has the exact cefdinir structure. Other
    wrong ARO-row identifiers were not imported into this native record and are not
    separate native findings.
  target_ids:
  - CHEBI:3485
  field_paths:
  - xrefs[4]
  evidence_ids:
  - wrong-chembl
  - replacement
  - identity
  - chemistry
  - source
  rule_id: 'native-review-checklist: exact chemical identity, accurate names and source-supported
    references'
  native_severity: major
  normalization_reason: Severity reflects the specific confirmed field error; coherent
    native identity is retained where independently supported.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO cross-reference assertion
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained exact-grounding correction or suppression
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerate the joined exact record
actions:
- action_id: A1
  description: Replace the iclaprim ChEMBL accession in cefdinir’s exact xrefs
  finding_ids:
  - F1
  target_ids:
  - CHEBI:3485
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO cross-reference assertion
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained exact-grounding correction or suppression
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerate the joined exact record
  acceptance_checks:
  - Suppress or replace only the erroneous exact ChEMBL mapping through a maintained
    source or grounding decision; independently reconfirm CHEMBL927 before adoption.
  - Preserve native cefdinir structure, exact source concepts and unrelated correct
    xrefs. Verify that reseeding cannot restore CHEMBL134561 to cefdinir.
  - Implement through a maintained source/extraction/decision correction and regenerate;
    preserve original provenance and inspect the exact diff. Do not patch generated
    YAML alone.
  - Run focused schema/strict and independent chemistry, verify-corpus, and applicable
    shared gates after any separately authorized correction.
limitations:
- No paid registry or research service was used. An inaccessible document is an explicit
  verification limit, not evidence that the document or biological effect does not
  exist.
- All six adopted/target/parent MED lead dispositions were inspected; two have metadata
  only. The 1994 activity study remains abstract-level.
- Original 1988 Methods and relevant PBP/other assay Results were inspected; not every
  susceptibility-table cell or figure point was audited. Table 8 was checked visually.
  The prior referenced Spratt modification and supplied solid form remain limits.
- The 2018 resistance article’s original body was inspected; supplements and Figure
  2 plot points were not independently extracted. Association is not mutation-isolated
  causality.
- Beilstein and DrugBank contents remain independently unverified, and Wikipedia was
  unavailable. Patent inspection was metadata/abstract-level.
- All FDA native/source assertions were checked; live web comparison covers application
  product counts, marketing statuses and original dates, not a comprehensive regulatory-event
  or worldwide product audit.
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
