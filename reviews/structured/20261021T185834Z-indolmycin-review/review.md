# Indolmycin: exact antibacterial identity supported, with an invalid native indole SMILES

- Review: 20261021T185834Z-indolmycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:21:47Z
- Finished UTC: 2026-10-21T18:58:34Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Independent primary synthesis, antibacterial experiments and a ligand-bound TrpRS structure support the intended neutral (5S,1R) indolmycin identity. The native and current ChEBI SMILES omit the pyrrolic hydrogen and do not parse, although the independently valid InChI, formula and stereochemistry agree with the inspected evidence. This invalid principal representation is a blocker. The remaining exact references have explicit authority-access limits; missing optional mechanism and assay objects are not treated as defects.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 552; one entire exact record. All thirteen original input hashes were verified and preserved. Actual ownership is confined to the captured ChEBI raw inventory, source configuration, extractor and seeder.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:79394 | data/antibiotics/antibacterial/indolmycin.yaml | generated | indolmycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | CHEBI:79394 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:79394 | Actual focused execution exited 0. |
| Focused chemistry verification | failed | False | CHEBI:79394 | Actual focused execution exited 1. |
| Structured source grounding before mechanism follow-up | passed | False | CHEBI:79394 | Actual structured query completed. The returned gene annotation is contextual and is not evidence of indolmycin binding or exposure. |
| Structured source grounding before mechanism follow-up | passed | False | CHEBI:79394 | Actual structured query completed. The returned gene annotation is contextual and is not evidence of indolmycin binding or exposure. |
| Independent exact-structure and systematic-name comparison | passed | False | CHEBI:79394 | Diagnostic execution succeeded. Native/current ChEBI SMILES are invalid; the valid InChI, scratch-only indole repair, exact systematic synonym, KNApSAcK encodings, PubChem tautomer and both stereochemical CCD 5BX SMILES reproduce the same full Standard InChI/key. |
| Authoritative full QC | failed | True | CHEBI:79394 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:79394 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:79394 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:79394 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:79394 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:79394 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:79394 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:79394 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:79394 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral structure and stereochemistry

identity: supported. Targets: CHEBI:79394.

Primary synthesis, exact experimental identity and independent name/authority parses support the intended (5S,1R) neutral parent. The principal SMILES serialization is invalid and requires a source-owned correction; the valid InChI must not be inverted or replaced with a salt or racemate.

### Names, parents and exact references

grounding: unknown. Targets: CHEBI:79394.

All seven names and three structural parents are compatible with inspected authority/primary evidence. CAS is indirectly corroborated; KNApSAcK structural strings agree despite its unreproduced displayed key. MetaCyc and Reaxys were not independently resolved at graph depth. The patent is appropriately a document reference.

### Antibacterial class and antimicrobial roles

evidence: supported. Targets: CHEBI:79394.

Exact TAK-083 identity and original bacterial growth-inhibition measurements support both roles. The study-specific selectivity, methods and gerbil-model scope are retained. The record does not assert approval, universal susceptibility, fungal activity or a human clinical indication.

### Optional target and resistance enrichment

evidence: supported. Targets: CHEBI:79394.

Primary competitive enzyme kinetics and a directly bound exact ligand establish a defensible TrpRS mechanism for optional curation. The native has no target or resistance assertion to correct. Abstract-level H43N association, host-response context, biosynthetic genes and generic structured annotations remain separate evidence classes.

### Actual source ownership, source concept and history

provenance: supported. Targets: CHEBI:79394.

The exact raw row, source configuration and extraction/seeding branches explain all populated native fields and four history entries. Source concept minting independently reproduces antibioticmech:chebi-e1ab3782d6. Thirteen initial input hashes were preserved; no additional adopted source owner was identified.

### Whole-record coverage and all adopted leads

completeness: unknown. Targets: CHEBI:79394.

Every populated native field was assessed and all nine adopted citations dispositioned: one full synthesis article, one selected host-context main/figure, five complete original abstracts and two metadata-only discovery leads. Exact-reference access and historical full-text limits remain explicit. Optional target, MIC, producer and graph gaps are not defects by themselves.

## Findings

### F1: Repair the non-parsing indole SMILES while preserving the supported identity

blocker / open / confirmed; issue key: indolmycin-invalid-indole-smiles.

The native SMILES contains c2cnc3ccccc23, omitting the pyrrolic [nH], and fails RDKit kekulization. Current ChEBI reproduces the same invalid serialization. A scratch-only [nH] repair produces exactly the independently valid native InChI/key and primary-supported (5S,1R) identity. Correct the maintained source representation or a scoped source override and regenerate; do not replace the parent with a tautomer-specific name, salt or stereoisomer.

## Recommended Actions And Acceptance Checks

### A1

Correct the inherited indole serialization reproducibly and retain the exact identity.

- The regenerated SMILES parses and reproduces GNTVWGDQPXCYBV-PELKAZGASA-N, C14H15N3O2, neutral charge and both primary-supported stereocentres.
- Preserve the independent InChI, naming, source attribution and material boundaries; apply the fix in maintained normalization or a scoped override rather than directly patching generated YAML.
- Run focused schema, strict, chemistry and source-reproduction gates after future curation.

### A2

Preserve precise evidence and authority boundaries in optional scientific enrichment.

- If adding a target, distinguish the purified BsTrpRS competitive Ki and 5DK4 ligand-bound structure from species-specific enzyme-system IC50, bacterial MIC, host modeling and biosynthetic genes.
- If adding activity or resistance, retain exact material, organism/strain, methods and endpoint; do not infer clinical approval from gerbil efficacy or reconstruct uninspected H43N experiments from the abstract alone.
- Resolve MetaCyc/Reaxys through legitimate accessible authority evidence before certifying exact equivalence. Preserve the KNApSAcK displayed-key inconsistency without asserting a structural mismatch where both inspected graphs agree.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/indolmycin.yaml; Entire native record: identifier, label, status, definition, seven synonyms, three parents, two roles, all chemistry, four exact xrefs, patent document xref, source concept and four history events. | supports | The SEEDED/EXACT record represents neutral indolmycin, CHEBI:79394, C14H15N3O2, charge zero and GNTVWGDQPXCYBV-PELKAZGASA-N. The definition is structural. No clinical status, producer, molecular target, mode of action, resistance, MIC, causal graph or dataset object is populated. Neither the generic antimicrobial role nor this absence asserts activity against every microbial kingdom or an approved clinical use. |
| owners | data/raw/chebi_antimicrobials.tsv:2038; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Entire exact raw row; extraction and seeding branches for structure, naming, role selection, references and provenance; hidden/ignored-inclusive owner search. | supports | ChEBI is the sole adopted source row. Its nine citations were all dispositioned separately; they are retained as discovery leads, not silently promoted to claim-level evidence. The configured antimicrobial roles explain class/role placement, while no mapped mechanism role is present in the raw row. The patent is correctly emitted under document_xrefs. Exact searches found no ARO, target/resistance, FDA, BindingDB, MIBiG, fallback PubChem or curator override row. The thirteen original captured inputs remain unchanged. |
| chebi | CHEBI:79394; https://www.ebi.ac.uk/chebi/backend/api/public/compound/79394/; Complete official compound JSON, including all names, chemical properties, default structure, relations, origins and references. | supports | Current ChEBI reproduces the native non-parsing indole SMILES, valid InChI/key, exact names, parents, roles, CAS, KNApSAcK, MetaCyc, Reaxys and patent references. It distinguishes the neutral entity from conjugate acid CHEBI:91179. Current additional bacterial-metabolite and TrpRS-inhibitor roles are independent context rather than evidence that missing optional native fields are erroneous. |
| classes | CHEBI:24828; CHEBI:46812; CHEBI:50995; CHEBI:33281; CHEBI:33282; Official term JSON files for indoles, 1,3-oxazoles, secondary amino compound and both activity roles. | supports | The valid graph has an indole ring, an oxazolone belonging to the stated 1,3-oxazole class, and an exocyclic secondary methylamino group. The official antibacterial-role definition permits growth inhibition. The broader antimicrobial role is compatible with demonstrated bacterial activity and does not require separate fungal or viral experiments. |
| chemistry | 552-authority-chemistry.json; native/current ChEBI; OPSIN exact native systematic synonym; PubChem CID135417159; CCD5BX; Independent RDKit parsing, formula/mass/charge/stereochemistry and full Standard InChI comparison. | supports | Native/current ChEBI SMILES fail kekulization because c2cnc3 omits the pyrrolic [nH]. A scratch-only replacement with c2c[nH]c3 parses and reproduces the native full InChI/key, two centres (side chain R, oxazolone S), C14H15N3O2 and neutral charge. OPSIN independently parses the exact systematic synonym to the same graph. PubChem uses a different mobile-hydrogen tautomer but gives the same full Standard InChI; this is not an opposite stereoisomer. Both stereochemical CCD 5BX SMILES agree. Calculated average mass 257.293 and exact mass 257.11642672 agree with the stored precision. |
| xref-knapsack | knapsack:C00026624; http://www.knapsackfamily.com/knapsack_core/information.php?word=C00026624; Entire official entry, including names, CAS, formula and both displayed structural strings. | supports | The displayed Standard InChI and SMILES independently reproduce the native valid identity. The page also displays GNTVWGDQPXCYBV-YBJWJCFPNA-N, which does not reproduce either displayed string under the current parser. This external key inconsistency is retained as an authority limitation; the two exact structural encodings agree, so it does not establish a different-compound xref or justify replacing the native identity. Listed biosynthetic starting materials are predictions and listed organisms are not native producer assertions. |
| xref-limits | cas:21200-24-8; metacyc.compound:CPD0-920; reaxys:620840; 552-fetch-results.json and 552-fetch3-results.json; CAS public API attempt, independent PubChem CAS lookup, exact public MetaCyc page/XML routes, and adopted/current ChEBI registry mapping. | partial | The CAS API returned 401. PubChem lookup by the exact CAS and the current ChEBI/KNApSAcK association corroborate the intended parent identity, but do not replace a directly read CAS registry record. MetaCyc page and public XML routes both returned account-required HTML, not an inspected compound graph. The licensed Reaxys entry was not inspected. Their exact equivalence remains bounded rather than certified or declared wrong. |
| patent | patent:GB862685; https://patents.google.com/patent/GB862685A/en; Public original patent abstract and metadata inspected; no complete scanned description or assay table obtained. | partial | The patent describes PA155A separately from PA155B and PA155X, its isolation from a Streptomyces albus culture, physicochemical features, negative rotation and antibacterial activity. It distinguishes free material and possible acid salts. The patent document association and PA155A aliases are supported at this abstract depth; quantitative activity, salt-specific potency and other co-produced antibiotics are not transferred. |
| synthesis2001 | PMID:11767081; DOI:10.1248/cpb.49.1604; Complete original five-page paper read; Charts 1/3 and parent experimental passage p 1607 visually inspected in 552-synthesis-1/2/4.png. | supports | Exact parent 1 is (5S)-5-[(1R)-1-(1H-indol-3-yl)ethyl]-2-methylamino-2-oxazolin-4-one. The final optically active synthesis gives 99.4% ee and reports rotation −212.5 (c 2, methanol), consistent with the cited −214. Formula and indole NH characterization agree with the valid native InChI. Preliminary racemic route experiments and separately drawn metabolites do not make the named exact parent a racemate. This paper establishes structure/synthesis; its antibacterial introduction is not a new susceptibility assay. |
| activity2001 | PMID:11502514; DOI:10.1128/AAC.45.9.2455-2459.2001; PMC90677; Complete main article, Methods, Results, Discussion, Tables 1–3 and captions read; original Figure 1 structure viewed. | supports | TAK-083 is explicitly identified as exact (5S,1R) indolmycin. Table 1 reports 54 H. pylori isolates with range ≤0.008–0.031 µg/mL, MIC50 0.016 and MIC90 0.031. Agar dilution used brucella agar plus 7% horse blood, approximately 10^6 CFU/mL suspension delivered in 5 µL, 37°C and four days of microaerobic incubation; endpoint was no visible growth. Table 2 separately gives S. aureus FDA 209P 2 µg/mL and E. coli NIHJ JC-2 32 µg/mL under its aerobic protocol. Trp-tRNA formation IC50 values were 12.2 nM for H. pylori and 9.25 nM for E. coli enzyme systems versus 4.04 mM for bovine liver. These are assay inhibition values, not binding Kd. Oral dosing cleared infection in the tested gerbil model; the paper proposes further clinical work and does not establish human approval. |
| trprs2016 | PMID:26555258; DOI:10.1074/jbc.M115.690321; PMC4697160; Complete main Methods, Results, Discussion, tables and captions read; original Figures 1/2 viewed. Published online 2015, journal volume 2016. | supports | Purified Bacillus stearothermophilus TrpRS competitive PPi–ATP exchange kinetics give Ki 2.0×10^-9 M (reported error 5.2×10^-10 M), with MgATP in the assay. The 1.9 Å indolmycin–MgATP–TrpRS structure directly supports binding at the substrate site; His43 and Asp132 participate in recognition. Thermal shifts and the proposed magnesium-dependent stabilization are distinct endpoints from antibacterial MIC. Human cytosolic TrpRS comparison uses modeling and substrate-bound structures, not an experimental human indolmycin complex; it is not universal proof of absent mammalian off-target effects. |
| structure5DK4 | PDB:5DK4; CCD:5BX; https://data.rcsb.org/rest/v1/core/chemcomp/5BX; Official entry, all four nonpolymer entity assignments and complete CCD descriptor JSON. | supports | 5DK4 entity 5 is exact indolmycin component 5BX, alongside ATP, Mg and glycerol. Both canonical stereochemical descriptors and the full InChI match the native intended parent. The exact ligand-to-paper link is established; ATP-only comparator structures are not described as indolmycin-bound. This is an independent authority/experimental-material bridge, not a new native xref. |
| staph2004 | PMID:15243028; DOI:10.1093/jac/dkh352; Complete indexed original abstract; correct publisher page403 and public archive candidate 404. | supports | The study reports bacteriostatic activity against MSSA, MRSA and VISA, including comparator-resistant strains. High-level selected resistance (MIC 128 mg/L) is associated with TrpS H43N and fitness loss; the locus for lower-level resistance remains unidentified. The abstract proposes topical development rather than approved treatment. Detailed isolate-by-isolate results and experimental causal reconstruction were not inspected, so no new strain-resolved resistance object or stronger mechanistic claim is asserted. |
| early-adopted | PMID:14421508; PMID:14436229; PMID:5095271; PMID:582120; PMID:786633; PMID:809439; Two 1960 leads at title/metadata depth; 1971 author-linked original abstract; complete indexed abstracts for 1979, 1976 and 1975. | partial | The two 1960 discovery reports lack retrieved abstracts/full text. The 1971 biosynthesis abstract describes S. griseus precursor incorporation and chemical correlation of absolute configuration. The 1976 enzyme abstract supports competitive inhibition of E. coli Trp-tRNA ligase with little effect in its rat-liver comparison. The 1979 rat-liver study reports additional host tryptophan-metabolism effects; derivative results are not transferred to the parent. The 1975 biosynthesis abstract reports a crude-extract methyltransferase feedback effect lost after purification, which does not establish that enzyme as the direct antibacterial target. |
| host2012 | PMID:22500807; DOI:10.1016/j.cell.2012.02.050; PMC3613046; Complete abstract, selected toxin Methods/Results and original Figure 2A–C inspected; main not exhaustively read and supplement retrieval returned challenge HTML. | context_only | Figure 2A lists indolmycin among tRNA-synthetase toxins as general biological context. Panels 2B/C demonstrate C. elegans avoidance for other named compounds and do not supply an exact indolmycin antibacterial assay. This adopted lead is neither a bacterial MIC experiment nor evidence that every listed compound caused the measured host response. The figure-only name was explicitly checked rather than relying on a negative plain-text search. |
| biosynthetic-context | PMID:25730866; PMC4352800; PMID:34659732; DOI:10.1039/d1sc90180j; 2015 biosynthesis abstract and selected main Results/Discussion; complete 2021 correction text. | context_only | The 2015 work uses gene inactivation and enzyme reconstruction to study indolmycin production; Ind3/Ind6 biosynthetic functions are not antibacterial targets. The 2021 correction explicitly changes the engineered gene description from tryptophanyl-tRNA synthetase to tryptophan synthase. That engineering paper’s corrected trpS terminology must not be promoted into a drug-target assertion. No full2021 main or supplementary dataset was inspected. |
| adapter | 552-adapter.json; iModulonDB datasets and E. coli precise1k trpS query; Actual structured adapter execution before mechanism follow-up. | context_only | The catalog returned 28 datasets; the query identified E. coli b3384/trpS as tryptophan–tRNA ligase and no module hit. This is gene annotation context, not binding, drug exposure or a mechanistic causal result. Primary purified-enzyme and structural evidence supplies the relevant drug-specific support. |
| search | 552-local-hits.txt;552-owner-hits.txt;552-literature.json;552-fetch-results.json through552-fetch5-results.json; Hidden/ignored-inclusive native, maintained-source and research-cache searches; exact names, identifier and all nine adopted citations; bounded primary follow-up. | context_only | Historical research ledgers were treated only as leads and explicitly remain unreviewed rather than independent biological evidence. Retrieved primary synthesis/activity/TrpRS studies were assessed at the depths stated above. Derivatives, racemic route experiments, host effects, biosynthetic proteins and hypothetical clinical uses were not transferred to the exact native entity. The search is bounded and does not establish universal literature absence. |

## Limits And Additional Notes

- The original 2001 synthesis paper and 2001 antibacterial main article were read in full, with the synthesis Charts 1/3, parent experimental passage and antibacterial Figure 1 visually inspected. Raw spectra and crystallographic data were not independently reprocessed.
- The 2015-online/2016-volume TrpRS main article was read in full, including Methods, tables and captions, and Figures 1/2 were visually inspected. The human cytosolic comparison is modeled; no universal absence of host effects is inferred.
- Among the nine adopted leads, the 1960 discovery papers remain title/metadata-only. The 1971 biosynthesis abstract was recovered from the authors’ institutional publication page; the 1975,1976,1979 and 2004 papers were read at complete abstract depth. The correct 2004 publisher page returned 403 and the public archive candidate 404. An earlier guessed 2004 URL was not the correct paper and was not used as evidence.
- The 2012 host-response paper was read selectively, including actual Figure 2A where indolmycin is listed in contextual toxin examples. Its supplementary PDF route returned challenge HTML, not a PDF. Neither those contextual names nor the measured effects of other drugs are exact-parent bacterial assays.
- The MetaCyc exact compound and XML routes returned account-required HTML; CAS public API returned 401; licensed Reaxys was not inspected. These limits prevent unqualified exact-reference sign-off. PubChem CAS lookup is indirect corroboration, not a primary registry inspection.
- KNApSAcK displays an unreproduced key despite two structural strings that match the intended parent. PubChem’s mobile-hydrogen tautomer shares the full Standard InChI. These representation limits do not warrant a different-identity finding.
- The native chemistry check actually exited 1 for invalid SMILES; schema and strict checks passed. Successful independent diagnostics identify the defect and do not erase the failed native chemistry result.
- The 2021 biosynthesis main retrieval returned a browser challenge; only its complete published correction and the 2015 biosynthesis abstract/selected main sections were used as contextual leads. The structured adapter returned annotations, not an indolmycin-specific experiment.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Public retrieval manifests retain actual URLs, UTC timestamps, response statuses and content hashes. Preserved original inputs were verified before assessment. Independent PubChem, OPSIN and PDB checks are corroboration rather than a claim that those resources seeded the native record.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T185834Z-indolmycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Indolmycin: exact antibacterial identity supported, with an invalid native
  indole SMILES'
started_at: '2026-10-21T18:21:47Z'
finished_at: '2026-10-21T18:58:34Z'
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
summary: Independent primary synthesis, antibacterial experiments and a ligand-bound
  TrpRS structure support the intended neutral (5S,1R) indolmycin identity. The native
  and current ChEBI SMILES omit the pyrrolic hydrogen and do not parse, although the
  independently valid InChI, formula and stereochemistry agree with the inspected
  evidence. This invalid principal representation is a blocker. The remaining exact
  references have explicit authority-access limits; missing optional mechanism and
  assay objects are not treated as defects.
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
  - path: data/antibiotics/antibacterial/indolmycin.yaml
    sha256: b21cd5ea1e7bc945d5b5f9a4b815c8485598e9d38399484e9bd0cfbfc3a4747b
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
- target_id: CHEBI:79394
  path: data/antibiotics/antibacterial/indolmycin.yaml
  label: indolmycin
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
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 552; one entire exact record. All thirteen original input
    hashes were verified and preserved. Actual ownership is confined to the captured
    ChEBI raw inventory, source configuration, extractor and seeder.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:79394
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:79394
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/indolmycin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:79394
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/indolmycin.yaml --out /private/tmp/am-review-session/552-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: failed
  required: false
  summary: Actual focused execution exited 1.
  target_ids:
  - CHEBI:79394
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 552
  exit_code: 1
  expected_exit_code: 0
- check_id: adapter-catalog
  name: Structured source grounding before mechanism follow-up
  status: passed
  required: false
  summary: Actual structured query completed. The returned gene annotation is contextual
    and is not evidence of indolmycin binding or exposure.
  target_ids:
  - CHEBI:79394
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-trpS
  name: Structured source grounding before mechanism follow-up
  status: passed
  required: false
  summary: Actual structured query completed. The returned gene annotation is contextual
    and is not evidence of indolmycin binding or exposure.
  target_ids:
  - CHEBI:79394
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query trpS
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-comparison
  name: Independent exact-structure and systematic-name comparison
  status: passed
  required: false
  summary: Diagnostic execution succeeded. Native/current ChEBI SMILES are invalid;
    the valid InChI, scratch-only indole repair, exact systematic synonym, KNApSAcK
    encodings, PubChem tautomer and both stereochemical CCD 5BX SMILES reproduce the
    same full Standard InChI/key.
  target_ids:
  - CHEBI:79394
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/552-compare.py
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
  - CHEBI:79394
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
  - CHEBI:79394
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
  - CHEBI:79394
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
  - CHEBI:79394
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
  - CHEBI:79394
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
  - CHEBI:79394
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
  - CHEBI:79394
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
  - CHEBI:79394
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
  - CHEBI:79394
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/indolmycin.yaml
  locator: 'Entire native record: identifier, label, status, definition, seven synonyms,
    three parents, two roles, all chemistry, four exact xrefs, patent document xref,
    source concept and four history events.'
  accessed_at: '2026-10-21T18:57:59Z'
  support: supports
  summary: The SEEDED/EXACT record represents neutral indolmycin, CHEBI:79394, C14H15N3O2,
    charge zero and GNTVWGDQPXCYBV-PELKAZGASA-N. The definition is structural. No
    clinical status, producer, molecular target, mode of action, resistance, MIC,
    causal graph or dataset object is populated. Neither the generic antimicrobial
    role nor this absence asserts activity against every microbial kingdom or an approved
    clinical use.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv:2038; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Entire exact raw row; extraction and seeding branches for structure, naming,
    role selection, references and provenance; hidden/ignored-inclusive owner search.
  accessed_at: '2026-10-21T18:57:59Z'
  support: supports
  summary: ChEBI is the sole adopted source row. Its nine citations were all dispositioned
    separately; they are retained as discovery leads, not silently promoted to claim-level
    evidence. The configured antimicrobial roles explain class/role placement, while
    no mapped mechanism role is present in the raw row. The patent is correctly emitted
    under document_xrefs. Exact searches found no ARO, target/resistance, FDA, BindingDB,
    MIBiG, fallback PubChem or curator override row. The thirteen original captured
    inputs remain unchanged.
  snapshot_sha256: 4f3522b8afb6bdf0d79a8debc69af3dc9fb9a5c3adb35a1434e34378e201ab2b
- evidence_id: chebi
  kind: authority
  reference: CHEBI:79394; https://www.ebi.ac.uk/chebi/backend/api/public/compound/79394/
  locator: Complete official compound JSON, including all names, chemical properties,
    default structure, relations, origins and references.
  accessed_at: '2026-10-21T18:51:00Z'
  support: supports
  summary: Current ChEBI reproduces the native non-parsing indole SMILES, valid InChI/key,
    exact names, parents, roles, CAS, KNApSAcK, MetaCyc, Reaxys and patent references.
    It distinguishes the neutral entity from conjugate acid CHEBI:91179. Current additional
    bacterial-metabolite and TrpRS-inhibitor roles are independent context rather
    than evidence that missing optional native fields are erroneous.
  snapshot_sha256: 55acd7cc30627612a262384a58844d30d8415ca56684a9efddbd95a3a1097d70
- evidence_id: classes
  kind: authority
  reference: CHEBI:24828; CHEBI:46812; CHEBI:50995; CHEBI:33281; CHEBI:33282
  locator: Official term JSON files for indoles, 1,3-oxazoles, secondary amino compound
    and both activity roles.
  accessed_at: '2026-10-21T18:51:01Z'
  support: supports
  summary: The valid graph has an indole ring, an oxazolone belonging to the stated
    1,3-oxazole class, and an exocyclic secondary methylamino group. The official
    antibacterial-role definition permits growth inhibition. The broader antimicrobial
    role is compatible with demonstrated bacterial activity and does not require separate
    fungal or viral experiments.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: chemistry
  kind: authority
  reference: 552-authority-chemistry.json; native/current ChEBI; OPSIN exact native
    systematic synonym; PubChem CID135417159; CCD5BX
  locator: Independent RDKit parsing, formula/mass/charge/stereochemistry and full
    Standard InChI comparison.
  accessed_at: '2026-10-21T18:57:59Z'
  support: supports
  summary: Native/current ChEBI SMILES fail kekulization because c2cnc3 omits the
    pyrrolic [nH]. A scratch-only replacement with c2c[nH]c3 parses and reproduces
    the native full InChI/key, two centres (side chain R, oxazolone S), C14H15N3O2
    and neutral charge. OPSIN independently parses the exact systematic synonym to
    the same graph. PubChem uses a different mobile-hydrogen tautomer but gives the
    same full Standard InChI; this is not an opposite stereoisomer. Both stereochemical
    CCD 5BX SMILES agree. Calculated average mass 257.293 and exact mass 257.11642672
    agree with the stored precision.
  snapshot_sha256: c4d2f6424590375de6c75c5a3a51c54dc00ae9614767bc1c561de911a7fd563e
- evidence_id: xref-knapsack
  kind: authority
  reference: knapsack:C00026624; http://www.knapsackfamily.com/knapsack_core/information.php?word=C00026624
  locator: Entire official entry, including names, CAS, formula and both displayed
    structural strings.
  accessed_at: '2026-10-21T18:51:00Z'
  support: supports
  summary: The displayed Standard InChI and SMILES independently reproduce the native
    valid identity. The page also displays GNTVWGDQPXCYBV-YBJWJCFPNA-N, which does
    not reproduce either displayed string under the current parser. This external
    key inconsistency is retained as an authority limitation; the two exact structural
    encodings agree, so it does not establish a different-compound xref or justify
    replacing the native identity. Listed biosynthetic starting materials are predictions
    and listed organisms are not native producer assertions.
  snapshot_sha256: 111a8e486261ae92a82eb02b06585e0d4cd692ff13668cdae27867f5895ad597
- evidence_id: xref-limits
  kind: authority
  reference: cas:21200-24-8; metacyc.compound:CPD0-920; reaxys:620840; 552-fetch-results.json
    and 552-fetch3-results.json
  locator: CAS public API attempt, independent PubChem CAS lookup, exact public MetaCyc
    page/XML routes, and adopted/current ChEBI registry mapping.
  accessed_at: '2026-10-21T18:51:37Z'
  support: partial
  summary: The CAS API returned 401. PubChem lookup by the exact CAS and the current
    ChEBI/KNApSAcK association corroborate the intended parent identity, but do not
    replace a directly read CAS registry record. MetaCyc page and public XML routes
    both returned account-required HTML, not an inspected compound graph. The licensed
    Reaxys entry was not inspected. Their exact equivalence remains bounded rather
    than certified or declared wrong.
  snapshot_sha256: de22cc37de5e3b9a56c17e9d0c57e5a785fafedc656a37f2c03ecb7023e2be64
- evidence_id: patent
  kind: primary_source
  reference: patent:GB862685; https://patents.google.com/patent/GB862685A/en
  locator: Public original patent abstract and metadata inspected; no complete scanned
    description or assay table obtained.
  accessed_at: '2026-10-21T18:51:00Z'
  support: partial
  summary: The patent describes PA155A separately from PA155B and PA155X, its isolation
    from a Streptomyces albus culture, physicochemical features, negative rotation
    and antibacterial activity. It distinguishes free material and possible acid salts.
    The patent document association and PA155A aliases are supported at this abstract
    depth; quantitative activity, salt-specific potency and other co-produced antibiotics
    are not transferred.
  snapshot_sha256: 185dd8e523f5601ecd372ca9ccb458d870b7db5044db217603061da5b8cdb41a
- evidence_id: synthesis2001
  kind: primary_source
  reference: PMID:11767081; DOI:10.1248/cpb.49.1604
  locator: Complete original five-page paper read; Charts 1/3 and parent experimental
    passage p 1607 visually inspected in 552-synthesis-1/2/4.png.
  accessed_at: '2026-10-21T18:51:37Z'
  support: supports
  summary: Exact parent 1 is (5S)-5-[(1R)-1-(1H-indol-3-yl)ethyl]-2-methylamino-2-oxazolin-4-one.
    The final optically active synthesis gives 99.4% ee and reports rotation −212.5
    (c 2, methanol), consistent with the cited −214. Formula and indole NH characterization
    agree with the valid native InChI. Preliminary racemic route experiments and separately
    drawn metabolites do not make the named exact parent a racemate. This paper establishes
    structure/synthesis; its antibacterial introduction is not a new susceptibility
    assay.
  snapshot_sha256: 1ca65ebed38d95e5b265af9091b72f72c1adc28637c289e0e60caa87ea90ec76
- evidence_id: activity2001
  kind: primary_source
  reference: PMID:11502514; DOI:10.1128/AAC.45.9.2455-2459.2001; PMC90677
  locator: Complete main article, Methods, Results, Discussion, Tables 1–3 and captions
    read; original Figure 1 structure viewed.
  accessed_at: '2026-10-21T18:52:53Z'
  support: supports
  summary: TAK-083 is explicitly identified as exact (5S,1R) indolmycin. Table 1 reports
    54 H. pylori isolates with range ≤0.008–0.031 µg/mL, MIC50 0.016 and MIC90 0.031.
    Agar dilution used brucella agar plus 7% horse blood, approximately 10^6 CFU/mL
    suspension delivered in 5 µL, 37°C and four days of microaerobic incubation; endpoint
    was no visible growth. Table 2 separately gives S. aureus FDA 209P 2 µg/mL and
    E. coli NIHJ JC-2 32 µg/mL under its aerobic protocol. Trp-tRNA formation IC50
    values were 12.2 nM for H. pylori and 9.25 nM for E. coli enzyme systems versus
    4.04 mM for bovine liver. These are assay inhibition values, not binding Kd. Oral
    dosing cleared infection in the tested gerbil model; the paper proposes further
    clinical work and does not establish human approval.
  snapshot_sha256: 02be885c4ec4fcf6108f4abc6fefd3afd1e123c7e10af37371e5452aadad0aa4
- evidence_id: trprs2016
  kind: primary_source
  reference: PMID:26555258; DOI:10.1074/jbc.M115.690321; PMC4697160
  locator: Complete main Methods, Results, Discussion, tables and captions read; original
    Figures 1/2 viewed. Published online 2015, journal volume 2016.
  accessed_at: '2026-10-21T18:51:37Z'
  support: supports
  summary: Purified Bacillus stearothermophilus TrpRS competitive PPi–ATP exchange
    kinetics give Ki 2.0×10^-9 M (reported error 5.2×10^-10 M), with MgATP in the
    assay. The 1.9 Å indolmycin–MgATP–TrpRS structure directly supports binding at
    the substrate site; His43 and Asp132 participate in recognition. Thermal shifts
    and the proposed magnesium-dependent stabilization are distinct endpoints from
    antibacterial MIC. Human cytosolic TrpRS comparison uses modeling and substrate-bound
    structures, not an experimental human indolmycin complex; it is not universal
    proof of absent mammalian off-target effects.
  snapshot_sha256: 771a1705aee9356c9792b49db2048f2f8414f4153ae8067dde4ab075883a31dc
- evidence_id: structure5DK4
  kind: authority
  reference: PDB:5DK4; CCD:5BX; https://data.rcsb.org/rest/v1/core/chemcomp/5BX
  locator: Official entry, all four nonpolymer entity assignments and complete CCD
    descriptor JSON.
  accessed_at: '2026-10-21T18:55:37Z'
  support: supports
  summary: 5DK4 entity 5 is exact indolmycin component 5BX, alongside ATP, Mg and
    glycerol. Both canonical stereochemical descriptors and the full InChI match the
    native intended parent. The exact ligand-to-paper link is established; ATP-only
    comparator structures are not described as indolmycin-bound. This is an independent
    authority/experimental-material bridge, not a new native xref.
  snapshot_sha256: 2a40e5fa129018a05e86895bce9595e99542b3a917016c4cd861a2a83eb6b0fd
- evidence_id: staph2004
  kind: primary_source
  reference: PMID:15243028; DOI:10.1093/jac/dkh352
  locator: Complete indexed original abstract; correct publisher page403 and public
    archive candidate 404.
  accessed_at: '2026-10-21T18:51:01Z'
  support: supports
  summary: The study reports bacteriostatic activity against MSSA, MRSA and VISA,
    including comparator-resistant strains. High-level selected resistance (MIC 128
    mg/L) is associated with TrpS H43N and fitness loss; the locus for lower-level
    resistance remains unidentified. The abstract proposes topical development rather
    than approved treatment. Detailed isolate-by-isolate results and experimental
    causal reconstruction were not inspected, so no new strain-resolved resistance
    object or stronger mechanistic claim is asserted.
  snapshot_sha256: bfcd4b27eb2252631fb75b680c5367de7fbe696f7827f95f03ffb2d3fbd09318
- evidence_id: early-adopted
  kind: primary_source
  reference: PMID:14421508; PMID:14436229; PMID:5095271; PMID:582120; PMID:786633;
    PMID:809439
  locator: Two 1960 leads at title/metadata depth; 1971 author-linked original abstract;
    complete indexed abstracts for 1979, 1976 and 1975.
  accessed_at: '2026-10-21T18:52:53Z'
  support: partial
  summary: The two 1960 discovery reports lack retrieved abstracts/full text. The
    1971 biosynthesis abstract describes S. griseus precursor incorporation and chemical
    correlation of absolute configuration. The 1976 enzyme abstract supports competitive
    inhibition of E. coli Trp-tRNA ligase with little effect in its rat-liver comparison.
    The 1979 rat-liver study reports additional host tryptophan-metabolism effects;
    derivative results are not transferred to the parent. The 1975 biosynthesis abstract
    reports a crude-extract methyltransferase feedback effect lost after purification,
    which does not establish that enzyme as the direct antibacterial target.
  snapshot_sha256: 2a28cfe62cd5f67452b982f8ad70e7ccf9c60c06c3c1d06b36722e879fe4d6b0
- evidence_id: host2012
  kind: primary_source
  reference: PMID:22500807; DOI:10.1016/j.cell.2012.02.050; PMC3613046
  locator: Complete abstract, selected toxin Methods/Results and original Figure 2A–C
    inspected; main not exhaustively read and supplement retrieval returned challenge
    HTML.
  accessed_at: '2026-10-21T18:55:15Z'
  support: context_only
  summary: Figure 2A lists indolmycin among tRNA-synthetase toxins as general biological
    context. Panels 2B/C demonstrate C. elegans avoidance for other named compounds
    and do not supply an exact indolmycin antibacterial assay. This adopted lead is
    neither a bacterial MIC experiment nor evidence that every listed compound caused
    the measured host response. The figure-only name was explicitly checked rather
    than relying on a negative plain-text search.
  snapshot_sha256: e7628559f76c1c670460f5f0cc6e39d66e286328ccaf8cf3409dc10db4db506a
- evidence_id: biosynthetic-context
  kind: primary_source
  reference: PMID:25730866; PMC4352800; PMID:34659732; DOI:10.1039/d1sc90180j
  locator: 2015 biosynthesis abstract and selected main Results/Discussion; complete
    2021 correction text.
  accessed_at: '2026-10-21T18:51:37Z'
  support: context_only
  summary: The 2015 work uses gene inactivation and enzyme reconstruction to study
    indolmycin production; Ind3/Ind6 biosynthetic functions are not antibacterial
    targets. The 2021 correction explicitly changes the engineered gene description
    from tryptophanyl-tRNA synthetase to tryptophan synthase. That engineering paper’s
    corrected trpS terminology must not be promoted into a drug-target assertion.
    No full2021 main or supplementary dataset was inspected.
  snapshot_sha256: c27003dd1aa27f61e8d0299db0519d530fb80f21aa4a4fe187264c3a2a658b19
- evidence_id: adapter
  kind: database
  reference: 552-adapter.json; iModulonDB datasets and E. coli precise1k trpS query
  locator: Actual structured adapter execution before mechanism follow-up.
  accessed_at: '2026-10-21T18:57:59Z'
  support: context_only
  summary: The catalog returned 28 datasets; the query identified E. coli b3384/trpS
    as tryptophan–tRNA ligase and no module hit. This is gene annotation context,
    not binding, drug exposure or a mechanistic causal result. Primary purified-enzyme
    and structural evidence supplies the relevant drug-specific support.
  snapshot_sha256: 7628f8354c14f4fb51a0cba07fd7bb8981fa8d72aae67f24c1f3a5bca33684c9
- evidence_id: search
  kind: search
  reference: 552-local-hits.txt;552-owner-hits.txt;552-literature.json;552-fetch-results.json
    through552-fetch5-results.json
  locator: Hidden/ignored-inclusive native, maintained-source and research-cache searches;
    exact names, identifier and all nine adopted citations; bounded primary follow-up.
  accessed_at: '2026-10-21T18:51:02Z'
  support: context_only
  summary: Historical research ledgers were treated only as leads and explicitly remain
    unreviewed rather than independent biological evidence. Retrieved primary synthesis/activity/TrpRS
    studies were assessed at the depths stated above. Derivatives, racemic route experiments,
    host effects, biosynthetic proteins and hypothetical clinical uses were not transferred
    to the exact native entity. The search is bounded and does not establish universal
    literature absence.
  snapshot_sha256: 8cf39cbf81827faa5bf5053ce1e07002bd0922abe24bd20f8ab43f6b1ba4fcc5
  search_scope: 2026-10-21; repository and local cache searches included hidden and
    ignored files. Exact indolmycin/indolemycin/PA155A/TAK-083, CHEBI:79394, full
    key, all nine adopted PMIDs and bounded primary structure/activity/TrpRS follow-up.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral structure and stereochemistry
  outcome: supported
  summary: Primary synthesis, exact experimental identity and independent name/authority
    parses support the intended (5S,1R) neutral parent. The principal SMILES serialization
    is invalid and requires a source-owned correction; the valid InChI must not be
    inverted or replaced with a salt or racemate.
  target_ids:
  - CHEBI:79394
  evidence_ids:
  - chemistry
  - synthesis2001
  - activity2001
  - structure5DK4
- assessment_id: grounding
  area: grounding
  topic: Names, parents and exact references
  outcome: unknown
  summary: All seven names and three structural parents are compatible with inspected
    authority/primary evidence. CAS is indirectly corroborated; KNApSAcK structural
    strings agree despite its unreproduced displayed key. MetaCyc and Reaxys were
    not independently resolved at graph depth. The patent is appropriately a document
    reference.
  target_ids:
  - CHEBI:79394
  evidence_ids:
  - chebi
  - classes
  - xref-knapsack
  - xref-limits
  - patent
  - synthesis2001
- assessment_id: activity
  area: evidence
  topic: Antibacterial class and antimicrobial roles
  outcome: supported
  summary: Exact TAK-083 identity and original bacterial growth-inhibition measurements
    support both roles. The study-specific selectivity, methods and gerbil-model scope
    are retained. The record does not assert approval, universal susceptibility, fungal
    activity or a human clinical indication.
  target_ids:
  - CHEBI:79394
  evidence_ids:
  - activity2001
  - staph2004
  - classes
- assessment_id: mechanism
  area: evidence
  topic: Optional target and resistance enrichment
  outcome: supported
  summary: Primary competitive enzyme kinetics and a directly bound exact ligand establish
    a defensible TrpRS mechanism for optional curation. The native has no target or
    resistance assertion to correct. Abstract-level H43N association, host-response
    context, biosynthetic genes and generic structured annotations remain separate
    evidence classes.
  target_ids:
  - CHEBI:79394
  evidence_ids:
  - trprs2016
  - structure5DK4
  - staph2004
  - host2012
  - early-adopted
  - biosynthetic-context
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Actual source ownership, source concept and history
  outcome: supported
  summary: The exact raw row, source configuration and extraction/seeding branches
    explain all populated native fields and four history entries. Source concept minting
    independently reproduces antibioticmech:chebi-e1ab3782d6. Thirteen initial input
    hashes were preserved; no additional adopted source owner was identified.
  target_ids:
  - CHEBI:79394
  evidence_ids:
  - owners
  - native
  - chebi
- assessment_id: coverage
  area: completeness
  topic: Whole-record coverage and all adopted leads
  outcome: unknown
  summary: 'Every populated native field was assessed and all nine adopted citations
    dispositioned: one full synthesis article, one selected host-context main/figure,
    five complete original abstracts and two metadata-only discovery leads. Exact-reference
    access and historical full-text limits remain explicit. Optional target, MIC,
    producer and graph gaps are not defects by themselves.'
  target_ids:
  - CHEBI:79394
  evidence_ids:
  - early-adopted
  - staph2004
  - host2012
  - synthesis2001
  - search
  - xref-limits
findings:
- finding_id: F1
  issue_key: indolmycin-invalid-indole-smiles
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Repair the non-parsing indole SMILES while preserving the supported identity
  description: The native SMILES contains c2cnc3ccccc23, omitting the pyrrolic [nH],
    and fails RDKit kekulization. Current ChEBI reproduces the same invalid serialization.
    A scratch-only [nH] repair produces exactly the independently valid native InChI/key
    and primary-supported (5S,1R) identity. Correct the maintained source representation
    or a scoped source override and regenerate; do not replace the parent with a tautomer-specific
    name, salt or stereoisomer.
  target_ids:
  - CHEBI:79394
  field_paths:
  - chemical_structure.smiles
  evidence_ids:
  - native
  - chebi
  - chemistry
  - synthesis2001
  - structure5DK4
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Inherited chemical representation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated structure emission
  rule_id: 'Shared record-review severity rubric: invalid chemical representation'
  native_severity: blocker
  normalization_reason: The shared rubric classifies an invalid principal chemical
    representation as blocker. A valid InChI preserves the intended identity but does
    not cure a non-parsing SMILES; this finding does not assert that the native InChI
    denotes the wrong molecule.
actions:
- action_id: A1
  description: Correct the inherited indole serialization reproducibly and retain
    the exact identity.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:79394
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Inherited chemical representation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated structure emission
  acceptance_checks:
  - The regenerated SMILES parses and reproduces GNTVWGDQPXCYBV-PELKAZGASA-N, C14H15N3O2,
    neutral charge and both primary-supported stereocentres.
  - Preserve the independent InChI, naming, source attribution and material boundaries;
    apply the fix in maintained normalization or a scoped override rather than directly
    patching generated YAML.
  - Run focused schema, strict, chemistry and source-reproduction gates after future
    curation.
- action_id: A2
  description: Preserve precise evidence and authority boundaries in optional scientific
    enrichment.
  finding_ids: []
  target_ids:
  - CHEBI:79394
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/indolmycin.yaml
    role: Optional curator-owned scientific additions through the validated writer
  acceptance_checks:
  - If adding a target, distinguish the purified BsTrpRS competitive Ki and 5DK4 ligand-bound
    structure from species-specific enzyme-system IC50, bacterial MIC, host modeling
    and biosynthetic genes.
  - If adding activity or resistance, retain exact material, organism/strain, methods
    and endpoint; do not infer clinical approval from gerbil efficacy or reconstruct
    uninspected H43N experiments from the abstract alone.
  - Resolve MetaCyc/Reaxys through legitimate accessible authority evidence before
    certifying exact equivalence. Preserve the KNApSAcK displayed-key inconsistency
    without asserting a structural mismatch where both inspected graphs agree.
limitations:
- The original 2001 synthesis paper and 2001 antibacterial main article were read
  in full, with the synthesis Charts 1/3, parent experimental passage and antibacterial
  Figure 1 visually inspected. Raw spectra and crystallographic data were not independently
  reprocessed.
- The 2015-online/2016-volume TrpRS main article was read in full, including Methods,
  tables and captions, and Figures 1/2 were visually inspected. The human cytosolic
  comparison is modeled; no universal absence of host effects is inferred.
- Among the nine adopted leads, the 1960 discovery papers remain title/metadata-only.
  The 1971 biosynthesis abstract was recovered from the authors’ institutional publication
  page; the 1975,1976,1979 and 2004 papers were read at complete abstract depth. The
  correct 2004 publisher page returned 403 and the public archive candidate 404. An
  earlier guessed 2004 URL was not the correct paper and was not used as evidence.
- The 2012 host-response paper was read selectively, including actual Figure 2A where
  indolmycin is listed in contextual toxin examples. Its supplementary PDF route returned
  challenge HTML, not a PDF. Neither those contextual names nor the measured effects
  of other drugs are exact-parent bacterial assays.
- The MetaCyc exact compound and XML routes returned account-required HTML; CAS public
  API returned 401; licensed Reaxys was not inspected. These limits prevent unqualified
  exact-reference sign-off. PubChem CAS lookup is indirect corroboration, not a primary
  registry inspection.
- KNApSAcK displays an unreproduced key despite two structural strings that match
  the intended parent. PubChem’s mobile-hydrogen tautomer shares the full Standard
  InChI. These representation limits do not warrant a different-identity finding.
- The native chemistry check actually exited 1 for invalid SMILES; schema and strict
  checks passed. Successful independent diagnostics identify the defect and do not
  erase the failed native chemistry result.
- The 2021 biosynthesis main retrieval returned a browser challenge; only its complete
  published correction and the 2015 biosynthesis abstract/selected main sections were
  used as contextual leads. The structured adapter returned annotations, not an indolmycin-specific
  experiment.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Public retrieval manifests retain actual URLs, UTC timestamps, response statuses
  and content hashes. Preserved original inputs were verified before assessment. Independent
  PubChem, OPSIN and PDB checks are corroboration rather than a claim that those resources
  seeded the native record.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
