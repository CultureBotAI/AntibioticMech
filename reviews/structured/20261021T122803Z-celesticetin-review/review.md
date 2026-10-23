# Celesticetin: unresolved stereochemical identity across exact references

- Review: 20261021T122803Z-celesticetin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:02:30Z
- Finished UTC: 2026-10-21T12:28:03Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One major identity finding: the native PubChem-derived graph leaves all eight stereocentres unspecified, while its exact ChEBI reference specifies six and natural celesticetin is depicted as stereodefined in original literature. Resolve the intended exact structure before changing the graph or source grounding. The two resistance edges are faithfully attributed database assertions; their underlying sources have material limits, including an upstream LmrC homonym conflation.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position267; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-94c19a1c3c | data/antibiotics/antibacterial/celesticetin.yaml | generated | celesticetin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-94c19a1c3c | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-94c19a1c3c | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-94c19a1c3c | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-94c19a1c3c | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-94c19a1c3c | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-94c19a1c3c | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-94c19a1c3c | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-94c19a1c3c | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-94c19a1c3c | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-94c19a1c3c | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-94c19a1c3c | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-94c19a1c3c | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Native exact structure versus cited ChEBI identity

identity: concern. Targets: antibioticmech:aro-94c19a1c3c.

Connectivity, composition and mass agree, but the native all-unspecified stereo graph and six-defined-centre ChEBI mapping are not the same exact representation. Natural stereodefined material requires a separately verified identity decision.

### Lincosamide class and antibacterial filing

grounding: supported. Targets: antibioticmech:aro-94c19a1c3c.

The parent is broader than the compound and original cell inhibition supports antibacterial filing. Neither proves exact solid form or all absolute configurations.

### Producer and niddamycin clause

evidence: unknown. Targets: antibioticmech:aro-94c19a1c3c.

S. caelestis production is directly supported in 2017 culture/isolation methods. The niddamycin clause remains source-attributed but independently unverified because its cited 1968 full paper was unavailable.

### Attributed ErmV target alteration

evidence: supported. Targets: antibioticmech:aro-94c19a1c3c.

The native database assertion matches CARD and the methylase mechanism family. Original exact-strain celesticetin resistance endpoints are not independently established at the inspected abstract depth.

### LmrC source identity and exact-drug scope

evidence: unknown. Targets: antibioticmech:aro-94c19a1c3c.

The imported relation is faithfully attributed, but upstream Lactococcus membrane-transporter and Streptomyces ABCF identities are conflated. Inspected primary sources do not resolve exact celesticetin target protection; preserve provenance and seek exact protein/assay support.

### All six adopted source and parent leads

evidence: supported. Targets: antibioticmech:aro-94c19a1c3c.

Each adopted source lead has a declared abstract/metadata disposition; additional original studies supply bounded producer/activity and homonym context.

### Maintained owners and original captures

provenance: supported. Targets: antibioticmech:aro-94c19a1c3c.

All 18 input hashes and three native history events remain intact. Actual PubChem enrichment owner is included alongside ARO inventories.

### Unpopulated primary targets, activity, clinical and graph content

completeness: not_applicable. Targets: antibioticmech:aro-94c19a1c3c.

Optional omissions are not defects. Biosynthetic enzymes, inhibition zones and MICs remain distinct from direct antibacterial target experiments.

## Findings

### F1: Exact cross-reference disagrees with the native stereochemical specification

major / open / confirmed; issue key: celesticetin-incompatible-exact-stereochemical-groundings.

The native PubChem CID 220087 graph leaves all eight stereocentres unspecified and yields VMSQKUCYEMOKMM-UHFFFAOYSA-N. Asserted exact CHEBI:156421 instead defines six centres and yields VMSQKUCYEMOKMM-AFJAYNRNSA-N. Original natural celesticetin is stereodefined, while CID 20054860 is an eight-defined-centre candidate requiring atom-level verification. Resolve the intended exact compound and correct the source-owned graph/crosswalk together; do not call the current unspecified graph a racemate or silently adopt a candidate.

## Recommended Actions And Acceptance Checks

### A1

Resolve natural celesticetin stereochemistry and make source-owned identity, structure and exact cross-references agree.

- Atom-map original stereochemical evidence to the complete candidate graph, retaining any unresolved centres explicitly.
- Do not infer racemic composition from unspecified stereochemistry or equate connectivity-only keys.
- Use maintained PubChem/ARO extraction or grounding adjudication that survives reseeding; reassess minted identity if the intended grounding changes.
- Keep the 1973 hydrochloride comparator and 2017 unspecified final solid-form assays separately scoped.
- Rerun independent full-graph calculations, exact-reference, schema, strict, provenance and reproduction gates after separately authorized curation.

### A2

Resolve the upstream LmrC homonym/citation conflation before adding exact celesticetin primary resistance evidence.

- Distinguish S. lincolnensis cytosolic ABCF LmrC from L. lactis YdaG/LmrC plus YdbA/LmrD membrane transporter.
- Seek a direct celesticetin assay for the exact protein and strain; retain database attribution until that scope is resolved.
- Do not remove a biologically possible resistance relationship solely because inspected papers tested other substrates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/celesticetin.yaml; Entire YAML | supports | Read minted ARO identifier, class/status, definition with source PMID, lincosamide parent/class, full PubChem structure/masses, four exact references, source concept, both resistance assertions and all three history events. No synonyms, primary molecular targets, quantitative activity or causal graph are populated. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; data/raw/aro_resistance_edges.tsv; scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py; ARO molecule row 219, PubChem row 57, resistance rows 3888-3889; enrichment and seed code | supports | The ARO inventory supplies identity, definition and crosswalks; PubChem supplies an unassigned-stereo graph. Both resistance entries match their adopted rows. Original captures are preserved and all 18 expanded input hashes are unchanged. |
| chemistry | Independent RDKit 2026.03.5 molecular calculations; 267-chemistry.json | supports | Native SMILES and InChI generate VMSQKUCYEMOKMM-UHFFFAOYSA-N, C24H36N2O9S, neutral one-component material and eight unassigned stereocentres. Masses and ARO source mint reproduce. Unspecified centres do not mean a racemate. |
| pubchem-native | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/220087/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON; CID 220087 complete structure | supports | Current CID 220087 matches the native unassigned-stereo structure exactly. It does not independently establish the full configuration of natural celesticetin. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:156421; Current complete SMILES, InChI and InChIKey | refutes | The asserted exact ChEBI reference instead yields VMSQKUCYEMOKMM-AFJAYNRNSA-N and specifies six of eight centres. The molecular connectivity agrees, but stereochemical identity is narrower than the native graph. Its two remaining unspecified centres mean that simply substituting this graph would still leave a natural-product identity question. |
| pubchem-candidate | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/20054860/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON; Celesticetin A, complete eight-centre candidate | context_only | This database candidate specifies all eight centres and gives VMSQKUCYEMOKMM-PBZRRIJCSA-N. It is a curation lead, not an approved replacement: a full atom mapping to original natural-product stereochemistry has not been completed. |
| xref-calculation | Independent external structure parsing; 027-root-xref-check.json, target 267 | supports | Both SMILES and InChI from each authority independently confirm the three different stereochemical specification levels: native CID 220087 zero, ChEBI six, candidate CID 20054860 eight assigned centres. |
| card | https://card.mcmaster.ca/aro/3001231; Current identity, class, producer definition and publication | supports | Current CARD reproduces the native crosswalks, lincosamide class and S. caelestis/niddamycin definition with PMID 5638307. ARO is a source concept, not an independently stereodefined chemical structure. |
| erm-card | https://card.mcmaster.ca/aro/3002824; ErmV definition, relation and references | supports | Current CARD gives ErmV/ermSV as a 23S rRNA methyltransferase and explicitly links celesticetin resistance. Native target-alteration category matches this source; the record itself describes database rather than primary evidence. |
| lmr-card | https://card.mcmaster.ca/aro/3002881; Definition, ydaG synonym, reference and reference protein model | partial | Current CARD mixes S. lincolnensis ABCF LmrC with Lactococcus lactis LmrCD membrane-transporter language and cites the Lactococcus distribution study. The native edge faithfully reports the source category, but the external source identity/citation conflation prevents treating that citation as exact celesticetin ribosomal-protection proof. |
| lead-5638307 | PMID:5638307; 267-core.json; complete abstract where available, otherwise metadata only | context_only | The 1968 celesticetin structure paper (DOI 10.1021/ja01005a036) was resolved bibliographically. No abstract or full original text was obtained; the native niddamycin co-production clause remains independently unverified, not proven false. |
| lead-6163765 | PMID:6163765; 267-core.json; complete abstract where available, otherwise metadata only | context_only | Complete abstract describes inducible macrolide/lincosamide/streptogramin resistance and rRNA adenine methylation in Streptomyces strains. It supports the mechanism family, but does not by itself provide a complete exact celesticetin/ErmV strain MIC assay. |
| lead-9055987 | PMID:9055987; 267-core.json; complete abstract where available, otherwise metadata only | context_only | Complete abstract of ermSV induction work distinguishes reporter induction by antibiotics from direct susceptibility or binding measurements. Celesticetin induction is not converted into a quantitative resistance endpoint. |
| lead-16958846 | PMID:16958846; 267-core.json; complete abstract where available, otherwise metadata only | context_only | Complete abstract examines multidrug-resistance gene diversity in Lactococcus lactis, including lmrCD. This is not a direct Streptomyces ABCF LmrC-celesticetin target-protection experiment. |
| lead-10582867 | PMID:10582867; 267-core.json; complete abstract where available, otherwise metadata only | context_only | The adopted parent-level methylase nomenclature paper was resolved bibliographically without an abstract; it provides classification context only. |
| lead-15135500 | PMID:15135500; 267-core.json; complete abstract where available, otherwise metadata only | context_only | The complete parent-associated abstract concerns pneumococcal ribosomal mutants and other macrolide/lincosamide antibiotics. It is not exact celesticetin strain/material evidence. |
| primary2017 | PMID:28507704; DOI:10.1039/c6sc04235j; Full original main text; Fig.1 and Fig.5 visually inspected by source reader, Fig.1 independently checked by coordinator | supports | Original biosynthetic work depicts stereodefined celesticetin and tests isolated natural compound against Kocuria rhizophila. It reports MIC 1600 nM and a 19-mm inhibition zone. Ccb1/Ccb2 are producer biosynthetic enzymes, not antibacterial targets. The drawing demonstrates configuration matters but has not been atom-mapped to the proposed replacement database graph. |
| primary2017-si | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5416915/supplementaryFiles; Original SI pp.1-3 and 5, recovered from EPMC supplementary archive | partial | SI describes production and isolation from S. caelestis ATCC15084 culture broth. Diffusion used 5 nmol on 5-mm discs, 37 degrees C for 20 h; liquid MIC used 5 microlitres of a 0.5 McFarland K. rhizophila suspension in 1 mL LB containing 25-1600 nM compound, 37 degrees C for 24 h. No Kocuria strain accession or exact counterion/hydrate of final assay solid is established. |
| primary1973 | https://doi.org/10.7164/antibiotics.26.7; Full original text pp.7-14; Table 2 visually inspected by source reader | partial | The congener study explicitly uses celesticetin HCl as comparator, including S. aureus UC80 MIC 2 micrograms/mL and E. coli UC51 &gt;500. Twofold dilution in brain-heart infusion broth, 37 degrees C for 20 h. These hydrochloride measurements must not be silently relabeled as unsalted native-solid observations. |
| lmr2021 | PMID:34488446; DOI:10.1128/mbio.01731-21; Original Results, Discussion, strain/culture/MIC methods and all celesticetin body occurrences; source-reader report | partial | S. lincolnensis ATCC25466 LmrC is a cytosolic ABCF ATPase with lincomycin/clindamycin resistance and biosynthetic regulation experiments. Celesticetin appears in S. caelestis production comparisons, not an identified LmrC-mediated celesticetin resistance assay. Absence of that endpoint in this paper is not biological proof that LmrC cannot protect against celesticetin. |
| lmr2004 | PMID:15192086; DOI:10.1074/jbc.M404072200; Original full paper pp.34449-34455, Table II and renaming passage; source-reader inspection | partial | L. lactis YdaG/YdbA, renamed LmrC/LmrD, are membrane half-transporters with six predicted transmembrane helices each and a nucleotide-binding domain. The study uses IL1403 genes and NZ9000 expression, with ethidium/BCECF-AM/daunomycin/Hoechst transport substrates. This establishes a distinct homonym, not the Streptomyces cytosolic ABCF protein or direct celesticetin transport. |
| reader | Collaborative primary-source inspection report; 267-source-reader-report.json | context_only | The report records exact locators, source hashes, timestamps, primary observations, figure checks and failed routes. Original 1968 structure and full 1991 ribosome work remain unavailable; no all-eight-centre replacement assignment or niddamycin co-production confirmation is claimed. |
| adapter | Installed kg-microbe-sources imodulondb adapter; 027-root-imodulondb-datasets.txt | context_only | Structured dataset discovery preceded open protein/pathway research. The queried catalog lacks the exact Streptomyces/Lactococcus species needed for these assertions; no unrelated reference species was substituted. Catalog coverage is not evidence about resistance or absence of a mechanism. |

## Limits And Additional Notes

- The original 1968 structure determination remained unavailable; full all-eight-centre atom mapping was not completed. The eight-defined-centre PubChem entry is a lead only.
- Niddamycin co-production remains independently unverified; this access limit is not treated as a proven native factual error.
- ErmV source papers were inspected at abstract depth; LmrC exact celesticetin phenotype remains unresolved despite primary homonym clarification.
- Full 1991 ribosome paper and 2006 Lactococcus distribution paper were unavailable. The latter complete abstract was inspected. No exhaustive resistance literature search is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All initial input hashes were retained when actual owners were appended; no native/source/history/status edits occurred.
- The source reader inspected the cited full primary texts and SI at explicit locators; the coordinator independently checked the exact native record, full authority structures, original natural-product drawing and antibacterial results.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T122803Z-celesticetin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Celesticetin: unresolved stereochemical identity across exact references'
started_at: '2026-10-21T12:02:30Z'
finished_at: '2026-10-21T12:28:03Z'
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
summary: 'One major identity finding: the native PubChem-derived graph leaves all
  eight stereocentres unspecified, while its exact ChEBI reference specifies six and
  natural celesticetin is depicted as stereodefined in original literature. Resolve
  the intended exact structure before changing the graph or source grounding. The
  two resistance edges are faithfully attributed database assertions; their underlying
  sources have material limits, including an upstream LmrC homonym conflation.'
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
  - path: curation/curator_antibiotics.tsv
    sha256: 224cbb7261add427184b2762a29c2ff3e85c85e0a06cf22b144545346487247b
    role: context
  - path: curation/decisions.tsv
    sha256: a5834b44307b0449b0df9362c551b7fcd707f3ae51f73d429d37d51f5a169d61
    role: context
  - path: data/antibiotics/antibacterial/celesticetin.yaml
    sha256: dd62c5c221873c28e02e8f01e30938c9d52553dd51ba05566c4dec4fc9394515
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
- target_id: antibioticmech:aro-94c19a1c3c
  path: data/antibiotics/antibacterial/celesticetin.yaml
  label: celesticetin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual maintained source or transform for this record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Actual maintained source or transform for this record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual maintained source or transform for this record
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Actual maintained source or transform for this record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Actual PubChem structure enrichment owner; captured before inspection
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position267; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-94c19a1c3c
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-94c19a1c3c
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    267
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-94c19a1c3c
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/celesticetin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-94c19a1c3c
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/celesticetin.yaml --out /private/tmp/am-review-session/267-strict.tsv
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
  - antibioticmech:aro-94c19a1c3c
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
  - antibioticmech:aro-94c19a1c3c
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
  - antibioticmech:aro-94c19a1c3c
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
  - antibioticmech:aro-94c19a1c3c
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
  - antibioticmech:aro-94c19a1c3c
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
  - antibioticmech:aro-94c19a1c3c
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
  - antibioticmech:aro-94c19a1c3c
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
  - antibioticmech:aro-94c19a1c3c
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
  - antibioticmech:aro-94c19a1c3c
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/celesticetin.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T12:23:50Z'
  support: supports
  summary: Read minted ARO identifier, class/status, definition with source PMID,
    lincosamide parent/class, full PubChem structure/masses, four exact references,
    source concept, both resistance assertions and all three history events. No synonyms,
    primary molecular targets, quantitative activity or causal graph are populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; data/raw/aro_resistance_edges.tsv;
    scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py
  locator: ARO molecule row 219, PubChem row 57, resistance rows 3888-3889; enrichment
    and seed code
  accessed_at: '2026-10-21T12:23:50Z'
  support: supports
  summary: The ARO inventory supplies identity, definition and crosswalks; PubChem
    supplies an unassigned-stereo graph. Both resistance entries match their adopted
    rows. Original captures are preserved and all 18 expanded input hashes are unchanged.
  snapshot_sha256: b2de7ad1bbe75e427297f4688d8536dbbc701e5fde451902c959acb5011aa5f7
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit 2026.03.5 molecular calculations
  locator: 267-chemistry.json
  accessed_at: '2026-10-21T12:23:50Z'
  support: supports
  summary: Native SMILES and InChI generate VMSQKUCYEMOKMM-UHFFFAOYSA-N, C24H36N2O9S,
    neutral one-component material and eight unassigned stereocentres. Masses and
    ARO source mint reproduce. Unspecified centres do not mean a racemate.
  snapshot_sha256: fc1def76368e9d865fda0118987b3c3b4da80e6b918b5c469b17f2df8e242454
- evidence_id: pubchem-native
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/220087/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON
  locator: CID 220087 complete structure
  accessed_at: '2026-10-21T12:23:50Z'
  support: supports
  summary: Current CID 220087 matches the native unassigned-stereo structure exactly.
    It does not independently establish the full configuration of natural celesticetin.
  snapshot_sha256: 613c66172934a62e8892ebcf1a850daa7196cf6ad65e70a97926b8b8c33ce41b
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:156421
  locator: Current complete SMILES, InChI and InChIKey
  accessed_at: '2026-10-21T12:23:50Z'
  support: refutes
  summary: The asserted exact ChEBI reference instead yields VMSQKUCYEMOKMM-AFJAYNRNSA-N
    and specifies six of eight centres. The molecular connectivity agrees, but stereochemical
    identity is narrower than the native graph. Its two remaining unspecified centres
    mean that simply substituting this graph would still leave a natural-product identity
    question.
  snapshot_sha256: 24b93a459e62dbcb4e721990c2f3ab55663e322dc2060c78011fe989aefc8ab4
- evidence_id: pubchem-candidate
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/20054860/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON
  locator: Celesticetin A, complete eight-centre candidate
  accessed_at: '2026-10-21T12:23:50Z'
  support: context_only
  summary: 'This database candidate specifies all eight centres and gives VMSQKUCYEMOKMM-PBZRRIJCSA-N.
    It is a curation lead, not an approved replacement: a full atom mapping to original
    natural-product stereochemistry has not been completed.'
  snapshot_sha256: f11358d6bae7ff6dea7a141dbd5917b0d74f48725a50307f517420feb6437bb8
- evidence_id: xref-calculation
  kind: validation
  reference: Independent external structure parsing
  locator: 027-root-xref-check.json, target 267
  accessed_at: '2026-10-21T12:23:50Z'
  support: supports
  summary: 'Both SMILES and InChI from each authority independently confirm the three
    different stereochemical specification levels: native CID 220087 zero, ChEBI six,
    candidate CID 20054860 eight assigned centres.'
  snapshot_sha256: fae7157a323812f8e3eeb541fc3b030c11787e689fc5e413d94f2737984bbe2e
- evidence_id: card
  kind: authority
  reference: https://card.mcmaster.ca/aro/3001231
  locator: Current identity, class, producer definition and publication
  accessed_at: '2026-10-21T12:23:50Z'
  support: supports
  summary: Current CARD reproduces the native crosswalks, lincosamide class and S.
    caelestis/niddamycin definition with PMID 5638307. ARO is a source concept, not
    an independently stereodefined chemical structure.
  snapshot_sha256: a7e52a2f971eb18e0f4b11fb20a7ee0119af865526314f798955919189be849d
- evidence_id: erm-card
  kind: authority
  reference: https://card.mcmaster.ca/aro/3002824
  locator: ErmV definition, relation and references
  accessed_at: '2026-10-21T12:23:50Z'
  support: supports
  summary: Current CARD gives ErmV/ermSV as a 23S rRNA methyltransferase and explicitly
    links celesticetin resistance. Native target-alteration category matches this
    source; the record itself describes database rather than primary evidence.
  snapshot_sha256: 31be72abd4d45e7db5c0ee30b5f9b9927564dde13d6356830285e47ae1be7564
- evidence_id: lmr-card
  kind: authority
  reference: https://card.mcmaster.ca/aro/3002881
  locator: Definition, ydaG synonym, reference and reference protein model
  accessed_at: '2026-10-21T12:23:50Z'
  support: partial
  summary: Current CARD mixes S. lincolnensis ABCF LmrC with Lactococcus lactis LmrCD
    membrane-transporter language and cites the Lactococcus distribution study. The
    native edge faithfully reports the source category, but the external source identity/citation
    conflation prevents treating that citation as exact celesticetin ribosomal-protection
    proof.
  snapshot_sha256: 4516d106f5026973d661ccec9d3fdcd666cf13cfa20fb7a094d7c49c0d9eb723
- evidence_id: lead-5638307
  kind: primary_source
  reference: PMID:5638307
  locator: 267-core.json; complete abstract where available, otherwise metadata only
  accessed_at: '2026-10-21T12:23:50Z'
  support: context_only
  summary: The 1968 celesticetin structure paper (DOI 10.1021/ja01005a036) was resolved
    bibliographically. No abstract or full original text was obtained; the native
    niddamycin co-production clause remains independently unverified, not proven false.
  snapshot_sha256: 5b34444b8bbf806b4ef5a276389f3476885d4b7d0b1100077cf1be711c44a8ab
- evidence_id: lead-6163765
  kind: primary_source
  reference: PMID:6163765
  locator: 267-core.json; complete abstract where available, otherwise metadata only
  accessed_at: '2026-10-21T12:23:50Z'
  support: context_only
  summary: Complete abstract describes inducible macrolide/lincosamide/streptogramin
    resistance and rRNA adenine methylation in Streptomyces strains. It supports the
    mechanism family, but does not by itself provide a complete exact celesticetin/ErmV
    strain MIC assay.
  snapshot_sha256: 5b34444b8bbf806b4ef5a276389f3476885d4b7d0b1100077cf1be711c44a8ab
- evidence_id: lead-9055987
  kind: primary_source
  reference: PMID:9055987
  locator: 267-core.json; complete abstract where available, otherwise metadata only
  accessed_at: '2026-10-21T12:23:50Z'
  support: context_only
  summary: Complete abstract of ermSV induction work distinguishes reporter induction
    by antibiotics from direct susceptibility or binding measurements. Celesticetin
    induction is not converted into a quantitative resistance endpoint.
  snapshot_sha256: 5b34444b8bbf806b4ef5a276389f3476885d4b7d0b1100077cf1be711c44a8ab
- evidence_id: lead-16958846
  kind: primary_source
  reference: PMID:16958846
  locator: 267-core.json; complete abstract where available, otherwise metadata only
  accessed_at: '2026-10-21T12:23:50Z'
  support: context_only
  summary: Complete abstract examines multidrug-resistance gene diversity in Lactococcus
    lactis, including lmrCD. This is not a direct Streptomyces ABCF LmrC-celesticetin
    target-protection experiment.
  snapshot_sha256: 5b34444b8bbf806b4ef5a276389f3476885d4b7d0b1100077cf1be711c44a8ab
- evidence_id: lead-10582867
  kind: primary_source
  reference: PMID:10582867
  locator: 267-core.json; complete abstract where available, otherwise metadata only
  accessed_at: '2026-10-21T12:23:50Z'
  support: context_only
  summary: The adopted parent-level methylase nomenclature paper was resolved bibliographically
    without an abstract; it provides classification context only.
  snapshot_sha256: 5b34444b8bbf806b4ef5a276389f3476885d4b7d0b1100077cf1be711c44a8ab
- evidence_id: lead-15135500
  kind: primary_source
  reference: PMID:15135500
  locator: 267-core.json; complete abstract where available, otherwise metadata only
  accessed_at: '2026-10-21T12:23:50Z'
  support: context_only
  summary: The complete parent-associated abstract concerns pneumococcal ribosomal
    mutants and other macrolide/lincosamide antibiotics. It is not exact celesticetin
    strain/material evidence.
  snapshot_sha256: 5b34444b8bbf806b4ef5a276389f3476885d4b7d0b1100077cf1be711c44a8ab
- evidence_id: primary2017
  kind: primary_source
  reference: PMID:28507704; DOI:10.1039/c6sc04235j
  locator: Full original main text; Fig.1 and Fig.5 visually inspected by source reader,
    Fig.1 independently checked by coordinator
  accessed_at: '2026-10-21T12:23:50Z'
  support: supports
  summary: Original biosynthetic work depicts stereodefined celesticetin and tests
    isolated natural compound against Kocuria rhizophila. It reports MIC 1600 nM and
    a 19-mm inhibition zone. Ccb1/Ccb2 are producer biosynthetic enzymes, not antibacterial
    targets. The drawing demonstrates configuration matters but has not been atom-mapped
    to the proposed replacement database graph.
  snapshot_sha256: 4de5e9439521b6d160b61a620967118ce6c5582a7c9149e2257a1ac50ea0ce80
- evidence_id: primary2017-si
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5416915/supplementaryFiles
  locator: Original SI pp.1-3 and 5, recovered from EPMC supplementary archive
  accessed_at: '2026-10-21T12:23:50Z'
  support: partial
  summary: SI describes production and isolation from S. caelestis ATCC15084 culture
    broth. Diffusion used 5 nmol on 5-mm discs, 37 degrees C for 20 h; liquid MIC
    used 5 microlitres of a 0.5 McFarland K. rhizophila suspension in 1 mL LB containing
    25-1600 nM compound, 37 degrees C for 24 h. No Kocuria strain accession or exact
    counterion/hydrate of final assay solid is established.
  snapshot_sha256: 13844f0aa5159ca31a776e8dccc69918f22880972d57e993ea142a8489792c79
- evidence_id: primary1973
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.26.7
  locator: Full original text pp.7-14; Table 2 visually inspected by source reader
  accessed_at: '2026-10-21T12:23:50Z'
  support: partial
  summary: The congener study explicitly uses celesticetin HCl as comparator, including
    S. aureus UC80 MIC 2 micrograms/mL and E. coli UC51 >500. Twofold dilution in
    brain-heart infusion broth, 37 degrees C for 20 h. These hydrochloride measurements
    must not be silently relabeled as unsalted native-solid observations.
  snapshot_sha256: 058009a9d1957e66e590cd9c2908c0e7ca3102912579bbc33a9354f6e69aa3d9
- evidence_id: lmr2021
  kind: primary_source
  reference: PMID:34488446; DOI:10.1128/mbio.01731-21
  locator: Original Results, Discussion, strain/culture/MIC methods and all celesticetin
    body occurrences; source-reader report
  accessed_at: '2026-10-21T12:23:50Z'
  support: partial
  summary: S. lincolnensis ATCC25466 LmrC is a cytosolic ABCF ATPase with lincomycin/clindamycin
    resistance and biosynthetic regulation experiments. Celesticetin appears in S.
    caelestis production comparisons, not an identified LmrC-mediated celesticetin
    resistance assay. Absence of that endpoint in this paper is not biological proof
    that LmrC cannot protect against celesticetin.
  snapshot_sha256: 6f3df86a7aecf1aca3162ae6e2f857882beb7f4ee1f6d0c990fd902aec5d11d6
- evidence_id: lmr2004
  kind: primary_source
  reference: PMID:15192086; DOI:10.1074/jbc.M404072200
  locator: Original full paper pp.34449-34455, Table II and renaming passage; source-reader
    inspection
  accessed_at: '2026-10-21T12:23:50Z'
  support: partial
  summary: L. lactis YdaG/YdbA, renamed LmrC/LmrD, are membrane half-transporters
    with six predicted transmembrane helices each and a nucleotide-binding domain.
    The study uses IL1403 genes and NZ9000 expression, with ethidium/BCECF-AM/daunomycin/Hoechst
    transport substrates. This establishes a distinct homonym, not the Streptomyces
    cytosolic ABCF protein or direct celesticetin transport.
  snapshot_sha256: ce07eb3ea25e5cf362dfcc63fd7af0d98e1f639ab72bcaf06b79d8923f9bcb14
- evidence_id: reader
  kind: record_content
  reference: Collaborative primary-source inspection report
  locator: 267-source-reader-report.json
  accessed_at: '2026-10-21T12:23:50Z'
  support: context_only
  summary: The report records exact locators, source hashes, timestamps, primary observations,
    figure checks and failed routes. Original 1968 structure and full 1991 ribosome
    work remain unavailable; no all-eight-centre replacement assignment or niddamycin
    co-production confirmation is claimed.
  snapshot_sha256: 4a1314ea6c097adec44d8be34838d0f167c082e9335bc85b059f63d99a75dd21
- evidence_id: adapter
  kind: search
  reference: Installed kg-microbe-sources imodulondb adapter
  locator: 027-root-imodulondb-datasets.txt
  accessed_at: '2026-10-21T12:23:50Z'
  support: context_only
  summary: Structured dataset discovery preceded open protein/pathway research. The
    queried catalog lacks the exact Streptomyces/Lactococcus species needed for these
    assertions; no unrelated reference species was substituted. Catalog coverage is
    not evidence about resistance or absence of a mechanism.
  search_scope: Dataset catalog before open protein research; exact native name/IDs/full
    key and owner search with hidden/ignored files included outside .git/.venv; all
    six adopted source/class/determinant leads plus bounded original follow-up.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
assessments:
- assessment_id: identity
  area: identity
  topic: Native exact structure versus cited ChEBI identity
  outcome: concern
  summary: Connectivity, composition and mass agree, but the native all-unspecified
    stereo graph and six-defined-centre ChEBI mapping are not the same exact representation.
    Natural stereodefined material requires a separately verified identity decision.
  target_ids:
  - antibioticmech:aro-94c19a1c3c
  evidence_ids:
  - native
  - chemistry
  - chebi
  - pubchem-native
  - pubchem-candidate
  - xref-calculation
  - primary2017
- assessment_id: class
  area: grounding
  topic: Lincosamide class and antibacterial filing
  outcome: supported
  summary: The parent is broader than the compound and original cell inhibition supports
    antibacterial filing. Neither proves exact solid form or all absolute configurations.
  target_ids:
  - antibioticmech:aro-94c19a1c3c
  evidence_ids:
  - card
  - primary2017
  - primary2017-si
  - primary1973
- assessment_id: definition
  area: evidence
  topic: Producer and niddamycin clause
  outcome: unknown
  summary: S. caelestis production is directly supported in 2017 culture/isolation
    methods. The niddamycin clause remains source-attributed but independently unverified
    because its cited 1968 full paper was unavailable.
  target_ids:
  - antibioticmech:aro-94c19a1c3c
  evidence_ids:
  - native
  - card
  - lead-5638307
  - primary2017-si
- assessment_id: erm
  area: evidence
  topic: Attributed ErmV target alteration
  outcome: supported
  summary: The native database assertion matches CARD and the methylase mechanism
    family. Original exact-strain celesticetin resistance endpoints are not independently
    established at the inspected abstract depth.
  target_ids:
  - antibioticmech:aro-94c19a1c3c
  evidence_ids:
  - erm-card
  - lead-6163765
  - lead-9055987
- assessment_id: lmr
  area: evidence
  topic: LmrC source identity and exact-drug scope
  outcome: unknown
  summary: The imported relation is faithfully attributed, but upstream Lactococcus
    membrane-transporter and Streptomyces ABCF identities are conflated. Inspected
    primary sources do not resolve exact celesticetin target protection; preserve
    provenance and seek exact protein/assay support.
  target_ids:
  - antibioticmech:aro-94c19a1c3c
  evidence_ids:
  - lmr-card
  - lead-16958846
  - lmr2021
  - lmr2004
- assessment_id: leads
  area: evidence
  topic: All six adopted source and parent leads
  outcome: supported
  summary: Each adopted source lead has a declared abstract/metadata disposition;
    additional original studies supply bounded producer/activity and homonym context.
  target_ids:
  - antibioticmech:aro-94c19a1c3c
  evidence_ids:
  - lead-5638307
  - lead-6163765
  - lead-9055987
  - lead-16958846
  - lead-10582867
  - lead-15135500
  - reader
- assessment_id: provenance
  area: provenance
  topic: Maintained owners and original captures
  outcome: supported
  summary: All 18 input hashes and three native history events remain intact. Actual
    PubChem enrichment owner is included alongside ARO inventories.
  target_ids:
  - antibioticmech:aro-94c19a1c3c
  evidence_ids:
  - owners
  - native
- assessment_id: optional
  area: completeness
  topic: Unpopulated primary targets, activity, clinical and graph content
  outcome: not_applicable
  summary: Optional omissions are not defects. Biosynthetic enzymes, inhibition zones
    and MICs remain distinct from direct antibacterial target experiments.
  target_ids:
  - antibioticmech:aro-94c19a1c3c
  evidence_ids:
  - native
  - primary2017
  - primary2017-si
  - adapter
findings:
- finding_id: F1
  issue_key: celesticetin-incompatible-exact-stereochemical-groundings
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Exact cross-reference disagrees with the native stereochemical specification
  description: The native PubChem CID 220087 graph leaves all eight stereocentres
    unspecified and yields VMSQKUCYEMOKMM-UHFFFAOYSA-N. Asserted exact CHEBI:156421
    instead defines six centres and yields VMSQKUCYEMOKMM-AFJAYNRNSA-N. Original natural
    celesticetin is stereodefined, while CID 20054860 is an eight-defined-centre candidate
    requiring atom-level verification. Resolve the intended exact compound and correct
    the source-owned graph/crosswalk together; do not call the current unspecified
    graph a racemate or silently adopt a candidate.
  target_ids:
  - antibioticmech:aro-94c19a1c3c
  field_paths:
  - chemical_structure
  - xrefs[2]
  - xrefs[3]
  evidence_ids:
  - native
  - chemistry
  - chebi
  - pubchem-native
  - pubchem-candidate
  - xref-calculation
  - primary2017
  rule_id: native-review-checklist:Identity and Equivalence
  native_severity: major exact stereochemical cross-reference conflict
  normalization_reason: The published exact mapping equates different stereochemical
    specification levels; connectivity and formula alone cannot establish exact natural-product
    identity. No unverified replacement configuration is asserted.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual maintained source or transform for this record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual maintained source or transform for this record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Actual PubChem structure enrichment owner; captured before inspection
actions:
- action_id: A1
  description: Resolve natural celesticetin stereochemistry and make source-owned
    identity, structure and exact cross-references agree.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-94c19a1c3c
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual maintained source or transform for this record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual maintained source or transform for this record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Actual PubChem structure enrichment owner; captured before inspection
  acceptance_checks:
  - Atom-map original stereochemical evidence to the complete candidate graph, retaining
    any unresolved centres explicitly.
  - Do not infer racemic composition from unspecified stereochemistry or equate connectivity-only
    keys.
  - Use maintained PubChem/ARO extraction or grounding adjudication that survives
    reseeding; reassess minted identity if the intended grounding changes.
  - Keep the 1973 hydrochloride comparator and 2017 unspecified final solid-form assays
    separately scoped.
  - Rerun independent full-graph calculations, exact-reference, schema, strict, provenance
    and reproduction gates after separately authorized curation.
- action_id: A2
  description: Resolve the upstream LmrC homonym/citation conflation before adding
    exact celesticetin primary resistance evidence.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-94c19a1c3c
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported determinant relation and category
  acceptance_checks:
  - Distinguish S. lincolnensis cytosolic ABCF LmrC from L. lactis YdaG/LmrC plus
    YdbA/LmrD membrane transporter.
  - Seek a direct celesticetin assay for the exact protein and strain; retain database
    attribution until that scope is resolved.
  - Do not remove a biologically possible resistance relationship solely because inspected
    papers tested other substrates.
limitations:
- The original 1968 structure determination remained unavailable; full all-eight-centre
  atom mapping was not completed. The eight-defined-centre PubChem entry is a lead
  only.
- Niddamycin co-production remains independently unverified; this access limit is
  not treated as a proven native factual error.
- ErmV source papers were inspected at abstract depth; LmrC exact celesticetin phenotype
  remains unresolved despite primary homonym clarification.
- Full 1991 ribosome paper and 2006 Lactococcus distribution paper were unavailable.
  The latter complete abstract was inspected. No exhaustive resistance literature
  search is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All initial input hashes were retained when actual owners were appended; no native/source/history/status
  edits occurred.
- The source reader inspected the cited full primary texts and SI at explicit locators;
  the coordinator independently checked the exact native record, full authority structures,
  original natural-product drawing and antibacterial results.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://card.mcmaster.ca/aro/3001231
- https://www.ebi.ac.uk/chebi/CHEBI:156421
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5416915/
tags:
- celesticetin
- stereochemistry
- exact-cross-reference
- LmrC-homonym
```
