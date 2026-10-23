# Cefuzonam: coherent neutral identity and antibacterial evidence with salt and terminology qualifications

- Review: 20261021T122757Z-cefuzonam
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:02:27Z
- Finished UTC: 2026-10-21T12:27:57Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The record consistently denotes neutral cefuzonam, with matching structure, names, source mint and resolved official chemical graphs. Antibacterial filing and retained roles are supported. Original papers support activity and PBP competition, but the mechanistic material is explicitly cefuzonam sodium and other assays do not resolve the counterion. ChEBI uses second generation while two adopted papers use third generation; this is preserved as a source terminology difference without asserting a wrong structure. No confirmed corrective finding emerged. Optional primary mechanism enrichment and several access or form qualifications remain. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire native YAML: definition, four synonyms, broader cephalosporin parent, two roles, all structure descriptors, CAS/Reaxys identifiers, DrugCentral/KEGG drug links, encyclopedia link, sole ChEBI source concept and four history events. All six adopted literature records were checked, with original full text or selected sections read as documented.

Selection: Queue 266; initial thirteen source/input hashes captured before assessment and preserved unchanged. The sole actual seed owner is the captured ChEBI row and its extractor/seeder path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:55488 | data/antibiotics/antibacterial/cefuzonam.yaml | generated | cefuzonam |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:55488 | No schema issues found. |
| strict | passed | True | CHEBI:55488 | One exact file scanned, zero strict errors. |
| chemistry | passed | False | CHEBI:55488 | Supplementary RDKit check from batch027 cwd using batch019 interpreter: both native encodings and sole source mint agree. |
| Authoritative full QC | failed | True | CHEBI:55488 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:55488 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:55488 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:55488 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:55488 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:55488 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:55488 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:55488 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:55488 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral cefuzonam identity

identity: supported. Targets: CHEBI:55488.

The native neutral structure, names, CAS attestation and independently parsed external graphs agree. The conjugate anion and sodium salt are distinct; neither is substituted into the record. The drug-granularity references retain their documented scope. Reaxys remains publicly attested but not independently graph-checked.

### Cephalosporin parent and antibacterial roles

scope: supported. Targets: CHEBI:55488.

The structural parent is broader and the retained roles justify ANTIBACTERIAL filing. Exact cefuzonam studies support antibacterial activity rather than relying on class inference alone. Clinical observations support historical drug use but do not establish a current jurisdictional approval.

### Second versus third generation terminology

evidence: unknown. Targets: CHEBI:55488.

The definition faithfully preserves ChEBI, while two inspected original papers use third generation. Preserve that discrepancy and consider explicit source qualification; no universal taxonomy was established that would justify silently replacing one label with the other. No wrong-structure finding follows.

### Optional PBP and cell-wall mechanism enrichment

completeness: unknown. Targets: CHEBI:55488.

Primary membrane competition and morphology/killing evidence provide a bounded enrichment path. The native seed has no erroneous target claim to remove. Its sodium-material evidence must remain qualified if added to a neutral record; ID50 must not become a dissociation constant or MIC, and an observed binding/morphology association must not be overstated as a uniquely proven causal chain.

### Activity observations and susceptible/resistant populations

evidence: supported. Targets: CHEBI:55488.

The 1994 MSSA/MRSA tables and 1987 clinical-isolate study support antibacterial activity but differ in population, date and testing context. Native YAML presently asserts no numeric MIC or blanket MRSA susceptibility. Population MIC quantiles are not single-isolate outcomes; minocycline and combination results are separate experiments.

### All six adopted citation dispositions

evidence: supported. Targets: CHEBI:55488.

7933531 supplies original susceptibility results; 3599391 supplies laboratory/clinical observations; 2041152 is a clinical pneumonia series; 2042464 is sodium-material cement mechanics; 3530123 is rabbit pharmacokinetics; 3329242 is a secondary review. Each is verified at the stated reading depth. None alone proves the full record or justifies importing unrelated host, material or comparator claims.

### Optional fields and scientific status

completeness: unknown. Targets: CHEBI:55488.

No producer, resistance determinant, causal graph, dataset or current clinical-status assertion is required merely because these slots exist. A semisynthetic drug source is not a producing organism; a resistant clinical isolate is not a producer. SEEDED remains appropriate pending any separate curator sign-off.

### Reproducible source and unchanged capture

ownership: supported. Targets: CHEBI:55488.

ChEBI identity and source normalization own any future definition/identifier change; primary-literature additions are curator-owned on the actual cefuzonam record. All thirteen initial input hashes remain unchanged and all focused checks pass.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

If mechanism and activity enrichment is undertaken, add the original experimental support with explicit chemical-form and endpoint qualifications.

- Preserve the exact sodium material of the 1986 L-105 paper and the unspecified counterion of other studies; do not silently turn them into neutral-acid measurements.
- Represent Table 8 as radiolabeled penicillin competition with the exact PBP and organism, ID50 units and source naming; do not relabel it as Kd or MIC. Keep morphology, viable-count and mouse efficacy experiments as separate endpoints.
- For 1994 susceptibility, retain isolate counts, collection dates, media, dilution method, MIC range/quantile and material qualification. Preserve poor MRSA susceptibility and do not import minocycline values.
- Do not promote the native record to REVIEWED without the documented separate curation/history workflow and complete native sign-off. Optional enrichment is not itself a corrective finding.

### A2

If revising the definition, preserve the observed generation-terminology difference through explicit source qualification or a structure-based description.

- Do not assert that second or third generation is universally correct on the evidence reviewed here. ChEBI and the original papers use different labels for the same active moiety.
- Keep exact chemical identity and ANTIBACTERIAL filing unchanged unless independent evidence justifies a separate correction; a terminology qualification must not become a salt/neutral identity merger.
- If a maintained correction is chosen in a later authorized task, regenerate and rerun focused validation and applicable corpus gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cefuzonam.yaml; Whole record, including all four history events. | supports | SEEDED, EXACT and ANTIBACTERIAL. The neutral formula is C16H15N7O5S4, net charge zero, full key CXHKZHZLDMQGFF-ZSDSSEDPSA-N. No molecular target, mode enum, activity observation, resistance item, producer, clinical-status assertion, causal graph or dataset is present. This is a compact identity/role seed; optional missing slots are not automatically scientific errors. |
| source | data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact ChEBI row 1007, source provenance/configuration, concept construction, synonym normalization, role filing and xref slot rules. | supports | The native identity, definition and imported fields reproduce the three-star in-scope ChEBI row. CHEBI:36047 maps to ANTIBACTERIAL while generic antimicrobial CHEBI:33281 is retained. The four synonyms exclude the duplicate label. DrugCentral/KEGG links are intentionally drug-granularity references; Wikipedia is a document reference. The row contains six literature leads but no mechanism role. No record-level primary mechanism evidence was implied by its bibliography. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:55488; Complete visible entry: definition, names, chemical descriptors, outgoing relations and manual registry/drug links. | supports | ChEBI has the same neutral structure, formula, charge, masses, key, 6R/7R and Z-oxime systematic names, INN cefuzonamum and alias cefuzoname. It explicitly distinguishes conjugate base CHEBI:55494. CAS 82219-78-1 and Reaxys 6030288 are attested; Reaxys was not independently accessed behind its service boundary. The current definition remains second generation. |
| official-graphs | https://rest.kegg.jp/get/D03432; https://drugcentral.org/drugcard/3077; https://pubchem.ncbi.nlm.nih.gov/compound/6336505; Complete KEGG entry/molfile, DrugCentral identity card and molfile/SMILES, CAS-resolved PubChem structure response. | supports | All five independently parsed encodings—KEGG molfile, DrugCentral molfile and SMILES, PubChem SMILES and InChI—reproduce the native neutral full key. PubChem 6336505 is an external cross-check, not a native identifier. DrugCentral includes sodium-related aliases and other-form links at drug granularity, but its actual parsed structure is neutral; no graph mismatch is established. KEGG supports antibacterial/cell-wall-inhibitor context, without supplying a primary experiment. |
| classes | https://www.ebi.ac.uk/chebi/CHEBI:23066; https://www.ebi.ac.uk/chebi/CHEBI:33281; https://www.ebi.ac.uk/chebi/CHEBI:36047; Official term labels and complete definitions; native roles and relation scope. | supports | CHEBI:23066 is the strictly broader cephalosporin class; CHEBI:33281 is antimicrobial agent and CHEBI:36047 is antibacterial drug. The role and filing are consistent and do not assert antiviral, fungal or producer activity. The encyclopedia link resolves to the cefuzonam topic but was not used as primary scientific evidence. |
| activity1994 | PMID:7933531; DOI:10.11553/antibiotics1968b.47.1013; https://www.jstage.jst.go.jp/article/antibiotics1968b/47/8/47_1013/_pdf; Original English main-text narrative read, including all Methods, Results and Discussion; Table 1-1 and Table 1-2 on page 1016 inspected visually. Other tabular pages were not independently transcribed. | supports | Clinical isolate collections were tested using MIC2000 broth dilution and organism-specific agar methods. Cefuzonam is listed as parenteral material from Lederle; exact counterion is not specified in the inspected Methods. Table 1-1 reports 63 MSSA isolates with cefuzonam range 0.25–2 µg/mL and MIC90 of 1; Table 1-2 reports 60 MRSA isolates with range 4 to greater than128 and MIC50/80/90 greater than128. These are population summaries, not single-strain values. No minocycline endpoint or antibacterial spectrum is transferred to cefuzonam. |
| pediatric | PMID:3599391; DOI:10.11553/antibiotics1968b.40.427; https://www.jstage.jst.go.jp/article/antibiotics1968b/40/2/40_427/_pdf; Complete indexed abstract, original introductory/material and susceptibility passages; original page 427 and its S. aureus distribution inspected visually. | partial | This study explicitly identifies cefuzonam with L-105 and reports plate-dilution susceptibility distributions for clinical isolates, plus pharmacokinetic and five-patient treatment observations. Its S. aureus panel has 26 isolates, with the distribution 0.39–1.56 µg/mL. This supports antibacterial activity and bounded clinical-use context, not a universal susceptible species claim, direct PBP binding, current regulatory approval or exact neutral material. |
| pbp | DOI:10.11250/chemotherapy1953.34.Supplement3_79; https://www.jstage.jst.go.jp/article/chemotherapy1953/34/Supplement3/34_Supplement3_79/_pdf; Original 1986 paper: abstract, exact material, Methods and selected Results/Discussion read; pages 79,82,90 and92 inspected visually, including Figure 1, Table 8 and Figures 24–26. | partial | The material is explicitly sodium cefuzonam/L-105, formula C16H14N7O5S4Na, with the carboxylate/sodium structure drawn in Figure 1. Membrane competition against 14C-penicillin G gives Table 8 ID50 values 0.013 µg/mL for E. coli K-12 PBP3 and 0.022 for S. aureus 209-PJC PBP2; these are 50% competition endpoints, not Kd or MIC. Other PBPs have different responses. Microscopy and killing experiments independently show filamentation/lysis or viable-count changes under specified concentrations. The discussion relates these phenomena; it is not a genetic rescue experiment or proof that every link is exclusive. Sodium material must remain explicit in any neutral-record enrichment. |
| pneumonia | PMID:2041152; DOI:10.11553/antibiotics1968b.44.111; https://www.jstage.jst.go.jp/article/antibiotics1968b/44/2/44_111/_pdf; Complete original abstract and narrative Methods/Results/Discussion read; tables not independently re-extracted. | context_only | Ten adults with underlying disease or complications received intravenous cefuzonam; nine were judged clinically effective. This small clinical series supports historical use, not a direct antibacterial target or modern regulatory status. The English abstract says no laboratory abnormalities, while the narrative describes changes judged unrelated to the drug; no unqualified safety statement is imported. |
| bone | PMID:2042464; DOI:10.3109/17453679108993599; https://actaorthop.org/actao/article/download/22202/26131/70676; Original abstract, material/preparation methods on page 232, concluding strength/fractography interpretation and references read. | context_only | Cefuzonam sodium (Cosmosin) is added to PMMA cement for tensile, shearing and bending tests. Mechanical strength and powder morphology are the measured endpoints; this is not a cefuzonam antibacterial assay, producer report or mechanism study. The authors call the drug third generation, differing from ChEBI terminology. |
| rabbit | PMID:3530123; DOI:10.1128/AAC.30.1.157; https://pubmed.ncbi.nlm.nih.gov/3530123/; Complete indexed original abstract and bibliographic record; ordinary PMC and ?page=1 routes inspected as retrieval failures. | context_only | The study measures cefuzonam exposure in serum and cerebrospinal fluid of 16 rabbits, including healthy and experimental meningitis groups. It reports pharmacokinetic ratios, not PBP binding or a bacterial killing concentration. Both attempted PMC routes returned HTML challenges, so exact full-text material and experimental details remain uninspected. No negative biological conclusion follows from that access limit. |
| review | PMID:3329242; DOI:10.11553/antibiotics1968b.40.1953; https://www.jstage.jst.go.jp/article/antibiotics1968b/40/12/40_1953/_pdf; Bibliographic record marks a review and has no indexed abstract. Original introductory/material and selected mechanism-summary passages, and references, were read from the free PDF. | context_only | This is a secondary review, not new primary experimentation. It explicitly uses sodium cefuzonam and supplies original-study leads, including the 1986 PBP/activity paper independently inspected here. Its early MRSA efficacy language is not treated as overriding the 1994 original clinical-isolate results; source populations and dates matter. |
| generation | PMID:7933531, Discussion page 1029; PMID:2042464, abstract page 232; CHEBI:55488 definition; Exact original wording and current official definition compared. | context_only | The 1994 activity paper and 1991 cement paper call cefuzonam a third-generation cephalosporin; ChEBI calls it second generation and KEGG places it under other cephalosporins. This confirms nonuniform classification terminology. It does not establish an alternate structure, that the acid and sodium salt belong to different generations, or that one convention is universally wrong. A source-qualified wording or structure-based definition could avoid implying consensus. |
| search | 266-inclusive-hits.txt; bounded public cefuzonam/L-105 primary-paper searches; Inclusive local exact identifier/label/key/mint search and public primary discovery. | context_only | Hidden and ignored files were included. Relevant local hits are the exact record, ChEBI row, readiness queue and generated projections; no exact corrective overlay or exclusion decision was found in the searched paths. Public searches located the original L-105 PBP paper and free publisher articles. Search snippets and historical summaries were used only as leads. The native record names no gene, protein, regulator, pathway, stress-response or dataset, so the structured-adapter trigger did not apply to its assertions. |
| validation | 266-schema.log;266-strict.log;266-strict.tsv;266-chemistry.json;266-xref-chemistry.json; Actual focused command outputs and independent official-graph parses. | supports | Schema and strict validation exit 0. Native SMILES and InChI reproduce formula, net charge, average/monoisotopic mass, R/R centres and full key. The sole ChEBI mint reproduces exactly. All five external official structure parses agree. Passing deterministic checks does not certify universal primary evidence or satisfy native REVIEWED sign-off. |

## Limits And Additional Notes

- All native fields and six adopted bibliography records were reviewed. Scientific completion remains partial because reading depth and exact assay material differ among sources. The full neutral structure is independently verified, but no isolated neutral-acid PBP assay is claimed.
- The 1994 original main-text narrative was read; Table 1-1/1-2 were inspected visually. Other tabular pages were not independently transcribed. The 1986 primary material, PBP methods and selected results/figures were inspected directly rather than treating its abstract as a complete mechanism proof.
- The 1987 pediatric paper and secondary review were read in selected original sections with their complete available abstracts or bibliography. Japanese original sections were read with their English summaries and visible experimental labels; no exhaustive clinical table audit or translation is claimed.
- The 1991 pneumonia narrative was read, but its detailed patient tables were not re-extracted. The cement paper was inspected for its exact material, mechanical-assay scope and concluding interpretation rather than a full engineering reanalysis.
- The rabbit pharmacokinetics paper was read at complete indexed-abstract depth. Both public PMC routes returned HTML challenges, so full experimental material details remain unresolved.
- Reaxys 6030288 is attested by the official ChEBI entry but was not independently accessed. No paid registry, provider research, article purchase, author contact or external mutation was used.
- The generation label is not uniform across inspected sources. The review preserves this disagreement without claiming a universal classification adjudication.
- The native record has no structured-adapter trigger. Optional PBP evidence was discovered from exact primary-paper searches; no expression-module membership or absent module is used as causal evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T122757Z-cefuzonam
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefuzonam: coherent neutral identity and antibacterial evidence with salt
  and terminology qualifications'
started_at: '2026-10-21T12:02:27Z'
finished_at: '2026-10-21T12:27:57Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the seed. Independently read the full native
    record, actual ChEBI row and source logic, inspected official chemical structures
    and original activity papers, and ran focused validators. Root captured initial
    provenance before judgment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The record consistently denotes neutral cefuzonam, with matching structure,
  names, source mint and resolved official chemical graphs. Antibacterial filing and
  retained roles are supported. Original papers support activity and PBP competition,
  but the mechanistic material is explicitly cefuzonam sodium and other assays do
  not resolve the counterion. ChEBI uses second generation while two adopted papers
  use third generation; this is preserved as a source terminology difference without
  asserting a wrong structure. No confirmed corrective finding emerged. Optional primary
  mechanism enrichment and several access or form qualifications remain. Scientific
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
  - path: data/antibiotics/antibacterial/cefuzonam.yaml
    sha256: 9711dddc12b360a10c08151a906767590bc96b4e9d8cf6055d09b40d60937479
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
- target_id: CHEBI:55488
  path: data/antibiotics/antibacterial/cefuzonam.yaml
  label: cefuzonam
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
  description: 'Entire native YAML: definition, four synonyms, broader cephalosporin
    parent, two roles, all structure descriptors, CAS/Reaxys identifiers, DrugCentral/KEGG
    drug links, encyclopedia link, sole ChEBI source concept and four history events.
    All six adopted literature records were checked, with original full text or selected
    sections read as documented.'
  selection: Queue 266; initial thirteen source/input hashes captured before assessment
    and preserved unchanged. The sole actual seed owner is the captured ChEBI row
    and its extractor/seeder path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:55488
  exclusions:
  - target: Cefuzonam sodium, the conjugate anion, other cephalosporins and minocycline
      comparator data
    reason: They are distinct structures or experimental comparators. Salt and unspecified-material
      results are retained as qualified active-moiety context rather than silently
      assigned as exact neutral-form measurements.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: No schema issues found.
  target_ids:
  - CHEBI:55488
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefuzonam.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: One exact file scanned, zero strict errors.
  target_ids:
  - CHEBI:55488
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefuzonam.yaml --out /private/tmp/am-review-session/266-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: 'Supplementary RDKit check from batch027 cwd using batch019 interpreter:
    both native encodings and sole source mint agree.'
  target_ids:
  - CHEBI:55488
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 266
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
  - CHEBI:55488
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
  - CHEBI:55488
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
  - CHEBI:55488
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
  - CHEBI:55488
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
  - CHEBI:55488
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
  - CHEBI:55488
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
  - CHEBI:55488
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
  - CHEBI:55488
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
  - CHEBI:55488
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cefuzonam.yaml
  locator: Whole record, including all four history events.
  accessed_at: '2026-10-21T12:24:58Z'
  support: supports
  summary: SEEDED, EXACT and ANTIBACTERIAL. The neutral formula is C16H15N7O5S4, net
    charge zero, full key CXHKZHZLDMQGFF-ZSDSSEDPSA-N. No molecular target, mode enum,
    activity observation, resistance item, producer, clinical-status assertion, causal
    graph or dataset is present. This is a compact identity/role seed; optional missing
    slots are not automatically scientific errors.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Exact ChEBI row 1007, source provenance/configuration, concept construction,
    synonym normalization, role filing and xref slot rules.
  accessed_at: '2026-10-21T12:24:58Z'
  support: supports
  summary: The native identity, definition and imported fields reproduce the three-star
    in-scope ChEBI row. CHEBI:36047 maps to ANTIBACTERIAL while generic antimicrobial
    CHEBI:33281 is retained. The four synonyms exclude the duplicate label. DrugCentral/KEGG
    links are intentionally drug-granularity references; Wikipedia is a document reference.
    The row contains six literature leads but no mechanism role. No record-level primary
    mechanism evidence was implied by its bibliography.
  snapshot_sha256: 1b195208727f4551fdc4f0256385308420ffbc574cc28455d2d5385e3e21ef52
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:55488
  locator: 'Complete visible entry: definition, names, chemical descriptors, outgoing
    relations and manual registry/drug links.'
  accessed_at: '2026-10-21T12:21:28Z'
  support: supports
  summary: ChEBI has the same neutral structure, formula, charge, masses, key, 6R/7R
    and Z-oxime systematic names, INN cefuzonamum and alias cefuzoname. It explicitly
    distinguishes conjugate base CHEBI:55494. CAS 82219-78-1 and Reaxys 6030288 are
    attested; Reaxys was not independently accessed behind its service boundary. The
    current definition remains second generation.
  snapshot_sha256: b269e68a5f167da7e0ad2ccbe9ebdc10dc412137af0c684ff4b919c6ef9b6d1b
- evidence_id: official-graphs
  kind: database
  reference: https://rest.kegg.jp/get/D03432; https://drugcentral.org/drugcard/3077;
    https://pubchem.ncbi.nlm.nih.gov/compound/6336505
  locator: Complete KEGG entry/molfile, DrugCentral identity card and molfile/SMILES,
    CAS-resolved PubChem structure response.
  accessed_at: '2026-10-21T12:24:58Z'
  support: supports
  summary: All five independently parsed encodings—KEGG molfile, DrugCentral molfile
    and SMILES, PubChem SMILES and InChI—reproduce the native neutral full key. PubChem
    6336505 is an external cross-check, not a native identifier. DrugCentral includes
    sodium-related aliases and other-form links at drug granularity, but its actual
    parsed structure is neutral; no graph mismatch is established. KEGG supports antibacterial/cell-wall-inhibitor
    context, without supplying a primary experiment.
  snapshot_sha256: b232ff809da80b39fb28089ae07f46d6e09b3d2f9bd3685a0597f3341cb478f4
- evidence_id: classes
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:23066; https://www.ebi.ac.uk/chebi/CHEBI:33281;
    https://www.ebi.ac.uk/chebi/CHEBI:36047
  locator: Official term labels and complete definitions; native roles and relation
    scope.
  accessed_at: '2026-10-21T12:21:28Z'
  support: supports
  summary: CHEBI:23066 is the strictly broader cephalosporin class; CHEBI:33281 is
    antimicrobial agent and CHEBI:36047 is antibacterial drug. The role and filing
    are consistent and do not assert antiviral, fungal or producer activity. The encyclopedia
    link resolves to the cefuzonam topic but was not used as primary scientific evidence.
  snapshot_sha256: ac2ebd34062bbb7883ee33d035e4a82578a3ee0ac7750480c7f3c232c1f3b073
- evidence_id: activity1994
  kind: primary_source
  reference: PMID:7933531; DOI:10.11553/antibiotics1968b.47.1013; https://www.jstage.jst.go.jp/article/antibiotics1968b/47/8/47_1013/_pdf
  locator: Original English main-text narrative read, including all Methods, Results
    and Discussion; Table 1-1 and Table 1-2 on page 1016 inspected visually. Other
    tabular pages were not independently transcribed.
  accessed_at: '2026-10-21T12:22:06Z'
  support: supports
  summary: Clinical isolate collections were tested using MIC2000 broth dilution and
    organism-specific agar methods. Cefuzonam is listed as parenteral material from
    Lederle; exact counterion is not specified in the inspected Methods. Table 1-1
    reports 63 MSSA isolates with cefuzonam range 0.25–2 µg/mL and MIC90 of 1; Table
    1-2 reports 60 MRSA isolates with range 4 to greater than128 and MIC50/80/90 greater
    than128. These are population summaries, not single-strain values. No minocycline
    endpoint or antibacterial spectrum is transferred to cefuzonam.
  snapshot_sha256: e012c9083e180112ab4cf5451b997737637bc9499756874196477f04c92f2256
- evidence_id: pediatric
  kind: primary_source
  reference: PMID:3599391; DOI:10.11553/antibiotics1968b.40.427; https://www.jstage.jst.go.jp/article/antibiotics1968b/40/2/40_427/_pdf
  locator: Complete indexed abstract, original introductory/material and susceptibility
    passages; original page 427 and its S. aureus distribution inspected visually.
  accessed_at: '2026-10-21T12:22:06Z'
  support: partial
  summary: This study explicitly identifies cefuzonam with L-105 and reports plate-dilution
    susceptibility distributions for clinical isolates, plus pharmacokinetic and five-patient
    treatment observations. Its S. aureus panel has 26 isolates, with the distribution
    0.39–1.56 µg/mL. This supports antibacterial activity and bounded clinical-use
    context, not a universal susceptible species claim, direct PBP binding, current
    regulatory approval or exact neutral material.
  snapshot_sha256: 845562b0cf9d133db05b03584edcd6d723c6425e783001acaa581dd026b1d3b9
- evidence_id: pbp
  kind: primary_source
  reference: DOI:10.11250/chemotherapy1953.34.Supplement3_79; https://www.jstage.jst.go.jp/article/chemotherapy1953/34/Supplement3/34_Supplement3_79/_pdf
  locator: 'Original 1986 paper: abstract, exact material, Methods and selected Results/Discussion
    read; pages 79,82,90 and92 inspected visually, including Figure 1, Table 8 and
    Figures 24–26.'
  accessed_at: '2026-10-21T12:22:06Z'
  support: partial
  summary: The material is explicitly sodium cefuzonam/L-105, formula C16H14N7O5S4Na,
    with the carboxylate/sodium structure drawn in Figure 1. Membrane competition
    against 14C-penicillin G gives Table 8 ID50 values 0.013 µg/mL for E. coli K-12
    PBP3 and 0.022 for S. aureus 209-PJC PBP2; these are 50% competition endpoints,
    not Kd or MIC. Other PBPs have different responses. Microscopy and killing experiments
    independently show filamentation/lysis or viable-count changes under specified
    concentrations. The discussion relates these phenomena; it is not a genetic rescue
    experiment or proof that every link is exclusive. Sodium material must remain
    explicit in any neutral-record enrichment.
  snapshot_sha256: 368ec88b38c1acc601a18f3198e4096ddba6f60da25f2f4586aaf082764c2175
- evidence_id: pneumonia
  kind: primary_source
  reference: PMID:2041152; DOI:10.11553/antibiotics1968b.44.111; https://www.jstage.jst.go.jp/article/antibiotics1968b/44/2/44_111/_pdf
  locator: Complete original abstract and narrative Methods/Results/Discussion read;
    tables not independently re-extracted.
  accessed_at: '2026-10-21T12:22:06Z'
  support: context_only
  summary: Ten adults with underlying disease or complications received intravenous
    cefuzonam; nine were judged clinically effective. This small clinical series supports
    historical use, not a direct antibacterial target or modern regulatory status.
    The English abstract says no laboratory abnormalities, while the narrative describes
    changes judged unrelated to the drug; no unqualified safety statement is imported.
  snapshot_sha256: 3a32e9d345f2c471af406517a6358fa64cafb66f3a25c7ed681aad4f14f90795
- evidence_id: bone
  kind: primary_source
  reference: PMID:2042464; DOI:10.3109/17453679108993599; https://actaorthop.org/actao/article/download/22202/26131/70676
  locator: Original abstract, material/preparation methods on page 232, concluding
    strength/fractography interpretation and references read.
  accessed_at: '2026-10-21T12:23:12Z'
  support: context_only
  summary: Cefuzonam sodium (Cosmosin) is added to PMMA cement for tensile, shearing
    and bending tests. Mechanical strength and powder morphology are the measured
    endpoints; this is not a cefuzonam antibacterial assay, producer report or mechanism
    study. The authors call the drug third generation, differing from ChEBI terminology.
  snapshot_sha256: 10f4a85a45f795d33f588224c3ec7951ed3c40356fa7ae74b999e689f5031360
- evidence_id: rabbit
  kind: primary_source
  reference: PMID:3530123; DOI:10.1128/AAC.30.1.157; https://pubmed.ncbi.nlm.nih.gov/3530123/
  locator: Complete indexed original abstract and bibliographic record; ordinary PMC
    and ?page=1 routes inspected as retrieval failures.
  accessed_at: '2026-10-21T12:21:28Z'
  support: context_only
  summary: The study measures cefuzonam exposure in serum and cerebrospinal fluid
    of 16 rabbits, including healthy and experimental meningitis groups. It reports
    pharmacokinetic ratios, not PBP binding or a bacterial killing concentration.
    Both attempted PMC routes returned HTML challenges, so exact full-text material
    and experimental details remain uninspected. No negative biological conclusion
    follows from that access limit.
  snapshot_sha256: 97a6605192b0fc372944c225401975c7fca2b685360ff4b7c7ddb37917665170
- evidence_id: review
  kind: database
  reference: PMID:3329242; DOI:10.11553/antibiotics1968b.40.1953; https://www.jstage.jst.go.jp/article/antibiotics1968b/40/12/40_1953/_pdf
  locator: Bibliographic record marks a review and has no indexed abstract. Original
    introductory/material and selected mechanism-summary passages, and references,
    were read from the free PDF.
  accessed_at: '2026-10-21T12:22:06Z'
  support: context_only
  summary: This is a secondary review, not new primary experimentation. It explicitly
    uses sodium cefuzonam and supplies original-study leads, including the 1986 PBP/activity
    paper independently inspected here. Its early MRSA efficacy language is not treated
    as overriding the 1994 original clinical-isolate results; source populations and
    dates matter.
  snapshot_sha256: f574629ef7880c49163f4c9f3da46f7181dfe33c1f9c431bcc0e8ad5cbae25c0
- evidence_id: generation
  kind: primary_source
  reference: PMID:7933531, Discussion page 1029; PMID:2042464, abstract page 232;
    CHEBI:55488 definition
  locator: Exact original wording and current official definition compared.
  accessed_at: '2026-10-21T12:22:06Z'
  support: context_only
  summary: The 1994 activity paper and 1991 cement paper call cefuzonam a third-generation
    cephalosporin; ChEBI calls it second generation and KEGG places it under other
    cephalosporins. This confirms nonuniform classification terminology. It does not
    establish an alternate structure, that the acid and sodium salt belong to different
    generations, or that one convention is universally wrong. A source-qualified wording
    or structure-based definition could avoid implying consensus.
  snapshot_sha256: e012c9083e180112ab4cf5451b997737637bc9499756874196477f04c92f2256
- evidence_id: search
  kind: search
  reference: 266-inclusive-hits.txt; bounded public cefuzonam/L-105 primary-paper
    searches
  locator: Inclusive local exact identifier/label/key/mint search and public primary
    discovery.
  accessed_at: '2026-10-21T12:24:58Z'
  support: context_only
  summary: Hidden and ignored files were included. Relevant local hits are the exact
    record, ChEBI row, readiness queue and generated projections; no exact corrective
    overlay or exclusion decision was found in the searched paths. Public searches
    located the original L-105 PBP paper and free publisher articles. Search snippets
    and historical summaries were used only as leads. The native record names no gene,
    protein, regulator, pathway, stress-response or dataset, so the structured-adapter
    trigger did not apply to its assertions.
  snapshot_sha256: 375db309a5cd06537f216c65cd91a4948de8cb0414ca0614263f399a6b42ebd4
  search_scope: rg --no-ignore --hidden -n -F for CHEBI:55488, cefuzonam, full InChIKey
    and source mint across data, curation, conf, scripts, src, docs, .claude, reviews
    and reports; public cefuzonam/L-105 plus penicillin-binding proteins, adopted
    titles and generation terms on 2026-10-21.
- evidence_id: validation
  kind: validation
  reference: 266-schema.log;266-strict.log;266-strict.tsv;266-chemistry.json;266-xref-chemistry.json
  locator: Actual focused command outputs and independent official-graph parses.
  accessed_at: '2026-10-21T12:24:58Z'
  support: supports
  summary: Schema and strict validation exit 0. Native SMILES and InChI reproduce
    formula, net charge, average/monoisotopic mass, R/R centres and full key. The
    sole ChEBI mint reproduces exactly. All five external official structure parses
    agree. Passing deterministic checks does not certify universal primary evidence
    or satisfy native REVIEWED sign-off.
  snapshot_sha256: 2c0e49d008d98605b2a9cb0bcc066b67419bce0c346ed48ee96d9a8432cead67
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral cefuzonam identity
  outcome: supported
  summary: The native neutral structure, names, CAS attestation and independently
    parsed external graphs agree. The conjugate anion and sodium salt are distinct;
    neither is substituted into the record. The drug-granularity references retain
    their documented scope. Reaxys remains publicly attested but not independently
    graph-checked.
  target_ids:
  - CHEBI:55488
  evidence_ids:
  - record
  - chebi
  - official-graphs
  - validation
- assessment_id: classification
  area: scope
  topic: Cephalosporin parent and antibacterial roles
  outcome: supported
  summary: The structural parent is broader and the retained roles justify ANTIBACTERIAL
    filing. Exact cefuzonam studies support antibacterial activity rather than relying
    on class inference alone. Clinical observations support historical drug use but
    do not establish a current jurisdictional approval.
  target_ids:
  - CHEBI:55488
  evidence_ids:
  - source
  - classes
  - activity1994
  - pediatric
  - pneumonia
- assessment_id: generation
  area: evidence
  topic: Second versus third generation terminology
  outcome: unknown
  summary: The definition faithfully preserves ChEBI, while two inspected original
    papers use third generation. Preserve that discrepancy and consider explicit source
    qualification; no universal taxonomy was established that would justify silently
    replacing one label with the other. No wrong-structure finding follows.
  target_ids:
  - CHEBI:55488
  evidence_ids:
  - chebi
  - generation
- assessment_id: mechanism
  area: completeness
  topic: Optional PBP and cell-wall mechanism enrichment
  outcome: unknown
  summary: Primary membrane competition and morphology/killing evidence provide a
    bounded enrichment path. The native seed has no erroneous target claim to remove.
    Its sodium-material evidence must remain qualified if added to a neutral record;
    ID50 must not become a dissociation constant or MIC, and an observed binding/morphology
    association must not be overstated as a uniquely proven causal chain.
  target_ids:
  - CHEBI:55488
  evidence_ids:
  - record
  - pbp
  - official-graphs
- assessment_id: activity
  area: evidence
  topic: Activity observations and susceptible/resistant populations
  outcome: supported
  summary: The 1994 MSSA/MRSA tables and 1987 clinical-isolate study support antibacterial
    activity but differ in population, date and testing context. Native YAML presently
    asserts no numeric MIC or blanket MRSA susceptibility. Population MIC quantiles
    are not single-isolate outcomes; minocycline and combination results are separate
    experiments.
  target_ids:
  - CHEBI:55488
  evidence_ids:
  - activity1994
  - pediatric
  - review
- assessment_id: bibliography
  area: evidence
  topic: All six adopted citation dispositions
  outcome: supported
  summary: 7933531 supplies original susceptibility results; 3599391 supplies laboratory/clinical
    observations; 2041152 is a clinical pneumonia series; 2042464 is sodium-material
    cement mechanics; 3530123 is rabbit pharmacokinetics; 3329242 is a secondary review.
    Each is verified at the stated reading depth. None alone proves the full record
    or justifies importing unrelated host, material or comparator claims.
  target_ids:
  - CHEBI:55488
  evidence_ids:
  - activity1994
  - pediatric
  - pneumonia
  - bone
  - rabbit
  - review
- assessment_id: remaining
  area: completeness
  topic: Optional fields and scientific status
  outcome: unknown
  summary: No producer, resistance determinant, causal graph, dataset or current clinical-status
    assertion is required merely because these slots exist. A semisynthetic drug source
    is not a producing organism; a resistant clinical isolate is not a producer. SEEDED
    remains appropriate pending any separate curator sign-off.
  target_ids:
  - CHEBI:55488
  evidence_ids:
  - record
  - source
  - activity1994
  - pbp
- assessment_id: ownership
  area: ownership
  topic: Reproducible source and unchanged capture
  outcome: supported
  summary: ChEBI identity and source normalization own any future definition/identifier
    change; primary-literature additions are curator-owned on the actual cefuzonam
    record. All thirteen initial input hashes remain unchanged and all focused checks
    pass.
  target_ids:
  - CHEBI:55488
  evidence_ids:
  - source
  - search
  - validation
findings: []
actions:
- action_id: A1
  description: If mechanism and activity enrichment is undertaken, add the original
    experimental support with explicit chemical-form and endpoint qualifications.
  finding_ids: []
  target_ids:
  - CHEBI:55488
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefuzonam.yaml
    role: Curator-owned claim-specific primary evidence and optional activity/target
      additions
  acceptance_checks:
  - Preserve the exact sodium material of the 1986 L-105 paper and the unspecified
    counterion of other studies; do not silently turn them into neutral-acid measurements.
  - Represent Table 8 as radiolabeled penicillin competition with the exact PBP and
    organism, ID50 units and source naming; do not relabel it as Kd or MIC. Keep morphology,
    viable-count and mouse efficacy experiments as separate endpoints.
  - For 1994 susceptibility, retain isolate counts, collection dates, media, dilution
    method, MIC range/quantile and material qualification. Preserve poor MRSA susceptibility
    and do not import minocycline values.
  - Do not promote the native record to REVIEWED without the documented separate curation/history
    workflow and complete native sign-off. Optional enrichment is not itself a corrective
    finding.
- action_id: A2
  description: If revising the definition, preserve the observed generation-terminology
    difference through explicit source qualification or a structure-based description.
  finding_ids: []
  target_ids:
  - CHEBI:55488
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted definition owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible definition normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition emission
  acceptance_checks:
  - Do not assert that second or third generation is universally correct on the evidence
    reviewed here. ChEBI and the original papers use different labels for the same
    active moiety.
  - Keep exact chemical identity and ANTIBACTERIAL filing unchanged unless independent
    evidence justifies a separate correction; a terminology qualification must not
    become a salt/neutral identity merger.
  - If a maintained correction is chosen in a later authorized task, regenerate and
    rerun focused validation and applicable corpus gates.
limitations:
- All native fields and six adopted bibliography records were reviewed. Scientific
  completion remains partial because reading depth and exact assay material differ
  among sources. The full neutral structure is independently verified, but no isolated
  neutral-acid PBP assay is claimed.
- The 1994 original main-text narrative was read; Table 1-1/1-2 were inspected visually.
  Other tabular pages were not independently transcribed. The 1986 primary material,
  PBP methods and selected results/figures were inspected directly rather than treating
  its abstract as a complete mechanism proof.
- The 1987 pediatric paper and secondary review were read in selected original sections
  with their complete available abstracts or bibliography. Japanese original sections
  were read with their English summaries and visible experimental labels; no exhaustive
  clinical table audit or translation is claimed.
- The 1991 pneumonia narrative was read, but its detailed patient tables were not
  re-extracted. The cement paper was inspected for its exact material, mechanical-assay
  scope and concluding interpretation rather than a full engineering reanalysis.
- The rabbit pharmacokinetics paper was read at complete indexed-abstract depth. Both
  public PMC routes returned HTML challenges, so full experimental material details
  remain unresolved.
- Reaxys 6030288 is attested by the official ChEBI entry but was not independently
  accessed. No paid registry, provider research, article purchase, author contact
  or external mutation was used.
- The generation label is not uniform across inspected sources. The review preserves
  this disagreement without claiming a universal classification adjudication.
- The native record has no structured-adapter trigger. Optional PBP evidence was discovered
  from exact primary-paper searches; no expression-module membership or absent module
  is used as causal evidence.
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
