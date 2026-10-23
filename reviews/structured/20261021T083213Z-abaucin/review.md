# Abaucin: supported antibacterial activity with a hydrochloride synonym conflict

- Review: 20261021T083213Z-abaucin
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:21:08Z
- Finished UTC: 2026-10-21T08:32:13Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Neutral abaucin chemistry matches official PubChem and ChEBI and its antibacterial activity is supported. The primary synthesis identifies MLJS-21001 as a hydrochloride, conflicting with its native exact-synonym placement on the neutral freebase. A minor finding concerns paraphrase in a verbatim-snippet slot; an informational follow-up identifies scoped activity, LolDF mechanism and transcriptomics enrichment.

## Scope And Provenance

Whole record, maintained curator source and seeder, sole adopted publication, original supplementary chemistry/assays, official chemical identities, structured LolE context, GEO metadata and selected2026 original mechanism results/methods.

Selection: Queue075, antibioticmech:curator-f8f4ef7fbd at the locked path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:curator-f8f4ef7fbd | data/antibiotics/antibacterial/abaucin.yaml | generated | Abaucin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | antibioticmech:curator-f8f4ef7fbd | Focused LinkML validation exited0. |
| strict | passed | True | antibioticmech:curator-f8f4ef7fbd | Focused strict scan has zero ERROR rows. |
| chemistry | passed | False | antibioticmech:curator-f8f4ef7fbd | Independent native SMILES/InChI chemistry and CURATOR mint agree. |
| adapter-datasets | failed | False | antibioticmech:curator-f8f4ef7fbd | Fresh inventory request failed DNS in sandbox. Previously inspected same-session dataset inventory055 identifies a_baumannii/precise139; used that coverage for successful public query. |
| adapter-lole | passed | False | antibioticmech:curator-f8f4ef7fbd | Public exact LolE query resolves one gene, zero modules. No component summary applies. |
| Authoritative full QC | failed | True | antibioticmech:curator-f8f4ef7fbd | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:curator-f8f4ef7fbd | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:curator-f8f4ef7fbd | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:curator-f8f4ef7fbd | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:curator-f8f4ef7fbd | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:curator-f8f4ef7fbd | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:curator-f8f4ef7fbd | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:curator-f8f4ef7fbd | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:curator-f8f4ef7fbd | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Freebase identity

identity: supported. Targets: antibioticmech:curator-f8f4ef7fbd.

PubChem,ChEBI and native representations agree on the neutral freebase; the structural definition is coherent.

### MLJS-21001 exact synonym

identity: concern. Targets: antibioticmech:curator-f8f4ef7fbd.

Original synthesis explicitly uses this code for the HCl salt, conflicting with unqualified exact synonym on freebase.

### Antibacterial definition and clinical isolate support

evidence: supported. Targets: antibioticmech:curator-f8f4ef7fbd.

The exact parent compound and tested material are explicitly linked by the adopted paper, which supports antibacterial activity and the bounded strain panel. Salt basis must accompany future numeric claims; no evidence of inactivity is inferred.

### Quotation versus interpretation

evidence: concern. Targets: antibioticmech:curator-f8f4ef7fbd.

Source snippet is an author-attributed curator summary, not a short verbatim passage. Its scientific content is supported, but placement violates native evidence rules.

### Target/response boundaries

completeness: unknown. Targets: antibioticmech:curator-f8f4ef7fbd.

Mechanism is a concrete optional enrichment opportunity.2023 indirect evidence and2026 direct biochemical/structural work must be distinguished; exact assay form and species context retained.

### Datasets,producer,clinical and graphs

completeness: unknown. Targets: antibioticmech:curator-f8f4ef7fbd.

GEO offers a relevant optional link. No biosynthetic producer,clinical approval or graph is asserted; none follows automatically from preclinical results or expression responses.

### Minted source rationale and candidate ChEBI

grounding: supported. Targets: antibioticmech:curator-f8f4ef7fbd.

Stable curator DOI-fragment source and exact structure support proposed identity. ChEBI93458 is a matching third-party candidate outside adopted inventory, requiring explicit curated grounding policy; no duplicated adopted target was found.

### Maintained row/status/history

ownership: supported. Targets: antibioticmech:curator-f8f4ef7fbd.

Curator row14 and seeder own the two corrective findings. All13 captured hashes unchanged; no native status/history modified.

### Focused schema/strict/chemistry

schema: supported. Targets: antibioticmech:curator-f8f4ef7fbd.

Documented focused validators and independent chemistry pass despite scientific salt/synonym and snippet findings.

## Findings

### F1: MLJS-21001 denotes the synthesized hydrochloride in the primary source

major / open / confirmed; issue key: abaucin-mljs-21001-hydrochloride-exact-synonym.

The neutral freebase record lists MLJS-21001 as EXACT_SYNONYM. Supplementary Note1 explicitly synthesizes, draws and labels MLJS-21001 compound1 as •HCl. Preserve this salt distinction and do not attach unqualified salt-mass assay values to the freebase. This does not refute abaucin antibacterial activity or the correctness of native freebase structure.

### F2: Move the curator summary out of the verbatim snippet slot

minor / open / confirmed; issue key: abaucin-curator-paraphrase-in-snippet.

The source-concept snippet beginning with author attribution is a paraphrase of discovery/activity findings. The paper supports its substance, but the field is reserved for exact quoted source text.

### F3: Curate bounded mechanism, activity and transcriptomics evidence after form adjudication

informational / open / confirmed; issue key: abaucin-claim-level-mechanism-assay-dataset-enrichment.

Primary2023 and2026 experiments provide assay and LolDF mechanism leads, and GEO provides a directly relevant public dataset. Preserve the hydrochloride/freebase boundary, LolE/LolF naming, surrogate organisms, indirect transcriptomic response versus binding, and panel-specific selectivity.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained exact synonym and document the tested salt form before numeric evidence additions.

- Remove or appropriately qualify MLJS-21001 in curator_antibiotics.tsv row14 based on explicit primaryHCl identity; do not silently replace native freebase with the salt.
- If a separate salt record is proposed, independently resolve full salt structure/key and source ownership; do not duplicate an existing adopted structure.
- For each proposed assay determine actual material and mass basis; retain published values without unsupported freebase conversion.
- Reseed through native validated writer/history then focused schema/strict,chemistry and required shared gates.

### A2

Replace source evidence_snippet with a short exact passage and move the current interpretation to evidence_notes.

- Verify the replacement word-for-word against the inspected original publication with precise locator.
- Preserve citation and salt/assay qualifications in notes, reseed and validate source-concept evidence plus corpus reproduction.

### A3

Optionally add claim-level exact-form activity,LolDF mechanism andGEO context without promoting status solely on this review.

- Use original organism/strain,endpoint,units,method,medium,time and exact-material scope for every activity entry; do not generalize species exclusivity or clinical efficacy.
- Separate2023 genetics/CRISPRi/RNA response from2026 direct structural/BLI/transport evidence. Ground a microbial complex/function and retain organism-specific protein examples; do not label hostCCR2 as antibacterial target.
- Keep2026 A.baylyi complementation distinct fromA.baumannii and preserve two/four ligand structural-state context. Resolve2026 supplied material before detailed freebase-specific claims.
- AddGSE214305 as exposure transcriptomics with ATCC17978/timing; iModulonDBABUW membership is different context.
- Use write_validated_antibiotic and record_curation_event on the actual native path; run focused and required shared checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/abaucin.yaml; Entire native YAML after075 capture. | supports | PROPOSED/MINTED neutral freebase, definition of a spirocyclic substituted phenethylamine with narrow A.baumannii activity, synonyms RS-102895/RS102895/MLJS-21001, antibacterial role33282, PubChem10000456, one CURATOR source concept with citation/snippet/notes and one2026-09-08 proposed event. Optional mechanism, target, activity, resistance, producer, dataset and clinical objects are absent. |
| source | curation/curator_antibiotics.tsv; Exact row14 in075-raw.json; seeder594–693 and1483–1669; conf/sources.yaml and maintained decisions. | supports | Native record exactly reproduces the curator inventory. load_curator_concepts copies evidence_snippet into source_concepts.evidence.snippet and copies the synonym list without converting salt scope. The stable DOI-fragment source_id reproduces CURATOR mint f8f4ef7fbd. PROPOSED status is deliberate for curator-only entries. No adopted ChEBI/ARO exact-key entry or override was found in the ignored-inclusive search. All13 captured inputs unchanged. |
| identity | https://pubchem.ncbi.nlm.nih.gov/compound/10000456; Official075-pubchem.json and075-synonyms.json; full ChEBI93458 page075-chebi.html/txt. | supports | PubChem matches all native structural fields: neutral C21H21F3N2O2,keyHIDWEYPGMLIQSN-UHFFFAOYSA-N,mass390.4,exact390.15551240; RS-102895,RS102895 and abaucin labels agree. Current ChEBI93458 is a third-party annotated exact-structure candidate with the same InChI/key and benzoxazine parent. It is not an adopted antimicrobial source row here; candidate grounding needs explicit adjudication rather than automatic status promotion. PubChem synonym aggregation includes a hydrochloride phrase, so synonym text alone is not proof of salt equivalence. |
| chemistry | Independent RDKit calculation; 075-chemistry.json/log;075-chemistry-check.py source-specific mint checks. | supports | SMILES and InChI parse to one neutral fragment, same full key,C21H21F3N2O2,average390.405 and exact390.155512572,with no chiral centres. PubChem mass390.4 is correctly rounded. CURATOR source-id SHA256 mint agrees. This does not make the hydrochloride salt the same exact structure. |
| primary | DOI:10.1038/s41589-023-01349-8; PMID37231267 verified075-epmc.json; full author-hosted075-2023-author.pdf from MIT; Results,Table1 visually inspected075-table1.png,Methods. | supports | The paper explicitly renames RS102895 as abaucin and reports A.baumannii ATCC17978 MIC about2µg/mL. Table1 differentiates abaucin1 from analogues2–4; assays use twofold dilution in LB at37°C until controls reach stationary phase, biological duplicate. It shows weak killing/regrowth after withdrawal, no activity in nutrient-depleted PBS and narrow panel activity, not universal species exclusivity. Clinical41-isolate panel and Supplementary Table1 support the native clinical-isolate statement; B.breve/B.longum are exceptions among53 commensals. |
| salt | DOI:10.1038/s41589-023-01349-8; Supplementary Note1 PDF pages10–11,075-2023-si.pdf/text; page11 visually inspected075-si-identity.png. | refutes | MethodA converts purified material with4.0M HCl/dioxane to an HCl salt. The next page labels that explicitly drawn •HCl material MLJS-21001,compound1,with0.313g/0.733mmol yield and95.9%HPLC purity. The yield ratio is consistent with the hydrochloride mass, not390.4 freebase. Main Table1 depicts the parent scaffold; it does not negate the explicit isolated salt. Thus MLJS-21001 is not supported as an unqualified exact synonym of the neutral structure, and quantitative assay form/mass basis needs retention. |
| 2023-mechanism | DOI:10.1038/s41589-023-01349-8; Full original Results/Figure3,Discussion,Methods and supplementary resistance table. | context_only | 2023 provides resistant-mutant mapping to LolE,CRISPRi sensitization,qPCR expression changes, morphology and transcriptomics; it does not directly measure drug binding. LolE is also called LolF in A.baumannii. ETC transcript changes and E.coli Cpx analogy are response/model evidence, not proof of direct respiratory inhibition or a measured A.baumannii Cpx phosphorylation chain. Wound-model control of bacterial burden is preclinical, not clinical efficacy. |
| new-mechanism | https://doi.org/10.1038/s41467-026-75428-4; Pang et al2026,075-2026.pdf/xml; inspected abstract,Results/Figures1,3–5 and relevant binding,transport/ATPase methods. | context_only | New primary structural and biochemical evidence includes abaucin-bound A.baumannii LolDF cryo-EM, BLI binding and impaired BamE transfer to LolA. The BLI uses detergent-solubilized purified complexes; cellular mutant complementation uses A.baylyi surrogate. Substrate association is preserved in the transport experiment. The2026 study reports A.baylyi activity and distinct assay MICs, so selectivity must remain panel/condition-specific. These are enrichment leads after exact supplied-form adjudication, not native asserted targets. |
| new-mechanism2 | https://doi.org/10.1038/s41467-026-72778-x; Zhang et al2026,075-2026b.pdf; inspected abstract,abaucin-binding Results and Discussion,protein preparation context. | context_only | Independent original work resolves two- and four-abaucin LolDF-bound states and measures ATPase inhibition with mutational probes. Do not collapse these structural states into a universal fixed occupancy or treat all proposed transport-cycle steps as directly observed. No existing native claim conflicts with these newly inspected mechanism leads. |
| dataset | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE214305; Full official075-geo.txt metadata and original transcriptomics methods. | context_only | GSE214305 is public ATCC17978 expression profiling after abaucin exposure, linked to PRJNA884833 and seven GSM samples. Original methods specify5xMIC/10µg/mL with3,4.5,6h exposure versus controls. It is a directly relevant optional dataset link, unlike the separate ABUW adapter context. Metadata were inspected, raw reads/reanalysis were not. |
| adapter | iModulonDB a_baumannii/precise139; Inspected same-session055 dataset inventory; actual075-imodulondb-lole.txt after sandbox inventoryDNS failure. | context_only | Exact querylolE returns a_baumannii/precise139/ABUW_0974, namedlolC and annotated lipoprotein-releasing system transmembrane protein LolE; zero module hits. This naming/strain distinction is preserved. It does not prove direct abaucin binding, drug response, or equivalence to the ATCC17978 experiment. |
| search | CultureBotAI/AntibioticMech; 075-local-hits.txt,075-maintained-search.txt and bounded official/primary web research. | context_only | Ignored-inclusive searches found only the curator source and review queue for this exact target, no target-specific overlay, decision or prior review in searched paths. Official identity and primary exact-name/DOI searches recovered2023 synthesis and2026 mechanism sources. A mistaken PMC10229426 search-result linkage resolved to an unrelated imaging paper and was rejected. No claim of exhaustive literature absence is made. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Exact form,synonyms,evidence standard,native optional fields; CLAUDE/CURATION/HARMONIZATION. | supports | A salt is a distinct exact structure. Evidence snippet is verbatim; curator paraphrase belongs in notes. Optional targets/activity/datasets need claim-level support but are not mandatory, and a review does not promote PROPOSED status. |
| validation | Focused documented native gates; 075-focused-results.json/schema.log/strict.log/strict.tsv; actual075-chemistry command exit0. | supports | Schema and strict pass; native chemistry and source mint pass. Actual shared corpus gates are recorded in the finalized review; full QC and chemical-map check encounter the pinned SciPy binary failure. |

## Limits And Additional Notes

- The scientific review retained all 13 captured maintained inputs unchanged. Shared corpus gates are reported with actual outcomes in the finalized review; the pinned SciPy binary prevents full QC and chemical-map completion.
- Publisher2023 main was paywalled; full author-hosted MIT PDF and publisher supplementary PDF were inspected instead. Supplementary chemistry and Table1 structures were visually checked; NMR raw spectra were not independently reinterpreted.
- Inspected selected2026 primary results and relevant biochemical methods, not every supplemental dataset or experimental provenance. Supplied salt form in those studies remains unresolved; no numeric direct-target entry is proposed as already curated.
- Current ChEBI93458 matching structure is a third-party annotated candidate, not an adopted antimicrobial entry. Formal exact grounding remains a curated decision; missing direct ChEBI grounding alone is not classified as an error.
- Fresh adapter inventory failed DNS; prior successful session inventory and a successful exact LolE query supplied bounded context. No module hits; no absence-based negative biological conclusion. GEO metadata inspected,raw sequencing not reanalysed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T083213Z-abaucin
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Abaucin: supported antibacterial activity with a hydrochloride synonym conflict'
started_at: '2026-10-21T08:21:08Z'
finished_at: '2026-10-21T08:32:13Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author record; captured inputs before judgment, read
    entire native record, curator row and seeder, inspected official identities, original
    article and supplementary chemistry, and bounded newer primary mechanism sources.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Neutral abaucin chemistry matches official PubChem and ChEBI and its antibacterial
  activity is supported. The primary synthesis identifies MLJS-21001 as a hydrochloride,
  conflicting with its native exact-synonym placement on the neutral freebase. A minor
  finding concerns paraphrase in a verbatim-snippet slot; an informational follow-up
  identifies scoped activity, LolDF mechanism and transcriptomics enrichment.
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
  - path: data/antibiotics/antibacterial/abaucin.yaml
    sha256: f62b655fc6aaab918a8c16566c4fc24c5cf91c87b11b4fb9420b5bbfd0fde4e3
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
- target_id: antibioticmech:curator-f8f4ef7fbd
  path: data/antibiotics/antibacterial/abaucin.yaml
  label: Abaucin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Row14 owns exact synonyms, definition, structure and source-concept evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: load_curator_concepts and generated field emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Formal grounding decision if justified
scope:
  description: Whole record, maintained curator source and seeder, sole adopted publication,
    original supplementary chemistry/assays, official chemical identities, structured
    LolE context, GEO metadata and selected2026 original mechanism results/methods.
  selection: Queue075, antibioticmech:curator-f8f4ef7fbd at the locked path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  exclusions:
  - target: Abaucin hydrochloride, analogues2–4, serdemetan and host CCR2 pharmacology
    reason: Keep exact salts and compounds distinct; host pharmacology is not the
      microbial antibacterial target.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Focused LinkML validation exited0.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/abaucin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Focused strict scan has zero ERROR rows.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/abaucin.yaml --out /private/tmp/am-review-session/075-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Independent native SMILES/InChI chemistry and CURATOR mint agree.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  evidence_ids:
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache .venv/bin/python
    /private/tmp/am-review-session/075-chemistry-check.py 75
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-datasets
  name: adapter-datasets
  status: failed
  required: false
  summary: Fresh inventory request failed DNS in sandbox. Previously inspected same-session
    dataset inventory055 identifies a_baumannii/precise139; used that coverage for
    successful public query.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 datasets
  exit_code: 2
  expected_exit_code: 0
- check_id: adapter-lole
  name: adapter-lole
  status: passed
  required: false
  summary: Public exact LolE query resolves one gene, zero modules. No component summary
    applies.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 search --organism a_baumannii --dataset
    precise139 --query lolE
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
  - antibioticmech:curator-f8f4ef7fbd
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
  - antibioticmech:curator-f8f4ef7fbd
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
  - antibioticmech:curator-f8f4ef7fbd
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
  - antibioticmech:curator-f8f4ef7fbd
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
  - antibioticmech:curator-f8f4ef7fbd
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
  - antibioticmech:curator-f8f4ef7fbd
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
  - antibioticmech:curator-f8f4ef7fbd
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
  - antibioticmech:curator-f8f4ef7fbd
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
  - antibioticmech:curator-f8f4ef7fbd
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/abaucin.yaml
  locator: Entire native YAML after075 capture.
  accessed_at: '2026-10-21T08:25:39Z'
  support: supports
  summary: PROPOSED/MINTED neutral freebase, definition of a spirocyclic substituted
    phenethylamine with narrow A.baumannii activity, synonyms RS-102895/RS102895/MLJS-21001,
    antibacterial role33282, PubChem10000456, one CURATOR source concept with citation/snippet/notes
    and one2026-09-08 proposed event. Optional mechanism, target, activity, resistance,
    producer, dataset and clinical objects are absent.
- evidence_id: source
  kind: record_content
  reference: curation/curator_antibiotics.tsv
  locator: Exact row14 in075-raw.json; seeder594–693 and1483–1669; conf/sources.yaml
    and maintained decisions.
  accessed_at: '2026-10-21T08:25:39Z'
  support: supports
  summary: Native record exactly reproduces the curator inventory. load_curator_concepts
    copies evidence_snippet into source_concepts.evidence.snippet and copies the synonym
    list without converting salt scope. The stable DOI-fragment source_id reproduces
    CURATOR mint f8f4ef7fbd. PROPOSED status is deliberate for curator-only entries.
    No adopted ChEBI/ARO exact-key entry or override was found in the ignored-inclusive
    search. All13 captured inputs unchanged.
  snapshot_sha256: 036504cdca24e40fd415dc4dbe602b48b98894d676bab5642f5b0f1768bfde5a
- evidence_id: identity
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/10000456
  locator: Official075-pubchem.json and075-synonyms.json; full ChEBI93458 page075-chebi.html/txt.
  accessed_at: '2026-10-21T08:25:39Z'
  support: supports
  summary: 'PubChem matches all native structural fields: neutral C21H21F3N2O2,keyHIDWEYPGMLIQSN-UHFFFAOYSA-N,mass390.4,exact390.15551240;
    RS-102895,RS102895 and abaucin labels agree. Current ChEBI93458 is a third-party
    annotated exact-structure candidate with the same InChI/key and benzoxazine parent.
    It is not an adopted antimicrobial source row here; candidate grounding needs
    explicit adjudication rather than automatic status promotion. PubChem synonym
    aggregation includes a hydrochloride phrase, so synonym text alone is not proof
    of salt equivalence.'
  snapshot_sha256: ffcc7479f4efdf794bb3c4890da4d5a07ce7691c4339834ed094aa881ebf62cc
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculation
  locator: 075-chemistry.json/log;075-chemistry-check.py source-specific mint checks.
  accessed_at: '2026-10-21T08:25:39Z'
  support: supports
  summary: SMILES and InChI parse to one neutral fragment, same full key,C21H21F3N2O2,average390.405
    and exact390.155512572,with no chiral centres. PubChem mass390.4 is correctly
    rounded. CURATOR source-id SHA256 mint agrees. This does not make the hydrochloride
    salt the same exact structure.
  snapshot_sha256: 0635eab758e1edbde8f3ca54322da4eafde2babf3c9d7df99120be110c40631c
- evidence_id: primary
  kind: primary_source
  reference: DOI:10.1038/s41589-023-01349-8
  locator: PMID37231267 verified075-epmc.json; full author-hosted075-2023-author.pdf
    from MIT; Results,Table1 visually inspected075-table1.png,Methods.
  accessed_at: '2026-10-21T08:25:39Z'
  support: supports
  summary: The paper explicitly renames RS102895 as abaucin and reports A.baumannii
    ATCC17978 MIC about2µg/mL. Table1 differentiates abaucin1 from analogues2–4; assays
    use twofold dilution in LB at37°C until controls reach stationary phase, biological
    duplicate. It shows weak killing/regrowth after withdrawal, no activity in nutrient-depleted
    PBS and narrow panel activity, not universal species exclusivity. Clinical41-isolate
    panel and Supplementary Table1 support the native clinical-isolate statement;
    B.breve/B.longum are exceptions among53 commensals.
  snapshot_sha256: 398de987927fc407f4e621eedaa4b5452764fdb87020d6531b7cb099aa9cea81
- evidence_id: salt
  kind: primary_source
  reference: DOI:10.1038/s41589-023-01349-8
  locator: Supplementary Note1 PDF pages10–11,075-2023-si.pdf/text; page11 visually
    inspected075-si-identity.png.
  accessed_at: '2026-10-21T08:25:39Z'
  support: refutes
  summary: MethodA converts purified material with4.0M HCl/dioxane to an HCl salt.
    The next page labels that explicitly drawn •HCl material MLJS-21001,compound1,with0.313g/0.733mmol
    yield and95.9%HPLC purity. The yield ratio is consistent with the hydrochloride
    mass, not390.4 freebase. Main Table1 depicts the parent scaffold; it does not
    negate the explicit isolated salt. Thus MLJS-21001 is not supported as an unqualified
    exact synonym of the neutral structure, and quantitative assay form/mass basis
    needs retention.
  snapshot_sha256: f4193934a8f064681512443f30e2c65598c43ee471986905c076b55e7e2667e7
- evidence_id: 2023-mechanism
  kind: primary_source
  reference: DOI:10.1038/s41589-023-01349-8
  locator: Full original Results/Figure3,Discussion,Methods and supplementary resistance
    table.
  accessed_at: '2026-10-21T08:25:39Z'
  support: context_only
  summary: 2023 provides resistant-mutant mapping to LolE,CRISPRi sensitization,qPCR
    expression changes, morphology and transcriptomics; it does not directly measure
    drug binding. LolE is also called LolF in A.baumannii. ETC transcript changes
    and E.coli Cpx analogy are response/model evidence, not proof of direct respiratory
    inhibition or a measured A.baumannii Cpx phosphorylation chain. Wound-model control
    of bacterial burden is preclinical, not clinical efficacy.
- evidence_id: new-mechanism
  kind: primary_source
  reference: https://doi.org/10.1038/s41467-026-75428-4
  locator: Pang et al2026,075-2026.pdf/xml; inspected abstract,Results/Figures1,3–5
    and relevant binding,transport/ATPase methods.
  accessed_at: '2026-10-21T08:25:39Z'
  support: context_only
  summary: New primary structural and biochemical evidence includes abaucin-bound
    A.baumannii LolDF cryo-EM, BLI binding and impaired BamE transfer to LolA. The
    BLI uses detergent-solubilized purified complexes; cellular mutant complementation
    uses A.baylyi surrogate. Substrate association is preserved in the transport experiment.
    The2026 study reports A.baylyi activity and distinct assay MICs, so selectivity
    must remain panel/condition-specific. These are enrichment leads after exact supplied-form
    adjudication, not native asserted targets.
  snapshot_sha256: 505ce6a6c551053fe56c9fccf3bb943611ea5a90c87a4eb7add40389d6b6cbc6
- evidence_id: new-mechanism2
  kind: primary_source
  reference: https://doi.org/10.1038/s41467-026-72778-x
  locator: Zhang et al2026,075-2026b.pdf; inspected abstract,abaucin-binding Results
    and Discussion,protein preparation context.
  accessed_at: '2026-10-21T08:25:39Z'
  support: context_only
  summary: Independent original work resolves two- and four-abaucin LolDF-bound states
    and measures ATPase inhibition with mutational probes. Do not collapse these structural
    states into a universal fixed occupancy or treat all proposed transport-cycle
    steps as directly observed. No existing native claim conflicts with these newly
    inspected mechanism leads.
  snapshot_sha256: bbdbf153182968a118982888efea93d9cc2ec55ad8dddfcc5571fffa0157d260
- evidence_id: dataset
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE214305
  locator: Full official075-geo.txt metadata and original transcriptomics methods.
  accessed_at: '2026-10-21T08:25:39Z'
  support: context_only
  summary: GSE214305 is public ATCC17978 expression profiling after abaucin exposure,
    linked to PRJNA884833 and seven GSM samples. Original methods specify5xMIC/10µg/mL
    with3,4.5,6h exposure versus controls. It is a directly relevant optional dataset
    link, unlike the separate ABUW adapter context. Metadata were inspected, raw reads/reanalysis
    were not.
  snapshot_sha256: ae61eaa78edb32e2bb0f7ca1fa8934f532c4f3fd220fa6af01e0c3c0f89f64fe
- evidence_id: adapter
  kind: database
  reference: iModulonDB a_baumannii/precise139
  locator: Inspected same-session055 dataset inventory; actual075-imodulondb-lole.txt
    after sandbox inventoryDNS failure.
  accessed_at: '2026-10-21T08:25:39Z'
  support: context_only
  summary: Exact querylolE returns a_baumannii/precise139/ABUW_0974, namedlolC and
    annotated lipoprotein-releasing system transmembrane protein LolE; zero module
    hits. This naming/strain distinction is preserved. It does not prove direct abaucin
    binding, drug response, or equivalence to the ATCC17978 experiment.
  snapshot_sha256: 158481f0aaba5390edc1bd1a107d57770f86d5a92503269aeb1c8ca7d555bb3c
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 075-local-hits.txt,075-maintained-search.txt and bounded official/primary
    web research.
  accessed_at: '2026-10-21T08:25:39Z'
  support: context_only
  summary: Ignored-inclusive searches found only the curator source and review queue
    for this exact target, no target-specific overlay, decision or prior review in
    searched paths. Official identity and primary exact-name/DOI searches recovered2023
    synthesis and2026 mechanism sources. A mistaken PMC10229426 search-result linkage
    resolved to an unrelated imaging paper and was rejected. No claim of exhaustive
    literature absence is made.
  search_scope: rg --no-ignore --hidden across batch008 excluding.git/.venv; focused
    curation,conf,scripts,data/raw,reports/yaml_record_review,reviews onabaucin,f8f4ef7fbd,01349-8,HIDWEYPGMLIQSN,RS-102895,MLJS-21001.
    OfficialPubChem/ChEBI/PubMed/EuropePMC/Nature,authorMITPDF,NCBIGEO and iModulonDB
    inspected. Vendors/Wikipedia/search snippets only leads, not biological support.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Exact form,synonyms,evidence standard,native optional fields; CLAUDE/CURATION/HARMONIZATION.
  accessed_at: '2026-10-21T08:25:39Z'
  support: supports
  summary: A salt is a distinct exact structure. Evidence snippet is verbatim; curator
    paraphrase belongs in notes. Optional targets/activity/datasets need claim-level
    support but are not mandatory, and a review does not promote PROPOSED status.
- evidence_id: validation
  kind: validation
  reference: Focused documented native gates
  locator: 075-focused-results.json/schema.log/strict.log/strict.tsv; actual075-chemistry
    command exit0.
  accessed_at: '2026-10-21T08:25:39Z'
  support: supports
  summary: Schema and strict pass; native chemistry and source mint pass. Actual shared
    corpus gates are recorded in the finalized review; full QC and chemical-map check
    encounter the pinned SciPy binary failure.
  snapshot_sha256: 3d8853e8adb47bff2f962220f8abd04f3b8a14ea15a902440275810f3b9f6fbe
assessments:
- assessment_id: native-structure
  area: identity
  topic: Freebase identity
  outcome: supported
  summary: PubChem,ChEBI and native representations agree on the neutral freebase;
    the structural definition is coherent.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  evidence_ids:
  - identity
  - chemistry
  - primary
- assessment_id: equivalence
  area: identity
  topic: MLJS-21001 exact synonym
  outcome: concern
  summary: Original synthesis explicitly uses this code for the HCl salt, conflicting
    with unqualified exact synonym on freebase.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  evidence_ids:
  - salt
  - record
  - rubric
- assessment_id: activity
  area: evidence
  topic: Antibacterial definition and clinical isolate support
  outcome: supported
  summary: The exact parent compound and tested material are explicitly linked by
    the adopted paper, which supports antibacterial activity and the bounded strain
    panel. Salt basis must accompany future numeric claims; no evidence of inactivity
    is inferred.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  evidence_ids:
  - primary
  - salt
- assessment_id: evidence-format
  area: evidence
  topic: Quotation versus interpretation
  outcome: concern
  summary: Source snippet is an author-attributed curator summary, not a short verbatim
    passage. Its scientific content is supported, but placement violates native evidence
    rules.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  evidence_ids:
  - record
  - source
  - primary
  - rubric
- assessment_id: mechanism
  area: completeness
  topic: Target/response boundaries
  outcome: unknown
  summary: Mechanism is a concrete optional enrichment opportunity.2023 indirect evidence
    and2026 direct biochemical/structural work must be distinguished; exact assay
    form and species context retained.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  evidence_ids:
  - 2023-mechanism
  - new-mechanism
  - new-mechanism2
  - adapter
- assessment_id: other
  area: completeness
  topic: Datasets,producer,clinical and graphs
  outcome: unknown
  summary: GEO offers a relevant optional link. No biosynthetic producer,clinical
    approval or graph is asserted; none follows automatically from preclinical results
    or expression responses.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  evidence_ids:
  - record
  - dataset
  - rubric
- assessment_id: grounding
  area: grounding
  topic: Minted source rationale and candidate ChEBI
  outcome: supported
  summary: Stable curator DOI-fragment source and exact structure support proposed
    identity. ChEBI93458 is a matching third-party candidate outside adopted inventory,
    requiring explicit curated grounding policy; no duplicated adopted target was
    found.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  evidence_ids:
  - source
  - identity
  - search
- assessment_id: ownership
  area: ownership
  topic: Maintained row/status/history
  outcome: supported
  summary: Curator row14 and seeder own the two corrective findings. All13 captured
    hashes unchanged; no native status/history modified.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  evidence_ids:
  - source
  - rubric
- assessment_id: gates
  area: schema
  topic: Focused schema/strict/chemistry
  outcome: supported
  summary: Documented focused validators and independent chemistry pass despite scientific
    salt/synonym and snippet findings.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: abaucin-mljs-21001-hydrochloride-exact-synonym
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: MLJS-21001 denotes the synthesized hydrochloride in the primary source
  description: The neutral freebase record lists MLJS-21001 as EXACT_SYNONYM. Supplementary
    Note1 explicitly synthesizes, draws and labels MLJS-21001 compound1 as •HCl. Preserve
    this salt distinction and do not attach unqualified salt-mass assay values to
    the freebase. This does not refute abaucin antibacterial activity or the correctness
    of native freebase structure.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  field_paths:
  - synonyms
  - source_concepts
  evidence_ids:
  - record
  - identity
  - salt
  - rubric
  rule_id: 'native-review-checklist: Identity/Equivalence; CLAUDE salt identity invariant'
  native_severity: major exact-form scope inflation
  normalization_reason: A specific source-defined salt is asserted as exact equivalence
    to a neutral structure. The record overall still denotes the intended parent,
    so this is major rather than a whole-record wrong-identity blocker.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Row14 owns exact synonyms, definition, structure and source-concept evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: load_curator_concepts and generated field emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Formal grounding decision if justified
- finding_id: F2
  issue_key: abaucin-curator-paraphrase-in-snippet
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Move the curator summary out of the verbatim snippet slot
  description: The source-concept snippet beginning with author attribution is a paraphrase
    of discovery/activity findings. The paper supports its substance, but the field
    is reserved for exact quoted source text.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  field_paths:
  - source_concepts.evidence.snippet
  evidence_ids:
  - source
  - primary
  - rubric
  rule_id: 'native-review-checklist: Evidence standard'
  native_severity: minor evidence-format provenance
  normalization_reason: Supported content is misplaced; this is not fabricated activity
    or an unsupported scientific conclusion.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Row14 owns exact synonyms, definition, structure and source-concept evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: load_curator_concepts and generated field emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Formal grounding decision if justified
- finding_id: F3
  issue_key: abaucin-claim-level-mechanism-assay-dataset-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Curate bounded mechanism, activity and transcriptomics evidence after form
    adjudication
  description: Primary2023 and2026 experiments provide assay and LolDF mechanism leads,
    and GEO provides a directly relevant public dataset. Preserve the hydrochloride/freebase
    boundary, LolE/LolF naming, surrogate organisms, indirect transcriptomic response
    versus binding, and panel-specific selectivity.
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  field_paths:
  - evidence
  - activity_spectrum
  - molecular_targets
  - datasets
  - discussions
  evidence_ids:
  - primary
  - salt
  - 2023-mechanism
  - new-mechanism
  - new-mechanism2
  - dataset
  - adapter
  - rubric
  rule_id: 'native-review-checklist: Mode/Targets/Activity/Datasets'
  native_severity: informational optional enrichment
  normalization_reason: These collections are optional in a PROPOSED record; no missing
    required representation is alleged.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/abaucin.yaml
    role: Curator-added claim evidence, activity, mechanism, discussions and dataset
      links through validated writer/history
actions:
- action_id: A1
  description: Correct the maintained exact synonym and document the tested salt form
    before numeric evidence additions.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Row14 owns exact synonyms, definition, structure and source-concept evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: load_curator_concepts and generated field emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Formal grounding decision if justified
  acceptance_checks:
  - Remove or appropriately qualify MLJS-21001 in curator_antibiotics.tsv row14 based
    on explicit primaryHCl identity; do not silently replace native freebase with
    the salt.
  - If a separate salt record is proposed, independently resolve full salt structure/key
    and source ownership; do not duplicate an existing adopted structure.
  - For each proposed assay determine actual material and mass basis; retain published
    values without unsupported freebase conversion.
  - Reseed through native validated writer/history then focused schema/strict,chemistry
    and required shared gates.
- action_id: A2
  description: Replace source evidence_snippet with a short exact passage and move
    the current interpretation to evidence_notes.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Row14 owns exact synonyms, definition, structure and source-concept evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: load_curator_concepts and generated field emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Formal grounding decision if justified
  acceptance_checks:
  - Verify the replacement word-for-word against the inspected original publication
    with precise locator.
  - Preserve citation and salt/assay qualifications in notes, reseed and validate
    source-concept evidence plus corpus reproduction.
- action_id: A3
  description: Optionally add claim-level exact-form activity,LolDF mechanism andGEO
    context without promoting status solely on this review.
  finding_ids:
  - F3
  target_ids:
  - antibioticmech:curator-f8f4ef7fbd
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/abaucin.yaml
    role: Curator-added claim evidence, activity, mechanism, discussions and dataset
      links through validated writer/history
  acceptance_checks:
  - Use original organism/strain,endpoint,units,method,medium,time and exact-material
    scope for every activity entry; do not generalize species exclusivity or clinical
    efficacy.
  - Separate2023 genetics/CRISPRi/RNA response from2026 direct structural/BLI/transport
    evidence. Ground a microbial complex/function and retain organism-specific protein
    examples; do not label hostCCR2 as antibacterial target.
  - Keep2026 A.baylyi complementation distinct fromA.baumannii and preserve two/four
    ligand structural-state context. Resolve2026 supplied material before detailed
    freebase-specific claims.
  - AddGSE214305 as exposure transcriptomics with ATCC17978/timing; iModulonDBABUW
    membership is different context.
  - Use write_validated_antibiotic and record_curation_event on the actual native
    path; run focused and required shared checks.
limitations:
- The scientific review retained all 13 captured maintained inputs unchanged. Shared
  corpus gates are reported with actual outcomes in the finalized review; the pinned
  SciPy binary prevents full QC and chemical-map completion.
- Publisher2023 main was paywalled; full author-hosted MIT PDF and publisher supplementary
  PDF were inspected instead. Supplementary chemistry and Table1 structures were visually
  checked; NMR raw spectra were not independently reinterpreted.
- Inspected selected2026 primary results and relevant biochemical methods, not every
  supplemental dataset or experimental provenance. Supplied salt form in those studies
  remains unresolved; no numeric direct-target entry is proposed as already curated.
- Current ChEBI93458 matching structure is a third-party annotated candidate, not
  an adopted antimicrobial entry. Formal exact grounding remains a curated decision;
  missing direct ChEBI grounding alone is not classified as an error.
- Fresh adapter inventory failed DNS; prior successful session inventory and a successful
  exact LolE query supplied bounded context. No module hits; no absence-based negative
  biological conclusion. GEO metadata inspected,raw sequencing not reanalysed.
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
