# Magainin B: two unspecified isoleucine centres and a source definition typo

- Review: 20261021T202611Z-magainin-b-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T20:11:20Z
- Finished UTC: 2026-10-21T20:26:11Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The whole native record and actual ARO/PubChem source rows were reviewed. The stored graph and current PubChem agree, but both leave Ile2 and Ile20 side-chain stereochemistry unspecified. Original synthetic peptide sequences identify ordinary isoleucine at those positions; an independently constructed sequence differs only by these two assignments. Exact B antibacterial and protozoal evidence is available with bounded preparation and endpoint scope. The source definition also repeats the word is.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Assigned queue position 625; one exact native record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-832bfb6c2e | data/antibiotics/antibacterial/magainin-b.yaml | generated | magainin B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-832bfb6c2e | Actual focused execution exited 0. Actual 063 cwd; chemistry used 019 RDKit and schema/strict used 063 environment. Passing syntax/internal consistency does not resolve missing peptide stereo. |
| Focused schema verification | passed | True | antibioticmech:aro-832bfb6c2e | Actual focused execution exited 0. Actual 063 cwd; chemistry used 019 RDKit and schema/strict used 063 environment. Passing syntax/internal consistency does not resolve missing peptide stereo. |
| Focused strict verification | passed | True | antibioticmech:aro-832bfb6c2e | Actual focused execution exited 0. Actual 063 cwd; chemistry used 019 RDKit and schema/strict used 063 environment. Passing syntax/internal consistency does not resolve missing peptide stereo. |
| Authoritative full QC | failed | True | antibioticmech:aro-832bfb6c2e | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-832bfb6c2e | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-832bfb6c2e | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-832bfb6c2e | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-832bfb6c2e | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-832bfb6c2e | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-832bfb6c2e | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-832bfb6c2e | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-832bfb6c2e | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Sequence and unresolved Ile side-chain stereo

identity: concern. Targets: antibioticmech:aro-832bfb6c2e.

The peptide connectivity, all 21 alpha centres and terminal amide match the synthetic B sequence. The native and its PubChem source omit the two beta configurations of ordinary Ile2/Ile20. This is an incomplete exact molecular description, not evidence of a mixed or opposite-stereoisomer preparation. Primary sequence convention identifies ordinary Ile; batch-level chiral purity was not independently measured in the inspected material.

### Source agreement versus exact peptide completeness

grounding: concern. Targets: antibioticmech:aro-832bfb6c2e.

ARO and CID16131332 resolve faithfully, and formula, neutral charge, masses and mint reproduce. Their agreement preserves the same two-centre omission. A curator must resolve the exact stereodefined graph and its chemical xref together; replacing it with a guessed CID or asserting that this current CID already encodes the full candidate would be incorrect.

### Synthetic analog wording and typography

evidence: concern. Targets: antibioticmech:aro-832bfb6c2e.

Synthetic analog status is supported. The originals specifically describe a magainin-2-based modification; the broader native analog-of-magainin 1 wording is less precise but is not independently proved chemically false, since the sequences are related. The repeated is is is a confirmed source-owned typo.

### Exact B activity with material and endpoint boundaries

evidence: supported. Targets: antibioticmech:aro-832bfb6c2e.

The inventor original gives exact B antibacterial growth endpoints, while the adopted 1990 paper supplies protozoal morphology/motility experiments for synthesized B. The biological preparation follows the declared ordinary-Ile sequence; its results should not be represented as evidence for every completion of the native partial graph. No other analog, host-cell kinase result or clinical efficacy is substituted.

### No molecular target inferred from permeability or host kinase data

evidence: unknown. Targets: antibioticmech:aro-832bfb6c2e.

The native has no molecular-target assertion. The adopted original leaves the detailed protozoal mechanism unresolved; observed membrane injury and helix correlation do not establish a unique bacterial protein target. The PKC original is explicitly separate host biochemistry.

### Optional enrichment and bounded reading depth

completeness: unknown. Targets: antibioticmech:aro-832bfb6c2e.

Missing optional structured activity, resistance, producer and causal graph fields are not flaws. The sole adopted citation was fully read from original scans, including methods and sequence; additional papers remain abstract-level comparators with explicit access limits. No native quotation snippet requires correction.

### Whole native and actual owner audit

provenance: supported. Targets: antibioticmech:aro-832bfb6c2e.

All native fields and three history entries were read. Exact source rows, current authorities and independent residue mapping distinguish source fidelity from scientific completeness. Original 13 and expanded 21 hashes remain unchanged.

## Findings

### F1: The exact peptide graph omits both isoleucine side-chain configurations

major / open / confirmed; issue key: magainin-b-ile2-ile20-beta-stereo-unspecified.

Native SMILES atoms 2 and 141 and corresponding InChI positions 65/66 are unspecified beta stereocentres of Ile2/Ile20. Original B sequences retain ordinary Ile at both positions and separately identify intentional D-residue modifications in H. A full L-Ile sequence gives KKNMJWFWBZQVFT-JHWRQTFCSA-N; clearing only those two beta assignments reproduces the native graph. Current CID16131332 shares the omission. Resolve the exact peptide structure and grounding together, without treating unspecified stereo as a racemate, an opposite configuration or experimental evidence of batch heterogeneity.

### F2: The source-owned definition repeats is

minor / open / confirmed; issue key: magainin-b-definition-duplicated-is.

The native and current ARO definition both contain is is. Remove the duplicate through maintained source text handling; the synthetic-analog meaning is otherwise retained.

## Recommended Actions And Acceptance Checks

### A1

Resolve and preserve the full ordinary-Ile synthetic B identity through maintained molecular grounding.

- Document the primary 23-residue B sequence, terminal amide and residue-to-atom mapping; verify both Ile beta centres as part of exact structure adjudication.
- Use the full candidate only after curator adjudication and verify all stereocentres, formula, mass and identifier generation; no empirical chiral-purity claim is implied.
- Do not retain CID16131332 as an unqualified exact full-graph equivalent unless the authority encoding is corrected; resolve or qualify the exact chemical xref through maintained support.
- Regenerate and run focused, reproduction and required shared checks.

### A2

Remove the duplicated word in maintained ARO definition handling and regenerate.

- Correct is is to is while preserving source provenance.
- If the definition is rewritten for precision, use the primary-described magainin-2 analog and verified modifications; do not invent a natural producer.
- Run focused and required shared validation after regeneration.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/magainin-b.yaml; Entire native record and all three history events | supports | The native ARO-derived record describes a synthetic analog, declares a peptide-antibiotic class, and imports a neutral PubChem graph with 21 defined and two undefined stereocentres. It has two xrefs and no synonyms, document xrefs or drug-level xrefs. The definition is the only activity statement; no separate structured targets, resistance, activity spectrum, producer, product or causal graph objects are asserted. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; curation/record_review_queue.tsv; Exact ARO row262, PubChem row87 and readiness subset | context_only | ARO owns the identity definition/citation and PubChem owns the graph. Original 13 input hashes were retained and actual owner/context capture expanded to21 before assessment. All generator paths were checked against real files. |
| local | /private/tmp/am-review-session/625-context-search.txt; Hidden- and ignored-inclusive exact identity/family search | context_only | The bounded search inspected native identifiers, the family name and key prefix across source, curation, configuration, script and report directories, with the initial search retained. The native typo and partial graph reproduce their adopted source rows. |
| adapter | /private/tmp/am-review-session/625-adapter-scope.json; Pre-research applicability assessment | context_only | The complete native record has no named protein, gene or pathway assertion. The magainin relationship is a peptide-identity claim. No structured protein/pathway query is applicable and no adapter result is implied. |
| aro | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3003568; Current ARO3003568 identity term | partial | The current source retains the same synthetic-analog definition, duplicated is, PMID2285300 and exact PubChem accession. This confirms provenance, not the completeness of PubChem stereochemistry. |
| parent | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3000053; Current ARO3000053 peptide-antibiotic definition | supports | The native graph is a peptide and exact synthetic B has antibacterial activity in the original inventor table. The parent is appropriate. Generic class mechanisms are not assigned as a specific B target. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/16131332/property/MolecularFormula,MolecularWeight,IsomericSMILES,InChI,InChIKey,MonoisotopicMass,Charge/JSON; Asserted CID16131332 structure properties | partial | The current authority reproduces the native C116H185N31O27S composition, neutral charge, KKNMJWFWBZQVFT-FIHNEYJFSA-N key and mass values. Its InChI explicitly has two unspecified tetrahedral centres. The xref faithfully identifies this partial graph; the concern is its use to represent the exact named peptide. |
| pubchem-notation | https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/16131332/JSON; Biologic line notation and depositor names | partial | The generated biologic notation explicitly labels positions 2/20 as xiIle and the IUPAC sequence as (3xi)-L-isoleucyl. Some depositor names instead use ordinary L-isoleucyl. The parsed graph, not the name alone, determines the actual level of stereo specification. |
| chemistry | /private/tmp/am-review-session/625-authority-chemistry.json; Four native/current encodings, independently assembled primary sequence and atom/residue mapping | supports | Native SMILES/InChI and current PubChem SMILES/InChI all give 21 assigned and two unassigned centres. The unknowns are native SMILES atoms 2/141, mapped to Ile2/Ile20 beta carbons; alpha atoms 4/140 are both S. Constructing the ordinary L-residue primary sequence with terminal amide gives KKNMJWFWBZQVFT-JHWRQTFCSA-N, with both beta carbons S. Removing only those two candidate assignments reproduces the native key and reciprocal chirality-aware graph matches. No opposite configuration or racemic material is inferred. |
| adopted-sequence | PMID:2285300; DOI:10.1128/AAC.34.9.1824; https://pmc.ncbi.nlm.nih.gov/articles/PMC171939/; Entire original pp1824–1826, including sequence block and synthesis methods; actual scans inspected | supports | The paper explicitly synthesizes B/G/H by solid-phase methods with preparative reverse-phase HPLC purification. B is GIGKFLHAAKKFAKAFVAEIMNS-NH2, with ordinary I at positions 2/20. D-alanine is separately denoted in H. The exact B sequence and synthetic production are directly supported; the paper does not describe a beta-epimer mixture or replace either Ile with allo-Ile. It does not provide an independent batch-level chiral-purity measurement. |
| adopted-assay | PMID:2285300; DOI:10.1128/AAC.34.9.1824; Original p1824 methods/results and p1826 discussion | partial | B was tested against axenic Blastocystis hominis NAND, Entamoeba histolytica 200 NIH clone and Trypanosoma cruzi 2380-260. Peptides in isotonic saline were applied at 50,100,200,500 micrograms/mL, with time-dependent morphology/motility observations. B caused rapid damage at high concentrations; regrowth assessment for B. hominis after exposure is separate from a standardized MBC. These protozoal results are not bacterial MICs or demonstrated in-vivo treatment efficacy. |
| adopted-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3953/171939/e5211ed7d174/aac00065-0227.png; Actual Figure 1 image and full caption on p1825 | partial | The image panels were opened but are extremely dark; detailed cell morphology cannot be independently resolved. The caption explicitly identifies B concentration conditions and controls. Caption claims are retained separately from visual confirmation of individual membrane changes. |
| adopted-discussion | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3953/171939/11e3ee60a5fc/aac00065-0228.png; Original p1826, full discussion and references | partial | The authors link the observed cell leakage with injury but explicitly leave the detailed antiprotozoal mechanism unresolved and call for in-vivo investigation. Their helix-content comparison is not a measured protein-binding target. |
| patent-sequence | https://patents.google.com/patent/US5221732A/en; Original PDF p5 Table 1, synthesis and p7 claim 6; actual Table 1 inspected | supports | The inventors define B as the Ala8,13,18 magainin-2 amide and spell out its sequence in claim 6. Ordinary Ile is retained at 2/20; D-Ala is explicitly a different analog modification. The synthetic products underwent chromatographic purification with reported HPLC purity greater than 93%. This supplies sequence-level identity, not an independent stereochemical-purity measurement for every batch. |
| patent-activity | https://patentimages.storage.googleapis.com/21/09/ae/d05ea212075f40/US5221732.pdf; Original PDF p6 Table 3 columnB and complete adjacent methods; actual table inspected | partial | B has 100% growth-inhibition endpoints 2.5,10,25,1,10,10,10 micrograms/mL against E. coli 25922, K. pneumoniae 13883, P. aeruginosa 27853, S. agalactiae 12386, historical S. faecalis 29212 and S. aureus 29213/25923. The assay uses trypticase soy broth, 10^5/10^6 CFU/mL inocula, 35 °C and 6–9 h OD600 readout. The paired 50% column values are separate endpoints. Per-row inoculum assignment and counterion stoichiometry are not specified. |
| pkc-original | PMID:2365080; DOI:10.1016/0014-5793(90)80307-5; Complete original abstract only | context_only | The paper explicitly defines B as the Ser8/Gly13/Gly18-to-Ala synthetic analog of magainin-2 amide. Its PKC isozyme and phorbol-binding observations concern a host biochemical context and do not establish the antibacterial mechanism. The full original methods were not recovered and no B protein target is proposed here. |
| lead-3410055 | PMID:3410055; Additional comparator abstract; no full-table claim | context_only | The 1988 analog synthesis paper reports enhanced antimicrobial activity, but its full sequence/activity tables were inaccessible. The inventor original supplies an independently inspected B table. |
| lead-2544449 | PMID:2544449; Additional comparator abstract; no full-table claim | context_only | The 1989 E. coli membrane study names A in its complete abstract; A is a distinct beta-alanine analog, so its quantitative results are not transferred to B. |
| lead-1708887 | PMID:1708887; Additional comparator abstract; no full-table claim | context_only | The 1991 transformed-cell cytolysis study is host-cell context and its abstract does not resolve exact B antibacterial results. |
| lead-3277183 | PMID:3277183; Additional comparator abstract; no full-table claim | context_only | The 1988 natural-sequence synthetic peptide comparison does not make the modified B a naturally isolated compound. |
| lead-3299384 | PMID:3299384; Additional comparator abstract; no full-table claim | context_only | The 1987 isolation paper provides natural magainin-family context, not isolation of B. |
| lead-2980783 | PMID:2980783; Additional comparator abstract; no full-table claim | context_only | The 1988 omission-analog series has only a database-truncated abstract; its results are not transferred to B. |
| access | /private/tmp/am-review-session/624-fetch2.json; /private/tmp/am-review-session/624-fetch4.json; /private/tmp/am-review-session/624-fetch5.json; Shared same-day original retrieval and bounded discovery record | context_only | The adopted original was fully read as three available page scans despite failed XML/PDF routes. The 1988/1989 full publisher attempts returned 403. Discovery screened the first 100 titles of a363-hit refined historical query and selected exact primary routes, not all family publications. Same-day existing source hashes and access timestamps are retained without pretending they were newly retrieved for B. |

## Limits And Additional Notes

- The original sequence/synthesis identifies ordinary Ile but the inspected sources do not independently quantify beta-epimer purity of each peptide batch. The finding concerns the named exact sequence, not an inferred mixture or measured impurity.
- The adopted original was fully read from three scan pages. Figure 1 panels are very dark, so caption statements are not presented as independently resolved cellular morphology.
- The 1988/1989 full originals were inaccessible through attempted publisher routes; additional historical comparators were read only as complete or explicitly truncated abstracts.
- Patent antibacterial values use a preparation-specific modified macrodilution method. Counterion stoichiometry, row-specific allocation of the two inoculum densities and clinical breakpoint relevance remain unspecified.
- Discovery was bounded to the first 100 refined titles and selected exact sources; no exhaustive family-literature claim is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Original 13 and expanded 21 input hashes remain unchanged; no native, source or history data were edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T202611Z-magainin-b-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Magainin B: two unspecified isoleucine centres and a source definition typo'
started_at: '2026-10-21T20:11:20Z'
finished_at: '2026-10-21T20:26:11Z'
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
summary: The whole native record and actual ARO/PubChem source rows were reviewed.
  The stored graph and current PubChem agree, but both leave Ile2 and Ile20 side-chain
  stereochemistry unspecified. Original synthetic peptide sequences identify ordinary
  isoleucine at those positions; an independently constructed sequence differs only
  by these two assignments. Exact B antibacterial and protozoal evidence is available
  with bounded preparation and endpoint scope. The source definition also repeats
  the word is.
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
  - path: data/antibiotics/antibacterial/magainin-b.yaml
    sha256: f21f3cd34a2437a2c8a7da5c9e6db0a800160eadfa8feaf3c12519433a4a0d2c
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
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
targets:
- target_id: antibioticmech:aro-832bfb6c2e
  path: data/antibiotics/antibacterial/magainin-b.yaml
  label: magainin B
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition and citation
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact PubChem graph
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Assigned queue position 625; one exact native record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-832bfb6c2e
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0. Actual 063 cwd; chemistry used 019 RDKit
    and schema/strict used 063 environment. Passing syntax/internal consistency does
    not resolve missing peptide stereo.
  target_ids:
  - antibioticmech:aro-832bfb6c2e
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    625
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Actual 063 cwd; chemistry used 019 RDKit
    and schema/strict used 063 environment. Passing syntax/internal consistency does
    not resolve missing peptide stereo.
  target_ids:
  - antibioticmech:aro-832bfb6c2e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/magainin-b.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Actual 063 cwd; chemistry used 019 RDKit
    and schema/strict used 063 environment. Passing syntax/internal consistency does
    not resolve missing peptide stereo.
  target_ids:
  - antibioticmech:aro-832bfb6c2e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/magainin-b.yaml --out /private/tmp/am-review-session/625-strict.tsv
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
  - antibioticmech:aro-832bfb6c2e
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
  - antibioticmech:aro-832bfb6c2e
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
  - antibioticmech:aro-832bfb6c2e
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
  - antibioticmech:aro-832bfb6c2e
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
  - antibioticmech:aro-832bfb6c2e
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
  - antibioticmech:aro-832bfb6c2e
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
  - antibioticmech:aro-832bfb6c2e
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
  - antibioticmech:aro-832bfb6c2e
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
  - antibioticmech:aro-832bfb6c2e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/magainin-b.yaml
  locator: Entire native record and all three history events
  accessed_at: '2026-10-21T20:24:57Z'
  support: supports
  summary: The native ARO-derived record describes a synthetic analog, declares a
    peptide-antibiotic class, and imports a neutral PubChem graph with 21 defined
    and two undefined stereocentres. It has two xrefs and no synonyms, document xrefs
    or drug-level xrefs. The definition is the only activity statement; no separate
    structured targets, resistance, activity spectrum, producer, product or causal
    graph objects are asserted.
  snapshot_sha256: f21f3cd34a2437a2c8a7da5c9e6db0a800160eadfa8feaf3c12519433a4a0d2c
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; curation/record_review_queue.tsv
  locator: Exact ARO row262, PubChem row87 and readiness subset
  accessed_at: '2026-10-21T20:24:57Z'
  support: context_only
  summary: ARO owns the identity definition/citation and PubChem owns the graph. Original
    13 input hashes were retained and actual owner/context capture expanded to21 before
    assessment. All generator paths were checked against real files.
  snapshot_sha256: ab9d2fca71d36b957d47e557d0932bf138916d1104c32be0ac6c0b8daf891a4d
- evidence_id: local
  kind: search
  reference: /private/tmp/am-review-session/625-context-search.txt
  locator: Hidden- and ignored-inclusive exact identity/family search
  accessed_at: '2026-10-21T20:24:57Z'
  support: context_only
  summary: The bounded search inspected native identifiers, the family name and key
    prefix across source, curation, configuration, script and report directories,
    with the initial search retained. The native typo and partial graph reproduce
    their adopted source rows.
  snapshot_sha256: d4ff503c7694b91e6471735af3907ef42a3357ba11a281141fe8ea47690e52b9
  search_scope: rg --no-ignore --hidden -n -i magainin|ARO:3003568|KKNMJWFWBZQVFT
    in data/raw, curation, conf, scripts and reports, plus initial local hits.
- evidence_id: adapter
  kind: search
  reference: /private/tmp/am-review-session/625-adapter-scope.json
  locator: Pre-research applicability assessment
  accessed_at: '2026-10-21T20:24:57Z'
  support: context_only
  summary: The complete native record has no named protein, gene or pathway assertion.
    The magainin relationship is a peptide-identity claim. No structured protein/pathway
    query is applicable and no adapter result is implied.
  snapshot_sha256: da44f3aa2f5c25be82b89f840019ac87afb4250057ff7bd35813d1dd52a7c5bb
  search_scope: Entire native field inventory and definition checked before open-ended
    follow-up.
- evidence_id: aro
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3003568
  locator: Current ARO3003568 identity term
  accessed_at: '2026-10-21T20:23:21.190976Z'
  support: partial
  summary: The current source retains the same synthetic-analog definition, duplicated
    is, PMID2285300 and exact PubChem accession. This confirms provenance, not the
    completeness of PubChem stereochemistry.
  snapshot_sha256: f74e1aaa8b47c10f82d82f81473ac36f0a176538238f4e9c92448104e78b8252
- evidence_id: parent
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3000053
  locator: Current ARO3000053 peptide-antibiotic definition
  accessed_at: '2026-10-21T20:18:39.284501Z'
  support: supports
  summary: The native graph is a peptide and exact synthetic B has antibacterial activity
    in the original inventor table. The parent is appropriate. Generic class mechanisms
    are not assigned as a specific B target.
  snapshot_sha256: b6ab78fcd5c01625148a14ecb461eb0b963eaf49e1c5992b9b06ea601f8cb57c
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/16131332/property/MolecularFormula,MolecularWeight,IsomericSMILES,InChI,InChIKey,MonoisotopicMass,Charge/JSON
  locator: Asserted CID16131332 structure properties
  accessed_at: '2026-10-21T20:23:21.190548Z'
  support: partial
  summary: The current authority reproduces the native C116H185N31O27S composition,
    neutral charge, KKNMJWFWBZQVFT-FIHNEYJFSA-N key and mass values. Its InChI explicitly
    has two unspecified tetrahedral centres. The xref faithfully identifies this partial
    graph; the concern is its use to represent the exact named peptide.
  snapshot_sha256: 253df80c30b41f3e4061b261aed68e56945c6e41136e807c6eeda14913ffcddd
- evidence_id: pubchem-notation
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/16131332/JSON
  locator: Biologic line notation and depositor names
  accessed_at: '2026-10-21T20:23:21.190889Z'
  support: partial
  summary: The generated biologic notation explicitly labels positions 2/20 as xiIle
    and the IUPAC sequence as (3xi)-L-isoleucyl. Some depositor names instead use
    ordinary L-isoleucyl. The parsed graph, not the name alone, determines the actual
    level of stereo specification.
  snapshot_sha256: 05348badfcbf51bf87a6760f95128ad4abf8cbefc24894c1ced8b976092fc4be
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/am-review-session/625-authority-chemistry.json
  locator: Four native/current encodings, independently assembled primary sequence
    and atom/residue mapping
  accessed_at: '2026-10-21T20:24:57Z'
  support: supports
  summary: Native SMILES/InChI and current PubChem SMILES/InChI all give 21 assigned
    and two unassigned centres. The unknowns are native SMILES atoms 2/141, mapped
    to Ile2/Ile20 beta carbons; alpha atoms 4/140 are both S. Constructing the ordinary
    L-residue primary sequence with terminal amide gives KKNMJWFWBZQVFT-JHWRQTFCSA-N,
    with both beta carbons S. Removing only those two candidate assignments reproduces
    the native key and reciprocal chirality-aware graph matches. No opposite configuration
    or racemic material is inferred.
  snapshot_sha256: 3660cf7bb51cd941fb4886562d586e06c9498809665700496f0cb54d62976eb4
- evidence_id: adopted-sequence
  kind: primary_source
  reference: PMID:2285300; DOI:10.1128/AAC.34.9.1824; https://pmc.ncbi.nlm.nih.gov/articles/PMC171939/
  locator: Entire original pp1824–1826, including sequence block and synthesis methods;
    actual scans inspected
  accessed_at: '2026-10-21T20:20:30.883022Z'
  support: supports
  summary: The paper explicitly synthesizes B/G/H by solid-phase methods with preparative
    reverse-phase HPLC purification. B is GIGKFLHAAKKFAKAFVAEIMNS-NH2, with ordinary
    I at positions 2/20. D-alanine is separately denoted in H. The exact B sequence
    and synthetic production are directly supported; the paper does not describe a
    beta-epimer mixture or replace either Ile with allo-Ile. It does not provide an
    independent batch-level chiral-purity measurement.
  snapshot_sha256: 5ccd1346bfff1e5ea1d5cf3336cac8fcdac637120f5e66f38d5a0af0acf4169e
- evidence_id: adopted-assay
  kind: primary_source
  reference: PMID:2285300; DOI:10.1128/AAC.34.9.1824
  locator: Original p1824 methods/results and p1826 discussion
  accessed_at: '2026-10-21T20:20:30.883022Z'
  support: partial
  summary: B was tested against axenic Blastocystis hominis NAND, Entamoeba histolytica
    200 NIH clone and Trypanosoma cruzi 2380-260. Peptides in isotonic saline were
    applied at 50,100,200,500 micrograms/mL, with time-dependent morphology/motility
    observations. B caused rapid damage at high concentrations; regrowth assessment
    for B. hominis after exposure is separate from a standardized MBC. These protozoal
    results are not bacterial MICs or demonstrated in-vivo treatment efficacy.
  snapshot_sha256: 5ccd1346bfff1e5ea1d5cf3336cac8fcdac637120f5e66f38d5a0af0acf4169e
- evidence_id: adopted-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3953/171939/e5211ed7d174/aac00065-0227.png
  locator: Actual Figure 1 image and full caption on p1825
  accessed_at: '2026-10-21T20:20:30.886937Z'
  support: partial
  summary: The image panels were opened but are extremely dark; detailed cell morphology
    cannot be independently resolved. The caption explicitly identifies B concentration
    conditions and controls. Caption claims are retained separately from visual confirmation
    of individual membrane changes.
  snapshot_sha256: 7788ae01e9559f71a153d22d1dbd3739ac1a55c7f7e69391eaba7c2846d57d17
- evidence_id: adopted-discussion
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3953/171939/11e3ee60a5fc/aac00065-0228.png
  locator: Original p1826, full discussion and references
  accessed_at: '2026-10-21T20:20:30.887650Z'
  support: partial
  summary: The authors link the observed cell leakage with injury but explicitly leave
    the detailed antiprotozoal mechanism unresolved and call for in-vivo investigation.
    Their helix-content comparison is not a measured protein-binding target.
  snapshot_sha256: c6de8efe500b20b4733fbece80900e1255c3a05618f1f74464cd8240b35ef14e
- evidence_id: patent-sequence
  kind: primary_source
  reference: https://patents.google.com/patent/US5221732A/en
  locator: Original PDF p5 Table 1, synthesis and p7 claim 6; actual Table 1 inspected
  accessed_at: '2026-10-21T20:21:03.126743Z'
  support: supports
  summary: The inventors define B as the Ala8,13,18 magainin-2 amide and spell out
    its sequence in claim 6. Ordinary Ile is retained at 2/20; D-Ala is explicitly
    a different analog modification. The synthetic products underwent chromatographic
    purification with reported HPLC purity greater than 93%. This supplies sequence-level
    identity, not an independent stereochemical-purity measurement for every batch.
  snapshot_sha256: b11506108b20c42700706e1f269707a7831df446edd3c478560c1cf37debd634
- evidence_id: patent-activity
  kind: primary_source
  reference: https://patentimages.storage.googleapis.com/21/09/ae/d05ea212075f40/US5221732.pdf
  locator: Original PDF p6 Table 3 columnB and complete adjacent methods; actual table
    inspected
  accessed_at: '2026-10-21T20:21:03.126743Z'
  support: partial
  summary: B has 100% growth-inhibition endpoints 2.5,10,25,1,10,10,10 micrograms/mL
    against E. coli 25922, K. pneumoniae 13883, P. aeruginosa 27853, S. agalactiae
    12386, historical S. faecalis 29212 and S. aureus 29213/25923. The assay uses
    trypticase soy broth, 10^5/10^6 CFU/mL inocula, 35 °C and 6–9 h OD600 readout.
    The paired 50% column values are separate endpoints. Per-row inoculum assignment
    and counterion stoichiometry are not specified.
  snapshot_sha256: b11506108b20c42700706e1f269707a7831df446edd3c478560c1cf37debd634
- evidence_id: pkc-original
  kind: primary_source
  reference: PMID:2365080; DOI:10.1016/0014-5793(90)80307-5
  locator: Complete original abstract only
  accessed_at: '2026-10-21T20:20:30.893866Z'
  support: context_only
  summary: The paper explicitly defines B as the Ser8/Gly13/Gly18-to-Ala synthetic
    analog of magainin-2 amide. Its PKC isozyme and phorbol-binding observations concern
    a host biochemical context and do not establish the antibacterial mechanism. The
    full original methods were not recovered and no B protein target is proposed here.
  snapshot_sha256: 7eb080614c0abb58fdbe086c3e0f4577bcfcaf8a6220dce0645bf5412011d746
- evidence_id: lead-3410055
  kind: primary_source
  reference: PMID:3410055
  locator: Additional comparator abstract; no full-table claim
  accessed_at: '2026-10-21T20:20:30.893866Z'
  support: context_only
  summary: The 1988 analog synthesis paper reports enhanced antimicrobial activity,
    but its full sequence/activity tables were inaccessible. The inventor original
    supplies an independently inspected B table.
  snapshot_sha256: 7eb080614c0abb58fdbe086c3e0f4577bcfcaf8a6220dce0645bf5412011d746
- evidence_id: lead-2544449
  kind: primary_source
  reference: PMID:2544449
  locator: Additional comparator abstract; no full-table claim
  accessed_at: '2026-10-21T20:20:30.893866Z'
  support: context_only
  summary: The 1989 E. coli membrane study names A in its complete abstract; A is
    a distinct beta-alanine analog, so its quantitative results are not transferred
    to B.
  snapshot_sha256: 7eb080614c0abb58fdbe086c3e0f4577bcfcaf8a6220dce0645bf5412011d746
- evidence_id: lead-1708887
  kind: primary_source
  reference: PMID:1708887
  locator: Additional comparator abstract; no full-table claim
  accessed_at: '2026-10-21T20:20:30.893866Z'
  support: context_only
  summary: The 1991 transformed-cell cytolysis study is host-cell context and its
    abstract does not resolve exact B antibacterial results.
  snapshot_sha256: 7eb080614c0abb58fdbe086c3e0f4577bcfcaf8a6220dce0645bf5412011d746
- evidence_id: lead-3277183
  kind: primary_source
  reference: PMID:3277183
  locator: Additional comparator abstract; no full-table claim
  accessed_at: '2026-10-21T20:20:30.893866Z'
  support: context_only
  summary: The 1988 natural-sequence synthetic peptide comparison does not make the
    modified B a naturally isolated compound.
  snapshot_sha256: 7eb080614c0abb58fdbe086c3e0f4577bcfcaf8a6220dce0645bf5412011d746
- evidence_id: lead-3299384
  kind: primary_source
  reference: PMID:3299384
  locator: Additional comparator abstract; no full-table claim
  accessed_at: '2026-10-21T20:20:30.893866Z'
  support: context_only
  summary: The 1987 isolation paper provides natural magainin-family context, not
    isolation of B.
  snapshot_sha256: 7eb080614c0abb58fdbe086c3e0f4577bcfcaf8a6220dce0645bf5412011d746
- evidence_id: lead-2980783
  kind: primary_source
  reference: PMID:2980783
  locator: Additional comparator abstract; no full-table claim
  accessed_at: '2026-10-21T20:20:30.893866Z'
  support: context_only
  summary: The 1988 omission-analog series has only a database-truncated abstract;
    its results are not transferred to B.
  snapshot_sha256: 7eb080614c0abb58fdbe086c3e0f4577bcfcaf8a6220dce0645bf5412011d746
- evidence_id: access
  kind: search
  reference: /private/tmp/am-review-session/624-fetch2.json; /private/tmp/am-review-session/624-fetch4.json;
    /private/tmp/am-review-session/624-fetch5.json
  locator: Shared same-day original retrieval and bounded discovery record
  accessed_at: '2026-10-21T20:24:57Z'
  support: context_only
  summary: The adopted original was fully read as three available page scans despite
    failed XML/PDF routes. The 1988/1989 full publisher attempts returned 403. Discovery
    screened the first 100 titles of a363-hit refined historical query and selected
    exact primary routes, not all family publications. Same-day existing source hashes
    and access timestamps are retained without pretending they were newly retrieved
    for B.
  snapshot_sha256: dcf001b4ccd14836530c5d5c44f2a454be773fd6a9a55ccafb4f1f521b3e8847
  search_scope: Historical magainin AND (beta-alanine OR magainin A OR magainin B),1987–1995,
    first100 titles; selected exact PMID/DOI and inventor patent routes. No exhaustive
    review of363 results.
assessments:
- assessment_id: identity
  area: identity
  topic: Sequence and unresolved Ile side-chain stereo
  outcome: concern
  summary: The peptide connectivity, all 21 alpha centres and terminal amide match
    the synthetic B sequence. The native and its PubChem source omit the two beta
    configurations of ordinary Ile2/Ile20. This is an incomplete exact molecular description,
    not evidence of a mixed or opposite-stereoisomer preparation. Primary sequence
    convention identifies ordinary Ile; batch-level chiral purity was not independently
    measured in the inspected material.
  target_ids:
  - antibioticmech:aro-832bfb6c2e
  evidence_ids:
  - native
  - pubchem
  - pubchem-notation
  - chemistry
  - adopted-sequence
  - patent-sequence
- assessment_id: grounding
  area: grounding
  topic: Source agreement versus exact peptide completeness
  outcome: concern
  summary: ARO and CID16131332 resolve faithfully, and formula, neutral charge, masses
    and mint reproduce. Their agreement preserves the same two-centre omission. A
    curator must resolve the exact stereodefined graph and its chemical xref together;
    replacing it with a guessed CID or asserting that this current CID already encodes
    the full candidate would be incorrect.
  target_ids:
  - antibioticmech:aro-832bfb6c2e
  evidence_ids:
  - aro
  - pubchem
  - chemistry
- assessment_id: definition
  area: evidence
  topic: Synthetic analog wording and typography
  outcome: concern
  summary: Synthetic analog status is supported. The originals specifically describe
    a magainin-2-based modification; the broader native analog-of-magainin 1 wording
    is less precise but is not independently proved chemically false, since the sequences
    are related. The repeated is is is a confirmed source-owned typo.
  target_ids:
  - antibioticmech:aro-832bfb6c2e
  evidence_ids:
  - native
  - aro
  - adopted-sequence
  - patent-sequence
  - pkc-original
- assessment_id: activity
  area: evidence
  topic: Exact B activity with material and endpoint boundaries
  outcome: supported
  summary: The inventor original gives exact B antibacterial growth endpoints, while
    the adopted 1990 paper supplies protozoal morphology/motility experiments for
    synthesized B. The biological preparation follows the declared ordinary-Ile sequence;
    its results should not be represented as evidence for every completion of the
    native partial graph. No other analog, host-cell kinase result or clinical efficacy
    is substituted.
  target_ids:
  - antibioticmech:aro-832bfb6c2e
  evidence_ids:
  - patent-activity
  - adopted-assay
  - adopted-figure
  - adopted-discussion
- assessment_id: mechanism
  area: evidence
  topic: No molecular target inferred from permeability or host kinase data
  outcome: unknown
  summary: The native has no molecular-target assertion. The adopted original leaves
    the detailed protozoal mechanism unresolved; observed membrane injury and helix
    correlation do not establish a unique bacterial protein target. The PKC original
    is explicitly separate host biochemistry.
  target_ids:
  - antibioticmech:aro-832bfb6c2e
  evidence_ids:
  - native
  - adopted-discussion
  - pkc-original
  - adapter
- assessment_id: completeness
  area: completeness
  topic: Optional enrichment and bounded reading depth
  outcome: unknown
  summary: Missing optional structured activity, resistance, producer and causal graph
    fields are not flaws. The sole adopted citation was fully read from original scans,
    including methods and sequence; additional papers remain abstract-level comparators
    with explicit access limits. No native quotation snippet requires correction.
  target_ids:
  - antibioticmech:aro-832bfb6c2e
  evidence_ids:
  - native
  - adopted-sequence
  - access
- assessment_id: provenance
  area: provenance
  topic: Whole native and actual owner audit
  outcome: supported
  summary: All native fields and three history entries were read. Exact source rows,
    current authorities and independent residue mapping distinguish source fidelity
    from scientific completeness. Original 13 and expanded 21 hashes remain unchanged.
  target_ids:
  - antibioticmech:aro-832bfb6c2e
  evidence_ids:
  - native
  - owners
  - local
  - aro
  - chemistry
findings:
- finding_id: F1
  issue_key: magainin-b-ile2-ile20-beta-stereo-unspecified
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The exact peptide graph omits both isoleucine side-chain configurations
  description: Native SMILES atoms 2 and 141 and corresponding InChI positions 65/66
    are unspecified beta stereocentres of Ile2/Ile20. Original B sequences retain
    ordinary Ile at both positions and separately identify intentional D-residue modifications
    in H. A full L-Ile sequence gives KKNMJWFWBZQVFT-JHWRQTFCSA-N; clearing only those
    two beta assignments reproduces the native graph. Current CID16131332 shares the
    omission. Resolve the exact peptide structure and grounding together, without
    treating unspecified stereo as a racemate, an opposite configuration or experimental
    evidence of batch heterogeneity.
  target_ids:
  - antibioticmech:aro-832bfb6c2e
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  - xrefs[1]
  evidence_ids:
  - native
  - pubchem
  - pubchem-notation
  - chemistry
  - adopted-sequence
  - patent-sequence
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted molecular graph
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted exact PubChem association
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated structure and xref owner
  rule_id: 'review-yaml-record: exact compound identity and stereochemistry'
  normalization_reason: Major under-specification of two defined amino-acid centres.
    No opposite stereoisomer is affirmatively encoded, so the finding is not normalized
    as a wrong-stereoisomer blocker.
- finding_id: F2
  issue_key: magainin-b-definition-duplicated-is
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The source-owned definition repeats is
  description: The native and current ARO definition both contain is is. Remove the
    duplicate through maintained source text handling; the synthetic-analog meaning
    is otherwise retained.
  target_ids:
  - antibioticmech:aro-832bfb6c2e
  field_paths:
  - definition
  evidence_ids:
  - native
  - aro
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition owner
  rule_id: 'review-yaml-record: readable source-owned definition'
  normalization_reason: Minor reproducible text defect without an independent change
    to chemical identity or activity.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-832bfb6c2e
  description: Resolve and preserve the full ordinary-Ile synthetic B identity through
    maintained molecular grounding.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted molecular graph
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted exact PubChem association
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated structure and xref owner
  generator: scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py
  acceptance_checks:
  - Document the primary 23-residue B sequence, terminal amide and residue-to-atom
    mapping; verify both Ile beta centres as part of exact structure adjudication.
  - Use the full candidate only after curator adjudication and verify all stereocentres,
    formula, mass and identifier generation; no empirical chiral-purity claim is implied.
  - Do not retain CID16131332 as an unqualified exact full-graph equivalent unless
    the authority encoding is corrected; resolve or qualify the exact chemical xref
    through maintained support.
  - Regenerate and run focused, reproduction and required shared checks.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-832bfb6c2e
  description: Remove the duplicated word in maintained ARO definition handling and
    regenerate.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition owner
  generator: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  acceptance_checks:
  - Correct is is to is while preserving source provenance.
  - If the definition is rewritten for precision, use the primary-described magainin-2
    analog and verified modifications; do not invent a natural producer.
  - Run focused and required shared validation after regeneration.
limitations:
- The original sequence/synthesis identifies ordinary Ile but the inspected sources
  do not independently quantify beta-epimer purity of each peptide batch. The finding
  concerns the named exact sequence, not an inferred mixture or measured impurity.
- The adopted original was fully read from three scan pages. Figure 1 panels are very
  dark, so caption statements are not presented as independently resolved cellular
  morphology.
- The 1988/1989 full originals were inaccessible through attempted publisher routes;
  additional historical comparators were read only as complete or explicitly truncated
  abstracts.
- Patent antibacterial values use a preparation-specific modified macrodilution method.
  Counterion stoichiometry, row-specific allocation of the two inoculum densities
  and clinical breakpoint relevance remain unspecified.
- Discovery was bounded to the first 100 refined titles and selected exact sources;
  no exhaustive family-literature claim is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Original 13 and expanded 21 input hashes remain unchanged; no native, source or
  history data were edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
