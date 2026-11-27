# Review of efrotomycin

- Review: 20261021T152457Z-efrotomycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:03:42Z
- Finished UTC: 2026-10-21T15:24:57Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The adopted structure is internally consistent but has E geometry at original-paper C37=C38, whereas the original numbered structure and independently mapped GSRS, KEGG and full PubChem structure have Z. All 21 tetrahedral centers are also unspecified in the adopted structure. The definition generalizes cell-free EF-Tu sensitivity into whole-cell Gram-group susceptibility, contrary to the cited source scope and original narrow-spectrum studies. The historical producer name contains an extra letter. Three findings require maintained-source corrections; class and exact-compound antibacterial activity remain supported.

## Scope And Provenance

Whole SEEDED, MINTED efrotomycin record: complete definition and sole selected definition citation, broader elfamycin parent/class, PubChem structure with all stereochemical descriptors and masses, three cross-references, source concept and three histories. All four adopted definition references and both parent-class references inspected at the stated levels.

Selection: Queue 395 in isolated batch 040. Initial 13 hashes preserved; actual ARO/PubChem owners appended before detailed assessment for 16 unchanged inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-5d5ecfee72 | data/antibiotics/antibacterial/efrotomycin.yaml | generated | efrotomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native schema | passed | True | antibioticmech:aro-5d5ecfee72 | Exit 0. |
| Native strict terms | passed | True | antibioticmech:aro-5d5ecfee72 | Exit 0; no ERROR rows. |
| Native internal chemical consistency | passed | False | antibioticmech:aro-5d5ecfee72 | Native fields are internally consistent; this does not establish agreement with authentic efrotomycin stereochemistry. |
| Initial direct graph comparison | failed | False | antibioticmech:aro-5d5ecfee72 | Executed initial script failed on the InChI-reader tautomer. Its exact script and log were preserved before explicit normalization. |
| Explicit mapped authority comparison | passed | False | antibioticmech:aro-5d5ecfee72 | Eight encodings compared, with stereo-preserving tautomer handling where needed. The audit detects one named-alkene conflict; agreement assertions for GSRS/KEGG/full PubChem pass. |
| Structured EF-Tu follow-up | passed | False | antibioticmech:aro-5d5ecfee72 | Dataset discovery and four searches completed before primary web follow-up; tufA/tufB gene keys resolved without component hits. |
| Whole source, citation and history ledger | passed | False | antibioticmech:aro-5d5ecfee72 | All 16 input hashes unchanged, four adopted references disposed, exact source projection and three ordered histories checked. |
| Authoritative full QC | failed | True | antibioticmech:aro-5d5ecfee72 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-5d5ecfee72 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-5d5ecfee72 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-5d5ecfee72 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-5d5ecfee72 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-5d5ecfee72 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-5d5ecfee72 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-5d5ecfee72 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-5d5ecfee72 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Mapped natural-product stereochemistry

identity: concern. Targets: antibioticmech:aro-5d5ecfee72.

Named C37=C38 geometry conflicts with original structure and mutually agreeing full authorities; all 21 native tetrahedral centers are unspecified.

### Whole-cell versus EF-Tu assay scope

scope: concern. Targets: antibioticmech:aro-5d5ecfee72.

The native Gram-group generalization does not describe the inspected whole-cell experiments or cited cell-free assays.

### Exact historical producer name

nomenclature: concern. Targets: antibioticmech:aro-5d5ecfee72.

The original producer is lactamdurans, not lactamodurans; genus changes require separate grounded taxonomy.

### Antibacterial role and elfamycin parent

evidence: supported. Targets: antibioticmech:aro-5d5ecfee72.

Exact-compound bacterial experiments and EF-Tu inhibition support the filing class and family; the spectrum defect does not erase antibacterial activity.

### Historical swine use and present authorization

scope: supported. Targets: antibioticmech:aro-5d5ecfee72.

Original feeding experiments support historical use; no current approval claim is introduced.

### Optional mechanism representations

completeness: supported. Targets: antibioticmech:aro-5d5ecfee72.

The record has no unsupported direct-target object. Later authorized curation can add a scoped EF-Tu/protein-synthesis representation after correcting identity; optional missing slots are not independently treated as defects.

### All adopted citations and generated owners

provenance: supported. Targets: antibioticmech:aro-5d5ecfee72.

Four adopted leads and both parent references disposed; source projection, 16 hashes and three histories checked.

## Findings

### F1: The encoded terminal alkene differs from authentic efrotomycin

major / open / confirmed; issue key: efrotomycin-native-terminal-diene-e-versus-primary-z.

The unique terminal C37=C38 is E in the adopted graph and PubChem 135434844, whereas the original numbered structure is Z and agrees with GSRS, KEGG and PubChem 135564847. Current ChEMBL 2106443 repeats E despite specifying the tetrahedral centers. The native structure additionally omits all 21 published tetrahedral assignments. Missing assignments do not establish a mixture, but the positive E/Z conflict requires an identity correction and exact-link reconciliation.

### F2: A biochemical sensitivity pattern is overstated as a whole-cell Gram-group rule

major / open / confirmed; issue key: efrotomycin-ef-tu-sensitivity-generalized-to-whole-cell-spectrum.

The native sentence says Gram-negative bacteria are generally susceptible and Gram-positive bacteria resistant. The selected primary citation explicitly distinguishes intact cells from cell-free systems, while the original antibacterial study reports a narrow mixed-genus spectrum. Correct the scope rather than simply reversing the Gram-group rule.

### F3: The historical producer species is misspelled

minor / open / confirmed; issue key: efrotomycin-producer-lactamodurans-misspelling.

The original NRRL 3802 culture report spells the historical name Streptomyces lactamdurans. Native lactamodurans adds an unsupported o. The later structure paper uses Nocardia lactamdurans; this review does not force an unverified modern genus mapping.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, correct the exact efrotomycin source mapping upstream or through a narrow maintained normalization, then refresh the PubChem enrichment and reseed. PubChem 135564847, GSRS 5BPJ82Q45X and KEGG D03964 provide mutually mapped full-structure candidates. Adopt the primary-supported C37=C38 Z configuration and verify every tetrahedral assignment; reconcile or remove the conflicting exact ChEMBL link until corrected. Do not only patch the generated YAML or infer a racemate from absent descriptors.

- The regenerated molecule has the original numbered C37=C38 Z geometry and the justified full stereochemical assignments, with documented atom mapping.
- Every retained exact cross-reference denotes the same stereo/form unit; native SMILES, InChI, key, formula, charge and masses agree.
- Required native schema/strict, corpus/reference/history and review gates pass after authorized extraction/reseeding.

### A2

Correct the ARO source definition upstream and refresh extraction, or implement a narrowly scoped maintained text transform before reseeding. Describe narrow strain/species-dependent whole-cell activity separately from EF-Tu sensitivity in cell-free experiments; correct lactamdurans and attach the original producer, activity and historical swine sources at their proper claims. The existing classification-only aro_definition_overrides key does not implement such a text correction.

- No blanket Gram-negative susceptible/Gram-positive resistant rule remains.
- The historical producer name and NRRL 3802 are faithful to the original culture report; any modern taxon is separately grounded.
- The selected definition citation or an explicit evidence representation supports each retained clause rather than implying that PMID:1590753 established producer and swine use.
- The correction survives source extraction/reseeding and all required native checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/efrotomycin.yaml; Entire native YAML | supports | The native record represents a neutral monomer and an ARO-minted source concept. It contains no dedicated target, MIC, resistance, producer, clinical-status or causal-graph entries. The three source-derived histories remain ordered. |
| chemistry | PubChem135434844 and135564847; ChEMBL2106443; GSRS5BPJ82Q45X; KEGG D03964; 395-pubchem.json;395-pubchem-name.json;395-chembl.json;395-gsrs.json;395-kegg.mol;395-authority-chemistry.json | refutes | All encodings have C59H88N2O20, one neutral component and identical heavy-atom connectivity. Native/adopted PubChem has all 21 tetrahedral centers unassigned and terminal C37=C38 E; current ChEMBL assigns21 centers but retains E. GSRS, KEGG and PubChem 135564847 have Z at the same uniquely mapped bond, retain all 21 assigned centers, and reciprocally match with chirality enabled. The native key OUYMVFBDSA, ChEMBL HCHBIZCOSA and fully specified SBHXXGSWSA encode these real distinctions. This is not inferred from raw slash notation, a conformer or a mixture assumption. |
| structure | PMID:4093333; DOI:10.7164/antibiotics.38.1691; 395-structure1985.pdf full main text; printedp1692 structureI and p1695 Table4, inspected rendered pages | refutes | The original numbered structure places C36 and C39 on the same side of C37=C38, hence Z; the terminal carbon on each alkene atom outranks its hydrogen. Table 4 reports H38 coupling11Hz, consistent with the drawn geometry. The paper establishes the absolute disaccharide configuration by degradation and comparison, beta linkage by coupling, and assigns the aurodox aglycone by close spectral comparison; it explicitly distinguishes that evidential basis from independent whole-molecule crystallography. |
| discovery | PMID:950325; DOI:10.7164/antibiotics.29.670; 395-original1976.pdf whole4-page report; culture/strain text and printedp672 activity paragraph visually checked | refutes | The producer is historical Streptomyces lactamdurans NRRL 3802, not lactamodurans. Culture, recovery and purification establish biosynthesis rather than mere isolation from an environmental sample. The report describes stronger Gram-positive activity in its panel, directly conflicting with the native generalization. Its provisional family comparison is not a substitute for the later exact structure paper. |
| whole-cell | DOI:10.7164/antibiotics.29.1083; 395-activity1976.pdf; printedp1083 abstract/material and agar methods; Table1 spectrum inspection | refutes | Efrotomycin greater than 90% purity was tested in a species/strain panel using brain-heart medium with serum when needed and 24/48-hour readings. Susceptible genera include both Gram-negative and Gram-positive members, notably Moraxella, Pasteurella, Yersinia, Haemophilus, Streptococcus and Corynebacterium. The paper describes a narrow spectrum, not a reliable Gram-group split. Quantitative table cells are not adopted into native MIC fields by this review. |
| ef-tu | PMID:1590753; PMID:8515234; 395-core-1590753.json and395-core-8515234.json complete original abstracts | refutes | The selected definition citation1590753 describes efrotomycin as inactive against intact E.coli and B.subtilis while their reconstituted cell-free systems differ. PMID:8515234 tests species EF-Tu through cell-free synthesis and GDP exchange: Gram-negative EF-Tu sensitivity is not whole-cell antibacterial susceptibility. These originals support EF-Tu-directed protein-synthesis inhibition at their biochemical scope, without a directly inspected efrotomycin co-crystal. |
| swine | PMID:3667459; PMID:3073676; 395-core-3667459.json and395-core-3073676.json complete original abstracts | context_only | The 1987 study reports six feeding trials involving 700 pigs and supports historical swine growth/feed-efficiency use. The 1988 inoculated-pig study found no appreciable treatment differences in its shedding and performance endpoints. Different designs are preserved. Neither study establishes present regulatory authorization or makes feed-growth outcomes a direct antibacterial MIC. |
| terms | ARO:3001236; ARO:3001219; ARO:3001310; 395-aro-blocks.json extracted from374-current-aro.obo;374-fetch-results.json | supports | All native ARO identifiers resolve. The current source repeats the faulty definition and exact PubChem/ChEMBL links. Kirromycin-like antibiotics remain narrower than elfamycin; the native broader class follows the maintained drug-class projection. The two parent-reference review abstracts are contextual; aurodox or GE2270 structures cannot be attributed to efrotomycin. |
| leads | Four adopted definition references; two class references; exact structural and animal-study follow-ups; 395-source-audit.json;395-core-*.json;395-new-congeners-core.json | context_only | All four adopted references are explicitly disposed: 950325 full discovery report, 1590753 and 8515234 complete original abstracts, 16677683 environmental veterinary-antibiotic review abstract. The two class references 12370016/16876786 were read as reviews. PMID:36445346 concerns new A1-A4/B1 congeners and a distinct producer/heterologous host; those identities and producer claims are not silently transferred to original efrotomycin. |
| adapter | iModulonDB e_coli/modulome; 395-adapter-results.json | context_only | Dataset discovery and searches for efrotomycin, tufA, tufB and elongation factor Tu preceded mechanism web follow-up. tufA and tufB resolve to b3339 and b3980; no component hit required summarization. Gene catalog membership supplies context only, not direct binding, susceptibility or producer evidence. |
| owners | ARO inventory, PubChem enrichment and seeder; 395-owner-append.json;395-raw-rows.json;395-source-audit.json; scripts/seed_from_sources.py build_concepts and definition selection | supports | All 16 hashes remain unchanged, including all 13 initial inputs. The ARO row owns the definition and exact cross-references; PubChem enrichment owns the graph. The seeder selects the first of four ARO references as definition_source, explaining its excessive apparent scope. Current aro_definition_overrides changes classification, not arbitrary definition text; future correction needs upstream source repair or a deliberately implemented maintained transform. |
| validation | Executed focused and supplementary checks; 395-focused-results.json;395-strict.tsv;395-authority-chemistry-initial.log;395-authority-chemistry.log;395-ledger.log | supports | Native chemistry/schema/strict pass. The preserved direct authority check failed on an InChI-reader tautomer; explicit normalization with bond and tetrahedral stereo removal disabled allows the final mapped audit to pass while reporting the genuine alkene disagreement. |
| access | Bounded exact-record source access; 395-local-hits.txt includes ignored files;395-fetch.json through395-fetch5.json | context_only | Original 1976 discovery/activity and 1985 structure PDFs were retrieved. The 1992 PMC XML returned 500 and its apparent PDF returned HTML; the 1993 publisher returned 403. Both complete original abstracts were available. The 2022 supplement response was empty 202. No inaccessible full text is claimed as inspected. |

## Limits And Additional Notes

- The complete 1992/1993 biochemical papers were inaccessible in attempted routes; their complete abstracts were inspected. The original 1976 activity/discovery and 1985 structure papers were available.
- The 1985 assignment uses direct carbohydrate characterization and an aurodox aglycone comparison, not an independently determined whole-molecule crystal. Current full authorities agree with the original drawn terminal geometry and each other.
- Native missing tetrahedral descriptors are not evidence of a mixture. Current ChEMBL and adopted PubChem conflict with primary-supported terminal geometry; their disagreement remains explicit.
- No quantitative MIC row or current regulatory/marketing assertion is added. Historical feed studies and modern new-congener work retain their exact material and experimental contexts.
- The initial direct graph check failed on the InChI-reader tautomer. Intermediate diagnostic development also encountered RDKit CIS/TRANS rather than E/Z enum names; the final audit uses the named carbon/hydrogen substituents and retains the original encodings.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Standalone chemistry used the batch 019 interpreter against batch 040; native schema/strict and source ledger used batch 040.
- The native record remains SEEDED. Optional EF-Tu enrichment is not a reason to promote scientific status or to copy a different elfamycin co-crystal.
- The current ARO snapshot is374-current-aro.obo, retrieved 2026-10-21T14:50:57Z with SHA256d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T152457Z-efrotomycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of efrotomycin
started_at: '2026-10-21T15:03:42Z'
finished_at: '2026-10-21T15:24:57Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Whole native and maintained source rows read; all adopted references
    resolved; original discovery and structural papers inspected; atom-mapped geometry
    and full-authority stereochemistry independently compared; original whole-cell
    and EF-Tu assay scopes separated.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Major terminal-diene geometry and antibacterial-spectrum defects;
  minor producer spelling
scientific_review: true
summary: The adopted structure is internally consistent but has E geometry at original-paper
  C37=C38, whereas the original numbered structure and independently mapped GSRS,
  KEGG and full PubChem structure have Z. All 21 tetrahedral centers are also unspecified
  in the adopted structure. The definition generalizes cell-free EF-Tu sensitivity
  into whole-cell Gram-group susceptibility, contrary to the cited source scope and
  original narrow-spectrum studies. The historical producer name contains an extra
  letter. Three findings require maintained-source corrections; class and exact-compound
  antibacterial activity remain supported.
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
  - path: data/antibiotics/antibacterial/efrotomycin.yaml
    sha256: 14ca62f268b3c49fff1e5e83e4bcf7baa516c589284cf9600811c27bb1309768
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
  description: 'Whole SEEDED, MINTED efrotomycin record: complete definition and sole
    selected definition citation, broader elfamycin parent/class, PubChem structure
    with all stereochemical descriptors and masses, three cross-references, source
    concept and three histories. All four adopted definition references and both parent-class
    references inspected at the stated levels.'
  selection: Queue 395 in isolated batch 040. Initial 13 hashes preserved; actual
    ARO/PubChem owners appended before detailed assessment for 16 unchanged inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-5d5ecfee72
targets:
- target_id: antibioticmech:aro-5d5ecfee72
  path: data/antibiotics/antibacterial/efrotomycin.yaml
  label: efrotomycin
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
    data/antibiotics/antibacterial/efrotomycin.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  evidence_ids:
  - validation
- check_id: strict
  name: Native strict terms
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/efrotomycin.yaml --out /private/tmp/am-review-session/395-strict.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no ERROR rows.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  evidence_ids:
  - validation
- check_id: native-chemistry
  name: Native internal chemical consistency
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    395 > /private/tmp/am-review-session/395-focused-run.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Native fields are internally consistent; this does not establish agreement
    with authentic efrotomycin stereochemistry.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  evidence_ids:
  - chemistry
  - validation
- check_id: direct-comparison
  name: Initial direct graph comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/395-authority-chemistry-initial.py
    > /private/tmp/am-review-session/395-authority-chemistry-initial.log 2>&1
  status: failed
  required: false
  exit_code: 1
  expected_exit_code: 0
  summary: Executed initial script failed on the InChI-reader tautomer. Its exact
    script and log were preserved before explicit normalization.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  evidence_ids:
  - chemistry
- check_id: mapped-comparison
  name: Explicit mapped authority comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/395-authority-chemistry.py
    > /private/tmp/am-review-session/395-authority-chemistry.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Eight encodings compared, with stereo-preserving tautomer handling where
    needed. The audit detects one named-alkene conflict; agreement assertions for
    GSRS/KEGG/full PubChem pass.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  evidence_ids:
  - chemistry
  - structure
- check_id: adapter
  name: Structured EF-Tu follow-up
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/395-adapter.py
    > /private/tmp/am-review-session/395-adapter.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Dataset discovery and four searches completed before primary web follow-up;
    tufA/tufB gene keys resolved without component hits.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  evidence_ids:
  - adapter
- check_id: source-ledger
  name: Whole source, citation and history ledger
  command: .venv/bin/python /private/tmp/am-review-session/395-ledger.py > /private/tmp/am-review-session/395-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All 16 input hashes unchanged, four adopted references disposed, exact
    source projection and three ordered histories checked.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  evidence_ids:
  - owners
  - leads
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-5d5ecfee72
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
  - antibioticmech:aro-5d5ecfee72
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
  - antibioticmech:aro-5d5ecfee72
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
  - antibioticmech:aro-5d5ecfee72
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
  - antibioticmech:aro-5d5ecfee72
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
  - antibioticmech:aro-5d5ecfee72
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
  - antibioticmech:aro-5d5ecfee72
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
  - antibioticmech:aro-5d5ecfee72
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
  - antibioticmech:aro-5d5ecfee72
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/efrotomycin.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T15:21:09Z'
  support: supports
  summary: The native record represents a neutral monomer and an ARO-minted source
    concept. It contains no dedicated target, MIC, resistance, producer, clinical-status
    or causal-graph entries. The three source-derived histories remain ordered.
- evidence_id: chemistry
  kind: authority
  reference: PubChem135434844 and135564847; ChEMBL2106443; GSRS5BPJ82Q45X; KEGG D03964
  locator: 395-pubchem.json;395-pubchem-name.json;395-chembl.json;395-gsrs.json;395-kegg.mol;395-authority-chemistry.json
  accessed_at: '2026-10-21T15:21:09Z'
  support: refutes
  summary: All encodings have C59H88N2O20, one neutral component and identical heavy-atom
    connectivity. Native/adopted PubChem has all 21 tetrahedral centers unassigned
    and terminal C37=C38 E; current ChEMBL assigns21 centers but retains E. GSRS,
    KEGG and PubChem 135564847 have Z at the same uniquely mapped bond, retain all
    21 assigned centers, and reciprocally match with chirality enabled. The native
    key OUYMVFBDSA, ChEMBL HCHBIZCOSA and fully specified SBHXXGSWSA encode these
    real distinctions. This is not inferred from raw slash notation, a conformer or
    a mixture assumption.
  snapshot_sha256: 72442b9bcb96ac5884977b440bd8305d1e2c2775ee5c968203c42bfc6b46b10e
- evidence_id: structure
  kind: primary_source
  reference: PMID:4093333; DOI:10.7164/antibiotics.38.1691
  locator: 395-structure1985.pdf full main text; printedp1692 structureI and p1695
    Table4, inspected rendered pages
  accessed_at: '2026-10-21T15:14:30.417393Z'
  support: refutes
  summary: The original numbered structure places C36 and C39 on the same side of
    C37=C38, hence Z; the terminal carbon on each alkene atom outranks its hydrogen.
    Table 4 reports H38 coupling11Hz, consistent with the drawn geometry. The paper
    establishes the absolute disaccharide configuration by degradation and comparison,
    beta linkage by coupling, and assigns the aurodox aglycone by close spectral comparison;
    it explicitly distinguishes that evidential basis from independent whole-molecule
    crystallography.
  snapshot_sha256: 88d4235a49e40ffbcfe3471eebc74e7ff7bb67e58ff38fcdd804839623308d7b
- evidence_id: discovery
  kind: primary_source
  reference: PMID:950325; DOI:10.7164/antibiotics.29.670
  locator: 395-original1976.pdf whole4-page report; culture/strain text and printedp672
    activity paragraph visually checked
  accessed_at: '2026-10-21T15:14:11.221766Z'
  support: refutes
  summary: The producer is historical Streptomyces lactamdurans NRRL 3802, not lactamodurans.
    Culture, recovery and purification establish biosynthesis rather than mere isolation
    from an environmental sample. The report describes stronger Gram-positive activity
    in its panel, directly conflicting with the native generalization. Its provisional
    family comparison is not a substitute for the later exact structure paper.
  snapshot_sha256: cdbf218b1732b1c25407044896dcb0cafaedce06dff0b2a7452316aa9f9ead2d
- evidence_id: whole-cell
  kind: primary_source
  reference: DOI:10.7164/antibiotics.29.1083
  locator: 395-activity1976.pdf; printedp1083 abstract/material and agar methods;
    Table1 spectrum inspection
  accessed_at: '2026-10-21T15:14:30.417644Z'
  support: refutes
  summary: Efrotomycin greater than 90% purity was tested in a species/strain panel
    using brain-heart medium with serum when needed and 24/48-hour readings. Susceptible
    genera include both Gram-negative and Gram-positive members, notably Moraxella,
    Pasteurella, Yersinia, Haemophilus, Streptococcus and Corynebacterium. The paper
    describes a narrow spectrum, not a reliable Gram-group split. Quantitative table
    cells are not adopted into native MIC fields by this review.
  snapshot_sha256: 017a222b1fe35240c5f1063f0aedce33c9481a5124b833ed7700367bd5713116
- evidence_id: ef-tu
  kind: primary_source
  reference: PMID:1590753; PMID:8515234
  locator: 395-core-1590753.json and395-core-8515234.json complete original abstracts
  accessed_at: '2026-10-21T15:13:43.349591Z'
  support: refutes
  summary: 'The selected definition citation1590753 describes efrotomycin as inactive
    against intact E.coli and B.subtilis while their reconstituted cell-free systems
    differ. PMID:8515234 tests species EF-Tu through cell-free synthesis and GDP exchange:
    Gram-negative EF-Tu sensitivity is not whole-cell antibacterial susceptibility.
    These originals support EF-Tu-directed protein-synthesis inhibition at their biochemical
    scope, without a directly inspected efrotomycin co-crystal.'
  snapshot_sha256: 70c2fc503a8621201fefe59f484aa5410bced087ccc76ea2205b4fab7d970942
- evidence_id: swine
  kind: primary_source
  reference: PMID:3667459; PMID:3073676
  locator: 395-core-3667459.json and395-core-3073676.json complete original abstracts
  accessed_at: '2026-10-21T15:18:21.683304Z'
  support: context_only
  summary: The 1987 study reports six feeding trials involving 700 pigs and supports
    historical swine growth/feed-efficiency use. The 1988 inoculated-pig study found
    no appreciable treatment differences in its shedding and performance endpoints.
    Different designs are preserved. Neither study establishes present regulatory
    authorization or makes feed-growth outcomes a direct antibacterial MIC.
  snapshot_sha256: 7270d52dd8c23a427aa9f3dbd7f2f8ec472630842d52c1ebb5d75a0776fd1c7b
- evidence_id: terms
  kind: authority
  reference: ARO:3001236; ARO:3001219; ARO:3001310
  locator: 395-aro-blocks.json extracted from374-current-aro.obo;374-fetch-results.json
  accessed_at: '2026-10-21T15:21:09Z'
  support: supports
  summary: All native ARO identifiers resolve. The current source repeats the faulty
    definition and exact PubChem/ChEMBL links. Kirromycin-like antibiotics remain
    narrower than elfamycin; the native broader class follows the maintained drug-class
    projection. The two parent-reference review abstracts are contextual; aurodox
    or GE2270 structures cannot be attributed to efrotomycin.
  snapshot_sha256: 53e273a0f582229aa13d851dfa0b52fb026122acbd1b8d40a25a4787b31ccefc
- evidence_id: leads
  kind: primary_source
  reference: Four adopted definition references; two class references; exact structural
    and animal-study follow-ups
  locator: 395-source-audit.json;395-core-*.json;395-new-congeners-core.json
  accessed_at: '2026-10-21T15:21:09Z'
  support: context_only
  summary: 'All four adopted references are explicitly disposed: 950325 full discovery
    report, 1590753 and 8515234 complete original abstracts, 16677683 environmental
    veterinary-antibiotic review abstract. The two class references 12370016/16876786
    were read as reviews. PMID:36445346 concerns new A1-A4/B1 congeners and a distinct
    producer/heterologous host; those identities and producer claims are not silently
    transferred to original efrotomycin.'
  snapshot_sha256: 27f6982162fd491a0989445c39de6f228ef91522441c198904bcbaf2a8684da6
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/modulome
  locator: 395-adapter-results.json
  accessed_at: '2026-10-21T15:21:09Z'
  support: context_only
  summary: Dataset discovery and searches for efrotomycin, tufA, tufB and elongation
    factor Tu preceded mechanism web follow-up. tufA and tufB resolve to b3339 and
    b3980; no component hit required summarization. Gene catalog membership supplies
    context only, not direct binding, susceptibility or producer evidence.
  snapshot_sha256: 3f30dcc933f5d1dcf98044fe23e195822bb512c1ca752ad864351052caac200a
- evidence_id: owners
  kind: database
  reference: ARO inventory, PubChem enrichment and seeder
  locator: 395-owner-append.json;395-raw-rows.json;395-source-audit.json; scripts/seed_from_sources.py
    build_concepts and definition selection
  accessed_at: '2026-10-21T15:21:09Z'
  support: supports
  summary: All 16 hashes remain unchanged, including all 13 initial inputs. The ARO
    row owns the definition and exact cross-references; PubChem enrichment owns the
    graph. The seeder selects the first of four ARO references as definition_source,
    explaining its excessive apparent scope. Current aro_definition_overrides changes
    classification, not arbitrary definition text; future correction needs upstream
    source repair or a deliberately implemented maintained transform.
  snapshot_sha256: 27f6982162fd491a0989445c39de6f228ef91522441c198904bcbaf2a8684da6
- evidence_id: validation
  kind: validation
  reference: Executed focused and supplementary checks
  locator: 395-focused-results.json;395-strict.tsv;395-authority-chemistry-initial.log;395-authority-chemistry.log;395-ledger.log
  accessed_at: '2026-10-21T15:21:09Z'
  support: supports
  summary: Native chemistry/schema/strict pass. The preserved direct authority check
    failed on an InChI-reader tautomer; explicit normalization with bond and tetrahedral
    stereo removal disabled allows the final mapped audit to pass while reporting
    the genuine alkene disagreement.
  snapshot_sha256: f26618dcd5ecaaa95675f93a9e34f2443f110eaaa3e64c9aed7d52376fe19474
- evidence_id: access
  kind: search
  reference: Bounded exact-record source access
  locator: 395-local-hits.txt includes ignored files;395-fetch.json through395-fetch5.json
  accessed_at: '2026-10-21T15:21:09Z'
  support: context_only
  summary: Original 1976 discovery/activity and 1985 structure PDFs were retrieved.
    The 1992 PMC XML returned 500 and its apparent PDF returned HTML; the 1993 publisher
    returned 403. Both complete original abstracts were available. The 2022 supplement
    response was empty 202. No inaccessible full text is claimed as inspected.
  snapshot_sha256: 60ea7101da45518971fdbeeb44faa0ebfac9dcf035fb42c91a412fb50eb248a6
  search_scope: 395-local-hits.txt includes ignored files;395-fetch.json through395-fetch5.json
assessments:
- assessment_id: identity
  area: identity
  topic: Mapped natural-product stereochemistry
  outcome: concern
  summary: Named C37=C38 geometry conflicts with original structure and mutually agreeing
    full authorities; all 21 native tetrahedral centers are unspecified.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  evidence_ids:
  - chemistry
  - structure
- assessment_id: activity
  area: scope
  topic: Whole-cell versus EF-Tu assay scope
  outcome: concern
  summary: The native Gram-group generalization does not describe the inspected whole-cell
    experiments or cited cell-free assays.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  evidence_ids:
  - whole-cell
  - ef-tu
  - discovery
- assessment_id: producer
  area: nomenclature
  topic: Exact historical producer name
  outcome: concern
  summary: The original producer is lactamdurans, not lactamodurans; genus changes
    require separate grounded taxonomy.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  evidence_ids:
  - discovery
  - structure
- assessment_id: class
  area: evidence
  topic: Antibacterial role and elfamycin parent
  outcome: supported
  summary: Exact-compound bacterial experiments and EF-Tu inhibition support the filing
    class and family; the spectrum defect does not erase antibacterial activity.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  evidence_ids:
  - whole-cell
  - ef-tu
  - terms
- assessment_id: use
  area: scope
  topic: Historical swine use and present authorization
  outcome: supported
  summary: Original feeding experiments support historical use; no current approval
    claim is introduced.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  evidence_ids:
  - swine
- assessment_id: completeness
  area: completeness
  topic: Optional mechanism representations
  outcome: supported
  summary: The record has no unsupported direct-target object. Later authorized curation
    can add a scoped EF-Tu/protein-synthesis representation after correcting identity;
    optional missing slots are not independently treated as defects.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  evidence_ids:
  - record
  - ef-tu
- assessment_id: provenance
  area: provenance
  topic: All adopted citations and generated owners
  outcome: supported
  summary: Four adopted leads and both parent references disposed; source projection,
    16 hashes and three histories checked.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  evidence_ids:
  - leads
  - owners
  - validation
findings:
- finding_id: F1
  issue_key: efrotomycin-native-terminal-diene-e-versus-primary-z
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The encoded terminal alkene differs from authentic efrotomycin
  description: The unique terminal C37=C38 is E in the adopted graph and PubChem 135434844,
    whereas the original numbered structure is Z and agrees with GSRS, KEGG and PubChem
    135564847. Current ChEMBL 2106443 repeats E despite specifying the tetrahedral
    centers. The native structure additionally omits all 21 published tetrahedral
    assignments. Missing assignments do not establish a mixture, but the positive
    E/Z conflict requires an identity correction and exact-link reconciliation.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  field_paths:
  - chemical_structure
  - xrefs[1]
  - xrefs[2]
  evidence_ids:
  - chemistry
  - structure
  - owners
  rule_id: 'review-checklist: exact structure, claim scope and source support'
  native_severity: Major scientific/source correction
  normalization_reason: The intended compound and connectivity remain identifiable,
    but its specific alkene geometry is wrong; this is major rather than a blanket
    wrong-record blocker.
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
- finding_id: F2
  issue_key: efrotomycin-ef-tu-sensitivity-generalized-to-whole-cell-spectrum
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: A biochemical sensitivity pattern is overstated as a whole-cell Gram-group
    rule
  description: The native sentence says Gram-negative bacteria are generally susceptible
    and Gram-positive bacteria resistant. The selected primary citation explicitly
    distinguishes intact cells from cell-free systems, while the original antibacterial
    study reports a narrow mixed-genus spectrum. Correct the scope rather than simply
    reversing the Gram-group rule.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - ef-tu
  - whole-cell
  - discovery
  - owners
  rule_id: 'review-checklist: exact structure, claim scope and source support'
  native_severity: Major scientific/source correction
  normalization_reason: The error changes the asserted antibacterial spectrum and
    transfers target-level results to whole organisms; it is more than stylistic wording.
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
- finding_id: F3
  issue_key: efrotomycin-producer-lactamodurans-misspelling
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: The historical producer species is misspelled
  description: The original NRRL 3802 culture report spells the historical name Streptomyces
    lactamdurans. Native lactamodurans adds an unsupported o. The later structure
    paper uses Nocardia lactamdurans; this review does not force an unverified modern
    genus mapping.
  target_ids:
  - antibioticmech:aro-5d5ecfee72
  field_paths:
  - definition
  evidence_ids:
  - discovery
  - structure
  - owners
  rule_id: 'review-checklist: exact structure, claim scope and source support'
  native_severity: Minor scientific/source correction
  normalization_reason: The strain number and intended producer remain recognizable;
    the bounded defect is a non-blocking nomenclature/provenance error.
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
  description: In separately authorized curation, correct the exact efrotomycin source
    mapping upstream or through a narrow maintained normalization, then refresh the
    PubChem enrichment and reseed. PubChem 135564847, GSRS 5BPJ82Q45X and KEGG D03964
    provide mutually mapped full-structure candidates. Adopt the primary-supported
    C37=C38 Z configuration and verify every tetrahedral assignment; reconcile or
    remove the conflicting exact ChEMBL link until corrected. Do not only patch the
    generated YAML or infer a racemate from absent descriptors.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-5d5ecfee72
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
  - The regenerated molecule has the original numbered C37=C38 Z geometry and the
    justified full stereochemical assignments, with documented atom mapping.
  - Every retained exact cross-reference denotes the same stereo/form unit; native
    SMILES, InChI, key, formula, charge and masses agree.
  - Required native schema/strict, corpus/reference/history and review gates pass
    after authorized extraction/reseeding.
- action_id: A2
  description: Correct the ARO source definition upstream and refresh extraction,
    or implement a narrowly scoped maintained text transform before reseeding. Describe
    narrow strain/species-dependent whole-cell activity separately from EF-Tu sensitivity
    in cell-free experiments; correct lactamdurans and attach the original producer,
    activity and historical swine sources at their proper claims. The existing classification-only
    aro_definition_overrides key does not implement such a text correction.
  finding_ids:
  - F2
  - F3
  target_ids:
  - antibioticmech:aro-5d5ecfee72
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
  - No blanket Gram-negative susceptible/Gram-positive resistant rule remains.
  - The historical producer name and NRRL 3802 are faithful to the original culture
    report; any modern taxon is separately grounded.
  - The selected definition citation or an explicit evidence representation supports
    each retained clause rather than implying that PMID:1590753 established producer
    and swine use.
  - The correction survives source extraction/reseeding and all required native checks.
limitations:
- The complete 1992/1993 biochemical papers were inaccessible in attempted routes;
  their complete abstracts were inspected. The original 1976 activity/discovery and
  1985 structure papers were available.
- The 1985 assignment uses direct carbohydrate characterization and an aurodox aglycone
  comparison, not an independently determined whole-molecule crystal. Current full
  authorities agree with the original drawn terminal geometry and each other.
- Native missing tetrahedral descriptors are not evidence of a mixture. Current ChEMBL
  and adopted PubChem conflict with primary-supported terminal geometry; their disagreement
  remains explicit.
- No quantitative MIC row or current regulatory/marketing assertion is added. Historical
  feed studies and modern new-congener work retain their exact material and experimental
  contexts.
- The initial direct graph check failed on the InChI-reader tautomer. Intermediate
  diagnostic development also encountered RDKit CIS/TRANS rather than E/Z enum names;
  the final audit uses the named carbon/hydrogen substituents and retains the original
  encodings.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Standalone chemistry used the batch 019 interpreter against batch 040; native schema/strict
  and source ledger used batch 040.
- The native record remains SEEDED. Optional EF-Tu enrichment is not a reason to promote
  scientific status or to copy a different elfamycin co-crystal.
- The current ARO snapshot is374-current-aro.obo, retrieved 2026-10-21T14:50:57Z with
  SHA256d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.7164/antibiotics.38.1691
- https://doi.org/10.7164/antibiotics.29.670
- https://doi.org/10.7164/antibiotics.29.1083
- https://pubmed.ncbi.nlm.nih.gov/1590753/
- https://pubmed.ncbi.nlm.nih.gov/8515234/
- https://pubchem.ncbi.nlm.nih.gov/compound/135564847
- https://www.kegg.jp/entry/D03964
tags:
- record-review
- efrotomycin
- stereochemistry
- assay-scope
```
