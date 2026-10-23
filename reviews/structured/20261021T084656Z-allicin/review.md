# Allicin: supported native chemistry and activities with a KNApSAcK stereochemical conflict

- Review: 20261021T084656Z-allicin
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:35:00Z
- Finished UTC: 2026-10-21T08:46:56Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Native neutral, sulfur-stereounspecified allicin agrees with ChEBI, PubChem and KEGG; original experiments support both antibacterial and antifungal roles. The linked KNApSAcK entry contains conflicting specified versus unspecified sulfur stereochemistry, a major external-equivalence finding. An informational follow-up covers qualified activity, thiol chemistry, response-versus-target scope and datasets.

## Scope And Provenance

Entire native record and adopted ChEBI row, chemical identifier verification, full2016 bacterial thiol-stress and2022 Cryptococcus primary studies, bounded Candida abstract, iModulonDB context and PRIDE/GSA metadata.

Selection: Queue086, exact CHEBI:28411 at the locked path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:28411 | data/antibiotics/antibacterial/allicin.yaml | generated | allicin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:28411 | Focused LinkML validation exited0. |
| strict | passed | True | CHEBI:28411 | Focused strict scan has zero ERROR rows. |
| chemistry | passed | False | CHEBI:28411 | Native structure, formula,charge,masses and source mint agree. |
| external-chemistry | passed | False | CHEBI:28411 | Comparison executed successfully and detected a conflicting external InChI. Success is not an all-xrefs-match assertion. |
| adapter-rpoh | passed | False | CHEBI:28411 | Exact query completed; interpreted only relevant exact gene/module context. |
| adapter-oxyr | passed | False | CHEBI:28411 | Exact query completed; interpreted only relevant exact gene/module context. |
| adapter-acea | passed | False | CHEBI:28411 | Exact query completed; interpreted only relevant exact gene/module context. |
| adapter-summary-37 | passed | False | CHEBI:28411 | Relevant returned component summary inspected. |
| adapter-summary-26 | passed | False | CHEBI:28411 | Relevant returned component summary inspected. |
| initial-fetch-helper | failed | False | CHEBI:28411 | Initial scratch fetch helper failed before requests because the source citation list is empty. Corrected to a discovery query; subsequent official identity fetches succeeded. This was not a native validator failure. |
| Authoritative full QC | failed | True | CHEBI:28411 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:28411 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:28411 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:28411 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:28411 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:28411 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:28411 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:28411 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:28411 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Native exact structure

identity: supported. Targets: CHEBI:28411.

Official ChEBI,PubChem and KEGG chemistry agree on stereounspecified neutral allicin; no native racemate claim.

### KNApSAcK stereochemical equivalence

identity: concern. Targets: CHEBI:28411.

Linked external page mixes specified sulfur InChI and unspecified SMILES. Native identity is supported independently.

### Antibacterial and antifungal roles

evidence: supported. Targets: CHEBI:28411.

Original synthetic-compound growth assays directly support both roles; additional fungal work retains reaction-mixture and endpoint qualifications.

### Thiol chemistry and stress-response enrichment

completeness: unknown. Targets: CHEBI:28411.

Original data support several measured effects; no sole protein target or allosteric causal chain is automatically established. Optional mechanism/evidence remains uncurated.

### Proteomics versus fungal transcriptomics

completeness: unknown. Targets: CHEBI:28411.

Public PRIDE records are relevant. GSA-Human record matches study but raw data are controlled; preserve protocol/access discrepancies and no raw reanalysis.

### Definition,producer,resistance,clinical and graph fields

completeness: unknown. Targets: CHEBI:28411.

No false optional assertions present. Source definition/citations are empty. Plant occurrence and a laboratory alliinase reaction alone do not establish a curated taxon/strain producer; no clinical approval or resistance mechanism inferred.

### Maintained ownership and provenance

ownership: supported. Targets: CHEBI:28411.

Source/extractor/seeder own external identity follow-up; actual native record owns optional curated additions. All13 initial hashes unchanged.

### Focused native gates

schema: supported. Targets: CHEBI:28411.

Documented focused schema/strict and independent chemistry pass despite scientific external-link conflict.

## Findings

### F1: KNApSAcK link contains conflicting sulfur stereochemistry

major / open / confirmed; issue key: allicin-knapsack-c00001242-sulfur-stereochemistry-conflict.

C00001242 has a matching stereounspecified SMILES but a specified sulfur InChI with a different calculated full key; its displayed key also disagrees with the InChI. Preserve supported native stereounspecified allicin and adjudicate external equivalence instead of treating the name match as sufficient. This is not proof that native allicin is the wrong compound or inactive.

### F2: Curate exact-material activity, measured thiol effects and qualified dataset context

informational / open / confirmed; issue key: allicin-qualified-thiol-activity-dataset-enrichment.

Primary studies and public proteomics offer concrete optional enrichment. Separate native stereounspecified structure from any stereoisomer,synthetic allicin from generated reaction material, microbial phenotypes from target causation, and stress-response expression from direct chemical modification. Preserve controlled-access RNA-seq and protocol discrepancies.

## Recommended Actions And Acceptance Checks

### A1

Resolve the external KNApSAcK equivalence through maintained source ownership.

- Reinspect C00001242 and independently parse all structures, retaining specified-versus-unspecified sulfur and full-key comparisons.
- Use upstream correction or a documented source/extractor qualification/exclusion of the exact-equivalence link if it remains conflicting. Do not silently replace supported native structure or hand-edit raw snapshots.
- Reseed through native writer/history and run focused schema/strict,chemistry,source reproduction and required shared gates.

### A2

Optionally curate activity, measured mechanism and accessible datasets on the actual native record.

- Attach narrow original evidence with exact supplied material,purity/conversion,organism/strain,medium,inoculum,time,units and endpoint; do not convert MIC to killing or clinical resistance.
- Distinguish2016 cysteine-adduct mass spectrometry and lysate enzyme activity from inferred allostery, general ROS production or a sole lethal target. RpoH/OxyR-associated response and iModulon membership are not direct inhibition evidence.
- Preserve bacterial versus fungal models and exact strains;2022 membrane/transcriptomic effects do not identify a specific fungal protein target or establish clinical efficacy.
- Link public PXD003158/PXD003063 with their distinct experimental scopes and note source-protocol conflict. Do not label HRA003391 raw data openly public; retain it in a qualified discussion until native public-dataset criteria can be satisfied.
- Use write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/allicin.yaml; no status promotion from this review alone; focused and required shared gates must pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/allicin.yaml; Entire native YAML after086 capture. | supports | SEEDED/EXACT allicin, neutral C6H10OS2 with unspecified sulfur configuration; four exact synonyms, parents22063/86494, antibacterial33282 and antifungal35718 roles, four chemical xrefs, one CHEBI source and three seed/reseed events. Definition,claim evidence,mechanism,targets,activity,resistance,producer,clinical,datasets and graphs are unpopulated. |
| source | data/raw/chebi_antimicrobials.tsv; Exact source line539 in086-raw.json; extractor176–339,seeder1483–1669,source config/manifest and role map. | supports | Source has no definition, citations or mechanism roles; native omissions reproduce that source and are not dropped evidence. Structural synonyms,parents,roles and xrefs reproduce the row. Antibacterial filing preserves the antifungal role. CHEBI mint278ab7efc8 and all13 initial hashes agree. No target-specific override/overlay/prior review found in ignored-inclusive search. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:28411; Complete086-chebi.html/txt,086-pubchem.json and086-kegg.txt/MOL. | supports | ChEBI confirms native identity, synonyms, sulfoxide22063 and botanical anti-fungal agent86494 parents; antifungal role is inherited through the parent. Current PubChem CID65036 and KEGG C07600 MOL match full key JDLKFOPOAOFWQN-UHFFFAOYSA-N. CAS539-86-6 is corroborated by accessible entries,not the registry directly. Beilstein1752823 is source-corroborated but not independently inspected. No configuration or racemate is inferred from unspecified sulfur. |
| chemistry | Independent RDKit calculation; 086-chemistry.json/log and086-xref-chemistry.json. | supports | Native SMILES/InChI each yield one neutral C6H10OS2 fragment, matching full key, average mass162.279 and exact mass162.01730694. The sulfur stereocentre is unspecified. Source-specific mint matches; KEGG MOL independently yields the same full key. |
| xref-conflict | http://www.knapsackfamily.com/knapsack_core/information.php?word=C00001242; Complete086-knapsack.html/txt; independently parsed086-xref-chemistry.json. | refutes | The page names allicin with matching CAS/formula and stereounspecified SMILES, but its InChI contains /t9-/m0/s1 and parses to JDLKFOPOAOFWQN-VIFPVBQESA-N, a specified sulfur configuration. The displayed key is JDLKFOPOAOFWQN-UHFFFAOYNA-N and does not agree with that InChI. Conflicting external representations prevent unqualified exact-stereochemical verification; native ChEBI chemistry remains independently supported. |
| 2016-activity | DOI:10.1074/jbc.M115.702308; PMID27008862,PMC4882420; full086-2016.xml main body; Figure2 visually checked086-2016-fig2.jpg. | supports | Synthesized allicin was95% by HPLC. Figure2A shows MICs64µg/mL for S.aureus DSM20231/ATCC43300 and E.coli DSM30083;32 for A.baumannii DSM30007/C.albicans DSM1386;512 for P.aeruginosa DSM50071. Methods retain organism-specific media and16–18h exposure; MG1655 MOPS assay is separate,Figure2B labeled23±2µg/mL. These support both roles without generalizing a species-wide potency. |
| 2016-mechanism | DOI:10.1074/jbc.M115.702308; Full Experimental Procedures,Results and Discussion,Tables1–2,Figures3–11. | context_only | At0.79mM in E.coli, experiments support thiol depletion, protein cysteine S-allylmercapto adducts,aggregation and RpoH stabilization/recovery. AceA Cys244 adduct identification and reduced lysate activity are associated; no isolated Cys244 mutant proves sole causation. Protein-expression response is proteomics,not RNA-seq or direct binding. GSH loss does not entail increased GSSG, and PhoA assay differs from diamide disulfide stress. RpoH is a protective response,not an inhibited target. |
| 2022-activity | DOI:10.3389/fmicb.2022.1012516; PMID36466672,PMC9709445; complete086-2022.xml main body,Table1; Figure1 visually checked086-2022-fig1.jpg. | supports | Alliin/alliinase-generated material had reported97.5% conversion,not established97.5% isolated-compound purity. Table1 gives allicin100%-growth-inhibition MIC2µg/mL for C.neoformans H99 and1–8 for46 clinical isolates. Assay uses RPMI,35°C,72h. Two AmB values exceed an ECV; this does not establish clinical resistance. H99 combination results cannot generalize to all clinical isolates. |
| 2022-mechanism | DOI:10.3389/fmicb.2022.1012516; Complete Methods/Results/Discussion; RNA-seq, TEM and permeability-dye experiments. | context_only | Expression enrichment and membrane injury support response/phenotype hypotheses,not specific protein binding; authors explicitly leave targets unverified. Preserve reaction-product context and method inconsistencies: incorrect QC species in one subsection, corrected later; comparator MICs differ between Tables1/2; colony-recovery timing differs from Figure2 caption. Mouse effects do not establish clinical efficacy. |
| candida | PMID:19924565; Complete abstract in086-primary-epmc.json; DOI10.1007/s11046-009-9251-3 verified. | context_only | Original allicin study reports activity across six Candida species and isolate-dependent azole combinations; synergy was not found in most species tested. Abstract-only context corroborates the broad antifungal role but does not supply fully verified material/methods for numeric entries. |
| adapter | iModulonDB e_coli/precise_mg1655; Same-session055 successful inventory;086-imodulondb-rpoh/oxyr/acea.txt and summary37/26.txt. | context_only | Exact genes b3461/rpoH,b3961/oxyR,b4015/aceA resolve. Component37 RpoH contains18 heat-shock/chaperone genes;component26 SoxS contains17 genes including grxA/ahpC/ahpF. These match bounded response vocabulary,not measured allicin activity in this database or direct target proof. Query oxyR also returns Nucleoside33 through substring matching; discarded as irrelevant. AceA has zero module hits. No Cryptococcus dataset in inspected inventory. |
| proteomics | https://www.ebi.ac.uk/pride/archive/projects/PXD003063; Official086-PXD003063.json and086-PXD003158.json complete metadata. | context_only | Both publicly resolve and cite PMID27008862. PXD003158 is gel-based response-protein identification; PXD003063 is label-free/OxICAT modification analysis after allicin exposure. Both describe E.coli with the original study protocols. Public metadata links are relevant enrichment,not independent replication. PXD003063 metadata says PEP above0.01 while the article says below0.01; raw files were not reanalysed to reconcile that protocol-text conflict. |
| fungal-dataset | https://ngdc.cncb.ac.cn/gsa-human/browse/HRA003391; Complete086-gsa.html/txt official landing page. | context_only | HRA003391 links PRJCA012538 and exactly names the2022 fungal study; study type Clinical pathogen explains its GSA-Human placement. Current metadata says Controlled access,release2024-11-07. The paper calls it publicly accessible; public metadata does not imply open access to raw sequence files. No data request was submitted. |
| search | CultureBotAI/AntibioticMech; 086-local-hits.txt/maintained-search.txt and bounded official/primary queries. | context_only | Ignored-inclusive searches found only source/queue occurrences for the exact target and no target-specific curated additions/decisions/prior review in searched paths. There are zero adopted publication leads.086-epmc.json is a broad discovery result,not a read bibliography; only the three sources in086-primary-epmc.json were used for primary assessment. Initial fetch helper failed on empty citations and was corrected before successful requests. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity/equivalence,activity,target,producer,datasets and audit;CLAUDE,HARMONIZATION,CURATION. | supports | Exact chemical links preserve configuration; optional evidence/definition/mechanism fields are not mandatory. Response modules are not target proof. Public dataset requirements cannot be satisfied by controlled raw data merely because its landing page is public. Curator-owned additions use the actual record path and validated history. |
| validation | Focused documented native gates; 086-focused-results.json/schema.log/strict.log/strict.tsv and086-chemistry.json. | supports | Schema/strict and native chemistry/mint pass. |

## Limits And Additional Notes

- The source has zero adopted citations. Full2016 and2022 main texts/methods/results/tables were inspected;2016 Figure2 and2022 Figure1 visually checked. Supplementary tables/raw omics were not comprehensively reanalysed;2009 Candida evidence is abstract-only.
- KNApSAcK conflicting external stereochemistry does not change supported native identity. CAS registry and legacy Beilstein entry were not directly inspected; accessible official sources corroborate accessions.
- GSA-Human study metadata are public but raw sequence access is controlled. PRIDE protocol text conflicts with the published PEP threshold. Neither is silently resolved, and no access request/raw-data acquisition occurred.
- Broad discovery query results are leads only and were not all reviewed. Initial helper failure on an empty citation field was corrected; focused native validators passed independently.
- iModulonDB context comes from the inspected same-session inventory and actual gene/module requests; it does not independently prove drug response or target binding. No applicable Cryptococcus inventory entry was available.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T084656Z-allicin
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Allicin: supported native chemistry and activities with a KNApSAcK stereochemical
  conflict'
started_at: '2026-10-21T08:35:00Z'
finished_at: '2026-10-21T08:46:56Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author record. Captured maintained hashes before assessment,
    read entire record/source and transforms, official identities, full original bacterial
    and fungal articles, structured stress-response context and official dataset metadata.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Native neutral, sulfur-stereounspecified allicin agrees with ChEBI, PubChem
  and KEGG; original experiments support both antibacterial and antifungal roles.
  The linked KNApSAcK entry contains conflicting specified versus unspecified sulfur
  stereochemistry, a major external-equivalence finding. An informational follow-up
  covers qualified activity, thiol chemistry, response-versus-target scope and datasets.
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
  - path: data/antibiotics/antibacterial/allicin.yaml
    sha256: 38b6ad70e3fd238938af4ecb2d8b8907be17ead58c208248eebe716c28abd2e9
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
- target_id: CHEBI:28411
  path: data/antibiotics/antibacterial/allicin.yaml
  label: allicin
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
  description: Entire native record and adopted ChEBI row, chemical identifier verification,
    full2016 bacterial thiol-stress and2022 Cryptococcus primary studies, bounded
    Candida abstract, iModulonDB context and PRIDE/GSA metadata.
  selection: Queue086, exact CHEBI:28411 at the locked path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:28411
  exclusions:
  - target: Alliin, ajoene, diallyl disulfide, garlic extracts and individual sulfur
      stereoisomers
    reason: Related precursors, products, mixtures and specified stereoisomers are
      not exact equivalences to the native stereounspecified structure.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Focused LinkML validation exited0.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/allicin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Focused strict scan has zero ERROR rows.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/allicin.yaml --out /private/tmp/am-review-session/086-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Native structure, formula,charge,masses and source mint agree.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache .venv/bin/python
    /private/tmp/am-review-session/086-chemistry-check.py 86
  exit_code: 0
  expected_exit_code: 0
- check_id: external-chemistry
  name: external-chemistry
  status: passed
  required: false
  summary: Comparison executed successfully and detected a conflicting external InChI.
    Success is not an all-xrefs-match assertion.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - xref-conflict
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache .venv/bin/python
    /private/tmp/am-review-session/086-xref-chem.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-rpoh
  name: adapter-rpoh
  status: passed
  required: false
  summary: Exact query completed; interpreted only relevant exact gene/module context.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 search --organism e_coli --dataset
    precise_mg1655 --query rpoH
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-oxyr
  name: adapter-oxyr
  status: passed
  required: false
  summary: Exact query completed; interpreted only relevant exact gene/module context.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 search --organism e_coli --dataset
    precise_mg1655 --query oxyR
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-acea
  name: adapter-acea
  status: passed
  required: false
  summary: Exact query completed; interpreted only relevant exact gene/module context.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 search --organism e_coli --dataset
    precise_mg1655 --query aceA
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-summary-37
  name: adapter-summary-37
  status: passed
  required: false
  summary: Relevant returned component summary inspected.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 summarize --organism e_coli --dataset
    precise_mg1655 --k 37
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-summary-26
  name: adapter-summary-26
  status: passed
  required: false
  summary: Relevant returned component summary inspected.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 summarize --organism e_coli --dataset
    precise_mg1655 --k 26
  exit_code: 0
  expected_exit_code: 0
- check_id: initial-fetch-helper
  name: initial-fetch-helper
  status: failed
  required: false
  summary: Initial scratch fetch helper failed before requests because the source
    citation list is empty. Corrected to a discovery query; subsequent official identity
    fetches succeeded. This was not a native validator failure.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - search
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache .venv/bin/python
    /private/tmp/am-review-session/086-fetch.py
  exit_code: 1
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
  - CHEBI:28411
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
  - CHEBI:28411
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
  - CHEBI:28411
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
  - CHEBI:28411
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
  - CHEBI:28411
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
  - CHEBI:28411
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
  - CHEBI:28411
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
  - CHEBI:28411
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
  - CHEBI:28411
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/allicin.yaml
  locator: Entire native YAML after086 capture.
  accessed_at: '2026-10-21T08:40:19Z'
  support: supports
  summary: SEEDED/EXACT allicin, neutral C6H10OS2 with unspecified sulfur configuration;
    four exact synonyms, parents22063/86494, antibacterial33282 and antifungal35718
    roles, four chemical xrefs, one CHEBI source and three seed/reseed events. Definition,claim
    evidence,mechanism,targets,activity,resistance,producer,clinical,datasets and
    graphs are unpopulated.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Exact source line539 in086-raw.json; extractor176–339,seeder1483–1669,source
    config/manifest and role map.
  accessed_at: '2026-10-21T08:40:19Z'
  support: supports
  summary: Source has no definition, citations or mechanism roles; native omissions
    reproduce that source and are not dropped evidence. Structural synonyms,parents,roles
    and xrefs reproduce the row. Antibacterial filing preserves the antifungal role.
    CHEBI mint278ab7efc8 and all13 initial hashes agree. No target-specific override/overlay/prior
    review found in ignored-inclusive search.
  snapshot_sha256: e1720325eeb2e0d749ad871bbc348d4b08a1f1f73abd60b397b08d0c602c5c3c
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:28411
  locator: Complete086-chebi.html/txt,086-pubchem.json and086-kegg.txt/MOL.
  accessed_at: '2026-10-21T08:40:19Z'
  support: supports
  summary: ChEBI confirms native identity, synonyms, sulfoxide22063 and botanical
    anti-fungal agent86494 parents; antifungal role is inherited through the parent.
    Current PubChem CID65036 and KEGG C07600 MOL match full key JDLKFOPOAOFWQN-UHFFFAOYSA-N.
    CAS539-86-6 is corroborated by accessible entries,not the registry directly. Beilstein1752823
    is source-corroborated but not independently inspected. No configuration or racemate
    is inferred from unspecified sulfur.
  snapshot_sha256: ddab63692d4b778a5086fd4dfc362a0431aca7c5b712620c17db5911a02d7892
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculation
  locator: 086-chemistry.json/log and086-xref-chemistry.json.
  accessed_at: '2026-10-21T08:40:19Z'
  support: supports
  summary: Native SMILES/InChI each yield one neutral C6H10OS2 fragment, matching
    full key, average mass162.279 and exact mass162.01730694. The sulfur stereocentre
    is unspecified. Source-specific mint matches; KEGG MOL independently yields the
    same full key.
  snapshot_sha256: f4a63767e2635a7139720edef4e8988f29317f1de1f5a4ecb688970639d3f69d
- evidence_id: xref-conflict
  kind: database
  reference: http://www.knapsackfamily.com/knapsack_core/information.php?word=C00001242
  locator: Complete086-knapsack.html/txt; independently parsed086-xref-chemistry.json.
  accessed_at: '2026-10-21T08:40:19Z'
  support: refutes
  summary: The page names allicin with matching CAS/formula and stereounspecified
    SMILES, but its InChI contains /t9-/m0/s1 and parses to JDLKFOPOAOFWQN-VIFPVBQESA-N,
    a specified sulfur configuration. The displayed key is JDLKFOPOAOFWQN-UHFFFAOYNA-N
    and does not agree with that InChI. Conflicting external representations prevent
    unqualified exact-stereochemical verification; native ChEBI chemistry remains
    independently supported.
  snapshot_sha256: faece9d8f39ce6ed423509ec2d6a125ca3737eecc59a066904cd895466bdd69e
- evidence_id: 2016-activity
  kind: primary_source
  reference: DOI:10.1074/jbc.M115.702308
  locator: PMID27008862,PMC4882420; full086-2016.xml main body; Figure2 visually checked086-2016-fig2.jpg.
  accessed_at: '2026-10-21T08:40:19Z'
  support: supports
  summary: Synthesized allicin was95% by HPLC. Figure2A shows MICs64µg/mL for S.aureus
    DSM20231/ATCC43300 and E.coli DSM30083;32 for A.baumannii DSM30007/C.albicans
    DSM1386;512 for P.aeruginosa DSM50071. Methods retain organism-specific media
    and16–18h exposure; MG1655 MOPS assay is separate,Figure2B labeled23±2µg/mL. These
    support both roles without generalizing a species-wide potency.
  snapshot_sha256: 9e1bf7547ae5a07989578ba5745d9879414e0aacc48f5b5772af2c82f8ebac80
- evidence_id: 2016-mechanism
  kind: primary_source
  reference: DOI:10.1074/jbc.M115.702308
  locator: Full Experimental Procedures,Results and Discussion,Tables1–2,Figures3–11.
  accessed_at: '2026-10-21T08:40:19Z'
  support: context_only
  summary: At0.79mM in E.coli, experiments support thiol depletion, protein cysteine
    S-allylmercapto adducts,aggregation and RpoH stabilization/recovery. AceA Cys244
    adduct identification and reduced lysate activity are associated; no isolated
    Cys244 mutant proves sole causation. Protein-expression response is proteomics,not
    RNA-seq or direct binding. GSH loss does not entail increased GSSG, and PhoA assay
    differs from diamide disulfide stress. RpoH is a protective response,not an inhibited
    target.
  snapshot_sha256: 9e1bf7547ae5a07989578ba5745d9879414e0aacc48f5b5772af2c82f8ebac80
- evidence_id: 2022-activity
  kind: primary_source
  reference: DOI:10.3389/fmicb.2022.1012516
  locator: PMID36466672,PMC9709445; complete086-2022.xml main body,Table1; Figure1
    visually checked086-2022-fig1.jpg.
  accessed_at: '2026-10-21T08:40:19Z'
  support: supports
  summary: Alliin/alliinase-generated material had reported97.5% conversion,not established97.5%
    isolated-compound purity. Table1 gives allicin100%-growth-inhibition MIC2µg/mL
    for C.neoformans H99 and1–8 for46 clinical isolates. Assay uses RPMI,35°C,72h.
    Two AmB values exceed an ECV; this does not establish clinical resistance. H99
    combination results cannot generalize to all clinical isolates.
  snapshot_sha256: ba5471cdb3b6217f1f009c19a022c359dff5a1393ef9187436606805115f59a4
- evidence_id: 2022-mechanism
  kind: primary_source
  reference: DOI:10.3389/fmicb.2022.1012516
  locator: Complete Methods/Results/Discussion; RNA-seq, TEM and permeability-dye
    experiments.
  accessed_at: '2026-10-21T08:40:19Z'
  support: context_only
  summary: 'Expression enrichment and membrane injury support response/phenotype hypotheses,not
    specific protein binding; authors explicitly leave targets unverified. Preserve
    reaction-product context and method inconsistencies: incorrect QC species in one
    subsection, corrected later; comparator MICs differ between Tables1/2; colony-recovery
    timing differs from Figure2 caption. Mouse effects do not establish clinical efficacy.'
  snapshot_sha256: ba5471cdb3b6217f1f009c19a022c359dff5a1393ef9187436606805115f59a4
- evidence_id: candida
  kind: primary_source
  reference: PMID:19924565
  locator: Complete abstract in086-primary-epmc.json; DOI10.1007/s11046-009-9251-3
    verified.
  accessed_at: '2026-10-21T08:40:19Z'
  support: context_only
  summary: Original allicin study reports activity across six Candida species and
    isolate-dependent azole combinations; synergy was not found in most species tested.
    Abstract-only context corroborates the broad antifungal role but does not supply
    fully verified material/methods for numeric entries.
  snapshot_sha256: 2ce61dbfe18c1ca641f4fc89a642ee3abd472404bb0b5d6cc1b828d4efc4124f
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/precise_mg1655
  locator: Same-session055 successful inventory;086-imodulondb-rpoh/oxyr/acea.txt
    and summary37/26.txt.
  accessed_at: '2026-10-21T08:40:19Z'
  support: context_only
  summary: Exact genes b3461/rpoH,b3961/oxyR,b4015/aceA resolve. Component37 RpoH
    contains18 heat-shock/chaperone genes;component26 SoxS contains17 genes including
    grxA/ahpC/ahpF. These match bounded response vocabulary,not measured allicin activity
    in this database or direct target proof. Query oxyR also returns Nucleoside33
    through substring matching; discarded as irrelevant. AceA has zero module hits.
    No Cryptococcus dataset in inspected inventory.
  snapshot_sha256: 40b50072421ea69f34fcfd2223d7e695c6985024ec9be763663394f0db3d3dc5
- evidence_id: proteomics
  kind: database
  reference: https://www.ebi.ac.uk/pride/archive/projects/PXD003063
  locator: Official086-PXD003063.json and086-PXD003158.json complete metadata.
  accessed_at: '2026-10-21T08:40:19Z'
  support: context_only
  summary: Both publicly resolve and cite PMID27008862. PXD003158 is gel-based response-protein
    identification; PXD003063 is label-free/OxICAT modification analysis after allicin
    exposure. Both describe E.coli with the original study protocols. Public metadata
    links are relevant enrichment,not independent replication. PXD003063 metadata
    says PEP above0.01 while the article says below0.01; raw files were not reanalysed
    to reconcile that protocol-text conflict.
  snapshot_sha256: 3010531e93f690ff96036514080debdf59eb4375ce58658372a58c02a538c046
- evidence_id: fungal-dataset
  kind: database
  reference: https://ngdc.cncb.ac.cn/gsa-human/browse/HRA003391
  locator: Complete086-gsa.html/txt official landing page.
  accessed_at: '2026-10-21T08:40:19Z'
  support: context_only
  summary: HRA003391 links PRJCA012538 and exactly names the2022 fungal study; study
    type Clinical pathogen explains its GSA-Human placement. Current metadata says
    Controlled access,release2024-11-07. The paper calls it publicly accessible; public
    metadata does not imply open access to raw sequence files. No data request was
    submitted.
  snapshot_sha256: 3d4de03e2adc05b380b4ea2a8d8b775d3cacfb4bcb4ea7d4c890b73e32c75348
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 086-local-hits.txt/maintained-search.txt and bounded official/primary queries.
  accessed_at: '2026-10-21T08:40:19Z'
  support: context_only
  summary: Ignored-inclusive searches found only source/queue occurrences for the
    exact target and no target-specific curated additions/decisions/prior review in
    searched paths. There are zero adopted publication leads.086-epmc.json is a broad
    discovery result,not a read bibliography; only the three sources in086-primary-epmc.json
    were used for primary assessment. Initial fetch helper failed on empty citations
    and was corrected before successful requests.
  search_scope: rg --no-ignore --hidden across batch009 excluding.git/.venv for allicin,28411,JDLKFOPOAOFWQN,278ab7efc8,plus
    maintained curation/conf/scripts/data/raw/reports/reviews. Public ChEBI,PubChem,KEGG,KNApSAcK;
    exact allicin thiol-stress and antifungal searches in PubMed/EuropePMC/JBC/Frontiers;
    structured iModulonDB,PRIDE,GSA metadata. Reviews/search snippets only discovery
    leads. No claim of exhaustive literature absence.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity/equivalence,activity,target,producer,datasets and audit;CLAUDE,HARMONIZATION,CURATION.
  accessed_at: '2026-10-21T08:40:19Z'
  support: supports
  summary: Exact chemical links preserve configuration; optional evidence/definition/mechanism
    fields are not mandatory. Response modules are not target proof. Public dataset
    requirements cannot be satisfied by controlled raw data merely because its landing
    page is public. Curator-owned additions use the actual record path and validated
    history.
- evidence_id: validation
  kind: validation
  reference: Focused documented native gates
  locator: 086-focused-results.json/schema.log/strict.log/strict.tsv and086-chemistry.json.
  accessed_at: '2026-10-21T08:40:19Z'
  support: supports
  summary: Schema/strict and native chemistry/mint pass.
  snapshot_sha256: f0a1cdd0420b8cce74ea65f1643e559000befaade2cdfd365a2e73f22145619d
assessments:
- assessment_id: identity
  area: identity
  topic: Native exact structure
  outcome: supported
  summary: Official ChEBI,PubChem and KEGG chemistry agree on stereounspecified neutral
    allicin; no native racemate claim.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - identity
  - chemistry
  - source
- assessment_id: xref
  area: identity
  topic: KNApSAcK stereochemical equivalence
  outcome: concern
  summary: Linked external page mixes specified sulfur InChI and unspecified SMILES.
    Native identity is supported independently.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - xref-conflict
  - identity
  - rubric
- assessment_id: roles
  area: evidence
  topic: Antibacterial and antifungal roles
  outcome: supported
  summary: Original synthetic-compound growth assays directly support both roles;
    additional fungal work retains reaction-mixture and endpoint qualifications.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - 2016-activity
  - 2022-activity
  - candida
  - source
- assessment_id: mechanism
  area: completeness
  topic: Thiol chemistry and stress-response enrichment
  outcome: unknown
  summary: Original data support several measured effects; no sole protein target
    or allosteric causal chain is automatically established. Optional mechanism/evidence
    remains uncurated.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - 2016-mechanism
  - 2022-mechanism
  - adapter
  - rubric
- assessment_id: datasets
  area: completeness
  topic: Proteomics versus fungal transcriptomics
  outcome: unknown
  summary: Public PRIDE records are relevant. GSA-Human record matches study but raw
    data are controlled; preserve protocol/access discrepancies and no raw reanalysis.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - proteomics
  - fungal-dataset
- assessment_id: other
  area: completeness
  topic: Definition,producer,resistance,clinical and graph fields
  outcome: unknown
  summary: No false optional assertions present. Source definition/citations are empty.
    Plant occurrence and a laboratory alliinase reaction alone do not establish a
    curated taxon/strain producer; no clinical approval or resistance mechanism inferred.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - record
  - source
  - 2022-activity
  - rubric
- assessment_id: ownership
  area: ownership
  topic: Maintained ownership and provenance
  outcome: supported
  summary: Source/extractor/seeder own external identity follow-up; actual native
    record owns optional curated additions. All13 initial hashes unchanged.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - source
  - search
- assessment_id: gates
  area: schema
  topic: Focused native gates
  outcome: supported
  summary: Documented focused schema/strict and independent chemistry pass despite
    scientific external-link conflict.
  target_ids:
  - CHEBI:28411
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: allicin-knapsack-c00001242-sulfur-stereochemistry-conflict
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: KNApSAcK link contains conflicting sulfur stereochemistry
  description: C00001242 has a matching stereounspecified SMILES but a specified sulfur
    InChI with a different calculated full key; its displayed key also disagrees with
    the InChI. Preserve supported native stereounspecified allicin and adjudicate
    external equivalence instead of treating the name match as sufficient. This is
    not proof that native allicin is the wrong compound or inactive.
  target_ids:
  - CHEBI:28411
  field_paths:
  - xrefs
  evidence_ids:
  - xref-conflict
  - identity
  - chemistry
  - source
  - rubric
  rule_id: 'native-review-checklist: Identity/Equivalence; exact-structure xref invariant'
  native_severity: major external exact-stereochemistry conflict
  normalization_reason: External exact equivalence is not established because its
    structures conflict. The independently supported native compound remains correctly
    identified, so blocker severity is unwarranted.
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
  issue_key: allicin-qualified-thiol-activity-dataset-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Curate exact-material activity, measured thiol effects and qualified dataset
    context
  description: Primary studies and public proteomics offer concrete optional enrichment.
    Separate native stereounspecified structure from any stereoisomer,synthetic allicin
    from generated reaction material, microbial phenotypes from target causation,
    and stress-response expression from direct chemical modification. Preserve controlled-access
    RNA-seq and protocol discrepancies.
  target_ids:
  - CHEBI:28411
  field_paths:
  - evidence
  - activity_spectrum
  - mode_of_action
  - molecular_targets
  - datasets
  - discussions
  evidence_ids:
  - 2016-activity
  - 2016-mechanism
  - 2022-activity
  - 2022-mechanism
  - adapter
  - proteomics
  - fungal-dataset
  - rubric
  rule_id: 'native-review-checklist: Evidence/Activity/Mode/Targets/Datasets'
  native_severity: informational optional enrichment
  normalization_reason: No missing required representation is alleged; current SEEDED
    record makes none of the extrapolated mechanism/dataset claims.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/allicin.yaml
    role: Curator-added evidence, activity, mechanism, discussions and dataset links
      through validated writer/history
actions:
- action_id: A1
  description: Resolve the external KNApSAcK equivalence through maintained source
    ownership.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:28411
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
  - Reinspect C00001242 and independently parse all structures, retaining specified-versus-unspecified
    sulfur and full-key comparisons.
  - Use upstream correction or a documented source/extractor qualification/exclusion
    of the exact-equivalence link if it remains conflicting. Do not silently replace
    supported native structure or hand-edit raw snapshots.
  - Reseed through native writer/history and run focused schema/strict,chemistry,source
    reproduction and required shared gates.
- action_id: A2
  description: Optionally curate activity, measured mechanism and accessible datasets
    on the actual native record.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:28411
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/allicin.yaml
    role: Curator-added evidence, activity, mechanism, discussions and dataset links
      through validated writer/history
  acceptance_checks:
  - Attach narrow original evidence with exact supplied material,purity/conversion,organism/strain,medium,inoculum,time,units
    and endpoint; do not convert MIC to killing or clinical resistance.
  - Distinguish2016 cysteine-adduct mass spectrometry and lysate enzyme activity from
    inferred allostery, general ROS production or a sole lethal target. RpoH/OxyR-associated
    response and iModulon membership are not direct inhibition evidence.
  - Preserve bacterial versus fungal models and exact strains;2022 membrane/transcriptomic
    effects do not identify a specific fungal protein target or establish clinical
    efficacy.
  - Link public PXD003158/PXD003063 with their distinct experimental scopes and note
    source-protocol conflict. Do not label HRA003391 raw data openly public; retain
    it in a qualified discussion until native public-dataset criteria can be satisfied.
  - Use write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/allicin.yaml;
    no status promotion from this review alone; focused and required shared gates
    must pass.
limitations:
- The source has zero adopted citations. Full2016 and2022 main texts/methods/results/tables
  were inspected;2016 Figure2 and2022 Figure1 visually checked. Supplementary tables/raw
  omics were not comprehensively reanalysed;2009 Candida evidence is abstract-only.
- KNApSAcK conflicting external stereochemistry does not change supported native identity.
  CAS registry and legacy Beilstein entry were not directly inspected; accessible
  official sources corroborate accessions.
- GSA-Human study metadata are public but raw sequence access is controlled. PRIDE
  protocol text conflicts with the published PEP threshold. Neither is silently resolved,
  and no access request/raw-data acquisition occurred.
- Broad discovery query results are leads only and were not all reviewed. Initial
  helper failure on an empty citation field was corrected; focused native validators
  passed independently.
- iModulonDB context comes from the inspected same-session inventory and actual gene/module
  requests; it does not independently prove drug response or target binding. No applicable
  Cryptococcus inventory entry was available.
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
