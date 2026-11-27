# Clarithromycin: coherent chemistry, qualified mechanism and resistance; separate brand naming

- Review: 20261021T132733Z-clarithromycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T13:05:00Z
- Finished UTC: 2026-10-21T13:27:33Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The full record has coherent exact chemistry, reproducible source provenance, qualified primary ribosome evidence, ten correctly bounded erm(55) associations and byte-exact CRyPTIC memberships. All45 FDA assertions agree with current application/product data. One minor finding concerns Biaxin being typed as an exact chemical synonym despite its product-name role. Primary access and assay-material boundaries remain explicit.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position307; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3732 | data/antibiotics/antibacterial/clarithromycin.yaml | generated | clarithromycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:3732 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:3732 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:3732 | Actual focused execution exited 0. |
| Exact CRyPTIC membership reconstruction | passed | False | CHEBI:3732 | All six groups and537 memberships reproduce byte-for-byte from maintained inventories; membership validation passes. |
| Authoritative full QC | failed | True | CHEBI:3732 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3732 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3732 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3732 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3732 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3732 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3732 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3732 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3732 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact chemistry, aliases and xrefs

identity: concern. Targets: CHEBI:3732.

The exact chemical representations agree across eight independent official encodings. One product alias has the wrong synonym type. Inaccessible legacy entries remain source-attested, not independently verified.

### Mode, target and causal graph

evidence: supported. Targets: CHEBI:3732.

Primary structural binding and cellular translation evidence support the broad mechanism. Native qualifiers correctly distinguish the coarse database P-site relation from curated NPET context. Every edge was reviewed; full elongation-specific causal dissection is not established by the accessible1998 abstract.

### All54 resistance assertions and corrected clinical table

evidence: supported. Targets: CHEBI:3732.

The44 imported associations retain database depth. All ten curated clinical associations match corrected Table2 and remain observational rather than allele-causal. Later engineered-host functional evidence is separate optional enrichment.

### CRyPTIC group and membership fidelity

evidence: supported. Targets: CHEBI:3732.

Six source groups and all537 subject links are faithful and reproducible, with unknown phenotypes and source testing criteria preserved.

### Exact ingredient, historical approval and marketing

evidence: supported. Targets: CHEBI:3732.

All45 current application/product comparisons pass; GSRS exact chemistry is stable across recorded versions. Product brands remain a distinct naming layer.

### Source ownership, adopted citation dispositions and immutable inputs

provenance: supported. Targets: CHEBI:3732.

Every native field group and all adopted original/secondary leads were assessed at explicit read depths. Maintained inputs and curator additions are separated, source mints and history retained, all30 hashes unchanged.

### Remaining evidence depth and optional enrichment

completeness: unknown. Targets: CHEBI:3732.

Exact primary graph/association evidence is substantial but full scientific sign-off is limited by inaccessible legacy entries, selected primary access and unresolved elongation-specific endpoint detail. Missing optional primary mechanisms for all44 database associations are not automatically defects.

## Findings

### F1: Type Biaxin as a brand name

minor / open / confirmed; issue key: clarithromycin-biaxin-brand-exact-synonym.

Biaxin is an FDA product name whose active ingredient is clarithromycin, but the native ARO synonym is EXACT_SYNONYM. Preserve the useful name with BRAND_NAME typing through maintained source handling. Review other ARO trade-name aliases individually; do not change correct chemical names or use brands to collapse preparations.

## Recommended Actions And Acceptance Checks

### A1

Preserve Biaxin with product-name typing through the maintained synonym path.

- Biaxin is BRAND_NAME rather than EXACT_SYNONYM; independently check other trade-name aliases before applying the same change.
- Reseeding reproduces the change without altering exact chemistry, clinical product provenance or primary curator evidence; run focused schema/strict and source-reproduction gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/clarithromycin.yaml; Entire1880-line record, all54 resistance entries,45 clinical assertions, six activity observations, membership reference, graph and11 history events | supports | Neutral C38H69NO13 exact clarithromycin with18 assigned stereocenters. The record separates44 CARD database assertions from ten observational UNKNOWN erm(55) associations, preserves CRyPTIC group semantics and historical FDA provenance, and uses a curated translation-inhibition graph with an explicitly broader ARO P-site mapping. No biosynthetic producer or clinical dosing advice is asserted. |
| owners | data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv;data/raw/aro_target_edges.tsv;data/raw/aro_resistance_edges.tsv;data/raw/fda_clinical_status.tsv;data/raw/cryptic_activity.tsv;conf/sources.yaml;scripts/seed_from_sources.py; Exact frozen rows and source/mapping ownership, plus all captured curator and membership inputs | supports | ChEBI owns identity/chemistry/definition/chemical parents; ARO supplies class/aliases, one target and44 resistance rows; FDA supplies45 clinical rows; CRyPTIC supplies six groups. Native curator-owned mode, causal graph and ten resistance associations are separate from seeded content. The original13 input hashes and17 appended actual inputs remain unchanged; generated-source fields require maintained-owner changes. |
| chemistry | 307-chemistry.json;307-xref-chemistry.json; Independent native and official-source graph calculations | supports | Native SMILES/InChI and ChEBI, PubChem84029, ChEMBL1741, KEGGC06912, DrugCentral668, LipidMapsLMPK04000014, PDBCCDCTY and GSRSH1250JIK0A all produce AGOYDEPGAOXOCK-KCBOHYOISA-N, matching composition, neutral charge and stereochemistry. Native formula/masses and both source mints pass. |
| chemical-groundings | https://www.ebi.ac.uk/chebi/CHEBI:3732;https://www.genome.jp/entry/C06912;https://www.lipidmaps.org/databases/lmsd/LMPK04000014;https://files.rcsb.org/ligands/download/CTY.cif; Official identity, aliases, parent/role terms and exact structures | supports | The methylated erythromycin identity and macrolide/glycoside structure fit the native parents and antibacterial role. KEGGD00276 is drug context; CAS81103-11-9 is independently cross-attested. All19 aliases were read, including chemical names/abbreviations and ARO product names. Biaxin is separately confirmed as an FDA product name. |
| patents | https://patents.google.com/patent/US4331803A/en;https://patents.google.com/patent/EP0041355A1/en; Original disclosure, Example1 exact6-O-methylerythromycinA, TE-031 antibacterial experiment and separation from TE-032 | supports | Both source-linked patents describe6-O-methylerythromycinA and distinguish the6,11-dimethyl compound. Example1 supplies formula C38H69NO13 and M+747; TE-031 names the parent in an agar-dilution assay. These documents support identity and experimental antibacterial context, not current clinical recommendations or patent legal status. |
| adapter | iModulonDB m_tuberculosis/modulome; e_coli/precise1k; s_aureus/staph_precise108; Catalog then rrl and erm(37) queries before primary mechanism follow-up | context_only | No iModulon components matched. The Mtuberculosis erm(37) query returned Rv1988; rrl queries returned no genes. The catalog lacks a matching Mchelonae dataset. These results are context only, with no negative biological inference, binding claim or clinical resistance transfer. |
| binding-primary | PMID:34935599;DOI:10.1080/22221751.2021.2022439;https://pmc.ncbi.nlm.nih.gov/articles/PMC8786254/; Complete original main XML, Materials/Methods, Results, Discussion and captions; supplement not inspected | supports | The3.3Å cryo-EM structure uses purified M.tuberculosisH37Ra50S and Sigma clarithromycin, with solvent exchange from acetone stock. It directly locates clarithromycin in the23SrRNA nascent-peptide exit tunnel. PDB7F0D corroborates the structural deposition. Specific water-mediated dynamics, resistance explanations and therapeutic synergy are interpretations or prior-study context, not new whole-cell functional measurements. |
| translation-primary | PMID:9425251;DOI:10.1007/s002849900290;https://link.springer.com/article/10.1007/s002849900290; Complete original indexed and publisher abstracts;1998 paper full text not obtained | supports | The S.aureus study measures growth, translation and50S assembly inhibition. Clarithromycin growth ID50 is0.075µg/mL and translation/assembly ID50 is0.15µg/mL; these are not MICs. This supports protein-synthesis inhibition while showing assembly effects also contribute. The accessible abstract does not isolate an elongation-only rate or independently certify starting material form. |
| graph | data/antibiotics/antibacterial/clarithromycin.yaml; All five causal nodes and four edges, two edge citations and explicit mapping qualifiers | supports | The graph models drug binding at the50S/23SrRNA NPET, a bound state and decreased translation/protein synthesis. RNA and biological-process nodes are not protein examples. The ARO P-site identifier is explicitly related/coarse, not asserted exact NPET identity. Structural binding and measured cellular translation are distinguished; the selected papers do not measure every edge in a single system or exclude parallel50S assembly effects. |
| card | https://card.mcmaster.ca/aro/0000065;https://card.mcmaster.ca/aro/3000757;44 determinant entries in307-card-digest.json; All current target/determinant definitions, relation context and native source correspondence | supports | Erm methylases, macrolide phosphotransferases, esterases, lmrP and species-specific23SrRNA mutation families are preserved as imported database assertions. Generic gene presence does not establish a strain phenotype or exact variant. The broad50S target remains PRIMARY_EVIDENCE_NEEDED; current CARD descriptions and citations are not silently upgraded to experimentally verified clarithromycin mechanisms. |
| erm55-original | PMID:37347171;DOI:10.1128/jcm.00428-23;https://journals.asm.org/doi/full/10.1128/jcm.00428-23; Original abstract, Introduction, complete Methods, Tables1–2 and early Results; later Results/Discussion incompletely accessible | supports | Commercial broth-microdilution plates, species identification and variant assays support matched clinical-isolate phenotypes and erm(55) genomic context. Resistant/susceptible paired isolates support association, without knockout/complementation or demonstrated horizontal transfer. Retrospective and prospective collections are distinct. Prepared antimicrobial form was not independently chemically characterized. |
| erm55-correction | PMID:38572983;DOI:10.1128/jcm.00415-24;https://journals.asm.org/doi/10.1128/jcm.00415-24; Entire original erratum, corrected Table2 and footnotes as publisher text | supports | All ten native resistant isolates match the corrected cells: six55P, two55T and two55C. The still-inconsistent heading must not override the cells. Several isolates become resistant only at extended readings. The susceptible20:68529 comparator and six intermediate isolates are correctly excluded. Native family-level UNKNOWN associations retain those distinctions and do not export numerical AST or allele-level causation. |
| erm55-functional | PMID:39817789;DOI:10.1128/spectrum.02397-24;https://pmc.ncbi.nlm.nih.gov/articles/PMC11878018/; Complete current original main XML and Tables1–3 independently read by source auditor; FigureS1 not inspected | context_only | Heterologous55P/C/T expression in efflux-deficient E.coliM6394Δ9 raises clarithromycin MIC relative to vector control. This is causal functional resistance in that engineered host, distinct from the ten clinical-isolate associations. The authors did not measure ribosomal methylation; proposed residue effects remain hypotheses. Optional enrichment should preserve construct, host and assay context. |
| cryptic | 307-membership-audit.json;data/raw/cryptic_activity.tsv;data/raw/cryptic_memberships.tsv.gz;data/raw/cryptic_isolates.tsv.gz; All six observations, membership payload inspection and complete maintained-source reconstruction | supports | The six MTBC-qualified source groups preserve method/project/critical-concentration and R/S/U distinctions. MYCOTB0.5mg/L groups have6R,6S,451U; solid7H10 at3mg/L has52R,21S; one method-unspecified group has1R. All537 subjects/memberships/measurements,333 unlinked subjects, counts, hashes and bytes reproduce exactly. Unknown is not susceptibility, and source criteria are not independently endorsed clinical breakpoints. |
| clinical | https://api.fda.gov/drug/drugsfda.json;https://gsrs.ncats.nih.gov/api/v1/substances/H1250JIK0A; Every native clinical row compared to current exact application/product and substance data | supports | All45 assertions across27 applications match current ingredient, product name, sponsor, original approval date and marketing status. Discontinued products remain explicitly distinct from currently marketed prescription products. Current GSRSversion89 matches native chemistry; historicalversion83 remains dated provenance. Individual labels for every product were not independently reread. |
| brand | https://api.fda.gov/drug/drugsfda.json?search=application_number:NDA050662; Original FDA current application/product response; native synonyms and clinical rows | supports | NDA050662 identifies BIAXIN as the product brand with CLARITHROMYCIN as active ingredient. Native ARO alias Biaxin is typed EXACT_SYNONYM, conflating product naming with chemical synonymy despite available BRAND_NAME typing. Other ARO trade names need the same bounded classification check rather than blanket deletion. |
| adopted-review | PMID:7683018;DOI:10.1093/jac/31.suppl_c.1; Indexed abstract explicitly truncated at250words; publication type review | context_only | The adopted macrolide overview supplies historical class context. It is secondary literature, and the truncated abstract is not represented as complete primary evidence or a compound-specific binding experiment. |
| adopted-derivatives | PMID:16387493;DOI:10.1016/j.bmcl.2005.12.033; Complete original indexed abstract; full parent-comparator table not inspected | context_only | The adopted study tests new4-double-prime malonyl clarithromycin derivatives, including cell-free translation and50S binding. The accessible abstract does not establish a quantitative unmodified-parent row. Derivative properties are not transferred to native clarithromycin. |
| access | 307-fetch-results.json;307-full-fetch-results.json;307-309-extra-results.json;307-erm55-source-report.json; Explicit source retrieval/read-depth ledger | unknown | HMDB and DrugBank direct routes returned403; legacy LINCS resolver had certificate failure. The1998 PDF route returned publisher HTML rather than a PDF.2023/2024 ASM text was partly available through the browser, while later retrieval was403; EuropePMC XML500 and PMC challenges did not supply their full texts. A university search hit was actually a nomenclature table, not the original study. No access obstacle was treated as contrary evidence. |

## Limits And Additional Notes

- The1998 original paper was available only as a complete indexed/publisher abstract. Its translation and50S assembly readouts are not an isolated elongation-rate measurement; no exact MIC is inferred.
- The2023 erm55 original was read through Methods, Tables1–2 and early Results, not the complete later Results/Discussion. The entire2024 correction was read as publisher text. The2025 functional main XML was inspected, but its supplementary FigureS1 was not.
- The binding-study main XML was read in full; supplementary atom-contact/energy tables and deposited cryo-EM map were not independently reprocessed. No proposed water-dynamics or synergy model is elevated to a new causal experimental result.
- HMDB/DrugBank direct bodies and legacy LINCS entry remain unresolved. GSRSversion89 corroborates chemistry while native datedversion83 remains historical. All45 FDA rows were compared, but individual generic product labels were not all read.
- All44 imported CARD relationships were checked at database/source-relation depth; their full underlying bibliographies were not exhaustively read. Native evidence qualifications remain appropriate.
- The adopted1993 overview abstract is explicitly truncated, and the2006 derivative paper was inspected at abstract depth. Their scope does not provide exact parent quantitative results.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T132733Z-clarithromycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Clarithromycin: coherent chemistry, qualified mechanism and resistance; separate
  brand naming'
started_at: '2026-10-21T13:05:00Z'
finished_at: '2026-10-21T13:27:33Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. The entire record
    and maintained source were read, independent chemistry calculated, asserted chemical
    groundings checked and exact-compound primary literature assessed with explicit
    access boundaries.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The full record has coherent exact chemistry, reproducible source provenance,
  qualified primary ribosome evidence, ten correctly bounded erm(55) associations
  and byte-exact CRyPTIC memberships. All45 FDA assertions agree with current application/product
  data. One minor finding concerns Biaxin being typed as an exact chemical synonym
  despite its product-name role. Primary access and assay-material boundaries remain
  explicit.
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
  - path: data/antibiotics/antibacterial/clarithromycin.yaml
    sha256: ab9144b6a1b21521e7166f05819d832e9ce4d127438ac1aa1e2e9f82d02a453c
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
    role: Adopted identity/class/aliases and publication leads
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: Adopted ribosomal target assertion
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: Adopted44 database resistance assertions
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: Target relation/type mapping
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
    role: Adopted45 FDA/GSRS assertions
  - path: scripts/extract_fda_clinical_status.py
    sha256: f30f385ea6d530dc1749e3d805dbcdbc8715fbc476abc510bf144ea13964e171
    role: FDA/GSRS assertion extraction
  - path: data/raw/cryptic_activity.tsv
    sha256: fa2fe5e5258328f10f9fe5724e4b74f354a98f5355bac68108ab28ffb17c7987
    role: Adopted6 activity groups
  - path: curation/cryptic_drug_map.tsv
    sha256: 69643f9b5e6dfc91761a4541317de63c5dca565131f6a07a3193878d7f863a54
    role: Exact CRyPTIC drug mapping
  - path: data/raw/cryptic_memberships.tsv.gz
    sha256: f121fc3ac48a44a89931366d908877d833bd846d9690257583c5dbbdb8bd2601
    role: Adopted source membership records
  - path: data/raw/cryptic_isolates.tsv.gz
    sha256: 7d51bf3032e295a56e2543f52f12e59d6a8589ad6f2208e2314a154e6e8cf2c5
    role: Adopted subject metadata
  - path: scripts/extract_cryptic_memberships.py
    sha256: d944260859c29ff3af55137c311e14be45b6c3219b5283c4cbd1b794d49fe952
    role: Membership extraction owner
  - path: scripts/cryptic_membership_inventory.py
    sha256: b0d8ae24cac64dfb2813bfa5a5ef590e3330e3c5ace82e25f3528b025147d6cc
    role: Source membership validation and loading
  - path: src/antibioticmech/activity_memberships.py
    sha256: 22849043b741d7a48a708dfade09524a11ac46afa7efb08d350ec7422ec2e146
    role: Native membership objects
  - path: data/antibiotics/antibacterial/membership-ac9b7b540ddc33b670ff85e5077fe30655c4f674d904871781fa9e818a240b27.json.gz
    sha256: ac9b7b540ddc33b670ff85e5077fe30655c4f674d904871781fa9e818a240b27
    role: Exact native membership sidecar
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: Existing CARD evidence qualifications context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: CARD qualification validation and emission
  - path: curation/uniprot_protein_examples.yaml
    sha256: 536ab4cc7ba9be95c80242bcc25321d67a5bdbfecbc50f3be5a449000abfe5f5
    role: Existing target/node review context
targets:
- target_id: CHEBI:3732
  path: data/antibiotics/antibacterial/clarithromycin.yaml
  label: clarithromycin
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
    role: Adopted identity/class/aliases and publication leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted ribosomal target assertion
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted44 database resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target relation/type mapping
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Adopted45 FDA/GSRS assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: FDA/GSRS assertion extraction
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_activity.tsv
    role: Adopted6 activity groups
  - repository: CultureBotAI/AntibioticMech
    path: curation/cryptic_drug_map.tsv
    role: Exact CRyPTIC drug mapping
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_memberships.tsv.gz
    role: Adopted source membership records
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/cryptic_isolates.tsv.gz
    role: Adopted subject metadata
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_cryptic_memberships.py
    role: Membership extraction owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/cryptic_membership_inventory.py
    role: Source membership validation and loading
  - repository: CultureBotAI/AntibioticMech
    path: src/antibioticmech/activity_memberships.py
    role: Native membership objects
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/membership-ac9b7b540ddc33b670ff85e5077fe30655c4f674d904871781fa9e818a240b27.json.gz
    role: Exact native membership sidecar
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Existing CARD evidence qualifications context
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: CARD qualification validation and emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/uniprot_protein_examples.yaml
    role: Existing target/node review context
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/clarithromycin.yaml
    role: Curator-owned mode, causal graph and ten observational resistance associations
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position307; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3732
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3732
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    307
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3732
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/clarithromycin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3732
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/clarithromycin.yaml --out /private/tmp/am-review-session/307-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: membership-reproduction
  name: Exact CRyPTIC membership reconstruction
  status: passed
  required: false
  summary: All six groups and537 memberships reproduce byte-for-byte from maintained
    inventories; membership validation passes.
  target_ids:
  - CHEBI:3732
  evidence_ids:
  - cryptic
  command: .venv/bin/python /private/tmp/am-review-session/307-membership-check.py
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
  - CHEBI:3732
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
  - CHEBI:3732
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
  - CHEBI:3732
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
  - CHEBI:3732
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
  - CHEBI:3732
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
  - CHEBI:3732
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
  - CHEBI:3732
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
  - CHEBI:3732
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
  - CHEBI:3732
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/clarithromycin.yaml
  locator: Entire1880-line record, all54 resistance entries,45 clinical assertions,
    six activity observations, membership reference, graph and11 history events
  accessed_at: '2026-10-21T13:24:10Z'
  support: supports
  summary: Neutral C38H69NO13 exact clarithromycin with18 assigned stereocenters.
    The record separates44 CARD database assertions from ten observational UNKNOWN
    erm(55) associations, preserves CRyPTIC group semantics and historical FDA provenance,
    and uses a curated translation-inhibition graph with an explicitly broader ARO
    P-site mapping. No biosynthetic producer or clinical dosing advice is asserted.
  snapshot_sha256: 5e535418fd03a0e60e36edace8bb4992c5047c955ce64fc0bfd270004db9109d
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv;data/raw/aro_target_edges.tsv;data/raw/aro_resistance_edges.tsv;data/raw/fda_clinical_status.tsv;data/raw/cryptic_activity.tsv;conf/sources.yaml;scripts/seed_from_sources.py
  locator: Exact frozen rows and source/mapping ownership, plus all captured curator
    and membership inputs
  accessed_at: '2026-10-21T13:24:10Z'
  support: supports
  summary: ChEBI owns identity/chemistry/definition/chemical parents; ARO supplies
    class/aliases, one target and44 resistance rows; FDA supplies45 clinical rows;
    CRyPTIC supplies six groups. Native curator-owned mode, causal graph and ten resistance
    associations are separate from seeded content. The original13 input hashes and17
    appended actual inputs remain unchanged; generated-source fields require maintained-owner
    changes.
  snapshot_sha256: 6c18dc3252ca8e03f49841615cdf7a4988c773fb0a626c256ca541f8ad21835d
- evidence_id: chemistry
  kind: validation
  reference: 307-chemistry.json;307-xref-chemistry.json
  locator: Independent native and official-source graph calculations
  accessed_at: '2026-10-21T13:24:10Z'
  support: supports
  summary: Native SMILES/InChI and ChEBI, PubChem84029, ChEMBL1741, KEGGC06912, DrugCentral668,
    LipidMapsLMPK04000014, PDBCCDCTY and GSRSH1250JIK0A all produce AGOYDEPGAOXOCK-KCBOHYOISA-N,
    matching composition, neutral charge and stereochemistry. Native formula/masses
    and both source mints pass.
  snapshot_sha256: 81cdf261631a57111efa0896ac2ff7e699f7172f39c691583c3938060a6a9e89
- evidence_id: chemical-groundings
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3732;https://www.genome.jp/entry/C06912;https://www.lipidmaps.org/databases/lmsd/LMPK04000014;https://files.rcsb.org/ligands/download/CTY.cif
  locator: Official identity, aliases, parent/role terms and exact structures
  accessed_at: '2026-10-21T13:24:10Z'
  support: supports
  summary: The methylated erythromycin identity and macrolide/glycoside structure
    fit the native parents and antibacterial role. KEGGD00276 is drug context; CAS81103-11-9
    is independently cross-attested. All19 aliases were read, including chemical names/abbreviations
    and ARO product names. Biaxin is separately confirmed as an FDA product name.
  snapshot_sha256: 5dc12c2346962f5253b8a4f196a07c1d45102758fe8281df9fbbca0cedff37e2
- evidence_id: patents
  kind: primary_source
  reference: https://patents.google.com/patent/US4331803A/en;https://patents.google.com/patent/EP0041355A1/en
  locator: Original disclosure, Example1 exact6-O-methylerythromycinA, TE-031 antibacterial
    experiment and separation from TE-032
  accessed_at: '2026-10-21T13:24:10Z'
  support: supports
  summary: Both source-linked patents describe6-O-methylerythromycinA and distinguish
    the6,11-dimethyl compound. Example1 supplies formula C38H69NO13 and M+747; TE-031
    names the parent in an agar-dilution assay. These documents support identity and
    experimental antibacterial context, not current clinical recommendations or patent
    legal status.
  snapshot_sha256: 010bf97e1872803434c1416ffb4b88236ccb0ac10acdc7d047f4b85de0a3dfbb
- evidence_id: adapter
  kind: database
  reference: iModulonDB m_tuberculosis/modulome; e_coli/precise1k; s_aureus/staph_precise108
  locator: Catalog then rrl and erm(37) queries before primary mechanism follow-up
  accessed_at: '2026-10-21T13:24:10Z'
  support: context_only
  summary: No iModulon components matched. The Mtuberculosis erm(37) query returned
    Rv1988; rrl queries returned no genes. The catalog lacks a matching Mchelonae
    dataset. These results are context only, with no negative biological inference,
    binding claim or clinical resistance transfer.
  snapshot_sha256: b86babdb4d73a757508c483a9d3507b3eb12916486161c64da09d987cab26afb
- evidence_id: binding-primary
  kind: primary_source
  reference: PMID:34935599;DOI:10.1080/22221751.2021.2022439;https://pmc.ncbi.nlm.nih.gov/articles/PMC8786254/
  locator: Complete original main XML, Materials/Methods, Results, Discussion and
    captions; supplement not inspected
  accessed_at: '2026-10-21T13:24:10Z'
  support: supports
  summary: The3.3Å cryo-EM structure uses purified M.tuberculosisH37Ra50S and Sigma
    clarithromycin, with solvent exchange from acetone stock. It directly locates
    clarithromycin in the23SrRNA nascent-peptide exit tunnel. PDB7F0D corroborates
    the structural deposition. Specific water-mediated dynamics, resistance explanations
    and therapeutic synergy are interpretations or prior-study context, not new whole-cell
    functional measurements.
  snapshot_sha256: 454d294183ec2f9b1fae2fb774bd1f0682e4ba31f16aee69ca755648dc64f357
- evidence_id: translation-primary
  kind: primary_source
  reference: PMID:9425251;DOI:10.1007/s002849900290;https://link.springer.com/article/10.1007/s002849900290
  locator: Complete original indexed and publisher abstracts;1998 paper full text
    not obtained
  accessed_at: '2026-10-21T13:24:10Z'
  support: supports
  summary: The S.aureus study measures growth, translation and50S assembly inhibition.
    Clarithromycin growth ID50 is0.075µg/mL and translation/assembly ID50 is0.15µg/mL;
    these are not MICs. This supports protein-synthesis inhibition while showing assembly
    effects also contribute. The accessible abstract does not isolate an elongation-only
    rate or independently certify starting material form.
  snapshot_sha256: c5812b67f40ccc2cff9da7bdad4b3d0b43c08cc442780abdab8b967e5fd0b26d
- evidence_id: graph
  kind: record_content
  reference: data/antibiotics/antibacterial/clarithromycin.yaml
  locator: All five causal nodes and four edges, two edge citations and explicit mapping
    qualifiers
  accessed_at: '2026-10-21T13:24:10Z'
  support: supports
  summary: The graph models drug binding at the50S/23SrRNA NPET, a bound state and
    decreased translation/protein synthesis. RNA and biological-process nodes are
    not protein examples. The ARO P-site identifier is explicitly related/coarse,
    not asserted exact NPET identity. Structural binding and measured cellular translation
    are distinguished; the selected papers do not measure every edge in a single system
    or exclude parallel50S assembly effects.
- evidence_id: card
  kind: database
  reference: https://card.mcmaster.ca/aro/0000065;https://card.mcmaster.ca/aro/3000757;44
    determinant entries in307-card-digest.json
  locator: All current target/determinant definitions, relation context and native
    source correspondence
  accessed_at: '2026-10-21T13:24:10Z'
  support: supports
  summary: Erm methylases, macrolide phosphotransferases, esterases, lmrP and species-specific23SrRNA
    mutation families are preserved as imported database assertions. Generic gene
    presence does not establish a strain phenotype or exact variant. The broad50S
    target remains PRIMARY_EVIDENCE_NEEDED; current CARD descriptions and citations
    are not silently upgraded to experimentally verified clarithromycin mechanisms.
  snapshot_sha256: dcb6e81c833fcb38c2ab67d840d836f1fe66842e5cd728960ddad8260356e83e
- evidence_id: erm55-original
  kind: primary_source
  reference: PMID:37347171;DOI:10.1128/jcm.00428-23;https://journals.asm.org/doi/full/10.1128/jcm.00428-23
  locator: Original abstract, Introduction, complete Methods, Tables1–2 and early
    Results; later Results/Discussion incompletely accessible
  accessed_at: '2026-10-21T13:24:10Z'
  support: supports
  summary: Commercial broth-microdilution plates, species identification and variant
    assays support matched clinical-isolate phenotypes and erm(55) genomic context.
    Resistant/susceptible paired isolates support association, without knockout/complementation
    or demonstrated horizontal transfer. Retrospective and prospective collections
    are distinct. Prepared antimicrobial form was not independently chemically characterized.
  snapshot_sha256: 941c5904917baa8b0a4ae0af686ed3e62038b1832a9240a117ee759397836069
- evidence_id: erm55-correction
  kind: primary_source
  reference: PMID:38572983;DOI:10.1128/jcm.00415-24;https://journals.asm.org/doi/10.1128/jcm.00415-24
  locator: Entire original erratum, corrected Table2 and footnotes as publisher text
  accessed_at: '2026-10-21T13:24:10Z'
  support: supports
  summary: 'All ten native resistant isolates match the corrected cells: six55P, two55T
    and two55C. The still-inconsistent heading must not override the cells. Several
    isolates become resistant only at extended readings. The susceptible20:68529 comparator
    and six intermediate isolates are correctly excluded. Native family-level UNKNOWN
    associations retain those distinctions and do not export numerical AST or allele-level
    causation.'
  snapshot_sha256: 941c5904917baa8b0a4ae0af686ed3e62038b1832a9240a117ee759397836069
- evidence_id: erm55-functional
  kind: primary_source
  reference: PMID:39817789;DOI:10.1128/spectrum.02397-24;https://pmc.ncbi.nlm.nih.gov/articles/PMC11878018/
  locator: Complete current original main XML and Tables1–3 independently read by
    source auditor; FigureS1 not inspected
  accessed_at: '2026-10-21T13:24:10Z'
  support: context_only
  summary: Heterologous55P/C/T expression in efflux-deficient E.coliM6394Δ9 raises
    clarithromycin MIC relative to vector control. This is causal functional resistance
    in that engineered host, distinct from the ten clinical-isolate associations.
    The authors did not measure ribosomal methylation; proposed residue effects remain
    hypotheses. Optional enrichment should preserve construct, host and assay context.
  snapshot_sha256: 74fecf5def73faf3a69974dfbb776ff35ab0abfd1f813b1e9785da01b57ee69e
- evidence_id: cryptic
  kind: validation
  reference: 307-membership-audit.json;data/raw/cryptic_activity.tsv;data/raw/cryptic_memberships.tsv.gz;data/raw/cryptic_isolates.tsv.gz
  locator: All six observations, membership payload inspection and complete maintained-source
    reconstruction
  accessed_at: '2026-10-21T13:24:10Z'
  support: supports
  summary: The six MTBC-qualified source groups preserve method/project/critical-concentration
    and R/S/U distinctions. MYCOTB0.5mg/L groups have6R,6S,451U; solid7H10 at3mg/L
    has52R,21S; one method-unspecified group has1R. All537 subjects/memberships/measurements,333
    unlinked subjects, counts, hashes and bytes reproduce exactly. Unknown is not
    susceptibility, and source criteria are not independently endorsed clinical breakpoints.
  snapshot_sha256: 916f8b420ff3121cfbd54f2d79838ba73982184a33d4e76b2892943b25048a46
- evidence_id: clinical
  kind: database
  reference: https://api.fda.gov/drug/drugsfda.json;https://gsrs.ncats.nih.gov/api/v1/substances/H1250JIK0A
  locator: Every native clinical row compared to current exact application/product
    and substance data
  accessed_at: '2026-10-21T13:24:10Z'
  support: supports
  summary: All45 assertions across27 applications match current ingredient, product
    name, sponsor, original approval date and marketing status. Discontinued products
    remain explicitly distinct from currently marketed prescription products. Current
    GSRSversion89 matches native chemistry; historicalversion83 remains dated provenance.
    Individual labels for every product were not independently reread.
  snapshot_sha256: 28dd0b49f5f7f6fa0b94efbf6f5770d70ec6b9251c084014dd67d2243b35b19a
- evidence_id: brand
  kind: database
  reference: https://api.fda.gov/drug/drugsfda.json?search=application_number:NDA050662
  locator: Original FDA current application/product response; native synonyms and
    clinical rows
  accessed_at: '2026-10-21T13:24:10Z'
  support: supports
  summary: NDA050662 identifies BIAXIN as the product brand with CLARITHROMYCIN as
    active ingredient. Native ARO alias Biaxin is typed EXACT_SYNONYM, conflating
    product naming with chemical synonymy despite available BRAND_NAME typing. Other
    ARO trade names need the same bounded classification check rather than blanket
    deletion.
  snapshot_sha256: 9780b8cc67ebf9e5a79c528b6f215ae79212d046f932e690b1eea586b83a073e
- evidence_id: adopted-review
  kind: database
  reference: PMID:7683018;DOI:10.1093/jac/31.suppl_c.1
  locator: Indexed abstract explicitly truncated at250words; publication type review
  accessed_at: '2026-10-21T13:24:10Z'
  support: context_only
  summary: The adopted macrolide overview supplies historical class context. It is
    secondary literature, and the truncated abstract is not represented as complete
    primary evidence or a compound-specific binding experiment.
  snapshot_sha256: 01f78a694e631431f0109d6e430601307ddedaa9a93e9ee8464cbd671095f2e4
- evidence_id: adopted-derivatives
  kind: primary_source
  reference: PMID:16387493;DOI:10.1016/j.bmcl.2005.12.033
  locator: Complete original indexed abstract; full parent-comparator table not inspected
  accessed_at: '2026-10-21T13:24:10Z'
  support: context_only
  summary: The adopted study tests new4-double-prime malonyl clarithromycin derivatives,
    including cell-free translation and50S binding. The accessible abstract does not
    establish a quantitative unmodified-parent row. Derivative properties are not
    transferred to native clarithromycin.
  snapshot_sha256: 01f78a694e631431f0109d6e430601307ddedaa9a93e9ee8464cbd671095f2e4
- evidence_id: access
  kind: search
  reference: 307-fetch-results.json;307-full-fetch-results.json;307-309-extra-results.json;307-erm55-source-report.json
  locator: Explicit source retrieval/read-depth ledger
  accessed_at: '2026-10-21T13:24:10Z'
  support: unknown
  summary: HMDB and DrugBank direct routes returned403; legacy LINCS resolver had
    certificate failure. The1998 PDF route returned publisher HTML rather than a PDF.2023/2024
    ASM text was partly available through the browser, while later retrieval was403;
    EuropePMC XML500 and PMC challenges did not supply their full texts. A university
    search hit was actually a nomenclature table, not the original study. No access
    obstacle was treated as contrary evidence.
  search_scope: Exact native identifiers and adopted primary leads; original binding/translation
    and erm55 correction follow-up,2026-10-21.
  snapshot_sha256: 941c5904917baa8b0a4ae0af686ed3e62038b1832a9240a117ee759397836069
assessments:
- assessment_id: identity
  area: identity
  topic: Exact chemistry, aliases and xrefs
  outcome: concern
  summary: The exact chemical representations agree across eight independent official
    encodings. One product alias has the wrong synonym type. Inaccessible legacy entries
    remain source-attested, not independently verified.
  target_ids:
  - CHEBI:3732
  evidence_ids:
  - native
  - chemistry
  - chemical-groundings
  - patents
  - brand
  - access
- assessment_id: mechanism
  area: evidence
  topic: Mode, target and causal graph
  outcome: supported
  summary: Primary structural binding and cellular translation evidence support the
    broad mechanism. Native qualifiers correctly distinguish the coarse database P-site
    relation from curated NPET context. Every edge was reviewed; full elongation-specific
    causal dissection is not established by the accessible1998 abstract.
  target_ids:
  - CHEBI:3732
  evidence_ids:
  - binding-primary
  - translation-primary
  - graph
  - card
  - adapter
- assessment_id: resistance
  area: evidence
  topic: All54 resistance assertions and corrected clinical table
  outcome: supported
  summary: The44 imported associations retain database depth. All ten curated clinical
    associations match corrected Table2 and remain observational rather than allele-causal.
    Later engineered-host functional evidence is separate optional enrichment.
  target_ids:
  - CHEBI:3732
  evidence_ids:
  - card
  - erm55-original
  - erm55-correction
  - erm55-functional
- assessment_id: activity
  area: evidence
  topic: CRyPTIC group and membership fidelity
  outcome: supported
  summary: Six source groups and all537 subject links are faithful and reproducible,
    with unknown phenotypes and source testing criteria preserved.
  target_ids:
  - CHEBI:3732
  evidence_ids:
  - cryptic
  - owners
- assessment_id: clinical
  area: evidence
  topic: Exact ingredient, historical approval and marketing
  outcome: supported
  summary: All45 current application/product comparisons pass; GSRS exact chemistry
    is stable across recorded versions. Product brands remain a distinct naming layer.
  target_ids:
  - CHEBI:3732
  evidence_ids:
  - clinical
  - brand
  - chemistry
- assessment_id: provenance
  area: provenance
  topic: Source ownership, adopted citation dispositions and immutable inputs
  outcome: supported
  summary: Every native field group and all adopted original/secondary leads were
    assessed at explicit read depths. Maintained inputs and curator additions are
    separated, source mints and history retained, all30 hashes unchanged.
  target_ids:
  - CHEBI:3732
  evidence_ids:
  - owners
  - adopted-review
  - adopted-derivatives
  - erm55-original
  - erm55-correction
- assessment_id: completeness
  area: completeness
  topic: Remaining evidence depth and optional enrichment
  outcome: unknown
  summary: Exact primary graph/association evidence is substantial but full scientific
    sign-off is limited by inaccessible legacy entries, selected primary access and
    unresolved elongation-specific endpoint detail. Missing optional primary mechanisms
    for all44 database associations are not automatically defects.
  target_ids:
  - CHEBI:3732
  evidence_ids:
  - access
  - translation-primary
  - card
  - erm55-functional
findings:
- finding_id: F1
  issue_key: clarithromycin-biaxin-brand-exact-synonym
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Type Biaxin as a brand name
  description: Biaxin is an FDA product name whose active ingredient is clarithromycin,
    but the native ARO synonym is EXACT_SYNONYM. Preserve the useful name with BRAND_NAME
    typing through maintained source handling. Review other ARO trade-name aliases
    individually; do not change correct chemical names or use brands to collapse preparations.
  target_ids:
  - CHEBI:3732
  field_paths:
  - synonyms
  evidence_ids:
  - native
  - brand
  - clinical
  rule_id: 'native-review-checklist: Identity and Clinical status'
  native_severity: minor
  normalization_reason: The exact molecule and product identity joins are correct;
    the confirmed defect is local alias typing.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source aliases
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained synonym classification or exclusion
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproduce source-aware synonym type
actions:
- action_id: A1
  description: Preserve Biaxin with product-name typing through the maintained synonym
    path.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:3732
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source aliases
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained synonym classification or exclusion
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproduce source-aware synonym type
  acceptance_checks:
  - Biaxin is BRAND_NAME rather than EXACT_SYNONYM; independently check other trade-name
    aliases before applying the same change.
  - Reseeding reproduces the change without altering exact chemistry, clinical product
    provenance or primary curator evidence; run focused schema/strict and source-reproduction
    gates.
limitations:
- The1998 original paper was available only as a complete indexed/publisher abstract.
  Its translation and50S assembly readouts are not an isolated elongation-rate measurement;
  no exact MIC is inferred.
- The2023 erm55 original was read through Methods, Tables1–2 and early Results, not
  the complete later Results/Discussion. The entire2024 correction was read as publisher
  text. The2025 functional main XML was inspected, but its supplementary FigureS1
  was not.
- The binding-study main XML was read in full; supplementary atom-contact/energy tables
  and deposited cryo-EM map were not independently reprocessed. No proposed water-dynamics
  or synergy model is elevated to a new causal experimental result.
- HMDB/DrugBank direct bodies and legacy LINCS entry remain unresolved. GSRSversion89
  corroborates chemistry while native datedversion83 remains historical. All45 FDA
  rows were compared, but individual generic product labels were not all read.
- All44 imported CARD relationships were checked at database/source-relation depth;
  their full underlying bibliographies were not exhaustively read. Native evidence
  qualifications remain appropriate.
- The adopted1993 overview abstract is explicitly truncated, and the2006 derivative
  paper was inspected at abstract depth. Their scope does not provide exact parent
  quantitative results.
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
