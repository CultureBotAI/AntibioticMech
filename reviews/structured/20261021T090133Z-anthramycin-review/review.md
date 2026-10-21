# Review of anthramycin

- Review: 20261021T090133Z-anthramycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:55:22Z
- Finished UTC: 2026-10-21T09:01:33Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Native anthramycin is internally consistent as the 11R,11aS hydroxy form. PDB CCD ANT instead encodes the 11S,11aS epimer and is associated with a covalent DNA adduct. The link requires explicit chemical scope rather than an arbitrary replacement of native stereochemistry. Primary microbial experiments offer bounded DNA,producer and growth-phase susceptibility annotations.

## Scope And Provenance

Whole exact SEEDED record,all ten adopted citation abstracts,current ChEBI classes/role,chemical and drug cross-references,free compound versus DNA-adduct stereochemistry,and primary microbial growth,uptake and biosynthetic context.

Selection: Path-ordered queue index 098;exactly one record prepared before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:40699 | data/antibiotics/antibacterial/anthramycin.yaml | generated | anthramycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record LinkML validation | passed | True | CHEBI:40699 | Exit 0;no issues found. |
| Documented closed-schema validation | passed | True | CHEBI:40699 | Exit 0;one file and zero ERROR rows. |
| Native structure and exact source comparison | failed | False | CHEBI:40699 | Exit 1 for the PDB stereochemical conflict. Native encodings,formula,mass,charge and mint pass; graph mapping localizes one epimeric center. KEGG drug graph omits both tetrahedral assignments. |
| Current ChEBI assertion comparison | passed | False | CHEBI:40699 | Exit 0;four parents,antibacterial role,synonyms,structure and mapping strings reproduce. |
| Authoritative full QC | failed | True | CHEBI:40699 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:40699 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:40699 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:40699 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:40699 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:40699 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:40699 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:40699 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:40699 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Free anthramycin versus PDB adduct context

identity: concern. Targets: CHEBI:40699.

Native exact form is consistent;ANT encodes another C11 epimer and its model is DNA linked. Preserve that distinction rather than reversing native chemistry.

### Chemical parents and antibacterial role

grounding: supported. Targets: CHEBI:40699.

Four broader classes fit. Primary bacterial growth evidence supports retaining antibacterial scope.

### DNA interaction without taxon-selectivity inflation

evidence: supported. Targets: CHEBI:40699.

Primary molecular and microbial evidence supports bounded DNA interaction. No bacterial-exclusive DNA binding or direct exonuclease target is established.

### Natural and engineered production

evidence: supported. Targets: CHEBI:40699.

Native natural-producer definition is supported;engineered 4F/S.lividans contexts must remain separate.

### Activity,resistance and mechanism enrichment

completeness: supported. Targets: CHEBI:40699.

Inspected primary experiments provide useful optional follow-up,without making empty optional fields a defect.

### Structured expression sources

scope: not_applicable. Targets: CHEBI:40699.

Native record has no gene,protein,locus,regulator,pathway or transcriptomics claim. Producer genus/name alone does not define an expression-module query.

### Generated source and status

ownership: supported. Targets: CHEBI:40699.

Four seed/reseed history events and native SEEDED status remain untouched.

### Native focused validation

schema: supported. Targets: CHEBI:40699.

Schema and strict checks pass;semantic mapping concern remains.

## Findings

### F1: PDB mapping conflates the native stereoisomer with an adduct-related component

major / open / confirmed; issue key: chebi-40699-anthramycin-pdb-ant-epimer-adduct-mapping.

Native free 11R,11aS hydroxy anthramycin and PDB ANT 11S,11aS are not exact stereochemical equivalents. ANT is meaningful DNA-adduct evidence,so the repair is to qualify that relationship instead of treating it as a replacement free-compound structure.

### F2: Primary experiments support bounded optional biological enrichment

informational / open / confirmed; issue key: chebi-40699-anthramycin-bounded-primary-enrichment.

DNA interaction,growth-phase susceptibility and natural/engineered production can be curated with their exact experimental scopes. No native false mechanism or required missing field is established.

## Recommended Actions And Acceptance Checks

### A1

Represent the PDB relationship with its stereochemical and covalent-adduct scope.

- Preserve the native 11R,11aS free hydroxy structure unless independent exact-form primary evidence warrants change. Do not use ANT bound-form context to invert it.
- Qualify or remove ANT from unqualified exact chemical mappings while retaining 274D/its primary paper as DNA-adduct evidence in an appropriate evidence/discussion field. No alternate CCD is nominated.
- Treat KEGG D02952 as a drug-level reference with unspecified tetrahedral centers;do not use its MOL as exact stereochemical replacement.
- Apply source inventory/extraction or maintained curation decisions,regenerate reproducibly,and run exact graph/source checks plus native schema,strict,term,reference,history and required corpus gates.

### A2

Optionally curate inspected primary biology with preserved assay and organism scope.

- Separate DNA adduction from direct protein targeting and from host antitumor endpoints. Substrate-lesion inhibition of exonuclease is not direct enzyme binding.
- Record growth phase and exposure conditions for producer self-protection;do not invent an MIC or an identified resistance gene. Keep the 1981 biosynthesis-location proposal explicitly hypothetical.
- Use natural-producer versus heterologous-host evidence types correctly;do not upgrade an unidentified Bacillus indicator to a species or treat HPLC-MS mass alone as complete stereochemical authentication.
- Use validated curation history and all native gates under separate curation authorization.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/anthramycin.yaml; Entire YAML and four seed/reseed events | supports | Native definition and IUPAC synonym explicitly specify11R,11aS and E side chain; chemistry agrees. It contains three chemical xrefs,one drug xref,one document link and no molecular target,activity observation,resistance or producer object. Natural-producer text is confined to the definition. |
| inventory | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; 098-chebi-row.json;098-inspect.json | supports | Generated identity and mappings reproduce the maintained ChEBI inventory. Exact-xref qualification belongs in source extraction/maintained decisions and regenerated output; curated primary evidence belongs in curator-owned evidence/discussions and biological fields. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:40699; 098-ols.json;098-chebi.html;098-parents.json | supports | Current nonobsolete term reproduces exact native structure,synonyms and definition. Pyrrolobenzodiazepine,primary amide,phenol and enamide parents fit; antibacterial role persists. |
| pdb-component | https://files.rcsb.org/ligands/download/ANT.cif; 098-pdb-ant.cif descriptors and systematic name;098-pdb-ant.json | refutes | CCD ANT defines a hydroxy compound with C11S,C11aS and VGQOVCHZGQWAOI-HYUHUPJXSA-N. Native C11 is R. This is the same constitution but a different specified epimer,so an unqualified exact chemical mapping does not reproduce the native form. |
| pdb-adduct | https://www.rcsb.org/structure/274D; 098-pdb274d.cif _struct_conn and _atom_site | context_only | The model associated with ANT is a covalent DNA complex:DG 9 N2 links to ANT C11. The actual ANT instance omits its leaving O11 atom. This is a reaction/adduct context,not a reason to change the free hemiaminal to the component dictionary epimer. |
| adduct-primary | PMID:7947769; DOI:10.1021/bi00250a011;PubMed full abstract and RCSB primary-citation abstract | context_only | Experimental crystallographic abstract reports C11S,C11aS in the covalent guanine-N2 adduct. It supports a structural mechanism link but does not establish the C11 configuration of free aqueous anthramycin. Full article was not read. |
| other-chemistry | https://rest.kegg.jp/get/D02952/mol; 098-kegg.mol;098-pubchem.json;098-metacyc.html | partial | KEGG drug accession matches formula and constitution/E side chain but specifies neither tetrahedral center. Supplemental PubChem 12306674 matches native exact key. MetaCyc returned an account page,not inspectable compound contents. CAS 4803-27-4 is corroborated,not independently registry-resolved. |
| microbial1981 | PMID:6895748; DOI:10.7164/antibiotics.34.1171;098-primary1981.pdf pp1171–1174;original p1172 image | supports | Growth/uptake experiments directly support bacterial activity and growth-phase-dependent self-protection. Early-log S.refuineus cells were inhibited at 100 µg/ml,whereas stationary cells resisted exposure and took up less labeled anthramycin. DNA from producer,C.perfringens and calf thymus bound drug in vitro. The authors proposed extracellular/periplasmic biosynthesis; that location was a hypothesis,not demonstrated localization. These exposure curves are not a standardized MIC. |
| biosynthesis2007 | PMID:17584616; DOI:10.1016/j.chembiol.2007.05.009;publisher Summary and indexed abstract | partial | Primary summary identifies S.refuineus subsp.thermotolerans as the natural producer and describes gene-replacement validation of a biosynthetic cluster. This supports the definition. Full body request failed HTTP403,so detailed strain and mutant experiments are not claimed as inspected. |
| heterologous2011 | PMID:22032628; DOI:10.1186/1471-2180-11-243;098-primary2011.xml anthramycin Results and Methods | partial | Engineered Streptomyces strain 4F carrying the introduced cluster produced an HPLC-MS-compatible compound at 47°C; a Bacillus-sp. bioassay was qualitative. This supports engineered production with analytical limits,not natural production by 4F,a precise indicator species or a purified-compound MIC. |
| leads | All ten adopted ChEBI PMID records; 098-core.json;098-lead-dispositions.json | context_only | Every indexed abstract was read. Radiolabel/NMR studies support DNA interaction; exonuclease blockade concerns damaged substrate rather than direct enzyme binding. Simulations are computational. Orf13 is biosynthetic,not an antimicrobial target; mouse CCK effects are host pharmacology; the PBD/ADC paper is a review. Heterologous hosts are distinguished from the natural producer. |
| chemistry | RDKit native and cross-reference comparison; 098-chemistry.py;098-chemistry.json | supports | Native two centers are S at atom 0 and R at atom 21; PDB comparison changes only atom 21 to S. Nonstereochemical normalized constitution agrees for all sources. KEGG is underassigned; native and supplemental PubChem exact keys agree. |
| source-check | Current ChEBI assertion comparison; 098-source-check.py;098-source-check.json | supports | All four parents,retained antibacterial role,chemical structure,synonyms and chemical/drug/document mapping strings pass. |
| validation | just validate;just validate-strict; Actual documented checks in batch010;098-strict.tsv | supports | Both commands exited 0;strict scanned one file with zero ERROR rows. |
| search | Ignored-inclusive native source and identity search; 098-local-hits.txt;098-inspect.json | context_only | One exact record and source owners resolved before assessment. All 13 captured inputs rechecked unchanged. All ten adopted citation abstracts were resolved and disposed individually. |

## Limits And Additional Notes

- All ten adopted abstracts were inspected;most original full papers were not. The 1981 microbial paper was read fully with its figure page,and relevant 2011 heterologous Methods/Results were inspected. The 2007 full body request failed HTTP403.
- The 1990 fullTextXML request failed HTTP500;an attempted PDF returned a browser-check HTML page despite HTTP200. It was recognized and excluded;only the indexed abstract supports its disposition.
- MetaCyc returned an account requirement,so its chemical contents were not verified. CAS is corroborated rather than independently checked in the CAS registry. KEGG does not assign native stereochemistry.
- PDB ANT and its parent DNA complex were inspected directly;the 1994 crystallographic paper was accessed at complete abstract scope. No claim is made that its full methods were read.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 13 captured input hashes rechecked unchanged;only scratch artifacts written.
- Two early scratch chemistry-comparison attempts stopped on representation-handling assertions:InChI parsing changes amide tautomer placement,and MOL bond geometry survived a simple stereo removal. The finalized comparison normalizes nonstereochemical encodings and maps the PDB canonical SMILES to native;its exit 1 represents the confirmed epimer mismatch,not those initial development errors.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T090133Z-anthramycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of anthramycin
started_at: '2026-10-21T08:55:22Z'
finished_at: '2026-10-21T09:01:33Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Native free-compound identity supported; major unqualified stereochemical/adduct
  mapping and optional primary enrichment
scientific_review: true
summary: Native anthramycin is internally consistent as the 11R,11aS hydroxy form.
  PDB CCD ANT instead encodes the 11S,11aS epimer and is associated with a covalent
  DNA adduct. The link requires explicit chemical scope rather than an arbitrary replacement
  of native stereochemistry. Primary microbial experiments offer bounded DNA,producer
  and growth-phase susceptibility annotations.
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
  - path: data/antibiotics/antibacterial/anthramycin.yaml
    sha256: 0da2aea8a256c31bf7be066f896ba5ca792c62d59219c61dee8621ea195d50c1
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
scope:
  description: Whole exact SEEDED record,all ten adopted citation abstracts,current
    ChEBI classes/role,chemical and drug cross-references,free compound versus DNA-adduct
    stereochemistry,and primary microbial growth,uptake and biosynthetic context.
  selection: Path-ordered queue index 098;exactly one record prepared before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:40699
targets:
- target_id: CHEBI:40699
  path: data/antibiotics/antibacterial/anthramycin.yaml
  label: anthramycin
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
  summary: Exit 0;no issues found.
  target_ids:
  - CHEBI:40699
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/anthramycin.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented closed-schema validation
  status: passed
  required: true
  summary: Exit 0;one file and zero ERROR rows.
  target_ids:
  - CHEBI:40699
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/anthramycin.yaml --out /private/tmp/am-review-session/098-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Native structure and exact source comparison
  status: failed
  required: false
  summary: Exit 1 for the PDB stereochemical conflict. Native encodings,formula,mass,charge
    and mint pass; graph mapping localizes one epimeric center. KEGG drug graph omits
    both tetrahedral assignments.
  target_ids:
  - CHEBI:40699
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/098-chemistry.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: source-check
  name: Current ChEBI assertion comparison
  status: passed
  required: false
  summary: Exit 0;four parents,antibacterial role,synonyms,structure and mapping strings
    reproduce.
  target_ids:
  - CHEBI:40699
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/098-source-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - source-check
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:40699
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
  - CHEBI:40699
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
  - CHEBI:40699
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
  - CHEBI:40699
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
  - CHEBI:40699
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
  - CHEBI:40699
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
  - CHEBI:40699
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
  - CHEBI:40699
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
  - CHEBI:40699
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/anthramycin.yaml
  locator: Entire YAML and four seed/reseed events
  accessed_at: '2026-10-21T08:58:47Z'
  support: supports
  summary: Native definition and IUPAC synonym explicitly specify11R,11aS and E side
    chain; chemistry agrees. It contains three chemical xrefs,one drug xref,one document
    link and no molecular target,activity observation,resistance or producer object.
    Natural-producer text is confined to the definition.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: 098-chebi-row.json;098-inspect.json
  accessed_at: '2026-10-21T08:58:47Z'
  support: supports
  summary: Generated identity and mappings reproduce the maintained ChEBI inventory.
    Exact-xref qualification belongs in source extraction/maintained decisions and
    regenerated output; curated primary evidence belongs in curator-owned evidence/discussions
    and biological fields.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:40699
  locator: 098-ols.json;098-chebi.html;098-parents.json
  accessed_at: '2026-10-21T08:58:47Z'
  support: supports
  summary: Current nonobsolete term reproduces exact native structure,synonyms and
    definition. Pyrrolobenzodiazepine,primary amide,phenol and enamide parents fit;
    antibacterial role persists.
  snapshot_sha256: efeee4dad4abe7d28d3fc87b19a728240eb528bca092107e466f6942f0361543
- evidence_id: pdb-component
  kind: database
  reference: https://files.rcsb.org/ligands/download/ANT.cif
  locator: 098-pdb-ant.cif descriptors and systematic name;098-pdb-ant.json
  accessed_at: '2026-10-21T08:58:47Z'
  support: refutes
  summary: CCD ANT defines a hydroxy compound with C11S,C11aS and VGQOVCHZGQWAOI-HYUHUPJXSA-N.
    Native C11 is R. This is the same constitution but a different specified epimer,so
    an unqualified exact chemical mapping does not reproduce the native form.
  snapshot_sha256: ac6dbf1f36c8228b682a871e82c0f49c5d4d7434549179e2088882c1ca36c386
- evidence_id: pdb-adduct
  kind: database
  reference: https://www.rcsb.org/structure/274D
  locator: 098-pdb274d.cif _struct_conn and _atom_site
  accessed_at: '2026-10-21T08:58:47Z'
  support: context_only
  summary: The model associated with ANT is a covalent DNA complex:DG 9 N2 links to
    ANT C11. The actual ANT instance omits its leaving O11 atom. This is a reaction/adduct
    context,not a reason to change the free hemiaminal to the component dictionary
    epimer.
  snapshot_sha256: d9e0e0b9c0934d8a0b1b632d9086766a544726b32defdddc062d9864ae99f009
- evidence_id: adduct-primary
  kind: primary_source
  reference: PMID:7947769
  locator: DOI:10.1021/bi00250a011;PubMed full abstract and RCSB primary-citation
    abstract
  accessed_at: '2026-10-21T08:58:47Z'
  support: context_only
  summary: Experimental crystallographic abstract reports C11S,C11aS in the covalent
    guanine-N2 adduct. It supports a structural mechanism link but does not establish
    the C11 configuration of free aqueous anthramycin. Full article was not read.
- evidence_id: other-chemistry
  kind: database
  reference: https://rest.kegg.jp/get/D02952/mol
  locator: 098-kegg.mol;098-pubchem.json;098-metacyc.html
  accessed_at: '2026-10-21T08:58:47Z'
  support: partial
  summary: KEGG drug accession matches formula and constitution/E side chain but specifies
    neither tetrahedral center. Supplemental PubChem 12306674 matches native exact
    key. MetaCyc returned an account page,not inspectable compound contents. CAS 4803-27-4
    is corroborated,not independently registry-resolved.
  snapshot_sha256: 11b8d678f6a020d9a2d048df8d2dadb60f8f92df13d2edd2bdca6ad6882a2c1e
- evidence_id: microbial1981
  kind: primary_source
  reference: PMID:6895748
  locator: DOI:10.7164/antibiotics.34.1171;098-primary1981.pdf pp1171–1174;original
    p1172 image
  accessed_at: '2026-10-21T08:58:47Z'
  support: supports
  summary: Growth/uptake experiments directly support bacterial activity and growth-phase-dependent
    self-protection. Early-log S.refuineus cells were inhibited at 100 µg/ml,whereas
    stationary cells resisted exposure and took up less labeled anthramycin. DNA from
    producer,C.perfringens and calf thymus bound drug in vitro. The authors proposed
    extracellular/periplasmic biosynthesis; that location was a hypothesis,not demonstrated
    localization. These exposure curves are not a standardized MIC.
  snapshot_sha256: 89febb26b96bfdf4ce1a06318d6e63f1e3f06310b4aad52feb8ddeaf8571b9a2
- evidence_id: biosynthesis2007
  kind: primary_source
  reference: PMID:17584616
  locator: DOI:10.1016/j.chembiol.2007.05.009;publisher Summary and indexed abstract
  accessed_at: '2026-10-21T08:58:47Z'
  support: partial
  summary: Primary summary identifies S.refuineus subsp.thermotolerans as the natural
    producer and describes gene-replacement validation of a biosynthetic cluster.
    This supports the definition. Full body request failed HTTP403,so detailed strain
    and mutant experiments are not claimed as inspected.
- evidence_id: heterologous2011
  kind: primary_source
  reference: PMID:22032628
  locator: DOI:10.1186/1471-2180-11-243;098-primary2011.xml anthramycin Results and
    Methods
  accessed_at: '2026-10-21T08:58:47Z'
  support: partial
  summary: Engineered Streptomyces strain 4F carrying the introduced cluster produced
    an HPLC-MS-compatible compound at 47°C; a Bacillus-sp. bioassay was qualitative.
    This supports engineered production with analytical limits,not natural production
    by 4F,a precise indicator species or a purified-compound MIC.
  snapshot_sha256: 92ad9b94b8d9c38ff16d1d65a43a09f5d5e55322a0a342ed840641277eab28f8
- evidence_id: leads
  kind: database
  reference: All ten adopted ChEBI PMID records
  locator: 098-core.json;098-lead-dispositions.json
  accessed_at: '2026-10-21T08:58:47Z'
  support: context_only
  summary: Every indexed abstract was read. Radiolabel/NMR studies support DNA interaction;
    exonuclease blockade concerns damaged substrate rather than direct enzyme binding.
    Simulations are computational. Orf13 is biosynthetic,not an antimicrobial target;
    mouse CCK effects are host pharmacology; the PBD/ADC paper is a review. Heterologous
    hosts are distinguished from the natural producer.
  snapshot_sha256: e3b5c78b08fdc953300fbbb95d3f06d6de6676bc7736907cb7cd04a087d74e69
- evidence_id: chemistry
  kind: validation
  reference: RDKit native and cross-reference comparison
  locator: 098-chemistry.py;098-chemistry.json
  accessed_at: '2026-10-21T08:58:47Z'
  support: supports
  summary: Native two centers are S at atom 0 and R at atom 21; PDB comparison changes
    only atom 21 to S. Nonstereochemical normalized constitution agrees for all sources.
    KEGG is underassigned; native and supplemental PubChem exact keys agree.
  snapshot_sha256: 06964e870b7816852083af7a02d2b4ecaa2bf901510580542032e47678f557c6
- evidence_id: source-check
  kind: validation
  reference: Current ChEBI assertion comparison
  locator: 098-source-check.py;098-source-check.json
  accessed_at: '2026-10-21T08:58:47Z'
  support: supports
  summary: All four parents,retained antibacterial role,chemical structure,synonyms
    and chemical/drug/document mapping strings pass.
  snapshot_sha256: b61f13fa938b410a0bba4fc38ec0ef4ff292b1733bc26b4e9c53a50f19a5717b
- evidence_id: validation
  kind: validation
  reference: just validate;just validate-strict
  locator: Actual documented checks in batch010;098-strict.tsv
  accessed_at: '2026-10-21T08:58:47Z'
  support: supports
  summary: Both commands exited 0;strict scanned one file with zero ERROR rows.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive native source and identity search
  locator: 098-local-hits.txt;098-inspect.json
  accessed_at: '2026-10-21T08:58:47Z'
  support: context_only
  summary: One exact record and source owners resolved before assessment. All 13 captured
    inputs rechecked unchanged. All ten adopted citation abstracts were resolved and
    disposed individually.
  search_scope: prepare.py 98 used rg --no-ignore --hidden excluding .git/.venv. Maintained
    source row and all native content were read before judgment. Any local absence
    finding is limited to this ignored-inclusive search scope.
assessments:
- assessment_id: identity
  area: identity
  topic: Free anthramycin versus PDB adduct context
  outcome: concern
  summary: Native exact form is consistent;ANT encodes another C11 epimer and its
    model is DNA linked. Preserve that distinction rather than reversing native chemistry.
  target_ids:
  - CHEBI:40699
  evidence_ids:
  - record
  - pdb-component
  - pdb-adduct
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Chemical parents and antibacterial role
  outcome: supported
  summary: Four broader classes fit. Primary bacterial growth evidence supports retaining
    antibacterial scope.
  target_ids:
  - CHEBI:40699
  evidence_ids:
  - chebi
  - source-check
  - microbial1981
- assessment_id: mechanism
  area: evidence
  topic: DNA interaction without taxon-selectivity inflation
  outcome: supported
  summary: Primary molecular and microbial evidence supports bounded DNA interaction.
    No bacterial-exclusive DNA binding or direct exonuclease target is established.
  target_ids:
  - CHEBI:40699
  evidence_ids:
  - leads
  - microbial1981
  - adduct-primary
- assessment_id: producer
  area: evidence
  topic: Natural and engineered production
  outcome: supported
  summary: Native natural-producer definition is supported;engineered 4F/S.lividans
    contexts must remain separate.
  target_ids:
  - CHEBI:40699
  evidence_ids:
  - biosynthesis2007
  - heterologous2011
  - leads
- assessment_id: optional
  area: completeness
  topic: Activity,resistance and mechanism enrichment
  outcome: supported
  summary: Inspected primary experiments provide useful optional follow-up,without
    making empty optional fields a defect.
  target_ids:
  - CHEBI:40699
  evidence_ids:
  - microbial1981
  - leads
- assessment_id: adapter
  area: scope
  topic: Structured expression sources
  outcome: not_applicable
  summary: Native record has no gene,protein,locus,regulator,pathway or transcriptomics
    claim. Producer genus/name alone does not define an expression-module query.
  target_ids:
  - CHEBI:40699
  evidence_ids:
  - record
- assessment_id: ownership
  area: ownership
  topic: Generated source and status
  outcome: supported
  summary: Four seed/reseed history events and native SEEDED status remain untouched.
  target_ids:
  - CHEBI:40699
  evidence_ids:
  - record
  - inventory
- assessment_id: schema
  area: schema
  topic: Native focused validation
  outcome: supported
  summary: Schema and strict checks pass;semantic mapping concern remains.
  target_ids:
  - CHEBI:40699
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: chebi-40699-anthramycin-pdb-ant-epimer-adduct-mapping
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: PDB mapping conflates the native stereoisomer with an adduct-related component
  description: Native free 11R,11aS hydroxy anthramycin and PDB ANT 11S,11aS are not
    exact stereochemical equivalents. ANT is meaningful DNA-adduct evidence,so the
    repair is to qualify that relationship instead of treating it as a replacement
    free-compound structure.
  target_ids:
  - CHEBI:40699
  field_paths:
  - xrefs
  - chemical_structure
  evidence_ids:
  - pdb-component
  - pdb-adduct
  - adduct-primary
  - chemistry
  rule_id: 'review-checklist: Structure and Equivalence; exact cross-references'
  native_severity: major exact-chemical mapping inconsistency
  normalization_reason: One specified epimer mismatch is confirmed,while native identity
    remains coherent. Bound-adduct evidence does not invalidate native free-compound
    chemistry.
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
  issue_key: chebi-40699-anthramycin-bounded-primary-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Primary experiments support bounded optional biological enrichment
  description: DNA interaction,growth-phase susceptibility and natural/engineered
    production can be curated with their exact experimental scopes. No native false
    mechanism or required missing field is established.
  target_ids:
  - CHEBI:40699
  field_paths:
  - mode_of_action_notes
  - molecular_targets
  - activity_spectrum
  - resistance_mechanisms
  - producer_organisms
  - evidence
  - discussions
  evidence_ids:
  - microbial1981
  - biosynthesis2007
  - heterologous2011
  - leads
  rule_id: 'review-checklist: claim-level biological evidence'
  native_severity: informational optional primary enrichment
  normalization_reason: Current native claims are restrained;optional unfilled biological
    fields alone do not require changes.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/anthramycin.yaml
    role: Curator-owned primary evidence,mechanism,activity,resistance,producer and
      discussions
actions:
- action_id: A1
  description: Represent the PDB relationship with its stereochemical and covalent-adduct
    scope.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:40699
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
  - Preserve the native 11R,11aS free hydroxy structure unless independent exact-form
    primary evidence warrants change. Do not use ANT bound-form context to invert
    it.
  - Qualify or remove ANT from unqualified exact chemical mappings while retaining
    274D/its primary paper as DNA-adduct evidence in an appropriate evidence/discussion
    field. No alternate CCD is nominated.
  - Treat KEGG D02952 as a drug-level reference with unspecified tetrahedral centers;do
    not use its MOL as exact stereochemical replacement.
  - Apply source inventory/extraction or maintained curation decisions,regenerate
    reproducibly,and run exact graph/source checks plus native schema,strict,term,reference,history
    and required corpus gates.
- action_id: A2
  description: Optionally curate inspected primary biology with preserved assay and
    organism scope.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:40699
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/anthramycin.yaml
    role: Curator-owned primary evidence,mechanism,activity,resistance,producer and
      discussions
  acceptance_checks:
  - Separate DNA adduction from direct protein targeting and from host antitumor endpoints.
    Substrate-lesion inhibition of exonuclease is not direct enzyme binding.
  - Record growth phase and exposure conditions for producer self-protection;do not
    invent an MIC or an identified resistance gene. Keep the 1981 biosynthesis-location
    proposal explicitly hypothetical.
  - Use natural-producer versus heterologous-host evidence types correctly;do not
    upgrade an unidentified Bacillus indicator to a species or treat HPLC-MS mass
    alone as complete stereochemical authentication.
  - Use validated curation history and all native gates under separate curation authorization.
limitations:
- All ten adopted abstracts were inspected;most original full papers were not. The
  1981 microbial paper was read fully with its figure page,and relevant 2011 heterologous
  Methods/Results were inspected. The 2007 full body request failed HTTP403.
- The 1990 fullTextXML request failed HTTP500;an attempted PDF returned a browser-check
  HTML page despite HTTP200. It was recognized and excluded;only the indexed abstract
  supports its disposition.
- MetaCyc returned an account requirement,so its chemical contents were not verified.
  CAS is corroborated rather than independently checked in the CAS registry. KEGG
  does not assign native stereochemistry.
- PDB ANT and its parent DNA complex were inspected directly;the 1994 crystallographic
  paper was accessed at complete abstract scope. No claim is made that its full methods
  were read.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 13 captured input hashes rechecked unchanged;only scratch artifacts written.
- Two early scratch chemistry-comparison attempts stopped on representation-handling
  assertions:InChI parsing changes amide tautomer placement,and MOL bond geometry
  survived a simple stereo removal. The finalized comparison normalizes nonstereochemical
  encodings and maps the PDB canonical SMILES to native;its exit 1 represents the
  confirmed epimer mismatch,not those initial development errors.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:40699
- https://www.rcsb.org/ligand/ANT
- https://www.rcsb.org/structure/274D
- https://doi.org/10.7164/antibiotics.34.1171
- https://doi.org/10.1016/j.chembiol.2007.05.009
tags:
- record-review
- anthramycin
- stereochemistry
- dna-adduct
- primary-evidence
```
