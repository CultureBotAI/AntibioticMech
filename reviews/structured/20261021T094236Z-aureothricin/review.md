# Aureothricin: qualify the unresolved RNA-polymerase mechanism and retain exact activity scope

- Review: 20261021T094236Z-aureothricin
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:33:25Z
- Finished UTC: 2026-10-21T09:42:36Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The neutral aureothricin identity and antimicrobial roles are supported. The source-derived RNA-polymerase note overstates certainty by saying that the mechanism is true: an inspected exact-compound primary study explicitly treats it as putative and unresolved. Its negative ssrS susceptibility result does not disprove every possible RNAP interaction. One major certainty/scope finding and one informational follow-up for qualified activity and producer evidence; no replacement mechanism is inferred from thiolutin or holomycin.

## Scope And Provenance

Whole exact aureothricin record: all names, structures, parents, roles and xrefs; biological definition; source-derived mechanism and target scope; all ten adopted citation dispositions; bounded primary activity, producer and response evidence.

Selection: Queue 124, CHEBI:156452 at its locked path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:156452 | data/antibiotics/antibacterial/aureothricin.yaml | generated | aureothricin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:156452 | Actual focused command exited 0. Deterministic validation does not establish mechanism truth. |
| strict | passed | True | CHEBI:156452 | Actual focused command exited 0. Deterministic validation does not establish mechanism truth. |
| chemistry | passed | False | CHEBI:156452 | Actual focused command exited 0. Deterministic validation does not establish mechanism truth. |
| Authoritative full QC | failed | True | CHEBI:156452 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:156452 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:156452 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:156452 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:156452 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:156452 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:156452 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:156452 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:156452 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral exact aureothricin and names

identity: supported. Targets: CHEBI:156452.

Structures, formula, charge, names and independent structural crosswalks agree. Historical source spelling does not warrant reassigning a producer species.

### Antibacterial and antifungal roles

evidence: supported. Targets: CHEBI:156452.

Original and modern exact-compound primary experiments support qualitative antibacterial/fungal inclusion. Potency varies by test organism and must remain assay-specific.

### Unresolved RNAP mechanism versus generated certainty

evidence: concern. Targets: CHEBI:156452.

ChEBI source provenance is faithful, but the assertion that the mechanism is true exceeds the inspected exact evidence. The 2022 primary study explicitly treats the mechanism as unclear; its negative genetic result is not proof of no possible RNAP action.

### Fermentation and producer definition

evidence: supported. Targets: CHEBI:156452.

Primary studies and abstracts support aureothricin/thiolutin co-production in multiple Streptomyces cultures; one adopted additional producer is Saccharothrix. The qualitative moderate-activity descriptor is assay-dependent, not a universal potency threshold.

### Exact activity, producer, resistance, host response and datasets

completeness: unknown. Targets: CHEBI:156452.

Activity and producer objects are useful optional follow-ups. No exact aureothricin resistance mechanism, clinical indication or exposure transcriptomics was established. Genetic RNA-seq and mixed-fermentation plant responses are not aureothricin exposure datasets.

### Source-derived mechanism and optional primary annotations

ownership: supported. Targets: CHEBI:156452.

The source mapping and generated explanatory text own the certainty correction. The actual native record owns separately authorized primary curation. No global deletion of the RNAP role mapping is justified by this record alone.

### Focused checks and history

schema: supported. Targets: CHEBI:156452.

Focused checks pass; source/record hashes and seed history are consistent. No REVIEWED promotion is proposed.

## Findings

### F1: Generated mechanism wording asserts certainty that the exact-compound evidence does not establish

major / open / confirmed; issue key: aureothricin-rnap-mechanism-certainty.

The source-derived note says the mechanism is true, although the exact aureothricin primary study PMID 35389235 explicitly treats RNAP inhibition as putative and the mechanism as unclear. Its ssrS experiment supports a limited susceptibility observation, not direct RNAP inhibition or its universal exclusion. Retain honest ChEBI provenance while qualifying the unresolved biological claim. Thiolutin and holomycin experiments cannot supply the missing exact mechanism.

### F2: Qualified exact activity and producer evidence can enrich the seed

informational / open / confirmed; issue key: aureothricin-qualified-primary-activity-producer-enrichment.

Modern primary isolation and separate pure-compound assays provide activity and producer evidence. Preserve exact AUR versus thiolutin columns, organism and protocol limits, and the distinction between pure compound, mixtures and culture filtrate. Do not turn plant defense responses, biosynthesis proteins or ssrS experiments into direct antibacterial targets or resistance claims.

## Recommended Actions And Acceptance Checks

### A1

Qualify the source-derived RNA-polymerase claim through maintained generation policy.

- Replace the assertion of demonstrated truth with accurate source attribution and the unresolved exact-compound mechanism. Preserve the ChEBI role as provenance; do not imply that PMID 35389235 disproves every RNAP interaction.
- Determine whether the mode should remain explicitly source-derived with qualification or be withheld pending exact primary evidence, using maintained compound-specific policy. Do not globally delete CHEBI:37416 mapping for other validated compounds.
- If HOST_SHARED_TARGET remains, describe it as the scope of the hypothesized enzyme family, not established host inhibition or selectivity for aureothricin. Do not substitute thiolutin zinc-chelation/Rpn11 results as a proven AUR mechanism.
- Regenerate through the maintained source workflow, inspect the exact diff and run focused schema/strict plus required shared source/history/reference gates.

### A2

Curate exact activity and fermentation evidence with remaining protocol limits.

- Use PMID 38183485 SYF1/aureothricin and the separate compound columns. Resolve supplemental strain/method details and the referenced broth-dilution protocol before numerical annotation; preserve MIC units and the &gt;200 limit, and distinguish fungi from oomycetes.
- Represent Streptomyces sp. JCK-8055 as the demonstrated cultured producer without assigning it to a nearest named species. Keep Saccharothrix algeriensis NRRL B-24137 distinct from Streptomyces and inspect original methods before precise producer/biosynthesis additions.
- Keep in planta two-antibiotic mixtures, filtrate, producer preparations and host PR-gene responses separate from purified aureothricin. Do not infer pure-compound disease control, immune pathways or clinical use.
- Keep the HG003 ssrS genotype comparison and sub-MIC spot assay distinct from direct enzyme inhibition, resistance mechanisms and aureothricin-induced RNA-seq.
- Use write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/aureothricin.yaml for separately authorized curation, then focused/shared gates. No automatic status promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/aureothricin.yaml; Entire YAML and all three seed/reseed events. | supports | SEEDED exact record with six exact names, two parents, three antimicrobial roles and three xrefs. The mode and note are source-derived, with HOST_SHARED_TARGET. No native molecular target object, quantitative activity, producer object, resistance, clinical indication, causal graph or transcriptomics dataset; these optional absences are not required-field errors. |
| source | data/raw/chebi_antimicrobials.tsv; 124-raw.json complete line 2768; conf/sources.yaml role mapping at lines 340 and 472; scripts/seed_from_sources.py mode_of_action_from_roles lines 1376–1455 and related name/structure handling. | supports | The native record faithfully reflects the adopted row and deterministic mapping of CHEBI:37416 to NUCLEIC_ACID_SYNTHESIS_INHIBITION and HOST_SHARED_TARGET. The stronger sentence that the mechanism is true comes from the generated note, not a compound-specific curator assessment. Extracted citation leads are not claim-level primary evidence. All 13 captured maintained inputs remain unchanged. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:156452; 124-chebi.html/txt, full identity, ontology, cross-reference and source sections. | supports | Current ChEBI agrees with all six names, structures, formula and xrefs. CHEBI:140325 is secondary carboxamide and CHEBI:156449 dithiolopyrrolone antibiotic; roles CHEBI:33281, CHEBI:33282 and CHEBI:35718 denote antimicrobial, antibacterial and antifungal roles. ChEBI also asserts CHEBI:37416, an RNA-polymerase inhibitor role. That accurately explains source provenance but is not independent primary validation of the exact mechanism. |
| chemistry | Independent RDKit; official PubChem CID 68460; KNApSAcK C00018653; 124-chemistry.json, 124-pubchem.json and 124-knapsack.html/txt. | supports | Native SMILES and InChI independently parse to one neutral C9H10N2O2S2 fragment, full key UGZYFXMSMFMTSM-UHFFFAOYSA-N, no stereocentres, and matching masses. Source mint agrees. PubChem structure and KNApSAcK formula, structure and full key independently match. All six native names describe the propanoyl pyrrothine rather than the acetyl thiolutin. CAS 574-95-8 is corroborated through official crosswalks, not a direct registry audit. |
| xref | KNApSAcK C00018653; MetaCyc CPD-17938; 124-knapsack.html/txt and 124-metacyc.html/txt. | partial | KNApSAcK exact structure agrees. Its predicted biosynthetic-category label is not an experimentally demonstrated pathway. MetaCyc returned an account gate despite HTTP 200, so underlying compound identity remains source-crosswalk-only; no account was created. |
| original | DOI:10.7883/yoken1948.1.512; 124-primary1948-correct.pdf and complete six-page extracted text. | partial | The original isolation study obtains crystalline aureothricin from Streptomyces sp. 26A, a 1947 Mitaka soil isolate. It tests bacteriostasis on nutrient agar, adding compound initially dissolved in acetone, streaking broth cultures and incubating 24 hours at 37 C. Narrative reports inhibition of Gram-positive and Gram-negative organisms. Historical table cells were not visually audited, so no exact dilution or MIC is adopted here. Similarity to named species does not assign strain 26A to them; later exact structures corroborate the modern chemical identity. |
| primary2024 | PMID:38183485; DOI:10.1007/s00253-023-12874-w; 124-primary2024.html/txt; relevant complete Methods, Results and Discussion; Figure 2 visually inspected in 124-2024-Figure2.webp. | partial | Aureothricin is purified SYF1, separate from thiolutin SYF2, from cultured Streptomyces sp. JCK-8055. HPLC, mass and proton NMR distinguish the propionamide and acetamide; Figure 2a matches the native aureothricin connectivity. Table 1 separately reports aureothricin MICs of 1.56 +/- 0 micrograms/mL against E. amylovora FB302, 4.16 +/- 1.48 against TS3128 and 25 +/- 0 against R. solanacearum SL341. Table 2 reports fungal inhibition including F. graminearum at 50 micrograms/mL, while F. oxysporum f. sp. cucumerinum is &gt;200. Oomycetes in the same table are not fungi. Pure-compound broth-dilution methods refer to a prior protocol; the detailed culture-filtrate protocol must not be silently assigned to every pure-compound fungal assay. Supplementary strain/method details were not independently inspected. |
| producer2024 | PMID:38183485; DOI:10.1007/s00253-023-12874-w; 124-primary2024.html/txt, isolation, fermentation, structural analysis and in planta Methods/Results/Discussion. | supports | The pepper-root endophytic isolate JCK-8055 produces aureothricin in laboratory culture; the authors retain Streptomyces sp. despite its nearest taxonomic relatives. TSB cultivation at 28 C for seven days yields both antibiotics. In planta experiments use a two-antibiotic SYF mixture, culture filtrate or producer preparations, not purified aureothricin alone. Host PR-gene responses and proposed SA/JA defense mechanisms therefore do not establish an aureothricin-specific host pathway, transcriptomic dataset or microbial target. The authors explicitly call for further work on the metabolites' modes of action. |
| rnap | PMID:35389235; DOI:10.1128/aac.02435-21; 124-primary2022.html/txt, exact-compound Results, complete Methods and Discussion; Figure 3 visually inspected in 124-2022-Figure3.jpg. | partial | The study explicitly calls aureothricin a putative RNAP inhibitor with an unclear mechanism. S. aureus HG003 and its ssrS deletion/complementation strains show no aureothricin hypersusceptibility attributable to loss of 6S RNA. Figure 3A uses BHI plus aureothricin 1.25 mg/L; the spot-test method uses serial dilution and sub-MIC exposure. The authors suggest that aureothricin does not bind the RNAP DNA interface. This is an indirect, site-limited inference, not a demonstration that aureothricin cannot inhibit RNAP anywhere. Purified RNAP/6S-RNA binding experiments do not directly assay aureothricin enzyme inhibition. The study's RNA-seq compares genetic backgrounds, not aureothricin exposure. |
| response2017 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5792653/; 124-primary2017-bioc.xml/txt, exact aureothricin paragraphs and relevant RNA-polymerase/target assay Methods. | partial | The thiolutin study reports accumulation of ubiquitylated proteins after aureothricin treatment in N. crassa, referring to a supplementary panel. Its purified polymerase, zinc-chelation and detailed JAMM/Rpn11 enzyme experiments concern thiolutin. Those results must not be rewritten as direct aureothricin Rpn11 binding/inhibition, zinc chelation or a proven bacterial killing mechanism. The aureothricin supplementary image and dose were not independently audited. |
| producer-adopted | PMID:1171186; PMID:20507156; PMID:2262169; 124-epmc.json; 124-primary1975.pdf, page 1 English abstract visually inspected in 124-primary1975-p1.png. | partial | PMID 1171186 / DOI 10.1248/yakushi1947.95.3_347 reports labeled propionate incorporation into aureothricin's propionamide after feeding Streptomyces luteoreticuli; only the English abstract was inspected, not the full Japanese experimental text. PMID 20507156 / DOI 10.1021/np900808u isolates aureothricin alongside distinct derivatives from Saccharothrix algeriensis NRRL B-24137 and reports moderate antimicrobial activity, without individual potencies in the abstract. Saccharothrix is not Streptomyces. PMID 2262169 / DOI 10.1007/bf02821279 reports methionine/ethionine regulation of thiolutin and aureothricin production in S. kasugaensis. These support producer/biosynthesis context, not antimicrobial molecular targets. |
| producer2016 | PMID:27018252; DOI:10.1016/j.bbrc.2016.03.105; 124-leads-epmc.json, complete original abstract. | partial | The aut-cluster study reports aureothricin and thiolutin production by Streptomyces thioluteus DSM 40027 with heterologous expression and in-frame deletion evidence. It supports a producer and biosynthesis lead. Biosynthetic genes and engineered HlmK are not aureothricin antimicrobial targets or demonstrated resistance mechanisms. Full methods were not inspected. |
| host-adopted | PMID:11433393; DOI:10.1002/ijc.1321; 124-epmc.json, complete abstract. | context_only | The HUVEC screen includes aureothricin, thioaurin and thiolutin. The 0.83 micromolar adhesion IC50, paxillin degradation and in vivo angiogenesis results in the abstract are explicitly thiolutin results and cannot be assigned to aureothricin or interpreted as aureothricin clinical efficacy. |
| historical-adopted | PMID:13084502; PMID:13096448; PMID:14275485; 124-epmc.json, complete bibliographic records; no abstracts returned. | unknown | PMID 13084502 concerns a yellow crystalline antibiotic identified with aureothricin from Streptomyces 39a; full taxonomic and identity evidence was not inspected. PMID 13096448 concerns a crystalline toxic substance from an aureothricin-producing culture; its title alone does not identify that toxic substance as aureothricin. PMID 14275485 concerns X-ray powder identification of thiolutin and aureothricin after chromatography. These remain unverified historical leads and supply no new exact potency or target assertion here. |
| reviews-adopted | PMID:24141227; PMID:24323287; PMID:24835149; 124-epmc.json, complete abstracts; 124-review2014-bioc.xml/txt, exact identity and complete section 4.1 mechanism paragraphs. | context_only | All three are secondary reviews used as leads. DOI 10.3390/md11103970 is a class isolation/synthesis/biosynthesis review; its holomycin resistance examples are not aureothricin results. DOI 10.1007/s00253-013-5410-z concerns holomycin, including hlm genetics and self-protection. DOI 10.1039/c3np70106a reviews dithiolopyrrolones and documents thiolutin/holomycin experiments and mechanism uncertainty; inspected mechanism paragraphs do not provide an exact aureothricin RNAP assay. None establishes an aureothricin-specific resistance or clinical claim. |
| adapter | iModulonDB structured cross-checks; 055-imodulondb-datasets-retry.txt successful inventory; 124-imodulondb-rnap.txt and 124-imodulondb-ssrS.txt successful searches. | context_only | Before open-ended mechanism research, the covered e_coli/precise_mg1655 RNA polymerase query returned ten gene matches including rpoA b3295 and rpoC b3988, but no iModulon. This is generic protein-name context, not evidence that E. coli is the native target organism or that aureothricin binds those proteins. A later s_aureus/staph_precise108 ssrS query returned no gene or module hit; that does not negate the HG003 experiment or prove catalog equivalence. S. thioluteus and N. crassa were not covered by the inspected inventory. |
| adapter-command | Structured adapter commands; Actual successful local runner and query invocations. | context_only | env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1 uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb --timeout 15 search --organism e_coli --dataset precise_mg1655 --query RNA\ polymerase; second query uses --organism s_aureus --dataset staph_precise108 --query ssrS. Both commands exited 0. No module hit warranted a summarize call. |
| search | CultureBotAI/AntibioticMech; 124-local-hits.txt and 124-maintained-search.txt; exact-name, DOI and original-title literature checks. | context_only | Hidden- and ignored-inclusive local searches locate the seed and source context but no maintained exact primary annotation or source-specific mechanism correction. Generated pages and historical reports were leads only. Bounded exact-compound literature research supports activity and producer leads but leaves molecular mechanism unresolved; this is not an exhaustive proof of absence. |
| validation | Focused schema, strict and chemistry checks; 124-focused-results.json and associated logs; initial input audit. | supports | All three actual focused commands exited 0. All 13 initial source/target hashes remain unchanged. History is three seed/reseed events, consistent with SEEDED. No native record edits occurred. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Exact identity, evidence placement, mechanism, activity, producer and native ownership rules. | supports | A source role may establish provenance without establishing exact-compound mechanism certainty. Keep related molecules, mixture effects, biosynthetic enzymes, genetic susceptibility, direct inhibition and host responses at their measured scopes. Missing optional annotation is not inherently an error. |

## Limits And Additional Notes

- All 13 captured maintained input hashes remain unchanged.
- All ten adopted bibliographic records and every available abstract were read. PMID 13084502, 13096448 and 14275485 have no inspected full text or abstract. The 1975 free paper was inspected only through its page-1 English abstract; the Japanese full methods were not independently translated. The 2010 ACS full text was inaccessible; its individual potency and methods remain unverified.
- The 1948 six-page extracted text was read completely, but historical table cells were not visually audited. No numerical historical MIC is curated from it.
- The 2022 exact aureothricin Results, complete Methods and Discussion, and Figure 3 were inspected. It is an indirect genetic susceptibility experiment; no exhaustive review of every historical RNAP experiment is claimed.
- The 2024 relevant complete Methods, Results and Discussion and structural Figure 2 were inspected. Raw spectra, supplement and referenced detailed pure-compound assay protocol were not independently audited. In planta efficacy and host-gene responses use mixtures or producer material.
- The 2017 exact aureothricin paragraphs and relevant polymerase/target Methods were inspected, not every supplementary experiment. The exact AUR supplemental protein-response panel was not independently viewed; no quantitative response or direct JAMM inhibition is asserted.
- MetaCyc is account-gated; CAS is crosswalk-only. Structured adapter matches are gene context, not target validation, and absent catalog coverage is not biological evidence. No exhaustive literature, resistance or producer census is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T094236Z-aureothricin
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Aureothricin: qualify the unresolved RNA-polymerase mechanism and retain exact
  activity scope'
started_at: '2026-10-21T09:33:25Z'
finished_at: '2026-10-21T09:42:36Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the record. Captured exact target and source
    hashes before assessment, then read the entire record, maintained row, config
    and relevant extractor/seeder code. Inspected all ten adopted citation records
    and available abstracts, official chemistry crosswalks and additional primary
    experiments.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'The neutral aureothricin identity and antimicrobial roles are supported.
  The source-derived RNA-polymerase note overstates certainty by saying that the mechanism
  is true: an inspected exact-compound primary study explicitly treats it as putative
  and unresolved. Its negative ssrS susceptibility result does not disprove every
  possible RNAP interaction. One major certainty/scope finding and one informational
  follow-up for qualified activity and producer evidence; no replacement mechanism
  is inferred from thiolutin or holomycin.'
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
  - path: data/antibiotics/antibacterial/aureothricin.yaml
    sha256: 03e5951ad48f132dc2bf2137f29d19a45ee24beb11932d66e8a143c4fe329d36
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
- target_id: CHEBI:156452
  path: data/antibiotics/antibacterial/aureothricin.yaml
  label: aureothricin
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
  description: 'Whole exact aureothricin record: all names, structures, parents, roles
    and xrefs; biological definition; source-derived mechanism and target scope; all
    ten adopted citation dispositions; bounded primary activity, producer and response
    evidence.'
  selection: Queue 124, CHEBI:156452 at its locked path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:156452
  exclusions:
  - target: Thiolutin, holomycin, aureothin, thioaurin and other dithiolopyrrolone
      analogues as exact equivalents
    reason: Different structures. Shared scaffold, fermentation or paper inclusion
      does not transfer mechanisms, potency or self-resistance.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused command exited 0. Deterministic validation does not establish
    mechanism truth.
  target_ids:
  - CHEBI:156452
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/aureothricin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual focused command exited 0. Deterministic validation does not establish
    mechanism truth.
  target_ids:
  - CHEBI:156452
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/aureothricin.yaml --out /private/tmp/am-review-session/124-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Actual focused command exited 0. Deterministic validation does not establish
    mechanism truth.
  target_ids:
  - CHEBI:156452
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache .venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 124
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
  - CHEBI:156452
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
  - CHEBI:156452
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
  - CHEBI:156452
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
  - CHEBI:156452
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
  - CHEBI:156452
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
  - CHEBI:156452
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
  - CHEBI:156452
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
  - CHEBI:156452
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
  - CHEBI:156452
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/aureothricin.yaml
  locator: Entire YAML and all three seed/reseed events.
  accessed_at: '2026-10-21T09:40:24Z'
  support: supports
  summary: SEEDED exact record with six exact names, two parents, three antimicrobial
    roles and three xrefs. The mode and note are source-derived, with HOST_SHARED_TARGET.
    No native molecular target object, quantitative activity, producer object, resistance,
    clinical indication, causal graph or transcriptomics dataset; these optional absences
    are not required-field errors.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: 124-raw.json complete line 2768; conf/sources.yaml role mapping at lines
    340 and 472; scripts/seed_from_sources.py mode_of_action_from_roles lines 1376–1455
    and related name/structure handling.
  accessed_at: '2026-10-21T09:40:24Z'
  support: supports
  summary: The native record faithfully reflects the adopted row and deterministic
    mapping of CHEBI:37416 to NUCLEIC_ACID_SYNTHESIS_INHIBITION and HOST_SHARED_TARGET.
    The stronger sentence that the mechanism is true comes from the generated note,
    not a compound-specific curator assessment. Extracted citation leads are not claim-level
    primary evidence. All 13 captured maintained inputs remain unchanged.
  snapshot_sha256: 8779526678793b4ff7938aa6ea6e5aff6665e81fb12ab2a699d5177517a0d84c
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:156452
  locator: 124-chebi.html/txt, full identity, ontology, cross-reference and source
    sections.
  accessed_at: '2026-10-21T09:40:24Z'
  support: supports
  summary: Current ChEBI agrees with all six names, structures, formula and xrefs.
    CHEBI:140325 is secondary carboxamide and CHEBI:156449 dithiolopyrrolone antibiotic;
    roles CHEBI:33281, CHEBI:33282 and CHEBI:35718 denote antimicrobial, antibacterial
    and antifungal roles. ChEBI also asserts CHEBI:37416, an RNA-polymerase inhibitor
    role. That accurately explains source provenance but is not independent primary
    validation of the exact mechanism.
  snapshot_sha256: 4cf380923ea1b135dd9f78ae682402a4febcdbe7ab04f2bffcdcc4998aac0856
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit; official PubChem CID 68460; KNApSAcK C00018653
  locator: 124-chemistry.json, 124-pubchem.json and 124-knapsack.html/txt.
  accessed_at: '2026-10-21T09:40:24Z'
  support: supports
  summary: Native SMILES and InChI independently parse to one neutral C9H10N2O2S2
    fragment, full key UGZYFXMSMFMTSM-UHFFFAOYSA-N, no stereocentres, and matching
    masses. Source mint agrees. PubChem structure and KNApSAcK formula, structure
    and full key independently match. All six native names describe the propanoyl
    pyrrothine rather than the acetyl thiolutin. CAS 574-95-8 is corroborated through
    official crosswalks, not a direct registry audit.
  snapshot_sha256: 2eccee4a4702fb08ff226b4b345b817aca698d43bc712c2982c98188cb7babac
- evidence_id: xref
  kind: database
  reference: KNApSAcK C00018653; MetaCyc CPD-17938
  locator: 124-knapsack.html/txt and 124-metacyc.html/txt.
  accessed_at: '2026-10-21T09:40:24Z'
  support: partial
  summary: KNApSAcK exact structure agrees. Its predicted biosynthetic-category label
    is not an experimentally demonstrated pathway. MetaCyc returned an account gate
    despite HTTP 200, so underlying compound identity remains source-crosswalk-only;
    no account was created.
  snapshot_sha256: c0b171ec86b93c0ddf41c31b25a820a4c1be5e488024438c3c2c6e76515ca0b8
- evidence_id: original
  kind: primary_source
  reference: DOI:10.7883/yoken1948.1.512
  locator: 124-primary1948-correct.pdf and complete six-page extracted text.
  accessed_at: '2026-10-21T09:40:24Z'
  support: partial
  summary: The original isolation study obtains crystalline aureothricin from Streptomyces
    sp. 26A, a 1947 Mitaka soil isolate. It tests bacteriostasis on nutrient agar,
    adding compound initially dissolved in acetone, streaking broth cultures and incubating
    24 hours at 37 C. Narrative reports inhibition of Gram-positive and Gram-negative
    organisms. Historical table cells were not visually audited, so no exact dilution
    or MIC is adopted here. Similarity to named species does not assign strain 26A
    to them; later exact structures corroborate the modern chemical identity.
  snapshot_sha256: ea20f6410ede8f98b72c02afd61e4dfbd619e7244fce18555be6a491d6fdfd72
- evidence_id: primary2024
  kind: primary_source
  reference: PMID:38183485; DOI:10.1007/s00253-023-12874-w
  locator: 124-primary2024.html/txt; relevant complete Methods, Results and Discussion;
    Figure 2 visually inspected in 124-2024-Figure2.webp.
  accessed_at: '2026-10-21T09:40:24Z'
  support: partial
  summary: Aureothricin is purified SYF1, separate from thiolutin SYF2, from cultured
    Streptomyces sp. JCK-8055. HPLC, mass and proton NMR distinguish the propionamide
    and acetamide; Figure 2a matches the native aureothricin connectivity. Table 1
    separately reports aureothricin MICs of 1.56 +/- 0 micrograms/mL against E. amylovora
    FB302, 4.16 +/- 1.48 against TS3128 and 25 +/- 0 against R. solanacearum SL341.
    Table 2 reports fungal inhibition including F. graminearum at 50 micrograms/mL,
    while F. oxysporum f. sp. cucumerinum is >200. Oomycetes in the same table are
    not fungi. Pure-compound broth-dilution methods refer to a prior protocol; the
    detailed culture-filtrate protocol must not be silently assigned to every pure-compound
    fungal assay. Supplementary strain/method details were not independently inspected.
  snapshot_sha256: cd0dc8c174c1c8671b2b156b486768edb8d7b16416b7d63d561ba74e7693c58d
- evidence_id: producer2024
  kind: primary_source
  reference: PMID:38183485; DOI:10.1007/s00253-023-12874-w
  locator: 124-primary2024.html/txt, isolation, fermentation, structural analysis
    and in planta Methods/Results/Discussion.
  accessed_at: '2026-10-21T09:40:24Z'
  support: supports
  summary: The pepper-root endophytic isolate JCK-8055 produces aureothricin in laboratory
    culture; the authors retain Streptomyces sp. despite its nearest taxonomic relatives.
    TSB cultivation at 28 C for seven days yields both antibiotics. In planta experiments
    use a two-antibiotic SYF mixture, culture filtrate or producer preparations, not
    purified aureothricin alone. Host PR-gene responses and proposed SA/JA defense
    mechanisms therefore do not establish an aureothricin-specific host pathway, transcriptomic
    dataset or microbial target. The authors explicitly call for further work on the
    metabolites' modes of action.
  snapshot_sha256: cd0dc8c174c1c8671b2b156b486768edb8d7b16416b7d63d561ba74e7693c58d
- evidence_id: rnap
  kind: primary_source
  reference: PMID:35389235; DOI:10.1128/aac.02435-21
  locator: 124-primary2022.html/txt, exact-compound Results, complete Methods and
    Discussion; Figure 3 visually inspected in 124-2022-Figure3.jpg.
  accessed_at: '2026-10-21T09:40:24Z'
  support: partial
  summary: The study explicitly calls aureothricin a putative RNAP inhibitor with
    an unclear mechanism. S. aureus HG003 and its ssrS deletion/complementation strains
    show no aureothricin hypersusceptibility attributable to loss of 6S RNA. Figure
    3A uses BHI plus aureothricin 1.25 mg/L; the spot-test method uses serial dilution
    and sub-MIC exposure. The authors suggest that aureothricin does not bind the
    RNAP DNA interface. This is an indirect, site-limited inference, not a demonstration
    that aureothricin cannot inhibit RNAP anywhere. Purified RNAP/6S-RNA binding experiments
    do not directly assay aureothricin enzyme inhibition. The study's RNA-seq compares
    genetic backgrounds, not aureothricin exposure.
  snapshot_sha256: 45ddd635b31584ef1c8555d6d8eabecd0da02c8cf1abeba31b27b27b9f164ce7
- evidence_id: response2017
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5792653/
  locator: 124-primary2017-bioc.xml/txt, exact aureothricin paragraphs and relevant
    RNA-polymerase/target assay Methods.
  accessed_at: '2026-10-21T09:40:24Z'
  support: partial
  summary: The thiolutin study reports accumulation of ubiquitylated proteins after
    aureothricin treatment in N. crassa, referring to a supplementary panel. Its purified
    polymerase, zinc-chelation and detailed JAMM/Rpn11 enzyme experiments concern
    thiolutin. Those results must not be rewritten as direct aureothricin Rpn11 binding/inhibition,
    zinc chelation or a proven bacterial killing mechanism. The aureothricin supplementary
    image and dose were not independently audited.
  snapshot_sha256: d1bbcc98d97d389178436967999c40d304a2afc068e1d1e397d960654fb2c019
- evidence_id: producer-adopted
  kind: primary_source
  reference: PMID:1171186; PMID:20507156; PMID:2262169
  locator: 124-epmc.json; 124-primary1975.pdf, page 1 English abstract visually inspected
    in 124-primary1975-p1.png.
  accessed_at: '2026-10-21T09:40:24Z'
  support: partial
  summary: PMID 1171186 / DOI 10.1248/yakushi1947.95.3_347 reports labeled propionate
    incorporation into aureothricin's propionamide after feeding Streptomyces luteoreticuli;
    only the English abstract was inspected, not the full Japanese experimental text.
    PMID 20507156 / DOI 10.1021/np900808u isolates aureothricin alongside distinct
    derivatives from Saccharothrix algeriensis NRRL B-24137 and reports moderate antimicrobial
    activity, without individual potencies in the abstract. Saccharothrix is not Streptomyces.
    PMID 2262169 / DOI 10.1007/bf02821279 reports methionine/ethionine regulation
    of thiolutin and aureothricin production in S. kasugaensis. These support producer/biosynthesis
    context, not antimicrobial molecular targets.
  snapshot_sha256: a7dd2d946c577cccc4ae5b13074ad298f8159ac18c2399382c5b909fc0da3e3a
- evidence_id: producer2016
  kind: primary_source
  reference: PMID:27018252; DOI:10.1016/j.bbrc.2016.03.105
  locator: 124-leads-epmc.json, complete original abstract.
  accessed_at: '2026-10-21T09:40:24Z'
  support: partial
  summary: The aut-cluster study reports aureothricin and thiolutin production by
    Streptomyces thioluteus DSM 40027 with heterologous expression and in-frame deletion
    evidence. It supports a producer and biosynthesis lead. Biosynthetic genes and
    engineered HlmK are not aureothricin antimicrobial targets or demonstrated resistance
    mechanisms. Full methods were not inspected.
  snapshot_sha256: 0202eb53e27f8259525d8939b4c1045c6841a6ca89935c89eb7096b097a6e339
- evidence_id: host-adopted
  kind: primary_source
  reference: PMID:11433393; DOI:10.1002/ijc.1321
  locator: 124-epmc.json, complete abstract.
  accessed_at: '2026-10-21T09:40:24Z'
  support: context_only
  summary: The HUVEC screen includes aureothricin, thioaurin and thiolutin. The 0.83
    micromolar adhesion IC50, paxillin degradation and in vivo angiogenesis results
    in the abstract are explicitly thiolutin results and cannot be assigned to aureothricin
    or interpreted as aureothricin clinical efficacy.
  snapshot_sha256: a7dd2d946c577cccc4ae5b13074ad298f8159ac18c2399382c5b909fc0da3e3a
- evidence_id: historical-adopted
  kind: primary_source
  reference: PMID:13084502; PMID:13096448; PMID:14275485
  locator: 124-epmc.json, complete bibliographic records; no abstracts returned.
  accessed_at: '2026-10-21T09:40:24Z'
  support: unknown
  summary: PMID 13084502 concerns a yellow crystalline antibiotic identified with
    aureothricin from Streptomyces 39a; full taxonomic and identity evidence was not
    inspected. PMID 13096448 concerns a crystalline toxic substance from an aureothricin-producing
    culture; its title alone does not identify that toxic substance as aureothricin.
    PMID 14275485 concerns X-ray powder identification of thiolutin and aureothricin
    after chromatography. These remain unverified historical leads and supply no new
    exact potency or target assertion here.
  snapshot_sha256: a7dd2d946c577cccc4ae5b13074ad298f8159ac18c2399382c5b909fc0da3e3a
- evidence_id: reviews-adopted
  kind: database
  reference: PMID:24141227; PMID:24323287; PMID:24835149
  locator: 124-epmc.json, complete abstracts; 124-review2014-bioc.xml/txt, exact identity
    and complete section 4.1 mechanism paragraphs.
  accessed_at: '2026-10-21T09:40:24Z'
  support: context_only
  summary: All three are secondary reviews used as leads. DOI 10.3390/md11103970 is
    a class isolation/synthesis/biosynthesis review; its holomycin resistance examples
    are not aureothricin results. DOI 10.1007/s00253-013-5410-z concerns holomycin,
    including hlm genetics and self-protection. DOI 10.1039/c3np70106a reviews dithiolopyrrolones
    and documents thiolutin/holomycin experiments and mechanism uncertainty; inspected
    mechanism paragraphs do not provide an exact aureothricin RNAP assay. None establishes
    an aureothricin-specific resistance or clinical claim.
  snapshot_sha256: 8312552128af460fb2e6819dfad2b9cba4627e39dbd5f503ee7696c6d8144dc3
- evidence_id: adapter
  kind: database
  reference: iModulonDB structured cross-checks
  locator: 055-imodulondb-datasets-retry.txt successful inventory; 124-imodulondb-rnap.txt
    and 124-imodulondb-ssrS.txt successful searches.
  accessed_at: '2026-10-21T09:40:24Z'
  support: context_only
  summary: Before open-ended mechanism research, the covered e_coli/precise_mg1655
    RNA polymerase query returned ten gene matches including rpoA b3295 and rpoC b3988,
    but no iModulon. This is generic protein-name context, not evidence that E. coli
    is the native target organism or that aureothricin binds those proteins. A later
    s_aureus/staph_precise108 ssrS query returned no gene or module hit; that does
    not negate the HG003 experiment or prove catalog equivalence. S. thioluteus and
    N. crassa were not covered by the inspected inventory.
  snapshot_sha256: f3c5ea1d91233e3c4cb2f09ed871d4f5f254fa2727657ab93307cb425bd41341
- evidence_id: adapter-command
  kind: validation
  reference: Structured adapter commands
  locator: Actual successful local runner and query invocations.
  accessed_at: '2026-10-21T09:40:24Z'
  support: context_only
  summary: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 search --organism e_coli --dataset
    precise_mg1655 --query RNA\ polymerase; second query uses --organism s_aureus
    --dataset staph_precise108 --query ssrS. Both commands exited 0. No module hit
    warranted a summarize call.
  snapshot_sha256: 25ced167b4574a4613d3f87484504df427338d48bd7cd1db2b7af9dd2d422101
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 124-local-hits.txt and 124-maintained-search.txt; exact-name, DOI and original-title
    literature checks.
  accessed_at: '2026-10-21T09:40:24Z'
  support: context_only
  summary: Hidden- and ignored-inclusive local searches locate the seed and source
    context but no maintained exact primary annotation or source-specific mechanism
    correction. Generated pages and historical reports were leads only. Bounded exact-compound
    literature research supports activity and producer leads but leaves molecular
    mechanism unresolved; this is not an exhaustive proof of absence.
  search_scope: rg --no-ignore --hidden for CHEBI:156452, aureothricin, slug and UGZYFXMSMFMTSM
    across batch013, then curation/conf/scripts/data/raw/src/reports/reviews; initial
    scan excludes .git and .venv. All ten adopted citation records and available original
    abstracts, official chemistry pages and bounded exact-compound primary mechanism/activity
    searches; free sources only.
  snapshot_sha256: 146b6a73eb7f03c03dd602f143739474f2ea9b7045d837ffed1c560c20545d1b
- evidence_id: validation
  kind: validation
  reference: Focused schema, strict and chemistry checks
  locator: 124-focused-results.json and associated logs; initial input audit.
  accessed_at: '2026-10-21T09:40:24Z'
  support: supports
  summary: All three actual focused commands exited 0. All 13 initial source/target
    hashes remain unchanged. History is three seed/reseed events, consistent with
    SEEDED. No native record edits occurred.
  snapshot_sha256: 73b09278556e4ee9bea0eecc7236909392017df179dda8201440aec6aff78d69
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Exact identity, evidence placement, mechanism, activity, producer and native
    ownership rules.
  accessed_at: '2026-10-21T09:40:24Z'
  support: supports
  summary: A source role may establish provenance without establishing exact-compound
    mechanism certainty. Keep related molecules, mixture effects, biosynthetic enzymes,
    genetic susceptibility, direct inhibition and host responses at their measured
    scopes. Missing optional annotation is not inherently an error.
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral exact aureothricin and names
  outcome: supported
  summary: Structures, formula, charge, names and independent structural crosswalks
    agree. Historical source spelling does not warrant reassigning a producer species.
  target_ids:
  - CHEBI:156452
  evidence_ids:
  - identity
  - chemistry
  - xref
- assessment_id: activity
  area: evidence
  topic: Antibacterial and antifungal roles
  outcome: supported
  summary: Original and modern exact-compound primary experiments support qualitative
    antibacterial/fungal inclusion. Potency varies by test organism and must remain
    assay-specific.
  target_ids:
  - CHEBI:156452
  evidence_ids:
  - original
  - primary2024
- assessment_id: mechanism
  area: evidence
  topic: Unresolved RNAP mechanism versus generated certainty
  outcome: concern
  summary: ChEBI source provenance is faithful, but the assertion that the mechanism
    is true exceeds the inspected exact evidence. The 2022 primary study explicitly
    treats the mechanism as unclear; its negative genetic result is not proof of no
    possible RNAP action.
  target_ids:
  - CHEBI:156452
  evidence_ids:
  - source
  - rnap
  - response2017
  - reviews-adopted
  - rubric
- assessment_id: producer
  area: evidence
  topic: Fermentation and producer definition
  outcome: supported
  summary: Primary studies and abstracts support aureothricin/thiolutin co-production
    in multiple Streptomyces cultures; one adopted additional producer is Saccharothrix.
    The qualitative moderate-activity descriptor is assay-dependent, not a universal
    potency threshold.
  target_ids:
  - CHEBI:156452
  evidence_ids:
  - producer-adopted
  - producer2016
  - producer2024
- assessment_id: optional
  area: completeness
  topic: Exact activity, producer, resistance, host response and datasets
  outcome: unknown
  summary: Activity and producer objects are useful optional follow-ups. No exact
    aureothricin resistance mechanism, clinical indication or exposure transcriptomics
    was established. Genetic RNA-seq and mixed-fermentation plant responses are not
    aureothricin exposure datasets.
  target_ids:
  - CHEBI:156452
  evidence_ids:
  - primary2024
  - producer2024
  - rnap
  - host-adopted
  - adapter
- assessment_id: ownership
  area: ownership
  topic: Source-derived mechanism and optional primary annotations
  outcome: supported
  summary: The source mapping and generated explanatory text own the certainty correction.
    The actual native record owns separately authorized primary curation. No global
    deletion of the RNAP role mapping is justified by this record alone.
  target_ids:
  - CHEBI:156452
  evidence_ids:
  - source
  - rubric
- assessment_id: gates
  area: schema
  topic: Focused checks and history
  outcome: supported
  summary: Focused checks pass; source/record hashes and seed history are consistent.
    No REVIEWED promotion is proposed.
  target_ids:
  - CHEBI:156452
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: aureothricin-rnap-mechanism-certainty
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generated mechanism wording asserts certainty that the exact-compound evidence
    does not establish
  description: The source-derived note says the mechanism is true, although the exact
    aureothricin primary study PMID 35389235 explicitly treats RNAP inhibition as
    putative and the mechanism as unclear. Its ssrS experiment supports a limited
    susceptibility observation, not direct RNAP inhibition or its universal exclusion.
    Retain honest ChEBI provenance while qualifying the unresolved biological claim.
    Thiolutin and holomycin experiments cannot supply the missing exact mechanism.
  target_ids:
  - CHEBI:156452
  field_paths:
  - mode_of_action
  - mode_of_action_notes
  - mode_of_action_target_scope
  evidence_ids:
  - record
  - source
  - identity
  - rnap
  - response2017
  - reviews-adopted
  - rubric
  rule_id: 'native-review-checklist: Claim-level primary mechanism evidence and scope'
  native_severity: major unsupported certainty in a mechanistic assertion
  normalization_reason: The problem is a material mechanism assertion, not optional
    missing detail. The role mapping is faithfully sourced, and the review does not
    prove RNAP inhibition false; the confirmed error is the unqualified certainty
    added to an unresolved exact-compound mechanism.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Compound-specific source mechanism policy if qualification or override is
      needed
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source-derived mode and certainty wording
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted upstream role provenance; refresh only through maintained extraction
- finding_id: F2
  issue_key: aureothricin-qualified-primary-activity-producer-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Qualified exact activity and producer evidence can enrich the seed
  description: Modern primary isolation and separate pure-compound assays provide
    activity and producer evidence. Preserve exact AUR versus thiolutin columns, organism
    and protocol limits, and the distinction between pure compound, mixtures and culture
    filtrate. Do not turn plant defense responses, biosynthesis proteins or ssrS experiments
    into direct antibacterial targets or resistance claims.
  target_ids:
  - CHEBI:156452
  field_paths:
  - activity_spectrum
  - producer_organisms
  - evidence
  - discussions
  evidence_ids:
  - primary2024
  - producer2024
  - producer-adopted
  - producer2016
  - rnap
  - rubric
  rule_id: 'native-review-checklist: Optional completeness with experiment-specific
    evidence'
  native_severity: informational optional primary enrichment
  normalization_reason: Current antimicrobial inclusion is supported and missing quantitative/producer
    fields are optional. Full protocol and source-specific scope checks precede enrichment.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/aureothricin.yaml
    role: Curator-owned qualified exact primary evidence, activity, producer and mechanism
      discussion through validated writer/history helper
actions:
- action_id: A1
  description: Qualify the source-derived RNA-polymerase claim through maintained
    generation policy.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:156452
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Compound-specific source mechanism policy if qualification or override is
      needed
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated source-derived mode and certainty wording
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted upstream role provenance; refresh only through maintained extraction
  acceptance_checks:
  - Replace the assertion of demonstrated truth with accurate source attribution and
    the unresolved exact-compound mechanism. Preserve the ChEBI role as provenance;
    do not imply that PMID 35389235 disproves every RNAP interaction.
  - Determine whether the mode should remain explicitly source-derived with qualification
    or be withheld pending exact primary evidence, using maintained compound-specific
    policy. Do not globally delete CHEBI:37416 mapping for other validated compounds.
  - If HOST_SHARED_TARGET remains, describe it as the scope of the hypothesized enzyme
    family, not established host inhibition or selectivity for aureothricin. Do not
    substitute thiolutin zinc-chelation/Rpn11 results as a proven AUR mechanism.
  - Regenerate through the maintained source workflow, inspect the exact diff and
    run focused schema/strict plus required shared source/history/reference gates.
- action_id: A2
  description: Curate exact activity and fermentation evidence with remaining protocol
    limits.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:156452
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/aureothricin.yaml
    role: Curator-owned qualified exact primary evidence, activity, producer and mechanism
      discussion through validated writer/history helper
  acceptance_checks:
  - Use PMID 38183485 SYF1/aureothricin and the separate compound columns. Resolve
    supplemental strain/method details and the referenced broth-dilution protocol
    before numerical annotation; preserve MIC units and the >200 limit, and distinguish
    fungi from oomycetes.
  - Represent Streptomyces sp. JCK-8055 as the demonstrated cultured producer without
    assigning it to a nearest named species. Keep Saccharothrix algeriensis NRRL B-24137
    distinct from Streptomyces and inspect original methods before precise producer/biosynthesis
    additions.
  - Keep in planta two-antibiotic mixtures, filtrate, producer preparations and host
    PR-gene responses separate from purified aureothricin. Do not infer pure-compound
    disease control, immune pathways or clinical use.
  - Keep the HG003 ssrS genotype comparison and sub-MIC spot assay distinct from direct
    enzyme inhibition, resistance mechanisms and aureothricin-induced RNA-seq.
  - Use write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/aureothricin.yaml
    for separately authorized curation, then focused/shared gates. No automatic status
    promotion.
limitations:
- All 13 captured maintained input hashes remain unchanged.
- All ten adopted bibliographic records and every available abstract were read. PMID
  13084502, 13096448 and 14275485 have no inspected full text or abstract. The 1975
  free paper was inspected only through its page-1 English abstract; the Japanese
  full methods were not independently translated. The 2010 ACS full text was inaccessible;
  its individual potency and methods remain unverified.
- The 1948 six-page extracted text was read completely, but historical table cells
  were not visually audited. No numerical historical MIC is curated from it.
- The 2022 exact aureothricin Results, complete Methods and Discussion, and Figure
  3 were inspected. It is an indirect genetic susceptibility experiment; no exhaustive
  review of every historical RNAP experiment is claimed.
- The 2024 relevant complete Methods, Results and Discussion and structural Figure
  2 were inspected. Raw spectra, supplement and referenced detailed pure-compound
  assay protocol were not independently audited. In planta efficacy and host-gene
  responses use mixtures or producer material.
- The 2017 exact aureothricin paragraphs and relevant polymerase/target Methods were
  inspected, not every supplementary experiment. The exact AUR supplemental protein-response
  panel was not independently viewed; no quantitative response or direct JAMM inhibition
  is asserted.
- MetaCyc is account-gated; CAS is crosswalk-only. Structured adapter matches are
  gene context, not target validation, and absent catalog coverage is not biological
  evidence. No exhaustive literature, resistance or producer census is claimed.
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
