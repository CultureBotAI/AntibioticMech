# Gibepyrone A: supported exact polyketide and producer, with bounded activity evidence

- Review: 20261021T173905Z-gibepyrone-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:27:39Z
- Finished UTC: 2026-10-21T17:39:05Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The exact E-configured gibepyrone A structure, systematic names and chemical parents agree with current official chemistry and the original synthesized/natural-compound comparison. The adopted biosynthesis study directly supports Fusarium fujikuroi production, polyketide origin and growth inhibition of the producing fungus. Antibacterial activity is retained honestly as a ChEBI assertion corroborated by the adopted paper’s account of the older original screen; that older full experimental paper was not accessible. No confirmed native defect was found. Biosynthetic genes and transport/regulatory effects are not antibacterial targets, and missing optional mechanism or numerical slots do not require correction. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 502; entire exact native record. All thirteen original input hashes were verified unchanged before judgment. Actual ChEBI inventory, role map, extractor, seeder and decision owners were already present in the preserved capture.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:156363 | data/antibiotics/antibacterial/gibepyrone-a.yaml | generated | gibepyrone A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | CHEBI:156363 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:156363 | Actual focused execution exited 0. |
| Focused chemistry verification | passed | False | CHEBI:156363 | Actual focused execution exited 0. |
| Independent native and chemical authority comparison | passed | False | CHEBI:156363 | All six native, current ChEBI and corroborating PubChem SMILES/InChI encodings match the full E-configured key, formula and neutral charge. |
| Authoritative full QC | failed | True | CHEBI:156363 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:156363 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:156363 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:156363 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:156363 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:156363 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:156363 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:156363 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:156363 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact E structure, names and quantities

identity: supported. Targets: CHEBI:156363.

Native ChEBI and corroborating PubChem chemistry agree; the original synthesized-standard characterization and Figure 1D support the exact pyrone and E geometry. The historical fusalanipyrone Z assignment is kept separate from its later revision.

### All four broader parents and two retained roles

grounding: supported. Targets: CHEBI:156363.

The ring and alkene classes match the graph, isotope/genetic experiments support the polyketide class, and direct fungal-growth inhibition supports the antibiotic-antifungal parent and role. Antibacterial filing preserves the antifungal role and reproduces ChEBI; detailed bacterial-primary confirmation remains limited.

### F.fujikuroi production and broad mycotoxin wording

evidence: supported. Targets: CHEBI:156363.

Culture/standard matching, deletion and complementation provide positive production evidence in IMI58289, beyond occurrence alone. Direct fungal growth inhibition supports toxicity in the broad ChEBI sense. No human-toxicity, clinical or causal rice-disease claim is inferred.

### Independent verification of the exact bacterial screen

evidence: unknown. Targets: CHEBI:156363.

The native antibacterial role is consistent with current ChEBI and the adopted paper’s explicit account of Barrero 1993. The original full table and assay could not be inspected, so this review does not claim independently verified exact MICs, strains, potency comparisons or bacterial mechanism.

### Three adopted leads and optional target/producer/graph enrichment

completeness: supported. Targets: CHEBI:156363.

All three adopted publications were assessed at their stated depths. They primarily concern biosynthesis; none justifies calling a production gene or transporter an antibacterial drug target. Optional absent slots do not require an edit.

### Exact source, role inheritance and seed history

provenance: supported. Targets: CHEBI:156363.

The maintained ChEBI row and generator reproduce the content and both roles. The source-concept mint and exact ChEBI identifier are consistent. The original thirteen hashes and seed-status boundary are retained.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

If extending activity or mechanism coverage, obtain the original antibacterial experiment and preserve assay and biosynthetic boundaries.

- Inspect the exact 1993 compound table and Methods before entering bacterial or yeast MICs. Keep secondary descriptions separate from direct original observations.
- For the 2016 fungal assay, preserve complete medium, 28 degrees C, four-day exposure, ethanol control and relative colony-diameter endpoint; do not reinterpret it as MIC, MFC or a killing percentage.
- Keep Gpy1/Pks8 and related transport/regulation evidence as production context. A new antimicrobial target requires its own exact-compound primary evidence.
- Any structured producer enrichment should identify the actual species, strain, genetic background and analytical confidence: direct F.fujikuroi knockout/complementation differs from tentative F.graminearum HRMS dereplication.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/gibepyrone-a.yaml; Entire YAML: identifier, label, definition, both exact names, four parents, both activity roles, all chemistry, source concept and three history events. | supports | The EXACT ChEBI-grounded, SEEDED record denotes neutral E-configured gibepyrone A. The definition asserts its substituted 2-pyranone constitution, mycotoxin character and production by the rice pathogen F.fujikuroi. Both antibacterial and antifungal roles are retained despite ANTIBACTERIAL filing. There are no external exact xrefs, target, mode, resistance, numerical activity, structured producer item, clinical data, dataset or causal graph. The producer assertion in prose still requires scientific review. History records seeding/reseeding, not sign-off. |
| owners | data/raw/chebi_antimicrobials.tsv:2757; data/raw/chebi_role_names.tsv; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; curation/decisions.tsv; Complete exact ChEBI row and relevant role/class filters, ancestry inheritance and source-aware field seeding; hidden-inclusive exact local search. | supports | The exact inventory row owns the native definition, both synonyms, four parents, chemistry and two roles. It supplies three adopted PMIDs, all resolved and assessed. No exact curator row or decision override was found in the inspected complete tables. The extractor permits reviewed three-star source content and inherits in-scope roles from ancestors, explaining retention of the antifungal role from the antibiotic-antifungal parent. The source-concept mint is reproducible provenance, not a competing exact identifier. |
| identity | CHEBI:156363; pubchem.compound:10103478; Complete official ChEBI entry, current corroborating PubChem structure response and independent parsing of six SMILES/InChI encodings. | supports | All encodings give C10H12O2, charge 0 and FEEGMVBAILJAQO-QPJJXVBHSA-N with the same E side-chain alkene and no tetrahedral stereocentres. The ring and substitution pattern agree with both native systematic names and the definition. Average mass 164.204 and exact mass 164.08373 agree at the stated precision. PubChem is an independent corroboration, not a newly adopted native xref. The record has no external exact xrefs requiring additional identity matching. |
| chemical-parents | CHEBI:26188; CHEBI:75885; CHEBI:78840; CHEBI:86478; CHEBI:33282; CHEBI:35718; Complete official term definitions and exact compound outgoing relations/role classification. | supports | The parents denote polyketide, 2-pyranones, olefinic compound and antibiotic antifungal agent, respectively. The latter is a broader class of microbial metabolites or their derivatives with antifungal properties, not an exact-compound identity or salt. Ring and alkene parents fit the graph; the polyketide parent is independently supported by feeding/genetic experiments, and antifungal activity is supported by the growth assay. The two retained roles mean antibacterial and antifungal agent. The broader ChEBI mycotoxin role is defined as a poisonous substance produced by fungi; this review does not interpret the native wording as demonstrated human foodborne toxicity. |
| producer2016 | PMID:27856636; DOI:10.1074/jbc.M116.753053; https://pmc.ncbi.nlm.nih.gov/articles/PMC5207165/; Original introduction, Results and Discussion, relevant culture/feeding/genetic/analytical Methods and exact gibepyrone A synthetic characterization; Figures 1 and 3 additionally viewed directly. | supports | F.fujikuroi IMI58289 produces a compound matching synthesized gibepyrone A by HPLC-MS and GC-MS retention times and mass spectra. Targeted GPY1/PKS13 deletion eliminates production in independent mutants and in-locus complementation restores it. The authors provide NMR and high-resolution mass characterization of the synthetic standard and explicitly separate a side-chain constitutional isomer formed in the same synthesis. These experiments positively establish production, rather than mere extraction from an associated organism, resistance or chemical transformation. The introduction identifies F.fujikuroi as the rice bakanae pathogen; the review does not infer that gibepyrone A itself causes that disease. |
| polyketide2016 | PMID:27856636; DOI:10.1074/jbc.M116.753053; Feeding Results and Methods, PKS/Ppt1 genetic experiments, proposed biosynthetic pathway and corresponding Discussion. | supports | Isotope incorporation from acetate and methyl-methionine, together with the Ppt1 and Gpy1 mutant/complementation experiments, supports a tetraketide origin with two SAM-derived methyl groups. This is stronger than assigning a terpenoid origin from the C10 formula. Individual proposed catalytic steps and regulatory pathways are not all direct purified-enzyme measurements. Gpy1, Gpy2, P450s, velvet regulators and Sge1 concern production or regulation; they are not demonstrated antibacterial targets of gibepyrone A. |
| antifungal2016 | PMID:27856636; DOI:10.1074/jbc.M116.753053; Gibepyrone A Is Toxic to F.fujikuroi Results and Fungal Strains, Media, and Growth Conditions Methods; supplemental Figure S13 not obtained. | partial | Synthetic gibepyrone A was incorporated into solid complete medium at 0–200 micrograms/mL. F.fujikuroi IMI58289 WT, Δgpy1 and Δgpy2 were incubated for four days at 28 degrees C in the dark; an ethanol solvent control was reported not to inhibit growth. The main text reports colony diameters reduced to approximately 50% and 15% at 100 and 200 micrograms/mL. This directly supports fungal growth inhibition and the native broad antifungal/mycotoxin language. These are relative colony-growth results, not MIC, MFC, lethal fractions or proof of a specific cellular target. The separate S13 image and complete raw data were unavailable. |
| structure-figure | PMID:27856636; DOI:10.1074/jbc.M116.753053; Direct visual inspection of Figure 1D and Figure 3, together with synthetic gibepyrone A characterization and the fusalanipyrone revision passage. | supports | Figure 1D shows gibepyrone A with the native substituted pyrone and E side chain. The paper separately depicts the historically reported Z fusalanipyrone structure, then revises that identification to gibepyrone A using NMR comparisons and chromatographic agreement. The native E structure is supported; the historical Z drawing must not be mistaken for a revision of A to Z. Figure 3 shows loss and restoration of the standard-matching chromatographic peak in the production mutants/complements, with differing signal scales that preclude treating peak heights as directly comparable absolute titers. |
| antibacterial-context | PMID:27856636; DOI:10.1074/jbc.M116.753053; reference31, DOI:10.1016/S0040-4020(01)80514-7; Inspected 2016 Introduction and Discussion, explicitly citing the older primary screen rather than conducting new bacterial/yeast MIC assays. | partial | The adopted 2016 paper reports that gibepyrone A inhibits B.subtilis, S.aureus, S.cerevisiae and C.albicans, with the 100–200 micrograms/mL range attributed to Barrero et al.1993. It distinguishes the narrower B-congener spectrum. This is secondary support for the bacterial/yeast activity of exact A; the 2016 original production and self-growth experiments do not convert that quoted earlier screen into a newly performed antibacterial assay. No numerical bacterial observation is native or added. |
| discovery1993 | DOI:10.1016/S0040-4020(01)80514-7; https://www.sciencedirect.com/science/article/pii/S0040402001805147; Complete original publisher abstract read through the browser; full text requires access and direct fetch returned 403. | partial | The original abstract states that six gibepyrones were identified from G.fujikuroi IMI58289 cultures, structures were determined by spectroscopy and chemical synthesis, and antimicrobial activity was screened. It does not expose the compound-specific table or detailed assay conditions. Thus the exact antibacterial results remain corroborated through the inspected 2016 citation, rather than independently rechecked against the original table. This access limit is not proof the ChEBI role is false. |
| biosynthesis2018 | PMID:30200525; DOI:10.3390/molecules23092232; https://pmc.ncbi.nlm.nih.gov/articles/PMC6225250/; Complete original main Introduction, Results/Discussion and Methods, including chemical-analysis and structural-elucidation sections and Table1 text; supplement not read. | partial | F.graminearum PH-1 overexpressing PKS8 has minor peaks tentatively matching gibepyrone A and B by HRMS dereplication; these peaks were absent in the tested WT conditions. Only gibepyrone D and prolipyrone B were isolated for the reported NMR confirmation. This source therefore does not independently prove a fully recharacterized exact-A natural isolate in every strain or condition. It supports biosynthetic-family context and makes no new antibacterial target measurement. The native definition names F.fujikuroi, whose production is established more directly in the 2016 study. |
| metabolomics2019 | PMID:31344458; DOI:10.1016/j.fgb.2019.103256; Complete original indexed abstract only. | context_only | The original metabolomics/genetics abstract reports isolation of gibepyrone A among metabolites increased in an F.graminearum kmt6 mutant lacking a repressive histone modification. This concerns production after genetic derepression. The abstract does not establish antibacterial mechanism or justify treating Kmt6 as a drug-binding target. No full Methods, compound characterization or supplement from this paper was read. |
| search | 502-inclusive-hits.txt; 502-raw-rows.json; 502-fetch-results.json through502-fetch4-results.json; Hidden- and ignored-inclusive local search; exact chemical authorities and all three adopted PMID/DOIs; bounded original 1993 title/DOI and official supplemental routes. | context_only | The exact record and actual source owners were found before judgment. The local search includes maintained and ignored evidence paths; no exhaustive absence of mechanism literature is asserted. Structured expression adapters are not applicable to the native record because it names no gene, protein, regulator, pathway, stress response or dataset. New biosynthetic genes encountered in primary literature were kept as source context, not used to invent a native antimicrobial mechanism. |
| checks | 502-focused-results.json; 502-chemistry.json; 502-authority-chemistry.json; Actual focused schema, strict and independent internal/authority graph checks; all original input hashes verified. | supports | All executed commands exited 0. Native SMILES/InChI, formula, charge, rounded masses and full key agree, as do both current chemical authorities. All thirteen original input hashes remain unchanged. The deterministic checks do not independently validate the older inaccessible antibacterial experiment. |

## Limits And Additional Notes

- The original 1993 discovery/antimicrobial paper was accessible only as a complete publisher abstract. Its full compound-specific activity table and Methods were not inspected; current ChEBI and the 2016 paper provide corroborating secondary bacterial activity support, not a newly verified exact MIC record.
- The 2016 main text was inspected in the described identity, biosynthesis, toxicity and experimental scope, and Figures 1 and 3 were viewed. The separate supplement, including fungal-growth FigureS13, was not obtained: the PMC index response was a download challenge and its linked publisher route returned 403. Main-text assay results are therefore not independently remeasured from that image.
- The complete 2018 main text was read, but its supplement and raw chromatograms were not reprocessed. Its gibepyrone A assignment is explicitly tentative HRMS dereplication, while the NMR work concerns other metabolites. The 2019 adopted paper remained complete-abstract depth.
- No specific antibacterial cellular mechanism, clinical efficacy or mammalian toxicity was established in this bounded review. Biosynthetic and regulatory experiments do not fill those optional claims.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All three adopted PMIDs were resolved. The 1993 original was followed from the 2016 reference list; its antibacterial results were not silently promoted from secondary narration.
- The current ChEBI entry also contains an Agricola reference and additional species origins outside the adopted three-PMID row. These current source additions were not treated as native claims or automatically imported.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T173905Z-gibepyrone-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Gibepyrone A: supported exact polyketide and producer, with bounded activity
  evidence'
started_at: '2026-10-21T17:27:39Z'
finished_at: '2026-10-21T17:39:05Z'
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
verdict: blocked
scientific_review: true
summary: The exact E-configured gibepyrone A structure, systematic names and chemical
  parents agree with current official chemistry and the original synthesized/natural-compound
  comparison. The adopted biosynthesis study directly supports Fusarium fujikuroi
  production, polyketide origin and growth inhibition of the producing fungus. Antibacterial
  activity is retained honestly as a ChEBI assertion corroborated by the adopted paper’s
  account of the older original screen; that older full experimental paper was not
  accessible. No confirmed native defect was found. Biosynthetic genes and transport/regulatory
  effects are not antibacterial targets, and missing optional mechanism or numerical
  slots do not require correction. Scientific assessment retains the stated evidence
  limits; full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/gibepyrone-a.yaml
    sha256: d880fc1a8effbf0fab8b047dfbf2aad391bd99d2bf0a25f9eb6ca522d584a592
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
- target_id: CHEBI:156363
  path: data/antibiotics/antibacterial/gibepyrone-a.yaml
  label: gibepyrone A
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
  selection: Queue position 502; entire exact native record. All thirteen original
    input hashes were verified unchanged before judgment. Actual ChEBI inventory,
    role map, extractor, seeder and decision owners were already present in the preserved
    capture.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:156363
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:156363
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/gibepyrone-a.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:156363
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/gibepyrone-a.yaml --out /private/tmp/am-review-session/502-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:156363
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 502
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-chemistry
  name: Independent native and chemical authority comparison
  status: passed
  required: false
  summary: All six native, current ChEBI and corroborating PubChem SMILES/InChI encodings
    match the full E-configured key, formula and neutral charge.
  target_ids:
  - CHEBI:156363
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/502-authority-check.py
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
  - CHEBI:156363
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
  - CHEBI:156363
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
  - CHEBI:156363
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
  - CHEBI:156363
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
  - CHEBI:156363
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
  - CHEBI:156363
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
  - CHEBI:156363
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
  - CHEBI:156363
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
  - CHEBI:156363
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/gibepyrone-a.yaml
  locator: 'Entire YAML: identifier, label, definition, both exact names, four parents,
    both activity roles, all chemistry, source concept and three history events.'
  accessed_at: '2026-10-21T17:36:55Z'
  support: supports
  summary: The EXACT ChEBI-grounded, SEEDED record denotes neutral E-configured gibepyrone
    A. The definition asserts its substituted 2-pyranone constitution, mycotoxin character
    and production by the rice pathogen F.fujikuroi. Both antibacterial and antifungal
    roles are retained despite ANTIBACTERIAL filing. There are no external exact xrefs,
    target, mode, resistance, numerical activity, structured producer item, clinical
    data, dataset or causal graph. The producer assertion in prose still requires
    scientific review. History records seeding/reseeding, not sign-off.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv:2757; data/raw/chebi_role_names.tsv;
    conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py;
    curation/decisions.tsv
  locator: Complete exact ChEBI row and relevant role/class filters, ancestry inheritance
    and source-aware field seeding; hidden-inclusive exact local search.
  accessed_at: '2026-10-21T17:36:55Z'
  support: supports
  summary: The exact inventory row owns the native definition, both synonyms, four
    parents, chemistry and two roles. It supplies three adopted PMIDs, all resolved
    and assessed. No exact curator row or decision override was found in the inspected
    complete tables. The extractor permits reviewed three-star source content and
    inherits in-scope roles from ancestors, explaining retention of the antifungal
    role from the antibiotic-antifungal parent. The source-concept mint is reproducible
    provenance, not a competing exact identifier.
  snapshot_sha256: 177ede883703421fe29f24ea9f12a256e956a0627b19251f1ba55b8ab0c69215
- evidence_id: identity
  kind: authority
  reference: CHEBI:156363; pubchem.compound:10103478
  locator: Complete official ChEBI entry, current corroborating PubChem structure
    response and independent parsing of six SMILES/InChI encodings.
  accessed_at: '2026-10-21T17:36:55Z'
  support: supports
  summary: All encodings give C10H12O2, charge 0 and FEEGMVBAILJAQO-QPJJXVBHSA-N with
    the same E side-chain alkene and no tetrahedral stereocentres. The ring and substitution
    pattern agree with both native systematic names and the definition. Average mass
    164.204 and exact mass 164.08373 agree at the stated precision. PubChem is an
    independent corroboration, not a newly adopted native xref. The record has no
    external exact xrefs requiring additional identity matching.
  snapshot_sha256: c94bef40e27e63d15d5388de76fac3e7ecacefedb769eafc6621b4b796922122
- evidence_id: chemical-parents
  kind: authority
  reference: CHEBI:26188; CHEBI:75885; CHEBI:78840; CHEBI:86478; CHEBI:33282; CHEBI:35718
  locator: Complete official term definitions and exact compound outgoing relations/role
    classification.
  accessed_at: '2026-10-21T17:33:39Z'
  support: supports
  summary: The parents denote polyketide, 2-pyranones, olefinic compound and antibiotic
    antifungal agent, respectively. The latter is a broader class of microbial metabolites
    or their derivatives with antifungal properties, not an exact-compound identity
    or salt. Ring and alkene parents fit the graph; the polyketide parent is independently
    supported by feeding/genetic experiments, and antifungal activity is supported
    by the growth assay. The two retained roles mean antibacterial and antifungal
    agent. The broader ChEBI mycotoxin role is defined as a poisonous substance produced
    by fungi; this review does not interpret the native wording as demonstrated human
    foodborne toxicity.
  snapshot_sha256: c6eb230608a7204bd514d4b4f1255f1c7e64038e39a3859729db254f62836452
- evidence_id: producer2016
  kind: primary_source
  reference: PMID:27856636; DOI:10.1074/jbc.M116.753053; https://pmc.ncbi.nlm.nih.gov/articles/PMC5207165/
  locator: Original introduction, Results and Discussion, relevant culture/feeding/genetic/analytical
    Methods and exact gibepyrone A synthetic characterization; Figures 1 and 3 additionally
    viewed directly.
  accessed_at: '2026-10-21T17:34:04Z'
  support: supports
  summary: F.fujikuroi IMI58289 produces a compound matching synthesized gibepyrone
    A by HPLC-MS and GC-MS retention times and mass spectra. Targeted GPY1/PKS13 deletion
    eliminates production in independent mutants and in-locus complementation restores
    it. The authors provide NMR and high-resolution mass characterization of the synthetic
    standard and explicitly separate a side-chain constitutional isomer formed in
    the same synthesis. These experiments positively establish production, rather
    than mere extraction from an associated organism, resistance or chemical transformation.
    The introduction identifies F.fujikuroi as the rice bakanae pathogen; the review
    does not infer that gibepyrone A itself causes that disease.
  snapshot_sha256: 2adbb27d0b53c2588445ec98f794914054792b0b104c80efea8351395564e6f8
- evidence_id: polyketide2016
  kind: primary_source
  reference: PMID:27856636; DOI:10.1074/jbc.M116.753053
  locator: Feeding Results and Methods, PKS/Ppt1 genetic experiments, proposed biosynthetic
    pathway and corresponding Discussion.
  accessed_at: '2026-10-21T17:34:04Z'
  support: supports
  summary: Isotope incorporation from acetate and methyl-methionine, together with
    the Ppt1 and Gpy1 mutant/complementation experiments, supports a tetraketide origin
    with two SAM-derived methyl groups. This is stronger than assigning a terpenoid
    origin from the C10 formula. Individual proposed catalytic steps and regulatory
    pathways are not all direct purified-enzyme measurements. Gpy1, Gpy2, P450s, velvet
    regulators and Sge1 concern production or regulation; they are not demonstrated
    antibacterial targets of gibepyrone A.
  snapshot_sha256: 2adbb27d0b53c2588445ec98f794914054792b0b104c80efea8351395564e6f8
- evidence_id: antifungal2016
  kind: primary_source
  reference: PMID:27856636; DOI:10.1074/jbc.M116.753053
  locator: Gibepyrone A Is Toxic to F.fujikuroi Results and Fungal Strains, Media,
    and Growth Conditions Methods; supplemental Figure S13 not obtained.
  accessed_at: '2026-10-21T17:34:04Z'
  support: partial
  summary: Synthetic gibepyrone A was incorporated into solid complete medium at 0–200
    micrograms/mL. F.fujikuroi IMI58289 WT, Δgpy1 and Δgpy2 were incubated for four
    days at 28 degrees C in the dark; an ethanol solvent control was reported not
    to inhibit growth. The main text reports colony diameters reduced to approximately
    50% and 15% at 100 and 200 micrograms/mL. This directly supports fungal growth
    inhibition and the native broad antifungal/mycotoxin language. These are relative
    colony-growth results, not MIC, MFC, lethal fractions or proof of a specific cellular
    target. The separate S13 image and complete raw data were unavailable.
  snapshot_sha256: 2adbb27d0b53c2588445ec98f794914054792b0b104c80efea8351395564e6f8
- evidence_id: structure-figure
  kind: primary_source
  reference: PMID:27856636; DOI:10.1074/jbc.M116.753053
  locator: Direct visual inspection of Figure 1D and Figure 3, together with synthetic
    gibepyrone A characterization and the fusalanipyrone revision passage.
  accessed_at: '2026-10-21T17:34:51Z'
  support: supports
  summary: Figure 1D shows gibepyrone A with the native substituted pyrone and E side
    chain. The paper separately depicts the historically reported Z fusalanipyrone
    structure, then revises that identification to gibepyrone A using NMR comparisons
    and chromatographic agreement. The native E structure is supported; the historical
    Z drawing must not be mistaken for a revision of A to Z. Figure 3 shows loss and
    restoration of the standard-matching chromatographic peak in the production mutants/complements,
    with differing signal scales that preclude treating peak heights as directly comparable
    absolute titers.
  snapshot_sha256: 73b1a86c57bb0a023992ec4c4e8c11be581e7cad0d8677925740ee8aa11a3289
- evidence_id: antibacterial-context
  kind: database
  reference: PMID:27856636; DOI:10.1074/jbc.M116.753053; reference31, DOI:10.1016/S0040-4020(01)80514-7
  locator: Inspected 2016 Introduction and Discussion, explicitly citing the older
    primary screen rather than conducting new bacterial/yeast MIC assays.
  accessed_at: '2026-10-21T17:34:04Z'
  support: partial
  summary: The adopted 2016 paper reports that gibepyrone A inhibits B.subtilis, S.aureus,
    S.cerevisiae and C.albicans, with the 100–200 micrograms/mL range attributed to
    Barrero et al.1993. It distinguishes the narrower B-congener spectrum. This is
    secondary support for the bacterial/yeast activity of exact A; the 2016 original
    production and self-growth experiments do not convert that quoted earlier screen
    into a newly performed antibacterial assay. No numerical bacterial observation
    is native or added.
  snapshot_sha256: 2adbb27d0b53c2588445ec98f794914054792b0b104c80efea8351395564e6f8
- evidence_id: discovery1993
  kind: primary_source
  reference: DOI:10.1016/S0040-4020(01)80514-7; https://www.sciencedirect.com/science/article/pii/S0040402001805147
  locator: Complete original publisher abstract read through the browser; full text
    requires access and direct fetch returned 403.
  accessed_at: '2026-10-21T17:36:55Z'
  support: partial
  summary: The original abstract states that six gibepyrones were identified from
    G.fujikuroi IMI58289 cultures, structures were determined by spectroscopy and
    chemical synthesis, and antimicrobial activity was screened. It does not expose
    the compound-specific table or detailed assay conditions. Thus the exact antibacterial
    results remain corroborated through the inspected 2016 citation, rather than independently
    rechecked against the original table. This access limit is not proof the ChEBI
    role is false.
- evidence_id: biosynthesis2018
  kind: primary_source
  reference: PMID:30200525; DOI:10.3390/molecules23092232; https://pmc.ncbi.nlm.nih.gov/articles/PMC6225250/
  locator: Complete original main Introduction, Results/Discussion and Methods, including
    chemical-analysis and structural-elucidation sections and Table1 text; supplement
    not read.
  accessed_at: '2026-10-21T17:34:04Z'
  support: partial
  summary: F.graminearum PH-1 overexpressing PKS8 has minor peaks tentatively matching
    gibepyrone A and B by HRMS dereplication; these peaks were absent in the tested
    WT conditions. Only gibepyrone D and prolipyrone B were isolated for the reported
    NMR confirmation. This source therefore does not independently prove a fully recharacterized
    exact-A natural isolate in every strain or condition. It supports biosynthetic-family
    context and makes no new antibacterial target measurement. The native definition
    names F.fujikuroi, whose production is established more directly in the 2016 study.
  snapshot_sha256: 2678c33017425335fb50dd49e765e2cd1e211ed4d17572128d40b0d7cbb46822
- evidence_id: metabolomics2019
  kind: primary_source
  reference: PMID:31344458; DOI:10.1016/j.fgb.2019.103256
  locator: Complete original indexed abstract only.
  accessed_at: '2026-10-21T17:33:39Z'
  support: context_only
  summary: The original metabolomics/genetics abstract reports isolation of gibepyrone
    A among metabolites increased in an F.graminearum kmt6 mutant lacking a repressive
    histone modification. This concerns production after genetic derepression. The
    abstract does not establish antibacterial mechanism or justify treating Kmt6 as
    a drug-binding target. No full Methods, compound characterization or supplement
    from this paper was read.
  snapshot_sha256: 039aad8f199d6ede217aebaf00d7d0b1598d507e08249c33e1a344e70bdebab7
- evidence_id: search
  kind: search
  reference: 502-inclusive-hits.txt; 502-raw-rows.json; 502-fetch-results.json through502-fetch4-results.json
  locator: Hidden- and ignored-inclusive local search; exact chemical authorities
    and all three adopted PMID/DOIs; bounded original 1993 title/DOI and official
    supplemental routes.
  accessed_at: '2026-10-21T17:36:55Z'
  support: context_only
  summary: The exact record and actual source owners were found before judgment. The
    local search includes maintained and ignored evidence paths; no exhaustive absence
    of mechanism literature is asserted. Structured expression adapters are not applicable
    to the native record because it names no gene, protein, regulator, pathway, stress
    response or dataset. New biosynthetic genes encountered in primary literature
    were kept as source context, not used to invent a native antimicrobial mechanism.
  search_scope: 2026-10-21; rg --no-ignore --hidden for gibepyrone A, gibepyrone-a,
    CHEBI156363 and full InChIKey across data, curation, conf, scripts, src, docs,
    .claude, reviews and reports; ChEBI/PubChem, EuropePMC/PMC, original DOI/title
    and official linked supplementary routes.
  snapshot_sha256: 89e7aaddc3f342376c983e645197d3816b7e5c88b8823f0a6d24251303f1bb61
- evidence_id: checks
  kind: validation
  reference: 502-focused-results.json; 502-chemistry.json; 502-authority-chemistry.json
  locator: Actual focused schema, strict and independent internal/authority graph
    checks; all original input hashes verified.
  accessed_at: '2026-10-21T17:36:55Z'
  support: supports
  summary: All executed commands exited 0. Native SMILES/InChI, formula, charge, rounded
    masses and full key agree, as do both current chemical authorities. All thirteen
    original input hashes remain unchanged. The deterministic checks do not independently
    validate the older inaccessible antibacterial experiment.
  snapshot_sha256: d06dc7259ecf4b98289cb1d4a355640407d17d0924a3d5d1ea088b1e31507a09
assessments:
- assessment_id: identity
  area: identity
  topic: Exact E structure, names and quantities
  outcome: supported
  summary: Native ChEBI and corroborating PubChem chemistry agree; the original synthesized-standard
    characterization and Figure 1D support the exact pyrone and E geometry. The historical
    fusalanipyrone Z assignment is kept separate from its later revision.
  target_ids:
  - CHEBI:156363
  evidence_ids:
  - identity
  - structure-figure
  - producer2016
  - checks
- assessment_id: parents
  area: grounding
  topic: All four broader parents and two retained roles
  outcome: supported
  summary: The ring and alkene classes match the graph, isotope/genetic experiments
    support the polyketide class, and direct fungal-growth inhibition supports the
    antibiotic-antifungal parent and role. Antibacterial filing preserves the antifungal
    role and reproduces ChEBI; detailed bacterial-primary confirmation remains limited.
  target_ids:
  - CHEBI:156363
  evidence_ids:
  - chemical-parents
  - polyketide2016
  - antifungal2016
  - antibacterial-context
  - owners
- assessment_id: producer
  area: evidence
  topic: F.fujikuroi production and broad mycotoxin wording
  outcome: supported
  summary: Culture/standard matching, deletion and complementation provide positive
    production evidence in IMI58289, beyond occurrence alone. Direct fungal growth
    inhibition supports toxicity in the broad ChEBI sense. No human-toxicity, clinical
    or causal rice-disease claim is inferred.
  target_ids:
  - CHEBI:156363
  evidence_ids:
  - producer2016
  - polyketide2016
  - antifungal2016
  - chemical-parents
- assessment_id: bacterial-primary
  area: evidence
  topic: Independent verification of the exact bacterial screen
  outcome: unknown
  summary: The native antibacterial role is consistent with current ChEBI and the
    adopted paper’s explicit account of Barrero 1993. The original full table and
    assay could not be inspected, so this review does not claim independently verified
    exact MICs, strains, potency comparisons or bacterial mechanism.
  target_ids:
  - CHEBI:156363
  evidence_ids:
  - antibacterial-context
  - discovery1993
  - search
- assessment_id: coverage
  area: completeness
  topic: Three adopted leads and optional target/producer/graph enrichment
  outcome: supported
  summary: All three adopted publications were assessed at their stated depths. They
    primarily concern biosynthesis; none justifies calling a production gene or transporter
    an antibacterial drug target. Optional absent slots do not require an edit.
  target_ids:
  - CHEBI:156363
  evidence_ids:
  - producer2016
  - biosynthesis2018
  - metabolomics2019
  - native
  - search
- assessment_id: provenance
  area: provenance
  topic: Exact source, role inheritance and seed history
  outcome: supported
  summary: The maintained ChEBI row and generator reproduce the content and both roles.
    The source-concept mint and exact ChEBI identifier are consistent. The original
    thirteen hashes and seed-status boundary are retained.
  target_ids:
  - CHEBI:156363
  evidence_ids:
  - owners
  - native
  - checks
findings: []
actions:
- action_id: A1
  description: If extending activity or mechanism coverage, obtain the original antibacterial
    experiment and preserve assay and biosynthetic boundaries.
  finding_ids: []
  target_ids:
  - CHEBI:156363
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/gibepyrone-a.yaml
    role: Optional curator-owned claim additions through the validated writer
  acceptance_checks:
  - Inspect the exact 1993 compound table and Methods before entering bacterial or
    yeast MICs. Keep secondary descriptions separate from direct original observations.
  - For the 2016 fungal assay, preserve complete medium, 28 degrees C, four-day exposure,
    ethanol control and relative colony-diameter endpoint; do not reinterpret it as
    MIC, MFC or a killing percentage.
  - Keep Gpy1/Pks8 and related transport/regulation evidence as production context.
    A new antimicrobial target requires its own exact-compound primary evidence.
  - 'Any structured producer enrichment should identify the actual species, strain,
    genetic background and analytical confidence: direct F.fujikuroi knockout/complementation
    differs from tentative F.graminearum HRMS dereplication.'
limitations:
- The original 1993 discovery/antimicrobial paper was accessible only as a complete
  publisher abstract. Its full compound-specific activity table and Methods were not
  inspected; current ChEBI and the 2016 paper provide corroborating secondary bacterial
  activity support, not a newly verified exact MIC record.
- 'The 2016 main text was inspected in the described identity, biosynthesis, toxicity
  and experimental scope, and Figures 1 and 3 were viewed. The separate supplement,
  including fungal-growth FigureS13, was not obtained: the PMC index response was
  a download challenge and its linked publisher route returned 403. Main-text assay
  results are therefore not independently remeasured from that image.'
- The complete 2018 main text was read, but its supplement and raw chromatograms were
  not reprocessed. Its gibepyrone A assignment is explicitly tentative HRMS dereplication,
  while the NMR work concerns other metabolites. The 2019 adopted paper remained complete-abstract
  depth.
- No specific antibacterial cellular mechanism, clinical efficacy or mammalian toxicity
  was established in this bounded review. Biosynthetic and regulatory experiments
  do not fill those optional claims.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All three adopted PMIDs were resolved. The 1993 original was followed from the 2016
  reference list; its antibacterial results were not silently promoted from secondary
  narration.
- The current ChEBI entry also contains an Agricola reference and additional species
  origins outside the adopted three-PMID row. These current source additions were
  not treated as native claims or automatically imported.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
