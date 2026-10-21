# Fonsecinone C: exact congener and antibacterial evidence supported; qualify isolation history

- Review: 20261021T164007Z-fonsecinone-c-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:22:24Z
- Finished UTC: 2026-10-21T16:40:07Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The entire native record reproduces the maintained ChEBI source, and independent structure comparisons agree. The adopted 2016 original directly tests fonsecinone C as compound 3 and supports its antibacterial role. One provisional minor finding concerns the definition’s first-isolation wording. Hemiketal/axial identity and source-assay limitations remain explicit without transferring evidence from fonsecinone A.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 454; one complete exact record, assessed separately from fonsecinone A. All thirteen initial hashes were verified before judgment and preserved; actual ChEBI owners were confirmed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:133757 | data/antibiotics/antibacterial/fonsecinone-c.yaml | generated | fonsecinone C |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | CHEBI:133757 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:133757 | Actual focused execution exited 0. |
| Focused chemistry verification | passed | False | CHEBI:133757 | Actual focused execution exited 0. |
| Independent current chemical authority comparison | passed | False | CHEBI:133757 | Native SMILES and InChI, official ChEBI molfile and name-resolved PubChem structure all reproduce the full native key and formula. Undefined hemiketal stereo warnings are retained as representation scope, not parsing failures. |
| Authoritative full QC | failed | True | CHEBI:133757 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:133757 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:133757 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:133757 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:133757 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:133757 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:133757 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:133757 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:133757 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact C constitution, synonym and ontology parents

identity: supported. Targets: CHEBI:133757.

Native and current authority graphs agree and match the exact compound 3 constitution in the original activity study. C is neither A nor B. Hemiketal and axial configuration remain unresolved by the stored encodings; an unspecified graph alone is not evidence of a mixture.

### Antibacterial role

evidence: supported. Targets: CHEBI:133757.

The original separately measures compound 3 whole-cell activity, binding and enzyme inhibition. Its precise strain/material limits and internal inconsistencies should accompany any future enrichment, but no native universal potency or causal target claim needs correction.

### Fungal isolation and historical priority wording

provenance: concern. Targets: CHEBI:133757.

Association with A. niger culture is supported; the original study also warns about instability and interconversion. The first-isolation modifier needs qualification because the current exact-C origin trail points to A. fonsecaeus and the 1984 source remains unavailable in full.

### Mechanism and optional biological objects

completeness: supported. Targets: CHEBI:133757.

The native record names no gene/protein/pathway/stress-response or dataset, so an adapter-first target lookup is not triggered. Direct FabI biochemistry is a concrete optional follow-up; biosynthetic proteins, other-congener activity and docking predictions are not automatically antibacterial causal mechanisms. Absent optional MIC, producer, resistance, clinical and graph objects are not independent defects.

### Maintained input ownership and adopted lead disposition

provenance: supported. Targets: CHEBI:133757.

All native fields, source row, two adopted citations, role/classification logic, registry metadata and history were assessed. Source transfer is reproducible and does not claim scientific REVIEWED status.

## Findings

### F1: Qualify the historical first-isolation modifier

minor / open / provisional; issue key: fonsecinone-c-first-isolation-wording.

The native definition says originally isolated from A. niger. The current exact-C ChEBI origin trail instead associates A. fonsecaeus NRRL67 with the 1984 discovery citation, while direct A. niger culture evidence comes from the later 2011 paper. Official Species Fungorum does not list A. niger as a synonym in the inspected name record. Because the 1984 full text and historical strain reidentification remain unresolved, the correction should preserve supported A. niger association while qualifying unverified priority, rather than asserting a definitive new taxonomy.

## Recommended Actions And Acceptance Checks

### A1

Resolve or qualify first-isolation wording through maintained source ownership.

- Read the exact 1984 primary source and any authoritative NRRL67 reidentification before retaining originally isolated from A. niger. Alternatively retain the supported phrase isolated from A. niger with a precise original-source citation and any isolation-instability qualification.
- Apply the change through the maintained ChEBI source or an explicit reproducible definition override, regenerate and run focused schema/strict and corpus reproduction. Preserve the exact C key and supported antibacterial role.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/fonsecinone-c.yaml; Entire native YAML including name, definition, all seven parents, sole activity role, complete structure, registry association, source concept and history. | supports | The SEEDED, EXACT record describes the neutral C32H28O11 cyclic-hemiketal congener, with one systematic synonym and an antibacterial-agent role. The definition says originally isolated from Aspergillus niger. No mode, target, resistance, MIC, producer object, clinical assertion, dataset or causal graph is present. Its sole exact external association is Reaxys 5209914. Three history events describe seeding and reseeding rather than scientific review. |
| owners | data/raw/chebi_antimicrobials.tsv:2523; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; curation/decisions.tsv; Complete exact maintained source row and applicable ChEBI extraction/classification/emission logic. | supports | The maintained ChEBI row supplies all native fields and two adopted leads, PMID 21176790 and PMID 27063778. Its mechanism-role column is empty. The source mint antibioticmech:chebi-982db5a358 reproduces, and the antibacterial filing follows the imported role. No additional exact ARO, molecular-target/resistance, FDA, PubChem-enrichment or MIBiG owner row was found in the source scan. Current source graphs are read as provenance, not substituted for primary experiments. |
| identity | CHEBI:133757; https://www.ebi.ac.uk/chebi/backend/api/public/compound/133757/; PubChem:90477754; reaxys:5209914; Complete official ChEBI entry/molfile, current name-resolved PubChem properties and independent four-encoding parsing. | supports | Native and current authority graphs all yield XWHLKURAEUPHAB-UHFFFAOYSA-N, neutral C32H28O11, average mass 588.565 and monoisotopic mass 588.16316. The precise cyclic-hemiketal constitution and systematic name agree. One tetrahedral hemiketal centre is unspecified, and axial configuration is not established by the Standard InChI/key. These omissions do not prove a mixture or racemate. Reaxys 5209914 is repeated in current ChEBI registry metadata; its underlying paid record was not inspected. PubChem 90477754 is corroborative discovery evidence, not a native exact cross-reference. |
| groundings | CHEBI:26195; CHEBI:35618; CHEBI:3992; CHEBI:59780; CHEBI:64459; CHEBI:64542; CHEBI:76224; CHEBI:33282; Exact official parent and role definitions, including the C-specific cyclic-hemiketal term. | supports | The parents denote polyphenol, aromatic ether, cyclic ketone, cyclic hemiketal, biaryl, naphtho-gamma-pyrone and aromatic ketone, all compatible with the represented graph. The cyclic hemiketal has an OH/OR-bearing carbon connected to two carbons. The activity role denotes antibacterial agent and supports the filing category when read with the primary experiment. |
| primary2016 | PMID:27063778; DOI:10.1038/srep24291; https://pmc.ncbi.nlm.nih.gov/articles/PMC4827027/; Complete adopted main article, exact compound 3 NMR description, isolation, Tables 1–3 and all relevant Methods; Figure 1 and Figure 3 independently viewed. | supports | Fonsecinone C is compound 3, separately isolated from Aspergillus sp. Z120 with stated HPLC purity at least 95%. Its Figure 1 constitution and reported NMR data support the hydrated linear-half congener represented natively. Table 1 gives C MICs in µg/mL: E. coli ATCC35218 4.26; E. coli ATCC25922 2.13; P. aeruginosa ATCC27853 17.04; K. pneumoniae ATCC700603 at least 100; S. aureus ATCC43300 34.08; E. faecalis ATCC29212 17.04. The last value is C’s own result, distinct from A’s 4.26. Broth microdilution uses Mueller-Hinton broth, stated 10^5 cells/mL, twofold serial dilution, triplicate,24 hours at 30°C and complete growth inhibition measured by OD600. These direct assays support antibacterial activity without a universal spectrum or clinical assertion. |
| fabI | PMID:27063778; DOI:10.1038/srep24291; Exact compound 3 biochemical results, Table 3, Figure 3 and recombinant protein/MST/enzyme methods. | supports | Recombinant E. coli K-12 MG1655 FabI is expressed in BL21(DE3) and tested directly. Table 3 reports C Kd 270.0±9.1 µM and IC50 3.0 µM. The plotted C MST panel instead reports 270±7.3 µM, while its caption mistakenly says fonsecinone B. The actual panel, compound table and structure mapping identify C. The enzyme assay uses crotonoyl-CoA and NADH; IC50 and Kd are distinct measurements. Direct biochemical interaction/inhibition is a useful optional curation lead, but docking poses and correlation with MIC do not demonstrate whole-cell FabI causality in each tested organism. |
| primary2011 | PMID:21176790; DOI:10.1016/j.fgb.2010.12.001; https://pmc.ncbi.nlm.nih.gov/articles/PMC3118676/; Complete indexed abstract and original culture/isolation Methods plus exact-compound identification and biosynthetic Results sections. | supports | The study uses A. niger ATCC11414 and identifies fonsecinone C as compound 8. It explicitly discusses chromatographic interconversion: subfractions B4/B5 contain equilibrating compounds 8/9 with dehydration products 12/13, and purification can alter the profile. This supports association with the fungal culture but does not establish that every isolated fraction is stable pure C. Polyketide-synthase knockout evidence concerns fungal biosynthesis, not an antibacterial target or resistance mechanism. No isolated C antibacterial assay is transferred from this paper. |
| source-boundaries | PMID:27063778; DOI:10.1038/srep24291; Main article structure, strain, mass, caption and statistical cross-check. | context_only | The source assigns axial R through ECD comparison and calculation, while Figure 1 does not resolve the hemiketal centre. The unread supplement limits independent assessment of those stereochemical calculations. Its ATCC35218 ESBL label is retained as the authors’ wording rather than independently verified phenotype; one prose strain accession and Figure 3 caption also conflict with the tables/plot. The reported high-resolution mass/ion annotation is inconsistent with the theoretical mass, although formula, other characterization, drawing and current authority structures agree. These are source-quality limits for future numerical/mechanistic enrichment, not native graph defects. |
| origin | CHEBI:133757 compound_origins; DOI:10.1016/S0040-4020(01)88792-5; fungorum:284301; https://www.speciesfungorum.org/Names/SynSpecies.asp?RecordID=284301; Current exact-C ChEBI origin entry, original 1984 publisher/Crossref title metadata, current Species Fungorum name page and adopted 2011 isolation text. | context_only | Current ChEBI associates this exact C congener with A. fonsecaeus NRRL67 and the 1984 discovery DOI, whose title names that fungus. Species Fungorum resolves record 284301 to A. fonsecaeus Thom &amp; Raper and states no synonyms. The native A. niger association is supported by the 2011 original, but the inspected sources do not establish its priority as the original isolation species. The 1984 full text and any historical strain reidentification were not obtained, so the proposed wording qualification remains provisional and does not transfer A’s historical account automatically to C. |
| search | 454-inclusive-hits.txt; 454-literature.json; 453-literature.json; public fetch manifests 453/454; Hidden- and ignored-inclusive exact local search, both adopted PMID resolutions and bounded public family/exact-congener follow-up. | context_only | The inclusive search finds the exact native/raw rows, distinct A sibling, maps and readiness queue. A historical report on another compound only points to shared literature and is not scientific evidence here. Both adopted citations were resolved; their complete abstracts were read, followed by the 2016 full main and relevant 2011 original sections. A narrow literal C title/abstract query returned no result, but the broader fonsecinone family query and adopted-source resolution recovered the directly relevant 2016 study; the narrow miss is not used as negative literature evidence. A-specific 2021 activity and atropisomer data are not transferred to C. |
| checks | 454-focused-results.json; 454-chemistry.json; 454-authority-chemistry.json; Actual focused schema/strict/standalone chemistry and independent authority checks. | supports | All executions exit 0, and the original thirteen input hashes remain unchanged. The full key, formula, mass, neutral charge and source mint are consistent. Undefined stereo warnings identify scope already visible in the graph; they are not a failed parse. |

## Limits And Additional Notes

- The 1984 discovery full text was unavailable; original publisher metadata, the exact-C authority origin entry and current fungal nomenclature were inspected. Historical priority is therefore provisional.
- The 2016 supplement could not be retrieved as a valid PDF through the inspected PMC/publisher routes: responses were preparation/challenge HTML or a DNS error. Additional NMR spectra and ECD calculations are not claimed as independently inspected.
- The 2011 source explicitly reports interconversion in C-containing fractions. Its fungal association does not establish stable pure C in every fraction or direct antibacterial activity; the 2016 separately purified compound 3 supports the activity assessment.
- The native graph leaves the hemiketal centre and axial configuration unresolved. The source’s axial R assignment is not promoted to an experimentally re-established absolute identity here.
- Reaxys 5209914 was checked as a current official ChEBI registry association only; its underlying record was not accessed. Internal source mass, strain and MST-caption discrepancies would require reconciliation before precise numerical or mechanistic enrichment.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All thirteen initial input hashes are preserved. Shared literature was independently mapped to C’s compound number and assays; no A-specific result was copied as C evidence.
- Optional FabI and MIC enrichment is a future curation opportunity, not a missing-required-field defect.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T164007Z-fonsecinone-c-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Fonsecinone C: exact congener and antibacterial evidence supported; qualify
  isolation history'
started_at: '2026-10-21T16:22:24Z'
finished_at: '2026-10-21T16:40:07Z'
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
summary: The entire native record reproduces the maintained ChEBI source, and independent
  structure comparisons agree. The adopted 2016 original directly tests fonsecinone
  C as compound 3 and supports its antibacterial role. One provisional minor finding
  concerns the definition’s first-isolation wording. Hemiketal/axial identity and
  source-assay limitations remain explicit without transferring evidence from fonsecinone
  A.
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
  - path: data/antibiotics/antibacterial/fonsecinone-c.yaml
    sha256: d3f0f230f5692785f5ef4c1481b1076590ed1ffc7df8225db55b4cef455cfed0
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
targets:
- target_id: CHEBI:133757
  path: data/antibiotics/antibacterial/fonsecinone-c.yaml
  label: fonsecinone C
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
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 454; one complete exact record, assessed separately from
    fonsecinone A. All thirteen initial hashes were verified before judgment and preserved;
    actual ChEBI owners were confirmed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:133757
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:133757
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/fonsecinone-c.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:133757
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/fonsecinone-c.yaml --out /private/tmp/am-review-session/454-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:133757
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 454
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-chemistry
  name: Independent current chemical authority comparison
  status: passed
  required: false
  summary: Native SMILES and InChI, official ChEBI molfile and name-resolved PubChem
    structure all reproduce the full native key and formula. Undefined hemiketal stereo
    warnings are retained as representation scope, not parsing failures.
  target_ids:
  - CHEBI:133757
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/454-authority-check.py
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
  - CHEBI:133757
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
  - CHEBI:133757
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
  - CHEBI:133757
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
  - CHEBI:133757
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
  - CHEBI:133757
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
  - CHEBI:133757
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
  - CHEBI:133757
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
  - CHEBI:133757
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
  - CHEBI:133757
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/fonsecinone-c.yaml
  locator: Entire native YAML including name, definition, all seven parents, sole
    activity role, complete structure, registry association, source concept and history.
  accessed_at: '2026-10-21T16:30:48Z'
  support: supports
  summary: The SEEDED, EXACT record describes the neutral C32H28O11 cyclic-hemiketal
    congener, with one systematic synonym and an antibacterial-agent role. The definition
    says originally isolated from Aspergillus niger. No mode, target, resistance,
    MIC, producer object, clinical assertion, dataset or causal graph is present.
    Its sole exact external association is Reaxys 5209914. Three history events describe
    seeding and reseeding rather than scientific review.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv:2523; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py; curation/decisions.tsv
  locator: Complete exact maintained source row and applicable ChEBI extraction/classification/emission
    logic.
  accessed_at: '2026-10-21T16:30:48Z'
  support: supports
  summary: The maintained ChEBI row supplies all native fields and two adopted leads,
    PMID 21176790 and PMID 27063778. Its mechanism-role column is empty. The source
    mint antibioticmech:chebi-982db5a358 reproduces, and the antibacterial filing
    follows the imported role. No additional exact ARO, molecular-target/resistance,
    FDA, PubChem-enrichment or MIBiG owner row was found in the source scan. Current
    source graphs are read as provenance, not substituted for primary experiments.
  snapshot_sha256: 63cbc53a82afc7f96a793fbdfeb241b606a79f321ed00c94bbd3c165cd3465c7
- evidence_id: identity
  kind: authority
  reference: CHEBI:133757; https://www.ebi.ac.uk/chebi/backend/api/public/compound/133757/;
    PubChem:90477754; reaxys:5209914
  locator: Complete official ChEBI entry/molfile, current name-resolved PubChem properties
    and independent four-encoding parsing.
  accessed_at: '2026-10-21T16:30:48Z'
  support: supports
  summary: Native and current authority graphs all yield XWHLKURAEUPHAB-UHFFFAOYSA-N,
    neutral C32H28O11, average mass 588.565 and monoisotopic mass 588.16316. The precise
    cyclic-hemiketal constitution and systematic name agree. One tetrahedral hemiketal
    centre is unspecified, and axial configuration is not established by the Standard
    InChI/key. These omissions do not prove a mixture or racemate. Reaxys 5209914
    is repeated in current ChEBI registry metadata; its underlying paid record was
    not inspected. PubChem 90477754 is corroborative discovery evidence, not a native
    exact cross-reference.
  snapshot_sha256: 8a285c6a265fee847c90dc60afdb2d022bc732507c5ab6dfa15b03aee2cee430
- evidence_id: groundings
  kind: authority
  reference: CHEBI:26195; CHEBI:35618; CHEBI:3992; CHEBI:59780; CHEBI:64459; CHEBI:64542;
    CHEBI:76224; CHEBI:33282
  locator: Exact official parent and role definitions, including the C-specific cyclic-hemiketal
    term.
  accessed_at: '2026-10-21T16:28:13Z'
  support: supports
  summary: The parents denote polyphenol, aromatic ether, cyclic ketone, cyclic hemiketal,
    biaryl, naphtho-gamma-pyrone and aromatic ketone, all compatible with the represented
    graph. The cyclic hemiketal has an OH/OR-bearing carbon connected to two carbons.
    The activity role denotes antibacterial agent and supports the filing category
    when read with the primary experiment.
  snapshot_sha256: f758b5da77539a832e2c281773a964392a96c6e65ceec9e9021489082db9de72
- evidence_id: primary2016
  kind: primary_source
  reference: PMID:27063778; DOI:10.1038/srep24291; https://pmc.ncbi.nlm.nih.gov/articles/PMC4827027/
  locator: Complete adopted main article, exact compound 3 NMR description, isolation,
    Tables 1–3 and all relevant Methods; Figure 1 and Figure 3 independently viewed.
  accessed_at: '2026-10-21T16:23:48Z'
  support: supports
  summary: 'Fonsecinone C is compound 3, separately isolated from Aspergillus sp.
    Z120 with stated HPLC purity at least 95%. Its Figure 1 constitution and reported
    NMR data support the hydrated linear-half congener represented natively. Table
    1 gives C MICs in µg/mL: E. coli ATCC35218 4.26; E. coli ATCC25922 2.13; P. aeruginosa
    ATCC27853 17.04; K. pneumoniae ATCC700603 at least 100; S. aureus ATCC43300 34.08;
    E. faecalis ATCC29212 17.04. The last value is C’s own result, distinct from A’s
    4.26. Broth microdilution uses Mueller-Hinton broth, stated 10^5 cells/mL, twofold
    serial dilution, triplicate,24 hours at 30°C and complete growth inhibition measured
    by OD600. These direct assays support antibacterial activity without a universal
    spectrum or clinical assertion.'
  snapshot_sha256: 67710e9ffcac1df267995a1d80f2b3fea59ff33d5ff7a16d77dda14d2a149d91
- evidence_id: fabI
  kind: primary_source
  reference: PMID:27063778; DOI:10.1038/srep24291
  locator: Exact compound 3 biochemical results, Table 3, Figure 3 and recombinant
    protein/MST/enzyme methods.
  accessed_at: '2026-10-21T16:23:48Z'
  support: supports
  summary: Recombinant E. coli K-12 MG1655 FabI is expressed in BL21(DE3) and tested
    directly. Table 3 reports C Kd 270.0±9.1 µM and IC50 3.0 µM. The plotted C MST
    panel instead reports 270±7.3 µM, while its caption mistakenly says fonsecinone
    B. The actual panel, compound table and structure mapping identify C. The enzyme
    assay uses crotonoyl-CoA and NADH; IC50 and Kd are distinct measurements. Direct
    biochemical interaction/inhibition is a useful optional curation lead, but docking
    poses and correlation with MIC do not demonstrate whole-cell FabI causality in
    each tested organism.
  snapshot_sha256: 67710e9ffcac1df267995a1d80f2b3fea59ff33d5ff7a16d77dda14d2a149d91
- evidence_id: primary2011
  kind: primary_source
  reference: PMID:21176790; DOI:10.1016/j.fgb.2010.12.001; https://pmc.ncbi.nlm.nih.gov/articles/PMC3118676/
  locator: Complete indexed abstract and original culture/isolation Methods plus exact-compound
    identification and biosynthetic Results sections.
  accessed_at: '2026-10-21T16:24:42Z'
  support: supports
  summary: 'The study uses A. niger ATCC11414 and identifies fonsecinone C as compound
    8. It explicitly discusses chromatographic interconversion: subfractions B4/B5
    contain equilibrating compounds 8/9 with dehydration products 12/13, and purification
    can alter the profile. This supports association with the fungal culture but does
    not establish that every isolated fraction is stable pure C. Polyketide-synthase
    knockout evidence concerns fungal biosynthesis, not an antibacterial target or
    resistance mechanism. No isolated C antibacterial assay is transferred from this
    paper.'
  snapshot_sha256: 304535e4f00c63dc5b50356ea482b370a77ae82abd7b63c7d879bec4b87f9d17
- evidence_id: source-boundaries
  kind: primary_source
  reference: PMID:27063778; DOI:10.1038/srep24291
  locator: Main article structure, strain, mass, caption and statistical cross-check.
  accessed_at: '2026-10-21T16:23:48Z'
  support: context_only
  summary: The source assigns axial R through ECD comparison and calculation, while
    Figure 1 does not resolve the hemiketal centre. The unread supplement limits independent
    assessment of those stereochemical calculations. Its ATCC35218 ESBL label is retained
    as the authors’ wording rather than independently verified phenotype; one prose
    strain accession and Figure 3 caption also conflict with the tables/plot. The
    reported high-resolution mass/ion annotation is inconsistent with the theoretical
    mass, although formula, other characterization, drawing and current authority
    structures agree. These are source-quality limits for future numerical/mechanistic
    enrichment, not native graph defects.
  snapshot_sha256: 67710e9ffcac1df267995a1d80f2b3fea59ff33d5ff7a16d77dda14d2a149d91
- evidence_id: origin
  kind: database
  reference: CHEBI:133757 compound_origins; DOI:10.1016/S0040-4020(01)88792-5; fungorum:284301;
    https://www.speciesfungorum.org/Names/SynSpecies.asp?RecordID=284301
  locator: Current exact-C ChEBI origin entry, original 1984 publisher/Crossref title
    metadata, current Species Fungorum name page and adopted 2011 isolation text.
  accessed_at: '2026-10-21T16:29:11Z'
  support: context_only
  summary: Current ChEBI associates this exact C congener with A. fonsecaeus NRRL67
    and the 1984 discovery DOI, whose title names that fungus. Species Fungorum resolves
    record 284301 to A. fonsecaeus Thom & Raper and states no synonyms. The native
    A. niger association is supported by the 2011 original, but the inspected sources
    do not establish its priority as the original isolation species. The 1984 full
    text and any historical strain reidentification were not obtained, so the proposed
    wording qualification remains provisional and does not transfer A’s historical
    account automatically to C.
  snapshot_sha256: e0fbb6ab03f34e5c9fd1ed5d0b4e0a9c43663eba38e5b89241f22369309e4bb7
- evidence_id: search
  kind: search
  reference: 454-inclusive-hits.txt; 454-literature.json; 453-literature.json; public
    fetch manifests 453/454
  locator: Hidden- and ignored-inclusive exact local search, both adopted PMID resolutions
    and bounded public family/exact-congener follow-up.
  accessed_at: '2026-10-21T16:30:48Z'
  support: context_only
  summary: The inclusive search finds the exact native/raw rows, distinct A sibling,
    maps and readiness queue. A historical report on another compound only points
    to shared literature and is not scientific evidence here. Both adopted citations
    were resolved; their complete abstracts were read, followed by the 2016 full main
    and relevant 2011 original sections. A narrow literal C title/abstract query returned
    no result, but the broader fonsecinone family query and adopted-source resolution
    recovered the directly relevant 2016 study; the narrow miss is not used as negative
    literature evidence. A-specific 2021 activity and atropisomer data are not transferred
    to C.
  search_scope: 2026-10-21; rg --no-ignore --hidden across data, curation, conf, scripts,
    src, docs, .claude, reviews and reports for CHEBI:133757, fonsecinone, XWHLKURAEUPHAB
    and 5209914. Europe PMC both adopted PMIDs, TITLE_ABS:fonsecinone and bounded
    literal fonsecinone C/discovery DOI query. Exact ChEBI/PubChem and official fungal-name
    lookup.
  snapshot_sha256: 49ca34cfd49b34c41b5eab6f3a8aef29c1b0e5bb11dedc4172af995c3085f720
- evidence_id: checks
  kind: validation
  reference: 454-focused-results.json; 454-chemistry.json; 454-authority-chemistry.json
  locator: Actual focused schema/strict/standalone chemistry and independent authority
    checks.
  accessed_at: '2026-10-21T16:30:48Z'
  support: supports
  summary: All executions exit 0, and the original thirteen input hashes remain unchanged.
    The full key, formula, mass, neutral charge and source mint are consistent. Undefined
    stereo warnings identify scope already visible in the graph; they are not a failed
    parse.
  snapshot_sha256: 3944c9392a8eaeb9718d9a2ffe3ddfb3e78b3d0379035a71f9ef30d6630b1961
assessments:
- assessment_id: identity
  area: identity
  topic: Exact C constitution, synonym and ontology parents
  outcome: supported
  summary: Native and current authority graphs agree and match the exact compound
    3 constitution in the original activity study. C is neither A nor B. Hemiketal
    and axial configuration remain unresolved by the stored encodings; an unspecified
    graph alone is not evidence of a mixture.
  target_ids:
  - CHEBI:133757
  evidence_ids:
  - native
  - identity
  - groundings
  - primary2016
  - source-boundaries
  - checks
- assessment_id: activity
  area: evidence
  topic: Antibacterial role
  outcome: supported
  summary: The original separately measures compound 3 whole-cell activity, binding
    and enzyme inhibition. Its precise strain/material limits and internal inconsistencies
    should accompany any future enrichment, but no native universal potency or causal
    target claim needs correction.
  target_ids:
  - CHEBI:133757
  evidence_ids:
  - primary2016
  - fabI
  - source-boundaries
- assessment_id: history
  area: provenance
  topic: Fungal isolation and historical priority wording
  outcome: concern
  summary: Association with A. niger culture is supported; the original study also
    warns about instability and interconversion. The first-isolation modifier needs
    qualification because the current exact-C origin trail points to A. fonsecaeus
    and the 1984 source remains unavailable in full.
  target_ids:
  - CHEBI:133757
  evidence_ids:
  - primary2011
  - origin
  - native
- assessment_id: completeness
  area: completeness
  topic: Mechanism and optional biological objects
  outcome: supported
  summary: The native record names no gene/protein/pathway/stress-response or dataset,
    so an adapter-first target lookup is not triggered. Direct FabI biochemistry is
    a concrete optional follow-up; biosynthetic proteins, other-congener activity
    and docking predictions are not automatically antibacterial causal mechanisms.
    Absent optional MIC, producer, resistance, clinical and graph objects are not
    independent defects.
  target_ids:
  - CHEBI:133757
  evidence_ids:
  - native
  - fabI
  - primary2011
  - source-boundaries
- assessment_id: provenance
  area: provenance
  topic: Maintained input ownership and adopted lead disposition
  outcome: supported
  summary: All native fields, source row, two adopted citations, role/classification
    logic, registry metadata and history were assessed. Source transfer is reproducible
    and does not claim scientific REVIEWED status.
  target_ids:
  - CHEBI:133757
  evidence_ids:
  - native
  - owners
  - identity
  - search
  - checks
findings:
- finding_id: F1
  issue_key: fonsecinone-c-first-isolation-wording
  category: provenance
  severity: minor
  status: open
  certainty: provisional
  title: Qualify the historical first-isolation modifier
  description: The native definition says originally isolated from A. niger. The current
    exact-C ChEBI origin trail instead associates A. fonsecaeus NRRL67 with the 1984
    discovery citation, while direct A. niger culture evidence comes from the later
    2011 paper. Official Species Fungorum does not list A. niger as a synonym in the
    inspected name record. Because the 1984 full text and historical strain reidentification
    remain unresolved, the correction should preserve supported A. niger association
    while qualifying unverified priority, rather than asserting a definitive new taxonomy.
  target_ids:
  - CHEBI:133757
  field_paths:
  - definition
  evidence_ids:
  - native
  - primary2011
  - origin
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained exact-C definition and origin provenance
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI definition extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition owner
  rule_id: Claim-level source support and precise provenance wording
  native_severity: minor
  normalization_reason: Chemical identity and antibacterial activity are supported.
    The bounded concern is a historical modifier, not a claim that the fungus cannot
    produce the compound.
actions:
- action_id: A1
  description: Resolve or qualify first-isolation wording through maintained source
    ownership.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:133757
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained exact-C definition and origin provenance
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI definition extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition owner
  acceptance_checks:
  - Read the exact 1984 primary source and any authoritative NRRL67 reidentification
    before retaining originally isolated from A. niger. Alternatively retain the supported
    phrase isolated from A. niger with a precise original-source citation and any
    isolation-instability qualification.
  - Apply the change through the maintained ChEBI source or an explicit reproducible
    definition override, regenerate and run focused schema/strict and corpus reproduction.
    Preserve the exact C key and supported antibacterial role.
  generator: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
limitations:
- The 1984 discovery full text was unavailable; original publisher metadata, the exact-C
  authority origin entry and current fungal nomenclature were inspected. Historical
  priority is therefore provisional.
- 'The 2016 supplement could not be retrieved as a valid PDF through the inspected
  PMC/publisher routes: responses were preparation/challenge HTML or a DNS error.
  Additional NMR spectra and ECD calculations are not claimed as independently inspected.'
- The 2011 source explicitly reports interconversion in C-containing fractions. Its
  fungal association does not establish stable pure C in every fraction or direct
  antibacterial activity; the 2016 separately purified compound 3 supports the activity
  assessment.
- The native graph leaves the hemiketal centre and axial configuration unresolved.
  The source’s axial R assignment is not promoted to an experimentally re-established
  absolute identity here.
- Reaxys 5209914 was checked as a current official ChEBI registry association only;
  its underlying record was not accessed. Internal source mass, strain and MST-caption
  discrepancies would require reconciliation before precise numerical or mechanistic
  enrichment.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All thirteen initial input hashes are preserved. Shared literature was independently
  mapped to C’s compound number and assays; no A-specific result was copied as C evidence.
- Optional FabI and MIC enrichment is a future curation opportunity, not a missing-required-field
  defect.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
