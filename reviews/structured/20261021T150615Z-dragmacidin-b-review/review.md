# Dragmacidin B: replace G-derived claims and preserve the documented trans structure

- Review: 20261021T150615Z-dragmacidin-b-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:43:52Z
- Finished UTC: 2026-10-21T15:06:15Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native and both adopted chemical authorities agree on a neutral B connectivity with two unspecified piperazine stereocentres. Primary depictions identify trans B, so the graph omits a documented relative-configuration constraint. A separate major finding concerns the G definition and G/H activity literature attached to B. The reviewed B-specific biological experiments concern mammalian cells; they do not establish an antibacterial phenotype or direct PP1 inhibition for B.

## Scope And Provenance

Entire native YAML: identity, label, filing class, full definition and citation, parent/class grounding, every chemical descriptor and all three xrefs, source concept and deterministic mint, and all three history events. Both adopted compound literature leads were read. B-specific primary discovery, synthesis and experimental activity were evaluated separately from other congeners.

Selection: Queue position 375, one exact record. Thirteen original input hashes are preserved, with three actual source/enrichment inputs appended before assessment for sixteen total.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-2c3e119979 | data/antibiotics/antibacterial/dragmacidin-b.yaml | generated | dragmacidin B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | antibioticmech:aro-2c3e119979 | Actual focused schema validation passed. |
| strict | passed | True | antibioticmech:aro-2c3e119979 | Actual focused strict validation passed. |
| initial-chemistry | failed | False | antibioticmech:aro-2c3e119979 | Actual scratch diagnostic exited 1 solely because RDKit average mass 502.254 differs from stored 502.2 by 0.054, exceeding its fixed half-last-digit 0.05 tolerance. All key, formula, charge, monoisotopic mass and deterministic mint comparisons pass. Current PubChem also reports 502.2; the subsequent authority comparison preserves this numerical-model/rounding boundary without inventing a native mass defect. |
| authority-chemistry | passed | False | antibioticmech:aro-2c3e119979 | Native encodings, PubChem SMILES and ChEMBL molfile independently produce the same unassigned full key, formula, charge and monoisotopic mass. Native average mass exactly matches current PubChem. |
| figure-comparison | passed | False | antibioticmech:aro-2c3e119979 | Manual mapping of the original 2018 B drawing gives the trans R/S graph. Inverting both centres produces the same meso key, distinguishing a known relative-configuration constraint from a choice of enantiomer. |
| Authoritative full QC | failed | True | antibioticmech:aro-2c3e119979 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-2c3e119979 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-2c3e119979 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-2c3e119979 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-2c3e119979 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-2c3e119979 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-2c3e119979 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-2c3e119979 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-2c3e119979 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Connectivity, relative stereochemistry and all exact xrefs

identity: concern. Targets: antibioticmech:aro-2c3e119979.

Both chemical authorities agree with the native connectivity, but all omit the trans constraint independently depicted for B in the 2005 synthesis and 2018 isolation papers. A full stereochemical structure would preserve that constraint. The current unspecified graph does not establish mixture composition.

### Congener-specific definition and adopted citation placement

evidence: concern. Targets: antibioticmech:aro-2c3e119979.

Both source leads concern G/H, while the native definition expressly describes G. Neither its chemical description nor its biological panel is evidence for B. This upstream error needs a maintained exact-B definition/citation correction.

### Filing class and B-specific biological scope

evidence: unknown. Targets: antibioticmech:aro-2c3e119979.

The structural bis-indole parent is appropriate at connectivity level. Exact-B antibacterial support was not established in the bounded reading. The 2018 tumor-cell study is real B evidence, but it is neither a bacterial phenotype nor positive purified-PP1 inhibition at the tested concentration. No universal B inactivity or compulsory exclusion is inferred.

### Mode, targets, resistance, producer and dataset scope

evidence: not_applicable. Targets: antibioticmech:aro-2c3e119979.

No native protein, gene, pathway, mechanism or transcriptomic assertion triggers a structured adapter. The newly encountered mammalian phosphatase/cell-cycle experiments remain research context, with no microbial-target transfer. Sponge extraction is not a demonstration of sponge biosynthesis.

### Generated ownership, history and completeness

provenance: supported. Targets: antibioticmech:aro-2c3e119979.

All present fields and history entries were checked against actual source owners. MINTED/SEEDED remains appropriate for unresolved scientific support. Missing optional biological slots are not separate defects. Original hashes and ignored-inclusive absence-search scope are preserved.

## Findings

### F1: Replace the G definition and biological claims attached to B

major / open / confirmed; issue key: dragmacidin-b-definition-transferred-from-g.

The B-labelled record carries a paragraph explicitly about dragmacidin G, including a pyrazine and sulfur-containing side chain absent from the B piperazine graph. Both adopted primary citations concern G/H. Replace or qualify these source-derived claims for the exact B congener; do not relabel the B graph as G or transfer the G experimental panel to B.

### F2: Retain the documented trans relative configuration of dragmacidin B

major / open / confirmed; issue key: dragmacidin-b-missing-documented-trans-configuration.

Native SMILES and Standard InChI leave both piperazine centres unassigned, as do the adopted PubChem and ChEMBL records. The independently inspected 2005 Scheme 2 and 2018 Figure 1 identify B with opposite-face indolyl substituents. The trans graph maps to meso R/S stereochemistry, with the same full key after simultaneous inversion. The native representation therefore lacks a known relative-configuration constraint; no mixture or opposite-enantiomer claim follows from the omission.

## Recommended Actions And Acceptance Checks

### A1

Supply an exact-B definition and review the antibacterial filing using compound-specific evidence.

- Remove the G paragraph from the B source path and attach a supported B identity definition with the correct primary citation. Keep G/H activity with those actual congeners.
- Establish exact-B antimicrobial evidence or document a bounded curator scope decision if it remains unsupported. Host-cell GI50, phosphatase models and antibacterial family membership are insufficient alone.
- Regenerate, inspect the resulting definition/citation and run schema, strict and source reproduction checks.

### A2

Resolve the exact-B trans representation through maintained chemical input and xref qualification.

- Use the primary B structure and atom mapping to preserve trans relative geometry. GRBPIEOBAMGKFD-SZPZYZBQSA-N is the independently mapped depicted graph, not an instruction to copy a database blindly.
- Keep connectivity-only PubChem/ChEMBL provenance explicit; assess whether existing exact-xref semantics remain valid for the refined structure and qualify broader identifiers where required. Do not infer or create a racemate/mixture record.
- Regenerate from an evidence-supported maintained identity input, reparse both chemical encodings and check full stereochemical agreement, formula, charge, mint, schema/strict and source reproduction.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/dragmacidin-b.yaml; Entire native YAML. | supports | ARO-derived MINTED/SEEDED dragmacidin B encodes C22H22Br2N4, neutral, GRBPIEOBAMGKFD-UHFFFAOYSA-N. Both piperazine stereocentres are unspecified. Its definition explicitly names G and describes a different pyrazine/sulfur-containing structure. No synonyms, quantitative activity, mode, targets, resistance, producers, datasets, clinical claims or causal graphs are present. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/extract_source_inventory.py; scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py; conf/sources.yaml; Complete exact ARO row 543 and PubChem row 236; relevant extraction, structure fallback and definition-source selection code. | supports | ARO supplies the label, class, G paragraph, both PMID references and chemical xrefs. PubChem provides the unassigned structure. The seeder copies the definition and selects PMID28085024, the first adopted reference. Isomeric SMILES and InChI are requested by the PubChem configuration, so the missing stereochemistry is already present in the adopted upstream record. The deterministic mint and all three seed/reseed events agree. No ChEBI row owns this record. |
| aro | ARO:3007775; ARO:3007773; https://raw.githubusercontent.com/arpcard/aro/master/src/ontology/aro.obo; Complete current B and broader class term blocks. | supports | Current ARO reproduces the same G paragraph, G/H citations, parent class and exact PubChem/ChEMBL accessions. The parent is structurally broader, but its antibiotic-activity wording is not independent experimental evidence for B. This confirms upstream provenance of the congener transfer. |
| pubchem | PubChem:14467479; Complete official chemical property response and independently parsed SMILES/InChI. | supports | The current source has the same formula, charge, masses, unassigned SMILES and full Standard InChIKey as the native record. It contains no trans/cis constraint. This supports source reproduction and connectivity but cannot resolve the narrower natural-product relative configuration. |
| chembl | CHEMBL4159271; Complete molecule response; canonical SMILES, Standard InChI and molfile independently checked. | supports | ChEMBL encodes the same neutral connectivity and unassigned full key, with average mass 502.25. Its molfile also leaves the two piperazine centres unassigned. Agreement between chemical databases therefore does not independently establish that the graph specifies the documented trans natural product. |
| g2017 | PMID:28085024; DOI:10.3390/md15010016; PMC5295236; Complete original main prose, structural-analysis table and assay methods read. | refutes | This primary study isolates and tests G, C23H19Br2N7S, with a pyrazine and guanidinoethylthio group. Its bacterial, mycobacterial, malaria and pancreatic-cell results are not B experiments. The native paragraph closely follows this G report and must not be transferred to B. The paper explicitly distinguishes untested pyruvate-kinase activity of G from results on other bis-indoles. |
| gh2024 | PMID:38206835; DOI:10.1021/acs.orglett.3c04039; Complete indexed and publisher abstract, not full original paper. | refutes | The study synthesizes G/H and tests them and analogues against S. aureus and an efflux-deficient Salmonella Typhimurium strain. The abstract gives no B-specific result. It cannot repair the G-to-B definition transfer. |
| ab2018 | PMID:30023878; DOI:10.1021/acsomega.7b01786; Complete main text, Tables 1–3 and methods read; original Figure 1 compound 4 visually inspected. XML under PMC6045348; current article HTML resolves to PMC6645895 for the same DOI. | context_only | The paper independently isolates B as compound 4 and compares its NMR/MS with earlier B reports. Figure 1 depicts trans B. Table 2 reports B GI50 values 20.3, 19.3 and 28.0 micromolar in A549, HT29 and MDA-MB-231 tumor cells. At 10 micromolar, B leaves 102.3 +/- 13.0 percent PP1 activity, and the authors explicitly say B lacks significant inhibition in that enzyme assay. Cell-cycle/phosphorylation changes and docking do not turn this into measured direct PP1 binding or a microbial mechanism. No antibacterial experiment is reported. |
| trans-figure | DOI:10.1021/acsomega.7b01786 Figure 1 compound 4; 375-figure-check.py; Original image and independent atom mapping, with mirror comparison. | refutes | B has two N-methyl groups and two opposite-face indolyl bonds. Mapping those bonds gives R/S centres and GRBPIEOBAMGKFD-SZPZYZBQSA-N. Reversing both gives the same key because this graph is meso. The native graph omits the trans constraint altogether. The review does not infer a mixture, racemate or an opposite natural enantiomer from unassigned notation. |
| synthesis2005 | DOI:10.1016/j.tetlet.2005.02.054; https://www.stoltz2.caltech.edu/publications/43-2005.pdf; Complete four-page original author-hosted PDF text and experimental notes read; page 2423 Scheme 2 visually inspected. | supports | Scheme 2 labels compound 5 dragmacidin B and explicitly depicts trans relative geometry, independently of the 2018 drawing. The work prepares pyrazine 7 and is a formal synthesis using a previously established conversion, not a new B biological assay. The text and note 7 distinguish B from trans-dragmacidin C and cite the Horne reduction route. |
| synthesis2000 | PMID:11009377; DOI:10.1021/ol0001970; Complete indexed and publisher abstract; full paper and spectra were not accessed. | context_only | This synthesis specifically identifies B as compound 1, with separate piperazine and didebromo analogues. The abstract describes reduction/reductive methylation of the pyrazine precursor. It supports exact compound nomenclature and the 2005 formal-synthesis citation chain, but not an antibacterial assay. |
| patent | WO2001094310A1; https://patents.google.com/patent/WO2001094310A1/en; Original patent HTML introductory identity scope and Examples 14–19 read; scanned PDF downloaded but not independently read. | context_only | Example 18 expressly prepares dragmacidin B 4 in 70 percent yield and says its spectral data agree with natural B. Example 14 states trans diequatorial selectivity for its separate piperazine intermediate. These are synthesis/material context, not B-specific bacterial susceptibility data. The intermediate selectivity is not alone treated as proof of every downstream structure. |
| discovery | DOI:10.1016/S0040-4020(01)81355-7; Complete original publisher abstract as indexed by the web tool; full original paper unavailable. | context_only | The original report isolates dragmacidon B as compound 9 alongside dragmacidon A and topsentin C from Hexadella sp. The abstract describes proposed spectroscopic structures and A-specific L1210 cytotoxicity. It does not supply a B antibacterial result. Later uses of the dragmacidin spelling are not treated as a new compound solely on spelling. |
| search | 375-inclusive-hits.txt; 375-curation-hits.txt; Ignored-inclusive local search and bounded public exact-name literature follow-up. | context_only | No exact corrective overlay was found; the queue row retains both adopted G/H leads. Public searches for dragmacidin B and dragmacidon B with antibacterial/antimicrobial/trans/synthesis terms found the exact synthesis and host-cell studies but no inspected positive B bacterial endpoint. Dragmacidonamine B, crude sponge extracts, G/D activity and other bis-indole classes were not conflated with B. |
| validation | 375-schema.log; 375-strict.log; 375-chemistry.json; 375-xref-chemistry.json; 375-figure-chemistry.json; Actual checks and unchanged-input hash recheck. | supports | Schema and strict pass. Initial scratch chemistry exit 1 is retained transparently: its average-mass rounding threshold failed by 0.004 Da, while current PubChem exactly reproduces the stored 502.2. Native/authority graph comparison and manual trans/meso mapping pass. These checks establish representation facts, not activity or natural-product identity by themselves. |

## Limits And Additional Notes

- The original 1990 discovery and 2000 synthesis papers were accessible at complete-abstract depth only; 1994 and 2000 full publisher routes returned 403. The 2005 original four-page synthesis paper and 2018 main paper were read fully, with the relevant B structures visually checked.
- The 2018 supplementary spectra, microscopy and docking outputs were not independently reprocessed. The reported B tumor-cell GI50 values exceed the stated 20 micromolar assay starting concentration for two cell lines; this source-quality inconsistency is retained as a limit on optional quantitative reuse, not imported as a native-field defect.
- The patent was read only for introductory identity context and Examples 14–19. Its downloaded scanned PDF was not independently reviewed. Generic activity language in a synthesis patent is not treated as a measured B antibacterial endpoint.
- The bounded literature search did not find an inspected exact-B positive antibacterial endpoint. This is not an assertion that no such evidence exists or that B is inactive in every organism and assay.
- The average-mass scratch diagnostic failed its chosen precision threshold; current authority values and independent formula calculations show a rounding/model boundary. The original failed result remains recorded and is not silently converted to a pass.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native source or record was changed. Scientific curation should preserve the distinction between the exact trans B structure, the unspecified adopted authority encodings and the chemically distinct G activity claims.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T150615Z-dragmacidin-b-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Dragmacidin B: replace G-derived claims and preserve the documented trans
  structure'
started_at: '2026-10-21T14:43:52Z'
finished_at: '2026-10-21T15:06:15Z'
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
summary: The native and both adopted chemical authorities agree on a neutral B connectivity
  with two unspecified piperazine stereocentres. Primary depictions identify trans
  B, so the graph omits a documented relative-configuration constraint. A separate
  major finding concerns the G definition and G/H activity literature attached to
  B. The reviewed B-specific biological experiments concern mammalian cells; they
  do not establish an antibacterial phenotype or direct PP1 inhibition for B.
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
  - path: data/antibiotics/antibacterial/dragmacidin-b.yaml
    sha256: 8d0cf2cccb88afb22b75c7c1f936d2761b2386de6d1f66915d7baf965dd68ab4
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
- target_id: antibioticmech:aro-2c3e119979
  path: data/antibiotics/antibacterial/dragmacidin-b.yaml
  label: dragmacidin B
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction and source-specific qualification
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
    path: data/raw/pubchem_structures.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Actual maintained source input for the record
scope:
  description: 'Entire native YAML: identity, label, filing class, full definition
    and citation, parent/class grounding, every chemical descriptor and all three
    xrefs, source concept and deterministic mint, and all three history events. Both
    adopted compound literature leads were read. B-specific primary discovery, synthesis
    and experimental activity were evaluated separately from other congeners.'
  selection: Queue position 375, one exact record. Thirteen original input hashes
    are preserved, with three actual source/enrichment inputs appended before assessment
    for sixteen total.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-2c3e119979
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused schema validation passed.
  target_ids:
  - antibioticmech:aro-2c3e119979
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/dragmacidin-b.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual focused strict validation passed.
  target_ids:
  - antibioticmech:aro-2c3e119979
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/dragmacidin-b.yaml --out /private/tmp/am-review-session/375-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: initial-chemistry
  name: initial-chemistry
  status: failed
  required: false
  summary: Actual scratch diagnostic exited 1 solely because RDKit average mass 502.254
    differs from stored 502.2 by 0.054, exceeding its fixed half-last-digit 0.05 tolerance.
    All key, formula, charge, monoisotopic mass and deterministic mint comparisons
    pass. Current PubChem also reports 502.2; the subsequent authority comparison
    preserves this numerical-model/rounding boundary without inventing a native mass
    defect.
  target_ids:
  - antibioticmech:aro-2c3e119979
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 375
  exit_code: 1
  expected_exit_code: 0
- check_id: authority-chemistry
  name: authority-chemistry
  status: passed
  required: false
  summary: Native encodings, PubChem SMILES and ChEMBL molfile independently produce
    the same unassigned full key, formula, charge and monoisotopic mass. Native average
    mass exactly matches current PubChem.
  target_ids:
  - antibioticmech:aro-2c3e119979
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/375-xref-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: figure-comparison
  name: figure-comparison
  status: passed
  required: false
  summary: Manual mapping of the original 2018 B drawing gives the trans R/S graph.
    Inverting both centres produces the same meso key, distinguishing a known relative-configuration
    constraint from a choice of enantiomer.
  target_ids:
  - antibioticmech:aro-2c3e119979
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/375-figure-check.py
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
  - antibioticmech:aro-2c3e119979
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
  - antibioticmech:aro-2c3e119979
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
  - antibioticmech:aro-2c3e119979
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
  - antibioticmech:aro-2c3e119979
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
  - antibioticmech:aro-2c3e119979
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
  - antibioticmech:aro-2c3e119979
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
  - antibioticmech:aro-2c3e119979
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
  - antibioticmech:aro-2c3e119979
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
  - antibioticmech:aro-2c3e119979
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/dragmacidin-b.yaml
  locator: Entire native YAML.
  accessed_at: '2026-10-21T15:01:18Z'
  support: supports
  summary: ARO-derived MINTED/SEEDED dragmacidin B encodes C22H22Br2N4, neutral, GRBPIEOBAMGKFD-UHFFFAOYSA-N.
    Both piperazine stereocentres are unspecified. Its definition explicitly names
    G and describes a different pyrazine/sulfur-containing structure. No synonyms,
    quantitative activity, mode, targets, resistance, producers, datasets, clinical
    claims or causal graphs are present.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/extract_source_inventory.py;
    scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py; conf/sources.yaml
  locator: Complete exact ARO row 543 and PubChem row 236; relevant extraction, structure
    fallback and definition-source selection code.
  accessed_at: '2026-10-21T15:01:18Z'
  support: supports
  summary: ARO supplies the label, class, G paragraph, both PMID references and chemical
    xrefs. PubChem provides the unassigned structure. The seeder copies the definition
    and selects PMID28085024, the first adopted reference. Isomeric SMILES and InChI
    are requested by the PubChem configuration, so the missing stereochemistry is
    already present in the adopted upstream record. The deterministic mint and all
    three seed/reseed events agree. No ChEBI row owns this record.
  snapshot_sha256: 17eacc2f8f73e469d15c01613839b5217906e6c955cdf52fc3ad9cc07eda1970
- evidence_id: aro
  kind: database
  reference: ARO:3007775; ARO:3007773; https://raw.githubusercontent.com/arpcard/aro/master/src/ontology/aro.obo
  locator: Complete current B and broader class term blocks.
  accessed_at: '2026-10-21T14:50:57Z'
  support: supports
  summary: Current ARO reproduces the same G paragraph, G/H citations, parent class
    and exact PubChem/ChEMBL accessions. The parent is structurally broader, but its
    antibiotic-activity wording is not independent experimental evidence for B. This
    confirms upstream provenance of the congener transfer.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: pubchem
  kind: authority
  reference: PubChem:14467479
  locator: Complete official chemical property response and independently parsed SMILES/InChI.
  accessed_at: '2026-10-21T14:57:41Z'
  support: supports
  summary: The current source has the same formula, charge, masses, unassigned SMILES
    and full Standard InChIKey as the native record. It contains no trans/cis constraint.
    This supports source reproduction and connectivity but cannot resolve the narrower
    natural-product relative configuration.
  snapshot_sha256: c8facd89772891b6b20ce8e5ff3ddf2c1a4dbd476a3df257ae9ee0fe3066cb1b
- evidence_id: chembl
  kind: authority
  reference: CHEMBL4159271
  locator: Complete molecule response; canonical SMILES, Standard InChI and molfile
    independently checked.
  accessed_at: '2026-10-21T14:57:41Z'
  support: supports
  summary: ChEMBL encodes the same neutral connectivity and unassigned full key, with
    average mass 502.25. Its molfile also leaves the two piperazine centres unassigned.
    Agreement between chemical databases therefore does not independently establish
    that the graph specifies the documented trans natural product.
  snapshot_sha256: a250f07b0fbaa0dae62f0377d0b561b1bcf9a086dd8e120f5bc01e2e0cea84ff
- evidence_id: g2017
  kind: primary_source
  reference: PMID:28085024; DOI:10.3390/md15010016; PMC5295236
  locator: Complete original main prose, structural-analysis table and assay methods
    read.
  accessed_at: '2026-10-21T14:51:22Z'
  support: refutes
  summary: This primary study isolates and tests G, C23H19Br2N7S, with a pyrazine
    and guanidinoethylthio group. Its bacterial, mycobacterial, malaria and pancreatic-cell
    results are not B experiments. The native paragraph closely follows this G report
    and must not be transferred to B. The paper explicitly distinguishes untested
    pyruvate-kinase activity of G from results on other bis-indoles.
  snapshot_sha256: 5274486045543d17a24c658a77c86d11e71359cbbd2af9cd7f769a344953c5ee
- evidence_id: gh2024
  kind: primary_source
  reference: PMID:38206835; DOI:10.1021/acs.orglett.3c04039
  locator: Complete indexed and publisher abstract, not full original paper.
  accessed_at: '2026-10-21T14:57:41Z'
  support: refutes
  summary: The study synthesizes G/H and tests them and analogues against S. aureus
    and an efflux-deficient Salmonella Typhimurium strain. The abstract gives no B-specific
    result. It cannot repair the G-to-B definition transfer.
  snapshot_sha256: 5283c999cf18d2cc3a1670088a2d06eb72694f36f3a7aaa0cda06b30a30bc636
- evidence_id: ab2018
  kind: primary_source
  reference: PMID:30023878; DOI:10.1021/acsomega.7b01786
  locator: Complete main text, Tables 1–3 and methods read; original Figure 1 compound
    4 visually inspected. XML under PMC6045348; current article HTML resolves to PMC6645895
    for the same DOI.
  accessed_at: '2026-10-21T14:51:22Z'
  support: context_only
  summary: The paper independently isolates B as compound 4 and compares its NMR/MS
    with earlier B reports. Figure 1 depicts trans B. Table 2 reports B GI50 values
    20.3, 19.3 and 28.0 micromolar in A549, HT29 and MDA-MB-231 tumor cells. At 10
    micromolar, B leaves 102.3 +/- 13.0 percent PP1 activity, and the authors explicitly
    say B lacks significant inhibition in that enzyme assay. Cell-cycle/phosphorylation
    changes and docking do not turn this into measured direct PP1 binding or a microbial
    mechanism. No antibacterial experiment is reported.
  snapshot_sha256: 8afbff444f3ad865021098e36dba189963d2da055db73cc61f45e2beaaa400a7
- evidence_id: trans-figure
  kind: primary_source
  reference: DOI:10.1021/acsomega.7b01786 Figure 1 compound 4; 375-figure-check.py
  locator: Original image and independent atom mapping, with mirror comparison.
  accessed_at: '2026-10-21T14:53:58Z'
  support: refutes
  summary: B has two N-methyl groups and two opposite-face indolyl bonds. Mapping
    those bonds gives R/S centres and GRBPIEOBAMGKFD-SZPZYZBQSA-N. Reversing both
    gives the same key because this graph is meso. The native graph omits the trans
    constraint altogether. The review does not infer a mixture, racemate or an opposite
    natural enantiomer from unassigned notation.
  snapshot_sha256: 46d071fb3e5adca3f94c1394961c55f1f3305bc53587396875a5cf9933c631d6
- evidence_id: synthesis2005
  kind: primary_source
  reference: DOI:10.1016/j.tetlet.2005.02.054; https://www.stoltz2.caltech.edu/publications/43-2005.pdf
  locator: Complete four-page original author-hosted PDF text and experimental notes
    read; page 2423 Scheme 2 visually inspected.
  accessed_at: '2026-10-21T14:58:59Z'
  support: supports
  summary: Scheme 2 labels compound 5 dragmacidin B and explicitly depicts trans relative
    geometry, independently of the 2018 drawing. The work prepares pyrazine 7 and
    is a formal synthesis using a previously established conversion, not a new B biological
    assay. The text and note 7 distinguish B from trans-dragmacidin C and cite the
    Horne reduction route.
  snapshot_sha256: 54a23c22bbd1e7e9c3c83656bff8ca0feebdb27298cab4a16faed67d131e3b25
- evidence_id: synthesis2000
  kind: primary_source
  reference: PMID:11009377; DOI:10.1021/ol0001970
  locator: Complete indexed and publisher abstract; full paper and spectra were not
    accessed.
  accessed_at: '2026-10-21T14:57:41Z'
  support: context_only
  summary: This synthesis specifically identifies B as compound 1, with separate piperazine
    and didebromo analogues. The abstract describes reduction/reductive methylation
    of the pyrazine precursor. It supports exact compound nomenclature and the 2005
    formal-synthesis citation chain, but not an antibacterial assay.
  snapshot_sha256: 5283c999cf18d2cc3a1670088a2d06eb72694f36f3a7aaa0cda06b30a30bc636
- evidence_id: patent
  kind: primary_source
  reference: WO2001094310A1; https://patents.google.com/patent/WO2001094310A1/en
  locator: Original patent HTML introductory identity scope and Examples 14–19 read;
    scanned PDF downloaded but not independently read.
  accessed_at: '2026-10-21T14:58:59Z'
  support: context_only
  summary: Example 18 expressly prepares dragmacidin B 4 in 70 percent yield and says
    its spectral data agree with natural B. Example 14 states trans diequatorial selectivity
    for its separate piperazine intermediate. These are synthesis/material context,
    not B-specific bacterial susceptibility data. The intermediate selectivity is
    not alone treated as proof of every downstream structure.
  snapshot_sha256: e8bcc37a0815eda6c51e79f81c6ff8cf6018565fdf07daa2e16e5aa7f4f63af7
- evidence_id: discovery
  kind: primary_source
  reference: DOI:10.1016/S0040-4020(01)81355-7
  locator: Complete original publisher abstract as indexed by the web tool; full original
    paper unavailable.
  accessed_at: '2026-10-21T15:01:18Z'
  support: context_only
  summary: The original report isolates dragmacidon B as compound 9 alongside dragmacidon
    A and topsentin C from Hexadella sp. The abstract describes proposed spectroscopic
    structures and A-specific L1210 cytotoxicity. It does not supply a B antibacterial
    result. Later uses of the dragmacidin spelling are not treated as a new compound
    solely on spelling.
- evidence_id: search
  kind: search
  reference: 375-inclusive-hits.txt; 375-curation-hits.txt
  locator: Ignored-inclusive local search and bounded public exact-name literature
    follow-up.
  accessed_at: '2026-10-21T15:01:18Z'
  support: context_only
  summary: No exact corrective overlay was found; the queue row retains both adopted
    G/H leads. Public searches for dragmacidin B and dragmacidon B with antibacterial/antimicrobial/trans/synthesis
    terms found the exact synthesis and host-cell studies but no inspected positive
    B bacterial endpoint. Dragmacidonamine B, crude sponge extracts, G/D activity
    and other bis-indole classes were not conflated with B.
  search_scope: 2026-10-21; rg --no-ignore --hidden across data, curation, conf, scripts,
    src, docs, .claude, reviews and reports for dragmacidin B, dragmacidon B, ARO:3007775
    and GRBPIEOBAMGKFD. A separate ignored-inclusive curation/conf/reports/reviews
    search confirmed no corrective overlay. Public web/Europe PMC searches used both
    exact names, the adopted PMIDs, exact synthesis DOIs and antibacterial, antimicrobial
    and trans configuration terms.
  snapshot_sha256: a7eeb3e799c146b0e13077124205e43ffbfe3cdf5c3921f4dee8e8565cafc536
- evidence_id: validation
  kind: validation
  reference: 375-schema.log; 375-strict.log; 375-chemistry.json; 375-xref-chemistry.json;
    375-figure-chemistry.json
  locator: Actual checks and unchanged-input hash recheck.
  accessed_at: '2026-10-21T15:01:18Z'
  support: supports
  summary: 'Schema and strict pass. Initial scratch chemistry exit 1 is retained transparently:
    its average-mass rounding threshold failed by 0.004 Da, while current PubChem
    exactly reproduces the stored 502.2. Native/authority graph comparison and manual
    trans/meso mapping pass. These checks establish representation facts, not activity
    or natural-product identity by themselves.'
  snapshot_sha256: e9cc2f84283717627c1f5bfa38e1608048a0ab2e493e2d3cd093e807270dc305
assessments:
- assessment_id: identity
  area: identity
  topic: Connectivity, relative stereochemistry and all exact xrefs
  outcome: concern
  summary: Both chemical authorities agree with the native connectivity, but all omit
    the trans constraint independently depicted for B in the 2005 synthesis and 2018
    isolation papers. A full stereochemical structure would preserve that constraint.
    The current unspecified graph does not establish mixture composition.
  target_ids:
  - antibioticmech:aro-2c3e119979
  evidence_ids:
  - native
  - pubchem
  - chembl
  - trans-figure
  - synthesis2005
  - validation
- assessment_id: definition
  area: evidence
  topic: Congener-specific definition and adopted citation placement
  outcome: concern
  summary: Both source leads concern G/H, while the native definition expressly describes
    G. Neither its chemical description nor its biological panel is evidence for B.
    This upstream error needs a maintained exact-B definition/citation correction.
  target_ids:
  - antibioticmech:aro-2c3e119979
  evidence_ids:
  - owners
  - aro
  - g2017
  - gh2024
- assessment_id: activity
  area: evidence
  topic: Filing class and B-specific biological scope
  outcome: unknown
  summary: The structural bis-indole parent is appropriate at connectivity level.
    Exact-B antibacterial support was not established in the bounded reading. The
    2018 tumor-cell study is real B evidence, but it is neither a bacterial phenotype
    nor positive purified-PP1 inhibition at the tested concentration. No universal
    B inactivity or compulsory exclusion is inferred.
  target_ids:
  - antibioticmech:aro-2c3e119979
  evidence_ids:
  - ab2018
  - discovery
  - synthesis2000
  - synthesis2005
  - patent
  - search
- assessment_id: mechanism
  area: evidence
  topic: Mode, targets, resistance, producer and dataset scope
  outcome: not_applicable
  summary: No native protein, gene, pathway, mechanism or transcriptomic assertion
    triggers a structured adapter. The newly encountered mammalian phosphatase/cell-cycle
    experiments remain research context, with no microbial-target transfer. Sponge
    extraction is not a demonstration of sponge biosynthesis.
  target_ids:
  - antibioticmech:aro-2c3e119979
  evidence_ids:
  - native
  - ab2018
- assessment_id: provenance
  area: provenance
  topic: Generated ownership, history and completeness
  outcome: supported
  summary: All present fields and history entries were checked against actual source
    owners. MINTED/SEEDED remains appropriate for unresolved scientific support. Missing
    optional biological slots are not separate defects. Original hashes and ignored-inclusive
    absence-search scope are preserved.
  target_ids:
  - antibioticmech:aro-2c3e119979
  evidence_ids:
  - native
  - owners
  - search
  - validation
findings:
- finding_id: F1
  issue_key: dragmacidin-b-definition-transferred-from-g
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Replace the G definition and biological claims attached to B
  description: The B-labelled record carries a paragraph explicitly about dragmacidin
    G, including a pyrazine and sulfur-containing side chain absent from the B piperazine
    graph. Both adopted primary citations concern G/H. Replace or qualify these source-derived
    claims for the exact B congener; do not relabel the B graph as G or transfer the
    G experimental panel to B.
  target_ids:
  - antibioticmech:aro-2c3e119979
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - native
  - owners
  - aro
  - g2017
  - gh2024
  rule_id: Exact-compound and narrowest-claim evidence checklist
  native_severity: major
  normalization_reason: The whole descriptive/activity paragraph is a confirmed congener
    transfer. This is a material scientific error despite faithful source reproduction,
    and does not imply that B is universally inactive.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted G definition and publication references
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained congener-specific definition qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition and claim-level citation selection
- finding_id: F2
  issue_key: dragmacidin-b-missing-documented-trans-configuration
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Retain the documented trans relative configuration of dragmacidin B
  description: Native SMILES and Standard InChI leave both piperazine centres unassigned,
    as do the adopted PubChem and ChEMBL records. The independently inspected 2005
    Scheme 2 and 2018 Figure 1 identify B with opposite-face indolyl substituents.
    The trans graph maps to meso R/S stereochemistry, with the same full key after
    simultaneous inversion. The native representation therefore lacks a known relative-configuration
    constraint; no mixture or opposite-enantiomer claim follows from the omission.
  target_ids:
  - antibioticmech:aro-2c3e119979
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  evidence_ids:
  - pubchem
  - chembl
  - trans-figure
  - synthesis2005
  - ab2018
  rule_id: Individual-structure identity and known relative-stereochemistry checklist
  native_severity: major
  normalization_reason: This is confirmed structural underspecification of the named
    natural product, not an explicitly wrong assigned stereoisomer. Source consensus
    on an unspecified encoding does not replace the primary relative-configuration
    evidence.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted structure with unspecified piperazine stereochemistry
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Exact source structure acquisition
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Evidence-backed structure scope adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible exact identity and xref scope
actions:
- action_id: A1
  description: Supply an exact-B definition and review the antibacterial filing using
    compound-specific evidence.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-2c3e119979
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted G definition and publication references
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained congener-specific definition qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition and claim-level citation selection
  acceptance_checks:
  - Remove the G paragraph from the B source path and attach a supported B identity
    definition with the correct primary citation. Keep G/H activity with those actual
    congeners.
  - Establish exact-B antimicrobial evidence or document a bounded curator scope decision
    if it remains unsupported. Host-cell GI50, phosphatase models and antibacterial
    family membership are insufficient alone.
  - Regenerate, inspect the resulting definition/citation and run schema, strict and
    source reproduction checks.
- action_id: A2
  description: Resolve the exact-B trans representation through maintained chemical
    input and xref qualification.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-2c3e119979
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted structure with unspecified piperazine stereochemistry
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Exact source structure acquisition
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Evidence-backed structure scope adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible exact identity and xref scope
  acceptance_checks:
  - Use the primary B structure and atom mapping to preserve trans relative geometry.
    GRBPIEOBAMGKFD-SZPZYZBQSA-N is the independently mapped depicted graph, not an
    instruction to copy a database blindly.
  - Keep connectivity-only PubChem/ChEMBL provenance explicit; assess whether existing
    exact-xref semantics remain valid for the refined structure and qualify broader
    identifiers where required. Do not infer or create a racemate/mixture record.
  - Regenerate from an evidence-supported maintained identity input, reparse both
    chemical encodings and check full stereochemical agreement, formula, charge, mint,
    schema/strict and source reproduction.
limitations:
- The original 1990 discovery and 2000 synthesis papers were accessible at complete-abstract
  depth only; 1994 and 2000 full publisher routes returned 403. The 2005 original
  four-page synthesis paper and 2018 main paper were read fully, with the relevant
  B structures visually checked.
- The 2018 supplementary spectra, microscopy and docking outputs were not independently
  reprocessed. The reported B tumor-cell GI50 values exceed the stated 20 micromolar
  assay starting concentration for two cell lines; this source-quality inconsistency
  is retained as a limit on optional quantitative reuse, not imported as a native-field
  defect.
- The patent was read only for introductory identity context and Examples 14–19. Its
  downloaded scanned PDF was not independently reviewed. Generic activity language
  in a synthesis patent is not treated as a measured B antibacterial endpoint.
- The bounded literature search did not find an inspected exact-B positive antibacterial
  endpoint. This is not an assertion that no such evidence exists or that B is inactive
  in every organism and assay.
- The average-mass scratch diagnostic failed its chosen precision threshold; current
  authority values and independent formula calculations show a rounding/model boundary.
  The original failed result remains recorded and is not silently converted to a pass.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native source or record was changed. Scientific curation should preserve the
  distinction between the exact trans B structure, the unspecified adopted authority
  encodings and the chemically distinct G activity claims.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
