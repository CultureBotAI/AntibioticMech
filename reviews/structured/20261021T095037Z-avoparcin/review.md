# Avoparcin: conflicting congener assignment and historical definition scope

- Review: 20261021T095037Z-avoparcin
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:28:15Z
- Finished UTC: 2026-10-21T09:50:37Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One major source/congener identity conflict and one minor historical definition/citation finding. Internal chemistry and both focused validators pass. The database-only chemical-target representation is appropriately cautious; exact primary evidence transfer remains unresolved.

## Scope And Provenance

Whole-record scientific review of the single minted avoparcin record.

Selection: Queue129 in isolated batch013.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-9aee56c696 | data/antibiotics/antibacterial/avoparcin.yaml | generated | avoparcin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | antibioticmech:aro-9aee56c696 | Actual command passed. |
| Focused strict | passed | True | antibioticmech:aro-9aee56c696 | Actual command passed. |
| Internal chemical consistency and source mint | passed | True | antibioticmech:aro-9aee56c696 | Both native encodings and ARO mint agree; exact congener mapping remains unresolved. |
| Authoritative full QC | failed | True | antibioticmech:aro-9aee56c696 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-9aee56c696 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-9aee56c696 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-9aee56c696 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-9aee56c696 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-9aee56c696 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-9aee56c696 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-9aee56c696 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-9aee56c696 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Generic mixture and conflicting alpha structures

identity: concern. Targets: antibioticmech:aro-9aee56c696.

The native structure is internally coherent, but its alpha name mapping conflicts with independent congener composition evidence. Source identity needs adjudication before exact assay transfer.

### Encodings,charge,masses and mint

identity: supported. Targets: antibioticmech:aro-9aee56c696.

Native chemical fields and actual ARO mint agree; one unspecified centre is retained without inventing a stereochemical assignment.

### Fallback source and parent/class

grounding: supported. Targets: antibioticmech:aro-9aee56c696.

ARO-based mint follows the adopted source pathway. Generic glycopeptide parent is broader and appropriate; current ChEBI naming does not warrant automatic grounding promotion.

### Chemical cross-reference scope

provenance: concern. Targets: antibioticmech:aro-9aee56c696.

ARO/PubChem/ChEBI links resolve, but structureless generic ChEMBL and conflicting alpha nomenclature require exact-equivalence adjudication.

### Veterinary history and regulatory citation

evidence: concern. Targets: antibioticmech:aro-9aee56c696.

The definition lacks geography/date and cites a1989 review for a later event. Rewrite with source-supported historical feed-use scope and distinguish precautionary regulatory rationale from proven transfer.

### Chemical moiety and database-only evidence

evidence: supported. Targets: antibioticmech:aro-9aee56c696.

ATTACKED_COMPONENT/CELL_WALL_COMPONENT and DATABASE_ASSERTION_ONLY accurately preserve the imported chemical-target assertion. Primary model-peptide experiments are useful follow-up after compound mapping; no direct protein or target organism is invented.

### Exact compound activity transfer

evidence: unknown. Targets: antibioticmech:aro-9aee56c696.

Primary antibacterial results exist for avoparcin preparations, but the exact native1747Da form was not established as their material. Do not transfer mixture MICs or congener binding constants automatically.

### Source dates and seed history

provenance: supported. Targets: antibioticmech:aro-9aee56c696.

Single ARO source,PubChem retrieval date and four seed events reproduce. No native status promotion is justified by passing focused gates.

### Potential primary additions

completeness: unknown. Targets: antibioticmech:aro-9aee56c696.

Binding,activity and producer leads are bounded by exact entity resolution. Optional empty fields do not create separate findings.

### Resistance,clinical,dataset and graph blocks

scope: not_applicable. Targets: antibioticmech:aro-9aee56c696.

No populated structured claims in these blocks; definition history is assessed separately.

### Structured adapter applicability

scope: not_applicable. Targets: antibioticmech:aro-9aee56c696.

The native target is a chemical peptidoglycan motif,not a named gene,protein,regulator,pathway or expression dataset. No covered organism/gene query applies.

### Focused validation

schema: supported. Targets: antibioticmech:aro-9aee56c696.

Both actual focused validators pass.

## Findings

### F1: Adjudicate generic avoparcin and conflicting alpha chemical assignments

major / open / confirmed; issue key: avoparcin-generic-alpha-composition-conflict.

The stored1747Da structure faithfully reproduces CID16132294 and CHEBI221101, but that ChEBI alpha label conflicts with CID20055225 and inspected primary congener masses/structure. Generic avoparcin also denotes mixtures. The record therefore cannot yet be treated as one verified natural avoparcin congener with all generic source claims. Resolve the discrepancy without silently adding a hexose,assigning a degradation-product name,or transferring mixture evidence.

### F2: Qualify the historical veterinary-use statement and cite its regulatory source

minor / open / confirmed; issue key: avoparcin-definition-regulatory-scope-citation.

The unqualified ban sentence is linked only to a1989 mechanism review. Official1997 EU text supports a feed-additive withdrawal with explicit geographic,date and precautionary boundaries. Cite that history separately and avoid implying a worldwide prohibition of all animal treatment.

## Recommended Actions And Acceptance Checks

### A1

Resolve ARO3000767/CID16132294/CHEBI221101 generic-versus-congener identity through maintained mapping inputs. Compare the native and independently indexed alpha structures against primary structural chemistry and record an explicit exact-entity or exclusion decision.

- Reconcile C83H92ClN9O31 versus C89H102ClN9O36 with full structural mapping; do not assign the missing-hexose product or unspecified centre by assumption.
- Retain source mixture identity separately from any single congener; do not treat structureless ChEMBL as exact-structure evidence.
- Preserve database-only target provenance until the tested congener maps exactly; any primary upgrade must retain model-peptide assay conditions and preparation composition.
- Run maintained extraction/enrichment/seeding as applicable,focused validation,chemical identity/duplicate checks and corpus gates; do not promote SEEDED until scientific criteria pass.

### A2

Rewrite the historical definition through its maintained owner with precise veterinary feed-use geography/date and a source that documents the regulatory event.

- Separate glycopeptide mechanism support from historical EU feed-additive withdrawal evidence.
- Retain precautionary-risk wording and avoid an unverified worldwide/current legal-status statement.
- Regenerate through the maintained workflow and check exact reference placement and focused validators.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/avoparcin.yaml; Entire YAML | supports | Read MINTED/SEEDED identity, definition and PMID2532132, glycopeptide parent/class, all chemical fields and four xrefs, ARO source mint, database-only D-Ala-D-Ala target with its qualifiers, and four seed-history events. No other populated optional blocks. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; data/raw/aro_target_edges.tsv; conf/aro_target_roles.tsv; ARO row205; PubChem row52; target row224; role configuration row7 | supports | Captured raw owners before assessment. Native source claims reproduce ARO3000767, fallback CID16132294 and target3000720. The raw ARO row also cites PMID9458981, while native definition retains only PMID2532132. Role configuration explicitly treats the chemical moiety as ATTACKED_COMPONENT/CELL_WALL_COMPONENT. |
| aro | https://purl.obolibrary.org/obo/aro.obo; Current ARO3000767,3000081,3000720 stanzas | supports | All native ARO identifiers resolve. Generic avoparcin retains the same definition and three chemical xrefs. The broader glycopeptide parent is appropriate. Target3000720 explicitly lists avoparcin and defines a terminal peptidoglycan group, not a protein. Its sole definition citation PMID18258256 is an oritavancin study. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/16132294; Live PUG chemical properties | supports | CID16132294 exactly matches native C83H92ClN9O31, charge0, average1747.1, exact1745.5587749 and key OTKPPUXRIADSGD-PPRNARJGSA-N. Database agreement establishes faithful reproduction, not correct generic-mixture or natural-congener assignment. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:221101; Live third-party entry | supports | CHEBI221101 is named Avoparcin alpha but reproduces the same native formula, full InChI and key. It is a one-star third-party MetaboLights entry; this name conflicts with independently inspected alpha material/formula evidence and cannot settle the identity alone. |
| alpha | https://pubchem.ncbi.nlm.nih.gov/compound/20055225; Live alpha-avoparcin name resolution and properties | supports | Separately indexed alpha-avoparcin has C89H102ClN9O36, average1909.2, exact1907.6115983 and key JWFVWARSGMYXRN-HTQQBIQNSA-N. Its formula differs from native by C6H10O5. This is a real composition conflict, not merely protonation or one unspecified stereocentre. No missing-sugar congener name is assigned here. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL2108224.json; Current molecule object | context_only | CHEMBL2108224 resolves to generic AVOPARCIN with structure_type NONE and null molecule_structures. It is a useful source-concept reference but supplies no exact structural equivalence. |
| chemistry | Independent RDKit and source-mint checks; Native SMILES/InChI and ARO mint | supports | Both encodings parse to one neutral fragment and exact native key/formula. Calculated average1747.134 agrees with rounded1747.1 and exact1745.558774844. Twenty-six potential tetrahedral centres are assigned and one is unassigned. ARO mint reproduces. |
| definition-citation | https://doi.org/10.1007/BF01967563; PMID2532132;1989 review indexed abstract | context_only | The cited review describes class-level glycopeptide binding to wall-precursor peptides and inhibition of peptidoglycan assembly. It is not primary exact-avoparcin evidence and predates the1997 EU feed-use withdrawal. It cannot document that later regulatory event. |
| spectrum | https://doi.org/10.1016/S0732-8893(97)00134-X; PMID9458981; indexed primary abstract | partial | Study tested avoparcin against814 human clinical isolates and reported staphylococcal MIC50 of4 micrograms/mL, with variable vanB enterococcal MICs. It supplies antibacterial evidence for its preparation; the abstract does not resolve exact congener composition. Its selection-risk interpretation is qualified, not an experimental demonstration of animal-to-human resistance transfer. |
| target-citation | https://doi.org/10.1016/j.jmb.2008.01.031; PMID18258256; indexed abstract of target-term citation | context_only | Study measures oritavancin/vancomycin and des-N-methylleucyl derivatives in Staphylococcus aureus. It does not provide exact avoparcin evidence in the inspected abstract; the native database-only status appropriately avoids calling it primary avoparcin validation. |
| binding | https://doi.org/10.1093/jac/44.5.593; PMID10552974; full author-posted text, Methods pp594–596 and TableI | partial | The1999 study explicitly used a commercial1:2 alpha/beta mixture, ratio confirmed by capillary electrophoresis. Mass-resolved ESI measurements found doubly protonated ions near955/973 and binding to synthetic wall-precursor peptides. TableI reports association constants for N-acetyl-D-Ala-D-Ala of14500/15000 perM. Conditions were5mM ammonium acetate,pH5.1,298K. These are direct model-peptide binding results for distinguishable components, not evidence that the1747Da native structure was the tested alpha congener. |
| binding-fulltext | https://www.researchgate.net/publication/12747908_Interactions_of_a-_and_b-avoparcin_with_bacterial_cell-wall_receptor-mimicking_peptides_studied_by_electrospray_ionization_mass_spectrometry; Author-posted full text read through web tool | supports | Full-text Methods and Results support the preparation and assay scope recorded above. The indexed abstract snapshot is hashed separately; full-text browser extraction was inspected but not downloaded as a local PDF. |
| production | https://doi.org/10.3390/fermentation8020044; 2022 full public publisher PDF, section3.3 and visually inspected Figure4 | partial | Fermentation/purification study distinguishes alpha,beta and additional ristosamynil factors. Its alpha/beta signals are[M+2H]2+ at m/z956/973; Figure4 shows five sugar units in the parent congeners. Source strain A.coloradensis ATCC53629 yields a complex, not one composition. Newly proposed sugar-addition regiochemistry remains unresolved, and their antimicrobial assays are future work. |
| regulation | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:31997L0006; Commission Directive97/6/EC; preamble,Article3 and Annex; complete browser text | supports | Historical EU directive deleted avoparcinE715 from authorized feedingstuff additives, requiring implementation by1April1997. It distinguishes Denmark1995/Germany1996 measures and explicitly adopts a precautionary response to unresolved animal-to-human resistance-transfer risk. This supports a geographically and temporally bounded historical account, not a worldwide prohibition of all veterinary treatment. |
| gates | just validate; just validate-strict; Actual batch013 focused commands | supports | Both commands exit0; strict checked one file with zero errors. Chemical consistency passes; exact entity applicability is a scientific issue beyond the schema. |
| search | CultureBotAI/AntibioticMech and free public sources; Ignored-inclusive identity/raw-owner/curation search | context_only | Search included ignored files outside.git/.venv. No adopted ChEBI221101 seed row or exact source-scope adjudication was located in bounded raw/curation searches; live ChEBI remains a verified cross-reference with conflicting naming scope. |

## Limits And Additional Notes

- The native1747Da species was not assigned a specific missing-sugar/degradation-product name. A formula delta alone does not resolve regiochemistry or every stereocentre; primary historical structural adjudication remains needed.
- PMID2532132,9458981 and18258256 were inspected at indexed-abstract level. Full1999 binding text and2022 producer paper were inspected,with the latter figure visually checked.
- Several publisher/PDF routes returned403/429 or empty responses. Author-posted full binding text and official EUR-Lex HTML were readable through the web tool but not captured as local PDF snapshots; their source URLs and locators are retained. The2022 alternate publisher PDF is hashed.
- Historical EU text establishes the1997 event,not a survey of current worldwide avoparcin regulation. No global clinical or legal-status inference is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All26 captured native/context input hashes were rechecked unchanged. No native fields,status,history or source inventory was edited.
- Initial chemistry helper used a ChEBI-only mint; corrected actual ARO mint is a scratch-helper correction,not a native defect.
- No optional missing field is scored as a finding. The observed primary binding results are retained as real experiments without assuming applicability to the unresolved native structure.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T095037Z-avoparcin
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Avoparcin: conflicting congener assignment and historical definition scope'
started_at: '2026-10-21T09:28:15Z'
finished_at: '2026-10-21T09:50:37Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Full native/source-owner read,current identities,independent
    chemistry and primary congener/assay plus official regulatory text.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One major source/congener identity conflict and one minor historical definition/citation
  finding. Internal chemistry and both focused validators pass. The database-only
  chemical-target representation is appropriately cautious; exact primary evidence
  transfer remains unresolved.
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
  - path: data/antibiotics/antibacterial/avoparcin.yaml
    sha256: 91d5799f39c21f2a86ab8329b9418795862333a50cce4d000889030be788e329
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
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: antibioticmech:aro-9aee56c696
  path: data/antibiotics/antibacterial/avoparcin.yaml
  label: avoparcin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source identity and definition
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Fallback structure
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported chemical target edge
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target-role configuration
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Fallback structure mapping
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Exact form adjudication
scope:
  description: Whole-record scientific review of the single minted avoparcin record.
  selection: Queue129 in isolated batch013.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-9aee56c696
  exclusions:
  - target: Other avoparcin congeners,commercial mixtures and related glycopeptides
      as separate records
    reason: Used only to test exact identity and evidence boundaries.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - antibioticmech:aro-9aee56c696
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/avoparcin.yaml
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
  - antibioticmech:aro-9aee56c696
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/avoparcin.yaml --out /private/tmp/am-review-session/129-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Internal chemical consistency and source mint
  status: passed
  required: true
  summary: Both native encodings and ARO mint agree; exact congener mapping remains
    unresolved.
  target_ids:
  - antibioticmech:aro-9aee56c696
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
  - antibioticmech:aro-9aee56c696
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
  - antibioticmech:aro-9aee56c696
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
  - antibioticmech:aro-9aee56c696
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
  - antibioticmech:aro-9aee56c696
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
  - antibioticmech:aro-9aee56c696
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
  - antibioticmech:aro-9aee56c696
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
  - antibioticmech:aro-9aee56c696
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
  - antibioticmech:aro-9aee56c696
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
  - antibioticmech:aro-9aee56c696
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/avoparcin.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T09:33:31Z'
  support: supports
  summary: Read MINTED/SEEDED identity, definition and PMID2532132, glycopeptide parent/class,
    all chemical fields and four xrefs, ARO source mint, database-only D-Ala-D-Ala
    target with its qualifiers, and four seed-history events. No other populated optional
    blocks.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; data/raw/aro_target_edges.tsv;
    conf/aro_target_roles.tsv
  locator: ARO row205; PubChem row52; target row224; role configuration row7
  accessed_at: '2026-10-21T09:33:31Z'
  support: supports
  summary: Captured raw owners before assessment. Native source claims reproduce ARO3000767,
    fallback CID16132294 and target3000720. The raw ARO row also cites PMID9458981,
    while native definition retains only PMID2532132. Role configuration explicitly
    treats the chemical moiety as ATTACKED_COMPONENT/CELL_WALL_COMPONENT.
- evidence_id: aro
  kind: authority
  reference: https://purl.obolibrary.org/obo/aro.obo
  locator: Current ARO3000767,3000081,3000720 stanzas
  accessed_at: '2026-10-21T09:28:50Z'
  support: supports
  summary: All native ARO identifiers resolve. Generic avoparcin retains the same
    definition and three chemical xrefs. The broader glycopeptide parent is appropriate.
    Target3000720 explicitly lists avoparcin and defines a terminal peptidoglycan
    group, not a protein. Its sole definition citation PMID18258256 is an oritavancin
    study.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/16132294
  locator: Live PUG chemical properties
  accessed_at: '2026-10-21T09:28:49Z'
  support: supports
  summary: CID16132294 exactly matches native C83H92ClN9O31, charge0, average1747.1,
    exact1745.5587749 and key OTKPPUXRIADSGD-PPRNARJGSA-N. Database agreement establishes
    faithful reproduction, not correct generic-mixture or natural-congener assignment.
  snapshot_sha256: 369039248e81ecd17ed05945a9b26f1b17d9f29b8a0451d9afceee65a3610138
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:221101
  locator: Live third-party entry
  accessed_at: '2026-10-21T09:28:51Z'
  support: supports
  summary: CHEBI221101 is named Avoparcin alpha but reproduces the same native formula,
    full InChI and key. It is a one-star third-party MetaboLights entry; this name
    conflicts with independently inspected alpha material/formula evidence and cannot
    settle the identity alone.
  snapshot_sha256: 90ab7a0e59f7c2f655f34433cbf1a6af61e440ca52245c17b7b5b735f64c009a
- evidence_id: alpha
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/20055225
  locator: Live alpha-avoparcin name resolution and properties
  accessed_at: '2026-10-21T09:28:50Z'
  support: supports
  summary: Separately indexed alpha-avoparcin has C89H102ClN9O36, average1909.2, exact1907.6115983
    and key JWFVWARSGMYXRN-HTQQBIQNSA-N. Its formula differs from native by C6H10O5.
    This is a real composition conflict, not merely protonation or one unspecified
    stereocentre. No missing-sugar congener name is assigned here.
  snapshot_sha256: 41771c6a9c377517ff81b77966a706a2a052880d1fd371966d2ac632f87efdb4
- evidence_id: chembl
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL2108224.json
  locator: Current molecule object
  accessed_at: '2026-10-21T09:28:50Z'
  support: context_only
  summary: CHEMBL2108224 resolves to generic AVOPARCIN with structure_type NONE and
    null molecule_structures. It is a useful source-concept reference but supplies
    no exact structural equivalence.
  snapshot_sha256: d7a89bcb77839ecc7e983c92fc055cd9691edcf253f22a3aa4cbf847f5711d8f
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit and source-mint checks
  locator: Native SMILES/InChI and ARO mint
  accessed_at: '2026-10-21T09:28:47Z'
  support: supports
  summary: Both encodings parse to one neutral fragment and exact native key/formula.
    Calculated average1747.134 agrees with rounded1747.1 and exact1745.558774844.
    Twenty-six potential tetrahedral centres are assigned and one is unassigned. ARO
    mint reproduces.
  snapshot_sha256: 94b3f3f2d79dee4444cc72a8b8ec44d5b1673655a23e37d38938b285cf41f1b5
- evidence_id: definition-citation
  kind: database
  reference: https://doi.org/10.1007/BF01967563
  locator: PMID2532132;1989 review indexed abstract
  accessed_at: '2026-10-21T09:28:50Z'
  support: context_only
  summary: The cited review describes class-level glycopeptide binding to wall-precursor
    peptides and inhibition of peptidoglycan assembly. It is not primary exact-avoparcin
    evidence and predates the1997 EU feed-use withdrawal. It cannot document that
    later regulatory event.
  snapshot_sha256: f0ea63999508ae0c54056915aa896f6e4536761f047cf8be5b7c616ca754b91b
- evidence_id: spectrum
  kind: primary_source
  reference: https://doi.org/10.1016/S0732-8893(97)00134-X
  locator: PMID9458981; indexed primary abstract
  accessed_at: '2026-10-21T09:28:50Z'
  support: partial
  summary: Study tested avoparcin against814 human clinical isolates and reported
    staphylococcal MIC50 of4 micrograms/mL, with variable vanB enterococcal MICs.
    It supplies antibacterial evidence for its preparation; the abstract does not
    resolve exact congener composition. Its selection-risk interpretation is qualified,
    not an experimental demonstration of animal-to-human resistance transfer.
  snapshot_sha256: 89ab18998fb8995c182f61b46a6e6a82132f97e4c44b6ebea394b7d52b4d79ed
- evidence_id: target-citation
  kind: primary_source
  reference: https://doi.org/10.1016/j.jmb.2008.01.031
  locator: PMID18258256; indexed abstract of target-term citation
  accessed_at: '2026-10-21T09:31:11Z'
  support: context_only
  summary: Study measures oritavancin/vancomycin and des-N-methylleucyl derivatives
    in Staphylococcus aureus. It does not provide exact avoparcin evidence in the
    inspected abstract; the native database-only status appropriately avoids calling
    it primary avoparcin validation.
  snapshot_sha256: e01e6ed2f8c9f6cb8e597d156e323a7d29367c8abe58102f7f3f638b87a2d9c1
- evidence_id: binding
  kind: primary_source
  reference: https://doi.org/10.1093/jac/44.5.593
  locator: PMID10552974; full author-posted text, Methods pp594–596 and TableI
  accessed_at: '2026-10-21T09:31:11Z'
  support: partial
  summary: The1999 study explicitly used a commercial1:2 alpha/beta mixture, ratio
    confirmed by capillary electrophoresis. Mass-resolved ESI measurements found doubly
    protonated ions near955/973 and binding to synthetic wall-precursor peptides.
    TableI reports association constants for N-acetyl-D-Ala-D-Ala of14500/15000 perM.
    Conditions were5mM ammonium acetate,pH5.1,298K. These are direct model-peptide
    binding results for distinguishable components, not evidence that the1747Da native
    structure was the tested alpha congener.
  snapshot_sha256: 543ffc7a2d1b871a5cd1cbfaa51c0c9cdb5cc8dd32d3fb34961f01a9adefa5ed
- evidence_id: binding-fulltext
  kind: primary_source
  reference: https://www.researchgate.net/publication/12747908_Interactions_of_a-_and_b-avoparcin_with_bacterial_cell-wall_receptor-mimicking_peptides_studied_by_electrospray_ionization_mass_spectrometry
  locator: Author-posted full text read through web tool
  accessed_at: '2026-10-21T09:33:31Z'
  support: supports
  summary: Full-text Methods and Results support the preparation and assay scope recorded
    above. The indexed abstract snapshot is hashed separately; full-text browser extraction
    was inspected but not downloaded as a local PDF.
- evidence_id: production
  kind: primary_source
  reference: https://doi.org/10.3390/fermentation8020044
  locator: 2022 full public publisher PDF, section3.3 and visually inspected Figure4
  accessed_at: '2026-10-21T09:31:38Z'
  support: partial
  summary: Fermentation/purification study distinguishes alpha,beta and additional
    ristosamynil factors. Its alpha/beta signals are[M+2H]2+ at m/z956/973; Figure4
    shows five sugar units in the parent congeners. Source strain A.coloradensis ATCC53629
    yields a complex, not one composition. Newly proposed sugar-addition regiochemistry
    remains unresolved, and their antimicrobial assays are future work.
  snapshot_sha256: f76bb39cdd4a3b22fa436b737c99453fec3c3539e38e0de27df348d8c5f70c24
- evidence_id: regulation
  kind: authority
  reference: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:31997L0006
  locator: Commission Directive97/6/EC; preamble,Article3 and Annex; complete browser
    text
  accessed_at: '2026-10-21T09:33:31Z'
  support: supports
  summary: Historical EU directive deleted avoparcinE715 from authorized feedingstuff
    additives, requiring implementation by1April1997. It distinguishes Denmark1995/Germany1996
    measures and explicitly adopts a precautionary response to unresolved animal-to-human
    resistance-transfer risk. This supports a geographically and temporally bounded
    historical account, not a worldwide prohibition of all veterinary treatment.
- evidence_id: gates
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual batch013 focused commands
  accessed_at: '2026-10-21T09:33:31Z'
  support: supports
  summary: Both commands exit0; strict checked one file with zero errors. Chemical
    consistency passes; exact entity applicability is a scientific issue beyond the
    schema.
  snapshot_sha256: b0fc56f8ba44a2a431531451d8c73ff7eea9229e8c9ed75903a9600da30c83ba
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech and free public sources
  locator: Ignored-inclusive identity/raw-owner/curation search
  accessed_at: '2026-10-21T09:28:17Z'
  support: context_only
  summary: Search included ignored files outside.git/.venv. No adopted ChEBI221101
    seed row or exact source-scope adjudication was located in bounded raw/curation
    searches; live ChEBI remains a verified cross-reference with conflicting naming
    scope.
  search_scope: prepare.py129 rg --no-ignore --hidden label,identifier,slug; exact
    ARO/CID/CHEBI searches of raw and curation; current ARO,PubChem,ChEBI,ChEMBL and
    cited/compound-specific primary follow-up.
  snapshot_sha256: 8f243c8d090df4200592c4be6de3705a5139880cb442ec2011541975d8673a51
assessments:
- assessment_id: identity
  area: identity
  topic: Generic mixture and conflicting alpha structures
  outcome: concern
  summary: The native structure is internally coherent, but its alpha name mapping
    conflicts with independent congener composition evidence. Source identity needs
    adjudication before exact assay transfer.
  target_ids:
  - antibioticmech:aro-9aee56c696
  evidence_ids:
  - native
  - pubchem
  - chebi
  - alpha
  - binding
  - production
- assessment_id: internal
  area: identity
  topic: Encodings,charge,masses and mint
  outcome: supported
  summary: Native chemical fields and actual ARO mint agree; one unspecified centre
    is retained without inventing a stereochemical assignment.
  target_ids:
  - antibioticmech:aro-9aee56c696
  evidence_ids:
  - chemistry
  - pubchem
- assessment_id: grounding
  area: grounding
  topic: Fallback source and parent/class
  outcome: supported
  summary: ARO-based mint follows the adopted source pathway. Generic glycopeptide
    parent is broader and appropriate; current ChEBI naming does not warrant automatic
    grounding promotion.
  target_ids:
  - antibioticmech:aro-9aee56c696
  evidence_ids:
  - owners
  - aro
  - chebi
- assessment_id: xref
  area: provenance
  topic: Chemical cross-reference scope
  outcome: concern
  summary: ARO/PubChem/ChEBI links resolve, but structureless generic ChEMBL and conflicting
    alpha nomenclature require exact-equivalence adjudication.
  target_ids:
  - antibioticmech:aro-9aee56c696
  evidence_ids:
  - aro
  - pubchem
  - chebi
  - chembl
  - alpha
- assessment_id: definition
  area: evidence
  topic: Veterinary history and regulatory citation
  outcome: concern
  summary: The definition lacks geography/date and cites a1989 review for a later
    event. Rewrite with source-supported historical feed-use scope and distinguish
    precautionary regulatory rationale from proven transfer.
  target_ids:
  - antibioticmech:aro-9aee56c696
  evidence_ids:
  - native
  - definition-citation
  - regulation
  - spectrum
- assessment_id: target
  area: evidence
  topic: Chemical moiety and database-only evidence
  outcome: supported
  summary: ATTACKED_COMPONENT/CELL_WALL_COMPONENT and DATABASE_ASSERTION_ONLY accurately
    preserve the imported chemical-target assertion. Primary model-peptide experiments
    are useful follow-up after compound mapping; no direct protein or target organism
    is invented.
  target_ids:
  - antibioticmech:aro-9aee56c696
  evidence_ids:
  - owners
  - aro
  - target-citation
  - binding
- assessment_id: activity
  area: evidence
  topic: Exact compound activity transfer
  outcome: unknown
  summary: Primary antibacterial results exist for avoparcin preparations, but the
    exact native1747Da form was not established as their material. Do not transfer
    mixture MICs or congener binding constants automatically.
  target_ids:
  - antibioticmech:aro-9aee56c696
  evidence_ids:
  - spectrum
  - binding
  - production
- assessment_id: history
  area: provenance
  topic: Source dates and seed history
  outcome: supported
  summary: Single ARO source,PubChem retrieval date and four seed events reproduce.
    No native status promotion is justified by passing focused gates.
  target_ids:
  - antibioticmech:aro-9aee56c696
  evidence_ids:
  - native
  - owners
  - gates
- assessment_id: completeness
  area: completeness
  topic: Potential primary additions
  outcome: unknown
  summary: Binding,activity and producer leads are bounded by exact entity resolution.
    Optional empty fields do not create separate findings.
  target_ids:
  - antibioticmech:aro-9aee56c696
  evidence_ids:
  - binding
  - spectrum
  - production
- assessment_id: other
  area: scope
  topic: Resistance,clinical,dataset and graph blocks
  outcome: not_applicable
  summary: No populated structured claims in these blocks; definition history is assessed
    separately.
  target_ids:
  - antibioticmech:aro-9aee56c696
  evidence_ids:
  - native
- assessment_id: adapter
  area: scope
  topic: Structured adapter applicability
  outcome: not_applicable
  summary: The native target is a chemical peptidoglycan motif,not a named gene,protein,regulator,pathway
    or expression dataset. No covered organism/gene query applies.
  target_ids:
  - antibioticmech:aro-9aee56c696
  evidence_ids:
  - native
  - aro
- assessment_id: schema
  area: schema
  topic: Focused validation
  outcome: supported
  summary: Both actual focused validators pass.
  target_ids:
  - antibioticmech:aro-9aee56c696
  evidence_ids:
  - gates
findings:
- finding_id: F1
  issue_key: avoparcin-generic-alpha-composition-conflict
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Adjudicate generic avoparcin and conflicting alpha chemical assignments
  description: The stored1747Da structure faithfully reproduces CID16132294 and CHEBI221101,
    but that ChEBI alpha label conflicts with CID20055225 and inspected primary congener
    masses/structure. Generic avoparcin also denotes mixtures. The record therefore
    cannot yet be treated as one verified natural avoparcin congener with all generic
    source claims. Resolve the discrepancy without silently adding a hexose,assigning
    a degradation-product name,or transferring mixture evidence.
  target_ids:
  - antibioticmech:aro-9aee56c696
  field_paths:
  - identifier
  - label
  - chemical_structure
  - xrefs
  - source_concepts
  - grounding_status
  - molecular_targets[0]
  evidence_ids:
  - native
  - pubchem
  - chebi
  - alpha
  - chembl
  - binding
  - production
  rule_id: docs/HARMONIZATION.md:The unit of the corpus is a structure; native-review-checklist:Identity
    and Equivalence
  native_severity: major exact entity and evidence scope unresolved
  normalization_reason: The cross-source composition conflict is confirmed; which
    source assignment should change remains unresolved. Internal encodings are valid,so
    this is not a fabricated structure or automatic blocker/duplicate judgment.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Inherited source identity and definition
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Fallback chemical mapping
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure mapping owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Exact source identity adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated identity
- finding_id: F2
  issue_key: avoparcin-definition-regulatory-scope-citation
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify the historical veterinary-use statement and cite its regulatory source
  description: The unqualified ban sentence is linked only to a1989 mechanism review.
    Official1997 EU text supports a feed-additive withdrawal with explicit geographic,date
    and precautionary boundaries. Cite that history separately and avoid implying
    a worldwide prohibition of all animal treatment.
  target_ids:
  - antibioticmech:aro-9aee56c696
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - native
  - definition-citation
  - regulation
  rule_id: native-review-checklist:Definition and Evidence Fidelity
  native_severity: minor definition scope and citation gap
  normalization_reason: The historical core is supportable; the defect is unbounded
    wording and a temporally unsuitable citation,not proof that no avoparcin restriction
    occurred.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Inherited source identity and definition
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Fallback chemical mapping
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure mapping owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Exact source identity adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated identity
actions:
- action_id: A1
  description: Resolve ARO3000767/CID16132294/CHEBI221101 generic-versus-congener
    identity through maintained mapping inputs. Compare the native and independently
    indexed alpha structures against primary structural chemistry and record an explicit
    exact-entity or exclusion decision.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-9aee56c696
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Inherited source identity and definition
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Fallback chemical mapping
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure mapping owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Exact source identity adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated identity
  acceptance_checks:
  - Reconcile C83H92ClN9O31 versus C89H102ClN9O36 with full structural mapping; do
    not assign the missing-hexose product or unspecified centre by assumption.
  - Retain source mixture identity separately from any single congener; do not treat
    structureless ChEMBL as exact-structure evidence.
  - Preserve database-only target provenance until the tested congener maps exactly;
    any primary upgrade must retain model-peptide assay conditions and preparation
    composition.
  - Run maintained extraction/enrichment/seeding as applicable,focused validation,chemical
    identity/duplicate checks and corpus gates; do not promote SEEDED until scientific
    criteria pass.
- action_id: A2
  description: Rewrite the historical definition through its maintained owner with
    precise veterinary feed-use geography/date and a source that documents the regulatory
    event.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-9aee56c696
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Inherited source identity and definition
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Fallback chemical mapping
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Structure mapping owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Exact source identity adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated identity
  acceptance_checks:
  - Separate glycopeptide mechanism support from historical EU feed-additive withdrawal
    evidence.
  - Retain precautionary-risk wording and avoid an unverified worldwide/current legal-status
    statement.
  - Regenerate through the maintained workflow and check exact reference placement
    and focused validators.
limitations:
- The native1747Da species was not assigned a specific missing-sugar/degradation-product
  name. A formula delta alone does not resolve regiochemistry or every stereocentre;
  primary historical structural adjudication remains needed.
- PMID2532132,9458981 and18258256 were inspected at indexed-abstract level. Full1999
  binding text and2022 producer paper were inspected,with the latter figure visually
  checked.
- Several publisher/PDF routes returned403/429 or empty responses. Author-posted full
  binding text and official EUR-Lex HTML were readable through the web tool but not
  captured as local PDF snapshots; their source URLs and locators are retained. The2022
  alternate publisher PDF is hashed.
- Historical EU text establishes the1997 event,not a survey of current worldwide avoparcin
  regulation. No global clinical or legal-status inference is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All26 captured native/context input hashes were rechecked unchanged. No native fields,status,history
  or source inventory was edited.
- Initial chemistry helper used a ChEBI-only mint; corrected actual ARO mint is a
  scratch-helper correction,not a native defect.
- No optional missing field is scored as a finding. The observed primary binding results
  are retained as real experiments without assuming applicability to the unresolved
  native structure.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://pubchem.ncbi.nlm.nih.gov/compound/16132294
- https://www.ebi.ac.uk/chebi/CHEBI:221101
- https://pubchem.ncbi.nlm.nih.gov/compound/20055225
- https://doi.org/10.1093/jac/44.5.593
- https://doi.org/10.3390/fermentation8020044
tags:
- avoparcin
- glycopeptide
- congener-scope
- identity-conflict
```
