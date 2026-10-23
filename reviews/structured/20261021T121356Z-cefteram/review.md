# Cefteram: active-acid identity and primary antibacterial evidence supported; one synonym typo

- Review: 20261021T121356Z-cefteram
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:49:05Z
- Finished UTC: 2026-10-21T12:13:56Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The record correctly represents cefteram, the neutral 6R,7R Z-oxime active acid T-2525, separately from cefteram pivoxil T-2588. Official chemical cross-references agree and original assays support antibacterial activity and PBP competition in named bacterial preparations. The native seed makes no unsupported primary target or quantitative activity assertion. One minor source-derived spelling error remains in a systematic synonym. Optional primary mechanism enrichment has a concrete lead but is not itself a required-field defect.

## Scope And Provenance

Entire CHEBI:135776 YAML: definition, four synonyms, parents, role, class, chemical structure, five chemical links, drug/document links, two source concepts and four history events. All four adopted citation abstracts were inspected and classified by actual scope.

Selection: Queue 255; original thirteen captured inputs retained and the actual ARO identity table appended before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:135776 | data/antibiotics/antibacterial/cefteram.yaml | generated | cefteram |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:135776 | Actual focused command exited 0. |
| strict | passed | True | CHEBI:135776 | Actual focused command exited 0. |
| chemistry | passed | False | CHEBI:135776 | Actual focused command exited 0. Batch019 RDKit parsed the batch026 record and reproduced both source mints. |
| Authoritative full QC | failed | True | CHEBI:135776 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:135776 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:135776 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:135776 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:135776 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:135776 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:135776 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:135776 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:135776 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact active acid and links

identity: supported. Targets: CHEBI:135776.

Native and inspected official chemical representations agree on the neutral 6R,7R Z-oxime acid. The pivoxil ester is an explicitly separate compound in the original paper. Chemical xrefs, broader parent/class terms, source mints and registry attestations are coherent.

### Inherited systematic-name typo

identity: concern. Targets: CHEBI:135776.

synonyms[0] says carboxyic acid. The other systematic synonym and independently verified structure confirm carboxylic acid. This is a spelling correction, not a structural or stereochemical revision.

### Antibacterial definition and filing

scope: supported. Targets: CHEBI:135776.

The source definition and antibacterial filing are supported by directly inspected original active-acid experiments. Population measurements, named-strain MICs, oral prodrug efficacy and mammalian host effects are kept separate.

### Optional primary PBP enrichment

completeness: unknown. Targets: CHEBI:135776.

No native mechanism or target object is asserted. The original radioligand competition study is a concrete optional enrichment lead for taxon-agnostic PBP targets with named-organism examples and exact material scope. Missing optional targets/graphs are not automatic errors. Do not turn competition ratios into Kd values or infer universal beta-lactamase stability.

### All four adopted citation leads

evidence: supported. Targets: CHEBI:135776.

All four abstracts were read: one bacterial combination study, two host studies and one review. No source supports all record fields by mere citation presence. The independent original antibacterial/PBP paper provides stronger exact-active-acid evidence.

### Maintained source correction

ownership: supported. Targets: CHEBI:135776.

The spelling defect belongs to the ChEBI inventory/extractor/seeder path. Fourteen captured inputs remain unchanged. No native status or history transition follows from this review.

### Focused gates

schema: supported. Targets: CHEBI:135776.

All focused checks pass. They do not catch the lexical typo or replace claim-level scientific assessment.

## Findings

### F1: Correct carboxyic to carboxylic in the imported systematic synonym

minor / open / confirmed; issue key: cefteram-carboxyic-systematic-synonym-typo.

synonyms[0].synonym_text ends in carboxyic acid, missing the letter l. The same typo appears in the maintained ChEBI source row and current upstream IUPAC field; synonyms[1], PubChem nomenclature and the molecular graph consistently identify a carboxylic acid. Correct the lexical error without changing identity, stereochemistry or protonation.

## Recommended Actions And Acceptance Checks

### A1

Reproduce the one-word systematic-synonym correction through the maintained source path.

- Correct carboxyic acid to carboxylic acid in the exact imported synonym through the inventory/extractor/seeder or an authorized maintained correction; preserve the full remaining chemical name.
- Regenerate and confirm that the native graph, formula, full key, two R centres, Z oxime, source mints and all other intended fields remain unchanged.
- Run focused schema/strict and applicable source/provenance/reproducibility checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cefteram.yaml; Entire YAML including chemical fields and all four history events. | supports | The SEEDED/EXACT record has a neutral C16H17N9O5S2 graph, two R stereocentres, Z oxime and full key XSPUSVIQHBDITA-RKYNPMAHSA-N. There are no molecular-target, mechanism, resistance, quantitative activity, producer, clinical-status, causal-graph or dataset objects. Absence of optional fields alone is not a required-field failure. |
| source | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact ChEBI row 2564 and ARO row 580; adopted role/class policy and source extraction/seeding code. | supports | ChEBI supplies the identity, definition, aliases, role and registry/drug links. ARO supplies the broader cephalosporin class and ChEMBL/PubChem links. Source bibliographies contain two ChEBI and two ARO PMIDs. The systematic synonym spelling error is already present in the maintained ChEBI row. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:135776; Current complete visible entry: structure, names, relations, registry numbers and links. | supports | The entry matches the native graph, masses 479.504/479.07941, formula, charge and key. CHEBI:23066 is the broader cephalosporin class. Current antibacterial-role detail supports, rather than contradicts, the seed antimicrobial ancestor CHEBI:33281. The current IUPAC field retains carboxyic rather than carboxylic; another exact synonym spells the functional group correctly. |
| chemical-links | https://pubchem.ncbi.nlm.nih.gov/compound/6537431; https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL2105953.json; https://drugcentral.org/drugcard/3076; https://drugcentral.org/drug/3076/inchi; Official chemical property records and independently parsed SMILES/InChI representations. | supports | Five representations from PubChem, ChEMBL and DrugCentral independently reproduce the native full key, formula, neutral charge, two R centres and Z oxime. The matching DrugCentral identity is the free acid even though broad drug context may discuss the prodrug. A search surfaced a separate E-oxime PubChem entry 5464257; it is not the native xref and was not substituted. |
| card | https://card.mcmaster.ca/ontology/47951; Full indexed source identity, structure, class, parents and publication list. | supports | ARO:3009121 is cefteram, explicitly under the third-generation cephalosporin subclass and broader cephalosporin ARO:0000032. Its matching Z-oxime SMILES, CAS 82547-58-8, ChEBI 135776, ChEMBL 2105953 and PubChem 6537431 corroborate the seed. The two cited ARO papers concern host pharmacology and antigenicity, so they are not treated as direct bacterial target experiments. |
| registry-document | https://www.ebi.ac.uk/chebi/CHEBI:135776; https://en.wikipedia.org/wiki/Cefteram; Public registry attestation and resolved document link. | partial | CAS 82547-58-8 is consistently attested by the inspected official chemical sources; ChEBI attests Reaxys 6030279, whose paid registry was not accessed. The Wikipedia document link resolves to the cefteram topic with its active-acid identity. It is not used as primary antimicrobial or regulatory evidence. |
| primary-identity-activity | PMID:3499115; https://doi.org/10.1128/AAC.31.7.1111; https://pmc.ncbi.nlm.nih.gov/articles/PMC174880/?page=1; All six original pages 1111–1116 personally read, including Figure 1, Methods, Tables 1–3 and Figures 2–5. | supports | Figure 1 distinguishes T-2588 pivoxil ester from T-2525 acid, matching the native connectivity and Z side chain. In vitro assays use T-2525 from Toyama. Twofold agar dilution uses sensitivity-test agar with species-specific media, approximately 1×10^4–4×10^4 CFU per spot, 37°C for 18 h or 48 h for obligate anaerobes, and no visible growth as endpoint. Table 1 reports population ranges/MIC50/MIC90; Figure 2 captions give strain-specific acid MICs of 3.13 µg/mL for S. aureus 209P JC-1 and 0.2 µg/mL for E. coli K-12 JE1011. These are distinct from oral T-2588 mouse efficacy and pharmacokinetic results. |
| primary-mechanism | PMID:3499115; https://doi.org/10.1128/AAC.31.7.1111; Original PBP methods on 1111–1112, Figures 2–3 on 1113, Table 2 on 1114 and Results/Discussion on 1115. | supports | Unlabelled T-2525 competes with [14C]penicillin G in membrane preparations at 30°C for 10 min, followed by gel separation, fluorography and densitometry. The paper reports strongest E. coli K-12 JE1011 affinity for PBP 3 and substantial affinity for PBP 1A/1Bs, plus organism-dependent profiles in S. aureus 209P JC-1, C. perfringens 13 and B. fragilis NCTC 943. Figure axes are drug-to-radioligand molar ratios, not dissociation constants. Table 2 demonstrates enzyme-dependent residual hydrolysis, including 12% relative hydrolysis by B. thetaiotaomicron GN11478 enzyme; do not generalize universal stability. The discussion infers bactericidal consequences from PBP patterns; the paper does not present a dedicated time-kill/MBC experiment. |
| adopted-combination | PMID:16944260; https://doi.org/10.1007/s10156-006-0447-x; Complete indexed original abstract. | partial | The study tests cefteram or other beta-lactams with clarithromycin/azithromycin in ten cefixime-resistant N. gonorrhoeae strains. Reported fractional-inhibitory-concentration interactions are combination/strain-specific. The abstract alone does not supply full raw monotherapy MICs or a direct PBP mechanism; cefixime resistance is not automatically cefteram resistance. |
| adopted-host | PMID:3840213; PMID:3761550; Complete indexed abstracts of both adopted Japanese studies. | context_only | 3840213 tests antigenicity of T-2588 and T-2525, including hapten-carrier immunization in animals; it does not demonstrate antibacterial activity. 3761550 explicitly identifies T-2588 as a pivaloyloxymethyl ester converted to T-2525 and studies mammalian general pharmacology. Its description of pharmacological inactivity concerns those host assays, not a conclusion that the active acid lacks antibacterial action. |
| adopted-review | PMID:29017833; https://doi.org/10.1016/j.jaip.2017.08.027; Complete indexed review abstract. | context_only | This is an allergy/cross-reactivity review, not primary antibacterial or exact target evidence. Its clinical claims are not transferred into an approval or producer assertion. |
| other-primary | PMID:2766865; https://doi.org/10.1159/000238677; PMID:3112176; https://doi.org/10.1128/jcm.25.7.1186-1190.1987; PMID:3568594; https://doi.org/10.1016/0732-8893(87)90012-5; Complete indexed original abstracts. | supports | These papers explicitly identify T-2525/Ro 19-5247 as cefteram active acid or active metabolite and report antibacterial testing in 355, 331 and 7745 isolates/strains, respectively. They corroborate antibacterial scope. Historical tentative disk breakpoints and population MIC50 values are not current clinical recommendations or single-isolate observations. Their full Methods were not inspected. |
| adapter | kg-microbe-sources imodulondb --timeout 15 datasets; kg-microbe-sources imodulondb --timeout 15 search --organism e_coli --dataset precise_mg1655 --query penicillin-binding; Structured source catalog and bounded contextual search using PYTHONDONTWRITEBYTECODE=1. | context_only | No native protein/pathway assertion triggered an adapter before the initial identity search. After the original PBP study was located, the catalog and contextual E. coli search were run before further mechanism assessment. Zero gene/module matches were returned. MG1655 expression data would not be the JE1011 membrane-binding assay, and no transcriptomic experiment or negative biological inference is proposed. |
| search | 255-inclusive-file-hits.txt; Hidden and ignored repository files included. | context_only | The inclusive search located exact source/native rows, queue/path locks and generated mappings, with no exact curator overlay or corrective decision found in the searched areas. Bounded public searches separated cefteram acid from cefteram pivoxil and found directly inspected primary evidence. |
| validation | 255-focused-results.json;255-chemistry.json;255-external-chemistry.json; Actual focused gates and independent chemical checks. | supports | Schema, strict and native chemistry commands all exit 0. Native SMILES/InChI and source mints agree. Five official external representations reproduce the full native key, charge, formula, two R centres and Z oxime. |

## Limits And Additional Notes

- All native fields and actual maintained source rows were read. The thirteen original input hashes were preserved and the actual ARO identity input appended before judgment; all fourteen remain unchanged.
- All six pages of PMID:3499115 were personally read from the official original scans, including Methods, structure and binding figures, tables, discussion and references. Oral T-2588 animal efficacy is not assigned to administered free-acid T-2525.
- All four adopted abstracts were inspected. Full papers for the Japanese host studies, gonococcal combination study and allergy review were not inspected; their abstract-level scope is preserved. Three additional antibacterial abstracts corroborate identity/activity but their full Methods were not read.
- CAS and Reaxys identifiers were checked through public official source attestations. Paid registry contents were not accessed. DrugCentral chemical identity was independently verified through its actual public InChI endpoint.
- Structured E. coli search was contextual to a newly discovered primary PBP lead; the covered MG1655 expression dataset is not the experimental JE1011 membrane preparation. Zero hits are not negative biological evidence. No optional target, causal-graph or transcriptomic field is treated as required.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T121356Z-cefteram
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefteram: active-acid identity and primary antibacterial evidence supported;
  one synonym typo'
started_at: '2026-10-21T11:49:05Z'
finished_at: '2026-10-21T12:13:56Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the seed. Read the entire native record and actual
    source rows after preserving the initial capture, independently parsed external
    official structures, and personally read all six original primary-paper scans.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The record correctly represents cefteram, the neutral 6R,7R Z-oxime active
  acid T-2525, separately from cefteram pivoxil T-2588. Official chemical cross-references
  agree and original assays support antibacterial activity and PBP competition in
  named bacterial preparations. The native seed makes no unsupported primary target
  or quantitative activity assertion. One minor source-derived spelling error remains
  in a systematic synonym. Optional primary mechanism enrichment has a concrete lead
  but is not itself a required-field defect.
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
  - path: data/antibiotics/antibacterial/cefteram.yaml
    sha256: 6e42120a9477abba4ff265f317ec978f9d45aad697665289589a8d70b554c29c
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
targets:
- target_id: CHEBI:135776
  path: data/antibiotics/antibacterial/cefteram.yaml
  label: cefteram
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
    role: Adopted ARO identity and bibliography
scope:
  description: 'Entire CHEBI:135776 YAML: definition, four synonyms, parents, role,
    class, chemical structure, five chemical links, drug/document links, two source
    concepts and four history events. All four adopted citation abstracts were inspected
    and classified by actual scope.'
  selection: Queue 255; original thirteen captured inputs retained and the actual
    ARO identity table appended before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:135776
  exclusions:
  - target: Cefteram pivoxil T-2588 and geometric/stereochemical variants
    reason: The record is the active free acid T-2525. Oral prodrug animal efficacy
      and PK are not automatically experiments on the administered free acid.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:135776
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefteram.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:135776
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefteram.yaml --out /private/tmp/am-review-session/255-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Actual focused command exited 0. Batch019 RDKit parsed the batch026 record
    and reproduced both source mints.
  target_ids:
  - CHEBI:135776
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 255
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
  - CHEBI:135776
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
  - CHEBI:135776
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
  - CHEBI:135776
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
  - CHEBI:135776
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
  - CHEBI:135776
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
  - CHEBI:135776
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
  - CHEBI:135776
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
  - CHEBI:135776
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
  - CHEBI:135776
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cefteram.yaml
  locator: Entire YAML including chemical fields and all four history events.
  accessed_at: '2026-10-21T11:56:41Z'
  support: supports
  summary: The SEEDED/EXACT record has a neutral C16H17N9O5S2 graph, two R stereocentres,
    Z oxime and full key XSPUSVIQHBDITA-RKYNPMAHSA-N. There are no molecular-target,
    mechanism, resistance, quantitative activity, producer, clinical-status, causal-graph
    or dataset objects. Absence of optional fields alone is not a required-field failure.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; conf/sources.yaml;
    scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  locator: Exact ChEBI row 2564 and ARO row 580; adopted role/class policy and source
    extraction/seeding code.
  accessed_at: '2026-10-21T11:56:41Z'
  support: supports
  summary: ChEBI supplies the identity, definition, aliases, role and registry/drug
    links. ARO supplies the broader cephalosporin class and ChEMBL/PubChem links.
    Source bibliographies contain two ChEBI and two ARO PMIDs. The systematic synonym
    spelling error is already present in the maintained ChEBI row.
  snapshot_sha256: ab979807a9353656acacf91c360a6e2c7a7db5681e60b7bcdcc6244d9fd76fa7
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:135776
  locator: 'Current complete visible entry: structure, names, relations, registry
    numbers and links.'
  accessed_at: '2026-10-21T11:56:41Z'
  support: supports
  summary: The entry matches the native graph, masses 479.504/479.07941, formula,
    charge and key. CHEBI:23066 is the broader cephalosporin class. Current antibacterial-role
    detail supports, rather than contradicts, the seed antimicrobial ancestor CHEBI:33281.
    The current IUPAC field retains carboxyic rather than carboxylic; another exact
    synonym spells the functional group correctly.
  snapshot_sha256: 6cab78e8acb5f37887fa1c8d2b1aced9f0cb628f8248faca52adb256567756f3
- evidence_id: chemical-links
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/6537431; https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL2105953.json;
    https://drugcentral.org/drugcard/3076; https://drugcentral.org/drug/3076/inchi
  locator: Official chemical property records and independently parsed SMILES/InChI
    representations.
  accessed_at: '2026-10-21T11:56:41Z'
  support: supports
  summary: Five representations from PubChem, ChEMBL and DrugCentral independently
    reproduce the native full key, formula, neutral charge, two R centres and Z oxime.
    The matching DrugCentral identity is the free acid even though broad drug context
    may discuss the prodrug. A search surfaced a separate E-oxime PubChem entry 5464257;
    it is not the native xref and was not substituted.
  snapshot_sha256: e92a0640d796d696c2cbffdb978cc3abaf704ce87a30cc754e01151ad729d912
- evidence_id: card
  kind: database
  reference: https://card.mcmaster.ca/ontology/47951
  locator: Full indexed source identity, structure, class, parents and publication
    list.
  accessed_at: '2026-10-21T11:56:41Z'
  support: supports
  summary: ARO:3009121 is cefteram, explicitly under the third-generation cephalosporin
    subclass and broader cephalosporin ARO:0000032. Its matching Z-oxime SMILES, CAS
    82547-58-8, ChEBI 135776, ChEMBL 2105953 and PubChem 6537431 corroborate the seed.
    The two cited ARO papers concern host pharmacology and antigenicity, so they are
    not treated as direct bacterial target experiments.
  snapshot_sha256: dcc6b7022e55af11341246258065134f1f9027af4e8a54e0926ccd9dc2eb66e0
- evidence_id: registry-document
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:135776; https://en.wikipedia.org/wiki/Cefteram
  locator: Public registry attestation and resolved document link.
  accessed_at: '2026-10-21T11:56:41Z'
  support: partial
  summary: CAS 82547-58-8 is consistently attested by the inspected official chemical
    sources; ChEBI attests Reaxys 6030279, whose paid registry was not accessed. The
    Wikipedia document link resolves to the cefteram topic with its active-acid identity.
    It is not used as primary antimicrobial or regulatory evidence.
  snapshot_sha256: 9c932d28b7828b6e7f9ef0379e8d1530eeb974e85a0c06e316d0f4fe66bc2d96
- evidence_id: primary-identity-activity
  kind: primary_source
  reference: PMID:3499115; https://doi.org/10.1128/AAC.31.7.1111; https://pmc.ncbi.nlm.nih.gov/articles/PMC174880/?page=1
  locator: All six original pages 1111–1116 personally read, including Figure 1, Methods,
    Tables 1–3 and Figures 2–5.
  accessed_at: '2026-10-21T11:56:41Z'
  support: supports
  summary: Figure 1 distinguishes T-2588 pivoxil ester from T-2525 acid, matching
    the native connectivity and Z side chain. In vitro assays use T-2525 from Toyama.
    Twofold agar dilution uses sensitivity-test agar with species-specific media,
    approximately 1×10^4–4×10^4 CFU per spot, 37°C for 18 h or 48 h for obligate anaerobes,
    and no visible growth as endpoint. Table 1 reports population ranges/MIC50/MIC90;
    Figure 2 captions give strain-specific acid MICs of 3.13 µg/mL for S. aureus 209P
    JC-1 and 0.2 µg/mL for E. coli K-12 JE1011. These are distinct from oral T-2588
    mouse efficacy and pharmacokinetic results.
  snapshot_sha256: c0925dc4a6543f7a7f99e9fd32c285294efe2f365c3acfa6c66a06bed3233e81
- evidence_id: primary-mechanism
  kind: primary_source
  reference: PMID:3499115; https://doi.org/10.1128/AAC.31.7.1111
  locator: Original PBP methods on 1111–1112, Figures 2–3 on 1113, Table 2 on 1114
    and Results/Discussion on 1115.
  accessed_at: '2026-10-21T11:56:41Z'
  support: supports
  summary: Unlabelled T-2525 competes with [14C]penicillin G in membrane preparations
    at 30°C for 10 min, followed by gel separation, fluorography and densitometry.
    The paper reports strongest E. coli K-12 JE1011 affinity for PBP 3 and substantial
    affinity for PBP 1A/1Bs, plus organism-dependent profiles in S. aureus 209P JC-1,
    C. perfringens 13 and B. fragilis NCTC 943. Figure axes are drug-to-radioligand
    molar ratios, not dissociation constants. Table 2 demonstrates enzyme-dependent
    residual hydrolysis, including 12% relative hydrolysis by B. thetaiotaomicron
    GN11478 enzyme; do not generalize universal stability. The discussion infers bactericidal
    consequences from PBP patterns; the paper does not present a dedicated time-kill/MBC
    experiment.
  snapshot_sha256: 53b356b85089ecf34e55320139b0800e8733420ba5b80a4a38a2215df3cd8244
- evidence_id: adopted-combination
  kind: primary_source
  reference: PMID:16944260; https://doi.org/10.1007/s10156-006-0447-x
  locator: Complete indexed original abstract.
  accessed_at: '2026-10-21T11:56:41Z'
  support: partial
  summary: The study tests cefteram or other beta-lactams with clarithromycin/azithromycin
    in ten cefixime-resistant N. gonorrhoeae strains. Reported fractional-inhibitory-concentration
    interactions are combination/strain-specific. The abstract alone does not supply
    full raw monotherapy MICs or a direct PBP mechanism; cefixime resistance is not
    automatically cefteram resistance.
  snapshot_sha256: fecebd6bca0814baae6dc1fbb4e3f30f25f039d4c474152ac8174b038a5ec9ea
- evidence_id: adopted-host
  kind: primary_source
  reference: PMID:3840213; PMID:3761550
  locator: Complete indexed abstracts of both adopted Japanese studies.
  accessed_at: '2026-10-21T11:56:41Z'
  support: context_only
  summary: 3840213 tests antigenicity of T-2588 and T-2525, including hapten-carrier
    immunization in animals; it does not demonstrate antibacterial activity. 3761550
    explicitly identifies T-2588 as a pivaloyloxymethyl ester converted to T-2525
    and studies mammalian general pharmacology. Its description of pharmacological
    inactivity concerns those host assays, not a conclusion that the active acid lacks
    antibacterial action.
  snapshot_sha256: fecebd6bca0814baae6dc1fbb4e3f30f25f039d4c474152ac8174b038a5ec9ea
- evidence_id: adopted-review
  kind: database
  reference: PMID:29017833; https://doi.org/10.1016/j.jaip.2017.08.027
  locator: Complete indexed review abstract.
  accessed_at: '2026-10-21T11:56:41Z'
  support: context_only
  summary: This is an allergy/cross-reactivity review, not primary antibacterial or
    exact target evidence. Its clinical claims are not transferred into an approval
    or producer assertion.
  snapshot_sha256: fecebd6bca0814baae6dc1fbb4e3f30f25f039d4c474152ac8174b038a5ec9ea
- evidence_id: other-primary
  kind: primary_source
  reference: PMID:2766865; https://doi.org/10.1159/000238677; PMID:3112176; https://doi.org/10.1128/jcm.25.7.1186-1190.1987;
    PMID:3568594; https://doi.org/10.1016/0732-8893(87)90012-5
  locator: Complete indexed original abstracts.
  accessed_at: '2026-10-21T11:56:41Z'
  support: supports
  summary: These papers explicitly identify T-2525/Ro 19-5247 as cefteram active acid
    or active metabolite and report antibacterial testing in 355, 331 and 7745 isolates/strains,
    respectively. They corroborate antibacterial scope. Historical tentative disk
    breakpoints and population MIC50 values are not current clinical recommendations
    or single-isolate observations. Their full Methods were not inspected.
  snapshot_sha256: f8e4395db078468295e4a82e3db84cf04a67862e095fb8378aff74e06ab79a16
- evidence_id: adapter
  kind: database
  reference: kg-microbe-sources imodulondb --timeout 15 datasets; kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise_mg1655 --query
    penicillin-binding
  locator: Structured source catalog and bounded contextual search using PYTHONDONTWRITEBYTECODE=1.
  accessed_at: '2026-10-21T11:56:41Z'
  support: context_only
  summary: No native protein/pathway assertion triggered an adapter before the initial
    identity search. After the original PBP study was located, the catalog and contextual
    E. coli search were run before further mechanism assessment. Zero gene/module
    matches were returned. MG1655 expression data would not be the JE1011 membrane-binding
    assay, and no transcriptomic experiment or negative biological inference is proposed.
  snapshot_sha256: c0c1349634c9fe27513341b9e3874b42ccdbe1e5aaf236bb1dc12561a196e078
- evidence_id: search
  kind: search
  reference: 255-inclusive-file-hits.txt
  locator: Hidden and ignored repository files included.
  accessed_at: '2026-10-21T11:56:41Z'
  support: context_only
  summary: The inclusive search located exact source/native rows, queue/path locks
    and generated mappings, with no exact curator overlay or corrective decision found
    in the searched areas. Bounded public searches separated cefteram acid from cefteram
    pivoxil and found directly inspected primary evidence.
  snapshot_sha256: f1b7225ad9d61b7256f7cdcc3efb46f4833b6f76c179d50bcd5d745527705e0a
  search_scope: rg --no-ignore --hidden over data, curation, conf, scripts, src, docs,
    .claude, reviews and reports for cefteram, CHEBI:135776, ARO:3009121, full key
    and source mint.
- evidence_id: validation
  kind: validation
  reference: 255-focused-results.json;255-chemistry.json;255-external-chemistry.json
  locator: Actual focused gates and independent chemical checks.
  accessed_at: '2026-10-21T11:56:41Z'
  support: supports
  summary: Schema, strict and native chemistry commands all exit 0. Native SMILES/InChI
    and source mints agree. Five official external representations reproduce the full
    native key, charge, formula, two R centres and Z oxime.
  snapshot_sha256: 06c8788730f4cbc244768051951eed26b6170a4d332a68351a20d1f097395f30
assessments:
- assessment_id: identity
  area: identity
  topic: Exact active acid and links
  outcome: supported
  summary: Native and inspected official chemical representations agree on the neutral
    6R,7R Z-oxime acid. The pivoxil ester is an explicitly separate compound in the
    original paper. Chemical xrefs, broader parent/class terms, source mints and registry
    attestations are coherent.
  target_ids:
  - CHEBI:135776
  evidence_ids:
  - chebi
  - chemical-links
  - card
  - registry-document
  - primary-identity-activity
  - validation
- assessment_id: names
  area: identity
  topic: Inherited systematic-name typo
  outcome: concern
  summary: synonyms[0] says carboxyic acid. The other systematic synonym and independently
    verified structure confirm carboxylic acid. This is a spelling correction, not
    a structural or stereochemical revision.
  target_ids:
  - CHEBI:135776
  evidence_ids:
  - record
  - source
  - chebi
  - chemical-links
- assessment_id: activity
  area: scope
  topic: Antibacterial definition and filing
  outcome: supported
  summary: The source definition and antibacterial filing are supported by directly
    inspected original active-acid experiments. Population measurements, named-strain
    MICs, oral prodrug efficacy and mammalian host effects are kept separate.
  target_ids:
  - CHEBI:135776
  evidence_ids:
  - primary-identity-activity
  - other-primary
  - adopted-combination
  - adopted-host
- assessment_id: mechanism
  area: completeness
  topic: Optional primary PBP enrichment
  outcome: unknown
  summary: No native mechanism or target object is asserted. The original radioligand
    competition study is a concrete optional enrichment lead for taxon-agnostic PBP
    targets with named-organism examples and exact material scope. Missing optional
    targets/graphs are not automatic errors. Do not turn competition ratios into Kd
    values or infer universal beta-lactamase stability.
  target_ids:
  - CHEBI:135776
  evidence_ids:
  - primary-mechanism
  - adapter
  - record
- assessment_id: citation-scope
  area: evidence
  topic: All four adopted citation leads
  outcome: supported
  summary: 'All four abstracts were read: one bacterial combination study, two host
    studies and one review. No source supports all record fields by mere citation
    presence. The independent original antibacterial/PBP paper provides stronger exact-active-acid
    evidence.'
  target_ids:
  - CHEBI:135776
  evidence_ids:
  - adopted-combination
  - adopted-host
  - adopted-review
  - primary-identity-activity
- assessment_id: ownership
  area: ownership
  topic: Maintained source correction
  outcome: supported
  summary: The spelling defect belongs to the ChEBI inventory/extractor/seeder path.
    Fourteen captured inputs remain unchanged. No native status or history transition
    follows from this review.
  target_ids:
  - CHEBI:135776
  evidence_ids:
  - source
  - search
  - validation
- assessment_id: gates
  area: schema
  topic: Focused gates
  outcome: supported
  summary: All focused checks pass. They do not catch the lexical typo or replace
    claim-level scientific assessment.
  target_ids:
  - CHEBI:135776
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: cefteram-carboxyic-systematic-synonym-typo
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Correct carboxyic to carboxylic in the imported systematic synonym
  description: synonyms[0].synonym_text ends in carboxyic acid, missing the letter
    l. The same typo appears in the maintained ChEBI source row and current upstream
    IUPAC field; synonyms[1], PubChem nomenclature and the molecular graph consistently
    identify a carboxylic acid. Correct the lexical error without changing identity,
    stereochemistry or protonation.
  target_ids:
  - CHEBI:135776
  field_paths:
  - synonyms[0].synonym_text
  evidence_ids:
  - record
  - source
  - chebi
  - chemical-links
  rule_id: 'native-review-checklist: exact synonym consistency and spelling'
  native_severity: minor
  normalization_reason: A nonblocking source-derived spelling defect. The intended
    functional group and every checked chemical identity remain unambiguous.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted exact-synonym source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible nomenclature extraction/correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated synonym owner
actions:
- action_id: A1
  description: Reproduce the one-word systematic-synonym correction through the maintained
    source path.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:135776
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted exact-synonym source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible nomenclature extraction/correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated synonym owner
  acceptance_checks:
  - Correct carboxyic acid to carboxylic acid in the exact imported synonym through
    the inventory/extractor/seeder or an authorized maintained correction; preserve
    the full remaining chemical name.
  - Regenerate and confirm that the native graph, formula, full key, two R centres,
    Z oxime, source mints and all other intended fields remain unchanged.
  - Run focused schema/strict and applicable source/provenance/reproducibility checks
    after separately authorized curation.
limitations:
- All native fields and actual maintained source rows were read. The thirteen original
  input hashes were preserved and the actual ARO identity input appended before judgment;
  all fourteen remain unchanged.
- All six pages of PMID:3499115 were personally read from the official original scans,
  including Methods, structure and binding figures, tables, discussion and references.
  Oral T-2588 animal efficacy is not assigned to administered free-acid T-2525.
- All four adopted abstracts were inspected. Full papers for the Japanese host studies,
  gonococcal combination study and allergy review were not inspected; their abstract-level
  scope is preserved. Three additional antibacterial abstracts corroborate identity/activity
  but their full Methods were not read.
- CAS and Reaxys identifiers were checked through public official source attestations.
  Paid registry contents were not accessed. DrugCentral chemical identity was independently
  verified through its actual public InChI endpoint.
- Structured E. coli search was contextual to a newly discovered primary PBP lead;
  the covered MG1655 expression dataset is not the experimental JE1011 membrane preparation.
  Zero hits are not negative biological evidence. No optional target, causal-graph
  or transcriptomic field is treated as required.
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
