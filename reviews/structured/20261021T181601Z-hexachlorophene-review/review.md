# Hexachlorophene: exact identity and measurements supported; add assay-interference context

- Review: 20261021T181601Z-hexachlorophene-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:48:35Z
- Finished UTC: 2026-10-21T18:16:01Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The neutral hexachlorophene graph agrees across eighteen native and authority encodings, and all ten FDA product assertions match the current official data. Both BindingDB measurements reproduce their original reported values. The SARS-CoV-2 FRET measurement lacks the original fluorescence-quenching qualification, a minor context omission rather than evidence of inactivity or disproven binding. Antibacterial activity is independently supported; target, host, formulation and agricultural-use boundaries remain explicit.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 530; one whole exact native record. All thirteen original input hashes were verified and preserved. Four actual FDA and BindingDB source/transform owners were appended before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:5693 | data/antibiotics/antibacterial/hexachlorophene.yaml | generated | hexachlorophene |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | CHEBI:5693 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:5693 | Actual focused execution exited 0. |
| Focused chemistry verification | passed | False | CHEBI:5693 | Actual focused execution exited 0. |
| Eighteen native and authority encodings reproduce the same neutral molecular graph. | passed | False | CHEBI:5693 | Eighteen native and authority encodings reproduce the same neutral molecular graph. |
| All ten native assertions match current official application/product, sponsor, ingredient, original approval date and marketing fields. | passed | False | CHEBI:5693 | All ten native assertions match current official application/product, sponsor, ingredient, original approval date and marketing fields. |
| Structured source applicability before web research | passed | False | CHEBI:5693 | Dataset catalog completed; no covered SARS-CoV or SARS-CoV-2 dataset matched the native target organisms, so a corresponding organism-specific search was not applicable. |
| Authoritative full QC | failed | True | CHEBI:5693 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:5693 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:5693 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:5693 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:5693 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:5693 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:5693 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:5693 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:5693 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral molecule and chemical groundings

identity: supported. Targets: CHEBI:5693.

Native structure, formula and masses agree with independent authority encodings, CAS and original chemical context. All systematic synonyms and broader structural parents are compatible with the graph.

### Remaining registry and document access limits

grounding: unknown. Targets: CHEBI:5693.

No positive exact-identifier mismatch was found, but direct HMDB, LINCS, Reaxys and DrugBank content was not available at complete-source depth. Upstream attribution is retained without pretending every registry was independently verified.

### Ten FDA assertions and clinical summary

evidence: supported. Targets: CHEBI:5693.

Current official data reproduce all ten assertions, including their distinct marketing flags. Two Prescription products remain positive current API support; discontinued products are not silently rewritten as never approved. Product use is not a general safety recommendation.

### Reported SARS-CoV Ki and protein grounding

evidence: supported. Targets: CHEBI:5693.

The original paper reports Ki 4 µM for recombinant 3CL protease, matching the retained kinetic measurement. UniProt polyprotein accessions include the processed protease; the experiment did not assay the full polyprotein or prove cellular antiviral efficacy.

### Reported SARS-CoV-2 FRET IC50 and interference qualification

evidence: concern. Targets: CHEBI:5693.

The reported 21.52 µM value and measured-association relation are correct, but the experimental context omits the original partial fluorescence-quenching qualification. The omission is bounded and does not justify deleting the measurement or denying binding.

### Antibacterial, antifungal and agricultural roles

grounding: supported. Targets: CHEBI:5693.

Direct bacterial experiments support exact-compound activity; fungal screening and historical agricultural sources support the broader roles. Dose per cell mass, library-hit endpoints, historical uses and contemporary approval scope remain distinct.

### Optional bacterial mechanism versus host and viral evidence

evidence: unknown. Targets: CHEBI:5693.

The record does not assert a bacterial causal graph. Purified FabI inhibition, expression responses, high-dose membrane injury and host channel effects support different claims and should not be promoted into a single established bacterial mechanism. Viral targets can coexist with antibacterial filing without becoming bacterial targets.

### Source inputs, citation placement and history

provenance: supported. Targets: CHEBI:5693.

Seventeen captured inputs retain the original thirteen hashes and include actual FDA/BindingDB owners. The source concept and nine history events are consistent with SEEDED status. Adopted leads are not treated as blanket evidence for the whole record.

### Optional representations and claim boundaries

completeness: supported. Targets: CHEBI:5693.

No missing optional activity, resistance, producer, graph or dataset object is itself a defect. Any enrichment must retain exact material, target-chain, taxon, unit, assay-interference and endpoint scope; neither synthesis nor host exposure proves natural production.

## Findings

### F1: Retain the fluorescence-quenching qualification with the SARS-CoV-2 FRET measurement

minor / open / confirmed; issue key: hexachlorophene-sars2-fret-quenching-context.

The native 21520 nM IC50 correctly reproduces Table 2 of the adopted 2020 preprint, but the target context and evidence notes omit that hexachlorophene is one of the partially fluorescence-quenching compounds. The published successor confirms that scope in Table 2 and Figure 5f. Because the record already uses MEASURED_TARGET_ASSOCIATION and does not assert direct binding, this is a non-blocking assay-context omission rather than a disproven measurement or established inactivity.

## Recommended Actions And Acceptance Checks

### A1

Add the source-supported quenching qualification through a maintained target-context overlay or extraction path, retaining the reported measurement.

- Retain the reported IC50 of 21520 nM, qualifier, BindingDB identifiers and measured-association relation; do not recast it as Kd or delete it solely because of partial quenching.
- State in experimental context or evidence notes that the original counter-screen detected fluorescence quenching and therefore limits interpretation of the FRET result. Preserve any verbatim assay description rather than inserting interpretation into quoted source text.
- Keep the SARS-CoV 2005 Ki independent from the SARS-CoV-2 counter-screen. If citing the published successor, preserve the original preprint provenance and distinguish recombinant processed protease from the parent polyprotein.
- Regenerate the exact source-owned record and pass focused schema/strict, reference and corpus reproduction checks.

### A2

If adding optional activity or bacterial mechanism evidence, keep the original material and assay boundaries.

- Do not encode the 1971 dose in µg per mg cell dry weight as a µg/mL MIC or equate higher-dose membrane injury with the primary killing target.
- Keep purified FabI assays, bacterial expression profiles, host channel activation, viral protease assays and clinical formulation records separate.
- Preserve antifungal abstract-only limits and historical agricultural-use context; do not infer universal current use or regulatory approval from a product name.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/hexachlorophene.yaml; Entire native YAML, including all thirty-nine synonyms, three parents, four roles, exact and broader references, both complete target objects, ten FDA assertions and nine history events. | supports | CHEBI:5693 denotes neutral hexachlorophene, C13H6Cl6O2, ACGUYXCXAPNIKK-UHFFFAOYSA-N, with EXACT grounding and SEEDED status. Both viral target relations are explicitly MEASURED_TARGET_ASSOCIATION, not direct binding. No quantitative microbial activity, resistance, producer, causal graph, transcriptomics dataset or discussion is populated. |
| owners | data/raw/chebi_antimicrobials.tsv:189; data/raw/fda_clinical_status.tsv:2-11; data/raw/bindingdb_target_measurements.tsv:90-95; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/extract_fda_clinical_status.py; scripts/extract_bindingdb_targets.py; scripts/seed_from_sources.py; Complete exact source rows, actual configuration and relevant extraction/seeding logic, including BindingDB filtering and original-approval/marketing handling. | supports | The ChEBI source supplies identity, definition, aliases, classes, roles and six citation leads. Ten FDA rows supply historical original approvals and separate marketing flags. Six BindingDB rows include the two retained measurements; review-derived, whole-cell immunofluorescence and CPE EC50 rows are filtered rather than promoted into target assays. The target relation mapping preserves measured association for Ki/IC50. Hidden/ignored-inclusive owner searches found no applicable exact curator addition or decision. All original thirteen hashes are retained among seventeen captured inputs. |
| chemistry | CHEBI:5693; pubchem.compound:3598; cas:70-30-4; KEGG:C08039; KEGG:D00859; pdb-ccd:H3P; UNII:IWW5FV6NK2; PPDB:381; BindingDB:31712; Complete available structure responses and independent native/authority SMILES, InChI or molfile parsing. | supports | All eighteen encodings reproduce the same full neutral key, formula and zero formal charge. CAS lookup independently returns CID3598. The native average and monoisotopic masses pass the focused check. Current GSRS version 27 and native version 25 have the same chemical graph. CCD descriptor variants and both KEGG entries also agree; no salt-component or stereochemical mismatch was found. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/5693/; CHEBI:26195; CHEBI:27096; CHEBI:87039; CHEBI:24127; CHEBI:33282; CHEBI:35718; CHEBI:86328; Complete current compound entry and all seven official parent/role definitions. | supports | The exact structure and systematic/INN aliases agree with the native graph. Thirty-one product aliases are retained as BRAND_NAME, not exact molecular equivalence. Polyphenol, trichlorobenzene and bridged diphenyl fungicide are compatible broader classes; each aromatic ring has three chlorines. Antibacterial, antifungal, fungicide and antifungal-agrochemical roles resolve correctly. Current ChEBI reproduces the adopted definition and source associations. |
| reference-boundaries | HMDB:HMDB0014894; LINCS:LSM-6032; Reaxys:2064407; DrugBank:DB00756; https://drugcentral.org/drugcard/1364; Accessible DrugCentral identity and synonyms, ChEBI cross-reference attribution, and indexed official HMDB search text; direct-access failures retained in fetch manifests. | context_only | DrugCentral matches name, CAS and formula, supporting the broader drug association. Direct DrugBank, HMDB, LINCS and Reaxys records were not independently available at complete-source depth. Official HMDB search text displays matching chemistry, but the actual page could not be opened, so this remains a lead rather than a separately verified exact graph. These access limits do not establish erroneous identifiers or universal regulatory absence. |
| fda | https://api.fda.gov/drug/drugsfda.json; UNII:IWW5FV6NK2; applications 006882,017411,017412,017413,017421,017433,017446,017452; All ten exact native application/product assertions compared against current official API records; current official GSRS identity parsed independently. | supports | Product names, sponsors, ingredient, original approval dates and marketing fields all match. PRE-OP and PRE-OP II under NDA 017433 remain Prescription in the current API; the other eight products are Discontinued. Historical original-AP evidence is not erased by discontinued marketing. The APPROVED summary therefore has positive retained support, and no withdrawal finding is inferred. Seven additional returned applications lacked the qualifying original-approval data used by the maintained filter. An unrelated homeopathic label and an empty PHISOHEX DailyMed search were not used as evidence for these products. |
| agricultural-use | https://sitem.herts.ac.uk/aeru/ppdb/en/Reports/381.htm; Regulation (EC) 2076/2002; PPDB chemical descriptors, use summary and current EU approval status inspected; historical regulation identifier and hexachlorophene entry checked through official indexed text, not a complete legal-history audit. | supports | PPDB describes hexachlorophene as an obsolete agricultural agent once used as acaricide and fungicide and reports Not approved under the current EU plant-protection framework. This supports historical agricultural use and the stated EU boundary. It does not establish current use frequency in every jurisdiction, a universal prohibition, or a current clinical recommendation. |
| documents | https://patents.google.com/patent/US2250480A/en; https://patents.google.com/patent/US2435593A/en; https://patents.google.com/patent/US2812365A/en; Complete US2250480 description and claims read; opening process descriptions and selected examples of the latter two patents inspected. The Wikipedia document link is contextual, not experimental evidence. | supports | The original patent describes the methylene-bridged trichlorophenol constitution and free-acid isolation, with salts treated separately. Later patents concern preparation and product isolation. These links are relevant documents, not exact molecular xrefs or modern clinical efficacy demonstrations. Historical product/process claims are not transferred into present-day safety or quantified antimicrobial outcomes. |
| protein-grounding | UniProtKB:P0C6U8; UniProtKB:P0DTD1; NCBITaxon:2901879; NCBITaxon:2697049; Complete reviewed UniProt records with processed-chain features and official NCBI taxonomy responses. | supports | P0C6U8 is reviewed SARS coronavirus replicase polyprotein 1a with 3CL protease/nsp5 residues 3241-3546. Its current UniProt taxon 694009 is a broader species lineage containing the native SARS-CoV taxon 2901879. P0DTD1 is reviewed SARS-CoV-2 polyprotein 1ab, with nsp5 residues 3264-3569 and matching taxon 2697049. The assays use recombinant processed protease, not the full polyproteins; parent-accession grounding is not evidence that an entire polyprotein was experimentally assayed. |
| bindingdb | https://www.bindingdb.org/rwd/bind/chemsearch/marvin/MolStructure.jsp?monomerid=31712; reactant sets 844294 and 844363; assays 8809_1 and 8814_1; Complete accessible ligand page and exact native raw measurement rows, cross-checked against original papers. | supports | The ligand page matches the exact graph and retains both reaction-set identifiers and reported 4000 nM Ki and 21520 nM IC50. Database fidelity supports provenance but does not remove the original assay-interference qualification. The values remain kinetic/response measurements, not dissociation constants. |
| sars2005 | PMID:15950190; DOI:10.1016/j.bbrc.2005.05.095; https://pmc.ncbi.nlm.nih.gov/articles/PMC7092914/; Complete original main text, Methods, Results, Discussion and figure captions read; original figure images not independently reanalysed. | supports | Recombinant SARS-CoV 3CL protease was expressed as an MBP fusion and released as a 306-residue enzyme. The FRET assay used a 20 nM enzyme preparation,30 µM substrate,25 degrees C and buffer containing 1 mM DTT, with a 15 min compound preincubation. Hexachlorophene gave a reported IC50 of 5 µM and competitive Ki of 4 µM, the latter matching native 4000 nM. Docking used a pre-existing structure and is computational, not an experimental drug-bound crystal. E. coli was the expression host, not the native assay target organism. These results do not by themselves establish cellular antiviral efficacy. |
| sars2020 | PMID:32803196; DOI:10.1101/2020.07.17.207019; https://pmc.ncbi.nlm.nih.gov/articles/PMC7427131/; Complete original preprint main text, both complete tables and Figure 5 caption read, including fluorescence-product counter-screen Methods and Results. | supports | The recombinant SARS-CoV-2 3CL FRET screen separately tested fluorescence quenching using the cleaved Edans-containing product without enzyme. Hexachlorophene appears in Table 2 among nine CPE-active quenching compounds, not the twenty-three minimally quenching hits in Table 1. Its reported IC50 is 21.52 µM, correctly converted to21520 nM in the native record. Table 2 also reports partial CPE protection and cytotoxicity; those whole-cell outcomes are distinct from the target assay. The authors warn that quenching and host-cell toxicity complicate interpretation. This primary preprint was not peer reviewed at posting; the subsequent published article preserves the relevant result. |
| published2020 | PMID:33062953; DOI:10.1021/acsptsci.0c00108; https://pmc.ncbi.nlm.nih.gov/articles/PMC7507806/; Published Results paragraphs on quenching, Table 2 and Figure 5 caption inspected; article-linked Figure 5 independently viewed, especially panel f. | supports | The published successor likewise places hexachlorophene in the quenching-compound table. Figure 5f shows enzyme-assay inhibition and a separate partial fluorescence-quenching response at higher concentrations. This supports retaining the measured association with a caveat; it does not prove that all observed inhibition is artifactual, that the molecule is inactive or that binding is absent. Table 2 gives CPE efficacy 43.57%, whereas the caption says47.57%; no precise CPE efficacy is imported here. Neither inspected version establishes an orthogonal hexachlorophene protease measurement that removes this limitation. |
| adopted-leads | PMID:1133685; PMID:22313968; PMID:23251633; PMID:397166; PMID:894425; PMID:952574; Complete indexed abstracts for five adopted papers; bibliographic metadata only for the IARC monograph PMID 397166, which has no indexed abstract. | context_only | PMID1133685 is colorimetric analysis of topical formulations. PMID22313968 studies rat brain injury/CNPase context after hexachlorophene or cuprizone. PMID23251633 concerns host KCNQ1/KCNE1 activation, not a bacterial target. PMID 397166 is a secondary IARC assessment rather than primary assay evidence. PMID894425 concerns infant exposure, pharmacokinetics and toxicity during soap bathing; it is not a pure-compound MIC or a current clinical recommendation. PMID952574 concerns rat biliary clearance and enterohepatic circulation. None establishes a natural producer or antibacterial causal chain. |
| host-channel | PMID:23251633; DOI:10.1371/journal.pone.0051820; https://pmc.ncbi.nlm.nih.gov/articles/PMC3520906/; Selected original CHO-expression/electrophysiology Methods, relevant Results and Discussion read after the complete abstract; not a complete independent audit of every figure. | context_only | The paper measures activation of mammalian KCNQ1/KCNE1 channels and reports an EC50 of 4.61±1.29 µM. It supports host pharmacology context, not bacterial membrane killing or approved treatment of long-QT syndrome. No such target is required merely because the literature exists. |
| bacterial1971 | PMID:4107813; DOI:10.1128/jb.108.1.482-491.1971; https://pmc.ncbi.nlm.nih.gov/articles/PMC247089/; Original scanned pages 482-484 and 489-491 independently viewed, including material/method details, selected results and discussion. Pages485-488 were downloaded but not independently read. | supports | The study uses supplier-identified hexachlorophene crystals, ethanol stocks and matched solvent controls against asporogenous Bacillus megaterium KM. Viability experiments and microscopy distinguish cell killing from higher-dose visible membrane injury. The approximate lethal threshold is 10 µg per mg cell dry weight, not10 µg/mL or a standardized MIC. At the threshold, overt cytopathology was not observed; higher concentrations caused membrane/dye effects. The authors distinguish adsorption and observable damage from proof of the primary causal target. This is direct compound-specific antibacterial evidence, with explicit assay/material limits. |
| bacterial-mechanism | PMID:10671494; DOI:10.1074/jbc.275.7.4654; PMID:11368521; DOI:10.1006/abbi.2001.2349; PMID:15273089; https://pmc.ncbi.nlm.nih.gov/articles/PMC478524/; Complete abstracts of the two purified-FabI studies; selected original 2004 expression-study Methods, hexachlorophene Results, FabI-assay text and Discussion. | supports | Purified FabI inhibition is reported, but the earlier S. aureus overexpression/mutant findings do not establish FabI as the whole-cell cause for hexachlorophene. The Haemophilus influenzae study reports an in vitro IC50 and acknowledges mechanistic ambiguity. The2004 B. subtilis 168 study finds a response distinct from the expected fatty-acid-synthesis inhibitor pattern and concludes that growth inhibition in that experiment did not follow the presumed FabI mechanism. Expression classification is not direct binding, and these differing evidence layers are not collapsed into a native causal chain. |
| fungal | PMID:32004725; DOI:10.1016/j.jgar.2020.01.002; Complete indexed original abstract only. | supports | A screen of 1280 approved-drug-library compounds against six resistant filamentous fungal strains identifies hexachlorophene among broad growth-inhibitory hits. This supports bounded antifungal activity, while exact strain-level concentrations, material purity and full assay conditions were not checked at full-text depth. No MICs or target assignments are imported. |
| adapter | 530-imodulondb-datasets.txt; shared structured source adapter; Dataset catalog run at 2026-10-21T18:05:00Z before protein-mechanism web follow-up. | context_only | No covered SARS-CoV or SARS-CoV-2 dataset matched the two native target organisms. The adapter is therefore not applicable beyond this catalog check. Absence from the catalog is not negative biochemical or antiviral evidence. |
| search | 530-local-hits.txt; 530-owner-hits.txt; 530-adopted.json; 530-followup.json; 530-fetch-results.json through530-fetch4-results.json; Initial exact identifier/label/slug search and actual-owner search included hidden and ignored files; bounded public chemical-authority, exact-name and cited-primary follow-up. | context_only | All six adopted ChEBI leads and both retained BindingDB citations were dispositioned. Excluded BindingDB review and whole-cell leads were checked at abstract/database depth for their distinct scope. Public failures, challenge HTML and empty responses were preserved rather than treated as source text. This bounded review does not claim to identify every antimicrobial target, formulation or regulatory event. |

## Limits And Additional Notes

- The review is partial because several registry pages and full experimental details remain unavailable. HMDB was available only as indexed official text, LINCS returned an error, Reaxys was not directly inspected and DrugBank direct retrieval failed. These are access limits, not confirmed identity defects.
- The2005 primary and 2020 preprint main texts were read completely. The published 2020 successor was checked in the relevant Results, Table 2 and Figure 5, whose image was independently viewed; unrelated supplemental experiments were not comprehensively reanalysed.
- The1971 paper was visually read on pages 482-484 and 489-491, not all ten pages. The two earlier purified-FabI studies and the 2020 fungal study were inspected at complete abstract depth only. The2004 expression study and 2012 host-channel paper were read selectively for the stated mechanistic scope.
- All six adopted ChEBI leads were dispositioned, but the 1979 IARC monograph had no indexed abstract and was not available at full-text depth. Analytical formulation, host toxicology and pharmacokinetic reports were not treated as microbial mechanism evidence.
- The preprint and published Table 2 report CPE efficacy 43.57%, whereas the corresponding Figure 5 caption says47.57%. This source inconsistency concerns a non-native whole-cell endpoint and was not transferred into a quantitative activity object.
- Current FDA API assertions and GSRS identity were checked, but this was not a comprehensive review of every historical regulatory notice or every marketed formulation. PPDB supports the current EU agricultural status; the complete legal history and contemporary global frequency of use were not audited.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Fetch manifests preserve actual URLs, UTC times, response failures and SHA256 values. All seventeen source input hashes were rechecked before draft output. Schema/strict/chemistry and independent comparisons are distinct from scientific assessment.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T181601Z-hexachlorophene-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Hexachlorophene: exact identity and measurements supported; add assay-interference
  context'
started_at: '2026-10-21T17:48:35Z'
finished_at: '2026-10-21T18:16:01Z'
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
verdict: needs_curation
scientific_review: true
summary: The neutral hexachlorophene graph agrees across eighteen native and authority
  encodings, and all ten FDA product assertions match the current official data. Both
  BindingDB measurements reproduce their original reported values. The SARS-CoV-2
  FRET measurement lacks the original fluorescence-quenching qualification, a minor
  context omission rather than evidence of inactivity or disproven binding. Antibacterial
  activity is independently supported; target, host, formulation and agricultural-use
  boundaries remain explicit.
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
  - path: data/antibiotics/antibacterial/hexachlorophene.yaml
    sha256: 4c3b1db8eb6cb1d30826bdb8ea9bb72f2bc6210b85752641601cdecf48d20bd4
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/bindingdb_target_measurements.tsv
    sha256: faccfe5634f467801aeb256e6560af09d193cdb53bdbf29dea195c9c0488c480
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
  - path: scripts/extract_bindingdb_targets.py
    sha256: 9914a61b93326808b9800f3680dc935af2abcfa1e9925d6c3dd39180dbc78a2d
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
- target_id: CHEBI:5693
  path: data/antibiotics/antibacterial/hexachlorophene.yaml
  label: hexachlorophene
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
    path: data/raw/fda_clinical_status.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/bindingdb_target_measurements.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_bindingdb_targets.py
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Actual maintained source input for the record
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 530; one whole exact native record. All thirteen original
    input hashes were verified and preserved. Four actual FDA and BindingDB source/transform
    owners were appended before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:5693
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:5693
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/hexachlorophene.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:5693
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/hexachlorophene.yaml --out /private/tmp/am-review-session/530-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:5693
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 530
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-chemistry
  name: Eighteen native and authority encodings reproduce the same neutral molecular
    graph.
  status: passed
  required: false
  summary: Eighteen native and authority encodings reproduce the same neutral molecular
    graph.
  target_ids:
  - CHEBI:5693
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/530-authority-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: fda-comparison
  name: All ten native assertions match current official application/product, sponsor,
    ingredient, original approval date and marketing fields.
  status: passed
  required: false
  summary: All ten native assertions match current official application/product, sponsor,
    ingredient, original approval date and marketing fields.
  target_ids:
  - CHEBI:5693
  command: .venv/bin/python /private/tmp/am-review-session/530-fda-compare.py
  exit_code: 0
  expected_exit_code: 0
- check_id: structured-adapter
  name: Structured source applicability before web research
  status: passed
  required: false
  summary: Dataset catalog completed; no covered SARS-CoV or SARS-CoV-2 dataset matched
    the native target organisms, so a corresponding organism-specific search was not
    applicable.
  target_ids:
  - CHEBI:5693
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
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
  - CHEBI:5693
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
  - CHEBI:5693
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
  - CHEBI:5693
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
  - CHEBI:5693
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
  - CHEBI:5693
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
  - CHEBI:5693
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
  - CHEBI:5693
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
  - CHEBI:5693
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
  - CHEBI:5693
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/hexachlorophene.yaml
  locator: Entire native YAML, including all thirty-nine synonyms, three parents,
    four roles, exact and broader references, both complete target objects, ten FDA
    assertions and nine history events.
  accessed_at: '2026-10-21T18:13:23Z'
  support: supports
  summary: CHEBI:5693 denotes neutral hexachlorophene, C13H6Cl6O2, ACGUYXCXAPNIKK-UHFFFAOYSA-N,
    with EXACT grounding and SEEDED status. Both viral target relations are explicitly
    MEASURED_TARGET_ASSOCIATION, not direct binding. No quantitative microbial activity,
    resistance, producer, causal graph, transcriptomics dataset or discussion is populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv:189; data/raw/fda_clinical_status.tsv:2-11;
    data/raw/bindingdb_target_measurements.tsv:90-95; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/extract_fda_clinical_status.py; scripts/extract_bindingdb_targets.py;
    scripts/seed_from_sources.py
  locator: Complete exact source rows, actual configuration and relevant extraction/seeding
    logic, including BindingDB filtering and original-approval/marketing handling.
  accessed_at: '2026-10-21T18:13:23Z'
  support: supports
  summary: The ChEBI source supplies identity, definition, aliases, classes, roles
    and six citation leads. Ten FDA rows supply historical original approvals and
    separate marketing flags. Six BindingDB rows include the two retained measurements;
    review-derived, whole-cell immunofluorescence and CPE EC50 rows are filtered rather
    than promoted into target assays. The target relation mapping preserves measured
    association for Ki/IC50. Hidden/ignored-inclusive owner searches found no applicable
    exact curator addition or decision. All original thirteen hashes are retained
    among seventeen captured inputs.
  snapshot_sha256: 0a00b77549951171d62d4a58c47aecc9ba7a139b1998e1ccf92b667045101afc
- evidence_id: chemistry
  kind: authority
  reference: CHEBI:5693; pubchem.compound:3598; cas:70-30-4; KEGG:C08039; KEGG:D00859;
    pdb-ccd:H3P; UNII:IWW5FV6NK2; PPDB:381; BindingDB:31712
  locator: Complete available structure responses and independent native/authority
    SMILES, InChI or molfile parsing.
  accessed_at: '2026-10-21T18:13:23Z'
  support: supports
  summary: All eighteen encodings reproduce the same full neutral key, formula and
    zero formal charge. CAS lookup independently returns CID3598. The native average
    and monoisotopic masses pass the focused check. Current GSRS version 27 and native
    version 25 have the same chemical graph. CCD descriptor variants and both KEGG
    entries also agree; no salt-component or stereochemical mismatch was found.
  snapshot_sha256: 972f4666437d001bcfc36b6808c5bc8fb25628e9ba200217bbe35464dc1f20b8
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/5693/; CHEBI:26195;
    CHEBI:27096; CHEBI:87039; CHEBI:24127; CHEBI:33282; CHEBI:35718; CHEBI:86328
  locator: Complete current compound entry and all seven official parent/role definitions.
  accessed_at: '2026-10-21T18:05:18Z'
  support: supports
  summary: The exact structure and systematic/INN aliases agree with the native graph.
    Thirty-one product aliases are retained as BRAND_NAME, not exact molecular equivalence.
    Polyphenol, trichlorobenzene and bridged diphenyl fungicide are compatible broader
    classes; each aromatic ring has three chlorines. Antibacterial, antifungal, fungicide
    and antifungal-agrochemical roles resolve correctly. Current ChEBI reproduces
    the adopted definition and source associations.
  snapshot_sha256: b14ad7ef204d37eb722ed830437844f187463245bb60cce79cde3b9281300d56
- evidence_id: reference-boundaries
  kind: database
  reference: HMDB:HMDB0014894; LINCS:LSM-6032; Reaxys:2064407; DrugBank:DB00756; https://drugcentral.org/drugcard/1364
  locator: Accessible DrugCentral identity and synonyms, ChEBI cross-reference attribution,
    and indexed official HMDB search text; direct-access failures retained in fetch
    manifests.
  accessed_at: '2026-10-21T18:05:19Z'
  support: context_only
  summary: DrugCentral matches name, CAS and formula, supporting the broader drug
    association. Direct DrugBank, HMDB, LINCS and Reaxys records were not independently
    available at complete-source depth. Official HMDB search text displays matching
    chemistry, but the actual page could not be opened, so this remains a lead rather
    than a separately verified exact graph. These access limits do not establish erroneous
    identifiers or universal regulatory absence.
  snapshot_sha256: fc21cb0798a0505353668f53767b0ee51526315028ba7c6cc1c7312ea61c5ccc
- evidence_id: fda
  kind: authority
  reference: https://api.fda.gov/drug/drugsfda.json; UNII:IWW5FV6NK2; applications
    006882,017411,017412,017413,017421,017433,017446,017452
  locator: All ten exact native application/product assertions compared against current
    official API records; current official GSRS identity parsed independently.
  accessed_at: '2026-10-21T18:13:23Z'
  support: supports
  summary: Product names, sponsors, ingredient, original approval dates and marketing
    fields all match. PRE-OP and PRE-OP II under NDA 017433 remain Prescription in
    the current API; the other eight products are Discontinued. Historical original-AP
    evidence is not erased by discontinued marketing. The APPROVED summary therefore
    has positive retained support, and no withdrawal finding is inferred. Seven additional
    returned applications lacked the qualifying original-approval data used by the
    maintained filter. An unrelated homeopathic label and an empty PHISOHEX DailyMed
    search were not used as evidence for these products.
  snapshot_sha256: c0376078ad230c16deecfa0aa7839b35e2cb78d36486b265ac8061be3f033c94
- evidence_id: agricultural-use
  kind: database
  reference: https://sitem.herts.ac.uk/aeru/ppdb/en/Reports/381.htm; Regulation (EC)
    2076/2002
  locator: PPDB chemical descriptors, use summary and current EU approval status inspected;
    historical regulation identifier and hexachlorophene entry checked through official
    indexed text, not a complete legal-history audit.
  accessed_at: '2026-10-21T18:05:19Z'
  support: supports
  summary: PPDB describes hexachlorophene as an obsolete agricultural agent once used
    as acaricide and fungicide and reports Not approved under the current EU plant-protection
    framework. This supports historical agricultural use and the stated EU boundary.
    It does not establish current use frequency in every jurisdiction, a universal
    prohibition, or a current clinical recommendation.
  snapshot_sha256: 3afcae77dc132c76e743a84c53812f3e3d587b56897e4024a83723718b5e0693
- evidence_id: documents
  kind: primary_source
  reference: https://patents.google.com/patent/US2250480A/en; https://patents.google.com/patent/US2435593A/en;
    https://patents.google.com/patent/US2812365A/en
  locator: Complete US2250480 description and claims read; opening process descriptions
    and selected examples of the latter two patents inspected. The Wikipedia document
    link is contextual, not experimental evidence.
  accessed_at: '2026-10-21T18:05:20Z'
  support: supports
  summary: The original patent describes the methylene-bridged trichlorophenol constitution
    and free-acid isolation, with salts treated separately. Later patents concern
    preparation and product isolation. These links are relevant documents, not exact
    molecular xrefs or modern clinical efficacy demonstrations. Historical product/process
    claims are not transferred into present-day safety or quantified antimicrobial
    outcomes.
  snapshot_sha256: 9c99f6bda85e7c359af582e052a031f7dbc00012b68cc6f403d9d5082c51e69c
- evidence_id: protein-grounding
  kind: authority
  reference: UniProtKB:P0C6U8; UniProtKB:P0DTD1; NCBITaxon:2901879; NCBITaxon:2697049
  locator: Complete reviewed UniProt records with processed-chain features and official
    NCBI taxonomy responses.
  accessed_at: '2026-10-21T18:05:20Z'
  support: supports
  summary: P0C6U8 is reviewed SARS coronavirus replicase polyprotein 1a with 3CL protease/nsp5
    residues 3241-3546. Its current UniProt taxon 694009 is a broader species lineage
    containing the native SARS-CoV taxon 2901879. P0DTD1 is reviewed SARS-CoV-2 polyprotein
    1ab, with nsp5 residues 3264-3569 and matching taxon 2697049. The assays use recombinant
    processed protease, not the full polyproteins; parent-accession grounding is not
    evidence that an entire polyprotein was experimentally assayed.
  snapshot_sha256: c24645f9215e405597a409e21491ac561e6bb6682f63ab12b989b7d7a167e93c
- evidence_id: bindingdb
  kind: database
  reference: https://www.bindingdb.org/rwd/bind/chemsearch/marvin/MolStructure.jsp?monomerid=31712;
    reactant sets 844294 and 844363; assays 8809_1 and 8814_1
  locator: Complete accessible ligand page and exact native raw measurement rows,
    cross-checked against original papers.
  accessed_at: '2026-10-21T18:05:52Z'
  support: supports
  summary: The ligand page matches the exact graph and retains both reaction-set identifiers
    and reported 4000 nM Ki and 21520 nM IC50. Database fidelity supports provenance
    but does not remove the original assay-interference qualification. The values
    remain kinetic/response measurements, not dissociation constants.
  snapshot_sha256: e15840104b34437bcb0b4395449ec12479835a8178dfd6c5d757bb9b9847ed20
- evidence_id: sars2005
  kind: primary_source
  reference: PMID:15950190; DOI:10.1016/j.bbrc.2005.05.095; https://pmc.ncbi.nlm.nih.gov/articles/PMC7092914/
  locator: Complete original main text, Methods, Results, Discussion and figure captions
    read; original figure images not independently reanalysed.
  accessed_at: '2026-10-21T18:05:51Z'
  support: supports
  summary: Recombinant SARS-CoV 3CL protease was expressed as an MBP fusion and released
    as a 306-residue enzyme. The FRET assay used a 20 nM enzyme preparation,30 µM
    substrate,25 degrees C and buffer containing 1 mM DTT, with a 15 min compound
    preincubation. Hexachlorophene gave a reported IC50 of 5 µM and competitive Ki
    of 4 µM, the latter matching native 4000 nM. Docking used a pre-existing structure
    and is computational, not an experimental drug-bound crystal. E. coli was the
    expression host, not the native assay target organism. These results do not by
    themselves establish cellular antiviral efficacy.
  snapshot_sha256: b5dc92a9242a854271b9d9a416ceb37e388c7be1632ffa00adc326f2d9f4af1e
- evidence_id: sars2020
  kind: primary_source
  reference: PMID:32803196; DOI:10.1101/2020.07.17.207019; https://pmc.ncbi.nlm.nih.gov/articles/PMC7427131/
  locator: Complete original preprint main text, both complete tables and Figure 5
    caption read, including fluorescence-product counter-screen Methods and Results.
  accessed_at: '2026-10-21T18:05:51Z'
  support: supports
  summary: The recombinant SARS-CoV-2 3CL FRET screen separately tested fluorescence
    quenching using the cleaved Edans-containing product without enzyme. Hexachlorophene
    appears in Table 2 among nine CPE-active quenching compounds, not the twenty-three
    minimally quenching hits in Table 1. Its reported IC50 is 21.52 µM, correctly
    converted to21520 nM in the native record. Table 2 also reports partial CPE protection
    and cytotoxicity; those whole-cell outcomes are distinct from the target assay.
    The authors warn that quenching and host-cell toxicity complicate interpretation.
    This primary preprint was not peer reviewed at posting; the subsequent published
    article preserves the relevant result.
  snapshot_sha256: 7a86fc82d8e42311e98b8d441a861dcb581e13ab25f186d1c89df67a2adf723e
- evidence_id: published2020
  kind: primary_source
  reference: PMID:33062953; DOI:10.1021/acsptsci.0c00108; https://pmc.ncbi.nlm.nih.gov/articles/PMC7507806/
  locator: Published Results paragraphs on quenching, Table 2 and Figure 5 caption
    inspected; article-linked Figure 5 independently viewed, especially panel f.
  accessed_at: '2026-10-21T18:07:29Z'
  support: supports
  summary: The published successor likewise places hexachlorophene in the quenching-compound
    table. Figure 5f shows enzyme-assay inhibition and a separate partial fluorescence-quenching
    response at higher concentrations. This supports retaining the measured association
    with a caveat; it does not prove that all observed inhibition is artifactual,
    that the molecule is inactive or that binding is absent. Table 2 gives CPE efficacy
    43.57%, whereas the caption says47.57%; no precise CPE efficacy is imported here.
    Neither inspected version establishes an orthogonal hexachlorophene protease measurement
    that removes this limitation.
  snapshot_sha256: e6a97d763be7122677297fa51828e9ed1fae0088edd0d233ebf57d00df2cd965
- evidence_id: adopted-leads
  kind: database
  reference: PMID:1133685; PMID:22313968; PMID:23251633; PMID:397166; PMID:894425;
    PMID:952574
  locator: Complete indexed abstracts for five adopted papers; bibliographic metadata
    only for the IARC monograph PMID 397166, which has no indexed abstract.
  accessed_at: '2026-10-21T18:05:20Z'
  support: context_only
  summary: PMID1133685 is colorimetric analysis of topical formulations. PMID22313968
    studies rat brain injury/CNPase context after hexachlorophene or cuprizone. PMID23251633
    concerns host KCNQ1/KCNE1 activation, not a bacterial target. PMID 397166 is a
    secondary IARC assessment rather than primary assay evidence. PMID894425 concerns
    infant exposure, pharmacokinetics and toxicity during soap bathing; it is not
    a pure-compound MIC or a current clinical recommendation. PMID952574 concerns
    rat biliary clearance and enterohepatic circulation. None establishes a natural
    producer or antibacterial causal chain.
  snapshot_sha256: a144c47c973c0b263ae847fca242366e3e637bcf1cc2d568c0058ceb5ef76e45
- evidence_id: host-channel
  kind: primary_source
  reference: PMID:23251633; DOI:10.1371/journal.pone.0051820; https://pmc.ncbi.nlm.nih.gov/articles/PMC3520906/
  locator: Selected original CHO-expression/electrophysiology Methods, relevant Results
    and Discussion read after the complete abstract; not a complete independent audit
    of every figure.
  accessed_at: '2026-10-21T18:05:51Z'
  support: context_only
  summary: The paper measures activation of mammalian KCNQ1/KCNE1 channels and reports
    an EC50 of 4.61±1.29 µM. It supports host pharmacology context, not bacterial
    membrane killing or approved treatment of long-QT syndrome. No such target is
    required merely because the literature exists.
  snapshot_sha256: ec6f889f1ccb3846f0ed73d4534f1b77b656e186514decf958b07faede0c2a89
- evidence_id: bacterial1971
  kind: primary_source
  reference: PMID:4107813; DOI:10.1128/jb.108.1.482-491.1971; https://pmc.ncbi.nlm.nih.gov/articles/PMC247089/
  locator: Original scanned pages 482-484 and 489-491 independently viewed, including
    material/method details, selected results and discussion. Pages485-488 were downloaded
    but not independently read.
  accessed_at: '2026-10-21T18:07:01Z'
  support: supports
  summary: The study uses supplier-identified hexachlorophene crystals, ethanol stocks
    and matched solvent controls against asporogenous Bacillus megaterium KM. Viability
    experiments and microscopy distinguish cell killing from higher-dose visible membrane
    injury. The approximate lethal threshold is 10 µg per mg cell dry weight, not10
    µg/mL or a standardized MIC. At the threshold, overt cytopathology was not observed;
    higher concentrations caused membrane/dye effects. The authors distinguish adsorption
    and observable damage from proof of the primary causal target. This is direct
    compound-specific antibacterial evidence, with explicit assay/material limits.
  snapshot_sha256: 8bb7b4b8cf91f70fd61f798c944f144ef01db8dec0f811721fd0c6d72ad149a8
- evidence_id: bacterial-mechanism
  kind: primary_source
  reference: PMID:10671494; DOI:10.1074/jbc.275.7.4654; PMID:11368521; DOI:10.1006/abbi.2001.2349;
    PMID:15273089; https://pmc.ncbi.nlm.nih.gov/articles/PMC478524/
  locator: Complete abstracts of the two purified-FabI studies; selected original
    2004 expression-study Methods, hexachlorophene Results, FabI-assay text and Discussion.
  accessed_at: '2026-10-21T18:07:01Z'
  support: supports
  summary: Purified FabI inhibition is reported, but the earlier S. aureus overexpression/mutant
    findings do not establish FabI as the whole-cell cause for hexachlorophene. The
    Haemophilus influenzae study reports an in vitro IC50 and acknowledges mechanistic
    ambiguity. The2004 B. subtilis 168 study finds a response distinct from the expected
    fatty-acid-synthesis inhibitor pattern and concludes that growth inhibition in
    that experiment did not follow the presumed FabI mechanism. Expression classification
    is not direct binding, and these differing evidence layers are not collapsed into
    a native causal chain.
  snapshot_sha256: 0c0bedcac57a70199b0c89587c5b5343837f09c386ef2f794e71e5a2be1d1663
- evidence_id: fungal
  kind: primary_source
  reference: PMID:32004725; DOI:10.1016/j.jgar.2020.01.002
  locator: Complete indexed original abstract only.
  accessed_at: '2026-10-21T18:05:52Z'
  support: supports
  summary: A screen of 1280 approved-drug-library compounds against six resistant
    filamentous fungal strains identifies hexachlorophene among broad growth-inhibitory
    hits. This supports bounded antifungal activity, while exact strain-level concentrations,
    material purity and full assay conditions were not checked at full-text depth.
    No MICs or target assignments are imported.
  snapshot_sha256: 1d693f449f470a7204844cf69fe62cd7b933985631d4322573cbe1a181f481a6
- evidence_id: adapter
  kind: database
  reference: 530-imodulondb-datasets.txt; shared structured source adapter
  locator: Dataset catalog run at 2026-10-21T18:05:00Z before protein-mechanism web
    follow-up.
  accessed_at: '2026-10-21T18:05:00Z'
  support: context_only
  summary: No covered SARS-CoV or SARS-CoV-2 dataset matched the two native target
    organisms. The adapter is therefore not applicable beyond this catalog check.
    Absence from the catalog is not negative biochemical or antiviral evidence.
  snapshot_sha256: 69de7daea0e635029ba57286ee0172c55ecab7580962ce8cb7a1c6ff8175f978
- evidence_id: search
  kind: search
  reference: 530-local-hits.txt; 530-owner-hits.txt; 530-adopted.json; 530-followup.json;
    530-fetch-results.json through530-fetch4-results.json
  locator: Initial exact identifier/label/slug search and actual-owner search included
    hidden and ignored files; bounded public chemical-authority, exact-name and cited-primary
    follow-up.
  accessed_at: '2026-10-21T18:05:52Z'
  support: context_only
  summary: All six adopted ChEBI leads and both retained BindingDB citations were
    dispositioned. Excluded BindingDB review and whole-cell leads were checked at
    abstract/database depth for their distinct scope. Public failures, challenge HTML
    and empty responses were preserved rather than treated as source text. This bounded
    review does not claim to identify every antimicrobial target, formulation or regulatory
    event.
  snapshot_sha256: 1d693f449f470a7204844cf69fe62cd7b933985631d4322573cbe1a181f481a6
  search_scope: 2026-10-21; hidden/ignored-inclusive repository identifier, label,
    slug, full-key and owner searches; bounded public Europe PMC, official chemical
    authority, FDA and exact-name primary searches. Full-text depth is stated separately
    for each inspected publication.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral molecule and chemical groundings
  outcome: supported
  summary: Native structure, formula and masses agree with independent authority encodings,
    CAS and original chemical context. All systematic synonyms and broader structural
    parents are compatible with the graph.
  target_ids:
  - CHEBI:5693
  evidence_ids:
  - native
  - chemistry
  - chebi
  - documents
- assessment_id: xref-access
  area: grounding
  topic: Remaining registry and document access limits
  outcome: unknown
  summary: No positive exact-identifier mismatch was found, but direct HMDB, LINCS,
    Reaxys and DrugBank content was not available at complete-source depth. Upstream
    attribution is retained without pretending every registry was independently verified.
  target_ids:
  - CHEBI:5693
  evidence_ids:
  - reference-boundaries
  - chemistry
  - documents
- assessment_id: clinical
  area: evidence
  topic: Ten FDA assertions and clinical summary
  outcome: supported
  summary: Current official data reproduce all ten assertions, including their distinct
    marketing flags. Two Prescription products remain positive current API support;
    discontinued products are not silently rewritten as never approved. Product use
    is not a general safety recommendation.
  target_ids:
  - CHEBI:5693
  evidence_ids:
  - fda
  - owners
- assessment_id: sars1
  area: evidence
  topic: Reported SARS-CoV Ki and protein grounding
  outcome: supported
  summary: The original paper reports Ki 4 µM for recombinant 3CL protease, matching
    the retained kinetic measurement. UniProt polyprotein accessions include the processed
    protease; the experiment did not assay the full polyprotein or prove cellular
    antiviral efficacy.
  target_ids:
  - CHEBI:5693
  evidence_ids:
  - sars2005
  - bindingdb
  - protein-grounding
- assessment_id: sars2
  area: evidence
  topic: Reported SARS-CoV-2 FRET IC50 and interference qualification
  outcome: concern
  summary: The reported 21.52 µM value and measured-association relation are correct,
    but the experimental context omits the original partial fluorescence-quenching
    qualification. The omission is bounded and does not justify deleting the measurement
    or denying binding.
  target_ids:
  - CHEBI:5693
  evidence_ids:
  - native
  - sars2020
  - published2020
  - bindingdb
- assessment_id: activity
  area: grounding
  topic: Antibacterial, antifungal and agricultural roles
  outcome: supported
  summary: Direct bacterial experiments support exact-compound activity; fungal screening
    and historical agricultural sources support the broader roles. Dose per cell mass,
    library-hit endpoints, historical uses and contemporary approval scope remain
    distinct.
  target_ids:
  - CHEBI:5693
  evidence_ids:
  - bacterial1971
  - fungal
  - agricultural-use
  - chebi
- assessment_id: mechanism
  area: evidence
  topic: Optional bacterial mechanism versus host and viral evidence
  outcome: unknown
  summary: The record does not assert a bacterial causal graph. Purified FabI inhibition,
    expression responses, high-dose membrane injury and host channel effects support
    different claims and should not be promoted into a single established bacterial
    mechanism. Viral targets can coexist with antibacterial filing without becoming
    bacterial targets.
  target_ids:
  - CHEBI:5693
  evidence_ids:
  - bacterial-mechanism
  - bacterial1971
  - host-channel
  - sars2005
  - sars2020
- assessment_id: provenance
  area: provenance
  topic: Source inputs, citation placement and history
  outcome: supported
  summary: Seventeen captured inputs retain the original thirteen hashes and include
    actual FDA/BindingDB owners. The source concept and nine history events are consistent
    with SEEDED status. Adopted leads are not treated as blanket evidence for the
    whole record.
  target_ids:
  - CHEBI:5693
  evidence_ids:
  - owners
  - native
  - adopted-leads
- assessment_id: coverage
  area: completeness
  topic: Optional representations and claim boundaries
  outcome: supported
  summary: No missing optional activity, resistance, producer, graph or dataset object
    is itself a defect. Any enrichment must retain exact material, target-chain, taxon,
    unit, assay-interference and endpoint scope; neither synthesis nor host exposure
    proves natural production.
  target_ids:
  - CHEBI:5693
  evidence_ids:
  - native
  - documents
  - bacterial1971
  - bacterial-mechanism
  - adapter
  - search
findings:
- finding_id: F1
  issue_key: hexachlorophene-sars2-fret-quenching-context
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Retain the fluorescence-quenching qualification with the SARS-CoV-2 FRET
    measurement
  description: The native 21520 nM IC50 correctly reproduces Table 2 of the adopted
    2020 preprint, but the target context and evidence notes omit that hexachlorophene
    is one of the partially fluorescence-quenching compounds. The published successor
    confirms that scope in Table 2 and Figure 5f. Because the record already uses
    MEASURED_TARGET_ASSOCIATION and does not assert direct binding, this is a non-blocking
    assay-context omission rather than a disproven measurement or established inactivity.
  target_ids:
  - CHEBI:5693
  field_paths:
  - molecular_targets[1].experimental_context
  - molecular_targets[1].evidence[0].notes
  evidence_ids:
  - native
  - owners
  - sars2020
  - published2020
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/bindingdb_target_measurements.tsv
    role: Adopted quantitative target source rows
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_bindingdb_targets.py
    role: Maintained extraction and assay qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Target evidence/context emission
  rule_id: 'Native review checklist: preserve original assay limitations and attach
    evidence to the narrowest supported claim'
  native_severity: minor
  normalization_reason: The exact compound, target-associated response and reported
    numerical value are preserved. The missing experimental caveat weakens interpretation
    without establishing a wrong identity, false numerical value or direct-binding
    overclaim.
actions:
- action_id: A1
  description: Add the source-supported quenching qualification through a maintained
    target-context overlay or extraction path, retaining the reported measurement.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:5693
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/bindingdb_target_measurements.tsv
    role: Adopted quantitative target source rows
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_bindingdb_targets.py
    role: Maintained extraction and assay qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Target evidence/context emission
  acceptance_checks:
  - Retain the reported IC50 of 21520 nM, qualifier, BindingDB identifiers and measured-association
    relation; do not recast it as Kd or delete it solely because of partial quenching.
  - State in experimental context or evidence notes that the original counter-screen
    detected fluorescence quenching and therefore limits interpretation of the FRET
    result. Preserve any verbatim assay description rather than inserting interpretation
    into quoted source text.
  - Keep the SARS-CoV 2005 Ki independent from the SARS-CoV-2 counter-screen. If citing
    the published successor, preserve the original preprint provenance and distinguish
    recombinant processed protease from the parent polyprotein.
  - Regenerate the exact source-owned record and pass focused schema/strict, reference
    and corpus reproduction checks.
- action_id: A2
  description: If adding optional activity or bacterial mechanism evidence, keep the
    original material and assay boundaries.
  finding_ids: []
  target_ids:
  - CHEBI:5693
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/hexachlorophene.yaml
    role: Optional curator-owned scientific additions through the validated writer
  acceptance_checks:
  - Do not encode the 1971 dose in µg per mg cell dry weight as a µg/mL MIC or equate
    higher-dose membrane injury with the primary killing target.
  - Keep purified FabI assays, bacterial expression profiles, host channel activation,
    viral protease assays and clinical formulation records separate.
  - Preserve antifungal abstract-only limits and historical agricultural-use context;
    do not infer universal current use or regulatory approval from a product name.
limitations:
- The review is partial because several registry pages and full experimental details
  remain unavailable. HMDB was available only as indexed official text, LINCS returned
  an error, Reaxys was not directly inspected and DrugBank direct retrieval failed.
  These are access limits, not confirmed identity defects.
- The2005 primary and 2020 preprint main texts were read completely. The published
  2020 successor was checked in the relevant Results, Table 2 and Figure 5, whose
  image was independently viewed; unrelated supplemental experiments were not comprehensively
  reanalysed.
- The1971 paper was visually read on pages 482-484 and 489-491, not all ten pages.
  The two earlier purified-FabI studies and the 2020 fungal study were inspected at
  complete abstract depth only. The2004 expression study and 2012 host-channel paper
  were read selectively for the stated mechanistic scope.
- All six adopted ChEBI leads were dispositioned, but the 1979 IARC monograph had
  no indexed abstract and was not available at full-text depth. Analytical formulation,
  host toxicology and pharmacokinetic reports were not treated as microbial mechanism
  evidence.
- The preprint and published Table 2 report CPE efficacy 43.57%, whereas the corresponding
  Figure 5 caption says47.57%. This source inconsistency concerns a non-native whole-cell
  endpoint and was not transferred into a quantitative activity object.
- Current FDA API assertions and GSRS identity were checked, but this was not a comprehensive
  review of every historical regulatory notice or every marketed formulation. PPDB
  supports the current EU agricultural status; the complete legal history and contemporary
  global frequency of use were not audited.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Fetch manifests preserve actual URLs, UTC times, response failures and SHA256 values.
  All seventeen source input hashes were rechecked before draft output. Schema/strict/chemistry
  and independent comparisons are distinct from scientific assessment.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
