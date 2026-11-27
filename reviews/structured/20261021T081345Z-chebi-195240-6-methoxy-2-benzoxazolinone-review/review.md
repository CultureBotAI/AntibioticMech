# Review of CHEBI:195240 (6-methoxy-2-benzoxazolinone)

- Review: 20261021T081345Z-chebi-195240-6-methoxy-2-benzoxazolinone-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:05:04Z
- Finished UTC: 2026-10-21T08:13:45Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The stored and current ChEBI SMILES omit lactam [nH] and fail chemical parsing. PubChem and KNApSAcK support a valid lactam encoding; the mobile-H InChI normalizes a lactim tautomer to the same key. Primary activity and recombinant bacterial DHFR inhibition offer a qualified enrichment opportunity, with negative and weak-activity assay results retained. Enzyme inhibition does not establish causal whole-cell target engagement.

## Scope And Provenance

Entire record, maintained-source ownership, structural encodings and ontology terms, external xrefs, all adopted PMID leads, and exact-compound primary activity and mechanism with assay and tautomer boundaries.

Selection: Path-ordered unreviewed queue index 061; exactly one record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:195240 | data/antibiotics/antibacterial/6-methoxy-2-benzoxazolinone.yaml | generated | 6-methoxy-2-benzoxazolinone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record LinkML validation | passed | True | CHEBI:195240 | Exit 0; No issues found. |
| Documented closed-schema validation | passed | True | CHEBI:195240 | Exit 0; one file, zero ERROR rows. |
| Independent structure and minted-identifier comparison | failed | False | CHEBI:195240 | Exit 1 because native SMILES fails kekulization. Valid lactam candidate and PubChem agree; stored mobile-H InChI also normalizes a lactim graph to the same key. Mint reproduces. |
| Current source term, structural and xref-string comparison | passed | False | CHEBI:195240 | Exit 0 for non-obsolete term/parents, native roles, synonyms, InChI and normalized xref strings. Current source SMILES is explicitly recognized as invalid. Independent KNApSAcK lactam and ChemSpider key checked. |
| Structured expression-context relevance | not_applicable | False | CHEBI:195240 | The current record contains no gene, protein, regulator, pathway, stress response or transcriptomic dataset annotation. Genes mentioned only in uncurated source leads are not existing assertions needing module validation. |
| Authoritative full QC | failed | True | CHEBI:195240 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:195240 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:195240 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:195240 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:195240 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:195240 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:195240 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:195240 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:195240 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Lactam representation and tautomer normalization

identity: concern. Targets: CHEBI:195240.

Native SMILES is invalid; independent lactam sources establish a precise repair. Standard InChI permits mobile-H lactim normalization and is not proof of a unique tautomer graph.

### Term, parents and antimicrobial roles

grounding: supported. Targets: CHEBI:195240.

Exact current term and two native parents reproduce. Direct primary evidence supports broad antibacterial/antifungal filing with condition-specific negative or weak results retained.

### Coixol synonym classification

grounding: unknown. Targets: CHEBI:195240.

Coixol string denotes this compound and BRAND_NAME reproduces the source; historical brand semantics were not established independently. No confirmed synonym-type defect is asserted.

### External target checks

grounding: unknown. Targets: CHEBI:195240.

KNApSAcK and ChemSpider agree; FooDB/HMDB/CAS exact external targets remain incompletely resolved.

### Biochemical DHFR inhibition versus cellular causality

scope: supported. Targets: CHEBI:195240.

Primary recombinant bacterial enzyme inhibition is available and must be qualified as a candidate cellular mechanism. Docking does not establish binding; growth inhibition alone does not prove bactericidality.

### Specific primary evidence opportunity

completeness: concern. Targets: CHEBI:195240.

Verified primary activity and biochemical inhibition support bounded evidence enrichment. Optional emptiness alone is not an error.

### Natural occurrence and production

representation: unknown. Targets: CHEBI:195240.

No producer is asserted. Database plant occurrence, degradation and biosynthesis predictions do not by themselves establish exact-compound biosynthesis in a named producer.

### Adjacent BOA detoxification literature

scope: unknown. Targets: CHEBI:195240.

The adopted FDB2 abstract concerns BOA. An exact MBOA resistance mechanism needs direct source verification before curation.

### Clinical, graph and dataset annotations

representation: not_applicable. Targets: CHEBI:195240.

No such objects are asserted. Mouse efficacy is preclinical, and host or transcriptomic responses are not direct antimicrobial-target evidence.

### Generated field ownership and history

ownership: supported. Targets: CHEBI:195240.

Maintained source row and mint reproduce, with four chronological seed/reseed events. Source-owned repair must survive regeneration.

### Schema success and chemistry failure

schema: concern. Targets: CHEBI:195240.

Focused schema checks pass; malformed SMILES remains a major barrier to native REVIEWED sign-off.

## Findings

### F1: Source-derived SMILES omits lactam [nH] and cannot be parsed

major / open / confirmed; issue key: chebi-195240-invalid-smiles-missing-lactam-hydrogen.

chemical_structure.smiles COc1ccc2nc(=O)oc2c1 fails kekulization. Candidate COc1ccc2[nH]c(=O)oc2c1 agrees with independent PubChem and KNApSAcK lactam structures, native standard key, formula and masses. Stored InChI can also generate a lactim tautomer; normalized key equality must not be described as graph equality. Adopted and current ChEBI share the defect.

### F2: Primary exact-compound activity and qualified DHFR evidence are available

minor / open / confirmed; issue key: chebi-195240-primary-activity-and-biochemical-evidence-completeness.

The source-seeded record lacks claim-level evidence. Verified primary observations offer a specific enrichment opportunity, with assay-specific negative results, censored MICs and tentative cellular mechanism retained.

## Recommended Actions And Acceptance Checks

### A1

Repair maintained source handling with independently supported lactam SMILES COc1ccc2[nH]c(=O)oc2c1, then regenerate reproducibly.

- Require valid parsing, native MKMCJLMBVKHUMS-UHFFFAOYSA-N, C8H7NO3, charge 0, masses 165.148/165.04259, and graph agreement with independent lactam structures. Preserve mobile-H tautomer normalization provenance rather than claiming InChI uniquely encodes the lactam.
- Do not patch only generated YAML or change correct InChI/key/formula to accommodate malformed input. Preserve evidence and maintained provenance of the correction.
- Use authorized curation/regeneration and validated history; complete schema, strict, source reproduction, corpus integrity and QC gates before native REVIEWED.

### A2

Curate claim-level primary activity and recombinant DHFR inhibition with explicit assay and causal limits.

- Preserve exact MBOA versus BOA and other indoles; retain strain, medium, dose, incubation and censored inequality for each verified observation. Keep 1993 negative coixol result and weak 1997 bacterial results as context; inspect original tables before quantitative curation where only extracted text was available.
- Represent 2026 DHFR as directly tested biochemical inhibition and a candidate cellular mechanism, not proven binding, a docking-only result, universal bactericidal action or established whole-cell target. Do not invent an IC50 or UniProt accession.
- Keep mouse S. Typhimurium efficacy separate from S. Typhi in-vitro assays and human clinical efficacy. Resolve source concentration/unit inconsistencies and retrieve supplementary tables before importing additional numerical results.
- Do not transfer BOA detoxification, host reproductive phenotypes, insect binding predictions or oomycete expression associations to bacterial target/resistance claims. Verify biosynthesis before producer_organisms annotation.
- Use validated writer/history and required native gates before REVIEWED sign-off.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/6-methoxy-2-benzoxazolinone.yaml; Entire generated record | supports | Read definition, eight synonyms, two parents, two activity roles, full structure, five xrefs, source concept and four seed/reseed events. No primary evidence, mode, target, activity observation, producer, resistance, clinical, graph or dataset object is asserted. |
| inventory | data/raw/chebi_antimicrobials.tsv; Full CHEBI:195240 row, manifest and ignored-inclusive maintained-input search | supports | Adopted row reproduces malformed SMILES and intended InChI/key, formula, masses, synonyms, roles and xrefs. Ten imported PMID leads are bibliographic inputs, not automatic claim evidence. No exact curator override was found in the ignored-inclusive maintained-input search. |
| ownership | scripts/extract_source_inventory.py; ChEBI structure import; scripts/seed_from_sources.py structure_from_chebi and normalize_xref | supports | Extractor copies source SMILES and seeder reproduces it. FooDB FDB identifiers deliberately normalize from foodb.food to foodb.compound. Correct structural encoding through maintained source handling and reproducible regeneration; primary annotations belong to curator-owned fields with validated history. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:195240; 061-chebi.html visible identity/structure | supports | Current ChEBI repeats malformed COc1ccc2nc(=O)oc2c1. Its source repetition is not a chemical validity check. |
| ontology | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_195240; 061-ols.json, 061-parents.json, 061-has_role.json | supports | Exact non-obsolete term has aromatic-ether and benzoxazole parents; native antibacterial and antifungal roles are present. Eight synonym strings and all native xrefs after documented FooDB normalization match. Coixol BRAND_NAME is source-derived; its historical brand status was not independently established. OLS repeats invalid SMILES. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/10772/property/InChI,InChIKey,MolecularFormula,CanonicalSMILES/JSON; 061-pubchem.json | supports | CID 10772 valid lactam SMILES agrees with repair candidate and recorded standard key, formula and neutral charge. |
| knapsack | https://www.knapsackfamily.com/knapsack_core/information.php?word=C00036627; 061-knapsack.html identity and organism sections | supports | Explicit SMILES COc1ccc2[nH]c(=O)oc2c1, InChI/key, C8H7NO3 and CAS 532-91-2 support the intended lactam. Plant-occurrence entries and predicted biosynthesis starting substances are not proof of an exact producer biosynthetic pathway. |
| xref-limits | chemspider:10317; foodb.compound:FDB015492; hmdb:HMDB0036582; cas:532-91-2; 061-chemspider.html and 061-fetch-results.json | context_only | ChemSpider structured identity matches native InChI/key and PubChem CID 10772. FooDB and HMDB returned 403; CAS returned an application shell. Those three external target structures remain unverified independently. |
| primary2001 | PMID:11701394; DOI:10.1016/S1532-0456(01)00264-2; complete abstract in 061-primarycore.json | supports | Exact 6-MBOA shows Proteus vulgaris antibacterial activity and activity against Mycosphaerella arachidicola, Botrytis cinerea and Physalospora piricola. S. aureus/B. subtilis outcomes belong to 5-methoxytryptamine. Abstract access gives no numerical MIC or full assay conditions. |
| primary2002 | PMID:12106902; DOI:10.1016/S1532-0456(02)00071-6; complete abstract in 061-primarycore.json | context_only | 6-MBOA is strongest tested against the three named fungi and HIV-1 reverse transcriptase. The strongest Agrobacterium result belongs to 5-methoxyindole-3-acetic acid. Fungal potato-dextrose agar cannot be assigned to the bacterial assay. Reverse-transcriptase inhibition alone is not antiviral cellular efficacy. |
| primary1993 | https://doi.org/10.3136/nskkk1962.40.5_353; 061-primary1993.pdf; English abstract and Japanese methods/results | context_only | Study reports no antimicrobial activity for isolated coixol while adlay extracts are active. The coixol test appears in the B. subtilis disc-assay context; coixol dose is not supplied. Extract MICs cannot be assigned to pure coixol, nor generalized across assays. |
| primary1997 | https://doi.org/10.1021/jf9608581; Author-uploaded full text https://www.researchgate.net/publication/231555242_Antimicrobial_Activity_of_Natural_2-Benzoxazolinones_and_Related_Derivatives ; methods/Table 1 textual rendering | context_only | Compound 2 MBOA has MIC &gt;1000 µg/mL against S. aureus ATCC 25923 and E. coli ATCC 25922, and 450 µg/mL against Candida albicans. Tests use 35 °C/24h; bacterial medium is Mueller-Hinton. The broad positive abstract needs these censored results. SAR is not molecular-target evidence. Original table pixels were not retrieved; values require visual confirmation before quantitative native curation. |
| primary2026 | PMID:42179630; DOI:10.1021/acsomega.5c12161; PMC13191540 full XML, methods/results | supports | Commercial 97% MBOA has Salmonella Typhi MTCC734 MIC &gt;0.25 and ≤0.5 mg/mL, most clinical isolates &gt;0.5 and ≤1 mg/mL, and several &gt;1 mg/mL. MHB microdilution uses 5×10^5 CFU/mL, overnight 37 °C. Recombinant S. Typhi DHFR NADPH assay shows concentration-dependent inhibition at 0.01–0.1 mg/mL; human DHFR comparison and docking accompany it. This supports biochemical inhibition, not direct binding or proven whole-cell target causality. Mouse efficacy uses S. Typhimurium OSS535, not S. Typhi. |
| all-adopted-leads | PMID:11701394; PMID:16154300; PMID:16425448; PMID:16478219; PMID:18160321; PMID:19302487; PMID:2203893; PMID:22982975; PMID:24402687; PMID:26940061; 061-primarycore.json and 061-lead-dispositions.json; all ten complete abstracts inspected | context_only | 11701394 supplies direct antimicrobial findings. Six leads concern sheep/rodent reproduction or photoperiod (16154300,18160321,2203893,22982975,24402687,26940061);16425448 concerns lettuce germination and alpha-amylase induction;16478219 concerns soil degradation.19302487 investigates F. verticillioides FDB2/BOA biotransformation; BOA-specific evidence must not become an MBOA resistance assertion. |
| additional-leads | PMID:28279674; PMID:32517283; PMID:33048595; PMID:35113672; PMID:35422782; PMID:7025209; 061-extra-core.json; six additional current ChEBI leads | context_only | Five complete abstracts inspected;7025209 resolves but has no abstract.28279674 is vole reproduction;32517283 models insect chemosensory-protein binding;35422782 measures vole cecal community changes, not direct killing of each taxon.33048595 reports Pythium growth suppression and increased corn disease in some conditions;35113672 reports Phytophthora sojae growth/chemotaxis effects and transcriptional pathway associations. These oomycetes are not bacteria; expression associations do not establish direct protein targets. Full papers were not inspected. |
| chemistry | RDKit and hashlib calculations; 061-chemistry.py and 061-chemistry.json | supports | Native SMILES fails kekulization. Candidate [nH] lactam and PubChem parse identically; stored InChI parses as lactim COc1ccc2nc(O)oc2c1. Both valid tautomers share the standard mobile-H InChIKey, C8H7NO3, charge 0 and masses 165.148/165.04259. Key equality does not prove identical tautomer graphs. Mint reproduces; standalone script exits 1 for native-SMILES failure. |
| source-check | Focused current-source assertions; 061-source-check.py and 061-source-check.json | supports | Exit 0 verifies source reproduction, native term/parents/roles, synonyms, normalized xrefs and identity strings. It explicitly expects defective source SMILES to fail parsing; this success does not replace the failed chemistry gate. |
| validation | just validate; just validate-strict; Actual isolated batch 007 executions; 061-strict.tsv | supports | Both documented focused gates exited0; strict scanned one record with zero ERROR rows. Schema success does not detect the malformed chemical graph. |
| search | Ignored-inclusive local and bounded public discovery; 061-local-hits.txt; exact-name, coixol and MBOA queries | context_only | Read all adopted abstract leads, current authority identities and selected primary activity/mechanism studies. Search does not establish universal absence of other mechanisms. |

## Limits And Additional Notes

- All ten adopted PMID abstracts were read. Six additional current ChEBI leads were resolved; five had abstracts and 7025209 had none. The 2001/2002 antimicrobial reports remain abstract-only; their numerical conditions cannot be inferred.
- The 2026 full XML was read, but ACS supplementary download returned 403. Methods and results differ in time-kill concentration/multiple wording; Figure 7 labels mouse doses mg/mL although methods use mg/kg. These source limits must be resolved before importing affected measurements. No direct binding, causal cellular target, clinical safety or human efficacy was established.
- The 1997 author-uploaded full text was read through a textual rendering; original table pixels were not retrieved. A university PDF endpoint instead returned an HTML challenge, preserved under 061-primary1997.pdf despite the suffix. Quantitative native annotation requires visual table confirmation.
- FooDB/HMDB returned 403 and CAS an application shell. Coixol BRAND_NAME historical semantics remain unverified. Source-string reproduction is narrower than independent authority validation.
- Current ChEBI/OLS repeat the invalid SMILES; chemistry intentionally exits 1. Schema success does not resolve the defect. Native REVIEWED remains blocked by the major structure issue and incomplete required gates; this bounded review is not an exhaustive literature inventory.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Only scratch review artifacts were written; native records and maintained inputs were unchanged. All 13 captured input hashes were rechecked before draft creation.
- The first combined scratch display returned the later display command status; the chemistry script was rerun alone and its actual exit 1 is the recorded result.
- Coordinator independently reproduced the native parsing failure and confirmed that the [nH] lactam repair gives the recorded key/formula while the stored mobile-H InChI renders a lactim graph. No native structure was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T081345Z-chebi-195240-6-methoxy-2-benzoxazolinone-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of CHEBI:195240 (6-methoxy-2-benzoxazolinone)
started_at: '2026-10-21T08:05:04Z'
finished_at: '2026-10-21T08:13:45Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Major invalid source-derived SMILES blocks native REVIEWED structural
  consistency; intended compound and antibacterial/antifungal classification supported
scientific_review: true
summary: The stored and current ChEBI SMILES omit lactam [nH] and fail chemical parsing.
  PubChem and KNApSAcK support a valid lactam encoding; the mobile-H InChI normalizes
  a lactim tautomer to the same key. Primary activity and recombinant bacterial DHFR
  inhibition offer a qualified enrichment opportunity, with negative and weak-activity
  assay results retained. Enzyme inhibition does not establish causal whole-cell target
  engagement.
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
  - path: data/antibiotics/antibacterial/6-methoxy-2-benzoxazolinone.yaml
    sha256: 42388a568a1b3772d0dd20d9657218f67bbb82c1d0d8c142a2464590d3745028
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
  description: Entire record, maintained-source ownership, structural encodings and
    ontology terms, external xrefs, all adopted PMID leads, and exact-compound primary
    activity and mechanism with assay and tautomer boundaries.
  selection: Path-ordered unreviewed queue index 061; exactly one record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:195240
targets:
- target_id: CHEBI:195240
  path: data/antibiotics/antibacterial/6-methoxy-2-benzoxazolinone.yaml
  label: 6-methoxy-2-benzoxazolinone
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
  - CHEBI:195240
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/6-methoxy-2-benzoxazolinone.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented closed-schema validation
  status: passed
  required: true
  summary: Exit 0; one file, zero ERROR rows.
  target_ids:
  - CHEBI:195240
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/6-methoxy-2-benzoxazolinone.yaml --out /private/tmp/am-review-session/061-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Independent structure and minted-identifier comparison
  status: failed
  required: false
  summary: Exit 1 because native SMILES fails kekulization. Valid lactam candidate
    and PubChem agree; stored mobile-H InChI also normalizes a lactim graph to the
    same key. Mint reproduces.
  target_ids:
  - CHEBI:195240
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/061-chemistry.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: source-check
  name: Current source term, structural and xref-string comparison
  status: passed
  required: false
  summary: Exit 0 for non-obsolete term/parents, native roles, synonyms, InChI and
    normalized xref strings. Current source SMILES is explicitly recognized as invalid.
    Independent KNApSAcK lactam and ChemSpider key checked.
  target_ids:
  - CHEBI:195240
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/061-source-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - source-check
- check_id: imodulondb
  name: Structured expression-context relevance
  status: not_applicable
  required: false
  summary: The current record contains no gene, protein, regulator, pathway, stress
    response or transcriptomic dataset annotation. Genes mentioned only in uncurated
    source leads are not existing assertions needing module validation.
  target_ids:
  - CHEBI:195240
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:195240
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
  - CHEBI:195240
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
  - CHEBI:195240
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
  - CHEBI:195240
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
  - CHEBI:195240
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
  - CHEBI:195240
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
  - CHEBI:195240
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
  - CHEBI:195240
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
  - CHEBI:195240
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/6-methoxy-2-benzoxazolinone.yaml
  locator: Entire generated record
  accessed_at: '2026-10-21T08:11:33Z'
  support: supports
  summary: Read definition, eight synonyms, two parents, two activity roles, full
    structure, five xrefs, source concept and four seed/reseed events. No primary
    evidence, mode, target, activity observation, producer, resistance, clinical,
    graph or dataset object is asserted.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Full CHEBI:195240 row, manifest and ignored-inclusive maintained-input
    search
  accessed_at: '2026-10-21T08:11:33Z'
  support: supports
  summary: Adopted row reproduces malformed SMILES and intended InChI/key, formula,
    masses, synonyms, roles and xrefs. Ten imported PMID leads are bibliographic inputs,
    not automatic claim evidence. No exact curator override was found in the ignored-inclusive
    maintained-input search.
- evidence_id: ownership
  kind: record_content
  reference: scripts/extract_source_inventory.py
  locator: ChEBI structure import; scripts/seed_from_sources.py structure_from_chebi
    and normalize_xref
  accessed_at: '2026-10-21T08:11:33Z'
  support: supports
  summary: Extractor copies source SMILES and seeder reproduces it. FooDB FDB identifiers
    deliberately normalize from foodb.food to foodb.compound. Correct structural encoding
    through maintained source handling and reproducible regeneration; primary annotations
    belong to curator-owned fields with validated history.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:195240
  locator: 061-chebi.html visible identity/structure
  accessed_at: '2026-10-21T08:11:33Z'
  support: supports
  summary: Current ChEBI repeats malformed COc1ccc2nc(=O)oc2c1. Its source repetition
    is not a chemical validity check.
  snapshot_sha256: 2cd5a89452b43a1bfbcfc12c2b86027b968efd460f6fb0473d469b61c0c8b2c6
- evidence_id: ontology
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_195240
  locator: 061-ols.json, 061-parents.json, 061-has_role.json
  accessed_at: '2026-10-21T08:11:33Z'
  support: supports
  summary: Exact non-obsolete term has aromatic-ether and benzoxazole parents; native
    antibacterial and antifungal roles are present. Eight synonym strings and all
    native xrefs after documented FooDB normalization match. Coixol BRAND_NAME is
    source-derived; its historical brand status was not independently established.
    OLS repeats invalid SMILES.
  snapshot_sha256: d4e3902422593aed88bb53884238fed83e744bb1e281b10e501cf82793ef5fc1
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/10772/property/InChI,InChIKey,MolecularFormula,CanonicalSMILES/JSON
  locator: 061-pubchem.json
  accessed_at: '2026-10-21T08:11:33Z'
  support: supports
  summary: CID 10772 valid lactam SMILES agrees with repair candidate and recorded
    standard key, formula and neutral charge.
  snapshot_sha256: 0a0ce78223e3af969db90515133dce175841d585f91ae72f90dc0ecef7fe8f84
- evidence_id: knapsack
  kind: database
  reference: https://www.knapsackfamily.com/knapsack_core/information.php?word=C00036627
  locator: 061-knapsack.html identity and organism sections
  accessed_at: '2026-10-21T08:11:33Z'
  support: supports
  summary: Explicit SMILES COc1ccc2[nH]c(=O)oc2c1, InChI/key, C8H7NO3 and CAS 532-91-2
    support the intended lactam. Plant-occurrence entries and predicted biosynthesis
    starting substances are not proof of an exact producer biosynthetic pathway.
  snapshot_sha256: 9c7fed39795c549ca232b4014b97f8ac4d5bb16492584eb8fabedae6555a79b6
- evidence_id: xref-limits
  kind: database
  reference: chemspider:10317; foodb.compound:FDB015492; hmdb:HMDB0036582; cas:532-91-2
  locator: 061-chemspider.html and 061-fetch-results.json
  accessed_at: '2026-10-21T08:11:33Z'
  support: context_only
  summary: ChemSpider structured identity matches native InChI/key and PubChem CID
    10772. FooDB and HMDB returned 403; CAS returned an application shell. Those three
    external target structures remain unverified independently.
  snapshot_sha256: b96ec4eb3f6b57da620a7edd00ebc9d379ae6f96f6064ac56d8d9d8e066c1411
- evidence_id: primary2001
  kind: primary_source
  reference: PMID:11701394
  locator: DOI:10.1016/S1532-0456(01)00264-2; complete abstract in 061-primarycore.json
  accessed_at: '2026-10-21T08:11:33Z'
  support: supports
  summary: Exact 6-MBOA shows Proteus vulgaris antibacterial activity and activity
    against Mycosphaerella arachidicola, Botrytis cinerea and Physalospora piricola.
    S. aureus/B. subtilis outcomes belong to 5-methoxytryptamine. Abstract access
    gives no numerical MIC or full assay conditions.
  snapshot_sha256: 8ee3580c47a39032350f69074c283782db991ad48f267bbb0cd8cdfe533d9767
- evidence_id: primary2002
  kind: primary_source
  reference: PMID:12106902
  locator: DOI:10.1016/S1532-0456(02)00071-6; complete abstract in 061-primarycore.json
  accessed_at: '2026-10-21T08:11:33Z'
  support: context_only
  summary: 6-MBOA is strongest tested against the three named fungi and HIV-1 reverse
    transcriptase. The strongest Agrobacterium result belongs to 5-methoxyindole-3-acetic
    acid. Fungal potato-dextrose agar cannot be assigned to the bacterial assay. Reverse-transcriptase
    inhibition alone is not antiviral cellular efficacy.
  snapshot_sha256: 8ee3580c47a39032350f69074c283782db991ad48f267bbb0cd8cdfe533d9767
- evidence_id: primary1993
  kind: primary_source
  reference: https://doi.org/10.3136/nskkk1962.40.5_353
  locator: 061-primary1993.pdf; English abstract and Japanese methods/results
  accessed_at: '2026-10-21T08:11:33Z'
  support: context_only
  summary: Study reports no antimicrobial activity for isolated coixol while adlay
    extracts are active. The coixol test appears in the B. subtilis disc-assay context;
    coixol dose is not supplied. Extract MICs cannot be assigned to pure coixol, nor
    generalized across assays.
  snapshot_sha256: c687087652188f25c1eb9d53e8eb474812f9a4238933fff9d79c9acdb9419118
- evidence_id: primary1997
  kind: primary_source
  reference: https://doi.org/10.1021/jf9608581
  locator: Author-uploaded full text https://www.researchgate.net/publication/231555242_Antimicrobial_Activity_of_Natural_2-Benzoxazolinones_and_Related_Derivatives
    ; methods/Table 1 textual rendering
  accessed_at: '2026-10-21T08:11:33Z'
  support: context_only
  summary: Compound 2 MBOA has MIC >1000 µg/mL against S. aureus ATCC 25923 and E.
    coli ATCC 25922, and 450 µg/mL against Candida albicans. Tests use 35 °C/24h;
    bacterial medium is Mueller-Hinton. The broad positive abstract needs these censored
    results. SAR is not molecular-target evidence. Original table pixels were not
    retrieved; values require visual confirmation before quantitative native curation.
- evidence_id: primary2026
  kind: primary_source
  reference: PMID:42179630
  locator: DOI:10.1021/acsomega.5c12161; PMC13191540 full XML, methods/results
  accessed_at: '2026-10-21T08:11:33Z'
  support: supports
  summary: Commercial 97% MBOA has Salmonella Typhi MTCC734 MIC >0.25 and ≤0.5 mg/mL,
    most clinical isolates >0.5 and ≤1 mg/mL, and several >1 mg/mL. MHB microdilution
    uses 5×10^5 CFU/mL, overnight 37 °C. Recombinant S. Typhi DHFR NADPH assay shows
    concentration-dependent inhibition at 0.01–0.1 mg/mL; human DHFR comparison and
    docking accompany it. This supports biochemical inhibition, not direct binding
    or proven whole-cell target causality. Mouse efficacy uses S. Typhimurium OSS535,
    not S. Typhi.
  snapshot_sha256: b8b7b168ad6587e1326cc65dbced1ac4a02a3e70e043a238a7c274b4f5929b50
- evidence_id: all-adopted-leads
  kind: primary_source
  reference: PMID:11701394; PMID:16154300; PMID:16425448; PMID:16478219; PMID:18160321;
    PMID:19302487; PMID:2203893; PMID:22982975; PMID:24402687; PMID:26940061
  locator: 061-primarycore.json and 061-lead-dispositions.json; all ten complete abstracts
    inspected
  accessed_at: '2026-10-21T08:11:33Z'
  support: context_only
  summary: 11701394 supplies direct antimicrobial findings. Six leads concern sheep/rodent
    reproduction or photoperiod (16154300,18160321,2203893,22982975,24402687,26940061);16425448
    concerns lettuce germination and alpha-amylase induction;16478219 concerns soil
    degradation.19302487 investigates F. verticillioides FDB2/BOA biotransformation;
    BOA-specific evidence must not become an MBOA resistance assertion.
  snapshot_sha256: 8ee3580c47a39032350f69074c283782db991ad48f267bbb0cd8cdfe533d9767
- evidence_id: additional-leads
  kind: primary_source
  reference: PMID:28279674; PMID:32517283; PMID:33048595; PMID:35113672; PMID:35422782;
    PMID:7025209
  locator: 061-extra-core.json; six additional current ChEBI leads
  accessed_at: '2026-10-21T08:11:33Z'
  support: context_only
  summary: Five complete abstracts inspected;7025209 resolves but has no abstract.28279674
    is vole reproduction;32517283 models insect chemosensory-protein binding;35422782
    measures vole cecal community changes, not direct killing of each taxon.33048595
    reports Pythium growth suppression and increased corn disease in some conditions;35113672
    reports Phytophthora sojae growth/chemotaxis effects and transcriptional pathway
    associations. These oomycetes are not bacteria; expression associations do not
    establish direct protein targets. Full papers were not inspected.
  snapshot_sha256: ec512c823005530a705ed3cc90848f165522022b15ebf0fda9e618d9d5801acc
- evidence_id: chemistry
  kind: validation
  reference: RDKit and hashlib calculations
  locator: 061-chemistry.py and 061-chemistry.json
  accessed_at: '2026-10-21T08:11:33Z'
  support: supports
  summary: Native SMILES fails kekulization. Candidate [nH] lactam and PubChem parse
    identically; stored InChI parses as lactim COc1ccc2nc(O)oc2c1. Both valid tautomers
    share the standard mobile-H InChIKey, C8H7NO3, charge 0 and masses 165.148/165.04259.
    Key equality does not prove identical tautomer graphs. Mint reproduces; standalone
    script exits 1 for native-SMILES failure.
  snapshot_sha256: 9e700a3f9ca5e606e9d800ff3bd3a8fa1d415ac24d5026a86c9c5c561b80b292
- evidence_id: source-check
  kind: validation
  reference: Focused current-source assertions
  locator: 061-source-check.py and 061-source-check.json
  accessed_at: '2026-10-21T08:11:33Z'
  support: supports
  summary: Exit 0 verifies source reproduction, native term/parents/roles, synonyms,
    normalized xrefs and identity strings. It explicitly expects defective source
    SMILES to fail parsing; this success does not replace the failed chemistry gate.
  snapshot_sha256: 3be7d72a252584eb345f8927fc88a9ebfd07f4d3d74afb740a010fd6185774ff
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual isolated batch 007 executions; 061-strict.tsv
  accessed_at: '2026-10-21T08:11:33Z'
  support: supports
  summary: Both documented focused gates exited0; strict scanned one record with zero
    ERROR rows. Schema success does not detect the malformed chemical graph.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local and bounded public discovery
  locator: 061-local-hits.txt; exact-name, coixol and MBOA queries
  accessed_at: '2026-10-21T08:11:33Z'
  support: context_only
  summary: Read all adopted abstract leads, current authority identities and selected
    primary activity/mechanism studies. Search does not establish universal absence
    of other mechanisms.
  search_scope: prepare.py 61 ran rg --no-ignore --hidden excluding only .git and
    .venv before judgment. Follow-up covered exact identity/aliases, antibacterial,
    antifungal, DHFR, activity and source-owner code; all ten adopted PMIDs and six
    additional current ChEBI leads were resolved.
assessments:
- assessment_id: identity
  area: identity
  topic: Lactam representation and tautomer normalization
  outcome: concern
  summary: Native SMILES is invalid; independent lactam sources establish a precise
    repair. Standard InChI permits mobile-H lactim normalization and is not proof
    of a unique tautomer graph.
  target_ids:
  - CHEBI:195240
  evidence_ids:
  - record
  - chemistry
  - pubchem
  - knapsack
- assessment_id: grounding
  area: grounding
  topic: Term, parents and antimicrobial roles
  outcome: supported
  summary: Exact current term and two native parents reproduce. Direct primary evidence
    supports broad antibacterial/antifungal filing with condition-specific negative
    or weak results retained.
  target_ids:
  - CHEBI:195240
  evidence_ids:
  - ontology
  - primary2001
  - primary1993
  - primary1997
  - primary2026
- assessment_id: terminology
  area: grounding
  topic: Coixol synonym classification
  outcome: unknown
  summary: Coixol string denotes this compound and BRAND_NAME reproduces the source;
    historical brand semantics were not established independently. No confirmed synonym-type
    defect is asserted.
  target_ids:
  - CHEBI:195240
  evidence_ids:
  - ontology
  - knapsack
- assessment_id: xref
  area: grounding
  topic: External target checks
  outcome: unknown
  summary: KNApSAcK and ChemSpider agree; FooDB/HMDB/CAS exact external targets remain
    incompletely resolved.
  target_ids:
  - CHEBI:195240
  evidence_ids:
  - xref-limits
  - knapsack
- assessment_id: mechanism
  area: scope
  topic: Biochemical DHFR inhibition versus cellular causality
  outcome: supported
  summary: Primary recombinant bacterial enzyme inhibition is available and must be
    qualified as a candidate cellular mechanism. Docking does not establish binding;
    growth inhibition alone does not prove bactericidality.
  target_ids:
  - CHEBI:195240
  evidence_ids:
  - primary2026
- assessment_id: completeness
  area: completeness
  topic: Specific primary evidence opportunity
  outcome: concern
  summary: Verified primary activity and biochemical inhibition support bounded evidence
    enrichment. Optional emptiness alone is not an error.
  target_ids:
  - CHEBI:195240
  evidence_ids:
  - record
  - primary2001
  - primary2026
- assessment_id: producer
  area: representation
  topic: Natural occurrence and production
  outcome: unknown
  summary: No producer is asserted. Database plant occurrence, degradation and biosynthesis
    predictions do not by themselves establish exact-compound biosynthesis in a named
    producer.
  target_ids:
  - CHEBI:195240
  evidence_ids:
  - knapsack
  - all-adopted-leads
- assessment_id: resistance
  area: scope
  topic: Adjacent BOA detoxification literature
  outcome: unknown
  summary: The adopted FDB2 abstract concerns BOA. An exact MBOA resistance mechanism
    needs direct source verification before curation.
  target_ids:
  - CHEBI:195240
  evidence_ids:
  - all-adopted-leads
- assessment_id: optional
  area: representation
  topic: Clinical, graph and dataset annotations
  outcome: not_applicable
  summary: No such objects are asserted. Mouse efficacy is preclinical, and host or
    transcriptomic responses are not direct antimicrobial-target evidence.
  target_ids:
  - CHEBI:195240
  evidence_ids:
  - record
  - primary2026
  - additional-leads
- assessment_id: provenance
  area: ownership
  topic: Generated field ownership and history
  outcome: supported
  summary: Maintained source row and mint reproduce, with four chronological seed/reseed
    events. Source-owned repair must survive regeneration.
  target_ids:
  - CHEBI:195240
  evidence_ids:
  - inventory
  - ownership
  - chemistry
- assessment_id: schema
  area: schema
  topic: Schema success and chemistry failure
  outcome: concern
  summary: Focused schema checks pass; malformed SMILES remains a major barrier to
    native REVIEWED sign-off.
  target_ids:
  - CHEBI:195240
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-195240-invalid-smiles-missing-lactam-hydrogen
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Source-derived SMILES omits lactam [nH] and cannot be parsed
  description: chemical_structure.smiles COc1ccc2nc(=O)oc2c1 fails kekulization. Candidate
    COc1ccc2[nH]c(=O)oc2c1 agrees with independent PubChem and KNApSAcK lactam structures,
    native standard key, formula and masses. Stored InChI can also generate a lactim
    tautomer; normalized key equality must not be described as graph equality. Adopted
    and current ChEBI share the defect.
  target_ids:
  - CHEBI:195240
  field_paths:
  - chemical_structure.smiles
  evidence_ids:
  - record
  - inventory
  - chebi
  - pubchem
  - knapsack
  - chemistry
  rule_id: 'review-checklist: Chemical identity and structural consistency'
  native_severity: major core structural inconsistency blocking native REVIEWED
  normalization_reason: One core encoding is invalid, but intended exact identity
    is established independently; this is a repairable major defect rather than an
    unresolved identity blocker.
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
- finding_id: F2
  issue_key: chebi-195240-primary-activity-and-biochemical-evidence-completeness
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Primary exact-compound activity and qualified DHFR evidence are available
  description: The source-seeded record lacks claim-level evidence. Verified primary
    observations offer a specific enrichment opportunity, with assay-specific negative
    results, censored MICs and tentative cellular mechanism retained.
  target_ids:
  - CHEBI:195240
  field_paths:
  - evidence
  - activity_spectrum
  - molecular_targets
  - mode_of_action_notes
  - discussions
  evidence_ids:
  - record
  - primary2001
  - primary1993
  - primary1997
  - primary2026
  rule_id: 'review-checklist: Evidence standard, Activity and Mechanism'
  native_severity: minor actionable primary-evidence completeness gap
  normalization_reason: Specific verified primary results are available; empty optional
    fields alone are not an error and biochemical inhibition does not justify unqualified
    whole-cell target causality.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/6-methoxy-2-benzoxazolinone.yaml
    role: Curator-owned evidence, activity_spectrum, molecular_targets, mode_of_action_notes
      and discussions through validated writer/history
actions:
- action_id: A1
  description: Repair maintained source handling with independently supported lactam
    SMILES COc1ccc2[nH]c(=O)oc2c1, then regenerate reproducibly.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:195240
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
  acceptance_checks:
  - Require valid parsing, native MKMCJLMBVKHUMS-UHFFFAOYSA-N, C8H7NO3, charge 0,
    masses 165.148/165.04259, and graph agreement with independent lactam structures.
    Preserve mobile-H tautomer normalization provenance rather than claiming InChI
    uniquely encodes the lactam.
  - Do not patch only generated YAML or change correct InChI/key/formula to accommodate
    malformed input. Preserve evidence and maintained provenance of the correction.
  - Use authorized curation/regeneration and validated history; complete schema, strict,
    source reproduction, corpus integrity and QC gates before native REVIEWED.
- action_id: A2
  description: Curate claim-level primary activity and recombinant DHFR inhibition
    with explicit assay and causal limits.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:195240
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/6-methoxy-2-benzoxazolinone.yaml
    role: Curator-owned evidence, activity_spectrum, molecular_targets, mode_of_action_notes
      and discussions through validated writer/history
  acceptance_checks:
  - Preserve exact MBOA versus BOA and other indoles; retain strain, medium, dose,
    incubation and censored inequality for each verified observation. Keep 1993 negative
    coixol result and weak 1997 bacterial results as context; inspect original tables
    before quantitative curation where only extracted text was available.
  - Represent 2026 DHFR as directly tested biochemical inhibition and a candidate
    cellular mechanism, not proven binding, a docking-only result, universal bactericidal
    action or established whole-cell target. Do not invent an IC50 or UniProt accession.
  - Keep mouse S. Typhimurium efficacy separate from S. Typhi in-vitro assays and
    human clinical efficacy. Resolve source concentration/unit inconsistencies and
    retrieve supplementary tables before importing additional numerical results.
  - Do not transfer BOA detoxification, host reproductive phenotypes, insect binding
    predictions or oomycete expression associations to bacterial target/resistance
    claims. Verify biosynthesis before producer_organisms annotation.
  - Use validated writer/history and required native gates before REVIEWED sign-off.
limitations:
- All ten adopted PMID abstracts were read. Six additional current ChEBI leads were
  resolved; five had abstracts and 7025209 had none. The 2001/2002 antimicrobial reports
  remain abstract-only; their numerical conditions cannot be inferred.
- The 2026 full XML was read, but ACS supplementary download returned 403. Methods
  and results differ in time-kill concentration/multiple wording; Figure 7 labels
  mouse doses mg/mL although methods use mg/kg. These source limits must be resolved
  before importing affected measurements. No direct binding, causal cellular target,
  clinical safety or human efficacy was established.
- The 1997 author-uploaded full text was read through a textual rendering; original
  table pixels were not retrieved. A university PDF endpoint instead returned an HTML
  challenge, preserved under 061-primary1997.pdf despite the suffix. Quantitative
  native annotation requires visual table confirmation.
- FooDB/HMDB returned 403 and CAS an application shell. Coixol BRAND_NAME historical
  semantics remain unverified. Source-string reproduction is narrower than independent
  authority validation.
- Current ChEBI/OLS repeat the invalid SMILES; chemistry intentionally exits 1. Schema
  success does not resolve the defect. Native REVIEWED remains blocked by the major
  structure issue and incomplete required gates; this bounded review is not an exhaustive
  literature inventory.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Only scratch review artifacts were written; native records and maintained inputs
  were unchanged. All 13 captured input hashes were rechecked before draft creation.
- The first combined scratch display returned the later display command status; the
  chemistry script was rerun alone and its actual exit 1 is the recorded result.
- Coordinator independently reproduced the native parsing failure and confirmed that
  the [nH] lactam repair gives the recorded key/formula while the stored mobile-H
  InChI renders a lactim graph. No native structure was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:195240
- https://pubchem.ncbi.nlm.nih.gov/compound/10772
- https://www.knapsackfamily.com/knapsack_core/information.php?word=C00036627
- https://doi.org/10.3136/nskkk1962.40.5_353
- https://doi.org/10.1021/jf9608581
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13191540/
tags:
- record-review
- benzoxazolinone
- invalid-smiles
- tautomer-scope
- primary-activity
- biochemical-target
```
