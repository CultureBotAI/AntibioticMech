# Bacitracin F: lost natural stereochemistry and bounded antibacterial evidence

- Review: 20261021T100559Z-bacitracin-f
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:50:42Z
- Finished UTC: 2026-10-21T10:05:59Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One confirmed major finding: the record loses 13 established natural stereochemical assignments. An informational follow-up preserves the unresolved antibacterial scope of the degradation product: the MIC &gt;25 panel alone does not refute its classification. Connectivity and oxidative degradation definition are supported. PDI inhibition is separate biochemical context. Focused validators and internal chemistry pass.

## Scope And Provenance

Whole-record review of minted bacitracin F.

Selection: Queue141 in isolated batch015.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-fb45bd17a5 | data/antibiotics/antibacterial/bacitracin-f.yaml | generated | bacitracin F |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | antibioticmech:aro-fb45bd17a5 | Actual command passed. |
| Focused strict | passed | True | antibioticmech:aro-fb45bd17a5 | Actual command passed. |
| Internal encodings, chemical properties and source mint | passed | True | antibioticmech:aro-fb45bd17a5 | Both encodings parse and agree; all13 unspecified centres are separately assessed against primary identity. |
| Authoritative full QC | failed | True | antibioticmech:aro-fb45bd17a5 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-fb45bd17a5 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-fb45bd17a5 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-fb45bd17a5 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-fb45bd17a5 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-fb45bd17a5 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-fb45bd17a5 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-fb45bd17a5 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-fb45bd17a5 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Oxidized F connectivity and stereochemistry

identity: concern. Targets: antibioticmech:aro-fb45bd17a5.

Connectivity, formula and oxidative-deamination relationship are supported, but all13 unspecified centres fail to represent the primary-characterized configurations of natural F. Do not interpret unspecified centres as a demonstrated racemate.

### Degradation relationship and mixture wording

evidence: supported. Targets: antibioticmech:aro-fb45bd17a5.

The definition correctly describes F as a component/degradation product and attributes cell-wall synthesis interference to the mixture. That wording does not itself establish F antibacterial action.

### Antibacterial eligibility versus peptide class

grounding: concern. Targets: antibioticmech:aro-fb45bd17a5.

NRPS-derived peptide classification is coherent. Antibacterial eligibility remains unresolved in this review: purified F did not inhibit the tested strains up to25 micrograms/mL, but that threshold alone cannot refute the classification. The source description of an inactive degradation product motivates further exact-F adjudication, not automatic exclusion.

### Source identifiers

provenance: supported. Targets: antibioticmech:aro-fb45bd17a5.

ARO and PubChem identifiers resolve and reproduce the adopted representation; structural specificity is assessed separately. The more specified named PubChem entry is a lead only.

### Two carrier-target database assertions

evidence: unknown. Targets: antibioticmech:aro-fb45bd17a5.

Faithful, explicitly qualified ARO assertions do not establish F-specific lipid-pyrophosphate binding or an antibacterial mechanism. Negative growth assays alone do not prove absence of molecular binding.

### Four inherited resistance assertions

evidence: unknown. Targets: antibioticmech:aro-fb45bd17a5.

Current ARO supports provenance; inspected generic bacitracin resistance abstracts do not resolve isolated F. Preserve database-only status and revisit source scope alongside eligibility; no blanket claim that all named genes lack function.

### Negative antibacterial assay and biochemical activity

evidence: supported. Targets: antibioticmech:aro-fb45bd17a5.

The primary agar assay has bounded negative F results. Separately, PDI inhibition is a real biochemical lead, not evidence of bacterial killing or a microbial target.

### Mint and seed history

provenance: supported. Targets: antibioticmech:aro-fb45bd17a5.

Source metadata, actual ARO mint and four seed events are coherent. No native status change.

### Source adjudication before optional annotations

completeness: unknown. Targets: antibioticmech:aro-fb45bd17a5.

Eligibility and exact configuration should be resolved before adding claims or promoting status. Optional absent fields are not schema defects; negative observations may be curated only in their exact assay context.

### Producer, clinical, dataset and graph claims

scope: not_applicable. Targets: antibioticmech:aro-fb45bd17a5.

No populated native claims. Nephrotoxicity background and generic treatment statements are not added as native facts.

### Focused validation

schema: supported. Targets: antibioticmech:aro-fb45bd17a5.

Both actual validators pass; internal encoding checks agree.

## Findings

### F1: Reassess antibacterial eligibility of the oxidized F component

informational / open / provisional; issue key: bacitracin-f-antibacterial-eligibility-unresolved.

Primary isolated-F assays show markedly lower potency than A and no inhibition through25 micrograms/mL in the measured panel. The paper also describes F as an inactive degradation product, but its bounded panel does not establish universal inactivity. Antibacterial eligibility requires further source adjudication; neither mixture membership nor PDI inhibition resolves it. The native classification is not declared disproven, and missing citations on a role are not themselves a defect.

### F2: Resolve the loss of natural F stereochemical specificity

major / open / confirmed; issue key: bacitracin-f-unspecified-natural-stereochemistry.

The PubChem fallback encodes all13 tetrahedral centres without configuration, although the primary F characterization identifies defined residue stereochemistry. The connectivity-level entity is broader than the experimentally isolated natural compound. A separately named partially specified PubChem entry is not an automatically valid replacement.

## Recommended Actions And Acceptance Checks

### A1

Optionally investigate exact-F antibacterial scope and preserve the bounded negative primary observations; do not change eligibility solely on this panel.

- Adjudicate exact-F antimicrobial scope using evidence beyond the bounded negative panel; consider higher test concentrations and other organisms/conditions before concluding ineligibility. Existing role assertions do not independently require a citation.
- If ineligible, use the supported exclusion/worklist mechanism rather than silently deleting generated YAML or inventing a replacement class.
- Preserve MIC&gt;25 qualifiers, exact strains, Mueller-Hinton II medium and incubation; do not generalize inactivity beyond tested conditions.
- Do not infer that negative growth assays disprove binding, or promote generic bacitracin resistance assertions to exact-F primary evidence.
- Regenerate from maintained owners and rerun corpus, target/resistance, reference and history gates.

### A2

Resolve a primary-supported stereochemical structure for the isolated F entity if retained; separately adjudicate any source accession replacement.

- Map each retained residue and side-chain configuration to inspected primary structural evidence.
- Do not equate unspecified stereochemistry with a racemate or select a candidate accession by name alone.
- Any replacement full SMILES/InChI/key/formula/charge agrees and identity/duplicate checks pass.
- Resolve antimicrobial eligibility before adding optional activity or target assertions; retain SEEDED until scientific criteria pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/bacitracin-f.yaml; Entire YAML | supports | Read MINTED/SEEDED identity, definition and PMID6752975, NRPS parent/class, all chemical fields, two xrefs, ARO source concept, four resistance assertions, two database-only chemical targets and four seed-history events. No activity, producer, clinical, dataset or graph blocks are populated. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; data/raw/aro_target_edges.tsv; data/raw/aro_resistance_edges.tsv; ARO row131; PubChem row31; target rows147–148; resistance rows2978–2981 | supports | Native inherits ARO3000631 definition/classification and CID3082210 structure. Correct ARO/PubChem source, enrichment and claim owners were captured before judgment. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/3082210; Live PUG properties | supports | Current source reproduces FCLQHQCOKGKLHR-UHFFFAOYSA-N, C66H98N16O17S, charge0 and reported masses. Standard InChI has no stereochemistry layer. |
| chemistry | Independent RDKit and ARO mint checks; Native encodings | supports | SMILES and InChI both parse to one neutral fragment with the same formula/key. Exact mass agrees. PubChem average mass is coarsely reported to one decimal. All13 potential tetrahedral centres are unspecified; actual ARO mint reproduces. This is a connectivity-level representation, not a racemate designation. |
| specified-lead | https://pubchem.ncbi.nlm.nih.gov/compound/121232955; Alternative named bacitracin F identity | context_only | Another PubChem entry has the same connectivity but12 specified centres and one unspecified centre, key FCLQHQCOKGKLHR-PPPWKGACSA-N. It is not an automatic replacement: full residue configuration and the remaining uncertainty must be adjudicated against primary evidence, not chosen by label. |
| primary1995 | https://doi.org/10.7164/antibiotics.48.233; PMID7730158; full PDF, Methods, Tables2/3/5, Figures3/4; pp237/240 visually inspected | partial | Study isolated F, checked purity above95% by HPLC, analyzed amino-acid configurations and confirmed the oxidized ketothiazole structure. The paper retains defined L/D residue configurations and the N-terminal side-chain configuration; the all-unspecified native structure loses this information. Table5 shows F MIC&gt;25 micrograms/mL against M.luteus ATCC9341, S.aureus IFO12732 and B.cereus var.mycoides ATCC11778; text reports no activity in the tested range against B.subtilis ATCC6633 and E.coli IFO3806. Agar dilution used Mueller-Hinton II,37C/20h. The same experiment found A activity at lower concentrations, establishing loss of potency for F within this panel. MIC&gt;25 alone does not exclude antibacterial activity above the tested range or under other conditions. |
| primary2017 | https://doi.org/10.1016/j.jpha.2016.06.001; PMID29404017/PMC5686873; full Methods and Results3.2.2.1 | supports | Commercial-material LC-MS identifies F as the ketothiazole oxidation product, with an otherwise retained cyclic peptide sequence. This independently supports the definition connectivity and degradation relationship. Introductory inactivity/nephrotoxicity statements are background, not new biological assays in this study. |
| pdi | https://doi.org/10.1111/j.1742-4658.2011.08119.x; PMID21481187; indexed abstract | context_only | Purified bacitracin analogues A/B/H/F inhibited protein disulfide isomerase in an insulin-aggregation assay; F IC50 was20 micromolar and B1050 micromolar. This establishes a biochemical activity lead despite absent antibacterial inhibition in the1995 range. Abstract does not establish a microbial antimicrobial target, exact protein taxon, or whether the reported disulfide interaction was independently demonstrated for F rather than another analogue. No PDI target is imported. |
| aro | https://purl.obolibrary.org/obo/aro.obo; Current ARO3000631,3009657,3000719,3003251,3002986–3002988,3003250 | supports | Native source definition, parent/class, PubChem mapping and all six target/resistance assertions persist upstream. These are inherited database relationships; current resolution does not establish F-specific antibacterial action. |
| adopted-review | https://doi.org/10.1016/0163-7258(82)90054-7; PMID6752975; indexed metadata only | context_only | The ARO-adopted 1982 Bacitracin citation resolves as a review. No abstract/full text was inspected; it is not used as primary evidence for specific resistance or binding assays. |
| adapter | kg-microbe-sources imodulondb; Recent same-session datasets and gene queries09:40:51–52 UTC reused before F protein follow-up | context_only | Structured queries preceded open-ended protein follow-up. Returned e_coli/precise1k/b3057 and b_subtilis/modulome/BSU_36530, each a UPP phosphatase gene and zero iModulon hits. No covered B.licheniformis or E.faecalis dataset was available. Gene context is not expression, transport or resistance proof. Same native resistance terms recur in F; these are gene-context results, not F-specific response or evidence for eukaryotic PDI. |
| uppp | https://doi.org/10.1093/jac/dkt048; PMID23460607; inspected indexed abstract | partial | E.faecalis JH2-2/V583 uppP mutants had bacitracin MIC3–6 mg/L versus32–48 wild type; overexpression increased MIC. This supports that species-specific BacA-type phosphatase resistance mechanism. Abstract does not establish a purified A preparation or E.coli-specific result. Abstract does not identify an isolated F preparation. |
| bcrab | https://doi.org/10.1111/j.1365-2958.1995.tb02322.x; PMID7476193; inspected indexed abstract | partial | B.licheniformis bcrABC locus transferred resistance to heterologous hosts. BcrA was an ATP-binding component and BcrB/BcrC hydrophobic components; removal of antibiotic from its target was proposed. Abstract does not supply direct drug-flux proof or purified-A composition. This B.licheniformis BcrC is distinct from B.subtilis phosphatase BcrC. Abstract does not identify an isolated F preparation. |
| bcrc | https://doi.org/10.1074/jbc.M413750200; PMID15946938; inspected indexed abstract | partial | B.subtilis BcrC/YwoA is a PAP2-family UPP phosphatase, experimentally linked to resistance, membrane phosphatase enhancement and purified-enzyme activity. The work concerns lipid-carrier dephosphorylation, not mutation of a bacitracin protein target. Exact preparation transfer remains unresolved at abstract level. Abstract does not identify an isolated F preparation. |
| search | Free EuropePMC and ignored-inclusive repository search; Bacitracin F compound query and native identifier/label/slug | context_only | EuropePMC exact-phrase search returned33 indexed records, including isolation/degradation studies and the PDI assay. No positive isolated-F antibacterial growth assay was established in this bounded inspected set. The negative assessment rests on the primary measured conditions, not search absence. |
| local-search | CultureBotAI/AntibioticMech; Ignored-inclusive local target search | context_only | Raw owners, native and generated/research references were searched including ignored files outside.git/.venv. Generated and historical research references were discovery context only. |
| gates | just validate; just validate-strict; Actual batch015 focused commands | supports | Both exit0; strict checked one file with zero errors. Native encodings are internally consistent while stereochemical specificity and antibacterial eligibility remain scientific concerns. |

## Limits And Additional Notes

- The negative primary bacterial assays cover specific strains and concentrations through25 micrograms/mL; higher MICs can still occur for genuine antibacterial compounds. This panel alone does not disprove the native class, establish universal inactivity or show absent molecular binding.
- The PDI source was inspected at abstract level. Protein taxon and analogue-specific covalent mechanism were not resolved; no antimicrobial protein target is inferred.
- The1982 adopted review was verified bibliographically only. Current primary F isolation/analysis evidence supplies the assessed structural and assay boundaries.
- Recent same-session structured resistance queries are reused for identical gene terms; they are not F-response data. Generic resistance primary abstracts did not resolve isolated F.
- The natural full stereochemical replacement accession remains unresolved. The more specified PubChem candidate requires residue-by-residue adjudication and still contains an unspecified centre.
- A public2024 author PDF request returned403; its background F statements are not used as independent primary F assay evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All20 captured input hashes unchanged. No native/source-table, status or history edits.
- The initial chemical helper assumed a ChEBI mint and overstrict mass precision; corrected scratch checks use the actual ARO source and acknowledge coarse PubChem mass reporting. These are helper limitations, not native findings.
- No optional absent field is classified as invalid schema.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T100559Z-bacitracin-f
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Bacitracin F: lost natural stereochemistry and bounded antibacterial evidence'
started_at: '2026-10-21T09:50:42Z'
finished_at: '2026-10-21T10:05:59Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Whole record/owner capture, current chemical authorities, actual
    validators, primary isolated-component structure/negative growth assays and separate
    biochemical activity lead.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'One confirmed major finding: the record loses 13 established natural stereochemical
  assignments. An informational follow-up preserves the unresolved antibacterial scope
  of the degradation product: the MIC >25 panel alone does not refute its classification.
  Connectivity and oxidative degradation definition are supported. PDI inhibition
  is separate biochemical context. Focused validators and internal chemistry pass.'
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: conf/sources.yaml
    sha256: 4a2dcd7a3a88953b6cb35b51a48ed77b626c3af2cbb542b0d38ba10540ed7df9
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: curation/curator_antibiotics.tsv
    sha256: 224cbb7261add427184b2762a29c2ff3e85c85e0a06cf22b144545346487247b
    role: context
  - path: curation/decisions.tsv
    sha256: a5834b44307b0449b0df9362c551b7fcd707f3ae51f73d429d37d51f5a169d61
    role: context
  - path: data/antibiotics/antibacterial/bacitracin-f.yaml
    sha256: 98e6c754bed73cc961ebf84fdc370a7b827da49336d96c4c0a18c2cd1f0057b1
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
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
- target_id: antibioticmech:aro-fb45bd17a5
  path: data/antibiotics/antibacterial/bacitracin-f.yaml
  label: bacitracin F
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition, class and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: PubChem molecular enrichment
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported target assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target role mapping
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Claim review decisions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusions
scope:
  description: Whole-record review of minted bacitracin F.
  selection: Queue141 in isolated batch015.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-fb45bd17a5
  exclusions:
  - target: A/B congeners, bacitracin complex and PDI as separate records
    reason: Evidence and identity boundaries only.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/bacitracin-f.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/bacitracin-f.yaml --out /private/tmp/am-review-session/141-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Internal encodings, chemical properties and source mint
  status: passed
  required: true
  summary: Both encodings parse and agree; all13 unspecified centres are separately
    assessed against primary identity.
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  evidence_ids:
  - chemistry
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-fb45bd17a5
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
  - antibioticmech:aro-fb45bd17a5
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
  - antibioticmech:aro-fb45bd17a5
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
  - antibioticmech:aro-fb45bd17a5
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
  - antibioticmech:aro-fb45bd17a5
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
  - antibioticmech:aro-fb45bd17a5
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
  - antibioticmech:aro-fb45bd17a5
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
  - antibioticmech:aro-fb45bd17a5
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
  - antibioticmech:aro-fb45bd17a5
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/bacitracin-f.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T09:57:50Z'
  support: supports
  summary: Read MINTED/SEEDED identity, definition and PMID6752975, NRPS parent/class,
    all chemical fields, two xrefs, ARO source concept, four resistance assertions,
    two database-only chemical targets and four seed-history events. No activity,
    producer, clinical, dataset or graph blocks are populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; data/raw/aro_target_edges.tsv;
    data/raw/aro_resistance_edges.tsv
  locator: ARO row131; PubChem row31; target rows147–148; resistance rows2978–2981
  accessed_at: '2026-10-21T09:57:50Z'
  support: supports
  summary: Native inherits ARO3000631 definition/classification and CID3082210 structure.
    Correct ARO/PubChem source, enrichment and claim owners were captured before judgment.
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/3082210
  locator: Live PUG properties
  accessed_at: '2026-10-21T09:51:27Z'
  support: supports
  summary: Current source reproduces FCLQHQCOKGKLHR-UHFFFAOYSA-N, C66H98N16O17S, charge0
    and reported masses. Standard InChI has no stereochemistry layer.
  snapshot_sha256: a80bef193d9d178579a181b77d59e728f969084dbb0135d533bc8599db0ddd2e
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit and ARO mint checks
  locator: Native encodings
  accessed_at: '2026-10-21T09:51:26Z'
  support: supports
  summary: SMILES and InChI both parse to one neutral fragment with the same formula/key.
    Exact mass agrees. PubChem average mass is coarsely reported to one decimal. All13
    potential tetrahedral centres are unspecified; actual ARO mint reproduces. This
    is a connectivity-level representation, not a racemate designation.
  snapshot_sha256: 3bc6df52ce06c4430109465149afa1c3f8de8b7cab0794ca92819914b7bbe86e
- evidence_id: specified-lead
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/121232955
  locator: Alternative named bacitracin F identity
  accessed_at: '2026-10-21T09:52:10Z'
  support: context_only
  summary: 'Another PubChem entry has the same connectivity but12 specified centres
    and one unspecified centre, key FCLQHQCOKGKLHR-PPPWKGACSA-N. It is not an automatic
    replacement: full residue configuration and the remaining uncertainty must be
    adjudicated against primary evidence, not chosen by label.'
  snapshot_sha256: f1c8d60b94058738b1966b688742754b938cfab1eeb20a0c92471c959d5d9ea6
- evidence_id: primary1995
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.48.233
  locator: PMID7730158; full PDF, Methods, Tables2/3/5, Figures3/4; pp237/240 visually
    inspected
  accessed_at: '2026-10-21T09:47:49Z'
  support: partial
  summary: Study isolated F, checked purity above95% by HPLC, analyzed amino-acid
    configurations and confirmed the oxidized ketothiazole structure. The paper retains
    defined L/D residue configurations and the N-terminal side-chain configuration;
    the all-unspecified native structure loses this information. Table5 shows F MIC>25
    micrograms/mL against M.luteus ATCC9341, S.aureus IFO12732 and B.cereus var.mycoides
    ATCC11778; text reports no activity in the tested range against B.subtilis ATCC6633
    and E.coli IFO3806. Agar dilution used Mueller-Hinton II,37C/20h. The same experiment
    found A activity at lower concentrations, establishing loss of potency for F within
    this panel. MIC>25 alone does not exclude antibacterial activity above the tested
    range or under other conditions.
  snapshot_sha256: 37a8ee478fcf7f842b7ee036c11b1babe6d8715f1c5fd699c2b15f44df89d5b1
- evidence_id: primary2017
  kind: primary_source
  reference: https://doi.org/10.1016/j.jpha.2016.06.001
  locator: PMID29404017/PMC5686873; full Methods and Results3.2.2.1
  accessed_at: '2026-10-21T09:47:41Z'
  support: supports
  summary: Commercial-material LC-MS identifies F as the ketothiazole oxidation product,
    with an otherwise retained cyclic peptide sequence. This independently supports
    the definition connectivity and degradation relationship. Introductory inactivity/nephrotoxicity
    statements are background, not new biological assays in this study.
  snapshot_sha256: 50347693e46a55d9d00d206def1d7c5d386ffff8d744e6ae4d027b4e438b69a3
- evidence_id: pdi
  kind: primary_source
  reference: https://doi.org/10.1111/j.1742-4658.2011.08119.x
  locator: PMID21481187; indexed abstract
  accessed_at: '2026-10-21T09:52:10Z'
  support: context_only
  summary: Purified bacitracin analogues A/B/H/F inhibited protein disulfide isomerase
    in an insulin-aggregation assay; F IC50 was20 micromolar and B1050 micromolar.
    This establishes a biochemical activity lead despite absent antibacterial inhibition
    in the1995 range. Abstract does not establish a microbial antimicrobial target,
    exact protein taxon, or whether the reported disulfide interaction was independently
    demonstrated for F rather than another analogue. No PDI target is imported.
  snapshot_sha256: ce24531f9fee92c7a41e71e3dd50527e648d92a16efbcd7ae0dd2ce01c15d469
- evidence_id: aro
  kind: authority
  reference: https://purl.obolibrary.org/obo/aro.obo
  locator: Current ARO3000631,3009657,3000719,3003251,3002986–3002988,3003250
  accessed_at: '2026-10-21T09:40:22Z'
  support: supports
  summary: Native source definition, parent/class, PubChem mapping and all six target/resistance
    assertions persist upstream. These are inherited database relationships; current
    resolution does not establish F-specific antibacterial action.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: adopted-review
  kind: database
  reference: https://doi.org/10.1016/0163-7258(82)90054-7
  locator: PMID6752975; indexed metadata only
  accessed_at: '2026-10-21T09:40:56Z'
  support: context_only
  summary: The ARO-adopted 1982 Bacitracin citation resolves as a review. No abstract/full
    text was inspected; it is not used as primary evidence for specific resistance
    or binding assays.
  snapshot_sha256: 458d043f63517b9606c4e0e7b43e549de2496df3c0c0ce918b70cccbdb8c50b6
- evidence_id: adapter
  kind: database
  reference: kg-microbe-sources imodulondb
  locator: Recent same-session datasets and gene queries09:40:51–52 UTC reused before
    F protein follow-up
  accessed_at: '2026-10-21T09:40:52Z'
  support: context_only
  summary: Structured queries preceded open-ended protein follow-up. Returned e_coli/precise1k/b3057
    and b_subtilis/modulome/BSU_36530, each a UPP phosphatase gene and zero iModulon
    hits. No covered B.licheniformis or E.faecalis dataset was available. Gene context
    is not expression, transport or resistance proof. Same native resistance terms
    recur in F; these are gene-context results, not F-specific response or evidence
    for eukaryotic PDI.
  snapshot_sha256: 4d2187c500f1a8f1e79e7289bc7d5c6310cf9eccc5fbf2657b24f24dfe333de1
- evidence_id: uppp
  kind: primary_source
  reference: https://doi.org/10.1093/jac/dkt048
  locator: PMID23460607; inspected indexed abstract
  accessed_at: '2026-10-21T09:40:56Z'
  support: partial
  summary: E.faecalis JH2-2/V583 uppP mutants had bacitracin MIC3–6 mg/L versus32–48
    wild type; overexpression increased MIC. This supports that species-specific BacA-type
    phosphatase resistance mechanism. Abstract does not establish a purified A preparation
    or E.coli-specific result. Abstract does not identify an isolated F preparation.
  snapshot_sha256: 2cc47afa1775164aee385ac70158a7298177b57abb12d3fb5e000d5713421ec1
- evidence_id: bcrab
  kind: primary_source
  reference: https://doi.org/10.1111/j.1365-2958.1995.tb02322.x
  locator: PMID7476193; inspected indexed abstract
  accessed_at: '2026-10-21T09:40:56Z'
  support: partial
  summary: B.licheniformis bcrABC locus transferred resistance to heterologous hosts.
    BcrA was an ATP-binding component and BcrB/BcrC hydrophobic components; removal
    of antibiotic from its target was proposed. Abstract does not supply direct drug-flux
    proof or purified-A composition. This B.licheniformis BcrC is distinct from B.subtilis
    phosphatase BcrC. Abstract does not identify an isolated F preparation.
  snapshot_sha256: 700673e74e4795eade4e37a143bfb13380cd4553642ecb67780bf4b7d3d28c5e
- evidence_id: bcrc
  kind: primary_source
  reference: https://doi.org/10.1074/jbc.M413750200
  locator: PMID15946938; inspected indexed abstract
  accessed_at: '2026-10-21T09:40:56Z'
  support: partial
  summary: B.subtilis BcrC/YwoA is a PAP2-family UPP phosphatase, experimentally linked
    to resistance, membrane phosphatase enhancement and purified-enzyme activity.
    The work concerns lipid-carrier dephosphorylation, not mutation of a bacitracin
    protein target. Exact preparation transfer remains unresolved at abstract level.
    Abstract does not identify an isolated F preparation.
  snapshot_sha256: 1dd831fb5aac9018301d8e181fc090708939c02b7b16bbfbc988164a12e967ff
- evidence_id: search
  kind: search
  reference: Free EuropePMC and ignored-inclusive repository search
  locator: Bacitracin F compound query and native identifier/label/slug
  accessed_at: '2026-10-21T09:51:28Z'
  support: context_only
  summary: EuropePMC exact-phrase search returned33 indexed records, including isolation/degradation
    studies and the PDI assay. No positive isolated-F antibacterial growth assay was
    established in this bounded inspected set. The negative assessment rests on the
    primary measured conditions, not search absence.
  search_scope: prepare.py141 rg --no-ignore --hidden outside.git/.venv; current ARO/PubChem;
    exact-phrase EuropePMC core query; primary1995/2017 full text and2011 abstract.
  snapshot_sha256: 82329bdf5614671824f9de830dbda45a3798886217430e34e6b0a361d91aa632
- evidence_id: local-search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive local target search
  accessed_at: '2026-10-21T09:50:43Z'
  support: context_only
  summary: Raw owners, native and generated/research references were searched including
    ignored files outside.git/.venv. Generated and historical research references
    were discovery context only.
  search_scope: Full worktree identifier, label and slug search with rg --no-ignore
    --hidden.
  snapshot_sha256: 9e8f38e2533042b8af522505b95e35d3c6b739d3cd29451a9f53496851ab36ec
- evidence_id: gates
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual batch015 focused commands
  accessed_at: '2026-10-21T09:57:50Z'
  support: supports
  summary: Both exit0; strict checked one file with zero errors. Native encodings
    are internally consistent while stereochemical specificity and antibacterial eligibility
    remain scientific concerns.
  snapshot_sha256: e95c1f3238406c7c66413ee7b8f8acb005b1bff92c8fde1d74bdb15eb032fed4
assessments:
- assessment_id: identity
  area: identity
  topic: Oxidized F connectivity and stereochemistry
  outcome: concern
  summary: Connectivity, formula and oxidative-deamination relationship are supported,
    but all13 unspecified centres fail to represent the primary-characterized configurations
    of natural F. Do not interpret unspecified centres as a demonstrated racemate.
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  evidence_ids:
  - native
  - pubchem
  - chemistry
  - primary1995
  - primary2017
- assessment_id: definition
  area: evidence
  topic: Degradation relationship and mixture wording
  outcome: supported
  summary: The definition correctly describes F as a component/degradation product
    and attributes cell-wall synthesis interference to the mixture. That wording does
    not itself establish F antibacterial action.
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  evidence_ids:
  - native
  - primary1995
  - primary2017
- assessment_id: classification
  area: grounding
  topic: Antibacterial eligibility versus peptide class
  outcome: concern
  summary: 'NRPS-derived peptide classification is coherent. Antibacterial eligibility
    remains unresolved in this review: purified F did not inhibit the tested strains
    up to25 micrograms/mL, but that threshold alone cannot refute the classification.
    The source description of an inactive degradation product motivates further exact-F
    adjudication, not automatic exclusion.'
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  evidence_ids:
  - aro
  - primary1995
  - search
- assessment_id: xref
  area: provenance
  topic: Source identifiers
  outcome: supported
  summary: ARO and PubChem identifiers resolve and reproduce the adopted representation;
    structural specificity is assessed separately. The more specified named PubChem
    entry is a lead only.
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  evidence_ids:
  - aro
  - pubchem
  - specified-lead
- assessment_id: targets
  area: evidence
  topic: Two carrier-target database assertions
  outcome: unknown
  summary: Faithful, explicitly qualified ARO assertions do not establish F-specific
    lipid-pyrophosphate binding or an antibacterial mechanism. Negative growth assays
    alone do not prove absence of molecular binding.
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  evidence_ids:
  - native
  - aro
  - primary1995
- assessment_id: resistance
  area: evidence
  topic: Four inherited resistance assertions
  outcome: unknown
  summary: Current ARO supports provenance; inspected generic bacitracin resistance
    abstracts do not resolve isolated F. Preserve database-only status and revisit
    source scope alongside eligibility; no blanket claim that all named genes lack
    function.
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  evidence_ids:
  - native
  - aro
  - adapter
  - uppp
  - bcrab
  - bcrc
- assessment_id: activity
  area: evidence
  topic: Negative antibacterial assay and biochemical activity
  outcome: supported
  summary: The primary agar assay has bounded negative F results. Separately, PDI
    inhibition is a real biochemical lead, not evidence of bacterial killing or a
    microbial target.
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  evidence_ids:
  - primary1995
  - pdi
- assessment_id: provenance
  area: provenance
  topic: Mint and seed history
  outcome: supported
  summary: Source metadata, actual ARO mint and four seed events are coherent. No
    native status change.
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  evidence_ids:
  - native
  - owners
  - chemistry
- assessment_id: completeness
  area: completeness
  topic: Source adjudication before optional annotations
  outcome: unknown
  summary: Eligibility and exact configuration should be resolved before adding claims
    or promoting status. Optional absent fields are not schema defects; negative observations
    may be curated only in their exact assay context.
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  evidence_ids:
  - primary1995
  - pdi
- assessment_id: other
  area: scope
  topic: Producer, clinical, dataset and graph claims
  outcome: not_applicable
  summary: No populated native claims. Nephrotoxicity background and generic treatment
    statements are not added as native facts.
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  evidence_ids:
  - native
  - primary2017
- assessment_id: schema
  area: schema
  topic: Focused validation
  outcome: supported
  summary: Both actual validators pass; internal encoding checks agree.
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  evidence_ids:
  - gates
  - chemistry
findings:
- finding_id: F1
  issue_key: bacitracin-f-antibacterial-eligibility-unresolved
  category: grounding
  severity: informational
  status: open
  certainty: provisional
  title: Reassess antibacterial eligibility of the oxidized F component
  description: Primary isolated-F assays show markedly lower potency than A and no
    inhibition through25 micrograms/mL in the measured panel. The paper also describes
    F as an inactive degradation product, but its bounded panel does not establish
    universal inactivity. Antibacterial eligibility requires further source adjudication;
    neither mixture membership nor PDI inhibition resolves it. The native classification
    is not declared disproven, and missing citations on a role are not themselves
    a defect.
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  field_paths:
  - antimicrobial_class
  - source_concepts
  evidence_ids:
  - native
  - owners
  - aro
  - primary1995
  - pdi
  - search
  rule_id: native-review-checklist:Antimicrobial Roles and Evidence Fidelity; docs/HARMONIZATION.md:The
    unit of the corpus is a structure
  native_severity: informational unresolved antibacterial scope
  normalization_reason: The inspected bounded negative assay and background inactivity
    characterization justify further research but do not establish a required corrective
    edit to the antibacterial class. Higher concentrations or other organisms may
    show activity; missing role citations are not themselves a defect. The confirmed
    stereochemical defect is tracked separately.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition, class and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: PubChem molecular enrichment
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported target assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target role mapping
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Claim review decisions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusions
- finding_id: F2
  issue_key: bacitracin-f-unspecified-natural-stereochemistry
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Resolve the loss of natural F stereochemical specificity
  description: The PubChem fallback encodes all13 tetrahedral centres without configuration,
    although the primary F characterization identifies defined residue stereochemistry.
    The connectivity-level entity is broader than the experimentally isolated natural
    compound. A separately named partially specified PubChem entry is not an automatically
    valid replacement.
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  field_paths:
  - chemical_structure
  - xrefs[1]
  - grounding_status
  evidence_ids:
  - native
  - pubchem
  - chemistry
  - primary1995
  - specified-lead
  rule_id: native-review-checklist:Identity and Equivalence; docs/HARMONIZATION.md:The
    unit of the corpus is a structure
  native_severity: major loss of established stereochemical granularity
  normalization_reason: Connectivity and oxidation state remain supported; unspecified
    configuration is broader rather than positively assigning the wrong stereoisomer.
    This warrants major rather than blocker.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition, class and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: PubChem molecular enrichment
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported target assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target role mapping
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Claim review decisions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusions
actions:
- action_id: A1
  description: Optionally investigate exact-F antibacterial scope and preserve the
    bounded negative primary observations; do not change eligibility solely on this
    panel.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition, class and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: PubChem molecular enrichment
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported target assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target role mapping
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Claim review decisions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusions
  acceptance_checks:
  - Adjudicate exact-F antimicrobial scope using evidence beyond the bounded negative
    panel; consider higher test concentrations and other organisms/conditions before
    concluding ineligibility. Existing role assertions do not independently require
    a citation.
  - If ineligible, use the supported exclusion/worklist mechanism rather than silently
    deleting generated YAML or inventing a replacement class.
  - Preserve MIC>25 qualifiers, exact strains, Mueller-Hinton II medium and incubation;
    do not generalize inactivity beyond tested conditions.
  - Do not infer that negative growth assays disprove binding, or promote generic
    bacitracin resistance assertions to exact-F primary evidence.
  - Regenerate from maintained owners and rerun corpus, target/resistance, reference
    and history gates.
- action_id: A2
  description: Resolve a primary-supported stereochemical structure for the isolated
    F entity if retained; separately adjudicate any source accession replacement.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-fb45bd17a5
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition, class and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: PubChem molecular enrichment
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported target assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target role mapping
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Claim review decisions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusions
  acceptance_checks:
  - Map each retained residue and side-chain configuration to inspected primary structural
    evidence.
  - Do not equate unspecified stereochemistry with a racemate or select a candidate
    accession by name alone.
  - Any replacement full SMILES/InChI/key/formula/charge agrees and identity/duplicate
    checks pass.
  - Resolve antimicrobial eligibility before adding optional activity or target assertions;
    retain SEEDED until scientific criteria pass.
limitations:
- The negative primary bacterial assays cover specific strains and concentrations
  through25 micrograms/mL; higher MICs can still occur for genuine antibacterial compounds.
  This panel alone does not disprove the native class, establish universal inactivity
  or show absent molecular binding.
- The PDI source was inspected at abstract level. Protein taxon and analogue-specific
  covalent mechanism were not resolved; no antimicrobial protein target is inferred.
- The1982 adopted review was verified bibliographically only. Current primary F isolation/analysis
  evidence supplies the assessed structural and assay boundaries.
- Recent same-session structured resistance queries are reused for identical gene
  terms; they are not F-response data. Generic resistance primary abstracts did not
  resolve isolated F.
- The natural full stereochemical replacement accession remains unresolved. The more
  specified PubChem candidate requires residue-by-residue adjudication and still contains
  an unspecified centre.
- A public2024 author PDF request returned403; its background F statements are not
  used as independent primary F assay evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All20 captured input hashes unchanged. No native/source-table, status or history
  edits.
- The initial chemical helper assumed a ChEBI mint and overstrict mass precision;
  corrected scratch checks use the actual ARO source and acknowledge coarse PubChem
  mass reporting. These are helper limitations, not native findings.
- No optional absent field is classified as invalid schema.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://pubchem.ncbi.nlm.nih.gov/compound/3082210
- https://doi.org/10.7164/antibiotics.48.233
- https://doi.org/10.1016/j.jpha.2016.06.001
- https://doi.org/10.1111/j.1742-4658.2011.08119.x
tags:
- bacitracin-f
- antibacterial-eligibility
- stereochemistry
- negative-assay
```
