# Acteoside: supported activity and native identity, with conflicting KNApSAcK stereochemistry

- Review: 20261021T083400Z-acteoside
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:25:55Z
- Finished UTC: 2026-10-21T08:34:00Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native exact structure agrees with ChEBI, PubChem and KEGG. Antibacterial and antileishmanial roles have original experimental support. The linked KNApSAcK entry contains conflicting stereochemical representations, a major external identity-link finding; the native structure should be preserved. Optional activity and mechanism enrichment must distinguish bacterial growth inhibition, anti-virulence effects and host pharmacology.

## Scope And Provenance

Whole native record and adopted ChEBI row, all ten source citation abstracts, official chemical identifiers, primary 2022 antibacterial methods/results, additional antileishmanial abstracts and bounded structured protein context.

Selection: Queue076 exact CHEBI:132853 at the locked path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:132853 | data/antibiotics/antibacterial/acteoside.yaml | generated | acteoside |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:132853 | Focused LinkML validation exited 0. |
| strict | passed | True | CHEBI:132853 | Focused strict scan has zero ERROR rows. |
| chemistry | passed | False | CHEBI:132853 | Native SMILES/InChI and source mint agree. |
| external-chemistry | passed | False | CHEBI:132853 | Executed comparison identifies mismatching external representations; script execution success does not mean all xrefs match. |
| adapter-ply | passed | False | CHEBI:132853 | Exact query returned zero genes and zero modules; no component summary applicable. No negative biological inference. |
| adapter-stp1 | passed | False | CHEBI:132853 | Exact query returned zero genes and zero modules; no component summary applicable. No negative biological inference. |
| Authoritative full QC | failed | True | CHEBI:132853 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:132853 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:132853 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:132853 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:132853 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:132853 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:132853 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:132853 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:132853 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Native exact structure

identity: supported. Targets: CHEBI:132853.

Official ChEBI,PubChem and independent KEGG structure agree; definition/synonyms/parents fit the native glycoside.

### KNApSAcK exact equivalence

identity: concern. Targets: CHEBI:132853.

External linked page has mutually inconsistent stereochemical structures; native chemistry is well corroborated.

### Antibacterial and antileishmanial activity roles

evidence: supported. Targets: CHEBI:132853.

Original bacterial and parasite experiments support the broad source roles, with assay limitations retained.

### All adopted publication leads

evidence: supported. Targets: CHEBI:132853.

Ten identifiers resolve to original abstracts; two concern antibacterial/anti-virulence activity and eight concern host/metabolism. Seeder did not misplace these as direct target evidence.

### Optional exact-claim activity and mechanism

completeness: unknown. Targets: CHEBI:132853.

Concrete enrichment is available, but ribosomal binding, membrane channels,host pathways and microbial toxin effects must not be collapsed.

### Producer,resistance,datasets,clinical and graphs

completeness: unknown. Targets: CHEBI:132853.

No such claims are asserted. Plant extraction/occurrence is not independent biosynthetic proof; host studies and meat preservation do not establish clinical antibacterial efficacy.

### Source reproduction and provenance

ownership: supported. Targets: CHEBI:132853.

Adopted ChEBI row/extractor/seeder own xref follow-up; actual native record owns separately curated optional fields. Captured hashes unchanged.

### Focused native gates

schema: supported. Targets: CHEBI:132853.

Documented focused validators and native chemistry pass despite external xref finding.

## Findings

### F1: KNApSAcK chemical xref does not currently establish exact stereochemical equivalence

major / open / confirmed; issue key: acteoside-knapsack-c00002783-stereochemical-conflict.

The linked entry labels acteoside correctly but its displayed key, InChI and SMILES disagree with each other and with the corroborated native exact structure. Its InChI reverses one specified centre; its SMILES additionally leaves four centres unspecified. Preserve native ChEBI chemistry and adjudicate the external equivalence claim. This is not a wrong-whole-record identity finding.

### F2: Add narrow activity and mechanism evidence when curator scope permits

informational / open / confirmed; issue key: acteoside-qualified-activity-mechanism-evidence-enrichment.

Original antibacterial and antileishmanial studies supply optional claim-level evidence. Preserve strain,assay,endpoint and source inconsistencies; distinguish direct bacterial growth inhibition from nonbacteriostatic pneumolysin effects, host pharmacology and indirect membrane/protein-synthesis phenotypes.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate the KNApSAcK equivalence in the maintained source path while preserving supported native chemistry.

- Reinspect all C00002783 structural representations and compare independently parsed full stereochemical structures against CHEBI:132853.
- Resolve through upstream correction or documented source/extractor qualification or exclusion of this exact-equivalence xref; a label match alone is insufficient. Do not mutate raw snapshots ad hoc or change native chemistry to match an external error.
- Reseed through the native workflow, then schema/strict,chemistry,source reproduction and required shared gates.

### A2

Optionally curate original assay and mechanistic observations on the actual native record.

- Preserve exact material,CAS,organism/strain,medium,inoculum,time,units and measured endpoint; do not infer clinical resistance from unusually high experimental MICs without applicable breakpoints.
- For2022 use Table2 PA69 FICI0.281 with the conflicting narrative recorded; document differing inoculum descriptions and incomplete biofilm methods.
- Separate pneumolysin anti-virulence from growth inhibition, Leishmania arginase from host immune effects, and precursor incorporation or dye/ATP responses from direct binding/channel evidence. Obtain full older primary methods before detailed mechanism coding.
- Do not extrapolate cytotoxicity at≤200µM to safety at bacterial MICs or plant occurrence to biosynthetic producer proof.
- Use write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/acteoside.yaml; retain SEEDED until native scientific review requirements are independently fulfilled; rerun focused and shared gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/acteoside.yaml; Entire native YAML after input capture. | supports | SEEDED/EXACT acteoside, neutral C29H36O15 with ten specified centres and trans-caffeate. Four exact synonyms, five structural parents, antibacterial and antileishmanial roles, five chemical xrefs, one document xref, one CHEBI source concept and four seed/reseed events. Optional claim evidence, activity, target, producer, resistance, dataset and graph collections are absent. |
| source | data/raw/chebi_antimicrobials.tsv; Exact source line2503 in076-raw.json; extractor176–339, seeder1483–1660, source config, role map and manifest. | supports | Native fields reproduce the maintained ChEBI row, including external identifiers. The row has ten PMID leads and no mechanism role IDs. Seeder intentionally does not convert source citations into claim-level evidence. Source role labels33282/70868 and CHEBI mint4620cc1fd6 match. All13 initially captured maintained hashes remain unchanged. |
| identity | https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:132853; Complete official076-chebi.html/txt;076-pubchem.json;076-kegg.txt and076-kegg.mol. | supports | ChEBI confirms label, definition, all four synonyms, five parents and both native roles. PubChem CID5281800 and KEGG C10501 MOL match full key FBSKJMQYURKNSU-ZLSOWSIRSA-N. CAS61276-17-3 is corroborated by these source entries, not directly by the registry. HMDB0034843 and Reaxys1278646 are corroborated in ChEBI only; HMDB page/XML were inaccessible403 and Reaxys was not inspected. Wikipedia Verbascoside resolves as a document about the intended compound, not primary biological evidence. |
| chemistry | Independent RDKit calculation; 076-chemistry.json/log and076-xref-chemistry.json. | supports | Native SMILES and InChI parse to the same neutral single fragment, ten specified stereocentres, formula C29H36O15, average mass624.592 and exact mass624.205420452. The source-specific minted identifier matches. KEGG MOL independently reproduces the native full InChIKey. |
| xref-conflict | http://www.knapsackfamily.com/knapsack_core/information.php?word=C00002783; Complete076-knapsack.html/txt; independently parsed076-xref-chemistry.json. | refutes | Names/CAS/formula match, but displayed key is FBSKJMQYURKNSU-OQSHRHNDNA-N. Displayed InChI has canonical centre23- where native has23+, and parses to FBSKJMQYURKNSU-SHHXCPTCSA-N. Displayed SMILES yields FBSKJMQYURKNSU-LAGMRWIXSA-N with four unspecified centres. These mutually inconsistent external representations cannot establish exact stereochemical equivalence to native ZLSOWSIRSA. This is an external-entry conflict, not evidence that native ChEBI chemistry is wrong. |
| adopted-bacterial | PMID:10432210; Complete original abstract in076-adopted-abstracts.txt; DOI10.1016/S0378-8741(98)00203-7 verified076-epmc.json. | supports | The1999 study names verbascoside isolated from Buddleja cordata and reports lethal effects on S.aureus using kill kinetics and precursor incorporation, including reduced leucine incorporation. This supports antibacterial activity and a protein-synthesis phenotype; abstract alone does not establish a direct ribosomal binding target or assay-specific numeric values. Full publisher text was inaccessible. |
| adopted-antivirulence | PMID:26700563; Complete original abstract; DOI10.1124/mol.115.100610. | context_only | The pneumolysin study explicitly describes verbascoside as nonbacteriostatic under its conditions. Simulation and mutational analysis support a proposed D3/D4 cleft interaction that impedes toxin oligomerization; hemolysis, A549 injury and mouse pneumonia are measured effects. This is anti-virulence support, not a bacterial-growth MIC or proof that every antibacterial phenotype shares this target. Full text inaccessible. |
| adopted-other | Ten adopted PMID records in Europe PMC; All ten complete abstracts read;076-epmc.json and076-adopted-abstracts.txt. | context_only | The remaining eight are distinct host/metabolic contexts: PMID25628651 DOI10.1155/2015/327872, mouse methotrexate mucositis;25900014 DOI10.1002/ptr.5357, senescent-mouse memory/NGF-TrkA;25900087 DOI10.1002/ptr.5358, memory/caspase-NOS;26427909 DOI10.3109/13880209.2015.1072830, human PBMC/THP1 immune activity and cytotoxicity;26453510 DOI10.1016/j.intimp.2015.09.026, THP1 IL32/caspase/NFkB;26827721 DOI10.1016/j.neulet.2016.01.042, exercised-rat fatigue/serotonin;26856531 DOI10.1002/bmc.3698, rat echinacoside/acteoside metabolism;26981096 DOI10.4103/1673-5374.175053, Parkinsonian-rat neuronal response. These do not independently establish antimicrobial targets, clinical antibacterial efficacy, producer biosynthesis or resistance. Introductory antibacterial/clinical statements were not transferred. |
| antileishmania | PMID:27096224; PMID:28017773; Complete original abstracts in076-extra-epmc.json; verified DOI10.1021/acs.jnatprod.5b00875 and10.1016/j.bcp.2016.12.018. | supports | 2016 exact verbascoside1 inhibits L.amazonensis promastigote growth, EC50 19µM, and competitively inhibits arginase, Ki0.7µM; docking is computational context.2017 reports intracellular amastigote EC50 32µM and parasite/host arginase selectivity. These support the broad antileishmanial role. Proposed downstream trypanothione mechanisms require full-text evaluation before causal entries. ACS full text unavailable; UniPisa institutional page confirms the2016 abstract but explicitly has no attached files. |
| 2022-activity | https://doi.org/10.3390/molecules27154943; PMID35956890,PMC9370273;076-2022.xml and extracted full main body; Methods2.1–2.4,Results3.1–3.2,Tables1–2. | supports | Commercial verbascoside CAS61276-17-3,purity≥98%, was tested by24h TSB microdilution at37°C with visual no-growth endpoint. MICs in µg/mL: S.aureus ATCC25923 2500,SA575 2500,SA596 625; P.aeruginosa ATCC15442 1250,PA69 625,PA261 2500. Table2 PA69 FICI is0.281; narrative0.0281 is inconsistent and arithmetic supports0.281. Methods2.3 imply about5×10^6CFU/mL final inoculum, while combination2.4 states5×10^5. Preserve these qualifications and do not relabel assays as a standard clinical resistance determination. |
| 2022-mechanism | https://doi.org/10.3390/molecules27154943; Full main body Methods2.5–2.12,Results3.3–3.9 and conclusion in076-2022-body.txt. | context_only | At625–1250µg/mL in SA596/PA69, ATP,pH,potential-dye,conductivity,fluorescence and microscopy assays indicate membrane/energy disruption. They do not directly measure a particular channel or drug-protein binding. SEM discussion itself notes no obvious S.aureus morphological injury. Host viability was tested only up to200µM, below antibacterial MIC concentrations; this cannot establish safety at MIC. Biofilm treatment timing is incompletely specified. The inoculated refrigerated-meat model is not clinical evidence. |
| adapter | iModulonDB public adapter; Same-session055 successful dataset inventory;076-imodulondb-ply.txt and076-imodulondb-stp1.txt. | context_only | Exact searches returned no gene/module hits in s_pneumoniae/precise718 for ply and s_aureus/staph_precise108 for stp1. No module summary applies. The Stp1 literature lead resolves to aurintricarboxylic acid, not acteoside, in PMID27499528 DOI10.1016/j.chembiol.2016.06.014 and is rejected. No applicable Leishmania dataset in inspected inventory; absence is not negative biological evidence. |
| search | CultureBotAI/AntibioticMech; 076-local-hits.txt and076-maintained-search.txt; bounded official and primary name/identifier queries. | context_only | Ignored-inclusive searches found no target-specific decision, overlay or prior review in the searched maintained review/source paths beyond source/queue occurrences. No exhaustive literature-absence claim. Primary exact-name work confirms bacterial and parasite activity while distinguishing toxin/host contexts. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity/equivalence,source support,activity,target and completeness sections;CLAUDE and HARMONIZATION. | supports | Chemical xrefs require exact structure; a shared name does not resolve conflicting stereochemistry. Optional collections require narrow claim evidence when added but are not mandatory in a SEEDED record. Current source assertions do not justify automatic scientific-status promotion. |
| validation | Focused documented native gates; 076-focused-results.json, schema/strict logs and TSV;076-chemistry.json. | supports | Schema, strict and independent native chemistry pass. Actual shared corpus gates are included in the finalized review; pinned SciPy prevents full QC and chemical-map completion. |

## Limits And Additional Notes

- All 13 initially captured maintained hashes remain unchanged. Actual shared gates are recorded in this review; full QC and chemical-map completion are limited by the pinned SciPy binary.
- All ten adopted original abstracts were inspected; most full papers were not. The1999 antibacterial and2016 pneumolysin publisher full text were inaccessible. Additional antileishmanial studies remain abstract-only after bounded official routes; UniPisa explicitly has no full-text file.
- The2022 original main text,methods and structured tables were read completely. No raw datasets or supplemental biofilm protocol were reanalysed; reported method and narrative inconsistencies are preserved.
- HMDB page/XML returned403; Reaxys and CAS registry were not directly inspected. Their identifiers are corroborated through adopted/current ChEBI and accessible other official entries; no claim that every xref is independently verified.
- Current KNApSAcK external structure conflict does not refute native structure or measured activity. Direct origin of the upstream inconsistency is unresolved.
- Adapter searches used previously inspected successful dataset inventory; zero hits do not establish gene absence or no mechanism. No matching Leishmania dataset was available in that inventory.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T083400Z-acteoside
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Acteoside: supported activity and native identity, with conflicting KNApSAcK
  stereochemistry'
started_at: '2026-10-21T08:25:55Z'
finished_at: '2026-10-21T08:34:00Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author record; captured maintained inputs before judgment,
    read entire native record and source row, source transform/seeder, official identifiers,
    all ten adopted abstracts and original antibacterial full text.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The native exact structure agrees with ChEBI, PubChem and KEGG. Antibacterial
  and antileishmanial roles have original experimental support. The linked KNApSAcK
  entry contains conflicting stereochemical representations, a major external identity-link
  finding; the native structure should be preserved. Optional activity and mechanism
  enrichment must distinguish bacterial growth inhibition, anti-virulence effects
  and host pharmacology.
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
  - path: data/antibiotics/antibacterial/acteoside.yaml
    sha256: 5365ffcaeb9ff3a31748112f1c1c00c88e14b5342c139bebeafe2a2f1d1bdcb8
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
- target_id: CHEBI:132853
  path: data/antibiotics/antibacterial/acteoside.yaml
  label: acteoside
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
  description: Whole native record and adopted ChEBI row, all ten source citation
    abstracts, official chemical identifiers, primary 2022 antibacterial methods/results,
    additional antileishmanial abstracts and bounded structured protein context.
  selection: Queue076 exact CHEBI:132853 at the locked path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:132853
  exclusions:
  - target: Isoverbascoside, related glycosides, plant extracts, host pharmacology
      and aurintricarboxylic acid
    reason: Adjacent structures and mixed extracts cannot support exact-compound claims;
      host effects are not microbial target evidence.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Focused LinkML validation exited 0.
  target_ids:
  - CHEBI:132853
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/acteoside.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Focused strict scan has zero ERROR rows.
  target_ids:
  - CHEBI:132853
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/acteoside.yaml --out /private/tmp/am-review-session/076-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Native SMILES/InChI and source mint agree.
  target_ids:
  - CHEBI:132853
  evidence_ids:
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache .venv/bin/python
    /private/tmp/am-review-session/076-chemistry-check.py 76
  exit_code: 0
  expected_exit_code: 0
- check_id: external-chemistry
  name: external-chemistry
  status: passed
  required: false
  summary: Executed comparison identifies mismatching external representations; script
    execution success does not mean all xrefs match.
  target_ids:
  - CHEBI:132853
  evidence_ids:
  - xref-conflict
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache .venv/bin/python
    /private/tmp/am-review-session/076-xref-chem.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-ply
  name: adapter-ply
  status: passed
  required: false
  summary: Exact query returned zero genes and zero modules; no component summary
    applicable. No negative biological inference.
  target_ids:
  - CHEBI:132853
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 search --organism s_pneumoniae --dataset
    precise718 --query ply
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-stp1
  name: adapter-stp1
  status: passed
  required: false
  summary: Exact query returned zero genes and zero modules; no component summary
    applicable. No negative biological inference.
  target_ids:
  - CHEBI:132853
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 search --organism s_aureus --dataset
    staph_precise108 --query stp1
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
  - CHEBI:132853
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
  - CHEBI:132853
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
  - CHEBI:132853
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
  - CHEBI:132853
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
  - CHEBI:132853
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
  - CHEBI:132853
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
  - CHEBI:132853
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
  - CHEBI:132853
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
  - CHEBI:132853
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/acteoside.yaml
  locator: Entire native YAML after input capture.
  accessed_at: '2026-10-21T08:31:03Z'
  support: supports
  summary: SEEDED/EXACT acteoside, neutral C29H36O15 with ten specified centres and
    trans-caffeate. Four exact synonyms, five structural parents, antibacterial and
    antileishmanial roles, five chemical xrefs, one document xref, one CHEBI source
    concept and four seed/reseed events. Optional claim evidence, activity, target,
    producer, resistance, dataset and graph collections are absent.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Exact source line2503 in076-raw.json; extractor176–339, seeder1483–1660,
    source config, role map and manifest.
  accessed_at: '2026-10-21T08:31:03Z'
  support: supports
  summary: Native fields reproduce the maintained ChEBI row, including external identifiers.
    The row has ten PMID leads and no mechanism role IDs. Seeder intentionally does
    not convert source citations into claim-level evidence. Source role labels33282/70868
    and CHEBI mint4620cc1fd6 match. All13 initially captured maintained hashes remain
    unchanged.
  snapshot_sha256: e41d073f6ce662ea897bc696ae6d50fbf9d34f8cb09bea25981659af36b543d9
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:132853
  locator: Complete official076-chebi.html/txt;076-pubchem.json;076-kegg.txt and076-kegg.mol.
  accessed_at: '2026-10-21T08:31:03Z'
  support: supports
  summary: ChEBI confirms label, definition, all four synonyms, five parents and both
    native roles. PubChem CID5281800 and KEGG C10501 MOL match full key FBSKJMQYURKNSU-ZLSOWSIRSA-N.
    CAS61276-17-3 is corroborated by these source entries, not directly by the registry.
    HMDB0034843 and Reaxys1278646 are corroborated in ChEBI only; HMDB page/XML were
    inaccessible403 and Reaxys was not inspected. Wikipedia Verbascoside resolves
    as a document about the intended compound, not primary biological evidence.
  snapshot_sha256: 4236b8699f66c3fc372a5524aa9769c7be9976336980eac10405d2e2049066e6
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculation
  locator: 076-chemistry.json/log and076-xref-chemistry.json.
  accessed_at: '2026-10-21T08:31:03Z'
  support: supports
  summary: Native SMILES and InChI parse to the same neutral single fragment, ten
    specified stereocentres, formula C29H36O15, average mass624.592 and exact mass624.205420452.
    The source-specific minted identifier matches. KEGG MOL independently reproduces
    the native full InChIKey.
  snapshot_sha256: 41152be24429b1122fad61cb329be37c6155d9d587be250f5fb513ea447485ac
- evidence_id: xref-conflict
  kind: database
  reference: http://www.knapsackfamily.com/knapsack_core/information.php?word=C00002783
  locator: Complete076-knapsack.html/txt; independently parsed076-xref-chemistry.json.
  accessed_at: '2026-10-21T08:31:03Z'
  support: refutes
  summary: Names/CAS/formula match, but displayed key is FBSKJMQYURKNSU-OQSHRHNDNA-N.
    Displayed InChI has canonical centre23- where native has23+, and parses to FBSKJMQYURKNSU-SHHXCPTCSA-N.
    Displayed SMILES yields FBSKJMQYURKNSU-LAGMRWIXSA-N with four unspecified centres.
    These mutually inconsistent external representations cannot establish exact stereochemical
    equivalence to native ZLSOWSIRSA. This is an external-entry conflict, not evidence
    that native ChEBI chemistry is wrong.
  snapshot_sha256: ea87dddf5727d526c191243ea9c3a31803f9db585072464dc72ae466bf242262
- evidence_id: adopted-bacterial
  kind: primary_source
  reference: PMID:10432210
  locator: Complete original abstract in076-adopted-abstracts.txt; DOI10.1016/S0378-8741(98)00203-7
    verified076-epmc.json.
  accessed_at: '2026-10-21T08:31:03Z'
  support: supports
  summary: The1999 study names verbascoside isolated from Buddleja cordata and reports
    lethal effects on S.aureus using kill kinetics and precursor incorporation, including
    reduced leucine incorporation. This supports antibacterial activity and a protein-synthesis
    phenotype; abstract alone does not establish a direct ribosomal binding target
    or assay-specific numeric values. Full publisher text was inaccessible.
  snapshot_sha256: 0bae455f68f61c4488e4d80909256613bf2fd5b86e412c4e3a39081c7cc35130
- evidence_id: adopted-antivirulence
  kind: primary_source
  reference: PMID:26700563
  locator: Complete original abstract; DOI10.1124/mol.115.100610.
  accessed_at: '2026-10-21T08:31:03Z'
  support: context_only
  summary: The pneumolysin study explicitly describes verbascoside as nonbacteriostatic
    under its conditions. Simulation and mutational analysis support a proposed D3/D4
    cleft interaction that impedes toxin oligomerization; hemolysis, A549 injury and
    mouse pneumonia are measured effects. This is anti-virulence support, not a bacterial-growth
    MIC or proof that every antibacterial phenotype shares this target. Full text
    inaccessible.
  snapshot_sha256: 0bae455f68f61c4488e4d80909256613bf2fd5b86e412c4e3a39081c7cc35130
- evidence_id: adopted-other
  kind: primary_source
  reference: Ten adopted PMID records in Europe PMC
  locator: All ten complete abstracts read;076-epmc.json and076-adopted-abstracts.txt.
  accessed_at: '2026-10-21T08:31:03Z'
  support: context_only
  summary: 'The remaining eight are distinct host/metabolic contexts: PMID25628651
    DOI10.1155/2015/327872, mouse methotrexate mucositis;25900014 DOI10.1002/ptr.5357,
    senescent-mouse memory/NGF-TrkA;25900087 DOI10.1002/ptr.5358, memory/caspase-NOS;26427909
    DOI10.3109/13880209.2015.1072830, human PBMC/THP1 immune activity and cytotoxicity;26453510
    DOI10.1016/j.intimp.2015.09.026, THP1 IL32/caspase/NFkB;26827721 DOI10.1016/j.neulet.2016.01.042,
    exercised-rat fatigue/serotonin;26856531 DOI10.1002/bmc.3698, rat echinacoside/acteoside
    metabolism;26981096 DOI10.4103/1673-5374.175053, Parkinsonian-rat neuronal response.
    These do not independently establish antimicrobial targets, clinical antibacterial
    efficacy, producer biosynthesis or resistance. Introductory antibacterial/clinical
    statements were not transferred.'
  snapshot_sha256: 0bae455f68f61c4488e4d80909256613bf2fd5b86e412c4e3a39081c7cc35130
- evidence_id: antileishmania
  kind: primary_source
  reference: PMID:27096224; PMID:28017773
  locator: Complete original abstracts in076-extra-epmc.json; verified DOI10.1021/acs.jnatprod.5b00875
    and10.1016/j.bcp.2016.12.018.
  accessed_at: '2026-10-21T08:31:03Z'
  support: supports
  summary: 2016 exact verbascoside1 inhibits L.amazonensis promastigote growth, EC50
    19µM, and competitively inhibits arginase, Ki0.7µM; docking is computational context.2017
    reports intracellular amastigote EC50 32µM and parasite/host arginase selectivity.
    These support the broad antileishmanial role. Proposed downstream trypanothione
    mechanisms require full-text evaluation before causal entries. ACS full text unavailable;
    UniPisa institutional page confirms the2016 abstract but explicitly has no attached
    files.
  snapshot_sha256: 0a2573cb173c12f61120447276a67aeeaf3cdaf3e9732063cc60f2c406fb64af
- evidence_id: 2022-activity
  kind: primary_source
  reference: https://doi.org/10.3390/molecules27154943
  locator: PMID35956890,PMC9370273;076-2022.xml and extracted full main body; Methods2.1–2.4,Results3.1–3.2,Tables1–2.
  accessed_at: '2026-10-21T08:31:03Z'
  support: supports
  summary: 'Commercial verbascoside CAS61276-17-3,purity≥98%, was tested by24h TSB
    microdilution at37°C with visual no-growth endpoint. MICs in µg/mL: S.aureus ATCC25923
    2500,SA575 2500,SA596 625; P.aeruginosa ATCC15442 1250,PA69 625,PA261 2500. Table2
    PA69 FICI is0.281; narrative0.0281 is inconsistent and arithmetic supports0.281.
    Methods2.3 imply about5×10^6CFU/mL final inoculum, while combination2.4 states5×10^5.
    Preserve these qualifications and do not relabel assays as a standard clinical
    resistance determination.'
  snapshot_sha256: 81a1043e966be9662d3cb41e80336e989c8ae0d54b73c3e900aef56227549551
- evidence_id: 2022-mechanism
  kind: primary_source
  reference: https://doi.org/10.3390/molecules27154943
  locator: Full main body Methods2.5–2.12,Results3.3–3.9 and conclusion in076-2022-body.txt.
  accessed_at: '2026-10-21T08:31:03Z'
  support: context_only
  summary: At625–1250µg/mL in SA596/PA69, ATP,pH,potential-dye,conductivity,fluorescence
    and microscopy assays indicate membrane/energy disruption. They do not directly
    measure a particular channel or drug-protein binding. SEM discussion itself notes
    no obvious S.aureus morphological injury. Host viability was tested only up to200µM,
    below antibacterial MIC concentrations; this cannot establish safety at MIC. Biofilm
    treatment timing is incompletely specified. The inoculated refrigerated-meat model
    is not clinical evidence.
  snapshot_sha256: 81a1043e966be9662d3cb41e80336e989c8ae0d54b73c3e900aef56227549551
- evidence_id: adapter
  kind: database
  reference: iModulonDB public adapter
  locator: Same-session055 successful dataset inventory;076-imodulondb-ply.txt and076-imodulondb-stp1.txt.
  accessed_at: '2026-10-21T08:31:03Z'
  support: context_only
  summary: Exact searches returned no gene/module hits in s_pneumoniae/precise718
    for ply and s_aureus/staph_precise108 for stp1. No module summary applies. The
    Stp1 literature lead resolves to aurintricarboxylic acid, not acteoside, in PMID27499528
    DOI10.1016/j.chembiol.2016.06.014 and is rejected. No applicable Leishmania dataset
    in inspected inventory; absence is not negative biological evidence.
  snapshot_sha256: 3460e8122697a947d227ad3929790a5e6e4999fba7514a1805a3a219f0f8c884
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 076-local-hits.txt and076-maintained-search.txt; bounded official and primary
    name/identifier queries.
  accessed_at: '2026-10-21T08:31:03Z'
  support: context_only
  summary: Ignored-inclusive searches found no target-specific decision, overlay or
    prior review in the searched maintained review/source paths beyond source/queue
    occurrences. No exhaustive literature-absence claim. Primary exact-name work confirms
    bacterial and parasite activity while distinguishing toxin/host contexts.
  search_scope: rg --no-ignore --hidden across batch008, excluding.git/.venv, for
    acteoside,verbascoside,CHEBI:132853,132853,4620cc1fd6 and FBSKJMQYURKNSU; maintained
    curation/conf/scripts/data/raw/reports/reviews. Official ChEBI/PubChem/KEGG/KNApSAcK/HMDB
    and bounded PubMed/EuropePMC/publisher/UniPisa exact-name and DOI searches.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity/equivalence,source support,activity,target and completeness sections;CLAUDE
    and HARMONIZATION.
  accessed_at: '2026-10-21T08:31:03Z'
  support: supports
  summary: Chemical xrefs require exact structure; a shared name does not resolve
    conflicting stereochemistry. Optional collections require narrow claim evidence
    when added but are not mandatory in a SEEDED record. Current source assertions
    do not justify automatic scientific-status promotion.
- evidence_id: validation
  kind: validation
  reference: Focused documented native gates
  locator: 076-focused-results.json, schema/strict logs and TSV;076-chemistry.json.
  accessed_at: '2026-10-21T08:31:03Z'
  support: supports
  summary: Schema, strict and independent native chemistry pass. Actual shared corpus
    gates are included in the finalized review; pinned SciPy prevents full QC and
    chemical-map completion.
  snapshot_sha256: 641d9d4d1f980a29797c71d3d76d0fca938cc2407c530a1861ef044624131822
assessments:
- assessment_id: identity
  area: identity
  topic: Native exact structure
  outcome: supported
  summary: Official ChEBI,PubChem and independent KEGG structure agree; definition/synonyms/parents
    fit the native glycoside.
  target_ids:
  - CHEBI:132853
  evidence_ids:
  - identity
  - chemistry
  - source
- assessment_id: xref
  area: identity
  topic: KNApSAcK exact equivalence
  outcome: concern
  summary: External linked page has mutually inconsistent stereochemical structures;
    native chemistry is well corroborated.
  target_ids:
  - CHEBI:132853
  evidence_ids:
  - xref-conflict
  - identity
  - chemistry
  - rubric
- assessment_id: roles
  area: evidence
  topic: Antibacterial and antileishmanial activity roles
  outcome: supported
  summary: Original bacterial and parasite experiments support the broad source roles,
    with assay limitations retained.
  target_ids:
  - CHEBI:132853
  evidence_ids:
  - adopted-bacterial
  - 2022-activity
  - antileishmania
- assessment_id: citations
  area: evidence
  topic: All adopted publication leads
  outcome: supported
  summary: Ten identifiers resolve to original abstracts; two concern antibacterial/anti-virulence
    activity and eight concern host/metabolism. Seeder did not misplace these as direct
    target evidence.
  target_ids:
  - CHEBI:132853
  evidence_ids:
  - source
  - adopted-bacterial
  - adopted-antivirulence
  - adopted-other
- assessment_id: mechanism
  area: completeness
  topic: Optional exact-claim activity and mechanism
  outcome: unknown
  summary: Concrete enrichment is available, but ribosomal binding, membrane channels,host
    pathways and microbial toxin effects must not be collapsed.
  target_ids:
  - CHEBI:132853
  evidence_ids:
  - 2022-activity
  - 2022-mechanism
  - adopted-bacterial
  - adopted-antivirulence
  - antileishmania
  - adapter
- assessment_id: other
  area: completeness
  topic: Producer,resistance,datasets,clinical and graphs
  outcome: unknown
  summary: No such claims are asserted. Plant extraction/occurrence is not independent
    biosynthetic proof; host studies and meat preservation do not establish clinical
    antibacterial efficacy.
  target_ids:
  - CHEBI:132853
  evidence_ids:
  - record
  - adopted-other
  - 2022-mechanism
  - rubric
- assessment_id: ownership
  area: ownership
  topic: Source reproduction and provenance
  outcome: supported
  summary: Adopted ChEBI row/extractor/seeder own xref follow-up; actual native record
    owns separately curated optional fields. Captured hashes unchanged.
  target_ids:
  - CHEBI:132853
  evidence_ids:
  - source
  - search
- assessment_id: gates
  area: schema
  topic: Focused native gates
  outcome: supported
  summary: Documented focused validators and native chemistry pass despite external
    xref finding.
  target_ids:
  - CHEBI:132853
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: acteoside-knapsack-c00002783-stereochemical-conflict
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: KNApSAcK chemical xref does not currently establish exact stereochemical
    equivalence
  description: The linked entry labels acteoside correctly but its displayed key,
    InChI and SMILES disagree with each other and with the corroborated native exact
    structure. Its InChI reverses one specified centre; its SMILES additionally leaves
    four centres unspecified. Preserve native ChEBI chemistry and adjudicate the external
    equivalence claim. This is not a wrong-whole-record identity finding.
  target_ids:
  - CHEBI:132853
  field_paths:
  - xrefs
  evidence_ids:
  - xref-conflict
  - identity
  - chemistry
  - source
  - rubric
  rule_id: 'native-review-checklist: Identity/Equivalence; HARMONIZATION chemical
    xref exact-structure invariant'
  native_severity: major exact-stereochemistry link conflict
  normalization_reason: The native exact compound is supported, but an asserted chemical-equivalence
    link has a confirmed structural conflict. Whole-record blocker severity is unwarranted.
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
- finding_id: F2
  issue_key: acteoside-qualified-activity-mechanism-evidence-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Add narrow activity and mechanism evidence when curator scope permits
  description: Original antibacterial and antileishmanial studies supply optional
    claim-level evidence. Preserve strain,assay,endpoint and source inconsistencies;
    distinguish direct bacterial growth inhibition from nonbacteriostatic pneumolysin
    effects, host pharmacology and indirect membrane/protein-synthesis phenotypes.
  target_ids:
  - CHEBI:132853
  field_paths:
  - evidence
  - activity_spectrum
  - molecular_targets
  - mode_of_action
  - discussions
  evidence_ids:
  - adopted-bacterial
  - adopted-antivirulence
  - antileishmania
  - 2022-activity
  - 2022-mechanism
  - adapter
  - rubric
  rule_id: 'native-review-checklist: Evidence/Mode/Targets/Activity'
  native_severity: informational optional enrichment
  normalization_reason: These fields are optional; missing claim objects in a SEEDED
    record are not a required-representation failure.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/acteoside.yaml
    role: Curator-added evidence, activity, targets and discussions through the validated
      writer and history
actions:
- action_id: A1
  description: Adjudicate the KNApSAcK equivalence in the maintained source path while
    preserving supported native chemistry.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:132853
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
  acceptance_checks:
  - Reinspect all C00002783 structural representations and compare independently parsed
    full stereochemical structures against CHEBI:132853.
  - Resolve through upstream correction or documented source/extractor qualification
    or exclusion of this exact-equivalence xref; a label match alone is insufficient.
    Do not mutate raw snapshots ad hoc or change native chemistry to match an external
    error.
  - Reseed through the native workflow, then schema/strict,chemistry,source reproduction
    and required shared gates.
- action_id: A2
  description: Optionally curate original assay and mechanistic observations on the
    actual native record.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:132853
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/acteoside.yaml
    role: Curator-added evidence, activity, targets and discussions through the validated
      writer and history
  acceptance_checks:
  - Preserve exact material,CAS,organism/strain,medium,inoculum,time,units and measured
    endpoint; do not infer clinical resistance from unusually high experimental MICs
    without applicable breakpoints.
  - For2022 use Table2 PA69 FICI0.281 with the conflicting narrative recorded; document
    differing inoculum descriptions and incomplete biofilm methods.
  - Separate pneumolysin anti-virulence from growth inhibition, Leishmania arginase
    from host immune effects, and precursor incorporation or dye/ATP responses from
    direct binding/channel evidence. Obtain full older primary methods before detailed
    mechanism coding.
  - Do not extrapolate cytotoxicity at≤200µM to safety at bacterial MICs or plant
    occurrence to biosynthetic producer proof.
  - Use write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/acteoside.yaml;
    retain SEEDED until native scientific review requirements are independently fulfilled;
    rerun focused and shared gates.
limitations:
- All 13 initially captured maintained hashes remain unchanged. Actual shared gates
  are recorded in this review; full QC and chemical-map completion are limited by
  the pinned SciPy binary.
- All ten adopted original abstracts were inspected; most full papers were not. The1999
  antibacterial and2016 pneumolysin publisher full text were inaccessible. Additional
  antileishmanial studies remain abstract-only after bounded official routes; UniPisa
  explicitly has no full-text file.
- The2022 original main text,methods and structured tables were read completely. No
  raw datasets or supplemental biofilm protocol were reanalysed; reported method and
  narrative inconsistencies are preserved.
- HMDB page/XML returned403; Reaxys and CAS registry were not directly inspected.
  Their identifiers are corroborated through adopted/current ChEBI and accessible
  other official entries; no claim that every xref is independently verified.
- Current KNApSAcK external structure conflict does not refute native structure or
  measured activity. Direct origin of the upstream inconsistency is unresolved.
- Adapter searches used previously inspected successful dataset inventory; zero hits
  do not establish gene absence or no mechanism. No matching Leishmania dataset was
  available in that inventory.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
