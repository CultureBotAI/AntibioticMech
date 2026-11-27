# Linolenyl alcohol: exact all-Z identity and primary comparator scope

- Review: 20261021T082722Z-linolenyl-alcohol
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:21:57Z
- Finished UTC: 2026-10-21T08:27:22Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Exact neutral all-Z identity, parent, antibacterial role, patent-document placement and generated provenance are supported. No corrective finding is demonstrated. Primary comparator data separate linolenyl growth delay/bacteriostatic combination from tridecan-1-ol bactericidal synergy; membrane mechanism remains a hypothesis. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record scientific review of one exact linolenyl alcohol record.

Selection: Queue072; CHEBI:77474 in isolated batch008.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:77474 | data/antibiotics/antibacterial/9z-12z-15z-octadecatrien-1-ol.yaml | generated | (9Z,12Z,15Z)-octadecatrien-1-ol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:77474 | Actual command passed. |
| Focused strict | passed | True | CHEBI:77474 | Actual command passed. |
| Structure consistency | passed | True | CHEBI:77474 | Both encodings, locants and live authorities agree. |
| Structured source applicability | not_applicable | False | CHEBI:77474 | No native named gene, protein, pathway, regulator, stress response or transcriptomic dataset; generic membrane speculation discovered in literature is not a specific covered module assertion. |
| Original primary access | passed | False | CHEBI:77474 | Complete1984 page scans and patent text inspected;1982 paper remains abstract-only. |
| Authoritative full QC | failed | True | CHEBI:77474 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:77474 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:77474 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:77474 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:77474 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:77474 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:77474 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:77474 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:77474 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact free all-Z fatty alcohol

identity: supported. Targets: CHEBI:77474.

Native names, full encodings, current ChEBI and exact-key PubChem agree. Independent locant/CIP checks support all three Z bonds.

### Broader parent and antibacterial filing

grounding: supported. Targets: CHEBI:77474.

Parent is broader; compound-specific1982 and1984 primary evidence supports antibacterial activity under tested conditions.

### Patent references and identity boundary

provenance: supported. Targets: CHEBI:77474.

All three patent documents resolve and concern named linolenyl alcohol. Their placement in document_xrefs is correct; family repetition, claim breadth and unreported full stereochemical specification limit assay transfer.

### Specific comparator and combination assays

evidence: supported. Targets: CHEBI:77474.

The1984 comparator supplies explicit dose, strain, medium, antioxidant, time andCFU context. Linolenyl alone slowed growth; its gentamicin combination was bacteriostatic in that assay. Preserve the more potent tridecan-1-ol comparison and do not recast a growth curve as MIC.

### Membrane hypothesis versus direct target

evidence: unknown. Targets: CHEBI:77474.

No native mechanism is asserted. The1984 authors propose a membrane effect but provide no linolenyl-specific direct binding or definitive molecular target. A target or causal graph should not be forced from class analogy or tridecan-1-ol synergy.

### Repeated-exposure phenotype

scope: supported. Targets: CHEBI:77474.

The1982 abstract’s unchanged BHT sensitivity is bounded to its exposure protocol and strain, not a universal resistance claim. Native resistance fields are empty and appropriate.

### Biotransformation and ester products

scope: not_applicable. Targets: CHEBI:77474.

No producer claim is native. Insect conversion of added labeled alcohol and enzyme-made ester production do not establish endogenous alcohol production or antibacterial action of the same chemical form.

### Proposed dental products versus clinical status

scope: not_applicable. Targets: CHEBI:77474.

Patent and paper proposals do not establish approved products, efficacy in patients or clinical status; none is asserted natively.

### Quantitative follow-up and optional fields

completeness: unknown. Targets: CHEBI:77474.

Concrete1984 comparator results and1982/patent leads can support future method-qualified observations after form/source adjudication. Optional blank activity/target/dataset/graph fields alone do not establish a corrective defect.

### Chemical registry references

provenance: unknown. Targets: CHEBI:77474.

CAS is consistent across authorities; independent Reaxys equivalence remains source-asserted with no demonstrated mismatch.

### Generated owner and history

provenance: supported. Targets: CHEBI:77474.

Adopted source metadata, reproducible mint, filing and four history events agree; SEEDED remains unchanged.

### Focused validators

schema: supported. Targets: CHEBI:77474.

Both native focused gates pass.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/9z-12z-15z-octadecatrien-1-ol.yaml; Entire YAML | supports | Read label, five exact synonyms, structural definition, single parent, antibacterial role, both structure encodings, formula, charge, masses, CAS/Reaxys identifiers, three document_xrefs, source metadata and all four seed/reseed events. No quantitative activity, molecular target, mechanism, producer, resistance, clinical, dataset or causal-graph assertion is native. |
| owner | data/raw/chebi_antimicrobials.tsv; Row1960; PATHS2228; configuration/extractor/seeder | supports | Raw identity and fields agree; source leads are PMIDs16186620,21338674,6508262,6763859. Patents correctly move from raw xrefs into document_xrefs. Mint antibioticmech:chebi-2d0da980dd reproduces. Imported corrections belong to raw/extractor/seeder; future scientific annotations belong to the native record through validated writer/history. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:77474; Names, structure, ontology, registry and document references | supports | Current ChEBI gives the same all-Z C18 primary alcohol, neutral C18H32O, key IKYKEVDKGZYRMQ-PDBXOOCHSA-N, mass264.453/exact264.24532, five synonyms, parent, antibacterial role, CAS506-44-5, Reaxys2101049 and three patent references. |
| parent | https://www.ebi.ac.uk/chebi/CHEBI:77396; Official definition and outgoing relation | supports | Long-chain primary fatty alcohol is a strictly broader class; the hydroxy-bearing methylene and long C18 chain satisfy the structural definition. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/6436081; Full-key PUG resolution | supports | Exact full-key lookup returns CID6436081, identical all-Z InChI/key, C18H32O, neutral charge and compatible masses. PubChem identity page also lists CAS506-44-5 from CAS Common Chemistry and other authorities. |
| chemistry | Independent RDKit structure calculation; Both native encodings; numbering from hydroxy-bearing carbon | supports | Both reproduce the complete key, formula, neutral charge, one fragment, mass264.453/exact264.245315644 and three Z bonds. Explicit numbering places them at9–10,12–13,15–16. |
| 1982 | PMID:6763859; DOI10.1016/0003-9969(82)90008-5; primary abstract | supports | Linolenyl and linoleyl alcohol inhibit the tested bacteria; S.mutans BHT is the main test strain. Gram-positive/Gram-negative statements concern the tested panel. Repeated exposure of BHT did not alter sensitivity, and cell-associated linolenyl alcohol was detected after24h without detected linolenic acid. These observations do not prove a molecular target, universal inability to evolve resistance or clinical efficacy. Full original methods were not accessible. |
| 1984 | PMID:6508262; DOI10.1128/AAC.26.3.306; complete original pp306–309; Figure2 and Discussion | supports | All four page scans were read. Nu Chek Prep alcohols were at least99% pure by TLC/GLC. S.mutans BHT grew in7mL Todd-Hewitt broth at37°C aerobically; inoculum1–5×10^7CFU/mL; ethanol controls and1.1mM ascorbic acid with linolenyl alcohol limited autooxidation. At22µM linolenyl alcohol slowed growth but CFU rose about2 logs by24h. Linolenyl plus gentamicin1.4µg/mL was bacteriostatic; the bactericidal combination belonged to tridecan-1-ol. Proposed membrane spacing/permeability remained mechanistic interpretation. |
| mycoplasma | PMID:6794448; DOI10.1128/AAC.19.5.917; primary abstract on PubMed/PMC181542 | context_only | Additional primary abstract reports linolenyl, linoleyl and oleyl alcohols as less effective under its mycoplasma test conditions than the saturated alcohols. Cholesterol reversal and electron-micrograph experiments concern stearyl alcohol, not linolenyl. This is a bounded additional activity lead; full original table values were not extracted. |
| ester | PMID:16186620; DOI10.1385/abab:127:1:017; primary abstract | context_only | Linolenyl alcohol is an esterification substrate. The antiradical result concerns linolenyl dihydrocaffeate, a distinct ester product, not antibacterial action of this free alcohol. |
| pheromone | PMID:21338674; DOI10.1016/j.ibmb.2011.02.004; primary abstract | context_only | Labeled linolenyl alcohol was converted to a labeled pheromone aldehyde in Hyphantria cunea glands. Substrate conversion and enzyme selectivity are not proof of bacterial inhibition or de novo biosynthesis of the administered alcohol. |
| patent-4209533 | https://patents.google.com/patent/US4209533A/en; Description, experimental tables and family statement | context_only | Original patent describes linolenyl/linoleyl alcohol antibacterial uses and broth growth curves in Klett units. The document is relevant and correctly placed in document_xrefs, not exact chemical xrefs. Patent claims span compounds/formulations and are not clinical authorization or independent family replications. The inspected text does not specify a complete Z/Z/Z material identity; numerical transfer requires preparation mapping. |
| patent-4340628 | https://patents.google.com/patent/US4340628A/en; Description, experimental tables and family statement | context_only | Division of the original patent describes linolenyl/linoleyl alcohol antibacterial uses and broth growth curves in Klett units. The document is relevant and correctly placed in document_xrefs, not exact chemical xrefs. Patent claims span compounds/formulations and are not clinical authorization or independent family replications. The inspected text does not specify a complete Z/Z/Z material identity; numerical transfer requires preparation mapping. |
| patent-4372978 | https://patents.google.com/patent/US4372978A/en; Description, experimental tables and family statement | context_only | Further division in the same family describes linolenyl/linoleyl alcohol antibacterial uses and broth growth curves in Klett units. The document is relevant and correctly placed in document_xrefs, not exact chemical xrefs. Patent claims span compounds/formulations and are not clinical authorization or independent family replications. The inspected text does not specify a complete Z/Z/Z material identity; numerical transfer requires preparation mapping. |
| patent-boundaries | https://patents.google.com/patent/US4372978A/en; Tables2–3,6,9 and accompanying interpretation | context_only | Table3 reports delayed growth of S.mutans BHT and a5h half-growth response near2.54nmol/mL; that is not a standard MIC. The patent infers lysis/death from reduced opacity in Clostridium cultures rather than establishing a direct molecular mechanism. Around Table9, prose alternates linoleyl and linolenyl while rows say linolenyl; preserve this source conflict before transferring E.coli results. |
| registries | https://www.ebi.ac.uk/chebi/CHEBI:77474; Registry Numbers | partial | CAS506-44-5 agrees with current official ChEBI/PubChem identity. Reaxys2101049 was only verified as an official ChEBI assertion; independent restricted-registry structure detail remains unavailable. |
| search | CultureBotAI/AntibioticMech; Ignored-inclusive repository search and free primary discovery | context_only | Full native/raw/PATHS/config and maintained curation surfaces were checked. The historical report is only discovery context and its optional-field-based major finding is not adopted. All four adopted abstracts were read, the complete1984 paper was inspected as page scans, and patent descriptions/tables were examined.1982 publisher access supplied abstract only. |
| gates | just validate; just validate-strict; Actual focused commands in batch008 | supports | Both validators exited0; one record and zero strictERROR rows. |

## Limits And Additional Notes

- The1982 paper remains abstract-only. Its full material characterization, quantitative doses and repeated-exposure protocol were not inspected.
- The1984 paper names commercial linolenyl alcohol with at least99% chromatographic purity but does not provide a complete stereochemical structure or catalog identifier; exact all-Z mapping is supported by current name/registry authorities rather than independent reanalysis of the historical material.
- Patent numbers are valid document references. Their broad formulations, repeated family data, opacity-based lysis inference and linoleyl/linolenyl wording conflict require adjudication before quantitative transfer.
- Independent Reaxys detail was unavailable; the bounded literature search is not an assertion that no additional exact-compound evidence exists.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All21 captured input hashes were rechecked unchanged; no native fields, history or scientific status were changed.
- Concrete follow-up: curate or explicitly defer1984 Figure2 comparator observations with22µM alcohol,1.1mM ascorbic acid,37°C aerobic Todd-Hewitt medium,BHT strain,time andCFU endpoint. Keep alcohol alone and gentamicin combination separate; no MIC or proven membrane target follows.
- Original1984 printed pages306,307,308,309 correspond respectively to scratch072-page4,page3,page1,page2; manifest stores original URLs and image hashes.
- Historical optional-field-based major finding is not adopted.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T082722Z-linolenyl-alcohol
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Linolenyl alcohol: exact all-Z identity and primary comparator scope'
started_at: '2026-10-21T08:21:57Z'
finished_at: '2026-10-21T08:27:22Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independently read complete native record, live authorities,
    primary abstracts, all1984 page scans and patent text; did not create the seed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: Exact neutral all-Z identity, parent, antibacterial role, patent-document
  placement and generated provenance are supported. No corrective finding is demonstrated.
  Primary comparator data separate linolenyl growth delay/bacteriostatic combination
  from tridecan-1-ol bactericidal synergy; membrane mechanism remains a hypothesis.
  Scientific assessment retains the stated evidence limits; full verification is blocked
  by the shared native-library failure.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
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
  - path: data/antibiotics/PATHS.tsv
    sha256: 3b1d82d007878e4aca2c28f4001a468776b325b726da2e48abb76a3dc551cc38
    role: context
  - path: data/antibiotics/antibacterial/9z-12z-15z-octadecatrien-1-ol.yaml
    sha256: e2e01fb080da4f59d0530dbcd6eeff9b871088e42c77aab04b30a80a3e23c7ca
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
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: reports/yaml_record_review/20260922T163539Z-9z-12z-15z-octadecatrien-1-ol.md
    sha256: bfc2cd1d03074bde3da175b79d4d1f26a0c05861319753b3b5bca0942bf72b42
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
- target_id: CHEBI:77474
  path: data/antibiotics/antibacterial/9z-12z-15z-octadecatrien-1-ol.yaml
  label: (9Z,12Z,15Z)-octadecatrien-1-ol
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
  description: Whole-record scientific review of one exact linolenyl alcohol record.
  selection: Queue072; CHEBI:77474 in isolated batch008.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:77474
  exclusions:
  - target: Linoleyl, tridecan-1-ol, stearyl alcohol, linolenic acid, derived esters,
      aldehydes and mixed extracts
    reason: Comparator or biotransformation context; their effects are not transferred
      to linolenyl alcohol.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - CHEBI:77474
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/9z-12z-15z-octadecatrien-1-ol.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - CHEBI:77474
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/9z-12z-15z-octadecatrien-1-ol.yaml --out /private/tmp/am-review-session/072-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Structure consistency
  status: passed
  required: true
  summary: Both encodings, locants and live authorities agree.
  target_ids:
  - CHEBI:77474
  evidence_ids:
  - chemistry
  - chebi
  - pubchem
- check_id: adapter
  name: Structured source applicability
  status: not_applicable
  required: false
  summary: No native named gene, protein, pathway, regulator, stress response or transcriptomic
    dataset; generic membrane speculation discovered in literature is not a specific
    covered module assertion.
  target_ids:
  - CHEBI:77474
  evidence_ids:
  - native
  - '1984'
- check_id: primary-access
  name: Original primary access
  status: passed
  required: false
  summary: Complete1984 page scans and patent text inspected;1982 paper remains abstract-only.
  target_ids:
  - CHEBI:77474
  evidence_ids:
  - '1984'
  - search
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:77474
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
  - CHEBI:77474
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
  - CHEBI:77474
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
  - CHEBI:77474
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
  - CHEBI:77474
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
  - CHEBI:77474
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
  - CHEBI:77474
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
  - CHEBI:77474
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
  - CHEBI:77474
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/9z-12z-15z-octadecatrien-1-ol.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T08:25:00Z'
  support: supports
  summary: Read label, five exact synonyms, structural definition, single parent,
    antibacterial role, both structure encodings, formula, charge, masses, CAS/Reaxys
    identifiers, three document_xrefs, source metadata and all four seed/reseed events.
    No quantitative activity, molecular target, mechanism, producer, resistance, clinical,
    dataset or causal-graph assertion is native.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Row1960; PATHS2228; configuration/extractor/seeder
  accessed_at: '2026-10-21T08:25:00Z'
  support: supports
  summary: Raw identity and fields agree; source leads are PMIDs16186620,21338674,6508262,6763859.
    Patents correctly move from raw xrefs into document_xrefs. Mint antibioticmech:chebi-2d0da980dd
    reproduces. Imported corrections belong to raw/extractor/seeder; future scientific
    annotations belong to the native record through validated writer/history.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:77474
  locator: Names, structure, ontology, registry and document references
  accessed_at: '2026-10-21T08:22:33Z'
  support: supports
  summary: Current ChEBI gives the same all-Z C18 primary alcohol, neutral C18H32O,
    key IKYKEVDKGZYRMQ-PDBXOOCHSA-N, mass264.453/exact264.24532, five synonyms, parent,
    antibacterial role, CAS506-44-5, Reaxys2101049 and three patent references.
  snapshot_sha256: cd36cc91ff4c04d6b8ead7a069b3580ab00c58caa62183546c635b26ed8a474a
- evidence_id: parent
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:77396
  locator: Official definition and outgoing relation
  accessed_at: '2026-10-21T08:22:34Z'
  support: supports
  summary: Long-chain primary fatty alcohol is a strictly broader class; the hydroxy-bearing
    methylene and long C18 chain satisfy the structural definition.
  snapshot_sha256: 04e4775028d6f03a986199846430424bc6752bdba7a8d39f6568244cdd38b13b
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/6436081
  locator: Full-key PUG resolution
  accessed_at: '2026-10-21T08:22:32Z'
  support: supports
  summary: Exact full-key lookup returns CID6436081, identical all-Z InChI/key, C18H32O,
    neutral charge and compatible masses. PubChem identity page also lists CAS506-44-5
    from CAS Common Chemistry and other authorities.
  snapshot_sha256: 8ebaca52bdd9894030c16f9ac36cfeb289abcb63ecc7f29e344f0c3882724488
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit structure calculation
  locator: Both native encodings; numbering from hydroxy-bearing carbon
  accessed_at: '2026-10-21T08:23:48Z'
  support: supports
  summary: Both reproduce the complete key, formula, neutral charge, one fragment,
    mass264.453/exact264.245315644 and three Z bonds. Explicit numbering places them
    at9–10,12–13,15–16.
  snapshot_sha256: be66c6d5380db01c35ee3e5c9026457f44ee81f53c7f550bd8d0b46dc6e481b3
- evidence_id: '1982'
  kind: primary_source
  reference: PMID:6763859
  locator: DOI10.1016/0003-9969(82)90008-5; primary abstract
  accessed_at: '2026-10-21T08:22:33Z'
  support: supports
  summary: Linolenyl and linoleyl alcohol inhibit the tested bacteria; S.mutans BHT
    is the main test strain. Gram-positive/Gram-negative statements concern the tested
    panel. Repeated exposure of BHT did not alter sensitivity, and cell-associated
    linolenyl alcohol was detected after24h without detected linolenic acid. These
    observations do not prove a molecular target, universal inability to evolve resistance
    or clinical efficacy. Full original methods were not accessible.
  snapshot_sha256: 14b627a9607f823e83124749e157e32957918773ace41721b7c85c30e13635da
- evidence_id: '1984'
  kind: primary_source
  reference: PMID:6508262
  locator: DOI10.1128/AAC.26.3.306; complete original pp306–309; Figure2 and Discussion
  accessed_at: '2026-10-21T08:23:03Z'
  support: supports
  summary: All four page scans were read. Nu Chek Prep alcohols were at least99% pure
    by TLC/GLC. S.mutans BHT grew in7mL Todd-Hewitt broth at37°C aerobically; inoculum1–5×10^7CFU/mL;
    ethanol controls and1.1mM ascorbic acid with linolenyl alcohol limited autooxidation.
    At22µM linolenyl alcohol slowed growth but CFU rose about2 logs by24h. Linolenyl
    plus gentamicin1.4µg/mL was bacteriostatic; the bactericidal combination belonged
    to tridecan-1-ol. Proposed membrane spacing/permeability remained mechanistic
    interpretation.
  snapshot_sha256: 760bbea7d43959e294f2bc3505378912231f2ad8691e1980dcb5309f37c51caa
- evidence_id: mycoplasma
  kind: primary_source
  reference: PMID:6794448
  locator: DOI10.1128/AAC.19.5.917; primary abstract on PubMed/PMC181542
  accessed_at: '2026-10-21T08:25:00Z'
  support: context_only
  summary: Additional primary abstract reports linolenyl, linoleyl and oleyl alcohols
    as less effective under its mycoplasma test conditions than the saturated alcohols.
    Cholesterol reversal and electron-micrograph experiments concern stearyl alcohol,
    not linolenyl. This is a bounded additional activity lead; full original table
    values were not extracted.
- evidence_id: ester
  kind: primary_source
  reference: PMID:16186620
  locator: DOI10.1385/abab:127:1:017; primary abstract
  accessed_at: '2026-10-21T08:22:37Z'
  support: context_only
  summary: Linolenyl alcohol is an esterification substrate. The antiradical result
    concerns linolenyl dihydrocaffeate, a distinct ester product, not antibacterial
    action of this free alcohol.
  snapshot_sha256: 84c81f50bf7ab233b70f070d576d453b8e256adc09452e415dd7a1d183050d3a
- evidence_id: pheromone
  kind: primary_source
  reference: PMID:21338674
  locator: DOI10.1016/j.ibmb.2011.02.004; primary abstract
  accessed_at: '2026-10-21T08:22:33Z'
  support: context_only
  summary: Labeled linolenyl alcohol was converted to a labeled pheromone aldehyde
    in Hyphantria cunea glands. Substrate conversion and enzyme selectivity are not
    proof of bacterial inhibition or de novo biosynthesis of the administered alcohol.
  snapshot_sha256: e3d72ff2bb1d72631680b3c9dfa2f6bbc3ddad06cdfea27f4fb3b45b29332d12
- evidence_id: patent-4209533
  kind: primary_source
  reference: https://patents.google.com/patent/US4209533A/en
  locator: Description, experimental tables and family statement
  accessed_at: '2026-10-21T08:22:33Z'
  support: context_only
  summary: Original patent describes linolenyl/linoleyl alcohol antibacterial uses
    and broth growth curves in Klett units. The document is relevant and correctly
    placed in document_xrefs, not exact chemical xrefs. Patent claims span compounds/formulations
    and are not clinical authorization or independent family replications. The inspected
    text does not specify a complete Z/Z/Z material identity; numerical transfer requires
    preparation mapping.
  snapshot_sha256: d79ccc4c42bf61035a42c5d79671b623647f0baf405c6100afa6adbcc71a7681
- evidence_id: patent-4340628
  kind: primary_source
  reference: https://patents.google.com/patent/US4340628A/en
  locator: Description, experimental tables and family statement
  accessed_at: '2026-10-21T08:22:33Z'
  support: context_only
  summary: Division of the original patent describes linolenyl/linoleyl alcohol antibacterial
    uses and broth growth curves in Klett units. The document is relevant and correctly
    placed in document_xrefs, not exact chemical xrefs. Patent claims span compounds/formulations
    and are not clinical authorization or independent family replications. The inspected
    text does not specify a complete Z/Z/Z material identity; numerical transfer requires
    preparation mapping.
  snapshot_sha256: 510f898d6f1c942c4ff8aef61c51fb426f99b8922cf3d47d2d94ae76cab5204e
- evidence_id: patent-4372978
  kind: primary_source
  reference: https://patents.google.com/patent/US4372978A/en
  locator: Description, experimental tables and family statement
  accessed_at: '2026-10-21T08:22:33Z'
  support: context_only
  summary: Further division in the same family describes linolenyl/linoleyl alcohol
    antibacterial uses and broth growth curves in Klett units. The document is relevant
    and correctly placed in document_xrefs, not exact chemical xrefs. Patent claims
    span compounds/formulations and are not clinical authorization or independent
    family replications. The inspected text does not specify a complete Z/Z/Z material
    identity; numerical transfer requires preparation mapping.
  snapshot_sha256: 7d754d9e0979f3d58a7d0d82d049d33b8ae3c8019255003fc2bf490e50d37016
- evidence_id: patent-boundaries
  kind: primary_source
  reference: https://patents.google.com/patent/US4372978A/en
  locator: Tables2–3,6,9 and accompanying interpretation
  accessed_at: '2026-10-21T08:22:33Z'
  support: context_only
  summary: Table3 reports delayed growth of S.mutans BHT and a5h half-growth response
    near2.54nmol/mL; that is not a standard MIC. The patent infers lysis/death from
    reduced opacity in Clostridium cultures rather than establishing a direct molecular
    mechanism. Around Table9, prose alternates linoleyl and linolenyl while rows say
    linolenyl; preserve this source conflict before transferring E.coli results.
  snapshot_sha256: 7d754d9e0979f3d58a7d0d82d049d33b8ae3c8019255003fc2bf490e50d37016
- evidence_id: registries
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:77474
  locator: Registry Numbers
  accessed_at: '2026-10-21T08:25:00Z'
  support: partial
  summary: CAS506-44-5 agrees with current official ChEBI/PubChem identity. Reaxys2101049
    was only verified as an official ChEBI assertion; independent restricted-registry
    structure detail remains unavailable.
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive repository search and free primary discovery
  accessed_at: '2026-10-21T08:25:00Z'
  support: context_only
  summary: Full native/raw/PATHS/config and maintained curation surfaces were checked.
    The historical report is only discovery context and its optional-field-based major
    finding is not adopted. All four adopted abstracts were read, the complete1984
    paper was inspected as page scans, and patent descriptions/tables were examined.1982
    publisher access supplied abstract only.
  search_scope: prepare.py72 used rg --no-ignore --hidden for ID,label,slug across
    batch008 excluding.git/.venv; follow-up full-key/raw and maintained curation searches.
    Free queries used linolenyl alcohol,506-44-5, exact label,1982title and DOI, plus
    linked PMC/primary sources. Generic extract/metabolomics/vendor claims were not
    used as exact-compound assay evidence.
- evidence_id: gates
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual focused commands in batch008
  accessed_at: '2026-10-21T08:23:48Z'
  support: supports
  summary: Both validators exited0; one record and zero strictERROR rows.
  snapshot_sha256: 0367dabc61e57ebfa617401a82f422943bd63845bebe00f74145e60f36eb1e27
assessments:
- assessment_id: identity
  area: identity
  topic: Exact free all-Z fatty alcohol
  outcome: supported
  summary: Native names, full encodings, current ChEBI and exact-key PubChem agree.
    Independent locant/CIP checks support all three Z bonds.
  target_ids:
  - CHEBI:77474
  evidence_ids:
  - native
  - chebi
  - pubchem
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Broader parent and antibacterial filing
  outcome: supported
  summary: Parent is broader; compound-specific1982 and1984 primary evidence supports
    antibacterial activity under tested conditions.
  target_ids:
  - CHEBI:77474
  evidence_ids:
  - parent
  - chebi
  - '1982'
  - '1984'
- assessment_id: documents
  area: provenance
  topic: Patent references and identity boundary
  outcome: supported
  summary: All three patent documents resolve and concern named linolenyl alcohol.
    Their placement in document_xrefs is correct; family repetition, claim breadth
    and unreported full stereochemical specification limit assay transfer.
  target_ids:
  - CHEBI:77474
  evidence_ids:
  - native
  - patent-4209533
  - patent-4340628
  - patent-4372978
  - patent-boundaries
- assessment_id: activity
  area: evidence
  topic: Specific comparator and combination assays
  outcome: supported
  summary: The1984 comparator supplies explicit dose, strain, medium, antioxidant,
    time andCFU context. Linolenyl alone slowed growth; its gentamicin combination
    was bacteriostatic in that assay. Preserve the more potent tridecan-1-ol comparison
    and do not recast a growth curve as MIC.
  target_ids:
  - CHEBI:77474
  evidence_ids:
  - '1984'
  - '1982'
  - mycoplasma
  - patent-boundaries
- assessment_id: mechanism
  area: evidence
  topic: Membrane hypothesis versus direct target
  outcome: unknown
  summary: No native mechanism is asserted. The1984 authors propose a membrane effect
    but provide no linolenyl-specific direct binding or definitive molecular target.
    A target or causal graph should not be forced from class analogy or tridecan-1-ol
    synergy.
  target_ids:
  - CHEBI:77474
  evidence_ids:
  - native
  - '1984'
- assessment_id: resistance
  area: scope
  topic: Repeated-exposure phenotype
  outcome: supported
  summary: The1982 abstract’s unchanged BHT sensitivity is bounded to its exposure
    protocol and strain, not a universal resistance claim. Native resistance fields
    are empty and appropriate.
  target_ids:
  - CHEBI:77474
  evidence_ids:
  - native
  - '1982'
- assessment_id: producer
  area: scope
  topic: Biotransformation and ester products
  outcome: not_applicable
  summary: No producer claim is native. Insect conversion of added labeled alcohol
    and enzyme-made ester production do not establish endogenous alcohol production
    or antibacterial action of the same chemical form.
  target_ids:
  - CHEBI:77474
  evidence_ids:
  - native
  - ester
  - pheromone
- assessment_id: clinical
  area: scope
  topic: Proposed dental products versus clinical status
  outcome: not_applicable
  summary: Patent and paper proposals do not establish approved products, efficacy
    in patients or clinical status; none is asserted natively.
  target_ids:
  - CHEBI:77474
  evidence_ids:
  - native
  - '1982'
  - patent-4209533
- assessment_id: completeness
  area: completeness
  topic: Quantitative follow-up and optional fields
  outcome: unknown
  summary: Concrete1984 comparator results and1982/patent leads can support future
    method-qualified observations after form/source adjudication. Optional blank activity/target/dataset/graph
    fields alone do not establish a corrective defect.
  target_ids:
  - CHEBI:77474
  evidence_ids:
  - '1984'
  - '1982'
  - patent-boundaries
  - search
- assessment_id: registry
  area: provenance
  topic: Chemical registry references
  outcome: unknown
  summary: CAS is consistent across authorities; independent Reaxys equivalence remains
    source-asserted with no demonstrated mismatch.
  target_ids:
  - CHEBI:77474
  evidence_ids:
  - registries
  - chebi
  - pubchem
- assessment_id: history
  area: provenance
  topic: Generated owner and history
  outcome: supported
  summary: Adopted source metadata, reproducible mint, filing and four history events
    agree; SEEDED remains unchanged.
  target_ids:
  - CHEBI:77474
  evidence_ids:
  - native
  - owner
  - chemistry
- assessment_id: schema
  area: schema
  topic: Focused validators
  outcome: supported
  summary: Both native focused gates pass.
  target_ids:
  - CHEBI:77474
  evidence_ids:
  - gates
findings: []
actions: []
limitations:
- The1982 paper remains abstract-only. Its full material characterization, quantitative
  doses and repeated-exposure protocol were not inspected.
- The1984 paper names commercial linolenyl alcohol with at least99% chromatographic
  purity but does not provide a complete stereochemical structure or catalog identifier;
  exact all-Z mapping is supported by current name/registry authorities rather than
  independent reanalysis of the historical material.
- Patent numbers are valid document references. Their broad formulations, repeated
  family data, opacity-based lysis inference and linoleyl/linolenyl wording conflict
  require adjudication before quantitative transfer.
- Independent Reaxys detail was unavailable; the bounded literature search is not
  an assertion that no additional exact-compound evidence exists.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All21 captured input hashes were rechecked unchanged; no native fields, history
  or scientific status were changed.
- 'Concrete follow-up: curate or explicitly defer1984 Figure2 comparator observations
  with22µM alcohol,1.1mM ascorbic acid,37°C aerobic Todd-Hewitt medium,BHT strain,time
  andCFU endpoint. Keep alcohol alone and gentamicin combination separate; no MIC
  or proven membrane target follows.'
- Original1984 printed pages306,307,308,309 correspond respectively to scratch072-page4,page3,page1,page2;
  manifest stores original URLs and image hashes.
- Historical optional-field-based major finding is not adopted.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:77474
- https://pmc.ncbi.nlm.nih.gov/articles/PMC176158/
- https://doi.org/10.1016/0003-9969(82)90008-5
tags:
- antibacterial
- fatty-alcohol
- exact-stereochemistry
- combination-assay
- seeded
```
