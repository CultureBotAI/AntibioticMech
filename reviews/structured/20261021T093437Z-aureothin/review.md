# Aureothin: one false positional synonym and qualified primary activity and target enrichment

- Review: 20261021T093437Z-aureothin
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:28:12Z
- Finished UTC: 2026-10-21T09:34:37Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The encoded neutral R-aureothin structure is consistent across ChEBI, PubChem, KEGG and the PDB chemical component. One imported EXACT_SYNONYM instead places the exocyclic double bond at oxolane position 5 rather than 4 and should be excluded or corrected through the maintained source policy. Exact antibacterial and antifungal activity is supported by inspected primary studies, with organism and assay limits. A separate primary study establishes binding to and inhibition of purified Thermus thermophilus respiratory complex I; that does not alone identify the whole-cell H. pylori or fungal killing mechanism. One major synonym finding and one informational enrichment follow-up.

## Scope And Provenance

Whole exact aureothin record: chemistry, three synonyms, all parents/roles/xrefs, biological definition, all ten adopted citation dispositions, source ownership and bounded exact-compound assay and mechanism evidence.

Selection: Queue 123, CHEBI:80024 at its locked path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:80024 | data/antibiotics/antibacterial/aureothin.yaml | generated | aureothin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:80024 | Actual focused command exited 0; chemistry agreement does not validate every textual synonym. |
| strict | passed | True | CHEBI:80024 | Actual focused command exited 0; chemistry agreement does not validate every textual synonym. |
| chemistry | passed | False | CHEBI:80024 | Actual focused command exited 0; chemistry agreement does not validate every textual synonym. |
| Authoritative full QC | failed | True | CHEBI:80024 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:80024 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:80024 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:80024 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:80024 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:80024 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:80024 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:80024 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:80024 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Encoded structure versus one false exact synonym

identity: concern. Targets: CHEBI:80024.

Stored R-aureothin structure and official structural xrefs agree; third exact synonym describes the exocyclic bond at the wrong ring position.

### Antibacterial and antifungal roles

evidence: supported. Targets: CHEBI:80024.

Exact primary antibacterial and antifungal results support inclusion, while organism, medium and endpoint limits must be preserved. Broad-spectrum activity is not asserted by the native record.

### Producer, insecticidal and antitumor wording

evidence: supported. Targets: CHEBI:80024.

Primary biosynthesis supports S. thioluteus as a producer and direct pesticidal tests support the insecticidal descriptor. Mammalian-cell assays support cytotoxic/antiproliferative context; no clinical antitumor efficacy is implied or established.

### Direct enzyme and whole-cell mechanism boundary

completeness: unknown. Targets: CHEBI:80024.

Purified bacterial complex-I binding/inhibition is a strong optional enrichment lead. It does not alone establish the causal mechanism for each antibacterial/fungal phenotype. Biosynthetic AurF/AurH are not drug targets.

### Resistance, clinical use and transcriptomics

completeness: unknown. Targets: CHEBI:80024.

No native claim in these optional fields is contradicted. No resistance mechanism, clinical efficacy or compound-induced transcriptomic dataset was established in the bounded review.

### Generated synonym and later primary annotation owners

ownership: supported. Targets: CHEBI:80024.

The adopted ChEBI assertion and source-specific synonym policy own the synonym correction. Later claim-level evidence belongs in the actual native record through authorized curation.

### Focused gates and source history

schema: supported. Targets: CHEBI:80024.

Focused checks pass; input state and three seed/reseed events are consistent. No status promotion proposed.

## Findings

### F1: An exact synonym moves the exocyclic double bond to a different ring carbon

major / open / confirmed; issue key: aureothin-wrong-ring-position-exact-synonym.

synonyms[2] uses (2R,5Z)-5-ylidene oxolan-2-yl, whereas the encoded native structure and independently concordant official names use (2R,4Z)-4-ylidene. This changes ring connectivity and is not an alternate numbering convention. The upstream ChEBI row contains the same error; retain the valid encoded structure and correct or suppress this single exact-synonym assertion.

### F2: Add qualified exact activity and bacterial complex-I evidence after checking remaining assay details

informational / open / confirmed; issue key: aureothin-qualified-primary-activity-target-enrichment.

Primary exact-compound antibacterial, antifungal and purified bacterial complex-I evidence is available, but the native seed has no claim-level annotation. Keep bacterial strain MICs separate from fungal inhibition zones, host-cell cytotoxicity and insect mortality. The enzyme experiment is direct target evidence in T. thermophilus and does not by itself close a whole-cell H. pylori or fungal causal chain.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained exact-synonym policy for CHEBI:80024 and regenerate the affected record through the normal source workflow.

- Exclude or correct the exact third synonym through the existing source-specific synonym policy after confirming ring position 4; do not globally remove the string from unrelated structures.
- Retain the correct first synonym, natural (+)-aureothin label, full key and encoded R/E/Z structure. Recheck all names after reseeding and ensure only intended fields change.
- Run focused schema/strict checks, terms/history/reference gates and source-regeneration checks. A chemistry-only pass is insufficient to verify the textual synonym.

### A2

Curate exact primary assays and the bounded complex-I target with their methods and limitations.

- For PMID 11079808 retain compound 2, H. pylori ATCC 43504 MIC 0.00078 micrograms/mL and the &gt;50 micrograms/mL limits for other tested strains. Record that the short paper omits medium, inoculum and incubation rather than inventing them; do not convert inhibition to killing.
- Retrieve 2010 assay supplementary methods before numerical fungal-zone enrichment; identify dose, strain, method and endpoint. Keep column 1 separate from derivatives and resolve figure resistance abbreviations before any resistance inference.
- For PMID 32811817 preserve purified T. thermophilus complex I, Q-site structural binding, assay conditions and PDB 6Q8W. Inspect supplementary Table 3 before recording IC50; do not infer the H. pylori or fungal killing mechanism from a separate enzyme system.
- Keep AurF/AurH and aur-cluster work under biosynthesis/producer evidence, not molecular drug targets or resistance. Separate natural S. thioluteus from heterologous hosts and related Streptomyces.
- Keep mammalian antiproliferative/cytotoxic and insect-mortality results distinct from antibacterial/fungal potency and clinical use. Preserve the historically different negative statement without treating it as a universal inactivity result.
- Use write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/aureothin.yaml for separately authorized curation, then run focused/shared gates; no automatic REVIEWED promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/aureothin.yaml; Entire YAML, including all three seed/reseed events. | supports | SEEDED exact ChEBI record with three exact synonyms, five chemical parents, two antimicrobial roles, three cross-references and a biological definition. No native molecular target, mode, quantitative activity, resistance, producer object, clinical indication, causal graph or transcriptomics dataset. Optional absence is not a required-field defect. |
| source | data/raw/chebi_antimicrobials.tsv; 123-raw.json, complete line 2043; conf/sources.yaml, extractor ChEBI row handling and seeder structure/name/role branches. | supports | The record faithfully copies the adopted source, including the problematic synonym and ten PMID leads. The extractor limits citation lists and does not turn them into claim-level primary evidence. ANTIBACTERIAL follows configured role priority while retaining antifungal. Existing conf/sources.yaml synonym_exclusions and seeder filtering provide a maintained record-specific correction path. All 13 captured inputs remain unchanged. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:80024; 123-chebi.html/txt, entire identity/ontology/registry/metabolite-source sections. | supports | Current ChEBI agrees with native formula, structures, source role terms and xrefs, including the same inconsistent third synonym. Parents CHEBI:131906, CHEBI:145408, CHEBI:26912, CHEBI:35716 and CHEBI:78840 denote 4-pyranones, ketene acetal, oxolanes, C-nitro and olefinic compounds. Roles CHEBI:33282/35718 are antibacterial/antifungal. Additional non-scope roles and a functional-parent relation are not missing required native fields. |
| chemistry | Independent RDKit, official PubChem CID 6569946 and KEGG C15689; 123-chemistry.json, 123-pubchem.json, 123-kegg.txt/mol; independent parsing of each structure. | supports | One neutral fragment C22H23NO6, one R centre and E/Z diene geometry yield GQKXCBCSVYJUMI-WACKOAQBSA-N. Formula, charge, reported masses and deterministic source mint agree. Independent PubChem SMILES and KEGG MOL yield the identical full key. KEGG explicitly names (2R,4Z)-4-ylidene oxolan-2-yl, supporting the correct first native synonym. CAS 2825-00-5 is corroborated through official crosswalks, not a direct registry audit. |
| synonym | Native exact synonym versus independent ring-connectivity audit; synonyms[2].synonym_text; 123-synonym-check.json; KEGG name and PDB HQW systematic name. | refutes | The third synonym states (2R,5Z)-5-ylidene oxolan-2-yl. Numbering the actual five-membered ring from oxygen 1 through the pyrone-substituted R carbon 2 places the exocyclic double bond at carbon 4; carbon 5 is a saturated methylene next to oxygen. A 5-ylidene name therefore denotes different connectivity, not an alternative numbering of this 2-substituted ring. Correct ChEBI IUPAC, KEGG and PDB systematic names use 4Z/4-ylidene. The stored structure itself is not implicated. |
| crosswalk | KEGG C15689; MetaCyc CPD-13144; PDB HQW; 123-kegg.txt/mol; 123-metacyc.html/txt; 123-PDB-HQW.json. | supports | KEGG structure and name independently agree. MetaCyc redirects to an account gate despite HTTP 200, so its underlying compound identity remains source-crosswalk-only; no account was created. PDB component HQW has the exact native full InChI/key, R/E/Z stereo-SMILES and the correct 4-ylidene name. Additional KEGG protein/pathway links are biosynthesis context, not adopted native antibacterial targets. |
| antibacterial | PMID:11079808; DOI:10.7164/antibiotics.53.844; 123-2000.pdf/text, all four pages; Figure 1 and Table 3 visually inspected on pages 845–846. | supports | Aureothin is compound 2, separate from isolated N-acetylaureothamine 1 and actinopyrone A 3. Table 3 reports aureothin MIC 0.00078 micrograms/mL for H. pylori ATCC 43504 and &gt;50 micrograms/mL for each of nine other tested bacterial strains. Figure 1 agrees with the native connectivity and stereochemical drawing. The short paper does not supply the antimicrobial assay medium, inoculum, incubation or endpoint definition. Its HeLa S3 IC50 of 10 micrograms/mL for compound 2 is a host-cell cytotoxicity result, not clinical antitumor efficacy. The Streptomyces netropsis fermentation and detailed new-compound elucidation concern compound 1 and cannot establish a new aureothin producer. |
| biosynthesis | PMID:14700630; PMID:15038705; PMID:15612710; PMID:17763486; Complete adopted abstracts and metadata in 123-epmc.json. | partial | PMID 14700630 / DOI 10.1016/j.chembiol.2003.11.009 identifies S. thioluteus HKI-227 and heterologous aur-cluster production, supporting a producer/biosynthesis lead. PMID 15038705 / DOI 10.1021/ja039328t reports labeling and AurF N-oxygenase genetics for p-nitrobenzoate formation. PMID 15612710 / DOI 10.1021/ja046104h reports AurH expression/inactivation and stereoselective furan-ring formation. PMID 17763486 / DOI 10.1002/cbic.200700309 distinguishes aureothin from S. thioluteus and neoaureothin from S. orinoci, with NorA cross-complementation. These enzymes synthesize compounds; they are not aureothin antimicrobial targets or resistance determinants. Full original methods were not retrieved. |
| other-adopted | All remaining adopted citation dispositions; 123-epmc.json, complete records and available abstracts. | partial | PMID 13174453 is the 1954 chemical study with no abstract; full text uninspected. PMID 18690656 / DOI 10.1002/cbic.200800301 is (+)-(R)-aureothin chemoenzymatic synthesis with no abstract; title is not a new assay. PMID 27213834 / DOI 10.1021/acs.joc.6b00878 describes racemic total synthesis; its racemate is not automatically the exact natural R material. PMID 17551211 / DOI 10.1038/ja.2007.41 isolates aureothin as compound 2 from Streptomyces sp. MM23, but the abstract HT1080 IC50 of 30 micromolar belongs to alloaureothin 1. PMID 18667785 / DOI 10.1038/ja.2008.52 includes aureothin in assays against T. brucei brucei GUTat 3.1 and T. b. rhodesiense STIB900, with MRC-5 cytotoxicity controls; abstract supplies no individual aureothin potency. These were all read as exact-subject leads, without transferring values. |
| antifungal | PMID:20662518; DOI:10.1021/ja102751h; PMC2925430; complete main text from official BioC in 123-2009-bioc.xml/text and 123-2009.html; Figure 10 visually inspected in 123-2010-Figure10.jpg. Scratch 2009 filenames do not indicate publication year, which is 2010. | partial | The original 2010 study explicitly compares aureothin 1 with distinct analogues. Figure 10 column 1 shows fungal inhibition zones, including 32 mm for C. albicans BMSY 212 and 38 mm for S. salmonicolor 549; these are diameters, not MICs. The paper separately reports mammalian-cell cytotoxic/antiproliferative endpoints. Exact dose and complete bioassay methods reside in supplementary information not successfully retrieved: the apparent PMC PDF was an HTML challenge and the official ACS route returned an empty response. Thus values are recognized as primary observations but not ready for an unqualified numerical annotation. Figure abbreviations MRSA/VRSA must not be treated as independently established resistance phenotypes, especially where its caption calls the latter E. faecalis. Biosynthetic engineering and analogue improvements are not direct drug-target evidence. |
| insecticide | DOI:10.1271/bbb1961.33.1790; 123-1969-correct.pdf and complete two-page text; publisher metadata also resolves DOI 10.1080/00021369.1969.10859541. | partial | The original 1969 study isolates crystalline aureothin from a soil Streptomyces culture using elemental analysis, melting point and IR comparison, then directly tests insect/mite mortality. The text reports 100 percent Pieris rapae mortality at 2.5 micrograms/insect and 100 percent mite mortality at 100 micrograms/mL. Its historical statement of no antimicrobial/antitumor activity is not an assay-matched refutation of later H. pylori and mammalian-cell observations. It does not demonstrate inhibition of a microbial respiratory complex. Exact absolute stereochemistry is not newly established by IR or melting point. |
| complexI | PMID:32811817; DOI:10.1038/s41467-020-17957-0; 123-2020.xml, exact ligand-binding Results, Fig. 4 caption, purification/activity/crystallization Methods and Data Availability; official PDB 6Q8W entry in 123-PDB-6Q8W.json. | partial | The study reports aureothin-bound T. thermophilus respiratory complex I and inhibitory activity of the purified enzyme. NADH oxidation is measured at 50 C with decylubiquinone as acceptor; aureothin co-crystallization/soaking uses 100 micromolar. Official 6Q8W metadata identifies the aureothin-bound complex at 3.4 angstrom resolution; the paper describes the Q-site interactions. This supports a bounded direct bacterial enzyme target lead, not proof of H. pylori killing through that target, a fungal mechanism, ROS induction or universal respiratory inhibition. The main text refers inhibitor IC50 values to supplementary Table 3, which was not retrieved; no numerical IC50 is asserted here. |
| adapter | iModulonDB applicability; Same-session successful 055-imodulondb-datasets-retry.txt inventory; whole native record and emerging biosynthesis/complex-I leads. | context_only | Native record has no gene/protein/pathway/response assertion. The exact biosynthesis producer S. thioluteus and enzyme organism T. thermophilus are not represented in the inspected inventory. Related Streptomyces or E. coli datasets were not substituted for those experiments. Lack of catalog coverage is not negative biological evidence. |
| search | CultureBotAI/AntibioticMech; 123-local-hits.txt and 123-maintained-search.txt; bounded exact-name, original-title and DOI searches. | context_only | Hidden- and ignored-inclusive searches locate the native row, record and readiness context, without a maintained exact-record primary addition or synonym override. Generated pages and historical reports are leads only. Two further ChEBI citation leads were inspected: PMID 770405 / DOI 10.7164/antibiotics.29.236 abstract identifies mycolutein as aureothin but is not full assay evidence; PMID 27559404 / DOI 10.3762/bjoc.12.148 is a biosynthesis review. A non-adopted NPAtlas result with a different ring connectivity was not used to replace the independently concordant native structure. |
| validation | Focused checks and initial input audit; 123-focused-results.json, focused logs, chemistry and initial inspect artifacts. | supports | Schema, strict and independent chemistry checks pass. All 13 maintained input hashes remain unchanged. Three seed/reseed events are consistent with SEEDED. No native records were edited; no paid access or contact occurred. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Exact identity/synonym, primary evidence, mechanism, producer, completeness and native ownership rules. | supports | A chemically different name must not be asserted as an exact synonym. Activity belongs to the tested compound and assay; biosynthesis proteins, purified-enzyme targets and whole-cell mechanism have distinct evidentiary scopes. Optional missing annotations are not automatically errors. |

## Limits And Additional Notes

- All ten adopted bibliographic records and every available original abstract were read. The 1954 chemical study and 2008 chemoenzymatic synthesis have no abstract; their full text was not inspected. Other adopted biosynthesis/synthesis/antitrypanosomal papers remain abstract-level except the complete 2000 antibacterial paper.
- The 2000 four-page primary paper was read completely and its structures/table visually inspected. It supplies strain MICs but omits detailed antimicrobial assay conditions. Raw spectra and original assay data were not independently audited.
- The 2010 main text and Figure 10 were inspected, but its bioassay supplement was not retrieved. Scratch files prefixed 123-2009 contain this 2010 article. Its detailed derivative chemistry does not constitute a full independent re-elucidation of natural aureothin.
- The 1969 pesticidal paper was read completely as extracted text; its tables were not separately visually audited, so only explicit narrative observations support the qualitative definition here. The 1961 original structure paper was not retrieved.
- The 2020 exact binding/assay Results, relevant full Methods, figure caption and data availability were inspected. Official 6Q8W metadata and HQW chemical descriptors were checked; electron-density maps and full supplementary IC50 table were not independently inspected. The SI retrieval failed with a DNS error.
- MetaCyc is account-gated and CAS is crosswalk-only. No exhaustive literature, resistance or producer census is claimed; no fungal or H. pylori causal killing chain is inferred from the purified Thermus enzyme.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T093437Z-aureothin
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Aureothin: one false positional synonym and qualified primary activity and
  target enrichment'
started_at: '2026-10-21T09:28:12Z'
finished_at: '2026-10-21T09:34:37Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the record. Exact target and input hashes were
    captured before assessment. Entire record, maintained ChEBI row, source config
    and relevant extraction/seeding code were inspected. All ten adopted citation
    records and available abstracts were read.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The encoded neutral R-aureothin structure is consistent across ChEBI, PubChem,
  KEGG and the PDB chemical component. One imported EXACT_SYNONYM instead places the
  exocyclic double bond at oxolane position 5 rather than 4 and should be excluded
  or corrected through the maintained source policy. Exact antibacterial and antifungal
  activity is supported by inspected primary studies, with organism and assay limits.
  A separate primary study establishes binding to and inhibition of purified Thermus
  thermophilus respiratory complex I; that does not alone identify the whole-cell
  H. pylori or fungal killing mechanism. One major synonym finding and one informational
  enrichment follow-up.
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
  - path: data/antibiotics/antibacterial/aureothin.yaml
    sha256: e0e17fb43a4b981b03e3939d183cee513644db8d9544fa2a13c6dab26f589a09
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
- target_id: CHEBI:80024
  path: data/antibiotics/antibacterial/aureothin.yaml
  label: aureothin
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
  description: 'Whole exact aureothin record: chemistry, three synonyms, all parents/roles/xrefs,
    biological definition, all ten adopted citation dispositions, source ownership
    and bounded exact-compound assay and mechanism evidence.'
  selection: Queue 123, CHEBI:80024 at its locked path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:80024
  exclusions:
  - target: Neoaureothin, alloaureothin, deoxyaureothin, N-acetylaureothamine, aureonitrile
      and synthetic analogues as exact equivalents
    reason: Distinct structures and experimental columns; their activities and targets
      cannot automatically transfer to aureothin.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused command exited 0; chemistry agreement does not validate
    every textual synonym.
  target_ids:
  - CHEBI:80024
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/aureothin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual focused command exited 0; chemistry agreement does not validate
    every textual synonym.
  target_ids:
  - CHEBI:80024
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/aureothin.yaml --out /private/tmp/am-review-session/123-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Actual focused command exited 0; chemistry agreement does not validate
    every textual synonym.
  target_ids:
  - CHEBI:80024
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache .venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 123
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
  - CHEBI:80024
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
  - CHEBI:80024
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
  - CHEBI:80024
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
  - CHEBI:80024
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
  - CHEBI:80024
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
  - CHEBI:80024
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
  - CHEBI:80024
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
  - CHEBI:80024
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
  - CHEBI:80024
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/aureothin.yaml
  locator: Entire YAML, including all three seed/reseed events.
  accessed_at: '2026-10-21T09:33:10Z'
  support: supports
  summary: SEEDED exact ChEBI record with three exact synonyms, five chemical parents,
    two antimicrobial roles, three cross-references and a biological definition. No
    native molecular target, mode, quantitative activity, resistance, producer object,
    clinical indication, causal graph or transcriptomics dataset. Optional absence
    is not a required-field defect.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: 123-raw.json, complete line 2043; conf/sources.yaml, extractor ChEBI row
    handling and seeder structure/name/role branches.
  accessed_at: '2026-10-21T09:33:10Z'
  support: supports
  summary: The record faithfully copies the adopted source, including the problematic
    synonym and ten PMID leads. The extractor limits citation lists and does not turn
    them into claim-level primary evidence. ANTIBACTERIAL follows configured role
    priority while retaining antifungal. Existing conf/sources.yaml synonym_exclusions
    and seeder filtering provide a maintained record-specific correction path. All
    13 captured inputs remain unchanged.
  snapshot_sha256: 485f7844f1747bf15c374633bc818d9b07f94b7b0447c0f600c040876e0d681a
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:80024
  locator: 123-chebi.html/txt, entire identity/ontology/registry/metabolite-source
    sections.
  accessed_at: '2026-10-21T09:33:10Z'
  support: supports
  summary: Current ChEBI agrees with native formula, structures, source role terms
    and xrefs, including the same inconsistent third synonym. Parents CHEBI:131906,
    CHEBI:145408, CHEBI:26912, CHEBI:35716 and CHEBI:78840 denote 4-pyranones, ketene
    acetal, oxolanes, C-nitro and olefinic compounds. Roles CHEBI:33282/35718 are
    antibacterial/antifungal. Additional non-scope roles and a functional-parent relation
    are not missing required native fields.
  snapshot_sha256: 51cafe15065a4d3f880a2062ccd73e96e06414d3326fd4c8fc26b2371e3985f5
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit, official PubChem CID 6569946 and KEGG C15689
  locator: 123-chemistry.json, 123-pubchem.json, 123-kegg.txt/mol; independent parsing
    of each structure.
  accessed_at: '2026-10-21T09:33:10Z'
  support: supports
  summary: One neutral fragment C22H23NO6, one R centre and E/Z diene geometry yield
    GQKXCBCSVYJUMI-WACKOAQBSA-N. Formula, charge, reported masses and deterministic
    source mint agree. Independent PubChem SMILES and KEGG MOL yield the identical
    full key. KEGG explicitly names (2R,4Z)-4-ylidene oxolan-2-yl, supporting the
    correct first native synonym. CAS 2825-00-5 is corroborated through official crosswalks,
    not a direct registry audit.
  snapshot_sha256: c9fd125b373b41021729c839c4a1f66742e191528f220800b6e1c734b72f2024
- evidence_id: synonym
  kind: validation
  reference: Native exact synonym versus independent ring-connectivity audit
  locator: synonyms[2].synonym_text; 123-synonym-check.json; KEGG name and PDB HQW
    systematic name.
  accessed_at: '2026-10-21T09:33:10Z'
  support: refutes
  summary: The third synonym states (2R,5Z)-5-ylidene oxolan-2-yl. Numbering the actual
    five-membered ring from oxygen 1 through the pyrone-substituted R carbon 2 places
    the exocyclic double bond at carbon 4; carbon 5 is a saturated methylene next
    to oxygen. A 5-ylidene name therefore denotes different connectivity, not an alternative
    numbering of this 2-substituted ring. Correct ChEBI IUPAC, KEGG and PDB systematic
    names use 4Z/4-ylidene. The stored structure itself is not implicated.
  snapshot_sha256: b6c520038e929ff2f89629be78334e16b37754613d0d22f4e8b6e0aaaefaf041
- evidence_id: crosswalk
  kind: database
  reference: KEGG C15689; MetaCyc CPD-13144; PDB HQW
  locator: 123-kegg.txt/mol; 123-metacyc.html/txt; 123-PDB-HQW.json.
  accessed_at: '2026-10-21T09:33:10Z'
  support: supports
  summary: KEGG structure and name independently agree. MetaCyc redirects to an account
    gate despite HTTP 200, so its underlying compound identity remains source-crosswalk-only;
    no account was created. PDB component HQW has the exact native full InChI/key,
    R/E/Z stereo-SMILES and the correct 4-ylidene name. Additional KEGG protein/pathway
    links are biosynthesis context, not adopted native antibacterial targets.
  snapshot_sha256: 24df5384cc33b8e810b516588c409bb49733db4b6d7e3c4332768d1c30083ee8
- evidence_id: antibacterial
  kind: primary_source
  reference: PMID:11079808; DOI:10.7164/antibiotics.53.844
  locator: 123-2000.pdf/text, all four pages; Figure 1 and Table 3 visually inspected
    on pages 845–846.
  accessed_at: '2026-10-21T09:33:10Z'
  support: supports
  summary: Aureothin is compound 2, separate from isolated N-acetylaureothamine 1
    and actinopyrone A 3. Table 3 reports aureothin MIC 0.00078 micrograms/mL for
    H. pylori ATCC 43504 and >50 micrograms/mL for each of nine other tested bacterial
    strains. Figure 1 agrees with the native connectivity and stereochemical drawing.
    The short paper does not supply the antimicrobial assay medium, inoculum, incubation
    or endpoint definition. Its HeLa S3 IC50 of 10 micrograms/mL for compound 2 is
    a host-cell cytotoxicity result, not clinical antitumor efficacy. The Streptomyces
    netropsis fermentation and detailed new-compound elucidation concern compound
    1 and cannot establish a new aureothin producer.
  snapshot_sha256: 927c1cae01d5fcd7e63728e463e3b15674e86990e3753295858b963d5c6e3f0b
- evidence_id: biosynthesis
  kind: primary_source
  reference: PMID:14700630; PMID:15038705; PMID:15612710; PMID:17763486
  locator: Complete adopted abstracts and metadata in 123-epmc.json.
  accessed_at: '2026-10-21T09:33:10Z'
  support: partial
  summary: PMID 14700630 / DOI 10.1016/j.chembiol.2003.11.009 identifies S. thioluteus
    HKI-227 and heterologous aur-cluster production, supporting a producer/biosynthesis
    lead. PMID 15038705 / DOI 10.1021/ja039328t reports labeling and AurF N-oxygenase
    genetics for p-nitrobenzoate formation. PMID 15612710 / DOI 10.1021/ja046104h
    reports AurH expression/inactivation and stereoselective furan-ring formation.
    PMID 17763486 / DOI 10.1002/cbic.200700309 distinguishes aureothin from S. thioluteus
    and neoaureothin from S. orinoci, with NorA cross-complementation. These enzymes
    synthesize compounds; they are not aureothin antimicrobial targets or resistance
    determinants. Full original methods were not retrieved.
  snapshot_sha256: 12beb6a001fbcef1d2e4d4b729bbb681f2fb2a2c8b15dbc6f2566de068ddfb8b
- evidence_id: other-adopted
  kind: primary_source
  reference: All remaining adopted citation dispositions
  locator: 123-epmc.json, complete records and available abstracts.
  accessed_at: '2026-10-21T09:33:10Z'
  support: partial
  summary: PMID 13174453 is the 1954 chemical study with no abstract; full text uninspected.
    PMID 18690656 / DOI 10.1002/cbic.200800301 is (+)-(R)-aureothin chemoenzymatic
    synthesis with no abstract; title is not a new assay. PMID 27213834 / DOI 10.1021/acs.joc.6b00878
    describes racemic total synthesis; its racemate is not automatically the exact
    natural R material. PMID 17551211 / DOI 10.1038/ja.2007.41 isolates aureothin
    as compound 2 from Streptomyces sp. MM23, but the abstract HT1080 IC50 of 30 micromolar
    belongs to alloaureothin 1. PMID 18667785 / DOI 10.1038/ja.2008.52 includes aureothin
    in assays against T. brucei brucei GUTat 3.1 and T. b. rhodesiense STIB900, with
    MRC-5 cytotoxicity controls; abstract supplies no individual aureothin potency.
    These were all read as exact-subject leads, without transferring values.
  snapshot_sha256: 12beb6a001fbcef1d2e4d4b729bbb681f2fb2a2c8b15dbc6f2566de068ddfb8b
- evidence_id: antifungal
  kind: primary_source
  reference: PMID:20662518; DOI:10.1021/ja102751h
  locator: PMC2925430; complete main text from official BioC in 123-2009-bioc.xml/text
    and 123-2009.html; Figure 10 visually inspected in 123-2010-Figure10.jpg. Scratch
    2009 filenames do not indicate publication year, which is 2010.
  accessed_at: '2026-10-21T09:33:10Z'
  support: partial
  summary: 'The original 2010 study explicitly compares aureothin 1 with distinct
    analogues. Figure 10 column 1 shows fungal inhibition zones, including 32 mm for
    C. albicans BMSY 212 and 38 mm for S. salmonicolor 549; these are diameters, not
    MICs. The paper separately reports mammalian-cell cytotoxic/antiproliferative
    endpoints. Exact dose and complete bioassay methods reside in supplementary information
    not successfully retrieved: the apparent PMC PDF was an HTML challenge and the
    official ACS route returned an empty response. Thus values are recognized as primary
    observations but not ready for an unqualified numerical annotation. Figure abbreviations
    MRSA/VRSA must not be treated as independently established resistance phenotypes,
    especially where its caption calls the latter E. faecalis. Biosynthetic engineering
    and analogue improvements are not direct drug-target evidence.'
  snapshot_sha256: 943e1260c8520a91c1f53b3f5ad7ac730a31ddd6f97c5f3e9d53a9d923acde00
- evidence_id: insecticide
  kind: primary_source
  reference: DOI:10.1271/bbb1961.33.1790
  locator: 123-1969-correct.pdf and complete two-page text; publisher metadata also
    resolves DOI 10.1080/00021369.1969.10859541.
  accessed_at: '2026-10-21T09:33:10Z'
  support: partial
  summary: The original 1969 study isolates crystalline aureothin from a soil Streptomyces
    culture using elemental analysis, melting point and IR comparison, then directly
    tests insect/mite mortality. The text reports 100 percent Pieris rapae mortality
    at 2.5 micrograms/insect and 100 percent mite mortality at 100 micrograms/mL.
    Its historical statement of no antimicrobial/antitumor activity is not an assay-matched
    refutation of later H. pylori and mammalian-cell observations. It does not demonstrate
    inhibition of a microbial respiratory complex. Exact absolute stereochemistry
    is not newly established by IR or melting point.
  snapshot_sha256: b64dd4049187ca22407feaadb4ecdc65d0c74691e621699f32d0ecde28628f5a
- evidence_id: complexI
  kind: primary_source
  reference: PMID:32811817; DOI:10.1038/s41467-020-17957-0
  locator: 123-2020.xml, exact ligand-binding Results, Fig. 4 caption, purification/activity/crystallization
    Methods and Data Availability; official PDB 6Q8W entry in 123-PDB-6Q8W.json.
  accessed_at: '2026-10-21T09:33:10Z'
  support: partial
  summary: The study reports aureothin-bound T. thermophilus respiratory complex I
    and inhibitory activity of the purified enzyme. NADH oxidation is measured at
    50 C with decylubiquinone as acceptor; aureothin co-crystallization/soaking uses
    100 micromolar. Official 6Q8W metadata identifies the aureothin-bound complex
    at 3.4 angstrom resolution; the paper describes the Q-site interactions. This
    supports a bounded direct bacterial enzyme target lead, not proof of H. pylori
    killing through that target, a fungal mechanism, ROS induction or universal respiratory
    inhibition. The main text refers inhibitor IC50 values to supplementary Table
    3, which was not retrieved; no numerical IC50 is asserted here.
  snapshot_sha256: 652da83d092168809424aa1d09a0798cd8f60fcd8ae53024a825b680c87d86e3
- evidence_id: adapter
  kind: database
  reference: iModulonDB applicability
  locator: Same-session successful 055-imodulondb-datasets-retry.txt inventory; whole
    native record and emerging biosynthesis/complex-I leads.
  accessed_at: '2026-10-21T09:33:10Z'
  support: context_only
  summary: Native record has no gene/protein/pathway/response assertion. The exact
    biosynthesis producer S. thioluteus and enzyme organism T. thermophilus are not
    represented in the inspected inventory. Related Streptomyces or E. coli datasets
    were not substituted for those experiments. Lack of catalog coverage is not negative
    biological evidence.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 123-local-hits.txt and 123-maintained-search.txt; bounded exact-name, original-title
    and DOI searches.
  accessed_at: '2026-10-21T09:33:10Z'
  support: context_only
  summary: 'Hidden- and ignored-inclusive searches locate the native row, record and
    readiness context, without a maintained exact-record primary addition or synonym
    override. Generated pages and historical reports are leads only. Two further ChEBI
    citation leads were inspected: PMID 770405 / DOI 10.7164/antibiotics.29.236 abstract
    identifies mycolutein as aureothin but is not full assay evidence; PMID 27559404
    / DOI 10.3762/bjoc.12.148 is a biosynthesis review. A non-adopted NPAtlas result
    with a different ring connectivity was not used to replace the independently concordant
    native structure.'
  search_scope: rg --no-ignore --hidden for identifier, name/slug and GQKXCBCSVYJUMI
    across batch013, then curation/conf/scripts/data/raw/src/reports/reviews; initial
    scan excludes .git and .venv. Official chemistry and all adopted citation records;
    bounded exact-name original activity/structure searches; free access only.
  snapshot_sha256: 9a352d5276a412a6808e447fe5f8b0d1d926e267a7bc3402604a7a9d5ebff2ed
- evidence_id: validation
  kind: validation
  reference: Focused checks and initial input audit
  locator: 123-focused-results.json, focused logs, chemistry and initial inspect artifacts.
  accessed_at: '2026-10-21T09:33:10Z'
  support: supports
  summary: Schema, strict and independent chemistry checks pass. All 13 maintained
    input hashes remain unchanged. Three seed/reseed events are consistent with SEEDED.
    No native records were edited; no paid access or contact occurred.
  snapshot_sha256: 76fc91b129855be80d076d698647529d4cc6b45e7fd913f2b57bbeaf7243239e
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Exact identity/synonym, primary evidence, mechanism, producer, completeness
    and native ownership rules.
  accessed_at: '2026-10-21T09:33:10Z'
  support: supports
  summary: A chemically different name must not be asserted as an exact synonym. Activity
    belongs to the tested compound and assay; biosynthesis proteins, purified-enzyme
    targets and whole-cell mechanism have distinct evidentiary scopes. Optional missing
    annotations are not automatically errors.
assessments:
- assessment_id: identity
  area: identity
  topic: Encoded structure versus one false exact synonym
  outcome: concern
  summary: Stored R-aureothin structure and official structural xrefs agree; third
    exact synonym describes the exocyclic bond at the wrong ring position.
  target_ids:
  - CHEBI:80024
  evidence_ids:
  - identity
  - chemistry
  - synonym
  - crosswalk
- assessment_id: activity
  area: evidence
  topic: Antibacterial and antifungal roles
  outcome: supported
  summary: Exact primary antibacterial and antifungal results support inclusion, while
    organism, medium and endpoint limits must be preserved. Broad-spectrum activity
    is not asserted by the native record.
  target_ids:
  - CHEBI:80024
  evidence_ids:
  - antibacterial
  - antifungal
- assessment_id: definition
  area: evidence
  topic: Producer, insecticidal and antitumor wording
  outcome: supported
  summary: Primary biosynthesis supports S. thioluteus as a producer and direct pesticidal
    tests support the insecticidal descriptor. Mammalian-cell assays support cytotoxic/antiproliferative
    context; no clinical antitumor efficacy is implied or established.
  target_ids:
  - CHEBI:80024
  evidence_ids:
  - biosynthesis
  - insecticide
  - antibacterial
  - antifungal
- assessment_id: mechanism
  area: completeness
  topic: Direct enzyme and whole-cell mechanism boundary
  outcome: unknown
  summary: Purified bacterial complex-I binding/inhibition is a strong optional enrichment
    lead. It does not alone establish the causal mechanism for each antibacterial/fungal
    phenotype. Biosynthetic AurF/AurH are not drug targets.
  target_ids:
  - CHEBI:80024
  evidence_ids:
  - complexI
  - biosynthesis
  - adapter
  - rubric
- assessment_id: optional
  area: completeness
  topic: Resistance, clinical use and transcriptomics
  outcome: unknown
  summary: No native claim in these optional fields is contradicted. No resistance
    mechanism, clinical efficacy or compound-induced transcriptomic dataset was established
    in the bounded review.
  target_ids:
  - CHEBI:80024
  evidence_ids:
  - record
  - other-adopted
  - adapter
- assessment_id: ownership
  area: ownership
  topic: Generated synonym and later primary annotation owners
  outcome: supported
  summary: The adopted ChEBI assertion and source-specific synonym policy own the
    synonym correction. Later claim-level evidence belongs in the actual native record
    through authorized curation.
  target_ids:
  - CHEBI:80024
  evidence_ids:
  - source
  - rubric
- assessment_id: gates
  area: schema
  topic: Focused gates and source history
  outcome: supported
  summary: Focused checks pass; input state and three seed/reseed events are consistent.
    No status promotion proposed.
  target_ids:
  - CHEBI:80024
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: aureothin-wrong-ring-position-exact-synonym
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: An exact synonym moves the exocyclic double bond to a different ring carbon
  description: synonyms[2] uses (2R,5Z)-5-ylidene oxolan-2-yl, whereas the encoded
    native structure and independently concordant official names use (2R,4Z)-4-ylidene.
    This changes ring connectivity and is not an alternate numbering convention. The
    upstream ChEBI row contains the same error; retain the valid encoded structure
    and correct or suppress this single exact-synonym assertion.
  target_ids:
  - CHEBI:80024
  field_paths:
  - synonyms[2].synonym_text
  - synonyms[2].synonym_type
  evidence_ids:
  - synonym
  - chemistry
  - identity
  - source
  - crosswalk
  - rubric
  rule_id: 'native-review-checklist: Exact chemical identity and synonym scope'
  native_severity: major false exact-identity assertion
  normalization_reason: A false structural synonym can misground name-based consumers
    even while the main structure and all deterministic gates pass. This does not
    make the entire record a wrong compound or require exclusion.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Record-specific synonym exclusion or correction policy
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated synonym filtering and reseeding
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted upstream synonym provenance; refresh only through maintained extraction
- finding_id: F2
  issue_key: aureothin-qualified-primary-activity-target-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Add qualified exact activity and bacterial complex-I evidence after checking
    remaining assay details
  description: Primary exact-compound antibacterial, antifungal and purified bacterial
    complex-I evidence is available, but the native seed has no claim-level annotation.
    Keep bacterial strain MICs separate from fungal inhibition zones, host-cell cytotoxicity
    and insect mortality. The enzyme experiment is direct target evidence in T. thermophilus
    and does not by itself close a whole-cell H. pylori or fungal causal chain.
  target_ids:
  - CHEBI:80024
  field_paths:
  - activity_spectrum
  - molecular_targets
  - mode_of_action
  - evidence
  - discussions
  evidence_ids:
  - antibacterial
  - antifungal
  - complexI
  - biosynthesis
  - rubric
  rule_id: 'native-review-checklist: Qualified primary evidence and optional completeness'
  native_severity: informational optional primary enrichment
  normalization_reason: The absent annotations are optional and the seeded classification
    is supported. Assay access limits and cross-system mechanism boundaries prevent
    unqualified automatic enrichment.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/aureothin.yaml
    role: Curator-owned qualified primary evidence, activity and target annotations
      through validated writer and history helper
actions:
- action_id: A1
  description: Correct the maintained exact-synonym policy for CHEBI:80024 and regenerate
    the affected record through the normal source workflow.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:80024
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Record-specific synonym exclusion or correction policy
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated synonym filtering and reseeding
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted upstream synonym provenance; refresh only through maintained extraction
  acceptance_checks:
  - Exclude or correct the exact third synonym through the existing source-specific
    synonym policy after confirming ring position 4; do not globally remove the string
    from unrelated structures.
  - Retain the correct first synonym, natural (+)-aureothin label, full key and encoded
    R/E/Z structure. Recheck all names after reseeding and ensure only intended fields
    change.
  - Run focused schema/strict checks, terms/history/reference gates and source-regeneration
    checks. A chemistry-only pass is insufficient to verify the textual synonym.
- action_id: A2
  description: Curate exact primary assays and the bounded complex-I target with their
    methods and limitations.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:80024
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/aureothin.yaml
    role: Curator-owned qualified primary evidence, activity and target annotations
      through validated writer and history helper
  acceptance_checks:
  - For PMID 11079808 retain compound 2, H. pylori ATCC 43504 MIC 0.00078 micrograms/mL
    and the >50 micrograms/mL limits for other tested strains. Record that the short
    paper omits medium, inoculum and incubation rather than inventing them; do not
    convert inhibition to killing.
  - Retrieve 2010 assay supplementary methods before numerical fungal-zone enrichment;
    identify dose, strain, method and endpoint. Keep column 1 separate from derivatives
    and resolve figure resistance abbreviations before any resistance inference.
  - For PMID 32811817 preserve purified T. thermophilus complex I, Q-site structural
    binding, assay conditions and PDB 6Q8W. Inspect supplementary Table 3 before recording
    IC50; do not infer the H. pylori or fungal killing mechanism from a separate enzyme
    system.
  - Keep AurF/AurH and aur-cluster work under biosynthesis/producer evidence, not
    molecular drug targets or resistance. Separate natural S. thioluteus from heterologous
    hosts and related Streptomyces.
  - Keep mammalian antiproliferative/cytotoxic and insect-mortality results distinct
    from antibacterial/fungal potency and clinical use. Preserve the historically
    different negative statement without treating it as a universal inactivity result.
  - Use write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/aureothin.yaml
    for separately authorized curation, then run focused/shared gates; no automatic
    REVIEWED promotion.
limitations:
- All ten adopted bibliographic records and every available original abstract were
  read. The 1954 chemical study and 2008 chemoenzymatic synthesis have no abstract;
  their full text was not inspected. Other adopted biosynthesis/synthesis/antitrypanosomal
  papers remain abstract-level except the complete 2000 antibacterial paper.
- The 2000 four-page primary paper was read completely and its structures/table visually
  inspected. It supplies strain MICs but omits detailed antimicrobial assay conditions.
  Raw spectra and original assay data were not independently audited.
- The 2010 main text and Figure 10 were inspected, but its bioassay supplement was
  not retrieved. Scratch files prefixed 123-2009 contain this 2010 article. Its detailed
  derivative chemistry does not constitute a full independent re-elucidation of natural
  aureothin.
- The 1969 pesticidal paper was read completely as extracted text; its tables were
  not separately visually audited, so only explicit narrative observations support
  the qualitative definition here. The 1961 original structure paper was not retrieved.
- The 2020 exact binding/assay Results, relevant full Methods, figure caption and
  data availability were inspected. Official 6Q8W metadata and HQW chemical descriptors
  were checked; electron-density maps and full supplementary IC50 table were not independently
  inspected. The SI retrieval failed with a DNS error.
- MetaCyc is account-gated and CAS is crosswalk-only. No exhaustive literature, resistance
  or producer census is claimed; no fungal or H. pylori causal killing chain is inferred
  from the purified Thermus enzyme.
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
