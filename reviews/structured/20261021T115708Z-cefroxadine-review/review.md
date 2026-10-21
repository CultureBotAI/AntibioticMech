# Cefroxadine: exact neutral structure and primary activity with a dihydrate boundary

- Review: 20261021T115708Z-cefroxadine-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:39:24Z
- Finished UTC: 2026-10-21T11:57:08Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No confirmed defect. The 6R,7R,side-chain 2R structure and accessible exact mappings agree. The original antibacterial/PBP paper directly supports activity but depicts a dihydrate; the native anhydrous representation must not silently inherit that material or concentration basis. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 248; one exact record in path order, initial captures retained and actual ARO/PubChem owners appended before detailed assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:31379 | data/antibiotics/antibacterial/cefroxadine.yaml | generated | cefroxadine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:31379 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:31379 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:31379 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:31379 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:31379 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:31379 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:31379 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:31379 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:31379 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:31379 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:31379 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:31379 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Antibacterial role and tested material

evidence: supported. Targets: CHEBI:31379.

Direct original experiments support antibacterial activity; Figure 1 explicitly depicts dihydrate, and the preparation notice gives an anhydrous potency basis for its own material. No exact-form MIC is populated in native.

### Bounded PBP and hydrolysis enrichment

evidence: supported. Targets: CHEBI:31379.

Original competition and substrate assays are useful future evidence with strain, material and assay context. Their absence from optional native fields is not a defect.

### Exact molecular identity

identity: supported. Targets: CHEBI:31379.

Native structure, names and accessible independent exact mappings agree on configuration, composition and form.

### Filing and role scope

grounding: supported. Targets: CHEBI:31379.

Compound-specific original antibacterial evidence and resolved classes support filing. Source class prose does not establish universal susceptibility.

### Owner captures, references and history

provenance: supported. Targets: CHEBI:31379.

All initial input hashes remain unchanged; actual maintained owners were appended and original captures preserved. All native source references were resolved or given access limits; history is seeding rather than scientific sign-off.

### Optional structured evidence

completeness: supported. Targets: CHEBI:31379.

No native activity/target/resistance/producer/dataset/clinical object is present. Optional blanks alone do not require edits; inspected research is bounded to its tested material and evidence type.

### Structured adapter applicability

scope: not_applicable. Targets: CHEBI:31379.

The native record names no gene, protein, regulator, pathway, stress response or expression dataset. Primary mechanism opportunities were discovered subsequently; generic expression-module catalog hits are not needed to validate the native populated claims.

### Native deterministic checks

schema: supported. Targets: CHEBI:31379.

Focused schema/strict and supplemental native chemistry exited 0; mandatory shared gates are integrated by the coordinator separately.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cefroxadine.yaml; Entire native YAML | supports | Read every identity, class, definition, molecular field, source concept, xref and seed/reseed event. Seven synonyms and four history events; no MIC observations, target, resistance, clinical, producer, dataset or causal graph is populated. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/chebi_antimicrobials.tsv; data/raw/pubchem_structures.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; 248-raw-rows.json and original/expanded captures | supports | Actual maintained rows were read. ChEBI owns identity, definition, chemistry, role and four PMID leads; ARO supplies a synonym, class and PMID 6998373. All five adopted compound leads are dispositioned. |
| chemistry | RDKit 2026.03.5; 248-chemistry.json and focused command ledger | supports | Both native encodings reproduce the complete stored key, elemental composition, charge, masses within their stated precision and deterministic source mints. Three R centres are retained: core 6R,7R and side-chain 2R. The 1,4-cyclohexadiene ring and 3-methoxy group agree with names/definition. No water component is encoded. |
| exact-authorities | CHEBI:31379; PubChem:5284529; ChEMBL:CHEMBL3186538; KEGG:C12979; ARO:3009113; 248-pubchem.json, 248-chembl.json, 248-aro.html; 247-248-external-chemistry.json | supports | Independent PubChem and ChEMBL SMILES/molfile comparisons reproduce the native complete key and chirality-aware graph. Current ChEBI matches all chemistry; both KEGG compound and drug molfiles independently reproduce the native graph/key. Current ARO retains the same identifiers and graph. |
| classification | CHEBI:23066; CHEBI:33281; ARO:0000032; ARO:3009105; 248-aro.html and 248-parent.html; 248-cephalosporin.json and 248-antimicrobial.json | supports | The exact compound belongs to cephalosporins. Current authorities resolve cephalosporin and antimicrobial agent; ARO places cefroxadine in first generation. The broad role is supported by original antibacterial experiments; no optional antibacterial-drug slot is required. |
| contextual-identifiers | cas:51762-05-1; reaxys:8165480; drugcentral:557; KEGG:D01528; wikipedia.en:Cefroxadine; 248-chebi-ols.json, 248-drugcentral.html, 248-kegg-D01528.txt, 248-wikipedia.html | partial | CAS and Reaxys are retained in current ChEBI; direct CAS access returned 401 and no independent Reaxys record was inspected. DrugCentral resolves cefroxadine with matching formula/CAS and linked exact acid identifiers; KEGG independently supplies the exact native graph. Wikipedia is a contextual compound document, not primary assay evidence. Its synthesis narrative was not used to assert a native producer or biosynthetic pathway. |
| primary-activity | PMID:6998373; DOI:10.1128/AAC.18.1.105; 248-page105.png through 248-page110.png, all six original printed pages | supports | Original CGP9000 paper identifies CIBA-GEIGY synthesis and Figure 1 depicts the zwitterionic dihydrate. Agar dilution used about 5 microliters of a 10^6-CFU/mL suspension, overnight at 37 C; Table 1 notes HI-broth inocula and the methods initially describe peptone water. Table 1 gives E. coli NIHJ-JC2 MIC 3.13 and K. pneumoniae PCI 602 MIC 1.56 micrograms/mL at the lower inoculum; several other tested taxa were &gt;100. Figure 2 comprises 90 S. aureus, 200 E. coli, 275 K. pneumoniae and 50 P. mirabilis isolates. These are panel/strain-specific activity results, not universal susceptibility or a native anhydrous-MIC observation. |
| primary-pbp | PMID:6998373; DOI:10.1128/AAC.18.1.105; Original pp.106,109–110; Figures 6–7 and discussion | supports | E. coli JE1011 PBP preparations were competed with cefroxadine or cephalexin at 1-, 5-, 25-fold the 34 micrograms/mL 14C-penicillin G concentration. Fluorography/densitometry showed stronger cefroxadine competition at PBP1A/1Bs than cephalexin. This is relative competition, not a measured Kd or direct cefroxadine radiolabel assay. The authors interpret greater lysis in relation to PBP1Bs; that interpretation is not an isolated causal perturbation chain. |
| primary-beta-lactamase | PMID:6998373; Original methods pp.105–106 and Table 3 p.109 | supports | Cell extracts were tested at 0.1 mM substrate. Cefroxadine relative hydrolysis was 33, 43, 62, 58 for four cephalosporinases with cephaloridine 100, versus 1 for each of two penicillinases with penicillin G 100. This supports enzyme-specific susceptibility/stability, not universal beta-lactamase resistance. No such universal claim exists in the native record. |
| pk-lead | PMID:2258253; 248-core.json, complete original abstract | partial | Healthy-volunteer infusion PK used a 1 g/0.5 h administration and microbiological quantitation with B. subtilis ATCC 6633. The abstract does not independently establish exact reagent hydration or antimicrobial spectrum; no PK measurement is adopted. |
| review-leads | PMID:29017833; PMID:6752462; 248-core.json complete abstracts; 248-6752462.pdf final English summary and publication header | context_only | PMID29017833 is a general beta-lactam cross-reactivity review, not an exact cefroxadine antigen experiment. PMID6752462 is explicitly a cefroxadine review summarizing historical clinical/PBP studies; its aggregate efficacy and safety statements are not independently revalidated primary trials. The Japanese article was read only at header/English-summary depth. |
| preparation-lead | PMID:7334594; https://www.jstage.jst.go.jp/article/antibiotics1968b/34/12/34_1765/_pdf/-char/en; 248-7334594.pdf printed p.1765, composition and potency section | partial | The original preparation notice specifies C16H19N3O5S·2H2O and 401.43 molecular weight, while expressing potency as anhydrous C16H19N3O5S; one mg standard contains 0.910 mg potency. This directly clarifies hydration/mass basis for that source. Its full Japanese clinical/toxicology compilation was not reviewed, and it is not treated as current regulatory status or an exact anhydrous formulation. |
| local-search | Ignored-inclusive repository search; 248-local-hits.txt and 248-owner-hits.txt | context_only | Searched identifier, label, slug, source IDs and complete key with ignored/hidden files included outside .git/.venv; actual source rows were read. No distinct exact-target curator evidence overlay was identified in the bounded curation/conf/scripts owner search. |

## Limits And Additional Notes

- Exact CAS registry access returned 401; Reaxys is corroborated through ChEBI but not independently opened. Contextual drug links are not treated as pharmaceutical products or proof of current approval.
- PMID2258253 and PMID29017833 are abstract-only; PMID6752462 was checked at original header/English-summary depth and PMID7334594 at its original first-page composition/potency section. Full historical Japanese clinical/toxicology panels and cited protocols were not reassessed.
- The original 1980 paper depicts a dihydrate; its methods and Table 1 differ in the named inoculum preparation medium. No exact anhydrous measurement, single-isomer claim beyond configured centres, or current breakpoint is inferred. PBP competition is not Kd, and lysis correlation is not a fully demonstrated causal chain.
- Supplemental RDKit used the existing 019 interpreter against 025; native schema/strict used 025 own frozen environment. Full shared QC results are integrated before final save. No native/status/history edits or paid research occurred.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- The source-authority molecular graph is not automatically the bulk experimental material. Salt, hydration, strain, assay and concentration basis remain explicit.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T115708Z-cefroxadine-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefroxadine: exact neutral structure and primary activity with a dihydrate
  boundary'
started_at: '2026-10-21T11:39:24Z'
finished_at: '2026-10-21T11:57:08Z'
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
summary: No confirmed defect. The 6R,7R,side-chain 2R structure and accessible exact
  mappings agree. The original antibacterial/PBP paper directly supports activity
  but depicts a dihydrate; the native anhydrous representation must not silently inherit
  that material or concentration basis. Scientific assessment retains the stated evidence
  limits; full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/cefroxadine.yaml
    sha256: b388c0d7befcfaceb96f0afbca26c02a9e42cce48819cfe40b8754765d2155e9
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
targets:
- target_id: CHEBI:31379
  path: data/antibiotics/antibacterial/cefroxadine.yaml
  label: cefroxadine
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
    role: Adopted ARO identity and citation leads
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 248; one exact record in path order,
    initial captures retained and actual ARO/PubChem owners appended before detailed
    assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:31379
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:31379
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    248
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:31379
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefroxadine.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:31379
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefroxadine.yaml --out /private/tmp/am-review-session/248-strict.tsv
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
  - CHEBI:31379
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
  - CHEBI:31379
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
  - CHEBI:31379
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
  - CHEBI:31379
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
  - CHEBI:31379
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
  - CHEBI:31379
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
  - CHEBI:31379
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
  - CHEBI:31379
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
  - CHEBI:31379
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cefroxadine.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T11:48:10Z'
  support: supports
  summary: Read every identity, class, definition, molecular field, source concept,
    xref and seed/reseed event. Seven synonyms and four history events; no MIC observations,
    target, resistance, clinical, producer, dataset or causal graph is populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/chebi_antimicrobials.tsv; data/raw/pubchem_structures.tsv;
    scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  locator: 248-raw-rows.json and original/expanded captures
  accessed_at: '2026-10-21T11:48:10Z'
  support: supports
  summary: Actual maintained rows were read. ChEBI owns identity, definition, chemistry,
    role and four PMID leads; ARO supplies a synonym, class and PMID 6998373. All
    five adopted compound leads are dispositioned.
  snapshot_sha256: 71d76269ffb0db3ba41676c072a39a1c9a985f9fb08badd913f979b9e7fb3d11
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5
  locator: 248-chemistry.json and focused command ledger
  accessed_at: '2026-10-21T11:48:10Z'
  support: supports
  summary: 'Both native encodings reproduce the complete stored key, elemental composition,
    charge, masses within their stated precision and deterministic source mints. Three
    R centres are retained: core 6R,7R and side-chain 2R. The 1,4-cyclohexadiene ring
    and 3-methoxy group agree with names/definition. No water component is encoded.'
  snapshot_sha256: 1d9f3a70515589331a2727de682a116f00cd31b50148ab1952e0fb1a6727aa26
- evidence_id: exact-authorities
  kind: database
  reference: CHEBI:31379; PubChem:5284529; ChEMBL:CHEMBL3186538; KEGG:C12979; ARO:3009113
  locator: 248-pubchem.json, 248-chembl.json, 248-aro.html; 247-248-external-chemistry.json
  accessed_at: '2026-10-21T11:48:10Z'
  support: supports
  summary: Independent PubChem and ChEMBL SMILES/molfile comparisons reproduce the
    native complete key and chirality-aware graph. Current ChEBI matches all chemistry;
    both KEGG compound and drug molfiles independently reproduce the native graph/key.
    Current ARO retains the same identifiers and graph.
  snapshot_sha256: b2ff99a1e99ee3663ee94b1ccc7608e769a110152c1c3cda570e90a20a3412aa
- evidence_id: classification
  kind: authority
  reference: CHEBI:23066; CHEBI:33281; ARO:0000032; ARO:3009105
  locator: 248-aro.html and 248-parent.html; 248-cephalosporin.json and 248-antimicrobial.json
  accessed_at: '2026-10-21T11:48:10Z'
  support: supports
  summary: The exact compound belongs to cephalosporins. Current authorities resolve
    cephalosporin and antimicrobial agent; ARO places cefroxadine in first generation.
    The broad role is supported by original antibacterial experiments; no optional
    antibacterial-drug slot is required.
  snapshot_sha256: a337f2686372f9580fe8b26b261a3dc91591365c2fe9b40a178265b4423f0c89
- evidence_id: contextual-identifiers
  kind: authority
  reference: cas:51762-05-1; reaxys:8165480; drugcentral:557; KEGG:D01528; wikipedia.en:Cefroxadine
  locator: 248-chebi-ols.json, 248-drugcentral.html, 248-kegg-D01528.txt, 248-wikipedia.html
  accessed_at: '2026-10-21T11:48:10Z'
  support: partial
  summary: CAS and Reaxys are retained in current ChEBI; direct CAS access returned
    401 and no independent Reaxys record was inspected. DrugCentral resolves cefroxadine
    with matching formula/CAS and linked exact acid identifiers; KEGG independently
    supplies the exact native graph. Wikipedia is a contextual compound document,
    not primary assay evidence. Its synthesis narrative was not used to assert a native
    producer or biosynthetic pathway.
  snapshot_sha256: 2787efdba18ec8abe1cc6c83c4e3843ebf0740b8ebd4d3f7c9335221c1e6e3f8
- evidence_id: primary-activity
  kind: primary_source
  reference: PMID:6998373; DOI:10.1128/AAC.18.1.105
  locator: 248-page105.png through 248-page110.png, all six original printed pages
  accessed_at: '2026-10-21T11:48:10Z'
  support: supports
  summary: Original CGP9000 paper identifies CIBA-GEIGY synthesis and Figure 1 depicts
    the zwitterionic dihydrate. Agar dilution used about 5 microliters of a 10^6-CFU/mL
    suspension, overnight at 37 C; Table 1 notes HI-broth inocula and the methods
    initially describe peptone water. Table 1 gives E. coli NIHJ-JC2 MIC 3.13 and
    K. pneumoniae PCI 602 MIC 1.56 micrograms/mL at the lower inoculum; several other
    tested taxa were >100. Figure 2 comprises 90 S. aureus, 200 E. coli, 275 K. pneumoniae
    and 50 P. mirabilis isolates. These are panel/strain-specific activity results,
    not universal susceptibility or a native anhydrous-MIC observation.
  snapshot_sha256: 0a84546ba8d0eda327588ec83287ef67d09bbc3d03c0a3328681cd0abf9f010b
- evidence_id: primary-pbp
  kind: primary_source
  reference: PMID:6998373; DOI:10.1128/AAC.18.1.105
  locator: Original pp.106,109–110; Figures 6–7 and discussion
  accessed_at: '2026-10-21T11:48:10Z'
  support: supports
  summary: E. coli JE1011 PBP preparations were competed with cefroxadine or cephalexin
    at 1-, 5-, 25-fold the 34 micrograms/mL 14C-penicillin G concentration. Fluorography/densitometry
    showed stronger cefroxadine competition at PBP1A/1Bs than cephalexin. This is
    relative competition, not a measured Kd or direct cefroxadine radiolabel assay.
    The authors interpret greater lysis in relation to PBP1Bs; that interpretation
    is not an isolated causal perturbation chain.
  snapshot_sha256: 0430208068546dbf7aa196560293f463853b25594f5c2d7057344c782de4f458
- evidence_id: primary-beta-lactamase
  kind: primary_source
  reference: PMID:6998373
  locator: Original methods pp.105–106 and Table 3 p.109
  accessed_at: '2026-10-21T11:48:10Z'
  support: supports
  summary: Cell extracts were tested at 0.1 mM substrate. Cefroxadine relative hydrolysis
    was 33, 43, 62, 58 for four cephalosporinases with cephaloridine 100, versus 1
    for each of two penicillinases with penicillin G 100. This supports enzyme-specific
    susceptibility/stability, not universal beta-lactamase resistance. No such universal
    claim exists in the native record.
  snapshot_sha256: 0430208068546dbf7aa196560293f463853b25594f5c2d7057344c782de4f458
- evidence_id: pk-lead
  kind: primary_source
  reference: PMID:2258253
  locator: 248-core.json, complete original abstract
  accessed_at: '2026-10-21T11:48:10Z'
  support: partial
  summary: Healthy-volunteer infusion PK used a 1 g/0.5 h administration and microbiological
    quantitation with B. subtilis ATCC 6633. The abstract does not independently establish
    exact reagent hydration or antimicrobial spectrum; no PK measurement is adopted.
  snapshot_sha256: ee1c19f7076d3a4531dae9370b0acb719e09cc2589a23def53f4f2502bcde99a
- evidence_id: review-leads
  kind: primary_source
  reference: PMID:29017833; PMID:6752462
  locator: 248-core.json complete abstracts; 248-6752462.pdf final English summary
    and publication header
  accessed_at: '2026-10-21T11:48:10Z'
  support: context_only
  summary: PMID29017833 is a general beta-lactam cross-reactivity review, not an exact
    cefroxadine antigen experiment. PMID6752462 is explicitly a cefroxadine review
    summarizing historical clinical/PBP studies; its aggregate efficacy and safety
    statements are not independently revalidated primary trials. The Japanese article
    was read only at header/English-summary depth.
  snapshot_sha256: ee1c19f7076d3a4531dae9370b0acb719e09cc2589a23def53f4f2502bcde99a
- evidence_id: preparation-lead
  kind: primary_source
  reference: PMID:7334594; https://www.jstage.jst.go.jp/article/antibiotics1968b/34/12/34_1765/_pdf/-char/en
  locator: 248-7334594.pdf printed p.1765, composition and potency section
  accessed_at: '2026-10-21T11:48:10Z'
  support: partial
  summary: The original preparation notice specifies C16H19N3O5S·2H2O and 401.43 molecular
    weight, while expressing potency as anhydrous C16H19N3O5S; one mg standard contains
    0.910 mg potency. This directly clarifies hydration/mass basis for that source.
    Its full Japanese clinical/toxicology compilation was not reviewed, and it is
    not treated as current regulatory status or an exact anhydrous formulation.
  snapshot_sha256: a95cab71d54f352d01bf31793cf8a981c3eadbada5faf1193e6d2259826e6933
- evidence_id: local-search
  kind: search
  reference: Ignored-inclusive repository search
  locator: 248-local-hits.txt and 248-owner-hits.txt
  accessed_at: '2026-10-21T11:48:10Z'
  support: context_only
  summary: Searched identifier, label, slug, source IDs and complete key with ignored/hidden
    files included outside .git/.venv; actual source rows were read. No distinct exact-target
    curator evidence overlay was identified in the bounded curation/conf/scripts owner
    search.
  search_scope: rg --no-ignore --hidden over isolated 025 checkout outside .git/.venv;
    targeted owner search over curation/conf/scripts. No inference from an ignored-aware
    miss.
  snapshot_sha256: 78356bf82ff25d9a33493295cf9d27383705da4362df9ddfad3e644fbb2ad7d4
assessments:
- assessment_id: activity
  area: evidence
  topic: Antibacterial role and tested material
  outcome: supported
  summary: Direct original experiments support antibacterial activity; Figure 1 explicitly
    depicts dihydrate, and the preparation notice gives an anhydrous potency basis
    for its own material. No exact-form MIC is populated in native.
  target_ids:
  - CHEBI:31379
  evidence_ids:
  - native
  - primary-activity
  - preparation-lead
- assessment_id: mechanism
  area: evidence
  topic: Bounded PBP and hydrolysis enrichment
  outcome: supported
  summary: Original competition and substrate assays are useful future evidence with
    strain, material and assay context. Their absence from optional native fields
    is not a defect.
  target_ids:
  - CHEBI:31379
  evidence_ids:
  - primary-pbp
  - primary-beta-lactamase
  - native
- assessment_id: identity
  area: identity
  topic: Exact molecular identity
  outcome: supported
  summary: Native structure, names and accessible independent exact mappings agree
    on configuration, composition and form.
  target_ids:
  - CHEBI:31379
  evidence_ids:
  - native
  - chemistry
  - exact-authorities
- assessment_id: classification
  area: grounding
  topic: Filing and role scope
  outcome: supported
  summary: Compound-specific original antibacterial evidence and resolved classes
    support filing. Source class prose does not establish universal susceptibility.
  target_ids:
  - CHEBI:31379
  evidence_ids:
  - classification
  - exact-authorities
  - primary-activity
- assessment_id: provenance
  area: provenance
  topic: Owner captures, references and history
  outcome: supported
  summary: All initial input hashes remain unchanged; actual maintained owners were
    appended and original captures preserved. All native source references were resolved
    or given access limits; history is seeding rather than scientific sign-off.
  target_ids:
  - CHEBI:31379
  evidence_ids:
  - owners
  - native
  - local-search
- assessment_id: optional
  area: completeness
  topic: Optional structured evidence
  outcome: supported
  summary: No native activity/target/resistance/producer/dataset/clinical object is
    present. Optional blanks alone do not require edits; inspected research is bounded
    to its tested material and evidence type.
  target_ids:
  - CHEBI:31379
  evidence_ids:
  - native
  - primary-pbp
- assessment_id: adapter
  area: scope
  topic: Structured adapter applicability
  outcome: not_applicable
  summary: The native record names no gene, protein, regulator, pathway, stress response
    or expression dataset. Primary mechanism opportunities were discovered subsequently;
    generic expression-module catalog hits are not needed to validate the native populated
    claims.
  target_ids:
  - CHEBI:31379
  evidence_ids:
  - native
- assessment_id: schema
  area: schema
  topic: Native deterministic checks
  outcome: supported
  summary: Focused schema/strict and supplemental native chemistry exited 0; mandatory
    shared gates are integrated by the coordinator separately.
  target_ids:
  - CHEBI:31379
  evidence_ids:
  - chemistry
findings: []
actions: []
limitations:
- Exact CAS registry access returned 401; Reaxys is corroborated through ChEBI but
  not independently opened. Contextual drug links are not treated as pharmaceutical
  products or proof of current approval.
- PMID2258253 and PMID29017833 are abstract-only; PMID6752462 was checked at original
  header/English-summary depth and PMID7334594 at its original first-page composition/potency
  section. Full historical Japanese clinical/toxicology panels and cited protocols
  were not reassessed.
- The original 1980 paper depicts a dihydrate; its methods and Table 1 differ in the
  named inoculum preparation medium. No exact anhydrous measurement, single-isomer
  claim beyond configured centres, or current breakpoint is inferred. PBP competition
  is not Kd, and lysis correlation is not a fully demonstrated causal chain.
- Supplemental RDKit used the existing 019 interpreter against 025; native schema/strict
  used 025 own frozen environment. Full shared QC results are integrated before final
  save. No native/status/history edits or paid research occurred.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- The source-authority molecular graph is not automatically the bulk experimental
  material. Salt, hydration, strain, assay and concentration basis remain explicit.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
