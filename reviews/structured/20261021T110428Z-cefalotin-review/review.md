# Review of cefalotin

- Review: 20261021T110428Z-cefalotin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:44:47Z
- Finished UTC: 2026-10-21T11:04:28Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native neutral cefalotin graph, both stereocenters and checked exact public mappings agree. Original CDA-1 susceptibility and hydrolysis experiments and OmpK35/OmpK36 deletion experiments support selected imported resistance routes. A primary PBP1b study provides a bounded cephalothin acylation lead for optional target enrichment. All 51 adopted or parent PMID records were resolved at the stated depth. No required native correction was demonstrated; several peripheral mappings and most determinant-specific primary experiments remain incompletely verified. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact SEEDED cefalotin record, five history events, all 27 imported resistance entries, the PBP target, actual ChEBI/ARO owners and all 51 adopted or parent PMID leads; selected original resistance studies and a bounded primary target follow-up.

Selection: Queue 208; original 13 captured inputs preserved, with five actual ARO/evidence owner inputs appended before detailed judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:124991 | data/antibiotics/antibacterial/cefalotin.yaml | generated | cefalotin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema check | passed | True | CHEBI:124991 | Exit 0. |
| Documented strict check | passed | True | CHEBI:124991 | Exit 0, zero ERROR rows. |
| Supplemental exact graph consistency | passed | False | CHEBI:124991 | Exit 0 using the 019 chemistry interpreter against 021 files. |
| Structured source catalog | passed | False | CHEBI:124991 | Catalog inspected before protein follow-up. |
| Structured AcrB query | passed | False | CHEBI:124991 | Gene annotation hit; no iModulon component hit. |
| Structured blaC query | passed | False | CHEBI:124991 | Gene annotation hit; no iModulon component hit. |
| Structured ampC query | passed | False | CHEBI:124991 | Gene annotation hit; no iModulon component hit. |
| Structured penicillin query | passed | False | CHEBI:124991 | Gene annotation hit; no iModulon component hit. |
| Authoritative full QC | failed | True | CHEBI:124991 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:124991 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:124991 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:124991 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:124991 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:124991 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:124991 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:124991 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:124991 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral free acid

identity: supported. Targets: CHEBI:124991.

The checked public graphs agree, including both R stereocenters; salt and enzyme-adduct forms are not substituted.

### Peripheral exact references

identity: unknown. Targets: CHEBI:124991.

HMDB, LINCS and commercial registry records were not independently resolved to a structure. This is an access/verification limitation, not a demonstrated mismatch.

### Class and activity roles

grounding: supported. Targets: CHEBI:124991.

Structure, original antibacterial studies and separate IgE evidence support their respective class/role contexts.

### Selected original resistance experiments

evidence: supported. Targets: CHEBI:124991.

CDA-1 and porin experiments support exact cephalothin routes at bounded strain, expression and assay scope.

### Other imported resistance entries

evidence: unknown. Targets: CHEBI:124991.

Database provenance is explicit; all lead abstracts/metadata were checked, but no exhaustive original assay audit of the remaining determinants is claimed.

### Optional primary PBP evidence

completeness: supported. Targets: CHEBI:124991.

The family-level target is plausible and a direct acylation lead exists; current PRIMARY_EVIDENCE_NEEDED correctly describes its imported evidence.

### References, source ownership and history

provenance: supported. Targets: CHEBI:124991.

All 51 lead records resolve at stated depth, actual owner rows match, and five history events remain unchanged.

### Focused validation

schema: supported. Targets: CHEBI:124991.

Focused checks and supplemental exact graph comparison passed.

## Findings

### F1: A bounded primary PBP acylation lead is available for optional enrichment

informational / open / confirmed; issue key: chebi-124991-optional-pbp-primary-evidence.

The imported PBP target openly requests primary evidence. The original PBP1b Table 1 reports cephalothin acylation, offering a concrete follow-up, but the entire methods context was not recovered in this review. This is optional enrichment rather than a demonstrated defect in the current database-derived target.

## Recommended Actions And Acceptance Checks

### A1

If curating primary target evidence, recover the complete PBP1b experiment and add a separate scoped primary claim using the native validated writer.

- Verify the exact cephalothin reagent, soluble construct, organism, acylation assay and units in the original article before quantitative adoption; do not relabel nitrocefin/cefotaxime crystal structures as cephalothin structures.
- Retain the family-level ARO target and original CARD source. Add any PRIMARY_LITERATURE claim with its own organism/construct context and claim-level citation; a protein example requires independent reviewed-UniProt verification.
- Use record_curation_event and write_validated_antibiotic for authorized native curation, then run focused schema/strict and required reference/history/source/full-corpus gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cefalotin.yaml; Entire YAML and five history events | supports | EXACT/SEEDED cefalotin is the neutral free acid. Twenty-seven resistance entries retain explicit CARD database provenance. The family-level PBP target is CARD_ARO with PRIMARY_EVIDENCE_NEEDED and unspecified organism/assay. No native MIC, producer or causal graph is asserted. |
| chemistry | CHEBI:124991; PubChem:6024; CHEMBL617; KEGG:C07761; PDB-CCD:CLS; 208-chemistry.py/.json; current public structure snapshots | supports | SMILES, InChI, full key XIURVHNZVLADCM-IUODEOHRSA-N, formula C16H16N2O6S2, charge 0, masses and two R centers agree. Current ChEBI, PubChem, ChEMBL, KEGG compound and CCD CLS agree with this intact graph. CLS is not a ring-opened enzyme adduct. No sodium ion or extra proton is introduced. |
| grounding | CHEBI:124991; ARO:3000704; ARO:0000032; 208-ols.json; 208-chebi.html; 208-aro-stanzas.txt; 208-kegg.txt; 208-drugcentral.html; 208-cls.json | partial | Cephalosporin, thiophene, carboxylic acid, azabicycloalkene, semisynthetic derivative and beta-lactam allergen parents are consistent with the native graph and authority record. Antimicrobial agent/antibacterial drug roles agree. KEGG D07635 and DrugCentral 574 resolve cefalotin in drug context; DB00456 is corroborated by CCD related mappings rather than a direct DrugBank fetch. Drug and document references remain separately placed. CAS 153-61-7 is authority-corroborated, not independently registry-verified. |
| activity | PMID:13963283; PMID:7571387; 208-core.json: complete original-study abstracts | supports | The 1963 original study identifies the 7-aminocephalosporanic-acid-derived thiopheneacetamido antibiotic and reports antibacterial activity using gradient plates. The 1995 veterinary study reports cephalothin activity against its staphylococcal and E. coli isolate collections and drug exposure in dogs. These support antibacterial/semisynthetic context; historical panels and pharmacokinetics are not contemporary universal susceptibility or a salt-identification assay. |
| allergen | PMID:12569987; PMID:2083978; 208-core.json: complete original-study abstracts | supports | Human IgE binding and hapten inhibition with cephalothin support the allergen context. They do not identify an antibacterial molecular target. Other ChEBI allergy leads concern broader antibody recognition, aztreonam or penicillin determinants and remain contextual. |
| cda | PMID:25136020; DOI:10.1128/aac.03237-14; 207-cda.html, original Methods/Results and Tables 1–2 rechecked for cephalothin | supports | Table 1 reports cephalothin MIC &gt;256 micrograms/mL for E. coli TOP10(pCDA-1), versus 1 for TOP10; porin-deficient HB4 already has 256 without that plasmid. Table 2 directly measures purified CDA-1 cephalothin hydrolysis: kcat 580 ±15 s^-1, Km 40 ±5 micromolar and kcat/Km 14,500 mM^-1 s^-1. Thus both phenotype and inactivation support exist, with enzyme expression and permeability distinguished. |
| porins | PMID:27645385; DOI:10.1128/JB.00590-16; 154-omp35.html, original Methods, Results and Tables 1/3 | supports | Clean K. pneumoniae ATCC 11296 deletions yield cephalothin MICs of 8 micrograms/mL for the parent, 32 for delta-ompK35 and 16 for delta-ompK36. The study used twofold broth dilution in LB plus 5 mM MgCl2, approximately 10^3 inoculated cells and 16 h at 37 C. Separate porin-expression experiments measure cephalothin influx in engineered E. coli. These support reduced-permeability routes through porin loss; normal porin activity enables influx. The paper identifies ATCC 11296 as subsp. ozaenae, so these values are not universal clinical breakpoints. |
| pbp | PMID:15637155; DOI:10.1073/pnas.0407186102; 208-pbp-core.json complete abstract; original PMC Methods/Results/Table 1 excerpts exposed by web search, 208-pbp-web.json | partial | The pneumococcal PBP1b study reports stopped-flow cephalothin acylation for defined constructs. Table 1 gives 253.8 ±20.0 times 10^3 M^-1 s^-1 for the WT soluble 74–791 construct and lower values for altered constructs. This is direct acylation evidence for optional target enrichment. Its antibiotic crystal structures use nitrocefin and cefotaxime, not cephalothin. The whole original article was not retrieved; quantitative adoption needs complete experimental-context verification. |
| substrates | PMID:33416461; DOI:10.1099/mgen.0.000500; 208-substrates.xml, Results on beta-lactamase substrate activity and ARP methods | context_only | The original study experimentally tests several native beta-lactamase names in an E. coli expression platform, but its newly assigned substrates include cefazolin, cefixime and other beta-lactams. These results must not be transferred to cefalotin merely because the determinant is shared. The paper also emphasizes host-dependent OXA-50 phenotype. Its in silico associations are separated from AST validation. |
| adopted-leads | All 51 adopted/parent PMID records; 208-core.json; 208-lead-dispositions.json; 208-aro-stanzas.txt | context_only | All 51 MED records resolve: 46 complete abstracts were read and five entries are metadata-only. The disposition file lists each scope. TRU-1, SED-1, AMZ-1, PSZ-1 and EBR-5 abstracts explicitly discuss cephalothin hydrolysis; several other determinant citations concern sequence, mobile-element context or other substrates. PBP/class references include reviews. Abstract or database coverage is not full primary verification of all 27 imported routes. |
| adapter | iModulonDB; 208-imodulondb-datasets.txt and four query outputs | context_only | The catalog and native structured adapter were used before protein web follow-up. Hits were e_coli/modulome/b0462 (AcrB), m_tuberculosis/modulome/Rv2068c (blaC), p_aeruginosa/precise364/PA4110 (ampC), and e_coli/modulome/b2430 (PBP4B/yfeW). No iModulon component hit required summarize. These are annotation context, not cefalotin experiments; PA4110 is not verification of PDC-3 or PDC-5 alleles, and E. coli PBP4B is not the pneumococcal PBP1b assay. |
| owners | data/raw/aro_resistance_edges.tsv; data/raw/aro_target_edges.tsv; 208-aro_resistance_edges.json; 208-aro_target_edges.json; extractor/seeder; maintained evidence-review owner | supports | All 27 native determinant IDs/mechanism types match their exact adopted rows. The single family-level PBP target matches the imported target row and keeps its database-only status. The ignored-inclusive local search found AST mapping context but no separate native cefalotin primary mechanism claim. Existing card_evidence_reviews qualifies imported resistance evidence notes; it is not a general primary-target writer. |
| validation | Focused schema, strict and supplemental chemistry checks; 208-strict.tsv; 208-chemistry.json | supports | Native schema and strict checks passed with exit 0. Supplemental chemistry passed using the 019 RDKit environment against 021 files. Required shared reference/history/source and full-corpus gates are separate. |

## Limits And Additional Notes

- Five adopted/parent MED entries have no indexed abstract: 18550213, 15673804, 6810737, 5326330 and 14251901. Forty-six complete abstracts were read. Complete original CDA-1 and porin HTML and selected substrate-study sections provide deeper support, not full verification of every determinant.
- The PBP1b complete abstract and original Methods/Results/Table 1 excerpts were inspected via web search. Europe PMC full-text XML returned HTTP 500; direct PMC HTML returned a browser challenge, Europe PMC HTML returned 403, and the author-copy route returned 429. The saved 208-pbp.html/alt.html are challenge pages and are not cited as original full text. No whole-article or cephalothin crystal inspection is claimed.
- Additional OXA-50 and early activity/AcrAB full-text routes failed or returned challenge pages. An indexed OXA-50 original table excerpt indicates weak cephalothin hydrolysis; no new quantitative claim or universal phenotype conclusion is adopted from that incomplete access.
- HMDB XML returned 403. PubChem name lookup for LINCS LSM-15184 returned 404 and did not resolve that mapping. Reaxys/Beilstein and CAS were not directly registry-verified; direct DrugBank and patents were not inspected. Their absence of independent verification is not evidence of an incorrect native mapping.
- No standardized MIC observations, breakpoint interpretation, causal graph or producer claim was added. Historical activity and clinical/prophylaxis papers retain their tested contexts. Most source determinant citations remain abstract-level leads.
- The 021 environment lacks RDKit, so supplemental chemistry used the existing 019 interpreter. Native schema/strict passed, but these focused checks do not substitute for required shared corpus gates or promote native scientific status.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 18 repository input hashes and the external ARO cache hash remain unchanged. No native record, saved bundle or Git state was modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T110428Z-cefalotin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of cefalotin
started_at: '2026-10-21T10:44:47Z'
finished_at: '2026-10-21T11:04:28Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: Exact neutral cefalotin identity supported; imported mechanisms retain
  honest database provenance
scientific_review: true
summary: The native neutral cefalotin graph, both stereocenters and checked exact
  public mappings agree. Original CDA-1 susceptibility and hydrolysis experiments
  and OmpK35/OmpK36 deletion experiments support selected imported resistance routes.
  A primary PBP1b study provides a bounded cephalothin acylation lead for optional
  target enrichment. All 51 adopted or parent PMID records were resolved at the stated
  depth. No required native correction was demonstrated; several peripheral mappings
  and most determinant-specific primary experiments remain incompletely verified.
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
  - path: data/antibiotics/antibacterial/cefalotin.yaml
    sha256: d3bcac46436b8e693f0d1ec4dbb584e733f11e37714468818058aeb8274cc028
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
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
scope:
  description: Entire exact SEEDED cefalotin record, five history events, all 27 imported
    resistance entries, the PBP target, actual ChEBI/ARO owners and all 51 adopted
    or parent PMID leads; selected original resistance studies and a bounded primary
    target follow-up.
  selection: Queue 208; original 13 captured inputs preserved, with five actual ARO/evidence
    owner inputs appended before detailed judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:124991
targets:
- target_id: CHEBI:124991
  path: data/antibiotics/antibacterial/cefalotin.yaml
  label: cefalotin
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
    role: Actual imported ARO claim or maintained evidence owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Actual imported ARO claim or maintained evidence owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Actual imported ARO claim or maintained evidence owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Actual imported ARO claim or maintained evidence owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Actual imported ARO claim or maintained evidence owner
checks:
- check_id: schema
  name: Documented schema check
  status: passed
  required: true
  summary: Exit 0.
  target_ids:
  - CHEBI:124991
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefalotin.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict check
  status: passed
  required: true
  summary: Exit 0, zero ERROR rows.
  target_ids:
  - CHEBI:124991
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefalotin.yaml --out /private/tmp/am-review-session/208-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Supplemental exact graph consistency
  status: passed
  required: false
  summary: Exit 0 using the 019 chemistry interpreter against 021 files.
  target_ids:
  - CHEBI:124991
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/208-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: adapter-catalog
  name: Structured source catalog
  status: passed
  required: false
  summary: Catalog inspected before protein follow-up.
  target_ids:
  - CHEBI:124991
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets > /private/tmp/am-review-session/208-imodulondb-datasets.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-acrb
  name: Structured AcrB query
  status: passed
  required: false
  summary: Gene annotation hit; no iModulon component hit.
  target_ids:
  - CHEBI:124991
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset modulome --query AcrB
    > /private/tmp/am-review-session/208-imodulondb-acrb.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-blac
  name: Structured blaC query
  status: passed
  required: false
  summary: Gene annotation hit; no iModulon component hit.
  target_ids:
  - CHEBI:124991
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism m_tuberculosis --dataset modulome --query
    blaC > /private/tmp/am-review-session/208-imodulondb-blac.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-ampc
  name: Structured ampC query
  status: passed
  required: false
  summary: Gene annotation hit; no iModulon component hit.
  target_ids:
  - CHEBI:124991
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism p_aeruginosa --dataset precise364 --query
    ampC > /private/tmp/am-review-session/208-imodulondb-ampc.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-pbp
  name: Structured penicillin query
  status: passed
  required: false
  summary: Gene annotation hit; no iModulon component hit.
  target_ids:
  - CHEBI:124991
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset modulome --query penicillin
    > /private/tmp/am-review-session/208-imodulondb-pbp.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:124991
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
  - CHEBI:124991
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
  - CHEBI:124991
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
  - CHEBI:124991
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
  - CHEBI:124991
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
  - CHEBI:124991
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
  - CHEBI:124991
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
  - CHEBI:124991
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
  - CHEBI:124991
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cefalotin.yaml
  locator: Entire YAML and five history events
  accessed_at: '2026-10-21T11:03:43Z'
  support: supports
  summary: EXACT/SEEDED cefalotin is the neutral free acid. Twenty-seven resistance
    entries retain explicit CARD database provenance. The family-level PBP target
    is CARD_ARO with PRIMARY_EVIDENCE_NEEDED and unspecified organism/assay. No native
    MIC, producer or causal graph is asserted.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:124991; PubChem:6024; CHEMBL617; KEGG:C07761; PDB-CCD:CLS
  locator: 208-chemistry.py/.json; current public structure snapshots
  accessed_at: '2026-10-21T11:03:43Z'
  support: supports
  summary: SMILES, InChI, full key XIURVHNZVLADCM-IUODEOHRSA-N, formula C16H16N2O6S2,
    charge 0, masses and two R centers agree. Current ChEBI, PubChem, ChEMBL, KEGG
    compound and CCD CLS agree with this intact graph. CLS is not a ring-opened enzyme
    adduct. No sodium ion or extra proton is introduced.
  snapshot_sha256: 54a7af977a583c9d9e1fe8c5e2b6997c4f6f50feb2a316072b813f39ebdcdd64
- evidence_id: grounding
  kind: authority
  reference: CHEBI:124991; ARO:3000704; ARO:0000032
  locator: 208-ols.json; 208-chebi.html; 208-aro-stanzas.txt; 208-kegg.txt; 208-drugcentral.html;
    208-cls.json
  accessed_at: '2026-10-21T11:03:43Z'
  support: partial
  summary: Cephalosporin, thiophene, carboxylic acid, azabicycloalkene, semisynthetic
    derivative and beta-lactam allergen parents are consistent with the native graph
    and authority record. Antimicrobial agent/antibacterial drug roles agree. KEGG
    D07635 and DrugCentral 574 resolve cefalotin in drug context; DB00456 is corroborated
    by CCD related mappings rather than a direct DrugBank fetch. Drug and document
    references remain separately placed. CAS 153-61-7 is authority-corroborated, not
    independently registry-verified.
  snapshot_sha256: 194070a6564b0544c8b832fb4ddc58d646c7fbc58e6ff720a605298737038d42
- evidence_id: activity
  kind: primary_source
  reference: PMID:13963283; PMID:7571387
  locator: '208-core.json: complete original-study abstracts'
  accessed_at: '2026-10-21T11:03:43Z'
  support: supports
  summary: The 1963 original study identifies the 7-aminocephalosporanic-acid-derived
    thiopheneacetamido antibiotic and reports antibacterial activity using gradient
    plates. The 1995 veterinary study reports cephalothin activity against its staphylococcal
    and E. coli isolate collections and drug exposure in dogs. These support antibacterial/semisynthetic
    context; historical panels and pharmacokinetics are not contemporary universal
    susceptibility or a salt-identification assay.
  snapshot_sha256: d07905990c4f514bc9efda12b4217ff0196438e9a9f35fb1a771b79961972a7c
- evidence_id: allergen
  kind: primary_source
  reference: PMID:12569987; PMID:2083978
  locator: '208-core.json: complete original-study abstracts'
  accessed_at: '2026-10-21T11:03:43Z'
  support: supports
  summary: Human IgE binding and hapten inhibition with cephalothin support the allergen
    context. They do not identify an antibacterial molecular target. Other ChEBI allergy
    leads concern broader antibody recognition, aztreonam or penicillin determinants
    and remain contextual.
  snapshot_sha256: d07905990c4f514bc9efda12b4217ff0196438e9a9f35fb1a771b79961972a7c
- evidence_id: cda
  kind: primary_source
  reference: PMID:25136020
  locator: DOI:10.1128/aac.03237-14; 207-cda.html, original Methods/Results and Tables
    1–2 rechecked for cephalothin
  accessed_at: '2026-10-21T11:03:43Z'
  support: supports
  summary: 'Table 1 reports cephalothin MIC >256 micrograms/mL for E. coli TOP10(pCDA-1),
    versus 1 for TOP10; porin-deficient HB4 already has 256 without that plasmid.
    Table 2 directly measures purified CDA-1 cephalothin hydrolysis: kcat 580 ±15
    s^-1, Km 40 ±5 micromolar and kcat/Km 14,500 mM^-1 s^-1. Thus both phenotype and
    inactivation support exist, with enzyme expression and permeability distinguished.'
  snapshot_sha256: b7bd4dfa5f8bd2dec1b70dee503f9e9a05d454eddcd310cb3b1bf7b86faf8d21
- evidence_id: porins
  kind: primary_source
  reference: PMID:27645385
  locator: DOI:10.1128/JB.00590-16; 154-omp35.html, original Methods, Results and
    Tables 1/3
  accessed_at: '2026-10-21T11:03:43Z'
  support: supports
  summary: Clean K. pneumoniae ATCC 11296 deletions yield cephalothin MICs of 8 micrograms/mL
    for the parent, 32 for delta-ompK35 and 16 for delta-ompK36. The study used twofold
    broth dilution in LB plus 5 mM MgCl2, approximately 10^3 inoculated cells and
    16 h at 37 C. Separate porin-expression experiments measure cephalothin influx
    in engineered E. coli. These support reduced-permeability routes through porin
    loss; normal porin activity enables influx. The paper identifies ATCC 11296 as
    subsp. ozaenae, so these values are not universal clinical breakpoints.
  snapshot_sha256: c21bc68dfe2b992b25a48da1d878e85f15c647486a2cfbe99733b756c4f2d8e4
- evidence_id: pbp
  kind: primary_source
  reference: PMID:15637155
  locator: DOI:10.1073/pnas.0407186102; 208-pbp-core.json complete abstract; original
    PMC Methods/Results/Table 1 excerpts exposed by web search, 208-pbp-web.json
  accessed_at: '2026-10-21T11:03:43Z'
  support: partial
  summary: The pneumococcal PBP1b study reports stopped-flow cephalothin acylation
    for defined constructs. Table 1 gives 253.8 ±20.0 times 10^3 M^-1 s^-1 for the
    WT soluble 74–791 construct and lower values for altered constructs. This is direct
    acylation evidence for optional target enrichment. Its antibiotic crystal structures
    use nitrocefin and cefotaxime, not cephalothin. The whole original article was
    not retrieved; quantitative adoption needs complete experimental-context verification.
  snapshot_sha256: 831f4fb35b9a6c478cda3ab4a70dbcf00d933c32c68f931149ede1af582257a2
- evidence_id: substrates
  kind: primary_source
  reference: PMID:33416461
  locator: DOI:10.1099/mgen.0.000500; 208-substrates.xml, Results on beta-lactamase
    substrate activity and ARP methods
  accessed_at: '2026-10-21T11:03:43Z'
  support: context_only
  summary: The original study experimentally tests several native beta-lactamase names
    in an E. coli expression platform, but its newly assigned substrates include cefazolin,
    cefixime and other beta-lactams. These results must not be transferred to cefalotin
    merely because the determinant is shared. The paper also emphasizes host-dependent
    OXA-50 phenotype. Its in silico associations are separated from AST validation.
  snapshot_sha256: 20de54b193f86d76e5985b4aadbe8442d7ded8a30d6a15f0050c7e1d76f8dd18
- evidence_id: adopted-leads
  kind: database
  reference: All 51 adopted/parent PMID records
  locator: 208-core.json; 208-lead-dispositions.json; 208-aro-stanzas.txt
  accessed_at: '2026-10-21T11:03:43Z'
  support: context_only
  summary: 'All 51 MED records resolve: 46 complete abstracts were read and five entries
    are metadata-only. The disposition file lists each scope. TRU-1, SED-1, AMZ-1,
    PSZ-1 and EBR-5 abstracts explicitly discuss cephalothin hydrolysis; several other
    determinant citations concern sequence, mobile-element context or other substrates.
    PBP/class references include reviews. Abstract or database coverage is not full
    primary verification of all 27 imported routes.'
  snapshot_sha256: d07905990c4f514bc9efda12b4217ff0196438e9a9f35fb1a771b79961972a7c
- evidence_id: adapter
  kind: database
  reference: iModulonDB
  locator: 208-imodulondb-datasets.txt and four query outputs
  accessed_at: '2026-10-21T11:03:43Z'
  support: context_only
  summary: The catalog and native structured adapter were used before protein web
    follow-up. Hits were e_coli/modulome/b0462 (AcrB), m_tuberculosis/modulome/Rv2068c
    (blaC), p_aeruginosa/precise364/PA4110 (ampC), and e_coli/modulome/b2430 (PBP4B/yfeW).
    No iModulon component hit required summarize. These are annotation context, not
    cefalotin experiments; PA4110 is not verification of PDC-3 or PDC-5 alleles, and
    E. coli PBP4B is not the pneumococcal PBP1b assay.
  snapshot_sha256: 98627808541dbd07b37e85a4bfb692fc0fe8a0a9564839813c9f2f9ac41a4a10
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_resistance_edges.tsv; data/raw/aro_target_edges.tsv
  locator: 208-aro_resistance_edges.json; 208-aro_target_edges.json; extractor/seeder;
    maintained evidence-review owner
  accessed_at: '2026-10-21T11:03:43Z'
  support: supports
  summary: All 27 native determinant IDs/mechanism types match their exact adopted
    rows. The single family-level PBP target matches the imported target row and keeps
    its database-only status. The ignored-inclusive local search found AST mapping
    context but no separate native cefalotin primary mechanism claim. Existing card_evidence_reviews
    qualifies imported resistance evidence notes; it is not a general primary-target
    writer.
  snapshot_sha256: f74f1812162fdadef129b66ebb74457c9a6f45852ff7a5c1beb59e56a765ba36
  search_scope: rg --no-ignore --hidden for cefalotin, cephalothin, CHEBI:124991 and
    ARO:3000704 across curation/conf/data/antibiotics; 208-local-hits.txt inspected.
- evidence_id: validation
  kind: validation
  reference: Focused schema, strict and supplemental chemistry checks
  locator: 208-strict.tsv; 208-chemistry.json
  accessed_at: '2026-10-21T11:03:43Z'
  support: supports
  summary: Native schema and strict checks passed with exit 0. Supplemental chemistry
    passed using the 019 RDKit environment against 021 files. Required shared reference/history/source
    and full-corpus gates are separate.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral free acid
  outcome: supported
  summary: The checked public graphs agree, including both R stereocenters; salt and
    enzyme-adduct forms are not substituted.
  target_ids:
  - CHEBI:124991
  evidence_ids:
  - chemistry
  - grounding
- assessment_id: peripheral-xrefs
  area: identity
  topic: Peripheral exact references
  outcome: unknown
  summary: HMDB, LINCS and commercial registry records were not independently resolved
    to a structure. This is an access/verification limitation, not a demonstrated
    mismatch.
  target_ids:
  - CHEBI:124991
  evidence_ids:
  - grounding
- assessment_id: classification
  area: grounding
  topic: Class and activity roles
  outcome: supported
  summary: Structure, original antibacterial studies and separate IgE evidence support
    their respective class/role contexts.
  target_ids:
  - CHEBI:124991
  evidence_ids:
  - chemistry
  - grounding
  - activity
  - allergen
- assessment_id: selected-resistance
  area: evidence
  topic: Selected original resistance experiments
  outcome: supported
  summary: CDA-1 and porin experiments support exact cephalothin routes at bounded
    strain, expression and assay scope.
  target_ids:
  - CHEBI:124991
  evidence_ids:
  - cda
  - porins
- assessment_id: remaining-resistance
  area: evidence
  topic: Other imported resistance entries
  outcome: unknown
  summary: Database provenance is explicit; all lead abstracts/metadata were checked,
    but no exhaustive original assay audit of the remaining determinants is claimed.
  target_ids:
  - CHEBI:124991
  evidence_ids:
  - adopted-leads
  - substrates
  - record
- assessment_id: target
  area: completeness
  topic: Optional primary PBP evidence
  outcome: supported
  summary: The family-level target is plausible and a direct acylation lead exists;
    current PRIMARY_EVIDENCE_NEEDED correctly describes its imported evidence.
  target_ids:
  - CHEBI:124991
  evidence_ids:
  - pbp
  - record
- assessment_id: provenance
  area: provenance
  topic: References, source ownership and history
  outcome: supported
  summary: All 51 lead records resolve at stated depth, actual owner rows match, and
    five history events remain unchanged.
  target_ids:
  - CHEBI:124991
  evidence_ids:
  - adopted-leads
  - owners
  - record
- assessment_id: schema
  area: schema
  topic: Focused validation
  outcome: supported
  summary: Focused checks and supplemental exact graph comparison passed.
  target_ids:
  - CHEBI:124991
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: chebi-124991-optional-pbp-primary-evidence
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: A bounded primary PBP acylation lead is available for optional enrichment
  description: The imported PBP target openly requests primary evidence. The original
    PBP1b Table 1 reports cephalothin acylation, offering a concrete follow-up, but
    the entire methods context was not recovered in this review. This is optional
    enrichment rather than a demonstrated defect in the current database-derived target.
  target_ids:
  - CHEBI:124991
  field_paths:
  - molecular_targets[0].evidence_status
  - molecular_targets[0].experimental_context
  evidence_ids:
  - pbp
  - record
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefalotin.yaml
    role: Curator-owned primary target evidence through the native validated writer
  - repository: CultureBotAI/AntibioticMech
    path: docs/CURATION.md
    role: Native curation and evidence placement requirements
  native_severity: optional enrichment; no required native correction
  normalization_reason: The record does not claim this primary experiment and explicitly
    labels its imported target evidence as incomplete.
actions:
- action_id: A1
  description: If curating primary target evidence, recover the complete PBP1b experiment
    and add a separate scoped primary claim using the native validated writer.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:124991
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefalotin.yaml
    role: Curator-owned primary target evidence through the native validated writer
  - repository: CultureBotAI/AntibioticMech
    path: docs/CURATION.md
    role: Native curation and evidence placement requirements
  acceptance_checks:
  - Verify the exact cephalothin reagent, soluble construct, organism, acylation assay
    and units in the original article before quantitative adoption; do not relabel
    nitrocefin/cefotaxime crystal structures as cephalothin structures.
  - Retain the family-level ARO target and original CARD source. Add any PRIMARY_LITERATURE
    claim with its own organism/construct context and claim-level citation; a protein
    example requires independent reviewed-UniProt verification.
  - Use record_curation_event and write_validated_antibiotic for authorized native
    curation, then run focused schema/strict and required reference/history/source/full-corpus
    gates.
limitations:
- 'Five adopted/parent MED entries have no indexed abstract: 18550213, 15673804, 6810737,
  5326330 and 14251901. Forty-six complete abstracts were read. Complete original
  CDA-1 and porin HTML and selected substrate-study sections provide deeper support,
  not full verification of every determinant.'
- The PBP1b complete abstract and original Methods/Results/Table 1 excerpts were inspected
  via web search. Europe PMC full-text XML returned HTTP 500; direct PMC HTML returned
  a browser challenge, Europe PMC HTML returned 403, and the author-copy route returned
  429. The saved 208-pbp.html/alt.html are challenge pages and are not cited as original
  full text. No whole-article or cephalothin crystal inspection is claimed.
- Additional OXA-50 and early activity/AcrAB full-text routes failed or returned challenge
  pages. An indexed OXA-50 original table excerpt indicates weak cephalothin hydrolysis;
  no new quantitative claim or universal phenotype conclusion is adopted from that
  incomplete access.
- HMDB XML returned 403. PubChem name lookup for LINCS LSM-15184 returned 404 and
  did not resolve that mapping. Reaxys/Beilstein and CAS were not directly registry-verified;
  direct DrugBank and patents were not inspected. Their absence of independent verification
  is not evidence of an incorrect native mapping.
- No standardized MIC observations, breakpoint interpretation, causal graph or producer
  claim was added. Historical activity and clinical/prophylaxis papers retain their
  tested contexts. Most source determinant citations remain abstract-level leads.
- The 021 environment lacks RDKit, so supplemental chemistry used the existing 019
  interpreter. Native schema/strict passed, but these focused checks do not substitute
  for required shared corpus gates or promote native scientific status.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 18 repository input hashes and the external ARO cache hash remain unchanged.
  No native record, saved bundle or Git state was modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.1073/pnas.0407186102
- https://doi.org/10.1128/aac.03237-14
- https://doi.org/10.1128/JB.00590-16
- https://doi.org/10.1099/mgen.0.000500
tags:
- record-review
- cefalotin
- primary-evidence-scope
```
