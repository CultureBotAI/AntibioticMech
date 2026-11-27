# Cinoxacin: supported identity and antibacterial activity; incorporate formal US approval withdrawals

- Review: 20261021T131713Z-cinoxacin
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T13:04:53Z
- Finished UTC: 2026-10-21T13:17:13Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact neutral cinoxacin structure, source identities, antibacterial role and historical US approvals are supported. One major finding concerns the current APPROVED summary despite formal withdrawal of every cited US application. One informational follow-up preserves the difference between a database assertion of GyrA binding, a GyrB sensitivity relation and direct cinoxacin subunit-binding evidence. Original whole-cell and assembled-gyrase experiments support bounded activity and functional inhibition, without upgrading the native primary-evidence-needed annotations.

## Scope And Provenance

Entire native record: definition, eight typed synonyms, four parents, role, structure, eight chemical xrefs, three drug xrefs, four document xrefs, two source concepts, two database-derived targets, four FDA assertions and seven history events; all seven adopted literature leads.

Selection: Queue 301, exact CHEBI:3716. Initial thirteen input hashes retained and five actual ARO/target/FDA input owners appended before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3716 | data/antibiotics/antibacterial/cinoxacin.yaml | generated | cinoxacin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:3716 | No schema issues. |
| strict | passed | True | CHEBI:3716 | One file, zero errors. |
| chemistry | passed | False | CHEBI:3716 | Native SMILES/InChI, formula, zero charge, achirality, masses and both source-ID mints agree. |
| external-chemistry | passed | False | CHEBI:3716 | Eight independently parsed encodings from PubChem, ChEMBL, DrugCentral, KEGG and FDA GSRS reproduce the full native key. |
| Authoritative full QC | failed | True | CHEBI:3716 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3716 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3716 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3716 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3716 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3716 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3716 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3716 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3716 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact free acid, names, structure and xrefs

identity: supported. Targets: CHEBI:3716.

The native identity is internally coherent and independently corroborated by multiple official chemical graphs. Restricted registry entries remain explicitly unverified; patent document links concern related disclosures and are not all exact chemical equivalences.

### Parent and antibacterial scope

scope: supported. Targets: CHEBI:3716.

Chemical parents fit; ARO family nomenclature is interpreted using the actual broader quinolone source class. Original cinoxacin assays and historical clinical trial support the antibacterial drug role with assay/material limits.

### Historical approvals versus current regulatory state

evidence: concern. Targets: CHEBI:3716.

All four FDA assertions accurately retain original approval events and discontinued marketing, but the regulatory-status summary omits formal withdrawal of all three cited US applications. Schema clinical_status denotes regulatory/use status, and WITHDRAWN is available. Historical approval dates must remain intact.

### GyrA/GyrB assertion depths and functional evidence

evidence: unknown. Targets: CHEBI:3716.

The primary-evidence-needed database status is honest. ARO directly asserts GyrA binding; its GyrB description and map rationale establish sensitivity rather than an inspected physical binding experiment. Assembled-gyrase inhibition neither proves nor refutes direct binding to each subunit. A bounded mapping review is appropriate without claiming confirmed nonbinding.

### Optional exact primary activity and mechanism enrichment

completeness: unknown. Targets: CHEBI:3716.

The original experiments could support qualified functional target/activity observations. Their absence from a SEEDED record is not independently a required-field defect. Biotransformation, host effects and secondary mechanism reviews do not justify producer or causal-graph additions. All seven adopted leads have explicit dispositions at the stated read depth.

## Findings

### F1: Represent formal withdrawal of the cited US approvals

major / open / confirmed; issue key: cinoxacin-formally-withdrawn-us-approvals.

clinical_status APPROVED and the unqualified product status APPROVED summarize four historical AP events, although original FDA notices withdrew NDA018067 effective 2007-12-07 and ANDA073005/073006 effective 2016-11-03. Discontinued marketing and currently_marketed false are accurately preserved, but are distinct from formal withdrawal of approval. The schema defines a regulatory/use status and provides WITHDRAWN. Incorporate the later US events and qualify the current summary while preserving all historical approval dates and product provenance. Do not infer worldwide withdrawal or a safety reason.

### F2: Resolve the GyrB sensitivity-to-direct-binding mapping at its stated evidence depth

informational / open / provisional; issue key: cinoxacin-gyrb-sensitivity-direct-binding-uncertainty.

The GyrB source entry and local mapping rationale describe a fluoroquinolone-sensitive subunit, while the native target relation is DIRECT_BINDING_TARGET. The native DATABASE and PRIMARY_EVIDENCE_NEEDED qualification already makes the primary-evidence gap visible. The inspected exact cinoxacin experiment measures assembled-gyrase supercoiling inhibition, not isolated GyrB binding; this neither proves nor refutes physical binding. Review whether the maintained source relation justifies the direct-binding type, or needs a weaker relation/context. Keep GyrA separate because its upstream entry explicitly asserts binding.

## Recommended Actions And Acceptance Checks

### A1

Reconcile formal US withdrawal events with product-level history and aggregate status through the maintained FDA pipeline.

- Retain original approval dates, identifiers, sponsors and strengths for all four assertions; cite original Federal Register notices and effective withdrawal dates.
- Represent current withdrawn US application status without equating all discontinued products with withdrawn approvals and without inventing a safety cause or worldwide status.
- Document the 2024 secondary FDA table date conflict while using the original 2007 notice as the operative evidence. Reseed and rerun focused validators plus applicable source-reproduction gates.

### A2

Review the GyrB relation mapping without upgrading or negating binding beyond inspected evidence.

- Distinguish an upstream explicit binding assertion from sensitivity/complex membership and from direct compound-specific physical evidence. Preserve DATABASE and PRIMARY_EVIDENCE_NEEDED unless appropriate original evidence is inspected.
- If the relation remains DIRECT_BINDING_TARGET, explain its source-semantic basis; otherwise choose the schema relation justified by the source. Do not extrapolate the conclusion to GyrA or all quinolones.

### A3

If enriching the exact record, curate original functional and antibacterial observations with full assay context.

- For PMID3010848 distinguish MIC greater than 1000 micrograms/mL from partial-supercoiling-inhibition Ip 312 micrograms/mL and preserve M. luteus MB1784/ATCC4698, material, medium and reaction conditions. Ip is not IC50 or Kd.
- For PMID1137390 retain medium and inoculum dependence and population distributions, without inventing single-strain measurements or exact salt identity. Do not transfer fungal transformation or human MHC effects as bacterial mechanism or biosynthesis.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cinoxacin.yaml; Complete YAML. | supports | SEEDED/EXACT/ANTIBACTERIAL. Neutral achiral C12H10N2O5, full key VDUWPHTZYNWKRN-UHFFFAOYSA-N. Two database target assertions explicitly require primary evidence. No quantitative activity, causal graph, biosynthetic producer or resistance determinant is asserted. Four product assertions preserve historical approvals and separately state Discontinued and currently_marketed false; aggregate clinical_status is APPROVED. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv; data/raw/fda_clinical_status.tsv; conf/aro_target_roles.tsv; conf/sources.yaml; data/raw/MANIFEST.yaml; scripts/extract_source_inventory.py; scripts/extract_fda_clinical_status.py; scripts/seed_from_sources.py; Complete ChEBI row 115, ARO row 307, target rows 243–244, FDA rows 3060–3063; source configuration/manifest and relevant extraction/assembly logic. | supports | ChEBI owns definition, identity, chemical parents and role; ARO supplies its concept, family, aliases and target edges; FDA owns four exact-substance product rows. Target mapping explicitly calls GyrB a sensitive subunit while emitting DIRECT_BINDING_TARGET. FDA extraction selects original AP approvals and preserves marketing status; seeding turns eligible product rows into APPROVED assertions and the aggregate APPROVED summary without adjudicating later formal withdrawal. All native data faithfully reproduce these maintained inputs. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:3716; https://pubchem.ncbi.nlm.nih.gov/compound/2762; https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1208; https://www.genome.jp/entry/D00872; https://drugcentral.org/drugcard/657; https://api.fda.gov/other/substance.json?search=unii:LMK22VUH23; Full official identity entries and independently parsed chemical representations. | supports | ChEBI, PubChem 2762, ChEMBL1208, DrugCentral 657, KEGG D00872 and FDA GSRS UNII LMK22VUH23 version 21 agree on the native full graph and formula. Public entries cross-attest CAS 28657-80-9. All eight native aliases are source-attested; KEGG independently uses CIN as an abbreviation. Cinobac is retained in product context, not misrepresented as a different molecule. |
| vsdb | https://bioregistry.io/vsdb:1881; Source-provided resolver to the University of Hertfordshire Veterinary Substances Database, full exact entry. | supports | VSDB 1881 gives the same CAS, SMILES, InChI and full key; independent parsing of both encodings matches the native graph. The initially guessed cheminfo URL was unrelated and is not used as evidence. |
| xref-limits | https://www.hmdb.ca/metabolites/HMDB0014965; https://go.drugbank.com/drugs/DB00827; https://bioregistry.io/lincs.smallmolecule:LSM-6552; beilstein:1084304; Official source xref attribution and attempted independent public access. | unknown | HMDB and DrugBank direct retrieval returned 403; LINCS source resolver failed certificate validation and an earlier guessed route returned 500. These identifiers remain ChEBI-attested but their independent exact graphs were not inspected. Beilstein was not accessed through paid services. No identity contradiction is inferred from access failure. |
| parents-role | https://www.ebi.ac.uk/chebi/CHEBI:25754; https://www.ebi.ac.uk/chebi/CHEBI:38104; https://www.ebi.ac.uk/chebi/CHEBI:38770; https://www.ebi.ac.uk/chebi/CHEBI:36047; https://card.mcmaster.ca/aro/0000001; Official ChEBI parent/role entries and ARO:0000001 class definition/aliases/membership. | supports | Oxocarboxylic acid, oxacycle and cinnoline parents fit the graph. The antibacterial-drug role is supported by original assays and historical clinical use. ARO:0000001 is named fluoroquinolone antibiotic but also has the quinolone alias and includes nonfluorinated quinolones such as cinoxacin and nalidixic acid; the source-qualified family label is not independent evidence that the graph contains fluorine. |
| documents | https://patents.google.com/patent/US3669965A/en; https://patents.google.com/patent/DE2005104A1/en; https://patents.google.com/patent/US6441167B1/en; Original patent text, relevant compound claims, material descriptions and examples. | context_only | US3669965 claim 2 names the exact 1-ethyl methylenedioxy oxocinnoline carboxylic acid; DE2005104 is the corresponding compound-family disclosure. Acid and salts are distinguished, so sodium-salt experimental claims are not automatically exact neutral-material measurements. US6441167 concerns cinoxacin lanthanide chelates and uses cinoxacin as a precursor; the document is relevant but chelate properties do not transfer. Wikipedia is a topic link, not primary evidence. |
| fda-products | https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:CINOXACIN&amp;limit=100; https://api.fda.gov/other/substance.json?search=unii:LMK22VUH23; Complete current Drugs@FDA and GSRS responses. | supports | NDA018067 products 001/002, ANDA073005 product 001 and ANDA073006 product 001 match the native ingredient, sponsors, strengths, original approval dates, AP submission status and discontinued marketing. GSRS structure is exact cinoxacin. These accurate historical AP events do not themselves establish continuing application approval after a formal withdrawal. |
| withdrawal-2007 | https://www.govinfo.gov/content/pkg/FR-2007-11-07/pdf/E7-21886.pdf; Original FDA Federal Register notice, Table row NDA18-067 and operative withdrawal paragraph, pages 62858–62863. | refutes | The notice explicitly withdraws NDA18-067 for Cinobac cinoxacin capsules 250 and 500 mg, Eli Lilly, effective 2007-12-07. Holders reported products no longer marketed and requested withdrawal. This is formal application withdrawal, not an inference from marketing discontinuation and not a finding of safety-related withdrawal. |
| withdrawal-2016 | https://www.govinfo.gov/content/pkg/FR-2016-10-04/pdf/2016-23893.pdf; Original FDA Federal Register notice, Table 1 rows ANDA073005/073006 and effective/operative paragraphs. | refutes | FDA withdraws Teva cinoxacin 250 mg ANDA073005 and 500 mg ANDA073006 effective 2016-11-03. The products were no longer marketed and applicants requested withdrawal, without prejudice to refiling. Together with the 2007 notice, every application supporting the native current APPROVED summary has a documented formal US withdrawal. |
| fda-context | https://www.accessdata.fda.gov/drugsatfda_docs/nda/2024/217927Orig1s000NameR.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2002/18067slr029ltr.pdf; 2024 proprietary-name review table and complete 2002 supplement letter. | context_only | The 2002 letter supports historical approved use and product context. A later 2024 FDA name-review table lists an inconsistent 2005-04-04 Federal Register withdrawal date for NDA018067; the directly inspected 2007 original legal notice supplies the operative date used here. Preserve this source discrepancy rather than silently equating the two dates. |
| adapter | iModulonDB adapter: e_coli/precise1k/b2231; e_coli/precise1k/b3699; Datasets discovery followed by gyrA and gyrB searches before open web research. | context_only | Structured lookup resolves E. coli gyrA/b2231 and gyrB/b3699 with no matching iModulon memberships. The native assertions have no specified organism, so these are representative function/context keys only. They are neither exact cinoxacin binding evidence nor negative evidence from absent modules. |
| aro-targets | ARO:3004010; ARO:3000733; ARO:3003261; https://card.mcmaster.ca/ontology; Complete current compound and two target entries plus maintained relation map. | supports | The GyrA entry explicitly asserts fluoroquinolone binding to the alpha subunit, citing general reviews PMID1657531 and PMID9293187. The GyrB entry describes a fluoroquinolone-sensitive beta subunit without an exact cinoxacin binding assay; conf/aro_target_roles.tsv uses sensitivity as its mapping rationale. Both native edges are DATABASE-backed and PRIMARY_EVIDENCE_NEEDED. The difference in source assertion depth warrants a bounded follow-up, not a conclusion that GyrB cannot bind cinoxacin. |
| gyrase-primary | PMID:3010848; DOI:10.1128/AAC.29.4.598; https://pmc.ncbi.nlm.nih.gov/articles/PMC180449/; Full original pages 598–601 visually read, especially Methods and Table 1; page 600 full scan is 301-page600-full.png. | supports | Lilly cinoxacin was tested against Micrococcus luteus MB1784/ATCC4698 and purified assembled gyrase from that strain. The same drug lot gave MIC greater than 1000 micrograms/mL and Ip 312 micrograms/mL. Ip is the lowest concentration producing partial inhibition of supercoiling, not IC50 or a binding constant. Broth MIC used 10^4 organisms/mL, tryptic soy broth, 37 degrees C and 24 hours. The functional reaction used A/B enzyme in a 1:1 ratio, relaxed phiX174 DNA, ATP and a 30-minute 37-degree-C incubation. It did not measure physical cinoxacin binding to an isolated subunit; the uptake comparisons involved other named quinolones. |
| activity-primary | PMID:1137390; DOI:10.1128/AAC.7.3.370; https://pmc.ncbi.nlm.nih.gov/articles/PMC429140/; Full original pages 370–373 visually read, all Methods/Results/Discussion and cumulative curves. | supports | Lilly compound 64716, cinoxacin, was assayed against 150 Enterobacteriaceae isolates plus 30 P. aeruginosa isolates. Agar/broth, nutrient/Mueller-Hinton medium and 10^6 versus 10^8 organisms/mL changed measured activity. The paper supports antibacterial activity but not a condition-free spectrum or a single strain MIC. The plots are cumulative isolate distributions; no exact strain identifiers are provided. Material counterion is not explicitly identified, so any future precise material claim must retain that limit. |
| activity-comparison | PMID:12717; DOI:10.1128/AAC.10.6.918; https://pubmed.ncbi.nlm.nih.gov/12717/; Complete original indexed abstract inspected. | supports | The original study of 138 Shigella isolates reports similar cinoxacin/nalidixic-acid activity, with greater oxolinic-acid potency by weight; pH and protein binding affect comparison. It supports the qualitative related-antibacterial-action definition without claiming equal potency or condition-independent activity. |
| gyrase-other-primary | PMID:2847648; DOI:10.1128/AAC.32.8.1192; Complete original indexed abstract. | context_only | Partially purified S. aureus FDA209P gyrase was studied; cinoxacin and nalidixic acid had 50% inhibitory doses of at least 100 micrograms/mL. This is assembled-enzyme functional inhibition at abstract depth, not direct physical subunit binding or an exact material-form certificate. |
| gyrase-reviews | PMID:1657531; PMID:9293187; Complete indexed abstracts and publication types of the two reviews cited by ARO GyrA. | context_only | These are secondary reviews of gyrase structure/function and quinolone-topoisomerase mechanisms. General enzyme-DNA complex trapping, DNA-break and resistance mechanisms are context, not independently inspected exact cinoxacin binding or causal experiments. |
| adopted-clinical | PMID:7017171; DOI:10.1016/S0022-5347(17)55219-2; Complete original indexed abstract; read scope and any full-text limit stated explicitly. | context_only | The ARO-adopted single-blind UTI trial randomized 50 patients to cinoxacin or nalidixic acid and found comparable eradication/clinical response. It supports former clinical use but does not establish the ARO compound-page mechanism of direct gyrase inhibition, double-strand breaks and death. |
| adopted-gyrase | PMID:3005575; DOI:10.1021/jm00153a015; Complete original indexed abstract; read scope and any full-text limit stated explicitly. | context_only | This original sixty-compound quinolone SAR abstract correlates gyrase inhibition and antibacterial activity, but does not provide an exact cinoxacin row. The ACS full-text route returned 403; no uninspected table or subunit binding result is claimed. |
| adopted-transformation | PMID:12204384; DOI:10.1111/j.1574-6968.2002.tb11336.x; Complete original indexed abstract; read scope and any full-text limit stated explicitly. | context_only | Beauveria bassiana ATCC7159 transforms added cinoxacin into reduced metabolites over twenty days. This is biotransformation of dosed substrate, not evidence that the fungus biosynthesizes cinoxacin. |
| adopted-chlorella | PMID:16295658; DOI:10.1007/BF02931567; Complete original indexed abstract; read scope and any full-text limit stated explicitly. | context_only | The study concerns endosymbiotic Chlorella in green hydra and damage to chloroplasts/mitochondria; it does not establish a bacterial molecular target. |
| adopted-host | PMID:29438107; DOI:10.1172/JCI97739; Complete original indexed abstract; read scope and any full-text limit stated explicitly. | context_only | The abstract concerns methyldopa inhibition of human HLA-DQ8 in autoimmune diabetes. A bounded exact-cinoxacin search of the accessible main text found no match; supplementary compound screening was not inspected. No human immune-target assertion transfers to this antibacterial record. |
| adopted-adverse | PMID:3147004; DOI:10.1136/bmj.297.6661.1434; Complete original indexed abstract; read scope and any full-text limit stated explicitly. | context_only | The original abstract reports cinoxacin-associated anaphylaxis cases. It supplies adverse-effect context, not antibacterial mechanism and not proof that the later regulatory withdrawals were safety-driven. |
| adopted-unavailable | PMID:6226270; https://pubmed.ncbi.nlm.nih.gov/6226270/; Indexed metadata and publisher resolution of its externally attached DOI. | unknown | Hatch 1983, AUAA Journal 3(3):10–11, Cinoxacin for urinary tract infection, has no indexed abstract. Europe PMC attaches DOI10.1007/BF03288285, but that DOI resolves to a different 1976 Inpharma newsletter item. The native source cites the PMID only, so this is a retrieval metadata conflict, not a demonstrated native erroneous DOI. No full original Hatch text was inspected. |
| inclusive-search | 301-inclusive-hits.txt; Exact identifier, label, key and ARO identifier across local maintained and generated content, including hidden and ignored files. | context_only | Matches comprise native/source rows, queue/PATHS and generated embeddings. No exact curator decision or maintained evidence overlay was found in the bounded searched scope. This is not a claim that additional public literature cannot exist. |
| validation | 301-schema.log; 301-strict.log; 301-chemistry.json; 301-xref-chemistry.json; 301-vsdb-chemistry.json; Actual focused checks and independent chemistry diagnostics. | supports | Schema and strict checks pass. Native and official external structures match. Both source identifiers reproduce their minted values. All eighteen captured input hashes, including the original thirteen, remain unchanged. |

## Limits And Additional Notes

- Independent HMDB, DrugBank and LINCS exact-entry access was unavailable; Beilstein was not accessed through paid services. The identifiers remain source-attested, while multiple other official structures independently confirm native identity.
- All seven adopted leads were resolved and dispositioned. Six were read as complete original indexed abstracts; PMID6226270 has no indexed abstract and its externally supplied DOI resolves to a different publication. Its original text was not inspected. The ACS full paper for PMID3005575 was inaccessible.
- Two additional original studies were read completely as page scans: PMID1137390 and PMID3010848. PMID2847648 and PMID12717 were read at original-abstract depth. Secondary gyrase reviews were not treated as exact primary evidence.
- Exact material counterion and direct subunit binding are not established by the inspected cinoxacin antibacterial/gyrase papers. Functional inhibition is not a measured physical-binding constant or a complete causal chain to bacterial death.
- Regulatory conclusions are limited to the three cited US applications and their four products. A 2024 FDA secondary name-review table gives a conflicting withdrawal date for NDA018067; the original 2007 notice was inspected directly. No safety-related or worldwide withdrawal claim follows.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T131713Z-cinoxacin
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cinoxacin: supported identity and antibacterial activity; incorporate formal
  US approval withdrawals'
started_at: '2026-10-21T13:04:53Z'
finished_at: '2026-10-21T13:17:13Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the seed. Preserved initial capture hashes, appended
    actual ARO/target/FDA ownership before assessment, read the complete native record
    and maintained source rows, inspected original regulatory notices and all adopted
    publication leads, and read two complete original antibacterial/gyrase studies
    as page scans.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The exact neutral cinoxacin structure, source identities, antibacterial role
  and historical US approvals are supported. One major finding concerns the current
  APPROVED summary despite formal withdrawal of every cited US application. One informational
  follow-up preserves the difference between a database assertion of GyrA binding,
  a GyrB sensitivity relation and direct cinoxacin subunit-binding evidence. Original
  whole-cell and assembled-gyrase experiments support bounded activity and functional
  inhibition, without upgrading the native primary-evidence-needed annotations.
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
  - path: data/antibiotics/antibacterial/cinoxacin.yaml
    sha256: 94f901a5989c09619754c2018edfcb4a39adaab5a2d90546086a779fa80801ad
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
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
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/extract_fda_clinical_status.py
    sha256: f30f385ea6d530dc1749e3d805dbcdbc8715fbc476abc510bf144ea13964e171
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
- target_id: CHEBI:3716
  path: data/antibiotics/antibacterial/cinoxacin.yaml
  label: cinoxacin
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
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Actual maintained source input for the record
scope:
  description: 'Entire native record: definition, eight typed synonyms, four parents,
    role, structure, eight chemical xrefs, three drug xrefs, four document xrefs,
    two source concepts, two database-derived targets, four FDA assertions and seven
    history events; all seven adopted literature leads.'
  selection: Queue 301, exact CHEBI:3716. Initial thirteen input hashes retained and
    five actual ARO/target/FDA input owners appended before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3716
  exclusions:
  - target: Other quinolones, cinoxacin derivatives or lanthanide chelates, fungal
      metabolites, isolated target subunits and other jurisdictions
    reason: No exact activity, physical binding, producer or regulatory status is
      transferred from adjacent compounds, material forms, experiments or jurisdictions.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: No schema issues.
  target_ids:
  - CHEBI:3716
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cinoxacin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: One file, zero errors.
  target_ids:
  - CHEBI:3716
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cinoxacin.yaml --out /private/tmp/am-review-session/301-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Native SMILES/InChI, formula, zero charge, achirality, masses and both
    source-ID mints agree.
  target_ids:
  - CHEBI:3716
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 301
  exit_code: 0
  expected_exit_code: 0
- check_id: external-chemistry
  name: external-chemistry
  status: passed
  required: false
  summary: Eight independently parsed encodings from PubChem, ChEMBL, DrugCentral,
    KEGG and FDA GSRS reproduce the full native key.
  target_ids:
  - CHEBI:3716
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/301-xref-check.py
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
  - CHEBI:3716
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
  - CHEBI:3716
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
  - CHEBI:3716
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
  - CHEBI:3716
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
  - CHEBI:3716
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
  - CHEBI:3716
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
  - CHEBI:3716
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
  - CHEBI:3716
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
  - CHEBI:3716
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cinoxacin.yaml
  locator: Complete YAML.
  accessed_at: '2026-10-21T13:14:35Z'
  support: supports
  summary: SEEDED/EXACT/ANTIBACTERIAL. Neutral achiral C12H10N2O5, full key VDUWPHTZYNWKRN-UHFFFAOYSA-N.
    Two database target assertions explicitly require primary evidence. No quantitative
    activity, causal graph, biosynthetic producer or resistance determinant is asserted.
    Four product assertions preserve historical approvals and separately state Discontinued
    and currently_marketed false; aggregate clinical_status is APPROVED.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv;
    data/raw/fda_clinical_status.tsv; conf/aro_target_roles.tsv; conf/sources.yaml;
    data/raw/MANIFEST.yaml; scripts/extract_source_inventory.py; scripts/extract_fda_clinical_status.py;
    scripts/seed_from_sources.py
  locator: Complete ChEBI row 115, ARO row 307, target rows 243–244, FDA rows 3060–3063;
    source configuration/manifest and relevant extraction/assembly logic.
  accessed_at: '2026-10-21T13:14:35Z'
  support: supports
  summary: ChEBI owns definition, identity, chemical parents and role; ARO supplies
    its concept, family, aliases and target edges; FDA owns four exact-substance product
    rows. Target mapping explicitly calls GyrB a sensitive subunit while emitting
    DIRECT_BINDING_TARGET. FDA extraction selects original AP approvals and preserves
    marketing status; seeding turns eligible product rows into APPROVED assertions
    and the aggregate APPROVED summary without adjudicating later formal withdrawal.
    All native data faithfully reproduce these maintained inputs.
  snapshot_sha256: 81b85ca0c985837c015628c411029c0e00c8e40150f9409f310e32243b8da67c
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3716; https://pubchem.ncbi.nlm.nih.gov/compound/2762;
    https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1208; https://www.genome.jp/entry/D00872;
    https://drugcentral.org/drugcard/657; https://api.fda.gov/other/substance.json?search=unii:LMK22VUH23
  locator: Full official identity entries and independently parsed chemical representations.
  accessed_at: '2026-10-21T13:14:35Z'
  support: supports
  summary: ChEBI, PubChem 2762, ChEMBL1208, DrugCentral 657, KEGG D00872 and FDA GSRS
    UNII LMK22VUH23 version 21 agree on the native full graph and formula. Public
    entries cross-attest CAS 28657-80-9. All eight native aliases are source-attested;
    KEGG independently uses CIN as an abbreviation. Cinobac is retained in product
    context, not misrepresented as a different molecule.
  snapshot_sha256: bb9cb0c81924730d035c03c80bdf735e7fc87c20364000c5d38d8894deb0c191
- evidence_id: vsdb
  kind: database
  reference: https://bioregistry.io/vsdb:1881
  locator: Source-provided resolver to the University of Hertfordshire Veterinary
    Substances Database, full exact entry.
  accessed_at: '2026-10-21T13:09:43Z'
  support: supports
  summary: VSDB 1881 gives the same CAS, SMILES, InChI and full key; independent parsing
    of both encodings matches the native graph. The initially guessed cheminfo URL
    was unrelated and is not used as evidence.
  snapshot_sha256: 8b5b8c590743be6b6ef0ba40a184bb087e3ad72749bb7d17a6a47ab34a407988
- evidence_id: xref-limits
  kind: database
  reference: https://www.hmdb.ca/metabolites/HMDB0014965; https://go.drugbank.com/drugs/DB00827;
    https://bioregistry.io/lincs.smallmolecule:LSM-6552; beilstein:1084304
  locator: Official source xref attribution and attempted independent public access.
  accessed_at: '2026-10-21T13:14:35Z'
  support: unknown
  summary: HMDB and DrugBank direct retrieval returned 403; LINCS source resolver
    failed certificate validation and an earlier guessed route returned 500. These
    identifiers remain ChEBI-attested but their independent exact graphs were not
    inspected. Beilstein was not accessed through paid services. No identity contradiction
    is inferred from access failure.
  snapshot_sha256: a70b09faae464f4790ecffddd327a4d00fa585cab39bcf1ab8eef7199c65d12c
- evidence_id: parents-role
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:25754; https://www.ebi.ac.uk/chebi/CHEBI:38104;
    https://www.ebi.ac.uk/chebi/CHEBI:38770; https://www.ebi.ac.uk/chebi/CHEBI:36047;
    https://card.mcmaster.ca/aro/0000001
  locator: Official ChEBI parent/role entries and ARO:0000001 class definition/aliases/membership.
  accessed_at: '2026-10-21T13:06:28Z'
  support: supports
  summary: Oxocarboxylic acid, oxacycle and cinnoline parents fit the graph. The antibacterial-drug
    role is supported by original assays and historical clinical use. ARO:0000001
    is named fluoroquinolone antibiotic but also has the quinolone alias and includes
    nonfluorinated quinolones such as cinoxacin and nalidixic acid; the source-qualified
    family label is not independent evidence that the graph contains fluorine.
  snapshot_sha256: 76a06a4cf51248ad3e701e177e74679be478d8200b3e2f7adcd2c34b3aac177f
- evidence_id: documents
  kind: primary_source
  reference: https://patents.google.com/patent/US3669965A/en; https://patents.google.com/patent/DE2005104A1/en;
    https://patents.google.com/patent/US6441167B1/en
  locator: Original patent text, relevant compound claims, material descriptions and
    examples.
  accessed_at: '2026-10-21T13:06:30Z'
  support: context_only
  summary: US3669965 claim 2 names the exact 1-ethyl methylenedioxy oxocinnoline carboxylic
    acid; DE2005104 is the corresponding compound-family disclosure. Acid and salts
    are distinguished, so sodium-salt experimental claims are not automatically exact
    neutral-material measurements. US6441167 concerns cinoxacin lanthanide chelates
    and uses cinoxacin as a precursor; the document is relevant but chelate properties
    do not transfer. Wikipedia is a topic link, not primary evidence.
  snapshot_sha256: 755a2e458c5f30daf456486d77df48ec2905cbb3c2268d9c3c19baaddffbf8a1
- evidence_id: fda-products
  kind: database
  reference: https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:CINOXACIN&limit=100;
    https://api.fda.gov/other/substance.json?search=unii:LMK22VUH23
  locator: Complete current Drugs@FDA and GSRS responses.
  accessed_at: '2026-10-21T13:06:30Z'
  support: supports
  summary: NDA018067 products 001/002, ANDA073005 product 001 and ANDA073006 product
    001 match the native ingredient, sponsors, strengths, original approval dates,
    AP submission status and discontinued marketing. GSRS structure is exact cinoxacin.
    These accurate historical AP events do not themselves establish continuing application
    approval after a formal withdrawal.
  snapshot_sha256: 370988ac5ae7d90bc756403a7f47f4bcb34d54e9b7a34577d329aedb1acdcfe7
- evidence_id: withdrawal-2007
  kind: primary_source
  reference: https://www.govinfo.gov/content/pkg/FR-2007-11-07/pdf/E7-21886.pdf
  locator: Original FDA Federal Register notice, Table row NDA18-067 and operative
    withdrawal paragraph, pages 62858–62863.
  accessed_at: '2026-10-21T13:08:48Z'
  support: refutes
  summary: The notice explicitly withdraws NDA18-067 for Cinobac cinoxacin capsules
    250 and 500 mg, Eli Lilly, effective 2007-12-07. Holders reported products no
    longer marketed and requested withdrawal. This is formal application withdrawal,
    not an inference from marketing discontinuation and not a finding of safety-related
    withdrawal.
  snapshot_sha256: dcdd49e13243da43b6a71b1e8c7b81a18a6a2465606e09f50180eb5f843fa142
- evidence_id: withdrawal-2016
  kind: primary_source
  reference: https://www.govinfo.gov/content/pkg/FR-2016-10-04/pdf/2016-23893.pdf
  locator: Original FDA Federal Register notice, Table 1 rows ANDA073005/073006 and
    effective/operative paragraphs.
  accessed_at: '2026-10-21T13:07:16Z'
  support: refutes
  summary: FDA withdraws Teva cinoxacin 250 mg ANDA073005 and 500 mg ANDA073006 effective
    2016-11-03. The products were no longer marketed and applicants requested withdrawal,
    without prejudice to refiling. Together with the 2007 notice, every application
    supporting the native current APPROVED summary has a documented formal US withdrawal.
  snapshot_sha256: 9746877d36d5fe8f7197068c1976b1cb9defc2ba4591f8b860eb529c7898abba
- evidence_id: fda-context
  kind: primary_source
  reference: https://www.accessdata.fda.gov/drugsatfda_docs/nda/2024/217927Orig1s000NameR.pdf;
    https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2002/18067slr029ltr.pdf
  locator: 2024 proprietary-name review table and complete 2002 supplement letter.
  accessed_at: '2026-10-21T13:07:56Z'
  support: context_only
  summary: The 2002 letter supports historical approved use and product context. A
    later 2024 FDA name-review table lists an inconsistent 2005-04-04 Federal Register
    withdrawal date for NDA018067; the directly inspected 2007 original legal notice
    supplies the operative date used here. Preserve this source discrepancy rather
    than silently equating the two dates.
  snapshot_sha256: 33d7e984402dd0fc3e2af3706b5065c58099d6decc7c03bb99c6f6feeba5491b
- evidence_id: adapter
  kind: database
  reference: 'iModulonDB adapter: e_coli/precise1k/b2231; e_coli/precise1k/b3699'
  locator: Datasets discovery followed by gyrA and gyrB searches before open web research.
  accessed_at: '2026-10-21T13:14:35Z'
  support: context_only
  summary: Structured lookup resolves E. coli gyrA/b2231 and gyrB/b3699 with no matching
    iModulon memberships. The native assertions have no specified organism, so these
    are representative function/context keys only. They are neither exact cinoxacin
    binding evidence nor negative evidence from absent modules.
  snapshot_sha256: 4133e00d83de83ccc9b4bf86c34d78e5273b004106a864bd37272eea94b2a8c5
- evidence_id: aro-targets
  kind: database
  reference: ARO:3004010; ARO:3000733; ARO:3003261; https://card.mcmaster.ca/ontology
  locator: Complete current compound and two target entries plus maintained relation
    map.
  accessed_at: '2026-10-21T13:06:27Z'
  support: supports
  summary: The GyrA entry explicitly asserts fluoroquinolone binding to the alpha
    subunit, citing general reviews PMID1657531 and PMID9293187. The GyrB entry describes
    a fluoroquinolone-sensitive beta subunit without an exact cinoxacin binding assay;
    conf/aro_target_roles.tsv uses sensitivity as its mapping rationale. Both native
    edges are DATABASE-backed and PRIMARY_EVIDENCE_NEEDED. The difference in source
    assertion depth warrants a bounded follow-up, not a conclusion that GyrB cannot
    bind cinoxacin.
  snapshot_sha256: 6f7750d1655fec11ae8cafe54bb2b0ae1843fe858b83c28ed24cb2a8b0967721
- evidence_id: gyrase-primary
  kind: primary_source
  reference: PMID:3010848; DOI:10.1128/AAC.29.4.598; https://pmc.ncbi.nlm.nih.gov/articles/PMC180449/
  locator: Full original pages 598–601 visually read, especially Methods and Table
    1; page 600 full scan is 301-page600-full.png.
  accessed_at: '2026-10-21T13:08:48Z'
  support: supports
  summary: Lilly cinoxacin was tested against Micrococcus luteus MB1784/ATCC4698 and
    purified assembled gyrase from that strain. The same drug lot gave MIC greater
    than 1000 micrograms/mL and Ip 312 micrograms/mL. Ip is the lowest concentration
    producing partial inhibition of supercoiling, not IC50 or a binding constant.
    Broth MIC used 10^4 organisms/mL, tryptic soy broth, 37 degrees C and 24 hours.
    The functional reaction used A/B enzyme in a 1:1 ratio, relaxed phiX174 DNA, ATP
    and a 30-minute 37-degree-C incubation. It did not measure physical cinoxacin
    binding to an isolated subunit; the uptake comparisons involved other named quinolones.
  snapshot_sha256: 728621f54ce4968b48c56b3d8f1785cb44c9d00f9676f457ffcdcfbc5379e7ac
- evidence_id: activity-primary
  kind: primary_source
  reference: PMID:1137390; DOI:10.1128/AAC.7.3.370; https://pmc.ncbi.nlm.nih.gov/articles/PMC429140/
  locator: Full original pages 370–373 visually read, all Methods/Results/Discussion
    and cumulative curves.
  accessed_at: '2026-10-21T13:08:49Z'
  support: supports
  summary: Lilly compound 64716, cinoxacin, was assayed against 150 Enterobacteriaceae
    isolates plus 30 P. aeruginosa isolates. Agar/broth, nutrient/Mueller-Hinton medium
    and 10^6 versus 10^8 organisms/mL changed measured activity. The paper supports
    antibacterial activity but not a condition-free spectrum or a single strain MIC.
    The plots are cumulative isolate distributions; no exact strain identifiers are
    provided. Material counterion is not explicitly identified, so any future precise
    material claim must retain that limit.
  snapshot_sha256: 3dbad2a7c77de8805d23f68ecddf14ccce06eee333e1b649e39ae4d10e83de88
- evidence_id: activity-comparison
  kind: primary_source
  reference: PMID:12717; DOI:10.1128/AAC.10.6.918; https://pubmed.ncbi.nlm.nih.gov/12717/
  locator: Complete original indexed abstract inspected.
  accessed_at: '2026-10-21T13:14:35Z'
  support: supports
  summary: The original study of 138 Shigella isolates reports similar cinoxacin/nalidixic-acid
    activity, with greater oxolinic-acid potency by weight; pH and protein binding
    affect comparison. It supports the qualitative related-antibacterial-action definition
    without claiming equal potency or condition-independent activity.
- evidence_id: gyrase-other-primary
  kind: primary_source
  reference: PMID:2847648; DOI:10.1128/AAC.32.8.1192
  locator: Complete original indexed abstract.
  accessed_at: '2026-10-21T13:07:17Z'
  support: context_only
  summary: Partially purified S. aureus FDA209P gyrase was studied; cinoxacin and
    nalidixic acid had 50% inhibitory doses of at least 100 micrograms/mL. This is
    assembled-enzyme functional inhibition at abstract depth, not direct physical
    subunit binding or an exact material-form certificate.
  snapshot_sha256: c8148a70ae0250b939734b610c6fd638437086d10716d6ca85bfb6233462e4f4
- evidence_id: gyrase-reviews
  kind: database
  reference: PMID:1657531; PMID:9293187
  locator: Complete indexed abstracts and publication types of the two reviews cited
    by ARO GyrA.
  accessed_at: '2026-10-21T13:07:17Z'
  support: context_only
  summary: These are secondary reviews of gyrase structure/function and quinolone-topoisomerase
    mechanisms. General enzyme-DNA complex trapping, DNA-break and resistance mechanisms
    are context, not independently inspected exact cinoxacin binding or causal experiments.
  snapshot_sha256: c8148a70ae0250b939734b610c6fd638437086d10716d6ca85bfb6233462e4f4
- evidence_id: adopted-clinical
  kind: primary_source
  reference: PMID:7017171; DOI:10.1016/S0022-5347(17)55219-2
  locator: Complete original indexed abstract; read scope and any full-text limit
    stated explicitly.
  accessed_at: '2026-10-21T13:06:30Z'
  support: context_only
  summary: The ARO-adopted single-blind UTI trial randomized 50 patients to cinoxacin
    or nalidixic acid and found comparable eradication/clinical response. It supports
    former clinical use but does not establish the ARO compound-page mechanism of
    direct gyrase inhibition, double-strand breaks and death.
  snapshot_sha256: c629787bb8d6e35dfddb111331feb59700a89392b8738e3a48f1f189e15635f9
- evidence_id: adopted-gyrase
  kind: primary_source
  reference: PMID:3005575; DOI:10.1021/jm00153a015
  locator: Complete original indexed abstract; read scope and any full-text limit
    stated explicitly.
  accessed_at: '2026-10-21T13:06:30Z'
  support: context_only
  summary: This original sixty-compound quinolone SAR abstract correlates gyrase inhibition
    and antibacterial activity, but does not provide an exact cinoxacin row. The ACS
    full-text route returned 403; no uninspected table or subunit binding result is
    claimed.
  snapshot_sha256: c629787bb8d6e35dfddb111331feb59700a89392b8738e3a48f1f189e15635f9
- evidence_id: adopted-transformation
  kind: primary_source
  reference: PMID:12204384; DOI:10.1111/j.1574-6968.2002.tb11336.x
  locator: Complete original indexed abstract; read scope and any full-text limit
    stated explicitly.
  accessed_at: '2026-10-21T13:06:30Z'
  support: context_only
  summary: Beauveria bassiana ATCC7159 transforms added cinoxacin into reduced metabolites
    over twenty days. This is biotransformation of dosed substrate, not evidence that
    the fungus biosynthesizes cinoxacin.
  snapshot_sha256: c629787bb8d6e35dfddb111331feb59700a89392b8738e3a48f1f189e15635f9
- evidence_id: adopted-chlorella
  kind: primary_source
  reference: PMID:16295658; DOI:10.1007/BF02931567
  locator: Complete original indexed abstract; read scope and any full-text limit
    stated explicitly.
  accessed_at: '2026-10-21T13:06:30Z'
  support: context_only
  summary: The study concerns endosymbiotic Chlorella in green hydra and damage to
    chloroplasts/mitochondria; it does not establish a bacterial molecular target.
  snapshot_sha256: c629787bb8d6e35dfddb111331feb59700a89392b8738e3a48f1f189e15635f9
- evidence_id: adopted-host
  kind: primary_source
  reference: PMID:29438107; DOI:10.1172/JCI97739
  locator: Complete original indexed abstract; read scope and any full-text limit
    stated explicitly.
  accessed_at: '2026-10-21T13:06:30Z'
  support: context_only
  summary: The abstract concerns methyldopa inhibition of human HLA-DQ8 in autoimmune
    diabetes. A bounded exact-cinoxacin search of the accessible main text found no
    match; supplementary compound screening was not inspected. No human immune-target
    assertion transfers to this antibacterial record.
  snapshot_sha256: c629787bb8d6e35dfddb111331feb59700a89392b8738e3a48f1f189e15635f9
- evidence_id: adopted-adverse
  kind: primary_source
  reference: PMID:3147004; DOI:10.1136/bmj.297.6661.1434
  locator: Complete original indexed abstract; read scope and any full-text limit
    stated explicitly.
  accessed_at: '2026-10-21T13:06:30Z'
  support: context_only
  summary: The original abstract reports cinoxacin-associated anaphylaxis cases. It
    supplies adverse-effect context, not antibacterial mechanism and not proof that
    the later regulatory withdrawals were safety-driven.
  snapshot_sha256: c629787bb8d6e35dfddb111331feb59700a89392b8738e3a48f1f189e15635f9
- evidence_id: adopted-unavailable
  kind: database
  reference: PMID:6226270; https://pubmed.ncbi.nlm.nih.gov/6226270/
  locator: Indexed metadata and publisher resolution of its externally attached DOI.
  accessed_at: '2026-10-21T13:07:56Z'
  support: unknown
  summary: Hatch 1983, AUAA Journal 3(3):10–11, Cinoxacin for urinary tract infection,
    has no indexed abstract. Europe PMC attaches DOI10.1007/BF03288285, but that DOI
    resolves to a different 1976 Inpharma newsletter item. The native source cites
    the PMID only, so this is a retrieval metadata conflict, not a demonstrated native
    erroneous DOI. No full original Hatch text was inspected.
  snapshot_sha256: 60e17a71203e903ec473aed5312c764090a21e2ee964bb1da999e9c3672890f7
- evidence_id: inclusive-search
  kind: search
  reference: 301-inclusive-hits.txt
  locator: Exact identifier, label, key and ARO identifier across local maintained
    and generated content, including hidden and ignored files.
  accessed_at: '2026-10-21T13:14:35Z'
  support: context_only
  summary: Matches comprise native/source rows, queue/PATHS and generated embeddings.
    No exact curator decision or maintained evidence overlay was found in the bounded
    searched scope. This is not a claim that additional public literature cannot exist.
  snapshot_sha256: a56aaf34fa554c0ec4dfce78479f10627b41650cfb75b04db6c53c1f04c25db5
  search_scope: rg --no-ignore --hidden -n -F for CHEBI:3716, cinoxacin, VDUWPHTZYNWKRN-UHFFFAOYSA-N
    and ARO:3004010 across data, curation, conf, scripts, src, docs, .claude, reviews
    and reports. Bounded public official identity/regulatory and exact-compound primary-literature
    searches on 2026-10-21.
- evidence_id: validation
  kind: validation
  reference: 301-schema.log; 301-strict.log; 301-chemistry.json; 301-xref-chemistry.json;
    301-vsdb-chemistry.json
  locator: Actual focused checks and independent chemistry diagnostics.
  accessed_at: '2026-10-21T13:14:35Z'
  support: supports
  summary: Schema and strict checks pass. Native and official external structures
    match. Both source identifiers reproduce their minted values. All eighteen captured
    input hashes, including the original thirteen, remain unchanged.
  snapshot_sha256: b503f57a538a7bd9cf169f3190950610f10097613765b6daba5c33b857e91d1f
assessments:
- assessment_id: identity
  area: identity
  topic: Exact free acid, names, structure and xrefs
  outcome: supported
  summary: The native identity is internally coherent and independently corroborated
    by multiple official chemical graphs. Restricted registry entries remain explicitly
    unverified; patent document links concern related disclosures and are not all
    exact chemical equivalences.
  target_ids:
  - CHEBI:3716
  evidence_ids:
  - native
  - identity
  - vsdb
  - xref-limits
  - documents
  - validation
- assessment_id: classification
  area: scope
  topic: Parent and antibacterial scope
  outcome: supported
  summary: Chemical parents fit; ARO family nomenclature is interpreted using the
    actual broader quinolone source class. Original cinoxacin assays and historical
    clinical trial support the antibacterial drug role with assay/material limits.
  target_ids:
  - CHEBI:3716
  evidence_ids:
  - parents-role
  - activity-primary
  - activity-comparison
  - adopted-clinical
- assessment_id: regulatory
  area: evidence
  topic: Historical approvals versus current regulatory state
  outcome: concern
  summary: All four FDA assertions accurately retain original approval events and
    discontinued marketing, but the regulatory-status summary omits formal withdrawal
    of all three cited US applications. Schema clinical_status denotes regulatory/use
    status, and WITHDRAWN is available. Historical approval dates must remain intact.
  target_ids:
  - CHEBI:3716
  evidence_ids:
  - owners
  - fda-products
  - withdrawal-2007
  - withdrawal-2016
  - fda-context
- assessment_id: targets
  area: evidence
  topic: GyrA/GyrB assertion depths and functional evidence
  outcome: unknown
  summary: The primary-evidence-needed database status is honest. ARO directly asserts
    GyrA binding; its GyrB description and map rationale establish sensitivity rather
    than an inspected physical binding experiment. Assembled-gyrase inhibition neither
    proves nor refutes direct binding to each subunit. A bounded mapping review is
    appropriate without claiming confirmed nonbinding.
  target_ids:
  - CHEBI:3716
  evidence_ids:
  - adapter
  - aro-targets
  - gyrase-primary
  - gyrase-other-primary
  - gyrase-reviews
- assessment_id: completeness
  area: completeness
  topic: Optional exact primary activity and mechanism enrichment
  outcome: unknown
  summary: The original experiments could support qualified functional target/activity
    observations. Their absence from a SEEDED record is not independently a required-field
    defect. Biotransformation, host effects and secondary mechanism reviews do not
    justify producer or causal-graph additions. All seven adopted leads have explicit
    dispositions at the stated read depth.
  target_ids:
  - CHEBI:3716
  evidence_ids:
  - activity-primary
  - gyrase-primary
  - adopted-gyrase
  - adopted-transformation
  - adopted-chlorella
  - adopted-host
  - adopted-adverse
  - adopted-unavailable
findings:
- finding_id: F1
  issue_key: cinoxacin-formally-withdrawn-us-approvals
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Represent formal withdrawal of the cited US approvals
  description: clinical_status APPROVED and the unqualified product status APPROVED
    summarize four historical AP events, although original FDA notices withdrew NDA018067
    effective 2007-12-07 and ANDA073005/073006 effective 2016-11-03. Discontinued
    marketing and currently_marketed false are accurately preserved, but are distinct
    from formal withdrawal of approval. The schema defines a regulatory/use status
    and provides WITHDRAWN. Incorporate the later US events and qualify the current
    summary while preserving all historical approval dates and product provenance.
    Do not infer worldwide withdrawal or a safety reason.
  target_ids:
  - CHEBI:3716
  field_paths:
  - clinical_status
  - clinical_status_assertions
  evidence_ids:
  - owners
  - fda-products
  - withdrawal-2007
  - withdrawal-2016
  rule_id: 'native-review-checklist: Clinical and regulatory claims; review-yaml-record:
    preserve scope and conflicts'
  native_severity: major
  normalization_reason: Confirmed later primary regulatory events contradict the current
    aggregate regulatory-status reading for every cited US application. This is a
    source-to-status transformation gap, not merely missing marketing detail or optional
    historical enrichment.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Maintain product-level regulatory events
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Extract current status without losing historical approval
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Emit qualified product and aggregate clinical status
- finding_id: F2
  issue_key: cinoxacin-gyrb-sensitivity-direct-binding-uncertainty
  category: evidence
  severity: informational
  status: open
  certainty: provisional
  title: Resolve the GyrB sensitivity-to-direct-binding mapping at its stated evidence
    depth
  description: The GyrB source entry and local mapping rationale describe a fluoroquinolone-sensitive
    subunit, while the native target relation is DIRECT_BINDING_TARGET. The native
    DATABASE and PRIMARY_EVIDENCE_NEEDED qualification already makes the primary-evidence
    gap visible. The inspected exact cinoxacin experiment measures assembled-gyrase
    supercoiling inhibition, not isolated GyrB binding; this neither proves nor refutes
    physical binding. Review whether the maintained source relation justifies the
    direct-binding type, or needs a weaker relation/context. Keep GyrA separate because
    its upstream entry explicitly asserts binding.
  target_ids:
  - CHEBI:3716
  field_paths:
  - molecular_targets[1].target_relation
  - molecular_targets[1].context
  evidence_ids:
  - owners
  - aro-targets
  - gyrase-primary
  - gyrase-reviews
  rule_id: 'native-review-checklist: Mechanism and target evidence; review-yaml-record:
    narrowest supported claim'
  native_severity: informational
  normalization_reason: Unresolved relation semantics with an existing explicit evidence
    warning. No confirmed false binding claim is inferred solely from absence of an
    inspected direct-binding experiment.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Review relation mapping rationale
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Preserve upstream target relation and context
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproduce source-qualified target assertions
actions:
- action_id: A1
  description: Reconcile formal US withdrawal events with product-level history and
    aggregate status through the maintained FDA pipeline.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:3716
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Maintain product-level regulatory events
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Extract current status without losing historical approval
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Emit qualified product and aggregate clinical status
  acceptance_checks:
  - Retain original approval dates, identifiers, sponsors and strengths for all four
    assertions; cite original Federal Register notices and effective withdrawal dates.
  - Represent current withdrawn US application status without equating all discontinued
    products with withdrawn approvals and without inventing a safety cause or worldwide
    status.
  - Document the 2024 secondary FDA table date conflict while using the original 2007
    notice as the operative evidence. Reseed and rerun focused validators plus applicable
    source-reproduction gates.
- action_id: A2
  description: Review the GyrB relation mapping without upgrading or negating binding
    beyond inspected evidence.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:3716
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Review relation mapping rationale
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Preserve upstream target relation and context
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproduce source-qualified target assertions
  acceptance_checks:
  - Distinguish an upstream explicit binding assertion from sensitivity/complex membership
    and from direct compound-specific physical evidence. Preserve DATABASE and PRIMARY_EVIDENCE_NEEDED
    unless appropriate original evidence is inspected.
  - If the relation remains DIRECT_BINDING_TARGET, explain its source-semantic basis;
    otherwise choose the schema relation justified by the source. Do not extrapolate
    the conclusion to GyrA or all quinolones.
- action_id: A3
  description: If enriching the exact record, curate original functional and antibacterial
    observations with full assay context.
  finding_ids: []
  target_ids:
  - CHEBI:3716
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cinoxacin.yaml
    role: Curator-owned primary literature additions
  acceptance_checks:
  - For PMID3010848 distinguish MIC greater than 1000 micrograms/mL from partial-supercoiling-inhibition
    Ip 312 micrograms/mL and preserve M. luteus MB1784/ATCC4698, material, medium
    and reaction conditions. Ip is not IC50 or Kd.
  - For PMID1137390 retain medium and inoculum dependence and population distributions,
    without inventing single-strain measurements or exact salt identity. Do not transfer
    fungal transformation or human MHC effects as bacterial mechanism or biosynthesis.
limitations:
- Independent HMDB, DrugBank and LINCS exact-entry access was unavailable; Beilstein
  was not accessed through paid services. The identifiers remain source-attested,
  while multiple other official structures independently confirm native identity.
- All seven adopted leads were resolved and dispositioned. Six were read as complete
  original indexed abstracts; PMID6226270 has no indexed abstract and its externally
  supplied DOI resolves to a different publication. Its original text was not inspected.
  The ACS full paper for PMID3005575 was inaccessible.
- 'Two additional original studies were read completely as page scans: PMID1137390
  and PMID3010848. PMID2847648 and PMID12717 were read at original-abstract depth.
  Secondary gyrase reviews were not treated as exact primary evidence.'
- Exact material counterion and direct subunit binding are not established by the
  inspected cinoxacin antibacterial/gyrase papers. Functional inhibition is not a
  measured physical-binding constant or a complete causal chain to bacterial death.
- Regulatory conclusions are limited to the three cited US applications and their
  four products. A 2024 FDA secondary name-review table gives a conflicting withdrawal
  date for NDA018067; the original 2007 notice was inspected directly. No safety-related
  or worldwide withdrawal claim follows.
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
