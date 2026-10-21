# Review of clavulanic acid

- Review: 20261021T132743Z-clavulanic-acid-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T13:05:01Z
- Finished UTC: 2026-10-21T13:27:43Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Native neutral clavulanic acid has the supported 2R,3Z,5R structure. Versioned MIBiG and the original isolation paper support Streptomyces clavuligerus ATCC 27064; the inherited PMID 8088547 caution is accurate. Primary enzyme studies support mechanism-based beta-lactamase inhibition with enzyme-specific reversible and irreversible components, and the original antibacterial experiments use sodium clavulanate. One minor naming correction is recommended because the exact alias Clavulanate also denotes the separately defined anion. No identity replacement or producer-attribution defect is demonstrated.

## Scope And Provenance

Entire SEEDED, EXACT record: definition, twelve synonyms, chemical parent, antibacterial role, all structure fields, eight chemical links, three drug links, two document links, exact producer object and six history events. All ten adopted ChEBI PMID leads and the inherited MIBiG PMID were resolved.

Selection: Queue 308; initial fourteen inputs preserved and actual MIBiG extractor appended, for fifteen unchanged hashes.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:48947 | data/antibiotics/antibacterial/clavulanic-acid.yaml | generated | clavulanic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema validation | passed | True | CHEBI:48947 | Exit 0. |
| Documented strict validation | passed | True | CHEBI:48947 | Exit 0; no ERROR rows. |
| Native molecular consistency | passed | False | CHEBI:48947 | Exit 0; native encodings, formula, charge, stereochemistry and masses agree. |
| Independent exact molecular comparisons | passed | False | CHEBI:48947 | Exit 0; all nine inspected encodings match by exact key and mutual chirality-aware graph mapping. |
| Maintained source, producer and citation reconciliation | passed | False | CHEBI:48947 | Exit 0; fifteen hashes, six history events, ten ChEBI leads and one inherited MIBiG lead reconcile. Version 5 has one exact compound. |
| Initial structured catalog attempt | failed | False | CHEBI:48947 | Exit 2 from sandbox DNS failure; approved network retry succeeded. |
| Structured catalog retry | passed | False | CHEBI:48947 | Exit 0; no S. clavuligerus dataset; no S. coelicolor or S. albidoflavus substitution. |
| Structured beta-lactamase context | passed | False | CHEBI:48947 | Exit 0; e_coli/modulome/b4150 gene hit, zero iModulons. No summarize call applies. |
| Authoritative full QC | failed | True | CHEBI:48947 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:48947 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:48947 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:48947 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:48947 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:48947 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:48947 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:48947 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:48947 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral 2R,3Z,5R molecule

identity: supported. Targets: CHEBI:48947.

Independent structures and atom mappings agree with native acid; measured salt forms retain explicit boundaries.

### Clavulanate as exact neutral-acid synonym

consistency: concern. Targets: CHEBI:48947.

The source uses the alias generically but independently defines the anion as a distinct charged entity. Exact typing is too strong for unambiguous form matching.

### Exact ATCC 27064 producer and BGC scope

evidence: supported. Targets: CHEBI:48947.

Versioned MIBiG single-compound join, original isolation and official strain identity support the assertion. Native questionable quality and inherited-reference limit are accurate.

### Beta-lactamase inhibition and antibacterial classification

evidence: supported. Targets: CHEBI:48947.

Primary evidence supports enzyme-dependent mechanism-based inhibition and measured intrinsic/synergistic activity; no universal irreversible-inhibition claim is inferred.

### Chemical, drug and document link scopes

identity: supported. Targets: CHEBI:48947.

Inspected exact chemical graphs agree; broader drug/document links remain in appropriate fields. Unavailable registry bodies and a KNApSAcK displayed-key conflict remain limitations.

### All adopted leads, maintained owners and history

provenance: supported. Targets: CHEBI:48947.

Ten ChEBI and one MIBiG lead have explicit checked dispositions. Fifteen input hashes and six history events are preserved.

### Optional primary mechanism and producer evidence

completeness: supported. Targets: CHEBI:48947.

Original papers could strengthen claim-level evidence after separate curation. No missing optional graph, clinical status or MIC is treated as a defect.

### Focused native validation

schema: supported. Targets: CHEBI:48947.

Native schema/strict checks pass; chemical and scientific review remain distinct from them.

## Findings

### F1: Clavulanate exact alias obscures the acid–anion distinction

minor / open / confirmed; issue key: chebi-48947-clavulanate-exact-alias-form-ambiguity.

The native neutral acid calls Clavulanate an EXACT_SYNONYM, although the inspected authority separately defines clavulanate as the monoanion CHEBI:487869. Current ChEBI and KEGG also use the word generically for the drug, so this is a bounded alias-typing ambiguity rather than evidence of a wrong native molecular identity.

## Recommended Actions And Acceptance Checks

### A1

Exclude Clavulanate from automatically generated exact aliases for CHEBI:48947 using the existing maintained synonym_exclusions entry, or separately implement a reproducible RELATED_SYNONYM override if preserving contextual search coverage is desired. Keep neutral acid structure and canonical name unchanged.

- Regeneration must no longer publish bare Clavulanate as an exact neutral-acid alias; retain traceable source provenance and distinguish CHEBI:487869 charge −1 from CHEBI:48947 charge 0.
- Preserve HZZVJAQRINQKSD-PBFISZAISA-N, formula C8H9NO5, exact stereochemistry and producer history. Rerun documented schema/strict validation and required corpus gates after authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/clavulanic-acid.yaml; Entire native YAML, including producer evidence note and complete history | supports | The record is neutral clavulanic acid, with one exact producer/BGC assertion and explicitly inherited rather than compound-attached PMID 8088547 evidence. It has no quantitative MIC, clinical-approval assertion, molecular target object, resistance edge or causal graph. |
| chemistry | CHEBI:48947; PubChem:5280980; PDB-CCD:J01; KEGG:C06662/D07711; MIBiG:BGC0000845; KNApSAcK:C00018091; 308-authority-chemistry.json;308-chemistry.py/.log; official molfile and structure snapshots | supports | Native SMILES and InChI, official ChEBI molfile, PubChem, PDB CCD stereochemical SMILES, both KEGG molfiles, versioned MIBiG structure and KNApSAcK SMILES all match HZZVJAQRINQKSD-PBFISZAISA-N with mutual chirality-aware atom mappings. Formula C8H9NO5, charge 0, average mass 199.162, monoisotopic mass 199.04807 and the 2R,3Z,5R identity agree. KNApSAcK displays a discordant legacy key HZZVJAQRINQKSD-LIJMCTQFNA-N, but its actual standard InChI and SMILES reproduce the native graph; this does not demonstrate a wrong native cross-reference. |
| authority | https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:48947; 308-chebi.json: definition, names, clavam parent CHEBI:64509, antibacterial role and source accessions | supports | Current ChEBI retains the native definition and neutral structure, chemical parent and antibacterial-drug role. Additional current host/pharmacologic roles are outside the adopted antibacterial slice. Twelve native names are source-concordant, including the generic Clavulanate alias. Current chemical xrefs remain source-concordant. |
| anion | https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:487869; 308-anion.json: preferred label, definition, formula/charge and conjugate-base relation | supports | Current ChEBI separately defines clavulanate as the conjugate base of clavulanic acid, C8H8NO5 with charge −1. The acid entry simultaneously retains Clavulanate as a generic synonym inherited from KEGG. Thus the name is used contextually for the drug but is not unambiguous exact-form nomenclature for neutral acid. The proposed correction concerns synonym typing, not native stereochemistry or structure. |
| mibig | https://mibig.secondarymetabolites.org/repository/BGC0000845.5/annotations.json; Version 5 status, quality, compounds, taxonomy, loci evidence and legacy references | supports | Official version 5 is active/questionable and contains one compound, exact clavulanic acid, taxonomy S. clavuligerus ATCC 27064/NCBI 1901 and locus DS570624.1 with Enzymatic assays and Heterologous expression. The compound evidence array is empty and PMID 8088547 is the first legacy reference. The native exact single-compound join, source quality and inherited-reference warning reproduce this scope. Old-schema GitHub JSON is corroborative history, not the version 5 provenance source. |
| isolation | PMID:879738; DOI:10.1128/aac.11.5.852; Original 1977 pp852–857;308-1977-p1.png through p6.png, all six pages visually inspected | supports | The original report cultivates S. clavuligerus ATCC 27064 (NRRL 3585), identifies clavulanic-acid activity separately from co-produced cephamycin C and penicillin N, and isolates the product as sodium clavulanate. Figure 1 depicts the Z-(2R,5R) acid structure. Table 2 is sodium-clavulanate enzyme-inhibition I50 after defined preincubation, not MIC; Table 3 measures sodium-clavulanate-alone and beta-lactam combination MICs by microtiter broth. Intrinsic activity and potentiation are separately reported. Weak inhibition of chromosomal cephalosporinases and absent synergy in some tested organisms preclude a universal beta-lactamase claim. These sodium-salt results support active-moiety biology without pretending the tested solid was neutral acid. |
| inactivation | PMID:7041890; DOI:10.1042/bj1990779; Original 1981 pp779–787;308-1981-p1.png through p9.png, all nine pages visually inspected | supports | Time-dependent enzyme assays, substrate dilution and gel filtration distinguish transient from irreversible inhibition. TEM-2 and K. pneumoniae E70 enzymes partition into transient and irreversible fractions; P. mirabilis C889 shows a much smaller irreversible fraction; E. cloacae P99 shows no detected irreversible inactivation under these conditions. Table 2 and discussion support mechanism-based/suicide inhibition in susceptible enzymes, with proposed covalent-intermediate interpretations distinguished from direct structural observation. This is enzyme-specific evidence, not proof that every bacterial beta-lactamase is irreversibly inhibited. The native generic mechanism description is acceptable at that bounded class level. |
| producer-2014 | PMID:25477926; DOI:10.1590/S1517-83822014000300022; 308-producer2014.xml: Methods, analytical procedure, control strain and selected production Results | supports | ATCC 27064 is the control producer. Potassium clavulanate is the reference reagent; broth product is quantified by imidazole derivatization at 311 nm, and screening zones are measured in the presence of amoxicillin. These results corroborate culture production, not a purified neutral-acid MIC or independent absolute-stereo determination. The new DAUFPE3060 isolate and its 96% 16S similarity-based species assignment are separate from the native producer and are not imported. |
| legacy-paper | PMID:8088547; DOI:10.1016/0378-1119(94)90036-1; Complete original abstract in 308-leads.json and PubMed | supports | The original abstract reports cloning and disruption of cla, with loss of clavulanic-acid production in starch/asparagine medium. This is relevant biosynthetic evidence, but the complete original methods and exact strain designation were not obtained. The native warning that this inherited reference is not independently established as support for the specific producer link is retained. |
| atcc | https://www.atcc.org/products/27064; Official organism identity, strain designation and production summary | supports | ATCC 27064 is S. clavuligerus, strain NRRL 3585, and the catalog explicitly lists clavulanic-acid production. This independently resolves the strain label; it is not substituted for primary mechanism or BGC evidence. |
| other-links | KEGG:C06662/D07711; PDB-CCD:J01; KNApSAcK:C00018091; VSDB:1930; DrugCentral:669; 308-kegg-*.txt/.mol;308-pdb.json/.cif;308-knapsack.html;308-vsdb.html;308-drugcentral.html | supports | KEGG, PDB CCD and KNApSAcK resolve to the exact native molecule. VSDB1930 resolves to clavulanic acid with exact formula, isomeric SMILES and key. DrugCentral669 is clavulanic-acid drug context, with broad salt aliases that are not copied into native exact names. HMDB XML and direct DrugBank returned 403; independent CAS, Beilstein and Reaxys registry bodies were not obtained. No unverified external alias or host target is adopted. |
| documents | Patent:DE2517316; Wikipedia:Clavulanic_Acid; 308-patent.html title and strain/compound discussion;308-wikipedia.html title and mechanism context | context_only | DE2517316A1 covers clavulanic acid, salts and esters and names the producing strain; the broader patent scope is appropriate for a document link, not an exact chemical assertion. Wikipedia resolves to the expected article and was used only as document context, not primary evidence. Neither document establishes regulatory approval or exact assay material by title alone. |
| leads | Ten adopted ChEBI MED citations plus inherited PMID8088547; 308-lead-dispositions.json;308-leads.json | supports | All eleven adopted/inherited leads have explicit dispositions. Three biosynthesis/production reviews remain secondary. Original host behavior, T-cell/IgE and duodenal studies do not establish antimicrobial mechanism. Clinical PK/UTI studies concern amoxicillin combinations, not clavulanic-acid monotherapy or free-acid approval. Only the 2014 producer paper was additionally inspected at Methods/Results depth. Newly added current ChEBI bibliography was not treated as frozen adopted evidence. |
| adapter | iModulonDB e_coli/modulome; 308-adapter-datasets.txt;308-adapter-ampC.txt | context_only | The catalog and ampC query preceded mechanism web research. No S. clavuligerus dataset is covered. The E. coli b4150/ampC hit is gene-catalog context, with zero iModulons; it does not prove clavulanate susceptibility or connect the native producer to a different Streptomyces species. |
| owners | data/raw/chebi_antimicrobials.tsv;data/raw/mibig_producers.tsv;scripts/extract_source_inventory.py;scripts/extract_mibig_producers.py;scripts/seed_from_sources.py;conf/sources.yaml; 308-source-audit.json; maintained synonym and MIBiG transformations | supports | The ChEBI row owns the exact alias and its seeder classification. Existing conf/sources.yaml synonym_exclusions can prevent this exact alias from recurring. MIBiG extraction carries locus evidence to the entry and retains the first legacy reference; the seeder labels a one-compound entry COMPOUND_SPECIFIC and explicitly qualifies inherited evidence. All fifteen captured inputs and six history events remain unchanged. |
| validation | Documented validators and independent chemistry checks; 308-focused-results.json;308-focused-run.log;308-schema.log;308-strict.log;308-authority-chemistry.json;308-source-audit.json | supports | Native schema, strict and molecular consistency checks, authority comparisons and source reconciliation pass. Initial adapter DNS failure is preserved separately; shared full-corpus gates remain separate. |
| search | Exact record and source discovery; Ignored-inclusive rg for CHEBI:48947,BGC0000845,8088547,HZZVJAQRINQKSD in curation,conf,scripts,data/raw; exact adopted MED query and original producer/enzyme searches | context_only | Ignored files were included. The ten adopted ChEBI records and inherited MIBiG record were resolved before source selection. Newly discovered source bibliography is not silently promoted to native evidence. |

## Limits And Additional Notes

- Original 1977 material was isolated and assayed as sodium clavulanate. The 2014 production study uses a potassium-clavulanate reference and an imidazole assay; these are active-moiety/producer evidence, not measurements on isolated neutral acid.
- Full original PMID 8088547 methods were not obtained. Its complete abstract supports biosynthetic disruption, but exact strain/method attribution is not substituted for the native inherited-reference caution.
- The original 1981 inhibitor batches were not independently structurally characterized here. Enzyme preparations and reaction conditions are explicit; the reversible/irreversible outcome is enzyme-specific.
- All ten adopted ChEBI records and inherited MIBiG citation were resolved; most ChEBI leads were abstract-only, with the 2014 producer Methods and selected Results inspected. New current ChEBI citations beyond the frozen ten were not exhaustively reviewed.
- HMDB and DrugBank returned 403; independent CAS, Beilstein and Reaxys bodies were not obtained. KNApSAcK displayed key differs from its own matching standard InChI/SMILES.
- Unversioned MIBiG JSON returned 404; official BGC0000845.5/annotations.json succeeded. Initial PMC PDF responses were browser-challenge HTML, and publisher PDF returned 403; all six 1977 and nine 1981 original journal page scans were successfully obtained and visually inspected.
- The patent title and relevant strain/compound passages were inspected, not every salt/ester example or legal claim. Wikipedia was checked as a document link and not used as primary scientific evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native or maintained source was edited; original capture hashes remain unchanged.
- Missing optional primary evidence enrichment is not reported as a producer or mechanism defect.
- The supported acid, its solution-phase conjugate base and isolated sodium/potassium assay salts are kept distinct.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T132743Z-clavulanic-acid-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of clavulanic acid
started_at: '2026-10-21T13:05:01Z'
finished_at: '2026-10-21T13:27:43Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Entire native record checked against preserved maintained inputs,
    independent exact molecular structures, versioned MIBiG and original producer/enzyme
    papers.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Exact neutral identity and producer supported; minor exact-alias typing
  concern; native REVIEWED gate depends on required shared checks
scientific_review: true
summary: Native neutral clavulanic acid has the supported 2R,3Z,5R structure. Versioned
  MIBiG and the original isolation paper support Streptomyces clavuligerus ATCC 27064;
  the inherited PMID 8088547 caution is accurate. Primary enzyme studies support mechanism-based
  beta-lactamase inhibition with enzyme-specific reversible and irreversible components,
  and the original antibacterial experiments use sodium clavulanate. One minor naming
  correction is recommended because the exact alias Clavulanate also denotes the separately
  defined anion. No identity replacement or producer-attribution defect is demonstrated.
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
  - path: data/antibiotics/antibacterial/clavulanic-acid.yaml
    sha256: 16c7ee5054b33f6e55caa15c59817103f91650f7a524b2ac6b57a6ac250af827
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
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
    role: Adopted exact BGC producer assertions
  - path: scripts/extract_mibig_producers.py
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
    role: Maintained exact MIBiG compound and producer extraction
scope:
  description: 'Entire SEEDED, EXACT record: definition, twelve synonyms, chemical
    parent, antibacterial role, all structure fields, eight chemical links, three
    drug links, two document links, exact producer object and six history events.
    All ten adopted ChEBI PMID leads and the inherited MIBiG PMID were resolved.'
  selection: Queue 308; initial fourteen inputs preserved and actual MIBiG extractor
    appended, for fifteen unchanged hashes.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:48947
targets:
- target_id: CHEBI:48947
  path: data/antibiotics/antibacterial/clavulanic-acid.yaml
  label: clavulanic acid
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
    path: data/raw/mibig_producers.tsv
    role: Adopted exact BGC producer assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_mibig_producers.py
    role: Maintained exact MIBiG compound and producer extraction
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_role_names.tsv
    role: Adopted role names
checks:
- check_id: schema
  name: Documented schema validation
  status: passed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/clavulanic-acid.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0.
  target_ids:
  - CHEBI:48947
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict validation
  status: passed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/clavulanic-acid.yaml --out /private/tmp/am-review-session/308-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no ERROR rows.
  target_ids:
  - CHEBI:48947
  evidence_ids:
  - validation
- check_id: native-chemistry
  name: Native molecular consistency
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    308 > /private/tmp/am-review-session/308-focused-run.log
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; native encodings, formula, charge, stereochemistry and masses agree.
  target_ids:
  - CHEBI:48947
  evidence_ids:
  - chemistry
  - validation
- check_id: authority-chemistry
  name: Independent exact molecular comparisons
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/308-chemistry.py
    > /private/tmp/am-review-session/308-chemistry.log
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; all nine inspected encodings match by exact key and mutual chirality-aware
    graph mapping.
  target_ids:
  - CHEBI:48947
  evidence_ids:
  - chemistry
- check_id: source-ledger
  name: Maintained source, producer and citation reconciliation
  status: passed
  required: false
  command: .venv/bin/python /private/tmp/am-review-session/308-ledger.py
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; fifteen hashes, six history events, ten ChEBI leads and one inherited
    MIBiG lead reconcile. Version 5 has one exact compound.
  target_ids:
  - CHEBI:48947
  evidence_ids:
  - owners
  - mibig
  - leads
- check_id: adapter-initial
  name: Initial structured catalog attempt
  status: failed
  required: false
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets > /private/tmp/am-review-session/308-adapter-datasets.txt
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 from sandbox DNS failure; approved network retry succeeded.
  target_ids:
  - CHEBI:48947
  evidence_ids:
  - adapter
- check_id: adapter-catalog
  name: Structured catalog retry
  status: passed
  required: false
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets > /private/tmp/am-review-session/308-adapter-datasets.txt
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no S. clavuligerus dataset; no S. coelicolor or S. albidoflavus
    substitution.
  target_ids:
  - CHEBI:48947
  evidence_ids:
  - adapter
- check_id: adapter-ampc
  name: Structured beta-lactamase context
  status: passed
  required: false
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset modulome --query ampC
    > /private/tmp/am-review-session/308-adapter-ampC.txt
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; e_coli/modulome/b4150 gene hit, zero iModulons. No summarize call
    applies.
  target_ids:
  - CHEBI:48947
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
  - CHEBI:48947
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
  - CHEBI:48947
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
  - CHEBI:48947
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
  - CHEBI:48947
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
  - CHEBI:48947
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
  - CHEBI:48947
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
  - CHEBI:48947
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
  - CHEBI:48947
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
  - CHEBI:48947
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/clavulanic-acid.yaml
  locator: Entire native YAML, including producer evidence note and complete history
  accessed_at: '2026-10-21T13:21:14Z'
  support: supports
  summary: The record is neutral clavulanic acid, with one exact producer/BGC assertion
    and explicitly inherited rather than compound-attached PMID 8088547 evidence.
    It has no quantitative MIC, clinical-approval assertion, molecular target object,
    resistance edge or causal graph.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:48947; PubChem:5280980; PDB-CCD:J01; KEGG:C06662/D07711; MIBiG:BGC0000845;
    KNApSAcK:C00018091
  locator: 308-authority-chemistry.json;308-chemistry.py/.log; official molfile and
    structure snapshots
  accessed_at: '2026-10-21T13:21:14Z'
  support: supports
  summary: Native SMILES and InChI, official ChEBI molfile, PubChem, PDB CCD stereochemical
    SMILES, both KEGG molfiles, versioned MIBiG structure and KNApSAcK SMILES all
    match HZZVJAQRINQKSD-PBFISZAISA-N with mutual chirality-aware atom mappings. Formula
    C8H9NO5, charge 0, average mass 199.162, monoisotopic mass 199.04807 and the 2R,3Z,5R
    identity agree. KNApSAcK displays a discordant legacy key HZZVJAQRINQKSD-LIJMCTQFNA-N,
    but its actual standard InChI and SMILES reproduce the native graph; this does
    not demonstrate a wrong native cross-reference.
  snapshot_sha256: 3f1267aba1f01d4458485da6acd75f3bfed6b045f448dd9e7d2bc198a39b3758
- evidence_id: authority
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:48947
  locator: '308-chebi.json: definition, names, clavam parent CHEBI:64509, antibacterial
    role and source accessions'
  accessed_at: '2026-10-21T13:17:02.947559Z'
  support: supports
  summary: Current ChEBI retains the native definition and neutral structure, chemical
    parent and antibacterial-drug role. Additional current host/pharmacologic roles
    are outside the adopted antibacterial slice. Twelve native names are source-concordant,
    including the generic Clavulanate alias. Current chemical xrefs remain source-concordant.
  snapshot_sha256: d5c1fecbd83c5bd9e4526b2bdc938d6b6807992783c3758fcfe049c44b3f42da
- evidence_id: anion
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:487869
  locator: '308-anion.json: preferred label, definition, formula/charge and conjugate-base
    relation'
  accessed_at: '2026-10-21T13:17:38.196868Z'
  support: supports
  summary: Current ChEBI separately defines clavulanate as the conjugate base of clavulanic
    acid, C8H8NO5 with charge −1. The acid entry simultaneously retains Clavulanate
    as a generic synonym inherited from KEGG. Thus the name is used contextually for
    the drug but is not unambiguous exact-form nomenclature for neutral acid. The
    proposed correction concerns synonym typing, not native stereochemistry or structure.
  snapshot_sha256: 7bfdfcec73495c93647163142770717d37477f2116ee60413e5a7aff3ba648b8
- evidence_id: mibig
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000845.5/annotations.json
  locator: Version 5 status, quality, compounds, taxonomy, loci evidence and legacy
    references
  accessed_at: '2026-10-21T13:18:27.937145Z'
  support: supports
  summary: Official version 5 is active/questionable and contains one compound, exact
    clavulanic acid, taxonomy S. clavuligerus ATCC 27064/NCBI 1901 and locus DS570624.1
    with Enzymatic assays and Heterologous expression. The compound evidence array
    is empty and PMID 8088547 is the first legacy reference. The native exact single-compound
    join, source quality and inherited-reference warning reproduce this scope. Old-schema
    GitHub JSON is corroborative history, not the version 5 provenance source.
  snapshot_sha256: 9c48b5d1d297fe776954fe51bf71d959d3d7e0df665b7e9062b51b14311f7b59
- evidence_id: isolation
  kind: primary_source
  reference: PMID:879738; DOI:10.1128/aac.11.5.852
  locator: Original 1977 pp852–857;308-1977-p1.png through p6.png, all six pages visually
    inspected
  accessed_at: '2026-10-21T13:18:41.201892Z'
  support: supports
  summary: The original report cultivates S. clavuligerus ATCC 27064 (NRRL 3585),
    identifies clavulanic-acid activity separately from co-produced cephamycin C and
    penicillin N, and isolates the product as sodium clavulanate. Figure 1 depicts
    the Z-(2R,5R) acid structure. Table 2 is sodium-clavulanate enzyme-inhibition
    I50 after defined preincubation, not MIC; Table 3 measures sodium-clavulanate-alone
    and beta-lactam combination MICs by microtiter broth. Intrinsic activity and potentiation
    are separately reported. Weak inhibition of chromosomal cephalosporinases and
    absent synergy in some tested organisms preclude a universal beta-lactamase claim.
    These sodium-salt results support active-moiety biology without pretending the
    tested solid was neutral acid.
  snapshot_sha256: be751d13e0d7b30478872f107b6cf486d0e296f703b426432603667b1324a125
- evidence_id: inactivation
  kind: primary_source
  reference: PMID:7041890; DOI:10.1042/bj1990779
  locator: Original 1981 pp779–787;308-1981-p1.png through p9.png, all nine pages
    visually inspected
  accessed_at: '2026-10-21T13:18:42.617923Z'
  support: supports
  summary: Time-dependent enzyme assays, substrate dilution and gel filtration distinguish
    transient from irreversible inhibition. TEM-2 and K. pneumoniae E70 enzymes partition
    into transient and irreversible fractions; P. mirabilis C889 shows a much smaller
    irreversible fraction; E. cloacae P99 shows no detected irreversible inactivation
    under these conditions. Table 2 and discussion support mechanism-based/suicide
    inhibition in susceptible enzymes, with proposed covalent-intermediate interpretations
    distinguished from direct structural observation. This is enzyme-specific evidence,
    not proof that every bacterial beta-lactamase is irreversibly inhibited. The native
    generic mechanism description is acceptable at that bounded class level.
  snapshot_sha256: 66244d1d285280839af61b0bcdc0696f82cf0708c4709f90a38682b2fa75ad67
- evidence_id: producer-2014
  kind: primary_source
  reference: PMID:25477926; DOI:10.1590/S1517-83822014000300022
  locator: '308-producer2014.xml: Methods, analytical procedure, control strain and
    selected production Results'
  accessed_at: '2026-10-21T13:17:38.197940Z'
  support: supports
  summary: ATCC 27064 is the control producer. Potassium clavulanate is the reference
    reagent; broth product is quantified by imidazole derivatization at 311 nm, and
    screening zones are measured in the presence of amoxicillin. These results corroborate
    culture production, not a purified neutral-acid MIC or independent absolute-stereo
    determination. The new DAUFPE3060 isolate and its 96% 16S similarity-based species
    assignment are separate from the native producer and are not imported.
  snapshot_sha256: ff7282241016e1bed07f9b7f86ffde81e895a128ac1d3dc47e855fd6c466b4b7
- evidence_id: legacy-paper
  kind: primary_source
  reference: PMID:8088547; DOI:10.1016/0378-1119(94)90036-1
  locator: Complete original abstract in 308-leads.json and PubMed
  accessed_at: '2026-10-21T13:17:03.961886Z'
  support: supports
  summary: The original abstract reports cloning and disruption of cla, with loss
    of clavulanic-acid production in starch/asparagine medium. This is relevant biosynthetic
    evidence, but the complete original methods and exact strain designation were
    not obtained. The native warning that this inherited reference is not independently
    established as support for the specific producer link is retained.
  snapshot_sha256: 3c4d0f2c3be27b92ce66854af2d6f5072c9591993db904bd71be01c5273196d3
- evidence_id: atcc
  kind: authority
  reference: https://www.atcc.org/products/27064
  locator: Official organism identity, strain designation and production summary
  accessed_at: '2026-10-21T13:17:04.669901Z'
  support: supports
  summary: ATCC 27064 is S. clavuligerus, strain NRRL 3585, and the catalog explicitly
    lists clavulanic-acid production. This independently resolves the strain label;
    it is not substituted for primary mechanism or BGC evidence.
  snapshot_sha256: 41770d31cb8cb9e58404cdf97e294af201526b9d5eef79a386bf215baa76d24b
- evidence_id: other-links
  kind: authority
  reference: KEGG:C06662/D07711; PDB-CCD:J01; KNApSAcK:C00018091; VSDB:1930; DrugCentral:669
  locator: 308-kegg-*.txt/.mol;308-pdb.json/.cif;308-knapsack.html;308-vsdb.html;308-drugcentral.html
  accessed_at: '2026-10-21T13:17:38.631245Z'
  support: supports
  summary: KEGG, PDB CCD and KNApSAcK resolve to the exact native molecule. VSDB1930
    resolves to clavulanic acid with exact formula, isomeric SMILES and key. DrugCentral669
    is clavulanic-acid drug context, with broad salt aliases that are not copied into
    native exact names. HMDB XML and direct DrugBank returned 403; independent CAS,
    Beilstein and Reaxys registry bodies were not obtained. No unverified external
    alias or host target is adopted.
  snapshot_sha256: fea62c45a0c400cbceeb8cd4ef5970540eddcd73f346f626e2c0e2b1b00a331e
- evidence_id: documents
  kind: authority
  reference: Patent:DE2517316; Wikipedia:Clavulanic_Acid
  locator: 308-patent.html title and strain/compound discussion;308-wikipedia.html
    title and mechanism context
  accessed_at: '2026-10-21T13:17:04.088010Z'
  support: context_only
  summary: DE2517316A1 covers clavulanic acid, salts and esters and names the producing
    strain; the broader patent scope is appropriate for a document link, not an exact
    chemical assertion. Wikipedia resolves to the expected article and was used only
    as document context, not primary evidence. Neither document establishes regulatory
    approval or exact assay material by title alone.
  snapshot_sha256: b6c6e2039ea0025bf22df259f3ed6a268d77d980d5672adfa35db769fc2947b7
- evidence_id: leads
  kind: database
  reference: Ten adopted ChEBI MED citations plus inherited PMID8088547
  locator: 308-lead-dispositions.json;308-leads.json
  accessed_at: '2026-10-21T13:21:14Z'
  support: supports
  summary: All eleven adopted/inherited leads have explicit dispositions. Three biosynthesis/production
    reviews remain secondary. Original host behavior, T-cell/IgE and duodenal studies
    do not establish antimicrobial mechanism. Clinical PK/UTI studies concern amoxicillin
    combinations, not clavulanic-acid monotherapy or free-acid approval. Only the
    2014 producer paper was additionally inspected at Methods/Results depth. Newly
    added current ChEBI bibliography was not treated as frozen adopted evidence.
  snapshot_sha256: d73f5ba88090cef198fc3751512d64379e2d36d3de7248a06123cda639257e1e
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/modulome
  locator: 308-adapter-datasets.txt;308-adapter-ampC.txt
  accessed_at: '2026-10-21T13:21:14Z'
  support: context_only
  summary: The catalog and ampC query preceded mechanism web research. No S. clavuligerus
    dataset is covered. The E. coli b4150/ampC hit is gene-catalog context, with zero
    iModulons; it does not prove clavulanate susceptibility or connect the native
    producer to a different Streptomyces species.
  snapshot_sha256: 5e1b839013d8c4f1ee297e57896de266f5deeea937de15421f8074542b1a7ab3
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv;data/raw/mibig_producers.tsv;scripts/extract_source_inventory.py;scripts/extract_mibig_producers.py;scripts/seed_from_sources.py;conf/sources.yaml
  locator: 308-source-audit.json; maintained synonym and MIBiG transformations
  accessed_at: '2026-10-21T13:21:14Z'
  support: supports
  summary: The ChEBI row owns the exact alias and its seeder classification. Existing
    conf/sources.yaml synonym_exclusions can prevent this exact alias from recurring.
    MIBiG extraction carries locus evidence to the entry and retains the first legacy
    reference; the seeder labels a one-compound entry COMPOUND_SPECIFIC and explicitly
    qualifies inherited evidence. All fifteen captured inputs and six history events
    remain unchanged.
  snapshot_sha256: bc8c013ca79dad99af591d81bc70c5419e66fcfb66c21f45d4066f531fbacf38
- evidence_id: validation
  kind: validation
  reference: Documented validators and independent chemistry checks
  locator: 308-focused-results.json;308-focused-run.log;308-schema.log;308-strict.log;308-authority-chemistry.json;308-source-audit.json
  accessed_at: '2026-10-21T13:21:14Z'
  support: supports
  summary: Native schema, strict and molecular consistency checks, authority comparisons
    and source reconciliation pass. Initial adapter DNS failure is preserved separately;
    shared full-corpus gates remain separate.
  snapshot_sha256: 5c6a3b07eaaccef5192f98b53a74dc8977738d5e968ff6266a69499e8e7a9523
- evidence_id: search
  kind: search
  reference: Exact record and source discovery
  locator: Ignored-inclusive rg for CHEBI:48947,BGC0000845,8088547,HZZVJAQRINQKSD
    in curation,conf,scripts,data/raw; exact adopted MED query and original producer/enzyme
    searches
  accessed_at: '2026-10-21T13:21:14Z'
  support: context_only
  summary: Ignored files were included. The ten adopted ChEBI records and inherited
    MIBiG record were resolved before source selection. Newly discovered source bibliography
    is not silently promoted to native evidence.
  snapshot_sha256: 930b744ba7c6977a3884b4ea00d790f8e00a47fd6246db26007c35e07a40de7a
  search_scope: Ignored-inclusive rg for CHEBI:48947,BGC0000845,8088547,HZZVJAQRINQKSD
    in curation,conf,scripts,data/raw; exact adopted MED query and original producer/enzyme
    searches
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral 2R,3Z,5R molecule
  outcome: supported
  summary: Independent structures and atom mappings agree with native acid; measured
    salt forms retain explicit boundaries.
  target_ids:
  - CHEBI:48947
  evidence_ids:
  - chemistry
  - authority
  - isolation
- assessment_id: alias
  area: consistency
  topic: Clavulanate as exact neutral-acid synonym
  outcome: concern
  summary: The source uses the alias generically but independently defines the anion
    as a distinct charged entity. Exact typing is too strong for unambiguous form
    matching.
  target_ids:
  - CHEBI:48947
  evidence_ids:
  - anion
  - authority
- assessment_id: producer
  area: evidence
  topic: Exact ATCC 27064 producer and BGC scope
  outcome: supported
  summary: Versioned MIBiG single-compound join, original isolation and official strain
    identity support the assertion. Native questionable quality and inherited-reference
    limit are accurate.
  target_ids:
  - CHEBI:48947
  evidence_ids:
  - mibig
  - isolation
  - atcc
  - legacy-paper
  - producer-2014
- assessment_id: mechanism
  area: evidence
  topic: Beta-lactamase inhibition and antibacterial classification
  outcome: supported
  summary: Primary evidence supports enzyme-dependent mechanism-based inhibition and
    measured intrinsic/synergistic activity; no universal irreversible-inhibition
    claim is inferred.
  target_ids:
  - CHEBI:48947
  evidence_ids:
  - isolation
  - inactivation
  - authority
- assessment_id: xref
  area: identity
  topic: Chemical, drug and document link scopes
  outcome: supported
  summary: Inspected exact chemical graphs agree; broader drug/document links remain
    in appropriate fields. Unavailable registry bodies and a KNApSAcK displayed-key
    conflict remain limitations.
  target_ids:
  - CHEBI:48947
  evidence_ids:
  - chemistry
  - other-links
  - documents
- assessment_id: provenance
  area: provenance
  topic: All adopted leads, maintained owners and history
  outcome: supported
  summary: Ten ChEBI and one MIBiG lead have explicit checked dispositions. Fifteen
    input hashes and six history events are preserved.
  target_ids:
  - CHEBI:48947
  evidence_ids:
  - leads
  - owners
  - mibig
- assessment_id: completeness
  area: completeness
  topic: Optional primary mechanism and producer evidence
  outcome: supported
  summary: Original papers could strengthen claim-level evidence after separate curation.
    No missing optional graph, clinical status or MIC is treated as a defect.
  target_ids:
  - CHEBI:48947
  evidence_ids:
  - record
  - isolation
  - inactivation
- assessment_id: schema
  area: schema
  topic: Focused native validation
  outcome: supported
  summary: Native schema/strict checks pass; chemical and scientific review remain
    distinct from them.
  target_ids:
  - CHEBI:48947
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: chebi-48947-clavulanate-exact-alias-form-ambiguity
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Clavulanate exact alias obscures the acid–anion distinction
  description: The native neutral acid calls Clavulanate an EXACT_SYNONYM, although
    the inspected authority separately defines clavulanate as the monoanion CHEBI:487869.
    Current ChEBI and KEGG also use the word generically for the drug, so this is
    a bounded alias-typing ambiguity rather than evidence of a wrong native molecular
    identity.
  target_ids:
  - CHEBI:48947
  field_paths:
  - synonyms[6].synonym_text
  - synonyms[6].synonym_type
  evidence_ids:
  - anion
  - authority
  - chemistry
  - owners
  rule_id: 'review-checklist: Identity and synonym accuracy'
  native_severity: Minor exact-form nomenclature ambiguity
  normalization_reason: Native structure, formula, charge and identity remain correct.
    The concern is limited to an overstrong exact alias that can conflate a conjugate
    base with its acid.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained synonym_exclusions for CHEBI:48947
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted source alias
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Synonym generation and classification
actions:
- action_id: A1
  description: Exclude Clavulanate from automatically generated exact aliases for
    CHEBI:48947 using the existing maintained synonym_exclusions entry, or separately
    implement a reproducible RELATED_SYNONYM override if preserving contextual search
    coverage is desired. Keep neutral acid structure and canonical name unchanged.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:48947
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained synonym_exclusions for CHEBI:48947
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted source alias
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Synonym generation and classification
  acceptance_checks:
  - Regeneration must no longer publish bare Clavulanate as an exact neutral-acid
    alias; retain traceable source provenance and distinguish CHEBI:487869 charge
    −1 from CHEBI:48947 charge 0.
  - Preserve HZZVJAQRINQKSD-PBFISZAISA-N, formula C8H9NO5, exact stereochemistry and
    producer history. Rerun documented schema/strict validation and required corpus
    gates after authorized curation.
limitations:
- Original 1977 material was isolated and assayed as sodium clavulanate. The 2014
  production study uses a potassium-clavulanate reference and an imidazole assay;
  these are active-moiety/producer evidence, not measurements on isolated neutral
  acid.
- Full original PMID 8088547 methods were not obtained. Its complete abstract supports
  biosynthetic disruption, but exact strain/method attribution is not substituted
  for the native inherited-reference caution.
- The original 1981 inhibitor batches were not independently structurally characterized
  here. Enzyme preparations and reaction conditions are explicit; the reversible/irreversible
  outcome is enzyme-specific.
- All ten adopted ChEBI records and inherited MIBiG citation were resolved; most ChEBI
  leads were abstract-only, with the 2014 producer Methods and selected Results inspected.
  New current ChEBI citations beyond the frozen ten were not exhaustively reviewed.
- HMDB and DrugBank returned 403; independent CAS, Beilstein and Reaxys bodies were
  not obtained. KNApSAcK displayed key differs from its own matching standard InChI/SMILES.
- Unversioned MIBiG JSON returned 404; official BGC0000845.5/annotations.json succeeded.
  Initial PMC PDF responses were browser-challenge HTML, and publisher PDF returned
  403; all six 1977 and nine 1981 original journal page scans were successfully obtained
  and visually inspected.
- The patent title and relevant strain/compound passages were inspected, not every
  salt/ester example or legal claim. Wikipedia was checked as a document link and
  not used as primary scientific evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native or maintained source was edited; original capture hashes remain unchanged.
- Missing optional primary evidence enrichment is not reported as a producer or mechanism
  defect.
- The supported acid, its solution-phase conjugate base and isolated sodium/potassium
  assay salts are kept distinct.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links: []
tags:
- record-review
- clavulanic-acid
- exact-form
- producer-evidence
```
