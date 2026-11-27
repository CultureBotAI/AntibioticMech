# Dragmacidin A: congener-specific definition correction and unresolved absolute-configuration comparison

- Review: 20261021T150611Z-dragmacidin-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:43:52Z
- Finished UTC: 2026-10-21T15:06:11Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native graph, PubChem accession and minted ARO identity are internally consistent. The imported definition instead describes dragmacidin G, including its different linker, sulfur-containing side chain and biological results. This confirmed major congener transfer needs source correction. One informational observation preserves a conflict between the native absolute configuration and a later A drawing without selecting an enantiomer from optical-rotation analogy. Exact-A antibacterial support was not established in the bounded literature reading.

## Scope And Provenance

Entire native YAML: identity, label, class, definition and citation, parent/class grounding, every chemical descriptor and both xrefs, source concept and deterministic mint, and all three history events. Both adopted source publication leads were read. Exact-congener discovery, synthesis and biological evidence were followed with the access limits below.

Selection: Queue position 374, one exact record. All thirteen original input hashes are preserved; actual ARO, PubChem and enrichment owners were appended before assessment, producing sixteen inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-e9b96b6d23 | data/antibiotics/antibacterial/dragmacidin-a.yaml | generated | dragmacidin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | antibioticmech:aro-e9b96b6d23 | Actual focused schema validation passed. |
| strict | passed | True | antibioticmech:aro-e9b96b6d23 | Actual one-record strict validation returned zero errors. |
| native-chemistry | passed | False | antibioticmech:aro-e9b96b6d23 | Both encodings reproduce the stored full key, formula, charge and masses; the deterministic ARO mint matches. |
| authority-chemistry | passed | False | antibioticmech:aro-e9b96b6d23 | Current PubChem SMILES and InChI independently parse to the native full key and formula. |
| figure-comparison | passed | False | antibioticmech:aro-e9b96b6d23 | Manual atom mapping of the visually inspected 2018 Figure 1 compound 3 reproduces the opposite absolute stereochemical depiction. This is a source comparison, not a natural-isolate assignment. |
| Authoritative full QC | failed | True | antibioticmech:aro-e9b96b6d23 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-e9b96b6d23 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-e9b96b6d23 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-e9b96b6d23 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-e9b96b6d23 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-e9b96b6d23 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-e9b96b6d23 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-e9b96b6d23 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-e9b96b6d23 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact graph, mints, xrefs and natural stereochemistry boundary

identity: concern. Targets: antibioticmech:aro-e9b96b6d23.

Native chemical encodings and the current exact PubChem entry agree, and the ARO-derived mint is reproducible. The 2018 source drawing has the opposite absolute depiction. The accessible primary scope does not resolve the natural/synthetic enantiomer comparison, so this remains an informational follow-up rather than a confirmed wrong-structure finding.

### Definition and adopted citation placement

evidence: concern. Targets: antibioticmech:aro-e9b96b6d23.

The complete paragraph concerns G, a chemically distinct congener. Both adopted papers are G/H evidence and cannot support the A-labelled paragraph. This is a confirmed source-origin congener transfer, independent of the unresolved A stereochemistry.

### Filing class and exact-compound biological evidence

evidence: unknown. Targets: antibioticmech:aro-e9b96b6d23.

The bis-indole structural class is chemically appropriate and reproduces ARO. Exact-A antibacterial support was not established by the inspected papers. Host-cell and phosphatase results do not substitute for a microbial phenotype; this bounded gap is not proof of universal inactivity or an automatic instruction to exclude A.

### Mode, targets, resistance, producer and experimental scope

evidence: not_applicable. Targets: antibioticmech:aro-e9b96b6d23.

No native mechanism, gene/protein, pathway, resistance, producer or transcriptomic assertion is present; structured source adapters were therefore not applicable at the native claim pass. The newly encountered PP1 experiments and PP2A/docking interpretations are host-cell context and are not imported as microbial targets or a causal graph.

### History, source ownership and completeness

provenance: supported. Targets: antibioticmech:aro-e9b96b6d23.

All present fields, adopted leads and three history events were read. MINTED and SEEDED remain honest. Optional synonyms, activity observations, clinical assertions and graphs need not be populated solely to complete this review. Actual generated owners and all original hashes are preserved; absence searches included ignored files.

## Findings

### F1: Replace the dragmacidin G definition attached to dragmacidin A

major / open / confirmed; issue key: dragmacidin-a-definition-transferred-from-g.

The native A-labelled record carries a paragraph explicitly about G, including its pyrazine linker, sulfur-containing side chain and biological panel. The neutral piperazine A structure lacks that chemistry. Both adopted source publications concern G/H. Correct the maintained ARO-derived definition and claim-level citation rather than relabelling A as G or transplanting G activity. Independently establish A-specific antimicrobial support before treating the imported antibacterial filing as scientifically confirmed.

### F2: Reconcile the later A drawing with the adopted absolute configuration

informational / open / provisional; issue key: dragmacidin-a-natural-absolute-configuration-reconciliation.

The 2018 Figure 1 compound 3 drawing maps to the opposite enantiomeric depiction from the native/current PubChem graph. The article uses optical-rotation analogy for new I/J and NMR/MS comparison for known A; those statements do not by themselves resolve natural A absolute stereochemistry. Full 1990/2002/2006 primary comparisons were unavailable. Preserve both source scopes and resolve the synthesis/isolate mapping before any inversion, merge or transfer of stereospecific assays.

## Recommended Actions And Acceptance Checks

### A1

Correct the A definition through maintained source qualification and retain only exact-A biological claims.

- Replace the G paragraph with independently supported A identity text and an appropriate exact-A primary citation. Keep G/H studies attached only to their actual compounds.
- Resolve the antibacterial filing using a bounded exact-A assay search or inspected original primary evidence. If no qualifying evidence can be established, document a curator scope decision; do not claim universal inactivity from this review.
- Regenerate from maintained inputs, compare the corrected claim and citation, and run schema, strict and source reproduction checks.

### A2

Resolve the source depiction conflict before proposing any stereochemical correction.

- Inspect the original natural A assignment and the enantioselective synthesis absolute-configuration and optical-rotation comparison at matched chemical form and conditions. Retain the 2018 drawing and its proposed I/J assignment as distinct evidence.
- Map the two piperazine centres by atom environment, not numbering alone. Do not select an enantiomer solely from sign of rotation, a review drawing or database consensus.
- Only if exact primary evidence resolves the identity should a maintained structure/identity input change; then regenerate and verify full stereochemical keys and relevant material-specific claims.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/dragmacidin-a.yaml; Entire native YAML. | supports | The MINTED/SEEDED record is labelled dragmacidin A and encodes neutral C21H20Br2N4, XQSOLGAZPINGFW-RTWAWAEBSA-N. Its definition explicitly names G and describes a pyrazine and sulfur-containing side chain absent from the stored piperazine graph. There are no synonyms, quantitative activity observations, molecular targets, mode, resistance assertions, producers, datasets, clinical assertions or causal graphs to validate. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/extract_source_inventory.py; scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py; conf/sources.yaml; Complete exact rows: ARO 542 and PubChem 235; relevant extraction, property selection, structure fallback and definition/citation selection code. | supports | ARO supplies the A label, G definition, parent/class and two PMID leads. PubChem supplies the exact structure. The seeder copies the ARO definition and selects its first reference, PMID38206835, as definition_source; this does not validate that the citation supports A. The PubChem configuration requests isomeric SMILES and InChI, and the current fetched descriptors agree. No ChEBI row owns this record. All three source-only history events and the ARO mint were checked. |
| aro | ARO:3007774; ARO:3007773; https://raw.githubusercontent.com/arpcard/aro/master/src/ontology/aro.obo; Current official A term and parent-class blocks read completely. | supports | The current ontology reproduces the same A label, PubChem11260315 xref, G definition and PMID38206835/28085024 references. ARO3007773 is the broader bis-indole alkaloid with antibiotic activity class. The native graph is chemically a bis-indole, but source inheritance alone does not establish A-specific antibacterial activity. The upstream term itself therefore carries the congener transfer. |
| pubchem | PubChem:11260315; Official property response and independent RDKit comparison of both encodings. | supports | The current neutral two-centre graph matches the native full Standard InChIKey, molecular formula and charge. Native SMILES atom 3, adjacent to NH, is S; atom 6, adjacent to N-methyl, is R. Native average and monoisotopic masses agree at their stated precision. Authority agreement verifies the adopted encoding, not by itself the absolute stereochemistry of every natural sample called dragmacidin A. |
| g2017 | PMID:28085024; DOI:10.3390/md15010016; PMC5295236; Complete main prose, structural-analysis text, Table 1 and assay methods read from original XML. Supplementary spectra were not reprocessed. | refutes | The isolated and tested compound is G, C23H19Br2N7S, with a pyrazine and guanidinoethylthio group. Its reported S. aureus and MRSA MICs are 0.62 micrograms/mL, with separate mycobacterial, malaria and mammalian-cell experiments. This supports the native paragraph only when attached to G, not A. The paper explicitly says pyruvate-kinase data for G are unavailable; nearby hamacanthin/topsentin findings cannot establish an A target. |
| gh2024 | PMID:38206835; DOI:10.1021/acs.orglett.3c04039; Complete indexed and publisher abstract read; full paper and supporting experiments not obtained. | refutes | The paper synthesizes G and H and tests those molecules and synthetic analogues against S. aureus and an efflux-deficient Salmonella Typhimurium strain. Its abstract does not report A. The chosen native definition_source therefore cannot support transferring the G paragraph to A. |
| ab2018 | PMID:30023878; DOI:10.1021/acsomega.7b01786; Complete main text, Tables 1–3, methods and captions read; Figure 1 visually inspected. XML requested under PMC6045348; current HTML resolves to PMC6645895 for the same DOI. | context_only | A is compound 3 and B compound 4, isolated with I/J and didebromodragmacidin from a Tanzanian Dragmacidon specimen; NMR and MS are compared with the prior literature. The biological work is mammalian antiproliferative/cell-cycle research. A has GI50 values 3.1, 3.3 and 3.8 micromolar in A549, HT29 and MDA-MB-231 cells. At 10 micromolar, A leaves 54.3 +/- 5.5 percent PP1 activity in the DiFMUP assay. This single-concentration result is not a fitted IC50 or direct binding measurement. PP2A participation and docking remain bounded mechanistic interpretations. No antibacterial assay is reported, and sponge extraction does not prove biosynthesis by the sponge. |
| figure-stereo | DOI:10.1021/acsomega.7b01786 Figure 1 compound 3; Original Figure 1 inspected visually and mapped to the native graph in 374-figure-check.py. | context_only | The depicted NH-adjacent centre maps to R and N-methyl-adjacent centre to S, producing XQSOLGAZPINGFW-LEWJYISDSA-N, the opposite enantiomeric depiction from the native encoding. The article proposes I/J absolute configuration by optical-rotation analogy to synthetic A; its NMR/MS comparison for A cannot distinguish enantiomers. This proves a depiction conflict, not that the native graph is wrong or that all biological samples have a known absolute configuration. |
| discovery | DOI:10.1016/S0040-4020(01)81355-7; Complete original publisher abstract as indexed by the web tool; attempted full publisher routes were unavailable. | context_only | The 1990 report identifies dragmacidon A as compound 8 and B as compound 9 from Hexadella sp. off British Columbia, with structures proposed from spectroscopy. The abstract reports A cytotoxicity in the L1210 assay, not an antibacterial endpoint. Full original tables, rotations and stereochemical arguments were not inspected. |
| syntheses | PMID:10986099; DOI:10.1021/ol006394g; DOI:10.1016/S0957-4166(02)00111-8; PMID:17312969; DOI:10.1039/b608910k; Complete 2000 and 2006 indexed abstracts and 2002 author-linked abstract read. Full original synthesis papers not obtained. | context_only | These primary studies establish synthetic work on A, including enantioselective routes. The 2002 abstract assigns the amino-alcohol intermediate and discusses dihydrohamacanthin stereochemistry but does not provide a complete exact-A natural/synthetic absolute-configuration comparison. The 2006 desymmetrisation abstract also does not resolve that comparison. No congener-wide bioactivity or natural A enantiomer is inferred from these abstracts. |
| antimicrobial-nearmiss | PMID:16508170; DOI:10.1248/bpb.29.570; Complete indexed original abstract. | context_only | The antibacterial bis-indole study tests topsentins 1–4 and hamacanthins 5–9, including deoxytopsentin and hamacanthin A. It does not test dragmacidin A. Its MRSA results are therefore a near miss, not support for the current exact-A filing. |
| search | 374-inclusive-hits.txt; 374-curation-hits.txt; 374-literature.json; Ignored-inclusive local search and bounded public literature search performed 2026-10-21. | context_only | No exact corrective curation overlay was found; the worklist is a discovery lead only. Public exact-name/alternate-name searches located discovery, synthesis and host-cell studies but no inspected exact-A antibacterial endpoint. Search results about G, D, related bis-indoles, crude sponge extracts and vendor activity summaries were not transferred to A. A 2024 synthesis review was used only as a lead to the 2002 paper, not as final stereochemical proof. |
| validation | 374-chemistry.json; 374-xref-chemistry.json; 374-figure-chemistry.json; 374-schema.log; 374-strict.log; Actual focused executions and input rehash. | supports | Schema, strict, native chemistry and PubChem chemistry checks pass. The manual figure comparison also executes successfully and preserves a source conflict. Every original input hash remains unchanged. Initial un-escalated network attempts failed name resolution; public retrieval then succeeded where recorded. A file named 374-2006-citeseer.pdf was HTML, not an inspected PDF. |

## Limits And Additional Notes

- The original 1990 discovery, 2000/2002/2006 synthesis and 2024 G/H papers were read at abstract depth only; free full-text attempts were unsuccessful. The 2002 abstract was accessible on an author-linked ResearchGate page, which explicitly said full text was unavailable. No paid access or author contact was used.
- The complete 2017 G and 2018 A/B main texts were read. The 2018 Figure 1 was inspected visually and mapped; remaining microscopy, docking images and supplementary spectra were not independently reprocessed. The review does not claim an independently secured absolute assignment for the natural A test sample.
- The bounded exact-A antibacterial search did not yield an inspected positive endpoint. This is an access/search boundary, not evidence that no such paper exists or that A is inactive in all microbial assays.
- Neither extraction from a sponge nor a putative family relationship establishes the actual biosynthetic producer. No missing producer or absent optional mechanism graph is treated as a defect.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- The current ARO definition reproduces the error; source agreement is not independent scientific validation. A later curation change must preserve the exact A/G distinction and the unresolved absolute-configuration boundary.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T150611Z-dragmacidin-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Dragmacidin A: congener-specific definition correction and unresolved absolute-configuration
  comparison'
started_at: '2026-10-21T14:43:52Z'
finished_at: '2026-10-21T15:06:11Z'
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
summary: The native graph, PubChem accession and minted ARO identity are internally
  consistent. The imported definition instead describes dragmacidin G, including its
  different linker, sulfur-containing side chain and biological results. This confirmed
  major congener transfer needs source correction. One informational observation preserves
  a conflict between the native absolute configuration and a later A drawing without
  selecting an enantiomer from optical-rotation analogy. Exact-A antibacterial support
  was not established in the bounded literature reading.
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
  - path: data/antibiotics/antibacterial/dragmacidin-a.yaml
    sha256: 6fbe543e45f9171bf58ce36487a802afa07204eed8a0d012b5d574ed02fa2c67
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
- target_id: antibioticmech:aro-e9b96b6d23
  path: data/antibiotics/antibacterial/dragmacidin-a.yaml
  label: dragmacidin A
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
  description: 'Entire native YAML: identity, label, class, definition and citation,
    parent/class grounding, every chemical descriptor and both xrefs, source concept
    and deterministic mint, and all three history events. Both adopted source publication
    leads were read. Exact-congener discovery, synthesis and biological evidence were
    followed with the access limits below.'
  selection: Queue position 374, one exact record. All thirteen original input hashes
    are preserved; actual ARO, PubChem and enrichment owners were appended before
    assessment, producing sixteen inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-e9b96b6d23
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused schema validation passed.
  target_ids:
  - antibioticmech:aro-e9b96b6d23
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/dragmacidin-a.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual one-record strict validation returned zero errors.
  target_ids:
  - antibioticmech:aro-e9b96b6d23
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/dragmacidin-a.yaml --out /private/tmp/am-review-session/374-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: native-chemistry
  name: native-chemistry
  status: passed
  required: false
  summary: Both encodings reproduce the stored full key, formula, charge and masses;
    the deterministic ARO mint matches.
  target_ids:
  - antibioticmech:aro-e9b96b6d23
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 374
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-chemistry
  name: authority-chemistry
  status: passed
  required: false
  summary: Current PubChem SMILES and InChI independently parse to the native full
    key and formula.
  target_ids:
  - antibioticmech:aro-e9b96b6d23
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/374-xref-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: figure-comparison
  name: figure-comparison
  status: passed
  required: false
  summary: Manual atom mapping of the visually inspected 2018 Figure 1 compound 3
    reproduces the opposite absolute stereochemical depiction. This is a source comparison,
    not a natural-isolate assignment.
  target_ids:
  - antibioticmech:aro-e9b96b6d23
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/374-figure-check.py
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
  - antibioticmech:aro-e9b96b6d23
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
  - antibioticmech:aro-e9b96b6d23
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
  - antibioticmech:aro-e9b96b6d23
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
  - antibioticmech:aro-e9b96b6d23
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
  - antibioticmech:aro-e9b96b6d23
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
  - antibioticmech:aro-e9b96b6d23
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
  - antibioticmech:aro-e9b96b6d23
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
  - antibioticmech:aro-e9b96b6d23
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
  - antibioticmech:aro-e9b96b6d23
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/dragmacidin-a.yaml
  locator: Entire native YAML.
  accessed_at: '2026-10-21T14:57:08Z'
  support: supports
  summary: The MINTED/SEEDED record is labelled dragmacidin A and encodes neutral
    C21H20Br2N4, XQSOLGAZPINGFW-RTWAWAEBSA-N. Its definition explicitly names G and
    describes a pyrazine and sulfur-containing side chain absent from the stored piperazine
    graph. There are no synonyms, quantitative activity observations, molecular targets,
    mode, resistance assertions, producers, datasets, clinical assertions or causal
    graphs to validate.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/extract_source_inventory.py;
    scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py; conf/sources.yaml
  locator: 'Complete exact rows: ARO 542 and PubChem 235; relevant extraction, property
    selection, structure fallback and definition/citation selection code.'
  accessed_at: '2026-10-21T14:57:08Z'
  support: supports
  summary: ARO supplies the A label, G definition, parent/class and two PMID leads.
    PubChem supplies the exact structure. The seeder copies the ARO definition and
    selects its first reference, PMID38206835, as definition_source; this does not
    validate that the citation supports A. The PubChem configuration requests isomeric
    SMILES and InChI, and the current fetched descriptors agree. No ChEBI row owns
    this record. All three source-only history events and the ARO mint were checked.
  snapshot_sha256: 9eab134ed628efb8140f71122691a6f1a1b36348389da952b811d308cc8337ce
- evidence_id: aro
  kind: database
  reference: ARO:3007774; ARO:3007773; https://raw.githubusercontent.com/arpcard/aro/master/src/ontology/aro.obo
  locator: Current official A term and parent-class blocks read completely.
  accessed_at: '2026-10-21T14:50:57Z'
  support: supports
  summary: The current ontology reproduces the same A label, PubChem11260315 xref,
    G definition and PMID38206835/28085024 references. ARO3007773 is the broader bis-indole
    alkaloid with antibiotic activity class. The native graph is chemically a bis-indole,
    but source inheritance alone does not establish A-specific antibacterial activity.
    The upstream term itself therefore carries the congener transfer.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: pubchem
  kind: authority
  reference: PubChem:11260315
  locator: Official property response and independent RDKit comparison of both encodings.
  accessed_at: '2026-10-21T14:50:57Z'
  support: supports
  summary: The current neutral two-centre graph matches the native full Standard InChIKey,
    molecular formula and charge. Native SMILES atom 3, adjacent to NH, is S; atom
    6, adjacent to N-methyl, is R. Native average and monoisotopic masses agree at
    their stated precision. Authority agreement verifies the adopted encoding, not
    by itself the absolute stereochemistry of every natural sample called dragmacidin
    A.
  snapshot_sha256: 2bc48ddc97ace454b565926fa1a6ca585b94e44f1ec001b03bd21df6004c4d23
- evidence_id: g2017
  kind: primary_source
  reference: PMID:28085024; DOI:10.3390/md15010016; PMC5295236
  locator: Complete main prose, structural-analysis text, Table 1 and assay methods
    read from original XML. Supplementary spectra were not reprocessed.
  accessed_at: '2026-10-21T14:51:22Z'
  support: refutes
  summary: The isolated and tested compound is G, C23H19Br2N7S, with a pyrazine and
    guanidinoethylthio group. Its reported S. aureus and MRSA MICs are 0.62 micrograms/mL,
    with separate mycobacterial, malaria and mammalian-cell experiments. This supports
    the native paragraph only when attached to G, not A. The paper explicitly says
    pyruvate-kinase data for G are unavailable; nearby hamacanthin/topsentin findings
    cannot establish an A target.
  snapshot_sha256: 5274486045543d17a24c658a77c86d11e71359cbbd2af9cd7f769a344953c5ee
- evidence_id: gh2024
  kind: primary_source
  reference: PMID:38206835; DOI:10.1021/acs.orglett.3c04039
  locator: Complete indexed and publisher abstract read; full paper and supporting
    experiments not obtained.
  accessed_at: '2026-10-21T14:50:57Z'
  support: refutes
  summary: The paper synthesizes G and H and tests those molecules and synthetic analogues
    against S. aureus and an efflux-deficient Salmonella Typhimurium strain. Its abstract
    does not report A. The chosen native definition_source therefore cannot support
    transferring the G paragraph to A.
  snapshot_sha256: bc5bc115eebede98c08a49f728c93e1e83a3a965afed552d8a2291a5451cd1f6
- evidence_id: ab2018
  kind: primary_source
  reference: PMID:30023878; DOI:10.1021/acsomega.7b01786
  locator: Complete main text, Tables 1–3, methods and captions read; Figure 1 visually
    inspected. XML requested under PMC6045348; current HTML resolves to PMC6645895
    for the same DOI.
  accessed_at: '2026-10-21T14:51:22Z'
  support: context_only
  summary: A is compound 3 and B compound 4, isolated with I/J and didebromodragmacidin
    from a Tanzanian Dragmacidon specimen; NMR and MS are compared with the prior
    literature. The biological work is mammalian antiproliferative/cell-cycle research.
    A has GI50 values 3.1, 3.3 and 3.8 micromolar in A549, HT29 and MDA-MB-231 cells.
    At 10 micromolar, A leaves 54.3 +/- 5.5 percent PP1 activity in the DiFMUP assay.
    This single-concentration result is not a fitted IC50 or direct binding measurement.
    PP2A participation and docking remain bounded mechanistic interpretations. No
    antibacterial assay is reported, and sponge extraction does not prove biosynthesis
    by the sponge.
  snapshot_sha256: 8afbff444f3ad865021098e36dba189963d2da055db73cc61f45e2beaaa400a7
- evidence_id: figure-stereo
  kind: primary_source
  reference: DOI:10.1021/acsomega.7b01786 Figure 1 compound 3
  locator: Original Figure 1 inspected visually and mapped to the native graph in
    374-figure-check.py.
  accessed_at: '2026-10-21T14:53:58Z'
  support: context_only
  summary: The depicted NH-adjacent centre maps to R and N-methyl-adjacent centre
    to S, producing XQSOLGAZPINGFW-LEWJYISDSA-N, the opposite enantiomeric depiction
    from the native encoding. The article proposes I/J absolute configuration by optical-rotation
    analogy to synthetic A; its NMR/MS comparison for A cannot distinguish enantiomers.
    This proves a depiction conflict, not that the native graph is wrong or that all
    biological samples have a known absolute configuration.
  snapshot_sha256: 46d071fb3e5adca3f94c1394961c55f1f3305bc53587396875a5cf9933c631d6
- evidence_id: discovery
  kind: primary_source
  reference: DOI:10.1016/S0040-4020(01)81355-7
  locator: Complete original publisher abstract as indexed by the web tool; attempted
    full publisher routes were unavailable.
  accessed_at: '2026-10-21T14:57:08Z'
  support: context_only
  summary: The 1990 report identifies dragmacidon A as compound 8 and B as compound
    9 from Hexadella sp. off British Columbia, with structures proposed from spectroscopy.
    The abstract reports A cytotoxicity in the L1210 assay, not an antibacterial endpoint.
    Full original tables, rotations and stereochemical arguments were not inspected.
- evidence_id: syntheses
  kind: primary_source
  reference: PMID:10986099; DOI:10.1021/ol006394g; DOI:10.1016/S0957-4166(02)00111-8;
    PMID:17312969; DOI:10.1039/b608910k
  locator: Complete 2000 and 2006 indexed abstracts and 2002 author-linked abstract
    read. Full original synthesis papers not obtained.
  accessed_at: '2026-10-21T14:53:58Z'
  support: context_only
  summary: These primary studies establish synthetic work on A, including enantioselective
    routes. The 2002 abstract assigns the amino-alcohol intermediate and discusses
    dihydrohamacanthin stereochemistry but does not provide a complete exact-A natural/synthetic
    absolute-configuration comparison. The 2006 desymmetrisation abstract also does
    not resolve that comparison. No congener-wide bioactivity or natural A enantiomer
    is inferred from these abstracts.
  snapshot_sha256: 00b0d9fb00e05e48d70476fbb399d5866e8334551da1121faeccd8ad97f04cb3
- evidence_id: antimicrobial-nearmiss
  kind: primary_source
  reference: PMID:16508170; DOI:10.1248/bpb.29.570
  locator: Complete indexed original abstract.
  accessed_at: '2026-10-21T14:53:58Z'
  support: context_only
  summary: The antibacterial bis-indole study tests topsentins 1–4 and hamacanthins
    5–9, including deoxytopsentin and hamacanthin A. It does not test dragmacidin
    A. Its MRSA results are therefore a near miss, not support for the current exact-A
    filing.
  snapshot_sha256: 00b0d9fb00e05e48d70476fbb399d5866e8334551da1121faeccd8ad97f04cb3
- evidence_id: search
  kind: search
  reference: 374-inclusive-hits.txt; 374-curation-hits.txt; 374-literature.json
  locator: Ignored-inclusive local search and bounded public literature search performed
    2026-10-21.
  accessed_at: '2026-10-21T14:57:08Z'
  support: context_only
  summary: No exact corrective curation overlay was found; the worklist is a discovery
    lead only. Public exact-name/alternate-name searches located discovery, synthesis
    and host-cell studies but no inspected exact-A antibacterial endpoint. Search
    results about G, D, related bis-indoles, crude sponge extracts and vendor activity
    summaries were not transferred to A. A 2024 synthesis review was used only as
    a lead to the 2002 paper, not as final stereochemical proof.
  search_scope: rg --no-ignore --hidden over data, curation, conf, scripts, src, docs,
    .claude, reviews and reports for dragmacidin A, ARO:3007774 and XQSOLGAZPINGFW;
    a separate ignored-inclusive search over curation/conf/reports/reviews also included
    dragmacidon A. Europe PMC and public web searches used the exact names plus antibacterial,
    antimicrobial, MIC, absolute configuration, the exact adopted PMIDs and primary
    synthesis DOIs.
  snapshot_sha256: a2e6d078067a8c5e2f5707911da79ead2b82b32f794d16cd6bb4232c589e2e71
- evidence_id: validation
  kind: validation
  reference: 374-chemistry.json; 374-xref-chemistry.json; 374-figure-chemistry.json;
    374-schema.log; 374-strict.log
  locator: Actual focused executions and input rehash.
  accessed_at: '2026-10-21T14:57:08Z'
  support: supports
  summary: Schema, strict, native chemistry and PubChem chemistry checks pass. The
    manual figure comparison also executes successfully and preserves a source conflict.
    Every original input hash remains unchanged. Initial un-escalated network attempts
    failed name resolution; public retrieval then succeeded where recorded. A file
    named 374-2006-citeseer.pdf was HTML, not an inspected PDF.
  snapshot_sha256: c35cc9692c027bfa0fc91d3a1f7bf5e7185425f54de060747fa65116d3549525
assessments:
- assessment_id: identity
  area: identity
  topic: Exact graph, mints, xrefs and natural stereochemistry boundary
  outcome: concern
  summary: Native chemical encodings and the current exact PubChem entry agree, and
    the ARO-derived mint is reproducible. The 2018 source drawing has the opposite
    absolute depiction. The accessible primary scope does not resolve the natural/synthetic
    enantiomer comparison, so this remains an informational follow-up rather than
    a confirmed wrong-structure finding.
  target_ids:
  - antibioticmech:aro-e9b96b6d23
  evidence_ids:
  - native
  - pubchem
  - figure-stereo
  - syntheses
  - validation
- assessment_id: definition
  area: evidence
  topic: Definition and adopted citation placement
  outcome: concern
  summary: The complete paragraph concerns G, a chemically distinct congener. Both
    adopted papers are G/H evidence and cannot support the A-labelled paragraph. This
    is a confirmed source-origin congener transfer, independent of the unresolved
    A stereochemistry.
  target_ids:
  - antibioticmech:aro-e9b96b6d23
  evidence_ids:
  - native
  - owners
  - aro
  - g2017
  - gh2024
- assessment_id: activity
  area: evidence
  topic: Filing class and exact-compound biological evidence
  outcome: unknown
  summary: The bis-indole structural class is chemically appropriate and reproduces
    ARO. Exact-A antibacterial support was not established by the inspected papers.
    Host-cell and phosphatase results do not substitute for a microbial phenotype;
    this bounded gap is not proof of universal inactivity or an automatic instruction
    to exclude A.
  target_ids:
  - antibioticmech:aro-e9b96b6d23
  evidence_ids:
  - aro
  - ab2018
  - discovery
  - antimicrobial-nearmiss
  - search
- assessment_id: mechanism
  area: evidence
  topic: Mode, targets, resistance, producer and experimental scope
  outcome: not_applicable
  summary: No native mechanism, gene/protein, pathway, resistance, producer or transcriptomic
    assertion is present; structured source adapters were therefore not applicable
    at the native claim pass. The newly encountered PP1 experiments and PP2A/docking
    interpretations are host-cell context and are not imported as microbial targets
    or a causal graph.
  target_ids:
  - antibioticmech:aro-e9b96b6d23
  evidence_ids:
  - native
  - ab2018
  - g2017
- assessment_id: audit
  area: provenance
  topic: History, source ownership and completeness
  outcome: supported
  summary: All present fields, adopted leads and three history events were read. MINTED
    and SEEDED remain honest. Optional synonyms, activity observations, clinical assertions
    and graphs need not be populated solely to complete this review. Actual generated
    owners and all original hashes are preserved; absence searches included ignored
    files.
  target_ids:
  - antibioticmech:aro-e9b96b6d23
  evidence_ids:
  - native
  - owners
  - search
  - validation
findings:
- finding_id: F1
  issue_key: dragmacidin-a-definition-transferred-from-g
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Replace the dragmacidin G definition attached to dragmacidin A
  description: The native A-labelled record carries a paragraph explicitly about G,
    including its pyrazine linker, sulfur-containing side chain and biological panel.
    The neutral piperazine A structure lacks that chemistry. Both adopted source publications
    concern G/H. Correct the maintained ARO-derived definition and claim-level citation
    rather than relabelling A as G or transplanting G activity. Independently establish
    A-specific antimicrobial support before treating the imported antibacterial filing
    as scientifically confirmed.
  target_ids:
  - antibioticmech:aro-e9b96b6d23
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - native
  - owners
  - aro
  - g2017
  - gh2024
  rule_id: Exact-compound evidence and congener-boundary checklist; source support
    belongs to the narrowest supported claim
  native_severity: major
  normalization_reason: This is a confirmed material congener transfer in descriptive
    and biological claims. The stable A label, exact PubChem accession and internally
    consistent graph remain separately identifiable; the review does not infer that
    A is universally inactive.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted source definition and publication references
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source-specific definition qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition and citation selection
- finding_id: F2
  issue_key: dragmacidin-a-natural-absolute-configuration-reconciliation
  category: identity
  severity: informational
  status: open
  certainty: provisional
  title: Reconcile the later A drawing with the adopted absolute configuration
  description: The 2018 Figure 1 compound 3 drawing maps to the opposite enantiomeric
    depiction from the native/current PubChem graph. The article uses optical-rotation
    analogy for new I/J and NMR/MS comparison for known A; those statements do not
    by themselves resolve natural A absolute stereochemistry. Full 1990/2002/2006
    primary comparisons were unavailable. Preserve both source scopes and resolve
    the synthesis/isolate mapping before any inversion, merge or transfer of stereospecific
    assays.
  target_ids:
  - antibioticmech:aro-e9b96b6d23
  field_paths:
  - chemical_structure
  evidence_ids:
  - pubchem
  - figure-stereo
  - ab2018
  - syntheses
  - discovery
  rule_id: Preserve reliable source conflicts; distinguish relative structure, absolute
    assignment and material identity
  native_severity: informational
  normalization_reason: The depiction conflict is reproducible, but a corrective native
    structure change is not established. This is an explicit identity research question
    rather than an asserted wrong-enantiomer defect.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact chemical encoding
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Reproducible PubChem structure provenance
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Only evidence-supported identity or scope decisions
actions:
- action_id: A1
  description: Correct the A definition through maintained source qualification and
    retain only exact-A biological claims.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-e9b96b6d23
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted source definition and publication references
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source-specific definition qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition and citation selection
  acceptance_checks:
  - Replace the G paragraph with independently supported A identity text and an appropriate
    exact-A primary citation. Keep G/H studies attached only to their actual compounds.
  - Resolve the antibacterial filing using a bounded exact-A assay search or inspected
    original primary evidence. If no qualifying evidence can be established, document
    a curator scope decision; do not claim universal inactivity from this review.
  - Regenerate from maintained inputs, compare the corrected claim and citation, and
    run schema, strict and source reproduction checks.
- action_id: A2
  description: Resolve the source depiction conflict before proposing any stereochemical
    correction.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-e9b96b6d23
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact chemical encoding
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Reproducible PubChem structure provenance
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Only evidence-supported identity or scope decisions
  acceptance_checks:
  - Inspect the original natural A assignment and the enantioselective synthesis absolute-configuration
    and optical-rotation comparison at matched chemical form and conditions. Retain
    the 2018 drawing and its proposed I/J assignment as distinct evidence.
  - Map the two piperazine centres by atom environment, not numbering alone. Do not
    select an enantiomer solely from sign of rotation, a review drawing or database
    consensus.
  - Only if exact primary evidence resolves the identity should a maintained structure/identity
    input change; then regenerate and verify full stereochemical keys and relevant
    material-specific claims.
limitations:
- The original 1990 discovery, 2000/2002/2006 synthesis and 2024 G/H papers were read
  at abstract depth only; free full-text attempts were unsuccessful. The 2002 abstract
  was accessible on an author-linked ResearchGate page, which explicitly said full
  text was unavailable. No paid access or author contact was used.
- The complete 2017 G and 2018 A/B main texts were read. The 2018 Figure 1 was inspected
  visually and mapped; remaining microscopy, docking images and supplementary spectra
  were not independently reprocessed. The review does not claim an independently secured
  absolute assignment for the natural A test sample.
- The bounded exact-A antibacterial search did not yield an inspected positive endpoint.
  This is an access/search boundary, not evidence that no such paper exists or that
  A is inactive in all microbial assays.
- Neither extraction from a sponge nor a putative family relationship establishes
  the actual biosynthetic producer. No missing producer or absent optional mechanism
  graph is treated as a defect.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- The current ARO definition reproduces the error; source agreement is not independent
  scientific validation. A later curation change must preserve the exact A/G distinction
  and the unresolved absolute-configuration boundary.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
