# Enacyloxin IIa: supported EF-Tu biology with a stereochemical xref mismatch and misplaced mechanism citation

- Review: 20261021T153410Z-enacyloxin-iia-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:03:49Z
- Finished UTC: 2026-10-21T15:34:10Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native and PubChem chemical encodings agree, and original experiments support antibacterial protein-synthesis inhibition, EF-Tu interaction and E. coli EF-Tu resistance variants. The adopted ChEMBL record has a different pattern of assigned and unassigned stereocentres, so it is not an exact graph match. The sole displayed definition citation reports release of EF-Tu·GDP, whereas the definition uses the later ribosome-trapping model. One major identity-link correction and one minor citation-placement correction are required.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 397; one complete native record. All thirteen initial hashes were verified unchanged before judgment and retained. Actual ARO, PubChem, target-role and CARD overlay owners were appended, giving twenty-one captured inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-9fd72752cb | data/antibiotics/antibacterial/enacyloxin-iia.yaml | generated | enacyloxin IIa |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | antibioticmech:aro-9fd72752cb | Actual focused schema validation passed. |
| strict | passed | True | antibioticmech:aro-9fd72752cb | Actual focused strict validation passed. |
| chemistry | passed | False | antibioticmech:aro-9fd72752cb | Native SMILES and InChI agree in full key, formula, charge and masses, and the ARO-derived minted alias reproduces. |
| authority-map-initial | failed | False | antibioticmech:aro-9fd72752cb | Initial diagnostic incorrectly required a direct substructure mapping for the InChI-imported tautomer and stopped at native_inchi. No molecular inconsistency was inferred from that mapping failure. |
| authority-map-corrected | passed | False | antibioticmech:aro-9fd72752cb | Corrected diagnostic compares full standard InChI identity and maps directly comparable SMILES/molfile graphs. Execution completed; PubChem matches, while ChEMBL has differing stereochemical scope. Completion is not a claim that every xref agrees. |
| adapter-catalog | passed | False | antibioticmech:aro-9fd72752cb | Complete public catalog inspected before mechanistic web follow-up. |
| adapter-eftu | passed | False | antibioticmech:aro-9fd72752cb | The query returns tufA/b3339 and tufB/b3980, with no iModulon hit. These identify the relevant protein family; they are not binding or resistance evidence. |
| Authoritative full QC | failed | True | antibioticmech:aro-9fd72752cb | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-9fd72752cb | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-9fd72752cb | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-9fd72752cb | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-9fd72752cb | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-9fd72752cb | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-9fd72752cb | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-9fd72752cb | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-9fd72752cb | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Native molecular representation and exact xrefs

identity: concern. Targets: antibioticmech:aro-9fd72752cb.

The native encodings and PubChem agree, but the ChEMBL xref assigns a different set of stereocentres. The same formula and stereocentre count do not establish equivalence. No opposite shared stereocentre or mixture is established. Complete natural-product stereochemical sign-off remains limited.

### Minted identity, hierarchy and chemical-class language

identity: supported. Targets: antibioticmech:aro-9fd72752cb.

The ARO concept is a molecule beneath a broader EF-Tu-defined elfamycin class. Absence of a trusted ChEBI exact link explains the deterministic minted identifier and MINTED status. The functional class does not require a shared backbone with kirromycin.

### EF-Tu target and definition support

evidence: concern. Targets: antibioticmech:aro-9fd72752cb.

Independent original evidence supports EF-Tu binding and protein-synthesis inhibition. The native database target qualification is honest and not itself a defect. The specific definition citation, however, reports the opposite release result from the later trapping model; that citation placement needs correction without rejecting the later mechanism.

### E. coli EF-Tu mutant database relation

evidence: supported. Targets: antibioticmech:aro-9fd72752cb.

The current official source relation and complete original 1999 abstract support the bounded target-alteration claim. Native evidence does not pretend to be a primary allele/strain MIC observation. No such numerical or taxonomic precision is invented.

### Antibacterial class and optional biological coverage

evidence: supported. Targets: antibioticmech:aro-9fd72752cb.

Original protein-synthesis experiments and separately purified IIa susceptibility data support antibacterial classification. Native empty quantitative activity, producer, clinical, graph and dataset fields are not defects. Biosynthetic enzymes or strain gene-expression changes are not antimicrobial targets.

### Whole-record evidence placement and maintained owners

provenance: supported. Targets: antibioticmech:aro-9fd72752cb.

All native fields, source rows and both adopted leads were assessed. Original hashes are preserved and actual owners appended. The first-reference seeding behavior explains the misplaced definition citation. Current SEEDED status is not promoted by this review.

## Findings

### F1: Reconcile the exact ChEMBL link with the native stereochemical scope

major / open / confirmed; issue key: enacyloxin-iia-chembl-stereochemical-scope-mismatch.

CHEMBL5282611 and the native PubChem-derived graph have identical constitution but assign different stereocentres. ChEMBL assigns the two hydroxyl-bearing centres left unspecified in native and leaves the native-assigned methyl-bearing and ring carboxyl-bearing centres unspecified. Their full standard InChIKeys differ. The unqualified exact xref therefore conflates different stereochemical scopes. Resolve or qualify that link through the source path; do not silently replace native with ChEMBL or call either an established mixture or opposite epimer.

### F2: Attach later primary support to the ribosome-trapping statement

minor / open / confirmed; issue key: enacyloxin-iia-ribosome-trapping-definition-citation.

The native definition_source selects PMID8665868 for a definition containing EF-Tu·GDP immobilization on the ribosome. That original 1996 paper reports EF-Tu·GDP leaving the ribosome and explicitly says enacyloxin does not inhibit its release. Later 1999 and 2006 studies support the trapping model. Preserve that distinction and attach appropriate later primary support to the corresponding statement rather than treating the 1996 source as support for every clause.

## Recommended Actions And Acceptance Checks

### A1

Resolve the ChEMBL exact-equivalence assertion with a documented stereochemical comparison in the maintained source path.

- Compare the actual current ChEMBL and chosen compound graph atom by atom; explicitly record assigned versus unassigned centres and full InChIKeys. Remove or qualify a non-equivalent link, or adopt a verified equivalent source identifier.
- Do not use equal formulas, centre counts or names as exact stereo equivalence. Resolve complete natural-product stereochemistry from appropriate original evidence before any graph replacement; do not automatically transfer IVa CIP labels to IIa.
- Regenerate through the maintained source path and pass focused schema, strict, chemistry and source-reproduction checks.

### A2

Make the definition citation accurately support the later EF-Tu ribosome-trapping statement.

- Retain PMID8665868 for its demonstrated EF-Tu and incorporation results, while recording its contrary release result. Attach inspected later primary evidence, such as PMID10610785 and PMID16257965, to the trapping claim with precise read depth.
- Preserve the current database-only target and resistance qualifications until separately curated primary evidence is installed; do not turn nucleotide-binding Kd or gas-phase stability into antibiotic affinity or whole-cell causality.
- Apply claim-level definition/evidence handling in the maintained source or overlay and regenerate; avoid a blanket reorder of all ARO citation lists. Run focused schema, strict and source-reproduction checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/enacyloxin-iia.yaml; Entire native YAML. | supports | The SEEDED, MINTED record is named enacyloxin IIa, with one ARO source concept and four history events. Its neutral C33H45Cl2NO11 structure has full key IWBADCVFZDCUTN-RYDLOJRTSA-N, seven assigned and two unassigned tetrahedral centres, and six specified alkenes. The definition cites PMID8665868 and proposes an EF-Tu·GDP ribosome-trapping model. ARO3001219 is the broader elfamycin class. Xrefs comprise ARO3001242, PubChem6444164 and CHEMBL5282611. One EF-Tu direct-binding target is explicitly PRIMARY_EVIDENCE_NEEDED and one E. coli mutant resistance mechanism is explicitly a CARD database assertion. No numerical activity, producer, clinical, dataset or causal-graph claims are present. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv; data/raw/aro_resistance_edges.tsv; data/raw/pubchem_structures.tsv; conf/aro_target_roles.tsv; scripts/extract_source_inventory.py; scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py; Complete exact source rows, target-role row and applicable generation code; CARD qualification overlay inspected. | supports | ARO concept row 226 supplies the definition, two literature leads, class and external links. PubChem row 61 supplies the molecular structure and retrieval date. Target row 227 maps EF-Tu through the explicit typed-role table; resistance row 3902 supplies the mutant relation and target-alteration category. The seeder preserves database-only qualification and chooses the first definition reference, PMID8665868, from the ARO list. PMID12370016 is a secondary review lead. No exact CARD review overlay applies. No ChEBI, FDA or MIBiG row owns this record. The actual PubChem enrichment script and ARO source paths are captured; original default ChEBI context hashes remain preserved. |
| aro | ARO:3001242; ARO:3000731; ARO:3003370; ARO:3001219; ARO:0001001; https://raw.githubusercontent.com/arpcard/aro/master/src/ontology/aro.obo; Complete five relevant current official OBO stanzas inspected from the previously downloaded public source; exact extraction retained as 397-current-aro-terms.txt. | supports | The official ontology retains the native molecule definition, both xrefs, EF-Tu targeted_by_antibiotic relation and mutant confers_resistance_to_antibiotic relation. ARO3003370 cites PMID10610785. ARO3001219 explicitly defines elfamycins by EF-Tu inhibition rather than a common chemical backbone, so this broader class does not assert structural similarity to kirromycin. ARO0001001 defines target alteration. Direct CARD page attempts returned 500; the actual official ontology source was inspected instead. |
| pubchem | PubChem:6444164; https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6444164/property/InChI,InChIKey,MolecularFormula,SMILES/JSON; Complete official property response and independent SMILES/InChI parsing. | supports | Current PubChem exactly matches the native full key, constitution, charge and molecular formula. The native average mass 702.6 is source-rounded from approximately 702.625; its monoisotopic mass agrees. Two hydroxyl-bearing side-chain centres remain explicitly unassigned. An unspecified centre alone is not evidence of a mixture or racemate. |
| chembl | ChEMBL:CHEMBL5282611; https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL5282611.json; Complete official molecule response; SMILES, InChI and molfile independently parsed and atom-mapped where directly comparable. | refutes | ChEMBL gives IWBADCVFZDCUTN-IDMQDXBZSA-N, with the same formula and constitution but a different stereochemical scope. Native atoms 10 and 11 are unspecified, whereas their ChEMBL counterparts 16 and 18 are S and R. Native atom 12, the methyl-bearing side-chain centre, and atom 30, the ring carboxyl-bearing centre, are assigned S but unspecified in ChEMBL. The other five shared assigned centres and alkene geometries agree. Both sources have seven assigned centres, but they assign different centres; equal counts and connectivity do not make the exact xref valid. No shared assigned centre was shown to be inverted. |
| original-structure | PMID:1592680; DOI:10.7164/antibiotics.45.470; https://www.jstage.jst.go.jp/article/antibiotics1968/45/4/45_4_470/_pdf; Complete original six-page 1992 main article read; original Figure 1 on p470 visually checked. | supports | The original exact IIa elucidation establishes the C33H45Cl2NO11 constitution, the ester linking the 3-position of dihydroxycyclohexanecarboxylic acid to the chlorinated polyene chain, the 15-prime ketone and the 19-prime carbamate. NMR supports alkene geometry 2E,4E,6E,8E,10Z,20E and ring relative geometry. The paper does not assign every absolute side-chain centre. The native constitution and alkene pattern agree; this early paper alone cannot settle all later absolute-stereochemistry choices. |
| later-stereo | PMID:17638342; DOI:10.1002/cbdv.200790140; Complete original indexed abstract; publisher and author-page full-text attempts returned 403. | context_only | The 2007 report assigns the previously unresolved 13-prime R,14-prime R,15-prime S configuration to enacyloxin IVa using J-resolved HMBC and NOESY. The abstract concerns IVa, a reduced congener, and does not itself establish every corresponding IIa CIP label or justify wholesale graph replacement. The exact IVa-to-IIa mapping and two native-unassigned centres remain bounded curation questions. The confirmed ChEMBL link mismatch does not depend on choosing a final natural-product graph. |
| early-moa | PMID:1778796; DOI:10.7164/antibiotics.44.1457; https://www.jstage.jst.go.jp/article/antibiotics1968/44/12/44_12_1457/_pdf; Complete original three-page 1991 paper read; Table 1 and methods on p1458 visually inspected. | supports | Enacyloxin IIa suppresses amino-acid incorporation in E. coli cultures and poly(U)-dependent phenylalanine incorporation in an E. coli K-12 S30 system. The study separately tests DNA, RNA, lipid and peptidoglycan precursors; it supports protein-synthesis inhibition under those conditions. The drug is dissolved in sodium bicarbonate for assays, which is not an independently characterized sodium-salt identity. These experiments are not MICs or direct proof of a particular EF-Tu contact. |
| adopted1996 | PMID:8665868; DOI:10.1002/j.1460-2075.1996.tb00618.x; https://www.embopress.org/doi/pdf/10.1002/j.1460-2075.1996.tb00618.x; Entire original eight-page paper read, including all methods and captions; original pp2609–2610 visually checked. | partial | The highly purified compound inhibits a reconstituted E. coli protein-synthesis system and alters EF-Tu nucleotide interaction, electrophoretic mobility and aa-tRNA positioning. Puromycin reactivity remains largely intact, distinguishing the observed incorporation effect from direct peptidyl-transferase-center inhibition. Critically, gel filtration on p2609 detects no nucleotide co-migration with ribosomes after GTP hydrolysis, and p2610 states that the antibiotic does not inhibit EF-Tu·GDP release. This supports EF-Tu action but does not support the trapping statement attached to this single definition citation. Nucleotide Kd values in this study are not antibiotic-binding Kd values. |
| adopted-review | PMID:12370016; DOI:10.2174/1389203023380855; Complete indexed abstract and bibliographic record of the adopted 2002 review. | context_only | This secondary review surveys multiple EF-Tu inhibitor subclasses and the aurodox and GE2270A crystal structures. It is retained as a review/context lead, not mislabeled as a primary enacyloxin experiment. Its full text was not obtained and its abstract alone does not resolve each clause in the ARO definition. |
| resistance-primary | PMID:10610785; DOI:10.1006/jmbi.1999.3296; Complete original indexed abstract; DOI landing response was not usable article text. | supports | The original 1999 experiment identifies E. coli EF-Tu variants Q124K, G316D, Q329H and A375T that confer resistance in its experimental systems. It reports dominance of sensitive EF-Tu in mixed populations and interprets the results in terms of impaired antibiotic binding, release after hydrolysis, or reduced interaction of the EF-Tu·GDP·antibiotic complex with aa-tRNA. This supports the native target-alteration database relation and later trapping model at abstract depth. No variant-specific whole-cell MIC, strain identity, accession or clinical resistance claim is reconstructed from the abstract. |
| binding2006 | PMID:16257965; DOI:10.1074/jbc.M505951200; PDB:2BVN; https://www.rcsb.org/structure/2BVN; Complete original abstract plus original experimental deposition metadata and relevant entity/ligand sections of the deposited mmCIF. Main publisher HTML/PDF returned 403. | supports | The original crystallographic study places enacyloxin IIa between EF-Tu domains 1 and 3 and describes inhibited EF-Tu·GDP release. PDB2BVN is the E. coli EF-Tu–GDPNP–ENX complex at 2.3 angstrom resolution and explicitly contains the ENX chemical entity. This directly supports physical target interaction, while not proving every proposed downstream step from this crystal alone. Density and coordinates were not re-refined, and the deposited ligand was not used to overwrite the unresolved complete natural-product stereochemistry. |
| binding2024 | PMID:38830009; DOI:10.1021/jasms.4c00087; PMC11228974; Complete original main XML body, methods, results, discussion and figure captions read; supplements and figure images not independently inspected. | supports | Native ESI-MS detects E. coli EF-Tu–GDPNP–enacyloxin complexes, and collision-induced unfolding measures stabilization and antibiotic dissociation in the gas phase. Experimental complexes and molecular-dynamics simulations are distinct. The study reports that the extra stabilization at its 50-percent unfolding metric is not significant, while lower unfolding thresholds distinguish the ligand effect. This is corroborating interaction evidence, not a whole-cell MIC, solution binding constant or independent full stereochemical elucidation. |
| purified-activity | PMID:21609847; DOI:10.1016/j.chembiol.2011.01.020; https://orca.cardiff.ac.uk/17346/1/OA-13.pdf; Selected original author-deposited main-paper text: isolation/structure and activity Results pp669–671, Table 3 text and methods pp675–676. Direct downloads returned 403 and screenshot rendering failed. | supports | HPLC separates enacyloxin IIa from its 4,5-Z iso congener before susceptibility testing. Table 3 reports IIa MIC 3.0 mg/L for A. baumannii OXA23 clone 2 and 6.5 mg/L for B. multivorans ATCC17616; other tested strains include resistant results above 100 mg/L. The method is standardized broth microdilution. These support antibacterial activity without transferring crude-culture or iso-congener effects. A biosynthetic prediction disagrees with an IVa C15 assignment; that position is a ketone in IIa and is not a native IIa stereocentre. |
| adapter | iModulonDB:e_coli/precise1k/b3339; iModulonDB:e_coli/precise1k/b3980; Actual complete catalog and EF-Tu search performed before open-ended mechanism research. | context_only | The adapter returns tufA and tufB as translation elongation factors Tu 1 and Tu 2, with zero iModulon hits. No module summary is applicable. These gene annotations do not establish the mutant resistance phenotype, exact protein accession or direct drug binding; original experiments provide that evidence. |
| search | 397-inclusive-hits.txt; 397-fetch-results.json through 397-fetch4-results.json; Ignored-inclusive local search, exact-source lookup and bounded public primary follow-up. | context_only | The local search covers hidden and ignored files, including the exact raw/native entry, queue and generated projections. The focused curation/conf/reviews/reports search finds the readiness queue but no exact overlay or prior report. Generated projections are not independent evidence. Public retrieval recovers full 1991, 1992, 1996 and 2024 originals; 1999, 2002, 2006 and 2007 remain at explicitly bounded depths. The wrong first CARD page routes and subsequent500 responses are retained as failed access, not inspected evidence. |
| validation | 397-schema.log; 397-strict.log; 397-chemistry.json; 397-xref-chemistry.json; Actual focused gates, corrected authority diagnostic and unchanged-input recheck. | supports | Focused schema, strict and native chemistry pass. The independent authority diagnostic exposes the ChEMBL stereo-scope mismatch despite these passing gates. Initial direct mapping of an InChI-imported tautomer failed; the final comparison distinguishes that technical mapping limit from the confirmed SMILES/molfile stereo mismatch. |

## Limits And Additional Notes

- The 1999 resistant-mutant study and 2006 crystallographic article were read at complete original abstract depth; the 2006 original deposition metadata and relevant mmCIF sections were additionally inspected. Main article access was not obtained. No detailed mutant MIC protocol, allele accession or crystal-density reanalysis is claimed.
- The adopted 2002 source is a secondary review, read at complete abstract depth. The 2007 stereochemical original was also available only as a complete abstract, and explicitly concerns IVa. A complete absolute-stereochemical reconstruction of natural IIa remains unresolved.
- The 2011 author-deposited article was inspected in selected original full-text sections and Table 3 text through the web tool. Direct PDF downloads returned 403 and screenshot rendering failed. Supplemental tables and the complete microdilution protocol were not inspected; no individual numerical native activity object is proposed.
- The 2024 main XML was read, including methods and figure captions, but supplements and figure images were not independently viewed. Its gas-phase experiments and simulations are not solution binding constants or bacterial MICs.
- Direct CARD pages returned 500. Current official ARO OBO stanzas were inspected from the same-session public download with its actual timestamp and hash.
- The initial chemistry mapping assumed that an InChI-imported tautomer would directly substructure-match the displayed native graph; that diagnostic failed and was corrected. Full native and PubChem standard-InChI agreement remains established, while the ChEMBL stereo discrepancy is independently demonstrated by directly mapped SMILES and molfile graphs.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- The native two unassigned centres are not by themselves proof of a mixture. The corrective xref finding is independent of a final choice of natural-product stereochemistry.
- The initial thirteen input hashes are retained alongside the appended actual owners. No native status promotion or source mutation is implied by these scientific assessments.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T153410Z-enacyloxin-iia-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Enacyloxin IIa: supported EF-Tu biology with a stereochemical xref mismatch
  and misplaced mechanism citation'
started_at: '2026-10-21T15:03:49Z'
finished_at: '2026-10-21T15:34:10Z'
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
summary: The native and PubChem chemical encodings agree, and original experiments
  support antibacterial protein-synthesis inhibition, EF-Tu interaction and E. coli
  EF-Tu resistance variants. The adopted ChEMBL record has a different pattern of
  assigned and unassigned stereocentres, so it is not an exact graph match. The sole
  displayed definition citation reports release of EF-Tu·GDP, whereas the definition
  uses the later ribosome-trapping model. One major identity-link correction and one
  minor citation-placement correction are required.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: conf/sources.yaml
    sha256: 4a2dcd7a3a88953b6cb35b51a48ed77b626c3af2cbb542b0d38ba10540ed7df9
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: curation/curator_antibiotics.tsv
    sha256: 224cbb7261add427184b2762a29c2ff3e85c85e0a06cf22b144545346487247b
    role: context
  - path: curation/decisions.tsv
    sha256: a5834b44307b0449b0df9362c551b7fcd707f3ae51f73d429d37d51f5a169d61
    role: context
  - path: data/antibiotics/antibacterial/enacyloxin-iia.yaml
    sha256: 900a4687b67dc2952123b01b90dab40fbe93a302260971f9e7b06ca762bfc2a0
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
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
  - path: data/raw/chebi_antimicrobials.tsv
    sha256: 4c33e56c3c342be657309f720f5b5cb9cad1fae13bec202ef99e449503c32004
    role: context
  - path: data/raw/chebi_role_names.tsv
    sha256: 5c476c0aacd7c98d7241d2343a6fc41ee9eb9338077404c5b011a04bf40c6ac5
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
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
- target_id: antibioticmech:aro-9fd72752cb
  path: data/antibiotics/antibacterial/enacyloxin-iia.yaml
  label: enacyloxin IIa
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO concept, target and resistance extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Maintained typed target assertion map
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained CARD evidence qualification overlay
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: CARD evidence overlay application
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 397; one complete native record. All thirteen initial
    hashes were verified unchanged before judgment and retained. Actual ARO, PubChem,
    target-role and CARD overlay owners were appended, giving twenty-one captured
    inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-9fd72752cb
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused schema validation passed.
  target_ids:
  - antibioticmech:aro-9fd72752cb
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/enacyloxin-iia.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual focused strict validation passed.
  target_ids:
  - antibioticmech:aro-9fd72752cb
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/enacyloxin-iia.yaml --out /private/tmp/am-review-session/397-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Native SMILES and InChI agree in full key, formula, charge and masses,
    and the ARO-derived minted alias reproduces.
  target_ids:
  - antibioticmech:aro-9fd72752cb
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 397
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-map-initial
  name: authority-map-initial
  status: failed
  required: false
  summary: Initial diagnostic incorrectly required a direct substructure mapping for
    the InChI-imported tautomer and stopped at native_inchi. No molecular inconsistency
    was inferred from that mapping failure.
  target_ids:
  - antibioticmech:aro-9fd72752cb
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/397-xref-check.py
  exit_code: 1
  expected_exit_code: 0
- check_id: authority-map-corrected
  name: authority-map-corrected
  status: passed
  required: false
  summary: Corrected diagnostic compares full standard InChI identity and maps directly
    comparable SMILES/molfile graphs. Execution completed; PubChem matches, while
    ChEMBL has differing stereochemical scope. Completion is not a claim that every
    xref agrees.
  target_ids:
  - antibioticmech:aro-9fd72752cb
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/397-xref-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-catalog
  name: adapter-catalog
  status: passed
  required: false
  summary: Complete public catalog inspected before mechanistic web follow-up.
  target_ids:
  - antibioticmech:aro-9fd72752cb
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-eftu
  name: adapter-eftu
  status: passed
  required: false
  summary: The query returns tufA/b3339 and tufB/b3980, with no iModulon hit. These
    identify the relevant protein family; they are not binding or resistance evidence.
  target_ids:
  - antibioticmech:aro-9fd72752cb
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query 'elongation
    factor Tu'
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
  - antibioticmech:aro-9fd72752cb
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
  - antibioticmech:aro-9fd72752cb
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
  - antibioticmech:aro-9fd72752cb
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
  - antibioticmech:aro-9fd72752cb
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
  - antibioticmech:aro-9fd72752cb
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
  - antibioticmech:aro-9fd72752cb
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
  - antibioticmech:aro-9fd72752cb
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
  - antibioticmech:aro-9fd72752cb
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
  - antibioticmech:aro-9fd72752cb
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/enacyloxin-iia.yaml
  locator: Entire native YAML.
  accessed_at: '2026-10-21T15:32:06Z'
  support: supports
  summary: The SEEDED, MINTED record is named enacyloxin IIa, with one ARO source
    concept and four history events. Its neutral C33H45Cl2NO11 structure has full
    key IWBADCVFZDCUTN-RYDLOJRTSA-N, seven assigned and two unassigned tetrahedral
    centres, and six specified alkenes. The definition cites PMID8665868 and proposes
    an EF-Tu·GDP ribosome-trapping model. ARO3001219 is the broader elfamycin class.
    Xrefs comprise ARO3001242, PubChem6444164 and CHEMBL5282611. One EF-Tu direct-binding
    target is explicitly PRIMARY_EVIDENCE_NEEDED and one E. coli mutant resistance
    mechanism is explicitly a CARD database assertion. No numerical activity, producer,
    clinical, dataset or causal-graph claims are present.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv; data/raw/aro_resistance_edges.tsv;
    data/raw/pubchem_structures.tsv; conf/aro_target_roles.tsv; scripts/extract_source_inventory.py;
    scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py
  locator: Complete exact source rows, target-role row and applicable generation code;
    CARD qualification overlay inspected.
  accessed_at: '2026-10-21T15:32:06Z'
  support: supports
  summary: ARO concept row 226 supplies the definition, two literature leads, class
    and external links. PubChem row 61 supplies the molecular structure and retrieval
    date. Target row 227 maps EF-Tu through the explicit typed-role table; resistance
    row 3902 supplies the mutant relation and target-alteration category. The seeder
    preserves database-only qualification and chooses the first definition reference,
    PMID8665868, from the ARO list. PMID12370016 is a secondary review lead. No exact
    CARD review overlay applies. No ChEBI, FDA or MIBiG row owns this record. The
    actual PubChem enrichment script and ARO source paths are captured; original default
    ChEBI context hashes remain preserved.
  snapshot_sha256: 57d4ea00131c59c927e2cd2ae4cced06c84667485bb537e08dec656fd58ad65f
- evidence_id: aro
  kind: authority
  reference: ARO:3001242; ARO:3000731; ARO:3003370; ARO:3001219; ARO:0001001; https://raw.githubusercontent.com/arpcard/aro/master/src/ontology/aro.obo
  locator: Complete five relevant current official OBO stanzas inspected from the
    previously downloaded public source; exact extraction retained as 397-current-aro-terms.txt.
  accessed_at: '2026-10-21T14:50:57Z'
  support: supports
  summary: The official ontology retains the native molecule definition, both xrefs,
    EF-Tu targeted_by_antibiotic relation and mutant confers_resistance_to_antibiotic
    relation. ARO3003370 cites PMID10610785. ARO3001219 explicitly defines elfamycins
    by EF-Tu inhibition rather than a common chemical backbone, so this broader class
    does not assert structural similarity to kirromycin. ARO0001001 defines target
    alteration. Direct CARD page attempts returned 500; the actual official ontology
    source was inspected instead.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: pubchem
  kind: authority
  reference: PubChem:6444164; https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6444164/property/InChI,InChIKey,MolecularFormula,SMILES/JSON
  locator: Complete official property response and independent SMILES/InChI parsing.
  accessed_at: '2026-10-21T15:26:05Z'
  support: supports
  summary: Current PubChem exactly matches the native full key, constitution, charge
    and molecular formula. The native average mass 702.6 is source-rounded from approximately
    702.625; its monoisotopic mass agrees. Two hydroxyl-bearing side-chain centres
    remain explicitly unassigned. An unspecified centre alone is not evidence of a
    mixture or racemate.
  snapshot_sha256: 3ec0b3dcd5a51077db22bca5398585cc1e40966b6ab48bab9f08d102d9fdd210
- evidence_id: chembl
  kind: authority
  reference: ChEMBL:CHEMBL5282611; https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL5282611.json
  locator: Complete official molecule response; SMILES, InChI and molfile independently
    parsed and atom-mapped where directly comparable.
  accessed_at: '2026-10-21T15:26:05Z'
  support: refutes
  summary: ChEMBL gives IWBADCVFZDCUTN-IDMQDXBZSA-N, with the same formula and constitution
    but a different stereochemical scope. Native atoms 10 and 11 are unspecified,
    whereas their ChEMBL counterparts 16 and 18 are S and R. Native atom 12, the methyl-bearing
    side-chain centre, and atom 30, the ring carboxyl-bearing centre, are assigned
    S but unspecified in ChEMBL. The other five shared assigned centres and alkene
    geometries agree. Both sources have seven assigned centres, but they assign different
    centres; equal counts and connectivity do not make the exact xref valid. No shared
    assigned centre was shown to be inverted.
  snapshot_sha256: 7b54a7861417705418317ece425954c19e32e51845869995933f919ecd5434ca
- evidence_id: original-structure
  kind: primary_source
  reference: PMID:1592680; DOI:10.7164/antibiotics.45.470; https://www.jstage.jst.go.jp/article/antibiotics1968/45/4/45_4_470/_pdf
  locator: Complete original six-page 1992 main article read; original Figure 1 on
    p470 visually checked.
  accessed_at: '2026-10-21T15:26:46Z'
  support: supports
  summary: The original exact IIa elucidation establishes the C33H45Cl2NO11 constitution,
    the ester linking the 3-position of dihydroxycyclohexanecarboxylic acid to the
    chlorinated polyene chain, the 15-prime ketone and the 19-prime carbamate. NMR
    supports alkene geometry 2E,4E,6E,8E,10Z,20E and ring relative geometry. The paper
    does not assign every absolute side-chain centre. The native constitution and
    alkene pattern agree; this early paper alone cannot settle all later absolute-stereochemistry
    choices.
  snapshot_sha256: 82eebd584b46ff4720945a4762965f7b960f9dea6b673f71a866fbef306cedec
- evidence_id: later-stereo
  kind: primary_source
  reference: PMID:17638342; DOI:10.1002/cbdv.200790140
  locator: Complete original indexed abstract; publisher and author-page full-text
    attempts returned 403.
  accessed_at: '2026-10-21T15:26:06Z'
  support: context_only
  summary: The 2007 report assigns the previously unresolved 13-prime R,14-prime R,15-prime
    S configuration to enacyloxin IVa using J-resolved HMBC and NOESY. The abstract
    concerns IVa, a reduced congener, and does not itself establish every corresponding
    IIa CIP label or justify wholesale graph replacement. The exact IVa-to-IIa mapping
    and two native-unassigned centres remain bounded curation questions. The confirmed
    ChEMBL link mismatch does not depend on choosing a final natural-product graph.
  snapshot_sha256: 974f1b690b7539490eb389773b967d86d89bcdba5ee164dfa95b39cd047a5702
- evidence_id: early-moa
  kind: primary_source
  reference: PMID:1778796; DOI:10.7164/antibiotics.44.1457; https://www.jstage.jst.go.jp/article/antibiotics1968/44/12/44_12_1457/_pdf
  locator: Complete original three-page 1991 paper read; Table 1 and methods on p1458
    visually inspected.
  accessed_at: '2026-10-21T15:26:46Z'
  support: supports
  summary: Enacyloxin IIa suppresses amino-acid incorporation in E. coli cultures
    and poly(U)-dependent phenylalanine incorporation in an E. coli K-12 S30 system.
    The study separately tests DNA, RNA, lipid and peptidoglycan precursors; it supports
    protein-synthesis inhibition under those conditions. The drug is dissolved in
    sodium bicarbonate for assays, which is not an independently characterized sodium-salt
    identity. These experiments are not MICs or direct proof of a particular EF-Tu
    contact.
  snapshot_sha256: be2394ccbf6b4aec308e558059acdd822b6fb829aacf6c8980d0ba04e64a39df
- evidence_id: adopted1996
  kind: primary_source
  reference: PMID:8665868; DOI:10.1002/j.1460-2075.1996.tb00618.x; https://www.embopress.org/doi/pdf/10.1002/j.1460-2075.1996.tb00618.x
  locator: Entire original eight-page paper read, including all methods and captions;
    original pp2609–2610 visually checked.
  accessed_at: '2026-10-21T15:28:51Z'
  support: partial
  summary: The highly purified compound inhibits a reconstituted E. coli protein-synthesis
    system and alters EF-Tu nucleotide interaction, electrophoretic mobility and aa-tRNA
    positioning. Puromycin reactivity remains largely intact, distinguishing the observed
    incorporation effect from direct peptidyl-transferase-center inhibition. Critically,
    gel filtration on p2609 detects no nucleotide co-migration with ribosomes after
    GTP hydrolysis, and p2610 states that the antibiotic does not inhibit EF-Tu·GDP
    release. This supports EF-Tu action but does not support the trapping statement
    attached to this single definition citation. Nucleotide Kd values in this study
    are not antibiotic-binding Kd values.
  snapshot_sha256: 1ec63f09d5208a808012e191d6fa91603dcd3c9a9adfabbf38fa82d613ff4855
- evidence_id: adopted-review
  kind: database
  reference: PMID:12370016; DOI:10.2174/1389203023380855
  locator: Complete indexed abstract and bibliographic record of the adopted 2002
    review.
  accessed_at: '2026-10-21T15:26:06Z'
  support: context_only
  summary: This secondary review surveys multiple EF-Tu inhibitor subclasses and the
    aurodox and GE2270A crystal structures. It is retained as a review/context lead,
    not mislabeled as a primary enacyloxin experiment. Its full text was not obtained
    and its abstract alone does not resolve each clause in the ARO definition.
  snapshot_sha256: 974f1b690b7539490eb389773b967d86d89bcdba5ee164dfa95b39cd047a5702
- evidence_id: resistance-primary
  kind: primary_source
  reference: PMID:10610785; DOI:10.1006/jmbi.1999.3296
  locator: Complete original indexed abstract; DOI landing response was not usable
    article text.
  accessed_at: '2026-10-21T15:26:06Z'
  support: supports
  summary: The original 1999 experiment identifies E. coli EF-Tu variants Q124K, G316D,
    Q329H and A375T that confer resistance in its experimental systems. It reports
    dominance of sensitive EF-Tu in mixed populations and interprets the results in
    terms of impaired antibiotic binding, release after hydrolysis, or reduced interaction
    of the EF-Tu·GDP·antibiotic complex with aa-tRNA. This supports the native target-alteration
    database relation and later trapping model at abstract depth. No variant-specific
    whole-cell MIC, strain identity, accession or clinical resistance claim is reconstructed
    from the abstract.
  snapshot_sha256: 974f1b690b7539490eb389773b967d86d89bcdba5ee164dfa95b39cd047a5702
- evidence_id: binding2006
  kind: primary_source
  reference: PMID:16257965; DOI:10.1074/jbc.M505951200; PDB:2BVN; https://www.rcsb.org/structure/2BVN
  locator: Complete original abstract plus original experimental deposition metadata
    and relevant entity/ligand sections of the deposited mmCIF. Main publisher HTML/PDF
    returned 403.
  accessed_at: '2026-10-21T15:28:51Z'
  support: supports
  summary: The original crystallographic study places enacyloxin IIa between EF-Tu
    domains 1 and 3 and describes inhibited EF-Tu·GDP release. PDB2BVN is the E. coli
    EF-Tu–GDPNP–ENX complex at 2.3 angstrom resolution and explicitly contains the
    ENX chemical entity. This directly supports physical target interaction, while
    not proving every proposed downstream step from this crystal alone. Density and
    coordinates were not re-refined, and the deposited ligand was not used to overwrite
    the unresolved complete natural-product stereochemistry.
  snapshot_sha256: d06cd2c36fcbd063efa5602197153ec21a6c3f056569584b788fee9809545146
- evidence_id: binding2024
  kind: primary_source
  reference: PMID:38830009; DOI:10.1021/jasms.4c00087; PMC11228974
  locator: Complete original main XML body, methods, results, discussion and figure
    captions read; supplements and figure images not independently inspected.
  accessed_at: '2026-10-21T15:26:47Z'
  support: supports
  summary: Native ESI-MS detects E. coli EF-Tu–GDPNP–enacyloxin complexes, and collision-induced
    unfolding measures stabilization and antibiotic dissociation in the gas phase.
    Experimental complexes and molecular-dynamics simulations are distinct. The study
    reports that the extra stabilization at its 50-percent unfolding metric is not
    significant, while lower unfolding thresholds distinguish the ligand effect. This
    is corroborating interaction evidence, not a whole-cell MIC, solution binding
    constant or independent full stereochemical elucidation.
  snapshot_sha256: 700f235960e6ca7b2fa69a35732b99d0ee529e156b58f7cfcccfad2cc790733c
- evidence_id: purified-activity
  kind: primary_source
  reference: PMID:21609847; DOI:10.1016/j.chembiol.2011.01.020; https://orca.cardiff.ac.uk/17346/1/OA-13.pdf
  locator: 'Selected original author-deposited main-paper text: isolation/structure
    and activity Results pp669–671, Table 3 text and methods pp675–676. Direct downloads
    returned 403 and screenshot rendering failed.'
  accessed_at: '2026-10-21T15:32:06Z'
  support: supports
  summary: HPLC separates enacyloxin IIa from its 4,5-Z iso congener before susceptibility
    testing. Table 3 reports IIa MIC 3.0 mg/L for A. baumannii OXA23 clone 2 and 6.5
    mg/L for B. multivorans ATCC17616; other tested strains include resistant results
    above 100 mg/L. The method is standardized broth microdilution. These support
    antibacterial activity without transferring crude-culture or iso-congener effects.
    A biosynthetic prediction disagrees with an IVa C15 assignment; that position
    is a ketone in IIa and is not a native IIa stereocentre.
- evidence_id: adapter
  kind: database
  reference: iModulonDB:e_coli/precise1k/b3339; iModulonDB:e_coli/precise1k/b3980
  locator: Actual complete catalog and EF-Tu search performed before open-ended mechanism
    research.
  accessed_at: '2026-10-21T15:32:06Z'
  support: context_only
  summary: The adapter returns tufA and tufB as translation elongation factors Tu
    1 and Tu 2, with zero iModulon hits. No module summary is applicable. These gene
    annotations do not establish the mutant resistance phenotype, exact protein accession
    or direct drug binding; original experiments provide that evidence.
  snapshot_sha256: 0b62c26d1f6e1be58f74bf2f110c794ec709ff24370207aceea014d997778b19
- evidence_id: search
  kind: search
  reference: 397-inclusive-hits.txt; 397-fetch-results.json through 397-fetch4-results.json
  locator: Ignored-inclusive local search, exact-source lookup and bounded public
    primary follow-up.
  accessed_at: '2026-10-21T15:32:06Z'
  support: context_only
  summary: The local search covers hidden and ignored files, including the exact raw/native
    entry, queue and generated projections. The focused curation/conf/reviews/reports
    search finds the readiness queue but no exact overlay or prior report. Generated
    projections are not independent evidence. Public retrieval recovers full 1991,
    1992, 1996 and 2024 originals; 1999, 2002, 2006 and 2007 remain at explicitly
    bounded depths. The wrong first CARD page routes and subsequent500 responses are
    retained as failed access, not inspected evidence.
  search_scope: '2026-10-21: rg --no-ignore --hidden across data, curation, conf,
    scripts, src, docs, .claude, reviews and reports for ARO:3001242, full key IWBADCVFZDCUTN
    and enacyloxin IIa name variants; separate focused curation/conf/reviews/reports
    search. Public follow-up used exact name, adopted PMIDs, current official ARO/chemical
    endpoints and original DOI/public author links. No paid source was used.'
  snapshot_sha256: e8c0c3f818ece49458be331d6e16d72a2bdf0dd545c09f7f61bb43d75bb5bcba
- evidence_id: validation
  kind: validation
  reference: 397-schema.log; 397-strict.log; 397-chemistry.json; 397-xref-chemistry.json
  locator: Actual focused gates, corrected authority diagnostic and unchanged-input
    recheck.
  accessed_at: '2026-10-21T15:32:06Z'
  support: supports
  summary: Focused schema, strict and native chemistry pass. The independent authority
    diagnostic exposes the ChEMBL stereo-scope mismatch despite these passing gates.
    Initial direct mapping of an InChI-imported tautomer failed; the final comparison
    distinguishes that technical mapping limit from the confirmed SMILES/molfile stereo
    mismatch.
  snapshot_sha256: 3d6e7fffe51144642a423eba21d5df6ef7028981b959a9cd5d97125822bee2de
assessments:
- assessment_id: identity
  area: identity
  topic: Native molecular representation and exact xrefs
  outcome: concern
  summary: The native encodings and PubChem agree, but the ChEMBL xref assigns a different
    set of stereocentres. The same formula and stereocentre count do not establish
    equivalence. No opposite shared stereocentre or mixture is established. Complete
    natural-product stereochemical sign-off remains limited.
  target_ids:
  - antibioticmech:aro-9fd72752cb
  evidence_ids:
  - native
  - pubchem
  - chembl
  - original-structure
  - later-stereo
  - validation
- assessment_id: grounding
  area: identity
  topic: Minted identity, hierarchy and chemical-class language
  outcome: supported
  summary: The ARO concept is a molecule beneath a broader EF-Tu-defined elfamycin
    class. Absence of a trusted ChEBI exact link explains the deterministic minted
    identifier and MINTED status. The functional class does not require a shared backbone
    with kirromycin.
  target_ids:
  - antibioticmech:aro-9fd72752cb
  evidence_ids:
  - owners
  - aro
  - native
- assessment_id: mechanism
  area: evidence
  topic: EF-Tu target and definition support
  outcome: concern
  summary: Independent original evidence supports EF-Tu binding and protein-synthesis
    inhibition. The native database target qualification is honest and not itself
    a defect. The specific definition citation, however, reports the opposite release
    result from the later trapping model; that citation placement needs correction
    without rejecting the later mechanism.
  target_ids:
  - antibioticmech:aro-9fd72752cb
  evidence_ids:
  - adopted1996
  - binding2006
  - binding2024
  - adopted-review
  - owners
- assessment_id: resistance
  area: evidence
  topic: E. coli EF-Tu mutant database relation
  outcome: supported
  summary: The current official source relation and complete original 1999 abstract
    support the bounded target-alteration claim. Native evidence does not pretend
    to be a primary allele/strain MIC observation. No such numerical or taxonomic
    precision is invented.
  target_ids:
  - antibioticmech:aro-9fd72752cb
  evidence_ids:
  - aro
  - resistance-primary
  - native
  - adapter
- assessment_id: activity
  area: evidence
  topic: Antibacterial class and optional biological coverage
  outcome: supported
  summary: Original protein-synthesis experiments and separately purified IIa susceptibility
    data support antibacterial classification. Native empty quantitative activity,
    producer, clinical, graph and dataset fields are not defects. Biosynthetic enzymes
    or strain gene-expression changes are not antimicrobial targets.
  target_ids:
  - antibioticmech:aro-9fd72752cb
  evidence_ids:
  - early-moa
  - adopted1996
  - purified-activity
  - native
- assessment_id: provenance
  area: provenance
  topic: Whole-record evidence placement and maintained owners
  outcome: supported
  summary: All native fields, source rows and both adopted leads were assessed. Original
    hashes are preserved and actual owners appended. The first-reference seeding behavior
    explains the misplaced definition citation. Current SEEDED status is not promoted
    by this review.
  target_ids:
  - antibioticmech:aro-9fd72752cb
  evidence_ids:
  - owners
  - search
  - validation
  - native
findings:
- finding_id: F1
  issue_key: enacyloxin-iia-chembl-stereochemical-scope-mismatch
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile the exact ChEMBL link with the native stereochemical scope
  description: CHEMBL5282611 and the native PubChem-derived graph have identical constitution
    but assign different stereocentres. ChEMBL assigns the two hydroxyl-bearing centres
    left unspecified in native and leaves the native-assigned methyl-bearing and ring
    carboxyl-bearing centres unspecified. Their full standard InChIKeys differ. The
    unqualified exact xref therefore conflates different stereochemical scopes. Resolve
    or qualify that link through the source path; do not silently replace native with
    ChEMBL or call either an established mixture or opposite epimer.
  target_ids:
  - antibioticmech:aro-9fd72752cb
  field_paths:
  - xrefs[1]
  - chemical_structure
  evidence_ids:
  - native
  - pubchem
  - chembl
  - validation
  rule_id: Every exact xref must denote the same salt, charge and stereochemical scope
  native_severity: major
  normalization_reason: This is a confirmed exact-equivalence defect. Shared assigned
    centres agree and the native constitution is supported, so the finding does not
    assert a wrong natural-product enantiomer or require exclusion.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted exact ChEMBL link
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source-specific xref handling
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted molecular representation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure retrieval
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated identity and xref emission
- finding_id: F2
  issue_key: enacyloxin-iia-ribosome-trapping-definition-citation
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attach later primary support to the ribosome-trapping statement
  description: The native definition_source selects PMID8665868 for a definition containing
    EF-Tu·GDP immobilization on the ribosome. That original 1996 paper reports EF-Tu·GDP
    leaving the ribosome and explicitly says enacyloxin does not inhibit its release.
    Later 1999 and 2006 studies support the trapping model. Preserve that distinction
    and attach appropriate later primary support to the corresponding statement rather
    than treating the 1996 source as support for every clause.
  target_ids:
  - antibioticmech:aro-9fd72752cb
  field_paths:
  - definition_source
  - definition
  evidence_ids:
  - owners
  - adopted1996
  - resistance-primary
  - binding2006
  rule_id: Place inspected support on the narrowest claim and preserve historical
    conflicts
  native_severity: minor
  normalization_reason: The overall target and later mechanism have primary support.
    The defect is the specific selected citation and its conflicting reported result,
    not evidence that enacyloxin lacks EF-Tu activity.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Definition and adopted reference list
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source-specific definition evidence handling
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: First-reference definition_source selection
actions:
- action_id: A1
  description: Resolve the ChEMBL exact-equivalence assertion with a documented stereochemical
    comparison in the maintained source path.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-9fd72752cb
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted exact ChEMBL link
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source-specific xref handling
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted molecular representation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure retrieval
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated identity and xref emission
  acceptance_checks:
  - Compare the actual current ChEMBL and chosen compound graph atom by atom; explicitly
    record assigned versus unassigned centres and full InChIKeys. Remove or qualify
    a non-equivalent link, or adopt a verified equivalent source identifier.
  - Do not use equal formulas, centre counts or names as exact stereo equivalence.
    Resolve complete natural-product stereochemistry from appropriate original evidence
    before any graph replacement; do not automatically transfer IVa CIP labels to
    IIa.
  - Regenerate through the maintained source path and pass focused schema, strict,
    chemistry and source-reproduction checks.
- action_id: A2
  description: Make the definition citation accurately support the later EF-Tu ribosome-trapping
    statement.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-9fd72752cb
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Definition and adopted reference list
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source-specific definition evidence handling
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: First-reference definition_source selection
  acceptance_checks:
  - Retain PMID8665868 for its demonstrated EF-Tu and incorporation results, while
    recording its contrary release result. Attach inspected later primary evidence,
    such as PMID10610785 and PMID16257965, to the trapping claim with precise read
    depth.
  - Preserve the current database-only target and resistance qualifications until
    separately curated primary evidence is installed; do not turn nucleotide-binding
    Kd or gas-phase stability into antibiotic affinity or whole-cell causality.
  - Apply claim-level definition/evidence handling in the maintained source or overlay
    and regenerate; avoid a blanket reorder of all ARO citation lists. Run focused
    schema, strict and source-reproduction checks.
limitations:
- The 1999 resistant-mutant study and 2006 crystallographic article were read at complete
  original abstract depth; the 2006 original deposition metadata and relevant mmCIF
  sections were additionally inspected. Main article access was not obtained. No detailed
  mutant MIC protocol, allele accession or crystal-density reanalysis is claimed.
- The adopted 2002 source is a secondary review, read at complete abstract depth.
  The 2007 stereochemical original was also available only as a complete abstract,
  and explicitly concerns IVa. A complete absolute-stereochemical reconstruction of
  natural IIa remains unresolved.
- The 2011 author-deposited article was inspected in selected original full-text sections
  and Table 3 text through the web tool. Direct PDF downloads returned 403 and screenshot
  rendering failed. Supplemental tables and the complete microdilution protocol were
  not inspected; no individual numerical native activity object is proposed.
- The 2024 main XML was read, including methods and figure captions, but supplements
  and figure images were not independently viewed. Its gas-phase experiments and simulations
  are not solution binding constants or bacterial MICs.
- Direct CARD pages returned 500. Current official ARO OBO stanzas were inspected
  from the same-session public download with its actual timestamp and hash.
- The initial chemistry mapping assumed that an InChI-imported tautomer would directly
  substructure-match the displayed native graph; that diagnostic failed and was corrected.
  Full native and PubChem standard-InChI agreement remains established, while the
  ChEMBL stereo discrepancy is independently demonstrated by directly mapped SMILES
  and molfile graphs.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- The native two unassigned centres are not by themselves proof of a mixture. The
  corrective xref finding is independent of a final choice of natural-product stereochemistry.
- The initial thirteen input hashes are retained alongside the appended actual owners.
  No native status promotion or source mutation is implied by these scientific assessments.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
