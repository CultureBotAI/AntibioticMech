# Carbapenem MM22383: exact identity supported; qualify historical activity and enzyme evidence

- Review: 20261021T104618Z-carbapenem-mm22383
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:32:39Z
- Finished UTC: 2026-10-21T10:46:18Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The exact neutral MM22383 structure is internally coherent and agrees with official ChEBI, PubChem and KEGG structures. Original primary studies support antibacterial activity and cell-free beta-lactamase inhibition, with assay material and stereochemical qualifications. No confirmed native error was found. One informational enrichment action distinguishes those observations and culture production from clinical use, generalized PBP binding and the adopted allergenicity citation. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole CHEBI58998 record: definition, three exact synonyms, two parents, three activity roles, full structure and masses, three xrefs, source mint and complete history. The sole adopted citation was inspected as a full abstract; three additional original primary papers were read in full main text.

Selection: Queue 195; preserved initial capture and exact native path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:58998 | data/antibiotics/antibacterial/carbapenem-mm22383.yaml | generated | carbapenem MM22383 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:58998 | Actual focused command exited 0. |
| strict | passed | True | CHEBI:58998 | Actual focused command exited 0. |
| chemistry | passed | False | CHEBI:58998 | Actual focused command exited 0. The batch020 environment lacks RDKit; the existing batch019 interpreter was used with batch020 as the working directory. Both strings reproduce the key, formula, charge, masses and source mint. |
| Authoritative full QC | failed | True | CHEBI:58998 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:58998 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:58998 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:58998 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:58998 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:58998 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:58998 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:58998 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:58998 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral structure and systematic names

identity: supported. Targets: CHEBI:58998.

Both strings, official structures and the original structure assignment agree. Sodium assay material, ester crystallography and absolute-assignment assumptions remain explicit.

### Parents, roles and registry references

grounding: supported. Targets: CHEBI:58998.

Parent classes and antimicrobial roles are structurally/source concordant; primary experiments independently support antibacterial inclusion. The antibacterial-drug role is ChEBI-attested, while an exact clinical-use claim was not independently established.

### Sole adopted citation disposition

evidence: supported. Targets: CHEBI:58998.

PMID3338858 supports allergenicity context only. It is correctly not automatically promoted into antimicrobial claim-level evidence.

### Historical exact-material antibacterial observations

evidence: supported. Targets: CHEBI:58998.

The original individual-strain and later clinical-panel experiments support antibacterial activity, with method, salt material and statistic boundaries retained.

### Cell-free enzyme inhibition versus antibacterial mechanism

completeness: supported. Targets: CHEBI:58998.

There is direct inhibition evidence for named beta-lactamase preparations. That does not identify a sequence-specific protein accession, establish all PBP targets or prove a complete bacterial killing chain. No native target claim is currently wrong.

### Natural production versus biosynthetic pathway

provenance: supported. Targets: CHEBI:58998.

Culture fermentation and purification support S. olivaceus ATCC31365 as a producer in the reported conditions. The paper explicitly leaves trans-olivanic-acid pathway relationships unresolved; no gene-cluster assignment is inferred.

### Optional primary evidence enrichment

completeness: supported. Targets: CHEBI:58998.

Activity, producer and bounded enzyme observations are available for future curation. Their missing optional fields are an informational opportunity rather than a required-field defect.

### Maintained source and future curated additions

ownership: supported. Targets: CHEBI:58998.

Source identity remains owned by the adopted ChEBI row/extractor/seeder. Future claim-level additions belong to the actual native record through validated curation entrypoints. Initial captures remain intact.

### Focused validity and history

schema: supported. Targets: CHEBI:58998.

The complete record and history were read; documented per-record validation and internal chemistry passed.

## Findings

### F1: Add exact primary observations with salt, assay and enzyme-preparation scope

informational / open / confirmed; issue key: mm22383-qualified-primary-evidence-enrichment.

The seed has sound identity and antibacterial inclusion but no claim-level primary observations. Original papers provide activity, culture production and cell-free beta-lactamase inhibition. The adopted allergenicity paper cannot supply those claims. Optional enrichment should preserve individual-strain versus median-panel MICs and avoid inferring clinical use or PBP binding.

## Recommended Actions And Acceptance Checks

### A1

Curate the original MM22383 observations without transferring neighboring compound or clinical claims.

- Attach the original structure and production/activity papers at the claims they support. Distinguish acid10, sodium salt14 and ester18 and resolve the tested material representation before assigning numerical observations to the neutral record.
- For 1979 Table3 preserve individual strain, nutrient-broth assay and reported MIC units. For 1980 Table1 preserve that each value is a median of ten isolates, the strict greater-than comparator, organism-dependent medium, incubation and no-growth endpoint. Do not silently convert medians to strain-level MICs or clinical breakpoints.
- If adding beta-lactamase inhibition, identify the exact cell-free preparation, substrate and reported I50 from 1979 Table4, and inspect its cited assay-method paper before supplying detailed kinetics or concentrations. Do not infer UniProt identity, PBP binding or mechanism of bacterial death from those preparations.
- Support producer_organisms with the reported pure-culture fermentation and purified product from S. olivaceus ATCC31365; independently resolve a strain/taxon accession before adding an ontology identifier. Do not infer a demonstrated trans-compound biosynthetic gene cluster.
- Keep PMID3338858 confined to its allergenicity scope. Treat the ChEBI antibacterial-drug role as source-attested until exact therapeutic-use evidence is inspected; do not add approval, clinical efficacy or safety claims from in vitro activity alone.
- Use write_validated_antibiotic and record_curation_event for separately authorized curation of data/antibiotics/antibacterial/carbapenem-mm22383.yaml, preserve additions through reseeding, and run applicable focused/shared checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/carbapenem-mm22383.yaml; Complete native record, all fields and three history entries. | supports | SEEDED/EXACT record of the neutral acid. No molecular target, mechanism, producer, activity observation, resistance claim or causal graph is asserted. Their absence alone is not an error. |
| source | data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact source row 1016; ChEBI quality/role policy, extractor lines 264–336 and seeder structure/concept import. | supports | Native identity, names, parents, roles and xrefs reproduce the maintained row. The only adopted citation lead is PMID3338858; extraction deliberately retains citation leads outside claim-level record evidence. Hidden-and-ignored-inclusive searches found no exact corrective curator/decision entry. All 13 initial input hashes remain unchanged. |
| official | https://www.ebi.ac.uk/chebi/CHEBI:58998; Complete official entry, including structure, ontology and registry references. | supports | ChEBI agrees with C13H16N2O5S, charge zero, key PRPNUZWHFGSGRV-RZFSBTTISA-N, average mass 312.347 and monoisotopic mass 312.07799. CHEBI46634 is carbapenemcarboxylic acid; CHEBI79020 is alpha,beta-unsaturated monocarboxylic acid. CHEBI33281, CHEBI33282 and CHEBI36047 denote antimicrobial agent, antibacterial agent and antibacterial drug. Exact systematic synonyms encode the same stereochemistry and E-vinyl side chain. CAS65322-98-7 and Beilstein497581 are source-attested; the subscription Beilstein registry was not independently inspected. |
| xref | https://rest.kegg.jp/get/C17398; https://rest.kegg.jp/get/C17398/mol; https://pubchem.ncbi.nlm.nih.gov/compound/22824517; Full KEGG entry and molfile; official PubChem property response. | supports | KEGG C17398 names MM22383 and epithienamycin D and cross-references ChEBI58998 and CAS65322-98-7. Independent parsing of its molfile reproduces the full native key and all three stereocentres. PubChem CID22824517 likewise matches the native InChI/key. The KEGG PubChem accession is a substance reference and is not treated as a mismatched compound CID. |
| chemistry | 195-chemistry.json; 195-kegg-chemistry.json; Independent native SMILES/InChI parsing, computed properties, exact source mint and KEGG structure comparison. | supports | Both native strings are valid one-fragment neutral structures with matching formula, key, masses, stereochemistry and source mint antibioticmech:chebi-76365d348b. There is no identity conflict among these inspected official structures. |
| adopted | PMID:3338858; DOI:10.1159/000234500; Complete indexed abstract; publisher full text unavailable with HTTP403. | context_only | The paper concerns MM22383 immunogenicity/allergenicity in guinea pigs and rabbits and occupational allergy implications. Hapten-protein conjugation is not bacterial PBP binding. This citation does not supply antibacterial potency, bacterial target identity or clinical efficacy evidence. |
| structure1979 | PMID:511786; DOI:10.7164/antibiotics.32.961; Complete original main text; original p961 structure drawings visually inspected. | supports | MM22383 is acid10, with sodium salt14 and p-nitrobenzyl ester18 distinguished. Spectroscopy establishes the E-vinyl group and trans beta-lactam relation. The ester crystallography establishes the relative hydroxyethyl configuration; the absolute C5R assignment is explicitly assumed from known natural beta-lactams. This supports the current literature designation without claiming an independent absolute X-ray determination. |
| production1979 | PMID:317283; DOI:10.7164/antibiotics.32.1239; Entire original paper; p1244 Tables3 and4 visually inspected. | supports | S. olivaceus ATCC31365 fermentation yielded chromatographically purified MM22383 sodium salt. Table3 reports nutrient-broth microtitre MICs including 8 micrograms/mL for E. coli O111 and S. aureus Oxford, 125 for P. aeruginosa A. Table4 reports cell-free beta-lactamase I50 values: E. cloacae P99 0.04, P. aeruginosa A 4.0, P. mirabilis C889 0.4, E. coli JT4 0.1 and S. aureus Russell &gt;2.0 micrograms/mL, with cephaloridine or benzylpenicillin substrate as specified. The method is delegated to Reading/Hepburn. Trans-compound biosynthetic relationships remained unresolved. |
| activity1980 | PMID:6968745; DOI:10.7164/antibiotics.33.878; Complete main text; original Table1 p880 visually inspected. | supports | Each Table1 value is a median MIC among ten clinical isolates, not a single-strain observation. MM22383 medians include 12.5 micrograms/mL for E. coli, 6.2 for susceptible/penicillin-resistant S. aureus, 100 for methicillin-resistant S. aureus and &gt;100 for P. aeruginosa. Broth dilution uses organism-dependent medium and no-visible-growth endpoint, 18 hours for aerobes and 24 hours for anaerobes at 37 degrees C. Combination results concern amoxicillin plus a fixed subinhibitory olivanic-acid concentration; they are not standalone MM22383 MICs. No direct PBP assay or clinical treatment demonstration is supplied. |
| adapter | Structured-source applicability assessed from complete native record before web research; No native gene, protein, locus, pathway, regulator, response or transcriptomic dataset. | context_only | No record assertion required an iModulonDB query. Newly encountered production and cell-free enzyme evidence does not turn expression-module absence into negative evidence or justify a sequence-specific target accession. |
| search | 195-maintained-search.txt; 195-inclusive-file-hits.txt; Exact identifier, name variants, slug and full-key stem; hidden and ignored files included. | context_only | Searches found the native and raw rows, path ledger, readiness queue and generated maps. No separate maintained correction or exact curated primary-evidence object was found within that scope. Generated maps and historical leads were not scientific evidence. |
| validation | 195-focused-results.json; 195-schema.log; 195-strict.log; Actual documented focused validators and independent chemistry. | supports | Schema, strict and chemistry checks all exit0. These passes establish deterministic consistency, not clinical use or primary scientific sign-off. |

## Limits And Additional Notes

- All 13 initial source inputs were captured before assessment and remain unchanged. Complete native record, source row, relevant configuration and source transforms were read.
- The adopted 1988 allergenicity paper was available as a complete indexed abstract only; the publisher returned HTTP403. The original 1979 structure/production papers and 1980 antibacterial paper were inspected in full main text, with the pertinent original structure drawing and Tables3/4 and Table1 visually checked.
- Absolute C5R in the original crystallographic structure paper is explicitly assumed from known natural beta-lactams. This review did not independently redetermine absolute configuration; current official structures agree with that literature assignment.
- Original isolation used sodium salts. The neutral-acid record is chemically coherent, but future quantitative observations must retain assay-material form and cannot silently imply that all experiments used the isolated free acid.
- The 1980 inoculum wording does not unambiguously identify the final well inoculum; no unreported final concentration is supplied. The 1979 Table3 footnote visibly specifies approximately10^6 cells/mL. Historical organism names require careful taxonomic resolution before adding modern accessions.
- The beta-lactamase method paper cited by the production study was not independently read. Therefore the review reports its Table4 I50 values and enzyme-preparation/substrate scope without reconstructing missing kinetic details.
- Beilstein497581 was verified as the ChEBI source xref, not by subscription-registry inspection. Clinical therapeutic use, approval and a complete PBP/causal mechanism were not established in this bounded review.
- A later derivative-synthesis paper was located and downloaded but not used as full-text evidence; its reported C8 inversion concerns a synthetic derivative route and does not independently contradict the native MM22383 structure.
- Chemistry used the existing batch019 RDKit interpreter because the batch020 locked environment lacks RDKit; its actual command and working-tree inputs are recorded. No native expression claim required a structured transcriptomics query.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T104618Z-carbapenem-mm22383
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Carbapenem MM22383: exact identity supported; qualify historical activity
  and enzyme evidence'
started_at: '2026-10-21T10:32:39Z'
finished_at: '2026-10-21T10:46:18Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the native seed. Inspected the complete record,
    exact maintained source and source transforms, independently parsed both native
    strings and the KEGG molfile, and read the original structure, production and
    antibacterial papers.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The exact neutral MM22383 structure is internally coherent and agrees with
  official ChEBI, PubChem and KEGG structures. Original primary studies support antibacterial
  activity and cell-free beta-lactamase inhibition, with assay material and stereochemical
  qualifications. No confirmed native error was found. One informational enrichment
  action distinguishes those observations and culture production from clinical use,
  generalized PBP binding and the adopted allergenicity citation. Scientific assessment
  retains the stated evidence limits; full verification is blocked by the shared native-library
  failure.
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
  - path: data/antibiotics/antibacterial/carbapenem-mm22383.yaml
    sha256: 3c0b85acfcb1a1443e9f529cad99e63b77d48c3da6d8c7585ade8fe101ae217f
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
- target_id: CHEBI:58998
  path: data/antibiotics/antibacterial/carbapenem-mm22383.yaml
  label: carbapenem MM22383
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
  description: 'Whole CHEBI58998 record: definition, three exact synonyms, two parents,
    three activity roles, full structure and masses, three xrefs, source mint and
    complete history. The sole adopted citation was inspected as a full abstract;
    three additional original primary papers were read in full main text.'
  selection: Queue 195; preserved initial capture and exact native path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:58998
  exclusions:
  - target: Other olivanic acids, thienamycin, C8-inverted or side-chain derivatives
      and sodium salts as structure-identical records
    reason: These differ in stereochemistry, substituents or material form; their
      results require explicit attribution.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:58998
  evidence_ids:
  - validation
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/carbapenem-mm22383.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:58998
  evidence_ids:
  - validation
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/carbapenem-mm22383.yaml --out /private/tmp/am-review-session/195-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Actual focused command exited 0. The batch020 environment lacks RDKit;
    the existing batch019 interpreter was used with batch020 as the working directory.
    Both strings reproduce the key, formula, charge, masses and source mint.
  target_ids:
  - CHEBI:58998
  evidence_ids:
  - validation
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 195
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
  - CHEBI:58998
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
  - CHEBI:58998
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
  - CHEBI:58998
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
  - CHEBI:58998
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
  - CHEBI:58998
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
  - CHEBI:58998
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
  - CHEBI:58998
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
  - CHEBI:58998
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
  - CHEBI:58998
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/carbapenem-mm22383.yaml
  locator: Complete native record, all fields and three history entries.
  accessed_at: '2026-10-21T10:40:19Z'
  support: supports
  summary: SEEDED/EXACT record of the neutral acid. No molecular target, mechanism,
    producer, activity observation, resistance claim or causal graph is asserted.
    Their absence alone is not an error.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Exact source row 1016; ChEBI quality/role policy, extractor lines 264–336
    and seeder structure/concept import.
  accessed_at: '2026-10-21T10:40:19Z'
  support: supports
  summary: Native identity, names, parents, roles and xrefs reproduce the maintained
    row. The only adopted citation lead is PMID3338858; extraction deliberately retains
    citation leads outside claim-level record evidence. Hidden-and-ignored-inclusive
    searches found no exact corrective curator/decision entry. All 13 initial input
    hashes remain unchanged.
  snapshot_sha256: c9e67c270b673ce0b09011a695bc58c4d8fee39c3c97906cfe5ea1d3b0134f43
- evidence_id: official
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:58998
  locator: Complete official entry, including structure, ontology and registry references.
  accessed_at: '2026-10-21T10:40:19Z'
  support: supports
  summary: ChEBI agrees with C13H16N2O5S, charge zero, key PRPNUZWHFGSGRV-RZFSBTTISA-N,
    average mass 312.347 and monoisotopic mass 312.07799. CHEBI46634 is carbapenemcarboxylic
    acid; CHEBI79020 is alpha,beta-unsaturated monocarboxylic acid. CHEBI33281, CHEBI33282
    and CHEBI36047 denote antimicrobial agent, antibacterial agent and antibacterial
    drug. Exact systematic synonyms encode the same stereochemistry and E-vinyl side
    chain. CAS65322-98-7 and Beilstein497581 are source-attested; the subscription
    Beilstein registry was not independently inspected.
  snapshot_sha256: f91b9dbb732a4d133073795a4111082c204d7f18af05ace390bc7efc0e2beea4
- evidence_id: xref
  kind: database
  reference: https://rest.kegg.jp/get/C17398; https://rest.kegg.jp/get/C17398/mol;
    https://pubchem.ncbi.nlm.nih.gov/compound/22824517
  locator: Full KEGG entry and molfile; official PubChem property response.
  accessed_at: '2026-10-21T10:40:19Z'
  support: supports
  summary: KEGG C17398 names MM22383 and epithienamycin D and cross-references ChEBI58998
    and CAS65322-98-7. Independent parsing of its molfile reproduces the full native
    key and all three stereocentres. PubChem CID22824517 likewise matches the native
    InChI/key. The KEGG PubChem accession is a substance reference and is not treated
    as a mismatched compound CID.
  snapshot_sha256: d382de122d62fdd00f5ad666bf4af3c07a7f0996d4e77549ad5ba4b5198d4824
- evidence_id: chemistry
  kind: validation
  reference: 195-chemistry.json; 195-kegg-chemistry.json
  locator: Independent native SMILES/InChI parsing, computed properties, exact source
    mint and KEGG structure comparison.
  accessed_at: '2026-10-21T10:40:19Z'
  support: supports
  summary: Both native strings are valid one-fragment neutral structures with matching
    formula, key, masses, stereochemistry and source mint antibioticmech:chebi-76365d348b.
    There is no identity conflict among these inspected official structures.
  snapshot_sha256: dbb312e56f845684868bd4b78c721049c9856cd9173d17dbcb9c73e9458b7ab4
- evidence_id: adopted
  kind: primary_source
  reference: PMID:3338858; DOI:10.1159/000234500
  locator: Complete indexed abstract; publisher full text unavailable with HTTP403.
  accessed_at: '2026-10-21T10:40:19Z'
  support: context_only
  summary: The paper concerns MM22383 immunogenicity/allergenicity in guinea pigs
    and rabbits and occupational allergy implications. Hapten-protein conjugation
    is not bacterial PBP binding. This citation does not supply antibacterial potency,
    bacterial target identity or clinical efficacy evidence.
  snapshot_sha256: add3244c7103ed004e0fb4b85551beb8892ac5312c1540cfa0df6ded25f54883
- evidence_id: structure1979
  kind: primary_source
  reference: PMID:511786; DOI:10.7164/antibiotics.32.961
  locator: Complete original main text; original p961 structure drawings visually
    inspected.
  accessed_at: '2026-10-21T10:40:19Z'
  support: supports
  summary: MM22383 is acid10, with sodium salt14 and p-nitrobenzyl ester18 distinguished.
    Spectroscopy establishes the E-vinyl group and trans beta-lactam relation. The
    ester crystallography establishes the relative hydroxyethyl configuration; the
    absolute C5R assignment is explicitly assumed from known natural beta-lactams.
    This supports the current literature designation without claiming an independent
    absolute X-ray determination.
  snapshot_sha256: cc90dd92cd2a2fe3dfd19fe93eace4ffea6ddf17f4af942e83189afa52e1e813
- evidence_id: production1979
  kind: primary_source
  reference: PMID:317283; DOI:10.7164/antibiotics.32.1239
  locator: Entire original paper; p1244 Tables3 and4 visually inspected.
  accessed_at: '2026-10-21T10:40:19Z'
  support: supports
  summary: 'S. olivaceus ATCC31365 fermentation yielded chromatographically purified
    MM22383 sodium salt. Table3 reports nutrient-broth microtitre MICs including 8
    micrograms/mL for E. coli O111 and S. aureus Oxford, 125 for P. aeruginosa A.
    Table4 reports cell-free beta-lactamase I50 values: E. cloacae P99 0.04, P. aeruginosa
    A 4.0, P. mirabilis C889 0.4, E. coli JT4 0.1 and S. aureus Russell >2.0 micrograms/mL,
    with cephaloridine or benzylpenicillin substrate as specified. The method is delegated
    to Reading/Hepburn. Trans-compound biosynthetic relationships remained unresolved.'
  snapshot_sha256: d0f1b974b59b6d8aeba3e51ac75ef6d971f162fcbea9c8b7a9bced5493962dbd
- evidence_id: activity1980
  kind: primary_source
  reference: PMID:6968745; DOI:10.7164/antibiotics.33.878
  locator: Complete main text; original Table1 p880 visually inspected.
  accessed_at: '2026-10-21T10:40:19Z'
  support: supports
  summary: Each Table1 value is a median MIC among ten clinical isolates, not a single-strain
    observation. MM22383 medians include 12.5 micrograms/mL for E. coli, 6.2 for susceptible/penicillin-resistant
    S. aureus, 100 for methicillin-resistant S. aureus and >100 for P. aeruginosa.
    Broth dilution uses organism-dependent medium and no-visible-growth endpoint,
    18 hours for aerobes and 24 hours for anaerobes at 37 degrees C. Combination results
    concern amoxicillin plus a fixed subinhibitory olivanic-acid concentration; they
    are not standalone MM22383 MICs. No direct PBP assay or clinical treatment demonstration
    is supplied.
  snapshot_sha256: f515c0aa78f3afd1d5329a60706e41e2d6f0dc6b8a70c914742390516566705d
- evidence_id: adapter
  kind: database
  reference: Structured-source applicability assessed from complete native record
    before web research
  locator: No native gene, protein, locus, pathway, regulator, response or transcriptomic
    dataset.
  accessed_at: '2026-10-21T10:40:19Z'
  support: context_only
  summary: No record assertion required an iModulonDB query. Newly encountered production
    and cell-free enzyme evidence does not turn expression-module absence into negative
    evidence or justify a sequence-specific target accession.
- evidence_id: search
  kind: search
  reference: 195-maintained-search.txt; 195-inclusive-file-hits.txt
  locator: Exact identifier, name variants, slug and full-key stem; hidden and ignored
    files included.
  accessed_at: '2026-10-21T10:40:19Z'
  support: context_only
  summary: Searches found the native and raw rows, path ledger, readiness queue and
    generated maps. No separate maintained correction or exact curated primary-evidence
    object was found within that scope. Generated maps and historical leads were not
    scientific evidence.
  snapshot_sha256: e5b6bd2300136d3a24a2e788cc203a880d6f19e4898ab66aa51c8931cf4c6f76
  search_scope: rg --no-ignore --hidden across data, curation, conf, scripts, src,
    docs, .claude, reviews and reports for CHEBI:58998, MM22383, MM 22383, carbapenem-mm22383
    and PRPNUZWHFGSGRV; .git and .venv internals excluded.
- evidence_id: validation
  kind: validation
  reference: 195-focused-results.json; 195-schema.log; 195-strict.log
  locator: Actual documented focused validators and independent chemistry.
  accessed_at: '2026-10-21T10:40:19Z'
  support: supports
  summary: Schema, strict and chemistry checks all exit0. These passes establish deterministic
    consistency, not clinical use or primary scientific sign-off.
  snapshot_sha256: d2a0765a1ffbc1f99bb1d7dd86b7cf947e621f81c519328de305dde8fedc6faf
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral structure and systematic names
  outcome: supported
  summary: Both strings, official structures and the original structure assignment
    agree. Sodium assay material, ester crystallography and absolute-assignment assumptions
    remain explicit.
  target_ids:
  - CHEBI:58998
  evidence_ids:
  - official
  - xref
  - chemistry
  - structure1979
- assessment_id: grounding
  area: grounding
  topic: Parents, roles and registry references
  outcome: supported
  summary: Parent classes and antimicrobial roles are structurally/source concordant;
    primary experiments independently support antibacterial inclusion. The antibacterial-drug
    role is ChEBI-attested, while an exact clinical-use claim was not independently
    established.
  target_ids:
  - CHEBI:58998
  evidence_ids:
  - official
  - production1979
  - activity1980
- assessment_id: citation
  area: evidence
  topic: Sole adopted citation disposition
  outcome: supported
  summary: PMID3338858 supports allergenicity context only. It is correctly not automatically
    promoted into antimicrobial claim-level evidence.
  target_ids:
  - CHEBI:58998
  evidence_ids:
  - source
  - adopted
- assessment_id: activity
  area: evidence
  topic: Historical exact-material antibacterial observations
  outcome: supported
  summary: The original individual-strain and later clinical-panel experiments support
    antibacterial activity, with method, salt material and statistic boundaries retained.
  target_ids:
  - CHEBI:58998
  evidence_ids:
  - structure1979
  - production1979
  - activity1980
- assessment_id: mechanism
  area: completeness
  topic: Cell-free enzyme inhibition versus antibacterial mechanism
  outcome: supported
  summary: There is direct inhibition evidence for named beta-lactamase preparations.
    That does not identify a sequence-specific protein accession, establish all PBP
    targets or prove a complete bacterial killing chain. No native target claim is
    currently wrong.
  target_ids:
  - CHEBI:58998
  evidence_ids:
  - production1979
  - activity1980
  - adapter
- assessment_id: producer
  area: provenance
  topic: Natural production versus biosynthetic pathway
  outcome: supported
  summary: Culture fermentation and purification support S. olivaceus ATCC31365 as
    a producer in the reported conditions. The paper explicitly leaves trans-olivanic-acid
    pathway relationships unresolved; no gene-cluster assignment is inferred.
  target_ids:
  - CHEBI:58998
  evidence_ids:
  - production1979
- assessment_id: completeness
  area: completeness
  topic: Optional primary evidence enrichment
  outcome: supported
  summary: Activity, producer and bounded enzyme observations are available for future
    curation. Their missing optional fields are an informational opportunity rather
    than a required-field defect.
  target_ids:
  - CHEBI:58998
  evidence_ids:
  - record
  - production1979
  - activity1980
- assessment_id: ownership
  area: ownership
  topic: Maintained source and future curated additions
  outcome: supported
  summary: Source identity remains owned by the adopted ChEBI row/extractor/seeder.
    Future claim-level additions belong to the actual native record through validated
    curation entrypoints. Initial captures remain intact.
  target_ids:
  - CHEBI:58998
  evidence_ids:
  - source
  - record
- assessment_id: checks
  area: schema
  topic: Focused validity and history
  outcome: supported
  summary: The complete record and history were read; documented per-record validation
    and internal chemistry passed.
  target_ids:
  - CHEBI:58998
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: mm22383-qualified-primary-evidence-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Add exact primary observations with salt, assay and enzyme-preparation scope
  description: The seed has sound identity and antibacterial inclusion but no claim-level
    primary observations. Original papers provide activity, culture production and
    cell-free beta-lactamase inhibition. The adopted allergenicity paper cannot supply
    those claims. Optional enrichment should preserve individual-strain versus median-panel
    MICs and avoid inferring clinical use or PBP binding.
  target_ids:
  - CHEBI:58998
  field_paths:
  - evidence
  - activity_spectrum
  - producer_organisms
  - molecular_targets
  evidence_ids:
  - record
  - adopted
  - structure1979
  - production1979
  - activity1980
  rule_id: 'native-review-checklist: exact-material claim-level evidence and optional
    completeness'
  native_severity: informational optional enrichment
  normalization_reason: No required representation is absent and no inspected native
    assertion is demonstrably false. The task is bounded evidence enrichment, not
    automatic status promotion.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/carbapenem-mm22383.yaml
    role: Future claim-level primary evidence, activity, producer and bounded enzyme
      observations
actions:
- action_id: A1
  description: Curate the original MM22383 observations without transferring neighboring
    compound or clinical claims.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:58998
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/carbapenem-mm22383.yaml
    role: Future claim-level primary evidence, activity, producer and bounded enzyme
      observations
  acceptance_checks:
  - Attach the original structure and production/activity papers at the claims they
    support. Distinguish acid10, sodium salt14 and ester18 and resolve the tested
    material representation before assigning numerical observations to the neutral
    record.
  - For 1979 Table3 preserve individual strain, nutrient-broth assay and reported
    MIC units. For 1980 Table1 preserve that each value is a median of ten isolates,
    the strict greater-than comparator, organism-dependent medium, incubation and
    no-growth endpoint. Do not silently convert medians to strain-level MICs or clinical
    breakpoints.
  - If adding beta-lactamase inhibition, identify the exact cell-free preparation,
    substrate and reported I50 from 1979 Table4, and inspect its cited assay-method
    paper before supplying detailed kinetics or concentrations. Do not infer UniProt
    identity, PBP binding or mechanism of bacterial death from those preparations.
  - Support producer_organisms with the reported pure-culture fermentation and purified
    product from S. olivaceus ATCC31365; independently resolve a strain/taxon accession
    before adding an ontology identifier. Do not infer a demonstrated trans-compound
    biosynthetic gene cluster.
  - Keep PMID3338858 confined to its allergenicity scope. Treat the ChEBI antibacterial-drug
    role as source-attested until exact therapeutic-use evidence is inspected; do
    not add approval, clinical efficacy or safety claims from in vitro activity alone.
  - Use write_validated_antibiotic and record_curation_event for separately authorized
    curation of data/antibiotics/antibacterial/carbapenem-mm22383.yaml, preserve additions
    through reseeding, and run applicable focused/shared checks.
limitations:
- All 13 initial source inputs were captured before assessment and remain unchanged.
  Complete native record, source row, relevant configuration and source transforms
  were read.
- The adopted 1988 allergenicity paper was available as a complete indexed abstract
  only; the publisher returned HTTP403. The original 1979 structure/production papers
  and 1980 antibacterial paper were inspected in full main text, with the pertinent
  original structure drawing and Tables3/4 and Table1 visually checked.
- Absolute C5R in the original crystallographic structure paper is explicitly assumed
  from known natural beta-lactams. This review did not independently redetermine absolute
  configuration; current official structures agree with that literature assignment.
- Original isolation used sodium salts. The neutral-acid record is chemically coherent,
  but future quantitative observations must retain assay-material form and cannot
  silently imply that all experiments used the isolated free acid.
- The 1980 inoculum wording does not unambiguously identify the final well inoculum;
  no unreported final concentration is supplied. The 1979 Table3 footnote visibly
  specifies approximately10^6 cells/mL. Historical organism names require careful
  taxonomic resolution before adding modern accessions.
- The beta-lactamase method paper cited by the production study was not independently
  read. Therefore the review reports its Table4 I50 values and enzyme-preparation/substrate
  scope without reconstructing missing kinetic details.
- Beilstein497581 was verified as the ChEBI source xref, not by subscription-registry
  inspection. Clinical therapeutic use, approval and a complete PBP/causal mechanism
  were not established in this bounded review.
- A later derivative-synthesis paper was located and downloaded but not used as full-text
  evidence; its reported C8 inversion concerns a synthetic derivative route and does
  not independently contradict the native MM22383 structure.
- Chemistry used the existing batch019 RDKit interpreter because the batch020 locked
  environment lacks RDKit; its actual command and working-tree inputs are recorded.
  No native expression claim required a structured transcriptomics query.
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
