# Review of cephradine

- Review: 20261021T123257Z-cephradine-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:20:01Z
- Finished UTC: 2026-10-21T12:32:57Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native cephradine structure, three R stereocenters, formula and inspected chemical authorities agree. Two minor findings concern one malformed systematic synonym and the exact-synonym typing of the verified Anspor and Sefril brands. The PBP-family assertion remains honestly database-qualified; an original membrane experiment supports PBP1a-dependent peptidoglycan inhibition without establishing an equilibrium binding constant. All 11 adopted PMID leads were resolved and dispositioned. Hydrate/product and allergen-evidence boundaries are retained.

## Scope And Provenance

Entire exact SEEDED cephradine record: definition, 16 synonyms, three parents, two roles, six chemical references, three drug links, Wikipedia document, one PBP target, source concepts and five history events.

Selection: Queue 273; 13 original inputs plus three actual ARO owner inputs, all 16 hashes preserved.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3547 | data/antibiotics/antibacterial/cephradine.yaml | generated | cephradine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema validation | passed | True | CHEBI:3547 | Exit 0; no issues found. |
| Documented strict validation | passed | True | CHEBI:3547 | Exit 0; zero ERROR rows. |
| Supplemental chemical identity comparison | passed | False | CHEBI:3547 | Exit 0; all six representations agree. |
| Initial structured adapter attempt | failed | False | CHEBI:3547 | Exit 2: sandbox DNS resolution failed. A permitted public-network retry subsequently succeeded. |
| Structured adapter public-network retry | passed | False | CHEBI:3547 | Exit 0 after network escalation. Dataset discovery and ftsI search preceded protein web research. |
| Initial structured adapter attempt | failed | False | CHEBI:3547 | Exit 2: sandbox DNS resolution failed. A permitted public-network retry subsequently succeeded. |
| Structured adapter public-network retry | passed | False | CHEBI:3547 | Exit 0 after network escalation. Dataset discovery and ftsI search preceded protein web research. |
| Supplemental source and preserved-input reconciliation | passed | False | CHEBI:3547 | Exit 0; 16 input hashes, one target source row and 11 lead dispositions checked. |
| Authoritative full QC | failed | True | CHEBI:3547 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3547 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3547 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3547 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3547 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3547 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3547 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3547 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3547 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact molecule and stereochemistry

identity: supported. Targets: CHEBI:3547.

Independent structures agree on the neutral molecule and all three R centers.

### Systematic name and brand types

identity: concern. Targets: CHEBI:3547.

One systematic synonym is malformed; Anspor and Sefril need brand-name typing.

### Antibacterial classification and structural parent

grounding: supported. Targets: CHEBI:3547.

Structure and primary activity support the cephalosporin and antibacterial claims.

### Allergen parent evidence depth

grounding: unknown. Targets: CHEBI:3547.

Authority classification is present, but exact-cephradine original IgE tables were not inspected.

### PBP-family assertion and primary enrichment

evidence: supported. Targets: CHEBI:3547.

Native source qualification is honest; a scoped primary PBP1a pathway experiment is available without conflating it with binding affinity.

### Source concepts, references and history

provenance: supported. Targets: CHEBI:3547.

Five history events and maintained owners are coherent; inaccessible registries remain explicitly qualified.

### Optional enrichment

completeness: supported. Targets: CHEBI:3547.

Optional assay or target enrichment can be added with material and taxon scope; empty optional fields are not defects.

### Focused validators

schema: supported. Targets: CHEBI:3547.

Schema, strict and supplemental chemistry checks pass.

## Findings

### F1: One systematic synonym incorrectly says phenylacetamido

minor / open / confirmed; issue key: CHEBI-3547-phenylacetamido-systematic-name.

synonyms[4] introduces a phenylacetamido fragment while omitting the actual amino group. The valid graph, definition and other systematic names consistently identify the amino-cyclohexadienyl side chain. This isolated source-name defect should not be propagated as exact nomenclature.

### F2: Verified product names are typed as exact chemical synonyms

minor / open / confirmed; issue key: CHEBI-3547-anspor-sefril-brand-types.

Anspor and Sefril are verified cephradine brands but native synonyms[8] and [14] carry EXACT_SYNONYM. Preserve the aliases as BRAND_NAME, consistent with the existing Velosef entry.

## Recommended Actions And Acceptance Checks

### A1

Exclude the exact malformed synonyms[4] string using conf/sources.yaml synonym_exclusions under CHEBI:3547, retaining the already correct systematic names. Alternatively adopt a source-reviewed corrected name. Do not change the valid molecular graph to fit the erroneous phenyl wording.

- The malformed phenylacetamido name is absent or replaced by a verified amino-side-chain name.
- The exact molecular key, formula, stereochemistry and valid nomenclature are unchanged.
- Run documented schema, strict and full-corpus gates after separately authorized curation.

### A2

Reclassify Anspor and Sefril through a maintained source-specific synonym-type correction or corrected upstream adoption, then regenerate as BRAND_NAME. Retain Velosef as already typed. Verify Eskacef independently at product-source depth before extending this finding.

- Anspor and Sefril remain discoverable as BRAND_NAME without duplicate EXACT_SYNONYM entries.
- Neutral molecular identity and genuine systematic/INN synonyms are preserved.
- Run documented schema, strict, seed-canary and full-corpus gates after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cephradine.yaml; Entire native YAML, source concepts and five history events | supports | The native record denotes one neutral cephradine structure. Its sole target is an explicitly qualified CARD PBP-family assertion with PRIMARY_EVIDENCE_NEEDED. There are no native MIC, resistance, producer, clinical-product or causal-graph assertions; those optional absences are not findings. |
| chemistry | CHEBI:3547; PubChem:38103; ChEMBL:CHEMBL1604; KEGG:D00264; 273-chemistry.py/.json; native SMILES/InChI and current ChEBI mol, PubChem, ChEMBL and KEGG structures | supports | All six representations reproduce RDLPVSKMFDYCOR-UEKVPHQBSA-N, C16H19N3O4S, net charge 0, three R stereocenters and native mass precision. The cyclohexa-1,4-dienyl ring is not phenyl. The valid molecular graph and definition support the amino side chain, unlike the malformed synonym. |
| name | CHEBI:3547; PubChem:38103; Native synonyms[4], definition and synonyms[5–6]; 273-ols.json and PubChem IUPACName | refutes | One source-derived exact synonym contains 2-phenylacetamido while also specifying the cyclohexadienyl substituent and omitting the actual amino group. Native and independent authority structures contain the amino-bearing alpha carbon and no phenyl ring. Current ChEBI repeats the wording, so a refresh alone cannot correct it. Other native systematic names already describe the intended exact structure. |
| grounding | CHEBI:23066; CHEBI:88225; CHEBI:33281; CHEBI:36047; ARO:0000032; 273-parent88225.json; 273-ols.json and 273-aro-stanzas.txt; previously inspected shared class/role authorities | partial | The cephalosporin parent fits the structure and original activity supports antibacterial classification. CHEBI:88225 resolves to beta-lactam antibiotic allergen. Adopted IgE papers give allergen/cross-reactivity context, but their abstracts do not independently verify every exact cephradine-specific result; retain this as a source-attributed parent rather than promoting a universal allergy claim. |
| links | CAS:38821-53-3; HMDB:HMDB0015428; Reaxys:4211105; DrugBank:DB01333; DrugCentral:576; KEGG:D00264; wikipedia.en:Cephradine; 273-fetch-results.json, 273-drugcentral.html/.txt, 273-kegg.txt and 273-wiki.html/.txt | partial | DrugCentral 576 resolves to cephradine, native CAS and formula. KEGG D00264 has the matching exact structure and identifies cephradine/cefradine names. Wikipedia Cephradine redirects to Cefradine and retains the native identity identifiers. Direct DrugBank and HMDB requests returned 403; their native identifiers and Reaxys were corroborated through current ChEBI without independent registry inspection. Wikipedia supplies contextual identity, not primary mechanism proof. |
| brands | FDA:ANDA061859; FDA:ANDA061866; https://www.acmeglobal.com/products/pharmaceuticals/brand/sefril/; 273-anspor.json products; 273-sefril.html Composition; native synonyms[8] and synonyms[14] | refutes | FDA explicitly labels ANSPOR as a brand for cephradine capsules and oral suspension. The manufacturer identifies SEFRIL as its cephradine product range and lists capsule, suspension, drops and injection compositions. These are legitimate product names but are imported as EXACT_SYNONYM, unlike the already correctly typed Velosef BRAND_NAME. The finding concerns metadata type, not rejection of the names or proof of a different active ingredient. |
| materials | FDA GSRS:F1BC02I72W; 273-gsrs.json current substance definition | context_only | The additional FDA substance entry for broadly named cephradine is a mixture-class material definition whose alternative components may be anhydrous, monohydrate or dihydrate forms. This external product/substance umbrella is not a native exact-structure link and was not added as one. It reinforces the need to preserve exact hydrate boundaries when importing future product or assay data. |
| adapter | iModulonDB:e_coli/precise1k/b0084; 273-imodulondb-datasets.txt and 273-imodulondb-ftsI.txt; actual initial errors and public-network retries | context_only | The successful ftsI search returned gene b0084 and zero iModulon components. No component summary was applicable. This gene catalog result is computational context and does not prove cephradine target binding or any assay phenotype. |
| pbp | PMID:16569861; DOI:10.1128/AAC.50.4.1425-1432.2006; 273-pbp.html/.txt: complete main methods, relevant transformant Results and full Table 2 | supports | E. coli AMA1004 membrane assays compare a ponB-deficient background with plasmid-encoded PBP1a or PBP1b. Cephradine inhibits PBP1a-dependent cross-linked peptidoglycan synthesis with IC50 7.2 ±1.2 micromolar; Table 2 gives approximately 590 for wild-type membranes and &gt;1000 for PBP1b-complemented and deficient membranes. The assay uses radiolabeled sugar precursors, 90 minutes at 37 degrees C and product capture. This supports scoped PBP1a-dependent pathway inhibition, not an equilibrium affinity, direct ligand-bound structure or whole-cell MIC. The Results prose says no effect on wild-type membranes, whereas its table supplies an approximate high-concentration value; retain the quantitative table and concentration scope. |
| activity | PMID:4790592; DOI:10.1128/AAC.3.2.270; PMID:24035952; 273-activity-core.json complete original abstract; 273-core.json complete 2013 abstract | supports | The 1973 original explicitly names cephradine hydrate and reports activity in infected mice after subcutaneous dosing; this supports antibacterial activity in a defined material/model context, not exact anhydrous solid identity or clinical efficacy. The 2013 original tests 24 capsule brands against four bacterial strains using disk diffusion. Its inhibition zones are not MICs, and formulation-quality comparisons cannot be generalized to all cephradine materials. Neither source was read at full-table depth. |
| leads | All 11 adopted ChEBI/ARO compound, class and PBP PMID leads; 273-core.json and 273-lead-dispositions.json | partial | All 11 records resolved; eight complete abstracts were read. PMID4572639, PMID15673804 and PMID6810737 supplied metadata without abstracts. The adopted 1973 preclinical/pharmacology summary therefore did not establish a directly inspected PBP assay. Analytical degradation-product detection, algae toxicity, human IgE cross-reactivity and class reviews were kept within their own scope. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv; conf/aro_target_roles.tsv; scripts/seed_from_sources.py; 273-source-audit.json and exact source row extracts; seeder synonym_exclusions lines 1533–1544 | supports | The malformed systematic name and the verified brand aliases come from ChEBI. Existing source-specific synonym_exclusions can omit the erroneous name under CHEBI:3547. Reclassification of brands needs a maintained source-specific kind correction or corrected upstream adoption; exclusion alone does not retype a name. One target row matches its ARO inventory. All 16 hashes remain unchanged. |
| validation | Focused documented checks and supplemental diagnostics; 273-strict.tsv; 273-chemistry.json; 273-source-audit.json | supports | Schema, strict, supplemental chemistry and source reconciliation pass. Initial structured adapter DNS failures were retried successfully and are retained as attempts. These checks do not replace shared full-corpus QC, term, reference or history gates. |

## Limits And Additional Notes

- Exact cephradine allergen results in the adopted 1990/1996 full bodies were not verified; their complete abstracts establish broader IgE cross-reactivity context. No universal allergy or cross-reactivity prediction is made.
- Three adopted records lack abstracts. The original 1973 activity and 2013 brand-panel papers were read at complete-abstract depth; no MIC values or clinical outcomes were newly adopted.
- Direct HMDB and DrugBank requests returned 403, and Reaxys was only corroborated through current ChEBI. Eskacef has historical secondary corroboration but was not included in the confirmed official-product typing finding.
- The first ChEBI molfile request returned compound JSON rather than a molfile. The separate real molfile was retrieved and used in the successful chemistry comparison. The EPMC primary XML endpoint returned 500; the actual PMC full HTML supplied the inspected original methods and Table 2.
- The PBP assay is membrane-based pathway inhibition; it does not by itself establish purified-protein binding affinity or an exact holo structure. Radioiodinated cephradine-derivative search leads were not substituted for unmodified cephradine.
- FDA substance/product nomenclature may encompass several hydration states. No broad GSRS material identifier or formulation claim was added to the exact native structure.
- Initial structured adapter attempts failed DNS in the sandbox; public-network retries succeeded. Focused results do not substitute for documented full-corpus gates.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record or maintained input was changed; all 16 captured hashes remain unchanged.
- Ignored-inclusive searches covered curation, conf, raw source tables, scripts and documentation for the target identifiers, labels and slug. Optional missing data were not treated as proven defects.
- Optional links and tags in this review refer only to cephradine; no links to other review targets are included.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T123257Z-cephradine-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of cephradine
started_at: '2026-10-21T12:20:01Z'
finished_at: '2026-10-21T12:32:57Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Independent read-only review of the complete generated record;
    original hashes preserved and three actual ARO owners appended before detailed
    judgment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Needs minor nomenclature and brand-type curation
scientific_review: true
summary: The native cephradine structure, three R stereocenters, formula and inspected
  chemical authorities agree. Two minor findings concern one malformed systematic
  synonym and the exact-synonym typing of the verified Anspor and Sefril brands. The
  PBP-family assertion remains honestly database-qualified; an original membrane experiment
  supports PBP1a-dependent peptidoglycan inhibition without establishing an equilibrium
  binding constant. All 11 adopted PMID leads were resolved and dispositioned. Hydrate/product
  and allergen-evidence boundaries are retained.
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
  - path: data/antibiotics/antibacterial/cephradine.yaml
    sha256: 1d3ac80ac6ef4d80ec090bb2266ded16eba7baf93a10dba2e543e739d1a378c1
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
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
scope:
  description: 'Entire exact SEEDED cephradine record: definition, 16 synonyms, three
    parents, two roles, six chemical references, three drug links, Wikipedia document,
    one PBP target, source concepts and five history events.'
  selection: Queue 273; 13 original inputs plus three actual ARO owner inputs, all
    16 hashes preserved.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3547
targets:
- target_id: CHEBI:3547
  path: data/antibiotics/antibacterial/cephradine.yaml
  label: cephradine
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
    role: Adopted ARO identity and synonym source
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted PBP target source row
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Maintained target semantic mapping
checks:
- check_id: schema
  name: Documented schema validation
  status: passed
  required: true
  summary: Exit 0; no issues found.
  target_ids:
  - CHEBI:3547
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cephradine.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict validation
  status: passed
  required: true
  summary: Exit 0; zero ERROR rows.
  target_ids:
  - CHEBI:3547
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cephradine.yaml --out /private/tmp/am-review-session/273-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Supplemental chemical identity comparison
  status: passed
  required: false
  summary: Exit 0; all six representations agree.
  target_ids:
  - CHEBI:3547
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/273-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: adapter-datasets-initial
  name: Initial structured adapter attempt
  status: failed
  required: false
  summary: 'Exit 2: sandbox DNS resolution failed. A permitted public-network retry
    subsequently succeeded.'
  target_ids:
  - CHEBI:3547
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets > /private/tmp/am-review-session/273-imodulondb-datasets.txt
  exit_code: 2
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-datasets
  name: Structured adapter public-network retry
  status: passed
  required: false
  summary: Exit 0 after network escalation. Dataset discovery and ftsI search preceded
    protein web research.
  target_ids:
  - CHEBI:3547
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets > /private/tmp/am-review-session/273-imodulondb-datasets.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-ftsI-initial
  name: Initial structured adapter attempt
  status: failed
  required: false
  summary: 'Exit 2: sandbox DNS resolution failed. A permitted public-network retry
    subsequently succeeded.'
  target_ids:
  - CHEBI:3547
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query ftsI
    > /private/tmp/am-review-session/273-imodulondb-ftsI.txt
  exit_code: 2
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-ftsI
  name: Structured adapter public-network retry
  status: passed
  required: false
  summary: Exit 0 after network escalation. Dataset discovery and ftsI search preceded
    protein web research.
  target_ids:
  - CHEBI:3547
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query ftsI
    > /private/tmp/am-review-session/273-imodulondb-ftsI.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: source-reconciliation
  name: Supplemental source and preserved-input reconciliation
  status: passed
  required: false
  summary: Exit 0; 16 input hashes, one target source row and 11 lead dispositions
    checked.
  target_ids:
  - CHEBI:3547
  command: .venv/bin/python /private/tmp/am-review-session/273-ledger.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - owners
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:3547
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
  - CHEBI:3547
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
  - CHEBI:3547
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
  - CHEBI:3547
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
  - CHEBI:3547
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
  - CHEBI:3547
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
  - CHEBI:3547
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
  - CHEBI:3547
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
  - CHEBI:3547
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cephradine.yaml
  locator: Entire native YAML, source concepts and five history events
  accessed_at: '2026-10-21T12:30:32Z'
  support: supports
  summary: The native record denotes one neutral cephradine structure. Its sole target
    is an explicitly qualified CARD PBP-family assertion with PRIMARY_EVIDENCE_NEEDED.
    There are no native MIC, resistance, producer, clinical-product or causal-graph
    assertions; those optional absences are not findings.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:3547; PubChem:38103; ChEMBL:CHEMBL1604; KEGG:D00264
  locator: 273-chemistry.py/.json; native SMILES/InChI and current ChEBI mol, PubChem,
    ChEMBL and KEGG structures
  accessed_at: '2026-10-21T12:30:32Z'
  support: supports
  summary: All six representations reproduce RDLPVSKMFDYCOR-UEKVPHQBSA-N, C16H19N3O4S,
    net charge 0, three R stereocenters and native mass precision. The cyclohexa-1,4-dienyl
    ring is not phenyl. The valid molecular graph and definition support the amino
    side chain, unlike the malformed synonym.
  snapshot_sha256: ba1c5864126561c1e2b674c2c07eb9f310ee6961bca2ce706a9800be378fea18
- evidence_id: name
  kind: authority
  reference: CHEBI:3547; PubChem:38103
  locator: Native synonyms[4], definition and synonyms[5–6]; 273-ols.json and PubChem
    IUPACName
  accessed_at: '2026-10-21T12:30:32Z'
  support: refutes
  summary: One source-derived exact synonym contains 2-phenylacetamido while also
    specifying the cyclohexadienyl substituent and omitting the actual amino group.
    Native and independent authority structures contain the amino-bearing alpha carbon
    and no phenyl ring. Current ChEBI repeats the wording, so a refresh alone cannot
    correct it. Other native systematic names already describe the intended exact
    structure.
  snapshot_sha256: 7ce9ea57748d2181741e1562b428e351da67b6617ae298e83a46e568d74a20cb
- evidence_id: grounding
  kind: authority
  reference: CHEBI:23066; CHEBI:88225; CHEBI:33281; CHEBI:36047; ARO:0000032
  locator: 273-parent88225.json; 273-ols.json and 273-aro-stanzas.txt; previously
    inspected shared class/role authorities
  accessed_at: '2026-10-21T12:30:32Z'
  support: partial
  summary: The cephalosporin parent fits the structure and original activity supports
    antibacterial classification. CHEBI:88225 resolves to beta-lactam antibiotic allergen.
    Adopted IgE papers give allergen/cross-reactivity context, but their abstracts
    do not independently verify every exact cephradine-specific result; retain this
    as a source-attributed parent rather than promoting a universal allergy claim.
  snapshot_sha256: 221cbe3d89a16c4d48a78cbe1150514e4d13bcdcbf66db2cd3243b7c0ff03bbe
- evidence_id: links
  kind: authority
  reference: CAS:38821-53-3; HMDB:HMDB0015428; Reaxys:4211105; DrugBank:DB01333; DrugCentral:576;
    KEGG:D00264; wikipedia.en:Cephradine
  locator: 273-fetch-results.json, 273-drugcentral.html/.txt, 273-kegg.txt and 273-wiki.html/.txt
  accessed_at: '2026-10-21T12:30:32Z'
  support: partial
  summary: DrugCentral 576 resolves to cephradine, native CAS and formula. KEGG D00264
    has the matching exact structure and identifies cephradine/cefradine names. Wikipedia
    Cephradine redirects to Cefradine and retains the native identity identifiers.
    Direct DrugBank and HMDB requests returned 403; their native identifiers and Reaxys
    were corroborated through current ChEBI without independent registry inspection.
    Wikipedia supplies contextual identity, not primary mechanism proof.
  snapshot_sha256: 78bf785221663745b4a436fe27195209e1227f6a5477abf5e6cdb525017a5c73
- evidence_id: brands
  kind: authority
  reference: FDA:ANDA061859; FDA:ANDA061866; https://www.acmeglobal.com/products/pharmaceuticals/brand/sefril/
  locator: 273-anspor.json products; 273-sefril.html Composition; native synonyms[8]
    and synonyms[14]
  accessed_at: '2026-10-21T12:30:32Z'
  support: refutes
  summary: FDA explicitly labels ANSPOR as a brand for cephradine capsules and oral
    suspension. The manufacturer identifies SEFRIL as its cephradine product range
    and lists capsule, suspension, drops and injection compositions. These are legitimate
    product names but are imported as EXACT_SYNONYM, unlike the already correctly
    typed Velosef BRAND_NAME. The finding concerns metadata type, not rejection of
    the names or proof of a different active ingredient.
  snapshot_sha256: 988ace35e740f1871f488b1b0e8988e9901ba0dff9354b0f6025d7b34f33d6df
- evidence_id: materials
  kind: authority
  reference: FDA GSRS:F1BC02I72W
  locator: 273-gsrs.json current substance definition
  accessed_at: '2026-10-21T12:30:32Z'
  support: context_only
  summary: The additional FDA substance entry for broadly named cephradine is a mixture-class
    material definition whose alternative components may be anhydrous, monohydrate
    or dihydrate forms. This external product/substance umbrella is not a native exact-structure
    link and was not added as one. It reinforces the need to preserve exact hydrate
    boundaries when importing future product or assay data.
  snapshot_sha256: b775ef3f7e98a84e3d71c1623c27528e70e94a731ce03ed4a637ad0736fbd4d4
- evidence_id: adapter
  kind: search
  reference: iModulonDB:e_coli/precise1k/b0084
  locator: 273-imodulondb-datasets.txt and 273-imodulondb-ftsI.txt; actual initial
    errors and public-network retries
  accessed_at: '2026-10-21T12:30:32Z'
  support: context_only
  summary: The successful ftsI search returned gene b0084 and zero iModulon components.
    No component summary was applicable. This gene catalog result is computational
    context and does not prove cephradine target binding or any assay phenotype.
  snapshot_sha256: e11ac9a1aaa77de1249f64718913ddabd60cc6a93375452fd9989485516b45b4
  search_scope: 273-imodulondb-datasets.txt and 273-imodulondb-ftsI.txt; actual initial
    errors and public-network retries
- evidence_id: pbp
  kind: primary_source
  reference: PMID:16569861; DOI:10.1128/AAC.50.4.1425-1432.2006
  locator: '273-pbp.html/.txt: complete main methods, relevant transformant Results
    and full Table 2'
  accessed_at: '2026-10-21T12:30:32Z'
  support: supports
  summary: E. coli AMA1004 membrane assays compare a ponB-deficient background with
    plasmid-encoded PBP1a or PBP1b. Cephradine inhibits PBP1a-dependent cross-linked
    peptidoglycan synthesis with IC50 7.2 ±1.2 micromolar; Table 2 gives approximately
    590 for wild-type membranes and >1000 for PBP1b-complemented and deficient membranes.
    The assay uses radiolabeled sugar precursors, 90 minutes at 37 degrees C and product
    capture. This supports scoped PBP1a-dependent pathway inhibition, not an equilibrium
    affinity, direct ligand-bound structure or whole-cell MIC. The Results prose says
    no effect on wild-type membranes, whereas its table supplies an approximate high-concentration
    value; retain the quantitative table and concentration scope.
  snapshot_sha256: 2295e102813ac6b1265fee34fa0c546934483a7c3d4244622434d489d1d0c38d
- evidence_id: activity
  kind: primary_source
  reference: PMID:4790592; DOI:10.1128/AAC.3.2.270; PMID:24035952
  locator: 273-activity-core.json complete original abstract; 273-core.json complete
    2013 abstract
  accessed_at: '2026-10-21T12:30:32Z'
  support: supports
  summary: The 1973 original explicitly names cephradine hydrate and reports activity
    in infected mice after subcutaneous dosing; this supports antibacterial activity
    in a defined material/model context, not exact anhydrous solid identity or clinical
    efficacy. The 2013 original tests 24 capsule brands against four bacterial strains
    using disk diffusion. Its inhibition zones are not MICs, and formulation-quality
    comparisons cannot be generalized to all cephradine materials. Neither source
    was read at full-table depth.
  snapshot_sha256: 5b9f59114f224a9fc66c62fc01dabe39cdabe90cfd548fcfeb46fc4a5ce423a9
- evidence_id: leads
  kind: database
  reference: All 11 adopted ChEBI/ARO compound, class and PBP PMID leads
  locator: 273-core.json and 273-lead-dispositions.json
  accessed_at: '2026-10-21T12:30:32Z'
  support: partial
  summary: All 11 records resolved; eight complete abstracts were read. PMID4572639,
    PMID15673804 and PMID6810737 supplied metadata without abstracts. The adopted
    1973 preclinical/pharmacology summary therefore did not establish a directly inspected
    PBP assay. Analytical degradation-product detection, algae toxicity, human IgE
    cross-reactivity and class reviews were kept within their own scope.
  snapshot_sha256: 2276d3cb83ad96723a18d0ecd669f482f218226d0bee8ed5d43232502a4c9ac9
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv;
    conf/aro_target_roles.tsv; scripts/seed_from_sources.py
  locator: 273-source-audit.json and exact source row extracts; seeder synonym_exclusions
    lines 1533–1544
  accessed_at: '2026-10-21T12:30:32Z'
  support: supports
  summary: The malformed systematic name and the verified brand aliases come from
    ChEBI. Existing source-specific synonym_exclusions can omit the erroneous name
    under CHEBI:3547. Reclassification of brands needs a maintained source-specific
    kind correction or corrected upstream adoption; exclusion alone does not retype
    a name. One target row matches its ARO inventory. All 16 hashes remain unchanged.
  snapshot_sha256: 52582d0173945c8bb8bca0fbffc3ede07075ad1c59f0a8bfdbce29547829908e
- evidence_id: validation
  kind: validation
  reference: Focused documented checks and supplemental diagnostics
  locator: 273-strict.tsv; 273-chemistry.json; 273-source-audit.json
  accessed_at: '2026-10-21T12:30:32Z'
  support: supports
  summary: Schema, strict, supplemental chemistry and source reconciliation pass.
    Initial structured adapter DNS failures were retried successfully and are retained
    as attempts. These checks do not replace shared full-corpus QC, term, reference
    or history gates.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact molecule and stereochemistry
  outcome: supported
  summary: Independent structures agree on the neutral molecule and all three R centers.
  target_ids:
  - CHEBI:3547
  evidence_ids:
  - chemistry
- assessment_id: synonyms
  area: identity
  topic: Systematic name and brand types
  outcome: concern
  summary: One systematic synonym is malformed; Anspor and Sefril need brand-name
    typing.
  target_ids:
  - CHEBI:3547
  evidence_ids:
  - name
  - brands
  - owners
- assessment_id: activity
  area: grounding
  topic: Antibacterial classification and structural parent
  outcome: supported
  summary: Structure and primary activity support the cephalosporin and antibacterial
    claims.
  target_ids:
  - CHEBI:3547
  evidence_ids:
  - chemistry
  - activity
  - grounding
- assessment_id: allergen
  area: grounding
  topic: Allergen parent evidence depth
  outcome: unknown
  summary: Authority classification is present, but exact-cephradine original IgE
    tables were not inspected.
  target_ids:
  - CHEBI:3547
  evidence_ids:
  - grounding
  - leads
- assessment_id: mechanism
  area: evidence
  topic: PBP-family assertion and primary enrichment
  outcome: supported
  summary: Native source qualification is honest; a scoped primary PBP1a pathway experiment
    is available without conflating it with binding affinity.
  target_ids:
  - CHEBI:3547
  evidence_ids:
  - record
  - pbp
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Source concepts, references and history
  outcome: supported
  summary: Five history events and maintained owners are coherent; inaccessible registries
    remain explicitly qualified.
  target_ids:
  - CHEBI:3547
  evidence_ids:
  - record
  - links
  - owners
- assessment_id: completeness
  area: completeness
  topic: Optional enrichment
  outcome: supported
  summary: Optional assay or target enrichment can be added with material and taxon
    scope; empty optional fields are not defects.
  target_ids:
  - CHEBI:3547
  evidence_ids:
  - record
  - materials
  - activity
  - pbp
- assessment_id: schema
  area: schema
  topic: Focused validators
  outcome: supported
  summary: Schema, strict and supplemental chemistry checks pass.
  target_ids:
  - CHEBI:3547
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: CHEBI-3547-phenylacetamido-systematic-name
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: One systematic synonym incorrectly says phenylacetamido
  description: synonyms[4] introduces a phenylacetamido fragment while omitting the
    actual amino group. The valid graph, definition and other systematic names consistently
    identify the amino-cyclohexadienyl side chain. This isolated source-name defect
    should not be propagated as exact nomenclature.
  target_ids:
  - CHEBI:3547
  field_paths:
  - synonyms[4].synonym_text
  evidence_ids:
  - name
  - chemistry
  - owners
  rule_id: '.claude/skills/curate-yaml-record/references/review-checklist.md: Exact
    identity and synonym correctness'
  native_severity: 'Minor: isolated malformed systematic synonym with otherwise coherent
    molecular identity'
  normalization_reason: The graph, identifier, definition and other systematic names
    agree; the defect is bounded to one imported wording.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted synonym source
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-scoped synonym exclusions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source name/kind extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generates synonyms and preserves their source types
- finding_id: F2
  issue_key: CHEBI-3547-anspor-sefril-brand-types
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Verified product names are typed as exact chemical synonyms
  description: Anspor and Sefril are verified cephradine brands but native synonyms[8]
    and [14] carry EXACT_SYNONYM. Preserve the aliases as BRAND_NAME, consistent with
    the existing Velosef entry.
  target_ids:
  - CHEBI:3547
  field_paths:
  - synonyms[8].synonym_type
  - synonyms[14].synonym_type
  evidence_ids:
  - brands
  - owners
  rule_id: '.claude/skills/curate-yaml-record/references/review-checklist.md: Synonym
    type and material scope'
  native_severity: 'Minor: non-blocking product metadata typing'
  normalization_reason: The brands identify cephradine products; this does not imply
    the active molecule itself is incorrect.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted synonym source
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-scoped synonym exclusions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source name/kind extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generates synonyms and preserves their source types
actions:
- action_id: A1
  description: Exclude the exact malformed synonyms[4] string using conf/sources.yaml
    synonym_exclusions under CHEBI:3547, retaining the already correct systematic
    names. Alternatively adopt a source-reviewed corrected name. Do not change the
    valid molecular graph to fit the erroneous phenyl wording.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:3547
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted synonym source
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-scoped synonym exclusions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source name/kind extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generates synonyms and preserves their source types
  ownership_note: The existing source-scoped exclusion works for CHEBI source IDs.
    Current upstream ChEBI repeats the defect, so a blind refresh is insufficient.
  generator: just seed; just seed-canary CHEBI:3547
  acceptance_checks:
  - The malformed phenylacetamido name is absent or replaced by a verified amino-side-chain
    name.
  - The exact molecular key, formula, stereochemistry and valid nomenclature are unchanged.
  - Run documented schema, strict and full-corpus gates after separately authorized
    curation.
- action_id: A2
  description: Reclassify Anspor and Sefril through a maintained source-specific synonym-type
    correction or corrected upstream adoption, then regenerate as BRAND_NAME. Retain
    Velosef as already typed. Verify Eskacef independently at product-source depth
    before extending this finding.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:3547
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted synonym source
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-scoped synonym exclusions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source name/kind extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generates synonyms and preserves their source types
  ownership_note: Existing exclusions can omit a wrongly typed duplicate but cannot
    themselves create a BRAND_NAME; the maintained source kind must be corrected.
  generator: just extract-inventory; just seed; just seed-canary CHEBI:3547
  acceptance_checks:
  - Anspor and Sefril remain discoverable as BRAND_NAME without duplicate EXACT_SYNONYM
    entries.
  - Neutral molecular identity and genuine systematic/INN synonyms are preserved.
  - Run documented schema, strict, seed-canary and full-corpus gates after separately
    authorized curation.
limitations:
- Exact cephradine allergen results in the adopted 1990/1996 full bodies were not
  verified; their complete abstracts establish broader IgE cross-reactivity context.
  No universal allergy or cross-reactivity prediction is made.
- Three adopted records lack abstracts. The original 1973 activity and 2013 brand-panel
  papers were read at complete-abstract depth; no MIC values or clinical outcomes
  were newly adopted.
- Direct HMDB and DrugBank requests returned 403, and Reaxys was only corroborated
  through current ChEBI. Eskacef has historical secondary corroboration but was not
  included in the confirmed official-product typing finding.
- The first ChEBI molfile request returned compound JSON rather than a molfile. The
  separate real molfile was retrieved and used in the successful chemistry comparison.
  The EPMC primary XML endpoint returned 500; the actual PMC full HTML supplied the
  inspected original methods and Table 2.
- The PBP assay is membrane-based pathway inhibition; it does not by itself establish
  purified-protein binding affinity or an exact holo structure. Radioiodinated cephradine-derivative
  search leads were not substituted for unmodified cephradine.
- FDA substance/product nomenclature may encompass several hydration states. No broad
  GSRS material identifier or formulation claim was added to the exact native structure.
- Initial structured adapter attempts failed DNS in the sandbox; public-network retries
  succeeded. Focused results do not substitute for documented full-corpus gates.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record or maintained input was changed; all 16 captured hashes remain
  unchanged.
- Ignored-inclusive searches covered curation, conf, raw source tables, scripts and
  documentation for the target identifiers, labels and slug. Optional missing data
  were not treated as proven defects.
- Optional links and tags in this review refer only to cephradine; no links to other
  review targets are included.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links: []
tags:
- record-review
- cephradine
- synonym-nomenclature
- brand-name
```
