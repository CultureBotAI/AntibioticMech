# Ceftiofur: coherent sodium structure with neutral-acid chemical cross-references

- Review: 20261021T121415Z-ceftiofur
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:49:12Z
- Finished UTC: 2026-10-21T12:14:15Z
- Reviewer: Codex review002 subagent with root evidence capture (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

CHEBI:31383 and the internally consistent structure identify ceftiofur sodium. PubChem 6328657 and ChEMBL 222913 instead identify neutral ceftiofur, a confirmed major exact-cross-reference defect inherited from ARO. The antibacterial classification is supported by the original sodium-material abstract and official product labeling. The PBP target and EBR-5 resistance items honestly retain database provenance. Primary studies support bounded PBP competition and recombinant resistance phenotypes, but do not establish an exact sodium-specific causal chain or ceftiofur-specific EBR-5 kinetics.

## Scope And Provenance

Entire native YAML: definition and PMID, two brand aliases, broader cephalosporin class, sodium structure and four xrefs, sole ARO source concept, EBR-5 resistance item, PBP target item and all four history events. The single adopted antibiotic-definition PMID and the primary study linked by the resistance database were inspected. Additional PBP and official label sources were checked within their exact scope.

Selection: Queue 259. Root captured the target before judgment; all original seventeen inputs were preserved and the actual maintained AST form-scope context was appended as the eighteenth input.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:31383 | data/antibiotics/antibacterial/ceftiofur.yaml | generated | ceftiofur |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| chemistry | passed | False | CHEBI:31383 | Root executed this focused command against batch026; retained output independently inspected, exit 0. Chemistry used the batch019 RDKit interpreter and reproduced the sole ARO mint. |
| schema | passed | True | CHEBI:31383 | Root executed this documented focused command against the exact record; retained output independently inspected, exit 0. |
| strict | passed | True | CHEBI:31383 | Root executed this documented focused command against the exact record; retained output independently inspected, exit 0. |
| Authoritative full QC | failed | True | CHEBI:31383 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:31383 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:31383 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:31383 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:31383 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:31383 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:31383 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:31383 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:31383 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact ceftiofur sodium structure

identity: supported. Targets: CHEBI:31383.

The native graph, ChEBI identity, CAS attestation and descriptors agree on one sodium salt. The generic source label merits explicit salt qualification in future display/curation, but is not sufficient evidence to replace this structure or exclude a supported antibacterial salt. Naxcel and Excenel powder have official sodium attestations.

### Neutral chemical xrefs on a sodium record

identity: concern. Targets: CHEBI:31383.

PubChem 6328657 and ChEMBL 222913 encode neutral ceftiofur, not the exact sodium structure. The difference is confirmed from independently parsed official structures, not inferred from naming alone. ARO is the source of the mixed references.

### Antibacterial class and broader cephalosporin parent

scope: supported. Targets: CHEBI:31383.

The structural class is genuinely broader, while the sodium-material study directly supports antibacterial activity. Empty ChEBI role ancestry in the lookup row does not erase ARO filing or establish a missing required role.

### PBP target and definition citation scope

evidence: unknown. Targets: CHEBI:31383.

The imported target honestly remains PRIMARY_EVIDENCE_NEEDED with unspecified organism and assay. Later primary competition data support a bounded PBP2x interaction, but not an exact sodium-specific lysis chain. The 1987 abstract supports activity and does not settle whether its inaccessible full text substantiates every mechanism clause. Retain this as a citation-scope limitation, not a confirmed erroneous citation or a claim that no primary PBP evidence exists.

### EBR-5 phenotype versus biochemical mechanism

evidence: supported. Targets: CHEBI:31383.

The native item is explicitly a CARD assertion. The original gene-transfer experiment corroborates reduced ceftiofur susceptibility in its named recombinant system. Antibiotic inactivation is the enzyme-family mechanism, but no ceftiofur-specific purified-enzyme kinetic result or salt specification is present in the inspected main text. Preserve database status and condition any literature enrichment on this scope.

### Optional enrichments and native scientific status

completeness: unknown. Targets: CHEBI:31383.

The absence of numerical MICs, producer, clinical status, causal graph, mode enum and datasets is not a separate required-field defect. Activity and target enrichment could be useful after material and assay qualification. A field isolate that resists ceftiofur is not its producer, and antibody-production host experiments are not antibacterial targets. SEEDED remains appropriate until exact xrefs and native sign-off criteria are resolved.

### Maintained source correction and provenance

ownership: supported. Targets: CHEBI:31383.

The actual owner is the ARO source/extractor/seeder path, with ChEBI supplying sodium structure through a lookup. The AST map is context only. All eighteen captured input hashes remain unchanged; no record mutation or scientific-status promotion is part of this review.

### Focused gate success and scientific limits

schema: supported. Targets: CHEBI:31383.

Root focused schema, strict and chemical checks pass. Those checks do not compare the currently resolved external PubChem/ChEMBL structures, so they do not invalidate the major finding.

## Findings

### F1: Reconcile neutral-acid chemical links with the exact sodium identity

major / open / confirmed; issue key: ceftiofur-sodium-neutral-acid-chemical-xrefs.

The native CHEBI:31383 structure is ceftiofur sodium, RFLHUYUQCKHUKS-JUODUXDSSA-M, but xrefs[2] ChEMBL222913 and xrefs[3] PubChem6328657 are neutral ceftiofur, ZBHXIWJRIFEVQY-IHMPYVIRSA-N. Independent official structure parses confirm the missing sodium and different composition. The current ARO page and adopted row mix these identities. Preserve the valid sodium graph and reconcile only exact chemical links through the maintained source path. PubChem23671563 is an independently verified sodium candidate; no sodium ChEMBL replacement is established.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained cross-reference mapping and reproduce a sodium-only exact chemical identity set.

- Remove or replace the neutral PubChem and ChEMBL identifiers from the sodium record through a reproducible source correction or maintained mapping; do not relabel neutral identities as exact sodium links.
- Verify any replacement from its full chemical graph, counterion, protonation and stereochemistry. PubChem23671563 already matches the native graph and full key; other same-key tautomer results require separate adjudication.
- Preserve CHEBI:31383, sodium composition, two R centres, source mint and claim provenance unless a separately justified scope decision changes them. Do not replace the entire record with neutral ceftiofur.
- Rerun the authorized source/seeder path and focused schema/strict plus applicable reference, history and corpus gates; confirm regeneration does not reintroduce the wrong exact links.

### A2

If mechanism or resistance enrichment is undertaken, add claim-specific primary support with explicit material and assay scope.

- Keep the 1987 reference bounded to the inspected sodium activity evidence unless its full text is obtained; do not treat unavailable full text as proof of a bad citation.
- Represent the PBP2x competitive ELISA endpoint as IC50 in its analytical context, not Kd, MIC or measured whole-cell lysis. Retain unspecified ceftiofur counterion and distinguish docking from experimental binding.
- For EBR-5 retain strain, vector, inducer and selection conditions, exact inequalities and units. Do not infer ceftiofur-specific kinetic constants from Table2 or transfer unspecified material into an exact sodium measurement without qualification.
- Use the native validated writer/history workflow only in a separately authorized curation task; this optional enrichment is not a required correction by itself.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/ceftiofur.yaml; Entire native record, all fields and four history events. | supports | The SEEDED/EXACT record contains a ceftiofur carboxylate plus sodium, net charge 0, formula C19H16N5O7S3.Na, two R stereocentres and key RFLHUYUQCKHUKS-JUODUXDSSA-M. The generic ARO label supplies the filename and label. There are no native quantitative activity, clinical-status, producer, causal-graph or dataset objects. The target is explicitly PRIMARY_EVIDENCE_NEEDED; both imported target and resistance notes identify database assertions. |
| source | data/raw/aro_antibiotics.tsv; data/raw/chebi_antimicrobials.tsv; data/raw/aro_target_edges.tsv; data/raw/aro_resistance_edges.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; conf/sources.yaml; conf/aro_target_roles.tsv; ARO row 303; ChEBI row 636; target row 239; resistance row 3999; concept construction, definition/xref emission and imported-edge logic. | supports | ChEBI 31383 is outside the adopted antimicrobial-role scope but supplies the sodium structure through the ARO cross-reference lookup. ARO supplies the generic name, definition, PMID 3631686, aliases and the incompatible chemical xrefs. The seeder uses the first ARO definition reference and passes unresolved external chemical xrefs through its identity gate. Target and resistance import preserve explicit database provenance. Only the ARO concept is native; its mint is reproducible. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:31383; Complete visible identity, structure, names, relations and manual cross-references. | supports | The current entry is Ceftiofur sodium, with the same sodium-containing SMILES, Standard InChI, key, formula, charge and masses. CAS 104010-37-9 and KEGG C13143/D01682 are explicit. The broad organic-molecular-entity parent CHEBI:50860 is not an asserted antimicrobial role. This is a coherent exact salt, not evidence to replace it wholesale with the neutral drug. |
| neutral-xrefs | https://pubchem.ncbi.nlm.nih.gov/compound/6328657; https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL222913.json; Complete official structure responses; independent parses retained in 026-root-xref-check.json, key 259. | refutes | Both identifiers describe neutral C19H17N5O7S3 without sodium, key ZBHXIWJRIFEVQY-IHMPYVIRSA-N. PubChem SMILES and ChEMBL SMILES, molfile and InChI independently parse to the neutral identity. Native SMILES and InChI instead reproduce the sodium key. These exact chemical xrefs therefore violate the same-structure rule even though the underlying active moiety is shared. |
| salt-xrefs | https://pubchem.ncbi.nlm.nih.gov/compound/23671563; https://rest.kegg.jp/get/C13143; https://rest.kegg.jp/get/D01682; CAS-based PubChem response, independently parsed candidate SMILES, and both official KEGG structures. | supports | PubChem 23671563, returned by CAS 104010-37-9, explicitly has the sodium carboxylate graph, native formula and full key; its SMILES independently reproduces that key. Both KEGG molfiles likewise match. A full-key query also returns CIDs 9571073 and 131664133; Standard InChI equivalence alone does not adjudicate their tautomer/proton representation, so these are not interchangeable replacement candidates by default. No sodium ChEMBL replacement is asserted. |
| card | https://card.mcmaster.ca/aro/3004006; https://card.mcmaster.ca/aro/0000032; https://card.mcmaster.ca/aro/3000749; https://card.mcmaster.ca/aro/3007437; Official identity, definition, class, target, resistance and publication sections. | partial | ARO 3004006 is ceftiofur under the broader cephalosporin class ARO 0000032. Its current page itself combines a neutral SMILES/PubChem/ChEMBL identity with sodium ChEBI/CAS references, localizing the upstream mismatch. ARO 3000749 is the generic beta-lactam-sensitive PBP target, with a ceftiofur relation; it is not one organism-specific protein. EBR-5 ARO 3007437 has an antibiotic-inactivation classification and ceftiofur resistance relation linked to PMID 36719228. |
| sodium-primary | PMID:3631686; https://pubmed.ncbi.nlm.nih.gov/3631686/; Complete original indexed abstract and bibliographic record, source MED. Original AVMA HTML/PDF routes inspected as retrieval failures. | supports | The original 1987 study explicitly defines ceftiofur sodium and reports MIC evaluation of 264 strains from 17 species and nine genera, plus activity in specified mouse infection models. It supports antibacterial identity and spectrum context for sodium material. The abstract does not present a PBP-binding assay or directly trace the entire lysis mechanism. Both publisher routes returned the same 1444-byte HTML challenge, including the nominal PDF; their full experimental contents were not inspected. This access limit does not prove the citation is erroneous. |
| ebr-primary | PMID:36719228; DOI:10.1128/spectrum.00039-23; https://pmc.ncbi.nlm.nih.gov/articles/PMC10101081/; Full original main-text XML read, including Methods in Observation, Table 1 and Table 2 with footnotes. | partial | Table 1 reports ceftiofur MICs of 64 mg/L for E. stercoris SCVM0123, 4 mg/L for E. coli BL21 carrying pET24a-blaEBR-5 and no more than 0.125 mg/L for the empty-vector control. Recombinant tests include 50 mg/L kanamycin and 0.2 mM IPTG. The gene-transfer comparison supports an EBR-5-associated susceptibility shift; the field isolate also carries other resistance genes. Purified EBR-5 hydrolyzes other tested beta-lactams, but ceftiofur is absent from Table 2 kinetics. The exact ceftiofur counterion is not specified in the main text. No ceftiofur-specific catalytic value or exact-sodium numeric claim follows. |
| pbp-primary | PMID:34577037; DOI:10.3390/molecules26185569; https://pmc.ncbi.nlm.nih.gov/articles/PMC8470104/; Full original XML main text read; Results 2.1.1, Table 2 and Methods 3.1–3.2 distinguish competition measurements from later docking. | partial | Commercial ceftiofur from the National Institutes for Food and Drug Control is tested by direct competitive ELISA with recombinant PBP2x*. Table 2 reports IC50 2.63 ng/mL; standards compete with an enzyme marker for 30 minutes at 37 degrees C before color measurement. This is a measured competition endpoint, not a dissociation constant, bacterial MIC or whole-cell causal chain. The material counterion is not specified. Figure 5 uses molecular docking against a PBP2x structure, not a new ceftiofur co-crystal or direct measurement of those modeled contacts. |
| pbp-origin | PMID:23336133; DOI:10.3967/0895-3988.2013.02.004; https://pubmed.ncbi.nlm.nih.gov/23336133/; Complete indexed original abstract, cited as reference 24 by the 2021 assay paper. | partial | The earlier assay study identifies recombinant PBP2x* from S. pneumoniae R6 and reports ceftiofur among beta-lactams detectable in a milk residue assay. This verifies the origin and analytical context of the receptor system; the abstract does not supply an exact sodium material specification or whole-cell antibacterial mechanism. |
| brands | https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b6fed070-b398-4348-9927-9891f78c7c31; https://www.hpra.ie/find-a-medicine/for-animal-use/suspended-medicines/details/15; NAXCEL Description/chemical-name/ingredient sections; HPRA archived Excenel 4 g powder identity. | supports | NAXCEL explicitly contains ceftiofur sodium and describes bactericidal cell-wall-synthesis inhibition. HPRA explicitly identifies ceftiofur sodium as the active substance of Excenel 4 g sterile powder. The generic Excenel alias therefore cannot be rejected merely because another formulation uses hydrochloride. These are product-qualified brand attestations, not exact equivalence of all excipients, formulations, markets or regulatory histories. |
| structured | 026-root-imodulondb-datasets.txt; 026-root-imodulondb-pbp.txt; Root structured adapter outputs generated before open web research; both outputs independently read. | context_only | The dataset catalog has no E. stercoris entry. The penicillin query in e_coli/precise1k returns b2430/yfeW, penicillin-binding protein 4B, and zero iModulon hits. Neither finding establishes or refutes ceftiofur binding or EBR-5 resistance. There is no relevant component to summarize; computational expression membership is not antibacterial mechanism evidence. |
| scope-map | curation/ncbi_ast_drug_map.tsv; Maintained ceftiofur mapping row 24, captured before this assessment. | context_only | The AST mapping already distinguishes neutral ceftiofur PubChem 6328657 from the lexical sodium corpus candidate CHEBI:31383 and labels that AST mapping MISSING_CORPUS_RECORD. This is maintained scope context, not primary proof and not an instruction to exclude the valid sodium record. The AST adoption lane remains deferred; no AST requests or source contact were made. |
| search | 259-inclusive-local-hits.txt; public exact ceftiofur/PBP and sodium-brand searches; Inclusive local search, bounded public discovery and source retrieval. | context_only | Hidden and ignored files were included. Hits identify the native record, exact source rows, readiness queue, AST scope decision and generated projections; no exact corrective decision or overlay was found in the searched areas. Public PBP searches yielded the original analytical competition study. Search snippets and the broad 259-primary-search.json discovery collection are not treated as inspected experimental support. |
| validation | 259-focused-results.json;259-schema.log;259-strict.log;259-chemistry.json;026-root-xref-check.json;259-candidate-chemistry.json; Actual root focused gate logs and independently inspected chemical outputs; additional sodium candidate parse. | supports | Schema and strict validation pass with zero errors. Native SMILES and InChI agree on composition, charge, masses, two R centres and full key; sole ARO mint matches. External PubChem/ChEMBL neutral graphs disagree in composition and full key. Both KEGG structures and the separately parsed PubChem sodium candidate match the native salt. Chemical consistency alone does not validate external exact-identity links. |

## Limits And Additional Notes

- The whole native record and actual maintained rows were read. Initial seventeen input hashes were preserved and the actual AST mapping context appended before judgment; all eighteen were rechecked unchanged.
- The sole adopted definition PMID was read at full indexed-abstract depth. Both original 1987 AVMA routes returned an HTML challenge rather than full article/PDF; exact numerical assays and complete causal support from that paper remain unverified.
- The EBR-5 original main-text XML, including both tables and their footnotes, was read. Its supplementary methods were not independently audited; no exact ceftiofur counterion or ceftiofur-specific purified-enzyme kinetics are inferred.
- The 2021 PBP paper was read in full main-text XML; figures were not used as crystallographic evidence. The 2013 precursor was read at complete abstract depth. Exact assay material salt and the full whole-cell causal chain remain unresolved.
- Official chemical and product-label pages were inspected without paid registry access. Brand/product identity was checked in specific formulations; no universal cross-jurisdictional brand or clinical-status assertion is made.
- The structured adapter outputs were generated by root before web research and independently inspected here. They provide no matched causal experiment; absence of a relevant module or species is not negative biological evidence.
- Discovery results were used only as leads. In particular, the broad primary-search response is not claimed as a fully inspected literature survey. The maintained AST adoption restriction was respected; no new AST endpoint requests or contact occurred.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T121415Z-ceftiofur
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Ceftiofur: coherent sodium structure with neutral-acid chemical cross-references'
started_at: '2026-10-21T11:49:12Z'
finished_at: '2026-10-21T12:14:15Z'
reviewer:
  identity: Codex review002 subagent with root evidence capture
  kind: agent
  independence: independent
  independence_basis: Did not author the seed. Independently read the entire native
    record, source rows, official identities and original papers. Root captured initial
    provenance and ran focused gates; their retained outputs were inspected. Additional
    public primary and official checks were performed by this reviewer.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: CHEBI:31383 and the internally consistent structure identify ceftiofur sodium.
  PubChem 6328657 and ChEMBL 222913 instead identify neutral ceftiofur, a confirmed
  major exact-cross-reference defect inherited from ARO. The antibacterial classification
  is supported by the original sodium-material abstract and official product labeling.
  The PBP target and EBR-5 resistance items honestly retain database provenance. Primary
  studies support bounded PBP competition and recombinant resistance phenotypes, but
  do not establish an exact sodium-specific causal chain or ceftiofur-specific EBR-5
  kinetics.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
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
  - path: curation/ncbi_ast_drug_map.tsv
    sha256: 8b224448e1b2107e40107c4fb99820230249ec1318e36b032bb60324e1948088
    role: context
  - path: data/antibiotics/antibacterial/ceftiofur.yaml
    sha256: a5bb84123d6f54f25599e00501a58a474bc18edcd19a676a33dabd7af3f4bc08
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
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
- target_id: CHEBI:31383
  path: data/antibiotics/antibacterial/ceftiofur.yaml
  label: ceftiofur
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Out-of-role-scope ChEBI identity and structure lookup used by the ARO concept
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO and ChEBI extraction and source normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition, aliases, class and cross-reference owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported PBP target relation owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported EBR-5 resistance relation owner
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target type, relation and evidence-status policy
  - repository: CultureBotAI/AntibioticMech
    path: curation/ncbi_ast_drug_map.tsv
    role: Maintained AST scope decision consulted as context; not owner of ChEBI/CARD
      xrefs
scope:
  description: 'Entire native YAML: definition and PMID, two brand aliases, broader
    cephalosporin class, sodium structure and four xrefs, sole ARO source concept,
    EBR-5 resistance item, PBP target item and all four history events. The single
    adopted antibiotic-definition PMID and the primary study linked by the resistance
    database were inspected. Additional PBP and official label sources were checked
    within their exact scope.'
  selection: Queue 259. Root captured the target before judgment; all original seventeen
    inputs were preserved and the actual maintained AST form-scope context was appended
    as the eighteenth input.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:31383
  exclusions:
  - target: Neutral ceftiofur, hydrochloride products, desfuroylceftiofur and broader
      cephalosporin experiments
    reason: These are distinct materials or contexts. Generic drug terminology is
      not an exact sodium identity assertion; no quantitative result is silently transferred
      across forms.
checks:
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Root executed this focused command against batch026; retained output independently
    inspected, exit 0. Chemistry used the batch019 RDKit interpreter and reproduced
    the sole ARO mint.
  target_ids:
  - CHEBI:31383
  evidence_ids:
  - validation
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    259
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Root executed this documented focused command against the exact record;
    retained output independently inspected, exit 0.
  target_ids:
  - CHEBI:31383
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/ceftiofur.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Root executed this documented focused command against the exact record;
    retained output independently inspected, exit 0.
  target_ids:
  - CHEBI:31383
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/ceftiofur.yaml --out /private/tmp/am-review-session/259-strict.tsv
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
  - CHEBI:31383
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
  - CHEBI:31383
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
  - CHEBI:31383
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
  - CHEBI:31383
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
  - CHEBI:31383
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
  - CHEBI:31383
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
  - CHEBI:31383
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
  - CHEBI:31383
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
  - CHEBI:31383
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/ceftiofur.yaml
  locator: Entire native record, all fields and four history events.
  accessed_at: '2026-10-21T12:11:51Z'
  support: supports
  summary: The SEEDED/EXACT record contains a ceftiofur carboxylate plus sodium, net
    charge 0, formula C19H16N5O7S3.Na, two R stereocentres and key RFLHUYUQCKHUKS-JUODUXDSSA-M.
    The generic ARO label supplies the filename and label. There are no native quantitative
    activity, clinical-status, producer, causal-graph or dataset objects. The target
    is explicitly PRIMARY_EVIDENCE_NEEDED; both imported target and resistance notes
    identify database assertions.
- evidence_id: source
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/chebi_antimicrobials.tsv; data/raw/aro_target_edges.tsv;
    data/raw/aro_resistance_edges.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py;
    conf/sources.yaml; conf/aro_target_roles.tsv
  locator: ARO row 303; ChEBI row 636; target row 239; resistance row 3999; concept
    construction, definition/xref emission and imported-edge logic.
  accessed_at: '2026-10-21T12:11:51Z'
  support: supports
  summary: ChEBI 31383 is outside the adopted antimicrobial-role scope but supplies
    the sodium structure through the ARO cross-reference lookup. ARO supplies the
    generic name, definition, PMID 3631686, aliases and the incompatible chemical
    xrefs. The seeder uses the first ARO definition reference and passes unresolved
    external chemical xrefs through its identity gate. Target and resistance import
    preserve explicit database provenance. Only the ARO concept is native; its mint
    is reproducible.
  snapshot_sha256: 5ac05c15b3a1e863df6a0b26f7742469e94d258748d7267118b4daae342a2bff
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:31383
  locator: Complete visible identity, structure, names, relations and manual cross-references.
  accessed_at: '2026-10-21T11:51:43Z'
  support: supports
  summary: The current entry is Ceftiofur sodium, with the same sodium-containing
    SMILES, Standard InChI, key, formula, charge and masses. CAS 104010-37-9 and KEGG
    C13143/D01682 are explicit. The broad organic-molecular-entity parent CHEBI:50860
    is not an asserted antimicrobial role. This is a coherent exact salt, not evidence
    to replace it wholesale with the neutral drug.
  snapshot_sha256: ffebcaa2c3ad36614cd4692b7da6a0997ec66949fdf6777ba4f54cd2cb0d5748
- evidence_id: neutral-xrefs
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/6328657; https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL222913.json
  locator: Complete official structure responses; independent parses retained in 026-root-xref-check.json,
    key 259.
  accessed_at: '2026-10-21T12:11:51Z'
  support: refutes
  summary: Both identifiers describe neutral C19H17N5O7S3 without sodium, key ZBHXIWJRIFEVQY-IHMPYVIRSA-N.
    PubChem SMILES and ChEMBL SMILES, molfile and InChI independently parse to the
    neutral identity. Native SMILES and InChI instead reproduce the sodium key. These
    exact chemical xrefs therefore violate the same-structure rule even though the
    underlying active moiety is shared.
  snapshot_sha256: 1643d3834cf071dee6f775eb3cc483fd2876a03dbe21b09c81a07d0fc87fe2a0
- evidence_id: salt-xrefs
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/23671563; https://rest.kegg.jp/get/C13143;
    https://rest.kegg.jp/get/D01682
  locator: CAS-based PubChem response, independently parsed candidate SMILES, and
    both official KEGG structures.
  accessed_at: '2026-10-21T11:58:34Z'
  support: supports
  summary: PubChem 23671563, returned by CAS 104010-37-9, explicitly has the sodium
    carboxylate graph, native formula and full key; its SMILES independently reproduces
    that key. Both KEGG molfiles likewise match. A full-key query also returns CIDs
    9571073 and 131664133; Standard InChI equivalence alone does not adjudicate their
    tautomer/proton representation, so these are not interchangeable replacement candidates
    by default. No sodium ChEMBL replacement is asserted.
  snapshot_sha256: e38490d80182b2cc5944f849d62f7f1239dea5cd5ec4cd75b9123730ad05fc2f
- evidence_id: card
  kind: database
  reference: https://card.mcmaster.ca/aro/3004006; https://card.mcmaster.ca/aro/0000032;
    https://card.mcmaster.ca/aro/3000749; https://card.mcmaster.ca/aro/3007437
  locator: Official identity, definition, class, target, resistance and publication
    sections.
  accessed_at: '2026-10-21T11:51:45Z'
  support: partial
  summary: ARO 3004006 is ceftiofur under the broader cephalosporin class ARO 0000032.
    Its current page itself combines a neutral SMILES/PubChem/ChEMBL identity with
    sodium ChEBI/CAS references, localizing the upstream mismatch. ARO 3000749 is
    the generic beta-lactam-sensitive PBP target, with a ceftiofur relation; it is
    not one organism-specific protein. EBR-5 ARO 3007437 has an antibiotic-inactivation
    classification and ceftiofur resistance relation linked to PMID 36719228.
  snapshot_sha256: ddd4c4c0b118925648b8d7cfe5d2d04ea4d44d1e2d00a1c8b13b754efc23f14a
- evidence_id: sodium-primary
  kind: primary_source
  reference: PMID:3631686; https://pubmed.ncbi.nlm.nih.gov/3631686/
  locator: Complete original indexed abstract and bibliographic record, source MED.
    Original AVMA HTML/PDF routes inspected as retrieval failures.
  accessed_at: '2026-10-21T11:51:46Z'
  support: supports
  summary: The original 1987 study explicitly defines ceftiofur sodium and reports
    MIC evaluation of 264 strains from 17 species and nine genera, plus activity in
    specified mouse infection models. It supports antibacterial identity and spectrum
    context for sodium material. The abstract does not present a PBP-binding assay
    or directly trace the entire lysis mechanism. Both publisher routes returned the
    same 1444-byte HTML challenge, including the nominal PDF; their full experimental
    contents were not inspected. This access limit does not prove the citation is
    erroneous.
  snapshot_sha256: 20463f5c0bce7ab12484fca708a0721d6be384e97f8be12488f93ffa445bb907
- evidence_id: ebr-primary
  kind: primary_source
  reference: PMID:36719228; DOI:10.1128/spectrum.00039-23; https://pmc.ncbi.nlm.nih.gov/articles/PMC10101081/
  locator: Full original main-text XML read, including Methods in Observation, Table
    1 and Table 2 with footnotes.
  accessed_at: '2026-10-21T11:53:23Z'
  support: partial
  summary: Table 1 reports ceftiofur MICs of 64 mg/L for E. stercoris SCVM0123, 4
    mg/L for E. coli BL21 carrying pET24a-blaEBR-5 and no more than 0.125 mg/L for
    the empty-vector control. Recombinant tests include 50 mg/L kanamycin and 0.2
    mM IPTG. The gene-transfer comparison supports an EBR-5-associated susceptibility
    shift; the field isolate also carries other resistance genes. Purified EBR-5 hydrolyzes
    other tested beta-lactams, but ceftiofur is absent from Table 2 kinetics. The
    exact ceftiofur counterion is not specified in the main text. No ceftiofur-specific
    catalytic value or exact-sodium numeric claim follows.
  snapshot_sha256: 49001d32c9c8863d1fa49f979c9a90fa4cc7f9c8c84e143ce19aa40abadee7f5
- evidence_id: pbp-primary
  kind: primary_source
  reference: PMID:34577037; DOI:10.3390/molecules26185569; https://pmc.ncbi.nlm.nih.gov/articles/PMC8470104/
  locator: Full original XML main text read; Results 2.1.1, Table 2 and Methods 3.1–3.2
    distinguish competition measurements from later docking.
  accessed_at: '2026-10-21T12:03:03Z'
  support: partial
  summary: Commercial ceftiofur from the National Institutes for Food and Drug Control
    is tested by direct competitive ELISA with recombinant PBP2x*. Table 2 reports
    IC50 2.63 ng/mL; standards compete with an enzyme marker for 30 minutes at 37
    degrees C before color measurement. This is a measured competition endpoint, not
    a dissociation constant, bacterial MIC or whole-cell causal chain. The material
    counterion is not specified. Figure 5 uses molecular docking against a PBP2x structure,
    not a new ceftiofur co-crystal or direct measurement of those modeled contacts.
  snapshot_sha256: 0ea9e600b24c72d0f375ea1b17593a4f42ed8ab7dab70f74dc05918265b7045a
- evidence_id: pbp-origin
  kind: primary_source
  reference: PMID:23336133; DOI:10.3967/0895-3988.2013.02.004; https://pubmed.ncbi.nlm.nih.gov/23336133/
  locator: Complete indexed original abstract, cited as reference 24 by the 2021 assay
    paper.
  accessed_at: '2026-10-21T12:11:51Z'
  support: partial
  summary: The earlier assay study identifies recombinant PBP2x* from S. pneumoniae
    R6 and reports ceftiofur among beta-lactams detectable in a milk residue assay.
    This verifies the origin and analytical context of the receptor system; the abstract
    does not supply an exact sodium material specification or whole-cell antibacterial
    mechanism.
- evidence_id: brands
  kind: authority
  reference: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b6fed070-b398-4348-9927-9891f78c7c31;
    https://www.hpra.ie/find-a-medicine/for-animal-use/suspended-medicines/details/15
  locator: NAXCEL Description/chemical-name/ingredient sections; HPRA archived Excenel
    4 g powder identity.
  accessed_at: '2026-10-21T12:03:49Z'
  support: supports
  summary: NAXCEL explicitly contains ceftiofur sodium and describes bactericidal
    cell-wall-synthesis inhibition. HPRA explicitly identifies ceftiofur sodium as
    the active substance of Excenel 4 g sterile powder. The generic Excenel alias
    therefore cannot be rejected merely because another formulation uses hydrochloride.
    These are product-qualified brand attestations, not exact equivalence of all excipients,
    formulations, markets or regulatory histories.
  snapshot_sha256: 1a253a29ea8a51688ccced397fe9ba2793c43effdd4e1db12c3db1c54d29911c
- evidence_id: structured
  kind: database
  reference: 026-root-imodulondb-datasets.txt; 026-root-imodulondb-pbp.txt
  locator: Root structured adapter outputs generated before open web research; both
    outputs independently read.
  accessed_at: '2026-10-21T12:11:51Z'
  support: context_only
  summary: The dataset catalog has no E. stercoris entry. The penicillin query in
    e_coli/precise1k returns b2430/yfeW, penicillin-binding protein 4B, and zero iModulon
    hits. Neither finding establishes or refutes ceftiofur binding or EBR-5 resistance.
    There is no relevant component to summarize; computational expression membership
    is not antibacterial mechanism evidence.
  snapshot_sha256: b0f3ec2d7316806c534510fc9e133a264a0079b8388c2e423af73d3f40edf70a
- evidence_id: scope-map
  kind: record_content
  reference: curation/ncbi_ast_drug_map.tsv
  locator: Maintained ceftiofur mapping row 24, captured before this assessment.
  accessed_at: '2026-10-21T12:11:51Z'
  support: context_only
  summary: The AST mapping already distinguishes neutral ceftiofur PubChem 6328657
    from the lexical sodium corpus candidate CHEBI:31383 and labels that AST mapping
    MISSING_CORPUS_RECORD. This is maintained scope context, not primary proof and
    not an instruction to exclude the valid sodium record. The AST adoption lane remains
    deferred; no AST requests or source contact were made.
- evidence_id: search
  kind: search
  reference: 259-inclusive-local-hits.txt; public exact ceftiofur/PBP and sodium-brand
    searches
  locator: Inclusive local search, bounded public discovery and source retrieval.
  accessed_at: '2026-10-21T12:11:51Z'
  support: context_only
  summary: Hidden and ignored files were included. Hits identify the native record,
    exact source rows, readiness queue, AST scope decision and generated projections;
    no exact corrective decision or overlay was found in the searched areas. Public
    PBP searches yielded the original analytical competition study. Search snippets
    and the broad 259-primary-search.json discovery collection are not treated as
    inspected experimental support.
  snapshot_sha256: ebc9499c02ea148dfd92c4782c76b1c5236069c588981934a8f918c07b223b59
  search_scope: rg --no-ignore --hidden -n -F for CHEBI:31383, ceftiofur, full sodium
    InChIKey and ARO mint across data, curation, conf, scripts, src, docs, .claude,
    reviews and reports; public ceftiofur plus penicillin-binding/PBP/affinity and
    Naxcel/Excenel sodium queries on 2026-10-21.
- evidence_id: validation
  kind: validation
  reference: 259-focused-results.json;259-schema.log;259-strict.log;259-chemistry.json;026-root-xref-check.json;259-candidate-chemistry.json
  locator: Actual root focused gate logs and independently inspected chemical outputs;
    additional sodium candidate parse.
  accessed_at: '2026-10-21T12:11:51Z'
  support: supports
  summary: Schema and strict validation pass with zero errors. Native SMILES and InChI
    agree on composition, charge, masses, two R centres and full key; sole ARO mint
    matches. External PubChem/ChEMBL neutral graphs disagree in composition and full
    key. Both KEGG structures and the separately parsed PubChem sodium candidate match
    the native salt. Chemical consistency alone does not validate external exact-identity
    links.
  snapshot_sha256: 2e2e0d0bf8021374008723c6bbed4c80c327b0e20af4e703f35f84dc0dfa3e84
assessments:
- assessment_id: identity
  area: identity
  topic: Exact ceftiofur sodium structure
  outcome: supported
  summary: The native graph, ChEBI identity, CAS attestation and descriptors agree
    on one sodium salt. The generic source label merits explicit salt qualification
    in future display/curation, but is not sufficient evidence to replace this structure
    or exclude a supported antibacterial salt. Naxcel and Excenel powder have official
    sodium attestations.
  target_ids:
  - CHEBI:31383
  evidence_ids:
  - record
  - chebi
  - salt-xrefs
  - brands
  - validation
- assessment_id: equivalence
  area: identity
  topic: Neutral chemical xrefs on a sodium record
  outcome: concern
  summary: PubChem 6328657 and ChEMBL 222913 encode neutral ceftiofur, not the exact
    sodium structure. The difference is confirmed from independently parsed official
    structures, not inferred from naming alone. ARO is the source of the mixed references.
  target_ids:
  - CHEBI:31383
  evidence_ids:
  - neutral-xrefs
  - salt-xrefs
  - card
  - source
- assessment_id: classification
  area: scope
  topic: Antibacterial class and broader cephalosporin parent
  outcome: supported
  summary: The structural class is genuinely broader, while the sodium-material study
    directly supports antibacterial activity. Empty ChEBI role ancestry in the lookup
    row does not erase ARO filing or establish a missing required role.
  target_ids:
  - CHEBI:31383
  evidence_ids:
  - sodium-primary
  - card
  - source
  - brands
- assessment_id: target
  area: evidence
  topic: PBP target and definition citation scope
  outcome: unknown
  summary: The imported target honestly remains PRIMARY_EVIDENCE_NEEDED with unspecified
    organism and assay. Later primary competition data support a bounded PBP2x interaction,
    but not an exact sodium-specific lysis chain. The 1987 abstract supports activity
    and does not settle whether its inaccessible full text substantiates every mechanism
    clause. Retain this as a citation-scope limitation, not a confirmed erroneous
    citation or a claim that no primary PBP evidence exists.
  target_ids:
  - CHEBI:31383
  evidence_ids:
  - record
  - sodium-primary
  - pbp-primary
  - pbp-origin
  - brands
  - structured
- assessment_id: resistance
  area: evidence
  topic: EBR-5 phenotype versus biochemical mechanism
  outcome: supported
  summary: The native item is explicitly a CARD assertion. The original gene-transfer
    experiment corroborates reduced ceftiofur susceptibility in its named recombinant
    system. Antibiotic inactivation is the enzyme-family mechanism, but no ceftiofur-specific
    purified-enzyme kinetic result or salt specification is present in the inspected
    main text. Preserve database status and condition any literature enrichment on
    this scope.
  target_ids:
  - CHEBI:31383
  evidence_ids:
  - record
  - card
  - ebr-primary
- assessment_id: completeness
  area: completeness
  topic: Optional enrichments and native scientific status
  outcome: unknown
  summary: The absence of numerical MICs, producer, clinical status, causal graph,
    mode enum and datasets is not a separate required-field defect. Activity and target
    enrichment could be useful after material and assay qualification. A field isolate
    that resists ceftiofur is not its producer, and antibody-production host experiments
    are not antibacterial targets. SEEDED remains appropriate until exact xrefs and
    native sign-off criteria are resolved.
  target_ids:
  - CHEBI:31383
  evidence_ids:
  - record
  - sodium-primary
  - ebr-primary
  - pbp-primary
- assessment_id: ownership
  area: ownership
  topic: Maintained source correction and provenance
  outcome: supported
  summary: The actual owner is the ARO source/extractor/seeder path, with ChEBI supplying
    sodium structure through a lookup. The AST map is context only. All eighteen captured
    input hashes remain unchanged; no record mutation or scientific-status promotion
    is part of this review.
  target_ids:
  - CHEBI:31383
  evidence_ids:
  - source
  - scope-map
  - search
  - validation
- assessment_id: checks
  area: schema
  topic: Focused gate success and scientific limits
  outcome: supported
  summary: Root focused schema, strict and chemical checks pass. Those checks do not
    compare the currently resolved external PubChem/ChEMBL structures, so they do
    not invalidate the major finding.
  target_ids:
  - CHEBI:31383
  evidence_ids:
  - validation
  - neutral-xrefs
findings:
- finding_id: F1
  issue_key: ceftiofur-sodium-neutral-acid-chemical-xrefs
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile neutral-acid chemical links with the exact sodium identity
  description: The native CHEBI:31383 structure is ceftiofur sodium, RFLHUYUQCKHUKS-JUODUXDSSA-M,
    but xrefs[2] ChEMBL222913 and xrefs[3] PubChem6328657 are neutral ceftiofur, ZBHXIWJRIFEVQY-IHMPYVIRSA-N.
    Independent official structure parses confirm the missing sodium and different
    composition. The current ARO page and adopted row mix these identities. Preserve
    the valid sodium graph and reconcile only exact chemical links through the maintained
    source path. PubChem23671563 is an independently verified sodium candidate; no
    sodium ChEMBL replacement is established.
  target_ids:
  - CHEBI:31383
  field_paths:
  - xrefs[2]
  - xrefs[3]
  evidence_ids:
  - record
  - source
  - chebi
  - neutral-xrefs
  - salt-xrefs
  - card
  - validation
  rule_id: 'docs/CURATION.md: every chemical xref denotes the same structure; native-review-checklist:
    Equivalence'
  native_severity: major
  normalization_reason: A confirmed salt/neutral mismatch in two structure-exact identifiers
    can misjoin chemical and activity data. The underlying native identity is coherent,
    so this is a major cross-reference correction rather than a blocker requiring
    wholesale structure replacement.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted mixed cross-reference assertion
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible source normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Structure selection and exact-xref gate
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-specific identity policy where appropriate
actions:
- action_id: A1
  description: Correct the maintained cross-reference mapping and reproduce a sodium-only
    exact chemical identity set.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:31383
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted mixed cross-reference assertion
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible source normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Structure selection and exact-xref gate
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-specific identity policy where appropriate
  acceptance_checks:
  - Remove or replace the neutral PubChem and ChEMBL identifiers from the sodium record
    through a reproducible source correction or maintained mapping; do not relabel
    neutral identities as exact sodium links.
  - Verify any replacement from its full chemical graph, counterion, protonation and
    stereochemistry. PubChem23671563 already matches the native graph and full key;
    other same-key tautomer results require separate adjudication.
  - Preserve CHEBI:31383, sodium composition, two R centres, source mint and claim
    provenance unless a separately justified scope decision changes them. Do not replace
    the entire record with neutral ceftiofur.
  - Rerun the authorized source/seeder path and focused schema/strict plus applicable
    reference, history and corpus gates; confirm regeneration does not reintroduce
    the wrong exact links.
- action_id: A2
  description: If mechanism or resistance enrichment is undertaken, add claim-specific
    primary support with explicit material and assay scope.
  finding_ids: []
  target_ids:
  - CHEBI:31383
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/ceftiofur.yaml
    role: Curator-owned literature additions beside imported source assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Imported definition and database-edge provenance must remain distinguishable
  acceptance_checks:
  - Keep the 1987 reference bounded to the inspected sodium activity evidence unless
    its full text is obtained; do not treat unavailable full text as proof of a bad
    citation.
  - Represent the PBP2x competitive ELISA endpoint as IC50 in its analytical context,
    not Kd, MIC or measured whole-cell lysis. Retain unspecified ceftiofur counterion
    and distinguish docking from experimental binding.
  - For EBR-5 retain strain, vector, inducer and selection conditions, exact inequalities
    and units. Do not infer ceftiofur-specific kinetic constants from Table2 or transfer
    unspecified material into an exact sodium measurement without qualification.
  - Use the native validated writer/history workflow only in a separately authorized
    curation task; this optional enrichment is not a required correction by itself.
limitations:
- The whole native record and actual maintained rows were read. Initial seventeen
  input hashes were preserved and the actual AST mapping context appended before judgment;
  all eighteen were rechecked unchanged.
- The sole adopted definition PMID was read at full indexed-abstract depth. Both original
  1987 AVMA routes returned an HTML challenge rather than full article/PDF; exact
  numerical assays and complete causal support from that paper remain unverified.
- The EBR-5 original main-text XML, including both tables and their footnotes, was
  read. Its supplementary methods were not independently audited; no exact ceftiofur
  counterion or ceftiofur-specific purified-enzyme kinetics are inferred.
- The 2021 PBP paper was read in full main-text XML; figures were not used as crystallographic
  evidence. The 2013 precursor was read at complete abstract depth. Exact assay material
  salt and the full whole-cell causal chain remain unresolved.
- Official chemical and product-label pages were inspected without paid registry access.
  Brand/product identity was checked in specific formulations; no universal cross-jurisdictional
  brand or clinical-status assertion is made.
- The structured adapter outputs were generated by root before web research and independently
  inspected here. They provide no matched causal experiment; absence of a relevant
  module or species is not negative biological evidence.
- Discovery results were used only as leads. In particular, the broad primary-search
  response is not claimed as a fully inspected literature survey. The maintained AST
  adoption restriction was respected; no new AST endpoint requests or contact occurred.
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
