# Geranylgeranyl acetate: coherent exact seed with bounded primary activity support

- Review: 20261021T173858Z-geranylgeranyl-acetate-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:27:37Z
- Finished UTC: 2026-10-21T17:38:58Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The all-trans geranylgeranyl acetate structure, four exact synonyms, acetate-ester parent and both external chemical references are mutually consistent and corroborated by current official authorities. The adopted original antimycobacterial abstract directly supports the qualitative antibacterial role, while its full experimental methods were not accessible. The other eight adopted leads concern insect chemistry, chemical transformations, an essential-oil formulation or host biology and do not establish an antibacterial target. No confirmed defect was found; optional activity and mechanism fields need not be populated. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 501; entire exact record. All thirteen original input hashes were verified unchanged before judgment. The initial capture already contains the actual ChEBI inventory, role mapping, extractor and seeder owners; no extra source owner was required.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:229666 | data/antibiotics/antibacterial/geranylgeranyl-acetate.yaml | generated | geranylgeranyl acetate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | CHEBI:229666 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:229666 | Actual focused execution exited 0. |
| Focused chemistry verification | passed | False | CHEBI:229666 | Actual focused execution exited 0. |
| Independent exact chemical authority comparison | passed | False | CHEBI:229666 | All eight native, ChEBI, PubChem and LIPID MAPS SMILES/InChI encodings give the same full stereochemical key, formula and neutral charge. |
| Authoritative full QC | failed | True | CHEBI:229666 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:229666 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:229666 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:229666 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:229666 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:229666 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:229666 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:229666 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:229666 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact ester, all-trans names, quantities and external equivalences

identity: supported. Targets: CHEBI:229666.

ChEBI, NIST, LIPID MAPS and corroborating PubChem agree on the exact all-trans neutral acetate. Both external xrefs are verified at structure level; the structural definition and all four native synonyms are coherent.

### Broader parent and antibacterial role

grounding: supported. Targets: CHEBI:229666.

Acetate ester is a valid strictly broader class. The adopted original antibacterial abstract directly names and tests the acetate, supporting CHEBI33282 and ANTIBACTERIAL filing, with full assay/material limitations retained.

### All nine adopted publication leads

evidence: supported. Targets: CHEBI:229666.

All nine identifiers resolve and their actual inspected depth is recorded: eight available abstracts plus metadata without abstract for PMID6047693, with selected 2017 original main text additionally read. Activity is grounded to the exact antimycobacterial paper, not insect, host, mixture or derivative experiments.

### Optional mechanism, activity and producer detail

completeness: unknown. Targets: CHEBI:229666.

No specific antibacterial mechanism was established in this bounded review. The optional fields are absent rather than incorrectly inferred. Full activity Methods would be needed before any numerical enrichment, and occurrence in insects or an oil mixture is not sufficient for a new de novo producer claim.

### Source reproduction, exact grounding and seed history

provenance: supported. Targets: CHEBI:229666.

The exact ChEBI row owns all native fields; the source-concept mint and exact identifier serve their intended distinct provenance roles. Three seed/reseed events are consistent with SEEDED status. All original input hashes are preserved.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

If quantitative activity or mechanism enrichment is undertaken, inspect the exact original experiment and preserve material and assay scope.

- Obtain and inspect PMID17924309 full Methods and exact compound characterization before turning the abstract MIC into a structured observation; preserve strain, medium, inoculum, time, endpoint and E/Z/purity context.
- Do not transfer geranylgeraniol, geranyl acetate, epoxide/halogenated derivative, frankincense-mixture or host-cell results to the exact ester.
- Do not assign an antibacterial target from lipophilicity, an insect pheromone phenotype or host protein-homeostasis background alone. Absence of optional target/graph/producer slots does not itself require a correction.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/geranylgeranyl-acetate.yaml; Entire YAML, including identity, definition, four exact synonyms, parent, activity role, all chemistry, two exact xrefs, source concept and three history events. | supports | The record denotes one neutral all-trans geranylgeranyl acetate structure and is SEEDED with EXACT ChEBI grounding. It contains no antibacterial mechanism, target, resistance, quantitative activity, producer, clinical assertion, dataset or causal graph. Its definition is structural rather than an unqualified activity or biosynthesis claim. The source-concept mint is provenance for the ChEBI concept, not a conflicting native identifier. History records source seeding and reseeding, not scientific sign-off. |
| owners | data/raw/chebi_antimicrobials.tsv:2908; data/raw/chebi_role_names.tsv:22; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; curation/decisions.tsv; Complete exact ChEBI row and role-name row; relevant three-star/relation-status scope filters, structure/name/xref extraction and source-precedence/class/role seeding logic. | supports | Every native imported field is present in the exact ChEBI inventory row. Its nine adopted publication leads were resolved individually. The source role is antibacterial agent and the structural parent is acetate ester; the generator preserves the role when filing the record as ANTIBACTERIAL. No exact curator row or decision override was found in the inspected complete tables and hidden-inclusive local search. Existing input ownership is accurate and all thirteen original hashes remain intact. |
| chebi | CHEBI:229666; https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:229666; Complete current official compound entry, names, structure, properties, relations, external references and all nine citation identifiers. | supports | Current three-star ChEBI agrees with the native definition, all four exact names, all-trans structure, formula C22H36O2, charge 0 and full key NHYSRKKHKHCRGR-RFRQLJORSA-N. The three geometrically distinguishable alkene positions are 2E,6E,10E; the terminal alkene with identical methyl substituents does not add another E/Z assignment. The acetate ester is distinct from geranylgeraniol and geranyl acetate. ChEBI also contains an out-of-antimicrobial-scope pheromone role, which need not be copied into this repository’s activity_roles slice. |
| parent | CHEBI:47622; CHEBI:33282; Current official parent and role definitions and their relation to the exact compound. | supports | CHEBI47622 is the class of carboxylic esters whose acid component is acetic acid. It is strictly broader than this individual ester. CHEBI33282 is antibacterial agent, meaning a substance or active part that kills or slows bacterial growth. The native parent/class and role are supported without implying clinical approval or a universal bacterial spectrum. |
| nist | cas:61691-98-3; https://webbook.nist.gov/cgi/cbook.cgi?ID=61691-98-3; Complete official NIST identity section, exact CAS, InChI, key, formula and names. | supports | NIST explicitly associates CAS61691-98-3 with the E,E,E acetate and reproduces the full native InChI and key. It independently corroborates the exact systematic synonyms. Its displayed molecular weight 332.5200 differs slightly from ChEBI’s 332.528 convention/precision, while formula and exact identity agree; the native ChEBI value is internally consistent and this is not a wrong-structure finding. |
| lipidmaps | lipidmaps:LMFA07010351; https://www.lipidmaps.org/rest/compound/lm_id/LMFA07010351/all/json; Complete official LIPID MAPS record and independent parsing of its SMILES and InChI; corroborating PubChem CAS-query response. | supports | LIPID MAPS names geranylgeranyl acetate with the exact 2E,6E,10E systematic name, C22H36O2, exact mass 332.271531 and native full key. Its structure parses to the same exact graph. PubChem CAS lookup resolves to CID5366012 with the same graph and supports the rounded masses. No exact-reference mismatch was found; SFE 22:4 is a database shorthand, not a new native synonym asserting a broad lipid class. |
| antibacterial | PMID:17924309; DOI:10.1055/s-2007-990238; https://pubmed.ncbi.nlm.nih.gov/17924309/; Complete original indexed abstract. Publisher full-text PDF endpoint returned an HTML waiting/challenge page, not a PDF; no full Methods or Table was inspected. | partial | Vik, James and Gundersen explicitly tested terpenes and synthetic analogues against Mycobacterium tuberculosis in the microplate Alamar Blue assay. The abstract distinguishes geranylgeraniol from geranylgeranyl acetate and reports MIC 3.13 micrograms/mL for the acetate. This directly supports the native qualitative antibacterial role. The available abstract does not establish the exact strain, medium, incubation, endpoint implementation, purity or E/Z composition of the tested batch; therefore the numerical result is not presented as a complete curatable observation or clinical susceptibility threshold. |
| insect-leads | PMID:11382068; DOI:10.1023/a:1005667916765; PMID:17193334; DOI:10.1002/cbdv.200690099; PMID:19730955; DOI:10.1007/s10886-009-9679-4; PMID:28695826; DOI:10.7554/elife.24063; All four complete indexed abstracts; selected original 2017 main-text chemistry, biological Results and synthesis Methods additionally inspected. | context_only | The 2001 and 2006 originals identify all-trans acetate in bee gland secretions, and the 2009 abstract describes GC-MS profiles of stingless-bee extracts. These are occurrence/chemical-ecology sources, not exact bacterial activity or de novo producer experiments. The 2017 original tests Lygus reproductive communication and distinguishes GGA from its alcohol GGOH. None establishes an antibacterial target for this record. |
| insect-primary | PMID:28695826; DOI:10.7554/elife.24063; https://pmc.ncbi.nlm.nih.gov/articles/PMC5505696/; Selected original introduction, GC-MS identity Results, relevant behavioral Discussion and synthesis/identity Methods; figure captions read, figures and raw source data not independently reprocessed. | context_only | The study compares extract retention times and mass spectra with authentic standards. It prepares geranylgeranyl acetate by acetylating commercial geranylgeraniol with acetic anhydride/pyridine, reporting 96% GC purity after chromatography. Its experiments concern mating-associated pheromone behavior and changing acetate/alcohol abundance. This provides independent chemistry context but no antibacterial mechanism; conversion in females is not automatically a native biosynthetic-producer assertion. |
| other-leads | PMID:16839173; DOI:10.1021/jo060760d; PMID:32505743; DOI:10.1053/j.gastro.2020.05.080; PMID:36277209; DOI:10.3389/fphys.2022.1001136; PMID:6047693; DOI:10.1021/ja00977a052; Complete available indexed abstracts and identifier metadata; PMID6047693 has no indexed abstract. | context_only | PMID16839173 describes allylic chlorination of polyprenoid substrates and subsequent derivatives, not a parent-acetate antibacterial mechanism. PMID36277209 measures frankincense essential-oil nanoemulsion effects on insect larvae and identifies the acetate as one GC-MS constituent; mixture activity cannot be transferred to the pure compound. PMID32505743 is a host biliary-atresia/redox and protein-homeostasis study; its abstract does not establish an exact acetate antibacterial target, and full text was not obtained from the attempted XML endpoint. PMID6047693 concerns laboratory cyclization of a terminal epoxide derivative; with no indexed abstract, neither its full identity mapping nor activity is verified. These sources remain bounded leads, not transferable mechanistic evidence. |
| search | 501-inclusive-hits.txt; 501-fetch-results.json; 501-fetch2-results.json; Hidden- and ignored-inclusive local identity/source search; exact official chemical records and nine PMID/DOI retrieval; bounded public search for the 2007 original. | context_only | Local searches included data, curation, conf, scripts, src, docs, .claude, reviews and reports. Public searches used the exact title, DOI and geranylgeranyl acetate/antibacterial identifiers. The accessible sources establish a positive activity lead, not absence of mechanism literature. Structured transcriptomic adapters are not applicable: no native gene, protein, regulator, pathway, stress response or dataset is asserted. Newly encountered host or biosynthesis background was not promoted into native mechanism. |
| checks | 501-focused-results.json; 501-chemistry.json; 501-authority-chemistry.json; Actual focused schema/strict/chemistry and independent multi-authority graph comparison. | supports | All commands exited 0. SMILES and InChI reproduce formula, neutral charge, masses and the full key. Eight authority/native encodings agree, and all thirteen original captured input hashes remain unchanged. These deterministic checks do not substitute for missing full activity Methods. |

## Limits And Additional Notes

- The main antibacterial original PMID17924309 was inspected only at complete indexed-abstract depth. Its public publisher PDF route returned an HTML waiting/challenge document, and bounded exact-title/DOI searches did not yield a readable free full text. Detailed assay conditions, selectivity controls and batch geometry/purity therefore remain unverified.
- All nine adopted citation identifiers were resolved. PMID6047693 has no indexed abstract; the other eight abstracts were read. Only selected chemical/behavioral sections and figure captions of the 2017 insect paper were additionally inspected; other full papers, primary figures and supplements were not all read.
- The host biliary-atresia source PMID32505743 remained abstract-level after its EuropePMC XML endpoint returned 500. No exact-compound host target or antibacterial mechanism is inferred from that abstract.
- NIST and ChEBI display slightly different average-mass conventions, but their formula, full InChI and key agree. Native masses match its stated ChEBI source and independent internal checks.
- An initial scratch source-row filter accidentally matched the common antibacterial role across many unrelated rows; it was narrowed to the exact compound and the exact role-name row before the evidence was assessed. No original capture or repository input was changed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Fetch manifests preserve actual source timestamps and SHA256 values. Despite its .pdf filename, 501-2007-original.pdf is HTML and was not represented as inspected full text.
- No corrected source or native content is proposed as mandatory. Optional enrichment does not change the zero-finding result of this bounded review.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T173858Z-geranylgeranyl-acetate-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Geranylgeranyl acetate: coherent exact seed with bounded primary activity
  support'
started_at: '2026-10-21T17:27:37Z'
finished_at: '2026-10-21T17:38:58Z'
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
summary: The all-trans geranylgeranyl acetate structure, four exact synonyms, acetate-ester
  parent and both external chemical references are mutually consistent and corroborated
  by current official authorities. The adopted original antimycobacterial abstract
  directly supports the qualitative antibacterial role, while its full experimental
  methods were not accessible. The other eight adopted leads concern insect chemistry,
  chemical transformations, an essential-oil formulation or host biology and do not
  establish an antibacterial target. No confirmed defect was found; optional activity
  and mechanism fields need not be populated. Scientific assessment retains the stated
  evidence limits; full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/geranylgeranyl-acetate.yaml
    sha256: 90cfd177544fdbc38cca87a9bec8e6e3e5d20568e472df2eec95f59daff4b185
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
- target_id: CHEBI:229666
  path: data/antibiotics/antibacterial/geranylgeranyl-acetate.yaml
  label: geranylgeranyl acetate
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
  selection: Queue position 501; entire exact record. All thirteen original input
    hashes were verified unchanged before judgment. The initial capture already contains
    the actual ChEBI inventory, role mapping, extractor and seeder owners; no extra
    source owner was required.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:229666
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:229666
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/geranylgeranyl-acetate.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:229666
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/geranylgeranyl-acetate.yaml --out /private/tmp/am-review-session/501-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:229666
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 501
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-chemistry
  name: Independent exact chemical authority comparison
  status: passed
  required: false
  summary: All eight native, ChEBI, PubChem and LIPID MAPS SMILES/InChI encodings
    give the same full stereochemical key, formula and neutral charge.
  target_ids:
  - CHEBI:229666
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/501-authority-check.py
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
  - CHEBI:229666
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
  - CHEBI:229666
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
  - CHEBI:229666
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
  - CHEBI:229666
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
  - CHEBI:229666
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
  - CHEBI:229666
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
  - CHEBI:229666
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
  - CHEBI:229666
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
  - CHEBI:229666
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/geranylgeranyl-acetate.yaml
  locator: Entire YAML, including identity, definition, four exact synonyms, parent,
    activity role, all chemistry, two exact xrefs, source concept and three history
    events.
  accessed_at: '2026-10-21T17:33:09Z'
  support: supports
  summary: The record denotes one neutral all-trans geranylgeranyl acetate structure
    and is SEEDED with EXACT ChEBI grounding. It contains no antibacterial mechanism,
    target, resistance, quantitative activity, producer, clinical assertion, dataset
    or causal graph. Its definition is structural rather than an unqualified activity
    or biosynthesis claim. The source-concept mint is provenance for the ChEBI concept,
    not a conflicting native identifier. History records source seeding and reseeding,
    not scientific sign-off.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv:2908; data/raw/chebi_role_names.tsv:22;
    conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py;
    curation/decisions.tsv
  locator: Complete exact ChEBI row and role-name row; relevant three-star/relation-status
    scope filters, structure/name/xref extraction and source-precedence/class/role
    seeding logic.
  accessed_at: '2026-10-21T17:33:09Z'
  support: supports
  summary: Every native imported field is present in the exact ChEBI inventory row.
    Its nine adopted publication leads were resolved individually. The source role
    is antibacterial agent and the structural parent is acetate ester; the generator
    preserves the role when filing the record as ANTIBACTERIAL. No exact curator row
    or decision override was found in the inspected complete tables and hidden-inclusive
    local search. Existing input ownership is accurate and all thirteen original hashes
    remain intact.
  snapshot_sha256: c9c9087648cf807328ac86516e004d593e80c9c31a347828c05ea288ddc49662
- evidence_id: chebi
  kind: authority
  reference: CHEBI:229666; https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:229666
  locator: Complete current official compound entry, names, structure, properties,
    relations, external references and all nine citation identifiers.
  accessed_at: '2026-10-21T17:31:14Z'
  support: supports
  summary: Current three-star ChEBI agrees with the native definition, all four exact
    names, all-trans structure, formula C22H36O2, charge 0 and full key NHYSRKKHKHCRGR-RFRQLJORSA-N.
    The three geometrically distinguishable alkene positions are 2E,6E,10E; the terminal
    alkene with identical methyl substituents does not add another E/Z assignment.
    The acetate ester is distinct from geranylgeraniol and geranyl acetate. ChEBI
    also contains an out-of-antimicrobial-scope pheromone role, which need not be
    copied into this repository’s activity_roles slice.
  snapshot_sha256: 873d8a11e3570044bb4d4a3ffe1880e045e11bf93839dca5c18c6d04e3e1ae17
- evidence_id: parent
  kind: authority
  reference: CHEBI:47622; CHEBI:33282
  locator: Current official parent and role definitions and their relation to the
    exact compound.
  accessed_at: '2026-10-21T17:31:14Z'
  support: supports
  summary: CHEBI47622 is the class of carboxylic esters whose acid component is acetic
    acid. It is strictly broader than this individual ester. CHEBI33282 is antibacterial
    agent, meaning a substance or active part that kills or slows bacterial growth.
    The native parent/class and role are supported without implying clinical approval
    or a universal bacterial spectrum.
  snapshot_sha256: 920adf6e3ca4fd81d4289410e249bcd5893dadac27014a9f753d82df2883a005
- evidence_id: nist
  kind: authority
  reference: cas:61691-98-3; https://webbook.nist.gov/cgi/cbook.cgi?ID=61691-98-3
  locator: Complete official NIST identity section, exact CAS, InChI, key, formula
    and names.
  accessed_at: '2026-10-21T17:31:46Z'
  support: supports
  summary: NIST explicitly associates CAS61691-98-3 with the E,E,E acetate and reproduces
    the full native InChI and key. It independently corroborates the exact systematic
    synonyms. Its displayed molecular weight 332.5200 differs slightly from ChEBI’s
    332.528 convention/precision, while formula and exact identity agree; the native
    ChEBI value is internally consistent and this is not a wrong-structure finding.
  snapshot_sha256: fe2bffb0fcbcf642ed6bc0377068dfda3c6e274db3499b0e6bda575753102297
- evidence_id: lipidmaps
  kind: authority
  reference: lipidmaps:LMFA07010351; https://www.lipidmaps.org/rest/compound/lm_id/LMFA07010351/all/json
  locator: Complete official LIPID MAPS record and independent parsing of its SMILES
    and InChI; corroborating PubChem CAS-query response.
  accessed_at: '2026-10-21T17:31:15Z'
  support: supports
  summary: LIPID MAPS names geranylgeranyl acetate with the exact 2E,6E,10E systematic
    name, C22H36O2, exact mass 332.271531 and native full key. Its structure parses
    to the same exact graph. PubChem CAS lookup resolves to CID5366012 with the same
    graph and supports the rounded masses. No exact-reference mismatch was found;
    SFE 22:4 is a database shorthand, not a new native synonym asserting a broad lipid
    class.
  snapshot_sha256: 7e6e150748948247eb82768ecfd47fa4e61a8cbec76a699bf562e25273d0c60e
- evidence_id: antibacterial
  kind: primary_source
  reference: PMID:17924309; DOI:10.1055/s-2007-990238; https://pubmed.ncbi.nlm.nih.gov/17924309/
  locator: Complete original indexed abstract. Publisher full-text PDF endpoint returned
    an HTML waiting/challenge page, not a PDF; no full Methods or Table was inspected.
  accessed_at: '2026-10-21T17:31:14Z'
  support: partial
  summary: Vik, James and Gundersen explicitly tested terpenes and synthetic analogues
    against Mycobacterium tuberculosis in the microplate Alamar Blue assay. The abstract
    distinguishes geranylgeraniol from geranylgeranyl acetate and reports MIC 3.13
    micrograms/mL for the acetate. This directly supports the native qualitative antibacterial
    role. The available abstract does not establish the exact strain, medium, incubation,
    endpoint implementation, purity or E/Z composition of the tested batch; therefore
    the numerical result is not presented as a complete curatable observation or clinical
    susceptibility threshold.
  snapshot_sha256: ea3091a57431229d2c9c3abc0ec7e8cbed3bed475320219fabc6f401ce2f8294
- evidence_id: insect-leads
  kind: database
  reference: PMID:11382068; DOI:10.1023/a:1005667916765; PMID:17193334; DOI:10.1002/cbdv.200690099;
    PMID:19730955; DOI:10.1007/s10886-009-9679-4; PMID:28695826; DOI:10.7554/elife.24063
  locator: All four complete indexed abstracts; selected original 2017 main-text chemistry,
    biological Results and synthesis Methods additionally inspected.
  accessed_at: '2026-10-21T17:31:14Z'
  support: context_only
  summary: The 2001 and 2006 originals identify all-trans acetate in bee gland secretions,
    and the 2009 abstract describes GC-MS profiles of stingless-bee extracts. These
    are occurrence/chemical-ecology sources, not exact bacterial activity or de novo
    producer experiments. The 2017 original tests Lygus reproductive communication
    and distinguishes GGA from its alcohol GGOH. None establishes an antibacterial
    target for this record.
  snapshot_sha256: ea3091a57431229d2c9c3abc0ec7e8cbed3bed475320219fabc6f401ce2f8294
- evidence_id: insect-primary
  kind: primary_source
  reference: PMID:28695826; DOI:10.7554/elife.24063; https://pmc.ncbi.nlm.nih.gov/articles/PMC5505696/
  locator: Selected original introduction, GC-MS identity Results, relevant behavioral
    Discussion and synthesis/identity Methods; figure captions read, figures and raw
    source data not independently reprocessed.
  accessed_at: '2026-10-21T17:31:46Z'
  support: context_only
  summary: The study compares extract retention times and mass spectra with authentic
    standards. It prepares geranylgeranyl acetate by acetylating commercial geranylgeraniol
    with acetic anhydride/pyridine, reporting 96% GC purity after chromatography.
    Its experiments concern mating-associated pheromone behavior and changing acetate/alcohol
    abundance. This provides independent chemistry context but no antibacterial mechanism;
    conversion in females is not automatically a native biosynthetic-producer assertion.
  snapshot_sha256: b34929efb3b8f179efae759c48f5bae19ca2dbd3c4770b89f3d26ba68b6c1e65
- evidence_id: other-leads
  kind: database
  reference: PMID:16839173; DOI:10.1021/jo060760d; PMID:32505743; DOI:10.1053/j.gastro.2020.05.080;
    PMID:36277209; DOI:10.3389/fphys.2022.1001136; PMID:6047693; DOI:10.1021/ja00977a052
  locator: Complete available indexed abstracts and identifier metadata; PMID6047693
    has no indexed abstract.
  accessed_at: '2026-10-21T17:31:14Z'
  support: context_only
  summary: PMID16839173 describes allylic chlorination of polyprenoid substrates and
    subsequent derivatives, not a parent-acetate antibacterial mechanism. PMID36277209
    measures frankincense essential-oil nanoemulsion effects on insect larvae and
    identifies the acetate as one GC-MS constituent; mixture activity cannot be transferred
    to the pure compound. PMID32505743 is a host biliary-atresia/redox and protein-homeostasis
    study; its abstract does not establish an exact acetate antibacterial target,
    and full text was not obtained from the attempted XML endpoint. PMID6047693 concerns
    laboratory cyclization of a terminal epoxide derivative; with no indexed abstract,
    neither its full identity mapping nor activity is verified. These sources remain
    bounded leads, not transferable mechanistic evidence.
  snapshot_sha256: ea3091a57431229d2c9c3abc0ec7e8cbed3bed475320219fabc6f401ce2f8294
- evidence_id: search
  kind: search
  reference: 501-inclusive-hits.txt; 501-fetch-results.json; 501-fetch2-results.json
  locator: Hidden- and ignored-inclusive local identity/source search; exact official
    chemical records and nine PMID/DOI retrieval; bounded public search for the 2007
    original.
  accessed_at: '2026-10-21T17:33:09Z'
  support: context_only
  summary: 'Local searches included data, curation, conf, scripts, src, docs, .claude,
    reviews and reports. Public searches used the exact title, DOI and geranylgeranyl
    acetate/antibacterial identifiers. The accessible sources establish a positive
    activity lead, not absence of mechanism literature. Structured transcriptomic
    adapters are not applicable: no native gene, protein, regulator, pathway, stress
    response or dataset is asserted. Newly encountered host or biosynthesis background
    was not promoted into native mechanism.'
  search_scope: 2026-10-21; rg --no-ignore --hidden for exact label/slug/CHEBI229666/full
    key across maintained and ignored-inclusive paths; PubMed/EuropePMC, ChEBI, NIST,
    LIPID MAPS, PubChem and bounded exact-title/DOI web search.
  snapshot_sha256: c9fc95e63a6f6ba88d72255d65145ca642d81a44140c2b4933e25092a0911cbd
- evidence_id: checks
  kind: validation
  reference: 501-focused-results.json; 501-chemistry.json; 501-authority-chemistry.json
  locator: Actual focused schema/strict/chemistry and independent multi-authority
    graph comparison.
  accessed_at: '2026-10-21T17:33:09Z'
  support: supports
  summary: All commands exited 0. SMILES and InChI reproduce formula, neutral charge,
    masses and the full key. Eight authority/native encodings agree, and all thirteen
    original captured input hashes remain unchanged. These deterministic checks do
    not substitute for missing full activity Methods.
  snapshot_sha256: 1ce74501ec7ec78d467fbba4d736926685beff3583d02e168625a20ed6ccd67d
assessments:
- assessment_id: identity
  area: identity
  topic: Exact ester, all-trans names, quantities and external equivalences
  outcome: supported
  summary: ChEBI, NIST, LIPID MAPS and corroborating PubChem agree on the exact all-trans
    neutral acetate. Both external xrefs are verified at structure level; the structural
    definition and all four native synonyms are coherent.
  target_ids:
  - CHEBI:229666
  evidence_ids:
  - chebi
  - nist
  - lipidmaps
  - checks
- assessment_id: classification
  area: grounding
  topic: Broader parent and antibacterial role
  outcome: supported
  summary: Acetate ester is a valid strictly broader class. The adopted original antibacterial
    abstract directly names and tests the acetate, supporting CHEBI33282 and ANTIBACTERIAL
    filing, with full assay/material limitations retained.
  target_ids:
  - CHEBI:229666
  evidence_ids:
  - parent
  - antibacterial
  - owners
- assessment_id: citation-scope
  area: evidence
  topic: All nine adopted publication leads
  outcome: supported
  summary: 'All nine identifiers resolve and their actual inspected depth is recorded:
    eight available abstracts plus metadata without abstract for PMID6047693, with
    selected 2017 original main text additionally read. Activity is grounded to the
    exact antimycobacterial paper, not insect, host, mixture or derivative experiments.'
  target_ids:
  - CHEBI:229666
  evidence_ids:
  - antibacterial
  - insect-leads
  - insect-primary
  - other-leads
- assessment_id: mechanism
  area: completeness
  topic: Optional mechanism, activity and producer detail
  outcome: unknown
  summary: No specific antibacterial mechanism was established in this bounded review.
    The optional fields are absent rather than incorrectly inferred. Full activity
    Methods would be needed before any numerical enrichment, and occurrence in insects
    or an oil mixture is not sufficient for a new de novo producer claim.
  target_ids:
  - CHEBI:229666
  evidence_ids:
  - native
  - antibacterial
  - insect-primary
  - other-leads
  - search
- assessment_id: provenance
  area: provenance
  topic: Source reproduction, exact grounding and seed history
  outcome: supported
  summary: The exact ChEBI row owns all native fields; the source-concept mint and
    exact identifier serve their intended distinct provenance roles. Three seed/reseed
    events are consistent with SEEDED status. All original input hashes are preserved.
  target_ids:
  - CHEBI:229666
  evidence_ids:
  - native
  - owners
  - checks
findings: []
actions:
- action_id: A1
  description: If quantitative activity or mechanism enrichment is undertaken, inspect
    the exact original experiment and preserve material and assay scope.
  finding_ids: []
  target_ids:
  - CHEBI:229666
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/geranylgeranyl-acetate.yaml
    role: Optional curator-owned evidence and activity additions through the validated
      writer
  acceptance_checks:
  - Obtain and inspect PMID17924309 full Methods and exact compound characterization
    before turning the abstract MIC into a structured observation; preserve strain,
    medium, inoculum, time, endpoint and E/Z/purity context.
  - Do not transfer geranylgeraniol, geranyl acetate, epoxide/halogenated derivative,
    frankincense-mixture or host-cell results to the exact ester.
  - Do not assign an antibacterial target from lipophilicity, an insect pheromone
    phenotype or host protein-homeostasis background alone. Absence of optional target/graph/producer
    slots does not itself require a correction.
limitations:
- The main antibacterial original PMID17924309 was inspected only at complete indexed-abstract
  depth. Its public publisher PDF route returned an HTML waiting/challenge document,
  and bounded exact-title/DOI searches did not yield a readable free full text. Detailed
  assay conditions, selectivity controls and batch geometry/purity therefore remain
  unverified.
- All nine adopted citation identifiers were resolved. PMID6047693 has no indexed
  abstract; the other eight abstracts were read. Only selected chemical/behavioral
  sections and figure captions of the 2017 insect paper were additionally inspected;
  other full papers, primary figures and supplements were not all read.
- The host biliary-atresia source PMID32505743 remained abstract-level after its EuropePMC
  XML endpoint returned 500. No exact-compound host target or antibacterial mechanism
  is inferred from that abstract.
- NIST and ChEBI display slightly different average-mass conventions, but their formula,
  full InChI and key agree. Native masses match its stated ChEBI source and independent
  internal checks.
- An initial scratch source-row filter accidentally matched the common antibacterial
  role across many unrelated rows; it was narrowed to the exact compound and the exact
  role-name row before the evidence was assessed. No original capture or repository
  input was changed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Fetch manifests preserve actual source timestamps and SHA256 values. Despite its
  .pdf filename, 501-2007-original.pdf is HTML and was not represented as inspected
  full text.
- No corrected source or native content is proposed as mandatory. Optional enrichment
  does not change the zero-finding result of this bounded review.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
