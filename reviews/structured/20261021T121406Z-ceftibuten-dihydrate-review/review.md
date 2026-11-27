# Ceftibuten dihydrate: exact hydrate and qualified clinical evidence

- Review: 20261021T121406Z-ceftibuten-dihydrate-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:49:09Z
- Finished UTC: 2026-10-21T12:14:06Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No confirmed native defect. The neutral dihydrate, current GSRS identity and all three discontinued FDA product assertions agree. Clinical treatment evidence is separated from indication approval and exact solid-form antibacterial measurements. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 257; one exact record in path order; actual source owners appended without replacing initial hashes.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:34618 | data/antibiotics/antibacterial/ceftibuten-dihydrate.yaml | generated | ceftibuten dihydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:34618 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:34618 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:34618 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:34618 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:34618 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:34618 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:34618 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:34618 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:34618 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:34618 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:34618 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:34618 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Three FDA assertions and clinical-use wording

evidence: supported. Targets: CHEBI:34618.

Exact substance join and all three product facts agree. Respiratory indication evidence and primary urinary-treatment studies support bounded use; UTI use is not represented as an FDA-approved indication.

### Exact molecular form and stereochemistry

identity: supported. Targets: CHEBI:34618.

Native names, composition, configured centres and independent exact graph checks agree. Drug-level aliases alone do not redefine salt or hydration identity.

### Parent and role fit

grounding: supported. Targets: CHEBI:34618.

Parent classes and antibacterial roles fit the resolved chemical form and bounded primary activity/use evidence.

### Primary experiments and material assignment

evidence: supported. Targets: CHEBI:34618.

Original experiments establish ceftibuten antibacterial function. Analytical disodium2.5-hydrate, neutral dihydrate and unspecified supplied assay material remain distinct; no unqualified exact-form MIC is added.

### Captured owners and history

ownership: supported. Targets: CHEBI:34618.

All 15 initial/appended input hashes remain unchanged. Source captures identify the actual maintained owners; seed history is not scientific sign-off.

### Optional structured evidence

completeness: supported. Targets: CHEBI:34618.

Absence of optional quantitative activity, resistance, producer and causal graph fields is not itself a finding. Future enrichment must retain exact material, strain, assay and authority scope.

### Native protein/pathway applicability

scope: not_applicable. Targets: CHEBI:34618.

No populated native gene, protein, pathway, stress response or transcriptomics assertion requires an expression adapter. PBP research is contextual follow-up for the active moiety.

### Focused deterministic checks

schema: supported. Targets: CHEBI:34618.

Native schema/strict and supplemental chemistry pass; shared required QC outcomes are integrated before final save.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/ceftibuten-dihydrate.yaml; Complete YAML including names, structure, xrefs, source concepts and history | supports | Read every native field. Five synonyms, one hydrate parent, antibacterial-drug role, one chemical CAS link, two drug links, three complete FDA assertions and six history events; no MIC, target, resistance, producer or graph. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; 257-raw-rows.json; initial and expanded captures | supports | Read actual matched rows. ChEBI row 718 owns identity/definition and supplies no PMID leads. FDA rows 2660–2662 own clinical assertions; the FDA extractor uses exact full-key GSRS joins. |
| chemistry | RDKit 2026.03.5; 257-chemistry.json; 026-root-xref-check.json entry257 | supports | Both native encodings reproduce the complete stored key, elemental composition, net zero charge, masses within stated precision and source mints. The two core R centres and Z side-chain alkene agree. Three components encode ceftibuten plus two waters; component formula equals the summed Hill formula. |
| exact-xrefs | cas:118081-34-8; KEGG:D02121; UNII:62F4443RWP; 026-root-xref-check.json entry257; live authority responses | supports | Independent molecular encodings agree with native. GSRS version15 SMILES and molfile, and KEGG D02121 molfile reproduce SSWTVBYDDFPFAF-DKOGRLLHSA-N. CAS lookup returns seven CIDs with different stereo completeness/configuration, so name lookup alone is not an exact join; CID5282241 specifically matches the native full key. |
| classes | CHEBI:34618; CHEBI:35505; CHEBI:36047; 257-chebi-ols.json and 257-parent.json; actual source role/class rows | supports | The hydrate parent and antibacterial drug role fit the explicitly hydrated cephalosporin. Current OLS SMILES loses the side-chain Z annotation while the native, authority InChI/key and independent structures retain it. This is an external serialization discrepancy, not a native stereo finding. |
| label | https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2dd58c88-142f-41ad-bc31-0a4fff074970; CEDAX label dated 2010-01-12; Description, Indications and Clinical Studies | supports | The official label identifies ceftibuten dihydrate and dose expressed as active ceftibuten equivalent. It lists susceptible-organism respiratory/ear/throat indications, including acute bacterial exacerbations of chronic bronchitis, and does not list UTI as an approved indication. Native prose says used to treat, not FDA-approved for UTI. This dated label establishes formulation/use context, not current marketing availability or an exact anhydrous assay. |
| clinical-uti | PMID:2050421; DOI:10.1007/BF01645584; PMID:11605809; Complete original abstracts from PubMed and 257258-uti-core.json | partial | The1991 open study treated74 women with acute uncomplicated UTI using oral ceftibuten400mg daily for7days; it reports recurrence and gastrointestinal adverse effects. The2001 randomized open trial enrolled62 complicated-UTI patients but analyzed45 after exclusions, including resistant pathogens;23 received ceftibuten. These directly establish studied urinary-treatment use with restricted populations. Abstracts do not specify exact crystalline hydration; no regulatory indication or formulation-specific efficacy value is inferred. |
| synthesis | PMID:3680016; DOI:10.7164/antibiotics.40.1468; All three original pages; Scheme1 and Table1/footnote p1469; independent reader report and root text audit | supports | 7432-S is compound9a with R=H and Z side-chain alkene;9b/9c are analogues and10 is the E isomer. Slow crystallization with isomerization gives approximately1:99 E/Z. The analytical footnote explicitly characterizes the DISODIUM2.5-hydrate, not the neutral dihydrate. Table1 demonstrates antibacterial activity, including E. coli NIHJ JC-2 at0.1micrograms/mL, but its assay preparation/medium/inoculum are insufficiently described for a complete exact-form observation. NMR geometry and analogue distinctions are preserved. |
| primary-activity | PMID:3190185; DOI:10.1128/AAC.32.10.1576; Original pp1576–1582, all seven page scans inspected by delegated source reader; root p1576 material/method audit; Tables1–4 | supports | The study tested Schering ceftibuten7432-S/SCH39720 against690 selected strains enriched for resistance, with reference broth microdilution at5×10^5CFU/mL for16–20hours and organism-specific supplements/agar exceptions. Exact hydration/counterion of supplied material is unstated. Species/strain-dependent activity includes poor activity against many staphylococci and nonfermenters; the panel cannot establish universal Gram-negative coverage. Historical disk-breakpoint proposals are not current standards. Table/abstract MIC90 discrepancies for B. catarrhalis and gonococci are retained in the reader report; no such value is imported. |
| pbp-primary | DOI:10.11250/chemotherapy1953.37.Supplement1_730; Original pp730–737, especially membrane methods p731 and Table5 p733; root visually checked Table5 | supports | Shionogi7432-S was preincubated with membrane fractions before14C-penicillinG competition and fluorography. E. coli K12 PBP3 ID50 is0.025micrograms/mL; PBP1a20 and1bs6, and2/4/5/6 &gt;400. This is a concentration reducing radioligand binding, not Kd or purified transpeptidase catalysis. P. vulgaris CN329 selective PBP3 labeling is qualitative in its figure; the E. coli value must not be transferred. Bulk salt/hydration is not specified. |
| enzyme-boundary | DOI:10.11250/chemotherapy1953.37.Supplement1_730; Original Tables1–4; root visually inspected Table4 p733 | supports | Beta-lactamase stability is enzyme-specific. B. fragilis V-283 hydrolysis gives relativeVmax41 with cephaloridine100 and Km560micromolar; the value is Km, not Ki. No universal beta-lactamase-stability claim is established. Native does not assert such universality. |
| hydrate-patent | https://patents.google.com/patent/CN106397455A/en; Translated original description and Example1, elemental analysis/Karl Fischer/TGA; root text audit | supports | Example1 characterizes crystalline material with elemental percentages matching C15H14N4O6S2·2H2O and water8.08percent by Karl Fischer,8.07percent by TGA. This supports the exact dihydrate material. Experiments concern solid-state/formulation properties, not MIC or PBP. A machine-translated background phrase about dihydrochloride does not override the example elemental/water data. |
| fda | https://api.fda.gov/drug/drugsfda.json?search=application_number:NDA050685&amp;limit=1; https://api.fda.gov/drug/drugsfda.json?search=application_number:NDA050686&amp;limit=1; 257-fda-050685.json and 257-fda-050686.json; native product numbers and original AP submission | supports | All three native assertions agree: NDA 050685 product 002 (400 mg equivalent) and NDA 050686 products 001 (90 mg per 5 mL equivalent) and 002 (180 mg per 5 mL equivalent), sponsor BURKE THERAP, CEDAX, original AP date 1995-12-20. All are Discontinued with currently_marketed false. APPROVED records the regulatory decision, not ongoing marketing. GSRS version 15 has the exact native full hydrate identity. |
| context-links | DrugBank:DB01415; 257-drugbank.html retrieval403; 257-kegg-D02121.txt | partial | DrugBank returned403 and was not independently inspected. KEGG drug link supplies the exact hydrate graph. Typed drug/document links are not automatically exact formulation assertions. |
| local-search | Ignored-inclusive repository and owner search; 257-local-hits.txt and 257-owner-hits.txt | context_only | Identifier, label, source IDs and full key were searched with hidden/ignored coverage outside .git/.venv. Actual matched source rows and maintained owners were read. No separate exact-target primary-curation overlay was identified in the bounded curation/conf/scripts search. |

## Limits And Additional Notes

- Original1987 synthesis,1988 activity scans and1989 membrane study were inspected with a delegated source reader; root independently checked selected structure/material/method/table passages. No direct anhydrous-versus-dihydrate potency comparison was established in this bounded source set.
- Clinical UTI studies were read at complete abstract depth; their exact crystalline materials and full trial protocols remain unverified. The2001 trial excludes resistant-pathogen patients from analysis, limiting generalization.
- DrugBank retrieval returned403. Proprietary registry content was not independently audited. Current OLS serialization drops alkene stereo; preserve independently corroborated native Z.
- The direct PMC1988 PDF response was an HTML challenge; genuine original page scans were used instead. Initial unpadded EP URL404 was resolved with EP0136721A2.
- Native activity observations were not added. Assay concentrations, membrane-competition ID50, relative enzymeVmax, Km and clinical doses are not interchangeable. Shared full-QC limitations are integrated before save.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T121406Z-ceftibuten-dihydrate-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Ceftibuten dihydrate: exact hydrate and qualified clinical evidence'
started_at: '2026-10-21T11:49:09Z'
finished_at: '2026-10-21T12:14:06Z'
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
summary: No confirmed native defect. The neutral dihydrate, current GSRS identity
  and all three discontinued FDA product assertions agree. Clinical treatment evidence
  is separated from indication approval and exact solid-form antibacterial measurements.
  Scientific assessment retains the stated evidence limits; full verification is blocked
  by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/ceftibuten-dihydrate.yaml
    sha256: bb705f34e7e292bedc83a731f9509228f7659fab58e9a3b3b5e4a4c46dce1a60
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
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/extract_fda_clinical_status.py
    sha256: f30f385ea6d530dc1749e3d805dbcdbc8715fbc476abc510bf144ea13964e171
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
- target_id: CHEBI:34618
  path: data/antibiotics/antibacterial/ceftibuten-dihydrate.yaml
  label: ceftibuten dihydrate
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
    path: data/raw/fda_clinical_status.tsv
    role: Actual maintained source or transform for this record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Actual maintained source or transform for this record
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 257; one exact record in path order;
    actual source owners appended without replacing initial hashes.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:34618
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:34618
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    257
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:34618
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/ceftibuten-dihydrate.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:34618
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/ceftibuten-dihydrate.yaml --out /private/tmp/am-review-session/257-strict.tsv
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
  - CHEBI:34618
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
  - CHEBI:34618
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
  - CHEBI:34618
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
  - CHEBI:34618
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
  - CHEBI:34618
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
  - CHEBI:34618
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
  - CHEBI:34618
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
  - CHEBI:34618
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
  - CHEBI:34618
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/ceftibuten-dihydrate.yaml
  locator: Complete YAML including names, structure, xrefs, source concepts and history
  accessed_at: '2026-10-21T12:07:57Z'
  support: supports
  summary: Read every native field. Five synonyms, one hydrate parent, antibacterial-drug
    role, one chemical CAS link, two drug links, three complete FDA assertions and
    six history events; no MIC, target, resistance, producer or graph.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: 257-raw-rows.json; initial and expanded captures
  accessed_at: '2026-10-21T12:07:57Z'
  support: supports
  summary: Read actual matched rows. ChEBI row 718 owns identity/definition and supplies
    no PMID leads. FDA rows 2660–2662 own clinical assertions; the FDA extractor uses
    exact full-key GSRS joins.
  snapshot_sha256: 729fa724d53e674b9a60ae1860d1976e619c731e7f76ffc5924d1bc0ba6b29d8
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5
  locator: 257-chemistry.json; 026-root-xref-check.json entry257
  accessed_at: '2026-10-21T12:07:57Z'
  support: supports
  summary: Both native encodings reproduce the complete stored key, elemental composition,
    net zero charge, masses within stated precision and source mints. The two core
    R centres and Z side-chain alkene agree. Three components encode ceftibuten plus
    two waters; component formula equals the summed Hill formula.
  snapshot_sha256: 1643d3834cf071dee6f775eb3cc483fd2876a03dbe21b09c81a07d0fc87fe2a0
- evidence_id: exact-xrefs
  kind: database
  reference: cas:118081-34-8; KEGG:D02121; UNII:62F4443RWP
  locator: 026-root-xref-check.json entry257; live authority responses
  accessed_at: '2026-10-21T12:07:57Z'
  support: supports
  summary: Independent molecular encodings agree with native. GSRS version15 SMILES
    and molfile, and KEGG D02121 molfile reproduce SSWTVBYDDFPFAF-DKOGRLLHSA-N. CAS
    lookup returns seven CIDs with different stereo completeness/configuration, so
    name lookup alone is not an exact join; CID5282241 specifically matches the native
    full key.
  snapshot_sha256: 1643d3834cf071dee6f775eb3cc483fd2876a03dbe21b09c81a07d0fc87fe2a0
- evidence_id: classes
  kind: authority
  reference: CHEBI:34618; CHEBI:35505; CHEBI:36047
  locator: 257-chebi-ols.json and 257-parent.json; actual source role/class rows
  accessed_at: '2026-10-21T12:07:57Z'
  support: supports
  summary: The hydrate parent and antibacterial drug role fit the explicitly hydrated
    cephalosporin. Current OLS SMILES loses the side-chain Z annotation while the
    native, authority InChI/key and independent structures retain it. This is an external
    serialization discrepancy, not a native stereo finding.
  snapshot_sha256: 924fb825e891c574609d1d50f8583a5950f41bad8f64810b67b15c443552bd51
- evidence_id: label
  kind: authority
  reference: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2dd58c88-142f-41ad-bc31-0a4fff074970
  locator: CEDAX label dated 2010-01-12; Description, Indications and Clinical Studies
  accessed_at: '2026-10-21T12:07:57Z'
  support: supports
  summary: The official label identifies ceftibuten dihydrate and dose expressed as
    active ceftibuten equivalent. It lists susceptible-organism respiratory/ear/throat
    indications, including acute bacterial exacerbations of chronic bronchitis, and
    does not list UTI as an approved indication. Native prose says used to treat,
    not FDA-approved for UTI. This dated label establishes formulation/use context,
    not current marketing availability or an exact anhydrous assay.
  snapshot_sha256: 038427ffc36a7b78043aad2d696d6503aaa16dec18f594859aedda5e4b0f4f75
- evidence_id: clinical-uti
  kind: primary_source
  reference: PMID:2050421; DOI:10.1007/BF01645584; PMID:11605809
  locator: Complete original abstracts from PubMed and 257258-uti-core.json
  accessed_at: '2026-10-21T12:07:57Z'
  support: partial
  summary: The1991 open study treated74 women with acute uncomplicated UTI using oral
    ceftibuten400mg daily for7days; it reports recurrence and gastrointestinal adverse
    effects. The2001 randomized open trial enrolled62 complicated-UTI patients but
    analyzed45 after exclusions, including resistant pathogens;23 received ceftibuten.
    These directly establish studied urinary-treatment use with restricted populations.
    Abstracts do not specify exact crystalline hydration; no regulatory indication
    or formulation-specific efficacy value is inferred.
  snapshot_sha256: 494e852c3873b695f3d5e3201b615de42f23db6fab86586e892ed549ab9d5753
- evidence_id: synthesis
  kind: primary_source
  reference: PMID:3680016; DOI:10.7164/antibiotics.40.1468
  locator: All three original pages; Scheme1 and Table1/footnote p1469; independent
    reader report and root text audit
  accessed_at: '2026-10-21T12:07:57Z'
  support: supports
  summary: 7432-S is compound9a with R=H and Z side-chain alkene;9b/9c are analogues
    and10 is the E isomer. Slow crystallization with isomerization gives approximately1:99
    E/Z. The analytical footnote explicitly characterizes the DISODIUM2.5-hydrate,
    not the neutral dihydrate. Table1 demonstrates antibacterial activity, including
    E. coli NIHJ JC-2 at0.1micrograms/mL, but its assay preparation/medium/inoculum
    are insufficiently described for a complete exact-form observation. NMR geometry
    and analogue distinctions are preserved.
  snapshot_sha256: bf1e9fc5f140bdf226eb8c41685625c838ceeb66db539ffa75c54323b2e5f7a5
- evidence_id: primary-activity
  kind: primary_source
  reference: PMID:3190185; DOI:10.1128/AAC.32.10.1576
  locator: Original pp1576–1582, all seven page scans inspected by delegated source
    reader; root p1576 material/method audit; Tables1–4
  accessed_at: '2026-10-21T12:07:57Z'
  support: supports
  summary: The study tested Schering ceftibuten7432-S/SCH39720 against690 selected
    strains enriched for resistance, with reference broth microdilution at5×10^5CFU/mL
    for16–20hours and organism-specific supplements/agar exceptions. Exact hydration/counterion
    of supplied material is unstated. Species/strain-dependent activity includes poor
    activity against many staphylococci and nonfermenters; the panel cannot establish
    universal Gram-negative coverage. Historical disk-breakpoint proposals are not
    current standards. Table/abstract MIC90 discrepancies for B. catarrhalis and gonococci
    are retained in the reader report; no such value is imported.
  snapshot_sha256: 3e60037526e38cd7142d5a0cf7bf0c5a04832d9702165cdc7203dacfd4d7d9a6
- evidence_id: pbp-primary
  kind: primary_source
  reference: DOI:10.11250/chemotherapy1953.37.Supplement1_730
  locator: Original pp730–737, especially membrane methods p731 and Table5 p733; root
    visually checked Table5
  accessed_at: '2026-10-21T12:07:57Z'
  support: supports
  summary: Shionogi7432-S was preincubated with membrane fractions before14C-penicillinG
    competition and fluorography. E. coli K12 PBP3 ID50 is0.025micrograms/mL; PBP1a20
    and1bs6, and2/4/5/6 >400. This is a concentration reducing radioligand binding,
    not Kd or purified transpeptidase catalysis. P. vulgaris CN329 selective PBP3
    labeling is qualitative in its figure; the E. coli value must not be transferred.
    Bulk salt/hydration is not specified.
  snapshot_sha256: 6550a19a410dad0f9f5d14a5c28d3727faa535e9b07e76673ee1605f0b041bcb
- evidence_id: enzyme-boundary
  kind: primary_source
  reference: DOI:10.11250/chemotherapy1953.37.Supplement1_730
  locator: Original Tables1–4; root visually inspected Table4 p733
  accessed_at: '2026-10-21T12:07:57Z'
  support: supports
  summary: Beta-lactamase stability is enzyme-specific. B. fragilis V-283 hydrolysis
    gives relativeVmax41 with cephaloridine100 and Km560micromolar; the value is Km,
    not Ki. No universal beta-lactamase-stability claim is established. Native does
    not assert such universality.
  snapshot_sha256: 977ddfe64fd95c09dee332ad126dbfac81e6060e14baca4e27eab39c9454711d
- evidence_id: hydrate-patent
  kind: primary_source
  reference: https://patents.google.com/patent/CN106397455A/en
  locator: Translated original description and Example1, elemental analysis/Karl Fischer/TGA;
    root text audit
  accessed_at: '2026-10-21T12:07:57Z'
  support: supports
  summary: Example1 characterizes crystalline material with elemental percentages
    matching C15H14N4O6S2·2H2O and water8.08percent by Karl Fischer,8.07percent by
    TGA. This supports the exact dihydrate material. Experiments concern solid-state/formulation
    properties, not MIC or PBP. A machine-translated background phrase about dihydrochloride
    does not override the example elemental/water data.
  snapshot_sha256: c86ff8e506d149ffc2966310062e7f6cf4f1b868a580cb8530a07d59e286bc04
- evidence_id: fda
  kind: authority
  reference: https://api.fda.gov/drug/drugsfda.json?search=application_number:NDA050685&limit=1;
    https://api.fda.gov/drug/drugsfda.json?search=application_number:NDA050686&limit=1
  locator: 257-fda-050685.json and 257-fda-050686.json; native product numbers and
    original AP submission
  accessed_at: '2026-10-21T12:07:57Z'
  support: supports
  summary: 'All three native assertions agree: NDA 050685 product 002 (400 mg equivalent)
    and NDA 050686 products 001 (90 mg per 5 mL equivalent) and 002 (180 mg per 5
    mL equivalent), sponsor BURKE THERAP, CEDAX, original AP date 1995-12-20. All
    are Discontinued with currently_marketed false. APPROVED records the regulatory
    decision, not ongoing marketing. GSRS version 15 has the exact native full hydrate
    identity.'
  snapshot_sha256: b0711199fe34152506c2479caa3e7db000855cdb68473b791d090054f20bbb38
- evidence_id: context-links
  kind: database
  reference: DrugBank:DB01415
  locator: 257-drugbank.html retrieval403; 257-kegg-D02121.txt
  accessed_at: '2026-10-21T12:07:57Z'
  support: partial
  summary: DrugBank returned403 and was not independently inspected. KEGG drug link
    supplies the exact hydrate graph. Typed drug/document links are not automatically
    exact formulation assertions.
- evidence_id: local-search
  kind: search
  reference: Ignored-inclusive repository and owner search
  locator: 257-local-hits.txt and 257-owner-hits.txt
  accessed_at: '2026-10-21T12:07:57Z'
  support: context_only
  summary: Identifier, label, source IDs and full key were searched with hidden/ignored
    coverage outside .git/.venv. Actual matched source rows and maintained owners
    were read. No separate exact-target primary-curation overlay was identified in
    the bounded curation/conf/scripts search.
  search_scope: rg --no-ignore --hidden over isolated026 outside .git/.venv, then
    exact owner search curation/conf/scripts; absence is only within that searched
    scope.
  snapshot_sha256: 1eaefe3aa8abad2b0ac1e7c294353d3d9373b49eabfe3d6bf8edb1c95900283b
assessments:
- assessment_id: clinical
  area: evidence
  topic: Three FDA assertions and clinical-use wording
  outcome: supported
  summary: Exact substance join and all three product facts agree. Respiratory indication
    evidence and primary urinary-treatment studies support bounded use; UTI use is
    not represented as an FDA-approved indication.
  target_ids:
  - CHEBI:34618
  evidence_ids:
  - fda
  - exact-xrefs
  - label
  - clinical-uti
- assessment_id: identity
  area: identity
  topic: Exact molecular form and stereochemistry
  outcome: supported
  summary: Native names, composition, configured centres and independent exact graph
    checks agree. Drug-level aliases alone do not redefine salt or hydration identity.
  target_ids:
  - CHEBI:34618
  evidence_ids:
  - native
  - chemistry
  - exact-xrefs
- assessment_id: classification
  area: grounding
  topic: Parent and role fit
  outcome: supported
  summary: Parent classes and antibacterial roles fit the resolved chemical form and
    bounded primary activity/use evidence.
  target_ids:
  - CHEBI:34618
  evidence_ids:
  - classes
  - primary-activity
  - label
- assessment_id: activity
  area: evidence
  topic: Primary experiments and material assignment
  outcome: supported
  summary: Original experiments establish ceftibuten antibacterial function. Analytical
    disodium2.5-hydrate, neutral dihydrate and unspecified supplied assay material
    remain distinct; no unqualified exact-form MIC is added.
  target_ids:
  - CHEBI:34618
  evidence_ids:
  - synthesis
  - primary-activity
  - hydrate-patent
  - enzyme-boundary
- assessment_id: provenance
  area: ownership
  topic: Captured owners and history
  outcome: supported
  summary: All 15 initial/appended input hashes remain unchanged. Source captures
    identify the actual maintained owners; seed history is not scientific sign-off.
  target_ids:
  - CHEBI:34618
  evidence_ids:
  - owners
  - native
  - local-search
- assessment_id: optional
  area: completeness
  topic: Optional structured evidence
  outcome: supported
  summary: Absence of optional quantitative activity, resistance, producer and causal
    graph fields is not itself a finding. Future enrichment must retain exact material,
    strain, assay and authority scope.
  target_ids:
  - CHEBI:34618
  evidence_ids:
  - native
  - primary-activity
  - pbp-primary
- assessment_id: adapter
  area: scope
  topic: Native protein/pathway applicability
  outcome: not_applicable
  summary: No populated native gene, protein, pathway, stress response or transcriptomics
    assertion requires an expression adapter. PBP research is contextual follow-up
    for the active moiety.
  target_ids:
  - CHEBI:34618
  evidence_ids:
  - native
- assessment_id: schema
  area: schema
  topic: Focused deterministic checks
  outcome: supported
  summary: Native schema/strict and supplemental chemistry pass; shared required QC
    outcomes are integrated before final save.
  target_ids:
  - CHEBI:34618
  evidence_ids:
  - chemistry
findings: []
actions: []
limitations:
- Original1987 synthesis,1988 activity scans and1989 membrane study were inspected
  with a delegated source reader; root independently checked selected structure/material/method/table
  passages. No direct anhydrous-versus-dihydrate potency comparison was established
  in this bounded source set.
- Clinical UTI studies were read at complete abstract depth; their exact crystalline
  materials and full trial protocols remain unverified. The2001 trial excludes resistant-pathogen
  patients from analysis, limiting generalization.
- DrugBank retrieval returned403. Proprietary registry content was not independently
  audited. Current OLS serialization drops alkene stereo; preserve independently corroborated
  native Z.
- The direct PMC1988 PDF response was an HTML challenge; genuine original page scans
  were used instead. Initial unpadded EP URL404 was resolved with EP0136721A2.
- Native activity observations were not added. Assay concentrations, membrane-competition
  ID50, relative enzymeVmax, Km and clinical doses are not interchangeable. Shared
  full-QC limitations are integrated before save.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:34618
- https://doi.org/10.7164/antibiotics.40.1468
- https://doi.org/10.11250/chemotherapy1953.37.Supplement1_730
tags:
- record-review
- ceftibuten-dihydrate
- material-scope
```
