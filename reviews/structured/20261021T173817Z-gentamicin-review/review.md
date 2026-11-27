# Review of gentamicin

- Review: 20261021T173817Z-gentamicin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:15:14Z
- Finished UTC: 2026-10-21T17:38:17Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The record explicitly denotes administered gentamicin mixture, but assigns one stereo-unspecified C21 molecular graph and an exact ChEMBL cross-reference containing three different components. This is a blocker identity mismatch. All twelve curated CDC MIC rows and ENA BioSample/taxon links were independently checked and remain valuable mixture-drug evidence that must be preserved without transfer to a selected congener. One verified product alias is also incorrectly typed. Thirty-two resistance assertions retain database provenance; primary evidence has important material and causal limits.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 498; original 13 input hashes preserved and seven actual source/curation owner inputs appended before detailed assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-b380d64ee1 | data/antibiotics/antibacterial/gentamicin.yaml | generated | gentamicin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-b380d64ee1 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-b380d64ee1 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-b380d64ee1 | Actual focused execution exited 0. |
| Independent current authority comparison | passed | False | antibioticmech:aro-b380d64ee1 | Seven encodings parsed. Native and PubChem3467 agree internally at one neutral graph; three ChEMBL encodings have three different molecular components and are not equivalent. |
| Input, source, citation, MIC and history audit | passed | False | antibioticmech:aro-b380d64ee1 | 20 unchanged input hashes, all 39 adopted leads, 32 current ARO edges, 12 CDC/ENA MIC/context rows and 14 chronological events checked. |
| Structured source catalog | passed | False | antibioticmech:aro-b380d64ee1 | Catalog inspected before bacterial mechanism follow-up. |
| Structured acrD query | passed | False | antibioticmech:aro-b380d64ee1 | The query returned gene metadata and no iModulon; no component summary applies. Catalog annotation is not experimental phenotype evidence. |
| Structured crcB query | passed | False | antibioticmech:aro-b380d64ee1 | The query returned gene metadata and no iModulon; no component summary applies. Catalog annotation is not experimental phenotype evidence. |
| Authoritative full QC | failed | True | antibioticmech:aro-b380d64ee1 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-b380d64ee1 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-b380d64ee1 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-b380d64ee1 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-b380d64ee1 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-b380d64ee1 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-b380d64ee1 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-b380d64ee1 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-b380d64ee1 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Explicit administered mixture and individual-structure contract

identity: concern. Targets: antibioticmech:aro-b380d64ee1.

The source and native definition explicitly denote a mixture; one stereo-unspecified C21 graph cannot represent that concept. This is not an inference of mixture from partial stereochemistry.

### Current exact chemical cross-references

grounding: concern. Targets: antibioticmech:aro-b380d64ee1.

PubChem agrees with the native single graph but ChEMBL is a multicomponent representation. Neither automatic replacement nor relabeling to a selected C congener resolves the source-level mixture concept.

### Aminoglycoside antibacterial context

nomenclature: supported. Targets: antibioticmech:aro-b380d64ee1.

The broad parent/class and antibacterial use are supported for gentamicin components and preparations; classification cannot repair the individual-structure identity mismatch.

### Cidomycin product alias

grounding: concern. Targets: antibioticmech:aro-b380d64ee1.

The official authority defines a sulfate injectable product; native EXACT_SYNONYM typing omits this product/material boundary.

### Twelve curated isolate MICs and strain provenance

quantity: supported. Targets: antibioticmech:aro-b380d64ee1.

Every value, qualifier, unit conversion, current source interpretation, edition boundary, sample/taxon link and stated special MLST/source detail agrees with inspected CDC/ENA records. Preserve them as gentamicin-test-drug observations; do not migrate them to a purified component automatically.

### Thirty-two source-qualified resistance mechanisms

evidence: unknown. Targets: antibioticmech:aro-b380d64ee1.

Current database edges are preserved and all adopted leads have dispositions. AcrD has direct deletion/complementation/uptake support in its stated conditions; CrcB and fosA5 exact causal scope remains unresolved. Other abstracts have host/expression/substrate limits and do not prove every congener-level relation.

### Clinical, toxicity and mixture-proportion prose

evidence: unknown. Targets: antibioticmech:aro-b380d64ee1.

The review citation and official product source provide bounded toxicity/use context. Exact80/20 component proportions and every indication are not independently verified; typographic repiratory and makes about around are low-impact source wording defects.

### Optional target, producer and causal objects

completeness: supported. Targets: antibioticmech:aro-b380d64ee1.

No falsely specific native primary target, producer strain or causal graph is asserted. Exact target/congener enrichment must follow identity resolution.

### Generated identity and curated activity provenance

ownership: supported. Targets: antibioticmech:aro-b380d64ee1.

Actual source/exclusion and curated writer/event lanes are identified, hashes preserved and history checked. Recommended corrections are not executed.

## Findings

### F1: An explicit gentamicin mixture is represented as one molecular graph

blocker / open / confirmed; issue key: gentamicin-mixture-assigned-single-component-graph.

Native and current ARO explicitly denote an administered gentamicin mixture, but the record assigns one C21H43N5O7 graph and exact chemical cross-references. ChEMBL3039597 independently represents three different molecular components. Exclude the mixture from the individual-structure corpus through a maintained decision; preserve all 12 independently verified curated MIC observations and their provenance in an appropriate mixture/drug evidence representation. Do not transfer those observations or 32 database mechanisms to a chosen congener or infer a mixture solely from unspecified stereochemistry.

### F2: Cidomycin is an injectable sulfate product rather than an exact chemical synonym

minor / open / confirmed; issue key: gentamicin-cidomycin-product-alias-exact-typing.

The official SmPC identifies Cidomycin as a gentamicin sulfate injectable mixture product. Its native EXACT_SYNONYM typing conflates that product with the one neutral molecular graph. Qualify or suppress the alias through maintained source controls in any retained representation; other five aliases remain bounded rather than automatically classified by name.

## Recommended Actions And Acceptance Checks

### A1

Plan and apply a justified EXCLUDE for ARO:3007382 through curation/decisions.tsv and documented source regeneration. Before any pruning, preserve the 12 curated MIC observations, exact source URLs, sample/taxon mappings and history in a supported drug/mixture evidence destination; if no destination exists, preserve an explicit archival artifact and resolve its ownership rather than silently discard evidence. Independently verify each proposed exact congener before reassignment or addition.

- Prove the explicit mixture is excluded reproducibly while source and all 12 curated activity observations/history remain recoverable.
- Do not relabel the native graph to C1 or copy mixed-drug MICs/mechanisms onto a component without exact material evidence.
- Run documented schema, strict term, reference/history, corpus reproducibility and QC gates after separately authorized curation.

### A2

Use maintained source synonym controls to product-qualify Cidomycin or suppress it from exact chemical synonyms in any retained source representation. Preserve sulfate, injectable formulation and mixture context.

- Compare official product 14742 and ensure no formulation-specific clinical claim is inherited by a single neutral component.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/gentamicin.yaml; Entire native record, all 12 activity observations,32 resistance objects and 14 history events | supports | The SEEDED/MINTED record explicitly says gentamicin is administered as a mixture and gives claimed component proportions. It assigns one neutral stereo-unspecified C21H43N5O7 graph, six EXACT_SYNONYM aliases, three xrefs and an aminoglycoside parent. Its32 resistance objects explicitly cite database assertions; no primary molecular-target object, exact producer strain or causal graph is asserted. |
| mixture | ARO:3007382; ARO:3000707; 498-aro-blocks.json;426-current-aro.obo with manifest426-fetch2-results.json | supports | Current ARO repeats the explicit administered-mixture definition and classifies the concept under antibiotic mixture. This independent source scope, not absence of encoded stereochemistry, establishes that the native concept is not one individual chemical structure. |
| chemistry | PubChem:3467; ChEMBL:CHEMBL3039597; 498-authority-chemistry.json;498-pc.json;498-chembl.json;498-fetch.json | supports | Four native/PubChem SMILES/InChI encodings agree at CEAZRRDELHUEMR-UHFFFAOYSA-N, neutral C21H43N5O7 with unassigned tetrahedral centres. Three ChEMBL encodings instead have key NPEFREDMMVQEPL-RWPARATISA-N and three disconnected component graphs with formulas C21H43N5O7, C20H41N5O7 and C19H39N5O7. Reciprocal whole-graph matching fails. The database multicomponent encoding does not establish an equimolar physical formulation and cannot be substituted into an individual-structure record. |
| primary-mixture | PMID:32601158; DOI:10.1128/AAC.00533-20; Shared496-PMC7449222.html; original introduction/initial characterization, isolation and susceptibility Methods;496-2020-fig1.jpg viewed | supports | The original study separates commercial gentamicin sulfate into distinct C congeners; purified free bases are resulfated before susceptibility testing. It directly supports the mixture/component distinction, without verifying the native fixed 80/20 proportions or assigning isolated-sulfate MICs to the native stereo-unspecified free-base graph. The table was only partly inspected and no quantitative row is adopted from it here. |
| brand | https://www.medicines.org.uk/emc/product/14742/smpc; 496-cidomycin.html; official sections1,2,5.1;496-fetch5.json | supports | Cidomycin 80 mg/2 ml is a gentamicin sulfate solution for injection, with sulfate equivalent to 80 mg gentamicin base per ampoule/vial. Section 5.1 calls gentamicin a mixture. This verifies a product name rather than an exact chemical synonym of the one native molecular graph; the other five aliases are not adjudicated as products merely from spelling. |
| mic | Twelve native CDC/FDA AR Isolate Bank URLs and corresponding ENA BioSample records; 498-cdc-fetch.json;498-source-audit.json mic_rows;498-cdc-&lt;strain&gt;.html and498-biosample-&lt;strain&gt;.xml | supports | All12 native MIC rows match actual gentamicin values, comparators and R interpretations:0349=8,0297&gt;16,0346&gt;16,1305&gt;16,0702=16,0726&gt;32,0729&gt;32,0730&gt;32,0033=16,0078&gt;16,0083&gt;16,0538=8 micrograms/ml. Native mg/L is numerically equivalent. All pages state broth microdilution and modal MIC; each linked BioSample and Study ID agrees, and ENA taxon identifiers/names match. The stated CLSI editions match source footnotes, while0033 correctly preserves absence of a versioned footnote. This verifies source-reported interpretation, not independent recalculation of CLSI breakpoints or a purified-congener assay. |
| strain | CDC isolates0033,0078,0083; ENA SAMN04014874,SAMN04014919,SAMN04014924; Actual isolate header/source/MLST fields in498-cdc-0033.html,-0078.html,-0083.html and corresponding ENA XML | supports | The CDC pages confirm0033 ST85(Pasteur)/ST1089(Oxford),0078 ST229(Pasteur)/ST203(Oxford) and Pus,0083 ST1(Pasteur)/ST231/1604(Oxford);0033/0083 retain Unknown source. ENA sample taxon and panel identifiers agree. No organism-wide resistance or causal gene assignment is inferred from these isolate measurements. |
| adopted | All39 frozen/current ARO PMID leads; 498-adopted-core.json;498-source-audit.json adopted_leads | supports | All39 MED identifiers resolve. Thirty-six complete supplied abstracts were read, one abstract is explicitly truncated at 250 words, and two historical reviews have no abstract. Each has a disposition preserving source type, host, expression, material and assay boundaries. The current32 exact ARO resistance edges remain present; their native evidence honestly identifies database provenance. |
| acrD | PMID:10692383; DOI:10.1128/JB.182.6.1754-1756.2000; 498-acrD.html; complete original main text including Table1 and uptake Methods/Results;498-primary-fetch2.json | supports | E. coli acrD deletion increases susceptibility and radiolabeled gentamicin accumulation; complementation restores the MIC. Table1 includes gentamicin 6 versus 1.5 micrograms/ml in one LB condition. Absolute MICs vary strongly with medium ingredients/ions. The tested radiolabeled drug has no resolved individual congener or salt stated. The same original reports no susceptibility effect from acrA or tolC disruption in its context; it cannot alone validate every later AcrAD-TolC complex claim. |
| ant | PMID:25564464; DOI:10.1128/mBio.02180-14; 498-PMC4313920.xml; structural/kinetic Results and kinetic assay Methods, Figure1/5 captions | supports | The new ANT(2double-prime)-Ia crystal complex and kinetic experiments use kanamycin B. The paper depicts a proposed gentamicin C2 adenylylation mechanism and reuses an earlier gentamicin C1a-RNA structure. Its relevance to a gentamicin database edge does not turn the measured substrate or crystallized complex into gentamicin. |
| crcB | PMID:23405357; PMID:35631066; 498-PMC3569361.xml complete short main;498-PMC9144577.xml Methods, resistance Results and limitations | supports | The first original is an Ecl8 genome announcement without a CrcB/gentamicin functional experiment. The second annotates 89 Kenyan Klebsiella isolates using CARD and labels crcB among conserved resistance-associated genes; its listed AST panel omits gentamicin, and it does not perform a crcB deletion or transport assay. These sources establish genomic/source context, not direct gentamicin efflux. The native edge remains a qualified database assertion rather than a disproven biological activity. |
| fosA5 | PMID:25441705; DOI:10.1111/lam.12366; Complete supplied abstract in498-adopted-core.json; failed correct publisher route recorded498-primary-fetch2.json | supports | The original abstract establishes fosA5 and fosfomycin resistance using isolate, transconjugant and transformant MICs. It does not establish gentamicin inactivation. The correct 60(3):259–264 publisher route returned403; isolate co-resistance versus gene-specific gentamicin causality remains unresolved. No blanket removal or absence-of-activity conclusion is made. |
| definition | PMID:28507482; DOI:10.17179/excli2017-165; 498-PMC5427480.xml; complete abstract, selected renal-mechanism and conclusion paragraphs | supports | The adopted definition citation is a nephrotoxicity review, not an original antibacterial-target or mixture-composition experiment. It supports broad renal-toxicity context; exact component proportions and all clinical indications were not independently verified from it. Original component work and the official product source independently support the material boundary. |
| adapter | iModulonDB e_coli/precise1k genes b2470 and b0624; 498-imodulon-datasets.json;498-imodulon-acrD.json;498-imodulon-crcB.json | supports | Catalog-first search returns acrD/b2470 RND-permease and crcB/b0624 fluoride-channel annotations with zero iModulon hits. No summarize call applies. Expression membership or cross-organism gene-name annotation is not direct transport, binding or resistance evidence. |
| owners | Actual ARO/PubChem sources and curated activity writer; 498-inspect.json;498-raw-rows.json;498-source-audit.json;498-owners-search.json | supports | Original13 input hashes and seven appended actual owners are unchanged. Thirty-four exact raw rows reproduce source/enrichment claims;14 history events are chronological. Ignored-inclusive raw/curation/conf/scripts/src searches located maintained source/decision/generator and curated writer/event ownership. Curated MIC and history evidence must survive any exclusion or source-concept reorganization. |

## Limits And Additional Notes

- Thirty-six of 39 adopted leads were read as complete supplied abstracts; one was explicitly truncated at 250 words and two reviews supplied metadata only. Most full resistance papers were not inspected; detailed component/material support remains unresolved.
- The fosA5 correct publisher route returned403; its abstract supports fosfomycin resistance, and gentamicin co-resistance versus gene-specific mechanism is unresolved. The CrcB sources inspected establish genome/annotation context, not direct gentamicin transport, without disproving possible activity.
- AcrD was read as complete original main text and Table1. The ANT original was read at stated Results/Methods/caption depth; its crystal/kinetics use kanamycin B. No broader claim of complete supplementary inspection is made.
- The native toxicity citation is a review; exact mixture proportions and every clinical indication were not independently verified. Only Cidomycin among six aliases was independently verified as a product.
- CDC MICs identify gentamicin as test drug without purified-congener or exact salt lot identity; their R classifications and edition footnotes are source-reported, not independently recalculated from licensed CLSI tables.
- The initial guessed fosA5 URL was not the correct article and failed; the corrected DOI-matched route also failed. The guessed CDC FAQ returned a Page Not Found body and contributes no evidence; all modal-MIC assertions were verified on the actual isolate pages.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Standalone chemistry used batch019 against batch050; native schema, strict, ledger and contract checks used batch050.
- All original input hashes remain preserved. No native/source bytes, curated observations or scientific status were changed. The draft proposes preservation and exclusion work; it does not record those actions as performed.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T173817Z-gentamicin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of gentamicin
started_at: '2026-10-21T17:15:14Z'
finished_at: '2026-10-21T17:38:17Z'
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
summary: The record explicitly denotes administered gentamicin mixture, but assigns
  one stereo-unspecified C21 molecular graph and an exact ChEMBL cross-reference containing
  three different components. This is a blocker identity mismatch. All twelve curated
  CDC MIC rows and ENA BioSample/taxon links were independently checked and remain
  valuable mixture-drug evidence that must be preserved without transfer to a selected
  congener. One verified product alias is also incorrectly typed. Thirty-two resistance
  assertions retain database provenance; primary evidence has important material and
  causal limits.
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
  - path: data/antibiotics/antibacterial/gentamicin.yaml
    sha256: fed1a91545302837eba2fa9dc4cf048db7e423556ef956f5d35cc226dd7ac5d8
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
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
  - path: src/antibioticmech/validation/write_validated.py
    sha256: 7e75d39582e3a8c6d816c7927126b39948fbd2bf7650b579a71e93d912d659db
    role: context
  - path: src/antibioticmech/curate/curation_event.py
    sha256: d080b25ad399a054d2f86636c1e9dc6847099ef4417dcd8f50e57661448f95a6
    role: context
  - path: .claude/skills/research-resistant-taxa/SKILL.md
    sha256: 0a3fc942e28b784e2133ef6604e1198669b0a39174c342d9bb34bb9da8a6cb25
    role: context
targets:
- target_id: antibioticmech:aro-b380d64ee1
  path: data/antibiotics/antibacterial/gentamicin.yaml
  label: gentamicin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition, aliases and cross-references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted CARD/ARO resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Neutral structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem enrichment producer
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated fields and preservation of curator-owned activity
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusion decisions
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Source-scoped controls
  - repository: CultureBotAI/AntibioticMech
    path: src/antibioticmech/validation/write_validated.py
    role: Validated writer for curator-owned native activity observations
  - repository: CultureBotAI/AntibioticMech
    path: src/antibioticmech/curate/curation_event.py
    role: Curation history writer
  - repository: CultureBotAI/AntibioticMech
    path: .claude/skills/research-resistant-taxa/SKILL.md
    role: Native resistance/MIC evidence scope rubric
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 498; original 13 input hashes preserved
    and seven actual source/curation owner inputs appended before detailed assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-b380d64ee1
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-b380d64ee1
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    498
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-b380d64ee1
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/gentamicin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-b380d64ee1
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/gentamicin.yaml --out /private/tmp/am-review-session/498-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority
  name: Independent current authority comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/498-authority-check.py
    > /private/tmp/am-review-session/498-authority-check.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Seven encodings parsed. Native and PubChem3467 agree internally at one
    neutral graph; three ChEMBL encodings have three different molecular components
    and are not equivalent.
  target_ids:
  - antibioticmech:aro-b380d64ee1
- check_id: ledger
  name: Input, source, citation, MIC and history audit
  command: .venv/bin/python /private/tmp/am-review-session/498-ledger.py > /private/tmp/am-review-session/498-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: 20 unchanged input hashes, all 39 adopted leads, 32 current ARO edges,
    12 CDC/ENA MIC/context rows and 14 chronological events checked.
  target_ids:
  - antibioticmech:aro-b380d64ee1
- check_id: adapter-catalog
  name: Structured source catalog
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets > /private/tmp/am-review-session/498-imodulon-datasets.json
    2> /private/tmp/am-review-session/498-imodulon-datasets.err
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Catalog inspected before bacterial mechanism follow-up.
  target_ids:
  - antibioticmech:aro-b380d64ee1
- check_id: adapter-acrD
  name: Structured acrD query
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query acrD
    > /private/tmp/am-review-session/498-imodulon-acrD.json 2> /private/tmp/am-review-session/498-imodulon-acrD.err
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: The query returned gene metadata and no iModulon; no component summary
    applies. Catalog annotation is not experimental phenotype evidence.
  target_ids:
  - antibioticmech:aro-b380d64ee1
- check_id: adapter-crcB
  name: Structured crcB query
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query crcB
    > /private/tmp/am-review-session/498-imodulon-crcB.json 2> /private/tmp/am-review-session/498-imodulon-crcB.err
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: The query returned gene metadata and no iModulon; no component summary
    applies. Catalog annotation is not experimental phenotype evidence.
  target_ids:
  - antibioticmech:aro-b380d64ee1
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-b380d64ee1
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
  - antibioticmech:aro-b380d64ee1
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
  - antibioticmech:aro-b380d64ee1
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
  - antibioticmech:aro-b380d64ee1
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
  - antibioticmech:aro-b380d64ee1
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
  - antibioticmech:aro-b380d64ee1
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
  - antibioticmech:aro-b380d64ee1
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
  - antibioticmech:aro-b380d64ee1
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
  - antibioticmech:aro-b380d64ee1
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/gentamicin.yaml
  locator: Entire native record, all 12 activity observations,32 resistance objects
    and 14 history events
  accessed_at: '2026-10-21T17:37:30Z'
  support: supports
  summary: The SEEDED/MINTED record explicitly says gentamicin is administered as
    a mixture and gives claimed component proportions. It assigns one neutral stereo-unspecified
    C21H43N5O7 graph, six EXACT_SYNONYM aliases, three xrefs and an aminoglycoside
    parent. Its32 resistance objects explicitly cite database assertions; no primary
    molecular-target object, exact producer strain or causal graph is asserted.
- evidence_id: mixture
  kind: authority
  reference: ARO:3007382; ARO:3000707
  locator: 498-aro-blocks.json;426-current-aro.obo with manifest426-fetch2-results.json
  accessed_at: '2026-10-21T17:37:30Z'
  support: supports
  summary: Current ARO repeats the explicit administered-mixture definition and classifies
    the concept under antibiotic mixture. This independent source scope, not absence
    of encoded stereochemistry, establishes that the native concept is not one individual
    chemical structure.
  snapshot_sha256: 20bd4116c52ed1f3745054fe4b5af0129ea339f10161e4dc380a1fa9295c9673
- evidence_id: chemistry
  kind: authority
  reference: PubChem:3467; ChEMBL:CHEMBL3039597
  locator: 498-authority-chemistry.json;498-pc.json;498-chembl.json;498-fetch.json
  accessed_at: '2026-10-21T17:37:30Z'
  support: supports
  summary: Four native/PubChem SMILES/InChI encodings agree at CEAZRRDELHUEMR-UHFFFAOYSA-N,
    neutral C21H43N5O7 with unassigned tetrahedral centres. Three ChEMBL encodings
    instead have key NPEFREDMMVQEPL-RWPARATISA-N and three disconnected component
    graphs with formulas C21H43N5O7, C20H41N5O7 and C19H39N5O7. Reciprocal whole-graph
    matching fails. The database multicomponent encoding does not establish an equimolar
    physical formulation and cannot be substituted into an individual-structure record.
  snapshot_sha256: defaf866afa4cf5fcec6ce704cdbefad3d1436be6b9f176234ff7d45ce800f05
- evidence_id: primary-mixture
  kind: primary_source
  reference: PMID:32601158; DOI:10.1128/AAC.00533-20
  locator: Shared496-PMC7449222.html; original introduction/initial characterization,
    isolation and susceptibility Methods;496-2020-fig1.jpg viewed
  accessed_at: '2026-10-21T17:37:30Z'
  support: supports
  summary: The original study separates commercial gentamicin sulfate into distinct
    C congeners; purified free bases are resulfated before susceptibility testing.
    It directly supports the mixture/component distinction, without verifying the
    native fixed 80/20 proportions or assigning isolated-sulfate MICs to the native
    stereo-unspecified free-base graph. The table was only partly inspected and no
    quantitative row is adopted from it here.
  snapshot_sha256: 1ff2ec241866ee77117e5422ba749beaf73a23f775f3ee767db361e3617ab715
- evidence_id: brand
  kind: authority
  reference: https://www.medicines.org.uk/emc/product/14742/smpc
  locator: 496-cidomycin.html; official sections1,2,5.1;496-fetch5.json
  accessed_at: '2026-10-21T17:37:30Z'
  support: supports
  summary: Cidomycin 80 mg/2 ml is a gentamicin sulfate solution for injection, with
    sulfate equivalent to 80 mg gentamicin base per ampoule/vial. Section 5.1 calls
    gentamicin a mixture. This verifies a product name rather than an exact chemical
    synonym of the one native molecular graph; the other five aliases are not adjudicated
    as products merely from spelling.
  snapshot_sha256: 4c4eb1040286d87b6dcec60495f64c67955baff210c0e6fdd2a31b9939b48517
- evidence_id: mic
  kind: authority
  reference: Twelve native CDC/FDA AR Isolate Bank URLs and corresponding ENA BioSample
    records
  locator: 498-cdc-fetch.json;498-source-audit.json mic_rows;498-cdc-<strain>.html
    and498-biosample-<strain>.xml
  accessed_at: '2026-10-21T17:37:30Z'
  support: supports
  summary: All12 native MIC rows match actual gentamicin values, comparators and R
    interpretations:0349=8,0297>16,0346>16,1305>16,0702=16,0726>32,0729>32,0730>32,0033=16,0078>16,0083>16,0538=8
    micrograms/ml. Native mg/L is numerically equivalent. All pages state broth microdilution
    and modal MIC; each linked BioSample and Study ID agrees, and ENA taxon identifiers/names
    match. The stated CLSI editions match source footnotes, while0033 correctly preserves
    absence of a versioned footnote. This verifies source-reported interpretation,
    not independent recalculation of CLSI breakpoints or a purified-congener assay.
  snapshot_sha256: 315c4a97cc1ea0109dd00ff4245293643482ecf317b07eb5c3e74d8d6ced3c4d
- evidence_id: strain
  kind: authority
  reference: CDC isolates0033,0078,0083; ENA SAMN04014874,SAMN04014919,SAMN04014924
  locator: Actual isolate header/source/MLST fields in498-cdc-0033.html,-0078.html,-0083.html
    and corresponding ENA XML
  accessed_at: '2026-10-21T17:37:30Z'
  support: supports
  summary: The CDC pages confirm0033 ST85(Pasteur)/ST1089(Oxford),0078 ST229(Pasteur)/ST203(Oxford)
    and Pus,0083 ST1(Pasteur)/ST231/1604(Oxford);0033/0083 retain Unknown source.
    ENA sample taxon and panel identifiers agree. No organism-wide resistance or causal
    gene assignment is inferred from these isolate measurements.
  snapshot_sha256: 4bc2aef6b002efb90ba704e3fb7f971690633838536976956ce57af0d3253fc0
- evidence_id: adopted
  kind: database
  reference: All39 frozen/current ARO PMID leads
  locator: 498-adopted-core.json;498-source-audit.json adopted_leads
  accessed_at: '2026-10-21T17:37:30Z'
  support: supports
  summary: All39 MED identifiers resolve. Thirty-six complete supplied abstracts were
    read, one abstract is explicitly truncated at 250 words, and two historical reviews
    have no abstract. Each has a disposition preserving source type, host, expression,
    material and assay boundaries. The current32 exact ARO resistance edges remain
    present; their native evidence honestly identifies database provenance.
  snapshot_sha256: 315c4a97cc1ea0109dd00ff4245293643482ecf317b07eb5c3e74d8d6ced3c4d
- evidence_id: acrD
  kind: primary_source
  reference: PMID:10692383; DOI:10.1128/JB.182.6.1754-1756.2000
  locator: 498-acrD.html; complete original main text including Table1 and uptake
    Methods/Results;498-primary-fetch2.json
  accessed_at: '2026-10-21T17:37:30Z'
  support: supports
  summary: E. coli acrD deletion increases susceptibility and radiolabeled gentamicin
    accumulation; complementation restores the MIC. Table1 includes gentamicin 6 versus
    1.5 micrograms/ml in one LB condition. Absolute MICs vary strongly with medium
    ingredients/ions. The tested radiolabeled drug has no resolved individual congener
    or salt stated. The same original reports no susceptibility effect from acrA or
    tolC disruption in its context; it cannot alone validate every later AcrAD-TolC
    complex claim.
  snapshot_sha256: a19f4e3f3fee2e961df47507d46888956ded3f005a7201486e6e5957e324e647
- evidence_id: ant
  kind: primary_source
  reference: PMID:25564464; DOI:10.1128/mBio.02180-14
  locator: 498-PMC4313920.xml; structural/kinetic Results and kinetic assay Methods,
    Figure1/5 captions
  accessed_at: '2026-10-21T17:37:30Z'
  support: supports
  summary: The new ANT(2double-prime)-Ia crystal complex and kinetic experiments use
    kanamycin B. The paper depicts a proposed gentamicin C2 adenylylation mechanism
    and reuses an earlier gentamicin C1a-RNA structure. Its relevance to a gentamicin
    database edge does not turn the measured substrate or crystallized complex into
    gentamicin.
  snapshot_sha256: 6b35ab135cf8ca2a598d8980fb684f61aed30d2a96396870ceae5e59edd58e70
- evidence_id: crcB
  kind: primary_source
  reference: PMID:23405357; PMID:35631066
  locator: 498-PMC3569361.xml complete short main;498-PMC9144577.xml Methods, resistance
    Results and limitations
  accessed_at: '2026-10-21T17:37:30Z'
  support: supports
  summary: The first original is an Ecl8 genome announcement without a CrcB/gentamicin
    functional experiment. The second annotates 89 Kenyan Klebsiella isolates using
    CARD and labels crcB among conserved resistance-associated genes; its listed AST
    panel omits gentamicin, and it does not perform a crcB deletion or transport assay.
    These sources establish genomic/source context, not direct gentamicin efflux.
    The native edge remains a qualified database assertion rather than a disproven
    biological activity.
  snapshot_sha256: ad5439974579cfc2db1db75fdfb745bbc2331d5d1f7c43a8b37a19eef539522c
- evidence_id: fosA5
  kind: primary_source
  reference: PMID:25441705; DOI:10.1111/lam.12366
  locator: Complete supplied abstract in498-adopted-core.json; failed correct publisher
    route recorded498-primary-fetch2.json
  accessed_at: '2026-10-21T17:37:30Z'
  support: supports
  summary: The original abstract establishes fosA5 and fosfomycin resistance using
    isolate, transconjugant and transformant MICs. It does not establish gentamicin
    inactivation. The correct 60(3):259–264 publisher route returned403; isolate co-resistance
    versus gene-specific gentamicin causality remains unresolved. No blanket removal
    or absence-of-activity conclusion is made.
  snapshot_sha256: cfe8d895ab3894e780f9351584326dabc438ea319b6548782e8289e4acad5214
- evidence_id: definition
  kind: authority
  reference: PMID:28507482; DOI:10.17179/excli2017-165
  locator: 498-PMC5427480.xml; complete abstract, selected renal-mechanism and conclusion
    paragraphs
  accessed_at: '2026-10-21T17:37:30Z'
  support: supports
  summary: The adopted definition citation is a nephrotoxicity review, not an original
    antibacterial-target or mixture-composition experiment. It supports broad renal-toxicity
    context; exact component proportions and all clinical indications were not independently
    verified from it. Original component work and the official product source independently
    support the material boundary.
  snapshot_sha256: 037c6fa9bd7ec5ea3339d950eca4608194467c2d5d69286787eda69b8ba989e0
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/precise1k genes b2470 and b0624
  locator: 498-imodulon-datasets.json;498-imodulon-acrD.json;498-imodulon-crcB.json
  accessed_at: '2026-10-21T17:37:30Z'
  support: supports
  summary: Catalog-first search returns acrD/b2470 RND-permease and crcB/b0624 fluoride-channel
    annotations with zero iModulon hits. No summarize call applies. Expression membership
    or cross-organism gene-name annotation is not direct transport, binding or resistance
    evidence.
  snapshot_sha256: 6d975f37417a24db9494108d52bb8bf9a4a0222726f717fbdff5a332e16fe3a0
- evidence_id: owners
  kind: validation
  reference: Actual ARO/PubChem sources and curated activity writer
  locator: 498-inspect.json;498-raw-rows.json;498-source-audit.json;498-owners-search.json
  accessed_at: '2026-10-21T17:37:30Z'
  support: supports
  summary: Original13 input hashes and seven appended actual owners are unchanged.
    Thirty-four exact raw rows reproduce source/enrichment claims;14 history events
    are chronological. Ignored-inclusive raw/curation/conf/scripts/src searches located
    maintained source/decision/generator and curated writer/event ownership. Curated
    MIC and history evidence must survive any exclusion or source-concept reorganization.
  snapshot_sha256: 315c4a97cc1ea0109dd00ff4245293643482ecf317b07eb5c3e74d8d6ced3c4d
assessments:
- assessment_id: identity
  area: identity
  topic: Explicit administered mixture and individual-structure contract
  outcome: concern
  summary: The source and native definition explicitly denote a mixture; one stereo-unspecified
    C21 graph cannot represent that concept. This is not an inference of mixture from
    partial stereochemistry.
  target_ids:
  - antibioticmech:aro-b380d64ee1
  evidence_ids:
  - record
  - mixture
  - chemistry
  - primary-mixture
- assessment_id: grounding
  area: grounding
  topic: Current exact chemical cross-references
  outcome: concern
  summary: PubChem agrees with the native single graph but ChEMBL is a multicomponent
    representation. Neither automatic replacement nor relabeling to a selected C congener
    resolves the source-level mixture concept.
  target_ids:
  - antibioticmech:aro-b380d64ee1
  evidence_ids:
  - chemistry
  - mixture
- assessment_id: class
  area: nomenclature
  topic: Aminoglycoside antibacterial context
  outcome: supported
  summary: The broad parent/class and antibacterial use are supported for gentamicin
    components and preparations; classification cannot repair the individual-structure
    identity mismatch.
  target_ids:
  - antibioticmech:aro-b380d64ee1
  evidence_ids:
  - record
  - primary-mixture
  - brand
- assessment_id: alias
  area: grounding
  topic: Cidomycin product alias
  outcome: concern
  summary: The official authority defines a sulfate injectable product; native EXACT_SYNONYM
    typing omits this product/material boundary.
  target_ids:
  - antibioticmech:aro-b380d64ee1
  evidence_ids:
  - brand
  - record
- assessment_id: mic
  area: quantity
  topic: Twelve curated isolate MICs and strain provenance
  outcome: supported
  summary: Every value, qualifier, unit conversion, current source interpretation,
    edition boundary, sample/taxon link and stated special MLST/source detail agrees
    with inspected CDC/ENA records. Preserve them as gentamicin-test-drug observations;
    do not migrate them to a purified component automatically.
  target_ids:
  - antibioticmech:aro-b380d64ee1
  evidence_ids:
  - mic
  - strain
  - owners
- assessment_id: resistance
  area: evidence
  topic: Thirty-two source-qualified resistance mechanisms
  outcome: unknown
  summary: Current database edges are preserved and all adopted leads have dispositions.
    AcrD has direct deletion/complementation/uptake support in its stated conditions;
    CrcB and fosA5 exact causal scope remains unresolved. Other abstracts have host/expression/substrate
    limits and do not prove every congener-level relation.
  target_ids:
  - antibioticmech:aro-b380d64ee1
  evidence_ids:
  - adopted
  - acrD
  - ant
  - crcB
  - fosA5
  - adapter
- assessment_id: definition
  area: evidence
  topic: Clinical, toxicity and mixture-proportion prose
  outcome: unknown
  summary: The review citation and official product source provide bounded toxicity/use
    context. Exact80/20 component proportions and every indication are not independently
    verified; typographic repiratory and makes about around are low-impact source
    wording defects.
  target_ids:
  - antibioticmech:aro-b380d64ee1
  evidence_ids:
  - definition
  - brand
  - record
- assessment_id: completeness
  area: completeness
  topic: Optional target, producer and causal objects
  outcome: supported
  summary: No falsely specific native primary target, producer strain or causal graph
    is asserted. Exact target/congener enrichment must follow identity resolution.
  target_ids:
  - antibioticmech:aro-b380d64ee1
  evidence_ids:
  - record
  - ant
  - primary-mixture
- assessment_id: ownership
  area: ownership
  topic: Generated identity and curated activity provenance
  outcome: supported
  summary: Actual source/exclusion and curated writer/event lanes are identified,
    hashes preserved and history checked. Recommended corrections are not executed.
  target_ids:
  - antibioticmech:aro-b380d64ee1
  evidence_ids:
  - owners
findings:
- finding_id: F1
  issue_key: gentamicin-mixture-assigned-single-component-graph
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: An explicit gentamicin mixture is represented as one molecular graph
  description: Native and current ARO explicitly denote an administered gentamicin
    mixture, but the record assigns one C21H43N5O7 graph and exact chemical cross-references.
    ChEMBL3039597 independently represents three different molecular components. Exclude
    the mixture from the individual-structure corpus through a maintained decision;
    preserve all 12 independently verified curated MIC observations and their provenance
    in an appropriate mixture/drug evidence representation. Do not transfer those
    observations or 32 database mechanisms to a chosen congener or infer a mixture
    solely from unspecified stereochemistry.
  target_ids:
  - antibioticmech:aro-b380d64ee1
  field_paths:
  - identifier
  - definition
  - chemical_structure
  - xrefs
  - activity_spectrum
  - source_concepts
  evidence_ids:
  - record
  - mixture
  - chemistry
  - primary-mixture
  - mic
  - owners
  rule_id: 'CLAUDE.md: A record is a structure; docs/record-reviews.md: wrong identity
    blocker'
  normalization_reason: Blocker because the represented concept fails the individual-chemical-structure
    identity contract despite internally valid chemistry and successful focused schema
    checks.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained source-concept EXCLUDE decision
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Explicit mixture source identity
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Single-graph enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Source-to-structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source eligibility and assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Native regeneration
  - repository: CultureBotAI/AntibioticMech
    path: src/antibioticmech/validation/write_validated.py
    role: Preservation and validation of curator-owned activity evidence
  - repository: CultureBotAI/AntibioticMech
    path: src/antibioticmech/curate/curation_event.py
    role: Required provenance for any later curated change
- finding_id: F2
  issue_key: gentamicin-cidomycin-product-alias-exact-typing
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Cidomycin is an injectable sulfate product rather than an exact chemical
    synonym
  description: The official SmPC identifies Cidomycin as a gentamicin sulfate injectable
    mixture product. Its native EXACT_SYNONYM typing conflates that product with the
    one neutral molecular graph. Qualify or suppress the alias through maintained
    source controls in any retained representation; other five aliases remain bounded
    rather than automatically classified by name.
  target_ids:
  - antibioticmech:aro-b380d64ee1
  field_paths:
  - synonyms[0]
  evidence_ids:
  - record
  - brand
  - owners
  rule_id: 'src/antibioticmech/schema/antibioticmech.yaml: SynonymTypeEnum'
  normalization_reason: Minor bounded product-versus-chemical synonym typing error,
    secondary to the blocker mixture identity mismatch.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source synonyms and definition
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Source synonym controls
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated aliases
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-b380d64ee1
  description: Plan and apply a justified EXCLUDE for ARO:3007382 through curation/decisions.tsv
    and documented source regeneration. Before any pruning, preserve the 12 curated
    MIC observations, exact source URLs, sample/taxon mappings and history in a supported
    drug/mixture evidence destination; if no destination exists, preserve an explicit
    archival artifact and resolve its ownership rather than silently discard evidence.
    Independently verify each proposed exact congener before reassignment or addition.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained source-concept EXCLUDE decision
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Explicit mixture source identity
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Single-graph enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Source-to-structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source eligibility and assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Native regeneration
  - repository: CultureBotAI/AntibioticMech
    path: src/antibioticmech/validation/write_validated.py
    role: Preservation and validation of curator-owned activity evidence
  - repository: CultureBotAI/AntibioticMech
    path: src/antibioticmech/curate/curation_event.py
    role: Required provenance for any later curated change
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py;
    validated curator writer/event for curated evidence changes
  acceptance_checks:
  - Prove the explicit mixture is excluded reproducibly while source and all 12 curated
    activity observations/history remain recoverable.
  - Do not relabel the native graph to C1 or copy mixed-drug MICs/mechanisms onto
    a component without exact material evidence.
  - Run documented schema, strict term, reference/history, corpus reproducibility
    and QC gates after separately authorized curation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-b380d64ee1
  description: Use maintained source synonym controls to product-qualify Cidomycin
    or suppress it from exact chemical synonyms in any retained source representation.
    Preserve sulfate, injectable formulation and mixture context.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source synonyms and definition
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Source synonym controls
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated aliases
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py
  acceptance_checks:
  - Compare official product 14742 and ensure no formulation-specific clinical claim
    is inherited by a single neutral component.
limitations:
- Thirty-six of 39 adopted leads were read as complete supplied abstracts; one was
  explicitly truncated at 250 words and two reviews supplied metadata only. Most full
  resistance papers were not inspected; detailed component/material support remains
  unresolved.
- The fosA5 correct publisher route returned403; its abstract supports fosfomycin
  resistance, and gentamicin co-resistance versus gene-specific mechanism is unresolved.
  The CrcB sources inspected establish genome/annotation context, not direct gentamicin
  transport, without disproving possible activity.
- AcrD was read as complete original main text and Table1. The ANT original was read
  at stated Results/Methods/caption depth; its crystal/kinetics use kanamycin B. No
  broader claim of complete supplementary inspection is made.
- The native toxicity citation is a review; exact mixture proportions and every clinical
  indication were not independently verified. Only Cidomycin among six aliases was
  independently verified as a product.
- CDC MICs identify gentamicin as test drug without purified-congener or exact salt
  lot identity; their R classifications and edition footnotes are source-reported,
  not independently recalculated from licensed CLSI tables.
- The initial guessed fosA5 URL was not the correct article and failed; the corrected
  DOI-matched route also failed. The guessed CDC FAQ returned a Page Not Found body
  and contributes no evidence; all modal-MIC assertions were verified on the actual
  isolate pages.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Standalone chemistry used batch019 against batch050; native schema, strict, ledger
  and contract checks used batch050.
- All original input hashes remain preserved. No native/source bytes, curated observations
  or scientific status were changed. The draft proposes preservation and exclusion
  work; it does not record those actions as performed.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://pubchem.ncbi.nlm.nih.gov/compound/3467
- https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3039597
- https://pmc.ncbi.nlm.nih.gov/articles/PMC94475/
- https://www.medicines.org.uk/emc/product/14742/smpc
tags:
- record-review
- gentamicin
- mixture-boundary
- curated-mic
```
