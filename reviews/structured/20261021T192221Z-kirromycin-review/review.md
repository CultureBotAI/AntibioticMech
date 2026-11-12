# Kirromycin: terminal alkene identity and EF-Tu domain corrections

- Review: 20261021T192221Z-kirromycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:53:54Z
- Finished UTC: 2026-10-21T19:22:21Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native graph is internally valid but encodes the terminal C37=C38 bond as E, whereas inspected original structures and independent ChEBI/CCD encodings specify Z. A separate ChEMBL exact reference also differs at a tetrahedral centre. The definition incorrectly names the EF-Tu I/II interface; original mutation, binding and structural studies support I/III. The two qualified CARD resistance assertions are reproducible and have relevant primary support. One blocker and two major findings require source-owned correction.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 576; one complete native record. All thirteen initial input hashes remain unchanged; four actual source-owner inputs were appended before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-8b2f0e38fa | data/antibiotics/antibacterial/kirromycin.yaml | generated | kirromycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | antibioticmech:aro-8b2f0e38fa | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-8b2f0e38fa | Actual focused execution exited 0. |
| Focused chemistry verification | failed | False | antibioticmech:aro-8b2f0e38fa | The optional chemistry helper exited 1 because native average_mass 796.9 differs from RDKit 796.955 by 0.055, exceeding its fixed 0.05 tolerance. Both serializations parse and reproduce the stored formula, charge, monoisotopic mass, key and source mint. This precision difference is not the stereochemical identity finding. |
| Independent exact chemical authority and bond diagnostic | passed | False | antibioticmech:aro-8b2f0e38fa | Both native serializations and PubChem agree. Changing only canonical InChI C9=C11 from E to Z reproduces the ChEBI InChI and CCD KIR key. ChEMBL additionally requires inversion at canonical C27 to reproduce that key. |
| Authoritative full QC | failed | True | antibioticmech:aro-8b2f0e38fa | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-8b2f0e38fa | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-8b2f0e38fa | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-8b2f0e38fa | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-8b2f0e38fa | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-8b2f0e38fa | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-8b2f0e38fa | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-8b2f0e38fa | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-8b2f0e38fa | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Constitution, stereo and chemical properties

identity: concern. Targets: antibioticmech:aro-8b2f0e38fa.

The chemical strings are mutually valid and the stored properties are consistent within source precision. The natural-product identity nevertheless fails at one positively mapped terminal alkene: native E versus primary Z.

### Five exact references and class terms

grounding: concern. Targets: antibioticmech:aro-8b2f0e38fa.

ARO and current PubChem reproduce the record. ChEBI and public CAS-associated material instead have terminal Z, and ChEMBL adds an independent tetrahedral conflict. The elfamycin parent/class is appropriate at its declared source scope; it is not proof of the native exact stereoisomer.

### EF-Tu interface and inhibited step

evidence: concern. Targets: antibioticmech:aro-8b2f0e38fa.

The core EF-Tu trapping mechanism is supported for natural kirromycin, but I/II is positively contradicted by I/III mapping and later structural context. GTP-like is more accurate than an identical GTP conformation. Translocation should be stated as a downstream consequence of the earlier stall, not a direct EF-G inhibition.

### Both qualified CARD determinant assertions

evidence: supported. Targets: antibioticmech:aro-8b2f0e38fa.

Both exact CARD edges reproduce the maintained source and have relevant original experimental support. The native database-only evidence status is honest; no clinical breakpoint, strain MIC or direct-binding primary claim is added. All activity and mechanism material must be reconciled with the native terminal-E identity before scientific sign-off.

### Antibacterial filing and biological material

evidence: supported. Targets: antibioticmech:aro-8b2f0e38fa.

The primary studies establish bacterial translation inhibition and whole-cell resistance selection for named natural kirromycin. The ANTIBACTERIAL filing is appropriate for that named compound, but it cannot validate the separately encoded E-terminal isomer without identity reconciliation. Aurodox and other elfamycins are not quantitative substitutes.

### Source ownership, history and evidence placement

provenance: supported. Targets: antibioticmech:aro-8b2f0e38fa.

All native values and history are accounted for by the maintained ARO/PubChem sources. The first-PMID definition citation is an importer choice and does not make every inherited mechanistic clause a finding of that paper. Source status and timestamp facts remain intact.

### All native assertions and all seven adopted leads

completeness: supported. Targets: antibioticmech:aro-8b2f0e38fa.

The entire native record and actual source rows were inspected. Four adopted original articles were read fully, two at complete-abstract depth, and the secondary 1985 review at metadata depth. Additional binding and cryo-EM sources were read at the stated selected scope. Missing optional target, MIC, producer and graph objects are not defects.

## Findings

### F1: Correct the terminal alkene identity through the maintained source

blocker / open / confirmed; issue key: kirromycin-terminal-c37-c38-geometry.

The native SMILES and InChI encode conventional C37=C38 as E. Original numbered structures from 1988 and 1989 and the 2018 primary figure depict Z; independently parsed CCD KIR and ChEBI InChI agree. A scratch change of only canonical InChI C9=C11 from E to Z reproduces their full key while preserving all other stereo assignments. The record therefore denotes a different stereoisomer from the named experimental natural product. Correct the source association and regenerate after independent atom/bond review; this finding does not establish that the E isomer is inactive.

### F2: Resolve the additional ChEMBL exact-reference conflict

major / open / confirmed; issue key: kirromycin-chembl-exact-stereocentre-conflict.

CHEMBL4297102 agrees with terminal Z but assigns the opposite canonical InChI C27 tetrahedral configuration from native, CCD and ChEBI. Its SMILES, InChI and molfile agree with each other. Inverting that centre alone reproduces the CCD key. Preserve any useful related-isomer association with explicit semantics or suppress the unsupported exact equivalence; do not copy the entire ChEMBL graph to repair the terminal bond.

### F3: Correct the EF-Tu binding interface and clarify the stalled step

major / open / confirmed; issue key: kirromycin-eftu-domain-interface.

The inherited definition names domains 1,2, whereas the original mutation/binding studies locate the relevant interface at I/III and subsequent kirromycin-stalled structural studies support that assignment. Preserve the supported EF-Tu trapping mechanism, describe the post-hydrolysis state as GTP-like, and distinguish failed EF-Tu release/aa-tRNA accommodation from downstream cessation of elongation. The cited 1974 paper explicitly found no direct inhibition in its separate EF-G translocation assay.

## Recommended Actions And Acceptance Checks

### A1

Repair the source-owned exact structure and cross-reference mapping.

- Map conventional C37=C38 to canonical C9=C11 and independently confirm Z from original drawings; retain all other validated centres and bonds unless separate evidence supports a change.
- Resolve the ChEMBL C27 conflict separately. Check every retained exact xref against the selected complete structure; association fields must state their broader relation.
- Regenerate through maintained sources, preserve provenance and reassess all inherited biological material against the corrected exact entity. Run schema, strict, structure and source-reproduction gates.

### A2

Correct the inherited mechanism wording and attach each claim to the appropriate experiment.

- Use I/III rather than I/II and cite the actual mutation/binding and structural sources at their measured scope.
- Keep EF-Tu release/accommodation, peptide formation and EF-G translocation distinct. Use GTP-like intermediate wording and avoid claiming exact identity with the isolated GTP state.
- Do not attribute all detailed structural claims to PMID4373734 merely because it is the first imported definition reference.

### A3

Preserve the supported resistance assertions and qualify any future enrichment.

- Retain database qualification unless original primary observations are separately curated with organism, mutant, assay and material context. Check CARD PMID1552908 before using it as kirromycin support.
- Do not transfer aurodox hybrid/preincubation results, Table2 values lacking a kirromycin row, or cell-free EC50 values as MICs.
- S. cinnamoneus is a kirrothricin producer in PMID9043138; the separate S. collinus biosynthesis study supports kirromycin production. Biosynthetic enzymes are not antibacterial targets.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/kirromycin.yaml; Entire native record, including all five xrefs, two resistance objects and three history events. | supports | ARO-seeded MINTED kirromycin has the valid neutral C43H60N2O12 graph HMSYAPGFKGSXAJ-GFNGQHCCSA-N, eleven assigned tetrahedral centres and seven E double bonds. The definition names EF-Tu domains 1,2 and describes retention after GTP hydrolysis. Mocimycin is an exact synonym. Both resistance objects explicitly remain CARD database assertions. There are no native quantitative activity, clinical, producer, molecular-target, causal-graph, pathway or dataset objects. |
| owners | data/raw/aro_antibiotics.tsv:222; data/raw/pubchem_structures.tsv:58; data/raw/aro_resistance_edges.tsv:3898-3899; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py; Exact inventory rows and relevant configuration/extractor/fallback, definition selection and CARD edge emission branches. | supports | The record reproduces the ARO definition, seven source references and two determinant edges. PubChem CID 135452521 supplies its structure because no adopted ChEBI inventory row supplies this concept. The seeder selects the first ARO definition PMID, emits imported exact xrefs and labels CARD edges as database assertions. Current two-star ChEBI availability does not retroactively make the historical MINTED status an error. All thirteen initial hashes are preserved; the four actual owner inputs were appended. |
| local-search | /private/tmp/am-review-session/576-local-hits.txt; /private/tmp/am-review-session/576-owner-hits.txt; Ignored-inclusive and hidden-inclusive exact label, identifier and slug search; native source row cross-check. | context_only | Searches included ignored and hidden files. Hits included inventories, native and generated records, historical research ledgers and related elfamycins. Historical reports were leads only. No optional field absence is promoted into a defect; the entire native file determines its actual assertion set. |
| aro | https://purl.obolibrary.org/obo/aro.obo; Official current snapshot: ARO3001234,3001310,3001219,3003359,3003368 and0001001. | supports | All six terms were read. Current ARO repeats the I/II definition, the synonym, five chemical associations and both exact kirromycin resistance relations. ARO3001219 is the elfamycin target-based antibiotic class, not a claim that every member has one conserved backbone. The seven adopted definition references are unchanged. The snapshot was fetched at 2026-10-21T15:57:42Z and extracted into 576-current-aro-terms.json. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/190786/; Complete official response and independently parsed default structure. | supports | CHEBI190786 labels the compound Mocimycin and associates CAS50935-71-2 and CCD KIR. Its valid InChI encodes terminal Z and has key HMSYAPGFKGSXAJ-PAHGNTJYSA-N. Its supplied aromatic SMILES independently fails parsing; that separate upstream serialization problem is not present in the native PubChem SMILES. The two-star entry is corroboration, not sole experimental proof. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/135452521; Current structure properties and CAS-based public lookup. | supports | CID 135452521 reproduces both native serializations and the all-E key. In contrast, a public lookup of CAS50935-71-2 returns CID 135484176 with the Z-terminal PAHGNTJY key. CAS identity was corroborated by public associations, not inspected in a licensed registry. |
| ccd | https://data.rcsb.org/rest/v1/core/chemcomp/KIR; Complete chemical component and CACTVS/OpenEye stereochemical SMILES plus InChI. | supports | All three independently parsed CCD KIR encodings agree with C43H60N2O12 and HMSYAPGFKGSXAJ-PAHGNTJYSA-N. The terminal diene is E,Z; all eleven tetrahedral centres agree with the native graph. The only native-versus-CCD stereo difference is the terminal double bond. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL4297102.json; Complete official structure fields, with SMILES, InChI and molfile independently parsed. | supports | All three ChEMBL encodings give HMSYAPGFKGSXAJ-UIMKWNSLSA-N. They agree with terminal Z but invert canonical InChI C27 relative to CCD/ChEBI/native. Canonical C27 is the methyl-bearing linker centre adjacent to the methoxy-bearing carbon and the tetrahydrofuran ring. This additional discrepancy is separate from the native terminal alkene. |
| mapping | /private/tmp/am-review-session/576-authority-chemistry.json; Reproducible independent parsing and one-bond/one-centre scratch diagnostics. | supports | Only changing native canonical C9=C11 from E to Z gives the exact CCD/ChEBI PAHGNTJY key. The bond maps to conventional C37=C38 in the original numbered structure, at the methyl-terminated end of the goldinonic-acid side chain. Separately, only inverting canonical ChEMBL C27 gives the same PAHGNTJY key. No native file was changed. |
| nmr1988 | PMID:3356609; DOI:10.7164/antibiotics.41.202; Complete original five-page article read; numbered structure1 on p202 visually inspected, Methods and Results read. | supports | The exact kirromycin/mocimycin drawing has terminal C37=C38 Z. Purified mocimycin was studied with deuterated E. coli EF-Tu by proton NMR. Titration supports a 1:1 complex and a protein conformation resembling, but not identical to, the GTP form. The NMR study is not an atomic domain-binding map. Its named material does not validate the native E-terminal isomer. |
| activity1989 | PMID:2499247; DOI:10.1128/AAC.33.3.322; All four original scanned pages read, including Figure1 and both tables. | supports | Figure 1 independently depicts terminal Z. Kirromycin supplied by Jill Barber gave E. coli cell-free EC50 values of 0.23 µM for poly(Phe) synthesis and EF-Tu-dependent GTPase in Table 1. These are biochemical endpoints, not MICs or binding constants. Table 2 does not give a kirromycin row; the hybrid ribosome/factor and preincubation experiments concern aurodox, so those exact results are not transferred to kirromycin. |
| biosynthesis2018 | PMID:29459765; DOI:10.1038/s41598-018-21507-6; Introduction, Methods, selected Results/Discussion and original Figure1A inspected; full XML downloaded. | supports | Figure 1A again depicts the methyl-terminal alkene as Z. Experiments use wild-type Streptomyces collinus Tü365 and biosynthetic gene mutants, with HPLC-HRMS and NMR analysis of derivatives. This is direct producer/biosynthetic context, not a bacterial target assay. The native record has no producer object requiring correction. Unrelated derivative and biosynthetic-enzyme results are not promoted into kirromycin antibacterial targets. |
| mechanism1974 | PMID:4373734; DOI:10.1073/pnas.71.12.4910; All five original scanned pages read, including Tables1-3 and Discussion. | supports | The cited primary paper supports EF-Tu-dependent inhibition, retention of EF-Tu after GTP hydrolysis and effects on EF-Tu nucleotide/tRNA interactions. It explicitly distinguishes inhibition of EF-Tu-dependent peptide formation from direct peptidyltransferase or EF-G-driven translocation inhibition; those separate activities were unaffected under the reported tests. The paper does not assign the I/II binding interface. The historical stated molecular weight794 is not used as modern identity evidence. |
| resistance1977 | PMID:337296; DOI:10.1073/pnas.74.10.4341; All five original scanned pages read, Methods, Figures1-5 and Discussion. | supports | E. coli D22-derived D2216 carries resistant tufB-associated EF-Tu with an inactive or deficient second tuf contribution; complementation and cell-free mixing show dominance of sensitivity. Temperature-dependent 80-700-fold differences are cell-free response shifts, not clinical MIC fold changes. The study supports exact kirromycin target-alteration resistance while distinguishing uptake effects and genetic background. |
| binding1994 | PMID:7525272; DOI:10.1002/j.1460-2075.1994.tb06815.x; Complete abstract and original pp4877,4881-4884 visually read; Figures7-11 and Methods on p4884 inspected. | supports | E. coli EF-Tu G316D, A375T, A375V and Q124K show altered kirromycin binding and biochemical sensitivity. The mutations map to the I/III interface in the GTP state, and the authors propose binding near or in that interface. Binding and release effects are distinguished. The crystallographic mapping used existing factor structures; this paper is not itself a direct kirromycin co-crystal. |
| mutation1994 | PMID:7925958; DOI:10.1016/0014-5793(94)00937-6; Complete indexed original abstract; official free PDF route returned403. | supports | Thirteen resistance substitutions at seven sites cluster at domains I and III in EF-Tu-GTP, supporting the proposed interface. The full title and abstract say I/III. The later 2002 article bibliography incorrectly renders this title as I/II; that bibliographic typo must not override the inspected original abstract. No specific numerical binding constant is extracted. |
| resistance1997 | PMID:9043138; DOI:10.1099/00221287-143-2-617; Complete original indexed abstract; publisher full-text route returned403. | supports | The kirrothricin producer S. cinnamoneus supplies an EF-Tu resistant to kirromycin in a poly(U)-directed cell-free assay. A Thr378-to-Ala substitution increases kirromycin sensitivity; GE2270 sensitivity is separately described. This supports the named determinant context but does not make S. cinnamoneus a demonstrated kirromycin producer or establish a clinical MIC. |
| cryoem2002 | https://pmc.ncbi.nlm.nih.gov/articles/PMC126079/; Introduction, Results on domain fitting, TableI, relevant Discussion and complete Methods inspected. | supports | Kirromycin-stalled E. coli ribosome/EF-Tu/GDP/aa-tRNA reconstructions support a GTP-like intermediate and failure of normal accommodation/release. Domain I/III is the binding-site context; domain II contacts 16S rRNA and must not be confused with the drug interface. The map is an ensemble with partial occupancy and fitted coordinates, not proof that the factor is exactly identical to the free GTP state. |
| cryoem2009 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2666022/; Selected Results paragraphs on molecular-model construction and EF-Tu conformation. | context_only | This kirromycin-stalled ribosomal study explicitly distinguishes its cryo-EM complex, the aurodox/methylkirromycin crystal model used in docking, and exact kirromycin entry1OB2. The models support I/III and a particular intermediate geometry; aurodox atomic contacts are not automatically exact kirromycin observations. |
| pdb | https://www.rcsb.org/structure/1OB2; Official structure-entry metadata and CCD KIR checked. | context_only | 1OB2 is an exact kirromycin-containing EF-Tu/guanine-nucleotide-analogue/tRNA structural dataset at 3.35 Å. Its primary citation is marked To be published; it is not represented here as a published primary article or as GDP-state evidence. |
| review-leads | PMID:3904612; DOI:10.1146/annurev.mi.39.100185.003013; PMID:12370016; DOI:10.2174/1389203023380855; Adopted1985 review metadata and later CARD-linked2002 review complete abstract. | context_only | The 1985 adopted review has no indexed abstract and its full text was not obtained. The 2002 review discusses EF-Tu antibiotics but is secondary context. Neither is typed as direct experimental evidence. |
| card-citation-limit | ARO:3003368; PMID:1552908; DOI:10.1007/BF00299141; Current CARD reference list and indexed original title/abstract, truncated at250 words. | context_only | One CARD-linked reference concerns rpsL alleles and streptomycin resistance rather than a demonstrated kirromycin/EF-Tu experiment. This upstream citation association should be checked before any primary-evidence upgrade. It does not refute the independently supported, explicitly database-qualified native resistance assertion. |
| adapter | iModulonDB e_coli/precise1k genes b3339 and b3980; Actual catalog and tufA/tufB structured searches before web research; execution manifest576-adapter.json. | context_only | The 28-dataset catalog lacks S. cinnamoneus. Exact E. coli searches resolve tufA to b3339 and tufB to b3980, with no matching modules. These annotations corroborate gene naming only; no binding, resistance, expression module or phenotype is inferred from them. |

## Limits And Additional Notes

- The optional chemistry helper really exited 1 on average-mass precision; all structural parsing and mint comparisons succeeded. Required focused schema and strict checks exited 0. Initial copied helper runs accidentally targeted jadomycin B; their outputs are retained under 576-initial-wrong-target-* and excluded from the kirromycin check results. The corrected commands were rerun against kirromycin.
- The four adopted 1974,1977,1988 and 1989 original articles were read fully. The 1997 and 1994 FEBS originals were available as complete abstracts; official publisher routes returned 403. The1985 secondary review had metadata only.
- The additional 1994 EMBO original was inspected at pp 4877 and 4881-4884, including relevant figures and Methods, rather than claimed fully read. The 2002 and 2009 cryo-EM articles were used only at the selected sections stated in their evidence entries.
- The 2018 primary source was inspected for structure and producer/biosynthetic context at the stated sections; its original Figure 1A was viewed. The Springer image route returned HTML despite 200, so only the successfully fetched PMC image is used. Raw NMR spectra were not reprocessed.
- ChEBI supplies an invalid aromatic SMILES alongside a valid Z-terminal InChI; the native PubChem SMILES is valid. The review does not silently substitute one full external graph or equate parsing failure with the separate native stereochemical conflict.
- CAS corroboration used public associations rather than licensed registry access. The bounded literature search captured the first 100 of 119 hits; selected relevant studies were followed, not an exhaustive literature census. Missing optional observations are not proof that no other biological evidence exists.
- The exact natural-material mechanism and resistance evidence cannot automatically be attached to the native E-terminal stereoisomer. No activity or inactivity claim about that isolated isomer is established by this review.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Original capture hashes are preserved. Public retrieval manifests retain actual URLs, UTC timestamps, response status and hashes. The current ARO snapshot is shared with its original retrieval timestamp; all exact terms were independently inspected for this record.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T192221Z-kirromycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Kirromycin: terminal alkene identity and EF-Tu domain corrections'
started_at: '2026-10-21T18:53:54Z'
finished_at: '2026-10-21T19:22:21Z'
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
summary: The native graph is internally valid but encodes the terminal C37=C38 bond
  as E, whereas inspected original structures and independent ChEBI/CCD encodings
  specify Z. A separate ChEMBL exact reference also differs at a tetrahedral centre.
  The definition incorrectly names the EF-Tu I/II interface; original mutation, binding
  and structural studies support I/III. The two qualified CARD resistance assertions
  are reproducible and have relevant primary support. One blocker and two major findings
  require source-owned correction.
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
  - path: data/antibiotics/antibacterial/kirromycin.yaml
    sha256: dccf09a75a6ad8b3c3e1d0c23840a63b3f26a05fe3908020567406167baab799
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
- target_id: antibioticmech:aro-8b2f0e38fa
  path: data/antibiotics/antibacterial/kirromycin.yaml
  label: kirromycin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
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
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Actual maintained source input for the record
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 576; one complete native record. All thirteen initial
    input hashes remain unchanged; four actual source-owner inputs were appended before
    assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-8b2f0e38fa
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/kirromycin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/kirromycin.yaml --out /private/tmp/am-review-session/576-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: failed
  required: false
  summary: The optional chemistry helper exited 1 because native average_mass 796.9
    differs from RDKit 796.955 by 0.055, exceeding its fixed 0.05 tolerance. Both
    serializations parse and reproduce the stored formula, charge, monoisotopic mass,
    key and source mint. This precision difference is not the stereochemical identity
    finding.
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 576
  exit_code: 1
  expected_exit_code: 0
- check_id: authority-comparison
  name: Independent exact chemical authority and bond diagnostic
  status: passed
  required: false
  summary: Both native serializations and PubChem agree. Changing only canonical InChI
    C9=C11 from E to Z reproduces the ChEBI InChI and CCD KIR key. ChEMBL additionally
    requires inversion at canonical C27 to reproduce that key.
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/576-compare.py
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
  - antibioticmech:aro-8b2f0e38fa
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
  - antibioticmech:aro-8b2f0e38fa
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
  - antibioticmech:aro-8b2f0e38fa
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
  - antibioticmech:aro-8b2f0e38fa
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
  - antibioticmech:aro-8b2f0e38fa
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
  - antibioticmech:aro-8b2f0e38fa
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
  - antibioticmech:aro-8b2f0e38fa
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
  - antibioticmech:aro-8b2f0e38fa
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
  - antibioticmech:aro-8b2f0e38fa
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/kirromycin.yaml
  locator: Entire native record, including all five xrefs, two resistance objects
    and three history events.
  accessed_at: '2026-10-21T19:19:07Z'
  support: supports
  summary: ARO-seeded MINTED kirromycin has the valid neutral C43H60N2O12 graph HMSYAPGFKGSXAJ-GFNGQHCCSA-N,
    eleven assigned tetrahedral centres and seven E double bonds. The definition names
    EF-Tu domains 1,2 and describes retention after GTP hydrolysis. Mocimycin is an
    exact synonym. Both resistance objects explicitly remain CARD database assertions.
    There are no native quantitative activity, clinical, producer, molecular-target,
    causal-graph, pathway or dataset objects.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv:222; data/raw/pubchem_structures.tsv:58;
    data/raw/aro_resistance_edges.tsv:3898-3899; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py
  locator: Exact inventory rows and relevant configuration/extractor/fallback, definition
    selection and CARD edge emission branches.
  accessed_at: '2026-10-21T19:19:07Z'
  support: supports
  summary: The record reproduces the ARO definition, seven source references and two
    determinant edges. PubChem CID 135452521 supplies its structure because no adopted
    ChEBI inventory row supplies this concept. The seeder selects the first ARO definition
    PMID, emits imported exact xrefs and labels CARD edges as database assertions.
    Current two-star ChEBI availability does not retroactively make the historical
    MINTED status an error. All thirteen initial hashes are preserved; the four actual
    owner inputs were appended.
  snapshot_sha256: b51cb7028dc514df022cb7ecd9eb2225ecbc1767a57d8c04359c16e48483a1e5
- evidence_id: local-search
  kind: validation
  reference: /private/tmp/am-review-session/576-local-hits.txt; /private/tmp/am-review-session/576-owner-hits.txt
  locator: Ignored-inclusive and hidden-inclusive exact label, identifier and slug
    search; native source row cross-check.
  accessed_at: '2026-10-21T19:19:07Z'
  support: context_only
  summary: Searches included ignored and hidden files. Hits included inventories,
    native and generated records, historical research ledgers and related elfamycins.
    Historical reports were leads only. No optional field absence is promoted into
    a defect; the entire native file determines its actual assertion set.
  snapshot_sha256: 569569e5ab139a160c93d69c5533ae555714b89ef645d9b5d871692c23d3c950
- evidence_id: aro
  kind: database
  reference: https://purl.obolibrary.org/obo/aro.obo
  locator: 'Official current snapshot: ARO3001234,3001310,3001219,3003359,3003368
    and0001001.'
  accessed_at: '2026-10-21T15:57:42Z'
  support: supports
  summary: All six terms were read. Current ARO repeats the I/II definition, the synonym,
    five chemical associations and both exact kirromycin resistance relations. ARO3001219
    is the elfamycin target-based antibiotic class, not a claim that every member
    has one conserved backbone. The seven adopted definition references are unchanged.
    The snapshot was fetched at 2026-10-21T15:57:42Z and extracted into 576-current-aro-terms.json.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/190786/
  locator: Complete official response and independently parsed default structure.
  accessed_at: '2026-10-21T19:11:54Z'
  support: supports
  summary: CHEBI190786 labels the compound Mocimycin and associates CAS50935-71-2
    and CCD KIR. Its valid InChI encodes terminal Z and has key HMSYAPGFKGSXAJ-PAHGNTJYSA-N.
    Its supplied aromatic SMILES independently fails parsing; that separate upstream
    serialization problem is not present in the native PubChem SMILES. The two-star
    entry is corroboration, not sole experimental proof.
  snapshot_sha256: 958b6a0d8ed1b0e293edc5d182d8908c4a0ad3ac7eec56ae1171da9d0854f04e
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/135452521
  locator: Current structure properties and CAS-based public lookup.
  accessed_at: '2026-10-21T19:11:54Z'
  support: supports
  summary: CID 135452521 reproduces both native serializations and the all-E key.
    In contrast, a public lookup of CAS50935-71-2 returns CID 135484176 with the Z-terminal
    PAHGNTJY key. CAS identity was corroborated by public associations, not inspected
    in a licensed registry.
  snapshot_sha256: dd031a98a80f15a5ed7f92e5840df4f1a0f419ca3786130297149aed4e22dd09
- evidence_id: ccd
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/chemcomp/KIR
  locator: Complete chemical component and CACTVS/OpenEye stereochemical SMILES plus
    InChI.
  accessed_at: '2026-10-21T19:12:31Z'
  support: supports
  summary: All three independently parsed CCD KIR encodings agree with C43H60N2O12
    and HMSYAPGFKGSXAJ-PAHGNTJYSA-N. The terminal diene is E,Z; all eleven tetrahedral
    centres agree with the native graph. The only native-versus-CCD stereo difference
    is the terminal double bond.
  snapshot_sha256: 497ecc7a4df5502a95a712d86981d2d592b96c2179ecbd3ae544579bc9f77a13
- evidence_id: chembl
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL4297102.json
  locator: Complete official structure fields, with SMILES, InChI and molfile independently
    parsed.
  accessed_at: '2026-10-21T19:11:54Z'
  support: supports
  summary: All three ChEMBL encodings give HMSYAPGFKGSXAJ-UIMKWNSLSA-N. They agree
    with terminal Z but invert canonical InChI C27 relative to CCD/ChEBI/native. Canonical
    C27 is the methyl-bearing linker centre adjacent to the methoxy-bearing carbon
    and the tetrahydrofuran ring. This additional discrepancy is separate from the
    native terminal alkene.
  snapshot_sha256: e44ab02c40f676a0b4ccbc6017c8ddab8c5a295a281dc606bf747ad09389dd11
- evidence_id: mapping
  kind: validation
  reference: /private/tmp/am-review-session/576-authority-chemistry.json
  locator: Reproducible independent parsing and one-bond/one-centre scratch diagnostics.
  accessed_at: '2026-10-21T19:19:07Z'
  support: supports
  summary: Only changing native canonical C9=C11 from E to Z gives the exact CCD/ChEBI
    PAHGNTJY key. The bond maps to conventional C37=C38 in the original numbered structure,
    at the methyl-terminated end of the goldinonic-acid side chain. Separately, only
    inverting canonical ChEMBL C27 gives the same PAHGNTJY key. No native file was
    changed.
  snapshot_sha256: 782709938c148364039289571c0ed5fd892e550bfb741a4094aeadd0420f450a
- evidence_id: nmr1988
  kind: primary_source
  reference: PMID:3356609; DOI:10.7164/antibiotics.41.202
  locator: Complete original five-page article read; numbered structure1 on p202 visually
    inspected, Methods and Results read.
  accessed_at: '2026-10-21T19:12:31Z'
  support: supports
  summary: The exact kirromycin/mocimycin drawing has terminal C37=C38 Z. Purified
    mocimycin was studied with deuterated E. coli EF-Tu by proton NMR. Titration supports
    a 1:1 complex and a protein conformation resembling, but not identical to, the
    GTP form. The NMR study is not an atomic domain-binding map. Its named material
    does not validate the native E-terminal isomer.
  snapshot_sha256: 2099765635edbfa4f5a0e0d533f9ec210174f4c76460420d1a37be8bf0edf8d7
- evidence_id: activity1989
  kind: primary_source
  reference: PMID:2499247; DOI:10.1128/AAC.33.3.322
  locator: All four original scanned pages read, including Figure1 and both tables.
  accessed_at: '2026-10-21T19:13:30Z'
  support: supports
  summary: Figure 1 independently depicts terminal Z. Kirromycin supplied by Jill
    Barber gave E. coli cell-free EC50 values of 0.23 µM for poly(Phe) synthesis and
    EF-Tu-dependent GTPase in Table 1. These are biochemical endpoints, not MICs or
    binding constants. Table 2 does not give a kirromycin row; the hybrid ribosome/factor
    and preincubation experiments concern aurodox, so those exact results are not
    transferred to kirromycin.
  snapshot_sha256: 749a788d09cdcead1812d35434dd78923f657e4a22db8aa62aa4a11ea3760c9e
- evidence_id: biosynthesis2018
  kind: primary_source
  reference: PMID:29459765; DOI:10.1038/s41598-018-21507-6
  locator: Introduction, Methods, selected Results/Discussion and original Figure1A
    inspected; full XML downloaded.
  accessed_at: '2026-10-21T19:17:04Z'
  support: supports
  summary: Figure 1A again depicts the methyl-terminal alkene as Z. Experiments use
    wild-type Streptomyces collinus Tü365 and biosynthetic gene mutants, with HPLC-HRMS
    and NMR analysis of derivatives. This is direct producer/biosynthetic context,
    not a bacterial target assay. The native record has no producer object requiring
    correction. Unrelated derivative and biosynthetic-enzyme results are not promoted
    into kirromycin antibacterial targets.
  snapshot_sha256: 093c8829091aad4aefb745001bd6c3bf5e90a88c882ed7a6341e7f8a6a153b10
- evidence_id: mechanism1974
  kind: primary_source
  reference: PMID:4373734; DOI:10.1073/pnas.71.12.4910
  locator: All five original scanned pages read, including Tables1-3 and Discussion.
  accessed_at: '2026-10-21T19:13:29Z'
  support: supports
  summary: The cited primary paper supports EF-Tu-dependent inhibition, retention
    of EF-Tu after GTP hydrolysis and effects on EF-Tu nucleotide/tRNA interactions.
    It explicitly distinguishes inhibition of EF-Tu-dependent peptide formation from
    direct peptidyltransferase or EF-G-driven translocation inhibition; those separate
    activities were unaffected under the reported tests. The paper does not assign
    the I/II binding interface. The historical stated molecular weight794 is not used
    as modern identity evidence.
  snapshot_sha256: a6d81b8595549b1899408213499a8c22aa1d3af56357e2a31733990d43ee19a6
- evidence_id: resistance1977
  kind: primary_source
  reference: PMID:337296; DOI:10.1073/pnas.74.10.4341
  locator: All five original scanned pages read, Methods, Figures1-5 and Discussion.
  accessed_at: '2026-10-21T19:13:29Z'
  support: supports
  summary: E. coli D22-derived D2216 carries resistant tufB-associated EF-Tu with
    an inactive or deficient second tuf contribution; complementation and cell-free
    mixing show dominance of sensitivity. Temperature-dependent 80-700-fold differences
    are cell-free response shifts, not clinical MIC fold changes. The study supports
    exact kirromycin target-alteration resistance while distinguishing uptake effects
    and genetic background.
  snapshot_sha256: b89c8bd7939ed6d3c28528861b42112b1423bec23d8f3eee7e8d1b25aebe218f
- evidence_id: binding1994
  kind: primary_source
  reference: PMID:7525272; DOI:10.1002/j.1460-2075.1994.tb06815.x
  locator: Complete abstract and original pp4877,4881-4884 visually read; Figures7-11
    and Methods on p4884 inspected.
  accessed_at: '2026-10-21T19:16:45Z'
  support: supports
  summary: E. coli EF-Tu G316D, A375T, A375V and Q124K show altered kirromycin binding
    and biochemical sensitivity. The mutations map to the I/III interface in the GTP
    state, and the authors propose binding near or in that interface. Binding and
    release effects are distinguished. The crystallographic mapping used existing
    factor structures; this paper is not itself a direct kirromycin co-crystal.
  snapshot_sha256: 06d54ffa1c33aab181ecc283889b11f060f2ea8e5a2cb5e4250a847a71198a55
- evidence_id: mutation1994
  kind: primary_source
  reference: PMID:7925958; DOI:10.1016/0014-5793(94)00937-6
  locator: Complete indexed original abstract; official free PDF route returned403.
  accessed_at: '2026-10-21T19:11:54Z'
  support: supports
  summary: Thirteen resistance substitutions at seven sites cluster at domains I and
    III in EF-Tu-GTP, supporting the proposed interface. The full title and abstract
    say I/III. The later 2002 article bibliography incorrectly renders this title
    as I/II; that bibliographic typo must not override the inspected original abstract.
    No specific numerical binding constant is extracted.
  snapshot_sha256: dd6417f0218f8a8001a0bc9dfc0179c99c7e8af1dd9886fb55d6e1a796b91e78
- evidence_id: resistance1997
  kind: primary_source
  reference: PMID:9043138; DOI:10.1099/00221287-143-2-617
  locator: Complete original indexed abstract; publisher full-text route returned403.
  accessed_at: '2026-10-21T19:11:54Z'
  support: supports
  summary: The kirrothricin producer S. cinnamoneus supplies an EF-Tu resistant to
    kirromycin in a poly(U)-directed cell-free assay. A Thr378-to-Ala substitution
    increases kirromycin sensitivity; GE2270 sensitivity is separately described.
    This supports the named determinant context but does not make S. cinnamoneus a
    demonstrated kirromycin producer or establish a clinical MIC.
  snapshot_sha256: dd6417f0218f8a8001a0bc9dfc0179c99c7e8af1dd9886fb55d6e1a796b91e78
- evidence_id: cryoem2002
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC126079/
  locator: Introduction, Results on domain fitting, TableI, relevant Discussion and
    complete Methods inspected.
  accessed_at: '2026-10-21T19:16:20Z'
  support: supports
  summary: Kirromycin-stalled E. coli ribosome/EF-Tu/GDP/aa-tRNA reconstructions support
    a GTP-like intermediate and failure of normal accommodation/release. Domain I/III
    is the binding-site context; domain II contacts 16S rRNA and must not be confused
    with the drug interface. The map is an ensemble with partial occupancy and fitted
    coordinates, not proof that the factor is exactly identical to the free GTP state.
  snapshot_sha256: 3895c49db512a956e6a745ea6d38f1d52f973fc3e548a29c646e4ff73450d6ee
- evidence_id: cryoem2009
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2666022/
  locator: Selected Results paragraphs on molecular-model construction and EF-Tu conformation.
  accessed_at: '2026-10-21T19:16:20Z'
  support: context_only
  summary: This kirromycin-stalled ribosomal study explicitly distinguishes its cryo-EM
    complex, the aurodox/methylkirromycin crystal model used in docking, and exact
    kirromycin entry1OB2. The models support I/III and a particular intermediate geometry;
    aurodox atomic contacts are not automatically exact kirromycin observations.
  snapshot_sha256: b0b4910bc613c497d687a8b4a0e252de6bfd87b88c14089717a85c96ee453e45
- evidence_id: pdb
  kind: database
  reference: https://www.rcsb.org/structure/1OB2
  locator: Official structure-entry metadata and CCD KIR checked.
  accessed_at: '2026-10-21T19:13:29Z'
  support: context_only
  summary: 1OB2 is an exact kirromycin-containing EF-Tu/guanine-nucleotide-analogue/tRNA
    structural dataset at 3.35 Å. Its primary citation is marked To be published;
    it is not represented here as a published primary article or as GDP-state evidence.
  snapshot_sha256: 244c08b856cc988d8ffc11782406e572a494eaad573a5798731155c7037f15bf
- evidence_id: review-leads
  kind: database
  reference: PMID:3904612; DOI:10.1146/annurev.mi.39.100185.003013; PMID:12370016;
    DOI:10.2174/1389203023380855
  locator: Adopted1985 review metadata and later CARD-linked2002 review complete abstract.
  accessed_at: '2026-10-21T19:12:31Z'
  support: context_only
  summary: The 1985 adopted review has no indexed abstract and its full text was not
    obtained. The 2002 review discusses EF-Tu antibiotics but is secondary context.
    Neither is typed as direct experimental evidence.
  snapshot_sha256: 92d7efc1ca000a4f7d3b1001eb3ac286d40ee974526b0cdb09ceb97a5a68337d
- evidence_id: card-citation-limit
  kind: database
  reference: ARO:3003368; PMID:1552908; DOI:10.1007/BF00299141
  locator: Current CARD reference list and indexed original title/abstract, truncated
    at250 words.
  accessed_at: '2026-10-21T19:12:31Z'
  support: context_only
  summary: One CARD-linked reference concerns rpsL alleles and streptomycin resistance
    rather than a demonstrated kirromycin/EF-Tu experiment. This upstream citation
    association should be checked before any primary-evidence upgrade. It does not
    refute the independently supported, explicitly database-qualified native resistance
    assertion.
  snapshot_sha256: 92d7efc1ca000a4f7d3b1001eb3ac286d40ee974526b0cdb09ceb97a5a68337d
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/precise1k genes b3339 and b3980
  locator: Actual catalog and tufA/tufB structured searches before web research; execution
    manifest576-adapter.json.
  accessed_at: '2026-10-21T19:19:07Z'
  support: context_only
  summary: The 28-dataset catalog lacks S. cinnamoneus. Exact E. coli searches resolve
    tufA to b3339 and tufB to b3980, with no matching modules. These annotations corroborate
    gene naming only; no binding, resistance, expression module or phenotype is inferred
    from them.
  snapshot_sha256: f20ff02d4cf2681e8e90ebb9bec1a5d22f036f6cea779a8b4da46a32e30b8c06
assessments:
- assessment_id: identity
  area: identity
  topic: Constitution, stereo and chemical properties
  outcome: concern
  summary: 'The chemical strings are mutually valid and the stored properties are
    consistent within source precision. The natural-product identity nevertheless
    fails at one positively mapped terminal alkene: native E versus primary Z.'
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  evidence_ids:
  - native
  - mapping
  - nmr1988
  - activity1989
  - biosynthesis2018
  - ccd
- assessment_id: xref
  area: grounding
  topic: Five exact references and class terms
  outcome: concern
  summary: ARO and current PubChem reproduce the record. ChEBI and public CAS-associated
    material instead have terminal Z, and ChEMBL adds an independent tetrahedral conflict.
    The elfamycin parent/class is appropriate at its declared source scope; it is
    not proof of the native exact stereoisomer.
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  evidence_ids:
  - aro
  - pubchem
  - chebi
  - ccd
  - chembl
  - mapping
- assessment_id: definition
  area: evidence
  topic: EF-Tu interface and inhibited step
  outcome: concern
  summary: The core EF-Tu trapping mechanism is supported for natural kirromycin,
    but I/II is positively contradicted by I/III mapping and later structural context.
    GTP-like is more accurate than an identical GTP conformation. Translocation should
    be stated as a downstream consequence of the earlier stall, not a direct EF-G
    inhibition.
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  evidence_ids:
  - mechanism1974
  - nmr1988
  - binding1994
  - mutation1994
  - cryoem2002
  - cryoem2009
- assessment_id: resistance
  area: evidence
  topic: Both qualified CARD determinant assertions
  outcome: supported
  summary: Both exact CARD edges reproduce the maintained source and have relevant
    original experimental support. The native database-only evidence status is honest;
    no clinical breakpoint, strain MIC or direct-binding primary claim is added. All
    activity and mechanism material must be reconciled with the native terminal-E
    identity before scientific sign-off.
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  evidence_ids:
  - aro
  - resistance1977
  - binding1994
  - resistance1997
  - card-citation-limit
- assessment_id: activity
  area: evidence
  topic: Antibacterial filing and biological material
  outcome: supported
  summary: The primary studies establish bacterial translation inhibition and whole-cell
    resistance selection for named natural kirromycin. The ANTIBACTERIAL filing is
    appropriate for that named compound, but it cannot validate the separately encoded
    E-terminal isomer without identity reconciliation. Aurodox and other elfamycins
    are not quantitative substitutes.
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  evidence_ids:
  - mechanism1974
  - resistance1977
  - activity1989
  - nmr1988
- assessment_id: provenance
  area: provenance
  topic: Source ownership, history and evidence placement
  outcome: supported
  summary: All native values and history are accounted for by the maintained ARO/PubChem
    sources. The first-PMID definition citation is an importer choice and does not
    make every inherited mechanistic clause a finding of that paper. Source status
    and timestamp facts remain intact.
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  evidence_ids:
  - owners
  - native
  - aro
- assessment_id: coverage
  area: completeness
  topic: All native assertions and all seven adopted leads
  outcome: supported
  summary: The entire native record and actual source rows were inspected. Four adopted
    original articles were read fully, two at complete-abstract depth, and the secondary
    1985 review at metadata depth. Additional binding and cryo-EM sources were read
    at the stated selected scope. Missing optional target, MIC, producer and graph
    objects are not defects.
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  evidence_ids:
  - owners
  - local-search
  - mechanism1974
  - resistance1977
  - activity1989
  - nmr1988
  - mutation1994
  - resistance1997
  - review-leads
findings:
- finding_id: F1
  issue_key: kirromycin-terminal-c37-c38-geometry
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Correct the terminal alkene identity through the maintained source
  description: The native SMILES and InChI encode conventional C37=C38 as E. Original
    numbered structures from 1988 and 1989 and the 2018 primary figure depict Z; independently
    parsed CCD KIR and ChEBI InChI agree. A scratch change of only canonical InChI
    C9=C11 from E to Z reproduces their full key while preserving all other stereo
    assignments. The record therefore denotes a different stereoisomer from the named
    experimental natural product. Correct the source association and regenerate after
    independent atom/bond review; this finding does not establish that the E isomer
    is inactive.
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  field_paths:
  - chemical_structure
  - xrefs[4]
  evidence_ids:
  - mapping
  - nmr1988
  - activity1989
  - biosynthesis2018
  - ccd
  - chebi
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact structure fallback
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure source selection and normalization
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Upstream compound-to-PubChem association
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible identity and structure emission
  rule_id: 'Native record checklist: exact identity, equivalent xrefs and claim-specific
    primary support'
  native_severity: blocker
  normalization_reason: A positively identified wrong stereoisomer is a wrong-identity
    blocker even though both serializations are chemically valid.
- finding_id: F2
  issue_key: kirromycin-chembl-exact-stereocentre-conflict
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Resolve the additional ChEMBL exact-reference conflict
  description: CHEMBL4297102 agrees with terminal Z but assigns the opposite canonical
    InChI C27 tetrahedral configuration from native, CCD and ChEBI. Its SMILES, InChI
    and molfile agree with each other. Inverting that centre alone reproduces the
    CCD key. Preserve any useful related-isomer association with explicit semantics
    or suppress the unsupported exact equivalence; do not copy the entire ChEMBL graph
    to repair the terminal bond.
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  field_paths:
  - xrefs[3]
  evidence_ids:
  - chembl
  - mapping
  - ccd
  - chebi
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported exact chemical cross-references
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Exact-reference import
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact-reference emission
  rule_id: 'Native record checklist: exact identity, equivalent xrefs and claim-specific
    primary support'
  native_severity: major
  normalization_reason: This is a positive exact-reference stereo conflict independent
    of the native terminal-alkene blocker.
- finding_id: F3
  issue_key: kirromycin-eftu-domain-interface
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Correct the EF-Tu binding interface and clarify the stalled step
  description: The inherited definition names domains 1,2, whereas the original mutation/binding
    studies locate the relevant interface at I/III and subsequent kirromycin-stalled
    structural studies support that assignment. Preserve the supported EF-Tu trapping
    mechanism, describe the post-hydrolysis state as GTP-like, and distinguish failed
    EF-Tu release/aa-tRNA accommodation from downstream cessation of elongation. The
    cited 1974 paper explicitly found no direct inhibition in its separate EF-G translocation
    assay.
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - mechanism1974
  - nmr1988
  - binding1994
  - mutation1994
  - cryoem2002
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported compound definition and source references
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Definition extraction or maintained adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Definition and claim citation emission
  rule_id: 'Native record checklist: exact identity, equivalent xrefs and claim-specific
    primary support'
  native_severity: major
  normalization_reason: The binding-site statement is positively wrong, not merely
    missing primary support. The downstream translocation wording needs qualification
    rather than a claim that translation proceeds normally.
actions:
- action_id: A1
  description: Repair the source-owned exact structure and cross-reference mapping.
  finding_ids:
  - F1
  - F2
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact structure fallback
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure source selection and normalization
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Upstream compound-to-PubChem association
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible identity and structure emission
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported exact chemical cross-references
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Exact-reference import
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact-reference emission
  acceptance_checks:
  - Map conventional C37=C38 to canonical C9=C11 and independently confirm Z from
    original drawings; retain all other validated centres and bonds unless separate
    evidence supports a change.
  - Resolve the ChEMBL C27 conflict separately. Check every retained exact xref against
    the selected complete structure; association fields must state their broader relation.
  - Regenerate through maintained sources, preserve provenance and reassess all inherited
    biological material against the corrected exact entity. Run schema, strict, structure
    and source-reproduction gates.
- action_id: A2
  description: Correct the inherited mechanism wording and attach each claim to the
    appropriate experiment.
  finding_ids:
  - F3
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported compound definition and source references
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Definition extraction or maintained adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Definition and claim citation emission
  acceptance_checks:
  - Use I/III rather than I/II and cite the actual mutation/binding and structural
    sources at their measured scope.
  - Keep EF-Tu release/accommodation, peptide formation and EF-G translocation distinct.
    Use GTP-like intermediate wording and avoid claiming exact identity with the isolated
    GTP state.
  - Do not attribute all detailed structural claims to PMID4373734 merely because
    it is the first imported definition reference.
- action_id: A3
  description: Preserve the supported resistance assertions and qualify any future
    enrichment.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-8b2f0e38fa
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/kirromycin.yaml
    role: Curator-owned primary evidence, activity and mechanism additions through
      the validated writer
  acceptance_checks:
  - Retain database qualification unless original primary observations are separately
    curated with organism, mutant, assay and material context. Check CARD PMID1552908
    before using it as kirromycin support.
  - Do not transfer aurodox hybrid/preincubation results, Table2 values lacking a
    kirromycin row, or cell-free EC50 values as MICs.
  - S. cinnamoneus is a kirrothricin producer in PMID9043138; the separate S. collinus
    biosynthesis study supports kirromycin production. Biosynthetic enzymes are not
    antibacterial targets.
limitations:
- The optional chemistry helper really exited 1 on average-mass precision; all structural
  parsing and mint comparisons succeeded. Required focused schema and strict checks
  exited 0. Initial copied helper runs accidentally targeted jadomycin B; their outputs
  are retained under 576-initial-wrong-target-* and excluded from the kirromycin check
  results. The corrected commands were rerun against kirromycin.
- The four adopted 1974,1977,1988 and 1989 original articles were read fully. The
  1997 and 1994 FEBS originals were available as complete abstracts; official publisher
  routes returned 403. The1985 secondary review had metadata only.
- The additional 1994 EMBO original was inspected at pp 4877 and 4881-4884, including
  relevant figures and Methods, rather than claimed fully read. The 2002 and 2009
  cryo-EM articles were used only at the selected sections stated in their evidence
  entries.
- The 2018 primary source was inspected for structure and producer/biosynthetic context
  at the stated sections; its original Figure 1A was viewed. The Springer image route
  returned HTML despite 200, so only the successfully fetched PMC image is used. Raw
  NMR spectra were not reprocessed.
- ChEBI supplies an invalid aromatic SMILES alongside a valid Z-terminal InChI; the
  native PubChem SMILES is valid. The review does not silently substitute one full
  external graph or equate parsing failure with the separate native stereochemical
  conflict.
- CAS corroboration used public associations rather than licensed registry access.
  The bounded literature search captured the first 100 of 119 hits; selected relevant
  studies were followed, not an exhaustive literature census. Missing optional observations
  are not proof that no other biological evidence exists.
- The exact natural-material mechanism and resistance evidence cannot automatically
  be attached to the native E-terminal stereoisomer. No activity or inactivity claim
  about that isolated isomer is established by this review.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Original capture hashes are preserved. Public retrieval manifests retain actual
  URLs, UTC timestamps, response status and hashes. The current ARO snapshot is shared
  with its original retrieval timestamp; all exact terms were independently inspected
  for this record.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
