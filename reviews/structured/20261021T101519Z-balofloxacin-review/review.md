# Review of balofloxacin

- Review: 20261021T101519Z-balofloxacin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:40:26Z
- Finished UTC: 2026-10-21T10:15:19Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native graph is internally valid R-balofloxacin and reproduces ChEBI/KEGG. Its exact mappings include stereounspecified drug records, while FDA explicitly defines generic balofloxacin as racemic. The exact hydrate synonym also conflicts with the water-free graph. Primary antibacterial/gyrase and LamB phenotype evidence supports drug-context activity but does not resolve the enantiomer or hydrate of tested material.

## Scope And Provenance

Entire SEEDED record, four history events, ChEBI/ARO source ownership, nine adopted publication records including three LamB leads, current identity comparisons and selected original LamB Methods/Results.

Selection: Path-ordered queue index 147 prepared and hashed before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:34553 | data/antibiotics/antibacterial/balofloxacin.yaml | generated | Balofloxacin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema check | passed | True | CHEBI:34553 | Exit 0. |
| Documented strict check | passed | True | CHEBI:34553 | Exit 0; zero ERROR rows. |
| Native chemistry and bounded source comparison | passed | False | CHEBI:34553 | Exit 0; native internal consistency, mints and current ChEBI comparison pass. Script reports the conflicting source stereochemical scopes rather than treating unequal keys as exact matches. |
| Native catalog before web | passed | False | CHEBI:34553 | Exit 0; native catalog read before web source research. |
| Native gyrA context | passed | False | CHEBI:34553 | Exit 0; gene context and zero iModulons. |
| Native LamB context | passed | False | CHEBI:34553 | Exit 0; b4036 lamB and zero iModulons. |
| Authoritative full QC | failed | True | CHEBI:34553 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:34553 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:34553 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:34553 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:34553 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:34553 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:34553 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:34553 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:34553 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Stereoisomer and drug-form boundaries

identity: concern. Targets: CHEBI:34553.

The R graph is valid, but exact generic-drug xrefs and hydrate alias are not reconciled with explicit racemate/solvate evidence.

### Chemical family and antibacterial role

grounding: supported. Targets: CHEBI:34553.

Fluoroquinolone classification and drug-context antibacterial evidence agree; that does not resolve which stereochemical entity the record should denote.

### Gyrase and LamB source scopes

evidence: supported. Targets: CHEBI:34553.

The definition has primary drug-level support and LamB retains honest database provenance. Enantiomer-specific mechanism is not established.

### Sources, publication leads and history

provenance: supported. Targets: CHEBI:34553.

All adopted lead dispositions and the generated field owners were checked; history remains unchanged.

### Enrichment after identity resolution

completeness: unknown. Targets: CHEBI:34553.

Resolve exact identity before promoting drug-level potency or protein-target claims into an enantiomer-specific record.

### Focused deterministic gates

schema: supported. Targets: CHEBI:34553.

Schema, strict and chemistry/source observation checks pass. Scientific identity concerns remain.

## Findings

### F1: Reconcile the R-enantiomer record with generic balofloxacin mappings

major / open / confirmed; issue key: chebi-34553-balofloxacin-r-enantiomer-generic-drug-mapping.

The native structure specifies R configuration, as do ChEBI and KEGG. Exact PubChem and ChEMBL xrefs instead have no specified configuration, and the drug-context DrugCentral export likewise omits it. FDA explicitly defines generic balofloxacin as racemic and distinguishes its enantiomers. Consequently the merged generic-drug identity and its assays cannot be treated as proven exact R-enantiomer equivalence. The conflicting upstream records require an explicit owner decision, not automatic removal of chirality.

### F2: Stop presenting the hydrate as an exact synonym of the water-free structure

minor / open / confirmed; issue key: chebi-34553-balofloxacin-hydrate-exact-alias.

The generated EXACT_SYNONYM balofloxacin hydrate is incompatible with the native water-free formula. Official JAN identifies a dihydrate. The source uses a related synonym and the seeder promotes its generic SYNONYM category to EXACT_SYNONYM.

## Recommended Actions And Acceptance Checks

### A1

Resolve balofloxacin identity through maintained source harmonization before adding enantiomer-specific assays.

- Compare authoritative R, S, racemic and hydrated entities explicitly. Retaining the current R entity requires a correspondingly specific label/scope and defensible same-structure xrefs; generic drug associations must remain qualified. Do not infer racemate composition merely from an unspecified SMILES.
- Use the adopted ChEBI/ARO inventory and extractor/grounding decision path to implement the chosen resolution reproducibly. A racemate is not automatically one exact stereostructure; do not simply strip chirality and claim the identity issue solved.
- Recheck full InChIKeys and accepted source_concepts, synonyms and drug-context associations after a canary reseed. Resolve assay-material form before assigning drug-level primary assays to a single enantiomer.
- Retain LamB database provenance and the distinction between loss/downregulation, reduced growth inhibition, direct accumulation and clinical resistance. The available original paper measures direct accumulation only for chlortetracycline.
- Run required native gates and preserve validated curation history before any native sign-off.

### A2

Preserve the hydrate boundary in maintained synonym mapping.

- Remove or explicitly qualify the hydrate alias as a related drug-form name through the maintained inventory/transform; do not emit it as EXACT_SYNONYM for C20H24FN3O4.
- Check the source CAS and form associations together with F1. Do not replace the native formula with a hydrate formula unless the chosen chemical entity itself is changed through the proper source-owned path.
- Canary reseeding must preserve the chosen synonym scope and keep unrelated synonyms unchanged.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/balofloxacin.yaml; Whole YAML, source_concepts and four curation-history events | supports | An exact ChEBI record merges an ARO concept into a single R-configured, water-free structure. Antibacterial/gyrase wording has a primary reference. LamB is explicitly a database assertion; there are no structured MICs, causal graphs or molecular targets. |
| chemistry | Native structure and source concept mints; 147-chemistry.py;147-chemistry.json | supports | SMILES and InChI yield MGQLHRYJBWGORO-LLVKDONJSA-N, one R center, C20H24FN3O4, neutral charge and consistent masses. Both minted identifiers reproduce. Current ChEBI is nonobsolete, two-star, and agrees exactly with native structure and two chemical parents. |
| identity-sources | PubChem CID:65958;CHEMBL1210954;DrugCentral:283;KEGG:C13906; 147-pubchem.json;147-chembl.json;147-drugcentral-smiles.txt;147-kegg.mol | refutes | KEGG encodes the native R enantiomer. PubChem, ChEMBL and DrugCentral encode the same connectivity without specified chirality, key MGQLHRYJBWGORO-UHFFFAOYSA-N. Unspecified chirality alone does not prove a racemate, but it does not establish an exact R-enantiomer xref. |
| gsrs | FDA GSRS UNII:Q022B63JPM; https://api.fda.gov/other/substance.json?search=unii:Q022B63JPM&amp;limit=10;147-gsrs.json; structure, names and relationships | refutes | The retrieved API substance version 18 explicitly specifies RACEMIC, optical activity (+/-), zero defined centers of one, and separately relates R and S enantiomer substances and the dihydrate. This is substance identity evidence, not proof of US approval or the composition of an individual assay reagent. |
| hydrate | NIHS Japanese Accepted Names: Balofloxacin Hydrate; https://jpdb.nihs.go.jp/jan/DetailList_ja?submit=all_alp;147-jan.html; Balofloxacin Hydrate entry | refutes | The official entry specifies C20H24FN3O4·2H2O, mass 425.45 and CAS127294-70-6. It contradicts exact equivalence of the hydrate name with the native water-free formula. The shared CAS is a drug-form boundary requiring reconciliation, not proof that every use of that CAS means the native R form. |
| gyrase | PMID:1329626; DOI:10.1128/AAC.36.8.1708;147-core.json; complete indexed abstract | partial | Q-35 activity and supercoiling assays for S. aureus, E. coli and P. aeruginosa support the native drug-level definition. Full Methods and material stereochemistry were not retrieved, so these results do not prove isolated R-balofloxacin activity. |
| staphylococci | PMID:7492097; DOI:10.1128/AAC.39.7.1522;147-core.json; complete indexed abstract | partial | The selected resistant-staphylococcal strains and gyrA context support a bounded bactericidal comparison. These results do not imply universal susceptibility or an enantiomer-specific target interaction. |
| lamb-primary | PMID:24412198; DOI:10.1016/j.jprot.2013.12.024;147-lamb.pdf; Methods2.1/2.5, Results3.2/3.3/3.6, Table2 | partial | E. coli BW25113 deletion experiments show improved growth of the lamB mutant under balofloxacin. The BLFX reagent is identified by supplier, without form or stereochemistry. Direct accumulation measurements use chlortetracycline, not balofloxacin. The study supports a drug-context reduced-permeability interpretation but does not directly measure BLFX influx or establish a clinical resistance breakpoint. |
| aro-cache | ARO:3004126; 147-aro-lamb-stanza.txt;original cache /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/downloads/aro.obo | context_only | The cached ontology describes LamB absence/downregulation as resistance-associated and lists three publication leads. Its ancestry includes a gene-conferring-resistance-via-absence concept. The native reduced-permeability type is database-scoped; ordinary LamB presence should not be rewritten as the causal resistant state. |
| leads | Nine adopted publication records and one supplemental pharmacokinetic source; 147-core.json;147-lamb-core.json;147-lead-dispositions.json | context_only | Eight adopted records have complete indexed abstracts; the liver-injury bibliography has metadata only. All were inspected. The tetracycline LamB study is drug-distinct; the prophage-sequence study is not balofloxacin evidence. Hybrid/derivative activity remains distinct from the parent. The extra pharmacokinetic abstract explicitly concerns dihydrate. |
| owners | Source extraction and seeding owners; data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv;data/raw/aro_resistance_edges.tsv;scripts/seed_from_sources.py SYNONYM_TYPE/build_concepts | context_only | The ChEBI row supplies the R graph and hydrate SYNONYM; SYNONYM is emitted as EXACT_SYNONYM. The ARO row supplies generic-drug xrefs and definition. Current OLS calls the hydrate name a related synonym. Fixing only generated YAML would not correct these maintained inputs. |
| adapter | Native iModulonDB; 147-imodulondb-datasets.txt;147-imodulondb-gyra.txt;147-imodulondb-lamb.txt | context_only | Catalog and exact gene-context searches returned gyrase-related genes and lamB, with zero matching iModulons. No summary call applies and no expression association is used as target proof. |
| validation | Focused native schema and strict checks; 147-strict.tsv | supports | Both required focused validators passed. These gates do not adjudicate stereoisomer/racemate mappings. |
| search | Ignored-inclusive local ownership search; 147-local-hits.txt;147-inspect.json | context_only | All 16 captured repository inputs and the separately hashed external ARO cache remain unchanged. |

## Limits And Additional Notes

- The explicit R structure is internally consistent and agrees with ChEBI/KEGG, while other authorities differ. This review identifies a confirmed identity conflict but does not establish an automatically safe replacement identity.
- Eight of nine adopted publication records had complete abstracts; PMID15646539 had metadata only and its DOI access failed. The original1992/1995 and2022 full-text XML requests returned500; a direct1992 PMC page produced a browser challenge. No uninspected full Methods or SI are treated as read.
- The LamB original PDF was inspected for relevant Methods, Results and Table2, not every assay in the paper. Its supplier information does not establish enantiomeric or hydration form.
- FDA API version18 was inspected; a separately indexed FDA page exposed a newer version number, so the API snapshot is not mislabeled as that version. FDA substance identity is not approval evidence.
- NIHS JAN is a large official name list; its local fetched entry was read. DrugCentral’s first guessed SMILES endpoint returned404, while the actual drug endpoint succeeded.
- The native iModulonDB results are gene context only. No causal target inference follows from expression or membership.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 16 repository input hashes unchanged, plus external ARO cache hash rechecked separately. No native records edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T101519Z-balofloxacin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of balofloxacin
started_at: '2026-10-21T09:40:26Z'
finished_at: '2026-10-21T10:15:19Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Valid R-enantiomer graph conflicts with generic-drug and hydrate mappings
scientific_review: true
summary: The native graph is internally valid R-balofloxacin and reproduces ChEBI/KEGG.
  Its exact mappings include stereounspecified drug records, while FDA explicitly
  defines generic balofloxacin as racemic. The exact hydrate synonym also conflicts
  with the water-free graph. Primary antibacterial/gyrase and LamB phenotype evidence
  supports drug-context activity but does not resolve the enantiomer or hydrate of
  tested material.
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
  - path: data/antibiotics/antibacterial/balofloxacin.yaml
    sha256: 71be2cd53322bc7f853d901a5430f8c3c0d6579393528b4fda2fc654db914e97
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
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
scope:
  description: Entire SEEDED record, four history events, ChEBI/ARO source ownership,
    nine adopted publication records including three LamB leads, current identity
    comparisons and selected original LamB Methods/Results.
  selection: Path-ordered queue index 147 prepared and hashed before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:34553
targets:
- target_id: CHEBI:34553
  path: data/antibiotics/antibacterial/balofloxacin.yaml
  label: Balofloxacin
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
    role: Adopted ARO/PubChem source owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted ARO/PubChem source owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted ARO/PubChem source owner
checks:
- check_id: schema
  name: Documented schema check
  status: passed
  required: true
  summary: Exit 0.
  target_ids:
  - CHEBI:34553
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/balofloxacin.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict check
  status: passed
  required: true
  summary: Exit 0; zero ERROR rows.
  target_ids:
  - CHEBI:34553
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/balofloxacin.yaml --out /private/tmp/am-review-session/147-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Native chemistry and bounded source comparison
  status: passed
  required: false
  summary: Exit 0; native internal consistency, mints and current ChEBI comparison
    pass. Script reports the conflicting source stereochemical scopes rather than
    treating unequal keys as exact matches.
  target_ids:
  - CHEBI:34553
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/147-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
  - identity-sources
- check_id: adapter
  name: Native catalog before web
  status: passed
  required: false
  summary: Exit 0; native catalog read before web source research.
  target_ids:
  - CHEBI:34553
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-gyra
  name: Native gyrA context
  status: passed
  required: false
  summary: Exit 0; gene context and zero iModulons.
  target_ids:
  - CHEBI:34553
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset modulome --query gyrA
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-lamb
  name: Native LamB context
  status: passed
  required: false
  summary: Exit 0; b4036 lamB and zero iModulons.
  target_ids:
  - CHEBI:34553
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset modulome --query lamB
  exit_code: 0
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
  - CHEBI:34553
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
  - CHEBI:34553
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
  - CHEBI:34553
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
  - CHEBI:34553
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
  - CHEBI:34553
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
  - CHEBI:34553
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
  - CHEBI:34553
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
  - CHEBI:34553
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
  - CHEBI:34553
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/balofloxacin.yaml
  locator: Whole YAML, source_concepts and four curation-history events
  accessed_at: '2026-10-21T09:45:52Z'
  support: supports
  summary: An exact ChEBI record merges an ARO concept into a single R-configured,
    water-free structure. Antibacterial/gyrase wording has a primary reference. LamB
    is explicitly a database assertion; there are no structured MICs, causal graphs
    or molecular targets.
- evidence_id: chemistry
  kind: validation
  reference: Native structure and source concept mints
  locator: 147-chemistry.py;147-chemistry.json
  accessed_at: '2026-10-21T09:45:52Z'
  support: supports
  summary: SMILES and InChI yield MGQLHRYJBWGORO-LLVKDONJSA-N, one R center, C20H24FN3O4,
    neutral charge and consistent masses. Both minted identifiers reproduce. Current
    ChEBI is nonobsolete, two-star, and agrees exactly with native structure and two
    chemical parents.
  snapshot_sha256: 53707ac3313fe8fcd786dc3882dc13bdacbb4994ff22063e016b216a2c72f2d0
- evidence_id: identity-sources
  kind: database
  reference: PubChem CID:65958;CHEMBL1210954;DrugCentral:283;KEGG:C13906
  locator: 147-pubchem.json;147-chembl.json;147-drugcentral-smiles.txt;147-kegg.mol
  accessed_at: '2026-10-21T09:45:52Z'
  support: refutes
  summary: KEGG encodes the native R enantiomer. PubChem, ChEMBL and DrugCentral encode
    the same connectivity without specified chirality, key MGQLHRYJBWGORO-UHFFFAOYSA-N.
    Unspecified chirality alone does not prove a racemate, but it does not establish
    an exact R-enantiomer xref.
  snapshot_sha256: 53707ac3313fe8fcd786dc3882dc13bdacbb4994ff22063e016b216a2c72f2d0
- evidence_id: gsrs
  kind: database
  reference: FDA GSRS UNII:Q022B63JPM
  locator: https://api.fda.gov/other/substance.json?search=unii:Q022B63JPM&limit=10;147-gsrs.json;
    structure, names and relationships
  accessed_at: '2026-10-21T09:45:52Z'
  support: refutes
  summary: The retrieved API substance version 18 explicitly specifies RACEMIC, optical
    activity (+/-), zero defined centers of one, and separately relates R and S enantiomer
    substances and the dihydrate. This is substance identity evidence, not proof of
    US approval or the composition of an individual assay reagent.
  snapshot_sha256: de49be80da2bc4d2dda8024ce74803b917ecd4f0fb2473f4b46230e348eea45c
- evidence_id: hydrate
  kind: database
  reference: 'NIHS Japanese Accepted Names: Balofloxacin Hydrate'
  locator: https://jpdb.nihs.go.jp/jan/DetailList_ja?submit=all_alp;147-jan.html;
    Balofloxacin Hydrate entry
  accessed_at: '2026-10-21T09:45:52Z'
  support: refutes
  summary: The official entry specifies C20H24FN3O4·2H2O, mass 425.45 and CAS127294-70-6.
    It contradicts exact equivalence of the hydrate name with the native water-free
    formula. The shared CAS is a drug-form boundary requiring reconciliation, not
    proof that every use of that CAS means the native R form.
  snapshot_sha256: 45b34d21090fca484a52d6aacabe7321a86e81de47c07cba258fdfb010b81b2e
- evidence_id: gyrase
  kind: primary_source
  reference: PMID:1329626
  locator: DOI:10.1128/AAC.36.8.1708;147-core.json; complete indexed abstract
  accessed_at: '2026-10-21T09:45:52Z'
  support: partial
  summary: Q-35 activity and supercoiling assays for S. aureus, E. coli and P. aeruginosa
    support the native drug-level definition. Full Methods and material stereochemistry
    were not retrieved, so these results do not prove isolated R-balofloxacin activity.
- evidence_id: staphylococci
  kind: primary_source
  reference: PMID:7492097
  locator: DOI:10.1128/AAC.39.7.1522;147-core.json; complete indexed abstract
  accessed_at: '2026-10-21T09:45:52Z'
  support: partial
  summary: The selected resistant-staphylococcal strains and gyrA context support
    a bounded bactericidal comparison. These results do not imply universal susceptibility
    or an enantiomer-specific target interaction.
- evidence_id: lamb-primary
  kind: primary_source
  reference: PMID:24412198
  locator: DOI:10.1016/j.jprot.2013.12.024;147-lamb.pdf; Methods2.1/2.5, Results3.2/3.3/3.6,
    Table2
  accessed_at: '2026-10-21T09:45:52Z'
  support: partial
  summary: E. coli BW25113 deletion experiments show improved growth of the lamB mutant
    under balofloxacin. The BLFX reagent is identified by supplier, without form or
    stereochemistry. Direct accumulation measurements use chlortetracycline, not balofloxacin.
    The study supports a drug-context reduced-permeability interpretation but does
    not directly measure BLFX influx or establish a clinical resistance breakpoint.
  snapshot_sha256: f7a92903e1b1059ff1c96864ede7f4f2a2febd9233cb064c302f4cfe4d649121
- evidence_id: aro-cache
  kind: database
  reference: ARO:3004126
  locator: 147-aro-lamb-stanza.txt;original cache /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/downloads/aro.obo
  accessed_at: '2026-10-21T09:45:52Z'
  support: context_only
  summary: The cached ontology describes LamB absence/downregulation as resistance-associated
    and lists three publication leads. Its ancestry includes a gene-conferring-resistance-via-absence
    concept. The native reduced-permeability type is database-scoped; ordinary LamB
    presence should not be rewritten as the causal resistant state.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: leads
  kind: database
  reference: Nine adopted publication records and one supplemental pharmacokinetic
    source
  locator: 147-core.json;147-lamb-core.json;147-lead-dispositions.json
  accessed_at: '2026-10-21T09:45:52Z'
  support: context_only
  summary: Eight adopted records have complete indexed abstracts; the liver-injury
    bibliography has metadata only. All were inspected. The tetracycline LamB study
    is drug-distinct; the prophage-sequence study is not balofloxacin evidence. Hybrid/derivative
    activity remains distinct from the parent. The extra pharmacokinetic abstract
    explicitly concerns dihydrate.
  snapshot_sha256: 11bf104719c6709620fe13ad8bbd6d6b7aaafd0b1430e0845d5f4d10a872e9a9
- evidence_id: owners
  kind: record_content
  reference: Source extraction and seeding owners
  locator: data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv;data/raw/aro_resistance_edges.tsv;scripts/seed_from_sources.py
    SYNONYM_TYPE/build_concepts
  accessed_at: '2026-10-21T09:45:52Z'
  support: context_only
  summary: The ChEBI row supplies the R graph and hydrate SYNONYM; SYNONYM is emitted
    as EXACT_SYNONYM. The ARO row supplies generic-drug xrefs and definition. Current
    OLS calls the hydrate name a related synonym. Fixing only generated YAML would
    not correct these maintained inputs.
- evidence_id: adapter
  kind: database
  reference: Native iModulonDB
  locator: 147-imodulondb-datasets.txt;147-imodulondb-gyra.txt;147-imodulondb-lamb.txt
  accessed_at: '2026-10-21T09:45:52Z'
  support: context_only
  summary: Catalog and exact gene-context searches returned gyrase-related genes and
    lamB, with zero matching iModulons. No summary call applies and no expression
    association is used as target proof.
- evidence_id: validation
  kind: validation
  reference: Focused native schema and strict checks
  locator: 147-strict.tsv
  accessed_at: '2026-10-21T09:45:52Z'
  support: supports
  summary: Both required focused validators passed. These gates do not adjudicate
    stereoisomer/racemate mappings.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local ownership search
  locator: 147-local-hits.txt;147-inspect.json
  accessed_at: '2026-10-21T09:45:52Z'
  support: context_only
  summary: All 16 captured repository inputs and the separately hashed external ARO
    cache remain unchanged.
  search_scope: prepare.py 147 used rg --no-ignore --hidden excluding .git/.venv.
    Scope covers the exact native record, all adopted publication leads and bounded
    current identity/primary-mechanism follow-up; no exhaustive quinolone review.
assessments:
- assessment_id: identity
  area: identity
  topic: Stereoisomer and drug-form boundaries
  outcome: concern
  summary: The R graph is valid, but exact generic-drug xrefs and hydrate alias are
    not reconciled with explicit racemate/solvate evidence.
  target_ids:
  - CHEBI:34553
  evidence_ids:
  - chemistry
  - identity-sources
  - gsrs
  - hydrate
- assessment_id: grounding
  area: grounding
  topic: Chemical family and antibacterial role
  outcome: supported
  summary: Fluoroquinolone classification and drug-context antibacterial evidence
    agree; that does not resolve which stereochemical entity the record should denote.
  target_ids:
  - CHEBI:34553
  evidence_ids:
  - chemistry
  - gyrase
- assessment_id: mechanism
  area: evidence
  topic: Gyrase and LamB source scopes
  outcome: supported
  summary: The definition has primary drug-level support and LamB retains honest database
    provenance. Enantiomer-specific mechanism is not established.
  target_ids:
  - CHEBI:34553
  evidence_ids:
  - gyrase
  - staphylococci
  - lamb-primary
  - aro-cache
- assessment_id: provenance
  area: provenance
  topic: Sources, publication leads and history
  outcome: supported
  summary: All adopted lead dispositions and the generated field owners were checked;
    history remains unchanged.
  target_ids:
  - CHEBI:34553
  evidence_ids:
  - record
  - leads
  - owners
- assessment_id: completeness
  area: completeness
  topic: Enrichment after identity resolution
  outcome: unknown
  summary: Resolve exact identity before promoting drug-level potency or protein-target
    claims into an enantiomer-specific record.
  target_ids:
  - CHEBI:34553
  evidence_ids:
  - identity-sources
  - gsrs
  - gyrase
  - lamb-primary
- assessment_id: validation
  area: schema
  topic: Focused deterministic gates
  outcome: supported
  summary: Schema, strict and chemistry/source observation checks pass. Scientific
    identity concerns remain.
  target_ids:
  - CHEBI:34553
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-34553-balofloxacin-r-enantiomer-generic-drug-mapping
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile the R-enantiomer record with generic balofloxacin mappings
  description: The native structure specifies R configuration, as do ChEBI and KEGG.
    Exact PubChem and ChEMBL xrefs instead have no specified configuration, and the
    drug-context DrugCentral export likewise omits it. FDA explicitly defines generic
    balofloxacin as racemic and distinguishes its enantiomers. Consequently the merged
    generic-drug identity and its assays cannot be treated as proven exact R-enantiomer
    equivalence. The conflicting upstream records require an explicit owner decision,
    not automatic removal of chirality.
  target_ids:
  - CHEBI:34553
  field_paths:
  - grounding_status
  - chemical_structure
  - source_concepts
  - xrefs
  - drug_xrefs
  - definition
  - synonyms
  evidence_ids:
  - chemistry
  - identity-sources
  - gsrs
  - gyrase
  - owners
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
    role: Adopted ARO/PubChem source owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted ARO/PubChem source owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted ARO/PubChem source owner
  rule_id: 'CLAUDE.md: xrefs mean the same structure; stereoisomers are distinct'
  native_severity: major exact-identity harmonization conflict
  normalization_reason: The graph is valid and the conflict is located in source harmonization
    and exact scope. A defensible native replacement has not been established, so
    this is a major unresolved mapping defect rather than a proposed automatic graph
    replacement.
- finding_id: F2
  issue_key: chebi-34553-balofloxacin-hydrate-exact-alias
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Stop presenting the hydrate as an exact synonym of the water-free structure
  description: The generated EXACT_SYNONYM balofloxacin hydrate is incompatible with
    the native water-free formula. Official JAN identifies a dihydrate. The source
    uses a related synonym and the seeder promotes its generic SYNONYM category to
    EXACT_SYNONYM.
  target_ids:
  - CHEBI:34553
  field_paths:
  - synonyms
  evidence_ids:
  - record
  - hydrate
  - owners
  - gsrs
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
    role: Adopted ARO/PubChem source owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted ARO/PubChem source owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted ARO/PubChem source owner
  rule_id: 'CLAUDE.md: salts and distinct structures remain separate'
  native_severity: minor synonym scope correction
  normalization_reason: This finding isolates the bounded alias-scope error; the broader
    unresolved stereochemical identity conflict is tracked separately as F1.
actions:
- action_id: A1
  description: Resolve balofloxacin identity through maintained source harmonization
    before adding enantiomer-specific assays.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:34553
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
    role: Adopted ARO/PubChem source owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted ARO/PubChem source owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted ARO/PubChem source owner
  acceptance_checks:
  - Compare authoritative R, S, racemic and hydrated entities explicitly. Retaining
    the current R entity requires a correspondingly specific label/scope and defensible
    same-structure xrefs; generic drug associations must remain qualified. Do not
    infer racemate composition merely from an unspecified SMILES.
  - Use the adopted ChEBI/ARO inventory and extractor/grounding decision path to implement
    the chosen resolution reproducibly. A racemate is not automatically one exact
    stereostructure; do not simply strip chirality and claim the identity issue solved.
  - Recheck full InChIKeys and accepted source_concepts, synonyms and drug-context
    associations after a canary reseed. Resolve assay-material form before assigning
    drug-level primary assays to a single enantiomer.
  - Retain LamB database provenance and the distinction between loss/downregulation,
    reduced growth inhibition, direct accumulation and clinical resistance. The available
    original paper measures direct accumulation only for chlortetracycline.
  - Run required native gates and preserve validated curation history before any native
    sign-off.
- action_id: A2
  description: Preserve the hydrate boundary in maintained synonym mapping.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:34553
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
    role: Adopted ARO/PubChem source owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted ARO/PubChem source owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted ARO/PubChem source owner
  acceptance_checks:
  - Remove or explicitly qualify the hydrate alias as a related drug-form name through
    the maintained inventory/transform; do not emit it as EXACT_SYNONYM for C20H24FN3O4.
  - Check the source CAS and form associations together with F1. Do not replace the
    native formula with a hydrate formula unless the chosen chemical entity itself
    is changed through the proper source-owned path.
  - Canary reseeding must preserve the chosen synonym scope and keep unrelated synonyms
    unchanged.
limitations:
- The explicit R structure is internally consistent and agrees with ChEBI/KEGG, while
  other authorities differ. This review identifies a confirmed identity conflict but
  does not establish an automatically safe replacement identity.
- Eight of nine adopted publication records had complete abstracts; PMID15646539 had
  metadata only and its DOI access failed. The original1992/1995 and2022 full-text
  XML requests returned500; a direct1992 PMC page produced a browser challenge. No
  uninspected full Methods or SI are treated as read.
- The LamB original PDF was inspected for relevant Methods, Results and Table2, not
  every assay in the paper. Its supplier information does not establish enantiomeric
  or hydration form.
- FDA API version18 was inspected; a separately indexed FDA page exposed a newer version
  number, so the API snapshot is not mislabeled as that version. FDA substance identity
  is not approval evidence.
- NIHS JAN is a large official name list; its local fetched entry was read. DrugCentral’s
  first guessed SMILES endpoint returned404, while the actual drug endpoint succeeded.
- The native iModulonDB results are gene context only. No causal target inference
  follows from expression or membership.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 16 repository input hashes unchanged, plus external ARO cache hash rechecked
  separately. No native records edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:34553
- https://precision.fda.gov/ginas/app/ui/substances/4c9248c6-5658-44a3-92c7-9f4c8e5259c1
- https://doi.org/10.1128/AAC.36.8.1708
- https://doi.org/10.1016/j.jprot.2013.12.024
tags:
- record-review
- balofloxacin
- stereochemical-identity
- hydrate-boundary
```
