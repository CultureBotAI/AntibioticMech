# Klebsidin: defined lasso peptide with stereochemical and spectrum corrections

- Review: 20261021T192413Z-klebsidin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:53:56Z
- Finished UTC: 2026-10-21T19:24:13Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native constitution matches the nineteen-residue Gly1–Glu8 macrolactam, but all seventeen stereocentres are unspecified despite the original polypeptide(L) structural deposition. Its cited paper assigns the broad Enterobacteriaceae/Escherichia/Salmonella sentence to microcin J25, while actual klebsidin experiments depend on strain, transport and intracellular versus extracellular exposure. Two source-owned corrections are warranted. RNA-polymerase inhibition and the lasso class remain supported within explicit experimental limits.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position579; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-1d2367825f | data/antibiotics/antibacterial/klebsidin.yaml | generated | klebsidin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-1d2367825f | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-1d2367825f | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-1d2367825f | Actual focused execution exited 0. |
| Structured annotation adapter before open mechanism research | passed | False | antibioticmech:aro-1d2367825f | Actual exit0; annotation context does not establish drug action or susceptibility. |
| Structured annotation adapter before open mechanism research | passed | False | antibioticmech:aro-1d2367825f | Actual exit0; annotation context does not establish drug action or susceptibility. |
| Structured annotation adapter before open mechanism research | passed | False | antibioticmech:aro-1d2367825f | Actual exit0; annotation context does not establish drug action or susceptibility. |
| Independent authority and sequence/closure diagnostic | passed | False | antibioticmech:aro-1d2367825f | Native SMILES/InChI, current PubChem and current ChEBI InChI agree. The independently constructed L-peptide macrolactam has the same connectivity with seventeen configured sites. Current ChEBI standalone SMILES is invalid but is not native. |
| Authoritative full QC | failed | True | antibioticmech:aro-1d2367825f | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-1d2367825f | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-1d2367825f | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-1d2367825f | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-1d2367825f | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-1d2367825f | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-1d2367825f | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-1d2367825f | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-1d2367825f | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Nineteen-residue macrolactam and stereochemical scope

identity: unknown. Targets: antibioticmech:aro-1d2367825f.

Constitution, formula, charge and source properties agree. Seventeen defined residue configurations are absent from the principal graph; no racemate or opposite stereoisomer is established.

### Mint, three xrefs and broader lasso class

grounding: supported. Targets: antibioticmech:aro-1d2367825f.

ARO and the two chemistry authorities match the named source and unspecified native graph. The historical fallback/mint and broader class fit. Future stereo correction must also resolve exact-xref scope instead of calling the specified and unspecified graphs exact equivalents.

### Producer, spectrum and exposure route

evidence: concern. Targets: antibioticmech:aro-1d2367825f.

K.pneumoniae origin and RNAP-linked action are supported. The adopted source attributes the broad Enterobacteriaceae/Salmonella sentence to another lasso peptide. Actual klebsidin activity must retain named strains, transport and exposure conditions; E.coli activity is not entirely denied.

### RNA-polymerase action and resistance experiment

evidence: supported. Targets: antibioticmech:aro-1d2367825f.

Original primary abstract and2022 engineered-RpoC data support RNAP-linked activity. Annotation adapters are context; lasso NMR is not an RNAP complex. No quantitative affinity, clinical use or universal permeability claim is made.

### Maintained source ownership and capture integrity

provenance: supported. Targets: antibioticmech:aro-1d2367825f.

Native fields faithfully inherit ARO/PubChem. Original thirteen hashes and the three actual-owner additions are preserved. The generated source owners, rather than direct YAML edits, control the proposed corrections.

### All native fields, adopted source and bounded primary leads

completeness: supported. Targets: antibioticmech:aro-1d2367825f.

Whole-record review covers identity, broad class, definition, all xrefs, structure and provenance. The sole adopted main and SI were inspected. Optional targets, MICs and graphs were not required merely because absent; the two findings concern populated identity and spectrum.

## Findings

### F1: Preserve the defined peptide stereochemistry

major / open / confirmed; issue key: klebsidin-missing-known-peptide-stereochemistry.

All seventeen tetrahedral sites are unspecified in the native principal graph, although the original-linked structural deposition explicitly defines the nineteen-residue L peptide and standard residues. Independent L-sequence/macrolactam reconstruction agrees with native constitution and formula. Resolve exact stereochemical scope and maintained groundings before regenerating an assigned graph; no opposite enantiomer or physical mixture is established.

### F2: Correct the spectrum attribution and exposure context

major / open / confirmed; issue key: klebsidin-spectrum-from-microcin-j25.

The native broad Enterobacteriaceae/Escherichia/Salmonella wording reproduces a sentence the cited paper applies to microcinJ25. The klebsidin study instead reports strain- and delivery-dependent results, including intracellular expression and high-concentration external spot assays. Replace the transferred Salmonella/family-wide implication with exact klebsidin evidence, retaining demonstrated E.coli/K.pneumoniae results and their limits. Do not claim that Salmonella can never be affected.

## Recommended Actions And Acceptance Checks

### A1

Resolve and regenerate the exact L-peptide identity with scoped authority links.

- Independently confirm GSDGPIIEFFNPNGVMHYG, Gly1–Glu8 side-chain macrolactam, fifteen L alpha centres and two L-isoleucine beta centres from original-linked data.
- Primary-sequence diagnostic candidate is XNBIEFNBLNDRGW-ILRSLDFVSA-N; verify it independently before adoption and handle the current unspecified ChEBI/PubChem references explicitly.
- Preserve lasso topology descriptively/with primary evidence; ordinary SMILES alone does not encode threading. Run schema, strict, chemistry, grounding and source reproduction checks.

### A2

Replace the transferred spectrum sentence with bounded klebsidin evidence.

- The regenerated definition cites the actual klebsidin experiments; no Salmonella or broad family claim is retained solely from the MccJ25 introduction.
- Keep extracellular strain-specific spot concentrations separate from broth MIC and from intracellular kleABC induction. Preserve K.pneumoniae KP23/E.coli BW25113 positives and DH10B negative conditions.
- Keep wild-type klebsidin separate from P12V/F9Y variants and the2024 multi-peptide chitosan composite.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/klebsidin.yaml; Entire native record, all fields and three provenance-history events. | supports | SEEDED/MINTED ARO-derived individual; neutral C93H129N23O27S, XNBIEFNBLNDRGW-UHFFFAOYSA-N, valid PubChem-derived principal graph. All seventeen possible tetrahedral sites lack configuration. ARO:3009658 is a broader lasso-peptide class, not an exact compound. No molecular_target/resistance/MIC/citation-snippet/causal_graph object is populated. The free-prose definition asserts producer, spectrum and RNA-polymerase inhibition. |
| owners | data/raw/aro_antibiotics.tsv:388; data/raw/pubchem_structures.tsv:133; scripts/enrich_pubchem_structures.py; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Complete exact raw rows and relevant source extraction, PubChem fallback, stable mint, definition-source and class emission. | supports | ARO owns definition, cited PMID35315272, parent/class and xrefs; PubChem inventory supplies all stored chemistry and retrieval date. The native retains the source wording and unspecified structure faithfully. Original thirteen captured inputs were preserved, then actual ARO/PubChem/enricher owners appended before scientific judgment, giving sixteen inputs. Hidden/ignored-inclusive source/overlay searches were included. No native or source mutation occurred. |
| aro | https://purl.obolibrary.org/obo/aro.obo; ARO:3007093; ARO:3009658; Exact current ontology terms from the public snapshot426-current-aro.obo, retrieved2026-10-21; derived exact-term extract579-current-aro-terms.txt. | supports | Current ARO repeats the native spectrum/accumulation wording and sole cited PMID35315272, with ChEBI219023 and PubChem146684527. The broader class describes the threaded lariat topology of ribosomal peptides. It does not independently verify the spectrum sentence or the seventeen unspecified centres. A direct alternate CARD hostname failed TLS validation; no content from it was treated as verified. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/146684527/property/MolecularFormula,MolecularWeight,IsomericSMILES,InChI,InChIKey,MonoisotopicMass,Charge/JSON; Complete official current property response; SMILES/InChI independently parsed. | supports | Current PubChem preserves the native valid graph and all seventeen unspecified centres. Formula, neutral charge, monoisotopic mass2031.9148971 and rounded average mass2033.2 agree with native and independent calculations. This proves faithful source adoption, not a defined stereochemical identity or a racemic experimental material. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/219023/; Complete current two-star submitted entry, including default representations, source origin and ontology. | supports | ChEBI219023 has no definition; its submitted InChI/key agrees with the native unspecified structure and names Klebsiella pneumoniae4541-2 as an origin, citing PMID28106375. Its separate displayed imidazole SMILES lacks the required [nH] and fails parsing, but native PubChem SMILES and ChEBI InChI are valid. That upstream string is not an invalid-native-structure finding or evidence that the entire cross-reference denotes a different graph. |
| original2017 | PMID:28106375; DOI:10.1021/acschembio.6b01154; Complete original abstract; official18-page supporting information text, particularly klebsidin TablesS4/S6/S7 and FiguresS2/S8/S9/S11; FigureS11 actual page viewed. Main article retrieval returned403. | supports | The original study identifies klebsidin and acinetodin from human bacterial isolates and reports bacterial RNA-polymerase inhibition. Klebsidin supplementary NMR assignments enumerate GSDGPIIEFFNPNGVMHYG, nineteen residues. TableS4/MALDI fragmentation and NMR calculations support the sequence and lasso assignment. FigureS9 tests intracellular kleABC expression; FigureS11 applies5µL of1mM klebsidin to E.coli BW25113 lawns: the empty-vector host is not inhibited whereas K.pneumoniae4541-2 fhuA expression permits inhibition. The assay uses M9 agar, 0.6% overlay, ampicillin/arabinose,30°C24h, three experiments. These zone results are not broth MICs. The paper abstract supports RNAP action but inaccessible main assay details/quantitative affinities are not invented. MicrocinJ25 and acinetodin results are kept separate. |
| pdb | PDB:5UI7; https://files.rcsb.org/download/5UI7.cif; Original2017-linked solution-NMR deposition; entity_poly, full entity sequence, residue identities and standard-component chiral annotations. | supports | 5UI7 is a klebsidin solution-NMR ensemble, not a klebsidin–RNAP complex. Entity1 is explicitly polypeptide(L), nstd_monomer=no, with nineteen residues GSDGPIIEFFNPNGVMHYG. Standard L residues give fifteen chiral alpha carbons plus the two isoleucine beta centres. The exact Gly1-to-Glu8 macrolactam is independently supplied by the primary topology/2022 description. The depositor lists252 distance restraints and a ten-model ensemble. This structural model is evidence for defined peptide stereochemical scope; no new absolute-configuration experiment or RNAP contact map is claimed. |
| chemical-diagnostic | 058-root-chem.py; 058-root-chemistry.json; Independent L-sequence construction and explicit Gly1 nitrogen–Glu8 side-chain carbonyl closure; dehydration and full constitution comparison. | supports | The primary-sequence/L-residue diagnostic reconstructs neutral C93H129N23O27S with seventeen assigned centres and full keyXNBIEFNBLNDRGW-ILRSLDFVSA-N. Removing only stereochemistry reproduces the full native key. Thus the stored constitution contains the correct sequence/macrolactam but loses its known stereochemical specification. Ordinary SMILES/InChI do not encode physical lasso threading; this diagnostic does not claim to establish topology from a two-dimensional graph. |
| adopted2022 | PMID:35315272; DOI:10.1021/acschembio.2c00148; PMC9976627; Entire scientific main text: Introduction, Results, Discussion and Methods; actual Figures1/4/5 viewed; official SI text with actual S8/S11 pages viewed. | supports | The sole adopted source explicitly assigns the Enterobacteriaceae including Escherichia/Salmonella statement to microcinJ25. It then distinguishes klebsidin, describing K.pneumoniae targeting, fhuA-dependent E.coli access and intracellular expression without export. Its main selection expresses kleABC in E.coli DH10B with70µM IPTG and measures growth enrichment for320/361 single variants. This integrates biosynthesis, stability and RNAP inhibition while bypassing extracellular uptake; it is not a minimum inhibitory concentration panel. The producer pathway and Gly1/Glu8 ring are supported. No Salmonella wild-type-klebsidin experiment is present in the inspected main/SI; this is a document-bounded statement, not a claim that no such experiment exists anywhere. |
| external2022 | PMID:35315272 Figure4; supplementary FiguresS7/S8/S11; Complete external zone-assay Methods, exact wild-type panels and captions; actual plate images viewed. | supports | Purified wild-type klebsidin inhibits K.pneumoniae KP23 at the250µM spotting dilution in Figure4E and E.coli BW25113 at500µM in S8. P12V separately reaches125µM against KP23; that variant endpoint is not parent klebsidin. Assays spot5µL from1mM twofold dilutions on Mueller-Hinton agar with5mL top agar containing10^7CFU, incubated16h37°C. These are spotting-solution concentrations, not broth MICs or clinical susceptibility classifications. No external inhibition of E.coli DH10B or its RpoCT931I derivative was observed with1mM wild type/F9Y in S11. Different strains and media account for essential experimental scope; earlier2017 BW25113 results are not flattened into a universal claim. |
| rnapp2022 | PMID:35315272 Figure5 and Methods; Relevant engineered-strain Results and Methods; actual Figure5 viewed. | supports | A CRISPR-installed E.coli DH10B RpoCT931I variant resists intracellular wild-type klebsidin. F9Y klebsidin partially restores intracellular growth inhibition in that background, yet the purified F9Y variant lacks external KP23/BW25113 inhibition at1mM. These results support RNAP-linked cellular action and variant specificity. They do not demonstrate exact atomic contacts or direct binding constants; the paper discusses a contact hypothesis. No standalone native target object needs correction merely for being absent. |
| later2024 | PMID:39475538; Complete accessible abstract from exact-name search; main article not inspected. | context_only | The2024 study concerns a nanocomposite containing acinetodin, capistruin and klebsidin with chitosan. Its composite antibacterial endpoints are not evidence for single-parent klebsidin spectrum, potency or Salmonella susceptibility. This lead is explicitly excluded from individual-parent efficacy inference. |
| adapters | 579-adapter-results.json;579-adapter-results.txt;579-adapter-scope.json; Actual structured catalog plus E.coli rpoB and rpoC queries, run before open target research. | context_only | All three commands exit0 and provide annotation context for E.coli b3987/rpoB and b3988/rpoC, with no iModulon hit. This is not a klebsidin exposure experiment or target-binding proof. The initial batch template N/A scope was corrected after reading this native definition and before any open mechanism research. |
| search | 579-local-hits.txt;579-owner-hits.txt;579-discovery.json;058-root-fetch1.json through058-root-fetch9.json; Ignored/hidden-inclusive exact record/source search, exact-name public primary search and cited original-paper follow-up. | context_only | All populated fields and the sole adopted citation were assessed. The exact-name result contained the2017 original,2022 mutational study and2024 composite paper; each received the explicit disposition above. Full primary access limits and failed XML/publisher routes are recorded, with2022 main recovered through the author PMC page and official supplements from ACS figshare. No complete-literature absence claim or paid research is made. |

## Limits And Additional Notes

- The2017 original abstract and official supplementary text were inspected; its main article retrieval returned403, so exact transcription-inhibition protocol or affinity is not claimed read. Actual SI FigureS11 was viewed; spectra and coordinate ensembles were not reprocessed.
- The2022 scientific main, Methods and official SI text were read, with actual Figures1/4/5 and S8/S11 viewed. Oligonucleotide listings were inspected as context, not independently validated by experimental reconstruction.
- The PDB NMR entry is an isolated L peptide, not an RNAP complex. Sequence-based chemical reconstruction supports constitution/stereo completeness and does not prove threading or new absolute stereochemistry experimentally.
- Current ChEBI standalone SMILES is invalid while its InChI and native PubChem SMILES agree; the invalid upstream serialization is explicitly separated from the native findings.
- The2024 composite study was abstract-only; no parent-specific MIC or mechanistic detail was inferred. There is no global negative claim about Salmonella literature.
- Structured source adapters return gene annotation context only; no iModulon or exposure evidence was returned. The originally templated adapter-scope entry was corrected before external mechanism research.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All changes are review artifacts only. Original sixteen current captured hashes are verified; the original thirteen are preserved. Shared full-QC disposition is added before final validation.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T192413Z-klebsidin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Klebsidin: defined lasso peptide with stereochemical and spectrum corrections'
started_at: '2026-10-21T18:53:56Z'
finished_at: '2026-10-21T19:24:13Z'
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
summary: The native constitution matches the nineteen-residue Gly1–Glu8 macrolactam,
  but all seventeen stereocentres are unspecified despite the original polypeptide(L)
  structural deposition. Its cited paper assigns the broad Enterobacteriaceae/Escherichia/Salmonella
  sentence to microcin J25, while actual klebsidin experiments depend on strain, transport
  and intracellular versus extracellular exposure. Two source-owned corrections are
  warranted. RNA-polymerase inhibition and the lasso class remain supported within
  explicit experimental limits.
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
  - path: data/antibiotics/antibacterial/klebsidin.yaml
    sha256: 3e9b0013b7de94b29a46e6fdb691af32813a8fd0338033cbaf5a2e0b379fc131
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
- target_id: antibioticmech:aro-1d2367825f
  path: data/antibiotics/antibacterial/klebsidin.yaml
  label: klebsidin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Maintained ARO/PubChem identity and source owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Maintained ARO/PubChem identity and source owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained ARO/PubChem identity and source owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ARO/PubChem identity and source owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Maintained ARO/PubChem identity and source owner
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position579; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-1d2367825f
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-1d2367825f
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    579
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-1d2367825f
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/klebsidin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-1d2367825f
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/klebsidin.yaml --out /private/tmp/am-review-session/579-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-catalog
  name: Structured annotation adapter before open mechanism research
  status: passed
  required: false
  summary: Actual exit0; annotation context does not establish drug action or susceptibility.
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - antibioticmech:aro-1d2367825f
- check_id: adapter-rpoB
  name: Structured annotation adapter before open mechanism research
  status: passed
  required: false
  summary: Actual exit0; annotation context does not establish drug action or susceptibility.
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query rpoB
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - antibioticmech:aro-1d2367825f
- check_id: adapter-rpoC
  name: Structured annotation adapter before open mechanism research
  status: passed
  required: false
  summary: Actual exit0; annotation context does not establish drug action or susceptibility.
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query rpoC
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - antibioticmech:aro-1d2367825f
- check_id: structure-comparison
  name: Independent authority and sequence/closure diagnostic
  status: passed
  required: false
  summary: Native SMILES/InChI, current PubChem and current ChEBI InChI agree. The
    independently constructed L-peptide macrolactam has the same connectivity with
    seventeen configured sites. Current ChEBI standalone SMILES is invalid but is
    not native.
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/058-root-chem.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - antibioticmech:aro-1d2367825f
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-1d2367825f
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
  - antibioticmech:aro-1d2367825f
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
  - antibioticmech:aro-1d2367825f
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
  - antibioticmech:aro-1d2367825f
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
  - antibioticmech:aro-1d2367825f
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
  - antibioticmech:aro-1d2367825f
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
  - antibioticmech:aro-1d2367825f
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
  - antibioticmech:aro-1d2367825f
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
  - antibioticmech:aro-1d2367825f
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/klebsidin.yaml
  locator: Entire native record, all fields and three provenance-history events.
  accessed_at: '2026-10-21T19:09:19Z'
  support: supports
  summary: SEEDED/MINTED ARO-derived individual; neutral C93H129N23O27S, XNBIEFNBLNDRGW-UHFFFAOYSA-N,
    valid PubChem-derived principal graph. All seventeen possible tetrahedral sites
    lack configuration. ARO:3009658 is a broader lasso-peptide class, not an exact
    compound. No molecular_target/resistance/MIC/citation-snippet/causal_graph object
    is populated. The free-prose definition asserts producer, spectrum and RNA-polymerase
    inhibition.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv:388; data/raw/pubchem_structures.tsv:133;
    scripts/enrich_pubchem_structures.py; scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  locator: Complete exact raw rows and relevant source extraction, PubChem fallback,
    stable mint, definition-source and class emission.
  accessed_at: '2026-10-21T19:09:19Z'
  support: supports
  summary: ARO owns definition, cited PMID35315272, parent/class and xrefs; PubChem
    inventory supplies all stored chemistry and retrieval date. The native retains
    the source wording and unspecified structure faithfully. Original thirteen captured
    inputs were preserved, then actual ARO/PubChem/enricher owners appended before
    scientific judgment, giving sixteen inputs. Hidden/ignored-inclusive source/overlay
    searches were included. No native or source mutation occurred.
  snapshot_sha256: 6ab7f9456e20d17ed63a181aeced3460257a1ca2264610b0de5e6ac1265cccef
- evidence_id: aro
  kind: authority
  reference: https://purl.obolibrary.org/obo/aro.obo; ARO:3007093; ARO:3009658
  locator: Exact current ontology terms from the public snapshot426-current-aro.obo,
    retrieved2026-10-21; derived exact-term extract579-current-aro-terms.txt.
  accessed_at: '2026-10-21T19:09:19Z'
  support: supports
  summary: Current ARO repeats the native spectrum/accumulation wording and sole cited
    PMID35315272, with ChEBI219023 and PubChem146684527. The broader class describes
    the threaded lariat topology of ribosomal peptides. It does not independently
    verify the spectrum sentence or the seventeen unspecified centres. A direct alternate
    CARD hostname failed TLS validation; no content from it was treated as verified.
  snapshot_sha256: 68aa7cd21116e4edef8e140620ca82524559e46de51d8907628afe0210c53a93
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/146684527/property/MolecularFormula,MolecularWeight,IsomericSMILES,InChI,InChIKey,MonoisotopicMass,Charge/JSON
  locator: Complete official current property response; SMILES/InChI independently
    parsed.
  accessed_at: '2026-10-21T19:09:19Z'
  support: supports
  summary: Current PubChem preserves the native valid graph and all seventeen unspecified
    centres. Formula, neutral charge, monoisotopic mass2031.9148971 and rounded average
    mass2033.2 agree with native and independent calculations. This proves faithful
    source adoption, not a defined stereochemical identity or a racemic experimental
    material.
  snapshot_sha256: bf4245c071e77802579af80053741b5de955a740889c9bbec0eee200d1887e60
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/219023/
  locator: Complete current two-star submitted entry, including default representations,
    source origin and ontology.
  accessed_at: '2026-10-21T19:09:19Z'
  support: supports
  summary: ChEBI219023 has no definition; its submitted InChI/key agrees with the
    native unspecified structure and names Klebsiella pneumoniae4541-2 as an origin,
    citing PMID28106375. Its separate displayed imidazole SMILES lacks the required
    [nH] and fails parsing, but native PubChem SMILES and ChEBI InChI are valid. That
    upstream string is not an invalid-native-structure finding or evidence that the
    entire cross-reference denotes a different graph.
  snapshot_sha256: cfed33f2eabf4d7630198b8de5fc88c57da76978fa60878effe8773e18ed03fd
- evidence_id: original2017
  kind: primary_source
  reference: PMID:28106375; DOI:10.1021/acschembio.6b01154
  locator: Complete original abstract; official18-page supporting information text,
    particularly klebsidin TablesS4/S6/S7 and FiguresS2/S8/S9/S11; FigureS11 actual
    page viewed. Main article retrieval returned403.
  accessed_at: '2026-10-21T19:09:19Z'
  support: supports
  summary: 'The original study identifies klebsidin and acinetodin from human bacterial
    isolates and reports bacterial RNA-polymerase inhibition. Klebsidin supplementary
    NMR assignments enumerate GSDGPIIEFFNPNGVMHYG, nineteen residues. TableS4/MALDI
    fragmentation and NMR calculations support the sequence and lasso assignment.
    FigureS9 tests intracellular kleABC expression; FigureS11 applies5µL of1mM klebsidin
    to E.coli BW25113 lawns: the empty-vector host is not inhibited whereas K.pneumoniae4541-2
    fhuA expression permits inhibition. The assay uses M9 agar, 0.6% overlay, ampicillin/arabinose,30°C24h,
    three experiments. These zone results are not broth MICs. The paper abstract supports
    RNAP action but inaccessible main assay details/quantitative affinities are not
    invented. MicrocinJ25 and acinetodin results are kept separate.'
  snapshot_sha256: a72c1978b962a423cf51b41a3296c2365326b3fc654194ecf4b9b71550c17091
- evidence_id: pdb
  kind: primary_source
  reference: PDB:5UI7; https://files.rcsb.org/download/5UI7.cif
  locator: Original2017-linked solution-NMR deposition; entity_poly, full entity sequence,
    residue identities and standard-component chiral annotations.
  accessed_at: '2026-10-21T19:09:19Z'
  support: supports
  summary: 5UI7 is a klebsidin solution-NMR ensemble, not a klebsidin–RNAP complex.
    Entity1 is explicitly polypeptide(L), nstd_monomer=no, with nineteen residues
    GSDGPIIEFFNPNGVMHYG. Standard L residues give fifteen chiral alpha carbons plus
    the two isoleucine beta centres. The exact Gly1-to-Glu8 macrolactam is independently
    supplied by the primary topology/2022 description. The depositor lists252 distance
    restraints and a ten-model ensemble. This structural model is evidence for defined
    peptide stereochemical scope; no new absolute-configuration experiment or RNAP
    contact map is claimed.
  snapshot_sha256: 320441a6d08280e47757b7282e11866932ea433ce9a8a3eb59a771d776da0e78
- evidence_id: chemical-diagnostic
  kind: validation
  reference: 058-root-chem.py; 058-root-chemistry.json
  locator: Independent L-sequence construction and explicit Gly1 nitrogen–Glu8 side-chain
    carbonyl closure; dehydration and full constitution comparison.
  accessed_at: '2026-10-21T19:09:19Z'
  support: supports
  summary: The primary-sequence/L-residue diagnostic reconstructs neutral C93H129N23O27S
    with seventeen assigned centres and full keyXNBIEFNBLNDRGW-ILRSLDFVSA-N. Removing
    only stereochemistry reproduces the full native key. Thus the stored constitution
    contains the correct sequence/macrolactam but loses its known stereochemical specification.
    Ordinary SMILES/InChI do not encode physical lasso threading; this diagnostic
    does not claim to establish topology from a two-dimensional graph.
  snapshot_sha256: 81b4b3546288f39d9e303581ab394f7dff8261b7997f54a96f891d771163e55f
- evidence_id: adopted2022
  kind: primary_source
  reference: PMID:35315272; DOI:10.1021/acschembio.2c00148; PMC9976627
  locator: 'Entire scientific main text: Introduction, Results, Discussion and Methods;
    actual Figures1/4/5 viewed; official SI text with actual S8/S11 pages viewed.'
  accessed_at: '2026-10-21T19:09:19Z'
  support: supports
  summary: The sole adopted source explicitly assigns the Enterobacteriaceae including
    Escherichia/Salmonella statement to microcinJ25. It then distinguishes klebsidin,
    describing K.pneumoniae targeting, fhuA-dependent E.coli access and intracellular
    expression without export. Its main selection expresses kleABC in E.coli DH10B
    with70µM IPTG and measures growth enrichment for320/361 single variants. This
    integrates biosynthesis, stability and RNAP inhibition while bypassing extracellular
    uptake; it is not a minimum inhibitory concentration panel. The producer pathway
    and Gly1/Glu8 ring are supported. No Salmonella wild-type-klebsidin experiment
    is present in the inspected main/SI; this is a document-bounded statement, not
    a claim that no such experiment exists anywhere.
  snapshot_sha256: 3e64198c54389d800e9a85e6a27c0ff00072b3d497694f3b4c4e423c43f24eb9
- evidence_id: external2022
  kind: primary_source
  reference: PMID:35315272 Figure4; supplementary FiguresS7/S8/S11
  locator: Complete external zone-assay Methods, exact wild-type panels and captions;
    actual plate images viewed.
  accessed_at: '2026-10-21T19:09:19Z'
  support: supports
  summary: Purified wild-type klebsidin inhibits K.pneumoniae KP23 at the250µM spotting
    dilution in Figure4E and E.coli BW25113 at500µM in S8. P12V separately reaches125µM
    against KP23; that variant endpoint is not parent klebsidin. Assays spot5µL from1mM
    twofold dilutions on Mueller-Hinton agar with5mL top agar containing10^7CFU, incubated16h37°C.
    These are spotting-solution concentrations, not broth MICs or clinical susceptibility
    classifications. No external inhibition of E.coli DH10B or its RpoCT931I derivative
    was observed with1mM wild type/F9Y in S11. Different strains and media account
    for essential experimental scope; earlier2017 BW25113 results are not flattened
    into a universal claim.
  snapshot_sha256: 14f5bdee159bf43fd7bafff5db98a8418c25fd05800fa8e603bf54284b197741
- evidence_id: rnapp2022
  kind: primary_source
  reference: PMID:35315272 Figure5 and Methods
  locator: Relevant engineered-strain Results and Methods; actual Figure5 viewed.
  accessed_at: '2026-10-21T19:09:19Z'
  support: supports
  summary: A CRISPR-installed E.coli DH10B RpoCT931I variant resists intracellular
    wild-type klebsidin. F9Y klebsidin partially restores intracellular growth inhibition
    in that background, yet the purified F9Y variant lacks external KP23/BW25113 inhibition
    at1mM. These results support RNAP-linked cellular action and variant specificity.
    They do not demonstrate exact atomic contacts or direct binding constants; the
    paper discusses a contact hypothesis. No standalone native target object needs
    correction merely for being absent.
  snapshot_sha256: ddac71f7ac4698407a568e022ce57191e3c30363d06d7eaac9da3e7eeca8488f
- evidence_id: later2024
  kind: primary_source
  reference: PMID:39475538
  locator: Complete accessible abstract from exact-name search; main article not inspected.
  accessed_at: '2026-10-21T19:09:19Z'
  support: context_only
  summary: The2024 study concerns a nanocomposite containing acinetodin, capistruin
    and klebsidin with chitosan. Its composite antibacterial endpoints are not evidence
    for single-parent klebsidin spectrum, potency or Salmonella susceptibility. This
    lead is explicitly excluded from individual-parent efficacy inference.
  snapshot_sha256: 54084ed717b40192667fe1cad01b4a37255dbca41ef0bc68606d078d50ca40a7
- evidence_id: adapters
  kind: database
  reference: 579-adapter-results.json;579-adapter-results.txt;579-adapter-scope.json
  locator: Actual structured catalog plus E.coli rpoB and rpoC queries, run before
    open target research.
  accessed_at: '2026-10-21T19:09:19Z'
  support: context_only
  summary: All three commands exit0 and provide annotation context for E.coli b3987/rpoB
    and b3988/rpoC, with no iModulon hit. This is not a klebsidin exposure experiment
    or target-binding proof. The initial batch template N/A scope was corrected after
    reading this native definition and before any open mechanism research.
  snapshot_sha256: b33f0ea2013777ad6ae23d515d3059670909e6d8430b231640c640ed1a2fbaa5
- evidence_id: search
  kind: search
  reference: 579-local-hits.txt;579-owner-hits.txt;579-discovery.json;058-root-fetch1.json
    through058-root-fetch9.json
  locator: Ignored/hidden-inclusive exact record/source search, exact-name public
    primary search and cited original-paper follow-up.
  accessed_at: '2026-10-21T19:09:19Z'
  support: context_only
  summary: All populated fields and the sole adopted citation were assessed. The exact-name
    result contained the2017 original,2022 mutational study and2024 composite paper;
    each received the explicit disposition above. Full primary access limits and failed
    XML/publisher routes are recorded, with2022 main recovered through the author
    PMC page and official supplements from ACS figshare. No complete-literature absence
    claim or paid research is made.
  search_scope: 2026-10-21 exact klebsidin, ARO3007093, CHEBI219023, PubChem146684527,
    full native key and cited PMIDs; hidden and ignored repository files included.
  snapshot_sha256: 54084ed717b40192667fe1cad01b4a37255dbca41ef0bc68606d078d50ca40a7
assessments:
- assessment_id: identity
  area: identity
  topic: Nineteen-residue macrolactam and stereochemical scope
  outcome: unknown
  summary: Constitution, formula, charge and source properties agree. Seventeen defined
    residue configurations are absent from the principal graph; no racemate or opposite
    stereoisomer is established.
  target_ids:
  - antibioticmech:aro-1d2367825f
  evidence_ids:
  - native
  - pubchem
  - chebi
  - pdb
  - chemical-diagnostic
- assessment_id: grounding
  area: grounding
  topic: Mint, three xrefs and broader lasso class
  outcome: supported
  summary: ARO and the two chemistry authorities match the named source and unspecified
    native graph. The historical fallback/mint and broader class fit. Future stereo
    correction must also resolve exact-xref scope instead of calling the specified
    and unspecified graphs exact equivalents.
  target_ids:
  - antibioticmech:aro-1d2367825f
  evidence_ids:
  - owners
  - aro
  - pubchem
  - chebi
  - pdb
- assessment_id: definition
  area: evidence
  topic: Producer, spectrum and exposure route
  outcome: concern
  summary: K.pneumoniae origin and RNAP-linked action are supported. The adopted source
    attributes the broad Enterobacteriaceae/Salmonella sentence to another lasso peptide.
    Actual klebsidin activity must retain named strains, transport and exposure conditions;
    E.coli activity is not entirely denied.
  target_ids:
  - antibioticmech:aro-1d2367825f
  evidence_ids:
  - original2017
  - adopted2022
  - external2022
  - rnapp2022
- assessment_id: mechanism
  area: evidence
  topic: RNA-polymerase action and resistance experiment
  outcome: supported
  summary: Original primary abstract and2022 engineered-RpoC data support RNAP-linked
    activity. Annotation adapters are context; lasso NMR is not an RNAP complex. No
    quantitative affinity, clinical use or universal permeability claim is made.
  target_ids:
  - antibioticmech:aro-1d2367825f
  evidence_ids:
  - original2017
  - pdb
  - adopted2022
  - rnapp2022
  - adapters
- assessment_id: provenance
  area: provenance
  topic: Maintained source ownership and capture integrity
  outcome: supported
  summary: Native fields faithfully inherit ARO/PubChem. Original thirteen hashes
    and the three actual-owner additions are preserved. The generated source owners,
    rather than direct YAML edits, control the proposed corrections.
  target_ids:
  - antibioticmech:aro-1d2367825f
  evidence_ids:
  - native
  - owners
  - aro
- assessment_id: coverage
  area: completeness
  topic: All native fields, adopted source and bounded primary leads
  outcome: supported
  summary: Whole-record review covers identity, broad class, definition, all xrefs,
    structure and provenance. The sole adopted main and SI were inspected. Optional
    targets, MICs and graphs were not required merely because absent; the two findings
    concern populated identity and spectrum.
  target_ids:
  - antibioticmech:aro-1d2367825f
  evidence_ids:
  - search
  - native
  - adopted2022
  - original2017
  - later2024
findings:
- finding_id: F1
  issue_key: klebsidin-missing-known-peptide-stereochemistry
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Preserve the defined peptide stereochemistry
  description: All seventeen tetrahedral sites are unspecified in the native principal
    graph, although the original-linked structural deposition explicitly defines the
    nineteen-residue L peptide and standard residues. Independent L-sequence/macrolactam
    reconstruction agrees with native constitution and formula. Resolve exact stereochemical
    scope and maintained groundings before regenerating an assigned graph; no opposite
    enantiomer or physical mixture is established.
  target_ids:
  - antibioticmech:aro-1d2367825f
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  evidence_ids:
  - native
  - pubchem
  - pdb
  - chemical-diagnostic
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted unspecified fallback graph
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem retrieval and property normalization
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Exact identity/grounding decision
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Principal chemical representation and xref emission
  rule_id: 'Native checklist: exact structure and claim-level primary support'
  native_severity: major
  normalization_reason: A populated scientific claim needs substantive source-owned
    correction; valid native chemistry is not an invalid-SMILES blocker.
- finding_id: F2
  issue_key: klebsidin-spectrum-from-microcin-j25
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Correct the spectrum attribution and exposure context
  description: The native broad Enterobacteriaceae/Escherichia/Salmonella wording
    reproduces a sentence the cited paper applies to microcinJ25. The klebsidin study
    instead reports strain- and delivery-dependent results, including intracellular
    expression and high-concentration external spot assays. Replace the transferred
    Salmonella/family-wide implication with exact klebsidin evidence, retaining demonstrated
    E.coli/K.pneumoniae results and their limits. Do not claim that Salmonella can
    never be affected.
  target_ids:
  - antibioticmech:aro-1d2367825f
  field_paths:
  - definition
  evidence_ids:
  - aro
  - adopted2022
  - external2022
  - original2017
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Inherited spectrum/definition and citation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ARO definition extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Definition emission
  rule_id: 'Native checklist: exact structure and claim-level primary support'
  native_severity: major
  normalization_reason: A populated scientific claim needs substantive source-owned
    correction; valid native chemistry is not an invalid-SMILES blocker.
actions:
- action_id: A1
  description: Resolve and regenerate the exact L-peptide identity with scoped authority
    links.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-1d2367825f
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted unspecified fallback graph
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem retrieval and property normalization
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Exact identity/grounding decision
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Principal chemical representation and xref emission
  acceptance_checks:
  - Independently confirm GSDGPIIEFFNPNGVMHYG, Gly1–Glu8 side-chain macrolactam, fifteen
    L alpha centres and two L-isoleucine beta centres from original-linked data.
  - Primary-sequence diagnostic candidate is XNBIEFNBLNDRGW-ILRSLDFVSA-N; verify it
    independently before adoption and handle the current unspecified ChEBI/PubChem
    references explicitly.
  - Preserve lasso topology descriptively/with primary evidence; ordinary SMILES alone
    does not encode threading. Run schema, strict, chemistry, grounding and source
    reproduction checks.
- action_id: A2
  description: Replace the transferred spectrum sentence with bounded klebsidin evidence.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-1d2367825f
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Inherited spectrum/definition and citation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ARO definition extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Definition emission
  acceptance_checks:
  - The regenerated definition cites the actual klebsidin experiments; no Salmonella
    or broad family claim is retained solely from the MccJ25 introduction.
  - Keep extracellular strain-specific spot concentrations separate from broth MIC
    and from intracellular kleABC induction. Preserve K.pneumoniae KP23/E.coli BW25113
    positives and DH10B negative conditions.
  - Keep wild-type klebsidin separate from P12V/F9Y variants and the2024 multi-peptide
    chitosan composite.
limitations:
- The2017 original abstract and official supplementary text were inspected; its main
  article retrieval returned403, so exact transcription-inhibition protocol or affinity
  is not claimed read. Actual SI FigureS11 was viewed; spectra and coordinate ensembles
  were not reprocessed.
- The2022 scientific main, Methods and official SI text were read, with actual Figures1/4/5
  and S8/S11 viewed. Oligonucleotide listings were inspected as context, not independently
  validated by experimental reconstruction.
- The PDB NMR entry is an isolated L peptide, not an RNAP complex. Sequence-based
  chemical reconstruction supports constitution/stereo completeness and does not prove
  threading or new absolute stereochemistry experimentally.
- Current ChEBI standalone SMILES is invalid while its InChI and native PubChem SMILES
  agree; the invalid upstream serialization is explicitly separated from the native
  findings.
- The2024 composite study was abstract-only; no parent-specific MIC or mechanistic
  detail was inferred. There is no global negative claim about Salmonella literature.
- Structured source adapters return gene annotation context only; no iModulon or exposure
  evidence was returned. The originally templated adapter-scope entry was corrected
  before external mechanism research.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All changes are review artifacts only. Original sixteen current captured hashes
  are verified; the original thirteen are preserved. Shared full-QC disposition is
  added before final validation.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
