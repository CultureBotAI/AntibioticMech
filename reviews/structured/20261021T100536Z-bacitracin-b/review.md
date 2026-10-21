# Bacitracin B: nonnatural stored stereochemistry and unresolved generic-congener mapping

- Review: 20261021T100536Z-bacitracin-b
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:46:27Z
- Finished UTC: 2026-10-21T10:05:36Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One blocker: the stored Val8 structure has six inverted defined centres and unspecified His10 relative to natural material. One major finding: a generic B fraction is mapped to one congener without supported adjudication. Focused validators and internal chemistry pass; primary congener assays are preserved without transfer to the mismatching structure.

## Scope And Provenance

Whole-record review of minted bacitracin B.

Selection: Queue140 in isolated batch014.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-d2b8d66d15 | data/antibiotics/antibacterial/bacitracin-b.yaml | generated | bacitracin B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | antibioticmech:aro-d2b8d66d15 | Actual command passed. |
| Focused strict | passed | True | antibioticmech:aro-d2b8d66d15 | Actual command passed. |
| Internal chemical consistency and actual ARO mint | passed | True | antibioticmech:aro-d2b8d66d15 | Encodings, formula, charge, masses and source mint agree internally; natural stereochemistry conflicts separately. |
| Authoritative full QC | failed | True | antibioticmech:aro-d2b8d66d15 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-d2b8d66d15 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-d2b8d66d15 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-d2b8d66d15 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-d2b8d66d15 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-d2b8d66d15 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-d2b8d66d15 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-d2b8d66d15 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-d2b8d66d15 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Natural B congener versus stored stereochemistry

identity: concern. Targets: antibioticmech:aro-d2b8d66d15.

Native has Val8 connectivity but six specified centres conflict with characterized natural material and His10 remains unspecified. Passing internal chemistry and matching live PubChem do not make this natural B2.

### Generic B source concept

identity: concern. Targets: antibioticmech:aro-d2b8d66d15.

B is historically a fraction with three positional congeners; source definition does not identify the replacement position. Exact congener mapping must be adjudicated before this generic source is assigned one molecular record.

### ARO and PubChem links

grounding: supported. Targets: antibioticmech:aro-d2b8d66d15.

Both identifiers resolve and faithfully represent source mappings. The PubChem molecular identity itself is scientifically problematic, so resolution is not an endorsement of the assignment.

### Component and cell-wall description

evidence: unknown. Targets: antibioticmech:aro-d2b8d66d15.

The generic definition is compatible with historical B fractions and bacitracin mixture mechanism, but the1982 review was verified only bibliographically and cannot establish the stored stereochemical entity.

### NRPS class and antibacterial filing

grounding: supported. Targets: antibioticmech:aro-d2b8d66d15.

Primary congeners are cyclic peptide antibacterials and the NRPS superclass is appropriate. Exact native activity remains unresolved because its molecular stereochemistry differs.

### Carrier chemical targets

evidence: unknown. Targets: antibioticmech:aro-d2b8d66d15.

Both native entries clearly label chemical carrier database assertions. Exact B-congener direct binding was not established in the bounded primary review. Do not transfer purified-A crystal/liposome results automatically.

### Four database assertions

evidence: unknown. Targets: antibioticmech:aro-d2b8d66d15.

Faithful inherited assertions retain their limited status. Generic bacitracin resistance experiments do not prove the same activity for the stored stereoisomer. Species-specific BcrC and biosynthetic BacA naming boundaries remain necessary.

### Defined natural B-congener MICs

evidence: supported. Targets: antibioticmech:aro-d2b8d66d15.

Primary isolated B congeners have measured activity. Numerical transfer to native is conditional on resolving identity, not an argument that the measurements are unreliable.

### Source, mint and history

provenance: supported. Targets: antibioticmech:aro-d2b8d66d15.

ARO mint, fallback source provenance and four seed events are coherent; the upstream structure defect remains.

### Evidence addition priority

completeness: unknown. Targets: antibioticmech:aro-d2b8d66d15.

Identity and congener mapping precede optional primary activity/target additions. Empty optional fields are not separate findings and SEEDED is retained.

### Producer, clinical, dataset and graph blocks

scope: not_applicable. Targets: antibioticmech:aro-d2b8d66d15.

No populated native claims; no clinical or transcriptomic inference made.

### Focused validation

schema: supported. Targets: antibioticmech:aro-d2b8d66d15.

Both actual validators and internal formula/encoding checks pass. Scientific molecular correspondence is independently assessed.

## Findings

### F1: Correct the molecular stereochemistry before treating this as natural bacitracin B

blocker / open / confirmed; issue key: bacitracin-b-nonnatural-stereochemistry.

Native and live CID121232829 represent Val8 connectivity with six defined centres inverted relative to the primary-characterized natural congener and His10 unspecified. This affects the principal structure, not just an external xref. Exact antimicrobial identity and primary-assay transfer are blocked pending a supported complete structure.

### F2: Adjudicate the generic B fraction against individually resolved congeners

major / open / confirmed; issue key: bacitracin-b-generic-fraction-versus-congener.

Primary studies distinguish B congeners with Val at positions1,5 or8, with historical numbering differences. The adopted generic B concept and definition do not justify selecting one position. Establish whether the source denotes a group/fraction or one explicitly supported congener before retaining an exact molecular mapping.

## Recommended Actions And Acceptance Checks

### A1

Resolve a primary-supported full natural congener structure through maintained PubChem/identity adjudication, preserving the present erroneous accession as provenance where appropriate.

- Verify all residue configurations, including Ile1, Leu3, Ile5, Lys6 and His10, against the characterized congener.
- Do not promote a scratch-derived comparison key to authority without independent identity verification.
- Regenerated SMILES/InChI/key/formula agree and all required identity, duplicate, term, reference and history gates pass.
- No MIC or direct-target claim is attached to the mismatching current stereoisomer.

### A2

Adjudicate whether ARO3000630 is the historical B group or one exact congener; use the supported exclusion/worklist route for a group and separately ground individual compounds if justified.

- Document residue-position mapping rather than relying on B1/B2/B3 labels across publications.
- Retain primary assay strain, preparation, medium, units and threshold qualifiers for any later activity_spectrum additions.
- Keep generic bacitracin resistance assertions distinct from exact-congener primary experiments; do not automatically inherit A binding assays.
- Regenerate from maintained owners and rerun focused plus full corpus checks; retain SEEDED until scientific sign-off criteria pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/bacitracin-b.yaml; Entire YAML | supports | Read MINTED/SEEDED identity, definition and PMID6752975, NRPS class/parent, all PubChem chemical fields, two xrefs, one source concept, four resistance assertions, two database-only chemical targets and four seed-history events. No populated optional activity, producer, clinical, dataset or graph blocks. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; data/raw/aro_target_edges.tsv; data/raw/aro_resistance_edges.tsv; ARO row130; PubChem row30; target rows145–146; resistance rows2974–2977 | supports | Native faithfully inherits ARO3000630 generic B definition and CID121232829 structure. Applicable ARO/PubChem extraction, enrichment, claim and seeding owners were captured before assessment. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/121232829; Live PUG chemical properties | supports | Live PubChem reproduces native C65H101N17O16S, neutral charge, rounded mass1408.7, exact1407.73329138 and key CDTJNKFURPZXMS-LRBSCOJMSA-N. Upstream agreement does not establish the natural congener stereochemistry. |
| chemistry | Independent RDKit and actual ARO source-mint check; Native SMILES/InChI | supports | Both encodings parse to the same one-fragment neutral structure, formula and key. Masses agree within reported precision. There are13 specified and one unspecified tetrahedral centres. The actual ARO mint reproduces. These internal consistency checks do not prove biological identity. |
| stereo | Independent natural-Val8 congener comparison; Scratch derivation from bacitracin A and full graph mapping | refutes | Using the independently supported A structure, replace only Ile8 terminal carbon with hydrogen to produce Val8; retain all remaining stereochemistry. Result has identical native connectivity and key CDTJNKFURPZXMS-QTFUODODSA-N. Native differs at six defined centres: Ile1 alpha/beta, Leu3 alpha, Ile5 alpha/beta, Lys6 alpha. His10 is unspecified. This is not merely a tautomer, CIP-numbering change or missing one stereo assignment. The derived structure is a comparison model, not an automatically curated replacement. |
| a-reference | https://pubchem.ncbi.nlm.nih.gov/compound/10909430; Live bacitracin A identity used only as a structural comparator | context_only | A full key CLKOFPXJLQSYAH-ABRJDSQDSA-N agrees with ChEBI and primary structural sequence. The B comparison alters only Ile8 connectivity and preserves the primary-supported remaining residues. No A activity or direct-target assay is transferred to B. |
| primary1995 | https://doi.org/10.7164/antibiotics.48.233; PMID7730158; full primary PDF, Methods, Tables1/3/5 and Figures3/4; pp237/240 visually inspected | supports | HPLC-isolated components were characterized by amino-acid stereochemical analysis and mass spectrometry. Historical B material comprised three positional congeners. In this paper B1 substitutes Val1, B2 Val8 and B3 Val5; remaining residues retain the A configuration, including L-Leu, L-Lys, L-His and L-Ile. Hydrolysis-induced N-terminal epimerization is explicitly corrected and is not natural stereochemical heterogeneity. Table5 reports purified B2 MIC0.78 micrograms/mL for M.luteus ATCC9341,12.5 for S.aureus IFO12732 and25 for B.cereus var.mycoides ATCC11778, using Mueller-Hinton II agar,37C/20h. These measurements apply to the defined natural congener, not the mismatching native stereoisomer. |
| primary2017 | https://doi.org/10.1016/j.jpha.2016.06.001; PMID29404017/PMC5686873; full Methods and Results3.2/Table2 | supports | Analysis of commercial batch130902BA and USP reference material independently separates B1/B2/B3 and assigns the same three substitution positions. It is analytical structural evidence, not a new MIC or target study. Its introductory claim that bacitracin belongs to polymyxins is not adopted; native NRPS classification remains the appropriate broader class. |
| primary1994 | https://doi.org/10.1002/bms.1200230403; PMID8172927; indexed abstract | context_only | Earlier isolated-congener study calls Val8 material B1a, Val5 material B1b and Val1 material B2. This naming difference explains why names alone cannot resolve the exact compound. Molecular position and stereochemistry are the mapping criteria. |
| aro | https://purl.obolibrary.org/obo/aro.obo; Current ARO3000630,3009657,3000719,3003251,3002986–3002988,3003250 | supports | All native ARO identifiers resolve and generic B target/resistance assertions persist. Database provenance does not assign one of the three natural B congeners or resolve the native stereochemistry. |
| adopted-review | https://doi.org/10.1016/0163-7258(82)90054-7; PMID6752975; indexed metadata only | context_only | The ARO-adopted 1982 Bacitracin citation resolves as a review. No abstract/full text was inspected; it is not used as primary evidence for specific resistance or binding assays. |
| adapter | kg-microbe-sources imodulondb; Reused same-session actual datasets and gene queries from09:40:51–52 UTC, before open-ended B protein follow-up | context_only | Structured queries preceded open-ended protein follow-up. Returned e_coli/precise1k/b3057 and b_subtilis/modulome/BSU_36530, each a UPP phosphatase gene and zero iModulon hits. No covered B.licheniformis or E.faecalis dataset was available. Gene context is not expression, transport or resistance proof. The same four native resistance terms are present in A and B; this recent exact gene-context query is reused without implying a B-specific experiment. |
| uppp | https://doi.org/10.1093/jac/dkt048; PMID23460607; inspected indexed abstract | partial | E.faecalis JH2-2/V583 uppP mutants had bacitracin MIC3–6 mg/L versus32–48 wild type; overexpression increased MIC. This supports that species-specific BacA-type phosphatase resistance mechanism. Abstract does not establish a purified A preparation or E.coli-specific result. No exact B-congener preparation is established in the inspected abstract. |
| bcrab | https://doi.org/10.1111/j.1365-2958.1995.tb02322.x; PMID7476193; inspected indexed abstract | partial | B.licheniformis bcrABC locus transferred resistance to heterologous hosts. BcrA was an ATP-binding component and BcrB/BcrC hydrophobic components; removal of antibiotic from its target was proposed. Abstract does not supply direct drug-flux proof or purified-A composition. This B.licheniformis BcrC is distinct from B.subtilis phosphatase BcrC. No exact B-congener preparation is established in the inspected abstract. |
| bcrc | https://doi.org/10.1074/jbc.M413750200; PMID15946938; inspected indexed abstract | partial | B.subtilis BcrC/YwoA is a PAP2-family UPP phosphatase, experimentally linked to resistance, membrane phosphatase enhancement and purified-enzyme activity. The work concerns lipid-carrier dephosphorylation, not mutation of a bacitracin protein target. Exact preparation transfer remains unresolved at abstract level. No exact B-congener preparation is established in the inspected abstract. |
| gates | just validate; just validate-strict; Actual focused batch014 commands | supports | Both commands exit0; strict checked one file with zero errors. Internal encoding consistency passes while the primary structural comparison identifies the stereochemical defect. |
| search | CultureBotAI/AntibioticMech and free public literature; Ignored-inclusive identifier/label/slug and targeted source/congener searches | context_only | Ignored-inclusive repository search covered native, raw, curation, research and generated references outside .git/.venv. Historical/generated material was only discovery context. Free primary follow-up located experimentally characterized B congeners; broad EuropePMC query returned503, so direct citation/publisher sources were used. |

## Limits And Additional Notes

- The1982 definition citation was verified only at metadata level; no abstract was available. The full1995 primary paper and2017 analytical study provide the congener boundary instead.
- The comparison key is a scratch model based on the independently supported A structure and primary Val8 substitution. A curator must establish an independently supported replacement accession and exact source mapping.
- Resistance papers were inspected at abstract level in this same session; exact B-congener preparation and direct BcrAB transport were not established. Recent structured gene queries are reused as context, not drug-response evidence.
- The broad EuropePMC B query returned503; direct primary citation and publisher retrieval succeeded. This is a bounded review, not an exhaustive reconstruction of historical fraction naming.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All20 captured inputs rechecked unchanged. No native/source-table or status/history edits.
- Initial helper assumed a ChEBI source mint; actual ARO mint was recomputed and passes. This helper error is not a native defect.
- No optional empty field is classified as a finding. Distinct natural B activities are retained as useful evidence after identity resolution.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T100536Z-bacitracin-b
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Bacitracin B: nonnatural stored stereochemistry and unresolved generic-congener
  mapping'
started_at: '2026-10-21T09:46:27Z'
finished_at: '2026-10-21T10:05:36Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Whole native and owner review, current source identity, graph-mapped
    stereochemistry, primary isolation/structure/activity paper and independent analytical
    congener evidence.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'One blocker: the stored Val8 structure has six inverted defined centres
  and unspecified His10 relative to natural material. One major finding: a generic
  B fraction is mapped to one congener without supported adjudication. Focused validators
  and internal chemistry pass; primary congener assays are preserved without transfer
  to the mismatching structure.'
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
  - path: data/antibiotics/antibacterial/bacitracin-b.yaml
    sha256: c393649a7602a5f0b6989d556e115d4e173bcf20cf6c85b57443c568f9624759
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
- target_id: antibioticmech:aro-d2b8d66d15
  path: data/antibiotics/antibacterial/bacitracin-b.yaml
  label: bacitracin B
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
  description: Whole-record review of minted bacitracin B.
  selection: Queue140 in isolated batch014.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-d2b8d66d15
  exclusions:
  - target: Other bacitracin records and individual B congeners as separate targets
    reason: Identity and evidence comparators only.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/bacitracin-b.yaml
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
  - antibioticmech:aro-d2b8d66d15
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/bacitracin-b.yaml --out /private/tmp/am-review-session/140-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Internal chemical consistency and actual ARO mint
  status: passed
  required: true
  summary: Encodings, formula, charge, masses and source mint agree internally; natural
    stereochemistry conflicts separately.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
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
  - antibioticmech:aro-d2b8d66d15
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
  - antibioticmech:aro-d2b8d66d15
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
  - antibioticmech:aro-d2b8d66d15
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
  - antibioticmech:aro-d2b8d66d15
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
  - antibioticmech:aro-d2b8d66d15
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
  - antibioticmech:aro-d2b8d66d15
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
  - antibioticmech:aro-d2b8d66d15
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
  - antibioticmech:aro-d2b8d66d15
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
  - antibioticmech:aro-d2b8d66d15
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/bacitracin-b.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T09:50:41Z'
  support: supports
  summary: Read MINTED/SEEDED identity, definition and PMID6752975, NRPS class/parent,
    all PubChem chemical fields, two xrefs, one source concept, four resistance assertions,
    two database-only chemical targets and four seed-history events. No populated
    optional activity, producer, clinical, dataset or graph blocks.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; data/raw/aro_target_edges.tsv;
    data/raw/aro_resistance_edges.tsv
  locator: ARO row130; PubChem row30; target rows145–146; resistance rows2974–2977
  accessed_at: '2026-10-21T09:50:41Z'
  support: supports
  summary: Native faithfully inherits ARO3000630 generic B definition and CID121232829
    structure. Applicable ARO/PubChem extraction, enrichment, claim and seeding owners
    were captured before assessment.
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/121232829
  locator: Live PUG chemical properties
  accessed_at: '2026-10-21T09:47:19Z'
  support: supports
  summary: Live PubChem reproduces native C65H101N17O16S, neutral charge, rounded
    mass1408.7, exact1407.73329138 and key CDTJNKFURPZXMS-LRBSCOJMSA-N. Upstream agreement
    does not establish the natural congener stereochemistry.
  snapshot_sha256: bcf46b4693a2e40776287f2f3547e24ce999288b0f90215610c0019ea76bafa2
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit and actual ARO source-mint check
  locator: Native SMILES/InChI
  accessed_at: '2026-10-21T09:47:13Z'
  support: supports
  summary: Both encodings parse to the same one-fragment neutral structure, formula
    and key. Masses agree within reported precision. There are13 specified and one
    unspecified tetrahedral centres. The actual ARO mint reproduces. These internal
    consistency checks do not prove biological identity.
  snapshot_sha256: 07b74cedee4c9ed99f46e97a3c2214f1b6b357a3a608cbfcd75341340a1dce96
- evidence_id: stereo
  kind: validation
  reference: Independent natural-Val8 congener comparison
  locator: Scratch derivation from bacitracin A and full graph mapping
  accessed_at: '2026-10-21T09:50:30Z'
  support: refutes
  summary: 'Using the independently supported A structure, replace only Ile8 terminal
    carbon with hydrogen to produce Val8; retain all remaining stereochemistry. Result
    has identical native connectivity and key CDTJNKFURPZXMS-QTFUODODSA-N. Native
    differs at six defined centres: Ile1 alpha/beta, Leu3 alpha, Ile5 alpha/beta,
    Lys6 alpha. His10 is unspecified. This is not merely a tautomer, CIP-numbering
    change or missing one stereo assignment. The derived structure is a comparison
    model, not an automatically curated replacement.'
  snapshot_sha256: 0b30e511dcb944a99f70c6738e383e2f0013223b7b5e46849eddb6743d3a928d
- evidence_id: a-reference
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/10909430
  locator: Live bacitracin A identity used only as a structural comparator
  accessed_at: '2026-10-21T09:40:22Z'
  support: context_only
  summary: A full key CLKOFPXJLQSYAH-ABRJDSQDSA-N agrees with ChEBI and primary structural
    sequence. The B comparison alters only Ile8 connectivity and preserves the primary-supported
    remaining residues. No A activity or direct-target assay is transferred to B.
  snapshot_sha256: d86485f14d105fc629ee9cbbc07d8270e042991a84d677bbd5d210ab6464f43d
- evidence_id: primary1995
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.48.233
  locator: PMID7730158; full primary PDF, Methods, Tables1/3/5 and Figures3/4; pp237/240
    visually inspected
  accessed_at: '2026-10-21T09:47:49Z'
  support: supports
  summary: HPLC-isolated components were characterized by amino-acid stereochemical
    analysis and mass spectrometry. Historical B material comprised three positional
    congeners. In this paper B1 substitutes Val1, B2 Val8 and B3 Val5; remaining residues
    retain the A configuration, including L-Leu, L-Lys, L-His and L-Ile. Hydrolysis-induced
    N-terminal epimerization is explicitly corrected and is not natural stereochemical
    heterogeneity. Table5 reports purified B2 MIC0.78 micrograms/mL for M.luteus ATCC9341,12.5
    for S.aureus IFO12732 and25 for B.cereus var.mycoides ATCC11778, using Mueller-Hinton
    II agar,37C/20h. These measurements apply to the defined natural congener, not
    the mismatching native stereoisomer.
  snapshot_sha256: 37a8ee478fcf7f842b7ee036c11b1babe6d8715f1c5fd699c2b15f44df89d5b1
- evidence_id: primary2017
  kind: primary_source
  reference: https://doi.org/10.1016/j.jpha.2016.06.001
  locator: PMID29404017/PMC5686873; full Methods and Results3.2/Table2
  accessed_at: '2026-10-21T09:47:41Z'
  support: supports
  summary: Analysis of commercial batch130902BA and USP reference material independently
    separates B1/B2/B3 and assigns the same three substitution positions. It is analytical
    structural evidence, not a new MIC or target study. Its introductory claim that
    bacitracin belongs to polymyxins is not adopted; native NRPS classification remains
    the appropriate broader class.
  snapshot_sha256: 50347693e46a55d9d00d206def1d7c5d386ffff8d744e6ae4d027b4e438b69a3
- evidence_id: primary1994
  kind: primary_source
  reference: https://doi.org/10.1002/bms.1200230403
  locator: PMID8172927; indexed abstract
  accessed_at: '2026-10-21T09:47:42Z'
  support: context_only
  summary: Earlier isolated-congener study calls Val8 material B1a, Val5 material
    B1b and Val1 material B2. This naming difference explains why names alone cannot
    resolve the exact compound. Molecular position and stereochemistry are the mapping
    criteria.
  snapshot_sha256: d3e04ef76f250f625a1c20ce980c40cc0ece5c820ae2a3e2555d949869cc7746
- evidence_id: aro
  kind: authority
  reference: https://purl.obolibrary.org/obo/aro.obo
  locator: Current ARO3000630,3009657,3000719,3003251,3002986–3002988,3003250
  accessed_at: '2026-10-21T09:40:22Z'
  support: supports
  summary: All native ARO identifiers resolve and generic B target/resistance assertions
    persist. Database provenance does not assign one of the three natural B congeners
    or resolve the native stereochemistry.
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
  locator: Reused same-session actual datasets and gene queries from09:40:51–52 UTC,
    before open-ended B protein follow-up
  accessed_at: '2026-10-21T09:40:52Z'
  support: context_only
  summary: Structured queries preceded open-ended protein follow-up. Returned e_coli/precise1k/b3057
    and b_subtilis/modulome/BSU_36530, each a UPP phosphatase gene and zero iModulon
    hits. No covered B.licheniformis or E.faecalis dataset was available. Gene context
    is not expression, transport or resistance proof. The same four native resistance
    terms are present in A and B; this recent exact gene-context query is reused without
    implying a B-specific experiment.
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
    or E.coli-specific result. No exact B-congener preparation is established in the
    inspected abstract.
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
    phosphatase BcrC. No exact B-congener preparation is established in the inspected
    abstract.
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
    No exact B-congener preparation is established in the inspected abstract.
  snapshot_sha256: 1dd831fb5aac9018301d8e181fc090708939c02b7b16bbfbc988164a12e967ff
- evidence_id: gates
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual focused batch014 commands
  accessed_at: '2026-10-21T09:50:41Z'
  support: supports
  summary: Both commands exit0; strict checked one file with zero errors. Internal
    encoding consistency passes while the primary structural comparison identifies
    the stereochemical defect.
  snapshot_sha256: 65774fab5e5b0a8b877974197c6a1656ce176fa0c47dfc3de9d38cfb29418eac
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech and free public literature
  locator: Ignored-inclusive identifier/label/slug and targeted source/congener searches
  accessed_at: '2026-10-21T09:46:30Z'
  support: context_only
  summary: Ignored-inclusive repository search covered native, raw, curation, research
    and generated references outside .git/.venv. Historical/generated material was
    only discovery context. Free primary follow-up located experimentally characterized
    B congeners; broad EuropePMC query returned503, so direct citation/publisher sources
    were used.
  search_scope: prepare.py140 rg --no-ignore --hidden; ARO/raw target and resistance
    rows; direct1994/1995/2017 primary sources; current PubChem; recent same-session
    structured protein queries.
  snapshot_sha256: 86deb1eff2680db6465e818af7b7c23c973827c593c8bfc8eb8d5cb28a986dd7
assessments:
- assessment_id: identity
  area: identity
  topic: Natural B congener versus stored stereochemistry
  outcome: concern
  summary: Native has Val8 connectivity but six specified centres conflict with characterized
    natural material and His10 remains unspecified. Passing internal chemistry and
    matching live PubChem do not make this natural B2.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
  evidence_ids:
  - native
  - pubchem
  - chemistry
  - stereo
  - primary1995
  - primary2017
- assessment_id: scope
  area: identity
  topic: Generic B source concept
  outcome: concern
  summary: B is historically a fraction with three positional congeners; source definition
    does not identify the replacement position. Exact congener mapping must be adjudicated
    before this generic source is assigned one molecular record.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
  evidence_ids:
  - native
  - owners
  - primary1995
  - primary1994
  - primary2017
- assessment_id: xref
  area: grounding
  topic: ARO and PubChem links
  outcome: supported
  summary: Both identifiers resolve and faithfully represent source mappings. The
    PubChem molecular identity itself is scientifically problematic, so resolution
    is not an endorsement of the assignment.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
  evidence_ids:
  - pubchem
  - aro
  - stereo
- assessment_id: definition
  area: evidence
  topic: Component and cell-wall description
  outcome: unknown
  summary: The generic definition is compatible with historical B fractions and bacitracin
    mixture mechanism, but the1982 review was verified only bibliographically and
    cannot establish the stored stereochemical entity.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
  evidence_ids:
  - native
  - adopted-review
  - primary1995
- assessment_id: classification
  area: grounding
  topic: NRPS class and antibacterial filing
  outcome: supported
  summary: Primary congeners are cyclic peptide antibacterials and the NRPS superclass
    is appropriate. Exact native activity remains unresolved because its molecular
    stereochemistry differs.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
  evidence_ids:
  - aro
  - primary1995
- assessment_id: targets
  area: evidence
  topic: Carrier chemical targets
  outcome: unknown
  summary: Both native entries clearly label chemical carrier database assertions.
    Exact B-congener direct binding was not established in the bounded primary review.
    Do not transfer purified-A crystal/liposome results automatically.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
  evidence_ids:
  - native
  - aro
  - primary1995
  - a-reference
- assessment_id: resistance
  area: evidence
  topic: Four database assertions
  outcome: unknown
  summary: Faithful inherited assertions retain their limited status. Generic bacitracin
    resistance experiments do not prove the same activity for the stored stereoisomer.
    Species-specific BcrC and biosynthetic BacA naming boundaries remain necessary.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
  evidence_ids:
  - native
  - aro
  - adapter
  - uppp
  - bcrab
  - bcrc
- assessment_id: activity
  area: evidence
  topic: Defined natural B-congener MICs
  outcome: supported
  summary: Primary isolated B congeners have measured activity. Numerical transfer
    to native is conditional on resolving identity, not an argument that the measurements
    are unreliable.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
  evidence_ids:
  - primary1995
  - stereo
- assessment_id: provenance
  area: provenance
  topic: Source, mint and history
  outcome: supported
  summary: ARO mint, fallback source provenance and four seed events are coherent;
    the upstream structure defect remains.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
  evidence_ids:
  - native
  - owners
  - chemistry
- assessment_id: completeness
  area: completeness
  topic: Evidence addition priority
  outcome: unknown
  summary: Identity and congener mapping precede optional primary activity/target
    additions. Empty optional fields are not separate findings and SEEDED is retained.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
  evidence_ids:
  - primary1995
  - stereo
- assessment_id: other
  area: scope
  topic: Producer, clinical, dataset and graph blocks
  outcome: not_applicable
  summary: No populated native claims; no clinical or transcriptomic inference made.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
  evidence_ids:
  - native
  - adapter
- assessment_id: schema
  area: schema
  topic: Focused validation
  outcome: supported
  summary: Both actual validators and internal formula/encoding checks pass. Scientific
    molecular correspondence is independently assessed.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
  evidence_ids:
  - gates
  - chemistry
findings:
- finding_id: F1
  issue_key: bacitracin-b-nonnatural-stereochemistry
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Correct the molecular stereochemistry before treating this as natural bacitracin
    B
  description: Native and live CID121232829 represent Val8 connectivity with six defined
    centres inverted relative to the primary-characterized natural congener and His10
    unspecified. This affects the principal structure, not just an external xref.
    Exact antimicrobial identity and primary-assay transfer are blocked pending a
    supported complete structure.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
  field_paths:
  - chemical_structure
  - xrefs[1]
  evidence_ids:
  - native
  - pubchem
  - stereo
  - a-reference
  - primary1995
  - primary2017
  rule_id: native-review-checklist:Identity and Equivalence; docs/HARMONIZATION.md:The
    unit of the corpus is a structure
  native_severity: blocker wrong stereochemical identity
  normalization_reason: Internal encodings agree but denote a different specified
    stereochemical entity from the natural Val8 congener. No automatic conversion
    of unspecified His10 or silent replacement with a comparison model is authorized.
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
  issue_key: bacitracin-b-generic-fraction-versus-congener
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Adjudicate the generic B fraction against individually resolved congeners
  description: Primary studies distinguish B congeners with Val at positions1,5 or8,
    with historical numbering differences. The adopted generic B concept and definition
    do not justify selecting one position. Establish whether the source denotes a
    group/fraction or one explicitly supported congener before retaining an exact
    molecular mapping.
  target_ids:
  - antibioticmech:aro-d2b8d66d15
  field_paths:
  - identifier
  - label
  - definition
  - source_concepts
  - grounding_status
  evidence_ids:
  - native
  - owners
  - primary1995
  - primary1994
  - primary2017
  - aro
  rule_id: docs/HARMONIZATION.md:The unit of the corpus is a structure; native-review-checklist:Evidence
    Fidelity
  native_severity: major unresolved group-to-structure grounding
  normalization_reason: This is source entity scope, distinct from the wrong encoded
    centres. Different B numbering is contextual evidence, not a separate naming or
    synonym finding.
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
  description: Resolve a primary-supported full natural congener structure through
    maintained PubChem/identity adjudication, preserving the present erroneous accession
    as provenance where appropriate.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-d2b8d66d15
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
  - Verify all residue configurations, including Ile1, Leu3, Ile5, Lys6 and His10,
    against the characterized congener.
  - Do not promote a scratch-derived comparison key to authority without independent
    identity verification.
  - Regenerated SMILES/InChI/key/formula agree and all required identity, duplicate,
    term, reference and history gates pass.
  - No MIC or direct-target claim is attached to the mismatching current stereoisomer.
- action_id: A2
  description: Adjudicate whether ARO3000630 is the historical B group or one exact
    congener; use the supported exclusion/worklist route for a group and separately
    ground individual compounds if justified.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-d2b8d66d15
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
  - Document residue-position mapping rather than relying on B1/B2/B3 labels across
    publications.
  - Retain primary assay strain, preparation, medium, units and threshold qualifiers
    for any later activity_spectrum additions.
  - Keep generic bacitracin resistance assertions distinct from exact-congener primary
    experiments; do not automatically inherit A binding assays.
  - Regenerate from maintained owners and rerun focused plus full corpus checks; retain
    SEEDED until scientific sign-off criteria pass.
limitations:
- The1982 definition citation was verified only at metadata level; no abstract was
  available. The full1995 primary paper and2017 analytical study provide the congener
  boundary instead.
- The comparison key is a scratch model based on the independently supported A structure
  and primary Val8 substitution. A curator must establish an independently supported
  replacement accession and exact source mapping.
- Resistance papers were inspected at abstract level in this same session; exact B-congener
  preparation and direct BcrAB transport were not established. Recent structured gene
  queries are reused as context, not drug-response evidence.
- The broad EuropePMC B query returned503; direct primary citation and publisher retrieval
  succeeded. This is a bounded review, not an exhaustive reconstruction of historical
  fraction naming.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All20 captured inputs rechecked unchanged. No native/source-table or status/history
  edits.
- Initial helper assumed a ChEBI source mint; actual ARO mint was recomputed and passes.
  This helper error is not a native defect.
- No optional empty field is classified as a finding. Distinct natural B activities
  are retained as useful evidence after identity resolution.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://pubchem.ncbi.nlm.nih.gov/compound/121232829
- https://doi.org/10.7164/antibiotics.48.233
- https://doi.org/10.1002/bms.1200230403
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5686873/
tags:
- bacitracin-b
- stereochemistry
- congener-scope
- primary-evidence
```
