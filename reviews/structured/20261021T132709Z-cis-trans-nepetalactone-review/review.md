# cis-trans-Nepetalactone: coherent exact isomer and purified-material antimicrobial evidence

- Review: 20261021T132709Z-cis-trans-nepetalactone-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T13:04:58Z
- Finished UTC: 2026-10-21T13:27:09Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No required native correction identified. The exact (4aS,7S,7aR) structure agrees with current official encodings and primary structure figures. A later original study tests purified cis,trans-nepetalactone against bacteria and fungi. All ten adopted citation leads were resolved with explicit distinctions among purified isomer, essential oil, behavioral endpoints and plant biosynthesis. MetaCyc access and some inherited non-antimicrobial claims remain limited. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 305; one exact record. All 13 initial input hashes were preserved, and all 21 expanded input hashes were rechecked.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:7518 | data/antibiotics/antibacterial/cis-trans-nepetalactone.yaml | generated | cis-trans-nepetalactone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:7518 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:7518 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:7518 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:7518 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:7518 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:7518 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:7518 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:7518 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:7518 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:7518 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:7518 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:7518 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Absolute isomer, formula, charge and mass

identity: supported. Targets: CHEBI:7518.

Native graph, current ChEBI, KEGG, LipidMaps and original stereochemical figures consistently identify (4aS,7S,7aR)-nepetalactone. Other stereoisomers and mixed oils remain separate.

### Asserted chemical and document references

grounding: supported. Targets: CHEBI:7518.

KEGG, LipidMaps and KNApSAcK structural encodings agree with the native identity, and CAS is corroborated. The KNApSAcK displayed-key inconsistency is upstream and does not invalidate its matching graph. Wikipedia is correctly treated as a broad document reference.

### MetaCyc CPD-15029 independent verification

grounding: unknown. Targets: CHEBI:7518.

The asserted identifier remains source-backed but independently unresolved because the direct route required account access. No contrary exact mapping was established.

### Chemical classes and antibacterial/antifungal roles

evidence: supported. Targets: CHEBI:7518.

The graph fits both chemical parents. Published purified cis,trans material and Table 2 support antimicrobial roles independently of extract-only adopted evidence. Assay scope and published structural characterization remain explicit.

### All ten inherited PMID leads

evidence: supported. Targets: CHEBI:7518.

Each lead was resolved and its evidence type bounded. The set includes isolation, ecological behavior, metabolism, an extract study, biosynthesis originals and a minireview; they are not interchangeable antibacterial mechanism evidence.

### Analgesic, aphid pheromone and cat-attractant breadth

evidence: unknown. Targets: CHEBI:7518.

The inherited qualitative claims have relevant original leads, but accessible analgesia evidence concerns essential oil and ecological/metabolic abstracts do not independently resolve every exact-isomer behavioral claim. This bounded reading does not establish those claims false.

### Optional activity_spectrum enrichment

completeness: unknown. Targets: CHEBI:7518.

The 2021 purified-material table is a useful optional quantitative lead. Any future curation should retain exact material, strain, mg/mL units, endpoint and method limits, and resolve the fungal name conflicts. Missing optional activity objects are not a defect.

### Optional producer and mechanism evidence

completeness: unknown. Targets: CHEBI:7518.

Primary isolation supports bounded Nepeta producer context, with cultivar/isomer variation. ISY/NEPS are biosynthetic proteins and host macrophage responses are not antibacterial direct targets. No unsupported mechanism or causal graph should be inferred from these sources.

### Unpopulated resistance, clinical and dataset assertions

scope: not_applicable. Targets: CHEBI:7518.

There are no native assertions in these domains. A strain resistant to other drugs does not itself establish resistance to this compound.

### Imported ownership, EXACT/SEEDED status and four history events

provenance: supported. Targets: CHEBI:7518.

The exact ChEBI row and transform explain native content and history. All original hashes were preserved. This review does not promote the native scientific curation status.

### Focused deterministic checks

schema: supported. Targets: CHEBI:7518.

Native schema, strict validation and molecular consistency pass; scientific interpretation remains separately bounded.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally enrich exact-isomer activity and producer context from the inspected original sources.

- Retain the 2021 isolated cis,trans material and original Table 2 column, units, strain mappings and method limits.
- Keep extracts, trans,cis material, combinations and host-cell endpoints separate.
- Resolve fungal table/method naming conflicts before quantitative fungal strain export.
- Do not convert plant biosynthetic enzymes into antibacterial targets; run applicable native gates after separately authorized curation.

### A2

Resolve inaccessible legacy mapping and ancillary definition details only when those fields are revised or enriched.

- Verify MetaCyc CPD-15029 directly before claiming independent confirmation or removal.
- Preserve the KNApSAcK encoding/display distinction; its matching molecular graph does not warrant automatic removal.
- Use original isolated-material evidence before asserting a direct analgesic receptor or quantified exact-isomer behavioral effect.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cis-trans-nepetalactone.yaml; Entire 88-line YAML: all chemical fields, nine synonyms, parents, roles, six references, source concept and four history events | supports | The record is an EXACT, SEEDED antibacterial entry for CHEBI:7518. Definition, chemical classes, antibacterial/antifungal roles and imported references were read in full. No quantitative activity_spectrum, molecular target, resistance determinant, producer object, clinical assertion, dataset assertion or causal graph is populated. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/chebi_role_names.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact raw ChEBI row 241 and source/extraction ownership | supports | The source row reproduces the native chemical identity, definition, nine retained synonyms, parents, roles and chemical/document references, and supplies ten adopted PMID leads. Source extraction and seeding own the imported fields. No target-specific curator or decision override was found in the ignored-inclusive focused search. All 13 initial and 21 expanded hashes remain unchanged. |
| rubric | .claude/skills/review-yaml-record/SKILL.md; docs/record-review-profile.md; .claude/skills/curate-yaml-record/references/review-checklist.md; Identity, evidence scope, source ownership and optional completeness rubric | supports | Optional mechanistic, quantitative activity and producer objects require defensible source mapping; their absence is not itself a native schema or scientific defect. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/7518/; Complete current CHEBI:7518 compound record | supports | The current definition, absolute (4aS,7S,7aR) names, neutral C10H14O2 formula and full key ZDKZHVNKFOXMND-NBEYISGCSA-N agree with the native structure. The source itself includes additional biological roles and producer references, which are not silently imported as native assertions. |
| terms | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms; 305-term-38606.json, 305-term-50563.json, 305-term-33282.json and 305-term-35718.json | supports | All four asserted terms resolve: cyclopentapyran, iridoid monoterpenoid, antibacterial agent and antifungal agent. Chemical classes fit the molecular graph; biological roles are separately assessed from original assay material. |
| chemistry | Independent RDKit and source identifier calculation; 305-chemistry.json; 305306-xref-chemistry.json; 305306-final-audit.json, target 305 | supports | Native SMILES and InChI give one neutral component, all three stereocentres assigned, the full stored key, C10H14O2 and consistent masses. The source mint antibioticmech:chebi-9e73b2a41d recomputes correctly. Current ChEBI, KEGG and LipidMaps structures and the independent PubChem CID 161367 comparator generate the same full key. |
| kegg-lipids | https://rest.kegg.jp/get/C09791; KEGG C09791 text and molfile; LipidMaps LMPR0102070013 JSON; independent full-graph calculation | supports | KEGG C09791 and LipidMaps LMPR0102070013 identify the intended cis-trans form with the same complete absolute structure. KEGG molfile coordinates and stereochemical bonds preserve all three stereocentres. CAS 21651-62-7 is corroborated by these exact-compound entries and ChEBI. |
| knapsack | https://www.knapsackfamily.com/knapsack_core/information.php?word=C00003091; C00003091 names, CAS, formula, InChI, SMILES and displayed key | supports | KNApSAcK names cis-trans-nepetalactone and supplies CAS 21651-62-7. Its displayed key ZDKZHVNKFOXMND-KKRMJURBNA-N differs from the native standard key, but its actual standard InChI and stereochemical SMILES independently generate ZDKZHVNKFOXMND-NBEYISGCSA-N. This is an upstream representation inconsistency, not evidence of a different native molecule or a required xref removal. |
| xref-audit | Current official structural encodings; 305306-final-audit.json, target 305 only | supports | Independent parsing confirms both ChEBI encodings and both KNApSAcK encodings match the native graph. The KNApSAcK displayed-key discrepancy is explicitly retained instead of being silently described as exact string agreement. |
| legacy-document | https://metacyc.org/compound?orgid=META&amp;id=CPD-15029; MetaCyc CPD-15029 access result; 305-wiki.html topic page | context_only | The direct MetaCyc route leads to account-required content, so its exact molecular mapping remains independently unresolved. The Wikipedia reference resolves to the broader nepetalactone topic; it is a document link, not primary evidence or an assertion that every stereoisomer is equivalent. |
| adopted-isolation | https://doi.org/10.1021/np049647d; PMID:15974613, complete original abstract; official ACS supporting-file metadata | partial | The 2005 isolation/interconversion paper describes Nepeta racemosa/mussinii and faassenii material, several nepetalactone/nepetalactol diastereomers, NMR and calculated conformational properties. It supports chemical/isolation context, not an antibacterial endpoint. Publisher full text was inaccessible; eight official legacy .chm supplement entries were discovered but not decoded or executed. No exact numerical result is assigned from them. |
| adopted-aphid | https://doi.org/10.1016/j.chroma.2007.12.020; PMID:18166192, complete original abstract | partial | The 2008 SPME-GC/MS study detects cis-trans-nepetalactone and nepetalactol associated with Cinara pilicornis on spruce and interprets them as likely pheromone components. It is analytical and ecological evidence, not an antibacterial assay; the abstract does not independently establish absolute hand or a purified-isomer mating-response experiment. |
| adopted-extract | https://doi.org/10.1016/j.fitote.2010.03.007; PMID:20307630, complete original abstract | context_only | The 2010 shoot-culture study assigns cis-trans-nepetalactone to N. sibirica and trans-cis to N. rtanjensis, but tests methanolic plant extracts for antimicrobial activity. These mixed-material endpoints are not purified native-isomer MICs. Publisher retrieval failed, so no uninspected table or strain values are transferred. |
| adopted-behavior | https://doi.org/10.1016/j.phytochem.2010.09.016; https://doi.org/10.1007/s10886-015-0585-7; PMID:21056438 and PMID:25956798, complete original abstracts | context_only | The 2011 study separately considers named (4aS,7S,7aR) and (4aS,7S,7aS) nepetalactones and mixtures in mosquito, tick and mite repellence. The 2015 study tests the native absolute isomer and nepetalactol in lacewing trap responses. These are behavioral endpoints and mixtures require separate attribution; neither paper establishes bacterial killing. |
| adopted-metabolism | https://doi.org/10.1126/science.164.3885.1281; PMID:5770619, complete original abstract | partial | The 1969 paper follows radiolabeled cis-trans-nepetalactone metabolism in cats, including excretion products. The inspected abstract is not a new quantified attraction assay and supplies no antibacterial mechanism. The cat-attractant description is inherited context; its complete behavioral proof was not independently reconstructed here. |
| adopted-analgesia | https://doi.org/10.1111/j.2042-7158.1998.tb07145.x; PMID:9720633, complete original abstract | partial | The analgesia paper screens N. caesarea essential oil whose major component is assigned as 4a-alpha,7-alpha,7a-alpha-nepetalactone. Naloxone-sensitive effects are attributed to the dominant constituent by the authors. The accessible abstract does not establish isolated exact-isomer dosing or direct opioid-receptor binding. Its inference is not upgraded to a purified-compound target assertion. |
| adopted-2018 | https://doi.org/10.1016/j.phytochem.2017.10.004; PMID:29091815 / PMC5739345; full body and Methods; Figure 1 visually inspected | supports | The original study identifies natural cis-trans-nepetalactone as (4aS,7S,7aR), with species/cultivar-dependent isomer distributions. Methods isolate an authentic cis-trans standard from N. faassenii Six Hills Giant and use GC/MS and NMR comparisons. Figure 1 explicitly distinguishes the four stereoisomers. Plant iridoid synthases produce earlier pathway intermediates; they are biosynthetic enzymes, not demonstrated antibacterial targets of the product. |
| adopted-2019 | https://doi.org/10.1038/s41589-018-0185-2; PMID:30531909 / PMC6513753; identity, NEPS Results, Discussion and GC/MS Methods; Figure 1 visually inspected | supports | The original enzyme study distinguishes cis-trans product 1a from the other three stereoisomers. NEPS1 oxidizes cis-trans-nepetalactol; coupled ISY/NEPS systems generate specific products in vitro. The authors explicitly limit inference about in-planta roles and conditions. This is plant biosynthesis evidence, not antibacterial target inhibition. Figure 1 agrees with the native cis-trans configuration. |
| adopted-review | https://doi.org/10.1002/chem.201805412; PMID:30664302, publication type and complete abstract | context_only | This source is a minireview on biocatalytic cycloadditions. It provides biosynthesis context and discovery pointers, not an independent original antibacterial or exact-target experiment. |
| primary-material | https://doi.org/10.3390/ph14050414; PMC8145025; Sections 2.1 and 3.2; official supplement Figure S2a, PDF p5, visually inspected | supports | The 2021 study purifies 2 mg cis,trans-nepetalactone from N. cataria essential oil and characterizes it by chromatography, mass spectrometry and NMR with literature comparison. Figure S2a depicts the native absolute stereochemical drawing. The isolated cis,trans material is distinct from the study extracts and trans,cis fraction. No independent chiral-purity measurement was identified in the inspected methods; the published identification and structure are retained at their stated level. |
| primary-activity | https://doi.org/10.3390/ph14050414; Sections 2.4 and 3.5; Table 2, original PDF p12 visually inspected, continuation p13 read | supports | The cis,trans column reports bacterial MIC/MBC values in mg/mL, including S. aureus 0.010/0.020, E. coli 0.020/0.040 and L. monocytogenes 0.0025/0.005. Methods map these to ATCC 6538, ATCC 35210 and NCTC 7973. These are purified-compound observations, separate from the two extract columns. The same table reports fungal inhibition. Modified microdilution and compound stocks in 5% DMSO are stated, but the local methods refer to an earlier protocol instead of restating every incubation, inoculum and endpoint detail. Stock solvent concentration is not asserted to equal final assay concentration. |
| primary-boundaries | https://doi.org/10.3390/ph14050414; Sections 2.4, 2.5, 3.5 and Figure 4 caption; original full XML | supports | The resistant P. aeruginosa biofilm model is distinct from the Table 2 ATCC strain; its crystal-violet endpoint concerns prevention of biomass formation, not eradication. Tested additive combinations contain trans,cis-nepetalactone, not cis,trans. Macrophage ROS responses are host observations, not a bacterial target. Fungal name inconsistencies between table and methods require adjudication before exact fungal strain export. |
| search-adapter | Ignored-inclusive local search and structured iModulonDB catalog; 305-local-hits.txt; 305-focused-local-search.json; 297-adapter-catalog.json | context_only | The local search included ignored and hidden files. The previously executed structured catalog was inspected before protein follow-up; it has no Nepeta dataset. The native record has no protein/pathway assertion. Plant biosynthetic enzymes were therefore assessed in original papers without inventing an expression-dataset mapping or treating database absence as a negative biological result. |
| access | Free official and original-source retrievals; 305306-fetch.json, 305306-primary-fetch.json, 305306-supp-fetch.json, 305306-final-fetch.json and 305306-image-fetch.json | context_only | All ten adopted leads were resolved at original metadata/abstract level. Two original biosynthetic articles and the later purified-isomer antimicrobial article were read beyond abstracts. Several publisher routes returned 403, certificate errors or challenge pages. The 2021 original PDF and supplement were recovered from public MDPI resources and Europe PMC. Failed routes are retained; no paid or contact route was used. |
| gates | Actual focused chemistry, native schema and strict commands; 305-focused-results.json and corresponding logs | supports | All three actual focused checks exited zero against the unchanged exact record. Independent source comparisons are additional scientific checks, not a replacement for shared required gates. |

## Limits And Additional Notes

- MetaCyc CPD-15029 remains independently inaccessible. KNApSAcK displays a differing key despite matching standard InChI and SMILES; no native identity defect is inferred.
- Eight adopted sources were assessed at complete abstract/metadata depth, including the minireview. The 2018 biosynthesis body was read in full; the 2019 identity, enzyme-results, discussion and GC/MS portions were inspected, without exhaustive supplementary kinetic adjudication.
- The 2021 material, antimicrobial and immunomodulatory sections and relevant methods were read. Table 2 and supplement Figure S2a were visually inspected; NMR spectra were not independently reprocessed, and chiral purity was not independently measured.
- The 2021 methods omit some local incubation/inoculum details and contain fungal name discrepancies. No exact fungal strain observation or clinical breakpoint is exported.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record, source table, curation status or history was altered.
- Native schema and strict checks used the batch 031 environment. Independent molecular checks used the existing batch 019 RDKit interpreter against batch 031 cwd.
- All optional links, tags and notes were checked against this exact target. Discovery leads were not treated as evidence without the stated original-source reading.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T132709Z-cis-trans-nepetalactone-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'cis-trans-Nepetalactone: coherent exact isomer and purified-material antimicrobial
  evidence'
started_at: '2026-10-21T13:04:58Z'
finished_at: '2026-10-21T13:27:09Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. The entire native
    record, exact maintained source row, source ownership and history were read. Independent
    molecular checks, live official groundings and original source text were assessed,
    with original figures and supplements inspected where specified.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: No required native correction identified. The exact (4aS,7S,7aR) structure
  agrees with current official encodings and primary structure figures. A later original
  study tests purified cis,trans-nepetalactone against bacteria and fungi. All ten
  adopted citation leads were resolved with explicit distinctions among purified isomer,
  essential oil, behavioral endpoints and plant biosynthesis. MetaCyc access and some
  inherited non-antimicrobial claims remain limited. Scientific assessment retains
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
  - path: data/antibiotics/antibacterial/cis-trans-nepetalactone.yaml
    sha256: d715ba8cbbb2640746781afa320866957a6a3f78b3e434d447fc8fc6ea4ebed7
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
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
targets:
- target_id: CHEBI:7518
  path: data/antibiotics/antibacterial/cis-trans-nepetalactone.yaml
  label: cis-trans-nepetalactone
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
    path: data/raw/chebi_role_names.tsv
    role: Adopted ChEBI role names
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 305; one exact record. All 13 initial input hashes were
    preserved, and all 21 expanded input hashes were rechecked.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:7518
  exclusions:
  - target: Other nepetalactone stereoisomers, essential oils, mixed extracts and
      combination treatments as exact single-isomer observations
    reason: Material identity and assay endpoints do not transfer automatically to
      the native absolute stereoisomer.
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:7518
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    305 (cwd /private/tmp/antibioticmech-record-reviews-031)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:7518
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cis-trans-nepetalactone.yaml (cwd /private/tmp/antibioticmech-record-reviews-031)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:7518
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cis-trans-nepetalactone.yaml --out /private/tmp/am-review-session/305-strict.tsv
    (cwd /private/tmp/antibioticmech-record-reviews-031)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:7518
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
  - CHEBI:7518
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
  - CHEBI:7518
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
  - CHEBI:7518
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
  - CHEBI:7518
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
  - CHEBI:7518
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
  - CHEBI:7518
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
  - CHEBI:7518
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
  - CHEBI:7518
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cis-trans-nepetalactone.yaml
  locator: 'Entire 88-line YAML: all chemical fields, nine synonyms, parents, roles,
    six references, source concept and four history events'
  accessed_at: '2026-10-21T13:21:29Z'
  support: supports
  summary: The record is an EXACT, SEEDED antibacterial entry for CHEBI:7518. Definition,
    chemical classes, antibacterial/antifungal roles and imported references were
    read in full. No quantitative activity_spectrum, molecular target, resistance
    determinant, producer object, clinical assertion, dataset assertion or causal
    graph is populated.
  snapshot_sha256: 81ac6b1025c8126ff30b33960b8e9ae503f6dfabcb6fd6b934896f5027e0c934
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/chebi_role_names.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Exact raw ChEBI row 241 and source/extraction ownership
  accessed_at: '2026-10-21T13:21:29Z'
  support: supports
  summary: The source row reproduces the native chemical identity, definition, nine
    retained synonyms, parents, roles and chemical/document references, and supplies
    ten adopted PMID leads. Source extraction and seeding own the imported fields.
    No target-specific curator or decision override was found in the ignored-inclusive
    focused search. All 13 initial and 21 expanded hashes remain unchanged.
  snapshot_sha256: 87f7c72559ee24997b97fe1034d8b0fb25b955500e384ae5cf9e1e7a6e3e0406
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/review-yaml-record/SKILL.md; docs/record-review-profile.md;
    .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity, evidence scope, source ownership and optional completeness rubric
  accessed_at: '2026-10-21T13:21:29Z'
  support: supports
  summary: Optional mechanistic, quantitative activity and producer objects require
    defensible source mapping; their absence is not itself a native schema or scientific
    defect.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/7518/
  locator: Complete current CHEBI:7518 compound record
  accessed_at: '2026-10-21T13:13:02.105803Z'
  support: supports
  summary: The current definition, absolute (4aS,7S,7aR) names, neutral C10H14O2 formula
    and full key ZDKZHVNKFOXMND-NBEYISGCSA-N agree with the native structure. The
    source itself includes additional biological roles and producer references, which
    are not silently imported as native assertions.
  snapshot_sha256: a867ecfd56dd0a5b4bf641b1f755c93ccc2ce7ea080fe1c736d7dc536ff724ce
- evidence_id: terms
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms
  locator: 305-term-38606.json, 305-term-50563.json, 305-term-33282.json and 305-term-35718.json
  accessed_at: '2026-10-21T13:13:04.562846Z'
  support: supports
  summary: 'All four asserted terms resolve: cyclopentapyran, iridoid monoterpenoid,
    antibacterial agent and antifungal agent. Chemical classes fit the molecular graph;
    biological roles are separately assessed from original assay material.'
  snapshot_sha256: c615f73f2991f83b4553ad11f378734e1ad296c7bdb8382dbfb0715a80146a5b
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit and source identifier calculation
  locator: 305-chemistry.json; 305306-xref-chemistry.json; 305306-final-audit.json,
    target 305
  accessed_at: '2026-10-21T13:21:29Z'
  support: supports
  summary: Native SMILES and InChI give one neutral component, all three stereocentres
    assigned, the full stored key, C10H14O2 and consistent masses. The source mint
    antibioticmech:chebi-9e73b2a41d recomputes correctly. Current ChEBI, KEGG and
    LipidMaps structures and the independent PubChem CID 161367 comparator generate
    the same full key.
  snapshot_sha256: 6f8509eaadb85ccaf8042134ab50d84ff01f7f0f2d1bcec13b6ab62f6755aad2
- evidence_id: kegg-lipids
  kind: database
  reference: https://rest.kegg.jp/get/C09791
  locator: KEGG C09791 text and molfile; LipidMaps LMPR0102070013 JSON; independent
    full-graph calculation
  accessed_at: '2026-10-21T13:21:29Z'
  support: supports
  summary: KEGG C09791 and LipidMaps LMPR0102070013 identify the intended cis-trans
    form with the same complete absolute structure. KEGG molfile coordinates and stereochemical
    bonds preserve all three stereocentres. CAS 21651-62-7 is corroborated by these
    exact-compound entries and ChEBI.
  snapshot_sha256: d5d6188d437a2e05b5d4de8d0a67bc6a3df071cd0a71f10e5d231599f818021e
- evidence_id: knapsack
  kind: database
  reference: https://www.knapsackfamily.com/knapsack_core/information.php?word=C00003091
  locator: C00003091 names, CAS, formula, InChI, SMILES and displayed key
  accessed_at: '2026-10-21T13:13:02.106381Z'
  support: supports
  summary: KNApSAcK names cis-trans-nepetalactone and supplies CAS 21651-62-7. Its
    displayed key ZDKZHVNKFOXMND-KKRMJURBNA-N differs from the native standard key,
    but its actual standard InChI and stereochemical SMILES independently generate
    ZDKZHVNKFOXMND-NBEYISGCSA-N. This is an upstream representation inconsistency,
    not evidence of a different native molecule or a required xref removal.
  snapshot_sha256: ef46c4527770c9cd98467f783e0222bca993b82c9e92caf3a1697457545597b7
- evidence_id: xref-audit
  kind: validation
  reference: Current official structural encodings
  locator: 305306-final-audit.json, target 305 only
  accessed_at: '2026-10-21T13:21:29Z'
  support: supports
  summary: Independent parsing confirms both ChEBI encodings and both KNApSAcK encodings
    match the native graph. The KNApSAcK displayed-key discrepancy is explicitly retained
    instead of being silently described as exact string agreement.
  snapshot_sha256: 81ac6b1025c8126ff30b33960b8e9ae503f6dfabcb6fd6b934896f5027e0c934
- evidence_id: legacy-document
  kind: database
  reference: https://metacyc.org/compound?orgid=META&id=CPD-15029
  locator: MetaCyc CPD-15029 access result; 305-wiki.html topic page
  accessed_at: '2026-10-21T13:13:03.251616Z'
  support: context_only
  summary: The direct MetaCyc route leads to account-required content, so its exact
    molecular mapping remains independently unresolved. The Wikipedia reference resolves
    to the broader nepetalactone topic; it is a document link, not primary evidence
    or an assertion that every stereoisomer is equivalent.
  snapshot_sha256: 24b2a5abdd8d3058fe1e7712b8b3184785d0d2e8b86ff8784e1e511f2bda41da
- evidence_id: adopted-isolation
  kind: primary_source
  reference: https://doi.org/10.1021/np049647d
  locator: PMID:15974613, complete original abstract; official ACS supporting-file
    metadata
  accessed_at: '2026-10-21T13:13:02.106162Z'
  support: partial
  summary: The 2005 isolation/interconversion paper describes Nepeta racemosa/mussinii
    and faassenii material, several nepetalactone/nepetalactol diastereomers, NMR
    and calculated conformational properties. It supports chemical/isolation context,
    not an antibacterial endpoint. Publisher full text was inaccessible; eight official
    legacy .chm supplement entries were discovered but not decoded or executed. No
    exact numerical result is assigned from them.
  snapshot_sha256: 22baa73c1b5b0bae9a53afc5682713993617c49d3bcb7724d53fed09e98295ef
- evidence_id: adopted-aphid
  kind: primary_source
  reference: https://doi.org/10.1016/j.chroma.2007.12.020
  locator: PMID:18166192, complete original abstract
  accessed_at: '2026-10-21T13:13:02.106162Z'
  support: partial
  summary: The 2008 SPME-GC/MS study detects cis-trans-nepetalactone and nepetalactol
    associated with Cinara pilicornis on spruce and interprets them as likely pheromone
    components. It is analytical and ecological evidence, not an antibacterial assay;
    the abstract does not independently establish absolute hand or a purified-isomer
    mating-response experiment.
  snapshot_sha256: 22baa73c1b5b0bae9a53afc5682713993617c49d3bcb7724d53fed09e98295ef
- evidence_id: adopted-extract
  kind: primary_source
  reference: https://doi.org/10.1016/j.fitote.2010.03.007
  locator: PMID:20307630, complete original abstract
  accessed_at: '2026-10-21T13:13:02.106162Z'
  support: context_only
  summary: The 2010 shoot-culture study assigns cis-trans-nepetalactone to N. sibirica
    and trans-cis to N. rtanjensis, but tests methanolic plant extracts for antimicrobial
    activity. These mixed-material endpoints are not purified native-isomer MICs.
    Publisher retrieval failed, so no uninspected table or strain values are transferred.
  snapshot_sha256: 22baa73c1b5b0bae9a53afc5682713993617c49d3bcb7724d53fed09e98295ef
- evidence_id: adopted-behavior
  kind: primary_source
  reference: https://doi.org/10.1016/j.phytochem.2010.09.016; https://doi.org/10.1007/s10886-015-0585-7
  locator: PMID:21056438 and PMID:25956798, complete original abstracts
  accessed_at: '2026-10-21T13:13:02.106162Z'
  support: context_only
  summary: The 2011 study separately considers named (4aS,7S,7aR) and (4aS,7S,7aS)
    nepetalactones and mixtures in mosquito, tick and mite repellence. The 2015 study
    tests the native absolute isomer and nepetalactol in lacewing trap responses.
    These are behavioral endpoints and mixtures require separate attribution; neither
    paper establishes bacterial killing.
  snapshot_sha256: 22baa73c1b5b0bae9a53afc5682713993617c49d3bcb7724d53fed09e98295ef
- evidence_id: adopted-metabolism
  kind: primary_source
  reference: https://doi.org/10.1126/science.164.3885.1281
  locator: PMID:5770619, complete original abstract
  accessed_at: '2026-10-21T13:13:02.106162Z'
  support: partial
  summary: The 1969 paper follows radiolabeled cis-trans-nepetalactone metabolism
    in cats, including excretion products. The inspected abstract is not a new quantified
    attraction assay and supplies no antibacterial mechanism. The cat-attractant description
    is inherited context; its complete behavioral proof was not independently reconstructed
    here.
  snapshot_sha256: 22baa73c1b5b0bae9a53afc5682713993617c49d3bcb7724d53fed09e98295ef
- evidence_id: adopted-analgesia
  kind: primary_source
  reference: https://doi.org/10.1111/j.2042-7158.1998.tb07145.x
  locator: PMID:9720633, complete original abstract
  accessed_at: '2026-10-21T13:13:02.106162Z'
  support: partial
  summary: The analgesia paper screens N. caesarea essential oil whose major component
    is assigned as 4a-alpha,7-alpha,7a-alpha-nepetalactone. Naloxone-sensitive effects
    are attributed to the dominant constituent by the authors. The accessible abstract
    does not establish isolated exact-isomer dosing or direct opioid-receptor binding.
    Its inference is not upgraded to a purified-compound target assertion.
  snapshot_sha256: 22baa73c1b5b0bae9a53afc5682713993617c49d3bcb7724d53fed09e98295ef
- evidence_id: adopted-2018
  kind: primary_source
  reference: https://doi.org/10.1016/j.phytochem.2017.10.004
  locator: PMID:29091815 / PMC5739345; full body and Methods; Figure 1 visually inspected
  accessed_at: '2026-10-21T13:13:51.086984Z'
  support: supports
  summary: The original study identifies natural cis-trans-nepetalactone as (4aS,7S,7aR),
    with species/cultivar-dependent isomer distributions. Methods isolate an authentic
    cis-trans standard from N. faassenii Six Hills Giant and use GC/MS and NMR comparisons.
    Figure 1 explicitly distinguishes the four stereoisomers. Plant iridoid synthases
    produce earlier pathway intermediates; they are biosynthetic enzymes, not demonstrated
    antibacterial targets of the product.
  snapshot_sha256: f89c47eb497de3bf2e7561ede24b6c503d6c58913a44acf66093dc808f487b70
- evidence_id: adopted-2019
  kind: primary_source
  reference: https://doi.org/10.1038/s41589-018-0185-2
  locator: PMID:30531909 / PMC6513753; identity, NEPS Results, Discussion and GC/MS
    Methods; Figure 1 visually inspected
  accessed_at: '2026-10-21T13:14:51.259295Z'
  support: supports
  summary: The original enzyme study distinguishes cis-trans product 1a from the other
    three stereoisomers. NEPS1 oxidizes cis-trans-nepetalactol; coupled ISY/NEPS systems
    generate specific products in vitro. The authors explicitly limit inference about
    in-planta roles and conditions. This is plant biosynthesis evidence, not antibacterial
    target inhibition. Figure 1 agrees with the native cis-trans configuration.
  snapshot_sha256: 9b6ed90744ba75002d719117519ab4fb452f5f9ae41a8fc4374f2e628eaa8ec9
- evidence_id: adopted-review
  kind: primary_source
  reference: https://doi.org/10.1002/chem.201805412
  locator: PMID:30664302, publication type and complete abstract
  accessed_at: '2026-10-21T13:13:02.106162Z'
  support: context_only
  summary: This source is a minireview on biocatalytic cycloadditions. It provides
    biosynthesis context and discovery pointers, not an independent original antibacterial
    or exact-target experiment.
  snapshot_sha256: 22baa73c1b5b0bae9a53afc5682713993617c49d3bcb7724d53fed09e98295ef
- evidence_id: primary-material
  kind: primary_source
  reference: https://doi.org/10.3390/ph14050414
  locator: PMC8145025; Sections 2.1 and 3.2; official supplement Figure S2a, PDF p5,
    visually inspected
  accessed_at: '2026-10-21T13:17:20.880060Z'
  support: supports
  summary: The 2021 study purifies 2 mg cis,trans-nepetalactone from N. cataria essential
    oil and characterizes it by chromatography, mass spectrometry and NMR with literature
    comparison. Figure S2a depicts the native absolute stereochemical drawing. The
    isolated cis,trans material is distinct from the study extracts and trans,cis
    fraction. No independent chiral-purity measurement was identified in the inspected
    methods; the published identification and structure are retained at their stated
    level.
  snapshot_sha256: 7d9aa4e2f9d321b346e1a1a4a6a2f630b90158cfe450bb8a774e9f27b85da573
- evidence_id: primary-activity
  kind: primary_source
  reference: https://doi.org/10.3390/ph14050414
  locator: Sections 2.4 and 3.5; Table 2, original PDF p12 visually inspected, continuation
    p13 read
  accessed_at: '2026-10-21T13:17:20.880860Z'
  support: supports
  summary: The cis,trans column reports bacterial MIC/MBC values in mg/mL, including
    S. aureus 0.010/0.020, E. coli 0.020/0.040 and L. monocytogenes 0.0025/0.005.
    Methods map these to ATCC 6538, ATCC 35210 and NCTC 7973. These are purified-compound
    observations, separate from the two extract columns. The same table reports fungal
    inhibition. Modified microdilution and compound stocks in 5% DMSO are stated,
    but the local methods refer to an earlier protocol instead of restating every
    incubation, inoculum and endpoint detail. Stock solvent concentration is not asserted
    to equal final assay concentration.
  snapshot_sha256: 8be958f40f3b30aadbaa22bad5ea8f4035cc69ed48288fc9c802c918fa29ea42
- evidence_id: primary-boundaries
  kind: primary_source
  reference: https://doi.org/10.3390/ph14050414
  locator: Sections 2.4, 2.5, 3.5 and Figure 4 caption; original full XML
  accessed_at: '2026-10-21T13:13:51.087467Z'
  support: supports
  summary: The resistant P. aeruginosa biofilm model is distinct from the Table 2
    ATCC strain; its crystal-violet endpoint concerns prevention of biomass formation,
    not eradication. Tested additive combinations contain trans,cis-nepetalactone,
    not cis,trans. Macrophage ROS responses are host observations, not a bacterial
    target. Fungal name inconsistencies between table and methods require adjudication
    before exact fungal strain export.
  snapshot_sha256: cd993373a6cda9b31e704a684ac59cbbc6e83b99d4d77f57471802d304e5ca2b
- evidence_id: search-adapter
  kind: search
  reference: Ignored-inclusive local search and structured iModulonDB catalog
  locator: 305-local-hits.txt; 305-focused-local-search.json; 297-adapter-catalog.json
  accessed_at: '2026-10-21T13:21:29Z'
  support: context_only
  summary: The local search included ignored and hidden files. The previously executed
    structured catalog was inspected before protein follow-up; it has no Nepeta dataset.
    The native record has no protein/pathway assertion. Plant biosynthetic enzymes
    were therefore assessed in original papers without inventing an expression-dataset
    mapping or treating database absence as a negative biological result.
  snapshot_sha256: 2a9af6d2bf00a01bf4e48a869cf4e11637f5122dc72d93133f98c9048c73ccdb
  search_scope: 2026-10-21; exact queue 305 record identifier, names, full chemical
    key and adopted citation identifiers. Initial repository-wide and focused curation/conf
    searches included hidden and ignored files. Bounded free official, primary publisher
    and public archive retrievals are recorded in the cited manifests; no exhaustive
    literature-absence claim is made.
- evidence_id: access
  kind: search
  reference: Free official and original-source retrievals
  locator: 305306-fetch.json, 305306-primary-fetch.json, 305306-supp-fetch.json, 305306-final-fetch.json
    and 305306-image-fetch.json
  accessed_at: '2026-10-21T13:21:29Z'
  support: context_only
  summary: All ten adopted leads were resolved at original metadata/abstract level.
    Two original biosynthetic articles and the later purified-isomer antimicrobial
    article were read beyond abstracts. Several publisher routes returned 403, certificate
    errors or challenge pages. The 2021 original PDF and supplement were recovered
    from public MDPI resources and Europe PMC. Failed routes are retained; no paid
    or contact route was used.
  snapshot_sha256: 28c040b662691e3d837520d86bfc084c99c81c4eccbea1669d4d4b7d9cb2a8d7
  search_scope: 2026-10-21; exact queue 305 record identifier, names, full chemical
    key and adopted citation identifiers. Initial repository-wide and focused curation/conf
    searches included hidden and ignored files. Bounded free official, primary publisher
    and public archive retrievals are recorded in the cited manifests; no exhaustive
    literature-absence claim is made.
- evidence_id: gates
  kind: validation
  reference: Actual focused chemistry, native schema and strict commands
  locator: 305-focused-results.json and corresponding logs
  accessed_at: '2026-10-21T13:21:29Z'
  support: supports
  summary: All three actual focused checks exited zero against the unchanged exact
    record. Independent source comparisons are additional scientific checks, not a
    replacement for shared required gates.
  snapshot_sha256: becb459fffab34f98d2e0d78e4fb21a245d97ee7ad3e13d16077444351e3a672
assessments:
- assessment_id: identity
  area: identity
  topic: Absolute isomer, formula, charge and mass
  outcome: supported
  summary: Native graph, current ChEBI, KEGG, LipidMaps and original stereochemical
    figures consistently identify (4aS,7S,7aR)-nepetalactone. Other stereoisomers
    and mixed oils remain separate.
  target_ids:
  - CHEBI:7518
  evidence_ids:
  - native
  - chebi
  - chemistry
  - kegg-lipids
  - adopted-2018
  - adopted-2019
  - primary-material
- assessment_id: grounding
  area: grounding
  topic: Asserted chemical and document references
  outcome: supported
  summary: KEGG, LipidMaps and KNApSAcK structural encodings agree with the native
    identity, and CAS is corroborated. The KNApSAcK displayed-key inconsistency is
    upstream and does not invalidate its matching graph. Wikipedia is correctly treated
    as a broad document reference.
  target_ids:
  - CHEBI:7518
  evidence_ids:
  - chebi
  - kegg-lipids
  - knapsack
  - xref-audit
  - legacy-document
- assessment_id: metacyc
  area: grounding
  topic: MetaCyc CPD-15029 independent verification
  outcome: unknown
  summary: The asserted identifier remains source-backed but independently unresolved
    because the direct route required account access. No contrary exact mapping was
    established.
  target_ids:
  - CHEBI:7518
  evidence_ids:
  - legacy-document
  - access
- assessment_id: classes-roles
  area: evidence
  topic: Chemical classes and antibacterial/antifungal roles
  outcome: supported
  summary: The graph fits both chemical parents. Published purified cis,trans material
    and Table 2 support antimicrobial roles independently of extract-only adopted
    evidence. Assay scope and published structural characterization remain explicit.
  target_ids:
  - CHEBI:7518
  evidence_ids:
  - terms
  - primary-material
  - primary-activity
  - adopted-extract
- assessment_id: adopted-leads
  area: evidence
  topic: All ten inherited PMID leads
  outcome: supported
  summary: Each lead was resolved and its evidence type bounded. The set includes
    isolation, ecological behavior, metabolism, an extract study, biosynthesis originals
    and a minireview; they are not interchangeable antibacterial mechanism evidence.
  target_ids:
  - CHEBI:7518
  evidence_ids:
  - adopted-isolation
  - adopted-aphid
  - adopted-extract
  - adopted-behavior
  - adopted-metabolism
  - adopted-analgesia
  - adopted-2018
  - adopted-2019
  - adopted-review
- assessment_id: definition-ancillary
  area: evidence
  topic: Analgesic, aphid pheromone and cat-attractant breadth
  outcome: unknown
  summary: The inherited qualitative claims have relevant original leads, but accessible
    analgesia evidence concerns essential oil and ecological/metabolic abstracts do
    not independently resolve every exact-isomer behavioral claim. This bounded reading
    does not establish those claims false.
  target_ids:
  - CHEBI:7518
  evidence_ids:
  - adopted-aphid
  - adopted-behavior
  - adopted-metabolism
  - adopted-analgesia
- assessment_id: activity-completeness
  area: completeness
  topic: Optional activity_spectrum enrichment
  outcome: unknown
  summary: The 2021 purified-material table is a useful optional quantitative lead.
    Any future curation should retain exact material, strain, mg/mL units, endpoint
    and method limits, and resolve the fungal name conflicts. Missing optional activity
    objects are not a defect.
  target_ids:
  - CHEBI:7518
  evidence_ids:
  - primary-material
  - primary-activity
  - primary-boundaries
  - rubric
- assessment_id: mechanism-producer
  area: completeness
  topic: Optional producer and mechanism evidence
  outcome: unknown
  summary: Primary isolation supports bounded Nepeta producer context, with cultivar/isomer
    variation. ISY/NEPS are biosynthetic proteins and host macrophage responses are
    not antibacterial direct targets. No unsupported mechanism or causal graph should
    be inferred from these sources.
  target_ids:
  - CHEBI:7518
  evidence_ids:
  - adopted-2018
  - adopted-2019
  - primary-material
  - primary-boundaries
  - search-adapter
  - rubric
- assessment_id: other-domains
  area: scope
  topic: Unpopulated resistance, clinical and dataset assertions
  outcome: not_applicable
  summary: There are no native assertions in these domains. A strain resistant to
    other drugs does not itself establish resistance to this compound.
  target_ids:
  - CHEBI:7518
  evidence_ids:
  - native
  - primary-boundaries
- assessment_id: provenance
  area: provenance
  topic: Imported ownership, EXACT/SEEDED status and four history events
  outcome: supported
  summary: The exact ChEBI row and transform explain native content and history. All
    original hashes were preserved. This review does not promote the native scientific
    curation status.
  target_ids:
  - CHEBI:7518
  evidence_ids:
  - owners
  - native
  - rubric
- assessment_id: schema
  area: schema
  topic: Focused deterministic checks
  outcome: supported
  summary: Native schema, strict validation and molecular consistency pass; scientific
    interpretation remains separately bounded.
  target_ids:
  - CHEBI:7518
  evidence_ids:
  - gates
  - chemistry
findings: []
actions:
- action_id: A1
  description: Optionally enrich exact-isomer activity and producer context from the
    inspected original sources.
  finding_ids: []
  target_ids:
  - CHEBI:7518
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cis-trans-nepetalactone.yaml
    role: Curator-owned activity_spectrum and producer evidence through the validated
      writer
  acceptance_checks:
  - Retain the 2021 isolated cis,trans material and original Table 2 column, units,
    strain mappings and method limits.
  - Keep extracts, trans,cis material, combinations and host-cell endpoints separate.
  - Resolve fungal table/method naming conflicts before quantitative fungal strain
    export.
  - Do not convert plant biosynthetic enzymes into antibacterial targets; run applicable
    native gates after separately authorized curation.
- action_id: A2
  description: Resolve inaccessible legacy mapping and ancillary definition details
    only when those fields are revised or enriched.
  finding_ids: []
  target_ids:
  - CHEBI:7518
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Imported source-owned identity, definition and references
  acceptance_checks:
  - Verify MetaCyc CPD-15029 directly before claiming independent confirmation or
    removal.
  - Preserve the KNApSAcK encoding/display distinction; its matching molecular graph
    does not warrant automatic removal.
  - Use original isolated-material evidence before asserting a direct analgesic receptor
    or quantified exact-isomer behavioral effect.
limitations:
- MetaCyc CPD-15029 remains independently inaccessible. KNApSAcK displays a differing
  key despite matching standard InChI and SMILES; no native identity defect is inferred.
- Eight adopted sources were assessed at complete abstract/metadata depth, including
  the minireview. The 2018 biosynthesis body was read in full; the 2019 identity,
  enzyme-results, discussion and GC/MS portions were inspected, without exhaustive
  supplementary kinetic adjudication.
- The 2021 material, antimicrobial and immunomodulatory sections and relevant methods
  were read. Table 2 and supplement Figure S2a were visually inspected; NMR spectra
  were not independently reprocessed, and chiral purity was not independently measured.
- The 2021 methods omit some local incubation/inoculum details and contain fungal
  name discrepancies. No exact fungal strain observation or clinical breakpoint is
  exported.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record, source table, curation status or history was altered.
- Native schema and strict checks used the batch 031 environment. Independent molecular
  checks used the existing batch 019 RDKit interpreter against batch 031 cwd.
- All optional links, tags and notes were checked against this exact target. Discovery
  leads were not treated as evidence without the stated original-source reading.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:7518
- https://doi.org/10.3390/ph14050414
- https://doi.org/10.1016/j.phytochem.2017.10.004
tags:
- cis-trans-nepetalactone
- exact-stereoisomer
- purified-compound-assays
```
