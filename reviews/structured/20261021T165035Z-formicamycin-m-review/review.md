# Formicamycin M: reproducible seeded hypothesis with unresolved exact-compound experimental support

- Review: 20261021T165035Z-formicamycin-m-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:37:18Z
- Finished UTC: 2026-10-21T16:50:35Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The complete native record and its actual ARO/PubChem sources reproduce a consistent inferred formicamycin M graph. The original discovery explicitly reports M as MS-only, without isolation, and its activity and resistance experiments concern other congeners. One informational finding distinguishes permitted database seed admission from unresolved exact-M experimental sign-off. No inactivity, wrong constitution or mandatory exclusion is inferred. A standalone mass-tolerance failure is retained transparently alongside passing schema, strict and graph-equivalence checks. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 468; one complete exact M record, independently distinguished from L and from fasamycin M. All thirteen initial hashes were verified before assessment and preserved; actual ARO/PubChem owners were appended, yielding sixteen captured inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-4fcd06e09d | data/antibiotics/antibacterial/formicamycin-m.yaml | generated | formicamycin M |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | antibioticmech:aro-4fcd06e09d | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-4fcd06e09d | Actual focused execution exited 0. |
| Focused chemistry verification | failed | False | antibioticmech:aro-4fcd06e09d | The optional standalone diagnostic exits 1 solely because native/current PubChem average_mass 597.4 differs from RDKit 597.458 by 0.058, exceeding its 0.05 tolerance. Both native encodings parse and match the key, formula, charge, monoisotopic mass and source mint. The failed result is retained, not rewritten as a pass. |
| Independent current authority graph comparison | passed | False | antibioticmech:aro-4fcd06e09d | Native SMILES/InChI, ChEBI molfile and exact-CID PubChem graph all reproduce the same full key, formula, neutral charge and two R tetrahedral centres. This graph comparison does not resolve the separate average-mass precision difference. |
| Authoritative full QC | failed | True | antibioticmech:aro-4fcd06e09d | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-4fcd06e09d | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-4fcd06e09d | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-4fcd06e09d | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-4fcd06e09d | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-4fcd06e09d | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-4fcd06e09d | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-4fcd06e09d | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-4fcd06e09d | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Represented M hypothesis versus experimental identity

identity: supported. Targets: antibioticmech:aro-4fcd06e09d.

The stored encodings consistently represent the original proposed M structure and agree across chemical authorities. The only direct M analytical result located is high-resolution MS/formula, so exact natural-product regiochemistry and absolute configuration remain experimentally unresolved. This is not proof that the proposed graph is wrong.

### Mass fields and diagnostic limits

identity: unknown. Targets: antibioticmech:aro-4fcd06e09d.

Formula, charge, exact mass and full key agree. The 597.4 versus 597.458 average-mass difference is reproduced across PubChem versus ChEBI/RDKit and triggers the optional helper. The precise source calculation/precision cause remains unresolved; it is not used to infer a different chemical identity.

### Permitted database seed and explicit family wording

provenance: supported. Targets: antibioticmech:aro-4fcd06e09d.

The native record faithfully represents an ARO-classified antibiotic candidate with a single proposed structure, and its status remains SEEDED. CARD-based seed admission is allowed by documented policy. The definition speaks of congeners, so a missing exact-M test is not reinterpreted as a false native numerical observation.

### Exact-M structural, antibacterial and selection-barrier validation

evidence: unknown. Targets: antibioticmech:aro-4fcd06e09d.

The inspected primary evidence does not establish an isolated exact-M sample, exact-M antibacterial assay or exact-M serial-exposure result. Later same-letter fasamycin results and other formicamycin congeners cannot fill that gap. Scientific sign-off is therefore unresolved even though the seeded proposal is reproducible.

### Optional targets, resistance, producer and clinical claims

completeness: supported. Targets: antibioticmech:aro-4fcd06e09d.

The record contains no native named gene/protein/pathway or expression dataset requiring a structured adapter lookup. General resistant-organism wording is not a transcriptomic assertion. Biosynthetic regulation and proposed self-resistance are not promoted to antibacterial binding/causal mechanisms. Missing optional objects are not counted as defects.

## Findings

### F1: Keep the MS-inferred M proposal distinct from an experimentally validated antimicrobial

informational / open / confirmed; issue key: formicamycin-m-ms-only-experimental-signoff.

The 2017 original positively reports M (16) as an MS-detected, structurally inferred congener, explicitly without isolation. Its activity table covers 1–15 and selection tests use 6, 13 and 15. The adopted 2021 source supplies family context and tests other exact compounds. The bounded later-primary search did not establish isolated M material or an exact-M activity experiment. Because native status is SEEDED, the definition is family-qualified and CARD seed admission is permitted, this is a scientific-sign-off question rather than a demonstrated wrong identity, inactivity claim or mandatory exclusion.

## Recommended Actions And Acceptance Checks

### A1

Resolve or explicitly retain the experimental uncertainty before promoting exact formicamycin M to scientific sign-off.

- Find and inspect primary evidence linking an isolated or independently characterized exact-M material to the proposed graph and an antimicrobial assay, or preserve a curator-owned discussion explicitly stating the current MS-inferred and untested scope. Do not transfer L (15), fasamycin M or generic family results.
- Retain the source database assertion and SEEDED provenance unless a separately justified source/eligibility decision is made. Any future structural or class correction belongs in maintained source ownership, followed by regeneration and focused schema/strict, identity and corpus reproduction checks; no exclusion follows solely from this bounded search.
- Before future numerical sign-off, reconcile the average-mass source convention or document why the low-precision PubChem value is retained. Keep the actual standalone diagnostic result visible.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/formicamycin-m.yaml; Entire native YAML, including definition/source, parent/class, full structure, all three exact cross-references, source concept and three history events. | supports | The SEEDED, MINTED record denotes formicamycin M as neutral C30H29BrO8, key KHXIDNHTRXJJNS-YKGWIAGDSA-N. Its definition explicitly speaks of formicamycin congeners and cites PMID 33440167. ARO:3005171 is the broader parent and structural class. No synonyms, exact-M MIC, specific target, resistance determinant, producer object, clinical assertion, expression dataset or causal graph is asserted. The history records only source seeding and reseeding. |
| owners | data/raw/aro_antibiotics.tsv:473; data/raw/pubchem_structures.tsv:184; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py; Complete maintained ARO/PubChem rows and applicable extraction, classification, structure-fallback, definition and emission code. | supports | The ARO row supplies the family definition, single adopted PMID, structural class and cross-references. PubChem supplies the inferred graph, mass fields and 2026-08-29 retrieval date. The source mint antibioticmech:aro-4fcd06e09d reproduces. No exact adopted ChEBI, target/resistance, FDA or MIBiG owner row was found. The initial default ChEBI owner was corrected to actual ARO/PubChem ownership without replacing any of the thirteen original hashes. Current ChEBI identity availability alone is not a defect in the frozen MINTED source state. |
| authority | ARO:3007586; CHEBI:219506; pubchem.compound:146684593; Complete current official ARO term, ChEBI entry/molfile and PubChem properties; four independently parsed graph encodings. | supports | ARO identifies M and repeats the family definition, PMID 33440167 and both chemical cross-references. Current ChEBI and PubChem, native SMILES and native InChI all encode the same neutral constitutional and assigned R,R graph, giving KHXIDNHTRXJJNS-YKGWIAGDSA-N. The structure matches the original proposed M drawing with a single bromine at C22 and no chlorines. Database agreement supports reproducible representation of the proposal; it does not independently prove that the MS-detected biological material has every drawn regiochemical or stereochemical feature. No conflicting exact external graph was found. |
| mass | pubchem.compound:146684593; CHEBI:219506; https://pubchem.ncbi.nlm.nih.gov/docs/atomic-mass-changes-2016; https://pubchem.ncbi.nlm.nih.gov/rest/pug/periodictable/JSON; Native/current chemical-property comparison, standalone RDKit diagnostic and official PubChem mass-convention explanation. | partial | Native and current PubChem both report average mass 597.4. ChEBI and RDKit give 597.458, while all sources agree on formula and monoisotopic mass 596.10458. The optional helper’s 0.05 average-mass tolerance therefore fails by 0.008. PubChem documents use of conventional atomic weights and limited precision, but the exact cause of this particular 0.058 difference was not established; the current periodic-table values alone do not reproduce a simple one-decimal rounding to 597.4. This small unresolved property-convention discrepancy is retained without claiming a different molecule or silently declaring every chemical check passed. |
| policy-class | docs/HARMONIZATION.md:244; .claude/skills/curate-yaml-record/references/review-checklist.md; ARO:3005171; Seed-admission and scientific-review rules plus the official structural-class term. | supports | The harmonization policy explicitly permits CARD’s antibiotic assertion as evidence for seed admission. The checklist separately requires precise claim scope and warns against inferring activity solely from a chemical family. The native status is SEEDED and its definition is family-qualified; it does not claim an exact-M primary MIC or REVIEWED sign-off. The asserted polyketide class is compatible with the proposed scaffold, while its experimentally antibacterial character for M remains unresolved. These distinctions support an informational follow-up rather than an unsupported inactivity or exclusion finding. |
| discovery | PMID:28507698; DOI:10.1039/C6SC04265A; https://pmc.ncbi.nlm.nih.gov/articles/PMC5414599/; Complete original main text, Figure 1 independently viewed, exact M supplementary entry p. 54 visually inspected, and isolation/activity/resistance Methods. | partial | Figure 1 maps M to compound 16. Growth of S. formicae KY5 with 2 mM sodium bromide yielded brominated metabolites 14–16; the Results explicitly state that 16 was detected only by MS owing to low production and its structure was inferred. The supplement gives C30H29O8Br and observed [M+H]+ 597.1120 versus calculated 597.1119, with no isolated yield or M NMR assignment. Mass/formula support a brominated candidate but cannot alone establish the complete drawn regio- and stereochemistry. The broad abstract language about sixteen molecules is narrowed by these explicit Results and supplemental details. |
| assay-boundary | PMID:28507698; DOI:10.1039/C6SC04265A; Original Table 1, assay Results and supplementary p. 56. | context_only | Table 1 and the MIC Results explicitly cover compounds 1–15, not M (16). Serial MRSA exposure tests use compounds 6, 13 and 15. Thus neither the MRSA/VRE MICs of L (15) nor its resistance-selection outcome is direct evidence for M (16). The original paper reports a positive MS-based candidate identity, not a negative antibacterial test for M. No universal inactivity conclusion follows. |
| adopted | PMID:33440167; DOI:10.1016/j.chembiol.2020.12.011; https://pmc.ncbi.nlm.nih.gov/articles/PMC8062789/; Complete adopted abstract; Introduction, new-congener Results/Table 2, Discussion/Significance and congener-analysis/bioassay Methods. | context_only | The adopted 2021 paper describes biosynthetic regulation and cites the 2017 discovery for family antibacterial activity and the selection barrier. Table 2’s L and M measurements belong to fasamycins, while the formicamycin columns are J, R and S. Those data do not close the exact formicamycin-M gap. Biosynthetic regulators and putative export/self-resistance pathways are not demonstrated antibacterial targets or measured resistance mechanisms for M. The native definition’s explicit family wording remains consistent with this source. |
| followup2019 | DOI:10.1038/s41467-019-11538-6; https://pmc.ncbi.nlm.nih.gov/articles/PMC6689052/; Complete abstract and original metabolomic-discovery/isolation/biological-activity Results. | context_only | The 2019 study investigates nitrogen-containing formicapyridines and additional biosynthetic products. Its bromide-induced trace candidates and its negative/weak antibacterial tests concern formicapyridine compounds numbered within that paper, not formicamycin M. No exact-M isolation, NMR or activity result was identified in the inspected sections, and the compound numbers are not transferred between papers. |
| followup2020 | PMID:33033611; DOI:10.1039/D0SC01712D; https://pmc.ncbi.nlm.nih.gov/articles/PMC7504897/; Complete abstract and original mutational-analysis/biomimetic-semisynthesis Results. | context_only | The 2020 work addresses lactone intermediates, ForX/ForY-dependent transformations and reduced synthetic products. Its congener numbers and stereoisomeric mixtures belong to those specific products; they do not establish that natural M is a mixture or provide an isolated M assay. No exact-M experiment was identified in the inspected Results. |
| revision2026 | PMID:41988676; DOI:10.1021/acs.jnatprod.6c00145; https://pmc.ncbi.nlm.nih.gov/articles/PMC13532170/; Main abstract and relevant axial-configuration/regiochemical-revision Results; Table 1 and revised-structure figure independently viewed. | context_only | Table 1 measures formicamycins G, H, I, J, R and S, not M. The explicit formicamycin methoxy-regiochemistry corrections concern B, D and I. A broader Sa axial proposal is an inference beyond those exact measured congeners. The observed M proposal has both hanging-ring methoxy groups, so the single-methoxy correction is not automatically applicable. No exact M crystal/NMR confirmation was established by this source assessment. |
| search | 468-inclusive-hits.txt; 468-exact-literature.json; 468-key-literature.json; 468-bromine-literature.json; 468-followup-exact-search.json; 467-literature.json; Hidden- and ignored-inclusive native/source search; bounded exact-name, key, brominated-family and primary-reference follow-up. | context_only | The local search finds the exact native/ARO/PubChem rows and readiness/index products, without a separate exact-M primary-data overlay. Europe PMC literal exact-name/key/brominated title-abstract queries returned no hits, despite the known original M report being available in full text, demonstrating that these misses are not evidence of biological absence. Broader family queries and web exact-name searches recovered the 2017 original, 2019/2020/2021 biosynthesis work and 2026 revision. Parsed full XML text of those four later studies was searched with word boundaries for the exact name, formula/mass and key; no exact-M result was identified. Search snippets and a later secondary review are leads only. |
| checks | 468-focused-results.json; 468-chemistry.json; 468-authority-chemistry.json; Actual schema/strict and chemical executions, with initial hashes rechecked. | supports | Schema and strict validators exit 0. The standalone diagnostic exits 1 solely on average-mass tolerance; independent graph equivalence exits 0. Original thirteen input hashes remain unchanged within the sixteen-input capture. No failed output is replaced or misreported as a successful native chemistry pass. |

## Limits And Additional Notes

- No isolated exact-M sample, M-specific NMR/crystal experiment or M-specific antibacterial test was established in the inspected originals. The finding is bounded to the identified source trail and public searches, not a statement that no such evidence exists anywhere.
- The original proposed M graph has a single bromine and assigned R,R centres, but its own direct analytical evidence is mass/formula only. Family-based stereochemical inference and database agreement are not independent experimental verification; unspecified axial information is not evidence of a mixture.
- The 2019, 2020, 2021 and 2026 follow-up papers were read at the exact sections stated. Their complete raw supplemental datasets were not reprocessed. Shared compound numbers and fasamycin/formicamycin names were kept distinct.
- The optional standalone chemical diagnostic failed only on the 0.058 average-mass difference between PubChem/native and ChEBI/RDKit. Public mass-convention documentation did not establish the exact numerical cause, so this discrepancy remains unresolved rather than silently normalized. Graph, formula, charge, monoisotopic mass and mint consistency were independently confirmed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- This is a partial scientific review of the seeded hypothesis and its source limits. It does not constitute scientific REVIEWED sign-off or assert that M lacks antibacterial activity.
- The review contract does not allow a seed_only verdict with scientific_review true; pass_with_limitations here describes the bounded review outcome while the assessments explicitly preserve the distinction between database admission and unresolved exact-M validation.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T165035Z-formicamycin-m-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Formicamycin M: reproducible seeded hypothesis with unresolved exact-compound
  experimental support'
started_at: '2026-10-21T16:37:18Z'
finished_at: '2026-10-21T16:50:35Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. The entire record
    and maintained source were read, independent chemistry calculated, asserted chemical
    groundings checked and exact-compound primary literature assessed with explicit
    access boundaries.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The complete native record and its actual ARO/PubChem sources reproduce a
  consistent inferred formicamycin M graph. The original discovery explicitly reports
  M as MS-only, without isolation, and its activity and resistance experiments concern
  other congeners. One informational finding distinguishes permitted database seed
  admission from unresolved exact-M experimental sign-off. No inactivity, wrong constitution
  or mandatory exclusion is inferred. A standalone mass-tolerance failure is retained
  transparently alongside passing schema, strict and graph-equivalence checks. Scientific
  assessment retains the stated evidence limits; full verification is blocked by the
  shared native-library failure.
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
  - path: data/antibiotics/antibacterial/formicamycin-m.yaml
    sha256: 17ec2d39683631944084f1ad5394f366001c8d883b3608e79781f4824dfa6e76
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/chebi_antimicrobials.tsv
    sha256: 4c33e56c3c342be657309f720f5b5cb9cad1fae13bec202ef99e449503c32004
    role: context
  - path: data/raw/chebi_role_names.tsv
    sha256: 5c476c0aacd7c98d7241d2343a6fc41ee9eb9338077404c5b011a04bf40c6ac5
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
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
- target_id: antibioticmech:aro-4fcd06e09d
  path: data/antibiotics/antibacterial/formicamycin-m.yaml
  label: formicamycin M
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction and class mapping
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
    path: data/raw/pubchem_structures.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Actual maintained source input for the record
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 468; one complete exact M record, independently distinguished
    from L and from fasamycin M. All thirteen initial hashes were verified before
    assessment and preserved; actual ARO/PubChem owners were appended, yielding sixteen
    captured inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-4fcd06e09d
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-4fcd06e09d
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/formicamycin-m.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-4fcd06e09d
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/formicamycin-m.yaml --out /private/tmp/am-review-session/468-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: failed
  required: false
  summary: The optional standalone diagnostic exits 1 solely because native/current
    PubChem average_mass 597.4 differs from RDKit 597.458 by 0.058, exceeding its
    0.05 tolerance. Both native encodings parse and match the key, formula, charge,
    monoisotopic mass and source mint. The failed result is retained, not rewritten
    as a pass.
  target_ids:
  - antibioticmech:aro-4fcd06e09d
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 468
  exit_code: 1
  expected_exit_code: 0
- check_id: authority-graph
  name: Independent current authority graph comparison
  status: passed
  required: false
  summary: Native SMILES/InChI, ChEBI molfile and exact-CID PubChem graph all reproduce
    the same full key, formula, neutral charge and two R tetrahedral centres. This
    graph comparison does not resolve the separate average-mass precision difference.
  target_ids:
  - antibioticmech:aro-4fcd06e09d
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/468-authority-check.py
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
  - antibioticmech:aro-4fcd06e09d
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
  - antibioticmech:aro-4fcd06e09d
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
  - antibioticmech:aro-4fcd06e09d
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
  - antibioticmech:aro-4fcd06e09d
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
  - antibioticmech:aro-4fcd06e09d
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
  - antibioticmech:aro-4fcd06e09d
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
  - antibioticmech:aro-4fcd06e09d
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
  - antibioticmech:aro-4fcd06e09d
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
  - antibioticmech:aro-4fcd06e09d
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/formicamycin-m.yaml
  locator: Entire native YAML, including definition/source, parent/class, full structure,
    all three exact cross-references, source concept and three history events.
  accessed_at: '2026-10-21T16:48:19Z'
  support: supports
  summary: The SEEDED, MINTED record denotes formicamycin M as neutral C30H29BrO8,
    key KHXIDNHTRXJJNS-YKGWIAGDSA-N. Its definition explicitly speaks of formicamycin
    congeners and cites PMID 33440167. ARO:3005171 is the broader parent and structural
    class. No synonyms, exact-M MIC, specific target, resistance determinant, producer
    object, clinical assertion, expression dataset or causal graph is asserted. The
    history records only source seeding and reseeding.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv:473; data/raw/pubchem_structures.tsv:184;
    conf/sources.yaml; scripts/extract_source_inventory.py; scripts/enrich_pubchem_structures.py;
    scripts/seed_from_sources.py
  locator: Complete maintained ARO/PubChem rows and applicable extraction, classification,
    structure-fallback, definition and emission code.
  accessed_at: '2026-10-21T16:48:19Z'
  support: supports
  summary: The ARO row supplies the family definition, single adopted PMID, structural
    class and cross-references. PubChem supplies the inferred graph, mass fields and
    2026-08-29 retrieval date. The source mint antibioticmech:aro-4fcd06e09d reproduces.
    No exact adopted ChEBI, target/resistance, FDA or MIBiG owner row was found. The
    initial default ChEBI owner was corrected to actual ARO/PubChem ownership without
    replacing any of the thirteen original hashes. Current ChEBI identity availability
    alone is not a defect in the frozen MINTED source state.
  snapshot_sha256: 000063ec8130283f06bfac8494ac6f2bebc61b725fa8d280ab34d89261a43b80
- evidence_id: authority
  kind: authority
  reference: ARO:3007586; CHEBI:219506; pubchem.compound:146684593
  locator: Complete current official ARO term, ChEBI entry/molfile and PubChem properties;
    four independently parsed graph encodings.
  accessed_at: '2026-10-21T16:48:19Z'
  support: supports
  summary: ARO identifies M and repeats the family definition, PMID 33440167 and both
    chemical cross-references. Current ChEBI and PubChem, native SMILES and native
    InChI all encode the same neutral constitutional and assigned R,R graph, giving
    KHXIDNHTRXJJNS-YKGWIAGDSA-N. The structure matches the original proposed M drawing
    with a single bromine at C22 and no chlorines. Database agreement supports reproducible
    representation of the proposal; it does not independently prove that the MS-detected
    biological material has every drawn regiochemical or stereochemical feature. No
    conflicting exact external graph was found.
  snapshot_sha256: c974e1984a81ddff0e9b4327151498ccbea232b1742b8263993256e9836ffeb1
- evidence_id: mass
  kind: authority
  reference: pubchem.compound:146684593; CHEBI:219506; https://pubchem.ncbi.nlm.nih.gov/docs/atomic-mass-changes-2016;
    https://pubchem.ncbi.nlm.nih.gov/rest/pug/periodictable/JSON
  locator: Native/current chemical-property comparison, standalone RDKit diagnostic
    and official PubChem mass-convention explanation.
  accessed_at: '2026-10-21T16:48:19Z'
  support: partial
  summary: Native and current PubChem both report average mass 597.4. ChEBI and RDKit
    give 597.458, while all sources agree on formula and monoisotopic mass 596.10458.
    The optional helper’s 0.05 average-mass tolerance therefore fails by 0.008. PubChem
    documents use of conventional atomic weights and limited precision, but the exact
    cause of this particular 0.058 difference was not established; the current periodic-table
    values alone do not reproduce a simple one-decimal rounding to 597.4. This small
    unresolved property-convention discrepancy is retained without claiming a different
    molecule or silently declaring every chemical check passed.
  snapshot_sha256: 4a65583dfc7b617c2fab20302836ab23e04c0f4b55f2f4158de1fc8f84a9f66d
- evidence_id: policy-class
  kind: record_content
  reference: docs/HARMONIZATION.md:244; .claude/skills/curate-yaml-record/references/review-checklist.md;
    ARO:3005171
  locator: Seed-admission and scientific-review rules plus the official structural-class
    term.
  accessed_at: '2026-10-21T16:48:19Z'
  support: supports
  summary: The harmonization policy explicitly permits CARD’s antibiotic assertion
    as evidence for seed admission. The checklist separately requires precise claim
    scope and warns against inferring activity solely from a chemical family. The
    native status is SEEDED and its definition is family-qualified; it does not claim
    an exact-M primary MIC or REVIEWED sign-off. The asserted polyketide class is
    compatible with the proposed scaffold, while its experimentally antibacterial
    character for M remains unresolved. These distinctions support an informational
    follow-up rather than an unsupported inactivity or exclusion finding.
- evidence_id: discovery
  kind: primary_source
  reference: PMID:28507698; DOI:10.1039/C6SC04265A; https://pmc.ncbi.nlm.nih.gov/articles/PMC5414599/
  locator: Complete original main text, Figure 1 independently viewed, exact M supplementary
    entry p. 54 visually inspected, and isolation/activity/resistance Methods.
  accessed_at: '2026-10-21T16:30:15Z'
  support: partial
  summary: Figure 1 maps M to compound 16. Growth of S. formicae KY5 with 2 mM sodium
    bromide yielded brominated metabolites 14–16; the Results explicitly state that
    16 was detected only by MS owing to low production and its structure was inferred.
    The supplement gives C30H29O8Br and observed [M+H]+ 597.1120 versus calculated
    597.1119, with no isolated yield or M NMR assignment. Mass/formula support a brominated
    candidate but cannot alone establish the complete drawn regio- and stereochemistry.
    The broad abstract language about sixteen molecules is narrowed by these explicit
    Results and supplemental details.
  snapshot_sha256: 741a682eefa78fdbcfb69b76eddd1d23df3e5bffbb60b2c7df34b51d923083d5
- evidence_id: assay-boundary
  kind: primary_source
  reference: PMID:28507698; DOI:10.1039/C6SC04265A
  locator: Original Table 1, assay Results and supplementary p. 56.
  accessed_at: '2026-10-21T16:48:19Z'
  support: context_only
  summary: Table 1 and the MIC Results explicitly cover compounds 1–15, not M (16).
    Serial MRSA exposure tests use compounds 6, 13 and 15. Thus neither the MRSA/VRE
    MICs of L (15) nor its resistance-selection outcome is direct evidence for M (16).
    The original paper reports a positive MS-based candidate identity, not a negative
    antibacterial test for M. No universal inactivity conclusion follows.
  snapshot_sha256: c30ad317fb5a4e00f304850ff2bd67d2960f7643f468e35a913bda99aca2f70d
- evidence_id: adopted
  kind: primary_source
  reference: PMID:33440167; DOI:10.1016/j.chembiol.2020.12.011; https://pmc.ncbi.nlm.nih.gov/articles/PMC8062789/
  locator: Complete adopted abstract; Introduction, new-congener Results/Table 2,
    Discussion/Significance and congener-analysis/bioassay Methods.
  accessed_at: '2026-10-21T16:29:46Z'
  support: context_only
  summary: The adopted 2021 paper describes biosynthetic regulation and cites the
    2017 discovery for family antibacterial activity and the selection barrier. Table
    2’s L and M measurements belong to fasamycins, while the formicamycin columns
    are J, R and S. Those data do not close the exact formicamycin-M gap. Biosynthetic
    regulators and putative export/self-resistance pathways are not demonstrated antibacterial
    targets or measured resistance mechanisms for M. The native definition’s explicit
    family wording remains consistent with this source.
  snapshot_sha256: e55b2fd0ccc375fd9d04e77b0102d8588ed7bab670427d6124477a3d2c38cdae
- evidence_id: followup2019
  kind: primary_source
  reference: DOI:10.1038/s41467-019-11538-6; https://pmc.ncbi.nlm.nih.gov/articles/PMC6689052/
  locator: Complete abstract and original metabolomic-discovery/isolation/biological-activity
    Results.
  accessed_at: '2026-10-21T16:44:30Z'
  support: context_only
  summary: The 2019 study investigates nitrogen-containing formicapyridines and additional
    biosynthetic products. Its bromide-induced trace candidates and its negative/weak
    antibacterial tests concern formicapyridine compounds numbered within that paper,
    not formicamycin M. No exact-M isolation, NMR or activity result was identified
    in the inspected sections, and the compound numbers are not transferred between
    papers.
  snapshot_sha256: c7b70b734a42911ebac7c32b059c7cf872de0da7bf111fc197df0f632c4d03cd
- evidence_id: followup2020
  kind: primary_source
  reference: PMID:33033611; DOI:10.1039/D0SC01712D; https://pmc.ncbi.nlm.nih.gov/articles/PMC7504897/
  locator: Complete abstract and original mutational-analysis/biomimetic-semisynthesis
    Results.
  accessed_at: '2026-10-21T16:29:46Z'
  support: context_only
  summary: The 2020 work addresses lactone intermediates, ForX/ForY-dependent transformations
    and reduced synthetic products. Its congener numbers and stereoisomeric mixtures
    belong to those specific products; they do not establish that natural M is a mixture
    or provide an isolated M assay. No exact-M experiment was identified in the inspected
    Results.
  snapshot_sha256: 912909a527dbcc7222b49324c6fb9342604ea760e40bae221c1292220b4c2efc
- evidence_id: revision2026
  kind: primary_source
  reference: PMID:41988676; DOI:10.1021/acs.jnatprod.6c00145; https://pmc.ncbi.nlm.nih.gov/articles/PMC13532170/
  locator: Main abstract and relevant axial-configuration/regiochemical-revision Results;
    Table 1 and revised-structure figure independently viewed.
  accessed_at: '2026-10-21T16:29:46Z'
  support: context_only
  summary: Table 1 measures formicamycins G, H, I, J, R and S, not M. The explicit
    formicamycin methoxy-regiochemistry corrections concern B, D and I. A broader
    Sa axial proposal is an inference beyond those exact measured congeners. The observed
    M proposal has both hanging-ring methoxy groups, so the single-methoxy correction
    is not automatically applicable. No exact M crystal/NMR confirmation was established
    by this source assessment.
  snapshot_sha256: 55796020973e571658d3a02c0080a44cff02e2bd6113dbfe0c942357eb04354d
- evidence_id: search
  kind: search
  reference: 468-inclusive-hits.txt; 468-exact-literature.json; 468-key-literature.json;
    468-bromine-literature.json; 468-followup-exact-search.json; 467-literature.json
  locator: Hidden- and ignored-inclusive native/source search; bounded exact-name,
    key, brominated-family and primary-reference follow-up.
  accessed_at: '2026-10-21T16:48:19Z'
  support: context_only
  summary: The local search finds the exact native/ARO/PubChem rows and readiness/index
    products, without a separate exact-M primary-data overlay. Europe PMC literal
    exact-name/key/brominated title-abstract queries returned no hits, despite the
    known original M report being available in full text, demonstrating that these
    misses are not evidence of biological absence. Broader family queries and web
    exact-name searches recovered the 2017 original, 2019/2020/2021 biosynthesis work
    and 2026 revision. Parsed full XML text of those four later studies was searched
    with word boundaries for the exact name, formula/mass and key; no exact-M result
    was identified. Search snippets and a later secondary review are leads only.
  search_scope: 2026-10-21; rg --no-ignore --hidden across data, curation, conf, scripts,
    src, docs, .claude, reviews and reports for ARO:3007586, formicamycin M, KHXIDNHTRXJJNS,
    CHEBI:219506, 146684593 and aro-4fcd06e09d. Europe PMC exact name/key and formicamycin
    with brominated/bromine queries plus the broader family search. Web exact formicamycin
    M isolation/antibacterial/NMR and key queries. Explicit parsed full-text search
    of PMC6689052, PMC7504897, PMC8062789 and PMC13532170 includes every nested XML
    text node, independent of filesystem ignore rules.
  snapshot_sha256: 4dbe4c38ffa2959b58dc99f8d2a2d7cb4576211c17e1e58bcd035d37182133b2
- evidence_id: checks
  kind: validation
  reference: 468-focused-results.json; 468-chemistry.json; 468-authority-chemistry.json
  locator: Actual schema/strict and chemical executions, with initial hashes rechecked.
  accessed_at: '2026-10-21T16:48:19Z'
  support: supports
  summary: Schema and strict validators exit 0. The standalone diagnostic exits 1
    solely on average-mass tolerance; independent graph equivalence exits 0. Original
    thirteen input hashes remain unchanged within the sixteen-input capture. No failed
    output is replaced or misreported as a successful native chemistry pass.
  snapshot_sha256: 1e030070a1dc237036d26a56c11855a9563442fbbca44278446ce88011e4066a
assessments:
- assessment_id: identity
  area: identity
  topic: Represented M hypothesis versus experimental identity
  outcome: supported
  summary: The stored encodings consistently represent the original proposed M structure
    and agree across chemical authorities. The only direct M analytical result located
    is high-resolution MS/formula, so exact natural-product regiochemistry and absolute
    configuration remain experimentally unresolved. This is not proof that the proposed
    graph is wrong.
  target_ids:
  - antibioticmech:aro-4fcd06e09d
  evidence_ids:
  - authority
  - discovery
  - revision2026
  - checks
- assessment_id: mass
  area: identity
  topic: Mass fields and diagnostic limits
  outcome: unknown
  summary: Formula, charge, exact mass and full key agree. The 597.4 versus 597.458
    average-mass difference is reproduced across PubChem versus ChEBI/RDKit and triggers
    the optional helper. The precise source calculation/precision cause remains unresolved;
    it is not used to infer a different chemical identity.
  target_ids:
  - antibioticmech:aro-4fcd06e09d
  evidence_ids:
  - mass
  - checks
- assessment_id: seed-admission
  area: provenance
  topic: Permitted database seed and explicit family wording
  outcome: supported
  summary: The native record faithfully represents an ARO-classified antibiotic candidate
    with a single proposed structure, and its status remains SEEDED. CARD-based seed
    admission is allowed by documented policy. The definition speaks of congeners,
    so a missing exact-M test is not reinterpreted as a false native numerical observation.
  target_ids:
  - antibioticmech:aro-4fcd06e09d
  evidence_ids:
  - native
  - owners
  - policy-class
  - adopted
- assessment_id: signoff
  area: evidence
  topic: Exact-M structural, antibacterial and selection-barrier validation
  outcome: unknown
  summary: The inspected primary evidence does not establish an isolated exact-M sample,
    exact-M antibacterial assay or exact-M serial-exposure result. Later same-letter
    fasamycin results and other formicamycin congeners cannot fill that gap. Scientific
    sign-off is therefore unresolved even though the seeded proposal is reproducible.
  target_ids:
  - antibioticmech:aro-4fcd06e09d
  evidence_ids:
  - discovery
  - assay-boundary
  - adopted
  - followup2019
  - followup2020
  - revision2026
  - search
- assessment_id: completeness
  area: completeness
  topic: Optional targets, resistance, producer and clinical claims
  outcome: supported
  summary: The record contains no native named gene/protein/pathway or expression
    dataset requiring a structured adapter lookup. General resistant-organism wording
    is not a transcriptomic assertion. Biosynthetic regulation and proposed self-resistance
    are not promoted to antibacterial binding/causal mechanisms. Missing optional
    objects are not counted as defects.
  target_ids:
  - antibioticmech:aro-4fcd06e09d
  evidence_ids:
  - native
  - owners
  - adopted
findings:
- finding_id: F1
  issue_key: formicamycin-m-ms-only-experimental-signoff
  category: evidence
  severity: informational
  status: open
  certainty: confirmed
  title: Keep the MS-inferred M proposal distinct from an experimentally validated
    antimicrobial
  description: The 2017 original positively reports M (16) as an MS-detected, structurally
    inferred congener, explicitly without isolation. Its activity table covers 1–15
    and selection tests use 6, 13 and 15. The adopted 2021 source supplies family
    context and tests other exact compounds. The bounded later-primary search did
    not establish isolated M material or an exact-M activity experiment. Because native
    status is SEEDED, the definition is family-qualified and CARD seed admission is
    permitted, this is a scientific-sign-off question rather than a demonstrated wrong
    identity, inactivity claim or mandatory exclusion.
  target_ids:
  - antibioticmech:aro-4fcd06e09d
  field_paths:
  - chemical_structure
  - definition
  - antimicrobial_class
  - curation_status
  evidence_ids:
  - native
  - policy-class
  - discovery
  - assay-boundary
  - adopted
  - search
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Maintained source classification and family definition
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Maintained proposed exact M graph
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/formicamycin-m.yaml
    role: Curator-owned evidence/discussion and future scientific sign-off
  rule_id: Database assertion versus primary exact-compound evidence; claim-level
    review scope
  native_severity: informational
  normalization_reason: The source explicitly limits its exact-M experiment to MS
    detection. Existing database provenance and SEEDED status are honest; no unsupported
    direct MIC or target object is present. The unresolved gap matters for future
    scientific sign-off, not as proof that the molecule is inactive.
actions:
- action_id: A1
  description: Resolve or explicitly retain the experimental uncertainty before promoting
    exact formicamycin M to scientific sign-off.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-4fcd06e09d
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Maintained source classification and family definition
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Maintained proposed exact M graph
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/formicamycin-m.yaml
    role: Curator-owned evidence/discussion and future scientific sign-off
  acceptance_checks:
  - Find and inspect primary evidence linking an isolated or independently characterized
    exact-M material to the proposed graph and an antimicrobial assay, or preserve
    a curator-owned discussion explicitly stating the current MS-inferred and untested
    scope. Do not transfer L (15), fasamycin M or generic family results.
  - Retain the source database assertion and SEEDED provenance unless a separately
    justified source/eligibility decision is made. Any future structural or class
    correction belongs in maintained source ownership, followed by regeneration and
    focused schema/strict, identity and corpus reproduction checks; no exclusion follows
    solely from this bounded search.
  - Before future numerical sign-off, reconcile the average-mass source convention
    or document why the low-precision PubChem value is retained. Keep the actual standalone
    diagnostic result visible.
limitations:
- No isolated exact-M sample, M-specific NMR/crystal experiment or M-specific antibacterial
  test was established in the inspected originals. The finding is bounded to the identified
  source trail and public searches, not a statement that no such evidence exists anywhere.
- The original proposed M graph has a single bromine and assigned R,R centres, but
  its own direct analytical evidence is mass/formula only. Family-based stereochemical
  inference and database agreement are not independent experimental verification;
  unspecified axial information is not evidence of a mixture.
- The 2019, 2020, 2021 and 2026 follow-up papers were read at the exact sections stated.
  Their complete raw supplemental datasets were not reprocessed. Shared compound numbers
  and fasamycin/formicamycin names were kept distinct.
- The optional standalone chemical diagnostic failed only on the 0.058 average-mass
  difference between PubChem/native and ChEBI/RDKit. Public mass-convention documentation
  did not establish the exact numerical cause, so this discrepancy remains unresolved
  rather than silently normalized. Graph, formula, charge, monoisotopic mass and mint
  consistency were independently confirmed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- This is a partial scientific review of the seeded hypothesis and its source limits.
  It does not constitute scientific REVIEWED sign-off or assert that M lacks antibacterial
  activity.
- The review contract does not allow a seed_only verdict with scientific_review true;
  pass_with_limitations here describes the bounded review outcome while the assessments
  explicitly preserve the distinction between database admission and unresolved exact-M
  validation.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
