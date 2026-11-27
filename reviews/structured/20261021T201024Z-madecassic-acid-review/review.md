# Madecassic acid: exact references and primary activity review

- Review: 20261021T201024Z-madecassic-acid-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:52:52Z
- Finished UTC: 2026-10-21T20:10:24Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native neutral madecassic-acid graph is coherent and primary antibacterial studies support the filing role. Two major grounding findings concern an internally contradictory KNApSAcK entry and stereochemically incomplete HMDB/LIPID MAPS structures. All ten adopted references were disposed at complete-abstract depth; newer original experiments were assessed without converting docking or crude-extract effects into direct binding.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position619; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:73058 | data/antibiotics/antibacterial/madecassic-acid.yaml | generated | madecassic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:73058 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:73058 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:73058 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:73058 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:73058 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:73058 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:73058 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:73058 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:73058 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:73058 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:73058 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:73058 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact native structure and names

identity: supported. Targets: CHEBI:73058.

The native neutral thirteen-centre ursane-derived acid agrees with current ChEBI/PubChem and the original2023 drawing. No native wrong-isomer finding is justified.

### Exact external associations

grounding: concern. Targets: CHEBI:73058.

KNApSAcK has mutually incompatible encodings. HMDB and LIPID MAPS carry two unassigned native centres, so exact stereochemical equivalence is not established. Other restricted references remain explicit limitations.

### Antibacterial classification and exact-material scope

evidence: supported. Targets: CHEBI:73058.

Primary2023 growth inhibition and2026 E.coli experiments support the antibacterial role. Extracts, derivatives, host effects and quorum-sensing endpoints remain separate.

### Envelope, crude topoisomerase and respiratory evidence

evidence: unknown. Targets: CHEBI:73058.

The papers support bounded cellular and membrane-functional effects. Crude extracts and computational affinities do not prove selective direct binding; no mandatory missing target object is inferred.

### Adopted sources, reference links and generated history

provenance: supported. Targets: CHEBI:73058.

All native fields and ten adopted abstracts were assessed; patents resolve as related documents. Thirteen original inputs and generated-file boundaries are preserved.

### Bounded optional curation

completeness: unknown. Targets: CHEBI:73058.

Exact-strain activity and qualified respiratory/envelope evidence can support later curation. Restricted registries, supplementary controls and raw measurements remain unverified; optional omissions are not findings.

## Findings

### F1: KNApSAcK exact accession has conflicting constitutional encodings

major / open / confirmed; issue key: madecassic-acid-knapsack-inconsistent-structure-descriptors.

C00051418 has a correct native InChI but a formate-ester SMILES and a third displayed key. Exact grounding must resolve the internal disagreement; a matching name or formula is insufficient. Do not replace the correct native acid with the incompatible SMILES.

### F2: Two asserted exact registries omit two native stereocentres

major / open / confirmed; issue key: madecassic-acid-hmdb-lipidmaps-incomplete-stereochemistry.

HMDB0036670 displayed molfile and LMPR0106180009 actual encodings leave Standard InChI centres21 and23 unassigned. Remaining assigned centres and constitution agree, so these are incomplete stereo representations, not proven opposite epimers. The native exact xrefs overstate the verified structure equivalence.

## Recommended Actions And Acceptance Checks

### A1

Resolve or qualify the affected exact association through maintained ChEBI source handling and regenerate.

- Compare actual SMILES, InChI and molfile graphs, including every native stereocentre; preserve internal provider conflicts rather than accepting a displayed label/key alone.
- Retain the native acid and its primary activity. Do not infer an opposite epimer from missing stereo or substitute a formate ester.
- Regenerate through maintained inputs and rerun focused schema/strict/chemistry, corpus reproduction and required shared gates.

### A2

Resolve or qualify the affected exact association through maintained ChEBI source handling and regenerate.

- Compare actual SMILES, InChI and molfile graphs, including every native stereocentre; preserve internal provider conflicts rather than accepting a displayed label/key alone.
- Retain the native acid and its primary activity. Do not infer an opposite epimer from missing stereo or substitute a formate ester.
- Regenerate through maintained inputs and rerun focused schema/strict/chemistry, corpus reproduction and required shared gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/madecassic-acid.yaml; Entire native record and exact ChEBI inventory row1868 | supports | All three names, three parents, antibacterial role, five chemical xrefs, DrugBank association, three patents, one source concept and four seed events were read. The record has no structured MIC, molecular target, resistance, producer, clinical, dataset or causal-graph objects. The source-owned correction path is ChEBI extraction and seeding; all thirteen original input hashes are preserved. |
| local | /private/tmp/am-review-session/619-local-hits.txt; Exact identity/label/slug search including hidden and ignored files | context_only | The whole native and maintained source row were assessed. Local results were discovery context, not independent experimental evidence. Optional enrichment was not treated as a required missing field. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/73058/; Current complete entry and original adopted row | supports | Current ChEBI reproduces the native C30H48O6, neutral charge, thirteen assigned tetrahedral centres, exact key PRAUVHZJPXOEIF-AOLYGAPISA-N, aliases and associations. The systematic name and native graph specify the urs-12-ene, 2alpha/3beta/6beta/23-hydroxy carboxylic acid. Source agreement does not independently validate every propagated xref. |
| chemistry | /private/tmp/am-review-session/619-authority-chemistry.json; 619-compare.py independently parses fourteen actual structure encodings | partial | Native SMILES/InChI, current ChEBI SMILES/InChI and contextual PubChem73412 SMILES/InChI match reciprocally with chirality. KNApSAcK InChI also matches, but its actual SMILES has different constitution. LIPID MAPS SMILES/InChI/molfile, its linked PubChem6710742 pair, and HMDB displayed molfile all leave the same two native centres unspecified. Formula, masses and source mint pass focused checks. |
| knapsack | http://www.knapsackfamily.com/knapsack_core/information.php?word=C00051418; Complete displayed identity/structure fields | refutes | The InChI exactly matches native madecassic acid. The SMILES instead contains a formate ester branch OC=O where the native graph has C(=O)O, yielding RYNVHQKDPRHKGH-WYIBYPNRSA-N. Its displayed key RYNVHQKDPRHKGH-AWQHCHLSNA-N disagrees with both encodings. This is an internal descriptor conflict, not proof that the entire named accession denotes only a different molecule. |
| lipidmaps | https://www.lipidmaps.org/rest/compound/lm_id/LMPR0106180009/all; Actual JSON and separately downloaded molfile endpoint | partial | The entry names 6beta-hydroxyasiatic acid but encodes PRAUVHZJPXOEIF-VGKQSNDQSA-N with two unspecified ring-junction stereocentres: Standard InChI /t21? and23?. All other assigned centres match. The molfile and its linked PubChem6710742 corroborate that incomplete representation. The initial /mol endpoint returned an error message despite HTTP200; only the corrected /molfile response was parsed. |
| hmdb | https://hmdb.ca/metabolites/HMDB0036670; Web-rendered complete two-dimensional MOL block, lines74–156, preserved in619-hmdb-web-capture.txt | partial | The initial web response exposed the complete37-atom/41-bond MOL block. Its fixed-width content was extracted with only presentation indentation and header normalization; independent parsing yields the same VGKQSNDQSA key and two unspecified centres as LIPID MAPS. Subsequent page, XML and direct molfile requests returned403. No unavailable HMDB InChI, SMILES, 3D block or full page is claimed read. |
| parents | CHEBI:25384; CHEBI:25872; CHEBI:33573; CHEBI:33282; Current official term responses 618619-term-*.json and actual molecular graph | supports | Monocarboxylic acid, pentacyclic triterpenoid and tetrol fit the single carboxy group, five-ring triterpenoid scaffold and four non-carboxy hydroxy groups. Antibacterial agent is independently supported by exact-compound experiments. |
| restricted | CAS:18449-41-7; Reaxys:3041357; DrugBank:DB14037; Public registry attempts and current ChEBI associations | unknown | CAS supplied only a public page shell; Reaxys and DrugBank access was restricted. Independent exact registry contents were not established. Their propagated associations are neither certified nor condemned, and no paid access was used. |
| patents | CN101991578A; TW200938215A; FR2963553A3; Original patent abstract/background/claims relevant to madecassic acid; French abstract and exact composition passages | context_only | CN concerns extraction and alpha-glucosidase-inhibitor use; claims specify separated acids above95% purity. TW concerns antiglycation by the acids or extracts. FR concerns a multicomponent hydration/anti-inflammatory cosmetic formulation containing madecassic acid. These are related document links, not parent-compound bacterial target or clinical efficacy evidence. FR resolves as A3, whereas guessed A1/B1 routes failed; legal status and unrelated examples were not audited. |
| adopted22816768 | PMID:22816768; DOI:10.1021/jf302529x; Complete original indexed abstract in619-adopted.json | context_only | Dietary triterpene absorption and antioxidant effects, not a bacterial assay. Full original methods were not assessed for this adopted lead. |
| adopted22966846 | PMID:22966846; DOI:10.3109/13880209.2012.685946; Complete original indexed abstract in619-adopted.json | context_only | Centella asiatica HPLC profiles by plant part and harvest, a source-occurrence lead. Full original methods were not assessed for this adopted lead. |
| adopted23346217 | PMID:23346217; DOI:10.1155/2012/848093; Complete original indexed abstract in619-adopted.json | context_only | Burn-wound healing comparison; glycosides and aglycones are distinct materials. Full original methods were not assessed for this adopted lead. |
| adopted24965394 | PMID:24965394; Complete original indexed abstract in619-adopted.json | context_only | CT26 mouse colon-cancer apoptosis/immunomodulation, not bacterial inhibition. Full original methods were not assessed for this adopted lead. |
| adopted25685908 | PMID:25685908; DOI:10.3390/molecules20023001; Complete original indexed abstract in619-adopted.json | context_only | Zebrafish metabolism, not a bacterial mechanism. Full original methods were not assessed for this adopted lead. |
| adopted26633490 | PMID:26633490; DOI:10.3390/nu7125512; Complete original indexed abstract in619-adopted.json | context_only | Diabetic mouse effects of madecassic and rotundic acids, not antibacterial evidence. Full original methods were not assessed for this adopted lead. |
| adopted27728894 | PMID:27728894; DOI:10.1016/j.biopha.2016.10.015; Complete original indexed abstract in619-adopted.json | context_only | Hypoxic retinal-cell ROS/ER-stress effects, a host endpoint. Full original methods were not assessed for this adopted lead. |
| adopted28358365 | PMID:28358365; DOI:10.1038/cddis.2017.150; Complete original indexed abstract in619-adopted.json | context_only | Host colitis/PPARgamma-AMPK pathway, not a bacterial protein target. Full original methods were not assessed for this adopted lead. |
| adopted30324102 | PMID:30324102; DOI:10.3389/fchem.2018.00434; Complete original indexed abstract in619-adopted.json | context_only | Modified derivatives5,12,17 and host ERK/BRAF outcomes are not parent-compound bacterial results. Full original methods were not assessed for this adopted lead. |
| adopted30679477 | PMID:30679477; DOI:10.1038/s41598-018-36555-1; Complete original indexed abstract in619-adopted.json | context_only | Murtilla extract and isolated madecassic acid insulin/endothelial outcomes have distinct material and host scopes. Full original methods were not assessed for this adopted lead. |
| activity2023 | PMID:36838882; DOI:10.3390/molecules28041895; PMC9967526; Complete main text and tables; Methods4.1–4.3; actual Figure16 viewed | supports | Madecassic acid from Shanghai Yuanye, lotJ12HB184580 and &gt;98% HPLC purity, was tested in a TTC microdilution assay with10^6–10^7 CFU/mL suspension,37C for12–16h plus4h TTC development. Text MICs are S.aureus CMCC(B)26003 31.25, MRSA ATCC43300 62.5, E.coli ATCC25922 250, P.aeruginosa ATCC27853 125, B.subtilis62.5 and B.megaterium ATCC35985 62.5 micrograms/mL. B.subtilis strain is not specified. Table1 rounds31.25 to31.2 and oxacillin0.048 to0.0; retain text precision and assay context before numerical curation. Figure16 visibly shows the carboxylic acid and native hydroxy stereochemical pattern. |
| mechanism2023 | DOI:10.3390/molecules28041895; Full Results/Methods; actual Figures13/14 and their lane captions | partial | Conductivity, extracellular nucleic-acid/protein/AKP measurements and TEM support envelope injury under the tested conditions. Soluble-protein bands and post-treatment SDH/MDH activities do not identify direct protein binding. Topoisomerase assays use crude S.aureus extract and pET-28a, with altered relaxation patterns at mg/mL concentrations; the article also reports DNA changes without enzyme. These experiments do not establish selective binding to purified TopA or gyrase. The actual gels were viewed without independent densitometry. |
| bd2026 | PMID:41574235; DOI:10.1039/d5md01116g; PMC12822377; Complete main XML, Results/Methods and open author PDF; actual Figures1/2 at printedp1516 viewed; supplementary data not recovered | partial | Centella-derived madecassic acid inhibits oxygen consumption in E.coli EC958 bd-I-only membranes, IC50 34±11 micromolar, and growth, IC50 9.4±1.5 micromolar with63% maximum inhibition. Wild-type growth has approximately10 micromolar IC50 and48% maximum inhibition. The parent viability curve shows little change below 1 mM, but its 1 mM point is near log10(survival percent)=0, versus approximately2 at baseline. This conflicts with categorical no-killing language in the main text; no universal absence of killing or exact MBC is inferred. DerivativeMA-4 results remain separate. Membrane assays use0.5mg/mL wet membranes,8mM succinate,37C,15–20min; growth uses glycerol/casamino-acid M9 and DMSO. Docking-derived Kd1.14 micromolar is computational, not measured affinity. Main text reports complementary SDH and duroquinol controls in EcoM4 pSU2718G-cydABX-his6 membranes, including loss of bd-I oxygen consumption at 1 mM; underlying supplementary figures/raw data were not inspected. Binding-site specificity remains modeled. |
| kp2026 | PMID:41619992; DOI:10.1016/j.micpath.2026.108332; Complete original indexed abstract only | context_only | Exact PT-5 madecassic acid had negligible bactericidal action against KP31 but reduced quorum-sensing/virulence-associated phenotypes and enhanced antibiotics at32 micrograms/mL. Gene-expression changes and a larval combination model are not direct protein binding or human efficacy. Full strain/material/assay methods were not recovered. |
| adapter | kg-microbe-sources iModulonDB e_coli/precise1k; Catalog and actual cydA/topA/gyrB queries before new mechanism-paper follow-up | context_only | The native record names no protein mechanism. New primary leads prompted E.coli queries resolving cydA b0733, topA b1274 and gyrB b3699; no iModulons were returned. These reference-gene results are naming context, not EC958 or S.aureus assay evidence, and cannot prove inhibition. |
| search | Europe PMC TITLE_ABS:"madecassic acid"; All first100 titles of204 results read, followed by exact adopted and selected antibacterial originals | context_only | Search recovered primary bacterial experiments alongside derivatives, extract and host studies. All ten adopted abstracts and selected2023/2026 originals have explicit depth limits. No exhaustive absence claim or uninspected-source mechanism is made. |

## Limits And Additional Notes

- All ten adopted papers were read at complete-abstract depth, with no full-method claim for those leads. The2023 and2026 respiratory main texts were read in full; the2026 KP31 lead is abstract-only.
- HMDB assessment uses the complete initially web-displayed2D molfile only; subsequent direct requests failed. Its remaining chemical fields are not independently verified. CAS, Reaxys and DrugBank remain restricted or shell-only.
- The2026 respiratory supplement was not recovered; control experiments are known from main-text reporting, not independent inspection of supplementary figures. Computational Kd is not measured binding. Raw assay data and spectra were not reprocessed.
- Patent reading was limited to compound-relevant abstracts/background/claims/composition, without legal-status assessment or transfer of mixture/host results to bacterial activity.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Native data, source inputs and status/history were not edited. Chemistry used the isolated019 RDKit interpreter against062; schema/strict checks used062.
- The initial LIPID MAPS /mol response was a text error, PMC pages sometimes returned challenge HTML, and guessed FR A1/B1 URLs failed. Actual /molfile, FR A3, EuropePMC XML and author-repository PDF were used after inspecting response contents.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T201024Z-madecassic-acid-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Madecassic acid: exact references and primary activity review'
started_at: '2026-10-21T19:52:52Z'
finished_at: '2026-10-21T20:10:24Z'
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
summary: The native neutral madecassic-acid graph is coherent and primary antibacterial
  studies support the filing role. Two major grounding findings concern an internally
  contradictory KNApSAcK entry and stereochemically incomplete HMDB/LIPID MAPS structures.
  All ten adopted references were disposed at complete-abstract depth; newer original
  experiments were assessed without converting docking or crude-extract effects into
  direct binding.
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
  - path: data/antibiotics/antibacterial/madecassic-acid.yaml
    sha256: 88367388a7f7d5cfa017ec0bceab5338f6cd624f0ac9eec527c49ed91610eb8e
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
- target_id: CHEBI:73058
  path: data/antibiotics/antibacterial/madecassic-acid.yaml
  label: madecassic acid
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
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position619; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:73058
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:73058
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    619
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:73058
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/madecassic-acid.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:73058
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/madecassic-acid.yaml --out /private/tmp/am-review-session/619-strict.tsv
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
  - CHEBI:73058
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
  - CHEBI:73058
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
  - CHEBI:73058
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
  - CHEBI:73058
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
  - CHEBI:73058
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
  - CHEBI:73058
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
  - CHEBI:73058
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
  - CHEBI:73058
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
  - CHEBI:73058
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/madecassic-acid.yaml
  locator: Entire native record and exact ChEBI inventory row1868
  accessed_at: '2026-10-21T20:10:17Z'
  support: supports
  summary: All three names, three parents, antibacterial role, five chemical xrefs,
    DrugBank association, three patents, one source concept and four seed events were
    read. The record has no structured MIC, molecular target, resistance, producer,
    clinical, dataset or causal-graph objects. The source-owned correction path is
    ChEBI extraction and seeding; all thirteen original input hashes are preserved.
  snapshot_sha256: 6a768b8813d09b5735db500fd0ca21bc785d8253c3d74a9e383a856b8a3c364e
- evidence_id: local
  kind: search
  reference: /private/tmp/am-review-session/619-local-hits.txt
  locator: Exact identity/label/slug search including hidden and ignored files
  accessed_at: '2026-10-21T20:10:17Z'
  support: context_only
  summary: The whole native and maintained source row were assessed. Local results
    were discovery context, not independent experimental evidence. Optional enrichment
    was not treated as a required missing field.
  search_scope: Initial rg --no-ignore --hidden identity/label/slug inventory; exact
    source-row scans across raw and curator inputs; no claim of universal literature
    absence.
  snapshot_sha256: 85b8ec9e79f8fb31f20966e64733165a468d2c611bf56fcec0eda08dfe0afe6e
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/73058/
  locator: Current complete entry and original adopted row
  accessed_at: '2026-10-21T20:10:17Z'
  support: supports
  summary: Current ChEBI reproduces the native C30H48O6, neutral charge, thirteen
    assigned tetrahedral centres, exact key PRAUVHZJPXOEIF-AOLYGAPISA-N, aliases and
    associations. The systematic name and native graph specify the urs-12-ene, 2alpha/3beta/6beta/23-hydroxy
    carboxylic acid. Source agreement does not independently validate every propagated
    xref.
  snapshot_sha256: b8d69e068222713033099bcd15a9b661d1532ea3f8e2af8ed5f807a48f3e8dc3
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/am-review-session/619-authority-chemistry.json
  locator: 619-compare.py independently parses fourteen actual structure encodings
  accessed_at: '2026-10-21T20:10:17Z'
  support: partial
  summary: Native SMILES/InChI, current ChEBI SMILES/InChI and contextual PubChem73412
    SMILES/InChI match reciprocally with chirality. KNApSAcK InChI also matches, but
    its actual SMILES has different constitution. LIPID MAPS SMILES/InChI/molfile,
    its linked PubChem6710742 pair, and HMDB displayed molfile all leave the same
    two native centres unspecified. Formula, masses and source mint pass focused checks.
  snapshot_sha256: 3cd84fc6d5c7e67bf0b65bd56fc9ad138c1bac02cdec948d79edcebe4c351abe
- evidence_id: knapsack
  kind: authority
  reference: http://www.knapsackfamily.com/knapsack_core/information.php?word=C00051418
  locator: Complete displayed identity/structure fields
  accessed_at: '2026-10-21T20:10:17Z'
  support: refutes
  summary: The InChI exactly matches native madecassic acid. The SMILES instead contains
    a formate ester branch OC=O where the native graph has C(=O)O, yielding RYNVHQKDPRHKGH-WYIBYPNRSA-N.
    Its displayed key RYNVHQKDPRHKGH-AWQHCHLSNA-N disagrees with both encodings. This
    is an internal descriptor conflict, not proof that the entire named accession
    denotes only a different molecule.
  snapshot_sha256: e3d7be57c650b7814c654c2a3e7821e06899a7a4d66761b49f1f6ea26e0fa6f1
- evidence_id: lipidmaps
  kind: authority
  reference: https://www.lipidmaps.org/rest/compound/lm_id/LMPR0106180009/all
  locator: Actual JSON and separately downloaded molfile endpoint
  accessed_at: '2026-10-21T20:10:17Z'
  support: partial
  summary: 'The entry names 6beta-hydroxyasiatic acid but encodes PRAUVHZJPXOEIF-VGKQSNDQSA-N
    with two unspecified ring-junction stereocentres: Standard InChI /t21? and23?.
    All other assigned centres match. The molfile and its linked PubChem6710742 corroborate
    that incomplete representation. The initial /mol endpoint returned an error message
    despite HTTP200; only the corrected /molfile response was parsed.'
  snapshot_sha256: 75dc3a45d6608d69f85ed4d72a5e2f564ad8e0a3863afaea1a575ad9d2a95bb7
- evidence_id: hmdb
  kind: authority
  reference: https://hmdb.ca/metabolites/HMDB0036670
  locator: Web-rendered complete two-dimensional MOL block, lines74–156, preserved
    in619-hmdb-web-capture.txt
  accessed_at: '2026-10-21T20:10:17Z'
  support: partial
  summary: The initial web response exposed the complete37-atom/41-bond MOL block.
    Its fixed-width content was extracted with only presentation indentation and header
    normalization; independent parsing yields the same VGKQSNDQSA key and two unspecified
    centres as LIPID MAPS. Subsequent page, XML and direct molfile requests returned403.
    No unavailable HMDB InChI, SMILES, 3D block or full page is claimed read.
  snapshot_sha256: df192bc69fbd9626f18c99948b38fe3a0f5374dac4cc9abdf6080c01d41eb113
- evidence_id: parents
  kind: authority
  reference: CHEBI:25384; CHEBI:25872; CHEBI:33573; CHEBI:33282
  locator: Current official term responses 618619-term-*.json and actual molecular
    graph
  accessed_at: '2026-10-21T20:10:17Z'
  support: supports
  summary: Monocarboxylic acid, pentacyclic triterpenoid and tetrol fit the single
    carboxy group, five-ring triterpenoid scaffold and four non-carboxy hydroxy groups.
    Antibacterial agent is independently supported by exact-compound experiments.
  snapshot_sha256: 261207ff98f67f017610f10d605179a0ac8f65ff77b9444d6335ae0defd3a2e1
- evidence_id: restricted
  kind: authority
  reference: CAS:18449-41-7; Reaxys:3041357; DrugBank:DB14037
  locator: Public registry attempts and current ChEBI associations
  accessed_at: '2026-10-21T20:10:17Z'
  support: unknown
  summary: CAS supplied only a public page shell; Reaxys and DrugBank access was restricted.
    Independent exact registry contents were not established. Their propagated associations
    are neither certified nor condemned, and no paid access was used.
  snapshot_sha256: df365746088e309661613adb0392ec7c3d4623065d5a708cd0417ba97e29f117
- evidence_id: patents
  kind: primary_source
  reference: CN101991578A; TW200938215A; FR2963553A3
  locator: Original patent abstract/background/claims relevant to madecassic acid;
    French abstract and exact composition passages
  accessed_at: '2026-10-21T20:10:17Z'
  support: context_only
  summary: CN concerns extraction and alpha-glucosidase-inhibitor use; claims specify
    separated acids above95% purity. TW concerns antiglycation by the acids or extracts.
    FR concerns a multicomponent hydration/anti-inflammatory cosmetic formulation
    containing madecassic acid. These are related document links, not parent-compound
    bacterial target or clinical efficacy evidence. FR resolves as A3, whereas guessed
    A1/B1 routes failed; legal status and unrelated examples were not audited.
  snapshot_sha256: b4ae6f36dabcb01c609d140e6d2c727384e722c73b906e4ad86182260d07d204
- evidence_id: adopted22816768
  kind: primary_source
  reference: PMID:22816768; DOI:10.1021/jf302529x
  locator: Complete original indexed abstract in619-adopted.json
  accessed_at: '2026-10-21T20:10:17Z'
  support: context_only
  summary: Dietary triterpene absorption and antioxidant effects, not a bacterial
    assay. Full original methods were not assessed for this adopted lead.
  snapshot_sha256: 08f7790e1625e95ac87a6860e3d2719ec7e69caeeb3abd32225a47b36ca0137c
- evidence_id: adopted22966846
  kind: primary_source
  reference: PMID:22966846; DOI:10.3109/13880209.2012.685946
  locator: Complete original indexed abstract in619-adopted.json
  accessed_at: '2026-10-21T20:10:17Z'
  support: context_only
  summary: Centella asiatica HPLC profiles by plant part and harvest, a source-occurrence
    lead. Full original methods were not assessed for this adopted lead.
  snapshot_sha256: 08f7790e1625e95ac87a6860e3d2719ec7e69caeeb3abd32225a47b36ca0137c
- evidence_id: adopted23346217
  kind: primary_source
  reference: PMID:23346217; DOI:10.1155/2012/848093
  locator: Complete original indexed abstract in619-adopted.json
  accessed_at: '2026-10-21T20:10:17Z'
  support: context_only
  summary: Burn-wound healing comparison; glycosides and aglycones are distinct materials.
    Full original methods were not assessed for this adopted lead.
  snapshot_sha256: 08f7790e1625e95ac87a6860e3d2719ec7e69caeeb3abd32225a47b36ca0137c
- evidence_id: adopted24965394
  kind: primary_source
  reference: PMID:24965394
  locator: Complete original indexed abstract in619-adopted.json
  accessed_at: '2026-10-21T20:10:17Z'
  support: context_only
  summary: CT26 mouse colon-cancer apoptosis/immunomodulation, not bacterial inhibition.
    Full original methods were not assessed for this adopted lead.
  snapshot_sha256: 08f7790e1625e95ac87a6860e3d2719ec7e69caeeb3abd32225a47b36ca0137c
- evidence_id: adopted25685908
  kind: primary_source
  reference: PMID:25685908; DOI:10.3390/molecules20023001
  locator: Complete original indexed abstract in619-adopted.json
  accessed_at: '2026-10-21T20:10:17Z'
  support: context_only
  summary: Zebrafish metabolism, not a bacterial mechanism. Full original methods
    were not assessed for this adopted lead.
  snapshot_sha256: 08f7790e1625e95ac87a6860e3d2719ec7e69caeeb3abd32225a47b36ca0137c
- evidence_id: adopted26633490
  kind: primary_source
  reference: PMID:26633490; DOI:10.3390/nu7125512
  locator: Complete original indexed abstract in619-adopted.json
  accessed_at: '2026-10-21T20:10:17Z'
  support: context_only
  summary: Diabetic mouse effects of madecassic and rotundic acids, not antibacterial
    evidence. Full original methods were not assessed for this adopted lead.
  snapshot_sha256: 08f7790e1625e95ac87a6860e3d2719ec7e69caeeb3abd32225a47b36ca0137c
- evidence_id: adopted27728894
  kind: primary_source
  reference: PMID:27728894; DOI:10.1016/j.biopha.2016.10.015
  locator: Complete original indexed abstract in619-adopted.json
  accessed_at: '2026-10-21T20:10:17Z'
  support: context_only
  summary: Hypoxic retinal-cell ROS/ER-stress effects, a host endpoint. Full original
    methods were not assessed for this adopted lead.
  snapshot_sha256: 08f7790e1625e95ac87a6860e3d2719ec7e69caeeb3abd32225a47b36ca0137c
- evidence_id: adopted28358365
  kind: primary_source
  reference: PMID:28358365; DOI:10.1038/cddis.2017.150
  locator: Complete original indexed abstract in619-adopted.json
  accessed_at: '2026-10-21T20:10:17Z'
  support: context_only
  summary: Host colitis/PPARgamma-AMPK pathway, not a bacterial protein target. Full
    original methods were not assessed for this adopted lead.
  snapshot_sha256: 08f7790e1625e95ac87a6860e3d2719ec7e69caeeb3abd32225a47b36ca0137c
- evidence_id: adopted30324102
  kind: primary_source
  reference: PMID:30324102; DOI:10.3389/fchem.2018.00434
  locator: Complete original indexed abstract in619-adopted.json
  accessed_at: '2026-10-21T20:10:17Z'
  support: context_only
  summary: Modified derivatives5,12,17 and host ERK/BRAF outcomes are not parent-compound
    bacterial results. Full original methods were not assessed for this adopted lead.
  snapshot_sha256: 08f7790e1625e95ac87a6860e3d2719ec7e69caeeb3abd32225a47b36ca0137c
- evidence_id: adopted30679477
  kind: primary_source
  reference: PMID:30679477; DOI:10.1038/s41598-018-36555-1
  locator: Complete original indexed abstract in619-adopted.json
  accessed_at: '2026-10-21T20:10:17Z'
  support: context_only
  summary: Murtilla extract and isolated madecassic acid insulin/endothelial outcomes
    have distinct material and host scopes. Full original methods were not assessed
    for this adopted lead.
  snapshot_sha256: 08f7790e1625e95ac87a6860e3d2719ec7e69caeeb3abd32225a47b36ca0137c
- evidence_id: activity2023
  kind: primary_source
  reference: PMID:36838882; DOI:10.3390/molecules28041895; PMC9967526
  locator: Complete main text and tables; Methods4.1–4.3; actual Figure16 viewed
  accessed_at: '2026-10-21T20:10:17Z'
  support: supports
  summary: Madecassic acid from Shanghai Yuanye, lotJ12HB184580 and >98% HPLC purity,
    was tested in a TTC microdilution assay with10^6–10^7 CFU/mL suspension,37C for12–16h
    plus4h TTC development. Text MICs are S.aureus CMCC(B)26003 31.25, MRSA ATCC43300
    62.5, E.coli ATCC25922 250, P.aeruginosa ATCC27853 125, B.subtilis62.5 and B.megaterium
    ATCC35985 62.5 micrograms/mL. B.subtilis strain is not specified. Table1 rounds31.25
    to31.2 and oxacillin0.048 to0.0; retain text precision and assay context before
    numerical curation. Figure16 visibly shows the carboxylic acid and native hydroxy
    stereochemical pattern.
  snapshot_sha256: 55e997632aaf937158d8a1e754c80750c0a7b4d3db91b0c25b145368fe05855d
- evidence_id: mechanism2023
  kind: primary_source
  reference: DOI:10.3390/molecules28041895
  locator: Full Results/Methods; actual Figures13/14 and their lane captions
  accessed_at: '2026-10-21T20:10:17Z'
  support: partial
  summary: Conductivity, extracellular nucleic-acid/protein/AKP measurements and TEM
    support envelope injury under the tested conditions. Soluble-protein bands and
    post-treatment SDH/MDH activities do not identify direct protein binding. Topoisomerase
    assays use crude S.aureus extract and pET-28a, with altered relaxation patterns
    at mg/mL concentrations; the article also reports DNA changes without enzyme.
    These experiments do not establish selective binding to purified TopA or gyrase.
    The actual gels were viewed without independent densitometry.
  snapshot_sha256: 55e997632aaf937158d8a1e754c80750c0a7b4d3db91b0c25b145368fe05855d
- evidence_id: bd2026
  kind: primary_source
  reference: PMID:41574235; DOI:10.1039/d5md01116g; PMC12822377
  locator: Complete main XML, Results/Methods and open author PDF; actual Figures1/2
    at printedp1516 viewed; supplementary data not recovered
  accessed_at: '2026-10-21T20:10:17Z'
  support: partial
  summary: Centella-derived madecassic acid inhibits oxygen consumption in E.coli
    EC958 bd-I-only membranes, IC50 34±11 micromolar, and growth, IC50 9.4±1.5 micromolar
    with63% maximum inhibition. Wild-type growth has approximately10 micromolar IC50
    and48% maximum inhibition. The parent viability curve shows little change below
    1 mM, but its 1 mM point is near log10(survival percent)=0, versus approximately2
    at baseline. This conflicts with categorical no-killing language in the main text;
    no universal absence of killing or exact MBC is inferred. DerivativeMA-4 results
    remain separate. Membrane assays use0.5mg/mL wet membranes,8mM succinate,37C,15–20min;
    growth uses glycerol/casamino-acid M9 and DMSO. Docking-derived Kd1.14 micromolar
    is computational, not measured affinity. Main text reports complementary SDH and
    duroquinol controls in EcoM4 pSU2718G-cydABX-his6 membranes, including loss of
    bd-I oxygen consumption at 1 mM; underlying supplementary figures/raw data were
    not inspected. Binding-site specificity remains modeled.
  snapshot_sha256: cc948b3130abf83906d6aee0c26cf4e732748f11076617906956de8e81802d9a
- evidence_id: kp2026
  kind: primary_source
  reference: PMID:41619992; DOI:10.1016/j.micpath.2026.108332
  locator: Complete original indexed abstract only
  accessed_at: '2026-10-21T20:10:17Z'
  support: context_only
  summary: Exact PT-5 madecassic acid had negligible bactericidal action against KP31
    but reduced quorum-sensing/virulence-associated phenotypes and enhanced antibiotics
    at32 micrograms/mL. Gene-expression changes and a larval combination model are
    not direct protein binding or human efficacy. Full strain/material/assay methods
    were not recovered.
  snapshot_sha256: 9ed38838e67f8c1aad626c8b8c3def3a71b3aeadb013f4e7cb18ee7ab717773d
- evidence_id: adapter
  kind: database
  reference: kg-microbe-sources iModulonDB e_coli/precise1k
  locator: Catalog and actual cydA/topA/gyrB queries before new mechanism-paper follow-up
  accessed_at: '2026-10-21T20:10:17Z'
  support: context_only
  summary: The native record names no protein mechanism. New primary leads prompted
    E.coli queries resolving cydA b0733, topA b1274 and gyrB b3699; no iModulons were
    returned. These reference-gene results are naming context, not EC958 or S.aureus
    assay evidence, and cannot prove inhibition.
  snapshot_sha256: 5b24a9153d416937a28a1602df52d1db1a31d2a32749cf1c45d959eb11f7d3fa
- evidence_id: search
  kind: search
  reference: Europe PMC TITLE_ABS:"madecassic acid"
  locator: All first100 titles of204 results read, followed by exact adopted and selected
    antibacterial originals
  accessed_at: '2026-10-21T20:10:17Z'
  support: context_only
  summary: Search recovered primary bacterial experiments alongside derivatives, extract
    and host studies. All ten adopted abstracts and selected2023/2026 originals have
    explicit depth limits. No exhaustive absence claim or uninspected-source mechanism
    is made.
  search_scope: 2026-10-21; exact native identity and ten adopted PMIDs; first100/204
    EuropePMC titles; focused free primary and official registry follow-up; local
    ignored-inclusive inventory retained.
  snapshot_sha256: 9ed38838e67f8c1aad626c8b8c3def3a71b3aeadb013f4e7cb18ee7ab717773d
assessments:
- assessment_id: identity
  area: identity
  topic: Exact native structure and names
  outcome: supported
  summary: The native neutral thirteen-centre ursane-derived acid agrees with current
    ChEBI/PubChem and the original2023 drawing. No native wrong-isomer finding is
    justified.
  target_ids:
  - CHEBI:73058
  evidence_ids:
  - native
  - chebi
  - chemistry
  - activity2023
- assessment_id: grounding
  area: grounding
  topic: Exact external associations
  outcome: concern
  summary: KNApSAcK has mutually incompatible encodings. HMDB and LIPID MAPS carry
    two unassigned native centres, so exact stereochemical equivalence is not established.
    Other restricted references remain explicit limitations.
  target_ids:
  - CHEBI:73058
  evidence_ids:
  - knapsack
  - lipidmaps
  - hmdb
  - chemistry
  - restricted
- assessment_id: activity
  area: evidence
  topic: Antibacterial classification and exact-material scope
  outcome: supported
  summary: Primary2023 growth inhibition and2026 E.coli experiments support the antibacterial
    role. Extracts, derivatives, host effects and quorum-sensing endpoints remain
    separate.
  target_ids:
  - CHEBI:73058
  evidence_ids:
  - activity2023
  - bd2026
  - kp2026
  - parents
- assessment_id: mechanism
  area: evidence
  topic: Envelope, crude topoisomerase and respiratory evidence
  outcome: unknown
  summary: The papers support bounded cellular and membrane-functional effects. Crude
    extracts and computational affinities do not prove selective direct binding; no
    mandatory missing target object is inferred.
  target_ids:
  - CHEBI:73058
  evidence_ids:
  - mechanism2023
  - bd2026
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Adopted sources, reference links and generated history
  outcome: supported
  summary: All native fields and ten adopted abstracts were assessed; patents resolve
    as related documents. Thirteen original inputs and generated-file boundaries are
    preserved.
  target_ids:
  - CHEBI:73058
  evidence_ids:
  - native
  - local
  - patents
  - adopted22816768
  - adopted22966846
  - adopted23346217
  - adopted24965394
  - adopted25685908
  - adopted26633490
  - adopted27728894
  - adopted28358365
  - adopted30324102
  - adopted30679477
- assessment_id: completeness
  area: completeness
  topic: Bounded optional curation
  outcome: unknown
  summary: Exact-strain activity and qualified respiratory/envelope evidence can support
    later curation. Restricted registries, supplementary controls and raw measurements
    remain unverified; optional omissions are not findings.
  target_ids:
  - CHEBI:73058
  evidence_ids:
  - activity2023
  - bd2026
  - restricted
  - search
findings:
- finding_id: F1
  issue_key: madecassic-acid-knapsack-inconsistent-structure-descriptors
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: KNApSAcK exact accession has conflicting constitutional encodings
  description: C00051418 has a correct native InChI but a formate-ester SMILES and
    a third displayed key. Exact grounding must resolve the internal disagreement;
    a matching name or formula is insufficient. Do not replace the correct native
    acid with the incompatible SMILES.
  target_ids:
  - CHEBI:73058
  field_paths:
  - xrefs[2]
  evidence_ids:
  - native
  - knapsack
  - chemistry
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
  rule_id: Exact xrefs must denote the same structure including stereochemistry
  normalization_reason: Material external-grounding conflict is major; independently
    corroborated native chemical identity is not a blocker.
- finding_id: F2
  issue_key: madecassic-acid-hmdb-lipidmaps-incomplete-stereochemistry
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two asserted exact registries omit two native stereocentres
  description: HMDB0036670 displayed molfile and LMPR0106180009 actual encodings leave
    Standard InChI centres21 and23 unassigned. Remaining assigned centres and constitution
    agree, so these are incomplete stereo representations, not proven opposite epimers.
    The native exact xrefs overstate the verified structure equivalence.
  target_ids:
  - CHEBI:73058
  field_paths:
  - xrefs[1]
  - xrefs[3]
  evidence_ids:
  - native
  - hmdb
  - lipidmaps
  - chemistry
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
  rule_id: Exact xrefs must denote the same structure including stereochemistry
  normalization_reason: Material external-grounding conflict is major; independently
    corroborated native chemical identity is not a blocker.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - CHEBI:73058
  description: Resolve or qualify the affected exact association through maintained
    ChEBI source handling and regenerate.
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
  generator: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  acceptance_checks:
  - Compare actual SMILES, InChI and molfile graphs, including every native stereocentre;
    preserve internal provider conflicts rather than accepting a displayed label/key
    alone.
  - Retain the native acid and its primary activity. Do not infer an opposite epimer
    from missing stereo or substitute a formate ester.
  - Regenerate through maintained inputs and rerun focused schema/strict/chemistry,
    corpus reproduction and required shared gates.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - CHEBI:73058
  description: Resolve or qualify the affected exact association through maintained
    ChEBI source handling and regenerate.
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
  generator: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  acceptance_checks:
  - Compare actual SMILES, InChI and molfile graphs, including every native stereocentre;
    preserve internal provider conflicts rather than accepting a displayed label/key
    alone.
  - Retain the native acid and its primary activity. Do not infer an opposite epimer
    from missing stereo or substitute a formate ester.
  - Regenerate through maintained inputs and rerun focused schema/strict/chemistry,
    corpus reproduction and required shared gates.
limitations:
- All ten adopted papers were read at complete-abstract depth, with no full-method
  claim for those leads. The2023 and2026 respiratory main texts were read in full;
  the2026 KP31 lead is abstract-only.
- HMDB assessment uses the complete initially web-displayed2D molfile only; subsequent
  direct requests failed. Its remaining chemical fields are not independently verified.
  CAS, Reaxys and DrugBank remain restricted or shell-only.
- The2026 respiratory supplement was not recovered; control experiments are known
  from main-text reporting, not independent inspection of supplementary figures. Computational
  Kd is not measured binding. Raw assay data and spectra were not reprocessed.
- Patent reading was limited to compound-relevant abstracts/background/claims/composition,
  without legal-status assessment or transfer of mixture/host results to bacterial
  activity.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Native data, source inputs and status/history were not edited. Chemistry used the
  isolated019 RDKit interpreter against062; schema/strict checks used062.
- The initial LIPID MAPS /mol response was a text error, PMC pages sometimes returned
  challenge HTML, and guessed FR A1/B1 URLs failed. Actual /molfile, FR A3, EuropePMC
  XML and author-repository PDF were used after inspecting response contents.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
