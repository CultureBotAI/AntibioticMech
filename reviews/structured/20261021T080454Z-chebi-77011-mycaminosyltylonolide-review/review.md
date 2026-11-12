# Review of CHEBI:77011 (5-O-mycaminosyltylonolide)

- Review: 20261021T080454Z-chebi-77011-mycaminosyltylonolide-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:57:59Z
- Finished UTC: 2026-10-21T08:04:54Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Native SMILES, InChI, PubChem and KEGG agree on one stereodefined neutral OMT entity. Current ChEBI parents, inherited antimicrobial role and ARO macrolide class are valid. Two minor findings identify verified primary activity/mechanism enrichment and a recoverable patent-locator formatting problem. Ribosome-binding species, polypeptide-dependent translation effects, derivative results and potentiator combinations require separate scope.

## Scope And Provenance

Entire mixed ChEBI/ARO record, ownership, all molecular/ontology/source identities, external and document xrefs, exact OMT ribosome binding and translation experiments, antibacterial observations and combination/derivative boundaries.

Selection: Path-ordered unreviewed queue index 054; exactly one record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:77011 | data/antibiotics/antibacterial/5-o-mycaminosyltylonolide.yaml | generated | 5-O-mycaminosyltylonolide |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record LinkML validation | passed | True | CHEBI:77011 | Exit 0; No issues found. |
| Documented per-record closed-schema validation | passed | True | CHEBI:77011 | Exit 0; one file, zero ERROR rows. |
| Independent structure and minted-identifier comparison | passed | False | CHEBI:77011 | Exit 0. Native SMILES/InChI, PubChem isomeric SMILES and KEGG Molfile agree on full key, formula, neutral charge, masses, 12 assigned centres and two E double bonds. Both source-concept mints reproduce. |
| Current source term, parent, role and structure comparison | passed | False | CHEBI:77011 | Exit 0. Four ChEBI parents, inherited CHEBI:33281 antimicrobial role, valid ARO:3007570 and ARO:0000000 class, source strings and Greek beta/ASCII beta synonym equivalence match. Current CARD confirms merged identity. No exact target/resistance edge is present in the adopted ARO tables. |
| Structured expression-module adapter applicability | not_applicable | False | CHEBI:77011 | The current record contains chemical identity/classification only, with no gene, protein, pathway, regulator, stress response or dataset annotation. Ribosome/efflux terms occur only in literature being reviewed, not an existing annotation requiring module validation. |
| Initial supplementary source-download helper | failed | False | CHEBI:77011 | Exit 1 before requests because this exact ChEBI term has no direct has_role link. The inherited role was subsequently resolved through its macrolide-antibiotic parent; corrected downloads and source comparison succeeded. This was a helper assumption, not a native record defect. |
| Authoritative full QC | failed | True | CHEBI:77011 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:77011 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:77011 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:77011 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:77011 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:77011 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:77011 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:77011 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:77011 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral stereodefined OMT

identity: supported. Targets: CHEBI:77011.

All four structural representations agree. This is monoglycosylated OMT, retaining its aldehyde and C23 hydroxyl; tylosin, protylonolide analogues, oxime and peptide derivatives remain separate.

### Structural parents, inherited role and ARO class

grounding: supported. Targets: CHEBI:77011.

Four ChEBI parents fit; broad antimicrobial role is inherited. ARO:0000000 is the correct macrolide class and the merged ARO entity matches PubChem. Direct experiments support antibacterial filing.

### Exact identity and document references

grounding: concern. Targets: CHEBI:77011.

PubChem/KEGG/CARD mappings support exact identity. Three other authority target checks remain incomplete. Patents are correctly placed as documents, but one literal publication token fails its resolver and has a supported normalized counterpart.

### Ribosomal binding and conditional translation inhibition

evidence: supported. Targets: CHEBI:77011.

Direct parent binding and translation measurements support a ribosomal mechanism. Preserve E. coli binding in 1983, D. radiodurans binding in 2010 and E. coli lysate translation separately; GFP and Fluc outcomes differ.

### Individual-compound versus combination observations

evidence: supported. Targets: CHEBI:77011.

Exact OMT has primary antibacterial activity. Colistin/PMBN combination MICs cannot become single-agent values, and partner efficacy differs by organism and strain.

### Concrete primary annotation opportunity

completeness: concern. Targets: CHEBI:77011.

The seed lacks experimentally supported exact-parent mechanism/activity annotations available from inspected primary sources. This is a specific useful enrichment, not an error inferred from optional empty slots.

### Semisynthesis versus biological production

scope: not_applicable. Targets: CHEBI:77011.

No producer object is asserted. The patent fermentation of a precursor followed by acid hydrolysis does not itself prove direct biosynthesis of OMT; do not infer a producer from tylosin production.

### Efflux and combination context

scope: unknown. Targets: CHEBI:77011.

No resistance mechanism is asserted and adopted ARO tables have no exact edge. Source abstracts support an efflux/permeability-sensitive context, but not an identified individual transporter-specific direct biochemical interaction with OMT.

### Clinical, graph and dataset scope

representation: not_applicable. Targets: CHEBI:77011.

No clinical, graph or dataset annotation is asserted. In vitro combinations and derivative toxicity experiments do not establish parent-compound clinical efficacy or safety.

### Source merge and generated history

ownership: supported. Targets: CHEBI:77011.

Both source-concept mints and merged exact identity reproduce. Four seed/reseed events are consistent. Correct document identifiers in maintained source handling and add primary annotations through the validated writer.

### Focused schema and independent validation

schema: supported. Targets: CHEBI:77011.

Both native focused validators, independent chemistry and source assertions pass. The corrected inherited-role retrieval assumption and external link failures are preserved separately.

## Findings

### F1: Exact-parent ribosome and translation evidence can enrich the seed

minor / open / confirmed; issue key: chebi-77011-primary-ribosome-translation-evidence-completeness.

The record has no primary mechanism or activity annotation even though original exact-OMT binding, polypeptide-dependent translation and strain-level antibacterial observations are available. These support precise curation without transferring derivative or combination effects.

### F2: One optional patent locator needs publication-number normalization

minor / open / confirmed; issue key: chebi-77011-patent-publication-number-normalization.

Source-derived patent:US2006014707 produces 404 at its declared resolver. The corresponding zero-padded publication US20060014707A1 is accessible and explicitly uses OMT as a starting material. Retain the source token as provenance while supplying a validated resolvable document identifier.

## Recommended Actions And Acceptance Checks

### A1

Curate exact-parent ribosome/translation mechanism and strain-specific antibacterial evidence with assay and combination qualifiers.

- Use original 1983 compound 7 only. ID50=0.5µM is radioligand competition with E. coli ribosomes, not a dissociation constant. Preserve exact MIC strains and µg/mL units and retrieve cited full antimicrobial methods before claiming missing assay details.
- Use 2010 apparent Kd=3nM for D. radiodurans 70S binding separately from E. coli-lysate translation. Preserve Fluc IC50=0.15µM and poor GFP inhibition; do not describe universal inhibition of every translated polypeptide. Identify modeled contacts and displacement proposals as interpretation.
- Ground the target at its supported ribosomal/RNA level rather than inventing a protein UniProt target. Do not transfer C23/C20 derivative binding contacts, resistance or safety claims to OMT.
- Represent PMBN and colistin combination experiments separately from single-agent susceptibility. The adopted 2023 PMID uses polymyxin B nonapeptide, not polymyxin B; the accessible supplement contains comparator drugs only. Source ARO wording is not a native OMT-alone activity assertion.
- Attach claim-level sources through validated writer/history and run schema/strict, full-corpus reference/history/term and QC gates before native REVIEWED.

### A2

Normalize the source-derived patent publication locator to a verified resolvable document identifier, preserving the original source token and document scope.

- Verify US20060014707A1 is the intended source publication, preserve provenance of US2006014707 and implement correction in maintained source extraction/normalization rather than only generated YAML.
- Regenerate document_xrefs and verify the resulting declared resolver retrieves the inspected Sixteen-member macrolide antiinfective agents document. Keep patents out of exact chemical xrefs and do not import derivative claims as parent evidence.
- Run the native validation and reproducibility gates and preserve validated history.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/5-o-mycaminosyltylonolide.yaml; Entire generated record | supports | Read definition, five synonyms, five parents including ARO class, inherited antimicrobial role, full structure, six identity xrefs, three document xrefs, two source concepts and four history events. No primary evidence, mode, target, activity observation, producer, resistance, clinical, graph or dataset object is asserted. |
| inventory | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; Complete CHEBI:77011 and ARO:3007570 rows, related edge/promotion tables and ignored-inclusive local discovery | supports | The ChEBI row supplies exact identity/structure and three patent leads; it contains no PMID citations. The ARO row supplies macrolide class, matching alias/PubChem ID and one source PMID lead, 37208456. No exact target/resistance edge or primary promotion/curator override was found in the ignored-inclusive maintained-input search. |
| ownership | scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Source import, structure_from_chebi, source merging, normalize_xref and document_xrefs placement | supports | Generated identity and document strings belong to source import and regeneration. Patent documents are correctly separated from exact-structure xrefs; the existing normalizer does not pad publication numbers. Primary annotations belong to curator-owned fields with validated history. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:77011; 054-chebi.html and 054-ols.json | supports | Current native ChEBI entry matches the compound, valid fully specified structure, five aliases and source document strings. Beta-D-mycaminose attached to tylonolide is distinct from tylosin and other glycosylated or C20/C23-modified congeners. |
| ontology | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_77011; 054-parents.json, 054-parentroles.json and 054-roleterm.json | supports | Four non-obsolete parents are aldehyde, macrolide antibiotic, enone and monosaccharide derivative. CHEBI:33281 means antimicrobial agent and is inherited from macrolide antibiotic CHEBI:25105, rather than directly attached to this term. Its broad role is preserved while ARO and direct experiments support ANTIBACTERIAL filing. |
| aro | ARO:3007570; ARO:0000000; https://card.mcmaster.ca/ontology/46343; 054-card.html; read-only original downloads/aro.obo cache, hash recorded in 054-source-check.json | supports | ARO:3007570 names mycaminosyltylonolide, links PubChem 6437420 and is_a ARO:0000000, the valid macrolide-antibiotic class. The all-zero local class ID is legitimate. Current CARD and cached ontology agree. Source ARO definition says polymyxin B, whereas its PMID:37208456 concerns polymyxin B nonapeptide; the native record adopts the chemical ChEBI definition, not that source activity wording. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6437420/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; 054-pubchem.json | supports | The ARO-linked PubChem entity has the same stereospecific InChIKey and neutral C31H51NO10 structure as ChEBI, supporting the source merge. |
| kegg | https://rest.kegg.jp/get/C12002; 054-kegg.html and 054-keggmol.html, plain text despite suffix | supports | KEGG C12002 and its Molfile match exact stereochemistry, key, formula and charge. Pathway or reaction placement is not independent proof of a producing organism or microbial antimicrobial target. |
| xref-limits | cas:61257-02-1; metacyc.compound:CPD-15944; reaxys:4730900; 054-fetch-results.json, CAS and BioCyc responses | context_only | CAS returned a JavaScript application shell; MetaCyc returned an account-access page. Reaxys target was not independently resolved. Source strings reproduce, but direct exact-structure authority verification remains incomplete for these three xrefs. |
| patent1 | https://patents.google.com/patent/US20060014707A1/en; 054-patent1.html; description of Figure 1 synthetic route; native literal resolver in 054-final-fetch-results.json | supports | The normalized publication US20060014707A1, Sixteen-member macrolide antiinfective agents, explicitly identifies 5-O-mycaminosyltylonolide as starting material 1. The native/source token US2006014707 omits one leading zero from the seven-digit serial portion, and its declared Google-patent resolver returns 404. This document is relevant provenance, not an exact-identity equivalence or proof that every derivative activity belongs to OMT. |
| patent2 | https://patents.google.com/patent/US4537957A/en; 054-patent2.html; summary, OMT preparation examples and claims | supports | US4537957 is directly relevant to OMT production by acid treatment of demycinosyltylosin. The described Streptomyces fermentation produces the precursor DMT; subsequent acid hydrolysis yields OMT. These passages do not by themselves justify a structured claim that the strain biosynthesizes OMT directly. |
| patent3 | https://patents.google.com/patent/WO2013076169A1/en; 054-patent3.html; paragraph 0102, preparation of YT106 | supports | WO2013076169 explicitly prepares parent OMT YT106 from tylosin before further derivative synthesis. The document reference is correctly in document_xrefs; downstream derivative activities and claims remain separate. |
| primary1983 | PMID:6662812; DOI:10.7164/antibiotics.36.1709; complete 054-primary1983.pdf, Methods and Table 1 compound 7; page1711 visually inspected | supports | Exact parent OMT compound 7 competes with radiolabeled tetrahydroleucomycin A3 for E. coli ribosome binding, ID50 0.5 µM. Table 1 MICs are 1.6 µg/mL for B. subtilis PCI219 and S. aureus FDA209P, 0.1 for M. luteus PCI1001 and 25 for E. coli NIHJ. These are strain-specific values; ID50 is a competition endpoint, not Kd or MIC. Full broth/agar/inoculum/timing details are not supplied here and require the cited methods. |
| primary2010 | PMID:20534348; DOI:10.1016/j.chembiol.2010.04.008; 054-primary2010.pdf Results, Figures 4-6 and Experimental Procedures; page 510 visually inspected | supports | OMT competes with erythromycin for empty D. radiodurans 70S ribosomes; text reports apparent Kd 3 nM. In a separate E. coli lysate translation system it inhibits firefly-luciferase synthesis, IC50 0.15 µM, but poorly inhibits GFP synthesis. This supports compound-specific translation effects with polypeptide dependence. Proposed drug displacement and modeled atomic contacts are mechanistic interpretations, not a new experimentally solved OMT structure. |
| primary2023 | PMID:37208456; DOI:10.1038/s41429-023-00628-9; abstract in 054-primarycore.json; publisher abstract/metadata and 054-supp2023.docx | supports | The sole adopted PMID lead studies OMT with polymyxin B nonapeptide against MDR P. aeruginosa, following discovery in efflux-pump deletion strain YM64. Accessible supplement Table S1 contains comparator-antibiotic MICs for clinical strains, not OMT combination values. Main quantitative combination tables were inaccessible; no values or specific pump-substrate conclusion are inferred. |
| primary2024combo | DOI:10.1248/bpbreports.7.5_157; Full 054-primary2024combo.html, Methods and Tables 1-3 | supports | Exact synthesized OMT is tested alone and with colistin. For E. coli ATCC25922, Table 2 gives OMT alone &gt;64 µg/mL and colistin MIC 0.5; OMT MIC is 2 with half-MIC colistin and 8 with quarter-MIC colistin. These are conditional combination values, not OMT-alone susceptibility. Potentiation varies by strain/species; proposed clinical benefit remains untested. |
| derivative-boundary | PMID:24090034; PMID:16873579; PMID:39691534; Abstracts in 054-primarycore.json; selected accessible 2024 publisher/PMC narrative and tables | context_only | 2013 amino-acid conjugates, 2006 oxime derivatives and 2024 C23 derivatives are distinct molecules. Parent controls may inform OMT when explicitly identified; enhanced derivative potency, resistance avoidance, c9 docking and toxicity cannot be transferred to the parent. No such derivative-based native claim is asserted. |
| chemistry | Independent RDKit/hashlib calculation; 054-chemistry.py and 054-chemistry.json | supports | Native SMILES/InChI, PubChem and KEGG yield WGUJDBLMJBJUQU-VKRLOHBMSA-N, C31H51NO10, charge 0 and matching masses. Twelve centres are assigned, both alkene stereochemistries are E, and both source-concept identifiers reproduce. |
| source-check | Focused source/ontology assertion checks; 054-source-check.py and 054-source-check.json | supports | All asserted source identity/term/class/inherited-role checks pass, including both ARO terms. Source xref/document-string matching is separate from exact target verification. Greek beta and ASCII beta naming differences were explicitly normalized. |
| retrieval | Public source retrieval attempts; 054-more-fetch-initial.py preserves initial code; corrected 054-more-fetch.py, 054-more-fetch-results.json and 054-final-fetch-results.json | context_only | Initial helper exited 1 before requests because no direct has_role link existed. The corrected source workflow follows the parent role, retrieves source documents and passes. Primary2024 derivative XML returned 500; the literal native patent resolver returned 404 while normalized publication succeeded. These retrieval outcomes are not unexecuted checks. |
| validation | just validate; just validate-strict; Actual isolated batch-006 executions; 054-strict.tsv | supports | Both documented focused native validators exited 0; strict scanned one record with zero ERROR rows. Independent chemistry and current-source comparisons also exited 0. |
| search | Ignored-inclusive local and bounded primary-source discovery; 054-local-hits.txt; maintained inputs and primary databases/publisher searches | context_only | Exact OMT studies were distinguished from tylosin, protylonolide congeners, C20/C23 derivatives and potentiator combinations. No exhaustive literature or universal resistance claim is made. |

## Limits And Additional Notes

- CAS returned an application shell, MetaCyc an account-access page and Reaxys exact target was not independently resolved. Current source string matching does not complete those authority target checks.
- The 2023 main paper remains abstract/metadata only; its accessible supplement reports comparator-antibiotic MICs, not the missing OMT combination table. All quantitative combination values cited here come from the independently inspected2024 full paper.
- The 1983 paper reports exact strains and MICs but refers out for assay methodology. No unreported medium, inoculum or incubation conditions are invented. Its competition ID50 and 2010 apparent Kd are different endpoints and species.
- The 2010 PDF text extractor renders micro units as m in places; the relevant page 510 and 1983 Table 1 were visually checked. Values above use verified µM units. Polypeptide-dependent translation effects do not establish an exclusive atomic binding model.
- The initial supplementary fetch helper failed because it assumed a direct has_role link; the corrected inherited-role lookup succeeds. The original helper code is preserved. A local optional HTML parser dependency was unavailable; source text was successfully extracted using the Python standard library.
- The 2024 derivative-paper XML endpoint returned 500. Only accessible abstract/selected article text was used for derivative scope context, not quantitative parent mechanism claims.
- The failed literal patent resolver and normalized accessible publication are both retained. Their relevance was checked in document text, not inferred from automated chemical tags alone.
- This bounded review does not exhaust all literature or establish native REVIEWED status. Primary curation, document normalization, unresolved checks and required gates remain outstanding.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Only scratch review artifacts were written. No native record, maintained input, generated artifact or curation history was modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T080454Z-chebi-77011-mycaminosyltylonolide-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of CHEBI:77011 (5-O-mycaminosyltylonolide)
started_at: '2026-10-21T07:57:59Z'
finished_at: '2026-10-21T08:04:54Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Exact neutral OMT identity and antibacterial classification supported;
  primary ribosome/translation evidence and one document-locator repair await curation
scientific_review: true
summary: Native SMILES, InChI, PubChem and KEGG agree on one stereodefined neutral
  OMT entity. Current ChEBI parents, inherited antimicrobial role and ARO macrolide
  class are valid. Two minor findings identify verified primary activity/mechanism
  enrichment and a recoverable patent-locator formatting problem. Ribosome-binding
  species, polypeptide-dependent translation effects, derivative results and potentiator
  combinations require separate scope.
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
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: curation/curator_antibiotics.tsv
    sha256: 224cbb7261add427184b2762a29c2ff3e85c85e0a06cf22b144545346487247b
    role: context
  - path: curation/decisions.tsv
    sha256: a5834b44307b0449b0df9362c551b7fcd707f3ae51f73d429d37d51f5a169d61
    role: context
  - path: data/antibiotics/antibacterial/5-o-mycaminosyltylonolide.yaml
    sha256: 624462f572512a470d13e420afe73b5cd4966ce6dd01e0f984b8a92891bcdc17
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
scope:
  description: Entire mixed ChEBI/ARO record, ownership, all molecular/ontology/source
    identities, external and document xrefs, exact OMT ribosome binding and translation
    experiments, antibacterial observations and combination/derivative boundaries.
  selection: Path-ordered unreviewed queue index 054; exactly one record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:77011
targets:
- target_id: CHEBI:77011
  path: data/antibiotics/antibacterial/5-o-mycaminosyltylonolide.yaml
  label: 5-O-mycaminosyltylonolide
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
    role: ARO identity merging and macrolide class
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: ARO exact target edges
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: ARO exact resistance edges
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Primary evidence promotion decisions
checks:
- check_id: schema
  name: Documented per-record LinkML validation
  status: passed
  required: true
  summary: Exit 0; No issues found.
  target_ids:
  - CHEBI:77011
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/5-o-mycaminosyltylonolide.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented per-record closed-schema validation
  status: passed
  required: true
  summary: Exit 0; one file, zero ERROR rows.
  target_ids:
  - CHEBI:77011
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/5-o-mycaminosyltylonolide.yaml --out /private/tmp/am-review-session/054-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Independent structure and minted-identifier comparison
  status: passed
  required: false
  summary: Exit 0. Native SMILES/InChI, PubChem isomeric SMILES and KEGG Molfile agree
    on full key, formula, neutral charge, masses, 12 assigned centres and two E double
    bonds. Both source-concept mints reproduce.
  target_ids:
  - CHEBI:77011
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/054-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: source-check
  name: Current source term, parent, role and structure comparison
  status: passed
  required: false
  summary: Exit 0. Four ChEBI parents, inherited CHEBI:33281 antimicrobial role, valid
    ARO:3007570 and ARO:0000000 class, source strings and Greek beta/ASCII beta synonym
    equivalence match. Current CARD confirms merged identity. No exact target/resistance
    edge is present in the adopted ARO tables.
  target_ids:
  - CHEBI:77011
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/054-source-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ontology
  - source-check
- check_id: imodulondb
  name: Structured expression-module adapter applicability
  status: not_applicable
  required: false
  summary: The current record contains chemical identity/classification only, with
    no gene, protein, pathway, regulator, stress response or dataset annotation. Ribosome/efflux
    terms occur only in literature being reviewed, not an existing annotation requiring
    module validation.
  target_ids:
  - CHEBI:77011
  evidence_ids:
  - record
- check_id: source-download-initial
  name: Initial supplementary source-download helper
  status: failed
  required: false
  summary: Exit 1 before requests because this exact ChEBI term has no direct has_role
    link. The inherited role was subsequently resolved through its macrolide-antibiotic
    parent; corrected downloads and source comparison succeeded. This was a helper
    assumption, not a native record defect.
  target_ids:
  - CHEBI:77011
  command: python /private/tmp/am-review-session/054-more-fetch.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - retrieval
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:77011
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
  - CHEBI:77011
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
  - CHEBI:77011
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
  - CHEBI:77011
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
  - CHEBI:77011
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
  - CHEBI:77011
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
  - CHEBI:77011
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
  - CHEBI:77011
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
  - CHEBI:77011
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/5-o-mycaminosyltylonolide.yaml
  locator: Entire generated record
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: Read definition, five synonyms, five parents including ARO class, inherited
    antimicrobial role, full structure, six identity xrefs, three document xrefs,
    two source concepts and four history events. No primary evidence, mode, target,
    activity observation, producer, resistance, clinical, graph or dataset object
    is asserted.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv
  locator: Complete CHEBI:77011 and ARO:3007570 rows, related edge/promotion tables
    and ignored-inclusive local discovery
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: The ChEBI row supplies exact identity/structure and three patent leads;
    it contains no PMID citations. The ARO row supplies macrolide class, matching
    alias/PubChem ID and one source PMID lead, 37208456. No exact target/resistance
    edge or primary promotion/curator override was found in the ignored-inclusive
    maintained-input search.
- evidence_id: ownership
  kind: record_content
  reference: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  locator: Source import, structure_from_chebi, source merging, normalize_xref and
    document_xrefs placement
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: Generated identity and document strings belong to source import and regeneration.
    Patent documents are correctly separated from exact-structure xrefs; the existing
    normalizer does not pad publication numbers. Primary annotations belong to curator-owned
    fields with validated history.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:77011
  locator: 054-chebi.html and 054-ols.json
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: Current native ChEBI entry matches the compound, valid fully specified
    structure, five aliases and source document strings. Beta-D-mycaminose attached
    to tylonolide is distinct from tylosin and other glycosylated or C20/C23-modified
    congeners.
  snapshot_sha256: 8c56378c7f9ee3951625478b05e9ca2a1a1c4b20fb73e9fd71cb1db5b10dd1f8
- evidence_id: ontology
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_77011
  locator: 054-parents.json, 054-parentroles.json and 054-roleterm.json
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: Four non-obsolete parents are aldehyde, macrolide antibiotic, enone and
    monosaccharide derivative. CHEBI:33281 means antimicrobial agent and is inherited
    from macrolide antibiotic CHEBI:25105, rather than directly attached to this term.
    Its broad role is preserved while ARO and direct experiments support ANTIBACTERIAL
    filing.
  snapshot_sha256: 38b7f1f43db9b28a0a7ef6a2477ae81b728352c12ad29ada96f7a5b326c4c02c
- evidence_id: aro
  kind: database
  reference: ARO:3007570; ARO:0000000; https://card.mcmaster.ca/ontology/46343
  locator: 054-card.html; read-only original downloads/aro.obo cache, hash recorded
    in 054-source-check.json
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: ARO:3007570 names mycaminosyltylonolide, links PubChem 6437420 and is_a
    ARO:0000000, the valid macrolide-antibiotic class. The all-zero local class ID
    is legitimate. Current CARD and cached ontology agree. Source ARO definition says
    polymyxin B, whereas its PMID:37208456 concerns polymyxin B nonapeptide; the native
    record adopts the chemical ChEBI definition, not that source activity wording.
  snapshot_sha256: e39f0561a3374cf022eb35f568ebfdfcbc825f987899641933ba4391a9fe23e3
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6437420/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  locator: 054-pubchem.json
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: The ARO-linked PubChem entity has the same stereospecific InChIKey and
    neutral C31H51NO10 structure as ChEBI, supporting the source merge.
  snapshot_sha256: 3ebbe73dca4edef3f94b2b085ebb391b51b8f9c0a036246c389e12c2769722c5
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/C12002
  locator: 054-kegg.html and 054-keggmol.html, plain text despite suffix
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: KEGG C12002 and its Molfile match exact stereochemistry, key, formula and
    charge. Pathway or reaction placement is not independent proof of a producing
    organism or microbial antimicrobial target.
  snapshot_sha256: c9d6e37b49edb5ab1ad49b9a2b8c53e77de2f084ef9fbddec6cdda037992eb03
- evidence_id: xref-limits
  kind: database
  reference: cas:61257-02-1; metacyc.compound:CPD-15944; reaxys:4730900
  locator: 054-fetch-results.json, CAS and BioCyc responses
  accessed_at: '2026-10-21T08:04:19Z'
  support: context_only
  summary: CAS returned a JavaScript application shell; MetaCyc returned an account-access
    page. Reaxys target was not independently resolved. Source strings reproduce,
    but direct exact-structure authority verification remains incomplete for these
    three xrefs.
  snapshot_sha256: 3866432012518b72ae98435f3f7a1d4452ca53e0c4b2b883991d83584fd94efa
- evidence_id: patent1
  kind: primary_source
  reference: https://patents.google.com/patent/US20060014707A1/en
  locator: 054-patent1.html; description of Figure 1 synthetic route; native literal
    resolver in 054-final-fetch-results.json
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: The normalized publication US20060014707A1, Sixteen-member macrolide antiinfective
    agents, explicitly identifies 5-O-mycaminosyltylonolide as starting material 1.
    The native/source token US2006014707 omits one leading zero from the seven-digit
    serial portion, and its declared Google-patent resolver returns 404. This document
    is relevant provenance, not an exact-identity equivalence or proof that every
    derivative activity belongs to OMT.
  snapshot_sha256: 22c60758bca6b690bc95f87c17e47f5a52320681436176e5b5d27cb511f4479c
- evidence_id: patent2
  kind: primary_source
  reference: https://patents.google.com/patent/US4537957A/en
  locator: 054-patent2.html; summary, OMT preparation examples and claims
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: US4537957 is directly relevant to OMT production by acid treatment of demycinosyltylosin.
    The described Streptomyces fermentation produces the precursor DMT; subsequent
    acid hydrolysis yields OMT. These passages do not by themselves justify a structured
    claim that the strain biosynthesizes OMT directly.
  snapshot_sha256: 0cfe044475dd29f85962248124c3fe3ba7b2958e46f9ab9b11c18c16a046dbb2
- evidence_id: patent3
  kind: primary_source
  reference: https://patents.google.com/patent/WO2013076169A1/en
  locator: 054-patent3.html; paragraph 0102, preparation of YT106
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: WO2013076169 explicitly prepares parent OMT YT106 from tylosin before further
    derivative synthesis. The document reference is correctly in document_xrefs; downstream
    derivative activities and claims remain separate.
  snapshot_sha256: 00b74f475a699ca0be05947b600f27764f4053a1a68b1a87a22865b763322598
- evidence_id: primary1983
  kind: primary_source
  reference: PMID:6662812
  locator: DOI:10.7164/antibiotics.36.1709; complete 054-primary1983.pdf, Methods
    and Table 1 compound 7; page1711 visually inspected
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: Exact parent OMT compound 7 competes with radiolabeled tetrahydroleucomycin
    A3 for E. coli ribosome binding, ID50 0.5 µM. Table 1 MICs are 1.6 µg/mL for B.
    subtilis PCI219 and S. aureus FDA209P, 0.1 for M. luteus PCI1001 and 25 for E.
    coli NIHJ. These are strain-specific values; ID50 is a competition endpoint, not
    Kd or MIC. Full broth/agar/inoculum/timing details are not supplied here and require
    the cited methods.
  snapshot_sha256: 896cc17bc6d09fa54ebf756aed74cdaa15c082213f3fa0b912b1456eb75f3c24
- evidence_id: primary2010
  kind: primary_source
  reference: PMID:20534348
  locator: DOI:10.1016/j.chembiol.2010.04.008; 054-primary2010.pdf Results, Figures
    4-6 and Experimental Procedures; page 510 visually inspected
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: OMT competes with erythromycin for empty D. radiodurans 70S ribosomes;
    text reports apparent Kd 3 nM. In a separate E. coli lysate translation system
    it inhibits firefly-luciferase synthesis, IC50 0.15 µM, but poorly inhibits GFP
    synthesis. This supports compound-specific translation effects with polypeptide
    dependence. Proposed drug displacement and modeled atomic contacts are mechanistic
    interpretations, not a new experimentally solved OMT structure.
  snapshot_sha256: cc11fac8b7695d82a8bc411ee5e137af3709abec7c98789169be2461dde7ac17
- evidence_id: primary2023
  kind: primary_source
  reference: PMID:37208456
  locator: DOI:10.1038/s41429-023-00628-9; abstract in 054-primarycore.json; publisher
    abstract/metadata and 054-supp2023.docx
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: The sole adopted PMID lead studies OMT with polymyxin B nonapeptide against
    MDR P. aeruginosa, following discovery in efflux-pump deletion strain YM64. Accessible
    supplement Table S1 contains comparator-antibiotic MICs for clinical strains,
    not OMT combination values. Main quantitative combination tables were inaccessible;
    no values or specific pump-substrate conclusion are inferred.
  snapshot_sha256: 604f6e576159792fc3a46ddfed2c8912683c23c497ddb26f5e393a1c1355e897
- evidence_id: primary2024combo
  kind: primary_source
  reference: DOI:10.1248/bpbreports.7.5_157
  locator: Full 054-primary2024combo.html, Methods and Tables 1-3
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: Exact synthesized OMT is tested alone and with colistin. For E. coli ATCC25922,
    Table 2 gives OMT alone >64 µg/mL and colistin MIC 0.5; OMT MIC is 2 with half-MIC
    colistin and 8 with quarter-MIC colistin. These are conditional combination values,
    not OMT-alone susceptibility. Potentiation varies by strain/species; proposed
    clinical benefit remains untested.
  snapshot_sha256: c638ed0f040bc02ffe0ed68a0fb0d2a3504145a1cca0da63f44b425f5b7c34db
- evidence_id: derivative-boundary
  kind: primary_source
  reference: PMID:24090034; PMID:16873579; PMID:39691534
  locator: Abstracts in 054-primarycore.json; selected accessible 2024 publisher/PMC
    narrative and tables
  accessed_at: '2026-10-21T08:04:19Z'
  support: context_only
  summary: 2013 amino-acid conjugates, 2006 oxime derivatives and 2024 C23 derivatives
    are distinct molecules. Parent controls may inform OMT when explicitly identified;
    enhanced derivative potency, resistance avoidance, c9 docking and toxicity cannot
    be transferred to the parent. No such derivative-based native claim is asserted.
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit/hashlib calculation
  locator: 054-chemistry.py and 054-chemistry.json
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: Native SMILES/InChI, PubChem and KEGG yield WGUJDBLMJBJUQU-VKRLOHBMSA-N,
    C31H51NO10, charge 0 and matching masses. Twelve centres are assigned, both alkene
    stereochemistries are E, and both source-concept identifiers reproduce.
  snapshot_sha256: 502997706b95c404286c4b25d91cee2443de556ec6485a92d30f782f2f94d1f5
- evidence_id: source-check
  kind: validation
  reference: Focused source/ontology assertion checks
  locator: 054-source-check.py and 054-source-check.json
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: All asserted source identity/term/class/inherited-role checks pass, including
    both ARO terms. Source xref/document-string matching is separate from exact target
    verification. Greek beta and ASCII beta naming differences were explicitly normalized.
  snapshot_sha256: bec68496e56fbe88aac8c56cae87763a10d462327ee41c2c15da882dae7c26d9
- evidence_id: retrieval
  kind: validation
  reference: Public source retrieval attempts
  locator: 054-more-fetch-initial.py preserves initial code; corrected 054-more-fetch.py,
    054-more-fetch-results.json and 054-final-fetch-results.json
  accessed_at: '2026-10-21T08:04:19Z'
  support: context_only
  summary: Initial helper exited 1 before requests because no direct has_role link
    existed. The corrected source workflow follows the parent role, retrieves source
    documents and passes. Primary2024 derivative XML returned 500; the literal native
    patent resolver returned 404 while normalized publication succeeded. These retrieval
    outcomes are not unexecuted checks.
  snapshot_sha256: bdcd28dc49503ea95f077ac752957aaa1e68293c5ba014ac7e51f0bd4394dd9d
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual isolated batch-006 executions; 054-strict.tsv
  accessed_at: '2026-10-21T08:04:19Z'
  support: supports
  summary: Both documented focused native validators exited 0; strict scanned one
    record with zero ERROR rows. Independent chemistry and current-source comparisons
    also exited 0.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local and bounded primary-source discovery
  locator: 054-local-hits.txt; maintained inputs and primary databases/publisher searches
  accessed_at: '2026-10-21T08:04:19Z'
  support: context_only
  summary: Exact OMT studies were distinguished from tylosin, protylonolide congeners,
    C20/C23 derivatives and potentiator combinations. No exhaustive literature or
    universal resistance claim is made.
  search_scope: prepare.py 54 used rg --no-ignore --hidden excluding only .git and
    .venv. Before source judgment, ownership/inspect input hashes were expanded for
    ARO tables and promotion decisions. Follow-up searched curation/conf and exact
    edge tables for CHEBI:77011, ARO:3007570, label and aliases. Current chemical
    authorities, all three document leads, the sole adopted PMID, original 1983 full
    PDF,2010 full PDF and2024 exact-parent combination paper were inspected; selected
    derivative abstracts provided scope context.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral stereodefined OMT
  outcome: supported
  summary: All four structural representations agree. This is monoglycosylated OMT,
    retaining its aldehyde and C23 hydroxyl; tylosin, protylonolide analogues, oxime
    and peptide derivatives remain separate.
  target_ids:
  - CHEBI:77011
  evidence_ids:
  - record
  - chebi
  - pubchem
  - kegg
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Structural parents, inherited role and ARO class
  outcome: supported
  summary: Four ChEBI parents fit; broad antimicrobial role is inherited. ARO:0000000
    is the correct macrolide class and the merged ARO entity matches PubChem. Direct
    experiments support antibacterial filing.
  target_ids:
  - CHEBI:77011
  evidence_ids:
  - ontology
  - aro
  - source-check
  - primary1983
- assessment_id: xrefs
  area: grounding
  topic: Exact identity and document references
  outcome: concern
  summary: PubChem/KEGG/CARD mappings support exact identity. Three other authority
    target checks remain incomplete. Patents are correctly placed as documents, but
    one literal publication token fails its resolver and has a supported normalized
    counterpart.
  target_ids:
  - CHEBI:77011
  evidence_ids:
  - pubchem
  - kegg
  - aro
  - xref-limits
  - patent1
  - patent2
  - patent3
- assessment_id: mechanism
  area: evidence
  topic: Ribosomal binding and conditional translation inhibition
  outcome: supported
  summary: Direct parent binding and translation measurements support a ribosomal
    mechanism. Preserve E. coli binding in 1983, D. radiodurans binding in 2010 and
    E. coli lysate translation separately; GFP and Fluc outcomes differ.
  target_ids:
  - CHEBI:77011
  evidence_ids:
  - primary1983
  - primary2010
- assessment_id: activity
  area: evidence
  topic: Individual-compound versus combination observations
  outcome: supported
  summary: Exact OMT has primary antibacterial activity. Colistin/PMBN combination
    MICs cannot become single-agent values, and partner efficacy differs by organism
    and strain.
  target_ids:
  - CHEBI:77011
  evidence_ids:
  - primary1983
  - primary2023
  - primary2024combo
- assessment_id: completeness
  area: completeness
  topic: Concrete primary annotation opportunity
  outcome: concern
  summary: The seed lacks experimentally supported exact-parent mechanism/activity
    annotations available from inspected primary sources. This is a specific useful
    enrichment, not an error inferred from optional empty slots.
  target_ids:
  - CHEBI:77011
  evidence_ids:
  - record
  - primary1983
  - primary2010
  - primary2024combo
- assessment_id: producer
  area: scope
  topic: Semisynthesis versus biological production
  outcome: not_applicable
  summary: No producer object is asserted. The patent fermentation of a precursor
    followed by acid hydrolysis does not itself prove direct biosynthesis of OMT;
    do not infer a producer from tylosin production.
  target_ids:
  - CHEBI:77011
  evidence_ids:
  - record
  - patent2
  - patent3
- assessment_id: resistance
  area: scope
  topic: Efflux and combination context
  outcome: unknown
  summary: No resistance mechanism is asserted and adopted ARO tables have no exact
    edge. Source abstracts support an efflux/permeability-sensitive context, but not
    an identified individual transporter-specific direct biochemical interaction with
    OMT.
  target_ids:
  - CHEBI:77011
  evidence_ids:
  - record
  - source-check
  - primary2023
  - primary2024combo
- assessment_id: optional
  area: representation
  topic: Clinical, graph and dataset scope
  outcome: not_applicable
  summary: No clinical, graph or dataset annotation is asserted. In vitro combinations
    and derivative toxicity experiments do not establish parent-compound clinical
    efficacy or safety.
  target_ids:
  - CHEBI:77011
  evidence_ids:
  - record
  - primary2024combo
  - derivative-boundary
- assessment_id: provenance
  area: ownership
  topic: Source merge and generated history
  outcome: supported
  summary: Both source-concept mints and merged exact identity reproduce. Four seed/reseed
    events are consistent. Correct document identifiers in maintained source handling
    and add primary annotations through the validated writer.
  target_ids:
  - CHEBI:77011
  evidence_ids:
  - record
  - inventory
  - ownership
  - chemistry
- assessment_id: schema-assessment
  area: schema
  topic: Focused schema and independent validation
  outcome: supported
  summary: Both native focused validators, independent chemistry and source assertions
    pass. The corrected inherited-role retrieval assumption and external link failures
    are preserved separately.
  target_ids:
  - CHEBI:77011
  evidence_ids:
  - validation
  - source-check
  - retrieval
findings:
- finding_id: F1
  issue_key: chebi-77011-primary-ribosome-translation-evidence-completeness
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Exact-parent ribosome and translation evidence can enrich the seed
  description: The record has no primary mechanism or activity annotation even though
    original exact-OMT binding, polypeptide-dependent translation and strain-level
    antibacterial observations are available. These support precise curation without
    transferring derivative or combination effects.
  target_ids:
  - CHEBI:77011
  field_paths:
  - evidence
  - molecular_targets
  - mode_of_action
  - mode_of_action_notes
  - activity_spectrum
  - discussions
  evidence_ids:
  - record
  - primary1983
  - primary2010
  - primary2024combo
  rule_id: 'review-checklist: Evidence standard, Mode of action, Molecular targets,
    Activity and Audit'
  native_severity: minor actionable evidence-completeness gap
  normalization_reason: A specific primary enrichment is verified; no false existing
    native mechanism or activity value is asserted. Missing optional fields alone
    is not a major error.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/5-o-mycaminosyltylonolide.yaml
    role: Curator-owned evidence, molecular_targets, mode_of_action, activity_spectrum
      and discussions through validated writer/history
- finding_id: F2
  issue_key: chebi-77011-patent-publication-number-normalization
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: One optional patent locator needs publication-number normalization
  description: Source-derived patent:US2006014707 produces 404 at its declared resolver.
    The corresponding zero-padded publication US20060014707A1 is accessible and explicitly
    uses OMT as a starting material. Retain the source token as provenance while supplying
    a validated resolvable document identifier.
  target_ids:
  - CHEBI:77011
  field_paths:
  - document_xrefs
  evidence_ids:
  - record
  - ownership
  - patent1
  - retrieval
  rule_id: 'review-checklist: Equivalence and Audit; exact document locator verification'
  native_severity: minor recoverable document-provenance locator gap
  normalization_reason: This is an optional document locator with a verified recoverable
    publication, not a broken primary evidence assertion, internal reference or compound
    identity. Its placement as document_xrefs is otherwise correct.
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
actions:
- action_id: A1
  description: Curate exact-parent ribosome/translation mechanism and strain-specific
    antibacterial evidence with assay and combination qualifiers.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:77011
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/5-o-mycaminosyltylonolide.yaml
    role: Curator-owned evidence, molecular_targets, mode_of_action, activity_spectrum
      and discussions through validated writer/history
  acceptance_checks:
  - Use original 1983 compound 7 only. ID50=0.5µM is radioligand competition with
    E. coli ribosomes, not a dissociation constant. Preserve exact MIC strains and
    µg/mL units and retrieve cited full antimicrobial methods before claiming missing
    assay details.
  - Use 2010 apparent Kd=3nM for D. radiodurans 70S binding separately from E. coli-lysate
    translation. Preserve Fluc IC50=0.15µM and poor GFP inhibition; do not describe
    universal inhibition of every translated polypeptide. Identify modeled contacts
    and displacement proposals as interpretation.
  - Ground the target at its supported ribosomal/RNA level rather than inventing a
    protein UniProt target. Do not transfer C23/C20 derivative binding contacts, resistance
    or safety claims to OMT.
  - Represent PMBN and colistin combination experiments separately from single-agent
    susceptibility. The adopted 2023 PMID uses polymyxin B nonapeptide, not polymyxin
    B; the accessible supplement contains comparator drugs only. Source ARO wording
    is not a native OMT-alone activity assertion.
  - Attach claim-level sources through validated writer/history and run schema/strict,
    full-corpus reference/history/term and QC gates before native REVIEWED.
- action_id: A2
  description: Normalize the source-derived patent publication locator to a verified
    resolvable document identifier, preserving the original source token and document
    scope.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:77011
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
  - Verify US20060014707A1 is the intended source publication, preserve provenance
    of US2006014707 and implement correction in maintained source extraction/normalization
    rather than only generated YAML.
  - Regenerate document_xrefs and verify the resulting declared resolver retrieves
    the inspected Sixteen-member macrolide antiinfective agents document. Keep patents
    out of exact chemical xrefs and do not import derivative claims as parent evidence.
  - Run the native validation and reproducibility gates and preserve validated history.
limitations:
- CAS returned an application shell, MetaCyc an account-access page and Reaxys exact
  target was not independently resolved. Current source string matching does not complete
  those authority target checks.
- The 2023 main paper remains abstract/metadata only; its accessible supplement reports
  comparator-antibiotic MICs, not the missing OMT combination table. All quantitative
  combination values cited here come from the independently inspected2024 full paper.
- The 1983 paper reports exact strains and MICs but refers out for assay methodology.
  No unreported medium, inoculum or incubation conditions are invented. Its competition
  ID50 and 2010 apparent Kd are different endpoints and species.
- The 2010 PDF text extractor renders micro units as m in places; the relevant page
  510 and 1983 Table 1 were visually checked. Values above use verified µM units.
  Polypeptide-dependent translation effects do not establish an exclusive atomic binding
  model.
- The initial supplementary fetch helper failed because it assumed a direct has_role
  link; the corrected inherited-role lookup succeeds. The original helper code is
  preserved. A local optional HTML parser dependency was unavailable; source text
  was successfully extracted using the Python standard library.
- The 2024 derivative-paper XML endpoint returned 500. Only accessible abstract/selected
  article text was used for derivative scope context, not quantitative parent mechanism
  claims.
- The failed literal patent resolver and normalized accessible publication are both
  retained. Their relevance was checked in document text, not inferred from automated
  chemical tags alone.
- This bounded review does not exhaust all literature or establish native REVIEWED
  status. Primary curation, document normalization, unresolved checks and required
  gates remain outstanding.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Only scratch review artifacts were written. No native record, maintained input,
  generated artifact or curation history was modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:77011
- https://card.mcmaster.ca/ontology/46343
- https://rest.kegg.jp/get/C12002
- https://pubchem.ncbi.nlm.nih.gov/compound/6437420
- https://doi.org/10.7164/antibiotics.36.1709
- https://doi.org/10.1016/j.chembiol.2010.04.008
- https://doi.org/10.1038/s41429-023-00628-9
- https://doi.org/10.1248/bpbreports.7.5_157
- https://patents.google.com/patent/US20060014707A1/en
- https://patents.google.com/patent/US4537957A/en
- https://patents.google.com/patent/WO2013076169A1/en
tags:
- record-review
- macrolide
- ribosome
- polypeptide-dependent-translation
- combination-scope
- document-provenance
```
