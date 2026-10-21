# Declovanillobiocin: missing sugar stereochemistry and incorrect structural term

- Review: 20261021T142502Z-declovanillobiocin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:02:32Z
- Finished UTC: 2026-10-21T14:25:02Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native graph omits all four stereocentres of the defined noviose-containing compound shown in the original paper. A major exact-structure completion is needed, alongside a minor correction from crenelated to prenylated in the definition. The original establishes antibacterial disc-diffusion activity and production by a cloQ-defective strain; it does not report a declovanillobiocin MIC or direct gyrase-binding experiment.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 348; one entire exact record. All 13 original input hashes were preserved within 31 expanded inputs, with actual ARO/PubChem owner paths recorded.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-cb28770ae8 | data/antibiotics/antibacterial/declovanillobiocin.yaml | generated | declovanillobiocin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-cb28770ae8 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-cb28770ae8 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-cb28770ae8 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-cb28770ae8 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-cb28770ae8 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-cb28770ae8 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-cb28770ae8 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-cb28770ae8 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-cb28770ae8 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-cb28770ae8 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-cb28770ae8 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-cb28770ae8 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Defined noviose-containing product versus native partial graph

identity: concern. Targets: antibioticmech:aro-cb28770ae8.

The original Figure2 and structural comparison identify a stereodefined sugar scaffold, while the native graph omits all four centres. This is incomplete exact identity, not proof of a racemic or mixed preparation. Connectivity, charge and formula are coherent.

### ARO, ChEBI and PubChem exact links

grounding: supported. Targets: antibioticmech:aro-cb28770ae8.

All three asserted xrefs resolve and match the current source identity/partial graph. The upstream agreement does not fill the known stereochemical gap. Any authorized structure completion must reconcile the partial database groundings explicitly.

### Structural comparator wording and adopted source

evidence: concern. Targets: antibioticmech:aro-cb28770ae8.

The sole original directly supports vanilloyl substitution and loss of aminocoumarin chlorine, but its word is prenylated, not crenelated. The native miswording is inherited from ARO.

### Antibacterial eligibility and optional activity_spectrum

scope: supported. Targets: antibioticmech:aro-cb28770ae8.

Exact isolated declovanillobiocin has measurable B. subtilis disc-diffusion activity. Relative zone-based potency cannot be converted into a MIC or a species-wide clinical susceptibility conclusion. Optional numerical enrichment should retain the stated disc amount, medium, strain and endpoint.

### Optional mechanism, target and resistance fields

completeness: unknown. Targets: antibioticmech:aro-cb28770ae8.

No native target or resistance annotation is populated. The original assays do not establish direct declovanillobiocin gyrase binding or resistance alleles, and structured annotation of gyrB does not close that evidence gap.

### Optional producer annotation

provenance: supported. Targets: antibioticmech:aro-cb28770ae8.

The isolated compound comes from the engineered cloQ-defective DS12.976 strain under the reported fermentation; this is not interchangeable with ordinary wild-type production. The isolated cloR discussion typo is retained as a source limitation.

### Clinical products, causal graph, datasets and synonyms

scope: not_applicable. Targets: antibioticmech:aro-cb28770ae8.

No native clinical product, approval, causal graph, dataset or synonym assertion is populated. The source establishes laboratory activity and production, not human use.

### Actual source ownership and generated history

provenance: supported. Targets: antibioticmech:aro-cb28770ae8.

The three seeding/reseeding events and SEEDED status are coherent. Initial captures are preserved; ARO owns definition/class/xrefs and PubChem owns structure, with exact transformation owners recorded for reproducibility.

### Focused gates

schema: supported. Targets: antibioticmech:aro-cb28770ae8.

All actual focused checks pass. They establish internal encoding consistency, not completeness of experimental stereochemical identity.

## Findings

### F1: All four sugar stereocentres are omitted from the named natural-product graph

major / open / confirmed; issue key: declovanillobiocin-missing-noviose-stereochemistry.

The original Figure2 defines the noviose scaffold of isolated declovanillobiocin, supported by its NMR comparison with the related products and clorobiocin. Native SMILES and InChI instead leave all four stereocentres unassigned, matching the incomplete PubChem/ChEBI encoding. This broader partial graph does not retain the exact characterized compound. Recover and verify the original sugar configuration through maintained ownership; do not infer a racemate or fill centres by arbitrary enumeration.

### F2: The definition misnames the clorobiocin prenylated aryl group

minor / open / confirmed; issue key: declovanillobiocin-prenylated-definition-term.

The original repeatedly describes prenylated 4-hydroxybenzoic acid, whose dimethylallyl substituent is shown in Figure1. The native ARO-derived definition says crenelated, which is not the chemical group. Correct this source wording while retaining the supported vanillic-acid and chlorine comparisons.

## Recommended Actions And Acceptance Checks

### A1

Recover the four defined sugar configurations and reconcile all final molecular encodings.

- Map each sugar centre to original Figure2 and verify the noviose configuration and 3-double-prime ester position against Table1 and the primary comparator structures.
- Generate mutually consistent stereospecific SMILES, InChI and key while preserving formula, charge and connectivity.
- Qualify or resolve upstream partial graph links explicitly rather than silently treating unspecified and assigned structures as identical.
- Use maintained curation/source ownership and pass required chemistry, schema, corpus, provenance and history checks.

### A2

Correct the inherited structural term to prenylated.

- Match the primary structural description and retain its correct compound comparisons.
- Keep the source correction reproducible through extraction/seeding and required validation.

### A3

Optionally add the original phenotype and engineered-producer evidence.

- Record B. subtilis ATCC14893 disc diffusion with 8/16/32 nmol dosing and relative activity 1.5-3%; do not convert it to MIC.
- Distinguish the cloQ-defective DS12.976 production context from wild type and from the separate cloR mutant experiment.
- Do not assign direct gyrase binding or a resistance mechanism from the clorobiocin introduction or a gene-source query.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/declovanillobiocin.yaml; Entire YAML, definition, family class, structure, all three xrefs, source and three history events | supports | The SEEDED, MINTED antibacterial record has no synonym list, molecular target, resistance entry, activity_spectrum, clinical product, structured producer, causal graph or dataset. Its definition asserts structural differences from clorobiocin/vanillobiocin, and all three history events describe source seeding/reseeding. |
| owners | data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv; ARO row354; PubChem row119; extractor/enricher/seeder ownership | supports | ARO owns the definition, class, adopted PMID and xrefs; PubChem owns the complete native chemical_structure. The initial generic ChEBI owner list was replaced in the expanded target description by the actual ARO/PubChem owners, while all original captured bytes/hashes were preserved. No exact native ChEBI seed row, target/resistance source edge or producer join was found in the inspected source subsets. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Exact structure, nomenclature, source evidence and optional fields | supports | A named stereodefined natural product must retain its known chemical identity. Unassigned stereochemistry is not evidence of a racemate. Missing optional primary-target or assay fields alone are not native defects; original compound and experimental endpoint boundaries must be preserved. |
| chemistry | Independent batch019 RDKit against batch035 cwd; 346348-focused.py;348-chemistry.json | supports | Native SMILES and InChI agree on neutral C31H32N2O12, key JURYCYSCKRZQLD-UHFFFAOYSA-N, average mass 624.599 and exact mass 624.195524. All four potential sugar stereocentres are unassigned: native SMILES zero-based atoms 9,10,11 and 14. Formula, charge, rounded masses and minted identifier reproduce; valid parsing does not recover the missing configuration. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/76173558/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; CID76173558 complete property response | context_only | Current PubChem agrees exactly with the native graph and lacks all four sugar assignments. This verifies the source of the incomplete graph, not the stereochemical identity of the material characterized in the original paper. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/206681/; CHEBI:206681 current names, formula, default InChI/key, origin and ontology parents | context_only | Current ChEBI also has the same stereochemically unassigned InChI/key and an unstereospecified systematic name. Its submitted aromatic SMILES has a pyrrole encoding problem, but that string is not the native representation and is not raised as a native defect. Its broad glycoside/coumarin classification agrees with constitution but does not supply the missing configuration. |
| aro | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3004718; ARO:3004718 and native definition/class/xrefs | context_only | The live ARO term reproduces the definition, including crenelated, and the exact adopted citation. The family class ARO:3000103 resolves. No compound-specific protein-target or resistance claim is asserted by this record. |
| primary | https://doi.org/10.7164/antibiotics.57.205; Adopted PMID:15152806; full five-page original, Methods/Results/Discussion | supports | The original separately isolates vanillobiocin, isovanillobiocin and declovanillobiocin from the cloQ-defective Streptomyces roseochromogenes DS12.976 culture. Declovanillobiocin is compound 3, lacks the aminocoumarin chlorine, and retains the 3-double-prime pyrrole ester and noviose scaffold. The aryl difference from clorobiocin is vanilloyl in place of prenylated 4-hydroxybenzoate. The native word crenelated does not name that group. |
| structure-figure | https://doi.org/10.7164/antibiotics.57.205; Actual Figure2, page208, visually inspected with compound3 substituent row | supports | Figure2 depicts a defined sugar ring with oriented substituents: anomeric aromatic glycoside, free hydroxy, pyrrole ester and methoxy. The same scaffold is used for all three products, with the declovanillobiocin row specifying ester at3-double-prime, free2-double-prime hydroxy and no aminocoumarin chlorine. The native graph retains connectivity but none of the four sugar configurations. |
| nmr-table | https://doi.org/10.7164/antibiotics.57.205; Actual Table1, page207, visually inspected; structural elucidation text | supports | Original1H NMR data distinguish compound 3 from the chlorinated analogues and compare its sugar resonances with authentic clorobiocin. The paper does not describe four independently randomized centres or a stereoisomer mixture. The figures and assigned noviose scaffold support completion of known stereochemistry; this review does not independently reassign absolute configuration from raw spectra. |
| assay | https://doi.org/10.7164/antibiotics.57.205; Bioassay Methods, page206; actual Figure3 on page208; activity Results | supports | Separately isolated compound 3 was dissolved in methanol and applied at 8,16 and 32 nmol to 3-mm paper discs on nutrient agar containing approximately 2×10^5 Bacillus subtilis ATCC14893 spores/mL. After 30 minutes drying and overnight incubation at 37 C, inhibition-zone diameters were compared with authentic clorobiocin and novobiocin. Declovanillobiocin relative activity is 1.5-3% with clorobiocin set to 100%. These are comparative disc-diffusion observations, not MICs, direct binding or clinical efficacy. |
| producer | https://doi.org/10.7164/antibiotics.57.205; Fermentation/isolation Methods and Results, pages205-207; final discussion scope | supports | The production culture was incubated at 33 C for 9 days. Acidified broth extraction, Sephadex and preparative HPLC separately yielded 0.4 mg declovanillobiocin from 800 mL. The primary context is a cloQ-defective engineered strain; wild type did not accumulate detectable vanillobiocins. A separate cloR mutant also lacked their accumulation. One discussion sentence says cloR where title, abstract, Methods and Results consistently identify cloQ; retain that source typo instead of changing the supported producer genotype. |
| target-boundary | https://doi.org/10.7164/antibiotics.57.205; Introduction and biological-assay section | context_only | The introduction names bacterial DNA gyrase as the target of clorobiocin and cites earlier parent-family experiments. This paper measures declovanillobiocin bacterial growth zones and structure; it does not demonstrate exact-compound gyrase binding, ATPase inhibition, an allele-specific resistance mechanism or a causal chain. Family inference should not be promoted to a direct target annotation. |
| adapter | https://imodulondb.org/api/datasets; 348-adapter.json and348-adapter-network.json; query before protein-mechanism web follow-up | context_only | The initial structured e_coli/precise1k/gyrB query failed with sandbox DNS, then the authorized public-network retry succeeded with b3699/gyrB and zero modules. This is gene annotation context, not declovanillobiocin binding or resistance. No source absence is inferred from the initial failure. |
| search | Ignored-inclusive repository search and public primary retrieval; 346348-local-focused.txt;348-discovery.json;346348-fetch1-3.json | context_only | The sole adopted original was retrieved freely from J-STAGE and fully read. Additional hits were database/review context, not new exact-compound target experiments. All native xrefs were checked through current official sources. No paid source or third-party contact was used. |
| gates | Actual focused native checks; 348-focused-results.json;348-schema.log;348-strict.log | supports | Schema, strict and chemistry checks all exit 0. The omitted sugar stereochemistry is internally consistent across the source identifiers and therefore survives those gates. |

## Limits And Additional Notes

- The full adopted 2004 original was read, with actual Figure2, Figure3 and Table1 visually inspected. Raw NMR data and a new absolute-configuration analysis were not independently reconstructed. The correction requires explicit mapping of the four known sugar centres; no arbitrary stereoisomer key is proposed.
- The direct activity evidence is relative disc diffusion. No declovanillobiocin MIC, direct gyrase-binding assay, resistance genotype or clinical efficacy measurement was established from the inspected source.
- The producer paper has a cloR/cloQ typo in one discussion sentence and a neighboring isovanillobiocin positional-comparison typo. Its repeated Methods/Results and Figure2 supply the bounded compound/producer mapping; those isolated sentences are not imported literally.
- Current ChEBI/PubChem agree with the partial graph. ChEBI’s separate malformed aromatic SMILES is not native and was not turned into an extra native finding.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record, source, status or history was edited.
- Schema/strict used batch035; standalone RDKit used existing batch019 against batch035 cwd.
- Optional links, tags, notes and finding field paths were checked against this exact compound.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T142502Z-declovanillobiocin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Declovanillobiocin: missing sugar stereochemistry and incorrect structural
  term'
started_at: '2026-10-21T14:02:32Z'
finished_at: '2026-10-21T14:25:02Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. The entire YAML and
    actual ARO/PubChem source rows were read after initial hash verification. Chemical
    representations were independently parsed, official groundings checked, and the
    sole adopted original was fully read with structure, NMR table and bioassay figures
    visually inspected.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The native graph omits all four stereocentres of the defined noviose-containing
  compound shown in the original paper. A major exact-structure completion is needed,
  alongside a minor correction from crenelated to prenylated in the definition. The
  original establishes antibacterial disc-diffusion activity and production by a cloQ-defective
  strain; it does not report a declovanillobiocin MIC or direct gyrase-binding experiment.
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
  - path: data/antibiotics/antibacterial/declovanillobiocin.yaml
    sha256: f9e7f9bb96c60c69d6f1ee837033a39d458a6d51c39fec209ff88dffebe30585
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
- target_id: antibioticmech:aro-cb28770ae8
  path: data/antibiotics/antibacterial/declovanillobiocin.yaml
  label: declovanillobiocin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO definition, identity, class and adopted citation
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: PubChem chemical structure owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source fields
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Identity grounding overrides
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 348; one entire exact record. All 13 original input hashes
    were preserved within 31 expanded inputs, with actual ARO/PubChem owner paths
    recorded.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-cb28770ae8
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-cb28770ae8
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/346348-focused.py
    (cwd /private/tmp/antibioticmech-record-reviews-035)
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
  - antibioticmech:aro-cb28770ae8
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/declovanillobiocin.yaml (cwd /private/tmp/antibioticmech-record-reviews-035)
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
  - antibioticmech:aro-cb28770ae8
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/declovanillobiocin.yaml --out /private/tmp/am-review-session/348-strict.tsv
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
  - antibioticmech:aro-cb28770ae8
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
  - antibioticmech:aro-cb28770ae8
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
  - antibioticmech:aro-cb28770ae8
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
  - antibioticmech:aro-cb28770ae8
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
  - antibioticmech:aro-cb28770ae8
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
  - antibioticmech:aro-cb28770ae8
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
  - antibioticmech:aro-cb28770ae8
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
  - antibioticmech:aro-cb28770ae8
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
  - antibioticmech:aro-cb28770ae8
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/declovanillobiocin.yaml
  locator: Entire YAML, definition, family class, structure, all three xrefs, source
    and three history events
  accessed_at: '2026-10-21T14:18:43Z'
  support: supports
  summary: The SEEDED, MINTED antibacterial record has no synonym list, molecular
    target, resistance entry, activity_spectrum, clinical product, structured producer,
    causal graph or dataset. Its definition asserts structural differences from clorobiocin/vanillobiocin,
    and all three history events describe source seeding/reseeding.
  snapshot_sha256: 9846d19bb6bdbd5d99b1d0193039d86c2b4f6f45638e01f9bd98c9f1252be6b7
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv
  locator: ARO row354; PubChem row119; extractor/enricher/seeder ownership
  accessed_at: '2026-10-21T14:18:43Z'
  support: supports
  summary: ARO owns the definition, class, adopted PMID and xrefs; PubChem owns the
    complete native chemical_structure. The initial generic ChEBI owner list was replaced
    in the expanded target description by the actual ARO/PubChem owners, while all
    original captured bytes/hashes were preserved. No exact native ChEBI seed row,
    target/resistance source edge or producer join was found in the inspected source
    subsets.
  snapshot_sha256: 9846d19bb6bdbd5d99b1d0193039d86c2b4f6f45638e01f9bd98c9f1252be6b7
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Exact structure, nomenclature, source evidence and optional fields
  accessed_at: '2026-10-21T14:18:43Z'
  support: supports
  summary: A named stereodefined natural product must retain its known chemical identity.
    Unassigned stereochemistry is not evidence of a racemate. Missing optional primary-target
    or assay fields alone are not native defects; original compound and experimental
    endpoint boundaries must be preserved.
- evidence_id: chemistry
  kind: validation
  reference: Independent batch019 RDKit against batch035 cwd
  locator: 346348-focused.py;348-chemistry.json
  accessed_at: '2026-10-21T14:18:43Z'
  support: supports
  summary: 'Native SMILES and InChI agree on neutral C31H32N2O12, key JURYCYSCKRZQLD-UHFFFAOYSA-N,
    average mass 624.599 and exact mass 624.195524. All four potential sugar stereocentres
    are unassigned: native SMILES zero-based atoms 9,10,11 and 14. Formula, charge,
    rounded masses and minted identifier reproduce; valid parsing does not recover
    the missing configuration.'
  snapshot_sha256: 36dd4d92f5be799f426b90e87fe0fef212844864e9daeca3949d68432e7ff9fc
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/76173558/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: CID76173558 complete property response
  accessed_at: '2026-10-21T14:11:07.977722Z'
  support: context_only
  summary: Current PubChem agrees exactly with the native graph and lacks all four
    sugar assignments. This verifies the source of the incomplete graph, not the stereochemical
    identity of the material characterized in the original paper.
  snapshot_sha256: 913b8023d598556ed0cb540e4b6817acf228d1b658023d1e786158686701b8ee
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/206681/
  locator: CHEBI:206681 current names, formula, default InChI/key, origin and ontology
    parents
  accessed_at: '2026-10-21T14:11:07.977624Z'
  support: context_only
  summary: Current ChEBI also has the same stereochemically unassigned InChI/key and
    an unstereospecified systematic name. Its submitted aromatic SMILES has a pyrrole
    encoding problem, but that string is not the native representation and is not
    raised as a native defect. Its broad glycoside/coumarin classification agrees
    with constitution but does not supply the missing configuration.
  snapshot_sha256: 590a746d3344add668eca1d75d68aa3c0871e5572cc1103c3aafcefe5cbacc99
- evidence_id: aro
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3004718
  locator: ARO:3004718 and native definition/class/xrefs
  accessed_at: '2026-10-21T14:11:08.524421Z'
  support: context_only
  summary: The live ARO term reproduces the definition, including crenelated, and
    the exact adopted citation. The family class ARO:3000103 resolves. No compound-specific
    protein-target or resistance claim is asserted by this record.
  snapshot_sha256: 0e3001650362ab507822c410d0f057de4f13f4bbb3d2514bfcef7f640f645669
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.57.205
  locator: Adopted PMID:15152806; full five-page original, Methods/Results/Discussion
  accessed_at: '2026-10-21T14:11:39.961024Z'
  support: supports
  summary: The original separately isolates vanillobiocin, isovanillobiocin and declovanillobiocin
    from the cloQ-defective Streptomyces roseochromogenes DS12.976 culture. Declovanillobiocin
    is compound 3, lacks the aminocoumarin chlorine, and retains the 3-double-prime
    pyrrole ester and noviose scaffold. The aryl difference from clorobiocin is vanilloyl
    in place of prenylated 4-hydroxybenzoate. The native word crenelated does not
    name that group.
  snapshot_sha256: b9a15e77107aabb75c51748ca67a6a974de2882e2ffef9add1820d54f95dabce
- evidence_id: structure-figure
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.57.205
  locator: Actual Figure2, page208, visually inspected with compound3 substituent
    row
  accessed_at: '2026-10-21T14:18:43Z'
  support: supports
  summary: 'Figure2 depicts a defined sugar ring with oriented substituents: anomeric
    aromatic glycoside, free hydroxy, pyrrole ester and methoxy. The same scaffold
    is used for all three products, with the declovanillobiocin row specifying ester
    at3-double-prime, free2-double-prime hydroxy and no aminocoumarin chlorine. The
    native graph retains connectivity but none of the four sugar configurations.'
  snapshot_sha256: ebfe0bfcb82fa310a896f07cf04ae377bde712ab1bf990259ad2bba556e2e951
- evidence_id: nmr-table
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.57.205
  locator: Actual Table1, page207, visually inspected; structural elucidation text
  accessed_at: '2026-10-21T14:18:43Z'
  support: supports
  summary: Original1H NMR data distinguish compound 3 from the chlorinated analogues
    and compare its sugar resonances with authentic clorobiocin. The paper does not
    describe four independently randomized centres or a stereoisomer mixture. The
    figures and assigned noviose scaffold support completion of known stereochemistry;
    this review does not independently reassign absolute configuration from raw spectra.
  snapshot_sha256: 1f373719f4cecd2ed1886dc18e6342628ced53f93d4f95a54828ec2fbc1f2b54
- evidence_id: assay
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.57.205
  locator: Bioassay Methods, page206; actual Figure3 on page208; activity Results
  accessed_at: '2026-10-21T14:18:43Z'
  support: supports
  summary: Separately isolated compound 3 was dissolved in methanol and applied at
    8,16 and 32 nmol to 3-mm paper discs on nutrient agar containing approximately
    2×10^5 Bacillus subtilis ATCC14893 spores/mL. After 30 minutes drying and overnight
    incubation at 37 C, inhibition-zone diameters were compared with authentic clorobiocin
    and novobiocin. Declovanillobiocin relative activity is 1.5-3% with clorobiocin
    set to 100%. These are comparative disc-diffusion observations, not MICs, direct
    binding or clinical efficacy.
  snapshot_sha256: ebfe0bfcb82fa310a896f07cf04ae377bde712ab1bf990259ad2bba556e2e951
- evidence_id: producer
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.57.205
  locator: Fermentation/isolation Methods and Results, pages205-207; final discussion
    scope
  accessed_at: '2026-10-21T14:11:39.961024Z'
  support: supports
  summary: The production culture was incubated at 33 C for 9 days. Acidified broth
    extraction, Sephadex and preparative HPLC separately yielded 0.4 mg declovanillobiocin
    from 800 mL. The primary context is a cloQ-defective engineered strain; wild type
    did not accumulate detectable vanillobiocins. A separate cloR mutant also lacked
    their accumulation. One discussion sentence says cloR where title, abstract, Methods
    and Results consistently identify cloQ; retain that source typo instead of changing
    the supported producer genotype.
  snapshot_sha256: b9a15e77107aabb75c51748ca67a6a974de2882e2ffef9add1820d54f95dabce
- evidence_id: target-boundary
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.57.205
  locator: Introduction and biological-assay section
  accessed_at: '2026-10-21T14:11:39.961024Z'
  support: context_only
  summary: The introduction names bacterial DNA gyrase as the target of clorobiocin
    and cites earlier parent-family experiments. This paper measures declovanillobiocin
    bacterial growth zones and structure; it does not demonstrate exact-compound gyrase
    binding, ATPase inhibition, an allele-specific resistance mechanism or a causal
    chain. Family inference should not be promoted to a direct target annotation.
  snapshot_sha256: b9a15e77107aabb75c51748ca67a6a974de2882e2ffef9add1820d54f95dabce
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 348-adapter.json and348-adapter-network.json; query before protein-mechanism
    web follow-up
  accessed_at: '2026-10-21T14:18:43Z'
  support: context_only
  summary: The initial structured e_coli/precise1k/gyrB query failed with sandbox
    DNS, then the authorized public-network retry succeeded with b3699/gyrB and zero
    modules. This is gene annotation context, not declovanillobiocin binding or resistance.
    No source absence is inferred from the initial failure.
  snapshot_sha256: 139a8aeed59d5fd9b66fc2b3f58c823facfc18c32906aabb058f2d82b85027e8
- evidence_id: search
  kind: search
  reference: Ignored-inclusive repository search and public primary retrieval
  locator: 346348-local-focused.txt;348-discovery.json;346348-fetch1-3.json
  accessed_at: '2026-10-21T14:11:08.688014Z'
  support: context_only
  summary: The sole adopted original was retrieved freely from J-STAGE and fully read.
    Additional hits were database/review context, not new exact-compound target experiments.
    All native xrefs were checked through current official sources. No paid source
    or third-party contact was used.
  snapshot_sha256: 83c0881bc0bbc402754a34c9790fcc834db9ce025c775ca7f24ea5d71b9e00f9
  search_scope: 2026-10-21; exact declovanillobiocin label, ARO:3004718, CHEBI:206681,
    CID76173558, native molecular key and PMID15152806. Local searches included hidden
    and ignored files. Public primary follow-up was bounded and is not a claim that
    no further evidence exists.
- evidence_id: gates
  kind: validation
  reference: Actual focused native checks
  locator: 348-focused-results.json;348-schema.log;348-strict.log
  accessed_at: '2026-10-21T14:18:43Z'
  support: supports
  summary: Schema, strict and chemistry checks all exit 0. The omitted sugar stereochemistry
    is internally consistent across the source identifiers and therefore survives
    those gates.
  snapshot_sha256: 2116b5ca779c30f356c99bb4825102944ed6902875a31fe936eaf8d9290a6f2b
assessments:
- assessment_id: identity
  area: identity
  topic: Defined noviose-containing product versus native partial graph
  outcome: concern
  summary: The original Figure2 and structural comparison identify a stereodefined
    sugar scaffold, while the native graph omits all four centres. This is incomplete
    exact identity, not proof of a racemic or mixed preparation. Connectivity, charge
    and formula are coherent.
  target_ids:
  - antibioticmech:aro-cb28770ae8
  evidence_ids:
  - chemistry
  - structure-figure
  - nmr-table
  - primary
  - rubric
- assessment_id: groundings
  area: grounding
  topic: ARO, ChEBI and PubChem exact links
  outcome: supported
  summary: All three asserted xrefs resolve and match the current source identity/partial
    graph. The upstream agreement does not fill the known stereochemical gap. Any
    authorized structure completion must reconcile the partial database groundings
    explicitly.
  target_ids:
  - antibioticmech:aro-cb28770ae8
  evidence_ids:
  - aro
  - chebi
  - pubchem
  - chemistry
- assessment_id: definition
  area: evidence
  topic: Structural comparator wording and adopted source
  outcome: concern
  summary: The sole original directly supports vanilloyl substitution and loss of
    aminocoumarin chlorine, but its word is prenylated, not crenelated. The native
    miswording is inherited from ARO.
  target_ids:
  - antibioticmech:aro-cb28770ae8
  evidence_ids:
  - primary
  - aro
  - structure-figure
- assessment_id: classification-activity
  area: scope
  topic: Antibacterial eligibility and optional activity_spectrum
  outcome: supported
  summary: Exact isolated declovanillobiocin has measurable B. subtilis disc-diffusion
    activity. Relative zone-based potency cannot be converted into a MIC or a species-wide
    clinical susceptibility conclusion. Optional numerical enrichment should retain
    the stated disc amount, medium, strain and endpoint.
  target_ids:
  - antibioticmech:aro-cb28770ae8
  evidence_ids:
  - assay
  - primary
  - rubric
- assessment_id: targets-resistance
  area: completeness
  topic: Optional mechanism, target and resistance fields
  outcome: unknown
  summary: No native target or resistance annotation is populated. The original assays
    do not establish direct declovanillobiocin gyrase binding or resistance alleles,
    and structured annotation of gyrB does not close that evidence gap.
  target_ids:
  - antibioticmech:aro-cb28770ae8
  evidence_ids:
  - native
  - target-boundary
  - adapter
- assessment_id: producer
  area: provenance
  topic: Optional producer annotation
  outcome: supported
  summary: The isolated compound comes from the engineered cloQ-defective DS12.976
    strain under the reported fermentation; this is not interchangeable with ordinary
    wild-type production. The isolated cloR discussion typo is retained as a source
    limitation.
  target_ids:
  - antibioticmech:aro-cb28770ae8
  evidence_ids:
  - producer
  - primary
- assessment_id: other
  area: scope
  topic: Clinical products, causal graph, datasets and synonyms
  outcome: not_applicable
  summary: No native clinical product, approval, causal graph, dataset or synonym
    assertion is populated. The source establishes laboratory activity and production,
    not human use.
  target_ids:
  - antibioticmech:aro-cb28770ae8
  evidence_ids:
  - native
  - assay
- assessment_id: ownership
  area: provenance
  topic: Actual source ownership and generated history
  outcome: supported
  summary: The three seeding/reseeding events and SEEDED status are coherent. Initial
    captures are preserved; ARO owns definition/class/xrefs and PubChem owns structure,
    with exact transformation owners recorded for reproducibility.
  target_ids:
  - antibioticmech:aro-cb28770ae8
  evidence_ids:
  - native
  - owners
- assessment_id: checks
  area: schema
  topic: Focused gates
  outcome: supported
  summary: All actual focused checks pass. They establish internal encoding consistency,
    not completeness of experimental stereochemical identity.
  target_ids:
  - antibioticmech:aro-cb28770ae8
  evidence_ids:
  - gates
  - chemistry
findings:
- finding_id: F1
  issue_key: declovanillobiocin-missing-noviose-stereochemistry
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: All four sugar stereocentres are omitted from the named natural-product graph
  description: The original Figure2 defines the noviose scaffold of isolated declovanillobiocin,
    supported by its NMR comparison with the related products and clorobiocin. Native
    SMILES and InChI instead leave all four stereocentres unassigned, matching the
    incomplete PubChem/ChEBI encoding. This broader partial graph does not retain
    the exact characterized compound. Recover and verify the original sugar configuration
    through maintained ownership; do not infer a racemate or fill centres by arbitrary
    enumeration.
  target_ids:
  - antibioticmech:aro-cb28770ae8
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  evidence_ids:
  - chemistry
  - structure-figure
  - nmr-table
  - primary
  - pubchem
  - chebi
  - owners
  - rubric
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted unstereospecified chemical structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated chemical_structure
  rule_id: native-review-checklist:Identity
  native_severity: major incomplete exact stereochemical identity
  normalization_reason: The graph is chemically valid and has the correct constitution,
    but it omits known defining stereochemistry rather than specifying a confirmed
    opposite isomer.
- finding_id: F2
  issue_key: declovanillobiocin-prenylated-definition-term
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The definition misnames the clorobiocin prenylated aryl group
  description: The original repeatedly describes prenylated 4-hydroxybenzoic acid,
    whose dimethylallyl substituent is shown in Figure1. The native ARO-derived definition
    says crenelated, which is not the chemical group. Correct this source wording
    while retaining the supported vanillic-acid and chlorine comparisons.
  target_ids:
  - antibioticmech:aro-cb28770ae8
  field_paths:
  - definition
  evidence_ids:
  - primary
  - aro
  - owners
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition
  rule_id: native-review-checklist:Evidence
  native_severity: minor inherited structural terminology error
  normalization_reason: The mistaken word obscures a specific structural comparison
    but does not change the otherwise supported formula or compound connectivity.
actions:
- action_id: A1
  description: Recover the four defined sugar configurations and reconcile all final
    molecular encodings.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-cb28770ae8
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted unstereospecified chemical structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated chemical_structure
  acceptance_checks:
  - Map each sugar centre to original Figure2 and verify the noviose configuration
    and 3-double-prime ester position against Table1 and the primary comparator structures.
  - Generate mutually consistent stereospecific SMILES, InChI and key while preserving
    formula, charge and connectivity.
  - Qualify or resolve upstream partial graph links explicitly rather than silently
    treating unspecified and assigned structures as identical.
  - Use maintained curation/source ownership and pass required chemistry, schema,
    corpus, provenance and history checks.
- action_id: A2
  description: Correct the inherited structural term to prenylated.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-cb28770ae8
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition
  acceptance_checks:
  - Match the primary structural description and retain its correct compound comparisons.
  - Keep the source correction reproducible through extraction/seeding and required
    validation.
- action_id: A3
  description: Optionally add the original phenotype and engineered-producer evidence.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-cb28770ae8
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/declovanillobiocin.yaml
    role: Curator-owned optional primary evidence/history
  acceptance_checks:
  - Record B. subtilis ATCC14893 disc diffusion with 8/16/32 nmol dosing and relative
    activity 1.5-3%; do not convert it to MIC.
  - Distinguish the cloQ-defective DS12.976 production context from wild type and
    from the separate cloR mutant experiment.
  - Do not assign direct gyrase binding or a resistance mechanism from the clorobiocin
    introduction or a gene-source query.
limitations:
- The full adopted 2004 original was read, with actual Figure2, Figure3 and Table1
  visually inspected. Raw NMR data and a new absolute-configuration analysis were
  not independently reconstructed. The correction requires explicit mapping of the
  four known sugar centres; no arbitrary stereoisomer key is proposed.
- The direct activity evidence is relative disc diffusion. No declovanillobiocin MIC,
  direct gyrase-binding assay, resistance genotype or clinical efficacy measurement
  was established from the inspected source.
- The producer paper has a cloR/cloQ typo in one discussion sentence and a neighboring
  isovanillobiocin positional-comparison typo. Its repeated Methods/Results and Figure2
  supply the bounded compound/producer mapping; those isolated sentences are not imported
  literally.
- Current ChEBI/PubChem agree with the partial graph. ChEBI’s separate malformed aromatic
  SMILES is not native and was not turned into an extra native finding.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record, source, status or history was edited.
- Schema/strict used batch035; standalone RDKit used existing batch019 against batch035
  cwd.
- Optional links, tags, notes and finding field paths were checked against this exact
  compound.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://pubchem.ncbi.nlm.nih.gov/compound/76173558
- https://doi.org/10.7164/antibiotics.57.205
- https://card.csu.mcmaster.ca/ontology/42773
tags:
- declovanillobiocin
- noviose-stereochemistry
- disc-diffusion
- engineered-producer
```
