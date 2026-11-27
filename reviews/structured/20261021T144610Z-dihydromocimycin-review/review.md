# Dihydromocimycin: wrong pyridone saturation in the imported structure

- Review: 20261021T144610Z-dihydromocimycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:27:14Z
- Finished UTC: 2026-10-21T14:46:10Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native graph reproduces its PubChem source but contradicts the original characterization of dihydromocimycin: its pyridone C5-C6 bond is unsaturated and its formula has two hydrogens too few. The original patent explicitly establishes the saturated bond, distinguishes mocimycin, and supports production by Streptomyces ramocissimus CBS190.69 plus bounded antibacterial activity. One identity blocker and one minor definition-citation problem require maintained-source curation.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 366; one exact record. All 13 original input hashes are preserved within 25 expanded source/context inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-6e963f402b | data/antibiotics/antibacterial/dihydromocimycin.yaml | generated | dihydromocimycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Structured-source applicability | not_applicable | False | antibioticmech:aro-6e963f402b | No native named gene, molecular protein target, pathway or transcriptomic assertion is present. No iModulon evidence was used to infer a molecular mechanism from elfamycin class membership. |
| Focused chemistry verification | passed | False | antibioticmech:aro-6e963f402b | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-6e963f402b | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-6e963f402b | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-6e963f402b | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-6e963f402b | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-6e963f402b | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-6e963f402b | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-6e963f402b | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-6e963f402b | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-6e963f402b | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-6e963f402b | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-6e963f402b | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact named molecule versus stored graph

identity: concern. Targets: antibioticmech:aro-6e963f402b.

The original saturated dihydromocimycin structure is incompatible with the native pyridone double bond and H60 formula. Internal encoding agreement and current PubChem propagation cannot resolve the mismatch. This is a wrong-identity blocker.

### Minted ARO identity and chemical xrefs

grounding: concern. Targets: antibioticmech:aro-6e963f402b.

The ARO concept and broader class resolve, but its PubChem equivalence supplies a graph with the wrong hydrogenation state. Recover the exact intended structure before selecting any corrected chemical grounding; do not replace it with a similarly named elfamycin.

### Antibacterial eligibility and class

scope: supported. Targets: antibioticmech:aro-6e963f402b.

The characterized natural compound belongs to the elfamycin family and has original antibacterial dilution results. This supports intended-compound eligibility but does not repair the identity of the current graph.

### Producer statement and definition citation

evidence: concern. Targets: antibioticmech:aro-6e963f402b.

The producer/strain statement is supported by the original patent. PMID2272911 instead reports SB22484 and only lists dihydromocimycin as a comparator; the seeded first-reference choice does not support the exact producer assertion.

### Optional activity_spectrum

completeness: supported. Targets: antibioticmech:aro-6e963f402b.

Bounded dihydromocimycin assay rows are available after identity correction. No quantitative row should be attached to the current unsaturated graph or assigned unreported material/medium details. Optional absence is not a required-field defect.

### Absent mechanism, targets and resistance

completeness: unknown. Targets: antibioticmech:aro-6e963f402b.

No such native claim is populated. Elfamycin class context alone does not establish the exact-compound molecular target or resistance alleles. The patent supplies phenotypes and chemistry, not a direct-target experiment.

### Both adopted primary-paper leads

evidence: supported. Targets: antibioticmech:aro-6e963f402b.

Both originals were inspected at their relevant material/Introduction/comparator/reference scope. Their main experiments concern other antibiotics; neither was silently converted to exact dihydromocimycin assay evidence.

### Clinical products, producer objects, graph and datasets

scope: not_applicable. Targets: antibioticmech:aro-6e963f402b.

No structured assertions of these kinds occur. The definition contains a supported producer claim requiring the correct citation; patent formulation/therapeutic statements do not establish a clinical product or causal graph.

### Source merge, status and history

provenance: supported. Targets: antibioticmech:aro-6e963f402b.

The ARO mint, source version and three generated events reproduce. The original 13 inputs remain unchanged and actual PubChem/ARO ownership is captured. SEEDED status is retained.

### Deterministic checks versus scientific identity

schema: supported. Targets: antibioticmech:aro-6e963f402b.

Schema, strict and structure-consistency checks pass; the source-level chemical identity defect is outside those checks. Shared same-base corpus gates are attached by root.

## Findings

### F1: The stored graph lacks the defining pyridone hydrogenation

blocker / open / confirmed; issue key: dihydromocimycin-wrong-pyridone-hydrogenation.

Native SMILES/InChI encode C5=C6 in the pyridone ring and C43H60N2O12. The original dihydromocimycin drawing and chemical proof require a saturated C5-C6 bond and parent C43H62N2O12. This is a constitutional hydrogenation-state mismatch, not a tautomer or hydrate difference. Current PubChem54679334 repeats the incorrect graph. Curate the exact named natural structure and its cross-reference through maintained inputs before any assay enrichment.

### F2: The definition points to a comparator paper instead of the producer experiment

minor / open / confirmed; issue key: dihydromocimycin-producer-definition-citation.

PMID2272911 reports SB22484 from NRRL15496 and lists dihydromocimycin only as a literature comparator. It does not directly support S. ramocissimus CBS190.69 production. The original dihydromocimycin patent does support that statement. Correct the evidence pointer without discarding the substantiated producer fact.

## Recommended Actions And Acceptance Checks

### A1

Resolve and regenerate the exact dihydromocimycin structure and equivalent chemical links.

- Reconcile the original saturated pyridone, full tautomer/stereochemistry and parent C43H62N2O12; distinguish free acid from salts/hydrates.
- Do not use the scratch bond-repair graph as an automatically accepted full replacement; confirm every remaining stereochemical and connectivity assignment.
- Remove or correct any exact xref whose independently retrieved structure retains the C5=C6 bond.
- Recalculate SMILES/InChI/key, formula, charge and masses together and run schema, strict, source provenance and corpus-reproduction checks.

### A2

Attach the producer statement to the original evidence through maintained definition provenance.

- The regenerated definition_source resolves to inspected evidence for CBS190.69 production of dihydromocimycin.
- Retain the adopted1990/1986 papers only at their actual comparator/discovery scope.
- Keep mocimycin-only assays, growth promotion and earlier patent tables separate from dihydromocimycin.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/dihydromocimycin.yaml; Complete native record: definition/source, parent/class, full graph, two xrefs, one source concept and three history events | supports | The MINTED/SEEDED ARO record calls the material dihydromocimycin and cites PMID2272911 for production by S. ramocissimus CBS190.69. Its PubChem-derived graph is C43H60N2O12. No synonym, mode, molecular target, resistance, activity_spectrum, clinical product, producer object, causal graph or dataset assertion is populated. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; ARO row229 and PubChem row63; extractor/enrichment/seeder ownership | supports | The actual ARO row supplies the definition, two literature references and CID54679334. The corresponding PubChem row supplies all structure fields. The seeder selects the first definition reference and uses the broad elfamycin class as the parent. Initial captures were retained and actual ARO/PubChem owners added; the ChEBI table contains no exact-name row in this inspected source snapshot. |
| chemistry | Independent RDKit2026.03.5 using batch019 interpreter against batch037 cwd; 366-chemistry.json | supports | Both native encodings reproduce LWXUPCAADQWXRE-UPMFUDSQSA-N, neutral C43H60N2O12, 11 assigned centres, masses and the ARO source mint. Internal agreement does not establish that the graph represents the named natural product. |
| aro | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3001248; Current ARO:3001248 complete term, definition references and PubChem cross-reference | supports | Current ARO repeats the native name, producer statement, two PMID citations and PubChem54679334 link. The term is not obsolete. This confirms source propagation, not the correctness of the linked molecular graph. |
| parent | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3001219; Current ARO:3001219 elfamycin antibiotic | supports | The parent resolves as the broader elfamycin antibiotic class. Class membership does not imply that the particular compound has a demonstrated EF-Tu target or that an unsaturated analogue is chemically equivalent. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/54679334/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; CID54679334 current complete structure properties | supports | Current PubChem reproduces the native C43H60N2O12 graph and key. The separate synonym route returned 404, so no independently readable current PubChem name list established the dihydromocimycin assignment. The structural mismatch is inherited from the adopted ARO-to-PubChem mapping. |
| adopted1990 | https://doi.org/10.7164/antibiotics.43.1349; PMID2272911; original abstract, producer/material Methods, Discussion/Table7 at printed page1355 and reference31; actual Table7 viewed | supports | The experiments concern SB22484 from Streptomyces sp. NRRL15496. Dihydromocimycin is a literature comparator in Table7, with molecular weight 798 versus kirromycin(mocimycin) 796 and a patent reference. The paper does not report the native CBS190.69 producer experiment; its SB22484 activities cannot be transferred. Its comparator mass independently agrees with the original dihydromocimycin patent. |
| adopted1986 | https://doi.org/10.7164/antibiotics.39.1361; PMID3781906; original abstract/Introduction and relevant material, activity and reference6 scope | context_only | The original study isolates L-681,217. Dihydromocimycin appears in the Introduction as a related antibiotic with a patent citation. Its exact producer, structure and antibacterial assays were not newly established in this paper. The L-681,217 or mocimycin growth-promotion results are not dihydromocimycin evidence. |
| patent-identity | https://patents.google.com/patent/US4062948A/en; Original US4062948 scan PDF page11, printed columns9-10: actual structural formula and elemental analysis; page12 column11 chemical proof | supports | The patent explicitly distinguishes dihydromocimycin from mocimycin by saturation of pyridone C5-C6. The actual drawing shows this single bond. Elemental analysis is calculated for C43H62N2O12·2H2O; the parent molecule therefore has H62, not H60. Replacement of two olefinic doublets by methylene triplets and degradation to beta-alanine support the assignment. Hydration does not explain a two-hydrogen change with unchanged oxygen count. |
| atom-map | Scratch bond-order comparison; native graph left untouched; 366-saturation-check.json; zero-based RDKit atom mapping of native SMILES | supports | The ring is N33-C34(=O)-C28-C29(=O)-C31=C32-N33. Thus patent pyridone positions5/6 map to atoms31/32, which are both CH with a double bond in the native graph. Changing only that bond to single in scratch yields C43H62N2O12 and ATKFZHHCPMJIBV-UPMFUDSQSA-N. This diagnoses the missing hydrogenation; it is not a fully adjudicated replacement tautomer/stereostructure. |
| patent-producer | https://patents.google.com/patent/US4062948A/en; Dihydromocimycin section, printed columns12-14; fermentation and separation paragraphs | supports | The original patent identifies S. ramocissimus CBS190.69 and distinguishes co-produced mocimycin from dihydromocimycin by controlled precipitation, chromatography and spectroscopic characterization. It describes increased dihydromocimycin yield with aeration. The native producer statement is substantively supported here, but the populated PMID is not this primary experiment. |
| patent-activity | https://patents.google.com/patent/US4062948A/en; Original scan PDF page12, printed column12; actual paired agar/liquid dilution MIC tables | supports | The tables contain separate mocimycin and dihydromocimycin columns. Dihydromocimycin agar MICs include Diplococcus pneumoniae L54 &lt;0.75 and Listeria monocytogenes A2130 1.5 micrograms/mL; liquid dilution includes B. subtilis ATCC6633 50 micrograms/mL. Agar culture is explicitly anaerobic. Full medium/incubation and exact preparation salt/hydrate for these paired assays are not supplied locally. Earlier TableII and its detailed method belong to mocimycin and must not be borrowed. These data establish activity of characterized dihydromocimycin, not the incorrect native unsaturated graph. |
| patent-boundaries | https://patents.google.com/patent/US4062948A/en; Dihydromocimycin separation, therapeutic claims and dehydrogenation sections | context_only | The patent discusses free acid, salts and hydration separately and chemically converts dihydromocimycin to mocimycin. It explicitly distinguishes their animal growth-promotion behavior. Patent therapeutic language is not a regulatory approval or independently verified clinical efficacy claim; derivative/salt use does not establish the neutral record as a formulation. |
| search | Ignored-inclusive local search and official authority/primary discovery; 366367-local-focused.txt;366-discovery.json;366-chebi-search.json | context_only | The exact native key occurs in the adopted PubChem row and this native record in the searched local source/review surfaces. Current official ChEBI exact-name search returned no term for dihydromocimycin. This supports preserving an explicit minted-identity workflow, not automatic substitution of a near-name compound. Public patent discovery supplied the primary identity and activity evidence. |
| gates | Focused schema, strict and standalone chemistry; 366-focused-results.json | supports | All focused gates exit 0 despite the wrong named-structure assignment. Native checks used batch037; standalone chemistry used batch019 RDKit against batch037 cwd. |

## Limits And Additional Notes

- The original patent structure, elemental analysis, chemical proof and paired antibacterial tables were inspected as actual scan images. The full stereochemical identity of a corrected replacement graph has not been adjudicated; the scratch saturation calculation is diagnostic only.
- Both adopted papers were read at their relevant compound/material, comparator, Introduction/Discussion and reference scope; unrelated SB22484/L-681,217 assay tables were not transferred or exhaustively reanalyzed.
- The patent distinguishes salts, a hydrated analytical specimen, neutral material and mixtures. Exact preparation form and full conditions for the dihydromocimycin paired dilution tables are incompletely specified; earlier mocimycin assay methods are not assumed to apply.
- Current PubChem structure data resolve, but its synonym endpoint returned 404. The bounded official ChEBI exact-name search found no term; this does not establish that no alternative authoritative grounding exists.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native/source/status/history was edited. Optional links, tags and notes were checked against dihydromocimycin.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T144610Z-dihydromocimycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Dihydromocimycin: wrong pyridone saturation in the imported structure'
started_at: '2026-10-21T14:27:14Z'
finished_at: '2026-10-21T14:46:10Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent reviewer read the whole native record and exact
    ARO/PubChem rows after verifying original inputs, calculated the full graph and
    targeted bond change, inspected current authority responses, both adopted original-paper
    scopes and the original patent structure/characterization/antibacterial tables.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: 'The native graph reproduces its PubChem source but contradicts the original
  characterization of dihydromocimycin: its pyridone C5-C6 bond is unsaturated and
  its formula has two hydrogens too few. The original patent explicitly establishes
  the saturated bond, distinguishes mocimycin, and supports production by Streptomyces
  ramocissimus CBS190.69 plus bounded antibacterial activity. One identity blocker
  and one minor definition-citation problem require maintained-source curation.'
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
  - path: data/antibiotics/antibacterial/dihydromocimycin.yaml
    sha256: 10faac0a353e8aa7fb9ac8e938988a0716d5b718869f97d154abaff9c5bede9b
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
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
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: antibioticmech:aro-6e963f402b
  path: data/antibiotics/antibacterial/dihydromocimycin.yaml
  label: dihydromocimycin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO identity, definition and adopted citation owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Minted exact graph and chemical xref owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure retrieval
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 366; one exact record. All 13 original input hashes are
    preserved within 25 expanded source/context inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-6e963f402b
checks:
- check_id: structured-adapter
  name: Structured-source applicability
  status: not_applicable
  required: false
  target_ids:
  - antibioticmech:aro-6e963f402b
  summary: No native named gene, molecular protein target, pathway or transcriptomic
    assertion is present. No iModulon evidence was used to infer a molecular mechanism
    from elfamycin class membership.
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-6e963f402b
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/366367-focused.py
    (cwd /private/tmp/antibioticmech-record-reviews-037)
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
  - antibioticmech:aro-6e963f402b
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/dihydromocimycin.yaml (cwd /private/tmp/antibioticmech-record-reviews-037)
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
  - antibioticmech:aro-6e963f402b
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/dihydromocimycin.yaml --out /private/tmp/am-review-session/366-strict.tsv
    (cwd /private/tmp/antibioticmech-record-reviews-037)
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
  - antibioticmech:aro-6e963f402b
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
  - antibioticmech:aro-6e963f402b
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
  - antibioticmech:aro-6e963f402b
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
  - antibioticmech:aro-6e963f402b
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
  - antibioticmech:aro-6e963f402b
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
  - antibioticmech:aro-6e963f402b
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
  - antibioticmech:aro-6e963f402b
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
  - antibioticmech:aro-6e963f402b
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
  - antibioticmech:aro-6e963f402b
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/dihydromocimycin.yaml
  locator: 'Complete native record: definition/source, parent/class, full graph, two
    xrefs, one source concept and three history events'
  accessed_at: '2026-10-21T14:43:13Z'
  support: supports
  summary: The MINTED/SEEDED ARO record calls the material dihydromocimycin and cites
    PMID2272911 for production by S. ramocissimus CBS190.69. Its PubChem-derived graph
    is C43H60N2O12. No synonym, mode, molecular target, resistance, activity_spectrum,
    clinical product, producer object, causal graph or dataset assertion is populated.
  snapshot_sha256: 8dba1c940ffb355facf80886400db93a2427ae7038f62074a99ac2dcfb60e542
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv
  locator: ARO row229 and PubChem row63; extractor/enrichment/seeder ownership
  accessed_at: '2026-10-21T14:43:13Z'
  support: supports
  summary: The actual ARO row supplies the definition, two literature references and
    CID54679334. The corresponding PubChem row supplies all structure fields. The
    seeder selects the first definition reference and uses the broad elfamycin class
    as the parent. Initial captures were retained and actual ARO/PubChem owners added;
    the ChEBI table contains no exact-name row in this inspected source snapshot.
  snapshot_sha256: 8dba1c940ffb355facf80886400db93a2427ae7038f62074a99ac2dcfb60e542
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit2026.03.5 using batch019 interpreter against batch037
    cwd
  locator: 366-chemistry.json
  accessed_at: '2026-10-21T14:43:13Z'
  support: supports
  summary: Both native encodings reproduce LWXUPCAADQWXRE-UPMFUDSQSA-N, neutral C43H60N2O12,
    11 assigned centres, masses and the ARO source mint. Internal agreement does not
    establish that the graph represents the named natural product.
  snapshot_sha256: 1246d70c929c593bc816eacf459eddf9e2b4469b9dbe799b41ef970f2ce9fd8e
- evidence_id: aro
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3001248
  locator: Current ARO:3001248 complete term, definition references and PubChem cross-reference
  accessed_at: '2026-10-21T14:40:00.315508Z'
  support: supports
  summary: Current ARO repeats the native name, producer statement, two PMID citations
    and PubChem54679334 link. The term is not obsolete. This confirms source propagation,
    not the correctness of the linked molecular graph.
  snapshot_sha256: fc47ca7424286597afbdec11ab6b025e3be0792cc3ace204deed814d33210221
- evidence_id: parent
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3001219
  locator: Current ARO:3001219 elfamycin antibiotic
  accessed_at: '2026-10-21T14:40:00.319995Z'
  support: supports
  summary: The parent resolves as the broader elfamycin antibiotic class. Class membership
    does not imply that the particular compound has a demonstrated EF-Tu target or
    that an unsaturated analogue is chemically equivalent.
  snapshot_sha256: 062102bcad4324c79e0f537e00f5eddaa8dd2933038cd2597518306ca426058e
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/54679334/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: CID54679334 current complete structure properties
  accessed_at: '2026-10-21T14:40:00.322769Z'
  support: supports
  summary: Current PubChem reproduces the native C43H60N2O12 graph and key. The separate
    synonym route returned 404, so no independently readable current PubChem name
    list established the dihydromocimycin assignment. The structural mismatch is inherited
    from the adopted ARO-to-PubChem mapping.
  snapshot_sha256: 2ba37fa7e4a3b72c13fe8f9ba984906f3064f598e11498465a73852330aee2b7
- evidence_id: adopted1990
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.43.1349
  locator: PMID2272911; original abstract, producer/material Methods, Discussion/Table7
    at printed page1355 and reference31; actual Table7 viewed
  accessed_at: '2026-10-21T14:40:25.583957Z'
  support: supports
  summary: The experiments concern SB22484 from Streptomyces sp. NRRL15496. Dihydromocimycin
    is a literature comparator in Table7, with molecular weight 798 versus kirromycin(mocimycin)
    796 and a patent reference. The paper does not report the native CBS190.69 producer
    experiment; its SB22484 activities cannot be transferred. Its comparator mass
    independently agrees with the original dihydromocimycin patent.
  snapshot_sha256: 346c954a9ba13566841acc81726152fd0d4ea8d25d1849d011a81e19efe9e74c
- evidence_id: adopted1986
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.39.1361
  locator: PMID3781906; original abstract/Introduction and relevant material, activity
    and reference6 scope
  accessed_at: '2026-10-21T14:40:25.586394Z'
  support: context_only
  summary: The original study isolates L-681,217. Dihydromocimycin appears in the
    Introduction as a related antibiotic with a patent citation. Its exact producer,
    structure and antibacterial assays were not newly established in this paper. The
    L-681,217 or mocimycin growth-promotion results are not dihydromocimycin evidence.
  snapshot_sha256: b2904f46382e4907d593e11b454ea4a825d07211bef16238d334df7da5149592
- evidence_id: patent-identity
  kind: primary_source
  reference: https://patents.google.com/patent/US4062948A/en
  locator: 'Original US4062948 scan PDF page11, printed columns9-10: actual structural
    formula and elemental analysis; page12 column11 chemical proof'
  accessed_at: '2026-10-21T14:41:05.565654Z'
  support: supports
  summary: The patent explicitly distinguishes dihydromocimycin from mocimycin by
    saturation of pyridone C5-C6. The actual drawing shows this single bond. Elemental
    analysis is calculated for C43H62N2O12·2H2O; the parent molecule therefore has
    H62, not H60. Replacement of two olefinic doublets by methylene triplets and degradation
    to beta-alanine support the assignment. Hydration does not explain a two-hydrogen
    change with unchanged oxygen count.
  snapshot_sha256: 63a027e6a9be65f204ad86bad1ce90189777344a25bd051e50b54784d2da1664
- evidence_id: atom-map
  kind: validation
  reference: Scratch bond-order comparison; native graph left untouched
  locator: 366-saturation-check.json; zero-based RDKit atom mapping of native SMILES
  accessed_at: '2026-10-21T14:43:13Z'
  support: supports
  summary: The ring is N33-C34(=O)-C28-C29(=O)-C31=C32-N33. Thus patent pyridone positions5/6
    map to atoms31/32, which are both CH with a double bond in the native graph. Changing
    only that bond to single in scratch yields C43H62N2O12 and ATKFZHHCPMJIBV-UPMFUDSQSA-N.
    This diagnoses the missing hydrogenation; it is not a fully adjudicated replacement
    tautomer/stereostructure.
  snapshot_sha256: 6271a5558065e00f6ee892d2a9acacd6a4b2f8feb9a3810e32dae82bc65d36be
- evidence_id: patent-producer
  kind: primary_source
  reference: https://patents.google.com/patent/US4062948A/en
  locator: Dihydromocimycin section, printed columns12-14; fermentation and separation
    paragraphs
  accessed_at: '2026-10-21T14:40:25.588413Z'
  support: supports
  summary: The original patent identifies S. ramocissimus CBS190.69 and distinguishes
    co-produced mocimycin from dihydromocimycin by controlled precipitation, chromatography
    and spectroscopic characterization. It describes increased dihydromocimycin yield
    with aeration. The native producer statement is substantively supported here,
    but the populated PMID is not this primary experiment.
  snapshot_sha256: 2893d3e87de40d84fe4caa0c6f262226ef9d879ea6e26f148123208c8ad35c11
- evidence_id: patent-activity
  kind: primary_source
  reference: https://patents.google.com/patent/US4062948A/en
  locator: Original scan PDF page12, printed column12; actual paired agar/liquid dilution
    MIC tables
  accessed_at: '2026-10-21T14:41:05.565654Z'
  support: supports
  summary: The tables contain separate mocimycin and dihydromocimycin columns. Dihydromocimycin
    agar MICs include Diplococcus pneumoniae L54 <0.75 and Listeria monocytogenes
    A2130 1.5 micrograms/mL; liquid dilution includes B. subtilis ATCC6633 50 micrograms/mL.
    Agar culture is explicitly anaerobic. Full medium/incubation and exact preparation
    salt/hydrate for these paired assays are not supplied locally. Earlier TableII
    and its detailed method belong to mocimycin and must not be borrowed. These data
    establish activity of characterized dihydromocimycin, not the incorrect native
    unsaturated graph.
  snapshot_sha256: 63a027e6a9be65f204ad86bad1ce90189777344a25bd051e50b54784d2da1664
- evidence_id: patent-boundaries
  kind: primary_source
  reference: https://patents.google.com/patent/US4062948A/en
  locator: Dihydromocimycin separation, therapeutic claims and dehydrogenation sections
  accessed_at: '2026-10-21T14:40:25.588413Z'
  support: context_only
  summary: The patent discusses free acid, salts and hydration separately and chemically
    converts dihydromocimycin to mocimycin. It explicitly distinguishes their animal
    growth-promotion behavior. Patent therapeutic language is not a regulatory approval
    or independently verified clinical efficacy claim; derivative/salt use does not
    establish the neutral record as a formulation.
  snapshot_sha256: 2893d3e87de40d84fe4caa0c6f262226ef9d879ea6e26f148123208c8ad35c11
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local search and official authority/primary discovery
  locator: 366367-local-focused.txt;366-discovery.json;366-chebi-search.json
  accessed_at: '2026-10-21T14:40:00.976032Z'
  support: context_only
  summary: The exact native key occurs in the adopted PubChem row and this native
    record in the searched local source/review surfaces. Current official ChEBI exact-name
    search returned no term for dihydromocimycin. This supports preserving an explicit
    minted-identity workflow, not automatic substitution of a near-name compound.
    Public patent discovery supplied the primary identity and activity evidence.
  snapshot_sha256: bfddf5725dae4bb6d39fa69d6378319cfe2660c973230562215b5a58f8675d84
  search_scope: 2026-10-21; dihydromocimycin, ARO:3001248, PubChem54679334, both adopted
    PMIDs, exact native InChIKey and original patent leads. Local reference and exact-key
    searches included ignored and hidden files under data, curation, conf, src, scripts,
    reports and reviews. Official ChEBI exact-name search was bounded to that spelling;
    no universal ontology absence is claimed.
- evidence_id: gates
  kind: validation
  reference: Focused schema, strict and standalone chemistry
  locator: 366-focused-results.json
  accessed_at: '2026-10-21T14:43:13Z'
  support: supports
  summary: All focused gates exit 0 despite the wrong named-structure assignment.
    Native checks used batch037; standalone chemistry used batch019 RDKit against
    batch037 cwd.
  snapshot_sha256: ef86772842b5290afc65712f7f6e363b6cf97eca2a001f96ef23cdde6072b379
assessments:
- assessment_id: identity
  area: identity
  topic: Exact named molecule versus stored graph
  outcome: concern
  summary: The original saturated dihydromocimycin structure is incompatible with
    the native pyridone double bond and H60 formula. Internal encoding agreement and
    current PubChem propagation cannot resolve the mismatch. This is a wrong-identity
    blocker.
  target_ids:
  - antibioticmech:aro-6e963f402b
  evidence_ids:
  - patent-identity
  - atom-map
  - chemistry
  - pubchem
  - adopted1990
- assessment_id: grounding
  area: grounding
  topic: Minted ARO identity and chemical xrefs
  outcome: concern
  summary: The ARO concept and broader class resolve, but its PubChem equivalence
    supplies a graph with the wrong hydrogenation state. Recover the exact intended
    structure before selecting any corrected chemical grounding; do not replace it
    with a similarly named elfamycin.
  target_ids:
  - antibioticmech:aro-6e963f402b
  evidence_ids:
  - aro
  - parent
  - pubchem
  - patent-identity
  - owners
- assessment_id: classification
  area: scope
  topic: Antibacterial eligibility and class
  outcome: supported
  summary: The characterized natural compound belongs to the elfamycin family and
    has original antibacterial dilution results. This supports intended-compound eligibility
    but does not repair the identity of the current graph.
  target_ids:
  - antibioticmech:aro-6e963f402b
  evidence_ids:
  - patent-activity
  - patent-identity
  - parent
  - adopted1990
- assessment_id: definition
  area: evidence
  topic: Producer statement and definition citation
  outcome: concern
  summary: The producer/strain statement is supported by the original patent. PMID2272911
    instead reports SB22484 and only lists dihydromocimycin as a comparator; the seeded
    first-reference choice does not support the exact producer assertion.
  target_ids:
  - antibioticmech:aro-6e963f402b
  evidence_ids:
  - patent-producer
  - adopted1990
  - adopted1986
  - owners
- assessment_id: activity
  area: completeness
  topic: Optional activity_spectrum
  outcome: supported
  summary: Bounded dihydromocimycin assay rows are available after identity correction.
    No quantitative row should be attached to the current unsaturated graph or assigned
    unreported material/medium details. Optional absence is not a required-field defect.
  target_ids:
  - antibioticmech:aro-6e963f402b
  evidence_ids:
  - patent-activity
  - patent-boundaries
- assessment_id: mode
  area: completeness
  topic: Absent mechanism, targets and resistance
  outcome: unknown
  summary: No such native claim is populated. Elfamycin class context alone does not
    establish the exact-compound molecular target or resistance alleles. The patent
    supplies phenotypes and chemistry, not a direct-target experiment.
  target_ids:
  - antibioticmech:aro-6e963f402b
  evidence_ids:
  - native
  - parent
  - patent-activity
- assessment_id: leads
  area: evidence
  topic: Both adopted primary-paper leads
  outcome: supported
  summary: Both originals were inspected at their relevant material/Introduction/comparator/reference
    scope. Their main experiments concern other antibiotics; neither was silently
    converted to exact dihydromocimycin assay evidence.
  target_ids:
  - antibioticmech:aro-6e963f402b
  evidence_ids:
  - adopted1990
  - adopted1986
- assessment_id: other
  area: scope
  topic: Clinical products, producer objects, graph and datasets
  outcome: not_applicable
  summary: No structured assertions of these kinds occur. The definition contains
    a supported producer claim requiring the correct citation; patent formulation/therapeutic
    statements do not establish a clinical product or causal graph.
  target_ids:
  - antibioticmech:aro-6e963f402b
  evidence_ids:
  - native
  - patent-producer
  - patent-boundaries
- assessment_id: provenance
  area: provenance
  topic: Source merge, status and history
  outcome: supported
  summary: The ARO mint, source version and three generated events reproduce. The
    original 13 inputs remain unchanged and actual PubChem/ARO ownership is captured.
    SEEDED status is retained.
  target_ids:
  - antibioticmech:aro-6e963f402b
  evidence_ids:
  - native
  - owners
  - chemistry
- assessment_id: schema
  area: schema
  topic: Deterministic checks versus scientific identity
  outcome: supported
  summary: Schema, strict and structure-consistency checks pass; the source-level
    chemical identity defect is outside those checks. Shared same-base corpus gates
    are attached by root.
  target_ids:
  - antibioticmech:aro-6e963f402b
  evidence_ids:
  - gates
  - chemistry
  - patent-identity
findings:
- finding_id: F1
  issue_key: dihydromocimycin-wrong-pyridone-hydrogenation
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The stored graph lacks the defining pyridone hydrogenation
  description: Native SMILES/InChI encode C5=C6 in the pyridone ring and C43H60N2O12.
    The original dihydromocimycin drawing and chemical proof require a saturated C5-C6
    bond and parent C43H62N2O12. This is a constitutional hydrogenation-state mismatch,
    not a tautomer or hydrate difference. Current PubChem54679334 repeats the incorrect
    graph. Curate the exact named natural structure and its cross-reference through
    maintained inputs before any assay enrichment.
  target_ids:
  - antibioticmech:aro-6e963f402b
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  - chemical_structure.molecular_formula
  - chemical_structure.average_mass
  - chemical_structure.monoisotopic_mass
  - xrefs[1]
  evidence_ids:
  - native
  - patent-identity
  - atom-map
  - pubchem
  - adopted1990
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Incorrect exact PubChem assignment
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Propagated graph, formula and masses
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Source structure retrieval
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible native generation
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Publication-backed exact structure route if required
  rule_id: review-checklist:Identity/Structure/Equivalence
  native_severity: blocker
  normalization_reason: The native rubric defines a wrong chemical identity as blocker
    even when encodings and deterministic gates agree.
- finding_id: F2
  issue_key: dihydromocimycin-producer-definition-citation
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The definition points to a comparator paper instead of the producer experiment
  description: PMID2272911 reports SB22484 from NRRL15496 and lists dihydromocimycin
    only as a literature comparator. It does not directly support S. ramocissimus
    CBS190.69 production. The original dihydromocimycin patent does support that statement.
    Correct the evidence pointer without discarding the substantiated producer fact.
  target_ids:
  - antibioticmech:aro-6e963f402b
  field_paths:
  - definition_source
  evidence_ids:
  - owners
  - adopted1990
  - adopted1986
  - patent-producer
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Definition and ordered source references
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO definition provenance extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Definition-source selection
  rule_id: review-checklist:Evidence/Producer
  native_severity: minor
  normalization_reason: A bounded provenance mismatch for a statement independently
    supported by original evidence; distinct from the blocking structure defect.
actions:
- action_id: A1
  description: Resolve and regenerate the exact dihydromocimycin structure and equivalent
    chemical links.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-6e963f402b
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Incorrect exact PubChem assignment
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Propagated graph, formula and masses
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Source structure retrieval
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible native generation
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Publication-backed exact structure route if required
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Reconcile the original saturated pyridone, full tautomer/stereochemistry and parent
    C43H62N2O12; distinguish free acid from salts/hydrates.
  - Do not use the scratch bond-repair graph as an automatically accepted full replacement;
    confirm every remaining stereochemical and connectivity assignment.
  - Remove or correct any exact xref whose independently retrieved structure retains
    the C5=C6 bond.
  - Recalculate SMILES/InChI/key, formula, charge and masses together and run schema,
    strict, source provenance and corpus-reproduction checks.
- action_id: A2
  description: Attach the producer statement to the original evidence through maintained
    definition provenance.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-6e963f402b
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Definition and ordered source references
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO definition provenance extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Definition-source selection
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - The regenerated definition_source resolves to inspected evidence for CBS190.69
    production of dihydromocimycin.
  - Retain the adopted1990/1986 papers only at their actual comparator/discovery scope.
  - Keep mocimycin-only assays, growth promotion and earlier patent tables separate
    from dihydromocimycin.
limitations:
- The original patent structure, elemental analysis, chemical proof and paired antibacterial
  tables were inspected as actual scan images. The full stereochemical identity of
  a corrected replacement graph has not been adjudicated; the scratch saturation calculation
  is diagnostic only.
- Both adopted papers were read at their relevant compound/material, comparator, Introduction/Discussion
  and reference scope; unrelated SB22484/L-681,217 assay tables were not transferred
  or exhaustively reanalyzed.
- The patent distinguishes salts, a hydrated analytical specimen, neutral material
  and mixtures. Exact preparation form and full conditions for the dihydromocimycin
  paired dilution tables are incompletely specified; earlier mocimycin assay methods
  are not assumed to apply.
- Current PubChem structure data resolve, but its synonym endpoint returned 404. The
  bounded official ChEBI exact-name search found no term; this does not establish
  that no alternative authoritative grounding exists.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native/source/status/history was edited. Optional links, tags and notes were
  checked against dihydromocimycin.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://card.mcmaster.ca/ontology/3001248
- https://pubchem.ncbi.nlm.nih.gov/compound/54679334
- https://patents.google.com/patent/US4062948A/en
- https://doi.org/10.7164/antibiotics.43.1349
tags:
- dihydromocimycin
- elfamycin
- chemical-identity
- pyridone-hydrogenation
```
