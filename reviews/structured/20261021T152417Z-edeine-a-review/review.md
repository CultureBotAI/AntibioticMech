# Edeine A: exact-identity reconciliation with original peptide chemistry

- Review: 20261021T152417Z-edeine-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:03:29Z
- Finished UTC: 2026-10-21T15:24:17Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native encodings reproduce the imported PubChem entry but require chemical identity correction against original edeine structures. Reconcile the mixture definition and incomplete stereochemistry with a single A1 structure. Database mechanism and resistance assertions remain explicitly distinguished from congener-specific primary experiments. All adopted literature leads and twenty captured inputs were checked.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue 391, isolated batch040; thirteen original input hashes preserved, actual ARO/PubChem/edge owners and source code appended before assessment, twenty inputs unchanged.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-68a16c2153 | data/antibiotics/antibacterial/edeine-a.yaml | generated | edeine A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-68a16c2153 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-68a16c2153 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-68a16c2153 | Actual focused execution exited 0. |
| source-ledger | passed | False | antibioticmech:aro-68a16c2153 | All native source fields, exact edge ownership, original hashes and histories checked. |
| authority-comparison | passed | False | antibioticmech:aro-68a16c2153 | Native/current PubChem agreement and independent original-diagram diagnostic composition/stereochemistry checks pass; chemical-source disagreements are substantive findings. |
| Authoritative full QC | failed | True | antibioticmech:aro-68a16c2153 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-68a16c2153 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-68a16c2153 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-68a16c2153 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-68a16c2153 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-68a16c2153 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-68a16c2153 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-68a16c2153 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-68a16c2153 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### One exact molecule, constitution and configuration

identity: concern. Targets: antibioticmech:aro-68a16c2153.

The definition explicitly makes this record an A1/A2 mixture, while its single graph has only active-alpha A1 connectivity and leaves all six carbon stereocenters unspecified. Original structures distinguish A2 by isoserine-to-DAPA beta-amino acyl linkage; removing stereochemical descriptors does not encode that second constitutional isomer. Reconcile the record to one explicitly identified constituent with source-supported configuration, and keep mixture/sample information separate. The current PubChem entry reproduces this incompleteness; it is not independent evidence that natural A1 has unknown configuration.

### Exact material and antimicrobial endpoint scope

evidence: supported. Targets: antibioticmech:aro-68a16c2153.

Original studies support edeine A material activity under stated conditions, but sample isomer/salt boundaries and the identity correction prevent unqualified transfer to the current graph.

### Database P-site target versus primary binding evidence

evidence: unknown. Targets: antibioticmech:aro-68a16c2153.

The native source is transparently marked PRIMARY_EVIDENCE_NEEDED. New E. coli congener-B data distinguish E-site binding from indirect P-site effects, with ligand-model and nomenclature limits. Other congener models do not establish experimental direct binding for this record.

### Qualified16S mutation and EdeQ assertions

evidence: supported. Targets: antibioticmech:aro-68a16c2153.

Both edges are correctly attributed as database assertions. Exact allele, strain, congener and assay support remain unresolved; neither abstract-level EdeQ chemistry nor generic16S functional mapping licenses a new primary-resistance claim.

### Class, source context and optional enrichments

completeness: supported. Targets: antibioticmech:aro-68a16c2153.

The nonribosomal class is supported. Optional blank activity/producer/graph slots do not create additional findings. No clinical inference or fabricated protein example is made.

### Every source lead and maintained owner

provenance: supported. Targets: antibioticmech:aro-68a16c2153.

Native values reproduce their source rows and all adopted leads have explicit access/scope dispositions; scientific errors are inherited, not evidence of drift. All twenty captures remain unchanged.

## Findings

### F1: Reconcile the mixture definition and incomplete stereochemistry with a single A1 structure

major / open / confirmed; issue key: edeine-a-exact-chemical-identity.

The definition explicitly makes this record an A1/A2 mixture, while its single graph has only active-alpha A1 connectivity and leaves all six carbon stereocenters unspecified. Original structures distinguish A2 by isoserine-to-DAPA beta-amino acyl linkage; removing stereochemical descriptors does not encode that second constitutional isomer. Reconcile the record to one explicitly identified constituent with source-supported configuration, and keep mixture/sample information separate. The current PubChem entry reproduces this incompleteness; it is not independent evidence that natural A1 has unknown configuration.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate exact constituent identity through maintained source ownership, then regenerate.

- Use the original residue/configuration and linkage evidence to define the intended active constituent; retain inactive isomer and sample mixture distinctions.
- Reconcile every SMILES/InChI/key, formula, charge, mass and exact database link with the chosen identity; independently map atom connectivity and stereochemical parity.
- Do not treat database agreement or the scratch diagnostic key as sufficient authority. Preserve source provenance and run focused schema/strict, chemical checks and complete source reproduction after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/edeine-a.yaml; Entire native YAML, every asserted field and four histories | supports | SEEDED, MINTED edeine A contains one neutral C33H58N10O10 graph, key HENXXJCYASTLGZ-UHFFFAOYSA-N; one nonribosomal-peptide parent/class, exact ARO and PubChem links, two resistance entries explicitly marked database assertions, and a DIRECT_BINDING_TARGET P-site entry explicitly marked PRIMARY_EVIDENCE_NEEDED. No quantitative activity, clinical-status, producer, causal-graph or expression dataset objects are present. |
| owners | Adopted ARO/PubChem inventories and maintained extractor/enricher/seeder; Exact target rows in 391-source-rows.json;391394-ledger.json; inspected seeder structure_from_pubchem/load_concepts/build_record | supports | The actual target row reproduces the definition, first definition PMID, graph, class and identifiers. The complete definition_refs list was inspected rather than only the first projected citation. Target and resistance rows reproduce their stated database provenance. Deterministic ARO mint, source version and four chronological histories agree. Incidental other-congener rows in name-search output were excluded from target ownership. Twenty hashes, including all thirteen original captures, remain unchanged. |
| chemistry | Native RDKit chemistry and current PubChem exact CID; 391394-structure-comparison.json; native focused chemistry/schema/strict results | supports | Native SMILES and InChI agree in key, composition, charge and mass, and independently fetched current PubChem encodings reproduce them. A has six unassigned stereocenters; B/D/F have six assigned. This establishes source and internal consistency, not correspondence to the isolated antibiotic. Explicit scratch diagnostic graphs built from the original residue/configuration diagram distinguish the intended active alpha isomers. No native graph was modified. |
| primary-structure | PMID:6615592; DOI:10.7164/antibiotics.36.793; DOI:10.7164/antibiotics.36.1001; Complete original 1983 F isolation and D total-synthesis papers; F Figure1 p796 and D backbone Figure1/2 plus synthesis/results; actual D Table2 p1003 inspected | supports | The original papers establish S-beta-tyrosine or S-beta-phenyl-beta-alanine, S-isoserine, S-diaminopropionate and (2R,6S,7R)-diaminohydroxyazelate, followed by glycine and spermidine/guanidylspermidine. A/B retain phenol; D/F lack it. B/F carry a guanidino group on terminal spermidine nitrogen. Active alpha and inactive beta isomers differ in whether isoserine acylates the alpha or beta amino group of DAPA; this is a connectivity change, not merely stereochemistry. D synthesis distinguishes uncontaminated active/inactive products despite indistinguishable TLC/electrophoresis, and F is obtained from D by amidination and matched to fermentation material. |
| structure-D | DOI:10.7164/antibiotics.36.1239; Complete original decarboxy-D paper; actual Figure1 p1239 | supports | The independently displayed native D parent explicitly contains beta-Phe NH2-CH(phenyl)-CH2-CO, isoserine NH-CH2-CH(OH)-CO, the singly alpha-acylated DAPA unit, and the glycine linkage CO-NH-CH2-CO-NH. It distinguishes the carboxyl-containing parent from a separately synthesized decarboxy analogue. This supports the structural comparison without assigning analogue activity to the parent. |
| aro | Current official ARO3000130/134/135/136;3000756;3003223;3004063;3009657; 374-current-aro.obo and391394-aro-blocks.txt, retrieved2026-10-21 | supports | Current ARO retains the adopted compound and class assignments, P-site target edges and both resistance edges. The nonribosomal peptide class fits the reported biosynthesis and chemistry. ARO is direct evidence of database assertion provenance, not congener-resolved experimental validation. Its target lead15755955 is a review; its16S-rRNA resistance lead16269538 concerns deleterious mutations and target-site mapping. |
| leads | All adopted definition_refs for this exact ARO record; 391394-primary-abstracts.json; exact original PDFs where available | context_only | PMID4984939 (1970 A1/B1 structure) resolves with no abstract and full text unavailable; PMID14731399 (2004 ribosome study) complete abstract read, exact congener not specified; PMID70202 (1977 Bacillus peptide review) resolves with no abstract and full text inaccessible. |
| adapter | iModulonDB e_coli/modulome; dataset catalog; 391394-adapter-sandbox-results.json and391394-adapter-results.json | context_only | Before primary mechanism follow-up, initial sandbox queries failed DNS and were retained as access failures. The successful scoped retry returned a full dataset catalog and zero hits for16S ribosomal RNA in e_coli/modulome. No Brevibacillus dataset was listed, so an EdeQ organism-matched query was unavailable. No component hit required summarization. These bounded results do not establish biological absence or resistance. |
| resistance | PMID:23891151; PMID:16269538; PMID:15755955; Complete original2013 EdeQ abstract;2005 PNAS main article via web;2005 initiation-review abstract | context_only | Purified EdeQ acetylates the free internal DAPA amine, not the spermidine terminus; the original abstract reports loss of cell and cell-free translation activity but does not identify every tested congener. The inspected16269538 main text selects deleterious16S mutations and studies translation/growth; it does not provide a verified exact-congener edeine resistance measurement. The target review is secondary. Native entries honestly retain database scope; neither full causal allele evidence nor measured D/F EdeQ susceptibility is inferred. |
| cryo2025 | PMID:40075065; DOI:10.1038/s41467-025-57731-8; Full original XML: edeine Results, Discussion and Methods; original SI pages5–9/16; actual Supplementary Figure7 p8 | context_only | The study identifies the experimental compound as congener B and locates its resolved core in the E-site of E. coli30S, spanning h23/h24 and the mRNA path. P-site initiator-tRNA inhibition is interpreted as indirect. Cryo-EM used100 micromolar drug and functional stopped-flow assays5 micromolar, with prepared initiation complexes. A/C/D are in-silico models, not independent experimental binding measurements. Supplementary Fig7 labels its phenyl/spermidine and phenyl/guanidyl congeners C/D, conflicting with original D/F nomenclature; it cannot support uncritical transfer by congener letter. The guanylspermidine tail has weak density. These findings challenge a universal direct P-site assignment but do not directly map all congeners or taxa. |
| pdb-limit | PDB:9FDA; CCD:EDE; 391394-9FDA.json;9FDA nonpolymer18;391394-EDE.cif full chemical descriptors | context_only | The current deposition identifies ligand EDE and its CCD contains C34H59N11O10 with WEPSNLBXXUYQJF-LQXCWRENSA-N, the same missing-nitrogen graph as native B/PubChem. The coordinate model therefore is not independent chemical validation of a complete guanidylspermidine molecule. The primary E-site density/functional interpretation is assessed with that chemical-model limitation, and the newer deposition is not allowed to override original chemical elucidation. |
| activity | DOI:10.7164/antibiotics.34.28; Complete original1981 ester/amide study; actual Table1 p29 and Biological Activity p31 | supports | The laboratory-isolated edeine A sulfate is the parent comparator, separate from ten modified analogues. Its IC50 is90 micrograms/mL for B. subtilis without a specified strain,100 for E. coli K-12 and32 for S. cerevisiae ATCC9763. Bacteria use Sensitive Test Medium,37C,pH7.2,18h with660nm turbidity. These are50-percent growth-inhibition endpoints, not MICs; active/inactive-isomer purity of the comparator is not independently established here. They support A preparation antibacterial activity without assigning those values to every stereochemical interpretation of the current graph. |
| access | Exact name/identifier/DOI and ignored-inclusive maintained-source searches; 391394-inclusive-search.txt; per-target owner searches; free-fetch manifests1–9 | context_only | Local absence conclusions include ignored files in curation/conf/scripts/src/docs/.claude/reports/reviews. No exact corrective overlay was identified in that bounded scope. Original1970 ACS text and1977 review full text were inaccessible;2013 EdeQ remained abstract-only. Initial Europe PMC/DNS/interstitial and PubMed query failures are retained. The2025 main HTML was not mistaken for a PDF; its exact publisher-linked SI was subsequently retrieved and inspected. The2007 paper is immunoregulation research, inspected only for introduction/structure/material context, not original antibacterial SAR. |

## Limits And Additional Notes

- The1970 A1/B1 structure paper has no indexed abstract and its full text was not inspected; the1977 review also remained inaccessible. Independent original1981/1983 chemistry and activity papers supply explicitly scoped evidence.
- The2013 EdeQ paper was read at complete-original-abstract depth. Exact congener substrate assignments were not inferred. The2005 mutation paper main text does not establish the claimed exact-congener resistance assay; this does not prove absence from all literature.
- The2025 E. coli experiment is identified as B by its authors, but its EDE CCD repeats the deficient N11 chemistry. The guanylspermidine tail is weakly resolved. Its SI congener labels C/D conflict with original D/F naming; modelled other congeners are not experimental binding evidence.
- Natural preparations may contain alpha/beta isomers formed by intramolecular acyl migration. Aqueous sample composition, sulfate/hydrate form, growth IC50, MIC and calibrated potency units must remain distinct.
- Diagnostic primary-derived graphs are scratch comparisons, not new curated identifiers. No record, inventory, dependency or source code was changed. Full required-gate status is attached separately.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T152417Z-edeine-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Edeine A: exact-identity reconciliation with original peptide chemistry'
started_at: '2026-10-21T15:03:29Z'
finished_at: '2026-10-21T15:24:17Z'
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
summary: The native encodings reproduce the imported PubChem entry but require chemical
  identity correction against original edeine structures. Reconcile the mixture definition
  and incomplete stereochemistry with a single A1 structure. Database mechanism and
  resistance assertions remain explicitly distinguished from congener-specific primary
  experiments. All adopted literature leads and twenty captured inputs were checked.
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
  - path: data/antibiotics/antibacterial/edeine-a.yaml
    sha256: a4e018392bf577094d249a902b415c0ccb8615c6dbf9fd98131fb26e78fe3a67
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
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
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
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: antibioticmech:aro-68a16c2153
  path: data/antibiotics/antibacterial/edeine-a.yaml
  label: edeine A
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition and PubChem identity link
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Imported complete chemical structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Native identity projection
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Any explicit identity adjudication
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted target relation
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Maintained target relation qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Native target projection
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Qualified resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue 391, isolated batch040; thirteen original input hashes preserved,
    actual ARO/PubChem/edge owners and source code appended before assessment, twenty
    inputs unchanged.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-68a16c2153
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-68a16c2153
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    391
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-68a16c2153
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/edeine-a.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-68a16c2153
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/edeine-a.yaml --out /private/tmp/am-review-session/391-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: source-ledger
  name: source-ledger
  status: passed
  required: false
  command: .venv/bin/python /private/tmp/am-review-session/391394-ledger.py > /private/tmp/am-review-session/391394-ledger.log
    2>&1
  exit_code: 0
  expected_exit_code: 0
  summary: All native source fields, exact edge ownership, original hashes and histories
    checked.
  target_ids:
  - antibioticmech:aro-68a16c2153
- check_id: authority-comparison
  name: authority-comparison
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/391394-structure-compare.py
    > /private/tmp/am-review-session/391394-structure-compare.log 2>&1
  exit_code: 0
  expected_exit_code: 0
  summary: Native/current PubChem agreement and independent original-diagram diagnostic
    composition/stereochemistry checks pass; chemical-source disagreements are substantive
    findings.
  target_ids:
  - antibioticmech:aro-68a16c2153
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-68a16c2153
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
  - antibioticmech:aro-68a16c2153
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
  - antibioticmech:aro-68a16c2153
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
  - antibioticmech:aro-68a16c2153
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
  - antibioticmech:aro-68a16c2153
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
  - antibioticmech:aro-68a16c2153
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
  - antibioticmech:aro-68a16c2153
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
  - antibioticmech:aro-68a16c2153
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
  - antibioticmech:aro-68a16c2153
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/edeine-a.yaml
  locator: Entire native YAML, every asserted field and four histories
  accessed_at: '2026-10-21T15:18:35Z'
  support: supports
  summary: SEEDED, MINTED edeine A contains one neutral C33H58N10O10 graph, key HENXXJCYASTLGZ-UHFFFAOYSA-N;
    one nonribosomal-peptide parent/class, exact ARO and PubChem links, two resistance
    entries explicitly marked database assertions, and a DIRECT_BINDING_TARGET P-site
    entry explicitly marked PRIMARY_EVIDENCE_NEEDED. No quantitative activity, clinical-status,
    producer, causal-graph or expression dataset objects are present.
- evidence_id: owners
  kind: database
  reference: Adopted ARO/PubChem inventories and maintained extractor/enricher/seeder
  locator: Exact target rows in 391-source-rows.json;391394-ledger.json; inspected
    seeder structure_from_pubchem/load_concepts/build_record
  accessed_at: '2026-10-21T15:18:35Z'
  support: supports
  summary: The actual target row reproduces the definition, first definition PMID,
    graph, class and identifiers. The complete definition_refs list was inspected
    rather than only the first projected citation. Target and resistance rows reproduce
    their stated database provenance. Deterministic ARO mint, source version and four
    chronological histories agree. Incidental other-congener rows in name-search output
    were excluded from target ownership. Twenty hashes, including all thirteen original
    captures, remain unchanged.
  snapshot_sha256: 9c0c648c4eec9f83ed7b70d4e2fe476d9adaf924e084ba8902ee2b535bd62be9
- evidence_id: chemistry
  kind: validation
  reference: Native RDKit chemistry and current PubChem exact CID
  locator: 391394-structure-comparison.json; native focused chemistry/schema/strict
    results
  accessed_at: '2026-10-21T15:18:35Z'
  support: supports
  summary: Native SMILES and InChI agree in key, composition, charge and mass, and
    independently fetched current PubChem encodings reproduce them. A has six unassigned
    stereocenters; B/D/F have six assigned. This establishes source and internal consistency,
    not correspondence to the isolated antibiotic. Explicit scratch diagnostic graphs
    built from the original residue/configuration diagram distinguish the intended
    active alpha isomers. No native graph was modified.
  snapshot_sha256: 128d4a3f6045fd4d813622e1b4b72c47461f7eb0653925770f6289447025dc8e
- evidence_id: primary-structure
  kind: primary_source
  reference: PMID:6615592; DOI:10.7164/antibiotics.36.793; DOI:10.7164/antibiotics.36.1001
  locator: Complete original 1983 F isolation and D total-synthesis papers; F Figure1
    p796 and D backbone Figure1/2 plus synthesis/results; actual D Table2 p1003 inspected
  accessed_at: '2026-10-21T15:18:35Z'
  support: supports
  summary: The original papers establish S-beta-tyrosine or S-beta-phenyl-beta-alanine,
    S-isoserine, S-diaminopropionate and (2R,6S,7R)-diaminohydroxyazelate, followed
    by glycine and spermidine/guanidylspermidine. A/B retain phenol; D/F lack it.
    B/F carry a guanidino group on terminal spermidine nitrogen. Active alpha and
    inactive beta isomers differ in whether isoserine acylates the alpha or beta amino
    group of DAPA; this is a connectivity change, not merely stereochemistry. D synthesis
    distinguishes uncontaminated active/inactive products despite indistinguishable
    TLC/electrophoresis, and F is obtained from D by amidination and matched to fermentation
    material.
  snapshot_sha256: 6e79bab3f877acfeb9c75b69d388587cc5597f5db8cf221f60e33e50d20c8a69
- evidence_id: structure-D
  kind: primary_source
  reference: DOI:10.7164/antibiotics.36.1239
  locator: Complete original decarboxy-D paper; actual Figure1 p1239
  accessed_at: '2026-10-21T15:18:35Z'
  support: supports
  summary: The independently displayed native D parent explicitly contains beta-Phe
    NH2-CH(phenyl)-CH2-CO, isoserine NH-CH2-CH(OH)-CO, the singly alpha-acylated DAPA
    unit, and the glycine linkage CO-NH-CH2-CO-NH. It distinguishes the carboxyl-containing
    parent from a separately synthesized decarboxy analogue. This supports the structural
    comparison without assigning analogue activity to the parent.
  snapshot_sha256: 6bdd900feaabe1c05ddb47bce6c1940800d739a1dda85da503c8858446fc4b57
- evidence_id: aro
  kind: authority
  reference: Current official ARO3000130/134/135/136;3000756;3003223;3004063;3009657
  locator: 374-current-aro.obo and391394-aro-blocks.txt, retrieved2026-10-21
  accessed_at: '2026-10-21T15:18:35Z'
  support: supports
  summary: Current ARO retains the adopted compound and class assignments, P-site
    target edges and both resistance edges. The nonribosomal peptide class fits the
    reported biosynthesis and chemistry. ARO is direct evidence of database assertion
    provenance, not congener-resolved experimental validation. Its target lead15755955
    is a review; its16S-rRNA resistance lead16269538 concerns deleterious mutations
    and target-site mapping.
  snapshot_sha256: 9bdb05463a487c35327151429e9e3d008589b1e0269789d4d0929ef1b2de8f88
- evidence_id: leads
  kind: primary_source
  reference: All adopted definition_refs for this exact ARO record
  locator: 391394-primary-abstracts.json; exact original PDFs where available
  accessed_at: '2026-10-21T15:18:35Z'
  support: context_only
  summary: PMID4984939 (1970 A1/B1 structure) resolves with no abstract and full text
    unavailable; PMID14731399 (2004 ribosome study) complete abstract read, exact
    congener not specified; PMID70202 (1977 Bacillus peptide review) resolves with
    no abstract and full text inaccessible.
  snapshot_sha256: d377ad5170cb88bf69fd01dd340916c621b3291d71208158512ed31b70b19080
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/modulome; dataset catalog
  locator: 391394-adapter-sandbox-results.json and391394-adapter-results.json
  accessed_at: '2026-10-21T15:18:35Z'
  support: context_only
  summary: Before primary mechanism follow-up, initial sandbox queries failed DNS
    and were retained as access failures. The successful scoped retry returned a full
    dataset catalog and zero hits for16S ribosomal RNA in e_coli/modulome. No Brevibacillus
    dataset was listed, so an EdeQ organism-matched query was unavailable. No component
    hit required summarization. These bounded results do not establish biological
    absence or resistance.
  snapshot_sha256: 9b492be25e2e6a069f433548a339ced1dfe7fb6fb6238beb11044b08e8e33968
- evidence_id: resistance
  kind: primary_source
  reference: PMID:23891151; PMID:16269538; PMID:15755955
  locator: Complete original2013 EdeQ abstract;2005 PNAS main article via web;2005
    initiation-review abstract
  accessed_at: '2026-10-21T15:18:35Z'
  support: context_only
  summary: Purified EdeQ acetylates the free internal DAPA amine, not the spermidine
    terminus; the original abstract reports loss of cell and cell-free translation
    activity but does not identify every tested congener. The inspected16269538 main
    text selects deleterious16S mutations and studies translation/growth; it does
    not provide a verified exact-congener edeine resistance measurement. The target
    review is secondary. Native entries honestly retain database scope; neither full
    causal allele evidence nor measured D/F EdeQ susceptibility is inferred.
  snapshot_sha256: d377ad5170cb88bf69fd01dd340916c621b3291d71208158512ed31b70b19080
- evidence_id: cryo2025
  kind: primary_source
  reference: PMID:40075065; DOI:10.1038/s41467-025-57731-8
  locator: 'Full original XML: edeine Results, Discussion and Methods; original SI
    pages5–9/16; actual Supplementary Figure7 p8'
  accessed_at: '2026-10-21T15:18:35Z'
  support: context_only
  summary: The study identifies the experimental compound as congener B and locates
    its resolved core in the E-site of E. coli30S, spanning h23/h24 and the mRNA path.
    P-site initiator-tRNA inhibition is interpreted as indirect. Cryo-EM used100 micromolar
    drug and functional stopped-flow assays5 micromolar, with prepared initiation
    complexes. A/C/D are in-silico models, not independent experimental binding measurements.
    Supplementary Fig7 labels its phenyl/spermidine and phenyl/guanidyl congeners
    C/D, conflicting with original D/F nomenclature; it cannot support uncritical
    transfer by congener letter. The guanylspermidine tail has weak density. These
    findings challenge a universal direct P-site assignment but do not directly map
    all congeners or taxa.
  snapshot_sha256: 0a623fb17afd24592902e08d498df1860d7e7cd304f442e654edf5955a01fee0
- evidence_id: pdb-limit
  kind: authority
  reference: PDB:9FDA; CCD:EDE
  locator: 391394-9FDA.json;9FDA nonpolymer18;391394-EDE.cif full chemical descriptors
  accessed_at: '2026-10-21T15:18:35Z'
  support: context_only
  summary: The current deposition identifies ligand EDE and its CCD contains C34H59N11O10
    with WEPSNLBXXUYQJF-LQXCWRENSA-N, the same missing-nitrogen graph as native B/PubChem.
    The coordinate model therefore is not independent chemical validation of a complete
    guanidylspermidine molecule. The primary E-site density/functional interpretation
    is assessed with that chemical-model limitation, and the newer deposition is not
    allowed to override original chemical elucidation.
  snapshot_sha256: ca638cbd3c6aaabc9add983f909999945b58a759dea9eb7ed5c3927b398bc508
- evidence_id: activity
  kind: primary_source
  reference: DOI:10.7164/antibiotics.34.28
  locator: Complete original1981 ester/amide study; actual Table1 p29 and Biological
    Activity p31
  accessed_at: '2026-10-21T15:18:35Z'
  support: supports
  summary: The laboratory-isolated edeine A sulfate is the parent comparator, separate
    from ten modified analogues. Its IC50 is90 micrograms/mL for B. subtilis without
    a specified strain,100 for E. coli K-12 and32 for S. cerevisiae ATCC9763. Bacteria
    use Sensitive Test Medium,37C,pH7.2,18h with660nm turbidity. These are50-percent
    growth-inhibition endpoints, not MICs; active/inactive-isomer purity of the comparator
    is not independently established here. They support A preparation antibacterial
    activity without assigning those values to every stereochemical interpretation
    of the current graph.
  snapshot_sha256: 1e06109bb32e0231c4d775e034372a40366276d4026903bedd36cdcc59e8311e
- evidence_id: access
  kind: search
  reference: Exact name/identifier/DOI and ignored-inclusive maintained-source searches
  locator: 391394-inclusive-search.txt; per-target owner searches; free-fetch manifests1–9
  accessed_at: '2026-10-21T15:18:35Z'
  support: context_only
  summary: Local absence conclusions include ignored files in curation/conf/scripts/src/docs/.claude/reports/reviews.
    No exact corrective overlay was identified in that bounded scope. Original1970
    ACS text and1977 review full text were inaccessible;2013 EdeQ remained abstract-only.
    Initial Europe PMC/DNS/interstitial and PubMed query failures are retained. The2025
    main HTML was not mistaken for a PDF; its exact publisher-linked SI was subsequently
    retrieved and inspected. The2007 paper is immunoregulation research, inspected
    only for introduction/structure/material context, not original antibacterial SAR.
  search_scope: Exact names, native identifiers and full keys with rg --no-ignore
    --hidden; complete adopted citation lists; bounded free original-paper and official
    chemistry retrieval.
  snapshot_sha256: 54130ab4e957b6d3a17b38add6259c41c206395a06ab7b54e1ea5e96c78f50dd
assessments:
- assessment_id: identity
  area: identity
  topic: One exact molecule, constitution and configuration
  outcome: concern
  summary: The definition explicitly makes this record an A1/A2 mixture, while its
    single graph has only active-alpha A1 connectivity and leaves all six carbon stereocenters
    unspecified. Original structures distinguish A2 by isoserine-to-DAPA beta-amino
    acyl linkage; removing stereochemical descriptors does not encode that second
    constitutional isomer. Reconcile the record to one explicitly identified constituent
    with source-supported configuration, and keep mixture/sample information separate.
    The current PubChem entry reproduces this incompleteness; it is not independent
    evidence that natural A1 has unknown configuration.
  target_ids:
  - antibioticmech:aro-68a16c2153
  evidence_ids:
  - native
  - chemistry
  - primary-structure
  - structure-D
- assessment_id: activity
  area: evidence
  topic: Exact material and antimicrobial endpoint scope
  outcome: supported
  summary: Original studies support edeine A material activity under stated conditions,
    but sample isomer/salt boundaries and the identity correction prevent unqualified
    transfer to the current graph.
  target_ids:
  - antibioticmech:aro-68a16c2153
  evidence_ids:
  - activity
  - primary-structure
  - native
- assessment_id: target
  area: evidence
  topic: Database P-site target versus primary binding evidence
  outcome: unknown
  summary: The native source is transparently marked PRIMARY_EVIDENCE_NEEDED. New
    E. coli congener-B data distinguish E-site binding from indirect P-site effects,
    with ligand-model and nomenclature limits. Other congener models do not establish
    experimental direct binding for this record.
  target_ids:
  - antibioticmech:aro-68a16c2153
  evidence_ids:
  - native
  - aro
  - leads
  - cryo2025
  - pdb-limit
- assessment_id: resistance
  area: evidence
  topic: Qualified16S mutation and EdeQ assertions
  outcome: supported
  summary: Both edges are correctly attributed as database assertions. Exact allele,
    strain, congener and assay support remain unresolved; neither abstract-level EdeQ
    chemistry nor generic16S functional mapping licenses a new primary-resistance
    claim.
  target_ids:
  - antibioticmech:aro-68a16c2153
  evidence_ids:
  - aro
  - resistance
  - adapter
- assessment_id: scope
  area: completeness
  topic: Class, source context and optional enrichments
  outcome: supported
  summary: The nonribosomal class is supported. Optional blank activity/producer/graph
    slots do not create additional findings. No clinical inference or fabricated protein
    example is made.
  target_ids:
  - antibioticmech:aro-68a16c2153
  evidence_ids:
  - native
  - aro
  - activity
- assessment_id: provenance
  area: provenance
  topic: Every source lead and maintained owner
  outcome: supported
  summary: Native values reproduce their source rows and all adopted leads have explicit
    access/scope dispositions; scientific errors are inherited, not evidence of drift.
    All twenty captures remain unchanged.
  target_ids:
  - antibioticmech:aro-68a16c2153
  evidence_ids:
  - owners
  - leads
  - access
  - chemistry
findings:
- finding_id: F1
  issue_key: edeine-a-exact-chemical-identity
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile the mixture definition and incomplete stereochemistry with a single
    A1 structure
  description: The definition explicitly makes this record an A1/A2 mixture, while
    its single graph has only active-alpha A1 connectivity and leaves all six carbon
    stereocenters unspecified. Original structures distinguish A2 by isoserine-to-DAPA
    beta-amino acyl linkage; removing stereochemical descriptors does not encode that
    second constitutional isomer. Reconcile the record to one explicitly identified
    constituent with source-supported configuration, and keep mixture/sample information
    separate. The current PubChem entry reproduces this incompleteness; it is not
    independent evidence that natural A1 has unknown configuration.
  target_ids:
  - antibioticmech:aro-68a16c2153
  field_paths:
  - definition
  - chemical_structure
  - xrefs
  evidence_ids:
  - native
  - chemistry
  - primary-structure
  - structure-D
  rule_id: Represent one evidence-backed chemical identity without mixture or connectivity
    collapse
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition and PubChem identity link
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Imported complete chemical structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Native identity projection
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Any explicit identity adjudication
actions:
- action_id: A1
  description: Adjudicate exact constituent identity through maintained source ownership,
    then regenerate.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-68a16c2153
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition and PubChem identity link
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Imported complete chemical structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Native identity projection
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Any explicit identity adjudication
  acceptance_checks:
  - Use the original residue/configuration and linkage evidence to define the intended
    active constituent; retain inactive isomer and sample mixture distinctions.
  - Reconcile every SMILES/InChI/key, formula, charge, mass and exact database link
    with the chosen identity; independently map atom connectivity and stereochemical
    parity.
  - Do not treat database agreement or the scratch diagnostic key as sufficient authority.
    Preserve source provenance and run focused schema/strict, chemical checks and
    complete source reproduction after separately authorized curation.
limitations:
- The1970 A1/B1 structure paper has no indexed abstract and its full text was not
  inspected; the1977 review also remained inaccessible. Independent original1981/1983
  chemistry and activity papers supply explicitly scoped evidence.
- The2013 EdeQ paper was read at complete-original-abstract depth. Exact congener
  substrate assignments were not inferred. The2005 mutation paper main text does not
  establish the claimed exact-congener resistance assay; this does not prove absence
  from all literature.
- The2025 E. coli experiment is identified as B by its authors, but its EDE CCD repeats
  the deficient N11 chemistry. The guanylspermidine tail is weakly resolved. Its SI
  congener labels C/D conflict with original D/F naming; modelled other congeners
  are not experimental binding evidence.
- Natural preparations may contain alpha/beta isomers formed by intramolecular acyl
  migration. Aqueous sample composition, sulfate/hydrate form, growth IC50, MIC and
  calibrated potency units must remain distinct.
- Diagnostic primary-derived graphs are scratch comparisons, not new curated identifiers.
  No record, inventory, dependency or source code was changed. Full required-gate
  status is attached separately.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.7164/antibiotics.36.793
- https://doi.org/10.7164/antibiotics.36.1001
- https://doi.org/10.1038/s41467-025-57731-8
```
