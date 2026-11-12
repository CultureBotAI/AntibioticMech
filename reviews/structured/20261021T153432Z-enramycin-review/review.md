# Review of enramycin

- Review: 20261021T153432Z-enramycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:03:55Z
- Finished UTC: 2026-10-21T15:34:32Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Official GSRS defines enramycin as a mixture requiring components A and B, consistent with the original separation paper. The native record nevertheless stores a single hydrate graph. That graph is not either authentic component: independent comparison identifies different peptide connectivity and acyl geometry. The imported RiPP class also contradicts original NRPS biosynthesis evidence. The adopted poultry paper supports a feed-intervention context but does not establish exact component, hydrate or primary target identity.

## Scope And Provenance

Whole SEEDED, MINTED record: definition and sole adopted PMID, RiPP parent and structural class, complete PubChem hydrate structure, three cross-references, source concept and three histories. Official mixture/component definitions, original A/B structure, biosynthesis and qualified mechanism evidence checked separately.

Selection: Queue 399 in isolated batch 040. All 13 initial hashes preserved; actual ARO and PubChem owners appended before assessment for 16 unchanged inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-bd55fbe0ca | data/antibiotics/antibacterial/enramycin.yaml | generated | enramycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native schema | passed | True | antibioticmech:aro-bd55fbe0ca | Exit 0. |
| Native strict terms | passed | True | antibioticmech:aro-bd55fbe0ca | Exit 0; no ERROR rows. |
| Internal native molecular consistency | passed | False | antibioticmech:aro-bd55fbe0ca | Native fields agree internally and the minted identifier recalculates. This does not validate chemical identity against authentic components. |
| Initial authority-comparison attempt | failed | False | antibioticmech:aro-bd55fbe0ca | Actual exit 1: InChI-reader tautomer lacked the expected amide SMARTS; tautomer enumeration also hit its 1000-state limit. This failed approach is preserved and is not used to prove a chemistry defect. |
| Explicit component and adjacency audit | passed | False | antibioticmech:aro-bd55fbe0ca | Six encodings audited. Native organic graph matches neither official component even using bond-order-generic adjacency queries; concrete imide/glycine and acyl-geometry differences are retained. Each official component SMILES/molfile pair matches with chirality enabled. |
| Structured MurG follow-up | passed | False | antibioticmech:aro-bd55fbe0ca | Dataset discovery and four queries preceded mechanism web research; murG resolves to b0090 with no component hit requiring summary. |
| Whole source and reference ledger | passed | False | antibioticmech:aro-bd55fbe0ca | All 16 hashes unchanged; sole adopted PMID disposed, all source fields reconciled and three ordered histories checked. |
| Authoritative full QC | failed | True | antibioticmech:aro-bd55fbe0ca | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-bd55fbe0ca | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-bd55fbe0ca | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-bd55fbe0ca | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-bd55fbe0ca | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-bd55fbe0ca | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-bd55fbe0ca | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-bd55fbe0ca | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-bd55fbe0ca | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### One structure versus source-defined mixture

identity: concern. Targets: antibioticmech:aro-bd55fbe0ca.

The broad source concept requires both A and B and cannot be represented by a single hydrate graph.

### Stored graph versus authentic components

consistency: concern. Targets: antibioticmech:aro-bd55fbe0ca.

Neither authentic component matches the native organic adjacency or acyl geometry; missing tetrahedral descriptors alone are not used as mixture evidence.

### RiPP versus NRPS biosynthesis

grounding: concern. Targets: antibioticmech:aro-bd55fbe0ca.

Primary gene-disruption evidence contradicts the imported ribosomal class.

### Antibacterial role and feed context

evidence: supported. Targets: antibioticmech:aro-bd55fbe0ca.

The source-defined enduracidin complex is an antibacterial peptide material; this role does not validate the stored exact graph or every clinical-use clause.

### MurG-step inhibition versus primary cellular mechanism

scope: concern. Targets: antibioticmech:aro-bd55fbe0ca.

The original study favors lipidII/transglycosylation and preserves MurG-step inhibition. No direct MurG protein-binding target is asserted by native, and none is inferred here.

### Producer genus

evidence: supported. Targets: antibioticmech:aro-bd55fbe0ca.

Original separation and biosynthesis studies concern Streptomyces fungicidicus, supporting the genus at the stated scope.

### Pig prevention and exact administered form

scope: unknown. Targets: antibioticmech:aro-bd55fbe0ca.

The adopted paper is a broiler diet/metagenome study; pig necrotic-enteritis efficacy and exact hydrate/component material remain unverified in the inspected sources.

### Optional target and resistance objects

completeness: not_applicable. Targets: antibioticmech:aro-bd55fbe0ca.

Identity must first be reconciled; optional object population cannot rescue a broad mixture as one chemical structure.

### All adopted leads and histories

provenance: supported. Targets: antibioticmech:aro-bd55fbe0ca.

The sole adopted PMID and current authorities were inspected at explicit levels; source rows and 16 unchanged inputs checked.

## Findings

### F1: A source-defined A/B mixture is minted as one chemical structure

blocker / open / confirmed; issue key: enramycin-mixture-minted-as-single-structure.

GSRS requires both enramycin A and B, and the original study separates those components. Native label/source concept nevertheless denotes broad enramycin while chemical_structure stores only one hydrated molecule. The mismatch is established from positive source definitions, not inferred from incomplete stereo.

### F2: The imported organic graph is neither authentic component

major / open / confirmed; issue key: enramycin-pubchem-graph-differs-from-authentic-components.

Even after retaining water as a separate explicit component, the native organic graph has different peptide adjacency and 2E rather than authentic 2Z acyl geometry. It has two imide links and no glycine-backbone motif, unlike both official components and the original structure. Its A-like gross formula cannot justify renaming this record to A.

### F3: A nonribosomal peptide is placed in the RiPP class

major / open / confirmed; issue key: enramycin-nrps-misclassified-as-ripp.

The primary endA-D disruption and sequencing study establishes NRPS biosynthesis, whereas ARO:3009656 explicitly describes ribosomal precursor synthesis. Current ARO reproduces the error and the seeder carries it into both parent_compounds and structural_class.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, record an EXCLUDE decision for ARO:3007197 and the existing minted identifier, with the official mixture and original separation evidence. Regenerate through the maintained source/seeder workflow while preserving provenance and historical review artifacts. Do not relabel the broad concept as A or silently transfer mixture assays. Any future exact A/B records require independent source identities, structures and form-specific evidence.

- The broad mixture no longer appears as an active exact-structure AntibioticRecord and remains traceable in the excluded-source decision lane.
- Any retained or newly added component has its own fully adjudicated identity and assay material scope; no arbitrary mapping to the broad concept remains.
- Native schema/strict and full corpus/reference/history gates pass, with no orphaned references from the separately authorized reconciliation.

### A2

Prevent the erroneous PubChem56842192 graph from being reused as either component through a maintained source correction or exclusion. If a separately authorized component record is curated, use the original structure and independent official component snapshots to establish its peptide connectivity, acyl geometry, stereo, hydration and charge; refresh enrichment and reseed. Removing water or supplying chiral tags alone does not fix the existing graph.

- Component identity is tested by atom adjacency and stereochemistry, not formula alone.
- Gly and Orn backbone connectivity and the 2Z,4E acyl geometry agree with primary and independent authority evidence.
- All retained exact identifiers, native structure fields and masses describe the same complete formula unit.

### A3

Correct the upstream ARO biosynthetic placement and refresh extraction, or implement a narrow maintained classification correction. For any future exact component, use a verified nonribosomal/lipodepsipeptide description and a supported broader peptide parent rather than the RiPP category. The mixture exclusion remains necessary independently of this class repair.

- No enramycin-derived exact component inherits the contradicted ribosomal-synthesis class.
- The class correction preserves antibacterial activity and documents original NRPS evidence.
- The change survives re-extraction/reseeding and required native validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/enramycin.yaml; Entire native YAML | supports | The record has a broad enramycin label and ARO source concept, one hydrated organic graph, RiPP class and a MurG sentence in its definition. It has no dedicated molecular-target, MIC, resistance, producer or clinical-status objects. |
| mixture | GSRS UNII:4GP7CLG9EG; 399-gsrs.json substanceClass and mixture.components | refutes | The official enramycin substance is a mixture. Both ENRAMYCIN A, UNII09I5H1AG37, and ENRAMYCIN B, UNII5TQ7Z201B8, are marked MUST_BE_PRESENT. This positive material definition is independent of the missing stereochemistry in the native graph. |
| chemistry | PubChem CID56842192; GSRS09I5H1AG37 and5TQ7Z201B8; 399-pubchem.json;399-gsrs-A.json;399-gsrs-B.json;399-authority-chemistry.json | refutes | Native and current PubChem agree on C107H140Cl2N26O32, comprising C107H138Cl2N26O31 plus water, with no assigned tetrahedral centers. Equal gross composition to component A is misleading: the organic graph has two carbonyl-N-carbonyl imide links and no glycine-backbone match. Both GSRS components have a glycine backbone and no such imide link; A and B differ by CH2 in their lipid chains. Native also encodes 2E,4E instead of the original and official 2Z,4E acyl geometry. Adjacency comparison allows different guanidine bond orders, so the mismatch is not a tautomer artifact. |
| structure | DOI:10.1248/cpb.21.1184; 399-structure1973.pdf selected printed pp1184,1185,1188,1189; Figure9 and separation/formula passages inspected as images | refutes | The original study separates enduracidins A and B chromatographically and characterizes their distinct C12 and C13 acyl residues. Both are 2-cis,4-trans. Figure9 contains Gly and D-Orn in the peptide backbone rather than the native imide connectivity. Table1 describes hydrochloride samples; it does not establish an exact monohydrate for the broad mixture. |
| chembl | chembl:CHEMBL2109091; 399-chembl.json structure_type and molecule_structures | context_only | The exact cited ChEMBL entry resolves to ENRAMYCIN but explicitly has structure_type NONE and no molecular graph. It cannot independently verify the adopted PubChem hydrate or a particular A/B component. This is unresolved exact structural grounding, not a fabricated graph mismatch attributed to ChEMBL. |
| biosynthesis | PMID:17005978; DOI:10.1099/mic.0.29043-0; 399-core-17005978.json complete original abstract; publisher abstract independently resolved | refutes | The original gene-cluster study identifies endA-D nonribosomal peptide synthetases in Streptomyces fungicidicus ATCC21013. Targeted NRPS disruption abolishes enduracidin production. This directly contradicts ribosomal precursor synthesis, while supporting the native producer-genus context. The inaccessible full experimental body is not claimed as read. |
| adopted | PMID:35841645; DOI:10.1016/j.psj.2022.102010; 399-PMC9293667.xml selected main introduction, experimental design, DNA sequencing/annotation, results and discussion | context_only | The study uses 144 broiler chicks assigned to four diets, including 10 mg/kg enramycin powder, and analyzes cecal metagenomic DNA against CARD. Its MurG and necrotic-enteritis statements are cited background; it performs neither an enzyme assay nor a pig or necrotic-enteritis challenge. The reported ARG abundance is not direct expression measurement or experimental proof of each gene conferring enramycin resistance. Exact component ratio and hydrate identity are not specified in the inspected methods. |
| mechanism | PMID:16880924; DOI:10.1039/B515328J; 399-mechanism-core.json complete original abstract | supports | Original comparative inhibition and substrate-binding evidence favors lipidII/transglycosylation over the MurG step for enduracidin, while retaining in-vitro inhibition of both steps. Native does not assert a DIRECT_BINDING_TARGET object, so this review does not recast its MurG sentence as an explicitly measured direct protein interaction or assert that MurG-step inhibition is absent. Exact reagent component ratio was not verified from the accessible abstract. |
| analytical | DOI:10.3389/fvets.2024.1462743; PMC:PMC11405371; 399-PMC11405371.xml A/B materials, analytical methods and selected results | context_only | The original analytical study uses separately purchased A and B standards of stated 95% and85% purity and resolves their mass-spectrometric responses. It provides an experimentally operational component distinction. Residue detection, extraction acidification and background use statements are not exact hydrate, antibacterial efficacy or current authorization evidence. |
| modern-biosynthesis | PMC:PMC11909717; 399-PMC11909717.xml selected introduction, strain and gene-editing methods | context_only | The 2025 original study explicitly treats enduracidin/enramycin as nonribosomal and examines industrial Streptomyces fungicidicus TXX3120. Its fermentation and assay material refers to A/B production and a 4% standard; that material is not a pure unspecified hydrate, and its strain cannot be silently equated with every historical producer. |
| terms | ARO:3007197; ARO:3009656; 399-aro-blocks.json;374-current-aro.obo and374-fetch-results.json | refutes | Both identifiers resolve, but the current ARO source still places enramycin under the ribosomally synthesized and post-translationally modified peptide class. That defined biosynthetic category is contradicted by the original NRPS evidence. Source agreement does not make this class scientifically correct. |
| adapter | iModulonDB e_coli/modulome; 399-adapter-results.json | context_only | Dataset discovery and enramycin,MurG,murG,cell-wall queries ran before mechanism web follow-up. murG resolves to b0090; no iModulon component hit required summary. This is gene-catalog context, not target binding or an enramycin phenotype. |
| owners | Maintained ARO/PubChem inputs and source-boundary decision lane; 399-owner-append.json;399-raw-rows.json;399-source-audit.json;curation/decisions.tsv;docs/HARMONIZATION.md | supports | The record reproduces the adopted ARO definition/class and PubChem graph. All 16 hashes, including the original 13, remain unchanged, and three histories are ordered. The documented EXCLUDE decision preserves a source concept while preventing a mixture from becoming an exact-structure record. It provides the primary correction lane; arbitrary relabeling to component A would not solve the chemistry conflict. |
| validation | Actual native and supplementary checks; 399-focused-results.json;399-strict.tsv;399-authority-chemistry-initial.log;399-authority-chemistry.log;399-ledger.log | supports | Native chemistry/schema/strict and the final component audit/source ledger pass. The initial supplemental attempt failed on tautomer processing and remains recorded separately. Deterministic validity does not erase the positive mixture, connectivity or biosynthetic-class findings. |
| access | Bounded exact enramycin evidence search; 399-local-hits.txt and399-exact-boundary-hits.txt include ignored files;399-fetch.json and399-fetch2.json | context_only | Original structural PDF, adopted poultry and later analytical/genetic papers were retrieved. RSC direct full-text/PDF attempts returned403; the NRPS publisher returned403 and its mirror404. Complete original abstracts resolved. Indexed publisher body text was used as a discovery lead, not claimed as an independently retrieved full methods section. |

## Limits And Additional Notes

- The original NRPS paper was inspected at complete-abstract level; direct full-text routes failed. The original 1973 structure was inspected on selected rendered pages, including component separation, formulas and Figure9, rather than claimed as a fully OCR-readable paper.
- The original mechanism abstract supports inhibition of both biochemical steps with lipidII/transglycosylation preferred. Exact reagent A/B ratio and hydrate state were not verified. No absence of MurG-step inhibition or direct protein-binding target is inferred.
- The sole adopted poultry study provides background claims and a metagenomic feed experiment. It does not experimentally establish producer biosynthesis, exact graph, pig disease prevention or each detected ARG as an enramycin resistance determinant.
- The separate GSRS component B has an unspecified lipid-chain stereocenter; that limitation is preserved and does not make B itself an experimentally demonstrated mixture. Native missing stereochemistry similarly does not establish the broad mixture finding.
- ChEMBL2109091 has no structure, so it resolves as a broad name entry without independently verifying the exact native chemical form.
- The first supplemental chemical comparison failed on InChI tautomer handling and enumeration limits. Final topology checks avoid that failed inference; the native chemistry gate itself passed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Standalone chemistry used batch019 Python against batch040; native schema/strict and ledger used batch040.
- An ignored-file-inclusive targeted search of native records, decisions, ChEBI inventory and source configuration found only the broad enramycin record for the checked names. Future component creation still requires an exhaustive exact-identifier deduplication step.
- Optional mechanistic wording can be improved during later authorized reconciliation: distinguish substrate sequestration and primary cellular action from an unqualified MurG-only explanation, without deleting genuine biochemical MurG inhibition.
- No native scientific status was changed. The source-defined mixture, graph defect and biosynthetic-class contradiction are separate findings with separate maintained owners.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T153432Z-enramycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of enramycin
started_at: '2026-10-21T15:03:55Z'
finished_at: '2026-10-21T15:34:32Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Entire native and exact source rows read; independent official
    mixture/component chemistry, original separated structures and NRPS evidence;
    adopted primary study methods and assay scope inspected; executable source and
    history checks.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: Mixture identity blocks exact-record sign-off; major graph and RiPP
  classification defects
scientific_review: true
summary: 'Official GSRS defines enramycin as a mixture requiring components A and
  B, consistent with the original separation paper. The native record nevertheless
  stores a single hydrate graph. That graph is not either authentic component: independent
  comparison identifies different peptide connectivity and acyl geometry. The imported
  RiPP class also contradicts original NRPS biosynthesis evidence. The adopted poultry
  paper supports a feed-intervention context but does not establish exact component,
  hydrate or primary target identity.'
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
  - path: data/antibiotics/antibacterial/enramycin.yaml
    sha256: 1ba9ab2b2524a581ce68852df0655626a2a0baeaf1dd0ca79f4033d50fa9bcd2
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
    role: context
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
  - path: data/raw/pubchem_structures.tsv
    role: context
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
  - path: scripts/enrich_pubchem_structures.py
    role: context
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
scope:
  description: 'Whole SEEDED, MINTED record: definition and sole adopted PMID, RiPP
    parent and structural class, complete PubChem hydrate structure, three cross-references,
    source concept and three histories. Official mixture/component definitions, original
    A/B structure, biosynthesis and qualified mechanism evidence checked separately.'
  selection: Queue 399 in isolated batch 040. All 13 initial hashes preserved; actual
    ARO and PubChem owners appended before assessment for 16 unchanged inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-bd55fbe0ca
targets:
- target_id: antibioticmech:aro-bd55fbe0ca
  path: data/antibiotics/antibacterial/enramycin.yaml
  label: enramycin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted CARD/ARO definition, class, citations and cross-references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained PubChem enrichment owner
checks:
- check_id: schema
  name: Native schema
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/enramycin.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - validation
- check_id: strict
  name: Native strict terms
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/enramycin.yaml --out /private/tmp/am-review-session/399-strict.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no ERROR rows.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - validation
- check_id: native-chemistry
  name: Internal native molecular consistency
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    399 > /private/tmp/am-review-session/399-focused-run.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Native fields agree internally and the minted identifier recalculates.
    This does not validate chemical identity against authentic components.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - chemistry
  - validation
- check_id: initial-authorities
  name: Initial authority-comparison attempt
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/399-authority-chemistry-initial.py
    > /private/tmp/am-review-session/399-authority-chemistry-initial.log 2>&1
  status: failed
  required: false
  exit_code: 1
  expected_exit_code: 0
  summary: 'Actual exit 1: InChI-reader tautomer lacked the expected amide SMARTS;
    tautomer enumeration also hit its 1000-state limit. This failed approach is preserved
    and is not used to prove a chemistry defect.'
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - chemistry
- check_id: authority-chemistry
  name: Explicit component and adjacency audit
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/399-authority-chemistry.py
    > /private/tmp/am-review-session/399-authority-chemistry.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Six encodings audited. Native organic graph matches neither official component
    even using bond-order-generic adjacency queries; concrete imide/glycine and acyl-geometry
    differences are retained. Each official component SMILES/molfile pair matches
    with chirality enabled.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - chemistry
  - structure
- check_id: adapter
  name: Structured MurG follow-up
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/399-adapter.py
    > /private/tmp/am-review-session/399-adapter.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Dataset discovery and four queries preceded mechanism web research; murG
    resolves to b0090 with no component hit requiring summary.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - adapter
- check_id: source-ledger
  name: Whole source and reference ledger
  command: .venv/bin/python /private/tmp/am-review-session/399-ledger.py > /private/tmp/am-review-session/399-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All 16 hashes unchanged; sole adopted PMID disposed, all source fields
    reconciled and three ordered histories checked.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - owners
  - adopted
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
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
  - antibioticmech:aro-bd55fbe0ca
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
  - antibioticmech:aro-bd55fbe0ca
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
  - antibioticmech:aro-bd55fbe0ca
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
  - antibioticmech:aro-bd55fbe0ca
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
  - antibioticmech:aro-bd55fbe0ca
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
  - antibioticmech:aro-bd55fbe0ca
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
  - antibioticmech:aro-bd55fbe0ca
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
  - antibioticmech:aro-bd55fbe0ca
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/enramycin.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T15:27:33Z'
  support: supports
  summary: The record has a broad enramycin label and ARO source concept, one hydrated
    organic graph, RiPP class and a MurG sentence in its definition. It has no dedicated
    molecular-target, MIC, resistance, producer or clinical-status objects.
- evidence_id: mixture
  kind: authority
  reference: GSRS UNII:4GP7CLG9EG
  locator: 399-gsrs.json substanceClass and mixture.components
  accessed_at: '2026-10-21T15:22:01.395221Z'
  support: refutes
  summary: The official enramycin substance is a mixture. Both ENRAMYCIN A, UNII09I5H1AG37,
    and ENRAMYCIN B, UNII5TQ7Z201B8, are marked MUST_BE_PRESENT. This positive material
    definition is independent of the missing stereochemistry in the native graph.
  snapshot_sha256: b6f0460eb0525a8a57c4fcfc6409556ad3b341c3de938e1ad649002374ba5819
- evidence_id: chemistry
  kind: authority
  reference: PubChem CID56842192; GSRS09I5H1AG37 and5TQ7Z201B8
  locator: 399-pubchem.json;399-gsrs-A.json;399-gsrs-B.json;399-authority-chemistry.json
  accessed_at: '2026-10-21T15:27:33Z'
  support: refutes
  summary: 'Native and current PubChem agree on C107H140Cl2N26O32, comprising C107H138Cl2N26O31
    plus water, with no assigned tetrahedral centers. Equal gross composition to component
    A is misleading: the organic graph has two carbonyl-N-carbonyl imide links and
    no glycine-backbone match. Both GSRS components have a glycine backbone and no
    such imide link; A and B differ by CH2 in their lipid chains. Native also encodes
    2E,4E instead of the original and official 2Z,4E acyl geometry. Adjacency comparison
    allows different guanidine bond orders, so the mismatch is not a tautomer artifact.'
  snapshot_sha256: 0407e3cdba9b1d18b5c9794e908383499fb8496768b11cd2b9782deec2931982
- evidence_id: structure
  kind: primary_source
  reference: DOI:10.1248/cpb.21.1184
  locator: 399-structure1973.pdf selected printed pp1184,1185,1188,1189; Figure9 and
    separation/formula passages inspected as images
  accessed_at: '2026-10-21T15:22:39.736695Z'
  support: refutes
  summary: The original study separates enduracidins A and B chromatographically and
    characterizes their distinct C12 and C13 acyl residues. Both are 2-cis,4-trans.
    Figure9 contains Gly and D-Orn in the peptide backbone rather than the native
    imide connectivity. Table1 describes hydrochloride samples; it does not establish
    an exact monohydrate for the broad mixture.
  snapshot_sha256: cfe78596bc403b6f367920ad9b4c1d314ae80d4441b44a36adb5506ff525a6bd
- evidence_id: chembl
  kind: authority
  reference: chembl:CHEMBL2109091
  locator: 399-chembl.json structure_type and molecule_structures
  accessed_at: '2026-10-21T15:22:01.395131Z'
  support: context_only
  summary: The exact cited ChEMBL entry resolves to ENRAMYCIN but explicitly has structure_type
    NONE and no molecular graph. It cannot independently verify the adopted PubChem
    hydrate or a particular A/B component. This is unresolved exact structural grounding,
    not a fabricated graph mismatch attributed to ChEMBL.
  snapshot_sha256: 2929e3d22f1521e3774e784664bbb68ecffb8b2ebf46b625cb490c23f836975a
- evidence_id: biosynthesis
  kind: primary_source
  reference: PMID:17005978; DOI:10.1099/mic.0.29043-0
  locator: 399-core-17005978.json complete original abstract; publisher abstract independently
    resolved
  accessed_at: '2026-10-21T15:22:02.767953Z'
  support: refutes
  summary: The original gene-cluster study identifies endA-D nonribosomal peptide
    synthetases in Streptomyces fungicidicus ATCC21013. Targeted NRPS disruption abolishes
    enduracidin production. This directly contradicts ribosomal precursor synthesis,
    while supporting the native producer-genus context. The inaccessible full experimental
    body is not claimed as read.
  snapshot_sha256: ec81088919227f4c6e741d55c62a45c1f931e34b28861fe05c7291e61bc0cb45
- evidence_id: adopted
  kind: primary_source
  reference: PMID:35841645; DOI:10.1016/j.psj.2022.102010
  locator: 399-PMC9293667.xml selected main introduction, experimental design, DNA
    sequencing/annotation, results and discussion
  accessed_at: '2026-10-21T15:22:01.395280Z'
  support: context_only
  summary: The study uses 144 broiler chicks assigned to four diets, including 10
    mg/kg enramycin powder, and analyzes cecal metagenomic DNA against CARD. Its MurG
    and necrotic-enteritis statements are cited background; it performs neither an
    enzyme assay nor a pig or necrotic-enteritis challenge. The reported ARG abundance
    is not direct expression measurement or experimental proof of each gene conferring
    enramycin resistance. Exact component ratio and hydrate identity are not specified
    in the inspected methods.
  snapshot_sha256: eb3eecd2c41b4f3bb83d7727f3fef758e58a537087f9521fee703db7b913f9bb
- evidence_id: mechanism
  kind: primary_source
  reference: PMID:16880924; DOI:10.1039/B515328J
  locator: 399-mechanism-core.json complete original abstract
  accessed_at: '2026-10-21T15:22:03.045592Z'
  support: supports
  summary: Original comparative inhibition and substrate-binding evidence favors lipidII/transglycosylation
    over the MurG step for enduracidin, while retaining in-vitro inhibition of both
    steps. Native does not assert a DIRECT_BINDING_TARGET object, so this review does
    not recast its MurG sentence as an explicitly measured direct protein interaction
    or assert that MurG-step inhibition is absent. Exact reagent component ratio was
    not verified from the accessible abstract.
  snapshot_sha256: f0fda91bd86642a632ebaa2cb2bbd03ba2a483fed56e2d1f32377c7495096db4
- evidence_id: analytical
  kind: primary_source
  reference: DOI:10.3389/fvets.2024.1462743; PMC:PMC11405371
  locator: 399-PMC11405371.xml A/B materials, analytical methods and selected results
  accessed_at: '2026-10-21T15:22:01.939639Z'
  support: context_only
  summary: The original analytical study uses separately purchased A and B standards
    of stated 95% and85% purity and resolves their mass-spectrometric responses. It
    provides an experimentally operational component distinction. Residue detection,
    extraction acidification and background use statements are not exact hydrate,
    antibacterial efficacy or current authorization evidence.
  snapshot_sha256: 77d0da0274a3f0ff2fa05e96d4ee25b68cc6689448cdbc3dc7309ab84fe37dba
- evidence_id: modern-biosynthesis
  kind: primary_source
  reference: PMC:PMC11909717
  locator: 399-PMC11909717.xml selected introduction, strain and gene-editing methods
  accessed_at: '2026-10-21T15:22:39.964629Z'
  support: context_only
  summary: The 2025 original study explicitly treats enduracidin/enramycin as nonribosomal
    and examines industrial Streptomyces fungicidicus TXX3120. Its fermentation and
    assay material refers to A/B production and a 4% standard; that material is not
    a pure unspecified hydrate, and its strain cannot be silently equated with every
    historical producer.
  snapshot_sha256: a15b387eedd1abef5c468dcba4d153c0d54cb86fb7a4065817e7f888aba378ba
- evidence_id: terms
  kind: authority
  reference: ARO:3007197; ARO:3009656
  locator: 399-aro-blocks.json;374-current-aro.obo and374-fetch-results.json
  accessed_at: '2026-10-21T15:27:33Z'
  support: refutes
  summary: Both identifiers resolve, but the current ARO source still places enramycin
    under the ribosomally synthesized and post-translationally modified peptide class.
    That defined biosynthetic category is contradicted by the original NRPS evidence.
    Source agreement does not make this class scientifically correct.
  snapshot_sha256: 0350a70f883fab4a7c3e72078095fc6cb1b5efa832c905ec973135bfec63a4dd
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/modulome
  locator: 399-adapter-results.json
  accessed_at: '2026-10-21T15:27:33Z'
  support: context_only
  summary: Dataset discovery and enramycin,MurG,murG,cell-wall queries ran before
    mechanism web follow-up. murG resolves to b0090; no iModulon component hit required
    summary. This is gene-catalog context, not target binding or an enramycin phenotype.
  snapshot_sha256: 36343148447012eb5fcb90ef94112010db19fb0cbacef831435fc8b974aedeee
- evidence_id: owners
  kind: database
  reference: Maintained ARO/PubChem inputs and source-boundary decision lane
  locator: 399-owner-append.json;399-raw-rows.json;399-source-audit.json;curation/decisions.tsv;docs/HARMONIZATION.md
  accessed_at: '2026-10-21T15:27:33Z'
  support: supports
  summary: The record reproduces the adopted ARO definition/class and PubChem graph.
    All 16 hashes, including the original 13, remain unchanged, and three histories
    are ordered. The documented EXCLUDE decision preserves a source concept while
    preventing a mixture from becoming an exact-structure record. It provides the
    primary correction lane; arbitrary relabeling to component A would not solve the
    chemistry conflict.
  snapshot_sha256: 981b9fc623fad2df20086a83991be7c8be16c80f0e6ecf41bd1edbedf8eafab6
- evidence_id: validation
  kind: validation
  reference: Actual native and supplementary checks
  locator: 399-focused-results.json;399-strict.tsv;399-authority-chemistry-initial.log;399-authority-chemistry.log;399-ledger.log
  accessed_at: '2026-10-21T15:27:33Z'
  support: supports
  summary: Native chemistry/schema/strict and the final component audit/source ledger
    pass. The initial supplemental attempt failed on tautomer processing and remains
    recorded separately. Deterministic validity does not erase the positive mixture,
    connectivity or biosynthetic-class findings.
  snapshot_sha256: e284d401009e6327d12d51503202259fbb04ef8860a837e851da043aa5dcf0b3
- evidence_id: access
  kind: search
  reference: Bounded exact enramycin evidence search
  locator: 399-local-hits.txt and399-exact-boundary-hits.txt include ignored files;399-fetch.json
    and399-fetch2.json
  accessed_at: '2026-10-21T15:27:33Z'
  support: context_only
  summary: Original structural PDF, adopted poultry and later analytical/genetic papers
    were retrieved. RSC direct full-text/PDF attempts returned403; the NRPS publisher
    returned403 and its mirror404. Complete original abstracts resolved. Indexed publisher
    body text was used as a discovery lead, not claimed as an independently retrieved
    full methods section.
  snapshot_sha256: 9ba7997b168de5ab0829eacef18363aa0fa60ca06c0e3b668f8430fb5e95984f
  search_scope: 399-local-hits.txt and399-exact-boundary-hits.txt include ignored
    files;399-fetch.json and399-fetch2.json
assessments:
- assessment_id: boundary
  area: identity
  topic: One structure versus source-defined mixture
  outcome: concern
  summary: The broad source concept requires both A and B and cannot be represented
    by a single hydrate graph.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - mixture
  - structure
  - owners
- assessment_id: graph
  area: consistency
  topic: Stored graph versus authentic components
  outcome: concern
  summary: Neither authentic component matches the native organic adjacency or acyl
    geometry; missing tetrahedral descriptors alone are not used as mixture evidence.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - chemistry
  - structure
- assessment_id: class
  area: grounding
  topic: RiPP versus NRPS biosynthesis
  outcome: concern
  summary: Primary gene-disruption evidence contradicts the imported ribosomal class.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - biosynthesis
  - terms
- assessment_id: activity
  area: evidence
  topic: Antibacterial role and feed context
  outcome: supported
  summary: The source-defined enduracidin complex is an antibacterial peptide material;
    this role does not validate the stored exact graph or every clinical-use clause.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - adopted
  - structure
  - mechanism
- assessment_id: mechanism
  area: scope
  topic: MurG-step inhibition versus primary cellular mechanism
  outcome: concern
  summary: The original study favors lipidII/transglycosylation and preserves MurG-step
    inhibition. No direct MurG protein-binding target is asserted by native, and none
    is inferred here.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - mechanism
  - adopted
- assessment_id: producer
  area: evidence
  topic: Producer genus
  outcome: supported
  summary: Original separation and biosynthesis studies concern Streptomyces fungicidicus,
    supporting the genus at the stated scope.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - structure
  - biosynthesis
- assessment_id: use
  area: scope
  topic: Pig prevention and exact administered form
  outcome: unknown
  summary: The adopted paper is a broiler diet/metagenome study; pig necrotic-enteritis
    efficacy and exact hydrate/component material remain unverified in the inspected
    sources.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - adopted
  - analytical
- assessment_id: completeness
  area: completeness
  topic: Optional target and resistance objects
  outcome: not_applicable
  summary: Identity must first be reconciled; optional object population cannot rescue
    a broad mixture as one chemical structure.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - record
  - mixture
- assessment_id: provenance
  area: provenance
  topic: All adopted leads and histories
  outcome: supported
  summary: The sole adopted PMID and current authorities were inspected at explicit
    levels; source rows and 16 unchanged inputs checked.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  evidence_ids:
  - owners
  - adopted
  - validation
findings:
- finding_id: F1
  issue_key: enramycin-mixture-minted-as-single-structure
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: A source-defined A/B mixture is minted as one chemical structure
  description: GSRS requires both enramycin A and B, and the original study separates
    those components. Native label/source concept nevertheless denotes broad enramycin
    while chemical_structure stores only one hydrated molecule. The mismatch is established
    from positive source definitions, not inferred from incomplete stereo.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  field_paths:
  - identifier
  - label
  - chemical_structure
  - source_concepts[0]
  evidence_ids:
  - mixture
  - structure
  - owners
  rule_id: 'review-checklist and HARMONIZATION: exact chemical identity and scientifically
    correct class'
  native_severity: Blocker scientific identity or grounding correction
  normalization_reason: The record scope violates the repository one-structure boundary
    and blocks exact identity sign-off.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
- finding_id: F2
  issue_key: enramycin-pubchem-graph-differs-from-authentic-components
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The imported organic graph is neither authentic component
  description: Even after retaining water as a separate explicit component, the native
    organic graph has different peptide adjacency and 2E rather than authentic 2Z
    acyl geometry. It has two imide links and no glycine-backbone motif, unlike both
    official components and the original structure. Its A-like gross formula cannot
    justify renaming this record to A.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  field_paths:
  - chemical_structure
  - xrefs[2]
  evidence_ids:
  - chemistry
  - structure
  - owners
  rule_id: 'review-checklist and HARMONIZATION: exact chemical identity and scientifically
    correct class'
  native_severity: Major scientific identity or grounding correction
  normalization_reason: This independent chemistry defect would survive merely narrowing
    the broad label or removing water; internally consistent identifiers do not validate
    the source graph.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted CARD/ARO definition, class, citations and cross-references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained PubChem enrichment owner
- finding_id: F3
  issue_key: enramycin-nrps-misclassified-as-ripp
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: A nonribosomal peptide is placed in the RiPP class
  description: The primary endA-D disruption and sequencing study establishes NRPS
    biosynthesis, whereas ARO:3009656 explicitly describes ribosomal precursor synthesis.
    Current ARO reproduces the error and the seeder carries it into both parent_compounds
    and structural_class.
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  field_paths:
  - parent_compounds[0]
  - structural_class
  - structural_class_id
  evidence_ids:
  - biosynthesis
  - terms
  - owners
  rule_id: 'review-checklist and HARMONIZATION: exact chemical identity and scientifically
    correct class'
  native_severity: Major scientific identity or grounding correction
  normalization_reason: This is a positive mechanistic classification contradiction,
    not missing evidence or stylistic preference.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted CARD/ARO definition, class, citations and cross-references
actions:
- action_id: A1
  description: In separately authorized curation, record an EXCLUDE decision for ARO:3007197
    and the existing minted identifier, with the official mixture and original separation
    evidence. Regenerate through the maintained source/seeder workflow while preserving
    provenance and historical review artifacts. Do not relabel the broad concept as
    A or silently transfer mixture assays. Any future exact A/B records require independent
    source identities, structures and form-specific evidence.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  acceptance_checks:
  - The broad mixture no longer appears as an active exact-structure AntibioticRecord
    and remains traceable in the excluded-source decision lane.
  - Any retained or newly added component has its own fully adjudicated identity and
    assay material scope; no arbitrary mapping to the broad concept remains.
  - Native schema/strict and full corpus/reference/history gates pass, with no orphaned
    references from the separately authorized reconciliation.
- action_id: A2
  description: Prevent the erroneous PubChem56842192 graph from being reused as either
    component through a maintained source correction or exclusion. If a separately
    authorized component record is curated, use the original structure and independent
    official component snapshots to establish its peptide connectivity, acyl geometry,
    stereo, hydration and charge; refresh enrichment and reseed. Removing water or
    supplying chiral tags alone does not fix the existing graph.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted CARD/ARO definition, class, citations and cross-references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained PubChem enrichment owner
  acceptance_checks:
  - Component identity is tested by atom adjacency and stereochemistry, not formula
    alone.
  - Gly and Orn backbone connectivity and the 2Z,4E acyl geometry agree with primary
    and independent authority evidence.
  - All retained exact identifiers, native structure fields and masses describe the
    same complete formula unit.
- action_id: A3
  description: Correct the upstream ARO biosynthetic placement and refresh extraction,
    or implement a narrow maintained classification correction. For any future exact
    component, use a verified nonribosomal/lipodepsipeptide description and a supported
    broader peptide parent rather than the RiPP category. The mixture exclusion remains
    necessary independently of this class repair.
  finding_ids:
  - F3
  target_ids:
  - antibioticmech:aro-bd55fbe0ca
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted CARD/ARO definition, class, citations and cross-references
  acceptance_checks:
  - No enramycin-derived exact component inherits the contradicted ribosomal-synthesis
    class.
  - The class correction preserves antibacterial activity and documents original NRPS
    evidence.
  - The change survives re-extraction/reseeding and required native validation.
limitations:
- The original NRPS paper was inspected at complete-abstract level; direct full-text
  routes failed. The original 1973 structure was inspected on selected rendered pages,
  including component separation, formulas and Figure9, rather than claimed as a fully
  OCR-readable paper.
- The original mechanism abstract supports inhibition of both biochemical steps with
  lipidII/transglycosylation preferred. Exact reagent A/B ratio and hydrate state
  were not verified. No absence of MurG-step inhibition or direct protein-binding
  target is inferred.
- The sole adopted poultry study provides background claims and a metagenomic feed
  experiment. It does not experimentally establish producer biosynthesis, exact graph,
  pig disease prevention or each detected ARG as an enramycin resistance determinant.
- The separate GSRS component B has an unspecified lipid-chain stereocenter; that
  limitation is preserved and does not make B itself an experimentally demonstrated
  mixture. Native missing stereochemistry similarly does not establish the broad mixture
  finding.
- ChEMBL2109091 has no structure, so it resolves as a broad name entry without independently
  verifying the exact native chemical form.
- The first supplemental chemical comparison failed on InChI tautomer handling and
  enumeration limits. Final topology checks avoid that failed inference; the native
  chemistry gate itself passed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Standalone chemistry used batch019 Python against batch040; native schema/strict
  and ledger used batch040.
- An ignored-file-inclusive targeted search of native records, decisions, ChEBI inventory
  and source configuration found only the broad enramycin record for the checked names.
  Future component creation still requires an exhaustive exact-identifier deduplication
  step.
- 'Optional mechanistic wording can be improved during later authorized reconciliation:
  distinguish substrate sequestration and primary cellular action from an unqualified
  MurG-only explanation, without deleting genuine biochemical MurG inhibition.'
- No native scientific status was changed. The source-defined mixture, graph defect
  and biosynthetic-class contradiction are separate findings with separate maintained
  owners.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://gsrs.ncats.nih.gov/api/v1/substances/4GP7CLG9EG
- https://gsrs.ncats.nih.gov/api/v1/substances/09I5H1AG37
- https://gsrs.ncats.nih.gov/api/v1/substances/5TQ7Z201B8
- https://doi.org/10.1248/cpb.21.1184
- https://doi.org/10.1099/mic.0.29043-0
- https://doi.org/10.1039/B515328J
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9293667/
tags:
- record-review
- enramycin
- mixture-boundary
- nonribosomal-peptide
```
