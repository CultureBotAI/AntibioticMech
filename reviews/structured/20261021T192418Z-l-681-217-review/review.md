# L-681,217: terminal alkene identity conflict and non-equivalent ChEBI grounding

- Review: 20261021T192418Z-l-681-217-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:53:57Z
- Finished UTC: 2026-10-21T19:24:18Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The adopted 1986 original and later direct characterization support the natural antibiotic, producer and elfamycin family. Both original structure figures show C31=C32 as Z, while native and current PubChem assert E. A one-bond diagnostic confirms a wrong stereoisomer, normalized as a blocker. Current asserted ChEBI omits every alkene geometry, creating a separate major exact-grounding mismatch. Later absolute stereochemical proposals, sodium-salt assays, free-acid assays and derivative-specific binding measurements retain their evidence boundaries.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Assigned queue position 580; one exact native record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-ca1f16372a | data/antibiotics/antibacterial/l-681-217.yaml | generated | L-681,217 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-ca1f16372a | Actual focused execution exited 0. Executed against batch058; chemistry used existing batch019 RDKit while schema/strict used batch058. Passing deterministic gates do not resolve the primary identity conflict. |
| Focused schema verification | passed | True | antibioticmech:aro-ca1f16372a | Actual focused execution exited 0. Executed against batch058; chemistry used existing batch019 RDKit while schema/strict used batch058. Passing deterministic gates do not resolve the primary identity conflict. |
| Focused strict verification | passed | True | antibioticmech:aro-ca1f16372a | Actual focused execution exited 0. Executed against batch058; chemistry used existing batch019 RDKit while schema/strict used batch058. Passing deterministic gates do not resolve the primary identity conflict. |
| Authoritative full QC | failed | True | antibioticmech:aro-ca1f16372a | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-ca1f16372a | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-ca1f16372a | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-ca1f16372a | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-ca1f16372a | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-ca1f16372a | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-ca1f16372a | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-ca1f16372a | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-ca1f16372a | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact natural structure versus stored molecular graph

identity: concern. Targets: antibioticmech:aro-ca1f16372a.

The graph parses and masses/formula/charge agree, but terminal C31=C32 is asserted E where independently inspected original 1986 and characterized2024 sources depict Z. This is a wrong geometric isomer despite current PubChem agreement. The ten unassigned tetrahedra require separate qualified adjudication of the 2024 relative/analogy-based proposals; absence of tags is not a racemate claim.

### Class, minted identifier and exact chemical links

grounding: concern. Targets: antibioticmech:aro-ca1f16372a.

ARO-minted identity and elfamycin parent are valid. PubChem matches the stored wrong graph, while asserted CHEBI201407 has no alkene geometry and cannot be exact-equivalent. A correction must reconcile both links against the adjudicated primary structure, rather than blindly importing either authority.

### Definition, adopted lead, producer and antibacterial eligibility

evidence: supported. Targets: antibioticmech:aro-ca1f16372a.

The sole adopted 1986 original was read completely and supports natural-product production and sodium-salt antibacterial zones, but not its appended BGC claim. Later2016 SI and2024 genomic/metabolomic evidence support that broad BGC statement with putative-function limits. Separate2024 parent-acid MICs support natural-compound eligibility. Quantitative salt/acid, strain, medium and derivative boundaries are preserved.

### Mechanistic and stereochemical enrichment boundaries

completeness: unknown. Targets: antibioticmech:aro-ca1f16372a.

The optional structured fields are absent without a schema violation. Direct original data can support bounded EF-Tu-dependent translation inhibition and assay-specific activity enrichment, but no derivative KD, universal GTPase effect, whole-pathogen EF-Tu susceptibility, or all-enzyme BGC validation should be imported. The ten tetrahedral assignments merit primary-qualified curation rather than automatic filling from family analogy.

### Source ownership and reproducibility

provenance: supported. Targets: antibioticmech:aro-ca1f16372a.

All original 13 and expanded 26 input hashes remain unchanged. ARO owns the named definition/class/xrefs; PubChem enrichment owns the stored graph. The full native history was read and is consistent with generation. Future fixes belong to maintained source/overlay handling and regeneration; no status promotion or native mutation occurred.

## Findings

### F1: The stored terminal E alkene denotes the wrong geometric isomer

blocker / open / confirmed; issue key: l-681217-terminal-alkene-wrong-geometry.

Native and adopted/current PubChem encode seven E alkenes. Original1986 Figure 5 and independently characterized2024 Figure 1/SI depict the distal terminal bond C31=C32 as Z. Native atoms 40–41 map directly to that bond; a one-bond diagnostic changes only /b9-7+ to /b9-7- and yields OSKAZZUZQORABG-QVHXHHNKSA-N. This establishes the wrong asserted geometry without requiring unqualified adoption of all ten later tetrahedral proposals.

### F2: CHEBI201407 lacks the alkene geometry required for exact equivalence

major / open / confirmed; issue key: l-681217-chebi-exact-stereo-mismatch.

Current CHEBI201407 has identical constitution but no specified alkene geometries, with key OSKAZZUZQORABG-UHFFFAOYSA-N. Native xrefs asserts chemical identity to a graph with seven defined alkenes. This mismatch is independently present before and after the terminal-Z repair; the ChEBI submitted all-E name does not repair its unspecified default graph.

## Recommended Actions And Acceptance Checks

### A1

Correct the terminal geometry through maintained structural ownership after primary adjudication, preserving separate tetrahedral uncertainty.

- Map the actual1986 Figure 5 and2024 Figure 1/SI C31=C32 bond to native atoms 40–41 and encode Z while retaining the six other E alkenes, formula and neutral molecular form.
- Treat the one-bond candidate key as a diagnostic, not a complete absolute-structure replacement. Review all ten2024 tetrahedral proposals with their ROESY-versus-analogy evidence before deciding what to encode.
- Implement a reproducible maintained-source or curator structural correction and regenerate SMILES/InChI/key together; do not patch generated YAML or infer racemic material from unspecified stereo.
- Recheck PubChem6439903 and all exact chemical xrefs against the adjudicated graph, then rerun focused and required corpus gates.

### A2

Resolve or qualify the ChEBI source link according to exact-structure semantics.

- Preserve ARO source provenance while preventing CHEBI201407 with unknown alkene geometry from being emitted as an exact chemical equivalent.
- Retain the observed ChEBI name-versus-graph discrepancy in source adjudication; do not substitute the no-stereo graph or its all-E name for primary geometry.
- Validate the repaired xref against the chosen exact stereochemical representation and rerun source/reference checks.

### A3

Optional evidence enrichment should separate the original activity/producer citation from later biosynthetic and mechanism evidence.

- Cite the later 2016/2024 cluster work for biosynthesis and preserve comparative/putative enzyme-function scope;1986 alone has no BGC experiment.
- Keep1986 sodium-salt diffusion zones distinct from2024 parent-acid MICs and combinations. Preserve actual strain identifiers and the BL21-versus-BW25113 mutant-background difference.
- Do not transfer derivative 10 KD, other elfamycin targets, hybrid-system pathogen susceptibility, or inferred absolute stereochemistry as unqualified parent observations. Missing optional fields alone require no correction.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/l-681-217.yaml; Entire native record, source concept and three seed/reseed history events | supports | The neutral C36H53NO10 ARO-minted record has seven E alkenes and ten unassigned tetrahedral centres. It asserts elfamycin classification, Streptomyces cattleya production, a characterized biosynthetic cluster, and exact ARO/ChEBI/PubChem links. There are no separate structured target, resistance, activity, producer, product or causal-graph objects; the definition claims are assessed below. The sole adopted lead is PMID3781906. |
| owners | data/raw/aro_antibiotics.tsv#ARO:3001258; Complete exact row 237, readiness row 2741 and actual ownership | context_only | The exact ARO row supplies the definition, broad class, ChEBI/PubChem links and sole PMID. Source target/resistance inventories have no exact matching row; no exact ChEBI, curator or decisions row was found. Broad parent-class results include other elfamycins and are not compound-specific evidence. Original 13 input hashes were retained and expanded to 26 before detailed judgment. |
| pubchem-owner | data/raw/pubchem_structures.tsv#pubchem.compound:6439903; Complete exact row 71 | context_only | The adopted enrichment row already contains the all-E graph and ten unspecified tetrahedra. Native generation preserved that representation, so the wrong terminal geometry is inherited from the structural source rather than a YAML transcription loss. |
| search | /private/tmp/am-review-session/580-context-search.txt; Preserved initial scan plus ignored-inclusive exact follow-up | context_only | Exact name, minted identifier, ARO molecule and broader class were searched with hidden and ignored files included. Negative source-row conclusions are confined to the inspected inventories; broader-class hits were not treated as exact evidence. |
| adapter | /private/tmp/am-review-session/580-adapter.json; Structured search before open primary research | context_only | The catalog had no S. cattleya dataset. The actual E. coli precise1k tufA query returned gene b3339 and zero components. This establishes only expression-database context; it supplies no L-681,217 binding, activity, producer or biosynthetic-cluster evidence. |
| aro | https://raw.githubusercontent.com/arpcard/aro/master/aro.obo; Exact ARO 3001258, 3001310 and 3001219 terms | supports | The molecule definition and PMID match adopted ownership. The kirromycin-like grouping and broader elfamycin parent are compatible with independent natural-product and EF-Tu experiments; native uses the broader valid class. This authority is not primary proof of biosynthesis or precise target action. |
| card | https://card.mcmaster.ca/ontology/37657; Resolved live molecule page, accession ARO3001258 | supports | The live CARD page resolves to L-681,217 and retains the source definition and chemical links. It is a database-tier identity/class comparison, not an independent experimental source. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6439903/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass/JSON; Exact current CID6439903 response | supports | Current PubChem reproduces native formula, neutral charge, mass, all-E alkene geometry and full key OSKAZZUZQORABG-UQKUNJBPSA-N. Its agreement with native is real, but both conflict with the primary terminal Z structure. Ten unspecified tetrahedra are not evidence of a racemate. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/201407/; Current CHEBI201407 default structure and submitted name | refutes | The two-star MetaboLights-origin term has the same connectivity and composition but no alkene stereochemistry at all: key OSKAZZUZQORABG-UHFFFAOYSA-N. Its submitted IUPAC name nevertheless says all-E. The chemical graph therefore cannot be an exact equivalent of native or the primary-supported Z form; the authority also contains a name-versus-graph annotation discrepancy. |
| adopted | PMID:3781906; DOI:10.7164/antibiotics.39.1361; Complete original main, pp1361–1367; actual p1365 tables and p1366 Figure 5 viewed | supports | The sole adopted original establishes S. cattleya ATCC39203 production and isolation of L-681,217. Fermentation ran 90 h at 28 °C, 400 rpm and 3 L/min aeration after seed stages. Acid extraction, sodium hydroxide back-extraction and preparative HPLC yielded purified sodium salt; the paper separately prepared free acid and methyl ester. These forms are not interchangeable quantitative assay materials. No biosynthetic gene-cluster experiment appears in this 1986 article. |
| original-structure | https://www.jstage.jst.go.jp/article/antibiotics1968/39/10/39_10_1361/_pdf; Actual Figure 5 compound 1, p1366, plus Table 2 p1365 | refutes | The original depicted constitution matches native, but its distal terminal diene bond is Z. The other six alkene geometries agree with native E. Figure 5 does not establish the ten absolute tetrahedra. The actual formula is C36H53NO10; a text-extraction artifact in the formula was checked against the printed table. |
| original-activity | PMID:3781906; Actual Table 3 p1365 and footnote, complete assay description | supports | The tested sodium salt was a 255 µg/mL solution in 10% aqueous methanol; 15 µL droplets delivered 3.825 µg onto seeded nutrient agar. Reported inhibition zones include B. subtilis ATCC6633 12 mm, M. luteus ATCC9341 25 mm, S. aureus ATCC6538P 10 mm and E. coli ATCC9637 17 mm; P. aeruginosa MB2824 had a 12 mm hazy zone, whereas P. stutzeri ATCC11607 and E. atroseptica ATCC4446 had zero. These are diffusion-zone endpoints, not MICs or evidence of uniform clinical spectrum. Exact inoculum and incubation were not specified locally. |
| mechanism1989 | PMID:2499247; DOI:10.1128/aac.33.3.322; Complete original four scanned pages322–325, including actual Figure 1 and Tables 1–3 | supports | The Roche-supplied L-681,217 preparation has no fully specified salt/purity in Methods. E. coli ATCC25922 poly(U)-directed poly(Phe) synthesis had EC50 0.4 µM for L-681,217; the EF-Tu-dependent GTPase assay had EC50 6.0 µM. S. aureus ATCC25923 poly(Phe) synthesis exceeded 1000 µM. The aurodox-specific hybrid assay and preincubation controls cannot be attributed numerically to L-681,217. The original Figure 1 also depicts the terminal Z alkene. |
| mechanism1989-method | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8744/171486/2141ee99022c/aac00071-0082.png; Actual pp322–324 Methods and Results | context_only | The E. coli poly(Phe) assay used a partially purified elongation-factor mixture, radiolabeled Phe-tRNA, poly(U), GTP and ribosomes at 37 °C for 5 min. The GTPase assay used purified E. coli EF-Tu plus ribosomes, radiolabeled GTP and a 10 min incubation at 30 °C. Its ribosome-containing endpoint differs from the later standalone steady-state EF-Tu assay; the two GTPase results should not be collapsed or treated as a simple contradiction. |
| biosynthesis2016 | PMID:27220410; DOI:10.1038/ja.2016.53; Accessible publisher opening paragraphs and full SI TablesS1–S2 text | context_only | The accessible main describes S. cattleya NBRC14057 grown on 5 L ISP2 agar for seven days and isolation of a new demethyl compound 1 alongside known compound 2. SI TableS1 gives separate NMR columns for demethyl-L-681,217 and parent L-681,217; TableS2 lists putative SCAT3572–3590 cluster functions and kir homolog comparisons. These support a biosynthetic assignment at the stated comparative level, not experimental proof of every enzyme or transfer of demethyl bioactivity. The rest of the main requires account access and was not read. |
| biosynthesis2024 | PMID:39568943; DOI:10.1039/d4sc04174g; Exact S. cattleya Results section, Figure 5 caption and actual Figure 5 | supports | Genomic/metabolomic work on S. cattleya NRRL8057 assigns Region 1.15 to the lca cluster and identifies L-681,217 as cattlemycin A (1a); isolated 1a was NMR-confirmed. Figure 5 distinguishes the parent from demethyl and methyl-ester congeners. This supports the broad native characterized-cluster statement through later evidence, without claiming every proposed metabolite or enzymatic step was individually validated. Absolute configurations are proposed from NOESY, bioinformatics and kirromycin comparison. Unrelated organism sections were not fully reviewed. |
| biosynthesis-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/899d/11752868/08412e1fcd1e/d4sc04174g-f5.jpg; Actual Figure 5a–d viewed | context_only | Region 1.15 is explicitly labelled L-681,217/cattlemycin, and panel c separately depicts cattlemycin A1a and D1d. The diagram is a source-specific cluster/metabolite assignment, not an inhibitory target map. |
| primary2024-material | PMID:39576948; DOI:10.1021/acs.biochem.4c00541; Complete scientific main and Methods; production/purification section | supports | S. cattleya ATCC35852 was grown in modified R5 at 30 °C with 24 h seed and 24 h production stages. XAD2 adsorption, ethyl acetate extraction, silica separation and lyophilization yielded the parent acid for characterization and assays, without the original sodium-hydroxide back-extraction. The authors observed same-mass isomers and increased isomerization after base exposure; their purification selected the main L-681,217 peak. This is not proof that every historical preparation had identical isomer composition. |
| primary2024-structure | PMID:39576948; Complete structural Results and actual Figure 1 compound 3; SI S9 and S20 viewed | refutes | The paper directly analyzes the terminal diene using J(H29,H30)&gt;15 Hz and ROESY H29/H31, H30/H33 and strong H31/H32 contacts. Figure 1 and SI S9 depict C29=C30 E and C31=C32 Z, corroborating the 1986 figure. The authors propose ten tetrahedral configurations from relative ROESY relationships plus analogy to crystallographically characterized aurodox/kirromycin; they do not report an L-681,217 absolute-structure crystal. Those inferential assignments must remain qualified. |
| primary2024-si | https://ndownloader.figshare.com/files/50724695; SI S2–S5, parent/derivative characterization S9–S11 and actual S9/S20 | supports | The legitimate ACS Figshare supplement was recovered after direct ACS/PMC routes failed. S2 identifies M. catarrhalis ATCC8176, E. hirae NRRL B-1295 and BW25113-derived Keio mutants JW0451/JW0452/JW0940/JW5503. The main table also includes BL21, so mutant-to-BL21 differences are not a clean isogenic deletion comparison. Actual S9 depicts parent3 separately from NHS ester9; S20 ROESY was viewed, without raw-FID reprocessing or independent absolute stereochemical determination. |
| primary2024-activity | PMID:39576948; Actual main Table 1 and MIC Methods, with SI strain table | supports | Parent L-681,217 MICs are 1 µg/mL for E. hirae, 0.016 for M. catarrhalis, 128 for E. coli BL21 and ΔtolC, 32 for ΔacrA/ΔacrB and 64 for ΔompA. BL21 combinations with colistin 1.1 µg/mL or PAβN 15.6 µg/mL yield 0.5 or 4 µg/mL, respectively; these are combination outcomes. Main MIC Methods delegates the base protocol to reference27, so exact inoculum, assay medium and incubation are not independently resolved here. These assays establish conditional antibacterial eligibility of the natural parent, not of the native wrong terminal isomer. |
| primary2024-mechanism | PMID:39576948; Full biochemical Methods/Results, actual Tables 1–2 and Figure 4 | supports | Parent L-681,217 inhibits E. coli sfGFP cell-free synthesis with IC50 15 µM, versus 12 for kirromycin, and produces a distinct EF-Tu native-gel shift. It shows negligible standalone EF-Tu GTPase enhancement over 0–200 µM in the coupled steady-state assay, unlike kirromycin. The 1989 GTPase assay included ribosomes and used a different endpoint. PurA inhibition by L-681,217 is marginal; the aurodox/kirromycin PurA result is not a parent target claim. |
| derivative-boundary | PMID:39576948; Figures 6–8 captions and complete surrounding text/Methods | context_only | BLI KD 138 µM belongs to biotin-PEG derivative 10, not the parent. An incompletely EF-Tu-drained cell-free system gives model-derived parent Ki 7.4 µM, KM 2.4 µM and alpha 1.1; these are kinetic-system parameters, not a direct parent equilibrium KD. Recombinant A375T and mixed-protein experiments show conditional susceptibility differences in this cell-free system, not clinical mutation prevalence. Heterologous A. baumannii/K. pneumoniae/P. aeruginosa EF-Tu tests use an E. coli hybrid system and are not whole-cell MICs for those pathogens. |
| mapping | /private/tmp/am-review-session/580-map.py; 019 RDKit2026.03.5 run against batch058; all native/current encodings and one-bond candidate | supports | Native and current PubChem SMILES/InChI agree. Primary C27/C29/C30/C31/C32/C33 map to native zero-based atoms 36/38/39/40/41/42. Bond40 between atoms 40–41 is E, with priority substituents39 and42; switching only that bond to Z gives OSKAZZUZQORABG-QVHXHHNKSA-N and InChI /b9-7- instead of /b9-7+. Composition, neutral charge and all ten unassigned tetrahedra remain unchanged; six other alkenes remain E. ChEBI encodings omit all seven. This diagnostic is not a native replacement or an assertion that the partial candidate exhausts natural stereochemistry. |
| access | /private/tmp/am-review-session/580-fetch6.json; Actual public-source access and preserved failures | context_only | The adopted 1986 PDF, all four 1989 scan pages, 2024 ACS main/figures/SI and relevant RSC section/figure were obtained. The 2016 main was only partly readable, but its original SI was downloaded. EPMC ACS XML failed500, direct ACS SI returned403, PMC SI returned challenge HTML, and EPMC supplementary returned XML rather than a PDF/ZIP; an early guessed Figshare file returned empty202 and was never evidence. The resolved publisher DOI-to-Figshare route supplied the genuine SI. |

## Limits And Additional Notes

- The sole adopted 1986 paper was read in full, with actual Table 2/Table 3 and Figure 5 viewed. The complete four-page1989 scan was read. The2024 ACS scientific main and Methods were fully read; actual Figures 1/4, Tables 1/2 and SI S9/S20 were viewed. Other plots were assessed through source text/captions, not independently remeasured.
- The2024 SI strain/material sections S2–S5 and chemical characterization S9–S11 were read; raw FIDs were not reprocessed. Exact MIC inoculum, assay medium and incubation remain delegated to the source-cited protocol and were not independently recovered. Numeric results are retained with that boundary.
- The2016 publisher main was available only as opening paragraphs; its full SI TablesS1–S2 were read as text, but original spectral images were not independently interpreted. The RSC study was read only for its exact S. cattleya section, relevant references and actual Figure 5, not all unrelated metabolomic discoveries.
- Absolute tetrahedral assignments in2024 rely partly on analogy to other elfamycins. This review confirms the terminal alkene conflict without presenting a final-product crystal or independently established absolute hand. Historical salt preparations and possible isomerization are not assumed identical to the later isolated acid.
- Some scratch filenames contain2025 because of the PMC release context; the ACS source itself is correctly identified as the 2024 publication PMID39576948/DOI10.1021/acs.biochem.4c00541. Failed and guessed retrieval routes remain in manifests but are not evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All original 13 and expanded 26 source input hashes were verified unchanged at draft writing. No native/source/history/progress/saved-bundle/Git writes occurred.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T192418Z-l-681-217-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'L-681,217: terminal alkene identity conflict and non-equivalent ChEBI grounding'
started_at: '2026-10-21T18:53:57Z'
finished_at: '2026-10-21T19:24:18Z'
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
summary: The adopted 1986 original and later direct characterization support the natural
  antibiotic, producer and elfamycin family. Both original structure figures show
  C31=C32 as Z, while native and current PubChem assert E. A one-bond diagnostic confirms
  a wrong stereoisomer, normalized as a blocker. Current asserted ChEBI omits every
  alkene geometry, creating a separate major exact-grounding mismatch. Later absolute
  stereochemical proposals, sodium-salt assays, free-acid assays and derivative-specific
  binding measurements retain their evidence boundaries.
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
  - path: data/antibiotics/antibacterial/l-681-217.yaml
    sha256: 3d61e5539fe2f48cbd3f963951ad16e3dfa54bfe3bef34b66ae377aec75c2468
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
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
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
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
    role: context
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
targets:
- target_id: antibioticmech:aro-ca1f16372a
  path: data/antibiotics/antibacterial/l-681-217.yaml
  label: L-681,217
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO molecule identity, classification, structure and citation owner
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: ARO classification and source merge rules
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure enrichment transform
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Assigned queue position 580; one exact native record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-ca1f16372a
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0. Executed against batch058; chemistry
    used existing batch019 RDKit while schema/strict used batch058. Passing deterministic
    gates do not resolve the primary identity conflict.
  target_ids:
  - antibioticmech:aro-ca1f16372a
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    580
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against batch058; chemistry
    used existing batch019 RDKit while schema/strict used batch058. Passing deterministic
    gates do not resolve the primary identity conflict.
  target_ids:
  - antibioticmech:aro-ca1f16372a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/l-681-217.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against batch058; chemistry
    used existing batch019 RDKit while schema/strict used batch058. Passing deterministic
    gates do not resolve the primary identity conflict.
  target_ids:
  - antibioticmech:aro-ca1f16372a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/l-681-217.yaml --out /private/tmp/am-review-session/580-strict.tsv
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
  - antibioticmech:aro-ca1f16372a
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
  - antibioticmech:aro-ca1f16372a
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
  - antibioticmech:aro-ca1f16372a
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
  - antibioticmech:aro-ca1f16372a
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
  - antibioticmech:aro-ca1f16372a
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
  - antibioticmech:aro-ca1f16372a
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
  - antibioticmech:aro-ca1f16372a
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
  - antibioticmech:aro-ca1f16372a
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
  - antibioticmech:aro-ca1f16372a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/l-681-217.yaml
  locator: Entire native record, source concept and three seed/reseed history events
  accessed_at: '2026-10-21T19:14:07Z'
  support: supports
  summary: The neutral C36H53NO10 ARO-minted record has seven E alkenes and ten unassigned
    tetrahedral centres. It asserts elfamycin classification, Streptomyces cattleya
    production, a characterized biosynthetic cluster, and exact ARO/ChEBI/PubChem
    links. There are no separate structured target, resistance, activity, producer,
    product or causal-graph objects; the definition claims are assessed below. The
    sole adopted lead is PMID3781906.
  snapshot_sha256: 3d61e5539fe2f48cbd3f963951ad16e3dfa54bfe3bef34b66ae377aec75c2468
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv#ARO:3001258
  locator: Complete exact row 237, readiness row 2741 and actual ownership
  accessed_at: '2026-10-21T19:14:07Z'
  support: context_only
  summary: The exact ARO row supplies the definition, broad class, ChEBI/PubChem links
    and sole PMID. Source target/resistance inventories have no exact matching row;
    no exact ChEBI, curator or decisions row was found. Broad parent-class results
    include other elfamycins and are not compound-specific evidence. Original 13 input
    hashes were retained and expanded to 26 before detailed judgment.
  snapshot_sha256: a195299f467a3b7d3373900f6b51cd40ec53dafcee18b71ee641a90af670c429
- evidence_id: pubchem-owner
  kind: record_content
  reference: data/raw/pubchem_structures.tsv#pubchem.compound:6439903
  locator: Complete exact row 71
  accessed_at: '2026-10-21T19:14:07Z'
  support: context_only
  summary: The adopted enrichment row already contains the all-E graph and ten unspecified
    tetrahedra. Native generation preserved that representation, so the wrong terminal
    geometry is inherited from the structural source rather than a YAML transcription
    loss.
  snapshot_sha256: 4806fcf65f1574233b3b17b0f057f3e1a87131ef2803b277629c48eb95031add
- evidence_id: search
  kind: search
  reference: /private/tmp/am-review-session/580-context-search.txt
  locator: Preserved initial scan plus ignored-inclusive exact follow-up
  accessed_at: '2026-10-21T19:14:07Z'
  support: context_only
  summary: Exact name, minted identifier, ARO molecule and broader class were searched
    with hidden and ignored files included. Negative source-row conclusions are confined
    to the inspected inventories; broader-class hits were not treated as exact evidence.
  snapshot_sha256: 9ba5a3dae4139be1b98ba15240ff6bd2e80e0fe91ddc9cc7bdf06950e6298e2f
  search_scope: Initial 580-local-hits plus rg --no-ignore --hidden across curation,
    conf, scripts and data/raw.
- evidence_id: adapter
  kind: search
  reference: /private/tmp/am-review-session/580-adapter.json
  locator: Structured search before open primary research
  accessed_at: '2026-10-21T19:14:07Z'
  support: context_only
  summary: The catalog had no S. cattleya dataset. The actual E. coli precise1k tufA
    query returned gene b3339 and zero components. This establishes only expression-database
    context; it supplies no L-681,217 binding, activity, producer or biosynthetic-cluster
    evidence.
  snapshot_sha256: 76192a4521c8e4c5a9af214f397a60be256e0e21a38f702105b79db69f418dc6
  search_scope: Existing catalog456460; actual kg-microbe-sources imodulondb --timeout
    15 search --organism e_coli --dataset precise1k --query tufA, exit 0.
- evidence_id: aro
  kind: authority
  reference: https://raw.githubusercontent.com/arpcard/aro/master/aro.obo
  locator: Exact ARO 3001258, 3001310 and 3001219 terms
  accessed_at: '2026-10-21T15:57:42Z'
  support: supports
  summary: The molecule definition and PMID match adopted ownership. The kirromycin-like
    grouping and broader elfamycin parent are compatible with independent natural-product
    and EF-Tu experiments; native uses the broader valid class. This authority is
    not primary proof of biosynthesis or precise target action.
  snapshot_sha256: 4273073b4f4655d14846d901ee24ffd0eb8231f32171198091280152e13b9336
- evidence_id: card
  kind: authority
  reference: https://card.mcmaster.ca/ontology/37657
  locator: Resolved live molecule page, accession ARO3001258
  accessed_at: '2026-10-21T19:07:02.148302Z'
  support: supports
  summary: The live CARD page resolves to L-681,217 and retains the source definition
    and chemical links. It is a database-tier identity/class comparison, not an independent
    experimental source.
  snapshot_sha256: af789eef76b89cae40106324ff7fad928245d9b02e528c1a54ca16daa939c4f9
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6439903/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass/JSON
  locator: Exact current CID6439903 response
  accessed_at: '2026-10-21T19:06:49.111281Z'
  support: supports
  summary: Current PubChem reproduces native formula, neutral charge, mass, all-E
    alkene geometry and full key OSKAZZUZQORABG-UQKUNJBPSA-N. Its agreement with native
    is real, but both conflict with the primary terminal Z structure. Ten unspecified
    tetrahedra are not evidence of a racemate.
  snapshot_sha256: 6ac378db031e21eb80ecadbd1428d20046e0ebfb3397f18f8002377763ae74a6
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/201407/
  locator: Current CHEBI201407 default structure and submitted name
  accessed_at: '2026-10-21T19:06:49.112402Z'
  support: refutes
  summary: 'The two-star MetaboLights-origin term has the same connectivity and composition
    but no alkene stereochemistry at all: key OSKAZZUZQORABG-UHFFFAOYSA-N. Its submitted
    IUPAC name nevertheless says all-E. The chemical graph therefore cannot be an
    exact equivalent of native or the primary-supported Z form; the authority also
    contains a name-versus-graph annotation discrepancy.'
  snapshot_sha256: ca8c9c30f9f97bba818bd79c844f406ac62069fb94d0a0ee6dcdddea5033e367
- evidence_id: adopted
  kind: primary_source
  reference: PMID:3781906; DOI:10.7164/antibiotics.39.1361
  locator: Complete original main, pp1361–1367; actual p1365 tables and p1366 Figure
    5 viewed
  accessed_at: '2026-10-21T14:40:25.586394Z'
  support: supports
  summary: The sole adopted original establishes S. cattleya ATCC39203 production
    and isolation of L-681,217. Fermentation ran 90 h at 28 °C, 400 rpm and 3 L/min
    aeration after seed stages. Acid extraction, sodium hydroxide back-extraction
    and preparative HPLC yielded purified sodium salt; the paper separately prepared
    free acid and methyl ester. These forms are not interchangeable quantitative assay
    materials. No biosynthetic gene-cluster experiment appears in this 1986 article.
  snapshot_sha256: b2904f46382e4907d593e11b454ea4a825d07211bef16238d334df7da5149592
- evidence_id: original-structure
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/antibiotics1968/39/10/39_10_1361/_pdf
  locator: Actual Figure 5 compound 1, p1366, plus Table 2 p1365
  accessed_at: '2026-10-21T14:40:25.586394Z'
  support: refutes
  summary: The original depicted constitution matches native, but its distal terminal
    diene bond is Z. The other six alkene geometries agree with native E. Figure 5
    does not establish the ten absolute tetrahedra. The actual formula is C36H53NO10;
    a text-extraction artifact in the formula was checked against the printed table.
  snapshot_sha256: b2904f46382e4907d593e11b454ea4a825d07211bef16238d334df7da5149592
- evidence_id: original-activity
  kind: primary_source
  reference: PMID:3781906
  locator: Actual Table 3 p1365 and footnote, complete assay description
  accessed_at: '2026-10-21T14:40:25.586394Z'
  support: supports
  summary: The tested sodium salt was a 255 µg/mL solution in 10% aqueous methanol;
    15 µL droplets delivered 3.825 µg onto seeded nutrient agar. Reported inhibition
    zones include B. subtilis ATCC6633 12 mm, M. luteus ATCC9341 25 mm, S. aureus
    ATCC6538P 10 mm and E. coli ATCC9637 17 mm; P. aeruginosa MB2824 had a 12 mm hazy
    zone, whereas P. stutzeri ATCC11607 and E. atroseptica ATCC4446 had zero. These
    are diffusion-zone endpoints, not MICs or evidence of uniform clinical spectrum.
    Exact inoculum and incubation were not specified locally.
  snapshot_sha256: b2904f46382e4907d593e11b454ea4a825d07211bef16238d334df7da5149592
- evidence_id: mechanism1989
  kind: primary_source
  reference: PMID:2499247; DOI:10.1128/aac.33.3.322
  locator: Complete original four scanned pages322–325, including actual Figure 1
    and Tables 1–3
  accessed_at: '2026-10-21T19:10:39.536453Z'
  support: supports
  summary: The Roche-supplied L-681,217 preparation has no fully specified salt/purity
    in Methods. E. coli ATCC25922 poly(U)-directed poly(Phe) synthesis had EC50 0.4
    µM for L-681,217; the EF-Tu-dependent GTPase assay had EC50 6.0 µM. S. aureus
    ATCC25923 poly(Phe) synthesis exceeded 1000 µM. The aurodox-specific hybrid assay
    and preincubation controls cannot be attributed numerically to L-681,217. The
    original Figure 1 also depicts the terminal Z alkene.
  snapshot_sha256: 749a788d09cdcead1812d35434dd78923f657e4a22db8aa62aa4a11ea3760c9e
- evidence_id: mechanism1989-method
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8744/171486/2141ee99022c/aac00071-0082.png
  locator: Actual pp322–324 Methods and Results
  accessed_at: '2026-10-21T19:10:39.533102Z'
  support: context_only
  summary: The E. coli poly(Phe) assay used a partially purified elongation-factor
    mixture, radiolabeled Phe-tRNA, poly(U), GTP and ribosomes at 37 °C for 5 min.
    The GTPase assay used purified E. coli EF-Tu plus ribosomes, radiolabeled GTP
    and a 10 min incubation at 30 °C. Its ribosome-containing endpoint differs from
    the later standalone steady-state EF-Tu assay; the two GTPase results should not
    be collapsed or treated as a simple contradiction.
  snapshot_sha256: fd00f3381aa7a4d1be1c27d686f00578d9f535e9127ab336e17e8813ec8d5eca
- evidence_id: biosynthesis2016
  kind: primary_source
  reference: PMID:27220410; DOI:10.1038/ja.2016.53
  locator: Accessible publisher opening paragraphs and full SI TablesS1–S2 text
  accessed_at: '2026-10-21T19:10:39.542439Z'
  support: context_only
  summary: The accessible main describes S. cattleya NBRC14057 grown on 5 L ISP2 agar
    for seven days and isolation of a new demethyl compound 1 alongside known compound
    2. SI TableS1 gives separate NMR columns for demethyl-L-681,217 and parent L-681,217;
    TableS2 lists putative SCAT3572–3590 cluster functions and kir homolog comparisons.
    These support a biosynthetic assignment at the stated comparative level, not experimental
    proof of every enzyme or transfer of demethyl bioactivity. The rest of the main
    requires account access and was not read.
  snapshot_sha256: 6cf19654dd3b358470201ed6448e066a2c45bb6f0262191e091710880ac28b27
- evidence_id: biosynthesis2024
  kind: primary_source
  reference: PMID:39568943; DOI:10.1039/d4sc04174g
  locator: Exact S. cattleya Results section, Figure 5 caption and actual Figure 5
  accessed_at: '2026-10-21T19:07:02.143569Z'
  support: supports
  summary: Genomic/metabolomic work on S. cattleya NRRL8057 assigns Region 1.15 to
    the lca cluster and identifies L-681,217 as cattlemycin A (1a); isolated 1a was
    NMR-confirmed. Figure 5 distinguishes the parent from demethyl and methyl-ester
    congeners. This supports the broad native characterized-cluster statement through
    later evidence, without claiming every proposed metabolite or enzymatic step was
    individually validated. Absolute configurations are proposed from NOESY, bioinformatics
    and kirromycin comparison. Unrelated organism sections were not fully reviewed.
  snapshot_sha256: 3b7015d975ee90d94b06047e15ac579dd86722b4284b102c9b83749b8edb67aa
- evidence_id: biosynthesis-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/899d/11752868/08412e1fcd1e/d4sc04174g-f5.jpg
  locator: Actual Figure 5a–d viewed
  accessed_at: '2026-10-21T19:10:39.858180Z'
  support: context_only
  summary: Region 1.15 is explicitly labelled L-681,217/cattlemycin, and panel c separately
    depicts cattlemycin A1a and D1d. The diagram is a source-specific cluster/metabolite
    assignment, not an inhibitory target map.
  snapshot_sha256: ae2a33a2e8f64af413406f9afca631af542dc607e32a5fff2a5635375ec724b2
- evidence_id: primary2024-material
  kind: primary_source
  reference: PMID:39576948; DOI:10.1021/acs.biochem.4c00541
  locator: Complete scientific main and Methods; production/purification section
  accessed_at: '2026-10-21T19:07:21.258946Z'
  support: supports
  summary: S. cattleya ATCC35852 was grown in modified R5 at 30 °C with 24 h seed
    and 24 h production stages. XAD2 adsorption, ethyl acetate extraction, silica
    separation and lyophilization yielded the parent acid for characterization and
    assays, without the original sodium-hydroxide back-extraction. The authors observed
    same-mass isomers and increased isomerization after base exposure; their purification
    selected the main L-681,217 peak. This is not proof that every historical preparation
    had identical isomer composition.
  snapshot_sha256: 1c90b3895f24d1f4fe455ec0b4d54fed1707d9456d235d2ac0a461056316a92d
- evidence_id: primary2024-structure
  kind: primary_source
  reference: PMID:39576948
  locator: Complete structural Results and actual Figure 1 compound 3; SI S9 and S20
    viewed
  accessed_at: '2026-10-21T19:07:58.248245Z'
  support: refutes
  summary: The paper directly analyzes the terminal diene using J(H29,H30)>15 Hz and
    ROESY H29/H31, H30/H33 and strong H31/H32 contacts. Figure 1 and SI S9 depict
    C29=C30 E and C31=C32 Z, corroborating the 1986 figure. The authors propose ten
    tetrahedral configurations from relative ROESY relationships plus analogy to crystallographically
    characterized aurodox/kirromycin; they do not report an L-681,217 absolute-structure
    crystal. Those inferential assignments must remain qualified.
  snapshot_sha256: 492e0a91657ed96b6ce1a6e0ef2dc812f131378f808509cbaf807975301543c3
- evidence_id: primary2024-si
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/50724695
  locator: SI S2–S5, parent/derivative characterization S9–S11 and actual S9/S20
  accessed_at: '2026-10-21T19:11:14.462454Z'
  support: supports
  summary: The legitimate ACS Figshare supplement was recovered after direct ACS/PMC
    routes failed. S2 identifies M. catarrhalis ATCC8176, E. hirae NRRL B-1295 and
    BW25113-derived Keio mutants JW0451/JW0452/JW0940/JW5503. The main table also
    includes BL21, so mutant-to-BL21 differences are not a clean isogenic deletion
    comparison. Actual S9 depicts parent3 separately from NHS ester9; S20 ROESY was
    viewed, without raw-FID reprocessing or independent absolute stereochemical determination.
  snapshot_sha256: 02d2942a17efeb293124459387c0fa7315dca860e4ae295c9ac4d6109857017d
- evidence_id: primary2024-activity
  kind: primary_source
  reference: PMID:39576948
  locator: Actual main Table 1 and MIC Methods, with SI strain table
  accessed_at: '2026-10-21T19:07:21.258946Z'
  support: supports
  summary: Parent L-681,217 MICs are 1 µg/mL for E. hirae, 0.016 for M. catarrhalis,
    128 for E. coli BL21 and ΔtolC, 32 for ΔacrA/ΔacrB and 64 for ΔompA. BL21 combinations
    with colistin 1.1 µg/mL or PAβN 15.6 µg/mL yield 0.5 or 4 µg/mL, respectively;
    these are combination outcomes. Main MIC Methods delegates the base protocol to
    reference27, so exact inoculum, assay medium and incubation are not independently
    resolved here. These assays establish conditional antibacterial eligibility of
    the natural parent, not of the native wrong terminal isomer.
  snapshot_sha256: 1c90b3895f24d1f4fe455ec0b4d54fed1707d9456d235d2ac0a461056316a92d
- evidence_id: primary2024-mechanism
  kind: primary_source
  reference: PMID:39576948
  locator: Full biochemical Methods/Results, actual Tables 1–2 and Figure 4
  accessed_at: '2026-10-21T19:07:21.258946Z'
  support: supports
  summary: Parent L-681,217 inhibits E. coli sfGFP cell-free synthesis with IC50 15
    µM, versus 12 for kirromycin, and produces a distinct EF-Tu native-gel shift.
    It shows negligible standalone EF-Tu GTPase enhancement over 0–200 µM in the coupled
    steady-state assay, unlike kirromycin. The 1989 GTPase assay included ribosomes
    and used a different endpoint. PurA inhibition by L-681,217 is marginal; the aurodox/kirromycin
    PurA result is not a parent target claim.
  snapshot_sha256: 1c90b3895f24d1f4fe455ec0b4d54fed1707d9456d235d2ac0a461056316a92d
- evidence_id: derivative-boundary
  kind: primary_source
  reference: PMID:39576948
  locator: Figures 6–8 captions and complete surrounding text/Methods
  accessed_at: '2026-10-21T19:07:21.258946Z'
  support: context_only
  summary: BLI KD 138 µM belongs to biotin-PEG derivative 10, not the parent. An incompletely
    EF-Tu-drained cell-free system gives model-derived parent Ki 7.4 µM, KM 2.4 µM
    and alpha 1.1; these are kinetic-system parameters, not a direct parent equilibrium
    KD. Recombinant A375T and mixed-protein experiments show conditional susceptibility
    differences in this cell-free system, not clinical mutation prevalence. Heterologous
    A. baumannii/K. pneumoniae/P. aeruginosa EF-Tu tests use an E. coli hybrid system
    and are not whole-cell MICs for those pathogens.
  snapshot_sha256: 1c90b3895f24d1f4fe455ec0b4d54fed1707d9456d235d2ac0a461056316a92d
- evidence_id: mapping
  kind: validation
  reference: /private/tmp/am-review-session/580-map.py
  locator: 019 RDKit2026.03.5 run against batch058; all native/current encodings and
    one-bond candidate
  accessed_at: '2026-10-21T19:14:07Z'
  support: supports
  summary: Native and current PubChem SMILES/InChI agree. Primary C27/C29/C30/C31/C32/C33
    map to native zero-based atoms 36/38/39/40/41/42. Bond40 between atoms 40–41 is
    E, with priority substituents39 and42; switching only that bond to Z gives OSKAZZUZQORABG-QVHXHHNKSA-N
    and InChI /b9-7- instead of /b9-7+. Composition, neutral charge and all ten unassigned
    tetrahedra remain unchanged; six other alkenes remain E. ChEBI encodings omit
    all seven. This diagnostic is not a native replacement or an assertion that the
    partial candidate exhausts natural stereochemistry.
  snapshot_sha256: 39b51cd33b096f4ae73c22706a4033926c439f00dfe3675127edc287fefc7624
- evidence_id: access
  kind: validation
  reference: /private/tmp/am-review-session/580-fetch6.json
  locator: Actual public-source access and preserved failures
  accessed_at: '2026-10-21T19:14:07Z'
  support: context_only
  summary: The adopted 1986 PDF, all four 1989 scan pages, 2024 ACS main/figures/SI
    and relevant RSC section/figure were obtained. The 2016 main was only partly readable,
    but its original SI was downloaded. EPMC ACS XML failed500, direct ACS SI returned403,
    PMC SI returned challenge HTML, and EPMC supplementary returned XML rather than
    a PDF/ZIP; an early guessed Figshare file returned empty202 and was never evidence.
    The resolved publisher DOI-to-Figshare route supplied the genuine SI.
  snapshot_sha256: 262e233686b47756611a9ea4c3ab4bda4efd99e76e0220b79f95993389752738
assessments:
- assessment_id: identity
  area: identity
  topic: Exact natural structure versus stored molecular graph
  outcome: concern
  summary: The graph parses and masses/formula/charge agree, but terminal C31=C32
    is asserted E where independently inspected original 1986 and characterized2024
    sources depict Z. This is a wrong geometric isomer despite current PubChem agreement.
    The ten unassigned tetrahedra require separate qualified adjudication of the 2024
    relative/analogy-based proposals; absence of tags is not a racemate claim.
  target_ids:
  - antibioticmech:aro-ca1f16372a
  evidence_ids:
  - native
  - pubchem-owner
  - original-structure
  - primary2024-structure
  - mapping
- assessment_id: grounding
  area: grounding
  topic: Class, minted identifier and exact chemical links
  outcome: concern
  summary: ARO-minted identity and elfamycin parent are valid. PubChem matches the
    stored wrong graph, while asserted CHEBI201407 has no alkene geometry and cannot
    be exact-equivalent. A correction must reconcile both links against the adjudicated
    primary structure, rather than blindly importing either authority.
  target_ids:
  - antibioticmech:aro-ca1f16372a
  evidence_ids:
  - aro
  - card
  - pubchem
  - chebi
  - mapping
- assessment_id: evidence
  area: evidence
  topic: Definition, adopted lead, producer and antibacterial eligibility
  outcome: supported
  summary: The sole adopted 1986 original was read completely and supports natural-product
    production and sodium-salt antibacterial zones, but not its appended BGC claim.
    Later2016 SI and2024 genomic/metabolomic evidence support that broad BGC statement
    with putative-function limits. Separate2024 parent-acid MICs support natural-compound
    eligibility. Quantitative salt/acid, strain, medium and derivative boundaries
    are preserved.
  target_ids:
  - antibioticmech:aro-ca1f16372a
  evidence_ids:
  - adopted
  - original-activity
  - biosynthesis2016
  - biosynthesis2024
  - primary2024-material
  - primary2024-activity
- assessment_id: completeness
  area: completeness
  topic: Mechanistic and stereochemical enrichment boundaries
  outcome: unknown
  summary: The optional structured fields are absent without a schema violation. Direct
    original data can support bounded EF-Tu-dependent translation inhibition and assay-specific
    activity enrichment, but no derivative KD, universal GTPase effect, whole-pathogen
    EF-Tu susceptibility, or all-enzyme BGC validation should be imported. The ten
    tetrahedral assignments merit primary-qualified curation rather than automatic
    filling from family analogy.
  target_ids:
  - antibioticmech:aro-ca1f16372a
  evidence_ids:
  - mechanism1989
  - mechanism1989-method
  - primary2024-structure
  - primary2024-si
  - primary2024-mechanism
  - derivative-boundary
- assessment_id: provenance
  area: provenance
  topic: Source ownership and reproducibility
  outcome: supported
  summary: All original 13 and expanded 26 input hashes remain unchanged. ARO owns
    the named definition/class/xrefs; PubChem enrichment owns the stored graph. The
    full native history was read and is consistent with generation. Future fixes belong
    to maintained source/overlay handling and regeneration; no status promotion or
    native mutation occurred.
  target_ids:
  - antibioticmech:aro-ca1f16372a
  evidence_ids:
  - owners
  - pubchem-owner
  - search
  - native
findings:
- finding_id: F1
  issue_key: l-681217-terminal-alkene-wrong-geometry
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The stored terminal E alkene denotes the wrong geometric isomer
  description: Native and adopted/current PubChem encode seven E alkenes. Original1986
    Figure 5 and independently characterized2024 Figure 1/SI depict the distal terminal
    bond C31=C32 as Z. Native atoms 40–41 map directly to that bond; a one-bond diagnostic
    changes only /b9-7+ to /b9-7- and yields OSKAZZUZQORABG-QVHXHHNKSA-N. This establishes
    the wrong asserted geometry without requiring unqualified adoption of all ten
    later tetrahedral proposals.
  target_ids:
  - antibioticmech:aro-ca1f16372a
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  evidence_ids:
  - pubchem-owner
  - pubchem
  - original-structure
  - primary2024-structure
  - mapping
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure enrichment transform
  rule_id: 'review-yaml-record: exact identity'
  normalization_reason: 'Blocker under the explicit wrong-identity rubric: the graph
    asserts the opposite alkene geometry, rather than merely leaving a centre unspecified.'
- finding_id: F2
  issue_key: l-681217-chebi-exact-stereo-mismatch
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: CHEBI201407 lacks the alkene geometry required for exact equivalence
  description: Current CHEBI201407 has identical constitution but no specified alkene
    geometries, with key OSKAZZUZQORABG-UHFFFAOYSA-N. Native xrefs asserts chemical
    identity to a graph with seven defined alkenes. This mismatch is independently
    present before and after the terminal-Z repair; the ChEBI submitted all-E name
    does not repair its unspecified default graph.
  target_ids:
  - antibioticmech:aro-ca1f16372a
  field_paths:
  - xrefs[1]
  evidence_ids:
  - native
  - chebi
  - mapping
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO molecule identity, classification, structure and citation owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record field owner
  rule_id: 'review-yaml-record: exact chemical grounding'
  normalization_reason: Major wrong exact grounding; a same-connectivity database
    entry with unspecified alkene geometry is not an interchangeable exact structure.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-ca1f16372a
  description: Correct the terminal geometry through maintained structural ownership
    after primary adjudication, preserving separate tetrahedral uncertainty.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure enrichment transform
  generator: scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py
  acceptance_checks:
  - Map the actual1986 Figure 5 and2024 Figure 1/SI C31=C32 bond to native atoms 40–41
    and encode Z while retaining the six other E alkenes, formula and neutral molecular
    form.
  - Treat the one-bond candidate key as a diagnostic, not a complete absolute-structure
    replacement. Review all ten2024 tetrahedral proposals with their ROESY-versus-analogy
    evidence before deciding what to encode.
  - Implement a reproducible maintained-source or curator structural correction and
    regenerate SMILES/InChI/key together; do not patch generated YAML or infer racemic
    material from unspecified stereo.
  - Recheck PubChem6439903 and all exact chemical xrefs against the adjudicated graph,
    then rerun focused and required corpus gates.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-ca1f16372a
  description: Resolve or qualify the ChEBI source link according to exact-structure
    semantics.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO molecule identity, classification, structure and citation owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record field owner
  generator: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  acceptance_checks:
  - Preserve ARO source provenance while preventing CHEBI201407 with unknown alkene
    geometry from being emitted as an exact chemical equivalent.
  - Retain the observed ChEBI name-versus-graph discrepancy in source adjudication;
    do not substitute the no-stereo graph or its all-E name for primary geometry.
  - Validate the repaired xref against the chosen exact stereochemical representation
    and rerun source/reference checks.
- action_id: A3
  finding_ids: []
  target_ids:
  - antibioticmech:aro-ca1f16372a
  description: Optional evidence enrichment should separate the original activity/producer
    citation from later biosynthetic and mechanism evidence.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO molecule identity, classification, structure and citation owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record field owner
  acceptance_checks:
  - Cite the later 2016/2024 cluster work for biosynthesis and preserve comparative/putative
    enzyme-function scope;1986 alone has no BGC experiment.
  - Keep1986 sodium-salt diffusion zones distinct from2024 parent-acid MICs and combinations.
    Preserve actual strain identifiers and the BL21-versus-BW25113 mutant-background
    difference.
  - Do not transfer derivative 10 KD, other elfamycin targets, hybrid-system pathogen
    susceptibility, or inferred absolute stereochemistry as unqualified parent observations.
    Missing optional fields alone require no correction.
limitations:
- The sole adopted 1986 paper was read in full, with actual Table 2/Table 3 and Figure
  5 viewed. The complete four-page1989 scan was read. The2024 ACS scientific main
  and Methods were fully read; actual Figures 1/4, Tables 1/2 and SI S9/S20 were viewed.
  Other plots were assessed through source text/captions, not independently remeasured.
- The2024 SI strain/material sections S2–S5 and chemical characterization S9–S11 were
  read; raw FIDs were not reprocessed. Exact MIC inoculum, assay medium and incubation
  remain delegated to the source-cited protocol and were not independently recovered.
  Numeric results are retained with that boundary.
- The2016 publisher main was available only as opening paragraphs; its full SI TablesS1–S2
  were read as text, but original spectral images were not independently interpreted.
  The RSC study was read only for its exact S. cattleya section, relevant references
  and actual Figure 5, not all unrelated metabolomic discoveries.
- Absolute tetrahedral assignments in2024 rely partly on analogy to other elfamycins.
  This review confirms the terminal alkene conflict without presenting a final-product
  crystal or independently established absolute hand. Historical salt preparations
  and possible isomerization are not assumed identical to the later isolated acid.
- Some scratch filenames contain2025 because of the PMC release context; the ACS source
  itself is correctly identified as the 2024 publication PMID39576948/DOI10.1021/acs.biochem.4c00541.
  Failed and guessed retrieval routes remain in manifests but are not evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All original 13 and expanded 26 source input hashes were verified unchanged at draft
  writing. No native/source/history/progress/saved-bundle/Git writes occurred.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
