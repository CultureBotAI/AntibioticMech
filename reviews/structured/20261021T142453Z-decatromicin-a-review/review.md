# Decatromicin A: invalid pyrrole SMILES with supported natural-product evidence

- Review: 20261021T142453Z-decatromicin-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:02:30Z
- Finished UTC: 2026-10-21T14:24:53Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native SMILES lacks the pyrrole hydrogen and fails chemical parsing. Its retained InChI, natural-product structure and bounded antibacterial/producer claims are supported by the original isolation and structure studies. A scratch-only hydrogen correction reproduces the exact key. No native molecular target is asserted; newer activity and quorum-sensing observations require distinct endpoint annotations.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 346; one entire exact record. All 13 original inputs were preserved within 31 expanded inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65728 | data/antibiotics/antibacterial/decatromicin-a.yaml | generated | decatromicin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | failed | False | CHEBI:65728 | Actual focused execution exited 1. |
| Focused schema verification | passed | True | CHEBI:65728 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:65728 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:65728 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65728 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65728 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65728 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65728 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65728 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65728 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65728 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65728 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Natural-product graph and structural encoding

identity: concern. Targets: CHEBI:65728.

The original structure and thirteen assigned centres are coherent with the retained InChI. The invalid pyrrole SMILES is a confirmed repairable representation defect.

### Names, chemical authorities and exact groundings

grounding: supported. Targets: CHEBI:65728.

Official ChEBI reproduces the intended A InChI and source names; the sole Reaxys link remains authority-confirmed with independent-register limits. Additional PubChem name results are not native exact links.

### Antibacterial roles and historical definition

scope: supported. Targets: CHEBI:65728.

The original isolated A has direct strain-level antibacterial activity and a verified Actinomadura producer. The historical Gram-positive emphasis is panel-scoped, not a universal spectrum claim.

### Optional activity_spectrum

completeness: unknown. Targets: CHEBI:65728.

Exact original and newer strain-level measurements are available for optional enrichment, but units, agar versus OD90 microbroth endpoints, producer-derived materials and assay-specific MBC definitions must remain explicit. No present-day susceptibility breakpoint or clinical category is inferred.

### Optional mechanism and resistance assertions

evidence: unknown. Targets: CHEBI:65728.

No native molecular target or resistance entry is populated. Gelatinase suppression supports a bounded phenotype; it does not identify direct Fsr binding or explain antibacterial killing. Parent-family analogies and docking of other molecules are insufficient for target import.

### Definition producer and optional structured producer

provenance: supported. Targets: CHEBI:65728.

The original identifies MK73-NF4 and its deposit as the A/B producer. The 2022 A30804 experiment is a separate producer with 16S accession OP225395. Neither strain should be silently replaced by a named species merely from a phylogenetic neighbor.

### Clinical products, causal graph and datasets

scope: not_applicable. Targets: CHEBI:65728.

No clinical product, approval, causal graph or dataset assertion is present. Acute mouse toxicity and in vitro assays do not establish human therapeutic safety or efficacy.

### Source ownership, status and history

provenance: supported. Targets: CHEBI:65728.

Three generated seeding/reseeding events and SEEDED status are coherent. All original hashes are preserved, with source ownership recorded for reproducible correction.

### Focused validation

schema: concern. Targets: CHEBI:65728.

Native schema gates pass while chemical parsing fails. The independent original-source comparison supports the retained A configuration; parsing and key agreement alone do not establish scientific identity.

## Findings

### F1: Missing pyrrole hydrogen makes the native SMILES invalid

major / open / confirmed; issue key: decatromicin-a-invalid-pyrrole-smiles.

The pyrrole nitrogen is encoded as aromatic n rather than [nH]. Independent parsing fails kekulization, while correcting only that hydrogen in scratch gives precisely the stored InChI/key, formula and stereochemistry. Original drawings explicitly show the pyrrole NH. Repair the maintained source representation while preserving the supported A configuration.

## Recommended Actions And Acceptance Checks

### A1

Repair the maintained pyrrole SMILES and verify all exact chemical fields.

- Encode the pyrrole NH explicitly and ensure SMILES parses and agrees with the intended final InChI, formula, charge and thirteen stereocentres.
- Do not confuse this hydrogen correction with adjudication of sugar configuration.
- Make any authorized change through maintained source/curation ownership and pass native, chemistry, corpus, provenance and history gates.

### A2

Optionally enrich exact activity, producer and quorum-sensing phenotype context.

- Keep 1999 micrograms/mL agar-dilution MICs separate from 2022 micromolar MIC90/MBC90 values and their respective strains.
- Preserve P. aeruginosa A3=100 in the original table and avoid importing the later paper’s incorrect inherited 3.13 micromolar comparison.
- Keep anti-gelatinase phenotype separate from growth MIC, direct enzyme inhibition, docking and target binding.
- Retain MK73-NF4 and A30804 as distinct producer observations; do not infer clinical safety or optional-field invalidity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/decatromicin-a.yaml; Entire record, exact synonym, all chemical parents/roles, structure, source and three history events | supports | This SEEDED, EXACT record has one stereospecific synonym, ten structural parents and two antimicrobial roles. It has no molecular target, resistance entry, activity_spectrum, clinical product, causal graph, dataset or structured producer object. The producer and historical activity scope occur in the definition. The sole xref is Reaxys8469607. |
| owners | data/raw/chebi_antimicrobials.tsv; ChEBI row1285; extractor and seeder ownership | supports | All asserted scientific source fields, including the defective SMILES and exact synonym, reproduce the ChEBI row. The sole adopted citation is PMID10726925. Actual source/transform/context inputs were appended without changing the original 13 hashes. No exact ARO target/resistance or MIBiG producer row was present in the inspected exact-name/key source subsets. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity, exact stereochemistry, primary evidence and optional completeness | supports | A molecular representation must parse and preserve the exact natural-product structure. Exact synonym and assay material must agree. Optional target, producer and activity fields are not automatically required simply because enrichment is possible. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/65728/; CHEBI:65728, complete current structure, names, roles, parents, origin and citations | context_only | Current ChEBI retains the native invalid pyrrole SMILES and the same complete InChI. All native role and structural-parent identifiers resolve in the current authority. Agreement with the source confirms inheritance but does not resolve the independent primary structural comparison. |
| reaxys | https://www.ebi.ac.uk/chebi/backend/api/public/compound/65728/; Reaxys8469607 registry accession | context_only | The only native registry link is retained by official ChEBI. No independent paid Reaxys register was accessed, so that register was not used as independent stereochemical evidence. |
| chemistry | Independent batch019 RDKit against batch035 cwd; 346348-focused.py;346-chemistry.json | refutes | Native SMILES fails kekulization because its pyrrole N is encoded as aromatic n. Replacing only that token with [nH] in scratch reproduces the stored key YKLXDAWPGVZXKC-NMNDIUEASA-N, formula, neutral charge and thirteen assigned centres. The native InChI parses and its masses and source mint reproduce. The separately reviewed B epimer issue does not alter the supported A mapping. No native edit occurred. |
| stereo-map | Independent numbered sugar mapping and dechlorination comparison; 346348-map.py;346347-stereo-map.json | supports | In hydrogen-repaired native strings, sugar C1-prime/C2-prime/C3-prime/C4-prime are zero-based atoms41/42/43/45; C5-prime is55 in A and56 in B. A sugar centres are R,R,S,R at C1/C3/C4/C5; B is R,S,S,R. Flipping only B C3-prime gives OKYWSSBYCHUWKT-SHSCNYKZSA-N. Removing only its extra pyrrole5-double-prime chlorine then reproduces the entire A key exactly, including all remaining centres and double bonds. |
| isolation-primary | https://doi.org/10.7164/antibiotics.52.781; Adopted PMID:10726925; full original six-page paper, Methods and Results, Tables3-4 | supports | The original isolates separate white-powder A and B from Actinomadura sp. MK73-NF4, deposited as FERM P-16335. Production uses 27 C for 168 hours; purified A 31.7 mg and B 154.7 mg are separately obtained by extraction/chromatography. Table3 supplies their different one- versus two-chlorine formulas. FAB protonated/deprotonated ions are analytical ions, not salt identities. |
| activity1999 | https://doi.org/10.7164/antibiotics.52.781; Original Table4, page785, visually inspected; Biological Activities Methods, page782 | supports | A MICs are 1.56 micrograms/mL for S. aureus FDA209P, Smith and both named MRSA strains, and 3.13 for MS9610. Bacterial MICs used agar dilution in Mueller-Hinton agar at 37 C for 18 hours; the M. smegmatis ATCC607 row used 42 hours. These are measured strain-level observations, not present-day clinical breakpoint categories. |
| activity1999-boundary | https://doi.org/10.7164/antibiotics.52.781; Original Table4 and biological-activity prose | context_only | The original panel generally reports Gram-negative bacteria and yeast above 100 micrograms/mL, but the actual P. aeruginosa A3 row is 100, not greater than 100. Preserve the table/prose boundary rather than converting all rows into uniform inactivity. The paper reports acute mouse i.p. LD50 above 100 mg/kg, which is not evidence of human therapeutic safety or clinical efficacy. |
| structure-primary | https://doi.org/10.7164/antibiotics.52.787; PMID:10726926; original structure paper, pages787-796, Figure1, Table1, conversion and absolute-configuration sections | supports | Original Figure1 uses one shared A/B stereochemical scaffold differing only at the pyrrole chlorine. Page790 converts B to A by selective dechlorination and reports matching spectra and optical rotation. B methanolysis supplies the sugar whose bromobenzoyl derivative is assigned by anomalous-scattering crystallography; the stated sugar is D-arabino pyrrosamine. Aglycone relative geometry and absolute C9 configuration use NOESY and modified Mosher analysis. |
| structure-figure | https://doi.org/10.7164/antibiotics.52.787; Actual Figure1 and numbered Figure2 on page788 visually inspected | supports | The common drawing explicitly shows pyrrole NH and the same sugar C3-prime hydroxy orientation for A and B. A has R1=H/R2=Cl and B has R1=Cl/R2=Cl. This directly supports the missing-hydrogen correction and the absence of a sugar epimer difference between the named natural congeners. |
| structure-source-limit | https://doi.org/10.7164/antibiotics.52.787; Sugar stereochemistry, pages792-795; experimental crystallographic discussion | context_only | The paper calls degradation compound5 an alpha methyl glycoside in its preparation and coupling discussion, but a later naming sentence prints beta. That internal anomer-label inconsistency does not change the explicitly beta parent linkage, the shared A/B drawing, C3-prime coupling/NOESY relationship or chemical B-to-A conversion. No parent anomer correction is inferred from that isolated sentence. Crystal data were read, not independently rerefined. |
| pubchem-discovery | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/Decatromicin%20A/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; Name-search property results, used only as additional comparison | context_only | PubChem name retrieval supplies alternative tetronic-acid tautomer encodings; B additionally returns several records with different stereochemistry or unspecified centres. None is a native exact xref. No first-hit name match or key-prefix comparison was used to override the original structure, and no new PubChem mapping is recommended without full graph/tautomer adjudication. |
| activity2022 | https://doi.org/10.3390/molecules27238196; PMID:36500287 / PMC9737171; full main Methods/Results, exact A/B isolation, Table3 and actual Figure1 | supports | The study separately isolates A 10.9 mg and B 6.5 mg from Actinomadura sp. A30804 and identifies them by published MS/NMR comparison. Figure1 again has one shared sugar scaffold. Table3 gives S. aureus ATCC25923 MIC90/MBC90 of 3.3/3.9 micromolar for A and 1.4/3.1 for B. A. baumannii ATCC19606 is above 100 for A, while B MIC90 is 28.3 and MBC90 above 100 micromolar. These are new observations, not the 1999 strain panel. |
| activity2022-method | https://doi.org/10.3390/molecules27238196; Section2.6 and Table3; methods and endpoint interpretation | supports | The microbroth protocol uses 5.5×10^5 cells/mL,37 C for 24 hours and OD600, with triplicates. Its MBC90 is obtained by 5-microliter transfer into fresh medium and OD600 regrowth under the same incubation conditions; it is not an independently enumerated 99.9% kill endpoint. The main text does not specify the bacterial broth formulation here. The follow-up establishes natural B activity against one Gram-negative strain, so the historical definition should not be read as a universal exclusion of Gram-negative activity. |
| adapter | https://imodulondb.org/api/datasets; 325-adapter-catalog-network.json;346347-adapter.json, before open protein/pathway follow-up | context_only | No E. faecalis or Actinomadura dataset occurs in the inspected structured catalog. A supported S. aureus AgrA query returned USA300HOU_RS10975 and the Agr component. This establishes structured annotation context only; it is neither decatromicin binding nor proof of an E. faecalis mechanism. |
| quorum-primary | https://doi.org/10.3390/metabo12030246; PMID:35323689 / PMC8955454; exact decatromicin Results/Discussion, Table1 and Methods4.1-4.3 | context_only | Library compounds from the Biotechnology Research Center at Toyama Prefectural University were tested in E. faecalis OG1RF. The screen used 10 micrograms/mL; growth was OD600 and supernatant gelatinase activity was assayed with azocoll after 5-hour THB culture. The paper reports gelatinase suppression at 1 micromolar with little growth effect. These are phenotypic anti-virulence observations; they do not demonstrate direct binding to a particular Fsr protein, and S. aureus AgrA docking of other hit compounds is not decatromicin target proof. |
| quorum-boundary | https://doi.org/10.3390/metabo12030246; Table1 rows13-14 and decatromicin comparison paragraph | context_only | For A/B the S. aureus screen records strong growth inhibition and luciferase NA, not a separately demonstrated absence of Agr inhibition. The paper’s inherited 3.13 micromolar MIC sentence does not match the original Table4 units/congener values; it is not imported. Exact library batch purity and new absolute-configuration determination were not established from the inspected methods. |
| search | Ignored-inclusive local search and primary literature discovery; 346348-local-focused.txt;346347-exact-discovery.json;346348-fetch1-3.json | context_only | The sole adopted lead was fully read and the directly relevant companion structural original recovered. The bounded exact title/abstract query found two 2022 originals, both inspected at stated depth. The broader initial search included irrelevant stemming matches and was not treated as exhaustive. No paid register or source was accessed. |
| gates | Actual focused native checks; 346-focused-results.json; schema and strict logs | supports | Schema and strict checks pass, while independent chemistry records failure for the invalid native SMILES. The scratch-only corrected representation reproduces the retained graph; primary stereochemical accuracy remains a separate question. |

## Limits And Additional Notes

- The 1999 isolation paper was fully read, including Table4 visually. The companion structural paper was read through structure, conversion, stereochemical and experimental sections; Figures1-2 and relevant tables were inspected. Raw spectra and crystallographic coordinates were not independently reprocessed.
- The 2022 spirotetronate main methods/results and exact compound Table3 were read; Figure1 was visually inspected. The PMC supplementary ZIP route returned an HTML challenge, so all supplemental spectra, raw dose-response plots and cytotoxicity figures were not independently inspected.
- The 2022 quorum-sensing paper was read for exact decatromicin results, library source, strains, phenotype methods and Table1. Its individual raw plots, library batch purity and compound reidentification were not independently reconstructed; no direct molecular target is assigned.
- PubChem name results include tautomeric and stereochemical alternatives and are not asserted native xrefs. The review does not resolve every database variant or recommend automatic first-hit replacement.
- Reaxys was verified through official ChEBI accession metadata; the independent paid register was not accessed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record, maintained source, status or history was edited.
- Schema/strict used batch035; independent RDKit used existing batch019 against batch035 cwd.
- Optional links, tags and field paths were checked for this exact congener.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T142453Z-decatromicin-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Decatromicin A: invalid pyrrole SMILES with supported natural-product evidence'
started_at: '2026-10-21T14:02:30Z'
finished_at: '2026-10-21T14:24:53Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. The entire YAML,
    actual ChEBI source row and maintained transformations were read after preserved-input
    verification. Original isolation and structural papers, chemical drawings, assays
    and current authorities were independently inspected. Previous review drafts were
    not scientific evidence.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The native SMILES lacks the pyrrole hydrogen and fails chemical parsing.
  Its retained InChI, natural-product structure and bounded antibacterial/producer
  claims are supported by the original isolation and structure studies. A scratch-only
  hydrogen correction reproduces the exact key. No native molecular target is asserted;
  newer activity and quorum-sensing observations require distinct endpoint annotations.
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
  - path: data/antibiotics/antibacterial/decatromicin-a.yaml
    sha256: 961a83e349e64e696fc89ec2f40a4df7c8b9035c2debead901b91957625d763f
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
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
    role: context
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
  - path: scripts/extract_mibig_producers.py
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
    role: context
targets:
- target_id: CHEBI:65728
  path: data/antibiotics/antibacterial/decatromicin-a.yaml
  label: decatromicin A
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
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 346; one entire exact record. All 13 original inputs were
    preserved within 31 expanded inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65728
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: failed
  required: false
  summary: Actual focused execution exited 1.
  target_ids:
  - CHEBI:65728
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/346348-focused.py
    (cwd /private/tmp/antibioticmech-record-reviews-035)
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65728
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/decatromicin-a.yaml (cwd /private/tmp/antibioticmech-record-reviews-035)
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
  - CHEBI:65728
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/decatromicin-a.yaml --out /private/tmp/am-review-session/346-strict.tsv
    (cwd /private/tmp/antibioticmech-record-reviews-035)
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
  - CHEBI:65728
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
  - CHEBI:65728
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
  - CHEBI:65728
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
  - CHEBI:65728
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
  - CHEBI:65728
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
  - CHEBI:65728
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
  - CHEBI:65728
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
  - CHEBI:65728
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
  - CHEBI:65728
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/decatromicin-a.yaml
  locator: Entire record, exact synonym, all chemical parents/roles, structure, source
    and three history events
  accessed_at: '2026-10-21T14:16:35Z'
  support: supports
  summary: This SEEDED, EXACT record has one stereospecific synonym, ten structural
    parents and two antimicrobial roles. It has no molecular target, resistance entry,
    activity_spectrum, clinical product, causal graph, dataset or structured producer
    object. The producer and historical activity scope occur in the definition. The
    sole xref is Reaxys8469607.
  snapshot_sha256: 9846d19bb6bdbd5d99b1d0193039d86c2b4f6f45638e01f9bd98c9f1252be6b7
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: ChEBI row1285; extractor and seeder ownership
  accessed_at: '2026-10-21T14:16:35Z'
  support: supports
  summary: All asserted scientific source fields, including the defective SMILES and
    exact synonym, reproduce the ChEBI row. The sole adopted citation is PMID10726925.
    Actual source/transform/context inputs were appended without changing the original
    13 hashes. No exact ARO target/resistance or MIBiG producer row was present in
    the inspected exact-name/key source subsets.
  snapshot_sha256: 9846d19bb6bdbd5d99b1d0193039d86c2b4f6f45638e01f9bd98c9f1252be6b7
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity, exact stereochemistry, primary evidence and optional completeness
  accessed_at: '2026-10-21T14:16:35Z'
  support: supports
  summary: A molecular representation must parse and preserve the exact natural-product
    structure. Exact synonym and assay material must agree. Optional target, producer
    and activity fields are not automatically required simply because enrichment is
    possible.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/65728/
  locator: CHEBI:65728, complete current structure, names, roles, parents, origin
    and citations
  accessed_at: '2026-10-21T14:11:07.977218Z'
  support: context_only
  summary: Current ChEBI retains the native invalid pyrrole SMILES and the same complete
    InChI. All native role and structural-parent identifiers resolve in the current
    authority. Agreement with the source confirms inheritance but does not resolve
    the independent primary structural comparison.
  snapshot_sha256: 3f707ccb412a87ff990b70c38e97dae5afcdab33a37e7d915db0f19093ad2a21
- evidence_id: reaxys
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/65728/
  locator: Reaxys8469607 registry accession
  accessed_at: '2026-10-21T14:11:07.977218Z'
  support: context_only
  summary: The only native registry link is retained by official ChEBI. No independent
    paid Reaxys register was accessed, so that register was not used as independent
    stereochemical evidence.
  snapshot_sha256: 3f707ccb412a87ff990b70c38e97dae5afcdab33a37e7d915db0f19093ad2a21
- evidence_id: chemistry
  kind: validation
  reference: Independent batch019 RDKit against batch035 cwd
  locator: 346348-focused.py;346-chemistry.json
  accessed_at: '2026-10-21T14:16:35Z'
  support: refutes
  summary: Native SMILES fails kekulization because its pyrrole N is encoded as aromatic
    n. Replacing only that token with [nH] in scratch reproduces the stored key YKLXDAWPGVZXKC-NMNDIUEASA-N,
    formula, neutral charge and thirteen assigned centres. The native InChI parses
    and its masses and source mint reproduce. The separately reviewed B epimer issue
    does not alter the supported A mapping. No native edit occurred.
  snapshot_sha256: 8e78ac2b74fd77b26119b443d0d66eff4ef0ab906a2bbee0f54d013176f181f1
- evidence_id: stereo-map
  kind: validation
  reference: Independent numbered sugar mapping and dechlorination comparison
  locator: 346348-map.py;346347-stereo-map.json
  accessed_at: '2026-10-21T14:16:35Z'
  support: supports
  summary: In hydrogen-repaired native strings, sugar C1-prime/C2-prime/C3-prime/C4-prime
    are zero-based atoms41/42/43/45; C5-prime is55 in A and56 in B. A sugar centres
    are R,R,S,R at C1/C3/C4/C5; B is R,S,S,R. Flipping only B C3-prime gives OKYWSSBYCHUWKT-SHSCNYKZSA-N.
    Removing only its extra pyrrole5-double-prime chlorine then reproduces the entire
    A key exactly, including all remaining centres and double bonds.
  snapshot_sha256: bcd092e443c7dbc105c399a0859bc4e1b1f9865f2462dbffe49c8fbbd5671f5f
- evidence_id: isolation-primary
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.52.781
  locator: Adopted PMID:10726925; full original six-page paper, Methods and Results,
    Tables3-4
  accessed_at: '2026-10-21T14:11:39.957407Z'
  support: supports
  summary: The original isolates separate white-powder A and B from Actinomadura sp.
    MK73-NF4, deposited as FERM P-16335. Production uses 27 C for 168 hours; purified
    A 31.7 mg and B 154.7 mg are separately obtained by extraction/chromatography.
    Table3 supplies their different one- versus two-chlorine formulas. FAB protonated/deprotonated
    ions are analytical ions, not salt identities.
  snapshot_sha256: 98f7ae55319743587b290c476dc4b94877688d911d744cc6abfea3c3a19c45ea
- evidence_id: activity1999
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.52.781
  locator: Original Table4, page785, visually inspected; Biological Activities Methods,
    page782
  accessed_at: '2026-10-21T14:16:35Z'
  support: supports
  summary: A MICs are 1.56 micrograms/mL for S. aureus FDA209P, Smith and both named
    MRSA strains, and 3.13 for MS9610. Bacterial MICs used agar dilution in Mueller-Hinton
    agar at 37 C for 18 hours; the M. smegmatis ATCC607 row used 42 hours. These are
    measured strain-level observations, not present-day clinical breakpoint categories.
  snapshot_sha256: 1ad0d81b64713a17af07cb2b31e088eec2d7ed38346d9fc692417cee6c265064
- evidence_id: activity1999-boundary
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.52.781
  locator: Original Table4 and biological-activity prose
  accessed_at: '2026-10-21T14:11:39.957407Z'
  support: context_only
  summary: The original panel generally reports Gram-negative bacteria and yeast above
    100 micrograms/mL, but the actual P. aeruginosa A3 row is 100, not greater than
    100. Preserve the table/prose boundary rather than converting all rows into uniform
    inactivity. The paper reports acute mouse i.p. LD50 above 100 mg/kg, which is
    not evidence of human therapeutic safety or clinical efficacy.
  snapshot_sha256: 98f7ae55319743587b290c476dc4b94877688d911d744cc6abfea3c3a19c45ea
- evidence_id: structure-primary
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.52.787
  locator: PMID:10726926; original structure paper, pages787-796, Figure1, Table1,
    conversion and absolute-configuration sections
  accessed_at: '2026-10-21T14:11:39.957723Z'
  support: supports
  summary: Original Figure1 uses one shared A/B stereochemical scaffold differing
    only at the pyrrole chlorine. Page790 converts B to A by selective dechlorination
    and reports matching spectra and optical rotation. B methanolysis supplies the
    sugar whose bromobenzoyl derivative is assigned by anomalous-scattering crystallography;
    the stated sugar is D-arabino pyrrosamine. Aglycone relative geometry and absolute
    C9 configuration use NOESY and modified Mosher analysis.
  snapshot_sha256: d80373fb408a140a4933ead4a65df2d375380fc0e807ced63bc126e5744c34e4
- evidence_id: structure-figure
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.52.787
  locator: Actual Figure1 and numbered Figure2 on page788 visually inspected
  accessed_at: '2026-10-21T14:16:35Z'
  support: supports
  summary: The common drawing explicitly shows pyrrole NH and the same sugar C3-prime
    hydroxy orientation for A and B. A has R1=H/R2=Cl and B has R1=Cl/R2=Cl. This
    directly supports the missing-hydrogen correction and the absence of a sugar epimer
    difference between the named natural congeners.
  snapshot_sha256: 8bd4e24603dbe5064bc41efa4028e8bbc49bd94df08ce16948734b9496891bb2
- evidence_id: structure-source-limit
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.52.787
  locator: Sugar stereochemistry, pages792-795; experimental crystallographic discussion
  accessed_at: '2026-10-21T14:11:39.957723Z'
  support: context_only
  summary: The paper calls degradation compound5 an alpha methyl glycoside in its
    preparation and coupling discussion, but a later naming sentence prints beta.
    That internal anomer-label inconsistency does not change the explicitly beta parent
    linkage, the shared A/B drawing, C3-prime coupling/NOESY relationship or chemical
    B-to-A conversion. No parent anomer correction is inferred from that isolated
    sentence. Crystal data were read, not independently rerefined.
  snapshot_sha256: d80373fb408a140a4933ead4a65df2d375380fc0e807ced63bc126e5744c34e4
- evidence_id: pubchem-discovery
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/Decatromicin%20A/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: Name-search property results, used only as additional comparison
  accessed_at: '2026-10-21T14:11:07.977900Z'
  support: context_only
  summary: PubChem name retrieval supplies alternative tetronic-acid tautomer encodings;
    B additionally returns several records with different stereochemistry or unspecified
    centres. None is a native exact xref. No first-hit name match or key-prefix comparison
    was used to override the original structure, and no new PubChem mapping is recommended
    without full graph/tautomer adjudication.
  snapshot_sha256: 8ab5769d0ae39a1585147d733e067be3e90c18025a09c1b4a6a349e3e98b91b5
- evidence_id: activity2022
  kind: primary_source
  reference: https://doi.org/10.3390/molecules27238196
  locator: PMID:36500287 / PMC9737171; full main Methods/Results, exact A/B isolation,
    Table3 and actual Figure1
  accessed_at: '2026-10-21T14:11:39.963076Z'
  support: supports
  summary: The study separately isolates A 10.9 mg and B 6.5 mg from Actinomadura
    sp. A30804 and identifies them by published MS/NMR comparison. Figure1 again has
    one shared sugar scaffold. Table3 gives S. aureus ATCC25923 MIC90/MBC90 of 3.3/3.9
    micromolar for A and 1.4/3.1 for B. A. baumannii ATCC19606 is above 100 for A,
    while B MIC90 is 28.3 and MBC90 above 100 micromolar. These are new observations,
    not the 1999 strain panel.
  snapshot_sha256: e84504b89bcb331ab56fc7e71cda15267fa363c3858a9b1e60139f6ac3f1464a
- evidence_id: activity2022-method
  kind: primary_source
  reference: https://doi.org/10.3390/molecules27238196
  locator: Section2.6 and Table3; methods and endpoint interpretation
  accessed_at: '2026-10-21T14:11:39.963076Z'
  support: supports
  summary: The microbroth protocol uses 5.5×10^5 cells/mL,37 C for 24 hours and OD600,
    with triplicates. Its MBC90 is obtained by 5-microliter transfer into fresh medium
    and OD600 regrowth under the same incubation conditions; it is not an independently
    enumerated 99.9% kill endpoint. The main text does not specify the bacterial broth
    formulation here. The follow-up establishes natural B activity against one Gram-negative
    strain, so the historical definition should not be read as a universal exclusion
    of Gram-negative activity.
  snapshot_sha256: e84504b89bcb331ab56fc7e71cda15267fa363c3858a9b1e60139f6ac3f1464a
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 325-adapter-catalog-network.json;346347-adapter.json, before open protein/pathway
    follow-up
  accessed_at: '2026-10-21T14:16:35Z'
  support: context_only
  summary: No E. faecalis or Actinomadura dataset occurs in the inspected structured
    catalog. A supported S. aureus AgrA query returned USA300HOU_RS10975 and the Agr
    component. This establishes structured annotation context only; it is neither
    decatromicin binding nor proof of an E. faecalis mechanism.
  snapshot_sha256: 0fd7551026d0997091ddc7959cf84e8434c72ab4055e7b4c6080eb354a121f92
- evidence_id: quorum-primary
  kind: primary_source
  reference: https://doi.org/10.3390/metabo12030246
  locator: PMID:35323689 / PMC8955454; exact decatromicin Results/Discussion, Table1
    and Methods4.1-4.3
  accessed_at: '2026-10-21T14:13:33.154200Z'
  support: context_only
  summary: Library compounds from the Biotechnology Research Center at Toyama Prefectural
    University were tested in E. faecalis OG1RF. The screen used 10 micrograms/mL;
    growth was OD600 and supernatant gelatinase activity was assayed with azocoll
    after 5-hour THB culture. The paper reports gelatinase suppression at 1 micromolar
    with little growth effect. These are phenotypic anti-virulence observations; they
    do not demonstrate direct binding to a particular Fsr protein, and S. aureus AgrA
    docking of other hit compounds is not decatromicin target proof.
  snapshot_sha256: 15ec96a6442b8d2f1e077dda65f3ec54713ffbbd4c4f50eb6cfd9a08a37275de
- evidence_id: quorum-boundary
  kind: primary_source
  reference: https://doi.org/10.3390/metabo12030246
  locator: Table1 rows13-14 and decatromicin comparison paragraph
  accessed_at: '2026-10-21T14:13:33.154200Z'
  support: context_only
  summary: For A/B the S. aureus screen records strong growth inhibition and luciferase
    NA, not a separately demonstrated absence of Agr inhibition. The paper’s inherited
    3.13 micromolar MIC sentence does not match the original Table4 units/congener
    values; it is not imported. Exact library batch purity and new absolute-configuration
    determination were not established from the inspected methods.
  snapshot_sha256: 15ec96a6442b8d2f1e077dda65f3ec54713ffbbd4c4f50eb6cfd9a08a37275de
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local search and primary literature discovery
  locator: 346348-local-focused.txt;346347-exact-discovery.json;346348-fetch1-3.json
  accessed_at: '2026-10-21T14:16:35Z'
  support: context_only
  summary: The sole adopted lead was fully read and the directly relevant companion
    structural original recovered. The bounded exact title/abstract query found two
    2022 originals, both inspected at stated depth. The broader initial search included
    irrelevant stemming matches and was not treated as exhaustive. No paid register
    or source was accessed.
  snapshot_sha256: 998aa46dda99f5a6c6de5d4c3ca6123eb9ad857177e3fee724772b3c9418368d
  search_scope: 2026-10-21; exact decatromicin names, ChEBI identifiers and molecular
    keys; hidden and ignored repository files included. Exact TITLE_ABS Europe PMC
    queries and free original-paper follow-up were bounded, not an exhaustive literature
    census.
- evidence_id: gates
  kind: validation
  reference: Actual focused native checks
  locator: 346-focused-results.json; schema and strict logs
  accessed_at: '2026-10-21T14:16:35Z'
  support: supports
  summary: Schema and strict checks pass, while independent chemistry records failure
    for the invalid native SMILES. The scratch-only corrected representation reproduces
    the retained graph; primary stereochemical accuracy remains a separate question.
  snapshot_sha256: fdae2a27ae83b69ed5a9c865c05f96f0ed893f919ebbdbc8b7e50fcfe4ed6c53
assessments:
- assessment_id: identity
  area: identity
  topic: Natural-product graph and structural encoding
  outcome: concern
  summary: The original structure and thirteen assigned centres are coherent with
    the retained InChI. The invalid pyrrole SMILES is a confirmed repairable representation
    defect.
  target_ids:
  - CHEBI:65728
  evidence_ids:
  - chemistry
  - stereo-map
  - structure-primary
  - structure-figure
  - structure-source-limit
  - rubric
- assessment_id: grounding
  area: grounding
  topic: Names, chemical authorities and exact groundings
  outcome: supported
  summary: Official ChEBI reproduces the intended A InChI and source names; the sole
    Reaxys link remains authority-confirmed with independent-register limits. Additional
    PubChem name results are not native exact links.
  target_ids:
  - CHEBI:65728
  evidence_ids:
  - chebi
  - pubchem-discovery
  - structure-primary
  - stereo-map
  - reaxys
- assessment_id: classification
  area: scope
  topic: Antibacterial roles and historical definition
  outcome: supported
  summary: The original isolated A has direct strain-level antibacterial activity
    and a verified Actinomadura producer. The historical Gram-positive emphasis is
    panel-scoped, not a universal spectrum claim.
  target_ids:
  - CHEBI:65728
  evidence_ids:
  - isolation-primary
  - activity1999
  - activity1999-boundary
  - activity2022
  - activity2022-method
  - structure-primary
- assessment_id: activity
  area: completeness
  topic: Optional activity_spectrum
  outcome: unknown
  summary: Exact original and newer strain-level measurements are available for optional
    enrichment, but units, agar versus OD90 microbroth endpoints, producer-derived
    materials and assay-specific MBC definitions must remain explicit. No present-day
    susceptibility breakpoint or clinical category is inferred.
  target_ids:
  - CHEBI:65728
  evidence_ids:
  - activity1999
  - activity2022
  - activity2022-method
  - rubric
- assessment_id: targets-resistance
  area: evidence
  topic: Optional mechanism and resistance assertions
  outcome: unknown
  summary: No native molecular target or resistance entry is populated. Gelatinase
    suppression supports a bounded phenotype; it does not identify direct Fsr binding
    or explain antibacterial killing. Parent-family analogies and docking of other
    molecules are insufficient for target import.
  target_ids:
  - CHEBI:65728
  evidence_ids:
  - native
  - quorum-primary
  - quorum-boundary
  - adapter
  - rubric
- assessment_id: producer
  area: provenance
  topic: Definition producer and optional structured producer
  outcome: supported
  summary: The original identifies MK73-NF4 and its deposit as the A/B producer. The
    2022 A30804 experiment is a separate producer with 16S accession OP225395. Neither
    strain should be silently replaced by a named species merely from a phylogenetic
    neighbor.
  target_ids:
  - CHEBI:65728
  evidence_ids:
  - isolation-primary
  - activity2022
  - chebi
- assessment_id: other
  area: scope
  topic: Clinical products, causal graph and datasets
  outcome: not_applicable
  summary: No clinical product, approval, causal graph or dataset assertion is present.
    Acute mouse toxicity and in vitro assays do not establish human therapeutic safety
    or efficacy.
  target_ids:
  - CHEBI:65728
  evidence_ids:
  - native
  - activity1999-boundary
- assessment_id: provenance
  area: provenance
  topic: Source ownership, status and history
  outcome: supported
  summary: Three generated seeding/reseeding events and SEEDED status are coherent.
    All original hashes are preserved, with source ownership recorded for reproducible
    correction.
  target_ids:
  - CHEBI:65728
  evidence_ids:
  - native
  - owners
  - search
- assessment_id: checks
  area: schema
  topic: Focused validation
  outcome: concern
  summary: Native schema gates pass while chemical parsing fails. The independent
    original-source comparison supports the retained A configuration; parsing and
    key agreement alone do not establish scientific identity.
  target_ids:
  - CHEBI:65728
  evidence_ids:
  - gates
  - chemistry
  - stereo-map
findings:
- finding_id: F1
  issue_key: decatromicin-a-invalid-pyrrole-smiles
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Missing pyrrole hydrogen makes the native SMILES invalid
  description: The pyrrole nitrogen is encoded as aromatic n rather than [nH]. Independent
    parsing fails kekulization, while correcting only that hydrogen in scratch gives
    precisely the stored InChI/key, formula and stereochemistry. Original drawings
    explicitly show the pyrrole NH. Repair the maintained source representation while
    preserving the supported A configuration.
  target_ids:
  - CHEBI:65728
  field_paths:
  - chemical_structure.smiles
  evidence_ids:
  - chemistry
  - chebi
  - structure-figure
  - owners
  - gates
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted structure and exact synonym source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated molecular identity and source fields
  rule_id: native-review-checklist:Identity
  native_severity: major invalid molecular encoding with recoverable retained graph
  normalization_reason: The representation is unparseable despite valid YAML; an independently
    coherent InChI makes the encoding error locally diagnosable.
actions:
- action_id: A1
  description: Repair the maintained pyrrole SMILES and verify all exact chemical
    fields.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65728
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted structure and exact synonym source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated molecular identity and source fields
  acceptance_checks:
  - Encode the pyrrole NH explicitly and ensure SMILES parses and agrees with the
    intended final InChI, formula, charge and thirteen stereocentres.
  - Do not confuse this hydrogen correction with adjudication of sugar configuration.
  - Make any authorized change through maintained source/curation ownership and pass
    native, chemistry, corpus, provenance and history gates.
- action_id: A2
  description: Optionally enrich exact activity, producer and quorum-sensing phenotype
    context.
  finding_ids: []
  target_ids:
  - CHEBI:65728
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/decatromicin-a.yaml
    role: Curator-owned primary evidence and history
  acceptance_checks:
  - Keep 1999 micrograms/mL agar-dilution MICs separate from 2022 micromolar MIC90/MBC90
    values and their respective strains.
  - Preserve P. aeruginosa A3=100 in the original table and avoid importing the later
    paper’s incorrect inherited 3.13 micromolar comparison.
  - Keep anti-gelatinase phenotype separate from growth MIC, direct enzyme inhibition,
    docking and target binding.
  - Retain MK73-NF4 and A30804 as distinct producer observations; do not infer clinical
    safety or optional-field invalidity.
limitations:
- The 1999 isolation paper was fully read, including Table4 visually. The companion
  structural paper was read through structure, conversion, stereochemical and experimental
  sections; Figures1-2 and relevant tables were inspected. Raw spectra and crystallographic
  coordinates were not independently reprocessed.
- The 2022 spirotetronate main methods/results and exact compound Table3 were read;
  Figure1 was visually inspected. The PMC supplementary ZIP route returned an HTML
  challenge, so all supplemental spectra, raw dose-response plots and cytotoxicity
  figures were not independently inspected.
- The 2022 quorum-sensing paper was read for exact decatromicin results, library source,
  strains, phenotype methods and Table1. Its individual raw plots, library batch purity
  and compound reidentification were not independently reconstructed; no direct molecular
  target is assigned.
- PubChem name results include tautomeric and stereochemical alternatives and are
  not asserted native xrefs. The review does not resolve every database variant or
  recommend automatic first-hit replacement.
- Reaxys was verified through official ChEBI accession metadata; the independent paid
  register was not accessed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record, maintained source, status or history was edited.
- Schema/strict used batch035; independent RDKit used existing batch019 against batch035
  cwd.
- Optional links, tags and field paths were checked for this exact congener.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:65728
- https://doi.org/10.7164/antibiotics.52.781
- https://doi.org/10.7164/antibiotics.52.787
tags:
- decatromicin-a
- pyrrole-smiles
- primary-assay-scope
```
