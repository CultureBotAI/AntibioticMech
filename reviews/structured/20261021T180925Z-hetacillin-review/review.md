# Hetacillin: exact identity and hydrolysis supported; enzyme contribution unresolved

- Review: 20261021T180925Z-hetacillin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:48:35Z
- Finished UTC: 2026-10-21T18:09:25Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The neutral hetacillin graph, aliases and exact chemical identifiers agree with current authorities and independent parsing. Original experiments demonstrate hydrolysis in defined aqueous buffer to ampicillin and acetone, and rapid assays also report transient activity attributed to intact hetacillin. The specific esterase contribution remains unresolved; buffer hydrolysis does not exclude an additional enzymatic route in vivo. The sole adopted 1966 paper was available only as bibliographic metadata. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 529; one whole exact native record. All thirteen original input hashes were verified and preserved; the actual adopted ARO owner was appended before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:5683 | data/antibiotics/antibacterial/hetacillin.yaml | generated | hetacillin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | CHEBI:5683 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:5683 | Actual focused execution exited 0. |
| Focused chemistry verification | passed | False | CHEBI:5683 | Actual focused execution exited 0. |
| Independent exact-structure authority comparison | passed | False | CHEBI:5683 | Ten native and authority encodings reproduce the same neutral graph, formula and four assigned stereocentres. |
| Structured source adapter before web research | passed | False | CHEBI:5683 | Actual catalog or esterase search; expression-module results are not conversion evidence. |
| Structured source adapter before web research | passed | False | CHEBI:5683 | Actual catalog or esterase search; expression-module results are not conversion evidence. |
| Authoritative full QC | failed | True | CHEBI:5683 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:5683 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:5683 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:5683 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:5683 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:5683 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:5683 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:5683 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:5683 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral molecule and aliases

identity: supported. Targets: CHEBI:5683.

Independent authorities and source chemistry agree on the neutral graph, stereochemistry, formula, masses and exact CAS. Broad drug/document associations remain distinct from exact xrefs.

### Parents, roles and antibacterial filing

grounding: supported. Targets: CHEBI:5683.

The penicillin scaffold and prodrug role are supported. Original neutral free-acid administration and compound-specific antibacterial experiments support the broad antibacterial context, while conversion, salt and endpoint boundaries prevent stronger material-specific claims.

### Specific conversion mechanism in the definition

evidence: unknown. Targets: CHEBI:5683.

Positive primary experiments support aqueous hydrolysis to ampicillin and acetone. The source databases repeat an unqualified esterase attribution, but the inspected primary evidence does not establish that attribution. The native wording does not explicitly make esterases necessary or exclusive, so the buffer experiments do not establish a contradiction. The adopted1966 paper remains unavailable at full-text depth.

### Intrinsic versus conversion-mediated activity

evidence: supported. Targets: CHEBI:5683.

The overall antibacterial/prodrug description is defensible. Earlier studies questioned intrinsic activity, whereas rapid1973 assays report transient parent-attributed effects. Preserve the experimental conflict and time/conversion dependence; neither generic inactivity nor a precise direct molecular target is established.

### Actual source owners and history

provenance: supported. Targets: CHEBI:5683.

Fourteen input hashes include the preserved original thirteen and appended ARO table. Source precedence explains the imported definition, and the source-concept/history shape is consistent with SEEDED status. Validation success is not scientific status promotion.

### Optional fields and possible enrichment

completeness: supported. Targets: CHEBI:5683.

No required representation was found missing. Optional quantitative activity, target, clinical, resistance, producer, graph or transcriptomic fields should not be filled by transferring ampicillin, salt, beta-lactamase or generic database annotations.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally strengthen the definition evidence by distinguishing demonstrated aqueous hydrolysis from an unresolved additional esterase contribution.

- If revising the definition, retain demonstrated hydrolysis to ampicillin and acetone and qualify the esterase contribution according to exact primary evidence. Buffer conversion alone is not proof that in vivo enzymatic conversion is false.
- Retain antibacterial/prodrug scope and do not replace it with universal parent inactivity. Preserve the rapid1973 assay result and its temporal, material and ampicillin-equivalent limits.
- Do not describe the unavailable1966 source as disproved. Regenerate the exact record through the maintained owner and pass focused schema/strict plus corpus reproduction checks.

### A2

If enriching optional scientific fields, preserve exact material and endpoint scope.

- Distinguish oral free-acid material, intramuscular potassium salt, kinetic potassium salt and the unspecified bulk form of the rapid-assay lot.
- Do not encode transient optical growth effects as MICs or transfer ampicillin PBP annotations into direct hetacillin binding evidence.
- Retain the adopted1966 full-text access limit until the actual paper is inspected; broader drug products do not establish a universal current clinical status.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/hetacillin.yaml; Entire native YAML, including seven synonyms, both parents and roles, structure, exact and drug references, two source concepts and four source history events. | supports | CHEBI:5683 denotes neutral hetacillin, C19H23N3O4S, DXVUYOAEDJXBPY-NFFDBFGFSA-N. The record is EXACT and SEEDED. Its definition cites PMID:5907864 and specifically attributes conversion to esterases. No molecular target, quantitative activity, resistance, producer, clinical assertion, causal graph, dataset or discussion is populated. |
| owners | data/raw/chebi_antimicrobials.tsv:187; data/raw/aro_antibiotics.tsv:591; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Complete exact source rows; relevant reviewed-edge, role/class, synonym and xref mapping; definition precedence and seeding sections; seven raw source lanes and owner search. | supports | The ChEBI row supplies identity, chemistry, aliases and roles but has no definition or literature lead. The ARO row supplies the definition and sole adopted PMID:5907864. The seeder therefore selects the ARO definition. DrugBank, DrugCentral and KEGG drug entries are deliberately broader drug_xrefs; patent and Wikipedia are documents. No applicable exact curator addition or decision was found by the hidden/ignored-inclusive search. Original thirteen hashes remain unchanged and the actual ARO input was appended. |
| chemistry | CHEBI:5683; pubchem.compound:443387; chembl.compound:CHEMBL1201116; kegg.compound:C11729; kegg.drug:D01074; cas:3511-16-8; Complete current structure responses and independent parsing of native, ChEBI, PubChem and ChEMBL SMILES/InChI plus both KEGG molfiles. | supports | All ten encodings reproduce the full neutral key, C19H23N3O4S and four stereocentres. The CAS query independently returns CID443387 with that graph. Native average and monoisotopic masses pass the focused diagnostic. The seven aliases describe the retained graph; INN translations and systematic names preserve stereochemistry. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/5683/; CHEBI:17334; CHEBI:33281; CHEBI:36047; Complete current exact term and the official parent/role definitions. | supports | The current term supports hetacillin identity, aliases, penicillin parent and antibacterial/prodrug roles. The penicillin class is compatible with the cyclic acylamino substituent. Beilstein5405483 is corroborated as a registry association on ChEBI, not by direct inspection of the registry. Later current citation leads are not silently treated as adopted record evidence. |
| aro | https://purl.obolibrary.org/obo/aro.obo; ARO:3009132; ARO:3009123; ARO:3000008; Exact current term and extended-spectrum penicillin/penicillin class stanzas; shared official snapshot fetched 2026-10-21T15:57:42Z, SHA256 d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4. | supports | Current ARO repeats the esterase attribution and PMID:5907864. Native ARO identity and broad penicillin structural classification agree with this source. This is source fidelity, not independent validation of the enzymatic attribution. |
| drug-associations | https://drugcentral.org/drugcard/1363; DrugBank:DB00739; KEGG:D01074; DrugCentral identity, synonyms and product/approval sections; public PubChem DrugBank-attributed metabolism field; current KEGG drug record and graph. | supports | DrugCentral1363 matches name, CAS and formula but also includes potassium-product context, appropriately represented as a broader drug association. No current clinical status is inferred. Direct DrugBank retrieval was unavailable; its text reproduced by PubChem explicitly attributes ampicillin formation to esterases. This corroborates a database assertion rather than providing an independent enzyme experiment. KEGG drug D01074 has the same graph but its target annotation is not promoted into native primary evidence. |
| documents | https://patents.google.com/patent/US3198804A/en; https://en.wikipedia.org/wiki/Hetacillin; Patent general description and Examples1–10 inspected; Wikipedia used only as a document and discovery lead, not primary experimental proof. | context_only | The patent describes ampicillin/acetone condensation and hydrolysis, free-acid isolation and separate salt/ester examples. Example7 concerns a methyl ester and Example10 a potassium salt; their material scope is not collapsed into the native neutral acid. Patent numerical biological tables were not comprehensively audited or transferred. The document links resolve to hetacillin context rather than asserting exact molecular equivalence. |
| adopted | PMID:5907864; DOI:10.1021/jo01341a060; Complete indexed bibliographic record and original publisher landing page; no indexed abstract and no accessible full text obtained. | context_only | Hardcastle and colleagues, The preparation and structure of hetacillin, J Org Chem31,897–899,1966, is the sole adopted lead. The publisher offers a PDF-only article and the attempted public routes did not supply it. The review cannot determine which definition clauses that paper supports; lack of access is not treated as a confirmed bad citation. |
| hydrolysis1967 | PMID:5182358; DOI:10.1136/bmj.2.5555.804; https://pmc.ncbi.nlm.nih.gov/articles/PMC1843140/; All five original scanned pages804–808 read through OCR, with pages804–806 independently viewed, including Figure1, reaction experiment, susceptibility methods and oral-material specification. | supports | The paper demonstrates conversion of hetacillin to ampicillin and acetone in defined phosphate buffer at pH7 and37 degrees C without an added esterase. TLC identifies ampicillin and gas chromatography measures acetone. Its oral volunteer comparison explicitly uses hetacillin free acid and ampicillin free acid; intramuscular comparisons use potassium hetacillin and sodium ampicillin. Overnight susceptibility and serum observations are confounded by conversion and are not direct target-binding experiments. The authors question substantial intrinsic activity but do not prove universal inactivity. |
| rapid1973 | PMID:4597707; DOI:10.1128/AAC.3.1.15; https://pmc.ncbi.nlm.nih.gov/articles/PMC444353/; All four original scanned pages15–18 independently viewed, including complete Methods, Results, Discussion and Figures1–6. | supports | Rapid optical growth assays of E. coli O14 and S. aureus S1 Oxford strain report transient effects attributed to intact hetacillin when beta-lactamase destroys released ampicillin. Concentrations are expressed as ampicillin equivalents. The tested hetacillin lot is identified, but its bulk counterion is not explicit. Buffer hydrolysis at pH6.7 and37 degrees C occurs without added esterase. The added bacterial penicillinase is a beta-lactamase used to distinguish activity, not evidence for esterase activation. The authors could not directly quantify conversion in bacterial cultures because of assay interference. These rapid growth effects are not MICs, permanent resistance or direct PBP binding; they caution against calling the parent universally inactive. |
| kinetics1974 | PMID:4468090; DOI:10.1248/cpb.22.2434; https://www.jstage.jst.go.jp/article/cpb1958/22/10/22_10_2434/_pdf; Complete ten-page original paper read by OCR; Methods page2435 and reaction Chart1 page2438 independently viewed. | supports | The study uses crystalline potassium hetacillin in defined aqueous buffers, normally at35 degrees C and controlled ionic strength, without added enzyme. Ampicillin and acetone formation are tracked chemically. The kinetic reaction scheme concerns hydrolysis of the acetone-derived cyclic adduct, with pH-dependent equilibrium and alkaline epimerization. It provides positive evidence for chemical conversion but does not exclude an additional enzymatic contribution in vivo. Salt material and kinetic experiments are not transferred as exact neutral-acid whole-cell MICs. |
| abstract-context | PMID:5514976; DOI:10.1159/000220703; PMID:18591; DOI:10.1002/jps.2600660727; Complete original publisher abstract for1970 and complete indexed abstract for1977; full papers not independently read. | supports | The1970 abstract describes aqueous conversion to ampicillin and acetone and suggests little intrinsic activity; this interpretation remains distinct from the rapid1973 experimental report. The1977 abstract concerns pH-dependent hydrolysis and epimerization. Neither is used to assign a bacterial protein target or assert that in vivo esterase participation is impossible. |
| adapter | iModulonDB e_coli/precise1k; 529-imodulondb-datasets.txt; 529-imodulondb-esterase.txt; Actual dataset catalog and esterase search run before open-ended web follow-up. | context_only | The bounded E. coli search returned ten gene hits, including aes, tesA and tesB, and no iModulon hits. The native esterase wording names no species or exact enzyme. Expression annotation cannot establish prodrug conversion, and no absence of an in vivo enzyme mechanism is inferred from this result. |
| search | 529-local-hits.txt; 529-owner-hits.txt; 529-literature.json; 529-fetch-results.json; 529-fetch2-results.json; 529-fetch3-results.json; 529-fetch4-results.json; Hidden/ignored-inclusive repository identifier/label/slug search and owner search by key/CAS; bounded public Europe PMC title/abstract and exact-name primary discovery. | context_only | The title/abstract query reported156 hits and returned the first100, including patent and follow-up records. Relevant exact-compound primary papers were selected and inspected at the stated depths. This search does not establish that no other enzyme experiment exists. |

## Limits And Additional Notes

- The sole adopted1966 publication has no indexed abstract and the attempted public publisher routes did not provide full text. Its precise support for individual definition clauses remains unresolved.
- The1967 paper was read completely through OCR with selected original pages804–806 visually checked; every numerical table cell was not independently transcribed. The1973 paper was visually read in full. The1974 paper was read completely through OCR with Methods and reaction-scheme images checked; raw experimental traces were not reanalysed.
- The1970 and1977 papers were read at complete abstract depth only. Direct DrugBank retrieval was unavailable, although its specific metabolism assertion was inspected through PubChem attribution. Beilstein was corroborated through ChEBI rather than directly.
- The reviewed buffer experiments establish chemical hydrolysis but do not exclude additional enzyme participation in vivo. The original literature differs in its interpretation of intrinsic activity, and exact bulk material is not equally specified across experiments.
- No exact bacterial protein-binding or clinical-resistance claim is introduced. The structured adapter is a bounded expression-context check and its lack of module hits is not negative biochemical evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Fetch manifests preserve actual URLs, UTC retrieval times, response failures and SHA256 values. Input hashes were rechecked before draft output.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T180925Z-hetacillin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Hetacillin: exact identity and hydrolysis supported; enzyme contribution unresolved'
started_at: '2026-10-21T17:48:35Z'
finished_at: '2026-10-21T18:09:25Z'
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
summary: The neutral hetacillin graph, aliases and exact chemical identifiers agree
  with current authorities and independent parsing. Original experiments demonstrate
  hydrolysis in defined aqueous buffer to ampicillin and acetone, and rapid assays
  also report transient activity attributed to intact hetacillin. The specific esterase
  contribution remains unresolved; buffer hydrolysis does not exclude an additional
  enzymatic route in vivo. The sole adopted 1966 paper was available only as bibliographic
  metadata. Scientific assessment retains the stated evidence limits; full verification
  is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/hetacillin.yaml
    sha256: 94430434cc4d3910e77053c8282d40bf1e52474d8078f46a0c99038cd509865d
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
- target_id: CHEBI:5683
  path: data/antibiotics/antibacterial/hetacillin.yaml
  label: hetacillin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
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
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 529; one whole exact native record. All thirteen original
    input hashes were verified and preserved; the actual adopted ARO owner was appended
    before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:5683
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:5683
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/hetacillin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:5683
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/hetacillin.yaml --out /private/tmp/am-review-session/529-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:5683
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 529
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-chemistry
  name: Independent exact-structure authority comparison
  status: passed
  required: false
  summary: Ten native and authority encodings reproduce the same neutral graph, formula
    and four assigned stereocentres.
  target_ids:
  - CHEBI:5683
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/529-authority-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-4
  name: Structured source adapter before web research
  status: passed
  required: false
  summary: Actual catalog or esterase search; expression-module results are not conversion
    evidence.
  target_ids:
  - CHEBI:5683
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-5
  name: Structured source adapter before web research
  status: passed
  required: false
  summary: Actual catalog or esterase search; expression-module results are not conversion
    evidence.
  target_ids:
  - CHEBI:5683
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query esterase
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
  - CHEBI:5683
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
  - CHEBI:5683
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
  - CHEBI:5683
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
  - CHEBI:5683
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
  - CHEBI:5683
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
  - CHEBI:5683
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
  - CHEBI:5683
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
  - CHEBI:5683
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
  - CHEBI:5683
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/hetacillin.yaml
  locator: Entire native YAML, including seven synonyms, both parents and roles, structure,
    exact and drug references, two source concepts and four source history events.
  accessed_at: '2026-10-21T18:04:01Z'
  support: supports
  summary: CHEBI:5683 denotes neutral hetacillin, C19H23N3O4S, DXVUYOAEDJXBPY-NFFDBFGFSA-N.
    The record is EXACT and SEEDED. Its definition cites PMID:5907864 and specifically
    attributes conversion to esterases. No molecular target, quantitative activity,
    resistance, producer, clinical assertion, causal graph, dataset or discussion
    is populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv:187; data/raw/aro_antibiotics.tsv:591;
    conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  locator: Complete exact source rows; relevant reviewed-edge, role/class, synonym
    and xref mapping; definition precedence and seeding sections; seven raw source
    lanes and owner search.
  accessed_at: '2026-10-21T18:04:01Z'
  support: supports
  summary: The ChEBI row supplies identity, chemistry, aliases and roles but has no
    definition or literature lead. The ARO row supplies the definition and sole adopted
    PMID:5907864. The seeder therefore selects the ARO definition. DrugBank, DrugCentral
    and KEGG drug entries are deliberately broader drug_xrefs; patent and Wikipedia
    are documents. No applicable exact curator addition or decision was found by the
    hidden/ignored-inclusive search. Original thirteen hashes remain unchanged and
    the actual ARO input was appended.
  snapshot_sha256: e6d5935f55668948b5761a922efb2e3e0814bdf41ed7d54c5a8a24ba24797a0b
- evidence_id: chemistry
  kind: authority
  reference: CHEBI:5683; pubchem.compound:443387; chembl.compound:CHEMBL1201116; kegg.compound:C11729;
    kegg.drug:D01074; cas:3511-16-8
  locator: Complete current structure responses and independent parsing of native,
    ChEBI, PubChem and ChEMBL SMILES/InChI plus both KEGG molfiles.
  accessed_at: '2026-10-21T18:04:01Z'
  support: supports
  summary: All ten encodings reproduce the full neutral key, C19H23N3O4S and four
    stereocentres. The CAS query independently returns CID443387 with that graph.
    Native average and monoisotopic masses pass the focused diagnostic. The seven
    aliases describe the retained graph; INN translations and systematic names preserve
    stereochemistry.
  snapshot_sha256: a1d20d8b5b0e2cad2bc5ca8610eec3a72e15f2f4e027ffb0e1261903042ad0b1
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/5683/; CHEBI:17334;
    CHEBI:33281; CHEBI:36047
  locator: Complete current exact term and the official parent/role definitions.
  accessed_at: '2026-10-21T17:58:30Z'
  support: supports
  summary: The current term supports hetacillin identity, aliases, penicillin parent
    and antibacterial/prodrug roles. The penicillin class is compatible with the cyclic
    acylamino substituent. Beilstein5405483 is corroborated as a registry association
    on ChEBI, not by direct inspection of the registry. Later current citation leads
    are not silently treated as adopted record evidence.
  snapshot_sha256: 80e7f7769a64ce9b173189765af6e81fecbe97f0efbe4da93a55fa8dfb638d80
- evidence_id: aro
  kind: authority
  reference: https://purl.obolibrary.org/obo/aro.obo; ARO:3009132; ARO:3009123; ARO:3000008
  locator: Exact current term and extended-spectrum penicillin/penicillin class stanzas;
    shared official snapshot fetched 2026-10-21T15:57:42Z, SHA256 d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4.
  accessed_at: '2026-10-21T15:57:42Z'
  support: supports
  summary: Current ARO repeats the esterase attribution and PMID:5907864. Native ARO
    identity and broad penicillin structural classification agree with this source.
    This is source fidelity, not independent validation of the enzymatic attribution.
  snapshot_sha256: df1a333ebf110f6d1b0f6af319aabc3738c36e58bdd0a530f6964b683fd379bb
- evidence_id: drug-associations
  kind: database
  reference: https://drugcentral.org/drugcard/1363; DrugBank:DB00739; KEGG:D01074
  locator: DrugCentral identity, synonyms and product/approval sections; public PubChem
    DrugBank-attributed metabolism field; current KEGG drug record and graph.
  accessed_at: '2026-10-21T18:00:39Z'
  support: supports
  summary: DrugCentral1363 matches name, CAS and formula but also includes potassium-product
    context, appropriately represented as a broader drug association. No current clinical
    status is inferred. Direct DrugBank retrieval was unavailable; its text reproduced
    by PubChem explicitly attributes ampicillin formation to esterases. This corroborates
    a database assertion rather than providing an independent enzyme experiment. KEGG
    drug D01074 has the same graph but its target annotation is not promoted into
    native primary evidence.
  snapshot_sha256: 8f4d80afeeb0125751752800af0caecd69dcf660efc3dbd5d8dcfed7ad34b7dc
- evidence_id: documents
  kind: database
  reference: https://patents.google.com/patent/US3198804A/en; https://en.wikipedia.org/wiki/Hetacillin
  locator: Patent general description and Examples1–10 inspected; Wikipedia used only
    as a document and discovery lead, not primary experimental proof.
  accessed_at: '2026-10-21T17:58:31Z'
  support: context_only
  summary: The patent describes ampicillin/acetone condensation and hydrolysis, free-acid
    isolation and separate salt/ester examples. Example7 concerns a methyl ester and
    Example10 a potassium salt; their material scope is not collapsed into the native
    neutral acid. Patent numerical biological tables were not comprehensively audited
    or transferred. The document links resolve to hetacillin context rather than asserting
    exact molecular equivalence.
  snapshot_sha256: 76df93275da05a75867fda696a72f32ebc123db4ebab173f32506dd9adaa7b72
- evidence_id: adopted
  kind: database
  reference: PMID:5907864; DOI:10.1021/jo01341a060
  locator: Complete indexed bibliographic record and original publisher landing page;
    no indexed abstract and no accessible full text obtained.
  accessed_at: '2026-10-21T17:58:31Z'
  support: context_only
  summary: Hardcastle and colleagues, The preparation and structure of hetacillin,
    J Org Chem31,897–899,1966, is the sole adopted lead. The publisher offers a PDF-only
    article and the attempted public routes did not supply it. The review cannot determine
    which definition clauses that paper supports; lack of access is not treated as
    a confirmed bad citation.
  snapshot_sha256: 9645da77a356f48f0d64d13ae629baf3a6d0a86eddb01c2cd0256b5178781de1
- evidence_id: hydrolysis1967
  kind: primary_source
  reference: PMID:5182358; DOI:10.1136/bmj.2.5555.804; https://pmc.ncbi.nlm.nih.gov/articles/PMC1843140/
  locator: All five original scanned pages804–808 read through OCR, with pages804–806
    independently viewed, including Figure1, reaction experiment, susceptibility methods
    and oral-material specification.
  accessed_at: '2026-10-21T17:58:49Z'
  support: supports
  summary: The paper demonstrates conversion of hetacillin to ampicillin and acetone
    in defined phosphate buffer at pH7 and37 degrees C without an added esterase.
    TLC identifies ampicillin and gas chromatography measures acetone. Its oral volunteer
    comparison explicitly uses hetacillin free acid and ampicillin free acid; intramuscular
    comparisons use potassium hetacillin and sodium ampicillin. Overnight susceptibility
    and serum observations are confounded by conversion and are not direct target-binding
    experiments. The authors question substantial intrinsic activity but do not prove
    universal inactivity.
  snapshot_sha256: 409aab6e462b2c482c7735ce36a1c485ae0704da31d94da1a1352e80a820172f
- evidence_id: rapid1973
  kind: primary_source
  reference: PMID:4597707; DOI:10.1128/AAC.3.1.15; https://pmc.ncbi.nlm.nih.gov/articles/PMC444353/
  locator: All four original scanned pages15–18 independently viewed, including complete
    Methods, Results, Discussion and Figures1–6.
  accessed_at: '2026-10-21T17:58:49Z'
  support: supports
  summary: Rapid optical growth assays of E. coli O14 and S. aureus S1 Oxford strain
    report transient effects attributed to intact hetacillin when beta-lactamase destroys
    released ampicillin. Concentrations are expressed as ampicillin equivalents. The
    tested hetacillin lot is identified, but its bulk counterion is not explicit.
    Buffer hydrolysis at pH6.7 and37 degrees C occurs without added esterase. The
    added bacterial penicillinase is a beta-lactamase used to distinguish activity,
    not evidence for esterase activation. The authors could not directly quantify
    conversion in bacterial cultures because of assay interference. These rapid growth
    effects are not MICs, permanent resistance or direct PBP binding; they caution
    against calling the parent universally inactive.
  snapshot_sha256: e6f5d92c000603a41d44a092fec8983e6a684c5821fbf1535a523f6b776e0e5b
- evidence_id: kinetics1974
  kind: primary_source
  reference: PMID:4468090; DOI:10.1248/cpb.22.2434; https://www.jstage.jst.go.jp/article/cpb1958/22/10/22_10_2434/_pdf
  locator: Complete ten-page original paper read by OCR; Methods page2435 and reaction
    Chart1 page2438 independently viewed.
  accessed_at: '2026-10-21T17:58:49Z'
  support: supports
  summary: The study uses crystalline potassium hetacillin in defined aqueous buffers,
    normally at35 degrees C and controlled ionic strength, without added enzyme. Ampicillin
    and acetone formation are tracked chemically. The kinetic reaction scheme concerns
    hydrolysis of the acetone-derived cyclic adduct, with pH-dependent equilibrium
    and alkaline epimerization. It provides positive evidence for chemical conversion
    but does not exclude an additional enzymatic contribution in vivo. Salt material
    and kinetic experiments are not transferred as exact neutral-acid whole-cell MICs.
  snapshot_sha256: 7f84a5a66f594766747dc9cb08ab121b6e03edb301e489815620ae8b086ab6d7
- evidence_id: abstract-context
  kind: primary_source
  reference: PMID:5514976; DOI:10.1159/000220703; PMID:18591; DOI:10.1002/jps.2600660727
  locator: Complete original publisher abstract for1970 and complete indexed abstract
    for1977; full papers not independently read.
  accessed_at: '2026-10-21T17:58:31Z'
  support: supports
  summary: The1970 abstract describes aqueous conversion to ampicillin and acetone
    and suggests little intrinsic activity; this interpretation remains distinct from
    the rapid1973 experimental report. The1977 abstract concerns pH-dependent hydrolysis
    and epimerization. Neither is used to assign a bacterial protein target or assert
    that in vivo esterase participation is impossible.
  snapshot_sha256: 5cfa1c52d70483a53833502b83836dcbda43b2e2fa8bdbfeb5a8d558dca210e5
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/precise1k; 529-imodulondb-datasets.txt; 529-imodulondb-esterase.txt
  locator: Actual dataset catalog and esterase search run before open-ended web follow-up.
  accessed_at: '2026-10-21T18:04:01Z'
  support: context_only
  summary: The bounded E. coli search returned ten gene hits, including aes, tesA
    and tesB, and no iModulon hits. The native esterase wording names no species or
    exact enzyme. Expression annotation cannot establish prodrug conversion, and no
    absence of an in vivo enzyme mechanism is inferred from this result.
  snapshot_sha256: be754720c15c568c34b2b6877dbebdb4ae57420e78ce82fbe6136e6ebf18002d
- evidence_id: search
  kind: search
  reference: 529-local-hits.txt; 529-owner-hits.txt; 529-literature.json; 529-fetch-results.json;
    529-fetch2-results.json; 529-fetch3-results.json; 529-fetch4-results.json
  locator: Hidden/ignored-inclusive repository identifier/label/slug search and owner
    search by key/CAS; bounded public Europe PMC title/abstract and exact-name primary
    discovery.
  accessed_at: '2026-10-21T17:58:31Z'
  support: context_only
  summary: The title/abstract query reported156 hits and returned the first100, including
    patent and follow-up records. Relevant exact-compound primary papers were selected
    and inspected at the stated depths. This search does not establish that no other
    enzyme experiment exists.
  snapshot_sha256: 5cfa1c52d70483a53833502b83836dcbda43b2e2fa8bdbfeb5a8d558dca210e5
  search_scope: 2026-10-21; repository searches included hidden and ignored files;
    public Europe PMC TITLE_ABS hetacillin query and bounded exact-name web/public-publisher
    discovery, with stated returned-result and full-text limits.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral molecule and aliases
  outcome: supported
  summary: Independent authorities and source chemistry agree on the neutral graph,
    stereochemistry, formula, masses and exact CAS. Broad drug/document associations
    remain distinct from exact xrefs.
  target_ids:
  - CHEBI:5683
  evidence_ids:
  - native
  - chemistry
  - chebi
  - drug-associations
  - documents
- assessment_id: grounding
  area: grounding
  topic: Parents, roles and antibacterial filing
  outcome: supported
  summary: The penicillin scaffold and prodrug role are supported. Original neutral
    free-acid administration and compound-specific antibacterial experiments support
    the broad antibacterial context, while conversion, salt and endpoint boundaries
    prevent stronger material-specific claims.
  target_ids:
  - CHEBI:5683
  evidence_ids:
  - chebi
  - aro
  - hydrolysis1967
  - rapid1973
- assessment_id: mechanism
  area: evidence
  topic: Specific conversion mechanism in the definition
  outcome: unknown
  summary: Positive primary experiments support aqueous hydrolysis to ampicillin and
    acetone. The source databases repeat an unqualified esterase attribution, but
    the inspected primary evidence does not establish that attribution. The native
    wording does not explicitly make esterases necessary or exclusive, so the buffer
    experiments do not establish a contradiction. The adopted1966 paper remains unavailable
    at full-text depth.
  target_ids:
  - CHEBI:5683
  evidence_ids:
  - native
  - aro
  - drug-associations
  - hydrolysis1967
  - rapid1973
  - kinetics1974
  - adopted
- assessment_id: activity
  area: evidence
  topic: Intrinsic versus conversion-mediated activity
  outcome: supported
  summary: The overall antibacterial/prodrug description is defensible. Earlier studies
    questioned intrinsic activity, whereas rapid1973 assays report transient parent-attributed
    effects. Preserve the experimental conflict and time/conversion dependence; neither
    generic inactivity nor a precise direct molecular target is established.
  target_ids:
  - CHEBI:5683
  evidence_ids:
  - hydrolysis1967
  - rapid1973
  - abstract-context
- assessment_id: provenance
  area: provenance
  topic: Actual source owners and history
  outcome: supported
  summary: Fourteen input hashes include the preserved original thirteen and appended
    ARO table. Source precedence explains the imported definition, and the source-concept/history
    shape is consistent with SEEDED status. Validation success is not scientific status
    promotion.
  target_ids:
  - CHEBI:5683
  evidence_ids:
  - owners
  - native
- assessment_id: coverage
  area: completeness
  topic: Optional fields and possible enrichment
  outcome: supported
  summary: No required representation was found missing. Optional quantitative activity,
    target, clinical, resistance, producer, graph or transcriptomic fields should
    not be filled by transferring ampicillin, salt, beta-lactamase or generic database
    annotations.
  target_ids:
  - CHEBI:5683
  evidence_ids:
  - native
  - owners
  - rapid1973
  - kinetics1974
  - adapter
  - search
findings: []
actions:
- action_id: A1
  description: Optionally strengthen the definition evidence by distinguishing demonstrated
    aqueous hydrolysis from an unresolved additional esterase contribution.
  finding_ids: []
  target_ids:
  - CHEBI:5683
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition text
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ARO definition extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Definition precedence and generated field emission
  acceptance_checks:
  - If revising the definition, retain demonstrated hydrolysis to ampicillin and acetone
    and qualify the esterase contribution according to exact primary evidence. Buffer
    conversion alone is not proof that in vivo enzymatic conversion is false.
  - Retain antibacterial/prodrug scope and do not replace it with universal parent
    inactivity. Preserve the rapid1973 assay result and its temporal, material and
    ampicillin-equivalent limits.
  - Do not describe the unavailable1966 source as disproved. Regenerate the exact
    record through the maintained owner and pass focused schema/strict plus corpus
    reproduction checks.
- action_id: A2
  description: If enriching optional scientific fields, preserve exact material and
    endpoint scope.
  finding_ids: []
  target_ids:
  - CHEBI:5683
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/hetacillin.yaml
    role: Optional curator-owned scientific additions through the validated writer
  acceptance_checks:
  - Distinguish oral free-acid material, intramuscular potassium salt, kinetic potassium
    salt and the unspecified bulk form of the rapid-assay lot.
  - Do not encode transient optical growth effects as MICs or transfer ampicillin
    PBP annotations into direct hetacillin binding evidence.
  - Retain the adopted1966 full-text access limit until the actual paper is inspected;
    broader drug products do not establish a universal current clinical status.
limitations:
- The sole adopted1966 publication has no indexed abstract and the attempted public
  publisher routes did not provide full text. Its precise support for individual definition
  clauses remains unresolved.
- The1967 paper was read completely through OCR with selected original pages804–806
  visually checked; every numerical table cell was not independently transcribed.
  The1973 paper was visually read in full. The1974 paper was read completely through
  OCR with Methods and reaction-scheme images checked; raw experimental traces were
  not reanalysed.
- The1970 and1977 papers were read at complete abstract depth only. Direct DrugBank
  retrieval was unavailable, although its specific metabolism assertion was inspected
  through PubChem attribution. Beilstein was corroborated through ChEBI rather than
  directly.
- The reviewed buffer experiments establish chemical hydrolysis but do not exclude
  additional enzyme participation in vivo. The original literature differs in its
  interpretation of intrinsic activity, and exact bulk material is not equally specified
  across experiments.
- No exact bacterial protein-binding or clinical-resistance claim is introduced. The
  structured adapter is a bounded expression-context check and its lack of module
  hits is not negative biochemical evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Fetch manifests preserve actual URLs, UTC retrieval times, response failures and
  SHA256 values. Input hashes were rechecked before draft output.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
