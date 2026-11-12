# Clioquinol: supported exact identity and activity, minor source spelling and scoped evidence follow-up

- Review: 20261021T075738Z-5-chloro-7-iodoquinolin-8-ol
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:36:23Z
- Finished UTC: 2026-10-21T07:57:38Z
- Reviewer: Codex review002 subagent with coordinator validation captures (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Exact clioquinol chemistry, broader parents, antimicrobial roles and source provenance are coherent. Current product information supports topical cream use; a primary pilot trial supports the qualified Alzheimer-investigation statement. One minor spelling error is inherited from ChEBI, and one informational opportunity concerns scoped assay/mechanism evidence. Primary bacterial, fungal, host and analogue contexts must remain distinct. Focused schema, strict and corrected independent chemistry checks pass. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted identifiers and definition claims, maintained inputs, all adopted citation records, and bounded additional activity/mechanism research.

Selection: Queue index049, CHEBI:74460 at its locked native path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:74460 | data/antibiotics/antibacterial/5-chloro-7-iodoquinolin-8-ol.yaml | generated | 5-chloro-7-iodoquinolin-8-ol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused LinkML validation | passed | True | CHEBI:74460 | Coordinator command exited0 with no issues. |
| Focused strict validation | passed | True | CHEBI:74460 | Coordinator scanned one file; zero ERROR rows. |
| Initial independent chemistry helper | failed | False | CHEBI:74460 | The initial helper incorrectly calculated the source mint with SHA1. Structures, formula, masses and charge passed; the helper defect produced mint_matches:false. Original output is retained. This was not a native-record failure. The original exit code is not retained in the supplied capture. |
| Corrected independent chemistry helper | passed | False | CHEBI:74460 | After aligning mint calculation with repository SHA256 of CHEBI&#124;source_id, all checks passed without changing the native record. |
| Structured dataset inventory | passed | False | CHEBI:74460 | Inventory retrieved; human, Candida and Saccharomyces contexts are not covered. M.tuberculosis/modulome is covered. |
| Covered bacterial enzyme context | passed | False | CHEBI:74460 | Exact methionine-aminopeptidase search returned mapA/Rv0734 and mapB/Rv2861c genes and zero iModulons. No component summary applies. |
| Independent registry and LINCS access | unavailable | False | CHEBI:74460 | NIST/CAS endpoint and LINCS routes were inaccessible; Reaxys was not independently inspected. CAS is corroborated by multiple official chemical/drug records; LINCS and Reaxys remain ChEBI-source assertions. |
| Additional full-text access | unavailable | False | CHEBI:74460 | One adopted citation has no abstract. Most adopted host papers were checked at abstract level. The 2011 MetAP and copper-context full texts were blocked by PMC/EuropePMC routes; the 2018 cream-study PDF was403. These limits do not erase the inspected primary assay evidence. |
| Authoritative full QC | failed | True | CHEBI:74460 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:74460 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:74460 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:74460 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:74460 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:74460 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:74460 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:74460 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:74460 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact clioquinol identity

identity: supported. Targets: CHEBI:74460.

Official identity records, all native synonyms and independently calculated chemistry agree. Sibling hydroxyquinolines and metal complexes remain separate.

### Broader parents and activity roles

grounding: supported. Targets: CHEBI:74460.

Chemical parents fit and independent primary/official evidence supports antibacterial, antifungal and historical antiprotozoal roles. ANTIBACTERIAL class is compatible with additional activity roles.

### All cross-reference groups

grounding: supported. Targets: CHEBI:74460.

Drug/ligand/document identifiers resolve with noted LINCS/Reaxys/NIST limits. Patent topic links are not asserted as modern structure or efficacy proof.

### Topical use and Alzheimer investigation

evidence: supported. Targets: CHEBI:74460.

Current product information and a primary pilot trial support the qualified definition. No universal approval or efficacy is implied.

### Inherited definition spelling

representation: concern. Targets: CHEBI:74460.

The word atifungal is a confirmed spelling error reproduced from the source; it does not change identity or the otherwise supported activity claim.

### Mechanism completeness and scope

evidence: supported. Targets: CHEBI:74460.

There are primary biochemical and fungal phenotype observations suitable for qualified enrichment. Their absence is optional; host pathways, analogue data and disputed cell-wall effects require explicit separation.

### Producer, resistance and graph fields

representation: not_applicable. Targets: CHEBI:74460.

No native objects require correction. No biological producer, clinical efficacy or universal resistance mechanism follows from these observations.

### Claim-level evidence and assay objects

completeness: supported. Targets: CHEBI:74460.

The seed can be enriched using exact primary data with endpoint, species, formulation and metal-condition qualifiers. This is not a schema defect.

### Maintained source/status

ownership: supported. Targets: CHEBI:74460.

The record reproduces its maintained source and current ChEBI definition. Scientific additions belong to the native record; inherited definition correction belongs to the source path. All13 capture hashes remain unchanged.

### Focused checks

schema: supported. Targets: CHEBI:74460.

Focused schema and strict pass; corrected chemistry passes. The initial helper defect is documented separately.

## Findings

### F1: Correct the inherited spelling atifungal

minor / open / confirmed; issue key: chebi-74460-source-definition-atifungal-typo.

Native definition and maintained/current ChEBI source all contain atifungal where antifungal is intended. This is a presentation defect, not an unsupported antifungal claim or extraction mismatch.

### F2: Represent optional primary assay and mechanism evidence with scope qualifiers

informational / open / confirmed; issue key: chebi-74460-qualified-primary-activity-mechanism-enrichment.

Exact compound primary observations are available but absent from optional activity/evidence/target fields. They support bounded enrichment; conflicting fungal outcomes, biochemical versus cellular evidence, and formulation effects prevent a single universal mechanism claim.

## Recommended Actions And Acceptance Checks

### A1

Correct atifungal to antifungal through a reviewed source correction or source-specific normalization that remains reproducible on reseeding.

- Keep the ChEBI origin and source-version provenance truthful; do not silently patch only the generated record.
- If extraction behavior changes, regenerate the maintained inventory/manifest through the authorized source workflow and reseed; inspect the exact definition diff.
- Rerun focused schema/strict and required corpus gates after the separately authorized correction.

### A2

If selected for scientific curation, add claim-level primary evidence and qualified assay/target observations to the exact native record.

- Preserve agar versus broth assays, MIC50 versus MIC80 versus MFC, strain, duration, units, formulation and metal concentrations; do not replace &gt; endpoints with equalities.
- Keep measured enzyme inhibition distinct from validated cellular target engagement; verify exact isoform/protein grounding and evidence before adding targets.
- Preserve the2019/2020 fungal cell-wall disagreement and dose-dependent membrane results rather than generalizing to every organism.
- Do not transfer host cancer/neuro signaling, nitroxoline/CLBQ14 mechanisms or claimed clinical approvals from background text.
- Use write_validated_antibiotic and native history; rerun focused and required corpus gates without automatic status promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/5-chloro-7-iodoquinolin-8-ol.yaml; Entire YAML: definition, 12 synonyms, three chemical parents, four roles, structure, ten xrefs across three groups, source concept and four history events. | supports | The exact neutral achiral entity is clioquinol. Definition states antibacterial/antifungal properties, topical cream use and investigation as a Cu/Zn chelator for possible Alzheimer treatment. It does not claim approved Alzheimer therapy. Optional quantitative activity, molecular targets, causal graphs, resistance, producer and clinical objects are not present. The definition contains the word atifungal. |
| owner | data/raw/chebi_antimicrobials.tsv; CHEBI:74460 row1891; complete 049-raw.json; raw MANIFEST/PATHS; conf/sources.yaml; extract_chebi and build_record. | supports | The source row matches the native record, including the spelling error. Extraction carries the source definition; build_record selects the ChEBI definition. Ten source citations are leads intentionally not automatically assigned claim-level evidence. Mechanism roles are empty. Four seed/reseed events and source version2026-08-30 are coherent; all13 initial hashes remain unchanged. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:74460; Complete current ChEBI page 049-chebi.html and049-chebi.txt; PubChem CID2788 049-pubchem.json and049-pubchem-synonyms.json. | supports | ChEBI, PubChem and native chemistry agree on C9H5ClINO, neutral charge, mass305.502, exact mass304.91044, full InChI and QCDFBFJGMNKBDO-UHFFFAOYSA-N. All12 native synonym strings are corroborated by the source and PubChem synonyms; INN labels are ChEBI assertions, with clioquinol also labeled INN by KEGG. Parents36683 organochlorine,37142 organoiodine and38775 monohydroxyquinoline fit. Roles33281 antimicrobial,33282 antibacterial,35718 antifungal and35820 antiprotozoal drug are correctly separated from parent classes. CAS130-26-7 is corroborated; NIST inspection was unavailable. |
| xrefs | https://www.rcsb.org/ligand/CQL; Official CQL ligand page; https://drugcentral.org/drugcard/681 and049-drugcentral-inchi.txt/049-drugcentral-smiles.txt; https://www.kegg.jp/entry/D03538; https://go.drugbank.com/drugs/DB04815; current ChEBI xrefs. | supports | RCSB CQL has the exact native SMILES/InChI/key. DrugCentral681 returns the same full InChI and corresponding SMILES. KEGG D03538 resolves to clioquinol with matching formula/CAS and INN label. DrugBank DB04815 public page resolves to clioquinol with formula, aliases and topical description; no gated target data were inspected. LINCS LSM-2186 and Reaxys153637 are present in ChEBI but independent endpoints were unavailable or uninspected. |
| documents | https://patents.google.com/patent/US641491A/en; US641491A description/claim; DE117767C description at https://patents.google.com/patent/DE117767C/en. | context_only | Both document identifiers resolve to historical iodochloroxyquinolin preparation texts. US claim describes iodination of5-chloro-8-oxyquinoline; DE text retains uncertainty in iodine positional assignment. These are related historical documents, not modern proof of exact regioisomer identity, potency, safety or current clinical authorization. Automated patent chemical-entity links were not treated as structure evidence. |
| wiki | https://en.wikipedia.org/wiki/Clioquinol; Document cross-reference identity section only. | context_only | The page resolves to clioquinol and displays the same full InChI/key. It is used to verify the document link only; mechanistic, regulatory and clinical claims were assessed against primary or official sources. |
| chemistry-initial | Coordinator initial helper result; 049-initial-chemistry.json and049-initial-chemistry.log. | context_only | The earlier helper output has matching native SMILES/InChI structures but a wrong SHA1-derived mint. The review preserves this actual failed helper attempt and subsequent correction. |
| chemistry | Coordinator corrected RDKit calculation; 049-focused-results.json;049-chemistry.json/log; inspected current chem005.py. | supports | Both structures parse to the same neutral single fragment with no tetrahedral centers, formulaC9H5ClINO, mass305.502 and exact mass304.91043946. Full key and repository SHA256 mint antibioticmech:chebi-781dacc9d8 match. Final helper exited0. |
| topical | https://www.medicines.org.uk/emc/product/12911/smpc; Current Chemidex Betamethasone valerate/Clioquinol cream SmPC, revised2025-10-16; sections2,4.1,4.3,5.1. | supports | The marketed combination contains30mg/g clioquinol and identifies its antibacterial and anticandidal actions. Indications concern inflammatory skin conditions with secondary infection present, suspected or likely. This supports use in creams; it does not justify universal skin-infection treatment or transferring the corticosteroid’s effects to clioquinol. |
| alzheimer | PMID:14676042; DOI:10.1001/archneur.60.12.1685; complete official abstract in049-additional-epmc.json. | supports | A36-person randomized pilot phase2 study explicitly investigated clioquinol as a metal-protein-attenuating compound involving Cu/Zn and amyloid. It supports the native investigated-for-possible-treatment wording, not an approved indication or definitive efficacy claim. |
| adopted | Europe PMC official citation metadata and abstracts; 049-epmc.json: all ten adopted PMIDs resolve; nine abstracts inspected, PMID15651505 has none. | supports | PMID15074181 reports a retrospective D.fragilis pediatric treatment cohort including27 clioquinol recipients; this supports historical antiprotozoal use, not current general prescribing efficacy. PMID15651505 is a Dutch amoebiasis case report without an available abstract. PMID21080020 concerns solid-state structure. PMID16087879 concerns huntingtin cell/mouse models. PMID20651355,21426304 and21899946 concern cancer-cell pathways or comparisons with nitroxoline. PMID21199452 and21247386 are reviews, not primary experiments. PMID185949 concerns hydroxyquinolines/viral polymerase and cannot establish exact clioquinol antibacterial targets from its abstract. |
| antibacterial | PMID:29214226; DOI:10.1016/j.bbrep.2016.03.014; entire original article in049-2016.xml/txt; compound6, Methods2.1–2.2 and Table1. | supports | Commercial Sigma clioquinol6 was tested by agar dilution on Mueller-Hinton agar,37°C for24–48h, with0.5% DMSO control. Table1 gives26.19µM for S.aureus ATCC25923/29213 and E.coli ATCC25922; P.aeruginosa ATCC27853 and K.pneumoniae ATCC700603 are &gt;837.97µM. These exact-compound data support antibacterial activity without universal susceptibility. The paper’s background clinical assertions and hypotheses about uptake/chelation are not experimental target proof. |
| fungal2020 | PMID:32546212; DOI:10.1186/s12866-020-01850-3; entire article049-2020.html/txt, Results/Methods and Figures4–5 captions. | supports | C.albicans SC5314 had MIC1µg/mL and MFC3µg/mL; standard susceptibility uses MIC50 for clioquinol at30°C/48h. The separate metal assay uses24h MIC80, baseline2.5µM. Added Cu/Zn/Fe increased that endpoint while chelators lowered it; FeRhoNox measured reduced labile Fe2+. Membrane leakage was significant only at32µg/mL, depolarization from4µg/mL. Sorbitol and ergosterol tests gave no MIC increase. These conditional phenotypes support metal-homeostasis involvement, not direct binding to a bacterial protein. |
| fungal2019 | PMID:30662305; DOI:10.1016/j.jsps.2018.07.017; complete original XML/text049-fungal2019; Methods2.1–2.5, Results3.1–3.3. | supports | With different Candida isolates including ATCC18804 and dermatophytes, clioquinol increased MICs with sorbitol after seven days and showed no significant nucleic-acid leakage at its MIC. This conflicts with a universal cell-wall-negative conclusion from the2020 study; strains, doses, readouts and durations differ. No ergosterol-associated MIC shift was observed. The sulfonic-acid derivatives’ membrane results must not be transferred to clioquinol. |
| enzyme | DOI:10.2478/acph-2025-0018; Official original article https://hrcak.srce.hr/en/331554;049-2025.html/txt, MtMetAP1a methods and TableIV footnote. | supports | Clioquinol is a measured positive control: MtMetAP1a IC50 is11µM with Co2+ and101µM with Fe2+, while Mn2+/Ni2+ conditions give57%/50% residual activity at125µM. This supports biochemical inhibition with metal-specific conditions; it does not prove this enzyme alone mediates cellular growth inhibition. Most compound series, human MetAP2 and cathepsin experiments concern nitroxoline analogues. |
| primary-scope | PMID:29650464; PMID:39417316; Complete official abstracts049-additional-epmc.json. | context_only | The2018 study reports broad fungal but weak antibacterial activity of3% cream, emphasizing formulation/organism scope. The2024 Candida study reports RNA-seq and enzyme/membrane/apoptosis changes; decreased squalene-epoxidase activity is not by itself direct binding. These contexts can guide further curation without transferring effects to bacterial targets or inventing a public dataset accession. |
| adapter | https://imodulondb.org/api/datasets; Actual049-imodulondb-datasets.txt and049-imodulondb-methionine.txt. | context_only | Inventory has no human or fungal dataset. Covered m_tuberculosis/modulome exact enzyme search returns genes m_tuberculosis/modulome/Rv0734 mapA and m_tuberculosis/modulome/Rv2861c mapB, zero iModulons. This is gene-context confirmation, not clioquinol response, target engagement or a causal mechanism. With no component hit there is no summary to run. |
| search | CultureBotAI/AntibioticMech; 049-local-hits.txt,049-maintained-search.txt and049-focused-local-hits.txt; exact-name/identifier primary discovery. | context_only | The ignored-inclusive focused repository search found no matches in maintained curation/review/conf paths outside queue. Additional sources are bounded leads, not exhaustive global evidence. No producer, resistance or complete mechanism absence is inferred. |
| access | Free public retrieval routes; PMC11059541/PMC5038248; EuropePMC XML; publisher pages; FDA-hosted2018-paper PDF; LINCS/NIST endpoints. | context_only | 2016 antibacterial and2019 fungal XML and2020/2025 publisher texts were obtained. The2011 MetAP primary abstract is mainly about CLBQ14 and was treated as a further exact-CQ-table lead; full text was unavailable. The copper-scaffold paper was not used to assign its detailed8HQ mechanism to CQ. Paid registry/full-text access was not used. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity, definition, evidence, activity, mechanism and status rules; CURATION/HARMONIZATION. | supports | Optional omissions do not imply required-field failure. Evidence must remain compound/organism/assay specific; cellular responses or biochemical inhibition are not automatically whole-cell target validation. An exact spelling defect is minor, even if inherited from source. |
| validation | Coordinator documented focused validators; 049-focused-results.json,049-schema.log,049-strict.log/tsv,049-chemistry.json. | supports | Captured actual schema/strict/corrected-chemistry results are0. The helper’s initial failed mint attempt is separately retained. Shared corpus gate results are documented separately in the final bundle. |

## Limits And Additional Notes

- All ten adopted citation records were checked; nine abstracts were read, including two reviews. PMID15651505 has no available abstract. Their complete original reports were not all retrieved.
- Complete2016 antibacterial,2019 fungal and2020 fungal texts were read. The2025 article’s exact control assay and methods were inspected. The2011 MetAP and copper-scaffold full texts were inaccessible; detailed uninspected parent/analogue results are not adopted.
- The2018 cream and2024 Candida studies were inspected at official-abstract level; no exact strain details or RNA-seq accession is invented.
- NIST and LINCS access were unavailable; Reaxys was not independently inspected. DrugBank public identity fields were inspected without gated data. Patent OCR/historical naming is used for document-topic resolution, not decisive exact-structure evidence.
- The source typo is faithfully inherited, not an extractor failure. The bounded search and dataset inventory do not establish the absence of all additional mechanisms, resistance studies or evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T075738Z-5-chloro-7-iodoquinolin-8-ol
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Clioquinol: supported exact identity and activity, minor source spelling and
  scoped evidence follow-up'
started_at: '2026-10-21T07:36:23Z'
finished_at: '2026-10-21T07:57:38Z'
reviewer:
  identity: Codex review002 subagent with coordinator validation captures
  kind: agent
  independence: independent
  independence_basis: Neither reviewer authored the native record. Coordinator captured
    provenance before assessment and ran focused checks. Review002 read the entire
    native record/source row, maintained transforms, official identifiers, all ten
    adopted citation records with nine available abstracts, additional primary papers
    and the captured validator results.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: Exact clioquinol chemistry, broader parents, antimicrobial roles and source
  provenance are coherent. Current product information supports topical cream use;
  a primary pilot trial supports the qualified Alzheimer-investigation statement.
  One minor spelling error is inherited from ChEBI, and one informational opportunity
  concerns scoped assay/mechanism evidence. Primary bacterial, fungal, host and analogue
  contexts must remain distinct. Focused schema, strict and corrected independent
  chemistry checks pass. Scientific assessment retains the stated evidence limits;
  full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/5-chloro-7-iodoquinolin-8-ol.yaml
    sha256: 18887f77a26548822defcee1cc7c5662ac5b330a4f76fa645be4adb7cf2a4a2b
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
- target_id: CHEBI:74460
  path: data/antibiotics/antibacterial/5-chloro-7-iodoquinolin-8-ol.yaml
  label: 5-chloro-7-iodoquinolin-8-ol
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
  description: Entire exact native record, all asserted identifiers and definition
    claims, maintained inputs, all adopted citation records, and bounded additional
    activity/mechanism research.
  selection: Queue index049, CHEBI:74460 at its locked native path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:74460
  exclusions:
  - target: Nitroxoline, cloxyquin, CLBQ14, other hydroxyquinolines and their isolated
      metal complexes
    reason: Distinct structures; their activity, targets or clinical status are not
      transferred to clioquinol.
checks:
- check_id: schema
  name: Focused LinkML validation
  status: passed
  required: true
  summary: Coordinator command exited0 with no issues.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/5-chloro-7-iodoquinolin-8-ol.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict validation
  status: passed
  required: true
  summary: Coordinator scanned one file; zero ERROR rows.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/5-chloro-7-iodoquinolin-8-ol.yaml --out /private/tmp/am-review-session/049-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry-initial
  name: Initial independent chemistry helper
  status: failed
  required: false
  summary: The initial helper incorrectly calculated the source mint with SHA1. Structures,
    formula, masses and charge passed; the helper defect produced mint_matches:false.
    Original output is retained. This was not a native-record failure. The original
    exit code is not retained in the supplied capture.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - chemistry-initial
- check_id: chemistry
  name: Corrected independent chemistry helper
  status: passed
  required: false
  summary: After aligning mint calculation with repository SHA256 of CHEBI|source_id,
    all checks passed without changing the native record.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - chemistry
  command: .venv/bin/python /private/tmp/am-review-session/chem005.py 49
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-inventory
  name: Structured dataset inventory
  status: passed
  required: false
  summary: Inventory retrieved; human, Candida and Saccharomyces contexts are not
    covered. M.tuberculosis/modulome is covered.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-search
  name: Covered bacterial enzyme context
  status: passed
  required: false
  summary: Exact methionine-aminopeptidase search returned mapA/Rv0734 and mapB/Rv2861c
    genes and zero iModulons. No component summary applies.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 search --organism m_tuberculosis --dataset
    modulome --query 'methionine aminopeptidase'
  exit_code: 0
  expected_exit_code: 0
- check_id: registry-limits
  name: Independent registry and LINCS access
  status: unavailable
  required: false
  summary: NIST/CAS endpoint and LINCS routes were inaccessible; Reaxys was not independently
    inspected. CAS is corroborated by multiple official chemical/drug records; LINCS
    and Reaxys remain ChEBI-source assertions.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - identity
  - xrefs
- check_id: literature-limits
  name: Additional full-text access
  status: unavailable
  required: false
  summary: One adopted citation has no abstract. Most adopted host papers were checked
    at abstract level. The 2011 MetAP and copper-context full texts were blocked by
    PMC/EuropePMC routes; the 2018 cream-study PDF was403. These limits do not erase
    the inspected primary assay evidence.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - adopted
  - primary-scope
  - access
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:74460
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
  - CHEBI:74460
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
  - CHEBI:74460
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
  - CHEBI:74460
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
  - CHEBI:74460
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
  - CHEBI:74460
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
  - CHEBI:74460
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
  - CHEBI:74460
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
  - CHEBI:74460
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/5-chloro-7-iodoquinolin-8-ol.yaml
  locator: 'Entire YAML: definition, 12 synonyms, three chemical parents, four roles,
    structure, ten xrefs across three groups, source concept and four history events.'
  accessed_at: '2026-10-21T07:56:47Z'
  support: supports
  summary: The exact neutral achiral entity is clioquinol. Definition states antibacterial/antifungal
    properties, topical cream use and investigation as a Cu/Zn chelator for possible
    Alzheimer treatment. It does not claim approved Alzheimer therapy. Optional quantitative
    activity, molecular targets, causal graphs, resistance, producer and clinical
    objects are not present. The definition contains the word atifungal.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: CHEBI:74460 row1891; complete 049-raw.json; raw MANIFEST/PATHS; conf/sources.yaml;
    extract_chebi and build_record.
  accessed_at: '2026-10-21T07:56:47Z'
  support: supports
  summary: The source row matches the native record, including the spelling error.
    Extraction carries the source definition; build_record selects the ChEBI definition.
    Ten source citations are leads intentionally not automatically assigned claim-level
    evidence. Mechanism roles are empty. Four seed/reseed events and source version2026-08-30
    are coherent; all13 initial hashes remain unchanged.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:74460
  locator: Complete current ChEBI page 049-chebi.html and049-chebi.txt; PubChem CID2788
    049-pubchem.json and049-pubchem-synonyms.json.
  accessed_at: '2026-10-21T07:56:47Z'
  support: supports
  summary: ChEBI, PubChem and native chemistry agree on C9H5ClINO, neutral charge,
    mass305.502, exact mass304.91044, full InChI and QCDFBFJGMNKBDO-UHFFFAOYSA-N.
    All12 native synonym strings are corroborated by the source and PubChem synonyms;
    INN labels are ChEBI assertions, with clioquinol also labeled INN by KEGG. Parents36683
    organochlorine,37142 organoiodine and38775 monohydroxyquinoline fit. Roles33281
    antimicrobial,33282 antibacterial,35718 antifungal and35820 antiprotozoal drug
    are correctly separated from parent classes. CAS130-26-7 is corroborated; NIST
    inspection was unavailable.
- evidence_id: xrefs
  kind: database
  reference: https://www.rcsb.org/ligand/CQL
  locator: Official CQL ligand page; https://drugcentral.org/drugcard/681 and049-drugcentral-inchi.txt/049-drugcentral-smiles.txt;
    https://www.kegg.jp/entry/D03538; https://go.drugbank.com/drugs/DB04815; current
    ChEBI xrefs.
  accessed_at: '2026-10-21T07:56:47Z'
  support: supports
  summary: RCSB CQL has the exact native SMILES/InChI/key. DrugCentral681 returns
    the same full InChI and corresponding SMILES. KEGG D03538 resolves to clioquinol
    with matching formula/CAS and INN label. DrugBank DB04815 public page resolves
    to clioquinol with formula, aliases and topical description; no gated target data
    were inspected. LINCS LSM-2186 and Reaxys153637 are present in ChEBI but independent
    endpoints were unavailable or uninspected.
- evidence_id: documents
  kind: primary_source
  reference: https://patents.google.com/patent/US641491A/en
  locator: US641491A description/claim; DE117767C description at https://patents.google.com/patent/DE117767C/en.
  accessed_at: '2026-10-21T07:56:47Z'
  support: context_only
  summary: Both document identifiers resolve to historical iodochloroxyquinolin preparation
    texts. US claim describes iodination of5-chloro-8-oxyquinoline; DE text retains
    uncertainty in iodine positional assignment. These are related historical documents,
    not modern proof of exact regioisomer identity, potency, safety or current clinical
    authorization. Automated patent chemical-entity links were not treated as structure
    evidence.
- evidence_id: wiki
  kind: database
  reference: https://en.wikipedia.org/wiki/Clioquinol
  locator: Document cross-reference identity section only.
  accessed_at: '2026-10-21T07:56:47Z'
  support: context_only
  summary: The page resolves to clioquinol and displays the same full InChI/key. It
    is used to verify the document link only; mechanistic, regulatory and clinical
    claims were assessed against primary or official sources.
- evidence_id: chemistry-initial
  kind: validation
  reference: Coordinator initial helper result
  locator: 049-initial-chemistry.json and049-initial-chemistry.log.
  accessed_at: '2026-10-21T07:56:47Z'
  support: context_only
  summary: The earlier helper output has matching native SMILES/InChI structures but
    a wrong SHA1-derived mint. The review preserves this actual failed helper attempt
    and subsequent correction.
  snapshot_sha256: 0bb10956388907a213843e5c90af514fa10b52302bcdb2493d4a1db1fe1bf86f
- evidence_id: chemistry
  kind: validation
  reference: Coordinator corrected RDKit calculation
  locator: 049-focused-results.json;049-chemistry.json/log; inspected current chem005.py.
  accessed_at: '2026-10-21T07:56:47Z'
  support: supports
  summary: Both structures parse to the same neutral single fragment with no tetrahedral
    centers, formulaC9H5ClINO, mass305.502 and exact mass304.91043946. Full key and
    repository SHA256 mint antibioticmech:chebi-781dacc9d8 match. Final helper exited0.
  snapshot_sha256: aaf4368137454efc71734a7f48e94298ff7b2d7582591bb15bb4a33209c3f6ec
- evidence_id: topical
  kind: authority
  reference: https://www.medicines.org.uk/emc/product/12911/smpc
  locator: Current Chemidex Betamethasone valerate/Clioquinol cream SmPC, revised2025-10-16;
    sections2,4.1,4.3,5.1.
  accessed_at: '2026-10-21T07:56:47Z'
  support: supports
  summary: The marketed combination contains30mg/g clioquinol and identifies its antibacterial
    and anticandidal actions. Indications concern inflammatory skin conditions with
    secondary infection present, suspected or likely. This supports use in creams;
    it does not justify universal skin-infection treatment or transferring the corticosteroid’s
    effects to clioquinol.
- evidence_id: alzheimer
  kind: primary_source
  reference: PMID:14676042
  locator: DOI:10.1001/archneur.60.12.1685; complete official abstract in049-additional-epmc.json.
  accessed_at: '2026-10-21T07:56:47Z'
  support: supports
  summary: A36-person randomized pilot phase2 study explicitly investigated clioquinol
    as a metal-protein-attenuating compound involving Cu/Zn and amyloid. It supports
    the native investigated-for-possible-treatment wording, not an approved indication
    or definitive efficacy claim.
- evidence_id: adopted
  kind: database
  reference: Europe PMC official citation metadata and abstracts
  locator: '049-epmc.json: all ten adopted PMIDs resolve; nine abstracts inspected,
    PMID15651505 has none.'
  accessed_at: '2026-10-21T07:56:47Z'
  support: supports
  summary: PMID15074181 reports a retrospective D.fragilis pediatric treatment cohort
    including27 clioquinol recipients; this supports historical antiprotozoal use,
    not current general prescribing efficacy. PMID15651505 is a Dutch amoebiasis case
    report without an available abstract. PMID21080020 concerns solid-state structure.
    PMID16087879 concerns huntingtin cell/mouse models. PMID20651355,21426304 and21899946
    concern cancer-cell pathways or comparisons with nitroxoline. PMID21199452 and21247386
    are reviews, not primary experiments. PMID185949 concerns hydroxyquinolines/viral
    polymerase and cannot establish exact clioquinol antibacterial targets from its
    abstract.
  snapshot_sha256: 6b75fe33cca18dd81e97844be4e8e48ec9272942971822ee8faed192965eb9d7
- evidence_id: antibacterial
  kind: primary_source
  reference: PMID:29214226
  locator: DOI:10.1016/j.bbrep.2016.03.014; entire original article in049-2016.xml/txt;
    compound6, Methods2.1–2.2 and Table1.
  accessed_at: '2026-10-21T07:56:47Z'
  support: supports
  summary: Commercial Sigma clioquinol6 was tested by agar dilution on Mueller-Hinton
    agar,37°C for24–48h, with0.5% DMSO control. Table1 gives26.19µM for S.aureus ATCC25923/29213
    and E.coli ATCC25922; P.aeruginosa ATCC27853 and K.pneumoniae ATCC700603 are >837.97µM.
    These exact-compound data support antibacterial activity without universal susceptibility.
    The paper’s background clinical assertions and hypotheses about uptake/chelation
    are not experimental target proof.
  snapshot_sha256: 2cfdd4c7f39f9b9ce02c400ee71452f1ec32391c8be10eed9c687221a260a451
- evidence_id: fungal2020
  kind: primary_source
  reference: PMID:32546212
  locator: DOI:10.1186/s12866-020-01850-3; entire article049-2020.html/txt, Results/Methods
    and Figures4–5 captions.
  accessed_at: '2026-10-21T07:56:47Z'
  support: supports
  summary: C.albicans SC5314 had MIC1µg/mL and MFC3µg/mL; standard susceptibility
    uses MIC50 for clioquinol at30°C/48h. The separate metal assay uses24h MIC80,
    baseline2.5µM. Added Cu/Zn/Fe increased that endpoint while chelators lowered
    it; FeRhoNox measured reduced labile Fe2+. Membrane leakage was significant only
    at32µg/mL, depolarization from4µg/mL. Sorbitol and ergosterol tests gave no MIC
    increase. These conditional phenotypes support metal-homeostasis involvement,
    not direct binding to a bacterial protein.
  snapshot_sha256: 21f03aca365fc466572a4f4225cd09be4073a4da670ed1b640ec8b1f4515e7ab
- evidence_id: fungal2019
  kind: primary_source
  reference: PMID:30662305
  locator: DOI:10.1016/j.jsps.2018.07.017; complete original XML/text049-fungal2019;
    Methods2.1–2.5, Results3.1–3.3.
  accessed_at: '2026-10-21T07:56:47Z'
  support: supports
  summary: With different Candida isolates including ATCC18804 and dermatophytes,
    clioquinol increased MICs with sorbitol after seven days and showed no significant
    nucleic-acid leakage at its MIC. This conflicts with a universal cell-wall-negative
    conclusion from the2020 study; strains, doses, readouts and durations differ.
    No ergosterol-associated MIC shift was observed. The sulfonic-acid derivatives’
    membrane results must not be transferred to clioquinol.
  snapshot_sha256: fc99ec935c462a7d68a0cdda71b20997651ad29d13c05ba7a53048ab4db1645c
- evidence_id: enzyme
  kind: primary_source
  reference: DOI:10.2478/acph-2025-0018
  locator: Official original article https://hrcak.srce.hr/en/331554;049-2025.html/txt,
    MtMetAP1a methods and TableIV footnote.
  accessed_at: '2026-10-21T07:56:47Z'
  support: supports
  summary: 'Clioquinol is a measured positive control: MtMetAP1a IC50 is11µM with
    Co2+ and101µM with Fe2+, while Mn2+/Ni2+ conditions give57%/50% residual activity
    at125µM. This supports biochemical inhibition with metal-specific conditions;
    it does not prove this enzyme alone mediates cellular growth inhibition. Most
    compound series, human MetAP2 and cathepsin experiments concern nitroxoline analogues.'
  snapshot_sha256: 8adfda0beb63d7fa0184a50b52c2072dc8824b9206f1b7f50355c0e1a4f198be
- evidence_id: primary-scope
  kind: primary_source
  reference: PMID:29650464; PMID:39417316
  locator: Complete official abstracts049-additional-epmc.json.
  accessed_at: '2026-10-21T07:56:47Z'
  support: context_only
  summary: The2018 study reports broad fungal but weak antibacterial activity of3%
    cream, emphasizing formulation/organism scope. The2024 Candida study reports RNA-seq
    and enzyme/membrane/apoptosis changes; decreased squalene-epoxidase activity is
    not by itself direct binding. These contexts can guide further curation without
    transferring effects to bacterial targets or inventing a public dataset accession.
  snapshot_sha256: 0083cb280cf996304d0cd0f0a3f52c0e7947bb6af06495b5e881a1ed53a7ff29
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Actual049-imodulondb-datasets.txt and049-imodulondb-methionine.txt.
  accessed_at: '2026-10-21T07:56:47Z'
  support: context_only
  summary: Inventory has no human or fungal dataset. Covered m_tuberculosis/modulome
    exact enzyme search returns genes m_tuberculosis/modulome/Rv0734 mapA and m_tuberculosis/modulome/Rv2861c
    mapB, zero iModulons. This is gene-context confirmation, not clioquinol response,
    target engagement or a causal mechanism. With no component hit there is no summary
    to run.
  snapshot_sha256: 4bd081f59f8a229b90d3d37f46782715c0d717af46cd2ff4e484045e189d520d
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 049-local-hits.txt,049-maintained-search.txt and049-focused-local-hits.txt;
    exact-name/identifier primary discovery.
  accessed_at: '2026-10-21T07:56:47Z'
  support: context_only
  summary: The ignored-inclusive focused repository search found no matches in maintained
    curation/review/conf paths outside queue. Additional sources are bounded leads,
    not exhaustive global evidence. No producer, resistance or complete mechanism
    absence is inferred.
  search_scope: rg --no-ignore --hidden identifier,label,slug across worktree005 excluding.git/.venv;
    focused CHEBI:74460,QCDFBFJGMNKBDO,5-chloro-7-iodoquinolin-8-ol,clioquinol across
    curation,reviews,reports/yaml_record_review,conf excluding record_review_queue.tsv.
    Ignored files included. Free exact-name/CAS, antibacterial, antifungal, metal/MetAP
    and clinical-source searches.
- evidence_id: access
  kind: search
  reference: Free public retrieval routes
  locator: PMC11059541/PMC5038248; EuropePMC XML; publisher pages; FDA-hosted2018-paper
    PDF; LINCS/NIST endpoints.
  accessed_at: '2026-10-21T07:56:47Z'
  support: context_only
  summary: 2016 antibacterial and2019 fungal XML and2020/2025 publisher texts were
    obtained. The2011 MetAP primary abstract is mainly about CLBQ14 and was treated
    as a further exact-CQ-table lead; full text was unavailable. The copper-scaffold
    paper was not used to assign its detailed8HQ mechanism to CQ. Paid registry/full-text
    access was not used.
  search_scope: Official Europe PMC/PubMed, PMC and original publisher routes for
    inspected DOI/PMID sources; free original-paper reproduction in an FDA docket;
    official drug/structure endpoints and linked LINCS routes. Full-text failures
    were500,403 or browser challenges; no paywall circumvention or paid credits.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity, definition, evidence, activity, mechanism and status rules; CURATION/HARMONIZATION.
  accessed_at: '2026-10-21T07:56:47Z'
  support: supports
  summary: Optional omissions do not imply required-field failure. Evidence must remain
    compound/organism/assay specific; cellular responses or biochemical inhibition
    are not automatically whole-cell target validation. An exact spelling defect is
    minor, even if inherited from source.
- evidence_id: validation
  kind: validation
  reference: Coordinator documented focused validators
  locator: 049-focused-results.json,049-schema.log,049-strict.log/tsv,049-chemistry.json.
  accessed_at: '2026-10-21T07:56:47Z'
  support: supports
  summary: Captured actual schema/strict/corrected-chemistry results are0. The helper’s
    initial failed mint attempt is separately retained. Shared corpus gate results
    are documented separately in the final bundle.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact clioquinol identity
  outcome: supported
  summary: Official identity records, all native synonyms and independently calculated
    chemistry agree. Sibling hydroxyquinolines and metal complexes remain separate.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - record
  - identity
  - xrefs
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Broader parents and activity roles
  outcome: supported
  summary: Chemical parents fit and independent primary/official evidence supports
    antibacterial, antifungal and historical antiprotozoal roles. ANTIBACTERIAL class
    is compatible with additional activity roles.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - identity
  - antibacterial
  - fungal2020
  - adopted
  - topical
- assessment_id: xref
  area: grounding
  topic: All cross-reference groups
  outcome: supported
  summary: Drug/ligand/document identifiers resolve with noted LINCS/Reaxys/NIST limits.
    Patent topic links are not asserted as modern structure or efficacy proof.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - xrefs
  - identity
  - documents
  - wiki
- assessment_id: definition
  area: evidence
  topic: Topical use and Alzheimer investigation
  outcome: supported
  summary: Current product information and a primary pilot trial support the qualified
    definition. No universal approval or efficacy is implied.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - topical
  - alzheimer
  - record
- assessment_id: spelling
  area: representation
  topic: Inherited definition spelling
  outcome: concern
  summary: The word atifungal is a confirmed spelling error reproduced from the source;
    it does not change identity or the otherwise supported activity claim.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - record
  - owner
  - identity
- assessment_id: mechanism
  area: evidence
  topic: Mechanism completeness and scope
  outcome: supported
  summary: There are primary biochemical and fungal phenotype observations suitable
    for qualified enrichment. Their absence is optional; host pathways, analogue data
    and disputed cell-wall effects require explicit separation.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - enzyme
  - fungal2020
  - fungal2019
  - adopted
  - adapter
  - primary-scope
- assessment_id: other
  area: representation
  topic: Producer, resistance and graph fields
  outcome: not_applicable
  summary: No native objects require correction. No biological producer, clinical
    efficacy or universal resistance mechanism follows from these observations.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - record
  - rubric
- assessment_id: completeness
  area: completeness
  topic: Claim-level evidence and assay objects
  outcome: supported
  summary: The seed can be enriched using exact primary data with endpoint, species,
    formulation and metal-condition qualifiers. This is not a schema defect.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - record
  - antibacterial
  - fungal2020
  - enzyme
  - primary-scope
  - rubric
- assessment_id: provenance
  area: ownership
  topic: Maintained source/status
  outcome: supported
  summary: The record reproduces its maintained source and current ChEBI definition.
    Scientific additions belong to the native record; inherited definition correction
    belongs to the source path. All13 capture hashes remain unchanged.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - owner
  - record
  - rubric
- assessment_id: schema
  area: schema
  topic: Focused checks
  outcome: supported
  summary: Focused schema and strict pass; corrected chemistry passes. The initial
    helper defect is documented separately.
  target_ids:
  - CHEBI:74460
  evidence_ids:
  - validation
  - chemistry
  - chemistry-initial
findings:
- finding_id: F1
  issue_key: chebi-74460-source-definition-atifungal-typo
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the inherited spelling atifungal
  description: Native definition and maintained/current ChEBI source all contain atifungal
    where antifungal is intended. This is a presentation defect, not an unsupported
    antifungal claim or extraction mismatch.
  target_ids:
  - CHEBI:74460
  field_paths:
  - definition
  evidence_ids:
  - record
  - owner
  - identity
  - topical
  - rubric
  rule_id: 'native-review-checklist: Definition'
  native_severity: minor wording defect
  normalization_reason: A confirmed spelling error does not alter molecular identity
    or biological scope.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI definition; update through an authorized source refresh, not
      a generated-record-only patch
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source definition extraction and any reviewed source-specific normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition selection and reproducible seeding
- finding_id: F2
  issue_key: chebi-74460-qualified-primary-activity-mechanism-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Represent optional primary assay and mechanism evidence with scope qualifiers
  description: Exact compound primary observations are available but absent from optional
    activity/evidence/target fields. They support bounded enrichment; conflicting
    fungal outcomes, biochemical versus cellular evidence, and formulation effects
    prevent a single universal mechanism claim.
  target_ids:
  - CHEBI:74460
  field_paths:
  - evidence
  - activity_spectrum
  - molecular_targets
  - mode_of_action_notes
  evidence_ids:
  - record
  - antibacterial
  - fungal2020
  - fungal2019
  - enzyme
  - primary-scope
  - rubric
  rule_id: 'native-review-checklist: Activity, Mechanism and Evidence'
  native_severity: informational optional enrichment
  normalization_reason: No current false target/MIC statement or missing required
    representation exists.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/5-chloro-7-iodoquinolin-8-ol.yaml
    role: Curator-owned scientific additions through write_validated_antibiotic and
      native curation history
actions:
- action_id: A1
  description: Correct atifungal to antifungal through a reviewed source correction
    or source-specific normalization that remains reproducible on reseeding.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:74460
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI definition; update through an authorized source refresh, not
      a generated-record-only patch
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source definition extraction and any reviewed source-specific normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition selection and reproducible seeding
  acceptance_checks:
  - Keep the ChEBI origin and source-version provenance truthful; do not silently
    patch only the generated record.
  - If extraction behavior changes, regenerate the maintained inventory/manifest through
    the authorized source workflow and reseed; inspect the exact definition diff.
  - Rerun focused schema/strict and required corpus gates after the separately authorized
    correction.
- action_id: A2
  description: If selected for scientific curation, add claim-level primary evidence
    and qualified assay/target observations to the exact native record.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:74460
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/5-chloro-7-iodoquinolin-8-ol.yaml
    role: Curator-owned scientific additions through write_validated_antibiotic and
      native curation history
  acceptance_checks:
  - Preserve agar versus broth assays, MIC50 versus MIC80 versus MFC, strain, duration,
    units, formulation and metal concentrations; do not replace > endpoints with equalities.
  - Keep measured enzyme inhibition distinct from validated cellular target engagement;
    verify exact isoform/protein grounding and evidence before adding targets.
  - Preserve the2019/2020 fungal cell-wall disagreement and dose-dependent membrane
    results rather than generalizing to every organism.
  - Do not transfer host cancer/neuro signaling, nitroxoline/CLBQ14 mechanisms or
    claimed clinical approvals from background text.
  - Use write_validated_antibiotic and native history; rerun focused and required
    corpus gates without automatic status promotion.
limitations:
- All ten adopted citation records were checked; nine abstracts were read, including
  two reviews. PMID15651505 has no available abstract. Their complete original reports
  were not all retrieved.
- Complete2016 antibacterial,2019 fungal and2020 fungal texts were read. The2025 article’s
  exact control assay and methods were inspected. The2011 MetAP and copper-scaffold
  full texts were inaccessible; detailed uninspected parent/analogue results are not
  adopted.
- The2018 cream and2024 Candida studies were inspected at official-abstract level;
  no exact strain details or RNA-seq accession is invented.
- NIST and LINCS access were unavailable; Reaxys was not independently inspected.
  DrugBank public identity fields were inspected without gated data. Patent OCR/historical
  naming is used for document-topic resolution, not decisive exact-structure evidence.
- The source typo is faithfully inherited, not an extractor failure. The bounded search
  and dataset inventory do not establish the absence of all additional mechanisms,
  resistance studies or evidence.
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
