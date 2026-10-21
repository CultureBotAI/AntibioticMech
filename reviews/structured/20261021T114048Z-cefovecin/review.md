# Cefovecin: correct native Z oxime with an E-oxime exact cross-reference

- Review: 20261021T114048Z-cefovecin
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:21:26Z
- Finished UTC: 2026-10-21T11:40:48Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One major exact-xref defect and one minor definition/provenance defect. The native neutral (6R,7R), tetrahydrofuranyl 2S, Z-oxime structure is coherent and matches PubChem. ChEMBL2110625 and the current ARO displayed SMILES instead encode the E oxime. The definition inherits a Pasteurella spelling error and cites an E. coli resistance survey for treatment-specific claims that are supported by a different source, the official cefovecin sodium product label. Salt/formulation and assay scopes remain separate from the neutral molecule.

## Scope And Provenance

Whole-record review of neutral cefovecin, including its definition citation and all exact cross-references.

Selection: Queue 239 in isolated batch 024; preserved initial captures and appended actual ARO/PubChem owners before detailed judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-c73757ed91 | data/antibiotics/antibacterial/cefovecin.yaml | generated | cefovecin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | antibioticmech:aro-c73757ed91 | Actual focused command passed with zero errors. |
| Focused strict | passed | True | antibioticmech:aro-c73757ed91 | Actual focused command passed with zero errors. |
| Supplemental native molecular encodings and source mint | passed | False | antibioticmech:aro-c73757ed91 | Both native encodings reproduce the complete key, formula, neutral charge, masses, three assigned centres and source mint. This does not validate the external ChEMBL structure. |
| Independent native versus ChEMBL stereochemical comparison | passed | False | antibioticmech:aro-c73757ed91 | Comparison ran successfully and exposed the scientific mismatch: native oxime Z versus ChEMBL oxime E across SMILES, InChI and molfile, with matching connectivity and core centres. |
| Authoritative full QC | failed | True | antibioticmech:aro-c73757ed91 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-c73757ed91 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-c73757ed91 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-c73757ed91 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-c73757ed91 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-c73757ed91 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-c73757ed91 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-c73757ed91 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-c73757ed91 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Correct neutral native molecule

identity: supported. Targets: antibioticmech:aro-c73757ed91.

Native encodings and current PubChem agree on 6R,7R, oxolanyl 2S, Z oxime and complete formula/key. The minted ARO identifier and three-event history are coherent; no native molecular rewrite is warranted.

### External stereochemical equivalence

grounding: concern. Targets: antibioticmech:aro-c73757ed91.

Retained ChEMBL exact xref encodes the E oxime in three molecular representations. ARO displays that same E SMILES while also linking the correct PubChem Z form. Source provenance must remain traceable while exact equivalence is corrected.

### Clinical-use wording, spelling and citation

evidence: concern. Targets: antibioticmech:aro-c73757ed91.

The drug-use concept is independently supported for susceptible pathogens under the sodium-product label. The native Pasturella misspelling and its sole PMID attribution need correction; an E. coli surveillance study does not establish those specific treatment indications.

### Cephalosporin and antibacterial filing

grounding: supported. Targets: antibioticmech:aro-c73757ed91.

Structural framework, live parent term, original antibacterial study and official sodium-product label support filing/class. No additional role slot is required solely because it is empty.

### Source opportunities and boundaries

evidence: unknown. Targets: antibioticmech:aro-c73757ed91.

Native has no numeric observations or resistance assertions. The adopted survey provides phenotype/genotype leads but contains assay-reporting and denominator limitations; additional primary abstracts and product trial results require material/host/panel qualification before enrichment.

### Absent native molecular/pathway claims

scope: not_applicable. Targets: antibioticmech:aro-c73757ed91.

Native names no protein, pathway, regulator or transcriptomics dataset, so structured-source adapter has no native candidate. No direct PBP binding claim is inferred from label/class prose, and quinolone resistance targets are not transferred to cefovecin.

### Producer, clinical objects, graph and dataset

scope: not_applicable. Targets: antibioticmech:aro-c73757ed91.

No native producer, structured clinical-status, causal-graph or dataset object is present. Generic veterinary-use definition is reviewed separately; no human indication or current product approval assertion is added.

### Actual ARO/PubChem ownership

provenance: supported. Targets: antibioticmech:aro-c73757ed91.

Original capture hashes preserved; actual ARO and PubChem owners appended. Source mint and seed/reseed history match. Definition and xref corrections belong to maintained source inputs, not an isolated generated-record edit.

### Optional enrichment

completeness: supported. Targets: antibioticmech:aro-c73757ed91.

Concrete activity/clinical source leads exist, with explicit limits; absent optional fields are not findings. Exact-xref and citation defects are populated assertions requiring correction.

### Native deterministic checks

schema: supported. Targets: antibioticmech:aro-c73757ed91.

Focused schema/strict and supplemental native molecular checks pass; scientific source discrepancies remain.

## Findings

### F1: The exact ChEMBL cross-reference encodes the opposite oxime geometry

major / open / confirmed; issue key: aro-3007458-cefovecin-chembl2110625-oxime-geometry.

Native/PubChem cefovecin is Z at its methoxyimino C=N, whereas retained CHEMBL2110625 encodes E in its canonical SMILES, Standard InChI and molfile. Formula, connectivity and all three tetrahedral centres agree, so name/formula matching would miss this stereoisomer mismatch. Current ARO also displays the ChEMBL E SMILES. Preserve the correct native PubChem-derived structure and ARO provenance; adjudicate the exact ChEMBL link and document the upstream ARO representation conflict rather than replacing native Z with E.

### F2: The definition has a genus typo and an unsuitable treatment-specific citation

minor / open / confirmed; issue key: aro-3007458-cefovecin-definition-citation-and-taxonym.

The definition spells Pasteurella as Pasturella and cites PMID 37107106 for feline Pasteurella/canine staphylococcal skin-treatment claims. That original paper studies E. coli resistance in companion animals, not those treatment indications. The official sodium-product label independently supports qualified susceptible-pathogen indications, so the needed change is accurate spelling and appropriately scoped provenance rather than removal of the supported veterinary-use concept.

## Recommended Actions And Acceptance Checks

### A1

Correct exact xref applicability through source adjudication while preserving native Z cefovecin.

- Exclude or correct the CHEMBL2110625 exact-equivalence assertion until an inspected source represents the native Z structure. The bounded native-key query returned no replacement; do not guess one.
- Retain ARO:3007458 as provenance and document its displayed E versus linked PubChem Z conflict under the repository’s supported source-adjudication policy. Do not silently change the native molecular structure to match ChEMBL.
- Re-extract/reseed only through maintained owners; verify every surviving exact xref agrees on 6R,7R, tetrahydrofuranyl 2S and Z oxime, full key and charge/formula.
- Run schema/strict and applicable xref, term, history and corpus validation after separately authorized curation.

### A2

Repair source-owned definition spelling and evidence placement.

- Correct Pasturella to Pasteurella and cite a source that explicitly supports the claimed veterinary indications. Preserve susceptible-strain and sodium-product context; avoid implying all Staphylococcus infections are indicated.
- Use official label Description/Indications or directly inspected primary treatment studies for treatment-use support. Retain PMID 37107106 only for the E. coli survey context it actually measures.
- Confirm source-owned changes survive reseeding without rewriting the correct neutral PubChem structure; validate native schema/strict and provenance/history.

### A3

Optionally enrich activity/resistance only after resolving exact material and survey limitations.

- For PMID 37107106 resolve cefovecin-specific MIC/breakpoint methodology and the 89 versus 90 and 70 versus 78 dog-isolate discrepancies before importing quantitative genotype relationships.
- Preserve Korean 2018–2019 isolate selection; associated CTX-M/CMY genes do not by themselves establish individual-enzyme kinetics. gyrA/parC/PMQR results concern quinolone resistance.
- Inspect the 2006 original study’s full methods and reagent identity before neutral-form numeric activity transfer. Keep sodium formulation trials and aggregate MIC90 separate from exact single-isolate observations.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cefovecin.yaml; Entire YAML | supports | Read identifier, label, MINTED/SEEDED/class status, definition and PMID source, cephalosporin parent/class, all molecular fields, three exact xrefs, ARO source concept/mint and all three seed/reseed events. No native quantitative activity, mode, molecular target, resistance, producer, clinical-status, dataset or causal-graph object is populated. |
| owners | data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv;curation/ncbi_ast_drug_map.tsv; ARO row 413; PubChem row 149; AST map row 18 | supports | ARO owns definition, class and ChEMBL/PubChem cross-reference adoption. PubChem inventory owns the native complete structure. AST map is additional context that explicitly distinguishes the neutral active moiety from sodium formulation; it is not an activity-measurement owner. Original captures naming ChEBI generically were preserved while actual ARO/PubChem owners were appended. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md;docs/HARMONIZATION.md; Identity, Equivalence, Evidence standard and maintained ownership | supports | An exact xref must denote the same stereochemical structure, and citations must support the narrow claim. InChI differences alone are insufficient; the present finding is supported by explicit opposite oxime configurations in multiple encodings. |
| chemistry | RDKit 2026.03.5 native molecular checks; 239-chemistry.json | supports | Both native encodings produce ZJGQFXVQDVCVOK-QFKLAVHZSA-N, C17H19N5O6S2, one neutral fragment, masses within reported precision and R,R,S assigned centres. The SHA256-derived ARO mint agrees. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6336480/JSON; Full current CID 6336480 structure and systematic name | supports | Current PubChem matches the exact neutral native InChI/key, formula, complete stereochemical SMILES and (6R,7R), (2Z), tetrahydrofuranyl 2S name. No sodium ion or formulation is introduced. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL2110625.json; Full ChEMBL structure, molfile and hierarchy | refutes | Named cefovecin entry CHEMBL2110625 has the same formula and tetrahedral configuration but standard InChI /b21-10+ and key ZJGQFXVQDVCVOK-MSUXKOGISA-N. Its canonical SMILES and molfile encode the E oxime, unlike the native/PubChem /b21-10- Z oxime. |
| xref-stereo | Independent native/ChEMBL graph comparison; 239-xref-check.py and 239-xref-check.json | refutes | RDKit identifies native oxime STEREOZ and ChEMBL SMILES, InChI and molfile STEREOE. ChEMBL SMILES/molfile share the native connectivity after stereo removal and all three R,R,S tetrahedral centres, but chirality-aware structure matching fails. The discrepancy is specifically oxime geometry, not a tautomer-only or mass-rounding difference. |
| aro | https://card.mcmaster.ca/aro/3007458; Complete current cefovecin entry | partial | Current ARO retains the same name, definition, PMID 37107106 and PubChem/ChEMBL links. Its displayed SMILES is identical to the ChEMBL E-oxime SMILES. The ARO identifier remains traceable source provenance, but its displayed molecular representation is not exact proof for the native Z form. |
| parent | https://card.mcmaster.ca/aro/0000032; Drug-class identity | supports | ARO:0000032 resolves cephalosporin and is broader than this individual molecule. The native beta-lactam/cephem structure and original activity source support the structural class; class-level prose is not substituted for a compound-specific target experiment. |
| definition-source | PMID:37107106; DOI 10.3390/antibiotics12040745; full main text, Results/Table 1, Discussion and Methods | partial | Original 2023 Korean survey reports cefovecin resistance among 836 E. coli isolates from diseased dogs and cats collected in 2018–2019. It studies E. coli susceptibility and associated resistance genotypes, not treatment of Pasteurella multocida in cats or staphylococcal skin infections in dogs. Those definition-specific indications are not established by this cited experiment. |
| survey-limits | DOI:10.3390/antibiotics12040745; Methods 4.3; Results 2.2, Tables 1/3/4 | partial | Methods names Sensititre COMPGN1F and broth microdilution, but its enumerated drug list omits cefovecin; no exact salt or cefovecin-specific breakpoint value is stated there. Results 2.2 says 89 isolates with 70 dogs plus 11 cats, while Table 3 says 78 dogs plus 11 cats; Table 1 gives 90 co-resistant isolates. These limits need resolution before quantitative genotype-linked enrichment. Quinolone gyrA/parC observations are not cefovecin target mechanisms. |
| label | https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2daeaf25-f98f-49d3-943c-f604a844d93c; CONVENIA SPL version 7, published 2022-12-12; Description, Indications, Microbiology, Effectiveness | supports | Official label explicitly names the sodium salt with (6R,7R), (2Z), tetrahydrofuranyl 2S configuration, formulated as cefovecin-equivalent strength. Indications are susceptible S. intermedius/S. canis canine skin infections and susceptible Pasteurella multocida feline wounds/abscesses. This supports the qualified drug-use concept and correct spelling, not an unqualified statement that neutral powder is the marketed formulation. |
| label-trials | https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/2daeaf25-f98f-49d3-943c-f604a844d93c.xml; Effectiveness Tables 7/8 and formulation description | supports | Label reports controlled sodium-product field trials: canine clinical success 109/118 versus 108/117 control and feline 86/89 versus 80/88. These are product-, host- and study-specific outcomes, not organism MICs or the same denominator as all enrolled animals. Generic PBP prose is regulatory context rather than a newly inspected purified-target experiment. |
| activity-primary | PMID:16801403; DOI 10.1128/AAC.00077-06; inspected original abstract | partial | Original 2006 study tested 2641 canine/feline clinical isolates by CLSI broth microdilution and reports cefovecin MIC90 values 0.25 µg/mL for S. intermedius, 1.0 for E. coli and 0.06 for P. multocida. Supports antibacterial spectrum with exact panel scope; full methods/reagent form were not accessible, so no unqualified neutral-form quantitative transfer is proposed. |
| canine-trial | PMID:18673028; DOI 10.2460/javma.233.3.433; original abstract | partial | Randomized positive-controlled canine skin-infection trial reports 109/118 cefovecin and 108/117 cefadroxil treatment successes. It supports clinical use under study conditions, with full formulation and methods still requiring source inspection before numeric curation. |
| feline-trial | PMID:17725587; DOI 10.1111/j.1748-5827.2007.00390.x; original abstract | partial | Randomized feline abscess/wound study compares injected cefovecin with oral amoxicillin/clavulanate; efficacy was reported as comparable. This is a separate clinical-use lead, not a biochemical target measurement or exact neutral reagent declaration. |
| chembl-search | https://www.ebi.ac.uk/chembl/api/data/molecule.json?molecule_structures__standard_inchi_key=ZJGQFXVQDVCVOK-QFKLAVHZSA-N; Exact complete-key lookup | context_only | The current exact native-key query returned total_count 0. No replacement ChEMBL identifier is guessed; this is a bounded API result, not proof that no alternative representation exists anywhere. |
| access | Free PMC/Europe PMC/publisher retrieval; 239-more-fetch-results.json;239-alt-fetch-results.json;239-PMC1489759.html | context_only | The 2006 full-text XML endpoint returned 500, PMC returned a browser CAPTCHA, and ordinary Europe PMC PDF/publisher routes returned 403. No full-text or figure inspection is claimed for that paper. |
| local-search | Ignored-inclusive local review search; 239-owner-hits.txt and 239-local-hits.txt | context_only | Searched exact identifier, label, slug, ARO ID and key across batch 024 including ignored/hidden files outside .git/.venv. Historical discovery/AST-mapping artifacts were used only as context; native and primary sources were inspected independently. |
| gates | Focused native validators; 239-focused-results.json | supports | Schema, strict and supplemental native chemistry each exit 0. None detects the current external ChEMBL oxime mismatch or definition citation scope. |

## Limits And Additional Notes

- The current ChEMBL exact-native-key API query returned no candidate; it does not exhaust every alternative representation or historical release. Upstream ARO/ChEMBL correction was not requested or performed.
- The 2006 activity study is abstract-only here: EPMC XML 500, PMC CAPTCHA and alternative Europe PMC/publisher 403 prevented full text. Additional canine/feline efficacy leads were also inspected at abstract level only.
- The adopted survey does not fully specify cefovecin reagent form or an explicit cefovecin breakpoint in Methods 4.3 and contains denominator discrepancies. No quantitative resistance or protein-target claim is transferred.
- The official CONVENIA source is a versioned sodium-product label. Its formulation, active-moiety strength, indication and trial results do not make the native neutral acid a pharmaceutical product.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 23 expanded input hashes unchanged, preserving original captures. No native/source/status/history edits.
- Focused validators used batch 024 own environment; standalone chemistry used existing batch 019 RDKit 2026.03.5 against batch 024 cwd.
- Free public retrieval only. No paid research, external contact or source mutation.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T114048Z-cefovecin
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefovecin: correct native Z oxime with an E-oxime exact cross-reference'
started_at: '2026-10-21T11:21:26Z'
finished_at: '2026-10-21T11:40:48Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent complete native and actual ARO/PubChem owner review;
    current exact structure comparison across PubChem, ChEMBL and ARO; full adopted
    2023 primary text; official label and additional original activity/efficacy abstracts.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One major exact-xref defect and one minor definition/provenance defect. The
  native neutral (6R,7R), tetrahydrofuranyl 2S, Z-oxime structure is coherent and
  matches PubChem. ChEMBL2110625 and the current ARO displayed SMILES instead encode
  the E oxime. The definition inherits a Pasteurella spelling error and cites an E.
  coli resistance survey for treatment-specific claims that are supported by a different
  source, the official cefovecin sodium product label. Salt/formulation and assay
  scopes remain separate from the neutral molecule.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
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
  - path: curation/ncbi_ast_drug_map.tsv
    sha256: 8b224448e1b2107e40107c4fb99820230249ec1318e36b032bb60324e1948088
    role: context
  - path: data/antibiotics/antibacterial/cefovecin.yaml
    sha256: 1a9d21184e216fe11d5206f7af421f4f15577de1e1e9ef5d4b1c7d93b2641d53
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
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
- target_id: antibioticmech:aro-c73757ed91
  path: data/antibiotics/antibacterial/cefovecin.yaml
  label: cefovecin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition, parent/class and citation lead
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted PubChem molecular structure and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusion overrides
scope:
  description: Whole-record review of neutral cefovecin, including its definition
    citation and all exact cross-references.
  selection: Queue 239 in isolated batch 024; preserved initial captures and appended
    actual ARO/PubChem owners before detailed judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-c73757ed91
  exclusions:
  - target: Cefovecin sodium, CONVENIA/SOLOVECIN formulations and E-oxime cefovecin
      representation
    reason: Distinct salt/product or stereochemical scope; drug-level use evidence
      does not establish exact neutral assay material.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual focused command passed with zero errors.
  target_ids:
  - antibioticmech:aro-c73757ed91
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefovecin.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual focused command passed with zero errors.
  target_ids:
  - antibioticmech:aro-c73757ed91
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefovecin.yaml --out /private/tmp/am-review-session/239-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Supplemental native molecular encodings and source mint
  status: passed
  required: false
  summary: Both native encodings reproduce the complete key, formula, neutral charge,
    masses, three assigned centres and source mint. This does not validate the external
    ChEMBL structure.
  target_ids:
  - antibioticmech:aro-c73757ed91
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/check199200.py
    239 (cwd /private/tmp/antibioticmech-record-reviews-024)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: xref-stereo
  name: Independent native versus ChEMBL stereochemical comparison
  status: passed
  required: false
  summary: 'Comparison ran successfully and exposed the scientific mismatch: native
    oxime Z versus ChEMBL oxime E across SMILES, InChI and molfile, with matching
    connectivity and core centres.'
  target_ids:
  - antibioticmech:aro-c73757ed91
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/239-xref-check.py
    (cwd /private/tmp/antibioticmech-record-reviews-024)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - xref-stereo
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-c73757ed91
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
  - antibioticmech:aro-c73757ed91
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
  - antibioticmech:aro-c73757ed91
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
  - antibioticmech:aro-c73757ed91
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
  - antibioticmech:aro-c73757ed91
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
  - antibioticmech:aro-c73757ed91
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
  - antibioticmech:aro-c73757ed91
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
  - antibioticmech:aro-c73757ed91
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
  - antibioticmech:aro-c73757ed91
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cefovecin.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T11:38:21Z'
  support: supports
  summary: Read identifier, label, MINTED/SEEDED/class status, definition and PMID
    source, cephalosporin parent/class, all molecular fields, three exact xrefs, ARO
    source concept/mint and all three seed/reseed events. No native quantitative activity,
    mode, molecular target, resistance, producer, clinical-status, dataset or causal-graph
    object is populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv;curation/ncbi_ast_drug_map.tsv
  locator: ARO row 413; PubChem row 149; AST map row 18
  accessed_at: '2026-10-21T11:38:21Z'
  support: supports
  summary: ARO owns definition, class and ChEMBL/PubChem cross-reference adoption.
    PubChem inventory owns the native complete structure. AST map is additional context
    that explicitly distinguishes the neutral active moiety from sodium formulation;
    it is not an activity-measurement owner. Original captures naming ChEBI generically
    were preserved while actual ARO/PubChem owners were appended.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md;docs/HARMONIZATION.md
  locator: Identity, Equivalence, Evidence standard and maintained ownership
  accessed_at: '2026-10-21T11:38:21Z'
  support: supports
  summary: An exact xref must denote the same stereochemical structure, and citations
    must support the narrow claim. InChI differences alone are insufficient; the present
    finding is supported by explicit opposite oxime configurations in multiple encodings.
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5 native molecular checks
  locator: 239-chemistry.json
  accessed_at: '2026-10-21T11:34:56Z'
  support: supports
  summary: Both native encodings produce ZJGQFXVQDVCVOK-QFKLAVHZSA-N, C17H19N5O6S2,
    one neutral fragment, masses within reported precision and R,R,S assigned centres.
    The SHA256-derived ARO mint agrees.
  snapshot_sha256: 0b4a225998bcb25ff59257885ca02fec1886983e809ee9369c0b375ebae24607
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6336480/JSON
  locator: Full current CID 6336480 structure and systematic name
  accessed_at: '2026-10-21T11:34:47Z'
  support: supports
  summary: Current PubChem matches the exact neutral native InChI/key, formula, complete
    stereochemical SMILES and (6R,7R), (2Z), tetrahydrofuranyl 2S name. No sodium
    ion or formulation is introduced.
  snapshot_sha256: e2c2e459ec44b7df8e51d12ea7656906fe375e2107f7bf2f774000f46a534d87
- evidence_id: chembl
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL2110625.json
  locator: Full ChEMBL structure, molfile and hierarchy
  accessed_at: '2026-10-21T11:34:47Z'
  support: refutes
  summary: Named cefovecin entry CHEMBL2110625 has the same formula and tetrahedral
    configuration but standard InChI /b21-10+ and key ZJGQFXVQDVCVOK-MSUXKOGISA-N.
    Its canonical SMILES and molfile encode the E oxime, unlike the native/PubChem
    /b21-10- Z oxime.
  snapshot_sha256: eef42c638307f0a0e1cec0b7789e36069e73b5daf9cbbe8d76b0c472d62914d4
- evidence_id: xref-stereo
  kind: validation
  reference: Independent native/ChEMBL graph comparison
  locator: 239-xref-check.py and 239-xref-check.json
  accessed_at: '2026-10-21T11:35:26Z'
  support: refutes
  summary: RDKit identifies native oxime STEREOZ and ChEMBL SMILES, InChI and molfile
    STEREOE. ChEMBL SMILES/molfile share the native connectivity after stereo removal
    and all three R,R,S tetrahedral centres, but chirality-aware structure matching
    fails. The discrepancy is specifically oxime geometry, not a tautomer-only or
    mass-rounding difference.
  snapshot_sha256: ab35a14cb03b6dc6351c186bf0bd1b25745a49d060fcd8e81753ef21beb5d1b3
- evidence_id: aro
  kind: authority
  reference: https://card.mcmaster.ca/aro/3007458
  locator: Complete current cefovecin entry
  accessed_at: '2026-10-21T11:34:47Z'
  support: partial
  summary: Current ARO retains the same name, definition, PMID 37107106 and PubChem/ChEMBL
    links. Its displayed SMILES is identical to the ChEMBL E-oxime SMILES. The ARO
    identifier remains traceable source provenance, but its displayed molecular representation
    is not exact proof for the native Z form.
  snapshot_sha256: a1bf5a849eaddaac6ffe40fd42e303d8c563659cbac21b30ce9968060af001c5
- evidence_id: parent
  kind: authority
  reference: https://card.mcmaster.ca/aro/0000032
  locator: Drug-class identity
  accessed_at: '2026-10-21T11:34:47Z'
  support: supports
  summary: ARO:0000032 resolves cephalosporin and is broader than this individual
    molecule. The native beta-lactam/cephem structure and original activity source
    support the structural class; class-level prose is not substituted for a compound-specific
    target experiment.
  snapshot_sha256: 02ffddbdf5a54f2f2dab9b057307671483f42a396086ba33936767bf224c0523
- evidence_id: definition-source
  kind: primary_source
  reference: PMID:37107106
  locator: DOI 10.3390/antibiotics12040745; full main text, Results/Table 1, Discussion
    and Methods
  accessed_at: '2026-10-21T11:35:12Z'
  support: partial
  summary: Original 2023 Korean survey reports cefovecin resistance among 836 E. coli
    isolates from diseased dogs and cats collected in 2018–2019. It studies E. coli
    susceptibility and associated resistance genotypes, not treatment of Pasteurella
    multocida in cats or staphylococcal skin infections in dogs. Those definition-specific
    indications are not established by this cited experiment.
  snapshot_sha256: fdb10ffc74620f289dba4f4dde33895c22a115e2959f6e541f43e74eb78da3a2
- evidence_id: survey-limits
  kind: primary_source
  reference: DOI:10.3390/antibiotics12040745
  locator: Methods 4.3; Results 2.2, Tables 1/3/4
  accessed_at: '2026-10-21T11:35:12Z'
  support: partial
  summary: Methods names Sensititre COMPGN1F and broth microdilution, but its enumerated
    drug list omits cefovecin; no exact salt or cefovecin-specific breakpoint value
    is stated there. Results 2.2 says 89 isolates with 70 dogs plus 11 cats, while
    Table 3 says 78 dogs plus 11 cats; Table 1 gives 90 co-resistant isolates. These
    limits need resolution before quantitative genotype-linked enrichment. Quinolone
    gyrA/parC observations are not cefovecin target mechanisms.
  snapshot_sha256: fdb10ffc74620f289dba4f4dde33895c22a115e2959f6e541f43e74eb78da3a2
- evidence_id: label
  kind: authority
  reference: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2daeaf25-f98f-49d3-943c-f604a844d93c
  locator: CONVENIA SPL version 7, published 2022-12-12; Description, Indications,
    Microbiology, Effectiveness
  accessed_at: '2026-10-21T11:35:12Z'
  support: supports
  summary: Official label explicitly names the sodium salt with (6R,7R), (2Z), tetrahydrofuranyl
    2S configuration, formulated as cefovecin-equivalent strength. Indications are
    susceptible S. intermedius/S. canis canine skin infections and susceptible Pasteurella
    multocida feline wounds/abscesses. This supports the qualified drug-use concept
    and correct spelling, not an unqualified statement that neutral powder is the
    marketed formulation.
  snapshot_sha256: b85471bbab3a0be13580b6ac83d10d9fd3924e3e09f0b9b486fafbebfb2a12bc
- evidence_id: label-trials
  kind: authority
  reference: https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/2daeaf25-f98f-49d3-943c-f604a844d93c.xml
  locator: Effectiveness Tables 7/8 and formulation description
  accessed_at: '2026-10-21T11:35:12Z'
  support: supports
  summary: 'Label reports controlled sodium-product field trials: canine clinical
    success 109/118 versus 108/117 control and feline 86/89 versus 80/88. These are
    product-, host- and study-specific outcomes, not organism MICs or the same denominator
    as all enrolled animals. Generic PBP prose is regulatory context rather than a
    newly inspected purified-target experiment.'
  snapshot_sha256: e2d17c5cfbf6c02f760ccf3312b0755e72fb517c7f6347f45dfc9174d36fe5ef
- evidence_id: activity-primary
  kind: primary_source
  reference: PMID:16801403
  locator: DOI 10.1128/AAC.00077-06; inspected original abstract
  accessed_at: '2026-10-21T11:34:48Z'
  support: partial
  summary: Original 2006 study tested 2641 canine/feline clinical isolates by CLSI
    broth microdilution and reports cefovecin MIC90 values 0.25 µg/mL for S. intermedius,
    1.0 for E. coli and 0.06 for P. multocida. Supports antibacterial spectrum with
    exact panel scope; full methods/reagent form were not accessible, so no unqualified
    neutral-form quantitative transfer is proposed.
  snapshot_sha256: 54673fbb208fbe9500cdb37c84b7483a55bf3f37fa69bf93d3f0a5527a6601d6
- evidence_id: canine-trial
  kind: primary_source
  reference: PMID:18673028
  locator: DOI 10.2460/javma.233.3.433; original abstract
  accessed_at: '2026-10-21T11:34:48Z'
  support: partial
  summary: Randomized positive-controlled canine skin-infection trial reports 109/118
    cefovecin and 108/117 cefadroxil treatment successes. It supports clinical use
    under study conditions, with full formulation and methods still requiring source
    inspection before numeric curation.
  snapshot_sha256: 54673fbb208fbe9500cdb37c84b7483a55bf3f37fa69bf93d3f0a5527a6601d6
- evidence_id: feline-trial
  kind: primary_source
  reference: PMID:17725587
  locator: DOI 10.1111/j.1748-5827.2007.00390.x; original abstract
  accessed_at: '2026-10-21T11:34:48Z'
  support: partial
  summary: Randomized feline abscess/wound study compares injected cefovecin with
    oral amoxicillin/clavulanate; efficacy was reported as comparable. This is a separate
    clinical-use lead, not a biochemical target measurement or exact neutral reagent
    declaration.
  snapshot_sha256: 54673fbb208fbe9500cdb37c84b7483a55bf3f37fa69bf93d3f0a5527a6601d6
- evidence_id: chembl-search
  kind: search
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule.json?molecule_structures__standard_inchi_key=ZJGQFXVQDVCVOK-QFKLAVHZSA-N
  locator: Exact complete-key lookup
  accessed_at: '2026-10-21T11:36:42Z'
  support: context_only
  summary: The current exact native-key query returned total_count 0. No replacement
    ChEMBL identifier is guessed; this is a bounded API result, not proof that no
    alternative representation exists anywhere.
  snapshot_sha256: c4e2727ca3ac5b893c5bd5ea8d918848a8174a41d53b6eafa4621fe5bcbe968c
  search_scope: 2026-10-21 free current official identifier, DailyMed and Europe PMC
    retrieval; exact native InChIKey ChEMBL query; rg --no-ignore --hidden across
    batch 024 outside .git/.venv. Native has no named protein/pathway assertion requiring
    a structured expression adapter.
- evidence_id: access
  kind: search
  reference: Free PMC/Europe PMC/publisher retrieval
  locator: 239-more-fetch-results.json;239-alt-fetch-results.json;239-PMC1489759.html
  accessed_at: '2026-10-21T11:35:54Z'
  support: context_only
  summary: The 2006 full-text XML endpoint returned 500, PMC returned a browser CAPTCHA,
    and ordinary Europe PMC PDF/publisher routes returned 403. No full-text or figure
    inspection is claimed for that paper.
  snapshot_sha256: 6fbf87ea2fe7202b52c5f7847ab9934f7f5fea946267e161b45798a86dc77c70
  search_scope: 2026-10-21 free current official identifier, DailyMed and Europe PMC
    retrieval; exact native InChIKey ChEMBL query; rg --no-ignore --hidden across
    batch 024 outside .git/.venv. Native has no named protein/pathway assertion requiring
    a structured expression adapter.
- evidence_id: local-search
  kind: search
  reference: Ignored-inclusive local review search
  locator: 239-owner-hits.txt and 239-local-hits.txt
  accessed_at: '2026-10-21T11:34:28Z'
  support: context_only
  summary: Searched exact identifier, label, slug, ARO ID and key across batch 024
    including ignored/hidden files outside .git/.venv. Historical discovery/AST-mapping
    artifacts were used only as context; native and primary sources were inspected
    independently.
  snapshot_sha256: 3cfbdbd99958b026e2b35dd194061d1b0401f965c3dd587f273f0ce6a68fb8f1
  search_scope: 2026-10-21 free current official identifier, DailyMed and Europe PMC
    retrieval; exact native InChIKey ChEMBL query; rg --no-ignore --hidden across
    batch 024 outside .git/.venv. Native has no named protein/pathway assertion requiring
    a structured expression adapter.
- evidence_id: gates
  kind: validation
  reference: Focused native validators
  locator: 239-focused-results.json
  accessed_at: '2026-10-21T11:34:57Z'
  support: supports
  summary: Schema, strict and supplemental native chemistry each exit 0. None detects
    the current external ChEMBL oxime mismatch or definition citation scope.
  snapshot_sha256: ecdacad3b84e69542a804c092cb6357d8cb0e1e7dc3fedb30f56937227afa476
assessments:
- assessment_id: identity
  area: identity
  topic: Correct neutral native molecule
  outcome: supported
  summary: Native encodings and current PubChem agree on 6R,7R, oxolanyl 2S, Z oxime
    and complete formula/key. The minted ARO identifier and three-event history are
    coherent; no native molecular rewrite is warranted.
  target_ids:
  - antibioticmech:aro-c73757ed91
  evidence_ids:
  - native
  - chemistry
  - pubchem
- assessment_id: xref
  area: grounding
  topic: External stereochemical equivalence
  outcome: concern
  summary: Retained ChEMBL exact xref encodes the E oxime in three molecular representations.
    ARO displays that same E SMILES while also linking the correct PubChem Z form.
    Source provenance must remain traceable while exact equivalence is corrected.
  target_ids:
  - antibioticmech:aro-c73757ed91
  evidence_ids:
  - chembl
  - xref-stereo
  - aro
  - pubchem
  - rubric
- assessment_id: definition
  area: evidence
  topic: Clinical-use wording, spelling and citation
  outcome: concern
  summary: The drug-use concept is independently supported for susceptible pathogens
    under the sodium-product label. The native Pasturella misspelling and its sole
    PMID attribution need correction; an E. coli surveillance study does not establish
    those specific treatment indications.
  target_ids:
  - antibioticmech:aro-c73757ed91
  evidence_ids:
  - native
  - aro
  - definition-source
  - label
- assessment_id: classification
  area: grounding
  topic: Cephalosporin and antibacterial filing
  outcome: supported
  summary: Structural framework, live parent term, original antibacterial study and
    official sodium-product label support filing/class. No additional role slot is
    required solely because it is empty.
  target_ids:
  - antibioticmech:aro-c73757ed91
  evidence_ids:
  - parent
  - pubchem
  - activity-primary
  - label
- assessment_id: activity-resistance
  area: evidence
  topic: Source opportunities and boundaries
  outcome: unknown
  summary: Native has no numeric observations or resistance assertions. The adopted
    survey provides phenotype/genotype leads but contains assay-reporting and denominator
    limitations; additional primary abstracts and product trial results require material/host/panel
    qualification before enrichment.
  target_ids:
  - antibioticmech:aro-c73757ed91
  evidence_ids:
  - definition-source
  - survey-limits
  - activity-primary
  - canine-trial
  - feline-trial
  - label-trials
- assessment_id: mechanism-adapter
  area: scope
  topic: Absent native molecular/pathway claims
  outcome: not_applicable
  summary: Native names no protein, pathway, regulator or transcriptomics dataset,
    so structured-source adapter has no native candidate. No direct PBP binding claim
    is inferred from label/class prose, and quinolone resistance targets are not transferred
    to cefovecin.
  target_ids:
  - antibioticmech:aro-c73757ed91
  evidence_ids:
  - native
  - survey-limits
  - label-trials
- assessment_id: other-fields
  area: scope
  topic: Producer, clinical objects, graph and dataset
  outcome: not_applicable
  summary: No native producer, structured clinical-status, causal-graph or dataset
    object is present. Generic veterinary-use definition is reviewed separately; no
    human indication or current product approval assertion is added.
  target_ids:
  - antibioticmech:aro-c73757ed91
  evidence_ids:
  - native
  - label
- assessment_id: provenance
  area: provenance
  topic: Actual ARO/PubChem ownership
  outcome: supported
  summary: Original capture hashes preserved; actual ARO and PubChem owners appended.
    Source mint and seed/reseed history match. Definition and xref corrections belong
    to maintained source inputs, not an isolated generated-record edit.
  target_ids:
  - antibioticmech:aro-c73757ed91
  evidence_ids:
  - owners
  - native
  - chemistry
- assessment_id: completeness
  area: completeness
  topic: Optional enrichment
  outcome: supported
  summary: Concrete activity/clinical source leads exist, with explicit limits; absent
    optional fields are not findings. Exact-xref and citation defects are populated
    assertions requiring correction.
  target_ids:
  - antibioticmech:aro-c73757ed91
  evidence_ids:
  - activity-primary
  - label-trials
  - rubric
- assessment_id: schema
  area: schema
  topic: Native deterministic checks
  outcome: supported
  summary: Focused schema/strict and supplemental native molecular checks pass; scientific
    source discrepancies remain.
  target_ids:
  - antibioticmech:aro-c73757ed91
  evidence_ids:
  - gates
  - chemistry
  - xref-stereo
findings:
- finding_id: F1
  issue_key: aro-3007458-cefovecin-chembl2110625-oxime-geometry
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The exact ChEMBL cross-reference encodes the opposite oxime geometry
  description: Native/PubChem cefovecin is Z at its methoxyimino C=N, whereas retained
    CHEMBL2110625 encodes E in its canonical SMILES, Standard InChI and molfile. Formula,
    connectivity and all three tetrahedral centres agree, so name/formula matching
    would miss this stereoisomer mismatch. Current ARO also displays the ChEMBL E
    SMILES. Preserve the correct native PubChem-derived structure and ARO provenance;
    adjudicate the exact ChEMBL link and document the upstream ARO representation
    conflict rather than replacing native Z with E.
  target_ids:
  - antibioticmech:aro-c73757ed91
  field_paths:
  - xrefs[1]
  - xrefs[0]
  evidence_ids:
  - native
  - owners
  - pubchem
  - chembl
  - xref-stereo
  - aro
  - label
  - rubric
  rule_id: native-review-checklist:Identity and Equivalence
  native_severity: major wrong exact stereochemical cross-reference
  normalization_reason: A populated equivalence points to a different explicitly encoded
    oxime geometry. Native identity remains correct, so this is major grounding rather
    than a blocker for a wrong native compound.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source-owned xrefs and definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction and cross-reference interpretation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated fields
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Supported source-adjudication override route
- finding_id: F2
  issue_key: aro-3007458-cefovecin-definition-citation-and-taxonym
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The definition has a genus typo and an unsuitable treatment-specific citation
  description: The definition spells Pasteurella as Pasturella and cites PMID 37107106
    for feline Pasteurella/canine staphylococcal skin-treatment claims. That original
    paper studies E. coli resistance in companion animals, not those treatment indications.
    The official sodium-product label independently supports qualified susceptible-pathogen
    indications, so the needed change is accurate spelling and appropriately scoped
    provenance rather than removal of the supported veterinary-use concept.
  target_ids:
  - antibioticmech:aro-c73757ed91
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - native
  - owners
  - aro
  - definition-source
  - label
  - canine-trial
  - feline-trial
  rule_id: native-review-checklist:Evidence standard and Clinical status
  native_severity: minor non-blocking definition wording and provenance
  normalization_reason: The underlying drug-use concept is independently supported;
    the defect is the inherited taxonym and its specific citation placement. No new
    indication or exact neutral-form administration claim is justified.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source-owned xrefs and definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction and cross-reference interpretation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated fields
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Supported source-adjudication override route
actions:
- action_id: A1
  description: Correct exact xref applicability through source adjudication while
    preserving native Z cefovecin.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-c73757ed91
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source-owned xrefs and definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction and cross-reference interpretation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated fields
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Supported source-adjudication override route
  acceptance_checks:
  - Exclude or correct the CHEMBL2110625 exact-equivalence assertion until an inspected
    source represents the native Z structure. The bounded native-key query returned
    no replacement; do not guess one.
  - Retain ARO:3007458 as provenance and document its displayed E versus linked PubChem
    Z conflict under the repository’s supported source-adjudication policy. Do not
    silently change the native molecular structure to match ChEMBL.
  - Re-extract/reseed only through maintained owners; verify every surviving exact
    xref agrees on 6R,7R, tetrahydrofuranyl 2S and Z oxime, full key and charge/formula.
  - Run schema/strict and applicable xref, term, history and corpus validation after
    separately authorized curation.
- action_id: A2
  description: Repair source-owned definition spelling and evidence placement.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-c73757ed91
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source-owned xrefs and definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction and cross-reference interpretation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated fields
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Supported source-adjudication override route
  acceptance_checks:
  - Correct Pasturella to Pasteurella and cite a source that explicitly supports the
    claimed veterinary indications. Preserve susceptible-strain and sodium-product
    context; avoid implying all Staphylococcus infections are indicated.
  - Use official label Description/Indications or directly inspected primary treatment
    studies for treatment-use support. Retain PMID 37107106 only for the E. coli survey
    context it actually measures.
  - Confirm source-owned changes survive reseeding without rewriting the correct neutral
    PubChem structure; validate native schema/strict and provenance/history.
- action_id: A3
  description: Optionally enrich activity/resistance only after resolving exact material
    and survey limitations.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-c73757ed91
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefovecin.yaml
    role: Curator-owned activity_spectrum/resistance evidence via validated writer
  acceptance_checks:
  - For PMID 37107106 resolve cefovecin-specific MIC/breakpoint methodology and the
    89 versus 90 and 70 versus 78 dog-isolate discrepancies before importing quantitative
    genotype relationships.
  - Preserve Korean 2018–2019 isolate selection; associated CTX-M/CMY genes do not
    by themselves establish individual-enzyme kinetics. gyrA/parC/PMQR results concern
    quinolone resistance.
  - Inspect the 2006 original study’s full methods and reagent identity before neutral-form
    numeric activity transfer. Keep sodium formulation trials and aggregate MIC90
    separate from exact single-isolate observations.
limitations:
- The current ChEMBL exact-native-key API query returned no candidate; it does not
  exhaust every alternative representation or historical release. Upstream ARO/ChEMBL
  correction was not requested or performed.
- 'The 2006 activity study is abstract-only here: EPMC XML 500, PMC CAPTCHA and alternative
  Europe PMC/publisher 403 prevented full text. Additional canine/feline efficacy
  leads were also inspected at abstract level only.'
- The adopted survey does not fully specify cefovecin reagent form or an explicit
  cefovecin breakpoint in Methods 4.3 and contains denominator discrepancies. No quantitative
  resistance or protein-target claim is transferred.
- The official CONVENIA source is a versioned sodium-product label. Its formulation,
  active-moiety strength, indication and trial results do not make the native neutral
  acid a pharmaceutical product.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 23 expanded input hashes unchanged, preserving original captures. No native/source/status/history
  edits.
- Focused validators used batch 024 own environment; standalone chemistry used existing
  batch 019 RDKit 2026.03.5 against batch 024 cwd.
- Free public retrieval only. No paid research, external contact or source mutation.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://card.mcmaster.ca/aro/3007458
- https://pubchem.ncbi.nlm.nih.gov/compound/6336480
- https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL2110625.json
- https://doi.org/10.3390/antibiotics12040745
- https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2daeaf25-f98f-49d3-943c-f604a844d93c
tags:
- cefovecin
- oxime-stereochemistry
- exact-xref
- definition-provenance
```
