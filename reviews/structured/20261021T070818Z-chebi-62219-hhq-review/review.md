# Review of CHEBI:62219: HHQ structure encoding and phenotype boundaries

- Review: 20261021T070818Z-chebi-62219-hhq-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T06:59:19Z
- Finished UTC: 2026-10-21T07:08:18Z
- Reviewer: Codex agent review002 (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One major source-origin structure defect is confirmed: the stored aromatic SMILES cannot be kekulized because the quinolone nitrogen lacks its required hydrogen. InChI, official Molfile and structure drawing consistently identify the intended lactam. Schema and strict validation pass. Primary literature supports scoped antibacterial activity while signalling and swarming evidence must remain distinct from growth inhibition.

## Scope And Provenance

Entire target, maintained source/configuration/code, official identifiers and alternative chemical representations, primary evidence and bounded structured-source cross-check.

Selection: Path-ordered unreviewed queue index 018.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:62219 | data/antibiotics/antibacterial/2-heptyl-4-quinolone.yaml | generated | 2-heptyl-4-quinolone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record LinkML validation | passed | True | CHEBI:62219 | Exit 0; No issues found. |
| Documented per-record closed-schema validation | passed | True | CHEBI:62219 | Exit 0; one file scanned; zero ERROR rows. |
| Independent RDKit structure and internal identifier consistency | failed | False | CHEBI:62219 | RDKit rejects stored SMILES with a kekulization error. Stored InChI and scratch [nH] lactam parse and reproduce the recorded key, formula, charge and masses. Initial chemistry probe also exited 1 for the same parse failure. |
| Independent official Molfile parsing | passed | False | CHEBI:62219 | Official Molfile parses to the [nH] lactam and recorded Standard InChIKey. |
| Structured source dataset discovery | passed | False | CHEBI:62219 | Pseudomonas precise364 and precise411 are exposed; dataset names are not proof of exact PA14 experimental equivalence. |
| Exact regulator-name search in precise364 | passed | False | CHEBI:62219 | Zero name hits; the alias search below resolves MvfR. |
| Exact regulator-name search in precise411 | passed | False | CHEBI:62219 | Zero name hits; no biological absence inference. |
| Regulator-alias search | passed | False | CHEBI:62219 | Found PA1003 and modules 85/MvfR and 15/LasR; only module 85 was selected for relevant context. |
| Relevant MvfR module summary | passed | False | CHEBI:62219 | Seven module member genes in the pqs/phn region; computational expression context only. |
| Additional pathway query | failed | False | CHEBI:62219 | Adapter failed because an iModulon regulator was null where a JSON list was expected. No pathway absence conclusion. |
| Authoritative full QC | failed | True | CHEBI:62219 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:62219 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:62219 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:62219 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:62219 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:62219 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:62219 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:62219 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:62219 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Intended lactam recoverable; SMILES malformed

identity: concern. Targets: CHEBI:62219.

Identity is unambiguous from label, InChI, official Molfile and drawing. The stored SMILES is an invalid chemical representation despite faithful source copying.

### Parent and tautomer boundaries

grounding: supported. Targets: CHEBI:62219.

Broader parent and antibacterial classification are source-backed. Preserve the separate ChEBI tautomer identity; Standard InChI equality does not authorize merging.

### Antibacterial versus behavioural effects

evidence: supported. Targets: CHEBI:62219.

Primary sources independently support scoped HHQ antibacterial activity. Swarming suppression and growth inhibition are separate endpoints.

### Unknown antibacterial mechanism

completeness: unknown. Targets: CHEBI:62219.

Molecular mechanism remains unresolved. Neither expression context nor signalling genetics establishes the antibacterial target.

### Unasserted optional scientific objects

representation: not_applicable. Targets: CHEBI:62219.

Empty optional fields are not blanket errors. Assay and evidence enrichment is actionable but requires precise phenotype and form scope.

### Source defect propagation and seed history

ownership: supported. Targets: CHEBI:62219.

Three history events and mapped fields are consistent with generation. Repair must be reproducible from maintained source inputs/code; scientific additions belong to the actual record.

### Structural validation gap

schema: concern. Targets: CHEBI:62219.

Schema/strict pass while independent chemistry fails. Existing InChI fallback mitigates embedding impact but does not validate the stored SMILES.

## Findings

### F1: Source SMILES omits the lactam nitrogen hydrogen and cannot be parsed

major / open / confirmed; issue key: chebi-62219-smiles-missing-quinolone-nh.

Stored and current ChEBI webpage SMILES CCCCCCCc1cc(=O)c2ccccc2n1 cannot be kekulized by RDKit. The same entry’s Molfile, SVG and stored InChI support CCCCCCCc1cc(=O)c2ccccc2[nH]1. This is a concrete structure-representation defect in an asserted field, not a missing optional enrichment or a tautomer-duplicate finding.

### F2: Primary growth and signalling evidence needs separate claim-level treatment

informational / open / confirmed; issue key: chebi-62219-phenotype-specific-evidence-enrichment.

Specific primary sources can enrich this seed, while the antimicrobial target remains unresolved. Empty optional fields are not assigned a scientific error, and the scope of solution-phase HHQ experiments must be explicit.

## Recommended Actions And Acceptance Checks

### A1

During separately authorized curation, correct the maintained extraction/structure representation using the official Molfile and provenance-backed normalization, regenerate the target, and retain the lactam identity. The validated scratch [nH] candidate provides a concrete repair to assess.

- The stored SMILES sanitizes and agrees with the official lactam Molfile on formula, charge, connectivity and Standard InChIKey.
- Preserve CHEBI:62219 and its tautomer-specific naming; do not merge CHEBI:75306 solely because mobile-H keys match.
- Rerun the documented source extraction/seeding path and just validate, just validate-strict, just verify-corpus --summary and just qc; inspect affected structure outputs.

### A2

Curate primary HHQ growth observations separately from swarming or signalling findings, retain strain/media/dose and tested chemical-form context, and preserve an explicit unresolved antibacterial-mechanism rationale.

- Fixed-dose growth and swarm phenotypes are not converted into MICs or direct target-binding assertions.
- Do not transfer PQS, HQNO, modified-analogue or expression-module effects to the parent antibacterial mechanism.
- Use the validated writer and curation history, with focused validation and native promotion gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/2-heptyl-4-quinolone.yaml; Entire YAML | supports | Read exact identity, structural definition, three aliases, parent, role, both chemical encodings, masses, registry, source concept and all three history events. No scientific evidence, mechanism, target, activity observation, resistance, producer, clinical, dataset or causal-graph object is asserted. |
| inventory | data/raw/chebi_antimicrobials.tsv; Complete CHEBI:62219 row at line 1079 and header; maintained tables | supports | The 3-star in-scope row has the same SMILES, InChI, metadata and sole PMID:21965567 lead; mechanism-role column is empty. No exact-ID/minted-ID decision or curator override matched the inclusive search. |
| ownership | scripts/extract_source_inventory.py; ChEBI default-structure selection and row construction; scripts/seed_from_sources.py structure_from_chebi, mint and build_record; source config and MANIFEST | supports | Extractor copies the default ChEBI SMILES and seeder copies that string to the record. Citation leads are not automatically claim evidence. Antibacterial mapping and source version reproduce the adopted inventory. Scientific additions and source-field repairs have distinct maintained owners. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:62219; Full entry, aliases, ontology, registry and structure fields | supports | Official label, three aliases, definition, formula, charge, masses, InChI/key, Reaxys 1529939, parent and antibacterial role match. The current entry repeats the same unparseable SMILES. Other roles are outside the adopted antimicrobial subset. |
| parent | https://www.ebi.ac.uk/chebi/CHEBI:23765; Official quinolone entry, outgoing and incoming edges | supports | The broader quinolone class resolves and lists CHEBI:62219 as a child. It is not an exact identity cross-reference or an inference of fluoroquinolone topoisomerase action. |
| role | https://www.ebi.ac.uk/chebi/CHEBI:33282; Definition and exact compound outgoing edge | supports | The identifier denotes antibacterial agent, matching source classification. |
| tautomer | https://www.ebi.ac.uk/chebi/CHEBI:75306; Full official lactim entry and reciprocal tautomer edge from CHEBI:62219 | supports | ChEBI distinguishes keto/lactam CHEBI:62219 from hydroxy/lactim CHEBI:75306 while assigning identical mobile-H Standard InChI and key. Different tautomer-specific names/registry entries are preserved. Shared Standard InChI alone is not a duplicate determination. |
| chemistry | RDKit 2026.03.5 independent calculation; /private/tmp/am-review-session/018-chemistry-check.py; 018-structure.json; 018-chemistry.log | refutes | Stored CCCCCCCc1cc(=O)c2ccccc2n1 fails sanitization/kekulization. Stored InChI parses to CCCCCCCc1cc(=O)c2ccccc2[nH]1, reproducing UYRHHBXYXSYGHA-UHFFFAOYSA-N, C16H21NO, charge 0, masses 243.35/243.162314292, one fragment, no stereocenters and minted antibioticmech:chebi-a9be2766fb. The scratch lactim also shares the mobile-H key. |
| molfile | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/62219; Official Molfile; /private/tmp/am-review-session/018-chebi.mol; 018-chebi-chemistry.py | supports | Official Molfile independently parses to CCCCCCCc1cc(=O)c2ccccc2[nH]1, formula C16H21NO and the stored key. This corroborates the intended lactam without substituting the lactim record. |
| drawing | https://www.ebi.ac.uk/chebi/backend/api/public/structure/2779534/; Official SVG rendered locally as 018-chebi.png and visually inspected | supports | The official structure explicitly depicts NH and the 4-carbonyl with a heptyl substituent at position 2. |
| fallback | src/antibioticmech/chemical_embedding.py; parse_structure, lines 191-220 | context_only | The embedding parser attempts SMILES then Standard InChI. The valid fallback bounds impact: this finding does not claim every downstream consumer fails. |
| primary2011 | PMID:21965567; DOI:10.1128/JB.05929-11; author-hosted full PDF https://www-spring.ch.cam.ac.uk/publications/pdf/2011_JB_6770.pdf; Methods, Table 3, Results and Discussion | supports | Chemically synthesized HHQ at 0.5 µM represses swarming in specified P. aeruginosa PA14 mutants on arginine medium; PqsR and phenazine/PCA-dependent genetic relationships are investigated. The authors leave downstream steps unresolved. These signalling/phenotype experiments are not antibacterial MIC or direct lethal-target measurements. |
| primary-activity | PMID:21539583; PubMed abstract; DOI:10.1111/j.1574-6941.2011.01121.x | supports | The abstract names HHQ as 2-heptyl-4-quinolone and reports bacteriostatic activity including V. vulnificus, alongside separate motility and biofilm effects. It supports antibacterial activity without supplying a compound-wide direct target. |
| primary2020 | DOI:10.1099/mic.0.000876; Publisher abstract and author-uploaded full text https://www.researchgate.net/publication/338083972_A_structure-function_analysis_of_interspecies_antagonism_by_the_2-heptyl-4-alkyl-quinolone_signal_molecule_from_Pseudomonas_aeruginosa; Methods, Results and Discussion | supports | HHQ testing at 10 µM shows strain/medium-dependent growth inhibition and unaffected comparators, including V. parahaemolyticus RIMD 2210633. The authors explicitly leave its antibacterial mechanism unknown and distinguish this from antivirulence activity. HHQ is named using hydroxyquinoline terminology; no isolated-tautomer potency difference is established. Analogue/PQS/HQNO results must not transfer. |
| adapter | iModulonDB public API via kg-microbe-sources; /private/tmp/am-review-session/018-imodulondb-datasets.json; pqsR364.txt; pqsR411.txt; mvfR364.txt; summary85.txt; phenazine411.err | context_only | Exact pqsR queries returned no hits; mvfR resolves p_aeruginosa/precise364/PA1003 and MvfR module p_aeruginosa/precise364/85. Summary has seven pqs/phn members. This is expression-module context, not binding, PA14 phenotype or antibacterial-mechanism proof. The precise411 phenazine query failed schema normalization on null regulator; no absence is inferred. |
| validation | just validate; just validate-strict; /private/tmp/am-review-session/018-validate.log; 018-strict.log; 018-strict.tsv | supports | Both documented focused validators exited 0; strict scanned one file and returned zero ERROR rows. These gates do not refute the independent chemical parser failure. |
| search | Inclusive local and bounded free source search; 018-local-hits.txt; 018-owner-search.txt; free exact-name/identifier/primary-title retrieval | context_only | No maintained exact-ID/minted-ID override matched. Full official identity, author-hosted primary paper and author-uploaded primary text were inspected; unrelated congener results were kept separate. |

## Limits And Additional Notes

- Independent Reaxys destination was not accessed; its asserted identifier was verified against official ChEBI.
- The 2011 interspecies paper was inspected at abstract level. The adopted swarming paper was inspected in author-hosted full text; the 2020 paper was inspected through author-uploaded full text after publisher full-text retrieval failed.
- The optional precise411 phenazine adapter query failed on a null regulator field. Successful alias/module retrieval remains contextual and is not exact PA14 experiment or antimicrobial target evidence.
- Bounded retrieval did not establish a direct HHQ antibacterial target; this is not an exhaustive literature-absence claim.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No record, source table or generated artifact was changed. Original input capture was retained; chemical_embedding.py was additionally hashed as reviewed implementation context.
- The initial chemistry probe and the robust follow-up both failed on stored SMILES; the independent official Molfile check passed. Scratch candidate structures were not applied.
- The author PDF Figure 2 was visually inspected for pathway context; the explicit chemical NH drawing was verified in the official ChEBI SVG, not inferred from that pathway figure.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T070818Z-chebi-62219-hhq-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Review of CHEBI:62219: HHQ structure encoding and phenotype boundaries'
started_at: '2026-10-21T06:59:19Z'
finished_at: '2026-10-21T07:08:18Z'
reviewer:
  identity: Codex agent review002
  kind: agent
  independence: independent
  independence_basis: Read-only review in a task-owned worktree, by an agent uninvolved
    in authoring the record; exact input hashes were captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: SEEDED identity recoverable from InChI and official Molfile; stored
  SMILES needs correction
scientific_review: true
summary: 'One major source-origin structure defect is confirmed: the stored aromatic
  SMILES cannot be kekulized because the quinolone nitrogen lacks its required hydrogen.
  InChI, official Molfile and structure drawing consistently identify the intended
  lactam. Schema and strict validation pass. Primary literature supports scoped antibacterial
  activity while signalling and swarming evidence must remain distinct from growth
  inhibition.'
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
  - path: data/antibiotics/antibacterial/2-heptyl-4-quinolone.yaml
    sha256: 821a5ddb81a01d413df4f447de50280acef38aa07bc9104b37c68ef4caff881f
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
  - path: src/antibioticmech/chemical_embedding.py
    sha256: 43d4e2f2a598e6e9938f68a7a5d97c8837102a9f629bee4bb7449fb86828bae1
    role: context
scope:
  description: Entire target, maintained source/configuration/code, official identifiers
    and alternative chemical representations, primary evidence and bounded structured-source
    cross-check.
  selection: Path-ordered unreviewed queue index 018.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:62219
  exclusions:
  - target: CHEBI:75306 lactim and other alkylquinolone congeners
    reason: Used only to preserve tautomer and analogue boundaries; no separate record
      verdict or deduplication is assigned.
targets:
- target_id: CHEBI:62219
  path: data/antibiotics/antibacterial/2-heptyl-4-quinolone.yaml
  label: 2-heptyl-4-quinolone
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
checks:
- check_id: schema
  name: Documented per-record LinkML validation
  status: passed
  required: true
  summary: Exit 0; No issues found.
  target_ids:
  - CHEBI:62219
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/2-heptyl-4-quinolone.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented per-record closed-schema validation
  status: passed
  required: true
  summary: Exit 0; one file scanned; zero ERROR rows.
  target_ids:
  - CHEBI:62219
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/2-heptyl-4-quinolone.yaml --out /private/tmp/am-review-session/018-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Independent RDKit structure and internal identifier consistency
  status: failed
  required: false
  summary: RDKit rejects stored SMILES with a kekulization error. Stored InChI and
    scratch [nH] lactam parse and reproduce the recorded key, formula, charge and
    masses. Initial chemistry probe also exited 1 for the same parse failure.
  target_ids:
  - CHEBI:62219
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/018-chemistry-check.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: official-mol
  name: Independent official Molfile parsing
  status: passed
  required: false
  summary: Official Molfile parses to the [nH] lactam and recorded Standard InChIKey.
  target_ids:
  - CHEBI:62219
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/018-chebi-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - molfile
- check_id: imodulondb-datasets
  name: Structured source dataset discovery
  status: passed
  required: false
  summary: Pseudomonas precise364 and precise411 are exposed; dataset names are not
    proof of exact PA14 experimental equivalence.
  target_ids:
  - CHEBI:62219
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: imodulondb-pqsR364
  name: Exact regulator-name search in precise364
  status: passed
  required: false
  summary: Zero name hits; the alias search below resolves MvfR.
  target_ids:
  - CHEBI:62219
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 search --organism p_aeruginosa --dataset
    precise364 --query pqsR
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: imodulondb-pqsR411
  name: Exact regulator-name search in precise411
  status: passed
  required: false
  summary: Zero name hits; no biological absence inference.
  target_ids:
  - CHEBI:62219
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 search --organism p_aeruginosa --dataset
    precise411 --query pqsR
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: imodulondb-mvfR
  name: Regulator-alias search
  status: passed
  required: false
  summary: Found PA1003 and modules 85/MvfR and 15/LasR; only module 85 was selected
    for relevant context.
  target_ids:
  - CHEBI:62219
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 search --organism p_aeruginosa --dataset
    precise364 --query mvfR
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: imodulondb-summary
  name: Relevant MvfR module summary
  status: passed
  required: false
  summary: Seven module member genes in the pqs/phn region; computational expression
    context only.
  target_ids:
  - CHEBI:62219
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 summarize --organism p_aeruginosa --dataset
    precise364 --k 85
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: imodulondb-phenazine
  name: Additional pathway query
  status: failed
  required: false
  summary: Adapter failed because an iModulon regulator was null where a JSON list
    was expected. No pathway absence conclusion.
  target_ids:
  - CHEBI:62219
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 search --organism p_aeruginosa --dataset
    precise411 --query phenazine
  exit_code: 2
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:62219
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
  - CHEBI:62219
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
  - CHEBI:62219
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
  - CHEBI:62219
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
  - CHEBI:62219
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
  - CHEBI:62219
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
  - CHEBI:62219
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
  - CHEBI:62219
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
  - CHEBI:62219
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/2-heptyl-4-quinolone.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T07:05:04Z'
  support: supports
  summary: Read exact identity, structural definition, three aliases, parent, role,
    both chemical encodings, masses, registry, source concept and all three history
    events. No scientific evidence, mechanism, target, activity observation, resistance,
    producer, clinical, dataset or causal-graph object is asserted.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Complete CHEBI:62219 row at line 1079 and header; maintained tables
  accessed_at: '2026-10-21T07:05:04Z'
  support: supports
  summary: The 3-star in-scope row has the same SMILES, InChI, metadata and sole PMID:21965567
    lead; mechanism-role column is empty. No exact-ID/minted-ID decision or curator
    override matched the inclusive search.
- evidence_id: ownership
  kind: record_content
  reference: scripts/extract_source_inventory.py
  locator: ChEBI default-structure selection and row construction; scripts/seed_from_sources.py
    structure_from_chebi, mint and build_record; source config and MANIFEST
  accessed_at: '2026-10-21T07:05:04Z'
  support: supports
  summary: Extractor copies the default ChEBI SMILES and seeder copies that string
    to the record. Citation leads are not automatically claim evidence. Antibacterial
    mapping and source version reproduce the adopted inventory. Scientific additions
    and source-field repairs have distinct maintained owners.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:62219
  locator: Full entry, aliases, ontology, registry and structure fields
  accessed_at: '2026-10-21T07:05:04Z'
  support: supports
  summary: Official label, three aliases, definition, formula, charge, masses, InChI/key,
    Reaxys 1529939, parent and antibacterial role match. The current entry repeats
    the same unparseable SMILES. Other roles are outside the adopted antimicrobial
    subset.
- evidence_id: parent
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:23765
  locator: Official quinolone entry, outgoing and incoming edges
  accessed_at: '2026-10-21T07:05:04Z'
  support: supports
  summary: The broader quinolone class resolves and lists CHEBI:62219 as a child.
    It is not an exact identity cross-reference or an inference of fluoroquinolone
    topoisomerase action.
- evidence_id: role
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:33282
  locator: Definition and exact compound outgoing edge
  accessed_at: '2026-10-21T07:05:04Z'
  support: supports
  summary: The identifier denotes antibacterial agent, matching source classification.
- evidence_id: tautomer
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:75306
  locator: Full official lactim entry and reciprocal tautomer edge from CHEBI:62219
  accessed_at: '2026-10-21T07:05:04Z'
  support: supports
  summary: ChEBI distinguishes keto/lactam CHEBI:62219 from hydroxy/lactim CHEBI:75306
    while assigning identical mobile-H Standard InChI and key. Different tautomer-specific
    names/registry entries are preserved. Shared Standard InChI alone is not a duplicate
    determination.
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5 independent calculation
  locator: /private/tmp/am-review-session/018-chemistry-check.py; 018-structure.json;
    018-chemistry.log
  accessed_at: '2026-10-21T07:05:04Z'
  support: refutes
  summary: Stored CCCCCCCc1cc(=O)c2ccccc2n1 fails sanitization/kekulization. Stored
    InChI parses to CCCCCCCc1cc(=O)c2ccccc2[nH]1, reproducing UYRHHBXYXSYGHA-UHFFFAOYSA-N,
    C16H21NO, charge 0, masses 243.35/243.162314292, one fragment, no stereocenters
    and minted antibioticmech:chebi-a9be2766fb. The scratch lactim also shares the
    mobile-H key.
  snapshot_sha256: da0b3c07becd6e98575cea295f25a0f9bf003a920de23ca1b13c22ea275fd618
- evidence_id: molfile
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/62219
  locator: Official Molfile; /private/tmp/am-review-session/018-chebi.mol; 018-chebi-chemistry.py
  accessed_at: '2026-10-21T07:05:04Z'
  support: supports
  summary: Official Molfile independently parses to CCCCCCCc1cc(=O)c2ccccc2[nH]1,
    formula C16H21NO and the stored key. This corroborates the intended lactam without
    substituting the lactim record.
  snapshot_sha256: fa658c74e71e3f1b1ef96eba294ac60f1bbfea5e405031d3a90957c00aa3455c
- evidence_id: drawing
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/structure/2779534/
  locator: Official SVG rendered locally as 018-chebi.png and visually inspected
  accessed_at: '2026-10-21T07:05:04Z'
  support: supports
  summary: The official structure explicitly depicts NH and the 4-carbonyl with a
    heptyl substituent at position 2.
  snapshot_sha256: c6db0c9c73e11274345080663c0615af82c38928921d4363109f0628a4f94f34
- evidence_id: fallback
  kind: record_content
  reference: src/antibioticmech/chemical_embedding.py
  locator: parse_structure, lines 191-220
  accessed_at: '2026-10-21T07:05:04Z'
  support: context_only
  summary: 'The embedding parser attempts SMILES then Standard InChI. The valid fallback
    bounds impact: this finding does not claim every downstream consumer fails.'
- evidence_id: primary2011
  kind: primary_source
  reference: PMID:21965567
  locator: DOI:10.1128/JB.05929-11; author-hosted full PDF https://www-spring.ch.cam.ac.uk/publications/pdf/2011_JB_6770.pdf;
    Methods, Table 3, Results and Discussion
  accessed_at: '2026-10-21T07:05:04Z'
  support: supports
  summary: Chemically synthesized HHQ at 0.5 µM represses swarming in specified P.
    aeruginosa PA14 mutants on arginine medium; PqsR and phenazine/PCA-dependent genetic
    relationships are investigated. The authors leave downstream steps unresolved.
    These signalling/phenotype experiments are not antibacterial MIC or direct lethal-target
    measurements.
  snapshot_sha256: 49d9696eb3fd270df47ce2ab5d3ff86e0ed97f70809f15de29a46f3325b4b3b9
- evidence_id: primary-activity
  kind: primary_source
  reference: PMID:21539583
  locator: PubMed abstract; DOI:10.1111/j.1574-6941.2011.01121.x
  accessed_at: '2026-10-21T07:05:04Z'
  support: supports
  summary: The abstract names HHQ as 2-heptyl-4-quinolone and reports bacteriostatic
    activity including V. vulnificus, alongside separate motility and biofilm effects.
    It supports antibacterial activity without supplying a compound-wide direct target.
- evidence_id: primary2020
  kind: primary_source
  reference: DOI:10.1099/mic.0.000876
  locator: Publisher abstract and author-uploaded full text https://www.researchgate.net/publication/338083972_A_structure-function_analysis_of_interspecies_antagonism_by_the_2-heptyl-4-alkyl-quinolone_signal_molecule_from_Pseudomonas_aeruginosa;
    Methods, Results and Discussion
  accessed_at: '2026-10-21T07:05:04Z'
  support: supports
  summary: HHQ testing at 10 µM shows strain/medium-dependent growth inhibition and
    unaffected comparators, including V. parahaemolyticus RIMD 2210633. The authors
    explicitly leave its antibacterial mechanism unknown and distinguish this from
    antivirulence activity. HHQ is named using hydroxyquinoline terminology; no isolated-tautomer
    potency difference is established. Analogue/PQS/HQNO results must not transfer.
- evidence_id: adapter
  kind: database
  reference: iModulonDB public API via kg-microbe-sources
  locator: /private/tmp/am-review-session/018-imodulondb-datasets.json; pqsR364.txt;
    pqsR411.txt; mvfR364.txt; summary85.txt; phenazine411.err
  accessed_at: '2026-10-21T07:05:04Z'
  support: context_only
  summary: Exact pqsR queries returned no hits; mvfR resolves p_aeruginosa/precise364/PA1003
    and MvfR module p_aeruginosa/precise364/85. Summary has seven pqs/phn members.
    This is expression-module context, not binding, PA14 phenotype or antibacterial-mechanism
    proof. The precise411 phenazine query failed schema normalization on null regulator;
    no absence is inferred.
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: /private/tmp/am-review-session/018-validate.log; 018-strict.log; 018-strict.tsv
  accessed_at: '2026-10-21T07:05:04Z'
  support: supports
  summary: Both documented focused validators exited 0; strict scanned one file and
    returned zero ERROR rows. These gates do not refute the independent chemical parser
    failure.
- evidence_id: search
  kind: search
  reference: Inclusive local and bounded free source search
  locator: 018-local-hits.txt; 018-owner-search.txt; free exact-name/identifier/primary-title
    retrieval
  accessed_at: '2026-10-21T07:05:04Z'
  support: context_only
  summary: No maintained exact-ID/minted-ID override matched. Full official identity,
    author-hosted primary paper and author-uploaded primary text were inspected; unrelated
    congener results were kept separate.
  search_scope: prepare.py 18 used rg --no-ignore --hidden across the worktree for
    identifier, label and slug, including ignored/hidden content except .git and .venv.
    Maintained curator/decision tables were also searched for exact and minted identifiers.
    Free searches used exact quinolone name, Standard InChIKey, adopted PMID, swarming
    title and interspecies-antagonism title. Structured adapter discovery searched
    installed command and ignored-inclusive pyproject paths, locating the local CLAW
    runner. No paid access, author contact, or native mutation occurred.
assessments:
- assessment_id: identity
  area: identity
  topic: Intended lactam recoverable; SMILES malformed
  outcome: concern
  summary: Identity is unambiguous from label, InChI, official Molfile and drawing.
    The stored SMILES is an invalid chemical representation despite faithful source
    copying.
  target_ids:
  - CHEBI:62219
  evidence_ids:
  - record
  - chebi
  - chemistry
  - molfile
  - drawing
- assessment_id: grounding
  area: grounding
  topic: Parent and tautomer boundaries
  outcome: supported
  summary: Broader parent and antibacterial classification are source-backed. Preserve
    the separate ChEBI tautomer identity; Standard InChI equality does not authorize
    merging.
  target_ids:
  - CHEBI:62219
  evidence_ids:
  - chebi
  - parent
  - role
  - tautomer
  - chemistry
- assessment_id: activity
  area: evidence
  topic: Antibacterial versus behavioural effects
  outcome: supported
  summary: Primary sources independently support scoped HHQ antibacterial activity.
    Swarming suppression and growth inhibition are separate endpoints.
  target_ids:
  - CHEBI:62219
  evidence_ids:
  - primary2011
  - primary-activity
  - primary2020
- assessment_id: mechanism
  area: completeness
  topic: Unknown antibacterial mechanism
  outcome: unknown
  summary: Molecular mechanism remains unresolved. Neither expression context nor
    signalling genetics establishes the antibacterial target.
  target_ids:
  - CHEBI:62219
  evidence_ids:
  - primary2011
  - primary2020
  - adapter
- assessment_id: optional
  area: representation
  topic: Unasserted optional scientific objects
  outcome: not_applicable
  summary: Empty optional fields are not blanket errors. Assay and evidence enrichment
    is actionable but requires precise phenotype and form scope.
  target_ids:
  - CHEBI:62219
  evidence_ids:
  - record
  - primary2020
- assessment_id: provenance
  area: ownership
  topic: Source defect propagation and seed history
  outcome: supported
  summary: Three history events and mapped fields are consistent with generation.
    Repair must be reproducible from maintained source inputs/code; scientific additions
    belong to the actual record.
  target_ids:
  - CHEBI:62219
  evidence_ids:
  - record
  - inventory
  - ownership
- assessment_id: validation-assessment
  area: schema
  topic: Structural validation gap
  outcome: concern
  summary: Schema/strict pass while independent chemistry fails. Existing InChI fallback
    mitigates embedding impact but does not validate the stored SMILES.
  target_ids:
  - CHEBI:62219
  evidence_ids:
  - validation
  - chemistry
  - fallback
findings:
- finding_id: F1
  issue_key: chebi-62219-smiles-missing-quinolone-nh
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Source SMILES omits the lactam nitrogen hydrogen and cannot be parsed
  description: Stored and current ChEBI webpage SMILES CCCCCCCc1cc(=O)c2ccccc2n1 cannot
    be kekulized by RDKit. The same entry’s Molfile, SVG and stored InChI support
    CCCCCCCc1cc(=O)c2ccccc2[nH]1. This is a concrete structure-representation defect
    in an asserted field, not a missing optional enrichment or a tautomer-duplicate
    finding.
  target_ids:
  - CHEBI:62219
  field_paths:
  - chemical_structure.smiles
  evidence_ids:
  - record
  - inventory
  - ownership
  - chebi
  - chemistry
  - molfile
  - drawing
  - fallback
  rule_id: 'review-checklist: Identity and Chemical structure'
  native_severity: major unusable stored structure encoding
  normalization_reason: One chemical representation is invalid and can break SMILES-dependent
    consumers. Overall identity remains recoverable from valid independent encodings,
    so the finding is not normalized as a wrong-entity blocker.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained adopted structure row; repair through reproducible extraction
      rather than only the generated record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI structure extraction/normalization and provenance owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerates the seeded chemical structure from the maintained row
- finding_id: F2
  issue_key: chebi-62219-phenotype-specific-evidence-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Primary growth and signalling evidence needs separate claim-level treatment
  description: Specific primary sources can enrich this seed, while the antimicrobial
    target remains unresolved. Empty optional fields are not assigned a scientific
    error, and the scope of solution-phase HHQ experiments must be explicit.
  target_ids:
  - CHEBI:62219
  field_paths:
  - evidence
  - activity_spectrum
  - mode_of_action_notes
  evidence_ids:
  - record
  - primary2011
  - primary-activity
  - primary2020
  - adapter
  rule_id: 'review-checklist: Evidence standard and Mode of action'
  native_severity: informational evidence enrichment
  normalization_reason: Concrete follow-up is available, but current optional fields
    make no false claim.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-heptyl-4-quinolone.yaml
    role: Curator-owned claim-level evidence and assays through write_validated_antibiotic
      and curation event
actions:
- action_id: A1
  description: During separately authorized curation, correct the maintained extraction/structure
    representation using the official Molfile and provenance-backed normalization,
    regenerate the target, and retain the lactam identity. The validated scratch [nH]
    candidate provides a concrete repair to assess.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:62219
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained adopted structure row; repair through reproducible extraction
      rather than only the generated record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI structure extraction/normalization and provenance owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerates the seeded chemical structure from the maintained row
  acceptance_checks:
  - The stored SMILES sanitizes and agrees with the official lactam Molfile on formula,
    charge, connectivity and Standard InChIKey.
  - Preserve CHEBI:62219 and its tautomer-specific naming; do not merge CHEBI:75306
    solely because mobile-H keys match.
  - Rerun the documented source extraction/seeding path and just validate, just validate-strict,
    just verify-corpus --summary and just qc; inspect affected structure outputs.
- action_id: A2
  description: Curate primary HHQ growth observations separately from swarming or
    signalling findings, retain strain/media/dose and tested chemical-form context,
    and preserve an explicit unresolved antibacterial-mechanism rationale.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:62219
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-heptyl-4-quinolone.yaml
    role: Curator-owned claim-level evidence and assays through write_validated_antibiotic
      and curation event
  acceptance_checks:
  - Fixed-dose growth and swarm phenotypes are not converted into MICs or direct target-binding
    assertions.
  - Do not transfer PQS, HQNO, modified-analogue or expression-module effects to the
    parent antibacterial mechanism.
  - Use the validated writer and curation history, with focused validation and native
    promotion gates.
limitations:
- Independent Reaxys destination was not accessed; its asserted identifier was verified
  against official ChEBI.
- The 2011 interspecies paper was inspected at abstract level. The adopted swarming
  paper was inspected in author-hosted full text; the 2020 paper was inspected through
  author-uploaded full text after publisher full-text retrieval failed.
- The optional precise411 phenazine adapter query failed on a null regulator field.
  Successful alias/module retrieval remains contextual and is not exact PA14 experiment
  or antimicrobial target evidence.
- Bounded retrieval did not establish a direct HHQ antibacterial target; this is not
  an exhaustive literature-absence claim.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No record, source table or generated artifact was changed. Original input capture
  was retained; chemical_embedding.py was additionally hashed as reviewed implementation
  context.
- The initial chemistry probe and the robust follow-up both failed on stored SMILES;
  the independent official Molfile check passed. Scratch candidate structures were
  not applied.
- The author PDF Figure 2 was visually inspected for pathway context; the explicit
  chemical NH drawing was verified in the official ChEBI SVG, not inferred from that
  pathway figure.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:62219
- https://www-spring.ch.cam.ac.uk/publications/pdf/2011_JB_6770.pdf
- https://pubmed.ncbi.nlm.nih.gov/21539583/
- https://www.microbiologyresearch.org/content/journal/micro/10.1099/mic.0.000876
tags:
- record-review
- hhq
- smiles
- tautomer-boundary
```
