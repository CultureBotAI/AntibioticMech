# Ceftizoxime: coherent acid with penam-name and product-synonym defects

- Review: 20261021T122229Z-ceftizoxime
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:02:15Z
- Finished UTC: 2026-10-21T12:22:29Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Two minor inherited synonym defects: penam names the wrong ring framework, and CEFIZOX is typed as an exact molecular synonym although official labeling identifies a sodium-salt product. Native identifier, 6R,7R/Z acid structure, formula, masses and checked complete cross-references agree. The native PBP family edge remains a qualified CARD assertion requiring primary evidence. Original experiments support species-specific PBP interactions and target-alteration resistance, with sodium-salt or unresolved reagent preparation boundaries. No optional-field absence is a defect.

## Scope And Provenance

Whole-record review of exact ceftizoxime free-acid graph.

Selection: Queue 261 in isolated batch027; original captures preserved and actual ARO owner inventories appended.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:553473 | data/antibiotics/antibacterial/ceftizoxime.yaml | generated | ceftizoxime |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:553473 | Actual command exited 0; native schema/strict or supplemental complete molecular comparison passed. |
| Focused strict | passed | True | CHEBI:553473 | Actual command exited 0; native schema/strict or supplemental complete molecular comparison passed. |
| Focused chemistry | passed | False | CHEBI:553473 | Actual command exited 0; native schema/strict or supplemental complete molecular comparison passed. |
| Focused xref-comparison | passed | False | CHEBI:553473 | Actual command exited 0; native schema/strict or supplemental complete molecular comparison passed. |
| Authoritative full QC | failed | True | CHEBI:553473 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:553473 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:553473 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:553473 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:553473 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:553473 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:553473 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:553473 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:553473 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact native acid and source mints

identity: supported. Targets: CHEBI:553473.

Complete graph, 6R,7R/Z geometry, formula, masses, charge and both source mints agree; sodium/prodrug material remains separate.

### Scaffold-name and branded-product synonym conflicts

identity: concern. Targets: CHEBI:553473.

The didehydropenam exact synonym has a five-membered fused ring framework, inconsistent with the six-membered cephem graph. CEFIZOX is an official sodium-salt product name and needs brand/product semantics. Other full names and native identity remain sound.

### Cephalosporin parents and antibacterial roles

grounding: supported. Targets: CHEBI:553473.

Broader parents and inherited antimicrobial/antibacterial-drug roles are supported. Parenteral administration is supported by clinical original text, with formulation identity qualified.

### Exact versus typed drug/document mappings

grounding: supported. Targets: CHEBI:553473.

PubChem, CAS, ChEMBL and KEGG full identities agree. DrugCentral/DrugBank are drug context and Wikipedia documentary; direct DrugBank and proprietary Reaxys access limited.

### Qualified CARD target and primary target scope

evidence: supported. Targets: CHEBI:553473.

Family-level target edge is explicitly database-origin with primary evidence queued. Primary 2005 S. aureus PBP2 and 1981 Gram-negative PBP1/3 experiments support targeted enrichment without assigning one universal PBP number or fitted binding constant.

### Assay material and phenotype boundaries

evidence: supported. Targets: CHEBI:553473.

Primary antibacterial evidence is strain/protocol specific. 1981 sodium structure, 2005 unspecified powder and clinical IV product cannot silently establish exact free-acid solid dosing. No native quantitative activity claim exists to correct.

### Optional primary target-alteration enrichment

completeness: supported. Targets: CHEBI:553473.

P458L allelic-replacement evidence provides a bounded future S. aureus 27s/ZOX3 resistance annotation; native resistance slot is unpopulated and not defective for that reason.

### All adopted citation dispositions

evidence: supported. Targets: CHEBI:553473.

All eight adopted PMIDs inspected at declared depth; safety, conjugate/imaging, prodrug and review sources do not become original bacterial target evidence.

### Structured search context

scope: supported. Targets: CHEBI:553473.

Datasets and corrected covered E. coli query completed after network retry; zero module hits are not negative biological evidence.

### Producer, clinical status, graph, datasets and discussions

scope: not_applicable. Targets: CHEBI:553473.

No populated native assertions in these optional domains; clinical-administration evidence does not establish regulatory approval or a natural producer.

### Source-owned versus curator-owned claims

provenance: supported. Targets: CHEBI:553473.

Full ChEBI/ARO owner inputs and schema/guidance read; initial and expanded hashes unchanged. Five seed/reseed events and SEEDED status retained.

### Focused native and supplemental checks

schema: supported. Targets: CHEBI:553473.

All actual focused commands pass. Shared corpus-only gates are coordinator-owned and must be inserted before final save.

## Findings

### F1: One exact synonym uses penam instead of the cephalosporin ring framework

minor / open / confirmed; issue key: chebi-553473-ceftizoxime-penam-synonym.

synonyms[3] names a 2,3-didehydropenam-2-carboxylic acid. Official penam has beta-lactam fused to a five-membered sulfur ring; dehydrogenation cannot create the six-membered ring of native ceftizoxime. Native full graph and another exact systematic name agree on the 8-oxo-5-thia-1-azabicyclo[4.2.0]octane framework. Remove or replace the erroneous inherited name through maintained source ownership, preserving the correct graph.

### F2: CEFIZOX needs product-name semantics instead of exact molecular equivalence

minor / open / confirmed; issue key: chebi-553473-ceftizoxime-cefizox-synonym-type.

synonyms[5] types CEFIZOX as EXACT_SYNONYM of the unsalted acid. Official labeling identifies Cefizox as ceftizoxime sodium injection, with vial strength expressed in active-ceftizoxime equivalents. Retain the legitimate brand association with BRAND_NAME or another supported product-context representation and explicit sodium-preparation scope; do not replace the valid native acid graph.

## Recommended Actions And Acceptance Checks

### A1

Remove or source-correct the erroneous penam exact synonym.

- Preserve the native complete key and valid 6R,7R/Z systematic name; do not alter the graph to fit the incorrect synonym.
- Use an upstream correction or supported persistent source adjudication so reseeding reproduces the fix.
- Check exact names against ring framework and rerun schema/strict and applicable reference/history/corpus gates after separately authorized curation.

### A2

Optionally add primary target and target-alteration evidence with strain/material scope.

- Keep the CARD-owned family edge and its provenance distinct from added primary items.
- Use S. aureus 27s/ZOX3 PBP2/P458L evidence with native agar PAP and radiolabel competition endpoints; do not call 0.1 microgram/mL a fitted IC50 or Kd.
- Preserve paper-internal discrepancies before extracting numeric observations: Table 1 ZOX12 MIC 25 versus Results 12; minor parental/mecA/pbpD MIC differences across Results/Discussion; nucleotide 1373 versus Table 1 pMC1 label 1337.
- Retain 1981 sodium/antiisomer and AS-924/liposomal/radiolabel boundaries.
- Resolve exact subject/taxon/protein mapping and claim-level references rather than deriving experimental identities from module membership.

### A3

Retain CEFIZOX as a qualified product/brand association rather than an exact molecular synonym.

- Use supported BRAND_NAME or other appropriate product-context semantics and preserve the sodium-salt preparation relationship.
- Keep CHEBI:553473 and the valid free-acid structure and exact cross-references unchanged.
- Implement the type correction through maintained source ownership so it survives reseeding, then run native schema/strict and relevant reference/history/corpus checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/ceftizoxime.yaml; Entire YAML | supports | Read identifier/class/status/grounding, definition, ten synonyms, two parents/two roles, full structure and mass fields, all exact/drug/document xrefs, both source concepts, qualified CARD target and five history events. |
| owners | data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv;data/raw/aro_target_edges.tsv; ChEBI row 2976; ARO molecule row 304; target row 240 | supports | ChEBI owns exact synonym and chemical graph plus seven PMID leads. ARO supplies the family target edge and review PMID 6326062. No matched resistance row was found in the ignored-inclusive owner search. Initial hashes retained. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity, equivalence, source-owned fields and target evidence | supports | Exact synonyms must agree with molecular structure; source-owned corrections need a reproducible input path. Optional mode/activity/resistance additions are not mandatory schema defects. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:553473; Current complete structure, definition and Names | partial | Current ChEBI reproduces the native full structure and the erroneous didehydropenam synonym. Other full systematic names correctly specify the 8-oxo-5-thia[4.2.0]octane cephem framework. Additional current ontology annotations do not compel optional expansion. |
| penam | https://www.ebi.ac.uk/chebi/CHEBI:35991; Definition, structural graph and systematic synonym | supports | Official penam scaffold has beta-lactam fused to a five-membered sulfur-containing ring, 4-thia-1-azabicyclo[3.2.0]heptan-7-one. Dehydrogenation does not expand it to the six-membered ring of native ceftizoxime. |
| chemistry | RDKit2026.03.5 native molecular checks; 261-chemistry.json | supports | SMILES and InChI both reproduce NNULBSISHYWZJU-LLKWHZGFSA-N, C13H13N5O5S2, charge 0, one fragment, matching average/exact masses and R, R centres. Both ARO/ChEBI source mints agree. |
| xref-comparison | Independent complete chemical mappings; 261-external-chemistry.json | supports | Both KEGG molfiles, ChEMBL SMILES, native PubChem CID and CAS-resolved PubChem SMILES independently reproduce the complete native key and formula. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6533629/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON; CID 6533629 complete structure and systematic name | supports | Complete key, 6R,7R/Z specification and free-acid formula agree. |
| cas | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/68401-81-0/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON; CAS 68401-81-0 lookup | supports | CAS resolves the exact acid CID 6533629 and full key, rather than sodium salt. This is PubChem CAS resolution, not independent proprietary CAS Registry access. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL528.json; CHEMBL528 molecule structures | supports | Full key and explicit isomeric structure agree. |
| kegg | https://rest.kegg.jp/get/C06890; C06890 and D07658 full records/molfiles | supports | C06890 and D07658 identify ceftizoxime acid, with matching formula and full independently generated key. D07658 separates sodium drug product D00923 from the native acid. |
| parents | CHEBI:23066;CHEBI:33281;CHEBI:36047;ARO:0000032; Current OLS terms and CARD class page; 261-chebi23066/33281/36047.json | supports | Cephalosporin parents are broader than exact acid; antimicrobial-agent and antibacterial-drug roles are compatible with original experimental and clinical sources. Current terms resolve. |
| aro | https://card.mcmaster.ca/aro/3004007; Current chemical identity, classification and publications | supports | Current CARD gives ceftizoxime, same isomeric structure/CID/ChEBI and broad PBP mechanism prose; PMID 6326062 is a review, not the original binding experiment. |
| aro-target | https://card.mcmaster.ca/aro/3000749; Target term definition and native target edge | supports | Term denotes beta-lactam-sensitive PBP family. Native context explicitly discloses unspecified organism/assay and PRIMARY_EVIDENCE_NEEDED; its direct-target relation is an attributed database assertion, not a claimed native quantitative experiment. |
| drugcentral | https://drugcentral.org/drugcard/563; Drug identity and external references | supports | DrugCentral563 is ceftizoxime with acid and sodium-related names/references aggregated. DB01332 crosswalk is corroborated here and byKEGG, but direct DrugBank access returned 403. Drug-level mappings are not all exact salt equivalents. |
| wiki | https://en.wikipedia.org/wiki/Ceftizoxime; Native documentary reference | context_only | The named document resolves and concerns ceftizoxime. It does not substitute for primary scientific support. |
| adapter | kg-microbe-sources imodulondb; 261-adapter-results.json; actual datasets and E. coli/precise1k query | context_only | Adapter was attempted before open protein research. Sandbox DNS failed; permitted retry listed datasets. A mistyped precise1 query is retained but not interpreted; corrected covered e_coli/precise1k query for penicillin-binding protein returned zero hits. No absence or mechanistic inference is made from module-search results. |
| adopted-11452157 | PMID:11452157; DOI 10.1046/j.1537-2995.2001.41070893.x; complete abstract | context_only | Ceftizox-induced immune hemolysis case plus retrospective drug-dependent antibody work. Supports adverse immunological context, not bacterial target binding or native free-acid formulation identity. |
| adopted-11711261 | PMID:11711261; DOI 10.1016/S0924-8579(01)00444-7; complete abstract | context_only | Original AS-924 bifunctional-prodrug animal absorption and simulated PK activity study distinguishes ceftizoxime from its POM/L-alanyl prodrug. Active-ceftizoxime activity is discussed, but full exact-reagent/MIC methods were not inspected; do not make AS-924 a synonym or infer direct prodrug binding. |
| adopted-1384868 | PMID:1384868; DOI 10.1159/000236216; complete abstract | context_only | Aztreonam monoclonal antibody/HSA-conjugate cross-reaction study. Ceftizoxime is not singled out in the inspected abstract. Adopted association is retained as unresolved relevance at this depth, not used to support antimicrobial mechanism. |
| adopted-22726927 | PMID:22726927; DOI 10.1016/j.bmcl.2012.05.105; complete abstract | context_only | Technetium-99m-labeled ceftizoxime in long-circulating pH-sensitive liposomes is studied for osteomyelitis imaging in rats. Radiolabeled liposomal biodistribution is not native free-acid antibacterial potency or PBP binding. |
| adopted-29017833 | PMID:29017833; DOI 10.1016/j.jaip.2017.08.027; complete abstract | context_only | Review of beta-lactam allergy and side-chain cross-reactivity. Secondary safety context; not independent original ceftizoxime antimicrobial mechanism evidence. |
| adopted-6326062 | PMID:6326062; DOI 10.1002/j.1875-9114.1984.tb03313.x; complete abstract | context_only | Adopted ARO review of ceftizoxime pharmacology/activity/clinical use. Historical beta-lactamase stability and broad-spectrum prose is contextual and cannot erase strain-specific resistance or replace original PBP experiments. |
| adopted-15716453 | PMID:15716453; DOI 10.1128/JB.187.5.1815-1824.2005; full Methods/Results/Discussion, Table1, Figures 2-3 | partial | USP ceftizoxime powder is used; salt/hydration is not specified. S. aureus 27s/ZOX3 membrane competition uses 80 micrograms of protein, drug 0.1-20 microgram/mL, 30°C for 10 min, then radiolabeled benzylpenicillin 10 microgram/mL for 10 min. PBP2 inhibition shifts from 0.1 microgram/mL in 27s to 1-2 microgram/mL in ZOX3; this is a competition pattern, not a newly fitted Kd/IC50. Reciprocal allelic replacement and site-directed P458L pbpB mutation reproduce resistance/reduced affinity. Population analysis on agar at 37°C for 48 h reports main parental 0.8 and ZOX3 6 microgram/mL. Figures 2-3 visually inspected; source has additional numeric inconsistencies, so no full AST object is copied. |
| adopted-23394621 | PMID:23394621; DOI 10.1186/1756-0500-6-57; full original text and Tables 1-3 | partial | Open randomized 180-woman timing study compares 1 g IV ceftizoxime before incision versus after cord clamping. Both arms receive drug; there is no untreated/other-antibiotic control and authors explicitly state inadequate power for equivalence/superiority. Product salt is unspecified. The text/table contain 8 (6.7%) among 90 and reversed timing prose; retain as administration context without transferring those disputed rates. |
| primary1981 | PMID:7018389; DOI 10.1128/AAC.19.3.393; all four original scanned pages, Fig. 1, Tables 1-3 | partial | Fig. 1 explicitly depicts ceftizoxime as COONa and anti FR14060 as COOH. Fujisawa material; agar dilution on heart infusion agar, 10^6 cells/mL suspension, 37°C for 20 h. Table 1 syn ceftizoxime MIC 0.025 microgram/mL for E. coli NIHJ JC-2 and 0.1 for E. cloacae 58-5. Membrane [14C]penicillin G competition Table 3 gives censored I50 &lt;3.2 microgram/mL for E. coli PBP1a/1bs/3 and &lt;1 for E. cloacae corresponding PBPs; anti-isomer PBP1bs is 35 and 13 respectively. These sodium-preparation endpoints are not asserted as exact unsalted-solid measurements. |
| primary1981-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8342/181443/6ac215772f3d/aac00003-0030.png; Original p394, Fig. 1 and Table 1 | supports | Visual inspection establishes the sodium depiction, antiisomer distinction, MIC units and table-specific inoculum. The manifest 261-primary-fetch-results.json preserves all four original scan hashes. |
| primary1980 | https://www.jstage.jst.go.jp/article/chemotherapy1953/28/Supplement5/28_Supplement5_44/_pdf; Original methods pp44-45 and English summary p49 | partial | Additional Japanese primary study uses Fujisawa ceftizoxime, E. coli NIHJ JC-2 and V. cholerae E2 membrane preparations and radiolabel competition. Summary reports PBP1a/1b/3 affinities and strong 1b binding; not evidence that S. aureus uses the same numbered primary target. Only these sections were assessed and no figure-derived numerical endpoint is copied. |
| gates | Actual focused commands; 261-focused-results.json | supports | Schema, strict and supplemental molecular checks each exit 0; external structural comparison also exit 0. Native validation alone does not detect the wrong-ring synonym. |
| local-search | Ignored-inclusive local/source review; 261-owner-hits.txt;261-local-hits.txt | context_only | Exact name, identifier, key and ARO identifier searched including hidden/ignored files outside .git/.venv. Findings are scoped to this exact record; native omitted optional domains are not alleged absent from all literature. |
| cefizox-label | https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0013824b-6aee-4da4-affd-35bc6bf19d91; Official DailyMed label effective 2006-06-08; Description and Ingredients and Appearance | supports | Cefizox is ceftizoxime sodium for injection, formula C13H12N5NaO5S2 and molecular weight 405.38. ADD-vantage vials contain sodium salt expressed as 1-g or 2-g ceftizoxime equivalents. This establishes a branded-product/active-moiety relationship, not exact identity with the native C13H13N5O5S2 acid. The historical label is used for product identity without asserting present marketing status. |

## Limits And Additional Notes

- Six adopted leads were evaluated at abstract depth; two adopted papers had full text, and additional 1981 scans were fully read. Exact reagent salt/hydration remains unresolved for the 2005 USP powder and 2013 IV product.
- DrugBank direct page returned 403; crosswalk was corroborated by other databases. Proprietary Reaxys content was not independently inspected.
- EPMC XML for PMC1064008 returned 500; alternate PMC full HTML and original figure images succeeded. GoldBook direct requests returned 403; authoritative ChEBI penam scaffold text/structure was inspected instead.
- Source-internal numeric inconsistencies in 2005 resistance and 2013 trial tables are disclosed; no disputed numeric data is promoted into native claims.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 23 expanded input hashes unchanged; original capture preserved. No native/source/status/history changes.
- Native checks used batch 027 environment; standalone RDKit 2026.03.5 used existing batch 019 interpreter against batch 027 cwd.
- Only free public sources were used. Optional links and tags were checked against ceftizoxime; the unrelated queue-258 phrase in an unsaved evidence summary was removed before finalization.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T122229Z-ceftizoxime
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Ceftizoxime: coherent acid with penam-name and product-synonym defects'
started_at: '2026-10-21T12:02:15Z'
finished_at: '2026-10-21T12:22:29Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent complete native and actual ChEBI/ARO owner review;
    all eight adopted PMID leads; current full chemical comparisons; original 2005
    PBP2/allelic-replacement full text and figures, all four 1981 original scan pages,
    1980 methods/English summary and 2013 clinical full text.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Two minor inherited synonym defects: penam names the wrong ring framework,
  and CEFIZOX is typed as an exact molecular synonym although official labeling identifies
  a sodium-salt product. Native identifier, 6R,7R/Z acid structure, formula, masses
  and checked complete cross-references agree. The native PBP family edge remains
  a qualified CARD assertion requiring primary evidence. Original experiments support
  species-specific PBP interactions and target-alteration resistance, with sodium-salt
  or unresolved reagent preparation boundaries. No optional-field absence is a defect.'
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
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
  - path: data/antibiotics/antibacterial/ceftizoxime.yaml
    sha256: 00b83dde491918e2ad2c41c57d69f08a271328208b46c2bc9a4b9c9177b4ac77
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
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
- target_id: CHEBI:553473
  path: data/antibiotics/antibacterial/ceftizoxime.yaml
  label: ceftizoxime
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
    role: Adopted CARD identity, bibliography, classification and crosswalks
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted CARD target edge
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Bounded resistance-owner check
scope:
  description: Whole-record review of exact ceftizoxime free-acid graph.
  selection: Queue 261 in isolated batch027; original captures preserved and actual
    ARO owner inventories appended.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:553473
  exclusions:
  - target: Ceftizoxime sodium, anti oxime FR14060, AS-924 prodrug and radiolabeled/liposomal
      material as exact native identities
    reason: Related forms and preparations retain their own material and experiment
      scope.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual command exited 0; native schema/strict or supplemental complete
    molecular comparison passed.
  target_ids:
  - CHEBI:553473
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/ceftizoxime.yaml (cwd /private/tmp/antibioticmech-record-reviews-027)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual command exited 0; native schema/strict or supplemental complete
    molecular comparison passed.
  target_ids:
  - CHEBI:553473
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/ceftizoxime.yaml --out /private/tmp/am-review-session/261-validation.tsv
    (cwd /private/tmp/antibioticmech-record-reviews-027)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Focused chemistry
  status: passed
  required: false
  summary: Actual command exited 0; native schema/strict or supplemental complete
    molecular comparison passed.
  target_ids:
  - CHEBI:553473
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/check199200.py
    261 (cwd /private/tmp/antibioticmech-record-reviews-027)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: xref-comparison
  name: Focused xref-comparison
  status: passed
  required: false
  summary: Actual command exited 0; native schema/strict or supplemental complete
    molecular comparison passed.
  target_ids:
  - CHEBI:553473
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/compare-261.py
    (cwd /private/tmp/antibioticmech-record-reviews-027)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - xref-comparison
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:553473
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
  - CHEBI:553473
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
  - CHEBI:553473
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
  - CHEBI:553473
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
  - CHEBI:553473
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
  - CHEBI:553473
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
  - CHEBI:553473
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
  - CHEBI:553473
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
  - CHEBI:553473
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/ceftizoxime.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T12:08:41Z'
  support: supports
  summary: Read identifier/class/status/grounding, definition, ten synonyms, two parents/two
    roles, full structure and mass fields, all exact/drug/document xrefs, both source
    concepts, qualified CARD target and five history events.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv;data/raw/aro_target_edges.tsv
  locator: ChEBI row 2976; ARO molecule row 304; target row 240
  accessed_at: '2026-10-21T12:08:41Z'
  support: supports
  summary: ChEBI owns exact synonym and chemical graph plus seven PMID leads. ARO
    supplies the family target edge and review PMID 6326062. No matched resistance
    row was found in the ignored-inclusive owner search. Initial hashes retained.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity, equivalence, source-owned fields and target evidence
  accessed_at: '2026-10-21T12:08:41Z'
  support: supports
  summary: Exact synonyms must agree with molecular structure; source-owned corrections
    need a reproducible input path. Optional mode/activity/resistance additions are
    not mandatory schema defects.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:553473
  locator: Current complete structure, definition and Names
  accessed_at: '2026-10-21T12:05:01.274700Z'
  support: partial
  summary: Current ChEBI reproduces the native full structure and the erroneous didehydropenam
    synonym. Other full systematic names correctly specify the 8-oxo-5-thia[4.2.0]octane
    cephem framework. Additional current ontology annotations do not compel optional
    expansion.
  snapshot_sha256: d57ca9eb0d1c9dd79aa4279b76ae1a3c6250cf5b6e8dcda68fa03920af45c92f
- evidence_id: penam
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:35991
  locator: Definition, structural graph and systematic synonym
  accessed_at: '2026-10-21T12:06:35.057837Z'
  support: supports
  summary: Official penam scaffold has beta-lactam fused to a five-membered sulfur-containing
    ring, 4-thia-1-azabicyclo[3.2.0]heptan-7-one. Dehydrogenation does not expand
    it to the six-membered ring of native ceftizoxime.
  snapshot_sha256: bcca57d41662e4315ded468f4aceb466753a167c46e023503045999bb5893d06
- evidence_id: chemistry
  kind: validation
  reference: RDKit2026.03.5 native molecular checks
  locator: 261-chemistry.json
  accessed_at: '2026-10-21T12:04:41Z'
  support: supports
  summary: SMILES and InChI both reproduce NNULBSISHYWZJU-LLKWHZGFSA-N, C13H13N5O5S2,
    charge 0, one fragment, matching average/exact masses and R, R centres. Both ARO/ChEBI
    source mints agree.
  snapshot_sha256: 528e7823ef3248d4697977a3f8562f569fbe70d87d2b68a246d26a4a813eb6bc
- evidence_id: xref-comparison
  kind: validation
  reference: Independent complete chemical mappings
  locator: 261-external-chemistry.json
  accessed_at: '2026-10-21T12:06:31Z'
  support: supports
  summary: Both KEGG molfiles, ChEMBL SMILES, native PubChem CID and CAS-resolved
    PubChem SMILES independently reproduce the complete native key and formula.
  snapshot_sha256: 7118d6773dccfa45f4968c7d5bb77e72cd15cf5649dcf657ad1984a8b50f2dcb
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6533629/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON
  locator: CID 6533629 complete structure and systematic name
  accessed_at: '2026-10-21T12:05:01.275131Z'
  support: supports
  summary: Complete key, 6R,7R/Z specification and free-acid formula agree.
  snapshot_sha256: 947564dbac3c642d4680093c31b7b1844b8d490f30eb51abc593917a7d380b79
- evidence_id: cas
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/68401-81-0/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON
  locator: CAS 68401-81-0 lookup
  accessed_at: '2026-10-21T12:05:01.275251Z'
  support: supports
  summary: CAS resolves the exact acid CID 6533629 and full key, rather than sodium
    salt. This is PubChem CAS resolution, not independent proprietary CAS Registry
    access.
  snapshot_sha256: 947564dbac3c642d4680093c31b7b1844b8d490f30eb51abc593917a7d380b79
- evidence_id: chembl
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL528.json
  locator: CHEMBL528 molecule structures
  accessed_at: '2026-10-21T12:05:01.275327Z'
  support: supports
  summary: Full key and explicit isomeric structure agree.
  snapshot_sha256: dce6eb25b8380e78765d027b1ff401b78d11f204d38968e84fc32bea4e441749
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/C06890
  locator: C06890 and D07658 full records/molfiles
  accessed_at: '2026-10-21T12:05:02.037779Z'
  support: supports
  summary: C06890 and D07658 identify ceftizoxime acid, with matching formula and
    full independently generated key. D07658 separates sodium drug product D00923
    from the native acid.
  snapshot_sha256: 5e54766da09a95f2f22e8bbb72f0afcf34a77ea58c7c6069a0d525ae8ac52ce4
- evidence_id: parents
  kind: authority
  reference: CHEBI:23066;CHEBI:33281;CHEBI:36047;ARO:0000032
  locator: Current OLS terms and CARD class page; 261-chebi23066/33281/36047.json
  accessed_at: '2026-10-21T12:05:02.903097Z'
  support: supports
  summary: Cephalosporin parents are broader than exact acid; antimicrobial-agent
    and antibacterial-drug roles are compatible with original experimental and clinical
    sources. Current terms resolve.
  snapshot_sha256: ac2ebd34062bbb7883ee33d035e4a82578a3ee0ac7750480c7f3c232c1f3b073
- evidence_id: aro
  kind: authority
  reference: https://card.mcmaster.ca/aro/3004007
  locator: Current chemical identity, classification and publications
  accessed_at: '2026-10-21T12:05:02.650511Z'
  support: supports
  summary: Current CARD gives ceftizoxime, same isomeric structure/CID/ChEBI and broad
    PBP mechanism prose; PMID 6326062 is a review, not the original binding experiment.
  snapshot_sha256: 7c2543d19cc71d5904d6a246af198a8cd00d1748b02ae767bf45e08e13ff932a
- evidence_id: aro-target
  kind: authority
  reference: https://card.mcmaster.ca/aro/3000749
  locator: Target term definition and native target edge
  accessed_at: '2026-10-21T12:05:02.676236Z'
  support: supports
  summary: Term denotes beta-lactam-sensitive PBP family. Native context explicitly
    discloses unspecified organism/assay and PRIMARY_EVIDENCE_NEEDED; its direct-target
    relation is an attributed database assertion, not a claimed native quantitative
    experiment.
  snapshot_sha256: 047aecb4ebcfa32e6629b90485001859692f03afb142d88a8d5d176b2c77c081
- evidence_id: drugcentral
  kind: database
  reference: https://drugcentral.org/drugcard/563
  locator: Drug identity and external references
  accessed_at: '2026-10-21T12:05:02.052429Z'
  support: supports
  summary: DrugCentral563 is ceftizoxime with acid and sodium-related names/references
    aggregated. DB01332 crosswalk is corroborated here and byKEGG, but direct DrugBank
    access returned 403. Drug-level mappings are not all exact salt equivalents.
  snapshot_sha256: f2b395ab3e38272c2fc7ac063d60d40ae747b445f2294eb3dd131d2022311c19
- evidence_id: wiki
  kind: database
  reference: https://en.wikipedia.org/wiki/Ceftizoxime
  locator: Native documentary reference
  accessed_at: '2026-10-21T12:05:02.614397Z'
  support: context_only
  summary: The named document resolves and concerns ceftizoxime. It does not substitute
    for primary scientific support.
  snapshot_sha256: ea94a524f563a515f4c313e8a5638802c78ef5fb8b7e85da496b12ffe963c9a7
- evidence_id: adapter
  kind: search
  reference: kg-microbe-sources imodulondb
  locator: 261-adapter-results.json; actual datasets and E. coli/precise1k query
  accessed_at: '2026-10-21T12:04:45Z'
  support: context_only
  summary: Adapter was attempted before open protein research. Sandbox DNS failed;
    permitted retry listed datasets. A mistyped precise1 query is retained but not
    interpreted; corrected covered e_coli/precise1k query for penicillin-binding protein
    returned zero hits. No absence or mechanistic inference is made from module-search
    results.
  snapshot_sha256: dd93a36e624ed3f6953d24652eb394f8f2d86d90e59d3a4404a76322e02f1d71
  search_scope: 2026-10-21; isolated batch 027; rg --no-ignore --hidden outside .git/.venv;
    structured adapter then official databases, all eight adopted abstracts, selected
    public original full texts and scans.
- evidence_id: adopted-11452157
  kind: primary_source
  reference: PMID:11452157
  locator: DOI 10.1046/j.1537-2995.2001.41070893.x; complete abstract
  accessed_at: '2026-10-21T12:05:04.029632Z'
  support: context_only
  summary: Ceftizox-induced immune hemolysis case plus retrospective drug-dependent
    antibody work. Supports adverse immunological context, not bacterial target binding
    or native free-acid formulation identity.
  snapshot_sha256: 6155830a27484ee68e2cbb1a3b24f410331ad8e3a0ba68796c976ae3cff48524
- evidence_id: adopted-11711261
  kind: primary_source
  reference: PMID:11711261
  locator: DOI 10.1016/S0924-8579(01)00444-7; complete abstract
  accessed_at: '2026-10-21T12:05:04.029632Z'
  support: context_only
  summary: Original AS-924 bifunctional-prodrug animal absorption and simulated PK
    activity study distinguishes ceftizoxime from its POM/L-alanyl prodrug. Active-ceftizoxime
    activity is discussed, but full exact-reagent/MIC methods were not inspected;
    do not make AS-924 a synonym or infer direct prodrug binding.
  snapshot_sha256: 6155830a27484ee68e2cbb1a3b24f410331ad8e3a0ba68796c976ae3cff48524
- evidence_id: adopted-1384868
  kind: primary_source
  reference: PMID:1384868
  locator: DOI 10.1159/000236216; complete abstract
  accessed_at: '2026-10-21T12:05:04.029632Z'
  support: context_only
  summary: Aztreonam monoclonal antibody/HSA-conjugate cross-reaction study. Ceftizoxime
    is not singled out in the inspected abstract. Adopted association is retained
    as unresolved relevance at this depth, not used to support antimicrobial mechanism.
  snapshot_sha256: 6155830a27484ee68e2cbb1a3b24f410331ad8e3a0ba68796c976ae3cff48524
- evidence_id: adopted-22726927
  kind: primary_source
  reference: PMID:22726927
  locator: DOI 10.1016/j.bmcl.2012.05.105; complete abstract
  accessed_at: '2026-10-21T12:05:04.029632Z'
  support: context_only
  summary: Technetium-99m-labeled ceftizoxime in long-circulating pH-sensitive liposomes
    is studied for osteomyelitis imaging in rats. Radiolabeled liposomal biodistribution
    is not native free-acid antibacterial potency or PBP binding.
  snapshot_sha256: 6155830a27484ee68e2cbb1a3b24f410331ad8e3a0ba68796c976ae3cff48524
- evidence_id: adopted-29017833
  kind: primary_source
  reference: PMID:29017833
  locator: DOI 10.1016/j.jaip.2017.08.027; complete abstract
  accessed_at: '2026-10-21T12:05:04.029632Z'
  support: context_only
  summary: Review of beta-lactam allergy and side-chain cross-reactivity. Secondary
    safety context; not independent original ceftizoxime antimicrobial mechanism evidence.
  snapshot_sha256: 6155830a27484ee68e2cbb1a3b24f410331ad8e3a0ba68796c976ae3cff48524
- evidence_id: adopted-6326062
  kind: primary_source
  reference: PMID:6326062
  locator: DOI 10.1002/j.1875-9114.1984.tb03313.x; complete abstract
  accessed_at: '2026-10-21T12:05:04.029632Z'
  support: context_only
  summary: Adopted ARO review of ceftizoxime pharmacology/activity/clinical use. Historical
    beta-lactamase stability and broad-spectrum prose is contextual and cannot erase
    strain-specific resistance or replace original PBP experiments.
  snapshot_sha256: 6155830a27484ee68e2cbb1a3b24f410331ad8e3a0ba68796c976ae3cff48524
- evidence_id: adopted-15716453
  kind: primary_source
  reference: PMID:15716453
  locator: DOI 10.1128/JB.187.5.1815-1824.2005; full Methods/Results/Discussion, Table1,
    Figures 2-3
  accessed_at: '2026-10-21T12:06:00.103089Z'
  support: partial
  summary: USP ceftizoxime powder is used; salt/hydration is not specified. S. aureus
    27s/ZOX3 membrane competition uses 80 micrograms of protein, drug 0.1-20 microgram/mL,
    30°C for 10 min, then radiolabeled benzylpenicillin 10 microgram/mL for 10 min.
    PBP2 inhibition shifts from 0.1 microgram/mL in 27s to 1-2 microgram/mL in ZOX3;
    this is a competition pattern, not a newly fitted Kd/IC50. Reciprocal allelic
    replacement and site-directed P458L pbpB mutation reproduce resistance/reduced
    affinity. Population analysis on agar at 37°C for 48 h reports main parental 0.8
    and ZOX3 6 microgram/mL. Figures 2-3 visually inspected; source has additional
    numeric inconsistencies, so no full AST object is copied.
  snapshot_sha256: 1a0be4a48e487b6de05dbc392c3cf679f416e8b426303f60c9468cdeebdc65d6
- evidence_id: adopted-23394621
  kind: primary_source
  reference: PMID:23394621
  locator: DOI 10.1186/1756-0500-6-57; full original text and Tables 1-3
  accessed_at: '2026-10-21T12:05:21.236193Z'
  support: partial
  summary: Open randomized 180-woman timing study compares 1 g IV ceftizoxime before
    incision versus after cord clamping. Both arms receive drug; there is no untreated/other-antibiotic
    control and authors explicitly state inadequate power for equivalence/superiority.
    Product salt is unspecified. The text/table contain 8 (6.7%) among 90 and reversed
    timing prose; retain as administration context without transferring those disputed
    rates.
  snapshot_sha256: 691a230ea309d24803e7ea4183f8834e8e24eef02221dbc826829d75a25f3f25
- evidence_id: primary1981
  kind: primary_source
  reference: PMID:7018389
  locator: DOI 10.1128/AAC.19.3.393; all four original scanned pages, Fig. 1, Tables
    1-3
  accessed_at: '2026-10-21T12:05:21.236326Z'
  support: partial
  summary: Fig. 1 explicitly depicts ceftizoxime as COONa and anti FR14060 as COOH.
    Fujisawa material; agar dilution on heart infusion agar, 10^6 cells/mL suspension,
    37°C for 20 h. Table 1 syn ceftizoxime MIC 0.025 microgram/mL for E. coli NIHJ
    JC-2 and 0.1 for E. cloacae 58-5. Membrane [14C]penicillin G competition Table
    3 gives censored I50 <3.2 microgram/mL for E. coli PBP1a/1bs/3 and <1 for E. cloacae
    corresponding PBPs; anti-isomer PBP1bs is 35 and 13 respectively. These sodium-preparation
    endpoints are not asserted as exact unsalted-solid measurements.
  snapshot_sha256: 1fb96c70c9c3dbc6754577edef860d39a7a6d17ab25d26598a161d8bfade4b7c
- evidence_id: primary1981-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8342/181443/6ac215772f3d/aac00003-0030.png
  locator: Original p394, Fig. 1 and Table 1
  accessed_at: '2026-10-21T12:05:59.767155Z'
  support: supports
  summary: Visual inspection establishes the sodium depiction, antiisomer distinction,
    MIC units and table-specific inoculum. The manifest 261-primary-fetch-results.json
    preserves all four original scan hashes.
  snapshot_sha256: 02db8f5c40621f7fd90aa71e4168c68e748c9340c72b19d727ccfff82370c395
- evidence_id: primary1980
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/chemotherapy1953/28/Supplement5/28_Supplement5_44/_pdf
  locator: Original methods pp44-45 and English summary p49
  accessed_at: '2026-10-21T12:05:21.236396Z'
  support: partial
  summary: Additional Japanese primary study uses Fujisawa ceftizoxime, E. coli NIHJ
    JC-2 and V. cholerae E2 membrane preparations and radiolabel competition. Summary
    reports PBP1a/1b/3 affinities and strong 1b binding; not evidence that S. aureus
    uses the same numbered primary target. Only these sections were assessed and no
    figure-derived numerical endpoint is copied.
  snapshot_sha256: 1cc5ef6ee3fa10387622474fd21bae72ee01d687607763e27562d551ea5c9a74
- evidence_id: gates
  kind: validation
  reference: Actual focused commands
  locator: 261-focused-results.json
  accessed_at: '2026-10-21T12:04:41Z'
  support: supports
  summary: Schema, strict and supplemental molecular checks each exit 0; external
    structural comparison also exit 0. Native validation alone does not detect the
    wrong-ring synonym.
  snapshot_sha256: 9e4753ff1dd027e306e992820d1f0011b67430740b800c7ee724cf28f816c185
- evidence_id: local-search
  kind: search
  reference: Ignored-inclusive local/source review
  locator: 261-owner-hits.txt;261-local-hits.txt
  accessed_at: '2026-10-21T12:03:56Z'
  support: context_only
  summary: Exact name, identifier, key and ARO identifier searched including hidden/ignored
    files outside .git/.venv. Findings are scoped to this exact record; native omitted
    optional domains are not alleged absent from all literature.
  snapshot_sha256: 965f3ddc87bb37b5e71d3ef146d713991340eed74c2e0811041f0904df84105c
  search_scope: 2026-10-21; isolated batch 027; rg --no-ignore --hidden outside .git/.venv;
    structured adapter then official databases, all eight adopted abstracts, selected
    public original full texts and scans.
- evidence_id: cefizox-label
  kind: authority
  reference: https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0013824b-6aee-4da4-affd-35bc6bf19d91
  locator: Official DailyMed label effective 2006-06-08; Description and Ingredients
    and Appearance
  accessed_at: '2026-10-21T12:20:29.942865Z'
  support: supports
  summary: Cefizox is ceftizoxime sodium for injection, formula C13H12N5NaO5S2 and
    molecular weight 405.38. ADD-vantage vials contain sodium salt expressed as 1-g
    or 2-g ceftizoxime equivalents. This establishes a branded-product/active-moiety
    relationship, not exact identity with the native C13H13N5O5S2 acid. The historical
    label is used for product identity without asserting present marketing status.
  snapshot_sha256: 70b2303f890f01a50476a9ee63f14ed0635ed19630b4d2da23bebf81e9dc4e32
assessments:
- assessment_id: identity
  area: identity
  topic: Exact native acid and source mints
  outcome: supported
  summary: Complete graph, 6R,7R/Z geometry, formula, masses, charge and both source
    mints agree; sodium/prodrug material remains separate.
  target_ids:
  - CHEBI:553473
  evidence_ids:
  - native
  - chemistry
  - xref-comparison
  - pubchem
- assessment_id: synonyms
  area: identity
  topic: Scaffold-name and branded-product synonym conflicts
  outcome: concern
  summary: The didehydropenam exact synonym has a five-membered fused ring framework,
    inconsistent with the six-membered cephem graph. CEFIZOX is an official sodium-salt
    product name and needs brand/product semantics. Other full names and native identity
    remain sound.
  target_ids:
  - CHEBI:553473
  evidence_ids:
  - native
  - chebi
  - penam
  - pubchem
  - cefizox-label
- assessment_id: classification
  area: grounding
  topic: Cephalosporin parents and antibacterial roles
  outcome: supported
  summary: Broader parents and inherited antimicrobial/antibacterial-drug roles are
    supported. Parenteral administration is supported by clinical original text, with
    formulation identity qualified.
  target_ids:
  - CHEBI:553473
  evidence_ids:
  - parents
  - aro
  - adopted-23394621
  - primary1981
- assessment_id: xrefs
  area: grounding
  topic: Exact versus typed drug/document mappings
  outcome: supported
  summary: PubChem, CAS, ChEMBL and KEGG full identities agree. DrugCentral/DrugBank
    are drug context and Wikipedia documentary; direct DrugBank and proprietary Reaxys
    access limited.
  target_ids:
  - CHEBI:553473
  evidence_ids:
  - xref-comparison
  - drugcentral
  - wiki
- assessment_id: target
  area: evidence
  topic: Qualified CARD target and primary target scope
  outcome: supported
  summary: Family-level target edge is explicitly database-origin with primary evidence
    queued. Primary 2005 S. aureus PBP2 and 1981 Gram-negative PBP1/3 experiments
    support targeted enrichment without assigning one universal PBP number or fitted
    binding constant.
  target_ids:
  - CHEBI:553473
  evidence_ids:
  - aro-target
  - owners
  - adopted-15716453
  - primary1981
- assessment_id: activity
  area: evidence
  topic: Assay material and phenotype boundaries
  outcome: supported
  summary: Primary antibacterial evidence is strain/protocol specific. 1981 sodium
    structure, 2005 unspecified powder and clinical IV product cannot silently establish
    exact free-acid solid dosing. No native quantitative activity claim exists to
    correct.
  target_ids:
  - CHEBI:553473
  evidence_ids:
  - primary1981
  - adopted-15716453
  - adopted-23394621
- assessment_id: resistance
  area: completeness
  topic: Optional primary target-alteration enrichment
  outcome: supported
  summary: P458L allelic-replacement evidence provides a bounded future S. aureus
    27s/ZOX3 resistance annotation; native resistance slot is unpopulated and not
    defective for that reason.
  target_ids:
  - CHEBI:553473
  evidence_ids:
  - native
  - adopted-15716453
- assessment_id: leads
  area: evidence
  topic: All adopted citation dispositions
  outcome: supported
  summary: All eight adopted PMIDs inspected at declared depth; safety, conjugate/imaging,
    prodrug and review sources do not become original bacterial target evidence.
  target_ids:
  - CHEBI:553473
  evidence_ids:
  - adopted-11452157
  - adopted-11711261
  - adopted-1384868
  - adopted-22726927
  - adopted-29017833
  - adopted-6326062
  - adopted-15716453
  - adopted-23394621
- assessment_id: adapter
  area: scope
  topic: Structured search context
  outcome: supported
  summary: Datasets and corrected covered E. coli query completed after network retry;
    zero module hits are not negative biological evidence.
  target_ids:
  - CHEBI:553473
  evidence_ids:
  - adapter
- assessment_id: optional
  area: scope
  topic: Producer, clinical status, graph, datasets and discussions
  outcome: not_applicable
  summary: No populated native assertions in these optional domains; clinical-administration
    evidence does not establish regulatory approval or a natural producer.
  target_ids:
  - CHEBI:553473
  evidence_ids:
  - native
- assessment_id: provenance
  area: provenance
  topic: Source-owned versus curator-owned claims
  outcome: supported
  summary: Full ChEBI/ARO owner inputs and schema/guidance read; initial and expanded
    hashes unchanged. Five seed/reseed events and SEEDED status retained.
  target_ids:
  - CHEBI:553473
  evidence_ids:
  - native
  - owners
  - rubric
- assessment_id: validation
  area: schema
  topic: Focused native and supplemental checks
  outcome: supported
  summary: All actual focused commands pass. Shared corpus-only gates are coordinator-owned
    and must be inserted before final save.
  target_ids:
  - CHEBI:553473
  evidence_ids:
  - gates
  - chemistry
  - xref-comparison
findings:
- finding_id: F1
  issue_key: chebi-553473-ceftizoxime-penam-synonym
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: One exact synonym uses penam instead of the cephalosporin ring framework
  description: synonyms[3] names a 2,3-didehydropenam-2-carboxylic acid. Official
    penam has beta-lactam fused to a five-membered sulfur ring; dehydrogenation cannot
    create the six-membered ring of native ceftizoxime. Native full graph and another
    exact systematic name agree on the 8-oxo-5-thia-1-azabicyclo[4.2.0]octane framework.
    Remove or replace the erroneous inherited name through maintained source ownership,
    preserving the correct graph.
  target_ids:
  - CHEBI:553473
  field_paths:
  - synonyms[3].synonym_text
  evidence_ids:
  - native
  - owners
  - chebi
  - penam
  - pubchem
  - chemistry
  rule_id: native-review-checklist:Identity and Equivalence
  native_severity: minor bounded redundant synonym error
  normalization_reason: Only one redundant exact-name string is wrong; primary identifier,
    graph, definition, class and other systematic name remain correct. No wrong-native-structure
    blocker is inferred.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned exact synonym
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source-owned names
- finding_id: F2
  issue_key: chebi-553473-ceftizoxime-cefizox-synonym-type
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: CEFIZOX needs product-name semantics instead of exact molecular equivalence
  description: synonyms[5] types CEFIZOX as EXACT_SYNONYM of the unsalted acid. Official
    labeling identifies Cefizox as ceftizoxime sodium injection, with vial strength
    expressed in active-ceftizoxime equivalents. Retain the legitimate brand association
    with BRAND_NAME or another supported product-context representation and explicit
    sodium-preparation scope; do not replace the valid native acid graph.
  target_ids:
  - CHEBI:553473
  field_paths:
  - synonyms[5].synonym_type
  evidence_ids:
  - native
  - owners
  - chebi
  - cefizox-label
  - chemistry
  rule_id: native-review-checklist:Identity and Equivalence
  native_severity: minor bounded trade-name typing error
  normalization_reason: The brand association with ceftizoxime is valid, but its exact
    molecular synonym type omits the sodium product boundary. This bounded metadata
    error does not invalidate the coherent native acid graph or assert a separate
    covalent prodrug as identical.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned CEFIZOX exact-synonym annotation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source-owned names
actions:
- action_id: A1
  description: Remove or source-correct the erroneous penam exact synonym.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:553473
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned exact synonym
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source-owned names
  acceptance_checks:
  - Preserve the native complete key and valid 6R,7R/Z systematic name; do not alter
    the graph to fit the incorrect synonym.
  - Use an upstream correction or supported persistent source adjudication so reseeding
    reproduces the fix.
  - Check exact names against ring framework and rerun schema/strict and applicable
    reference/history/corpus gates after separately authorized curation.
- action_id: A2
  description: Optionally add primary target and target-alteration evidence with strain/material
    scope.
  finding_ids: []
  target_ids:
  - CHEBI:553473
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/ceftizoxime.yaml
    role: Curator-owned molecular_targets, activity_spectrum and resistance_mechanisms
      via validated writer
  acceptance_checks:
  - Keep the CARD-owned family edge and its provenance distinct from added primary
    items.
  - Use S. aureus 27s/ZOX3 PBP2/P458L evidence with native agar PAP and radiolabel
    competition endpoints; do not call 0.1 microgram/mL a fitted IC50 or Kd.
  - 'Preserve paper-internal discrepancies before extracting numeric observations:
    Table 1 ZOX12 MIC 25 versus Results 12; minor parental/mecA/pbpD MIC differences
    across Results/Discussion; nucleotide 1373 versus Table 1 pMC1 label 1337.'
  - Retain 1981 sodium/antiisomer and AS-924/liposomal/radiolabel boundaries.
  - Resolve exact subject/taxon/protein mapping and claim-level references rather
    than deriving experimental identities from module membership.
- action_id: A3
  description: Retain CEFIZOX as a qualified product/brand association rather than
    an exact molecular synonym.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:553473
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned CEFIZOX exact-synonym annotation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source-owned names
  acceptance_checks:
  - Use supported BRAND_NAME or other appropriate product-context semantics and preserve
    the sodium-salt preparation relationship.
  - Keep CHEBI:553473 and the valid free-acid structure and exact cross-references
    unchanged.
  - Implement the type correction through maintained source ownership so it survives
    reseeding, then run native schema/strict and relevant reference/history/corpus
    checks after separately authorized curation.
limitations:
- Six adopted leads were evaluated at abstract depth; two adopted papers had full
  text, and additional 1981 scans were fully read. Exact reagent salt/hydration remains
  unresolved for the 2005 USP powder and 2013 IV product.
- DrugBank direct page returned 403; crosswalk was corroborated by other databases.
  Proprietary Reaxys content was not independently inspected.
- EPMC XML for PMC1064008 returned 500; alternate PMC full HTML and original figure
  images succeeded. GoldBook direct requests returned 403; authoritative ChEBI penam
  scaffold text/structure was inspected instead.
- Source-internal numeric inconsistencies in 2005 resistance and 2013 trial tables
  are disclosed; no disputed numeric data is promoted into native claims.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 23 expanded input hashes unchanged; original capture preserved. No native/source/status/history
  changes.
- Native checks used batch 027 environment; standalone RDKit 2026.03.5 used existing
  batch 019 interpreter against batch 027 cwd.
- Only free public sources were used. Optional links and tags were checked against
  ceftizoxime; the unrelated queue-258 phrase in an unsaved evidence summary was removed
  before finalization.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:553473
- https://pmc.ncbi.nlm.nih.gov/articles/PMC1064008/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC181443/
- https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0013824b-6aee-4da4-affd-35bc6bf19d91
tags:
- ceftizoxime
- exact-synonym
- primary-target
- assay-material-scope
- brand-salt-boundary
```
