# Cervimycin C: coherent identity and direct antibacterial evidence with bounded mechanism and tautomer scope

- Review: 20261021T124006Z-cervimycin-c
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:20:05Z
- Finished UTC: 2026-10-21T12:40:06Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native neutral cervimycin C graph and all asserted identifiers agree with official ChEBI/PubChem structures. The adopted 2022 paper directly supports antibacterial activity of C as well as the general polyketide description. Primary follow-up provides resistance genetics, high-concentration gyrase inhibition and drug-response observations, but does not establish a single low-concentration molecular mechanism. The papers draw an alternative A-ring keto-enol form, so exact experimental chemical-form and structural-proof limits remain explicit. No confirmed corrective finding emerged; optional enrichment requires careful separation of direct assays, resistance determinants and hypotheses. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole native YAML: label and mint, antibacterial filing, definition and sole PMID, structural class/parent, every chemical descriptor and three xrefs, the source concept and all three history events. Actual maintained ARO/PubChem rows and relevant extractor/enricher/seeder logic were inspected. Every adopted literature lead was assessed.

Selection: Queue 276; all thirteen original input hashes were preserved. Actual ARO/PubChem inventories and PubChem enrichment script were appended, followed by two local MIBiG context inputs, for eighteen captured inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-72f1180eb7 | data/antibiotics/antibacterial/cervimycin-c.yaml | generated | cervimycin C |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | antibioticmech:aro-72f1180eb7 | No schema issues found. |
| strict | passed | True | antibioticmech:aro-72f1180eb7 | One record scanned; zero strict errors. |
| chemistry | passed | False | antibioticmech:aro-72f1180eb7 | Native encodings, formula, charge, masses and stable ARO mint agree. Run from batch028 using the batch019 RDKit interpreter. |
| official-structure-check | passed | False | antibioticmech:aro-72f1180eb7 | Four official ChEBI/PubChem encodings independently reproduce the full native key. |
| Authoritative full QC | failed | True | antibioticmech:aro-72f1180eb7 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-72f1180eb7 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-72f1180eb7 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-72f1180eb7 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-72f1180eb7 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-72f1180eb7 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-72f1180eb7 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-72f1180eb7 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-72f1180eb7 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact C database identity and representation boundary

identity: supported. Targets: antibioticmech:aro-72f1180eb7.

The native neutral carbamoyl/dimethylmalonyl graph, identifiers and source mint agree with current official structures. Published drawings use another A-ring keto-enol placement and do not independently establish the full native absolute stereochemical proof. Preserve this qualification; it is not a demonstrated wrong-congener or opposite-enantiomer error.

### Antibacterial scope and broader polyketide parent

scope: supported. Targets: antibioticmech:aro-72f1180eb7.

The parent denotes a broad chemical class and the adopted original C susceptibility experiments directly support antibacterial filing. C values are distinguished from D and from experimental pH variants. The record asserts no broad clinical susceptibility breakpoint or approval.

### Sole adopted citation and experimental scope

evidence: supported. Targets: antibioticmech:aro-72f1180eb7.

PMID:36173303 is correctly identified and supports both the general description and C activity. Its resistance genetics and omics are useful enrichment evidence but do not by themselves establish direct Clp/WalK binding or a complete antimicrobial causal chain.

### Optional direct target and phenotype enrichment

completeness: unknown. Targets: antibioticmech:aro-72f1180eb7.

The 2024 holoenzyme assay supports high-concentration gyrase inhibition. It does not identify a unique GyrB binding site or show that this effect explains killing near the MIC. Low-concentration transcriptional resemblance and the Figure 7 model remain hypotheses. Since the seed makes no target claim, an optional mechanism gap is not a corrective finding.

### Optional resistance determinants and transcriptomic context

completeness: supported. Targets: antibioticmech:aro-72f1180eb7.

The 2010 bmrA mutation dissection and 2022 Clp/WalK experiments provide exact C resistance context with distinct organisms and experimental designs. Direct transport, drug binding, mutant phenotype and expression change must remain separate evidence types. No current native resistance assertion is wrong.

### Producer and biosynthesis context

completeness: unknown. Targets: antibioticmech:aro-72f1180eb7.

Original abstracts identify S. tendae HKI-179 and C biosynthesis, but detailed original 2004/2005 experiments were not inspected. The local MIBiG CS113 entry has a different exact structure key and does not justify an automatic producer addition or identity substitution. Absence of the native producer slot is not a confirmed required-field error.

### Actual source ownership and preserved provenance

ownership: supported. Targets: antibioticmech:aro-72f1180eb7.

ARO source extraction and PubChem enrichment own the generated identity/class fields; primary additions are curator-owned on the exact C record. All eighteen captured input hashes remain unchanged. SEEDED history is preserved; successful deterministic checks do not constitute native REVIEWED sign-off.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

If enriching cervimycin C, add claim-specific activity, resistance and mechanism evidence while preserving exact material and experimental limitations.

- Use original C columns and strain-level protocols; do not copy sibling D values, pH-dependent values into unadjusted assays, or a repeated 2022 table as an independent 2024 experiment.
- Represent the 2024 result as gyrase holoenzyme supercoiling inhibition at the tested concentrations. Do not label it direct GyrB binding, a measured Kd or the proven low-concentration lethal mechanism.
- Keep BmrA promoter/RNA-stability evidence and Clp/WalK genetic effects as resistance evidence. RNAP–promoter binding is not antibiotic–RNAP binding, and purified C transport by BmrA was not established in the inspected study.
- Separate 2022 resistant-mutant omics from 2024 drug-treated-cell omics. A Figure 7 hypothesis or response-gene correlation must not become an unqualified direct causal edge. Run applicable structured-source cross-checks when curating named proteins or datasets.
- Preserve the native/database versus published-drawing keto-enol representation boundary and the original absolute-stereochemical access limitation. Do not replace the structure or import the MIBiG producer solely on a label match.
- Any later curation must follow native claim-evidence/history/status rules and rerun focused validators and applicable corpus gates. Optional enrichment is not itself a corrective finding.

### A2

For a later producer or structural-proof enrichment, inspect the original C isolation and biosynthesis papers and reconcile exact material and organism scope.

- Verify original 2004/2005 figures, chemical degradation and feeding methods before claiming complete experimental absolute-configuration or pathway proof.
- Distinguish S. tendae HKI-179 primary material from the local CS113 cluster record. A name match and canonical tautomer diagnostic do not authorize merging exact structures or substituting a producer.
- Retain the absence of independently inspected supplemental data and do not turn article access failures into negative biological evidence.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cervimycin-c.yaml; Whole YAML, including all three history events. | supports | SEEDED, MINTED and ANTIBACTERIAL. Neutral formula C61H81NO25, charge zero, key CYKZTBKVWQAQLU-KSQSWLAPSA-N. Native fields do not assert a molecular target, resistance determinant, MIC, producer, clinical approval, causal graph or transcriptomic dataset. Missing optional enrichment is not automatically a defect. |
| source | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py; ARO row 489, PubChem row 199 and exact source selection, class normalization, fallback structure, identity and definition emission. | supports | ARO:3007603 supplies the C name, family definition, PMID:36173303 and xrefs. Its drug class ARO:3005171 becomes the structural parent; the family parent ARO:3007600 is retained in source context. PubChem CID 54687465 supplies structure. CHEBI:208953 is not in the adopted ChEBI inventory, so MINTED follows the inspected resolution rule despite a current matching external ChEBI entry. No source-field inconsistency was established. |
| official | https://card.mcmaster.ca/aro/3007603; https://card.mcmaster.ca/aro/3005171; https://www.ebi.ac.uk/chebi/CHEBI:208953; https://pubchem.ncbi.nlm.nih.gov/compound/54687465; Complete current ARO molecule/class entries, complete visible ChEBI identity entry, official PubChem PUG property response and four independent structure parses. | supports | All asserted xrefs resolve consistently to C, and the ARO parent is the broader polyketide antibiotic class. ChEBI and PubChem reproduce the full native key and neutral carbamoyl/dimethylmalonyl structure. ChEBI is a third-party MetaboLights submission; its chemical agreement does not independently certify the original absolute-stereochemical elucidation. ChEBI reports Streptomyces with PMID:15326518 as a producer lead. |
| tautomer | PMID:36173303, Figure 1; PMID:38722162, Figure 1; Both original Figure 1 images inspected visually against the native graph and the official database encodings. | context_only | The drawings identify C by its carbamoyl group and dimethylmalonyl ester and show an alternative A-ring keto-enol placement relative to the native/PubChem/ChEBI structure. The 2022 caption explicitly says relative configuration. A scratch-only local keto-enol relocation regenerates the distinct local MIBiG key XANNJZUQOYYGNE-KSQSWLAPSA-N. This is a representation limit, not evidence of a different congener or inverted stereochemistry. No native structure substitution or identity merge is justified by it. |
| mibig-context | data/raw/mibig_producers.tsv; scripts/extract_mibig_producers.py; scripts/seed_from_sources.py; Local row 685 for BGC0001439, compound index 4 of 5; exact-key producer join and source taxonomy fields. | context_only | The local row calls the compound cervimycin C but uses XANNJZUQOYYGNE-KSQSWLAPSA-N and Streptomyces sp. CS113, with questionable source quality and gene-expression-correlated production evidence. The seeder requires an exact full-key match; the row does not match the native key and is not imported. It is not a native producer claim or proof that a required producer was omitted. A future producer addition must independently resolve exact material, organism and evidence scope rather than copying this local name match. |
| discovery | PMID:15940739; DOI:10.1002/chem.200500320; PMID:15326518; DOI:10.1039/B409221J; Complete original indexed abstracts, with publisher title/DOI checks; original 2004/2005 full structural papers inaccessible. | partial | The 2005 discovery abstract reports A–D antibacterial glycosides from Streptomyces tendae, with NMR/degradation structure work and activity against resistant Gram-positive organisms. The 2004 original abstract specifically identifies C as the major HKI-179 product with six trideoxysugars and a dimethylmalonyl residue; feeding/molecular studies attribute that unit to valine. These support exact C producer/biosynthetic context at abstract depth, not a fully inspected stereochemical derivation or all biosynthetic reaction steps. |
| activity2022 | PMID:36173303; DOI:10.1128/spectrum.02567-22; https://pmc.ncbi.nlm.nih.gov/articles/PMC9603734/; Complete main narrative, main tables and figure captions; Table 1 and antimicrobial susceptibility Methods. Figure 1 additionally inspected visually during C review. | supports | Table 1 directly reports C MICs: B. subtilis 168, 0.25 µg/mL; S. aureus SG511 Berlin, 2; methicillin-resistant S. aureus N315, 4; vancomycin-resistant E. faecium BM4147, 2. C and D columns are distinct. Table 1 uses Mueller Hinton broth and 24 h incubation; Methods specify cation-adjusted medium, 5e5 CFU/mL, 37 C and the lowest concentration preventing visible growth. Unadjusted-medium values must not be conflated with Table 2 pH experiments. Supplemental MBC tables were not independently inspected. |
| resistance2022 | PMID:36173303, mutant construction, Tables 3/5/6 and Discussion; Complete original resistance and functional narrative with exact C/D-selected lineages distinguished. | supports | CmR01–06 were selected with C and CmR07–09 with D. Reconstruction/deletion experiments show bounded C susceptibility changes from ClpP/ClpC and WalK perturbations; the single DnaK A112P reconstruction has no MIC effect. C does not alter wild-type ClpXP activity in the reported substrate assay, and direct WalK effects were unreproducible. Mutant resistance and reduced mutant kinase/protease function do not prove direct drug binding to those proteins. The 2022 omics compares resistant mutant/revertant with parent, not drug-treated with untreated cells. |
| bmrA2010 | PMID:21077936; DOI:10.1111/j.1574-6968.2010.02143.x; https://genome.imb-jena.de/publications/download/free/Kruegel_2010.pdf; Complete main narrative and figure captions read from author-institution full PDF; pages 155 and 160 inspected visually to verify units and mutation dissection. Supplemental tables not inspected. | supports | B. subtilis 168 derivatives 8R/IR carry a bmrA promoter -35 change plus a +6 untranslated-region change. Reporter, RNAP–DNA interaction, transcription, RNA-stability and protein experiments distinguish the contributions. Reconstructed -35-only material grows at 3 µM C, while the double mutation supports growth at 5 µM; +6 alone does not confer that phenotype. These are growth/resistance experiments, not MICs of a purified enzyme. Direct transport of C by purified BmrA was not measured here; RNAP–promoter binding is not C–RNAP binding. The producer MFS statement cites unpublished data and is not a supported native producer-resistance addition. |
| gyrase2024 | PMID:38722162; DOI:10.1128/msphere.00764-23; https://pmc.ncbi.nlm.nih.gov/articles/PMC11237698/; Complete main narrative/tables/captions and original Figure 4 inspected; cloning, holoenzyme supercoiling and antisense susceptibility Methods read. | supports | Reconstituted S. aureus SG511 GyrA/GyrB and commercial E. coli gyrase are tested by a relaxed-DNA supercoiling assay. The authors report significant S. aureus inhibition beginning at 100 µM C and near-total inhibition at 400 µM, roughly 62.5× and 250× their reference whole-cell MIC. The GyrB antisense clone has a 1.45-fold inhibition-zone diameter increase, which is not a 1.45-fold MIC change or proof of direct GyrB binding. The biochemical experiment measures holoenzyme activity, not an isolated GyrB binding site, dissociation constant or low-concentration lethal mechanism. |
| response2024 | PMID:38722162, cellular experiments and Figures 3, 6 and 7; Complete main narrative and Methods; Figures 1, 3, 4, 6 and 7 inspected visually. | supports | S. aureus SG511 exposed to 3× MIC C for 1 h shows cell/septum abnormalities and a drug-versus-DMSO transcriptomic response involving CtsR/HrcA and autolysin genes, without the canonical gyrase-inhibitor response. B. subtilis microscopy uses 8× MIC. Toeprinting at 50 µM did not demonstrate translation arrest, and tested potassium-efflux conditions did not show a pore-forming response. Figure 7 presents possible mistranslation, inactive autolysins and downstream stress as a model; its question-mark arrows are not experimentally proven causal edges. These findings do not justify declaring C a proven ribosome, WalK or ClpP inhibitor. |
| search | 276-inclusive-hits.txt; bounded exact C primary-paper discovery and retrieval manifests; Local exact identifier/label/slug/key/mint search includes hidden and ignored files. | context_only | Relevant hits include native/source rows, MIBiG context, readiness queue and generated indexes/embeddings. No exact curator overlay or decision was found in the stated scope. Public searches recovered the 2010 author PDF and complete 2022/2024 main XML/figures. 2004/2005 full text and 2022/2024 supplemental PDFs remain unavailable through the inspected routes. The record itself names no gene/protein/pathway/response/dataset, so no native structured-adapter trigger applied before web research. |
| validation | 276-schema.log; 276-strict.log; 276-strict.tsv; 276-chemistry.json; 276-xref-chemistry.json; 276-local-tautomer-check.json; Actual focused validation and independent chemical diagnostic outputs. | supports | Schema and strict validation exit 0. Native SMILES/InChI reproduce full key, formula, charge and masses; the ARO mint matches. Four official external encodings agree. The scratch local keto-enol change independently explains the different MIBiG key without modifying the record. Broader tautomer enumeration reached a transform limit and is not used as exhaustive identity proof. A failed ad hoc context-capture attempt with system python lacked yaml; the successful capture used the locked batch028 interpreter, preserving every prior hash. |

## Limits And Additional Notes

- Full original 2004 and 2005 structural/biosynthetic papers were not accessible. Their complete original indexed abstracts and publisher metadata were inspected, but no full stereochemical derivation or detailed BGC mapping is claimed.
- The 2022 and 2024 main narratives, main tables and captions were read. C structure figures and selected 2024 mechanism figures were inspected visually. Supplemental PDF routes returned challenge HTML rather than PDF files; no supplemental MBC table, kill-curve image or full differential-expression table was independently verified.
- The 2010 primary main narrative and captions were read from the author-institution PDF, with pages 155 and 160 visually checked for mutation and concentration units. Its supplemental cross-resistance and primer tables were not read.
- The papers depict an alternative A-ring keto-enol form and the 2022 caption specifies relative configuration. Official database agreement supports the native mapping but does not prove that a single tautomer or absolute form was experimentally isolated in every assay.
- The 2024 main-text assay recipe contains potentially problematic mass-unit renderings for some biochemical reagents. Numeric recipe details beyond the verified endpoint/concentration framework were not transcribed or silently corrected. No native field depends on those recipe values.
- Dataset accessions reported by the papers were not independently audited at the repository level; no dataset is added or asserted to contain a particular sample. The record itself has no native structured-adapter trigger.
- The local MIBiG name match is contextual, uses a different full key and does not establish a native omission. The limited tautomer-enumeration diagnostic is not an exhaustive chemical identity proof.
- No paid source, provider research, article purchase, author contact or external mutation was used. Scientific completion is partial, and no deterministic pass promotes the native record to REVIEWED.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T124006Z-cervimycin-c
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cervimycin C: coherent identity and direct antibacterial evidence with bounded
  mechanism and tautomer scope'
started_at: '2026-10-21T12:20:05Z'
finished_at: '2026-10-21T12:40:06Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the seed. Read the entire native record, actual
    ARO/PubChem rows, source logic and relevant local MIBiG context, independently
    parsed official structures, and inspected original 2010, 2022 and 2024 studies
    at the documented depth. Initial source capture preceded judgment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The native neutral cervimycin C graph and all asserted identifiers agree
  with official ChEBI/PubChem structures. The adopted 2022 paper directly supports
  antibacterial activity of C as well as the general polyketide description. Primary
  follow-up provides resistance genetics, high-concentration gyrase inhibition and
  drug-response observations, but does not establish a single low-concentration molecular
  mechanism. The papers draw an alternative A-ring keto-enol form, so exact experimental
  chemical-form and structural-proof limits remain explicit. No confirmed corrective
  finding emerged; optional enrichment requires careful separation of direct assays,
  resistance determinants and hypotheses. Scientific assessment retains the stated
  evidence limits; full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/cervimycin-c.yaml
    sha256: 123c0f78fa0a130dd0c252054cb978939a3ecbad29c4e07563e50efaf21a8b33
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
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
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
  - path: scripts/extract_mibig_producers.py
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
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
- target_id: antibioticmech:aro-72f1180eb7
  path: data/antibiotics/antibacterial/cervimycin-c.yaml
  label: cervimycin C
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction and hierarchy normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Maintained ARO identity, definition, class and literature lead row
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Maintained PubChem exact structure row linked by ARO identifier
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure enrichment owner
scope:
  description: 'Whole native YAML: label and mint, antibacterial filing, definition
    and sole PMID, structural class/parent, every chemical descriptor and three xrefs,
    the source concept and all three history events. Actual maintained ARO/PubChem
    rows and relevant extractor/enricher/seeder logic were inspected. Every adopted
    literature lead was assessed.'
  selection: Queue 276; all thirteen original input hashes were preserved. Actual
    ARO/PubChem inventories and PubChem enrichment script were appended, followed
    by two local MIBiG context inputs, for eighteen captured inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-72f1180eb7
  exclusions:
  - target: Cervimycin A, B, D and K congeners, bulk cervimycin complex and other
      tetracyclic antibiotics
    reason: These are different compounds or preparations. Sibling potency, biosynthetic
      transformations and comparator target mechanisms cannot be assigned to exact
      C without compound-specific evidence.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: No schema issues found.
  target_ids:
  - antibioticmech:aro-72f1180eb7
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cervimycin-c.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: One record scanned; zero strict errors.
  target_ids:
  - antibioticmech:aro-72f1180eb7
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cervimycin-c.yaml --out /private/tmp/am-review-session/276-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Native encodings, formula, charge, masses and stable ARO mint agree. Run
    from batch028 using the batch019 RDKit interpreter.
  target_ids:
  - antibioticmech:aro-72f1180eb7
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 276
  exit_code: 0
  expected_exit_code: 0
- check_id: official-structure-check
  name: official-structure-check
  status: passed
  required: false
  summary: Four official ChEBI/PubChem encodings independently reproduce the full
    native key.
  target_ids:
  - antibioticmech:aro-72f1180eb7
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/276-xref-check.py
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
  - antibioticmech:aro-72f1180eb7
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
  - antibioticmech:aro-72f1180eb7
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
  - antibioticmech:aro-72f1180eb7
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
  - antibioticmech:aro-72f1180eb7
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
  - antibioticmech:aro-72f1180eb7
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
  - antibioticmech:aro-72f1180eb7
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
  - antibioticmech:aro-72f1180eb7
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
  - antibioticmech:aro-72f1180eb7
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
  - antibioticmech:aro-72f1180eb7
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cervimycin-c.yaml
  locator: Whole YAML, including all three history events.
  accessed_at: '2026-10-21T12:37:09Z'
  support: supports
  summary: SEEDED, MINTED and ANTIBACTERIAL. Neutral formula C61H81NO25, charge zero,
    key CYKZTBKVWQAQLU-KSQSWLAPSA-N. Native fields do not assert a molecular target,
    resistance determinant, MIC, producer, clinical approval, causal graph or transcriptomic
    dataset. Missing optional enrichment is not automatically a defect.
- evidence_id: source
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; conf/sources.yaml;
    scripts/extract_source_inventory.py; scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py
  locator: ARO row 489, PubChem row 199 and exact source selection, class normalization,
    fallback structure, identity and definition emission.
  accessed_at: '2026-10-21T12:37:09Z'
  support: supports
  summary: ARO:3007603 supplies the C name, family definition, PMID:36173303 and xrefs.
    Its drug class ARO:3005171 becomes the structural parent; the family parent ARO:3007600
    is retained in source context. PubChem CID 54687465 supplies structure. CHEBI:208953
    is not in the adopted ChEBI inventory, so MINTED follows the inspected resolution
    rule despite a current matching external ChEBI entry. No source-field inconsistency
    was established.
  snapshot_sha256: 33d92d3bc830b4110d8f05c1d5e50701fca7a95069a6b6c50bc0df30b76096ab
- evidence_id: official
  kind: database
  reference: https://card.mcmaster.ca/aro/3007603; https://card.mcmaster.ca/aro/3005171;
    https://www.ebi.ac.uk/chebi/CHEBI:208953; https://pubchem.ncbi.nlm.nih.gov/compound/54687465
  locator: Complete current ARO molecule/class entries, complete visible ChEBI identity
    entry, official PubChem PUG property response and four independent structure parses.
  accessed_at: '2026-10-21T12:32:14Z'
  support: supports
  summary: All asserted xrefs resolve consistently to C, and the ARO parent is the
    broader polyketide antibiotic class. ChEBI and PubChem reproduce the full native
    key and neutral carbamoyl/dimethylmalonyl structure. ChEBI is a third-party MetaboLights
    submission; its chemical agreement does not independently certify the original
    absolute-stereochemical elucidation. ChEBI reports Streptomyces with PMID:15326518
    as a producer lead.
  snapshot_sha256: 6bc0879bec91b15c1cb8e7e637795c5d0fca19144b872058e7b83112c73352eb
- evidence_id: tautomer
  kind: primary_source
  reference: PMID:36173303, Figure 1; PMID:38722162, Figure 1
  locator: Both original Figure 1 images inspected visually against the native graph
    and the official database encodings.
  accessed_at: '2026-10-21T12:33:03Z'
  support: context_only
  summary: The drawings identify C by its carbamoyl group and dimethylmalonyl ester
    and show an alternative A-ring keto-enol placement relative to the native/PubChem/ChEBI
    structure. The 2022 caption explicitly says relative configuration. A scratch-only
    local keto-enol relocation regenerates the distinct local MIBiG key XANNJZUQOYYGNE-KSQSWLAPSA-N.
    This is a representation limit, not evidence of a different congener or inverted
    stereochemistry. No native structure substitution or identity merge is justified
    by it.
  snapshot_sha256: 3469b27b0f39bb86306077d873521b5c9a9b7229dd0ffc04696aebf72fc4ca40
- evidence_id: mibig-context
  kind: record_content
  reference: data/raw/mibig_producers.tsv; scripts/extract_mibig_producers.py; scripts/seed_from_sources.py
  locator: Local row 685 for BGC0001439, compound index 4 of 5; exact-key producer
    join and source taxonomy fields.
  accessed_at: '2026-10-21T12:37:09Z'
  support: context_only
  summary: The local row calls the compound cervimycin C but uses XANNJZUQOYYGNE-KSQSWLAPSA-N
    and Streptomyces sp. CS113, with questionable source quality and gene-expression-correlated
    production evidence. The seeder requires an exact full-key match; the row does
    not match the native key and is not imported. It is not a native producer claim
    or proof that a required producer was omitted. A future producer addition must
    independently resolve exact material, organism and evidence scope rather than
    copying this local name match.
  snapshot_sha256: 0d7b8c939ef546a35fe0e672eac16025e093f156613a01cc2c98e93d150cdaf9
- evidence_id: discovery
  kind: primary_source
  reference: PMID:15940739; DOI:10.1002/chem.200500320; PMID:15326518; DOI:10.1039/B409221J
  locator: Complete original indexed abstracts, with publisher title/DOI checks; original
    2004/2005 full structural papers inaccessible.
  accessed_at: '2026-10-21T12:37:09Z'
  support: partial
  summary: The 2005 discovery abstract reports A–D antibacterial glycosides from Streptomyces
    tendae, with NMR/degradation structure work and activity against resistant Gram-positive
    organisms. The 2004 original abstract specifically identifies C as the major HKI-179
    product with six trideoxysugars and a dimethylmalonyl residue; feeding/molecular
    studies attribute that unit to valine. These support exact C producer/biosynthetic
    context at abstract depth, not a fully inspected stereochemical derivation or
    all biosynthetic reaction steps.
  snapshot_sha256: 9679f6e13b949f4c316df16943301a7aa6f9e148f41009391612043ce1b08893
- evidence_id: activity2022
  kind: primary_source
  reference: PMID:36173303; DOI:10.1128/spectrum.02567-22; https://pmc.ncbi.nlm.nih.gov/articles/PMC9603734/
  locator: Complete main narrative, main tables and figure captions; Table 1 and antimicrobial
    susceptibility Methods. Figure 1 additionally inspected visually during C review.
  accessed_at: '2026-10-21T12:29:02Z'
  support: supports
  summary: 'Table 1 directly reports C MICs: B. subtilis 168, 0.25 µg/mL; S. aureus
    SG511 Berlin, 2; methicillin-resistant S. aureus N315, 4; vancomycin-resistant
    E. faecium BM4147, 2. C and D columns are distinct. Table 1 uses Mueller Hinton
    broth and 24 h incubation; Methods specify cation-adjusted medium, 5e5 CFU/mL,
    37 C and the lowest concentration preventing visible growth. Unadjusted-medium
    values must not be conflated with Table 2 pH experiments. Supplemental MBC tables
    were not independently inspected.'
  snapshot_sha256: 571563deb53e4ecdf391db262053dd2c022534737f7d43a45cd131a90b397d35
- evidence_id: resistance2022
  kind: primary_source
  reference: PMID:36173303, mutant construction, Tables 3/5/6 and Discussion
  locator: Complete original resistance and functional narrative with exact C/D-selected
    lineages distinguished.
  accessed_at: '2026-10-21T12:29:02Z'
  support: supports
  summary: CmR01–06 were selected with C and CmR07–09 with D. Reconstruction/deletion
    experiments show bounded C susceptibility changes from ClpP/ClpC and WalK perturbations;
    the single DnaK A112P reconstruction has no MIC effect. C does not alter wild-type
    ClpXP activity in the reported substrate assay, and direct WalK effects were unreproducible.
    Mutant resistance and reduced mutant kinase/protease function do not prove direct
    drug binding to those proteins. The 2022 omics compares resistant mutant/revertant
    with parent, not drug-treated with untreated cells.
  snapshot_sha256: 571563deb53e4ecdf391db262053dd2c022534737f7d43a45cd131a90b397d35
- evidence_id: bmrA2010
  kind: primary_source
  reference: PMID:21077936; DOI:10.1111/j.1574-6968.2010.02143.x; https://genome.imb-jena.de/publications/download/free/Kruegel_2010.pdf
  locator: Complete main narrative and figure captions read from author-institution
    full PDF; pages 155 and 160 inspected visually to verify units and mutation dissection.
    Supplemental tables not inspected.
  accessed_at: '2026-10-21T12:33:19Z'
  support: supports
  summary: B. subtilis 168 derivatives 8R/IR carry a bmrA promoter -35 change plus
    a +6 untranslated-region change. Reporter, RNAP–DNA interaction, transcription,
    RNA-stability and protein experiments distinguish the contributions. Reconstructed
    -35-only material grows at 3 µM C, while the double mutation supports growth at
    5 µM; +6 alone does not confer that phenotype. These are growth/resistance experiments,
    not MICs of a purified enzyme. Direct transport of C by purified BmrA was not
    measured here; RNAP–promoter binding is not C–RNAP binding. The producer MFS statement
    cites unpublished data and is not a supported native producer-resistance addition.
  snapshot_sha256: 927af3f3c19d0dabbfca03b6fa3a4a249a322b5a3244b4c58f8a9068c3a724d0
- evidence_id: gyrase2024
  kind: primary_source
  reference: PMID:38722162; DOI:10.1128/msphere.00764-23; https://pmc.ncbi.nlm.nih.gov/articles/PMC11237698/
  locator: Complete main narrative/tables/captions and original Figure 4 inspected;
    cloning, holoenzyme supercoiling and antisense susceptibility Methods read.
  accessed_at: '2026-10-21T12:29:02Z'
  support: supports
  summary: Reconstituted S. aureus SG511 GyrA/GyrB and commercial E. coli gyrase are
    tested by a relaxed-DNA supercoiling assay. The authors report significant S.
    aureus inhibition beginning at 100 µM C and near-total inhibition at 400 µM, roughly
    62.5× and 250× their reference whole-cell MIC. The GyrB antisense clone has a
    1.45-fold inhibition-zone diameter increase, which is not a 1.45-fold MIC change
    or proof of direct GyrB binding. The biochemical experiment measures holoenzyme
    activity, not an isolated GyrB binding site, dissociation constant or low-concentration
    lethal mechanism.
  snapshot_sha256: 11d631592adff08922e27b8f95da1f03af5fd500e7941b381162f942ca8030a9
- evidence_id: response2024
  kind: primary_source
  reference: PMID:38722162, cellular experiments and Figures 3, 6 and 7
  locator: Complete main narrative and Methods; Figures 1, 3, 4, 6 and 7 inspected
    visually.
  accessed_at: '2026-10-21T12:33:03Z'
  support: supports
  summary: S. aureus SG511 exposed to 3× MIC C for 1 h shows cell/septum abnormalities
    and a drug-versus-DMSO transcriptomic response involving CtsR/HrcA and autolysin
    genes, without the canonical gyrase-inhibitor response. B. subtilis microscopy
    uses 8× MIC. Toeprinting at 50 µM did not demonstrate translation arrest, and
    tested potassium-efflux conditions did not show a pore-forming response. Figure
    7 presents possible mistranslation, inactive autolysins and downstream stress
    as a model; its question-mark arrows are not experimentally proven causal edges.
    These findings do not justify declaring C a proven ribosome, WalK or ClpP inhibitor.
  snapshot_sha256: daa538d4a30bd958fa43e8d66d6ec7f5ab8fe541ebd729dac4cf334882d50f81
- evidence_id: search
  kind: search
  reference: 276-inclusive-hits.txt; bounded exact C primary-paper discovery and retrieval
    manifests
  locator: Local exact identifier/label/slug/key/mint search includes hidden and ignored
    files.
  accessed_at: '2026-10-21T12:37:09Z'
  support: context_only
  summary: Relevant hits include native/source rows, MIBiG context, readiness queue
    and generated indexes/embeddings. No exact curator overlay or decision was found
    in the stated scope. Public searches recovered the 2010 author PDF and complete
    2022/2024 main XML/figures. 2004/2005 full text and 2022/2024 supplemental PDFs
    remain unavailable through the inspected routes. The record itself names no gene/protein/pathway/response/dataset,
    so no native structured-adapter trigger applied before web research.
  snapshot_sha256: cbcbc586265317e7275b4e6bc9f033ba6510900ae5754ce3144aee80765edd30
  search_scope: rg --no-ignore --hidden -n -F for ARO:3007603, cervimycin C, cervimycin-c,
    CYKZTBKVWQAQLU-KSQSWLAPSA-N, antibioticmech:aro-72f1180eb7 and CHEBI:208953 across
    data, curation, conf, scripts, src, docs, .claude, reviews and reports. Public
    exact name, original paper titles and DOI searches on 2026-10-21; official PubMed/PMC/Europe
    PMC/publisher pages and author-institution archive inspected.
- evidence_id: validation
  kind: validation
  reference: 276-schema.log; 276-strict.log; 276-strict.tsv; 276-chemistry.json; 276-xref-chemistry.json;
    276-local-tautomer-check.json
  locator: Actual focused validation and independent chemical diagnostic outputs.
  accessed_at: '2026-10-21T12:37:09Z'
  support: supports
  summary: Schema and strict validation exit 0. Native SMILES/InChI reproduce full
    key, formula, charge and masses; the ARO mint matches. Four official external
    encodings agree. The scratch local keto-enol change independently explains the
    different MIBiG key without modifying the record. Broader tautomer enumeration
    reached a transform limit and is not used as exhaustive identity proof. A failed
    ad hoc context-capture attempt with system python lacked yaml; the successful
    capture used the locked batch028 interpreter, preserving every prior hash.
  snapshot_sha256: 886f589fb3208a04d08749ea6c7a70cb591cb8371a7a76c0d5ca03e63ed2dd9e
assessments:
- assessment_id: identity
  area: identity
  topic: Exact C database identity and representation boundary
  outcome: supported
  summary: The native neutral carbamoyl/dimethylmalonyl graph, identifiers and source
    mint agree with current official structures. Published drawings use another A-ring
    keto-enol placement and do not independently establish the full native absolute
    stereochemical proof. Preserve this qualification; it is not a demonstrated wrong-congener
    or opposite-enantiomer error.
  target_ids:
  - antibioticmech:aro-72f1180eb7
  evidence_ids:
  - record
  - official
  - tautomer
  - validation
- assessment_id: filing
  area: scope
  topic: Antibacterial scope and broader polyketide parent
  outcome: supported
  summary: The parent denotes a broad chemical class and the adopted original C susceptibility
    experiments directly support antibacterial filing. C values are distinguished
    from D and from experimental pH variants. The record asserts no broad clinical
    susceptibility breakpoint or approval.
  target_ids:
  - antibioticmech:aro-72f1180eb7
  evidence_ids:
  - source
  - official
  - activity2022
- assessment_id: citation
  area: evidence
  topic: Sole adopted citation and experimental scope
  outcome: supported
  summary: PMID:36173303 is correctly identified and supports both the general description
    and C activity. Its resistance genetics and omics are useful enrichment evidence
    but do not by themselves establish direct Clp/WalK binding or a complete antimicrobial
    causal chain.
  target_ids:
  - antibioticmech:aro-72f1180eb7
  evidence_ids:
  - activity2022
  - resistance2022
- assessment_id: mechanism
  area: completeness
  topic: Optional direct target and phenotype enrichment
  outcome: unknown
  summary: The 2024 holoenzyme assay supports high-concentration gyrase inhibition.
    It does not identify a unique GyrB binding site or show that this effect explains
    killing near the MIC. Low-concentration transcriptional resemblance and the Figure
    7 model remain hypotheses. Since the seed makes no target claim, an optional mechanism
    gap is not a corrective finding.
  target_ids:
  - antibioticmech:aro-72f1180eb7
  evidence_ids:
  - record
  - gyrase2024
  - response2024
- assessment_id: resistance
  area: completeness
  topic: Optional resistance determinants and transcriptomic context
  outcome: supported
  summary: The 2010 bmrA mutation dissection and 2022 Clp/WalK experiments provide
    exact C resistance context with distinct organisms and experimental designs. Direct
    transport, drug binding, mutant phenotype and expression change must remain separate
    evidence types. No current native resistance assertion is wrong.
  target_ids:
  - antibioticmech:aro-72f1180eb7
  evidence_ids:
  - bmrA2010
  - resistance2022
  - response2024
- assessment_id: producer
  area: completeness
  topic: Producer and biosynthesis context
  outcome: unknown
  summary: Original abstracts identify S. tendae HKI-179 and C biosynthesis, but detailed
    original 2004/2005 experiments were not inspected. The local MIBiG CS113 entry
    has a different exact structure key and does not justify an automatic producer
    addition or identity substitution. Absence of the native producer slot is not
    a confirmed required-field error.
  target_ids:
  - antibioticmech:aro-72f1180eb7
  evidence_ids:
  - discovery
  - mibig-context
  - tautomer
- assessment_id: ownership
  area: ownership
  topic: Actual source ownership and preserved provenance
  outcome: supported
  summary: ARO source extraction and PubChem enrichment own the generated identity/class
    fields; primary additions are curator-owned on the exact C record. All eighteen
    captured input hashes remain unchanged. SEEDED history is preserved; successful
    deterministic checks do not constitute native REVIEWED sign-off.
  target_ids:
  - antibioticmech:aro-72f1180eb7
  evidence_ids:
  - source
  - search
  - validation
findings: []
actions:
- action_id: A1
  description: If enriching cervimycin C, add claim-specific activity, resistance
    and mechanism evidence while preserving exact material and experimental limitations.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-72f1180eb7
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cervimycin-c.yaml
    role: Curator-owned exact C primary activity, resistance, target and causal evidence
  acceptance_checks:
  - Use original C columns and strain-level protocols; do not copy sibling D values,
    pH-dependent values into unadjusted assays, or a repeated 2022 table as an independent
    2024 experiment.
  - Represent the 2024 result as gyrase holoenzyme supercoiling inhibition at the
    tested concentrations. Do not label it direct GyrB binding, a measured Kd or the
    proven low-concentration lethal mechanism.
  - Keep BmrA promoter/RNA-stability evidence and Clp/WalK genetic effects as resistance
    evidence. RNAP–promoter binding is not antibiotic–RNAP binding, and purified C
    transport by BmrA was not established in the inspected study.
  - Separate 2022 resistant-mutant omics from 2024 drug-treated-cell omics. A Figure
    7 hypothesis or response-gene correlation must not become an unqualified direct
    causal edge. Run applicable structured-source cross-checks when curating named
    proteins or datasets.
  - Preserve the native/database versus published-drawing keto-enol representation
    boundary and the original absolute-stereochemical access limitation. Do not replace
    the structure or import the MIBiG producer solely on a label match.
  - Any later curation must follow native claim-evidence/history/status rules and
    rerun focused validators and applicable corpus gates. Optional enrichment is not
    itself a corrective finding.
- action_id: A2
  description: For a later producer or structural-proof enrichment, inspect the original
    C isolation and biosynthesis papers and reconcile exact material and organism
    scope.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-72f1180eb7
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cervimycin-c.yaml
    role: Curator-owned primary producer and identity evidence
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/mibig_producers.tsv
    role: Conditional context to investigate; not an adopted producer assertion for
      this record
  acceptance_checks:
  - Verify original 2004/2005 figures, chemical degradation and feeding methods before
    claiming complete experimental absolute-configuration or pathway proof.
  - Distinguish S. tendae HKI-179 primary material from the local CS113 cluster record.
    A name match and canonical tautomer diagnostic do not authorize merging exact
    structures or substituting a producer.
  - Retain the absence of independently inspected supplemental data and do not turn
    article access failures into negative biological evidence.
limitations:
- Full original 2004 and 2005 structural/biosynthetic papers were not accessible.
  Their complete original indexed abstracts and publisher metadata were inspected,
  but no full stereochemical derivation or detailed BGC mapping is claimed.
- The 2022 and 2024 main narratives, main tables and captions were read. C structure
  figures and selected 2024 mechanism figures were inspected visually. Supplemental
  PDF routes returned challenge HTML rather than PDF files; no supplemental MBC table,
  kill-curve image or full differential-expression table was independently verified.
- The 2010 primary main narrative and captions were read from the author-institution
  PDF, with pages 155 and 160 visually checked for mutation and concentration units.
  Its supplemental cross-resistance and primer tables were not read.
- The papers depict an alternative A-ring keto-enol form and the 2022 caption specifies
  relative configuration. Official database agreement supports the native mapping
  but does not prove that a single tautomer or absolute form was experimentally isolated
  in every assay.
- The 2024 main-text assay recipe contains potentially problematic mass-unit renderings
  for some biochemical reagents. Numeric recipe details beyond the verified endpoint/concentration
  framework were not transcribed or silently corrected. No native field depends on
  those recipe values.
- Dataset accessions reported by the papers were not independently audited at the
  repository level; no dataset is added or asserted to contain a particular sample.
  The record itself has no native structured-adapter trigger.
- The local MIBiG name match is contextual, uses a different full key and does not
  establish a native omission. The limited tautomer-enumeration diagnostic is not
  an exhaustive chemical identity proof.
- No paid source, provider research, article purchase, author contact or external
  mutation was used. Scientific completion is partial, and no deterministic pass promotes
  the native record to REVIEWED.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
