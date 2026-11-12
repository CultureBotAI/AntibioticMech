# Klebsazolicin: supported ribosomal mechanism; known Pro4 stereochemistry is omitted

- Review: 20261021T192406Z-klebsazolicin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:53:55Z
- Finished UTC: 2026-10-21T19:24:06Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The full adopted original supports the RiPP identity, genome-guided discovery, antibacterial activity and nascent-peptide exit-tunnel inhibition. The native graph is internally coherent and matches current PubChem, but both omit the Pro4 S annotation explicitly shown in the publisher’s final Figure 1 and corroborated by the deposited model. One major source-owned stereochemical completeness correction is needed; primary material, strain, medium, transport and derivative boundaries are retained.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Assigned queue position 578; one exact native record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-2b2f71621c | data/antibiotics/antibacterial/klebsazolicin.yaml | generated | klebsazolicin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-2b2f71621c | Actual focused execution exited 0. Executed against058; chemistry used existing019 RDKit while schema/strict used058. |
| Focused schema verification | passed | True | antibioticmech:aro-2b2f71621c | Actual focused execution exited 0. Executed against058; chemistry used existing019 RDKit while schema/strict used058. |
| Focused strict verification | passed | True | antibioticmech:aro-2b2f71621c | Actual focused execution exited 0. Executed against058; chemistry used existing019 RDKit while schema/strict used058. |
| Authoritative full QC | failed | True | antibioticmech:aro-2b2f71621c | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-2b2f71621c | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-2b2f71621c | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-2b2f71621c | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-2b2f71621c | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-2b2f71621c | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-2b2f71621c | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-2b2f71621c | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-2b2f71621c | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Complete molecular annotation and exact compound boundary

identity: concern. Targets: antibioticmech:aro-2b2f71621c.

Connectivity, composition, masses, charge, assigned stereocentres and minted ARO identity are coherent. Pro4 is the sole unknown tetrahedron in native and current PubChem, but the publisher final primary figure explicitly assigns S and the deposited model agrees. This is an inherited omission of known stereochemistry, not evidence of a racemate or an asserted opposite enantiomer.

### RiPP parent/class and current source groundings

grounding: supported. Targets: antibioticmech:aro-2b2f71621c.

ARO class membership is broader and supported by heterologous expression of a ribosomal precursor/maturation cluster. Current PubChem matches the stored partial graph. A future fully specified repair must reassess exact-PubChem equivalence instead of silently keeping an unresolved stereo record as identical; PDB/BIRD is contextual structural evidence only.

### Native definition and antibacterial eligibility

evidence: supported. Targets: antibioticmech:aro-2b2f71621c.

The sole adopted original was read in full, including Methods and Tables 1–2, and directly supports antibacterial activity and ribosomal exit-tunnel inhibition. Producer-genome, assay-host and structural-host identities remain distinct. The later synthetic panel broadens conditional activity without refuting the original strain-specific observations. Native peptide-access wording is imprecise but does not explicitly assert a different binding site.

### Optional mechanistic, producer and activity enrichment

completeness: unknown. Targets: antibioticmech:aro-2b2f71621c.

Native has no required populated target/resistance/activity slot to repair beyond the known structural omission. The original supports bounded future annotations for exit-tunnel rRNA, engineered mutations and strain-specific MICs, but no generic protein target, universal clinical spectrum or transport-binding conclusion. Inaccessible supplementary and2024 figure details remain explicit.

### Actual owners and historical state

provenance: supported. Targets: antibioticmech:aro-2b2f71621c.

Original 13 and expanded 26 captured inputs remain unchanged. Complete ARO and PubChem owner rows explain native generation and all three seed/reseed events. Corrections belong in maintained source/enrichment handling; no generated YAML, history or curation status was altered.

## Findings

### F1: The graph omits the established Pro4 S configuration

major / open / confirmed; issue key: klebsazolicin-pro4-known-stereo-omitted.

Native SMILES atom 110 and InChI atom 48 are unspecified, matching current adopted PubChem. The final publisher Figure 1b explicitly labels this natural proline S, and the linked 5W4K model maps it to L-PRO with matching local coordinates. The molecular annotation is materially incomplete despite internal validation passing. The scratch one-atom S candidate changes only this stereo tag and yields RSVIJELKMXTPMI-GFJPOFEGSA-N; it is not an automatic record replacement.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate and encode the primary-supported Pro4 S annotation through maintained structure ownership, then reconcile dependent exact groundings.

- Use the publisher final Figure 1b and mapped deposited PRO3/Pro4 evidence; preserve the manuscript-versus-final graphical difference and the limits of the truncated PDB model.
- Introduce a reproducible source/curator structure correction for Pro4 S; retain all other centres, full 23-residue connectivity, formula and neutral molecular form. Regenerate matching SMILES/InChI/key together.
- Do not infer a racemate from the old unknown centre. Recheck PubChem 146684557 against the repaired fully specified graph and qualify or resolve exact equivalence if it still omits Pro4; do not replace the molecule with BIRD’s truncated formula.
- Rerun focused/schema/strict and required shared corpus gates after a future source-owned correction.

### A2

Optional evidence enrichment should state nascent-peptide exit-tunnel obstruction and preserve exact experimental scope.

- Keep K. pneumoniae genome donor, E. coli heterologous producer/assay backgrounds and T. thermophilus ribosome structural host distinct.
- Store single-agent MICs with exact media, strains, inoculum, duration and censoring; keep2017 and 2024 material/panel differences and analogues separate.
- Treat uptake/self-resistance phenotypes and engineered 23S rRNA mutations at their actual evidence level, not as direct transporter binding or population susceptibility. Missing optional slots alone are not validation failures.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/klebsazolicin.yaml; Entire native record, source concept and all three history events | supports | The SEEDED ARO-minted record denotes a neutral C76H107N27O30S3 peptide with 15 assigned and one unspecified tetrahedral centre. It has one KLB synonym, one RiPP parent/class, ARO and PubChem chemical links, and no separate structured target/resistance/activity/producer/product/causal graph objects; definition claims are assessed below. Its definition cites the sole adopted PMID28846667. |
| owners | data/raw/aro_antibiotics.tsv#ARO:3009315; data/raw/pubchem_structures.tsv#pubchem.compound:146684557; Complete exact ARO row 635, PubChem row 262 and readiness row 2739 | context_only | The ARO row supplies the names, class, definition and sole PMID lead; adopted PubChem enrichment supplies the partially specified graph. Exact source searches found no matching target, resistance, ChEBI, curator or decisions row. Broad parent-class search also returns other RiPP rows, which are not this record. Original 13 hashes were preserved and expanded to 26 before detailed judgment. |
| pubchem-owner | data/raw/pubchem_structures.tsv; Complete exact row 262, including enrichment provenance | context_only | The adopted PubChem row already contains the same unknown Pro4 stereocentre; this is inherited input, not a YAML parsing or seeding loss. The actual raw inventory and enrichment transform were appended to captured inputs and ownership before the chemical assessment. |
| local-search | /private/tmp/am-review-session/578-context-search.txt; Initial target scan plus follow-up including ignored and hidden files | context_only | Identifier, exact label, ARO molecule and broader RiPP class were searched with gitignore-independent coverage. Source absence conclusions apply to the inspected inventories; parent-class hits are not mistaken for exact molecular evidence. |
| aro-current | https://raw.githubusercontent.com/arpcard/aro/master/aro.obo; Exact current ARO 3009315 and ARO 3009656 terms from captured official OBO | supports | The molecule term identifies klebsazolicin/KLB, its adopted original and PubChem link; the broader term defines the RiPP class. Actual biosynthetic work supports class membership. Current source definition retains the broad peptide-access wording. A guessed numeric CARD web route was not verified as this term and is not relied on. |
| pubchem-current | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/146684557/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass/JSON; Exact current CID 146684557 molecular response | supports | Current PubChem reproduces native formula, neutral charge, full key RSVIJELKMXTPMI-CKSXXEILSA-N and the sole unknown proline centre. Therefore the asserted current xref is coherent with the graph as stored; independent primary structure evidence exposes a shared annotation omission. |
| adapter | /private/tmp/am-review-session/578-adapter-network.json; Structured expression search before open primary research | context_only | The catalog had no matching Klebsiella dataset. An E. coli precise1k ribosome search returned a generic Translation component and gene hits, not KLB perturbation or binding-site data. Initial sandbox DNS failure was resolved through free network retrieval; the component cannot validate this antibiotic’s mechanism. |
| adapter-summary | /private/tmp/am-review-session/578-adapter-summary-corrected.json; Translation component 1 summary | context_only | The corrected summarize command reports 53 members with mapped UniProt identifiers, but supplies no compound-specific evidence. An earlier command-argument error is preserved separately and is not a biological no-hit. No module member is converted into a native molecular target. |
| primary-discovery | PMID:28846667; DOI:10.1038/nchembio.2462; Complete original scientific main, Methods and exact Tables 1–2 | supports | K. pneumoniae subsp. ozaenae ATCC11296 genomic cluster klpABCDE was expressed in surrogate E. coli BL21(DE3). Culture supernatant was purified by C18 and reverse-phase HPLC with 0.1% TFA, lyophilized and dissolved in DMSO. The full 23-residue core and modifications were established by MS and extensive 2D NMR; the publication does not require a defined TFA stoichiometric salt to replace the neutral molecular record. Native genome-guided wording is supported; this is not a demonstration of constitutive natural-host secretion in clinical conditions. |
| primary-activity | PMID:28846667; Table 1 and Methods Evaluation of bioactivity | supports | Broth microdilution used approximately 5e5 cells/mL, twofold dilutions in 100 µL, incubation 37 °C for 16–20h, with listed 30 °C and two-day organism exceptions. LB MICs were 32 µg/mL for E. coli B,128 for MG1655,64 for Y. pseudotuberculosis IP32953 and 128 for K. pneumoniae 875; M9+glucose values were 4, 16 and 64 for E. coli B/MG1655/K. pneumoniae, respectively. Tested Pseudomonas, Acinetobacter, Vibrio and Gram-positive backgrounds exceeded 1024 µg/mL in LB. This supports conditional activity, not all Gram-negative species or clinical efficacy. |
| primary-transport | PMID:28846667; Table 1, uptake discussion and cloning methods | context_only | In E. coli MG1655, deleting ompF increased LB MIC from 128 to 256 µg/mL and deleting sbmA raised it above 1024; sbmA/ompF overexpression lowered it to 64. klpE expression increased MIC to 1024. These genetic susceptibility data support uptake/export-related interpretations; they are not direct transporter binding measurements or transferable clinical resistance thresholds. |
| primary-mechanism | PMID:28846667; Full mechanism Results/Methods, Figures 2–4 captions and actual Figure 3 inspected | supports | E. coli reporter, S30 luciferase IC50 .34±.04 µM, chemical footprinting and osmC toeprinting establish translation elongation inhibition. The2.7 Å T. thermophilus70S structure places KLB in the 50S nascent-peptide exit tunnel, overlapping macrolide/streptogramin sites. The PTC remains compatible with A/P-site substrates; the mechanism is obstruction of nascent-peptide passage, not competitive exclusion of aminoacyl-tRNA. hns translation is partly resistant, so sequence context matters. Native core mechanism is supported; its peptide-access phrase could be made more precise. |
| primary-figure3 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c03c/5701663/730c6140cd7f/nihms894386f3.jpg; Actual Figure 3 panelsa–g, full image viewed | supports | The density and complex views place the compound near 23S rRNA and label Pro4 among the resolved N-terminal residues. Only the first 19 residues are visible, so neither this image nor a truncated deposited ligand is a full replacement molecular graph. Binding taxon is T. thermophilus; susceptibility and engineered resistance experiments use distinct E. coli backgrounds. |
| primary-resistance | PMID:28846667; Resistance selection and testing Methods plus Results | context_only | Selected E. coli SQ110DTC cells had a single rrn allele, tolC deletion and uptake overexpression; four sequenced resistant clones carried U2609A/G. Reconstructed single-rrn E. coli variants corroborated rRNA-dependent effects. The body and Methods contain inconsistent Table 2 cross-calls: the actual displayed Table 2 is the KLB-derivative table, not an rRNA-mutant table. Do not invent a mutant table or generalize these engineered backgrounds to population resistance. |
| derivative-boundary | PMID:28846667; Actual Table 2 all rows and derivative discussion | context_only | S1A, Q2N, S3A, A14K and truncated/azole variants are distinct molecules. The intact KLB row has M9+glucose MG1655 MIC 16 µg/mL; truncated constructs can inhibit cell-free translation without whole-cell activity. Such results support structure/function hypotheses but are not quantitative observations on the exact native compound. |
| publisher-structure | https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fnchembio.2462/MediaObjects/41589_2017_Article_BFnchembio2462_Fig1_HTML.jpg; Publisher final Figure 1b, actual full image and enlarged N-terminal region inspected | refutes | The final publisher structure explicitly labels Pro4 S and depicts the dashed C-alpha/carbonyl bond. Its other displayed alpha centres are S and the Thr19 beta centre is R, agreeing with the existing assigned native centres. The manuscript image differs at the proline depiction; the final figure and deposited model resolve the omitted native annotation. |
| manuscript-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c03c/5701663/0a2693b2e8ae/nihms894386f1.jpg; Actual manuscript Figure 1b and enlarged proline region | context_only | The manuscript graphic is not identical to the publisher final figure and lacks its explicit configuration labels; its proline bond rendering is unsuitable as the sole stereochemical authority. Both versions are retained transparently, and the final publisher figure is the decisive2D source for Pro4 S. |
| pdb-model | https://models.rcsb.org/v1/5w4k/atoms?label_asym_id=ID&amp;encoding=cif; Original-linked PDB 5W4K; entity 58, chain ID/auth A, PRO sequence3 | supports | The source’s deposited model maps Ser1-Gln2 to monomer9VA and natural Pro4 to standard PRO at polymer sequence 3. Actual CA/N/C/CB coordinates have the same local handedness as standard L-PRO S. This corroborates the final figure without claiming independent re-refinement or absolute stereochemical proof from raw diffraction. Only residues 1–19 are represented; BIRD formula is therefore not the full molecule formula. |
| pdb-components | https://files.rcsb.org/ligands/view/PRO.cif; PRO CCD and PRD 002277 residue/link definitions | supports | Standard PRO is explicitly L-PEPTIDE LINKING with alpha-C S. PRD sequence/link records map SER2–PRO3–GLY4 onto natural Ser3–Pro4–Gly5. This is a mapped structural comparison, not a substitution of a macromolecular accession for exact chemical identity. |
| mapping | /private/tmp/am-review-session/578-map.py; 019 RDKit2026.03.5 against058; complete graph and local-coordinate diagnostics | supports | Four native/current-PubChem encodings agree. The missing centre is native SMILES atom 110, InChI atom 48, with N114, carbonylC108 and ringC111 neighbours. Setting only atom 110 to S gives full key RSVIJELKMXTPMI-GFJPOFEGSA-N, unchanged composition/charge and all 16 centres assigned. PDB scalar triple product 2.18196 and CCD S reference 2.74624 have matching sign. Candidate is a diagnostic for curator review, not a native edit. |
| biosynthesis2018 | PMID:29601195; DOI:10.1021/jacs.8b02277; Complete additional original abstract only | context_only | The in-vitro biosynthesis study identifies KlpD YcaO as the enzyme required for azole and amidine formation, with TldD/E processing. These are biosynthetic enzymes rather than antibiotic inhibition targets. This comparator was not an adopted lead and its full experimental data were not inspected. |
| synthesis2024 | PMID:38923770; DOI:10.1002/anie.202407952; Complete original scientific main and Table 1 via publisher web text | context_only | Synthetic KLB compound 5 was purified separately from 11 analogues. In M9+glucose it had MIC 32 µg/mL against E. coli 5, .25 against B. cereus BC177/BC107, .25/.5 against V. cholerae V1978/V1853, and &gt;128 against E. coli CL4 and K. pneumoniae Hvkp7/FJ8. The paper reports no activity in its LB panel. These distinct material/strain/media results do not erase the 2017 panel or imply universal Gram-negative restriction. Exact assay inoculum/incubation and raw spectra remain inaccessible in SI; streptamidine epimerization is not transferred to KLB. |
| web-notes | /private/tmp/am-review-session/578-web-reading-notes.json; Reviewer paraphrase notes for successful2024 web text | context_only | The notes identify actual reading scope and exact source URL; their hash is not a downloaded publisher PDF hash. Original PDF, SI and figure fetch failures remain in manifests. The 2024 structure drawing itself was not viewed and supplies no decisive Pro4 assignment here. |
| access | /private/tmp/am-review-session/578-fetch4.json; Public free retrieval boundaries across fetch1–9 | context_only | 2017 main XML and actual manuscript/publisher figures were obtained. PMC SI routes returned HTML, CDN routes404, static host DNS failure, and EPMC supplementary ZIP contained only an empty image entry.2024 Wiley/CityU/ResearchGate PDF, SI and figure routes returned403; publisher web text remained readable. No paywall purchase or contact occurred. |

## Limits And Additional Notes

- The sole adopted 2017 original scientific main, Methods and Tables 1–2 were fully read. Actual manuscript Figure 1, publisher final Figure 1 and Figure 3 were viewed; other plots and original SI were not independently inspected. Failed SI routes and empty EPMC ZIP are retained.
- The 2024 additional original main/Table 1 was read through publisher web text, but its actual figures, SI, spectra, precise bioassay setup and complete synthetic salt characterization were inaccessible. Its quantitative results are comparison evidence with those limits. The 2018 biosynthetic comparator remains abstract-level.
- PDB 5W4K is the original-linked refined model, not independently re-refined diffraction evidence; only the resolved N-terminal 19 residues are represented. Standard PRO mapping and local coordinates corroborate the explicit final 2D figure without supplying a whole-molecule replacement.
- Current PubChem is internally consistent with native but shares the unknown Pro4 annotation. ARO’s official OBO was checked; a guessed numeric CARD webpage was not validated as this term and is not used.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All original 13 and expanded 26 input hashes were checked unchanged at draft writing. No native/source/history/progress/saved-bundle/Git writes occurred.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T192406Z-klebsazolicin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Klebsazolicin: supported ribosomal mechanism; known Pro4 stereochemistry is
  omitted'
started_at: '2026-10-21T18:53:55Z'
finished_at: '2026-10-21T19:24:06Z'
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
summary: The full adopted original supports the RiPP identity, genome-guided discovery,
  antibacterial activity and nascent-peptide exit-tunnel inhibition. The native graph
  is internally coherent and matches current PubChem, but both omit the Pro4 S annotation
  explicitly shown in the publisher’s final Figure 1 and corroborated by the deposited
  model. One major source-owned stereochemical completeness correction is needed;
  primary material, strain, medium, transport and derivative boundaries are retained.
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
  - path: data/antibiotics/antibacterial/klebsazolicin.yaml
    sha256: 771419f37751e2e532c37a1a399c08f7979f4daa56ad3999dfb688e27e18568a
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
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: antibioticmech:aro-2b2f71621c
  path: data/antibiotics/antibacterial/klebsazolicin.yaml
  label: klebsazolicin
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
    role: Actual PubChem structure/composition accession mapping owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained PubChem enrichment transform
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Assigned queue position 578; one exact native record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-2b2f71621c
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0. Executed against058; chemistry used
    existing019 RDKit while schema/strict used058.
  target_ids:
  - antibioticmech:aro-2b2f71621c
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    578
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against058; chemistry used
    existing019 RDKit while schema/strict used058.
  target_ids:
  - antibioticmech:aro-2b2f71621c
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/klebsazolicin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against058; chemistry used
    existing019 RDKit while schema/strict used058.
  target_ids:
  - antibioticmech:aro-2b2f71621c
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/klebsazolicin.yaml --out /private/tmp/am-review-session/578-strict.tsv
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
  - antibioticmech:aro-2b2f71621c
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
  - antibioticmech:aro-2b2f71621c
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
  - antibioticmech:aro-2b2f71621c
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
  - antibioticmech:aro-2b2f71621c
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
  - antibioticmech:aro-2b2f71621c
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
  - antibioticmech:aro-2b2f71621c
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
  - antibioticmech:aro-2b2f71621c
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
  - antibioticmech:aro-2b2f71621c
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
  - antibioticmech:aro-2b2f71621c
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/klebsazolicin.yaml
  locator: Entire native record, source concept and all three history events
  accessed_at: '2026-10-21T19:05:59Z'
  support: supports
  summary: The SEEDED ARO-minted record denotes a neutral C76H107N27O30S3 peptide
    with 15 assigned and one unspecified tetrahedral centre. It has one KLB synonym,
    one RiPP parent/class, ARO and PubChem chemical links, and no separate structured
    target/resistance/activity/producer/product/causal graph objects; definition claims
    are assessed below. Its definition cites the sole adopted PMID28846667.
  snapshot_sha256: 771419f37751e2e532c37a1a399c08f7979f4daa56ad3999dfb688e27e18568a
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv#ARO:3009315; data/raw/pubchem_structures.tsv#pubchem.compound:146684557
  locator: Complete exact ARO row 635, PubChem row 262 and readiness row 2739
  accessed_at: '2026-10-21T19:05:59Z'
  support: context_only
  summary: The ARO row supplies the names, class, definition and sole PMID lead; adopted
    PubChem enrichment supplies the partially specified graph. Exact source searches
    found no matching target, resistance, ChEBI, curator or decisions row. Broad parent-class
    search also returns other RiPP rows, which are not this record. Original 13 hashes
    were preserved and expanded to 26 before detailed judgment.
  snapshot_sha256: 02327b3c7a8db993571c07d45bab4543245cf12dec9dee82dfa15472f40e386e
- evidence_id: pubchem-owner
  kind: record_content
  reference: data/raw/pubchem_structures.tsv
  locator: Complete exact row 262, including enrichment provenance
  accessed_at: '2026-10-21T19:05:59Z'
  support: context_only
  summary: The adopted PubChem row already contains the same unknown Pro4 stereocentre;
    this is inherited input, not a YAML parsing or seeding loss. The actual raw inventory
    and enrichment transform were appended to captured inputs and ownership before
    the chemical assessment.
  snapshot_sha256: b47b384c052cbfbb1794677a7a6bd33fdc4a052d8f7fed084a973c0e98a014cc
- evidence_id: local-search
  kind: search
  reference: /private/tmp/am-review-session/578-context-search.txt
  locator: Initial target scan plus follow-up including ignored and hidden files
  accessed_at: '2026-10-21T19:05:59Z'
  support: context_only
  summary: Identifier, exact label, ARO molecule and broader RiPP class were searched
    with gitignore-independent coverage. Source absence conclusions apply to the inspected
    inventories; parent-class hits are not mistaken for exact molecular evidence.
  snapshot_sha256: b121572e203bc3da043f8d18a673866253f2fab591bffba465b3283fa3d5447c
  search_scope: Initial preserved578-local-hits plus rg --no-ignore --hidden across
    curation, conf, scripts and data/raw.
- evidence_id: aro-current
  kind: authority
  reference: https://raw.githubusercontent.com/arpcard/aro/master/aro.obo
  locator: Exact current ARO 3009315 and ARO 3009656 terms from captured official
    OBO
  accessed_at: '2026-10-21T15:57:42Z'
  support: supports
  summary: The molecule term identifies klebsazolicin/KLB, its adopted original and
    PubChem link; the broader term defines the RiPP class. Actual biosynthetic work
    supports class membership. Current source definition retains the broad peptide-access
    wording. A guessed numeric CARD web route was not verified as this term and is
    not relied on.
  snapshot_sha256: 572a9eca14cd9eada44c73538df715983da7f5698a17cf8cd6d8af48bb92c80a
- evidence_id: pubchem-current
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/146684557/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass/JSON
  locator: Exact current CID 146684557 molecular response
  accessed_at: '2026-10-21T18:58:18.815204Z'
  support: supports
  summary: Current PubChem reproduces native formula, neutral charge, full key RSVIJELKMXTPMI-CKSXXEILSA-N
    and the sole unknown proline centre. Therefore the asserted current xref is coherent
    with the graph as stored; independent primary structure evidence exposes a shared
    annotation omission.
  snapshot_sha256: f732e7c098b4e9406858dbed2c326928e4996d4e6857f3891fbb5f1032c528ad
- evidence_id: adapter
  kind: search
  reference: /private/tmp/am-review-session/578-adapter-network.json
  locator: Structured expression search before open primary research
  accessed_at: '2026-10-21T19:05:59Z'
  support: context_only
  summary: The catalog had no matching Klebsiella dataset. An E. coli precise1k ribosome
    search returned a generic Translation component and gene hits, not KLB perturbation
    or binding-site data. Initial sandbox DNS failure was resolved through free network
    retrieval; the component cannot validate this antibiotic’s mechanism.
  snapshot_sha256: 9b7b571666b327c0541cc9102aef778f2cff0559a7ff751c64dc3efc04ab1c4d
  search_scope: Pre-open catalog456460-adapter-catalog; E. coli/precise1k query ribosome;
    exact command and actual response retained.
- evidence_id: adapter-summary
  kind: search
  reference: /private/tmp/am-review-session/578-adapter-summary-corrected.json
  locator: Translation component 1 summary
  accessed_at: '2026-10-21T19:05:59Z'
  support: context_only
  summary: The corrected summarize command reports 53 members with mapped UniProt
    identifiers, but supplies no compound-specific evidence. An earlier command-argument
    error is preserved separately and is not a biological no-hit. No module member
    is converted into a native molecular target.
  snapshot_sha256: e3ee646cbbe316a9a169d761e2dcd9ad85e47fe62958e8ef9d8ee1fe787debaf
  search_scope: Actual corrected kg-microbe-sources imodulondb --timeout 15 summarize
    --organism e_coli --dataset precise1k --k 1.
- evidence_id: primary-discovery
  kind: primary_source
  reference: PMID:28846667; DOI:10.1038/nchembio.2462
  locator: Complete original scientific main, Methods and exact Tables 1–2
  accessed_at: '2026-10-21T18:58:39.254013Z'
  support: supports
  summary: K. pneumoniae subsp. ozaenae ATCC11296 genomic cluster klpABCDE was expressed
    in surrogate E. coli BL21(DE3). Culture supernatant was purified by C18 and reverse-phase
    HPLC with 0.1% TFA, lyophilized and dissolved in DMSO. The full 23-residue core
    and modifications were established by MS and extensive 2D NMR; the publication
    does not require a defined TFA stoichiometric salt to replace the neutral molecular
    record. Native genome-guided wording is supported; this is not a demonstration
    of constitutive natural-host secretion in clinical conditions.
  snapshot_sha256: 1e7b7b83fb12de6674f45125a07e72532507fb1054efb4d33e62a72f7f95b610
- evidence_id: primary-activity
  kind: primary_source
  reference: PMID:28846667
  locator: Table 1 and Methods Evaluation of bioactivity
  accessed_at: '2026-10-21T18:58:39.254013Z'
  support: supports
  summary: Broth microdilution used approximately 5e5 cells/mL, twofold dilutions
    in 100 µL, incubation 37 °C for 16–20h, with listed 30 °C and two-day organism
    exceptions. LB MICs were 32 µg/mL for E. coli B,128 for MG1655,64 for Y. pseudotuberculosis
    IP32953 and 128 for K. pneumoniae 875; M9+glucose values were 4, 16 and 64 for
    E. coli B/MG1655/K. pneumoniae, respectively. Tested Pseudomonas, Acinetobacter,
    Vibrio and Gram-positive backgrounds exceeded 1024 µg/mL in LB. This supports
    conditional activity, not all Gram-negative species or clinical efficacy.
  snapshot_sha256: 1e7b7b83fb12de6674f45125a07e72532507fb1054efb4d33e62a72f7f95b610
- evidence_id: primary-transport
  kind: primary_source
  reference: PMID:28846667
  locator: Table 1, uptake discussion and cloning methods
  accessed_at: '2026-10-21T18:58:39.254013Z'
  support: context_only
  summary: In E. coli MG1655, deleting ompF increased LB MIC from 128 to 256 µg/mL
    and deleting sbmA raised it above 1024; sbmA/ompF overexpression lowered it to
    64. klpE expression increased MIC to 1024. These genetic susceptibility data support
    uptake/export-related interpretations; they are not direct transporter binding
    measurements or transferable clinical resistance thresholds.
  snapshot_sha256: 1e7b7b83fb12de6674f45125a07e72532507fb1054efb4d33e62a72f7f95b610
- evidence_id: primary-mechanism
  kind: primary_source
  reference: PMID:28846667
  locator: Full mechanism Results/Methods, Figures 2–4 captions and actual Figure
    3 inspected
  accessed_at: '2026-10-21T18:58:39.254013Z'
  support: supports
  summary: E. coli reporter, S30 luciferase IC50 .34±.04 µM, chemical footprinting
    and osmC toeprinting establish translation elongation inhibition. The2.7 Å T.
    thermophilus70S structure places KLB in the 50S nascent-peptide exit tunnel, overlapping
    macrolide/streptogramin sites. The PTC remains compatible with A/P-site substrates;
    the mechanism is obstruction of nascent-peptide passage, not competitive exclusion
    of aminoacyl-tRNA. hns translation is partly resistant, so sequence context matters.
    Native core mechanism is supported; its peptide-access phrase could be made more
    precise.
  snapshot_sha256: 1e7b7b83fb12de6674f45125a07e72532507fb1054efb4d33e62a72f7f95b610
- evidence_id: primary-figure3
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c03c/5701663/730c6140cd7f/nihms894386f3.jpg
  locator: Actual Figure 3 panelsa–g, full image viewed
  accessed_at: '2026-10-21T19:00:49.152218Z'
  support: supports
  summary: The density and complex views place the compound near 23S rRNA and label
    Pro4 among the resolved N-terminal residues. Only the first 19 residues are visible,
    so neither this image nor a truncated deposited ligand is a full replacement molecular
    graph. Binding taxon is T. thermophilus; susceptibility and engineered resistance
    experiments use distinct E. coli backgrounds.
  snapshot_sha256: de28ae9b77e071190127143f5df90488e3dcaedac3a3bb78448735c4e15bacbe
- evidence_id: primary-resistance
  kind: primary_source
  reference: PMID:28846667
  locator: Resistance selection and testing Methods plus Results
  accessed_at: '2026-10-21T18:58:39.254013Z'
  support: context_only
  summary: 'Selected E. coli SQ110DTC cells had a single rrn allele, tolC deletion
    and uptake overexpression; four sequenced resistant clones carried U2609A/G. Reconstructed
    single-rrn E. coli variants corroborated rRNA-dependent effects. The body and
    Methods contain inconsistent Table 2 cross-calls: the actual displayed Table 2
    is the KLB-derivative table, not an rRNA-mutant table. Do not invent a mutant
    table or generalize these engineered backgrounds to population resistance.'
  snapshot_sha256: 1e7b7b83fb12de6674f45125a07e72532507fb1054efb4d33e62a72f7f95b610
- evidence_id: derivative-boundary
  kind: primary_source
  reference: PMID:28846667
  locator: Actual Table 2 all rows and derivative discussion
  accessed_at: '2026-10-21T18:58:39.254013Z'
  support: context_only
  summary: S1A, Q2N, S3A, A14K and truncated/azole variants are distinct molecules.
    The intact KLB row has M9+glucose MG1655 MIC 16 µg/mL; truncated constructs can
    inhibit cell-free translation without whole-cell activity. Such results support
    structure/function hypotheses but are not quantitative observations on the exact
    native compound.
  snapshot_sha256: 1e7b7b83fb12de6674f45125a07e72532507fb1054efb4d33e62a72f7f95b610
- evidence_id: publisher-structure
  kind: primary_source
  reference: https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fnchembio.2462/MediaObjects/41589_2017_Article_BFnchembio2462_Fig1_HTML.jpg
  locator: Publisher final Figure 1b, actual full image and enlarged N-terminal region
    inspected
  accessed_at: '2026-10-21T19:03:02.891913Z'
  support: refutes
  summary: The final publisher structure explicitly labels Pro4 S and depicts the
    dashed C-alpha/carbonyl bond. Its other displayed alpha centres are S and the
    Thr19 beta centre is R, agreeing with the existing assigned native centres. The
    manuscript image differs at the proline depiction; the final figure and deposited
    model resolve the omitted native annotation.
  snapshot_sha256: 8253cb1ca20bd4274fb0410bb28a59fe1c6d10848254be6af3309cdaeab0700b
- evidence_id: manuscript-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c03c/5701663/0a2693b2e8ae/nihms894386f1.jpg
  locator: Actual manuscript Figure 1b and enlarged proline region
  accessed_at: '2026-10-21T19:00:49.150892Z'
  support: context_only
  summary: The manuscript graphic is not identical to the publisher final figure and
    lacks its explicit configuration labels; its proline bond rendering is unsuitable
    as the sole stereochemical authority. Both versions are retained transparently,
    and the final publisher figure is the decisive2D source for Pro4 S.
  snapshot_sha256: adb30237b486029236ed515ee497168aed6ce02f441c5f0030c9d797e2fb7145
- evidence_id: pdb-model
  kind: primary_source
  reference: https://models.rcsb.org/v1/5w4k/atoms?label_asym_id=ID&encoding=cif
  locator: Original-linked PDB 5W4K; entity 58, chain ID/auth A, PRO sequence3
  accessed_at: '2026-10-21T19:02:37.531979Z'
  support: supports
  summary: The source’s deposited model maps Ser1-Gln2 to monomer9VA and natural Pro4
    to standard PRO at polymer sequence 3. Actual CA/N/C/CB coordinates have the same
    local handedness as standard L-PRO S. This corroborates the final figure without
    claiming independent re-refinement or absolute stereochemical proof from raw diffraction.
    Only residues 1–19 are represented; BIRD formula is therefore not the full molecule
    formula.
  snapshot_sha256: a2dd5289c0b5d4e76d3da00d56b11532a196bf7abaacf203ca4aed8d03ca87b4
- evidence_id: pdb-components
  kind: authority
  reference: https://files.rcsb.org/ligands/view/PRO.cif
  locator: PRO CCD and PRD 002277 residue/link definitions
  accessed_at: '2026-10-21T19:02:37.533510Z'
  support: supports
  summary: Standard PRO is explicitly L-PEPTIDE LINKING with alpha-C S. PRD sequence/link
    records map SER2–PRO3–GLY4 onto natural Ser3–Pro4–Gly5. This is a mapped structural
    comparison, not a substitution of a macromolecular accession for exact chemical
    identity.
  snapshot_sha256: 08674e4d60bc40ad5702b8de6e5e4abb66c2bbb603832c021c31194f4b4e593c
- evidence_id: mapping
  kind: validation
  reference: /private/tmp/am-review-session/578-map.py
  locator: 019 RDKit2026.03.5 against058; complete graph and local-coordinate diagnostics
  accessed_at: '2026-10-21T19:05:59Z'
  support: supports
  summary: Four native/current-PubChem encodings agree. The missing centre is native
    SMILES atom 110, InChI atom 48, with N114, carbonylC108 and ringC111 neighbours.
    Setting only atom 110 to S gives full key RSVIJELKMXTPMI-GFJPOFEGSA-N, unchanged
    composition/charge and all 16 centres assigned. PDB scalar triple product 2.18196
    and CCD S reference 2.74624 have matching sign. Candidate is a diagnostic for
    curator review, not a native edit.
  snapshot_sha256: b0d8a7ed74da58b7c6208b8440bb1c8f9746558bc7b693f22d1774beb6771ed6
- evidence_id: biosynthesis2018
  kind: primary_source
  reference: PMID:29601195; DOI:10.1021/jacs.8b02277
  locator: Complete additional original abstract only
  accessed_at: '2026-10-21T18:58:39.254447Z'
  support: context_only
  summary: The in-vitro biosynthesis study identifies KlpD YcaO as the enzyme required
    for azole and amidine formation, with TldD/E processing. These are biosynthetic
    enzymes rather than antibiotic inhibition targets. This comparator was not an
    adopted lead and its full experimental data were not inspected.
  snapshot_sha256: 46165f08ee43c21c74e906e67f058505e127a44b3127a234e28f6c0beeb9ad6b
- evidence_id: synthesis2024
  kind: primary_source
  reference: PMID:38923770; DOI:10.1002/anie.202407952
  locator: Complete original scientific main and Table 1 via publisher web text
  accessed_at: '2026-10-21T19:05:59Z'
  support: context_only
  summary: Synthetic KLB compound 5 was purified separately from 11 analogues. In
    M9+glucose it had MIC 32 µg/mL against E. coli 5, .25 against B. cereus BC177/BC107,
    .25/.5 against V. cholerae V1978/V1853, and >128 against E. coli CL4 and K. pneumoniae
    Hvkp7/FJ8. The paper reports no activity in its LB panel. These distinct material/strain/media
    results do not erase the 2017 panel or imply universal Gram-negative restriction.
    Exact assay inoculum/incubation and raw spectra remain inaccessible in SI; streptamidine
    epimerization is not transferred to KLB.
- evidence_id: web-notes
  kind: validation
  reference: /private/tmp/am-review-session/578-web-reading-notes.json
  locator: Reviewer paraphrase notes for successful2024 web text
  accessed_at: '2026-10-21T19:05:59Z'
  support: context_only
  summary: The notes identify actual reading scope and exact source URL; their hash
    is not a downloaded publisher PDF hash. Original PDF, SI and figure fetch failures
    remain in manifests. The 2024 structure drawing itself was not viewed and supplies
    no decisive Pro4 assignment here.
  snapshot_sha256: 3d5989e5db084de3dd22882d9db885cdd93410cf42b84227b9dc2e46afc81581
- evidence_id: access
  kind: validation
  reference: /private/tmp/am-review-session/578-fetch4.json
  locator: Public free retrieval boundaries across fetch1–9
  accessed_at: '2026-10-21T19:05:59Z'
  support: context_only
  summary: 2017 main XML and actual manuscript/publisher figures were obtained. PMC
    SI routes returned HTML, CDN routes404, static host DNS failure, and EPMC supplementary
    ZIP contained only an empty image entry.2024 Wiley/CityU/ResearchGate PDF, SI
    and figure routes returned403; publisher web text remained readable. No paywall
    purchase or contact occurred.
  snapshot_sha256: 88f3c93a93e8bba36ced2de9200a623b659152c2be4d27a352e95917c49a7678
assessments:
- assessment_id: identity
  area: identity
  topic: Complete molecular annotation and exact compound boundary
  outcome: concern
  summary: Connectivity, composition, masses, charge, assigned stereocentres and minted
    ARO identity are coherent. Pro4 is the sole unknown tetrahedron in native and
    current PubChem, but the publisher final primary figure explicitly assigns S and
    the deposited model agrees. This is an inherited omission of known stereochemistry,
    not evidence of a racemate or an asserted opposite enantiomer.
  target_ids:
  - antibioticmech:aro-2b2f71621c
  evidence_ids:
  - native
  - pubchem-current
  - publisher-structure
  - pdb-model
  - mapping
- assessment_id: grounding
  area: grounding
  topic: RiPP parent/class and current source groundings
  outcome: supported
  summary: ARO class membership is broader and supported by heterologous expression
    of a ribosomal precursor/maturation cluster. Current PubChem matches the stored
    partial graph. A future fully specified repair must reassess exact-PubChem equivalence
    instead of silently keeping an unresolved stereo record as identical; PDB/BIRD
    is contextual structural evidence only.
  target_ids:
  - antibioticmech:aro-2b2f71621c
  evidence_ids:
  - aro-current
  - primary-discovery
  - pubchem-current
  - pdb-components
  - mapping
- assessment_id: evidence
  area: evidence
  topic: Native definition and antibacterial eligibility
  outcome: supported
  summary: The sole adopted original was read in full, including Methods and Tables
    1–2, and directly supports antibacterial activity and ribosomal exit-tunnel inhibition.
    Producer-genome, assay-host and structural-host identities remain distinct. The
    later synthetic panel broadens conditional activity without refuting the original
    strain-specific observations. Native peptide-access wording is imprecise but does
    not explicitly assert a different binding site.
  target_ids:
  - antibioticmech:aro-2b2f71621c
  evidence_ids:
  - primary-discovery
  - primary-activity
  - primary-mechanism
  - primary-figure3
  - synthesis2024
- assessment_id: completeness
  area: completeness
  topic: Optional mechanistic, producer and activity enrichment
  outcome: unknown
  summary: Native has no required populated target/resistance/activity slot to repair
    beyond the known structural omission. The original supports bounded future annotations
    for exit-tunnel rRNA, engineered mutations and strain-specific MICs, but no generic
    protein target, universal clinical spectrum or transport-binding conclusion. Inaccessible
    supplementary and2024 figure details remain explicit.
  target_ids:
  - antibioticmech:aro-2b2f71621c
  evidence_ids:
  - adapter
  - adapter-summary
  - primary-transport
  - primary-resistance
  - derivative-boundary
  - biosynthesis2018
  - access
- assessment_id: provenance
  area: provenance
  topic: Actual owners and historical state
  outcome: supported
  summary: Original 13 and expanded 26 captured inputs remain unchanged. Complete
    ARO and PubChem owner rows explain native generation and all three seed/reseed
    events. Corrections belong in maintained source/enrichment handling; no generated
    YAML, history or curation status was altered.
  target_ids:
  - antibioticmech:aro-2b2f71621c
  evidence_ids:
  - owners
  - pubchem-owner
  - local-search
  - native
findings:
- finding_id: F1
  issue_key: klebsazolicin-pro4-known-stereo-omitted
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The graph omits the established Pro4 S configuration
  description: Native SMILES atom 110 and InChI atom 48 are unspecified, matching
    current adopted PubChem. The final publisher Figure 1b explicitly labels this
    natural proline S, and the linked 5W4K model maps it to L-PRO with matching local
    coordinates. The molecular annotation is materially incomplete despite internal
    validation passing. The scratch one-atom S candidate changes only this stereo
    tag and yields RSVIJELKMXTPMI-GFJPOFEGSA-N; it is not an automatic record replacement.
  target_ids:
  - antibioticmech:aro-2b2f71621c
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  evidence_ids:
  - native
  - pubchem-owner
  - pubchem-current
  - publisher-structure
  - pdb-model
  - mapping
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual PubChem structure/composition accession mapping owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained PubChem enrichment transform
  rule_id: 'review-yaml-record: exact identity and known stereochemical completeness'
  normalization_reason: 'Major known-stereochemistry omission: stored graph does not
    assert the opposite stereoisomer, so this is not normalized to a wrong-enantiomer
    blocker.'
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-2b2f71621c
  description: Adjudicate and encode the primary-supported Pro4 S annotation through
    maintained structure ownership, then reconcile dependent exact groundings.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual PubChem structure/composition accession mapping owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained PubChem enrichment transform
  generator: scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py
  acceptance_checks:
  - Use the publisher final Figure 1b and mapped deposited PRO3/Pro4 evidence; preserve
    the manuscript-versus-final graphical difference and the limits of the truncated
    PDB model.
  - Introduce a reproducible source/curator structure correction for Pro4 S; retain
    all other centres, full 23-residue connectivity, formula and neutral molecular
    form. Regenerate matching SMILES/InChI/key together.
  - Do not infer a racemate from the old unknown centre. Recheck PubChem 146684557
    against the repaired fully specified graph and qualify or resolve exact equivalence
    if it still omits Pro4; do not replace the molecule with BIRD’s truncated formula.
  - Rerun focused/schema/strict and required shared corpus gates after a future source-owned
    correction.
- action_id: A2
  finding_ids: []
  target_ids:
  - antibioticmech:aro-2b2f71621c
  description: Optional evidence enrichment should state nascent-peptide exit-tunnel
    obstruction and preserve exact experimental scope.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/klebsazolicin.yaml
    role: Future evidence-backed annotations through validated curation
  acceptance_checks:
  - Keep K. pneumoniae genome donor, E. coli heterologous producer/assay backgrounds
    and T. thermophilus ribosome structural host distinct.
  - Store single-agent MICs with exact media, strains, inoculum, duration and censoring;
    keep2017 and 2024 material/panel differences and analogues separate.
  - Treat uptake/self-resistance phenotypes and engineered 23S rRNA mutations at their
    actual evidence level, not as direct transporter binding or population susceptibility.
    Missing optional slots alone are not validation failures.
limitations:
- The sole adopted 2017 original scientific main, Methods and Tables 1–2 were fully
  read. Actual manuscript Figure 1, publisher final Figure 1 and Figure 3 were viewed;
  other plots and original SI were not independently inspected. Failed SI routes and
  empty EPMC ZIP are retained.
- The 2024 additional original main/Table 1 was read through publisher web text, but
  its actual figures, SI, spectra, precise bioassay setup and complete synthetic salt
  characterization were inaccessible. Its quantitative results are comparison evidence
  with those limits. The 2018 biosynthetic comparator remains abstract-level.
- PDB 5W4K is the original-linked refined model, not independently re-refined diffraction
  evidence; only the resolved N-terminal 19 residues are represented. Standard PRO
  mapping and local coordinates corroborate the explicit final 2D figure without supplying
  a whole-molecule replacement.
- Current PubChem is internally consistent with native but shares the unknown Pro4
  annotation. ARO’s official OBO was checked; a guessed numeric CARD webpage was not
  validated as this term and is not used.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All original 13 and expanded 26 input hashes were checked unchanged at draft writing.
  No native/source/history/progress/saved-bundle/Git writes occurred.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
