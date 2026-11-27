# Lugdunin: repair invalid SMILES, homodetic classification and an over-specified exact link

- Review: 20261021T195805Z-lugdunin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:32:16Z
- Finished UTC: 2026-10-21T19:58:05Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The entire native record and actual ChEBI/ARO rows were assessed. Primary figures and original supplementary characterization support the retained seven residue configurations and dynamic thiazolidine epimerism. Three major findings concern an invalid indole SMILES, a homodetic classification contradicted by the non-amide closure, and an exact ChEMBL link that fixes the interconverting centre. Bounded original antibacterial and membrane experiments support eligibility and optional mechanistic enrichment. Schema and strict validation passed; the chemical helper failed on the native SMILES as recorded.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Assigned queue position 610; one exact native record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:133127 | data/antibiotics/antibacterial/lugdunin.yaml | generated | lugdunin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | failed | False | CHEBI:133127 | Actual focused execution exited 1. Executed against batch061. The chemical helper used existing batch019 RDKit and failed on native SMILES; schema/strict were then run separately in batch061. |
| Focused schema verification | passed | True | CHEBI:133127 | Actual focused execution exited 0. Executed against batch061. The chemical helper used existing batch019 RDKit and failed on native SMILES; schema/strict were then run separately in batch061. |
| Focused strict verification | passed | True | CHEBI:133127 | Actual focused execution exited 0. Executed against batch061. The chemical helper used existing batch019 RDKit and failed on native SMILES; schema/strict were then run separately in batch061. |
| Authoritative full QC | failed | True | CHEBI:133127 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:133127 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:133127 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:133127 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:133127 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:133127 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:133127 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:133127 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:133127 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Primary-supported residue identity and invalid SMILES

identity: concern. Targets: CHEBI:133127.

The retained InChI, formula/masses, systematic synonym and seven residue configurations agree with current PubChem, ChEBI molfile and actual primary structures. Original reinjection experiments specifically justify the dynamic unassigned thiazolidine centre; it is neither evidence of a racemate nor a missing natural-residue assignment. The native SMILES still fails because the indole hydrogen was omitted.

### Chemical and ontology equivalence

grounding: concern. Targets: CHEBI:133127.

PubChem and ARO identity links are coherent, but ChEMBL fixes the dynamically interconverting thiazolidine centre and is not the same exact graph. The homodetic parent and definition conflict with the actual secondary-amine closure and the primary analogue comparison. Indole, peptide-antibiotic, thiazolidine, macrocycle and NRPS class groundings remain supported.

### Antibacterial eligibility and nasal producer

evidence: supported. Targets: CHEBI:133127.

The adopted original and additional synthetic-material experiments support antibacterial activity, including exact MRSA assays, and nasal S. lugdunensis production. Native broad bactericidal wording has original support, while individual killing-curve strain, inaccessible 2016 method details, model species and synthetic-versus-natural materials remain qualified. No blanket absence-of-resistance or human therapeutic claim is inferred.

### Optional activity, producer and membrane-mechanism representation

completeness: unknown. Targets: CHEBI:133127.

The inspected originals offer useful optional enrichment with exact strains, media, durations, material scope and evidence tiers. The lack of separate optional objects is not a native defect. Any mechanism chain should distinguish observed depolarization/proton transport from inferred nanotube assembly and simulations, and should not force a protein target.

### Source ownership, bibliography, history and actual validation

provenance: supported. Targets: CHEBI:133127.

Both inventories converge on the sole adopted original PMID, whose abstract, accessible original figures/table/SI and correction were dispositioned. Actual ChEBI and ARO owners, four history events and both source mints are coherent. All original 13 and expanded 22 hashes remain unchanged. Native validator passes are distinguished from the actual chemical failure.

## Findings

### F1: The indole SMILES omits its required nitrogen hydrogen

major / open / confirmed; issue key: lugdunin-invalid-indole-n-smiles.

chemical_structure.smiles contains Cc2cnc3ccccc23 and fails RDKit kekulization. The retained InChI, current official molfile, PubChem and original structures instead contain indole NH. A scratch-only n→[nH] repair reproduces the exact retained key and formula without changing stereochemistry. Current ChEBI repeats the invalid string, so correction must occur through source handling rather than blindly refreshing it.

### F2: Lugdunin is incorrectly classified as homodetic

major / open / confirmed; issue key: lugdunin-incorrect-homodetic-classification.

Definition and parent_compounds[0] call lugdunin a homodetic cyclic peptide. CHEBI:24613 requires exclusively peptide linkages in the ring, whereas lugdunin has six amides and a secondary-amine thiazolidine closure. The original 2019 paper explicitly contrasts lugdunin 1 with homodetic analogues 10 and 14. The current ChEBI definition repeats the source error; other supported peptide/macrocycle classes should be preserved.

### F3: The exact ChEMBL link fixes the dynamic thiazolidine centre

major / open / confirmed; issue key: lugdunin-chembl-fixed-interconverting-epimer.

Native xrefs[1] asserts CHEMBL5267022, whose current SMILES and InChI encode S at the thiazolidine carbon and yield VHMRHJACSA-N. Native and PubChem retain ZBQZSICZSA-N with that carbon unassigned. Original 2016 chromatography demonstrates rapid re-equilibration of both epimers, and 2019 reiterates their inseparability. The linked entry is a specific epimeric representation, not proof that a different whole-molecule enantiomer is present; the exact-link scope needs qualification or correction.

## Recommended Actions And Acceptance Checks

### A1

Repair the inherited indole SMILES through maintained ChEBI source handling and regenerate.

- Use the retained InChI/official molfile and actual original NH structure to justify the minimal indole hydrogen correction.
- Require successful SMILES parsing and exact agreement with retained QZNGYMKAHFFKCJ-ZBQZSICZSA-N, C40H62N8O6S, charge and masses.
- Preserve all seven residue configurations and the dynamic unassigned thiazolidine carbon; rerun chemistry and required native gates.

### A2

Correct the homodetic parent and definition through source-owned curation.

- Remove the homodetic assertion or replace it only with an independently verified appropriate cyclic-peptide parent.
- Describe the thiazolidine-containing nonribosomal macrocycle without changing supported indole, thiazolidine, peptide-antibiotic and macrocycle classifications.
- Keep natural lugdunin distinct from homodetic analogues 10/14 and rerun term/schema/strict gates after regeneration.

### A3

Adjudicate the fixed-epimer ChEMBL association instead of asserting unqualified exact equivalence.

- Retain both actual full InChIKeys and identify the sole difference at original carbon 40.
- Qualify or remove the exact link unless an upstream representation matching the native dynamic-centre scope is verified. Preserve the association as provenance where appropriate.
- Do not assign a fixed thiazolidine epimer or erase the other seven configurations merely to match a database entry.

### A4

Optional enrichment may add exact producer, activity and membrane-mechanism observations from inspected primary sources.

- Separate 2016 natural-material observations from 2019 synthetic parent and analogue assays, retaining concentration units, strain, inoculum, medium and endpoint.
- Do not import malformed final rows from the current publisher Table 1 or invent inaccessible 2016 Methods.
- Distinguish direct membrane-potential/vesicle/electrophysiology evidence from 2024 model-derived nanotube geometry; no protein target is required.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/lugdunin.yaml; Entire native record, synonym, six parents, role, class, three xrefs, document, two source concepts and four history events | supports | Native denotes lugdunin with C40H62N8O6S, neutral charge and key QZNGYMKAHFFKCJ-ZBQZSICZSA-N. Definition asserts a thiazolidine-containing homodetic cyclic peptide from human nasal bacteria with bactericidal activity including MRSA. The graph has seven assigned residue centres and an unassigned thiazolidine centre. No separate target, resistance, activity spectrum, producer, product or causal graph objects occur; definition claims remain in scope. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; Complete exact rows 2519 and 279; empty exact curator/decision subsets | context_only | ChEBI owns the adopted definition, chemistry, synonym and chemical parents. ARO owns the nonribosomal peptide class, ARO accession and ChEMBL/PubChem associations. Both adopt PMID27466123. Actual source-owner capture was expanded before detailed judgment while preserving all original 13 hashes; 22 inputs are retained. Source extraction and seeding are future generated-field owners. |
| search | /private/tmp/am-review-session/610-context-search.txt; Preserved initial search and ignored-inclusive follow-up | context_only | Exact CHEBI:133127, ARO:3003898 and lugdunin searches included hidden and ignored curation, configuration, scripts and raw inventories. No exact curator or decisions override was found in that scope. Readiness marks mechanism review as a lead, not proof of a mandatory native gap. |
| adapter | Native structured-source applicability assessment; Complete native field set and definition | context_only | The native record names no gene, locus, protein, regulator, pathway or transcriptomic dataset. A structured iModulonDB query is therefore not applicable. Biosynthetic genes encountered in additional primary and document sources were not converted to native antibacterial target assertions. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/133127/; Complete current CHEBI:133127 response | partial | Current ChEBI repeats the invalid indole SMILES and homodetic definition/parent. Its retained InChI encodes seven assigned centres and one unassigned thiazolidine centre with native formula and full key. Authority agreement does not resolve the source defects. |
| chebi-mol | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/133127/; Complete official molfile | supports | The current molfile parses and generates native QZNGYMKAHFFKCJ-ZBQZSICZSA-N. Its valid indole NH and stereochemical scope corroborate the retained InChI rather than the invalid current SMILES. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/121596231/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass/JSON; Complete asserted CID121596231 structural response | supports | Both PubChem encodings parse and give the retained native full key, formula, seven assigned residue centres and one unassigned thiazolidine centre. The asserted exact PubChem link is coherent. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL5267022.json; Complete asserted CHEMBL5267022 response | refutes | Both current ChEMBL encodings instead fix the thiazolidine carbon S and give QZNGYMKAHFFKCJ-VHMRHJACSA-N. All seven residue configurations agree with native. The difference is specifically the interconverting centre, not a different residue sequence or an enantiomer of the entire molecule. |
| aro | https://purl.obolibrary.org/obo/aro.obo; Previously retrieved official current snapshot, exact ARO:3003898 and ARO:3009657 terms | supports | ARO resolves lugdunin, its PMID27466123 source, exact chemical associations and nonribosomal peptide parent. The class definition explicitly concerns NRPS natural products. The source definition contains a producer spelling/grammar defect, but it is not the adopted native definition and is not reported as a native textual finding. Actual prior retrieval timestamp and full snapshot hash are retained. |
| document | https://en.wikipedia.org/wiki/Lugdunin; Resolved document title, chemical infobox, introduction and references | context_only | The document correctly concerns lugdunin and provides the native InChI/key plus a valid indole-NH SMILES. It is a secondary document association, not the authority for precise mechanism, producer-genome annotation or clinical efficacy. The native bibliography link resolves. |
| chemical-failure | /private/tmp/am-review-session/610-chemistry-failed.log; Actual batch019 helper execution against batch061 | refutes | The helper exited 1 at MolFromSmiles: the aromatic indole fragment Cc2cnc3ccccc23 cannot be kekulized with its neutral n lacking hydrogen. This failed execution is retained, not replaced by the later successful diagnostic calculation. Schema and strict were subsequently run separately and passed. |
| chemical-map | /private/tmp/am-review-session/610-authority-map.json; Native/current encodings and scratch-only hydrogen diagnostic | supports | Native and ChEBI SMILES both fail parsing. Native/ChEBI InChI, PubChem SMILES/InChI and ChEBI molfile agree. Changing only the indole n to [nH] in scratch restores parsing and exact retained key/formula, charge zero, average mass 783.053 and exact mass 782.451302704. ChEMBL supplies one defined thiazolidine epimer. No native file was repaired during review. |
| residue-map | /private/tmp/am-review-session/610-residue-map.json; Diagnostic RDKit zero-based atom map against actual primary structures | supports | Residue positions 1–7 map to atoms 29/22/8/4/48/41/34: L-Cys-derived thiazolidine R, D-Val R, L-Trp S, D-Leu R, L-Val S, D-Val R and L-Val-derived aldehyde S. These agree with actual 2016 Figure 2c and 2019 Scheme 1. The unassigned atom 32 corresponds to original carbon 40. Six amide bonds occur; closure C32–N33 is a secondary amine bond, with no carbonyl at C32. The macrocyclic ring contains 21 atoms. |
| mints | /private/tmp/am-review-session/610-mints.json; Independent source-mint calculation after the failed chemistry helper | supports | Both retained source mints reproduce from SHA256 of the source namespace and source ID. The failed helper did not reach this stage; this separate calculation is recorded explicitly. |
| term-24613 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/24613/; Complete current parent/role response | refutes | The definition requires a cyclic ring composed solely of amino-acid residues in peptide linkages. Lugdunin has a non-amide secondary-amine closure and does not satisfy this parent. |
| term-24828 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/24828/; Complete current parent/role response | supports | Indoles require an indole skeleton, present in the retained tryptophan side chain. |
| term-25903 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/25903/; Complete current parent/role response | supports | The peptide-antibiotic parent covers antimicrobial peptides and is supported by original activity. |
| term-35622 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/35622/; Complete current parent/role response | supports | The term is thiazolidines; the exact graph and primary characterization contain the saturated five-member N/S heterocycle. |
| term-51026 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/51026/; Complete current parent/role response | supports | Macrocycles require at least nine ring atoms; the native 21-member macrocyclic backbone qualifies. |
| term-33281 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33281/; Complete current parent/role response | supports | The antimicrobial role covers killing or slowing microorganisms; exact bacterial assays support the native use. |
| adopted2016 | PMID:27466123; DOI:10.1038/nature18634; Complete indexed abstract and accessible original publisher content | partial | Both source inventories adopt this same original. It identifies nasal S. lugdunensis production, nonribosomal biosynthesis and bactericidal activity. Human carriage association, producer competition and purified-drug effects are distinct endpoints; no clinical efficacy is inferred. The publisher main/PDF routes returned preview HTML, not full main prose or Methods. Public figures, table and SI were separately retrieved and inspected. |
| original2016-structure | https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fnature18634/MediaObjects/41586_2016_Article_BFnature18634_Fig2_HTML.jpg; Actual Figure 2c and producer/biosynthetic figure | supports | The figure labels L-Trp, D-Leu and the alternating valines, shows the indole NH, six carbonyl amides and the non-amide thiazolidine closure. A wavy bond at the thiazolidine centre explicitly preserves its ambiguity. The seven residue configurations agree with the native retained InChI and diagnostic atom map. |
| original2016-si | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnature18634/MediaObjects/41586_2016_BFnature18634_MOESM40_ESM.pdf; Supplementary discussion, all six pages; structure determination lines29–110 especially pages2–4 | supports | Original chromatography separated signals at retention times 17.0 and 17.5 min, but each isolated fraction regenerated both signals within minutes, establishing dynamic diastereomerization at carbon 40. The original cannot isolate those epimers individually. Advanced Marfey analysis used 6 N HCl hydrolysis with antioxidant/scavenger additives for 24 h at 110°C and FDLA-HPLC analysis. A minor +14 Da D-allo-isoleucine analogue was separately noted; its composition must not replace C40 lugdunin. The biosynthetic discussion is explicitly a proposed NRPS sequence, distinct from direct antibacterial targets. |
| original2016-table | https://www.nature.com/articles/nature18634/tables/1; Complete readable Table 1 rows and their actual HTML cells | partial | The correctly aligned rows report lugdunin MIC 1.5 µg/mL for MRSA USA300 LAC and NRS384; LAC remains 1.5 with 50% human serum. Mu50/SA113/RN4220 and E. faecium BK463 are 3, E. faecalis VRE366 12, L. monocytogenes ATCC19118 6 and S. pneumoniae ATCC49619 1.5 µg/mL. Final table rows are malformed in current publisher HTML, with blank species or shifted concentration cells, so those entries were not transferred. Full original MIC conditions remain outside accessible main content. |
| original2016-killing | https://www.nature.com/articles/nature18634/figures/3; Actual Figure 3 image and complete caption | partial | At 10×MIC the depicted S. aureus killing curve reaches the stated detection floor by 30 h; three experiments are reported. The caption does not identify a strain in that panel, so it is not silently labeled MRSA. Subinhibitory serial passage is a bounded failure to select resistance, not proof resistance can never arise. Mouse skin treatment reduced burdens; this is not a human efficacy result. |
| original2016-killing-image | https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fnature18634/MediaObjects/41586_2016_Article_BFnature18634_Fig3_HTML.jpg; Actual Figure 3 panels a–d inspected | context_only | The observed falling CFU curve and lower mouse skin burdens agree with the accessible caption. No curve values were independently digitized, and exact Methods unavailable in the main article were not supplied from inference. |
| correction | https://www.nature.com/articles/nature19781; Complete correction body, DOI10.1038/nature19781 | context_only | The correction amends competing-interest disclosure for the university patent application. It does not revise the chemical structure, activity data or experimental conclusions. |
| sar2019 | PMID:31059155; DOI:10.1002/anie.201901589; Complete original main XML, Table 1 and all figure captions; actual Scheme 1 and Figure 1 inspected | supports | The paper explicitly reports interconverting inseparable thiazolidine epimers. Synthetic lugdunin 1 has MIC 3.1 µg/mL (3.9 µM) against MRSA USA300 LAC. It distinguishes homodetic analogue 10, whose ring consists only of peptide bonds, and proline homodetic analogue 14; both have MIC ≥100 µg/mL. This directly contradicts calling native lugdunin homodetic. Individual residue inversion analogues are distinct from the dynamically epimerizing thiazolidine carbon. |
| sar2019-figure | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6618241/supplementaryFiles; Original archive member ANIE-58-9234-g001.jpg, actual Figure 1 | supports | The native structure1 includes indole NH and a thiazolidine non-amide bond; analogue 10 instead shows a carbonyl amide at that linkage. The proline analogue 14 is also distinct. This is a direct structural comparison, not an inferred classification based only on the title. |
| sar2019-scheme | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6618241/supplementaryFiles; Original archive member ANIE-58-9234-g006.jpg, actual Scheme 1 | supports | The synthesis scheme shows re/si attack yielding the thiazolidine epimers, with the original residue stereochemistry retained. This independently supports leaving that one carbon unspecified and does not justify fixing it to the ChEMBL S epimer. |
| sar2019-methods | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6618241/supplementaryFiles; SI member ANIE-58-9234-s001.pdf, pages11–20 and 113; actual assay page14 viewed | supports | Active synthetic peptides were HPLC-purified; the main notes partial terminal-valine racemization in crude products, so inactive crude analogues are not assumed stereopure. MIC assays used Mueller-Hinton broth, 10^6 CFU/mL, 37°C for 21 h with shaking and an OD600 no-growth endpoint. Natural lugdunin control MIC was 3.13 µg/mL; TableS3 gives lugdunin 3.1 µg/mL for NCTC8325. HRMS parent [M+H]+ calculated 783.4586/found 783.4596 supports C40 composition. Synthetic HR-LCMS characterization and epimeric NMR are reported; no unsupported numerical purity is supplied. |
| mechanism2019 | PMID:31059155; DOI:10.1002/anie.201901589; Full main membrane Results and relevant SI pages14–18 | partial | NCTC8325 DiOC2(3) depolarization correlated with activity, but PI entry remained absent up to 30 µg/mL under the stated exposure. POPC vesicles showed limited carboxyfluorescein leakage and rapid pyranine pH equilibration, supporting ion/proton transport without large membrane lesions. Membrane-potential experiments used two biological and two technical replicates each. These are cellular and model-membrane endpoints, not direct binding to a protein. The 2019 paper left carrier versus channel mechanism unresolved. |
| mechanism2024 | PMID:38664456; DOI:10.1038/s41467-024-47803-6; Main introduction, exact-lugdunin Results/Tables1–2, membrane Methods and figure captions; actual Figure 1 | partial | The later original combines experimental membrane partitioning, ATR-FTIR, vesicle transport and voltage-clamp recordings with molecular dynamics. Synthetic lugdunin 1 is distinguished from ditryptophan2 and methylated3–5. POPC black lipid membranes at 500 mM monovalent salt and +100 mV exhibited channel events after 2.5–10 nM lugdunin. Nanotube geometry and water wires integrate spectroscopic inference with simulations; they are not a bacterial protein structure or direct visualization in an infected host. Full simulation parameter derivations, videos and all supplement data were not independently audited. |
| mechanism2024-structure | https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41467-024-47803-6/MediaObjects/41467_2024_47803_Fig1_HTML.png; Actual Figure 1, structure1 and derivative legend | supports | The newer figure retains indole NH, the wavy thiazolidine bond and the original residue stereochemistry despite a changed residue-numbering origin. Derivative substituent labels belong to separately numbered analogues and are not native lugdunin. |
| access | /private/tmp/am-review-session/610-fetch1.json; /private/tmp/am-review-session/610-fetch2.json; Actual access outcomes, alternate routes and limits | context_only | Nature main and PDF requests returned preview HTML; the public original table/figures/SI/correction were readable. PMC HTML routes returned browser challenges, but Europe PMC full XML and the original supplementary archive succeeded. The guessed CARD HTML path resolved ARO:3003260 rather than lugdunin and was excluded; exact ARO terms were instead read in the verified official OBO snapshot. Failed or wrong routes were not counted as source support. |

## Limits And Additional Notes

- The original 2016 full main and Methods were not available from the publisher preview/PDF route. Its complete abstract, public Table 1, actual Figures2/3, extended captions, six-page SI and correction were inspected. Malformed final table rows were excluded.
- The 2016 supplement describes dynamic thiazolidine epimers and a minor +14 Da analogue; this review preserves that material distinction. Raw chromatographic/spectral data were not reprocessed or re-integrated.
- The 2019 full main XML and Table 1 were read; actual Scheme 1/Figure 1 and SI assay page14 were viewed. SI synthesis/purification, exact parent characterization, membrane methods and epimer commentary were inspected, not every unrelated analogue spectrum across the 117-page supplement.
- The 2024 exact-parent membrane Results, both tables, relevant Methods, figure captions and actual Figure 1 were read. Simulation force-field derivations, all supplementary figures, videos and raw channel traces were not independently reanalysed. Model-derived nanotube architecture is not treated as direct bacterial protein evidence.
- PMC HTML routes returned challenges; Europe PMC XML/archive routes succeeded. The initial CARD HTML guess resolved another accession and supplied no evidence; exact ARO terms were verified using the official OBO snapshot at its actual prior timestamp.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All original 13 and expanded 22 input hashes were verified unchanged. Only scratch evidence, diagnostic calculations and an unsaved draft were created. Native/source records, curation history, progress and Git were not modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T195805Z-lugdunin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Lugdunin: repair invalid SMILES, homodetic classification and an over-specified
  exact link'
started_at: '2026-10-21T19:32:16Z'
finished_at: '2026-10-21T19:58:05Z'
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
verdict: needs_curation
scientific_review: true
summary: The entire native record and actual ChEBI/ARO rows were assessed. Primary
  figures and original supplementary characterization support the retained seven residue
  configurations and dynamic thiazolidine epimerism. Three major findings concern
  an invalid indole SMILES, a homodetic classification contradicted by the non-amide
  closure, and an exact ChEMBL link that fixes the interconverting centre. Bounded
  original antibacterial and membrane experiments support eligibility and optional
  mechanistic enrichment. Schema and strict validation passed; the chemical helper
  failed on the native SMILES as recorded.
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
  - path: data/antibiotics/antibacterial/lugdunin.yaml
    sha256: 54604e007195af17e30caad7c9bc117060f1347e9c782fcb802da4567d2c412d
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
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
targets:
- target_id: CHEBI:133127
  path: data/antibiotics/antibacterial/lugdunin.yaml
  label: lugdunin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI and ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO classification, exact links and citation
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Assigned queue position 610; one exact native record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:133127
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: failed
  required: false
  summary: Actual focused execution exited 1. Executed against batch061. The chemical
    helper used existing batch019 RDKit and failed on native SMILES; schema/strict
    were then run separately in batch061.
  target_ids:
  - CHEBI:133127
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    610
  exit_code: 1
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against batch061. The chemical
    helper used existing batch019 RDKit and failed on native SMILES; schema/strict
    were then run separately in batch061.
  target_ids:
  - CHEBI:133127
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/lugdunin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against batch061. The chemical
    helper used existing batch019 RDKit and failed on native SMILES; schema/strict
    were then run separately in batch061.
  target_ids:
  - CHEBI:133127
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/lugdunin.yaml --out /private/tmp/am-review-session/610-strict.tsv
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
  - CHEBI:133127
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
  - CHEBI:133127
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
  - CHEBI:133127
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
  - CHEBI:133127
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
  - CHEBI:133127
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
  - CHEBI:133127
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
  - CHEBI:133127
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
  - CHEBI:133127
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
  - CHEBI:133127
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/lugdunin.yaml
  locator: Entire native record, synonym, six parents, role, class, three xrefs, document,
    two source concepts and four history events
  accessed_at: '2026-10-21T19:51:44Z'
  support: supports
  summary: Native denotes lugdunin with C40H62N8O6S, neutral charge and key QZNGYMKAHFFKCJ-ZBQZSICZSA-N.
    Definition asserts a thiazolidine-containing homodetic cyclic peptide from human
    nasal bacteria with bactericidal activity including MRSA. The graph has seven
    assigned residue centres and an unassigned thiazolidine centre. No separate target,
    resistance, activity spectrum, producer, product or causal graph objects occur;
    definition claims remain in scope.
  snapshot_sha256: 54604e007195af17e30caad7c9bc117060f1347e9c782fcb802da4567d2c412d
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv
  locator: Complete exact rows 2519 and 279; empty exact curator/decision subsets
  accessed_at: '2026-10-21T19:51:44Z'
  support: context_only
  summary: ChEBI owns the adopted definition, chemistry, synonym and chemical parents.
    ARO owns the nonribosomal peptide class, ARO accession and ChEMBL/PubChem associations.
    Both adopt PMID27466123. Actual source-owner capture was expanded before detailed
    judgment while preserving all original 13 hashes; 22 inputs are retained. Source
    extraction and seeding are future generated-field owners.
  snapshot_sha256: cbda16e7858ee9e0dc536e28ae53757b49777a8b1bd8b7d6fa8f23758190c6d4
- evidence_id: search
  kind: search
  reference: /private/tmp/am-review-session/610-context-search.txt
  locator: Preserved initial search and ignored-inclusive follow-up
  accessed_at: '2026-10-21T19:51:44Z'
  support: context_only
  summary: Exact CHEBI:133127, ARO:3003898 and lugdunin searches included hidden and
    ignored curation, configuration, scripts and raw inventories. No exact curator
    or decisions override was found in that scope. Readiness marks mechanism review
    as a lead, not proof of a mandatory native gap.
  snapshot_sha256: 197bdb338ac923c375b7b9705dfd0f6ac396a3cb655789d9ad9d5ec3a46ddbfd
  search_scope: Preserved 610-local-hits and rg --no-ignore --hidden -n -i for CHEBI:133127,
    ARO:3003898 and lugdunin across curation, conf, scripts and data/raw.
- evidence_id: adapter
  kind: search
  reference: Native structured-source applicability assessment
  locator: Complete native field set and definition
  accessed_at: '2026-10-21T19:51:44Z'
  support: context_only
  summary: The native record names no gene, locus, protein, regulator, pathway or
    transcriptomic dataset. A structured iModulonDB query is therefore not applicable.
    Biosynthetic genes encountered in additional primary and document sources were
    not converted to native antibacterial target assertions.
  snapshot_sha256: 54604e007195af17e30caad7c9bc117060f1347e9c782fcb802da4567d2c412d
  search_scope: Full native definition and structured fields checked before open source
    follow-up; no applicable named protein/pathway claim.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/133127/
  locator: Complete current CHEBI:133127 response
  accessed_at: '2026-10-21T19:41:53Z'
  support: partial
  summary: Current ChEBI repeats the invalid indole SMILES and homodetic definition/parent.
    Its retained InChI encodes seven assigned centres and one unassigned thiazolidine
    centre with native formula and full key. Authority agreement does not resolve
    the source defects.
  snapshot_sha256: 88f55ec24923c92f26dabf30d3e22e622e83c8eb8856a87ea15b48e2e36599a3
- evidence_id: chebi-mol
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/133127/
  locator: Complete official molfile
  accessed_at: '2026-10-21T19:41:53Z'
  support: supports
  summary: The current molfile parses and generates native QZNGYMKAHFFKCJ-ZBQZSICZSA-N.
    Its valid indole NH and stereochemical scope corroborate the retained InChI rather
    than the invalid current SMILES.
  snapshot_sha256: b9252e6fcd9624f12565befdf87687b0dd562510f65ba47e0cb42532c324793c
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/121596231/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass/JSON
  locator: Complete asserted CID121596231 structural response
  accessed_at: '2026-10-21T19:41:54Z'
  support: supports
  summary: Both PubChem encodings parse and give the retained native full key, formula,
    seven assigned residue centres and one unassigned thiazolidine centre. The asserted
    exact PubChem link is coherent.
  snapshot_sha256: dd3b541c9dae000c3e7b7c2aa2910cbbdc2d09fc0c11539bb6037055297bf2c4
- evidence_id: chembl
  kind: authority
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL5267022.json
  locator: Complete asserted CHEMBL5267022 response
  accessed_at: '2026-10-21T19:41:54Z'
  support: refutes
  summary: Both current ChEMBL encodings instead fix the thiazolidine carbon S and
    give QZNGYMKAHFFKCJ-VHMRHJACSA-N. All seven residue configurations agree with
    native. The difference is specifically the interconverting centre, not a different
    residue sequence or an enantiomer of the entire molecule.
  snapshot_sha256: fd9110989e2b413745e89de2cc6878b75b1419bdc047360df66227cda68b91a0
- evidence_id: aro
  kind: authority
  reference: https://purl.obolibrary.org/obo/aro.obo
  locator: Previously retrieved official current snapshot, exact ARO:3003898 and ARO:3009657
    terms
  accessed_at: '2026-10-21T15:57:42Z'
  support: supports
  summary: ARO resolves lugdunin, its PMID27466123 source, exact chemical associations
    and nonribosomal peptide parent. The class definition explicitly concerns NRPS
    natural products. The source definition contains a producer spelling/grammar defect,
    but it is not the adopted native definition and is not reported as a native textual
    finding. Actual prior retrieval timestamp and full snapshot hash are retained.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: document
  kind: database
  reference: https://en.wikipedia.org/wiki/Lugdunin
  locator: Resolved document title, chemical infobox, introduction and references
  accessed_at: '2026-10-21T19:41:57Z'
  support: context_only
  summary: The document correctly concerns lugdunin and provides the native InChI/key
    plus a valid indole-NH SMILES. It is a secondary document association, not the
    authority for precise mechanism, producer-genome annotation or clinical efficacy.
    The native bibliography link resolves.
  snapshot_sha256: 8189baa76eadb7d4df09a60d595cc9d83e4ca3ad299ad5bf85af8c290c86bf2b
- evidence_id: chemical-failure
  kind: validation
  reference: /private/tmp/am-review-session/610-chemistry-failed.log
  locator: Actual batch019 helper execution against batch061
  accessed_at: '2026-10-21T19:51:44Z'
  support: refutes
  summary: 'The helper exited 1 at MolFromSmiles: the aromatic indole fragment Cc2cnc3ccccc23
    cannot be kekulized with its neutral n lacking hydrogen. This failed execution
    is retained, not replaced by the later successful diagnostic calculation. Schema
    and strict were subsequently run separately and passed.'
  snapshot_sha256: 47aa176673286f61e716c6bd8398757ceb4bbb6107a8e99178036d4063056410
- evidence_id: chemical-map
  kind: validation
  reference: /private/tmp/am-review-session/610-authority-map.json
  locator: Native/current encodings and scratch-only hydrogen diagnostic
  accessed_at: '2026-10-21T19:51:44Z'
  support: supports
  summary: Native and ChEBI SMILES both fail parsing. Native/ChEBI InChI, PubChem
    SMILES/InChI and ChEBI molfile agree. Changing only the indole n to [nH] in scratch
    restores parsing and exact retained key/formula, charge zero, average mass 783.053
    and exact mass 782.451302704. ChEMBL supplies one defined thiazolidine epimer.
    No native file was repaired during review.
  snapshot_sha256: 281f68eb2c546a503fd682570dbdb01034e50335ec825f34551d85e20f3b4f44
- evidence_id: residue-map
  kind: validation
  reference: /private/tmp/am-review-session/610-residue-map.json
  locator: Diagnostic RDKit zero-based atom map against actual primary structures
  accessed_at: '2026-10-21T19:51:44Z'
  support: supports
  summary: 'Residue positions 1–7 map to atoms 29/22/8/4/48/41/34: L-Cys-derived thiazolidine
    R, D-Val R, L-Trp S, D-Leu R, L-Val S, D-Val R and L-Val-derived aldehyde S. These
    agree with actual 2016 Figure 2c and 2019 Scheme 1. The unassigned atom 32 corresponds
    to original carbon 40. Six amide bonds occur; closure C32–N33 is a secondary amine
    bond, with no carbonyl at C32. The macrocyclic ring contains 21 atoms.'
  snapshot_sha256: 2bbba934cc13e6f0ecad4630eb33e0c7aee20f7d13b0c035bac584220fd0b7d2
- evidence_id: mints
  kind: validation
  reference: /private/tmp/am-review-session/610-mints.json
  locator: Independent source-mint calculation after the failed chemistry helper
  accessed_at: '2026-10-21T19:51:44Z'
  support: supports
  summary: Both retained source mints reproduce from SHA256 of the source namespace
    and source ID. The failed helper did not reach this stage; this separate calculation
    is recorded explicitly.
  snapshot_sha256: fb4b68ed35aff6d0f98537fe877e6a431fb143e504dd387b8b2d7f1cf2c82a9f
- evidence_id: term-24613
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/24613/
  locator: Complete current parent/role response
  accessed_at: '2026-10-21T19:41:53Z'
  support: refutes
  summary: The definition requires a cyclic ring composed solely of amino-acid residues
    in peptide linkages. Lugdunin has a non-amide secondary-amine closure and does
    not satisfy this parent.
  snapshot_sha256: 2e18308d9a954aa3c16c9de0b05752e7748c57855ab6b7e9ec4f62032c853564
- evidence_id: term-24828
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/24828/
  locator: Complete current parent/role response
  accessed_at: '2026-10-21T19:41:54Z'
  support: supports
  summary: Indoles require an indole skeleton, present in the retained tryptophan
    side chain.
  snapshot_sha256: 6f1d1b0389a98587147007169ee4ae28d1ec771f63576cb233eeeccdb48f425d
- evidence_id: term-25903
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/25903/
  locator: Complete current parent/role response
  accessed_at: '2026-10-21T19:41:54Z'
  support: supports
  summary: The peptide-antibiotic parent covers antimicrobial peptides and is supported
    by original activity.
  snapshot_sha256: 85e8de3e0f737f2cad7481a8643e717a945d1630db4039cac4077e277df294d6
- evidence_id: term-35622
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/35622/
  locator: Complete current parent/role response
  accessed_at: '2026-10-21T19:41:54Z'
  support: supports
  summary: The term is thiazolidines; the exact graph and primary characterization
    contain the saturated five-member N/S heterocycle.
  snapshot_sha256: ae9afbea78c05b51288f9ca464d6c3eba09b8ea54aa887ccbab5f1d24db85023
- evidence_id: term-51026
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/51026/
  locator: Complete current parent/role response
  accessed_at: '2026-10-21T19:41:54Z'
  support: supports
  summary: Macrocycles require at least nine ring atoms; the native 21-member macrocyclic
    backbone qualifies.
  snapshot_sha256: 1cadb78bef0b4baceb8f03f1ee7f7065056985f8abb1a3e35ddf4f343043d4c4
- evidence_id: term-33281
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33281/
  locator: Complete current parent/role response
  accessed_at: '2026-10-21T19:41:50Z'
  support: supports
  summary: The antimicrobial role covers killing or slowing microorganisms; exact
    bacterial assays support the native use.
  snapshot_sha256: 0f66df822d1a825c02531f80cc0fcc12783ac72a0c2f0482a9d9018db0dba9e1
- evidence_id: adopted2016
  kind: primary_source
  reference: PMID:27466123; DOI:10.1038/nature18634
  locator: Complete indexed abstract and accessible original publisher content
  accessed_at: '2026-10-21T19:41:54Z'
  support: partial
  summary: Both source inventories adopt this same original. It identifies nasal S.
    lugdunensis production, nonribosomal biosynthesis and bactericidal activity. Human
    carriage association, producer competition and purified-drug effects are distinct
    endpoints; no clinical efficacy is inferred. The publisher main/PDF routes returned
    preview HTML, not full main prose or Methods. Public figures, table and SI were
    separately retrieved and inspected.
  snapshot_sha256: 3b96bc01f4f876883589a31ab20e2d1e5f91fee33f619580880d6bdf3354f9eb
- evidence_id: original2016-structure
  kind: primary_source
  reference: https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fnature18634/MediaObjects/41586_2016_Article_BFnature18634_Fig2_HTML.jpg
  locator: Actual Figure 2c and producer/biosynthetic figure
  accessed_at: '2026-10-21T19:48:34.420893Z'
  support: supports
  summary: The figure labels L-Trp, D-Leu and the alternating valines, shows the indole
    NH, six carbonyl amides and the non-amide thiazolidine closure. A wavy bond at
    the thiazolidine centre explicitly preserves its ambiguity. The seven residue
    configurations agree with the native retained InChI and diagnostic atom map.
  snapshot_sha256: 80025b8f5f11c196c68ae2f0c5da27768fd5bc27ae4f64b817ce69dd9b2f6830
- evidence_id: original2016-si
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnature18634/MediaObjects/41586_2016_BFnature18634_MOESM40_ESM.pdf
  locator: Supplementary discussion, all six pages; structure determination lines29–110
    especially pages2–4
  accessed_at: '2026-10-21T19:48:34.024708Z'
  support: supports
  summary: Original chromatography separated signals at retention times 17.0 and 17.5
    min, but each isolated fraction regenerated both signals within minutes, establishing
    dynamic diastereomerization at carbon 40. The original cannot isolate those epimers
    individually. Advanced Marfey analysis used 6 N HCl hydrolysis with antioxidant/scavenger
    additives for 24 h at 110°C and FDLA-HPLC analysis. A minor +14 Da D-allo-isoleucine
    analogue was separately noted; its composition must not replace C40 lugdunin.
    The biosynthetic discussion is explicitly a proposed NRPS sequence, distinct from
    direct antibacterial targets.
  snapshot_sha256: f33add950cc6bd084b08ad97966a536d0298cc26f047564736682c4540f1947a
- evidence_id: original2016-table
  kind: primary_source
  reference: https://www.nature.com/articles/nature18634/tables/1
  locator: Complete readable Table 1 rows and their actual HTML cells
  accessed_at: '2026-10-21T19:48:34.029106Z'
  support: partial
  summary: The correctly aligned rows report lugdunin MIC 1.5 µg/mL for MRSA USA300
    LAC and NRS384; LAC remains 1.5 with 50% human serum. Mu50/SA113/RN4220 and E.
    faecium BK463 are 3, E. faecalis VRE366 12, L. monocytogenes ATCC19118 6 and S.
    pneumoniae ATCC49619 1.5 µg/mL. Final table rows are malformed in current publisher
    HTML, with blank species or shifted concentration cells, so those entries were
    not transferred. Full original MIC conditions remain outside accessible main content.
  snapshot_sha256: 8e5a1b2b956ecd5b4b9817ac6e0fef7f81078afb259bfb2d6b2924954e20b46f
- evidence_id: original2016-killing
  kind: primary_source
  reference: https://www.nature.com/articles/nature18634/figures/3
  locator: Actual Figure 3 image and complete caption
  accessed_at: '2026-10-21T19:48:34.029476Z'
  support: partial
  summary: At 10×MIC the depicted S. aureus killing curve reaches the stated detection
    floor by 30 h; three experiments are reported. The caption does not identify a
    strain in that panel, so it is not silently labeled MRSA. Subinhibitory serial
    passage is a bounded failure to select resistance, not proof resistance can never
    arise. Mouse skin treatment reduced burdens; this is not a human efficacy result.
  snapshot_sha256: a03a3a3b44a1db4becea5f54b6b58dde272cf574b7ef171df994f03ea8ca1b69
- evidence_id: original2016-killing-image
  kind: primary_source
  reference: https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fnature18634/MediaObjects/41586_2016_Article_BFnature18634_Fig3_HTML.jpg
  locator: Actual Figure 3 panels a–d inspected
  accessed_at: '2026-10-21T19:48:34.881823Z'
  support: context_only
  summary: The observed falling CFU curve and lower mouse skin burdens agree with
    the accessible caption. No curve values were independently digitized, and exact
    Methods unavailable in the main article were not supplied from inference.
  snapshot_sha256: 7d406aa55f7872a23c80dd2f02d37331df7d3e0d0be48b380073b2a1c04953a3
- evidence_id: correction
  kind: primary_source
  reference: https://www.nature.com/articles/nature19781
  locator: Complete correction body, DOI10.1038/nature19781
  accessed_at: '2026-10-21T19:48:34.026200Z'
  support: context_only
  summary: The correction amends competing-interest disclosure for the university
    patent application. It does not revise the chemical structure, activity data or
    experimental conclusions.
  snapshot_sha256: ed9cadeb71de288c941c4fa37597f88edb6c0ebfb4dbe759e9115493d7a3d3c1
- evidence_id: sar2019
  kind: primary_source
  reference: PMID:31059155; DOI:10.1002/anie.201901589
  locator: Complete original main XML, Table 1 and all figure captions; actual Scheme
    1 and Figure 1 inspected
  accessed_at: '2026-10-21T19:41:56Z'
  support: supports
  summary: The paper explicitly reports interconverting inseparable thiazolidine epimers.
    Synthetic lugdunin 1 has MIC 3.1 µg/mL (3.9 µM) against MRSA USA300 LAC. It distinguishes
    homodetic analogue 10, whose ring consists only of peptide bonds, and proline
    homodetic analogue 14; both have MIC ≥100 µg/mL. This directly contradicts calling
    native lugdunin homodetic. Individual residue inversion analogues are distinct
    from the dynamically epimerizing thiazolidine carbon.
  snapshot_sha256: 6d0267b0daf62eea0febc46a00f59582439477d08b5f049e022b68ed21828dad
- evidence_id: sar2019-figure
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6618241/supplementaryFiles
  locator: Original archive member ANIE-58-9234-g001.jpg, actual Figure 1
  accessed_at: '2026-10-21T19:48:34.026551Z'
  support: supports
  summary: The native structure1 includes indole NH and a thiazolidine non-amide bond;
    analogue 10 instead shows a carbonyl amide at that linkage. The proline analogue
    14 is also distinct. This is a direct structural comparison, not an inferred classification
    based only on the title.
  snapshot_sha256: e86eab181245f6f7dde46d54feff1f430c747c7ce51d0d9181c5ef6f54cdabc4
- evidence_id: sar2019-scheme
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6618241/supplementaryFiles
  locator: Original archive member ANIE-58-9234-g006.jpg, actual Scheme 1
  accessed_at: '2026-10-21T19:48:34.026551Z'
  support: supports
  summary: The synthesis scheme shows re/si attack yielding the thiazolidine epimers,
    with the original residue stereochemistry retained. This independently supports
    leaving that one carbon unspecified and does not justify fixing it to the ChEMBL
    S epimer.
  snapshot_sha256: 3cc136ef4d5eb518e9a7100519dc1ba8f22aec6ff4c38827da7363477985f723
- evidence_id: sar2019-methods
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6618241/supplementaryFiles
  locator: SI member ANIE-58-9234-s001.pdf, pages11–20 and 113; actual assay page14
    viewed
  accessed_at: '2026-10-21T19:48:34.026551Z'
  support: supports
  summary: Active synthetic peptides were HPLC-purified; the main notes partial terminal-valine
    racemization in crude products, so inactive crude analogues are not assumed stereopure.
    MIC assays used Mueller-Hinton broth, 10^6 CFU/mL, 37°C for 21 h with shaking
    and an OD600 no-growth endpoint. Natural lugdunin control MIC was 3.13 µg/mL;
    TableS3 gives lugdunin 3.1 µg/mL for NCTC8325. HRMS parent [M+H]+ calculated 783.4586/found
    783.4596 supports C40 composition. Synthetic HR-LCMS characterization and epimeric
    NMR are reported; no unsupported numerical purity is supplied.
  snapshot_sha256: 65e8f3ac7e15453741d67b978adcea2904cfe13ca595189256c45602077ef011
- evidence_id: mechanism2019
  kind: primary_source
  reference: PMID:31059155; DOI:10.1002/anie.201901589
  locator: Full main membrane Results and relevant SI pages14–18
  accessed_at: '2026-10-21T19:41:56Z'
  support: partial
  summary: NCTC8325 DiOC2(3) depolarization correlated with activity, but PI entry
    remained absent up to 30 µg/mL under the stated exposure. POPC vesicles showed
    limited carboxyfluorescein leakage and rapid pyranine pH equilibration, supporting
    ion/proton transport without large membrane lesions. Membrane-potential experiments
    used two biological and two technical replicates each. These are cellular and
    model-membrane endpoints, not direct binding to a protein. The 2019 paper left
    carrier versus channel mechanism unresolved.
  snapshot_sha256: 6d0267b0daf62eea0febc46a00f59582439477d08b5f049e022b68ed21828dad
- evidence_id: mechanism2024
  kind: primary_source
  reference: PMID:38664456; DOI:10.1038/s41467-024-47803-6
  locator: Main introduction, exact-lugdunin Results/Tables1–2, membrane Methods and
    figure captions; actual Figure 1
  accessed_at: '2026-10-21T19:41:56Z'
  support: partial
  summary: The later original combines experimental membrane partitioning, ATR-FTIR,
    vesicle transport and voltage-clamp recordings with molecular dynamics. Synthetic
    lugdunin 1 is distinguished from ditryptophan2 and methylated3–5. POPC black lipid
    membranes at 500 mM monovalent salt and +100 mV exhibited channel events after
    2.5–10 nM lugdunin. Nanotube geometry and water wires integrate spectroscopic
    inference with simulations; they are not a bacterial protein structure or direct
    visualization in an infected host. Full simulation parameter derivations, videos
    and all supplement data were not independently audited.
  snapshot_sha256: a2f0240eb6b6a1931da63c9310508b0bb6a479dc998bc3abf08c6927fec77fe7
- evidence_id: mechanism2024-structure
  kind: primary_source
  reference: https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41467-024-47803-6/MediaObjects/41467_2024_47803_Fig1_HTML.png
  locator: Actual Figure 1, structure1 and derivative legend
  accessed_at: '2026-10-21T19:48:34.228722Z'
  support: supports
  summary: The newer figure retains indole NH, the wavy thiazolidine bond and the
    original residue stereochemistry despite a changed residue-numbering origin. Derivative
    substituent labels belong to separately numbered analogues and are not native
    lugdunin.
  snapshot_sha256: 1f5b38ced3e908683f7c78a7ff6f88139002118498d67363106dc356e0512c27
- evidence_id: access
  kind: validation
  reference: /private/tmp/am-review-session/610-fetch1.json; /private/tmp/am-review-session/610-fetch2.json
  locator: Actual access outcomes, alternate routes and limits
  accessed_at: '2026-10-21T19:51:44Z'
  support: context_only
  summary: Nature main and PDF requests returned preview HTML; the public original
    table/figures/SI/correction were readable. PMC HTML routes returned browser challenges,
    but Europe PMC full XML and the original supplementary archive succeeded. The
    guessed CARD HTML path resolved ARO:3003260 rather than lugdunin and was excluded;
    exact ARO terms were instead read in the verified official OBO snapshot. Failed
    or wrong routes were not counted as source support.
  snapshot_sha256: bf373e038b6e4dd435816ad43a450308c3fd2fc6d1a7e518a38489206f725a95
assessments:
- assessment_id: identity
  area: identity
  topic: Primary-supported residue identity and invalid SMILES
  outcome: concern
  summary: The retained InChI, formula/masses, systematic synonym and seven residue
    configurations agree with current PubChem, ChEBI molfile and actual primary structures.
    Original reinjection experiments specifically justify the dynamic unassigned thiazolidine
    centre; it is neither evidence of a racemate nor a missing natural-residue assignment.
    The native SMILES still fails because the indole hydrogen was omitted.
  target_ids:
  - CHEBI:133127
  evidence_ids:
  - native
  - chemical-failure
  - chemical-map
  - residue-map
  - original2016-structure
  - original2016-si
  - sar2019-scheme
- assessment_id: grounding
  area: grounding
  topic: Chemical and ontology equivalence
  outcome: concern
  summary: PubChem and ARO identity links are coherent, but ChEMBL fixes the dynamically
    interconverting thiazolidine centre and is not the same exact graph. The homodetic
    parent and definition conflict with the actual secondary-amine closure and the
    primary analogue comparison. Indole, peptide-antibiotic, thiazolidine, macrocycle
    and NRPS class groundings remain supported.
  target_ids:
  - CHEBI:133127
  evidence_ids:
  - chebi
  - pubchem
  - chembl
  - aro
  - term-24613
  - term-24828
  - term-25903
  - term-35622
  - term-51026
  - sar2019
  - residue-map
- assessment_id: evidence
  area: evidence
  topic: Antibacterial eligibility and nasal producer
  outcome: supported
  summary: The adopted original and additional synthetic-material experiments support
    antibacterial activity, including exact MRSA assays, and nasal S. lugdunensis
    production. Native broad bactericidal wording has original support, while individual
    killing-curve strain, inaccessible 2016 method details, model species and synthetic-versus-natural
    materials remain qualified. No blanket absence-of-resistance or human therapeutic
    claim is inferred.
  target_ids:
  - CHEBI:133127
  evidence_ids:
  - adopted2016
  - original2016-table
  - original2016-killing
  - original2016-si
  - sar2019
  - sar2019-methods
  - term-33281
- assessment_id: completeness
  area: completeness
  topic: Optional activity, producer and membrane-mechanism representation
  outcome: unknown
  summary: The inspected originals offer useful optional enrichment with exact strains,
    media, durations, material scope and evidence tiers. The lack of separate optional
    objects is not a native defect. Any mechanism chain should distinguish observed
    depolarization/proton transport from inferred nanotube assembly and simulations,
    and should not force a protein target.
  target_ids:
  - CHEBI:133127
  evidence_ids:
  - adapter
  - search
  - mechanism2019
  - mechanism2024
  - sar2019-methods
  - access
- assessment_id: provenance
  area: provenance
  topic: Source ownership, bibliography, history and actual validation
  outcome: supported
  summary: Both inventories converge on the sole adopted original PMID, whose abstract,
    accessible original figures/table/SI and correction were dispositioned. Actual
    ChEBI and ARO owners, four history events and both source mints are coherent.
    All original 13 and expanded 22 hashes remain unchanged. Native validator passes
    are distinguished from the actual chemical failure.
  target_ids:
  - CHEBI:133127
  evidence_ids:
  - owners
  - native
  - mints
  - adopted2016
  - correction
  - chemical-failure
  - access
findings:
- finding_id: F1
  issue_key: lugdunin-invalid-indole-n-smiles
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The indole SMILES omits its required nitrogen hydrogen
  description: chemical_structure.smiles contains Cc2cnc3ccccc23 and fails RDKit kekulization.
    The retained InChI, current official molfile, PubChem and original structures
    instead contain indole NH. A scratch-only n→[nH] repair reproduces the exact retained
    key and formula without changing stereochemistry. Current ChEBI repeats the invalid
    string, so correction must occur through source handling rather than blindly refreshing
    it.
  target_ids:
  - CHEBI:133127
  field_paths:
  - chemical_structure.smiles
  evidence_ids:
  - native
  - owners
  - chebi
  - chebi-mol
  - chemical-failure
  - chemical-map
  - original2016-structure
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI and ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  rule_id: 'review-yaml-record: chemical representation consistency'
  normalization_reason: Major invalid structural representation. Independent InChI,
    formula, authorities and primary structures still identify the intended compound,
    so this is not a wrong-identity blocker.
- finding_id: F2
  issue_key: lugdunin-incorrect-homodetic-classification
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Lugdunin is incorrectly classified as homodetic
  description: Definition and parent_compounds[0] call lugdunin a homodetic cyclic
    peptide. CHEBI:24613 requires exclusively peptide linkages in the ring, whereas
    lugdunin has six amides and a secondary-amine thiazolidine closure. The original
    2019 paper explicitly contrasts lugdunin 1 with homodetic analogues 10 and 14.
    The current ChEBI definition repeats the source error; other supported peptide/macrocycle
    classes should be preserved.
  target_ids:
  - CHEBI:133127
  field_paths:
  - definition
  - parent_compounds[0]
  evidence_ids:
  - native
  - owners
  - term-24613
  - residue-map
  - original2016-structure
  - sar2019
  - sar2019-figure
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI and ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  rule_id: 'review-yaml-record: ontology and definition accuracy'
  normalization_reason: Major wrong ontology grounding and linked definition claim;
    the label and molecular identity remain recoverable and should not be replaced
    by a homodetic analogue.
- finding_id: F3
  issue_key: lugdunin-chembl-fixed-interconverting-epimer
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The exact ChEMBL link fixes the dynamic thiazolidine centre
  description: Native xrefs[1] asserts CHEMBL5267022, whose current SMILES and InChI
    encode S at the thiazolidine carbon and yield VHMRHJACSA-N. Native and PubChem
    retain ZBQZSICZSA-N with that carbon unassigned. Original 2016 chromatography
    demonstrates rapid re-equilibration of both epimers, and 2019 reiterates their
    inseparability. The linked entry is a specific epimeric representation, not proof
    that a different whole-molecule enantiomer is present; the exact-link scope needs
    qualification or correction.
  target_ids:
  - CHEBI:133127
  field_paths:
  - xrefs[1]
  evidence_ids:
  - native
  - owners
  - chembl
  - pubchem
  - chemical-map
  - original2016-si
  - sar2019-scheme
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI and ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO classification, exact links and citation
  rule_id: 'review-yaml-record: exact chemical grounding'
  normalization_reason: Major over-specific exact chemical equivalence. The primary-supported
    native dynamic-centre representation is retained, without asserting a wrong natural
    residue configuration.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - CHEBI:133127
  description: Repair the inherited indole SMILES through maintained ChEBI source
    handling and regenerate.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI and ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  generator: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  acceptance_checks:
  - Use the retained InChI/official molfile and actual original NH structure to justify
    the minimal indole hydrogen correction.
  - Require successful SMILES parsing and exact agreement with retained QZNGYMKAHFFKCJ-ZBQZSICZSA-N,
    C40H62N8O6S, charge and masses.
  - Preserve all seven residue configurations and the dynamic unassigned thiazolidine
    carbon; rerun chemistry and required native gates.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - CHEBI:133127
  description: Correct the homodetic parent and definition through source-owned curation.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI and ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  generator: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  acceptance_checks:
  - Remove the homodetic assertion or replace it only with an independently verified
    appropriate cyclic-peptide parent.
  - Describe the thiazolidine-containing nonribosomal macrocycle without changing
    supported indole, thiazolidine, peptide-antibiotic and macrocycle classifications.
  - Keep natural lugdunin distinct from homodetic analogues 10/14 and rerun term/schema/strict
    gates after regeneration.
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - CHEBI:133127
  description: Adjudicate the fixed-epimer ChEMBL association instead of asserting
    unqualified exact equivalence.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI and ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO classification, exact links and citation
  generator: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  acceptance_checks:
  - Retain both actual full InChIKeys and identify the sole difference at original
    carbon 40.
  - Qualify or remove the exact link unless an upstream representation matching the
    native dynamic-centre scope is verified. Preserve the association as provenance
    where appropriate.
  - Do not assign a fixed thiazolidine epimer or erase the other seven configurations
    merely to match a database entry.
- action_id: A4
  finding_ids: []
  target_ids:
  - CHEBI:133127
  description: Optional enrichment may add exact producer, activity and membrane-mechanism
    observations from inspected primary sources.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI and ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO classification, exact links and citation
  acceptance_checks:
  - Separate 2016 natural-material observations from 2019 synthetic parent and analogue
    assays, retaining concentration units, strain, inoculum, medium and endpoint.
  - Do not import malformed final rows from the current publisher Table 1 or invent
    inaccessible 2016 Methods.
  - Distinguish direct membrane-potential/vesicle/electrophysiology evidence from
    2024 model-derived nanotube geometry; no protein target is required.
limitations:
- The original 2016 full main and Methods were not available from the publisher preview/PDF
  route. Its complete abstract, public Table 1, actual Figures2/3, extended captions,
  six-page SI and correction were inspected. Malformed final table rows were excluded.
- The 2016 supplement describes dynamic thiazolidine epimers and a minor +14 Da analogue;
  this review preserves that material distinction. Raw chromatographic/spectral data
  were not reprocessed or re-integrated.
- The 2019 full main XML and Table 1 were read; actual Scheme 1/Figure 1 and SI assay
  page14 were viewed. SI synthesis/purification, exact parent characterization, membrane
  methods and epimer commentary were inspected, not every unrelated analogue spectrum
  across the 117-page supplement.
- The 2024 exact-parent membrane Results, both tables, relevant Methods, figure captions
  and actual Figure 1 were read. Simulation force-field derivations, all supplementary
  figures, videos and raw channel traces were not independently reanalysed. Model-derived
  nanotube architecture is not treated as direct bacterial protein evidence.
- PMC HTML routes returned challenges; Europe PMC XML/archive routes succeeded. The
  initial CARD HTML guess resolved another accession and supplied no evidence; exact
  ARO terms were verified using the official OBO snapshot at its actual prior timestamp.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All original 13 and expanded 22 input hashes were verified unchanged. Only scratch
  evidence, diagnostic calculations and an unsaved draft were created. Native/source
  records, curation history, progress and Git were not modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
